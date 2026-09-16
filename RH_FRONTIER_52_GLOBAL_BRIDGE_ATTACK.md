# Frontier 52 — global bridge attack: from positive theta atoms to Turan/Jensen

## Status

This frontier organizes the next three proof mechanisms after the new all-order atomwise positivity theorem. It deliberately separates exact identities, sufficient conditions, and conjectural bridges.

## 1. Positive atomic representation

For
\[
M_m=\sum_{k\ge1}B_m(\pi k^2),
\]
Frontier 50 establishes
\[
B_m(\pi k^2)>0.
\]
Thus `M_m` is a positive discrete sum, but this alone does not determine its curvature in `m`.

## 2. Exact factorial-conjugate Turan gate

With `q_m=m!/(2m)!` and `gamma_m=Cq_mM_m`,
\[
\gamma_{m+1}^2-\gamma_m\gamma_{m+2}\ge0
\]
is equivalent to
\[
\boxed{
\frac{M_{m+1}^2}{M_mM_{m+2}}
\ge
\frac{(m+2)(2m+3)}{(m+1)(2m+1)}.
}
\]
This is the exact local gate that must feed the degree-3 Jensen condition.

## 3. Total-positivity mechanism

Define the positive atom matrix
\[
\mathsf B_{m,k}=B_m(\pi k^2).
\]
The natural orientation suggested by direct numerical exploration is
\[
\mathsf B_{m,k}\mathsf B_{m+1,k+1}
-\mathsf B_{m,k+1}\mathsf B_{m+1,k}\le0,
\]
which is equivalent to `B_{m+1}(pi k^2)/B_m(pi k^2)` decreasing in `k` whenever all entries are positive.

This is a **research target**, not yet a theorem. A proof would be valuable because monotone likelihood ratios can convert discrete sums into covariance inequalities.

## 4. Ratio representation

Set
\[
R_m(k)=\frac{B_{m+1}(\pi k^2)}{B_m(\pi k^2)}.
\]
Then
\[
M_{m+1}=\sum_k B_m(\pi k^2)R_m(k),
\]
so
\[
\frac{M_{m+1}}{M_m}=E_m[R_m(K)],
\]
where `P_m(K=k)=B_m(pi k^2)/M_m`.

Likewise,
\[
\frac{M_{m+2}}{M_{m+1}}
=E_{m+1}[R_{m+1}(K)].
\]
The Turan gate therefore becomes a comparison of adjacent tilted expectations. This reframes the problem as a discrete transport inequality rather than a pointwise kernel inequality.

## 5. Degree-3 endgame

Once the adjacent gamma Turan inequality is proved for all required indices, the exact degree-3 Hermite condition remains stronger:
\[
\boxed{4v^3+w^2\le0}.
\]
Therefore the next decisive step is not merely another numerical Turan check. It is an all-index theorem controlling the centered third moment `w` relative to the negative variance-like invariant `v` for the specific Riemann coefficient sequence.

## 6. New falsification protocol

Before accepting any proposed total-positivity or likelihood-ratio theorem, test:

1. small `m,k`;
2. adjacent and non-adjacent `k`;
3. large `m` asymptotics;
4. the exact incomplete-Gamma representation from Frontier 48;
5. the first theta atom against the tail;
6. the sign after factorial normalization.

A theorem that survives only finite numerical checks remains a conjecture.

## 7. Audit

**New:** a positive-atom transport formulation of the remaining Turan bridge and an explicit total-positivity/likelihood-ratio target.

**Proved previously:** all-order positivity of each `B_m(pi k^2)`.

**Still open:** the transport inequality, degree-3 cone, all-degree Jensen hyperbolicity, global Xi sign-regularity, and RH.
