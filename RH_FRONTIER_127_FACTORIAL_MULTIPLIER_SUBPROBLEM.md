# Frontier 127 — Reciprocal-factorial multiplier-sequence subproblem

Date: 2026-09-17

## Exact operator

For n>=0 define
\[
(T_n p)(X)=\sum_{j\ge0}\frac{(2n)!}{(2n+2j)!}a_jX^j,
\quad p(X)=\sum a_jX^j.
\]
The diagonal multiplier sequence has exponential generating function
\[
\Psi_n(z)=\sum_{j\ge0}\frac{z^j}{j!}\frac{(2n)!}{(2n+2j)!}
={}_0F_2(;n+\tfrac12,n+1;z/4).
\]

## Important distinction

A proof that \(\Psi_n\) belongs to the Laguerre–Pólya class would establish that \(T_n\) preserves real-rootedness of real polynomials. That would be a genuine unconditional theorem about the factorial operator.

It would still **not** prove RH, because the Riemann theta moment polynomial entering \(\gamma_{n+j}=M_{n+j}/(2n+2j)!\) has not itself been shown to be a hyperbolic input for \(T_n\).

## Exact finite-degree evidence

For n=0 and degree 10,
\[
\sum_{j=0}^{10}\binom{10}{j}\frac{X^j}{(2j)!}
\]
has ten distinct negative real roots. This is consistent with, but does not prove, a multiplier-sequence theorem.

## Proof target

Prove or disprove, independently of RH,
\[
{}_0F_2(;n+\tfrac12,n+1;z/4)\in\mathcal{LP}
\]
for every n>=0.

A successful proof would need a rigorous Laguerre–Pólya representation, a verified stability-preserving symbol, or an equivalent multiplier-sequence theorem. Numerical root checks are not sufficient.

## Riemann-specific bridge still required

After this operator theorem, one still needs a zero-free proof that the unsummed completed theta lattice supplies the correct stable input and that the composition exactly produces every Jensen polynomial of Xi. This bridge remains the principal RH wall.

## Status

Open subproblem; no RH assumption used.
