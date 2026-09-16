# Frontier 64 — Quintic Hermite determinant equals the exact discriminant

Date: 2026-09-16

For the centered monic quintic

P(y)=y^5+10v y^3+10w y^2+5z y+h,

let p_k be the Newton power sums of its five roots and H=(p_{i+j})_{0<=i,j<=4} the 5x5 Hermite matrix.

Direct symbolic Newton-sum elimination gives

 det(H)=3125 D_5(v,w,z,h),

where D_5 is exactly the centered discriminant polynomial recorded in Frontier 58.

This is a useful structural check: the degree-5 discriminant obstruction is not an unrelated calculation; it is precisely the top Hermite principal minor in this normalization.

Consequently, for five distinct real roots, H is positive definite and D_5>0. Conversely, positivity/rank conditions on the full Hermite matrix provide the appropriate real-rootedness certificate; the top determinant alone remains insufficient.

The same strategy suggests an all-degree algebraic program: derive centered Jensen polynomials, form their Hermite matrices from Newton sums, and search for a Riemann-specific mechanism proving positive semidefiniteness for every degree. The obstacle is not algebraic definability but obtaining uniform inequalities for all centered invariants.

Status: exact finite-degree result; no universal RH closure.