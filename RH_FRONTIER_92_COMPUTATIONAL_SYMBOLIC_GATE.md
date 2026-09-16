# Frontier 92 — Symbolic low-degree Hermite gate

Date: 2026-09-16

## Purpose

Establish an exact algebraic gate for future symbolic searches. This does not use numerical zeros and does not claim a proof.

For
\[
P(X)=aX^2+bX+c,
\]
the Hermite matrix (up to an irrelevant positive convention factor) is governed by the discriminant
\[
\Delta=b^2-4ac.
\]
For the degree-two Jensen polynomial
\[
J_{2,n}(X)=\gamma_n+2\gamma_{n+1}X+\gamma_{n+2}X^2,
\]
we obtain
\[
\boxed{\Delta_{2,n}=4(\gamma_{n+1}^2-\gamma_n\gamma_{n+2}).}
\]
With \(\gamma_k=(2k+1)I_k/k!\),
\[
\boxed{
\frac{\Delta_{2,n}}4
=\frac{(2n+3)^2}{((n+1)!)^2}I_{n+1}^2
-\frac{(2n+1)(2n+5)}{n!(n+2)!}I_nI_{n+2}.
}
\]
Multiplying by the positive factor \(n!(n+2)!\), the exact gate is
\[
\boxed{
\frac{n+2}{n+1}(2n+3)^2I_{n+1}^2
-(2n+1)(2n+5)I_nI_{n+2}\ge0.
}
\]

This is the first coefficient-level identity that any proposed theta-specific Gram factorization must reproduce exactly.

## Strong falsification rule

A candidate proof that instead derives ordinary moment log-concavity
\[
I_{n+1}^2\le I_nI_{n+2}
\]
has not proved the canonical Jensen inequality: the factorial correction reverses the relevant threshold. Therefore ordinary Stieltjes/Hankel positivity cannot be substituted for the required canonical gate.

## Next target

Search for an exact theta modular identity for the corrected combination above, preferably as a double sum/integral whose summands are squares or whose terms pair under the theta involution. Any identity discovered must be checked symbolically before generalizing to d>=3.

## Status

Exact diagnostic gate only; RH remains unproved.
