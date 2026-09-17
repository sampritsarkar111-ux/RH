# RH Frontier 135 — Hamburger–Cauchy Rigidity Theorem

## Status

This closes the **rigidity subproblem** from Frontiers 133–134. It does **not** prove RH, because the remaining step is to prove unconditionally that every Hankel matrix built from the sequence below is positive semidefinite.

## Setup

For every nontrivial zero \(\rho\) of \(\zeta(s)\), with multiplicity, define

\[
v_\rho=-\bigl(\rho-\tfrac12\bigr)^{-2},
\qquad
\tau_n=\sum_\rho v_\rho^{\,n+1},\qquad n\ge 0.
\]

The standard zero-counting estimate implies

\[
\sum_\rho |v_\rho|=\sum_\rho |\rho-\tfrac12|^{-2}<\infty.
\]

Hence \(R:=\sup_\rho |v_\rho|<\infty\), and all sums below converge absolutely where used. Conjugation symmetry of the zeta zeros makes every \(\tau_n\) real.

## Theorem (Hamburger–Cauchy rigidity)

Assume every finite Hankel matrix

\[
H_N=(\tau_{i+j})_{0\le i,j\le N}
\]

is positive semidefinite. Then

\[
v_\rho\in(0,\infty)
\qquad\text{for every nontrivial zero }\rho.
\]

Consequently

\[
\Re\rho=\tfrac12
\]

for every nontrivial zero, i.e. the Hankel-PSD condition implies RH.

### Proof

### 1. Hamburger representation

Since \((\tau_n)\) is real and all Hankel matrices are PSD, the Hamburger moment theorem gives a positive Borel measure \(\mu\) on \(\mathbb R\) such that

\[
\tau_n=\int_{\mathbb R}x^n\,d\mu(x).
\]

### 2. The representing measure is compactly supported

Let

\[
C=\sum_\rho |v_\rho|<\infty,
\qquad
R=\sup_\rho |v_\rho|.
\]

For every \(n\ge0\),

\[
0\le \int x^{2n}\,d\mu(x)=\tau_{2n}
\le \sum_\rho |v_\rho|^{2n+1}
\le C R^{2n}.
\]

If \(\mu\bigl(\{|x|>R+\varepsilon\}\bigr)>0\) for some \(\varepsilon>0\), then

\[
\int x^{2n}\,d\mu(x)
\ge (R+\varepsilon)^{2n}\mu\bigl(\{|x|>R+\varepsilon\}\bigr),
\]

contradicting the previous bound for large \(n\). Thus

\[
\operatorname{supp}\mu\subset[-R,R].
\]

### 3. Cauchy-transform identity near infinity

Define the Cauchy transform

\[
C_\mu(w)=\int_{\mathbb R}\frac{d\mu(x)}{w-x},
\qquad w\in\mathbb C\setminus\mathbb R.
\]

For \(|w|>R\), compact support allows the absolutely convergent expansion

\[
C_\mu(w)
=\sum_{n\ge0}\frac{\tau_n}{w^{n+1}}
=\sum_\rho\sum_{n\ge0}\frac{v_\rho^{n+1}}{w^{n+1}}
=\sum_\rho\frac{v_\rho}{w-v_\rho}.
\]

Set

\[
M(w):=\sum_\rho\frac{v_\rho}{w-v_\rho}.
\]

After combining equal nodes, if a node \(a\ne0\) occurs with total multiplicity \(m(a)\), then \(M\) has a simple pole at \(a\) with residue

\[
\operatorname*{Res}_{w=a}M(w)=m(a)a\ne0.
\]

The only accumulation point of the nodes is \(0\).

### 4. Nonreal nodes are impossible

The positive-measure Cauchy transform \(C_\mu\) is holomorphic on the whole upper and lower half-planes.

Suppose some node \(a\) lies in the upper half-plane. On the connected domain obtained from the upper half-plane by removing the discrete nodes, \(C_\mu\) and \(M\) agree for all sufficiently large \(|w|\), hence by the identity theorem they agree everywhere on that punctured domain.

But \(C_\mu\) is holomorphic at \(a\), whereas \(M\) has a nonremovable simple pole there with residue \(m(a)a\ne0\). Contradiction.

The same argument in the lower half-plane excludes nodes there. Therefore every \(v_\rho\) is real.

### 5. Negative real nodes are impossible

Fix a real node \(a\ne0\) of multiplicity \(m(a)\). Since the nodes can accumulate only at \(0\), \(a\) is isolated. From the upper-half-plane identity,

\[
\lim_{y\downarrow0}iy\,C_\mu(a+iy)
=\lim_{y\downarrow0}iy\,M(a+iy)
=m(a)a.
\]

For a positive measure, dominated convergence gives the standard atom formula

\[
\lim_{y\downarrow0}iy\,C_\mu(a+iy)=\mu(\{a\})\ge0.
\]

Hence

\[
\mu(\{a\})=m(a)a\ge0.
\]

Because \(m(a)>0\) and \(a\ne0\), necessarily

\[
a>0.
\]

Thus every node satisfies \(v_\rho\in(0,\infty)\).

Finally,

\[
v_\rho=-\bigl(\rho-\tfrac12\bigr)^{-2}>0
\]

implies \((\rho-\tfrac12)^2\) is negative real, so \(\rho-\tfrac12\) is purely imaginary. Therefore \(\Re\rho=\tfrac12\). QED.

## Uniqueness compatibility

Once all nodes are positive, define

\[
\nu=\sum_a m(a)a\,\delta_a.
\]

Then \(\nu\) is a finite positive measure supported in \([0,R]\), and

\[
\int x^n\,d\nu(x)=\sum_a m(a)a^{n+1}=\tau_n.
\]

Both \(\mu\) and \(\nu\) are compactly supported positive measures with the same moments, hence the compact moment problem is determinate and \(\mu=\nu\). Thus the positive-real Hamburger representation is not merely compatible with the zero-divisor representation: it is forced to be exactly the weighted atomic measure carried by the zero nodes.

## Exact equivalence obtained

The converse is immediate under RH: if \(\rho=\tfrac12+i\gamma\), then

\[
v_\rho=\gamma^{-2}>0,
\]

and

\[
\tau_{i+j}=\sum_\rho v_\rho^{i+j+1}
\]

is the moment matrix of the positive atomic measure \(\sum_\rho v_\rho\delta_{v_\rho}\). Hence

\[
\boxed{\text{RH}\iff H_N\succeq0\text{ for every }N.}
\]

This equivalence is non-circular: the difficult remaining direction is now isolated entirely in proving **unconditional all-order Hankel positivity** from the theta/explicit-formula side without using zero locations.

## Remaining wall

The rigidity wall is closed. The sole proof-bearing target in this route is now:

\[
\boxed{H_N=(\tau_{i+j})_{0\le i,j\le N}\succeq0\quad\text{for every }N,\text{ derived without RH}.}
\]

Any proposed completion must prove this global positivity theorem analytically; finite numerical checks are insufficient.