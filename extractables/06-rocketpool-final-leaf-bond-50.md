# EX-06 — Rocket Pool: unverified final-level leaves let a challenger defeat a proposal and claim the bond

**Net for an unprivileged actor:** **~$50 net** per defeated proposal (53.333 RPL gross ≈ $71.47 at $1.34/RPL, minus gas)
**Confidence:** LOW — the path is live and happened once (proposal 12), but it needs a future proposer-side malformed leaf; no proposal is currently pending
**Gate:** registered-node status; 10 RPL per-index challenge bond (refunded)
**Chain:** Ethereum (1)
**Status:** headline RPH-02 path traversal is PATCHED in live v3; this is the residual RPH-09 issue.

## Contract

| Role | Address |
|---|---|
| RocketDAOProtocolVerifier | `0xc4D85aA3e318c38005F6D73cC53E5A2b4223723a` |
| RPL token | `0xD33526068D116cE69F19A9ee46F0bd304F21A51f` |

Live `version() = 3`, `getDepthPerRound() = 5`, verifier balance 0.

## Bug

`submitRoot()` skips `verifyLeaves()` when `indexDepth + depthPerRound < treeDepth * 2`. Final-level network leaves can therefore be arbitrary hashes. A registered-node challenger can defeat a proposal whose pollard contains a malformed leaf hash (e.g. a non-`keccak(0)` hash for an empty leaf) and claim 2/3 of the 100 RPL proposal bond.

The headline RPH-02 arbitrary path traversal is closed by the witness-length check in live v3 (`Invalid proof length`). This is the remaining RPH-09 variant.

## Evidence of the live instance

- Proposal 12: `nodeCount = 4165`, `maxDepth = 13`, `defeatIndex = 8192`.
- Challenge tx `0x5978c28abb6aede1c11ae3c120de9efd4b423f27a433f64fe338dddae47c2ba7` calls `createChallenge(12, 8192, (0,0x00), [(0,0x00),(0,0x0128…),(0,0xf5c7…)])`.
- Claim tx `0xca508f7cb2800c9cd8a7a3eb6b090f15752ec03b60fb5a6ab0e40ed085593f5b` from `0xCCbFF44E0f0329527feB0167bC8744d7D5aEd3e9` pays `RPLTransferred(0xf357… -> 0xCCbF…, 53.333333333333333333 RPL)` and burns 13.333333333333333333 RPL.
- RPL ≈ $1.34 → gross $71.47; net ~$50 after gas.

## Step-by-step

```
wait for a proposal whose pollard has a malformed final-level leaf
createChallenge(proposalId, index, (0, 0x00), witnesses)
proposer cannot respond
defeatProposal() -> claimBondChallenger() -> 2/3 of 100 RPL
```

## PoC

`stage3/work/S3-185/sigmaprime_rocket_pool_rocket_0xc4D85a/poc/repro.md` — reproduction notes and the exact tx/calldata above. No Foundry test: the live instance already happened on-chain.

## Economics

- Gross 53.333 RPL ≈ $71.47; net ~$50 after gas.
- Challenge bond 10 RPL per index, refunded on success.
- Repeatability LOW: needs a proposer to submit a malformed final-level leaf; no Pending proposal now.
- Registered-node status is permissionless but requires the 10 RPL bond.

## Risks / caveats

- LOW confidence because the trigger is proposer-side; the path is not continuously available.
- The bond and gas must be fronted; the 10 RPL bond is refunded only on a successful defeat.
- If the verifier is upgraded to check final-level leaves, the path closes.
- The live verifier's `version() = 3` and the witness-length check confirm the headline is patched; this is a residual issue.

## Handover

1. Monitor `submitRoot`/`createChallenge` for proposals with malformed final-level leaves.
2. Replay proposal 12's calldata on a fork to confirm the bond payout.
3. Check the current proposal queue and the verifier version; confirm no pending proposal.
4. If a malformed leaf appears, the path is live; otherwise keep as LOW and monitor.
