# Riemann Hypothesis — Frontier 03: Jensen/Real-Rootedness Attack

Date: 2026-09-16

## Target

Let

\[
F(w)=\frac{\Xi(\sqrt w)}{\Xi(0)}=\sum_{n\ge0}c_n w^n,
\qquad c_n=(-1)^n a_n/a_0.
\]

RH is equivalent to every zero of \(F\) being real and positive.

## Key observation

For any finite truncation

\[
F_N(w)=\sum_{n=0}^N c_nw^n,
\]

real-rootedness of \(F_N\) would be a finite-dimensional certificate, but real-rootedness of finitely many truncations does **not** by itself imply real-rootedness of the limiting entire function. A uniform limiting theorem is mandatory.

## Jensen route

For a power series \(F(w)=\sum_{n\ge0}c_nw^n\), the degree-\(d\), shift-\(m\) Jensen polynomial can be formed from

\[
J_{m,d}(X)=\sum_{k=0}^d\binom dk c_{m+k}X^k,
\]

up to the conventional normalization/reversal used in the chosen Jensen-polynomial theorem.

The research problem is therefore split into two independent parts:

### A. Universal hyperbolicity

Prove hyperbolicity of \(J_{m,d}\) for **every** \(m,d\) required by the exact theorem.

### B. Exact converse/limit theorem

Prove that the resulting all-degree/all-shift hyperbolicity implies \(F\) belongs to the appropriate Laguerre–Pólya-type class, with the sign information needed to force zeros onto \((0,\infty)\).

## Important sign issue

The even substitution \(w=t^2\) changes the geometry of zeros. A real zero \(t=\pm\gamma\) corresponds to the positive zero \(w=\gamma^2\). Thus proving merely that zeros of \(F\) are real is insufficient: their sign must also be controlled.

## First coefficient diagnostic

The initial normalized coefficients are positive in magnitude and alternate in \(w\):

\[
F(w)=1-0.023099\ldots w+0.0002483\ldots w^2-1.674\times10^{-6}\ldots w^3+\cdots.
\]

This is compatible with positive real zeros, but is not a proof.

## Hard bottleneck

No general coefficient inequality currently derived here forces all Jensen polynomials of \(F\) to be hyperbolic. In particular, ordinary log-concavity of \(a_n\) is too weak, and the initial Hankel determinants of \((a_n/a_0)\) are not all positive.

## New proposed subtarget

Derive a direct integral representation for the Jensen discriminants of \(F\) in terms of the theta-kernel defining \(\Xi\). If every discriminant can be represented as a manifestly nonnegative multiple integral, this could yield universal hyperbolicity without assuming RH.

The representation must be exact and its positivity must hold for arbitrary degree and shift.

## Status

This is a genuine proof-development target, not a completed proof. The previous frontier eliminated two naive positivity certificates. The next step is to derive and test the Jensen discriminant integral representation.
