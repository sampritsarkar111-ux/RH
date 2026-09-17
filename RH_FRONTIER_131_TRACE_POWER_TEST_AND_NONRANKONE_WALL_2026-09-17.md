# RH Frontier 131 — Exact Trace-Power Test and the Non-Rank-One Determinant Wall — 2026-09-17

## 1. Correct theta normalization

Let
\[
\omega(x)=\sum_{n\ge1}(2\pi^2n^4x^2-3\pi n^2x)e^{-\pi n^2x}.
\]
Then
\[
\xi(s)=\int_0^\infty\omega(x)x^{s/2-1}\,dx,
\qquad
\omega(1/x)=x^{1/2}\omega(x).
\]
With \(x=e^u\), define
\[
g(u)=e^{u/4}\omega(e^u).
\]
Then \(g(-u)=g(u)\), and
\[
\Xi(z)=\xi(1/2+iz)=\int_{\mathbb R}g(u)e^{izu/2}\,du.
\]
This normalization agrees with the standard theta formula after the coordinate rescaling used in the usual \(\Phi\)-kernel representation.

## 2. Exact rank-one operator and every trace power

For real \(z\), set
\[
v_z(u)=g(u)^{1/2}e^{izu/4},
\qquad
R_z=|v_z\rangle\langle Uv_z|,
\qquad (Uf)(u)=f(-u).
\]
Then
\[
\operatorname{tr}R_z=\Xi(z).
\]
Because \(R_z\) is rank one,
\[
R_z^2=\Xi(z)R_z,
\]
and therefore, for every \(n\ge1\),
\[
\boxed{\operatorname{tr}(R_z^n)=\Xi(z)^n.}
\]
Consequently, for any scalar analytic \(\lambda(z)\), whenever the Fredholm expansion is valid,
\[
\log\det(I-\lambda R_z)
=-\sum_{n\ge1}\frac{\lambda(z)^n\Xi(z)^n}{n}
=\log(1-\lambda(z)\Xi(z)).
\]
Hence the entire trace hierarchy of this rank-one modular construction contains no new spectral information beyond the single scalar \(\Xi(z)\).

## 3. Exact conclusion from the test

A determinant representation of the form
\[
\Xi(z)=E(z)\det(I-K_z)
\]
with \(E(z)\neq0\) cannot be obtained from a rank-one theta matrix element by merely taking powers or resumming them. The operator must contain genuinely independent cyclic degrees of freedom.

Equivalently, for
\[
\log\det(I-K_z)=-\sum_{n\ge1}\frac{\operatorname{tr}K_z^n}{n},
\]
the quantities \(\operatorname{tr}K_z^n\) must not reduce to powers of \(\Xi(z)\).

## 4. Concrete non-rank-one target

The next candidate must be a theta-derived integral operator on \(L^2(0,\infty)\), retaining the two-variable modular product
\[
M(a,b)=\Phi(a+b)\Phi(a-b),
\]
where \(\Phi\) is the standard even Riemann theta kernel.

A legitimate candidate \(K_z(a,b)\) must satisfy all of:

1. \(K_z\) is trace class for each \(z\), with locally trace-norm analytic dependence on \(z\);
2. its diagonal trace contains the exact one-variable Xi information;
3. its off-diagonal part retains \(M(a,b)\), so \(\operatorname{tr}K_z^2\) and higher cyclic integrals contain genuinely two-variable theta correlations;
4. the all-order determinant agrees with \(\Xi\) up to a zero-free factor.

The second trace has the exact form
\[
\operatorname{tr}K_z^2
=\int_0^\infty\!\int_0^\infty
K_z(a,b)K_z(b,a)\,da\,db,
\]
provided the kernel is trace-class/HS in the required sense. Likewise,
\[
\operatorname{tr}K_z^3
=\iiint K_z(a,b)K_z(b,c)K_z(c,a)\,da\,db\,dc.
\]
These are the first places where arithmetic information not present in the rank-one scalar can enter.

## 5. The exact all-order criterion

Suppose such a \(K_z\) is found. Then define
\[
L(z)=-\sum_{n\ge1}\frac{\operatorname{tr}K_z^n}{n}.
\]
The determinant identity requires
\[
\boxed{
L(z)=\log\Xi(z)-\log E(z)
}
\]
on every simply connected zero-free domain, with analytic continuation across the plane controlled by the canonical product.
Differentiating gives the stronger test
\[
\boxed{
-\operatorname{tr}\big((I-K_z)^{-1}K_z'\big)
=\frac{\Xi'(z)}{\Xi(z)}-\frac{E'(z)}{E(z)}.
}
\]
This is the equation that a genuine determinant construction must ultimately satisfy.

## 6. RH-specific spectral requirement

Even exact equality of determinants would not finish RH unless the determinant is tied to a real spectral parameter. The required final implication is
\[
\det(I-K_z)=0
\Longrightarrow z\in\mathbb R,
\]
with the converse and multiplicity matching for every nontrivial Xi zero.
A proof can instead establish an equivalent de Branges/Hermite-Biehler property, but that property itself must be derived from the theta operator rather than assumed.

## 7. Status

Closed exactly:
- theta modular involution;
- exact Xi matrix element;
- all rank-one trace powers;
- exact proof that rank-one resummation cannot produce the required Xi spectral determinant.

Still open:
- explicit non-rank-one theta operator;
- trace-class proof;
- exact \(\operatorname{tr}K_z^2\) and \(\operatorname{tr}K_z^3\) matching;
- all-order determinant identity;
- real-zero spectral/de Branges mechanism.

No RH proof is claimed.
