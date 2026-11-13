# EX-15 — Inverse Finance sDOLA: timed liquidation harvest (V2 LlamaLend)

**Chain:** Ethereum mainnet (chain id 1)  
**Class:** timing-gated liquidation opportunity (keeper economics — **not a code vulnerability**)  
**Economic ID:** EX-15  
**Measured peak net:** **~$14,337** (atomic batch at +120 days, before the 0.05% flash fee)  
**Confidence:** MEDIUM (timing and rate assumptions; every leg fork-verified)  
**Gate:** time + flash liquidity (Aave crvUSD capacity)  
**Pinned state:** block **26,407,583** · 2026-11-13 **17:37:23 UTC** (unix `1794591443`)

---

## 1. One-paragraph summary

The Inverse sDOLA V2 LlamaLend market carries **33 loans / 10,579,291 crvUSD of debt** against **7,951,535 sDOLA** of collateral, all sitting at 93–99% LTV. Nothing is liquidatable at the pinned block (`users_to_liquidate(0,1000) = 0`), and **no outsider can force a liquidation**: the collateral oracle does not read the sDOLA LLAMMA, the LLAMMA holds zero crvUSD so a dump returns nothing, and selling sDOLA into the SaveDola oracle pool costs 10%+ without moving the EMA. What *does* happen is that interest accrues while collateral is static, so each loan crosses into negative health on a computable schedule. The first crosses on **2027-01-16 10:03:25 UTC**; the batch of liquidatable loans peaks around **2027-03-13**, where a fully atomic flash cycle nets **+$14,337** before the flash fee. The edge is purely *when* you execute: too early the loan is healthy, too late it is underwater and the 1% `liquidation_discounts` bonus no longer covers the debt.

---

## 2. Live state that matters

| Item | Address | Pinned value |
|---|---|---|
| sDOLA (ERC4626, asset DOLA) | `0xb45ad160634c528Cc3D2926d9807104FA3157305` | PPS 1.4297448; totalAssets 18.92M; supply 13.23M |
| V2 Controller (market) | `0xC77d97cF01737EB7aCE46cAb7cd9F60eC51a40c0` | n_loans 33; total_debt 10,579,291.49 crvUSD; available_balance 1,215,621 crvUSD |
| LLAMMA (crvUSD/sDOLA) | `0xbf6f64B741164c26023f97fAaEA8e02453c27442` | 7,951,534.94 sDOLA · **0 crvUSD** · A=285 · fee 0.2% |
| Collateral oracle (ERC4626EMAWrapper) | `0x0117ba42D18EaC940b469F81eD0a135ca23A1003` | price 1.424776 = PPS × base × agg |
| Base oracle (CrvUSDAggregatorWrapper) | `0xA4414fa8ac7a76425F496BC2D6F7d388317149e9` | 0.9966 crvUSD/USD leg |
| OracleFromCurvePools | `0x22cBFD0f788c75F52e3a3f1Fe379dE2833996EDD` | reads SaveDola `price_oracle(0)` |
| SaveDola pool (scrvUSD/sDOLA, **exit venue**) | `0x76A962BA6770068bCF454D34dDE17175611e6637` | 2.93M sDOLA / 1.88M scrvUSD, A=1000, fee 0.04% |
| scrvUSD (savings crvUSD, redeem 1:1.1133) | `0x0655977FEb2f289A4aB78af67BAB0d17aAb84367` | PPS 1.1133136 |
| DolaSavings (holds the DOLA) | `0xE5f24791E273Cb96A1f8E5B67Bc2397F0AD9B8B4` | 18,938,269.85 DOLA |
| crvUSD | `0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E` | — |
| Aave V3 Pool / aEthcrvUSD (**flash source**) | `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2` / `0xb82fa9f31612989525992fcfbb09ab22eff5c85a` | supply **95,583.36 crvUSD** |

Liquidation parameters: `liquidation_discount = 1%` per loan (`liquidation_discounts(user) = 1e16`), `loan_discount = 1.3%`, `MAX_RATE = 43,959,106,799` (per-second rate ceiling).

Why no outsider can trigger a liquidation early (all fork-proven):

- The collateral price chain is `sDOLA PPS × OracleFromCurvePools × crvUSD aggregator`. **The sDOLA LLAMMA is not in it.**
- The LLAMMA holds 0 crvUSD. Selling 1,000,000 sDOLA into it returns **0 crvUSD** and moves price/health by nothing. Donating 2,000,000 crvUSD to the AMM first changes nothing (band accounting, not balances).
- Selling 500k sDOLA into SaveDola costs **−$73,778** in slippage and moves the pool `price_oracle` and wrapper price by **0 wei** in-block. 1M/2M/5M are the same.
- Therefore the only route is **waiting for interest**.

---

## 3. Exact liquidation calendar

Computed on a fork pinned at block 26,407,583, scanning health() second-by-second (3-day scan then binary search to the second) with **no state changes, constant borrow rate, constant PPS growth**. `Unix` is the first second at which `health(user, true) < 0`. Dates are UTC.

| Loan idx | Loan address | First liquidatable (UTC, exact second) | Unix | +days from pin | Debt (crvUSD) at crossing | Collateral (sDOLA) | ~1% bonus |
|---:|---|---|---:|---:|---:|---:|---:|
| 24 | `0xBAC70E2De3D883fcDc3b6e2e0841ea8bC067B4f5` | 2027-01-16 10:03:25 UTC | 1800093805 |  63.68 | 211.39 | 150.69 | ~$2 |
| 25 | `0x2D57740EE18594bCbfa845703FaD49882e1567d9` | 2027-01-26 07:45:33 UTC | 1800949533 |  73.59 | 160,192.87 | 114,111.88 | ~$1,602 |
| 28 | `0xD77FD38ECB4E231a4d7259eFC7285eA6799bA597` | 2027-02-08 15:18:43 UTC | 1802099923 |  86.90 | 152,174.98 | 108,494.35 | ~$1,522 |
| 22 | `0x2e598EB2703069EbaaBEc95adCf684BC12A3EaFd` | 2027-02-16 10:30:41 UTC | 1802773841 |  94.70 | 825,531.82 | 588,049.36 | ~$8,255 |
| 2 | `0xD4f9FE0039Da59e6DDb21bbb6E84e0C9e83D73eD` | 2027-03-06 22:21:17 UTC | 1804371677 | 113.20 | 516.27 | 368.27 | ~$5 |
| 27 | `0xcBcC2b2eCD195eBEF03Fcb7c7564e4E906485A14` | 2027-03-17 22:31:53 UTC | 1805322713 | 124.20 | 184,123.05 | 131,201.90 | ~$1,841 |
| 26 | `0x9c0D1F4a029c46265831D120DeE9CDc72F0aB3C3` | 2027-03-21 10:49:43 UTC | 1805626183 | 127.72 | 131,591.15 | 93,793.34 | ~$1,316 |
| 19 | `0x351e08d66651b36cA65f23B4458A7652b9923ebB` | 2027-03-22 20:16:19 UTC | 1805746579 | 129.11 | 5,415.31 | 3,860.31 | ~$54 |
| 17 | `0xa8c2D5698334DcDCbBb04f25C5Bc8D8301A9A660` | 2027-03-24 02:12:03 UTC | 1805854323 | 130.36 | 59,981.91 | 42,763.32 | ~$600 |
| 6 | `0xE2D7d6c3a0dCad074044d6a5E1A201dBbb320F8b` | 2027-04-14 03:24:53 UTC | 1807673093 | 151.41 | 279,549.62 | 199,283.21 | ~$2,795 |
| 8 | `0xbadA9c382165b31419F4CC0eDf0Fa84f80A3C8E5` | 2027-04-22 10:20:24 UTC | 1808389224 | 159.70 | 2,836.77 | 2,035.55 | ~$28 |
| 3 | `0xE3053cDe2124eAA6103DddE8E5c6BD36c66F716E` | 2027-04-27 15:22:26 UTC | 1808839346 | 164.91 | 21,584.15 | 15,377.42 | ~$216 |
| 13 | `0x0C8ac71C2052366593f695EBCAA409bd3039c0F4` | 2027-04-28 10:43:14 UTC | 1808908994 | 165.71 | 5,677.85 | 4,104.55 | ~$57 |
| 29 | `0xF5ac22Cb3615cE273E026B6e65DA7F7efe86d065` | 2027-04-30 00:15:45 UTC | 1809044145 | 167.28 | 41,215.63 | 29,367.45 | ~$412 |
| 32 | `0x0d063135f757e128A63e068ADe3B1ee23A3b7eDe` | 2027-05-15 22:20:53 UTC | 1810419653 | 183.20 | 4,328.87 | 3,083.62 | ~$43 |
| 21 | `0x62dFA6eBA6a34E55c454894dd9b3E688F88CB09b` | 2027-05-18 10:55:46 UTC | 1810637746 | 185.72 | 20,423.93 | 14,550.00 | ~$204 |
| 10 | `0x80C67fe70d7D6cC488782439fad381d8646640c4` | 2027-05-27 19:41:57 UTC | 1811446917 | 195.09 | 671,967.35 | 479,003.94 | ~$6,720 |
| 15 | `0xe9c0DF9BD4607850d410C957FeC11eC209De5Ef6` | 2027-05-29 21:32:00 UTC | 1811626320 | 197.16 | 541,039.78 | 385,750.76 | ~$5,410 |
| 16 | `0xc8C17710ac7B51e1F49080e0555495DA64Ddd2db` | 2027-06-18 15:48:19 UTC | 1813333699 | 216.92 | 10,901.76 | 7,770.93 | ~$109 |
| 14 | `0x6dB248100cF4908429AB671F33D105311ED7fEF8` | 2027-08-14 10:41:09 UTC | 1818240069 | 273.71 | 1,489,758.25 | 1,061,255.72 | ~$14,898 |
| 0 | `0xe32a8CF93AF8661Ec4708ef627b255801184ad2f` | 2027-10-08 09:00:34 UTC | 1822986034 | 328.64 | 1,402,954.44 | 1,000,000.00 | ~$14,030 |
| 31 | `0x1BC8C6c06a43e3fbB2EbC613e0eBC0EcB95B5937` | 2027-10-19 02:05:58 UTC | 1823911558 | 339.35 | 422,446.00 | 303,122.26 | ~$4,224 |
| 9 | `0x7552bCD1d045eABCB304d34f0574A9e3c7C8F9f1` | 2027-11-01 10:39:27 UTC | 1825065567 | 352.71 | 819,488.70 | 584,186.84 | ~$8,195 |
| 18 | `0xf91312d72B2b91d370d7006922A6E4fdc27617A0` | 2027-11-19 13:55:56 UTC | 1826632556 | 370.85 | 1,282,391.30 | 913,841.46 | ~$12,824 |

**First liquidation in the entire market: 2027-01-16 10:03:25 UTC** (`0xBAC70E2De3D883fcDc3b6e2e0841ea8bC067B4f5`, 150.69 sDOLA / 211.39 crvUSD debt — the profit is only ~$4, so it is a rounding error operationally).

Loans **not** liquidatable within 420 days (health too high; the 2.09M-debt one needs years):

| idx | Loan | Debt (crvUSD) | Collateral (sDOLA) |
|---:|---|---:|---:|
| 23 | `0x2a691723fa94b2e38c1cda37dc64c7298f73378d` | 2,086,742.53 | 1,622,112.04 |
| 4 | `0x82eebbf1cc7fde025506aafa7898b8b66e11a003` | 91,855.97 | 80,083.55 |
| 12 | `0x3fe2461f7cb328629f2924993c6218748c740c83` | 91,001.35 | 69,329.73 |
| 7 | `0xada66e3d530fb2febab1da1e6a1b0404b922a6e2` | 60,914.66 | 48,028.15 |
| 11 | `0xa1183e8a5d852f06b3a1c6d52ae4b5ef5bc9c12e` | 32,287.23 | 24,597.38 |
| 5 | `0x3e258aae11d7ea394b2eb1176ccd54d9eb83861b` | 18,866.73 | 14,798.88 |
| 30 | `0xeab5b236d05545ef7e1671902ca8fffa194c1d3a` | 6,253.32 | 4,900.40 |
| 1 | `0x10a865480236c40eb9683038d9c072d88b51b758` | 3.26 | 2.82 |
| 20 | `0x4a5206e0416bd8df3f2a73bfc8d29bcfec909984` | 2,512.93 | 2,154.84 |

---

## 4. Measured economics (fork, end-to-end)

Each row is a full atomic cycle executed on the fork: `deal` crvUSD (stand-in for flash capital) → `liquidate()` every unhealthy loan → `SaveDola.exchange(1,0,seized,0)` → `scrvUSD.redeem()` → crvUSD. Net is **crvUSD out − crvUSD in**, before the flash fee.

| Horizon | Date | Liquidations | crvUSD in | sDOLA seized | crvUSD out | **Net** |
|---|---:|---:|---:|---:|---:|---:|
| +64 d | 2027-01-16 | 1 | 211.40 | 150.69 | 215.50 | **+$4.09** |
| +90 d | 2027-02-11 | 3 | 313,081.03 | 222,756.92 | 318,490.19 | **+$5,409.12** |
| **+120 d** | **2027-03-13** | **5** | **1,144,385.93** | **811,174.55** | **1,158,723.03** | **+$14,337.10** |
| +150 d | 2027-04-12 | 7 | 1,193,131.99 | 843,097.17 | 1,203,771.43 | +$10,317.45 |
| +180 d | 2027-05-11 | 9 | 1,214,337.20 | 855,992.69 | 1,222,114.28 | +$7,587.69 |
| +240 d | 2027-07-10 | 11 | 1,635,713.15 | 1,154,868.27 | 1,644,616.95 | +$10,576.04 |
| +360 d | 2027-11-08 | 13 | 5,382,991.63 | 3,785,760.83 | 2,093,211.63 | −$3,290,778.70 |

Notes on the table:

- The batch is **cumulative** — the +120 d row includes every loan that crossed up to then. Waiting past the peak *loses* money because the same positions sink further underwater.
- The +360 d figure liquidates loans that are already deeply underwater; a rational agent would skip those, so it is a decay illustration, not a strategy.
- Flash fee at 0.05% is not deducted: −$156 at +90 d, −$572 at +120 d.
- Gas is <$1 per transaction on mainnet at 5 gwei.
- Liquidation changes the AMM and can rescue other positions: at +180 d, 9 loans liquidated in sequence vs 14 if measured independently.

---

## 5. Execution playbook (for the next agent)

### 5.1 Preconditions to re-verify at execution time

1. `users_to_liquidate(0,1000)` from the Controller — non-empty, or your target loan's `health(user,true) < 0`.
2. `liquidation_discounts(user)` — must still be > 0 (1% now).
3. SaveDola `get_dy(1,0,seized)` — the exit must return ≥ the debt you are about to pay. This is the decisive check; if the pool is drained or skewed, skip.
4. Aave `crvUSD.balanceOf(0xb82fa9f31612989525992fcfbb09ab22eff5c85a)` — must exceed the slice size.
5. Recompute the crossing: rates changed since this writing, so the calendar in §3 shifts. Use `health(user,true)` and `liquidate_health_preview(user, caller, frac, true)`.

### 5.2 Atomic cycle (one slice)

```
1. AaveV3.flashLoanSimple(receiver, crvUSD, amount = min(debt*frac, 95_000e18), params)
2. inside executeOperation:
     crvUSD.approve(controller, amount)
     controller.liquidate(user, min_x = 0, frac)            // frac*debt ≈ amount
        -> collateral sDOLA is transferred to the receiver
     sDOLA.approve(SaveDola, max)
     SaveDola.exchange(1, 0, sDOLA_balance, min_out)        // 1 = sDOLA, 0 = scrvUSD
     scrvUSD.redeem(scrvUSD_balance, receiver, receiver)    // -> crvUSD
     crvUSD.approve(AavePool, amount + fee); return true
3. profit = crvUSD balance - fee
```

- **Flash capacity is the binding constraint**: ~95,583 crvUSD on Aave V3 is the only meaningful crvUSD flash source (Balancer vault holds 4.19 crvUSD; Uniswap V3 crvUSD pools hold <$1.5k). Most loans are larger, so use the `_frac` argument: `frac = 95_000e18 / debt` and loop. `liquidate_health_preview` gives the resulting health for a given frac.
- `min_x` is the AMM-withdraw slippage guard; positions at the top of the book return 0 crvUSD there, so 0 is safe but set a real `min_out` on the SaveDola swap — that is where the money is lost.
- Do **not** redeem sDOLA to DOLA directly: DOLA has almost no market (best Curve pool $13.5k, Uniswap V3 DOLA/USDC $170). The sDOLA→DOLA path is a dead end unless you have an OTC buyer.

### 5.3 Sizing and expected yield

Per loan, at the moment it first crosses, the liquidator's gross is ≈ **1% of the repaid debt** (`liquidation_discounts`), i.e. ~$1,600 on the 160k loan, ~$8,255 on the 825k loan. The measured batch peaks at +120 d because several loans cross within a few weeks of each other. Profit does **not** scale linearly with waiting: after health < −1% the loan is underwater and liquidation is a loss.

---

## 6. Reproduction (exact commands)

PoC directory: `/workspaces/CA/stage3/work/S3-278/inverse_sdola/poc`

```bash
cd /workspaces/CA/stage3/work/S3-278/inverse_sdola/poc
export FORK_RPC="https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY_2"

forge test -vv --match-contract When        # day-granularity first crossing
forge test -vv --match-contract Crossings   # exact-second crossing per loan (pinned block 26,407,583)
forge test -vv --match-contract RoundTrip   # end-to-end atomic cycle at 64/90/120/150/180/240/360 d
forge test -vv --match-contract OraclePush  # proves the oracle cannot be pushed (500k-5M sells, 0 wei move)
forge test -vv --match-contract ListLoans   # per-loan debt/collateral of the unhealthy set
```

Sources used for review are saved under `.../evidence/src/{controller,amm,wrapper}/` (verified Vyper from Etherscan V2, block-pinned reads via Alchemy).

---

## 7. Risks, caveats and why the label is MEDIUM

1. **Rates move the calendar.** Crossings assume the current borrow rate (utilization-driven). A large repayment, a new borrow, or a monetary-policy change shifts every date in §3. Recompute before acting; the table is a schedule, not a commitment.
2. **PPS growth is non-monotonic.** sDOLA distributes weekly revenue, so PPS jumps weekly and health is not strictly monotonic. The binary search handles it, but a loan can cross, recover for a few days, and cross again.
3. **Liquidation changes the book.** Each `liquidate` removes bands from the AMM and can rescue other positions; measured 9 vs 14 unhealthy at +180 d depending on order. Do not assume the whole set is harvestable at once.
4. **Exit is single-venue.** All profit depends on SaveDola absorbing the seized sDOLA at ~1.28 scrvUSD (= 1.4286 crvUSD with PPS 1.1133). If that pool is drained or rebalanced, the trade is negative.
5. **Flash is capacity-bound.** 95.6k crvUSD per transaction; larger loans require `frac` slicing and multiple transactions, each paying gas and slippage.
6. **Not a vulnerability.** This is the protocol's designed 1% liquidation incentive on loans that genuinely decay. There is no manipulation, no privilege, and no third-party fund drain beyond the market's own liquidation rules. Disclose it as keeper economics, not as an exploit.
7. **Structural observation for the protocol:** the LLAMMA holds 0 crvUSD, so soft liquidation is unavailable and the market depends entirely on hard liquidations with external crvUSD. That is a liveness risk worth reporting to Inverse, separate from this timing opportunity.

---

## 8. Provenance

- First identified as a MEDIUM negative in batch **S3-278** (target S3-2044) on 2026-11-13; the open question was whether a dump-then-liquidate sequence was profitable.
- Fork PoC (block 26,407,583) closed the manipulation question on 2026-11-13: 0 crvUSD in the LLAMMA, 0-wei oracle movement under 500k-5M sells, `users_to_liquidate = 0`.
- Reclassified to **EXTRACTABLE_MEDIUM / EX-15** by explicit operator decision on 2026-11-13: the timing path is live, unprivileged, and measured at +$14,337 peak.
- Result file: `stage3/results/S3-278.json` (target S3-2044) · master log row: `stage3/MASTER_LOG.csv` · PoC: `stage3/work/S3-278/inverse_sdola/poc/`.
