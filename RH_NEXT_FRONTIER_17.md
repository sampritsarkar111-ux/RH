# Riemann Hypothesis — Frontier 17: Global Closure Audit

Date: 2026-09-16

## Current verified target

The exact RH-equivalent Jensen criterion uses
\[
\xi\!\left(\frac12+z\right)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},
\qquad
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j.
\]
RH is equivalent to hyperbolicity of every \(J_{d,n}\).

## New 2026 theorem checked

Jonathan Holland (arXiv:2608.08682) proves an absolute-constant wedge
\[
n^3\log^2(n+2)\ge Kd^5
\Longrightarrow J_{d,n}\text{ hyperbolic}.
\]
This is a genuine simultaneous degree/shift theorem, but the complement is infinite.

## Alternative heat-flow route

For the de Bruijn–Newman family \(H_t\), Rodgers–Tao proved \(\Lambda\ge0\), while RH is equivalent to \(\Lambda\le0\). Hence the heat-flow route reduces RH to the exact boundary statement \(\Lambda=0\). No unconditional proof of \(\Lambda\le0\) was found.

## Closure attempt

Three possible global certificates were tested conceptually:

1. Positive theta kernel \(\Phi\ge0\): insufficient because ordinary moment sequences are log-convex in the wrong direction for the required Jensen inequalities.
2. Raw moment Jensen polynomials: invalid normalization; the factorial factor \(n!/(2n)!\) must be retained.
3. Asymptotic wedge + finite computation: insufficient because the complement has infinitely many degrees.

The remaining theorem is therefore genuinely global:
\[
\forall d,n\ge0,\quad J_{d,n}\text{ hyperbolic},
\]
or an independent proof that \(\xi(1/2+z)\) belongs to the Laguerre–Pólya class.

## Status

No complete rigorous proof of RH has been obtained in this cycle. Any claim that it has would be false. The research has instead eliminated a normalization-based false obstruction and isolated the exact missing global theorem.
