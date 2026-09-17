# Unconditional positive-Gram attack: cyclicity wall isolated exactly

## Main result
A positive Gram mechanism is available unconditionally for the finite Nyman–Beurling problem. The remaining cyclicity statement is not an independent auxiliary lemma: in the Hardy-space formulation it is equivalent to the absence of zeros of zeta in the relevant half-plane, and in the critical L2 formulation it is equivalent to RH.

Let rho(x)={x} and rho_a(x)=rho(1/(a x)) on (0,infinity). For 0<Re(s)<1,

M rho_a(s) = -a^{-s} zeta(s)/s.

Mellin–Plancherel on Re(s)=1/2 gives

|| sum_{a<=N} c_a rho_a ||_2^2
 = (1/(2 pi)) integral |zeta(1/2+it)/(1/2+it)|^2 |sum_{a<=N} c_a a^(-1/2-it)|^2 dt >= 0.

Thus, with

(B_N c)(t) = zeta(1/2+it)/(1/2+it) * sum_{a<=N} c_a a^(-1/2-it),

we have the exact finite factorization G_N=B_N^*B_N >= 0, with no RH assumption.

The target chi_(0,1) has Mellin transform 1/s. Hence

d_N^2 = inf_{A_N} (1/(2 pi)) integral |(1-zeta(1/2+it) A_N(1/2+it))/(1/2+it)|^2 dt,

where A_N(s)=sum_{a<=N} c_a a^(-s). Therefore

1/s in closure Ran(B_infinity) <=> d_N -> 0.

Baéz-Duarte's integer-dilate theorem says this closure is equivalent to RH.

## Exact Hardy-space obstruction: why cyclicity is the wall
Passing to the Mellin/Hardy model turns the arithmetic family into the multiplier zeta(s)/s times Dirichlet polynomials. Point evaluation in H2 on a half-plane is bounded.

Suppose zeta(rho)=0 for some rho with Re(rho)>1/2. Every finite arithmetic multiple

F(s)=zeta(s) A_N(s)/s

satisfies F(rho)=0. Therefore every H2-limit of such F also has value 0 at rho. But the target 1/s satisfies 1/rho != 0. Hence the target cannot lie in the closure. Thus

cyclicity of 1/s => zeta has no zero with Re(s)>1/2.

Conversely, the classical Beurling/Nyman theory gives the corresponding density implication from zero-freeness in the relevant half-plane. In the critical L2 formulation, Baéz-Duarte's strengthening gives

1/s in closure Ran(B_infinity) <=> RH.

So an unconditional proof of the requested cyclicity theorem would itself constitute an unconditional proof of RH. It cannot be obtained merely by strengthening finite-dimensional Gram positivity.

## Adjoint formulation
For the Mellin-side synthesis operator B_infinity,

closure Ran(B_infinity) = (ker B_infinity^*)^perp.

Thus cyclicity is equivalent to triviality of the relevant adjoint kernel. A zero rho with Re(rho)>1/2 yields a bounded point-evaluation obstruction in the Hardy model. Eliminating every such obstruction is therefore exactly the zero-free problem.

## Target-vector coefficients
The target vector against each integer dilate is explicitly

<chi_(0,1),rho_a> = (log a + 1 - gamma)/a.

Thus q_N is completely explicit; the unresolved issue is global completeness of the arithmetic family.

## Non-circularity audit
The safe exact implications are:

finite Gram positivity -> G_N >= 0;
cyclicity -> d_N -> 0;
d_N -> 0 <=> RH;
zeta(rho)=0 with Re(rho)>1/2 -> failure of the corresponding Hardy cyclicity.

A circular proof would assert cyclicity by assuming RH, nonvanishing of zeta throughout Re(s)>1/2, positivity of all Li coefficients, or an unconstructed Hilbert–Polya operator.

## Conclusion
The requested wall is now isolated exactly:

**the decisive missing theorem is an unconditional proof that 1/s is cyclic for the arithmetic Nyman–Beurling synthesis operator. By Baéz-Duarte, that statement is equivalent to RH.**

Therefore the finite positive-Gram mechanism cannot by itself close the proof. A genuine completion needs a new unconditional argument that excludes all off-line zeros (or an equivalent theorem), rather than only stronger finite-dimensional PSD estimates.

## References
Balazard–Saïas: classical Mellin identity and Nyman–Beurling formulation.
Baéz-Duarte (2002): integer-dilate strengthening, RH iff chi_(0,1) belongs to the closed span of rho_a.
Baéz-Duarte (2003): published strengthening of the Nyman–Beurling criterion.
