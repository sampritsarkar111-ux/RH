# Frontier 76 — algebraic sanity checks for the parallel program

Date: 2026-09-16

## Exact multiplier-ratio check
For
\[
a_n=\frac{n!}{(2n)!},
\]
we have exactly
\[
\frac{a_{n+1}^2}{a_na_{n+2}}=\frac{2n+3}{2n+1}>1.
\]
Consequently
\[
\gamma_{n+1}^2\ge \gamma_n\gamma_{n+2}
\iff
M_{n+1}^2\ge \frac{2n+1}{2n+3}M_nM_{n+2}.
\]
This confirms that the factorial correction is structurally essential: replacing \(\gamma_n\) by \(M_n\) changes the degree-two gate.

## Logical consequence
The positive-moment inequality
\[
M_{n+1}^2\le M_nM_{n+2}
\]
does not by itself decide the corrected inequality because the factor \((2n+1)/(2n+3)<1\) leaves a nontrivial interval between the two bounds. Thus the raw-moment obstruction eliminates one naive LP-preimage argument, but does not eliminate the canonical Jensen route.

## Proof audit
No numerical fit or symbolic simplification was promoted to a global theorem. The remaining problem is genuinely the canonical coefficient sequence and its all-degree real-rootedness.
