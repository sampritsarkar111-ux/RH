# RH research pivot: Li–Weil–Nyman–Beurling

## Status
A rigorous change of attack after the theta/Laguerre Jensen route reached an unresolved all-degree hyperbolicity wall. No step here assumes RH.

## Established Li identities
For the completed xi-function, Li's coefficients have the exact equivalent forms
\[
\lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right]
\]
with the standard symmetric interpretation over nontrivial zeros, and
\[
\lambda_n=\frac1{(n-1)!}\left.\frac{d^n}{ds^n}\left[s^{n-1}\log\xi(s)\right]\right|_{s=1},\qquad n\ge1.
\]
The theorem-level criterion is \(\lambda_n\ge0\) for every \(n\ge1\) iff RH. Hence all-degree Li positivity is not an auxiliary lemma: it is itself the decisive RH target.

For the first coefficient,
\[
\lambda_1=1+\frac\gamma2-\log(2\sqrt\pi)>0,
\]
an unconditional finite case only.

## Current Li obstruction
The zero-free derivative formula is exact but does not expose coefficientwise positivity. Known asymptotics distinguish the RH-compatible growth from the non-RH oscillatory regime, but do not prove the sign for every \(n\). The proof-bearing target is therefore an exact positive representation derived from prime/gamma/theta data, not a restatement of \(\lambda_n\ge0\).

## Three-route program
1. **Li coefficients:** derive an explicit zero-free representation and search for a manifestly nonnegative decomposition valid for every \(n\).
2. **Weil positivity:** derive the explicit-formula quadratic form and seek an exact PSD/Gram representation on the full admissible test-function class.
3. **Nyman–Beurling:** construct admissible finite approximants with rigorously proved \(L^2\)-error tending to zero.

## Weil route
For an admissible even test function, Weil's explicit formula gives a zeros/primes duality. RH is equivalent to the corresponding positivity criterion on functions of factorized form. The next proof-bearing target is an exact Gram/SOS factorization derived from the explicit formula itself, without inserting RH.

## Nyman–Beurling route
Let \(\rho(x)=x-\lfloor x\rfloor\) and \(\rho_a(x)=\rho(1/(ax))\). The Nyman–Beurling criterion identifies RH with the closure of the span of these functions containing the target \(\chi_{(0,1)}\); Baez-Duarte proved that integer dilations suffice. This is an exact reformulation, not a proof. The target is a constructive sequence with a rigorous norm bound tending to zero.

## Non-circularity rules
- Do not assume RH or that all Xi zeros are real.
- Do not assume a self-adjoint Hilbert–Polya operator without constructing and verifying it.
- Finite-degree positivity, numerical zeros, and asymptotics are evidence only, never an all-degree theorem.
- Every positivity decomposition must be exact on its full domain.
- Failed identities must retain their exact residual/obstruction.
- If a proposed lemma is RH-equivalent, label it as the main target rather than an established supporting lemma.

## Immediate execution order
1. Derive the Li identities and isolate the exact sign-bearing remainder.
2. Translate Li functionals into Weil quadratic forms and test for a theta/prime Gram factorization.
3. Derive exact finite-N Nyman–Beurling norm formulas for candidate approximants.
4. Cross-check any successful positivity mechanism against the other routes.

## Decision rule
Any unproved positivity/density statement equivalent to RH remains `open` or `critical_obstruction`; RH is not declared proved unless every bridge is unconditional and complete.
