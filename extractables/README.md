# Extractables — live fund-draining findings

Twenty-five unique findings survived the Stage 3 live audit with a positive net for an external unprivileged actor (31 target rows; Prospective World, Reserve and MANTRA each have duplicate target rows for the same live bug). EX-15 is a timing-gated keeper opportunity rather than a code bug - see its dossier for the exact-second liquidation calendar.

| ID | Protocol | Chain | Net | Confidence | Gate | Dossier |
|---|---|---|---:|---|---|---|
| EX-01 | Frankencoin — zero-second challenge period | Ethereum | ~$500,000 | HIGH path / MEDIUM realization | FPS veto risk | `01-frankencoin-zero-challenge-500k.md` |
| EX-02 | FrankenCoin — near-expiry clone | Ethereum | $7,597 | HIGH | capital (10 WETH, 48h) | `02-frankencoin-expired-clone-7597.md` |
| EX-03 | Prospective World — `reserve()` free-mint | Tron | ~$48,000 | MEDIUM | none | `11-prospective-world-free-mint-48k.md` |
| EX-04 | LoopFi — CDPVault pre-penalty liquidation | Ethereum | $2,963 | MEDIUM | oracle/price drop | `09-loopfi-cdp-liquidation-2963.md` |
| EX-05 | YVS Finance — withdraw reward accounting | Ethereum | $656 | MEDIUM | capital (1.7 LP, 84 days) | `03-yvs-vault-reward-accounting-656.md` |
| EX-06 | Spartan Protocol — `burnSynth` mispricing | BNB Chain | $600 | MEDIUM | capital | `07-spartan-burnsynth-600.md` |
| EX-07 | PerpCity — same-block mark self-liquidation | Arbitrum | $64.01/cycle | MEDIUM | none | `05-perpcity-same-block-mark-64.md` |
| EX-08 | Rocket Pool — unverified final-level leaf bond | Ethereum | $50 | LOW | registered node + bond | `06-rocketpool-final-leaf-bond-50.md` |
| EX-09 | Reserve Folio — cross-Folio auction bid | Solana | $36 | MEDIUM | none | `12-reserve-folio-auction-36.md` |
| EX-10 | Nome Protocol — Boardroom retroactive claim | Berachain | $25.42 | HIGH | none | `08-nome-boardroom-25.md` |
| EX-11 | MANTRA DEX — stableswap decimals | MANTRA Chain | $24.55 | MEDIUM | none | `10-mantra-dex-decimals-24.md` |
| EX-12 | Harmonix Finance — stale-NAV deposit | HyperEVM | $16.31/cycle | MEDIUM | capital + 60s window | `04-harmonix-stale-nav-16.md` |
| EX-13 | Marginswap — stale SUSHI oracle | Ethereum | $11.31 | HIGH | none | `13-marginswap-stale-oracle-11.md` |
| EX-14 | Doefin — expired orders / raw target | Arbitrum | $6.78 | HIGH | none | `14-doefin-stale-orders-6.md` |

**Total unique headline value: ~$587,422** (PerpCity appears twice as EX-07 and is counted once). (includes EX-15's $14,337 timing-gated keeper opportunity, EX-16's $15.18 per-attack capture, EX-17's $19.12 and EX-18's $226.90).

Each dossier contains: contracts, live state, bug, step-by-step path, PoC location/evidence, economics, risks, and handover steps. PoCs live under `stage3/work/<batch>/<protocol>/poc/`.

All work was read-only: no broadcasts, no private keys, no mainnet transactions. `EXTRACTABLE` means the contract path is live and the PoC/evidence reproduces the gain; it does not mean funds have been moved.
