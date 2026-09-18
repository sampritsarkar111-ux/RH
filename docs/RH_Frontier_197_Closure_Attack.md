# RH Frontier 197 — Closure Attack: Positive-Factorization + Orbit-Separation + Jensen Residual

Date: 2026-09-18

## Research status

This is a proof-oriented research program. It does **not** claim that the Riemann Hypothesis has been proved.

The current mathematically decisive bottleneck is not another numeral representation. The proof-bearing object must be an unconditional theorem that forces positivity/coercivity independently of the unknown zero set.

## 1. Exact identity already available

For Re(s)>1, the MRDTS reciprocal-zeta channel has the form

$$
M_d(s)=d^{-s}/\zeta(s),
\qquad
\frac{d}{ds}\log M_d(s)=-\log d-\frac{\zeta'(s)}{\zeta(s)}.
$$

Combining this with the elementary, Gamma and pi factors gives the standard completed xi function

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$

This is an identity-level normalization bridge. It does not locate zeros.

## 2. New proof-bearing target: Positive-Factorization Theorem

Let A be the admissible Weil test-function space and define the MR quadratic form by the exact prime + archimedean + boundary construction.

### Target theorem PF

Find a zero-independent operator T_MR and a nonnegative remainder R such that

$$
\boxed{
Q_{MR}(f)=\|T_{MR}f\|_{\mathcal H}^2+R(f),
\qquad R(f)\ge0
}
$$

for every admissible f, and prove

$$
\boxed{Q_{MR}(f)=W_\xi(f).}
$$

Then Weil positivity follows without examining individual zeros.

The crucial anti-circularity condition is that T_MR and R are constructed solely from arithmetic data, theta/Gamma data, transforms, and explicit limiting procedures—not from the zero set.

## 3. Gram-kernel reformulation

A practical subtarget is to construct a kernel K_MR(x,y) satisfying

$$
Q_{MR}(f)=\iint f(x)K_{MR}(x,y)\overline{f(y)}\,dx\,dy
$$

and then prove positive definiteness by a Gram representation

$$
\boxed{
K_{MR}(x,y)=\langle \Phi_x,\Phi_y\rangle_{\mathcal H}.
}
$$

This changes the global positivity problem into two auditable identities:

1. exact kernel equality to the Weil kernel;
2. explicit Hilbert-space Gram realization.

A finite truncation should produce matrices G_N=(K(x_i,x_j)) whose positive semidefiniteness is checked by interval arithmetic. Such checks are finite certificates only; the proof requires a uniform N→∞ theorem.

## 4. Orbit-Separation Certificate

For a hypothetical off-critical symmetry orbit O(rho), write

$$
W_\xi(g)=W_O(g)+W_{rest}(g).
$$

A sufficient contradiction certificate is

$$
\boxed{
W_O(g)\le-2\varepsilon,
\qquad
|W_{rest}(g)|\le\varepsilon
}
$$

for admissible g and explicit epsilon>0.

The real target is therefore not a negative summand but a uniformly isolating witness theorem:

> every off-critical orbit admits an admissible witness whose target-orbit contribution dominates every non-target contribution.

The unresolved parts are admissibility, orbit isolation, prime/archimedean tails, all other zeros, and the justified limit passage.

## 5. Jensen residual-region program

With correctly factorial-normalized Jensen coefficients, degree 3 reduces to

$$
F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2,
$$

where

$$
r_n=\frac{\gamma_{n+1}^2}{\gamma_n\gamma_{n+2}},
\qquad
q_n=\frac{\gamma_{n+2}^2}{\gamma_{n+1}\gamma_{n+3}}.
$$

Degree-3 hyperbolicity is equivalent to F(r_n,q_n)<=0. The shifted variables x=r-1 and y=q-1 give

$$
F=(x-y)^2-2xy(x+y)-3x^2y^2.
$$

This identifies a new structural quantity: **adjacent Turan-ratio variation**, rather than log-concavity alone.

The higher-degree target is to control the finite ratio vector

$$
(r_n,r_{n+1},...,r_{n+d-2})
$$

by a Riemann-specific total-variation/Hankel-positivity inequality covering the residual (d,n) region.

## 6. Three-way closure theorem

A complete proof can be organized as the following dependency DAG:

1. exact MRDTS-to-xi normalization;
2. exact MRDTS-to-Weil quadratic-form identity;
3. independent global positivity OR independent orbit-separation;
4. Weil criterion;
5. RH.

No numerical experiment, finite Jensen family, or numeral encoding is allowed to substitute for step 3.

## 7. Computational certificate protocol

Every computation must report:

- precision;
- truncation parameters;
- interval enclosure;
- tail bound;
- independent implementation/check;
- exact statement certified;
- explicit distinction between evidence and theorem.

The repository should never label numerical consistency as an RH proof.

## 8. Breakthrough criterion

A genuine breakthrough occurs if and only if one of the following is proved unconditionally:

### PF route
A zero-independent positive factorization of Q_MR plus exact equality Q_MR=W_xi.

### OS route
A uniform orbit-separation theorem with admissible witnesses and complete remainder control.

### JH route
An all-degree/all-shift Jensen-hyperbolicity theorem for xi, or a theorem that covers its entire residual region.

Until one of these is completed, RH remains open.

## 9. Immediate next lemmas

**Lemma A — Kernel factorization:** derive the exact MRDTS kernel before any positivity claim.

**Lemma B — Tail domination:** obtain a uniform explicit bound for every omitted prime/archimedean component.

**Lemma C — Orbit witness:** construct a parametrized admissible witness g_rho with a target contribution bounded below away from zero.

**Lemma D — Residual Jensen control:** derive a Riemann-specific inequality for consecutive Turan ratios that propagates from degree 3 to arbitrary degree.

**Lemma E — Anti-circularity audit:** prove that none of A–D assumes RH through zero locations, density statements, or equivalent positivity criteria.

## Conclusion

The program has been compressed to a small number of proof-bearing gates. The strongest new route is the **Positive-Factorization / Orbit-Separation dual attack**: either construct positivity directly as a Gram norm, or separate every hypothetical off-line orbit by a rigorously bounded admissible witness. These are genuinely theorem-level targets; they are not claims that the RH has already been solved.
