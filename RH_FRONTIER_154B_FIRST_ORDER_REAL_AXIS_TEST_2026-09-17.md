# Frontier 154B — First-Order Real-Axis Test

This file records a diagnostic calculation only; it is not a proof.

For m(x)=-H'(x)/H(x), numerical evaluation at x=1 gives alternating signs through the first several derivatives:

(-1)^n m^(n)(1) > 0 for n=1,...,6.

These values are approximately:

n=1: 3.68862277417651e-5
n=2: 2.84407921506078e-7
n=3: 3.90200535620099e-9
n=4: 7.52508312274973e-11
n=5: 1.84930959481438e-12
n=6: 5.49541149713410e-14

Interpretation: the finite-order real-axis test is consistent with the desired Stieltjes gate, but finite numerical sign checks cannot establish complete monotonicity or analytic continuation. The proof-bearing task remains an exact theta-derived all-order identity.

No zero locations were used in this diagnostic.