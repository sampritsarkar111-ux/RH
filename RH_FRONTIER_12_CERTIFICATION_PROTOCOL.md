# Frontier 12 — Certification Protocol

## Purpose

Turn the Jensen-polynomial bottleneck into machine-checkable finite tests without confusing finite verification with a proof of RH.

## Exact objects

For

\[
G(z)=8\xi(1/2+z)=\sum_{n\ge0}\gamma(n)z^{2n}/n!,
\]

define

\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j.
\]

For each selected `(d,n)` the certification record must contain:

1. precision of every input coefficient;
2. an enclosure for every coefficient;
3. a certified real-root isolation result, or a certified non-real-root witness;
4. the precision/error bound used;
5. a reproducible hash of the input data and computation;
6. the exact normalization convention.

## Degree-2 gate

Before any all-degree conjecture is trusted, certify

\[
\gamma(n+1)^2-\gamma(n)\gamma(n+2)\ge0
\]

for the tested range. Equivalently, under the moment normalization used in Frontier 11,

\[
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]

A failure is a route-level falsification, not evidence against RH itself.

## Universal-proof gate

A finite table of successful Jensen tests never proves RH. Promotion to a proof requires a theorem valid for all `d,n`, followed by a rigorous theorem connecting the resulting entire-function class to the zero-line statement.

## Anti-circularity checks

Reject any computation or lemma that:

- assumes all zeros lie on the critical line;
- imports a theorem whose hypotheses already contain RH;
- uses an asymptotic with an uncontrolled error term to infer an exact universal inequality;
- infers exact root reality from floating-point roots alone.

## Next mathematical target

Find a structural identity for the Riemann theta kernel that controls the sign of every relevant Jensen/Hankel minor. This is the point at which a genuinely new theorem would convert the current research program into a proof attempt.