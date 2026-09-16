# Exact unsummed 3×3 Riemann–Xi theta determinant

## Status
This is an exact calculation for the degree-three Hankel determinant of the even Taylor moments of the completed Riemann Xi function. It does **not** prove RH. In fact, it exposes why ordinary Hankel positivity is too weak: the determinant is manifestly nonnegative independently of RH.

## 1. Exact theta-derived kernel
Use
\[
\Xi(t)=\int_0^\infty \Phi(u)\cos(tu)\,du,
\]
with
\[
\boxed{
\Phi(u)=\sum_{n=1}^{\infty}
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)e^{-\pi n^2e^{2u}}.
}
\]
Equivalently, termwise,
\[
\phi_n(u)=2\pi n^2e^{5u/2}\left(2\pi n^2e^{2u}-3\right)e^{-\pi n^2e^{2u}},
\qquad \Phi=\sum_{n\ge1}\phi_n.
\]
For \(u\ge0\), \(2\pi n^2e^{2u}-3\ge2\pi-3>0\), hence every \(\phi_n(u)>0\).

## 2. Exact moment coefficients
Define
\[
a_m:=(-1)^m\Xi^{(2m)}(0).
\]
Differentiating the cosine transform under the integral gives
\[
\boxed{a_m=\int_0^\infty u^{2m}\Phi(u)\,du.}
\]
Thus
\[
a_0=\int\Phi,
\quad a_1=\int u^2\Phi,
\quad a_2=\int u^4\Phi,
\quad a_3=\int u^6\Phi,
\quad a_4=\int u^8\Phi,
\]
with all integrals over \((0,\infty)\).

## 3. Exact 3×3 determinant before collapsing the lattice
Let
\[
\Delta_3:=
\det\begin{pmatrix}
a_0&a_1&a_2\\a_1&a_2&a_3\\a_2&a_3&a_4\end{pmatrix}.
\]
Andreief's identity yields the exact unsummed formula
\[
\boxed{
\Delta_3=
\frac1{3!}\int_{(0,\infty)^3}
\Phi(u_1)\Phi(u_2)\Phi(u_3)
\det\begin{pmatrix}1&u_1^2&u_1^4\\1&u_2^2&u_2^4\\1&u_3^2&u_3^4\end{pmatrix}^{\!2}
\,du_1du_2du_3.
}
\]
Since
\[
\det[1,u_r^2,u_r^4]_{r=1}^3
=(u_2^2-u_1^2)(u_3^2-u_1^2)(u_3^2-u_2^2),
\]
we obtain
\[
\boxed{
\Delta_3=\frac16\int_{(0,\infty)^3}
\Phi_1\Phi_2\Phi_3
\prod_{1\le r<s\le3}(u_s^2-u_r^2)^2\,d^3u\ge0.
}
\]
This is exact and no collapsed theta value has been used.

## 4. Keep the lattice unsummed
Substituting \(\Phi=\sum_{n\ge1}\phi_n\), justified by positivity/Tonelli,
\[
\boxed{
\Delta_3=
\frac16\sum_{n_1,n_2,n_3\ge1}
\int_{(0,\infty)^3}
\prod_{r=1}^3\phi_{n_r}(u_r)
\prod_{r<s}(u_s^2-u_r^2)^2\,d^3u.
}
\]
Every summand is nonnegative because every \(\phi_n(u)>0\).

## 5. Exact logarithmic incomplete-gamma form of each lattice moment
Set
\[
x=\pi n^2e^{2u}.
\]
Then \(u=\tfrac12\log(x/(\pi n^2))\) and
\[
\boxed{
\phi_n(u)\,du
=\pi^{-1/4}n^{-1/2}
\left(2x^{5/4}-3x^{1/4}\right)e^{-x}\,dx,
\qquad x\in[\pi n^2,\infty).
}
\]
Therefore
\[
\boxed{
\mu_{m,n}:=\int_0^\infty u^{2m}\phi_n(u)\,du
=\frac{\pi^{-1/4}n^{-1/2}}{2^{2m}}
\int_{\pi n^2}^{\infty}
\left(2x^{5/4}-3x^{1/4}\right)e^{-x}
\left[\log\frac{x}{\pi n^2}\right]^{2m}dx.
}
\]
This is an exact unsummed lattice formula, with no numerical approximation.

## 6. The residual calculation
Take as the positive part
\[
P_3:=\frac16\sum_{n_1,n_2,n_3\ge1}
\int_{(0,\infty)^3}
\prod_r\phi_{n_r}(u_r)
\prod_{r<s}(u_s^2-u_r^2)^2\,d^3u.
\]
But this is exactly the determinant itself. Hence the exact residual relative to the full unsummed Andreief/Vandermonde decomposition is
\[
\boxed{E_3:=\Delta_3-P_3=0.}
\]
There is no hidden negative residual at this level.

## 7. Important consequence: this does NOT prove RH
The identity above proves only positivity of the Hankel moment determinant
\[
\Delta_3\ge0.
\]
That positivity follows from \(\Phi(u)>0\), so it is not Riemann-specific enough to imply that all zeros of \(\Xi\) are real.

The crucial remaining wall is therefore not the sign of \(\Delta_3\). It is a stronger property involving the coefficient/Jensen-polynomial structure. In particular, the previous factorial-gauge/PF∞ proposal must not identify ordinary moment-Hankel positivity with the Laguerre–Pólya criterion.

## 8. Correct next target
The genuinely decisive 3×3 object should instead be a finite Jensen/Hurwitz-type minor whose hyperbolicity condition is equivalent to a discriminant inequality. For
\[
J_{n,3}(X)=a_n+3a_{n+1}X+3a_{n+2}X^2+a_{n+3}X^3,
\]
its discriminant is
\[
\boxed{
\operatorname{Disc}(J_{n,3})
=18bcde-4b^3d+b^2c^2-4c^3e-27a^2e^2
}
\]
when \((a,b,c,d)=(a_n,3a_{n+1},3a_{n+2},a_{n+3})\) is substituted appropriately. Explicitly,
\[
\boxed{
\operatorname{Disc}(J_{n,3})
=162a_na_{n+1}a_{n+2}a_{n+3}
-108a_n a_{n+2}^3
+81a_{n+1}^2a_{n+2}^2
-108a_{n+1}^3a_{n+3}
-27a_n^2a_{n+3}^2.
}
\]
Proving \(\operatorname{Disc}(J_{n,3})\ge0\) for the relevant normalized Jensen family, together with the all-degree hyperbolicity theorem and the Laguerre–Pólya closure step, is substantially closer to RH than proving \(\Delta_3\ge0\).

## 9. Research conclusion
The exact unsummed 3×3 theta determinant has a zero residual in the Andreief/Vandermonde decomposition:
\[
\boxed{E_3=0.}
\]
But this is a **diagnostic obstruction**, not a solution: the decomposition is positive because the Xi kernel is a positive moment kernel. The next attack must therefore target Jensen-polynomial hyperbolicity / PF∞ structure directly, not ordinary Hankel positivity.
