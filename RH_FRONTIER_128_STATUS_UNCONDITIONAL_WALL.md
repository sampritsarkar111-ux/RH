# Frontier 128 — Exact status of the zero-free all-degree factorial-theta route

Date: 2026-09-17

## Final status of this branch

The all-degree factorial-theta stability theorem is **not yet proved**. The audit was performed without using RH or any zero-location hypothesis.

The program now has a clean separation:

1. **Factorial operator:** exact diagonal multiplier
\[
\lambda_j^{(n)}=\frac{(2n)!}{(2n+2j)!},
\]
with exact hypergeometric symbol
\[
{}_0F_2(;n+\tfrac12,n+1;z/4).
\]

2. **Theta coefficients:**
\[
\gamma_k=\frac{M_k}{(2k)!}.
\]

3. **Finite-degree gates:** exact algebraic regions can be derived degree by degree.

4. **Missing bridge:** an unconditional theta-specific stability theorem connecting the unsummed theta lattice to all Jensen polynomials after factorial normalization.

## What cannot be claimed

It is not valid to say that the factorial transform itself has solved the Riemann problem. Even a full multiplier-sequence theorem for the diagonal factorial operator would only preserve hyperbolicity of an already-hyperbolic input.

Likewise, positivity of the theta moment measure, sign-regularity of the factorial Hankel kernel, or positive Cauchy–Binet weights alone do not supply the missing input stability.

## Proof criterion

A future claim may be promoted to a genuine RH proof only if it supplies all of the following without zeros:

\[
\boxed{
\text{unsummed theta identity}
\;+
\text{stability-preserving operator theorem}
\;+
\text{all-degree closure}
\;+
\text{zero-free implication to RH}.
}
\]

Any omitted arrow remains a proof gap.

## Research direction

The highest-value next calculation is to construct the exact bivariate stability symbol of the unsummed theta/factorial operator and test whether it is stable for arbitrary complex variables. If it fails, the first explicit non-stable specialization should be retained as the obstruction rather than hidden by numerical positivity.
