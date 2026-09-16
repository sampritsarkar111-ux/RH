# Frontier 43 — all-degree endgame protocol and falsification matrix

## Purpose

Convert the remaining RH problem into a finite list of theorem obligations, while explicitly preventing a finite-order result from being mistaken for RH.

## Gate A — coefficient Turan hierarchy

For the Xi-side coefficient sequence \(\gamma_n\), prove for every admissible \(n\) the inequalities required by Jensen hyperbolicity, beginning with
\[
\gamma_{n+2}^2-\gamma_{n+1}\gamma_{n+3}\ge0
\]
and the stronger centered degree-3 condition
\[
4v^3+w^2\le0.
\]
Frontier 42 supplies an exact theta/incomplete-Gamma representation but not positivity.

## Gate B — all-degree Jensen hyperbolicity

For every degree \(d\ge1\) and shift \(n\ge0\), prove that the Jensen polynomial is real-rooted. A sufficient exact certificate is positivity of the appropriate Hermite matrix (with the sign convention fixed from the monic polynomial). Every principal-minor inequality must be proved uniformly in \(d,n\), not numerically sampled.

## Gate C — Toeplitz/exterior-power closure

Independently, prove total positivity/sign-regularity of every consecutive Xi coefficient minor. Existing Jacobi–Trudi/Desnanot–Jacobi identities can propagate information only after an unconditional strict inequality closes the unresolved wedge.

## Gate D — Riemann-specific kernel theorem

Generic positive Stieltjes moment arguments are insufficient: earlier exact atomic counterexamples violate the needed higher Hermite cone. Therefore the missing theorem must use the actual theta kernel, its modular relation, or an equivalent Riemann-specific structure.

## Gate E — adversarial falsification

Before accepting any proposed positivity lemma, test it against:
- finite positive atomic measures;
- the raw continuous kernel, including its negative sectors;
- small-degree symbolic specializations;
- large-index asymptotic regimes;
- boundary cases where centered variance tends to zero.
A lemma that survives only because the theta measure is special must state that dependence explicitly.

## Gate F — final RH implication audit

A completed proof must explicitly establish:
1. analytic continuation and normalization of the Xi function used;
2. exact equivalence between the proved coefficient/Jensen/Toeplitz property and all zeros lying on \(\Re s=1/2\);
3. every interchange of sum, integral, derivative, determinant, and limit;
4. convergence and sign preservation in every infinite operation;
5. strict versus non-strict cases and multiplicities;
6. absence of any step that assumes RH or an equivalent statement.

## Current status

Frontiers 39–42 provide exact reductions and falsification results. They materially narrow the proof search but do not supply Gate B/C/D. Therefore the project must **not** label RH proved at this stage.
