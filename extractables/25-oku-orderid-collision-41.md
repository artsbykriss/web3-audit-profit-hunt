# EX-25 — Oku: order-ID collision double refund (two v1 escrows)

**Chain:** Optimism (10) · **Targets:** S3-3308 + S3-3310 (one economic id) · **Contracts:** v1 `AutomationMaster 0x09f1e409…` → Bracket `0xA90307…` / StopLimit `0x5320E4…` (the batch leads `0xCaE450` and `0xfdcFdd` are the patched v2 masters)  
**Economic ID:** EX-25 · **Net:** **$41.30** combined (Bracket $22.99 + StopLimit $18.23) · **Confidence:** HIGH (fork-proven) · **Gate:** capital (~$41, returned)

## Mechanism

`AutomationMaster.generateOrderId` is `keccak256(abi.encodePacked(sender, block.timestamp))` with no per-order nonce; both sub-keepers push the id into `pendingOrderIds` without a uniqueness check, and `_cancelOrder` refunds the full `amountIn` for every array entry with that id. Two orders created by the same sender in the same block therefore share an id, and cancelling both refunds the same escrow twice.

The audited H-7/H-5 defects are patched in the v2 masters, but the older v1 generation still holds user escrow and carries the bug. Fork test at Optimism block **159,533,765** as a fresh EOA: **+39.38 USDC + 0.0009996 WETH**, all three escrows zeroed, gas under $0.01, capital ≈41 USDC returned.

## PoC

`stage3/work/S3-594/oku_orderid_collision/poc` — 8/8 tests pass: create two same-block orders, cancel both, observe the double refund.

## Economics

| Escrow | Value |
|---|---:|
| Bracket | $22.99 |
| StopLimit | $18.23 |
| **Total** | **$41.30** |

One-shot per escrow pair; repeatable only while fresh escrow is funded. HIGH confidence because the fork pays as a fresh EOA.

## Remediation

Include a nonce in `generateOrderId` and enforce uniqueness in `pendingOrderIds`; migrate the v1 escrows.

## Provenance

Batch S3-594, 2026-11-14; result `stage3/results/S3-594.json`; work folder kept.
