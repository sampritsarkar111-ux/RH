# Frontier 34 — normalized third-Hermite obstruction and sharpened theta target

Starting from Frontier 32, define
\[
r_j=\frac{q_j}{q_0},\qquad j=1,2,3,4,
\]
with \(q_0=\gamma_{n+d}>0\). Since \(\mathcal Q_d\) is homogeneous of degree four,
\[
\boxed{\mathcal Q_d=q_0^4\widetilde Q_d(r_1,r_2,r_3,r_4)}.
\]

The exact normalized polynomial is
\[
\begin{aligned}
\widetilde Q_d={}&
-4d r_1^3r_3+3d r_1^2r_2^2-2d r_1^2r_4+10d r_1r_2r_3-6d r_2^3\\
&+2d r_2r_4-3d r_3^2
+6r_1^2r_4-12r_1r_2r_3+6r_2^3-6r_2r_4+6r_3^2.
\end{aligned}
\]

Therefore the exact Hermite minor from Frontier 32 simplifies to
\[
\boxed{
\Delta_3=\frac{d^3(d-1)^2(d-2)}{12}\,\widetilde Q_d.
}
\]
Thus, for \(d\ge3\), \(\Delta_3\ge0\) is equivalent to \(\widetilde Q_d\ge0\).

## 1. Structural decomposition

Define
\[
P_0=-4r_1^3r_3+3r_1^2r_2^2-2r_1^2r_4+10r_1r_2r_3-6r_2^3+2r_2r_4-3r_3^2,
\]
and
\[
H_0=r_2r_4-r_3^2-r_1^2r_4+2r_1r_2r_3-r_2^3.
\]
Then
\[
\boxed{\widetilde Q_d=dP_0-6H_0},
\]
where \(H_0=H_3(q)/q_0^3\). Hence the exact closure inequality is
\[
\boxed{dP_0\ge6H_0.}
\]

## 2. Why generic moment positivity is insufficient

Frontier 33 gives an exact counterexample: the positive two-atom Stieltjes measure
\[
\mu=14\,\delta_{10}+\delta_{40}
\]
with moments \(M_m=14\,10^m+40^m\), followed by the same positive factorial weighting \(\gamma_m=m!M_m/(2m)!\), has \(\mathcal Q_3<0\) at \(n=2\). Thus the desired inequality is not a consequence of Stieltjes moment positivity plus the factorial multiplier alone.

## 3. Sharpened Riemann-specific target

The next genuine proof target is therefore:
\[
\boxed{
\text{derive }dP_0-6H_0\ge0\text{ directly from the exact Riemann theta kernel, uniformly in }n,d.
}
\]

Possible mechanisms include an explicit positive-kernel/SOS representation, a stronger total-positivity property of the factorially weighted theta moments, or an all-degree hyperbolicity argument that bypasses separate Hermite minors.

The target must not assume RH, Jensen hyperbolicity, LP status, or a finite-degree numerical check.

## Status

**Partial, rigorous reduction.** This frontier gives a dimensionless exact target and records the generic-moment obstruction. It is not a proof of RH.
