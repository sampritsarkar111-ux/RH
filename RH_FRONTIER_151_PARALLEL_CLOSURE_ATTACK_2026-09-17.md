# RH Frontier 151 — Parallel Closure Attack — 2026-09-17

## Status
The Riemann Hypothesis is not proved by this frontier. The purpose is to close proof-bearing gaps, not to relabel reductions as a proof.

## Master acceptance gate
A route closes only if it yields an unconditional theorem implying that every nontrivial zero of the completed Xi-function is real. No critical-line zero parametrization, zero-defined operator, finite-order computation, asymptotic-only statement, or RH-equivalent reformulation is accepted as closure.

## A — Pick/Weyl global sign
Starting from the exact theta double-integral representation for the Pick numerator, retain all lattice indices, apply Poisson/Jacobi to the complete paired block, and compute the exact orbit numerator. Test three factorization classes:

1. modulus-square/SOS;
2. Vandermonde-square/Binet-Cauchy;
3. positive resolvent/Stieltjes representation.

For a truncation N, the proof-bearing form is
`P_N(z)=S_N(z)^*S_N(z)+R_N(z)` with `R_N(z)>=0`, followed by a locally uniform bound `R_N -> R` and `R>=0`. If every such decomposition fails, record the exact residual and formulate a no-go theorem rather than forcing a sign.

## B — tau-Hankel
The theta Taylor moments and logarithmic-derivative coefficients are related nonlinearly. Derive the cumulant transform exactly and test whether
`Q_N(c)=sum_{i,j=0}^N c_i c_j tau_{i+j}`
has a theta-specific Gram/SOS representation for arbitrary N. Generic positive-measure moment arguments are explicitly excluded because nonlinear cumulants need not preserve Hankel positivity.

## C — de Branges / canonical system
Construct a theta-defined canonical system with characteristic/spectral determinant equal to Xi. Required lemmas: self-adjoint Hamiltonian, admissible de Branges space, convergence of the determinant normalization, and exact multiplicity-preserving correspondence between spectrum and Xi zeros. The construction must be completed before any assertion about zero reality.

## D — Li/Weil
Derive the Weil explicit-formula quadratic form directly from theta/Mellin data. Seek an RH-independent factorization into manifestly nonnegative terms for every admissible test function. A statement equivalent to RH is a reduction, not a closure, unless the positivity itself is independently proved.

## E — de Bruijn–Newman
Use the heat-flow family of the Xi kernel to isolate the endpoint obstruction. A complete route must establish the endpoint value required for RH, not merely quote the equivalence between RH and a sign condition on the Newman constant. Any lower/upper bound must be combined with an independent endpoint rigidity theorem.

## F — cross-route synthesis
Build explicit implication edges only when the hypotheses are proved. In particular:

- Pick/Stieltjes -> positive spectral representation -> Hankel positivity -> zero-reality theorem;
- theta all-degree Jensen/Hermite -> Laguerre–Pólya -> zero reality;
- de Branges -> self-adjoint spectral determinant -> real zeros;
- Li/Weil -> real-zero criterion only after independent positivity;
- de Bruijn–Newman -> RH only after the endpoint is forced.

## Adversarial checks
1. Never write a nontrivial zero as `1/2+it` before zero reality is established.
2. Never define an operator using the unknown zeros and then use its positivity.
3. Never infer all-degree Jensen hyperbolicity from raw moment/Hankel positivity alone.
4. Never promote numerical or finite-degree evidence to an infinite theorem.
5. Justify Tonelli/Fubini, dominated convergence, Poisson interchange, analytic continuation, and infinite determinant limits.
6. Track exact normalizations: Xi, H, theta moments, tau coefficients, and spectral determinants must not be silently rescaled.

## Immediate work order
Run A–E independently. For each route, the next proof-bearing object is either an exact nonnegative identity with all analytic hypotheses or the smallest exact obstruction. Then cross-check surviving identities against the other routes before attempting a final synthesis.

## Current ledger linkage
Supabase ledger entries 64–69 track Frontier 151A–F. GitHub issue #22 is the master issue. Notion contains the prior Frontier 110–149 records and their corrections.

## Final criterion
If no route reaches an unconditional zero-reality theorem, the mathematically correct outcome is an obstruction report and a new frontier. RH remains open until such a theorem is actually proved.
