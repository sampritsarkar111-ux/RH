# RH Frontier 152 — Next Proof-Bearing Identities — 2026-09-17

## Pick/Weyl
Attempt to rewrite the exact theta numerator as a positive quadratic form after modular transformation:

`P(z)=<T_z Phi,T_z Phi>_+` or `P(z)=sum_j |A_j(z)|^2 + integral |A(z,s)|^2 dmu(s)`.

The transformation must be performed before collapsing the theta lattice and must preserve the exact analytic domain. If an unavoidable signed residual survives, isolate it exactly.

## tau-Hankel
Let `M_k` denote the theta moments and let `K_n` denote the exact Bell-polynomial cumulants defining tau. Seek an identity of the form

`det(K_{i+j})_{i,j=0}^n = integral_{D_n} |Delta_n(x)|^2 W_n(x) dx`

with `W_n>=0` derived directly from theta/modular structure. This bypasses the false generic claim that arbitrary moment-to-cumulant maps preserve positivity.

## de Branges
Do not assume a pre-existing `E`. Construct

`E_*(z)=A_*(z)-i B_*(z)`

from a theta-modular pair, then target the exact identity

`|E_*(z)|^2-|E_*#(z)|^2 = R_theta(z)`

with `R_theta(z)>0` for `Im z>0`. Separately prove that the symmetrized object reproduces the completed zeta function.

## Li/Weil + de Bruijn-Newman
Seek a direct theta representation

`Q(g)= integral |L_theta g(x)|^2 w_theta(x) dx + R(g)`

with both terms nonnegative for every admissible test function. Only after this is established should the Weil/Li equivalence to the zero-location condition be invoked.

## Cross-route diagnostic
If the same positive theta operator appears in two routes, treat it as a structural cross-check, not as permission to transfer conclusions. Each route must retain an independent proof of its final zero-location implication.