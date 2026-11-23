# Quantum Temporal Feedback Eraser

**An optical receiver can restore an unknown qubit by interfering nearby times and sending one phase correction label.** For a photon spanning one full relative-phase winding, a detector with $`K\ge2`$ separate coherent windows needs exactly $`K`$ labels. It can use a two-mode measurement within each window and reuse the same finite set of phase corrections across all windows.

| Detector | What it can achieve |
| --- | --- |
| Disjoint, contiguous windows | Exact recovery with $`M=K`$ labels. For a uniform packet, the optimal error with $`M=K-1`$ is of order $`K^{-3}`$. |
| Ideal arrival-time detection | Optimal error $`\varepsilon_{\mathrm{arr}}(M)=[1-\mathrm{sinc}(\pi/M)]/2`$. At $`M=K-1`$ this is of order $`K^{-2}`$. |
| Overlapping windows of maximum span $`\tau`$ | Exact recovery needs order $`T/\tau`$ labels. Pairing temporal portions across overlapping windows can reduce the required span at a fixed label count. |

The unknown input may be entangled with a reference. The optical helper receives one photon in a single rail, has calibrated local phase control, and sends one message at a fixed time. The ideal guarantees account for every trial. The [optical analysis](science/robustness.md) gives the loss, arm balance, timing and phase conditions for a discrete implementation.

## Read the project

- [Scientific account](science/README.md) leads from the isometry through the recovery theorem, optimal error, receiver and overlap construction.
- [Learning route](learning/README.md) links 30 milestones to one textbook and the corresponding proofs.
- [Closest work](references/RELATED_WORK.md) traces the inherited recovery framework and physical receiver precedents.
- [Verification](verification/README.md) checks the finite receivers and numerical optimizations. From the repository root, run:

```bash
python verification/check_receiver.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
