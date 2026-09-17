# RH Frontier 143 — Exact Theta Pick Numerator and Square-Factorization Attack

Date: 2026-09-17

## Objective
Attack the strongest remaining target directly: derive an all-order theta-generated nonnegative representation for the Pick numerator of

F(z)=H'(z)/H(z),  H(z)=Xi(sqrt(z)).

No zero locations are assumed. Numerical checks are diagnostic only.

## 1. Exact theta representation
Write

H(z)=2 int_0^infinity Phi(u) cos(u sqrt(z)) du,

with Phi(u)>0. Put q=sqrt(z), q=a+ib with b>0 and choose the analytic branch.

Differentiation gives

H'(z)=-(1/(2q)) int_0^infinity u Phi(u) sin(qu) du.

Therefore

-Im F(z) = -Im(H'(z) conjugate(H(z)))/|H(z)|^2 = P(z)/|H(z)|^2,

where P is exactly the symmetric double integral below.

## 2. Exact symmetric kernel
After inserting the two theta integrals and symmetrising in u,v,

P(z)=int_0^infinity int_0^infinity Phi(u)Phi(v) K_{a,b}(u,v) du dv,

with

K_{a,b}(u,v)= [ a cos(a(u-v)) sinh(b(u+v)) - b sin(a(u+v)) cosh(b(u-v)) ] / [4(a^2+b^2)].

This is an exact identity, not an approximation.

Equivalently, with p=u+v and r=u-v,

K_{a,b}= [a cos(ar)sinh(bp)-b sin(ap)cosh(br)]/[4(a^2+b^2)].

Hence the desired RH-closing identity is equivalent to proving

P(z)>=0 for every a+ib=sqrt(z) in the relevant upper-half-plane branch.

## 3. Why the obvious square factorization fails
K_{a,b}(u,v) is not pointwise nonnegative. The first term contains cos(ar), and the second contains sin(ap). Thus positivity cannot be obtained by simply using Phi(u)Phi(v)>=0.

This is stronger than the previous sign observation because the exact obstruction is now isolated into the two-variable kernel K_{a,b}.

## 4. New closure target: global theta square after integration
Seek an identity of the form

P(z)=sum_j |A_j(z)|^2 + integral_S |A(z;s)|^2 dmu(s),

with every A_j and A generated from the unsummed theta lattice, and dmu>=0 independent of RH.

A weaker but still sufficient target is an exact positive resolvent

F(z)=c + integral_0^infinity dnu(t)/(z+t),

where nu is constructed solely from Phi/theta data and its positivity is proved without reference to zeros.

## 5. Equivalent operator target
If an RH-independent positive self-adjoint operator J can be constructed from the theta kernel and a cyclic vector e such that

H(z)/H(0)=<e,(I+zJ)^(-1)e>,

then

-F(z)=<e,J(I+zJ)^(-1)e>/<e,(I+zJ)^(-1)e>

and the required Pick/Stieltjes sign follows from the spectral theorem provided the representation has the correct normalization.

The construction must be RH-independent; defining J from the zeros is forbidden because it is circular.

## 6. Exact status
PROVED: the theta-to-Pick-numerator identity and the closed symmetric kernel K_{a,b} above.

PROVED: the problem has been reduced to a concrete global integral/square-factorization statement.

FAILED: pointwise kernel positivity.

OPEN: a global square factorization or positive resolvent generated directly from theta.

OPEN: unconditional Pick/Stieltjes, all-order tau-Hankel positivity, and RH.

## 7. Literature boundary
Recent 2026 work reports strict log-concavity/TP2 for the Xi theta kernel while explicitly leaving the TP2-to-TP-infinity/Laguerre-Pólya passage open. This supports treating the present global square/resolvent identity as the genuinely higher-order wall, not as a consequence of log-concavity alone.

No literature result located here supplies the required unconditional Pick identity.

## 8. Next attack
Do not return to finite Hankel determinants. Attempt modular/Poisson symmetrisation of P(z) before the n-sum is collapsed, looking for cancellation of the cosine/sine phases into squared theta-modular amplitudes. If the modular transform cannot produce a positive measure, derive an explicit signed residual and establish a no-go theorem for that factorization class.
