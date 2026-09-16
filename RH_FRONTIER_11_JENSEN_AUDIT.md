# Frontier 11 — Jensen Bottleneck Audit

## Exact target

For the normalized even entire function

\[
G(z)=8\xi\!\left(\frac12+z\right)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},
\]

prove hyperbolicity of every Jensen polynomial

\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j.
\]

## First necessary test

For degree two,

\[
J_{2,n}(X)=\gamma(n)+2\gamma(n+1)X+\gamma(n+2)X^2.
\]

Its discriminant is

\[
\Delta_{2,n}=4\bigl(\gamma(n+1)^2-\gamma(n)\gamma(n+2)\bigr).
\]

Thus degree-2 hyperbolicity requires

\[
\gamma(n+1)^2\ge\gamma(n)\gamma(n+2).
\]

Using \(\gamma(n)=8n!M_n/(2n)!\), this is equivalent to

\[
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]

## Critical warning

Cauchy–Schwarz for a positive moment measure gives the opposite generic direction,
\[
M_{n+1}^2\le M_nM_{n+2},
\]
so positivity of the measure cannot prove the required lower bound. The special arithmetic/theta structure must enter explicitly.

## Proof obligation

A valid completion must provide a theorem that implies all degrees \(d\), not merely degree two or asymptotic ranges. Every closure step must be proved with the exact normalization above.

## Falsification obligation

If any proposed structural theorem implies a Jensen inequality that fails for a certified coefficient computation, the theorem is rejected. Numerical confirmation alone is never sufficient for RH.
