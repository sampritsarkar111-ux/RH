# Frontier 37 — Cubic sign-cone reduction and parallel closure targets

Date: 2026-09-16

## 1. Starting point

For normalized consecutive coefficients
\[
r_j=q_j/q_0,
\]
set
\[
a=r_1,\qquad v=r_2-a^2,
\]
\[
w=r_3-3ar_2+2a^3,
\qquad
z=r_4-4ar_3+6a^2r_2-3a^4.
\]
Frontier 36 gives the exact third-Hermite obstruction
\[
\widetilde Q_d
=2(d-3)vz-3(d-2)w^2-6(d-1)v^3.
\]
Thus the problem is reduced to a four-coordinate sign cone, with no root variables remaining.

## 2. New exact cubic specialization

At \(d=3\),
\[
\boxed{\widetilde Q_3=-3w^2-12v^3.}
\]
Therefore
\[
\boxed{\widetilde Q_3\ge0
\iff
4(-v)^3\ge w^2.}
\]
In particular, a necessary condition for the degree-3 Hermite minor is
\[
\boxed{v\le0,}
\]
and, unless \(v=w=0\), the stronger condition is
\[
\boxed{v<0,\qquad |w|\le2(-v)^{3/2}.}
\]
This is substantially sharper than ordinary Hankel/Stieltjes positivity, which would impose \(v\ge0\). Hence the relevant Riemann-xi coefficient geometry is intrinsically outside the ordinary Stieltjes cone.

## 3. Exact general-degree sign decomposition

Write \(u=-v\). Whenever \(v<0\), the obstruction becomes
\[
\boxed{
\widetilde Q_d
=6(d-1)u^3-3(d-2)w^2-2(d-3)uz.
}
\]
For \(d=3\), the \(z\)-term disappears exactly. For \(d>3\), a successful proof must control the competition between the cubic scale \(u^3\), skew term \(w^2\), and fourth-central coordinate \(uz\).

A useful sufficient cone condition is therefore
\[
\boxed{
6(d-1)u^3\ge3(d-2)w^2+2(d-3)uz
\quad(d\ge3).
}
\]
The central task is to derive this inequality from the exact Riemann-theta representation, uniformly in shift \(n\) and degree \(d\), without assuming RH.

## 4. Numerical reconnaissance (not proof)

Direct high-precision differentiation of the exact xi-function gives, for the first admissible shift in the cubic test, \(v<0\), \(w>0\), and
\[
4(-v)^3-w^2>0.
\]
The same sign pattern persists in the first several tested shifts. This supports the sign-cone formulation but is not evidence sufficient for an all-\(n\) theorem.

## 5. Three parallel closure attacks

### A. Theta-kernel SOS attack

Insert
\[
\gamma_m=8\frac{m!}{(2m)!}M_m,
\qquad
M_m=\int_0^\infty\Phi(u)u^{2m}\,du,
\]
into \(u,v,w,z\). Clear all positive factorial denominators and seek an exact multiple-integral representation of \(\widetilde Q_d\) whose integrand is a sum of squares times the explicit theta kernel factors.

The target is not merely positivity of \(M_m\). It is a signed identity for the precise Jensen/Hermite combination.

### B. Ratio/recurrence attack

Define consecutive ratios
\[
R_m=\gamma_{m+1}/\gamma_m.
\]
Then
\[
v=R_{m-1}(R_m-R_{m-1}),
\]
up to the corresponding normalization convention, and \(w,z\) can be rewritten entirely in finite differences of consecutive ratios. The objective is to derive explicit bounds on the ratio curvature and higher finite differences from the theta kernel.

### C. Global Laguerre–Pólya attack

Instead of proving each Hermite minor separately, prove directly that
\[
G(z)=8\xi\!\left(\frac12+z\right)
\]
belongs to the Laguerre–Pólya class. Any such proof must be unconditional; asymptotic Jensen hyperbolicity alone is insufficient because infinitely many finite-degree/finite-shift cases remain.

## 6. Hard closure lemma

The current bottleneck can now be stated as a single explicit theorem candidate:

\[
\boxed{
\forall n\ge0,\ d\ge3:
\quad
6(d-1)(-v)^3
\ge
3(d-2)w^2+2(d-3)(-v)z,
}
\]
with \(v,w,z\) formed from the actual normalized Riemann-xi coefficients.

Proving this lemma would establish the entire third Hermite-minor layer. It would still not by itself prove RH: all higher Hermite minors (or an equivalent global LP theorem) would remain.

## 7. No false closure

The exact status is therefore:

- the algebraic reduction is rigorous;
- the ordinary Stieltjes shortcut is ruled out;
- the degree-3 obstruction has a new exact sign-cone form;
- numerical reconnaissance supports, but does not prove, the required sign pattern;
- the universal Hermite/LP closure remains open.

A complete RH proof may be claimed only after an unconditional all-degree closure theorem is supplied and independently checked.
