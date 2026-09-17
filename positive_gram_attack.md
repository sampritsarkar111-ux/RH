# Unconditional positive-Gram attack: corrected decisive wall

## Main result
A positive Gram mechanism is already available unconditionally for the finite Nyman–Beurling problem. The real missing ingredient is **cyclicity/density**, not finite-dimensional positivity.

Let rho(x)={x} and rho_a(x)=rho(1/(a x)) on (0,infinity). For 0<Re(s)<1,

M rho_a(s) = -a^{-s} zeta(s)/s.

This is the classical Mellin identity for the fractional-part function. Mellin–Plancherel on Re(s)=1/2 gives, for finite coefficient vectors c,

|| sum_{a<=N} c_a rho_a ||_2^2
 = (1/(2 pi)) integral |zeta(1/2+it)/(1/2+it)|^2 |sum_{a<=N} c_a a^{-1/2-it}|^2 dt >= 0.

Therefore, defining

(B_N c)(t) = zeta(1/2+it)/(1/2+it) * sum_{a<=N} c_a a^{-1/2-it},

we have the exact factorization

G_N = B_N^* B_N >= 0.

No zero locations and no RH assumption enter this factorization.

The target chi_(0,1) has Mellin transform 1/s. Hence

d_N^2 = inf_{A_N} (1/(2 pi)) integral |(1-zeta(1/2+it) A_N(1/2+it))/(1/2+it)|^2 dt,

where A_N(s)=sum_{a<=N} c_a a^{-s}.

Thus the exact proof target is

1/s in closure of Ran(B_infinity),

equivalently d_N -> 0.

By the Nyman–Beurling–Báez-Duarte criterion, this density statement is equivalent to RH. So the Gram positivity is not the missing theorem; the missing theorem is an unconditional cyclicity theorem for the target vector.

## A second exact finite identity
The target vector against each integer dilate has the elementary closed form

<chi_(0,1),rho_a> = (log a + 1 - gamma)/a.

Indeed, after u=1/(a x),

<chi,rho_a> = (1/a) integral_{1/a}^infinity {u} u^{-2} du,

and splitting at the positive integers yields the stated expression. Thus q_N is explicitly known; the only genuinely difficult object in the finite projection formula is the Gram geometry, not the target vector.

## Consequence for the Weil route
A term-by-term positive decomposition of the prime side is not the correct target, because the explicit-formula prime contribution has signed oscillatory terms. The proof-bearing objective must instead be a global exact factorization

Q_W(f)=||T_W f||^2

on the complete admissible test space, followed by an unconditional cyclicity/completeness theorem. A finite-window PSD certificate is insufficient.

## Cross-route target
Construct one arithmetic positive operator P=T^*T such that

(i) its finite compressions reproduce the Nyman Gram operators,
(ii) its quadratic form reproduces the full Weil explicit formula,
(iii) the Li coefficients arise as distinguished finite test vectors, and
(iv) the relevant target vector is proved cyclic for T without assuming RH.

If (i)–(iv) are established, RH follows. At present (i) is exact and unconditional; (ii)–(iv), especially cyclicity, remain open.

## Non-circularity audit
No claim here proves RH. Any argument that proves cyclicity by assuming nonvanishing of zeta in Re(s)>1/2, positivity of all Li coefficients, reality of Xi zeros, or an unconstructed Hilbert–Polya operator is circular.

## Verification references
The classical Mellin identity and Nyman–Beurling formulation are documented in Balazard–Saïas, while Báez-Duarte proves the integer-dilate strengthening and states that RH is equivalent to closure of the span of the integer family. The conditional Möbius approximation rate is also explicitly stated in his second version. The Li/Weil equivalence is documented by Bombieri–Lagarias. 
