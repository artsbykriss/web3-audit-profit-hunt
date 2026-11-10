# Prior-work deployment trace — confidence assessment

**Date:** 2026-11-10  
**Scope:** the campaign that ran before the GitHub `web3-audit-findings` and HuggingFace `x23` corpora were introduced — `research/audits/hunt/` (73 protocol hunts) and `research/audits/index/hunt_groups.json` (152 discovered protocol groups).  
**Question:** how confident are we that the deployment contract addresses (CAs) of that prior work were actually traced, and that everything discovered was included?

## 1. Headline

| Measure | Result | Confidence |
|---|---:|---:|
| Hunts with at least one recorded CA | 64 / 73 | **87.7%** |
| Hunts with CA + non-unverified code match | 53 / 73 | **72.6%** |
| Hunts with a definitive disposition (CA found, or proven not deployed) | 68 / 73 | **93.2%** |
| Hunts left UNPROVEN | 5 / 73 | 6.8% |
| **Discovered groups actually hunted/traced** | **40 / 152** | **26.3%** |
| Profit-keyword groups traced | 38 / 113 | 33.6% |
| Groups containing criticals traced | 24 / 82 | 29.3% |
| Critical findings covered | 91 / 190 | 47.9% |
| Critical+High findings covered | 484 / 772 | 62.7% |

**One-line answer:** within the 73 protocols that were hunted, the CA trace is strong (73% code-verified, 93% definitive). But **“everything was included” is not true: only 40 of the 152 discovered groups (26%) were hunted**, covering 63% of the C/H finding volume. The honest overall coverage confidence is **~26% by protocol count, ~63% by C/H volume** — not 100%.

## 2. What counts as traced

- `address recorded` — the hunt JSON contains at least one 40-hex address in `addresses[]`.
- `CA + code match` — an address is recorded and `code_match` is not `unverified` (i.e. `exact`, `changed`, or `not deployed` with negative evidence).
- `definitive` — the verdict is not `UNPROVEN`: `LIVE`, `PATCHED`, `GATED`, `DRAINED`, or `NOT_DEPLOYED`.
- Coverage is counted at the protocol-group level, because the prior work discovered protocols, then hunted a subset.

## 3. The 73 hunts

| Hunt | Protocol | Chain | Verdict | Addresses | Code match | Evidence quality |
|---|---|---|---|---:|---|---|
| HUNT-001 | RAAC Core Contracts | ethereum | NOT_DEPLOYED | 9 | unverified | on-chain |
| HUNT-002 | Beanstalk: The Finale | arbitrum | PATCHED | 3 | changed | on-chain |
| HUNT-003 | Zaros (Part 2) | arbitrum | NOT_DEPLOYED | 4 | unverified | on-chain |
| HUNT-004 | Tadle | ethereum+bsc | PATCHED | 12 | changed | on-chain |
| HUNT-005 | QuantAMM | ethereum, base, arbi | NOT_DEPLOYED | 5 | changed | on-chain |
| HUNT-006 | Steadefi | arbitrum | PATCHED | 5 | changed | on-chain |
| HUNT-007 | DittoETH | ethereum | PATCHED | 9 | changed | on-chain |
| HUNT-008 | Liquidity Management (Gamma GMX Perpetual Vault) | arbitrum | GATED | 7 | changed | docs/other |
| HUNT-009 | Biconomy: Nexus | ethereum | PATCHED | 4 | changed | source |
| HUNT-010 | ArkProject: NFT Bridge | ethereum | GATED | 6 | changed | on-chain |
| HUNT-011 | Beedle - Oracle free perpetual lending | none | NOT_DEPLOYED | 0 | unverified | docs/other |
| HUNT-012 | GainsNetwork | arbitrum | PATCHED | 5 | changed | source |
| HUNT-013 | Lucidly | ethereum | PATCHED | 19 | exact | on-chain |
| HUNT-014 | Omo | base | DRAINED | 9 | changed | source |
| HUNT-015 | Bunni | ethereum | PATCHED | 8 | changed | source |
| HUNT-016 | KittenSwap | hyperliquid | PATCHED | 8 | changed | docs/other |
| HUNT-017 | Blueberry | hyperliquid | PATCHED | 7 | exact | on-chain |
| HUNT-018 | OLY | ethereum | PATCHED | 16 | changed | on-chain |
| HUNT-019 | StationX | linea | LIVE | 5 | changed | on-chain |
| HUNT-020 | TapiocaDAO | arbitrum | PATCHED | 9 | changed | on-chain |
| HUNT-021 | Saffron | ethereum | NOT_DEPLOYED | 0 | unverified | source |
| HUNT-022 | Peapods | ethereum | PATCHED | 10 | changed | docs/other |
| HUNT-023 | RipIt | base | PATCHED | 9 | changed | on-chain |
| HUNT-024 | Burve | berachain | PATCHED | 4 | changed | docs/other |
| HUNT-025 | Hyperhyper | hyperliquid | NOT_DEPLOYED | 13 | unverified | on-chain |
| HUNT-026 | Nexus | ethereum | PATCHED | 9 | changed | on-chain |
| HUNT-027 | SharwaFinance | arbitrum | PATCHED | 11 | changed | on-chain |
| HUNT-028 | Astrolab | arbitrum | PATCHED | 3 | changed | on-chain |
| HUNT-029 | Radiant | base | GATED | 12 | exact | on-chain |
| HUNT-030 | Elytra | hyperevm | NOT_DEPLOYED | 0 | unverified | source |
| HUNT-031 | Reya Network | reya | PATCHED | 5 | exact | on-chain |
| HUNT-032 | Karak | ethereum | NOT_DEPLOYED | 4 | changed | on-chain |
| HUNT-033 | Ostium | arbitrum | GATED | 6 | changed | source |
| HUNT-034 | Hyperstable | hyperliquid | PATCHED | 4 | changed | on-chain |
| HUNT-035 | BOB-Staking | bob | PATCHED | 3 | changed | source |
| HUNT-036 | Polygun | polygon | UNPROVEN | 0 | unverified | on-chain |
| HUNT-037 | Regnum Aurum | ethereum | NOT_DEPLOYED | 11 | not deployed | on-chain |
| HUNT-038 | Coinflip | none identified | UNPROVEN | 0 | unverified | on-chain |
| HUNT-039 | Roots | berachain | PATCHED | 10 | changed | on-chain |
| HUNT-040 | STBL ESS / Redemptions | ethereum | NOT_DEPLOYED | 6 | unverified | on-chain |
| HUNT-041 | Accountable | ethereum | PATCHED | 9 | changed | on-chain |
| HUNT-042 | Remora Dynamic Tokens | none identified | UNPROVEN | 0 | unverified | source |
| HUNT-043 | Licredity | none | NOT_DEPLOYED | 0 | unverified | on-chain |
| HUNT-044 | Paladin Valkyrie | none | NOT_DEPLOYED | 0 | unverified | docs/other |
| HUNT-045 | Stake.Link Withdrawals | ethereum | PATCHED | 15 | changed | on-chain |
| HUNT-046 | Casimir Selfstake | ethereum | NOT_DEPLOYED | 5 | unverified | on-chain |
| HUNT-047 | DeXe | bsc | PATCHED | 8 | changed | source |
| HUNT-048 | EARN'M | polygon | UNPROVEN | 7 | unverified | on-chain |
| HUNT-049 | Beefy CL | arbitrum | PATCHED | 6 | changed | source |
| HUNT-050 | Goldilocks | berachain | UNPROVEN | 10 | changed | source |
| HUNT-051 | Beanstalk BIP-39 | arbitrum | PATCHED | 5 | changed | on-chain |
| HUNT-052 | Sudoswap sudoAMM v2 | ethereum | GATED | 3 | changed | on-chain |
| HUNT-053 | Wells / Basin | arbitrum, ethereum | GATED | 12 | changed | docs/other |
| HUNT-054 | Xtatuz DMCC | none (searched ether | NOT_DEPLOYED | 0 | unverified | on-chain |
| HUNT-055 | FWX | base (also bsc, aval | PATCHED | 17 | changed | docs/other |
| HUNT-056 | Vega Investment Group | ethereum | PATCHED | 3 | changed | source |
| HUNT-057 | Code Sekai | ethereum | PATCHED | 4 | changed | on-chain |
| HUNT-058 | Syndicate | ethereum | PATCHED | 5 | exact | on-chain |
| HUNT-059 | Pluto (Pluto Fi) | solana | NOT_DEPLOYED | 11 | unverified | docs/other |
| HUNT-060 | Raga Finance | berachain | PATCHED | 13 | changed | on-chain |
| HUNT-061 | Zoniqx Smart Contracts | polygon | PATCHED | 12 | exact | source |
| HUNT-062 | iBax | bsc-testnet | NOT_DEPLOYED | 3 | unverified | on-chain |
| HUNT-063 | BIT5 | bsc | PATCHED | 4 | changed | docs/other |
| HUNT-064 | Guessmeme | ethereum | GATED | 5 | changed | on-chain |
| HUNT-065 | MemeSwap | berachain | PATCHED | 3 | changed | on-chain |
| HUNT-066 | IAm0x52/audit-portfolio | hyperliquid (HyperEV | PATCHED | 7 | changed | source |
| HUNT-067 | 0xsimao/audits portfolio — selected target: Exactly Pro | optimism | GATED | 13 | exact | docs/other |
| HUNT-068 | devNamedKiki/Audits (USSD) | arbitrum | PATCHED | 7 | changed | source |
| HUNT-069 | V4 Swap Router (z0r0z/v4-router) | ethereum | DRAINED | 1 | changed | source |
| HUNT-070 | PollenDAO | avalanche | PATCHED | 6 | changed | source |
| HUNT-071 | Castr.fun | base | NOT_DEPLOYED | 6 | unverified | on-chain |
| HUNT-072 | Astrophelverse/Audits — Morpho Blue | ethereum | GATED | 8 | exact | source |
| HUNT-073 | TrueFi (Helium) — audit portfolio zaryab2000/Smart-Cont | ethereum | PATCHED | 6 | changed | on-chain |

Evidence-quality counts:

| Quality | Hunts |
|---|---:|
| on-chain | 43 |
| source | 19 |
| docs/other | 11 |

The five UNPROVEN hunts: HUNT-036 Polygun, HUNT-038 Coinflip, HUNT-042 Remora Dynamic Tokens, HUNT-048 EARN'M, HUNT-050 Goldilocks.

The nine hunts with no recorded address: HUNT-011 Beedle - Oracle free perpetual lending, HUNT-021 Saffron, HUNT-030 Elytra, HUNT-036 Polygun, HUNT-038 Coinflip, HUNT-042 Remora Dynamic Tokens, HUNT-043 Licredity, HUNT-044 Paladin Valkyrie, HUNT-054 Xtatuz DMCC.  
Some of these are negative conclusions (`NOT_DEPLOYED`), not missing work.

## 4. Coverage of the 152 discovered groups

| Source | Groups | Traced | Group coverage | C/H findings | C/H covered | C/H coverage |
|---|---:|---:|---:|---:|---:|---:|
| pashov | 127 | 28 | 22.0% | 560 | 307 | 54.8% |
| codehawks | 24 | 12 | 50.0% | 211 | 177 | 83.9% |
| researcher | 1 | 0 | 0.0% | 1 | 0 | 0.0% |
| **Total** | **152** | **40** | **26.3%** | **772** | **484** | **62.7%** |

**112 groups were never hunted.** They contain **288 Critical/High findings**, including **99 criticals**. The top 30 by C/H volume:

| # | Group | Source | Critical | High | Latest |
|---:|---|---|---:|---:|---|
| 1 | Bear Cave | pashov | 6 | 3 | 2023-07-06 |
| 2 | Kinetiq | pashov | 0 | 8 | 2025-02-26 |
| 3 | Dyad | pashov | 2 | 6 | 2024-10-02 |
| 4 | Zaros Part 1 | codehawks | 0 | 8 | 2024-07-17 |
| 5 | apDAO | pashov | 2 | 5 | 2024-10-03 |
| 6 | Increment | pashov | 1 | 5 | 2024-03-05 |
| 7 | Nume | pashov | 2 | 4 | 2024-03-04 |
| 8 | Gigaverse | pashov | 0 | 5 | 2025-01-18 |
| 9 | Interpol | pashov | 1 | 4 | 2024-12-24 |
| 10 | ULTI | pashov | 2 | 3 | 2024-11 |
| 11 | MoarCandy | pashov | 3 | 2 | 2024-07-05 |
| 12 | Subsquid | pashov | 1 | 4 | 2024-02-12 |
| 13 | Ambire | pashov | 4 | 1 | 2023-09-25 |
| 14 | PumpScience | pashov | 1 | 3 | 2024-12-24 |
| 15 | g8keep | pashov | 0 | 4 | 2024-12-12 |
| 16 | Primodium | pashov | 4 | 0 | 2024-10-02 |
| 17 | Rivus | pashov | 2 | 2 | 2024-10 |
| 18 | Sofamon | pashov | 0 | 4 | 2024-08 |
| 19 | Groupcoin | pashov | 2 | 2 | 2024-07-13 |
| 20 | LayerZeroZROClaim | pashov | 2 | 2 | 2024-06-20 |
| 21 | Fyde | pashov | 1 | 3 | 2024-05 |
| 22 | Curio | pashov | 3 | 1 | 2024-04-18 |
| 23 | Catalyst | pashov | 3 | 1 | 2024-04 |
| 24 | ForgottenPlayland | pashov | 2 | 2 | 2024-03-28 |
| 25 | veTenet | pashov | 3 | 1 | 2023-08-10 |
| 26 | Rolling Dutch Auction | pashov | 3 | 1 | 2023-04-08 |
| 27 | Lizard Staking | pashov | 2 | 2 | 2023-03-27 |
| 28 | MorpheusAI | codehawks | 0 | 4 |  |
| 29 | The Standard | codehawks | 0 | 4 |  |
| 30 | Foundry DeFi Stablecoin CodeHawks Audit Contest | codehawks | 0 | 4 |  |

## 5. What this means

- **The 73 hunts are usable.** 87.7% have a CA, 72.6% have a code match, 93.2% reached a definitive disposition. The 1 LIVE (StationX, +$119.28) and the 9 GATED / 2 DRAINED records are the actionable residue.
- **The prior corpus is not fully covered.** 112 of 152 groups were never hunted. The 33 hunts that are not in the 152-group set came from the later expanded corpus (`audits2`), whose 4,645 detailed C/H were not individually traced.
- **The coverage number depends on the denominator.** By group count it is 26.3%; by C/H finding volume it is 62.7%; by critical-only findings it is 47.9%. None of these is 100%.
- **Before Stage 3 treats the prior work as a complete baseline, the 112 uncovered groups need a Stage 2-style pass.** Priority: the 75 profit-keyword groups among them, starting with Bear Cave, Kinetiq, Dyad, Zaros Part 1, apDAO, Increment, Nume, Gigaverse, Interpol and ULTI.

## 6. Files

- `research/audits/hunt/MASTER.csv` and `HUNT-*.json` — the 73 hunts.
- `research/audits/index/hunt_groups.json` — the 152 discovered groups.
- `research/EXTRACTABLE_VALUE_MASTER.md` — the actionable residue and dossiers.
