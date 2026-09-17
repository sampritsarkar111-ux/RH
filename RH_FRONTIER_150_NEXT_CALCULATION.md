# Frontier 150 — Next Exact Calculation

## Goal
Attack the global Pick wall first, because a successful theta-derived Pick/Stieltjes theorem would directly produce the spectral/Hankel mechanism needed by the existing rigidity chain.

## Calculation protocol
1. Start from the exact double-integral formula for Im(H'/H) already recorded in the Frontier 143 issue.
2. Substitute the complete unsummed Riemann theta series for both kernel factors.
3. Expand as a finite lattice truncation indexed by all theta indices; do not collapse the lattice prematurely.
4. Apply the Jacobi/Poisson transformation to the entire paired block.
5. Collect terms into symmetric and antisymmetric index orbits.
6. Compute the exact numerator for each orbit.
7. Search symbolically for Vandermonde-square, modulus-square, or resolvent forms.
8. Prove positivity orbit-by-orbit if possible.
9. If a residual remains, derive its exact sign/size and test whether it can be absorbed by a second modular pairing.
10. Only after finite truncations are controlled, prove local-uniform convergence to the infinite expression.

## Failure protocol
If the required global sign cannot be obtained, do not promote a heuristic factorization. Record the smallest exact obstruction and use it to redesign the route.

## Parallel backup
In parallel, perform the same structural audit on the nonlinear tau-Hankel and all-degree Jensen forms, while independently testing the de Branges, Li/Weil, and Nyman–Beurling constructions.

## Success criterion
An unconditional inequality with a complete proof, or a rigorous obstruction theorem. Neither finite numerics nor an RH-equivalent reformulation counts as closure.
