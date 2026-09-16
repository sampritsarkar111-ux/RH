# Frontier 97 — Degree-two modular gate: concrete outcome

Date: 2026-09-16

## Exact kernel test

For
\[
c_k=\frac{2k+1}{k!},\qquad
K_n(y_1,y_2)=c_{n+1}^2y_1y_2-\frac{c_nc_{n+2}}2(y_1^2+y_2^2),
\]
set \(r=y_1/y_2\) and
\[
R_n=\frac{c_{n+1}^2}{c_nc_{n+2}}=\frac{(2n+3)^2}{(2n+1)(2n+5)}.
\]
Then
\[
K_n\ge0
\iff
R_n-\sqrt{R_n^2-1}\le r\le R_n+\sqrt{R_n^2-1}.
\]
Outside this interval the kernel is strictly negative.

The interval contracts toward \(r=1\) as \(n\to\infty\). Thus any pointwise square certificate would have to contradict the exact algebraic sign change, independent of the theta measure.

## Modular conclusion

The completed theta kernel is even under the Jacobi modular reflection, but the already-collapsed variable \(y=x(1-x)u^2\) is invariant. Therefore a direct orbit average of the collapsed kernel cannot change its sign.

The correct remaining degree-two problem is the **unsummed complete-theta transform**: apply Poisson/Jacobi inversion to the complete lattice before collapsing to \(y\), then seek a Gram representation. This is now the sole modular route being pursued for degree two.

## Numerical sanity checks (not proof)

The exact positivity intervals are approximately:

- \(n=0\): \([0.303337,3.296663]\)
- \(n=1\): \([0.544540,1.836412]\)
- \(n=2\): \([0.657984,1.519794]\)
- \(n=10\): \([0.883941,1.131297]\)
- \(n=100\): \([0.9861629,1.0140312]\)

These values only illustrate the exact formula; they do not establish any theta-integrated inequality.

## Decision

The natural collapsed modular-orbit pairing is closed as a no-go. The unsummed theta-lattice Gram identity remains open and is the next proof-bearing target.

**Status: exact partial result; no RH proof.**
