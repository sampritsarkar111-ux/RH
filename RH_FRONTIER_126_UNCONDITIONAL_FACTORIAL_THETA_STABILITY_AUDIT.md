# Frontier 126 — Unconditional audit of the all-degree factorial-theta stability theorem

Date: 2026-09-17

## Verdict

The requested **all-degree factorial-theta stability theorem has not been derived**. The current program contains exact factorial-kernel identities and exact finite-degree Jensen gates, but it does not yet contain an unconditional theorem saying that the Riemann-theta moment functional, after factorial normalization, produces a hyperbolic Jensen family for every degree and every shift.

No zero locations and no form of RH are used in this audit.

## 1. Exact factorial transform

For a fixed shift n, define
\[
T_n\!\left[\sum_{j=0}^d a_jX^j\right]
=
\sum_{j=0}^d \lambda_j^{(n)}a_jX^j,
\qquad
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!}.
\]

Using the duplication formula,
\[
\lambda_j^{(n)}
=
\frac{1}{4^j(n+\tfrac12)_j(n+1)_j}.
\]

The Pólya–Schur exponential generating function attached to this diagonal operator is therefore exactly
\[
\boxed{
\Psi_n(z)=\sum_{j\ge0}\frac{\lambda_j^{(n)}}{j!}z^j
={}_0F_2\!\left(;n+\tfrac12,n+1;\frac z4\right).
}
\]

Thus the statement “the factorial transform is a multiplier sequence” is a precise independent subproblem: it requires an unconditional Laguerre–Pólya characterization of this \({}_0F_2\) family, not an RH assumption.

## 2. Why that subproblem is not yet the Riemann theorem

Even if \(T_n\) were proved to preserve hyperbolicity on every polynomial degree, this only gives
\[
p\text{ hyperbolic}
\Longrightarrow
T_n[p]\text{ hyperbolic}.
\]

Our Riemann coefficients instead have the form
\[
\gamma_{n+j}
=
\frac{M_{n+j}}{(2n+2j)!},
\]
where \(M_k\) are theta moments. The missing implication is that the relevant theta-moment polynomial or its infinite-degree stability object lies in the domain on which the factorial operator can be applied to obtain the required Jensen hyperbolicity.

Ordinary positivity of the moment functional does not provide that input: earlier exact calculations already produced positive moment measures whose associated raw-moment cubic is not hyperbolic.

Therefore
\[
\boxed{
\text{factorial multiplier property}\ \not\Rightarrow\ \text{Riemann Jensen hyperbolicity}
}
\]
without an additional theta-specific stability theorem.

## 3. Exact degree-3 Riemann gate remains

With
\[
R_{n,j}=\frac{\gamma_{n+j}/\gamma_n}
{(\gamma_{n+1}/\gamma_n)^j},
\]
the normalized cubic is
\[
1+3X+3R_{n,2}X^2+R_{n,3}X^3.
\]
Its exact hyperbolicity region is
\[
\boxed{
R_{n,2}\le1,
\qquad
\left|R_{n,3}-(3R_{n,2}-2)\right|
\le2(1-R_{n,2})^{3/2}.
}
\]
This is an unconditional algebraic criterion, but proving that the Riemann theta coefficients satisfy it for all n is still a separate theorem.

## 4. Degree-uniform target

The actual missing theorem can now be stated without any reference to zeros:

> **Factorial-theta stability theorem (target).** For every \(n,d\ge0\), the coefficient vector
> \[
> \left(\frac{M_n}{(2n)!},\frac{M_{n+1}}{(2n+2)!},\ldots,\frac{M_{n+d}}{(2n+2d)!}\right)
> \]
> generates a degree-d Jensen polynomial that is hyperbolic; equivalently, the associated normalized shape vector lies in the full hyperbolicity region \(\mathscr R_d\).

A proof must use only unconditional properties of the theta kernel, its Poisson/Jacobi identities, and rigorous positivity/stability-preserving operators. It cannot invoke a representation of the theta kernel in terms of zeros \(\rho\), nor assume \(\Re\rho=1/2\).

## 5. What has actually been ruled out

The following proposed shortcuts are not sufficient:

1. raw Stieltjes moment positivity;
2. a single Vandermonde-square factor in the collapsed triple integral;
3. ordinary total positivity of the raw factorial Hankel kernel;
4. positivity of individual theta moments;
5. a zero-tail argument that writes zero parameters in a form already requiring RH.

The repository's previous frontiers contain exact obstructions for these routes.

## 6. Remaining proof-bearing mechanisms

There are only two clean unconditional routes left in this branch of the program:

### A. Theta-specific stability preserver

Construct an operator \(\mathcal S_n\), directly from the unsummed theta lattice and Poisson/Jacobi transformation, such that
\[
\mathcal S_n[\text{admissible stable input}]
\]
is stable and its Taylor coefficients are exactly the factorially normalized theta coefficients.

The symbol of \(\mathcal S_n\) must be checked directly for stability; a positive linear combination argument is not enough.

### B. All-order Gram/Hermite-matrix factorization

Construct, for every d, an exact identity of the form
\[
H_{n,d}=A_{n,d}^*G_{n,d}A_{n,d}+R_{n,d},
\qquad
G_{n,d}\succeq0,\quad R_{n,d}\succeq0,
\]
where the principal minors of \(H_{n,d}\) are precisely the Hermite/Jensen hyperbolicity certificates. The identity must be derived before any zero parametrization is introduced.

## 7. Status

**Derived:** exact factorial normalization; exact degree-3 gate; exact degree-4 discriminant; exact sign-regularity of the discrete factorial kernel; exact unsummed low-degree obstruction calculations.

**Not derived:** the all-degree theta-specific stability-preserving theorem.

**Conclusion:** this frontier does not prove RH. It does, however, reduce the requested zero-location-free route to a sharply specified theorem whose hypotheses and failure modes are now explicit.
