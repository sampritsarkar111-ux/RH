# RH Frontier 124 — Explicit Theta Jacobi Operator and Exact Xi Determinant Identity — 2026-09-17

## Status
This file records a rigorous operator construction obtained directly from the completed Riemann-theta kernel. It does **not** prove RH. The construction closes the canonical theta-to-Jacobi and theta-to-Xi matrix-element steps, while the spectral-determinant/zero-correspondence step remains open.

## 1. Exact theta starting point

Use
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\qquad \Phi(-u)=\Phi(u),
\]
with the completed Riemann theta kernel \(\Phi\).

Set \(x=u^2\) and define the positive measure on \((0,\infty)\)
\[
d\nu(x)=\frac{\Phi(\sqrt{x})}{\sqrt{x}}\,dx.
\]
Then for every polynomial \(p\),
\[
L[p]=\int_0^\infty p(x)\,d\nu(x)
=\int_{\mathbb R}p(u^2)\Phi(u)\,du.
\]
Its moments are
\[
M_n=L[x^n]=\int_{\mathbb R}u^{2n}\Phi(u)\,du.
\]

## 2. Canonical self-adjoint operator

Let
\[
\mathcal H=L^2((0,\infty),d\nu),
\]
and define the multiplication operator
\[
(Af)(x)=xf(x),
\qquad
\mathcal D(A)=\{f\in\mathcal H:xf\in\mathcal H\}.
\]
Because \(x\) is real-valued, \(A\) is self-adjoint and positive.

The spectral theorem gives
\[
\langle 1,f(A)1\rangle=\int_0^\infty f(x)\,d\nu(x).
\]

## 3. Explicit Jacobi matrix

Let \(p_n\) be the monic orthogonal polynomials for \(d\nu\), with
\[
\int p_np_m\,d\nu=0\quad(n\ne m).
\]
Let
\[
D_n=\det[M_{i+j}]_{i,j=0}^{n},\qquad D_{-1}=1.
\]
The monic recurrence is
\[
xp_n=p_{n+1}+a_np_n+\beta_np_{n-1},
\]
where
\[
\beta_n=\frac{D_nD_{n-2}}{D_{n-1}^2}>0
\]
whenever the moment problem is nondegenerate, and
\[
a_n=\frac{\int xp_n(x)^2\,d\nu(x)}{\int p_n(x)^2\,d\nu(x)}.
\]
After normalization \(q_n=p_n/\sqrt{h_n}\), \(h_n=\int p_n^2d\nu\), multiplication by \(x\) is represented by
\[
J=
\begin{pmatrix}
 a_0&b_1&0&0&\cdots\\
 b_1&a_1&b_2&0&\cdots\\
 0&b_2&a_2&b_3&\cdots\\
 0&0&b_3&a_3&\ddots\\
 \vdots&\vdots&\vdots&\ddots&\ddots
\end{pmatrix},
\qquad b_n=\sqrt{\beta_n}>0.
\]
Thus \(J\) is self-adjoint (as the Jacobi representation of the self-adjoint multiplication operator, with the standard closure of the polynomial domain).

## 4. First coefficients

\[
p_0(x)=1,
\qquad
p_1(x)=x-\frac{M_1}{M_0}.
\]
Therefore
\[
a_0=\frac{M_1}{M_0},
\qquad
b_1^2=\frac{M_0M_2-M_1^2}{M_0^2}.
\]
Also
\[
p_2(x)=x^2+Ax+B,
\]
with
\[
A=\frac{M_1^2-M_0M_3}{M_0M_2-M_1^2},
\qquad
B=\frac{M_1M_3-M_2^2}{M_0M_2-M_1^2},
\]
and hence
\[
a_1=
\frac{M_0^2M_3-2M_0M_1M_2+M_1^3}
{M_0(M_0M_2-M_1^2)}.
\]

## 5. Exact Xi matrix-element identity

Let \(e_0=1/\sqrt{M_0}\) in the normalized polynomial basis. Since \(J\) is multiplication by \(u^2\), functional calculus gives
\[
\boxed{
\frac{\Xi(t)}{\Xi(0)}
=\langle e_0,\cos(t\sqrt J)e_0\rangle.
}
\]
Indeed,
\[
\langle e_0,J^ke_0\rangle=\frac{M_k}{M_0},
\]
so
\[
\langle e_0,\cos(t\sqrt J)e_0\rangle
=\sum_{k\ge0}\frac{(-1)^kt^{2k}}{(2k)!}\frac{M_k}{M_0}
=\frac{\Xi(t)}{\Xi(0)}.
\]
This is an exact identity, provided the standard moment/series interchange justified by the completed theta kernel is used.

## 6. Exact rank-one determinant identity

Let \(P_0=|e_0\rangle\langle e_0|\). Since \((\cos(t\sqrt J)-I)P_0\) is rank one,
\[
\det\left(I+(\cos(t\sqrt J)-I)P_0\right)
=1+\langle e_0,(\cos(t\sqrt J)-I)e_0\rangle.
\]
Therefore
\[
\boxed{
\frac{\Xi(t)}{\Xi(0)}
=\det\left(I+(\cos(t\sqrt J)-I)P_0\right).
}
\]
This is an exact Fredholm/rank-one determinant representation of the Xi matrix element.

## 7. Critical limitation — this is not yet the RH spectral determinant

The tempting identity
\[
\Xi(t)/\Xi(0)=\lim_{N\to\infty}\det(I-t^2J_N^{-1})
\]
is **not derived** here and must not be asserted.

A matrix element of a self-adjoint operator need not have only real zeros. Likewise, the rank-one determinant above does not by itself identify zeros of \(\Xi\) with eigenvalues of \(J\).

Therefore the remaining proof-bearing target is an intrinsically theta-derived perturbation determinant, Weyl function, or equivalent Herglotz identity whose zeros are forced onto the real spectral set.

## 8. Exact next target

Find and prove, without using known zeta-zero locations,
\[
\Xi(t)=E(t)\det_F(I-F(t,J)),
\]
where \(E\) is zero-free and the spectral map \(F\) is derived from the completed theta/modular structure. An equivalent target is a theta-derived Weyl function satisfying a rigorously established fixed transform of \(\Xi'/\Xi\), with the Herglotz property proved independently.

## 9. RH status

This frontier closes:
\[
\Phi\to d\nu\to J\to\Xi
\]
through an exact theta-derived self-adjoint Jacobi operator and an exact Xi matrix-element/rank-one determinant identity.

It does **not** close:
\[
J\to\text{spectral determinant}\to\text{all Xi zeros real}.
\]
That final bridge remains the genuine RH wall. No RH proof is claimed.
