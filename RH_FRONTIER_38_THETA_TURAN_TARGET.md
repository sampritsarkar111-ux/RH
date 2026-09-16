# Frontier 38 — exact theta-level Turan target

## Objective

Attack the necessary degree-3 gate from Frontier 37 directly from the Riemann theta representation, without assuming RH.

For the standard normalized Xi/Taylor coefficients \(\gamma_m\), define
\[
T_m:=\gamma_{m+1}^2-\gamma_m\gamma_{m+2}.
\]
Frontier 37 proves that the degree-3 Jensen/Hermite condition implies
\[
\boxed{T_m\ge0}
\]
for every relevant shift. The actual degree-3 condition is stronger and also involves the third central coordinate \(w\).

## Theta representation

The available exact coefficient formula has the form
\[
\gamma_m=C\,\frac{m!}{(2m)!}\left(32\binom{2m}{2}F(2m-2)-F(2m)\right),
\]
where
\[
F(N)=\int_1^\infty (\log t)^N t^{-3/4}\theta_0(t)\,dt,
\qquad
\theta_0(t)=\sum_{k\ge1}e^{-\pi k^2t},
\]
with a positive constant \(C\). This representation is a starting point for an RH-independent calculation. A published mathematical reference reproduces this exact integral formula. See the source cited in the research log.

## New concrete target

Substitute the integral formula for \(\gamma_m,\gamma_{m+1},\gamma_{m+2}\) into
\[
T_m=\gamma_{m+1}^2-\gamma_m\gamma_{m+2}.
\]
After combining the two double integrals, seek an identity
\[
T_m=\iint_{[1,\infty)^2}K_m(t,u)\,d\nu(t)d\nu(u)
\]
where \(d\nu(t)=t^{-3/4}\theta_0(t)dt\), and where \(K_m(t,u)\) can be shown nonnegative by an explicit algebraic factorization such as
\[
K_m(t,u)=(\log t-\log u)^2\,R_m(\log t,\log u)
\]
with \(R_m\ge0\), or by a finite sum of squares.

The crucial point is that the factorial/binomial prefactors must remain exact; dropping them or replacing the theta measure by an arbitrary positive measure is not allowed, because Frontier 33 gives a counterexample to the generic moment mechanism.

## Adversarial test

Any proposed kernel factorization must be checked symbolically before being treated as a theorem. In particular:

1. verify exact equality after expansion;
2. test diagonal \(t=u\), where the \((\log t-\log u)^2\) factor vanishes;
3. test extreme ratios \(t/u\to\infty\);
4. test the smallest admissible \(m\);
5. ensure no step uses the unknown signs/locations of nontrivial zeros.

## Why this is a useful closure gate

If \(T_m<0\) for any exact coefficient index, the proposed all-degree Jensen route is dead at degree 3. If \(T_m\ge0\) is proved for all \(m\), this still does not prove RH: one must continue to the stronger five-term degree-3 inequality and then all degrees.

## Status

**Concrete RH-independent analytic target; not yet a proof.**
