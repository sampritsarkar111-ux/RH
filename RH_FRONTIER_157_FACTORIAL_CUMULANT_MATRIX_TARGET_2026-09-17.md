# RH Frontier 157 — Factorial-Cumulant Matrix Target — 2026-09-17

## Objective
Attack the first arrow through the exact nonlinear Taylor coefficients of \(m=H'/H\), without using zero locations.

## 1. Coefficient recurrence
If
\[
H(z)=\sum_{n\ge0}h_n z^n/n!,\qquad m(z)=\sum_{n\ge0}c_nz^n/n!,
\]
then \(H'=mH\) gives the exact recurrence
\[
\boxed{h_{n+1}=\sum_{k=0}^n\binom nk c_kh_{n-k}.}
\]
Thus the \(c_n=m^{(n)}(0)\) are uniquely determined by theta moments and form a nonlinear cumulant transform.

## 2. First coefficients
\[
c_0=h_1/h_0,
\quad c_1=(h_0h_2-h_1^2)/h_0^2,
\]
\[
c_2=(h_0^2h_3-3h_0h_1h_2+2h_1^3)/h_0^3.
\]
Higher coefficients should be generated from the recurrence rather than repeatedly differentiating quotients.

## 3. New positive-matrix target
A Stieltjes remainder \(R\) has moment/Hankel matrices
\[
K_N(x)=\left[(-1)^{i+j}R^{(i+j)}(x)/(i+j)!\right]_{i,j=0}^N\succeq0.
\]
Therefore the next proof-bearing construction is to express these matrices directly as theta Gram matrices after subtracting an independently determined entire \(E'\):
\[
K_N(x)=\int V_N(u;x)V_N(u;x)^*\,d\nu_x(u).
\]
The factorization must be exact and all-order.

## 4. Why this is stronger than scalar tests
Scalar complete monotonicity checks only diagonal entries. Hankel positivity simultaneously tests all mixed derivative constraints and is closer to a resolvent/Stieltjes certificate.

## 5. Parallel route
If a theta-defined finite matrix \(J_N\ge0\) can be found whose resolvent quadratic form equals the same \(K_N\), then the scalar Gram identity and the positive-resolvent route merge. The determinant identity remains an independent requirement.

## 6. Status
This is a proof target, not a claimed theorem. The unknown zeros are nowhere used in the construction.