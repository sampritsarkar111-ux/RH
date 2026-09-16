# Frontier 111 — cubic multi-copy factorisation target

Date: 2026-09-16

## 1. Exact four-copy representation

Let
\[
d\mu(u)=\Phi(u)\,du,\qquad Y=u^2,
\]
and write \(M_k=\int Y^k\,d\mu\). For the cubic Jensen gate of Frontier 110,
\[
Q_3^*=M_0^2M_3^2-90M_0M_1M_2M_3+2700M_0M_2^3+360M_1^3M_3-2700M_1^2M_2^2.
\]
Introduce four independent copies \(Y_1,Y_2,Y_3,Y_4\) of the same positive measure. Then each monomial is represented exactly as a product integral, e.g.
\[
M_0^2M_3^2
=\int Y_3^3Y_4^3\,d\mu_1d\mu_2d\mu_3d\mu_4,
\]
\[
M_0M_1M_2M_3
=\int Y_2Y_3^2Y_4^3\,d\mu_1d\mu_2d\mu_3d\mu_4,
\]
with analogous representations for the remaining terms.

A fully symmetrized kernel is therefore obtained by averaging over all permutations of the four copies:
\[
Q_3^*=\frac1{4!}\int_{\mathbb R^4}\mathcal S_3(Y_1,Y_2,Y_3,Y_4)\,\prod_{j=1}^4d\mu(u_j),
\]
where
\[
\mathcal S_3(Y_1,Y_2,Y_3,Y_4)
=\operatorname{Sym}\left[
Y_3^3Y_4^3
-90Y_2Y_3^2Y_4^3
+2700Y_2^3Y_3^3
+360Y_2Y_3Y_4^3
-2700Y_2^2Y_3^2
\right].
\]
Here \(\operatorname{Sym}\) means the sum over all \(24\) permutations, with the same normalization applied to every term.

## 2. Why symmetrisation is not yet positivity

The symmetric polynomial \(\mathcal S_3\) has no generic reason to be nonnegative on \([0,\infty)^4\). Consequently, positivity of \(d\mu\) still does not produce a Gram certificate. The missing input must come from the specific theta measure and its modular reflection.

## 3. Exact Riemann-specific target

The completed kernel satisfies
\[
\Phi(u)=\Phi(-u)>0.
\]
For the four-copy integral, pair variables under the involution \(u_j\mapsto -u_j\) and apply the theta functional equation before attempting any termwise lattice expansion. The proof-bearing target is an identity of the form
\[
\boxed{
Q_3^*=\sum_{\alpha}\int_{\Omega_\alpha}
\left|P_{\alpha}(u_1,u_2,u_3,u_4)\right|^2
\,d\lambda_\alpha
}
\]
where each \(d\lambda_\alpha\) is manifestly positive and the \(P_\alpha\) are explicit finite combinations of theta-lattice terms.

A weaker but still useful target is a decomposition
\[
Q_3^*=A_3+B_3,
\qquad A_3\ge0,
\]
with \(B_3\) an explicitly controlled modular-reflection remainder. The remainder must itself be proved nonnegative or vanish exactly.

## 4. Critical diagnostic

The generic positive-measure counterexample in Frontier 110 shows that the desired sign cannot follow from moment positivity alone. Thus, if an attempted derivation eliminates all explicit theta dependence and reduces to a universal inequality for arbitrary Stieltjes moment sequences, it is necessarily too weak and cannot prove the Riemann-specific cubic gate.

Conversely, an explicit theta-dependent positive remainder would constitute a genuine new structural result and could plausibly be iterated to higher degrees.

## 5. Immediate next computation

Compute the exact symmetrized polynomial \(\mathcal S_3\), factor it over the symmetric-polynomial ring, and determine whether it contains a Vandermonde-square factor
\[
\prod_{i<j}(Y_i-Y_j)^2
\]
or a sum of such factors. If it does not, identify the exact residual symmetric polynomial. That residual is the first object on which the modular theta identity must act.

## 6. Status

This frontier is a concrete algebraic target for the first Riemann-specific multi-copy Gram identity. It does not assert that the required factorisation exists and does not prove RH.
