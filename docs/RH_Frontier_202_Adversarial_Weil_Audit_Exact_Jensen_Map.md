# RH Frontier 202 — Adversarial Weil Audit + Exact Jensen Closure Map

Date: 2026-09-18

## Executive status
RH remains unproved. This frontier performs an adversarial audit of a purported one-test-function Weil contradiction and derives a stronger exact criterion for the cubic Jensen gate.

## 1. Critical audit of the one-test-function argument
A common proposed argument is: choose an admissible transform \hat g that is nonnegative on the real axis; an off-critical zero evaluates \hat g at a complex argument; choose parameters making its real part negative; conclude Weil positivity fails.

This is insufficient. Weil positivity is a statement about the **complete quadratic/linear functional**, not the sign of one isolated complex summand. The other zeros and the arithmetic/archimedean terms must be controlled. Therefore a numerical negative value such as Re[\hat g(γ-iδ)]<0 is not itself a contradiction.

## 2. Exact cubic Jensen theorem
For r,q>=1,
F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2.
Writing x=r-1 and y=q-1 gives
F=(x-y)^2-2xy(x+y)-3x^2y^2.
Hence
F<=0 iff
|x-y|^2 <= xy[2(x+y)+3xy].
This is a necessary-and-sufficient cubic synchronization condition, not merely a necessary condition.

## 3. Consequence near the Turan boundary
If x,y are simultaneously small and comparable, cubic hyperbolicity requires |x-y|=O((xy(x+y))^(1/2)), which is smaller than the generic O(x+y) variation. Thus a proof based only on r_n>=1 cannot close degree three.

## 4. Two closure programs
Jensen closure:
derive an unconditional theorem on the coefficient sequence of xi that implies the synchronization inequality at every n and its higher-degree analogues.

Weil closure:
construct an exact zero-independent positive representation
W_xi(g)=||Tg||^2+R(g), R(g)>=0,
including all prime, Gamma, boundary and limiting terms.

## 5. Formal proof skeleton
Assume rho off the critical line. Use an admissible witness g. Isolate the full symmetry orbit O(rho). Prove W_O(g)<0. Establish a global defect bound
|W_xi(g)-W_O(g)|<-W_O(g).
Then W_xi(g)<0 contradicts Weil positivity.

The defect bound is the decisive unproved theorem.

## 6. Numerical/computational rule
Computer algebra can verify polynomial identities and explore candidate inequalities. It cannot replace the infinite-dimensional positivity theorem, uniform tail bounds, or analytic continuation arguments.

## 7. Literature warning
SciSpace surfaced recent self-described RH-proof manuscripts. Their abstracts contain claims of complete proofs, but claims in a repository or preprint are not equivalent to an independently verified theorem. In particular, a manuscript relying on a single complex evaluation of an admissible transform still faces the global Weil-functional issue above.

## 8. Acceptance criterion
No RH claim is marked PROVED until every implication is unconditional, domains are specified, all interchanges/limits are justified, and no RH-equivalent statement is used as an input.
