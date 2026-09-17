# RH Frontier 139 — Exact Theta → tau Bridge and the Residual Recast

Date: 2026-09-17

## 1. Goal

The previous frontier proved positivity of the intrinsic theta moment Hankel matrices, but this is not yet positivity of the transformed-zero moments

`tau_n = sum_rho [-(rho-1/2)^(-2)]^(n+1)`.

The first task is therefore to derive the bridge exactly, without assuming RH.

## 2. Correct entire-function normalization

Let

`Xi(w) = xi(1/2+w)`

and define

`H(z) = Xi(sqrt(z))`,

where the evenness of Xi makes H a single-valued entire function of z.

The theta/Fourier representation has the form

`Xi(w) = 2 integral_0^infinity Phi(u) cos(w u) du`.

Hence

`H(z) = 2 integral_0^infinity Phi(u) cos(u sqrt(z)) du`.

This normalization is essential: if a zero of Xi is at `w=i gamma`, then its H-image is

`z=(i gamma)^2=-gamma^2`,

so RH is exactly the statement that all zeros of H lie on `(-infinity,0]`.

Expanding at z=0 gives

`H(z) = 2 sum_{k>=0} (-1)^k M_k z^k/(2k)!`,

where

`M_k = integral_0^infinity Phi(u)u^(2k)du`.

Thus the theta moments are the Taylor coefficients of H with the explicit alternating/factorial normalization.

## 3. Exact theta → tau bridge through the logarithmic derivative

Let `a_rho=rho-1/2`. Pairing the zeros `+a_rho` and `-a_rho` in the even canonical product gives factors

`1 + z/a_rho^2`.

After the standard genus-one polynomial normalization is separated, differentiation removes the polynomial ambiguity at sufficiently high order. The zero-dependent part of the logarithmic derivative is

`H'(z)/H(z) = A(z) + sum_rho 1/(z+a_rho^2)`

in the region of local convergence, with A an entire polynomial of degree at most the genus contribution.

For n large enough that the polynomial contribution vanishes (and in particular for the convergent power sums defining the present tau sequence),

`(H'/H)^(n)(0) = (-1)^n n! sum_rho a_rho^(-2n-2)`.

Since

`tau_n = sum_rho [-a_rho^(-2)]^(n+1) = (-1)^(n+1) sum_rho a_rho^(-2n-2)`,

we obtain

`boxed{ tau_n = -(1/n!) (d^n/dz^n)[H'(z)/H(z)]_{z=0} }`

for every n in the range where the genus polynomial has disappeared; for the present zeta zero sums this includes the RH-bearing tail. The low-index normalization must be handled separately rather than silently absorbed.

No zero location is assumed in this identity.

## 4. The crucial correction: tau is not the theta moment sequence

Let `m_k=H^(k)(0)`. Then

`H'/H=(log H)'`.

Hence tau is a sequence of logarithmic-derivative coefficients, i.e. cumulant-type polynomials in the theta Taylor data, not the raw moments themselves.

Because H is even in `sqrt(z)`, its z-expansion has alternating coefficients inherited from the cosine kernel. Writing `h_k=H^(k)(0)`, the first log-derivative coefficients are

`(H'/H)(0)=h_1/h_0`,

`(H'/H)'(0)=(h_0h_2-h_1^2)/h_0^2`,

`(H'/H)''(0)=(h_0^2h_3-3h_0h_1h_2+2h_1^3)/h_0^3`.

Therefore the corresponding tau values are exact cumulant polynomials with the signs dictated by the boxed derivative identity, subject to the low-index genus normalization just noted.

This identifies the previous residual wall precisely: it is not an unknown additive error between two equal moment sequences. It is the nonlinear logarithmic/cumulant transform

`{M_k} -> {tau_k}`

induced by taking `log H`.

## 5. Four-index consequence

The positive theta determinant

`det(M_{i+j})_{0<=i,j<=3} >= 0`

does not directly control

`det(tau_{i+j})_{0<=i,j<=3}`.

The latter is a determinant of nonlinear cumulant polynomials in the theta Taylor data. Therefore the naive identity

`det(tau_{i+j}) = Theta_4 + R_4`

is not canonical until the exact logarithmic transform and all normalization terms are inserted.

The correct proof target is now either:

(A) prove that the theta-generated H belongs to the Laguerre–Pólya class by an RH-independent total-positivity theorem, which would force all zeros of H to be real and hence RH;

(B) prove directly that `F=H'/H` is a Stieltjes/Pick function with poles on the negative real axis; or

(C) prove an all-order sign theorem for the logarithmic-derivative/cumulant sequence strong enough to imply that every zero of H lies on the negative real axis.

## 6. New route: Stieltjes inversion from theta data

If one can prove

`F(z)=H'(z)/H(z) = a + integral_0^infinity dnu(t)/(z+t)`

with `a>=0` and `nu>=0`, then every pole of F is on `(-infinity,0]`. Since poles of F are zeros of H, this gives RH.

Equivalently, the key analytic target is the Pick sign

`Im z>0 => Im F(z)<=0`,

plus analyticity/growth conditions sufficient for the Stieltjes representation.

## 7. Direct theta expression for the Pick numerator

Set `q=sqrt(z)` on a consistent branch. Then

`H(z)=2 integral Phi(u) cos(u q) du`,

`H'(z)= - integral Phi(u) u sin(u q)/q du`.

Therefore

`Im F(z) = Im(H'(z) overline(H(z)))/|H(z)|^2`.

The numerator is the exact double integral

`Im(H'(z) overline(H(z))) = -2 Im integral integral Phi(u)Phi(v) [u sin(q u) cos(overline(q)v)/q] du dv`.

After antisymmetrization one obtains a two-variable kernel analogous to Frontier 137. Its pointwise sign is not available from positivity of Phi alone, so any successful Pick proof must use a global modular pairing, spectral representation, or another nonlocal identity.

## 8. What is genuinely closed here

PROVED/STRUCTURALLY IDENTIFIED:

1. The correct theta-generated entire function for the zero-location problem is `H(z)=Xi(sqrt(z))`, not `Xi(i sqrt(z))`.
2. The theta moments are its Taylor coefficients with explicit alternating/factorial normalization.
3. The transformed-zero moments arise from the higher logarithmic-derivative coefficients of H, with the exact sign relation above after the canonical-product normalization is accounted for.
4. The earlier theta-vs-tau residual is therefore a nonlinear logarithmic/cumulant transform, not an arbitrary unknown additive error.
5. The four-index theta determinant remains positive, but it cannot be substituted for the tau determinant.

OPEN:

1. An RH-independent theorem converting the theta Taylor structure into real-negative zeros of H.
2. The global Pick/Stieltjes inequality.
3. An all-order total-positivity/Laguerre–Pólya theorem for the Riemann theta kernel.
4. RH itself.

## 9. Adversarial conclusion

The exact normalization correction is important: zeros `rho=1/2+i gamma` map to `z=-gamma^2`. Any future proof using `H=Xi(i sqrt(z))` as the Stieltjes zero-location variable has the sign reversed and must be corrected.

No RH proof is claimed at this frontier. Any future argument that simply identifies `M_k` with `tau_k`, or assumes the cumulant residual is positive, is invalid until proved.