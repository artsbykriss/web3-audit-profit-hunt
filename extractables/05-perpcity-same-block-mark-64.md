# EX-05 — PerpCity: same-block mark manipulation self-liquidation

**Net for an unprivileged actor:** **$64.01 per $4,000 cycle** before gas; loopable/scalable
**Confidence:** MEDIUM — the path is acknowledged-unfixed in the final audit, but the live implementation is unverified and the Guardian PoC repo is private, so it was not re-run on a local fork
**Gate:** none
**Chain:** Arbitrum (42161)
**Status:** headline C-02 (dust-maker residual) is audit-resolved. This is a new acknowledged-unfixed path in the final audited code.

## Contracts

| Role | Address |
|---|---|
| Perp implementation (UUPS, unverified) | `0x9b74b1ff217bdE6EB0e221Ca11034D67187EF9d3` |
| Market proxy 1 | `0x8614c6af5c3db50e694d37c4147a3c3891b0e877` (~23,859 USDC) |
| Market proxy 2 | `0xb9f540ce4315e7f4382c96532f8ec3903899d86d` (~9,231 USDC) |
| Market proxy 3 | `0xfd40006f4dbb8b89bc38c774615995e786302e64` (~6,319 USDC) |

Live aggregate margin across 50 markets: ~56,073 USDC; top market ~23,851 USDC.

## Bug

The mark price is a 50/50 blend of the live AMM price and an EMA. `accrue()` at `dt == 0` leaves the EMAs unchanged. A trader can therefore:

1. Open a helper position and push the AMM mark in the same block.
2. Withdraw collateral that the honest mark would reject.
3. Restore the mark.
4. Self-liquidate the stripped position and collect the liquidation reward.

The Guardian final report (RR2 C-02, acknowledged, p.162) records +$64.011402 on $4,000 capital and $73.55 bad debt. A second acknowledged path (RR2 H-02, p.165) sandwiches beacon reports to poison the index EMA and force a healthy long into a wrongful backstop, then seizes the NFT.

## Step-by-step

```
open helper position -> move AMM mark
withdraw collateral from the target position at the manipulated mark
close helper -> restore mark
liquidateTaker(target) -> collect reward; bad debt socialized
```

## PoC

No local Foundry PoC. The live implementation `0x9b74b1ff…` is unverified and the Guardian PoC repository is private. Evidence:

- Guardian RR2 C-02 (acknowledged): +$64.011402 on $4,000, $73.55 bad debt.
- `evidence/decomp2/decompiled.sol` — decompiled implementation.
- `evidence/positions.json`, `perps.json`, `market_txs.json` — live market state.
- `evidence/report.pdf` — Guardian report.

## Economics

- $64.01 per $4,000 cycle before gas; $73.55 bad debt per cycle.
- Loopable across markets; aggregate margin ~$56k, top market ~$23.8k.
- MEDIUM because the exact live bytecode path was not fork-proven; the audit report and decompilation support it.

## Risks / caveats

- The implementation is unverified; the decompiled logic must be matched to the audited revision.
- The Guardian PoC is private; the $64.01 figure is from the report, not a local run.
- If the live mark/EMA implementation differs from the audited code, the path may be closed.
- Bad debt is socialized; the attacker's reward is the liquidation bonus, not the full position.

## Handover

1. Obtain verified source or complete the decompilation of `0x9b74b1ff…`; compare to the Guardian final report.
2. Rebuild the same-block mark manipulation PoC on an Arbitrum fork; confirm the +$64.01 and bad debt.
3. Check each live market's AMM depth and margin; size the cycle.
4. If the path reproduces, upgrade confidence to HIGH; if the live code differs, close as NOT_EXTRACTABLE.
