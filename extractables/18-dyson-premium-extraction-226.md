# EX-18 — Dyson Finance DYSN/USDC: premium paid out of pool reserves

**Chain:** Polygon zkEVM (chain id 1101)  
**Class:** unprivileged arbitrage inside one pool (note premium funded by reserves)  
**Economic ID:** EX-18  
**Net:** **+$226.897895 USDC** per cycle, fresh EOA, no gate  
**Confidence:** HIGH (fork-proven, exact bytecode match)  
**Gate:** capital (refundable; $22,577.49 for 1 day or $4,122.07 for 30 days)  
**Target:** S3-1804 · `0xC9001AFF3701e19C29E996D48e474Baf4C5eD006` (Dyson V1 Pair, 13,298-byte runtime)  
**Pinned state:** block 33,391,890

---

## 1. Summary

The deployed pair is the audited Dyson V1 `Pair` bytecode (13,298 bytes, identical outside the `DOMAIN_SEPARATOR` immutable). `deposit0`/`deposit1` book a note at the **simulated swap amounts plus a lock-time premium without executing the swap**, and `withdraw` lets the note owner take whichever leg is worth more. With `feeRatio = 0`, the token1 leg equals `deposit × (1 + premium)`, and `_withdraw` pays that leg **out of the pair's own reserve**.

A fresh EOA deposited **22,577.490710 USDC** for a 1-day lock and withdrew **22,804.388605 USDC** — net **+226.897895 USDC**, which is the pair's entire USDC reserve (1 wei left). A 30-day note reaches the same profit with only **4,122.066984 USDC** of capital.

The headline (Decurity 4.1 "arbitrage inside one pool") is **LIVE**, not merely analogous. The original 2.5× sequence does not transplant (it needs a much larger reserve), but the underlying defect does.

---

## 2. Exact live state (block 33,391,890)

| Item | Value |
|---|---|
| Pair | `0xC9001AFF3701e19C29E996D48e474Baf4C5eD006` |
| Reserves | 23,217.144891592640172332 DYSN · **226.897896 USDC** |
| Token balances | equal reserves; `accumulatedFee = 0` |
| `getFeeRatio()` | (0, 0) |
| `halfLife` | 720 |
| `basis` | 0.48e18 |
| `getPremium(1 days)` | 1.0049739313732103e16 ≈ **1.005%** |
| Sibling `allPairs(0)` | `0xEce7244a0e861C841651401fC22cEE577fEE90AF` — bricked (`getReserves()` underflow), ~$280.91 unreachable |

The USDC reserve is the binding constraint: the extraction pays out the whole 226.897896 USDC.

---

## 3. PoC (fork-proven)

`stage3/work/S3-415/dyson-dysn-usdc/`:

- `poc/test/` — `testPremiumExtraction1Day`: deposit 22,577,490,710 USDC units → note `(token0Amt 23,217.144891586234624901 DYSN, token1Amt 22,804.388605 USDC, due +86,400)` → `withdraw` → end balance 22,804.388605 USDC → **net +226,897,895 (6dp)**; pair USDC left = 1 wei.
- `testPremiumExtraction30Day`: deposit 4,122,066,984 → same net +226,897,895 (longer lock).
- `evidence/bytecode_match.txt` — 13,351-byte build vs live, 13,298 bytes after CBOR strip, differing in exactly two 32-byte PUSH32 immediates (the DOMAIN_SEPARATOR).
- `evidence/live_state.txt`, `fork_test.log`.

```bash
cd /workspaces/CA/stage3/work/S3-415/dyson-dysn-usdc/poc
forge test --fork-url "$ZKEVM_RPC" --fork-block-number 33391890 -vv
```

---

## 4. Economics

| Scenario | Capital | Lock | Profit | Gas |
|---|---:|---|---:|---:|
| 1-day note | 22,577.490710 USDC | 1 day | **+226.897895 USDC** | ~738k @ 0.01 gwei ≈ $0.014 |
| 30-day note | 4,122.066984 USDC | 30 days | **+226.897895 USDC** | same |
| **Net** | refundable | — | **≈ +$226.88** | — |

The profit is exactly the pair's USDC reserve; the deposit is returned (the note is the claim). It is **one-shot per pool** — after withdrawal the USDC side holds 1 wei, so a repeat requires the pool to be refilled by other users.

---

## 5. Risks and caveats

1. **Drains the pool.** The extraction leaves 1 wei of USDC; it is a pool-killing trade, not a repeatable yield.
2. **Sibling risk.** `allPairs(0)` is bricked and holds ~$280.91 that nobody — including the attacker — can reach; do not count it as extractable.
3. **Liquidity timing.** The 1-day variant needs the full 22,577.49 USDC; the 30-day variant needs only 4,122.07 but locks capital for a month. If the pool is refilled, the premium math must be recomputed from `getPremium()` and current reserves.
4. **HIGH confidence**: exact bytecode match, two fork tests, live reserves read at a pinned block.

---

## 6. Provenance

- Stage 3 batch **S3-415**, target **S3-1804**, 2026-11-14.
- Result: `stage3/results/S3-415.json`; PoC and evidence kept under `stage3/work/S3-415/dyson-dysn-usdc/`.
- Ledger: **EX-18**, $226.90.
