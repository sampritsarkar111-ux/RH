# Frontier 169 — Parallel Closure Results — 2026-09-17

## Scope

This frontier executes the remaining proof-bearing routes in parallel: Stieltjes/Pick, tau-Hankel, Jensen/Hermite, de Branges/spectral, Li/Weil, and Nyman–Beurling. The purpose is to close a route only when its universal theorem is actually proved. No numerical result is promoted to an RH proof.

## 1. Canonical master gate

Let

\[
\Xi(w)=\xi(1/2+w),\qquad H(z)=\Xi(\sqrt z).
\]

Then RH is equivalent to every zero of H being real and nonpositive. A sufficient zero-location-free target is

\[
\frac{H'(z)}{H(z)}=a+\int_{[0,\infty)}\frac{d\mu(t)}{z+t},\qquad \mu\ge0,
\]

with all analytic, growth, and interchange conditions proved directly from theta structure.

## 2. Jensen/Hermite calculation actually completed

For a cubic

\[
J(x)=g_0+3g_1x+3g_2x^2+g_3x^3,
\]

write its monic form as

\[
p(x)=x^3+a x^2+b x+c,
\qquad a=3g_2/g_3,\ b=3g_1/g_3,\ c=g_0/g_3.
\]

Its Hermite matrix \(\mathcal H=[s_{i+j}]_{i,j=0}^2\), with Newton sums, has principal minors

\[
\Delta_1=3,
\]

\[
\Delta_2=\frac{18(g_2^2-g_1g_3)}{g_3^2},
\]

\[
\Delta_{13}=\frac{18(9g_2^4-12g_1g_2^2g_3+g_1^2g_3^2+2g_0g_2g_3^2)}{g_3^4},
\]

\[
\Delta_{23}=\frac{9(9g_1^2g_2^2-6g_0g_2^3-12g_1^3g_3+10g_0g_1g_2g_3-g_0^2g_3^2)}{g_3^4},
\]

and

\[
\det\mathcal H=
\frac{27(3g_1^2g_2^2-4g_0g_2^3-4g_1^3g_3+6g_0g_1g_2g_3-g_0^2g_3^2)}{g_3^4}.
\]

Thus the degree-three closure problem is reduced exactly to proving the corresponding Hermite principal-minor inequalities for the Riemann Jensen coefficients. This is an algebraic reduction, not yet a proof of those inequalities.

## 3. Stieltjes/tau-Hankel audit

The existing high-precision diagnostic ledger gives alternating coefficients for \(H'/H\) and positive determinants for the first small factorial-Hankel blocks. These are finite numerical observations only. No theta-derived Gram/SOS identity has been found that proves all Hankel blocks PSD, and no Stieltjes representation has been derived.

## 4. Pick/Weyl audit

The previous pointwise Pick-kernel construction is sign-indefinite. The remaining proof-bearing target is therefore a modular-orbit paired finite-truncation identity with a uniform tail bound. No such identity has been proved in this execution.

## 5. de Branges/spectral audit

A formal self-adjoint operator is insufficient. The required chain remains: exact Hilbert space and domain → self-adjointness → spectral control → rigorously defined determinant → exact determinant identity with Xi. No candidate currently satisfies the full chain unconditionally.

## 6. Li/Weil and Nyman–Beurling

Both routes remain equivalence-based unless the required universal positivity/coercivity theorem is established. Finite Gram matrices and computed Li coefficients are diagnostics and cannot close the infinite statement.

## 7. Research literature cross-check

SciSpace retrieval confirms the classical Jensen–Pólya route: RH is equivalent to hyperbolicity of all relevant Jensen polynomials, while known work establishes eventual hyperbolicity and finite-degree results. This confirms that the unresolved part is the uniform all-degree/all-shift theorem, not the finite cases.

## 8. Verdict

**No complete RH proof was obtained in Frontier 169.** The strongest concrete new result is the exact cubic Hermite certificate above, which converts the first nontrivial all-degree Jensen case into explicit polynomial inequalities. The universal theta-specific identity needed to prove those inequalities, or an equivalent master Stieltjes/spectral theorem, remains open.

## Acceptance gate

A future frontier may claim RH only after proving one unconditional universal theorem implying that every nontrivial zero of Xi has real spectral parameter (equivalently, every zero of H lies on \((-\infty,0]\)), with all limits, sums, integrals, determinants, and domain assertions justified and without assuming RH.