# Riemann Hypothesis — Frontier 20: Operator-Preimage Audit and a New Closure Program

Date: 2026-09-16

## 1. Objective

The previous research branch identified the canonical Pólya/Jensen coefficients

\[
\gamma_n = C\,\frac{n!}{(2n)!}M_n,
\qquad
M_n=\int_0^\infty \Phi(t)t^{2n}\,dt,
\]
where the nonzero constant \(C\) is irrelevant to hyperbolicity.

The associated Jensen polynomials are

\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]

The universal hyperbolicity of these polynomials is equivalent to RH by the Pólya/Jensen criterion.

## 2. First correction: degree 2 is not the true bottleneck

For \(d=2\), hyperbolicity is equivalent to

\[
\gamma_{n+1}^2\ge \gamma_n\gamma_{n+2},
\]
which is exactly

\[
M_{n+1}^2\ge \frac{2n+1}{2n+3}M_nM_{n+2}.
\]

The classical Csordas–Norfolk–Varga theorem proves the corresponding Turán inequalities for the Riemann \(\xi\)-function coefficients. Therefore the research branch must not continue treating degree 2 as an unproved RH obstruction. The previous Frontier-11 status was too conservative.

This does **not** prove RH: all degrees remain required.

## 3. Exact operator bridge

Define

\[
B(x)=\sum_{n\ge0}M_n\frac{x^n}{n!},
\qquad
(T_aB)(x)=\sum_{n\ge0}a_nM_n\frac{x^n}{n!},
\qquad
 a_n=\frac{n!}{(2n)!}.
\]

Then

\[
T_aB(x)=\sum_{n\ge0}M_n\frac{x^n}{(2n)!}.
\]

After the standard substitution \(x=-z^2\), this is the even entire function obtained from the Riemann \(\Xi\)-function. Thus the RH problem can be viewed as a zero-preservation problem for the diagonal operator \(T_a\).

The exponential generating function of the multiplier sequence \(a_n\) is

\[
\sum_{n\ge0}a_n\frac{z^n}{n!}
=\sum_{n\ge0}\frac{z^n}{(2n)!}
=\cosh(\sqrt z),
\]
while with the alternating sign it is

\[
\sum_{n\ge0}(-1)^na_n\frac{z^n}{n!}
=\cos(\sqrt z).
\]

Hence \((a_n)\) is a classical Pólya–Schur multiplier sequence.

## 4. Critical logical direction

The multiplier theorem gives only the forward implication

\[
B\in LP
\quad\Longrightarrow\quad
T_aB\in LP.
\]

It does **not** give

\[
T_aB\in LP
\quad\Longrightarrow\quad
B\in LP.
\]

This direction cannot be silently reversed. The reciprocal diagonal sequence

\[
\left(\frac{(2n)!}{n!}\right)_{n\ge0}
\]
is not a classical multiplier sequence in the required transcendental sense; in particular, the naive inverse-operator argument is invalid.

Therefore the exact new target is an **LP preimage theorem specialized to the Riemann moment sequence**, not a generic multiplier-sequence inversion theorem.

## 5. New closure target

A sufficient RH proof would follow from either of the following genuinely infinite statements:

### Target A — Riemann moment preimage theorem

Prove directly that

\[
B(x)=\int_0^\infty\Phi(t)e^{xt^2}\,dt
\in LP^+_I.
\]

Then Pólya–Schur immediately gives

\[
T_aB\in LP,
\]
and hence RH.

### Target B — direct all-degree Jensen transport

Prove for every \(d,n\ge0\) that

\[
J_{d,n}(X)=
\sum_{j=0}^d\binom dj
\frac{(n+j)!}{(2n+2j)!}M_{n+j}X^j
\]
has only real zeros.

This avoids any need to invert \(T_a\).

## 6. Proposed new mechanism: positive-kernel factorization

The Riemann moment representation suggests searching for a representation of every Jensen discriminant/Hermite determinant in the form

\[
\mathcal D_{d,n}
=
\int_{(0,\infty)^r}
W_{d,n}(t_1,\ldots,t_r)
\prod_{i<j}(t_i^2-t_j^2)^2\,dt_1\cdots dt_r,
\]
with \(W_{d,n}\ge0\) proved from the explicit theta kernel \(\Phi\).

A successful identity would simultaneously explain the known low-degree Turán inequalities and could potentially establish all-degree hyperbolicity without locating any zeta zeros.

This is a research target, not an asserted identity: the required positive factorization has not yet been proved.

## 7. Current global obstruction

The 2026 literature contains an explicit unconditional positivity wedge for consecutive Toeplitz minors of normalized Riemann-xi coefficients, but it applies only when

\[
k\ge 10^{18}r^3.
\]
The complementary regime remains the essential difficulty. Finite verification and asymptotic fixed-degree results cannot close the universal quantifier.

## 8. Non-circularity test

Any future proof in this branch must pass all four checks:

1. No assertion about zero locations may be used before RH is proved.
2. No finite numerical computation may replace an infinite quantifier.
3. Every transform must be used in a direction actually justified by a zero-preservation theorem.
4. Every claimed positive determinant must have an explicit analytic proof of nonnegativity/strict positivity.

## 9. Status

**RH is not proved by this document.**

The concrete advance of Frontier 20 is structural: the degree-2 route is removed as a false bottleneck, the exact multiplier direction is separated from its invalid inverse, and the remaining problem is reduced to a precise Riemann-kernel LP-preimage theorem or an equivalent all-degree positive-determinant construction.
