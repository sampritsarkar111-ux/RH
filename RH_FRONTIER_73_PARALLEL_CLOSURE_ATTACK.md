# Frontier 73 — parallel closure attack

Date: 2026-09-16

## Objective
Attack the remaining RH gap simultaneously through canonical Jensen hyperbolicity, Toeplitz/PF-infinity, self-weighted Hamburger positivity, and de Bruijn–Newman heat flow. No RH-equivalent assertion is admitted as an axiom.

## Common exact target
Let
\[
\xi(1/2+z)=\sum_{n\ge0}\frac{\gamma_n}{n!}z^{2n},\qquad
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
A complete Jensen route requires
\[
\forall d,n\ge0:\quad J_{d,n}\text{ has only real zeros}.
\]
This is an infinite quantifier and cannot be replaced by finite computation.

## Parallel gate A — finite-degree Hermite algebra
For each fixed \((d,n)\), form the Hermite matrix of \(J_{d,n}\). Its positive semidefiniteness is equivalent to real-rootedness of the polynomial (with the standard multiplicity convention). Thus an unconditional proof can be reduced to explicit nonnegative formulae for every principal Hermite minor. The first nontrivial cubic minor reduces exactly to
\[
w^2+4v^3\le0
\]
under the normalized central-moment variables used in the earlier frontiers. Ordinary positive-moment inequalities give the opposite structural tendency, so a generic Stieltjes argument cannot close this gate.

## Parallel gate B — Toeplitz/Jacobi–Trudi
For
\[
F(z)=\xi(1/2+\sqrt z)=\sum_{m\ge0}a_mz^m,
\]
write
\[
\frac1{F(-z)}=\sum_{m\ge0}h_mz^m.
\]
The fixed-shift duality gives
\[
D_{r,k}=\det(h_{r+j-i})_{i,j=0}^{k-1}.
\]
Desnanot–Jacobi gives
\[
D_{r,k}D_{r-2,k}=D_{r-1,k}^2-D_{r-1,k-1}D_{r-1,k+1}.
\]
Therefore a global proof could propagate positivity if a uniform strict curvature inequality were established. No such inequality follows from coefficient positivity alone, and no unconditional Xi-specific proof of it was obtained here.

## Parallel gate C — self-weighted Hamburger
For zeros \(\rho\), define formally
\[
v_\rho=-\frac1{(\rho-1/2)^2},\qquad
\tau_r=\sum_\rho v_\rho^{r+1}.
\]
The target is
\[
H_N=[\tau_{i+j+1}]_{i,j=0}^N\succeq0\quad\forall N.
\]
If this entire tower were proved from an explicit formula without assuming \(\Re\rho=1/2\), positivity would force the nodes to be positive and hence the critical line. The missing step is an unconditional positive-kernel representation of every quadratic form \(c^TH_Nc\). A signed/complex zero measure does not suffice.

## Parallel gate D — heat flow
The de Bruijn–Newman formulation requires a global functional whose evolution under the backward/forward heat parameter yields the needed threshold inequality. Pairwise zero-repulsion estimates do not automatically control the infinite configuration or boundary terms. No globally sign-definite Lyapunov functional was derived.

## Adversarial conclusion
The four routes are logically distinct but all currently hit the same type of obstruction: an unconditional infinite positivity/real-zero certificate. No circular closure, fitted recurrence, finite verification, or asymptotic wedge is promoted to a theorem.

**Status: research frontier, not a proof of RH.**