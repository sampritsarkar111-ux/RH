# Frontier 64 — exact cubic gate and wedge strategy

## Purpose

Frontier 63 replaced the overly broad PF∞ target by a uniform Jensen certificate. The next concrete attack is to make the first nontrivial finite-degree gate completely explicit and then ask whether its theta structure reveals a propagation law.

## Cubic Jensen gate

For a monic cubic
\[
p(x)=x^3+a x^2+b x+c,
\]
its discriminant is
\[
\boxed{\Delta_3(p)=a^2b^2-4b^3-4a^3c+18abc-27c^2.}
\]
For a real cubic, \(\Delta_3(p)>0\) means three distinct real roots; \(\Delta_3(p)=0\) gives a repeated-root degeneration. Thus the discriminant is an exact finite-degree gate.

## Existing factorial-weighted obstruction

The project has an exact Hermite-form reduction
\[
\widetilde Q_d
=2(d-3)vz-3(d-2)w^2-6(d-1)v^3.
\]
At \(d=3\),
\[
\boxed{\widetilde Q_3=-3(w^2+4v^3).}
\]

If the external factor relating \(\widetilde Q_d\) to the selected Hermite determinant is positive, then ordinary Stieltjes positivity \(v\ge0\) forces \(\widetilde Q_3\le0\). Therefore a proof requiring \(\widetilde Q_3\ge0\) cannot come from ordinary Stieltjes positivity. The sign/orientation convention of the selected Hermite gate must be audited before any positivity assertion is accepted.

This is an adversarial checkpoint, not a contradiction to RH.

## Correct structural target

Do not attempt to prove \(v,w,z\) independently positive. The actual question is:

\[
\boxed{\text{Can the exact theta/factorial representation determine the required orientation of the cubic Hermite gate?}}
\]

Once the orientation is fixed, the next target is an explicit theta-kernel identity for the correctly oriented quantity.

## Uniform-shift propagation target

Known Jensen theory proves hyperbolicity for sufficiently large shift \(n\) at each fixed degree \(d\). Therefore a complete proof can be organized as:

1. establish the exact finite-degree gate for the remaining shifts;
2. prove a propagation lemma in \(n\) or an exact multiplier relation;
3. use the asymptotic hyperbolic region only as a boundary condition;
4. eliminate the entire infinite complementary wedge.

The propagation lemma must be an exact theorem about the Jensen sequence; numerical continuation is not admissible.

## Candidate propagation invariant

Let
\[
r_j(n)=\frac{q_{n+j}}{q_n},
\]
and let \(\mathcal H_{d,n}\) denote a chosen Hermite determinant for \(J^{d,n}\). Search for
\[
\mathcal H_{d,n+1}-\Lambda_{d,n}\mathcal H_{d,n}
=\mathcal P_{d,n},
\qquad
\Lambda_{d,n}\ge0,
\quad
\mathcal P_{d,n}\ge0,
\]
with \(\mathcal P_{d,n}\) admitting an explicit theta-kernel representation.

Such an identity would convert the infinite shift problem into a boundary problem plus a positive propagation law. No such identity has yet been proved.

## Status

This frontier gives an exact finite-degree discriminant gate and a concrete uniform-shift propagation target. It is **not an RH proof**. The sign-orientation audit is mandatory before any positivity claim is accepted.
