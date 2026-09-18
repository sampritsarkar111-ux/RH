# Parallel RH Gate Audit — 2026-09-18

## Executive result

This run does **not** produce a rigorous proof of the Riemann Hypothesis. Instead, it found a decisive obstruction to one proposed Pólya gate and sharpened the exact proof obligations for all five gates.

The Riemann Hypothesis remains an open problem.

## 1. Pólya gate: global positivity

Candidate auxiliary series:
S(x) = Sum_{n>=1} (4 π^2 n^4 x^2 - 6 π n^2 x) exp(-π n^2 x), x>0.

A high-precision Wolfram computation using the first 100 terms sampled x from 10^-3 to 10^3 produced a negative value at the first sampled point:
S(10^-3) ≈ -1.0416443282267591 × 10^-10.

Therefore the blanket statement S(x)>0 for all x>0 is false for this exact displayed series. Any claimed proof using this positivity statement must repair the normalization/kernel identity before proceeding. Numerical evidence is not itself a proof of the opposite global statement, but a single certified negative value would suffice to refute it; the computed result strongly identifies the first place requiring interval-arithmetic certification.

## 2. Weil gate

The correct proof-bearing target is not merely “an off-line zero gives a negative contribution.” Weil's criterion is a global positivity condition over an admissible test-function class. A rigorous closure needs a theorem of the form:

If an off-line zero exists, construct an admissible test function f for which the complete Weil functional W(f)<0.

The test function must control all zero terms and the prime/archimedean terms simultaneously. A pointwise contribution from one hypothetical zero is insufficient because the remaining zeros can contribute with either sign.

## 3. Spectral gate

A self-adjoint operator whose spectrum is numerically fitted to imaginary parts of zeta zeros is not enough. The proof-bearing identity must establish, with domains and multiplicities,
det_reg(H - z) = C e^{az+b} ξ(1/2+z)
(or an equivalent canonical-product identity),
where H is genuinely self-adjoint and the determinant is defined in a rigorous regularized sense.

Only then does self-adjointness force the relevant zero parameters to be real. Constructing H from the zero set itself is circular unless the construction is independent of RH and the determinant identity is independently proved.

## 4. Jensen gate

Finite-degree Jensen-polynomial hyperbolicity, or asymptotic hyperbolicity in fixed degree, does not by itself establish RH. The proof-bearing theorem must be unconditional and cover every degree and every required shift/scaling, with exact coefficient identities connecting the Jensen family to ξ.

A computationally positive list of Jensen discriminants is evidence, not an all-degree theorem.

## 5. Unified kernel

A useful non-circular unified target is an operator/kernel identity in which all four gates are consequences of one positive quadratic form:

W(f) = <T f, f> = ||A f||^2,

together with exact transforms linking:
Pólya Fourier positivity ↔ T positivity,
Weil positivity ↔ T positivity,
spectral self-adjointness ↔ T being a positive/self-adjoint realization,
Jensen hyperbolicity ↔ finite principal minors / total positivity of the same kernel.

The critical requirement is that T (or K_RH) be defined directly from established zeta/theta data, not from the assertion that its spectrum equals the desired zeros.

## New breakthrough direction: obstruction-first closure

Before attempting a grand synthesis, every proposed bridge should pass three tests:

1. Non-circular definition: the object is defined without assuming RH.
2. Exact equivalence: every arrow has a published/provable theorem, not numerical agreement.
3. Global quantifier: the statement covers the entire domain/test-function class/all degrees, not a finite range.

The current Pólya candidate fails test 2/3 because its displayed S(x) is numerically negative near x=10^-3.

## Status

Pólya: OPEN — displayed positivity target is contradicted numerically and needs correction.

Weil: OPEN — need a globally admissible off-line witness.

Spectral: OPEN — need an independent self-adjoint realization plus exact determinant/divisor identity.

Jensen: OPEN — need unconditional all-degree hyperbolicity.

Unified K_RH: OPEN — promising organizing framework, but no non-circular exact kernel has yet been established.

## Reproducibility

The computational checks in this audit were run through Wolfram. Academic discovery was cross-checked against SciSpace, including recent manuscripts that claim RH proofs; those manuscripts are treated as research claims rather than established resolution of the problem.

