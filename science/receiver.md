# Building the receiver

Within a window the relevant photon space is the span of the two conditional waveforms. If $`z_b=\sum_j q_{bj}w_j`$, send the two input modes through the linear isometry specified on those waveforms by

```math
u_b\longmapsto\sum_j\sqrt{q_{bj}}\,|j\rangle,\qquad
v_b\longmapsto\sum_j\sqrt{q_{bj}}\,w_j|j\rangle .
```

The map preserves both norms and their inner product. Orthogonal-mode detection implements the desired POVM. The active phase labels can be chosen with at most three nonzero weights in a block, by planar Carathéodory. A two-port receiver suffices when the target overlap is on a chord between two labels. A third port can use a vacuum input. A continuous waveform requires a calibrated waveform sorter to map the two-dimensional span to paths.

## A discrete two-port implementation

For even $`K`$, use two disjoint copies of the same pulse shape, early $`E_b`$ and late $`L_b`$, in each of $`K`$ equally likely blocks. Let $`\theta_b=2\pi b/K`$ and $`0<\eta<\pi/K`$. Prepare the relative branch waveforms

```math
u_b=\frac{E_b+L_b}{\sqrt{2}},\qquad
v_b=e^{i\theta_b}\frac{e^{-i\eta}E_b+e^{i\eta}L_b}{\sqrt{2}}.
```

Use the orthonormal modes $`b_0=(E_b+L_b)/\sqrt{2}`$ and $`b_1=i(L_b-E_b)/\sqrt{2}`$. Detect in this two-port basis:

```math
m_+=\cos(\eta/2)b_0+\sin(\eta/2)b_1,\qquad
m_-=\sin(\eta/2)b_0-\cos(\eta/2)b_1 .
```

The ratio of the conditional amplitudes at the two ports is $`+e^{i\theta_b}`$ and $`-e^{i\theta_b}`$, respectively. Each outcome has the same probability on both qubit branches. Assign its label to $`b`$ or $`b+K/2`$ modulo $`K`$. The optical analyzer can be reused unchanged across blocks. The time index is used only in the local label map.

A synchronized switch sends the early mode through a delay and the late mode through a short arm, aligning the pulses at a calibrated two-port interferometer. The path difference matches the early–late separation, which fits within each window. This requires a stable optical delay, two detector ports and local clocking. All output events are accepted in the ideal model. The helper buffers the label until the common delivery slot, while the qubit holder keeps its state coherent. The same optical switches and ports can be reused across windows. [Active time-bin readout precedents](../references/RELATED_WORK.md) establish the component mechanism.

With $`\eta=\pi/(2K)`$, the direct timing detector sees $`2K`$ equally spaced relative phases. It needs $`2K`$ labels to reach exact recovery. Under the same $`K`$-label budget and lossless optics its optimal coherence is $`\cos\eta`$. This finite source uses engineered time bins. The [uniform continuous](approximate.md) model gives the distinct near-threshold law.
