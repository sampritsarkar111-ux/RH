# Frontier 175 — Parallel Closure Matrix

| Route | Exact sufficient gate | Current state |
|---|---|---|
| Theta → Stieltjes/Pick | Explicit positive Stieltjes measure for the nonlinear Xi logarithmic derivative | OPEN |
| Factorial Hankel / tau | All-order Gram/SOS identity, not finite numerical PSD | OPEN |
| Jensen/Hermite | Arbitrary-degree nonnegative Jensen polynomials derived from theta structure | OPEN |
| de Branges | Explicit Hermite–Biehler/canonical-system construction whose determinant is Xi | OPEN |
| Li/Weil | Universal positive quadratic-form/SOS representation for every test function | OPEN |
| de Bruijn–Newman | Exact proof that the relevant endpoint has the required rigidity/sign | OPEN |
| Nyman–Beurling / Báez-Duarte | Global coercivity/density estimate equivalent to RH | OPEN |

## New unifying principle

Do not seek seven unrelated miracles. Seek one zero-independent positivity certificate that has several projections:
\[
\boxed{\text{theta data}\;\Longrightarrow\;\text{positive measure / positive operator}\;\Longrightarrow\;\text{all-order positivity}\;\Longrightarrow\;\text{RH}.}
\]

The certificate must be constructed before inserting any assumed zero locations. If a proof uses \(\rho=1/2+i\gamma\) at an intermediate step, it is circular unless that representation has already been derived from an independent theorem.

## Immediate algebraic stress test

Symmetry alone is insufficient. The function
\[
f(s)=(s-1/2)^2-1
\]
satisfies \(f(1-s)=f(s)\) and is real on the critical line but has off-line zeros. Therefore any symmetry-based spectral proof must add a genuine positivity/self-adjointness/determinant condition.

Likewise, positive raw theta moments do not automatically imply positive logarithmic-cumulant Hankel matrices. The nonlinear map \(H\mapsto-H'/H\) is the critical obstruction.

## Finish line

The project can honestly be called a proof only after one of the sufficient gates is proved with all analytic continuation, convergence, boundary behavior, and zero correspondence justified. Until then, computational confirmation remains diagnostic.