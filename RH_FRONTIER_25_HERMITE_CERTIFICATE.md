# Frontier 25 — Exact Hermite Certificate for Jensen Hyperbolicity

## Claim established

For a real polynomial

\[
p(x)=x^d+b_1x^{d-1}+\cdots+b_d,
\]
let \(s_k=\sum_{r=1}^d\rho_r^k\) be its Newton power sums (with multiplicity), and form the Hermite matrix

\[
\mathcal H(p)=\bigl[s_{i+j}\bigr]_{i,j=0}^{d-1}.
\]

The classical Hermite criterion gives:

\[
\boxed{\quad p\text{ has only real zeros }\Longleftrightarrow \mathcal H(p)\succeq0.\quad}
\]

For the stricter certificate \(\mathcal H(p)\succ0\), all zeros are real and simple.

This turns Jensen-polynomial hyperbolicity into an exact algebraic positivity problem. It does **not** by itself prove RH; the new research target is to prove these matrix inequalities uniformly for the Riemann Jensen family.

## Application to Jensen polynomials

For

\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j,
\]
let \(L_{d,n}\) be its leading coefficient and define the monic polynomial

\[
p_{d,n}(x)=L_{d,n}^{-1}J_{d,n}(x).
\]

Then the RH-equivalent Jensen route can be attacked through

\[
\boxed{\mathcal H_{d,n}:=\mathcal H(p_{d,n})\succeq0\quad\forall d,n.}
\]

A proof of these inequalities for every \(d,n\), together with the established Jensen-Pólya equivalence, would close this route. Finite checks remain only diagnostics.

## Exact degree-4 certificate

Write

\[
p(x)=x^4+b_3x^3+b_2x^2+b_1x+b_0.
\]

The first Newton sums are

\[
\begin{aligned}
s_0&=4,\\
s_1&=-b_3,\\
s_2&=b_3^2-2b_2,\\
s_3&=-b_3^3+3b_3b_2-3b_1,\\
s_4&=b_3^4-4b_3^2b_2+2b_2^2+4b_3b_1-4b_0,
\end{aligned}
\]
with \(s_k+b_3s_{k-1}+b_2s_{k-2}+b_1s_{k-3}+b_0s_{k-4}=0\) for \(k>4\).

The leading principal Hermite determinants are exactly

\[
\Delta_1=4,
\]

\[
\boxed{\Delta_2=3b_3^2-8b_2},
\]

\[
\boxed{\Delta_3=2(16b_0b_2-6b_0b_3^2-18b_1^2+14b_1b_2b_3-3b_1b_3^3-4b_2^3+b_2^2b_3^2)},
\]

and

\[
\boxed{
\begin{aligned}
\Delta_4={}&256b_0^3-192b_0^2b_1b_3-128b_0^2b_2^2+144b_0^2b_2b_3^2-27b_0^2b_3^4\\
&+144b_0b_1^2b_2-6b_0b_1^2b_3^2-80b_0b_1b_2^2b_3+18b_0b_1b_2b_3^3\\
&+16b_0b_2^4-4b_0b_2^3b_3^2-27b_1^4+18b_1^3b_2b_3-4b_1^3b_3^3\\
&-4b_1^2b_2^3+b_1^2b_2^2b_3^2.
\end{aligned}}
\]

Thus a strict degree-4 certificate is

\[
\Delta_1>0,\quad\Delta_2>0,\quad\Delta_3>0,\quad\Delta_4>0.
\]

This is sufficient for \(\mathcal H(p)\succ0\), hence for four distinct real roots.

## Why this is a useful structural reduction

The previous program treated certified roots as the main object. The Hermite formulation removes root-finding from the universal theorem: the problem becomes proving positivity of explicit polynomial/rational expressions in the Jensen coefficients.

The next bottleneck is therefore sharply stated:

\[
\boxed{
\text{theta/arithmetic structure of }\gamma(n)
\ \Longrightarrow\ 
\mathcal H_{d,n}\succeq0\text{ for every }d,n.
}
\]

For degree 2 this recovers the exact Turán condition. For higher degree it packages all root interactions into a single positive-semidefinite matrix.

## Anti-circularity

No zero-location information about \(\zeta\) is used in deriving the Hermite certificate. The remaining implication must be proved from the explicit coefficient/theta representation itself.

## Status

**Genuine rigorous reduction, not an RH proof.** The mathematical novelty target is now a uniform PSD theorem for the Jensen-Hermite matrices, preferably via an explicit Gram/integral factorization coming from the Riemann theta kernel.
