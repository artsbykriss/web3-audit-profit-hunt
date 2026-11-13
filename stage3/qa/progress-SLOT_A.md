2026-11-13T16:43:19Z | S3-237 | DONE | S3-2411 NE HIGH $0; S3-2433 NE HIGH $0; S3-2517 NE HIGH $0 | Pine unverified impl: 49 selectors enumerated, all value paths gated; MEDIUM->HIGH x2
2026-11-13T16:47:02Z | S3-005 | DONE | S3-1096 NE HIGH $0; S3-1045 NE HIGH $0; S3-1063 NE HIGH $0 | privacy-pools vk matched to published withdrawal_vk.json (repo vkey stale) -> MEDIUM->HIGH; diamond 19 facets enumerated
2026-11-13T16:48:01Z | S3-037 | DONE | S3-0326 NE HIGH $0; S3-0336 NE HIGH $0; S3-0356 NE HIGH $0 | Du Bois: audited marketplace never deployed, DAU token role-gated & 0 ETH -> MEDIUM->HIGH
2026-11-13T16:48:36Z | S3-063 | DONE | S3-0271 NE HIGH $0; S3-0272 NE HIGH $0 (VAR $1152 unreachable); S3-0275 NE HIGH $0 | Cork beforeSwap unpatched but drain fork-proven revert + paused config -> MEDIUM->HIGH
2026-11-13T16:49:07Z | S3-114 | DONE | S3-0315 NE HIGH $0; S3-0316 NE HIGH $0; S3-0319 NE HIGH $0 | Derive manager metadata-hash version proof (3d5fe48c vs a68d5adc) + fork-proven guards -> MEDIUM->HIGH
2026-11-13T16:49:30Z | S3-151 | DONE | S3-0733 NE HIGH $0; S3-0734 NE HIGH $0; S3-0746 NE HIGH $0 (VAR $20.8k unreachable) | Resonate cross-asset consumer residue closed by state exhaustion (604 gwei / 0.43 WETH left / 6-vs-18 decimals) -> MEDIUM->HIGH
2026-11-13T16:50:22Z | S3-194 | DONE | S3-1103 NE HIGH $0; S3-1108 NE HIGH $0; S3-1112 NE HIGH $0 (VAR $1201 frozen) | zkLink closed with fresh-EOA claimMessage -> 'Not relayer' + paused escrow -> MEDIUM->HIGH
2026-11-13T16:50:49Z | S3-210 | DONE | S3-1724 NE HIGH $0; S3-1741 NE HIGH $0 (headline UNVERIFIED, TVL 0); S3-1751 NE HIGH $0 | Curves Form RPC still dead -> MEDIUM->HIGH on zero-TVL closure, code-coverage rows marked checked=false
2026-11-13T16:51:14Z | S3-217 | DONE | S3-1254 NE HIGH $0; S3-1275 NE HIGH $0; S3-1325 NE HIGH $0 (VAR $166.4k protocol-owned) | Abracadabra impl totalSupply=0 re-read, PMM fair pricing -> MEDIUM->HIGH
2026-11-13T16:52:06Z | S3-278 | DONE | S3-2031 NE HIGH $0; S3-2042 NE HIGH $0; S3-2044 NE MEDIUM $0 (VAR $20.9M) | sDOLA High-2 soft-liquidation on 33 loans/10.58M debt NOT PoC'd -> MEDIUM kept, path named
2026-11-13T16:53:01Z | S3-722 | DONE | S3-0353 NE HIGH $0; S3-0793 NE HIGH $0; S3-0795 NE HIGH $0 | SendIt: audited CosmWasm not deployed; Solana guards from ELF -> MEDIUM->HIGH (IDL caveat recorded)
2026-11-13T16:53:54Z | S3-732 | DONE | S3-0352 NE HIGH $0; S3-0417 NE HIGH $0; S3-0438 NE HIGH $0 | Glow closed by LCD zero-position + no-winner prize + insolvency -> MEDIUM->HIGH
2026-11-13T16:54:18Z | S3-740 | DONE | S3-0236 NE HIGH $0; S3-0237 NE HIGH $0; S3-0245 NE HIGH $0 | Cetus: 11 CLMM modules enumerated (no limit_order), v4 order_id check + math_u256 v7 -> MEDIUM->HIGH
2026-11-13T16:54:39Z | S3-760 | DONE | S3-1456 NE HIGH $0; S3-1970 NE HIGH $0; S3-2112 NE HIGH $0 | Lavarage: guard strings in ELF + ConstraintSeeds simulate -> MEDIUM->HIGH
2026-11-13T16:55:29Z | S3-765 | DONE | S3-2531 NE HIGH $0; S3-2626 NE HIGH $0; S3-2678 NE HIGH $0 | Render: claim tx account-list analysis (circuit-breaker TransferV0, separate pool); amount validation flagged LOW -> MEDIUM->HIGH
2026-11-13T16:55:49Z | S3-782 | DONE | S3-2106 NE HIGH $0; S3-2107 NE HIGH $0; S3-2111 NE HIGH $0 | Lavarage C4 H-01: simulate 6004/6006 on real positions + IDL discriminator match -> MEDIUM->HIGH
2026-11-13T16:56:14Z | S3-801 | DONE | S3-3248 NE HIGH $0; S3-3267 EXTRACTABLE MEDIUM $24.55 (unchanged, schema completed); S3-3282 NE HIGH $0 | NEAR manager closed by sandbox 'Missing wallets signatures' + predecessor-based FT id -> MEDIUM->HIGH
2026-11-13T16:56:35Z | S3-819 | DONE | S3-0551 NE HIGH $0; S3-0575 NE HIGH $0; S3-0811 NE HIGH $0 | Lulo: single accepted mint + max+1 clamp simulate -> MEDIUM->HIGH
2026-11-13T16:56:51Z | S3-834 | DONE | S3-2721 NE HIGH $0; S3-2310 NE HIGH $0; S3-2705 NE HIGH $0 | OctoLend audited bytecode still unlocated (stated); anchor CDDDLS Vault V2 auth-gated -> MEDIUM->HIGH
2026-11-13T16:57:07Z | S3-845 | DONE | S3-3683 NE HIGH $0; S3-1691 NE HIGH $0; S3-1190 NE HIGH $0 | Chainlink: audited Oracle addr not supplied, token anchor closed (no oracle logic, fixed supply) -> MEDIUM->HIGH
2026-11-13T16:57:25Z | S3-851 | DONE | S3-1863 NE HIGH $0; S3-1899 NE HIGH $0; S3-1915 NE HIGH $0 | Gearbox: getAddressOrRevert(LOSS_POLICY::ALIASED,310) reverts -> loss-shift branch unresolvable -> MEDIUM->HIGH
2026-11-13T16:57:56Z | S3-862 | DONE | S3-2668 NE HIGH $0; S3-2711 NE HIGH $0; S3-2756 NE HIGH $0 | SteakHut: deployer 21 creations enumerated (no Enigma), both anchors closed -> MEDIUM->HIGH
2026-11-13T16:58:04Z | SLOT_FINAL 22/22 complete
