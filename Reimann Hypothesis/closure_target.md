# Closure target after the second attack

The research program is reduced to one non-circular mathematical target:

For
`F(z)=xi(1/2+sqrt(z))=sum_{n>=0} a_n z^n`,
prove that the Toeplitz matrix `T=(a_{j-i})_{i,j>=0}`, with `a_m=0` for `m<0`, is totally nonnegative.

Equivalently, establish nonnegativity of every finite Toeplitz minor. The consecutive minors
`D_{r,k}=det(a_{k+j-i})_{i,j=0}^{r-1}` obey the exact Desnanot-Jacobi identity

`D_{r,k}D_{r-2,k}=D_{r-1,k}^2-D_{r-1,k-1}D_{r-1,k+1}`.

## Important correction

Nonnegativity of **all consecutive minors by itself is not enough** to establish total positivity for a general Toeplitz matrix. A finite counterexample is the coefficient sequence

`a=(2,2,2,2,1)`.

Its consecutive minors `D_{r,k}` are all nonnegative for `1 <= r <= 5` (the rows of values are respectively

`(2,2,2,2,1)`,
`(4,0,0,2,1)`,
`(8,0,0,2,1)`,
`(16,8,4,2,1)`,
`(32,0,8,0,1)`).

Yet the non-consecutive Toeplitz minor using rows `(0,1,2)` and columns `(1,2,4)` equals `-4`:

`det([[2,2,2],[2,2,2],[2,2,1]]) = -4`.

Therefore an RH proof must either control **all** finite Toeplitz minors, or prove an additional structural theorem specific to the Riemann-xi coefficient sequence that reduces all minors to a rigorously controlled family. The Desnanot-Jacobi identity alone does not provide that reduction.

## Genuine closure routes

A complete proof could therefore follow either route:

1. prove all finite Toeplitz minors `>=0` directly;
2. prove a non-circular structural reduction from all minors to a smaller family and then prove that family;
3. prove a non-circular propagation inequality that forces the unresolved wedge from a sufficiently strong tail theorem; or
4. find a different RH-equivalent criterion and prove it without presupposing the location of the nontrivial zeros.

What is not sufficient:
- checking any finite number of zeros;
- checking finitely many Toeplitz minors;
- assuming the global factorisation by critical-line ordinates;
- replacing an infinite bound by numerical evidence.

The current July-2026 tail result `k >= 10^18 r^3` is useful but does not itself close the wedge `k < 10^18 r^3`.
