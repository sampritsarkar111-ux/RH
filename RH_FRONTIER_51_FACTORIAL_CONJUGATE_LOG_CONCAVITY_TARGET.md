# Frontier 51 — factorial-conjugate log-concavity: the exact remaining local bridge

## Objective

Frontier 50 proves every theta atom `B_m(pi k^2)` is strictly positive. The next obstruction is not positivity but the interaction between the factorial prefactor and the atom sum.

Write
\[
M_m:=\sum_{k\ge1}B_m(\pi k^2),
\qquad
\gamma_m=Cq_mM_m,
\qquad q_m=\frac{m!}{(2m)!}>0.
\]

The adjacent Turan inequality
\[
\gamma_{m+1}^2\ge\gamma_m\gamma_{m+2}
\]
is exactly equivalent to
\[
\boxed{
\frac{M_{m+1}^2}{M_mM_{m+2}}
\ge
\frac{q_mq_{m+2}}{q_{m+1}^2}
=
\frac{(m+2)(2m+3)}{(m+1)(2m+1)}.
}
\]

Equivalently, since the right side is greater than one,
\[
\boxed{
M_{m+1}^2\ge
\frac{(m+2)(2m+3)}{(m+1)(2m+1)}M_mM_{m+2}.
}
\]
This is a stronger-than-log-concavity condition on the unnormalized theta atom sum.

## 1. Exact factorial correction

Direct calculation gives
\[
\boxed{
\frac{q_{m+1}^2}{q_mq_{m+2}}
=\frac{(m+1)(2m+1)}{(m+2)(2m+3)}.
}
\]
Thus no normalization ambiguity remains: the complete local Turan problem is a single explicit inequality for `M_m`.

## 2. Why positivity of `B_m` is insufficient

Frontier 50 gives `B_m(pi k^2)>0`, but positive sequences can be log-convex rather than log-concave. Numerically, the atom sequences and their sums exhibit this competing tendency before factorial correction. Therefore replacing the signed kernel by a positive-measure argument cannot by itself close Turan positivity.

## 3. Exact double-sum reformulation

Because every atom is now positive, define
\[
p_m(k)=\frac{B_m(\pi k^2)}{M_m}.
\]
Then `p_m` is a probability distribution over `k`. The ratio
\[
\frac{M_{m+1}^2}{M_mM_{m+2}}
\]
can be interpreted as a change-of-measure overlap between the three adjacent atom distributions. A successful proof should exploit this structured coupling rather than pointwise positivity.

## 4. New structural target: cross-order likelihood ratio

A sufficient route would be to prove monotonicity of
\[
\mathcal R_m(k):=
\frac{B_{m+1}(\pi k^2)}{B_m(\pi k^2)}
\]
in `k`, together with a quantitative bound on its spread from `m` to `m+1`. Such a result could convert the double-sum Turan form into a covariance inequality.

A stronger target is the four-point inequality
\[
\boxed{
B_{m+1}(a)B_{m+1}(b)
\ge
\eta_m\bigl(B_m(a)B_{m+2}(b)+B_m(b)B_{m+2}(a)\bigr)
}
\]
for `a,b` in the theta set. This is deliberately stronger than necessary; it must be adversarially tested before being promoted.

## 5. Falsification requirement

The raw Turan kernel was previously shown to take negative values off the diagonal. Therefore the stronger four-point inequality above cannot be assumed. Any proof attempt must search for explicit counterexamples in `(m,a,b)` before using it.

The correct global target remains the summed inequality for `M_m`, not pointwise positivity of the kernel.

## 6. Audit

**Established:** exact factorial-conjugate reformulation of adjacent Turan positivity.

**New research target:** prove the required strengthened inequality for the theta atom sum using cross-order likelihood ratios, total positivity, or a Gram representation.

**Not established:** the target inequality, all-order Jensen hyperbolicity, or RH.
