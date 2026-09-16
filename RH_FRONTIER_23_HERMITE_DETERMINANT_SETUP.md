# Riemann Hypothesis — Frontier 23 setup: Hermite determinant

For a real cubic
\[
p(x)=ax^3+bx^2+cx+d,
\qquad a\ne0,
\]
its three roots are all real iff its discriminant is nonnegative. Equivalently, the Hermite matrix of the roots is positive semidefinite.

For the Riemann Jensen cubic
\[
p=J_{3,n}(X)=A+c_1X+c_2X^2+c_3X^3,
\]
with
\[
c_1=\frac{3B}{2(2n+1)},\quad
c_2=\frac{3C}{4(2n+1)(2n+3)},\quad
c_3=\frac{D}{4(2n+1)(2n+3)(2n+5)},
\]
the discriminant calculation gives the exact scalar Hermite obstruction
\[
\operatorname{Disc}(J_{3,n})
=-\frac{27Q_{3,n}}{64(2n+1)^4(2n+3)^3(2n+5)^2}.
\]
Therefore any proof of RH through Jensen hyperbolicity must prove \(Q_{3,n}\le0\) for every \(n\ge0\), and analogous inequalities for every higher degree.

The important point is that \(Q_{3,n}\) is not a generic Hankel determinant. It contains alternating combinations of \(A,B,C,D\). Consequently ordinary positivity of the moment Hankel matrix cannot establish it by itself.

The next non-circular target is to substitute
\[
M_k=\int_0^\infty\Phi(t)t^{2k}\,dt
\]
into \(Q_{3,n}\), expand the products as fourfold integrals, and test whether symmetrisation can factor the resulting kernel into manifestly signed pieces. Any successful factorization must be proved from the explicit theta kernel; if it is equivalent to RH, that equivalence must be stated rather than treated as a proof.

Status: research target only; no RH proof.
