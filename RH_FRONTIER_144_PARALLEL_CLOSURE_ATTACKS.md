# Frontier 144 — Parallel Closure Attacks: Pointwise Positivity, Resolvent, Pick, and tau-Hankel

Date: 2026-09-17

## Executive result

Four closure walls were attacked independently and in parallel. Two important no-go results are now exact: the theta Pick kernel is not pointwise nonnegative, and the proposed positive resolvent for H is impossible even under RH because its pole geometry is wrong. The remaining viable route is therefore a genuinely global theta identity, not scalar positivity.

## 1. Pointwise Pick-kernel positivity: CLOSED AS A NO-GO

Let H(z)=Xi(sqrt(z)), q=sqrt(z)=a+ib with b>0. The exact theta representation gives

- Im(H'(z)/H(z)) = -P(z)/|H(z)|^2,

where

P(z)=double integral Phi(u)Phi(v) K_{a,b}(u,v) du dv,

K_{a,b}(u,v)=[a cos(a(u-v)) sinh(b(u+v)) - b sin(a(u+v)) cosh(b(u-v))]/[4(a^2+b^2)].

The completed theta kernel satisfies Phi(u)>0, but K is not pointwise nonnegative. An explicit counterexample is

a=1, b=1/2, u=1/2, v=2,

for which

K = [cos(3/2)sinh(5/4) -(1/2)sin(5/2)cosh(3/4)]/5 approximately -0.0548201335.

Therefore the implication Phi(u)Phi(v)>=0 => P(z)>=0 is invalid. Any successful proof must exploit global integration, modular pairing, or a square factorization. This independently confirms the obstruction recorded in Frontier 143.

## 2. Naive positive-resolvent for H: CLOSED AS A NO-GO

The ansatz

H(z)/H(0)=<e,(I+zJ)^(-1)e>,   J>=0,

cannot represent H. A positive resolvent is zero-free on real z>0, while H has positive-real zeros corresponding to the rigorously known nontrivial zeros of zeta on the critical line. Thus this operator target fails before any RH implication is attempted.

There is also a sign/orientation correction to the proposed Stieltjes target. A standard Stieltjes transform

S(w)=a+integral_0^infinity dmu(t)/(w+t),  mu>=0,

has singularities on the nonpositive real axis with positive residues. Under the RH parametrization H(z)=product(z-gamma^2) up to the standard entire factors, F=H'/H has poles at positive z=gamma^2 with positive residues. Hence F itself cannot literally be a standard Stieltjes transform in the variable z.

The geometrically compatible Cauchy-transform target is instead

F(z)=A(z)+integral_0^infinity dmu(t)/(z-t),  mu>=0,

or equivalently a Stieltjes-type statement for -F(-w), after the appropriate entire/polynomial normalization is controlled. This correction prevents proving the wrong theorem.

## 3. Global Pick/Stieltjes wall: reduced to the exact global object

The correct RH-bearing inequality is still

Im z>0  =>  Im F(z)<=0,

with F=H'/H, but the representation must have support compatible with the positive-zero geometry. The exact numerator P is already known. The remaining question is whether modular/Poisson transformation of the *unsummed* theta lattice converts P into

P(z)=sum_j |A_j(z)|^2 + integral |A(z;s)|^2 dmu(s),

or into an equivalent positive Weyl-Titchmarsh form.

A local proof is impossible because K changes sign. A proof, if it exists, must be global.

## 4. Theta-generated square factorization: strengthened target

The failed one-copy ansatz

P(z)=integral Q(z,u)^2 Phi(u) du

is too restrictive. The correct candidate is a finite multi-copy modular Gram identity

P(z)=integral_{R^q} |A(z;u_1,...,u_q)|^2 prod_l Phi(u_l) du_l
      + explicit nonnegative boundary terms,

where A is built before collapsing the lattice sum and incorporates the Jacobi involution.

The first nontrivial algebraic test is q=2 or q=4 after antisymmetrization. The decisive signature is a Vandermonde square

prod_{r<s}(u_s-u_r)^2

or, because the completed moment representation is even, the corresponding square in u_s^2. If the modularly transformed antisymmetric part does not reduce to such squares plus nonnegative remainders, that factorization class is ruled out.

No RH assumption is permitted in constructing A or the measure.

## 5. All-order tau-Hankel wall: exact structural obstruction

For the positive theta measure dmu=Phi(u)du, raw even moments satisfy

det(M_{i+j})_{0<=i,j<N}
=1/N! integral prod_r Phi(u_r) prod_{r<s}(u_s^2-u_r^2)^2 d^N u >=0.

This is a genuine all-order Gram/Vandermonde identity.

However, tau_n is obtained from the logarithmic derivative of H, hence from the nonlinear cumulant transform of the H Taylor coefficients. Consequently raw moment Hankel positivity does not transfer automatically to tau-Hankel positivity. The missing map is nonlinear and depends on all lower coefficients.

The actual target is therefore an all-order nonlinear total-positivity identity of the form

c^T T_N(tau)c = integral |B_N(c;u_1,...,u_q)|^2 dmu_q >=0

for every N and every c, with B explicitly theta-generated and without zero locations.

## 6. Parallel attack matrix

A. Pointwise kernel: disproved. Exact sign-changing counterexample.

B. Naive H-resolvent: disproved. Pole/zero geometry gives a rigorous no-go.

C. Global Pick: OPEN. Must use modular pairing or a global square/Weyl representation.

D. All-order tau-Hankel: OPEN. Raw theta Hankel is positive, but the cumulant transform is the unresolved nonlinear wall.

## 7. New strategic pivot

The four walls should no longer be treated as four independent positivity conjectures. The strongest common target is a single theta-generated Weyl function W(z) whose boundary imaginary part has an explicit positive spectral density and whose logarithmic derivative recovers F after a controlled algebraic transformation.

Desired chain:

theta lattice -> modularly paired Weyl kernel -> positive spectral measure -> global Pick property of transformed F -> all-order tau-Hankel positivity -> Laguerre-Pólya/Jensen hyperbolicity -> RH.

The key advantage is that the same spectral measure would close the Pick and tau-Hankel walls simultaneously. The current evidence does not establish this measure or the final identity, so RH remains open in this project.

## Status

GREEN: completed theta-kernel positivity; exact theta-to-H map; exact Pick numerator; raw moment Vandermonde positivity; exact logarithmic/cumulant bridge.

RED: global Pick factorization; theta-generated positive Weyl representation; all-order tau-Hankel positivity; RH.

This frontier intentionally records exact failures rather than treating numerical or finite-degree positivity as proof.