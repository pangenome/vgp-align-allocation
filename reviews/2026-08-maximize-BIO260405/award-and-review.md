# BIO260405: ACCESS Maximize award notification and reviewer comments

Interned verbatim from the ACCESS Allocations Service email. This is the record
of what was decided and said; do not edit the quoted text.

- **Request number:** BIO260405
- **Project title:** All-to-all whole-genome alignment across the vertebrate tree
- **PI:** Erik Garrison, University of Tennessee Health Science Center
- **Type:** New Maximize
- **Recommended:** Provisional award, 6 months (instead of the standard 12)
- **Award period:** 2026-10-01 to 2027-03-31
- **Awarded resources:** TACC Stampede3 (Dell/Intel Sapphire Rapids, Ice Lake,
  Skylake) — 100,000.0 Node Hours
- **Estimated value:** $20,000.00
- **Renewal submission window:** 2026-12-15 to 2027-01-31

The panel asks that the reviewer comments be addressed in a document known in
the submission system as **"Addressing Reviewer Comments"**, submitted with the
other required documents as a **"renewal"** in the submission system:
<https://allocations.access-ci.org/prepare-requests>

If the reviewer comments are addressed in the revised request, a renewal of a
12-month award will be recommended, with the potential for all service units
requested within the renewal proposal.

---

## Award notification (verbatim)

> Dear Dr. Garrison,
>
> Congratulations! Your Maximize request, "All-to-all whole-genome alignment
> across the vertebrate tree" (BIO260405), has been reviewed by the ACCESS
> Allocation Review Committee (AARC) and approved for an award. If this is your
> first Maximize project, welcome!
>
> The ACCESS Maximize review panel has recommended a "Provisional Award" of 6
> months instead of the standard 12 months. The reviewers were encouraged by
> your request but felt it was not suitable for a full award. Rather than
> declining the proposal, they recommended a partial award to begin working on
> your proposed research. A revised renewal request is to be submitted during
> the December 15, 2026 - January 31, 2027 submission period. If the reviewer's
> comments are addressed in the revised request, a renewal of a 12-month award
> will be recommended with the potential for all service units requested within
> the renewal proposal.
>
> The reviewer's ask that you address their comments in a document known in the
> submission system as "Addressing Reviewer Comments" which will be included
> along with all other required documents and submitted as a "renewal" in the
> submission system: https://allocations.access-ci.org/prepare-requests See the
> bottom of this message for project award details and reviewer comments. You
> can also see the reviewers' comments any time in the ACCESS Portal
> (https://allocations.access-ci.org). Log in, click on Allocations, then select
> My Allocation Requests.
>
> By default the PI, all co-PIs, and all Allocation Managers will be added to
> the resources awarded. PIs, co-PIs, or Allocation Managers can add additional
> persons to or remove persons from resources on this project via the ACCESS
> portal.
>
> The estimated value of these awarded resources is $20,000.00. The allocation
> of these resources represents an investment by the NSF in advanced computing
> infrastructure for the U.S. The dollar value of your allocation is estimated
> from the NSF awards supporting the allocated resources.
>
> In exchange for using ACCESS resources, we ask just two things. First, help
> us improve our reporting by keeping your ACCESS user profile up to date,
> including the demographic fields. Second, for any published works resulting
> from this project, please acknowledge use of ACCESS and allocated resources.
>
> Best regards,
>
> ACCESS Allocations Service

---

## Review #0

**Overall Rating: Fair**

**Assessment and Summary:** This proposal is a new proposal requesting 1 M Node
Hours on Stampede 3. PI reported no funding support in the main proposal
document. However, PI's biosketch shows NSF and NIH funding support. PI stated
that completed pilot contains 568 vertebrate assemblies and 13 phylogenetic
outgroups—581 assemblies and 336,980 ordered pairs—computed on TACC Stampede3.
It does not show any usage of computational resource. The code performance and
scaling is not clear due to lack of information regarding the parallel use of
nodes. PI requests 1,000,000 Stampede3 service units for 1,568,800 new ordered
alignments, runtime variation, and bounded rework.

PI noted "To remain conservative, we size the tranche at the highest standard
CPU charge rate, SPR's 2 SUs per node-hour. Adding approximately 800 assemblies
requires 1,568,800 new pairs, 412,594 node-hours, and at most approximately
825,000 SUs. The remaining approximately 175,000 SUs cover input-dependent
runtime variation and bounded rework." Furthermore, "Its exact accession
manifest and reproducible selection script accompany the working materials.
Stampede3 bills node-hours at queue-specific rates: 1 SU on SKX, 1.5 SUs on
ICX, and 2 SUs on SPR [14]."

Is there any reason to run calculations on SPR queue?

In this project, PI proposes to study approximately 1,381 total assemblies of
complete or chromosome-level.

Lack of information of how many calculations/jobs will be submitted for
completing the project. Is there any checkpoint to restart the job if it
exceeds the wall clock time limit of 48 hours.

It is unclear of PI's request of "a longer queue is available we would use it".

This proposal should provide more details and strong justification for a large
request.

This reviewer recommends provisional support for six months.

**Appropriateness of Methodology:** With the evidence of previously performed
calculations on Stampede3, the methodology seems appropriate.

**Appropriateness of Plan for Resource Use:** It seems that this resource is not
appropriate. PI needs the resources with a longer queue (it means that more
wall clock time for jobs). Restart or timeout happened for many jobs over 50%
cases. It is also not clear the time loss for restarting the jobs. How good the
checkpoint files for restarting the jobs.

**Efficient Use of Resources:** PI stated "The alignment workload is
embarrassingly parallel — N(N−1) independent pairwise tasks — and distributes
across arbitrary numbers of nodes and across multiple systems without
modification. This is why access to several resources in parallel is useful to
us rather than merely convenient."

The efficiency of using the requested time is not clearly convinced by the data
and information provided by the PI.

## Review #1

**Overall Rating: Good**

**Assessment and Summary:** The PIs explain methodology and progress in
analysis, but it's unclear the biological imperative or impacts from the work.
PIs reference no publications or grants associated with the work in the portal
nor explain why the analyses are important. However, if you look at their CV
there are a few publications and grant titles that are probably associated with
the analysis. The project seems associated with Galaxy, however Galaxy submits
their own platform scientific justifications that don't include the VGP
project. Therefore, it's not possible to judge why this work is important or
provide justification for allocating 1 million SUs as a reviewer.

In the future it will be important to include a research justification that
might explain questions like why these pangenomes are important, or what impact
they have or will have on genomics, or why are PIs using all 4,467 NCBI
chromosome level vertebrate assemblies (other than that's what's available).
Redoing a pangenome assessment of all known vertebrate genomes seems
interesting and exciting; it shouldn't be difficult to provide justification.

**Appropriateness of Methodology:** PIs have scripted automatic analytical
pipelines and have a clear plan for continued analysis. They plan to submit
pangenomes to GenomeArk for long-term storage and reuse.

**Appropriateness of Plan for Resource Use:** PIs are currently running analyses
on Stampede3 in a tested and assessed analysis pipeline. No concerns. PIs are
not requesting additional storage.

**Efficient Use of Resources:** PIs provide error rates at 5.6% in an automated
pipeline on Stampede. They explain that timeout status in half of the jobs is
part of the checkpointing pipeline.

## Review #2

**Overall Rating: Good**

**Assessment and Summary:** The new Maximize ACCESS project request has good
potential to contribute to ACCESS's mission for enabling meritorious
computing/data-intensive science and technology development and for educating a
knowledgeable, skilled cyberworkforce through ACCESS resources and services.
The proposed project, overseen by a PI with considerable domain knowledge and
experience, contains necessary sections largely conforming to
application-specified Scientific Background, Research Objectives, Resource
Usage, Allocation Justification, Resource Appropriateness, Disclosure of
Alternative CI Resources and Services, and other supporting sections (e.g.
guideline-adherent PI CV). Although sections fail to exactly match application
guidelines for request organization, the content provided covers the main
topics with very good descriptions. Research team could be better elaborated
for organization, duties, and time dedication. Sections detail continuing
construction of a reference-free bioinformatics resource that will align
vertebrate genome assemblies and report the alignment network through an
interactive atlas and toolkit. Allocation request will enhance the team's
ability to increase scale of the reference databases. The ongoing ambitious
work is not supported by grants, and no relevant manuscripts are being
prepared, in press, or published at peer-review journals or other suitable
outlets. The project is well justified with scientific, technical, and social
merit. The project team has maintained a strong multi-year relationship with
and understanding of previous XSEDE and now ACCESS resources and services from
TACC. The research team has effectively optimized compute and storage utility
through well-conceived, past-usage-based performance and scaling enhancements on
relevant platforms, although the 17% continency request may be too much. The PI
intends to continue revising compute and storage benchmarks as the work
proceeds to completion.

**Appropriateness of Methodology:** The PI demonstrates extensive professional
qualifications and experience in bioinformatics. Described systems, tools, and
methodologies for computational studies and end-to-end data pipeline management
are appropriate, having been carefully and thoroughly perfected over years by
the project team. The research compute and storage requirements far exceed the
performance and capacity limits of the PI's institutional computational
environment resources, justifying some award of allocation requests.

**Appropriateness of Plan for Resource Use:** The research plan is appropriate,
although a timeline of milestones would be useful.

**Efficient Use of Resources:** The PI provided satisfactory use-history
documentation and benchmarking test results and predictions that the requested
allocations are sufficient and necessary to complete the identified scientific
objectives.
