# Frontier 94 — Exact theta modular orbit and degree-two no-go

Date: 2026-09-16

## Objective

Test the sharp target from Frontier 89: derive the theta modular orbit in the original variables and determine whether it can convert the factorial-corrected degree-two Jensen kernel into a manifestly nonnegative quadratic form.

The result is an exact obstruction to the **naive modular-orbit pairing mechanism**. The modular involution acts by reflection of the logarithmic theta variable, while the beta variable is unchanged (or may be reflected by the independent beta symmetry). The scale variable
\[
y=x(1-x)u^2
\]
is therefore invariant. Consequently the factorial-corrected degree-two kernel is itself invariant under the orbit and cannot acquire a new sign from orbit pairing.

This does **not** rule out every modular/operator proof. It rules out the specific strategy in which the modular involution alone pairs a negative kernel value with a transformed positive value or turns the kernel into a square.

## 1. Original theta variable and modular reflection

Use the standard logarithmic variable
\[
t=e^{4u}.
\]
The theta/Mellin representation of the xi-function has kernel
\[
\Phi(u)=\sum_{m\ge1}\left(2\pi^2m^4e^{9u}-3\pi m^2e^{5u}\right)e^{-\pi m^2e^{4u}}.
\]
Poisson summation gives the exact symmetry
\[
\boxed{\Phi(-u)=\Phi(u).}
\]
Equivalently, the underlying theta modular transformation is the inversion
\[
t\longmapsto t^{-1},
\]
which is
\[
\boxed{u\longmapsto-u.}
\]
This is the relevant orbit map after passing to logarithmic theta scale.

The beta variable has the independent involution
\[
\boxed{x\longmapsto1-x},
\]
and therefore
\[
x(1-x)\longmapsto(1-x)x=x(1-x).
\]

Hence the combined natural involution is
\[
\boxed{T(x,u)=(1-x,-u)}
\]
(or simply \((x,u)\mapsto(x,-u)\) if the beta symmetry is not used).
Its Jacobian has absolute value one.

## 2. The crucial invariant

The scale entering the moment representation is
\[
\boxed{y(x,u)=x(1-x)u^2.}
\]
Under the exact orbit,
\[
y(T(x,u))
=(1-x)x(-u)^2
=x(1-x)u^2
=y(x,u).
\]
Thus
\[
\boxed{y\circ T=y.}
\]
Every polynomial in y, including every power \(y^n\), is invariant.

Therefore the factorial-corrected degree-two kernel
\[
K_n(y_1,y_2)
=c_{n+1}^2y_1y_2-\frac{c_nc_{n+2}}2(y_1^2+y_2^2),
\qquad
c_k=\frac{2k+1}{k!},
\]
satisfies
\[
\boxed{K_n(y(Tz_1),y(Tz_2))=K_n(y(z_1),y(z_2)).}
\]

## 3. Orbit pairing cannot create positivity

Suppose one attempts the proposed two-orbit certificate
\[
W(z_1,z_2)K_n(z_1,z_2)
+W(Tz_1,Tz_2)K_n(Tz_1,Tz_2)
=Q_n(z_1,z_2)^2
\]
with a positive T-invariant weight \(W\). Since both y and K are T-invariant,
\[
W(Tz_1,Tz_2)K_n(Tz_1,Tz_2)=W(z_1,z_2)K_n(z_1,z_2),
\]
so the left side is simply
\[
\boxed{2W(z_1,z_2)K_n(z_1,z_2).}
\]
It therefore has exactly the same sign as K_n.

Consequently, the modular reflection cannot turn the degree-two kernel into a pointwise square unless K_n was already nonnegative on the entire positive scale quadrant.

## 4. Exact sign obstruction

Put
\[
r=\frac{y_1}{y_2}>0,
\qquad
R_n=\frac{c_{n+1}^2}{c_nc_{n+2}}
=\frac{(2n+3)^2}{(2n+1)(2n+5)}>1.
\]
Then
\[
K_n(y_1,y_2)
=y_2^2c_nc_{n+2}\left(R_nr-\frac{r^2+1}{2}\right).
\]
Hence
\[
K_n\ge0
\iff
r^2-2R_nr+1\le0.
\]
The positivity interval is exactly
\[
\boxed{
R_n-\sqrt{R_n^2-1}\le r\le R_n+\sqrt{R_n^2-1}.
}
\]
For
\[
r>R_n+\sqrt{R_n^2-1}
\]
or sufficiently small positive r, one has
\[
\boxed{K_n<0.}
\]
Since the modular orbit leaves r unchanged, it leaves this negative region unchanged.

## 5. Strong conclusion from the calculation

The proposed breakthrough mechanism
\[
\text{modular orbit}\;\Rightarrow\;\text{pair negative kernel with transformed positive kernel}
\]
is impossible for the natural theta modular involution acting on the original variables, because the orbit preserves the exact scale variable y on which the kernel depends.

Likewise, the beta reflection x\mapsto1-x provides no new sign: it also preserves x(1-x).

Therefore the degree-two obstruction is **not** a missing clever algebraic pairing under the basic modular involution.

## 6. What remains genuinely viable

The calculation leaves three substantially stronger possibilities:

1. **Nonlocal modular transfer:** the modular transformation must be used before collapsing the theta sum to the scalar invariant y, producing a genuinely different positive kernel rather than merely reflecting y.

2. **Operator/Hermite factorization:** construct directly
\[
\mathsf H_{d,n}=A_{d,n}^*G_{d,n}A_{d,n},\qquad G_{d,n}\succeq0,
\]
where the theta modular operator enters G rather than acting as a pointwise orbit on y.

3. **Variation-diminishing theta transform:** prove that the actual theta kernel, viewed as an integral transform in the scale variable, preserves the relevant Laguerre/Jensen cone. This must be a theta-specific total-positivity or interlacing theorem; generic positive mixing is insufficient.

The first possibility is the most direct continuation: retain the unsummed theta lattice index m and apply Poisson summation before forming the two-copy determinant. The target is a new double lattice expression whose transformed variables are not functions only of y_i.

## 7. Status

**Rigorous obstruction, not a proof of RH.** The natural modular orbit has been identified and its action on the exact factorial-corrected degree-two kernel has been evaluated. It does not produce the desired positive quadratic form. The next high-value attack is therefore the unsummed theta-lattice/operator level, not another attempt to pair the already-collapsed y-kernel by u\mapsto-u.
