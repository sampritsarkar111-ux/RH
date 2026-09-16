# Frontier 98 — Exact next breakthrough task after modular-orbit no-go

Date: 2026-09-16

## Locked conclusion

The collapsed-variable modular orbit is not sufficient. The scale variable y is invariant under the natural reflection, and the degree-two kernel changes sign. The correct route must retain the completed theta lattice until after Poisson/Jacobi transformation.

## Exact calculation to perform next

With
\[
\phi_m(u)=\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad
\Phi(u)=\sum_{m\ge1}\phi_m(u),
\]
expand the factorial-corrected degree-two quantity directly as a double lattice sum:
\[
\Delta_{2,n}=\sum_{m,k\ge1}\mathcal D_{n;m,k},
\]
where each \(\mathcal D_{n;m,k}\) is obtained by inserting \(\phi_m,\phi_k\) into the exact two-copy moment expression.

Then apply the Jacobi/Poisson transformation to the **complete double sum** and seek one of the following exact outcomes:

### Outcome A — Gram breakthrough
\[
\Delta_{2,n}=\sum_{\alpha}\int |P_{n,\alpha}|^2d\lambda_\alpha\ge0
\quad\forall n.
\]

### Outcome B — operator breakthrough
Find a theta-specific positive operator \(\mathcal P_n\) such that
\[
\Delta_{2,n}=\langle f_n,\mathcal P_nf_n\rangle,
\qquad \mathcal P_n\succeq0.
\]

### Outcome C — exact obstruction
Show that the transformed complete-lattice kernel contains an unavoidable negative principal minor, proving that this modular-Gram route cannot close degree two.

## Lift criterion

Only Outcome A or B is eligible for lifting to
\[
\mathsf H_{d,n}=A_{d,n}^*G_{d,n}A_{d,n},\qquad G_{d,n}\succeq0,
\]
for all d,n.

## Integrity rule

No finite numerical verification, asymptotic wedge, generic positive-mixture assertion, or RH-equivalent positivity statement counts as a breakthrough. Every identity must be exact and unconditional.

**Status: active proof-bearing target.**
