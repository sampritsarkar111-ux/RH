# Frontier 42 — exact theta double-sum representation and Mellin/incomplete-Gamma reduction

## Objective

Push Frontier 39 beyond the raw signed kernel by inserting the theta series *before* integration. The goal is an exact discrete representation of the Turan quantity
\[
T_m=\gamma_{m+1}^2-\gamma_m\gamma_{m+2},
\]
without assuming RH, and then identify what a genuinely Riemann-specific positivity lemma would have to prove.

## 1. Exact one-atom transform

For \(N\in\mathbb N_0\) and \(a>0\), define
\[
I_N(a):=\int_1^\infty (\log t)^N t^{-3/4}e^{-at}\,dt.
\]
For \(s>0\),
\[
\int_1^\infty t^{s-1}e^{-at}\,dt=a^{-s}\Gamma(s,a).
\]
Differentiating with respect to \(s\) under the integral (justified on compact \(s\)-intervals by exponential domination) gives the exact identity
\[
\boxed{I_N(a)=\left.\frac{\partial^N}{\partial s^N}\left[a^{-s}\Gamma(s,a)\right]\right|_{s=1/4}.}
\]
Thus every theta moment is an explicit finite-order parameter derivative of an incomplete-Gamma expression.

## 2. Exact theta moments

Since
\[
\theta_0(t)=\sum_{k\ge1}e^{-\pi k^2t},
\]
and every summand is nonnegative before multiplication by the polynomial factor in the coefficient formula, Tonelli applies separately to the positive raw moments
\[
F_N:=\int_1^\infty(\log t)^N t^{-3/4}\theta_0(t)\,dt
      =\sum_{k\ge1}I_N(\pi k^2).
\]
Consequently
\[
\boxed{F_N=\sum_{k\ge1}\left.\partial_s^N\left[(\pi k^2)^{-s}\Gamma(s,\pi k^2)\right]\right|_{s=1/4}.}
\]
The series is absolutely convergent because \(\Gamma(s,\pi k^2)\) has exponential decay in \(k^2\).

## 3. Exact coefficient sequence

With the normalization constant \(C>0\) used in earlier frontiers,
\[
\gamma_m=C\frac{m!}{(2m)!\,2^{2m-1}}
\left(32\binom{2m}{2}F_{2m-2}-F_{2m}\right).
\]
Hence \(T_m\) is an exact double sum
\[
\boxed{T_m=C^2q_{m+1}^2\sum_{k,\ell\ge1}\mathcal K_m(k,\ell),
\qquad q_m=\frac{m!}{(2m)!},}
\]
where \(\mathcal K_m(k,\ell)\) is obtained by replacing the two theta measures in the Frontier-39 kernel by the individual atoms \(e^{-\pi k^2t}dt\) and \(e^{-\pi\ell^2u}du\). Equivalently, with
\[
J_r(k):=I_r(\pi k^2),\qquad
B_m(k):=16m(2m-1)J_{2m-2}(k)-J_{2m}(k),
\]
we have the fully discrete exact formula
\[
\boxed{
T_m=C^2q_{m+1}^2\sum_{k,\ell\ge1}
\left[B_{m+1}(k)B_{m+1}(\ell)
-\eta_m\big(B_m(k)B_{m+2}(\ell)+B_m(\ell)B_{m+2}(k)\big)\right],
}
\]
with
\[
\eta_m=\frac{(m+1)(2m+1)}{2(m+2)(2m+3)}.
\]
This is an exact Riemann-specific reduction; no zero-location statement has entered.

## 4. New structural observation

The obstruction is now sharply localized. A successful proof of \(T_m\ge0\) cannot rely on pointwise positivity of the continuous kernel (Frontier 39 disproved that route). It must instead prove a *global quadratic-form inequality* for the discrete vector
\[
\big(B_m(k)\big)_{k\ge1}
\]
under the theta weight induced by the incomplete-Gamma transforms.

A particularly strong target is an explicit symmetric matrix \(M_m(k,\ell)\) with
\[
\sum_{k,\ell\ge1}M_m(k,\ell)\ge0
\]
proved by one of:

1. an exact \((k,\ell)\leftrightarrow(\ell,k)\) pairing plus a nonnegative remainder;
2. a Cauchy–Schwarz/Gram representation;
3. a modular transformation converting the signed polynomial in \(\log t\) into a manifestly positive combination;
4. an all-order total-positivity statement for the resulting theta/incomplete-Gamma kernel.

## 5. Stronger degree-3 target remains mandatory

Even a proof of every adjacent Turan inequality
\[
\gamma_{n+2}^2\ge\gamma_{n+1}\gamma_{n+3}
\]
would only establish the first necessary Jensen obstruction. The exact degree-3 centered condition remains
\[
\boxed{4v^3+w^2\le0},
\]
with \(v,w\) the centered invariants of the relevant coefficient block. Therefore the actual RH closure still requires either this stronger condition for every degree/index or a stronger all-degree hyperbolicity theorem.

## 6. Proof-audit status

Established here:
- exact incomplete-Gamma representation of every theta logarithmic moment;
- exact theta-series expansion of those moments;
- exact discrete double-sum representation of the Turan expression;
- precise identification of the remaining Riemann-specific positivity problem.

Not established:
- positivity of the double sum for all \(m\);
- the degree-3 cone for all indices;
- all-degree Jensen hyperbolicity;
- all-order Toeplitz total positivity;
- the final equivalence from those properties to RH.

**Status: rigorous new reduction, not an RH proof.**
