# Fixed-shift duality: exact identity and the real closure target

For `E(z)=sum_{n>=0} e_n z^n`, `e_0=1`, define

`1/E(-z)=sum_{n>=0} h_n z^n`.

For

`D_{r,k}=det(e_{k+j-i})_{i,j=0}^{r-1}`,

Jacobi–Trudi gives

`D_{r,k}=det(h_{r+j-i})_{i,j=0}^{k-1}`.

This was checked numerically against the Xi-kernel coefficients for `1<=r,k<=6`; the maximum floating-point discrepancy in the current finite test was below `9e-17` after the same normalization.

## New observation

The dual form means that for **fixed shift k**, positivity for arbitrarily large determinant order `r` is equivalent to positivity of a fixed-size `k x k` determinant sampled along the reciprocal-coefficient sequence `h_n`.

A sufficient condition is strict log-concavity in the Toeplitz-determinant sequence itself,

`D_{r,k}^2 > D_{r,k-1}D_{r,k+1}`,

because Desnanot–Jacobi then yields the next-order positivity once the lower orders are positive.

Numerically, the current Xi coefficient truncation gives positive curvature. For normalized coefficients, the smallest tested curvature ratios

`D_{r,k}^2/(D_{r,k-1}D_{r,k+1})`

for `r=1,...,5` and `k=1,...,5` were respectively greater than approximately `1.25, 1.53, 1.83, 2.17, 2.55` at the smallest displayed k-range. These are finite numerical observations only.

## Critical warning

The curvature inequality is not yet proved. It is essentially the exact obstruction encoded by Desnanot–Jacobi, so numerical positivity cannot be promoted to an infinite theorem without a new analytic mechanism.

The next rigorous target is therefore to prove a lower bound for this curvature ratio from the explicit Xi coefficient/kernel representation, with no appeal to RH, critical-line zero factorization, or finite zero verification.
