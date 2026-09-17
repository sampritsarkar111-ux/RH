# RH Frontier 127 — Zero-Correspondence Audit and Perturbation-Determinant Pivot — 2026-09-17

## Status
This frontier performs the decisive adversarial test of the Weyl m-function route. The theta Jacobi operator obtained from the positive theta density is a multiplication operator with continuous spectral measure, so its Weyl function is a Cauchy transform with a branch cut on [0,∞), not a meromorphic function whose poles can directly enumerate the zeros of Xi. Therefore the hoped-for direct pole correspondence m ↔ Xi'/Xi cannot be the missing RH mechanism. The proof-bearing route must pivot from the Weyl function itself to a theta-derived perturbation determinant or another de Branges/Herglotz object whose discrete spectral data can encode Xi zeros.

## 1. Exact spectral type

The operator is
\[
(Af)(x)=xf(x),\qquad \mathcal H=L^2((0,\infty),d\mu),
\]
with
\[
d\mu(x)=\frac{\Phi(\sqrt{x})}{\Xi(0)\sqrt{x}}dx.
\]
Since the theta kernel \(\Phi\) is an ordinary positive density on \((0,\infty)\), \(\mu\) is absolutely continuous with respect to Lebesgue measure. Consequently the spectral measure at \(e_0\) has no atoms.

The Weyl function is
\[
 m(z)=\int_0^\infty\frac{d\mu(x)}{x-z}.
\]
By the Stieltjes inversion formula, its jump across the positive axis recovers the density:
\[
\boxed{
\frac{d\mu}{dx}(x)=\frac1\pi\lim_{\eta\downarrow0}\operatorname{Im}m(x+i\eta)
}
\]
for almost every \(x>0\).

Thus \(m\) is naturally a Herglotz function with continuous boundary spectrum rather than a discrete pole list.

## 2. Decisive obstruction to a naive zero correspondence

A nontrivial zero \(\rho\) of \(\Xi\) produces a pole of \(\Xi'/\Xi\) at \(\rho\). A meromorphic identity of the form
\[
 m(z)=C(z)\frac{\Xi'(z)}{\Xi(z)}+D(z)
\]
would therefore force matching poles unless \(C\) cancels every zero. But the theta-derived \(m\) has no isolated poles arising from the absolutely continuous theta density. Hence such an identity cannot be the correct untransformed relation.

This is not a failure of the theta Jacobi construction. It identifies a categorical mismatch:
\[
\boxed{
\text{continuous Cauchy transform}\neq\text{discrete zero divisor}.
}
\]

## 3. Correct pivot: perturbation determinant

A scalar rank-one perturbation of \(A\),
\[
A_\lambda=A+\lambda P_0,
\qquad P_0=|e_0\rangle\langle e_0|,
\]
has the formal Birman--Krein/Krein determinant factor
\[
\boxed{
\Delta_\lambda(z)=1+\lambda m(z)
}
\]
whenever the rank-one perturbation determinant is defined with the chosen normalization. Its zeros correspond to eigenvalues created by the perturbation (outside the essential spectrum) through
\[
1+\lambda m(z)=0.
\]

This is the first object in the current route capable of converting the Herglotz Weyl data into a discrete zero set.

However, an arbitrary constant \(\lambda\) cannot encode the Xi divisor. The missing theta-specific theorem is therefore to construct an explicit analytic coupling \(\lambda=\lambda(s)\), or a finite-rank theta perturbation, for which a rigorously normalized determinant satisfies
\[
\boxed{
\Delta(s)=E(s)\Xi(s)
}
\]
with \(E\) entire and zero-free.

## 4. Necessary determinant identity

A successful RH proof along this route must establish all of:

1. **Construction:** define a trace-class/finite-rank perturbation \(K(s)\) from the theta modular transformation, with a well-defined Fredholm determinant.
2. **Exact identity:** prove
   \[
   \det(I+K(s))=E(s)\Xi(s).
   \]
3. **Self-adjoint reality:** on real \(s\), the underlying operator/perturbation must be self-adjoint in the spectral representation.
4. **Herglotz/de Branges property:** prove the associated scalar determinant belongs to a class whose zeros are forced onto the real axis.
5. **Zero completeness:** prove equality of entire functions, not merely equality away from zeros or asymptotic agreement.

Only step 4 plus exact zero correspondence would close RH.

## 5. New concrete construction target from the theta transform

The exact identity already established is
\[
F(s):=s\,m(-s^2)
=\frac1{\Xi(0)}\int_0^\infty e^{-st}\Xi(t)\,dt.
\]
Rather than forcing \(F\) to equal \(\Xi'/\Xi\), seek a theta-derived operator-valued transform \(\mathcal K(s)\) satisfying a resolvent identity of the form
\[
\boxed{
\frac{d}{ds}\log\det(I+\mathcal K(s))
=\frac{\Xi'(s)}{\Xi(s)}+E_0'(s),
}
\]
where \(E_0\) is explicitly computable and entire.

Integrating this identity then gives
\[
\det(I+\mathcal K(s))=C e^{E_0(s)}\Xi(s).
\]
Normalization at \(s=0\) fixes \(C\).

The central proof obligation is now reduced to constructing \(\mathcal K(s)\) directly from the theta modular involution, not from assumed zero locations.

## 6. Modular involution as the required source of finite-rank structure

The completed theta kernel obeys a modular/Poisson transformation exchanging the small-parameter and large-parameter regimes. A useful operator formulation must preserve this involution rather than collapse it immediately into the positive density \(d\mu\). The positive measure loses precisely the discrete modular cancellation information that could generate a determinant.

Therefore the next derivation should retain the unsummed theta lattice and define a paired operator \(T\) between the two modular halves. Candidate proof-bearing objects include
\[
T(s)=W_s\,U\,W_s,
\]
where \(U\) implements the theta modular involution and \(W_s\) is a rigorously chosen multiplication/heat-semigroup weight. The target is a trace-class operator for which
\[
\det(I-T(s))
\]
is provably proportional to \(\Xi(s)\) after the gamma/exponential completion factors are included.

No such determinant identity is asserted here; it is the explicit next theorem to prove.

## 7. Zero correspondence theorem — exact final form

The ultimate theorem needed is:
\[
\boxed{
\Xi(\rho)=0
\iff
\rho\in\operatorname{Spec}_{\mathrm{disc}}(\mathcal A),
}
\]
for a theta-derived self-adjoint operator \(\mathcal A\), with multiplicities preserved.
Then self-adjointness gives \(\rho\in\mathbb R\), and because \(\Xi\) is the completed zeta function, this yields the critical-line statement after the standard change of variables.

The present frontier does **not** claim this theorem. It isolates the exact construction required to prove it.

## 8. Verdict

### Closed
- exact theta spectral measure;
- exact self-adjoint Jacobi operator;
- exact Herglotz Weyl function;
- exact Laplace transform relation to Xi;
- decisive identification of the continuous-spectrum/discrete-zero mismatch.

### Remaining proof-bearing wall
\[
\boxed{
\text{unsummed theta modular involution}
\Longrightarrow
\text{trace-class/self-adjoint perturbation}
\Longrightarrow
\text{Fredholm determinant}=E\Xi
\Longrightarrow
\text{complete real-zero correspondence}.
}
\]

No RH proof is claimed.
