# Frontier 42 — Quartic Hermite determinant in forward ratio coordinates

Date: 2026-09-16

## Exact specialization

For \(J_{4,n}\), use the monic coefficients
\[
b_1=4r_1,\quad b_2=6r_2,\quad b_3=4r_3,\quad b_4=r_4,
\]
with
\[
r_1=R_m,\quad r_2=R_mR_{m+1},\quad r_3=R_mR_{m+1}R_{m+2},\quad r_4=R_mR_{m+1}R_{m+2}R_{m+3}.
\]
Substitution into the exact quartic discriminant gives the degree-4 Hermite determinant directly as a polynomial in four consecutive ratios.

## Structural interpretation

The resulting expression is homogeneous in the coefficient scale and invariant under translation after passage to centered cumulant coordinates. Thus the useful proof target is not the raw expanded polynomial but a factorization into centered variance/skewness/kurtosis-type coordinates together with lower Hermite minors.

## Research target

Find an exact factorization of the specialized \(\Delta_4\) in the coordinates
\[
a=r_1,\quad v=r_2-a^2,\quad w=r_3-3ar_2+2a^3,\quad z=r_4-4ar_3+6a^2r_2-3a^4.
\]
Then determine whether its sign follows from the cubic cone plus one genuinely new fourth-order inequality.

A successful fourth-order closure would still be only one finite Hermite layer; all degrees remain necessary for RH.

## Status

Exact specialization and proof target established. No universal Riemann-specific sign theorem obtained.
