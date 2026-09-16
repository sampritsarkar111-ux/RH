# Frontier 45 — All-degree Hermite closure target

Date: 2026-09-16

## Objective

Convert the degree-by-degree Hermite-minor program into an all-degree target. For a real monic polynomial P(x)=x^d+b_1x^(d-1)+...+b_d with roots lambda_i, define power sums s_k=sum_i lambda_i^k and H_d=(s_{i+j})_{0<=i,j<d}. If all roots are real, H_d is positive semidefinite since c^T H_d c=sum_i(sum_j c_j lambda_i^j)^2 >= 0. The converse is governed by the classical Hermite inertia/rank criterion, with degeneracies handled by rank.

## Jensen specialization

For J_{d,n}(X)=sum_{j=0}^d binom(d,j) gamma(n+j) X^j, monic normalization gives b_{d-j}=binom(d,j) gamma(n+j)/gamma(n+d). Hence every Hermite entry is an explicit expression in consecutive gamma-ratios.

## Research target

Find a Riemann-xi-specific mechanism implying the complete Hermite conditions for every d,n, not merely finitely many minors. Generic Stieltjes moment positivity is insufficient, as established by finite positive atomic counterexamples in earlier frontiers.

Desired closure form:

Riemann-specific structural identity/positivity => H_d(J_{d,n}) satisfies the full Hermite hyperbolicity criterion for every d,n.

If obtained, Pólya-Jensen would convert the universal hyperbolicity statement into RH.

## Critical gap

No such all-degree Riemann-specific implication is currently established. Finitely many degrees, fixed-degree asymptotics, or numerical verification do not close the universal gap.

## Parallel directions

1. Theta-kernel total positivity / PF_infinity structure.
2. Heat-equation/de Bruijn-Newman flow and preservation of hyperbolicity.
3. Direct all-degree Jensen-polynomial generating-function identities.
4. Determinant or sum-of-squares representations for Hermite matrices.
5. Rigorous computer algebra for low degrees as theorem discovery and falsification only.

## Status

Structural target established. No complete all-degree closure theorem and no RH proof obtained.
