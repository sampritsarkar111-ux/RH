# Frontier 149 — PF∞ / Translation-Total-Positivity Route: Rigorous PF5 No-Go

Date: 2026-09-17

## 1. Purpose

The route “Riemann-Jacobi kernel \Phi is PF∞ / a translation kernel totally positive of all orders \Rightarrow its cosine/Fourier transform is in the Laguerre–Pólya class” requires total positivity beyond TP2. We test a necessary local condition at order 5.

Let
\[
K(x,y)=\Phi(x-y),
\]
with the even Riemann-Jacobi kernel
\[
\Phi(u)=\sum_{n\ge1}\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)e^{-\pi n^2e^{2u}}.
\]
For a translation kernel, TP5 implies the corresponding order-5 derivative Wronskian has the sign forced by the y-derivative factors. Since
\[
\partial_y^jK(x,y)=(-1)^j\Phi^{(j)}(x-y),
\]
the local TP5 condition at the diagonal requires
\[
(-1)^{5\cdot4/2}W_5(u)=W_5(u)\ge0,
\]
where
\[
W_5(u)=\det\big(\Phi^{(i+j)}(u)\big)_{i,j=0}^{4}.
\]
Thus any point where \(W_5<0\) rules out PF5, and hence PF∞, for this translation kernel.

## 2. Exact derivative recurrence

For one theta summand put \(x=\pi n^2\). For
\[
f_{\alpha,x}(u)=e^{\alpha u-xe^{2u}},
\]
write
\[
\left.\frac{d^k}{du^k}f_{\alpha,x}(u)\right|_{u=0}=Q_k^{(\alpha)}(x)e^{-x}.
\]
Then
\[
Q_0^{(\alpha)}(x)=1,
\qquad
Q_{k+1}^{(\alpha)}(x)=(\alpha-2x)Q_k^{(\alpha)}(x)+2x\frac{d}{dx}Q_k^{(\alpha)}(x).
\]
Hence
\[
\Phi^{(k)}(0)=\sum_{n\ge1}p_k(\pi n^2)e^{-\pi n^2},
\]
where \(p_k(x)=4x^2Q_k^{(9/2)}(x)-6xQ_k^{(5/2)}(x)\).
For the needed even orders:
\[
p_0(x)=2x(2x-3),
\]
\[
p_2(x)=\frac{x}{2}(32x^3-224x^2+330x-75),
\]
\[
p_4(x)=\frac{x}{8}(512x^5-8448x^4+41408x^3-68096x^2+30930x-1875),
\]
\[
p_6(x)=\frac{x}{32}(8192x^7-245760x^6+2536960x^5-11109120x^4+20633312x^3-14260064x^2+2610330x-46875),
\]
\[
p_8(x)=\frac{x}{128}(131072x^9-6225920x^8+110460928x^7-932413440x^6+3959811072x^5-8263546368x^4+7716000128x^3-2640409856x^2+214061730x-1171875).
\]
Because \(\Phi\) is even, all odd derivatives vanish at zero.

## 3. Reduction of W5 at u=0

Set
\[
a_{2j}=\Phi^{(2j)}(0).
\]
After the zero odd rows/columns are separated,
\[
W_5(0)=\big(a_2a_6-a_4^2\big)
\det\begin{pmatrix}
a_0&a_2&a_4\\
a_2&a_4&a_6\\
a_4&a_6&a_8
\end{pmatrix}.
\]

Using the first four theta terms exactly with outward interval arithmetic, together with the analytic tail estimate below, gives
\[
a_0\in[0.8933938009342468583,\,0.8933938009342469180],
\]
\[
a_2\in[-16.73050077470326034,\,-16.73050077470325340],
\]
\[
a_4\in[812.1628334554236776,\,812.1628334554248974],
\]
\[
a_6\in[-50735.72590616856284,\,-50735.72590616827049],
\]
\[
a_8\in[1823335.788363595197,\,1823335.788363685094].
\]
These enclosures imply
\[
a_2a_6-a_4^2\in[189225.6335319359,\,189225.6335319432]>0,
\]
and
\[
\det\begin{pmatrix}
a_0&a_2&a_4\\a_2&a_4&a_6\\a_4&a_6&a_8
\end{pmatrix}
\in[-644014900.3774350,\,-644014900.3773719]<0.
\]
Therefore
\[
\boxed{W_5(0)<0}.
\]
Numerically the product is approximately
\[
W_5(0)\approx-1.21864127527923\times10^{14}.
\]

## 4. Analytic tail bound

For \(n\ge5\), use \(3<\pi<22/7\) and
\[
e^{-\pi n^2}<e^{-3n^2}.
\]
Bounding the absolute polynomial coefficients in the five displayed \(p_k\)'s after substituting \(x\le(22/7)n^2\) gives the safe constants
\[
C_0<59,\quad C_2<6800,\quad C_4<1.2\times10^6,
\quad C_6<2.9\times10^8,\quad C_8<8.9\times10^{10},
\]
so
\[
|p_k(\pi n^2)e^{-\pi n^2}|
\le C_k n^{20}e^{-3n^2}.
\]
For \(n\ge5\), the function \(x^{20}e^{-3x^2}\) is decreasing, and
\[
\sum_{n=5}^{\infty}n^{20}e^{-3n^2}
\le 5^{20}e^{-75}+\int_5^\infty x^{20}e^{-3x^2}\,dx
<2.66\times10^{-19}.
\]
Thus the omitted tails in \(a_0,a_2,a_4,a_6,a_8\) are bounded respectively by
\[
1.57\times10^{-17},\quad1.81\times10^{-15},\quad3.20\times10^{-13},
\quad7.72\times10^{-11},\quad2.37\times10^{-8},
\]
which are tiny relative to the determinant margins above.

## 5. Closure consequence

Hence the exact Riemann-Jacobi kernel \(\Phi\) is **not PF5 as a translation kernel**. In particular it is not PF∞. Therefore the following proof architecture is permanently blocked for this fixed kernel:

\[
\Phi\text{ PF}_\infty
\Longrightarrow \text{Fourier/cosine transform hyperbolicity}
\Longrightarrow \Xi\in\mathrm{LP}
\Longrightarrow \mathrm{RH}.
\]

This is a route no-go, not a disproof of RH.

## 6. New surviving target

Any total-positivity approach must therefore modify at least one structural ingredient:

1. use a **non-translation** theta kernel;
2. insert the factorial/cosine transform before taking minors and prove positivity of a different kernel;
3. use a Riemann-specific modular operator whose positive kernel is not \(\Phi(x-y)\);
4. or abandon PF∞ and close the global Pick/Weyl or nonlinear \(\tau\)-Hankel theorem directly.

This strengthens the current closure map by removing the fixed-kernel PF∞ route rather than repeatedly testing finite Jensen or raw-moment positivity.

## Status

**PROVED:** local PF5 obstruction at \(u=0\), with explicit derivative recurrence and analytic tail control.

**OPEN:** theta-specific global Pick/Weyl factorization; nonlinear theta\(\to\tau\) total positivity; a modified non-translation TP∞ mechanism; RH.
