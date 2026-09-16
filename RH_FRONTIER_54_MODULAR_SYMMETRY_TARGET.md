# Frontier 54 — modular-symmetry attack on the signed Turan kernel

## Objective

The raw Turan kernel changes sign, so pointwise positivity is impossible. The next genuinely different mechanism is to exploit the modular transformation of the Riemann theta function rather than individual atoms.

For the theta kernel in the coefficient representation, the relevant integral is over `t>=1`. The modular relation has the schematic form
\[
\theta(t)=t^{-1/2}\theta(1/t)
\]
for the appropriate Jacobi theta normalization. After the logarithmic variable `x=log t`, the involution `t -> 1/t` becomes `x -> -x`.

## Proposed symmetric extension

Rather than proving positivity of the one-sided polynomial weight
\[
A_m(x)=x^{2m-2}\bigl(16m(2m-1)-x^2\bigr),
\]
construct the modularly completed signed measure on the whole real line and rewrite the coefficient as an integral against an even transformed kernel.

The target is an identity of the form
\[
\gamma_m=\int_{-\infty}^{\infty} \mathcal A_m(x)\,d\mu_{\rm mod}(x)
\]
with `mu_mod` positive and `A_m` carrying the exact modular correction.

## Why this branch is different

The previous obstruction was a signed two-variable kernel. A modular completion may create cancellation between `x` and `-x` before the Turan quadratic form is expanded. If successful, the cancellation could produce a square/Gram term that does not exist in the raw one-sided kernel.

## Concrete theorem target

Find an explicit transformed kernel `G_m(x,y)` such that
\[
T_m=\iint G_m(x,y)\,d\mu_{\rm mod}(x)d\mu_{\rm mod}(y),
\]
and prove either
\[
G_m\succeq0
\]
in the integral-operator sense, or an exact decomposition
\[
G_m(x,y)=\sum_r c_r\,u_r(x)u_r(y),\qquad c_r\ge0.
\]

The requirement is operator positivity, not pointwise positivity.

## Adversarial guardrail

Any claimed symmetric extension must first verify the boundary contribution at `t=1` and every change-of-variable Jacobian. A formal use of theta modularity without these terms is insufficient.

## Status

This is a new research direction. No modular Gram identity has yet been established, and no RH conclusion follows until such an identity and the all-order closure are proved.
