# ACCESS-CI Maximize allocation rules and logistics — researched 2026-07-30

Every claim below carries a source. Items I could not verify from a primary
source are flagged explicitly rather than filled in by inference.

---

## 1. Required documents and page limits

Source: <https://allocations.access-ci.org/prepare-requests>

| Document | Pages | Required? |
| --- | --- | --- |
| Main Document | 10 | Yes |
| Progress Report | 3 | **Renewals only** |
| Code Performance & Resource Costs | 5 | Yes |
| Curriculum Vitae | 2 per individual | Yes, each PI and co-PI |
| References | no limit | Optional |
| Special Requirements | 1 | Optional |

**Main Document** must address: Scientific Background, Research Objectives,
Resource Usage Plan, Justification of allocation amounts, Resource
Appropriateness, and Access to other CI resources. Verbatim: *"Research request
must include a well-documented resource-use plan."*

**Code Performance & Resource Costs**, verbatim: *"REQUIRED document should
contain code performance timings, resource usage details, and scaling
information"* — must support calculation of the resource request with benchmark
data.

**CVs**: *"Two-page NSF or NIH formats are highly recommended."*

**References** is optional but worth using — it has no page limit and frees
space in the 10-page Main Document.

### Review criteria

Three core criteria: **Appropriateness of Methodology**, **Appropriateness of
Research Plan**, and **Efficient Use of Resources**, plus intellectual merit
alignment with supporting grants.

---

## 2. Submission windows — READ THE CAVEAT

**Correction to a common misconception: Maximize ACCESS is _semi-annual_, not
quarterly.** Policy page, verbatim: *"Maximize ACCESS requests are accepted,
reviewed, and awarded semi-annually."*
(<https://allocations.access-ci.org/allocations-policy>)

Two cycles per year, with award start dates in **April** and **October**.

### What is firmly verified

| Window | Award start | Source |
| --- | --- | --- |
| Dec 12, 2024 – Jan 31, 2025 | Apr 1, 2025 | [announcement, published 2024-12-05](https://support.access-ci.org/announcements/maximize-access-proposal-submission-window-opening-soon) |
| **Jun 15 – Jul 31, 2025** | **Oct 1, 2025** | [events/7893](https://support.access-ci.org/events/7893) |

Note the close date drifted: an older ACCESS announcement described the summer
window as *"June 15 to July 15"*, but the 2025 cycle actually ran to **July 31**.

### 2026 cycle

**Close date: July 31, 2026. Awards start October 1, 2026.** Confirmed by the PI.

Worth recording how thin the public trail was, in case a future cycle needs
checking: no primary ACCESS page confirmed the 2026 window. The announcements
feed (<https://support.access-ci.org/announcements>) carries no 2026 Maximize
announcement at all — its most recent Maximize posts are from late 2024 — and
both `allocations.access-ci.org` and its opportunities page sit behind an XRAS
login, so the live window state is not publicly fetchable. The only public
signal was a search-engine summary, which is not a source worth trusting on its
own.

**For future cycles, check the portal directly while logged in rather than
trying to confirm dates from public pages.**

---

## 3. Renewals

Source: <https://allocations.access-ci.org/allocations-policy> and
<https://allocations.access-ci.org/prepare-requests>

- Renewal requests should be submitted **approximately one year after the
  initial submission**.
- A **Progress Report (≤3 pages) is mandatory** for a renewal. Verbatim: it
  *"should describe how the PI's current or prior allocation was used and
  summarize findings or results."*
- It must **explain significant deviations** from originally proposed resource
  usage.
- Where a resource was underutilized, it *"should briefly describe the reasons
  for the underutilization and any mitigation."*
- Progress reports must also summarize accomplishments, describe resource usage,
  and identify publications.

This last set of requirements is the reason the Bridges-2 / Stampede3
zero-usage question in `usage-data.md` is blocking: the policy obliges us to
address underutilization directly, so we must know whether those lines were
exhausted or unused.

---

## 4. Allocation size, duration, and credits

Source: <https://allocations.access-ci.org/allocations-policy>

- **Duration**: *"awards are typically made for a 12-month period; shorter
  periods may be recommended by the review panel."* Extensions capped at six
  months.
- **No cap on request size**: verbatim, *"ACCESS does not place an upper limit
  on the size of allocations that can be requested or awarded"* — though
  individual Resource Providers may impose their own caps.
- **Supplements**: *"supplement requests have no limit, although Resource
  Providers may limit supplemental awards based on resource availability."*
  Relevant precedent — this project won three supplements in the 2023/24 cycle.
- **ACCESS Credits** apply to the smaller opportunities (Explore, Discover,
  Accelerate), where researchers exchange credits for resource-specific
  allocations, and initial awards grant half the credit limit with the remainder
  released on a progress report. **Maximize requests are made directly in
  resource units, so the credits mechanism is largely not our concern.**

### Eligibility

PI must be a US-based researcher or educator at graduate level or higher at an
eligible institution (academic, nonprofit, FFRDC, military academy, or
commercial). Institutional email must match institutional affiliation.
Unaffiliated individuals cannot serve as PI.

---

## 5. Exchange rates

**Not verified.** The exchange calculator at
<https://allocations.access-ci.org/exchange_calculator> is an interactive tool;
it documents that *"Each resource has a fixed exchange rate for ACCESS
Credits"* and that *"Most multicore compute resources are allocated in
core-hours, unless they are GPU-based resources, in which case the units tend to
be GPU-hours"*, with storage in gigabytes — but the numeric per-resource rates
are not present in the fetchable page content.

Since Maximize is requested directly in resource units rather than credits, this
is a low-priority gap. The unit conventions matter more than the rates, and
those are confirmed: **core-hours for CPU, GPU-hours for GPU, GB for storage —
except Stampede3, which charges node-hours.**

---

## 6. Resource landscape

See `resource-landscape.md` for the full table. Headline items:

- **Everything in the 2025/26 request remains ACCESS-allocatable.** No forced
  restructuring of the request.
- **TACC Frontera is retiring: queues stay open until September 30, 2026**,
  with login nodes and filesystems available a few months longer for data
  migration. Source: [TACC user update, "The Future of Frontera and
  Horizon"](https://tacc.utexas.edu/news/user-updates/107625/). Frontera is not
  an ACCESS-allocated resource and appears in our tables as "Frontera
  (non-ACCESS)" at ~2,899 core-hours/month, so the direct impact is small — but
  any workload still pinned there needs a destination before Oct 2026.
- **TACC Horizon**: early-user access began spring 2026; several thousand GPUs
  in bring-up. TACC states it will continue accepting allocations on **Vista**
  and **Stampede3** through the ACCESS program during the transition.
- **NCSA DeltaAI** (NVIDIA Grace Hopper GH200) is ACCESS-allocated and was not
  in our 2025/26 request. It is the correct target for KegAlign GPU work — our
  2025 request cited "H200 GPUs" on Delta, but Delta's GPU nodes are A100-class
  and the Grace Hopper parts live on DeltaAI.

---

## 7. Policy changes 2025–2026

**Nothing found that affects this renewal.** The ACCESS announcements feed for
2026 carries community and training items (Regional AI Workshops, EduHPC'26,
a workflows series) but no allocation policy changes, no new reporting
requirements, and no storage policy changes. The ACCESS operations news feed
carries no resource retirement or decommissioning announcements for 2026.

Caveat: absence of an announcement is weaker evidence than a positive
confirmation. If the portal shows anything unexpected at submission time, trust
the portal.
