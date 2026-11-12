# EX-12 — Reserve Folio: `bid()` accepts an Auction from a different Folio

**Net for an unprivileged actor:** **~$36** (tracked basket value $48.98, minus ~$13 attacker rent)
**Confidence:** MEDIUM — `simulateTransaction` reaches `AuctionNotOngoing` with every account check passing, but no auction was open at the snapshot
**Gate:** none
**Chain:** Solana
**Status:** headline TOB-DTFSSOLANA-6 is PATCHED; this is a new cross-Folio auction-binding bug.

## Program

| Item | Value |
|---|---|
| Folio program | `DTF4yDGBkXJ25Ech1JVQpfwVb1vqYW4RJs5SuGNWdDev` |
| ProgramData | `53yQfYFEjAoQtADW2emAaLEZhinbUNq3TSS135ZjpSjP` |
| ELF | 1,366,152 bytes, sha256 `49331254…73aa` |
| Deployed | slot 372,263,076, 2025-10-09, repo HEAD `35248a6` |

## Bug

`bid()` validates the `Auction` account without binding it to the Folio whose basket is debited. `Auction::validate_auction` is used by `close_auction` but not by `bid`. An attacker can:

1. Create a Folio and advance its rebalance nonce to the victim's nonce.
2. Open an auction on the victim's sell/buy pair at an attacker-set near-zero price.
3. Call `bid()` with the victim's Folio, basket, token mint and ATAs plus the attacker's Auction account.

`auction_ends` is re-derived from `(victim, auction.nonce, sorted mints)` and passes; `rebalance.nonce` matches; the victim's tracked basket is debited at the attacker's price. The attacker receives the victim's basket tokens for ~1 raw unit of the buy token.

At the snapshot: 11 live Folios with a current-nonce `auction_ends` for a token still in the tracked basket; $48.98 tracked value; ~$13 attacker rent; net ~$36. Total tracked TVL across 45 Folios is $637.10.

**Note:** two Stage 3 targets (S3-2535 and S3-2540) point at the same program and the same bug. They are one economic finding; the master log counts both target rows ($36 each).

## Step-by-step

```
create attacker Folio; set rebalance nonce = victim nonce
open auction on victim's sell/buy pair at near-zero price
bid(victim folio, victim basket, victim token ATAs, attacker Auction)
// victim basket debited at attacker price; attacker receives basket tokens
```

## PoC

`stage3/work/S3-791/Reserve_DTF4yDGB/poc/sim_bid.py`

`simulateTransaction` (sigVerify=false) case A:

- Victim `5BP4N3NRwZn7tXQzrs6AdJY6NWRDrhizbdM7mqGizoWi` + foreign auction `DKGeM2yrVF1ejqqWzE6iz8JPkCaisKn2CF8SNHb6pLDh` owned by Folio `6d3sV2wLNpKmfju7J9AAgta7HEAsnWWaQgD4AfMPdWvG`.
- Result: `AuctionNotOngoing (6061)` at `bid.rs:199` — every account check passed.
- Control: same victim + its own auction gives the identical error; wrong sell mint gives `InvalidAuctionSellTokenMint (6063)` at `bid.rs:163`.

The only blocker at the snapshot is that no auction was open (`111 Auction accounts, 0 open`).

## Economics

- Tracked basket value $48.98; attacker rent ~$13; net ~$36.
- Total tracked TVL $637.10 across 45 Folios.
- Repeatable per Folio with a live auction; the snapshot had 11 reachable Folios.

## Evidence

- Program ELF sha256, slot/blockTime, repo HEAD `35248a6`.
- ELF strings contain `bid.rs`, `open_auction.rs`, `close_auction.rs`; no `dtf_program_signer`.
- `simulateTransaction` logs as above.
- 111 Auction accounts, 111 AuctionEnds, 45 Folios, TVL $637.10 (Jupiter v3, 2026-11-12).

## Risks / caveats

- No auction was open at the snapshot; the attacker must wait for or induce one.
- MEDIUM because the final debit was not executed end-to-end; the account checks pass and the only stop is `AuctionNotOngoing`.
- If the program binds `Auction` to the Folio in `bid()`, the path closes.

## Handover

1. Monitor `open_auction` for a live auction on a Folio with a tracked basket.
2. Re-run `sim_bid.py` with the live auction; confirm the basket debit and the attacker's token receipt.
3. Measure the victim basket value and the attacker rent; recompute net.
4. If the program is upgraded to bind the auction, close.
