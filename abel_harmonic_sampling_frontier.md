# Abel-regularized harmonic arithmetic sampling: exact frontier

## Status

**Established:** Abel regularization gives an exact positive finite-ρ sampling operator; its kernel is explicit through the polylogarithm; the singular harmonic limit is logarithmic on the diagonal and distributional off the diagonal.

**Not established:** the ρ→1 limit yields an RH-independent coercive lower bound. RH remains open.

## 1. Abel regularization

For 0<r<1 define
\[
Q_r=\sum_{n\ge1}r^n\,|Be_n\rangle\langle Be_n|,
\qquad
(Be_n)(t)=\frac{\zeta(1/2+it)}{1/2+it}n^{-1/2-it}.
\]
Every finite partial sum is positive and the series converges in trace norm because
\[
\operatorname{Tr}Q_r=(\log(2\pi)-\gamma)\sum_{n\ge1}\frac{r^n}{n}
=-(\log(2\pi)-\gamma)\log(1-r).
\]
Thus Q_r is positive trace class for every r<1.

## 2. Exact kernel

Writing \(\Delta=t-u\),
\[
Q_r(t,u)=
\frac{\zeta(1/2+it)}{1/2+it}
\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}
\sum_{n\ge1}r^n n^{-1-i\Delta}.
\]
Hence
\[
\boxed{
Q_r(t,u)=
\frac{\zeta(1/2+it)}{1/2+it}
\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}
\operatorname{Li}_{1+i(t-u)}(r).
}
\]
This is exact for 0<r<1.

## 3. Singular harmonic limit

For fixed nonzero \(\Delta\), Abel's theorem gives
\[
\lim_{r\uparrow1}\operatorname{Li}_{1+i\Delta}(r)=\zeta(1+i\Delta).
\]
At \(\Delta=0\),
\[
\operatorname{Li}_1(r)=-\log(1-r),
\]
so the diagonal diverges logarithmically.

Therefore the formal harmonic kernel cannot be interpreted as an ordinary bounded integral kernel by simply putting r=1. The correct limit requires a renormalization or distributional formulation.

## 4. Positivity versus coercivity

For every r<1,
\[
\langle f,Q_rf\rangle
=\sum_{n\ge1}r^n|(B^*f)_n|^2\ge0.
\]
But Q_r is trace class, hence compact on the infinite-dimensional critical-line Hilbert space. Consequently
\[
Q_r\not\ge cI\qquad(c>0).
\]
Thus Abel regularization preserves positivity but cannot itself supply the required uniform lower bound.

## 5. The real proof-bearing limit

Any successful harmonic mechanism must establish a renormalized limit of the form
\[
Q_{\mathrm{harm}}=\operatorname*{ren\!\lim}_{r\uparrow1}
\left(Q_r-a(r)P-b(r)I\right)
\]
(or an equivalent positive quadratic-form limit), together with an RH-independent estimate
\[
\langle f,Q_{\mathrm{harm}}f\rangle\ge c\|f\|^2
\]
on the relevant closure/image class.

The divergence is explicitly diagonal/logarithmic, so any proposed subtraction must account for the \(-\log(1-r)\) singularity. No such coercive renormalized identity is proved here.

## 6. Non-circularity audit

Nothing above assumes RH, a zero-free half-plane, or Nyman–Beurling density. The result is an exact regularized positive family plus a precise identification of its singular boundary. It narrows the next target but is not an RH proof.

## 7. Literature connection

Ehm's 2024 analysis of the Nyman–Beurling Gram matrices derives explicit Gram kernels and reciprocity relations, consistent with the need to handle the critical boundary through nontrivial analytic continuation rather than an absolutely convergent double Dirichlet series. See arXiv:2405.06349.
