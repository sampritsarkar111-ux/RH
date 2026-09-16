# Frontier 67 — cubic invariant failure and new target

## Adversarial finding

A direct symbolic audit shows that the cubic discriminant is exactly
\[
\Delta_3(J^{3,n})=\frac{9q_n^4}{q_{n+3}^4}\widetilde Q_3(n),
\qquad
\widetilde Q_3=-3(w^2+4v^3).
\]
Thus the cubic gate is an exact algebraic test, but the generic moment route points in the wrong direction.

## New target: coefficient-specific log-convexity must be avoided

Because `v` is the ordinary second central-moment expression, any attempt to force `v\ge0` as a standalone theta certificate immediately forces `Qtilde_3\le0`. Therefore the certificate must exploit a coupled relation among `v,w` and the higher coefficient structure rather than positivity of `v` alone.

The next finite-degree problem is consequently:
\[
\boxed{w^2+4v^3\le0}
\]
for the actual xi/Jensen coefficient sequence, equivalently `Delta_3>=0`.

This is highly restrictive and cannot hold for an arbitrary positive-moment sequence. It must come from the special signed/factorial theta representation.

## Propagation route

Instead of assuming a positive recurrence for the discriminant itself, search for a recurrence in the normalized pair `(v,w)` or in the discriminant numerator `B_n` after substituting the exact theta coefficient formula. The desired form is an identity whose remainder has a provable sign from theta monotonicity/modular symmetry.

No such recurrence has yet been proved.

## Status

This frontier records a strengthened obstruction and a narrower, coefficient-specific target. It is not an RH proof.
