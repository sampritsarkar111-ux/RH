# Frontier 123 — Factorial Shape Region: exact corrected cubic Jensen gate

Date: 2026-09-17

## Executive result

A normalization audit of the latest degree-3 calculation finds a decisive correction.

For
\[
g(z)=\Xi(\sqrt{-z})=\sum_{k\ge0}\gamma_k z^k,
\qquad
\gamma_k=\frac{M_k}{(2k)!},
\qquad
M_k=\int_0^\infty u^{2k}\Phi(u)\,du,
\]
the standard Jensen polynomial is
\[
J_{n,3}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3.
\]
The raw moments \(M_k\) themselves are **not** the Jensen coefficients. Omitting the factorials changes the polynomial and destroys the RH equivalence.

This note derives the exact factorial-corrected cubic hyperbolicity region in only two dimensionless variables.

---

## 1. Audit of the raw-moment cubic

Suppose incorrectly one defines
\[
\widetilde J_{n,3}(X)=M_n+3M_{n+1}X+3M_{n+2}X^2+M_{n+3}X^3.
\]
Normalize by the probability measure
\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},\qquad Y=u^2,
\]
and write
\[
m_j=\mathbb E_{\nu_n}[Y^j].
\]
Then \(M_{n+j}=M_n m_j\), and the cubic discriminant is
\[
\operatorname{Disc}(\widetilde J_{n,3})
=27M_n^4\left(6m_1m_2m_3-4m_2^3+3m_1^2m_2^2-4m_1^3m_3-m_3^2\right).
\]
Writing
\[
v=m_2-m_1^2,\qquad \mu_3=m_3-3m_1m_2+2m_1^3,
\]
a direct exact expansion gives
\[
\boxed{
6m_1m_2m_3-4m_2^3+3m_1^2m_2^2-4m_1^3m_3-m_3^2
=-\mu_3^2-4v^3.
}
\]
Hence
\[
\boxed{
\operatorname{Disc}(\widetilde J_{n,3})
=-27M_n^4\left(\mu_3^2+4v^3\right)\le0.
}
\]
For a non-degenerate positive measure this is strictly negative. Therefore the raw-moment cubic is generically non-hyperbolic. This proves that the factorial normalization cannot be discarded.

---

## 2. Correct factorially normalized ratios

Set
\[
q_1:=\frac{\gamma_{n+1}}{\gamma_n},\qquad
q_2:=\frac{\gamma_{n+2}}{\gamma_n},\qquad
q_3:=\frac{\gamma_{n+3}}{\gamma_n}.
\]
Then
\[
J_{n,3}(X)=\gamma_n\left(1+3q_1X+3q_2X^2+q_3X^3\right).
\]
Its exact discriminant is
\[
\boxed{
\Delta_{n,3}
=27\gamma_n^4
\left(6q_1q_2q_3-4q_2^3+3q_1^2q_2^2-4q_1^3q_3-q_3^2\right).
}
\]

Now introduce the dimensionless **factorial shape coordinates**
\[
\boxed{
P_n:=\frac{q_2}{q_1^2},\qquad
Q_n:=\frac{q_3}{q_1^3}.
}
\]
Because \(q_1>0\),
\[
\boxed{
\Delta_{n,3}=27\gamma_n^4q_1^6\,\mathcal F(P_n,Q_n),
}
\]
where the new universal cubic shape function is
\[
\boxed{
\mathcal F(P,Q)
=-Q^2+(6P-4)Q+3P^2-4P^3.
}
\]

This separates all scale dependence from the genuinely hyperbolic shape information.

---

## 3. Exact Factorial Shape Region

Treat \(\mathcal F(P,Q)\) as a quadratic in \(Q\). Its discriminant is
\[
\boxed{
(6P-4)^2+4(3P^2-4P^3)=16(1-P)^3.
}
\]
Therefore \(\mathcal F(P,Q)\ge0\) is possible exactly when \(P\le1\), and then
\[
\boxed{
3P-2-2(1-P)^{3/2}
\le Q\le
3P-2+2(1-P)^{3/2}.
}
\]
Thus the complete degree-3 Jensen gate is the two-dimensional region
\[
\boxed{
\mathscr R_3=
\left\{(P,Q):
P\le1,\ 
|Q-(3P-2)|\le2(1-P)^{3/2}
\right\}.
}
\]
Call this the **Factorial Shape Region (FSR)**.

For positive coefficients, \(\Delta_{n,3}\ge0\) is precisely the cubic real-rootedness gate (with equality allowing multiplicity). Hence
\[
\boxed{
J_{n,3}\text{ is hyperbolic}
\iff
(P_n,Q_n)\in\mathscr R_3.
}
\]

---

## 4. Express the FSR directly in theta moments

Let
\[
A_n=(2n+1)(2n+2),
\quad
B_n=(2n+3)(2n+4),
\quad
C_n=(2n+5)(2n+6).
\]
Under \(\nu_n\), let
\[
m_j=\mathbb E_{\nu_n}[Y^j].
\]
Since
\[
\frac{\gamma_{n+j}}{\gamma_n}
=\frac{(2n)!}{(2n+2j)!}\,m_j,
\]
we obtain
\[
\boxed{
P_n=\frac{A_n}{B_n}\frac{m_2}{m_1^2},
\qquad
Q_n=\frac{A_n^2}{B_nC_n}\frac{m_3}{m_1^3}.
}
\]
Therefore degree three is reduced exactly to proving
\[
\boxed{
\frac{A_n}{B_n}\frac{m_2}{m_1^2}\le1
}
\]
and
\[
\boxed{
\left|
\frac{A_n^2}{B_nC_n}\frac{m_3}{m_1^3}
-3\frac{A_n}{B_n}\frac{m_2}{m_1^2}+2
\right|
\le
2\left(
1-\frac{A_n}{B_n}\frac{m_2}{m_1^2}
\right)^{3/2}.
}
\]
The first inequality is exactly the factorial-corrected degree-2 Jensen/Turán gate. The second is the new sharp third-order constraint.

---

## 5. New framework: factorial cumulant-shape hierarchy

The FSR suggests an all-degree replacement for raw moment positivity.

Define normalized coefficient shapes
\[
R_{n,j}:=\frac{\gamma_{n+j}/\gamma_n}{(\gamma_{n+1}/\gamma_n)^j},\qquad j\ge2.
\]
Thus \(R_{n,2}=P_n\) and \(R_{n,3}=Q_n\).

For each degree \(d\), divide the Jensen polynomial by \(\gamma_n\) and rescale \(X\mapsto X/q_1\). This gives the scale-free polynomial
\[
\boxed{
\mathcal J_{n,d}(X)
=1+dX+\binom d2 R_{n,2}X^2+\cdots+R_{n,d}X^d.
}
\]
Hence every degree-\(d\) hyperbolicity condition is a semialgebraic constraint only on
\[
(R_{n,2},\ldots,R_{n,d}).
\]
Define the **degree-\(d\) Factorial Shape Region**
\[
\boxed{
\mathscr R_d:=
\left\{(R_2,\ldots,R_d):
1+dX+\sum_{j=2}^d\binom djR_jX^j
\text{ has only real zeros}
\right\}.
}
\]
Then
\[
\boxed{
\text{RH}
\iff
(R_{n,2},\ldots,R_{n,d})\in\mathscr R_d
\quad\text{for every }n\ge0,d\ge1.
}
\]
This is an exact reformulation, not a proof.

The advantage is that all irrelevant scale has been removed and the factorial correction is built into the coordinates from the beginning. The degree-3 boundary is now explicit and surprisingly simple.

---

## 6. Relation to the four-copy symmetrized kernel

For the raw-moment cubic integrand from the previous note, full permutation symmetrization factors exactly as
\[
\operatorname{Sym}_4Q
=-54L_1L_2L_3,
\]
where
\[
L_1=x_1x_2-2x_1x_3+x_1x_4+x_2x_3-2x_2x_4+x_3x_4,
\]
\[
L_2=x_1x_2+x_1x_3-2x_1x_4-2x_2x_3+x_2x_4+x_3x_4,
\]
\[
L_3=2x_1x_2-x_1x_3-x_1x_4-x_2x_3-x_2x_4+2x_3x_4.
\]
This product changes sign on the positive orthant. Thus even after full \(S_4\)-symmetrization there is no universal pointwise nonnegative certificate for the raw-moment object.

The factorially corrected FSR shows why the next mechanism must act on the **factorial transform of the moments**, not merely on positivity of the underlying theta measure.

---

## 7. Next proof-bearing target

The sharp next theorem is now:

> For the completed Riemann theta measure and every \(n\ge0\), prove the exact FSR inequalities for \((P_n,Q_n)\) directly from the unsummed theta/Jacobi structure; then identify the degree-uniform extension showing \((R_{n,2},\ldots,R_{n,d})\in\mathscr R_d\) for every \(d\).

A promising operator to study is the factorial transform
\[
\mathcal T_n[m_j]
=\frac{(2n)!}{(2n+2j)!}m_j,
\]
because ordinary Stieltjes moment positivity fails at degree three whereas the transformed sequence is exactly the RH-relevant coefficient sequence.

The central unresolved problem is therefore no longer "find a Vandermonde square for raw moments"; it is:
\[
\boxed{
\text{prove that the Riemann-theta moment sequence enters every factorial shape region after }\mathcal T_n.
}
\]

## Status

This frontier makes a rigorous normalization correction, closes the raw-moment cubic route, derives an exact new two-parameter hyperbolicity region for degree three, and gives a scale-free all-degree reformulation. It does **not** prove RH; the remaining infinite-degree theta-specific inclusion theorem is open.
