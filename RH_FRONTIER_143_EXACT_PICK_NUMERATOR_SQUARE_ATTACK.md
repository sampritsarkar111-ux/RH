# RH Frontier 143 — Exact Theta Pick Numerator and Global Square/Resolvent Closure

Date: 2026-09-17

## Objective
Attack the strongest remaining target directly: derive an all-order theta-generated nonnegative representation for the Pick numerator of F(z)=H'(z)/H(z), H(z)=Xi(sqrt(z)). No zero locations are assumed.

## 1. Exact theta representation
Write H(z)=2 int_0^infinity Phi(u) cos(u sqrt(z)) du. Put q=sqrt(z)=a+ib, b>0.

Differentiation gives H'(z)=-(1/(2q)) int_0^infinity u Phi(u) sin(qu) du.

Therefore -Im F(z)=P(z)/|H(z)|^2, where P is an exact symmetric double integral.

## 2. Correct exact symmetric kernel
Careful recomputation of the conjugation, differentiation factor, and u<->v symmetrisation gives

P(z)=int_0^infinity int_0^infinity Phi(u)Phi(v) K_{a,b}(u,v) du dv,

with

K_{a,b}(u,v)=[a cos(a(u-v)) sinh(b(u+v))-b sin(a(u+v)) cosh(b(u-v))]/[2(a^2+b^2)].

Equivalently, p=u+v and r=u-v give

K_{a,b}=[a cos(ar)sinh(bp)-b sin(ap)cosh(br)]/[2(a^2+b^2)].

This normalization was independently checked symbolically from the unsymmetrised kernel Im(sin(qu)cos(conj(q)v)/q) and then symmetrised.

## 3. Pointwise-square attack fails
K_{a,b} is not pointwise nonnegative because cos(ar) and sin(ap) oscillate independently. Thus Phi(u)Phi(v)>=0 cannot imply P(z)>=0 term-by-term.

The diagonal restriction is K(u,u)=[a sinh(2bu)-b sin(2au)]/[2(a^2+b^2)].

## 4. Stronger target: global theta square factorization
Seek an identity P(z)=sum_j |A_j(z)|^2 + int_S |A(z;s)|^2 dmu(s), with dmu>=0 and amplitudes generated from the unsummed theta lattice, or an equivalent modular/Poisson pairing that yields this identity before the n-sum is collapsed.

A successful identity gives -Im F(z)>=0 in the upper half-plane and hence the Pick property. Together with the analytic structure of F, this would force zeros of H onto (-infinity,0], hence RH.

## 5. No-go for a tempting operator ansatz
The stronger representation H(z)/H(0)=<e,(I+zJ)^(-1)e>, J>=0, cannot represent H itself: a nonzero positive resolvent is positive and zero-free for real z>0, whereas H(z)=Xi(sqrt(z)) has positive-real zeros coming from rigorously isolated nontrivial zeta zeros on the critical line. Thus the operator target must be formulated for F=H'/H or an associated Weyl/Herglotz function, not H itself.

## 6. Correct operator target
Seek an RH-independent positive operator J and theta-defined Weyl function m(z) such that F(z)=a+m(z), m(z)=int_0^infinity dnu(t)/(z+t), nu>=0, or an equivalent Weyl-Titchmarsh/Herglotz representation. The operator/measure must be defined solely from theta data, not from zeta zeros.

## 7. Modular/Poisson route
Insert the unsummed theta expression Phi(u)=sum_{n>=1}P_n(u)exp(-pi n^2 exp(2u)) into P(z), perform Poisson/Jacobi transformation before collapsing the lattice, and test whether the paired-lattice expression becomes a sum of squares. If phase terms remain sign-indefinite, record the exact residual and prove a no-go theorem for that factorization class.

## 8. Status
PROVED: exact theta-to-Pick-numerator identity and corrected symmetric kernel; pointwise positivity is unavailable; the naive positive-resolvent representation of H is structurally impossible.

OPEN: global theta square factorization for P(z), or a theta-generated positive Weyl/Stieltjes function for F; unconditional Pick/Stieltjes; all-order tau-Hankel positivity; RH.

## 9. Next attack
Do not return to finite Hankel determinants. Perform modular/Poisson pairing at the unsummed lattice level and derive the exact paired residual. The decisive outcome is either an exact sum-of-squares/positive Weyl representation or an exact sign-indefinite residual proving a no-go theorem for that factorization class.
