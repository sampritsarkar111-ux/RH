# RH Frontier 162 — Parallel Closure Execution — 2026-09-17

## Objective
Run the remaining proof-bearing routes in parallel. A route is closed only by an unconditional theorem whose hypotheses do not encode RH.

## Current verified state
The research ledger reports that the following remain open: global Pick/Weyl positivity; the nonlinear theta-to-tau Hankel bridge; an unconditional theta-defined de Branges/canonical system with exact Xi determinant; a RH-independent Li/Weil positive factorization; and the de Bruijn-Newman endpoint. Low-order factorial Hankel determinants are positive numerically, but this is diagnostic only.

## Parallel Route A — Exact theta → Pick/Stieltjes
Target: construct an analytic function F from the exact theta representation such that

    F(z) = a + bz + integral_0^infinity ((1/(u-z)) - u/(1+u^2)) dmu(u),

with a real, b >= 0, and a positive measure mu, together with all convergence and boundary-value conditions. Equivalent target: prove the Pick inequality Im F(z) >= 0 for Im z > 0 without using zero locations.

Hard gate: theta modularity alone is not sufficient; the nonlinear logarithmic derivative must inherit positivity by an explicit identity.

## Parallel Route B — tau-Hankel / cumulant → Gram
For coefficients c_n of the relevant logarithmic derivative, define the factorially normalized Hankel matrix

    K_N = [(-1)^(i+j)c_(i+j)/(i+j)!]_(0<=i,j<=N).

A successful proof must show K_N >= 0 for every N by an exact theta-generated Gram/SOS representation, not finite numerical testing. Current diagnostic values recorded in the ledger give positive determinants for N=1,2,3.

Hard gate: prove the nonlinear cumulant transform from theta moments to c_n preserves the required positivity for the Riemann-specific sequence.

## Parallel Route C — de Branges / canonical system
Construct a theta-defined E(z) or canonical system with an unconditional Hermite-Biehler inequality and an exact characteristic determinant for Xi. The decisive chain is:

    self-adjoint canonical system/operator
      -> real spectral parameters
      -> Xi zeros represented by those parameters
      -> Re(rho)=1/2.

The construction must not define the operator using the unknown zero locations in a circular way.

## Parallel Route D — Li/Weil
Seek an identity for the Weil quadratic form of the form

    Q(phi) = ||T phi||^2 + R(phi),

where R is explicitly nonnegative and the derivation is unconditional. The strongest closure is Q(phi)>=0 for every admissible test function, which by the Li/Weil criterion implies RH.

Hard gate: positivity must arise from the theta/arithmetic data itself, not from assuming all zeros lie on the line.

## Parallel Route E — de Bruijn-Newman
Work with the deformed Xi family and seek a direct endpoint inequality forcing the required endpoint parameter. Merely rewriting RH as an endpoint statement is not enough. The proof must establish the endpoint property from unconditional theta estimates.

## Parallel Route F — Jensen/Laguerre-Pólya / total positivity
Try to prove that the relevant theta-derived entire function belongs to the Laguerre-Pólya class, equivalently obtain compatible Jensen-polynomial positivity or an exact PF-infinity/total-positivity mechanism strong enough to imply only real zeros.

Hard gate: generic theta-kernel positivity or finite Jensen positivity is insufficient; the infinite-order theorem must be proved.

## Parallel Route G — Nyman-Beurling / model-space cross-check
Use the exact NB/BD equivalence as an independent closure route. Any claimed cyclicity, atom-freeness, or projection estimate must be proved without encoding the zero set or RH in the model construction.

## Cross-route theorem target
The most valuable breakthrough is a single theta-generated positive-resolvent identity that simultaneously implies:

    Pick/Stieltjes positivity
        => all-order Hankel positivity
        => Li/Weil positivity
        => a de Branges/spectral realization.

This is a target, not an established theorem.

## Anti-circularity checklist
1. No zero locations may be assumed in defining a measure, operator, inner function, or positivity cone.
2. Every infinite sum/integral interchange must have a stated domination/convergence argument.
3. Every positivity claim must hold at all orders, not just numerically tested orders.
4. Exact determinant/spectral identities must be proved, not inferred from matching zeros.
5. A computational match is evidence only and cannot close RH.

## Status
No route is closed by this execution record. The purpose of Frontier 162 is to make the next calculations explicit and parallel while preserving a strict proof standard.
