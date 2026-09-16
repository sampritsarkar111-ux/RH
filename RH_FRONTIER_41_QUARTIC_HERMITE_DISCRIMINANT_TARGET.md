# Frontier 41 — Quartic Hermite minor / discriminant target

Date: 2026-09-16

## 1. Purpose

Frontier 40 reduced the third-Hermite obstruction to exact ratio finite differences. The next independent layer is the 4x4 Hermite minor. For a monic quartic
\[
P(x)=x^4+b_1x^3+b_2x^2+b_3x+b_4,
\]
the 4x4 Hermite determinant is the quartic discriminant (with the standard monic normalization). Thus degree four gives an exact algebraic target rather than another heuristic moment condition.

## 2. Exact quartic determinant

Using Newton power sums
\[
s_0=4,\qquad s_k+b_1s_{k-1}+\cdots+b_{k-1}s_1+kb_k=0
\]
(with \(b_k=0\) for \(k>4\)), direct elimination gives
\[
\boxed{\begin{aligned}
\Delta_4={}&-27b_1^4b_4^2+18b_1^3b_2b_3b_4-4b_1^3b_3^3-4b_1^2b_2^3b_4+b_1^2b_2^2b_3^2\\
&+144b_1^2b_2b_4^2-6b_1^2b_3^2b_4-80b_1b_2^2b_3b_4+18b_1b_2b_3^3\\
&-192b_1b_3b_4^2+16b_2^4b_4-4b_2^3b_3^2-128b_2^2b_4^2\\
&+144b_2b_3^2b_4-27b_3^4+256b_4^3.
\end{aligned}}
\]
Hyperbolicity of a real monic quartic is equivalent to nonnegative discriminant together with the appropriate lower Hermite/principal-minor conditions; therefore \(\Delta_4\ge0\) alone is not sufficient.

## 3. Jensen specialization

For a degree-4 Jensen polynomial
\[
J_{4,n}(X)=\sum_{j=0}^4\binom4j\gamma(n+j)X^j,
\]
its monic normalization is obtained by dividing by \(\gamma(n+4)\). Hence
\[
(b_1,b_2,b_3,b_4)=\left(4r_1,\ 6r_2,\ 4r_3,\ r_4\right),
\]
where
\[
r_j=\frac{\gamma(n+j)}{\gamma(n+4)}.
\]
Equivalently, in forward ratio variables \(R_k=\gamma(k+1)/\gamma(k)\), these are products of consecutive ratios.

## 4. Exact research target

The Riemann-specific target is therefore:

> Establish the complete Hermite-positive conditions for every \(J_{4,n}\), using the explicit Riemann-xi/theta structure rather than generic Stieltjes positivity.

This includes the already-derived lower minors and the quartic discriminant. A proof of this degree-4 layer would be a genuine new theorem, but would still not establish RH because the Pólya–Jensen criterion requires all degrees and all shifts.

## 5. Why the generic-moment route remains insufficient

Frontier 40 exhibited a finite positive atomic measure whose factorially weighted moment coefficients violate the cubic cone. Therefore positivity of a representing kernel, raw Stieltjes moment inequalities, or generic log-convexity cannot by themselves establish these Hermite conditions.

The missing ingredient must be specific to the Riemann xi function: explicit theta-kernel structure, total positivity, a functional/heat-equation identity, or another theorem controlling the entire coefficient sequence.

## 6. Parallel closure program

1. Reduce \(\Delta_4\) to consecutive ratio differences and simplify symbolically.
2. Test the resulting inequality numerically for the known Riemann-xi coefficients over many \(n\) (reconnaissance only).
3. Search for a Riemann-specific structural inequality capable of proving the ratio constraints.
4. In parallel, derive the general \(k\times k\) Hermite-minor recurrence so that the degree-4 calculation is not isolated.
5. Any candidate implication must ultimately cover every \(d,n\), not merely fixed degree.

## 7. Status

Exact algebraic target established. No Riemann-specific proof of the quartic conditions has been obtained, and no RH proof is claimed.
