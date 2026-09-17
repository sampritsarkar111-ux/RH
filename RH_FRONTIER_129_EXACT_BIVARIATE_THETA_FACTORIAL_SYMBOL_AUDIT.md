# Frontier 129 — Exact bivariate stability symbol of the unsummed theta/factorial operator

Date: 2026-09-17

## 0. Conclusion first

The exact bivariate symbol splits into two logically different objects.

1. The **factorial-only symbol** is stable in every degree. This is now an unconditional theorem: the diagonal sequence
\[
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!}
\]
is a Laguerre multiplier sequence, so its algebraic symbol is stable for every degree.

2. The **full unsummed theta/factorial symbol** is exactly the Jensen polynomial of the completed Xi coefficients. Its stability for every shift and every degree is therefore the missing theta-specific statement; the factorial symbol by itself does not imply it.

No RH or zero-location assumption is used anywhere below.

---

## 1. Completed unsummed theta kernel

Use
\[
\phi_m(u)=\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad
\Phi(u)=\sum_{m\ge1}\phi_m(u).
\]
The completed theta transformation gives \(\Phi(-u)=\Phi(u)\), and the completed kernel is positive after the full lattice sum is formed.

The crucial analytic rule is retained here:
\[
\boxed{\text{form the completed sum }\Phi(u)=\sum_m\phi_m(u)\text{ before any global Mellin/moment integration.}}
\]
Individual lattice terms are not being treated as separate positive measures.

Define
\[
M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du,
\qquad
\gamma_k=\frac{M_k}{(2k)!}.
\]
No zero information is used.

---

## 2. Exact factorial diagonal operator

For fixed shift \(n\), define on polynomials of degree at most \(d\)
\[
\boxed{
\mathcal T_n\!\left[\sum_{j=0}^{d}a_jz^j\right]
=
\sum_{j=0}^{d}
\lambda_j^{(n)}a_jz^j,
\qquad
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!}.
}
\]
By duplication,
\[
\lambda_j^{(n)}
=\frac{1}{4^j\,(n+\tfrac12)_j\,(n+1)_j}.
\]
Hence the Pólya–Schur exponential generating function is exactly
\[
\boxed{
\Psi_n(z)=
\sum_{j\ge0}\frac{\lambda_j^{(n)}}{j!}z^j
={}_0F_2\!\left(;n+\tfrac12,n+1;\frac z4\right).
}
\]

---

## 3. Exact bivariate algebraic symbol

For degree \(d\), the Borcea–Brändén symbol is
\[
\boxed{
G_{n,d}(x,y)
:=\mathcal T_n[(x+y)^d]
=
\sum_{j=0}^{d}\binom dj
\frac{(2n)!}{(2n+2j)!}
 x^j y^{d-j}.
}
\]
Equivalently,
\[
G_{n,d}(x,y)=y^d\,g_{n,d}(x/y),
\qquad
g_{n,d}(z)=\sum_{j=0}^{d}\binom dj\lambda_j^{(n)}z^j.
\]
For a homogeneous real polynomial with positive coefficients, stability in the two upper half-planes is equivalent here to all zeros of \(g_{n,d}\) being real and non-positive.

This is the exact algebraic symbol of the factorial operator, with no theta or zero-location input.

---

## 4. All-degree stability of the factorial symbol

Set
\[
\varphi_n(t):=\frac{1}{\Gamma(2t+2n+1)}.
\]
Its zeros are
\[
 t=-n-\frac12-\frac{k}{2},
\qquad k=0,1,2,\ldots,
\]
so every zero is real and strictly negative. Since the reciprocal Gamma function is Laguerre–Pólya and affine real rescaling preserves the class, \(\varphi_n\in\mathcal{LP}(-\infty,0)\).

Moreover
\[
\varphi_n(j)=\frac1{(2n+2j)!}
\quad\Longrightarrow\quad
\lambda_j^{(n)}=(2n)!\,\varphi_n(j).
\]
Laguerre's theorem implies that a sequence obtained by sampling an \(\mathcal{LP}(-\infty,0)\) function at the nonnegative integers is a multiplier sequence. Therefore
\[
\boxed{\{\lambda_j^{(n)}\}_{j\ge0}\text{ is a multiplier sequence for every }n\ge0.}
\]
By the Pólya–Schur algebraic characterization, for every degree \(d\), \(g_{n,d}\) has only real zeros of one sign; since its coefficients are positive, they are all negative. Thus
\[
\boxed{G_{n,d}(x,y)\text{ is stable for every }n,d.}
\]

This is the first genuine all-degree theorem recovered from the factorial side.

Literature check: Laguerre's theorem and the definition of Laguerre multiplier sequences are stated in the Craven–Csordas survey; it explicitly notes that Laguerre sequences are multiplier sequences. The Borcea–Brändén framework identifies \(T[(x+y)^d]\) as the algebraic symbol controlling stability preservation.

---

## 5. Exact low-degree algebraic checks

These are exact, not numerical.

### Degree 2
\[
g_{n,2}(z)=1+2\lambda_1z+\lambda_2z^2,
\]
and
\[
\boxed{
\operatorname{Disc}(g_{n,2})
=\frac{4n+5}{(n+1)^2(n+2)(2n+1)^2(2n+3)}>0.
}
\]

### Degree 3
\[
\boxed{
\operatorname{Disc}(g_{n,3})
=
\frac{27\left(64n^3+360n^2+656n+381\right)}
{16(n+1)^4(n+2)^3(n+3)^2(2n+1)^4(2n+3)^3(2n+5)^2}>0.
}
\]

### Degree 4
\[
\boxed{
\operatorname{Disc}(g_{n,4})
=\frac{27P_6(n)}{4(n+1)^6(n+2)^5(n+3)^4(n+4)^3(2n+1)^6(2n+3)^5(2n+5)^4(2n+7)^3}>0,
}
\]
where
\[
\begin{aligned}
P_6(n)=&4096n^6+61440n^5+377856n^4+1216384n^3\\
&+2154896n^2+1983656n+736797.
\end{aligned}
\]
All coefficients of \(P_6\) are positive for \(n\ge0\).

These finite-degree checks are consistent with the all-degree Laguerre-multiplier theorem, but the theorem—not the checks—is what supplies the unrestricted degree conclusion.

---

## 6. The exact UNSUMMED theta/factorial symbol

Define the theta/factorial operator
\[
\boxed{
(\mathcal A_n p)(x)
:=
\frac1{(2n)!}
\int_{\mathbb R}
\Phi(u)u^{2n}
\bigl(\mathcal T_np\bigr)(u^2x)\,du.
}
\]
Using \(\gamma_k=M_k/(2k)!\), one obtains exactly
\[
\mathcal A_n[z^j]=\gamma_{n+j}x^j.
\]
Therefore its degree-\(d\) algebraic symbol is
\[
\boxed{
\Sigma_{n,d}(x,y)
:=\mathcal A_n[(z+y)^d]
=\sum_{j=0}^{d}\binom dj\gamma_{n+j}x^j y^{d-j}.
}
\]
Keeping the theta lattice visibly unsummed until after the completed kernel is formed,
\[
\boxed{
\Sigma_{n,d}(x,y)
=
\frac1{(2n)!}
\int_{\mathbb R}
\left(\sum_{m\ge1}\phi_m(u)\right)u^{2n}
G_{n,d}(u^2x,y)\,du.
}
\]
This is the exact bivariate symbol requested in the present frontier.

Crucially, the inner polynomial \(G_{n,d}(u^2x,y)\) is stable for every \(u\neq0\). The remaining question is whether the completed theta integration preserves that stability.

---

## 7. Exact obstruction to the naive composition argument

The implication
\[
\text{every local }G_{n,d}(u^2x,y)\text{ stable}
\quad\Longrightarrow\quad
\int G_{n,d}(u^2x,y)\,d\mu(u)\text{ stable}
\]
is false for general positive measures.

An exact counterexample is
\[
(X+Y)^2+(X+3Y)^2
=2(X^2+4XY+5Y^2),
\]
whose dehomogenization is
\[
2(z^2+4z+5)=2\bigl((z+2)^2+1\bigr),
\]
with non-real roots \(-2\pm i\). Thus positive averaging of stable bivariate polynomials is not, by itself, a stability-preserving operation.

Therefore the following tempting proof is invalid:
\[
G_{n,d}(u^2x,y)\text{ stable pointwise}
+\Phi(u)\ge0
\Longrightarrow
\Sigma_{n,d}\text{ stable}.
\]
A theta-specific closure theorem is genuinely required.

---

## 8. What stability of the full symbol means

Since
\[
\Sigma_{n,d}(x,y)=J_{d,n}(x,y),
\]
stability of the full symbol for every \(n,d\) is exactly hyperbolicity of every Jensen polynomial.

### Degree 2 exact gate
\[
\Sigma_{n,2}(x,1)=\gamma_n+2\gamma_{n+1}x+\gamma_{n+2}x^2
\]
is hyperbolic iff
\[
\boxed{\gamma_{n+1}^2\ge\gamma_n\gamma_{n+2}.}
\]

### Degree 3 exact gate
With
\[
q_j=\frac{\gamma_{n+j}}{\gamma_n},\qquad
P_n=\frac{q_2}{q_1^2},\qquad
Q_n=\frac{q_3}{q_1^3},
\]
the full cubic is hyperbolic exactly when
\[
\boxed{
P_n\le1,
\qquad
|Q_n-(3P_n-2)|\le2(1-P_n)^{3/2}.
}
\]
This is the first nontrivial global theta test.

---

## 9. Numerical theta check (evidence only)

Using high-precision evaluation of the standard completed Xi function at \(t=0\), the first coefficients are approximately
\[
\gamma_0=0.4971207781883141,
\quad
\gamma_1=0.01148597215757272,
\quad
\gamma_2=1.234520180703180\times10^{-4},
\]
\[
\gamma_3=8.32355481385527\times10^{-7},
\quad
\gamma_4=3.99222655134414\times10^{-9}.
\]
The degree-2 ratio
\[
\gamma_{n+1}^2/(\gamma_n\gamma_{n+2})
\]
is approximately
\[
2.1496878850,\quad1.5941154994,\quad1.4057377748,\quad1.3100630986
\]
for \(n=0,1,2,3\), respectively.

For the cubic theta symbol, the scale-free discriminant factor
\[
\mathcal F(P,Q)=-Q^2+(6P-4)Q+3P^2-4P^3
\]
has the approximate values
\[
0.06400129246,\quad0.04865383647,\quad0.03259170079
\]
for \(n=0,1,2\).

These are numerical checks only; they are not used as proof.

---

## 10. Exact status of the frontier

The calculation has produced a clean split:

\[
\boxed{
\underbrace{\text{factorial symbol stable in all degrees}}_{\text{proved}}\quad
\not\Rightarrow\quad
\underbrace{\text{unsummed theta symbol stable in all degrees}}_{\text{still open in this project}}.
}
\]

The remaining bridge is therefore narrower than before. It is no longer the factorial operator. The exact missing theorem is:
\[
\boxed{
\Sigma_{n,d}(x,y)
=
\frac1{(2n)!}
\int
\Phi(u)u^{2n}G_{n,d}(u^2x,y)\,du
\quad\text{is stable for every }n,d,
}
\]
proved directly from the completed unsummed theta lattice, without importing zero locations.

Equivalently, one needs a theta-specific stability-preserving transformation that acts on the family \(u\mapsto G_{n,d}(u^2x,y)\) and survives the completed lattice integration. Generic positive averaging is insufficient.

No RH proof is claimed by this frontier.
