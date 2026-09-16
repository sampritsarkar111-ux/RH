# Frontier 45 — exact off-diagonal kernel countercheck

For m=1 the raw Turan kernel simplifies exactly to
\[
K_1(x,y)=-\frac1{10}\bigl(x^6y^2-16x^6-10x^4y^4+720x^4y^2+3840x^4+x^2y^6+720x^2y^4-92160x^2y^2-16y^6+3840y^4\bigr).
\]
At the exact positive point \((x,y)=(1,5)\),
\[
\boxed{K_1(1,5)=-\frac{163612}{5}<0.}
\]
Thus the pointwise-positive-kernel route is decisively falsified by an exact rational evaluation, not merely floating-point sampling.

This does **not** imply \(T_1<0\): the theta-weighted double integral can still be positive despite a signed integrand. The correct remaining problem is therefore global positivity after the Riemann theta measure is inserted.

Status: exact counterexample to pointwise positivity; no RH proof.
