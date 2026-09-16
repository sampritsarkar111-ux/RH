# 2026-09-16 — k=3 exact reciprocal-minor formula

From the fixed-shift Jacobi–Trudi duality,

`D_{r,k}=det(h_{r+j-i})_{i,j=0}^{k-1}`.

For `k=3`, this becomes exactly

`D_{r,3}=h_r^3-2h_{r-1}h_rh_{r+1}+h_{r-1}^2h_{r+2}+h_{r-2}h_{r+1}^2-h_{r-2}h_rh_{r+2}`.

Equivalently, with the determinant displayed,

`D_{r,3}=det[[h_r,h_{r+1},h_{r+2}],[h_{r-1},h_r,h_{r+1}],[h_{r-2},h_{r-1},h_r]]`.

This is the first genuinely higher-order reciprocal obstruction beyond log-concavity. Proving `D_{r,2}>0` alone cannot imply `D_{r,3}>0` without an additional structural theorem.

## New target

Find an Xi-specific inequality implying simultaneous positivity of

`h_r^2-h_{r-1}h_{r+1}`

and

`det[[h_r,h_{r+1},h_{r+2}],[h_{r-1},h_r,h_{r+1}],[h_{r-2},h_{r-1},h_r]]`

uniformly in `r`, preferably through a moment/cumulant or variation-diminishing representation of `1/E(-z)`.

## Barrier

Known coefficient positivity, ordinary log-concavity, finite Jensen hyperbolicity, and finite zero verification do not supply this all-order reciprocal PF condition. Any proposed inequality must be checked against generic positive sequences before being specialized to Xi.

Status: exact algebraic reduction; no infinite positivity proof yet.
