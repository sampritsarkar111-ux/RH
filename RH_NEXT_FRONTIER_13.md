# Riemann Hypothesis — Frontier 13: de Bruijn–Newman Route Cross-Check

Date: 2026-09-16

## Alternative exact reduction

For the heat-flow family
\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\]
there is a finite de Bruijn–Newman constant \(\Lambda\) such that all zeros are real exactly for \(t\ge\Lambda\). RH is equivalent to \(\Lambda\le0\). Rodgers and Tao proved the complementary inequality \(\Lambda\ge0\), so RH is equivalent to the boundary statement \(\Lambda=0\).

## Proof attempt

A complete proof through this route therefore needs a rigorous argument that the heat flow at exactly \(t=0\) has only real zeros. The known \(\Lambda\ge0\) result does not provide that upper-bound/boundary step; it proves only that the threshold cannot be negative.

Known effective work also gives unconditional positive upper bounds, so the interval containing \(\Lambda\) is narrow compared with the original formulation, but it does not collapse to zero.

## Strategic consequence

There are now two exact proof targets in the repository:

1. **Jensen route:** prove all \(J_{d,n}\) hyperbolic.
2. **Heat-flow route:** prove \(\Lambda\le0\), which together with \(\Lambda\ge0\) gives \(\Lambda=0\).

The two routes are related through the same xi/Fourier structure, but neither missing theorem has been proved here.

## Status

No complete RH proof has been obtained. The new value of this frontier is the precise boundary target \(\Lambda=0\), rather than an attempt to reprove the already-known lower bound.
