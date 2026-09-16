# Degree-3 Jensen discriminant from the unsummed Riemann theta lattice

## Executive result

For the normalized Jensen polynomial
\[
J_{n,3}(X)=a_n+3a_{n+1}X+3a_{n+2}X^2+a_{n+3}X^3,
\]
the exact cubic discriminant is
\[
\boxed{
\mathcal D_n=
162a_na_{n+1}a_{n+2}a_{n+3}
-108a_na_{n+2}^3
+81a_{n+1}^2a_{n+2}^2
-108a_{n+1}^3a_{n+3}
-27a_n^2a_{n+3}^2.
}
\]
The important point is that, unlike the ordinary Hankel determinant, this is not automatically a positive moment determinant.

## 1. Exact unsummed theta representation

Use the completed Riemann Xi cosine transform
\[
\Xi(t)=\int_0^\infty\Phi(u)\cos(tu)\,du,
\]
where
\[
\Phi(u)=\sum_{r\ge1}\phi_r(u),
\qquad
\phi_r(u)=2\pi r^2e^{5u/2}(2\pi r^2e^{2u}-3)e^{-\pi r^2e^{2u}}.
\]
For every \(u\ge0,r\ge1\), \(\phi_r(u)>0\).

Define
\[
a_m=(-1)^m\Xi^{(2m)}(0)
=\int_0^\infty u^{2m}\Phi(u)\,du
=\sum_{r\ge1}\mu_{m,r},
\]
with
\[
\mu_{m,r}:=\int_0^\infty u^{2m}\phi_r(u)\,du.
\]
Hence every \(a_m>0\).

## 2. Exact lattice-level expression

Introduce three independent lattice indices \(r,s,t\). Every product in \(\mathcal D_n\) becomes an exact triple sum over \(r,s,t\), but the terms carry different moment exponents. Define
\[
M_k(r):=\int_0^\infty u^{2k}\phi_r(u)\,du.
\]
Then
\[
a_k=\sum_{r\ge1}M_k(r).
\]
Consequently
\[
\boxed{
\mathcal D_n=
\sum_{r,s,t\ge1}\mathfrak d_n(r,s,t),
}
\]
where the exact unsummed lattice integrand is
\[
\boxed{
\begin{aligned}
\mathfrak d_n(r,s,t)= {}&
162M_n(r)M_{n+1}(s)M_{n+2}(t)M_{n+3}(\ell)\\
&-108M_n(r)M_{n+2}(s)M_{n+2}(t)M_{n+2}(\ell)\\
&+81M_{n+1}(r)M_{n+1}(s)M_{n+2}(t)M_{n+2}(\ell)\\
&-108M_{n+1}(r)M_{n+1}(s)M_{n+1}(t)M_{n+3}(\ell)\\
&-27M_n(r)M_n(s)M_{n+3}(t)M_{n+3}(\ell),
\end{aligned}
}
\]
with a fourth independent index \(\ell\). Thus the precise lattice object is actually a **four-copy** sum, not a three-copy sum.

More transparently, define four independent variables \(u_1,u_2,u_3,u_4\) and
\[
\Phi_j:=\Phi(u_j).
\]
Then
\[
\boxed{
\begin{aligned}
\mathcal D_n={}&\int_{(0,\infty)^4}\Phi_1\Phi_2\Phi_3\Phi_4\,\mathcal P_n(u_1,u_2,u_3,u_4)\,d^4u,
\\
\mathcal P_n={}&162u_1^{2n}u_2^{2n+2}u_3^{2n+4}u_4^{2n+6}
-108u_1^{2n}u_2^{2n+4}u_3^{2n+4}u_4^{2n+4}
\\
&+81u_1^{2n+2}u_2^{2n+2}u_3^{2n+4}u_4^{2n+4}
-108u_1^{2n+2}u_2^{2n+2}u_3^{2n+2}u_4^{2n+6}
\\
&-27u_1^{2n}u_2^{2n}u_3^{2n+6}u_4^{2n+6}.
\end{aligned}
}
\]
This is the exact direct unsummed theta-lattice formula.

## 3. Homogeneous factorization

Factor out \((u_1u_2u_3u_4)^{2n}\) and put
\[
x_j=u_j^2>0.
\]
Then
\[
\boxed{
\mathcal P_n=(x_1x_2x_3x_4)^n Q(x_1,x_2,x_3,x_4),
}
\]
where
\[
\boxed{
Q=162x_2x_3^2x_4^3
-108x_2^2x_3^2x_4^2
+81x_1x_2x_3^2x_4^2
-108x_1x_2x_3x_4^3
-27x_3^3x_4^3.
}
\]
Factor further:
\[
\boxed{
Q=27x_3x_4^2
\left(
6x_2x_3x_4-4x_2^2x_3+3x_1x_2x_3-4x_1x_2x_4-x_3^2x_4
\right).
}
\]
This polynomial is **not pointwise nonnegative** on \((0,\infty)^4\). For example, taking \(x_1=x_2=x_3=x_4=1\) gives
\[
Q(1,1,1,1)=27(6-4+3-4-1)=0,
\]
but changing the variables independently can make the bracket positive or negative. Therefore the naive termwise positive decomposition fails.

## 4. A useful exact identity: the discriminant as a root-separation invariant

For a cubic
\[
p(X)=A X^3+B X^2+C X+D,
\]
\[
\operatorname{Disc}(p)=
B^2C^2-4AC^3-4B^3D-27A^2D^2+18ABCD.
\]
For
\[
A=a_{n+3},\quad B=3a_{n+2},\quad C=3a_{n+1},\quad D=a_n,
\]
this gives the formula above.

If \(J_{n,3}\) has three real roots, \(\mathcal D_n\ge0\); conversely, because all coefficients are positive, \(\mathcal D_n>0\) is the algebraic condition for three distinct real roots (with the usual cubic reality criterion). Thus this determinant/discriminant is genuinely relevant to Jensen hyperbolicity.

## 5. Why a direct positive decomposition is difficult

The four-copy integrand \(Q\) contains both positive and negative monomials. Hence neither
\[
\mathcal D_n=\int \text{(pointwise nonnegative kernel)}
\]
nor a termwise nonnegative lattice sum follows from positivity of \(\Phi\).

This is qualitatively different from the previous Hankel determinant, whose Vandermonde-square representation was automatically nonnegative.

Therefore the exact residual against a **naive monomial-positive decomposition** is nonzero and sign-indefinite. There is no valid claim of a manifestly positive decomposition at this stage.

## 6. Stronger structural reformulation

The correct question is whether the four-copy polynomial can be symmetrized over permutations of the four variables into a sum of squares or a positive combination of Schur/Vandermonde-type invariants. Let
\[
\operatorname{Sym}_4 Q:=\sum_{\sigma\in S_4}Q(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)},x_{\sigma(4)}).
\]
A positive decomposition of the form
\[
\boxed{
\operatorname{Sym}_4Q
=\sum_\lambda c_\lambda S_\lambda(x_1,x_2,x_3,x_4),
\qquad c_\lambda\ge0,
}
\]
or, more strongly,
\[
\boxed{
\operatorname{Sym}_4Q
=\sum_k c_kR_k(x)^2,\qquad c_k\ge0,
}
\]
would provide the desired finite-degree mechanism.

However, symmetrization is not by itself enough: because \(\mathcal D_n\) is already symmetric after integration against the identical product measure, one must prove that the symmetrized polynomial is nonnegative on the positive orthant, not merely that selected coefficients are positive.

## 7. Exact residual status

At the level of the unsummed theta lattice, define \(P_3^{+}\) to be any proposed pointwise-positive/sum-of-squares component obtained from an explicit algebraic decomposition of \(Q\). The exact residual is
\[
\boxed{
E_3=\mathcal D_n-P_3^{+}
=\int \Phi_1\Phi_2\Phi_3\Phi_4
\left[(x_1x_2x_3x_4)^nQ-P_3^{+}\right]d^4u.
}
\]
For the naive choice \(P_3^{+}=0\), this is simply \(E_3=\mathcal D_n\), whose integrand is sign-indefinite. No nontrivial positive decomposition has been established here.

## 8. Critical correction to the earlier program

The earlier statement that one could simply seek
\[
\mathcal D_n=P_3+E_3,
\qquad P_3\ge0,
\]
and expect \(E_3=0\) from the theta positivity was too optimistic. The cubic Jensen discriminant is not a moment Hankel determinant, and its integrand is not automatically Vandermonde-square positive.

Thus the genuine degree-three wall is now explicit:
\[
\boxed{
\text{Find an exact algebraic/representation-theoretic positive decomposition of the four-copy }Q,
}
\]
possibly after the **Poisson/Jacobi transformation at the lattice-kernel level** rather than after collapsing the theta sum.

## 9. Current conclusion

The direct calculation establishes:

1. The cubic Jensen discriminant has the exact formula above.
2. It admits an exact four-copy unsummed theta representation.
3. Its raw lattice integrand contains unavoidable-looking positive and negative monomials.
4. Positivity of the theta kernel alone does not yield a positive decomposition.
5. No exact positive decomposition, and therefore no RH proof, has been established by this calculation.

The next decisive computation is to apply Poisson/Jacobi to the **four-copy unsummed kernel before integrating or collapsing the lattice**, then test whether the transformed symmetric polynomial admits a Vandermonde-square/Schur-positive or Gram-square decomposition. A successful identity there would be a genuinely stronger mechanism than ordinary Hankel positivity.
