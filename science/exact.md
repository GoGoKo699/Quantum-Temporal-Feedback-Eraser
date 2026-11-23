# Exact recovery with a common phase alphabet

A label specifies a unit complex number $`w_j`$, and the qubit holder applies its inverse phase. For the Bell-state score, block $`b`$ contributes $`\Re\sum_j\overline{w_j}c_{bj}`$. Its maximum is at most one by the [overlap constraints](model.md). If every positive-weight block attains one, all terms must align and exhaust the norm budget. Hence:

> Exact recovery is possible if and only if every $`z_b`$ lies in the convex hull of the same set of correction phases.

For sufficiency, let $`z_b=\sum_jq_{bj}w_j`$ with probabilities $`q_{bj}`$. Use effects with compressed off-diagonals $`q_{bj}w_j`$ and equal diagonals $`q_{bj}`$. Their rank-one Gram matrices define the [mode measurement](receiver.md), and the corrected qubit equals the input on every outcome of positive probability. This criterion uses the random-unitary recovery framework of [Gregoratti and Werner and Buscemi et al.](../references/RELATED_WORK.md). The new constraint is the common choice of phases across a specified measurement partition.

## Label count for a single turn

Suppose the relative phase is strictly monotone through one full turn on the packet, with positive intensity in the interior of each of $`K\ge2`$ contiguous windows. Write the phase arc of one window using its midpoint $`\theta_b`$ and halfwidth $`a_b`$. Since its conditional distribution assigns positive weight to the open arc,

```math
\Re(e^{-i\theta_b}z_b)>\cos a_b.
```

Any hull containing $`z_b`$ must therefore include a phase strictly in that arc. The open arcs are disjoint, so at least $`K`$ labels are necessary. A decreasing winding simply reverses the order.

For the upper bound, choose the mean $`z_*`$ of the overlaps. It lies inside the unit disk. Extend each ray from $`z_*`$ through a distinct noncentral point $`z_b`$ to meet the circle at $`w_b`$, so that $`z_b=z_*+s_b(w_b-z_*)`$ with $`0<s_b\le1`$. The defining mean relation implies $`\sum_b s_b(w_b-z_*)=0`$, with zero terms for central points. Hence $`z_*`$ and all overlaps are in the hull of at most $`K`$ phases. If all overlaps coincide, two endpoints of a chord through the common overlap suffice. With one coherent window, two phases suffice and are necessary for a nontrivial winding. In particular, the minimum over freely chosen contiguous partitions with maximum span $`\tau`$ is $`\max\{2,\lceil T/\tau\rceil\}`$.

## Uniform packet and message entropy

For the uniformly illuminated one-winding packet with equal windows, the overlaps are $`z_b=r e^{i\theta_b}`$ with $`r=\mathrm{sinc}(\pi/K)`$ and equally spaced centers $`\theta_b`$. Here $`\mathrm{sinc}x=\sin(x)/x`$. The regular polygon of the block centers suffices. If $`K`$ is even, each block uses its center label and its antipode only. At $`K=4`$, the two probabilities are $`(1\pm2\sqrt{2}/\pi)/2`$.

The alphabet count cannot be compressed to constant Shannon entropy on this uniform example. For any exact scheme draw the uniform block index $`B`$ and the emitted label $`Y`$. The convex decomposition gives

```math
\mathbb{E}|e^{i\theta_B}-w_Y|^2=2(1-r).
```

Estimate $`B`$ by the closest grid center to $`w_Y`$, and denote the signed cyclic error in block units by $`D`$. The angular distance is at most $`\pi/2`$ times the chord distance, and rounding adds at most half a block. Thus $`\mathbb{E}D^2\le 1/2+K^2(1-r)/4\le1/2+\pi^2/24`$. Given the estimate, the signed error specifies the actual block. By relative entropy to integer weights proportional to $`(1+d^2)^{-1}`$ and Jensen's inequality, $`H(B\mid Y)\le H(D)=O(1)`$. Therefore $`H(Y)\ge\log_2 K-O(1)`$, and the attained alphabet gives $`H(Y)\le\log_2 K`$. If the receiver can interfere the whole packet, the same input channel has zero total overlap and needs only one bit.
