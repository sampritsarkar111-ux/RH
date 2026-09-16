# Frontier 44 — All-degree closure map

Date: 2026-09-16

## Objective

The finite-degree Hermite program is now organized into an explicit hierarchy. The exact Jensen/Hermite equivalence requires positivity/hyperbolicity for every degree \(d\) and shift \(n\). Finite verification cannot replace this universal quantifier.

## Layer hierarchy

- Degree 2: adjacent Turán inequality for \(\gamma_n\).
- Degree 3: centered cubic cone \(4(-v)^3\ge w^2\).
- Degree 4: centered quartic discriminant \(\mathcal D_4(v,w,z)\ge0\), plus lower Hermite conditions.
- Degree \(d\ge5\): higher principal Hermite minors introduce progressively higher centered coefficient invariants.

## Universal target

The research program should seek a theorem of the form
\[
\boxed{\text{Riemann-specific structural condition on }(\gamma_n)_{n\ge0}\Longrightarrow J_{d,n}\text{ hyperbolic for all }d,n.}
\]

A merely asymptotic theorem, a fixed-degree theorem, a numerical check, or generic moment positivity is insufficient.

## Parallel routes

1. Explicit theta-kernel / total-positivity route.
2. Consecutive-ratio and finite-difference route.
3. Entire-function / Laguerre–Pólya route.
4. Higher Hermite-minor algebra and invariant factorization.
5. Independent falsification tests against generic positive measures.

The fifth route is a safeguard: any proposed lemma that follows only from positivity of a generic Stieltjes kernel must be tested against finite atomic measures before being treated as Riemann-specific.

## Status

This file is a proof architecture, not a proof. The universal Riemann-specific closure theorem remains the central unsolved target.
