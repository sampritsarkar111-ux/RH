# RH Frontier 138 — Explicit Four-Index Theta-Kernel Factorization

Date: 2026-09-17

## 1. Objective

The previous frontier reduced the missing Pick sign to an unsummed theta double integral but showed that the pointwise antisymmetric kernel is not sign-definite. The next proof-bearing calculation is the first genuinely four-copy factorization: compute the degree-4 Hankel determinant of the theta moment functional directly from the unsummed theta kernel.

This is a rigorous positive factorization, but it must not be confused with the still-missing bridge from theta moments to the transformed zeta-zero moments `tau_n`.

## 2. Unsummed theta weight

Use

`Phi(u) = sum_{n>=1} (4*pi^2*n^4*exp(9u/2) - 6*pi*n^2*exp(5u/2)) exp(-pi*n^2*exp(2u))`,

for `u >= 0`.

Every summand is positive because

`4*pi^2*n^4*exp(9u/2) - 6*pi*n^2*exp(5u/2) = 2*pi*n^2*exp(5u/2)*(2*pi*n^2*exp(2u)-3) > 0`.

Define the theta moments

`M_k = integral_0^infinity Phi(u) u^(2k) du`,  k >= 0.

Then `M_k > 0`.

## 3. Four-copy determinant identity

Let

`G_4 = (M_{i+j})_{0 <= i,j <= 3}`.

By expanding the determinant and applying the multilinearity of integration,

`det(G_4) = 1/4! * integral_{(0,infinity)^4} prod_{r=1}^4 Phi(u_r) * det[(u_r^2)^j]_{r,j=1}^4^2 du_1...du_4`.

The Vandermonde determinant is

`det[(u_r^2)^j]_{r,j=0}^3 = prod_{1 <= r < s <= 4} (u_s^2-u_r^2)`.

Therefore the exact factorization is

`boxed{ det(G_4) = 1/24 * integral_{(0,infinity)^4} [prod_r Phi(u_r)] [prod_{r<s}(u_s^2-u_r^2)^2] du_1...du_4 >= 0. }`

Strict positivity holds because `Phi(u)>0` on a set of positive measure and the Vandermonde square is nonzero off the coincidence hyperplanes `u_r=u_s`.

## 4. Fully unsummed four-index lattice form

Insert

`Phi(u_r) = sum_{n_r>=1} P_{n_r}(u_r) exp(-pi*n_r^2*exp(2u_r))`,

where

`P_n(u)=4*pi^2*n^4*exp(9u/2)-6*pi*n^2*exp(5u/2)`.

Then, by absolute convergence,

`det(G_4) = 1/24 * sum_{n_1,n_2,n_3,n_4>=1} I(n_1,n_2,n_3,n_4)`,

with the explicit four-index kernel

`I(n_1,n_2,n_3,n_4)`

`= integral_{(0,infinity)^4} [prod_{r=1}^4 P_{n_r}(u_r) exp(-pi*n_r^2*exp(2u_r))] [prod_{r<s}(u_s^2-u_r^2)^2] du_1...du_4`.

Every individual `I(n_1,n_2,n_3,n_4)` is nonnegative, and it is positive for every fixed positive integer quadruple because each `P_n(u)>0` and the Vandermonde square is positive away from a null set.

Thus the four-index theta lattice has an exact positive decomposition:

`boxed{ I(n_1,n_2,n_3,n_4) >= 0 }`.

## 5. Why this is useful

This closes the four-copy positivity calculation for the intrinsic theta moment functional. It is stronger than checking only the first few determinants numerically: the factorization is exact and degree-specific, and the same Andreief/Vandermonde argument extends to arbitrary degree `d`.

For general `d`,

`det(M_{i+j})_{i,j=0}^{d-1} = 1/d! * integral prod_r Phi(u_r) * prod_{r<s}(u_s^2-u_r^2)^2 du_1...du_d >= 0`.

No zeta-zero locations are used in this identity.

## 6. Critical wall that remains

This does **not** yet prove RH. The moments `M_k` are moments of the positive theta measure `Phi(u)du` in the variable `u^2`. The RH rigidity theorem requires positivity of the different sequence

`tau_n = sum_rho v_rho^(n+1)`,  with `v_rho=-(rho-1/2)^(-2)`.

The missing bridge is an exact, RH-independent identity or positive transform converting the theta moment functional into these zero-node moments. Without that bridge, positivity of `G_4` is only intrinsic theta positivity and cannot be substituted for positivity of the `tau` Hankel matrices.

## 7. Pick-route connection

The four-copy factorization is also not, by itself, a proof of the Pick inequality for `F=H'/H`. The Pick numerator contains the oscillatory/nonlocal kernel from Frontier 137. The Vandermonde square controls a determinant of polynomial moments; it does not automatically control the complex logarithmic derivative.

Therefore the next genuinely decisive calculation is to test whether the four-copy positive form can be coupled to the Pick numerator through an exact transform identity, or whether a residual term survives.

## Status

**PROVED:** exact four-copy theta moment determinant identity; explicit four-index unsummed lattice kernel; termwise nonnegative Vandermonde-square factorization; strict positivity of the degree-4 theta Hankel determinant; general-degree analogue.

**NOT PROVED:** the theta-to-`tau_n` positivity bridge; the global Pick sign; RH.

**Next target:** derive an exact four-index transform identity linking this positive theta Gram form to the zero-node Hankel form, with every residual retained rather than discarded.