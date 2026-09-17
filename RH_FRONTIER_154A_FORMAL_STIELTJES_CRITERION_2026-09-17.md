# Frontier 154A — Formal Stieltjes Criterion

Let H(z)=Xi(sqrt(z)) and m(z)=-H'(z)/H(z).

A sufficient route to the master gate is:

1. Prove m is holomorphic on C\(-infinity,0] and m(x)>=0 for x>0.
2. Prove complete monotonicity: (-1)^n m^(n)(x)>=0 for all x>0,n>=0.
3. Prove the Stieltjes/Pick analytic condition, e.g. Im m(z)<=0 for Im z>0, together with m(x)=O(1/x) after removal of an explicit entire/affine term.
4. Apply the Stieltjes representation theorem to obtain m(z)=a+integral_0^infinity dmu(t)/(z+t), mu>=0.
5. Independently prove the Hadamard/determinant normalization that excludes an additional zero-bearing entire factor.

Important: complete monotonicity alone is not being asserted here as sufficient for an arbitrary analytic function to be Stieltjes; the Stieltjes analytic/growth condition is an additional required certificate.

The theta representation H(z)=4 integral_0^infinity Phi(u) cosh(u sqrt(z)) du gives an exact starting point, but positivity of Phi does not by itself imply the required sign for the nonlinear logarithmic derivative.

Therefore the actual missing theorem is an all-order Riemann-specific theta Gram/SOS identity for m^(n), or an equivalent positive-resolvent/determinant construction.