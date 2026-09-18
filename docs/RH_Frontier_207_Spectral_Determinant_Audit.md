# RH Frontier 207 — Spectral Determinant Audit and Proof-Gate Extraction

Date: 2026-09-18

## Status

**OPEN — RH remains unproved.**

## 1. New horizon: spectral construction must be audited at the determinant level

SciSpace surfaced recent manuscripts claiming spectral-geometric proofs of RH using self-adjoint operators. Their abstracts assert that a zeta-related determinant has zeros matching xi/zeta zeros and then use self-adjointness to force critical-line location.

The proof-bearing issue is not merely constructing a self-adjoint operator. It is proving, independently and exactly, a spectral identity of the form

ZetaDet(D(s)) = C(s) xi(s)

(or an equivalent canonical determinant identity)

with all domains, boundary conditions, regularization, multiplicities, growth factors, and normalization controlled.

Self-adjointness alone only constrains the spectrum of the operator. It does not identify an arbitrary analytic function's zeros with that spectrum.

## 2. Spectral determinant lemma

If A is self-adjoint and its spectral parameter enters through an expression whose zero set is exactly the spectrum under a rigorously established determinant identity, then the relevant spectral parameters are real. This can imply critical-line location after an explicitly proved affine change of variable.

But the determinant identity is an independent theorem and cannot be inferred from the functional equation of xi.

## 3. Adversarial test

For any proposed D(s), require proof of all six bridges:

1. D(s) is well-defined on a specified Hilbert domain.
2. The relevant operator at real spectral parameter is self-adjoint.
3. The regularized determinant exists.
4. Its zeros equal the spectral parameters with multiplicity.
5. The determinant equals xi(s), up to a completely controlled nonvanishing factor.
6. The parameter map sends the real spectrum exactly to Re(s)=1/2.

Failure of any bridge leaves RH unproved.

## 4. Why this is useful for our program

This gives a second independent attack on the previous kernel route. Instead of guessing a positive kernel first, search for a rigorously realizable spectral determinant whose self-adjointness supplies the line constraint. If that route fails at the determinant identity, the failure is mathematically explicit.

## 5. Three-scale Weil route remains independent

For an off-critical zero rho, the proof target remains

A_rho(g)<=-eta,

|D_near(g)|<=eta/4,

|D_far(g)|<=eta/4,

which implies W_xi(g)<0.

This route does not require a spectral operator if the estimates can be proved directly.

## 6. Gaussian phase diagnostic

For a Gaussian transform exp(-a z^2), a complex off-line evaluation can have oscillatory real part. Such a sign is useful for witness design but is not itself a Weil contradiction. The complete zero sum and arithmetic/archimedean terms must be controlled.

## 7. Jensen bridge

The exact cubic gate remains

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2,

with

F<=0 iff
(r-q)^2 <= (r-1)(q-1)[2(r+q-2)+3(r-1)(q-1)]

for r,q>=1.

No all-degree RH-independent synchronization theorem has yet been obtained.

## 8. Proof status

No complete proof has been found. Frontier 207 instead identifies a rigorous audit framework that can reject incomplete Hilbert–Polya-style arguments at the exact point where the missing determinant/spectral identification occurs.

## 9. Next theorem target

Construct or rule out a concrete operator A with a fully rigorous canonical determinant identity

det_reg(s-A) = nonzero_factor(s) * xi(s)

and a self-adjoint spectral parameterization s=1/2+i lambda.

If such an identity is proved with the required analytic details, the RH implication becomes immediate. If it cannot be established, the obstruction should be recorded and the three-scale Weil route pursued instead.
