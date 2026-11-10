# Extractable Value Master — external unprivileged actor

**Generated:** 2026-11-08
**Scope:** every finding from (A) the 906-incident DeFiHackLabs residual campaign and (B) the audit-driven Cyfrin / CodeHawks / researcher-GitHub campaign that has **positive value for an external actor**, plus the gated/latent cases that could become positive.
**Purpose:** a single hand-off file so another agent can evaluate, re-verify, and prioritise without re-reading the whole corpus.

**Read this first:** values are point-in-time and move. Every finding below names the chain, contract, block, evidence file and exact gate. Re-read the chain before acting. Nothing here is an instruction to attack a live protocol; it is a disclosure-ready evidence base.

---

## 0. Verdict and evidence standard

| Verdict | Meaning |
|---|---|
| **LIVE** | Fork-proven positive net for a fresh unprivileged EOA, with the exact calls and attacker delta. |
| **HOLDER-GATED** | The path is live but only a specific NFT/token holder can execute it. |
| **LOCKED / CONDITIONAL** | The value exists but a time lock, market state, or future event gates it. |
| **BELOW_THRESHOLD** | Positive net but < $10, or gas-dependent dust. |
| **GATED / LATENT** | The bug is live but a real gate (keeper, whitelist, supply, dead shares, economic spread) blocks a fresh EOA today. |
| **DRAINED** | The bug is live but the contract/pool has no material fuel. |
| **PATCHED** | The live code no longer contains the vulnerable path. |
| **NOT_DEPLOYED** | No live deployment found; the audited code is pre-launch/contest-only. |
| **UNPROVEN** | Deployment, code match, or reachability could not be established from public evidence. |

**LIVE bar:** exact contract/address, current real funds > $10, permissionless entry, no effective gate, fork-proven net profit > $10 after gas/flash costs, unchanged code.

**Net** means after gas and, where applicable, flash-loan/financing costs. Gross is the value moved before those costs. Do not add gross values across findings; they are not additive.

---

## 1. Master ranking — all net-positive findings

| # | Target | Chain | Bug / source | Who can take it | Gross | Net | Status | Confidence |
|---:|---|---|---|---|---:|---:|---|---|
| 1 | **StationX** | Linea | Pashov C-03 native-fee drain via local ERC721 buy | **fresh unprivileged EOA** | **$121.14** | **+$119.28** | **LIVE, confirmed twice** | High |
| 2 | **X7Finance X7Pioneer** | Ethereum | `claimRewards([])` re-counts ETH delta; NFT #300 only | holder of NFT #300 | $48.30 | **+$47.80** | HOLDER-GATED, live | High |
| 3 | **HeavensGate HATE** | Ethereum | Stale 2,197-epoch rebase backlog + 0.5% mint loop | **fresh unprivileged EOA** | $29.54 ceiling | **+$20.01** best tx | **LIVE** | High |
| 4 | **Gensyn Delphi DPM** | Gensyn 685689 | Terminal-marginal-price liquidation on FAILED/EXPIRED | fresh EOA **after** market fails/expires | $143.88 payout | **+$11.85** conditional | CONDITIONAL after 2027-01-02 | Medium |
| 5 | **INUKO Bond** | BSC | `LpToToken` balanceOf/reserves mismatch | fresh EOA **after** 10-year lock | $19.96 | +$8.55 | LOCKED 10 years | High |
| 6 | **OverNight USD+** | Avalanche | Permissionless `payout()` NAV rebase, capped premium | fresh unprivileged EOA | $7.49 | +$7.48 | BELOW_THRESHOLD, one-shot | High |
| 7 | **PegaBall** | Ethereum | `buyGamesFrom` pays vendor/referrer from proxy balance | fresh unprivileged EOA | $8.35 | +$5.92 | BELOW_THRESHOLD | High |
| 8 | **Renzo ezETH** | Ethereum | Secondary-market discount vs 14-day redemption | fresh EOA with capital | $24.66 spread | +$2.49 | ARBITRAGE, 14-day cooldown | Medium |
| 9 | **SinstakeZombie** | BSC | Unbacked dividend drip | fresh unprivileged EOA | $0.86 | +$0.81 | BELOW_THRESHOLD | High |
| 10 | **Dumbo** | BSC | Permissionless distributor epochs | fresh unprivileged EOA | $0.99 | +$0.79 | BELOW_THRESHOLD | High |
| 11 | **SCROLL** | Ethereum | Unchecked balance underflow | fresh unprivileged EOA | $0.59 | +$0.54 | BELOW_THRESHOLD | High |
| 12 | **DeezNutz DN404** | Ethereum | Self-transfer `rOwned` overwrite | fresh unprivileged EOA | $2.88 | −$0.17 at 0.0508 gwei; **+$0.53 at 0.0392 gwei** | GAS-DEPENDENT | High |
| 13 | **Limit Break V2** | Polygon | ERC-2771 forwarder offset bypass | fresh unprivileged EOA | $0.5207 | +$0.4686 | BELOW_THRESHOLD | High |

**Two findings are fresh-unprivileged, >$10, and currently executable: #1 StationX (+$119.28) and #3 HeavensGate (+$20.01).** #2 X7Finance is larger (+$47.80) but requires NFT #300. Everything from #4 down is conditional, locked, or below the $10 bar. IdolsNFT is no longer positive — its reward pot is now 999,999 wei; see §5.

---

## 2. Detailed dossiers

### 2.1 StationX — LIVE, +$119.28 (Linea)

**Source:** Pashov audit `researchers/pashov-audits/team/md/StationX-security-review.md`, 2024-07-19, finding **C-03 "Native tokens can be drained from the Factory contract"** (3 critical / 12 high). Review commit `de6dbb69fd6ec51570899d6e110030d0d5ac602f`. No fix status stated.

**Live contracts (Linea, chain 59144):**

| Role | Address |
|---|---|
| Factory proxy | `0x17f251afb0f1b47d47d50f2a5f2dcb72b12c06bc` |
| Factory impl | `0xd11f5a51a366fa2742dd77e05fcac5ed262ae7b3` |
| BuyDaoToken proxy | `0x9be2a2750b0bdfb9ff6bbb8a45e093f73e27e364` |
| BuyDaoToken impl | `0xf74e742f245a32d50c9d8351aa9d16039a9b26e9` |
| Platform fee address | `0x1A17beA23DFa5D9CF5B0d0838C826Ad88537c6fb` |

**Bug:** `BuyDaoToken._buyGovernanceTokenERC721DAO` pays the native deposit and owner share out of the BuyDaoToken's own balance without checking that `msg.value` covers those amounts. The audited `crossChainBuy` trigger is now LZ-gated (`Only Factory`), but the same payout is reachable through the public local `buyGovernanceTokenERC721DAO` on an attacker-created ERC721 DAO with a native deposit token.

**Call sequence (fresh EOA, no role):**

1. `createERC721DAO(...)` with:
   - `_depositTokenAddress[0] = 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE`
   - `_pricePerToken = 55240000000000000` (0.05524 ETH)
   - `_maxTokensPerUser = 1`, `_distributionAmount = 1`, `_ownerFeePerDepositPercent = 0`
   - `_depositChainIds = [183]`, `_commLayerId = 183`
   - `msg.value = 0.00095 ETH` (the `createFees()` value; the live function does not enforce it)
2. `buyGovernanceTokenERC721DAO(DAO, "x", 1, [])` with `msg.value = 0`.
3. The BuyDaoToken pays `0.05424 ETH` to the attacker-controlled Safe and `0.001 ETH` to the platform fee address, leaving its own balance at 0.

**Economics (independently reproduced):** gross `0.05424 ETH` = **$121.14**; gas `0.00083416176 ETH` at 0.48 gwei; net `0.05340583824 ETH` = **$119.28** at $2,233.491126/ETH. The original run measured $118.13; the difference is the unenforced create fee and gas. **One-shot:** the BuyDaoToken balance goes to zero and a second buy reverts `Fee Transfer failed`.

**Current state (last checked block 32,546,700):** BuyDaoToken native balance **0.05524 ETH**; Factory native balance **0.201476 ETH**; both EIP-1967 implementations unchanged. The Factory's own 0.201 ETH is **not** reachable by this path.

**Evidence:**
- `research/audits/hunt/HUNT-019.md` (original)
- `research/audits/hunt/HUNT-019-VERIFY.md` (independent confirmation, block 32,546,005, fresh EOA/DAO/Safe)
- `research/audits/hunt/HUNT-019.json`, `HUNT-019-VERIFY.json`
- Audit report and C-03 text: `research/audits/researchers/pashov-audits/team/md/StationX-security-review.md`

**What would change the verdict:** a BuyDaoToken/Factory upgrade that adds a `msg.value` check or removes the local ERC721 buy; a pause on `createERC721DAO`/`buyGovernanceTokenERC721DAO`; the BuyDaoToken balance being swept. The Factory's 0.201 ETH would become reachable only through a different bug.

---

### 2.2 X7Finance X7Pioneer — HOLDER-GATED, +$47.80 (Ethereum)

**Source:** incident `20261008-X7Finance_X7Pioneer_s_claimRewards_adds_-0013`, tx `0xc98056d6…21766d` (block 26,146,922); report `research/leads/h2-x7finance.md`, PoC `research/data/h2-x7finance/poc/test/X7Dust.t.sol` (7/7 pass).

**Contract:** X7Pioneer / reward pool `0x70000299Ee8910cCaCD97B1bB560E34F49c9e4f7` (also the NFT contract).

**Bug:** `totalRewards += balance − lastETHBalance` runs on every call, while `lastETHBalance` is only refreshed inside `if (claimable > 0)`. After the attack's ~639 empty `claimRewards([])` calls, `totalRewards` is 21,580.116842936802664294 ETH of accounting fiction and per-NFT is 33.771700849666357847 ETH. Only NFT #300 has `rewardsClaimed == per-NFT`; every other token's claimable exceeds the pool and underflows.

**Gate:** only the holder of **X7Pioneer NFT #300** can claim. At the last check, `ownerOf(300) = 0xC79352119A7cF6EFbFaBBD7e6b013B79687BaCf2` — the 2026-10-08 attacker EOA, 0 code. `totalSupply = 639`; `rewardsClaimed(300) = 33.771700849666357847 ETH`; `transferUnlocked(300) = true`, so the NFT is transferable.

**Economics:** pool holds `0.021581365277773518 ETH` ($48.30). The break-even donation is `totalSupply × balance = 13.790492412497277941 ETH`; the donation is fully refunded by the claim. With a zero-fee Balancer V2 flash loan, **gross $48.30, net +$47.80** (gas ~3.54M). A 5 ETH donation nets $17.52; 2.855 ETH nets $10.

**Current state (block 26,367,607):** pool native balance **0.021581365277773518 ETH**; `ownerOf(300)` still `0xC793…`; `totalSupply` 639; `rewardsClaimed(300)` unchanged. The pool is still funded and the gate is unchanged.

**Evidence:** `research/leads/h2-x7finance.md`, `research/data/h2-x7finance/`, `research/audits/hunt/` not applicable (this is from the previous campaign).

**What would change the verdict:** NFT #300 being transferred to a new holder (the new holder can claim); any ETH inflow to the pool (100% stealable by #300's holder); a change to `rewardsClaimed`/`totalSupply`.

---

### 2.3 HeavensGate HATE — LIVE, +$20.01 (Ethereum)

**Source:** incident `20230905-HeavensGate_Rebasing_logic_issue-0592`; reports `research/leads/handover-heavensgate-max.md`, `handover-heavensgate.md`.

**Contracts (Ethereum):**

| Role | Address |
|---|---|
| HATE token | `0x7b768470590B8A0d28fC714d0A70754d556D14eD` |
| sHATE | `0xf829d7014Db17D6DCe448bE958c7e4983cdb1F77` |
| HATEStaking | `0x8EBd6c7D2B79CA4Dc5FBdEc239a8Bb0F214212b8` |
| HATE/WETH pair | `0x738dab4AF8D21b7aafb73545D79D3B4831eE79dA` |
| StakingDistributor | `0xceF0019C3679Be632a6D1eA1854f2b5313F4FB81` |
| HateTreasury | `0x710154A8503428D53710A620B8A1C970BeDdB8CA` |
| Uniswap V2 router | `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D` |

**Bug:** `HATEStaking.rebase()` is permissionless and fires while `epoch.end <= block.timestamp`. The last real epoch ended 1,730,772,023 (2024-11-05), leaving ~2,197 backlogged epochs (28,800 s each). Every `stake()`, `unstake(..., true)` and direct `rebase()` consumes one epoch and `distributor.distribute()` mints **0.5% of HATE total supply** to the staking contract. A flash-swap + 200 stake/unstake loops redeems more HATE than staked and sells it into the only HATE/WETH pair.

**Economics (measured):**

| Sequence | Block | Gross | Net |
|---|---:|---:|---:|
| 1 tx × 200 loops | 26,361,721 | 0.011345833007962675 WETH = $25.47 | **+$20.01** |
| 4 txs × 200 loops (full drain) | 26,361,740 | 0.013156182028208334 WETH = $29.54 | +$2.52 (later cycles are gas-negative) |

Gas at the measured base fee; a 240-loop tx reverts `UniswapV2: K`. The pair's WETH is the hard ceiling.

**Current state (block 26,367,607):** pair WETH **0.013160802174490065** — unchanged from the fork block. The backlog and distributor mint are still present. The net at current gas may differ; re-measure before acting.

**Evidence:** `research/leads/handover-heavensgate-max.md`, `handover-heavensgate.md`; PoC under `research/data/heavensgate-max/`.

**What would change the verdict:** the pair being drained/reseeded; the team calling `rebase()` up to date or disabling the distributor mint; a gas spike above the break-even.

---

### 2.4 Gensyn Delphi DPM — CONDITIONAL, +$11.85 (Gensyn 685689)

**Source:** `research/leads/immunefi-disclosures.md`; Trail of Bits LMSR High sibling.

**Contracts:** DPM gateway `0x982a67aE92D8de361957249fB2BB4a62BCc6A8d5`; factory `0x9C73417f79a1361c6aF9Bd828343badEE1b84936`; collateral USDC.e `0x5b32c997211621d55a89Cc5abAF1cC21F3A6ddF5`; best market `0x3df2a20a0d889c3bba71e996d84fd835b77cdf71`.

**Bug:** FAILED/EXPIRED liquidation values every share at the **final marginal price** (`k * q * (S+q) / sqrt(newSumTerm36)`), which can exceed the integrated average price paid on entry. The spread comes from the market's existing value; most of the payout is the attacker's own capital returned.

**Gate:** the market is currently `OPEN`; `liquidate` reverts `MarketNotLiquidatable(OPEN)`. Trading deadline 2026-12-31 23:59 UTC; settlement deadline 2027-01-02 23:59 UTC. The payout requires a future FAILED/EXPIRED state that an outsider cannot currently invoke.

**Economics:** best market held 63.989836 USDC.e at block 17,631,137; conditional payout 143.875679 USDC; conservative net **+$11.85** after share acquisition/fees, 5% financing to expiry, L1/L2 gas, LayerZero fee and 0.5% bridge slippage. Current gross **$0**.

**Evidence:** `research/leads/immunefi-disclosures.md`.

**What would change the verdict:** the market reaching FAILED/EXPIRED after 2027-01-02 without other state changes; a fresh market with the same pattern and an earlier terminal date.

---

### 2.5 INUKO Bond — LOCKED, +$8.55 (BSC)

**Source:** incident `20221014-INUKO_FlashLoan_price_manipulation-0771`; report `research/leads/h2-inuko.md`.

**Contracts:** Bond `0x09beDDae85a9b5Ada57a5bd7979bb7b3dd08B538`; INUKO/USDT pair `0xD50B9Bcd8B7D4B791EA301DBCC8318EE854d8B67`; INUKO `0xEa51801b8F5B88543DdaD3D1727400c15b209D8f`; LP vault `0x62d55e1D648Dc1076b5E273018122607d9666BEa`.

**Bug:** `LpToToken()` prices the LP using `otherToken.balanceOf(pair)`, which a plain USDT transfer inflates without touching `getReserves()`; `LpToSig()` converts at the real reserves. Donate USDT, call `buyBond`, recover the donation with `pair.skim()`, and the bond records a claim far above the LP value. `claim()` pays the recorded INUKO after the lock.

**Gate:** `bondList(0).lockingPeriod = 315,360,000` seconds (**10 years**); `claim()` at +3 days pays 0. The bond holds **4,241.976 INUKO** (~$19.96) against 243,816.19 INUKO of matured claims (57.5× insolvent).

**Economics:** even with a zero lock, gross 4,240 INUKO + 198 leftover sold = 19.55 USDT; LP cost 9.40; gas ~$0.23 → **net +$8.55**, below the $10 bar. At latest (BSC block 132,324,584) the bond still holds 4,241.976 INUKO.

**Evidence:** `research/leads/h2-inuko.md`.

**What would change the verdict:** the owner shortening `bondList[0].lockingPeriod`; a re-deposit into the bond; a new active bond with a short lock.

---

### 2.6 OverNight USD+ — BELOW_THRESHOLD, +$7.48 (Avalanche)

**Source:** incident `20221202-_OverNight_FlashLoan_Attack-0742`; report `research/leads/h2-overnight-flashloan.md`.

**Contracts:** USD+ `0xe80772Eaf6e2E18B651F160Bc9158b2A5caFCA65`; Exchange `0x73cb180bf0521828d8849bc8CF2B920918e23032`; portfolio manager `0xFDf56CF6d743a92D9196806b9028Ac3dBCE61f87`; StrategyAave `0xA2007Ae3…8893`; Benqi Comptroller `0x486Af39519B4Dc9a7fCcd318217352830E8AD9b4`.

**Bug/state:** the historical flash-loan/NAV path is dead: `Exchange.redeem()` is 1:1 with a 0.04% fee, the strategies no longer hold nUSDLP, and Benqi `borrowGuardianPaused(qiUSDC) = true`. The only live value path is permissionless `Exchange.payout()`: buy USD+ at 1:1, call `payout()`, redeem at the rebased NAV. The premium is capped by the pre-existing **$11.319179** NAV surplus.

**Economics:** `totalNetAssets() = 845.141280 USDC`, `USD+ totalSupply = 833.822101`, NAV $1.013575. A $4,000 ticket measured +$7.486489 (3,998.400000 → 4,009.090125 USD+ → 4,007.486489 USDC). **Gross $7.49 / net ~$7.48 before gas — below $10.** Larger tickets are worse; $50k is −$9.20.

**Evidence:** `research/leads/h2-overnight-flashloan.md`; PoC `research/data/h2-overnight-flashloan/poc`.

**What would change the verdict:** `totalNetAssets` growing far beyond USD+ supply (a fresh NAV premium >$10 after fees); Benqi unpausing and a non-Aave strategy holding pool/LP exposure again.

---

### 2.7 PegaBall — BELOW_THRESHOLD, +$5.92 (Ethereum)

**Source:** incident `20250603-PegaBall_Business_Logic_Flaw-0244`; report `research/leads/gap-GAP-043-pegaball-business-logic.md`.

**Contracts:** proxy `0xb8fcabf7bd88a2489fafbafa5f9a05a0e068cb5e`; implementation `0x29003dd6b9970ad658314fffb61e42f352c41630`.

**Bug:** `buyGamesFrom(_amount)` computes `price = gamePrice * _amount`, sends `price` from the proxy to itself, then `_distributeBuyTax` pays vendorCut (1%) and referrerCut (1%) to the vendor/referrer. The caller's `msg.value` is never required; `hasETHBalance` checks only the caller's wallet balance. Vendor registration is open; buying is not locked; whitelist is off.

**Economics:** proxy held 0.0045088 ETH; 112 `buyGamesFrom(1)` calls drain 0.003744 ETH = **$8.3541 gross**, gas 24,453,635 at 44,653,646 wei = $2.4365 → **net $5.9176**. The last purchase must leave 764.8e12 wei; the cap is exact.

**Current state (block 26,367,607):** proxy still holds 0.0045088 ETH. The path is live but below the $10 bar.

**Evidence:** `research/leads/gap-GAP-043-pegaball-business-logic.md`; JSON `research/data/coverage-gaps/GAP-043.json`.

**What would change the verdict:** the proxy being re-funded above ~0.006 ETH; a change to `gamePrice`/tax.

---

### 2.8 Renzo ezETH — ARBITRAGE, +$2.49 (Ethereum)

**Source:** `research/leads/lst-redemption-arb.md`.

**Contracts:** ezETH `0xbf5495Efe5DB9ce00f80364C8B423567e58d2110`; WithdrawQueue `0x5efc9D10E42FB517456f4ac41EB5e2eBe42C8918`; impl `0xF821A5Cff2cDd014C6e6BbB8E05B81c3D7e98003`; RestakeManager `0x74a09653A083691711cF8215a6ab074BB4e99ef5`.

**Path:** buy discounted ezETH on the open market, request redemption, wait the live 14-day cooldown, claim ETH. This is not a protocol bug; it is a secondary-market discount vs funded redemption.

**Economics (block 26,354,213):** 5 ETH bought 4.602561105490465359 ezETH; claim 5.011116508796105932 ETH; gross spread **$24.66**; net **+$2.49** after 14-day 5% APR financing ($21.27) and gas ($0.89). A 10 ETH cycle was **−$0.14**; break-even financing is 5.586% APR. WithdrawQueue buffer was 37,232 ETH ($82.6M), a liquidity ceiling, not extractable profit.

**Evidence:** `research/leads/lst-redemption-arb.md`.

**What would change the verdict:** the ezETH discount widening or the financing rate falling; the cooldown/buffer changing. Re-quote before relying on it; it does not scale.

---

### 2.9 Dust positives — below $10

| Target | Chain | Address | Bug | Gross | Net | Evidence |
|---|---|---|---:|---:|---:|---|
| **SinstakeZombie** | BSC | victim `0x7314729d691fd074dbba03ca3c6ef3be61b31d34`; ZOMBIE `0xE2A6428fD332287B0470965E16350D3cc1736E3E` | Unbacked dividend drip; victim holds 2,089 ZOMBIE | $0.86 | +$0.81 | `gap-GAP-028-sinstakezombie.md` |
| **Dumbo** | BSC | distributor `0x495670e5a43ce393597952b2fe944036e6785baf` | Permissionless 190-epoch distributor; victim empty; $469 upper is the DUM/BUSD pair | $0.99 | +$0.79 | `gap-GAP-031-dumbo-business-logic.md` |
| **SCROLL** | Ethereum | token `0xe51D3dE9b81916D383eF97855C271250852eC7B7`; pair `0xa718aa1b3f61C2b90A01aB244597816a7eE69fD2` | Unchecked balance underflow; dump into the only WETH pair | $0.59 | +$0.54 | `handover-scroll-underflow.md` |
| **DeezNutz** | Ethereum | DN `0xb57E874082417b66877429481473CF9FCd8e0b8a`; pair `0x1fB4904b26DE8C043959201A63b4b23C414251E2` | Self-transfer `rOwned` overwrite; 192 cycles | $2.88 | −$0.17 at 0.0508 gwei; +$0.53 at 0.0392 gwei | `handover-deeznutz-max.md` |
| **Limit Break V2** | Polygon | V2 `0x9A1D00bEd7CD04BCDA516d721A596eb22Aac6834` | ERC-2771 forwarder offset bypass; best target `0x20D4DF177d227cC3d59006673aA892ad922133c7` | $0.520684 | +$0.468581 | `limitbreak-census.md` |

All five are live or live-with-fuel-gone; none reaches the $10 bar. They matter only if fuel is added or gas collapses.

---

## 3. Gated / latent value — not currently extractable

These have real value behind a gate. Another agent should monitor the gate, not re-audit the bug.

| Target | Chain | Value | Gate / why not extractable now | Evidence |
|---|---|---:|---|---|
| **V4 Router (z0r0z)** | Ethereum + 5 chains | $0 today; live critical | The audited Critical payer-check bypass is **live** on `0x00000000000044a361Ae3cAc094c9D1b14Eece97`, but the only real-token allowance with balance is 5 USDT, and USDT settlement reverts on the non-standard ERC20 return. DRAINED. | `HUNT-069.md` |
| **Morpho Blue** | Ethereum | $33.21 to an existing supplier; fresh EOA $0 | Bad-debt socialization bug live (`Morpho.sol:392`), but the only dust market (`0x0ff9c1…d789`) has zero liquidity and two 1-wei positions; the 85.09% supplier can shift $33.21 by withdrawing before socialization. | `HUNT-072.md` |
| **Ostium** | Arbitrum | 9,169.62 USDC legacy discounts | 963 legacy `LockedDepositNft` holders; new discount-deposit creation removed. Only legacy holders can act. | `HUNT-033.md` |
| **Radiant dLP** | Base | $15,539 AUM; bug live | Initial-donation bug live on `0x8A76639FE8e390Ed16eA88f87BEB46d6A5328254`, but supply is 5.3M shares; zeroing a $10 deposit would need ~$53M of donation. | `HUNT-029.md` |
| **Gamma GMX vaults** | Arbitrum | $115 at risk ($124 total) | `run`/`runNextAction`/`cancelFlow` are keeper-only (`NotAKeeper`); the funded vault is in an open 1x position. | `HUNT-008.md` |
| **Exactly Protocol** | Optimism / Ethereum / Base | $2.80M OP / $0.15M ETH / $12.1M Base TVL | Rounding/donation bug live, but every live market is seeded with 5 USD of dead shares; smallest supply 974,959 wei; `enableMarket` is admin-only. A new market seeded without dead shares reopens it. | `HUNT-067.md` |
| **Omo** | Base | $3.36 max | H-02 `transferFrom` live, but the sole holder has zero router allowance; H-01 reverts `NotWhitelisted`; two vaults hold 4,448 sats cbBTC. | `HUNT-014.md` |
| **ArkProject NFT Bridge** | Ethereum | 888 EveraiDuo (~$11,464) | Genuine Starknet L2→L1 message consumption + whitelist; all five validated highs are DoS/design, not drains. | `HUNT-010.md` |
| **TesseraSwap** | Base | $818,972 treasury | Callback repays at the engine quote, not the amount received; engine bid must exceed best ask + ~5 bp. 251/251 samples were negative. | `h2-tesseraswap.md` |
| **SKY** | BSC | $122,280 pair | Token acquisition blocked; 35% sell tax; V2 buys revert `Transaction Closed`; net −$3,482. | `sky-final.md` |
| **PMMSKYDAO** | BSC | $0.37 | Pool emptied during research; `releaseToken` key-gated. | `pmmskydao-final.md` |
| **GoldPesa GPX hook** | Base | $71,258 | Rebalance price gate closed; opening costs $123,168.72 > the LP. | `goldpesa-verify.md` |
| **Likwid C4–C6** | BSC | $31.08 / $20.29 / $11.07 gross | 16.777215× `minBorrowLevel`; net negative at all sizes. | `likwid-extract.md` |
| **BTCPay Server ≤2.4.1** | Bitcoin/Litecoin | Unquantified | Vendor-confirmed actively exploited; no server probed; no public balance. | `btcpay-deep.md` |

---

## 4. Gross-positive but net-negative — do not re-chase

These were measured; the attacker loses money. Kept here so another agent does not re-open them as "gross extractable".

| Target | Gross | Net | Why |
|---|---:|---:|---|
| Balancer rounding | $2,418.53 ceiling | $0 | Pools emptied; net zero at best. |
| Vault4626 | $1,782,594 with $1.78M capital | −$1,443.02 | Requires holding the capital; redeem pays USDC-first. |
| WGPT | $94.17 ordinary pair proceeds | −$5.79 | Incremental exploit $0; `burnToken=false`. |
| WUSD.fi GLO sybil | $197.20/address | −$881.23 | 2 GLO per address, $1,000 fee, locked. |
| NovaBox | $196.06 | −$4,674 | Break-even deposit 260.56 ETH; pot 0.0877 ETH. |
| BeatXswap | $0.0034 | −$7,500 | Mandatory 75% treasury cut. |
| Onyx precision loss | $3.18 | $0 | All markets CF=0; liquidity borrowed out. |
| LPC | $0.0011 | −$0.02 | Pair dust. |
| JUDAO | $0.45 | −$0.02 | Pair nearly empty. |
| DeFiPlaza | $0.0033 | −$0.12 | Pool dust. |
| DogeAlliance | $0.00008 | −$7 | Pools empty. |
| RnsPay | $0.000088 | −$2.53 | Approvals revoked. |
| WiseLending | $0.019 | −$1.11 | $38.91 mooConvex not borrowable. |

---

## 5. Stale / changed since the report

| Target | Original | Current | Action |
|---|---|---|---|
| **IdolsNFT** | +$5.28 net at block 26,362,008 | `allocatedStethRewards()` = **999,999 wei** at block 26,367,607 (~$0.000002); the 2,705 stETH principal remains unreachable | **Remove from the positive list.** Re-open only if the pot is topped up by >$10. |
| **Papertrade** | +$505.55/cycle at the 2026-11-06 snapshot | As of 2026-11-07 the live book is 20–40× deeper; break-even notional $68M–$81M > caps; unprofitable at any capital within caps | Current value **$0**; treat as a historical snapshot, not a live finding. |
| **PMMSKYDAO** | Conditional +$53,453.59 | Pool emptied to $0.37; `releaseToken` key-gated | Dead; remove. |
| **SKY** | ≤$8,776 gross | Pair still $122,280, but net −$3,482 | Negative; do not count as extractable. |
| **HeavensGate / StationX / SCROLL / DeezNutz / X7 / PegaBall / SinstakeZombie / Dumbo** | — | Re-checked at blocks 26,367,607 (ETH), 32,546,700 (Linea), 132,324,584 (BSC) — balances unchanged | Still current; re-check before acting. |

---

## 6. Excluded — patched / not deployed / no value

The audit campaign deep-hunted 73 protocols. **39 PATCHED, 17 NOT_DEPLOYED, 9 GATED, 5 UNPROVEN, 2 DRAINED, 1 LIVE.** Full table: `research/audits/hunt/SUMMARY.md`, `MASTER.csv`.

**Patched (do not re-open without a code change):** Beanstalk Finale, Beanstalk BIP-39, Tadle, Steadefi, DittoETH, Biconomy Nexus, GainsNetwork, Lucidly, Bunni, KittenSwap, Blueberry, OLY, TapiocaDAO, Peapods, RipIt, Burve, Nexus, SharwaFinance, Astrolab, Reya, Hyperstable, BOB-Staking, Roots, Accountable, Stake.Link, DeXe, Beefy CL, FWX, Vega, Code Sekai, Syndicate, Raga, Zoniqx, BIT5, MemeSwap, IAm0x52/Hyperstable, devNamedKiki/USSD, PollenDAO, TrueFi.

**Not deployed (pre-launch/contest-only):** RAAC, Zaros, QuantAMM, Beedle, Saffron, Hyperhyper, Karak native vault, Licredity, Paladin Valkyrie, Casimir, STBL ESS, Castr.fun, Pluto, Xtatuz, iBax, Regnum Aurum, Elytra.

**Gated / no fresh-EOA profit:** Gamma GMX vaults, ArkProject, Sudoswap v2, Wells/Basin, Radiant, Ostium, Guessmeme, Exactly, Morpho Blue.

**Unproven (no public deployment or code match):** Polygun, Coinflip, Remora, EARN'M, Goldilocks.

**Drained:** Omo ($3.36 max), V4 Router (live critical, no settleable victim).

The 906-incident campaign's 449 BLOCKED and 24 PATCHED rows were not re-opened; the only survivors from that corpus are the ones in §1–§2.

---

## 7. Re-verification checklist for the next agent

### Priority order

1. **StationX (Linea)** — the only fresh-unprivileged >$10 finding. Re-check at latest:
   - `BuyDaoToken.balanceOf` native = 0.05524 ETH?
   - EIP-1967 impls unchanged?
   - `createERC721DAO` + `buyGovernanceTokenERC721DAO` from a fresh EOA, `msg.value = 0`.
   - Confirm one-shot and net > $10 at current gas.
2. **HeavensGate (Ethereum)** — re-check pair WETH (0.013160802), rebase backlog, distributor mint; re-measure the 200-loop net at current gas.
3. **X7Finance (Ethereum)** — re-check `ownerOf(300)` and pool balance; if #300 has moved, the new holder can claim.
4. **Gensyn (Gensyn 685689)** — check the best market's status; if FAILED/EXPIRED after 2027-01-02, execute the conditional path.
5. **INUKO (BSC)** — check `bondList(0).lockingPeriod`; if shortened, re-run the donation/skim path.
6. **Below-threshold live bugs** — OverNight, PegaBall, SinstakeZombie, Dumbo, SCROLL, DeezNutz, Limit Break. Only if fuel increases or gas collapses.
7. **Gated/latent** — monitor the exact gate in §3; do not re-audit the bug.

### RPCs

- Ethereum: `https://ethereum-rpc.publicnode.com` (fallback `https://eth.drpc.org`)
- Linea: `https://rpc.linea.build`
- BSC: `https://bsc-dataseed.binance.org` (fallback `https://bsc-rpc.publicnode.com`)
- Avalanche: `https://api.avax.network/ext/bc/C/rpc`
- Gensyn: public RPC used in `immunefi-disclosures.md` (chain 685689)
- Arbitrum: `https://arb1.arbitrum.io/rpc`
- Base: `https://mainnet.base.org`

### Tools

- Foundry: `/workspaces/CA/research/tools/foundry/{forge,cast,anvil}`
- Chain toolkit: `python3 /workspaces/CA2/residual/tools/chain.py <cmd> <chain> <address> [block]`
- DefiLlama prices: `https://coins.llama.fi/prices/current/<chain>:<address>` / `historical/<ts>/<chain>:<address>`

### Evidence paths

- Audit corpus: `research/audits/`
- Hunt results: `research/audits/hunt/HUNT-*.md` and `.json`
- Master hunt table: `research/audits/hunt/SUMMARY.md`, `MASTER.csv`
- StationX verification: `research/audits/hunt/HUNT-019-VERIFY.md`
- Previous-campaign leads: `research/leads/`
- Previous-campaign PoCs/data: `research/data/`

---

## 8. Caveats

- **Point-in-time.** All balances and nets are pinned to the named block; the chain moves. Re-read before acting.
- **Net definitions differ by finding.** StationX includes create gas and the unenforced create fee; HeavensGate includes the measured gas at its block; Renzo includes 14-day financing; DeezNutz is gas-dependent. Do not compare nets without reading the dossier.
- **Single-agent vs confirmed.** StationX is independently confirmed twice. HeavensGate, X7, INUKO, OverNight, PegaBall, Renzo, SinstakeZombie, Dumbo, SCROLL, DeezNutz and Limit Break were each produced by one specialist agent (some with prior campaign verification); treat them as high-confidence but re-check before relying on them.
- **Gross ≠ net.** The gross-positive/net-negative table exists because several reports headline gross numbers that lose money after costs. Do not promote them.
- **Corpus coverage.** CodeHawks private/invite-only contests, redacted Cyfrin audits, private GitHub repos, and Code4rena/Sherlock/Cantina were sampled, not exhaustively indexed. "Nothing missed" is bounded by what is public.
- **No transactions.** Every result is read-only (public RPC + local Foundry/Anvil forks). No key, no `.env`, no broadcast.
