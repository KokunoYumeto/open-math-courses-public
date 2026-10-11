# Dimension and cohomology of the boundary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The boundary \(B\) of [The compact space and its boundary](the-compact-space-and-its-boundary.md) is a continuum with more than one point. This lesson proves two further properties.

- \(B\) has covering dimension at most one (Theorem 2.3). No assumption beyond the standing ones is needed. The reason is that a level cut of a finite-energy function accumulates on the boundary only in a very thin set, and away from the cuts the boundary is cut into small pieces by finitely many signs.
- If every \(1\)-cochain on the Cayley complex whose coboundary has finite support can be corrected by a cochain of finite support, then the first Čech cohomology of \(B\) vanishes (Theorem 3.2). A Čech cocycle on \(B\) is transported to the Cayley complex by labelling the vertices, corrected there, and brought back.

Together with [Dendrites and cut points](course:continua-arcs-and-cut-points/dendrites-and-cut-points) this gives a strong restriction (Corollary 3.3): under these assumptions \(B\) is locally connected only if it has cut points. The arguments are those of [OpenAI-S, Section 5].

Notation and standing assumptions are those of the previous two lessons: \(X=\Gamma\cup B\) with its metric \(\rho\), the families \(\mathcal F_0\subseteq\mathcal F\), cuts \(S(F,t)\), the set \(V(C)\) of ends of the edges of \(C\), the quantities \(\Lambda_g(e)\), and \(\rho(x,y)=\sum_jc_j|F_j(x)-F_j(y)|\) for an enumeration \(F_1,F_2,\dots\) of \(\mathcal F\). We use Definition 2.1 of [Covering dimension and finite trivializing covers](course:index-theory-of-elliptic-operators/covering-dimension-and-finite-trivializing-covers#2-covering-dimension) and the lesson [First Čech cohomology of a compact metric space](course:continua-arcs-and-cut-points/first-cech-cohomology-of-a-compact-metric-space).

## 1. Where a cut meets the boundary

For \(F\in\mathcal F\) and a level \(t\) that is regular for \(F\), let
\[
E(F,t)=\overline{V(S(F,t))}\cap B ,
\]
the set of boundary points at which the ends of the edges of the cut accumulate. It is compact.

A subset \(Y\) of a metric space has *length zero* if for every \(\varepsilon>0\) it is covered by finitely many sets whose diameters add up to less than \(\varepsilon\). A finite union of sets of length zero has length zero.

**Lemma 1.1** (thin walls). For every \(F\in\mathcal F\) and almost every \(t\in\mathbb R\), the level \(t\) is regular for \(F\) and \(E(F,t)\) has length zero.

**Proof.** *Base functions.* Let \(F\in\mathcal F_0\). By Lemma 2.2 of [The convergence action](the-convergence-action.md), with \(g=1\),
\[
\int_{\mathbb R}\ \sum_{e\in S(F,t)}\Lambda_1(e)\,dt<\infty .
\]
So for almost every \(t\) the sum \(\sum_{e\in S(F,t)}\Lambda_1(e)\) is finite. Fix such a \(t\) that is also regular, write \(S=S(F,t)\), and let \(\varepsilon>0\). Choose a finite \(D_0\subseteq S\) with
\[
\sum_{e\in S\setminus D_0}\Lambda_1(e)<\frac\varepsilon2 .
\]
The set \(S\) has finitely many dual components (Lemma 1.2 of the previous lesson), and every edge is dually adjacent to at most \(D\) others; so \(S\setminus D_0\) has finitely many dual components \(C_1,\dots,C_r\), as in the proof of Proposition 2.2 there. By Lemma 2.1 of the lesson on the convergence action, with \(g=1\), the diameter of \(V(C_l)\), and so of its closure, is at most \(2\sum_{e\in C_l}\Lambda_1(e)\). The sum of these diameters is less than \(\varepsilon\).

The closures of the sets \(V(C_l)\) cover \(E(F,t)\). Indeed a point \(x\in E(F,t)\) is a limit of pairwise distinct vertices of \(V(S)\); only finitely many vertices are ends of edges of \(D_0\), so \(x\) is a limit of vertices of \(V(S\setminus D_0)=\bigcup_lV(C_l)\).

*The functions \(h_{O,U}\).* Let \(T=h_{O,U}\), where \(O\) has the conditions \((F_j;a_j,b_j)\). For \(0<t<1\) the cut \(S(T,t)\) lies in the union of the cuts \(S(F_j,a_j+t)\) and \(S(F_j,b_j-t)\) (Lemma 3.1 of the previous lesson). So \(E(T,t)\) lies in the union of the sets \(E(F_j,a_j+t)\) and \(E(F_j,b_j-t)\), whenever all the levels are regular. For almost every \(t\) they are, and all these sets have length zero. For \(t<0\) and \(t>1\) the cut is empty. \(\blacksquare\)

**Lemma 1.2** (the sign of a point off the wall). Let \(F\in\mathcal F\), let \(t\) be regular for \(F\), and \(x\in B\setminus E(F,t)\). There is an open neighbourhood \(V\) of \(x\) in \(X\) such that \(F-t\) has the same sign at all vertices in \(V\). This sign, \(+\) or \(-\), is the *sign of \(x\)* for \((F,t)\). It is a locally constant function of \(x\in B\setminus E(F,t)\). If it is \(+\), then \(F(x)\ge t\); if it is \(-\), then \(F(x)\le t\).

**Proof.** Since \(x\) is not in the closure of \(V(S(F,t))\), there is an open neighbourhood \(W\) of \(x\) in \(X\) that contains no end of an edge of \(S(F,t)\). Theorem 6.2 of the previous lesson gives an open neighbourhood \(V\subseteq W\) of \(x\) such that any two vertices in \(V\) are joined by a path with all vertices in \(W\). No edge of such a path lies in \(S(F,t)\), and \(t\) is regular; so \(F-t\) has the same sign at the two vertices. Every neighbourhood of \(x\) contains vertices, so the sign does not depend on the choice of \(V\). For \(y\in B\cap V\), the set \(V\) is a neighbourhood of \(y\) with the same property, so \(y\) has the same sign. The last statement holds because \(x\) is a limit of vertices and \(F\) is continuous. \(\blacksquare\)

## 2. Dimension at most one

**Lemma 2.1.** Let \(K\) be a compact metric space of length zero and \(\varepsilon>0\). Then \(K\) is the union of finitely many pairwise disjoint compact open subsets of diameter less than \(\varepsilon\).

**Proof.** Let \(x\in K\). The map \(y\mapsto\rho(x,y)\) does not increase distances, so the image of a set of diameter \(d\) lies in an interval of length \(d\). Hence the set of distances \(\{\rho(x,y):y\in K\}\) is covered by finitely many intervals of arbitrarily small total length, and there is \(r\in(0,\varepsilon/2)\) that is not the distance from \(x\) to any point of \(K\). The ball \(\{y\in K:\rho(x,y)<r\}\) then equals \(\{y\in K:\rho(x,y)\le r\}\); it is open and closed in \(K\) and has diameter less than \(\varepsilon\). Finitely many such balls \(N_1,\dots,N_m\) cover \(K\), and the sets \(N_1\), \(N_2\setminus N_1\), \(N_3\setminus(N_1\cup N_2),\dots\) are open and closed, pairwise disjoint, and cover \(K\). \(\blacksquare\)

**Lemma 2.2.** Let \(\varepsilon>0\). There are finitely many pairs \((F,t)\), with \(F\in\mathcal F\), \(t\) regular for \(F\) and \(E(F,t)\) of length zero, such that any two points of \(B\) that lie in no \(E(F,t)\) of the list and have the same sign for every pair of the list are at distance at most \(\varepsilon\).

**Proof.** Choose \(J\) with \(\sum_{j>J}c_j<\varepsilon/2\), and \(\varepsilon'>0\) with \(\varepsilon'\sum_{j\le J}c_j<\varepsilon/2\). For each \(j\le J\) choose levels
\[
0<t_{j,1}<t_{j,2}<\dots<t_{j,q}<1
\]
such that \(t_{j,1}<\varepsilon'\), \(t_{j,q}>1-\varepsilon'\), consecutive levels differ by less than \(\varepsilon'\), and every \(t_{j,i}\) is regular for \(F_j\) with \(E(F_j,t_{j,i})\) of length zero. This is possible by Lemma 1.1, since the excluded levels have measure zero. The list consists of the pairs \((F_j,t_{j,i})\).

Let \(x,y\) be as in the statement and \(j\le J\). By the last statement of Lemma 1.2, \(F_j(x)\ge t_{j,i}\) for the levels with sign \(+\) and \(F_j(x)\le t_{j,i}\) for those with sign \(-\), and the same holds for \(y\) with the same signs. For a vertex, \(F_j>t\) at one level implies it at all lower levels; so the signs are \(+\) up to some index \(i\) and \(-\) after it. So \(F_j(x)\) and \(F_j(y)\) lie in the same one of the intervals \([0,t_{j,1}]\), \([t_{j,i},t_{j,i+1}]\), \([t_{j,q},1]\), each of length less than \(\varepsilon'\). Since all functions have values in \([0,1]\),
\[
\begin{aligned}
\rho(x,y)&\le\varepsilon'\sum_{j\le J}c_j+\sum_{j>J}c_j\\
&<\varepsilon .
\end{aligned}
\]
\(\blacksquare\)

**Theorem 2.3.** Under the standing assumptions, \(\dim B\le1\).

**Proof.** Let \(\mathcal U\) be a finite open cover of \(B\) and \(\varepsilon>0\) a Lebesgue number: every subset of \(B\) of diameter less than \(\varepsilon\) lies in a member of \(\mathcal U\). We construct a finite open cover of \(B\) by sets of diameter less than \(\varepsilon\) in which every point lies in at most two members. It refines \(\mathcal U\), which proves the theorem.

Take the list of Lemma 2.2 for \(\varepsilon/2\) and let \(E_\ast\) be the union of the sets \(E(F,t)\) of the list. It is a compact subset of \(B\) of length zero.

*Pieces off \(E_\ast\).* For each assignment \(\tau\) of a sign to every pair of the list, let \(\Sigma_\tau\) be the set of points of \(B\setminus E_\ast\) with these signs. By Lemma 1.2 each \(\Sigma_\tau\) is open in \(B\setminus E_\ast\), hence in \(B\). The sets \(\Sigma_\tau\) are pairwise disjoint, cover \(B\setminus E_\ast\), and have diameter at most \(\varepsilon/2\) by Lemma 2.2.

*Pieces around \(E_\ast\).* By Lemma 2.1, \(E_\ast=K_1\cup\dots\cup K_m\) with pairwise disjoint compact sets of diameter less than \(\varepsilon/4\). Let \(\theta>0\) be smaller than \(\varepsilon/8\) and, if \(m\ge2\), than a third of the least distance between two of the \(K_i\), and let \(N_i\) be the set of points of \(B\) at distance less than \(\theta\) from \(K_i\). The sets \(N_i\) are open, pairwise disjoint, of diameter less than \(\varepsilon/2\), and cover \(E_\ast\).

The sets \(N_i\) and \(\Sigma_\tau\) form a finite open cover of \(B\) by sets of diameter less than \(\varepsilon\). A point lies in at most one \(N_i\) and in at most one \(\Sigma_\tau\). \(\blacksquare\)

## 3. The first cohomology of the boundary

Let \(k\) be an abelian group. For a \(1\)-cochain \(\alpha:E\to k\) on the Cayley complex, the *coboundary* \(d\alpha\) is the function on cells whose value at a cell is the integral of \(\alpha\) around the boundary of the cell. So \(\alpha\) is a cocycle exactly when \(d\alpha=0\).

**Assumption \((\mathrm C_k)\).** For every \(1\)-cochain \(\alpha:E\to k\) whose coboundary \(d\alpha\) is nonzero on only finitely many cells, there is a \(1\)-cochain \(\eta:E\to k\), nonzero on only finitely many edges, with \(d\eta=d\alpha\).

This is a statement about the Cayley complex. It is the form in which the vanishing of the group cohomology \(H^2(\Gamma;k\Gamma)\) is used in [OpenAI-S, Section 5]; the translation between the two is not proved or used in this lesson.

**Lemma 3.1** (labels). Let \((U_i)_{i\in I}\) be a finite cover of \(B\) by open subsets of \(B\). There are a number \(\delta>0\) and a label \(i(u)\in I\) for every vertex \(u\) such that every \(x\in B\) has the following property: if \(u\) is a vertex with \(\rho(u,x)<\delta\), then \(U_{i(u)}\) contains \(x\).

**Proof.** Let \(6\delta\) be less than a Lebesgue number of the cover, so that every ball of radius \(3\delta\) in \(B\) lies in some \(U_i\). For a vertex \(u\) choose a point \(b(u)\in B\) nearest to \(u\), and a label \(i(u)\) such that \(U_{i(u)}\) contains the ball of radius \(3\delta\) about \(b(u)\) in \(B\). If \(\rho(u,x)<\delta\) with \(x\in B\), then \(\rho(u,b(u))\le\rho(u,x)\), so \(\rho(b(u),x)<2\delta\) and \(x\in U_{i(u)}\). \(\blacksquare\)

**Theorem 3.2.** Under the standing assumptions and \((\mathrm C_k)\), \(\check H^1(B;k)=0\).

**Proof.** By Theorem 3.1 of the lesson on Čech cohomology it suffices to show: for every finite open cover \((U_i)_{i\in I}\) of \(B\) and every cocycle \((d_{ij})\) on its nerve there are locally constant maps \(l_i:U_i\to k\) with \(l_j-l_i=d_{ij}\) on \(U_i\cap U_j\). Fix the cover and the cocycle, and take \(\delta\) and the labels of Lemma 3.1. For \(x\in B\) let \(W_x\) be the open ball of radius \(\delta\) about \(x\) in \(X\); so \(x\in U_{i(u)}\) for every vertex \(u\in W_x\).

*Step 1: a cochain on the Cayley complex.* Define \(\alpha:E\to k\) by
\[
\alpha(e)=d_{i(e^-)\,i(e^+)}
\]
if \(U_{i(e^-)}\) and \(U_{i(e^+)}\) meet, and \(\alpha(e)=0\) otherwise.

*Step 2: \(d\alpha\) has finite support.* Suppose \(d\alpha\) is nonzero on infinitely many cells \((g_n,r_n)\). Passing to a subsequence, \(r_n=r\) is constant, the \(g_n\) are pairwise distinct, and \(g_n\to x\in B\) in \(X\). The vertices of the cell are \(g_n\) times finitely many fixed elements, so by Lemma 1.1 of the lesson on the convergence action they all converge to \(x\). For large \(n\) they lie in \(W_x\), so all their labels \(i\) have \(x\in U_i\). Then every edge of the cell has \(\alpha(e)=d_{i(e^-)i(e^+)}\), and the integral of \(\alpha\) around the cell is a sum \(d_{i_0i_1}+d_{i_1i_2}+\dots+d_{i_{m-1}i_0}\) over a closed sequence of labels of sets containing \(x\). (A backward traversal of \(e\) contributes \(-d_{i(e^-)i(e^+)}=d_{i(e^+)i(e^-)}\).) By the cocycle identity for sets with the common point \(x\), \(d_{i_0i_1}+d_{i_1i_2}=d_{i_0i_2}\), and so on; the sum is \(d_{i_0i_0}=0\). This contradicts the choice of the cells.

*Step 3: correction.* By \((\mathrm C_k)\) there is \(\eta\) with finite support and \(d\eta=d\alpha\). Then \(\alpha-\eta\) is a cocycle, and by Lemma 1.1 of [Finite-energy functions on a Cayley complex](finite-energy-functions-on-a-cayley-complex.md) there is \(l:\Gamma\to k\) with
\[
\alpha-\eta=dl .
\]

*Step 4: the function near a boundary point.* Let \(i\in I\) and \(x\in U_i\). For a vertex \(u\in W_x\) put
\[
\lambda_i(u)=l(u)+d_{i(u)\,i} ,
\]
which is defined because \(x\in U_{i(u)}\cap U_i\). Let \(W\subseteq W_x\) be an open neighbourhood of \(x\) in \(X\) containing no end of an edge on which \(\eta\) is nonzero; there are finitely many such vertices and \(x\) is not a vertex. Let \(e\) be an edge with both ends \(u=e^-\), \(v=e^+\) in \(W\). Then \(\eta(e)=0\) and \(\alpha(e)=d_{i(u)i(v)}\), so \(l(v)-l(u)=d_{i(u)i(v)}\), and
\[
\begin{aligned}
&\lambda_i(v)-\lambda_i(u)\\
&\quad=d_{i(u)i(v)}+d_{i(v)i}-d_{i(u)i}=0
\end{aligned}
\]
by the cocycle identity at \(x\). By Theorem 6.2 of the previous lesson there is an open neighbourhood \(V\subseteq W\) of \(x\) any two of whose vertices are joined by a path with all vertices in \(W\). So \(\lambda_i\) is constant on the vertices in \(V\). Let \(l_i(x)\) be this constant. It does not depend on the choice of \(W\) and \(V\), because any two neighbourhoods of \(x\) have a vertex in common.

*Step 5: \(l_i\) is locally constant.* Let \(y\in U_i\cap V\cap B\). A neighbourhood of \(y\) inside \(V\cap W_y\) serves as the set \(W\) for \(y\), and the vertices of the corresponding smaller neighbourhood of \(y\) lie in \(V\), where \(\lambda_i\) has the value \(l_i(x)\). The function \(\lambda_i\) is given by the same formula for \(y\) as for \(x\). So \(l_i(y)=l_i(x)\).

*Step 6: the overlaps.* Let \(x\in U_i\cap U_j\) and let \(u\) be a vertex so close to \(x\) that \(\lambda_i(u)=l_i(x)\) and \(\lambda_j(u)=l_j(x)\). Then
\[
\begin{aligned}
l_j(x)-l_i(x)&=d_{i(u)\,j}-d_{i(u)\,i}\\
&=d_{ij}
\end{aligned}
\]
by the cocycle identity at \(x\). \(\blacksquare\)

**Corollary 3.3.** Assume the standing assumptions and \((\mathrm C_k)\) for some abelian group \(k\ne0\). Then \(B\) is a continuum with more than one point, \(\dim B\le1\) and \(\check H^1(B;k)=0\). Consequently \(B\) contains no simple closed curve, and if \(B\) is locally connected, then \(B\) is a dendrite and has cut points.

**Proof.** The first statement collects Theorem 5.1 of the previous lesson and Theorems 2.3 and 3.2. The rest is Theorem 2.1 and Corollaries 2.2 and 3.2 of [Dendrites and cut points](course:continua-arcs-and-cut-points/dendrites-and-cut-points). \(\blacksquare\)

In OpenAI's proof of the Singer conjecture in dimension four outside the middle degree, the assumption is used with \(k=\mathbb F_2\); the same three properties are then proved for a subcontinuum of \(B\) without cut points, which is shown to be locally connected, and the last statement of the corollary, applied to that subcontinuum, is the contradiction that ends the proof [OpenAI-S].

## 4. Exercises

**4.1.** Show that a compact subset of the line has length zero if and only if it has Lebesgue measure zero, and that a continuum with more than one point does not have length zero.

**4.2.** In the proof of Theorem 2.3, why can a point lie in two members of the cover, and why not in three?

**4.3.** Let \(\alpha\) be a \(1\)-cochain with values in \(k\) and \(\eta\) a \(1\)-cochain with finite support. Show that \(d\eta\) has finite support, and that \(d(\alpha-\eta)=0\) if and only if \(d\alpha=d\eta\).

**4.4.** Show that assumption \((\mathrm C_k)\) fails for \(\Gamma=\mathbb Z^2\) with the triangular presentation \(\langle s,t,y\mid y^{-1}st,\ y^{-1}ts\rangle\) and \(k=\mathbb F_2\), by considering the cochain that is \(1\) on the edges \((g,s)\) with \(g=s^at^b\), \(a=0\), \(b\ge0\), together with those edges \((g,y)\) that are needed to make the coboundary vanish away from one cell.

**4.5.** Where does the proof of Theorem 3.2 use Theorem 6.2 of the previous lesson, and what would go wrong if only the connectedness of \(B\) were known?

## 5. Solutions

**4.1.** A compact set of Lebesgue measure zero is covered by countably many open intervals of total length less than \(\varepsilon\), and by compactness by finitely many of them. Conversely a set of diameter \(d\) on the line lies in an interval of length \(d\), so a set of length zero has outer measure zero. Let \(K\) be a continuum and \(x\ne y\) in \(K\). The function \(z\mapsto\rho(x,z)\) maps \(K\) onto a connected set containing \(0\) and \(\rho(x,y)\), hence onto a set containing an interval of positive length; as in the proof of Lemma 2.1 the image of a set of length zero has measure zero.

**4.2.** The sets \(N_i\) are pairwise disjoint and so are the sets \(\Sigma_\tau\), so a point lies in at most one of each kind. A point of \(N_i\) outside the union of the walls lies in \(N_i\) and in one \(\Sigma_\tau\).

**4.3.** A cell has at most three edges and an edge lies in at most \(3|R|\) cells, so \(d\eta\) vanishes on all cells without an edge in the support of \(\eta\), that is, on all but finitely many. The coboundary is additive.

**4.4.** Write \(g=s^at^b\) as the point \((a,b)\) of the grid; the cells are the two triangles of each grid square, \(T^1_{a,b}\) with the edges \(((a,b),s)\), \(((a+1,b),t)\), \(((a,b),y)\), and \(T^2_{a,b}\) with the edges \(((a,b),t)\), \(((a,b+1),s)\), \(((a,b),y)\). Let \(\alpha\) be \(1\) on the edges \(((0,b),s)\) and \(((0,b),y)\) for \(b\ge0\) and \(0\) on all other edges. The triangle \(T^1_{0,b}\), \(b\ge0\), contains two edges with value \(1\); the triangle \(T^2_{0,b}\), \(b\ge0\), contains \(((0,b+1),s)\) and \(((0,b),y)\), again two; the triangle \(T^2_{0,-1}\) contains only \(((0,0),s)\); all other triangles contain none. So \(d\alpha\) is nonzero on exactly one cell. Suppose \(\eta\) has finite support and \(d\eta=d\alpha\). Then \(\alpha-\eta\) is a cocycle, so \(\alpha-\eta=dl\) with \(l:\mathbb Z^2\to\mathbb F_2\) (Lemma 1.1 of the first lesson). Choose \(M\) so large that \(\eta\) vanishes on every edge that has an end outside the square of the points with \(|a|,|b|<M\). The closed path around the square with corners \((\pm M,\pm M)\), along edges of the forms \((g,s)\) and \((g,t)\), uses no edge on which \(\eta\) is nonzero, so the integral of \(\alpha\) along it equals that of \(dl\), which is \(0\). But \(\alpha\) is \(1\) on exactly one edge of the path, the edge \(((0,M),s)\) on its upper side. This is a contradiction.

**4.5.** Theorem 6.2 of the previous lesson is used in Step 4: the function \(\lambda_i\) is constant along edges near \(x\), and the theorem joins any two vertices near \(x\) by a path of such edges, which makes \(\lambda_i\) constant near \(x\). Connectedness of \(B\) says nothing about paths of vertices near a point, so \(\lambda_i\) could take several values on vertices arbitrarily close to \(x\), and \(l_i(x)\) would not be defined.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
