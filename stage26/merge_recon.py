#!/usr/bin/env python3
"""Merge accepted Stage 2.6 recon results into the Stage 3 target corpus.

Reads stage26/results/*.json, takes every deployment that is not already a Stage 3
target for that project, and appends it as a new target plus new 3-target batches.

Idempotent: state in stage26/index/merge_state.json prevents re-adding an address.
Dry-run by default; pass --apply to write.

    python3 stage26/merge_recon.py            # show what would be added
    python3 stage26/merge_recon.py --apply    # write targets + batches
"""
import csv, glob, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
TARGETS = f"{ROOT}/stage3/index/stage3_targets.csv"
BATCHES = f"{ROOT}/stage3/batches"
STATE = f"{ROOT}/stage26/index/merge_state.json"
NON_EVM = {"solana", "cosmos", "osmosis", "sui", "aptos", "starknet", "ton", "cardano",
           "near", "stellar", "algorand", "tezos", "polkadot", "kusama", "multiversx",
           "elrond", "flow", "internet computer", "icp", "radix", "hedera", "xrpl"}

apply = "--apply" in sys.argv

rows = list(csv.DictReader(open(TARGETS)))
fields = list(rows[0].keys())
seen = {(r["project"].lower(), r["address"].lower()) for r in rows if r["address"]}
next_target = max(int(r["target_id"].split("-")[1]) for r in rows) + 1
next_batch = max(int(os.path.basename(p)[3:-5]) for p in glob.glob(f"{BATCHES}/S3-*.json")) + 1

state = json.load(open(STATE)) if os.path.exists(STATE) else {"added": [], "batches": []}
added_keys = set(state["added"])

new = []
for f in sorted(glob.glob(f"{ROOT}/stage26/results/*.json")):
    for u in json.load(open(f)).get("units", []):
        for d in u.get("deployments", []):
            addr = (d.get("address") or "").strip()
            if not addr or d.get("status") == "REJECTED":
                continue
            key = f"{u['project'].lower()}|{addr.lower()}"
            if key in added_keys or (u["project"].lower(), addr.lower()) in seen:
                continue
            chain = d.get("chain") or u.get("chain") or "unknown"
            is_evm = str(chain).lower() not in NON_EVM
            new.append({
                "target_id": f"S3-{next_target:04d}",
                "project": u["project"], "chain": chain, "address": addr,
                "contract": d.get("role", "core"),
                "evm": str(is_evm),
                "trace_status": "RECON_" + (u.get("status") or "ANCHORED"),
                "findings": u.get("n_findings", ""),
                "critical": u.get("critical", ""), "high": u.get("high", ""),
                "profit_yes": "", "profit_uncertain": "",
                "priority": "4" if is_evm else "5",
                "headline": (u.get("titles") or "").split(" | ")[0],
                "titles": u.get("titles", ""), "categories": "",
                "sources": "stage26/recon",
                "uids": u.get("uids", ""), "report_urls": u.get("report_urls", ""),
                "evidence_urls": u.get("evidence_urls", "") + ";" + (d.get("source") or ""),
                "project_addresses": u.get("known_addresses", ""),
                "slug": f"recon_{u['unit'].lower().replace('-', '_')}_{addr[:10].lower()}",
                "chain_id": d.get("chain_id", ""),
                "bytecode_match": d.get("bytecode_match", ""),
            })
            added_keys.add(key)
            next_target += 1

print(f"new targets: {len(new)}")
for r in new:
    print(f"  {r['target_id']} p{r['priority']} {r['project'][:44]:44} {r['chain'][:14]:14} {r['address']}")
if not apply:
    print("\ndry run — pass --apply to write")
    sys.exit(0)

if not new:
    sys.exit(0)

with open(TARGETS, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writerows(new)

made = []
for i in range(0, len(new), 3):
    bid = f"S3-{next_batch:04d}"
    chunk = new[i:i+3]
    json.dump({"batch_id": bid, "count": len(chunk), "targets": chunk},
              open(f"{BATCHES}/{bid}.json", "w"), indent=1)
    made.append(bid)
    next_batch += 1

state["added"] = sorted(added_keys)
state["batches"] += made
json.dump(state, open(STATE, "w"), indent=1)
print(f"\nappended {len(new)} targets; batches: {made[0]}..{made[-1]} ({len(made)})")
