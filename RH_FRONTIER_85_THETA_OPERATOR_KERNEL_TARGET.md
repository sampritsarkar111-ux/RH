# Frontier 85 — Theta operator-preserver endgame

Date: 2026-09-16

Frontier 84 rules out the simplest common-proper-position rescue of the bivariate integration step. The next target is therefore an operator theorem specific to the theta kernel.

## 1. Coefficient action

For a degree-D polynomial
\[
p(t)=\sum_{j=0}^D a_jt^j,
\]
the theta integration has coefficient action
\[
\mathcal T_D[p](X)
=\sum_{j=0}^D a_j\,\mu_{n+j}\,X^j,
\]
where the relevant \(\mu_m\) are the exact theta/Mellin moments after the factorial correction. Thus the problem is not arbitrary integration: it is a diagonal coefficient multiplier
\[
(a_0,\ldots,a_D)\mapsto(a_0\mu_n,\ldots,a_D\mu_{n+D}).
\]

## 2. Exact preservation criterion to attack

For each D,n, let
\[
M_{D,n}=\operatorname{diag}(\mu_n,\mu_{n+1},\ldots,\mu_{n+D}).
\]
The proof-bearing question is whether this diagonal operator preserves the hyperbolicity cone of the specific Jensen family. A general positive diagonal multiplier does not preserve hyperbolicity, so positivity of \(\mu_m\) is insufficient.

A complete route would prove one of the following, without RH assumptions:

- the symbol of the diagonal operator is stable in the relevant multivariate sense;
- the operator is a composition of known stability preservers;
- the theta moment sequence satisfies an all-order multiplier criterion exactly matched to the Jensen family;
- or every Hermite matrix of the transformed polynomial has a manifestly nonnegative theta representation.

## 3. Low-degree gates

Degree 2 requires
\[
\gamma_{n+1}^2-\gamma_n\gamma_{n+2}\ge0
\iff
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]
Degree 3 requires the centered invariant
\[
w^2+4v^3\le0.
\]
Therefore a successful operator theorem must imply both simultaneously and must continue to all degrees.

## 4. Non-circularity gate

It is not enough to assume the theta moment multiplier is PF-infinity, because PF-infinity of the canonical Xi coefficient sequence is itself RH-equivalent in the relevant formulations. The certificate must be derived before any zero-location statement.

## 5. New master target

Seek an explicit finite-dimensional operator identity
\[
\boxed{
\mathsf H_d(\mathcal T_Dp)
=\mathsf A_{D,d}^*\,\mathsf G_{D,d}\,\mathsf A_{D,d}
}
\]
where \(\mathsf G_{D,d}\succeq0\) follows solely from theta modularity and positivity. If this holds for every d,D,n, all Hermite minors of the transformed Jensen polynomials are nonnegative, yielding hyperbolicity.

An equivalent target is a theta-specific total-positivity factorization of the diagonal multiplier matrix after the factorial correction.

## Status

This is the narrowed proof-bearing endgame. No global factorization has yet been established; RH remains unproved.
