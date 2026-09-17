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
The theorem-level criterion is \(\lambda_n\ge0\) for every \(n\ge1\) iff RH. Hence all-degree Li positivity is not an auxiliary lemma: it is itself the decisive RH target. Bombieri–Lagarias also connect this criterion to Weil positivity. citeturn1search0turn1search1

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
Bombieri–Lagarias explicitly relate Li positivity to the Guinand–Weil explicit formula and Weil's positivity criterion. citeturn1search0 For an admissible even test function \(h\), with Fourier transform \(g\), the explicit formula has the standard zeros/primes/archimedean form
\[
\sum_\gamma h(\gamma)=2h(i/2)-g(0)\log\pi
+\frac1{2\pi}\int_{-\infty}^{\infty}h(r)\frac{\Gamma'}{\Gamma}\!\left(\frac14+\frac{ir}{2}\right)dr
-2\sum_{m\ge1}\frac{\Lambda(m)}{\sqrt m}g(\log m),
\]
under the usual admissibility hypotheses. The proof-bearing target is an exact PSD/Gram factorization of the resulting quadratic functional, derived from arithmetic/theta data rather than assumed RH.

## Nyman–Beurling attack
Let \(\rho(x)=x-\lfloor x\rfloor\), and use the integer-dilation family
\[
\rho_a(x)=\rho\!\left(\frac1{ax}\right),\qquad a\in\mathbb N.
\]
Báez-Duarte proved that RH is equivalent to \(\chi_{(0,1)}\) lying in the \(L^2(0,\infty)\)-closure of the span of these integer dilates. citeturn1academia24turn1academia25

For every finite \(N\), define the exact Gram matrix and target vector
\[
G_N=(\langle\rho_a,\rho_b\rangle)_{1\le a,b\le N},\qquad
q_N=(\langle\chi,\rho_a\rangle)_{1\le a\le N}.
\]
The orthogonal projection coefficients are characterized exactly by the normal equations
\[
G_Nc_N=q_N,
\]
and the minimum squared error is
\[
\boxed{d_N^2=\|\chi\|_2^2-q_N^*G_N^{\dagger}q_N=1-q_N^*G_N^{\dagger}q_N,}
\]
where \(G_N^{\dagger}\) is the Moore–Penrose inverse (ordinary inverse when the finite family is independent). This is an unconditional exact finite-dimensional reduction. It does **not** imply \(d_N\to0\).

### Explicit finite approximant benchmark
Báez-Duarte's second-version result gives the concrete Möbius-weighted candidate
\[
\boxed{G_N^{(c)}(x)=-\sum_{a=1}^{N}\mu(a)e^{-c\log a/\log\log N}\rho_a(x)}
\]
for some \(c>0\), and proves that **assuming RH** its distance from \(\chi_{(0,1)}\) is of order
\[
\boxed{\|\chi-G_N^{(c)}\|_2=O\!\big((\log\log N)^{-1/3}\big).}
\]
This is an explicit vanishing-error construction, but its theorem is conditional on RH, exactly as stated in Báez-Duarte's paper. citeturn3academia22

For comparison, the broader Nyman–Beurling–Báez-Duarte distance can be written on the Mellin side as
\[
d_N^2=\inf_{A_N}\frac1{2\pi}\int_{-\infty}^{\infty}\left|1-\zeta\!\left(\frac12+it\right)A_N\!\left(\frac12+it\right)\right|^2\frac{dt}{\frac14+t^2},
\]
where \(A_N(s)=\sum_{n\le N}a_n n^{-s}\). Burnol's unconditional lower bound is
\[
\liminf_{N\to\infty}d_N^2\log N\ge
\sum_{\Re\rho=1/2}\frac{m(\rho)^2}{|\rho|^2},
\]
so existing unconditional results constrain the possible rate from below rather than forcing convergence to zero. citeturn3search23

## Exact independent wall
The two requested attacks now reduce to two sharply stated, non-circular missing inequalities:

1. **Li/Weil:** derive an exact representation \(\lambda_n=A_n+R_n\) with \(A_n\ge0\) and \(R_n\ge0\) for every \(n\), using only arithmetic/theta/explicit-formula data. The current exact decomposition has an uncontrolled signed \(\eta\)-remainder.
2. **Nyman–Beurling:** prove an unconditional explicit coefficient sequence \(c_{a,N}\) with \(\|\chi-\sum_{a\le N}c_{a,N}\rho_a\|_2\le E_N\) and \(E_N\to0\). The known Möbius construction has the desired vanishing rate only under RH.

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
3. For Nyman–Beurling, compute/derive exact Gram entries and the projection identity above; then identify an unconditional analytic estimate that forces \(q_N^*G_N^{\dagger}q_N\to1\).
4. Cross-check any proposed mechanism against both Li positivity and Nyman–Beurling density.

## Decision rule
Any unproved positivity/density statement equivalent to RH remains `open` or `critical_obstruction`; RH is not declared proved unless every bridge is unconditional and complete.
