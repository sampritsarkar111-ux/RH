# Frontier 115 — Pick/Herglotz master-kernel target

Date: 2026-09-17

## Goal

Construct a zero-independent analytic object from the theta representation whose positivity is strong enough to imply that every zero of \(\Xi\) is real.

## Critical correction

The expression \(M(z)=-\Xi'(z)/\Xi(z)\) is meromorphic, so a global Herglotz statement must be formulated on each zero-free domain. One cannot simply assert \(\operatorname{Im}M(z)\ge0\) throughout the upper half-plane before proving that \(\Xi\) has no zeros there. The correct proof-bearing route is therefore to construct a positive Pick kernel or an equivalent representation first, then deduce the pole restriction.

## Kernel target

Seek an explicit theta-derived kernel \(P(z,w)\) on \(\mathbb C^+\) satisfying
\[
P(z,w)=\frac{M(z)-\overline{M(w)}}{z-\overline w}
\]
where defined, together with a positive-kernel extension across removable points. Prove
\[
\sum_{j,k}c_j\overline{c_k}P(z_j,z_k)\ge0
\]
for arbitrary finite systems.

## Closure theorem

If the resulting meromorphic object has a genuine Herglotz representation with representing measure supported on \(\mathbb R\), then its poles are real. Since poles correspond to zeros of \(\Xi\), all zeros of \(\Xi\) are real, giving RH.

## Main algebraic attack

Insert the exact theta/Fourier representation into finite Pick matrices before taking limits. Search for a factorisation by:

1. symmetrisation under \(u\mapsto-u\);
2. Binet–Cauchy expansion;
3. Vandermonde determinants in multiple theta variables;
4. reflection identities of the completed theta kernel;
5. positive integral representations of reciprocal differences.

No pointwise sign claim is allowed unless proved.

## Failure certificate

An exact negative principal minor at any finite matrix size disproves this specific kernel ansatz. It does not disprove RH.

## Required audit

The final argument must separately establish analyticity, convergence, kernel positivity, extension to all required points, pole/zero correspondence, multiplicities, and the final implication \(\Re\rho=1/2\).
