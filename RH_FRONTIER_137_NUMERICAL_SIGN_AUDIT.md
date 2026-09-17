# Frontier 137 Numerical Sign Audit

For `H(z)=Xi(i sqrt(z))` and `F=H'/H`, direct high-precision evaluation gives:

- `F(x)>0` for tested `x>=0`.
- `Im F(z)<0` for sampled `Im z>0`, including `z=1+i, 1+10i, 10+i, -1+i, -10+i, 100+100i`.
- The derivatives at `0` satisfy `(-1)^n F^(n)(0)>0` through order 5 in the numerical audit.
- The corresponding finite Hankel determinants of the local Stieltjes moment sequence remain positive through size 4 in the numerical test.

These computations are only consistency evidence; they are not a proof. The pointwise unsummed double kernel remains sign-indefinite, so a global theta/modular factorization is still required.
