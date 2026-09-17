# Frontier 131 — Theta-Reflection Gram Closure Framework

Date: 2026-09-17

## Status

This frontier introduces a new proof architecture for the unresolved link

`unsummed theta -> theta-specific stability -> all Jensen hyperbolicity`.

It is a **research construction, not a completed proof of RH**. Every identity below is intended to be exact; every positivity statement that would finish RH is explicitly marked as a theorem target rather than asserted.

The central idea is to stop trying to prove that a positive integral of stable polynomials is stable. Instead, convert the Jensen polynomial into its Hermite matrix, lift that matrix to a multi-copy theta/reflection kernel, and isolate the exact residual that a theta-specific Gram theorem must annihilate or make positive.

---

## 1. Starting point: exact Jensen symbol

Let

\[
\Phi(u)=\sum_{m\ge1}\phi_m(u),\qquad
M_k=\int_{\mathbb R}u^{2k}\Phi(u)\,du,
\qquad
\gamma_k=\frac{M_k}{(2k)!}.
\]

For integers \(n,d\ge0\), define

\[
J_{n,d}(z)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}z^j.
\]

The exact bivariate symbol is

\[
\Sigma_{n,d}(x,y)=y^dJ_{n,d}(x/y).
\]

No zero location is used.

---

# 2. New object: the Theta-Reflection Lift

For a polynomial \(p\) define its reflection-coupled lift

\[
\boxed{
\mathfrak L_n[p](u,v)
:=
(u v)^{2n}
\Phi\!\left(\frac{u+v}{2}\right)
\Phi\!\left(\frac{u-v}{2}\right)
\,p(u^2)p(v^2).
}
\]

The associated symmetric bilinear functional is

\[
\boxed{
\mathfrak B_n[p,q]
:=
\frac{1}{(2n)!^2}
\iint_{\mathbb R^2}
(uv)^{2n}
\Phi\!\left(\frac{u+v}{2}\right)
\Phi\!\left(\frac{u-v}{2}\right)
 p(u^2)q(v^2)\,du\,dv.
}
\]

Because the completed kernel is even, the change
\[
(u,v)\mapsto\left(\frac{u+v}{2},\frac{u-v}{2}\right)
\]
interchanges reflection and convolution coordinates without inserting any zero information.

The crucial point is that \(\mathfrak B_n\) is a **two-copy object**. It therefore retains cross-copy information that is invisible to the one-copy positive-average argument already ruled out.

---

# 3. New object: Hermite-Theta matrix

Write

\[
J_{n,d}(z)=a_d\prod_{r=1}^d(z-r_r),
\qquad a_d=\gamma_{n+d}.
\]

Do **not** assume the \(r_r\) are real. Define the power sums algebraically by Newton identities,

\[
S_k=\sum_{r=1}^d r_r^k,
\qquad S_0=d,
\]
with each \(S_k\) expressed rationally in the coefficients of \(J_{n,d}\).

Define the Hermite matrix

\[
\boxed{
\mathsf H_{n,d}:=(S_{i+j})_{0\le i,j\le d-1}.
}
\]

For a real polynomial, the classical Hermite criterion relates real-rootedness to positivity of this matrix (with the standard rank qualification in multiple-root cases). Thus the desired Jensen hyperbolicity can be attacked as a matrix-positivity problem rather than by directly controlling roots.

For cubic degree, the determinant identity is especially clean:

\[
\boxed{
\det\mathsf H_{n,3}
=
\frac{\operatorname{Disc}(J_{n,3})}{\gamma_{n+3}^{\,4}}.
}
\]

Therefore the cubic discriminant gate is literally a principal Gram/Hermite gate.

---

# 4. New operator: Theta-Reflection Gram Map

Define the matrix-valued map

\[
\boxed{
\mathcal G_n[p]_{ij}
:=
\mathfrak B_n\!\left[z^i,p(z)z^j\right],
\qquad 0\le i,j<\deg p.
}
\]

For any real vector \(c=(c_0,\ldots,c_{d-1})\),

\[
\boxed{
 c^T\mathcal G_n[p]c
=
\mathfrak B_n\!\left[\sum_i c_i z^i,\ p(z)\sum_jc_jz^j\right].
}
\]

The target is to find an exact theta-dependent congruence

\[
\boxed{
\mathsf H_{n,d}
=
C_{n,d}^{T}\mathcal G_n[\mathcal P_{n,d}]C_{n,d}
+\mathcal R_{n,d},
}
\]
where \(\mathcal P_{n,d}\) is an explicitly constructed square-weight polynomial and \(\mathcal R_{n,d}\) is a modular reflection remainder.

The decisive theorem would be

\[
\mathcal R_{n,d}\succeq0
\quad\text{and}\quad
\mathcal G_n[\mathcal P_{n,d}]\succeq0
\]
for every \(n,d\).

This is a theorem target, not an assertion.

---

# 5. New invariant: Reflection Defect

Define the exact defect

\[
\boxed{
\mathfrak D_{n,d}
:=
\mathsf H_{n,d}
-\Pi_{n,d}^{T}\mathcal G_n[\mathcal P_{n,d}]\Pi_{n,d},
}
\]
where \(\Pi_{n,d}\) is chosen by coefficient matching.

Rather than searching blindly for a positive representation of \(\mathsf H_{n,d}\), the computational task becomes:

1. construct \(\Pi_{n,d}\) from the factorial normalization;
2. compute \(\mathfrak D_{n,d}\) exactly;
3. factor it before evaluating any theta numerics;
4. determine whether it is
   - a Vandermonde square,
   - a determinant square,
   - a Pfaffian square,
   - a manifestly positive theta integral,
   - a modular boundary term, or
   - genuinely sign-indefinite.

A sign-indefinite exact defect is a falsification of the current ansatz, not something to be hidden by numerical fitting.

---

# 6. New scalar functional: Theta Hyperbolicity Energy

For each polynomial degree define

\[
\boxed{
\mathscr E_{n,d}(c)
:=
\det\!\left[
\sum_{r=0}^{d-1}c_r\,\mathsf H_{n,d}^{(r)}
\right]
}
\]

where \(\mathsf H_{n,d}^{(r)}\) denotes the appropriate principal Hermite block after the standard Newton reduction.

A more robust form is the quadratic Hermite energy

\[
\boxed{
\mathscr Q_{n,d}(c)=c^T\mathsf H_{n,d}c.
}
\]

The real-rootedness problem is therefore converted into the existence of an exact theta representation of \(\mathscr Q_{n,d}\) as a sum/integral of squares plus controlled modular remainder.

This avoids introducing roots as variables anywhere in the proof.

---

# 7. Reflection-square mechanism to test

The first nontrivial candidate is the antisymmetric two-copy square

\[
\boxed{
\Delta_p(u,v)
:=
\frac{p(u^2)-p(v^2)}{u^2-v^2}.
}
\]

For polynomial \(p\), \(\Delta_p\) is again polynomial. The associated nonnegative candidate is

\[
\boxed{
\mathscr R^{\square}_{n}[p]
:=
\frac{1}{(2n)!^2}
\iint
(u v)^{2n}
\Phi\!\left(\frac{u+v}{2}\right)
\Phi\!\left(\frac{u-v}{2}\right)
\left|\Delta_p(u,v)\right|^2\,du\,dv.
}
\]

This quantity is manifestly nonnegative whenever the integrand is defined, and the quotient is polynomial because the numerator is divisible by \(u^2-v^2\).

The central algebraic test is whether the Hermite minors can be written as linear combinations of \(\mathscr R^{\square}_{n}[p]\) and higher divided-difference squares.

This is deliberately stronger than a single Vandermonde factor: it uses the complete two-copy reflection geometry.

---

# 8. Higher-copy hierarchy

For \(q\ge2\), define divided-difference operators recursively:

\[
D_1p(u,v)=\frac{p(u^2)-p(v^2)}{u^2-v^2},
\]

\[
D_{q+1}p(u_0,\ldots,u_{q+1})
:=
\frac{D_qp(u_0,\ldots,u_q)-D_qp(u_1,\ldots,u_{q+1})}
{u_0^2-u_{q+1}^2}.
\]

Define the q-copy reflection energy

\[
\boxed{
\mathscr R_{n,q}[p]
:=
\int_{\mathbb R^{q+1}}
\left|D_qp(u_0,\ldots,u_q)\right|^2
\,d\mu_{n,q},
}
\]
where the candidate theta measure is constructed from the completed lattice through iterated reflection coordinates.

The conjectural closure has the form

\[
\boxed{
\text{Hermite minors of }J_{n,d}
=
\sum_{q=2}^{d}A_{n,d,q}\,\mathscr R_{n,q}[p]
+\mathscr M_{n,d},
}
\]
with \(A_{n,d,q}\ge0\) and \(\mathscr M_{n,d}\ge0\).

Again, this is the proposed identity to prove or disprove.

---

# 9. New all-degree target theorem: TRG Closure Theorem

The entire RH route would close if the following theorem were established without zero information:

\[
\boxed{
\begin{array}{c}
\textbf{Theta-Reflection Gram Closure}\[2mm]
\forall n,d\ge0:\quad
\mathsf H_{n,d}
=\mathsf P_{n,d}+\mathsf M_{n,d},\\
\mathsf P_{n,d}\succeq0,\quad
\mathsf M_{n,d}\succeq0,
\end{array}}
\]

where both terms are given explicitly by finite sums of squared divided differences against the unsummed completed theta lattice.

Then

\[
\mathsf H_{n,d}\succeq0
\Longrightarrow
J_{n,d}\text{ hyperbolic}
\]
for every \(n,d\).

This is the precise replacement for the invalid implication

\[
\text{pointwise stable integrand}+\text{positive measure}
\not\Rightarrow\text{stable integral}.
\]

---

# 10. Complete proposed chain

The desired chain is now reorganized as

\[
\boxed{
\begin{aligned}
&\text{unsummed completed theta lattice}\\
&\Downarrow\\
&\text{reflection coordinates }(u+v)/2,(u-v)/2\\
&\Downarrow\\
&\text{Theta-Reflection Lift }\mathfrak L_n\\
&\Downarrow\\
&\text{divided-difference square hierarchy }D_q\\
&\Downarrow\\
&\text{Theta-Reflection Gram Closure}\\
&\Downarrow\\
&\mathsf H_{n,d}\succeq0\quad\forall n,d\\
&\Downarrow\\
&J_{n,d}\text{ hyperbolic}\quad\forall n,d\\
&\Downarrow\\
&\Xi\in\mathrm{LP}\\
&\Downarrow\\
&\text{all nontrivial zeros of }\Xi\text{ are real}\\
&\Downarrow\\
&\Re\rho=\frac12\\
&\Downarrow\\
&\mathrm{RH}.
\end{aligned}}
\]

Only the first implication through Gram closure is new. The last implications still require their standard rigorous theorem statements and normalization checks.

---

# 11. Immediate exact experiments

The next computations are not optional:

### Experiment A — cubic

Compute \(\mathfrak D_{n,3}\) symbolically in \(\gamma_n,\gamma_{n+1},\gamma_{n+2},\gamma_{n+3}\), then substitute the unsummed theta moments. Determine whether the residual is a two-copy divided-difference square.

### Experiment B — quartic

Compute every principal Hermite minor for \(J_{n,4}\). Expand each through four independent theta copies. Search for exact square completion.

### Experiment C — modular transformation

Apply Poisson/Jacobi transformation before reducing the two-copy kernel. Compare the transformed reflection remainder with the untransformed defect.

### Experiment D — falsification

Run the same proposed identity on arbitrary positive measures. If it fails there but survives the completed theta lattice, the surviving term is genuinely theta-specific.

### Experiment E — all-degree coefficient recurrence

Determine whether the square coefficients \(A_{n,d,q}\) obey a positive recurrence in \(d\). A closed positive recurrence would be the route from finite-degree discovery to a theorem for every degree.

---

# 12. Non-circularity certificate

Any successful closure must satisfy all of the following:

1. No notation \(\rho=1/2+i\gamma\) appears before the final zero theorem.
2. No zero sum or zero ordinate is used in constructing \(\mathfrak L_n\).
3. All positivity comes from explicit squares, PSD matrices, or pointwise nonnegative kernels.
4. Every Poisson/Jacobi step is an identity on the theta lattice, not an asymptotic assertion.
5. Every finite-degree identity is checked symbolically before being generalized.
6. The all-degree step must be a proved recurrence, determinant identity, operator theorem, or uniform factorization.

---

# 13. Exact completion criterion

This frontier must not be labeled an RH proof unless one proves

\[
\boxed{
\forall n,d:\quad
\mathsf H_{n,d}\succeq0
}
\]
from the unsummed theta lattice and then supplies the full Jensen-to-LP-to-Xi-to-RH bridge.

At present, this document supplies a **new candidate architecture and exact test objects**, not that missing theorem.
