# 2026-09-16 — Exterior-power tail attack

## Objective

Extend the fixed-shift duality beyond k=2 in a way that can potentially use the verified-zero/core-versus-tail strategy without assuming RH for the unverified zeros.

Let

`E(z)=sum_{n>=0} e_n z^n`, `e_0=1`, and

`1/E(-z)=sum_{n>=0} h_n z^n`.

The exact Jacobi–Trudi duality is

`D_{r,k}=det(h_{r+j-i})_{i,j=0}^{k-1}`.

Thus, for each fixed k, the entire vertical line `{D_{r,k}: r>=k}` is a Toeplitz-minor positivity problem for the reciprocal sequence h.

## New structural observation

Suppose one can factor the reciprocal generating function as

`1/E(-z)=H_core(z) H_tail(z)`.

At the Toeplitz-matrix level this is multiplication

`T(h)=T(h_core) T(h_tail)`.

If both factors are totally nonnegative, Cauchy–Binet gives total nonnegativity of T(h), hence positivity of every D_{r,k} (subject to strictness conditions). This is an exact algebraic mechanism; it is not merely a coefficientwise perturbation estimate.

For a finite collection of rigorously known negative real zeros of E, the corresponding reciprocal factors have positive coefficients and their Toeplitz matrices are PF-infinite. Therefore the core factor is structurally safe.

## Critical obstruction

The unverified tail factor cannot be assumed PF-infinite. Saying that its coefficients are positive is insufficient: a positive coefficient sequence can have negative Toeplitz minors. Likewise, small coefficient mass does not automatically preserve every determinant sign, because the target family has unbounded order k and r and no uniform determinant margin is known.

Therefore the correct all-order tail target is stronger than Kessler's k=1 coefficient positivity:

> Prove that the unverified tail reciprocal factor is a PF-infinite multiplier, or prove an order-uniform exterior-power domination inequality strong enough to preserve every Toeplitz minor.

This formulation avoids the circular statement that all unverified zeros are real.

## Exterior-power formulation

For every k, positivity of all k x k Toeplitz minors is positivity of the matrix action on the kth exterior power. If

`A=A_core A_tail`,

then

`wedge^k A = (wedge^k A_core)(wedge^k A_tail)`.

A possible closure would therefore be an operator inequality on every exterior power, with constants uniform in k. A scalar operator-norm bound is not enough unless it is converted into a cone-preserving estimate with an explicit positive margin.

## Relation to the current frontier

This attack does not yet prove RH. It converts the remaining complementary wedge into a concrete matrix/operator problem:

`PF_infinity(h_tail)` or an equivalent all-exterior-power cone-preservation theorem.

It also explains why the k=1 result is insufficient: k=1 controls only the zeroth exterior power/coefficient signs, while RH requires all exterior powers.

## Falsification requirements

Any proposed tail estimate must be tested against:

1. positive but non-PF sequences;
2. arbitrarily high determinant order;
3. determinant margins tending to zero;
4. perturbations whose first several coefficients are positive but whose higher Toeplitz minors are negative.

No numerical success at finite k is accepted as an infinite closure.
