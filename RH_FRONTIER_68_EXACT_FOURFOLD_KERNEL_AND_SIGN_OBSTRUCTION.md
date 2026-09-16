# Frontier 68 — exact fourfold theta kernel and sign obstruction

## Objective

Push the cubic target one level deeper: substitute the exact theta-moment representation into the cubic discriminant numerator and determine whether the resulting fourfold kernel can itself be made sign-definite by permutation symmetrization.

From the established coefficient representation,
\[
q_k=8\frac{k!}{(2k)!}M_k,
\qquad
M_k=\int_0^\infty \Phi(u)u^{2k}\,du,
\]
write
\[
c_k=\frac{k!}{(2k)!},\qquad y=u^2.
\]
The common factor 8 is irrelevant for the sign of the homogeneous quartic expression.

## 1. Exact symmetrized fourfold kernel

For
\[
B_n=q_n^2q_{n+3}^2-6q_nq_{n+1}q_{n+2}q_{n+3}
+4q_nq_{n+2}^3+4q_{n+1}^3q_{n+3}-3q_{n+1}^2q_{n+2}^2,
\]
let \(\operatorname{Sym}(y^\alpha)\) denote the average over all distinct permutations of the exponent vector \(\alpha\). After expanding each product into four independent integrals and using symmetry of the product measure, the exact representation is
\[
B_n=8^4c_n^4\int_{(0,\infty)^4}\Phi(u_1)\cdots\Phi(u_4)
\prod_{i=1}^4y_i^n\,K_n(y_1,y_2,y_3,y_4)\,du_1\cdots du_4,
\]
where
\[
\begin{aligned}
K_n={}&r_3^2\operatorname{Sym}(y^{(0,0,3,3)})
-6r_1r_2r_3\operatorname{Sym}(y^{(0,1,2,3)})\\
&+4r_2^3\operatorname{Sym}(y^{(0,2,2,2)})
+4r_1^3r_3\operatorname{Sym}(y^{(1,1,1,3)})\\
&-3r_1^2r_2^2\operatorname{Sym}(y^{(1,1,2,2)}),
\end{aligned}
\]
with
\[
 r_j=\frac{c_{n+j}}{c_n}.
\]
Explicitly,
\[
 r_1=\frac1{2(2n+1)},\quad
 r_2=\frac1{4(2n+1)(2n+3)},\quad
 r_3=\frac1{8(2n+1)(2n+3)(2n+5)}.
\]
This is an exact algebraic reduction; no RH input is used.

## 2. Adversarial sign test

The symmetrized kernel is **not** pointwise nonnegative and is **not** pointwise nonpositive. Direct evaluation at positive \(y_i\) gives both signs. For example, numerical evaluations of the exact polynomial give values of both signs already for \(n=0,1,2\) (and still for large \(n\)). Therefore the naive certificate
\[
K_n(y_1,y_2,y_3,y_4)\ge0
\quad\text{or}\quad
K_n(y_1,y_2,y_3,y_4)\le0
\]
cannot be the missing theorem.

This is a stronger obstruction than merely observing that a generic moment inequality fails: even after the exact factorial normalization and full S_4 symmetrization, the most direct fourfold integrand is sign-indefinite.

## 3. Consequence for the proof search

A valid theta proof of the cubic gate must therefore use additional structure beyond pointwise positivity of the original theta kernel. Plausible surviving mechanisms are:

1. **nonlocal positivity:** the integral of the sign-indefinite kernel is controlled by a positive quadratic/SOS form;
2. **modular pairing:** pair \(u\) with the modularly transformed variable before symmetrization, producing cancellations not visible pointwise;
3. **divided-difference structure:** rewrite the signed kernel as a sum of divided differences whose integral is positive even though the raw kernel changes sign;
4. **shift propagation:** derive an exact recurrence for \(B_n\), \(v_n\), or \(w_n\) whose remainder has a theta-derived sign;
5. **higher-order determinant route:** bypass the cubic kernel and establish a direct all-degree Hermite/Jensen positivity theorem.

## 4. Important logical correction

The sign-indefiniteness of \(K_n\) does **not** show that the cubic inequality fails. It only rules out this particular pointwise-kernel certificate. The actual target remains
\[
B_n\le0
\quad\Longleftrightarrow\quad
\Delta_3(J^{3,n})\ge0
\quad\Longleftrightarrow\quad
w_n^2+4v_n^3\le0.
\]

## 5. Strongest next target

The next attack should not search for an arbitrary positive factorization. It should search for an **exact modular-paired identity** for \(B_n\), ideally of the form
\[
B_n= -\int\!\int\!\int\!\int
\mathcal S_n(u_1,u_2,u_3,u_4)^2\,d\mu_n
+\mathcal R_n,
\]
where \(\mathcal R_n\) has an independently provable sign, or an exact shift identity
\[
B_{n+1}-\Lambda_nB_n=R_n
\]
with explicit \(\Lambda_n\) and theta-derived sign control.

Neither identity has yet been proved. They are research targets, not assumptions.

## Status

**Rigorous partial progress.** The fourfold reduction is exact, and the direct pointwise-sign certificate has been adversarially eliminated. RH remains unproved.
