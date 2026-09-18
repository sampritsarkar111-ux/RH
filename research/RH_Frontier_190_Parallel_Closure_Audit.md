# RH Frontier 190 — Parallel Closure Attack and Hard-Gate Audit — 2026-09-18

## Status
This is an unconditional research audit, not a claimed proof of the Riemann Hypothesis. The objective is to close proof obligations, not to relabel evidence as a theorem.

## 1. Current hard gates
The surviving proof-bearing gates are:
1. Construct an unconditional analytic continuation/completion for the new MRDTS transform and prove it equals C(s) xi(s), with C(s) nonzero.
2. Derive the exact archimedean Gamma/pi contribution, not only the Euler/Möbius side.
3. Prove a dense-class identity from the MRDTS quadratic form to the Weil quadratic form.
4. Prove all-order Li positivity, or an equivalent theorem that implies it.
5. Prove the Nyman–Beurling density statement without assuming RH.
6. Construct an actual self-adjoint operator with a rigorous zero/spectrum correspondence; finite symmetric matrices are only diagnostics.
7. For the Jensen route, prove hyperbolicity for every degree and shift. Known results establish eventual hyperbolicity for each fixed degree, leaving the finite low-shift cases and, more fundamentally, the all-degree/all-shift theorem as the decisive gate.
8. For Pick/Stieltjes/Hankel routes, prove the global sign/positivity property in the whole required domain and show that it is equivalent to RH rather than merely implied by numerical samples.

## 2. MRDTS repair
The exact Möbius divisor channel is
\[
\boxed{M_d(s)=\sum_{n\ge1}\varepsilon_n(d)n^{-s}
=d^{-s}\sum_{q\ge1}\mu(q)q^{-s}
=\frac{d^{-s}}{\zeta(s)},\qquad \Re s>1.}
\]
This replaces the false Liouville identity. The Liouville series is instead \(\sum \lambda(n)n^{-s}=\zeta(2s)/\zeta(s)\).

## 3. New proof object: Arithmetic-to-Weil transfer operator
Define the target abstractly by
\[
\boxed{\mathcal Q_{\rm MR}(f)=\langle f,(I-\mathcal K_{\rm MR})f\rangle}
\]
on a dense test space, and require an exact identity
\[
\boxed{\mathcal Q_{\rm MR}(f)=\mathcal W_\xi(f)}
\]
where \(\mathcal W_\xi\) is the Weil quadratic form for the completed zeta function. The missing theorem is therefore not positivity of a finite matrix; it is equality of two infinite-dimensional quadratic forms with all convergence, continuation, and archimedean terms controlled.

## 4. Jensen attack
Pólya's equivalence gives:
\[
\boxed{\mathrm{RH}\iff J^{d,n}_\xi\text{ is hyperbolic for every }d\ge1,n\ge0.}
\]
Known work gives eventual hyperbolicity for each fixed degree. Therefore a finite computation cannot close RH. The mathematically meaningful next target is a uniform theorem in \(d,n\), with an explicit low-shift certificate and a remainder bound that is uniform in degree.

## 5. Spectral attack
The required implication is
\[
\boxed{\det_{\!F}(I-\mathcal K)=C(s)\xi(s),\quad \mathcal K=\mathcal K^*,\quad C(s)\ne0.}
\]
Self-adjointness alone is insufficient unless the determinant identity and the zero/spectrum correspondence are independently proved.

## 6. Anti-circularity rule
No proposed route is accepted if its positivity, self-adjointness, density, or determinant identity is obtained by assuming the location of zeta zeros, using an RH-equivalent statement as an input, or defining an operator from the unknown zero set.

## 7. Computational role
Numerical calculations may falsify candidate identities, certify finite truncations, and discover conjectural inequalities. They cannot replace an all-order or infinite-dimensional proof.

## 8. Closure result of this frontier
Closed:
- the Liouville/Möbius confusion is repaired;
- the reciprocal-zeta divisor channel is exact in Re(s)>1;
- the surviving proof gates are compressed into explicit analytic, quadratic-form, Jensen, and spectral obligations.

Not closed:
- global MRDTS-to-xi identity;
- Gamma/pi completion;
- MRDTS-to-Weil equality;
- unconditional all-order Li positivity;
- unconditional Nyman–Beurling density;
- genuine self-adjoint zero operator;
- all-degree/all-shift Jensen hyperbolicity.

## 9. Decision rule
A future result is marked **PROOF-CLOSING** only when every hypothesis is unconditional, every limit/interchange is justified, and the final implication to RH is explicit. Otherwise it is marked diagnostic, partial, or no-go.
