# Frontier 51 — factorial-conjugate log-concavity: the exact remaining local bridge

## Objective

Frontier 50 proves every theta atom `B_m(pi k^2)` is strictly positive. The next obstruction is not positivity but the interaction between the factorial prefactor and the atom sum.

Write
\[
M_m:=\sum_{k\ge1}B_m(\pi k^2),
\qquad
\gamma_m=Cq_mM_m,
\qquad q_m=\frac{m!}{(2m)!}>0.
\]

The adjacent Turan inequality
\[
\gamma_{m+1}^2\ge\gamma_m\gamma_{m+2}
\]
is exactly equivalent to
\[
\boxed{
\frac{M_{m+1}^2}{M_mM_{m+2}}
\ge
\frac{q_mq_{m+2}}{q_{m+1}^2}
=\frac{(m+2)(2m+3)}{(m+1)(2m+1)}.
}
\]

## 1. Exact factorial correction

\[
\boxed{\frac{q_{m+1}^2}{q_mq_{m+2}}=\frac{(m+1)(2m+1)}{(m+2)(2m+3)}}.
\]
Thus the local Turan problem is exactly one explicit inequality for `M_m`.

## 2. Positivity is insufficient

Frontier 50 proves `B_m(pi k^2)>0`, but positive sequences can be log-convex. The factorial factor must quantitatively overcome the atom-sum curvature.

## 3. Adversarial test of a tempting stronger route

A tempting sufficient condition is the four-point inequality
\[
B_{m+1}(a)B_{m+1}(b)
\ge
\eta_m\bigl(B_m(a)B_{m+2}(b)+B_m(b)B_{m+2}(a)\bigr),
\]
where
\[
\eta_m=\frac{(m+1)(2m+1)}{2(m+2)(2m+3)}.
\]
It is **false**. Direct high-precision quadrature gives a counterexample already at
\[
m=1,\qquad a=\pi,\qquad b=4\pi,
\]
for which the ratio left/right is approximately `0.3433<1`. Therefore the Turan form cannot be certified by pointwise positivity of this stronger four-point kernel inequality.

This falsification is important: it forces the proof to use genuinely global summation structure.

## 4. Exact global target

Define
\[
p_m(k)=\frac{B_m(\pi k^2)}{M_m}.
\]
Then `p_m` is a probability distribution over `k`. The remaining inequality is a structured overlap/transport inequality among the three adjacent distributions, not a pointwise kernel inequality.

A viable route is to prove monotonicity and quantitative contraction for
\[
\mathcal R_m(k)=\frac{B_{m+1}(\pi k^2)}{B_m(\pi k^2)},
\]
then convert the double sum into a covariance/variance bound.

## 5. New research target: total positivity of the atom matrix

Set
\[
\mathsf B_{m,k}=B_m(\pi k^2).
\]
Seek a two-by-two minor theorem of the form
\[
\boxed{
\mathsf B_{m,k}\mathsf B_{m+1,k+1}
-\mathsf B_{m,k+1}\mathsf B_{m+1,k}\ge0
}
\]
or the reverse sign, after determining the actual orientation. Such total positivity would provide a mathematically natural mechanism for controlling the change of measure in `k`.

The orientation must be established, not assumed.

## 6. Audit

**Established:** exact factorial-conjugate reformulation; a concrete counterexample to the tempting pointwise four-point strengthening; the precise global atom-sum target.

**Open:** the total-positivity orientation and theorem; the required atom-sum Turan inequality; the degree-3 cone; all-degree Jensen hyperbolicity; equivalence-to-RH closure; RH itself.

**Status: rigorous reduction plus adversarial falsification; no RH proof claimed.**
