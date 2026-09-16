# Frontier 95 — Unsummed theta-lattice operator target

Date: 2026-09-16

## Result carried forward

Frontier 94 proves that the basic modular reflection \(u\mapsto-u\), together with the beta symmetry \(x\mapsto1-x\), preserves
\[
y=x(1-x)u^2
\]
and hence preserves the factorial-corrected degree-two kernel. It therefore cannot itself create a pointwise-positive orbit pairing.

## New target

Do not collapse the theta lattice before applying modularity. Write the xi-kernel as a lattice sum
\[
\Phi(u)=\sum_{m\ge1}\phi_m(u)
\]
and retain the index m through the determinant calculation. For the degree-two correction form
\[
\Delta_{2,n}=\iint W_n(u_1,u_2)\,\Phi(u_1)\Phi(u_2)\,du_1du_2,
\]
expand
\[
\Phi(u_1)\Phi(u_2)=\sum_{m,k\ge1}\phi_m(u_1)\phi_k(u_2).
\]
The decisive question is whether Poisson/modular transformation on the pair \((m,k;u_1,u_2)\) yields a positive semidefinite matrix kernel
\[
\boxed{\mathcal K_n((m,u),(k,v))=\sum_\alpha P_{n,\alpha}(m,k;u,v)^2\,w_\alpha(m,k;u,v)}
\]
with \(w_\alpha\ge0\), or an equivalent Gram representation.

A successful degree-two Gram identity should then be lifted to the full Hermite matrix by replacing the scalar quadratic form with
\[
\boxed{\mathsf H_{d,n}=A_{d,n}^*G_{d,n}A_{d,n},\qquad G_{d,n}\succeq0.}
\]

## Hard requirements

- no use of RH or critical-line zero parametrization;
- exact Poisson/modular identities;
- justified sum/integral interchange;
- positivity of the resulting Gram kernel;
- all n for degree two;
- all d,n for the lifted theorem;
- explicit equality conditions;
- explicit final implication from all Jensen hyperbolicity to RH.

## Failure criterion

If the unsummed theta-lattice Gram kernel is sign-indefinite for a structurally unavoidable reason, record that exact obstruction and abandon the route rather than converting finite numerical evidence into a proof.

## Status

This is a proof-bearing target, not a claimed theorem. Frontier 94 establishes why the simpler collapsed modular orbit is insufficient.
