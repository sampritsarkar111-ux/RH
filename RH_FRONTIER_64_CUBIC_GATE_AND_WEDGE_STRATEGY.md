# Frontier 64 — exact cubic gate and wedge strategy

## Purpose

Frontier 63 replaced the overly broad PF∞ target by a uniform Jensen certificate. The next concrete attack is to make the first nontrivial finite-degree gate completely explicit and then ask whether its theta structure reveals a propagation law.

## Cubic Jensen gate

For a monic cubic
\[
p(x)=x^3+a x^2+b x+c,
\]
all three roots are real iff its discriminant is nonnegative together with the usual real-rootedness normalization. The exact discriminant is
\[
\boxed{\Delta_3(p)=a^2b^2-4b^3-4a^3c+18abc-27c^2.}
\]

For the normalized Jensen cubic, the project has already reduced the relevant Hermite determinant to the exact expression
\[
\widetilde Q_d
=2(d-3)vz-3(d-2)w^2-6(d-1)v^3.
\]
At \(d=3\),
\[
\boxed{\widetilde Q_3=-3w^2-12v^3.}
\]

This shows immediately that ordinary Stieltjes positivity \(v\ge0\) cannot prove the required sign. The actual coefficient sequence must supply a stronger theta-specific relation among \(v,w,z\), and the factorial conjugation is essential.

## New structural target

Do not attempt to prove \(v,w,z\) independently positive. Instead seek a theta-specific algebraic relation of the form
\[
\boxed{w^2+4v^3\le0}
\]
only if the sign conventions for the project's Hermite form make this exactly the required inequality. Because \(w^2\ge0\), this candidate is impossible when \(v\ge0\); therefore the correct next step is to re-check the sign convention/orientation of the Hermite determinant before imposing any inequality.

This is an important adversarial checkpoint: a contradiction here means the obstruction has been written with the opposite orientation, not that RH is false.

## Wedge strategy

The known Jensen theory proves hyperbolicity for sufficiently large shift \(n\) at each fixed degree \(d\). Hence a complete proof can be organized as:

1. establish the exact finite-degree gate for the remaining shifts;
2. prove a propagation lemma in \(n\) or a monotone multiplier relation;
3. use the asymptotic region only as the boundary condition;
4. eliminate the entire infinite complementary wedge.

The propagation lemma must be an exact theorem about the Jensen sequence; numerical continuation is not admissible.

## Candidate propagation invariant

Let
\[
r_j(n)=\frac{q_{n+j}}{q_n},
\]
and let \(\mathcal H_{d,n}\) denote a chosen Hermite determinant for \(J^{d,n}\). Search for an identity or inequality of the form
\[
\mathcal H_{d,n+1}-\Lambda_{d,n}\mathcal H_{d,n}
=\mathcal P_{d,n},
\qquad
\Lambda_{d,n}\ge0,
\quad
\mathcal P_{d,n}\ge0,
\]
where \(\mathcal P_{d,n}\) has an explicit theta-kernel representation.

Such an identity would convert the infinite shift problem into a boundary problem plus a positive propagation law. No such identity has yet been proved.

## Status

This frontier produces an exact finite-degree algebraic gate and a concrete propagation target. It is **not** an RH proof. The sign-orientation audit is mandatory before any positivity claim is accepted.
