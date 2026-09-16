# 2026-09-16 adversarial audit of a claimed RH proof

## Target
Avi Gershon, *The De Bruijn-Newman Constant Is Zero*, Preprints.org, 10.20944/preprints202604.1513.v1.

## Finding
The manuscript contains a circularity in its proposed global closure of the Desnanot-Jacobi hierarchy.

In Section 11, the argument introduces the zeros `z_k` of the entire generating function `g(z)=Xi(sqrt(z))` and then uses the representation

`z_k = -t_k^2`,

where `t_k` are the Riemann-zeta zero ordinates on the critical line, ordered for all `k`. That representation is valid for all zeros only if RH has already been established. The paper's finite verification of the first 10^13 zeros cannot supply the missing infinite statement.

The same assumption is then used in the spectral-gap estimate for the dissipation quantities `C_s(n)`, which is invoked to establish the unitarity/positivity condition needed for all Toeplitz minors. Thus the step from finite certification plus asymptotic heuristics to an all-(r,n) proof is not closed unconditionally.

## Precise location
See the manuscript's Section 11, especially the spectral-gap factorisation around equations (58) and the discussion immediately following it. The text explicitly identifies `z_k=-t_k^2` and uses the critical-line zero sequence beyond the finite verified range.

## Consequence
This does not prove RH false; it shows only that this particular claimed proof cannot currently be accepted as an unconditional proof. A valid replacement would need an RH-independent bound on the zeros of `g` (including their arguments), or a different argument establishing the required dissipation bound without assuming all zeros lie on the negative real axis.

## Research direction
A promising non-circular target remains:

1. prove a uniform all-order lower bound for consecutive Toeplitz minors `D_{r,n}` without using global zero locations;
2. combine it with the certified tail `n >= 10^18 r^3` from arXiv:2607.16795;
3. close the complementary wedge `n < 10^18 r^3` by a genuinely uniform argument in both `r` and `n`.

Finite determinant checks, Jensen-polynomial checks, and the verified first 10^13 zeta zeros are evidence only and are not substitutes for this infinite closure.
