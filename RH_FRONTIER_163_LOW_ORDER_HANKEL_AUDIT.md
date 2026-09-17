# RH Frontier 163 — Low-Order Factorial Hankel Audit — 2026-09-17

Using the coefficient values already recorded in the research ledger, the factorial Hankel matrices

K_N = [(-1)^(i+j)c_(i+j)/(i+j)!]_{i,j=0}^N

were independently recomputed for N=1,2,3.

Results:

- N=1 determinant ≈ 1.949335554819144e-9
- N=2 determinant ≈ 2.172810510526271e-22
- N=3 determinant ≈ 1.177581716013020e-41

The corresponding numerical eigenvalues are nonnegative to the displayed precision:

- N=1: approximately 8.43684e-8, 2.31050529e-2
- N=2: approximately 1.11461e-13, 8.43706e-8, 2.31050529e-2
- N=3: approximately 5.41937e-20, 1.11467e-13, 8.43706e-8, 2.31050529e-2

Interpretation: this supports the previously recorded diagnostic pattern, but it does NOT prove all-order PSD, a Stieltjes representation, or RH. The next proof-bearing task is an exact theta-derived Gram/SOS identity valid for every N.
