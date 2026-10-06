# Corners and inherited normal functionals

*Retained original OA-MOD-CP-11 proof under its exact published CC0 component grant. Scoped selection and bindings by GPT-6.1 Sol (OpenAI), Ultra, October 2026. The original manuscript names its OA-MOD-CP authorship and supplies no individual model attribution in this excerpt.*

This is the complete corner-predual statement used by the normal-products lesson. The published trace-class/predual chapter, Theorems 6.2 and 9.4, supplies vector-series descriptions, relative ultraweak topology, completeness and isometric duality. The companion spatial tensor supplement, Proposition 3.1, gives an alternative vector-series construction. This proof applies to every projection, including zero and noncentral projections. The statement concerns inherited normal functionals on a corner.

<a id="OA-MOD-CP-11"></a>
## OA-MOD-CP-11 — Corners have exactly their inherited predual

Let \(p\in M\) be a projection and let \(N=pMp\) act on \(pH\). It is a concrete von Neumann algebra there. To verify closedness, extend a weak operator convergent net on \(pH\) by zero on \((1-p)H\). The extensions converge weakly on \(H\), so a net from \(pMp\) has its limit in \(M\) and still satisfies \(x=pxp\).

Let \(j:N\to M\) be this inclusion, and let \(C:M\to N\) be \(C(x)=pxp\). Both are contractions and \(Cj=\operatorname{id}_N\). A vector-series functional on \(N\) extends through \(C\) using the same sequences in \(H\). Restricting a series from \(M\) through \(j\) replaces both vector sequences by their images under \(p\). Hence the ultraweak topology on \(N\) is exactly the inherited topology.

The maps
\[
r:M_*\to N_*,\quad r(f)=f\circ j,\qquad
s:N_*\to M_*,\quad s(g)=g\circ C
\]
are contractions, \(rs=1\), and \(s\) is isometric: restriction gives the reverse norm inequality. They preserve positivity. Every \(g\in N_*\) has an extension of exactly its norm, and therefore
\[
N_*\cong M_*/\ker r
\cong\operatorname{ran}P_*,
\qquad P_*f(x)=f(pxp),
\tag{CP.17}
\]
isometrically, where \(P_*=sr\) is a contractive idempotent. The second identification uses \(s\); a quotient is not identified with a subspace without a specified map.
