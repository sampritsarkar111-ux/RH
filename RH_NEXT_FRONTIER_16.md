# Riemann Hypothesis — Frontier 16: Canonical Jensen Normalization Audit

Date: 2026-09-16

## Objective

Audit the 2026 finite-strip Jensen-polynomial obstruction against the exact Pólya–Jensen normalization for the Riemann xi function.

## 1. Canonical coefficient sequence

Let
\[
\Xi(t):=\xi\!\left(\tfrac12+it\right)
=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n},
\]
where, for the standard positive theta kernel,
\[
M_n=\int_0^\infty \Phi(u)u^{2n}\,du>0.
\]
Putting \(t=-iz\) gives
\[
\xi\!\left(\tfrac12+z\right)
=\sum_{n\ge0}\frac{M_n}{(2n)!}z^{2n}.
\]
The Pólya–Jensen normalization used by Griffin–Ono–Rolen–Zagier is
\[
G(z):=8\xi\!\left(\tfrac12+z\right)
=\sum_{n\ge0}\frac{\gamma(n)}{n!}z^{2n}.
\]
Therefore coefficient comparison gives the exact identity
\[
\boxed{\gamma(n)=8\frac{n!}{(2n)!}M_n.}
\]
This factorial multiplier is essential.

The RH-equivalent Jensen polynomials are therefore
\[
\boxed{J_{d,n}(X)=\sum_{j=0}^d\binom dj\,8\frac{(n+j)!}{(2n+2j)!}M_{n+j}X^j.}
\]
Multiplying the whole polynomial by one nonzero scalar is harmless; multiplying each coefficient by a different \(j\)-dependent factorial factor is not.

## 2. Degree-2 consequence

For
\[
J_{2,n}(X)=\gamma(n)+2\gamma(n+1)X+\gamma(n+2)X^2,
\]
hyperbolicity is equivalent to
\[
\gamma(n+1)^2\ge\gamma(n)\gamma(n+2).
\]
Substitution of the exact normalization yields
\[
\boxed{M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.}
\]
This is the correct degree-2 moment inequality.

By contrast, using \(M_n\) directly as the Jensen coefficient gives the false target
\[
M_{n+1}^2\ge M_nM_{n+2},
\]
which is opposite to the generic Cauchy–Schwarz log-convexity inequality
\[
M_{n+1}^2\le M_nM_{n+2}.
\]

## 3. Audit of the 2026 finite-strip paper

The 2026 paper *Asymptotic Hyperbolicity of Jensen Polynomials and the Finite-Strip Obstruction to the Riemann Hypothesis* writes
\[
\Xi(t)=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n}
\]
and then identifies the standard Jensen coefficient with \(\gamma(n)=M_n\). That identification omits the conversion from ordinary Taylor coefficients to the exponential-generating coefficient sequence \(\gamma(n)/n!\).

The paper's own quadratic computation then gives
\[
\operatorname{Disc}(J_{2,n})=4(M_{n+1}^2-M_nM_{n+2})<0
\]
by Cauchy–Schwarz for all \(n\). In the same discussion it cites the established GORZ result that the canonical degree-2 Jensen polynomials are hyperbolic for all shifts. These statements cannot simultaneously concern the same coefficient sequence.

Hence the finite-strip obstruction in that paper is not a valid obstruction for the canonical RH-equivalent Pólya–Jensen family unless the missing factorial renormalization is restored and every later theorem is re-proved for that corrected family.

## 4. Consequence for our RH program

The canonical Jensen route remains
\[
\mathrm{RH}\iff J_{d,n}\text{ is hyperbolic for every }d,n\ge0
\]
with
\[
\gamma(n)=8\frac{n!}{(2n)!}M_n.
\]
The 2026 simultaneous wedge
\[
n^3\log^2(n+2)\ge Kd^5
\Longrightarrow J_{d,n}\text{ hyperbolic}
\]
uses the canonical \(\gamma(n)\) normalization and remains relevant.

The unresolved set is its infinite complement. A proof of RH still requires a rigorous theorem covering every remaining pair \((d,n)\), or an independent proof that \(G\) lies in the Laguerre–Pólya class.

## Status

This frontier removes a misleading 2026 obstruction by an exact normalization check. It is genuine progress in proof hygiene, but it is not a proof of RH. The all-degree/all-shift hyperbolicity theorem remains to be proved.
