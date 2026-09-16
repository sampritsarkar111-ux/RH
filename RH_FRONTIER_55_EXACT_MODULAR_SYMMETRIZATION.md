# Frontier 55 — exact modular symmetrization of the theta coefficient measure

## 1. Exact theta normalization

Take
\[
\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad t>0,
\]
so Poisson/Jacobi modularity is
\[
\theta(t)=t^{-1/2}\theta(1/t).
\]
Define the positive measure
\[
d\nu(t)=t^{-3/4}\theta(t)\,dt.
\]

## 2. The inversion is an exact measure symmetry

Under \(t=1/s\),
\[
dt=-s^{-2}ds,
\qquad
 t^{-3/4}\theta(t)
 =s^{3/4}s^{1/2}\theta(s)=s^{5/4}\theta(s).
\]
Therefore
\[
 t^{-3/4}\theta(t)dt=-s^{-3/4}\theta(s)ds,
\]
and hence the positive measure \(\nu\) is invariant under inversion (with orientation reversed by the substitution):
\[
\boxed{\iota_\#\nu=\nu,\qquad \iota(t)=1/t.}
\]

This is stronger than the schematic statement used in Frontier 54: the Jacobian exactly matches the modular weight.

## 3. Exact whole-line representation

Set
\[
x=\log t,\qquad t=e^x.
\]
Then
\[
d\nu(t)=\rho(x)\,dx,
\qquad
\rho(x)=e^{x/4}\theta(e^x).
\]
Using modularity,
\[
\rho(-x)=e^{-x/4}\theta(e^{-x})
=e^{-x/4}e^{x/2}\theta(e^x)
=\rho(x).
\]
Thus
\[
\boxed{\rho(-x)=\rho(x)>0.}
\]
The logarithmic theta measure is exactly even.

## 4. Symmetrizing the coefficient kernel

Let
\[
A_m(x)=x^{2m-2}\bigl(16m(2m-1)-x^2\bigr).
\]
This is even. Therefore
\[
\int_1^\infty A_m(\log t)\,d\nu(t)
=\int_0^\infty A_m(x)\rho(x)dx
=\frac12\int_{-\infty}^{\infty}A_m(x)\rho(x)dx.
\]
Hence the exact coefficient formula becomes
\[
\boxed{
\gamma_m=\frac{Cq_m}{2}
\int_{-\infty}^{\infty}
 x^{2m-2}\bigl(16m(2m-1)-x^2\bigr)\rho(x)\,dx,
\qquad q_m=\frac{m!}{(2m)!}.
}
\]
No boundary term is introduced: this is an equality of the original integral with one half of its even extension, not an integration-by-parts operation.

## 5. Equivalent positive measure on \(y=x^2\)

Because \(\rho\) is even, define a positive measure \(d\sigma(y)\) on \([0,\infty)\) by
\[
\int_0^\infty f(y)d\sigma(y)
:=\int_0^\infty f(x^2)\rho(x)dx.
\]
Then
\[
\boxed{
M_m:=\frac{2\gamma_m}{Cq_m}
=16m(2m-1)\mu_{m-1}-\mu_m,
\qquad
\mu_j:=\int_0^\infty y^j d\sigma(y).
}
\]
Thus the entire factorial-conjugate Turan problem is reduced to a single positive Stieltjes moment measure, but with an \(m\)-dependent linear combination of adjacent moments.

## 6. A useful exact shift identity

Since
\[
16(m+1)(2m+1)-y
=\bigl(16m(2m-1)-y\bigr)+32m+16,
\]
we have the exact polynomial relation
\[
A_{m+1}(x)=x^2A_m(x)+(32m+16)x^{2m}.
\]
Equivalently,
\[
\boxed{A_{m+1}=yA_m+(32m+16)y^m.}
\]
This exposes the obstruction sharply: the sequence is not a pure moment sequence, because a positive correction term is injected at every order.

## 7. New global target

The remaining adjacent Turan inequality is
\[
M_{m+1}^2\ge
\frac{(m+2)(2m+3)}{(m+1)(2m+1)}M_mM_{m+2}.
\]
Using the exact shift identity, the problem can be expanded entirely in \(\mu_j\). The desired result is therefore a structured Hankel inequality for the single positive measure \(\sigma\), not an atomwise inequality.

## 8. Adversarial conclusion

The modular involution itself is now fully rigorous and closes the boundary/Jacobian concern from Frontier 54. However, positivity of \(\sigma\) alone does **not** imply the required factorial-corrected log-concavity; generic positive Stieltjes measures already admit counterexamples to analogous higher-order claims. Consequently this frontier establishes a clean exact reduction, not RH.

## Status

**Closed:** exact modular symmetry, whole-line evenness, and the \(y=x^2\) positive-measure reduction.

**Open:** prove the resulting structured Hankel/factorial inequality for the specific Riemann theta measure, or derive an equivalent all-degree Jensen/hyperbolicity certificate.