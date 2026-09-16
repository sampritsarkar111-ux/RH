# Frontier 31 — Exact Hermite-Minor Attack at Degrees 4 and 5

## Objective

Continue the Jensen/Hermite route toward a genuinely complete proof of RH, without assuming RH, hyperbolicity, or Laguerre–Pólya membership.

The working equivalence is: RH holds iff every generalized Jensen polynomial
\[
J_{d,n}(X)=\sum_{j=0}^d {d\choose j}\gamma_{n+j}X^j
\]
is hyperbolic. For a monic real polynomial, hyperbolicity is equivalent to positive semidefiniteness of its Hermite matrix.

## 1. Exact universal 2x2 Hermite condition

Let
\[
P(x)=x^d+b_1x^{d-1}+b_2x^{d-2}+\cdots+b_d,
\]
and let \(s_k\) be its Newton power sums. The leading \(2\times2\) Hermite minor is
\[
\det\begin{pmatrix}s_0&s_1\\s_1&s_2\end{pmatrix}
=(d-1)b_1^2-2db_2.
\]
For
\[
b_1=d\frac{\gamma_{n+d-1}}{\gamma_{n+d}},\qquad
b_2={d\choose2}\frac{\gamma_{n+d-2}}{\gamma_{n+d}},
\]
this becomes the exact identity
\[
\boxed{
\Delta_2
=d^2(d-1)\frac{\gamma_{n+d-1}^2-\gamma_{n+d-2}\gamma_{n+d}}{\gamma_{n+d}^2}.
}
\]
Thus every Jensen degree imposes the same adjacent Turán inequality on the Taylor coefficients. This is a necessary condition, not a sufficient one.

The coefficient Turán inequalities for the Riemann xi function are known independently, so this lowest Hermite obstruction does not close RH.

## 2. Exact degree-4 normalization from the project ledger

Write the degree-4 Jensen polynomial in the normalized form
\[
P_4(x)=x^4+b_1x^3+b_2x^2+b_3x+b_4,
\]
with the coefficient notation used in Frontier 24:
\[
 b_1=8(2n+7)D/E,
\]
\[
 b_2=24(2n+7)(2n+6)(2n+5)C/E,
\]
\[
 b_3=32(2n+7)(2n+5)(2n+3)B/E,
\]
\[
 b_4=16(2n+7)(2n+5)(2n+3)(2n+1)A/E.
\]

The leading Hermite minors, computed exactly from Newton identities, are:
\[
\Delta_1=4,
\]
\[
\boxed{
\Delta_2=
\frac{192(2n+7)}{E^2}
\left((2n+7)D^2-2(2n+5)(n+3)CE\right).
}
\]
Hence degree-4 hyperbolicity necessarily requires
\[
\boxed{
(2n+7)D^2\ge2(2n+5)(n+3)CE.
}
\]
This is an exact algebraic reduction, not a numerical test.

For a general monic quartic the next leading principal minor is
\[
\Delta_3=
\frac{2}{1}
\left(
16b_4b_2-6b_4b_1^2-18b_3^2+14b_1b_2b_3-3b_1^3b_3-4b_2^3+b_2^2b_1^2
\right),
\]
with the appropriate common denominator after substituting the above \(b_i\). The full determinant is the quartic discriminant divided by the positive leading-coefficient normalization. These are exact polynomial inequalities in \(A,B,C,D,E\).

## 3. Exact degree-5 reduction

For a monic quintic
\[
P_5(x)=x^5+b_1x^4+b_2x^3+b_3x^2+b_4x+b_5,
\]
the first two Hermite minors are
\[
\Delta_1=5,
\qquad
\Delta_2=4b_1^2-10b_2.
\]
For Jensen coefficients this again reduces exactly to the adjacent Turán inequality.

The third and higher minors are genuinely new nonlinear inequalities involving three or more consecutive coefficients. They are not implied by the ordinary Turán inequalities alone.

## 4. What this attempt establishes

1. The Hermite route is algebraically exact and root-independent.
2. Degree 4 immediately produces a concrete new moment/coefficient inequality beyond the universal adjacent Turán condition.
3. Degree 5 produces still higher nonlinear constraints.
4. The degree-4/5 algebra does not itself provide a positivity proof for all \(n\).
5. A proof of all such finite-degree inequalities would still have to be promoted to an all-degree theorem covering every \((d,n)\).

## 5. Critical obstruction identified

The required missing statement is not merely positivity of ordinary moment Hankel matrices. Hermite minors contain nonlinear combinations of Newton sums. Consequently, positivity of the underlying theta moments does not automatically imply positivity of the Hermite minors.

A successful completion therefore needs a new theorem of one of the following forms:

### A. Total-positivity closure
Prove directly that the relevant Riemann theta/Fourier kernel generates a \(TP_\infty\) transform strong enough to imply every Jensen Hermite minor.

### B. All-degree Hermite SOS/integral identity
Construct, for every \(d,n\), an identity
\[
\Delta_{r}(d,n)=\sum_\ell\iint K_{\ell,d,n}(u,v)^2\,d\mu_n(u)d\mu_n(v)+\cdots
\]
with every remaining term manifestly nonnegative and with no unknown-zero dependence.

### C. Equivalent de Bruijn–Newman closure
Prove the required zero-location statement by showing the relevant de Bruijn–Newman parameter is nonpositive, with all analytic estimates made rigorous.

None of these closure statements has been established here. In particular, degree 4/5 symbolic positivity cannot be promoted to RH by itself.

## Status

**Research frontier — not a proof of RH.** The exact calculations eliminate algebraic ambiguity in the low-degree Hermite route and isolate the first genuinely higher-order positivity problem. A complete RH proof still requires an all-degree global closure theorem.
