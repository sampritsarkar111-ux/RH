# Frontier 66 — adversarial algebra audit

## Result

The cubic relation has been rechecked symbolically. The exact relation is
\[
\boxed{\Delta_3(J^{3,n})=\frac{9q_n^4}{q_{n+3}^4}\widetilde Q_3(n)},
\]
not `9 q_n^2/q_{n+3}^4 * Qtilde`.

Reason: with `r_j=q_{n+j}/q_n`,
\[
B_n=q_n^4(w^2+4v^3),
\]
while `Qtilde_3=-3(w^2+4v^3)`. Since `Delta_3=-27 B_n/q_{n+3}^4`, the displayed boxed relation follows.

This correction is important because a proof program must not allow a scaling error to survive as a claimed breakthrough. The sign conclusion is unchanged because the prefactor `9q_n^4/q_{n+3}^4` is strictly positive whenever `q_n q_{n+3}\ne0`.

## Consequence

The cubic gate still requires
\[
\widetilde Q_3\ge0
\]
for hyperbolicity, and ordinary Stieltjes positivity still gives `Qtilde_3\le0`. The negative route is therefore robust under the corrected scaling.

## Next mandatory task

Derive the actual theta integral for the coefficient sequence used in `q_n`, substitute it into `B_n`, and determine whether the four-fold symmetrized kernel has a sign-definite factorization. No heuristic sign argument is acceptable.

## Status

No RH proof. This audit strengthens the reliability of Frontier 64 by removing a coefficient-power error before further positivity work.
