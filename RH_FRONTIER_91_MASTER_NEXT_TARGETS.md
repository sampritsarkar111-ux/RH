# Frontier 91 — Master next-target program after scale-mixture obstruction

Date: 2026-09-16

## Current state

Frontiers 84–90 eliminate several generic routes and reduce the surviving problem to theta-specific structure. In particular, the degree-two Jensen discriminant has an exact two-point kernel, but that kernel changes sign away from the diagonal. Therefore generic positive-kernel and arbitrary positive-mixture arguments are unavailable.

## Three remaining high-value attacks

### A. Modular involution / orbit pairing

Derive the exact involution inherited from the theta transformation in the original \((x,u)\) variables, not after collapsing to \(y=x(1-x)u^2\). Determine whether each orbit contributes a square or a nonnegative quadratic form. The degree-two calculation is the first falsification gate.

### B. Hermite matrix factorization

For each finite \(d,n\), compute the Hermite matrix of
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
Seek an exact factorization
\[
\mathsf H_{d,n}=A_{d,n}^*G_{d,n}A_{d,n},\qquad G_{d,n}\succeq0,
\]
where every entry of \(G_{d,n}\) follows from theta modularity and positivity. Any factorization found only for small d is evidence, not a proof.

### C. Variation-diminishing operator

Treat
\[
q_{n,d}(t)=\frac{d!}{(n+d)!}\left[(2n+1)L_d^{(n)}(-t)-2t(L_d^{(n)})'(-t)\right]
\]
as the fixed-scale hyperbolic family. Prove, if possible, that the theta scale-mixture operator preserves this particular cone. A valid theorem must be family-specific; the generic statement is false.

## Hard acceptance criteria

A purported closure must establish:

1. all \(n,d\), not finitely many cases;
2. convergence and all sum/integral interchanges;
3. positivity or real-rootedness without assuming RH;
4. degenerate/equality cases;
5. an explicit implication to RH, not an RH-equivalent condition assumed as input.

## Non-claims

No current frontier is a proof of RH. Numerical zeros, finite Hermite matrices, asymptotic regions, or an unproved stability-preserving integration theorem cannot close the problem.

## Immediate next experiment

The highest-information symbolic experiment is to derive the exact modular orbit map in the original theta variables and substitute it into the degree-two kernel. If it yields a positive orbit identity, generalize the identity to the full Hermite matrix. If it fails, retain the explicit obstruction and move to operator factorization.
