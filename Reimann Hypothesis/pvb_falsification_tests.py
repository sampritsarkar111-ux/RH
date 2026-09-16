import numpy as np

# Algebraic test of the Pole–Vandermonde identity.
# h_n = sum_j c_j q_j^n with positive, distinct q_j and c_j.
# M_{r,k}=det(h_{r+j-i}) should equal
# prod(c_j q_j^r) * prod_{i<j} ((q_i-q_j)^2/(q_i*q_j)).

def det(M):
    return float(np.linalg.det(np.asarray(M, dtype=float)))

for k in range(1, 7):
    q = np.array([1.0/(j+1) for j in range(1, k+1)])
    c = np.array([1.0 + 0.1*j for j in range(k)])
    for r in range(1, 8):
        h = lambda n: sum(c[j] * q[j]**n for j in range(k))
        M = [[h(r+j-i) for j in range(k)] for i in range(k)]
        lhs = det(M)
        vand = np.prod(c * q**r)
        for i in range(k):
            for j in range(i+1, k):
                vand *= (q[i]-q[j])**2/(q[i]*q[j])
        err = abs(lhs-vand)
        assert lhs > 0
        assert err < 1e-8 * max(1.0, abs(lhs), abs(vand))
print('Pole–Vandermonde identity passed for k=1..6, r=1..7.')

# A deliberate failure mode: repeated poles make the Vandermonde factor vanish.
q = np.array([0.5, 0.5])
c = np.array([1.0, 2.0])
h = lambda n: sum(c[j]*q[j]**n for j in range(2))
M = [[h(3+j-i) for j in range(2)] for i in range(2)]
print('Repeated-pole determinant:', det(M))
