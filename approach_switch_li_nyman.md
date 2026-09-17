# RH research pivot: Li–Weil–Nyman–Beurling

## Status
This file records a rigorous change of attack after the theta/Laguerre Jensen route reached an unresolved all-degree hyperbolicity wall. No step here assumes RH.

## Primary target
Seek an unconditional proof through RH-equivalent criteria, with three independent routes:

1. **Li coefficients:** derive exact zero-free formulas and seek a manifestly nonnegative decomposition for every Li coefficient.
2. **Weil positivity:** derive the explicit-formula quadratic form and seek an exact positive-semidefinite/Gram representation on the full admissible test-function space.
3. **Nyman–Beurling:** construct admissible approximants whose L2 distance to 1 tends to zero, proving the required density theorem rather than relying on finite numerical convergence.

## Non-circularity rules
- Do not assume RH or that all Xi zeros are real.
- Do not assume a self-adjoint Hilbert–Polya operator without constructing and verifying it.
- Do not treat finite-degree positivity, numerical zero checks, or asymptotic evidence as an all-degree theorem.
- Every positivity decomposition must be exact and valid on the full required domain.
- Any failed identity must be retained with its exact residual/obstruction.

## Immediate mathematical program
For Li's coefficients use the exact criterion
\[
\lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right],
\]
with the standard symmetric/analytic interpretation, and independently derive the equivalent derivative representation from the completed zeta function. The next target is an explicit prime/gamma/theta-side representation whose sign can be analyzed without assuming RH.

For Weil's criterion, derive the explicit formula for the admissible test-function class and identify whether its quadratic form can be written exactly as \(\|Tg\|^2\), with no hidden RH input.

For Nyman–Beurling, formulate the relevant closed subspace in \(L^2(0,1)\), prove all approximants belong to it, and search for a constructive sequence with an exact norm estimate tending to zero.

## Decision rule
If a proposed lemma reduces to an RH-equivalent positivity statement without proving that positivity, mark it `open` or `critical_obstruction` rather than promoting it to a theorem.
