# RH Frontier 122 — Exact Cubic Triple-Integrand and Vandermonde-Square Obstruction

Date: 2026-09-16

## 1. Triple-product expansion

Write
\[
\gamma_n=\frac{M_n}{(2n)!},\qquad M_n=\int_0^\infty x^n\,d\nu(x),
\]
where \(x=u^2\) and \(d\nu\) is the push-forward of the completed theta measure \(\Phi(u)\,du\) (up to the harmless even-folding normalization).

For \(k\ge2\), the adjacent cubic Toeplitz minor is
\[
\Delta_{3,k}=-\gamma_{k-2}\gamma_k\gamma_{k+2}+\gamma_{k-2}\gamma_{k+1}^2+\gamma_{k-1}^2\gamma_{k+2}-2\gamma_{k-1}\gamma_k\gamma_{k+1}+\gamma_k^3.
\]

After inserting the moment integrals, \(\Delta_{3,k}\) is exactly a triple integral of a symmetric homogeneous polynomial \(P_k(x,y,z)\) against \(d\nu(x)d\nu(y)d\nu(z)\).

## 2. Exact obstruction to the ordinary Vandermonde-square mechanism

For the first admissible case \(k=2\), the symmetrized integrand is
\[
P_2(x,y,z)= -\frac{1}{87091200}\,Q_2(x,y,z),
\]
where
\[
\begin{aligned}
Q_2={}&15x^4y^2-180x^4yz+15x^4z^2-56x^3y^3+840x^3y^2z+840x^3yz^2-56x^3z^3\\
&+15x^2y^4+840x^2y^3z-6300x^2y^2z^2+840x^2yz^3+15x^2z^4\\
&-180xy^4z+840xy^3z^2+840xy^2z^3-180xyz^4+15y^4z^2-56y^3z^3+15y^2z^4.
\end{aligned}
\]

A squared Vandermonde factor
\[
V(x,y,z)^2=(x-y)^2(x-z)^2(y-z)^2
\]
would require divisibility by \(V^2\). It fails exactly: setting \(y=x\),
\[
P_2(x,x,z)=\frac{x^2}{43545600}\left(13x^4-660x^3z+2295x^2z^2-784xz^3+75z^4\right),
\]
which is not identically zero. Hence
\[
V^2\nmid P_2.
\]

The same failure occurs at \(k=3\):
\[
P_3(x,x,z)=\frac{x^4z}{438939648000}\left(17x^4-280x^3z+728x^2z^2-330xz^3+42z^4\right),
\]
so again \(V^2\nmid P_3\).

## 3. Consequence

The standard Andreief/Binet–Cauchy route, in which an \(r\times r\) determinant of moments becomes a single positive integral of \(V^2\), cannot be the mechanism for the factorial-corrected Toeplitz minor. The obstruction is algebraic and occurs before inserting any particular numerical values of the theta measure.

This does NOT prove that \(\Delta_{3,k}\) cannot be nonnegative for the Riemann measure. It proves only that its positivity cannot arise from the naive single-Vandermonde-square symmetrization of the raw triple-product expansion.

## 4. Poisson/Jacobi consequence

Jacobi inversion changes the representation of \(d\nu\) and establishes the exact completed-kernel reflection, but it does not change the factorial index coupling
\[
\frac{x^{k+j-i}}{(2k+2j-2i)!}.
\]
Therefore Poisson pairing alone cannot remove the obstruction above.

## 5. Surviving proof-bearing target

A genuine all-order mechanism must act on the factorial kernel itself. Equivalent forms of the remaining target are:

1. factor the kernel \(K(n,x)=x^n/(2n)!\) through a totally-positive transform;
2. construct a stability-preserving operator whose minors reproduce the factorial Toeplitz determinants;
3. find a multi-term SOS/Gram decomposition more general than a single \(V^2\) factor and prove that the resulting Gram form implies hyperbolicity.

This is a stronger and more precise characterization of the remaining wall than the earlier unsummed-theta formulation.

No RH proof is claimed.