# RH research pivot: Li–Weil–Nyman–Beurling

## Status
A rigorous change of attack after the theta/Laguerre Jensen route reached an unresolved all-degree hyperbolicity wall. No step here assumes RH. The two requested proof-bearing attacks were pushed to their exact current mathematical frontier: an exact zero-free Li arithmetic decomposition was derived, and an explicit Nyman–Beurling finite approximant with a known **conditional** vanishing-error estimate was identified. Neither currently supplies an unconditional RH proof.

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
\lambda_1=1+\frac\gamma2-\log(2\sqrt\pi)=0.0230957089661210338\ldots>0,
\]
an unconditional finite case only.

## Proof-bearing Li attack: exact arithmetic decomposition
Introduce the Laurent coefficients \(\eta_m\) by
\[
-\frac{\zeta'(1+w)}{\zeta(1+w)}=\frac1w+\sum_{m\ge0}\eta_m w^m.
\]
Then the Li coefficients admit the exact zero-free arithmetic formula
\[
\boxed{\lambda_n=
1-\frac n2(\log(4\pi)+\gamma)
+\sum_{j=2}^{n}(-1)^j\binom nj(1-2^{-j})\zeta(j)
-\sum_{j=1}^{n}\binom nj\eta_{j-1}.}
\]
This follows by inserting \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) into the derivative definition and expanding at \(s=1\). It contains no zeros and no RH assumption.

This is a genuine decomposition, but **not yet a positive decomposition**. The zeta/gamma trend part has no coefficientwise positivity theorem strong enough to dominate the \(\eta\)-remainder for every \(n\). The exact remaining obstruction is therefore
\[
\boxed{\text{prove a sign-bearing bound for the full }\eta\text{-remainder, or replace it by an exact PSD/Gram representation.}}
\]
Known asymptotics distinguish RH-compatible growth from the non-RH oscillatory regime, but do not prove the sign for every \(n\).

## Li → Weil translation
Bombieri–Lagarias establish that Li positivity is a special case of Weil positivity. For an admissible even test function \(h\), with Fourier transform \(g\), the explicit formula has the form
\[
\sum_\gamma h(\gamma)=2h(i/2)-g(0)\log\pi
+\frac1{2\pi}\int_{-\infty}^{\infty}h(r)\frac{\Gamma'}{\Gamma}\!\left(\frac14+\frac{ir}{2}\right)dr
-2\sum_{m\ge1}\frac{\Lambda(m)}{\sqrt m}g(\log m),
\]
under the standard admissibility hypotheses. Weil's criterion says RH is equivalent to nonnegativity on the appropriate factorized/positive-type test functions. Thus the next exact target is an arithmetic Gram factorization of this quadratic functional, not merely positivity checked on finitely many test functions.

## Nyman–Beurling attack
Let \(\rho(x)=x-\lfloor x\rfloor\), and use the integer-dilation family
\[
\rho_a(x)=\rho\!\left(\frac1{ax}\right),\qquad a\in\mathbb N.
\]
Báez-Duarte's strengthening gives
\[
\mathrm{RH}\iff \chi_{(0,1)}\in\overline{\operatorname{span}\{\rho_a:a\in\mathbb N\}}^{L^2(0,\infty)}.
\]
Hence an explicit sequence \(G_N=\sum_{a\le N}c_{a,N}\rho_a\) with \(\|\chi-G_N\|_2\to0\) would itself prove RH.

### Explicit finite approximant benchmark
Báez-Duarte's smoothing framework provides concrete Möbius-weighted candidates of the form
\[
G_N^{(\varepsilon)}(x)=-\sum_{a=1}^{N}\frac{\mu(a)}{a^{\varepsilon}}\rho_a(x),
\qquad \varepsilon>0,
\]
with an explicit Fourier–Mellin error decomposition. In particular, the exact norm splits into a truncation term measuring the difference between the finite Möbius sum and \(1/\xi\), plus a shift term measuring \(\xi(z)/\xi(z+\varepsilon)-1\). Báez-Duarte's analysis shows that suitable choices such as \(\varepsilon_N\asymp1/\log\log N\) yield vanishing error **under RH**. The available estimate is therefore a benchmark, not an unconditional proof. citeturn0search23

The unconditional finite-dimensional quantity is
\[
d_N:=\inf_{c_1,\dots,c_N}\left\|\chi_{(0,1)}-\sum_{a=1}^N c_a\rho_a\right\|_2,
\]
with \(d_N\downarrow d\), and the criterion gives \(d=0\iff\mathrm{RH}\). Known unconditional work instead supplies lower bounds; for example Burnol's refinement gives a liminf lower bound involving the multiplicities of zeros on the critical line. Thus the difficult direction is still an unconditional upper bound forcing \(d_N\to0\). citeturn0search0

## Exact independent wall
The two requested attacks now reduce to two sharply stated, non-circular missing inequalities:

1. **Li/Weil:** derive an exact representation \(\lambda_n=A_n+R_n\) with \(A_n\ge0\) and \(R_n\ge0\) for every \(n\), using only arithmetic/theta/explicit-formula data. The current exact decomposition has an uncontrolled signed \(\eta\)-remainder.
2. **Nyman–Beurling:** prove an unconditional explicit coefficient sequence \(c_{a,N}\) with \(\|\chi-\sum_{a\le N}c_{a,N}\rho_a\|_2\le E_N\) and \(E_N\to0\). The Möbius constructions currently available do not supply this independently of RH.

These are not merely computational gaps: each missing statement is strong enough to imply RH. Any derivation that obtains either bound by assuming the corresponding RH-equivalent property is circular.

## Non-circularity rules
- Do not assume RH or that all Xi zeros are real.
- Do not assume a self-adjoint Hilbert–Pólya operator without constructing and verifying it.
- Finite-degree positivity, numerical zeros, and asymptotics are evidence only, never an all-degree theorem.
- Every positivity decomposition must be exact on its full domain.
- Failed identities must retain their exact residual/obstruction.
- If a proposed lemma is RH-equivalent, label it as the main target rather than an established supporting lemma.

## Immediate execution order
1. Isolate the exact \(\eta\)-remainder in the Li arithmetic formula and test whether it admits a positive integral/Gram transform.
2. Construct the corresponding Weil quadratic form and seek an exact PSD factorization of its prime + gamma + archimedean side.
3. For Nyman–Beurling, derive exact Gram matrices and norm identities for the Möbius-weighted candidate; identify precisely which estimate would make the error bound unconditional.
4. Cross-check any proposed mechanism against both Li positivity and Nyman–Beurling density.

## Decision rule
Any unproved positivity/density statement equivalent to RH remains `open` or `critical_obstruction`; RH is not declared proved unless every bridge is unconditional and complete.
