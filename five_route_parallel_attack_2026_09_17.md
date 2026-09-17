# Five-route parallel RH attack — 2026-09-17

## Status

This note attempts all five proof-bearing routes simultaneously: Nyman–Beurling construction, adjoint arithmetic sampling, theta/Jensen hyperbolicity, Li positivity, and Weil positivity. All statements below are separated into exact unconditional results versus remaining RH-equivalent walls. **RH is not proved here.**

---

## Route 1 — Nyman–Beurling: explicit arithmetic residual

Let
\[
A_N(s)=\sum_{n\le N}c_n n^{-s}.
\]
The critical-line target norm is
\[
E(A_N)^2=\frac1{2\pi}\int_{\mathbb R}\left|\frac{1-\zeta(\frac12+it)A_N(\frac12+it)}{\frac12+it}\right|^2dt.
\]
A necessary admissibility condition appears immediately at the pole of \(\zeta\):
\[
\boxed{A_N(1)=0.}
\]
Indeed, if \(A_N(1)\neq0\), then \(\zeta(s)A_N(s)\) has a nonzero pole at \(s=1\); the inverse Mellin residual has a non-decaying constant component and the corresponding \(L^2\) norm diverges.

This kills the naive raw Möbius truncation
\[
A_N^{\mu}(s)=\sum_{n\le N}\mu(n)n^{-s}
\]
unless accidentally \(\sum_{n\le N}\mu(n)/n=0\).

For \(\Re s>1\),
\[
\zeta(s)A_N^{\mu}(s)-1
=\sum_{k>N}a_N(k)k^{-s},
\qquad
a_N(k)=\sum_{\substack{d\mid k\\d\le N}}\mu(d).
\]
The inverse Mellin transform of \(k^{-s}/s\) is \(1_{(0,1/k)}\), so formally/after the standard Mellin-Plancherel justification the raw residual is governed by
\[
S_N(y)=\sum_{N<k\le y}a_N(k)
=\sum_{d\le N}\mu(d)\left\lfloor\frac yd\right\rfloor-1.
\]
Thus the constructive NB problem becomes: choose admissible coefficients \(c_n\) with \(A_N(1)=0\) and prove the associated weighted step-function residual tends to zero. This is a concrete arithmetic approximation problem, not a finite Gram-positivity problem.

**Wall:** no explicit RH-independent admissible coefficient family with a proved \(E(A_N)\to0\) estimate has been obtained.

---

## Route 2 — Adjoint arithmetic sampling: compact-support uniqueness theorem

Write
\[
g_f(t)=\frac{\overline{\zeta(\frac12+it)}}{\frac12-it}f(t).
\]
Then \(B^*f=0\) implies
\[
\widehat g_f(\log n)=0\qquad(n=1,2,3,\dots).
\]

### Exact partial theorem
Assume additionally that \(g_f\) is compactly supported, say \(\operatorname{supp}g_f\subset[-T,T]\). Then
\[
F(z)=\int_{-T}^T g_f(t)e^{itz}\,dt
\]
is an entire function of exponential type at most \(T\) and is bounded on the real axis. Hence \(F\) lies in the Cartwright class and, if nonzero, its zero counting function satisfies
\[
N_F(R)=O(R).
\]
But the imposed zeros \(z=\log n\) satisfy
\[
\#\{n:\log n\le R\}=\lfloor e^R\rfloor,
\]
which grows exponentially. Therefore
\[
\boxed{\widehat g_f(\log n)=0\ \forall n\quad+\quad \operatorname{supp}g_f\text{ compact}\quad\Longrightarrow\quad g_f=0.}
\]
This gives genuine injectivity of the arithmetic sampling set on the compact-support subspace.

**Wall:** an arbitrary element of \(\ker B^*\) need not produce compactly supported \(g_f\). Truncating \(g_f\) destroys the exact zeros at \(\log n\). The missing theorem is a quasi-analytic/Hardy-space extension of the above uniqueness mechanism to the full zeta-weighted image class.

---

## Route 3 — Theta/Jensen: exact degree-2 variance reduction

Let
\[
M_n=\int_0^\infty \Phi_1(u)u^{2n}\,du,
\qquad
a_n=\frac{n!}{(2n)!}M_n>0,
\]
so the relevant coefficients are \(\gamma_n=(-1)^n a_n\).
The degree-2 Jensen polynomial is hyperbolic iff
\[
\gamma_{n+1}^2-\gamma_n\gamma_{n+2}\ge0,
\]
i.e.
\[
a_{n+1}^2\ge a_na_{n+2}.
\]
Since
\[
\frac{\left((n+1)!/(2n+2)!\right)^2}{(n!/(2n)!)( (n+2)!/(2n+4)!)}
=\frac{2n+3}{2n+1},
\]
we obtain the exact equivalent moment inequality
\[
\boxed{
\frac{M_{n+1}^2}{M_nM_{n+2}}\ge\frac{2n+1}{2n+3}.
}
\]
Define the tilted probability measure
\[
d\nu_n(u)=\frac{\Phi_1(u)u^{2n}}{M_n}\,du,
\qquad X=u^2.
\]
Then
\[
\frac{M_nM_{n+2}}{M_{n+1}^2}=\frac{\mathbb E_{\nu_n}X^2}{(\mathbb E_{\nu_n}X)^2}
=1+\frac{\operatorname{Var}_{\nu_n}(X)}{(\mathbb E_{\nu_n}X)^2}.
\]
Therefore degree-2 hyperbolicity is exactly
\[
\boxed{
\frac{\operatorname{Var}_{\nu_n}(X)}{(\mathbb E_{\nu_n}X)^2}
\le\frac{2}{2n+1}.
}
\]
This identifies a precise concentration inequality behind the factorial correction. Raw moment log-convexity alone gives the opposite-direction weak information and is insufficient.

**Wall:** RH requires all degrees and shifts. Literature already proves many finite/effective Jensen cases and eventual hyperbolicity for every fixed degree; the missing theorem is a uniform all-degree theta-specific total-positivity/Gram/variation-diminishing principle.

---

## Route 4 — Li coefficients: generating-function positivity target

Li's coefficients satisfy
\[
\log\xi\!\left(\frac1{1-z}\right)
=-\log2+\sum_{n\ge1}\frac{\lambda_n}{n}z^n
\]
near \(z=0\). Hence
\[
\boxed{
\frac{d}{dz}\log\xi\!\left(\frac1{1-z}\right)
=\sum_{n\ge1}\lambda_n z^{n-1}.
}
\]
Thus an RH-independent representation
\[
\frac{d}{dz}\log\xi\!\left(\frac1{1-z}\right)
=\int \frac{d\mu(x)}{1-zx},\qquad d\mu\ge0,
\]
(or any exact positive-moment representation with the same Taylor coefficients) would imply \(\lambda_n\ge0\) for all \(n\), hence RH.

The exact arithmetic eta-coefficient decomposition from earlier work remains available, but its remainder is signed and has not been converted to such a positive measure.

**Structural merger:** Bombieri–Lagarias identify Li positivity with Weil positivity evaluated on an explicit family of test functions. Therefore a complete positive Weil factorization would simultaneously close this route.

**Wall:** no unconditional positive measure / Stieltjes representation for the full Li generating derivative has been established.

---

## Route 5 — Weil positivity: finite-support prime-shift operator

For a compactly supported real test function \(f\), let
\[
g(a)=\int f(u)f(u-a)\,du=\langle f,T_af\rangle.
\]
On support \([-L,L]\), only prime powers with \(\log n\le2L\) contribute. The prime part of the Weil quadratic form can therefore be written exactly as the finite self-adjoint shift perturbation
\[
\boxed{
P_L=-2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}\,S_{\log n},
\qquad
S_a=\frac{T_a+T_a^*}{2}.
}
\]
If \(A_L\) denotes the archimedean-plus-pole constrained operator, then
\[
\boxed{W_L=A_L+P_L.}
\]
Crossing a single new prime-power threshold \(q\) changes the operator by the exact finite perturbation
\[
W_{L^+}=W_{L^-}-2\frac{\Lambda(q)}{\sqrt q}S_{\log q}.
\]
This gives a natural induction target: prove positivity is preserved at each threshold by controlling the new shift relative to the previous positive form.

A crude norm bound uses \(\|S_a\|\le1\):
\[
W_L\ge\left(c_L-2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}\right)I
\]
whenever \(A_L\ge c_LI\). This cannot plausibly globalize because the prime-weight sum grows on the scale \(e^L\); therefore any successful Weil proof must exploit arithmetic cancellation/geometry rather than triangle inequality.

**Wall:** prove a threshold-by-threshold Schur/comparison inequality for the full sequence of prime-power shifts, or an exact global factorization \(W=T^*T\), independently of RH.

---

# Combined conclusion

The five routes reduce to three genuinely distinct missing mechanisms:

1. **Arithmetic approximation / cyclicity:** construct admissible \(A_N\) with \(A_N(1)=0\) and prove \(E(A_N)\to0\), equivalently extend arithmetic-sampling uniqueness beyond compact support.
2. **Theta total positivity:** upgrade the exact factorially corrected moment inequalities from finite degree to all degrees/shifts.
3. **Global explicit-formula positivity:** factor or inductively control the Weil prime-shift operator; this would also imply Li positivity.

The strongest new exact partial result in this pass is the compact-support arithmetic-sampling uniqueness theorem, together with the exact degree-2 theta variance criterion and the pole-admissibility obstruction \(A_N(1)=0\) for NB Dirichlet-polynomial approximants.

None closes the global RH-equivalent step yet; therefore no complete RH proof is claimed.
