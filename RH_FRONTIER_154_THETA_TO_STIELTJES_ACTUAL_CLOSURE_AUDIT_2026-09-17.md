# RH Frontier 154 — Theta → Stieltjes Actual Closure Audit — 2026-09-17

## Status
OPEN. This frontier records an actual proof attempt of the first arrow

Theta modularity → positive spectral/Stieltjes structure.

No zero locations are assumed. No operator is defined from the zeros.

## 1. Canonical target
Let
\[
\Xi(w)=\xi(1/2+w),\qquad H(z)=\Xi(\sqrt z).
\]
Because \(\Xi\) is even, \(H\) is entire. A sufficient spectral gate is
\[
\frac{H'(z)}{H(z)}=a+\int_{[0,\infty)}\frac{d\mu(t)}{z+t},\qquad \mu\ge0.
\tag{S}
\]
If (S) is established with the required growth/zero-free factor control, all poles of \(H'/H\) lie on \(( -\infty,0]\), hence all zeros of \(H\) lie there and RH follows.

## 2. Exact real-axis criterion
Set
\[
m(z)=-\frac{H'(z)}{H(z)}.
\]
For any Stieltjes representation
\[
m(z)=a+\int_0^\infty\frac{d\mu(t)}{z+t},
\]
we necessarily have, for every \(x>0\),
\[
(-1)^n m^{(n)}(x)=n!\int_0^\infty\frac{d\mu(t)}{(x+t)^{n+1}}\ge0,\qquad n\ge0.
\tag{CM}
\]
Conversely, if \(m\) is completely monotone on \((0,\infty)\) and satisfies the appropriate Stieltjes growth/analytic continuation conditions, Bernstein/Stieltjes theory reconstructs a positive measure and gives (S).

Thus the theta-to-Stieltjes problem can be reduced to an unconditional theta proof of complete monotonicity plus the analytic continuation/growth certificate.

## 3. Theta representation attempted
Using the standard theta kernel representation
\[
\Xi(w)=4\int_0^\infty \Phi(u)\cosh(wu)\,du,
\]
we obtain formally, by differentiation under the integral (justified on compact subsets by the super-exponential decay of \(\Phi\)),
\[
H(z)=4\int_0^\infty \Phi(u)\cosh(u\sqrt z)\,du,
\]
\[
H'(z)=\frac{2}{\sqrt z}\int_0^\infty u\Phi(u)\sinh(u\sqrt z)\,du,
\]
with the removable value at \(z=0\) obtained by series expansion.

The obstruction is now explicit: positivity of \(\Phi\) does not imply a fixed sign for the ratio \(H'/H\), because \(\cosh(u\sqrt z)\) and \(\sinh(u\sqrt z)\) are not a positive Laplace kernel in \(z\) on the required complex domain.

## 4. Why the naive theta-positivity step does not close the arrow
A tempting claim would be
\[
\Phi(u)\ge0 \Longrightarrow (-1)^n\frac{d^n}{dz^n}\left(-H'(z)/H(z)\right)\ge0.
\]
This implication is false as a general transform theorem: the logarithmic derivative is nonlinear and the kernel \(\cosh(u\sqrt z)\) does not preserve complete monotonicity in \(z\). Therefore a genuinely Riemann-specific modular identity is still required.

This matches the project’s earlier cumulant obstruction: raw theta moment positivity cannot simply be transferred through the logarithmic derivative.

## 5. A stronger exact bridge to prove
The remaining proof-bearing identity should be one of the following equivalent-strength certificates:

### A. Complete-monotonicity certificate
For every \(x>0\) and \(n\ge0\), derive an explicit finite/multi-copy theta integral
\[
(-1)^n\frac{d^n}{dx^n}\left(-\frac{H'(x)}{H(x)}\right)
=\int_{(0,\infty)^{q_n}} |P_n(u_1,\ldots,u_{q_n};x)|^2\,d\nu_n\ge0.
\]
The integrand and measure must be constructed solely from the theta lattice and modular transformations.

### B. Direct resolvent certificate
Construct a theta-defined self-adjoint \(J\ge0\) and prove
\[
-\frac{H'(z)}{H(z)}=a+\langle v,(J+z)^{-1}v\rangle.
\]
The determinant/characteristic-function identity must be established independently.

### C. Determinant certificate
Construct finite theta matrices \(J_N\ge0\) such that
\[
\det(I+zJ_N^{-1})\to H(z)/H(0)
\]
locally uniformly with a zero-divisor theorem. Exact determinant matching is the missing step; positivity of \(J_N\) alone is insufficient.

## 6. Important correction to the project's earlier formulation
The first arrow is NOT currently proved merely from theta modularity. The mathematically precise bottleneck is:
\[
\boxed{\text{theta modularity + a new Riemann-specific positivity/Gram identity}}
\Longrightarrow\text{Stieltjes structure}.
\]
Modularity by itself supplies transformations and functional identities; it does not automatically imply total positivity, complete monotonicity, or a positive spectral measure.

## 7. Adversarial checkpoint
Any proposed identity must survive these tests:
1. it must be derived without writing zeros as \(1/2+i\gamma\);
2. it must work for every \(n\), not finitely many orders;
3. it must preserve the nonlinear quotient structure of \(H'/H\);
4. it must provide the analytic continuation from \((0,\infty)\) to \(\mathbb C\setminus(-\infty,0]\);
5. it must not define the measure/operator from the unknown zeros.

## 8. Current conclusion
We have converted the first arrow into a sharper theorem: an unconditional theta proof of complete monotonicity/Stieltjes structure for \(-H'/H\), or an equivalent positive-resolvent/determinant identity. The arrow itself remains OPEN. No valid RH proof has been obtained in this frontier.
