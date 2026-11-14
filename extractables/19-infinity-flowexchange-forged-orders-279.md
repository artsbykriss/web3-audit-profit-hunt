# EX-19 — Infinity / FlowExchange: unvalidated `complication` steals approved NFTs

**Chain:** Ethereum mainnet (chain id 1)  
**Class:** unprivileged theft via forged order + attacker-controlled "complication" contract  
**Economic ID:** EX-19  
**Net:** **~$279** per stolen-NFT set (fork-proven, two live NFTs at 245,867 gas)  
**Confidence:** HIGH (fork replay of a real mainnet exploit + live theft)  
**Gate:** none (requires only that a victim approved the exchange for ERC-721 transfers)  
**Target:** S3-2029 · `0xf1000142679a6a57abd2859d18f8002216b0ac2b` (FlowExchange, verified, solc 0.8.14, deployed 2023-01-23, **unpaused**)  
**Pinned state:** fork block 26,411,154

> **Disclosure notice.** This is not a hypothetical: mainnet tx `0xc45d8f53565cea67bcc5957ddd0b4f77b5481b69b4313e6d28533696071ddd68` (block 26,147,566) already used this path to steal 6 NFTs. Treat this dossier as evidence for a private report to the protocol/Immunefi, not as operational guidance. The local PoC exists to prove reachability; do not broadcast it.

---

## 1. Summary

Code4rena 2022-06 Infinity H-05 required validating the order's `complication`. The v2 rewrite moved that validation **into** `IComplication(makerOrder.execParams[0])` — an address supplied by the untrusted order — and removed the exchange-side `_complications` / `_currencies` whitelist. A forged order therefore names the attacker's own contract as both `complication` and `currency`:

- `complication.canExecTakeOneOrder(...)` returns `true` (attacker code),
- `currency.transferFrom(...)` is a no-op (attacker code),
- `constraints[1] == constraints[2] == 0`, so `execPrice = 0`,
- the exchange still executes `IERC721.transferFrom(victim, attacker, tokenId)`.

The same bypass exists in `takeOrders()`.

The audited commit `765376f` predates the deployment and is not live (DIFFERENT_VERSION); the batch lead is **FlowExchange**, not the paused InfinityExchange `0xbADa…` — the pause on the sibling does not protect FlowExchange.

---

## 2. Live state

| Item | Value |
|---|---|
| FlowExchange | `0xf1000142679a6a57abd2859d18f8002216b0ac2b` (verified) |
| `paused()` | **false** |
| Owner | `0xB81819ef…` |
| ETH / WETH | 0 / 0.0035668 WETH |
| InfinityExchange sibling `0xbADa…` | paused (same bug closed there) |
| Victim criterion | any holder with `ApprovalForAll(FlowExchange, true)` |

Enumeration: all 18 collections the exchange ever traded plus BAYC/MAYC/Azuki/Pudgy/Doodles/CloneX/Moonbirds were checked for standing approvals. Every approving holder was drainable except two (ENS `0x22c3b13e…`, Metroverse `0x0d1f133c…`) — a lower bound, not a proof of exhaustiveness for collections never traded on the exchange.

---

## 3. Proof

`stage3/work/S3-445/infinity/`:

- `poc/` — Foundry suite.
  - `testHistoricalReplay` (PASS, 671,781 gas): replays the real 6-NFT theft pattern at the historical block.
  - `testLiveTheft` (PASS, 245,867 gas): at fork block 26,411,154 steals **jfrazier.eth** and **Metroverse #7922** from holders with live approvals.
- `evidence/exploit_tx.txt` — the real exploit transaction and its attacker helper `0xDF0Ca434d3a621F392a7E61b0A2A19fE32204608` (deployed block 26,147,290).
- `evidence/flow_source.txt`, `complication_source.txt`, `state.txt`, `poc_output.txt`.

Net at fork prices: ~$279 for the two live NFTs. The historical 6-NFT set was larger.

---

## 4. Economics

| Item | Value |
|---|---:|
| Gas per theft | ~245,867 (~$0.05 at 1 gwei, ETH $1,914) |
| Proceeds | NFT floor values at the pinned block; $279 for the two proven tokens |
| Capital | 0 (the forged order has `execPrice = 0`) |
| Gate | victim approval only |

The constraint on total value is the set of live approvals, not the attacker's capital. It is repeatable for every approving holder until the exchange is paused or the approvals are revoked.

---

## 5. Remediation and disclosure

1. **Immediate:** pause FlowExchange (the sibling `0xbADa…` is already paused) and revoke/announce `ApprovalForAll` for all users.
2. The exchange must re-introduce an exchange-side whitelist for `complication` and `currency` (or verify `msg.sender == order.maker` for the complication call), not trust `execParams[0]`.
3. Report privately (protocol security contact / Immunefi) with the tx hash and the fork trace; do not post the PoC.

---

## 6. Risks and caveats

1. **Victim set is bounded by approvals.** The measured $279 is the two tokens the fork proved; the ceiling is every ERC-721 approval to the exchange.
2. **Live exploit.** The bug is being used in the wild; this is a defensive finding.
3. **HIGH confidence**: real exploit transaction + two independent fork tests.

---

## 7. Provenance

- Stage 3 batch **S3-445**, target **S3-2029**, 2026-11-14.
- Result: `stage3/results/S3-445.json`; PoC/evidence: `stage3/work/S3-445/infinity/`.
- Ledger: **EX-19**, $279.
