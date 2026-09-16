# Frontier 71 — multiplier preimage obstruction

Date: 2026-09-16

## Exact bridge
The canonical coefficients satisfy
\[
\gamma_n=a_nM_n,\qquad a_n=\frac{n!}{(2n)!},
\]
and
\[
\sum_{n\ge0}a_n\frac{x^n}{n!}=\cosh\sqrt{x}.
\]
The zeros are \(-\pi^2(k+1/2)^2\), so \((a_n)\) is a Pólya–Schur multiplier sequence.

Define
\[
B(x)=\sum_{n\ge0}M_n\frac{x^n}{n!}.
\]
Then coefficientwise multiplication gives
\[
T_aB(x)=\sum_{n\ge0}M_n\frac{x^n}{(2n)!}=\Xi(\sqrt{-x}).
\]

## Decisive obstruction
For the standard theta representation,
\[
M_n=\int_0^\infty\Phi(u)u^{2n}\,du,\qquad \Phi\ge0,
\]
so Cauchy–Schwarz gives
\[
M_{n+1}^2\le M_nM_{n+2},
\]
strictly for a nondegenerate kernel. The degree-two Jensen polynomial of \(B\),
\[
M_n+2M_{n+1}X+M_{n+2}X^2,
\]
has discriminant
\[
4(M_{n+1}^2-M_nM_{n+2})<0.
\]
Hence \(B\notin LP_\mathbb R\) already at degree two. Therefore the tempting closure
\[
B\in LP_\mathbb R\Rightarrow T_aB\in LP_\mathbb R
\]
cannot be used.

## Consequence
The multiplier bridge is real and useful, but the missing theorem must be preimage-specific or directly certify \(T_aB=\Xi(\sqrt{-x})\). The surviving global targets are universal canonical Jensen hyperbolicity, a direct LP certificate, consecutive Toeplitz positivity, the self-weighted Hamburger tower, or a genuinely new equivalent theorem.

This is a rigorous route correction, not a proof of RH.