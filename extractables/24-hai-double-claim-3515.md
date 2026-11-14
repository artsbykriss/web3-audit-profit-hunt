# EX-24 — Let's Get HAI RewardDistributor: one leaf paid once per Merkle root

**Chain:** Optimism (10) · **Target:** S3-3241 · **Address:** `0xfEd2eB6325432F0bF7110DcE2CCC5fF811ac3D4D` (only RewardDistributor instance, verified)  
**Economic ID:** EX-24 · **Net:** **$3,515.89** (distributor pool, upper bound for an allocated double-claimer) · **Confidence:** MEDIUM (requires an allocated leaf; on-chain replay proven) · **Gate:** capital (KITE stake for allocation)

## Mechanism

`isClaimed` is keyed by `(root, account)`, and the root is republished roughly every 22 hours. An account already paid under root `R_n` is payable again under `R_(n+1)`; front-running `updateMerkleRoots` lets an allocated account claim the same leaf once per root. The batch address is the correct and only instance, and its code is identical to `hai-on-op/core` main, so the audited logic is live.

Direct on-chain evidence: the same KITE leaf (`3.585351473606806394 KITE`) was paid twice at different blocks (see `stage3/work/S3-591/hai_rewarddistributor/evidence`). Pool size at audit: **$3,515.89**.

## Attack outline

1. Hold an allocated leaf (KITE staking gives the allocation).
2. Claim under the current root.
3. Wait for the next root republication (~22h) and claim the same leaf again.
4. Repeat while the root rotates and the pool pays.

No contract call is privileged; the only cost is the KITE stake and gas.

## Risks and caveats

1. Requires an allocated address (capital gate); the $3,515.89 assumes the attacker can claim the full pool, which may be shared with other claimers.
2. Root cadence can change; the distributor can pause or migrate.
3. MEDIUM confidence: the double-pay is proven on-chain, but the extractable amount depends on allocation size.

## Provenance

Batch S3-591, 2026-11-14; result `stage3/results/S3-591.json`; evidence folder kept.
