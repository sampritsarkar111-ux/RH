# Frontier 11 — Theta-Kernel Structural Audit

## Objective

Exploit structure specific to the Riemann theta kernel to prove the Jensen inequalities needed for all degrees.

## Candidate mechanisms

Investigate whether the transformed kernel satisfies a sufficiently strong form of:

- strict total positivity;
- sign-regularity of all relevant minors;
- Pólya-frequency properties;
- variation-diminishing transforms;
- complete monotonicity together with an additional rigidity condition.

## Required bridge

It is not enough to establish one of these properties in isolation. The proof must explicitly derive

\[
\text{kernel property}
\Longrightarrow
\text{coefficient/minor inequalities}
\Longrightarrow
\text{hyperbolicity of }J_{d,n}
\]

for every \(d,n\ge0\).

## Known obstruction

A generic positive measure representation gives moment log-convexity in the wrong direction for the needed degree-two lower bound. Therefore the argument must use a property that is stronger and genuinely tied to the Riemann kernel.

## Status

No such all-degree theorem has yet been proved here. This file records the exact bridge that remains to be established.
