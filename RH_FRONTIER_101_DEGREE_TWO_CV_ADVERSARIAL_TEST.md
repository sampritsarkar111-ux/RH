# Frontier 101 — degree-two coefficient-of-variation adversarial test

Date: 2026-09-16

## Purpose

Frontier 99 reduced the corrected degree-two gate to
\[
\frac{\operatorname{Var}(Y)}{E[Y]^2}\le R_n-1,
\qquad
R_n-1=\frac{4n^2+16n+13}{(n+1)(2n+1)(2n+5)}\sim\frac1n.
\]
Frontier 100 established \(\Phi(u)>0\) for the completed theta kernel and warned that global Mellin evaluation must preserve completion.

## Exact consequence

If the relevant Jensen variable were \(Y=u^2\) under the normalized positive measure \(d\nu(u)=\Phi(u)du/\int\Phi\), then the gate would require
\[
\frac{E[u^4]-E[u^2]^2}{E[u^2]^2}\le R_n-1.
\]
A direct high-precision quadrature audit of the completed kernel gives approximately
\[
E[u^2]\approx 0.0462085,\qquad
E[u^4]\approx 0.0059603,
\]
so the left side is approximately \(1.7911\). Since \(R_1-1=11/14\approx0.7857\) and \(R_n-1\) decreases to zero, this hypothetical identification \(Y=u^2\) cannot be the required all-n mechanism.

This numerical statement is **not** used as a proof of RH or non-RH. Its purpose is adversarial route selection: it shows that one must not silently identify the Jensen variable with \(u^2\). The exact Jensen construction must be recovered before any coefficient-of-variation theorem is attempted.

## New proof-bearing requirement

The remaining mathematical task is therefore sharper:

1. Recover the exact variable \(Y\) appearing in the factorial-corrected Jensen determinant from the repository's original derivation.
2. Derive its completed-theta pushforward measure exactly.
3. Compute or bound its coefficient of variation analytically, with no numerical inference.
4. If the gate fails, record the exact failure and abandon this degree-two route.
5. If it holds, use it only as a degree-two lemma; an independent all-degree hyperbolicity-preserving mechanism is still required for RH.

## Status

This frontier is an adversarial diagnostic, not a proof. RH remains unproved.
