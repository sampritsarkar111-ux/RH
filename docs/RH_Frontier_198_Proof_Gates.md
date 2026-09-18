# RH Frontier 198 — Proof-Gate Attack and Failure Analysis

Date: 2026-09-18

## Purpose

Turn Frontier 197 into explicit theorem obligations. No claim here proves RH.

## Gate P: Positive factorization

Define the exact Weil quadratic form on an admissible class A. The target is

Q(f)=||Tf||^2+R(f), R(f)>=0,

with T and R constructed without zero locations, and prove Q=W_xi exactly.

A candidate factorization is acceptable only after:
1. domain/completeness is proved;
2. every prime term is represented exactly;
3. the Gamma/archimedean term is represented exactly;
4. boundary terms vanish or are explicitly included;
5. equality survives the infinite limit;
6. positivity is uniform on A.

## Gate O: orbit separation

For each hypothetical off-line zero orbit O(rho), construct g_rho in A and epsilon(rho)>0 such that

W_O(g_rho)<=-2 epsilon,
|W_rest(g_rho)|<=epsilon.

The hard theorem is uniform control of the rest. A calculation for one hypothetical rho is not enough.

## Gate J: Jensen hyperbolicity

For degree 3,

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2.

With x=r-1,y=q-1,

F=(x-y)^2-2xy(x+y)-3x^2y^2.

This reveals a candidate invariant: adjacent-ratio anisotropy (x-y)^2 versus cubic/quartic damping. A future theorem should control this invariant along the complete Turan-ratio trajectory of xi.

## New lemma target: Ratio-variation barrier

Let r_n=gamma_{n+1}^2/(gamma_n gamma_{n+2}). Seek a Riemann-specific inequality of the form

|r_{n+1}-r_n|^2 <= C_n (r_n-1)(r_{n+1}-1)

with an explicit C_n strong enough to imply every required Jensen polynomial is hyperbolic. The inequality must be derived from xi, not assumed from RH.

This is a concrete bridge between local Turan data and all-degree Jensen hyperbolicity.

## Gate A: Anti-circularity

Every proposed theorem must be annotated by dependency:
- arithmetic only;
- functional equation only;
- unconditional zero-free information;
- numerical evidence;
- RH-equivalent assumption.

Any use of RH or an equivalent positivity statement inside the proof of the same positivity statement is rejected.

## Computational protocol

For every finite certificate record precision, exact/interval arithmetic, truncation, tail bound, and an independently reproducible implementation. Computation can discover lemmas but cannot close an infinite theorem by itself.

## Current conclusion

The remaining work is concentrated into P, O, and J. Frontier 198 therefore changes the workflow from 'invent another representation' to 'prove one of three explicit global inequalities.' Numeral systems remain available as coordinate systems, but no encoding is accepted as a proof mechanism without an independent analytic theorem.