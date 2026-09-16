# Frontier 90 — Degree-two modular-pairing test

Date: 2026-09-16

## Goal

Test the most economical possible modular-pairing mechanism on the exact degree-two Jensen inequality before attempting an all-degree Hermite construction.

Let
\[
\gamma_k=c_kI_k,\qquad c_k=\frac{2k+1}{k!},
\qquad I_k=\int y^k\,d\mu(y).
\]
Then
\[
\Delta_{2,n}=c_{n+1}^2I_{n+1}^2-c_nc_{n+2}I_nI_{n+2}.
\]

## Exact two-point kernel

With independent \(y_1,y_2\),
\[
\Delta_{2,n}=\iint (y_1y_2)^nK_n(y_1,y_2)\,d\mu(y_1)d\mu(y_2),
\]
where
\[
K_n(y_1,y_2)=c_{n+1}^2y_1y_2-\frac{c_nc_{n+2}}2(y_1^2+y_2^2).
\]
The kernel is homogeneous of degree two. Writing \(r=y_1/y_2\),
\[
K_n=y_2^2\left(c_{n+1}^2r-\frac{c_nc_{n+2}}2(r^2+1)\right).
\]
Since \(c_{n+1}^2>c_nc_{n+2}\), there is a bounded interval of ratios around \(r=1\) where the kernel is positive, but \(K_n<0\) for sufficiently large or small ratios.

## Modular pairing requirement

A modular involution would have to transform the negative-ratio regions into positive contributions with a compensating Jacobian/weight. A sufficient identity would have the schematic form
\[
W(y_1,y_2)K_n(y_1,y_2)+W(Ty_1,Ty_2)K_n(Ty_1,Ty_2)=Q_n(y_1,y_2)^2,
\]
with \(W\ge0\) and the transformed measure invariant under \(T\).

No such identity has been established here. Importantly, the sign change of \(K_n\) means modular symmetry cannot be replaced by a purely local square completion.

## Consequence

The degree-two problem is reduced to an explicit search for a measure-specific involutive pairing, not an arbitrary positive-kernel argument. Any successful pairing must use the exact theta modular relation and must preserve the full \(n\)-dependent factorial correction.

## Status

**No-go test passed; no pairing identity found.** This is a sharper target, not an RH proof.
