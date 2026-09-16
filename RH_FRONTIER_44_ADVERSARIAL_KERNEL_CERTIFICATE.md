# Frontier 44 — adversarial exact kernel certificate

## 1. Raw Turan kernel

For
\[
A_m(x)=x^{2m-2}\bigl(16m(2m-1)-x^2\bigr),
\qquad
\eta_m=\frac{(m+1)(2m+1)}{2(m+2)(2m+3)},
\]
the exact kernel is
\[
K_m(x,y)=A_{m+1}(x)A_{m+1}(y)-\eta_m[A_m(x)A_{m+2}(y)+A_m(y)A_{m+2}(x)].
\]

## 2. Exact diagonal certificate

Putting \(X=x^2\), symbolic simplification gives
\[
\boxed{
K_m(x,x)=\frac{X^{2m}}{(m+2)(2m+3)}P_m(X),
}
\]
where
\[
P_m(X)=4mX^2+5X^2-(256m^3+576m^2+416m+96)X
+4096m^5+21504m^4+40960m^3+34560m^2+12544m+1536.
\]
Thus the raw kernel is not identically zero on the diagonal. In particular, an exact representation
\[
K_m(x,y)=(x-y)^2R_m(x,y)
\]
with polynomial/continuous \(R_m\) is impossible.

## 3. Stronger pointwise falsification

For m=1,
\[
P_1(X)=15X^2-1344X+115200
      =3(5X^2-448X+38400).
\]
Its discriminant is
\[
448^2-4\cdot5\cdot38400=-562304<0,
\]
so \(P_1(X)>0\) for all real \(X\). This does not rescue the pointwise-positive route, because off-diagonal evaluations of \(K_1\) have negative values (already established computationally in Frontier 39). It instead gives a clean exact obstruction to any Vandermonde-square factorization.

## 4. Consequence for the proof search

The required inequality
\[
T_m=C^2q_{m+1}^2\iint K_m\,d\nu\,d\nu\ge0
\]
therefore has to be obtained from a *global* property of the theta measure, not from an elementary pointwise-positive raw kernel.

The remaining high-value targets are:
- derive a Gram/operator representation after summing the theta atoms;
- exploit the modular transformation before any positivity claim;
- search for a positive semidefinite correction whose integral vanishes exactly under the theta relation;
- simultaneously prove the stronger degree-3 centered inequality and then its all-degree analogue.

## Status

This is an exact obstruction/certificate, not a proof of RH.
