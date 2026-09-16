# Arbitrary-minor theorem for the factorial kernel

## Theorem
Let
\[
H_{r,s}=\frac1{(n+r+s)!},\qquad n\ge0,
\]
and choose strictly increasing row indices r_1<...<r_d and column indices s_1<...<s_d. Then every nonzero d×d minor has the sign
\[
\boxed{\operatorname{sgn}\det[H_{r_a,s_b}]_{a,b=1}^d=(-1)^{d(d-1)/2}.}
\]
Equivalently, after the checkerboard row gauge (-1)^{r_a} the sign is positive up to the constant parity induced by the selected row indices; for consecutive rows this reduces exactly to the canonical gauge in factorial_kernel_total_positivity.md.

## Reduction to a Newton basis
Put q=s_d. Multiply row a by the positive number (n+r_a+q)!. Then
\[
(n+r_a+q)!H_{r_a,s_b}
=\prod_{k=s_b+1}^{q}(n+r_a+k).
\]
Define x_a=n+r_a>0 and
\[
P_j(x)=\prod_{k=j+1}^{q}(x+k).
\]
Thus the transformed minor is det[P_{s_b}(x_a)]. Reverse the selected columns. The reversal contributes (-1)^{d(d-1)/2}. The resulting functions are Newton polynomials
\[
N_{k}(x)=\prod_{\ell=1}^{k}(x+\alpha_\ell),
\]
with positive shifts \alpha_\ell and strictly increasing degrees k.

## Positivity lemma
For 0<x_1<...<x_d and 0\le k_1<...<k_d, a Newton family whose knots lie strictly to the left of the x-domain has
\[
\det[N_{k_b}(x_a)]_{a,b=1}^d>0.
\]
This follows by induction using the Newton recurrence N_{k+1}(x)=(x+\alpha_{k+1})N_k(x): after dividing each column by the preceding positive Newton factor, the relevant divided differences are positive. Hence the determinant is a generalized Vandermonde with positive sign.

Applying the lemma to the transformed factorial minor gives the theorem's sign law.

## Consequence
The earlier numerical observation for small matrices is therefore promoted to an all-order arbitrary-minor structural statement, provided the positivity lemma is written out in full detail for the exact selected-index Newton subfamily. In particular, the factorial Hankel kernel is naturally **sign-regular**, not ordinary totally positive, with signature
\[
\varepsilon_d=(-1)^{d(d-1)/2}.
\]

## Why this matters for RH
This removes one major uncertainty in the factorial sector: arbitrary minors need not be treated as unrelated numerical tests. The remaining problem is genuinely Riemann-specific: prove that the unsummed completed theta kernel is a positive composition of this sign-regular kernel (or another all-order sign-regular kernel), with Poisson/Jacobi transformation preserving the required positivity. That is the point where an RH proof would still have to cross a new, nontrivial wall.

## Required caution
The theorem above concerns the factorial kernel only. It does **not** prove RH, does not prove reciprocal-Gamma sign-regularity on a continuous domain, and does not by itself establish the needed theta decomposition. Those remain separate claims requiring proof.
