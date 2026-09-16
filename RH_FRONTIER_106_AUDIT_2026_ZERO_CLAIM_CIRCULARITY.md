# Frontier 106 — audit of a 2026 preprint claiming Λ=0

Date: 2026-09-16

## Why this was investigated

A current (April 2026) unpeer-reviewed preprint, *The De Bruijn-Newman Constant Is Zero*, claims an unconditional proof of RH/Λ=0 using log-concavity, Jensen determinants, Desnanot–Jacobi recursion, and a spectral-gap argument. The paper itself is marked **not peer-reviewed**. Its central global step was therefore audited rather than adopted.

## Exact circularity found

The proposed global tail argument defines
\[
g(z)=\Xi(\sqrt z)
\]
and then states that the zeros of \(g\) can be written
\[
z_m=-t_m^2,
\qquad \rho_m=-1/t_m^2,
\]
where \(t_m\) are the Riemann zero ordinates on the critical line. It then uses the Binet–Cauchy expansion of Toeplitz minors to obtain
\[
\mu_r(n)\to 2\log(t_{n+1}/t_n)>0.
\]

The problem is that, before RH is proved, the zeros of \(g\) are only known to be the transformed nontrivial zeros of \(\xi\), and they need not all have the form \(-t_m^2\) with real \(t_m\). Writing the full spectral expansion with \(\rho_m=-1/t_m^2\) and ordering it by real critical-line ordinates therefore imports the desired real-zero structure into the tail argument.

The preprint itself contains a revealing sentence later: it says that ordering \(|z_0|<|z_1|<\cdots\) by the real critical-line ordinates follows from RH. That means the same spectral ordering cannot be used as an unconditional premise for proving RH.

## Precise logical failure

The claimed implication
\[
\text{finite DJ positivity + first-zero spectral gap}
\Longrightarrow
D_r(n)>0\ \forall r,n
\]
is not established unless the dominant-pole expansion is proved using the actual zeros of \(g\), with no assumption that all of them lie on the negative real axis.

For an unconditional proof, one must instead establish one of the following without RH:

1. a zero-location-free bound on the complex zero spectrum of \(g\) that gives the needed tail sign;
2. a determinant recurrence whose positivity propagates to all \(r,n\) without invoking the critical-line ordering of the zeros;
3. an independent total-positivity/Laguerre–Pólya theorem for the coefficient sequence.

## Consequence for our project

This does **not** prove the preprint's final theorem false; it identifies a missing unconditional justification in the presented argument. More importantly, it tells us exactly what a genuine breakthrough must avoid: no tail estimate may use \(t_n\), \(t_{n+1}\), or a real ordered zero spectrum beyond the range where those facts have independently been certified.

## Current status

As of 2026-09-16, the Clay Mathematics Institute still lists RH as unsolved. The claimed 2026 preprint is explicitly marked not peer-reviewed. Therefore it cannot be treated as a completed proof without independently repairing the circular step above.

Our research program should now target the same useful determinant/Desnanot–Jacobi architecture but replace the spectral tail with a zero-location-free analytic invariant.
