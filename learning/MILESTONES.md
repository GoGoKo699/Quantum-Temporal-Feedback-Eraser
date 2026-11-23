# Project understanding map

The 30 milestones trace how a photon receiver reverses qubit dephasing when it can interfere times within disjoint windows and send a single fixed-slot correction label. The first 11 milestones build the emission, readout, and recovery model. The remaining 19 connect the receiver construction to the exact and approximate label costs, the arrival-time benchmark, and the boundaries of the partition assumption. The [Watrous bridge](WATROUS_BRIDGE.md) provides the focused readings and a worked four-window example.

| Phase | Milestones | Connection established |
|---|---|---|
| Background and preliminaries | [M01](#m01-an-unknown-qubit-and-its-reference)–[M04](#m04-dephasing-from-the-photon-overlap) | The joint state, conditional waveforms, and loss of qubit coherence |
| Background and preliminaries | [M05](#m05-coherence-windows-and-block-overlaps)–[M08](#m08-the-picture-in-the-complex-plane) | Block measurements, conditional maps, and the shared phase set |
| Background and preliminaries | [M09](#m09-local-detector-outputs-and-shared-messages)–[M11](#m11-the-operational-recovery-question) | Resource accounting, error, and the full operational question |
| Narrative and innovation | [M12](#m12-the-granularity-of-a-block-measurement)–[M18](#m18-an-exact-receiver-from-a-polygon) | Measurement feasibility, decoder optimality, and the exact threshold |
| Narrative and innovation | [M19](#m19-two-pulses-and-a-two-port-receiver)–[M22](#m22-the-best-score-for-a-fixed-phase-set) | Receiver implementation, feedback entropy, and approximation in one window |
| Narrative and innovation | [M23](#m23-the-cost-of-merging-neighboring-centers)–[M26](#m26-the-gap-between-the-two-readout-models) | Matching label-deficit bounds and the arrival-time comparison |
| Narrative and innovation | [M27](#m27-loss-and-an-inaccessible-photon)–[M30](#m30-the-complete-receiver-tradeoff) | Imperfections, model boundaries, and the complete resource account |

## Phase I. Background and preliminaries

### M01 An unknown qubit and its reference

**Central question.** What must reach the end of a successful recovery?

**Understanding target.** Explain why success means applying the identity channel to the unknown qubit, even when the input is half of an entangled pair. Compare preserving populations, preserving a particular pure state, and preserving an arbitrary joint input with an untouched reference.

**Dependencies and story role.** Start with the object the experiment is supposed to protect.

**Conceptual connection.** The reference is outside the receiver's control and exposes lost correlations that tests on computational-basis inputs would miss.

**Sources.** [Watrous §§2.1.2–2.1.3 and 3.3.1](WATROUS_BRIDGE.md#targeted-reading) · [Model](../science/model.md)

### M02 Equal intensity and different phase

**Central question.** How can two photons arrive with the same time statistics and still carry different quantum states?

**Understanding target.** Describe the two normalized conditional photon waveforms and their shared intensity. Interpret their relative temporal phase as information that can be accessed by interfering portions of the photon.

**Dependencies and story role.** M01. Identify the receiver's only quantum input.

**Conceptual connection.** An arrival detector sees the same probability density in both branches, while an interferometer can respond to relative phases across times.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

### M03 The emission isometry

**Central question.** Where does the original qubit amplitude go during emission?

**Understanding target.** Extend the two computational-basis emission rules to an arbitrary qubit and reference by linearity. Explain how the orthogonal qubit basis states make the joint map an isometry even when the conditional photon states overlap.

**Dependencies and story role.** M01–M02. Join the protected state to the two conditional photon states.

**Conceptual connection.** The process can be reversible on the joint system even when the qubit by itself has dephased.

**Sources.** [Watrous §§2.2.2–2.2.3](WATROUS_BRIDGE.md#targeted-reading) · [Model](../science/model.md)

### M04 Dephasing from the photon overlap

**Central question.** What does the qubit holder see when the photon is ignored?

**Understanding target.** Trace the photon out of the emitted joint state and identify the overlap multiplying the off-diagonal qubit entry. Distinguish a reduction in coherence magnitude from a known phase that a qubit unitary can undo.

**Dependencies and story role.** M03. Translate the emission model into an observable effect on the qubit.

**Conceptual connection.** A full phase winding with uniform intensity can leave zero coherence despite equal basis populations and equal photon arrival distributions.

**Sources.** [Watrous §2.1.3](WATROUS_BRIDGE.md#targeted-reading) · [Model](../science/model.md)

### M05 Coherence windows and block overlaps

**Central question.** What information about the photon survives restricting interference to one time window at a time?

**Understanding target.** Define the disjoint temporal blocks, their shared branch weights, and the overlap of the normalized conditional waveforms in each block. Explain why the effects are block diagonal and the overall overlap is a weighted sum of block overlaps.

**Dependencies and story role.** M02–M04. Specify the physical restriction on the receiver.

**Conceptual connection.** The restriction admits arbitrary interference within a block. It gives the helper no coherence between separate blocks and gives the holder no block record.

**Sources.** [Model](../science/model.md) · [Overlapping windows](../science/overlapping.md)

### M06 An effect and its conditional qubit map

**Central question.** How can measuring the photon change the qubit without touching it?

**Understanding target.** Use the two diagonal photon matrix elements of an effect to describe the branch weights and the cross matrix element to describe surviving coherence. Interpret the resulting map as subnormalized when the label is fixed.

**Dependencies and story role.** M03, M05. Link receiver outcomes to qubit dynamics.

**Conceptual connection.** An outcome with unequal branch weights has acquired some basis information. An outcome with equal weights can still reduce coherence if its cross element has smaller magnitude.

**Sources.** [Watrous §§2.2.2 and 2.3.1](WATROUS_BRIDGE.md#targeted-reading) · [Model](../science/model.md)

### M07 Phase correction and label reuse

**Central question.** When can two different internal receiver outcomes use the same public label?

**Understanding target.** Track how a phase unitary acts on the off-diagonal entry. For branches with equal weights and a known relative phase, explain why the inverse phase recovers the qubit and why branches with the same required phase can share a label.

**Dependencies and story role.** M06. Identify which feature of the internal outcome the qubit holder needs.

**Conceptual connection.** Changing the receiver measurement by window is allowed. The holder uses the same correction each time a public label is received.

**Sources.** [Model](../science/model.md) · [Exact phase dictionary](../science/exact.md)

### M08 The picture in the complex plane

**Central question.** Why does a convex combination of unit phases describe a dephasing process?

**Understanding target.** Represent a known phase by a point on the unit circle and a weighted sum of phases by a point in the unit disk. Relate the magnitude of that sum to coherence and the mixture weights to branch probabilities.

**Dependencies and story role.** M04, M07. Build the geometry used to choose one label set for all windows.

**Conceptual connection.** A composition changes the phase factors by multiplication. Ignoring a classical choice between phases averages them instead.

**Sources.** [Model](../science/model.md) · [Exact phase dictionary](../science/exact.md)

### M09 Local detector outputs and shared messages

**Central question.** What does the holder learn from one receiver outcome?

**Understanding target.** Distinguish detector port, local block index, public label, delivery time, and the phase applied on the qubit. Explain why the helper can know the block while the holder receives one fixed-time alphabet symbol.

**Dependencies and story role.** M05, M07–M08. Join physical receiver resources to the communication constraint.

**Conceptual connection.** Delivering notifications at different times could implicitly give the holder an additional outcome. A buffer can keep delivery time fixed while allowing window-dependent processing in the receiver.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

### M10 Fidelity and worst-case recovery error

**Central question.** How can we test recovery for an unknown qubit?

**Understanding target.** Distinguish Bell-state fidelity on the channel's Choi input from half-diamond error optimized over inputs and references. Explain how the Bell-state projection gives a lower bound on half-diamond error from a target identity channel.

**Dependencies and story role.** M01, M04, M06. Fix the performance criteria before optimizing the receiver.

**Conceptual connection.** The two criteria agree for the real qubit dephasing channel used by an optimal protocol, as the narrative phase will establish.

**Sources.** [Watrous §§3.2.1 and 3.3.1–3.3.3](WATROUS_BRIDGE.md#targeted-reading) · [Approximate recovery](../science/approximate.md)

### M11 The operational recovery question

**Central question.** What is held fixed when two receiver designs are compared?

**Understanding target.** State the task from emission through correction, including unknown input, calibrated waveforms, disjoint coherence blocks, any permitted local receiver POVM, a shared label alphabet, fixed delivery time, and a correction on every run.

**Dependencies and story role.** M01–M10. Combine the physical setup, measurement access, communication resource, and error criterion.

**Conceptual connection.** Compare changing optical coherence time, adding a message symbol, adding arrival-time resolution, and extending qubit storage. These operations relax different constraints.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

## Phase II. Narrative and innovation

### M12 The granularity of a block measurement

**Central question.** Which degrees of freedom in a continuous block can affect recovery?

**Understanding target.** Compress the effect to the span of the two conditional waveforms. Relate the positivity of each two-state Gram matrix to the Cauchy–Schwarz constraint on its cross element, and relate POVM completeness to the sum of the matrices.

**Dependencies and story role.** M05–M06, M11. Replace a continuous optical optimization by finite variables without changing its allowed measurements.

**Conceptual connection.** Two waveforms per block yield at most a two-dimensional compression even if each waveform has an infinite description.

**Sources.** [Model](../science/model.md) · [Exact phase dictionary](../science/exact.md)

### M13 Realizing Gram data as a measurement

**Central question.** Which proposed cross elements can a receiver implement?

**Understanding target.** Explain how to augment a list of cross elements with equal diagonal weights so that each compressed effect is positive and the matrices sum to the input Gram matrix. For rank-one pieces, reconstruct two output amplitude vectors with that same Gram matrix.

**Dependencies and story role.** M08, M12. Establish the measurement construction needed by the exact and approximate protocols.

**Conceptual connection.** An arbitrary feasible decomposition in the finite geometry induces a physical receiver action on the occupied input span in the ideal model.

**Sources.** [Watrous §2.3.2](WATROUS_BRIDGE.md#targeted-reading) · [Model](../science/model.md) · [Receiver](../science/receiver.md)

### M14 Why qubit phase decoding suffices

**Central question.** Could a general qubit channel outperform phase feedback?

**Understanding target.** Understand the bound from a conditional map's diagonal Kraus coefficients and Cauchy–Schwarz. Explain why a phase unitary attains the optimal Bell-state contribution and how grouping outputs under one public label constrains that contribution.

**Dependencies and story role.** M06–M07, M10, M12. Reduce the decoder part of the optimization without assuming its answer.

**Conceptual connection.** The holder can use any permitted trace-preserving qubit map. A bound against that whole class is needed even if the proposed implementation is only a phase gate.

**Sources.** [Watrous §2.2.2](WATROUS_BRIDGE.md#targeted-reading) · [Decoder bound](../science/model.md)

### M15 When the Bell error is the channel error

**Central question.** When does the Bell-state lower bound already give the worst-case error?

**Understanding target.** Recognize a real, nonnegative residual-coherence factor as a mixture of the identity and a $`Z`$ operation. Use the Bell state to distinguish those branches and identify the half-diamond error with the $`Z`$-branch probability.

**Dependencies and story role.** M10, M14. Connect the scalar recovery score to the operational metric.

**Conceptual connection.** Optimization can align the net coherence phase. A formula for fixed phase labels generally states an entanglement-fidelity score without that optimization.

**Sources.** [Watrous §§3.3.2–3.3.3](WATROUS_BRIDGE.md#targeted-reading) · [Approximate recovery](../science/approximate.md)

### M16 The shared polygon for exact recovery

**Central question.** When does one set of correction phases recover every block exactly?

**Understanding target.** Explain why exact correction requires each block overlap to be a convex combination of the same label phases. Trace sufficiency to the Gram construction and necessity to equality in the bound on total recoverable coherence.

**Dependencies and story role.** M08, M12–M15. Formulate the exact recovery condition as a simultaneous geometric problem.

**Conceptual connection.** A separate two-phase set for every block can be easy to find. Requiring a shared set is what couples the individual block measurements.

**Sources.** [Exact phase dictionary](../science/exact.md) · [Watrous bridge example](WATROUS_BRIDGE.md#follow-a-complete-four-window-example)

### M17 One label in every phase arc

**Central question.** Why does a strict phase winding force the number of labels to grow with the number of windows?

**Understanding target.** Compare a block's averaged overlap with the supporting chord of its phase arc. Show that an overlap beyond that chord cannot be in a polygon whose vertices all avoid the open arc.

**Dependencies and story role.** M05, M08, M16. Derive the exact lower bound from the arrangement of disjoint arcs.

**Conceptual connection.** A shared phase at a touching endpoint cannot satisfy the strict interior condition for either adjacent arc. The one-window case uses the separate fact that a nontrivial overlap lies inside the circle.

**Sources.** [Exact lower bound](../science/exact.md)

### M18 An exact receiver from a polygon

**Central question.** How can the receiver reach the label lower bound for nonuniform blocks?

**Understanding target.** Describe the construction that draws rays from an interior center through the block overlaps and extends them to the unit circle. Explain why the center lies in the hull of the extended phases, why each overlap then lies in that hull, and how each block uses at most three such phases.

**Dependencies and story role.** M13, M16–M17. Turn the geometric threshold into a receiver for a prescribed partition.

**Conceptual connection.** Symmetric overlaps can use two ports by choosing opposite phases. The general construction handles unequal weights and unequal block widths within the stated winding assumptions.

**Sources.** [Exact upper bound](../science/exact.md) · [Receiver](../science/receiver.md)

### M19 Two pulses and a two-port receiver

**Central question.** How can a physical device interfere two different arrival slots?

**Understanding target.** Follow an early and late wavepacket through the switch and delay into aligned paths, then through a two-port mixing unitary. Relate the branch amplitude ratios at the ports to the two phase labels and the inverse corrections.

**Dependencies and story role.** M03, M09, M13, M18. Read the optical embodiment as a realization of the Gram construction.

**Conceptual connection.** The engineered two-pulse source is an explicit finite receiver model. A general continuous waveform requires the mode transformation that matches its own pair of conditional modes.

**Sources.** [Receiver](../science/receiver.md)

### M20 The uniform packet and its evenly spaced centers

**Central question.** Which part of the uniform model determines the cost of a missing label?

**Understanding target.** Derive the radius $`\mathrm{sinc}(\pi/K)`$ and equally spaced center phases from averaging a linear phase over equal blocks. Relate the radial deficit to the angular distance $`O(1/K)`$ at which a unit-circle correction label becomes too far away to cover the overlap.

**Dependencies and story role.** M05, M17. Extract the geometry used for the quantitative deficit law.

**Conceptual connection.** The exact threshold relies on disjoint arcs. This quantitative argument uses the stronger uniform-packet and equal-partition assumptions.

**Sources.** [Exact model](../science/exact.md) · [Uniform approximate regime](../science/approximate.md)

### M21 Message entropy for exact feedback

**Central question.** Could a large label alphabet still convey only a constant amount of information on a typical run?

**Understanding target.** Distinguish the number of available labels from the Shannon entropy of the emitted label. For an exact receiver and a uniform winding, use distances between the received phase and the true block center to understand why the block index can be inferred with only a bounded conditional uncertainty.

**Dependencies and story role.** M08–M09, M16–M18, M20. Test whether unequal use of labels can substantially reduce the message cost of exact recovery.

**Conceptual connection.** Recovering the block approximately from its correction adds up to a growing message entropy under segmentation. With complete coherence across the same uniform packet, exact correction can use one bit.

**Sources.** [Watrous §§5.1.1–5.1.2](WATROUS_BRIDGE.md#targeted-reading) · [Uniform packet and entropy](../science/exact.md#uniform-packet-and-message-entropy)

### M22 The best score for a fixed phase set

**Central question.** When an overlap lies beyond one edge of the phase polygon, what controls its best recovery score?

**Understanding target.** Identify the violated supporting chord, the outward direction, and the normal coordinate of the overlap. Follow how the chord gives a bound on the recoverable coherence and how two outcomes can reach that bound.

**Dependencies and story role.** M13–M16, M20. Replace a global approximate optimization by a local geometric score for each block.

**Conceptual connection.** The chord can determine the best score while the tangential coordinate still determines the mixture of the two outcomes that realizes it.

**Sources.** [Fixed-label optimization](../science/approximate.md)

### M23 The cost of merging neighboring centers

**Central question.** How can a receiver save several labels while preserving the other blocks exactly?

**Understanding target.** Follow the construction that merges disjoint neighboring pairs to phase midpoints and retains every unmerged center. Explain why the polygon still covers the unmerged blocks and why the angular displacements yield block error of order $`K^{-2}`$ on only order $`K-M`$ blocks.

**Dependencies and story role.** M16, M20, M22. Construct the near-threshold error upper bound.

**Conceptual connection.** Each block in the uniform model has weight $`1/K`$. Multiplying angular error squared by that weight explains the order $`K^{-3}`$ contribution per missing label.

**Sources.** [Near-threshold upper bound](../science/approximate.md)

### M24 Why the missing-label cost is unavoidable

**Central question.** Why can a different placement of the available labels fail to improve the near-threshold order?

**Understanding target.** Explain why at least $`K-M`$ block centers lack a sufficiently close label. Apply the chord-direction bound to show that each such block incurs order $`K^{-2}`$ local error despite optimized coherent readout.

**Dependencies and story role.** M20, M22–M23. Match the construction with a lower bound over the whole permitted receiver class.

**Conceptual connection.** At the threshold the error vanishes exactly. Losing a fixed number of labels below it therefore has different behavior from using a fixed fraction as many labels.

**Sources.** [Near-threshold lower bound](../science/approximate.md)

### M25 The best arrival-time encoder

**Central question.** What can a detector achieve if it records exact arrival time and then compresses that record?

**Understanding target.** Explain why choosing a closest available correction phase is pointwise optimal for a fixed phase set. Average the resulting cosine over the full uniform phase winding and explain why equally spaced phases maximize that average.

**Dependencies and story role.** M09, M15, M20. Build a baseline with optimal classical postprocessing and ideal time resolution.

**Conceptual connection.** The receiver learns time and can choose any allowed label from it. Measuring time discards the within-window coherence used by the optical construction.

**Sources.** [Arrival-time comparison](../science/approximate.md)

### M26 The gap between the two readout models

**Central question.** At equal feedback alphabet size, when does temporal interference change the achievable error?

**Understanding target.** Compare exact recovery at $`M=K`$, the near-threshold coherent law $`\Theta((K-M)/K^3)`$, and the arrival-only error $`(1-\mathrm{sinc}(\pi/M))/2`$. Explain what the limit $`M=K-1`$ reveals about the error orders of the two designs.

**Dependencies and story role.** M23–M25. Tie the mathematical resource law to a matched operational benchmark.

**Conceptual connection.** The comparison holds the common message resource fixed while varying the accessible optical measurement. The arrival detector has unlimited timing resolution in this benchmark.

**Sources.** [Approximate recovery and baseline](../science/approximate.md) · [Exact threshold](../science/exact.md)

### M27 Loss and an inaccessible photon

**Central question.** How does the comparison change when the photon receiver sometimes gets no click?

**Understanding target.** Separate the accessible photon event from an inaccessible environmental branch and specify which event is observed by each party. Explain why every event, including a no-click event, must be counted in the full corrected channel and its half-diamond error.

**Dependencies and story role.** M04, M09–M11, M26. Reintroduce a physical limitation excluded from the exact threshold.

**Conceptual connection.** Renormalizing a click-only dataset answers a heralded task. The deterministic model also needs a defined correction and communication rule on no-click runs.

**Sources.** [Robustness](../science/robustness.md) · [Model](../science/model.md)

### M28 Timing and mode-matching errors

**Central question.** What physical mismatch may overwhelm the gain from saving one label?

**Understanding target.** Explain how unequal transmission of the early and late pulses and their imperfect overlap limit coherent recovery. Compare the residual coherence of the coherent and arrival-only receivers under matched loss, including their common fallback.

**Dependencies and story role.** M19, M24, M26–M27. Connect small theoretical errors to operating requirements on a specific receiver.

**Conceptual connection.** The two-pulse implementation turns visibility into a quantitative comparison. Visibility lost to which-time information can remove the advantage of coherent readout.

**Sources.** [Receiver](../science/receiver.md) · [Robustness](../science/robustness.md)

### M29 Where the partition proof stops applying

**Central question.** How can overlapping coherence windows change the exact label requirement?

**Understanding target.** Explain why overlap removes the common block compression and how pairing separated, phase-weighted slices can still implement a shared two-label receiver. Compare the explicit span $`5T/12`$ example with the minimum span of a two-window partition for the same packet.

**Dependencies and story role.** M05, M11–M12, M16–M18. Mark the exact assumption separating the established partition law from broader receiver models.

**Conceptual connection.** Window overlap can improve the constant in the exact label count. Under the interval-support rule, the order $`\Theta(T/\tau)`$ for small allowed span $`\tau`$ still follows from locality.

**Sources.** [Overlapping windows](../science/overlapping.md) · [Exact phase dictionary](../science/exact.md)

### M30 The complete receiver tradeoff

**Central question.** Which resources let one recover the qubit and which determine the remaining error?

**Understanding target.** Tell the scientific story from photon-induced dephasing through block coherence, Gram realization, shared phases, exact and approximate bounds, and the timing benchmark. Specify which results use strict winding, uniformity, ideal optical access, or the particular discrete embodiment.

**Dependencies and story role.** M11, M18–M21, M24, M26–M29. Combine the theorem, constructive receiver, and scope in one operational account.

**Conceptual connection.** A chosen receiver sets local coherence access and outcome possibilities. The holder's shared alphabet and fixed delivery slot set the feedback resource. Keeping both visible explains the performance gap and the limits of transferring it to a different design.

**Sources.** [Model](../science/model.md) · [Exact threshold](../science/exact.md) · [Approximate recovery](../science/approximate.md) · [Receiver](../science/receiver.md) · [Robustness](../science/robustness.md) · [Overlapping windows](../science/overlapping.md)
