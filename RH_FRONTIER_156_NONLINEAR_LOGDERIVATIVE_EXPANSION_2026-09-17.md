# RH Frontier 156 — Nonlinear Log-Derivative Expansion and Next Attack — 2026-09-17

## 1. Exact expansion
Write
\[
H(z)=\sum_{k\ge0}h_k\frac{z^k}{k!},\qquad m(z)=\frac{H'(z)}{H(z)}.
\]
Then
\[
m(0)=\frac{h_1}{h_0},
\]
\[
m'(0)=\frac{h_0h_2-h_1^2}{h_0^2},
\]
\[
m''(0)=\frac{h_0^2h_3-3h_0h_1h_2+2h_1^3}{h_0^3}.
\]
These are exact and contain no zero data.

## 2. Theta moment substitution
For
\[
H(z)=4\int_0^\infty\Phi(u)\cosh(u\sqrt z)du,
\]
set \(M_r=\int_0^\infty u^r\Phi(u)du\). Then
\[
h_k=\frac{4k!}{(2k)!}M_{2k}.
\]
Consequently
\[
m'(0)=\frac{1}{3}\frac{M_0M_4}{M_0^2}-\frac{M_2^2}{M_0^2}
=\frac{M_0M_4/3-M_2^2}{M_0^2}.
\]
Cauchy-Schwarz only gives \(M_0M_4\ge M_2^2\), so it does NOT by itself imply positivity after the factorial factor 1/3. This corrects the stronger claim in Frontier 155: the simple Cauchy argument is insufficient to establish the sign of m'(0). The exact coefficient formula remains valid.

## 3. New calculation target
The next attack is therefore sharper: determine the exact sign of
\[
\Delta_2:=M_0M_4-3M_2^2
\]
from the explicit theta kernel, rather than using generic moment positivity. If \(\Delta_2\) has a definite sign, this gives the first genuine theta-specific cumulant test. Repeat for
\[
\Delta_3:=M_0^2M_6-9M_0M_2M_4+12M_2^3,
\]
which controls \(m''(0)\) after the factorial normalization.

## 4. Crucial lesson
The nonlinear quotient cannot be reduced to ordinary moment positivity. The required object is a theta-specific sequence of factorially renormalized Hankel/cumulant inequalities. This is precisely where modular/arithmetic structure must enter.

## 5. Parallel next steps
A. Compute \(\Delta_2,\Delta_3,\Delta_4\) exactly/numerically from the theta kernel and seek modular SOS identities.
B. Independently derive the entire subtraction \(E'(z)\) from the theta modular asymptotic and test \(R=H'/H-E'\).
C. Build finite theta matrices whose principal minors encode the same factorial-cumulant inequalities.
D. Search the literature for unconditional positive-resolvent/Stieltjes representations and audit any claimed RH proofs for circular zero encoding.

No zero locations are inserted. No RH proof is claimed.