# RH Frontier 191 — Exact Positive-Measure No-Go + Closure Gate

Date: 2026-09-18

## Executive result

A new exact falsification closes one remaining weak route: positivity of the underlying theta/moment measure, even with the factorial normalization used for Jensen coefficients, is **not by itself sufficient** to force degree-3 Jensen hyperbolicity.

Take the positive discrete measure
\[
\mu=\frac1{1000}\delta_{1}+\frac{999}{1000}\delta_{1/10}.
\]
Define
\[
M_n=\int u^{2n}\,d\mu(u),\qquad \gamma_n=\frac{M_n}{(2n)!},
\]
and
\[
J_{3,0}(X)=\gamma_0+3\gamma_1X+3\gamma_2X^2+\gamma_3X^3.
\]
Exact symbolic evaluation gives
\[
\boxed{\operatorname{Disc}(J_{3,0})=-\frac{98459838459955337}{3840000000000000000000000000}<0.}
\]
Therefore a generic positive-measure / factorial-moment argument cannot prove the Riemann Jensen gate. The Riemann-specific ingredient must be stronger: arithmetic theta structure, total positivity, sign regularity, or an equivalent global mechanism.

## 1. Verified cubic algebra

For
\[
p(X)=X^3+aX^2+bX+c,
\]
\[
\boxed{\operatorname{Disc}(p)=a^2b^2-4b^3-4a^3c+18abc-27c^2.}
\]
For
\[
a=3\gamma_{n+2}/\gamma_{n+3},\quad b=3\gamma_{n+1}/\gamma_{n+3},\quad c=\gamma_n/\gamma_{n+3},
\]
the Hermite determinant equals this discriminant exactly.

## 2. What this closes

The following implication is false:
\[
\Phi\ge0\quad\Longrightarrow\quad J_{d,n}\text{ hyperbolic for all }d,n.
\]
It already fails at d=3 for a positive two-atom measure. Thus raw positivity, ordinary moment positivity, and factorial normalization alone cannot be the missing RH theorem.

This is a genuine obstruction, not merely a numerical failure: the counterexample is rational and the discriminant is exactly negative.

## 3. Surviving proof-bearing gates

The remaining mathematically legitimate targets are:

1. **Theta-specific PF∞ / strict sign regularity:** prove the exact completed Riemann kernel has the stronger all-minor property required for Jensen hyperbolicity.
2. **Nyman–Beurling cyclicity:** prove the full RH-equivalent density statement without assuming an off-line zero is absent.
3. **Weil/Li positivity:** derive an RH-independent positive factorization of the full explicit-formula quadratic form.
4. **Zero-independent spectral realization:** construct a self-adjoint operator from theta/arithmetic data whose spectral determinant is exactly Xi, without defining the operator from the unknown zeros.

## 4. Anti-circular closure gate

A final proof must establish one complete implication
\[
\zeta(\rho)=0,\ 0<\Re\rho<1\quad\Longrightarrow\quad\Re\rho=\frac12,
\]
without assuming the conclusion in the construction of the operator, kernel, approximation space, positivity measure, or limiting argument.

## 5. Current status

This frontier closes a false shortcut but does not prove RH. The Clay Mathematics Institute currently lists RH as unsolved. The project therefore remains in research status.

## External verification

Wolfram Language independently returns the cubic discriminant formula and the exact negative rational counterexample above. Published Jensen-polynomial work establishes the equivalence between RH and all-degree Jensen hyperbolicity and proves substantial finite/effective/asymptotic results, but not the missing global theorem.
