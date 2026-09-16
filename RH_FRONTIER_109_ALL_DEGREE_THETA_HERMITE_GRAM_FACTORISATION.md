# Frontier 109 — explicit all-degree theta-derived Hermite/Gram factorisation

Date: 2026-09-16

## Objective

Attack the RH proof through an exact all-degree positive-semidefinite representation derived from the completed Riemann theta kernel, while retaining the full lattice sum until the positivity mechanism is exposed. This replaces the zero-location-free determinant-tail route rejected in Frontier 108.

The completed kernel is
\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad \Phi(-u)=\Phi(u),
\]
and Frontier 100 established \(\Phi(u)>0\) for every real \(u\).

## 1. Exact theta-to-moment expansion

Use the completed Fourier representation, with the project's fixed normalization,
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du.
\]
After the substitution \(z=-t^2\), define
\[
g(z):=\Xi(\sqrt{-z})
      =\int_{\mathbb R}\Phi(u)\cosh(u\sqrt z)\,du
      =\sum_{k\ge0}\gamma_kz^k,
\]
where termwise expansion is justified on compact \(z\)-sets by the rapid decay of the completed kernel and
\[
\boxed{\gamma_k=\frac{M_k}{(2k)!},\qquad
M_k:=\int_{\mathbb R}u^{2k}\Phi(u)\,du.}
\]
Thus the Taylor coefficients are exact even moments of the positive completed-theta measure.

This identity is the starting point for an all-degree calculation; no zero locations are used.

## 2. Exact Jensen polynomial representation

For degree \(d\) and shift \(n\), take the standard Jensen polynomial
\[
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j.
\]
Substitution of the moment formula gives the exact integral representation
\[
\boxed{
J_{d,n}(X)
=\int_{\mathbb R}\Phi(u)u^{2n}
\left[\sum_{j=0}^{d}\binom dj\frac{(u^2X)^j}{(2n+2j)!}\right]du.
}
\]
The bracket is an explicit finite polynomial, but it is NOT pointwise real-rooted in \(X\) for arbitrary \(u\), so this formula alone is not a Gram certificate.

## 3. Exact degree-two gate recovered from the theta measure

For \(d=2\),
\[
J_{2,n}(X)=\gamma_n+2\gamma_{n+1}X+\gamma_{n+2}X^2.
\]
Its discriminant condition is
\[
\gamma_{n+1}^2\ge \gamma_n\gamma_{n+2}.
\]
Using \(\gamma_k=M_k/(2k)!\), this becomes
\[
\boxed{
\frac{M_{n+1}^2}{M_nM_{n+2}}
\ge
\frac{(2n+2)!^2}{(2n)!(2n+4)!}
=
\frac{(n+1)(2n+1)(2n+5)}{(n+2)(2n+3)^2}.
}
\]
Equivalently, for the probability measure
\[
d\nu_n(u)=\frac{u^{2n}\Phi(u)\,du}{M_n},
\qquad Y=u^2,
\]
\[
\boxed{
\frac{\operatorname{Var}_{\nu_n}(Y)}{\mathbb E_{\nu_n}[Y]^2}
\le
\frac{4n^2+16n+13}{(n+1)(2n+1)(2n+5)}.
}
\]
This is an exact necessary condition for the degree-two Jensen mechanism. It is not yet proved for the Riemann theta measure for every \(n\).

## 4. What an all-degree Gram factorisation must actually prove

For the monic version \(\widehat J_{d,n}\) of \(J_{d,n}\), let
\[
\mathsf H_{d,n}=\big(s_{r+s}(\widehat J_{d,n})\big)_{0\le r,s<d},
\]
where \(s_k\) is the \(k\)-th Newton power sum of the roots, equivalently the trace power of the companion matrix.

The required RH-bearing statement is the explicit identity
\[
\boxed{
 c^T\mathsf H_{d,n}c
 =\sum_{\alpha}\int_{\Omega_\alpha}
 \left|\sum_{r=0}^{d-1}c_rP_{\alpha,r}(x)\right|^2
 d\mu_\alpha(x)\ge0
 \quad\forall d,n,c,
}
\]
with every \(P_{\alpha,r}\) and positive measure \(\mu_\alpha\) written explicitly in terms of the completed theta lattice (or an exactly equivalent transformed kernel).

If this identity is obtained, the Hermite criterion gives hyperbolicity of every Jensen polynomial; the Pólya-Jensen equivalence then supplies RH. The proof must establish the identity itself without assuming hyperbolicity or real zero locations.

## 5. New reduction: multilinear moment expansion

Every entry of \(\mathsf H_{d,n}\) is a polynomial/rational expression in the finite coefficient list \(\gamma_n,\ldots,\gamma_{n+d}\). After inserting
\[
\gamma_k=\frac1{(2k)!}\int u^{2k}\Phi(u)\,du,
\]
any homogeneous term of degree \(q\) becomes a \(q\)-fold integral against the positive product measure
\[
\prod_{\ell=1}^{q}\Phi(u_\ell)\,du_\ell.
\]
Therefore the remaining problem can be stated exactly as follows:

> Find a finite, degree-uniform algebraic transformation of the Newton/Hermite polynomial in the moments that factors its integrand into a sum of squares after the full theta kernel is retained.

This is stronger and more precise than merely asking whether the moment sequence is log-concave or totally positive.

## 6. Adversarial obstruction that must be avoided

The degree-two integrand obtained by collapsing everything to one copy of \(Y=u^2\) is indefinite in general. Hence the certificate cannot simply be
\[
\text{Hermite form}=\int Q(u)^2\Phi(u)\,du
\]
with one scalar variable and no cross-copy structure.

The viable possibility is instead a genuine multi-copy kernel
\[
\boxed{
\mathsf H_{d,n}[c]
=\int_{\mathbb R^q}
\mathcal K_{d,n}(u_1,\ldots,u_q;c)\,
\prod_{\ell=1}^{q}\Phi(u_\ell)\,du_\ell,
}
\]
where \(\mathcal K\) is itself converted by Binet–Cauchy, Vandermonde, or a theta-specific reflection identity into a sum of squares.

No sign is assigned to \(\mathcal K\) before that factorisation; this prevents the invalid pointwise-positivity shortcut exposed in Frontiers 99–101.

## 7. Concrete next algebraic target

For each fixed \(d\), derive the exact polynomial \(\mathcal K_{d,n}\) from Newton identities through degree \(d-1\), then search for a Binet–Cauchy factorisation of its antisymmetric part. The first nontrivial test is \(d=3\), because \(d=2\) only gives the scalar discriminant gate.

For \(d=3\), write
\[
\widehat J(X)=X^3+aX^2+bX+c.
\]
Newton identities give
\[
s_1=-a,\qquad s_2=a^2-2b,\qquad s_3=-a^3+3ab-3c,
\]
and hence
\[
\mathsf H_3=
\begin{pmatrix}
3&s_1&s_2\\
s_1&s_2&s_3\\
s_2&s_3&s_4
\end{pmatrix},
\]
with \(s_4=a^4-4a^2b+2b^2+4ac\).

The exact research task is to substitute the theta moments for \(a,b,c\), expand the resulting quadratic form into multi-integrals, and determine whether a positive Binet–Cauchy/Vandermonde factorisation exists. A negative exact principal minor would close this particular Gram ansatz as an obstruction; a successful sum-of-squares identity would be a genuine new proof-bearing step.

## 8. Status

This frontier derives an exact all-degree theta/moment representation and sharply identifies the missing theorem: an explicit multi-copy positive Gram factorisation of the Hermite forms, valid for every degree and shift without using zero locations.

It is **not an RH proof**. In particular, positivity of \(\Phi\), positivity of moment Hankel matrices, finite-degree experiments, or asymptotics do not by themselves establish hyperbolicity of all Jensen polynomials.
