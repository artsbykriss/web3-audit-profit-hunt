# Extractables — live fund-draining findings

Nine findings survived the Stage 3 live audit with a positive net for an external unprivileged actor.

| ID | Protocol | Chain | Net | Confidence | Gate | Dossier |
|---|---|---|---:|---|---|---|
| EX-01 | Frankencoin — zero-second challenge period | Ethereum | ~$500,000 | HIGH path / MEDIUM realization | FPS veto risk | `01-frankencoin-zero-challenge-500k.md` |
| EX-02 | FrankenCoin — near-expiry clone | Ethereum | $7,596.60 | HIGH | capital (10 WETH, 48h) | `02-frankencoin-expired-clone-7597.md` |
| EX-03 | LoopFi — CDPVault pre-penalty liquidation | Ethereum | $2,963 | MEDIUM | oracle/price drop | `09-loopfi-cdp-liquidation-2963.md` |
| EX-04 | YVS Finance — withdraw reward accounting | Ethereum | $655.82 | MEDIUM | capital (1.7 LP, 84 days) | `03-yvs-vault-reward-accounting-656.md` |
| EX-05 | Spartan Protocol — `burnSynth` mispricing | BNB Chain | ~$600 | MEDIUM | capital | `07-spartan-burnsynth-600.md` |
| EX-06 | PerpCity — same-block mark self-liquidation | Arbitrum | $64.01/cycle | MEDIUM | none | `05-perpcity-same-block-mark-64.md` |
| EX-07 | Rocket Pool — unverified final-level leaf bond | Ethereum | ~$50 | LOW | registered node + bond | `06-rocketpool-final-leaf-bond-50.md` |
| EX-08 | Nome Protocol — Boardroom retroactive claim | Berachain | $25.42 | HIGH | none | `08-nome-boardroom-25.md` |
| EX-09 | Harmonix Finance — stale-NAV deposit | HyperEVM | $16.31/cycle | MEDIUM | capital + 60s window | `04-harmonix-stale-nav-16.md` |

**Total headline value: ~$511,971.**

Each dossier contains: contracts, live state, bug, step-by-step path, PoC location/evidence, economics, risks, and handover steps. PoCs live under `stage3/work/<batch>/<protocol>/poc/`.

All work was read-only: no broadcasts, no private keys, no mainnet transactions. `EXTRACTABLE` means the contract path is live and the PoC/evidence reproduces the gain; it does not mean funds have been moved.
