# Pole–Vandermonde Barrier (PVB): a new fixed-shift reduction

## 1. Exact algebraic duality

Let

`G(z)=a_0 E(z)=sum_{n>=0} a_n z^n`, `a_0>0`, and write

`E(z)=sum_{n>=0} e_n z^n`, `e_0=1`.

Define `h_n` by

`1/E(-z)=sum_{n>=0} h_n z^n`.

For the consecutive Toeplitz minor

`D_{r,k}=det(e_{k+j-i})_{i,j=0}^{r-1} * a_0^r`,

Jacobi–Trudi duality gives the exact identity

`D_{r,k}/a_0^r = det(h_{r+j-i})_{i,j=0}^{k-1}`.

Thus a fixed shift `k` changes the problem from an `r x r` determinant to a `k x k` determinant while the index `r` moves into the coefficients `h_n`.

This is not a numerical approximation and does not use RH.

## 2. Pole model

Suppose, for a moment, that the reciprocal function has a finite positive-pole model

`H(z)=1/E(-z) = regular_part + sum_{j=1}^k c_j/(1-q_j z)`,

with

`c_j>0`, `q_j>0`, and `q_1>q_2>...>q_k>0`.

Then the pole contribution to the coefficients is

`h_n^(k)=sum_{j=1}^k c_j q_j^n`.

For the dual determinant,

`M_{r,k}=det(h_{r+j-i}^(k))_{i,j=0}^{k-1}`,

factorization through the Vandermonde matrices gives

`M_{r,k} = (prod_j c_j q_j^r) det(q_j^{-i}) det(q_j^j) > 0`.

The two Vandermonde determinants have opposite signs under the same ordering, so their product is positive. Equivalently,

`M_{r,k} = (prod_j c_j q_j^r) prod_{1<=i<j<=k} ((q_i-q_j)^2/(q_i q_j)) > 0`.

This is the **Pole–Vandermonde Barrier**: positivity is forced when the first `k` dominant poles are positive, simple, separated, and have positive residues, provided the remaining analytic tail is small enough in the determinant norm.

## 3. Application to Xi

Take

`G(z)=1/8 xi(1/2+sqrt(z)/2)=sum a_n z^n`.

A zero `rho` of `G` becomes a pole of `1/G(-z)`. If the corresponding zero is on the critical line, `rho=1/2+i gamma`, then the associated pole location in the normalized variable is positive and proportional to `gamma^{-2}`.

Therefore a finite verified block of critical-line zeros supplies a finite positive-pole core. The unresolved high-zero part becomes a remainder term.

The research problem is then split into two exact inequalities:

1. **Core positivity:** the first `k` verified poles contribute the positive Vandermonde product above.
2. **Tail domination:** the contribution of all remaining poles/analytic remainder is smaller than the positive core, in a norm strong enough to preserve the determinant sign.

No off-line zero may be assumed away. Any tail estimate must be derived from unconditional zero-counting/complex-analytic bounds.

## 4. Why this is useful

This framework attacks the complementary wedge from the opposite direction to the 2026 cubic-tail result. Michalowski proves positivity when the shift is enormous relative to the rank. PVB instead keeps the shift fixed and lets the rank grow, converting the growing determinant into a fixed-size determinant whose asymptotics are controlled by dominant poles.

The two mechanisms suggest a possible two-sided covering strategy:

- **pole-dominant regime:** fixed or moderately growing `k`, large `r`;
- **saddle-point regime:** `k >= 10^18 r^3`;
- **finite bridge region:** an explicit compact region in `(r,k)` checked by rigorous interval arithmetic.

A complete RH proof would require the bridge to cover every remaining `(r,k)` and, crucially, an unconditional tail bound that does not encode RH.

## 5. Important limitation

PVB is a new reduction/barrier mechanism, not yet a proof of RH. The difficult step is the uniform tail-domination theorem. If that estimate secretly assumes that all remaining zeros are on the critical line, the argument is circular and must be rejected.

## 6. Immediate test target

For each fixed `k`, prove an explicit inequality of the form

`||R_{r,k}|| <= eta_{r,k} Core_{r,k}` with `eta_{r,k}<1`,

where `R_{r,k}` is the determinant perturbation induced by the unverified zero tail. The strongest useful version is uniform in `r` for `1 <= k <= K`, followed by growth of `K`.

This turns the vague phrase “the verified zeros dominate” into a concrete determinant-stability inequality.
