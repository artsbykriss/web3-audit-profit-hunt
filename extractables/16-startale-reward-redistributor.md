# EX-16 — Startale RewardRedistributor: snapshot TVL inflation (Soneium)

**Chain:** Soneium (chain id 1868)  
**Class:** unprivileged yield-capture via TVL inflation around `snapshotVaultTVLs()` / `distribute()`  
**Economic ID:** EX-16  
**Net:** **+$15.18 per pre-snapshot attack** on a $2M deposit; **+$3.97 per post-snapshot JIT** on $1M  
**Confidence:** MEDIUM (fork-proven, but timing/capital dependent)  
**Gate:** capital ($1–2M) + landing the deposit in the operator's snapshot window  
**Target:** S3-1415 · `0xda798684ffD5eb509c2Ab7b8352EC55B31F18201` (RewardRedistributor, verified, 9,700 bytes, not a proxy)  
**Pinned state:** Soneium block 30,734,426 (fork), TVL read at block 30,740,435

---

## 1. Summary

Startale's `RewardRedistributor` snapshots each vault's TVL (`snapshotVaultTVLs()`) and later mint-and-credits the epoch yield (`distribute()`), which calls `EarnVault.onYield()`. The yield credited to a depositor is computed from the **current** vault principal, while the snapshot value drives the epoch allocation — so a large deposit placed on the right side of the snapshot captures a disproportionate slice of the epoch's yield, and the depositor withdraws immediately after.

Two fork-proven variants:

1. **Pre-snapshot capture** — deposit 2,000,000 USDSC before the operator's `snapshotVaultTVLs()`, hold through `distribute()`, withdraw. Net **+15,185,177 (6dp) = $15.18** for one 32,749,168 (6dp) epoch.
2. **Post-snapshot JIT** — deposit 1,000,000 USDSC *after* the snapshot but before `distribute()` (held ~6 seconds, blocks 30,734,429→430). Net **+3,969,852 (6dp) = $3.97**.

The operator distributes **7.83×/day** (1,000 `Distributed` events over 127.7 days), so the post-snapshot variant is repeatable ~8×/day; the pre-snapshot variant requires predicting the snapshot transaction.

This is not a key compromise and needs no role: anyone can deposit into the EarnVault. The profit is paid by honest EarnVault depositors and the treasury, and the attacker's principal is returned in full.

---

## 2. Live deployment map (Soneium, chain 1868)

| Role | Address | Notes |
|---|---|---|
| RewardRedistributor | `0xda798684ffD5eb509c2Ab7b8352EC55B31F18201` | verified; `snapshotVaultTVLs()`, `distribute()` OPERATOR_ROLE-gated |
| EarnVault proxy | `0xFdeB7e9F59cad080D9158ff850Ce79bCf6cdd5f0` | `deposit/withdraw/claimable`; impl `0x5a6ab092a02a945393c85118d5c07eabdd02cf08` |
| sUSDSC vault proxy | `0x938bca6c4281313Baa82154745E4d020E85E7340` | impl `0xde13186f7ff1173628ed5e15173d9e78e10ad6bb` (ERC-4626) |
| USDSC token proxy | `0x3f99231dD03a9F0E7e3421c92B7b90fbe012985a` | impl `0x38e4713a896efcf253430efd6292515dc13489a1`; `yieldRecipient = RewardRedistributor` |
| Operator EOA | `0x86bE13a26d548FA5407Ee3E5a8321B4E1019333C` | sole OPERATOR_ROLE; sends `snapshotVaultTVLs` + `distribute` in consecutive txs every ~5,400 blocks |

TVL at block 30,740,435: EarnVault USDSC **1,100,659,330,779** (6dp) + sUSDSC totalAssets 10,326,779,027 (6dp) = **$1,110,986.11**.

---

## 3. Mechanism, as observed

`distribute()` mints the epoch yield and forwards the EarnVault share through `onYield()`. The attacker's claimable is derived from the EarnVault principal at distribution time. In the fork run:

```
epoch yield (USDSC.yield())            32,749,168   (6dp)
lastEarnTVL before deposit             1,095,106,151,423
deposit                                2,000,000,000,000
lastEarnTVL after snapshot             3,095,816,257,882
distribute() -> claimable(attacker)    15,185,177
withdraw principal -> final profit     15,185,177   (6dp) = $15.18
```

The post-snapshot variant works because the snapshot is taken at block 30,734,427 and `distribute()` runs at 30,734,430: a deposit in between still counts toward the credited principal.

Reference epoch (tx `0x352761a9260406aac896dc3009d57fd1a44d1e84fc2108af58d4373757fad759`, block 30,739,830): minted 32,749,168, toEarnVault 8,320,082. Over 1,000 consecutive `Distributed` events: average minted **55.16 USDSC**, average toEarn **13.22 USDSC**, **7.83 distributions/day**.

---

## 4. Attack playbook

### Variant A — pre-snapshot (larger, timing-sensitive)

1. Hold ≥2,000,000 USDSC on Soneium.
2. Monitor the operator EOA `0x86bE…333C` for the pending `snapshotVaultTVLs()` transaction (consecutive with `distribute`).
3. In the same block before the snapshot (or as a bundle), `USDSC.approve(EarnVault)` and `EarnVault.deposit(X)`.
4. After the operator's `distribute()`, call `EarnVault.withdraw(X)`; the credited yield stays as `claimable`.
5. `claim()` the USDSC. Net = claimable ≈ X × epochYield / (T_earn + X), minus gas.

### Variant B — post-snapshot JIT (smaller, easier to land)

1. Watch for `snapshotVaultTVLs()` to be mined.
2. Immediately deposit into EarnVault before the next `distribute()` (usually the next transaction/block).
3. Withdraw right after `distribute()`; net ≈ X × epochYield / totalPrincipal × share, held for seconds.
4. Repeat each epoch (~7.8/day). $1M produced +$3.97 per epoch in the fork test.

Both variants leave the principal intact; only gas is at risk if the timing is missed.

---

## 5. PoC and reproduction

Files: `/workspaces/CA/stage3/work/S3-366/startale/`

- `poc/test/JIT3.t.sol` — pre-snapshot: deposits 2M, rolls to 30,734,427, operator snapshot, rolls to 30,734,430, operator distribute, claim/withdraw; assertion log `profit (6dp): 15185177`.
- `poc/test/JIT2.t.sol` — post-snapshot JIT: deposit at 30,734,429, distribute at 30,734,430; `profit (6dp): 3969852`.
- `evidence/jit_presnapshot.log`, `jit_postsnapshot.log`, `baseline.log` — full forge output.
- Verified sources: `RewardRedistributor.sol`, `EarnVault.sol`, `SUSDSCVault.sol`, `USDSC.sol`.

```bash
cd /workspaces/CA/stage3/work/S3-366/startale/poc
export SONEIUM_RPC=<soneium rpc>          # Blockscout/public endpoint
forge test -vv --match-test testPreSnapshot
forge test -vv --match-test testJIT
```

`setUp()` forks at block 30,734,426 and funds the attacker via `vm.store` on the USDSC balance slot; the operator calls are pranked as `0x86bE…333C`.

---

## 6. Economics and limits

| Variant | Capital | Profit/attack | Held for | Repeatability |
|---|---:|---:|---|---|
| Pre-snapshot | $2,000,000 | **$15.18** | snapshot + distribute (~1 block+) | needs to win the snapshot race |
| Post-snapshot JIT | $1,000,000 | **$3.97** | ~6 seconds | ~7.83/day, every epoch |

Per-epoch yield is small (avg 55.16 USDSC minted; 13.22 to EarnVault), so the capture is proportional: the edge is the TVL inflation ratio, not a large pool. At $1M and 7.83 epochs/day, the JIT variant yields roughly **$31/day ≈ 1.1% APR** before gas and competition — profitable but capital-heavy and competitive. A larger deposit scales the captured share only until it dominates the vault; the share formula is `X / (T_earn + X)`.

---

## 7. Risks and caveats

1. **Timing risk (primary).** Variant A requires landing the deposit before the operator's snapshot. If the operator bundles snapshot+distribute atomically, variant A collapses to variant B.
2. **Operator cadence can change.** 7.83/day is measured over 127.7 days; a slower cadence reduces annualized yield but not the per-epoch capture.
3. **Withdrawal liquidity.** EarnVault must have USDSC available to withdraw the principal; check `USDSC.balanceOf(EarnVault)` before depositing.
4. **Competition.** Any other depositor can dilute the capture; the attacker's share shrinks as TVL grows.
5. **MEDIUM confidence** because the profit depends on a live operator's timing and on capital that must be pre-positioned; the mechanism and the fork numbers are exact.
6. **Not a key compromise and not a bug in access control** — `distribute`/`snapshotVaultTVLs` are correctly OPERATOR-gated; the flaw is that the credited yield uses post-snapshot principal.

---

## 8. Provenance

- Found in Stage 3 batch **S3-366** (priority 2), target **S3-1415**, on 2026-11-14.
- Two fork PoCs in `stage3/work/S3-366/startale/poc`; result in `stage3/results/S3-366.json`.
- Headline status LIVE; new bugs recorded as HIGH confidence, extractability MEDIUM (capital/timing).
- Reclassified into the extractables ledger as **EX-16** with net **$15.18** per pre-snapshot attack.
