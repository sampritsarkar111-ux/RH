# Harmonic sampling: exact compactness obstruction

For 0<r<1,
\[
Q_r=\sum_{n\ge1}r^n|Be_n\rangle\langle Be_n|\succeq0,
\qquad
\operatorname{Tr}Q_r=(\log(2\pi)-\gamma)(-\log(1-r)).
\]
Thus each Q_r is positive trace class and compact. Therefore no fixed r<1 can satisfy Q_r >= cI on the infinite-dimensional critical-line Hilbert space.

Its exact kernel is
\[
Q_r(t,u)=
\frac{\zeta(1/2+it)}{1/2+it}
\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}
\operatorname{Li}_{1+i(t-u)}(r).
\]
As r->1, the diagonal factor is Li_1(r)=-log(1-r), while for Delta=t-u !=0,
Li_{1+iDelta}(r)->zeta(1+iDelta).

Therefore the only potentially new mechanism is a singular/non-trace-class boundary object or a target-specific inequality. Abel regularization itself does not produce the missing lower bound.

Status: established partial; RH remains open.