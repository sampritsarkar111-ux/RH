# Frontier 46 — Exact normalized quartic region analysis

Date: 2026-09-16

From Frontier 43, with u=-v>0, w=2u^(3/2)t, |t|<=1, y=z/u^2, the quartic Hermite determinant is

F(y,t)=y^3-18y^2+81y-216 t^2 y+432 t^2(1-t^2),

with Delta_4=256 u^6 F(y,t).

## Exact endpoint factorizations

At t=0:
F(y,0)=y(y-9)^2.

At t^2=1:
F(y,±1)=y(y^2-18y-135)=y(y-27)(y+5).

The derivative in y is

F_y=3(y^2-12y+27-72t^2).

Therefore any attempt to prove Delta_4>=0 must control the admissible range of y=z/u^2; the cubic alone is not globally nonnegative in y.

## Immediate consequence

The degree-3 cone |t|<=1 does not by itself force quartic Hermite positivity. A quartic closure theorem needs an additional Riemann-specific constraint linking z to v and w.

## Research target

Derive such a constraint from the explicit Riemann theta kernel, rather than from generic positive-measure moment inequalities. Candidate forms include a sharp upper/lower envelope for z/u^2 as a function of t, or a direct sum-of-squares identity for F on the Riemann-admissible region.

## Status

Exact reduction established; admissible-region closure remains open. No RH proof obtained.
