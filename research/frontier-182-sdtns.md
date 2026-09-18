# Frontier 182 — Signed Divisor-Ternary Numeral System (SDTNS)

Date: 2026-09-18

## Status

Partial closure only. SDTNS supplies an exact signed divisor-digit representation and a positive semidefinite kernel. The decisive bridge from this construction to the completed Riemann xi-function and a self-adjoint spectral theorem remains open. This document does **not** claim a proof of the Riemann Hypothesis.

## 1. Definition

For an integer n >= 1 and positive integer d, define the signed divisor digit

epsilon_n(d) =
  0,                         if d does not divide n,
  (-1)^(Omega(n/d)),         if d divides n,

where Omega(k) counts prime factors of k with multiplicity.

The digit alphabet is {-1, 0, +1}. The nonzero support is exactly the divisor set of n.

Hence the representation is injective in the sense that

n = max { d : epsilon_n(d) != 0 }.

## 2. Exact Mellin divisor polynomial

Define

P_n(s) = sum_{d|n} epsilon_n(d) d^(-s).

Writing n = product_p p^(a_p) gives

P_n(s)
= n^(-s) sum_{q|n} (-1)^(Omega(q)) q^s
= n^(-s) product_{p^(a_p)||n}
    (1 - p^s + p^(2s) - ... + (-1)^(a_p) p^(a_p s)).

This is an exact finite identity.

## 3. Positive SDTNS kernel

For t > 0 define

K_t(m,n)
= sum_{d>=1} exp(-t (log d)^2)
  epsilon_m(d) epsilon_n(d).

Because epsilon_m(d) and epsilon_n(d) vanish unless d divides both m and n,

K_t(m,n)
= sum_{d|gcd(m,n)}
    exp(-t (log d)^2)
    epsilon_m(d) epsilon_n(d).

For any finite complex coefficient vector c,

sum_{m,n} conjugate(c_m) K_t(m,n) c_n
=
sum_{d>=1} exp(-t (log d)^2)
  | sum_{n:d|n} epsilon_n(d)c_n |^2
>= 0.

Thus K_t is positive semidefinite.

## 4. RH-facing proof gate

A genuinely proof-bearing route would require an explicit transform and coefficient/function map for which the SDTNS quadratic form becomes the Weil quadratic form, schematically

M[K_t](u) = C(u) Q_Weil(u),

with C(u) > 0 on a dense admissible Weil test class, together with:

1. a rigorous SDTNS-to-theta/Weil transform;
2. global analytic continuation;
3. compatibility with the zeta functional equation;
4. an exact completed-xi determinant or trace identity;
5. an independently proved self-adjoint spectral realization;
6. universal positivity sufficient for RH.

None of these decisive implications is established here.

## 5. Anti-circularity requirement

The numeral system cannot encode the critical-line conclusion by definition. Any RH proof must derive the critical-line restriction from independently established analytic or spectral identities. In particular, positivity of a generic Gram kernel alone is insufficient to imply RH.

## 6. Computational check

A finite Wolfram verification tested the basic divisor-incidence equivalence over m = 2..40 and d = 1..40 and returned True. This is only a finite consistency check, not a proof of RH.

## Conclusion

SDTNS closes an exact representation layer and provides a positive semidefinite arithmetic kernel. The central unresolved problem is to prove, rather than conjecture, that an appropriate transform of this kernel is exactly the RH-bearing Weil/x i spectral object with all archimedean and continuation terms accounted for.

Riemann Hypothesis remains unproved by this frontier.
