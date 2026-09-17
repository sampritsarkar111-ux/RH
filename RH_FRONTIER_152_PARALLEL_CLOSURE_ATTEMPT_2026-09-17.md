# RH Frontier 152 — Parallel Closure Attempt — 2026-09-17

## Scope
Fresh simultaneous attack on the four user-selected surviving routes:
1. Pick/Weyl
2. tau-Hankel
3. modified de Branges
4. Li/Weil + de Bruijn-Newman

The standard is unconditional mathematics: no RH assumption, no assumed zero locations, and no finite numerical test is treated as a proof.

## Gate A — Pick/Weyl
Let `H(z)=Xi(sqrt(z))` and `F(z)=H'(z)/H(z)`. The correct RH-compatible Herglotz orientation is a positive measure representation for `-F`, with poles on the positive real axis:

`-F(z)=c+integral_[0,infinity] dnu(t)/(t-z)`

(up to the required subtraction terms).

The exact theta identity already established is

`-Im F(z)=P(z)/|H(z)|^2`,

where, for `q=sqrt(z)=a+ib`, `b>0`,

`P(z)=double_integral Phi(u) Phi(v) K_(a,b)(u,v) du dv`,

and

`K_(a,b)(u,v)=[a cos(a(u-v)) sinh(b(u+v))-b sin(a(u+v)) cosh(b(u-v))]/[4(a^2+b^2)]`.

### Closure test
Pointwise positivity is impossible because the kernel changes sign. The required remaining theorem is therefore a global positive quadratic-form/Gram identity for `P`, preferably after unsummed Poisson/Jacobi transformation.

### Result
**OPEN.** No valid global square decomposition or positive Weyl measure was derived in this pass. The naive positive-resolvent representation for `H` remains excluded because a nonzero positive resolvent is zero-free on positive real `z`, while `H` has positive-real zeros corresponding to established critical-line zeros.

## Gate B — tau-Hankel
The theta moments may form positive Hankel matrices, but the tau sequence is a nonlinear logarithmic-cumulant/Bell-polynomial transform. Generic moment-cone positivity does not imply positivity after this transform.

### Closure test
A proof requires an all-order cone-preservation identity, or a theta-specific Gram representation of every tau-Hankel minor. A single exact finite-order counterexample would instead close the transformation class negatively.

### Result
**OPEN.** The required all-order Bell/cumulant cone-preservation theorem was not derived. No RH-independent identity was found that converts raw theta Hankel positivity into all-order tau-Hankel positivity.

## Gate C — Modified total positivity
The fixed translation kernel route is excluded by the prior PF5/Wronskian obstruction. Thus the kernel must be genuinely non-translation-invariant, for example modular/scale-dependent.

### Closure test
For every order, derive the minors directly from the unsummed theta lattice and obtain an exact Vandermonde-square, Binet-Cauchy, or equivalent positive decomposition.

### Result
**OPEN.** No all-order positive non-translation kernel was derived. This route is not counted as solved by finite minors.

## Gate D — Modified de Branges
The needed object is an explicit theta-derived `E_*=A_*-iB_*` satisfying the Hermite-Biehler inequality

`|E_*(z)|^2-|E_*#(z)|^2 > 0` for `Im z>0`,

with the difference reduced to an RH-independent nonnegative theta expression.

### Closure test
Construct the pair explicitly, prove entire-function conditions, prove the upper-half-plane inequality, and establish the exact zero correspondence to `Xi`.

### Result
**OPEN.** No explicit theta-derived Hermite-Biehler pair with the required unconditional inequality was derived. The ordinary one-sided Fourier construction does not supply this automatically.

## Gate E — Li/Weil + de Bruijn-Newman
The target is a zero-location-free positive quadratic form for every admissible test function, obtained directly from theta/modular data, followed by the exact equivalence between that positivity criterion and the required zero-location statement.

### Closure test
Derive

`Q(g)=Q_theta(g)>=0`

without inserting `rho=1/2+i gamma` anywhere in the proof.

### Result
**OPEN.** No such positive factorization was derived in this pass. The explicit-formula identity alone does not provide positivity of the zero contribution without the missing structural theorem.

## Cross-route conclusion
All four routes still reduce to one of two genuinely hard structures:

1. a theta-derived positive spectral/Gram object whose positivity is independent of zero locations; or
2. an exact function-space theorem (Hermite-Biehler / Li-Weil) that forces the same zero geometry.

No route may borrow the desired zero geometry from another route. Consequently, the four gates remain mathematically open and no complete proof of RH has been obtained.

## What would constitute a genuine breakthrough
Any one of the following exact identities would materially close a route:

- `P(z)=sum_j |A_j(z)|^2 + integral |A(z;s)|^2 dmu(s)` with `dmu>=0` and all interchanges justified;
- an all-order theta-specific Bell/cumulant-to-Hankel Gram theorem;
- an explicit theta-derived Hermite-Biehler `E_*` with a proved strict upper-half-plane inequality;
- `Q(g)=Q_theta(g)>=0` for every admissible `g`, with a complete equivalence to RH;
- an exact non-translation theta kernel with all-order total positivity and a rigorous Laguerre-Pólya implication.

## Status
**No complete RH proof. Four selected closure gates remain open.**