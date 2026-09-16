# Frontier 107 — zero-location-free tail target

Date: 2026-09-16

## Goal

Repair the exact gap isolated in Frontier 106 without assuming RH. The Desnanot–Jacobi route needs positivity of all Toeplitz minors
\[
D_r(n)=\det[\gamma_{n+i-j}]_{0\le i,j<r}.
\]
The dangerous step is the dominant-pole expansion based on \(z_m=-t_m^2\), which is only unconditional for the finitely many zeros independently verified to lie on the critical line.

## Required replacement theorem

Let \(g(z)=\Xi(\sqrt z)=\sum_{k\ge0}\gamma_k z^k\). A genuinely unconditional tail lemma would have to use the actual zero set \(\{z_m\}\) of \(g\), with no assumption \(z_m<0\). One possible target is:

\[
\boxed{\exists\,\delta<1,\ C_{r,n}>0:\quad
\left|\frac{D_r(n+1)D_r(n-1)}{D_r(n)^2}-1\right|\le C_{r,n}\delta^{\,n}}
\]
with a sign-preserving determinant identity that does not require the phases of the \(z_m\) to be real.

A second, stronger target is a direct complex-zero-free lower bound on the relevant Binet–Cauchy sum after grouping conjugate zero pairs. The grouped terms must be shown positive by an exact Hermitian/Vandermonde-square identity.

## Why this could actually close the gap

If the tail positivity were proved from the actual complex zero set, the finite certified region plus the Desnanot–Jacobi propagation would no longer import the conclusion that the zeros are real. Combined with positivity of every \(D_r(n)\), the Pólya–Schur/Jensen criterion would then yield \(\Xi\in\mathrm{LP}\) and RH.

## Non-negotiable test

Any proof that replaces \(z_m\) by \(-t_m^2\) for all \(m\), orders all zeros by real ordinates, or uses \(t_{n+1}/t_n\) for arbitrary n before proving those zeros are on the critical line is circular and must be rejected.

## Status

This is the concrete remaining mathematical wall after the 2026 preprint audit. No proof of the zero-location-free tail lemma has yet been found.
