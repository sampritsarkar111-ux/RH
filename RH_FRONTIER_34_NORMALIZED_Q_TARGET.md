# Frontier 34 — normalized third-Hermite obstruction and sharpened theta target

Starting from Frontier 32, define the positive leading coefficient \(q_0=\gamma_{n+d}>0\) and normalized ratios
\[
r_1=\frac{q_1}{q_0},\quad r_2=\frac{q_2}{q_0},\quad r_3=\frac{q_3}{q_0},\quad r_4=\frac{q_4}{q_0}.
\]
Then the exact third-Hermite obstruction becomes
\[
\boxed{\mathcal Q_d=q_0^4\,\widetilde Q_d(r_1,r_2,r_3,r_4)}.
\]

The normalized polynomial is
\[
\begin{aligned}
\widetilde Q_d={}&
-4d r_1^3r_3+3d r_1^2r_2^2-2d r_1^2r_4+10d r_1r_2r_3-6d r_2^3\\
&+2d r_2r_4-3d r_3^2
+6r_1^2r_4-12r_1r_2r_3+6r_2^3-6r_2r_4+6r_3^2.
\end{aligned}
\]

Hence
\[
\boxed{
\Delta_3=
\frac{d^3(d-1)^2(d-2)}{12}\frac{\widetilde Q_d}{q_0^0}\,q_0^0
}
\]
with the equivalent and dimensionally cleaner form inherited directly from Frontier 32:
\[
\boxed{
\Delta_3=\frac{d^3(d-1)^2(d-2)}{12}\,\frac{\widetilde Q_d}{q_0^0}
}
\]
where the cancellation of powers of \(q_0\) follows because \(\mathcal Q_d\) is homogeneous of degree four. (The important point is the sign: \(\operatorname{sgn}\Delta_3=\operatorname{sgn}\widetilde Q_d\).)

More usefully, separate the \(d\)-dependence:
\[
\widetilde Q_d=dP_0-6H_0,
\]
where
\[
P_0=-4r_1^3r_3+3r_1^2r_2^2-2r_1^2r_4+10r_1r_2r_3-6r_2^3+2r_2r_4-3r_3^2,
\]
while
\[
H_0=r_2r_4-r_3^2-r_1^2r_4+2r_1r_2r_3-r_2^3
=\frac{H_3(q)}{q_0^3}.
\]
Thus the exact sign condition is
\[
\boxed{dP_0\ge6H_0.}
\]

## New target

The next closure problem is no longer an undifferentiated polynomial-positivity question. It is the Riemann-specific inequality
\[
\boxed{dP_0(r_1,r_2,r_3,r_4)\ge6H_0(r_1,r_2,r_3,r_4)}
\]
for the consecutive ratios of the Riemann-xi coefficients.

The Frontier 33 exact counterexample shows that generic Stieltjes moment positivity cannot imply this inequality: a positive two-atom measure, after applying the same \(m!/(2m)!\) multiplier, produces \(\mathcal Q_3<0\).

Therefore the next serious attack should derive \(P_0\) directly from the specific Riemann theta kernel, seeking an explicit positive integral/SOS representation or a stronger kernel inequality. Any proof must be uniform in \(n,d\), not finite-degree or numerical.

## Important correction

The normalized formula above preserves sign only; when substituting \(\mathcal Q_d=q_0^4\widetilde Q_d\) into Frontier 32's prefactor, one gets
\[
\Delta_3=\frac{d^3(d-1)^2(d-2)}{12}\frac{\widetilde Q_d}{q_0^0},
\]
i.e. the \(q_0^4\) cancels exactly. This is why \(\widetilde Q_d\) is the clean dimensionless target.

## Status

Partial: exact normalization and target reformulation. No positivity proof and no RH proof has been obtained.
