# RH Frontier 122 — Factorial Kernel as the Remaining Stability Mechanism

Date: 2026-09-16

Frontier 121 established a precise negative result: after Jacobi inversion is performed at the unsummed theta level, the completed kernel has exact reflection symmetry, but the cubic factorial-corrected Toeplitz minor does not acquire an ordinary Andreief/Vandermonde-square representation.

The obstruction is structural. The coefficient entries are
\[
K_{ij}=\frac{M_{k+j-i}}{(2k+2j-2i)!},
\qquad M_n=\int u^{2n}\Phi(u)\,du,
\]
and the factorial depends on the matrix entry rather than separating as a row factor times a column factor.

Therefore the next mechanism must act on the factorial kernel itself. The exact target is to prove a variation-diminishing / total-positivity theorem for
\[
K(n,u)=\frac{u^{2n}}{(2n)!},
\]
possibly after the change of variable \(x=u^2\), in a form compatible with the Poisson-paired Riemann theta measure.

A successful theorem would need to imply the required PF-infinity property of
\[
\gamma_n=\frac{M_n}{(2n)!}
\]
for the specific Riemann measure, not merely positivity or log-convexity of \(M_n\).

The key distinction is:
\[
\text{positive measure} \not\Rightarrow PF_\infty(\gamma_n).
\]

No RH proof is claimed. This frontier isolates the exact non-Vandermonde mechanism that must be discovered or proved next.