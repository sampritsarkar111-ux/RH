# Pole–Vandermonde decomposition: a fixed-shift reduction, with a critical obstruction

## Status

This note records a useful algebraic duality, but **not a positivity proof**. The initial idea that a positive-pole partial fraction expansion would automatically give a positive Vandermonde determinant is false in the Xi setting: partial-fraction residues of a product of positive linear factors need not all be positive, and the determinant sign also depends on pole ordering.

The failed positivity claim is deliberately retained here as a falsification result so it is not accidentally reused as a proof step.

## 1. Exact algebraic duality

Let

`G(z)=a_0 E(z)=sum_{n>=0} a_n z^n`, `a_0>0`, and write

`E(z)=sum_{n>=0} e_n z^n`, `e_0=1`.

Define `h_n` by

`1/E(-z)=sum_{n>=0} h_n z^n`.

Then the Jacobi–Trudi identity gives the exact duality

`D_{r,k}/a_0^r = det(h_{r+j-i})_{i,j=0}^{k-1}`.

Thus a fixed shift `k` converts the original `r x r` determinant into a `k x k` determinant whose index `r` appears in the reciprocal coefficients.

This identity is unconditional and can be useful for attacking the small-shift/large-r corner.

## 2. The tempting pole argument and why it fails

If, hypothetically,

`h_n = sum_{j=1}^k c_j q_j^n`,

then Cauchy–Binet/Vandermonde factorization gives

`det(h_{r+j-i}) = (prod_j c_j q_j^r) det(q_j^{-i}) det(q_j^j)`.

The magnitude contains the Vandermonde-square factor

`prod_{i<j} ((q_i-q_j)^2/(q_i q_j))`,

but the sign is not automatically positive. More importantly, for a product

`E(-z)=prod_j (1-alpha_j z)`,

the partial-fraction residues of `1/E(-z)` generally alternate in sign. Therefore “positive poles + positive residues” is not supplied by RH itself.

A direct numerical falsification uses positive distinct poles `q=(1/2,1/3)` with positive residues `c=(1,1.1)`: the determinant for `k=2` is negative, while the unsigned Vandermonde product is positive. Hence the earlier positivity statement was too strong.

## 3. What survives as a research tool

The exact duality remains valuable:

`D_{r,k}>0  <=>  det(h_{r+j-i})_{i,j=0}^{k-1}>0`.

For fixed `k`, this reduces an arbitrarily large determinant order `r` to fixed matrix size `k`. The new problem is to exploit the **special algebraic structure of the Xi reciprocal** rather than generic positive-pole residues.

Potential valid routes include:

1. prove a sign-regularity theorem for the signed residues of `1/G(-z)`;
2. use grouped residues rather than individual poles, with a provable positive grouped kernel;
3. derive asymptotics of `h_n` directly from the nearest poles without assuming their locations beyond what is unconditionally known;
4. combine this fixed-shift reduction with the already-certified large-shift saddle-point region.

## 4. Required non-circularity condition

Any pole argument must never replace the unknown statement “all zeros lie on the critical line” by an equivalent assertion about positive poles. If an estimate requires every pole of `1/G(-z)` to be positive, it has simply assumed RH.

## 5. Immediate next target

The rigorous target is now a **signed-residue variation bound** for the reciprocal Xi coefficients:

`det(h_{r+j-i}) = Core_{r,k} + Error_{r,k}`,

where `Core` is built from an explicitly unconditional finite subset of known zeros/poles and `|Error| < Core` is proved without assuming the location of the remaining zeros.

Until such a bound is established, this framework is a reduction only, not a closure of RH.
