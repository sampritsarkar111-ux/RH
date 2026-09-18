# Frontier 183 — SDTNS Local Euler Factor and Transform Obstruction

Date: 2026-09-18

## Status

Partial closure only. This frontier records an exact prime-by-prime factorization of the SDTNS kernel and a proof-bearing test for whether that kernel can represent the Weil explicit-formula quadratic form. It does not claim a proof of the Riemann Hypothesis.

## 1. Exact local factorization

Let

K_t(m,n) = sum_{d|gcd(m,n)} exp(-t (log d)^2) epsilon_m(d) epsilon_n(d),

where epsilon_n(d)=0 if d does not divide n and epsilon_n(d)=(-1)^Omega(n/d) otherwise.

Write

m = product_p p^(a_p),   n = product_p p^(b_p).

Then the kernel factors prime-by-prime:

K_t(m,n)
= product_p K_{t,p}(p^(a_p),p^(b_p)),

with

K_{t,p}(p^a,p^b)
= (-1)^(a+b) sum_{k=0}^{min(a,b)}
    exp(-t (k log p)^2).

This follows by writing every common divisor as d=product_p p^(k_p), separating the Liouville signs, and separating the Gaussian weight over primes.

## 2. Interpretation

The SDTNS kernel is therefore an arithmetic tensor product of finite local prime-power kernels. This exposes considerably more structure than the generic Gram representation.

The exact factorization is a closed algebraic gate, but it is not itself an RH implication.

## 3. Proof-bearing bridge target

A successful RH route would require an explicit map from finite coefficient vectors c to an admissible dense class of Weil test functions f_c such that

sum_{m,n} conjugate(c_m) K_t(m,n) c_n
= C(c) Q_Weil(f_c)

or an explicitly controlled equivalent identity, with all prime, gamma/archimedean, and continuation terms accounted for.

A sufficient form would preserve positivity through a rigorously established positive factor/correction and would then connect to a known RH-equivalent positivity criterion.

## 4. No-go alternative

If the SDTNS transform has a structural local or archimedean signature incompatible with the Weil quadratic form, the correct outcome is a rigorous obstruction theorem. Generic positive-semidefinite kernels cannot be identified with the Weil form without proving the required transform identity.

## 5. Parallel gates

1. Derive the complete Mellin/Dirichlet transform of K_t.
2. Determine its Euler factors in the relevant half-plane.
3. Identify whether an archimedean factor can arise naturally and exactly.
4. Construct, or disprove the existence of, a dense map c -> f_c into the Weil test-function space.
5. Compare the resulting quadratic form term-by-term with the Weil explicit formula.
6. Independently attack the Li/Stieltjes/de Branges criteria; do not assume that a representation or PSD kernel closes these criteria.

## 6. Verification note

A Wolfram symbolic evaluation was attempted for the local kernel. One evaluator call used invalid local-function syntax, so that particular computation is not counted as a verified computational result. The local factorization is retained as an algebraic derivation to be rechecked with corrected symbolic syntax.

## Conclusion

Frontier 183 closes an exact structural kernel gate and sharpens the decisive question to an SDTNS-to-Weil identity or a rigorous no-go theorem. The completed-xi identification, archimedean bridge, spectral realization, and unconditional RH implication remain open.
