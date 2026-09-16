# Frontier 57 — ratio-coordinate attack on the structured Turan gate

Define positive moment ratios
\[
r_j:=\frac{\mu_{j+1}}{\mu_j},\qquad j\ge0.
\]
For every positive measure on \([0,\infty)\), the Stieltjes moment sequence is log-convex, so
\[
\boxed{r_{j+1}\ge r_j.}
\]
Set
\[
M_m=\mu_m\left(16m(2m-1)\frac1{r_{m-1}}-1\right).
\]
Thus the factorial-conjugate Turan inequality can be rewritten purely in three consecutive ratios \(r_{m-1},r_m,r_{m+1}\).

Let
\[
\alpha_m=16m(2m-1),
\quad
\beta_m=\frac{(m+2)(2m+3)}{(m+1)(2m+1)}.
\]
Then
\[
\boxed{
\left(\frac{\alpha_{m+1}}{r_m}-1\right)^2
\ge
\beta_m
\left(\frac{\alpha_m}{r_{m-1}}-1\right)
\left(\frac{\alpha_{m+2}}{r_{m+1}}-1\right).
}
\]
The atom-positivity theorem ensures the three bracketed factors are positive for the actual theta measure.

## Why this is a sharper target

The infinite-dimensional Turan problem is now a finite ratio inequality. Universal Stieltjes structure gives only
\[
r_{m-1}\le r_m\le r_{m+1},
\]
plus stronger Hankel constraints. The next exact attack is therefore to determine whether the displayed inequality follows from a finite set of universal Stieltjes moment inequalities. If not, the first violating realizable moment sequence identifies precisely what extra theta-specific input is required.

## Status

This is an exact reparameterization, not a proof. It isolates a potentially tractable three-ratio core and provides a clean falsification target for future symbolic/semidefinite analysis.