# Frontier 124 — Theta de Branges H-inequality stress test

Date: 2026-09-17
Status: Strong numerical obstruction; interval-certified proof still required

## Setup

Let

\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad \Phi(-u)=\Phi(u),
\]

and define the theta-derived candidate

\[
E(z)=2\int_0^\infty \Phi(u)e^{-izu}\,du,
\qquad
E^\#(z)=\overline{E(\bar z)}.
\]

Then

\[
\Xi(z)=\frac{E(z)+E^\#(z)}2.
\]

For \(z=x+iy\), \(y>0\), the proposed Hermite–Biehler defect is

\[
\mathcal H(x,y)=|E(x+iy)|^2-|E^\#(x+iy)|^2
\]

with exact double-integral representation

\[
\mathcal H(x,y)=8\int_0^\infty\!\int_0^\infty
\Phi(u)\Phi(v)\sinh(y(u+v))\cos(x(u-v))\,du\,dv.
\]

The hoped-for global closure condition was \(\mathcal H(x,y)>0\) for all real \(x\) and \(y>0\).

## Exact boundary derivative

Since \(\mathcal H(x,0)=0\), differentiation at \(y=0\) gives

\[
\begin{aligned}
\partial_y\mathcal H(x,0)=16\Bigg[&\left(\int_0^\infty u\Phi(u)\cos(xu)\,du\right)
\left(\int_0^\infty \Phi(u)\cos(xu)\,du\right)\\
&+\left(\int_0^\infty u\Phi(u)\sin(xu)\,du\right)
\left(\int_0^\infty \Phi(u)\sin(xu)\,du\right)\Bigg].
\end{aligned}
\]

Direct numerical quadrature of the exact theta-series integrals gives

\[
\partial_y\mathcal H(17,0)\approx -2.5268760767571013\times10^{-5}.
\]

Therefore, if this sign is interval-certified, continuity implies \(\mathcal H(17,y)<0\) for all sufficiently small positive \(y\).

## Direct numerical stress test

The same exact integral evaluated numerically gives

\[
\mathcal H(17,10^{-3})\approx-2.5268763529982106\times10^{-8}<0,
\]

and

\[
\mathcal H(17,10^{-2})\approx-2.526903700803398\times10^{-7}<0.
\]

Additional values at \(y=0.01\):

| x | H(x,0.01) |
|---:|---:|
| 0 | 4.2809633959594017e-4 |
| 5 | 2.4859711212634434e-4 |
| 10 | 4.254242520520556e-5 |
| 14 | 2.339538313354787e-6 |
| 17 | -2.526903700803398e-7 |
| 20 | -5.335070699327106e-8 |
| 25 | 9.451518612193037e-10 |
| 30 | -2.8931497133767363e-11 |
| 40 | 1.523748387442940e-14 |
| 50 | -4.439647534969779e-18 |

Derivative scan:

- \(x=14\): \(+2.3395564017298165\times10^{-4}\)
- \(x=15\): \(+5.711677562382046\times10^{-5}\)
- \(x=16\): \(-1.0230339382687396\times10^{-5}\)
- \(x=17\): \(-2.5268760767571013\times10^{-5}\)
- \(x=18\): \(-2.059365636723285\times10^{-5}\)
- \(x=20\): \(-5.335105536250753\times10^{-6}\)

## Interpretation

The positivity of \(\Phi(u)\) for \(u\ge0\) does not imply positivity of \(\mathcal H\), because the factor \(\cos(x(u-v))\) is oscillatory. The canonical theta-derived \(E\) and the identity \(\Xi=(E+E^\#)/2\) remain valid, but the proposed universal Hermite–Biehler inequality is numerically contradicted.

This does **not** prove that RH is false. It only obstructs this particular de Branges closure mechanism.

## Required certification before theorem-level use

1. Bound the truncation error of the theta series uniformly over the numerical integration domain.
2. Bound quadrature/discretization error with rigorous interval arithmetic.
3. Produce an interval strictly below zero for either \(\partial_y\mathcal H(17,0)\) or \(\mathcal H(17,y_0)\) at an explicit positive \(y_0\).
4. If certified, record the canonical \(E\)-construction as a rigorously refuted Hermite–Biehler candidate.

## Next research target

Do not force \(\mathcal H>0\). Instead investigate:

- a modified theta-defined \(E_*(z)\) satisfying \(E_*+E_*^\#=2\Xi\) while possessing a genuinely positive Hermite–Biehler defect; or
- an independent theta-generated characteristic determinant / Weyl–Herglotz function whose real-zero property implies RH.

Any successful replacement must be derived without assuming RH or using the locations of zeta zeros.
