# Closure target after the second attack

The research program is reduced to one non-circular mathematical target:

For
`F(z)=xi(1/2+sqrt(z))=sum_{n>=0} a_n z^n`,
prove that the Toeplitz matrix `T=(a_{j-i})_{i,j>=0}`, with `a_m=0` for `m<0`, is totally nonnegative.

Equivalently, establish nonnegativity of every finite Toeplitz minor. The consecutive minors
`D_{r,k}=det(a_{k+j-i})_{i,j=0}^{r-1}` obey the exact Desnanot-Jacobi identity

`D_{r,k}D_{r-2,k}=D_{r-1,k}^2-D_{r-1,k-1}D_{r-1,k+1}`.

A complete proof could therefore follow either route:

1. prove all `D_{r,k}>=0` directly;
2. prove a non-circular propagation inequality that forces the unresolved wedge from a sufficiently strong tail theorem; or
3. find a different RH-equivalent criterion and prove it without presupposing the location of the nontrivial zeros.

What is not sufficient:
- checking any finite number of zeros;
- checking finitely many Toeplitz minors;
- assuming the global factorisation by critical-line ordinates;
- replacing an infinite bound by numerical evidence.

The current July-2026 tail result `k >= 10^18 r^3` is useful but does not itself close the wedge `k < 10^18 r^3`.
