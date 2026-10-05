# Special Requirements

We request two accommodations. Both concern throughput rather than volume, and
both are supported by measurement from our current work on Stampede3 under
TG-MCB140147.

## 1. Concurrent job limits

Our alignment workload is N(N−1) independent pairwise tasks with no inter-task
communication. We package these as command files, split into chunks, and
dispatch them with pylauncher across nodes with ParaFly managing within-node
concurrency.

**The number of chunks we create is set by how many jobs we may hold in the
queue, not by how much work remains.** This is the binding constraint on our
rate of progress. Across the 2,697 jobs belonging to multi-submission chains,
cumulative queue wait is 21,817 job-hours, of which 12,823 on SKX alone, where
wait is 17.1 hours at the median and 100.5 hours at the 90th percentile.

The completed pilot spanned portions of two award periods. Its calendar time
was governed by repeated queue waits rather than exhaustion of either
allocation. The new request increases the amount of independent work in flight,
so concurrency remains the determinant of whether we can consume the award
within its term.

We ask that per-user concurrent job limits be relaxed where possible, or that
the allocation be spread across several systems so that we can hold more work
in flight in aggregate. Breadth across resources is worth more to us than depth
on any single one.

## 2. Wall-clock limit

Our jobs run to the 48-hour limit and resume from recorded state on the next
submission. This works, and it is why our effective utilization is 94% despite
56.7% of node-hours ending in TIMEOUT. What it costs us is calendar time —
every link in a resumption chain pays the queue wait again.

A longer wall-clock limit would not reduce our service unit consumption. It
would reduce the number of resumption cycles, and with them the queue waits
that dominate our turnaround. Where a longer queue is available we would use
it. Where it is not, the concurrency accommodation in §1 is the substitute.

