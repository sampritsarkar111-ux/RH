# RH Frontier 200 — Global Obstruction Audit and Proof Kernel

Date: 2026-09-18

## Executive status

No unconditional proof of RH is established here. The decisive work is to separate exact equivalences from unsupported closure claims.

## 1. Weil positivity is global

For admissible g, the Weil criterion concerns the complete explicit-formula functional. If rho=sigma+it is off the critical line, then a transform evaluated at (rho-1/2)/i is generally complex. Even if its real part is negative, this is only one contribution.

Therefore:
negative single-zero contribution != negative complete Weil functional.

## 2. Correct contradiction certificate

For a hypothetical off-line orbit O(rho), a sufficient certificate is

W_O(g) <= -2 epsilon,
|W_xi(g)-W_O(g)| <= epsilon,

which yields W_xi(g)<0. The second inequality is the real global theorem.

## 3. New kernel theorem target

Define the Weil quadratic form Q on an admissible dense test space A. Seek an explicit map T:A->H such that

Q(g)=||Tg||_H^2.

If obtained by an identity that uses only the explicit formula and unconditional analytic/arithmetic estimates, positivity follows automatically.

A weaker but still sufficient target is

Q(g)=||Tg||_H^2+R(g), R(g)>=0.

The construction must include prime, Gamma, and boundary pieces and justify all limits.

## 4. Finite Gram certificate is not enough

For sample points x_1,...,x_N, positivity of

G_N=(K(x_i,x_j))

is a finite statement. To infer positivity of Q for all admissible g one needs a representation theorem plus convergence/closure estimates. Therefore numerical PSD checks are discovery tools, not the infinite proof.

## 5. Jensen route: obstruction

For degree 3,

F(r,q)=1-6qr+4q^2r+4qr^2-3q^2r^2.

With x=r-1,y=q-1,

F=(x-y)^2-2xy(x+y)-3x^2y^2.

The sign is not determined by r>=1,q>=1 alone. Consequently any proof based only on log-concavity/Turan positivity is insufficient.

## 6. New research principle: defect budget

For any proposed global contradiction, define a defect budget

D(g,rho)=|W_xi(g)-W_O(rho;g)|.

A valid orbit witness must satisfy

D(g,rho)<-W_O(rho;g).

This turns the vague phrase 'other terms are small' into a quantitative theorem obligation. The budget must include:
(a) all other zero orbits,
(b) prime powers,
(c) Gamma/archimedean terms,
(d) truncation/limit errors.

## 7. Literature audit

Current literature-search results include several recent manuscripts claiming RH proofs through Weil positivity, kernel positivity, Toeplitz positivity, or operator/fixed-point constructions. Such claims are not treated as established merely because they are deposited as preprints/repository records. Each must pass the same global identity, domain, and non-circularity audit.

## 8. Formal proof skeleton

Assume an off-line zero exists.
1. Choose g in the admissible test space.
2. Write the exact Weil explicit formula.
3. Isolate the symmetry orbit.
4. Prove the defect-budget inequality.
5. Obtain strict negative complete Weil value.
6. Apply Weil's criterion.
7. Contradiction.

The unresolved theorem is Step 4, unless the positive-factorization route closes Step 3 globally.

## 9. Breakthrough criterion

A claimed RH proof is accepted into the repository as 'proof' only after every analytic identity, positivity statement, domain assertion, and infinite limit is independently justified without RH or an equivalent criterion.

Until then the project status remains OPEN.