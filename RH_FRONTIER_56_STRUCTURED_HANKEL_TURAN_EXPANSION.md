# Frontier 56 — structured Hankel expansion of the factorial-corrected Turan gate

Let
\[
\mu_j=\int_0^\infty y^j\,d\sigma(y),\qquad
M_m=16m(2m-1)\mu_{m-1}-\mu_m.
\]
The exact adjacent Turan gate is
\[
(m+1)(2m+1)M_{m+1}^2-(m+2)(2m+3)M_mM_{m+2}\ge0.
\]

Substitution gives the exact four-moment polynomial
\[
\boxed{
\begin{aligned}
\mathcal T_m={}&A_m\mu_{m-1}\mu_{m+2}
+B_m\mu_m^2
+C_m\mu_m\mu_{m+1}
+D_m\mu_{m+1}^2,
\end{aligned}}
\]
where
\[
A_m=-(m+2)(2m+3)\,16m(2m-1),
\]
\[
B_m=(m+1)(2m+1)[16(m+1)(2m+1)]^2,
\]
\[
C_m=-2(m+1)(2m+1)16(m+1)(2m+1),
\]
plus the corresponding mixed terms from \(- (m+2)(2m+3)M_mM_{m+2}\). A fully expanded symbolic form is stored below as the coefficient identity.

## Exact expanded identity

Writing \(u_0=\mu_{m-1},u_1=\mu_m,u_2=\mu_{m+1},u_3=\mu_{m+2}\), symbolic expansion gives
\[
\begin{aligned}
\mathcal T_m={}&
(2048m^6+9216m^5+16896m^4+16128m^3+8448m^2+2304m+256)u_1^2\\
&+(2m^2+3m+1)u_2^2\\
&+(-2048m^6-13312m^5-30208m^4-24320m^3+3072m^2+9216m)u_0u_2\\
&+(64m^4+192m^3+80m^2-96m)u_0u_3\\
&+(-64m^4+64m^3+752m^2+1152m+544)u_1u_2\\
&+(-2m^2-7m-6)u_1u_3.
\end{aligned}
\]

This form is useful because every term involves only four consecutive Stieltjes moments. It also makes clear why ordinary Hankel positivity alone is insufficient: several coefficients are negative.

## New reduction target

For a positive Stieltjes measure, the moment sequence is log-convex and its Hankel matrices are positive semidefinite. The exact question is whether those universal Hankel inequalities, augmented by the special theta-measure structure, can dominate the negative mixed terms above.

A promising normalization is to define
\[
r_j=\frac{\mu_{j+1}\mu_{j-1}}{\mu_j^2}\ge1,
\qquad
s_j=\frac{\mu_{j+2}\mu_{j-1}}{\mu_{j+1}\mu_j},
\]
and rewrite \(\mathcal T_m/\mu_m^2\) entirely in terms of adjacent moment ratios. This reduces the infinite-dimensional measure problem to a finite-dimensional feasibility region constrained by total positivity of the Hankel matrix.

## Adversarial guardrail

No claim is made that the universal Stieltjes inequalities alone imply \(\mathcal T_m\ge0\). They need to be tested against realizable moment sequences. If a realizable positive measure violates the target, the proof must use an additional property of the Riemann theta measure.

## Status

**Exact reduction closed.**

**Open:** characterize the feasible ratio region for the specific theta measure and prove the factorial-corrected Turan inequality, or find a rigorous counterexample to this route. No RH conclusion follows yet.