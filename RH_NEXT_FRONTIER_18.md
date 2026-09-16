# RH NEXT FRONTIER 18 — Canonical coefficient-transform attack

Date: 2026-09-16

## Objective

Attempt a genuinely global proof of the Riemann Hypothesis through the canonical Pólya–Jensen sequence, rather than adding another finite numerical check.

The Riemann Hypothesis (RH) is currently still open.

## 1. Canonical entire function and Jensen sequence

Let
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(t)=\xi(1/2+it).
\]
Write
\[
\Xi(t)=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n}.
\]
Then
\[
8\xi(1/2+z)=\sum_{n\ge0}\frac{\gamma_n}{n!}z^{2n},
\qquad
\boxed{\gamma_n=8\frac{n!}{(2n)!}M_n}.
\]
The canonical Jensen polynomials are
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
Pólya–Jensen gives the exact RH equivalence: all these polynomials must be hyperbolic for every degree and shift.

## 2. Exact coefficient transform

Set
\[
a_n=\frac{n!}{(2n)!}=\frac{1}{4^n(1/2)_n}.
\]
Then
\[
\gamma_n=8a_nM_n.
\]
The quadratic condition is
\[
\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}
\iff
\boxed{M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}}.
\]
Also
\[
\frac{a_{n+1}^2}{a_na_{n+2}}=\frac{2n+3}{2n+1}>1.
\]

## 3. Beta-integral representation

The beta identity gives
\[
\frac{n!}{(2n)!}
=\frac{2n+1}{n!}\int_0^1[x(1-x)]^n\,dx.
\]
Thus, for a positive moment representation \(M_n=\int u^n\,d\mu(u)\), one obtains formally
\[
\gamma_n
=8\frac{2n+1}{n!}
\int_0^1\int_0^\infty[ux(1-x)]^n\,d\mu(u)\,dx.
\]
The prefactor depends on \(n\), so this does not turn \(\gamma_n\) into an ordinary fixed positive moment sequence. Hence Stieltjes positivity alone cannot close the Jensen problem.

## 4. New exact multiplier-sequence result

There is, however, a useful structural fact about the factorial multiplier itself.

Its exponential generating function is
\[
\sum_{n=0}^{\infty}a_n\frac{x^n}{n!}
=\sum_{n=0}^{\infty}\frac{x^n}{(2n)!}
=\cosh(\sqrt{x}).
\]
Equivalently, after the even-variable substitution \(x=z^2\), this is \(\cosh z\), an entire Laguerre–Pólya function with only real zeros after the standard imaginary-axis sign convention. More directly for the multiplier-sequence test, use the signed sequence \((-1)^na_n\), whose exponential generating function is
\[
\sum_{n=0}^{\infty}(-1)^na_n\frac{x^n}{n!}
=\cos(\sqrt{x}),
\]
which has only real zeros in \(x\). Therefore \((-1)^na_n\) is a classical Pólya–Schur multiplier sequence; equivalently, \(a_n\) is a multiplier sequence up to the harmless alternating-sign transform.

This is a real structural fact, but it does **not** solve RH. The reason is exact: the known function is
\[
8\xi(1/2+z)=\sum_n 8a_nM_n\frac{z^{2n}}{n!},
\]
so the multiplier acts on the exponential generating function
\[
B(w)=\sum_n M_n\frac{w^n}{n!},
\]
whereas the available theta expansion gives
\[
\xi(1/2+z)=\sum_n M_n\frac{z^{2n}}{(2n)!}.
\]
We do not have a proof that \(B\) belongs to the Laguerre–Pólya class. Establishing that missing bridge would be a genuinely new route to RH.

## 5. Exact higher-degree target

The unresolved global statement is
\[
\boxed{
J_{d,n}(X)=\sum_{j=0}^d\binom dj
8\frac{(n+j)!}{(2n+2j)!}M_{n+j}X^j
\text{ is hyperbolic for every }d,n\ge0.
}
\]

Degree 2 is only the first necessary condition. Generic moment positivity, finite computation, or fixed-degree asymptotics cannot replace the all-\(d\), all-\(n\) quantifier.

## 6. De Bruijn–Newman cross-check

For
\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\]
the de Bruijn–Newman constant \(\Lambda\) satisfies: all zeros are real exactly for \(t\ge\Lambda\), RH implies \(\Lambda\le0\), and Rodgers–Tao proved \(\Lambda\ge0\). Thus this route needs the exact boundary conclusion \(\Lambda=0\).

No proof of that final equality was obtained here.

## 7. Literature checkpoint

Known work proves eventual Jensen hyperbolicity for each fixed degree. A 2026 preprint by Jonathan Holland gives the simultaneous sufficient region
\[
n^3\log^2(n+2)\ge Kd^5\Longrightarrow J_{d,n}\text{ hyperbolic},
\]
but this still leaves a complementary region. It therefore does not establish RH.

## 8. What this frontier genuinely adds

1. Exact canonical normalization and degree-2 condition.
2. Exact beta representation showing why ordinary positive-moment arguments fail.
3. A new multiplier-sequence observation: the factorial multiplier is Pólya–Schur after the alternating-sign transform because its exponential generating function is \(\cos(\sqrt{x})\).
4. A precise reformulation of the missing bridge: prove the associated exponential generating function \(B(w)=\sum M_nw^n/n!\) has the required Laguerre–Pólya structure, or derive an equivalent direct hyperbolicity theorem.

## 9. Non-claim

This document does **not** claim a proof of RH. The final global zero-location step remains open and is stated explicitly so future work cannot accidentally hide the missing quantifier.
