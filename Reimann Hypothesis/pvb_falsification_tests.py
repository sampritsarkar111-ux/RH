import numpy as np

# Falsification test for the naive Pole–Vandermonde positivity claim.
# Even with positive, distinct q_j and positive residues c_j,
# det(h_{r+j-i}) can be negative because the two Vandermonde determinants
# carry a parity-dependent sign.

def det(M):
    return float(np.linalg.det(np.asarray(M, dtype=float)) )

for k in range(1, 6):
    q = np.array([1.0/(j+1) for j in range(1, k+1)])
    c = np.array([1.0 + 0.1*j for j in range(k)])
    for r in range(1, 5):
        h = lambda n: sum(c[j] * q[j]**n for j in range(k))
        M = [[h(r+j-i) for j in range(k)] for i in range(k)]
        lhs = det(M)
        rhs_unsigned = np.prod(c * q**r)
        for i in range(k):
            for j in range(i+1, k):
                rhs_unsigned *= (q[i]-q[j])**2/(q[i]*q[j])
        parity = (-1)**(k*(k-1)//2)
        assert abs(lhs - parity*rhs_unsigned) < 1e-8 * max(1.0, abs(lhs), abs(rhs_unsigned))
print('Signed Pole–Vandermonde identity passed for k=1..5, r=1..4.')
print('The unsigned positivity claim is therefore falsified for k=2,3 mod 4.')
