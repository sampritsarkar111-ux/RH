# Frontier 64 — exact cubic gate and wedge strategy

## Purpose

Frontier 63 replaced the overly broad PF∞ target by a uniform Jensen certificate. The next concrete attack is to make the first nontrivial finite-degree gate completely explicit and then ask whether its theta structure reveals a propagation law.

## Cubic Jensen gate: exact orientation audit

For the degree-3 Jensen polynomial at shift `n`, write
\[
J^{3,n}(x)=q_n+3q_{n+1}x+3q_{n+2}x^2+q_{n+3}x^3,
\]
where `q_m` denotes the relevant Jensen/Taylor coefficient sequence. Assuming `q_{n+3}\ne0`, divide by `q_{n+3}` to obtain the monic cubic
\[
p(x)=x^3+a x^2+b x+c,
\quad
 a=3\frac{q_{n+2}}{q_{n+3}},\;
 b=3\frac{q_{n+1}}{q_{n+3}},\;
 c=\frac{q_n}{q_{n+3}}.
\]
Its discriminant is
\[
\boxed{\Delta_3(p)=a^2b^2-4b^3-4a^3c+18abc-27c^2.}
\]
Direct substitution gives
\[
\boxed{
\Delta_3(J^{3,n})
= -\frac{27}{q_{n+3}^4}
\Big(q_n^2q_{n+3}^2-6q_nq_{n+1}q_{n+2}q_{n+3}
+4q_nq_{n+2}^3+4q_{n+1}^3q_{n+3}-3q_{n+1}^2q_{n+2}^2\Big).
}
\]

Now define normalized ratios
\[
r_j(n)=\frac{q_{n+j}}{q_n},\qquad
v=r_2-r_1^2,
\qquad
w=r_3-3r_1r_2+2r_1^3.
\]
The exact factorial-weighted cubic quantity from the central-moment reduction is
\[
\widetilde Q_3(n)=-3\big(w^2+4v^3\big).
\]
Expanding `w^2+4v^3` shows that the bracket above equals
\[
q_n^2\big(w^2+4v^3\big).
\]
Therefore the orientation is not ambiguous:
\[
\boxed{
\Delta_3(J^{3,n})
=\frac{9q_n^2}{q_{n+3}^4}\,\widetilde Q_3(n).
}
\]
Thus, whenever the displayed ratios are defined, the sign of the cubic discriminant is exactly the sign of `\widetilde Q_3`.

For a real cubic, `\Delta_3>0` means three distinct real roots, `\Delta_3=0` means a repeated-root degeneration, and `\Delta_3<0` means one real root together with a nonreal conjugate pair. Hence the cubic Jensen gate requires the **positive** orientation of `\widetilde Q_3` (apart from the repeated-root boundary).

## Adversarial consequence: ordinary Stieltjes positivity is definitively the wrong mechanism

The exact identity
\[
\boxed{\widetilde Q_3=-3(w^2+4v^3)}
\]
shows that if the normalized sequence were a genuine Stieltjes moment sequence, then `v\ge0` and hence
\[
\widetilde Q_3\le0.
\]
Because the discriminant has the same sign as `\widetilde Q_3`, ordinary Stieltjes positivity would obstruct rather than prove cubic Jensen hyperbolicity (except at degeneracy).

This closes the previous sign-orientation uncertainty. It is an important negative result: **the RH route cannot be reduced to proving that the relevant coefficient sequence is an ordinary Stieltjes moment sequence.** Any successful positivity mechanism must be more structured and must exploit the specific theta/factorial geometry of the xi coefficients.

## Correct structural target

The next target is no longer a sign audit. It is an exact theta representation of the correctly oriented discriminant:
\[
\boxed{
\Delta_3(J^{3,n})\ge0
\quad\Longleftrightarrow\quad
\widetilde Q_3(n)\ge0
}
\]
for the nondegenerate normalization above.

The desired proof must derive this inequality from an explicit theta identity, not from generic Stieltjes moment positivity.

## Uniform-shift propagation target

Known Jensen theory proves hyperbolicity for sufficiently large shift `n` at each fixed degree `d`. Therefore a complete proof can be organized as:

1. establish the exact finite-degree gate for the remaining shifts;
2. prove a propagation lemma in `n` or an exact multiplier relation;
3. use the asymptotic hyperbolic region only as a boundary condition;
4. eliminate the entire infinite complementary wedge.

The propagation lemma must be an exact theorem about the Jensen sequence; numerical continuation is not admissible.

## Candidate propagation invariant

Let
\[
r_j(n)=\frac{q_{n+j}}{q_n},
\]
and let `\mathcal H_{d,n}` denote a chosen Hermite determinant for `J^{d,n}`. Search for
\[
\mathcal H_{d,n+1}-\Lambda_{d,n}\mathcal H_{d,n}
=\mathcal P_{d,n},
\qquad
\Lambda_{d,n}\ge0,
\quad
\mathcal P_{d,n}\ge0,
\]
with `\mathcal P_{d,n}` admitting an explicit theta-kernel representation.

Such an identity would convert the infinite shift problem into a boundary problem plus a positive propagation law. No such identity has yet been proved.

## Stronger next experiment: exact theta multi-integral

Use the exact theta representation of the coefficient sequence to write each `q_{n+j}` as a one-dimensional integral. Substitute four such representations into the quartic polynomial defining the cubic discriminant. Then symmetrize the resulting four-variable integral.

The specific objective is to determine whether the discriminant numerator factors into a manifestly sign-controlled kernel involving Vandermonde-type factors, finite differences, or a theta modular defect. Any proposed factorization must be checked symbolically before being promoted to a positivity claim.

## Status

This frontier now contains an **exact algebraic orientation theorem** for the cubic Jensen gate and eliminates one entire false route (ordinary Stieltjes positivity). It is **not an RH proof**. The remaining mathematical wall is an independently derived theta-specific certificate or a rigorous shift-propagation law that controls all degrees and shifts.
