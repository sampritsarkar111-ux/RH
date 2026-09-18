# Finite Verification: Prime-Exponent Fock Layer

This file records exact finite checks for the PENS/Fock construction.

For a cutoff consisting of the first \(P\) primes and occupation numbers \(0\le v_j\le M\), the basis has \((M+1)^P\) states.

The diagonal Hamiltonian is
\[
H_0(\mathbf v)=\sum_{j=1}^P v_j\log p_j.
\]

## Exact identities tested

1. Unique-factorization energy:
\[
\exp(H_0(\mathbf v))=\prod_{j=1}^P p_j^{v_j}.
\]

2. Partition factorization:
\[
\sum_{0\le v_j\le M}e^{-sH_0(\mathbf v)}
=\prod_{j=1}^P\frac{1-p_j^{-(M+1)s}}{1-p_j^{-s}}.
\]
As \(M\to\infty\), this tends to the finite-prime Euler product for \(\Re s>0\) away from its poles.

3. Raising/lowering commutator on basis states:
\[
H_0a_p^+-a_p^+H_0=(\log p)a_p^+.
\]

## Interpretation

These identities establish the arithmetic Fock layer exactly. They do **not** establish RH. The unresolved step is a coupling whose determinant/explicit formula equals the completed \(\xi\)-function with the correct archimedean contribution and whose relevant operator is self-adjoint.
