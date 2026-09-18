# Frontier 31 — Exact Cubic Cumulant Gate and a Sharp Obstruction

## Status

This frontier strengthens Frontier 30 by eliminating the raw moment ratios in favor of dimensionless variance and third-central-moment parameters. It proves an exact algebraic cubic gate and gives an explicit positive-measure family showing that the degree-2 variance bound alone cannot imply the degree-3 Jensen gate. This is a rigorous obstruction, not a proof of RH.

## 1. Starting point

For

\[
J_{3,n}(X)=\gamma_n+3\gamma_{n+1}X+3\gamma_{n+2}X^2+\gamma_{n+3}X^3,
\]

write the monic polynomial

\[
p_{3,n}(X)=X^3+b_1X^2+b_2X+b_3.
\]

With

\[
r_1=\frac{M_{n+1}}{M_n},\qquad r_2=\frac{M_{n+2}}{M_{n+1}},\qquad r_3=\frac{M_{n+3}}{M_{n+2}},
\]

Frontier 30 established

\[
 b_1=-\frac{6(2n+5)}{r_3},\qquad
 b_2=\frac{12(2n+3)(2n+5)}{r_2r_3},\qquad
 b_3=-\frac{8(2n+1)(2n+3)(2n+5)}{r_1r_2r_3}.
\]

A real cubic is hyperbolic exactly when

\[
\Delta_3=b_1^2b_2^2-4b_2^3-4b_1^3b_3-27b_3^2+18b_1b_2b_3\ge0.
\]

## 2. Dimensionless central-moment variables

Under

\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},\qquad Y=u^2,
\]

set

\[
\mu=\mathbb E_n[Y]>0,
\qquad
v=\operatorname{Var}_n(Y),
\qquad
\kappa=\mathbb E_n[(Y-\mu)^3].
\]

Define the dimensionless parameters

\[
q:=\frac{v}{\mu^2}\ge0,
\qquad
 t:=\frac{\kappa}{\mu^3}.
\]

Then

\[
\mathbb E[Y^2]=\mu^2(1+q),
\qquad
\mathbb E[Y^3]=\mu^3(1+3q+t),
\]

and therefore

\[
 r_1=\mu,
\qquad
 r_2=\mu(1+q),
\qquad
 r_3=\mu\frac{1+3q+t}{1+q}.
\]

Consequently

\[
\boxed{
\begin{aligned}
 b_1&=-6(2n+5)\frac{1+q}{\mu(1+3q+t)},\\
 b_2&=12(2n+3)(2n+5)\frac{1}{\mu^2(1+3q+t)},\\
 b_3&=-8(2n+1)(2n+3)(2n+5)\frac{1}{\mu^3(1+3q+t)}.
\end{aligned}}
\]

## 3. Exact cubic gate

Let

\[
h:=2n+1.
\]

Substitution into the cubic discriminant and exact factorization gives

\[
\boxed{
\Delta_3
=-\frac{1728(h+2)(h+4)^2}{\mu^6(1+3q+t)^4}\,Q_h(q,t),
}
\]

where

\[
\boxed{
\begin{aligned}
Q_h(q,t)={}&
4h^3q^3+h^3t^2
+32h^2q^3-24h^2q^2-24h^2qt+2h^2t^2\\
&+64hq^3-48hq^2-48hqt+48hq+32ht\\
&-96q^2+64t-32.
\end{aligned}}
\]

Since the prefactor is strictly negative whenever the moments are nondegenerate,

\[
\boxed{
J_{3,n}\text{ is hyperbolic}
\iff
Q_{2n+1}(q,t)\le0.
}
\]

This is an exact, root-independent, dimensionless reformulation.

## 4. Degree-2 gate in the same variables

Frontier 28 established

\[
\frac{\operatorname{Var}_n(Y)}{\mathbb E_n[Y]^2}\le\frac{2}{2n+1}.
\]

Therefore, with \(h=2n+1\), the degree-2 condition is simply

\[
\boxed{0\le q\le\frac2h.}
\]

The cubic gate is substantially stronger because it also depends on the independent standardized third central moment \(t\).

## 5. Sharp obstruction: degree 2 does not imply degree 3

Take any \(n\ge1\), so \(h=2n+1\ge3\). Choose

\[
q=\frac2h,
\qquad
 t=0.
\]

These values are realizable by an explicit positive random variable: let

\[
Y=\mu\left(1\pm\sqrt{\frac2h}\right)
\]

with equal probabilities \(1/2\). Since \(h\ge3\),

\[
1-\sqrt{2/h}>0,
\]

so \(Y>0\). Its mean is \(\mu\), its variance is \(2\mu^2/h\), and its third central moment is zero.

Thus this is an admissible positive-measure moment model satisfying the degree-2 condition exactly at equality.

But direct substitution gives

\[
\boxed{
Q_h\left(\frac2h,0\right)=\frac{64(h+2)}{h^2}>0.
}
\]

Hence

\[
\Delta_3<0.
\]

Therefore the corresponding cubic Jensen gate fails even though the degree-2 variance bound is exactly satisfied.

This proves the non-implication

\[
\boxed{
\text{degree-2 theta moment inequality}
\not\Rightarrow
\text{degree-3 Jensen hyperbolicity}.
}
\]

The counterexample is not a counterexample to the Riemann xi kernel: it is a counterexample to the proposed *generic implication from the degree-2 inequality alone*. The special arithmetic/theta structure must supply additional constraints on higher standardized moments.

## 6. Consequence for the global proof program

Any successful all-degree proof cannot stop at a variance estimate. At minimum, it must establish a hierarchy of joint constraints on

\[
(q,t,\text{fourth cumulant},\ldots)
\]

strong enough to force every Hermite principal minor.

A candidate theorem must therefore have the structural form

\[
\boxed{
\text{specific Riemann-theta kernel structure}
\Longrightarrow
\text{joint standardized-moment/cumulant inequalities}
\Longrightarrow
H_{d,n}\succeq0\quad\forall d,n.
}
\]

Generic positivity of \(\Phi\), Stieltjes moment log-convexity, or the degree-2 variance estimate cannot close the chain.

## 7. What this closes

This frontier closes the following possible shortcut:

> Prove the degree-2 Jensen inequality from theta-kernel concentration, then bootstrap all higher Jensen degrees from that single variance inequality.

The explicit positive two-point model above rules out that bootstrap at the level of general tilted positive measures.

It also gives a precise next target: characterize the additional constraints on \(t\) and higher standardized cumulants that are genuinely forced by the Riemann theta kernel.

## 8. What remains open

The decisive unresolved implication remains

\[
\boxed{
\text{Riemann theta/arithmetic structure}
\Longrightarrow
Q_{2n+1}(q_n,t_n)\le0
\quad\forall n,
}
\]

and its all-degree analogue for the full Hermite matrix.

No assumption of RH, Laguerre–Pólya membership, zero-supported measures, or a pre-existing Hilbert–Pólya operator is used here.

## 9. Conclusion

Frontier 31 is a genuine obstruction theorem and an exact new gate. It removes one tempting but invalid route to closure and sharply identifies the missing information: higher standardized-moment structure beyond variance. It does **not** prove the Riemann Hypothesis.
