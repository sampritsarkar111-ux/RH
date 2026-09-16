# Frontier 65 — cubic theta-certificate attack

## Objective

The cubic Jensen gate is now algebraically oriented exactly. The task is to replace the abstract positivity target by an explicit theta-only identity.

## Exact target

For
\[
J^{3,n}(x)=q_n+3q_{n+1}x+3q_{n+2}x^2+q_{n+3}x^3,
\]
the discriminant is
\[
\Delta_3(J^{3,n})=-\frac{27}{q_{n+3}^4}B_n,
\]
where
\[
B_n=q_n^2q_{n+3}^2-6q_nq_{n+1}q_{n+2}q_{n+3}
+4q_nq_{n+2}^3+4q_{n+1}^3q_{n+3}-3q_{n+1}^2q_{n+2}^2.
\]
Equivalently, with
\[
v=\frac{q_{n+2}}{q_n}-\left(\frac{q_{n+1}}{q_n}\right)^2,
\quad
w=\frac{q_{n+3}}{q_n}-3\frac{q_{n+1}q_{n+2}}{q_n^2}+2\left(\frac{q_{n+1}}{q_n}\right)^3,
\]
we have
\[
B_n=q_n^4(w^2+4v^3),\qquad
\Delta_3=\frac{9q_n^4}{q_{n+3}^4}\widetilde Q_3,
\quad
\widetilde Q_3=-3(w^2+4v^3).
\]

## Theta reduction program

1. Insert the exact integral representation for each coefficient `q_{n+j}` coming from the completed-xi/theta representation.
2. Expand `B_n` into a four-fold integral over independent theta variables.
3. Apply the full permutation symmetrization in those variables before attempting any sign argument.
4. Test whether the symmetrized kernel factors through Vandermonde powers, divided differences, or a modular-pairing term.
5. If a sign-definite factorization appears, prove it symbolically and establish absolute convergence before exchanging integrals and algebraic operations.
6. If no sign-definite factorization exists, record the exact obstruction and move to the shift-propagation route rather than weakening the claim.

## Non-circularity conditions

A valid certificate may use only identities and inequalities proved directly from the theta representation and elementary real analysis/algebra. It may not use RH, zero locations, a Laguerre-Pólya conclusion, or an assumed total-positivity theorem whose proof already encodes RH.

## Parallel global route

In parallel, seek an exact identity
\[
\mathcal H_{d,n+1}-\Lambda_{d,n}\mathcal H_{d,n}=\mathcal P_{d,n},
\]
with `\Lambda_{d,n}\ge0` and `\mathcal P_{d,n}\ge0` obtained from the same theta kernel. A successful identity would turn the infinite shift direction into an inductive argument, but it must be derived rather than fitted numerically.

## Adversarial checkpoint

The cubic identity proves that ordinary Stieltjes moment positivity cannot supply the needed sign: it gives `v\ge0` and hence `\widetilde Q_3\le0`. Therefore any claimed positive certificate based only on that hypothesis is invalid.

## Status

This is a research target, not a proof. RH remains unresolved until every required Jensen degree and shift is covered by a rigorous certificate or an independently proved propagation theorem.
