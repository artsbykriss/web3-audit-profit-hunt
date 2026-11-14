# EX-21 — Phuture ManagedIndex: front-run a vToken deposit and mint PDI for free

**Chain:** Ethereum mainnet (chain id 1)  
**Class:** unprivileged front-run / accounting confusion (C4 2022-04 H-01 live variant)  
**Economic ID:** EX-21  
**Net:** **~$1,888.83 per 1 WETH victim deposit** (fork-proven; depends on a pending deposit)  
**Confidence:** MEDIUM (path is live, but value requires a victim deposit in flight)  
**Gate:** none (MEV timing)  
**Target:** S3-2405 · `0x632806bf5c8f062932dd121244c9fbe7becb8b48` (ManagedIndex "Phuture DeFi Index" PDI)  
**Pinned state:** fork block 26,411,604

---

## 1. Summary

`IndexLogic.mint(address)` (delegatecalled by the PDI index) computes what the caller owes from the **global** vToken balances:

```
amountInAsset = vToken.totalAssetSupply() - vToken.lastAssetBalance()
value         = convertToIndex(minAmountInBase) * totalSupply / convertToIndex(lastAssetBalanceInBase)
_mint(_recipient, value)
```

There is no per-caller accounting and no `sync()` first. Anyone can therefore front-run a pending `vToken.deposit()`: mint PDI against the victim's already-credited vToken balance, then burn/redeem the PDI to take the victim's deposit. The victim's follow-up `mint()` reverts.

This is the Code4rena 2022-04 H-01 pattern, still live in the deployed `IndexLogic 0xb7de911E…` (DIFFERENT_VERSION vs the audited commit, same accounting).

---

## 2. Live deployment

| Role | Address |
|---|---|
| ManagedIndex (PDI) | `0x632806bf5c8f062932dd121244c9fbe7becb8b48` (verified, 9,025 bytes) |
| IndexLogic (delegatecall target) | `0xb7de911EbC406055744253B06949e3642647e424` |
| Factory | `0xb4e85a5BFCd5f247D4BDa1491F57921473dDcE2e` (only one instance ever created, block 14,832,996) |
| vWETH (BeaconProxy) | `0x5b85fe0f0986d9341bF0AdbCFBd0D3CB0e56A993` → impl `0xf4B9d22f…` |
| Registry | `0x8f971223B4Bd9649702F10d306e469e6dbe3E3E9` |
| FeePool | `0x68ecC6BBA5f538cD7Ba6011b3A52513A282036Ab` |

State at the pin: `vWETH.totalAssetSupply() == lastAssetBalance() == 1,595,452,966,578,303,361` wei (1.595 WETH), so the current un-synced delta is zero; the attack needs the next pending deposit.

---

## 3. PoC

`stage3/work/S3-496/Phuture_Finance_contest_0x632806/poc/test/FrontRunMint.t.sol` (fork block 26,411,604):

- Simulates a 1 WETH victim `vWETH.deposit()`.
- Attacker calls `ManagedIndex.mint(attacker)`.
- Mints **33,840,184,439,774,824,749 PDI** (33,840.18 PDI) at zero cost.
- Attacker transfers PDI into the index and `burn()`s, receiving **993,010,000,138,637,233 wei = 0.99301 WETH (~$1,888.83)**.
- The victim's follow-up `mint()` reverts.

The 0.99301 WETH is the victim's deposit minus fees/slippage; the attacker's capital is zero (the front-run is atomic around the victim's transaction).

---

## 4. Economics

| Item | Value |
|---|---:|
| Victim deposit | 1 WETH (~$1,902 at the pin) |
| Attacker proceeds | 0.99301 WETH ≈ **$1,888.83** |
| Capital | 0 (front-run) |
| Gas | ~ a few hundred thousand gas (~$0.05) |
| Condition | a pending `vToken.deposit()`/`mint` in the mempool |

Value scales with the victim's deposit size, not with the protocol's $3,034.75 TVL. With no pending deposit there is nothing to capture — hence MEDIUM confidence.

---

## 5. Execution outline

1. Watch the mempool for `vWETH.deposit(...)` (or any index vToken deposit) from a non-index address.
2. In the same block, before it, call `ManagedIndex.mint(attacker)` — the victim's deposit is already reflected in `totalAssetSupply()` if their deposit landed first, or you mint after their deposit and before their `mint()` call.
3. Transfer the minted PDI to the index and `burn()` to redeem the underlying.
4. The victim's `mint()` reverts (insufficient remaining balance), so their deposit is lost.

The PoC file documents the exact call ordering.

---

## 6. Risks and caveats

1. **Requires a victim deposit.** No standing pending deposit at the pin; the $1,888.83 is per 1 WETH deposit, not a standing pool.
2. **MEV competition.** Other searchers can take the same front-run; the winner is the first in the block.
3. **MEDIUM confidence** for that reason; the code path and the fork result are exact.
4. **Protocol TVL is small** ($3.03k), so this is a perimeter finding, not a large drain.

---

## 7. Provenance

- Stage 3 batch **S3-496**, target **S3-2405**, 2026-11-14.
- Result: `stage3/results/S3-496.json`; PoC: `stage3/work/S3-496/Phuture_Finance_contest_0x632806/poc`.
- Ledger: **EX-21**, $1,888.83 per 1 WETH victim deposit.
