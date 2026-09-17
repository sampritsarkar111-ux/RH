# Frontier 173 — Exact Bridges and Operator No-Go Results — 2026-09-17

## 1. Exact common bridge: Stieltjes -> factorial Hankel Gram positivity

Let

F(z)=a+∫_[0,∞) dμ(t)/(z+t),  μ≥0,

on C\(-∞,0]. Fix x0>0 and define

M_n = (-1)^n F^(n)(x0)/n!.

Differentiation under the integral gives

M_n = ∫_[0,∞) (x0+t)^(-(n+1)) dμ(t).

Therefore the Hankel matrix K_N=(M_(i+j))_(0≤i,j≤N) is exactly a Gram matrix:

Σ_(i,j=0)^N c_i c_j M_(i+j)
 = ∫_[0,∞) |Σ_(i=0)^N c_i (x0+t)^(-i)|^2 dν(t) ≥ 0,

where dν(t)=dμ(t)/(x0+t).

Thus a positive Stieltjes representation automatically closes every finite factorial-Hankel PSD test. This is an exact algebraic bridge, not numerical evidence.

Conversely, all-order Hankel positivity alone does NOT yet give the Stieltjes representation. One must additionally prove the Stieltjes moment support/consistency and the global analytic continuation/growth hypotheses. Hence the theta-specific missing step is now precisely isolated.

## 2. Exact Herglotz sign condition

For a Stieltjes function

F(z)=a+∫_[0,∞) dμ(t)/(z+t),

and z=x+iy with y>0,

Im F(z) = -y ∫_[0,∞) dμ(t)/((x+t)^2+y^2) ≤ 0.

Therefore an RH-independent proof of the boundary/interior sign

Im(H'(z)/H(z)) ≤ 0  for Im z>0

would immediately force the required Pick/Stieltjes structure once the normalization and growth conditions are supplied. This turns the Stieltjes route into a concrete sign-inequality problem rather than a vague spectral ansatz.

## 3. Wolfram-verified no-go for a recent weighted first-order operator ansatz

A SciSpace-indexed manuscript proposes a weighted Hilbert-space operator of the form

A = -i d/dt - (i/2)(log w(t))'

on L^2(R,w(t)dt).

Let U:L^2(R,w dt)->L^2(R,dt) be (Uf)(t)=sqrt(w(t)) f(t). Direct symbolic conjugation gives

U A U^(-1) = -i d/dt.

Hence this differential expression is unitarily equivalent to the free momentum operator, provided the stated domain/unitarity hypotheses hold. The free momentum operator has continuous real spectrum; therefore a claimed discrete zeta-determinant identity det(A-z) proportional to ξ(1/2+iz) cannot follow merely from essential self-adjointness. An additional nontrivial spectral mechanism, boundary condition, compactification, or different operator is required.

This is a concrete obstruction to treating such a weighted first-order ansatz as an RH proof by itself.

## 4. Symmetry obstruction rechecked

For f(s)=(s-1/2)^2-1, Wolfram gives

f(1-s)=f(s),
Conjugate[f(Conjugate[s])]=f(s),
zeros s=-1/2, 3/2,
and f(1/2+i t)=-1-t^2.

Thus functional-equation-type symmetry and reality on the critical line do not force zero location. The actual spectral/positivity bridge remains indispensable.

## 5. Literature consequence

Recent SciSpace-indexed manuscripts claim complete RH proofs by Hilbert-Pólya, Herglotz/Weil, NB/BD, and weighted-operator constructions. They are retained as audit targets only. Abstract-level claims are not promoted to established mathematics.

## 6. Parallel route status

- Stieltjes/Pick: exact necessary sign condition and Hankel Gram consequence isolated; theta derivation still missing.
- Tau-Hankel: exact bridge to Stieltjes established; all-order theta-specific positivity still missing.
- Jensen/Hermite: requires uniform all-degree/all-shift hyperbolicity; finite or eventual results do not close RH.
- de Branges: operator construction must include genuine spectral determinant identification, not only self-adjointness.
- Li/Weil: universal positivity of the entire admissible test-function class remains the terminal target.
- de Bruijn-Newman: the missing endpoint inequality remains the barrier.
- Nyman-Beurling/Báez-Duarte: infinite-dimensional closure/coercivity remains the proof-bearing step.

## Acceptance rule

No route is COMPLETE unless it yields an unconditional theorem implying Re(rho)=1/2 for every nontrivial zero rho, without defining the positive/spectral object using the unknown zero locations.