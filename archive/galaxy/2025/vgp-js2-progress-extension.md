## **BIO240121: Deploying Vertebrate Genome Project (VGP) Data from ACCESS Resources**

**Progress Report (2025 Allocation Period)**

During the 2025 allocation period, we continued to build upon our prior success in deploying the Vertebrate Genomes Project (VGP) datasets across ACCESS resources, with an increased focus on enabling high-quality genome assembly workflows through the Galaxy platform operating on JetStream2 cloud infrastructure. Galaxy serves as a comprehensive, accessible environment for reproducible genome assembly, integrating essential tools, workflows, and training materials that democratize large-scale genomic analysis for the global research community.

A major milestone achieved during this period was the facilitation of 417 VGP genome assemblies executed via Galaxy running on ACCESS-CI resources. These assemblies represent reference-quality genomes across a broad range of vertebrate species, with genome sizes ranging from approximately 1 Gb to over 3 Gb and contig N50 values between 40 Mbp and 355 Mbp—often encompassing complete chromosomes and arms. The use of JetStream2 significantly improved scalability and responsiveness, allowing assembly jobs to run in parallel across hundreds of virtual nodes while maintaining tight integration with Galaxy’s provenance-tracking and data management systems.

This large-scale deployment not only highlights the performance capabilities of Galaxy for data-intensive genomics but also underscores JetStream2’s pivotal role as a unifying platform for VGP’s computational efforts. The system’s transparent workflow provenance, automated logging, and integrated visualization tools provide an unprecedented level of reproducibility and accessibility for large assembly tasks.

### **Encouraging global use of public infrastructure**

In parallel with these technical efforts, we have placed special emphasis on encouraging the global genomics community to perform large collaborative analyses on public research infrastructure such as JetStream2. This strategy leverages JetStream2’s open-access object storage, scalable compute, and reproducible workflow support to make downstream analysis broadly accessible to researchers worldwide. By promoting the use of public, community-supported cyberinfrastructure, we not only enhance scientific inclusivity but also increase the return on investment in national computing resources by demonstrating their effectiveness for large-scale, cost-efficient genomic research. This approach elevates the scientific value of JetStream2 and underscores its significance as a cornerstone for sustainable, transparent, and collaborative bioinformatics.

### **GenomeArk2.org: a unified distribution platform**

To further strengthen data accessibility and long-term sustainability, we are developing[ GenomeArk2.org](https://genomeark2.org) as the central distribution hub for VGP data (Figure on the next page). This resource will serve as the authoritative repository for reference assemblies, annotations, and downstream analysis results generated through the VGP and related initiatives. Built on top of JetStream2’s scalable object storage, GenomeArk2 provides fast, open access to petabyte-scale datasets while ensuring robust metadata support, versioning, and reproducibility. Its architecture is designed to integrate seamlessly with Galaxy and other community analysis systems, allowing researchers to discover, access, and process VGP data directly within public computational environments. By coupling open compute with open data distribution, GenomeArk2.org establishes an enduring model for transparent, FAIR (Findable, Accessible, Interoperable, and Reusable) genomics data dissemination.

  
  
  
  

|  |
| :-: |
|  |
| \*\*GenomeArk2\*\* (\<https://genomeark2.org/\>) was made possible via JetStream2 allocation |

### **Future Work**

In the upcoming allocation period, we plan to expand JetStream2’s role within the VGP ecosystem by deploying additional pipelines for assembly evaluation, polishing, and annotation within Galaxy. These efforts will leverage the same scalable infrastructure to streamline the generation and comparison of assemblies across diverse taxa.

In parallel, we are preparing a series of publications for Nature (under the umbrella of VGP Phase 1 completion) that will prominently feature JetStream2 as a key enabling infrastructure for large-scale, community-driven genome assembly. These papers will highlight how computational resources supported by ACCESS—specifically JetStream2—have made it possible to carry out hundreds of reference-quality assemblies reproducibly within the Galaxy environment, marking a major advance in open, accessible computational genomics.

  