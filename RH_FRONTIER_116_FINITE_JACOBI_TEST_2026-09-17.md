# RH Frontier 116 — Finite Jacobi Recurrence Target — 2026-09-17

## Core idea
For each truncation N, seek a real symmetric tridiagonal matrix J_N generated directly from the theta lattice, with
\[
P_N(\lambda)=\det(\lambda I-J_N),
\]
and recurrence
\[
P_{k+1}(\lambda)=(\lambda-a_k)P_k(\lambda)-b_k^2P_{k-1}(\lambda),\qquad b_k>0.
\]
Such a recurrence gives real simple zeros for every finite P_N by standard Sturm theory.

## RH bridge that must still be proved
The finite polynomials must converge to a canonical entire function proportional to Xi after the correct spectral variable change. One must prove convergence locally uniformly, identify the limiting zeros with the nontrivial zeta zeros, and prove no non-real zeros survive in the limit.

## Theta-specific requirement
The coefficients a_k and b_k must be derived from the completed theta lattice/modular transformation itself. Choosing them from numerically observed zeros is forbidden. Likewise, positivity of b_k must be established symbolically or by a theorem whose hypotheses are verified from the theta kernel.

## Falsification gate
If no exact theta-derived Jacobi representation exists, this route does not prove RH. In particular, arbitrary entire functions with real Taylor moments can have non-real zeros, so moment positivity alone cannot substitute for the missing spectral construction.

## Status
Research target only; no RH proof claimed.
