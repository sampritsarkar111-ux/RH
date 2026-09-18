# RH Frontier 208 — False-Proof Kill Test and Symmetry-vs-Spectrum Separation

Date: 2026-09-18

## Status
**OPEN — RH remains unproved.**

## 1. Critical adversarial finding

SciSpace surfaced multiple 2025–2026 repository manuscripts whose abstracts claim complete RH proofs via self-adjoint operators. One recurring proposed step is:

functional equation + Schwarz reflection
=> xi is real on the critical line
=> xi has a self-adjoint/operator structure
=> all zeros are on the critical line.

The first implication is correct. The second is not.

For every entire function f satisfying

f(s)=f(1-s),  f(conjugate(s))=conjugate(f(s)),

the restriction t -> f(1/2+it) is real-valued. These symmetries alone do not prohibit zeros away from the critical line.

## 2. Explicit counterexample family

For any real a != 1/2, define

f_a(s)=(s-a)(s-(1-a))(s-(a-bar?))

For real a this simplifies to

f_a(s)=(s-a)(s-(1-a)).

It satisfies f_a(1-s)=f_a(s) and has real coefficients, hence f_a(conjugate(s))=conjugate(f_a(s)). Yet its zeros are a and 1-a, generally off the critical line.

A concrete choice is a=1/4:

f(s)=(s-1/4)(s-3/4).

Then

f(1-s)=f(s),

f(conjugate(s))=conjugate(f(s)),

but zeros occur at 1/4 and 3/4.

Therefore symmetry plus reality on the critical line cannot prove RH.

## 3. Correct logical distinction

The valid theorem is:

functional equation + Schwarz reflection
=> xi(1/2+it) is real for real t.

The invalid theorem is:

xi(1/2+it) real
=> every zero of xi lies on the line.

A real-valued function of a real variable only tells us about zeros already restricted to that one-dimensional slice. It says nothing about zeros elsewhere in C.

## 4. Spectral proof requirement

To turn xi into a spectral determinant, one must independently construct an operator A and prove

det_reg(s-A)=E(s) xi(s)

with E nonzero and with the spectral parameterization mapping real spectrum to s=1/2+i lambda.

The functional equation does not supply this identity automatically.

## 5. New proof gate

**Symmetry-to-spectrum bridge theorem.**

Find an RH-independent construction in which the two symmetries of xi imply an actual operator adjoint relation

A*=A,

and separately prove that the complete zero divisor of xi is exactly the spectral divisor of A.

Only then does the spectral theorem yield RH.

## 6. Three-scale Weil route remains available

For an off-critical orbit O(rho), seek

A_O(g)<=-eta,

|D_near(g)|<=eta/4,

|D_far(g)|<=eta/4.

This remains a direct analytic route independent of Hilbert–Polya.

## 7. New horizon

The project should treat every proposed RH proof as a sequence of bridge claims and actively seek a counterexample whenever a bridge is asserted from symmetry alone.

This produces a rigorous **false-proof kill test**: any argument that derives global zero localization from critical-line reality without an independent divisor/spectral theorem is rejected.

## Conclusion

Frontier 208 does not solve RH. It does, however, close a tempting but invalid proof shortcut and makes the missing spectral theorem explicit. This prevents the project from mistaking symmetry for spectral realization.
