# Frontier 146 — Exact Two-Copy Kernel Factorisation Gate

Date: 2026-09-17

## Gate

For the exact Pick numerator kernel

K=[a cos(ar)sinh(bp)-b sin(ap)cosh(br)]/[4(a^2+b^2)],

with p=u+v and r=u-v, test the modularly paired two-copy expression before any lattice collapse.

## Required identity

Seek an exact decomposition

P(z)=integral_{u,v>0} |A(z;u,v)|^2 Phi(u)Phi(v) du dv + R_mod(z),

where R_mod is either zero or itself an explicit nonnegative modular remainder.

A weaker but still useful algebraic criterion is divisibility of the symmetrized antisymmetric component by the squared Vandermonde in the even variables:

R(u^2,v^2)=(u^2-v^2)^2 Q(u^2,v^2).

Then Q must have a positive Gram representation.

## Exact obstruction already established

The raw K is sign-changing; for example

a=1, b=1/2, u=1/2, v=2

gives K approximately -0.0548201335.

Thus no proof can assign a positive sign to K termwise.

## Research conclusion

The decisive unresolved calculation is symbolic modular pairing of the unsummed theta lattice. A successful factorization would be a genuine proof-bearing advance. A nonzero signed residual with an explicit negative principal minor would instead rule out this entire two-copy factorization class.
