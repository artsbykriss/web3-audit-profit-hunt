# EX-14 — Doefin: expired orders remain matchable and settle on the raw difficulty target

**Net for an unprivileged actor:** **$6.78** (gross $6.91: +2.07 USDC + 2.66 USDT + 3,175 sat WBTC)
**Confidence:** HIGH — fork-proven at Arbitrum block 523,758,771
**Gate:** none
**Chain:** Arbitrum (42161)
**Status:** headline "Order Updates Does Not Take the Payout Calculation Into Account" is LIVE; this is the concrete profitable path.

## Contracts

| Role | Address |
|---|---|
| DoefinV1OrderBook | `0xff15526547d147e884a88659da44824410d0205a` |
| BlockHeaderOracle | `0x6a8e5EF57f551A9B5897250A36EEaCa934159589` |
| Maker | `0xcF2CeB89F5346B2FE75Fd1b5bd0E24c0d449ec7b` |

OrderBook holds 2.1 USDC + 5.68 USDT + 3,225 sat WBTC; orderIdCounter 24.

## Bug

1. **Expired orders stay matchable.** `OrderBookUtils.validateMatch` compares the order's millisecond `deadline` (e.g. 1,735,572,077,486 = Jan-2025) with `block.timestamp` in seconds (Nov-2026 ≈ 1.76e9). The comparison never trips, and `matchOrder` does not check expiry. Orders 12/13/14 remain `Pending`.
2. **Wrong strike.** `finalStrike` is set to `calculateDifficultyTarget()` — the raw nBits target (~2.44e53) instead of a difficulty (~1.1e14). `finalStrike >= initialStrike` always, so the Below maker always loses and the taker always wins.

The attacker matches orders 12/13/14, relays two real Bitcoin headers (880095/880096) to the permissionless oracle, and exercises the orders.

## Step-by-step

```
matchOrder(12,13,14)               // expired but matchable
submitNextBlock(880095, 880096)    // permissionless oracle
settleOrder(12,13,14)              // finalStrike = raw nBits target
exerciseOrder(...)                 // Below maker loses; taker wins
```

## PoC

`stage3/work/S3-306/doefin_0xff1552/poc/test/DoefinStaleOrder.t.sol`

Fork at Arbitrum block 523,758,771:

```
[PASS] gas 3,435,870
finalStrike 244083926948996765466279200227113710829717638069878784
initialStrike 108520000000000
attacker USDC 10,000,000 -> 12,070,000
attacker USDT 10,000,000 -> 12,660,000
attacker WBTC 1,000,000 -> 1,003,175 sat
```

## Economics

- Cost: 0.90 USDC + 1.30 USDT + 1,775 sat WBTC (~$1.22 at $68,616/BTC).
- Return: 2.97 USDC + 3.96 USDT + 4,950 sat WBTC (~$3.40).
- Gross +$6.91; net $6.78 after ~$0.13 Arbitrum gas (3,435,870 gas at 0.02 gwei, ETH $1,923.52).
- Orders 12/13/14 are the live fuel; order 15 is pending.

## Evidence

- Arbiscan verified OrderBook (solc 0.8.24, non-proxy, deployed 2024-12-17).
- `getOrder(12..15)` state: Pending, deadlines 1,735,572,077,486, payouts 2.97e6 / 3.96e6 / 4,950.
- Oracle `currentBlockHeight=880094`; headers 880095/880096 relayed in the PoC.
- `poc/test/DoefinStaleOrder.t.sol` PASS output above.

## Risks / caveats

- Only orders 12/13/14 are live fuel; after exercise the path is exhausted.
- The oracle must accept the two headers; it did on the fork.
- If the team patches the deadline comparison or the strike calculation, the path closes.

## Handover

1. Re-read orders 12/13/14 and the oracle height.
2. Re-run the PoC at the latest Arbitrum block.
3. If the orders are still Pending, the path is live; otherwise close.
