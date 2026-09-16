# Frontier 43 — Exact centered factorization of the quartic Hermite determinant

Date: 2026-09-16

## Main algebraic result

For the degree-4 Jensen polynomial, define centered coordinates
\[
a=r_1,\quad v=r_2-a^2,\quad w=r_3-3ar_2+2a^3,\quad z=r_4-4ar_3+6a^2r_2-3a^4.
\]
Substituting the Jensen coefficients
\[
b_1=4r_1,\quad b_2=6r_2,\quad b_3=4r_3,\quad b_4=r_4
\]
into the exact quartic discriminant yields the exact translation-invariant identity
\[
\boxed{\Delta_4=256\,\mathcal D_4(v,w,z)}
\]
where
\[
\boxed{\mathcal D_4(v,w,z)=z^3-18v^2z^2+81v^4z+54vw^2z-54v^3w^2-27w^4.}
\]

## Consequences

The location parameter \(a\) disappears completely. Therefore the quartic Hermite layer depends only on the centered second-, third-, and fourth-order coordinates \((v,w,z)\). This is a substantial simplification of the previous raw-ratio expression.

The degree-3 cone from Frontier 37 is
\[
4(-v)^3\ge w^2.
\]
For the quartic layer, one now needs \(\mathcal D_4(v,w,z)\ge0\) together with the lower Hermite conditions.

## Normalized fourth-order target

If \(u=-v>0\) and
\[
w=2u^{3/2}t,\qquad |t|\le1,
\]
then
\[
\mathcal D_4
= z^3-18u^2z^2+81u^4z-216u^4t^2z+432u^6t^2-432u^6t^4.
\]
Writing \(y=z/u^2\), the sign target becomes
\[
\boxed{
\frac{\mathcal D_4}{u^6}=y^3-18y^2+81y-216t^2y+432t^2(1-t^2).
}
\]
This is a two-variable universal algebraic target for the fourth Hermite layer.

## Important limitation

This is an exact finite-degree reduction, not an RH proof. Even proving this inequality for every Riemann-xi Jensen quartic would establish only the degree-4 Hermite layer. RH requires hyperbolicity for every degree and shift.

The remaining central question is whether the Riemann-specific theta structure forces the admissible \((u,t,y)\) region into the nonnegative domain of this polynomial. Generic Stieltjes positivity has already been shown insufficient.

## Status

Genuine algebraic breakthrough within the finite-degree program: the quartic determinant has been reduced exactly to three centered invariants and then to a two-variable normalized polynomial under the cubic cone. No universal Riemann-specific closure theorem has yet been proved.
