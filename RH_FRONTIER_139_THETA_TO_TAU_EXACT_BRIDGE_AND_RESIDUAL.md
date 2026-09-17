# RH Frontier 139 — Exact Theta → tau Bridge and the Residual Recast

Date: 2026-09-17

## 1. Goal

The previous frontier proved positivity of the intrinsic theta moment Hankel matrices, but this is not yet positivity of the transformed-zero moments

`tau_n = sum_rho [-(rho-1/2)^(-2)]^(n+1)`.

The first task is therefore to derive the bridge exactly, without assuming RH.

## 2. Exact entire-function normalization

Let

`Xi(w) = xi(1/2+w)`

and define the even entire function

`H(z) = Xi(i sqrt(z))`.

Because Xi is even in w, H is single-valued and entire in z. From the theta representation,

`H(z) = 2 integral_0^infinity Phi(u) cosh(u sqrt(z)) du`,

with the standard Riemann theta kernel Phi.

Expanding at z=0 gives

`H(z) = sum_{k>=0} h_k z^k`,

where

`h_k = 2/(2k)! integral_0^infinity Phi(u) u^(2k) du`.

Thus the intrinsic theta moments are exactly the Taylor coefficients of H up to the factorial normalization:

`h_k = 2 M_k/(2k)!`.

This is an exact theta-to-H bridge and is RH-independent.

## 3. Exact theta → tau bridge through the logarithmic derivative

Write `a_rho = rho-1/2`. Pairing the zeros of Xi at `+a_rho` and `-a_rho` gives the canonical product in z. Consequently, in a neighborhood of z=0,

`H'(z)/H(z) = C_0 + sum_rho 1/(z+a_rho^2)`

with the standard genus/convergence normalization absorbed into the analytic constant term. For derivatives of order n>=1 the polynomial normalization disappears, giving the exact identity

`(H'/H)^(n)(0) = (-1)^n n! sum_rho a_rho^(-2n-2)`.

Therefore, with

`tau_n = sum_rho [-(a_rho)^(-2)]^(n+1)`,

we obtain the exact bridge

`boxed{ tau_n = - (1/n!) (d^n/dz^n)[H'(z)/H(z)]_{z=0},  n>=1 }`.

For n=0 there is an additive normalization issue in H'/H; the RH-bearing sequence begins with n>=1.

No zero location is assumed in this identity.

## 4. The crucial correction: tau is not the theta moment sequence

Let `m_k = H^(k)(0)`. Then

`H'/H = (log H)'`.

Hence tau is a sequence of logarithmic-derivative coefficients, i.e. cumulant-type polynomials in the theta moments, not the raw moments themselves.

The first exact identities are

`tau_1 = -(m_0 m_2 - m_1^2)/(m_0^2)`;

`tau_2 = -(m_0^2 m_3 - 3 m_0 m_1 m_2 + 2 m_1^3)/(2 m_0^3)`;

`tau_3 = -(m_0^3 m_4 - 4 m_0^2 m_1 m_3 - 3 m_0^2 m_2^2 + 12 m_0 m_1^2 m_2 - 6 m_1^4)/(6 m_0^4)`.

The factorials depend on the chosen indexing convention; the invariant formula is the boxed logarithmic-derivative identity above.

This identifies the previous residual wall precisely: it is not an unknown additive error between two equal moment sequences. It is the nonlinear cumulant transform

`{M_k} -> {tau_k}`

induced by taking `log H`.

## 5. Four-index consequence

The positive theta determinant

`det(M_{i+j})_{0<=i,j<=3} >= 0`

does not directly control

`det(tau_{i+j})_{0<=i,j<=3}`.

The latter is a determinant of nonlinear cumulant polynomials in the former Taylor data. Therefore an identity of the naive form

`det(tau_{i+j}) = Theta_4 + R_4`

is not canonical until the exact cumulant transform is inserted.

The correct proof target is now either:

(A) prove that the theta-generated H belongs to the Laguerre–Pólya class by an RH-independent total-positivity theorem, which would force all zeros of H to be real and hence RH;

(B) prove directly that `F=H'/H` is a Stieltjes/Pick function; or

(C) prove an all-order sign theorem for the cumulant sequence of H strong enough to imply that every zero of H lies on the negative real axis.

## 6. New route: Stieltjes inversion from theta data

If one can prove

`F(z)=H'(z)/H(z) = a + integral_0^infinity dnu(t)/(z+t)`

with `a>=0` and `nu>=0`, then every pole of F is on `(-infinity,0]`. Since poles of F are zeros of H, every zero of H is real nonpositive. Under `H(z)=Xi(i sqrt(z))`, this gives `rho=1/2+i gamma` and RH.

Equivalently, it is enough to prove the Pick sign

`Im z>0 => Im F(z)<0`,

plus the standard analyticity and growth conditions needed for the Stieltjes representation.

## 7. Direct theta expression for the Pick numerator

Set `q=sqrt(z)` on the principal branch. Then

`H(z)=2 integral Phi(u) cosh(qu) du`,

`H'(z)= integral Phi(u) u sinh(qu)/q du`.

Thus

`Im F(z) = Im(H'(z) overline(H(z)))/|H(z)|^2`.

The numerator is exactly

`Im(H'(z) overline(H(z))) = 2 Im integral integral Phi(u)Phi(v) [u sinh(qu) cosh(overline(q)v)/q] du dv`.

Antisymmetrization gives the exact kernel

`K_q(u,v) = u sinh(qu)cosh(overline(q)v)/q - v cosh(qu)sinh(overline(q)v)/overline(q)`.

The previous numerical sign audit showed that this pointwise kernel is not sign-definite. Therefore the Pick proof, if true, must come from a global integral identity, modular pairing, or spectral representation—not pointwise positivity.

## 8. What is genuinely closed here

PROVED:

1. The theta moments are the Taylor coefficients of the exact entire function H.
2. The transformed-zero moments tau are exactly the higher Taylor coefficients of H'/H.
3. The earlier theta-vs-tau residual is therefore a logarithmic/cumulant transform, not an arbitrary unknown remainder.
4. This bridge is RH-independent.
5. The four-index theta determinant remains positive, but it is a raw-moment statement and cannot be substituted for the tau determinant.

OPEN:

1. An RH-independent theorem that converts positivity/structure of the theta Taylor data into real-negative zeros of H.
2. The global Pick/Stieltjes inequality.
3. An all-order total-positivity/Laguerre–Pólya theorem for the Riemann theta kernel.
4. RH itself.

## 9. Adversarial conclusion

The exact bridge removes one ambiguity but does not prove RH. Any future argument that simply identifies `M_k` with `tau_k` is invalid. Any argument that treats the cumulant residual as automatically positive is also invalid. The proof-bearing problem has now been reduced to a precise zero-location theorem for the theta-generated entire function H.
