# Frontier 119 — First PF∞ Minors and Exact Closure Gate

Date: 2026-09-16

## Purpose

Test the new PF∞ formulation at the first nontrivial levels without confusing numerical positivity with proof.

For
\[
g(z)=\sum_{k\ge0}\gamma_k z^k,
\qquad \gamma_k=\frac{M_k}{(2k)!},
\]
with \(M_k=\int u^{2k}\Phi(u)du\), the PF∞ Toeplitz matrix is
\[
T_\gamma=(\gamma_{j-i})_{i,j\ge0},\qquad \gamma_r=0\;(r<0).
\]

## 1. First minors

The order-one minors are \(\gamma_k>0\).

The order-two adjacent minors are
\[
\boxed{\Delta_{2,k}=\gamma_k^2-\gamma_{k-1}\gamma_{k+1}.}
\]
Substitution gives
\[
\Delta_{2,k}=
\frac{M_k^2}{(2k)!^2}-
\frac{M_{k-1}M_{k+1}}{(2k-2)!(2k+2)!}.
\]
This is exactly the factorial-corrected Turán gate. A generic positive moment measure only gives the reverse-direction log-convex inequality \(M_k^2\le M_{k-1}M_{k+1}\), so the factorial correction is essential.

Thus even PF2 is not a consequence of moment positivity alone.

## 2. Order-three adjacent Toeplitz minor

The first genuinely higher-order adjacent Toeplitz minor is
\[
\boxed{
\Delta_{3,k}=
\det\begin{pmatrix}
\gamma_k&\gamma_{k+1}&\gamma_{k+2}\\
\gamma_{k-1}&\gamma_k&\gamma_{k+1}\\
\gamma_{k-2}&\gamma_{k-1}&\gamma_k
\end{pmatrix}.
}
\]
After substituting the factorial-corrected moments, this becomes a homogeneous cubic expression in \(M_{k-2},\ldots,M_{k+2}\). Its sign cannot be inferred from Hankel positivity alone.

The exact proof target is therefore not merely \(\Delta_{3,k}\ge0\), but an all-order representation of every Toeplitz minor by the completed theta lattice.

## 3. Why this is a stronger closure mechanism

If every finite Toeplitz minor is nonnegative, the coefficient sequence is PF∞. The corresponding entire generating function belongs to the real-negative-zero/Laguerre–Pólya mechanism, subject to the precise hypotheses of the total-positivity characterization. Consequently the zeros of \(g\) are real and nonpositive, which maps under \(g(-t^2)=\Xi(t)\) to real ordinates of the completed Xi zeros.

No individual zero is introduced into the proof.

## 4. Exact remaining theorem

The decisive theorem remains:
\[
\boxed{
\text{Completed Riemann theta lattice}
\Longrightarrow
\det(\gamma_{j_a-i_b})\ge0
\quad\text{for every finite minor.}
}
\]

A successful proof must preserve the theta lattice under Poisson/Jacobi transformation and expose a variation-diminishing or Binet–Cauchy/Vandermonde structure. Generic positive measures, finite numerical tests, and degree-by-degree discriminants are insufficient.

## 5. Anti-circularity

The proof must never parameterize zeros as \(-t^2\) with real \(t\) before establishing real-rootedness of \(g\). The transformation \(g(-t^2)=\Xi(t)\) is an identity in the variable, not an assumption about zero locations.

## Status

Open proof gate. This frontier sharply identifies the next exact calculation: derive \(\Delta_{3,k}\) and its theta-lattice Binet–Cauchy transform symbolically, then determine whether its sign is forced by the modular structure.