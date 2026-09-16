# Riemann Hypothesis — Frontier 07: Correct Pólya–Jensen Normalization and the Degree-2 Moment Inequality

Date: 2026-09-16

## 1. The key normalization correction

The RH-equivalent Jensen sequence is not the raw coefficient sequence of \(\Xi(\sqrt w)\). Pólya's criterion uses \(\gamma(n)\) defined by
\[
(-1+4z^2)\Lambda\!\left(\frac12+z\right)
=\sum_{n=0}^{\infty}\frac{\gamma(n)}{n!}z^{2n},
\qquad
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Because
\[
(-1+4z^2)\Lambda\!\left(\frac12+z\right)=8\xi\!\left(\frac12+z\right),
\]
if
\[
\Xi(t)=\xi\!\left(\frac12+it\right)
=\sum_{n=0}^{\infty}(-1)^n\frac{M_n}{(2n)!}t^{2n},
\]
then
\[
\boxed{\gamma(n)=8\frac{n!}{(2n)!}M_n}.
\]
This is the sequence whose Jensen polynomials characterize RH.

## 2. Exact degree-2 condition

Define
\[
J_{2,n}(X)=\gamma(n)+2\gamma(n+1)X+\gamma(n+2)X^2.
\]
Its discriminant is
\[
\Delta_{2,n}=4\bigl(\gamma(n+1)^2-\gamma(n)\gamma(n+2)\bigr).
\]
Therefore degree-2 hyperbolicity is equivalent to
\[
\boxed{\gamma(n+1)^2\ge\gamma(n)\gamma(n+2)}.
\]
After substitution,
\[
\boxed{
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}
}\qquad(n\ge0).
\]
The algebra is exact:
\[
\frac{n!(n+2)!}{(n+1)!^2}
\frac{(2n+2)!^2}{(2n)!(2n+4)!}
=\frac{2n+1}{2n+3}.
\]

## 3. Numerical verification of the corrected target

Using the previously computed Taylor coefficients of \(\Xi\), the corresponding first values satisfy
\[
\frac{\gamma(n+1)^2}{\gamma(n)\gamma(n+2)}
\approx
1.07484394,\ 1.06274367,\ 1.05430333,\ 1.04805048,\ 1.04321251,\ 1.03934510,
\]
for \(n=0,1,\ldots,5\). These are strictly above 1, hence pass the degree-2 Turán test in this range.

This is a finite numerical check, not an infinite proof.

## 4. Why the previous moment route failed

The earlier target was attached to \(M_n/(2n)!\) rather than to \(n!M_n/(2n)!\). That normalization error changes the Turán inequality. It is therefore unsafe to use the earlier Frontiers 05–06 inequalities as RH-equivalent statements.

The corrected moment inequality is weaker:
\[
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2},
\]
while Cauchy–Schwarz gives the opposite upper bound
\[
M_{n+1}^2\le M_nM_{n+2}.
\]
So the desired statement is a nontrivial two-sided control of the moment ratios.

## 5. Higher-degree obstruction

Even proving the degree-2 inequality for every \(n\) would not prove RH. The exact RH criterion requires
\[
\boxed{
J_{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma(n+j)X^j
\text{ is hyperbolic for every }d,n\ge0.
}
\]
Known theory proves this asymptotically for every fixed degree as the shift tends to infinity, but that does not control the finitely many small shifts uniformly in \(d\). The all-degree/all-shift quantifier is the remaining barrier.

## 6. New research direction

The corrected normalization suggests attacking the sequence
\[
\gamma(n)=8n!\,\frac{M_n}{(2n)!}
\]
as a structured moment sequence rather than attacking the coefficients of \(\Xi(\sqrt w)/\Xi(0)\) directly.

A decisive theorem would be a total-positivity, multiplier-sequence, or integral-kernel result proving all Jensen determinants of this \(\gamma\)-sequence have the signs required for hyperbolicity. Any such theorem must be proved without assuming RH.

A second route is to prove directly that the entire function
\[
G(z):=(-1+4z^2)\Lambda\!\left(\frac12+z\right)=8\xi\!\left(\frac12+z\right)
\]
belongs to the Laguerre–Pólya class.

## 7. Current conclusion

The proof attempt has not reached RH. The important result of this frontier is a correction of the Jensen normalization and an exact reduction of the first Jensen hyperbolicity condition to
\[
M_{n+1}^2\ge\frac{2n+1}{2n+3}M_nM_{n+2}.
\]
The next stage must attack the all-degree determinant/hyperbolicity problem rather than accumulating more low-degree numerical tests.
