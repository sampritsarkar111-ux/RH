# Frontier 87 — Diagonal multiplier test and exact no-go for the generic route

Date: 2026-09-16

## 1. Starting point

Frontier 85 reduces the FEATAM integral to a diagonal coefficient multiplier
\[
(a_0,\dots,a_D)\mapsto(a_0\mu_n,\dots,a_D\mu_{n+D}).
\]
The tempting shortcut is to invoke a generic positive-diagonal multiplier theorem.

## 2. Generic positivity is insufficient

A positive diagonal multiplier can destroy hyperbolicity. Already for degree two, let
\[
p(X)=X^2+4X+3=(X+1)(X+3).
\]
Multiplying its coefficients by \((1,1/10,1)\) gives
\[
\widetilde p(X)=X^2+0.4X+3.
\]
Its discriminant is
\[
0.4^2-12=-11.84<0,
\]
so the output is not hyperbolic.

Therefore the theta moments must satisfy a highly structured all-order multiplier condition; positivity or monotonicity alone cannot prove it.

## 3. Correct canonical condition

For the Xi/Jensen coefficients the first multiplier condition is exactly
\[
\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}
\iff
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]
The correction factor
\[
\frac{2n+1}{2n+3}<1
\]
is therefore not cosmetic: it is the obstruction preventing a generic positive-moment argument.

## 4. Stronger consequence

The FEATAM route cannot be closed by proving only that the theta moment sequence is a Stieltjes moment sequence, log-convex, totally positive at low order, or coefficientwise positive. The multiplier must be certified against the exact factorial-corrected Jensen cone at every order.

## 5. Surviving operator target

The next mathematically meaningful target is an explicit theta-derived factorization of the transformed Hermite matrix:
\[
\mathsf H_d(J_{D,n}^{\rm out})
=\mathsf A^*\mathsf G\mathsf A,
\qquad \mathsf G\succeq0,
\]
with \(\mathsf G\) constructed directly from the modular theta identity and independent of RH.

An equivalent route is a theta-specific multiplier theorem whose hypotheses can be checked from the exact theta kernel before any zero-location assertion.

## Status

This frontier closes another generic shortcut but does not close the RH problem. The remaining gap is now an all-order, theta-specific positivity/real-rootedness theorem.
