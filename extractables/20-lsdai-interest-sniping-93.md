# EX-20 — LSDai: stale-pool interest sniping (deposit before `rebase()`, withdraw after)

**Chain:** Ethereum mainnet (chain id 1)  
**Class:** unprivileged one-shot yield capture via stale share accounting  
**Economic ID:** EX-20  
**Net:** **+93.2476 DAI** per cycle with a 27,700 DAI Balancer flash loan (gas ~$0.09)  
**Confidence:** HIGH (fork-proven, live state)  
**Gate:** none (capital is flash-loanable)  
**Target:** S3-2105 · `0xe1A70B24E109F7A8b39806c554E123Efc6769E91` (LSDai)  
**Pinned state:** fork block 26,411,115

---

## 1. Summary

`LSDai._deposit()` mints shares from the **stale** `_totalPooledDai` and never calls `rebase()` first. `rebase()` is permissionless. So a depositor who enters before a rebase and exits after it captures the DSR interest that accrued since the previous rebase, diluting existing holders.

The Team Omega 2023 report records that the developers made **no code change** — the 1 bp withdrawal fee plus regular `rebase()` calls were the intended mitigation. No one has called `rebase()` for long enough that **101.341364 DAI (12.6% of the 903.5 DAI pot)** sits unclaimed. The trade is profitable today and is a one-shot: after the attacker's own `rebase()`, accrual restarts at the DSR rate (~1.25%/yr on $903).

---

## 2. Live state (fork block 26,411,115)

| Item | Value |
|---|---|
| Stored pooled DAI (`_totalPooledDai`) | 802.175947326663384340 DAI |
| Pot value (`potShares` → DAI) | 903.517311427025630582 DAI |
| Accrued, unrebased interest | **101.341364100362246242 DAI** |
| `withdrawalFee()` | 1 bp |
| `interestFee()` | 250 bps |
| `depositCap()` | 0 (unlimited) |
| `rebase()` | permissionless (`eth_call` from `0x…dEaD` succeeds) |
| Owner functions | reverts `Ownable: caller is not the owner` |
| `initialize` | reverts `LSDai__AlreadyInitialized` |

---

## 3. Attack path (fork-proven)

`stage3/work/S3-454/lsdai/poc/test/LSDaiInterest.t.sol`:

1. Balancer Vault `flashLoan(DAI, 27,700)`.
2. `DAI.approve(LSDai)`; `LSDai.deposit(attacker, 27,700 DAI)` — shares priced on the stale pooled total.
3. `LSDai.rebase()` — permissionless; pot interest is realized into the share price.
4. `LSDai.withdraw(balanceOf(attacker))` — 1 bp fee.
5. Repay the flash loan; keep the difference.

Measured:

| Capital | Net profit | Note |
|---:|---:|---|
| 27,700 DAI | **93.247568758569395355 DAI** | optimal; gas 440,604 ≈ $0.09 |
| 10,000 DAI | 90.461700116085081285 DAI | |
| 50,000 DAI | 92.238039133816256634 DAI | |
| 100,000 DAI | fails | Balancer `BAL#528` (flash liquidity) |

`test_accrued_interest_visible` confirms the 101.34 DAI gap before the attack; `test_attack_optimal` produces the 93.2476 DAI net.

---

## 4. Economics

- One-shot per unrebased accrual window; the profit is bounded by accrued interest (101.34 DAI), not by capital.
- After the attacker's rebase, the next sniper must wait for new accrual; at ~1.25%/yr on a $903 pot that is cents per day.
- The deposit is refundable; only gas and the flash fee (Balancer 0%) are at risk.
- Because `rebase()` is permissionless, a keeper calling it frequently removes the opportunity — the protocol's own intended mitigation.

---

## 5. Remediation

1. Call `rebase()` inside `_deposit()` and `_withdraw()` (or before pricing shares), so shares are always priced on current assets.
2. Alternatively, accrue interest lazily in `balanceOf()` and `totalAssets()`.
3. Operationally, run `rebase()` on a fixed cadence (the current mitigation is only as good as the keeper).

---

## 6. Risks and caveats

1. **One-shot.** The measured 93.25 DAI is the current accrued backlog; after it is taken, the pot accrues at the DSR rate.
2. **Flash-liquidity bound.** Balancer rejected 100k DAI; 27.7k was optimal, 50k still worked but paid slightly less (fee/rounding).
3. **HIGH confidence**: exact live state, full end-to-end fork test, permissionless `rebase()` verified.

---

## 7. Provenance

- Stage 3 batch **S3-454**, target **S3-2105**, 2026-11-14.
- Result: `stage3/results/S3-454.json`; PoC: `stage3/work/S3-454/lsdai/poc`.
- Ledger: **EX-20**, $93.20.
