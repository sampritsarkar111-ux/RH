# Frontier 103 — PF∞ translation-kernel route: exact closure target

Date: 2026-09-16

## Objective

Replace the failed collapsed-moment positivity route by a structural route that, if completed, gives RH directly from a total-positivity theorem for the completed Riemann theta kernel.

Let
\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad \Phi(-u)=\Phi(u).
\]
The completed xi-function admits the Fourier representation
\[
\Xi(t)=\xi(1/2+it)=\int_{-\infty}^{\infty}\Phi(u)e^{itu}\,du
\]
up to the fixed normalization convention used in the project. The exact normalization must be carried consistently if this route is formalized.

## Candidate sufficient theorem

Define the translation kernel
\[
K(x,y)=\Phi(x-y).
\]
A sufficient structural target is:

\[
\boxed{\det\!\big[\Phi(x_i-y_j)\big]_{i,j=1}^{n}\ge0
\quad\text{for every }n\ge1,
\quad x_1<\cdots<x_n,\ y_1<\cdots<y_n.}
\]
This is total positivity (PF∞) of the translation kernel.

Under the standard Schoenberg/Pólya theory, a suitable integrable PF∞ function has a Fourier transform in the Laguerre–Pólya class; therefore its real entire Fourier transform has only real zeros. Applied to the completed xi-function, this would imply RH.

## Why this is a materially different route

The previous degree-two program tried to force a positive quadratic form after collapsing the modular orbit to one moment variable. That kernel was proved indefinite. PF∞ does not require pointwise positivity of the degree-two Jensen kernel. It asks for positivity of every ordered minor of the full two-variable translation kernel before collapsing the theta lattice.

Thus the modular symmetry and the full lattice are retained at the level where total positivity can act.

## Exact proof obligations

The route is NOT yet a proof. It has four non-negotiable gates:

1. **Fourier normalization.** Derive the exact theta-to-xi Fourier identity from the project's \(\Phi\), including all constants and convergence statements.

2. **PF∞ theorem.** Prove the displayed determinant inequality for the specific \(\Phi\). It is not enough to prove \(\Phi>0\), log-concavity, finitely many minors, or numerical positivity.

3. **Schoenberg hypotheses.** Verify the precise integrability/variation hypotheses needed to pass from PF∞ to the Laguerre–Pólya property of the Fourier transform, rather than citing the implication informally.

4. **Zero correspondence.** Show that the resulting Fourier transform is exactly the completed xi-function and hence that all its real zeros correspond to nontrivial zeta zeros on \(\Re s=1/2\).

## First structural reduction to attack

For n=2 the PF∞ condition is
\[
\Phi(x_1-y_1)\Phi(x_2-y_2)-\Phi(x_1-y_2)\Phi(x_2-y_1)\ge0.
\]
Writing \(a=x_2-x_1>0\), \(b=y_2-y_1>0\), translation invariance reduces this to
\[
\Phi(u)\Phi(u+a-b)-\Phi(u-b)\Phi(u+a)\ge0.
\]
A proof for all \(a,b,u\) would already establish TP2, but TP2 alone is far from PF∞. It is therefore only a diagnostic gate, not the desired endpoint.

## Adversarial requirement

Any proposed proof that factors each theta summand separately is invalid unless the factorization survives summation over the complete lattice. The earlier audit established that the individual summands do not possess the global modular symmetry; only the completed kernel does.

## Status

This frontier defines a genuinely stronger structural target, but the central PF∞ inequality has NOT been proved here. Therefore this document does not claim a proof of RH.
