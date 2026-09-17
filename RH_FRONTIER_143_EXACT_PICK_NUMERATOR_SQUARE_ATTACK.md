# RH Frontier 143 — Exact Theta Pick Numerator and Global Square/Resolvent Closure

Date: 2026-09-17

## Objective
Attack the strongest remaining target directly: derive an all-order theta-generated nonnegative representation for the Pick numerator of

F(z)=H'(z)/H(z),  H(z)=Xi(sqrt(z)).

No zero locations are assumed in the derivation. Numerical checks are diagnostic only.

## 1. Exact theta representation
Write

H(z)=2 int_0^infinity Phi(u) cos(u sqrt(z)) du,

with Phi(u)>0. Put q=sqrt(z)=a+ib, b>0 on the analytic branch.

Differentiation gives

H'(z)=-(1/(2q)) int_0^infinity u Phi(u) sin(qu) du.

Therefore

-Im F(z)=P(z)/|H(z)|^2,

where P is an exact symmetric double integral.

## 2. Exact symmetric kernel
After inserting the two theta integrals and symmetrising in u,v,

P(z)=int_0^infinity int_0^infinity Phi(u)Phi(v)K_{a,b}(u,v)du dv,

with

K_{a,b}(u,v)=[a cos(a(u-v))sinh(b(u+v))-b sin(a(u+v))cosh(b(u-v))]/[4(a^2+b^2)].

Equivalently, with p=u+v and r=u-v,

K_{a,b}=[a cos(ar)sinh(bp)-b sin(ap)cosh(br)]/[4(a^2+b^2)].

This is exact.

## 3. Pointwise-square attack fails
The kernel is not pointwise nonnegative: cos(ar) and sin(ap) oscillate independently. Thus Phi(u)Phi(v)>=0 cannot imply P(z)>=0 term-by-term.

The diagonal restriction is

K_{a,b}(u,u)=[a sinh(2bu)-b sin(2au)]/[4(a^2+b^2)],

which is useful diagnostically but is not itself a positivity proof for the double integral.

## 4. Stronger target: global theta square factorization
The proof-bearing target is an identity

P(z)=sum_j |A_j(z)|^2 + int_S |A(z;s)|^2 dmu(s),

with dmu>=0 and all amplitudes generated from the unsummed theta lattice, or an equivalent modular/Poisson pairing that yields this identity before the n-sum is collapsed.

A successful identity would give -Im F(z)>=0 in the upper half-plane, hence the Pick property. Together with the analytic structure of F this would force every zero of H onto (-infinity,0], and therefore RH.

## 5. Important correction: the naive resolvent realization is too strong
A tempting construction was

H(z)/H(0)=<e,(I+zJ)^(-1)e>, J>=0.

This cannot represent H itself: a nonzero positive Stieltjes resolvent is zero-free and positive for real z>0, whereas H(z)=Xi(sqrt(z)) has known positive-real zeros corresponding to rigorously isolated nontrivial zeros on the critical line. Certified zero-isolation work gives such zeros without assuming RH. See the AMS computation of nontrivial zeros on the critical line. [Source: https://community.ams.org/journals/mcom/2017-86-307/S0025-5718-2017-03198-7/S0025-5718-2017-03198-7.pdf]

This is a permanent no-go for that particular operator ansatz. The operator target must be moved to F=H'/H (or an associated Weyl m-function), not H itself.

## 6. Correct operator target
Seek an RH-independent positive operator J and a theta-defined Weyl function m(z) such that

F(z)=a+m(z),

m(z)=int_0^infinity dnu(t)/(z+t), nu>=0,

or an equivalent Weyl-Titchmarsh/Herglotz representation. The operator and measure must be defined solely from theta data, not from zeta zeros.

## 7. Modular/Poisson route
Insert the unsummed theta expression

Phi(u)=sum_{n>=1}P_n(u)exp(-pi n^2exp(2u))

into P(z), perform the Poisson/Jacobi transformation before summing/collapsing the lattice, and test whether the resulting paired-lattice expression becomes a sum of squares. If phase terms remain sign-indefinite, record the exact residual rather than declaring failure heuristically.

## 8. Relation to current literature
A 2026 preprint proves strict log-concavity (TP2) of the Riemann Xi kernel but explicitly states that the passage from TP2 to TP-infinity/Laguerre-Pólya remains open. [Source: https://doi.org/10.20944/preprints202604.0159.v2]

A separate 2026 preprint claims a log-concavity-to-RH implication, but that claim requires independent checking of the stated Pólya theorem and its hypotheses and is not adopted here as a proof. [Source: https://doi.org/10.5281/zenodo.20465036]

## 9. Exact status
PROVED: theta-to-Pick-numerator identity and closed symmetric kernel K_{a,b}.

PROVED: pointwise kernel positivity is unavailable.

PROVED: the naive positive-resolvent representation of H itself is structurally impossible.

OPEN: global theta square factorization for P(z), or a theta-generated positive Weyl/Stieltjes function for F.

OPEN: unconditional Pick/Stieltjes, all-order tau-Hankel positivity, and RH.

## 10. Next attack
Do not return to finite Hankel determinants. Perform modular/Poisson pairing at the unsummed lattice level and derive the exact paired residual. The decisive outcome is binary:

1. exact sum-of-squares / positive Weyl representation -> Pick wall closes; or
2. exact sign-indefinite residual -> a rigorous no-go theorem for that factorization class and a new mechanism is required.
