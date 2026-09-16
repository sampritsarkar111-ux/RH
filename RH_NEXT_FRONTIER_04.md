# Riemann Hypothesis — Frontier 04: Corrected Jensen Diagnostic

Date: 2026-09-16

## 1. Exact even-variable expansion

The correct normalization is

\[
F(w)=\frac{\Xi(\sqrt w)}{\Xi(0)}
=\frac{\xi(1/2+i\sqrt w)}{\xi(1/2)}.
\]

Since
\[
\Xi(t)=\sum_{n\ge0}(-1)^n a_nt^{2n},
\]
we have
\[
F(w)=\sum_{n\ge0}(-1)^n\frac{a_n}{a_0}w^n.
\]

The corrected initial coefficients are

\[
F(w)=1-0.0231049931154w+0.000248334053789w^2
-1.67435262798\times10^{-6}w^3+8.03069742104\times10^{-9}w^4-\cdots.
\]

The alternating sign is exactly what is expected if all zeros of \(F\) are positive.

## 2. Shift-0 Jensen test

Using
\[
J_{0,d}(X)=\sum_{k=0}^{d}\binom dk c_kX^k,
\qquad c_k=[w^k]F(w),
\]
finite-precision diagnostics give positive real roots for degrees 2 through 5:

\[
\begin{array}{c|l}
d&\text{approximate roots of }J_{0,d}\\\hline
2&24.9988,\;161.0812\\
3&17.6381,\;105.0849,\;322.2264\\
4&13.6380,\;78.7409,\;224.0511,\;517.5462\\
5&11.1204,\;63.1395,\;173.9301,\;375.1800,\;742.3319
\end{array}
\]

This is consistent with the required positive-real-zero geometry, but is finite evidence only.

## 3. A sharper algebraic target

For a polynomial with positive roots \(r_1,\ldots,r_d\), its coefficient sequence is a Pólya-frequency sequence and satisfies Newton inequalities. Therefore a possible route is to prove, directly from the theta representation of \(\Xi\), the full family of Newton inequalities for every Jensen polynomial.

However, Newton inequalities alone are not sufficient for arbitrary polynomials to guarantee real-rootedness. Thus the real target is stronger:

\[
\boxed{\text{prove every Jensen polynomial is hyperbolic, with all roots positive.}}
\]

## 4. New proposed mechanism: theta-kernel determinant

Write
\[
\Xi(t)=\int_0^\infty \Phi(u)\cos(tu)\,du
\]
with the standard rapidly decaying even theta kernel \(\Phi\).

Then the even coefficients satisfy
\[
(-1)^na_n=\frac1{(2n)!}\int_0^\infty \Phi(u)u^{2n}\,du
\]
under the corresponding normalization.

Hence every Jensen coefficient is an explicit linear combination of moments
\[
M_n=\int_0^\infty\Phi(u)u^{2n}\,du.
\]

The next proof target is therefore to rewrite each Jensen discriminant as a determinant built from the moment sequence \((M_n)\), and then exploit the special theta structure of \(\Phi\). Ordinary Hankel positivity has already been falsified, so the determinant must incorporate the factorial/binomial normalization intrinsic to Jensen polynomials.

## 5. Research warning

No implication of the form
\[
\Phi(u)\ge0\Rightarrow \Xi\text{ has only real zeros}
\]
is valid. Positivity of a Fourier/cosine kernel is far weaker than the required Pólya-frequency or total-positivity property.

## 6. Status

This frontier corrects the sign/normalization issue in the preceding Jensen attack and produces a sharper algebraic target: prove all Jensen polynomials hyperbolic with positive roots by exploiting the theta-kernel moment structure and its factorial/binomial normalization.

No complete RH proof has been established here.
