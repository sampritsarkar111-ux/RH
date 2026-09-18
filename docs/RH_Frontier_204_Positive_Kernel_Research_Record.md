# RH Frontier 204 — Positive-Kernel / Spectrum Research Record

Date: 2026-09-18

## Status

**OPEN — not a proof of the Riemann Hypothesis.**

This document records the next research direction after Frontier 203. The goal is to turn the remaining RH bottleneck into explicit, independently checkable lemmas.

## 1. Central bridge

Seek an RH-independent real/even kernel K and Hilbert-space operator T such that the Weil functional satisfies

W_xi(g) = ||Tg||_H^2 + R(g),   R(g) >= 0,

for every admissible test function g.

The construction must use only established properties of xi/zeta and must not assume RH or an equivalent reformulation.

## 2. Spectrum requirement

A successful converse must also connect the spectrum of the resulting operator/kernel to the zero orbits of xi. Merely proving positive definiteness is insufficient: one must prove that positivity forces every nontrivial zero to satisfy Re(rho)=1/2.

Target structure:

W_xi(g) = W_O(rho)(g) + D_rho(g).

For an off-critical orbit O(rho), construct an admissible witness g_rho satisfying

W_O(rho)(g_rho) < 0

and

|D_rho(g_rho)| < -W_O(rho)(g_rho).

Then W_xi(g_rho)<0, contradicting Weil positivity.

## 3. Uniform separation theorem target

For every compact off-critical strip

S(delta,T) = {sigma+it : |sigma-1/2| >= delta, |t| <= T},

seek an explicit admissible witness family G(delta,T) and eta(delta,T)>0 such that

W_O(rho)(g_rho) <= -eta(delta,T)

and

|D_rho(g_rho)| <= eta(delta,T)/2.

The hard part is the global defect: all remaining zero orbits, prime-power terms, archimedean/Gamma terms, and limiting/truncation errors must be bounded uniformly.

## 4. Jensen/Turan bridge

For consecutive Turan ratios

r_n = gamma_{n+1}^2/(gamma_n gamma_{n+2}),

the exact cubic Jensen condition derived earlier is

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2 <= 0,

equivalently, for r,q >= 1,

(r-q)^2 <= (r-1)(q-1)[2(r+q-2)+3(r-1)(q-1)].

Writing r=1+x and q=1+y gives

(x-y)^2 <= xy[2(x+y)+3xy].

This identity is exact algebra, but it is not yet an unconditional theorem about all xi Jensen ratios. The missing step is an RH-independent mechanism forcing the required synchronization at every degree/shift.

## 5. Potential unification

A promising unification target is a single RH-independent totally-positive / positive-definite kernel whose minors imply Jensen-polynomial hyperbolicity while its quadratic form is the Weil functional.

This remains a research target, not an established theorem.

## 6. Anti-circularity requirements

Any claimed closure must:

1. define every operator/kernel/test space precisely;
2. prove positivity without RH;
3. establish the zero-spectrum correspondence independently;
4. control infinite sums and tails rigorously;
5. distinguish finite numerical evidence from an infinite theorem;
6. avoid using any criterion equivalent to RH as an assumption.

## 7. Computational protocol

Numerical experiments are admissible only as diagnostics. A rigorous computational claim should record precision, exact or interval arithmetic, truncation range, tail bounds, and an independently reproducible finite statement.

## 8. Current decisive wall

The decisive unresolved question is:

Can xi be represented by an RH-independent positive/totally-positive kernel whose spectrum encodes the zero orbits strongly enough that positivity implies critical-line support?

Until that bridge is proved, RH remains open in this project.
