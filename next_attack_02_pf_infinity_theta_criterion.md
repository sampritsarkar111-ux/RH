# Next attack 02 — PF∞ / Jensen-polynomial route for the completed Riemann kernel

## Objective
Attempt to turn the theta-lattice problem into a single all-orders criterion whose failure/success is mathematically decisive for RH.

This document is a research target, NOT a claim that RH has been proved.

## 1. Move from individual determinants to Jensen polynomials
Let
\[
\Xi(t)=\sum_{m\ge0}(-1)^m a_m\frac{t^{2m}}{(2m)!}
\]
with the normalization chosen so that RH is equivalent to \(\Xi\) belonging to the Laguerre–Pólya class.

For each n,d define the Jensen polynomial
\[
J_{n,d}(X)=\sum_{k=0}^{d}\binom dk a_{n+k}X^k.
\]
The central all-order target is eventual hyperbolicity of every fixed-degree Jensen family, together with a rigorous passage from eventual hyperbolicity to the required Laguerre–Pólya conclusion.

## 2. Factorial gauge as a Hankel kernel
Define
\[
H_{ij}=(-1)^i\frac{a_{i+j}}{(i+j)!}.
\]
Instead of proving H is positive semidefinite directly, seek a diagonal/sign gauge D and positive measure μ such that
\[
\boxed{(DHD)_{ij}=\int_0^\infty p_i(x)p_j(x)\,d\mu(x)}.
\]
If the p_i form a strictly sign-regular system, all minors acquire a controlled sign by Andreief.

## 3. Unsummed theta kernel — do not collapse first
Write the completed theta representation schematically as
\[
\Xi(t)=\int_0^\infty \mathcal K(u)\cos(tu)\,du,
\]
where \(\mathcal K\) is the exact completed theta-derived kernel.

The required operation order is:
\[
\boxed{\text{theta lattice}\;\xrightarrow{\rm Poisson/Jacobi}\;\text{dual lattice}\;\xrightarrow{\rm coefficient extraction}\;H\;\xrightarrow{\rm determinant}\;\text{minor}.}
\]
Do NOT first replace the lattice by a numerically collapsed theta value.

## 4. Degree-three decisive test
For the 3×3 Hankel minor
\[
\Delta_3=\det[a_{i+j}]_{i,j=0}^{2},
\]
compute the exact unsummed lattice expansion. Seek a decomposition
\[
\boxed{\sigma_3\Delta_3
=\sum_{\lambda}W_\lambda Q_\lambda,\qquad W_\lambda\ge0,\quad Q_\lambda\ge0,}
\]
where \(\sigma_3=-1\) is the factorial signature.

A mixed-sign residual must be retained explicitly. It cannot be discarded as an error term.

## 5. Stronger all-order target
Seek a kernel-level factorization
\[
\boxed{H=U\,W\,U^{\mathsf T},\qquad W\succeq0,}
\]
with U belonging to a strictly sign-regular class. Then
\[
\det H[I,J]
=\sum_{R} \det U[I,R]\det W[R,R]\det U[J,R],
\]
so determinant signs follow from the common sign of the two U-minors.

This is stronger and cleaner than finding separate Vandermonde-square identities at each degree.

## 6. Exact obstruction criterion
The route succeeds only if all four statements are proved:
1. exact theta-to-H factorization;
2. positivity of W, not merely numerical positivity;
3. strict sign-regularity of U at every order;
4. the resulting coefficient property implies the Laguerre–Pólya property of Xi.

If any one fails, record the exact obstruction and do not call the route a proof.

## 7. Computational falsification protocol
For d=1,...,12 and sufficiently many lattice cutoffs N:
- construct the unsummed coefficient kernel symbolically/rationally where possible;
- evaluate every principal minor and selected non-principal minors at high precision;
- compare signs before and after the checkerboard gauge;
- isolate the cutoff-dependent remainder;
- test whether the remainder has a monotone positive limit.

Numerics are diagnostic only; the final argument must replace every limiting numerical observation by an analytic bound or identity.

## 8. Potential decisive bridge
A particularly valuable theorem would be:
\[
\boxed{
\text{positive sign-regular theta representation}
\Longrightarrow
\text{all Jensen polynomials hyperbolic}
\Longrightarrow
\Xi\in\mathcal{LP}
\Longrightarrow RH.
}
\]
The first implication is the main unexplored mathematical wall in this program.

## 9. No overclaim
At present, the factorial determinant identities are exact, but the completed-Riemann-theta PF∞ factorization and the final Laguerre–Pólya implication remain unproved targets. A complete RH proof requires closing those gaps explicitly.
