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

**Correction (2026-07-30).** An earlier note here claimed the 2025 Main
document was wrong to cite "H200 GPUs" on Delta. That claim was itself wrong,
and the corresponding parenthetical has been removed from `main.md`.

Delta **does** now have H200 nodes: 8 nodes × 8 NVIDIA H200 (141 GB HBM3e),
schedulable via the `gpuH200x8` / `gpuH200x8-interactive` partitions at a 3.0
charge factor, awarded September 17, 2025 through the NSF NAIRR Pilot. Sources:
<https://delta.ncsa.illinois.edu/hardware_and_network/>,
<https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/running_jobs.html>,
<https://operations.access-ci.org/node/593>.

DeltaAI is a separate and larger system — **152 nodes / 608 H100** on GH200
superchips, up from the 114 nodes the ACCESS catalog still advertises. Either
would serve KegAlign; we are requesting DeltaAI on scale grounds.

### Other catalog entries that understate current capacity

The ACCESS resource descriptions lag the hardware in at least three places, so
do not size a request from the catalog blurb:

- **Jetstream2 GPU** is listed as "360 NVIDIA A100" but now also has **96
  NVIDIA H100** (24 nodes) and **32 L40S** (8 nodes).
  <https://docs.jetstream-cloud.org/overview/config/>
- **DeltaAI** listed at 114 nodes; actually 152.
- **TAMU ACES** has a Grace-Hopper node (`gh01`) absent from its description.

### Purdue additions worth knowing about

- **Anvil AI** (production 2025-02-19, open to ACCESS July 28 2025): 21 nodes ×
  4 NVIDIA H100 80GB = 84 H100. Guidance is to request "Purdue Anvil AI"
  explicitly rather than "Purdue Anvil GPU," which yields A100s.
- **Anvil Notebook** (production 2026-04-01): JupyterHub service with
  fractional GPU allocation, aimed at classroom use. Potentially relevant to
  Galaxy Interactive Tools and TIaaS training events.
- **Anvil Object Storage**: 1 PB Ceph S3, ACCESS-requestable since June 4 2026.

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
