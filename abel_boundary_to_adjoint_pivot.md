# Abel boundary pivot: from harmonic sampling to adjoint uniqueness

The Abel-regularized family
\[
Q_r=\sum_{n\ge1}r^n|Be_n\rangle\langle Be_n|,
\quad 0<r<1,
\]
is positive trace class. Hence fixed-r coercivity is impossible. As r→1, the kernel has the exact form
\[
Q_r(t,u)=\frac{\zeta(1/2+it)}{1/2+it}\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}\operatorname{Li}_{1+i(t-u)}(r),
\]
with diagonal divergence -log(1-r).

Therefore the next independent target is not another summable/Abel weight. It is the annihilator problem:
\[
B^*f=0 \Longrightarrow f=0.
\]
Under the Mellin/Fourier model this means a zeta-weighted transform vanishes at every arithmetic frequency log n. A proof must establish uniqueness for this specific image class without assuming that zeta is zero-free in Re(s)>1/2.

A relevant Hardy-space literature result explicitly states that the orthogonal complement of the Nyman-Beurling Hardy family encodes information about zeta zeros; thus an adjoint-kernel argument must avoid simply assuming the complement is trivial. See Calderaro–Manzur–Noor–Santos, arXiv:2203.05030.

## Proof-bearing target

Find an unconditional theorem of the form
\[
\{(B^*f)_n=0\ \forall n\}\Longrightarrow f=0
\]
for the exact Nyman-Beurling image class, using only independent analytic/growth/sampling input. If such a theorem is proved, Nyman–Beurling density follows and RH follows. If it requires an outer-function or zero-free statement equivalent to RH, the route is circular and must be rejected.

Status: research frontier; no RH proof.