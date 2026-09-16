# Frontier 62 — global certificate status

## Current state

The program has reached a clean mathematical bottleneck:

\[
\boxed{\text{Find a theta-specific real-zero-preserving certificate for }\Xi.}
\]

The Jensen-polynomial route is rigorously relevant because Pólya's criterion identifies RH with hyperbolicity of the Jensen polynomials, while known work proves hyperbolicity for sufficiently large shifts but does not supply the missing all-shift/all-degree theorem. See Griffin–Ono–Rolen–Thorner–Tripp, *Jensen Polynomials for the Riemann Xi Function*.

## Candidate global mechanism

The Fourier representation of \(\Xi\) through an even theta-derived kernel suggests studying the operator class of transforms that preserve real-rootedness. A useful research split is:

### Gate A — kernel positivity
Prove a genuinely global positivity property of the exact theta-derived kernel, not merely positivity of its ordinary moments.

### Gate B — total positivity / PF∞
Prove that the associated convolution or Fourier-transform kernel is Pólya-frequency of infinite order, or establish an equivalent variation-diminishing property.

### Gate C — entire-function closure
Use a precise theorem showing that the resulting transform belongs to the real Laguerre–Pólya class.

### Gate D — identify the exact xi transform
Verify normalization, convergence, and equality with \(\Xi\), including all zero-mode terms.

## Important negative result

The generic Stieltjes route is not enough: the project's exact third Hermite obstruction contains a contribution with the opposite sign to the ordinary Hankel determinant. Therefore “the coefficients are moments of a positive measure” cannot simply be promoted to RH.

## Current conclusion

No complete RH proof has been obtained. The work has, however, reduced the active search to a sharper structural problem: establish a theta-specific PF∞/variation-diminishing theorem or an equivalent global Laguerre–Pólya certificate. Any claimed completion must explicitly prove this missing theorem rather than infer it from numerical evidence, asymptotics, or finitely many Jensen polynomials.
