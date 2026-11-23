# Optical loss, alignment and timing

This analysis uses the even-$`K`$ discrete receiver in [Building the receiver](receiver.md), with uniform block weights and $`\eta=\pi/(2K)`$. Compare it with direct readout of the same two time bins and the same number of feedback labels. Loss in the early and late paths has intensity transmissions $`q_E,q_L`$, respectively. Equal efficiency at both final detector ports is absorbed into those transmissions. The aligned residual pulse shapes have mean complex overlap $`\gamma`$, after including unobserved phase fluctuations. Set the interferometer so the monitored overlap is $`|\gamma|`$. This model describes arm-dependent attenuation and distinguishability of the two paths.

## Exact corrected coherence

The click probability $`p=(q_E+q_L)/2`$ is independent of the qubit, since the conditional input intensities agree. Define $`A=2\sqrt{q_Eq_L}/(q_E+q_L)`$ when $`p>0`$. Before transmission, the difference of the two detector effects in the early/late basis is the off-diagonal observable with entry $`e^{-i\eta}`$. After arm loss and mismatch its entry is $`\sqrt{q_Eq_L}|\gamma|e^{-i\eta}`$. In block $`b`$, correcting the two detector outputs by opposite phases multiplies this difference by $`e^{-i\theta_b}`$. Using the two branch waveforms gives total click coherence $`\sqrt{q_Eq_L}|\gamma|`$ before dividing by the click probability. Thus the conditional coherence is $`C_{\mathrm{coh}}=A|\gamma|`$.

Use one of the same labels on a no-click trial. The no-click contribution to aggregate qubit coherence is zero, since the loss mechanism is the same in every block and $`\sum_b e^{i\theta_b}=0`$. The overall coherence is $`pC_{\mathrm{coh}}`$ and the unconditional error is $`(1-pC_{\mathrm{coh}})/2`$. The matched timing detector's coherence also scales by $`p`$ under the same fixed fallback. Guaranteed exact recovery requires perfect transmission in this unconditional model.

## Optimal direct timing with the same arm losses

The detected arrival phases form $`2K`$ equally spaced points with alternating weights proportional to $`q_E,q_L`$. For given correction phases, assigning each point to its nearest label is optimal for the cosine score. The assignments can be consecutive cyclic runs, with boundary ties broken cyclically. Reoptimizing the label of a run yields the magnitude of its weighted phasor sum. An optimal partition can use exactly $`K`$ nonempty runs, since splitting a run never reduces that sum.

Write $`S=q_E+q_L`$, $`D=q_E-q_L`$, $`B=\sqrt{S^2\cos^2\eta+D^2\sin^2\eta}`$ and $`h=B-S/2`$. The unnormalized phasor magnitude of an even run of length $`n`$ is $`B\sin(n\eta)/\sin(2\eta)`$. For an odd run starting on the heavy or light parity, use the respective sign in

```math
g_{\pm}(n)=
\frac{S\sin(n\eta)}{2\sin\eta}
\ \pm\ \frac{D\cos(n\eta)}{2\cos\eta}.
```

These expressions follow by summing the alternating phasors about their midpoint. The bounds on even and odd run magnitudes, respectively, are $`B+(n-2)h`$ and $`B+(n-2)h\pm D/2`$. For even lengths, the bound is exact at $`n=2`$ and holds at $`n=4`$ since $`B\ge S\cos\eta`$ and $`\cos\eta(3-2\cos2\eta)\ge1`$ for $`K\ge2`$. The sine curve is concave on the permitted range, extending the bound to larger even lengths. For odd lengths it is exact at $`n=1`$ and holds at $`n=3`$ by $`S\cos^2\eta\mp D\sin^2\eta\le B`$, from Cauchy–Schwarz. The functions $`g_\pm`$ are nonnegative and concave on $`[1,2K-1]`$, extending the bound to larger odd lengths. The start parities of successive odd runs alternate, so the signed terms cancel. Summing the lines over $`K`$ runs of total length $`2K`$ gives $`KB`$, attained by pairing adjacent arrival phases. Dividing by $`KS`$ proves

```math
C_{\mathrm{arr}}=\sqrt{1-A^2\sin^2\eta}.
```

Consequently the coherent receiver beats optimal matched timing, either conditional on clicks or unconditionally under the common fallback, exactly when $`A^2(|\gamma|^2+\sin^2\eta)>1`$.

## Timing and phase tolerances

For identical Gaussian pulse intensities of rms width $`\sigma_t`$, deterministic relative delay $`\Delta t`$ and independent zero-mean Gaussian interferometer phase of rms width $`\sigma_\phi`$, the mean overlap is

```math
|\gamma|=\exp\!\left[-\frac{\Delta t^2}{8\sigma_t^2}
-\frac{\sigma_\phi^2}{2}\right].
```

For balanced arms, the criterion is $`|\gamma|>\cos(\pi/(2K))`$. At $`K=16`$, this requires $`|\Delta t|<0.197\,\sigma_t`$ if delay is the only degradation, or $`\sigma_\phi<0.0983`$ rad when phase noise is the only degradation. These tolerances shrink as $`1/K`$. If an independent symmetric port flip occurs with probability $`e`$ and a block tag is misassigned by a symmetric integer shift $`R`$, multiply the corrected click coherence by $`(1-2e)\mathbb E\cos(2\pi R/K)`$. Comparing with the ideal matched timing score then gives a sufficient condition against a timing detector with its own tag errors. For a centered time tag and independent jitter $`J`$ the shift in this idealized clock model is the rounded ratio of $`J`$ to the block spacing.

The analysis assumes stable calibrations and uniform block weights, and counts the missed clicks. It gives tolerances for the discrete receiver. The continuous packet's $`K^{-3}`$ near-threshold result has a different preparation and detector model. Dark counts, nonstationary loss and finite-memory qubit errors require their own analysis.
