import mpmath as mp
import numpy as np
from itertools import combinations
mp.mp.dps = 50
pi = mp.pi
def phi(u):
    e4, e5, e9 = mp.e**(4*u), mp.e**(5*u), mp.e**(9*u)
    return mp.fsum((2*pi**2*m**4*e9 - 3*pi*m**2*e5) * mp.e**(-pi*m*m*e4) for m in range(1, 8))
moments, gamma = [], []
for n in range(15):
    val = mp.quad(lambda u, n=n: phi(u)*u**(2*n), [0, .25, .5, .8, 1.2, 2.0])
    moments.append(val)
    gamma.append(mp.factorial(n)*val/mp.factorial(2*n))
print('15 kernel moments / gamma coefficients:')
for n, g in enumerate(gamma): print(n, mp.nstr(g, 24))
print('\nJensen tests:')
for d in range(2, 6):
    for n in range(8):
        coeff = [mp.binomial(d,j)*gamma[n+j] for j in range(d+1)]
        scale = gamma[n]/gamma[n+1]
        roots = mp.polyroots(list(reversed([coeff[j]*scale**j for j in range(d+1)])), maxsteps=300)
        print(d, n, mp.nstr(max(abs(mp.im(z)) for z in roots), 8))
a = [moments[n]/mp.factorial(2*n) for n in range(15)]
r = a[0]/a[1]
b = np.array([float((a[n]/a[0])*r**n) for n in range(15)])
def tv(i,j):
    k=j-i
    return 0.0 if k<0 else b[k]
print('\nToeplitz minors in 9x9 truncation:')
for order in range(1,5):
    negative=tested=0; min_det=float('inf')
    for rows in combinations(range(9),order):
        for cols in combinations(range(9),order):
            det=float(np.linalg.det(np.array([[tv(i,j) for j in cols] for i in rows])))
            tested+=1; min_det=min(min_det,det)
            if det < -1e-12: negative+=1
    print(f'order={order} tested={tested} negative={negative} min_det={min_det:.6e}')
