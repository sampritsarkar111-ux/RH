# Riemann Hypothesis — Frontier 22: Structured Jensen Obstruction

Date: 2026-09-16

## 1. Critical correction to Frontiers 21–22

A previous statement claimed that because
\[
a_m=\frac{m!}{(2m)!}
\]
is a Pólya–Schur multiplier sequence, the finite polynomials
\[
G_{d,n}(Y)=\sum_{j=0}^d\binom dj a_{n+j}Y^j
\]
must be hyperbolic. That implication is **false**. Multiplier-sequence preservation applies to applying the diagonal multiplier to an already-real-rooted polynomial; it does not assert that every shifted binomial polynomial built from the multiplier sequence is itself real-rooted.

This correction is decisive and has been checked directly.

For \(d=3,n=0\),
\[
G_{3,0}(Y)=1+\frac32Y+\frac14Y^2+\frac1{60}Y^3.
\]
Its cubic discriminant is
\[
\operatorname{Disc}(G_{3,0})=-\frac{1809}{160000}<0,
\]
so it has exactly one real zero and one nonreal conjugate pair. Numerically,
\[
Y\approx-0.7574628319,
\qquad
Y\approx-7.1212685841\pm5.33847742499i.
\]
Therefore the pointwise-hyperbolicity premise in Frontier 21 fails already at \((d,n)=(3,0)\).

## 2. What remains exact

The coefficient factorization remains valid:
\[
J_{d,n}(X)
=C\int_0^\infty\Phi(t)t^{2n}G_{d,n}(Xt^2)\,dt,
\]
with
\[
G_{d,n}(Y)=\sum_{j=0}^d\binom dj\frac{(n+j)!}{(2n+2j)!}Y^j.
\]
This identity is exact and RH-independent.

However, neither \(G_{d,n}\) nor its positive scale mixture can be declared hyperbolic from Pólya–Schur theory.

## 3. Exact universal-operator obstruction remains valid

Even independently of the preceding correction, the scale-mixture operator
\[
\mathcal I_n[P](X)=\int_0^\infty\Phi(t)t^{2n}P(Xt^2)dt
\]
does not preserve arbitrary hyperbolicity. For
\[
P(Y)=(Y-1)^2,
\]
\[
\mathcal I_n[P](X)=m_2X^2-2m_1X+m_0,
\]
with discriminant
\[
4(m_1^2-m_0m_2)<0
\]
for a non-degenerate positive measure, by strict Cauchy–Schwarz.

## 4. Correct degree-2 statement

For the actual Riemann Jensen polynomial,
\[
J_{2,n}(X)=
M_n+\frac{M_{n+1}}{2n+1}X+
\frac{M_{n+2}}{2(2n+1)(2n+3)}X^2,
\]
and hyperbolicity is exactly
\[
\boxed{
M_{n+1}^2\ge
\frac{2n+1}{2n+3}M_nM_{n+2}.
}
\]

## 5. Correct degree-3 algebraic target

Let
\[
A=M_n,\quad B=M_{n+1},\quad C=M_{n+2},\quad D=M_{n+3}.
\]
Then
\[
J_{3,n}(X)=
A+\frac{3B}{2(2n+1)}X+
\frac{3C}{4(2n+1)(2n+3)}X^2+
\frac{D}{4(2n+1)(2n+3)(2n+5)}X^3.
\]
Its discriminant is
\[
\operatorname{Disc}(J_{3,n})
=-\frac{27}{64(2n+1)^4(2n+3)^3(2n+5)^2}Q_{3,n},
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
Thus degree-3 hyperbolicity requires
\[
\boxed{Q_{3,n}\le0.}
\]

## 6. New, sharper research target

The previous proposed proof route cannot work as stated. The correct next target is to derive the **actual Hermite/Jensen determinant hierarchy** directly from
\[
\gamma_m=C\frac{m!}{(2m)!}M_m
\]
and then use the explicit Riemann theta-kernel representation of \(M_m\).

The required work is:

1. derive exact Hermite matrices for \(J_{d,n}\);
2. express their minors as multilinear moment determinants;
3. apply Andréief/Cauchy–Binet only where the determinant structure actually permits it;
4. determine whether the resulting expressions have a nonnegative factorization that follows from the explicit theta kernel;
5. prove the all-degree statement without importing RH through an equivalent condition.

## 7. Status

This corrected Frontier 22 is **not a proof of RH**. It removes two invalid shortcuts:

- universal hyperbolicity preservation by the positive scale-mixture operator;
- the incorrect inference from Pólya–Schur multiplier status to hyperbolicity of the shifted binomial polynomials \(G_{d,n}\).

The RH remains open in the current research state. The Clay Mathematics Institute currently lists RH as an unsolved Millennium problem. The exact all-degree Jensen/Laguerre–Pólya closure remains the central unresolved target. 
