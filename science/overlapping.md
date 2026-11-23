# Overlapping measurement windows

A window constraint can describe coherent access without requiring a single contiguous partition. Allow each elementary positive effect $`E_s`$ to be supported inside a specified interval $`I_s`$ of length at most $`\tau`$. Its label can merge with any other effect and the elementary effects resolve the identity. This includes measurements on disjoint pairs of temporal regions whose enclosing intervals overlap. The proof also works for countably many effects or a weak POVM integral with a measurable interval support assignment. The qubit still receives only the phase label at the common slot.

## Converse for arbitrary overlaps

Assume uniform intensity on $`[0,T]`$ and one linear phase winding. View time modulo $`T`$ for the proof. For a test center $`t_0`$, let $`A`$ be the circular interval of length $`\tau`$ around it, and $`B`$ its enlargement by $`\tau`$ on both sides. Assume $`\tau\le T/3`$. Sum all effects whose support intervals intersect $`A`$ to obtain $`F`$. It is a positive contraction, is supported in $`B`$, and fixes every amplitude supported on $`A`$ because all omitted effects annihilate that subspace. In particular, $`\langle u,Fu\rangle\ge\tau/T`$.

Write $`w_0=e^{2\pi i t_0/T}`$ and let $`d(t_0)`$ be the chord distance to the nearest correction phase. On the selected effects, the direct sum of vectors $`E_s^{1/2}(w_s-w_0)u`$ has norm at least $`d(t_0)\sqrt{\tau/T}`$. The direct sum of $`E_s^{1/2}(v-w_0u)`$ has squared norm at most

```math
\frac1T\int_B|e^{2\pi it/T}-w_0|^2\,dt
\le \frac{\tau}{T}\left(\frac{3\pi\tau}{T}\right)^2 .
```

The last bound follows by integrating the squared linear angle over $`[-3\tau/2,3\tau/2]`$. At zero error the two direct-sum vectors coincide, so the nearest phase is within chord distance $`3\pi\tau/T`$ of every point on the circle. A covering by these arcs needs at least $`\pi/[2\arcsin(3\pi\tau/(2T))]`$ labels when the arcsine argument is below 1. The segmented construction shows that the required count is of order $`T/\tau`$ as $`\tau/T`$ goes to zero.

The same argument controls nonzero error. Let $`R_s=\|E_s^{1/2}(v-w_su)\|^2`$, so $`\sum_sR_s=4\varepsilon`$ for the phase-assigned entanglement infidelity. The reverse triangle inequality bounds the sum on selected effects below by $`(\tau/T)(d(t_0)-3\pi\tau/T)_+^2`$. Averaging over the test center counts each effect over a set of length at most $`2\tau`$, and so

```math
\varepsilon\ge
\frac18\mathbb E_{t_0}(d(t_0)-3\pi\tau/T)_+^2
\ \ge\ \frac1{16}\left(\frac1M-\frac{3\pi\tau}{T}\right)_+^2 .
```

For the last step, arcs of radius $`\pi/(2M)`$ cover at most half the circle. Outside them the chord distance is at least $`1/M`$. Arbitrary qubit corrections reduce to phase corrections by [the decoder argument](model.md). Arrival-time detection supplies the matching $`M^{-2}`$ order when $`M\le T/(6\pi\tau)`$.

## A shorter span with the same labels

Place $`M\ge2`$ labels at the centers of equal time cells. Within each cell use left and right phase distances $`x,y\in[0,\alpha]`$ where $`\alpha=\pi/M`$. The integrated sine measure has cumulative value $`1-\cos x`$. Match opposite quantiles on the two sides using $`q=(1-\cos x)/(1-\cos\alpha)`$ and $`1-q`$ on the other side. For each pair,

```math
\cos x+\cos y=1+\cos\alpha,\qquad
x+y\le 2\arccos[(1+\cos\alpha)/2].
```

The inequality uses concavity of cosine on the half-cell. For any paired quantile bin, the imaginary contributions cancel exactly. The normalized overlap of that union of two time regions lies on the radius toward the cell's label, from zero to one. The common regular polygon contains that radius, so [exact recovery](exact.md) applies to each union. The enclosing intervals overlap, while the paired regions partition the input.

As the bins refine, the maximum achievable span approaches

```math
\tau_*(M)=\frac{T}{\pi}\arccos[(1+\cos(\pi/M))/2]
\sim \frac{T}{\sqrt{2}\,M}.
```

Indeed, take $`\delta=\tau-\tau_*(M)>0`$, partition each half-cell into physical lengths at most $`\delta`$, and use the common refinement of both quantile boundary sets. The largest spanning pair increases the pointwise bound by at most $`\delta`$. At fixed proportional slack this uses order $`M`$ subreceivers, each with at most three used outputs. For $`M=2`$ use two equal sine quantile bins per half-cell. The middle distance is $`T/6`$ and the outer distance is $`T/4`$, giving four binary subreceivers of span at most $`5T/12`$. Contiguous disjoint windows at that span need at least three labels. The constant in the optimal arbitrary-overlap threshold remains open.
