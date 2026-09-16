# Riemann Hypothesis — Frontier 21: Exact Jensen-Integral Factorisation Attempt (corrected)

Date: 2026-09-16

## 1. Objective

Continue from Frontier 20 by attacking the all-degree Jensen hyperbolicity statement directly.

Let
\[
\gamma_m=C\frac{m!}{(2m)!}M_m,
\qquad
M_m=\int_0^\infty \Phi(t)t^{2m}\,dt,
\]
with \(C>0\) irrelevant to zero locations, and define
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
The exact target is to prove \(J_{d,n}\) hyperbolic for every \(d,n\ge0\).

## 2. Exact integral representation

Because the sum is finite,
\[
\boxed{
J_{d,n}(X)
=C\int_0^\infty \Phi(t)t^{2n}G_{d,n}(Xt^2)\,dt,
}
\]
where
\[
G_{d,n}(Y)=\sum_{j=0}^d\binom dj\frac{(n+j)!}{(2n+2j)!}Y^j.
\]
This identity is exact and contains no RH assumption.

## 3. Important correction to the previous version

The sequence
\[
a_m=\frac{m!}{(2m)!}
\]
has a Pólya–Schur multiplier-sequence structure because its signed exponential generating function is \(\cos(\sqrt z)\). However, this **does not imply** that the shifted binomial polynomials
\[
G_{d,n}(Y)=\sum_{j=0}^d\binom dj a_{n+j}Y^j
\]
are real-rooted. Multiplier sequences preserve real-rootedness when applied diagonally to an already-real-rooted polynomial; they do not make arbitrary shifted binomial combinations real-rooted.

Indeed,
\[
G_{3,0}(Y)=1+\frac32Y+\frac14Y^2+\frac1{60}Y^3
\]
has discriminant
\[
-\frac{67}{1600}<0,
\]
so it has a nonreal conjugate pair. This directly invalidates the previous pointwise-hyperbolicity assertion.

## 4. Universal positive-mixture preservation is also impossible

Consider
\[
\mathcal I_n[P](X)=\int_0^\infty\Phi(t)t^{2n}P(Xt^2)dt.
\]
For the hyperbolic polynomial \(P(Y)=(Y-1)^2\), writing
\[
m_k=\int_0^\infty t^{2k}\Phi(t)t^{2n}dt,
\]
we obtain
\[
\mathcal I_n[P](X)=m_2X^2-2m_1X+m_0
\]
with discriminant
\[
4(m_1^2-m_0m_2)<0
\]
by strict Cauchy–Schwarz for the non-degenerate Riemann measure. Thus no theorem asserting arbitrary-polynomial hyperbolicity preservation by this operator can close RH.

## 5. Exact low-degree Jensen constraints

For \(d=2\),
\[
J_{2,n}(X)=M_n+\frac{M_{n+1}}{2n+1}X+\frac{M_{n+2}}{2(2n+1)(2n+3)}X^2,
\]
and hyperbolicity is exactly
\[
\boxed{
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
}
\]

For \(d=3\), with \(A=M_n,B=M_{n+1},C=M_{n+2},D=M_{n+3}\),
\[
J_{3,n}(X)=A+\frac{3B}{2(2n+1)}X+\frac{3C}{4(2n+1)(2n+3)}X^2+\frac{D}{4(2n+1)(2n+3)(2n+5)}X^3.
\]
Its discriminant equals
\[
-\frac{27Q_{3,n}}{64(2n+1)^4(2n+3)^3(2n+5)^2},
\]
where
\[
\begin{aligned}
Q_{3,n}={}&(32n^3+176n^2+312n+180)B^3D\\
&-(24n^3+156n^2+330n+225)B^2C^2\\
&+(32n^3+176n^2+280n+100)AC^3\\
&-(96n^3+432n^2+552n+180)ABCD\\
&+(32n^3+80n^2+56n+12)A^2D^2.
\end{aligned}
\]
Hence degree 3 requires \(Q_{3,n}\le0\).

## 6. Correct remaining route

The proof must now attack the actual Jensen family directly. The natural next step is to derive the Hermite matrices and higher discriminants in terms of the moments \(M_n\), then substitute the explicit Riemann theta-kernel representation and seek a non-circular determinant factorisation.

A Vandermonde-square or Andréief identity may be useful, but it must be derived from the actual determinant. It cannot be assumed merely because moment determinants often admit such formulas.

## 7. Status

This corrected frontier does not prove RH. It removes two invalid shortcuts and isolates the exact all-degree algebraic/analytic problem. The Clay Mathematics Institute currently lists RH as unsolved.
