# Frontier 145 — Global Spectral Wall: A Unified Attack on Pick and tau-Hankel

Date: 2026-09-17

## Purpose

The previous frontier showed that pointwise positivity and a positive resolvent for H are dead ends. This frontier isolates a single global spectral object that could, if derived from the completed theta lattice without RH, close both remaining nonlinear walls.

## 1. Pole geometry fixes the analytic target

Let H(z)=Xi(sqrt z) and F=H'/H. Under RH, nontrivial zeros give positive real zeros gamma^2 of H, so F has simple poles at z=gamma^2 with positive residues. Therefore the compatible spectral form is a Cauchy transform with support on [0,infinity), not a standard Stieltjes transform in z:

F(z)=E(z)+integral_0^infinity dnu(t)/(z-t),  nu>=0,

with E accounting for the canonical entire/polynomial contribution. The equivalent negative-axis formulation requires the reflected variable and the corresponding sign normalization.

This is a structural correction, not an assumption of RH.

## 2. Global Pick numerator

The exact theta formula is

P(z)=double integral Phi(u)Phi(v) K_{a,b}(u,v) du dv,

K_{a,b}(u,v)=[a cos(a(u-v))sinh(b(u+v))-b sin(a(u+v))cosh(b(u-v))]/[4(a^2+b^2)].

Since K changes sign, any proof of P>=0 must rearrange the full integral. The natural transformations are:

1. exchange u,v and antisymmetrize;
2. pass to p=u+v and r=u-v;
3. apply the Jacobi involution to the unsummed theta lattice;
4. pair modular images before taking signs;
5. search for a squared amplitude.

The decisive algebraic endpoint is

P(z)=sum_j |A_j(z)|^2 + integral |A(z;s)|^2 dmu(s),

with dmu>=0 and A built solely from theta data.

## 3. A sharper square test

Because Phi is even, use x=u^2 and y=v^2 for moment-level components. Any antisymmetric two-copy contribution that survives modular pairing should be tested for divisibility by (x-y)^2. If

R(x,y)= (x-y)^2 Q(x,y)

and Q has a positive semidefinite Gram expansion, then the two-copy contribution is positive. If R is not divisible by (x-y)^2 after exact symmetrization, the simple Vandermonde mechanism is impossible at that degree.

This gives a symbolic criterion stronger than sampling numerical signs.

## 4. tau-Hankel as a second boundary value of the same spectral object

Write

F(z)=sum_{n>=0} c_n z^n,

tau_n=-c_n/n!.

If the corrected global spectral representation exists and its support is positive, expansion about any point strictly outside the support yields coefficients as signed moments of the same spectral measure. After the correct centering/reflection, the Hankel matrices of the resulting moment sequence are Gram matrices. The missing issue is the nonlinear canonical normalization between these spectral moments and the tau_n used in the project.

Thus the real theorem sought is not merely “theta moments are positive”; it is:

THETA SPECTRAL TRANSFER THEOREM: the logarithmic derivative of the completed theta transform admits a zero-location-free positive spectral representation whose canonical Taylor/cumulant coordinates are totally positive in all orders.

## 5. Four possible closure mechanisms

Mechanism I — Weyl-Titchmarsh: construct a self-adjoint operator directly from the theta kernel and prove F is its Weyl m-function after an explicit Möbius/affine normalization.

Mechanism II — Modular square: transform the unsummed lattice first and pair every oscillatory phase with its modular image, yielding exact square moduli.

Mechanism III — Determinantal transfer: represent every tau-Hankel determinant as a multi-copy theta integral and prove its kernel is a sum of Vandermonde squares.

Mechanism IV — de Branges route: construct an entire E-function from the theta transform for which the Hermite-Biehler inequality is equivalent to the required Pick sign.

These are genuinely different proof mechanisms; failure of one does not validate another.

## 6. Current hard wall

No zero-free theta-defined Weyl operator, modular square identity, all-order nonlinear determinant factorization, or de Branges Hermite-Biehler inequality has yet been derived. Consequently there is still no unconditional RH proof.

The most productive next exact calculation is the first nontrivial modularly paired two-copy kernel after the p,r substitution. Its full symbolic factorization—not numerical positivity—is the gate.

## Conclusion

The project has now eliminated two seductive false routes and corrected the analytic sign/support of the spectral target. The remaining path is a single global theta-to-spectral transfer theorem. Proving that theorem would simultaneously attack the global Pick and all-order tau-Hankel walls; without it, neither wall is closed.