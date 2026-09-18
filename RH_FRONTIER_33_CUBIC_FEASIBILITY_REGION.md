# Frontier 33 — Exact Cubic Feasibility Region in Standardized Tilted-Moment Coordinates

## Status

This frontier sharpens the degree-3 Jensen obstruction from Frontier 31. It gives the exact admissible region in the standardized variance/skewness plane `(q,t)` for cubic Jensen hyperbolicity. This is a rigorous necessary-and-sufficient finite-degree statement for the normalized cubic, but it is **not** an RH proof.

## 1. Setup

Let

\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},\qquad Y=u^2,
\]

and write

\[
\mu=\mathbb E[Y]>0,
\qquad
q=\frac{\operatorname{Var}(Y)}{\mu^2},
\qquad
 t=\frac{\mathbb E[(Y-\mu)^3]}{\mu^3},
\qquad h=2n+1.
\]

Then

\[
\mathbb E[Y^2]=\mu^2(1+q),
\qquad
\mathbb E[Y^3]=\mu^3(1+3q+t).
\]

For the cubic Jensen polynomial

\[
J_{3,n}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3,
\]

monic normalization gives

\[
\begin{aligned}
b_1&=-\frac{6(h+4)(1+q)}{\mu(1+3q+t)},\\
b_2&=\frac{12(h+2)(h+4)}{\mu^2(1+3q+t)},\\
b_3&=-\frac{8h(h+2)(h+4)}{\mu^3(1+3q+t)}.
\end{aligned}
\]

## 2. Exact discriminant reduction

The cubic discriminant is

\[
\Delta_3=b_1^2b_2^2-4b_2^3-4b_1^3b_3-27b_3^2+18b_1b_2b_3.
\]

Direct substitution and exact algebra give

\[
\boxed{
\Delta_3=-\frac{1728(h+2)(h+4)^2}{\mu^6(1+3q+t)^4}\,Q_h(q,t),
}
\]

where

\[
\begin{aligned}
Q_h(q,t)= {}&4h^3q^3+h^3t^2+32h^2q^3-24h^2q^2-24h^2qt+2h^2t^2\\
&+64hq^3-48hq^2-48hqt+48hq+32ht\\
&-96q^2+64t-32.
\end{aligned}
\]

Because the prefactor outside `Q_h` is strictly negative whenever the moment normalization is nondegenerate,

\[
\boxed{J_{3,n}\text{ is hyperbolic}\iff Q_h(q,t)\le0.}
\]

## 3. New exact factorization of the `t`-discriminant

Regard `Q_h(q,t)` as a quadratic polynomial in `t`:

\[
Q_h(q,t)=A_h t^2+B_h(q)t+C_h(q).
\]

The coefficients are

\[
A_h=h^2(h+2),
\]

\[
B_h(q)=-8(h+2)(3hq-4),
\]

and

\[
C_h(q)=4\bigl(h^3q^3+8h^2q^3-6h^2q^2+16hq^3-12hq^2+12hq-24q^2-8\bigr).
\]

The discriminant of this quadratic in `t` factors exactly as

\[
\boxed{
\operatorname{Disc}_t(Q_h)
=-16(h+2)(h+4)^2(hq-2)^3.
}
\]

Hence for the degree-2 admissible range

\[
0\le q\le\frac2h,
\]

we have:

* if `0\le q<2/h`, then `Disc_t(Q_h)>0`, so there are two real skewness boundaries;
* if `q=2/h`, then `Disc_t(Q_h)=0` and the two boundaries coalesce.

The two roots are

\[
\boxed{
 t_{\pm}(h,q)=
\frac{4(3hq-4)\pm
2\dfrac{h+4}{\sqrt{h+2}}(2-hq)^{3/2}}{h^2}.
}
\]

Since `A_h>0`, the exact cubic condition is

\[
\boxed{
J_{3,n}\text{ is hyperbolic}
\iff
0\le q<\frac2h
\quad\text{and}\quad
 t_-(h,q)\le t\le t_+(h,q),
}
\]

with the endpoint `q=2/h` handled separately. At that endpoint,

\[
Q_h\left(\frac2h,t\right)=\frac{h+2}{h^2}(h^2t-8)^2\ge0,
\]

so equality `Q_h=0` occurs exactly at

\[
\boxed{q=\frac2h,\qquad t=\frac8{h^2}.}
\]

Thus the cubic gate adds an exact skewness compatibility condition; the variance boundary itself is touched only at this single tangency value.

## 4. Relation to the degree-2 gate

Frontier 28 established the degree-2 condition

\[
q\le\frac2h.
\]

Frontier 33 shows that degree 3 is genuinely stronger: for `q<2/h`, it requires the third standardized central moment `t` to lie in an explicit curved interval depending on `q` and `h`. At the boundary `q=2/h`, only the tangency value `t=8/h^2` survives the cubic discriminant condition.

Therefore an all-degree proof cannot be reduced to variance control. It must control a hierarchy of higher standardized moments/cumulants, or bypass these coordinates by a direct positive Gram/Hermite factorization.

## 5. Exact obstruction to a variance-only bootstrap

At `q=2/h`, Frontier 31 used the positive two-point law

\[
Y=\mu\left(1\pm\sqrt{2/h}\right)
\]

with equal weights. It has `t=0`, saturates the degree-2 bound, and fails the cubic condition because

\[
Q_h\left(\frac2h,0\right)=\frac{64(h+2)}{h^2}>0.
\]

Frontier 33 strengthens the interpretation: variance saturation alone is insufficient; the cubic condition also specifies the required skewness at the saturation point.

## 6. What this does and does not prove

### Proven here

1. Exact standardized-coordinate formulas for the monic cubic Jensen coefficients.
2. Exact cubic discriminant reduction to `Q_h(q,t)`.
3. Exact factorization of the discriminant of `Q_h` as a quadratic in `t`.
4. Exact closed-form skewness boundaries `t_\pm(h,q)`.
5. Exact description of the cubic feasibility region in `(q,t)`, including its boundary tangency.

### Still unresolved

The decisive RH step remains to prove that the **specific Riemann theta kernel** satisfies these cubic constraints for every `n`, and then to obtain the corresponding higher-degree constraints for every degree `d`.

In particular, this frontier does **not** establish

\[
H_{d,n}\succeq0\quad\forall d,n,
\]

nor does it establish that the Riemann xi function belongs to the Laguerre–Pólya class.

## 7. Next decisive research target

The next nontrivial target is now sharply formulated:

\[
\boxed{
\text{derive theta-specific inequalities forcing}
\quad
Q_{2n+1}(q_n,t_n)\le0
\quad\forall n,
}
\]

and then determine whether those inequalities admit a systematic extension to the fourth and higher standardized cumulants sufficient to imply all Hermite principal minors.

A stronger target remains preferable:

\[
\boxed{
H_{d,n}=\int V_{d,n}(s)V_{d,n}(s)^T\,d\mu_{d,n}(s),
\qquad d\mu_{d,n}\ge0,
}
\]

with an explicit theta/arithmetic construction independent of the unknown roots of the Jensen polynomial.

No RH proof is claimed until that global implication is established rigorously.
