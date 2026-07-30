# **The Galaxy ACCESS-CI Gateway 2023/24 allocation: A supplement Request**

**Anton Nekrutenko**, Penn State University

**Michael Schatz**, Johns Hopkins University

**Nate Coraor**, Penn State University

**Enis Afgan**, Johns Hopkins University  
**Philip Blood**, Pittsburgh Supercomputing Center

  

# **1. Summary**

Galaxy is a Science Gateway supporting over 3,000 users per month, from training workshops and classroom instruction to full genome assembly and analysis. The success of this platform, freely available to anyone since 2006, and the resources provided by ACCESS (and predecessors) since 2016 has enabled a massive amount of scientific progress, as exhibited by related publications, tracked at <https://www.zotero.org/galaxyproject/library>. 

One key component of this progress has been a partnership with the Vertebrate Genomes Project (<https://vertebrategenomesproject.org/>), which is now using Galaxy to further their goals of assembling all living vertebrate species. The bulk of this assembly is now performed on Jetstream2, along with many jobs run by other users of the Galaxy gateway. Because of this, we have demonstrated a significant ability to utilize granted resources. For this supplemental request we are asking for:

  - **Indiana Jetstream2 CPU: 2,500,000 SUs**
  - **\*\*Indiana Jetstream2 Large Memory: 2,500,000 SUs\*\***

# **2. Background**

## **2.1. A primer on Genome Assembly**

Genome assembly reconstructs sequences of individual chromosomes from massive volumes of genomic fragments obtained with heterogeneous sequencing technologies. Over the past 30 years (counting from the origins of the human genome project) changes in approaches to genome assembly closely followed the evolution of sequencing technologies. The initial human genome assemblies published in 2001 were produced from Sanger sequencing data using two competing strategies: hierarchical shotgun (HS; [\[1\]](https://paperpile.com/c/ejQZ9P/HHXvO)) and whole genome shotgun (WGS; [\[2\]](https://paperpile.com/c/ejQZ9P/VQae3)) (see also [\[3\]](https://paperpile.com/c/ejQZ9P/LPe9g)), although WGS proved to be far more efficient and quickly became the preferred approach. The disruption brought about by high throughput “next-generation” sequencing, or NGS, approaches in mid-2000s achieved high genome coverage at progressively decreasing cost and cemented WGS as the dominant strategy for genome assembly as it required minimal “wet-lab” components for DNA isolation and sequencing library preparation. During the subsequent years two main algorithmic strategies for graph-based genome assembly were developed: overlap graphs [\[4\]](https://paperpile.com/c/ejQZ9P/u9Sej) and De Bruijn graphs [\[5\]](https://paperpile.com/c/ejQZ9P/wBf7Z). Because early NGS technologies produced short reads (36-400bp), assemblies produced from these data were typically fragmented and often failed to resolve complex (e.g., repetitive, duplicated, etc.) genomic regions due to fundamental data limitations. Attempts to address these limitations included generating sequencing libraries for paired-end and mate-pair sequencing across a wide range of insert sizes [\[6\]](https://paperpile.com/c/ejQZ9P/2fN5s) to span the gaps between such regions. Development of long read single molecule sequencing technologies by Pacific Biosciences (PacBio) and Oxford Nanopore (ONT) disrupted the field again. Aside from length alone, there were significant increases in nucleotide-level accuracy with PacBio hi-fidelity (HiFi) reads achieving accuracies \>99.9% (\~20kb mean) and ONT reaching accuracies over 95% for reads between 50 and 150 kb. These dramatic improvements simplified the assembly problem by (1) allowing resolving individual haplotypes in polyploid genomes due to increased accuracy and (2) producing longer higher quality assemblies due the ability to resolve repetitive and duplicated regions with greater confidence.  Given sufficient read coverage (\>50✕) it is now possible to produce high-quality telome-to-telomere (T2T) assemblies of individual chromosomes [\[7\]](https://paperpile.com/c/ejQZ9P/mB2eO). Importantly, using long read data minimizes computational complexity of the assembly process, decreases its hardware requirements, and leads to reference quality genome assemblies.

## **2.2. Our current production-level pipelines.** 

We have developed a series of production-level workflows routinely used for assembly on ACCESS-CI resources. The workflows are designed to produce the highest quality genome assemblies for a variety of input data types (orange boxes in Fig. 1): each possible combination has a unique trajectory (orange circles and connecting lines in Fig. 1). The first stage of the pipeline is generation of k-mer profiles for estimation of genome size, heterozygosity, repetitiveness, and error rate necessary for parameterizing downstream workflows. K-mer counts can be generated from HiFi data only (Workflow 1) or include data from parental reads for trio-based phasing (Workflow 2). The second stage is the contig assembly. In addition to using only HiFi reads (Workflow 3), the contiging step can leverage HiC (Workflow 4) or parental read (Workflow 5) data to produce better-phased initial hap1/hap2 or parental/maternal assemblies. The contiging workflows also produce a number of critical quality

|  |
| :-: |
|  |
| \*\*Figure 1.\*\* A set of 10 prototype workflows for the assembly of HiFi data. Stages 1 - 5 correspond to the first five rows of Table 1. Eight analysis trajectories are possible depending on the combination of input data. Decision on invocation of workflow 6 is based on the analysis of QC output of  workflows 3, 4, or 5 (see Supplemental data for full explanation). Thicker lines connecting workflows 7, 8, and 9 represent the fact that these workflows are invoked separately for each phased assembly (once for maternal and once for paternal). |

control (QC) metrics such as k-mer multiplicity profiles [\[8\]](https://paperpile.com/c/ejQZ9P/IIvzg). Inspection of these profiles provides information necessary for deciding whether the third stage—purging—is required. Purging (Workflow 6) identifies and resolves haplotype-specific assembly segments incorrectly labeled as primary contigs as well as heterozygous contig overlaps increasing continuity and quality of final assembly [\[9\]](https://paperpile.com/c/ejQZ9P/I949z). The purging stage is generally unnecessary if HiC or Trio data is available. The fourth stage, scaffolding, produces chromosome-level scaffolds using information provided by optical mapping (BioNano, Workflow 7) and HiC (Workflow 8) data. The final stage of nuclear genome assembly is the decontamination procedure (Workflow 9) designed to remove exogenous (e.g. viral and bacterial) sequences. An additional dedicated workflow (Workflow 0) is tailored to  mitochondrial genome assembly. 

# **3. Request Justification**

Because Galaxy brings the computational and workflow complexity of genome assembly to everyone, and because the availability of assembly enables a greater range of downstream genomic analysis, the computational needs of researchers using Galaxy remains high. We mitigate this by limiting the number of concurrent jobs each user can have queued or running at a time, and aggressive policing for duplicate accounts. The unique opportunity to enable a massive scientific effort in the Vertebrate Genomes Project has presented a higher computational need than originally expected when crafting our allocation request in July 2023.

# **4. Metrics for success**

## **4.1. Usage monitoring**

Over first two months of 2024, we were able to transfer 0.25 PB of archived histories to Ranch, and believe we can continue at this rate to the full requested capacity of 3 PB before the end of the allocation period. Ranch regularly reports the amount of space used, making it quite easy to monitor progress.

## **4.2. Assessing usability by soliciting feedback** 

The project combines software development with resource maintenance and administration efforts. The quality assurance aspects of the software process including version control, continuous integration, team coordination, and testing. To ensure the quality of our public site we employ continuous monitoring as well as the communication channels described above. These support channels provide a reliable way to identify pain points that are experienced by multiple users. Errors arising during execution of Galaxy tools are reported using a built-in mechanism. This mechanism allows users to provide additional details about the error they experience. All training materials contain built-in questionnaires to provide us with feedback.

## **4.3. Support and communication**

Our online forum was moved to a Discourse-based platform and mailing lists have been replaced with Galaxy Gitter channels for conversational discussion. Both shifts make Galaxy more welcoming and engaging. News is communicated primarily through Galaxy Newsletters and Twitter (@galaxyproject, \>13,700 followers). Other communication channels include the Galaxy News feed [\[10\]](https://paperpile.com/c/ejQZ9P/YcwpU), the Galactic Blog [\[11\]](https://paperpile.com/c/ejQZ9P/zg5P5), and the Galaxy Events calendar [\[12\]](https://paperpile.com/c/ejQZ9P/LWCga), all of which are promoted on Twitter and in the newsletters. All are part of a larger effort—the Galaxy Community Hub [\[13\]](https://paperpile.com/c/ejQZ9P/qWRw4).

# **References**

1\.  [Lander ES, .... Initial sequencing and analysis of the human genome. Nature. Whitehead Institute for Biomedical Research, Center for Genome Research, Cambridge, Massachusetts 02142, USA. lander@genome.wi.mit.edu: Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved.; 2001 Feb 15;409(6822):860–921.](http://paperpile.com/b/ejQZ9P/HHXvO)

2\.  [Venter JC… The sequence of the human genome. Science. science.org; 2001 Feb 16;291(5507):1304–1351. PMID: 11181995](http://paperpile.com/b/ejQZ9P/VQae3)

3\.  [Waterston RH, Lander ES, Sulston JE. On the sequencing of the human genome. Proc Natl Acad Sci U S A. 2002 Mar 19;99(6):3712–3716. PMCID: PMC122589](http://paperpile.com/b/ejQZ9P/LPe9g)

4\.  [Myers EW. The fragment assembly string graph. Bioinformatics. 2005 Sep 1;21 Suppl 2:ii79–85. PMID: 16204131](http://paperpile.com/b/ejQZ9P/u9Sej)

5\.  [Pevzner PA. An Eulerian path approach to DNA fragment assembly. Proceedings of the National Academy of Sciences. 2001 Aug 14;98(17):9748–9753.](http://paperpile.com/b/ejQZ9P/wBf7Z)

6\.  [Nagarajan N, Pop M. Sequence assembly demystified. Nat Rev Genet. 2013 Mar;14(3):157–167. PMID: 23358380](http://paperpile.com/b/ejQZ9P/2fN5s)

7\.  [Rautiainen M, Nurk S, Walenz BP, Logsdon GA, Porubsky D, Rhie A, Eichler EE, Phillippy AM, Koren S. Telomere-to-telomere assembly of diploid chromosomes with Verkko. Nat Biotechnol \[Internet\]. 2023 Feb 16; Available from: ](http://paperpile.com/b/ejQZ9P/mB2eO)<http://dx.doi.org/10.1038/s41587-023-01662-6>[ PMCID: 7877196](http://paperpile.com/b/ejQZ9P/mB2eO)

8\.  [Rhie A, Walenz BP, Koren S, Phillippy AM. Merqury: reference-free quality, completeness, and phasing assessment for genome assemblies. Genome Biol. 2020 Sep 14;21(1):245. PMCID: PMC7488777](http://paperpile.com/b/ejQZ9P/IIvzg)

9\.  [Guan D, McCarthy SA, Wood J, Howe K, Wang Y, Durbin R. Identifying and removing haplotypic duplication in primary genome assemblies. Bioinformatics. 2020 May 1;36(9):2896–2898. PMCID: PMC7203741](http://paperpile.com/b/ejQZ9P/I949z)

10\.  [Galaxy News \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/ejQZ9P/YcwpU)<https://galaxyproject.org/news/>

11\.  [The Galactic Blog - Galaxy Community Hub \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/ejQZ9P/zg5P5)<https://galaxyproject.org/blog/>

12\.  [Galaxy Event Horizon \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/ejQZ9P/LWCga)<https://galaxyproject.org/events/>

13\.  [Home - Galaxy Community Hub \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/ejQZ9P/qWRw4)<https://galaxyproject.org>

  