# Theta-to-Jensen all-degree frontier

## Status

This document records the exact mathematical frontier for the proposed theta/Gram route to RH. It deliberately does **not** claim a proof of RH unless the all-degree positivity theorem below is actually established.

## 1. Unconditional theta representation

Let
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi(t)=\xi(\tfrac12+it).
\]
With \(\theta(x)=\sum_{m\in\mathbb Z}e^{-\pi m^2x}\), Poisson/Jacobi gives
\[
\theta(x)=x^{-1/2}\theta(1/x),\qquad x>0.
\]
Splitting the Mellin integral at \(1\) and applying this identity yields the completed-zeta theta representation, without any assumption on zero locations. Differentiation under the resulting rapidly convergent integral is justified by absolute convergence on compact \(t\)-sets.

Equivalently, the standard Pólya form is
\[
\Xi(t)=\int_0^\infty \Phi_1(u)\cos(tu)\,du,
\]
with
\[
\Phi_1(u)=2\pi(2\pi e^{4u}-3)e^{5u-\pi e^{4u}},
\]
so that \(\Phi_1(u)>0\) for \(u\ge0\), and
\[
M_n=\int_0^\infty \Phi_1(u)u^{2n}\,du>0,
\qquad
\Xi(t)=\sum_{n\ge0}(-1)^nM_n\frac{t^{2n}}{(2n)!}.
\]

## 2. The decisive normalization issue

A positive moment representation immediately gives a Hankel Gram matrix
\[
H^{\rm mom}_{ij}=M_{i+j}
=\int_0^\infty \Phi_1(u)u^{2i}u^{2j}\,du\succeq0.
\]
This is unconditional, but it is **not** the required Jensen/Hermite Gram matrix. Raw moment positivity alone cannot imply the desired Jensen hyperbolicity.

Indeed, the raw moments are log-convex by Cauchy--Schwarz:
\[
M_{n+1}^2\le M_nM_{n+2}.
\]
Therefore a quadratic formed directly as
\[
M_n+2M_{n+1}X+M_{n+2}X^2
\]
has discriminant
\[
4(M_{n+1}^2-M_nM_{n+2})\le0,
\]
with strict negativity for a non-degenerate positive measure. Thus a purported proof that identifies this raw moment Hankel Gram matrix with the Jensen hyperbolicity certificate is invalid.

The actual all-degree object must encode the factorial/Jensen normalization and the Hermite (root-power-sum) structure simultaneously.

## 3. Exact target

For each degree \(d\), let \(J_{n,d}\) denote the correctly normalized Pólya--Jensen polynomial attached to the Taylor coefficient sequence of the even entire function \(\Xi\). The required theorem is
\[
\boxed{\forall n,d\ge0,\quad H(J_{n,d})\succeq0,}
\]
where \(H(J)\) is the Hermite matrix of the polynomial \(J\).

For a real polynomial, Hermite-matrix positivity is the algebraic real-root certificate (with the usual rank/nondegeneracy conventions). Hence the desired chain is
\[
H(J_{n,d})\succeq0
\Longrightarrow J_{n,d}\text{ hyperbolic}
\Longrightarrow \Xi\in\mathcal{LP}
\Longrightarrow Z(\Xi)\subset\mathbb R
\Longrightarrow RH.
\]

## 4. What remains genuinely open in this route

The missing theorem is an explicit, theta-derived identity of the form
\[
H(J_{n,d})=\mathcal G_{n,d}[\Phi_1]
\]
with an exact decomposition into manifestly nonnegative terms (or a genuine Gram/SOS representation), valid simultaneously for every \(n,d\), and with no occurrence of unknown zeros of \(\Xi\) or \(\zeta\).

Any candidate decomposition must pass these tests:

1. exact equality, not asymptotic equality;
2. all \(n,d\), not finite verification;
3. every weight/measure/kernel used in the Gram representation is proven nonnegative;
4. all factorial and parity normalizations are explicit;
5. no step uses RH, \(\Xi\in\mathcal{LP}\), real zeros, or an equivalent assumption;
6. the residual is identically zero or separately PSD.

## 5. Current conclusion

The theta moment positivity is a rigorous foundation, but it does not close the RH proof. The central research problem remains the construction of the exact all-degree factorial-normalized theta Gram identity above. Until that identity is proved, RH must not be declared proved.
