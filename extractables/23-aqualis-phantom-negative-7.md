# EX-23 — Aqualis: negative `totalSuppliedToLending` captured via AMU normalisation

**Chain:** Metis (1088) · **Target:** S3-3164 / S3-3165 (duplicate rows, one economic id) · **Address:** `0xaf14302087De6d467111059332CB9a41d9aea7bf` (AqualisSPProxy → patched impl `0x9A3C`), exploitable on sibling `0x88C16c1Cb3C50E06979ED19Cea7649a8cfcd5A00` (impl `0x8935`, older, no clamp)  
**Economic ID:** EX-23 · **Net:** **+$7.42** after gas (fork-proven $7.5056 gross) · **Confidence:** MEDIUM (one-shot, $42.6k capital for ~5 blocks) · **Gate:** capital

## Mechanism

The older sibling impl carries `totalSuppliedToLending = -20.688` with no clamp. A 42,600 m.USDT `createSP` pushes TVL to 44,078; `AqualisConfig.checkAMUAction` then returns `DEPOSIT 4,000`, which sets `totalSuppliedToLending` to +4,000 and erases the phantom. After the 5-block cooldown the depositor redeems 42,332 SP in chunks for **42,607.5 m.USDT = +$7.5056 gross**, ~$7.42 after ~2.1M gas at 15.8 gwei (METIS $2.36). The $42,600 principal is fully recovered.

Both audited headlines are **PATCHED** in the live lead impl (`createSP` divides by the pre-deposit share price; `redeemSPOnDepeg` multiplies by it; H-04 burn present); the extractable path is the sibling pool's accounting. Subsumed alternatives: AqualisLegacySPRedeem pays 1.01 m.USDT/AQLSP vs 1.00574 mint (max +$0.43), and the lead pool's 1.0 share-price floor adds +$0.0645.

## PoC

`stage3/work/S3-585/aqualis/poc` — fork at Metis block 23,411,794: deposit → cooldown → chunked redeem; net +$7.5056. One-shot: a second run loses $12.49 because the phantom is consumed.

## Risks

1. One-shot and capital-heavy ($42.6k locked ~5 blocks).
2. Sibling impl unverified; accounting read from live storage.
3. MEDIUM confidence; the fork net is measured.

## Provenance

Batch S3-585, 2026-11-14; result `stage3/results/S3-585.json`; both target rows share this economic id.
