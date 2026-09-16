# Frontier 38 — identification of the degree-3 Hermite minor with the cubic discriminant

For a monic cubic
\[
p(x)=x^3+b_1x^2+b_2x+b_3,
\]
the leading 3x3 Hermite determinant is exactly the polynomial discriminant:
\[
\boxed{
\det H_3
=-4b_1^3b_3+b_1^2b_2^2+18b_1b_2b_3-4b_2^3-27b_3^2
=\operatorname{Disc}(p).
}
\]

Therefore the degree-3 Jensen case is not merely an arbitrary Hermite constraint: it is exactly the cubic discriminant condition. The central-coordinate form from Frontier 36 gives the equivalent depressed-cubic discriminant structure
\[
\boxed{\operatorname{Disc}(p)=-27(w^2+4v^3)},
\]
where \(v,w\) are the normalized centered combinations of the five consecutive coefficient data used in the general-degree reduction.

For three real roots, the discriminant is nonnegative; hence
\[
\boxed{w^2+4v^3\le0}.
\]

This identifies the next Riemann-specific bottleneck as a discriminant inequality for the degree-3 Jensen polynomial. Any future proof of all-degree Jensen hyperbolicity must, in particular, establish this exact inequality for every shift \(n\).

**Status:** exact identification/reduction; no RH proof.
