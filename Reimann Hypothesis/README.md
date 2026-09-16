# Riemann Hypothesis research attack

Date: 16 September 2026

This folder records a rigorous research attempt based on a Pólya-frequency / total-positivity reformulation of RH.

**Important status:** this work does **not** claim a proof of RH. Clay currently lists RH as unsolved. The manuscript gives an exact reduction to total nonnegativity of a Toeplitz matrix, a Desnanot-Jacobi determinant hierarchy, a candidate propagation lemma, finite numerical stress tests, and an explicit description of the remaining infinite wedge.

Files:
- `Riemann_Hypothesis_Total_Positivity_Attack.pdf` — complete research manuscript generated and rendered/visually checked locally
- `rh_total_positivity_attack.tex` — repository source placeholder for the manuscript build
- `verify_rh_finite_tests.py` — reproducible high-precision kernel-moment, Jensen-polynomial, and finite Toeplitz-minor tests

The July 2026 preprint by Wojciech Michalowski proves positivity of consecutive Toeplitz minors in the tail `k >= 10^18 r^3`, while explicitly leaving the complementary region as the RH-relevant obstruction. See the manuscript for the exact citation and proof architecture.
