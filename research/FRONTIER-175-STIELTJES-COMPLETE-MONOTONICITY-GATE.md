# Frontier 175 — Exact Stieltjes/Complete-Monotonicity Gate

## Status

**Proof status: OPEN. No unconditional proof of RH is claimed.**

The project already established that theta-kernel positivity by itself does not imply positivity of the nonlinear logarithmic derivative. This frontier sharpens the target into an exact function-theoretic certificate.

Let
\[
H(x)=\Xi\!\left(\tfrac12+x\right),\qquad m(x)=-\frac{H'(x)}{H(x)}
\]
for real x in a zero-free interval containing the positive half-line.

## Exact Stieltjes certificate

A positive function m on (0,∞) is a Stieltjes function if and only if it admits
\[
m(x)=a+\frac b x+\int_{(0,\infty)}\frac{d\mu(t)}{x+t},
\qquad a,b\ge0,\quad \mu\ge0,
\]
with the standard integrability condition \(\int(1+t)^{-1}d\mu(t)<\infty\).

Such an m is completely monotone and satisfies the stronger derivative inequalities
\[
(-1)^n m^{(n)}(x)\ge0,
\qquad
(-1)^n (x m(x))^{(n)}\ge0
\quad(n\ge0,x>0).
\]

Thus a theta-derived proof can be split into two exact obligations:

1. **CM gate:** prove \((-1)^n m^{(n)}(x)\ge0\) for every n and every x>0.
2. **Stieltjes gate:** prove \((-1)^n (xm(x))^{(n)}\ge0\) for every n and every x>0, together with the Stieltjes growth/analyticity condition.

The second gate prevents the common error of replacing Stieltjes positivity by mere complete monotonicity.

## Factorial Hankel consequence

Define
\[
c_n=(-1)^n m^{(n)}(x_0),\qquad
K_N(x_0)=\left[\frac{c_{i+j}}{(i+j)!}\right]_{i,j=0}^{N}.
\]
A Stieltjes representation gives the Gram identity
\[
K_N(x_0)=\int_{[0,\infty)}
\mathbf v_N(t)\mathbf v_N(t)^T\,d\nu_{x_0}(t),
\qquad
\mathbf v_N(t)=\bigl(1,t,t^2,\ldots,t^N\bigr)^T,
\]
for the corresponding positive transformed measure \(d\nu_{x_0}\). Hence \(K_N\succeq0\) for every N.

This is a **necessary** consequence, not a proof of the converse unless the full moment/Stieltjes hypotheses are supplied.

## Zero-free implication

If the certificate is established globally on the relevant half-line and the resulting Pick/Stieltjes continuation is shown to coincide with the meromorphic logarithmic derivative of H, poles of m can occur only on the permitted Stieltjes support. A complete RH proof would then require an additional exact symmetry/continuation argument converting this pole-location statement into the assertion that every zero of Xi has real part 0, equivalently every nontrivial zeta zero has real part 1/2.

That final conversion is still a proof obligation; it must not be silently assumed.

## High-value attack

The most direct new calculation is therefore not another generic Hankel test. It is an **all-order theta identity** of the form
\[
(-1)^n\frac{d^n}{dx^n}\!\left[-\frac{H'(x)}{H(x)}\right]
=\int_0^\infty t^n e^{-xt}\,d\sigma(t),
\qquad d\sigma\ge0,
\]
plus the corresponding representation for \(x m(x)\). Any explicit positive \(\sigma\) derived solely from the Riemann theta kernel would close the nonlinear positivity wall without using zero locations.

A second independent target is the upper-half-plane identity
\[
\operatorname{Im}z>0\Longrightarrow \operatorname{Im}m(z)\le0,
\qquad m(x)\ge0\ (x>0),
\]
with the exact Stieltjes normalization and growth bound. This is the Pick formulation of the same obstruction and can be attacked directly from the theta transform.

## Falsification requirements

Any proposed identity must be checked against:

- exact low-order derivatives of Xi;
- arbitrary positive test points x;
- complex points in the upper half-plane;
- convergence/interchange of all sums and integrals;
- multiplicities and poles;
- the functional equation \(H(x)=H(-x)\);
- the possibility that a formally positive kernel loses positivity after the nonlinear logarithm.

Numerical PSD of finitely many Hankel matrices is evidence only and cannot be promoted to an all-order theorem.
