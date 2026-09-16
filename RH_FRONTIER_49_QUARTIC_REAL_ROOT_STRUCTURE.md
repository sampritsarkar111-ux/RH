# Frontier 49 — Quartic normalized real-root structure

Date: 2026-09-16

Let
\[
F(y,t)=y^3-18y^2+(81-216t^2)y+432t^2(1-t^2),\qquad |t|\le1.
\]

This is the normalized degree-4 Hermite determinant factor from Frontier 46.

## Exact discriminant in y

Writing q=t^2 gives
\[
\operatorname{disc}_y F=-629856\,q(8q^3-32q^2+6q-7).
\]
The cubic factor has exactly one real root,
\[
q_*\approx3.86451576899047,
\]
which lies outside the admissible interval 0<=q<=1. Hence for every 0<|t|<=1, the cubic F(y,t) has three distinct real critical-parameter roots as a polynomial in y only when its discriminant is positive; since the displayed discriminant is positive throughout 0<q<=1, F has three distinct real roots in y.

At q=0, F=y(y-9)^2 has a repeated root.

## Important interpretation

The determinant condition Delta_4>=0 is therefore not equivalent to a simple global sign condition on y: because F is a cubic with three real roots for 0<|t|<=1, its sign alternates between the roots. A successful quartic closure must prove that the Riemann-admissible y=z/u^2 lies in one of the nonnegative intervals.

This sharpens Frontier 46: the missing theorem can be formulated as an admissible-region theorem for (t,y), rather than as a vague quartic positivity assertion.

## Status

Exact real-algebraic structure established. The Riemann-specific bound placing y in a valid interval remains unproved. No RH proof obtained.
