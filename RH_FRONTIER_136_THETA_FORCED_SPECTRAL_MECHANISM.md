# RH Frontier 136 — Theta-Forced Spectral Mechanism Audit

Date: 2026-09-17

## Objective
Find an unconditional positivity/spectral mechanism forced by the Riemann theta representation, strong enough to imply all-order Hankel positivity or directly force real transformed zeros.

## Exact target
For

v_rho = -(rho-1/2)^(-2),
 tau_n = sum_rho v_rho^(n+1),
 H_N = (tau_{i+j})_{0<=i,j<=N},

find an RH-independent theta-derived identity implying

Q_N(c)=sum_{i,j=0}^N c_i c_j tau_{i+j} >= 0

for every N and every real c.

An equivalent spectral target is a positive self-adjoint operator T>=0 and vector e such that

tau_n = <e,T^n e>

with the representation derived directly from theta/Xi, not reconstructed from the zero locations.

## Strong candidate mechanism
The theta kernel Phi(u) is positive and rapidly decaying and Xi(t) is its cosine transform. Positivity of Phi alone is insufficient: Fourier transforms of positive kernels can have arbitrary zero geometry. Therefore the missing structure must be a nonlinear/spectral consequence of modular inversion, not merely pointwise kernel positivity.

A sharp candidate is the Stieltjes/Pick mechanism for

H(z)=Xi(sqrt(z))

(or an equivalent normalized square-root transform). If theta could prove, unconditionally,

- H(z) has no zeros on C\(-infinity,0], and
- -H'(z)/H(z) is a Stieltjes function,

then

-H'(z)/H(z)=a + integral_0^infinity dnu(t)/(z+t)

would force all zeros of H to lie on (-infinity,0], hence Re(rho)=1/2.

This is not yet proved. It is an exact proof-bearing target rather than an RH restatement if the Stieltjes representation is derived from theta data without inserting the zeros.

## Necessary rejection tests
1. Full PF-infinity of the original theta translation kernel cannot be used as the mechanism: recent literature records a certified PF_5 failure for the de Bruijn-Newman kernel, and a separate 2026 analysis argues that the original Riemann theta kernel cannot itself be PF-infinity.
2. Generic positive-measure/Hankel arguments are insufficient: positive measures can have Jensen discriminants of either sign.
3. Finite-degree positivity is insufficient for RH.
4. A spectral operator whose matrix elements are defined using the unknown zeros is circular.
5. Any factorization containing gamma_rho = Im(rho) before proving rho is on the critical line is circular.

## Concrete theta-to-spectral program
A. Start from the exact theta representation

Xi(t)=integral_0^infinity Phi(u) cos(tu) du.

B. Derive the transformed logarithmic derivative directly from this integral, before any zero factorization.

C. Seek an exact kernel K(z;u,v) such that

-H'(z)/H(z) = A(z) + double-integral K(z;u,v) Phi(u)Phi(v) du dv,

where K has a positive Stieltjes decomposition for z in C\(-infinity,0].

D. If such a decomposition exists, prove complete monotonicity of the boundary values and the Pick sign condition

Im z > 0 => Im[-H'(z)/H(z)] <= 0.

E. Convert the Pick/Stieltjes property into a positive Jacobi spectral measure. This gives a self-adjoint multiplication/Jacobi operator without assuming RH.

F. Independently compare the resulting moments with tau_n. Equality of moments would then trigger Frontier 135 Cauchy/Hamburger rigidity and force v_rho>0.

## Current conclusion
No unconditional theta-forced spectral mechanism has been established in this frontier. The strongest non-circular candidate is:

Theta modular structure -> Stieltjes/Pick property of the square-root Xi logarithmic derivative -> positive spectral measure -> all-order Hankel PSD -> Cauchy/Hamburger rigidity -> RH.

The decisive unresolved lemma is the theta-derived Pick/Stieltjes inequality. Proving it would be a genuine proof-bearing breakthrough; merely naming it or observing finite positivity is not enough.
