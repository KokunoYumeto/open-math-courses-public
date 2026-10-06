# Polish orbits and their quotient topology

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain \(CC0\).*

## Introduction

An orbit carries two natural topologies. One comes from its position inside the space on which the group acts. The other comes from the homogeneous space obtained by dividing the group by a stabilizer. A continuous bijection relates them, but its inverse need not be continuous. Effros's theorem identifies exactly when the two topologies agree, and explains what this says about the whole orbit space.

Throughout, a Polish group acts continuously on a Polish space. The group may fail to be locally compact, and the orbits may be uncountable. We prove the four equivalent conditions in Takesaki III, Exercise XIII.2(1)(b), at this full scope. The category argument uses the complete-parameter intersection technique of Jan van Mill, *A Note on the Effros Theorem*, Proposition 2.2 and Section 3. The proof is supplied below, with an explicit nested-set invariant; the citation gives mathematical credit rather than replacing the argument. These are known results, not claims of new research.

We use the written programme lesson *Effros Borel structure*, Theorem 2.1(1), for the complete metrization of a relatively open or a countable intersection of open subsets of a Polish space. Its reciprocal-distance metric and completeness proof apply without a measure hypothesis. The Baire category theorem and the elementary topology of metric spaces are prerequisites. The earlier lesson [Orbits, stabilizers and relation algebras](orbits-stabilizers-and-relation-algebras.md) gives the algebraic orbit conventions.

The last section introduces the closure conditions used by the stronger locally closed orbit criterion. The next lesson, [Locally closed orbits and measurable representatives](locally-closed-orbits-and-measurable-representatives.md), proves the complete Glimm equivalence, including the converse for ergodic measures and a Borel representative construction.

## 1. Quotients, stabilizers and category

Let \(G\curvearrowright X\) be a continuous action, with \(G,X\) Polish. Write \(\pi:X\to X/G\) for the orbit map. The quotient topology is defined by declaring \(A\subset X/G\) open exactly when \(\pi^{-1}(A)\) is open. Thus \(\pi\) is continuous. It is also open: for open \(U\subset X\),
\[
\pi^{-1}(\pi(U))=GU=\bigcup_{g\in G}gU
\tag{1.1}
\]
is open. If \(U_n\) is a countable base of \(X\), the sets \(\pi(U_n)\) form a countable base of \(X/G\). This assertion requires no Hausdorff separation of the quotient.

For \(x\in X\), the stabilizer \(H_x=\{g:gx=x\}\) is closed, by continuity of \(g\mapsto gx\). The map \(q:G\to G/H_x\), \(g\mapsto gH_x\), is continuous and open: \(q^{-1}(q(V))=VH_x\) for open \(V\subset G\). The canonical map
\[
\phi_x:G/H_x\longrightarrow Gx,\qquad gH_x\longmapsto gx
\tag{1.2}
\]
is a continuous bijection, where \(Gx\) has its relative topology in \(X\). Continuity follows from the definition of the quotient topology. In this lesson, saying that the action is *microtransitive on an orbit* means that \(Vx\) contains a relative neighborhood of \(x\) for every identity neighborhood \(V\subset G\).

**Lemma 1.1.** The map \(g\mapsto gx\) is open onto \(Gx\) exactly when the action is microtransitive at every point of that orbit. In that case \(\phi_x\) is a homeomorphism.

*Proof.* Openness gives the neighborhood condition immediately. Conversely, let \(A\subset G\) be open and \(gx\in Ax\), with \(g\in A\). Choose an identity neighborhood \(V\) such that \(gV\subset A\). The set \(Vx\) contains a neighborhood of \(x\), so \(gVx\subset Ax\) contains a neighborhood of \(gx\). Hence \(Ax\) is open in the orbit. For an open set \(B\subset G/H_x\), the identity \(\phi_x(B)=q^{-1}(B)x\) then proves that \(\phi_x\) is open. The reverse implication also follows by composing the open map \(q\) with a homeomorphism \(\phi_x\). \(\square\)

A set is *meagre* in a space if it is a countable union of nowhere dense sets there. A nonempty space is of the second category in itself if it is not meagre in itself. A Baire space is one in which a countable intersection of open dense sets is dense.

**Lemma 1.2.** A continuous open surjection from a nonempty Baire space has a Baire target.

*Proof.* Let \(f:Y\to Z\) be such a surjection and let \(D_n\subset Z\) be open dense. Each \(f^{-1}(D_n)\) is open dense in \(Y\): an open nonempty \(A\subset Y\) has an open nonempty image meeting \(D_n\). For an open nonempty \(W\subset Z\), the Baire property in \(Y\) gives a point in \(f^{-1}(W)\cap\bigcap_n f^{-1}(D_n)\). Its image lies in \(W\cap\bigcap_nD_n\). \(\square\)

In particular, every \(G/H_x\) is Baire, because \(G\) is completely metrizable and \(q\) is open. This suffices for the implication from homogeneous-space topology to second category below; no unproved complete metrization of the coset space is needed.

**Lemma 1.3 (Open images inside a Polish space).** Suppose \(P\) is Polish, \(Y\subset X\) with \(X\) Polish, and \(f:P\to Y\) is a continuous open surjection for the relative topology of \(Y\). Then \(Y\) is \(G_\delta\) in \(X\).

*Proof.* We give the metric-cover argument, including its refinement step. Every countable open cover \(A_j\) of a metric space has a countable locally finite open refinement. To see this, choose a point \(y_0\), put \(T_n=\bigcup_{j\leq n}A_j\), and set
\[
F_n=\{y:d(y,y_0)\leq n,\ \min(1,d(y,Y\setminus T_n))\geq1/(n+1)\},\qquad F_0=\varnothing.
\tag{1.3}
\]
The minimum is defined as one when the complement is empty. These closed sets exhaust the space and satisfy \(F_n\subset\operatorname{int}F_{n+1}\). The open bands \(\operatorname{int}F_{n+1}\setminus F_{n-1}\), \(n\geq1\), cover it and are locally finite: a neighborhood inside \(F_k\) misses every band with \(n\geq k+1\). Each band is contained in \(T_{n+1}\). Intersecting it with \(A_1,\ldots,A_{n+1}\) gives the desired refinement. An arbitrary open cover has a countable subcover in a second countable space, so the same construction applies.

Here is a useful extension of this refinement. For a nonempty relatively open \(C\subset Y\), put
\[
\widetilde C=\{x\in X:d(x,C)<\tfrac13d(x,Y\setminus C)\},
\tag{1.4}
\]
using \(\widetilde C=X\) when \(C=Y\). This is open and \(\widetilde C\cap Y=C\). If \(C_j\) is locally finite in \(Y\), its extensions are locally finite on some open neighborhood \(L\) of \(Y\) in \(X\). Indeed, near each \(y\in Y\) all but finitely many \(C_j\) miss a relative ball of radius \(r>0\). For those indices and \(d(x,y)<r/2\), one has \(d(x,C_j)\geq r-d(x,y)>r/2\) and \(d(x,Y\setminus C_j)\leq d(x,y)<r/2\), excluding \(x\) from \(\widetilde C_j\). The union of these ambient neighborhoods supplies \(L\).

Use a complete metric on \(P\) and a compatible metric on \(X\). We build a countable tree of pairs \((V_s,O_s)\), where \(V_s\) is a nonempty open parameter set and \(O_s\) is ambient open. Start with \((P,X)\). At every positive depth \(n\), the \(O_s\cap Y\) cover \(Y\), and the \(O_s\) are locally finite on an ambient open neighborhood \(L_n\) of \(Y\). Each child has
\[
\overline{V_{sj}}\subset V_s,\quad
\operatorname{diam}V_{sj}<2^{-n},\quad O_{sj}\subset O_s.
\tag{1.5}
\]
In addition, both \(f(V_{sj})\) and \(O_{sj}\) lie in the same ambient ball of radius \(2^{-n}\), and \(O_s\cap Y\subset f(V_s)\) for every node.

To construct a level, for each \(y\in O_s\cap Y\) choose \(p\in V_s\) with \(f(p)=y\). By continuity choose a small open parameter ball \(V\) with closure in \(V_s\), diameter less than \(2^{-n}\), and image in \(O_s\cap B(y,2^{-n})\). Openness of \(f\) makes \(f(V)\) relatively open and containing \(y\). These target sets, over all nodes at the preceding level, cover \(Y\). Choose a countable locally finite open refinement \(C_j\) of that cover, and assign each member to one covering set and its parameter ball \(V\). Extend it by (1.4), then intersect that extension with its parent \(O_s\), the ball \(B(y,2^{-n})\), and an ambient neighborhood \(L_n\) on which all extensions are locally finite. Call the result \(O_{sj}\), and use the assigned \(V\) as \(V_{sj}\). Its intersection with \(Y\) is exactly \(C_j\), so it is nonempty. All required properties follow. The parameter balls need not be disjoint.

Define the ambient \(G_\delta\) set
\[
Z=\bigcap_{n\geq1}\left(L_n\cap\bigcup_{|s|=n}O_s\right).
\tag{1.6}
\]
It contains \(Y\). For \(x\in Z\), finitely many nodes at each depth contain \(x\), by local finiteness at \(x\in L_n\); there is at least one at every depth, and every such child's parent also contains \(x\). This finitely branching tree has an infinite branch: recursively choose a child with descendants at arbitrarily large depths, which exists since there are only finitely many children. Along the branch the nonempty closed parameter sets \(\overline{V_s}\) are nested with diameters tending to zero. Completeness gives a point \(p\) in their intersection, lying in every open \(V_s\) by the next closure inclusion. At depth \(n\), the points \(f(p)\) and \(x\) lie in the same ball of radius \(2^{-n}\). Hence they coincide. Thus \(x\in Y\), proving \(Y=Z\). Empty \(Y\) is already \(G_\delta\). \(\square\)

## 2. Intersecting two analytic sets

For this section, let \(Y\) be a separable metrizable space, which need not be complete. Call \(A\subset Y\) *analytic* if \(A=\alpha(P)\) for a continuous map from a Polish space \(P\). Say that \(A\) is everywhere nonmeagre in \(Y\) if \(A\cap W\) is nonmeagre in \(Y\) for every nonempty open \(W\subset Y\). Such a set is dense. Removing a meagre set preserves this property, since otherwise the original intersection with some open set would also be meagre.

**Lemma 2.1.** Two analytic sets that are everywhere nonmeagre in a nonempty separable metrizable space intersect.

*Proof.* Write \(A=\alpha(P)\), \(B=\beta(Q)\), with \(P,Q\) Polish. First remove parameter regions whose images are meagre. For \(\alpha\), let \(D\) be the union of all open \(V\subset P\) for which \(\alpha(V)\) is meagre in \(Y\). A countable base supplies a countable subfamily with the same union, so \(\alpha(D)\) is meagre. The closed space \(P_0=P\setminus D\) is Polish. Its image contains \(A\setminus\alpha(D)\), so it is still everywhere nonmeagre. Every nonempty relatively open \(V\subset P_0\) has nonmeagre image: write \(V=V'\cap P_0\) with \(V'\) open in \(P\). Since \(V'\) meets \(P_0\), its image is not meagre, and
\[
\alpha(V')\subset\alpha(V)\cup\alpha(D).
\tag{2.1}
\]
The desired assertion follows. Apply the same operation to \(\beta\), obtaining \(Q_0\). Restrict both maps to these closed spaces.

Choose complete compatible metrics on \(P_0,Q_0\) and a compatible metric on \(Y\). We construct nonempty open parameter sets \(U_n\subset P_0\), \(V_n\subset Q_0\), and nonempty open sets \(W_n\subset Y\), starting with \(U_0=P_0,V_0=Q_0,W_0=Y\). The induction preserves
\[
W_n\subset\overline{\alpha(U_n)}\cap\overline{\beta(V_n)}.
\tag{2.2}
\]
For \(n\geq0\), it also arranges
\[
\begin{aligned}
\overline{U_{n+1}}&\subset U_n,&\overline{V_{n+1}}&\subset V_n,\\
\alpha(U_{n+1})&\subset W_n,&\beta(V_{n+1})&\subset W_n,\\
W_{n+1}&\subset W_n,&
\operatorname{diam}U_{n+1},\operatorname{diam}V_{n+1},
\operatorname{diam}W_{n+1}&<2^{-(n+1)}.
\end{aligned}
\tag{2.3}
\]
All closures in (2.2) are in \(Y\); the parameter closures in (2.3) use their respective complete metrics.

Suppose the sets at stage \(n\) have been chosen. Density in (2.2) lets us choose a nonempty open \(U_{n+1}\) of small diameter, with closure in \(U_n\cap\alpha^{-1}(W_n)\). Its image is nonmeagre, by the parameter property just established. Consequently its closure has nonempty interior, and there is a nonempty open

\[
Z\subset W_n\cap\operatorname{int}\overline{\alpha(U_{n+1})}.
\tag{2.4}
\]
To justify the intersection with \(W_n\), the image is contained in \(W_n\); the boundary of an open set is nowhere dense, so a nonempty interior of its closure cannot live entirely on that boundary. The set \(\beta(V_n)\) is dense in \(W_n\), hence meets \(Z\). Choose a nonempty open \(V_{n+1}\) of small diameter whose closure lies in \(V_n\cap\beta^{-1}(Z)\). Its image is again nonmeagre. Choose a nonempty open \(W_{n+1}\) of diameter less than \(2^{-(n+1)}\), contained in \(Z\cap\operatorname{int}\overline{\beta(V_{n+1})}\). The same boundary argument makes this possible. This set lies in both closures required in (2.2), and all of (2.3) holds.

The nested nonempty closed parameter sets have diameters tending to zero. Completeness gives \(p\in\bigcap_{n\geq1}\overline{U_n}\) and \(q\in\bigcap_{n\geq1}\overline{V_n}\). The closure inclusions imply \(p\in U_n,q\in V_n\) for every \(n\geq0\). Thus \(\alpha(p),\beta(q)\in W_n\) for every \(n\), by using the image inclusions at stage \(n+1\). Since the diameters of \(W_n\) tend to zero, these two points coincide. They belong to \(A\cap B\). Completeness was used only in the parameter spaces, not in \(Y\). \(\square\)

This distinction matters: in the next section \(Y\) is an orbit with its relative topology, and its completeness is part of what we are trying to understand. Assuming that orbit is Polish at the start would make the proof circular.

**Alternative proof by Borel separation.** The following complete proof is adapted from Jochen Wengenroth, [*Effros' theorem on transitive group actions with a glimpse into descriptive set theory*](https://arxiv.org/abs/2512.00910v1), Theorem 3.4, version 1 of 30 November 2025, itself credited there to van Mill. **This paragraph and its proof are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)**. AI changes restrict the ambient space to the separable metrizable setting above, rename the sets, and use the exact written programme separation theorem.

Suppose \(A,B\subset Y\) are analytic, \(A\) is nonmeagre, and \(B\) is nowhere meagre. If they were disjoint, the written *Polish and standard Borel spaces*, Theorem 2.4, would give a Borel separator \(C\) with \(A\subset C\subset Y\setminus B\). Borel sets have the Baire property, so nonmeagre \(C\) is comeagre in some nonempty open \(W\). Then \(W\cap B\subset W\setminus C\) is meagre, contradicting the hypothesis on \(B\). Thus \(A\cap B\ne\varnothing\). This supplies a second complete proof of the intersection assertion while retaining the complete-parameter proof above.

**End of the CC BY-NC-SA component.** The surrounding independently written text retains its CC0 dedication. The complete Baire-property sigma-algebra argument used in this alternative is also supplied in the next lesson, Lemma 2.2.

## 3. Second category makes orbit maps open

**Theorem 3.1.** If an orbit \(O=Gx\) is of the second category in itself, then the action on \(O\) is microtransitive, and every orbit map \(g\mapsto gz\), \(z\in O\), is open onto \(O\).

*Proof.* All category and closure statements in this proof refer to \(O\). Choose a symmetric open identity-neighborhood base \(U_n\) with \(U_{n+1}^2\subset U_n\). Such a base is obtained recursively using continuity of multiplication and inversion.

First, \(U_nz\) is nonmeagre for every \(z\in O\). Indeed, countably many left translates of \(U_n\) cover \(G\), by second countability. Their translates of \(U_nz\) cover \(O\). If \(U_nz\) were meagre, so would \(O\) be, since each group element acts by a homeomorphism of \(O\).

More precisely, \(U_nz\cap A\) is nonmeagre whenever \(A\subset O\) is open and meets \(U_nz\). Pick \(hz\in A\) with \(h\in U_n\). The continuity of \(g\mapsto gz\) gives an identity neighborhood \(V\) with \(Vh\subset U_n\) and \(Vhz\subset A\). Choose \(U_m\subset V\). Then
\[
U_m(hz)\subset A\cap U_nz,
\tag{3.1}
\]
and the left side is nonmeagre by the preceding paragraph.

It follows that \(I_n(z)=\operatorname{int}_O\overline{U_nz}\) is dense in \(U_nz\). For an open set \(A\) meeting \(U_nz\), its intersection with that set is nonmeagre and therefore not nowhere dense. Its closure has nonempty interior. Since \(A\) is open, some such interior lies in \(A\cap I_n(z)\). It also meets \(U_nz\), by density in its closure.

We next show \(z\in I_n(z)\). Choose \(hz\in I_{n+1}(z)\cap U_{n+1}z\), possible by that density. The open set \(h^{-1}I_{n+1}(z)\) contains \(z\), and
\[
h^{-1}I_{n+1}(z)
\subset\overline{h^{-1}U_{n+1}z}
\subset\overline{U_nz}.
\tag{3.2}
\]
Here \(h^{-1}\in U_{n+1}\) and \(U_{n+1}^2\subset U_n\). Hence this open neighborhood is contained in \(I_n(z)\).

Finally, fix \(w\in I_{n+1}(z)\). The set
\[
E=I_{n+1}(z)\cap I_{n+1}(w)
\tag{3.3}
\]
is an open neighborhood of \(w\). The two sets \(U_{n+1}z\cap E\) and \(U_{n+1}w\cap E\) are dense and everywhere nonmeagre in \(E\), by (3.1) and the definition of \(I_{n+1}\). They are analytic: each is the continuous image of the open Polish subset \(\{g\in U_{n+1}:gz\in E\}\), or its analogue with \(w\). Lemma 2.1 applies to the separable metrizable space \(E\). Thus \(gz=hw\) for some \(g,h\in U_{n+1}\), and
\[
w=h^{-1}gz\in U_nz.
\tag{3.4}
\]
We have proved \(I_{n+1}(z)\subset U_nz\). Since \(z\in I_{n+1}(z)\), the latter is a neighborhood of \(z\). The identity-neighborhood base now gives microtransitivity for every identity neighborhood. Lemma 1.1 proves openness of the orbit maps. \(\square\)

## 4. The four orbit criteria

**Theorem 4.1 (Effros's orbit criterion).** For a continuous action of a Polish group on a Polish space, the following are equivalent:

1. For every \(x\in X\), the canonical map \(G/H_x\to Gx\) is a homeomorphism.
2. Every orbit is of the second category in its relative topology.
3. Every orbit is a \(G_\delta\) subset of \(X\).
4. The quotient \(X/G\) is \(T_0\): distinct points are distinguished by an open set containing one of them.

*Proof.* Condition 1 implies condition 2 by Lemma 1.2: the homogeneous space is a nonempty Baire space, and a nonempty Baire space cannot be meagre in itself. Condition 2 implies condition 1 by Theorem 3.1. Condition 3 implies condition 2 because a \(G_\delta\) subset of a Polish space is Polish in its relative topology, by the exact written prerequisite in the introduction, and hence is Baire.

Condition 2 also implies condition 3: Theorem 3.1 makes \(G\to Gx\) a continuous open surjection, and Lemma 1.3 shows that its image is \(G_\delta\) in \(X\). We prove condition 4 implies condition 3 directly. With a countable base \(U_n\) of \(X\), define
\[
c(x)_n=\mathbf 1_{GU_n}(x),\qquad c:X\to\{0,1\}^{\mathbb N}.
\tag{4.1}
\]
This is a Borel map constant on each orbit. The sets \(\pi(U_n)\) form a quotient base. Under \(T_0\), their membership patterns distinguish distinct quotient points, so \(c(x)=c(y)\) exactly when \(Gx=Gy\). Consequently
\[
Gx=
\left(\bigcap_{n:c(x)_n=1}GU_n\right)
\cap
\left(\bigcap_{n:c(x)_n=0}(X\setminus GU_n)\right).
\tag{4.2}
\]
The first intersection is \(G_\delta\); the second is closed. Every closed subset of a metric space is \(G_\delta\), using its distance neighborhoods. Formula (4.2) proves condition 3. Empty intersections mean \(X\).

For the converse, suppose every orbit is \(G_\delta\). Distinct orbits cannot have the same closure \(F\) in \(X\). If they did, they would be disjoint dense \(G_\delta\) subsets of the nonempty closed Polish space \(F\), contrary to its Baire property. If the closures of two orbits differ, a point of one lies outside the closure of the other, after exchanging their roles if necessary. An open neighborhood of that point misses the latter closed set. Its saturation also misses the latter orbit, because each orbit closure is invariant under every group element. The image of this saturation in \(X/G\) is an open set distinguishing the two quotient points. Thus condition 3 implies condition 4. Combining the implications proves all four equivalences. For \(X=\varnothing\), all four conditions are vacuous and the quotient is \(T_0\). \(\square\)

The countable code in (4.1) is also an explicit countable Borel separation of the orbit space when these conditions hold. It does not by itself prove that its image is a Borel subset of the Cantor space, nor that every invariant Borel set is generated by the invariant open sets. Those are different assertions.

## 5. Three orbit spaces

**Example 5.1 (Rotating the circle).** Let \(\mathbb Z\) act on \(\mathbb T\) by \(n\cdot z=e^{2\pi i n\theta}z\), with \(\theta\) irrational. Every orbit is dense. For completeness, the fractional parts of \(0,\theta,\ldots,N\theta\) place two points within \(1/N\). Their difference gives a nonzero multiple of \(\theta\) modulo one at distance less than \(1/N\) from zero. Taking its sign gives a step \(0<t<1/N\) in the generated subgroup. The points \(0,t,2t,\ldots,\lfloor1/t\rfloor t\) come within \(t\) of every point of \([0,1]\). Arbitrarily small such steps prove density.

An invariant closed nonempty set therefore contains a dense orbit and equals the circle. Taking complements shows that the only invariant open sets are the empty set and the whole circle. Thus the quotient topology is indiscrete. There are distinct orbits, since each orbit is countable and the circle is uncountable; the quotient fails \(T_0\). Each orbit is countable without isolated points, so it is meagre in itself and is not \(G_\delta\) in the circle. Its stabilizer is trivial, and the continuous bijection from the discrete group \(\mathbb Z\) onto the orbit is not a homeomorphism.

Irrationality is essential. The printed Exercise XIII.2(1)(a) does not state it. For \(\theta=p/q\) in lowest terms, the orbits have \(q\) points. The map \(z\mapsto z^q\) has exactly these fibres and identifies the quotient homeomorphically with a circle: it is a continuous open surjection with those fibres. For \(\theta=0\), the action is trivial and the quotient is the original circle. These are complete counterexamples to the unqualified assertion.

**Example 5.2 (Rational translation).** The countable discrete Polish group \(\mathbb Q\) acts continuously on \(\mathbb R\) by translation. Each orbit \(x+\mathbb Q\) is countable and dense, with no isolated point, and is meagre in itself. A nonempty invariant closed subset is all of \(\mathbb R\), so the quotient is again indiscrete and fails \(T_0\). The bijection from \(\mathbb Q\), in its discrete topology, to one of these orbits, in its relative topology, is not a homeomorphism. This is a locally compact group action already exhibiting the failure.

**Example 5.3 (Scaling through zero).** The Polish group \(\mathbb R_{>0}\) acts on \(\mathbb R\) by multiplication. The three orbits are \(P=(0,\infty)\), \(N=(-\infty,0)\), and \(Z=\{0\}\). The first two are open, and the third is closed, so every orbit is \(G_\delta\). The quotient's open sets are exactly
\[
\varnothing,\quad\{P\},\quad\{N\},\quad\{P,N\},\quad\{P,N,Z\}.
\tag{5.1}
\]
It is \(T_0\), but not \(T_1\): the closure of \({P}\) is \({P,Z}\), and similarly for \(N\). The canonical orbit maps are homeomorphisms. At a positive or negative point the stabilizer is trivial and scaling parametrizes its half-line; at zero the homogeneous space is a singleton. Thus Effros's conclusion does not require a Hausdorff orbit space.

## 6. Quotient Borel sets and the stronger criterion

The *quotient Borel structure* is
\[
\mathscr B_q(X/G)=\{A\subset X/G:\pi^{-1}(A)\text{ is Borel in }X\}.
\tag{6.1}
\]
It is a sigma-algebra containing the Borel sets generated by the quotient topology. A countable family separates it if it distinguishes each pair of distinct orbits. The code (4.1) gives such a family under Theorem 4.1, but identifying the entire sigma-algebra requires an additional proof.

Here are the exact regularity assumptions in Exercise XIII.2(2). Condition C says that for every identity neighborhood \(N\) there is an identity neighborhood \(M\subset N\) with \(\overline{Mx}\subset Nx\) for every \(x\in X\). Condition D says that \(M\) can be chosen so that, for every \(x\) and every open neighborhood base \(Q_n\) at \(x\),
\[
\bigcap_n\overline{M Q_n}\subset Nx.
\tag{6.2}
\]
These are closures of the orbit image and the product image, respectively, in \(X\). They must not be replaced by group closures or omitted.

**Proposition 6.1.** Every continuous action of a locally compact Polish group on a Polish space satisfies both C and D.

*Proof.* For a given identity neighborhood \(N\), choose a compact identity neighborhood \(M\subset N\). Continuity makes \(Mx\) compact, hence closed in the Hausdorff space \(X\); this proves C. For D, fix \(y\in\bigcap_n\overline{M Q_n}\), choose a compatible metric on \(X\), and choose indices \(n(k)\) with \(Q_{n(k)}\) contained in the radius \(1/k\) ball about \(x\). There are \(m_k\in M,z_k\in Q_{n(k)}\) with \(d(m_kz_k,y)<1/k\). Compactness gives a convergent subsequence of \(m_k\), with limit \(m\in M\), while \(z_k\to x\). Joint continuity gives \(y=mx\in Nx\). This works for an arbitrary neighborhood base, which need not be nested. \(\square\)

**Proposition 6.2.** If the quotient Borel structure is countably separated, every nonzero ergodic sigma-finite Borel measure on \(X\) is concentrated on one orbit. Quasi-invariance is unnecessary.

*Proof.* Pull back a separating family to invariant Borel sets \(A_n\subset X\). Ergodicity means \(\mu(A_n)=0\) or \(\mu(X\setminus A_n)=0\). Choose the full-measure side \(C_n\) for each \(n\). The Borel set \(C=\bigcap_n C_n\) has full measure. It is nonempty because \(\mu\) is nonzero. All of its points have the same membership pattern, so separation puts them in one orbit \(O\). In fact the same pattern's fibre is exactly \(O\), making \(O\) Borel as a countable intersection of the \(A_n\) or their complements. Hence \(\mu(X\setminus O)=0\). The proof uses neither a Radon property nor quasi-invariance; even sigma-finiteness is unnecessary for this implication. \(\square\)

The full Glimm criterion relates locally closed orbits to equality of the two quotient Borel structures, countable separation and ergodic concentration under C, with standardness and a Borel transversal under D. All these implications are proved in [Locally closed orbits and measurable representatives](locally-closed-orbits-and-measurable-representatives.md), Theorem 1.1 and Sections 2–6. Its closed-set selector construction in fact gives the six-way equivalence already under C.

## 7. Exercises with solutions

**Exercise 7.1.** *Level 1.* Prove that the sets \(\pi(U_n)\) in Section 1 form a base, rather than just a family generating the quotient topology.

*Solution.* If \(A\subset X/G\) is open and \(\pi(x)\in A\), choose a base element \(U_n\) with \(x\in U_n\subset\pi^{-1}(A)\). Since \(\pi^{-1}(A)\) is invariant, \(GU_n\subset\pi^{-1}(A)\). Therefore \(\pi(x)\in\pi(U_n)\subset A\). This is exactly the base condition.

**Exercise 7.2.** *Level 2.* In Lemma 2.1, explain why removing the bad parameter region must use a countable base. Explain also why completeness of \(Y\) is unnecessary.

*Solution.* An uncountable union of meagre images need not be meagre. Each point of the union of bad open parameter sets has a base neighborhood contained in one such set; its image is still meagre. The union is thus the union of countably many bad base neighborhoods, so its image is meagre. The only completeness step is the intersection of nested closed sets in \(P_0\) and \(Q_0\). The two resulting images already exist in \(Y\) by continuity. Their distance is at most the diameter of \(W_n\) for every \(n\), hence is zero; no limit needs to be constructed by completing \(Y\).

**Exercise 7.3.** *Level 2.* Locate the step in Theorem 3.1 that would fail if \(\mathbb Q\), with its usual topology, replaced the Polish acting group. Use its action on \(\mathbb R\) by translation.

*Solution.* The orbit is \(\mathbb Q\) with its usual topology, which is meagre in itself, so the second-category assumption fails before any conclusion can be drawn. There is also no justification that an open subset of the acting group is Polish; this is needed when applying Lemma 2.1. Thus this action does not contradict the theorem. Its orbit map is actually a homeomorphism from the usual-topology \(\mathbb Q\) onto that orbit, showing why the implication from homogeneous-space topology to category also needs the Polish, hence Baire, acting group. With the discrete topology the group is Polish, but the orbit map is no longer a homeomorphism, as Example 5.2 shows.

**Exercise 7.4.** *Level 1.* For rotation by \(\theta=2/5\), find the stabilizer of a point and a continuous quotient coordinate. Decide whether the quotient is indiscrete.

*Solution.* The equality \(e^{4\pi i n/5}=1\) holds exactly when \(5\mid n\), so every stabilizer is \(5\mathbb Z\). The orbit has five points. The coordinate \(z\mapsto z^5\) is constant precisely on each orbit and is an open continuous surjection to the circle, so it identifies the quotient with the circle. For example, the inverse image of a proper open arc is a nonempty proper invariant open set. The quotient is therefore not indiscrete.

**Exercise 7.5.** *Level 2.* In the scaling example, use the base of rational open intervals to distinguish \(P,N,Z\) by the code (4.1), and compute their quotient closures.

*Solution.* The saturation of \((1,2)\) is the positive half-line, giving a coordinate whose value is one only on \(P\). The saturation of \((-2,-1)\) is the negative half-line, giving a coordinate whose value is one only on \(N\). These distinguish all three points, since \(Z\) has value zero for both coordinates. Every quotient neighborhood of \(Z\) is the whole quotient, whereas \(P\) and \(N\) each have their own singleton open neighborhood. Therefore \(\overline{\{P\}}=\{P,Z\}\), \(\overline{\{N\}}=\{N,Z\}\), and \(\overline{\{Z\}}=\{Z\}\). The quotient is \(T_0\) and fails \(T_1\).

**Exercise 7.6.** *Level 3.* Suppose two disjoint orbits are both \(G_\delta\) in \(X\) and have the same closure \(F\). Give the Baire contradiction with all density assertions justified.

*Solution.* Write the orbits as \(\bigcap_n V_n\) and \(\bigcap_n W_n\), with \(V_n,W_n\) open in \(X\). Each \(V_n\cap F\) contains the first orbit, which is dense in \(F\), and is therefore open dense in \(F\); the same holds for \(W_n\cap F\). The space \(F\) is nonempty, closed in a Polish space, and hence Baire. The intersection of all these open dense sets is nonempty. A point in it belongs to both orbits, contradicting disjointness.

**Exercise 7.7.** *Level 2.* Produce an ergodic Borel probability measure which is not quasi-invariant under the whole scaling group, and verify Proposition 6.2 for it.

*Solution.* The point mass \(\delta_1\) is ergodic: an invariant Borel set either contains \(1\), giving full mass, or does not, giving zero mass. It is not quasi-invariant under multiplication by \(2\), since the null set \(\{2\}\) has inverse image \(\{1\}\), which has mass one. Nevertheless its mass is concentrated on the positive orbit \(P\). The countable orbit-separating family in Exercise 7.5 applies, exactly as Proposition 6.2 requires.

**Exercise 7.8.** *Level 3.* In Proposition 6.1, explain why taking a convergent subsequence of group elements without choosing \(z_k\to x\) would not prove D. Give the correct construction for an arbitrary, nonnested base.

*Solution.* Joint continuity yields \(m_kz_k\to mx\) only when the point sequence also tends to \(x\); compactness of \(M\) alone controls no \(z_k\). For each \(k\), select a base member \(Q_{n(k)}\subset B(x,1/k)\). Since \(y\in\overline{M Q_{n(k)}}\), select \(m_k\in M,z_k\in Q_{n(k)}\) with \(d(m_kz_k,y)<1/k\). Then \(z_k\to x\), independently of nesting. A subsequence \(m_{k_j}\to m\in M\) gives \(m_{k_j}z_{k_j}\to mx\), and the error estimate forces the same limit to be \(y\). Thus \(y=mx\in Mx\subset Nx\).

## References and provenance

The source exercise is Masamichi Takesaki, *Theory of Operator Algebras III* (2003), Exercise XIII.2 supplied PDF pages 50–51. Its rotation assertion needs the irrationality qualification supplied in Example 5.1. Bibliography entry [508] identifies Edward G. Effros, *Transformation Groups and C\*-Algebras*, *Annals of Mathematics* 81 (1965), 38–55, [publisher record](https://doi.org/10.2307/1970381).

The open-orbit result is due to E. G. Effros. The complete-open-image principle in Lemma 1.3 is classically attributed to Hausdorff; see the discussion of Theorem 1.1 in van Mill's note. Its entire metric-cover proof is given here. The complete-parameter intersection method and the passage from neighborhood closures to actual orbit neighborhoods are credited to Jan van Mill, [*A Note on the Effros Theorem*](https://staff.fnwi.uva.nl/j.vanmill/papers/papers2004/monthly.pdf), *American Mathematical Monthly* 111 (2004), 801–806, Proposition 2.2 and Lemmas 3.1–3.4/Proposition 3.5. Section 2 supplies a complete mathematical reconstruction with its own induction invariant; Sections 3–4 check the argument against the full Polish action hypotheses. Van Mill's mathematical method is credited here; a complete comparative expression and arrangement review of this component remains in progress. Section 2 additionally integrates Wengenroth's complete separation-based proof with the visible CC BY-NC-SA component notice and AI change description there. His broader nonmetrizable theorem is not silently substituted for the scope checked here. No formal verification of this lesson is claimed.

The Polish-subspace prerequisite is the actual written programme lesson *Effros Borel structure*, Theorem 2.1(1), in *Operator algebra foundations*: its complete proof is supplied there. The additional separation prerequisite is the written *Polish and standard Borel spaces*, Theorem 2.4. Their own prerequisites are not proved here. Definitions, examples, solutions and the quotient-code argument above are integrated course exposition. The next lesson completes the stronger Glimm exercise.
