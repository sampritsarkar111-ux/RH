# Self-weighted Hamburger bridge — 2026-09-16

## Status
New exact RH-equivalent route; **not a proof**.

A recent 2026 preprint by Blaize Rouyea and Corey Bourgeois gives a self-weighted Hamburger criterion for the Riemann xi function. Define, for every nontrivial zero `rho` (with multiplicity),

\[
v_\rho=-\frac{1}{(\rho-1/2)^2},\qquad
\tau_r=\sum_\rho v_\rho^{r+1}.
\]

The reported criterion is

\[
\boxed{\mathrm{RH}\iff H_N=[\tau_{i+j+1}]_{i,j=0}^{N}\succeq0\quad\text{for every }N\ge0.}
\]

The special feature is **self-weighting**: the same node `v_rho` supplies both the location and the moment weight. Their rigidity theorem says that positivity of every finite Hamburger matrix forces every node to be positive real. Since

\[
v_\rho>0
\iff
(\rho-1/2)^2<0\text{ is real negative}
\iff
\Re\rho=1/2,
\]

this gives a direct route from an all-order Hankel positivity theorem to RH.

## Why this is useful

The previous attack was a two-parameter family of Toeplitz minors
\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1}.
\]
The new target compresses the zero-location problem into one infinite Hankel tower:
\[
\boxed{\forall N:\quad \det[\tau_{i+j+1}]_{i,j=0}^{N}>0.}
\]

This is conceptually cleaner because there is no independent shift parameter `k`.

## Exact obstacle

The missing theorem is now sharply stated:

> Prove, without assuming RH, that the sequence `(tau_{r+1})_{r\ge0}` is a Hamburger moment sequence, i.e. every finite Hankel matrix `[tau_{i+j+1}]` is positive semidefinite (or positive definite in the nondegenerate setting).

Merely rewriting the `tau_r` through `xi'/xi`, Li coefficients, or the Weil explicit formula does not close this gap. A representation by a signed/complex measure is insufficient; the required representing measure must be positive on the real line.

## Proposed next attack

1. Derive an explicit-formula representation of `tau_r` that is valid unconditionally.
2. Package the resulting quadratic form
   \[
   \sum_{i,j=0}^{N}c_i\overline{c_j}\tau_{i+j+1}
   \]
   into a single kernel `K(x,y)`.
3. Test whether `K` is positive semidefinite by an exact Gram decomposition, not pointwise positivity alone.
4. If the kernel splits into an archimedean and prime-power part, determine whether the two pieces form a genuinely positive combined object rather than separately divergent terms.
5. Stress-test every proposed positivity identity against finite signed zero configurations; this prevents an accidental RH assumption from entering through a hidden factorization.

## Adversarial warning

The statement that the Hankel tower is positive is already RH-equivalent. Therefore any derivation that inserts the critical-line parametrization `rho=1/2+i gamma` for all zeros, or factors xi using only critical-line zeros, is circular.

## Literature

Rouyea–Bourgeois, `Self-Weighted Hamburger Rigidity for the Riemann Xi Function`, submitted 25 Aug 2026. The current public abstract reports the criterion and the self-weighted rigidity mechanism.

Michalowski's July 2026 result remains relevant to the independent Toeplitz route: it proves `D_{r,k}>0` for `k >= 10^18 r^3` but explicitly leaves the complementary region open.

## Research verdict

This is a **new reduction/target**, not a solution. The next decisive step is an unconditional positive-kernel/Gram representation for the entire `tau` Hankel tower. If such a representation is found and proved, the self-weighted rigidity theorem would convert it into RH.