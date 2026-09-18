# Frontier 32 — Certification of the Variance-Only Route as a Closed Branch

## Status

This note records a rigorous closure of one proposed route: degree-2 variance control by itself cannot bootstrap to all Jensen degrees. Frontier 31 supplies the explicit obstruction.

## Exact statement

For the tilted positive measure

\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},\qquad Y=u^2,
\]

the degree-2 Jensen condition is

\[
q_n:=\frac{\operatorname{Var}_{\nu_n}(Y)}{\mathbb E_{\nu_n}[Y]^2}
\le \frac{2}{2n+1}.
\]

The degree-3 condition is instead

\[
Q_{2n+1}(q_n,t_n)\le0,
\]

where

\[
 t_n=\frac{\mathbb E_{\nu_n}[(Y-\mathbb E Y)^3]}{\mathbb E[Y]^3}
\]

and \(Q_h\) is the exact polynomial derived in Frontier 31.

## Obstruction theorem

For every \(n\ge1\), let \(h=2n+1\) and take the positive two-point law

\[
Y=\mu\left(1\pm\sqrt{2/h}\right)
\]

with equal weights. Then

\[
q=2/h,\qquad t=0,
\]

so the degree-2 gate is exactly saturated, while

\[
Q_h(2/h,0)=\frac{64(h+2)}{h^2}>0,
\]

and hence the cubic discriminant is negative.

Therefore no theorem whose hypotheses consist only of positivity plus the degree-2 variance bound can imply degree-3 Jensen hyperbolicity.

## Consequence

The proof program must use genuinely higher-order information. In particular, a valid all-degree closure needs either:

1. explicit theta-kernel inequalities controlling the complete standardized-moment hierarchy; or
2. a direct root-independent positive Gram/Hermite factorization that bypasses separate cumulant bounds.

Any argument claiming to bootstrap all degrees from the single variance inequality is now mathematically blocked by an explicit positive-measure model.

## Proof integrity

The obstruction does not claim that the two-point law is the Riemann theta kernel. It only establishes the logical non-implication for the larger class of positive tilted measures. Thus it removes a generic shortcut without producing a counterexample to RH or to the Riemann xi function.

## Remaining decisive theorem

The unresolved target remains

\[
\boxed{
\text{specific theta/arithmetic structure}
\Longrightarrow
H_{d,n}\succeq0\quad\forall d,n.
}
\]

Until that implication is proved, the Riemann Hypothesis is not proved by this program.
