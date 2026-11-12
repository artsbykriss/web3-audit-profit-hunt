# EX-10 — MANTRA DEX: legacy stableswap pool does not normalize decimals

**Net for an unprivileged actor:** **~$24.55** (hard-capped by the pool's 58.68 USDC)
**Confidence:** MEDIUM — live wasm/state confirmed, exploit modelled offline because the wasm rebuild OOM'd
**Gate:** none
**Chain:** MANTRA Chain
**Status:** headline H-10 (slippage tolerance) and H-02 (multi-coin fees) are patched; sibling finding **H-06 is LIVE** in the legacy `o.ausdy.uusdc` StableSwap pool.

## Contract / pool

| Item | Value |
|---|---|
| Pool Manager contract | `mantra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqagspfm` |
| code_id / version | 34 / `mantra:pool-manager1.2.0` |
| wasm sha256 | `1d93399a5bbd14ff706e2bb36dcdbb36fc7c78d2c0a6a450a5a90ed1b40b52c1` |
| Pool | `o.ausdy.uusdc` StableSwap, amp 85, decimals [18, 6] |
| Assets | 7,513,531,758,647,054,455 AUSDY (7.5135) / 58,682,467 USDC (58.682467) |
| LP supply | 28,048,317,707,843,537 |

## Bug

`compute_d` in the v1.2.0 pool-manager uses raw `Coin.amount` without decimal normalization. For a pool with assets of different decimals (18 and 6), the invariant is computed on incomparable units. An AUSDY deposit therefore mints inflated LP shares, which can be withdrawn pro-rata for USDC.

Live code hash and pool state confirm the legacy pool is deposit/withdraw/swap-enabled. v2.0.0 adds `compute_d_with_pool_info` / `normalize_amount`, but existing v1.2.0 pools remain live.

## Step-by-step

```
source 19 AUSDY on the sibling xyk pool
provide_liquidity(o.ausdy.uusdc, [19 AUSDY, 1 USDC], slippage_tolerance omitted)
// minted 57.1% of LP supply
withdraw_liquidity(57.1% LP)
// receive 34.08 USDC + 15.14 AUSDY
// net ~$24.55 after sourcing AUSDY
```

## PoC

`stage3/work/S3-762/mantra_dex_mantra14/poc/exploit_model.py` — offline model using the live pool state. The wasm rebuild OOM'd, so the exploit is modelled rather than executed on a local chain.

PoC output: 19 AUSDY + 1 USDC → 57.11% LP → 34.08 USDC + 15.14 AUSDY; net $24.55.

## Economics

- Deposit 19 AUSDY + 1 USDC; withdraw 34.08 USDC + 15.14 AUSDY.
- Net ~$24.55 after sourcing AUSDY on the sibling pool.
- Hard cap: the pool holds 58.68 USDC; larger deposits cannot extract more.
- Other LPs lose the value.

## Evidence

- MANTRA LCD: contract code_id 34; history INIT code 6, MIGRATE code 9, MIGRATE code 34.
- wasm sha256 matches; string `mantra:pool-manager1.2.0`.
- Pools query 2026-11-12: `o.ausdy.uusdc`, amp 85, decimals [18,6], assets/LP as above; deposits/withdrawals/swaps enabled.
- GitHub MANTRA-Chain/mantra-dex tag v1.2.0: `compute_d` uses raw `Coin.amount`; v2.0.0 adds normalization.
- PoC output in `evidence/poc_output.txt`.

## Risks / caveats

- MEDIUM because the wasm rebuild failed; the model uses the live code hash/state and the v1.2.0 source.
- The pool is small (58.68 USDC), so the prize is capped at ~$24.55.
- If the pool is migrated/disabled or v2.0.0 normalization is backported, the path closes.

## Handover

1. Re-read the pool state and code_id on MANTRA LCD.
2. Rebuild the v1.2.0 wasm (or run a local chain) and execute the deposit/withdraw; confirm the 57.1% LP mint and the 34.08 USDC withdrawal.
3. Check `slippage_tolerance` omission and pool enable flags.
4. If the pool is still live, this is a small but real unprivileged drain.
