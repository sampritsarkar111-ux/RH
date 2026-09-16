# Frontier 89 — Exact scale-mixture determinant gate

Date: 2026-09-16

## Objective

Push the Laguerre-inner-polynomial route beyond Frontier 82 by isolating exactly what the positive theta mixture must prove. The point is to replace the vague statement "the mixture should preserve hyperbolicity" by explicit finite-degree determinant inequalities.

## 1. Exact beta-corrected moment representation

Write
\[
\gamma_m=\int_0^\infty y^m\,d\nu(y),
\]
where the representation is understood through the beta-corrected theta measure
\[
 d\nu_m(y) \equiv \frac{2m+1}{m!}\,d\mu(y)
\]
when the exponent is indexed at m. Equivalently, for fixed n,
\[
\gamma_{n+j}=\frac{2(n+j)+1}{(n+j)!}\int y^{n+j}\,d\mu(y).
\]
The essential difficulty is the j-dependent weight.

## 2. Exact degree-two determinant

Set
\[
I_k=\int y^k\,d\mu(y),
\qquad
c_k=\frac{2k+1}{k!}.
\]
Then
\[
\gamma_k=c_kI_k.
\]
The degree-two Jensen discriminant is
\[
\Delta_{2,n}=\gamma_{n+1}^2-\gamma_n\gamma_{n+2}
=c_{n+1}^2I_{n+1}^2-c_nc_{n+2}I_nI_{n+2}.
\]
Using two independent copies of \(\mu\), this becomes the exact symmetrized kernel identity
\[
\boxed{
\Delta_{2,n}
=\iint (y_1y_2)^n
\left[c_{n+1}^2y_1y_2-\frac{c_nc_{n+2}}2(y_1^2+y_2^2)\right]
\,d\mu(y_1)d\mu(y_2).
}
\]
Because
\[
\frac{c_{n+1}^2}{c_nc_{n+2}}
=\frac{(2n+3)^2}{(2n+1)(2n+5)}>1,
\]
the kernel is positive near \(y_1=y_2\), but it becomes negative for sufficiently separated scales \(y_1/y_2\). Thus no proof can rely on pointwise nonnegativity of this two-variable kernel over the whole positive quadrant.

## 3. General finite-degree formulation

For fixed n,d define
\[
J_{d,n}(X)=\sum_{j=0}^d\binom dj c_{n+j}I_{n+j}X^j.
\]
Every coefficient is a positive linear functional of the same theta measure, but the coefficient multiplier \(c_{n+j}\) depends on j.

Let \(\mathsf H_{d,n}\) denote the Hermite matrix of \(J_{d,n}\). Hyperbolicity is equivalent to
\[
\mathsf H_{d,n}\succeq0
\]
with the standard Hermite rank/equality conditions handled separately.

Expanding each entry in the moment variables gives
\[
\boxed{
\mathsf H_{d,n}[a,b]
=\sum_{r,s} C_{a,b;r,s}(n,d)\,I_{n+r}I_{n+s}.
}
\]
Therefore every Hermite principal minor has a finite multi-integral representation
\[
\boxed{
\det\mathsf H_{d,n}[S,S]
=\int_{(0,\infty)^{|S|}}
(y_1\cdots y_{|S|})^n
K_{S,n,d}(y_1,\ldots,y_{|S|})
\,d\mu^{\otimes |S|}.
}
\]
This is an exact algebraic reduction; no RH assumption is used.

## 4. New obstruction theorem for naive SOS

A pointwise SOS proof of the form
\[
K_{S,n,d}(y_1,\ldots,y_m)\ge0
\quad\forall y_i>0
\]
would be sufficient, but the degree-two kernel above already disproves the analogous universal pointwise strategy. Indeed, for \(y_1/y_2\to\infty\), its leading term is
\[
-\frac{c_nc_{n+2}}2y_1^2<0.
\]
Thus the correct certificate must use additional theta information: the actual measure \(\mu\), its modular involution, or a nonlocal variation-diminishing property.

## 5. Stronger exact target: measure-specific Gram factorization

The remaining target is therefore not a generic mixture theorem. It is the existence, for every \(n,d\), of a theta-specific factorization
\[
\boxed{
\det\mathsf H_{d,n}[S,S]
=\sum_\alpha\int |P_{\alpha,S,n,d}(u_1,\ldots,u_m)|^2\,d\lambda_\alpha
}
\]
where each \(\lambda_\alpha\) is explicitly positive and every exchange of sums/integrals is justified from the theta kernel.

A particularly useful stronger operator form would be
\[
\boxed{
\mathsf H_{d,n}=\mathsf A_{d,n}^*\mathsf G_{d,n}\mathsf A_{d,n},
\qquad
\mathsf G_{d,n}\succeq0,
}
\]
with \(\mathsf G_{d,n}\) obtained directly from the modular identity rather than from an RH-equivalent assumption.

## 6. Relation to the Laguerre inner polynomial

The fixed-scale inner polynomial is already exactly hyperbolic:
\[
p_{n,d}(t)=\frac{d!}{(n+d)!}L_d^{(n)}(-t),
\]
and
\[
q_{n,d}(t)=(2n+1)p_{n,d}(t)+2tp'_{n,d}(t).
\]
Its d roots are real, simple, negative, and interlace those of \(p_{n,d}\).

The missing statement is therefore precisely:
\[
\boxed{
\mathcal M_n[q_{n,d}](X)
:=\int y^n q_{n,d}(yX)\,d\mu(y)
\text{ is hyperbolic for every }n,d.
}
\]
Frontier 89 shows why this cannot be replaced by the false generic assertion that arbitrary positive scale mixtures of hyperbolic polynomials remain hyperbolic.

## 7. Next high-value attack

The next calculation should derive the exact modular involution of \(\mu\) in the \(y=x(1-x)u^2\) variable and determine whether the degree-two kernel can be paired into a manifest square after the involution. If that succeeds, the same pairing should be lifted to the full Hermite matrix. If it fails, the obstruction should be recorded as a precise no-go result rather than hidden.

## Status

**Exact new reduction, not a proof of RH.** The global theorem still requires an all-degree theta-specific Gram/variation-diminishing mechanism.
