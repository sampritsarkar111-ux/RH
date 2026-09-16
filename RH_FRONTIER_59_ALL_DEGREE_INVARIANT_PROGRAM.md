# Frontier 59 — All-degree centered-invariant program

Date: 2026-09-16

## Objective

Replace degree-by-degree discriminant calculations with a uniform theorem on centered Jensen invariants.

For degree d, write the monic Jensen polynomial after translation by its first normalized coefficient. The resulting centered coefficients are translation-invariant polynomial combinations of consecutive gamma ratios. Hyperbolicity is equivalent to positive semidefiniteness of the associated Hermite matrix (with the usual rank interpretation for repeated roots).

## Required universal statement

For every n,d, the centered Jensen polynomial must have a real-rootedness certificate. Equivalently, all principal Hermite minors must satisfy the required nonnegativity/rank conditions.

The degree-3 and degree-4 calculations show that the first constraints involve (v,w,z); degree 5 introduces h. In general new centered invariants appear at every degree. Therefore a successful proof must either:

1. derive a closed recurrence/inequality system for all centered invariants from the Riemann theta kernel;
2. prove a stronger total-positivity / Pólya-frequency property of the relevant kernel that implies every Jensen polynomial is hyperbolic; or
3. construct another global spectral/operator theorem implying the same hyperbolicity directly.

## Falsification gate

Any proposed recurrence must be tested against:
- exact algebra for low degrees;
- the known positive theta-kernel representation;
- scale/asymptotic behavior of gamma ratios;
- generic positive-measure counterexamples, to ensure the argument uses genuinely Riemann-specific structure.

A finite list of inequalities, numerical checks, or fixed-degree theorem is not the universal closure.

## Immediate next targets

A. Express the degree-d centered coefficients directly as finite-difference polynomials in R_m=gamma_{m+1}/gamma_m.

B. Search for a kernel-level property implying the complete Hermite hierarchy rather than proving each minor independently.

C. Determine whether heat-flow/de Bruijn-Newman structure can supply the missing global sign mechanism.

D. If a universal theorem is found, write the implication chain explicitly to RH and independently audit every quantifier.

## Status

Research target only; no complete proof has been established.