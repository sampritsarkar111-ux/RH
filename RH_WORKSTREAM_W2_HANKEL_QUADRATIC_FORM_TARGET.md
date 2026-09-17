# W2 — Unconditional Hankel Quadratic-Form Target

## Objective

Prove, without assuming RH,
\[
Q_N(c):=\sum_{i,j=0}^{N}c_ic_j\tau_{i+j}\ge0
\quad\forall N\ge0,\ c\in\mathbb R^{N+1}.
\]

## Required zero-free starting point

Use only the completed Xi/theta representation and exact coefficient identities. In particular, do not replace Q_N by a sum of positive terms indexed by zeros, because that would assume the desired sign of the transformed zero nodes.

## Preferred certificate

Find an exact representation
\[
Q_N(c)=\sum_\alpha\int_{\Omega_\alpha}
\left|P_{N,c,\alpha}(u_1,\ldots,u_q)\right|^2
\,d\mu_\alpha(u_1,\ldots,u_q),
\]
with positive measures determined explicitly by the completed theta lattice.

## First finite gate

Compute the exact N=1,2,3 quadratic forms from the Xi/theta coefficients and attempt to identify a common kernel pattern. Then attack arbitrary N by polarization and Binet–Cauchy/Vandermonde identities.

## Failure certificate

If a proposed one-copy representation fails, record the exact signed residual rather than discarding it. A failure at degree 3 should identify the precise obstruction that a multi-copy or modular-reflection term must remove.

## Completion criterion

A theorem for all N, with every interchange and limiting operation justified and with no hidden use of RH, closes the central gate in the master program.