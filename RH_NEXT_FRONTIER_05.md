# Riemann Hypothesis — Frontier 05: Jensen/Theta Route Stress Test

Date: 2026-09-16

## Objective

Continue the Laguerre–Pólya/Jensen route without treating numerical hyperbolicity as proof.

## 1. Structural identity

Let
\[
F(w)=\frac{\Xi(\sqrt w)}{\Xi(0)}=\sum_{n\ge0}c_nw^n,
\qquad c_n=(-1)^n\frac{a_n}{a_0}.
\]

From a cosine-transform representation
\[
\Xi(t)=\int_0^\infty\Phi(u)\cos(tu)\,du,
\]
the coefficients have the form
\[
c_n=(-1)^n\frac{1}{a_0(2n)!}\int_0^\infty\Phi(u)u^{2n}\,du,
\]
subject to the exact normalization of the chosen \(\Phi\).

Therefore the Jensen polynomial
\[
J_{m,d}(X)=\sum_{k=0}^{d}\binom dk c_{m+k}X^k
\]
is a factorial-weighted moment polynomial.

## 2. What this does NOT prove

Even if \(\Phi\ge0\), an integral representation of \(J_{m,d}\) does not automatically preserve hyperbolicity. Likewise:

- coefficient sign alternation is insufficient;
- log-concavity is insufficient;
- ordinary Hankel/Stieltjes positivity is insufficient;
- finitely many real-rooted Jensen polynomials are insufficient.

Thus the missing theorem must be global and exact.

## 3. New algebraic observation

For \(m=0\), the degree-\(d\) Jensen polynomial can be written directly as
\[
J_{0,d}(X)=\sum_{k=0}^{d}\binom dk(-1)^k
\frac{M_k}{(2k)!a_0}X^k,
\qquad
M_k=\int_0^\infty\Phi(u)u^{2k}\,du.
\]

Equivalently,
\[
J_{0,d}(X)=\frac1{a_0}\int_0^\infty\Phi(u)
\left[\sum_{k=0}^{d}\binom dk(-1)^k
\frac{u^{2k}X^k}{(2k)!}\right]du.
\]

The bracketed polynomial is NOT simply \((1-u^2X)^d\); the factorial \((2k)!\) is the essential obstruction.

## 4. Candidate positivity mechanism

A successful proof would need a representation of the form
\[
\operatorname{Disc}(J_{m,d})
=\int_{(0,\infty)^r}
K_{m,d}(u_1,\ldots,u_r)\,du_1\cdots du_r,
\]
where the kernel \(K_{m,d}\) is manifestly nonnegative and is derived from the theta kernel without assuming RH.

A particularly strong form would be a Vandermonde-square factor
\[
K_{m,d}=W_{m,d}(u_1,\ldots,u_r)
\prod_{i<j}(u_i^2-u_j^2)^2,
\qquad W_{m,d}\ge0.
\]
Such a formula would connect the Jensen discriminant to total positivity.

No such formula has yet been derived; it is a target, not an established identity.

## 5. Numerical sanity check

The previously computed shift-zero Jensen polynomials of degrees 2–5 have positive real roots. This remains consistent with the RH-required geometry but provides no infinite conclusion.

## 6. Next decisive test

Do not increase the degree of numerical testing blindly. First derive the exact discriminant for \(d=2\):
\[
\operatorname{Disc}(J_{m,2})
=4c_{m+1}^2-8c_mc_{m+2}.
\]
Thus universal degree-2 hyperbolicity is equivalent to
\[
\boxed{c_{m+1}^2\ge2c_mc_{m+2}\quad\text{for every }m\ge0}
\]
for this Jensen normalization.

This is a concrete infinite coefficient inequality that can be attacked from the theta moments. Proving it for every \(m\) would be a genuine lemma, although still far short of RH because all degrees and shifts would remain to be controlled.

## Status

This frontier produces a precise first infinite subproblem and identifies the exact factorial obstruction. No complete proof of RH is claimed.
