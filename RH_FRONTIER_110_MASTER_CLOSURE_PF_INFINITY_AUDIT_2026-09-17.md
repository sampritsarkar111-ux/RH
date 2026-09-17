# RH Frontier 110 — Master Closure Attempt: PF∞ / Jensen / Weil / Nyman–Beurling

Date: 2026-09-17

## Executive result

This file attempts to close the remaining three walls by replacing them with one exact positivity/cyclicity theorem. The reduction is unconditional, but the final positivity statement is **not proved**. Therefore this file does not claim a proof of RH.

## 1. Master object

Let

\[
\Xi(t)=\xi\!\left(\frac12+it\right),
\qquad
\Xi(t)=\int_0^\infty \Phi(u)\cos(tu)\,du,
\]

with the standard Riemann theta-derived kernel \(\Phi\). RH is equivalent to \(\Xi\) belonging to the Laguerre–Pólya class.

A sufficient structural route is to prove that the appropriate coefficient/translation kernel is PF∞ (all finite Toeplitz minors nonnegative) and that the corresponding Fourier transform is in the Laguerre–Pólya class. The key point is that positivity of the raw moment Hankel matrices is insufficient: it gives Stieltjes/log-convexity information, whereas Jensen hyperbolicity requires the factorial-normalized coefficient structure.

## 2. Exact Jensen target

Write

\[
\Xi(z)=\sum_{n\ge0}(-1)^n\frac{\gamma(n)}{(2n)!}z^{2n}.
\]

For degree \(d\) and shift \(n\), the Jensen polynomial is

\[
J^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j.
\]

Pólya's criterion gives

\[
RH\iff J^{d,n}\text{ is hyperbolic for every }d,n\ge0.
\]

Hence a complete theta proof must establish hyperbolicity for **all** \((d,n)\), not merely a fixed-degree asymptotic region.

## 3. Degree-two exact gate

For the factorial-corrected moment representation used in the project, with

\[
M_n=\int_0^\infty \Phi_1(u)u^{2n}\,du,
\]

the quadratic Jensen condition is exactly

\[
\boxed{\frac{M_{n+1}^2}{M_nM_{n+2}}\ge \frac{2n+1}{2n+3}}
\]

or, for the probability measure proportional to \(\Phi_1(u)u^{2n}du\),

\[
\boxed{\frac{\operatorname{Var}(u^2)}{\mathbb E[u^2]^2}\le\frac{2}{2n+1}}.
\]

This is an exact necessary-and-sufficient gate for degree two in this normalization. It does not automatically extend to \(d\ge3\).

## 4. Proposed all-degree master inequality

A genuine closure theorem would need a theta-specific total-positivity statement of the following form:

\[
\boxed{
\det\!\big[\mathcal J_{r_i+r_j}(n)\big]_{i,j=0}^{k-1}\ge0
\quad\text{for every }k,n\ge1,
}
\]

where \(\mathcal J_m(n)\) is the exact factorial/Jensen-normalized moment transform, not the raw moment \(M_m\).

The determinant must be constructed so that its vanishing/sign is equivalent to the discriminant/interlacing conditions of every Jensen polynomial. A raw Hankel determinant cannot serve this role because positive measures automatically give Hankel positivity while Jensen hyperbolicity is strictly stronger.

## 5. Arithmetic route: exact remaining coercivity

For Nyman–Beurling, let \(B\) denote the critical-line dilation operator. Finite Gram matrices

\[
G_N=B_N^*B_N\succeq0
\]

are automatic. The target is instead

\[
\boxed{\operatorname{dist}\!\left(\frac1s,\overline{\operatorname{Ran}B}\right)=0.}
\]

Equivalently, for the finite projection residual \(d_N\), one needs

\[
\boxed{d_N^2=1-q_N^*G_N^\dagger q_N\longrightarrow0.}
\]

Any argument proving this unconditionally must avoid assuming the absence of an off-line zero. Indeed, if \(\zeta(\rho)=0\) with \(\Re\rho>1/2\), every arithmetic multiple \(\zeta(s)A_N(s)/s\) vanishes at \(\rho\), whereas \(1/s\) does not. Thus the missing cyclicity statement is exactly where the RH content resides.

## 6. Weil/Li route: exact global gate

Li's criterion requires

\[
\lambda_m\ge0\qquad(m\ge1).
\]

A non-circular proof would follow from an RH-independent positive representation of the generating derivative

\[
\frac{d}{dz}\log\xi\!\left(\frac1{1-z}\right)
=\sum_{m\ge1}\lambda_mz^{m-1}
\]

with a positive measure/kernel whose coefficient extraction preserves positivity. No such representation has been derived here.

Likewise, the compact-support Weil prime contribution is a finite self-adjoint shift perturbation

\[
P_L=-2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}S_{\log n}.
\]

Triangle-inequality/operator-norm estimates erase the arithmetic cancellation and cannot prove the required global positivity.

## 7. New synthesis: one master closure statement

The three routes can be organized around one abstract theorem:

> **Master Closure Theorem (target).** If the Riemann theta-derived Jensen-normalized translation kernel is PF∞ in the exact sense required to imply Laguerre–Pólya membership, then \(\Xi\) is Laguerre–Pólya, hence RH. Equivalently, an exact positive factorization of the corresponding Weil form would imply the same conclusion; equivalently, an RH-independent Nyman–Beurling cyclicity proof would imply the same conclusion.

The implication from any one of these completed mechanisms to RH is rigorous. The unresolved part is proving one of the mechanisms itself.

## 8. Adversarial checks that prevent circular closure

Any proposed final proof must survive all of the following tests:

1. No use of \(\zeta(\rho)\ne0\) for \(\Re\rho>1/2\) unless independently established.
2. No replacement of a critical-line identity by a convergent Dirichlet series outside its convergence half-plane.
3. No inference from raw moment positivity to Jensen hyperbolicity.
4. No finite-degree verification extrapolated to all degrees without a uniform theorem.
5. No asymptotic hyperbolicity region treated as global hyperbolicity.
6. No numerical zero verification treated as proof.
7. No positive decomposition whose positivity itself is equivalent to RH merely by renaming the target.

## 9. Current mathematical conclusion

The attempted closure does **not** establish RH. The remaining wall has been sharpened to one of three exact mechanisms:

- PF∞ / total positivity of the factorial-normalized Riemann theta translation kernel;
- unconditional Nyman–Beurling cyclicity/coercivity;
- unconditional global Weil/Li positivity/factorization.

Closing any one of these would give a complete proof. None has been proved in this pass.

## References

Clay Mathematics Institute, Riemann Hypothesis: https://www.claymath.org/millennium/Riemann-Hypothesis/

Griffin–Ono–Rolen–Zagier, Jensen polynomials: https://arxiv.org/abs/1902.07321

Griffin et al., Jensen polynomials for the Riemann Xi function: https://arxiv.org/abs/1910.01227

Holland (2026), hyperbolicity wedge for Jensen polynomials: https://arxiv.org/abs/2608.08682
