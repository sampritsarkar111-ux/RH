# Frontier 60 — zero-mode-corrected theta measure and the next exact target

## 1. Why the previous modular-measure route must be repaired

The tempting measure
\[
 t^{-3/4}\vartheta(t)\,dt
\]
is not finite on \([1,\infty)\), because \(\vartheta(t)\to1\). Therefore any proof that treats the full theta function as a finite moment measure on this interval is invalid.

The correct object is the nonzero theta tail
\[
\vartheta_*(t):=\vartheta(t)-1
=2\sum_{n\ge1}e^{-\pi n^2t}.
\]
This decays exponentially as \(t\to\infty\).

## 2. Exact zero-mode correction under modular inversion

Jacobi inversion gives
\[
\vartheta(e^{-x})=e^{x/2}\vartheta(e^x).
\]
Hence
\[
\vartheta_*(e^{-x})
=e^{x/2}\vartheta_*(e^x)+e^{x/2}-1.
\]
Define
\[
\rho_+(x):=e^{x/4}\vartheta_*(e^x).
\]
Then the exact identity is
\[
\boxed{
\rho_+(-x)-\rho_+(x)=e^{x/4}-e^{-x/4}=2\sinh(x/4).
}
\]
This identity isolates the entire failure of naive inversion symmetry: it is exactly the zero mode.

If a different normalization of \(\rho_+\) is used, the displayed factor changes accordingly; the invariant content is the explicit elementary zero-mode correction.

## 3. Corrected symmetric object

Define
\[
\boxed{
\rho_0(x):=\rho_+(x)-\sinh(x/4).
}
\]
Then
\[
\boxed{\rho_0(-x)=\rho_0(x).}
\]
Thus the theta tail admits an exactly even completion after subtracting the unique elementary zero-mode defect.

The crucial warning is that \(\rho_0\) is not automatically a positive density. Evenness alone does not imply Stieltjes positivity, total positivity, or Jensen hyperbolicity.

## 4. New exact moment decomposition

For every integer \(m\ge0\), whenever the integral is absolutely convergent,
\[
\int_{\mathbb R}x^{2m}\rho_0(x)\,dx
=2\int_0^\infty x^{2m}\rho_0(x)\,dx.
\]
Putting \(y=x^2\), this becomes
\[
\boxed{
\int_{\mathbb R}x^{2m}\rho_0(x)\,dx
=\int_0^\infty y^{m-1/2}\rho_0(\sqrt y)\,dy.
}
\]
This is an exact positive-measure representation only if the corrected density \(\rho_0(\sqrt y)\) is nonnegative; that sign question is therefore the first genuine gate.

## 5. The next proof target

The RH route through Jensen polynomials requires all relevant Jensen polynomials to be hyperbolic. Existing theory establishes that sufficiently high Jensen degrees/shifts are hyperbolic, but a complete RH proof still requires the finite exceptional region to be controlled and, more fundamentally, an argument establishing hyperbolicity for every degree and shift. See Griffin–Ono–Rolen–Thorner–Tripp for the Jensen-polynomial equivalence and large-shift results.

The next exact target is therefore not merely “prove positivity of theta moments.” It is:
\[
\boxed{
\text{derive an explicit sign-preserving transform of the zero-mode-corrected theta kernel}\
\text{that implies every Hermite minor of every Jensen polynomial is nonnegative.}
}
\]

A successful certificate must be one of the following:

1. an explicit nonnegative kernel identity for each Hermite minor;
2. a finite sum-of-squares identity valid uniformly in degree and shift;
3. a stronger total-positivity/P\u00f3lya-frequency theorem for the corrected theta transform;
4. a direct Laguerre–P\u00f3lya representation of the resulting entire function.

No finite numerical check, asymptotic statement, or assumption of RH counts as the missing step.

## 6. Adversarial gate

Any proposed positivity theorem must first survive the following checks:

- restore the zero mode before applying modular inversion;
- prove all exchanges of sums and integrals by absolute convergence;
- verify boundary terms at both \(0\) and \(\infty\);
- distinguish positivity of a kernel from positivity of its moments;
- test the claimed implication against arbitrary Stieltjes moment sequences, since earlier frontiers showed those conditions alone are insufficient;
- prove uniformity in both Jensen shift \(n\) and degree \(d\).

## Status

**Rigorous correction and new target, not a proof of RH.** The zero-mode defect is explicit. The remaining obstruction is the construction of a genuinely sign-preserving theta-specific certificate strong enough to imply all Jensen/Hermite inequalities.
