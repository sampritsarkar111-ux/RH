# Frontier 33 — factorially weighted moment-cone obstruction for the third Hermite minor

## Objective

The corrected Frontier 32 reduced the leading 3x3 Hermite minor to
\[
\Delta_3=\frac{d^3(d-1)^2(d-2)}{12q_0^4}\,\mathcal Q_d(q_0,q_1,q_2,q_3,q_4),
\]
with an explicit quartic polynomial \(\mathcal Q_d\). The next question is whether positivity of the underlying theta moments, even together with the factorial multiplier
\[
\gamma_m=C_0\frac{m!}{(2m)!}M_m,
\]
can force \(\mathcal Q_d\ge0\).

This frontier gives an exact negative answer for the full positive-moment cone: positivity of \(M_m\) as a Stieltjes moment sequence is not sufficient. Therefore the eventual RH proof must use additional structure of the specific Riemann theta kernel.

## 1. Exact obstruction polynomial

Write
\[
\begin{aligned}
\mathcal Q_d={}&
2d q_0^2q_2q_4-3d q_0^2q_3^2-2d q_0q_1^2q_4
+10d q_0q_1q_2q_3-6d q_0q_2^3\\
&-4d q_1^3q_3+3d q_1^2q_2^2
-6q_0^2q_2q_4+6q_0^2q_3^2+6q_0q_1^2q_4\\
&-12q_0q_1q_2q_3+6q_0q_2^3.
\end{aligned}
\]

For \(d=3\), the prefactor in \(\Delta_3\) is positive whenever \(q_0>0\), so the sign of \(\Delta_3\) is exactly the sign of \(\mathcal Q_3\).

## 2. Counterexample inside the positive moment cone

Take the positive two-atom measure
\[
\mu=14\,\delta_{10}+\delta_{40}.
\]
Its moments are
\[
M_m=14\,10^m+40^m>0,
\]
and it is a genuine Stieltjes moment sequence.

Use the same factorial multiplier appearing in the Riemann-xi relation,
\[
\gamma_m=\frac{m!}{(2m)!}M_m,
\]
(the global constant \(C_0>0\) cancels from the sign of \(\mathcal Q_d\)).

For \(d=3\) and shift \(n=2\), the five coefficients are
\[
(q_0,q_1,q_2,q_3,q_4)
=(\gamma_5,\gamma_4,\gamma_3,\gamma_2,\gamma_1).
\]
Direct exact rational evaluation gives
\[
\boxed{
\mathcal Q_3
=-\frac{156685000000000}{9261}<0.
}
\]
Consequently
\[
\boxed{\Delta_3<0}
\]
for this positive-moment example.

No floating-point approximation is used in this sign certificate.

## 3. Interpretation

This rules out the following proposed closure principle:

> “Because \(M_m\) are positive Stieltjes moments, and \(\gamma_m\) differs from \(M_m\) only by the positive factor \(m!/(2m)!\), all higher Jensen Hermite minors should follow from generic moment positivity.”

That implication is false already at the leading 3x3 Hermite minor.

This is stronger than the observation in Frontier 32 that the \(d\)-independent part contains \(-6q_0H_3\). The factorial weighting does not rescue positivity on the entire positive-moment cone.

## 4. What additional structure is required

The Riemann problem therefore cannot be closed by an abstract Stieltjes-moment theorem alone. A successful proof must exploit at least one genuinely Riemann-specific property, for example:

1. the exact theta kernel \(\Phi\), including its special functional form;
2. the precise dependence of the moments \(M_n\) on the shift \(n\);
3. a stronger total-positivity / variation-diminishing property tailored to the factorially weighted sequence;
4. an explicit sum-of-squares or positive-kernel representation of \(\mathcal Q_d\) for the Riemann moments;
5. or a different all-degree hyperbolicity mechanism that bypasses individual Hermite minors.

## 5. New closure target

The next mathematical target is therefore sharpened to:

\[
\boxed{
\text{Determine the exact additional theta-kernel inequality that forces }
\mathcal Q_d\ge0
\text{ for every }d,n.
}
\]

A useful intermediate target is to rewrite \(\mathcal Q_d\) in normalized moment ratios and isolate the smallest Riemann-specific inequality that is not implied by generic Stieltjes positivity.

## Status

**Rigorous obstruction / partial progress.** We have proved by an exact rational counterexample that even factorially weighted positive Stieltjes moments do not guarantee the required third Hermite minor. This eliminates a broad generic-moment closure route. It does not disprove RH and does not constitute a proof of RH.
