# EX-11 — Prospective World: `reserve()` free-mints the remaining ProsNft supply

**Net for an unprivileged actor:** **~$48,000 estimated** (market-dependent; up to 119,878 NFTs)
**Confidence:** MEDIUM — the free-mint path is proven from the live TVM bytecode, but the resale value depends on demand
**Gate:** none (gas only)
**Chain:** Tron
**Status:** headline F-2024-6691 (`mintPros` parameter manipulation) is PATCHED; this is a new unauthenticated `reserve()` function.

## Contract

| Role | Address |
|---|---|
| ProsNft | `TBcY26uLcLBHWRm55KToXycUbFT3d46Zfw` |
| Public entry | `TFf1aBoNFqxN32V2NQdvNrXVyYCy9qY8p1` |

Runtime: 27,340 bytes; keccak256 `adc2ee88…14a652`; 46 dispatcher selectors.

## Bug

Selector `0x819b25ba` (`reserve(uint256)`) has no access control. Its body checks `paused`, a reentrancy guard, and `0 < n <= 6`, then `_mint(CALLER, counter[0x13+i])` and increments the counter. There is no owner, whitelist, per-user limit, or payment check. Anyone can mint up to 6 NFTs per call for gas only, repeatable.

Tier counters (30,046 / 54,031 / 78,019 / 102,013 / 126,013) point at unminted IDs; up to 119,878 NFTs (sum of remaining supply) can be claimed. The primary mint price is 2,300–4,800 PROS ($50–$105), so the free-mint value is the resale spread.

## Step-by-step

```
call reserve(6) repeatedly
// each call mints 6 NFTs to the caller for ~23.5 TRX gas (~$7.4)
// up to 119,878 NFTs
sell the NFTs at the primary/secondary price
```

## PoC

No local Tron fork. Evidence is the live TVM disassembly and ABI:

- `evidence/prosnft.asm/disassembled.asm` — selector `0x819b25ba` body.
- `evidence/decomp/decompiled.sol` — decompiled runtime.
- `evidence/tron_contract.json`, `tronscan_contract.json`, `getcontract.json`.
- `evidence/txlist_*.json` — live activity.

## Economics

- Gas: ~23.5 TRX (~$7.4) per 6-NFT call at $0.3153/TRX.
- Up to 119,878 NFTs; primary mint 2,300–4,800 PROS ($50–$105).
- The $48,000 estimate assumes a resale spread; actual value depends on demand/liquidity.
- MEDIUM because the NFT market may not absorb the supply.

## Risks / caveats

- The $48,000 is an estimate, not a realized sale; the NFT market may be thin.
- `paused` and the reentrancy guard must remain false/available.
- If the owner pauses `reserve()` or adds access control, the path closes.
- Tron energy/bandwidth costs and market depth matter.

## Handover

1. Re-read the ProsNft bytecode and confirm selector `0x819b25ba` still has no access control.
2. Simulate `reserve(6)` on Tron; confirm the mint and counter increment.
3. Measure the secondary market depth and realistic sale price.
4. If the market absorbs it, the free-mint is live; otherwise downgrade the USD estimate.
