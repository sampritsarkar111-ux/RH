# Frontier 36 — exact central-moment factorization of the third Hermite obstruction

A new exact symbolic factorization sharpens the bottleneck substantially.

Set normalized consecutive ratios
\[
r_j=q_j/q_0,
\]
and introduce the formal central-moment coordinates
\[
a=r_1,
\]
\[
v=r_2-a^2,
\qquad
w=r_3-3ar_2+2a^3,
\qquad
z=r_4-4ar_3+6a^2r_2-3a^4.
\]
Equivalently,
\[
r_2=a^2+v,
\quad
r_3=a^3+3av+w,
\quad
r_4=a^4+6a^2v+4aw+z.
\]

Exact symbolic substitution into Frontier 34 gives the striking identities
\[
\boxed{P_0=2vz-3w^2-6v^3},
\]
\[
\boxed{H_0=vz-w^2-v^3}.
\]
Therefore
\[
\boxed{
\widetilde Q_d
=dP_0-6H_0
=2(d-3)vz-3(d-2)w^2-6(d-1)v^3.
}
\]
Consequently
\[
\boxed{
\Delta_3
=\frac{d^3(d-1)^2(d-2)}{12}
\left[2(d-3)vz-3(d-2)w^2-6(d-1)v^3\right].
}
\]

## Immediate consequence at d=3

For \(d=3\), the first term vanishes exactly:
\[
\boxed{
\widetilde Q_3=-3w^2-12v^3.
}
\]
Thus if the normalized five-term sequence \((q_0,\ldots,q_4)\) were itself a genuine Stieltjes moment sequence, then \(v\ge0\), and necessarily
\[
\widetilde Q_3\le0,
\]
with strict negativity whenever \(v>0\) or \(w\ne0\).

This is an important structural obstruction: ordinary Stieltjes/Hankel positivity of the \(\gamma\)-sequence is not merely insufficient; for a nondegenerate sequence it points in the opposite direction at the degree-3 Hermite obstruction.

The Riemann-xi sequence therefore requires a genuinely non-Stieltjes mechanism (or a more delicate signed/indefinite kernel structure) to establish Jensen hyperbolicity.

## New research target

The next exact question is now:
\[
\boxed{
\text{What signed or theta-specific structure makes }
2(d-3)vz-3(d-2)w^2-6(d-1)v^3\ge0
\text{ for the actual Riemann-xi ratios?}
}
\]

For \(d=3\), this reduces to understanding the sign pattern of the formal central coordinates \(v,w\) for consecutive \(\gamma_m\). This may provide a substantially more focused route than expanding higher Hermite determinants blindly.

## Status

**Rigorous symbolic breakthrough in the reduction; not a proof of RH.** The factorization is exact algebra. The remaining sign problem for the actual Riemann-xi coefficients is open within this research program.
