# RH Frontier 112 — Exact degree-3 Jensen/Hermite multicopy audit

Date: 2026-09-17

## Executive result

The degree-3 Jensen discriminant can be derived exactly from the theta moment representation. The calculation closes the finite algebraic reduction, but it does **not** close RH: positivity of the resulting quartic moment polynomial is not implied by positivity of the underlying measure. A generic positive measure gives counterexamples, so any successful Riemann-specific proof must use additional arithmetic/theta structure.

## 1. Moment coefficients

Let
\[
\gamma_k=\frac{M_k}{(2k)!},\qquad M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du,
\]
with the exact completed-theta kernel used in the project. Define
\[
J_{3,n}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3.
\]
After dividing by \(\gamma_{n+3}\), write
\[
\widehat J_{3,n}(X)=X^3+aX^2+bX+c,
\]
where
\[
a=\frac{3\gamma_{n+2}}{\gamma_{n+3}},\qquad
b=\frac{3\gamma_{n+1}}{\gamma_{n+3}},\qquad
c=\frac{\gamma_n}{\gamma_{n+3}}.
\]

## 2. Exact cubic discriminant

For \(X^3+aX^2+bX+c\),
\[
\Delta=a^2b^2-4b^3-4a^3c-27c^2+18abc.
\]
Substitution gives the exact identity
\[
\boxed{
\gamma_{n+3}^4\Delta
=27\left(
3\gamma_n^2\gamma_{n+3}^2
-18\gamma_n\gamma_{n+1}\gamma_{n+2}\gamma_{n+3}
-4\gamma_n\gamma_{n+2}^3
-4\gamma_{n+1}^3\gamma_{n+3}
+3\gamma_{n+1}^2\gamma_{n+2}^2
\right).
}
\]
Equivalently,
\[
\gamma_{n+3}^4\Delta
=-27\left(
\gamma_n^2\gamma_{n+3}^2
-6\gamma_n\gamma_{n+1}\gamma_{n+2}\gamma_{n+3}
+4\gamma_n\gamma_{n+2}^3
+4\gamma_{n+1}^3\gamma_{n+3}
-3\gamma_{n+1}^2\gamma_{n+2}^2
\right).
\]
For real coefficients, cubic hyperbolicity is equivalent to \(\Delta\ge0\), including multiplicities.

## 3. Exact factorial-normalized moment form

Set
\[
A_1=(2n+1)(2n+2),
\]
\[
A_2=(2n+1)(2n+2)(2n+3)(2n+4),
\]
\[
A_3=(2n+1)(2n+2)(2n+3)(2n+4)(2n+5)(2n+6).
\]
Then
\[
\gamma_n=\frac{M_n}{(2n)!},\quad
\gamma_{n+1}=\frac{M_{n+1}}{(2n)!A_1},\quad
\gamma_{n+2}=\frac{M_{n+2}}{(2n)!A_2},\quad
\gamma_{n+3}=\frac{M_{n+3}}{(2n)!A_3}.
\]
Thus the sign of \(\Delta\) is exactly the sign of
\[
\boxed{
\mathcal D_n=
\frac{3M_n^2M_{n+3}^2}{A_3^2}
-\frac{18M_nM_{n+1}M_{n+2}M_{n+3}}{A_1A_2A_3}
-\frac{4M_nM_{n+2}^3}{A_2^3}
-\frac{4M_{n+1}^3M_{n+3}}{A_1^3A_3}
+\frac{3M_{n+1}^2M_{n+2}^2}{A_1^2A_2^2}.
}
\]
Indeed, \(\Delta=27\mathcal D_n/[(2n)!^4\gamma_{n+3}^4]\) up to the positive normalization already displayed above; the decisive point is the sign of the bracketed expression.

## 4. Four-copy representation

Let
\[
d\mu(u)=\Phi(u)\,du,
\qquad x=u^2.
\]
For independent variables \(u_1,u_2,u_3,u_4\), every quartic product of moments in \(\mathcal D_n\) is an exact integral against
\[
 d\mu(u_1)d\mu(u_2)d\mu(u_3)d\mu(u_4).
\]
For example,
\[
M_n^2M_{n+3}^2
=\int x_1^n x_2^n x_3^{n+3}x_4^{n+3}\,d\mu_1d\mu_2d\mu_3d\mu_4,
\]
and similarly for the other four monomials. Symmetrizing over all permutations of the four copies gives a canonical symmetric kernel \(\mathcal K_{3,n}(x_1,x_2,x_3,x_4)\) whose integral equals \(\mathcal D_n\).

This is the exact multicopy reduction. It is algebraically legitimate, but it does not make \(\mathcal K_{3,n}\) pointwise nonnegative.

## 5. Why a generic Vandermonde-square certificate cannot be assumed

The relevant symmetric kernel has total polynomial degree six in the \(x_i\). A four-variable Vandermonde square has degree twelve, so the naive identity
\[
\mathcal K_{3,n}=Q(x_1,\ldots,x_4)\prod_{i<j}(x_i-x_j)^2
\]
with polynomial \(Q\) of nonnegative degree cannot hold on degree grounds unless substantial cancellations or a different measure/kernel normalization are introduced.

A three-variable Vandermonde square has degree six and is therefore dimensionally compatible with the moment degree, but it would represent a three-copy Hankel determinant structure. The cubic Jensen discriminant is not the ordinary \(3\times3\) Hankel determinant of \((M_k)\); factorial normalization changes the coefficient geometry. Hence ordinary moment total positivity is insufficient.

## 6. Generic positive-measure counterexample to the shortcut

Take a positive two-atom measure
\[
\mu=0.9\,\delta_{1}+0.1\,\delta_{10}.
\]
Its factorial-normalized moment sequence is
\[
\gamma_k=\frac{0.9+0.1\,10^{2k}}{(2k)!}.
\]
The degree-three Jensen polynomial at \(n=0\) has negative cubic discriminant (direct exact/rational evaluation confirms the sign). Therefore:

> positivity of \(\Phi\), positivity of all raw Hankel moment matrices, and the mere fact that \(\gamma_k\) comes from a positive measure do not imply Jensen hyperbolicity.

This is an obstruction to the generic measure/Gram shortcut, not to the Riemann theta measure itself.

## 7. Exact remaining theta-specific theorem

The RH-bearing statement now has a sharply constrained form:

\[
\boxed{
\mathcal D_{d,n}[\Phi]\ge0
\quad\text{for every }d,n,
}
\]
where \(\mathcal D_{d,n}\) is the corresponding Jensen/Hermite discriminant/minor functional after factorial normalization.

For \(d=3\), the exact functional is the \(\mathcal D_n\) above. To continue to an RH proof one must derive its positivity from a property special to the completed Riemann theta lattice — for example an exact arithmetic/modular factorization, a total-positivity theorem, or a de Bruijn/Newman-type monotonicity statement that reaches the required endpoint.

Any proof that replaces this step by generic positive-measure reasoning is invalid.

## 8. Parallel-route closure status

- **Theta/Jensen:** exact degree-3 reduction completed; all-degree theta-specific positivity remains open.
- **Nyman–Beurling:** finite Gram positivity is established, but cyclicity/density is the RH-equivalent wall.
- **Li/Weil:** exact criteria are available, but an RH-independent positive factorization remains the wall.
- **de Bruijn–Newman:** monotonicity alone does not imply the endpoint value required for RH; an independent endpoint argument is still necessary.

## 9. Conclusion

This frontier closes the finite algebraic reduction and eliminates a major false shortcut. It does **not** prove RH. The remaining problem is now more rigid: obtain an unconditional, theta-specific all-degree positivity mechanism that survives the factorial normalization and is not equivalent to assuming the desired zero geometry.
