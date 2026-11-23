# Approximate recovery and the arrival-time benchmark

## Exact score for fixed phases

Let $`P`$ be the hull of $`M\ge2`$ distinct unit phases. For a given block overlap $`z`$ inside $`P`$, the optimal Bell-state score is 1. Otherwise $`z`$ lies outside a unique supporting chord, in the disk segment of one gap between consecutive labels. Write their phases as $`\nu e^{\pm ia}`$, set $`h=\cos a`$ and $`x=\Re(\bar\nu z)>h`$. The optimal block score is

```math
C(z;P)=xh+\sqrt{(1-x^2)(1-h^2)}.
```

For the converse, use each $`\beta\ge0`$ and the [constraints](model.md) to get

```math
\Re\sum_j\bar w_jc_j
\le\max_j|w_j+\beta\nu|-\beta x
=\sqrt{1+2\beta h+\beta^2}-\beta x.
```

The minimum is attained at $`\beta=x\sqrt{1-h^2}/\sqrt{1-x^2}-h`$, with the boundary $`x=1`$ given by continuity. For attainment, take two normalized off-diagonal phases $`\nu(x\pm i\sqrt{1-x^2})`$, assigned to the corresponding chord endpoints. Choose their weights to match $`\Im(\bar\nu z)`$. This is possible because $`|z|\le1`$. The matching Gram matrices give a two-port measurement. When $`M=1`$ the score is simply $`\Re(\bar w_1 z)`$. Average the block scores with weights $`p_b`$ and optimize the common phases to obtain the optimal channel error via [the decoder reduction](model.md).

## Arrival time at the same message budget

For a uniform one-turn packet, a direct ideal time measurement produces a uniform phase on the circle. A classical encoder can map each time to the closest correction phase. Given circular gaps $`\Delta_j`$ between phases, the resulting score is $`\sum_j\sin(\Delta_j/2)/\pi`$. A different encoding, including randomized encodings, cannot exceed the pointwise largest cosine. Concavity of sine on $`[0,\pi]`$ makes equal gaps optimal, giving

```math
\varepsilon_{\mathrm{arr}}(M)
=\frac{1-\mathrm{sinc}(\pi/M)}2 .
```

This detector has arbitrary timing resolution and pays the same fixed message cost. Its error is strictly positive for every finite $`M`$.

## Optimal order below the exact threshold

For $`K\ge4`$ equally sized blocks of the uniform packet, write $`r=\mathrm{sinc}(\pi/K)`$ and $`\alpha=\arccos r\le2\pi/(3K)`$. The latter follows from the elementary bounds $`\mathrm{sinc}x\ge1-x^2/6`$ and $`\cos(2x/3)\le1-2x^2/9+2x^4/243`$ on $`0\le x\le\pi/2`$.

If the nearest phase label is angular distance $`d_b`$ from block center $`\theta_b`$, the same dual bound with normal $`e^{i\theta_b}`$ gives block error at least $`\sin^2((d_b-\alpha)_+/2)`$. Each label lies at distance strictly less than $`\pi/K`$ from at most one center. At least $`K-M`$ centers therefore have error at least $`1/(9K^2)`$.

For $`K/2\le M<K`$, merge $`K-M`$ disjoint neighboring pairs of centers into their midpoints. Keep all other centers as labels. The largest label gap is at most $`4\pi/K\le\pi`$, so the hull contains the origin. Every unmerged block is corrected exactly. Each paired block may ignore its local measurement and use its nearest midpoint at error $`[1-r\cos(\pi/K)]/2\le\pi^2/(3K^2)`$. Combining the bounds gives

```math
\frac{K-M}{9K^3}\ \le\ \varepsilon_{\mathrm{seg}}(K,M)\
\le\ \frac{2\pi^2(K-M)}{3K^3}.
```

For $`1\le M\le K/2`$, at least $`K/8`$ centers have distance at least $`3\pi/(8M)`$ from every label. Indeed, each such covering arc contains at most $`3K/(8M)+1`$ grid points. The same dual bound gives $`\varepsilon_{\mathrm{seg}}\ge1/(4608M^2)`$, while the direct arrival receiver gives $`\varepsilon_{\mathrm{seg}}\le\pi^2/(12M^2)`$. The near-threshold improvement is most pronounced at $`M=K-1`$. The bounds determine the order in both regimes and leave the optimum finite placement of labels as a continuous geometric problem.
