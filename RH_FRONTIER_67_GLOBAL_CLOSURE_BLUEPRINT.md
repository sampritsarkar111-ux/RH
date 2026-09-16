# Frontier 67 — Global RH closure blueprint

Date: 2026-09-16
Status: research target; not a proof

## Objective

Use the Jensen-polynomial equivalence without confusing any finite-degree certificate with RH. The exact target is

RH ⇔ J_{d,n}(X)=Σ_{j=0}^d C(d,j)γ(n+j)X^j is hyperbolic for every d,n≥0.

The current program splits the universal implication into three auditable layers.

## Layer A — all-degree Hermite positivity

For each d,n form the Hermite matrix H(J_{d,n}). A sufficient and necessary real-rootedness criterion is positivity of the appropriate Hermite/Hankel signature, including degeneracy/rank conditions. The research target is a Riemann-specific inequality proving all required principal minors have the correct sign for every d,n.

## Layer B — centered invariant hierarchy

After translation by r_1, the degree-d Jensen polynomial is expressed through centered invariants. Degree 3 introduces (v,w); degree 4 adds z; degree 5 adds h. Therefore an eventual theorem must control the entire centered sequence, not only a finite prefix. Candidate mechanism: derive these invariants directly from the theta integral and exploit exact kernel identities before applying moment inequalities.

## Layer C — heat-flow alternative

Use the de Bruijn-Newman deformation H_λ and seek a rigorous inequality forcing Λ≤0. Any Lyapunov functional must be defined globally, have a rigorously signed derivative, and have boundary/tail terms controlled uniformly. A local or numerical monotonicity result is insufficient.

## Mandatory falsification gates

1. Test every proposed moment inequality on arbitrary positive atomic measures.
2. Test finite Jensen degrees and indices separately; never extrapolate finite ranges.
3. Check zero/degenerate Hermite cases explicitly.
4. Track all limiting operations and theta-series tail bounds.
5. Require a final theorem with explicit ∀d,n quantifiers or a logically complete Λ≤0 proof.

## Current hard obstruction

The known positive theta-kernel representation alone does not force the canonical Jensen inequalities. Recent PF_k obstructions also make an unconditional PF_∞ shortcut unsafe. Consequently the missing ingredient must be a stronger Riemann-specific structural identity/inequality.

## Endgame theorem required

Produce either:

(A) a proof that every J_{d,n} is hyperbolic for all d,n, or

(B) a proof that the de Bruijn-Newman constant Λ≤0.

Only after one of (A)/(B) is proved with all analytic details may the repository label RH proved.

## Status

No complete proof has been obtained in this frontier. This file is a proof blueprint and falsification contract, not a claim of resolution.