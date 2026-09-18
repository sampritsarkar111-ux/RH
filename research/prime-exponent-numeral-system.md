# Prime-Exponent Numeral System (PENS) — RH research direction

Status: research hypothesis / proof program. This does NOT constitute a proof of the Riemann Hypothesis.

## 1. Why add a second system?

Balanced ternary is an additive/scale-oriented coordinate system:
n = sum_k d_k(n) 3^k, with d_k(n) in {-1,0,1}.

Its main weakness for RH is that the Euler product is multiplicative over all primes. The proposed companion system therefore uses prime valuations as coordinates.

## 2. Prime-Exponent Numeral System

Let p_1=2,p_2=3,p_3=5,... be the primes. For every n>=1 define

v(n) = (v_{p_1}(n),v_{p_2}(n),...),  v_{p_j}(n) in {0,1,2,...},

with finite support, by the exact unique factorization

n = product_j p_j^{v_{p_j}(n)}.

This is not claimed to be a new theorem: it is a coordinate representation of unique prime factorization. The research novelty is to combine these coordinates with the user's balanced-ternary coordinates and build proof-bearing operators.

## 3. Exact Dirichlet geometry

For Re(s)>1,

n^{-s} = exp(-s sum_j v_{p_j}(n) log p_j).

Hence

zeta(s)
= sum_{v in N_0^(N), finite support} exp(-s sum_j v_j log p_j)
= product_p (1-p^{-s})^{-1}.

The finite-support condition is essential.

Define the prime-coordinate energy

E_s(v) = sum_j v_j log p_j.

Then the Dirichlet weight is exp(-s E_s(v)). This turns the Euler product into a product of one-dimensional geometric directions.

## 4. Dual system with balanced ternary

For each n define

C(n) = (D_0(n),D_1(n),..., v_2(n),v_3(n),v_5(n),...).

The first part records additive base-3 structure; the second records multiplicative prime structure.

The key proposed object is a coupled kernel

K_s(m,n)
= A_s(D(m),D(n)) B_s(v(m),v(n)),

where A_s is a ternary kernel and B_s is a prime-valuation kernel.

A useful prime-coordinate choice is

B_t(m,n)
= exp(-t sum_p |v_p(m)-v_p(n)| log p),

for t>0.

This B_t is positive definite on the integer lattice of finite-support valuation vectors because |a-b| on Z is conditionally negative definite and exp(-t|a-b|) is positive definite in each coordinate; finite products preserve positive definiteness.

However, positive definiteness alone is NOT an RH proof.

## 5. Proof-bearing target

The real target is an operator H_TP for which all three identities hold:

(1) H_TP is self-adjoint on a rigorously specified Hilbert space.

(2) Its regularized spectral determinant is exactly
    det_*(I - H_TP(s)) = C(s) xi(s),
    with C(s) zero-free.

(3) The prime trace expansion of the determinant reproduces the Euler product:
    -log det_*(I-H_TP(s))
    = sum_p sum_{r>=1} p^{-rs}/r
    = log zeta(s)
in the region of absolute convergence, followed by a justified continuation.

Only a theorem establishing these identities, together with the completed functional-equation/theta side, would make the system proof-bearing for RH.

## 6. New bridge to the existing theta/Weil program

The strongest direction is not “ternary positivity” by itself. It is a factorization of the arithmetic Hilbert space into

H_additive (balanced ternary)
tensor
H_multiplicative (prime valuations)

and then a single operator

H_TP = H_theta + H_prime + H_coupling.

The coupling term must be Riemann-specific: it must simultaneously encode the archimedean/theta contribution and the prime contribution appearing in the Weil explicit formula.

A successful closure theorem would have the schematic form

Theta modularity
+ prime-valuation trace identity
+ self-adjointness
+ exact determinant normalization
=> xi(s) has only zeros on Re(s)=1/2.

## 7. Immediate falsification tests

For every finite truncation:

- check Hermiticity on s=1/2+it;
- check positive semidefiniteness of the proposed Weil kernel;
- compare regularized log-determinants with xi(1/2+it);
- compare traces with sums over prime powers;
- search for the smallest counterexample rather than only confirming examples;
- verify that no step silently replaces logarithmic/cumulant structure by raw moment positivity.

## 8. Important warning

Balanced ternary and prime-factor coordinates are established mathematical representations. Calling the coordinate system itself a new solution would be incorrect. The potentially new research object is the coupled ternary-prime operator and, above all, an exact theorem connecting its determinant/trace to xi(s) and the Weil criterion.

Current project status: OPEN. No RH gate is closed by this construction yet.
