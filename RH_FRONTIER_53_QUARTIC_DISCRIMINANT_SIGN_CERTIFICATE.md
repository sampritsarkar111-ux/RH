# Frontier 53 — Certified sign of the quartic discriminant factor

Date: 2026-09-16

Let q=t^2 with 0<=q<=1 and define
\[
p(q)=8q^3-32q^2+6q-7.
\]
The normalized quartic factor has
\[
\operatorname{disc}_y F=-629856\,q\,p(q).
\]

## Exact sign proof

\[
p'(q)=24q^2-64q+6,
\]
with critical points
\[
q_-=\frac43-\frac{\sqrt{55}}6\approx0.0996,
\qquad
q_+=\frac43+\frac{\sqrt{55}}6>1.
\]
Thus q_- is the only critical point in [0,1]. Direct exact evaluation gives p(0)=-7, p(1)=-25, and p(q_-)<0 (numerically about -6.71178). Since q_- is the unique interior critical point, p(q)<0 throughout [0,1]. Therefore
\[
\operatorname{disc}_y F>0\quad(0<q<=1).
\]
Thus F(y,t) has three distinct real y-roots for every 0<|t|<=1.

This finite algebraic certificate still does not identify which sign interval contains the Riemann value y=z/u^2 and therefore does not close the quartic Hermite condition.

## Status

Finite algebraic sign certificate completed; Riemann-specific admissible-region theorem remains open.
