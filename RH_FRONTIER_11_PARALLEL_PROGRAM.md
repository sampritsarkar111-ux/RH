# Riemann Hypothesis — Frontier 11: Parallel Proof Program

Date: 2026-09-16

## Starting point

Frontier 10 identifies the Jensen-polynomial bottleneck. With

\[
G(z)=8\xi\!\left(\frac12+z\right)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},
\qquad
\gamma(n)=8\frac{n!}{(2n)!}M_n,
\]

the degree-2 condition is

\[
M_{n+1}^2\ge \frac{2n+1}{2n+3}M_nM_{n+2}.
\]

This document does **not** assert that RH has been proved. It specifies parallel proof/falsification work so that every proposed implication is independently checkable.

## Workstream A — Exact total positivity

Target: prove a structural theorem for the sequence \(\gamma(n)\), strong enough to imply hyperbolicity of every

\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j.
\]

Required checkpoints:

1. Express the relevant Toeplitz/Hankel minors directly in terms of the Riemann theta kernel.
2. Identify a positivity/variation-diminishing property that is actually special to that kernel.
3. Prove closure under the factorial normalization \(n!/(2n)!\).
4. Deduce all Jensen hyperbolicity, not merely fixed degree.

A failure at any checkpoint must be recorded rather than promoted to a theorem.

## Workstream B — Degree-by-degree falsification

For small \(d,n\), compute the exact Jensen polynomial coefficients from certified high-precision values of \(\gamma(n)\). For each polynomial:

- compute roots at increasing precision;
- isolate real roots with interval arithmetic where possible;
- test whether nonreal roots persist under precision refinement;
- record the first potential counterexample, if one appears.

Numerics can falsify a proposed universal statement, but cannot establish RH.

## Workstream C — Operator/spectral route

Search for a self-adjoint operator \(H\) whose spectral determinant is proportional to \(\xi(1/2+z)\). The required implication is exact:

\[
\operatorname{Spec}(H)\subset\mathbb R
\quad\Longrightarrow\quad
\xi(1/2+z)=0\Rightarrow z\in\mathbb R.
\]

The difficult step is existence and equality of the determinant, not merely a formal analogy with Hilbert–Pólya.

Any candidate operator must have:

- a precise domain;
- self-adjointness proof;
- a discrete spectrum or a rigorously defined regularized determinant;
- an exact determinant identity with \(\xi\).

## Workstream D — Integral-kernel route

Starting from a theta-kernel representation, attempt to establish a transformation theorem implying the required Jensen inequalities. Positivity of the kernel alone is insufficient; Frontier 09 gives the generic moment obstruction.

Candidate properties to test:

\[
\text{total positivity},\quad
\text{strict sign-regularity},\quad
\text{complete monotonicity},\quad
\text{P\acute{o}lya-frequency structure}.
\]

Each property must be proved for the actual Riemann kernel and connected by explicit lemmas to Jensen hyperbolicity.

## Workstream E — Independent equivalence audit

For every proposed proof, audit the exact logical chain:

\[
\text{lemma}
\Rightarrow
\text{kernel/sequence property}
\Rightarrow
\text{all Jensen polynomials hyperbolic}
\Rightarrow
\text{Laguerre--P\acute{o}lya membership}
\Rightarrow
\text{RH}.
\]

No step may be replaced by numerical agreement, an unproved closure assertion, an asymptotic statement without uniform error control, or an appeal to the RH itself.

## Current status

No complete proof is claimed. The objective of Frontier 11 is to turn the remaining bottleneck into independently verifiable lemmas and, equally importantly, to expose any hidden false implication before it is used in a purported proof.
