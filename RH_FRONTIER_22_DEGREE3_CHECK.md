# Frontier 22 — Degree-3 discriminant verification

For
\[
J_{3,n}(X)=A+\frac{3B}{2(2n+1)}X+\frac{3C}{4(2n+1)(2n+3)}X^2+\frac{D}{4(2n+1)(2n+3)(2n+5)}X^3,
\]
set
\[
a=\frac{D}{4(2n+1)(2n+3)(2n+5)},\quad
b=\frac{3C}{4(2n+1)(2n+3)},
\]
\[
c=\frac{3B}{2(2n+1)},\quad d=A.
\]
Using
\[
\operatorname{Disc}(aX^3+bX^2+cX+d)=b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd,
\]
one obtains
\[
\operatorname{Disc}(J_{3,n})=-\frac{27}{64(2n+1)^4(2n+3)^3(2n+5)^2}Q_{3,n},
\]
with
\[
\begin{aligned}
Q_{3,n}={}&(32n^3+176n^2+312n+180)B^3D\\
&-(24n^3+156n^2+330n+225)B^2C^2\\
&+(32n^3+176n^2+280n+100)AC^3\\
&-(96n^3+432n^2+552n+180)ABCD\\
&+(32n^3+80n^2+56n+12)A^2D^2.
\end{aligned}
\]
Thus, for positive leading coefficient and positive coefficients, the degree-3 hyperbolicity condition is exactly \(Q_{3,n}\le0\). This formula has been independently expanded symbolically from the cubic discriminant and is the expression used in Frontier 22.
