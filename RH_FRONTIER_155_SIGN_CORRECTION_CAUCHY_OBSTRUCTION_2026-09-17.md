# RH Frontier 155 — Sign Correction and Exact Cauchy Audit — 2026-09-17

## Status
OPEN. This frontier corrects the logarithmic-derivative sign convention and audits the proposed first-order obstruction.

## 1. Correct logarithmic derivative convention
Let
\[
\Xi(w)=\xi(1/2+w),\qquad H(z)=\Xi(\sqrt z).
\]
A useful target, if the pole-bearing part can be isolated, is
\[
\boxed{m(z):=\frac{H'(z)}{H(z)}=E'(z)+\int_{[0,\infty)}\frac{d\mu(t)}{z+t},\qquad \mu\ge0.}
\]
For the Stieltjes term, the first derivative on \(x>0\) is non-positive.

## 2. Theta Taylor data
Using
\[
\Xi(w)=4\int_0^\infty\Phi(u)\cosh(wu)\,du,
\qquad \Phi(u)\ge0,
\]
we have
\[
H(z)=4\sum_{k\ge0}\frac{M_{2k}}{(2k)!}z^k,
\qquad M_r=\int_0^\infty u^r\Phi(u)\,du,
\]
and therefore
\[
h_k:=H^{(k)}(0)=\frac{4k!}{(2k)!}M_{2k}>0.
\]

## 3. Exact nonlinear identities
For \(m=H'/H\),
\[
m(0)=\frac{h_1}{h_0},
\]
\[
m'(0)=\frac{h_0h_2-h_1^2}{h_0^2},
\]
\[
m''(0)=\frac{h_0^2h_3-3h_0h_1h_2+2h_1^3}{h_0^3}.
\]
These are exact and zero-free in their derivation.

## 4. Correction: generic Cauchy-Schwarz is NOT enough
Although
\[
M_2^2\le M_0M_4
\]
by Cauchy-Schwarz, substitution gives
\[
m'(0)=\frac{M_0M_4/3-M_2^2}{M_0^2}.
\]
Thus Cauchy-Schwarz alone does **not** determine the sign because the required threshold is \(M_0M_4\gtrless 3M_2^2\), not merely \(M_0M_4\gtrless M_2^2\).

Therefore the earlier claimed exact no-go from Cauchy-Schwarz was too strong and is withdrawn. This is an important rigor correction.

## 5. Genuine next calculation
The first real theta-specific test is
\[
\Delta_2:=M_0M_4-3M_2^2.
\]
Its sign must be derived from the explicit theta kernel, not from generic moment positivity. The next nonlinear test is
\[
\Delta_3:=M_0^2M_6-9M_0M_2M_4+12M_2^3.
\]
These quantities determine the first nontrivial logarithmic-derivative signs after the factorial normalization.

## 6. Main bridge after the audit
Regardless of the sign of these raw tests, the proof-bearing target remains
\[
R(z)=\frac{H'(z)}{H(z)}-E'(z)
\]
with E independently constructed from theta/modular data and R admitting a positive Stieltjes representation. No zeros may be used to define E, R, the measure, or an operator.

## 7. Adversarial checkpoint
Any successful closure must be all-order, preserve the nonlinear quotient, justify analytic continuation and growth, and avoid encoding the unknown zero set into the construction.

No RH proof is claimed.