# Riemann Hypothesis — Frontier 06 (Corrected): Degree-2 Jensen Target

Date: 2026-09-16

## Critical correction

The previous version used the coefficients of
\[
F(w)=\Xi(\sqrt w)/\Xi(0)
\]
as though they were the coefficients in Pólya's Jensen criterion. That is not the canonical Jensen sequence.

Pólya's criterion uses the sequence \(\gamma(n)\) defined by
\[
(-1+4z^2)\Lambda\!\left(\frac12+z\right)
=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},
\qquad
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Since \((-1+4z^2)\Lambda(1/2+z)=8\xi(1/2+z)\),
\[
\gamma(n)=8\,\frac{n!}{(2n)!}\,\xi^{(2n)}\!\left(\frac12\right).
\]
Equivalently, if
\[
\Xi(t)=\xi\!\left(\frac12+it\right)
=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n},
\]
then
\[
\boxed{\gamma(n)=8\frac{n!}{(2n)!}M_n}.
\]

Thus the earlier Frontier-06 inequality for \(M_n/(2n)!\) was attached to the wrong Jensen sequence.

## Correct degree-2 condition

For
\[
J_{2,n}(X)=\gamma(n)+2\gamma(n+1)X+\gamma(n+2)X^2,
\]
hyperbolicity is equivalent to
\[
\boxed{\gamma(n+1)^2\ge\gamma(n)\gamma(n+2)}.
\]
Substituting \(\gamma(n)=8n!M_n/(2n)!\) gives the exact moment inequality
\[
\boxed{
M_{n+1}^2\ge
\frac{2n+1}{2n+3}\,M_nM_{n+2}
}\qquad(n\ge0).
\]
The factor is \((2n+1)/(2n+3)<1\), so this is compatible with ordinary moment log-convexity \(M_{n+1}^2\le M_nM_{n+2}\).

## Why this matters

This corrected target matches the actual Pólya-Jensen normalization. The earlier numerical Jensen calculations on the normalized coefficients of \(F\) were useful diagnostics, but were not direct tests of the RH-equivalent Jensen criterion.

Published work proves hyperbolicity for every fixed degree for all sufficiently large shifts, and outright hyperbolicity in a substantial finite degree range. The unresolved part is the simultaneous all-degree/all-shift statement equivalent to RH.

## Remaining proof target

A complete proof would need hyperbolicity of every
\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j
\]
for every \(d,n\ge0\), or an independent theorem placing the corresponding entire function in the Laguerre–Pólya class.

## Status

This file supersedes the earlier version of Frontier 06. It corrects the normalization and isolates the correct degree-2 Turán-type inequality. It does **not** prove RH.
