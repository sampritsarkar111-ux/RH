# Frontier 63 — Global route audit: de Bruijn-Newman / kernel positivity

Date: 2026-09-16

## Target

Seek a direct proof that the de Bruijn-Newman parameter satisfies Lambda <= 0, which together with the known unconditional lower bound Lambda >= 0 would imply Lambda=0 and hence RH.

## Necessary bridge

A proof cannot stop at strict log-concavity (TP2). The required endpoint is a global real-zero/Laguerre-Pólya statement, or an equivalent theorem proving Lambda <= 0. Any argument that uses finite-order Toeplitz/Jensen positivity must explain how the order tends to infinity or how a separate global mechanism replaces that limit.

## Audit variables

For Xi_lambda(z)=integral Phi(u) exp(lambda u^2) exp(i z u) du, investigate:

1. exact heat equation and zero-motion identities;
2. a Lyapunov/dissipation functional whose sign is uniform in lambda near 0;
3. boundary behavior as |u| -> infinity;
4. preservation of positivity under the backward heat flow;
5. whether any claimed dissipation estimate genuinely implies Lambda <= 0 rather than only finite-degree hyperbolicity.

## Falsification requirements

Any proposed global inequality must be checked against the exact theta-kernel series and must include tail bounds and all parameter ranges. Numerical interval certification may support a lemma on a compact domain but cannot replace an analytic treatment of the infinite tail unless the truncation error is rigorously bounded.

## Current status

No verified Lambda=0 proof has been established in this branch. This frontier is an explicit attack plan, not a solved theorem.