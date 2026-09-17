# Weighted arithmetic sampling: exact operator and a sharp no-go boundary

## Status

**Established:** exact weighted sampling operator; exact trace formula for summable weights; compactness obstruction to any infinite-dimensional lower frame bound for summable weights; explicit critical boundary for power weights.

**Not established:** a non-summable-weight coercive identity for the Nyman–Beurling image; RH remains open.

## 1. Weighted sampling form

Let

\[
(B e_n)(t)=\frac{\zeta(1/2+it)}{1/2+it}\,n^{-1/2-it}
\]

in the critical-line Mellin model. For nonnegative weights `w_n`, define formally

\[
Q_w=\sum_{n\ge1}w_n\,|Be_n\rangle\langle Be_n|,
\qquad
\mathcal S_w(f)=\sum_{n\ge1}w_n|(B^*f)_n|^2=\langle f,Q_wf\rangle.
\]

Every finite truncation is positive semidefinite, so positivity itself is automatic.

## 2. Exact trace of the summable-weight operator

The diagonal Gram entries are independent of `n` after the Mellin normalization:

\[
\|Be_n\|^2=K(n,n)=\frac{K(1,1)}{n},
\qquad
K(1,1)=\log(2\pi)-\gamma.
\]

Therefore, whenever

\[
\sum_{n\ge1}\frac{w_n}{n}<\infty,
\]

`Q_w` is positive trace class and

\[
\boxed{
\operatorname{Tr}Q_w
=(\log(2\pi)-\gamma)\sum_{n\ge1}\frac{w_n}{n}<\infty.
}
\]

Hence `Q_w` is compact.

## 3. No-go theorem for summable weighted coercivity

The critical Hilbert space is infinite-dimensional. A compact positive operator cannot satisfy

\[
Q_w\succeq cI,\qquad c>0,
\]

because then every singular value/eigenvalue would be at least `c`, forcing infinite trace.

Thus:

\[
\boxed{
\sum_{n\ge1}\frac{w_n}{n}<\infty
\quad\Longrightarrow\quad
\nexists c>0:\n\;\mathcal S_w(f)\ge c\|f\|^2\;\forall f.
}
\]

This is unconditional and uses no information about zero locations.

## 4. Power-weight boundary

For `w_n=n^{-\alpha}`,

\[
\sum_n\frac{w_n}{n}=\sum_n n^{-1-\alpha}
\]

converges exactly for `\alpha>0`. Therefore every decaying power weight

\[
w_n=n^{-\alpha},\qquad \alpha>0,
\]

is ruled out as a source of a global lower frame bound by compactness.

The harmonic-scale boundary `w_n\asymp 1` is the first regime not excluded by this trace argument. More generally, any candidate coercive arithmetic sampling weight must fail the summability condition

\[
\sum_n w_n/n<\infty.
\]

## 5. Exact kernel for a useful non-summable test family

Take `w_n=1`. The formal weighted kernel is

\[
Q_1(t,u)=
\frac{\zeta(1/2+it)}{1/2+it}
\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}
\sum_{n\ge1}n^{-1-i(t-u)}.
\]

The last Dirichlet series is only conditionally/distributionally meaningful on the line `Re=1`; it cannot be treated as an ordinary convergent series. This is exactly where a genuine regularization or arithmetic summation identity is required.

For comparison, `w_n=1/n` gives the absolutely convergent kernel

\[
\boxed{
Q_{1/n}(t,u)=
\frac{\zeta(1/2+it)}{1/2+it}
\frac{\overline{\zeta(1/2+iu)}}{1/2-iu}
\zeta(2+i(t-u)),
}
\]

but this case is already compact by the trace test and therefore cannot be coercive on the full infinite-dimensional space.

## 6. What this changes in the RH attack

The previous target was an independent positive sampling identity

\[
\sum_n w_n|(B^*f)_n|^2\ge c\|f\|^2.
\]

The exact trace calculation proves a sharp restriction on that strategy:

\[
\boxed{
\text{Any global coercive sampling mechanism must live at or beyond the non-summable weight boundary.}
}
\]

So merely choosing nicer decaying weights, including every positive power-decay weight, cannot close the RH gap.

The next proof-bearing target is therefore a **renormalized harmonic arithmetic sampling identity** (or a different non-summable positive operator) whose positivity and lower bound can be established independently of RH. No such identity is currently proved here.

## 7. Non-circularity audit

No step assumes RH, a zero-free half-plane, zero locations, or the Nyman–Beurling density conclusion. The only input is the exact Mellin representation of `Be_n` and Hilbert-space trace/compactness theory.

This is a narrowing result, not an RH proof.
