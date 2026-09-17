# Frontier 111 — Master Closure Gate: exact d=3 reduction and cross-route audit

Date: 2026-09-17

## Status

This document converts the five-route program into a proof-bearing algebraic checkpoint. It does **not** claim RH is proved. The purpose is to isolate the first exact identity whose successful positivity would imply the required all-degree Jensen/hyperbolicity gate.

## 1. Fixed zero-independent baseline

Work with the completed function

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \Xi(t)=\xi(1/2+it).
\]

Assume only the standard theta/Fourier representation and analytic properties already established in the project. No zero is assigned a location.

With the project's even positive kernel,

\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\]

and

\[
g(z):=\Xi(\sqrt{-z})=\sum_{k\ge0}\gamma_kz^k,
\qquad
\gamma_k=\frac{M_k}{(2k)!},
\quad
M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du.
\]

Positivity of \(\Phi\) alone is **not** enough to imply that the Jensen polynomials are hyperbolic.

## 2. Exact cubic Jensen polynomial

For shift \(n\), degree three is

\[
J_{3,n}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3.
\]

Its monic form is

\[
\widehat J(X)=X^3+aX^2+bX+c,
\]
with

\[
a=3\frac{\gamma_{n+2}}{\gamma_{n+3}},\qquad
b=3\frac{\gamma_{n+1}}{\gamma_{n+3}},\qquad
c=\frac{\gamma_n}{\gamma_{n+3}}.
\]

## 3. Exact Hermite matrix

Let \(s_k\) be Newton power sums of the roots. Then

\[
s_1=-a,
\quad s_2=a^2-2b,
\quad s_3=-a^3+3ab-3c,
\]

\[
s_4=a^4-4a^2b+2b^2+4ac.
\]

Therefore

\[
\boxed{
\mathsf H_3=
\begin{pmatrix}
3&-a&a^2-2b\\
-a&a^2-2b&-a^3+3ab-3c\\
a^2-2b&-a^3+3ab-3c&a^4-4a^2b+2b^2+4ac
\end{pmatrix}.}
\]

Its principal minors are

\[
\det H_1=3,
\qquad
\det H_2=2(a^2-3b),
\]

and

\[
\boxed{
\det H_3=-4a^3c+a^2b^2+18abc-4b^3-27c^2.}
\]

The last expression is exactly the cubic discriminant.

## 4. Exact coefficient form

Substituting the Jensen coefficients gives

\[
\boxed{
\det H_3
=-\frac{27}{\gamma_{n+3}^4}
\left(
\gamma_n^2\gamma_{n+3}^2
-6\gamma_n\gamma_{n+1}\gamma_{n+2}\gamma_{n+3}
+4\gamma_n\gamma_{n+2}^3
+4\gamma_{n+1}^3\gamma_{n+3}
-3\gamma_{n+1}^2\gamma_{n+2}^2
\right).}
\]

Thus a complete degree-three proof requires proving both relevant principal-minor inequalities, in particular the discriminant inequality, from the theta representation without assuming real zeros.

## 5. Proof-bearing multi-copy target

Insert

\[
\gamma_k=\frac1{(2k)!}\int u^{2k}\Phi(u)\,du
\]

into the polynomial above. Every degree-q monomial becomes a q-fold integral against the positive product measure

\[
\prod_{r=1}^q\Phi(u_r)\,du_r.
\]

The exact target is therefore a finite algebraic identity

\[
\boxed{
\mathcal D_{3,n}
=\int_{\mathbb R^q}
\mathcal K_{3,n}(u_1,\ldots,u_q)
\prod_{r=1}^q\Phi(u_r)\,du_r,
}
\]

followed by a theta-specific sum-of-squares/Binet-Cauchy/Vandermonde factorisation

\[
\boxed{
\mathcal K_{3,n}=\sum_\alpha |A_\alpha|^2
}
\]

or a decomposition into explicitly nonnegative terms. A merely positive one-variable moment argument is insufficient.

## 6. Cross-route master object: precise version

The slogan

\[
\mathcal P_\theta=\mathcal G_\theta=\mathcal L_\theta=\mathcal S_\theta\succeq0
\]

must not be treated as an identity until the spaces, domains, kernels, and maps are explicitly defined. The rigorous target is instead to construct a common positive sesquilinear form \(Q_\theta\) and explicit maps

\[
T_P,T_G,T_L,T_S
\]

such that

\[
Q_\theta(T_Pf,T_Pf)=Q_\theta(T_Gf,T_Gf)=Q_\theta(T_Lf,T_Lf)=Q_\theta(T_Sf,T_Sf)\ge0
\]

on a common dense test class, with each representation independently derived from theta data.

The final bridge must then prove one of:

1. Pick/Herglotz positivity of the logarithmic derivative and its pole theorem;
2. all-degree Jensen hyperbolicity;
3. Weil positivity;
4. a self-adjoint spectral realization whose spectrum is exactly the zero set of \(\Xi\).

## 7. Hard anti-circularity rules

- Never parameterize an unknown zero as \(1/2+it\).
- Never define an operator using the unknown zero set.
- Never infer all-order positivity from finitely many minors.
- Never replace an exact theta lattice by a numerically fitted kernel.
- Every limiting operation must carry a convergence theorem.
- Multiplicities must be preserved.
- Any theorem called "RH-bearing" must include the exact implication to real zeros of \(\Xi\).

## 8. Current conclusion

The exact d=3 algebra is now closed. The missing proof-bearing content is not the Hermite criterion itself; it is the theta-specific positive factorisation of the resulting multi-copy coefficient expression. Success there is a genuine new theorem. Failure with an exact negative minor would instead close this particular ansatz and redirect the attack.

**No RH claim is made in this frontier.**
