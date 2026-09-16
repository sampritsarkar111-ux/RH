# Frontier 26 — Gram-Factorization Target

Frontier 25 converts Jensen hyperbolicity into Hermite-matrix PSD. The next step is to seek a *structural* proof of PSD rather than checking determinants separately.

For a monic Jensen polynomial \(p_{d,n}\),
\[
\mathcal H_{d,n}=\bigl[s_{i+j}(p_{d,n})\bigr]_{0\le i,j<d}.
\]

A sufficient universal theorem would be an explicit factorization
\[
\boxed{\mathcal H_{d,n}=\int_\Omega V_{d,n}(t)V_{d,n}(t)^T\,d\mu_{d,n}(t)}
\]
with \(\mu_{d,n}\) a nonnegative measure. This immediately gives \(\mathcal H_{d,n}\succeq0\).

The decisive difficulty is that the measure/factorization must be derived from the exact Riemann \(\Xi\)/theta representation, not postulated from RH or from generic positivity. A positive moment representation by itself is insufficient for the Jensen inequalities required here.

## Algebraic bridge

If \(p(x)=\prod_{r=1}^d(x-\rho_r)\), then
\[
s_k=\sum_r\rho_r^k,
\qquad
u^T\mathcal H(p)\nu=\sum_r\left(\sum_{j=0}^{d-1}\nu_j\rho_r^j\right)^2.
\]
Thus, once all \(\rho_r\in\mathbb R\), \(\mathcal H(p)\succeq0\) is immediate. The hard direction is to derive this PSD property directly from the coefficients without already knowing the roots are real.

## New theorem target

Find kernels \(K_{d,n}(t,u)\) generated directly from the theta representation such that
\[
\mathcal H_{d,n}=\iint W_{d,n}(t,u)W_{d,n}(t,u)^T\,d\mu(t)d\mu(u)
\]
or an equivalent totally-positive determinant identity. Any proof must explicitly establish:

1. the exact theta-to-coefficient transformation;
2. nonnegativity of the measure/kernel used;
3. convergence/interchange of all integrals and sums;
4. equality with every Hermite entry;
5. no assumption equivalent to RH.

A successful factorization would prove every Jensen polynomial is real-rooted and therefore, through the classical Jensen criterion, would close the RH route. Until such a factorization is actually proved, this file is a research target, not a proof.
