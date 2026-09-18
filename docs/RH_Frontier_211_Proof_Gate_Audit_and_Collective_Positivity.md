# RH Frontier 211 — Proof-Gate Audit and Collective-Positivity Principle

**Date:** 2026-09-18  
**Status:** OPEN — no proof of RH established.

## 1. Exact Pólya-series audit

For
\[
S(x)=\sum_{n\ge1}(4\pi^2n^4x^2-6\pi n^2x)e^{-\pi n^2x},
\]
the nth summand is
\[
2\pi n^2x(2\pi n^2x-3)e^{-\pi n^2x}.
\]
Hence it is negative for
\[
0<x<\frac{3}{2\pi n^2}.
\]

So any proof of S(x)>0 must use collective cancellation/structure; termwise positivity is impossible.

## 2. Adversarial audit of a recent claimed Weil proof

SciSpace surfaced a 2026 manuscript claiming RH from one negative complex evaluation of a test transform. That logical move is insufficient.

For an off-line zero \(\rho=\sigma+i\gamma\), a negative value of one transformed term does not imply
\[
W_\xi(g)<0.
\]
The complete Weil functional contains the full symmetric zero contribution and the arithmetic/archimedean terms. A valid contradiction needs a global bound:
\[
W_{O(\rho)}(g)\le-\eta,
\qquad
|W_\xi(g)-W_{O(\rho)}(g)|<\eta.
\]

This is now an explicit kill-test for future purported proofs.

## 3. Spectral route audit

A self-adjoint operator alone does not prove RH. The determinant must encode exactly the completed xi divisor:
\[
\det_{\rm reg}(s-A)=E(s)\xi(s),
\qquad E(s)\ne0,
\]
with equality of zeros and multiplicities and a rigorous spectral parameterization whose real spectrum corresponds exactly to \(\Re s=1/2\).

## 4. New master principle

**Collective Positivity Principle.** Any Pólya-kernel proof based on a sign-changing theta series must establish a global identity/inequality in which cancellation is controlled analytically. A termwise sign argument cannot close the proof.

## 5. New breakthrough target

Search for an exact transformation
\[
S(x)=P(x)+R(x)
\]
where either
\[
P(x)\ge0,\quad R(x)\ge0,
\]
or
\[
P(x)>0,\quad |R(x)|<P(x)
\]
globally. The preferred mechanism is a theta/modular transformation, Poisson summation, or positive-semidefinite Gram representation.

## 6. Four simultaneous gates

- **P:** global Pólya-kernel positivity.
- **W:** globally dominated Weil orbit separation.
- **S:** exact self-adjoint spectral determinant.
- **J:** all-degree Jensen/total-positivity theorem.

No gate is presently closed.
