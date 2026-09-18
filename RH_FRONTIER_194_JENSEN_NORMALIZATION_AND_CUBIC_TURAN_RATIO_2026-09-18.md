# RH Frontier 194 — Jensen Normalization Correction + Cubic Turán-Ratio Theorem
## Date
2026-09-18

## Status
**Research frontier only. The Riemann Hypothesis is NOT proved by this document.**

This frontier records the latest exact correction and algebraic closure obtained while auditing Jensen-polynomial routes to RH.

---

## 1. Critical Jensen normalization correction

For the completed zeta function,
\[
\xi(1/2+z)=\sum_{n\ge 0}\frac{\gamma_n}{n!}z^{2n}.
\]

If the ordinary Taylor expansion is
\[
\xi(1/2+z)=\sum_{n\ge0}a_nz^{2n},
\]
then
\[
\boxed{\gamma_n=n!\,a_n}.
\]

When a theta/moment calculation gives
\[
a_n=\frac{M_n}{(2n)!},
\]
the standard Jensen coefficient is therefore
\[
\boxed{\gamma_n=\frac{n!}{(2n)!}M_n}.
\]

Any previous argument that identified raw Taylor coefficients or raw moments directly with the standard Jensen sequence must be re-audited under this normalization.

---

## 2. Standard Jensen polynomials

Define
\[
\boxed{
J^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j.
}
\]

The Pólya/Jensen route requires hyperbolicity for the complete family:
\[
\boxed{RH\iff J^{d,n}\text{ is hyperbolic for every }d,n\ge0}
\]
under the standard Jensen-polynomial formulation for the Riemann \(\xi\)-function.

Finite-degree or asymptotic hyperbolicity alone is not enough.

---

## 3. Exact degree-3 Turán-ratio theorem

For
\[
J^{3,n}(X)
=
\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3,
\]
define adjacent ratios
\[
r_n=\frac{\gamma_{n+1}^2}{\gamma_n\gamma_{n+2}},
\qquad
q_n=\frac{\gamma_{n+2}^2}{\gamma_{n+1}\gamma_{n+3}}.
\]

Assuming the relevant coefficients are nonzero, positive coefficient scaling leaves hyperbolicity invariant. The cubic discriminant sign is governed exactly by
\[
\boxed{
F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2.
}
\]

Therefore
\[
\boxed{
J^{3,n}\text{ hyperbolic}
\iff
F(r_n,q_n)\le0.
}
\]

Set
\[
x=r_n-1,\qquad y=q_n-1.
\]
Then the same invariant becomes
\[
\boxed{
F=(x-y)^2-2xy(x+y)-3x^2y^2.
}
\]

In the log-concave regime \(r_n,q_n\ge1\), the criterion can equivalently be written
\[
\boxed{
(r_n-q_n)^2
\le
(r_n-1)(q_n-1)
\left[
2(r_n+q_n-2)+3(r_n-1)(q_n-1)
\right].
}
\]

A useful special case is
\[
r_n=q_n=r>1
\quad\Longrightarrow\quad
F(r,r)=-(r-1)^3(1+3r)<0.
\]

Thus ordinary log-concavity by itself does not close the cubic gate; the consecutive Turán ratios must also satisfy a compatibility condition.

---

## 4. Hermite-matrix equivalent

For a monic cubic
\[
X^3+aX^2+bX+c,
\]
the Hermite matrix is
\[
H_3=
\begin{pmatrix}
3&-a&a^2-2b\\
-a&a^2-2b&-a^3+3ab-3c\\
a^2-2b&-a^3+3ab-3c&a^4-4a^2b+2b^2+4ac
\end{pmatrix}.
\]

Its relevant principal minors are
\[
\det H_1=3,
\]
\[
\det H_2=2(a^2-3b),
\]
and
\[
\det H_3
=
-4a^3c+a^2b^2+18abc-4b^3-27c^2.
\]

For the Jensen cubic, after substitution and coefficient scaling,
\[
\det H_3
=
-\frac{27}{\gamma_{n+3}^4}
\left(
\gamma_n^2\gamma_{n+3}^2
-6\gamma_n\gamma_{n+1}\gamma_{n+2}\gamma_{n+3}
+4\gamma_n\gamma_{n+2}^3
+4\gamma_{n+1}^3\gamma_{n+3}
-3\gamma_{n+1}^2\gamma_{n+2}^2
\right).
\]

This is algebraically consistent with the ratio invariant above.

---

## 5. 2026 literature boundary

A 2026 preprint by Jonathan Holland, *A new hyperbolicity wedge and a joint semicircle limit for Jensen polynomials of Riemann's xi-function*, gives a simultaneous degree/shift hyperbolicity region of the form
\[
n^3\log^2(n+2)\ge Kd^5
\]
for an absolute constant \(K>0\), under the theorem's stated hypotheses.

This is a substantial partial result, but it leaves a residual region in the \((d,n)\)-plane. It therefore does not establish RH.

Reference:
https://arxiv.org/abs/2608.08682

Earlier Jensen-polynomial work establishes fixed-degree/asymptotic hyperbolicity results and finite-degree cases, but the global all-\((d,n)\) theorem remains the decisive missing implication.

---

## 6. Numerical sanity checks

Numerical checks after applying the factorial normalization are consistent with the cubic ratio criterion in tested low-shift examples. Such computations are **sanity checks only**.

They cannot establish:
- all shifts \(n\),
- all degrees \(d\),
- uniform hyperbolicity,
- RH,
- or a zero-free half-plane.

---

## 7. New research program: adjacent-ratio geometry

The degree-3 result suggests a general route.

Define
\[
R_k=\frac{\gamma_{k+1}^2}{\gamma_k\gamma_{k+2}}.
\]

For degree \(d\), express every Hermite/Jensen principal minor in terms of
\[
R_n,R_{n+1},\ldots,R_{n+d-2}
\]
plus explicit positive scaling factors.

Target theorem:
\[
\boxed{
\text{Theta structure}
\Longrightarrow
\text{uniform compatibility inequalities among adjacent }R_k
\Longrightarrow
J^{d,n}\text{ hyperbolic for all }d,n.
}
\]

The first nontrivial next target is the exact degree-4 invariant in
\[
R_n,R_{n+1},R_{n+2}.
\]

The key requirement is a proof from the theta kernel, not numerical pattern matching.

---

## 8. Theta/moment normalization audit

If
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du
\]
and
\[
M_n=\int_{\mathbb R}u^{2n}\Phi(u)\,du,
\]
then the even Taylor coefficient in \(t\) is governed by
\[
\frac{(-1)^nM_n}{(2n)!}.
\]

The Jensen sequence must then be converted with the appropriate factorial factor. Consequently, every proposed implication
\[
\text{moment inequality}\Longrightarrow\text{Jensen hyperbolicity}
\]
must explicitly display this conversion.

Positive moments alone are not sufficient to imply the Laguerre--Pólya property.

---

## 9. Other open RH-bearing routes

The current research matrix still contains these independent proof-critical gates:

### A. Jensen / Pólya
Need a theorem covering every \((d,n)\), not merely a wedge or fixed-degree asymptotics.

### B. PF∞ / total positivity
Need an RH-independent proof that the relevant factorial-normalized theta translation kernel has the required total-positivity/PF∞ property.

### C. Weil / Li
Need an exact RH-independent global positivity identity or factorization implying all Weil/Li inequalities.

### D. Nyman--Beurling
Need unconditional cyclicity/coercivity:
\[
\operatorname{dist}
\left(
\frac1s,
\overline{\operatorname{Ran}B}
\right)=0.
\]
Finite projection residual decay alone is not enough without an unconditional proof.

### E. de Branges / spectral route
Need a rigorously constructed self-adjoint operator with a spectrum identified with the completed zeta zeros, without defining the operator using the unknown zeros.

### F. de Bruijn--Newman
Need an unconditional argument forcing the relevant deformation parameter to the RH side of the critical threshold.

---

## 10. Anti-circularity checklist

Any proposed closure must pass all of the following:

1. Do not assume RH in a hidden lemma.
2. Do not use \(\zeta(s)\)'s Euler/Dirichlet representation outside its convergence domain without continuation justification.
3. Do not identify unknown zeros as \(1/2+it\) before proving the real-part statement.
4. Do not infer all-degree hyperbolicity from finitely many degrees.
5. Do not infer global hyperbolicity from asymptotic hyperbolicity without controlling the residual region.
6. Do not infer RH from numerical verification.
7. Do not replace RH by an equivalent positivity statement and call that positivity proved.
8. Keep factorial normalization explicit.
9. Track multiplicities and analytic continuation.
10. For operator routes, prove self-adjointness, domain, spectrum identification, and completeness independently.

---

## 11. Current honest status

This frontier closes an algebraic normalization error and gives an exact degree-3 ratio criterion. It does **not** close the all-degree Jensen theorem and does **not** solve RH.

The decisive breakthrough target remains an unconditional theorem connecting the arithmetic/theta structure to global hyperbolicity or another RH-equivalent positivity mechanism.

## 12. Next exact targets

1. Derive the degree-4 Turán-ratio invariant symbolically.
2. Derive degree-5 compatibility conditions.
3. Translate the degree-2 moment gate using the corrected factorial normalization.
4. Search for a theta-kernel theorem implying the required ratio regularity.
5. Test whether a single total-positivity theorem subsumes all Jensen degrees.
6. Independently audit Weil/Li and Nyman--Beurling routes for a common positive quadratic form.
7. Keep every successful lemma tagged as unconditional, conditional, numerical, or heuristic.

---
**Repository note:** This file is a research record, not a claim of a completed proof of the Riemann Hypothesis.
