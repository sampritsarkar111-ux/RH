# Frontier 30 — Exact Degree-3 Jensen Gate in Theta-Moment Variables

## Status

This frontier derives an exact, root-independent degree-3 hyperbolicity condition for the Jensen polynomials of the xi function in the theta-moment normalization. It is a necessary research gate for an all-degree proof. It does **not** prove the Riemann Hypothesis.

## 1. Theta-moment normalization

Assume the standard cosine-transform representation

\[
\Xi(z)=C\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad \Phi(u)\ge0,
\]

and define

\[
M_k=\int_0^\infty u^{2k}\Phi(u)\,du.
\]

With

\[
a_k=\frac{k!}{(2k)!},
\]

the Taylor coefficients may be written, up to one positive global constant,

\[
\gamma_k=C(-1)^k a_kM_k.
\]

For the degree-3 Jensen polynomial

\[
J_{3,n}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3,
\]

divide by the nonzero leading coefficient \(\gamma_{n+3}\) to obtain the monic cubic

\[
p_{3,n}(X)=X^3+b_1X^2+b_2X+b_3.
\]

## 2. Exact coefficient reduction

Since

\[
\frac{a_n}{a_{n+3}}=8(2n+1)(2n+3)(2n+5),
\]

\[
\frac{a_{n+1}}{a_{n+3}}=4(2n+3)(2n+5),
\]

\[
\frac{a_{n+2}}{a_{n+3}}=2(2n+5),
\]

we get exactly

\[
\boxed{
\begin{aligned}
b_1&=-12(2n+3)(2n+5)\frac{M_{n+1}}{M_{n+3}},\\
b_2&=6(2n+5)\frac{M_{n+2}}{M_{n+3}},\\
b_3&=-8(2n+1)(2n+3)(2n+5)\frac{M_n}{M_{n+3}}.
\end{aligned}}
\]

No zeros of \(\Xi\), no root measure, and no RH assumption enter these identities.

## 3. Exact cubic hyperbolicity criterion

A real cubic is real-rooted if and only if its discriminant is nonnegative. Therefore

\[
p_{3,n}\text{ has three real roots}
\iff
\Delta_{3,n}\ge0,
\]

where

\[
\Delta_{3,n}=b_1^2b_2^2-4b_2^3-4b_1^3b_3-27b_3^2+18b_1b_2b_3.
\]

Introduce the positive consecutive moment ratios

\[
r_1=\frac{M_{n+1}}{M_n},\qquad
r_2=\frac{M_{n+2}}{M_{n+1}},\qquad
r_3=\frac{M_{n+3}}{M_{n+2}}.
\]

Then

\[
\frac{M_n}{M_{n+3}}=\frac1{r_1r_2r_3},\qquad
\frac{M_{n+1}}{M_{n+3}}=\frac1{r_2r_3},\qquad
\frac{M_{n+2}}{M_{n+3}}=\frac1{r_3}.
\]

Substitution gives a completely explicit rational polynomial condition in \((r_1,r_2,r_3,n)\). Equivalently, without expanding the large polynomial, the exact gate is

\[
\boxed{
\begin{aligned}
0\le \Delta_{3,n}
={}&[12(2n+3)(2n+5)]^2
 [6(2n+5)]^2\frac1{r_2^2r_3^2}\\
&-4[6(2n+5)]^3\frac1{r_3^3}\\
&-4[-12(2n+3)(2n+5)]^3[-8(2n+1)(2n+3)(2n+5)]
 \frac1{r_1r_2^4r_3^4}\\
&-27[8(2n+1)(2n+3)(2n+5)]^2\frac1{r_1^2r_2^2r_3^2}\\
&+18[-12(2n+3)(2n+5)][6(2n+5)][-8(2n+1)(2n+3)(2n+5)]
 \frac1{r_1r_2^2r_3^3}.
\end{aligned}}
\]

After multiplying by the positive denominator \(r_1^2r_2^4r_3^4\), this becomes a polynomial inequality with no divisions.

## 4. Why this is stronger than ordinary moment log-convexity

The positive measure only gives the Stieltjes/Hankel moment inequality

\[
M_{n+j}^2\le M_{n+j-1}M_{n+j+1}.
\]

Equivalently,

\[
r_1\le r_2\le r_3.
\]

But the cubic gate is a nonlinear inequality involving all three ratios and the arithmetic factors \((2n+1),(2n+3),(2n+5)\). Thus monotonicity of consecutive moment ratios is not, by itself, the desired theorem.

This establishes a precise hierarchy:

\[
\text{positive theta measure}
\Longrightarrow
r_1\le r_2\le r_3
\quad\not\Rightarrow\quad
\Delta_{3,n}\ge0.
\]

The missing ingredient must use additional structure of the specific Riemann theta kernel, not merely positivity.

## 5. Centered-moment formulation

Under the tilted probability measure

\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},
\qquad Y=u^2,
\]

we have

\[
\mathbb E_n[Y^k]=\frac{M_{n+k}}{M_n}.
\]

Hence

\[
r_1=\mathbb E_n[Y],
\]

\[
r_1r_2=\mathbb E_n[Y^2],
\]

\[
r_1r_2r_3=\mathbb E_n[Y^3].
\]

Therefore the degree-3 gate can be rewritten entirely in terms of the first three raw moments of the tilted variable \(Y\). Passing to centered moments

\[
\mu=\mathbb E_n[Y],
\qquad
\sigma^2=\mathbb E_n[(Y-\mu)^2],
\qquad
\kappa_3=\mathbb E_n[(Y-\mu)^3],
\]

is an algebraic change of variables. The resulting condition is an explicit cubic-scale constraint on \((\mu,\sigma^2,\kappa_3)\).

This identifies the next structural question: can the special theta kernel prove a sharp bound on the standardized skewness together with the variance bound from Frontier 28?

## 6. New proof target

A successful non-circular all-degree route would establish a family of theta-kernel inequalities controlling the complete centered-moment hierarchy strongly enough to imply every Jensen/Hermite principal minor.

For degree 2 the required condition is

\[
\frac{\operatorname{Var}_n(Y)}{\mathbb E_n[Y]^2}
\le \frac2{2n+1}.
\]

For degree 3 the exact discriminant above gives the next coupled condition involving \(\mathbb E_n[Y]\), \(\operatorname{Var}_n(Y)\), and \(\kappa_3\).

The research target is therefore not merely “prove log-convexity”, but

\[
\boxed{
\text{theta-kernel concentration/cumulant inequalities}
\Longrightarrow
\text{all Jensen discriminants and Hermite minors}\ge0.
}
\]

## 7. Anti-circularity and proof gate

This frontier does not assume:

- RH;
- the Laguerre–Pólya property of \(\Xi\);
- real-rootedness of any Jensen polynomial;
- a measure supported on zeros of \(\Xi\);
- a Hilbert–Pólya operator with the desired spectrum.

The remaining implication is genuinely open: deriving the exact cubic inequality, and eventually all higher Hermite inequalities, from the arithmetic/theta structure.

## 8. Conclusion

Frontier 30 converts the next Jensen level into an exact finite-dimensional moment gate. This is a genuine reduction of the proof problem, but **not a proof of RH**. The next decisive step is to derive a sharp theta-kernel inequality that implies the cubic gate and then generalize it to all degrees.
