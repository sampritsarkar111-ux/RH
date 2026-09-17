# RH Frontier 142 — Closure Attacks on R4, Global Pick/Stieltjes, and All-Order tau-Hankel Positivity

Date: 2026-09-17

## Objective
Attack the three remaining walls by genuinely different mechanisms: (1) the nonlinear residual R4 in the theta -> tau bridge; (2) the global Pick/Stieltjes inequality for F=H'/H; (3) unconditional positivity of every tau-Hankel matrix; and (4) the final implication to RH. No zero locations may be assumed. Numerical evidence is diagnostic only.

## 1. Residual R4: exact cumulant defect
Let H(z)=Xi(sqrt(z))=sum_{k>=0} h_k z^k and F(z)=H'(z)/H(z)=sum_{n>=0} c_n z^n. The zero-power sums are encoded by the logarithmic derivative, so the theta Taylor coefficients h_k do not map linearly to tau_k. The exact defect is the nonlinear cumulant transform c_n=[z^n](H'/H), tau_n=-c_n/n! in the convergent derivative range after canonical normalization.

### Attempt A — additive determinant residual
Target: det(tau_{i+j})_{0<=i,j<4}=Theta_4+R_4 with Theta_4 the positive theta Vandermonde integral and R_4>=0.

Failure: this decomposition is not canonical. Determinants of logarithmic derivatives are nonlinear rational polynomials in h_0,...,h_N; there is no natural additive remainder whose sign follows from the raw theta moment determinant. The correct object is a cumulant/Hankel defect, not an additive theta remainder.

### Attempt B — cumulant-to-moment inversion
H(z)=H(0) exp(integral_0^z F(w)dw). If F were Stieltjes, its Taylor coefficients would have the required signed moment structure and all tau-Hankel determinants would be nonnegative. But this assumes precisely the missing Pick/Stieltjes theorem.

Status: exact nonlinear bridge proved; positivity of its Hankel determinants remains open.

## 2. Global Pick/Stieltjes
Set F(z)=H'(z)/H(z). Desired sign: Im z>0 => Im F(z)<=0. A sufficient representation is F(z)=a+int_0^infinity dnu(t)/(z+t), a>=0, nu>=0.

### Attempt C — direct theta double integral
Starting from H(z)=2 int_0^infinity Phi(u) cos(u sqrt(z))du gives an exact double-integral expression for Im F. Phi(u)>0, but the complex antisymmetrized kernel is not pointwise sign-definite. Therefore positivity cannot be pushed inside the integral term-by-term.

### Attempt D — Hermite-Biehler / zero-free route
For a real entire function in the Laguerre-Pólya class, its logarithmic derivative has the Pick sign. Conversely, the Pick sign plus the correct growth forces poles of F onto the negative real axis, hence zeros of H there. This is a valid equivalence, not a new proof mechanism.

### Attempt E — modular pairing / square-modulus factorization
Seek -Im F(z)=N(z)/|H(z)|^2 with N(z)>=0 as an explicit theta-generated sum/integral of squares. The required factorization has not been derived; phase-aligned pairing is obstructed by nonlocal cancellation.

Status: OPEN.

## 3. All-order tau-Hankel positivity
For tau_n=sum_r v_r^(n+1), v_r=-(rho_r-1/2)^(-2), the desired condition is H_N=(tau_{i+j})_{i,j=0}^N >=0 for every N.

### Attempt F — raw theta Hankel minors
M_k=int_0^infinity Phi(u)u^(2k)du obey
 det(M_{i+j})_{i,j=0}^{N-1}=1/N! int prod_r Phi(u_r) prod_{r<s}(u_s^2-u_r^2)^2 du_1...du_N >=0.
But tau is a logarithmic-cumulant transform of M_k. Generic positive moment sequences do not preserve Hankel positivity under this nonlinear transform. Thus no closure follows without a Riemann-specific theorem.

### Attempt G — Stieltjes continued fraction
If F is Stieltjes, its S/J-fraction has nonnegative coefficients and the Hankel determinants factor into nonnegative products. Conversely, all tau-Hankel positivity yields the same moment structure. Hence this route is equivalent to the Pick/Stieltjes wall, not independent of it.

### Attempt H — Jensen-polynomial hyperbolicity
All-order Hankel positivity can be reformulated through all-order Jensen/Laguerre-Pólya hyperbolicity conditions for H. This is a useful equivalent formulation, but proving every degree hyperbolic is itself the missing all-order real-zero theorem.

## 4. Structural reduction: the three walls are one wall
Pick/Stieltjes F => poles of F lie on (-infinity,0] => zeros of H lie on (-infinity,0] => RH.

RH => v_r>0 => every tau-Hankel matrix is a Gram matrix => tau-Hankel positivity.

All-order tau-Hankel positivity => Hamburger moment representation => Cauchy-transform rigidity => v_r>0 => RH.

Thus proving any one of the three walls closes RH, but raw theta positivity cannot be transferred to tau without a new nonlinear theorem.

## 5. Adversarial no-go tests
Reject: Phi>0 => RH; Phi log-concave/TP2 => RH; raw theta Hankel PSD => tau-Hankel PSD; finite Jensen/Turan inequalities => RH; zero-defined spectral operators; numerical Pick checks as proofs; and phase-aligned blockwise positivity as a global proof.

A 2026 preprint reports strict log-concavity (TP2) of the Riemann Xi kernel while explicitly leaving the TP2 -> TP-infinity/Laguerre-Pólya passage open. Another 2026 preprint reports nonlocal cancellation as an obstruction to phase-aligned blockwise positivity. These are boundary checks, not RH proofs.

## 6. Exact mechanisms that would close the problem
(A) Theta-generated positive resolvent: F(z)=a+int_0^infinity dnu(t)/(z+t), nu>=0, with nu defined independently of RH.

(B) Global square factorization: -Im F(z)=|H(z)|^{-2} int_S |A(z,u)|^2 dmu(u), dmu>=0, with A explicitly theta-generated.

(C) All-order nonlinear total-positivity theorem: the theta-generated H has every logarithmic-cumulant Hankel matrix PSD.

(D) Theta-to-Laguerre-Pólya theorem: the Riemann theta kernel generates a TP-infinity Fourier transform.

Any A-D would be a genuine closure mechanism. None has been established here.

## Final status
GREEN/EXACT: theta moment Vandermonde positivity; exact theta -> H Taylor map; exact logarithmic-derivative bridge to tau; conditional equivalence of Pick/Stieltjes, tau-Hankel positivity, and RH through the rigidity chain.

RED/OPEN: sign of the nonlinear R4/cumulant defect; global Pick/Stieltjes inequality; unconditional all-order tau-Hankel positivity; RH.

No claim of a proof of RH is made at this frontier.
