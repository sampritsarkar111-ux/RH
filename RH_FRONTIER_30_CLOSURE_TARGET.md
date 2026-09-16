# Frontier 30 — Global Closure Target for the Jensen Program

## Purpose

Frontier 29 reduced the missing RH implication to exact nonlinear inequalities for tilted theta moments. The present step isolates the remaining global regime and specifies a non-circular closure theorem that would actually imply RH.

## 1. Exact target

Let
\[
\xi(1/2+z)=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n},
\qquad
J^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j.
\]

By the Jensen-Pólya equivalence, RH is equivalent to hyperbolicity of every \(J^{d,n}\). Thus the proof target is
\[
\boxed{\forall d,n\ge0,\quad J^{d,n}\text{ has only real zeros}.}
\]

## 2. Current global information

A recent 2026 result proves hyperbolicity in a large asymptotic wedge of the \((d,n)\)-plane: there is an absolute constant \(K>0\) such that
\[
n^3\log^2(n+2)\ge Kd^5
\quad\Longrightarrow\quad
J^{d,n}\text{ is hyperbolic}.
\]

Therefore any genuinely new proof must control the complementary region
\[
\boxed{d^5>K^{-1}n^3\log^2(n+2).}
\]

This is not a proof of RH: the complementary region remains unbounded in both parameters.

## 3. New closure formulation

For each \((d,n)\), form the monic polynomial \(P_{d,n}\) obtained from \(J^{d,n}\). Let \(H_{d,n}\) denote its Hermite matrix. Hyperbolicity is equivalent to
\[
H_{d,n}\succeq0.
\]

A sufficient global theorem is therefore the existence of an exact decomposition
\[
\boxed{
H_{d,n}=A_{d,n}^{\mathsf T}A_{d,n}+R_{d,n},
\qquad R_{d,n}\succeq0,
}
\]
where every entry of \(A_{d,n}\) and \(R_{d,n}\) is an explicit expression in the theta moments, with no dependence on the unknown zeros.

The key non-circular requirement is that positivity of \(R_{d,n}\) must follow from an independently proved inequality for the Riemann theta kernel.

## 4. Moment-kernel route

Write
\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},\qquad M_n=\int_0^\infty u^{2n}\Phi(u)\,du,
\]
and \(Y=u^2\). Then
\[
\mathbb E_{\nu_n}[Y^k]=M_{n+k}/M_n.
\]

Every coefficient of \(H_{d,n}\) is consequently a rational polynomial in finitely many moments of \(Y\). The missing theorem can be sought in the form
\[
\boxed{
Q_{d,n}(c_0,\ldots,c_r)
=\int_0^\infty\!\!\int_0^\infty
\mathcal K_{d,n}(u,v;c)\,\mathcal K_{d,n}(u,v;c)^{\mathsf T}
\,d\nu_n(u)d\nu_n(v)
}
\]
for every principal-minor polynomial \(Q_{d,n}\), or by a finite sum of such PSD integral terms.

## 5. Falsification conditions

Any proposed closure identity is invalid if it:

1. assumes RH or Laguerre-Pólya membership;
2. assumes hyperbolicity of the Jensen polynomial;
3. defines the measure from the unknown zeros;
4. establishes only fixed degree or fixed derivative order;
5. replaces exact inequalities by floating-point tests;
6. proves only the already-known asymptotic wedge.

## 6. Immediate research task

The next concrete algebraic test is degree 4 and degree 5 in the complementary scaling regime. Compute the exact Hermite principal minors symbolically as rational functions of \(M_n,\ldots,M_{n+d}\), factor them, and determine whether their numerators admit a representation as sums/integrals of manifestly nonnegative theta-kernel expressions.

A successful factorization would provide a reusable template for arbitrary \(d\). Failure is equally useful: it identifies the first obstruction that a global theorem must overcome.

## Status

This frontier is a rigorous research target and a reduction, not a proof of RH. No claim of a complete RH proof is made until every \((d,n)\) case is covered by a theorem with all implications proved.
