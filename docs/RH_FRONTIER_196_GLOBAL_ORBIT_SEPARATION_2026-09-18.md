# RH Frontier 196 — Global Orbit Separation

## New mathematical frontier

The decisive object is the complete Weil functional, not an individual zero contribution:

W(g) = W_O(g) + W_rest(g).

For a hypothetical off-critical symmetry orbit O, a sufficient contradiction is an admissible test function g and epsilon > 0 satisfying

W_O(g) <= -2 epsilon,
|W_rest(g)| <= epsilon.

Then W(g) <= -epsilon < 0, contradicting Weil positivity.

## Orbit-Separation Theorem (target)

If every off-critical orbit O admits an admissible g_O with a rigorous enclosure

W_O(g_O) + R_O(g_O) < 0,

where R_O encloses every non-target zero and all required archimedean, prime-side, and limiting terms, then RH follows.

Proof: Weil positivity requires W(g_O) >= 0 for every admissible g_O, while the certified enclosure gives W(g_O) < 0. Contradiction.

## Cone-separation reformulation

Let A be the admissible test-function cone and N(g)=1 a normalization. A stronger route is to prove

inf_{g in A, N(g)=1} W(g) < 0

whenever an off-critical orbit exists, followed by a finite admissible certificate and explicit remainder bounds.

Thus the remaining wall becomes a rigorous cone-separation + quantitative approximation problem.

## Phase mechanism

For F(z)=z^2 exp(-pi z^2/phi), phi=(1+sqrt(5))/2, real-axis positivity does not imply Re F(z)>=0 for complex z. A Wolfram computation at z=14.13-0.2i gives

Re F(z) approximately -4.732614291504393e-168,

and phase cosine approximately -0.021587019746475516.

This is evidence for a local complex-phase mechanism only; it is not a global RH contradiction.

## Proof obligations

- exact normalization of the Weil functional;
- admissibility of the witness class;
- symmetry-orbit rather than single-zero isolation;
- unconditional bounds on all non-target zero contributions;
- archimedean/gamma remainder;
- prime-side remainder where required;
- justified limiting operations;
- independently checkable strict inequalities.

## Status

This is a research frontier, not a claimed proof of RH. The decisive remaining theorem is a certified global negative witness for every possible off-critical orbit.
