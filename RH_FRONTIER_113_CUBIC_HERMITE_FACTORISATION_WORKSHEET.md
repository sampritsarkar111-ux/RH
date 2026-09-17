# Frontier 113 — Cubic Hermite factorisation worksheet

Date: 2026-09-17

## Exact algebra

For \(J(X)=\gamma_0+3\gamma_1X+3\gamma_2X^2+\gamma_3X^3\), set

\[
a=3\gamma_2/\gamma_3,\qquad b=3\gamma_1/\gamma_3,\qquad c=\gamma_0/\gamma_3.
\]

The Hermite matrix is

\[
H_3=\begin{pmatrix}
3&-a&a^2-2b\\
-a&a^2-2b&-a^3+3ab-3c\\
a^2-2b&-a^3+3ab-3c&a^4-4a^2b+2b^2+4ac
\end{pmatrix}.
\]

Its determinant is

\[
\det H_3=-4a^3c+a^2b^2+18abc-4b^3-27c^2.
\]

Equivalently,

\[
\det H_3=-\frac{27}{\gamma_3^4}\left(\gamma_0^2\gamma_3^2-6\gamma_0\gamma_1\gamma_2\gamma_3+4\gamma_0\gamma_2^3+4\gamma_1^3\gamma_3-3\gamma_1^2\gamma_2^2\right).
\]

## Shifted theta form

Replace \(\gamma_j\) by \(\gamma_{n+j}=M_{n+j}/(2n+2j)!\). The resulting inequality is a rational polynomial in \(M_n,M_{n+1},M_{n+2},M_{n+3}\) and factorials.

## Research target

Determine whether the exact shifted expression admits a finite multi-copy integral representation whose kernel has an exact Binet–Cauchy/Vandermonde sum-of-squares decomposition. If yes, derive it symbolically. If no, identify the first exact negative principal minor or other obstruction and record it as an ansatz failure.

## Guardrail

A positive moment measure does not by itself imply cubic hyperbolicity. Any proposed certificate must prove the complete Hermite criterion for the cubic and then generalize uniformly to all degrees.
