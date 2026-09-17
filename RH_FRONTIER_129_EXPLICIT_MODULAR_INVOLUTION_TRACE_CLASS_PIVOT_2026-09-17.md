# RH Frontier 129 — Explicit Modular Involution and Trace-Class Pivot — 2026-09-17

## Status
This frontier performs the requested next derivation rather than assuming a determinant. It gives the exact Hilbert-space realization of the theta modular involution, computes its Mellin action and square, and proves an obstruction: the bare modular involution is an involution and therefore cannot itself be the nontrivial compact/trace-class determinant kernel on an infinite-dimensional space. The correct determinant target must be a trace-class sandwich around the modular involution.

## 1. Exact modular involution

Use the Hilbert space
\[
\mathcal H_\theta=L^2((0,\infty),t^{-1/2}dt).
\]
Define
\[
\boxed{(Uf)(t)=t^{-1/2}f(1/t).}
\]
A direct substitution \(u=1/t\) gives
\[
\|Uf\|_{\mathcal H_\theta}^2
=\int_0^\infty t^{-1}|f(1/t)|^2t^{-1/2}dt
=\int_0^\infty |f(u)|^2u^{-1/2}du,
\]
so \(U\) is unitary. Also
\[
\boxed{U^2=I,\qquad U^*=U.}
\]
Thus the modular involution is an exact self-adjoint unitary symmetry.

## 2. Mellin linearization

For
\[
(Mf)(z)=\int_0^\infty f(t)t^{z-1}dt,
\]
initially where the integral converges absolutely,
\[
M[Uf](z)=\int_0^\infty t^{-1/2}f(1/t)t^{z-1}dt
=Mf(1/2-z).
\]
Hence
\[
\boxed{MUM^{-1}:g(z)\mapsto g(1/2-z).}
\]
The symmetry axis is \(\Re z=1/4\) in this normalization. After the usual completed-zeta re-centering, this is equivalent to the functional-equation reflection \(s\mapsto1-s\).

## 3. Decisive obstruction: \(U\) cannot itself be the Fredholm kernel

Because \(U^2=I\), every nonzero vector in either eigenspace has eigenvalue \(\pm1\). On the infinite-dimensional spaces of even/odd Mellin-reflection functions, these eigenspaces are infinite-dimensional. Therefore \(U\) is not compact and hence not trace class.

Consequently the tempting object
\[
\det_F(I-U)
\]
is not defined in the ordinary Fredholm sense on \(\mathcal H_\theta\).

This closes one false construction permanently:
\[
\boxed{\text{bare modular involution}\neq\text{Fredholm determinant kernel}.}
\]

## 4. Correct trace-class construction

Introduce operators \(A_s,B_s\) whose kernels/weights are derived from the completed theta factors and satisfy sufficient Hilbert-Schmidt bounds. Define
\[
\boxed{K_s=A_sUB_s.}
\]
If \(A_s,B_s\in\mathfrak S_2\) (Hilbert-Schmidt), then
\[
K_s\in\mathfrak S_1,
\qquad
\|K_s\|_1\le \|A_s\|_2\|B_s\|_2.
\]
Thus \(\det_F(I-K_s)\) is legitimate.

The modular involution remains exact, while the trace-class weights carry the analytic information that can generate a discrete determinant.

## 5. Trace powers

For a trace-class \(K_s\),
\[
\log\det(I-K_s)
=-\sum_{n\ge1}\frac1n\operatorname{tr}(K_s^n)
\]
whenever \(\|K_s\|<1\), with analytic continuation thereafter.

For \(K_s=A_sUB_s\), cyclicity gives
\[
\operatorname{tr}(K_s^n)
=\operatorname{tr}\big((B_sA_sU)^n\big).
\]
Because \(U^2=I\), every even power reduces to products of the paired operator \(B_sA_s\) and its modular conjugate \(U(B_sA_s)U\). In particular,
\[
\operatorname{tr}(K_s^2)
=\operatorname{tr}\big(A_sU B_sA_sU B_s\big),
\]
and higher powers are exact cyclic modular pairings. Any claimed Xi determinant must reproduce the corresponding theta lattice pairings term-by-term or via a rigorously summed identity.

## 6. What the theta comparison must actually prove

The required identity is now sharpened to
\[
\boxed{
\det_F(I-A_sUB_s)=E(s)\Xi(s),
\qquad E(s)\neq0.
}
\]
This cannot be established by matching only \(\operatorname{tr}K_s\), finitely many traces, asymptotics, or Taylor coefficients. Equality of the full determinant is required.

The first nontrivial exact tests are
\[
\operatorname{tr}(K_s),\quad
\operatorname{tr}(K_s^2),\quad
\operatorname{tr}(K_s^3),
\]
followed by the all-order trace identity
\[
-\frac{d}{ds}\log\det(I-K_s)
=\operatorname{tr}\big((I-K_s)^{-1}K_s'\big).
\]
This must equal \(\Xi'(s)/\Xi(s)+E'(s)/E(s)\).

## 7. New exact bottleneck

The abstract weights \(A_s,B_s\) are not yet determined. The remaining construction is therefore precise:

1. start with the explicit completed Riemann theta kernel;
2. split it into its two modular halves before scalar collapse;
3. derive the corresponding kernels of \(A_s\) and \(B_s\);
4. prove Hilbert-Schmidt estimates;
5. calculate the first three traces exactly;
6. identify the all-order trace generating function;
7. compare the resulting Fredholm determinant with the canonical/theta representation of \(\Xi\).

No RH proof is claimed until this determinant equality and the subsequent zero-correspondence theorem are proved.

## Verdict

The requested chain has now advanced from a formal modular operator to an exact operator-theoretic obstruction and the correct trace-class architecture:
\[
\boxed{
\text{theta modular involution }U
\xrightarrow{\;A_s\,\cdot\,B_s\;}
K_s\in\mathfrak S_1
\xrightarrow{\operatorname{tr}K_s^n}
\log\det(I-K_s)
\stackrel{?}{=}
\log\Xi(s)+\text{zero-free term}.
}
\]
The unsolved part is now the explicit derivation of \(A_s,B_s\) from the completed theta kernel and the all-order determinant identity.
