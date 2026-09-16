# Frontier 37 — exact degree-3 log-concavity gate

## 1. Starting point

For normalized consecutive ratios
\[
r_j=q_j/q_0,
\]
introduce
\[
a=r_1,\qquad v=r_2-a^2,
\]
\[
w=r_3-3ar_2+2a^3,\qquad z=r_4-4ar_3+6a^2r_2-3a^4.
\]
The exact central-moment factorization from Frontier 36 is
\[
\widetilde Q_d=2(d-3)vz-3(d-2)w^2-6(d-1)v^3.
\]
The degree-3 third-Hermite obstruction is proportional to \(\widetilde Q_3\).

## 2. Exact specialization to d=3

Substitution gives
\[
\boxed{\widetilde Q_3=-3w^2-12v^3.}
\]
The multiplicative prefactor relating this quantity to the Hermite minor is strictly positive for the admissible nondegenerate parameters. Therefore a necessary condition for the degree-3 Jensen/Hermite inequality is
\[
-3w^2-12v^3\ge0.
\]
Equivalently,
\[
\boxed{4v^3+w^2\le0.}
\]
Since \(w^2\ge0\), this immediately forces
\[
\boxed{v\le0.}
\]

## 3. Translation into the original coefficient sequence

For the relevant block \(q_j=\gamma_{n+d-j}\), at \(d=3\),
\[
q_0=\gamma_{n+3},\quad q_1=\gamma_{n+2},\quad q_2=\gamma_{n+1}.
\]
Hence
\[
v=\frac{\gamma_{n+1}}{\gamma_{n+3}}
-\left(\frac{\gamma_{n+2}}{\gamma_{n+3}}\right)^2
=\frac{\gamma_{n+1}\gamma_{n+3}-\gamma_{n+2}^2}{\gamma_{n+3}^2}.
\]
Thus
\[
\boxed{
\gamma_{n+2}^2\ge \gamma_{n+1}\gamma_{n+3}
}
\]
is a necessary condition for the degree-3 closure inequality.

This is a genuine gate: failure at any shift \(n\) would immediately falsify the proposed all-degree Jensen-hyperbolicity route at degree 3. Conversely, proving this log-concavity alone is not sufficient for RH; the full all-degree obstruction remains.

## 4. Stronger exact degree-3 condition

The exact condition is stronger than log-concavity:
\[
\boxed{4v^3+w^2\le0.}
\]
After clearing denominators, this is a polynomial inequality in five consecutive \(\gamma\)-coefficients. Therefore the research program should attack two nested targets:

1. prove the necessary Turan/log-concavity inequality
\[
\gamma_{m+1}^2-\gamma_m\gamma_{m+2}\ge0
\]
for all relevant \(m\);
2. prove the stronger five-term inequality \(4v^3+w^2\le0\) for every shift.

## 5. Theta-kernel target

Using the exact Riemann-theta moment representation of \(\gamma_m\), neither step may be replaced by generic positivity of a Stieltjes moment sequence: Frontier 33 gives an exact positive-moment counterexample to that generic mechanism.

The next closure calculation is therefore to insert the theta kernel directly into
\[
\gamma_{m+1}^2-\gamma_m\gamma_{m+2}
\]
and attempt an exact double-integral positive-kernel or sum-of-squares representation. If such a representation fails, the failure must be recorded explicitly rather than converted into a proof claim.

## Status

**Exact structural reduction; not a proof of RH.**
