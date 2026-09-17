# Theta-to-Jensen all-degree frontier

## Status

This document records the exact mathematical frontier for the proposed theta/Gram route to RH. It deliberately does **not** claim a proof of RH unless the all-degree positivity theorem below is actually established.

## 1. Unconditional theta representation

Let
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi(t)=\xi(\tfrac12+it).
\]
The completed zeta function has an unconditional theta/Mellin representation, and the standard Pólya form is
\[
\Xi(t)=\int_0^\infty \Phi_1(u)\cos(tu)\,du,
\]
with
\[
\Phi_1(u)=2\pi(2\pi e^{4u}-3)e^{5u-\pi e^{4u}}>0\qquad(u\ge0).
\]
Hence
\[
M_n=\int_0^\infty \Phi_1(u)u^{2n}\,du>0,
\qquad
\Xi(t)=\sum_{n\ge0}(-1)^nM_n\frac{t^{2n}}{(2n)!}.
\]

## 2. Correct even-variable Jensen normalization

Set
\[
F(z):=\Xi(\sqrt z).
\]
Because Xi is even entire, F is entire and
\[
F(z)=\sum_{n\ge0}\gamma_n\frac{z^n}{n!},
\qquad
\gamma_n=(-1)^n\frac{n!}{(2n)!}M_n.
\]
For the standard Jensen convention
\[
J_{n,d}^F(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j,
\]
substitution of the theta moments gives the exact integral identity
\[
J_{n,d}^F(X)=\int_0^\infty \Phi_1(u)u^{2n}K_{n,d}(u^2X)\,du,
\]
where
\[
K_{n,d}(Y)=\sum_{j=0}^d(-1)^{n+j}\binom dj\frac{(n+j)!}{(2n+2j)!}Y^j.
\]

## 3. New exact closed form: the Jensen kernel is Laguerre

Using
\[
(2n+2j)!= (2n)\,4^j\,(n+\tfrac12)_j(n+1)_j\quad\text{in the equivalent factorial-ratio identity},
\]
more precisely
\[
\frac{(n+j)!}{(2n+2j)!}
=\frac{n!}{(2n)!}\frac{1}{4^j(n+\tfrac12)_j},
\]
and
\[
\binom dj(-1)^j=\frac{(-d)_j}{j!},
\]
we obtain
\[
\boxed{
K_{n,d}(Y)=(-1)^n\frac{n!}{(2n)!}\,{}_1F_1\!\left(-d;n+\tfrac12;\frac Y4\right)
}
\]
and therefore, by the terminating Kummer--Laguerre identity,
\[
\boxed{
K_{n,d}(Y)=(-1)^n\frac{n!}{(2n)!}\frac{d!}{(n+\tfrac12)_d}
L_d^{\,n-1/2}\!\left(\frac Y4\right).
}
\]
Thus the exact Jensen polynomial has the representation
\[
\boxed{
J_{n,d}^F(X)=(-1)^n\frac{n!}{(2n)!}\frac{d!}{(n+\tfrac12)_d}
\int_0^\infty\Phi_1(u)u^{2n}
L_d^{\,n-1/2}\!\left(\frac{u^2X}{4}\right)du.
}
\]
This is an exact all-degree reduction, with no RH assumption.

## 4. What this does — and does not — prove

For each fixed \(n,d\), the inner Laguerre polynomial is real-rooted. This is a genuine structural simplification: the entire Jensen problem is reduced to a positive theta-weighted dilation mixture of generalized Laguerre polynomials.

However, **positive mixing does not automatically preserve hyperbolicity**. A generic positive discrete mixture of dilated real-rooted Laguerre kernels can already acquire nonreal zeros. Therefore the missing theorem is now sharply localized:
\[
\boxed{
\text{the specific theta weight }\Phi_1(u)u^{2n}du
\text{ must induce a hyperbolicity-preserving Laguerre-dilation transform.}
}
\]
A proof based only on positivity of \(\Phi_1\), or only on real-rootedness of each Laguerre kernel, is insufficient.

## 5. Equivalent all-degree target

The required theorem can now be stated in operator form. Define
\[
(\mathcal T_n p)(X):=
\int_0^\infty \Phi_1(u)u^{2n}p(u^2X)\,du.
\]
Then the exact Jensen polynomial is a positive scalar multiple (up to the harmless global sign \((-1)^n\)) of
\[
\mathcal T_n\!\left[L_d^{\,n-1/2}(\cdot/4)\right].
\]
The proof-bearing target is therefore
\[
\boxed{
\mathcal T_n\text{ preserves the relevant Laguerre hyperbolicity cone for every }n,d.
}
\]
Equivalently, one may prove
\[
H(J_{n,d}^F)\succeq0\qquad\forall n,d\ge0,
\]
by an exact theta-specific Gram/SOS representation.

## 6. Adversarial obstruction that remains

Ordinary moment positivity gives
\[
[M_{i+j}]_{i,j\ge0}\succeq0,
\]
but Cauchy--Schwarz gives raw moment log-convexity, which has the wrong sign for a naive raw-moment Jensen discriminant. Thus the Gram object must retain the factorial normalization.

Likewise, the exact Laguerre mixture above is not enough: arbitrary positive mixtures of dilations can fail hyperbolicity. The missing ingredient must use a special property of the Riemann theta weight (Poisson/Jacobi symmetry, total positivity, a variation-diminishing transform, or an equivalent exact structure).

## 7. Required finish line

The remaining chain is:
\[
\boxed{
\text{theta-specific Laguerre-dilation preservation}
\Longrightarrow
J_{n,d}^F\text{ hyperbolic for all }n,d
\Longrightarrow
\Xi\in\mathcal{LP}
\Longrightarrow
Z(\Xi)\subset\mathbb R
\Longrightarrow
\mathrm{RH}.
}
\]
The Jensen--Pólya literature confirms that hyperbolicity of the full Jensen family is the relevant RH-equivalent target; it does not supply the missing theta-specific all-degree theorem here.

**Current conclusion:** this is a substantial exact reduction, but it is not a proof of RH. RH must not be declared proved until the all-degree theta-specific preservation/Gram theorem is actually established.
