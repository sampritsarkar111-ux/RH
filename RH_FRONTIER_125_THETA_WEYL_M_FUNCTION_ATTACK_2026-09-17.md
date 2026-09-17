# RH Frontier 125 — Theta Weyl m-Function Attack — 2026-09-17

## Status
This frontier derives the Weyl/Stieltjes m-function of the theta Jacobi operator exactly from its spectral measure and derives an exact Laplace-transform identity linking m to Xi. It then tests the proposed direct relation to Xi'/Xi and identifies precisely why an unqualified equality cannot yet be claimed. This is a proof-bearing reduction, not a proof of RH.

## 1. Theta spectral measure and Jacobi operator

Start from
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)\cos(tu)\,du,
\qquad \Phi(-u)=\Phi(u),
\]
and define
\[
d\nu(x)=\frac{\Phi(\sqrt{x})}{\sqrt{x}}dx,
\qquad x>0,
\]
with moments
\[
M_k=\int_0^\infty x^k\,d\nu(x).
\]
Normalize
\[
d\mu(x)=\frac{d\nu(x)}{M_0}.
\]
The Jacobi operator \(J\) constructed from the orthonormal polynomials for \(\mu\) is self-adjoint and has spectral measure \(\mu\) at \(e_0\).

## 2. Weyl m-function — exact construction

Use the convention
\[
\boxed{
 m(z)=\langle e_0,(J-z)^{-1}e_0\rangle
      =\int_0^\infty\frac{d\mu(x)}{x-z},
 \qquad z\in\mathbb C\setminus[0,\infty).
}
\]
For \(\operatorname{Im}z>0\),
\[
\operatorname{Im}\frac1{x-z}>0,
\]
so
\[
\boxed{\operatorname{Im}m(z)>0\quad(\operatorname{Im}z>0).}
\]
Thus \(m\) is a Herglotz/Nevanlinna function. Its asymptotic normalization is
\[
 m(z)=-\frac1z-\frac{M_1/M_0}{z^2}-\frac{M_2/M_0}{z^3}+O(|z|^{-4})
\]
non-tangentially as \(|z|\to\infty\).

## 3. Continued-fraction/Jacobi representation

If
\[
J=\begin{pmatrix}
a_0&b_1&&\\b_1&a_1&b_2&\\&b_2&a_2&\ddots\\&&\ddots&\ddots\end{pmatrix},
\qquad b_n>0,
\]
then the Weyl function has the Jacobi continued fraction
\[
\boxed{
 m(z)=\cfrac1{a_0-z-\cfrac{b_1^2}{a_1-z-\cfrac{b_2^2}{a_2-z-\ddots}}}.
}
\]
Every coefficient is determined by theta moments through the Hankel determinants and orthogonal-polynomial recurrence.

## 4. Exact Xi-to-m Laplace identity

For \(\operatorname{Re}s>0\),
\[
\int_0^\infty e^{-st}\cos(t\sqrt{x})\,dt
=\frac{s}{s^2+x}.
\]
Because \(\Phi\) has rapid decay, Fubini/Tonelli and dominated convergence justify exchanging the integrals. Therefore
\[
\int_0^\infty e^{-st}\Xi(t)\,dt
=\int_0^\infty\frac{s}{s^2+x}\,d\nu(x).
\]
Since \(m(-s^2)=\int d\mu(x)/(x+s^2)\),
\[
\boxed{
\frac1{\Xi(0)}\int_0^\infty e^{-st}\Xi(t)\,dt
=s\,m(-s^2),
\qquad \operatorname{Re}s>0.
}
\]
Here \(\Xi(0)=M_0\).

Equivalently,
\[
\boxed{
 m(-s^2)=\frac1{s\Xi(0)}\int_0^\infty e^{-st}\Xi(t)\,dt.
}
\]
This is an exact theta-derived Weyl identity.

## 5. Why the desired direct \(m\leftrightarrow\Xi'/\Xi\) identity is harder

The logarithmic derivative is
\[
\frac{\Xi'(t)}{\Xi(t)},
\]
whose poles occur at zeros of \(\Xi\). In contrast, the Herglotz function \(m(z)\) has its natural singular support on the positive real spectral axis \([0,\infty)\) in the \(z\)-plane.

A naive identity such as
\[
 m(z)=C(z)\frac{\Xi'(z)}{\Xi(z)}+D(z)
\]
is therefore not justified by the spectral construction and has a variable/domain mismatch. In particular, \(\Xi\) is an even entire function of \(t\), whereas \(m\) is naturally a function of the spectral variable \(z=u^2\).

The exact variable correspondence suggested by the Laplace identity is
\[
 z=-s^2,
\]
not \(z=s\). Any successful logarithmic-derivative identity must respect this quadratic spectral map and its analytic continuation.

## 6. Stronger candidate: a Herglotz transform of the logarithmic derivative

A viable proof-bearing target is not necessarily \(m(z)=\Xi'(z)/\Xi(z)\), but an explicitly transformed quantity of the form
\[
\boxed{
 m(z)=\mathcal T\!\left[\frac{\Xi'}{\Xi}\right](z)+R(z),
}
\]
where \(\mathcal T\) is derived from the theta Laplace transform and \(R\) is explicit and zero-free. The required theorem would have to prove that the resulting function is Herglotz independently of RH and that its poles/atoms correspond exactly to zeros of \(\Xi\).

A particularly concrete next object is
\[
F(s)=\frac1{\Xi(0)}\int_0^\infty e^{-st}\Xi(t)\,dt=s\,m(-s^2),
\]
followed by a rigorous attempt to recover \(\Xi'/\Xi\) from \(F\) using the differential/functional identities of the completed theta kernel.

## 7. Necessary zero-correspondence test

Suppose an exact formula eventually yields a Herglotz function whose poles correspond to \(t=\pm\rho\). Herglotz theory then forces those spectral parameters to lie on the real axis. To imply RH, one must additionally prove:

1. every nontrivial zero of \(\zeta(s)\) corresponds to a pole/eigenvalue of this spectral object;
2. every such spectral parameter corresponds to a zero of \(\Xi\);
3. multiplicities are preserved;
4. no zero is lost under analytic continuation or transform inversion;
5. the normalization does not introduce zeros.

None of these zero-correspondence statements is assumed in this frontier.

## 8. Adversarial checkpoint

The identity
\[
\Xi(t)/\Xi(0)=\langle e_0,\cos(t\sqrt J)e_0\rangle
\]
and the Herglotz property of \(m\) hold for any positive theta-derived spectral measure. Therefore they cannot by themselves prove RH. The missing ingredient must use a genuinely special modular/theta relation connecting the Weyl object to the logarithmic derivative or a perturbation determinant.

## 9. Verdict

### Proven in this frontier
- exact theta spectral measure;
- self-adjoint Jacobi operator;
- exact Herglotz Weyl m-function;
- exact Jacobi continued fraction;
- exact Laplace identity
  \[
  m(-s^2)=\frac1{s\Xi(0)}\int_0^\infty e^{-st}\Xi(t)\,dt.
  \]

### Still open
\[
\boxed{
\text{theta modular structure}
\Longrightarrow
\text{Weyl/perturbation determinant identity for }\Xi'/\Xi
\Longrightarrow
\text{real-zero theorem}.
}
\]

No complete proof of RH is claimed.
