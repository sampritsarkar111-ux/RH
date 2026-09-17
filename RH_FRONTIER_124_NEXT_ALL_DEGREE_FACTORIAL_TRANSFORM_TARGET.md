# Frontier 124 — Next all-degree target: factorial-transform stability

Date: 2026-09-17

## Goal

The corrected degree-3 analysis shows that the proof-bearing object is not the positive theta moment sequence by itself, but its factorially transformed coefficient sequence
\[
\gamma_k=\frac{M_k}{(2k)!}.
\]

Define
\[
\mathcal T_n(m_j):=\frac{(2n)!}{(2n+2j)!}m_j,
\qquad
m_j=\frac{M_{n+j}}{M_n}.
\]
Then \(\mathcal T_n(m_j)=\gamma_{n+j}/\gamma_n\).

## Degree-3 exact target

With
\[
P_n=\frac{\mathcal T_n(m_2)}{\mathcal T_n(m_1)^2},
\qquad
Q_n=\frac{\mathcal T_n(m_3)}{\mathcal T_n(m_1)^3},
\]
the cubic Jensen polynomial is hyperbolic exactly when
\[
P_n\le1,
\qquad
|Q_n-(3P_n-2)|\le2(1-P_n)^{3/2}.
\]

## New conjectural mechanism to test

Seek an integral/operator representation of the factorial transform itself that preserves hyperbolicity, rather than attempting to prove ordinary moment total positivity. The basic kernel is
\[
K_n(y,j)=\frac{y^j}{(2n+2j)!}.
\]
The exact all-degree problem is to establish that applying this kernel to the Riemann-theta moment functional produces a multiplier sequence / PF∞ sequence / stability-preserving Jensen family.

This is the next proof gate because the earlier ordinary Stieltjes/Vandermonde route is algebraically obstructed.

## Required falsification tests

1. Test the degree-3 FSR for every accessible n using independently evaluated Xi coefficients.
2. Search for a finite positive integral representation of 1/(2n+2j)! compatible with the theta measure.
3. Determine whether the resulting composition is a known or new stability-preserving transform.
4. For d=4, compute the first nontrivial principal discriminant/resultant in the scale-free coordinates R_2,R_3,R_4.
5. Attempt a degree-uniform closure theorem; reject any argument that uses zeros of Xi or assumes RH.

## Status

This is a rigorous reformulation and research target, not a proof of RH. The remaining theorem is the unconditional all-degree factorial-transform stability statement for the Riemann Xi coefficients.
