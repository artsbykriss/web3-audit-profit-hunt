# EX-09 — LoopFi: CDPVault liquidation takes pre-penalty collateral, leaving bad debt

**Net for an unprivileged actor:** **~$2,963** per liquidation (1.449 WETH), with ~$934 pool bad debt
**Confidence:** MEDIUM — fork-proven at a mocked spot of 1.9; the live spot is 2.122 and the position is 3.8% from the liquidation threshold
**Gate:** oracle/price condition — requires ETH/USD to fall enough to make the position liquidatable
**Chain:** Ethereum (1)
**Status:** headline AuraVault H-01 is not deployed; this is live C4 H-02 in CDPVaultSpectra.

## Contracts

| Role | Address |
|---|---|
| PoolV3 | `0xa684eaf215ad323452e2b2bF6f817d4aa5c116ab` |
| CDPVaultSpectra | `0x9c5EE26b9623cA864693C575a8fBc8933ae964E7` |
| Position | `0x4C696a…` — collateral 38.519 WETH, debt 60.0 WETH, virtualDebt 71.485, spot 2.122, liquidationRatio 1.1, discount 0.98, penalty 0.99 |
| Chainlink ETH/USD | `0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419` |

Live pool: `totalAssets` 77.151 WETH; `totalSupply` 65.977; `availableLiquidity` 0.0000736 WETH; `totalBorrowed` 65.977.

## Bug

`CDPVaultSpectra.liquidatePosition` computes the collateral seized from the **pre-penalty repay amount**, then calls `PoolV3.repayCreditAccount`. The liquidator repays 71.0 WETH and receives 38.131 collateral worth 72.449 WETH; the position is left with 0.388 collateral and 1.195 debt. The liquidator captures the residual; the pool absorbs 0.457 WETH bad debt.

The headline AuraVault H-01 is removed (`scripts/deploy.js` has no AuraVault); the H-03 quota path is creditManager/gauge gated. Direct PoolV3 is $0 (10 role-gated credit managers, 1:1 deposit/redeem). The live CDPVaultSpectra holds 62.026 of the pool's 65.977 ETH principal.

## Step-by-step

```
wait until spot falls enough that the 0x4C69 position is liquidatable
liquidatePosition(0x4C69, 71.0 WETH)
// receive 38.131 collateral worth 72.449 WETH
// position left with 0.388 collateral, 1.195 debt
// pool bad debt 0.457 WETH
```

## PoC

`stage3/work/S3-255/2024_07_loopfi_0xa684ea/poc`

Fork test at block 26,398,284:

```
mockSpot = 1.9e18
repay = 71.0 WETH
collReceived = 38.131041890440386680 WETH
collRemaining = 0.388358499997111279 WETH
debtRemaining = 1.195370335524340471 WETH
attacker net = 1.449 WETH (~$2,963)
pool bad debt = 0.457 WETH (~$934)
```

Run with the Ethereum RPC at block 26,398,284.

## Economics

- Attacker capital: 71 WETH; net 1.449 WETH ≈ $2,963 at $2,044/ETH.
- Pool bad debt: 0.457 WETH ≈ $934.
- The live position is 3.8% from the liquidation threshold; at spot 2.122 it is not yet liquidatable. The PoC uses spot 1.9.

## Evidence

- `evidence/live_state.txt` — pool and position state.
- `evidence/cdp_0xb85095…/src/CDPVault.sol` — verified CDPVault source.
- C4 2024-07 LoopFi report — H-02.
- Fork PoC output.

## Risks / caveats

- **Oracle gate:** the position must become liquidatable; the live spot is 2.122 vs a 2.04-ish threshold. A ~4% ETH drop opens it.
- MEDIUM because the PoC mocks the spot; the live path depends on the oracle and the position's health.
- The liquidator needs 71 WETH capital; the net is ~2% of capital.
- If the position is repaid/closed or the oracle changes, the path disappears.

## Handover

1. Monitor the 0x4C69 position health and the Chainlink ETH/USD price.
2. When spot < liquidation threshold, re-run the PoC at the live block; confirm the 38.131 collateral / 1.195 debt residual.
3. Check `liquidationDiscount`/`penalty` and pool liquidity before sizing.
4. If the position is closed, look for other CDPVaultSpectra positions with the same pre-penalty logic.
