# Frontier 28 — Exact Theta-Moment Reduction of the First Hermite Gate

## Purpose

Frontier 27 isolated the nonlinear obstruction between a positive theta/moment representation and Hermite positivity. This frontier pushes that obstruction to an exact scalar inequality at degree two, so that any proposed global theta argument must prove a concrete analytic statement rather than rely on a generic moment-positivity slogan.

## 1. Exact coefficient representation

Use the standard even Fourier/theta representation in the form
\[
\Xi(z)=C\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad \Phi(u)\ge0,
\]
with sufficient decay for termwise differentiation at zero. Put
\[
M_n:=\int_0^\infty u^{2n}\Phi(u)\,du.
\]
Then the Taylor coefficient has the alternating-sign form
\[
\Xi(z)=C\sum_{n\ge0}\frac{(-1)^nM_n}{(2n)!}z^{2n}.
\]
If
\[
G(z)=8\Xi(1/2+z)=\sum_{n\ge0}\gamma_n\frac{z^{2n}}{n!},
\]
then, after absorbing the positive global normalization into \(C\),
\[
\boxed{\gamma_n=C(-1)^n\frac{n!}{(2n)!}M_n.}
\]
The sign is therefore structural; the positive moments are not themselves the Jensen coefficients.

## 2. Degree-two Jensen polynomial

Define
\[
J_{2,n}(X)=\gamma_n+2\gamma_{n+1}X+\gamma_{n+2}X^2.
\]
Its discriminant is
\[
\operatorname{disc}(J_{2,n})
=4\bigl(\gamma_{n+1}^2-\gamma_n\gamma_{n+2}\bigr).
\]
Thus degree-two hyperbolicity is exactly
\[
\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}.
\]
Substitution of the exact coefficient formula gives
\[
\frac{\gamma_{n+1}^2}{\gamma_n\gamma_{n+2}}
=\frac{(n+1)!^2}{(2n+2)!^2}
\frac{(2n)!(2n+4)!}{n!(n+2)!}
\frac{M_{n+1}^2}{M_nM_{n+2}}
=\frac{2n+3}{2n+1}\frac{M_{n+1}^2}{M_nM_{n+2}}.
\]
Therefore the exact necessary-and-sufficient degree-two condition is
\[
\boxed{
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}
\qquad(n\ge0).
}
\]

## 3. Why generic positivity cannot close this gate

Because \(\Phi\ge0\), Cauchy–Schwarz gives the ordinary moment log-convexity inequality
\[
M_{n+1}^2\le M_nM_{n+2}.
\]
The required Jensen inequality is a *reverse inequality up to the explicit factor*
\[
\frac{2n+1}{2n+3}<1.
\]
These two inequalities are compatible, so there is no contradiction. But the second inequality is not a generic consequence of positivity of \(\Phi\). It is an additional quantitative property of the specific Riemann theta kernel.

## 4. A normalized variance formulation

Define the probability measure
\[
 d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n}.
\]
Then
\[
\frac{M_{n+2}M_n}{M_{n+1}^2}
=\frac{\mathbb E_{\nu_n}[u^4]}{\mathbb E_{\nu_n}[u^2]^2}.
\]
Hence the degree-two Jensen condition is equivalent to
\[
\boxed{
\frac{\operatorname{Var}_{\nu_n}(u^2)}{\mathbb E_{\nu_n}[u^2]^2}
\le \frac{2}{2n+1}.
}
\]
Indeed,
\[
\frac{M_nM_{n+2}}{M_{n+1}^2}-1
=\frac{\operatorname{Var}_{\nu_n}(u^2)}{\mathbb E_{\nu_n}[u^2]^2},
\]
and the previous boxed inequality is equivalent to this variance bound.

This is a sharper analytic formulation of the first unresolved gate: the theta kernel would have to force a uniform, explicitly decaying coefficient of variation for the tilted random variable \(u^2\).

## 5. Research consequence

Any purported proof of all Jensen hyperbolicity from the theta representation must, as a special case, prove the variance bound above for every \(n\). Therefore a proof strategy that establishes only \(\Phi\ge0\), moment existence, or ordinary log-convexity is formally insufficient.

Conversely, proving this scalar inequality for all \(n\) would close only the \(d=2\) Hermite gate. It does **not** imply higher-degree Jensen hyperbolicity or RH.

## 6. New higher-degree target

The natural extension is to identify higher centered-moment/cumulant inequalities under the tilted measures \(\nu_n\) that are exactly equivalent to the principal minors of
\[
H(p_{d,n}).
\]
The required result must control the nonlinear Newton-sum combinations, not merely the Hankel moment matrix of \(M_n\).

A viable global theorem would have the form
\[
\boxed{
\text{explicit theta-kernel inequalities for all }(d,n)
\Longrightarrow H(p_{d,n})\succeq0\quad\forall d,n.
}
\]
The implication must be proved entry-by-entry or through a genuinely positive root-independent Gram identity.

## Status

This frontier is an exact analytic reduction and a new quantitative obstruction. It is **not** a proof of the Riemann Hypothesis. No RH conclusion is claimed.
