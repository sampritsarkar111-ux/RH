# Frontier 55 — Quartic root-localization target

Date: 2026-09-16

## Exact normalized quartic

With u=-v>0, w=2u^(3/2)t, y=z/u^2 and |t|<=1, the quartic Hermite determinant reduces to

F(y,t)=y^3-18y^2+(81-216t^2)y+432t^2(1-t^2).

## New exact observation

Writing q=t^2, the y-discriminant is

Disc_y F = -629856 q(8q^3-32q^2+6q-7).

The cubic h(q)=8q^3-32q^2+6q-7 is strictly negative on 0<=q<=1 because h'(q)=24q^2-64q+6 has its positive critical point below 1/2, and direct endpoint/critical-point evaluation remains negative. Therefore Disc_y F>0 for 0<q<=1.

Thus for every nondegenerate cubic-cone parameter t, F has three distinct real y-roots. The quartic closure problem is consequently an interval-localization problem: prove that the actual Riemann value y=z/u^2 lies in a region where F>=0, using Riemann-specific structure.

## Critical warning

Disc_y F>0 does not prove F(y,t)>=0 at the Riemann point. It only determines the root topology. Likewise, Delta_4>=0 alone is not a complete real-rootedness criterion without the other Hermite conditions/rank information.

## Next target

Obtain an exact inequality for y from the Riemann theta kernel, heat flow, or a total-positivity property, and compare it against the three explicit roots of F. Then seek an all-degree analogue.