# Frontier 170 — Parallel Closure Execution — 2026-09-17

## Status
**OPEN. No complete proof of the Riemann Hypothesis was obtained.**

This frontier records independent symbolic and numerical audits and closes one invalid proof inference while sharpening the remaining proof-bearing targets.

## 1. Exact obstruction to the symmetry-only spectral argument

Consider

\[
f(s)=\left(s-\frac12\right)^2-1.
\]

Direct symbolic evaluation gives

\[
f(1-s)=f(s),\qquad f(\bar s)=\overline{f(s)},
\]

and on the critical line

\[
f\left(\frac12+it\right)=-1-t^2\in\mathbb R
\qquad(t\in\mathbb R).
\]

But

\[
f(s)=0\iff s=-\frac12\ \text{or}\ s=\frac32.
\]

Hence the following implication is false:

\[
\boxed{f(1-s)=f(s)+\text{Schwarz symmetry}+f(\tfrac12+it)\in\mathbb R\ \Longrightarrow\ \text{all zeros lie on }\Re s=\tfrac12.}
\]

Therefore the statement “reality on the critical line is itself the self-adjoint property” cannot substitute for an actual operator-theoretic construction. A genuine Hilbert space, operator, self-adjointness theorem, spectral identification, and exact determinant/Xi identity are still required.

## 2. Independent verification of the Frontier 169 cubic Hermite certificate

For

\[
J(x)=g_0+3g_1x+3g_2x^2+g_3x^3,
\]

set

\[
a=\frac{3g_2}{g_3},\qquad b=\frac{3g_1}{g_3},\qquad c=\frac{g_0}{g_3},
\]

so that the associated monic cubic is

\[
p(x)=x^3+a x^2+b x+c.
\]

Using Newton sums to form the Hermite matrix, symbolic simplification independently returns zero for the difference between the derived principal minors and the formulas recorded in Frontier 169. Thus the following algebraic expressions are verified:

\[
\Delta_1=3,
\]

\[
\Delta_2=\frac{18(g_2^2-g_1g_3)}{g_3^2},
\]

\[
\Delta_{13}=\frac{18(9g_2^4-12g_1g_2^2g_3+g_1^2g_3^2+2g_0g_2g_3^2)}{g_3^4},
\]

\[
\Delta_{23}=\frac{9(9g_1^2g_2^2-6g_0g_2^3-12g_1^3g_3+10g_0g_1g_2g_3-g_0^2g_3^2)}{g_3^4},
\]

\[
\det\mathcal H=
\frac{27(3g_1^2g_2^2-4g_0g_2^3-4g_1^3g_3+6g_0g_1g_2g_3-g_0^2g_3^2)}{g_3^4}.
\]

This verifies the reduction, not the required Riemann-specific inequalities.

## 3. Independent factorial-Hankel numerical audit

Using the previously recorded coefficients

\[
(c_0,\ldots,c_6)\approx(2.310499311541897\times10^{-2},-3.717259928526969\times10^{-5},2.883478628019466\times10^{-7},-3.978190081517945\times10^{-9},7.712793961479843\times10^{-11},-1.905232141789218\times10^{-12},5.690394521313651\times10^{-14}),
\]

and

\[
K_N=\left[\frac{(-1)^{i+j}c_{i+j}}{(i+j)!}\right]_{i,j=0}^N,
\]

an independent computation reproduces

\[
\det K_1\approx1.9493355548191415\times10^{-9},
\]

\[
\det K_2\approx2.1728105105262686\times10^{-22},
\]

\[
\det K_3\approx1.1775817160119862\times10^{-41}.
\]

The computed eigenvalues of $K_3$ are positive to displayed precision. Numerical conditioning warnings are present, so this remains a diagnostic rather than an exact PSD theorem.

## 4. Remaining parallel proof engines

### A. Stieltjes/Pick
Prove directly from the Riemann theta representation that

\[
\frac{H'(z)}{H(z)}=a+\int_{[0,\infty)}\frac{d\mu(t)}{z+t},\qquad \mu\ge0,
\]

with all analyticity, growth, convergence, and interchange hypotheses proved without assuming RH.

### B. Tau-Hankel
Derive an all-order theta-specific cumulant-to-Gram/SOS identity proving PSD of every required logarithmic-derivative Hankel block.

### C. Jensen/Hermite
Prove the cubic inequalities above for the actual Riemann coefficients, then obtain a uniform arbitrary-degree/all-shift mechanism. Pólya's equivalence requires all degrees and shifts, not merely eventual hyperbolicity.

### D. de Branges / canonical systems
Construct an RH-independent theta-defined Hermite–Biehler function or canonical system and prove the exact Xi determinant correspondence plus self-adjointness and domain conditions.

### E. Li/Weil
Factor the complete explicit-formula quadratic form into an unconditional nonnegative theta/arithmetic SOS for the full admissible test class.

### F. de Bruijn–Newman
Prove the required endpoint property directly from unconditional theta estimates; do not merely restate RH as the endpoint condition.

### G. Nyman–Beurling / Báez–Duarte
Establish the required infinite-dimensional closure/coercivity statement independently of RH.

## 5. Acceptance gate

No finite computation, symmetry argument, repository-indexed claimed proof, or operator analogy closes RH. A valid conclusion requires an unconditional theorem implying every nontrivial zero $\rho$ satisfies

\[
\boxed{\operatorname{Re}\rho=\frac12}
\]

with every analytic continuation, limit, integral, determinant, spectral-domain assertion, and interchange justified, and with no use of the desired zero locations as an assumption.
