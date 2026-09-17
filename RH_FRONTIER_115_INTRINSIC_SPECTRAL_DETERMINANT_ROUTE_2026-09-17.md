# RH Frontier 115 — Intrinsic Spectral Determinant Route — 2026-09-17

## Objective
Construct a proof architecture that does not begin by trying to prove positivity of arbitrary moment sequences. Instead, extract a spectral object directly from the completed theta kernel whose real-rootedness would force RH.

## Proposed transform
Let
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\qquad \Phi(u)=\Phi(-u).
\]
Define the cosine-transform operator on a suitable even test-function space by
\[
(Tf)(x)=\int_{\mathbb R}\Phi(u)f(u)\cos(xu)\,du.
\]
The target is not to assert that T is positive merely because Phi is positive. Instead seek an exact self-adjoint realization H such that
\[
\Xi(t)=C\,\det_{\!F}(I-t^2H^{-1})
\]
(or an equivalent canonical-product identity), with the nontrivial zeros encoded as spectral parameters.

## Necessary closure conditions
1. Construct H explicitly from the theta/modular data, with a precise Hilbert space and domain.
2. Prove H is self-adjoint (or establish the exact operator class needed).
3. Prove the Fredholm/canonical-product identity without assuming RH.
4. Show every spectral parameter is real.
5. Prove that the real spectrum corresponds exactly to zeros of Xi on the real t-axis.
6. Control multiplicities and the possible zero at the origin.
7. Establish convergence of the determinant/product and all limiting operations.

## Key non-circularity test
A proof of positivity of a kernel that is obtained by inserting the desired zero locations, or by assuming the spectral parameters are real, is circular and must be rejected.

## Immediate algebraic target
For finite-rank truncations H_N, derive characteristic polynomials directly from the theta lattice and test whether their coefficients satisfy an exact interlacing/Sturm recurrence. A recurrence with parameter-independent positive Jacobi coefficients would provide a concrete route to a real spectrum. Numerical evidence alone is not a proof.

## Status
This is a proposed new route, not a theorem. No RH conclusion follows until conditions 1–7 are proved.
