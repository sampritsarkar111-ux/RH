# Riemann Hypothesis — Exact Proof Status Audit

Date: 2026-09-16

## Bottom line

No complete rigorous proof of the Riemann Hypothesis has been obtained in this research cycle. The repository therefore does **not** claim RH solved.

## Exact target

With
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Xi(t)=\xi(1/2+it),
\]
and
\[
\Xi(t)=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n},
\]
we have
\[
8\xi(1/2+z)=\sum_{n\ge0}\frac{\gamma_n}{n!}z^{2n},
\qquad
\gamma_n=8\frac{n!}{(2n)!}M_n.
\]
The canonical Jensen polynomials are
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
RH is equivalent to hyperbolicity of every \(J_{d,n}\).

## New exact algebraic checkpoint

The factorial multiplier satisfies
\[
\frac{n!}{(2n)!}=\frac{1}{4^n(1/2)_n}.
\]
For its own log-curvature,
\[
\frac{a_{n+1}^2}{a_na_{n+2}}=\frac{2n+3}{2n+1}>1,
\qquad a_n=\frac{n!}{(2n)!}.
\]
Consequently the canonical gamma sequence is not reducible to the raw moment sequence by a neutral Jensen-preserving rescaling. The quadratic Jensen condition is exactly
\[
\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}
\iff
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]

A beta identity gives
\[
\frac{n!}{(2n)!}=\frac{2n+1}{n!}\int_0^1[x(1-x)]^n\,dx,
\]
but the prefactor \((2n+1)/n!\) depends on \(n\), so this does not create a fixed positive measure representation for \(\gamma_n\). Thus ordinary Stieltjes-moment positivity is insufficient for the canonical Jensen problem.

## Literature cross-check

Current literature continues to treat the all-degree/all-shift Jensen condition as equivalent to RH. Griffin–Ono–Rolen–Zagier established eventual hyperbolicity for each fixed degree, while newer 2026 work gives stronger simultaneous asymptotic regions. These results leave a complementary region whose global hyperbolicity has not been proved.

The de Bruijn–Newman route is also exact: Rodgers–Tao established the non-negativity of the de Bruijn–Newman constant, while RH corresponds to the opposite inequality; hence that route still requires the equality/boundary conclusion.

## Required breakthrough

A complete proof now requires at least one genuinely global certificate, such as:

1. a theorem proving \(J_{d,n}\) hyperbolic for every \(d,n\ge0\);
2. a proof that the completed xi function belongs to the Laguerre–Pólya class;
3. a new argument proving the de Bruijn–Newman threshold is exactly zero in the direction needed for RH; or
4. an equivalent global zero-location theorem.

Finite computation, asymptotic hyperbolicity, moment positivity, or numerical zero checks do not close these quantifiers.

## Research discipline

Every future candidate proof must explicitly state its domain of quantification and verify the final global implication. If a proposed identity or normalization fails even at degree two, it must be rejected rather than used as evidence for RH.
