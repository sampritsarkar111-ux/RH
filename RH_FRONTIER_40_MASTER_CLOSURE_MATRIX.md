# Frontier 40 — master closure matrix

## Objective

Run the remaining RH proof targets as independent gates. No finite computation, asymptotic statement, numerical zero verification, or conditional implication is promoted to a proof.

## Gate A — Jensen degree 3

Necessary condition from the exact central-moment reduction:
\[
\gamma_{n+2}^2\ge\gamma_{n+1}\gamma_{n+3},
\qquad 4v^3+w^2\le0.
\]
The first inequality is only necessary; the second is the actual stronger cubic gate.

## Gate B — theta Turan mechanism

Frontier 39 gives the exact factorial-corrected double-integral kernel for
\[
T_m=\gamma_{m+1}^2-\gamma_m\gamma_{m+2}.
\]
The raw kernel changes sign, so a pointwise-positive kernel proof is unavailable without additional theta structure.

Required breakthrough: exploit the discrete theta sum, modular transformation, or another exact Riemann-specific identity to prove the integrated sign.

## Gate C — all-degree Jensen

Even if every degree-3 obstruction is proved, RH still requires hyperbolicity of every Jensen polynomial (or an equivalent Laguerre–Pólya criterion), with all shifts and degrees quantified.

Required breakthrough: an unconditional all-degree theorem for the actual Xi coefficients, not for an arbitrary moment sequence.

## Gate D — Toeplitz total positivity

Let
\[
G(z)=\xi\!\left(\frac12+\frac{\sqrt z}{2}\right)=\sum_{k\ge0}a_kz^k,
\qquad D_{r,k}=\det(a_{k+j-i})_{i,j=0}^{r-1}.
\]
An all-order strict sign-regularity theorem for these consecutive minors would provide a direct closure route. Known finite-order and asymptotic regions do not cover the entire (r,k)-plane.

## Gate E — de Bruijn–Newman / heat flow

A heat-flow route must establish a global Lyapunov/monotonicity statement strong enough to force the relevant de Bruijn–Newman parameter to the RH threshold, without assuming RH in the sign argument.

The previously considered raw-kernel PF-infinity route is not accepted after the recorded finite-order obstruction.

## Gate F — final logic audit

Any claimed proof must explicitly establish:
1. the analytic continuation and normalization used;
2. the exact equivalence from the constructed property to all nontrivial zeros lying on Re(s)=1/2;
3. convergence/interchange conditions for every infinite sum/integral/determinant limit;
4. strict versus non-strict inequalities where required;
5. absence of hidden RH assumptions;
6. coverage of every parameter range, not only a finite verified region.

## Current conclusion

The project has a substantially sharper map of the remaining proof obligations, including an exact new obstruction to the naive theta-kernel positivity strategy. No complete proof of RH has been obtained.
