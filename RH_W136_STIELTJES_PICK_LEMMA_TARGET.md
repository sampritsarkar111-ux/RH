# W136 — Exact Proof-Bearing Lemma Target

## Lemma to prove
Let H be the exact square-root normalization of the completed Riemann Xi function chosen so that under RH its nontrivial zero images are on (-infinity,0]. Prove directly from the theta/Mellin representation, without a zero-location assumption, that

F(z) = -H'(z)/H(z)

is a Stieltjes function:

F(z)=a + integral_0^infinity dnu(t)/(z+t),  a>=0, nu>=0,

on C\(-infinity,0].

## Equivalent analytic tests
It is enough to establish the appropriate normalization plus:
1. F is holomorphic on C\(-infinity,0];
2. F(x)>=0 for x>0;
3. Im F(z)<=0 for Im z>0;
4. F(x)=O(1/x) as x->+infinity (or the exact affine term is identified);
5. the theta-derived boundary measure is positive.

Then the Stieltjes representation theorem supplies the positive measure.

## Why this would close the spectral wall
The poles of F are exactly the zeros of H, with residues equal to their multiplicities. A Stieltjes function has poles only on the non-positive real axis and non-positive residues in the convention above. Therefore every zero of H lies on (-infinity,0], with multiplicity-compatible residues.

The inverse square-root map then gives Re(rho)=1/2.

## Critical warning
This is only a target until the theta integral actually proves the Pick inequality. A representation of F using the unknown zeros is circular and does not count.
