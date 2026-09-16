# Frontier 32 — Quartic normalization correction and exact third-Hermite obstruction

## Purpose

This frontier corrects an algebraic normalization error in Frontier 24 that propagated into the quartic part of Frontier 31. The correction is essential before attempting any positivity proof.

We keep the displayed quartic Jensen polynomial

\[
J_{4,n}(X)=
A+\frac{2B}{2n+1}X
+\frac{3C}{2(2n+1)(2n+3)}X^2
+\frac{D}{2(2n+1)(2n+3)(2n+5)}X^3
+\frac{E}{4(2n+1)(2n+3)(2n+5)(2n+7)}X^4,
\]
where
\[
A=M_n,\quad B=M_{n+1},\quad C=M_{n+2},\quad D=M_{n+3},\quad E=M_{n+4}.
\]

## 1. Correct monic normalization

The leading coefficient is
\[
a_4=\frac{E}{4(2n+1)(2n+3)(2n+5)(2n+7)}.
\]
Dividing every coefficient by \(a_4\) gives
\[
p(X)=X^4+c_3X^3+c_2X^2+c_1X+c_0,
\]
with the exact coefficients
\[
\boxed{c_3=2(2n+7)\frac{D}{E}},
\]
\[
\boxed{c_2=6(2n+5)(2n+7)\frac{C}{E}},
\]
\[
\boxed{c_1=8(2n+3)(2n+5)(2n+7)\frac{B}{E}},
\]
\[
\boxed{c_0=4(2n+1)(2n+3)(2n+5)(2n+7)\frac{A}{E}}.
\]

These follow by direct coefficient division. In particular, the earlier formulas in Frontier 24 containing factors \(8,24(2n+6),32,16\) are inconsistent with the displayed \(J_{4,n}\).

## 2. Correct second Hermite minor

For a monic quartic
\[
p(X)=X^4+c_3X^3+c_2X^2+c_1X+c_0,
\]
the leading second Hermite minor is
\[
\Delta_2=3c_3^2-8c_2.
\]
Substitution of the corrected monic coefficients yields
\[
\boxed{
\Delta_2=
\frac{12(2n+7)}{E^2}
\left((2n+7)D^2-4(2n+5)CE\right).
}
\]
Hence the exact quartic necessary condition is
\[
\boxed{(2n+7)D^2\ge 4(2n+5)CE.}
\]
This agrees with the universal adjacent-Turán form after translating \(\gamma_m=C_0\,m!M_m/(2m)!\).

## 3. Exact universal third Hermite minor

For a general monic degree-\(d\) polynomial
\[
P(x)=x^d+b_1x^{d-1}+b_2x^{d-2}+b_3x^{d-3}+b_4x^{d-4}+\cdots,
\]
Newton identities give
\[
\begin{aligned}
\Delta_3={}&-2db_1^3b_3+2b_1^3b_3
+d b_1^2b_2^2-2b_1^2b_2^2
-4db_1^2b_4+4b_1^2b_4\\
&+10db_1b_2b_3-12b_1b_2b_3
-4db_2^3+8b_2^3
+8db_2b_4-9db_3^2.
\end{aligned}
\]

For the monic Jensen polynomial, put
\[
q_0=\gamma_{n+d},\quad q_1=\gamma_{n+d-1},\quad q_2=\gamma_{n+d-2},\quad q_3=\gamma_{n+d-3},\quad q_4=\gamma_{n+d-4}.
\]
Then
\[
b_k={d\choose k}\frac{q_k}{q_0},\qquad k=1,2,3,4,
\]
and exact simplification gives
\[
\boxed{
\Delta_3=
\frac{d^3(d-1)^2(d-2)}{12q_0^4}\,\mathcal Q_d(q_0,q_1,q_2,q_3,q_4),
}
\]
where
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

A useful structural decomposition is obtained from the Hankel determinant
\[
H_3(q)=
\det\!\begin{pmatrix}
q_0&q_1&q_2\\
q_1&q_2&q_3\\
q_2&q_3&q_4
\end{pmatrix}
=q_0q_2q_4-q_0q_3^2-q_1^2q_4+2q_1q_2q_3-q_2^3.
\]
The entire \(d\)-independent part of \(\mathcal Q_d\) is exactly
\[
\boxed{-6q_0H_3(q).}
\]
Thus ordinary Hankel positivity alone cannot prove \(\Delta_3\ge0\): its contribution enters with the opposite sign and must be compensated by the genuinely Jensen-specific \(d\)-dependent terms.

## 4. Quartic specialization in consecutive xi coefficients

For \(d=4\), with
\[
g_j=\gamma_{n+j},
\]
so \(q_0=g_4,q_1=g_3,q_2=g_2,q_3=g_1,q_4=g_0\),
\[
\boxed{
\Delta_3=
\frac{192}{g_4^4}
\Big(
 g_4^2g_2g_0
-3g_4^2g_1^2
-g_4g_3^2g_0
+14g_4g_3g_2g_1
-9g_4g_2^3
-8g_3^3g_1
+6g_3^2g_2^2
\Big).
}
\]
This is the first corrected four/five-consecutive-coefficient obstruction beyond adjacent Turán positivity.

## 5. Consequence for the proof program

The next closure target is now precise: prove \(\mathcal Q_d\ge0\) for the Riemann-xi coefficient sequence for every \(d\ge3\) and every shift \(n\), and then continue to all higher Hermite minors. A generic moment-Hankel argument cannot suffice because \(-6q_0H_3(q)\) appears inside the exact expression.

A potentially viable route must exploit the specific factorially weighted theta moments in
\[
\gamma_m=C_0\frac{m!}{(2m)!}M_m,
\]
not merely positivity of \(M_m\).

## Status

**Rigorous correction and stronger reduction, not a proof of RH.** The quartic normalization has been repaired, the correct \(\Delta_2\) obtained, and the all-degree \(3\times3\) Hermite obstruction has been reduced to one explicit polynomial \(\mathcal Q_d\). The remaining problem is to prove its nonnegativity for the Riemann-xi sequence uniformly in \((d,n)\), followed by the higher Hermite minors.