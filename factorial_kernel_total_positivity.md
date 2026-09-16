# Factorial-Kernel Total-Positivity Mechanism

## Status

Research note for the Riemann Hypothesis program. The identities in Sections 1–3 below are exact. The continuous reciprocal-Gamma extension and the Riemann-theta positivity implication remain open targets; this note does **not** claim a proof of the Riemann Hypothesis.

## 1. Discrete factorial Hankel kernel

Define

\[
K_n(i,j)=\frac{1}{(n+i+j)!},\qquad i,j=0,\ldots,d-1,
\]

for integers \(n\ge 0\). Then

\[
\boxed{
\det\!\left[\frac1{(n+i+j)!}\right]_{i,j=0}^{d-1}
=
(-1)^{d(d-1)/2}
\frac{\displaystyle\prod_{0\le i<j\le d-1}(j-i)}
{\displaystyle\prod_{i=0}^{d-1}(n+i+d-1)!}
}
\]

Hence

\[
(-1)^{d(d-1)/2}\det K_n>0.
\]

### Derivation

Multiply row \(i\) by \((n+i+d-1)!\). The resulting entry is

\[
B_{ij}=\frac{(n+i+d-1)!}{(n+i+j)!}
=\prod_{r=j+1}^{d-1}(n+i+r).
\]

As a polynomial in \(x_i=n+i\), column \(j\) has degree \(d-1-j\) and leading coefficient 1. Reversing the columns gives polynomial degrees \(0,1,\ldots,d-1\), hence a Vandermonde determinant. Column reversal contributes \((-1)^{d(d-1)/2}\).

## 2. Exact 3x3 obstruction

For \(d=3\),

\[
K_n=
\begin{pmatrix}
1/n!&1/(n+1)!&1/(n+2)!\\
1/(n+1)!&1/(n+2)!&1/(n+3)!\\
1/(n+2)!&1/(n+3)!&1/(n+4)!
\end{pmatrix}
\]

and

\[
\boxed{
\det K_n=-\frac{2(n+3)(n+4)^2}{[(n+4)!]^3}<0.
}
\]

Thus the raw factorial kernel is not ordinary TP_3. Its determinant has the fixed sign predicted by
\( (-1)^{3(2)/2}=-1 \).

For \(n=0\),

\[
\det K_0=-\frac1{144}.
\]

## 3. Correct structural target: sign-regularity

The relevant signature is

\[
\varepsilon_d=(-1)^{d(d-1)/2}.
\]

The target is therefore sign-regularity rather than direct total positivity:

\[
\boxed{\varepsilon_d\,\Delta_d[K]\ge0}
\]

for the relevant minors. A future proof must distinguish consecutive minors (already covered by the exact formula above) from arbitrary minors.

## 4. Reciprocal-Gamma formulation

The factorial kernel is the integer specialization of

\[
K(x,y)=\frac1{\Gamma(x+y+1)}.
\]

A natural all-order conjectural extension is that this kernel is strictly sign-regular on an appropriate domain, with order-\(d\) signature

\[
\operatorname{sgn}\det[K(x_i,y_j)]_{i,j=1}^d
=(-1)^{d(d-1)/2}
\]

whenever the determinant is nonzero and the hypotheses on \(x_i,y_j\) guarantee the stated kernel domain/order. This continuous statement is **not established by the discrete calculation alone** and must be proved independently.

## 5. Riemann-theta target

The next Riemann-specific question is whether the completed theta kernel can be represented, after the required Poisson/Jacobi transformation, as a positive mixture or closure of sign-regular factorial-type kernels:

\[
\Theta_{\rm comp}(u,v)=\sum_{n\ge0}w_nK_n(u,v),\qquad w_n\ge0,
\]

or an analytically equivalent positive integral/Gram representation.

If such a representation exists, the determinant should be attacked through Cauchy–Binet/Andreief-type expansions rather than by searching for a single \(V^2\) factor. The desired structure is schematically

\[
\boxed{
\sum_{n_1<\cdots<n_d}
W_{n_1,\ldots,n_d}
\Delta(n_1,\ldots,n_d)
\Delta(x_1,\ldots,x_d)
\Delta(y_1,\ldots,y_d),
\qquad W_{n_1,\ldots,n_d}\ge0.
}
\]

The exact form of the completed-theta weights and whether they preserve the required sign-regularity is the central unresolved step.

## 6. Research status

- Exact consecutive factorial determinant: **proved**.
- Exact fixed parity sign: **proved for the consecutive minors above**.
- Arbitrary-minor reciprocal-Gamma sign-regularity: **target; requires proof**.
- Positive sign-regular decomposition of the completed Riemann theta kernel: **open target**.
- Deduction of RH from such a mechanism: **not established**.

## 7. Next attack

1. Start from the **unsummed** completed theta lattice.
2. Apply Poisson/Jacobi transformation before collapsing lattice sums.
3. Isolate the degree-six / 3x3 determinant kernel.
4. Express its factorial sector in the sign-regular basis above.
5. Compute all cross-terms exactly.
6. Test whether the completed weights admit a positive Cauchy–Binet/Gram expansion.
7. If successful, formulate and prove the corresponding all-order sign-regularity theorem.
8. Only after those steps establish whether the resulting positivity is sufficient for the desired RH criterion.

**Important:** positivity of this kernel alone is not a proof of the Riemann Hypothesis. The bridge from the completed theta kernel to the zero-location criterion must also be proved.
