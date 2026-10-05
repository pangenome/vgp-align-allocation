# Appeal — BIO260405

Draft appeal against the reduced provisional award. **Submit by 2026-10-14**
(four weeks from the 2026-09-16 notification).

## How to submit

- Log in at <https://allocations.access-ci.org> (XRAS) → **My Projects / My
  Allocation Requests** → BIO260405 → submit an **Appeal** action (a special
  type of supplement) against the award.
- If no Appeal option is visible: email `allocations@access-ci.org` or open an
  ACCESS support ticket, citing the Appeal process in the Allocations Policy.
- Grounds (policy): (1) supply additional information or clarification
  requested by the reviewers; (2) rebuttal for a reduced allocation.
- Process: original AARC reviewers reconsider where possible; ~2-week response;
  the ACCESS Allocations Coordinator determines any increase; at least one
  favorable review is required.

## Verified facts to use

- Award: 6-month provisional, 2026-10-01 → 2027-03-31, 100,000 Stampede3 node
  hours (requested 1,000,000 SUs).
- Pilot: **581 assemblies, 336,980 ordered pairs, 3,265 jobs, 331,119
  node-hours, 25,050,213 core-hours** on Stampede3 under TG-MCB140147.
- Aligner cost: FastGA **88,546 node-h / 0.263 per pair**; wfmash 211,275 /
  0.627.
- Job states: **56.7% of node-hours TIMEOUT** (checkpoint/resume design);
  NODE_FAIL + FAILED = **18,666 node-h, 5.6%**; effective utilization ~94%.
- Node cores: SKX 48, ICX 80, SPR 112, H100 96.
- Queue wait (median / p90): SKX 17.1 h / 100.5 h; ICX 1.0 h / 61.8 h;
  **SPR 0.0 h / 10.3 h**; H100 0.0 h / 2.0 h.
- Publication: Formenti G, et al. *The Vertebrate Genomes Project Phase I: a
  global reference genome resource.* bioRxiv. 2026.
  doi:10.64898/2026.06.24.732306 (posted 2026-06-26). Co-authored by E.
  Garrison, S. Cao, A. Guarracino.
- **Preprint passage describing our pilot** (section "Initial phylogeny and
  whole-genome alignments"): *"We also performed an all-vs-all alignment of the
  579 species data freeze, using wfmash and FastGA, generating 336,980 pairwise
  alignment files in PAF format per method (Supplementary Table 11, row 17).
  Each alignment was indexed using impg…"*
- **Grant link from the preprint acknowledgements:** *"E.G., P.S., S.C.
  acknowledge funding from NIH R01HG013017 and U01HG013760."*
- Count reconciliation: 336,980 = 581 × 580. 581 assemblies = 579-species data
  freeze (566 vertebrate species + 13 outgroup species) + 2 additional
  haplotypes (human GRCh38, mouse GRCm39). Matches our manifest's 566 matched
  species / 568 Vertebrata / 13 outgroups. (Confirm against Supplementary
  Table 11.)
- Request sizing: 800 new assemblies → 1,568,800 new pairs → 412,594 node-h →
  ~825,000 SUs at SPR's 2 SU/node-h, plus ~175,000 for variance/rework.

---

## Draft appeal text

> **Appeal of the AARC outcome for BIO260405 — "All-to-all whole-genome
> alignment across the vertebrate tree"**
> PI: Erik Garrison, University of Tennessee Health Science Center
> Notified: 2026-09-16 · Appeal submitted: [DATE]
>
> To the ACCESS Allocations Coordinator and the AARC reviewers,
>
> We are grateful for the provisional award and we accept it. We submit this
> Appeal within the four-week window to supply the information and
> clarification the reviewers requested and to request reconsideration of the
> reduced award — a 6-month period and 100,000 Stampede3 node hours, against the
> standard 12-month period and the requested 1,000,000 SUs. Each reviewer
> concern is addressed below with verified information.
>
> **1. Supporting grants (raised by all three reviews).** The work is directly
> supported by merit-reviewed NIH awards. The VGP Phase I preprint's
> acknowledgements state that *"E.G., P.S., S.C. acknowledge funding from NIH
> R01HG013017 and U01HG013760"* — that is, this project's PI, P. Sudmant, and S.
> Cao were funded for the work reported in the paper by **R01HG013017** (complete
> T2T primate genomes, Multiple PI, 2023–2028) and U01HG013760 (Building Tools
> and Community to Make Pangenomes Accessible, Contact PI, 2024–2027). A primate
> pangenome R01 with P. Sudmant (Multiple PI) continues that line. Additional
> current support: R01HG013618 (pangenome-aware CRISPR design; D. Bauer, Co-I,
> 2024–2028); U01DA057530 (pangenome methods for hybrid rats, Co-I, 2023–2028);
> U41HG010972 (Human Pangenome Coordinating Center, Co-I, 2024–2027); and the
> present ACCESS Stampede3 allocation (2026). Two multi-institution R01
> applications are under review. The proposed vertebrate catalogue expansion is
> the natural scale-up of the primate comparative-genomics line above, and these
> awards provide the personnel who execute it. Under the Supporting Grant
> Alignment criterion, the request is consistent with these objectives.
>
> **2. Publications and scientific rationale (Review #1).** The Vertebrate
> Genomes Project Phase I completion paper was posted 2026-06-26, before this
> request: Formenti et al., *The Vertebrate Genomes Project Phase I: a global
> reference genome resource* (bioRxiv, doi:10.64898/2026.06.24.732306). The PI,
> S. Cao, and A. Guarracino are co-authors. The paper's "Initial phylogeny and
> whole-genome alignments" section explicitly reports our pilot: *"We also
> performed an all-vs-all alignment of the 579 species data freeze, using wfmash
> and FastGA, generating 336,980 pairwise alignment files in PAF format per
> method (Supplementary Table 11, row 17). Each alignment was indexed using
> impg…"* This is the same 336,980-pair result, computed with the same tools,
> from which every unit cost in this request is derived. The same paper's
> comparative analyses reconstruct the genome of the last common ancestor of
> vertebrates (~500 Myr), characterize sex-chromosome evolution and
> clade-specific 3D genome architecture, map methylation landscapes, and support
> IUCN extinction-risk analysis. This request extends that published backbone
> from the VGP set to the full public vertebrate catalogue. We will add this
> citation and move this rationale ahead of the methods in the revised request.
>
> **3. Parallelism, scaling, and efficiency (Review #0).** The pilot *is*
> evidence of parallel execution at scale: 336,980 independent ordered pairs
> computed across **3,265 jobs**, on four Stampede3 partitions (SKX 48, ICX 80,
> SPR 112, H100 96 cores per node), dispatched across nodes by pylauncher with
> within-node concurrency managed by ParaFly. The workload is embarrassingly
> parallel — N(N−1) tasks with no inter-task communication — and scales with
> node count until queue concurrency binds. The Code Performance document
> carries the measured per-pair cost (FastGA 0.263 node-h/pair over the same
> 336,980 pairs) and the queue-wait distribution. We will add a thread-scaling
> curve for a representative step to make the node-level efficiency explicit.
>
> **4. Wall-clock, checkpoints, and job accounting (Review #0).** The reported
> 56.7% of node-hours ending in TIMEOUT is not lost work; it is the normal
> terminal state of an intermediate link in the checkpoint-and-resume chain.
> Jobs run to the 48-hour limit and the next submission resumes from recorded
> completion state, so no completed pair is recomputed. Genuinely unrecoverable
> work — NODE_FAIL and FAILED — is 18,666 node-hours, **5.6% of consumption**;
> effective utilization is approximately 94%.
>
> **5. Queue choice (Review #0, "why SPR?").** SPR is not an arbitrary choice.
> Its measured median queue wait is **0.0 h** (p90 10.3 h), against SKX's 17.1 h
> median and 100.5 h p90. We size the request at SPR's higher charge (2 SUs per
> node-hour) precisely to remain conservative, not because we require SPR.
>
> **6. Contingency and milestone timeline (Review #2).** We will itemize the
> variance/rework allowance against measured quantities rather than carrying an
> unexamined 17%, and we will add the milestone timeline the reviewer requested.
>
> **Requested relief.** We ask the panel to increase the provisional award to
> the full 12-month period and the full 1,000,000 SUs, or to such amount as the
> panel deems appropriate. The measured pilot provides the empirical basis for
> the request, and the same team has now completed an equivalent campaign once.
> We will report progress under the provisional award regardless of this
> appeal, and we remain ready to answer any further questions.
>
> Respectfully,
> Erik Garrison

---

## Notes / caveats

- Confirm that R01HG013017's scope covers the vertebrate expansion (or phrase it
  as the primate line this scales up). The preprint does credit it for the pilot.
- Confirm the 581 = 579 + 2-haplotype reconciliation against Supplementary
  Table 11 before quoting the arithmetic.
- The thread-scaling curve is promised, not yet produced.
- Keep the tone factual; the appeal is judged by the original reviewers.
