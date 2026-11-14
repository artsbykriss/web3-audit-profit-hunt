# EX-22 — blex.io BLX-1: close fee paid back to the user (AUM double-count)

**Chain:** Arbitrum (42161) · **Target:** S3-3034 · **Address:** `0xf14cBC388176B75401c6666C08bE8bB0046cdb83` (MarketRouter proxy; impl `0x90f6…`, deployed 2023-08-05, never upgraded)  
**Economic ID:** EX-22 · **Net:** ceiling **$6,947.93** (vault balance) · **Confidence:** MEDIUM (code-level invariant, no fork PoC) · **Gate:** capital

## What it is

Quantstamp BLX-1 ("User Can Receive Excessive Funds"): `PositionSubMgrLib.calculateTransToUser` transfers `collateralDelta + dPNL` when `collateralDelta + dPNL - fees == 0`, so the close fee is returned to the user instead of the vault. The fix (`<=` vs `<`) landed 2023-09-28 (commit 70938fc), but the live impl was created 2023-08-05 and its EIP-1967 slot was never upgraded — so the deployed code carries the bug (impl unverified, `UNVERIFIED_SOURCE`, local rebuild differs only by metadata).

`CoreVault.totalAssets() = getAUM()` also lets AUM exceed vault assets, so the last exiters can be underpaid; the reachable ceiling is the vault's balance, **$6,947.93**.

## Status and PoC

No Foundry PoC (the finding is a code-level invariant: AUM is not bounded by vault assets). To verify: read the impl at `0x90f6…`, confirm the `== 0` branch pays `collateralDelta+dPNL` to `msg.sender`, and check `getAUM()` vs the vault's token balance. A fork PoC would need a live position owner, which the target does not have.

## Economics and risks

| Item | Value |
|---|---:|
| Vault balance (ceiling) | $6,947.93 |
| Capital | position-sized |
| Confidence | MEDIUM — net bounded by other LPs' capital and no PoC |

## Provenance

Batch S3-578 (priority 2), 2026-11-14; result `stage3/results/S3-578.json`; evidence `stage3/work/S3-578/blex_io_215a1fca_0xf14cBC/`.
