# RH Frontier 122 — Exact Theta Transfer Operator Candidate — 2026-09-17

## Objective
Move directly from the completed theta kernel to an operator, without another finite Jensen-positivity test.

## Exact starting point
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\qquad \Phi(-u)=\Phi(u).
\]
Define the even transform operator formally by
\[
(C_t f)(u)=\frac12\big(f(u+t)+f(u-t)\big).
\]
Its Fourier multiplier is \(\cos(t\xi)\). Thus, for a suitable cyclic vector \(v\), the scalar quantity \(\langle v,C_t v\rangle\) is a cosine spectral transform.

## Canonical multiplication model
Let \(x=u^2\) and define the moment functional
\[
L[p]=\int_{\mathbb R}p(u^2)\Phi(u)\,du.
\]
Whenever the theta functional is positive on squares (this must be proved, not assumed), Gram-Schmidt applied to \(1,x,x^2,\ldots\) gives orthonormal polynomials \(p_n(x)\), and multiplication by \(x\) has a Jacobi representation
\[
Jp_n=b_{n+1}p_{n+1}+a_np_n+b_np_{n-1},\qquad b_n>0.
\]
The coefficients are exact moment determinants:
\[
a_n=\frac{\langle xp_n,p_n\rangle}{\langle p_n,p_n\rangle},
\qquad
b_{n+1}=\frac{\langle xp_n,p_{n+1}\rangle}{\|p_{n+1}\|\|p_n\|}.
\]
By the spectral theorem, if this construction is valid, then
\[
\Xi(t)=\langle 1,\cos(t\sqrt J)1\rangle.
\]
This is an exact theta-to-self-adjoint spectral representation at the level of a matrix element, not yet a determinant identity.

## Critical distinction
A self-adjoint \(J\) alone does NOT imply RH from the last display: a matrix element \(\langle1,\cos(t\sqrt J)1\rangle\) can have complex zeros. Therefore the proof-bearing upgrade must derive an additional characteristic/perturbation determinant identity
\[
\Xi(t)=E(t)\,\det(I-F(t,J)),
\]
where \(F(t,J)\) is defined intrinsically from the theta transfer structure and every zero of the right side is forced by real spectral parameters.

## New target: theta transfer determinant
Rather than guessing a Jacobi determinant, define the transfer matrix of the Jacobi recurrence
\[
\binom{P_{n+1}(\lambda)}{P_n(\lambda)}=
\begin{pmatrix}
(\lambda-a_n)/b_{n+1}&-b_n/b_{n+1}\\
1&0
\end{pmatrix}
\binom{P_n(\lambda)}{P_{n-1}(\lambda)}.
\]
The required theorem is an explicit theta identity identifying the limiting boundary function of this transfer system with the completed Xi function after a fixed spectral-variable map.

## Independent Herglotz companion
A second exact target is a theta-defined Weyl function \(m(z)\) satisfying
\[
\operatorname{Im}m(z)>0\quad(\operatorname{Im}z>0),
\]
with \(m\) equal to a fixed transform of \(\Xi'/\Xi\). If both the Herglotz property and exact equality are derived from theta data, the poles are confined to the real spectral axis.

## Status
Established: the multiplication/Jacobi representation is a mathematically canonical construction conditional on positivity of the theta moment functional, and it gives an exact spectral matrix-element representation.

Not established: positivity of the theta moment functional, the Xi perturbation-determinant identity, and the zero-preserving spectral-variable map. These are the actual theorem targets. No RH conclusion is claimed here.
