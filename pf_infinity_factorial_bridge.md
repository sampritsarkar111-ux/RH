# PF∞–Factorial Bridge: all-order RH attack

## Status
This is a research program, not a claimed proof of RH. Exact factorial identities below are proved; the theta-to-PF∞ bridge remains open.

## 1. Canonical factorial gauge
For K_n(i,j)=1/(n+i+j)! with i,j=0,...,d-1,

\[
\boxed{\det K_n=(-1)^{d(d-1)/2}\frac{\prod_{i<j}(j-i)}{\prod_{i=0}^{d-1}(n+i+d-1)!}.}
\]

Multiply row i by (-1)^i. Since product_i (-1)^i=(-1)^{d(d-1)/2}, the gauged consecutive determinant is strictly positive:

\[
\boxed{\det[(-1)^iK_n(i,j)]_{i,j=0}^{d-1}>0.}
\]

This identifies a natural checkerboard gauge before testing positivity.

## 2. New target: PF∞ rather than one Gram determinant
Let Xi(t) be the completed Riemann Xi function, normalized so RH is equivalent to all zeros of Xi(t) being real. Write

\[
\Xi(t)=\sum_{m\ge0}(-1)^m c_m\frac{t^{2m}}{(2m)!}.
\]

Define the factorial-gauged coefficient kernel

\[
\boxed{\mathcal F_{ij}=(-1)^i\frac{c_{i+j}}{(i+j)!}.}
\]

The proposed target is not merely positive semidefiniteness. It is positivity of all finite minors after the canonical sign gauge: an all-order PF∞/sign-regular structure.

## 3. Theta-lattice factorization target
Starting from the UNSUMMED completed theta lattice, seek

\[
\boxed{\mathcal F_{ij}=\sum_r w_r u_r(i)u_r(j),\qquad w_r\ge0,}
\]

with every finite minor of the sequence matrix u having one fixed sign after the same gauge. Then Cauchy–Binet gives

\[
\boxed{\det\mathcal F_{[d]}=\sum_{r_0<\cdots<r_{d-1}}\Big(\prod_a w_{r_a}\Big)\det[u_{r_a}(i)]\det[u_{r_a}(j)]\ge0.}
\]

The crucial point is that positivity would propagate to every order automatically; no separate ad-hoc d×d proof would be needed.

## 4. First genuine obstruction: d=3
For the factorial-normalized coefficients A_m define

\[
D_3=\det\begin{pmatrix}A_0/0!&A_1/1!&A_2/2!\\A_1/1!&A_2/2!&A_3/3!\\A_2/2!&A_3/3!&A_4/4!\end{pmatrix}.
\]

The raw factorial signature requires -D_3 >= 0; the checkerboard-gauged determinant must be >=0.

The decisive experiment/proof target is to insert the actual UNSUMMED completed-theta coefficients, perform Poisson/Jacobi transformation before collapsing the lattice, and derive exactly

\[
\boxed{-D_3=\sum_{r<s<t}W_{rst}Q_{rst},\qquad W_{rst}\ge0,\;Q_{rst}\ge0.}
\]

If an irreducible negative residual remains, that residual is the exact obstruction—not something to hide with numerical evidence.

## 5. All-order theorem to seek
**Factorial-gauged theta PF∞ theorem:** the completed-theta coefficient kernel is strictly PF∞ after the canonical checkerboard factorial gauge.

A successful proof must establish:
1. the exact unsummed completed-theta kernel;
2. Poisson/Jacobi transformation at kernel level;
3. a positive Cauchy–Binet/Andreief expansion with no negative remainder;
4. a rigorous PF∞/Laguerre–Pólya bridge for Xi.

Only all four together can yield RH.

## 6. Falsification rules
Reject or modify the mechanism if: (i) the exact transformed 3×3 determinant has an unavoidable negative remainder; (ii) transformed lattice weights have unavoidable mixed signs; (iii) some finite minor changes sign; or (iv) the resulting PF∞ statement does not imply the required Laguerre–Pólya property under the exact Xi normalization.

## 7. Research position
The factorial determinant and checkerboard gauge are exact. The new PF∞ bridge is a concrete, testable route. It is not yet a solution of RH, and no numerical result will be treated as a proof.
