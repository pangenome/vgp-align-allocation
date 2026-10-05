# Maximize ACCESS – August 2026 portal answers

## Request Information

**Project Title**  
All-to-all whole-genome alignment across the vertebrate tree

**Public overview**  
We will build a reference-free comparative resource that directly aligns vertebrate genome assemblies to one another and exposes the resulting alignment network through an interactive atlas and the `impg` implicit-pangenome toolkit. Our completed pilot contains 568 vertebrate assemblies and 13 phylogenetic outgroups—581 assemblies and 336,980 ordered pairs—computed on TACC Stampede3. The next clade-balanced tranche adds 800 current NCBI complete or chromosome-level assemblies, expanding coverage by 19 orders, 200 families, 779 genera, and 800 species. We will run FastGA pairwise alignment on standard Stampede3 CPU nodes, filter the results with SweepGA using a validated `wfmash` reference, and collate lightweight `impg` indexes at the end of each genome-versus-all batch. Pairwise PAF files, indexes, manifests, workflows, similarity summaries, and the interactive atlas will be released publicly through GenomeArk and GitHub. We request 1,000,000 Stampede3 service units for 1,568,800 new ordered alignments, runtime variation, and bounded rework.

**Keywords**  
comparative genomics, vertebrate genomics, whole-genome alignment, pangenomics, phylogenomics, FastGA, SweepGA, impg

**How do you plan to use this project?**  
Research (non-dissertation)

## Opportunity Questions

**How did you hear about ACCESS?**  
Choose the option corresponding to prior or current ACCESS use. We already use ACCESS through the Galaxy allocation `TG-MCB140147`. If the menu instead asks for a person or program, choose the closest truthful option and do not select Campus Champions unless applicable.

**Primary field of science**  
Biological Sciences — select Bioinformatics and/or Genetics and Genomics if those more specific entries are available.

**Secondary fields**  
Computational Biology; Computer and Information Science and Engineering, if available.

## Related Personnel

**PI**  
Erik Garrison — University of Tennessee Health Science Center

**Co-PIs / Allocation Managers**  
None required for this request unless another person needs authority to submit renewals or manage the allocation.

**Other collaborators for conflict-of-interest identification**  
- Shuo Cao
- Andrea Guarracino

Confirm that both remain significantly connected to this activity before entering them. Add any other scientific collaborator who will contribute to the alignment campaign or its analysis, even if that person will not use ACCESS directly.

## Supporting Grants

**Does this request include supporting grants?**  
Yes

**Supporting grants**
- NIH U01HG013760 — Building Tools and Community to Make Pangenomes Accessible — Contact PI — 2024–2027.
- NIH R01HG013017 — Complete T2T primate genomes — Multiple PI — 2023–2028. *(Anchor for the appeal; the VGP Phase I preprint credits this award to E.G./P.S./S.C.)*
- NIH R01 (primate pangenome) — Multiple PI with P. Sudmant.
- NIH R01HG013618 — Pangenome-aware CRISPR design — Co-I (D. Bauer) — 2024–2028.
- NIH U01DA057530 — Pangenome methods for hybrid rats — Co-I — 2023–2028.
- NIH U41HG010972 — Human Pangenome Coordinating Center — Co-I — 2024–2027.
- NSF 2118709 — PPoSS: LARGE: Panorama — PI — 2021–2026.

Two multi-institution R01 applications are under review.

Use the portal's exact award lookup or requested grant fields. Confirm each award is active on the submission date. Do not include the previously listed Qatari grant.

## Documents

Upload these PDFs:

| Portal type | Title | File |
| --- | --- | --- |
| Main Document | All-to-all alignment across the vertebrate tree | `build/main.pdf` |
| PI CV or resume | Erik Garrison CV | `build/cv-erik-garrison.pdf` |
| Code Perf & Scaling | Code Performance and Resource Costs | `build/perf.pdf` |
| Other / References, if available | References | `build/references.pdf` |
| Other / Special Requirements, if available | Concurrency and Wall-clock Requirements | `build/special-requirements.pdf` |

The abstract is entered as the public overview unless the portal exposes a separate abstract field later in the workflow.

## Access to Other Resources

We used TACC Stampede3 under the Galaxy gateway allocation `TG-MCB140147` to complete the 581-assembly pilot that supplies the measurements in this request. The Galaxy allocation PI has approved citation of that preliminary work. This request is distinct: it covers only ordered pairs involving the 800 newly selected assemblies and does not recharge completed pilot pairs. Source assemblies and durable public outputs reside in the GenomeArk bucket through the AWS Open Data Program. GenomeArk provides sponsored object storage, not an allocated compute resource under our control. One local L40S server supports software development, lightweight `impg` indexing, and small tests, but cannot execute the production pairwise campaign. We are not requesting or using another national compute allocation for the proposed work.

## Available Resources

Select only:

**TACC Dell/Intel Sapphire Rapids, Ice Lake, Skylake (Stampede3)**

Requested amount: **1,000,000 SUs**

Resource justification:

The requested tranche adds 800 assemblies to the completed 581-assembly pilot, producing 1,568,800 new ordered pairs. FastGA consumed 0.263 node-hours per ordered pair at pilot scale. At Stampede3's highest standard CPU charge of 2 SUs per node-hour, alignment costs at most approximately 825,000 SUs. The remaining approximately 175,000 SUs cover input-dependent runtime variation and bounded rework. Tasks are independent, single-node, and CPU-only. We request no GPU, large-memory, storage, or tape resource.

## Final portal walkthrough

1. Enter the title, public overview, and comma-separated keywords above.
2. Select **Research (non-dissertation)**.
3. Complete the ACCESS-discovery question with the closest truthful prior-user option.
4. Select Biological Sciences and the most specific available genomics/bioinformatics field.
5. Verify Erik Garrison is the sole PI.
6. Add collaborators for conflict checking. Do not give them allocation roles unless they need account authority.
7. Add the grants listed above only where the portal confirms the award is active on the submission date.
8. Upload the PDFs using the document mapping above.
9. Paste the Access to Other Resources statement.
10. Select only Stampede3 and request 1,000,000 SUs. Paste the resource justification.
11. Use the exchange calculator to confirm that the displayed credit/SU conversion still yields the intended 1,000,000 Stampede3 SUs.
12. Review the generated request summary for changed units, missing required fields, or unexpected storage resources.
13. Save a final portal draft or PDF preview before pressing Submit.
