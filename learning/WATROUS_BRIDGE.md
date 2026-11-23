# From Watrous to temporal feedback erasure

A qubit can lose its coherence when it emits a photon. Suppose the photon has the same arrival-time distribution for both qubit basis states, but its phase depends on which state emitted it. A receiver can measure the photon and send a correction label to the qubit holder. The question is how many labels suffice when the receiver can interfere times within each of several disjoint windows and sends just one message at a fixed time.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Section numbers refer to the author's 2018 prepublication manuscript. [Published book](https://doi.org/10.1017/9781316848142) · [Author's manuscript and contents](https://cs.uwaterloo.ca/~watrous/TQI/)

## Targeted reading

| Project use | Watrous sections | What to bring into the project |
|---|---|---|
| Qubit, photon, and reference (M01–M04) | [§§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Pure states, joint registers, and partial trace. |
| Emission and correction (M03–M10, M14–M16) | [§§2.2.1–2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Completely positive maps, isometries, and Kraus representations. |
| Receiver effects and their realization (M05–M08, M13, M18–M19) | [§§2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Measurement effects, classical outcomes, and Naimark dilation (Theorem 2.42). |
| Bell-state and worst-case channel error (M10, M14–M15, M27) | [§§3.2.1, 3.3.1–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Pure-target fidelity, the role of a reference, and the completely bounded trace norm. |
| Entropy of the phase label (M21) | [§§5.1.1–5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Shannon entropy, conditional entropy, and nonnegative relative entropy. |

Watrous develops these notions for finite registers. For a fixed temporal partition, the receiver only needs the span of two conditional photon vectors in each block. That is finite-dimensional even when the photon is described by a continuous waveform. The proof reduces the measurement on that span to an overlap problem. The receiver sets and resource comparisons belong to the [project model](../science/model.md) and [exact proof](../science/exact.md).

## Translate the notation

| Object | Role in this project |
|---|---|
| System $`S`$, photon $`P`$, reference $`R`$ | $`S`$ is the unknown input, $`P`$ is accessible to the helper, and $`R`$ can be entangled with $`S`$ and remains untouched. |
| Emission isometry $`V`$ | $`V\lvert0\rangle=\lvert0\rangle\lvert u\rangle`$ and $`V\lvert1\rangle=\lvert1\rangle\lvert v\rangle`$. Discarding $`P`$ leaves a dephasing channel on $`S`$. |
| Block $`b`$, weight $`p_b`$, overlap $`z_b`$ | $`p_b`$ is the probability weight of the time window in either branch. $`z_b=\langle u_b\vert v_b\rangle`$ uses the normalized branch waveforms inside the window. |
| Effect $`E_{bj}`$, correction phase $`w_j`$ | $`E_{bj}`$ is the receiver's positive operator for public label $`j`$ inside block $`b`$. The holder applies the inverse of $`w_j`$ as a phase on $`\lvert1\rangle`$ whenever label $`j`$ is received. |
| Entanglement fidelity and half-diamond error | The first uses the overlap with a Bell state after applying the channel to one half. The second is half the completely bounded trace norm of the channel difference. The project proves equality between the optimized infidelity and optimized half-diamond error in its ideal model. |

## Follow a complete four-window example

Take a uniform photon packet whose phase completes one turn across four equal windows. Rotate the phase origin so that the window-center phases are $`1,i,-1,-i`$. Their normalized overlaps are $`r,ir,-r,-ir`$, where $`r=\sin(\pi/4)/(\pi/4)`$ is the average of a unit phase over one window after removing the center phase. The four center phases serve as the shared label set. [Exact construction](../science/exact.md)

Within the window with overlap $`z_b=r w_b`$, use labels with phases $`w_b`$ and $`-w_b`$ at weights $`q_+=(1+r)/2`$ and $`q_-=(1-r)/2`$. A possible output amplitude vector for the photon from qubit state $`\lvert0\rangle`$ is $`(\sqrt{q_+},\sqrt{q_-})`$. The corresponding vector for $`\lvert1\rangle`$ is $`(w_b\sqrt{q_+},-w_b\sqrt{q_-})`$. The vectors both have unit norm and their inner product is $`r w_b=z_b`$. Matching the inner product and norms makes the map from the two input waveforms an isometry on their span. Reading the output port therefore implements a photon measurement. [Measurement and realization](../science/receiver.md)

In either port the qubit amplitudes pick up equal moduli, and the amplitude on $`\lvert1\rangle`$ acquires the port's label phase. The holder applies its inverse. Every port and window then gives back the input qubit, including its correlations with $`R`$. The helper can use the window locally to name the port's phase and deliver that label at the common time. The receiver has two local outputs for this construction and four different messages across the packet. [Model](../science/model.md) · [Receiver](../science/receiver.md)

This example uses two labels **within** a window. Fewer than four labels **across** the packet cannot reach exact recovery because each open quarter-turn arc must contain a distinct label phase. Ideal arrival-time detection followed by optimal four-label encoding has error $`(1-r)/2>0`$. The latter detector resolves arrival time fully and still lacks interference between times within a window. [Exact lower bound](../science/exact.md) · [Arrival-time comparison](../science/approximate.md)

## Where the project begins

- The conditional qubit maps are determined by the two photon-state matrix elements of each effect, and these matrices can be realized whenever they are positive and sum to the input pair's Gram matrix. Turning that condition into a simultaneous convex hull for every window is the project's step. [Measurement model](../science/model.md) · [Exact phase dictionary](../science/exact.md)
- A Bell-state test bounds every permitted decoder. A phase decoder attains the optimized bound and leaves a real residual coherence, so the error can be understood as the probability of a $`Z`$ error. The deficit when fewer labels are available is governed by how many block overlaps the shared polygon misses and by how far it misses them. [Approximate recovery](../science/approximate.md)
- Access to the complete environment already gives qubit recoherence by classical feedback. Buscemi, Chiribella, and D'Ariano established that result, including the unrestricted qubit classical information cost. The temporal partition, fixed-slot shared label budget, and comparison with arrival-time readout specify this project's question. [Buscemi et al., *Physical Review Letters* 95, 090501 (2005)](https://doi.org/10.1103/PhysRevLett.95.090501)

The [30-milestone map](MILESTONES.md) connects these steps to the receiver implementation and to the effects of [imperfections](../science/robustness.md) and [overlapping windows](../science/overlapping.md).
