# Riemann Hypothesis — Complete-Proof Attempt 01

Date: 2026-09-16

## Objective

Attempt a direct proof by establishing that the Pólya/Jensen sequence of the Riemann xi function has hyperbolic Jensen polynomials in every degree and shift.

## Exact reduction

Let
\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
G(z)=(-1+4z^2)\Lambda\!\left(\frac12+z\right)=8\xi\!\left(\frac12+z\right).
\]
Write
\[
G(z)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n}.
\]
The Jensen polynomials are
\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j.
\]
A complete Jensen route to RH would require hyperbolicity of every \(J_{d,n}\), followed by the exact Jensen/Laguerre–Pólya converse.

## First necessary condition

For \(d=2\),
\[
J_{2,n}(X)=\gamma(n)+2\gamma(n+1)X+\gamma(n+2)X^2,
\]
so
\[
\Delta=4(\gamma(n+1)^2-\gamma(n)\gamma(n+2)).
\]
Thus
\[
\gamma(n+1)^2\ge\gamma(n)\gamma(n+2)
\]
is necessary and sufficient for degree-2 hyperbolicity.

If
\[
\Xi(t)=\xi\!\left(\frac12+it\right)
=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n},
\]
then
\[
\gamma(n)=8\frac{n!}{(2n)!}M_n,
\]
and therefore
\[
\boxed{M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}}.
\]

## Attempted proof mechanism

A natural idea is to use the theta-kernel representation of \(\Xi\), express each \(M_n\) as a positive integral, and prove all Jensen determinants as nonnegative multiple integrals. The desired determinant would need a kernel with a structural factor such as
\[
\prod_{i<j}(u_i^2-u_j^2)^2
\]
and a nonnegative remaining weight.

The positivity of the theta kernel alone is insufficient: ordinary moment sequences are log-convex by Cauchy–Schwarz, whereas the Jensen problem asks for stronger factorial/binomial transforms and, in higher degree, full hyperbolicity.

## Failure point

No valid derivation of the required all-degree nonnegative determinant kernel has been obtained. In particular, replacing the actual Jensen sequence by the raw coefficients of \(\Xi(\sqrt w)\) is invalid, and finite numerical root checks cannot supply the missing universal quantifier.

Therefore this attempt does not constitute a proof of RH.

## What would complete the proof

It would be sufficient to establish one of the following rigorously without assuming RH:

1. every \(J_{d,n}\) is hyperbolic for all \(d,n\ge0\);
2. \(G\) is in the Laguerre–Pólya class;
3. an equivalent global real-zero-preserving theorem for \(G\) or \(\Xi\).

Until one of these is proved, the Riemann Hypothesis remains unproved in this research branch.
