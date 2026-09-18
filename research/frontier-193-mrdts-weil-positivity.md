# RH Frontier 193 — MRDTS → Weil Positivity Attack
Date: 2026-09-18

## Status

This document records a proof-oriented research audit. It does **not** claim that the Riemann Hypothesis has been proved.

## 1. Exact MRDTS arithmetic channel

For Re(s) > 1, the corrected Möbius divisor channel is

[
M_d(s)=\frac{d^{-s}}{\zeta(s)}.
]

Therefore

[
\frac{d}{ds}\log M_d(s)
=
-\log d-\frac{\zeta'(s)}{\zeta(s)}.
]

This is an exact arithmetic identity in the half-plane of absolute convergence.

## 2. Standard completed-zeta normalization

The completed zeta function is

[
\xi(s)=
\frac12 s(s-1)\pi^{-s/2}
\Gamma\!\left(\frac{s}{2}\right)\zeta(s).
]

Its logarithmic derivative decomposes as

[
\frac{\xi'(s)}{\xi(s)}
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi\!\left(\frac{s}{2}\right)
+\frac{\zeta'(s)}{\zeta(s)}.
]

Thus the MRDTS channel supplies the reciprocal-zeta / logarithmic-derivative component, while the explicit Gamma/pi factors provide the standard archimedean completion. This is an identity-level normalization bridge only; it does not determine zero locations.

## 3. Decisive infinite-dimensional target

Define, on a rigorously specified dense admissible test space,

[
Q_{\mathrm{MR}}(f)
=
Q_{\mathrm{prime}}(f)
+
Q_{\mathrm{arch}}(f)
+
Q_{\mathrm{boundary}}(f).
]

The proof-bearing equality to establish is

[
Q_{\mathrm{MR}}(f)=W_\xi(f)
\qquad
\forall f\in\mathcal D,
]

where (W_\xi) is the Weil quadratic form for the completed zeta function.

Every convergence statement, analytic continuation, boundary contribution, and limit/interchange must be justified.

## 4. Independent positivity target

A second theorem is required:

[
Q_{\mathrm{MR}}(f)\ge 0
\qquad
\forall f\in\mathcal D,
]

with positivity derived independently of RH and without assuming any RH-equivalent assertion.

A particularly strong desired factorization is

[
Q_{\mathrm{MR}}(f)
=
\|T_{\mathrm{MR}}f\|_{\mathcal H}^{2}
+
R_{\mathrm{MR}}(f),
]

where (R_{\mathrm{MR}}(f)\ge0), ideally (R_{\mathrm{MR}}=0).

Equivalently,

[
Q_{\mathrm{MR}}(f)
=
\langle f,A_{\mathrm{MR}}f\rangle,
\qquad
A_{\mathrm{MR}}\succeq0,
]

with (A_{\mathrm{MR}}) constructed solely from arithmetic/theta/archimedean data, not from the unknown zero set.

## 5. Rejected shortcut: a single negative zero contribution

A test in Wolfram confirms that for a hypothetical off-line zero, a selected Gaussian-polynomial test term can have a negative real part.

That is **not** a contradiction to Weil positivity: the complete Weil functional contains the full zero contribution together with prime and archimedean terms. A single negative summand cannot establish global negativity of the entire quadratic form.

Therefore:

[
\text{one negative zero contribution}
\not\Longrightarrow
\mathrm{RH}.
]

This shortcut is explicitly classified as non-proof-bearing.

## 6. Remaining proof programs

### A. Positive-kernel route

Construct an explicit positive-definite kernel (K_{\mathrm{MR}}(x,y)) such that

[
Q_{\mathrm{MR}}(f)
=
\iint
f(x)\overline{f(y)}
K_{\mathrm{MR}}(x,y)\,dx\,dy,
]

then prove (K_{\mathrm{MR}}\succeq0) independently and prove exact equality with (W_\xi).

### B. Spectral route

Construct a zero-independent self-adjoint operator (H_{\mathrm{MR}}) and establish a rigorous regularized determinant identity of the form

[
\det_{\mathrm{reg}}
\left(z-H_{\mathrm{MR}}\right)
=
C(z)\,
\xi\!\left(\frac12+iz\right),
\qquad
C(z)\ne0.
]

Self-adjointness alone is insufficient; the determinant and zero/spectrum correspondence must also be proved.

### C. Nyman–Beurling coercivity route

Map the MRDTS arithmetic data into the Nyman–Beurling framework and derive an unconditional coercive inequality. Exact mapping alone does not close the route because the density statement itself is RH-equivalent.

## 7. Closure matrix

| Gate | Status |
|---|---|
| Möbius reciprocal-zeta channel | EXACT |
| Prime-power logarithmic derivative | EXACT |
| Standard Gamma/pi completion | EXACT |
| MRDTS normalization to xi'/xi | IDENTITY-LEVEL CLOSED |
| Exact infinite-dimensional MRDTS → Weil equality | OPEN |
| Independent global MRDTS positivity | OPEN / DECISIVE |
| Li positivity | RH-equivalent / OPEN |
| Nyman–Beurling density | RH-equivalent / OPEN |
| Zero-independent self-adjoint operator | OPEN |
| Regularized determinant (C\xi) | OPEN |

## 8. Anti-circularity rule

A new numeral system does not alter the zero set of zeta. The construction becomes proof-bearing only if it creates a genuinely new analytic invariant—such as an independently positive kernel, coercive functional, self-adjoint operator, or exact determinant identity—whose connection to the Weil form is rigorously proved.

## 9. Current mathematical endpoint

The strongest remaining target is therefore

[
\boxed{
A_{\mathrm{MR}}\succeq0
\quad\text{and}\quad
Q_{\mathrm{MR}}=W_\xi.
}
]

If both statements are proved unconditionally and non-circularly, the classical Weil criterion supplies the final implication to RH.

Until then, this repository entry records an open research program rather than a claimed solution.
