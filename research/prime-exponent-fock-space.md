# Prime-Exponent Fock Space and the Ternary Coupling — RH research program

## Status
Research construction. No RH proof is claimed.

## 1. Prime-exponent basis

Let \(\mathcal V\) be the set of finite-support vectors
\[
\mathbf v=(v_2,v_3,v_5,\ldots),\qquad v_p\in\mathbb N_0.
\]
Associate \(n(\mathbf v)=\prod_p p^{v_p}\). Unique factorization makes this a bijection \(\mathcal V\leftrightarrow\mathbb N\).

Define the Hilbert space \(\mathcal F=\ell^2(\mathcal V)\) with orthonormal basis \(e_{\mathbf v}\).

## 2. Arithmetic Hamiltonian

Define on the natural finite-support domain
\[
H_0e_{\mathbf v}=E(\mathbf v)e_{\mathbf v},
\qquad
E(\mathbf v)=\sum_p v_p\log p=\log n(\mathbf v).
\]
Thus \(H_0\) is diagonal and self-adjoint.

For \(\Re s>1\), the trace of the heat/partition operator is formally and then absolutely
\[
\operatorname{Tr}(e^{-sH_0})
=\sum_{n\ge1}n^{-s}
=\zeta(s)
=\prod_p(1-p^{-s})^{-1}.
\]
This is a trace/partition representation of \(\zeta\), not a spectral proof of RH.

## 3. Creation and annihilation coordinates

For each prime \(p\), define on basis vectors
\[
a_p^+e_{\mathbf v}=e_{\mathbf v+\mathbf e_p},
\qquad
a_p^-e_{\mathbf v}=
\begin{cases}
e_{\mathbf v-\mathbf e_p},&v_p>0,\\
0,&v_p=0.
\end{cases}
\]
Then \(a_p^-=(a_p^+)^*\) on the finite-support core and
\[
H_0=\sum_p(\log p)N_p,
\qquad N_pe_{\mathbf v}=v_pe_{\mathbf v}.
\]
The sum is pointwise finite on each basis vector.

## 4. Balanced-ternary coupling

Let \(D_k(n)\in\{-1,0,1\}\) be the balanced-ternary digit at position \(k\). Define the bounded finite-coordinate observable
\[
T_k e_{\mathbf v}=D_k(n(\mathbf v))e_{\mathbf v}.
\]
A general finite-rank coupling can be written
\[
V_R=\sum_{p\le R}\sum_{k<K}c_{p,k}
\bigl(a_p^++a_p^-\bigr)T_k.
\]
If \(c_{p,k}\in\mathbb R\), then each summand is symmetric on the finite-support core; a rigorous self-adjoint realization still requires a domain/relative-boundedness argument.

## 5. Proof-bearing obstruction

A useful coupling is not enough. We need an explicit, rigorously controlled \(V\) such that a regularized determinant satisfies
\[
\det_*\!\bigl(I-\mathcal H(s)\bigr)=C(s)\,\xi(s),
\qquad C(s)\neq0,
\]
and whose logarithmic determinant has the exact prime-power expansion
\[
-\log\det_*(I-\mathcal H(s))
=\sum_p\sum_{r\ge1}\frac{p^{-rs}}r
=\log\zeta(s)
\]
where the series converges, with analytic continuation justified separately.

The diagonal \(H_0\) alone does not give the required critical-line spectral theorem: its partition trace is \(\zeta\), but it is not a construction of the zero set of \(\xi\).

## 6. Ternary digit operator and prime valuation operator

For integers \(m,n\), define
\[
K_{K,R}(m,n)
=\sum_{k<K}w_kD_k(m)D_k(n)
+\sum_{p\le R}u_p\,\phi(v_p(m),v_p(n)),
\]
with nonnegative weights when PSD is desired. Any PSD statement must be proved for the exact kernel and then connected to the Weil quadratic form; generic Gram positivity is insufficient.

## 7. Adversarial finite tests

For finite cutoffs:
1. Verify \(H_0=H_0^*\).
2. Verify \([H_0,N_p]=0\) and \([H_0,a_p^+]=(\log p)a_p^+\).
3. Compare \(\operatorname{Tr}(e^{-sH_0})\) against a direct truncated zeta sum.
4. Test Hermiticity of every proposed \(V\).
5. Test whether candidate determinant/log-trace identities fail at small cutoffs.
6. Never infer RH from finite-dimensional spectral reality or numerical zero matching.

## 8. Research gate

The next proof-bearing gate is now sharply stated:

> Construct a nontrivial ternary-prime coupling \(V\) with a controlled self-adjoint realization and prove an exact determinant/explicit-formula identity that contains both the Euler prime-power terms and the archimedean theta term.

Until that identity is proved, the program remains exploratory.
