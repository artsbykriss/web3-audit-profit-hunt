# Final fund-draining master — deployment trace

**Generated:** 2026-11-11  
**Scope:** all critical/high findings classified as profit-plausible across Stage 1, the prior campaign, and the broad prior corpus. DoS-only findings are excluded.

## Headline

| Metric | Value |
|---|---:|
| Clean fund-draining rows (C/H, profit yes/uncertain) | 7,479 |
| Rows with a deployment address | 6,254 |
| `FOUND` (named contract matched) | 3,510 |
| `PARTIAL` (project/core found, exact audited contract unpublished) | 3,024 |
| `NOT_DEPLOYED` (affirmative evidence) | 345 |
| `NOT_APPLICABLE` (node/pallet/circuit/off-chain) | 432 |
| `NOT_FOUND` (identity unresolved) | 168 |

`NOT_FOUND` fell from ~3,146 findings / 1,444 projects at the end of Stage 2 to **168 findings / 101 projects** after the re-trace. That is inside the 100–200 target.

## What changed in the re-trace

- 1,748 no-address projects were re-investigated with a strict ladder: project docs, Jina Reader (JS/Cloudflare), Etherscan V2, Alchemy/Infura/Ankr RPC, Blockscout, Sourcify, DefiLlama, Wayback and GitHub.
- 94 R1/R2 batches plus 9 U1 unknown-group batches plus 20 N2 cleanup batches were run. Cloudflare/403/JS was treated as a tooling failure, never a conclusion.
- `PARTIAL` is the dominant remaining state: the project is live, but the exact audited contract/instance is not published. That is a real evidence ceiling, not a search failure.

## CSV columns

`finding_uid`, `finding_title`, `severity`, `profit_confirmed`, `profit_path`, `project`, `protocol_category`, `chain`, `contract_name`, `deployment_address`, `address_role`, `proxy`, `implementation`, `project_addresses`, `trace_status`, `confidence`, `evidence_url`, `report_url`, `source_corpus`, `notes`, `last_checked`.

## Files

- `FINAL_FUND_DRAINING.csv` — the clean deliverable (C/H, fund-draining/profit, no DoS).
- `FINAL_MASTER.csv` — every row including `profit_confirmed=uncertain` and lower severities.
- `FINAL_SUMMARY.json` — machine-readable counts.
- `retrace/RETRACE.md` — the protocol used for the final pass.
- `retrace/index/retrace_projects.csv` — the 1,748-project worklist.
- `retrace/results.tar.gz` — all re-trace batch outputs with evidence URLs.

## Caveats

- `FOUND` means the contract is deployed; it does not mean the vulnerable path is unpatched. Stage 3 must check live bytecode/state.
- `PARTIAL` means the project/core is deployed but the exact audited instance is unpublished or indistinguishable; the address is a project anchor, not a byte-confirmed match.
- `NOT_DEPLOYED` requires two independent evidence URLs; `NOT_APPLICABLE` means no deployable contract exists by design.
- `profit_confirmed=uncertain` rows are kept because the source text was silent; they need a Stage 3 read before being treated as drains.
- No transactions, keys, audits or patch judgments were made.