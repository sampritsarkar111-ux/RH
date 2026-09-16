# RH Next Frontier 19 — Canonical Jensen normalization audit and a 2026 normalization correction

Date: 2026-09-16

## 1. Exact canonical setup

Let

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\psi(z):=\xi(1/2+z).
\]

The Jensen-polynomial literature used by Griffin–Ono–Rolen–Thorner–Tripp–Wagner defines

\[
\boxed{\psi(z)=\sum_{n\ge0}\frac{\gamma_n}{n!}z^{2n}},
\qquad
\boxed{J_{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j}.
\]

This is the normalization in which Pólya's criterion states RH iff every \(J_{d,n}\) is hyperbolic.

Now write the standard even Xi expansion

\[
\Xi(t):=\xi(1/2+it)=\sum_{n\ge0}(-1)^n\frac{M_n}{(2n)!}t^{2n}.
\]

Since \(\psi(z)=\Xi(-iz)\), comparison gives the exact conversion

\[
\boxed{\gamma_n=\frac{n!}{(2n)!}M_n}
\]

(or \(8n!M_n/(2n)!\) if one instead defines the Taylor coefficients using \(8\xi\)). The scalar factor \(8\) is irrelevant for hyperbolicity but the factorial factor is not.

## 2. A concrete normalization error in a recent 2026 Jensen paper

A 2026 paper on asymptotic hyperbolicity writes the traditional coefficients

\[
M_n=\frac{(-1)^n\Xi^{(2n)}(0)}{(2n)!}
\]

and then identifies these directly with its \(\gamma(n)\), constructing

\[
\sum_{j=0}^d\binom dj M_{n+j}X^j.
\]

That is **not** the canonical GORZ/Pólya Jensen family above: the missing factor \(n!/(2n)!\) changes the polynomial family.

A decisive diagnostic is degree 2. For the canonical family,

\[
J_{2,n}(X)=\gamma_n+2\gamma_{n+1}X+\gamma_{n+2}X^2,
\]

so its discriminant is

\[
\Delta_{2,n}=4(\gamma_{n+1}^2-\gamma_n\gamma_{n+2}).
\]

Substituting \(\gamma_n=n!M_n/(2n)!\) gives

\[
\boxed{
\Delta_{2,n}
=4\frac{(n+1)!^2}{(2n+2)!^2}
\left[
M_{n+1}^2-\frac{2n+1}{2n+3}M_nM_{n+2}
\right].
}
\]

Thus canonical degree-2 hyperbolicity requires

\[
\boxed{
M_{n+1}^2\ge \frac{2n+1}{2n+3}M_nM_{n+2}.
}
\]

By contrast, the unscaled \(M_n\)-polynomial has discriminant proportional to \(M_{n+1}^2-M_nM_{n+2}\), which is non-positive for an ordinary positive moment sequence. These are different tests.

## 3. Numerical sanity check at n=0

Using the Xi coefficients

\[
\Xi(0)\approx0.4971207781883141,
\quad
[t^2]\Xi(t)\approx-0.01148597215757272,
\quad
[t^4]\Xi(t)\approx1.23452018070318\times10^{-4},
\]

we obtain

\[
M_0\approx0.4971207781883141,
\quad
M_1\approx0.02297194431514544,
\quad
M_2\approx0.002962848433687632.
\]

For the canonical coefficients (without the optional global factor 8),

\[
\gamma_0=M_0,
\quad
\gamma_1=\frac{M_1}{2},
\quad
\gamma_2=\frac{M_2}{12}.
\]

Hence

\[
\gamma_1^2-\gamma_0\gamma_2>0
\]

numerically, whereas

\[
M_1^2-M_0M_2<0.
\]

So the two degree-2 Jensen tests give opposite signs already at \(n=0\). This is a direct falsification of any claim that the unscaled moment polynomial is the same Jensen family as the canonical Pólya/GORZ family.

## 4. Re-derive the multiplier-sequence structure correctly

Set

\[
a_n:=\frac{n!}{(2n)!}.
\]

Then

\[
\sum_{n\ge0}(-1)^na_n\frac{x^n}{n!}
=\sum_{n\ge0}\frac{(-1)^nx^n}{(2n)!}
=\cos\sqrt{x}.
\]

The entire function \(\cos\sqrt{x}\) has only real zeros,

\[
x=\left(k+\tfrac12\right)^2\pi^2,
\qquad k\in\mathbb Z,
\]

so Pólya–Schur gives a genuine multiplier-sequence structure for \((-1)^na_n\), equivalently for \(a_n\) after the sign reversal \(x\mapsto-x\).

Therefore the canonical gamma sequence is obtained from the \(M_n\) sequence by a real-root-preserving coefficient multiplier:

\[
\boxed{\gamma_n=a_nM_n.}
\]

This is a real structural fact. It does **not** prove RH, because the multiplier theorem says: if the source exponential-generating function \(B(x)=\sum M_nx^n/n!\) is in the relevant Laguerre–Pólya class, then the transformed function is real-rooted. We do not currently have that missing LP statement for \(B\).

## 5. New exact reformulation of the remaining bridge

Define

\[
B(x):=\sum_{n\ge0}M_n\frac{x^n}{n!}.
\]

Then the multiplier operator \(T_a\), defined coefficientwise by

\[
T_a\left(\sum c_n\frac{x^n}{n!}\right)
=\sum a_nc_n\frac{x^n}{n!},
\]

satisfies

\[
\boxed{
T_aB(x)=\sum_{n\ge0}M_n\frac{x^n}{(2n)!}
=\Xi(\sqrt{-x}).
}
\]

Thus RH can be attacked through the exact diagram

\[
B
\xrightarrow{\;T_a\;}
\Xi(\sqrt{-x}),
\qquad
T_a\text{ is a multiplier-sequence operator}.
\]

The unresolved step is to prove an appropriate LP property for \(B\), or to construct a stronger direct theorem showing that this specific \(B\) lies in the preimage of LP under \(T_a\).

## 6. Why positivity of the Xi moment kernel is insufficient

The formal identity

\[
B(x)=\int_0^\infty\Phi_1(u)e^{xu^2}\,du
\]

follows from the Xi cosine representation when differentiation and summation are justified. However the standard kernel \(\Phi_1(u)\) changes sign, so this is not a positive-measure Laplace-transform proof of LP membership. Therefore an attempted shortcut through ordinary Stieltjes moment positivity is invalid.

## 7. Current proof status

No complete proof of RH has been obtained in this frontier.

The useful advance is a **normalization correction plus an exact operator bridge**:

1. the canonical Pólya/GORZ Jensen coefficients contain the factorial multiplier \(n!/(2n)!\);
2. this multiplier has an explicit Pólya–Schur generating function \(\cos\sqrt{x}\);
3. the RH problem can therefore be reframed as finding a real-root-preserving characterization of the preimage \(B\) under this multiplier operator;
4. the unscaled \(M_n\)-Jensen family used in some recent 2026 exposition is not the canonical family and cannot be substituted for it.

The remaining theorem needed for a complete proof is still global: a valid LP/preimage theorem for the actual Xi coefficient sequence, or an equivalent all-degree/all-shift hyperbolicity proof.
