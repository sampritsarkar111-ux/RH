# Frontier 41 — diagonal obstruction to the raw Turan kernel ansatz

For the exact kernel K_m from Frontier 39, the frequently hoped-for form
\[
K_m(x,y)=(x-y)^2R_m(x,y)
\]
would force K_m(x,x)=0 identically. Direct symbolic substitution gives instead
\[
K_m(x,x)=\frac{x^{4m}}{(m+2)(2m+3)}P_m(x^2),
\]
where
\[
P_m(X)=4096m^5+21504m^4-256m^3X+40960m^3-576m^2X+34560m^2
+4mX^2-416mX+12544m+5X^2-96X+1536.
\]
This is not identically zero. Therefore the raw kernel cannot possess any exact factor (x-y)^2.

This is stronger than merely observing numerical sign changes: it is an exact algebraic obstruction to the proposed difference-square factorization.

Consequently the theta Turan problem requires a different decomposition, such as a positive diagonal component plus a signed off-diagonal component whose integral is controlled by theta-specific structure, or a completely different representation.

Status: exact obstruction; no RH conclusion.
