# Frontier 84 — Exact audit of the common proper-position route

Date: 2026-09-16

## Objective

Frontier 83 left a candidate rescue of the FEATAM integration step: prove that the family
\[
H_u(X,Y)=Y^D K_D(u^2X/Y)
\]
forms a common proper-position cone, so that positive integration in \(u\) preserves stability.

This frontier tests that candidate directly rather than assuming it.

## 1. Root scaling is exact

Write the positive-root form of the hyperbolic inner polynomial as
\[
K_D(t)=c_D\prod_{j=1}^D(t+\sigma_j),
\qquad
\sigma_1>\sigma_2>\cdots>\sigma_D>0.
\]
Then
\[
H_u(X,Y)=c_Du^{2D}\prod_{j=1}^D\left(X+\frac{\sigma_j}{u^2}Y\right).
\]
Thus the projective root locations are exactly
\[
-\sigma_j/u^2.
\]
Changing \(u\) multiplies the entire root configuration by one positive scale factor.

## 2. Two-scale interlacing is not automatic

Take two parameters \(u,v\), and put
\[
\lambda=u^2/v^2>0.
\]
After multiplying all roots of one polynomial by a common positive factor, the two root sets are
\[
\{\sigma_1,\ldots,\sigma_D\},
\qquad
\{\lambda\sigma_1,\ldots,\lambda\sigma_D\}.
\]
For \(D\ge2\), two arbitrary positive dilates of a non-geometric root set do **not** interlace for every \(\lambda>0\).

For example, with \(D=2\), interlacing would require the two ordered sets
\[
\sigma_1>\sigma_2>0,
\qquad
\lambda\sigma_1>\lambda\sigma_2>0
\]
to alternate. If \(\lambda>\sigma_1/\sigma_2\), then
\[
\lambda\sigma_1>\lambda\sigma_2>\sigma_1>\sigma_2,
\]
so the roots occur in two blocks rather than alternating. If \(0<\lambda<\sigma_2/\sigma_1\), the reverse blocking occurs.

Hence no global all-pair proper-position relation can follow merely from the common scaling form.

## 3. Consequence

The missing stability step cannot be repaired by the statement
\[
H_u\text{ stable for every }u
\quad+\quad
H_u\text{ obtained by positive scaling}
\quad\Longrightarrow\quad
\int H_u\,d\mu(u)\text{ stable}.
\]
The scaling family leaves every compact root configuration only to approach arbitrarily separated configurations as \(u/v\to0\) or \(\infty\). Therefore any proper-position theorem applicable to all \(u,v>0\) is impossible for degree \(D\ge2\).

This is an exact obstruction, not a numerical objection.

## 4. What remains viable

The integral must exploit additional structure beyond pairwise proper position. The surviving proof-bearing possibilities are:

1. **Kernel total positivity / variation diminution:** prove directly that the \(u\)-kernel acting on the coefficient vector is a stability-preserving transform.
2. **Operator factorization:** represent the integral as a composition of individually certified real-root-preserving operators, with domains and limits proved.
3. **Direct Hermite certificate:** prove every Hermite principal minor of the integrated Jensen polynomial is nonnegative by a theta-specific identity.
4. **Toeplitz/PF∞ route:** prove all consecutive Toeplitz minors for the Xi coefficients without assuming the zero locations.
5. **Heat-flow route:** establish a global de Bruijn–Newman inequality independently of RH.

The first option is now the most direct continuation of the FEATAM idea, but it requires a genuine total-positivity theorem rather than a proper-position argument.

## 5. New exact target

Let
\[
\mathcal T_D[p](X)=\int_0^\infty \Phi(u)\,Y^D p(u^2X/Y)\,du.
\]
The proof-bearing target is to characterize the matrix kernel of \(\mathcal T_D\) on coefficient vectors and prove that every finite truncation is a stability-preserving operator. Equivalently, for every \(D\), establish a direct criterion implying
\[
K_D\text{ hyperbolic}\quad\Longrightarrow\quad \mathcal T_D[K_D]\text{ hyperbolic}
\]
for the specific theta weight \(\Phi\).

Any such criterion must be proved from the theta/Mellin structure and cannot assume RH, PF∞ of the Xi sequence, or the desired zero location.

## Status

Frontier 84 closes the global common-proper-position subroute. It does **not** prove RH. It sharpens the remaining FEATAM gap to a theta-specific stability-preserving operator theorem.
