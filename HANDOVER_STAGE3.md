# Stage 3 handover brief — live fund-draining audit

**Prepared:** 2026-11-13  
**Prepared for:** the next agent taking over the Stage 3 campaign  
**Workspace:** `/workspaces/CA`

---

## 1. What this campaign is

We are auditing every on-chain deployment found in Stage 1/2 for **fund-draining bugs an external, unprivileged attacker can actually profit from**. The headline finding is the priority, but every target gets an all-round audit of the live contract/program, because a patched headline can coexist with a different live drain.

Stage 3 is **read-only**: no broadcasts, no private keys, no mainnet transactions. PoCs run on local forks/validators.

The campaign has three layers:

1. **Stage 1** — triage of 24,983 critical/high clusters → 6,792 profit-plausible findings.
2. **Stage 2** — deployment tracing → 6,254 findings with a deployment address → 3,685 unique project/address targets, plus 131 Stage 2.5 targets = 3,816.
3. **Stage 3** — live audit of those 3,816 targets.

**Stage 2.5** traced the 556 no-address `PARTIAL`/`NOT_FOUND` findings: 317 units → 45 `FOUND`, 177 `PARTIAL`, 7 `NOT_DEPLOYED`, 88 `NOT_FOUND`; 154 unique addresses, of which 131 new targets (102 priority 4 EVM, 29 priority 5 non-EVM) were added in batches **S3-1231..S3-1274**.

---

## 2. Current status

| Metric | Count |
|---|---:|
| Stage 3 targets total | 3,816 |
| Targets audited | **1,452** |
| `NOT_EXTRACTABLE` | 1,435 |
| Unique extractables | **25** |
| Extractable target rows | 31 (6 duplicates) |
| Unique extractable value | **~$587,422** |

### Coverage by priority

| Priority | Meaning | Total | Audited | Remaining |
|---|---|---:|---:|---:|
| 1 | critical `FOUND` EVM | 588 | 588 | 0 |
| 2 | `FOUND` EVM highs | 1,571 | 420 | **1,151** |
| 3 | `FOUND` non-EVM | 260 | 260 | 0 |
| 4 | `PARTIAL` EVM | 1,184 | 0 | **1,184** |
| 5 | `PARTIAL` non-EVM | 213 | 184 | **29** |

**Remaining: 2,364 targets** (1,151 priority 2 + 1,184 priority 4 + 29 priority 5).

Wave math with **N agents per wave** and **3 targets per agent** (constant):

```
targets per wave = 3 × N
waves remaining  = ceil(2,364 / (3 × N))
```

| Agents/wave | Targets/wave | Waves remaining |
|---:|---:|---:|
| 5 | 15 | 158 |
| 10 | 30 | 79 |
| 15 | 45 | 53 |
| 20 | 60 | 40 |

If priority 2 and priority 4/5 are run separately (not mixed in a wave), use 39 + 41 = 80 waves at 10 agents.

### Known gap: 148 units with no deployment at all

Stage 2.5 resolved 317 units. The `PARTIAL` verdict has two very different sub-cases, and only one of
them reached Stage 3:

| Stage 2.5 status | Units | With address | Stage 3 targets |
|---|---:|---:|---:|
| `FOUND` | 45 | 45 | — (already targets) |
| `PARTIAL` — anchor found | 29 | 29 | 131 |
| `PARTIAL` — nothing found | **148** | **0** | **0** |
| `NOT_DEPLOYED` | 7 | 0 | 0 |
| `NOT_FOUND` | 88 | 0 | 0 |

Those **148 units are auditable findings with no contract to audit**. They are outside the 3,816
targets. Stage 2.6 (`stage26/`) is the queue that closes this gap, and it also re-derives the
deployment for the 45 `FOUND` and 29 anchored units, because a single anchor is not proof.

---

## 3. The 14 extractables

All dossiers are in `/workspaces/CA/extractables/`. Each contains contracts, live state, bug, step-by-step path, PoC/evidence, economics, risks, and handover steps.

| ID | Protocol | Chain | Net | Confidence | Gate | Dossier |
|---|---|---|---:|---|---|---|
| EX-01 | Frankencoin — zero-second challenge period | Ethereum | ~$500,000 | HIGH path / MEDIUM realization | FPS veto risk | `01-frankencoin-zero-challenge-500k.md` |
| EX-02 | FrankenCoin — near-expiry clone | Ethereum | $7,597 | HIGH | capital | `02-frankencoin-expired-clone-7597.md` |
| EX-03 | Prospective World — `reserve()` free-mint | Tron | ~$48,000 | MEDIUM | none | `11-prospective-world-free-mint-48k.md` |
| EX-04 | LoopFi — CDPVault pre-penalty liquidation | Ethereum | $2,963 | MEDIUM | oracle/price drop | `09-loopfi-cdp-liquidation-2963.md` |
| EX-05 | YVS Finance — withdraw reward accounting | Ethereum | $656 | MEDIUM | capital + 84 days | `03-yvs-vault-reward-accounting-656.md` |
| EX-06 | Spartan Protocol — `burnSynth` mispricing | BNB Chain | $600 | MEDIUM | capital | `07-spartan-burnsynth-600.md` |
| EX-07 | PerpCity — same-block mark self-liquidation | Arbitrum | $64.01/cycle | MEDIUM | none | `05-perpcity-same-block-mark-64.md` |
| EX-08 | Rocket Pool — unverified final-level leaf bond | Ethereum | $50 | LOW | registered node + bond | `06-rocketpool-final-leaf-bond-50.md` |
| EX-09 | Reserve Folio — cross-Folio auction bid | Solana | $36 | MEDIUM | none | `12-reserve-folio-auction-36.md` |
| EX-10 | Nome Protocol — Boardroom retroactive claim | Berachain | $25.42 | HIGH | none | `08-nome-boardroom-25.md` |
| EX-11 | MANTRA DEX — stableswap decimals | MANTRA Chain | $24.55 | MEDIUM | none | `10-mantra-dex-decimals-24.md` |
| EX-12 | Harmonix Finance — stale-NAV deposit | HyperEVM | $16.31/cycle | MEDIUM | capital + 60s window | `04-harmonix-stale-nav-16.md` |
| EX-13 | Marginswap — stale SUSHI oracle | Ethereum | $11.31 | HIGH | none | `13-marginswap-stale-oracle-11.md` |
| EX-14 | Doefin — expired orders / raw target | Arbitrum | $6.78 | HIGH | none | `14-doefin-stale-orders-6.md` |
| EX-15 | Inverse sDOLA — timed liquidation harvest | Ethereum | ~$14,337 (peak batch) | MEDIUM | time + Aave crvUSD flash capacity | `15-inverse-sdola-liquidation-timing.md` |
| EX-16 | Startale RewardRedistributor — snapshot TVL inflation | Soneium | $15.18/attack (+$3.97 JIT) | MEDIUM | capital + snapshot timing | `16-startale-reward-redistributor.md` |
| EX-17 | Doomsday Settlers — confirmDisaster pays any caller | Ethereum | $19.12 | MEDIUM | timing window | `17-doomsday-confirm-disaster-19.md` |
| EX-18 | Dyson Finance DYSN/USDC — premium from reserves | Polygon zkEVM | $226.90 | HIGH | capital (refundable) | `18-dyson-premium-extraction-226.md` |
| EX-19 | Infinity / FlowExchange — unvalidated complication steals approved NFTs | Ethereum | ~$279 | HIGH | none (victim approvals) | `19-infinity-flowexchange-forged-orders-279.md` |
| EX-20 | LSDai — stale-pool interest sniping | Ethereum | $93.20/cycle | HIGH | none (flash-loanable) | `20-lsdai-interest-sniping-93.md` |
| EX-21 | Phuture ManagedIndex — front-run vToken deposit | Ethereum | ~$1,888.83 per 1 WETH deposit | MEDIUM | pending victim deposit (MEV) | `21-phuture-frontrun-mint-1889.md` |
| EX-22 | blex.io BLX-1 — close fee refunded | Arbitrum | $6,947.93 ceiling | MEDIUM | capital | `22-blex-blx1-excess-refund-6948.md` |
| EX-23 | Aqualis — phantom negative lending | Metis | $7.42 | MEDIUM | capital | `23-aqualis-phantom-negative-7.md` |
| EX-24 | Let's Get HAI — leaf per Merkle root | Optimism | $3,515.89 | MEDIUM | KITE allocation | `24-hai-double-claim-3515.md` |
| EX-25 | Oku — order-ID collision double refund | Optimism | $41.30 | HIGH | capital | `25-oku-orderid-collision-41.md` |

**Duplicates:** Prospective World, Reserve and MANTRA each have two target rows for the same live bug. The master log marks them with `economic_id` and dedupe. Do not add them twice.

---

## 4. The Stage 3 protocol (read this before running a wave)

The full protocol is `/workspaces/CA/stage3/STAGE3.md`. Summary:

### Per target

1. **Headline first.** Read the target's `headline`, `titles`, `uids`, `report_urls`, `evidence_urls`.
2. **Pull live code.** Etherscan V2 / chain-native RPC; compare to the audited version; decide `PATCHED` / `LIVE` / `UNVERIFIED`.
3. **All-round audit.** Walk every external/public entry point. Areas:
   - access control / ownership / initializer / proxy
   - accounting / shares / decimals / rounding
   - oracle / price / TWAP / stale data
   - replay / nonce / signature / permit
   - CPI / account validation (non-EVM)
   - reentrancy / callbacks / token quirks
   - pause / upgrade / role gates
4. **PoC.** Foundry fork for EVM; local validator/simulateTransaction for non-EVM. Measure attacker net USD after gas and capital.
5. **Rank.**
   - `EXTRACTABLE_HIGH` — fork-proven net > $5, unprivileged, repeatable, no effective gate.
   - `EXTRACTABLE_MEDIUM` — live unprivileged path, value depends on state/liquidity or PoC partial.
   - `EXTRACTABLE_LOW` — plausible but unproven.
   - `NOT_EXTRACTABLE_HIGH` — $0 with a concrete reason; **default for $0**.
   - `NOT_EXTRACTABLE_MEDIUM/LOW` — unresolved caveat.
6. **Folder rule.** Create `stage3/work/<batch>/<slug>/` with `report.md`, `result.json`, `poc/`, `evidence/`. If net < $5, delete the folder after writing the batch result.

### Non-EVM

Use chain-native tools: Solana JSON-RPC/IDL, Cosmos LCD, Sui/Aptos fullnode, Stellar Horizon/Soroban, NEAR RPC, TON API, Starknet RPC. Always write a `coverage` array: one row per entry point/area with `{area, entry_point, checked, result}`. This was added after the first non-EVM waves to make “all-round” auditable.

### Hard rules

- **`NEEDS_MORE` is forbidden.** Every target ends `EXTRACTABLE` or `NOT_EXTRACTABLE` with a confidence. If evidence is missing, decompile, try three RPCs, use archive sources, and decide.
- No DoS promotion. Freeze/griefing with no attacker gain is `NOT_EXTRACTABLE`.
- No invented addresses, balances, or PoC results.
- Read-only.

---

## 4b. Hardened non-extractability standard (mandatory)

A `NOT_EXTRACTABLE` verdict is only accepted when:

1. `confidence = HIGH` — no `NOT_EXTRACTABLE_MEDIUM/LOW` final verdicts.
2. `coverage` lists every external/public entry point (EVM selectors or non-EVM instructions).
3. `safe_reasons` gives a concrete reason per value-moving path (patched line/selector, role check, zero balance, revert trace, zero-net PoC).
4. A fresh-EOA closure artifact exists: fork/simulate revert, patched code match + live gate, or zero-value proof.
5. `value_at_risk_usd` and `tvl_source` are recorded; material value must be explicitly shown unreachable.
6. `headline_status` and `new_bugs` are explicit.

A separate QA pass samples 20% of negatives plus 100% of targets with >$100k value at risk. Weak negatives are re-audited by fresh agents; the wave does not count until QA accepts. Full checklist: `stage3/QA_CHECKLIST.md`.

## 4c. Address independence — the batch address is a lead, not evidence

This is now mandatory in every audit and is the fix for the weakest part of the corpus.

**The failure mode.** `PARTIAL` means *project located, exact audited instance unproven*. `FOUND` means
*one instance identified*, which says nothing about siblings, proxies, other chains, or later
versions. Agents that audited the batch address and stopped inherited that uncertainty: a negative on
the wrong version is worthless, and an extractable bug sitting in an unlisted instance is missed
entirely.

**The rule.** Every target gets a Step 0 deployment re-derivation before any audit work:

1. Independently locate the deployment (repo `deployments/`/`broadcast/`/address books, frontend JS
   bundle, explorer creation data, deployer-EOA pivot, DefiLlama, Wayback, chain-native tooling).
2. Prove the code exists on chain and tie it to the project with a source URL.
3. Version-test it against the audited commit (`EXACT_MATCH` / `MATCH_EXCEPT_IMMUTABLES` /
   `DIFFERENT_VERSION`). On `DIFFERENT_VERSION`, find the matching instance.
4. Enumerate instances: factory count, clones, proxies/impl, other chains.
5. Record it all in `derived_addresses`, and audit the derived address set, not just the lead.

**Multi-instance rule.** If the protocol deploys the same code many times, one negative covers one
instance only. Check the worst-case/highest-value instance and state the count.

## 4d. Stage 2.6 — the recon queue (`stage26/`)

222 units, 74 batches (`R3-001..R3-074`), 3 units per batch. Read `stage26/RECON.md` before launching;
it is a complete protocol (ladder, pivots, version test, instance enumeration, non-EVM specifics,
output schema).

| Lane | Units | Batches | What they are |
|---|---:|---:|---|
| `A_NO_ADDRESS` | 148 | 50 | `PARTIAL` with no address at all — the real gap |
| `B_PARTIAL_ANCHOR` | 29 | 10 | `PARTIAL` with an unproven anchor |
| `C_FOUND` | 45 | 15 | `FOUND`, but only one instance is known |

Units are chunked 3-per-batch in lane order, so one batch (`R3-050`) mixes lane A and B; the JSON
carries each unit's `lane` field. Counts above sum past 74 because of that shared batch.

Files:

```
stage26/RECON.md                 # protocol
stage26/index/recon_units.csv    # 222 units, sorted by criticality within lane
stage26/batches/R3-*.json        # 3 units each
stage26/results/, work/          # outputs
stage26/merge_recon.py           # accepted deployments -> new Stage 3 targets + batches
```

Recon statuses: `CONFIRMED` (audited code proven), `ANCHORED` (family located, identity unproven),
`UNRESOLVED` (ladder exhausted, every rung recorded), `NOT_DEPLOYED`.

**Merging.** `python3 stage26/merge_recon.py` is a dry run; `--apply` appends new targets to
`stage3/index/stage3_targets.csv` (ids continue past S3-3816), writes new 3-target batches, and is
idempotent via `stage26/index/merge_state.json`. Recon output is not audited work — do not count it as
coverage until the merged targets are audited.

## 5. How to run a wave

1. Pick the next N batches from `stage3/batches/` (each batch = 3 targets).
2. Launch an `AgentSwarm` with N items, using the prompt below (adjust `{{item}}`).
3. After the wave, rebuild the master log and reconcile failures.
4. Retry missing batches with **fresh agents** (do not resume failed subagents; inspect their `work/` folder and continue from partial files).
5. Do not launch a new wave until the current one is reconciled — the parent should not report until the agreed wave count is done.

### Prompt template

```
Execute Stage 3 batch {{item}}. Read /workspaces/CA/stage3/STAGE3.md and follow it exactly.
Your batch is /workspaces/CA/stage3/batches/{{item}}.json with 3 protocols.
For each target create /workspaces/CA/stage3/work/{{item}}/<slug>/ and do the aggressive
live audit: headline first, then all-round fund-draining review.
STEP 0 is mandatory: the batch address is a LEAD, not evidence. Independently re-derive the
deployment set (repo deployments/ and broadcast/ and address books, official frontend JS bundle,
explorer creation data, deployer-EOA pivot, DefiLlama, other claimed chains), version-test against
the audited commit, enumerate factory/clone instances and proxy/impl pairs, and audit the derived
set rather than the lead. Record `derived_addresses` with source + code check + bytecode match.
Follow /workspaces/CA/stage26/RECON.md sections "The derivation ladder", "Version-drift test",
"Enumerate, do not stop at one".
Use Foundry, Etherscan V2 ($ETHERSCANV2_API_KEY), Alchemy ($ALCHEMY_API_KEY_2 in
/workspaces/CA/alchemy.env), Infura, Ankr, Jina Reader, bytecode decompilation/disassembly,
and alternative public RPCs.
Read-only: no broadcasts, no private keys, no mainnet transactions.
NEEDS_MORE is forbidden. Finish end-to-end; if code is unverified, decompile and test the
exact selectors on a fork; if an RPC is down, try at least three alternatives.
Decide EXTRACTABLE or NOT_EXTRACTABLE with HIGH/MEDIUM/LOW confidence and a USD net.
$0 defaults to HIGH unless a concrete unresolved caveat remains (then MEDIUM).
If net < $5, delete the protocol folder after writing its result.
Write /workspaces/CA/stage3/results/{{item}}.json and .md in the exact schema.
Return a 4-line summary only.
```

For non-EVM batches, use the variant with chain-native tools and the `coverage` array (see §4).

---

## 6. Batch construction

Current batch ranges:

| Priority | Batches | Targets |
|---|---|---|
| 1 | S3-001..196 | 588 |
| 2 | S3-197..720 | 1,571 |
| 3 | S3-721..807 | 260 |
| 4 | S3-870..1230 + S3-1231..1274 | 1,184 |
| 5 | S3-808..869 + S3-1231..1274 | 213 |

**Priority 2 remaining:** S3-337..720 (384 batches; 1,151 targets).

**Stage 2.6 recon:** R3-001..R3-074 (74 batches; 222 units). Separate queue, separate protocol
(`stage26/RECON.md`), no audit. Its accepted deployments merge into Stage 3 as new targets (§4d).

**Priority 4 is built:** S3-870..S3-1230 (361 batches, 1,082 targets), plus the Stage 2.5 additions in S3-1231..S3-1274 (44 batches, 131 targets: 102 priority 4, 29 priority 5). Validated: every target appears once, batch counts are 3 except the last, 0 overlap with earlier targets.

Each batch JSON shape:

```json
{"batch_id":"S3-870","count":3,"targets":[ ... three rows from stage3_targets.csv ... ]}
```

---

## 7. Aggregation and dedupe

After each wave, rebuild `/workspaces/CA/stage3/MASTER_LOG.csv` from **all** `stage3/results/S3-*.json`, not from agent-appended rows. Agents sometimes append duplicates. The canonical script logic:

- Load every result file, key targets by `target_id` (last result wins).
- Map `target_id → batch_id` from `stage3/batches/`.
- For extractables, assign `economic_id` (EX-01..EX-14) and mark duplicate rows.
- Unique extractable value = sum of the **first** row per `economic_id`.
- Write columns: `batch_id,target_id,project,chain,address,headline_status,verdict,economic_id,extractability_usd,confidence,gate,new_bugs,poc,folder_removed,notes`.

Current unique total: **$587,421.84** (31 extractable rows, 25 unique; PerpCity/Oku/Aqualis duplicates counted once). EX-15 is a timing-gated keeper opportunity, not a code bug - see `extractables/15-inverse-sdola-liquidation-timing.md`.

---

## 8. Tools, keys, environment

Load without printing:

```bash
set -a; . /workspaces/CA/.env; . /workspaces/CA/alchemy.env; . /workspaces/CA/firecrawl.env; set +a
```

- Foundry: `/workspaces/CA/research/tools/foundry/{forge,cast,anvil}`.
- Etherscan V2: `$ETHERSCANV2_API_KEY` — `https://api.etherscan.io/v2/api?chainid=<id>&module=contract&action=getsourcecode&address=<addr>&apikey=$ETHERSCANV2_API_KEY`.
- Alchemy: `https://<chain>.g.alchemy.com/v2/$ALCHEMY_API_KEY_2` (eth/arb/base/opt/polygon).
- Infura: `https://mainnet.infura.io/v3/$INFURA_API_KEY`; Ankr: `https://rpc.ankr.com/<chain>/$ANKR_API_KEY`.
- Jina Reader (free): `https://r.jina.ai/<url>` and `https://r.jina.ai/https://www.bing.com/search?q=<query>`.
- Firecrawl keys are exhausted; do not rely on them. Key 19 may be 0.
- HF token: `$HF_TOKEN`; dataset `Mariano234/web3-audit-profit-hunt`.
- GitHub token: `$CHRIS_GITHUB_API_KEY_2` (repo scope); repo `artsbykriss/web3-audit-profit-hunt`.

---

## 9. Failure handling (important)

Observed errors: `step.end finishReason:"error"` and `prompt.aborted`, clustered at high step counts. This is provider/LLM failure under sustained subagent load, not disk/context exhaustion.

- **Keep ≤10 agents per wave.** 20 agents produced heavy failures; 10 agents + retries is workable.
- Some agents write their result files before the final message is lost. Always check `stage3/results/<batch>.json` and `stage3/work/<batch>/` before relaunching.
- Retry missing batches with **fresh agents**, not `resume_agent_ids`. Tell them: “inspect the work folder and continue from where the previous agent stopped.”
- Do not delete a batch result because the agent reported failure; validate the JSON first.

Disk maintenance before a long run:

```bash
rm -rf ~/.foundry/anvil ~/.cache/copilot ~/.cache/go-build ~/.cache/yarn ~/.cache/pip
rm -rf /tmp/*
df -h /workspaces
```

`~/.foundry/anvil` grows to ~2 GB. Keep at least 3–5 GB free.

---

## 10. Confidence assessment

**The 30/100 figure was coverage-weighted and reflected the old, permissive negative standard.** It is not a measure of the 14 positives, which are evidence-backed.

Under the hardened standard:

- **Per accepted target:** `NOT_EXTRACTABLE` is HIGH by construction (full coverage + safe_reasons + closure artifact + derived_addresses + QA). Target-level assurance ~85%.
- **Per wave:** QA acceptance; a wave with weak negatives is rejected.
- **Overall:** coverage × QA acceptance × **address identity**. At 100% coverage and a clean QA pass, ~85–90% — not 100%, because unverified code and time bounds remain.

**Address identity is the third factor and the one that was silently assumed before.** A negative is
only as good as the address it was tested on. For `PARTIAL`-derived targets (131 in the corpus) the
anchor was never proven to be the audited version; for multi-instance protocols a single-address
negative covers one instance. Step 0 (§4c) plus the Stage 2.6 recon lane is what converts that
assumption into evidence. Until a target has `derived_addresses` with a version verdict and instance
coverage, treat its negative as **provisional**, not accepted.

Current coverage is 1,452/3,816 (38%). The remaining 2,364 targets must be run under the hardened
standard; the overall figure rises as coverage rises. The 148 address-less units in §2 are outside
that denominator entirely.

## 11. Directory map / what not to delete

```
/workspaces/CA/
  FINAL_MASTER.csv                  # all 7,604 findings
  FINAL_FUND_DRAINING.csv           # clean 7,479 C/H fund-draining rows
  FINAL_SUMMARY.md/json
  extractables/                     # 14 dossiers + README
  stage3/
    STAGE3.md                       # protocol
    MASTER_LOG.csv                  # 1,452 audited targets
    index/stage3_targets.csv        # all 3,816 targets
    batches/S3-*.json               # 1,274 built, all priorities
    results/S3-*.json|.md           # batch outputs
    work/S3-*/<protocol>/           # kept PoCs/evidence for >$5 targets
    results.tar.gz                  # archive
  stage26/
    RECON.md                        # recon protocol (read before launching R3 batches)
    index/recon_units.csv           # 222 units
    batches/R3-*.json               # 74 recon batches
    merge_recon.py                  # merged deployments -> new Stage 3 targets
  research/
    corpus2/stage1/index/           # Stage 1 master/targets
    corpus2/stage2/index/           # Stage 2 master/targets/addresses
    prior/, retrace/                # prior campaign + re-trace
    audits/hunt, audits2/index      # prior evidence
    tools/foundry/                  # forge/cast/anvil
```

**Do not delete:** `FINAL_*`, `extractables/`, `stage3/MASTER_LOG.csv`, `stage3/index/`, `stage3/batches/`, `stage3/results/`, `research/corpus2/stage1|stage2/index`, `research/prior`, `research/retrace`, `research/tools`.

Public repo: `https://github.com/artsbykriss/web3-audit-profit-hunt`  
HF backup: `https://huggingface.co/datasets/Mariano234/web3-audit-profit-hunt`

Push after each checkpoint:

```bash
cd /workspaces/CA/research/corpus2/public-repo-v2
git add -A
git commit -m "Stage 3: <wave> complete"
GH_TOKEN="$CHRIS_GITHUB_API_KEY_2" git push origin main
```

---

## 12. First actions for the successor

1. Read `/workspaces/CA/stage3/STAGE3.md`, `/workspaces/CA/stage3/QA_CHECKLIST.md`, `/workspaces/CA/stage26/RECON.md` and this brief.
2. Rebuild `MASTER_LOG.csv` and confirm audited targets / 25 unique extractables.
3. Ask the user how many agents per wave (3 targets/agent constant); compute waves as `ceil(2,364 / (3 × N))`.
4. Continue priority 2 from **S3-337**; when exhausted, use the already-built priority 4 batches **S3-870..S3-1230** plus the Stage 2.5 batches **S3-1231..S3-1274**.
5. Run the Stage 2.6 recon lane **R3-001..R3-074** (3 units/agent, `stage26/RECON.md`) in parallel or between audit waves; `merge_recon.py --apply` turns `CONFIRMED`/`ANCHORED` deployments into new audit targets. Do not count recon as coverage.
6. Keep ≤10 agents per wave unless the user explicitly authorizes more; retry failures with fresh agents.
7. Publish checkpoints to GitHub + HF.
8. Do not claim “nothing missed” without stating the coverage, the address-identity basis and the confidence above.

**Never do these:** start an audit wave without the user's agent count; audit a batch address without
Step 0; accept a negative that lacks `derived_addresses`; treat the 148 address-less units as covered;
re-open the closed decisions (3 targets/agent, HIGH-only negatives, no `NEEDS_MORE`, duplicate
`economic_id`s not double-counted).
