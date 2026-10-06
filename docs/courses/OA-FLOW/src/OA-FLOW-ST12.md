# Concrete predual balls and faithful ultraweak representations

*Fresh local proof by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights in this exposition.*

This earlier portion proves ST-1–2 for arbitrary Hilbert spaces and faithful ultraweakly continuous representations. The faithful-state GNS/modular application ST-3 is a later separate lesson. No modular or arbitrary-weight theorem is an input here.

The precise earlier inputs are [CF Section 1](OA-FLOW-CF.md#OA-FLOW.CF.1), [CF Section 4](OA-FLOW-CF.md#OA-FLOW.CF.4), [CF Sections 6–7](OA-FLOW-CF.md#OA-FLOW.CF.6), [GNS Sections 2–5](OA-FLOW-GNS.md#gns-positive-form), [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0)/[SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0), [SF-2](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-2), [CP-01–06](OA-FLOW-CP.md#oa-flow.cp.1), and [BD-4–5](OA-FLOW-BD.md#oa-flow.bd.4). Only the six proved concrete-predual items are used; no CP support or arbitrary-weight descendants are premises.

For clarity, the entire CP contract used here is this: the completion of the projective-norm algebraic tensor \(H\otimes\overline H\) has dual \(B(H)\), via vector pairings; every completed tensor is an absolutely summable pure-tensor series, whose factors may be balanced into two square-summable sequences. Quotienting by the annihilator of a concrete von Neumann algebra \(M\) gives a Banach space \(M_*\), isometric to the vector-series functionals in \(M^*\), with \(M=(M_*)^*\). In particular \(M_*\) is norm closed in \(M^*\). These statements are proved, including tensor norm, completion, quotient and annihilator arguments, in the exact CP range just identified; a source-history judgment is separate from this mathematical proof binding.

<a id="oa-flow.st.1"></a>

## ST-1. Compact balls and a useful linear criterion

For any normed space \(E\), place the closed unit ball of \(E^*\) in
\[
\prod_{e\in E}\{z\in\mathbb C:|z|\leq\|e\|\}
\]
by evaluation. Each coordinate disc is compact, including a radius-zero disc. The arbitrary product is compact by the ultrafilter proof in CF Section 4, from the maximal principle proved in CF Section 1. The linearity equations are closed conditions on finitely many coordinates. Their solutions are exactly the functionals of norm at most one, so the dual ball is closed and compact in this product. The inherited topology is precisely the weak-star topology. Thus the unit ball of \(M\) is ultraweakly compact by the concrete duality just bound. This supplies a complete local compactness argument, rather than invoking the inherited WT compactness dependency.

We also need the following linear criterion. Let \(E\) be Banach, \(X=E^*\), and \(f\in X^*\). If \(f|_{B_X}\) is weak-star continuous at zero, then \(f\) belongs to the canonical copy of \(E\) in \(X^*\).

For \(\varepsilon>0\), continuity supplies \(e_1,\ldots,e_n\in E\) and \(\delta>0\) such that \(|f(x)|\leq\varepsilon\) whenever \(\|x\|\leq1\) and \(|x(e_j)|<\delta\) for all \(j\). Put \(K=\bigcap_j\ker e_j\), with \(e_j\) viewed as a functional on \(X\). Then \(\|f|_K\|\leq\varepsilon\). Hahn–Banach extends \(f|_K\) to \(h\in X^*\) with \(\|h\|\leq\varepsilon\). The functional \(f-h\) vanishes on \(K\), so it factors through the finite-dimensional map \(x\mapsto(x(e_j))_j\). Extending its linear functional on the image to \(\mathbb C^n\) gives
\[
f-h\in\operatorname{span}\{e_1,\ldots,e_n\}\subseteq E.
\tag{ST1}
\]
Thus \(f\) has distance at most \(\varepsilon\) from \(E\). The canonical inclusion \(E\to E^{**}\) is isometric by the norming Hahn–Banach identity in CF Section 1; completeness makes its range closed. Letting \(\varepsilon\downarrow0\) proves the criterion. It is a criterion for linear functionals and is not a general theorem about arbitrary convex sets.

<a id="oa-flow.st.2"></a>

## ST-2. An ultraweakly continuous faithful representation

Suppose \(\pi:M\to B(K)\) is a faithful \*-representation and is ultraweakly continuous. Put \(p=\pi(1)\) and work on \(pK\). It is isometric: contractivity is the C\* estimate in GNS Section 3, and if a positive \(b\) lost norm, choose a continuous scalar function zero on \([0,\|\pi(b)\|]\) but nonzero at \(\|b\|\). Continuous functional calculus would give \(f(b)\ne0\) but \(\pi(f(b))=0\). Applying positive norm preservation to \(x^*x\) gives the assertion for every \(x\). Therefore \(A=\pi(M)\) is a C\* algebra and \(\pi(B_M)=B_A\).

The last ball is ultraweakly compact by ST-1 and continuity, hence closed in the Hausdorff ultraweak topology. By BD-4, every contraction in \(A''\subseteq B(pK)\) is a bounded strong limit of contractions in \(A\). BD-5 proves ultraweak convergence of that net, so compact-ball closedness puts its limit back in \(A\). Thus \(A=A''\). Compression shows it is also ultraweakly closed in \(B(K)\): all limits stay compressed by \(p\), and restricting vector-series tests gives exactly the corner topology.

On the unit balls, \(\pi\) is a continuous bijection from a compact space to a Hausdorff space and hence a homeomorphism. Explicitly a closed subset of the compact ball is compact, its image is compact and therefore closed, proving continuity of the inverse without an additional topological theorem. For \(\omega\in M_*\), the bounded linear functional \(f=\omega\circ\pi^{-1}\) on \(A\) is continuous on \(B_A\). Applying ST-1's criterion to \(A=(A_*)^*\) proves \(f\in A_*\). This holds for every \(\omega\), so \(\pi^{-1}\) is ultraweakly continuous on all of \(A\), not merely on a ball.

Positive normal functionals pull back in both directions, preserving positivity, and
\[
(\omega\circ\pi^{-1})(\pi(x)^*\pi(x))=\omega(x^*x).
\tag{ST2}
\]
These equalities give both directions of the intrinsic \(\sigma\)-strong topology, and applying them also to \(x^*\) gives the \(\sigma\)-strong* topology. On uniformly norm-bounded sets these are the concrete strong and strong* topologies. Here is the full comparison: each positive normal \(\omega\) has a vector series \(\sum_j\langle x u_j,v_j\rangle\); for \(b\geq0\), Cauchy–Schwarz for \(b^{1/2}\) gives
\[
0\leq\omega(b)\leq
\frac12\sum_j\bigl(\langle b u_j,u_j\rangle+\langle b v_j,v_j\rangle\bigr).
\tag{ST3}
\]
At \(b=z^*z\), the right side is a sum of squared vector norms. A uniformly bounded strongly null net makes its finite initial sum tend to zero and its tail uniformly small. Conversely, the positive single-vector tests are among the defining seminorms. Repeat for adjoints. For the weak topology, a bounded weakly convergent net makes each finite initial vector-coefficient sum converge, and the same Cauchy–Schwarz tail bound as BD-5 is uniform; hence bounded weak and ultraweak convergence agree. These arguments apply to arbitrary nets.

Thus the complete topology conclusion of WH-02 holds for every faithful ultraweakly continuous representation, on arbitrary Hilbert spaces and with a possibly proper identity corner. The additional equivalence with the order-normal definition for arbitrary positive maps is not asserted by this proof.

