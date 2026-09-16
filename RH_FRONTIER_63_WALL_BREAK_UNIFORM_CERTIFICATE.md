# Frontier 63 — breaking the global wall: remove the circular PF∞ gate

## Executive result

The previous Frontier-62 bottleneck was stated as a theta-specific PF∞ / variation-diminishing certificate for the Fourier kernel of Xi. That gate is **too strong as an independent research target**: an infinite-order Pólya-frequency certificate for the relevant transform would already force the transformed entire function into the real Laguerre–Pólya class, and hence would contain essentially the whole RH conclusion.

So the wall is not merely “prove PF∞.” The correct non-circular wall is:

\[
\boxed{\text{construct a theta-specific, uniform, non-circular certificate for every Jensen degree and shift.}}
\]

This is a sharper target because it separates a genuinely theta/arithmetic inequality from the abstract closure theorem that is equivalent to RH.

## 1. Exact logical chain

Let
\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]
with Xi real and even entire. Write
\[
\xi\!\left(\frac12+z\right)=\sum_{n\ge0}\frac{\gamma_n}{n!}z^{2n},
\qquad
J^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]

Pólya's criterion gives the equivalence
\[
RH\iff J^{d,n}\text{ is hyperbolic for every }d,n\ge0.
\]
This equivalence is documented in Griffin–Ono–Rolen–Thorner–Tripp and is not itself a proof of RH.

## 2. What the recent asymptotic theorem actually removes

Recent work gives a simultaneous sufficient region of the form
\[
n^3\log^2(n+2)\ge Kd^5
\quad\Longrightarrow\quad
J^{d,n}\text{ hyperbolic},
\]
for an absolute constant K.

Therefore the unresolved Jensen domain is contained in the complementary wedge
\[
\boxed{n^3\log^2(n+2)<Kd^5.}
\]

This is a genuine reduction, but the wedge is still infinite. No finite numerical verification can close it.

## 3. Why the old PF∞ target was circular in spirit

A theorem saying that the exact theta-derived kernel belongs to PF∞, together with a standard real-zero-preserving Fourier/convolution theorem, would imply that Xi belongs to the Laguerre–Pólya class. That would imply that all zeros of Xi are real, i.e. RH.

Thus PF∞ is a possible *form* of a proof, but it cannot be treated as an intermediate fact that is somehow weaker than RH unless its theta-specific certificate is independently derived from identities that do not assume real-zero information.

The research program therefore rejects the following invalid inference:

\[
\text{positive theta moments}
\;\not\Rightarrow\;
\text{PF∞}
\;\not\Rightarrow\;
RH.
\]

In particular, the project's earlier Stieltjes-moment route is insufficient: the exact third Hermite obstruction has a sign structure that ordinary Hankel positivity does not control.

## 4. New non-circular target: a uniform Jensen certificate

For every n,d, construct an explicit identity
\[
\mathcal H_{d,n}
=
\sum_{\alpha\in A_{d,n}} C_{\alpha}(n,d)\,\mathcal I_{\alpha}(n,d),
\]
where:

1. \(\mathcal H_{d,n}\) is a complete hyperbolicity certificate (e.g. a Hermite determinant / Sturm certificate, or a finite set of equivalent inequalities) for \(J^{d,n}\);
2. every coefficient \(C_{\alpha}(n,d)\) is explicitly nonnegative;
3. every integral/sum \(\mathcal I_{\alpha}\) is explicitly nonnegative from theta identities alone;
4. all interchanges of sums and integrals are justified by absolute convergence;
5. no statement about zeros of Xi, Xi derivatives, or Jensen polynomials is used on the right-hand side.

The crucial word is **uniform**: the identity must work for all \(n,d\), not only fixed degree or asymptotic regions.

## 5. Exact first obstruction that the certificate must defeat

For the factorial-weighted theta moments used by the project, normalize consecutive moments by
\[
r_j=\frac{q_j}{q_0},\qquad
 a=r_1,\quad
 v=r_2-a^2,
\]
\[
w=r_3-3ar_2+2a^3,
\qquad
z=r_4-4ar_3+6a^2r_2-3a^4.
\]
Then the degree-three Hermite obstruction reduces exactly to
\[
\widetilde Q_d
=
2(d-3)vz-3(d-2)w^2-6(d-1)v^3,
\]
with the positive external factor
\[
\Delta_3
=\frac{d^3(d-1)^2(d-2)}{12}\widetilde Q_d.
\]
At \(d=3\),
\[
\widetilde Q_3=-3w^2-12v^3.
\]
Therefore a naive argument based only on \(v\ge0\) from Stieltjes positivity points in the wrong direction. Any successful certificate must exploit the factorial weights and the precise theta structure.

## 6. Zero-mode correction is mandatory

The nonzero theta tail is
\[
\theta_*(t)=2\sum_{m\ge1}e^{-\pi m^2t}.
\]
Under \(t=e^x\), define
\[
\rho_+(x)=e^{x/4}\theta_*(e^x).
\]
Jacobi inversion gives the exact defect
\[
\rho_+(-x)-\rho_+(x)=2\sinh(x/4).
\]
Hence the corrected even object is
\[
\rho_0(x)=\rho_+(x)-\sinh(x/4),
\qquad
\rho_0(-x)=\rho_0(x).
\]
Any whole-line positivity argument must use this corrected object or an exactly equivalent formulation. The earlier uncorrected full-theta measure route is closed as invalid.

## 7. Three remaining non-circular routes

### Route A — exact factorial-weighted kernel SOS

Insert the exact theta representation of each \(q_{n+j}\) into the Hermite form and search for a finite sum-of-squares kernel identity whose coefficients are polynomial/rational functions of \(n,d\).

This route directly attacks the obstruction and does not ask for PF∞ first.

### Route B — finite-order total positivity with degree-dependent order

Instead of proving PF∞ in one step, prove precisely the finite-order determinant required for degree d, with a bound uniform in n. The theorem needed is of the form
\[
\det[K(x_i,y_j)]_{i,j=1}^r\ge0
\quad (r\le R(d)),
\]
with \(R(d)\) exactly sufficient for hyperbolicity of \(J^{d,n}\).

This is strictly more targeted than PF∞ and leaves open only the determinant order actually required.

### Route C — wedge elimination

Combine the explicit large-\(n\)/degree region with an exact monotonicity or multiplier theorem that propagates hyperbolicity from a controlled boundary of the unresolved wedge toward all smaller shifts. A valid propagation theorem must be proved; numerical continuation is not enough.

## 8. Permanent gap-closure checklist

A future claimed proof is rejected unless it supplies all of:

- exact definition and normalization of Xi;
- exact theta representation;
- zero-mode correction;
- absolute convergence;
- legal differentiation/integration interchange;
- exact sign of every kernel term;
- a global or degree-uniform positivity certificate;
- proof that the certificate implies hyperbolicity;
- proof for every remaining n,d, not merely asymptotically;
- final Pólya equivalence back to RH;
- no circular use of RH, real zeros, Newman constant \(\Lambda\le0\), or an already-equivalent all-Jensen theorem.

## Status

**Major structural refinement, not an RH proof.**

The actual mathematical wall has been narrowed from “some mysterious global positivity theorem” to a concrete requirement: produce a theta-specific, non-circular, uniform certificate over the complementary Jensen wedge. The PF∞ gate is retained only as a possible final mechanism, not as an assumed intermediate theorem.
