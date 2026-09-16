# Frontier 52 — Computational certification plan

Date: 2026-09-16

## Purpose

Build a reproducible computational layer that can discover and falsify candidate inequalities without confusing finite evidence with proof.

## Required objects

For each selected n and degree d, compute gamma(n+j), the monic Jensen coefficients, the Hermite matrix, all principal minors, and the polynomial discriminant where appropriate.

## Exact arithmetic policy

Use arbitrary precision and interval/rational certification whenever numerical signs are used to reject or validate a conjectured finite instance. Floating-point agreement alone is not a proof of a sign that is close to zero.

## Discovery tasks

1. Search for sharp bounds on the quartic normalized variables (t,y).
2. Search for recurrence relations in consecutive gamma-ratios.
3. Test candidate total-positivity inequalities at finite truncation.
4. Search for low-degree sum-of-squares decompositions.
5. Compare candidate identities against generic positive atomic measures to identify which hypotheses are genuinely Riemann-specific.

## Proof boundary

A computational certificate can establish an exact finite statement. It cannot establish the universal quantifier over all n and d unless the computation itself is backed by a mathematically complete finite reduction covering those quantifiers.

## Status

Infrastructure target recorded. Universal closure remains open.
