#!/usr/bin/env python3
"""Rebuild stage3/MASTER_LOG.csv from every stage3/results/S3-*.json.

Canonical aggregation (handover §7):
- key targets by target_id, last result wins
- map target_id -> batch_id from stage3/batches/
- preserve existing economic_id assignments; assign new EX-NN to new extractables
- unique extractable value = first row per economic_id

Dry-run by default. --apply writes MASTER_LOG.csv after a .bak backup.
"""
import csv, glob, json, os, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(ROOT, "MASTER_LOG.csv")
BATCHES = os.path.join(ROOT, "batches")
RESULTS = os.path.join(ROOT, "results")
FIELDS = ["batch_id", "target_id", "project", "chain", "address", "headline_status",
          "verdict", "economic_id", "extractability_usd", "confidence", "gate",
          "new_bugs", "folder_removed", "notes"]

apply = "--apply" in sys.argv

target_batch = {}
for p in glob.glob(os.path.join(BATCHES, "S3-*.json")):
    d = json.load(open(p))
    for t in d["targets"]:
        target_batch[t["target_id"]] = d["batch_id"]

existing_econ = {}
if os.path.exists(LOG):
    for r in csv.DictReader(open(LOG)):
        if r.get("economic_id"):
            existing_econ[r["target_id"]] = r["economic_id"]
next_ex = max([int(e.split("-")[1]) for e in existing_econ.values()] or [0]) + 1

rows = {}
for p in sorted(glob.glob(os.path.join(RESULTS, "S3-*.json"))):
    for t in json.load(open(p)).get("targets", []):
        if t.get("target_id"):
            rows[t["target_id"]] = t

out, econ_count = [], {}
for tid, t in sorted(rows.items(), key=lambda kv: target_batch.get(kv[0], "~")):
    verdict = t.get("verdict", "")
    econ = ""
    if verdict == "EXTRACTABLE":
        econ = existing_econ.get(tid)
        if not econ:
            econ = f"EX-{next_ex:02d}"
            next_ex += 1
            existing_econ[tid] = econ
        econ_count[econ] = econ_count.get(econ, 0) + 1
    out.append({
        "batch_id": target_batch.get(tid, ""),
        "target_id": tid,
        "project": t.get("project", ""),
        "chain": t.get("chain", ""),
        "address": t.get("address", ""),
        "headline_status": t.get("headline_status", ""),
        "verdict": verdict,
        "economic_id": econ,
        "extractability_usd": t.get("extractability_usd", 0),
        "confidence": t.get("extractability_confidence", ""),
        "gate": t.get("gate", ""),
        "new_bugs": len(t.get("new_bugs") or []),
        "folder_removed": t.get("folder_removed", ""),
        "notes": (t.get("notes") or "").replace("\n", " "),
    })

seen = set()
unique_usd = 0.0
for r in out:
    if r["verdict"] == "EXTRACTABLE" and r["economic_id"] not in seen:
        seen.add(r["economic_id"])
        unique_usd += float(r["extractability_usd"] or 0)

print(f"targets: {len(out)}  batches: {len({r['batch_id'] for r in out})}")
print(f"extractable rows: {sum(1 for r in out if r['verdict'] == 'EXTRACTABLE')}  "
      f"unique economic_ids: {len(seen)}  duplicate rows: {sum(1 for c in econ_count.values() if c > 1)}")
print(f"unique extractable USD: {unique_usd:,.2f}")
neg = [r for r in out if r["verdict"] == "NOT_EXTRACTABLE"]
print(f"negatives: {len(neg)}  non-HIGH negatives: {sum(1 for r in neg if r['confidence'] != 'HIGH')}")

if not apply:
    print("dry run — pass --apply to write")
    sys.exit(0)

shutil.copy(LOG, LOG + ".bak")
with open(LOG, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(out)
print(f"wrote {LOG} (backup {LOG}.bak)")
