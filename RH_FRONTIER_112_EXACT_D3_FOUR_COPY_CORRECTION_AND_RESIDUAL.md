# Frontier 112 — exact d=3 four-copy kernel: correction, factorisation test, and modular-residual wall

Date: 2026-09-16

## Critical algebra correction

Recomputing directly from Newton identities gives
\[
\det H_3=-\frac{27}{\gamma_3^4}\left(\gamma_0^2\gamma_3^2-6\gamma_0\gamma_1\gamma_2\gamma_3+4\gamma_0\gamma_2^3+4\gamma_1^3\gamma_3-3\gamma_1^2\gamma_2^2\right).
\]
With \(\gamma_k=M_k/(2k)!\), the bracket is
\[
\boxed{E_3=\frac1{518400}\left(M_0^2M_3^2-90M_0M_1M_2M_3+150M_0M_2^3+360M_1^3M_3-675M_1^2M_2^2\right).}
\]
This corrects the earlier erroneous numerical coefficients.

## Exact four-copy kernel

Let \(Y=u^2\), \(\mu(du)=\Phi(u)du\). Define the symmetrized four-copy polynomial
\[
\mathcal Q_3(Y_1,Y_2,Y_3,Y_4)=\frac1{24}\sum_{\sigma\in S_4}\left[
Y_{\sigma(1)}^3Y_{\sigma(2)}^3-90Y_{\sigma(1)}^0Y_{\sigma(2)}^1Y_{\sigma(3)}^2Y_{\sigma(4)}^3+150Y_{\sigma(1)}^0Y_{\sigma(2)}^2Y_{\sigma(3)}^2Y_{\sigma(4)}^2
+360Y_{\sigma(1)}Y_{\sigma(2)}Y_{\sigma(3)}Y_{\sigma(4)}^3-675Y_{\sigma(1)}Y_{\sigma(2)}Y_{\sigma(3)}^2Y_{\sigma(4)}^2\right].
\]
Then exactly
\[
\boxed{518400E_3=\int_{\mathbb R^4}\mathcal Q_3(u_1^2,u_2^2,u_3^2,u_4^2)\prod_{j=1}^4\Phi(u_j)\,du_j.}
\]
No zero locations enter this identity.

## Exact obstruction to generic positive-measure SOS

Positivity of \(\Phi\) alone cannot imply the required sign. For the positive probability measure on \(Y\in\{1,100\}\) with weights \(9/10,1/10\),
\[
M_0=1,\quad M_1=109/10,\quad M_2=10009/10,\quad M_3=1000009/10,
\]
and the numerator
\[
Q=M_3^2-90M_1M_2M_3+150M_2^3+360M_1^3M_3-675M_1^2M_2^2
\]
satisfies
\[
\boxed{Q=56993330791157/2000>0.}
\]
Thus a generic theorem saying every positive even measure gives the required d=3 Hermite positivity is false.

## Riemann-specific modular target

The remaining possibility must use the completed theta kernel beyond mere positivity. Retain the complete lattice sum and its Poisson/Jacobi transformation before any termwise reflection. The desired identity has the schematic exact form
\[
\boxed{\int_{\mathbb R^4}\mathcal Q_3\prod_j\Phi(u_j)du_j
=\sum_\alpha\int|P_\alpha|^2d\lambda_\alpha+\mathcal R_{\rm mod},}
\]
followed by a proof that the transformed remainder \(\mathcal R_{\rm mod}\ge0\).

No such positive remainder has yet been derived. Modular symmetry by itself is not a positivity theorem.

## Degree/structure constraint

\(\mathcal Q_3\) has total degree six in the \(Y_j\), while a bare four-variable Vandermonde square \(\prod_{i<j}(Y_i-Y_j)^2\) has degree twelve. Therefore a direct bare Vandermonde-square polynomial identity is impossible; any Vandermonde mechanism must arise after a nontrivial transform, scaling kernel, or integral identity.

## Next proof-bearing gate

1. Substitute the full theta lattice formula for every \(\Phi(u_j)\).
2. Retain all four lattice indices.
3. Perform Poisson/Jacobi transformation on the completed expression, never termwise.
4. Expand the transformed d=3 expression exactly.
5. Search for a square decomposition and isolate the exact residual.
6. Either prove the residual is nonnegative or record an exact negative component as a rigorous obstruction.

**Status: OPEN. The exact d=3 four-copy kernel is derived; generic positive-measure SOS is ruled out; the genuinely Riemann-specific modular positive remainder remains unproved.**
