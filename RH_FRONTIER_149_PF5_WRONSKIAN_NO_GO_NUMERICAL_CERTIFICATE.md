# Frontier 149 Numerical Certificate Summary

At u=0, for the Riemann-Jacobi kernel Phi, exact recurrence evaluation of derivatives gives:

Phi^(0)(0) = 0.8933938009342469...
Phi^(2)(0) = -16.730500774703256...
Phi^(4)(0) = 812.1628334554243...
Phi^(6)(0) = -50735.72590616842...
Phi^(8)(0) = 1823335.788363640...

The order-five derivative Wronskian factors as

W5(0) = (a2*a6-a4^2) det([[a0,a2,a4],[a2,a4,a6],[a4,a6,a8]]).

Certified interval evaluation gives

a2*a6-a4^2 > 189225.6335319359,

while the 3x3 determinant lies below -644014900.3773719.

Therefore W5(0) < 0. The tail from n>=5 is bounded analytically using |p_k(pi n^2)e^{-pi n^2}| <= C_k n^20 e^{-3n^2} and sum_{n>=5} n^20 e^{-3n^2} < 2.66e-19.

This excludes PF5/PF∞ for the fixed translation kernel Phi(x-y).