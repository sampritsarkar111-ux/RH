# RH Frontier 209 — Pólya-Kernel Route: Exact Obstruction and Breakthrough Target

Date: 2026-09-18

## Status
**OPEN — no RH proof.**

## 1. New horizon

SciSpace surfaced a recent manuscript claiming RH from strict positivity of Pólya's Fourier-transform kernel Phi(u). This is a useful target because Pólya's criterion gives an exact equivalence: proving the required global nonnegativity of Phi would prove RH.

But the decisive issue is the claimed intermediate-region positivity. An assertion that numerical computation on a finite interval is “controlled” is not enough unless the actual interval enclosure, truncation bound, arithmetic certificate, and endpoint/asymptotic covering are supplied and independently verified.

## 2. Proof-grade reduction

Let Phi be the Fourier transform of the completed Xi kernel in a normalization for which Pólya's criterion applies.

A valid proof would require:

(A) exact derivation of Phi(u);
(B) analytic proof Phi(u)>=0 on (-infinity,-U] union [U,infinity);
(C) a finite interval [−U,U] covered by a rigorous enclosure argument, not floating-point sampling;
(D) explicit treatment of truncation and tails;
(E) exact transfer from Phi>=0 to RH through the established equivalence.

Thus the computational center is a theorem of the form

Phi(u) >= m(u) > 0

with m(u) certified by interval/rational arithmetic for every u in the finite region.

## 3. New “certificate compression” idea

Instead of sampling Phi, search for a decomposition

Phi(u)=P(e^{-c u},u) + R(u)

where P is manifestly nonnegative and R has a globally certified bound

|R(u)| <= P(e^{-c u},u)

on the target interval.

An even stronger certificate is

Phi(u)=sum_k w_k(u)^2 + R_tail(u),

with R_tail(u)>=0 proved analytically.

This converts an infinite-series positivity problem into a finite symbolic positivity certificate plus a rigorous tail theorem.

## 4. Symmetry warning

The theta/modular symmetry can cover asymptotic regions, but symmetry alone cannot establish positivity in the intermediate region. The polynomial counterexample from Frontier 208 remains the generic warning.

## 5. Computational proof gate

Any claimed finite-region certificate must provide:
- exact formula for the truncation;
- interval enclosure for every omitted term;
- certified derivative/Lipschitz or monotonicity bounds if gridding is used;
- enough precision to separate zero from strict positivity;
- reproducible exact finite inequalities.

A table of sampled values is evidence, not proof.

## 6. Relation to the three-scale Weil route

If Phi positivity is established globally, the RH follows through the Pólya equivalence and the need for an orbit-by-orbit Weil defect estimate disappears. Therefore this route may be more economical than direct orbit separation.

## 7. Jensen bridge

The cubic synchronization identity remains exact:

(r-q)^2 <= (r-1)(q-1)[2(r+q-2)+3(r-1)(q-1)].

A future kernel certificate might imply total positivity and hence all-degree Jensen hyperbolicity, but that implication still needs proof.

## 8. Decision point

The strongest immediate theorem target is:

**Global Pólya-kernel positivity certificate:** derive an explicit finite sum-of-squares/positive-remainder representation for Phi(u) that covers a compact interval, with analytic positivity outside it.

If achieved, combine it with Pólya's equivalence to obtain a proof of RH. If the certificate fails, record the exact sign obstruction rather than weakening the claim.

## Conclusion

Frontier 209 identifies a potentially shorter proof path: prove global positivity of the Pólya Fourier kernel with a proof-grade symbolic certificate. The recent claimed proof found by SciSpace is not adopted as verified; its finite numerical step is precisely the part that must be independently audited.

RH remains open.