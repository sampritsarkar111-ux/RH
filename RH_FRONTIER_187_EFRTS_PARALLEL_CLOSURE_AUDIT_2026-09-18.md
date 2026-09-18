# RH Frontier 187 — EFRTS Parallel Closure Audit — 2026-09-18

## Scope

This file records the Frontier 187 construction and audit for the Riemann Hypothesis (RH) program. The proposed numeral/encoding system is **EFRTS: Explicit-Formula Resonant Ternary System**.

> Status discipline: this is a research construction and audit, not a proof of RH. The remaining gates below are explicitly marked open.

## 1. Proposed EFRTS

For n >= 1, define

\[
\boxed{\mathfrak E(n)=\left((v_p(n))_{p\in\mathbb P},\mu(n),\lambda(n),\Lambda(n),\chi_3(n),\tau(n)\right)}
\]

where:
- \(v_p(n)\) is the p-adic valuation;
- \(\mu(n)\) is the Möbius function;
- \(\lambda(n)=(-1)^{\Omega(n)}\) is the Liouville function;
- \(\Lambda(n)\) is the von Mangoldt function;
- \(\chi_3(n)\) is the real Dirichlet character modulo 3;
- \(\tau(n)\) is a balanced-ternary encoding of the valuation vector.

The valuation stream reconstructs n exactly:

\[
\boxed{n=\prod_{p\in\mathbb P}p^{v_p(n)}}.
\]

The component functions are standard; the research proposal is their explicit coupling into a single arithmetic encoding.

## 2. Closed identity-level gates

### Euler prime-power structure

\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=
\sum_p\sum_{k\ge1}\frac{\log p}{p^{ks}},
\qquad \Re(s)>1.
}
\]

EFRTS contains \(\Lambda(n)\) exactly, so the encoding is compatible with the Euler prime-power expansion.

### Archimedean/Gamma completion

\[
\boxed{
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\xi(s)=\xi(1-s).
}
\]

This closes the standard normalization/completion identity, but does **not** prove RH.

### Correct Möbius/Liouville bridges

For \(\Re(s)>1\),

\[
\boxed{
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)},
\qquad
\sum_{n\ge1}\frac{\lambda(n)}{n^s}=\frac{\zeta(2s)}{\zeta(s)}.
}
\]

The second identity corrects the earlier false identification of the Liouville Dirichlet series with \(1/\zeta(s)\).

## 3. Remaining proof-bearing gates

| Gate | Status | Exact requirement |
|---|---|---|
| EFRTS -> Weil quadratic form | OPEN | Prove \(Q_{EFRTS}(g)=Q_{Weil}(g)\) for every admissible g, including convergence and all prime/archimedean/zero terms. |
| Li criterion | PARTIAL | Identity \(\lambda_n=\sum_\rho[1-(1-1/\rho)^n]\) is standard; all-order nonnegative Li coefficients remain equivalent to RH. |
| Nyman-Beurling | PARTIAL | The RH-equivalent density/cyclicity criterion is known; an independent proof of the required density remains open. |
| de Branges realization | OPEN | Construct a genuine de Branges space independently of RH and derive the RH-bearing positivity/reproducing-kernel statement. |
| Self-adjoint spectral determinant | OPEN | Construct an independent self-adjoint H and prove \(\det_*(F(H,s))=C(s)\xi(s)\), \(C(s)\ne0\), without encoding the zeros into H by definition. |
| Zero-spectrum correspondence | OPEN | Derive \(\rho=1/2+i\gamma\iff\gamma\in\operatorname{Spec}(H)\) from the independent construction. |

## 4. Anti-circularity rule

A numeral representation alone cannot alter the zeros of \(\zeta\). Therefore a successful EFRTS route must produce a new analytic invariant or an exact theorem connecting EFRTS coordinates to an RH-equivalent positivity, density, or self-adjoint spectral statement.

In particular, the following is insufficient:

\[
\text{new encoding}\quad\Longrightarrow\quad\text{RH}.
\]

A valid finish must instead establish one of the proof-bearing bridges above.

## 5. Numerical consistency checks

The completed xi-function formula gives, for example,

\[
\xi(2)=\frac{\pi}{6},
\qquad
\xi(4)=\frac{\pi^2}{15},
\]

and the functional equation numerically matches at tested points. The first several Li coefficients are positive in numerical evaluation. These are consistency checks only and do not establish all-order positivity.

## 6. Frontier 187 conclusion

**Closed at identity level:** arithmetic Euler structure, standard archimedean completion, and corrected Möbius/Liouville identities.

**Still open:** the decisive EFRTS-to-Weil bridge, all-order Li positivity, Nyman-Beurling density proof, independent de Branges realization, independent self-adjoint determinant, and non-circular zero-spectrum correspondence.

The research program therefore remains an RH proof attempt, not a completed proof.
