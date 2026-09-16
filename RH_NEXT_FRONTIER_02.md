# Riemann Hypothesis — Frontier 02: Coefficient/LP Stress Test

Date: 2026-09-16

## Objective

Continue from `RH_NEXT_FRONTIER.md` by attacking the Laguerre–Pólya route through the Maclaurin data of

\[
\Xi(t)=\xi(1/2+it).
\]

RH is equivalent to all zeros of the real entire function \(\Xi\) being real.

## 1. Exact structural expansion

Because \(\Xi\) is real and even,

\[
\Xi(t)=\sum_{n\ge0}(-1)^n a_n t^{2n}.
\]

The first coefficients, evaluated to high precision as a diagnostic, are

\[
\begin{aligned}
a_0&\approx0.4971207781883141099,\\
a_1&\approx0.01148597215757271877,\\
a_2&\approx1.234520180703180069\times10^{-4},\\
a_3&\approx8.323554813855270720\times10^{-7},\\
a_4&\approx3.992226551344137174\times10^{-9},\\
a_5&\approx1.461602576011096092\times10^{-11},\\
a_6&\approx4.274540045536844958\times10^{-14},\\
a_7&\approx1.030962613461805656\times10^{-16}.
\end{aligned}
\]

These numbers are consistent with the expected alternating Maclaurin signs, but finite coefficient evidence is not a proof of RH.

## 2. A necessary-condition attack that survives the first test

For \(n=1,\ldots,5\), the computed ratios

\[
R_n=\frac{a_n^2}{a_{n-1}a_{n+1}}
\]

are greater than one. Numerically,

\[
\log R_1\approx0.7653,\quad
\log R_2\approx0.4663,\quad
\log R_3\approx0.3406,\quad
\log R_4\approx0.2701,\quad
\log R_5\approx0.2246.
\]

Thus the coefficient sequence passes the initial log-concavity test.

### Critical obstruction

Log-concavity of \((a_n)\) is **not sufficient** for the Laguerre–Pólya property. Therefore the implication

\[
a_n>0\ \&\ a_n^2\ge a_{n-1}a_{n+1}\quad\forall n
\quad\Longrightarrow\quad RH
\]

cannot be used without a new theorem adding substantially stronger structure.

## 3. Stronger target: a zero-location coefficient theorem

Set

\[
F(w)=\frac{\Xi(\sqrt w)}{\Xi(0)}
      =\sum_{n\ge0}(-1)^n b_n w^n,
\qquad b_n=\frac{a_n}{a_0}.
\]

If RH holds, then formally the canonical product has the shape

\[
F(w)=\prod_{\gamma>0}\left(1-\frac{w}{\gamma^2}\right),
\]

with the appropriate canonical-product convergence factors understood from the growth of \(\Xi\).

This identifies a more precise target than ordinary log-concavity:

> Find a directly provable infinite-dimensional positivity/total-positivity condition on the normalized coefficient array \((b_n)\) that forces every zero of \(F\) to lie on \((0,\infty)\).

Such a theorem would imply that every zero of \(\Xi(t)\) is real.

## 4. Immediate falsification of one naive strengthening

The Hankel matrices \(H_k=(b_{i+j})_{0\le i,j\le k}\) are **not** positive semidefinite at the first levels. Numerically,

\[
\det H_1\approx-2.8550665307\times10^{-4},
\]

and

\[
\det H_2\approx-1.1969305654\times10^{-12}.
\]

Therefore ordinary Stieltjes-moment positivity of \((b_n)\) is not the right certificate.

This is useful negative information: a proof cannot simply assert that the Maclaurin coefficients form a positive moment sequence.

## 5. New research direction: Jensen hyperbolicity in the even variable

The next rigorous target is the Jensen-polynomial criterion applied to

\[
F(w)=\Xi(\sqrt w)/\Xi(0).
\]

For each degree \(d\) and shift \(m\), construct the normalized Jensen polynomial from the Taylor coefficients of \(F\). The decisive theorem to establish would have the form

\[
\boxed{
\text{All required Jensen polynomials are hyperbolic with the correct zero sign}
\ \Longrightarrow\ 
F\text{ has only positive real zeros}
}
\]

under the exact order/growth hypotheses satisfied by \(\Xi\).

The word **all** is essential: checking any finite set of Jensen polynomials can only be computational evidence.

## 6. Proof-engineering requirement

A successful continuation must prove, rather than assume, each of the following:

1. the exact Jensen normalization;
2. hyperbolicity for every degree and shift;
3. the sign/location condition needed to convert real zeros of \(F\) into real zeros of \(\Xi\);
4. the limiting theorem taking finite Jensen information to the full entire function;
5. all convergence and growth hypotheses;
6. no step may use RH, GRH, a zero-location statement, or an equivalent criterion as an assumption.

## 7. Current status of this frontier

This file records genuine progress by eliminating two tempting but insufficient coefficient routes:

- coefficient log-concavity alone;
- ordinary Hankel/Stieltjes moment positivity of the Maclaurin coefficients.

No complete proof of RH has been established in this iteration. The next concrete task is to derive the exact Jensen family for \(F(w)\), search for a universal hyperbolicity mechanism, and prove every implication rather than relying on finite computation.
