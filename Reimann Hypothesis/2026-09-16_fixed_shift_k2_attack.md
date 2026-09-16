# 2026-09-16 — Fixed-shift `k=2` attack and obstruction map

## 1. Exact fixed-shift duality

Let

`E(z)=sum_{n>=0} e_n z^n`, `e_0=1`,

and define

`1/E(-z)=sum_{n>=0} h_n z^n`.

For the consecutive Toeplitz minors

`D_{r,k}=det(e_{k+j-i})_{i,j=0}^{r-1}`

Jacobi–Trudi gives the exact identity

`D_{r,k}=det(h_{r+j-i})_{i,j=0}^{k-1}`.

Thus the first nontrivial fixed-shift case is

`D_{r,2}=h_r^2-h_{r-1}h_{r+1}`.

Therefore proving

`h_r^2 > h_{r-1}h_{r+1}` for every `r>=1`

would prove the entire `k=2` line of consecutive-minor positivity.

This is not a proof of RH: it controls only one fixed shift.

## 2. Why the target is structurally natural

If `E(z)` were known to have only negative real zeros, then `H(z)=1/E(-z)` would be an Edrei/Pólya-frequency generating function. The quantities `h_n` would then have the required total-positivity properties, including the displayed `2 x 2` determinant.

Using this implication directly would be circular for RH, because the negative-real-zero hypothesis is essentially the desired conclusion.

The research problem is therefore:

> Derive the `h_r^2-h_{r-1}h_{r+1}>0` inequality directly from the Riemann-xi coefficient/kernel representation, without assuming zero locations.

## 3. New literature constraints checked

- Kessler (Aug. 2026) reports a proof of the complete `k=1` line `D_{r,1}>0` for all `r`, using a verified low-zero core plus a controlled high-zero tail. This does not cover `k>=2`.
- Dimitrov–Lucas proved the first higher-order Turán inequalities for the Riemann xi coefficients, equivalently hyperbolicity of degree-3 generalized Jensen polynomials. This is finite-order information and does not imply `PF_infinity`.
- Wang–Yang (2024) obtain asymptotic Laguerre inequalities of arbitrary fixed order for the Riemann Xi coefficients; again this is an asymptotic/fixed-order result, not an all-order closure.
- Michalowski (2026) proves `D_{r,k}>0` uniformly for `k >= 10^18 r^3`, leaving the complementary region open.

## 4. Local ratio criterion is too weak

For a positive `r x r` matrix, Katkova–Vishnyakova give a sufficient adjacent-ratio condition of the form

`a_{n}^2 > 4 cos^2(pi/(r+1)) a_{n-1} a_{n+1}`.

For the xi coefficients, the unconditional Turán inequality only gives

`a_n^2 > ((n+1)/n) a_{n-1}a_{n+1}`.

Since `4 cos^2(pi/(r+1)) -> 4`, whereas `(n+1)/n -> 1`, this criterion can certify only the very small-order regime and cannot close RH. This is a genuine obstruction to a naive diagonal-dominance/local-ratio proof.

## 5. Current exact closure target

The next concrete analytic target is therefore not merely `D_{r,k}>0`, but a direct inequality for the reciprocal coefficients:

`h_r^2-h_{r-1}h_{r+1} > 0`,

followed by higher fixed-shift inequalities

`det(h_{r+j-i})_{i,j=0}^{k-1}>0`.

Any successful argument must remain independent of a global factorization of the xi function into critical-line zeros.

## 6. Status

This file records a rigorous reduction and an obstruction map. No RH proof is claimed here.
