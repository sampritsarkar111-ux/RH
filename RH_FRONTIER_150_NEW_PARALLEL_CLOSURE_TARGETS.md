# Frontier 150 — Post-PF5 Parallel Closure Targets

Date: 2026-09-17

Frontier 149 removes the fixed translation-kernel PF∞ route. The next parallel attacks are therefore:

## A. Global Pick/Weyl

Start from the exact symmetric numerator
\[
P(z)=\iint \Phi(u)\Phi(v)K_{a,b}(u,v)\,du\,dv,
\]
with
\[
K_{a,b}(u,v)=\frac{a\cos(a(u-v))\sinh(b(u+v))-b\sin(a(u+v))\cosh(b(u-v))}{2(a^2+b^2)}.
\]
Perform Poisson/Jacobi transformation before collapsing the theta lattice. Seek either an exact square-modulus identity or a positive Weyl measure for \(F=H'/H\). If a residual survives, classify its sign exactly.

## B. Nonlinear tau transfer

Treat
\[
\tau_n=-\frac1{n!}\left.\frac{d^n}{dz^n}\frac{H'}H\right|_{z=0}
\]
as a nonlinear cumulant transform. Do not identify it with raw theta moments. Seek an Riemann-specific transform theorem, e.g. a continued-fraction/Stieltjes representation of \(-H'/H\), directly from theta data.

## C. Modified total positivity

The fixed kernel \(\Phi(x-y)\) is not PF5. Search instead for a factorial/cosine-adapted kernel \(K_d(u,v)\), or a modular reflection kernel, whose all-order minors encode the Hermite/Jensen determinants. The positivity object must include the factorial normalization responsible for Jensen hyperbolicity.

## D. Direct growth / de Branges replacement

The naive canonical theta-defined Hermite–Biehler function is obstructed numerically. Search for a modified theta completion \(E_*(z)=A(z)-iB(z)\) with an explicit phase/prefactor for which the HB inequality can be derived from modular symmetry without zero data.

## E. Arithmetic routes

Maintain the Nyman–Beurling/Li/Weil branches as independent controls. Any new positivity identity must avoid cyclicity/completeness statements already known to be equivalent to RH.

## Global rule

No finite numerical positivity, no zero-built operator, and no theorem whose hypothesis is equivalent to RH may be promoted to a proof. A successful closure must be an unconditional identity with convergence, positivity, and the final zero-correspondence theorem proved separately.
