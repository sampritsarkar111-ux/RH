# Strict consecutive-minor reduction

## Result

For
`G(z)=xi(1/2+sqrt(z)/2)=sum_{k>=0} a_k z^k`,
set
`D_{r,k}=det(a_{k+j-i})_{i,j=0}^{r-1}`.

A key correction in this research program is the distinction between **nonnegative** and **strictly positive** consecutive minors.

A finite sequence can have every consecutive Toeplitz minor nonnegative while a non-consecutive minor is negative. Therefore nonnegative consecutive minors alone are not a valid reduction to total positivity.

However, Katkova's Theorem D states that, for a fixed order bound m, if all minors of orders 1,...,m formed from consecutive rows and consecutive columns of the relevant Toeplitz matrix are positive, then all minors of those orders are positive. Hence, after taking every m,

`D_{r,k}>0 for all r>=1,k>=0`

is a valid strict route to `PF_infinity`, and therefore to RH for this genus-zero positive-coefficient xi generating function.

## Why this matters

This removes a false obstruction from the earlier attack. We do not need an independent proof for every arbitrary row/column minor. The research target really is the two-parameter family `D_{r,k}`.

## Independent exact identity

For every r>=2, the consecutive minors satisfy Desnanot-Jacobi:

`D_{r,k} D_{r-2,k} = D_{r-1,k}^2 - D_{r-1,k-1}D_{r-1,k+1}`.

Thus a sufficient bridge from order r-1 to order r is a strict curvature estimate

`D_{r-1,k}^2 > D_{r-1,k-1}D_{r-1,k+1}`.

The crucial requirement is that such an estimate must be proved directly from the xi coefficient structure, not inferred from RH or from a global critical-line zero factorization.

## Current frontier

The 2026 Michalowski preprint proves `D_{r,k}>0` uniformly for `k >= 10^18 r^3`, while explicitly leaving the complementary wedge open. The older Katkova framework proves asymptotic positivity for every fixed order but does not provide a uniform all-order closure.

Therefore the genuine remaining problem is a uniform, non-circular curvature/positivity theorem in the complementary wedge.
