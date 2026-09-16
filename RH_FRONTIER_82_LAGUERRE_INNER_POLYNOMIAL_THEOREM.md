# Frontier 82 — Laguerre inner-polynomial theorem and exact mixing obstruction

Date: 2026-09-16

## Purpose

Use the exact beta-corrected theta representation from Frontier 80 at the level of a fixed Jensen degree/shift. The goal is to separate the finite algebraic factor from the theta measure and determine exactly which part is already hyperbolic and which part remains RH-hard.

## 1. Exact positive-measure form

Write the canonical coefficients as
\[
\gamma_m=\int y^m\,d\mu(y)\,\frac{2m+1}{m!},
\]
where \(d\mu\) is the positive measure induced by the theta kernel together with the beta variable \(x\in(0,1)\), with
\[
y=x(1-x)u^2.
\]
The representation is exact and the measure is independent of the Jensen shift/degree.

For fixed \(n,d\),
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j
\]
becomes
\[
\boxed{
J_{d,n}(X)=\int y^n q_{n,d}(yX)\,d\mu(y),
}\]
where
\[
q_{n,d}(t)=\sum_{j=0}^d\binom dj\frac{2(n+j)+1}{(n+j)!}t^j.
\]

No RH assumption is used in this identity.

## 2. Closed Laguerre form

Define
\[
p_{n,d}(t)=\sum_{j=0}^d\binom dj\frac{t^j}{(n+j)!}.
\]
Using
\[
{}_1F_1(-d;n+1;-t)=\sum_{j=0}^d\binom dj\frac{t^j}{(n+1)_j},
\]
and
\[
\frac1{(n+j)!}=\frac1{n!(n+1)_j},
\]
we obtain
\[
p_{n,d}(t)=\frac1{n!}{}_1F_1(-d;n+1;-t)
=\frac{d!}{(n+d)!}L_d^{(n)}(-t).
\]
Because
\[
q_{n,d}(t)=(2n+1)p_{n,d}(t)+2t\,p'_{n,d}(t),
\]
we have the exact finite polynomial representation
\[
\boxed{
q_{n,d}(t)=\frac{d!}{(n+d)!}
\left[(2n+1)L_d^{(n)}(-t)-2t\,(L_d^{(n)})'(-t)\right].
}
\]

## 3. The inner polynomial is itself hyperbolic

Let the zeros of \(p_{n,d}\) be
\[
r_1>r_2>\cdots>r_d,
\qquad r_i<0.
\]
This follows from the classical fact that \(L_d^{(n)}(x)\) has \(d\) simple positive zeros for \(n>-1\), hence \(L_d^{(n)}(-t)\) has \(d\) simple negative zeros.

For \(t\neq r_i\),
\[
\frac{q_{n,d}(t)}{p_{n,d}(t)}
=(2n+1)+2t\frac{p'_{n,d}(t)}{p_{n,d}(t)
}
=(2n+1)+2\sum_{i=1}^d\frac{t}{t-r_i}.
\]
On every pole-free interval,
\[
\frac{d}{dt}\left(\frac{q_{n,d}}{p_{n,d}}\right)
=2\sum_{i=1}^d\frac{-r_i}{(t-r_i)^2}>0,
\]
because \(r_i<0\). Thus the logarithmic-ratio function is strictly increasing between consecutive roots of \(p_{n,d}\).

At an interior pole \(r_i\),
\[
\lim_{t\to r_i^-}\frac{q}{p}=+\infty,
\qquad
\lim_{t\to r_i^+}\frac{q}{p}=-\infty.
\]
Hence there is exactly one zero of \(q\) in each interval \((r_{i+1},r_i)\).

On the rightmost interval \((r_1,\infty)\), the ratio tends to \(-\infty\) at \(r_1^+\) and to \(2n+1+2d>0\) as \(t\to+\infty\), so there is exactly one further zero. For \(t>0\), every summand \(t/(t-r_i)\) is positive, so the ratio is strictly positive; therefore that final zero lies in \((r_1,0)\).

There are therefore exactly \(d\) simple real zeros, all negative:
\[
\boxed{q_{n,d}\text{ is hyperbolic with strictly negative zeros, for every }n,d\ge0.}
\]
Moreover its zeros interlace those of \(p_{n,d}\).

This is an unconditional theorem and does not assume RH.

## 4. Exact remaining RH obstruction

The Jensen polynomial is not \(q_{n,d}\); it is the positive theta-measure mixture
\[
J_{d,n}(X)=\int y^n q_{n,d}(yX)\,d\mu(y).
\]
Although every individual dilate \(q_{n,d}(yX)\) is hyperbolic for \(y>0\), an arbitrary positive mixture of such dilates need not remain hyperbolic. Consequently the pointwise Laguerre theorem does **not** by itself prove RH.

The exact missing statement is now:
\[
\boxed{
\text{The specific theta/beta mixing operator }
\mathcal M_n[p](X):=\int y^n p(yX)\,d\mu(y)
\text{ preserves hyperbolicity on the family }q_{n,d},\ \forall n,d.
}
\]
A theorem of this form, proved directly from the theta kernel/modular symmetry and without assuming any zero-location result, would imply the full Jensen hyperbolicity theorem.

## 5. What this excludes

This frontier invalidates the shortcut
\[
q_{n,d}\text{ hyperbolic}\quad\Longrightarrow\quad J_{d,n}\text{ hyperbolic},
\]
because the mixing step is nontrivial. It also shows exactly where a future SOS, total-positivity, or variation-diminishing theorem must act: on \(\mathcal M_n\), not on the finite Laguerre polynomial itself.

## 6. Next proof-bearing target

Prove one of the following, uniformly in \(n,d\):

1. \(\mathcal M_n\) is a hyperbolicity-preserver on the Laguerre-derived cone containing all \(q_{n,d}\);
2. the kernel \((y,X)\mapsto q_{n,d}(yX)\) admits a theta-specific total-positivity/variation-diminishing theorem;
3. modular pairing converts \(\mathcal M_n[q_{n,d}]\) into a manifestly real-rooted polynomial or a positive sum of interlacing-preserving transforms;
4. an equivalent all-degree Hermite/PF∞ certificate is derived directly for the mixed polynomial.

Without one of these global mixing theorems, this frontier remains a rigorous partial result, not a proof of RH.
