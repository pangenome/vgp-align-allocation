# Special Requirements — The Galaxy ACCESS-CI Gateway 2026/27 allocation

*(Optional document, 1 page limit)*

The Galaxy gateway is not a single research code submitting a predictable job mix. It is a multi-tenant service that submits jobs on behalf of thousands of independent researchers, and this produces several requirements that do not fit the assumptions of standard batch allocations.

**Per-user queue depth limits are our binding constraint, not core-hours.** Because all gateway jobs are submitted under a single community account, per-user queue limits apply to the aggregate of all our users. Stampede3 limits users to 12–40 queued jobs depending on partition, and Expanse limits users to 64. A gateway serving thousands of monthly active users routinely has far more work ready to run than any one system will accept from a single account. This is why we request allocations on several similarly configured systems (Bridges-2, Expanse, Anvil) for what is nominally the same workload. It is a throughput requirement, not redundancy, and it is the reason a larger allocation on any single one of these systems would not substitute for allocations spread across all of them. Where a resource provider can raise the queue depth limit for a recognized community account, that is materially more valuable to us than additional SUs.

**Interactive latency requirements.** Galaxy presents a web interface, and users expect results in a timeframe consistent with an interactive system. Long queue waits are functionally equivalent to unavailability for a substantial fraction of our workload. This is the principal reason Jetstream2 — a cloud-style resource we can scale on demand via Slurm's cloud scheduling — carries the largest share of our request. Galaxy Interactive Tools (Jupyter, RStudio) are stricter still: they require a container to start promptly and then persist for the duration of a user session.

**Unprivileged access to CVMFS.** Galaxy distributes ~6 TB of reference data and all tool containers through CernVM-FS. On systems where CVMFS is not natively mounted we deploy `cvmfsexec` together with Apptainer to reproduce, on unprivileged shared HPC nodes, an execution environment identical to that on our dedicated cluster. Continued support for unprivileged user namespaces and FUSE on allocated systems is a hard requirement. Without it, entire classes of jobs cannot be routed to a resource regardless of how many SUs we hold there.

**Persistent, long-lived services.** Beyond batch jobs, the gateway requires continuously running components: CVMFS Stratum 0/1 replicas, and the object storage behind GenomeArk2 (<https://genomeark2.org>), the public distribution platform for Vertebrate Genomes Project data. These are steady-state capacity commitments rather than burst usage, and they cannot be drained and restarted between allocation periods without interrupting a public data resource used worldwide.

**Bursty, unpredictable load.** Our load is driven by external events — publication of a major dataset, a pandemic, a training workshop with fifty simultaneous participants running genome assembly. We manage the training case explicitly through Training Infrastructure as a Service (TIaaS), which reserves a dedicated queue for the duration of an event. The general case we manage by spreading load across resources, which again argues for breadth of allocation over depth on any single system.

**Long-running jobs.** Genome assembly and whole-genome alignment jobs routinely exceed typical partition walltime limits. Where a resource offers a long-queue partition, access to it is more valuable to us than an equivalent quantity of SUs in the standard queue.

<!-- TODO before submission:
- Confirm the CVMFS reference data footprint (5.8 TB as of the 2025 report).
- Confirm current queue depth limits on each requested resource — they may have changed.
- If any resource provider raised our queue limits during 2025/26, say so and quantify the throughput gain — it is a strong, concrete result.
-->
