# Frontier 105 — sharp de Bruijn–Newman route

Date: 2026-09-16

## Exact reduction

For the de Bruijn–Newman family
\[
H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)\,du,
\]
there is a threshold \(\Lambda\) such that all zeros are real for \(t\ge\Lambda\), and RH is equivalent to \(\Lambda\le0\). Rodgers–Tao proved \(\Lambda\ge0\), so the remaining target is exactly
\[
\boxed{\Lambda=0.}
\]
This is a sharper target than merely seeking an arbitrary RH reformulation.

## Why this route is serious

The already-proved lower bound means a successful argument only needs to prove that real-rootedness begins at or before \(t=0\). Equivalently, one needs a proof that \(H_0=\Xi\) has only real zeros. The heat-flow PDE
\[
\partial_t H_t(z)=-\partial_{zz}H_t(z)
\]
shows that this is a boundary regularity problem for the exact theta kernel.

## Candidate analytic gate

A sufficient route is to establish an all-order variation-diminishing / total-positivity property of the heat-deformed kernel that remains valid down to \(t=0\). The required statement must be global in order and cannot be replaced by finite-order numerical checks.

An equivalent Jensen route is:
\[
\forall d,n\ge0,\qquad J^{d,n}_\gamma(X)\text{ is hyperbolic},
\]
where
\[
J^{d,n}_\gamma(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j,
\qquad
\Xi(z)=\sum_{n\ge0}\gamma(n)z^{2n}/n!.
\]
Pólya's theorem makes this all-(d,n) condition equivalent to RH. Existing work proves eventual hyperbolicity for every fixed d, and effective results cover huge finite degree ranges, but this does not close the infinite family.

## New proof-engineering requirement

The next calculation should attack the **finite-strip obstruction** directly: derive exact symbolic recurrence/inequality relations among the Hankel/Jensen minors of the theta moments that propagate positivity from a finite seed to all degrees and shifts. A valid propagation lemma would convert the infinite hyperbolicity problem into finitely many exact base inequalities plus a proven induction invariant.

The induction invariant must be algebraic/analytic and exact; numerical interval evidence can only be used to discover candidate inequalities, never as the final proof.

## Integrity status

This frontier identifies the sharp remaining target \(\Lambda=0\) and a concrete induction architecture, but it does not claim that the induction invariant has yet been proved.
