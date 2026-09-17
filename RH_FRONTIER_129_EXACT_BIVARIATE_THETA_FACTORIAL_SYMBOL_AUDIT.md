# Frontier 129 — Exact bivariate stability symbol of the unsummed theta/factorial operator

Date: 2026-09-17

## Conclusion

The exact bivariate symbol splits into two objects.

1. The factorial-only symbol is stable in every degree: the diagonal sequence
\[
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!}
\]
is a classical Laguerre multiplier sequence.

2. The full unsummed theta/factorial symbol is the Jensen polynomial of the completed Xi coefficients. Its all-degree stability remains the missing theta-specific theorem.

No RH or zero-location assumption is used.

## 1. Completed unsummed theta kernel

\[
\phi_m(u)=\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad
\Phi(u)=\sum_{m\ge1}\phi_m(u).
\]
The completed theta transformation gives \(\Phi(-u)=\Phi(u)\). The completed kernel must be formed before global moment integration; individual lattice terms are not treated as separate positive measures.

Set
\[
M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du,
\qquad
\gamma_k=\frac{M_k}{(2k)!}.
\]

## 2. Exact factorial diagonal operator

For fixed shift \(n\),
\[
\boxed{
\mathcal T_n\!\left[\sum_{j=0}^{d}a_jz^j\right]
=\sum_{j=0}^{d}\lambda_j^{(n)}a_jz^j,
\qquad
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!}.
}
\]
By duplication,
\[
\lambda_j^{(n)}=\frac{1}{4^j(n+\tfrac12)_j(n+1)_j},
\]
and its exponential generating function is
\[
\boxed{\Psi_n(z)={}_0F_2\!\left(;n+\tfrac12,n+1;z/4\right).}
\]

## 3. Exact bivariate algebraic symbol

\[
\boxed{
G_{n,d}(x,y):=\mathcal T_n[(x+y)^d]
=\sum_{j=0}^{d}\binom dj\frac{(2n)!}{(2n+2j)!}x^jy^{d-j}.
}
\]
Equivalently, \(G_{n,d}(x,y)=y^dg_{n,d}(x/y)\), where
\[
g_{n,d}(z)=\sum_{j=0}^{d}\binom dj\lambda_j^{(n)}z^j.
\]
For this homogeneous real polynomial, stability in the two upper half-planes is equivalent to all zeros of \(g_{n,d}\) being real and non-positive.

## 4. Factorial-symbol stability

Let
\[
\varphi_n(t)=\frac1{\Gamma(2t+2n+1)}.
\]
The reciprocal gamma function is in the Laguerre–Pólya class, and real affine rescaling preserves that class. Its zeros are
\[
t=-n-\frac12-\frac{k}{2},\qquad k=0,1,2,\ldots,
\]
all real and negative. Since \(\varphi_n(j)=1/(2n+2j)!\), the classical Laguerre multiplier-sequence theorem gives
\[
\boxed{\{\lambda_j^{(n)}\}_{j\ge0}\text{ is a multiplier sequence for every }n\ge0.}
\]
Consequently the Pólya–Schur algebraic-symbol criterion gives
\[
\boxed{G_{n,d}(x,y)\text{ is stable for every }n,d.}
\]
This is an unconditional theorem about the factorial operator alone.

## 5. Exact low-degree checks

For \(d=2\),
\[
\boxed{
\operatorname{Disc}(g_{n,2})
=\frac{4n+5}{(n+1)^2(n+2)(2n+1)^2(2n+3)}>0.
}
\]
For \(d=3\),
\[
\boxed{
\operatorname{Disc}(g_{n,3})=
\frac{27(64n^3+360n^2+656n+381)}
{16(n+1)^4(n+2)^3(n+3)^2(2n+1)^4(2n+3)^3(2n+5)^2}>0.
}
\]
For \(d=4\),
\[
\boxed{
\operatorname{Disc}(g_{n,4})=\frac{27P_6(n)}{4(n+1)^6(n+2)^5(n+3)^4(n+4)^3(2n+1)^6(2n+3)^5(2n+5)^4(2n+7)^3}>0,
}
\]
with
\[
P_6(n)=4096n^6+61440n^5+377856n^4+1216384n^3+2154896n^2+1983656n+736797.
\]

## 6. Exact unsummed theta/factorial symbol

Define
\[
\boxed{
(\mathcal A_n p)(x)=\frac1{(2n)!}\int_{\mathbb R}\Phi(u)u^{2n}(\mathcal T_np)(u^2x)\,du.
}
\]
Then \(\mathcal A_n[z^j]=\gamma_{n+j}x^j\), and the exact degree-\(d\) symbol is
\[
\boxed{
\Sigma_{n,d}(x,y)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}x^jy^{d-j}.
}
\]
Keeping the completed lattice explicit,
\[
\boxed{
\Sigma_{n,d}(x,y)=\frac1{(2n)!}\int_{\mathbb R}
\left(\sum_{m\ge1}\phi_m(u)\right)u^{2n}G_{n,d}(u^2x,y)\,du.
}
\]
This is the exact bivariate symbol requested.

## 7. Exact obstruction to naive positive averaging

Every local polynomial \(G_{n,d}(u^2x,y)\) is stable, but positive averaging of stable polynomials is not generically stability-preserving. For example,
\[
(X+Y)^2+(X+3Y)^2=2(X^2+4XY+5Y^2),
\]
whose dehomogenization has roots \(-2\pm i\). Thus
\[
G_{n,d}(u^2x,y)\text{ stable pointwise}+\Phi(u)\ge0
\]
does not imply stability of \(\Sigma_{n,d}\).

This is a generic obstruction, not a counterexample to the actual theta symbol.

## 8. Full-symbol stability is the missing theta theorem

Since \(\Sigma_{n,d}=J_{d,n}\), stability for every \(n,d\) is exactly hyperbolicity of every Jensen polynomial.

Degree 2:
\[
\boxed{\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}.}
\]
Degree 3, with \(q_j=\gamma_{n+j}/\gamma_n\), \(P_n=q_2/q_1^2\), \(Q_n=q_3/q_1^3\):
\[
\boxed{P_n\le1,\qquad |Q_n-(3P_n-2)|\le2(1-P_n)^{3/2}.}
\]

## 9. Numerical theta evidence (not proof)

High-precision evaluation gives approximately
\[
\gamma_0=0.4971207781883141,\quad
\gamma_1=0.01148597215757272,\quad
\gamma_2=1.234520180703180\times10^{-4},
\]
\[
\gamma_3=8.32355481385527\times10^{-7},\quad
\gamma_4=3.99222655134414\times10^{-9}.
\]
The degree-2 ratios for \(n=0,1,2,3\) are approximately
\[
2.1496878850,\ 1.5941154994,\ 1.4057377748,\ 1.3100630986.
\]
For \(n=0,1,2\), the cubic discriminant factor is approximately
\[
0.06400129246,\quad0.04865383647,\quad0.03259170079.
\]
These values are evidence only.

## 10. Exact frontier status

The clean separation is
\[
\boxed{
\text{factorial symbol stable in all degrees}
\quad\not\Rightarrow\quad
\text{unsummed theta symbol stable in all degrees}.
}
\]
The remaining proof-bearing target is the theta-specific closure theorem
\[
\boxed{
\Sigma_{n,d}(x,y)=\frac1{(2n)!}\int\Phi(u)u^{2n}G_{n,d}(u^2x,y)\,du
\text{ is stable for every }n,d,
}
\]
proved directly from the completed unsummed theta lattice and without zero locations.

No RH proof is claimed by this frontier.
