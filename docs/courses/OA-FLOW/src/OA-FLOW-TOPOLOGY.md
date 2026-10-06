
<a id="oa-flow.hr.topology"></a><a id="oa-flow.xgaps.cstar.h0"></a>

# Compact topology and the Hilbert tensor construction

*Original CC0 proof. This independent topology slice has no Haar, Plancherel, group-C\* or crossed-product premise. Earlier inputs: CF choice/scalar primitives, compact Stone-Weierstrass (Section 5), and CF Section 8/Hilbert completion (Section 10).*

A continuous image of a compact space is compact: pull back an open cover, take its finite subcover, and push it forward. A compact subset of a Hausdorff space is closed: for a point outside it, separate that point from each member, retain finitely many neighbourhoods covering the compact set, and intersect their disjoint neighbourhoods of the outside point. Products and compact projections below use these facts.

<a id="l138-h0"></a>
## H0. Cutoffs, compact partitions and product approximation

We prove the topology used later. In a compact Hausdorff space, a point and a disjoint closed set have disjoint neighbourhoods: separate the point from each member of that compact set, and retain a finite subcover. Two disjoint closed sets then have disjoint neighbourhoods by a second finite-cover argument. Thus compact Hausdorff spaces are normal. Consequently, for a closed \(F\subset O\) with \(O\) open, there is open \(V\) with \(F\subset V\subset\overline V\subset O\): separate \(F\) and the complement of \(O\).

Here is the continuous separation construction. Choose open sets \(V_r\), indexed by dyadic \(r\in[0,1]\), so that \(F\subset V_0\), \(V_1=O\), and \(\overline{V_r}\subset V_s\) whenever \(r<s\). Construct the successive midpoints using the preceding shrinking property. Set
\[
 u(x)=\inf\bigl(\{r:x\in V_r\}\cup\{1\}\bigr).
\]
For \(0<t<1\), the set \(u<t\) is the union of \(V_r\) for \(r<t\); the set \(u>t\) is the union of the complements of \(\overline{V_r}\) for \(r>t\). These equalities follow from the nested closures and the density of dyadics. They prove continuity. Thus \(1-u\) is one on \(F\), zero outside \(O\), and takes values in \([0,1]\).

For an LCH space \(X\), a point in an open \(O\) has a neighbourhood with compact closure inside \(O\). To see this, first take an open neighbourhood with compact closure \(C\), then shrink in the compact Hausdorff space \(C\), inside its relative open intersection with \(O\) and the original neighbourhood. Compactness gives the same shrinking for a compact \(F\subset O\) by a finite union. The one-point compactification \(X^+=X\cup\{\infty\}\) is compact Hausdorff: neighbourhoods of infinity are complements of compact sets; a cover member containing infinity leaves a compact set to cover finitely; the shrinking just proved separates a point from infinity. This construction also works when \(X\) is compact, making infinity isolated. Apply the compact separation construction in \(X^+\) with an open relatively compact neighbourhood of \(F\) whose closure lies in \(O\). Its restriction gives
\[
 0\le h\le1,\qquad h|_F=1,\qquad h\in C_c(X),\qquad\operatorname{supp}h\subset O.
\tag{H0.1}
\]

If \(K\subset X\) is compact and \(U_1,\ldots,U_n\) cover it, choose finitely many compactly supported nonnegative cutoffs \(b_j\) subordinate to these sets whose sum \(b\) is positive on \(K\). Choose \(\kappa\in C_c(X)\) equal to one on \(K\), with support inside \(\{b>0\}\). Define \(h_j=\kappa b_j/b\) there and zero elsewhere. They are continuous, nonnegative, compactly supported, subordinate to the respective \(U_j\), and
\[
 \sum_jh_j=1\text{ on }K,\qquad\sum_jh_j\le1\text{ on }X.
\tag{H0.2}
\]
Repeated indices can be combined. The same partition approximates a continuous Banach-valued field \(v\) uniformly on \(K\) by \(\sum_jv(x_j)h_j\), where each \(U_j\) is chosen to make \(\|v(x)-v(x_j)\|<\varepsilon\). Its error on \(K\) is at most \(\varepsilon\), independently of the number of pieces.

Finite products of compact spaces are compact: for a cover of \(K\times L\), finitely many rectangle refinements cover each fibre \(\{x\}\times L\); their first-coordinate intersection gives a neighbourhood of \(x\) whose whole fibre strip has a finite cover. Finitely many such neighbourhoods cover \(K\). Induction handles more factors.

On compact \(K\times L\), the span of products \(u(x)v(y)\), with factors continuous on the respective compact sets, is uniformly dense by CF Section 5: it is a unital self-adjoint algebra separating pairs of points. For functions on LCH spaces one can use factors in \(C_c\), and retain common compact support. Indeed, choose fixed compact cutoffs equal to one on a given compact rectangle and larger compact support rectangles. On the larger rectangle their \(C_c\) restrictions, together with constants, separate points by ([H0.1](OA-FLOW-TOPOLOGY.md#l138-h0)); CF Section 5 applies. Multiply the approximants by the fixed two cutoffs. The error remains uniformly small everywhere, because the target is zero off the smaller support and both approximant and target are supported in the larger rectangle. The same finite partition of a compact image proves compact-support approximation of Banach-valued functions by finite scalar functions times fixed vectors. These constructions use finite covers, not a countable exhaustion.

We also fix the abstract Hilbert tensor construction, so that an older tensor theorem is not an additional input. For arbitrary Hilbert spaces \(E,F\), take the algebraic tensor product, defined by the bilinear relations, and set
\[
 \left\langle\sum_i x_i\otimes y_i,\sum_j x'_j\otimes y'_j\right\rangle
 =\sum_{i,j}\langle x_i,x'_j\rangle\langle y_i,y'_j\rangle.
\tag{H0.3}
\]
The formula respects those relations in each variable. Express the finitely many \(y_i\) in an orthonormal basis \(e_1,\ldots,e_n\) of their finite-dimensional span, obtained by successive subtraction of orthogonal projections and normalization. The tensor becomes \(\sum_l v_l\otimes e_l\) and its squared norm is \(\sum_l\|v_l\|^2\). If it is zero, every \(v_l=0\), so the original algebraic tensor is zero. This proves positive definiteness. CF Section 10 gives its Hilbert completion, denoted \(E\otimes F\). Flipping or associating finite tensors preserves their inner products; the inverse rules and density extend these to unitary identifications. A unitary tensored with an identity is likewise unitary. For a bounded \(T\), orthonormal expansion in the unchanged factor proves \(\|T\otimes1\|\le\|T\|\); if that factor is nonzero, a single unit vector gives the reverse inequality. This proves the amplification assertions needed below on arbitrary Hilbert spaces.
