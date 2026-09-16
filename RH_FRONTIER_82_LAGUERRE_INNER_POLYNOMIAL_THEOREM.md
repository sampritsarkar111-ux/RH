# Frontier 82 — Laguerre inner-polynomial theorem and exact mixing obstruction

Date: 2026-09-16

## Result

The exact beta-corrected theta representation reduces each Jensen polynomial to a positive theta-measure mixture of a finite polynomial \(q_{n,d}\). The finite polynomial itself is provably real-rooted by a Laguerre/logarithmic-derivative argument. The remaining RH-hard step is therefore isolated to the theta/beta mixing operator.

## Exact reduction

With \(y=x(1-x)u^2\), the canonical coefficients have the exact form
\[
\gamma_m=\int y^m\frac{2m+1}{m!}\,d\mu(y),
\]
so
\[
J_{d,n}(X)=\int y^n q_{n,d}(yX)\,d\mu(y),
\]
where
\[
q_{n,d}(t)=\sum_{j=0}^d\binom dj\frac{2(n+j)+1}{(n+j)!}t^j.
\]
No RH assumption is used.

Define
\[
p_{n,d}(t)=\sum_{j=0}^d\binom dj\frac{t^j}{(n+j)!}
=\frac{d!}{(n+d)!}L_d^{(n)}(-t).
\]
Then
\[
q_{n,d}(t)=(2n+1)p_{n,d}(t)+2t p'_{n,d}(t)
\]
and therefore
\[
q_{n,d}(t)=\frac{d!}{(n+d)!}\left[(2n+1)L_d^{(n)}(-t)-2t(L_d^{(n)})'(-t)\right].
\]

## Finite hyperbolicity theorem

The zeros \(r_1>\cdots>r_d\) of \(p_{n,d}\) are simple and negative. For \(t\ne r_i\),
\[
\frac{q_{n,d}(t)}{p_{n,d}(t)}
=(2n+1)+2\sum_{i=1}^d\frac{t}{t-r_i}.
\]
Its derivative is
\[
2\sum_{i=1}^d\frac{-r_i}{(t-r_i)^2}>0.
\]
The ratio runs from \(+\infty\) to \(-\infty\) across each pole and has one zero in each gap between consecutive roots of \(p_{n,d}\). On the rightmost interval it crosses once before \(0\), while it is positive for \(t>0\). Hence
\[
\boxed{q_{n,d}\text{ has exactly }d\text{ simple negative zeros for every }n,d\ge0.}
\]
The zeros interlace those of \(p_{n,d}\). This theorem is unconditional.

## Exact remaining gap

The implication
\[
q_{n,d}\text{ hyperbolic}
\Longrightarrow
\int y^n q_{n,d}(yX)\,d\mu(y)\text{ hyperbolic}
\]
is not automatic: arbitrary positive mixtures of real-rooted dilates need not preserve real-rootedness.

Thus the remaining proof-bearing target is exactly
\[
\boxed{
\mathcal M_n[p](X):=\int y^n p(yX)\,d\mu(y)
\text{ must be shown to preserve hyperbolicity on the family }q_{n,d},\ \forall n,d.
}
\]
A theta-specific total-positivity, variation-diminishing, modular-pairing, SOS/Hermite, or equivalent PF-infinity theorem proving this would close the Jensen route and then invoke the exact Jensen-to-RH equivalence.

## Status

This is a rigorous partial advance and a sharper localization of the global obstruction. It is **not** a proof of RH.
