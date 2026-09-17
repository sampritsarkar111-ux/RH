# Frontier 175 — Candidate Identity and Failure Tests

## Candidate target

For H(x)=Xi(1/2+x), seek a zero-independent representation
\[
(-1)^n m^{(n)}(x)=\int_0^\infty t^n e^{-xt}\,d\sigma(t),\qquad m=-H'/H,
\]
with a single positive measure \(d\sigma\ge0\), valid for all n≥0 and x>0.

If found, this proves complete monotonicity. To obtain a Stieltjes function, additionally establish the Stieltjes transform structure or equivalent Pick property.

## Structural warning

A representation for H itself as a positive theta/Laplace transform is insufficient. The logarithmic derivative is nonlinear:
\[
-H'/H=-\frac{(\text{positive transform})'}{\text{positive transform}}.
\]
The ratio can destroy total positivity and moment positivity.

## Required symbolic tests

1. Expand H and m at x=1 to high order.
2. Check exact signs of \((-1)^n m^{(n)}(1)\) for n=0,...,N.
3. Form the factorial Hankel matrices and test principal minors.
4. Test the candidate Pick sign at generic upper-half-plane points.
5. Search for a direct positive kernel factorization rather than fitting a measure numerically.

## Hard failure criterion

Any finite-order positivity pattern is not a theorem. If a sign or determinant eventually fails, the candidate route is eliminated; if all tested orders pass, the result remains only a conjectural certificate until an analytic proof is supplied.

## Cross-route leverage

A genuine positive measure identity would immediately provide Gram matrices and can potentially feed the tau-Hankel and Jensen/Hermite routes. A genuine Pick identity can potentially feed de Branges and spectral constructions. The reverse implication is not automatic.