# Frontier 61 — Laguerre–Pólya gate: reduce the RH closure to a single global certificate

## Objective

Let \(\Xi(z)\) denote the completed Riemann xi function on the critical line, normalized so that it is an even real entire function. RH is equivalent to all zeros of \(\Xi\) being real.

A sufficient global route is to prove
\[
\boxed{\Xi\in\mathcal{LP}_{\mathbb R}},
\]
the real Laguerre–Pólya class.

For an even real entire function, one useful diagnostic is the logarithmic-derivative/Hermite structure. If
\[
\Xi(z)=C\prod_k\left(1-\frac{z^2}{\alpha_k^2}\right)
\]
with real \(\alpha_k\), then its Taylor/Jensen data obey all Hermite positivity conditions. Conversely, a complete proof must construct such a real-zero-preserving representation or an equivalent global certificate; checking finitely many Jensen polynomials is insufficient.

## New synthesis target

The zero-mode-corrected theta kernel from Frontier 60 should be transformed into a P\u00f3lya-frequency certificate rather than attacked one Hermite minor at a time.

The target is an explicit transform \(T\) such that
\[
\boxed{
\Xi(z)=T[\rho_0](z),
\qquad
T\text{ preserves real-rootedness / total positivity},
\qquad
\rho_0\text{ satisfies the hypotheses of }T.
}
\]

The decisive missing lemma would then be a theorem of the form
\[
\boxed{
\rho_0\in\mathcal C_{\mathrm{PF}}\Longrightarrow T[\rho_0]\in\mathcal{LP}_{\mathbb R},
}
\]
where \(\mathcal C_{\mathrm{PF}}\) is an explicitly defined, verifiable theta-kernel positivity class.

## Why this is stronger than the current Hermite program

The prior frontiers reduce individual low-order Hermite minors to explicit polynomial inequalities. Frontier 36 shows that generic Stieltjes moment positivity cannot supply the required sign. Frontier 60 shows that even the modularly symmetric theta measure requires exact zero-mode correction.

Therefore the next breakthrough should establish a *global* structural preservation theorem. Such a theorem would imply every degree and shift simultaneously rather than proving infinitely many inequalities independently.

## Adversarial requirements

Any claimed theorem must prove, not assume:

1. the exact integral transform from the corrected theta kernel to \(\Xi\);
2. convergence and permitted interchange of sums/integrals;
3. the precise positivity or total-positivity hypothesis;
4. preservation of real-rootedness or membership in \(\mathcal{LP}_{\mathbb R}\);
5. absence of hidden RH-equivalent assumptions;
6. treatment of the full function, not merely large shifts/degrees.

## Status

**New global closure target; not a proof.** The research program has now moved from isolated Hermite inequalities toward a single real-zero-preserving transform theorem. The missing preservation lemma remains the central obstruction.
