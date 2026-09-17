# Frontier 138 — Residual Bridge Target

The exact four-copy theta factorization gives positivity for the theta moment Hankel determinant, but the RH-bearing sequence is the transformed zero-node moment sequence `tau_n`.

Target:

`det[(tau_{i+j})_{i,j=0}^{3}] = Theta_4 + R_4`,

where `Theta_4` is an explicitly positive theta four-index integral and `R_4` is an exact, fully displayed residual obtained from the theta-to-explicit-formula transform. The required proof would be `R_4 >= 0` or an exact cancellation/factorization of `R_4`.

No identification of `Theta_4` with the zero Hankel determinant is permitted without deriving the identity. In particular, positivity of the intrinsic theta moments does not imply positivity of `tau_n`.

For the Pick route, the analogous target is

`-Im(F(z)) = P_4(z) + R_P(z)`,

with `P_4(z)>=0` obtained from the four-copy Vandermonde/square structure and an exact residual `R_P`. The sign of `R_P` must be proved; numerical positivity is not sufficient.

This is the decisive audit point: either the residual admits a sign-definite theta modular factorization, or Frontier 138 is an obstruction rather than an RH proof.