# Frontier 96 — Correction to modular-scale derivation and unsummed gate

Date: 2026-09-16

## Important correction

The previous Frontier 94 used a logarithmic variable convention that was not sufficiently normalized against the standard xi-kernel. The standard kernel is commonly written with
\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\]
and satisfies \(\Phi(-u)=\Phi(u)\). An equivalent rescaling uses exponents \(9u\), \(5u\), and \(e^{-\pi m^2e^{4u}}\). The factor-of-two convention must be tracked consistently.

This does not alter the structural conclusion: the modular reflection is a reflection in logarithmic theta scale and preserves the quadratic scale invariant used after the beta substitution. But all future symbolic work must use one fixed normalization.

## Standard unsummed lattice term

Fix the standard normalization
\[
\phi_m(u)=\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad \Phi(u)=\sum_{m\ge1}\phi_m(u).
\]
The exact Fourier representation is
\[
\Xi(t)=\int_{-\infty}^{\infty}\Phi(u)e^{itu}\,du
\]
up to the chosen conventional normalization of \(\Xi\).

The modular transformation is encoded by theta inversion, but crucially the individual \(\phi_m(u)\) terms do **not** separately satisfy the evenness relation. Evenness belongs to the completed sum \(\Phi\), after Poisson/Jacobi transformation.

Therefore the earlier statement that the modular orbit acts termwise as \(u\mapsto-u\) on each lattice summand was too strong and must not be used.

## Revised proof target

The actual breakthrough test is now sharper:

1. Start from the unsummed product
\[
\Phi(u)\Phi(v)=\sum_{m,k\ge1}\phi_m(u)\phi_k(v).
\]
2. Form the exact factorial-corrected degree-two quadratic form before summing m,k.
3. Apply Poisson/Jacobi inversion to the **complete lattice sum**, not termwise.
4. Determine whether the transformed double-lattice expression admits a positive Gram decomposition.

The target is
\[
\boxed{
\Delta_{2,n}=\sum_\alpha\iint |P_{n,\alpha}(u,v)|^2\,d\lambda_\alpha(u,v)\ge0.
}
\]
A valid identity must hold for every \(n\ge0\), with all interchanges justified.

## Why this is genuinely stronger

Frontier 94 ruled out a pointwise pairing of the already-collapsed y-kernel. Frontier 96 shows that the correct place to search is earlier: modularity is a global identity of the completed theta lattice, not a pointwise symmetry of an individual summand.

If this gate succeeds, the next lift is the Hermite matrix:
\[
\mathsf H_{d,n}=A_{d,n}^*G_{d,n}A_{d,n},\qquad G_{d,n}\succeq0.
\]
If the double-lattice kernel remains indefinite after exact Poisson transformation, that is a structural obstruction to this entire modular-Gram route.

## External consistency check

Current literature confirms the standard facts used here: the Riemann xi-function has a Fourier representation through an even theta kernel, and evenness follows from the Jacobi theta transformation. Recent papers continue to treat positivity/log-concavity or related kernel conditions as nontrivial routes rather than established RH proofs.

## Status

**Correction + sharpened target.** No RH proof is claimed. The key next computation is the exact complete-lattice Poisson transform of the degree-two factorial-corrected form.
