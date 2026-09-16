# Frontier 110 — exact cubic Hermite test for the theta-moment Gram route

Date: 2026-09-16

## 1. Purpose

Frontier 109 reduced the all-degree program to an explicit multi-copy Gram problem. The first genuinely non-quadratic gate is Jensen degree \(d=3\). This frontier computes that gate exactly and tests whether positivity of the completed-theta measure alone can force it.

## 2. Exact cubic Hermite form

Write
\[
J(X)=\gamma_0+3\gamma_1X+3\gamma_2X^2+\gamma_3X^3,
\qquad \gamma_3\ne0,
\]
and normalize to
\[
\widehat J(X)=X^3+aX^2+bX+c,
\qquad
 a=\frac{3\gamma_2}{\gamma_3},\quad
 b=\frac{3\gamma_1}{\gamma_3},\quad
 c=\frac{\gamma_0}{\gamma_3}.
\]
Newton identities give
\[
s_1=-a,\quad s_2=a^2-2b,\quad s_3=-a^3+3ab-3c,
\]
\[
s_4=a^4-4a^2b+2b^2+4ac.
\]
Therefore the cubic Hermite matrix is
\[
\mathsf H_3=
\begin{pmatrix}
3&s_1&s_2\\
s_1&s_2&s_3\\s_2&s_3&s_4
\end{pmatrix},
\]
and its determinant is exactly the cubic discriminant
\[
\det\mathsf H_3
=-4a^3c+a^2b^2+18abc-4b^3-27c^2.
\]
After substitution of the Jensen coefficients,
\[
\boxed{
\det\mathsf H_3
=-\frac{27}{\gamma_3^4}
\left(
\gamma_0^2\gamma_3^2
-6\gamma_0\gamma_1\gamma_2\gamma_3
+4\gamma_0\gamma_2^3
+4\gamma_1^3\gamma_3
-3\gamma_1^2\gamma_2^2
\right).
}
\]
For real cubic coefficients, nonnegative discriminant is equivalent to all three roots being real (with multiplicity). Hence this is a complete degree-three hyperbolicity gate.

## 3. Substitution of the exact theta moments

From Frontier 109,
\[
\gamma_k=\frac{M_k}{(2k)!},
\qquad
M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du.
\]
Thus the degree-three condition is the exact quartic multi-moment inequality
\[
\boxed{
Q_3(M_0,M_1,M_2,M_3)\le0,
}
\]
where
\[
Q_3=
\frac{M_0^2M_3^2}{(6!)^2}
-6\frac{M_0M_1M_2M_3}{2!4!6!}
+4\frac{M_0M_2^3}{(4!)^3}
+4\frac{M_1^3M_3}{(2!)^3 6!}
-3\frac{M_1^2M_2^2}{(2!)^2(4!)^2}.
\]
Equivalently, multiplying by the positive common denominator,
\[
\boxed{
Q_3^{\!*}
= M_0^2M_3^2
-90M_0M_1M_2M_3
+2700M_0M_2^3
+360M_1^3M_3
-2700M_1^2M_2^2
\le0.
}
\]
This is an exact algebraic gate; no zero location is used.

## 4. Adversarial counterexample to a naive one-measure positivity theorem

Take any positive probability measure on \(Y=u^2\) with
\[
Y\in\{1,2\},\qquad \Pr(Y=1)=\Pr(Y=2)=\frac12.
\]
Then
\[
M_k=\frac{1+2^k}{2},
\]
so
\[
(\gamma_0,\gamma_1,\gamma_2,\gamma_3)
=\left(1,\frac34,\frac5{48},\frac1{160}\right).
\]
Direct exact substitution gives
\[
\boxed{
\det\mathsf H_3=-\frac{16957}{2764800}<0.
}
\]
Therefore positivity of the underlying measure \(\Phi(u)du\), even with all moments finite, cannot by itself imply Jensen degree-three hyperbolicity.

This does NOT test the actual Riemann theta measure; it eliminates only the generic claim that an arbitrary positive moment representation automatically supplies the required Gram certificate.

## 5. Consequence for the sought factorisation

A valid theta-derived certificate must exploit a Riemann-specific identity beyond positivity of \(\Phi\). The cubic gate shows precisely where such structure must enter. A candidate representation of the form
\[
\det\mathsf H_3=\int P(u)^2\Phi(u)\,du
\]
with a nonnegative integrand for every positive measure is impossible as a universal identity, because the two-point positive measure above makes the left side negative.

The remaining viable architecture is therefore genuinely Riemann-specific and/or multi-copy:
\[
\boxed{
\det\mathsf H_3
=\int_{\mathbb R^q}
\mathcal A_3(u_1,\ldots,u_q)\,
\prod_{j=1}^q\Phi(u_j)\,du_j,
}
\]
where the theta reflection/Poisson structure must force the integrated value to have the required sign, or equivalently produce a sum-of-squares after a nontrivial algebraic transformation.

## 6. Next proof-bearing gate

Do not jump to degree four. First derive the exact four-fold integral for \(Q_3^{\!*}\) by introducing independent variables \(Y_1,Y_2,Y_3,Y_4\), symmetrizing the polynomial, and testing whether its symmetrization admits a Vandermonde-square plus theta-reflection remainder. The key question is whether the completed theta functional equation supplies an exact positive remainder unavailable to generic positive measures.

A successful identity here would be the first concrete Riemann-specific all-degree Gram mechanism. Failure by an exact negative theta-induced term should instead be recorded as a route obstruction.

## 7. Status

This frontier is a rigorous degree-three algebraic reduction and adversarial obstruction to the naive positive-measure Gram idea. It does not prove RH.
