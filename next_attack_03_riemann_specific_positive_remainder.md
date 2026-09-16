# Next attack 03 — Riemann-specific positive-remainder theorem

## Purpose
Push beyond the abstract PF∞ target and isolate a concrete theorem about the actual completed Riemann kernel. This is the next mathematical wall; it is not yet a proof of RH.

## A. Start from the exact cosine-transform representation
Use the standard completed Xi Fourier representation in the form
\[
\Xi(t)=\int_0^\infty \Phi(u)\cos(tu)\,du,
\]
with the exact theta-derived \(\Phi\), retaining its unsummed lattice representation until after all algebraic pairings are performed.

Define even Taylor coefficients by
\[
a_m=(-1)^m\Xi^{(2m)}(0).
\]
Form the Hankel matrix \(A=(a_{i+j})\).

## B. Convert the determinant into a particle/lattice integral
For a d×d minor, use Andreief/Cauchy–Binet formally first, then prove every interchange and convergence estimate:
\[
\det\left[\int u^{2(i+j)}\Phi(u)\,du\right]_{i,j=0}^{d-1}
=\frac1{d!}\int_{(0,\infty)^d}
\det[u_r^{2i}]^2\prod_{r=1}^d\Phi(u_r)\,du_r.
\]
Since
\[
\det[u_r^{2i}]^2=\prod_{r<s}(u_s^2-u_r^2)^2\ge0,
\]
the sign question is reduced to the exact sign of the transformed measure/kernel.

## C. The real obstruction
The theta-derived \(\Phi\) is not automatically pointwise nonnegative in every representation. Therefore the decisive task is to find an exact decomposition
\[
\boxed{\Phi(u)=\sum_{n\ge0}w_n\phi_n(u)+R(u),\qquad w_n\ge0,}
\]
where the remainder satisfies an explicit determinant-level inequality, not merely pointwise positivity.

The strongest possible result is \(R\equiv0\) after a signed basis transformation. The next-best exact result is a positive determinant bound such as
\[
\det M_d[R+\sum_nw_n\phi_n]\ge0
\]
for every d.

## D. Degree-three target
Compute the exact d=3 determinant before lattice collapse. After Poisson/Jacobi transformation, seek
\[
\boxed{
-\Delta_3
=P_3+E_3,
\qquad P_3\ge0,
}
\]
and then determine E_3 exactly. Three outcomes are possible:

1. \(E_3=0\): major structural evidence for an all-order identity.
2. \(E_3\ge0\): a positive-remainder theorem may be possible.
3. \(E_3\) changes sign: the PF∞ ansatz must be modified.

No numerical fit is allowed to replace this trichotomy.

## E. All-order lift
If the degree-three remainder admits a representation as a sum over ordered lattice particles with squared Vandermonde,
\[
\boxed{
\sigma_d\Delta_d
=\frac1{d!}\sum_{\mathbf n}W(\mathbf n)
\prod_{r<s}Q(n_r,n_s)^2,
\qquad W(\mathbf n)\ge0,
}
\]
then positivity is immediate for every d. The remaining task becomes proving the exact convergence and identifying \(W\).

## F. RH bridge
After obtaining the all-order determinant property, explicitly prove the bridge to the Laguerre–Pólya class. Do not assume that positivity of one Hankel family automatically gives real-rootedness of Xi; identify the exact theorem/hypotheses required and verify them for Xi.

## G. Falsification
The proposed mechanism is rejected if any finite d has a sign violation, if the transformed weights are not nonnegative and cannot be regrouped into nonnegative blocks, or if the determinant property does not imply the required real-zero theorem.

## Current status
This document specifies a concrete Riemann-specific attack: unsummed theta → Poisson/Jacobi → Andreief particle determinant → exact positive-remainder decomposition → all-order sign regularity → Laguerre–Pólya → RH. The first four arrows remain research targets, not established results.
