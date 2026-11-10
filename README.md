# Web3 Audit Profit Hunt

**Stage 1 — critical/high triage for external, unprivileged profit.** Complete: 24,966 clusters triaged.
**Stage 2 — finding reconfirmation and deployment address trace.** Complete: 6,792 findings, 3,837 mapped to 1,696 deployment addresses.

## Scope

Two public audit corpora:

1. **GitHub — `DicksonWu654/web3-audit-findings`** (snapshot v1.3.0, 2026-10-22): 175,640 finding occurrences, 13,522 reports, 63 publishers.
2. **HuggingFace — `daveytea/x23-solidity-vulnerabilities-audit-findings`**: 55,134 findings, 4,395 reports.

The raw corpora are **not** redistributed here; only analysis outputs, indexes and reports are. Publisher text retains its own rights; check the original source before relying on a finding.

## Stage 1 — profit triage

- Unified critical/high dataset: **30,622 occurrences → 24,983 clusters** (5,084 Critical / 19,899 High).
- 24,966 clusters were batched and triaged; the 17 unbatched clusters are DoS/gas-only items with no profit path.
- Classification: **6,792 `PROFIT_PLAUSIBLE`**, 6,639 `DOS_ONLY`, 4,874 `UNCLEAR`, 4,709 `UNECONOMIC`, 1,952 `PRIVILEGED`.
- Each `PROFIT_PLAUSIBLE` record carries attacker, entry point, value at risk, exploit path, preconditions, gate, confidence and a Stage 2 target.

Start with `stage1/index/stage1_master_profit.csv` (6,792 rows). Project rollup: `stage1/index/stage1_projects.csv`. Repo/commit/file/function leads: `stage1/index/stage1_targets.csv`.

## Stage 2 — deployment trace

Stage 2 asks two questions per finding:

1. Is the reported path **profit or DoS** for an external unprivileged actor?
2. **Which deployed contract** does it concern?

Result: **3,837 of 6,792 findings (56.5%)** map to at least one address; 1,696 unique addresses; 2,399 project/chain/contract/address target rows.

| Verdict | Findings |
|---|---:|
| `profit_confirmed=yes` | 6,598 |
| `profit_confirmed=no` (DoS only) | 44 |
| `profit_confirmed=uncertain` | 150 |
| `trace_status=FOUND` | 1,968 |
| `trace_status=PARTIAL` | 1,678 |
| `trace_status=NOT_FOUND` | 3,146 |

**Start with `stage2/STAGE2_MASTER.md`.** It contains the method, coverage, every deployment target, every no-address group with its reason, the DoS refutations, and the earlier campaign findings. `stage2/STAGE2_SUMMARY.md` is the short hand-off.

**Important:** address existence is not exploitability. Stage 2 does not judge patch status, bytecode, TVL, or whether the vulnerable path is reachable. That is Stage 3.

## Repository layout

```
stage1/
  STAGE1.md, STAGE1B.md, STAGE1D.md   # triage protocols
  results.tar.gz                      # all 24,966 classifications (waves 1, 1B, 1C, 1D)
  index/stage1_master_profit.csv      # 6,792 profit-plausible findings
  index/stage1_projects.csv           # project rollup
  index/stage1_targets.csv            # repo/commit/file/function leads
  index/ch_master_all.csv.gz          # 30,622 critical/high occurrences
  index/ch_master_clusters.csv.gz     # 24,983 unique clusters
stage2/
  STAGE2.md                           # tracing protocol
  STAGE2_MASTER.md                    # full Stage 2 report
  STAGE2_SUMMARY.md                   # short hand-off
  results.tar.gz                      # 139 batch outputs with evidence URLs
  index/stage2_master.csv             # finding -> chain/contract/address
  index/stage2_targets.csv            # target -> finding_uid list
  index/stage2_addresses.csv          # project -> address list with evidence URL
  index/stage2_summary.json           # counts
prior/
  PRIOR_TRACE.md                      # protocol for the prior-campaign layer
  PRIOR_MASTER.md                     # 615 unpublished/un-hunted findings traced
  results.tar.gz                      # 13 batch outputs
  index/prior_master.csv              # finding -> address
  index/prior_targets.csv             # target -> finding list
legacy/
  EXTRACTABLE_VALUE_MASTER.md         # earlier campaign's live/gated findings
```

## Method notes and limits

- `FOUND` = the named vulnerable contract matched a deployed address; `PARTIAL` = project/core found, exact audited contract unpublished or indistinguishable; `NOT_FOUND` = no live deployment established from public evidence.
- Multi-instance protocols (per-pool, per-market, per-DAO) are recorded at the factory/core or a representative instance.
- `NOT_FOUND` is not proof of absence: several explorer APIs were Cloudflare/key-gated during the pass, and some projects publish no address.
- No transactions, private keys, audits, or patch judgments were made. All work was read-only public research.

## Attribution

- GitHub corpus: `https://github.com/DicksonWu654/web3-audit-findings` (CC BY 4.0 metadata; publisher text retains its own rights).
- HuggingFace dataset: `https://huggingface.co/datasets/daveytea/x23-solidity-vulnerabilities-audit-findings` (CC BY 4.0 compilation; original report text attributable to its source).
- Finding-level source URLs are preserved in the results and indexes.
