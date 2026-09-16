# RH Frontier 121 — Unsummed Theta Lattice, Poisson/Jacobi Transformation, and the Cubic Pairing Test

Date: 2026-09-16

## 1. Completed theta kernel before collapsing the lattice

Let
\[
\vartheta(t)=\sum_{m\in\mathbb Z}e^{-\pi m^2t},\qquad t>0.
\]
Since the zero mode is killed by differentiation,
\[
\Phi(u)=t^{9/4}\vartheta''(t)+\frac32t^{5/4}\vartheta'(t),\qquad t=e^{2u}.
\]
Equivalently, retaining the lattice explicitly,
\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}}.
\]

## 2. Poisson/Jacobi transformation before summation collapse

Jacobi inversion is
\[
\vartheta(t)=t^{-1/2}\vartheta(1/t).
\]
Differentiating twice and substituting into the completed differential combination gives the exact identity
\[
\boxed{\Phi(u)=e^{-9u/2}\vartheta''(e^{-2u})+\frac32e^{-5u/2}\vartheta'(e^{-2u})=\Phi(-u).}
\]
Thus the Poisson-dual lattice is still present before any moment integration or lattice collapse. The transformation is exact and introduces no RH assumption.

## 3. Exact cubic Toeplitz minor

For
\[
g(z)=\sum_{n\ge0}\gamma_nz^n,
\qquad
\gamma_n=\frac1{(2n)!}\int_{\mathbb R}u^{2n}\Phi(u)\,du,
\]
the adjacent cubic Toeplitz minor is
\[
\boxed{
\Delta_{3,k}=\det\begin{pmatrix}
\gamma_k&\gamma_{k+1}&\gamma_{k+2}\\
\gamma_{k-1}&\gamma_k&\gamma_{k+1}\\
\gamma_{k-2}&\gamma_{k-1}&\gamma_k
\end{pmatrix}
=-\gamma_{k-2}\gamma_k\gamma_{k+2}+\gamma_{k-2}\gamma_{k+1}^2+\gamma_{k-1}^2\gamma_{k+2}-2\gamma_{k-1}\gamma_k\gamma_{k+1}+\gamma_k^3.
}
\]

Substitution of the unsummed lattice gives an exact triple-lattice/triple-integral expansion of each of the five terms. The Poisson-transformed version is obtained by replacing each \(\Phi(u_i)\) with the dual expression in Section 2 before performing the \(u_i\)-integrals.

## 4. Why the naive Vandermonde-square mechanism does not close

A genuine Vandermonde-square identity normally comes from an Andréief/Hankel determinant,
\[
\det\left[\int x^{i+j}\,d\mu(x)\right]
=\frac1{r!}\int\!\cdots\!\int\prod_{a<b}(x_a-x_b)^2\prod_jd\mu(x_j).
\]
The cubic object above is instead Toeplitz in the coefficient index and has the factorially corrected entries
\[
\frac{M_{k+j-i}}{(2k+2j-2i)!},
\qquad M_n=\int u^{2n}\Phi(u)\,du.
\]
The denominator depends on the individual matrix entry through \(k+j-i\). It cannot be factored into independent row and column weights. Therefore the five signed terms cannot be converted, by the ordinary determinant/Andréief step, into one common determinant of monomials whose antisymmetrization automatically squares to a Vandermonde.

This is an exact algebraic obstruction, not a numerical failure.

## 5. What the Poisson transformation actually accomplishes

Jacobi inversion pairs the original and dual lattice exactly and proves evenness of \(\Phi\). It does **not** turn the factorial-corrected Toeplitz minor into a positive Gram determinant. The transformed lattice still contains the derivative combination
\[
q^{9/4}\vartheta''(q)+\frac32q^{5/4}\vartheta'(q),
\qquad q=e^{-2u},
\]
whose individual lattice summands are signed.

Hence there is no established identity of the form
\[
\Delta_{3,k}=\sum_{m_1,m_2,m_3}W_{m_1,m_2,m_3}
\,\bigl(\prod_{a<b}(X_a-X_b)^2\bigr),
\qquad W_{m_1,m_2,m_3}\ge0,
\]
obtained merely by Poisson pairing of the unsummed lattice.

## 6. Precise surviving target

The first viable all-order mechanism would need an additional transformation that handles the factorial kernel itself, not just the theta lattice. A proof-bearing target is therefore a total-positivity/variation-diminishing factorization of the coefficient kernel
\[
K(n,u)=\frac{u^{2n}}{(2n)!}
\]
combined with the Poisson-paired theta measure, or an equivalent stability-preserving operator identity.

The cubic calculation therefore gives a useful negative result: **Poisson/Jacobi symmetry alone does not supply the required Vandermonde-square positivity.** The missing ingredient is the factorial/stability transform.

No RH proof is claimed.