# RH Frontier 155 — Sign Correction and Exact Cauchy Obstruction — 2026-09-17

## Status
OPEN. This frontier corrects the master Stieltjes target and derives an exact unconditional obstruction to the overly rigid constant-plus-Stieltjes ansatz.

## 1. Correct logarithmic derivative
Let
\[
\Xi(w)=\xi(1/2+w),\qquad H(z)=\Xi(\sqrt z).
\]
If the zeros of H were all on the negative real axis, the pole-bearing logarithmic derivative would have the form
\[
\boxed{m(z)=\frac{H'(z)}{H(z)}=E'(z)+\int_{[0,\infty)}\frac{d\mu(t)}{z+t},\quad \mu\ge0.}
\]
The earlier sign choice \(-H'/H\) was incorrect for this convention: a positive Stieltjes resolvent has positive value on the positive axis and negative first derivative.

## 2. Theta Taylor data
Using
\[
\Xi(w)=4\int_0^\infty\Phi(u)\cosh(wu)\,du,\qquad \Phi(u)\ge0,
\]
we have
\[
H(z)=4\sum_{k\ge0}\frac{M_{2k}}{(2k)!}z^k,
\qquad M_r=\int_0^\infty u^r\Phi(u)\,du.
\]
Therefore
\[
h_k:=H^{(k)}(0)=\frac{4k!}{(2k)!}M_{2k}>0.
\]

## 3. Exact first-order obstruction
Cauchy-Schwarz for the positive measure \(\Phi(u)du\) gives
\[
M_2^2\le M_0M_4.
\]
After the factorial conversion,
\[
h_1^2\le \frac{1}{3}h_0h_2.
\]
In particular \(h_0h_2-h_1^2>0\). Since
\[
m'(0)=\frac{h_0h_2-h_1^2}{h_0^2},
\]
we obtain
\[
\boxed{m'(0)>0.}
\]
But a constant-plus-Stieltjes representation
\[
m(z)=a+\int_0^\infty\frac{d\mu(t)}{z+t}
\]
requires
\[
m'(0)=-\int_0^\infty t^{-2}\,d\mu(t)\le0
\]
whenever the derivative exists. Hence that ansatz is impossible for the positive-theta representation.

## 4. Consequence
This does NOT disprove RH. It proves that the project must retain a nonconstant entire factor/term \(E'(z)\). The pole-bearing remainder, not the entire logarithmic derivative by itself, is the correct Stieltjes target.

## 5. Next proof-bearing calculation
Find an independently theta-defined entire function E such that
\[
R(z):=\frac{H'(z)}{H(z)}-E'(z)
\]
has a Stieltjes representation. The first concrete tests are:
1. derive E from the Archimedean/theta local asymptotic rather than zeros;
2. verify \((-1)^nR^{(n)}(x)\ge0\) for all n on x>0;
3. prove the Pick/Stieltjes analytic continuation of R;
4. only then build the positive resolvent/determinant bridge.

## 6. Low-order nonlinear identities
For arbitrary Taylor data h_k=H^(k)(0),
\[
m(0)=h_1/h_0,
\]
\[
m'(0)=(h_0h_2-h_1^2)/h_0^2,
\]
\[
m''(0)=(h_0^2h_3-3h_0h_1h_2+2h_1^3)/h_0^3.
\]
These formulas expose exactly where raw theta moment positivity must be transformed by a genuinely Riemann-specific subtraction E'.

## 7. Adversarial checkpoint
No zero locations are used. No spectral operator is defined from zeros. The result is an exact no-go theorem for one overly rigid Stieltjes normalization and a sharper target for the next attack.
