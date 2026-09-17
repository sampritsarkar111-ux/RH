# RH Frontier 128 — Theta Modular Perturbation Determinant Program — 2026-09-17

## Objective
Construct, directly from the unsummed completed theta modular involution, a trace-class/self-adjoint operator family whose Fredholm determinant has exactly the completed Xi divisor. This is the proof-bearing replacement for the impossible direct identification of the continuous theta Weyl m-function with the meromorphic logarithmic derivative Xi'/Xi.

## 1. Why the unsummed kernel must be retained

The positive theta density determines a continuous spectral measure and hence a Herglotz Cauchy transform. That representation is exact but has no discrete pole set matching Xi zeros. The modular involution contains additional cancellation/pairing information that disappears after passing only to the scalar positive measure.

Therefore the construction must begin before the collapse to dmu.

## 2. Abstract determinant target

Seek an operator K(s) on a fixed Hilbert space such that:

\[
\boxed{\det(I-K(s))=E(s)\Xi(s)}
\]

where K(s) is trace class (or finite rank), E(s) is entire and zero-free, and the determinant is normalized at a fixed base point.

If additionally K(s) is self-adjoint for real s and belongs to an operator class for which zeros of the determinant are exactly spectral crossings, then Xi zeros are forced to be real.

## 3. Theta modular source

Let theta be represented schematically by a kernel Theta(t) satisfying its exact Poisson/modular involution Theta(t)=t^{-1/2}Theta(1/t), with the completed Xi kernel obtained by the standard Mellin/Gamma completion and subtraction of the elementary terms. The required operator must encode the involution U:t -> 1/t rather than merely its scalar integral.

A candidate weighted involution is
\[
(T_s f)(t)=w_s(t)\,t^{-1/2}f(1/t),
\]
with weights chosen so that T_s is bounded and the deviation from a reference involution is trace class after modular completion.

The key issue is not writing this formal operator but proving the precise Hilbert space, domain, weight, trace-class estimate, and determinant identity.

## 4. Mellin linearization

Under the Mellin transform, the modular involution becomes reflection of the Mellin spectral variable. If M denotes the Mellin transform, then formally
\[
M[U f](z)=M[f](1/2-z).
\]
After centering at the critical symmetry, this becomes a reflection z -> 1-z. The completed zeta factor is itself symmetric under this involution. Thus a determinant formulation should exploit the factorization into symmetric and antisymmetric Mellin sectors.

The proof-bearing target is an exact factorization
\[
\boxed{
\Xi(s)=C(s)\det(I-K_s)
}
\]
where K_s is built from the modular reflection and the completed theta multiplier, with C(s) zero-free.

## 5. Self-adjointness target

For real spectral parameter t, the desired operator A should satisfy
\[
A=A^*,
\]
and the determinant should have the form
\[
\Xi(t)=C(t)\det_F(tI-A)
\]
or an equivalent even spectral determinant with a zero-free factor. This exact equality is essential. Merely obtaining an operator with a similar asymptotic expansion, the same first moments, or the same finite-dimensional approximants is insufficient.

## 6. Zero correspondence checklist

A completed proof must establish, without assuming RH:

- trace-class/Hilbert-Schmidt legitimacy of every determinant;
- analytic dependence on the spectral parameter;
- exact equality with Xi by an identity theorem or a direct determinant evaluation;
- self-adjointness of the spectral operator;
- equality of zero multiplicities;
- absence of spurious determinant zeros from completion factors;
- no zeros lost in Mellin inversion or modular sector decomposition.

## 7. Immediate algebraic test

Any proposed determinant must pass the logarithmic-derivative identity
\[
-\frac{d}{ds}\log\det(I-K_s)
=\operatorname{tr}\big((I-K_s)^{-1}K_s'\big),
\]
whenever the derivative is trace-class legitimate. The right side must reproduce Xi'/Xi up to the derivative of the explicit zero-free completion factor.

This provides a direct falsification test: if the trace side has a continuous-spectrum branch structure incompatible with the meromorphic divisor of Xi, the candidate operator is wrong.

## 8. Current conclusion

The Weyl route has therefore produced a useful but nonfinal object. The decisive next construction is an unsummed-theta modular perturbation determinant. No determinant equal to Xi has yet been derived, and no RH proof is claimed.
