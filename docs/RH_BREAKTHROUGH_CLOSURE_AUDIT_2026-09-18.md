# RH Breakthrough Closure Audit — 2026-09-18

## Status

This document records a rigorous audit of the remaining logical bottleneck in the current RH program. It does **not** claim that the Riemann Hypothesis has been proved.

## 1. The decisive logical gap

A Weil-type criterion has the form

  W(g) = sum_{rho} H(g; rho) >= 0

for every admissible test function g, with the sum over non-trivial zeros (under the chosen normalization).

It is not sufficient to show that one summand H(g; rho_0) is negative for a hypothetical off-line zero rho_0.

The missing implication would be

  H(g; rho_0) < 0  ==>  W(g) < 0,

but the remaining zero contributions can have either sign and can, in principle, offset the negative contribution.

Therefore a valid contradiction requires a **global witness** g for which the entire Weil functional is strictly negative, with every other contribution bounded rigorously.

## 2. Second decisive gap: real-line positivity versus complex-plane positivity

For a test transform F satisfying F(u) >= 0 for real u, this does not imply

  Re F(z) >= 0

for complex z.

For the proposed Gaussian-polynomial witness

  F(z) = z^2 exp(-pi z^2/phi),   phi=(1+sqrt(5))/2,

an off-line zero rho=sigma+i gamma gives an argument z=gamma-i(delta), delta=sigma-1/2. The real part contains the phase factor

  cos(2 pi gamma delta / phi).

That factor can be negative. This establishes only that the **individual complex evaluation** can be negative; it does not establish negativity of the complete Weil sum.

## 3. New target: Global Witness Inequality (GWI)

Define a witness family G and a hypothetical off-line zero rho_0. A sufficient RH contradiction is the existence of g in G and an explicit margin epsilon>0 such that

  H(g;rho_0) + B_rest(g,rho_0) <= -epsilon,

where B_rest is a rigorous upper bound for the sum of all remaining zero, prime, gamma, and limiting contributions in the exact normalization.

The proof obligation is therefore global, not termwise.

## 4. New target: Witness Isolation Lemma (WIL)

A particularly strong route would prove:

For every off-line rho_0, there exists an admissible g_{rho_0} such that

  H(g_{rho_0};rho_0) <= -2 epsilon

and

  |sum_{rho != rho_0} H(g_{rho_0};rho)| <= epsilon.

Then W(g_{rho_0}) < 0, contradicting Weil positivity.

The difficult part is the second inequality. It is the genuine isolation problem.

## 5. Conjugate and functional-equation symmetry

Because non-trivial zeros occur with the standard conjugation and functional-equation symmetries, a witness cannot casually isolate a single zero. A rigorous construction should first group the relevant symmetry orbit and prove negativity for the orbit contribution while controlling every other orbit.

Thus the practical target is an **orbit-isolating witness**, not a single-zero witness.

## 6. Reusable anti-circularity rule

Any proposed RH proof should separate:

1. unconditional analytic identities;
2. unconditional estimates;
3. assumptions equivalent to RH;
4. numerical observations;
5. the final implication to RH.

An estimate derived using RH, even if later embedded in an equivalence framework, cannot serve as an unconditional proof step.

## 7. Machine-checkable certificate schema

A future certificate should contain:

- exact test function definition;
- admissibility proof;
- exact explicit-formula normalization;
- symmetry-orbit decomposition;
- certified enclosure for the target orbit;
- certified enclosure for all remaining zeros;
- certified archimedean/gamma remainder;
- certified prime-side remainder where applicable;
- order-of-limits justification;
- strict negative final interval [-b,-epsilon];
- independent recomputation using a second representation.

The decisive acceptance condition is:

  upper_bound(W(g)) < 0.

A floating-point value that is merely negative is not sufficient.

## 8. New research theorem target

**Global Witness Theorem (target).**
If every hypothetical off-critical symmetry orbit admits an admissible orbit-isolating witness satisfying the WIL bounds with a uniform positive margin, then the Riemann Hypothesis follows.

**Proof.**
Assume an off-critical orbit exists. Apply WIL to obtain an admissible g with W(g)<0. Weil positivity requires W(g)>=0 for every admissible g. Contradiction. Hence no off-critical orbit exists. Therefore every non-trivial zero lies on Re(s)=1/2.

This theorem is elementary once WIL is established; WIL is the substantive open problem.

## 9. Breakthrough direction

The most promising structural transformation is to stop searching for a magical single kernel and instead solve an optimization/separation problem in the admissible test-function cone:

  minimize W(g) subject to g admissible and normalized at the target orbit.

If the infimum can be bounded strictly below zero under the hypothesis of an off-line orbit, the separation itself becomes the witness.

This reframes the bottleneck as a rigorous convex-cone separation problem, with the remaining work concentrated in proving density/approximation and explicit remainder bounds.

## 10. Current conclusion

The program has produced a sharper and more defensible endpoint:

  RH
  <=> global Weil positivity
  <=> absence of an admissible global negative witness.

The remaining mathematical wall is therefore not merely 'find a negative term'. It is:

  **construct and certify a globally negative admissible witness for every possible off-critical symmetry orbit, without assuming RH anywhere in the construction.**

Any future claimed closure should be tested against this criterion.
