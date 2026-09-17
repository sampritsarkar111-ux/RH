# Remaining walls closure audit — 2026-09-17

## Executive status

I attempted all remaining proof mechanisms from the five-route program. No unconditional proof of RH was obtained. The correct outcome is a sharper obstruction map, not a fabricated closure.

## 1. Nyman–Beurling / arithmetic approximation

Target:
\[
\inf_{A_N}\frac1{2\pi}\int_{\mathbb R}\left|\frac{1-\zeta(1/2+it)A_N(1/2+it)}{1/2+it}\right|^2dt\to0.
\]

The exact inverse-Mellin residual of a Dirichlet polynomial reduces the problem to arithmetic step functions. Möbius truncation does not by itself supply the required L2 convergence; the literature explicitly records the difficulty of natural approximants and the criterion remains equivalent to RH.

Attempted closure: construct an RH-free universal coefficient family from finite Möbius convolution. Failure point: controlling the global L2 residual is itself equivalent in strength to the missing cyclicity theorem.

## 2. Adjoint arithmetic sampling

Compact-support theorem established in the previous note:
\[
\operatorname{supp}g\Subset\mathbb R,
\quad \widehat g(\log n)=0\ \forall n
\implies g=0.
\]

Attempted extension: truncate an arbitrary kernel element and preserve the sampling zeros. This is invalid: truncation changes every sample. No uniform quasi-analytic estimate has been derived that controls the truncation error while retaining exact arithmetic zeros.

Therefore the full implication
\[
B^*f=0\implies f=0
\]
remains open and is exactly the global cyclicity wall.

## 3. Theta/Jensen all-degree positivity

Degree two reduces exactly to
\[
\frac{\operatorname{Var}_{\nu_n}(u^2)}{\mathbb E_{\nu_n}[u^2]^2}\le\frac{2}{2n+1}.
\]

Attempted closure by ordinary moment inequalities fails because positivity of the measure gives log-convexity in the wrong direction. Attempted closure by positive mixing of Laguerre kernels also fails: a positive mixture of real-rooted polynomials need not be real-rooted.

Thus a genuinely theta-specific total-positivity/variation-diminishing theorem is still required.

## 4. Li positivity

Target:
\[
\lambda_n\ge0\quad(n\ge1).
\]

Attempted closure by Stieltjes representation of
\[
\frac d{dz}\log\xi\left(\frac1{1-z}\right)
\]
requires a positive measure whose moments are exactly the Li coefficients. No RH-independent construction of such a measure has been derived. The route is therefore reduced to the same global positivity problem represented in different coordinates.

## 5. Weil positivity

For compactly supported test functions, the prime contribution is a finite shift operator:
\[
P_L=-2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}S_{\log n}.
\]

Attempted threshold induction using \|S_a\|\le1 fails because triangle bounds lose the arithmetic cancellation needed at large support. Therefore a successful proof requires a nontrivial structured factorization or comparison inequality, not termwise domination.

## Cross-route conclusion

The five routes do not provide five independent remaining miracles. They collapse to three global mechanisms:

1. arithmetic cyclicity / approximation;
2. theta total positivity;
3. explicit-formula global positivity.

No route has been closed unconditionally in this pass. Current mathematical status remains that RH is an open problem. Any purported completion that simply assumes one of the three mechanisms is circular.
