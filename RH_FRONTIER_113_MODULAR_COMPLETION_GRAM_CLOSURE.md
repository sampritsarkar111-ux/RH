# RH Frontier 113 — Modular Completion, Gram Closure, and the Exact Remaining Theorem

Date: 2026-09-16

## Objective

Close the remaining gap after the exact degree-six / four-copy `d=3` theta-kernel calculation. The endpoint is an unconditional proof that the completed Riemann kernel has the total-positivity or stability structure needed for all Jensen polynomials, hence RH.

## Exact target

Let `Xi(t) = xi(1/2 + i t)`. The RH is equivalent to the assertion that the completed xi-function has only real zeros, and a powerful equivalent route is membership in the Laguerre–Pólya class. A Jensen-polynomial formulation requires hyperbolicity for every degree and shift.

The current theta program has reduced the low-degree problem to exact theta moments and a four-copy symmetrized kernel. The degree-six object is not pointwise positive in the form required for a direct Gram certificate.

## New closure distinction

A positive Gram/SOS representation of one fixed finite-degree kernel does **not** by itself imply real-rootedness. The missing implication is

`positive Gram/SOS -> hyperbolicity`,

which is false for arbitrary polynomial families.

Therefore the next proof-bearing object must contain a root-location mechanism. Adequate candidates are:

1. a Pólya-frequency / total-positivity theorem for the completed translation kernel;
2. an explicitly stability-preserving operator whose symbol is the completed theta kernel; or
3. an all-degree modular Gram identity whose positivity is itself tied to a stability/hyperbolicity theorem.

## Modular-completion requirement

Theta inversion supplies exact functional symmetry, but symmetry alone does not imply positivity of the residual. The desired identity has schematic form

`K_completed = G*G + R`,

with `R` independently positive semidefinite for every admissible scale and matrix size, and with the Gram structure implying hyperbolicity rather than merely coefficient positivity.

## Adversarial checks

Every proposed closure must survive:

- arbitrary finite truncation size;
- every degree, not only `d <= 3`;
- the theta zero-mode;
- all boundary terms under inversion;
- exact normalization factors;
- conjugate zero pairs without assuming critical-line location;
- no parametrization `z_m = -t_m^2` with real `t_m` before RH;
- no unproved positive-mixture/stability-preservation theorem;
- no inference from finite numerical positivity to the infinite theorem.

## Exact remaining theorem

### Route A — total positivity

Prove a sufficiently strong PF-infinity / strict total-positivity statement for the completed Riemann translation kernel, strong enough to imply hyperbolicity of every Jensen polynomial.

### Route B — stability operator

Construct an explicit stability-preserving transform `T_Xi` determined by the completed theta kernel and prove that every Jensen polynomial is obtained from a stable seed by `T_Xi`.

### Route C — all-degree modular Gram identity

For every degree `d`, shift `n`, and real vector `c`, express the exact Hermite/Jensen obstruction as a convergent modularly completed Gram form with a manifestly nonnegative remainder, while proving the additional stability implication.

## Status

This frontier is a rigorous narrowing of the remaining mathematical wall. It is **not** a claim that RH has been proved. The purpose is to prevent the program from repeatedly replacing the missing root-location theorem by positivity statements that are too weak.
