# RH Frontier 199 — Formal Proof Attempt

Date: 2026-09-18

## Claim under investigation

We seek to prove RH by an unconditional route through Weil positivity. This document is a formal attempt and records the exact point where a proof may or may not close.

## 1. Weil criterion

For a suitable admissible test function, RH is equivalent to nonnegativity of the corresponding Weil explicit-formula quadratic form. Therefore a proof must establish this positivity for the entire admissible class, not merely for one test function.

## 2. Why the common complex-evaluation shortcut fails

For an off-line zero rho=sigma+i gamma, an admissible Fourier transform that is nonnegative on the real axis can take complex or negative real values at gamma-i(sigma-1/2). Therefore a negative value of a single summand does not imply the full Weil sum is negative.

The full sum includes all zeros and arithmetic/archimedean terms. A contradiction requires a globally controlled witness.

## 3. Formal target theorem

Prove one of:

(P) Q(f)=||Tf||^2+R(f), R(f)>=0, exactly for all admissible f;

(O) every hypothetical off-line zero orbit has an admissible witness g with target-orbit negativity dominating all remaining terms;

(J) all Jensen polynomials of xi are hyperbolic by an unconditional theorem.

Any one would provide a route to RH through a known equivalence.

## 4. New local-to-global Jensen target

Define consecutive Turan ratios

r_n=gamma_{n+1}^2/(gamma_n gamma_{n+2}).

Degree 3 reduces to

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2.

At r=1+x, q=1+y,

F=(x-y)^2-2xy(x+y)-3x^2y^2.

Thus proving F<=0 requires a quantitative relation between adjacent ratio excesses and their variation. A candidate barrier is

|r_{n+1}-r_n|^2 <= C_n(r_n-1)(r_{n+1}-1),

but deriving a sufficiently strong unconditional C_n remains open.

## 5. Failure test

The inequality F<=0 is NOT implied by r>=1 and q>=1 alone. Symbolic elimination exhibits a nonempty region with r,q>=1 and F>0. Therefore plain Turan/log-concavity information cannot close Jensen degree 3.

This is a useful negative theorem: any successful Jensen proof must exploit additional Riemann-specific structure.

## 6. Formal proof skeleton

Assume an off-line zero rho exists.

A valid proof must:
A. choose an admissible g;
B. derive the complete explicit formula exactly;
C. isolate the orbit contribution;
D. bound every complementary zero contribution;
E. bound prime and archimedean tails;
F. establish strict negativity;
G. contradict Weil positivity.

The missing theorem is C-E simultaneously with explicit uniform constants.

## 7. Conclusion

No complete RH proof is claimed. Frontier 199 eliminates one tempting but invalid shortcut and narrows the next breakthrough to either a genuine positive factorization, a globally dominated orbit witness, or a Riemann-specific all-degree Jensen theorem.