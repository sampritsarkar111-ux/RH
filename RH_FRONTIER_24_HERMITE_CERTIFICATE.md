# RH Frontier 24 — Direct Hermite certificate

## Objective

The previous universal scale-mixture argument was invalid. The next attack therefore works directly with the Jensen polynomials

\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j,
\qquad
\gamma_m=C\frac{m!}{(2m)!}M_m.
\]

The target remains: prove every \(J_{d,n}\) is real-rooted.

## Hermite-matrix route

For a monic real polynomial
\[
p(x)=x^d+b_{d-1}x^{d-1}+\cdots+b_0
\]
with roots \(r_1,\ldots,r_d\), define Newton sums
\[
s_k=\sum_{i=1}^{d}r_i^k.
\]
The Hermite matrix is
\[
H_d(p)=\bigl(s_{i+j}\bigr)_{i,j=0}^{d-1}.
\]
For real roots,
\[
v^{T}H_d(p)v
=
\sum_{i=1}^{d}
\left(\sum_{j=0}^{d-1}v_jr_i^j\right)^2
\ge0.
\]
Thus positive semidefiniteness of \(H_d\) is a direct algebraic certificate for real-rootedness (including repeated roots).

## Explicit quartic certificate

Write
\[
A=M_n,\quad B=M_{n+1},\quad C=M_{n+2},\quad
D=M_{n+3},\quad E=M_{n+4}.
\]

Then
\[
J_{4,n}(X)=
A+
\frac{2B}{2n+1}X+
\frac{3C}{2(2n+1)(2n+3)}X^2+
\frac{D}{2(2n+1)(2n+3)(2n+5)}X^3+
\frac{E}{4(2n+1)(2n+3)(2n+5)(2n+7)}X^4.
\]

After division by its positive leading coefficient,
\[
p(X)=X^4+b_3X^3+b_2X^2+b_1X+b_0.
\]
The monic coefficients simplify exactly to
\[
b_3=8(2n+7)\frac DE,
\]
\[
b_2=24(2n+7)(2n+6)(2n+5)\frac CE,
\]
\[
b_1=32(2n+7)(2n+5)(2n+3)\frac BE,
\]
\[
b_0=16(2n+7)(2n+5)(2n+3)(2n+1)\frac AE.
\]

Its first Hermite principal minors are
\[
\Delta_1=4,
\]
\[
\boxed{\Delta_2=3b_3^2-8b_2},
\]
and
\[
\boxed{
\Delta_3=
2\left(
16b_0b_2-6b_0b_3^2-18b_1^2
+14b_1b_2b_3-3b_1b_3^3
-4b_2^3+b_2^2b_3^2
\right).
}
\]

The fourth determinant is the final quartic Hermite certificate.

## General research target

For every \(d,n\), establish
\[
\boxed{H_d(J_{d,n})\succeq0.}
\]
The crucial point is that this must be proved from the **specific Riemann kernel/moment structure**. Positivity of the moments alone is insufficient.

## New obstruction test

Any proposed theorem that claims arbitrary positive scale mixtures preserve hyperbolicity is rejected. The earlier research already supplied a counterexample. The present route avoids that invalid inference entirely.

## Status

This is a rigorous certificate framework and a concrete degree-4 reduction. It is **not yet a proof of RH**. The missing step is an all-degree, all-shift positivity theorem for the Hermite matrices of the Riemann Jensen family.
