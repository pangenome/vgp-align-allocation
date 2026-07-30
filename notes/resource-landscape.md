# Resource landscape for the 2026/27 cycle

Checked 2026-07-28 against
<https://operations.access-ci.org/resources/access-allocated> and the ACCESS
operations news feed.

## Good news: nothing we depend on has retired

Every resource in the 2025/26 request is still ACCESS-allocated:

| Resource | Status | Notes |
| --- | --- | --- |
| TACC Stampede3 | Available | |
| TACC Ranch | Available | tape archival |
| PSC Bridges-2 RM | Available | |
| PSC Bridges-2 EM | Available | described for "memory-intensive genome sequence assembly" — our exact use case |
| PSC Ocean | Available | disk + tape tiers, single namespace via HPE DMF |
| SDSC Expanse CPU | Available | AMD Rome, 128 cores/node, 3.373 PF |
| SDSC Expanse GPU | Available | 52 nodes × 4 NVIDIA V100 (32 GB SXM2) |
| SDSC Expanse Projects Storage | Available | 5 PB Lustre |
| Purdue Anvil | Available | CPU, GPU, and AI variants |
| NCSA Delta | Available | 124 dual-socket AMD EPYC 7763 nodes; GPU nodes are A100-class |
| IU Jetstream2 CPU | Available | AMD Milan 7713, 128 cores/node |
| IU Jetstream2 Large Memory | Available | 32 × 1 TB RAM nodes |
| IU Jetstream2 GPU | Available | 360 NVIDIA A100 |
| IU Jetstream2 Storage | Available | |

The ACCESS operations news feed carries no retirement or decommissioning
announcements for 2026; Anvil, Jetstream2, Expanse, Bridges-2, and Delta all
appear in routine 2026 maintenance notices, confirming they are live. Expanse
specifically was still running as of a 2026-05-30 operations item.

**Consequence: the 2026/27 request can keep the same resource structure as
2025/26.** No forced re-planning.

## New: NCSA DeltaAI

**DeltaAI** — 114 NVIDIA Grace Hopper (GH200) nodes — is now ACCESS-allocated
and was not in our 2025/26 request. This is the most relevant new resource to
us, because the whole-genome alignment work is GPU-bound and KegAlign is the
thing that would use it.

Note a probable error in the 2025 Main document worth correcting: it justified
the NCSA Delta GPU line by saying *"access to H200 GPUs will enable utilization
of the new alignment method."* Delta's GPU nodes are A100-class; the GH200 parts
are on **DeltaAI**, a separate resource. If GH200 is what we actually want, the
2026 request should name **DeltaAI**, not Delta.

## Caveat on units — do not convert casually

Resources charge in different units and the conversions are not uniform:

- Stampede3 is charged in **node-hours**, not core-hours. Our usage tracking is
  in core-hours. Comparing 700 core-hours/month against a 250,000 node-hour
  request without dividing by cores-per-node overstates utilization by roughly
  two orders of magnitude.
- GPU resources charge GPU-hours, often with a multiplier against the CPU SU.
- Storage is in GB/TB, straightforward.

**Any SU figure in the request derived from our core-hour tracking must be
converted using the resource's published charging policy.** Confirm against the
ACCESS exchange-rate table before the numbers go in.

## Not verified

- Current **ACCESS Credits exchange rates** per resource, and whether any cap
  applies to a Maximize request. Check the allocations portal at submission
  time; these change between cycles.
- Whether our 2025/26 allocations on Bridges-2 and Stampede3 were exhausted or
  merely expired (both show exactly zero for May and June 2025). See
  `usage-data.md` — this materially changes what the Progress Report should say.
