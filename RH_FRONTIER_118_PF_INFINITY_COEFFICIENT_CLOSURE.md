# Frontier 118 — PF∞ Coefficient Closure of the Completed Theta Kernel

Date: 2026-09-16

## Objective

Replace the degree-by-degree Hermite/Gram wall by a single infinite total-positivity statement on the Taylor coefficient sequence of the completed Riemann Xi function in the variable z=-t^2.

## 1. Exact coefficient generating function

Let
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\]
with the completed Riemann kernel \(\Phi\) used in Frontiers 109–114. Define
\[
g(z):=\Xi(\sqrt{-z})=\sum_{k\ge0}\gamma_k z^k.
\]
Because \(\Phi\) is even and rapidly decreasing,
\[
\boxed{\gamma_k=\frac{1}{(2k)!}\int_{\mathbb R}u^{2k}\Phi(u)\,du>0.}
\]
No zero location is used.

## 2. Exact PF∞ target

Form the infinite Toeplitz matrix
\[
T_\gamma=(\gamma_{j-i})_{i,j\ge0},
\qquad \gamma_r:=0\quad(r<0).
\]
The sharpened closure target is
\[
\boxed{T_\gamma\ \text{is totally nonnegative of every finite order (PF}_\infty\text{)}.}
\]
Equivalently, every finite Toeplitz minor
\[
\det(\gamma_{j_a-i_b})_{a,b=1}^r\ge0
\]
must hold for every \(r\) and every strictly increasing index sets \(i_1<\cdots<i_r\), \(j_1<\cdots<j_r\).

## 3. Why this closes the root-location mechanism if proved

The generating function \(g\) is entire with nonnegative coefficients. The Edrei/Schoenberg characterization of PF∞ sequences identifies their generating functions with the appropriate Laguerre–Pólya/real-negative-zero class (with the entire case having no denominator/pole factor). Therefore PF∞ of \((\gamma_k)\) forces all zeros of \(g\) to be real and nonpositive.

Since
\[
g(-t^2)=\Xi(t),
\]
a zero \(z_0\le0\) of \(g\) gives \(t=\pm\sqrt{-z_0}\in\mathbb R\). Conversely, under RH the zeros of \(g\) are precisely the nonpositive numbers \(-\gamma_\rho^2\) associated with the real ordinates of the Xi zeros, so the coefficient sequence has the corresponding PF∞ structure.

Thus the all-degree root-location wall can be compressed to one statement:
\[
\boxed{\text{theta structure}\ \Longrightarrow\ T_\gamma\text{ is PF}_\infty.}
\]
This is a substantially sharper target than proving unrelated moment inequalities or one Hermite determinant at a time.

## 4. Relation to Jensen polynomials

PF∞ immediately supplies the required finite-degree real-rootedness mechanism through the finite Toeplitz minors. In particular, the first nontrivial minor is
\[
\gamma_n^2-\gamma_{n-1}\gamma_{n+1}\ge0,
\]
which is the coefficient log-concavity gate underlying the degree-two Jensen condition. Higher Toeplitz minors encode the full variation-diminishing hierarchy instead of only adjacent Turán inequalities.

The key advantage is that the quantifiers are unified: one infinite matrix contains every degree and shift.

## 5. What cannot be claimed

The positive theta measure does **not** imply PF∞. A positive moment representation gives Hankel positivity, whereas PF∞ requires Toeplitz total positivity. Frontiers 108–114 already rule out replacing this distinction by generic positivity or a scalar SOS argument.

Likewise, positivity of finitely many Toeplitz minors or numerical checks cannot establish PF∞.

## 6. Exact theta-specific proof gate

The remaining genuine theorem is therefore:

> Prove directly from the completed Jacobi/Poisson theta lattice that every finite Toeplitz minor of \(\gamma_k\) is nonnegative.

A proof-bearing route must produce an exact identity of the form
\[
\boxed{
\det(\gamma_{j_a-i_b})_{a,b=1}^r
=\sum_\lambda\int_{\Omega_\lambda}
\left|F_{\lambda,r}(u_1,\ldots,u_r)\right|^2\,d\mu_\lambda\ge0,
}
\]
or an equivalent variation-diminishing / strictly totally positive representation, with the full theta lattice retained through Poisson/Jacobi transformation.

Crucially, the measure/weight and the functions \(F_{\lambda,r}\) must be derived from the Riemann theta kernel itself; arbitrary positive-measure arguments are insufficient.

## 7. New structural obstruction

There is no reason for a generic Stieltjes moment sequence to be PF∞. Therefore the proof cannot proceed by showing only that
\[
M_k=\int u^{2k}\Phi(u)\,du
\]
is a Stieltjes moment sequence. The factorial rescaling
\[
\gamma_k=M_k/(2k)!
\]
is essential, and the required theorem must control all Toeplitz minors after this rescaling.

This isolates the genuinely Riemann-specific information that the modular theta structure must supply.

## 8. Status

This frontier does not prove RH. It compresses the previous infinite Hermite/Jensen wall into a single exact all-order total-positivity theorem and identifies the precise object that a successful modular completion must factor: the Toeplitz matrix of the completed Xi coefficients.

The next proof-bearing calculation is to derive the first nontrivial higher Toeplitz minors directly from the unsummed theta lattice and determine whether Poisson/Jacobi pairing supplies a positive Binet–Cauchy/Vandermonde decomposition. Any sign-changing exact minor closes a proposed PF∞ ansatz; an all-order positive factorization would close the RH wall.