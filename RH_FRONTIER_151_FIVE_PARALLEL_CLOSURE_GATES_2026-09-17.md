# RH Frontier 151 — Five Parallel Closure Gates — 2026-09-17

## Purpose
Attack the five surviving closure routes independently. A route is closed only by an unconditional proof-bearing identity. Numerical evidence is diagnostic, not proof.

## Gate A — Pick/Weyl
The previous Stieltjes orientation needs correction. For `H(z)=Xi(sqrt(z))`, critical-line zeros correspond to positive real `z`, so the useful Herglotz/Stieltjes orientation for the logarithmic derivative is of the form

`-H'(z)/H(z) = c + integral_[0,infinity] dnu(t)/(t-z)`

with the appropriate regularization. The missing theorem is an RH-independent construction of `nu` from theta data. Frontier 143 already gives the exact Pick numerator and proves that its pointwise kernel changes sign. The next proof gate is an exact global Gram/square decomposition after Poisson/Jacobi transformation.

## Gate B — tau-Hankel
Raw theta Hankel positivity does not automatically imply positivity of the nonlinear cumulants entering tau. The proof-bearing object is an all-order Bell-polynomial/cumulant transfer theorem: theta moments -> tau moments -> Hankel minors, with every sign derived without zero-location assumptions. An exact finite-order negative minor would falsify that transformation class.

## Gate C — Modified total positivity
The fixed translation-kernel class has already encountered the PF5/Wronskian obstruction. The surviving class must be genuinely non-translation-invariant, e.g. modular or scale-dependent. For every order, derive minors directly from the theta lattice and seek a Vandermonde-square or equivalent positive decomposition. Finite numerical checks cannot close the route.

## Gate D — Modified de Branges
Construct explicit theta-derived `E_*=A_*-iB_*` and prove the Hermite-Biehler inequality

`|E_*(z)|^2-|E_*#(z)|^2 > 0` for `Im z > 0`.

The difference must reduce to an RH-independent nonnegative theta identity. No real-zero assumption may enter.

## Gate E — Li/Weil + de Bruijn-Newman
Derive a zero-location-free positive representation of the Weil/Li quadratic form from theta/modular data. The required theorem has the form `Q(g)=Q_theta(g)>=0` for every admissible test function, followed by a separate rigorous equivalence from this positivity criterion to the required zero-location statement.

## Cross-route rule
A successful route may be used as an independent cross-check, but no route may import RH, the critical-line zero parametrization, or a conclusion from another route as an assumption.

## Current status
No complete RH proof has been obtained. The exact Pick numerator and several finite-order/no-go results are established, while the five global closure gates remain open. The next work must produce either a genuine proof-bearing identity or an exact obstruction for each gate.
