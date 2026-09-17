# Frontier 174A — Stieltjes/Pick Sign Reduction — 2026-09-18

## Exact target
For H(z)=Xi(sqrt(z)), prove RH-independently that

Im(H'(z)/H(z)) <= 0,  Im z>0,

plus analyticity and normalization/growth sufficient for the Stieltjes representation

H'(z)/H(z)=a+∫_[0,∞) dμ(t)/(z+t), μ>=0.

## Why this is decisive
If the representation holds, then for x0>0 the factorial moments
M_n=(-1)^n F^(n)(x0)/n!
form a Hankel Gram matrix. Hence every finite Hankel positivity test follows automatically.

## Critical obstruction
A theta representation for H itself does not automatically imply a sign for the logarithmic derivative. Any proposed proof must control the quotient, not merely the positive theta kernel. In particular, positivity of an integral representation of H does not imply Pick/Stieltjes structure of H'/H.

## Closure condition
The missing theorem must be derived directly from the theta kernel and cannot use the unknown zeros to define μ or a spectral measure. If a single upper-half-plane counterexample to the sign exists, this exact Stieltjes route is false and must be abandoned rather than patched numerically.

## Status
OPEN — target isolated; no unconditional sign theorem obtained in this pass.