# Frontier 70 — global closure matrix

## Objective

Prevent local progress on the cubic gate from being mistaken for a complete RH argument. The global closure problem is organized into independent gates.

| Gate | Required statement | Current status |
|---|---|---|
| A | Exact theta representation for all canonical coefficients | established |
| B | Degree-2 Jensen hyperbolicity for every shift | reduced to a factorially corrected moment inequality |
| C | Degree-3 hyperbolicity for every shift | exact discriminant reduction; theta sign certificate missing |
| D | All finite degrees and shifts | open |
| E | Passage from all Jensen hyperbolicity to RH | exact Pólya–Jensen equivalence |
| F | Independent convergence/interchange proofs | must accompany any proposed global kernel identity |

## Global theorem target

The strongest non-circular closure statement in the present program is
\[
\boxed{\forall d,n\ge0,\qquad J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma(n+j)X^j\text{ is hyperbolic}.}
\]
This is sufficient for RH by the Pólya–Jensen criterion, but it is not currently proved.

## Required proof architecture

A genuine completion must supply all of the following:

1. an exact identity, not a fitted recurrence;
2. a sign theorem valid uniformly in both \(d\) and \(n\);
3. absolute convergence and justified exchanges of sums, products, and integrals;
4. explicit treatment of every degenerate case and denominator;
5. no hidden use of RH, unknown zero locations, or an equivalent LP/total-positivity theorem;
6. a final theorem connecting the certificate to RH.

## Active branches of attack

### Branch I — modular pairing

Derive a paired theta identity for the cubic numerator, then seek a general-degree analogue.

### Branch II — propagation

Derive exact shift relations for Hermite/Jensen invariants. Any positivity of a remainder must come from the theta structure and be proved independently.

### Branch III — direct LP closure

Search for a theta-derived real-zero-preserving transform proving \(\Xi\in LP_\mathbb R\) without assuming a total-positivity theorem equivalent to RH.

### Branch IV — Hermite matrix SOS

For each degree, seek an exact PSD representation of the Hermite matrix from theta data, with a uniform construction rather than separate finite computations.

## Adversarial rule

Finite numerical verification, a large-index asymptotic wedge, or a finite collection of Jensen degrees cannot close the infinite theorem. Such evidence is retained only as diagnostic information.

## Status

**Global program remains open.** This file is a closure specification and audit framework, not a proof of RH.
