# Frontier 55 — correction audit: the full Jacobi theta measure is not finite

## Critical correction
The previous version incorrectly used the full Jacobi theta
\[\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}\]
inside the positive coefficient measure on \([1,\infty)\). Because the zero mode is present, \(\theta(t)\to1\) as \(t\to\infty\), and therefore
\[
\int_1^\infty t^{-3/4}\theta(t)\,dt=\infty.
\]
So the claimed finite positive modular measure and the resulting even density were invalid.

## Correct coefficient measure
The coefficient representation uses the nonzero theta tail
\[
\theta_+(t)=\sum_{k\ge1}e^{-\pi k^2t}=\frac{\theta(t)-1}{2}.
\]
Thus
\[
d\nu_+(t)=t^{-3/4}\theta_+(t)\,dt
\]
is finite on \([1,\infty)\).

## Why the naive modular symmetry fails
Under inversion,
\[
\theta_+(1/t)=\frac12\bigl(t^{1/2}\theta(t)-1\bigr),
\]
so \(d\nu_+\) is not invariant under inversion. In logarithmic coordinates
\[
\rho_+(x)=e^{x/4}\theta_+(e^x),\qquad x\ge0,
\]
and modularity introduces an explicit zero-mode correction; therefore \(\rho_+(-x)=\rho_+(x)\) is false.

## Consequence
The earlier modular-even reduction, and any subsequent argument that depends essentially on it, cannot be treated as established. The positive Stieltjes representation must instead be rebuilt directly from the nonzero theta tail, or through a corrected modular completion that explicitly isolates the zero mode.

## Research target
Find an exact finite modular completion in which the zero-mode contribution is isolated as an elementary term. Only after that correction may a whole-line Gram/operator argument be used.

## Status
**Corrected/invalidated:** the earlier full-theta finite-measure symmetry claim.
**Open:** corrected modular completion and the Turan closure.