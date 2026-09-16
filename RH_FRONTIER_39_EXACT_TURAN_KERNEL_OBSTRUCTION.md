# Frontier 39 — exact factorial-corrected Turan kernel and obstruction

## Objective

Continue Frontier 38 by carrying the theta representation to an exact double-integral formula for
\[
T_m:=\gamma_{m+1}^2-\gamma_m\gamma_{m+2}.
\]
The purpose is to determine whether the direct pointwise-positive kernel mechanism is available.

## Exact reduction

Write
\[
d\nu(t)=t^{-3/4}\theta_0(t)\,dt,\qquad x=\log t\ge0,
\]
and
\[
A_m(x):=x^{2m-2}\bigl(16m(2m-1)-x^2\bigr).
\]
Then the exact coefficient formula becomes
\[
\gamma_m=Cq_m\int_1^\infty A_m(\log t)\,d\nu(t),
\qquad q_m=\frac{m!}{(2m)!},
\]
with C>0.

Since
\[
\frac{q_mq_{m+2}}{q_{m+1}^2}=\frac{(m+1)(2m+1)}{(m+2)(2m+3)},
\]
we obtain
\[
T_m=C^2q_{m+1}^2\iint K_m(x,y)\,d\nu_xd\nu_y,
\]
where
\[
K_m(x,y)=A_{m+1}(x)A_{m+1}(y)
-\frac{(m+1)(2m+1)}{2(m+2)(2m+3)}\bigl[A_m(x)A_{m+2}(y)+A_m(y)A_{m+2}(x)\bigr].
\]
This is an exact algebraic identity and uses no zero-location assumption.

## Falsification of the naive positivity route

The hoped-for direct factorization
\[
K_m(x,y)=(x-y)^2R_m(x,y),\qquad R_m\ge0,
\]
is not valid for the raw kernel. Symbolic expansion and sign testing on x,y>0 gives negative kernel values already for m=1 (and also for higher m). Thus a proof of T_m\ge0 cannot simply assert pointwise positivity of this first natural kernel.

This is a useful rigorous guardrail: the theta-specific structure must enter before positivity can be claimed.

## Next targets

1. Expand K_m in x^2,y^2 and isolate all negative coefficient sectors.
2. Insert \(\theta_0(t)=\sum_{k\ge1}e^{-\pi k^2t}\) before integration and derive an exact double-sum representation.
3. Search for a pairing/involution in the (k,l) indices or an exact integral identity converting the signed kernel into nonnegative pieces.
4. Test whether the modular theta transformation supplies the missing cancellation.
5. Attack the stronger degree-3 condition \(4v^3+w^2\le0\), because T_m\ge0 alone is only necessary.
6. Continue the all-order Toeplitz-minor route in parallel.

## Status

**Rigorous exact reduction plus falsification of the naive pointwise-positive kernel route. Not an RH proof.**
