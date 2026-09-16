# Frontier 113 — d=3 modular Gram verdict

Date: 2026-09-16

## Question

Does the completed Riemann theta lattice transform the exact d=3 four-copy kernel into a positive Gram object by the direct route proposed in Frontier 112?

## Exact invariant

The degree-3 Hermite determinant satisfies
\[
\det H_3=-\frac{27}{\gamma_3^4}\left(\gamma_0^2\gamma_3^2-6\gamma_0\gamma_1\gamma_2\gamma_3+4\gamma_0\gamma_2^3+4\gamma_1^3\gamma_3-3\gamma_1^2\gamma_2^2\right),
\]
and with \(\gamma_k=M_k/(2k)!\),
\[
E_3=\frac1{518400}\left(M_0^2M_3^2-90M_0M_1M_2M_3+150M_0M_2^3+360M_1^3M_3-675M_1^2M_2^2\right).
\]
The four-copy identity is
\[
518400E_3=\int_{\mathbb R^4}\mathcal Q_3(u_1^2,u_2^2,u_3^2,u_4^2)\prod_{j=1}^4\Phi(u_j)\,du_j.
\]

## Direct positivity obstruction

The completed theta kernel \(\Phi(u)\) is positive, but \(\mathcal Q_3\) is not pointwise nonnegative. More strongly, the actual Riemann theta moments give a negative value of the four-copy integral.

High-precision numerical evaluation of the defining theta series/integrals gives approximately
\[
M_0=0.24856038909415705496,
\]
\[
M_1=0.01148597215757271877,
\]
\[
M_2=0.00148142421684381608,
\]
\[
M_3=0.000299647973298789746.
\]
Substitution gives
\[
Q:=M_0^2M_3^2-90M_0M_1M_2M_3+150M_0M_2^3+360M_1^3M_3-675M_1^2M_2^2
\approx-1.92671056245139\times10^{-8},
\]
and therefore
\[
E_3\approx-3.71664846151889\times10^{-14}<0.
\]
Consequently the exact four-copy \(\mathcal Q_3\)-integral is negative for the actual completed theta measure. Hence the direct ansatz
\[
\int \mathcal Q_3\,d\mu^{\otimes4}=\sum_\alpha\int |P_\alpha|^2\,d\lambda_\alpha
\]
is impossible.

## Important sign interpretation

This does NOT contradict the required Hermite determinant positivity. Because
\[
\det H_3=-\frac{27}{\gamma_3^4}\,E_3,
\]
the observed \(E_3<0\) corresponds to \(\det H_3>0\) (assuming \(\gamma_3\ne0\)). Thus a viable Gram mechanism, if one exists, must represent the determinant-oriented quantity \(-E_3\), not \(E_3\) itself.

## What modular completion can and cannot do

Jacobi/Poisson completion is an exact change of representation; it cannot change the value of the scalar four-copy invariant. Therefore no modular transform can turn this particular scalar integral into a positive sum of squares without simultaneously introducing an overall sign reversal or additional terms whose combined value equals the same negative scalar.

The direct positive-remainder target
\[
\int \mathcal Q_3\prod\Phi
=\sum|P|^2+\mathcal R_{\rm mod},\qquad \mathcal R_{\rm mod}\ge0,
\]
is therefore ruled out for the actual theta kernel because its left side is negative.

The correct next target is instead an exact representation of
\[
-518400E_3=\sum_\alpha\int|P_\alpha|^2d\lambda_\alpha+\mathcal R_{\rm mod},
\qquad \mathcal R_{\rm mod}\ge0,
\]
or, preferably, a direct all-degree hyperbolicity-preserving operator whose d=3 specialization yields this sign.

## Rigor status

The sign conclusion above is a high-precision numerical diagnostic, not an exact proof of the numerical inequality. An unconditional proof still requires an analytic sign certificate for the actual theta moments or an exact transformed identity. The algebraic impossibility of a positive-SOS representation of \(E_3\) follows immediately if the exact sign \(E_3<0\) is established.

## Next proof-bearing gate

1. Transform the determinant-oriented quantity \(-E_3\), not \(E_3\).
2. Keep all four lattice indices through Jacobi/Poisson completion.
3. Derive an exact Binet–Cauchy/Gram identity for \(-E_3\), or identify its exact residual.
4. Generalize the mechanism from d=3 to arbitrary degree d; d=3 alone is not RH.

**Status: direct positive Gram ansatz for \(E_3\) is blocked; determinant-oriented sign-corrected Gram route remains OPEN. No RH proof claimed.**
