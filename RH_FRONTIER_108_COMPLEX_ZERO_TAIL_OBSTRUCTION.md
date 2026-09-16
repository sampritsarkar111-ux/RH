# Frontier 108 — obstruction to the proposed zero-location-free determinant tail

Date: 2026-09-16

## Purpose

Test the Frontier 107 proposal rather than assuming its tail ratio estimate can hold for an arbitrary complex zero set.

For a real entire function with a conjugate dominant zero pair
z_± = R exp(±iθ), 0<θ<π, coefficient asymptotics generically contain an oscillatory factor
γ_n ≈ C R^{-n} cos(nθ+φ).

Thus there is no general zero-location-free reason for a determinant ratio
D_r(n+1)D_r(n-1)/D_r(n)^2 - 1
to have a fixed sign or to be exponentially small. The phase can approach zero or change sign. Pairing conjugate zeros makes coefficients real, but does not make the oscillatory contribution positive.

## Exact diagnostic example

Take

g_θ(z)=1-2 cos(θ) z+z^2,

whose zeros are exp(±iθ). Conjugate pairing produces real coefficients but no positivity mechanism. Multiplying by a distant canonical product preserves the same dominant-pair phenomenon over arbitrarily long coefficient ranges.

## Consequence for Frontier 107

The proposed exponential tail estimate cannot be accepted without an additional Riemann-specific property excluding dominant complex-pair oscillation. Proving that property is itself a substantial zero-location statement and cannot be assumed.

Therefore the Desnanot–Jacobi route is blocked more precisely at this point:

> Conjugate-pair grouping gives reality of coefficients, not positivity or monotone determinant ratios.

## Required replacement

A viable proof must exploit a genuinely Riemann-specific positivity identity independent of zero locations, such as an exact positive operator/Gram factorization of every Jensen/Hermite form. A generic coefficient-tail argument is insufficient.

This is a route obstruction, not a disproof of RH and not a claim that Xi actually has a dominant complex pair.