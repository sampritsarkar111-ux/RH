# Frontier 50 — Uniform all-m atomwise positivity of the theta coefficient atoms

## Objective

Close the strongest immediate gap left by Frontier 49: prove
\[
B_m(\pi k^2)>0
\qquad(m,k\ge1),
\]
not merely for `m=1`. The key is a monotone-likelihood-ratio comparison after the exact substitution `x=log t`.

## 1. Exact atom

For `a>0`, define
\[
I_n(a)=\int_1^\infty (\log t)^n t^{-3/4}e^{-at}\,dt.
\]
With `t=e^x`,
\[
I_n(a)=\int_0^\infty x^n e^{x/4-ae^x}\,dx.
\]
The coefficient atom is
\[
B_m(a)=16m(2m-1)I_{2m-2}(a)-I_{2m}(a).
\]

## 2. Exponential-envelope factorization

Put
\[
\lambda=a-\frac14,
\qquad
h_a(x)=\exp\{-a(e^x-1-x)\}.
\]
Then the exact identity is
\[
\boxed{
I_n(a)=e^{-a}\int_0^\infty x^n e^{-\lambda x}h_a(x)\,dx.
}
\]
For `a>1/4`, `lambda>0`, and
\[
\frac{d}{dx}\log h_a(x)=-a(e^x-1)\le0.
\]
Hence `h_a` is positive and decreasing on `[0,infinity)`.

## 3. A weighted Gamma comparison lemma

Let `n>=0`, `lambda>0`, and let `h` be positive and decreasing. Let `Y` have the Gamma distribution with shape `n+1` and rate `lambda`, whose density is proportional to
\[
 x^n e^{-\lambda x}.
\]
Because `x^2` is increasing and `h(x)` is decreasing, Chebyshev's covariance inequality gives
\[
\operatorname{Cov}(Y^2,h(Y))\le0.
\]
Therefore
\[
\frac{\int_0^\infty x^{n+2}e^{-\lambda x}h(x)\,dx}
{\int_0^\infty x^ne^{-\lambda x}h(x)\,dx}
\le E[Y^2].
\]
For `Y~Gamma(n+1,lambda)`,
\[
E[Y^2]=\frac{(n+1)(n+2)}{\lambda^2}.
\]
Thus the exact comparison is
\[
\boxed{
\frac{I_{n+2}(a)}{I_n(a)}
\le
\frac{(n+1)(n+2)}{(a-1/4)^2},
\qquad a>\frac14.
}
\]
The inequality is strict for `a>1/4` because `h_a` is nonconstant and `x^2` is nonconstant on the support.

## 4. Uniform positivity of every `B_m` on the theta range

Take `n=2m-2`. Then
\[
\frac{I_{2m}(a)}{I_{2m-2}(a)}
<\frac{(2m-1)(2m)}{(a-1/4)^2}.
\]
If
\[
(a-1/4)^2>\frac18,
\]
then
\[
\frac{(2m-1)(2m)}{(a-1/4)^2}
<16m(2m-1).
\]
Consequently
\[
I_{2m}(a)<16m(2m-1)I_{2m-2}(a),
\]
and hence
\[
\boxed{B_m(a)>0\quad\text{whenever }a>\frac14+\frac1{2\sqrt2}.}
\]
Every theta atom has `a=pi k^2>=pi`, so in particular
\[
\boxed{B_m(\pi k^2)>0\quad\forall m,k\ge1.}
\]
This is an all-order, non-numerical result.

## 5. Why this is useful but not yet RH

The exact theta coefficient representation is
\[
\gamma_m=Cq_m\sum_{k\ge1}B_m(\pi k^2),
\qquad q_m=\frac{m!}{(2m)!}\times(\text{fixed positive normalization}),
\]
so Frontier 50 removes one major sign obstruction: every individual theta atom contributing to the coefficient is positive.

However, the required Turan form contains cross-products of different `m`:
\[
T_m=C^2q_{m+1}^2\sum_{k,\ell\ge1}
\Bigl[B_{m+1}(k)B_{m+1}(\ell)
-\eta_m\{B_m(k)B_{m+2}(\ell)+B_m(\ell)B_{m+2}(k)\}\Bigr].
\]
Atomwise positivity of all `B_m` does **not** imply positivity of this quadratic form.

## 6. New sharpened target

The remaining atomwise-to-global bridge can now be stated without any sign ambiguity:

> **Target A:** prove a ratio inequality strong enough to control
> `B_{m+1}(k)^2` against `B_m(k)B_{m+2}(k)` uniformly in `m,k`.
>
> **Target B:** prove total positivity / log-concavity of the matrix
> `M_{m,k}=B_m(pi k^2)` or of its factorial-normalized version.
>
> **Target C:** establish a Gram decomposition of the full double sum using the now-positive atom vectors.

Any one of these would materially advance the Turan closure, but none is asserted here.

## 7. Audit

**Proved:**
- exact Gamma-weight representation of `I_n`;
- exact decreasing multiplier `h_a`;
- rigorous weighted-Gamma moment-ratio bound;
- uniform `B_m(a)>0` for all `m>=1` on the entire theta range `a=pi k^2`;
- no numerical approximation is used in the proof.

**Still open:**
- Turan positivity for the summed coefficients;
- the degree-3 cone `4v^3+w^2<=0`;
- all-degree Jensen hyperbolicity;
- equivalence-to-RH closure;
- RH itself.

**Status: rigorous new theorem; no RH proof claimed.**
