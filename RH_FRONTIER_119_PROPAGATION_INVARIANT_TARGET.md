# Frontier 119 — finite-strip positivity propagation target

Date: 2026-09-17

## Motivation

The de Bruijn–Newman route reduces the endpoint to the missing global real-rootedness statement. The Jensen/Hermite route expresses the same obstruction through infinitely many degrees and shifts. A potentially decisive synthesis is an exact propagation invariant.

## Target invariant

Construct a family \(I_{d,n}\) of Hermite/Jensen minors or normalized discriminants such that

\[
I_{d,n}\ge0
\quad\Longrightarrow\quad
I_{d+1,n}\ge0,
\;I_{d,n+1}\ge0,
\]

under identities derived directly from the completed theta kernel.

The propagation must be uniform in both indices and must not use real-zero information.

## Stronger desired form

Find an exact recurrence
\[
I_{d+1,n}=A_{d,n}I_{d,n}+B_{d,n}I_{d,n+1}+R_{d,n},
\]
with \(A_{d,n},B_{d,n}\ge0\) and \(R_{d,n}\ge0\) proved from theta data. Such a recurrence would reduce the infinite problem to a finite seed set plus an induction theorem.

## Adversarial requirement

Any recurrence must be checked symbolically before numerical exploration. If a coefficient changes sign or a remainder is not provably nonnegative, classify the candidate as OPEN rather than treating numerical positivity as evidence of a theorem.
