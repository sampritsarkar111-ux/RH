# Frontier 27 — Exact Newton–Hermite Closure and the Nonlinear Bottleneck

## Objective

Convert the all-degree Jensen-polynomial problem into an exact finite algebraic certificate, while identifying precisely why the theta/moment representation cannot simply be declared a positive Gram representation.

Let
\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j,
\qquad \gamma_k=\gamma(k),
\]
and assume its leading coefficient is nonzero. Write its monic normalization as
\[
p_{d,n}(x)=x^d+b_1x^{d-1}+\cdots+b_d.
\]

## 1. Newton sums are determined exactly by the coefficients

Define
\[
s_k=\sum_{r=1}^{d}\rho_r^k,
\]
where \(\rho_r\) are the roots of \(p\). Newton's identities give, without assuming the roots are real,
\[
\boxed{
 s_k+b_1s_{k-1}+b_2s_{k-2}+\cdots+b_{k-1}s_1+k b_k=0
\quad(1\le k\le d),
}
\]
and for \(k>d\),
\[
\boxed{
 s_k+b_1s_{k-1}+\cdots+b_ds_{k-d}=0.
}
\]
Thus every entry of the Hermite matrix
\[
H(p)=[s_{i+j}]_{0\le i,j<d}
\]
is an explicit polynomial in \(b_1,\ldots,b_d\).

## 2. Exact all-degree certificate

For a real polynomial \(p\),
\[
\boxed{
p\text{ is real-rooted}\iff H(p)\succeq0.
}
\]
Therefore the RH/Jensen route can be closed by proving
\[
\boxed{
H(p_{d,n})\succeq0\qquad\forall d\ge1,\ n\ge0.
}
\]
Equivalently, every principal minor of every \(H(p_{d,n})\) must be nonnegative. This is a finite algebraic condition for each fixed \((d,n)\), but there are infinitely many \((d,n)\).

## 3. Determinant identity and the discriminant

For a monic polynomial with roots \(\rho_1,\ldots,\rho_d\),
\[
\det H(p)=\prod_{1\le i<j\le d}(\rho_i-\rho_j)^2.
\]
Hence \(\det H(p)\ge0\) is necessary, but it is not sufficient by itself for real-rootedness. Lower principal minors are essential.

For the quartic \(p=x^4+b_1x^3+b_2x^2+b_3x+b_4\), the full determinant is exactly the quartic discriminant after identifying \((b_1,b_2,b_3,b_4)\) with the coefficient notation used in Frontier 25.

## 4. The key nonlinear obstruction

The exact theta representation supplies linear moment data for \(\gamma_n\). However, after monic normalization,
\[
 b_j=\frac{\binom dj\gamma_{n+j}}{\gamma_{n+d}},
\]
and Newton sums are nonlinear polynomials in these ratios.

Consequently, a representation of the form
\[
\gamma_k=\int t^k\,d\mu(t),\qquad d\mu\ge0,
\]
does **not** by itself imply
\[
H(p_{d,n})\succeq0.
\]
The required statement is a positivity theorem for nonlinear combinations of the moments. This is the exact point at which the earlier positive-mixture shortcut fails.

## 5. A non-circular Gram representation must therefore satisfy an extra identity

A valid proof must construct, from the theta kernel alone, a positive measure or positive semidefinite kernel satisfying
\[
H(p_{d,n})=
\int V_{d,n}(t)V_{d,n}(t)^T\,d\mu_{d,n}(t),
\qquad d\mu_{d,n}\ge0,
\]
with every coordinate of \(V_{d,n}\) explicitly defined independently of the unknown roots of \(p_{d,n}\).

Using
\[
V(t)=(1,t,\ldots,t^{d-1})^T
\]
and taking \(d\mu\) to be the root-counting measure would prove the identity only after real-rootedness is known; that is circular and is excluded.

## 6. New exact research target

The remaining mathematical problem has now been isolated to the following statement:

> **Theta-to-Hermite Positivity Theorem.** For every \(d,n\), derive an explicit root-independent positive kernel from the exact Riemann Xi/theta representation whose Gram matrix is exactly \(H(p_{d,n})\).

A proof must establish coefficient identification, positivity, convergence/interchange, and non-circularity. If such a theorem is proved, all Jensen polynomials are real-rooted, and the classical Jensen characterization supplies the final RH implication.

## Status

This frontier is an exact closure of the algebraic certificate and a sharper formulation of the missing theorem. It is **not** a proof of RH. No claim of a completed RH proof is made.
