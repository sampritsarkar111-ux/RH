# Frontier 176 — Square-variable Stieltjes gate

## Status
OPEN. This is a sharpened sufficient gate, not a proof of RH.

## Core correction
For H(x)=Xi(1/2+x), the direct claim that -H'(x)/H(x) is a Stieltjes function in x is not the natural target. Under RH, zeros occur at x=±iγ, and

    -H'(x)/(x H(x))

is naturally a Stieltjes transform in u=x^2.

Define

    F(u) = - H'(sqrt(u)) / (sqrt(u) H(sqrt(u))).

Because H is even, H'(x)/x is even, so F has a single-valued meromorphic continuation in u away from images of zeros.

## Exact sufficient theorem
Assume F is an unconditional Stieltjes function:

    F(u)=a+b/u+∫_(0,∞) dμ(t)/(u+t),

with a,b≥0, μ≥0 and standard Stieltjes integrability, together with global meromorphic pole correspondence between zeros of H and poles of F.

A Stieltjes function is analytic on C\(-∞,0] (apart from its allowed cut/poles on the negative axis). If ρ is a nonzero zero of H of multiplicity m, then H'/H has a pole of residue m at ρ. Therefore F has a pole at u=ρ²; the pole cannot disappear because multiplication/division by the nonzero analytic factor 1/ρ does not cancel it.

Hence ρ²∈(-∞,0], so ρ is purely imaginary. Writing ρ=s-1/2 gives Re(s)=1/2. Thus every nontrivial zero lies on the critical line.

## Critical unresolved arrow
The missing theorem is still:

    theta kernel / arithmetic data
        => F(u) is Stieltjes globally

without using the zero set.

Positivity of the theta kernel alone does not imply positivity of a logarithmic derivative. The nonlinear quotient is the wall.

## Stronger equivalent certificate to seek
Find an explicit positive measure μ derived directly from the theta kernel such that

    -H'(sqrt(u))/(sqrt(u)H(sqrt(u)))
       = a+b/u+∫_0^∞ dμ(t)/(u+t),

with all analytic continuation and interchange steps justified.

Equivalent Pick form: F analytic on C\(-∞,0] and Im F(z)≤0 for Im z>0, with F(x)≥0 for x>0 and Stieltjes growth at infinity.

## Failure tests
1. Verify F is single-valued because H is even.
2. Verify every zero of H produces a genuine pole of F at ρ² with the correct multiplicity.
3. Test whether the candidate theta representation actually yields a positive measure rather than merely a positive kernel.
4. Check branch cuts and u=0 separately.
5. No use of RH, Hadamard factors with assumed imaginary zeros, or numerical zero locations in the derivation.

## Significance
This theorem isolates a clean proof-bearing finish line and corrects the earlier overly direct Stieltjes formulation. It does not itself establish the required theta-to-Stieltjes identity.
