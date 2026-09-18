# Frontier 184 — Independent RH Approaches

Date: 2026-09-18

Status: partial. This is a research frontier, not a claim that RH has been proved.

## Parallel approaches

### 1. Nyman–Beurling–Báez–Duarte
Construct an SDTNS-derived family whose Mellin transforms can be shown to have the required density/completeness property. The proof-bearing object is the density theorem, not a finite numerical approximation.

### 2. Li coefficients
Seek an exact SDTNS/arithmetic representation of the Li coefficients. RH is equivalent to positivity of all Li coefficients, so an unconditional proof must establish the exact identity and positivity for every index.

### 3. de Branges
Seek a genuine de Branges Hilbert-space realization with an exact correspondence between the completed xi function and the relevant Hermite–Biehler structure. Self-adjointness alone does not establish the required zero correspondence.

### 4. Weil positivity
Prove an explicit map from SDTNS coefficient vectors to admissible Weil test functions for which the SDTNS quadratic form equals the Weil quadratic form, including prime and archimedean terms.

### 5. No-go / invariant route
If the proposed arithmetic kernel cannot reproduce the required Weil/Mellin structure, test incompatible invariants: Euler local factors, gamma factor, functional-equation symmetry, growth order, pole/zero structure, and test-function class. A rigorous obstruction is preferable to an unjustified identification.

## Computational check

Wolfram evaluated a finite SDTNS local prime-power block at p=2 and t=1, producing the real symmetric matrix

{{1., -1., 1., -1.},
 {-1., 1.618503137801576, -1.618503137801576, 1.618503137801576},
 {1., -1.618503137801576, 1.764844680504541, -1.764844680504541},
 {-1., 1.618503137801576, -1.764844680504541, 1.7780904491473626}}.

This verifies only a finite numerical evaluation of the local formula; it is not evidence sufficient to prove RH.

## Literature-search note

SciSpace was used to locate recent literature discussing Nyman–Beurling/Báez–Duarte, Mellin/model-space, and operator-theoretic formulations. Search results may contain unverified claims of proofs; such claims are not adopted as established mathematics without independent verification.

## Current decisive gates

1. Exact SDTNS-to-Mellin transform.
2. Exact Euler-product/local-factor correspondence.
3. Exact archimedean/gamma correspondence.
4. Exact SDTNS-to-Weil quadratic-form identity, or a rigorous no-go theorem.
5. Independent RH-equivalent positivity/density/spectral theorem.
6. Analytic continuation and all domain/limit interchanges.
7. Final implication to RH with no circular use of RH.

Conclusion: Frontier 184 broadens the attack beyond generic PSD kernels while preserving strict anti-circularity. RH remains open.
