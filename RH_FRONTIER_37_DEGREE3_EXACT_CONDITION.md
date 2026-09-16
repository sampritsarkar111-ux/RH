# Frontier 37 — degree-3 exact condition in consecutive xi coefficients

Frontier 36 gives, for the leading 3x3 Hermite minor of a degree-\(d\) monic Jensen polynomial,
\[
\Delta_3=\frac{d^3(d-1)^2(d-2)}{12}\,\widetilde Q_d.
\]
At the first nontrivial case \(d=3\),
\[
\boxed{\widetilde Q_3=-3w^2-12v^3},
\]
where
\[
v=\frac{q_2q_0-q_1^2}{q_0^2},
\]
\[
w=\frac{q_3q_0^2-3q_1q_2q_0+2q_1^3}{q_0^3}.
\]
Hence
\[
\boxed{
\Delta_3(d=3)= -\frac{27}{2}\,q_0^0\,(w^2+4v^3)
}
\]
in the normalized form, or equivalently the exact sign condition is
\[
\boxed{w^2+4v^3\le0.}
\]
Because \(w^2\ge0\) over the reals, this requires
\[
\boxed{v\le0}
\]
and, more strongly,
\[
\boxed{-4v^3\ge w^2}.
\]

Thus the degree-3 Hermite condition forces the first normalized adjacent Turan quantity
\[
v=(q_0q_2-q_1^2)/q_0^2
\]
to be nonpositive. This is consistent with the fact that the Jensen coefficient sequence need not be log-concave/log-convex in the naive moment sense; the Hermite constraints encode a different geometry.

For the Riemann-xi coefficients, this becomes an exact, directly testable inequality on five consecutive \(\gamma\)'s. The next target is to substitute the exact theta-moment formula for \(\gamma_m\) and derive the sign of \(v\) and the cubic discriminant-type quantity \(-4v^3-w^2\) from the theta kernel.

**Status:** exact necessary condition; no RH proof.
