# RH Master Next-Steps — Parallel Proof Program

Date: 2026-09-17

## Current theorem boundary

Frontier 135 closes the Hamburger–Cauchy rigidity implication conditional on all-order Hankel positivity:

\[
H_N=(\tau_{i+j})_{0\le i,j\le N}\succeq0\ \forall N
\quad\Longrightarrow\quad
v_\rho=-(\rho-1/2)^{-2}>0
\quad\Longrightarrow\quad
\Re\rho=1/2.
\]

Combined with the converse under RH, the target reduction is

\[
\boxed{\mathrm{RH}\iff H_N\succeq0\quad\forall N.}
\]

This is a reduction, not a completed proof. The only proof-bearing wall is now an unconditional derivation of all-order Hankel PSD from Riemann's completed function/theta kernel (or an independent theorem implying it).

## Parallel workstreams

### W1 — Exact zero-location-free formula for tau_n

Define
\[
G(z)=\frac{\Xi(\sqrt z)}{\Xi(0)}.
\]
Using the Hadamard product in the symmetric variable,
\[
\log G(z)=\sum_{k\ge1}\frac{(-1)^{k+1}}k\tau_{k-1}z^k,
\]
inside its convergence disk. Derive every \(\tau_n\) directly from derivatives/Taylor coefficients of \(\Xi(\sqrt z)\), with all convergence and normalization constants explicit and no zero locations assumed.

**Gate:** an exact coefficient extraction theorem that can be used as input to positivity arguments.

### W2 — Direct Hankel quadratic-form attack

For arbitrary \(N\) and \(c=(c_0,\ldots,c_N)\), attack
\[
Q_N(c)=\sum_{i,j=0}^Nc_ic_j\tau_{i+j}.
\]
Rewrite it using W1 as a functional of the completed theta kernel, not as a positive sum over zeros. Seek
\[
Q_N(c)=\int \!|P_{N,c}(u)|^2\,d\mu(u)
\]
or a finite sum/integral of squares after Poisson/Jacobi transformation.

**Gate:** exact nonnegative Gram representation for every N.

### W3 — Multi-copy theta/Vandermonde mechanism

Continue Frontier 109's obstruction-aware route. For degree d=3 explicitly expand the Hermite/Newton form into 2-, 3-, and higher-copy theta integrals. Test whether antisymmetrisation gives exact Vandermonde squares
\[
\prod_{i<j}(u_i-u_j)^2
\]
with a nonnegative residual. Then generalize from d=3 to arbitrary d.

**Gate:** degree-3 exact positive factorisation, followed by a degree-uniform theorem.

### W4 — Stieltjes/J-fraction route

Treat
\[
F(z)=\sum_{n\ge0}\tau_nz^n
\]
as a formal moment generating function. Determine whether unconditional theta identities imply a Stieltjes continued fraction with nonnegative Jacobi parameters. Prove equivalence between those parameters and all Hankel determinants.

**Gate:** every principal Hankel determinant \(\Delta_N=\det(\tau_{i+j})_{0\le i,j\le N}\ge0\) from explicit theta quantities.

### W5 — Laguerre–Pólya/Jensen route

Derive the exact Jensen-polynomial criterion from the same theta coefficient data. Do not infer real-rootedness from positive theta moments alone. Establish an all-degree hyperbolicity theorem directly or show that W2/W3 implies it.

**Gate:** hyperbolicity of every Jensen polynomial without assuming RH.

### W6 — de Branges / canonical-system route

Use the intrinsic completed Xi function and construct a canonical/de Branges kernel whose positivity is proved directly from the theta kernel. Any Hermite–Biehler assertion must be established independently, not inferred from RH. Identify precisely whether the remaining issue is positivity of a kernel, self-adjointness, or zero correspondence.

**Gate:** a self-adjoint spectral realization whose spectrum forces zeros onto the critical line.

### W7 — de Bruijn–Newman heat-flow route

Translate the theta kernel to the de Bruijn–Newman family. Track exactly which theorem would be needed to prove the relevant zero-free/real-rooted state at a finite parameter and propagate it to the Xi parameter. Do not use numerical evidence as proof of the sign of the Newman constant.

**Gate:** a rigorous parameter inequality implying \(\Lambda\le0\) (equivalently the required real-zero state at the Xi parameter), or an exact replacement theorem.

### W8 — Adversarial/counterexample audit

For every proposed positivity identity, test: (i) finite truncation versus infinite sum, (ii) interchange of sum/integral, (iii) hidden RH assumptions, (iv) complex conjugation that presupposes real nodes, (v) sign of the residual, (vi) boundary accumulation at zero, (vii) normalization/factorial errors, and (viii) whether a finite-degree result is being promoted to all degree.

**Gate:** every claimed lemma has explicit hypotheses and no circular dependence on zero locations.

### W9 — Independent equivalent criteria

In parallel, derive exact implications/relations among: all-order Hankel PSD, hyperbolicity of Jensen polynomials, Li coefficients, total positivity/PF-infinity properties, and spectral/Herglotz representations. The purpose is not to combine equivalent conjectures into a proof, but to identify the representation in which an unconditional sign mechanism is actually accessible.

**Gate:** a dependency graph showing which statement is genuinely stronger, equivalent, or merely necessary.

### W10 — Computational theorem-discovery layer

Compute exact/high-precision values of the first Hankel determinants, Jensen discriminants, theta integrals, and candidate Gram residuals for increasing N and d. Use this only to discover identities or falsify proposed certificates. Every numerical observation must be converted into an exact symbolic lemma before entering the proof chain.

**Gate:** candidate identities with symbolic verification, not numerical-only evidence.

## Proof assembly order

1. Finish W1 exactly.
2. Attack W2 and W3 simultaneously; W3 supplies explicit finite-degree structure for W2.
3. In parallel run W4 and W5 as algebraic diagnostics; if either yields an unconditional positivity theorem, route directly to Frontier 135.
4. Run W6 and W7 as independent escape routes rather than assuming the theta-Gram route must work.
5. Run W8 continuously; no lemma is accepted without the adversarial audit.
6. Use W9 to collapse duplicate routes and identify the shortest genuinely new theorem.
7. Use W10 only for discovery/falsification.
8. Final assembly requires a single chain with no conditional step left:
\[
\text{theta/explicit formula}
\Rightarrow H_N\succeq0\ \forall N
\Rightarrow \text{positive Hamburger measure}
\Rightarrow \text{Cauchy rigidity}
\Rightarrow v_\rho>0
\Rightarrow \Re\rho=1/2.
\]

## Absolute completion gate

The project may state "RH proved" only after an unconditional proof of the boxed all-order Hankel positivity (or an independently complete theorem with an equally rigorous zero-location conclusion) is written with all analytic continuation, convergence, limiting, and positivity steps proved. Finite computation, numerical zeros, a positive theta kernel, or a conditional equivalence do not pass this gate.
