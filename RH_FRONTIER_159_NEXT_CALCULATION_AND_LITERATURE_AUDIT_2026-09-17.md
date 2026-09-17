# RH Frontier 159 — Next Calculation and Literature Audit — 2026-09-17

## 1. Exact correction to Frontier 155
For
\[
H(z)=4\sum_{k\ge0}\frac{M_{2k}}{(2k)!}z^k,
\qquad M_r=\int_0^\infty u^r\Phi(u)\,du,
\]
we have
\[
h_0=4M_0,\quad h_1=2M_2,\quad h_2=\frac23M_4.
\]
Therefore
\[
h_0h_2-h_1^2=\frac43M_0M_4-4M_2^2
=\frac43(M_0M_4-3M_2^2).
\]
Ordinary Cauchy–Schwarz only gives \(M_0M_4\ge M_2^2\), so it does NOT determine the sign of \(M_0M_4-3M_2^2\). The previous Cauchy-based sign obstruction was therefore invalid and is withdrawn.

## 2. Direct numerical diagnostic from the exact xi function
Using the standard completed xi function and \(H(z)=\Xi(\sqrt z)\), high-precision differentiation gives approximately
\[
h_0=0.4971207781883141,
\]
\[
h_1=0.01148597215757272,
\quad h_2=2.469040361406360\times10^{-4},
\quad h_3=4.994132888313162\times10^{-6}.
\]
Hence
\[
\Delta_2=M_0M_4-3M_2^2
\propto h_0h_2-h_1^2
\approx-9.18642982046709\times10^{-6}<0,
\]
so the first logarithmic-derivative coefficient is
\[
c_1=m'(0)\approx-3.71725992852697\times10^{-5}.
\]
The next coefficient is
\[
c_2=m''(0)\approx2.88347862801947\times10^{-7}>0.
\]
The next two are approximately
\[
c_3\approx-3.97819008151795\times10^{-9},\qquad
c_4\approx7.71279396147984\times10^{-11}.
\]
Thus the local coefficients are consistent with the alternating derivative pattern expected of a Stieltjes-type function, but this is numerical evidence only.

## 3. Third nonlinear invariant
The exact numerator for \(m''(0)\) is
\[
N_3=h_0^2h_3-3h_0h_1h_2+2h_1^3.
\]
In theta moments,
\[
N_3=\frac49\left(M_0^2M_6-9M_0M_2M_4+12M_2^3\right).
\]
Numerically the bracket is approximately
\[
\Delta_3=6.72977982003486\times10^{-6}>0.
\]
The next task is to derive \(\Delta_2,\Delta_3\), and higher \(\Delta_n\) directly from the explicit theta lattice, not from zero locations.

## 4. Stronger algebraic target
Generate \(c_n=m^{(n)}(0)\) from
\[
h_{n+1}=\sum_{k=0}^n\binom nk c_kh_{n-k}.
\]
Then construct the factorial Hankel matrices
\[
K_N(0)=\left[\frac{(-1)^{i+j}c_{i+j}}{(i+j)!}\right]_{i,j=0}^N.
\]
If an independently theta-derived subtraction \(E'\) is necessary, replace \(c_n\) by derivatives of \(R=m-E'\). The proof target is an exact all-order Gram/SOS factorization of \(K_N\), not finite numerical PSD.

## 5. Literature audit
SciSpace returned several repository-indexed papers claiming unconditional RH proofs. Their abstracts are not sufficient evidence of correctness. More useful unconditional results include work on Jensen-polynomial hyperbolicity and Nyman–Beurling/Báez-Duarte coercivity, but these leave a nontrivial bridge condition unresolved. In particular, conditional logarithmic-potential operator frameworks explicitly state that existence of the natural Weyl realization is not established unconditionally. Repository claims of complete Hilbert–Pólya proofs must therefore be independently checked at the operator construction and determinant-identification steps.

## 6. Current status
The RH first arrow remains OPEN. Frontier 155's Cauchy-Schwarz obstruction is corrected: no contradiction follows from ordinary moment positivity. The new evidence instead motivates a sharper question: whether the theta-specific moment sequence satisfies the stronger cumulant/Hankel inequalities needed for a genuine Stieltjes or Pick representation.

## 7. Immediate next proof-bearing calculations
1. Derive exact theta-lattice formulae for \(\Delta_2\) and \(\Delta_3\), preferably as finite sums/integrals of manifestly signed or squared expressions.
2. Compute \(K_2,K_3,K_4\) symbolically from the recurrence and factor their determinants.
3. Search for a theta-specific Vandermonde/Binet–Cauchy representation of these determinants.
4. Derive the only admissible entire subtraction \(E'\) from the large-positive-real-axis asymptotic of \(H'/H\), then retest complete monotonicity of the residual.
5. In parallel, attempt a theta-defined positive Jacobi matrix whose Weyl function equals the residual; determinant equality remains a separate theorem.
