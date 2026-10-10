# Coordinates, cells and items

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson and the next construct the instance of the graph-to-packing reduction (Theorem 4.1 of [Bin packing and the configuration program](bin-packing-and-the-configuration-program.md)). Here we choose the constants, place two trees of nested intervals and a row of job intervals on the real line for every vertex of the graph, and list every item with its role and a real *coordinate*. The next lesson turns roles, labels and coordinates into rational item sizes. Every item will have size close to \(1/5\), so a bin holds at most five items; the sizes are designed so that a five-item bin of one of four prescribed *patterns* fits exactly when a simple inequality between coordinates holds.

Throughout, \(c\geq0\) is a fixed integer (the allowed number of extra bins) and \(\rho>0\) a fixed real; the input is a simple graph \(G=(V,E)\) with \(V=\{1,\ldots,n\}\), \(m=|E|\geq1\) edges numbered \(e=1,\ldots,m\), and an integer \(0\leq k\leq n\). We use the competing trees of [Two competing trees](two-competing-trees.md) (Lemma 1.1 there) and the prefix identities of the first lesson (Lemma 5.1 there).

## 1. Constants

Put
\[
P_0=100^{11},\qquad K=25(c+1)(1+5P_0),\tag{1.1}
\]
and fix an integer \(d\) with
\[
d\geq\max\{72K,\ 120K/\rho\}.\tag{1.2}
\]
Apply the competing-trees lemma to \(d\): it gives trees \(T^+,T^-\) with all leaves at depth \(L\geq1\), quotas \(p_1,\ldots,p_L\) and separate \(d\)-fold markings. Put \(P=\sum_{\ell=1}^Lp_\ell\), and let \(D_*\geq1\) be an integer bounding the number of children of every vertex of both trees. These numbers depend only on \(c\) and \(\rho\). Finally put
\[
R=100(P+nK+1).\tag{1.3}
\]
The constant \(K\) will bound the number of items that a packing with at most \(c\) extra bins can keep out of the prescribed patterns; \(d\) is large compared with \(K\); and every incidence of an edge with a vertex is repeated \(R\) times, so that edge demands outweigh all losses.

## 2. Positions and their coordinates

A *position* is a pair \(r=(e,j)\) with \(1\leq e\leq m\) and \(1\leq j\leq R\); positions are ordered lexicographically. For a vertex \(v\) let
\[
\mathcal R_v=\{(e,j):v\text{ is an endpoint of }e,\ 1\leq j\leq R\},\qquad|\mathcal R_v|=R\deg(v).
\]
Define
\[
\theta_e=(R+1)^{e-1}-1,\qquad H_{e,j}=j(R+1)^{e-1}-1,\qquad g=\frac1{16(R+1)^m},\tag{2.1}
\]
\[
b_{(e,j)}=\frac12+gH_{e,j},\qquad\beta_e=g\theta_e .\tag{2.2}
\]
We write \(H_r=H_{e,j}\) for \(r=(e,j)\). The number \(b_r\) is the *baseline* of position \(r\), and \(\beta_e\) is the *offset* of edge \(e\).

**Lemma 2.1 (coordinate order).** For a position \(r=(e,j)\):
\[
H_{r'}-H_r\geq\theta_e+1\quad\text{for every position }r'>r,\qquad\theta_f-\theta_e\geq H_{e,R}+1\quad\text{for every edge }f>e.\tag{2.3}
\]
Moreover \(0\leq H_r<(R+1)^m\), so \(b_r\in[\tfrac12,\tfrac9{16})\), consecutive baselines differ by at least \(g\), and \(0\leq\beta_e<\tfrac1{16}\).

*Proof.* Within edge \(e\), consecutive values of \(H\) differ by \((R+1)^{e-1}=\theta_e+1\). From \((e,R)\) to \((e+1,1)\) the difference is \((R+1)^e-1-(R(R+1)^{e-1}-1)=(R+1)^{e-1}\), the same number. Since \(H\) increases along the order and the first step after any position of edge \(e\) is \(\theta_e+1\), and all later steps are positive, the first inequality follows. Next, \(\theta_{e+1}-\theta_e=R(R+1)^{e-1}=H_{e,R}+1\), and \(\theta\) increases with \(e\). Finally \(0\leq H_r\leq R(R+1)^{m-1}-1<(R+1)^m\), so \(0\leq gH_r<1/16\); the steps of \(H\) are at least one, so baselines differ by at least \(g\); and \(\theta_e<(R+1)^m\) gives \(\beta_e<1/16\). \(\square\)

The first inequality says that one step of position outweighs the largest possible offset of an earlier edge; the second that one step of edge offset outweighs every baseline difference within the edge. These two facts will make a later row or a later edge too large for a bin.

## 3. Cells and test intervals

Every vertex \(v\) of \(G\) receives its own copy of the following geometry on the real line; nothing below depends on \(v\) except the set \(\mathcal R_v\).

The roots of \(T^+\) and \(T^-\) are represented by the closed *cells* \([0,1]\) and \([4,5]\). A vertex of depth \(\ell\geq1\) has a cell of width
\[
\lambda_\ell=g\,[100(D_*+1)]^{-\ell},\tag{3.1}
\]
placed as follows: if the parent's cell has left endpoint \(x\) and the vertex is the \(j\)-th child of its parent (\(1\leq j\leq D_*\)), its cell is \([x+4j\lambda_\ell,\ x+(4j+1)\lambda_\ell]\). Put \(\Delta=\lambda_L/10\). For every position \(r\in\mathcal R_v\) the *job cell* is \([b_r-\Delta,b_r]\), regarded as lying on the plus side.

The *test intervals* of \(v\) are the leaf cells of both trees and the job cells, each made half-open by removing its right endpoint. Their union is denoted \(\mathcal I_v\). When we speak of cells meeting or containing each other, cells are closed.

**Lemma 3.1 (geometry).** (a) Every cell of positive depth lies inside the cell of its parent and inside the first tenth of its root cell. Two different cells of the same depth \(\ell\), in the same tree or in different trees, are at distance at least \(3\lambda_\ell\).

(b) Job cells lie in \((\tfrac1{10},\tfrac9{16})\), different job cells are at distance at least \(g-\Delta\), and the test intervals of \(v\) are pairwise disjoint.

(c) \(\Delta\leq\lambda_\ell/10\) for every \(\ell\), and \(\lambda_1+2\Delta<g\). Consequently a closed interval of length at most \(\lambda_\ell+\Delta\) meets at most one cell of depth \(\ell\), and if it contains a point of a leaf cell, that cell of depth \(\ell\) is the leaf's ancestor; and a closed interval of length at most \(\lambda_1+\Delta\) meets at most one job cell.

*Proof.* (a) The last child of a vertex ends at most \((4D_*+1)\lambda_\ell\) to the right of the parent's left endpoint. For \(\ell\geq2\) this is less than \(\lambda_{\ell-1}=100(D_*+1)\lambda_\ell\), so children lie inside their parent. For \(\ell=1\) it is less than \(g/25<1/10\), since \(\lambda_1=g/(100(D_*+1))\) and \(g\leq1/16\). By induction every cell of positive depth lies inside its depth-one ancestor, hence inside the first tenth of its root cell. Consecutive children of one parent are at distance \(3\lambda_\ell\). Cells of depth \(\ell\) with different parents lie inside two different cells of depth \(\ell-1\), which are at distance at least \(3\lambda_{\ell-1}>3\lambda_\ell\) by induction (for \(\ell=1\), the two root cells are at distance \(3\)). The nonroot cells of \(T^+\) lie in \([0,\tfrac1{10}]\) and those of \(T^-\) in \([4,4\tfrac1{10}]\).

(b) By Lemma 2.1, \(b_r\in[\frac12,\frac9{16})\) and consecutive baselines differ by at least \(g\), while \(\Delta<g\leq1/16\) by (c). So job cells lie in \((\frac1{10},\frac9{16})\) and are at distance at least \(g-\Delta>0\). They therefore meet no cell of positive depth. Leaf cells all have depth \(L\) and are pairwise at positive distance by (a). Hence all test intervals are disjoint.

(c) The widths decrease with depth, so \(\Delta=\lambda_L/10\leq\lambda_\ell/10\). Since \(100(D_*+1)\geq200\), \(\lambda_1+2\Delta\leq\frac65\lambda_1\leq\frac{6}{5}\cdot\frac g{200}<g\). A closed interval meeting two cells at distance at least \(3\lambda_\ell\) has length at least \(3\lambda_\ell>\frac{11}{10}\lambda_\ell\geq\lambda_\ell+\Delta\); so an interval of length at most \(\lambda_\ell+\Delta\) meets at most one cell of depth \(\ell\). A leaf cell lies inside its ancestor of depth \(\ell\), so an interval containing a point of the leaf cell meets that ancestor, which is then the only cell of depth \(\ell\) it meets. Finally \(\lambda_1+\Delta<g-\Delta\), the distance between job cells. \(\square\)

## 4. Roles, subclasses and patterns

Every item has one of five *roles*: rows \(X\), anchors \(A\), global auxiliaries \(U\), local auxiliaries \(D\) and flags \(F\). Each role is divided into *subclasses*, thirteen in all:

| role | subclasses |
|---|---|
| row \(X\) | \(T^+\) (plus tree row), \(T^-\) (minus tree row), \(S\) (job row) |
| anchor \(A\) | \(Z\) (deadline), \(Y\) (key) |
| global \(U\) | \(U^+\), \(U^-\), \(W\) (edge resource) |
| local \(D\) | \(D^{\mathrm M}\), \(D^{\mathrm G}\) |
| flag \(F\) | \(F^{\mathrm T}\), \(F^{\mathrm M}\), \(F^{\mathrm G}\) |

Rows, anchors and local auxiliaries carry a *label*, a vertex of \(G\); global auxiliaries and flags carry none. A *tuple* is a set of five distinct items. A *table tuple* has one item of each role, with subclasses as in one of the four *patterns*

| kind | \(X\) | \(A\) | \(U\) | \(D\) | \(F\) |
|---|---|---|---|---|---|
| M | \(T^+\) | \(Z\) | \(U^+\) | \(D^{\mathrm M}\) | \(F^{\mathrm T}\) |
| M | \(T^-\) | \(Z\) | \(U^-\) | \(D^{\mathrm M}\) | \(F^{\mathrm T}\) |
| M | \(S\) | \(Z\) | \(U^+\) | \(D^{\mathrm M}\) | \(F^{\mathrm M}\) |
| G | \(S\) | \(Y\) | \(W\) | \(D^{\mathrm G}\) | \(F^{\mathrm G}\) |

A table tuple is *good* if its row, anchor and local auxiliary have the same label.

A tuple of kind M will compare a row's *completion* with an anchor's *deadline*; a tuple of kind G will match a job row with a key. The flag decides which pattern a tuple must follow, and the remaining subclass constraints make the pattern rigid (next lesson).

## 5. The inventory

We now list all items. Each item gets a role, a subclass, possibly a label, some attributes, and a real *coordinate* \(w(i)\).

**Rows.** For every label \(v\) and every vertex \(x\) of \(T^+\) or of \(T^-\), *including the roots*, create \(d\) rows of label \(v\) whose *baseline* \(b\) is the right endpoint of the cell of \(x\), with coordinate \(w=b\); their subclass is \(T^+\) for vertices of \(T^+\) and \(T^-\) for vertices of \(T^-\). Add \(P\) further rows of subclass \(T^+\), label \(v\) and baseline \(1\) (the *padding*), with \(w=1\). Thus label \(v\) has
\[
t_{v,+}=d|V(T^+)|+P,\qquad t_{v,-}=d|V(T^-)|,\qquad t_v=t_{v,+}+t_{v,-}\geq P+2d\tag{5.1}
\]
tree rows. For each position \(r\in\mathcal R_v\) create \(2d\) *job rows* of subclass \(S\) and label \(v\) with baseline \(b_r\): \(d\) *short* ones with \(w=b_r-\Delta\) and \(d\) *long* ones with \(w=b_r\). Put \(J_v=d|\mathcal R_v|=dR\deg(v)\).

**Anchors.** Let \(\mathcal B_v\) be the multiset consisting of the baselines of all tree rows of label \(v\) (padding included) and of \(d\) copies of \(b_r\) for each \(r\in\mathcal R_v\); so \(|\mathcal B_v|=t_v+J_v\), and the job part counts \(d\) of the \(2d\) job rows of each position. For a real \(a\) let \(B_v(a)\) be the number of members of \(\mathcal B_v\) that are at most \(a\). Now, for each test interval \([l,r')\) of \(v\), replace \(d\) copies of its right endpoint \(r'\) in \(\mathcal B_v\) by \(l\). The copies exist: the right endpoint of a leaf cell is the baseline of the \(d\) rows of that leaf, and the right endpoint of a job cell is \(b_r\), present \(d\) times; different tests use different copies. Each member \(z\) of the resulting multiset is a *deadline*; create an anchor of subclass \(Z\), label \(v\) and coordinate \(w=-z\).

Since the test intervals are disjoint, Lemma 5.1(b) of the first lesson gives, for every real \(a\),
\[
\#\{Z\text{-anchors of label }v\text{ with deadline}\leq a\}=B_v(a)+d\,\mathbf 1\{a\in\mathcal I_v\}.\tag{5.2}
\]
In addition, for every position \(r=(e,j)\in\mathcal R_v\) create \(d\) *keys*: anchors of subclass \(Y\), label \(v\), with coordinate \(w=-b_r-\beta_e\). There are \(J_v\) keys of label \(v\).

**Global auxiliaries.** Each has a *length* \(\operatorname{len}\in\{0,1\}\) and coordinate \(w=-\operatorname{len}\). Create \(\sum_v(t_{v,+}+J_v)\) items of subclass \(U^+\), exactly \(dk\) of them of length one, and \(\sum_vt_{v,-}\) items of subclass \(U^-\), exactly \(d(n-k)\) of length one. For each edge \(e\) create \(dR\) *permits* of subclass \(W\) with \(w=\beta_e\) and \(dR\) *nonpermits* of subclass \(W\) with \(w=\beta_e+\Delta\); they *belong* to \(e\).

**Local auxiliaries.** For each label \(v\) create \(t_v+J_v\) items of subclass \(D^{\mathrm M}\) and label \(v\): for each \(\ell=1,\ldots,L\) exactly \(p_\ell\) of *length* \(\lambda_\ell\), the other \(t_v+J_v-P\) of length \(0\); their coordinate is \(w=-\operatorname{len}\). Also create \(J_v\) items of subclass \(D^{\mathrm G}\) and label \(v\), with \(w=0\).

**Flags.** Create \(\sum_vt_v\) flags \(F^{\mathrm T}\), and \(\sum_vJ_v\) flags of each of \(F^{\mathrm M}\) and \(F^{\mathrm G}\), all with \(w=0\).

The counts are nonnegative: \(t_{v,+}\geq d\) and \(t_{v,-}\geq d\) (the root rows), so there are at least \(dn\geq dk\) items \(U^+\) and \(dn\geq d(n-k)\) items \(U^-\); and \(t_v+J_v\geq P\) by (5.1). Put
\[
B=\sum_{v=1}^n(t_v+2J_v).\tag{5.3}
\]

**Lemma 5.1 (role counts).** Each of the five roles has exactly \(B\) items, and for each label \(v\) the rows, the anchors and the local auxiliaries of label \(v\) number \(t_v+2J_v\) each. All coordinates satisfy \(|w(i)|\leq6\).

*Proof.* Label \(v\) has \(t_v\) tree rows and \(2J_v\) job rows; \(t_v+J_v\) deadlines and \(J_v\) keys; \(t_v+J_v\) items \(D^{\mathrm M}\) and \(J_v\) items \(D^{\mathrm G}\). Summing over \(v\) gives \(B\) for rows, anchors and local auxiliaries. Every edge has two endpoints, so \(\sum_vJ_v=dR\sum_v\deg(v)=2dRm\), the number of items \(W\). The global auxiliaries number \(\sum_v(t_{v,+}+J_v)+\sum_vt_{v,-}+2dRm=\sum_v(t_v+2J_v)=B\), and the flags \(\sum_vt_v+2\sum_vJ_v=B\). Cell endpoints lie in \([0,5]\), lengths are at most one, \(\Delta<1\) and \(0\leq\beta_e<1/16\), so \(|w|\leq6\). \(\square\)

So an instance of \(5B\) items is being built in which, if each bin holds at most five items, a packing into \(B\) bins must fill every bin with exactly one item of each role. The next lesson makes this, and much more, a consequence of the item sizes.

## 6. What the coordinates encode

The coordinates are chosen so that, in a good tuple, fitting into a bin will mean \(\sum w\leq0\) (next lesson). For a good tuple of kind M with row baseline \(b\), deadline \(z\) and auxiliaries \(U,D\), the coordinates sum to \(h-z\), where
\[
h=b-\Delta\,\mathbf 1\{\text{the row is short}\}-\operatorname{len}(U)-\operatorname{len}(D)\leq b\tag{6.1}
\]
is the *completion* of the row: the auxiliaries move the row's point from its baseline \(b\) to the left. So the tuple will fit exactly when the completion meets the deadline, \(h\leq z\), and the row then *covers* the half-open interval \([h,b)\). By (5.1) of the first lesson, for any family of such tuples and any real \(a\),
\[
\#\{h\leq a\}=\#\{b\leq a\}+\#\{\text{intervals }[h,b)\text{ containing }a\}.\tag{6.2}
\]
Compared with (5.2), this is how deadlines that are met force coverage: a test interval has \(d\) deadlines more to the left of its points than baselines, and these can only be met by \(d\) intervals \([h,b)\) covering it.

For a good tuple of kind G, with key at position \(r=(e,j)\), row at position \(r'\) and \(W\)-item of edge \(f\), the coordinates sum to
\[
b_{r'}-b_r+\beta_f-\beta_e+\Delta\bigl(\mathbf 1\{\text{nonpermit}\}-\mathbf 1\{\text{the row is short}\}\bigr).\tag{6.3}
\]
Lemma 2.1 will show that this is positive whenever \(r'>r\) or \(f>e\): a key can only take a row of its own or an earlier position, and a resource of its own or an earlier edge. At its own position and edge, a long row needs a permit, and a short row accepts either kind.

The lengths are tied to the geometry: a local auxiliary of length \(\lambda_\ell\) can stretch a row's interval over at most one cell of depth \(\ell\) (Lemma 3.1(c)), and a global auxiliary of length one stretches it over a whole root cell. Long global auxiliaries are scarce: \(dk\) on the plus side and \(d(n-k)\) on the minus side, in total over all vertices.

## 7. Exercises

**7.1.** Verify the step computation in the proof of Lemma 2.1 for \(R=2\), \(m=2\): list \(H_r\) for the four positions \((1,1),(1,2),(2,1),(2,2)\), and check (2.3).

**7.2.** Show that every \(Z\)-anchor of label \(v\) has deadline at most the largest member of \(\mathcal B_v\), and that the deadlines and \(\mathcal B_v\) have the same number of elements.

**7.3.** Check (5.2) directly at a point \(a\) of a leaf cell \([l,r')\) of \(T^+\) and at its right endpoint \(a=r'\).

**7.4.** Why are the root rows included among the tree rows, and why is the padding of \(P\) rows with baseline \(1\) added? (Look at the nonnegativity statements and at the slots needed in the next lessons.)

**7.5.** Compute \(\sum_v J_v\) for the complete graph \(K_4\), and express \(B\) in terms of \(t=t_v\), \(d\) and \(R\).

## 8. Solutions

**7.1.** \((R+1)^0=1\) and \((R+1)^1=3\): \(H_{1,1}=0\), \(H_{1,2}=1\), \(H_{2,1}=2\), \(H_{2,2}=5\); \(\theta_1=0\), \(\theta_2=2\). Steps after positions of edge 1 are at least \(1=\theta_1+1\); after \((2,1)\) the step is \(3=\theta_2+1\). And \(\theta_2-\theta_1=2=H_{1,2}+1\).

**7.2.** The deadlines arise from \(\mathcal B_v\) by moving some members to smaller values, one for one.

**7.3.** For \(a\in[l,r')\): \(d\) members equal to \(r'>a\) were replaced by \(l\leq a\), so the count rises by \(d\); no other test contains \(a\). At \(a=r'\) both \(l\) and \(r'\) are at most \(a\), the count is unchanged, and \(r'\notin\mathcal I_v\) because tests are half-open and disjoint.

**7.4.** The \(d\) root rows on each side give every vertex at least \(d\) rows that can take a long global auxiliary covering a whole root cell; they also make the counts of \(U^\pm\) large enough to contain the length-one items. The padding rows supply \(P\) additional row slots, so that all \(P\) positive local auxiliaries of a vertex can always be placed (next lessons), and they have baseline \(1\), to the right of every plus test.

**7.5.** In \(K_4\) every vertex has degree \(3\), so \(J_v=3dR\) and \(\sum_vJ_v=12dR=2dRm\) with \(m=6\). All vertices have the same tree-row count \(t\), so \(B=4t+24dR\).

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
