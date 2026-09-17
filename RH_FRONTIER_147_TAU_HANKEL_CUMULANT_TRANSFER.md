# Frontier 147 — All-Order tau-Hankel: Cumulant Transfer Attack

Date: 2026-09-17

## Exact setup

H(z)=sum_{k>=0} h_k z^k,
F(z)=H'(z)/H(z)=sum_{n>=0} c_n z^n,
tau_n=-c_n/n!.

The map h -> c is nonlinear. Explicitly,

c_0=h_1/h_0,

c_1=2h_2/h_0-(h_1/h_0)^2,

c_2=3h_3/h_0-3h_1h_2/h_0^2+(h_1/h_0)^3,

and higher coefficients are complete Bell-polynomial/cumulant expressions.

## Consequence

Positive Hankel determinants of raw theta moments cannot simply be transferred to tau. The required theorem is a nonlinear total-positivity statement for this cumulant transform.

## Candidate global proof mechanism

If a theta-defined positive spectral measure dnu exists for F after the correct pole-support normalization, then its moment determinants have a Vandermonde-square formula. The remaining algebraic task is to show that the cumulant coordinates tau are related to these spectral moments by a transformation preserving total positivity.

Possible routes:

1. continued-fraction coefficients and Stieltjes moment theory;
2. planar-network/LGV factorization of cumulant minors;
3. multi-copy exponential generating-function factorization;
4. de Branges/Weyl boundary values;
5. direct Bell-polynomial determinant identities.

## Sharp gate

For every N, prove

det(tau_{i+j})_{i,j=0}^{N-1} >= 0

from a theta-only identity, with no reference to the zeros of zeta. It is insufficient to verify finitely many N or to assume Pick positivity.

## Status

The raw theta moment determinant is positive by the exact Vandermonde-square identity. The cumulant/Hankel transfer remains open. Therefore this frontier does not prove RH.