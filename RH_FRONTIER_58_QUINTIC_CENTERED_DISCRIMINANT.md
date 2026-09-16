# Frontier 58 — Exact centered quintic discriminant

Date: 2026-09-16

## 1. Degree-5 Jensen normalization

For consecutive coefficient ratios r_j=q_j/q_0, the monic degree-5 Jensen polynomial is

P(x)=x^5+5r_1x^4+10r_2x^3+10r_3x^2+5r_4x+r_5.

Put a=r_1 and shift x=y-a. Define

v=r_2-a^2,

w=r_3-3ar_2+2a^3,

z=r_4-4ar_3+6a^2r_2-3a^4,

h=r_5-5ar_4+10a^2r_3-10a^3r_2+4a^5.

Then exactly

P(y-a)=y^5+10v y^3+10w y^2+5z y+h.

The translation parameter a disappears.

## 2. Exact discriminant

Symbolic elimination gives

Disc(P)=3125 D_5(v,w,z,h),

where

D_5 = h^4 -120h^3vw +3456h^2v^5 -1440h^2v^3z +2640h^2v^2w^2 +160h^2vz^2 +360h^2w^2z
      -11520hv^4wz +5120hv^3w^3 +4480hv^2wz^2 -10080hvw^3z +3456hw^5 -640hwz^3
      +6400v^4z^3 -3200v^3w^2z^2 -2560v^2z^4 +5760vw^2z^3 -2160w^4z^2 +256z^5.

This is an exact algebraic obstruction for five real roots. It is necessary for hyperbolicity, but by itself is not sufficient; the full Hermite conditions/rank structure remain required.

## 3. Scale-normalized quintic target

Under the cubic-cone parametrization

v=-u,  u>0,
w=2u^(3/2)t,  |t|<=1,
z=u^2 y,
h=u^(5/2)s,

the discriminant factor is

Disc(P)/(3125 u^10)=K(y,t,s),

with

K = s^4 +240s^3t -160s^2y^2 +1440s^2yt^2 +1440s^2y +10560s^2t^2 -3456s^2
    -1280sy^3t +8960sy^2t +80640syt^3 -23040syt +110592st^5 -40960st^3
    +256y^5 -2560y^4 -23040y^3t^2 +6400y^3 -34560y^2t^4 +12800y^2t^2.

Thus degree 5 introduces one genuinely new normalized invariant s. Any attempted all-degree closure must control this higher centered moment jointly with (u,t,y), rather than relying only on the quartic variables.

## 4. New hard target

A complete RH proof through the Jensen/Hermite route would require a Riemann-specific theorem constraining the entire sequence of centered invariants, beginning with (u,t,y,s) and continuing at every degree, sufficiently to force every Jensen polynomial to be hyperbolic.

The quintic calculation therefore strengthens the gap diagnosis: low-degree quartic closure cannot simply be extrapolated without controlling new higher-order centered data.

## 5. Status

Exact symbolic result verified algebraically. No RH proof obtained. Numerical evidence or finite-degree certification must not be promoted to a universal proof.