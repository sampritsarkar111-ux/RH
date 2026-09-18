# RH Frontier 205 — Global-Weil Adversarial Audit and a New Proof Gate

Date: 2026-09-18

## Status

**OPEN — RH is not proved by this frontier.**

## 1. New breakthrough direction: global-sign discipline

A recent literature search surfaced several repository manuscripts that describe purported RH proofs through Weil positivity. Their abstracts illustrate a recurring logical hazard: showing that an individual off-critical zero produces a negative complex evaluation of a chosen transform does **not** by itself show that the complete Weil functional is negative.

For an admissible test function g, the Weil functional has the schematic form

W_xi(g) = sum over all nontrivial zero orbits of the corresponding transform contributions + prime/archimedean terms,

with the precise normalization depending on the chosen formulation.

Therefore the implication

Re(g-hat(gamma - i delta)) < 0
=> W_xi(g) < 0

is invalid unless every complementary contribution is bounded strongly enough.

## 2. Exact logical lemma

### Lemma (single-orbit negativity is insufficient)

Let W(g)=A_O(g)+D_O(g), where A_O is the contribution of one zero orbit and D_O contains every remaining contribution. If A_O(g)<0 but |D_O(g)| is unrestricted, then no contradiction with W(g)>=0 follows.

### Proof

Write D_O(g)=|D_O(g)| e^{i theta} only schematically; in the real Weil functional use its real-valued total contribution. Since D_O can have magnitude greater than -A_O(g), one can have

W(g)=A_O(g)+D_O(g)>=0.

Thus A_O(g)<0 alone is logically insufficient. A contradiction requires

D_O(g)<-A_O(g),

or the stronger absolute estimate

|D_O(g)|<-A_O(g).

QED.

## 3. New decisive gate

For a hypothetical off-critical orbit O(rho), the proof must establish an admissible g_rho satisfying

A_O(g_rho) <= -eta

and

|D_O(g_rho)| <= eta/2

for some eta>0.

Then

W_xi(g_rho) <= -eta/2 < 0,

contradicting Weil positivity.

This is the exact global defect-budget gate.

## 4. Uniform version

For every delta>0 and finite T>0, define

S(delta,T)={rho=sigma+it: |sigma-1/2|>=delta, |t|<=T}.

A complete compact-strip separation theorem would provide eta(delta,T)>0 and admissible witnesses such that every rho in S(delta,T) satisfies

A_O(g_rho) <= -eta(delta,T),

|D_O(g_rho)| <= eta(delta,T)/2.

The remaining unbounded-height problem requires a second theorem controlling |gamma|>T uniformly.

## 5. Important consequence for proposed theta/Gaussian kernels

For a Gaussian-type transform h(z)=z^2 exp(-a z^2), an off-line point z=gamma-i delta can indeed have negative real part because of its oscillatory phase. That establishes a useful **local witness mechanism**, but not a global Weil contradiction.

The missing theorem is not phase detection. It is global domination of all complementary terms.

## 6. New two-scale architecture

Split the hypothetical zero set into

O(rho),
Z_near(T) = other zero orbits with |Im rho'|<=T,
Z_far(T) = zero orbits with |Im rho'|>T.

Seek three estimates:

(1) Local negativity:
A_O(g_rho) <= -eta.

(2) Finite near-field domination:
|W_{Z_near(T)}(g_rho)+A_arch(g_rho)+A_prime(g_rho)| <= eta/4.

(3) Far-tail domination:
|W_{Z_far(T)}(g_rho)| <= eta/4.

Together they imply W_xi(g_rho)<0.

This decomposes the previously vague 'global defect' into three independently checkable theorems.

## 7. New kernel route

Instead of trying to prove positivity of an arbitrary candidate kernel, search for a factorization

W_xi(g)=<g,K g>_H

where K admits an RH-independent decomposition

K=K_local+K_near+K_far,

with K_local carrying the hypothetical off-line orbit signal and K_near,K_far controlled in operator norm.

A successful estimate would have the form

||K_near+K_far|| <= c < spectral separation of K_local.

This converts orbit separation into a concrete operator-norm problem.

## 8. Jensen connection

The exact cubic identity remains

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2

and

F(r,q)<=0 iff

(r-q)^2 <= (r-1)(q-1)[2(r+q-2)+3(r-1)(q-1)]

for r,q>=1.

This is an exact algebraic gate, independently verified symbolically. It does not establish the required inequalities for xi. The next genuine theorem would have to derive such synchronization from an RH-independent kernel/total-positivity mechanism.

## 9. Anti-circularity

No numeral system, encoding, operator, or spectral representation counts as proof-bearing unless it yields a theorem derived from established properties of zeta/xi without assuming RH or an equivalent criterion.

## 10. Research conclusion

The new horizon is a **three-scale global separation theorem**:

local orbit negativity + finite near-field bound + infinite far-tail bound.

This is substantially sharper than the previous single 'defect budget' statement because each term has a distinct analytic job and can be attacked with different tools: interpolation/RKHS for the local witness, explicit zero estimates for the near field, and density/transform decay for the far tail.

The RH proof remains OPEN until these bounds are proved unconditionally for every possible off-critical zero.
