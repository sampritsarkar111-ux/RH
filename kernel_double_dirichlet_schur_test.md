# Exact Nyman–Beurling Gram kernel, double-Dirichlet transform, and Schur-complement test

## Status

**Established:** exact kernel identity; rigorous double-Dirichlet representation for Re(s)>1 and its contour-shift reduction to a convergent one-variable arithmetic series; exact finite Schur-complement identity.

**Tested numerically:** the first finite Gram matrices are positive definite; the target Schur complement decreases with N in the computed range.

**Not established:** an unconditional coercive sampling inequality forcing the infinite adjoint kernel to vanish; RH remains open.

## 1. Operator and kernel

On the critical line write s=1/2+it and

B e_m(t) = zeta(s)/s * m^{-s}.

With the inner product (2 pi)^{-1} integral over R, the Gram entry is

K(m,n)=<B e_m,B e_n>
      =(1/(2 pi i)) integral_{Re(s)=1/2}
        m^{-s} n^{-(1-s)} zeta(s)zeta(1-s)/(s(1-s)) ds.

Equivalently,

K(m,n)=(1/(2 pi)) integral_R
 |zeta(1/2+it)|^2/(1/4+t^2)
 m^{-1/2-it} n^{-1/2+it} dt.

This is exactly the Gram kernel used in the Nyman–Beurling–Báez–Duarte approximation problem.

## 2. Real-variable identity

For rho(x)={x}, rho_m(x)=rho(1/(mx)),

K(m,n)= integral_0^infty rho_m(x)rho_n(x) dx.

After u=1/x,

K(m,n)= integral_0^infty {u/m}{u/n} du/u^2.

Thus K is manifestly positive semidefinite as a Gram matrix.

## 3. Double Dirichlet expansion and the exact obstruction

For Re(sigma)>1, expanding both zeta factors is absolutely legitimate. Put p=2 sigma. Then

K_sigma(m,n)
 = (1/(2 pi)) integral_R
   |zeta(sigma+it)|^2/(sigma^2+t^2)
   m^{-sigma-it} n^{-sigma+it} dt

and termwise integration gives

K_sigma(m,n)
 = sum_{a,b>=1} max(an,bm)^(-2 sigma).

Indeed the (a,b)-term is

(mnab)^(-sigma) exp(-sigma |log(bm/(an))|)
 = max(an,bm)^(-2 sigma).

This double Dirichlet series is directly convergent only for 2 sigma>2. Therefore its termwise specialization to sigma=1/2 is invalid: the critical kernel must be obtained by analytic continuation/contour shifting, not by naively setting sigma=1/2 in the double sum.

For Re(s)>1 the same arithmetic structure can be written as a single Dirichlet series

sum_{k>=1} k^{-2 sigma}
 [ floor(k/n)floor(k/m)
   -floor((k-1)/n)floor((k-1)/m) ].

The critical-line kernel is the analytically continued value represented below.

## 4. Exact contour-shift transformation

Let

K0=(log(2 pi)-gamma+1)/2,

R_1(x)=log x + gamma - H(x) - ({x}-1/2)/x,

S_1(x)=sum_{k>=1} R_1(kx),

where H(x)=sum_{1<=j<=x} 1/j.

The series S_1 converges absolutely for every x>0 because

R_1(x)=B_2({x})/(2x^2)+B_3({x})/(3x^3)+O(x^-4).

A contour shift of the exact Mellin kernel gives

boxed{
K(m,n)=1/n [ K0 + (1/2) log(n/m) ] + (1/m) S_1(n/m).
}

The representation is symmetric although symmetry is not termwise obvious. An explicitly symmetric equivalent form is

K(m,n)=1/(m+n) [ 2K0
 + (n/m)S_1(n/m)
 + (m/n)S_1(m/n) ].

At m=n=1,

S_1(1)=(log(2 pi)-gamma-1)/2,

so

K(1,1)=log(2 pi)-gamma.

The exact formula and contour-shift derivation are given by Ehm, arXiv:2405.06349, Theorem 2.1 and Proposition 3.2.

## 5. Arithmetic rational form

For r=n/m with gcd(m,n)=1, the same kernel can be written through the Vasyunin cotangent sums V(n,m):

K(m,n)=1/n * [ (1-r)/2 log r
              +(1+r)/2 (log(2 pi)-gamma) ]
        - pi/(2mn) [ V(n,m)+V(m,n) ].

For general m,n, first divide both indices by d=gcd(m,n); homogeneity gives

K(dm,dn)=K(m,n)/d.

This exposes the arithmetic dependence of the kernel explicitly.

## 6. Exact inverse/sampling identity

Let K_N=(K(m,n))_{1<=m,n<=N} and let

y_a=(B^*f)_a=<f,B e_a>.

For finite N, the orthogonal projection P_N onto span{B e_1,...,B e_N} satisfies

boxed{
 y_N^* K_N^{-1} y_N = ||P_N f||^2
}

whenever K_N is invertible. More generally K_N^+ gives the same identity on the range.

Consequently

0 <= y_N^*K_N^{-1}y_N <= ||f||^2,

and

lim_{N->infty} y_N^*K_N^+y_N
 = ||P_{closure Ran(B)} f||^2.

Therefore an unconditional coercive inequality

sup_N y_N^*K_N^+y_N >= c ||f||^2, c>0,

for every f is equivalent to completeness of Ran(B), hence to the cyclicity/density problem. The inverse Gram matrix itself does not create a new independent proof mechanism.

## 7. Target-vector Schur complement

For the target chi_(0,1), define

q_a=<chi,rho_a>=(log a+1-gamma)/a.

Let

H_N = [ K_N  q_N ; q_N^*  1 ].

Its Schur complement with respect to K_N is exactly

boxed{
Delta_N = 1-q_N^*K_N^{-1}q_N=d_N^2.
}

Equivalently,

(H_N^{-1})_{N+1,N+1}=1/d_N^2.

Thus the requested inverse/Schur-complement mechanism reduces exactly to the Báez–Duarte distance. Proving Delta_N -> 0 is RH-equivalent; proving a quantitative lower/upper bound does not by itself settle the direction needed for RH.

## 8. Numerical sanity test

Using the exact real-variable kernel integral and q_a above, direct high-precision quadrature gives approximately:

N    lambda_min(K_N)   lambda_max(K_N)   d_N^2
1    1.26066140        1.26066140        0.85821205
2    0.11144789        1.77954421        0.28996457
3    0.06758771        2.09255743        0.09383723
4    0.04053665        2.32144067        0.06512887
5    0.03012160        2.49307165        0.03610160
6    0.02246080        2.63653226        0.03598632
7    0.01708018        2.75289382        0.02430210
8    0.01422295        2.85453325        0.02416142
9    0.01041255        2.94251480        0.02401495
10   0.00916962        3.02070452        0.02377187

The computed Schur complements remain strictly positive at finite N, as expected. The inverse target entry 1/d_N^2 grows from about 3.45 at N=2 to about 42.07 at N=10.

The quantity d_N^2 log N is approximately 0.0547 at N=10; this finite-N value is only a numerical diagnostic and is not evidence for RH.

## 9. Decisive conclusion

The kernel calculation closes the requested algebraic step but also identifies the exact limitation:

**Positive Gram + explicit Dirichlet arithmetic + inverse Gram + Schur complements do not by themselves produce new coercivity.**

The inverse-Gram quadratic form is exactly the squared norm of the finite orthogonal projection. Its infinite coercivity is precisely the missing completeness statement.

A genuinely new proof mechanism would therefore have to establish an additional, independent identity or inequality that forces

closure Ran(B)=the full target Hilbert space

without assuming any zero-free region or an equivalent outer/cyclicity statement.

The most promising next target is not K_N^{-1} alone, but an independent arithmetic operator Q for which

sum_a w_a |(B^*f)_a|^2 >= c ||f||^2

can be proved from an identity not equivalent to Nyman–Beurling density itself.
