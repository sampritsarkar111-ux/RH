# Frontier 125 — Degree-4 scale-free Jensen discriminant

Date: 2026-09-17

Define the factorial-shape coordinates
\[
R_j=\frac{\gamma_{n+j}/\gamma_n}{(\gamma_{n+1}/\gamma_n)^j}.
\]
After dividing by \(\gamma_n\) and scaling \(X\mapsto X/(\gamma_{n+1}/\gamma_n)\), the degree-4 Jensen polynomial becomes
\[
\mathcal J_4(X)=1+4X+6R_2X^2+4R_3X^3+R_4X^4.
\]

Its exact quartic discriminant is
\[
\boxed{
\operatorname{Disc}(\mathcal J_4)=256\,D_4(R_2,R_3,R_4),
}
\]
where
\[
\boxed{
\begin{aligned}
D_4={}&81R_2^4R_4-54R_2^3R_3^2-54R_2^3R_4+36R_2^2R_3^2
-180R_2^2R_3R_4-18R_2^2R_4^2\\
&+108R_2R_3^3+54R_2R_3^2R_4+108R_2R_3R_4+54R_2R_4^2\\
&-27R_3^4-64R_3^3-6R_3^2R_4-12R_3R_4^2+R_4^3-27R_4^2.
\end{aligned}
}
\]

This is a necessary algebraic boundary for four-real-root hyperbolicity, but discriminant nonnegativity alone is not sufficient for a quartic: the remaining resolvent/sign conditions must also be imposed. Therefore this formula is a gate, not an RH proof.

The significance is structural: degree 3 required two shape coordinates; degree 4 requires three. The all-degree program can therefore be formulated as inclusion of the Riemann coefficient shape orbit in the exact hyperbolicity regions \(\mathscr R_d\), with no scale parameter and no zero-location assumptions.

## Status

Exact symbolic reduction completed. The remaining proof-bearing task is the degree-uniform theorem controlling the factorial-shape orbit \((R_{n,2},\ldots,R_{n,d})\) for the completed Riemann Xi coefficients.
