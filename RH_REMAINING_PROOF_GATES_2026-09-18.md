# RH — Remaining Proof-Bearing Gates (2026-09-18)

This file records the current non-circular targets after Frontier 191.

## Status

The Riemann Hypothesis is **not proved** by the project. Frontier 191 rigorously falsified a generic positive-measure/factorial-moment shortcut.

## Remaining gates

### Gate A — Riemann-specific PF∞ / strict sign-regularity
Goal: prove a theta/arithmetic-specific total-positivity or strict sign-regularity theorem strong enough to imply hyperbolicity of every Jensen polynomial of the completed Riemann Xi function.

Required form:
\[
\text{Riemann-specific kernel property}\Longrightarrow J_{d,n}\text{ hyperbolic for every }d,n.
\]

The theorem must use genuine Riemann structure; generic positivity is insufficient by Frontier 191.

Status: **OPEN**.

### Gate B — Nyman–Beurling cyclicity
Goal: prove the required density/cyclicity statement directly, without assuming RH or inserting the location of nontrivial zeros into the construction.

Status: **OPEN / RH-equivalent**.

### Gate C — Weil/Li positivity
Goal: obtain the required positivity of the Weil quadratic form or all Li coefficients from an RH-independent positive factorization.

Required anti-circular condition: the positivity certificate cannot be defined using the unknown zeros as input.

Status: **OPEN**.

### Gate D — Zero-independent spectral realization
Goal: construct a self-adjoint operator from explicit theta/arithmetic data such that its spectral determinant is exactly the completed Xi function, with the critical-line conclusion following from self-adjointness.

Anti-circular condition:
\[
\text{operator construction}\not\equiv\text{construction from the unknown zeros}.
\]

Status: **OPEN**.

## Frontier 191 no-go theorem

For
\[
\mu=\frac1{1000}\delta_1+\frac{999}{1000}\delta_{1/10},
\qquad M_n=\int u^{2n}\,d\mu(u),
\qquad \gamma_n=\frac{M_n}{(2n)!},
\]
the cubic Jensen polynomial
\[
J_{3,0}(X)=\gamma_0+3\gamma_1X+3\gamma_2X^2+\gamma_3X^3
\]
has exact discriminant
\[
\boxed{\operatorname{Disc}(J_{3,0})=-\frac{98459838459955337}{3840000000000000000000000000}<0.}
\]
Thus
\[
\text{positive measure + factorial normalization}\not\Longrightarrow\text{all Jensen polynomials hyperbolic}.
\]

## Closure criterion

A complete RH claim requires an unconditional proof of
\[
\zeta(\rho)=0,\quad0<\Re\rho<1
\quad\Longrightarrow\quad
\Re\rho=\frac12,
\]
with every analytic-continuation, limiting, positivity, operator, and approximation step justified independently of that conclusion.

## Research discipline

New numeral systems may be used as computational/encoding tools, but a numeral representation alone is not a proof-bearing step. Any proposed new system must produce a new theorem, inequality, invariant, factorization, or rigorously verified obstruction before it is counted as progress toward RH.
