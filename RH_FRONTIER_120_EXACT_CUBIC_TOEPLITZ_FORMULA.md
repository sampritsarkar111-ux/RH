# Frontier 120 — Exact Cubic Toeplitz Minor Formula

Date: 2026-09-16

For \(g(z)=\sum_{k\ge0}\gamma_k z^k\), the adjacent order-three Toeplitz minor is exactly
\[
\boxed{
\Delta_{3,k}
= -\gamma_{k-2}\gamma_k\gamma_{k+2}
+\gamma_{k-2}\gamma_{k+1}^2
+\gamma_{k-1}^2\gamma_{k+2}
-2\gamma_{k-1}\gamma_k\gamma_{k+1}
+\gamma_k^3.
}
\]

Substituting \(\gamma_j=M_j/(2j)!\) gives a five-moment expression with the exact factorial weights. This is the first higher Toeplitz obstruction beyond the factorial-corrected degree-two Turán condition.

The next calculation must substitute the unsummed completed-theta lattice moments and seek an exact Poisson/Jacobi/Binet–Cauchy factorization. The desired output is not a numerical sign but an identity proving \(\Delta_{3,k}\ge0\) for every \(k\), followed by its all-order analogue.

No RH proof is claimed by this formula alone.