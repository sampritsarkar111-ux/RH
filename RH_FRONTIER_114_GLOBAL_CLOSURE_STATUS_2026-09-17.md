# RH Frontier 114 — Global Closure Status — 2026-09-17

## Scope
This document consolidates the current proof-bearing routes after the exact degree-3 Jensen/Hermite audit.

## What is now exact

1. Completed-theta moment representation:
   gamma_k = M_k/(2k)!, M_k = integral_R u^(2k) Phi(u) du.
2. Jensen polynomials:
   J_{d,n}(X) = sum_{j=0}^d binom(d,j) gamma_{n+j} X^j.
3. Degree 3:
   gamma_{n+3}^4 Delta = 27(3 gamma_n^2 gamma_{n+3}^2 -18 gamma_n gamma_{n+1}gamma_{n+2}gamma_{n+3} -4 gamma_n gamma_{n+2}^3 -4 gamma_{n+1}^3 gamma_{n+3} +3 gamma_{n+1}^2 gamma_{n+2}^2).
4. Every quartic moment product has an exact four-copy integral representation against the positive product theta measure.

## Closed false shortcut

A generic positive measure cannot imply Jensen hyperbolicity. The two-atom positive measure 9/10 delta_1 + 1/10 delta_10 gives a negative degree-3 Jensen discriminant at n=0, exactly
-3988621262088331488000/1000036000486002916006561.
Therefore raw moment positivity, Hankel PSD, or a one-copy Gram representation is insufficient.

## Remaining proof walls

### A. Theta/Jensen
Prove an RH-independent all-degree theorem that factorial-normalized Jensen/Hermite forms are PSD, using a property genuinely special to the completed Riemann theta lattice. The theorem must cover every degree and shift and survive the infinite passage.

### B. Nyman–Beurling
Prove arithmetic cyclicity/coercivity independently. Finite Gram PSD is known but the limiting density statement is the RH-equivalent step.

### C. Li/Weil
Find a genuinely RH-independent positive factorisation of the global explicit-formula quadratic form. Rewriting the criterion is not sufficient.

### D. de Bruijn–Newman
Monotonicity of the de Bruijn–Newman parameter is not enough; an independent endpoint argument is needed to force the RH endpoint condition.

### E. Analytic legality
Every analytic continuation, contour shift, sum/integral interchange, truncation limit, determinant/minor limit, and all-degree passage must be justified.

## Current conclusion

No complete proof of the Riemann Hypothesis has been obtained. This is an exact research-status statement, not a limitation of the finite algebra. The project should not claim RH is proved unless one of A/B/C (or an entirely new independent route) is actually established without circularity.
