# Stage 3 QA checklist

For each sampled target:

**Deployment identity (Step 0) — check first**

- [ ] `derived_addresses` is present and non-empty.
- [ ] The audited address was independently re-derived: a source URL ties it to the project **and** a
      live code check was recorded (`eth_getCode` / chain-native existence).
- [ ] Version match is stated: `EXACT_MATCH`, `MATCH_EXCEPT_IMMUTABLES`, `DIFFERENT_VERSION`, or
      `UNVERIFIED_SOURCE` with a reason. `DIFFERENT_VERSION` without a search for the matching
      instance is a reject.
- [ ] Sibling/instance coverage: if the protocol is a factory, registry, or multi-vault deployment,
      the instance count is recorded and at least the highest-value instance was checked. A negative
      on a single instance of a multi-instance protocol is a reject.
- [ ] Proxy/implementation pairs are both recorded, and the address holding value was the one audited.
- [ ] Other claimed chains were checked or explicitly ruled out.
- [ ] If the derivation contradicted the batch address, the discrepancy is explained in `notes` and
      the audit targets the derived address.

**Verdict**

- [ ] `verdict` is `EXTRACTABLE` or `NOT_EXTRACTABLE`; no `NEEDS_MORE`.
- [ ] Negative verdict has `extractability_confidence = HIGH`.
- [ ] `coverage` lists every external/public entry point (EVM selectors or non-EVM instructions).
- [ ] `safe_reasons` has one concrete reason per value-moving path.
- [ ] A fresh-EOA closure artifact exists: fork/simulate revert, patched code match + live gate, or zero value proof.
- [ ] `value_at_risk_usd` and `tvl_source` are recorded.
- [ ] `headline_status` and `new_bugs` are explicit.
- [ ] If value at risk > $100k, the negative explains why that value is unreachable.
- [ ] Folder kept only if net > $5; otherwise `folder_removed = true` and the result is retained.

Reject the batch if any box is unchecked; re-run the target with a fresh agent.
