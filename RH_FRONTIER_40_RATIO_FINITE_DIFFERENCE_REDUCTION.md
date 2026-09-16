# Frontier 40 — Exact ratio/finite-difference reduction of the cubic Hermite cone

Date: 2026-09-16

## 1. Objective

Frontier 37 reduced the third-Hermite obstruction to
\[
\widetilde Q_d=6(d-1)u^3-3(d-2)w^2-2(d-3)uz,
\qquad u=-v.
\]
The immediate target is to determine whether the required cone inequality can be proved from structural properties of the Riemann-xi coefficient sequence.

## 2. Exact consecutive-ratio coordinates

Let
\[
q_j=\gamma_{m+j},\qquad R_k=\frac{\gamma_{k+1}}{\gamma_k}.
\]
Then exactly
\[
r_1=R_m,\quad r_2=R_mR_{m+1},\quad
r_3=R_mR_{m+1}R_{m+2},\quad
r_4=R_mR_{m+1}R_{m+2}R_{m+3}.
\]
Define finite differences
\[
R=R_m,\qquad \delta_1=R_{m+1}-R_m,\quad
\delta_2=R_{m+2}-R_{m+1},\quad
\delta_3=R_{m+3}-R_{m+2}.
\]
Direct algebra gives the exact identities
\[
\boxed{v=R\delta_1,}
\]
\[
\boxed{w=R\left[-R\delta_1+R\delta_2+\delta_1^2+\delta_1\delta_2\right],}
\]
and
\[
\boxed{
\begin{aligned}
z=R[&R^2\delta_1-2R^2\delta_2+R^2\delta_3-R\delta_1^2+2R\delta_1\delta_3\\
&+R\delta_2^2+R\delta_2\delta_3+\delta_1^3+2\delta_1^2\delta_2+\delta_1^2\delta_3\\
&+\delta_1\delta_2^2+\delta_1\delta_2\delta_3].
\end{aligned}}
\]
No normalization ambiguity remains in these formulas.

## 3. Exact factorial-moment relation

From
\[
\gamma_m=8\frac{m!}{(2m)!}M_m,
\qquad M_m=\int_0^\infty\Phi(u)u^{2m}\,du,
\]
we obtain
\[
\boxed{
R_m=\frac{1}{2(2m+1)}\frac{M_{m+1}}{M_m}.
}
\]
Thus the problem is not ordinary moment log-convexity: the factorial factor forces a specific competition between the increasing raw-moment ratio \(M_{m+1}/M_m\) and the explicit denominator \(2(2m+1)\).

## 4. d=3 cone in ratio coordinates

Since \(u=-R\delta_1\), the necessary sign condition is
\[
\delta_1\le0
\]
when \(R>0\). The exact d=3 condition is
\[
4(-R\delta_1)^3\ge
R^2\left[-R\delta_1+R\delta_2+\delta_1^2+\delta_1\delta_2\right]^2.
\]
For \(R>0\), this can be written as
\[
\boxed{
4R(-\delta_1)^3
\ge
\left[R(\delta_2-\delta_1)+\delta_1(\delta_1+\delta_2)\right]^2.
}
\]
This is an exact, dimensionally reduced inequality involving only the first two ratio differences.

## 5. Important obstruction: generic positive measures do NOT prove the cone

The theta-moment representation has a positive kernel, but positivity alone is insufficient. An explicit finite positive atomic measure can produce a factorially weighted coefficient sequence for which
\[
4(-v)^3-w^2<0,
\]
and even \(v>0\), contradicting the required Riemann-xi sign cone.

Therefore no argument of the form “\(\Phi\ge0\) + Stieltjes moment inequalities” can close Frontier 40. A successful proof must use a genuinely Riemann-specific property of \(\Phi\), such as its explicit theta-series structure, a differential/functional equation, total positivity stronger than Stieltjes positivity, or another global xi-specific mechanism.

## 6. Refined closure target

A sufficient Riemann-specific theorem would be any uniform estimate implying
\[
4R(-\delta_1)^3\ge
\left[R(\delta_2-\delta_1)+\delta_1(\delta_1+\delta_2)\right]^2
\]
for every admissible \(m\), together with the corresponding \(d>3\) control of \(z\).

A stronger route would prove a structural inequality for the ratio sequence \(R_m\) that simultaneously controls \(\delta_1,\delta_2,\delta_3\) and implies all third-Hermite degrees.

## 7. Status

The ratio reduction is rigorous and removes the previous normalization ambiguity. The generic-moment route is rigorously ruled out by counterexample. The Riemann-specific ratio inequality remains unproved.

This frontier therefore advances the target but does **not** prove the Riemann Hypothesis.
