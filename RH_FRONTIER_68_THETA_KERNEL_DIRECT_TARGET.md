# Frontier 68 — Direct theta-kernel closure target

Date: 2026-09-16
Status: hard target; no proof claimed

Let Xi(t)=∫_0^∞ Φ(u) cos(tu)du and M_n=∫_0^∞ Φ(u)u^{2n}du, with γ(n)=8 n!/(2n)! M_n.

The obstacle is that ordinary Stieltjes positivity yields M_{n+1}^2≤M_nM_{n+2}, while Jensen degree 2 requires the factorial-corrected reverse-direction inequality

γ(n+1)^2≥γ(n)γ(n+2)
⇔ M_{n+1}^2≥(2n+1)/(2n+3) M_nM_{n+2}.

Therefore seek an identity of the form

(2n+3)M_{n+1}^2-(2n+1)M_nM_{n+2}=E_n,

where E_n has a manifestly nonnegative Riemann-theta representation. The representation must use the explicit theta kernel and cannot follow merely from Φ≥0.

A viable derivation should:

1. insert the exact theta-series for Φ;
2. justify termwise operations by absolute convergence;
3. symmetrize the resulting double sum/integral;
4. seek a square-difference or positive-kernel factorization for E_n;
5. generalize the same factorization to the higher centered/Hermite minors.

Failure criterion: if the resulting expression changes sign for a valid positive kernel, the proposed generic mechanism is rejected rather than patched.

If successful, this gives the first genuinely Riemann-specific closure mechanism. It still must be lifted from degree 2 to all Hermite minors.
