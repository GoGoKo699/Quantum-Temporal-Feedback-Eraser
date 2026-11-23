# Model and resources

Let $`S`$ be an unknown qubit, with an arbitrary reference allowed. The emitter supplies the isometry

```math
V|0\rangle=|0\rangle|u\rangle,\qquad
V|1\rangle=|1\rangle|v\rangle,\qquad
v(t)=e^{i\phi(t)}u(t),\qquad
\int_0^T|u(t)|^2dt=1.
```

The photon occupies one accessible rail. Its two conditional intensity profiles are equal. The waveforms and phase calibration are known. The qubit holder can wait for the message and apply local quantum operations. The optical helper has no access to the qubit or to an additional branch flag.

In the segmented receiver the optical Hilbert space is the orthogonal sum over predetermined contiguous windows $`I_b`$. Each effect is block diagonal across windows. Within a window an arbitrary POVM is allowed. For positive block weight $`p_b=\int_{I_b}|u|^2`$, write $`u_b=P_bu/\sqrt{p_b}`$ and similarly for $`v_b`$. The normalized overlap is

```math
z_b=\langle u_b,v_b\rangle
=\frac{1}{p_b}\int_{I_b}|u(t)|^2e^{i\phi(t)}dt.
```

The helper emits one classical symbol from a common alphabet of size $`M`$ at a fixed delivery slot. It can use its own clock and keep the block index internally. The qubit holder receives the symbol alone. All trials count and any loss is handled explicitly. One can take the receiver's local measurements as independent of prior runs. Shared randomness gives a mixture of fixed single-run designs and cannot improve the optimum.

## Reduction to complex overlaps

For an effect on window $`b`$ and label $`j`$, define $`c_{bj}=\langle u_b,E_{bj}v_b\rangle`$. The allowable values are precisely

```math
\sum_jc_{bj}=z_b,\qquad
\sum_j|c_{bj}|\le1.
```

Positivity and Cauchy–Schwarz give the bound after summing the two diagonal squares. Conversely choose real $`q_{bj}\ge|c_{bj}|`$ summing to one. The compressed Gram matrices with diagonals $`q_{bj}`$ and off-diagonal $`c_{bj}`$ are positive and sum to the Gram matrix of the pair. Pull these matrices back through the map with columns $`u_b,v_b`$, using its inverse on the support of the Gram matrix, to obtain positive effects summing to the identity on the span. Complete the effects arbitrarily on the unused orthogonal modes. This also works for a dependent pair by restriction to that support.

The aggregate map for label $`j`$ is a Schur subchannel. Write its two unnormalized diagonal weights as $`a_j,b_j`$ and the corresponding off-diagonal weight as $`c_j=\sum_b p_b c_{bj}`$, in the convention where it multiplies the lower-left coherence. For any trace-preserving correction with Kraus operators $`L_\ell`$, its contribution to entanglement fidelity is bounded by

```math
\frac{1}{4}\sum_\ell
\left(a_j|(L_\ell)_{00}|^2+b_j|(L_\ell)_{11}|^2+
2\Re\!\left[c_j(L_\ell)_{11}\overline{(L_\ell)_{00}}\right]\right)
\le\frac{a_j+b_j+2|c_j|}{4}.
```

Trace preservation bounds the two sums of squares by one, and Cauchy–Schwarz bounds their cross term. A phase correction attains the bound. With phases optimized, the output is a mixture of identity and Pauli $`Z`$ with residual coherence $`C\in[0,1]`$. Thus the optimal half-diamond distance is $`\varepsilon=(1-C)/2`$. This also minimizes entanglement infidelity. The Bell-state test bounds half-diamond distance below by entanglement infidelity even for a general correction. For fixed correction phases, the score in [approximate recovery](approximate.md) gives optimal entanglement fidelity; its residual coherence can have an imaginary part.

## Resource boundaries

The temporal window, number of labels, storage of the qubit through the delivery slot and optical coherence are separate resources. The optical analyzer may use synchronized switching, path delays and extra vacuum ports inside an allowed window. If photon time tags arrive at the qubit, the same physical feedback link can carry additional block information. That is a different message model. The [overlap extension](overlapping.md) specifies an interval-support rule in place of a disjoint partition.
