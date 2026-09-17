# Frontier 112 — All-route RH closure execution matrix

Date: 2026-09-17

## Objective

Run the remaining proof-bearing routes in parallel, but require every route to terminate in an explicit theorem implying that every zero of the completed Xi function is real. This is a research execution matrix, not a claim that RH has been solved.

## Route A — Pick/Herglotz

Target: construct an exact theta-derived meromorphic logarithmic derivative with a genuine Herglotz/Pick representation whose representing measure is supported on the real axis.

Required closure:

\[
\operatorname{Im}z>0\Rightarrow\operatorname{Im}M(z)\ge0
\]

plus the pole theorem identifying poles of \(M\) with zeros of \(\Xi\).

Failure test: exhibit an exact kernel minor that is negative. Numerical tests are not closure or refutation.

## Route B — Jensen/Hermite

Target: prove hyperbolicity of \(J_{d,n}\) for every \(d,n\).

Immediate checkpoint: d=3 discriminant and all Hermite principal minors, followed by a degree-uniform construction.

Required closure:

\[
\forall d,n,\quad J_{d,n}\text{ hyperbolic}
\]

with the theorem connecting this all-degree property to the Laguerre-Pólya/RH criterion.

## Route C — de Branges

Target: construct a genuine canonical system or de Branges space from theta data and prove that the zero set of the resulting spectral determinant is exactly the zero set of \(\Xi\).

Required closure:

\[
\text{self-adjoint spectrum}\;=\;\{z:\Xi(z)=0\}.
\]

The spectral object must be defined without the unknown zeros.

## Route D — Li/Weil

Target: derive universal positivity from theta/arithmetic data.

Required closure:

\[
Q_\theta(g)\ge0\quad\forall g
\]

for the exact Weil test class, or an equivalent all-order Li positivity theorem, together with the precise equivalence to RH.

## Route E — de Bruijn–Newman

Target: obtain a zero-independent theorem forcing the deformation endpoint condition equivalent to RH.

Required closure: a rigorous endpoint inequality or rigidity identity, not merely numerical bounds for the constant.

## Cross-route bridge

Define one common positive form only after its domain and maps are explicit:

\[
Q_\theta(T_Pf,T_Pf)=Q_\theta(T_Gf,T_Gf)=Q_\theta(T_Lf,T_Lf)=Q_\theta(T_Sf,T_Sf)\ge0.
\]

Then identify which representation supplies the shortest zero-realness theorem.

## Execution invariant

At every checkpoint record exactly one of:

- PROVED — complete derivation and all analytic hypotheses checked;
- OBSTRUCTION — exact counterexample/minor disproves this ansatz;
- OPEN — algebraically reduced but not solved;
- NUMERICAL — evidence only, never promoted to proof.

## Final audit

No final RH statement is permitted until one route contains a complete implication

\[
\zeta(\rho)=0,\;0<\Re\rho<1
\Longrightarrow\Re\rho=\tfrac12
\]

with no assumed zero location and no unresolved convergence, multiplicity, continuation, or operator-spectrum identification gap.
