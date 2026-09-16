# Frontier 100 — exact positivity of the completed theta kernel and the completion trap

Date: 2026-09-16

## 1. Completed kernel

Let
\[
\phi_m(u)=\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)e^{-\pi m^2e^{2u}},
\qquad
\Phi(u)=\sum_{m\ge1}\phi_m(u).
\]
The completed theta identity gives
\[
\Phi(-u)=\Phi(u).
\]
This symmetry is a property of the complete lattice sum, not of each individual \(\phi_m\).

## 2. New exact positivity lemma

Set \(t=e^{2u}>0\). Then
\[
\phi_m(u)=\pi m^2t^{5/4}\left(2\pi m^2t-3\right)e^{-\pi m^2t}.
\]
If
\[
t\ge \frac{3}{2\pi},
\]
then every summand is nonnegative and the \(m=1\) summand is strictly positive except at the endpoint. Hence \(\Phi(u)>0\) throughout this region.

If
\[
t<\frac{3}{2\pi},
\]
then
\[
t^{-1}>\frac{2\pi}{3}>\frac{3}{2\pi},
\]
so \(\Phi(-u)>0\) by the already-established positive region. Since \(\Phi(-u)=\Phi(u)\), it follows that
\[
\boxed{\Phi(u)>0\qquad\forall u\in\mathbb R.}
\]

Thus the completed kernel defines a genuine positive measure \(d\mu(u)=\Phi(u)\,du\).

## 3. Completion trap: termwise Mellin integration is invalid

Although each \(\phi_m\) is elementary, one must not integrate the individual lattice terms from \(u=-\infty\) to \(+\infty\) and then sum over \(m\). Under \(t=e^{2u}\), the formal termwise integral produces an \(m^{-1/2}\) series whose separate pieces have divergent small-\(t\) behavior and whose cancellation is part of the completed theta transformation. The apparent sign contradiction obtained by termwise Mellin integration is therefore not a valid contradiction to \(\Phi>0\).

This is a concrete analytic warning for Frontier 98: Poisson/Jacobi completion must occur before global moment evaluation whenever the small-\(t\) endpoint is involved.

## 4. Consequence for the degree-two gate

The positive-measure interpretation of the corrected kernel is legitimate only after the completed lattice sum is formed. The exact gate remains
\[
\frac{\operatorname{Var}(Y)}{E[Y]^2}
\le
R_n-1,
\qquad
R_n-1=
\frac{4n^2+16n+13}{(n+1)(2n+1)(2n+5)}.
\]
The right-hand side is asymptotic to \(1/n\). Therefore any theta-induced distribution whose coefficient of variation has a fixed positive lower bound cannot satisfy this gate for all sufficiently large \(n\). Establishing such a lower bound for the exact \(Y\) used by the Jensen construction is now a sharply defined adversarial test.

## 5. Research status

This is a rigorous kernel-positivity and analytic-completion lemma, not an RH proof. It strengthens the next target by proving that the completed \(\Phi(u)du\) measure is positive while simultaneously ruling out a tempting but invalid termwise Mellin shortcut.

Next proof-bearing target: identify the exact \(Y\)-measure in the Jensen degree-two construction and either prove the coefficient-of-variation gate for every \(n\), or derive an exact contradiction showing that this particular degree-two gate cannot be the RH mechanism.
