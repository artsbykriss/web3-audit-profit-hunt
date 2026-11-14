# EX-17 — Doomsday Settlers: `confirmDisaster()` pays any caller 0.01 ETH

**Chain:** Ethereum mainnet (chain id 1)  
**Class:** unprivileged one-shot payout + third-party NFT burn (no capital, no role)  
**Economic ID:** EX-17  
**Net:** **+$19.12** per claim (0.01 ETH at $1,914.60, gas 151,621 ≈ $0.024)  
**Confidence:** MEDIUM (the vulnerability window recurs, but the claim is one-shot)  
**Gate:** none (timing window only)  
**Target:** S3-1792 · `0xB4CbA31bDAf6FF6e34eFC0CFC4906Bd29b0146E9` (DoomsdaySettlers, verified, solc 0.8.18, 24,259 bytes)  
**Pinned state:** fork block 26,364,225

---

## 1. Summary

Doomsday Settlers is in its endgame: `isDarkAge() = true`, `totalSupply = 2` (settlements 2246 and 2247), last settlement 2247. Its `confirmDisaster(uint32,uint32)` is callable by **any EOA** — no ownership of the token, no role, no capital. When `DoomsdaySettlersDarkAge.disaster()` passes its vulnerability check, the function:

1. burns the settlement NFT, and
2. pays `DESTRUCTION_FEE = 0.01 ETH` to `msg.sender`, unconditionally.

A fresh EOA called it on a fork and received exactly 0.01 ETH. The victim NFT (2247) is owned by `0xA4f6638Cde88f245B75670B510FD8e46fAFD1678`; the caller does not need it.

The claim is **one-shot**: the burn leaves `totalSupply = 1` and ends the dark age, so the game cannot be farmed repeatedly. The window is intermittent — token 2247 was vulnerable in **181 of 672 sampled 75-block windows** over the last 7 days — so timing is the whole edge.

The audited headline (weak PRNG in `settle()`) is still live in code, but `settle()` reverts `"dark age"`; it is not the payout path.

---

## 2. Exact live state

| Item | Value |
|---|---|
| `isDarkAge()` | true |
| `totalSupply()` | 2 (ids 2246, 2247) |
| `miningState()` | lastSettleBlock 17,908,610 · collapseBlock 17,915,808 |
| ownerOf(2246) | `0x015945Da2cEA827272a04FDBc2e1e3Fb8d9d8754` |
| ownerOf(2247) | `0xA4f6638Cde88f245B75670B510FD8e46fAFD1678` |
| `DESTRUCTION_FEE` | 0.01 ETH |
| Contract balance / escrow | funds the 0.01 ETH payout |

Vulnerability recurrence: scanning the last 7 days in 75-block windows, 2247 satisfied `DarkAge.disaster()` in **181 / 672** windows. When the condition is false the call reverts; when true it pays.

---

## 3. PoC (fork-proven)

`stage3/work/S3-413/doomsday/`:

- `poc/test/DoomsdayPoC.t.sol` — fresh EOA `0x1234` calls `confirmDisaster(2247, 2246)` at block 26,364,225.
- Result: caller balance **+0.01 ETH exactly**, `totalSupply` 2→1, dark age ends; gas used 151,621.
- `evidence/fork_trace_block26364225.txt` and `forge_test_result.txt` contain the trace and forge output.

```bash
cd /workspaces/CA/stage3/work/S3-413/doomsday/poc
forge test --fork-url "$ETH_RPC" --fork-block-number 26364225 -vv
```

Reproduction check before acting: call `isDarkAge()` and simulate `confirmDisaster(2247,2246)` from a fresh address at the latest block; if it reverts, rescan for the next vulnerable window.

---

## 4. Economics

| Item | Value |
|---|---:|
| Payout | 0.01 ETH = $19.15 (ETH $1,914.60) |
| Gas | 151,621 @ 81.25 gwei = 0.0000123 ETH ≈ $0.024 |
| **Net** | **≈ $19.12** |
| Capital | 0 |
| Repeatability | one-shot (ends the dark age) |

This is a small, one-time payout. It qualifies under the >$5 rule but is not a scalable drain; the value is in closing the finding.

---

## 5. Risks and caveats

1. **Window timing.** The disaster check is only true in some blocks (181/672 sampled). A failed call costs gas; simulate first.
2. **One-shot.** The burn ends the dark age; there is no second claim.
3. **Third-party NFT burn.** The call destroys 2247 owned by someone else — an unprivileged actor can do this without owning it. That is the actual defect.
4. **MEDIUM confidence** because the payout depends on the intermittent `DarkAge.disaster()` condition; the mechanism and the fork trace are exact.

---

## 6. Provenance

- Stage 3 batch **S3-413**, target **S3-1792**, 2026-11-14.
- Result: `stage3/results/S3-413.json`; PoC and evidence kept under `stage3/work/S3-413/doomsday/`.
- Ledger: **EX-17**, $19.12.
