# Frontier 99 — factorial-ratio correction in the degree-two modular gate

Date: 2026-09-16

## Critical audit

The degree-two kernel used in Frontier 97 was
\[
K_n(y_1,y_2)=c_{n+1}^2y_1y_2-\frac{c_nc_{n+2}}2(y_1^2+y_2^2),
\qquad c_k=\frac{2k+1}{k!}.
\]

Frontier 97 stated
\[
\frac{c_{n+1}^2}{c_nc_{n+2}}
=\frac{(2n+3)^2}{(2n+1)(2n+5)}.
\]
This is algebraically incorrect because the factorials do not cancel completely.

The exact ratio is
\[
\boxed{
R_n:=\frac{c_{n+1}^2}{c_nc_{n+2}}
=\frac{(n+2)(2n+3)^2}{(n+1)(2n+1)(2n+5)}
=1+\frac{4n^2+16n+13}{(n+1)(2n+1)(2n+5)}.
}
\]
In particular
\[
R_0=\frac92,
\qquad
R_n=1+\frac1n+O(n^{-3})\quad(n\to\infty).
\]
Thus the numerical positivity intervals recorded in Frontier 97 are not the intervals for the kernel actually defined there.

## Exact corrected sign decomposition

Set
\[
A_n=c_nc_{n+2},\qquad B_n=c_{n+1}^2.
\]
Then
\[
K_n
=\frac{B_n-A_n}{4}(y_1+y_2)^2
-\frac{B_n+A_n}{4}(y_1-y_2)^2.
\]
Moreover,
\[
B_n-A_n
=\frac{4n^2+16n+13}{(n+1)!(n+2)!}>0.
\]
Hence the kernel is exactly indefinite for every \(n\): one positive square and one negative square.

Equivalently, for \(r=y_1/y_2>0\),
\[
K_n\ge0
\iff
R_n-\sqrt{R_n^2-1}\le r\le R_n+\sqrt{R_n^2-1},
\]
with the corrected \(R_n\) above.

## Integrated interpretation

For a positive measure \(\mu\), write
\[
M_j=\int y^j\,d\mu(y).
\]
Then
\[
\iint K_n(y_1,y_2)d\mu(y_1)d\mu(y_2)
=B_nM_1^2-A_nM_0M_2.
\]
If \(M_0>0\), define \(d\nu=d\mu/M_0\), with mean \(m=E_\nu[y]\) and variance \(\sigma^2=\operatorname{Var}_\nu(y)\). The nonnegativity condition is exactly
\[
\boxed{
\frac{\sigma^2}{m^2}\le R_n-1
=\frac{4n^2+16n+13}{(n+1)(2n+1)(2n+5)}.
}
\]
Therefore the corrected degree-two problem is a theta-specific coefficient-of-variation bound, not a pointwise positivity problem.

## Consequence for the research program

1. The pointwise Gram route remains impossible because \(K_n\) is indefinite.
2. The previously claimed shrinking threshold of order \(n^{-2}\) was an artifact of the factorial-ratio error; the exact threshold is asymptotically \(n^{-1}\).
3. Any subsequent modular/Poisson argument using the Frontier-97 value of \(R_n\), or its numerical intervals, must be recomputed.
4. This correction does **not** prove RH. It removes a false normalization and replaces the degree-two gate with an exact variance inequality that can be tested against the actual theta-induced measure.

**Status: rigorous correction; no RH proof.**
