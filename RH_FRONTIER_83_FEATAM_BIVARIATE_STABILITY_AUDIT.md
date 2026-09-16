# Frontier 83 — Audit of the 2026 FEATAM/Jensen–Pólya claimed proof

Date: 2026-09-16

## 1. Trigger

A 2026 aiXiv preprint, *A Jensen–Pólya and Bivariate Stability Approach to the Riemann Hypothesis*, claims a complete RH proof. Its central route is:
\[
K_D\text{ hyperbolic}
\to H_u(X,Y)\text{ bivariate stable}
\to H_D(X,Y)=\int H_u(X,Y)\,d\mu(u)\text{ bivariate stable}
\to P_D\text{ hyperbolic}\to G\in LP^-\to RH.
\]
The preprint explicitly identifies its integration step as an application of a claimed continuous-integration form of a Wagner stability theorem.

## 2. What is correct

The following ingredients are individually valid or at least standard and independently checkable:

- the classical positive Xi-kernel representation;
- positivity of the displayed kernel for \(u\ge0\);
- the multiplier sequence \(c_j=j!/(2j)!\), whose exponential symbol is \(\cosh\sqrt z\);
- hyperbolicity of
\[
K_D(t)=\sum_{j=0}^D\binom Dj\frac{j!}{(2j)!}t^j;
\]
- the homogenization
\[
H_u(X,Y)=Y^DK_D(u^2X/Y)
=c_Du^{2D}\prod_i(X+\sigma_i u^{-2}Y),
\]
so each fixed-\(u\) polynomial is bivariate stable;
- the finite-moment estimates are sufficient for integrability if the preceding stability-preservation theorem were available.

These facts match the structural direction developed in Frontier 82.

## 3. Critical gap in the claimed proof

The decisive assertion is that a positive-measure integral of the family \(H_u\) remains bivariate stable merely because each \(H_u\) is bivariate stable and the coefficient functions are integrable.

The cited Wagner 2011 survey *Multivariate stable polynomials: theory and applications* (arXiv:0911.3569, Bull. AMS 48 (2011), 53–84) does not contain the cited continuous-integration theorem numbered "Theorem 4.14 / Corollary 4.15". Its Section 4 consists of the Grace–Walsh–Szegő coincidence theorem and subsections 4.1–4.3; its stability-preserver results are in Section 5. A search of the source does not produce the claimed continuous positive-measure integration statement.

Thus the preprint's main external theorem is not verified by the source it cites.

## 4. The naive integration principle is false in general

Positive linear combinations of stable polynomials need not be stable.

Take two bivariate homogeneous stable polynomials
\[
f_1(X,Y)=(X+Y)^2,
\qquad
f_2(X,Y)=(X+3Y)^2.
\]
Each factor is stable because \(X+\alpha Y\neq0\) whenever \(\Im X>0\), \(\Im Y>0\), and \(\alpha>0\). However their positive sum is
\[
f_1+f_2=2X^2+8XY+10Y^2.
\]
At \(Y=1\), this is
\[
2X^2+8X+10,
\]
whose discriminant is
\[
8^2-4(2)(10)=-16<0.
\]
Hence the sum is not stable. Therefore positivity of the measure plus pointwise stability is insufficient without an additional common-position/structure hypothesis.

This directly reopens the exact mixing obstruction isolated in Frontier 82.

## 5. Corrected proof target

The missing theorem must be substantially stronger than:
\[
p_u\text{ stable for every }u
\quad\Longrightarrow\quad
\int p_u\,d\mu(u)\text{ stable}.
\]
A valid route would need, for example:

1. a theorem that all \(H_u\) lie in a common proper-position cone and that the integral preserves that cone;
2. a genuine variation-diminishing/total-positivity theorem for the specific kernel \(u\mapsto H_u\);
3. an exact stability-preserving linear operator whose integral is a specialization/limit of known stability preservers;
4. or an independent Hermite/PF-infinity certificate for the integrated polynomial.

No such theorem has yet been proved in the RH repository.

## 6. Consequence for RH status

The preprint's claimed Theorem 7.9 (hyperbolicity of every \(P_D\)) depends on the unverified integration theorem. Therefore the subsequent LP-closure and RH conclusion do not follow from the currently audited argument.

This audit does **not** disprove the possibility that the specific theta family has an additional structure making the integral stable. It establishes only that the currently stated justification does not demonstrate that fact.

## 7. Research target opened by this audit

The next proof-bearing objective is now:
\[
\boxed{
\text{prove a theta-specific stability-preserving theorem for }
H_D(X,Y)=2\int_0^\infty\Phi(u)H_u(X,Y)\,du.
}
\]
In particular, search for a hidden common proper-position relation among the factors \(X+\sigma_i u^{-2}Y\), or transform the \(u\)-integration into a known stability-preserving differential/Hadamard operator.

## Status

Frontier 83 is an adversarial audit and blocker identification, not a proof of RH.
