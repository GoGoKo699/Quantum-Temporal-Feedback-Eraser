# Related work

| Source | What it supplies and how the task differs |
| --- | --- |
| [Gregoratti and Werner, 2004](https://doi.org/10.1063/1.1758320), §§III–IV | Perfect environment-assisted correction through random-unitary conditional maps, and optimization of corrections for a specified measured instrument. Here the temporal access and the common dictionary constrain the choice of that instrument. |
| [Buscemi, Chiribella and D’Ariano, 2005](https://doi.org/10.1103/PhysRevLett.95.090501), Theorem 2 and entropy bound | A qubit dephasing map with complete access to its pure environment has an optimal random-unitary decomposition with two outcomes and minimum feedback entropy equal to entropy exchange. Our fixed-window observer may need a number of labels that grows with the number of windows, even for the same qubit channel. |
| [Buscemi, 2007](https://doi.org/10.1103/PhysRevLett.99.180501) | Connects erasure of environment information with corrected entanglement fidelity. The shared phase alphabet under restricted temporal access is the optimization here. |
| [Zhao et al., 2014](https://doi.org/10.1103/PhysRevLett.112.103602), Eq. (2) and feedforward apparatus | Uses a time difference to drive phase correction in entanglement swapping with mismatched photons. The arrival-time benchmark here optimizes that information interface at a fixed message alphabet. |
| [Fognini et al., 2018](https://doi.org/10.1364/OE.26.024487) | Compensates fine-structure splitting using access to the polarization rails of the output. Our receiver observes a single rail containing two overlapping temporal modes, with no separate branch tag. |
| [Aqua and Dayan, arXiv:2404.01516v4](https://arxiv.org/abs/2404.01516v4), §§II–V | A temporal eraser heralds two-photon exchange symmetry for linear-optical fusion. The present task is deterministic correction of an unknown qubit through one emitted photon. |
| [Antesberger et al., 2024](https://doi.org/10.1103/PRXQuantum.5.010325), Fig. 3 | Uses synchronized switching to align early and late time bins and detects both output ports. The project uses this optical primitive and supplies the measurement and feedback choice. |
| [Serino et al., 2025](https://doi.org/10.1364/OE.544206) | Demonstrates programmable temporal-mode sorting. The continuous-waveform proofs assume the ideal mode measurement on a known two-dimensional input span. |

The main mathematical result is the common phase-alphabet tradeoff, including matched finite-error bounds and an explicit reduction in span when measurements can overlap. The optical robustness calculation compares a finite two-bin realization with optimal same-budget timing detection under a specified attenuation model.
