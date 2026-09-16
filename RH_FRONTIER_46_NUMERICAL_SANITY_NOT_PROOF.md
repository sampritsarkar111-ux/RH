# Frontier 46 — numerical sanity check for the first Turan quantities

Using direct quadrature for the incomplete-Gamma/theta-moment representation and retaining the rapidly decaying first four theta atoms, the first four computed Turan quantities are positive:
\[
T_1\approx2.3034443239380\times10^{-7},
\]
\[
T_2\approx8.2216891966648\times10^{-11},
\]
\[
T_3\approx2.6936944695027\times10^{-14},
\]
\[
T_4\approx8.1552585326433\times10^{-18}.
\]
The values stabilize strongly because the \(k\ge2\) theta atoms are exponentially suppressed.

These calculations are only a consistency check. They do **not** prove the inequalities for all indices and do not contribute an RH proof unless converted into a uniform analytic theorem with rigorous error bounds.

The important contrast is now exact:
- the raw two-variable kernel has explicit negative points, e.g. \(K_1(1,5)=-163612/5\);
- the theta-weighted integral nevertheless has positive low-order values.

Therefore the missing mechanism must be a nontrivial global property of the Riemann theta measure.
