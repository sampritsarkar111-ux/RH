# Frontier 81 — operator-intertwining endgame

Date: 2026-09-16

## Goal

The preceding analysis shows that the factorial multiplier
\[
a_n=\frac{n!}{(2n)!}
\]
cannot be replaced by a fixed positive measure. The correct question is therefore operator-theoretic: can the theta moment sequence be placed in a class on which the multiplier is real-zero preserving?

Let
\[
B(z)=\sum_{n\ge0}M_n\frac{z^n}{n!},
\qquad
(T_aB)(z)=\sum_{n\ge0}a_nM_n\frac{z^n}{n!}.
\]
Then
\[
T_aB(z)=\sum_{n\ge0}M_n\frac{z^n}{(2n)!}
=\Xi(\sqrt{-z})
\]
with the standard even-variable branch interpretation.

## Exact multiplier symbol

The exponential generating symbol of \(a_n\) is
\[
\sum_{n\ge0}a_n\frac{z^n}{n!}
=\sum_{n\ge0}\frac{z^n}{(2n)!}
=\cosh\sqrt z.
\]
Its zeros are
\[
z=-\pi^2\left(k+\frac12\right)^2,
\qquad k\in\mathbb Z,
\]
so the symbol itself belongs to the real-zero side of the classical multiplier-sequence picture.

## Critical obstruction

The general multiplier-sequence theorem does not imply that \(T_a\) maps every positive moment EGF to an LP function. Indeed, for the theta moment sequence the quadratic Jensen polynomial of \(B\) has the sign corresponding to log-convexity,
\[
M_{n+1}^2-M_nM_{n+2}\le0,
\]
while the canonical coefficients require the factorial-corrected inequality
\[
M_{n+1}^2-\frac{2n+1}{2n+3}M_nM_{n+2}\ge0.
\]
Thus the missing theorem must use the specific theta structure of \(B\), not merely positivity of its representing measure.

## New exact research target

Construct an intertwining relation
\[
\boxed{
\mathscr A\,B=\mathscr C\,(T_aB)
}
\]
where \(\mathscr A\) is an operator determined directly by the theta functional equation and \(\mathscr C\) is a real-zero/interlacing-preserving operator. A successful identity would convert modular structure into the missing canonical Jensen inequalities.

Necessary verification gates:

1. derive \(\mathscr A,\mathscr C\) exactly from the theta equation;
2. prove the operator domains and convergence;
3. prove the preservation/interlacing theorem independently of RH;
4. show the relation holds for all shifts \(n\), not only the base sequence;
5. deduce hyperbolicity for every finite Jensen degree;
6. invoke the exact Jensen-to-RH equivalence.

## Status

This is a sharpened endgame, not a proof. No operator intertwining theorem satisfying all six gates has yet been established.
