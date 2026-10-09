# Borel models, measurable inversion and Polish group quotients

*Public domain (CC0).*

A measurable parameter should let us recover the object it names, integrate over its values, and choose a representative when several names describe the same object. These three tasks require different theorems. A continuous image can fail to be Borel; an injective Borel map between standard Borel spaces has a Borel inverse on its image; a general surjection needs a selection theorem with explicit measurability conditions. This lesson develops those distinctions as tools for operator-algebra constructions.

Follow the image and inversion route first, then the measure route, then the choice route. The final route treats topological quotients of Polish groups: its conclusion includes the quotient topology, not just a Borel structure. For example, different representatives of a coset describe the same point, and a section supplies one representative without asserting that the section is continuous. These questions prepare for direct integrals and measurable fields, where mistaking a merely measurable choice for a continuous one changes the theorem.

The exact elementary, measure and topology prerequisites are listed and proved or linked below. All four routes retain the complete separation, measure and selection theorems and their worked exercises.

## Conventions

- \(\mathbb N=\{1,2,3,\dots\}\). "Countable" means finite or countably infinite.
- Borel spaces, Borel maps and isomorphisms, generating and separating families, countably generated and countably separated spaces, Polish spaces and standard Borel spaces are as in [the lesson on the Effros Borel structure](the-effros-borel-structure.md#oa-fnd-ef-01). A measure \(\mu\) on a Borel space \(X\) is *standard* if \(X\setminus N\), with its relative Borel structure, is standard for some Borel set \(N\) with \(\mu(N)=0\).
- For a topological space \(X\), \(\mathcal B(X)\) is its Borel \(\sigma\)-algebra. A subset carries the relative topology and the relative Borel structure. The Borel sets of a subspace are exactly the traces of the Borel sets of the whole space. Indeed, the traces form a \(\sigma\)-algebra on the subspace that contains its open sets; and the sets whose trace is Borel in the subspace form a \(\sigma\)-algebra that contains the open sets. So the two structures agree.
- *The Baire space.* \(\Lambda=\mathbb N^{\mathbb N}\), with the product of discrete topologies. \(\mathbb N^{<\mathbb N}\) is the set of finite sequences \(s=(s_1,\dots,s_k)\), including the empty sequence; \(|s|=k\) is the length and \(sn=(s_1,\dots,s_k,n)\). For \(t\in\Lambda\), \(t|k=(t_1,\dots,t_k)\). The *cylinder* \(\Lambda_s=\{t\in\Lambda:t|\,|s|=s\}\) is open and closed, \(\Lambda_s\) is the disjoint union of the \(\Lambda_{sn}\), and the cylinders \(\Lambda_{t|k}\), \(k\geq0\), form a neighbourhood base at \(t\). For \(T\subseteq\Lambda\) put \(T_s=T\cap\Lambda_s\). The space \(\Lambda\) is Polish (F2). Nothing else about its metric is needed.
- *The Cantor space* \(\mathcal C=\{0,1\}^{\mathbb N}\) is compact and metrizable. Binary words \(\{0,1\}^{<\mathbb N}\) use the same notation.
- A space is *zero-dimensional* if each point has a neighbourhood base of sets that are both open and closed.
- For a topological space \(Z\), call \(A\subseteq Z\) a *Polish image* in \(Z\) if \(A=g(P)\) for some Polish space \(P\) and some continuous \(g:P\to Z\). The empty set is one.
- For a metric \(d\), distance to the empty set is \(d(x,\varnothing)=+\infty\).
- Measures, outer measures and completions are set up at the start of [Section 6](#oa-fnd-pb-09).

## Prerequisites

The following facts are proved in [the lesson on the Effros Borel structure](the-effros-borel-structure.md#oa-fnd-ef-01).

- **(F1)** *Generators.* A map into a Borel space is measurable when its compositions with a generating family of maps are measurable. A countable base of a topological space generates its Borel sets. In a countable product of second countable spaces, the coordinate maps generate the Borel sets.
- **(F2)** *A stock of Polish spaces.* Closed subsets and countable products of Polish spaces are Polish, and \(\mathbb N^{\mathbb N}\) is Polish. A separable metrizable space has at most \(2^{\aleph_0}\) points. A countable disjoint sum of Polish spaces is Polish. The prerequisite lesson treats two pieces, and its metric (distance \(1\) between pieces, \(\min(d,1)\) inside a piece) works for countably many pieces: a Cauchy sequence eventually stays in one piece, and the union of countable dense subsets of the pieces is countable and dense.
- **(F3)** *Polish subspaces*, proved in [the prerequisite lesson](the-effros-borel-structure.md#oa-fnd-ef-02). Every \(G_\delta\) subset of a Polish space, in particular every open subset, is Polish. A Polish space is homeomorphic to a \(G_\delta\) subset of \([0,1]^{\mathbb N}\).
- **(F4)** *Change of topology*, also proved in [the prerequisite lesson](the-effros-borel-structure.md#oa-fnd-ef-02). Call a topology \(\tau'\) *admissible* for a Polish space \((X,\tau)\) if \(\tau'\) is Polish, \(\tau'\supseteq\tau\), and \(\tau'\) has the same Borel sets as \(\tau\).
  - (a) For \(\tau\)-open \(U\), the topology generated by \(\tau\) and \(X\setminus U\) is admissible.
  - (b) The topology generated by countably many admissible topologies is admissible. A countable base of it consists of finite intersections of members of countable bases of the given topologies.
  - (c) Every Borel set is open and closed for some admissible topology.

  Consequently each Borel set in a standard Borel space is itself standard.

The measure prerequisites are proved in [Measure and Hilbert space tools for Haar integration](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html).

- *Carathéodory's theorem*, [Theorem 1.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#1-from-an-outer-measure-to-a-measure). Let \(\mu^*\) be an outer measure on \(X\). The sets \(E\) with \(\mu^*(W)=\mu^*(W\cap E)+\mu^*(W\setminus E)\) for every \(W\subseteq X\) form a sigma-algebra. The restriction of \(\mu^*\) to it is a complete measure. No finiteness or countability hypothesis is needed.
- *Lebesgue measure*, constructed in the example following that theorem. There is a complete measure \(\lambda\) on the Lebesgue measurable subsets of \(\mathbb R\), containing the Borel sets, with \(\lambda([a,b])=b-a\) for \(a\leq b\). Translating interval covers proves that translation preserves both measurable sets and their measures.

### Cardinality and elementary topology

Choice is understood throughout, as in Section 1 of the Hahn–Banach lesson. Its Theorem 8.2 and Proposition 8.3 give the cardinal facts used here: \(|X|<|\mathcal P(X)|=2^{|X|}\), \((\kappa^\lambda)^\mu=\kappa^{\lambda\cdot\mu}\), and \((2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}\). The pairing of countable indices is independent of whether they start at zero or one.

Translations and inversion in a topological group are homeomorphisms, by Proposition 7.1(1) of the Haar lesson. Two disjoint compact sets in a Hausdorff space have disjoint open neighbourhoods; its Theorem 2.4 proof, part (3), gives the finite-cover argument. We will also use the following metric fact.

**Lemma (Sequential compactness).** A compact metrizable space is sequentially compact.

*Proof.* Consider a sequence in a compact metric space. Some point \(x\) has every neighbourhood containing infinitely many sequence terms, counted with their indices. Otherwise choose at each point an open neighbourhood containing only finitely many terms; a finite subcover would contain only finitely many terms in total, a contradiction. Recursively choose increasing indices \(n_k\) with \(d(x_{n_k},x)<1/k\). Then \(x_{n_k}\to x\). \(\square\)


## Elementary facts

These five facts are used throughout. Each has a short proof.

- **(B1)** (Cantor's intersection theorem) In a complete metric space, a decreasing sequence of nonempty closed sets \(F_k\) whose diameters tend to \(0\) has exactly one common point. Pick \(x_k\in F_k\); for \(j\geq k\), \(d(x_j,x_k)\leq\operatorname{diam}F_k\), so the sequence is Cauchy. Its limit lies in every closed \(F_k\), and two common points are at distance at most \(\operatorname{diam}F_k\) for every \(k\).
- **(B2)** A countable product \(\prod_iF_i\) of finite discrete sets is compact. Suppose an open cover has no finite subcover of \(\prod_iF_i\). Call a finite sequence \(s\) with \(s_i\in F_i\) *bad* if the cylinder of points beginning with \(s\) has no finite subcover. The empty sequence is bad, and a bad \(s\) has a bad one-step extension, since the finitely many extensions cover its cylinder. So some point \(t\) has every \(t|j\) bad. But \(t\) lies in a member of the cover, which contains the cylinder of some \(t|j\), a contradiction. In particular \(\mathcal C\) is compact.
- **(B3)** A continuous injection \(f\) of a compact space \(K\) into a Hausdorff space is a homeomorphism onto \(f(K)\): closed subsets of \(K\) are compact, so their images are compact, hence closed.
- **(B4)** A second countable space is Lindelöf. Given an open cover, choose for each basic open set that lies in some member of the cover one such member. These countably many members cover the space, because each point lies in a basic open set that lies inside some member of the cover.
- **(B5)** In a topological group, every neighbourhood \(W\) of \(1\) contains \(V^2\) for some open neighbourhood \(V\) of \(1\) with \(V=V^{-1}\). Continuity of multiplication at \((1,1)\) gives open neighbourhoods \(V_1,V_2\) of \(1\) with \(V_1V_2\subseteq W\); take \(V=V_0\cap V_0^{-1}\) with \(V_0=V_1\cap V_2\), which is open because inversion is a homeomorphism.

## A. Encode an image and recover its parameter

Trees encode successive approximations, and the Baire space supplies a common domain for those encodings. Separation of disjoint Souslin sets is the step that makes injective images behave better than arbitrary images. Lusin–Souslin then turns injectivity into measurable inversion. The standard Borel classification records what survives when only measurable sets, rather than a topology, are retained.

### 1. Trees in Polish spaces

Two tree constructions run through this lesson. A countably branching tree of closed sets shows that every nonempty Polish space is a continuous image of the Baire space. A binary tree of open balls places a copy of the Cantor space inside every uncountable Polish space.

**Theorem 1.1** (Continuous images of the Baire space). Let \(X\) be a nonempty Polish space with a complete compatible metric \(d\). There are nonempty closed sets \(F_s\subseteq X\), \(s\in\mathbb N^{<\mathbb N}\), with
\[
\begin{gathered}
F_\varnothing=X,\\
F_s=\bigcup_{n\in\mathbb N}F_{sn},\\
\operatorname{diam}F_s\leq2^{-|s|}\ \ (|s|\geq1).
\end{gathered}
\tag{1}
\]
For every family as in (1), \(\{\varphi(t)\}=\bigcap_kF_{t|k}\) defines a continuous map \(\varphi:\Lambda\to X\) with \(\varphi(\Lambda_s)=F_s\) for all \(s\). In particular \(\varphi\) maps \(\Lambda\) onto \(X\).

**Proof.** *The sets.* Let \(F\) be a nonempty closed set and \(r>0\). \(F\) is separable, so it has a dense sequence \((a_n)\); if \(F\) is finite, repeat its points. The closed balls \(\{x:d(x,a_n)\leq r/2\}\) meet \(F\) in nonempty closed sets of diameter at most \(r\), and these cover \(F\), since each point of \(F\) is within \(r/2\) of some \(a_n\). Start with \(F_\varnothing=X\), and apply this to \(F_s\) with \(r=2^{-|s|-1}\) to obtain the sets \(F_{sn}\).

*The map.* For \(t\in\Lambda\), the sets \(F_{t|k}\) are nonempty, closed and decreasing, and their diameters tend to \(0\). By Cantor's intersection theorem (B1) they have exactly one common point \(\varphi(t)\). If \(t|k=u|k\), then \(\varphi(t)\) and \(\varphi(u)\) lie in \(F_{t|k}\), so \(d(\varphi(t),\varphi(u))\leq2^{-k}\); thus \(\varphi\) is continuous. Clearly \(\varphi(\Lambda_s)\subseteq F_s\). Conversely, let \(x\in F_s\) with \(|s|=k\). Put \(t|k=s\) and choose \(t_{k+1},t_{k+2},\dots\) one at a time so that \(x\in F_{t|j}\) for every \(j\); this is possible because \(F_{t|j}=\bigcup_nF_{(t|j)n}\). Then \(x\in\bigcap_jF_{t|j}\), so \(\varphi(t)=x\) with \(t\in\Lambda_s\). \(\square\)

**Remark 1.2.** Both nonemptiness conditions are needed. The empty metric space is complete and separable, hence Polish, and no map from \(\Lambda\) into it exists. And if one set \(F_s\) of the tree were empty, the intersection along every branch through \(s\) would be empty. Repeating points, as in the proof, keeps every piece nonempty.

**Lemma 1.3** (Perfect set lemma). Every uncountable Polish space \(X\) contains a compact subset homeomorphic to \(\mathcal C\). Hence \(|X|=2^{\aleph_0}\).

**Proof.** Let \(d\) be a complete compatible metric and \((W_j)\) a countable base. Let \(X'\) be the set of points all of whose neighbourhoods are uncountable. A point outside \(X'\) has a countable neighbourhood, hence a countable basic neighbourhood \(W_j\). So \(X\setminus X'\) lies in the union of the countable sets \(W_j\), and it is countable. Since \(X\) is uncountable, \(X'\neq\varnothing\). If an open set \(V\) meets \(X'\), then \(V\) is uncountable while \(V\setminus X'\) is countable, so \(V\cap X'\) is uncountable.

Choose open sets \(U_s\), \(s\in\{0,1\}^{<\mathbb N}\), each meeting \(X'\), as follows. Put \(U_\varnothing=X\). Given \(U_s\), pick two different points \(a,b\in U_s\cap X'\) and \(r>0\) with \(3r<d(a,b)\), \(r\leq2^{-|s|-2}\), and the balls of radius \(2r\) about \(a\) and \(b\) inside \(U_s\). Let \(U_{s0}\) and \(U_{s1}\) be the open balls of radius \(r\) about \(a\) and \(b\). Their closures lie in \(U_s\) and are disjoint, their diameters are at most \(2^{-|s|-1}\), and they meet \(X'\) at \(a\) and \(b\).

For \(c\in\mathcal C\), the closed sets \(\overline{U_{c|k}}\), \(k\geq1\), are nonempty and decreasing, and their diameters tend to \(0\). So they have one common point \(e(c)\), by Cantor's intersection theorem (B1). If \(c|k=c'|k\), then \(d(e(c),e(c'))\leq2^{-k}\), so \(e\) is continuous. If \(c\) and \(c'\) first differ at place \(k+1\), then \(e(c)\) and \(e(c')\) lie in the disjoint closures of \(U_{(c|k)0}\) and \(U_{(c|k)1}\), so \(e\) is injective. The space \(\mathcal C\) is compact (B2), and a continuous injection of a compact space into a Hausdorff space is a homeomorphism onto its image (B3). So \(e\) is a homeomorphism onto the compact set \(e(\mathcal C)\). Finally \(|X|\geq|\mathcal C|=2^{\aleph_0}\), and \(|X|\leq2^{\aleph_0}\) because \(X\) is separable and metrizable (F2). \(\square\)

### 2. Souslin sets

A continuous image of a Polish space need not be Polish, and it need not even be Borel. Such images are the Souslin sets. This section shows that they are closed under countable unions, countable intersections and countable products, that disjoint Souslin sets can be separated by Borel sets, and that every Borel set is a Souslin set but not conversely.

#### Definition and closure properties

**Definition 2.1.** A *Souslin space*, also called an analytic space, is a metrizable space onto which some Polish space maps continuously. A *Souslin set* in a topological space \(Z\) is a subset of \(Z\) that, with the relative topology, is a Souslin space.

So the Souslin sets of a metrizable space are exactly its Polish images. The empty space is a Souslin space. A nonempty Souslin space is the image of \(\Lambda\) under a continuous map: compose a continuous map of \(\Lambda\) onto the Polish space ([Theorem 1.1](#oa-fnd-pb-01)) with the given map. Whether a set is a Souslin set depends only on the set with its own topology. Hence a Souslin set of a subspace \(Y\subseteq Z\) is a Souslin set of \(Z\), and a subset of \(Y\) that is a Souslin set of \(Z\) is one of \(Y\).

**Proposition 2.2.**

1. A Souslin space is separable, and its Borel structure is countably generated and countably separated.
2. If \(X\) is a Souslin space, \(Y\) is metrizable and \(f:X\to Y\) is continuous, then the subset \(f(X)\) of \(Y\) is a Souslin set.
3. A countable product of Souslin spaces is a Souslin space.
4. Let \(Z\) be a Hausdorff space and \(A_1,A_2,\ldots\) Polish images in \(Z\). Then \(\bigcup_nA_n\) and \(\bigcap_nA_n\) are Polish images in \(Z\). In particular, in a metrizable space countable unions and countable intersections of Souslin sets are Souslin sets.
5. Open subsets and closed subsets of a Souslin space are Souslin sets.
6. Let \(f:X\to Y\) be a continuous map between metrizable spaces, and \(A\subseteq X\), \(A'\subseteq Y\) Souslin sets. Then \(f(A)\) and \(A\cap f^{-1}(A')\) are Souslin sets.

**Proof.** (1) A continuous image of a separable space is separable. A separable metrizable space has a countable base: the balls with rational radii about the points of a countable dense set. This base generates the Borel sets (F1), and it separates points, because for \(x\neq y\) a small ball about \(x\) misses \(y\).

(2) Compose \(f\) with a continuous surjection from a Polish space onto \(X\). The image \(f(X)\) is metrizable, being a subset of \(Y\).

(3) If \(g_n:P_n\to X_n\) are continuous surjections from Polish spaces, the product map \(\prod_ng_n:\prod_nP_n\to\prod_nX_n\) is a continuous surjection. \(\prod_nP_n\) is Polish, since countable products of Polish spaces are Polish (F2), and a countable product of metrizable spaces is metrizable.

(4) Let \(g_n:P_n\to Z\) be continuous with \(g_n(P_n)=A_n\) and \(P_n\) Polish. For the union, let \(P\) be the disjoint sum of the \(P_n\), which is Polish (F2), and let \(g=g_n\) on \(P_n\). For the intersection, let
\[
\begin{gathered}
P=\{(p_n)\in\textstyle\prod_nP_n:\\
 \ g_1(p_1)=g_n(p_n)\text{ for all }n\}.
\end{gathered}
\]
The diagonal of \(Z\times Z\) is closed because \(Z\) is Hausdorff, and \(P\) is the intersection of its preimages under the continuous maps \((p_n)\mapsto(g_1(p_1),g_n(p_n))\). So \(P\) is closed in \(\prod_nP_n\), hence Polish (F2). The map \((p_n)\mapsto g_1(p_1)\) is continuous on \(P\) and its image is \(\bigcap_nA_n\): for \(x\) in the intersection, choose \(p_n\in g_n^{-1}(x)\). Every subset of a metrizable space is metrizable, which gives the last sentence.

(5) Let \(g:P\to X\) be a continuous surjection from a Polish space. For \(U\) open in \(X\), \(g^{-1}(U)\) is open in \(P\), hence Polish (F3), and \(g\) maps it onto \(U\). For \(F\) closed, \(g^{-1}(F)\) is closed, hence Polish (F2), and \(g\) maps it onto \(F\).

(6) \(f(A)\) is a Souslin set by (2), applied to \(f\) restricted to \(A\). Next, \(A\times A'\) is a Souslin space by (3), and \(G=\{(a,b)\in A\times A':f(a)=b\}\) is closed in it because \(Y\) is Hausdorff; so \(G\) is a Souslin set by (5). The first projection is continuous and maps \(G\) onto \(A\cap f^{-1}(A')\), so (2) applies. \(\square\)

Borel subsets of Souslin spaces are Souslin sets as well; this is Corollary 2.6 below.

#### The separation theorem

Two subsets \(E,E'\) of a Borel space are *Borel-separated* if some Borel set \(B\) has \(E\subseteq B\) and \(B\cap E'=\varnothing\).

**Lemma 2.3.** Let \(E_n,E'_m\) (\(n,m\in\mathbb N\)) be subsets of a Borel space, and for all \(n\) and \(m\) let \(B_{n,m}\) be a Borel set that contains \(E_n\) and misses \(E'_m\). Then \(\bigcup_nE_n\) and \(\bigcup_mE'_m\) are Borel-separated by
\[
B=\bigcup_n\bigcap_mB_{n,m}.
\tag{2}
\]

**Proof.** \(E_n\subseteq\bigcap_mB_{n,m}\subseteq B\). If \(x\in B\), then \(x\in B_{n,m}\) for one \(n\) and every \(m\), so \(x\) lies in no \(E'_m\). \(\square\)

So, by (2), if \(\bigcup_nE_n\) and \(\bigcup_mE'_m\) are not Borel-separated, then some pair \(E_n,E'_m\) is not Borel-separated.

**Theorem 2.4** (Lusin's separation theorem). Let \(X\) be a Hausdorff space and \((X_n)_{n\in I}\), with \(I\) countable, pairwise disjoint Polish images in \(X\). There are pairwise disjoint Borel sets \(B_n\) with \(X_n\subseteq B_n\). In particular this holds for pairwise disjoint Souslin sets of a metrizable space.


**Proof.** *Two sets.* Let \(Y,Y'\) be disjoint Polish images. If \(Y=\varnothing\), take \(B=\varnothing\); if \(Y'=\varnothing\), take \(B=X\). Otherwise there are continuous maps \(f,f':\Lambda\to X\) with \(f(\Lambda)=Y\) and \(f'(\Lambda)=Y'\): compose continuous maps of \(\Lambda\) onto the Polish spaces ([Theorem 1.1](#oa-fnd-pb-01)) with the given maps. Put \(Y_s=f(\Lambda_s)\) and \(Y'_s=f'(\Lambda_s)\); then \(Y_s=\bigcup_nY_{sn}\) and \(Y'_s=\bigcup_nY'_{sn}\).

Suppose \(Y\) and \(Y'\) are not Borel-separated. By Lemma 2.3 there are \(n_1,m_1\) with \(Y_{(n_1)}\) and \(Y'_{(m_1)}\) not Borel-separated. Applying the lemma again, to \(Y_{(n_1)}=\bigcup_nY_{(n_1,n)}\) and \(Y'_{(m_1)}=\bigcup_mY'_{(m_1,m)}\), and so on, we get \(t,t'\in\Lambda\) such that \(Y_{t|k}\) and \(Y'_{t'|k}\) are not Borel-separated for any \(k\). The points \(f(t)\in Y\) and \(f'(t')\in Y'\) are different, because \(Y\) and \(Y'\) are disjoint. Since \(X\) is Hausdorff, they have disjoint open neighbourhoods \(V\) and \(W\). The open set \(f^{-1}(V)\) contains \(t\), hence contains \(\Lambda_{t|k}\) for all large \(k\); likewise \(f'^{-1}(W)\supseteq\Lambda_{t'|k}\) for all large \(k\). For such \(k\), \(Y_{t|k}\subseteq V\) and \(Y'_{t'|k}\subseteq W\subseteq X\setminus V\). So the open set \(V\) separates them, which is a contradiction.

*Countably many sets.* Number the index set \(1,2,\ldots\). For \(n\neq m\) choose a Borel set \(B_{n,m}\supseteq X_n\) with \(B_{n,m}\cap X_m=\varnothing\). Put \(C_n=\bigcap_{m\neq n}B_{n,m}\) and \(B_n=C_n\setminus(C_1\cup\cdots\cup C_{n-1})\). These sets are Borel and pairwise disjoint. \(X_n\subseteq C_n\), and for \(j<n\), \(X_n\cap C_j\subseteq X_n\cap B_{j,n}=\varnothing\). So \(X_n\subseteq B_n\). \(\square\)

**Corollary 2.5** (Souslin's theorem). Let \(X\) be a Hausdorff space and \(A\subseteq X\). If \(A\) and \(X\setminus A\) are both Polish images, then \(A\) is Borel. In particular, in a metrizable space a Souslin set whose complement is a Souslin set is Borel.


**Proof.** By Theorem 2.4, some Borel set contains \(A\) and misses \(X\setminus A\). Such a set is \(A\). \(\square\)

#### Borel sets and Souslin sets

**Corollary 2.6** (Borel subsets of Souslin spaces). Every Borel set in a Souslin space is itself a Souslin set. In particular, all Borel subsets of Polish spaces are Souslin sets.

**Proof.** Let \(g:P\to X\) be a continuous surjection from a Polish space, and \(B\subseteq X\) Borel. The set \(g^{-1}(B)\) is Borel in \(P\). By the change-of-topology theorem (F4)(c), \(P\) has a Polish topology, finer than the given one and with the same Borel sets, in which \(g^{-1}(B)\) is closed. Then \(g^{-1}(B)\) is Polish in the finer topology (F2), \(g\) is still continuous on it, and \(g\) maps it onto \(B\) because \(g\) is onto. \(B\) is metrizable as a subset of \(X\). \(\square\)

**Remark 2.7.** So in a Polish space the Borel sets are exactly the Souslin sets whose complements are Souslin sets: one direction is Corollary 2.6, the other is Souslin's theorem. Example 2.9 gives a Souslin set that is not Borel, so Souslin's theorem has content.

**Corollary 2.8** (Counting). A Polish space has at most \(2^{\aleph_0}\) Souslin sets, and so at most \(2^{\aleph_0}\) Borel sets. Consequently \(\mathcal C\) has subsets that are not Borel.

**Proof.** Let \(X\) be Polish. A nonempty Souslin set of \(X\) has the form \(h(\Lambda)\) with \(h:\Lambda\to X\) continuous, as noted after Definition 2.1. The sequences that equal \(1\) from some place on form a countable dense set \(D_0\subseteq\Lambda\), and a continuous map into a Hausdorff space is determined by its values on a dense set. Since \(|X|\leq2^{\aleph_0}\) (F2), there are at most \(|X|^{\aleph_0}\leq(2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}\) such maps. By Corollary 2.6, Borel sets are Souslin sets. The space \(\mathcal C\) has \(2^{2^{\aleph_0}}\) subsets, and \(2^{2^{\aleph_0}}>2^{\aleph_0}\) by Cantor's theorem. \(\square\)

**Example 2.9** (A Souslin set that is not Borel). Let \(Z=\mathcal C\times\Lambda\), a Polish space, with a countable base \((V_n)_{n\geq1}\).

(a) The set \[
\begin{gathered}
O\\
=\{(y,z)\in\mathcal C\times Z:\ y_n=1\text{ and }z\in V_n\\
\text{ for some }n\}
\end{gathered}
\] is open, being the union of the open sets \(\{y:y_n=1\}\times V_n\). For an open \(W\subseteq Z\), let \(y_n=1\) exactly when \(V_n\subseteq W\); then the section \(O_y=\{z:(y,z)\in O\}\) equals \(W\). So \(F=(\mathcal C\times Z)\setminus O\) is a closed set whose sections \(F_y\) run through all closed subsets of \(Z\).

(b) Let \[
\begin{gathered}
U\\
=\{(y,x)\in\mathcal C\times\mathcal C:\ (y,x,w)\in F\\
\text{ for some }w\in\Lambda\},
\end{gathered}
\] the projection of \(F\) along \(\Lambda\). It is a Souslin set of \(\mathcal C\times\mathcal C\), being the image of the Polish space \(F\) under a continuous map. Every Souslin set \(A\subseteq\mathcal C\) is a section \(U_y\). If \(A=\varnothing\), take \(y\) with \(F_y=\varnothing\). Otherwise \(A=g(\Lambda)\) with \(g\) continuous, as noted after Definition 2.1; the set \(K=\{(g(w),w):w\in\Lambda\}\) is closed in \(Z\) because \(\mathcal C\) is Hausdorff, its projection to \(\mathcal C\) is \(A\), and we take \(y\) with \(F_y=K\).

(c) Let \(D=\{x\in\mathcal C:(x,x)\in U\}\). It is the projection to \(\mathcal C\) of the closed set \(\{(x,w)\in\mathcal C\times\Lambda:(x,x,w)\in F\}\), so \(D\) is a Souslin set. If \(D\) were Borel, \(\mathcal C\setminus D\) would be Borel, hence a Souslin set (Corollary 2.6), hence \(\mathcal C\setminus D=U_{y_0}\) for some \(y_0\). Then \(y_0\in D\) exactly when \((y_0,y_0)\in U\), that is, exactly when \(y_0\in U_{y_0}=\mathcal C\setminus D\). This is absurd. So \(D\) is a Souslin set that is not Borel, and by Souslin's theorem its complement is not a Souslin set.

The argument in (c) is Cantor's diagonal argument, applied to the universal set \(U\). It shows that the image of a closed set under a continuous map need not be Borel: \(D\) is the projection of a closed subset of \(\mathcal C\times\Lambda\). This is a strong form of the fact that Borel maps need not carry Borel sets to Borel sets. Examples 5.9 and 6.4 return to \(D\).

### 3. Lusin spaces and one-to-one images

A one-to-one continuous image of a Polish space in a Hausdorff space is always Borel. This is the Lusin–Souslin theorem, the main result of this section. The tool is a change of topology that makes a Polish space zero-dimensional without changing its Borel sets. A zero-dimensional Polish space is a closed subset of the Baire space, where tree arguments apply.

#### Lusin spaces and closed subsets of the Baire space

**Lemma 3.1** (Zero-dimensional refinement). Let \((X,\tau)\) be a Polish space and \(B_1,B_2,\ldots\) Borel sets. There is a zero-dimensional Polish topology \(\tau'\supseteq\tau\) with the same Borel sets as \(\tau\), in which every \(B_n\) is open and closed.

**Proof.** We use the change-of-topology theorem (F4). By (F4)(c), each \(B_n\) is open and closed for some admissible topology \(\tau_n\). By (F4)(b), the topology \(\tau''\) generated by \(\tau\) and all the \(\tau_n\) is admissible; if there are no sets \(B_n\), then \(\tau''=\tau\). Each \(B_n\) is open and closed in \(\tau''\), since this property passes to finer topologies.

Let \((U_m)\) be a countable base of \(\tau''\). By (F4)(a), applied to the Polish space \((X,\tau'')\), the topology \(\tau''_m\) generated by \(\tau''\) and \(X\setminus U_m\) is admissible for \(\tau''\). Let \(\tau'\) be generated by all the \(\tau''_m\). By (F4)(b) it is admissible for \(\tau''\), hence for \(\tau\), because \(\tau''\) and \(\tau\) have the same Borel sets. Each \(\tau''_m\) has the countable base formed by the sets \(U_j\) and \(U_j\setminus U_m\). So the finite intersections of sets \(U_j\) and \(X\setminus U_{m}\) form a base of \(\tau'\). All these sets are open and closed in \(\tau'\). So \(\tau'\) is zero-dimensional. \(\square\)

This is the change-of-topology technique of [the lesson on the Effros Borel structure](the-effros-borel-structure.md#oa-fnd-ef-02), used once more to make a whole base open and closed.

**Definition 3.2.** A metrizable space \(X\) is a *Lusin space* if some zero-dimensional Polish space maps continuously and bijectively onto \(X\). A *Lusin set* in a topological space \(Z\) is a subset of \(Z\) that, with the relative topology, is a Lusin space.

**Proposition 3.3.**

1. A metrizable space is a Lusin space if and only if some Polish space, zero-dimensional or not, maps continuously and bijectively onto it. So zero-dimensionality in the definition costs nothing.
2. Polish spaces are Lusin spaces, and Lusin spaces are Souslin spaces.
3. In a Hausdorff space, a countable intersection of Lusin sets is a Lusin set.
4. A countable union of pairwise disjoint Lusin sets of a metrizable space is a Lusin set.
5. Open subsets, closed subsets and \(G_\delta\) subsets of a Lusin space are Lusin sets.
6. A countable product of Lusin spaces is a Lusin space.

Example 3.8 proves that the intersection assertion (3) needs the Hausdorff hypothesis on the ambient space.

**Proof.** (1) If \(f:P\to X\) is a continuous bijection from a Polish space, refine the topology of \(P\) by Lemma 3.1, with no sets \(B_n\). The new topology is zero-dimensional and Polish, and \(f\) stays continuous because the topology became finer.

(2) The identity map of \(X\), from a zero-dimensional refinement to the given topology, is a continuous bijection. The second statement is clear.

(3) Let \(f_n:P_n\to L_n\) be continuous bijections from zero-dimensional Polish spaces onto Lusin sets \(L_n\) of a Hausdorff space \(Z\). As in the proof of Proposition 2.2(4), the set \(P=\{(p_n):f_1(p_1)=f_n(p_n)\text{ for all }n\}\) is closed in \(\prod_nP_n\), because the diagonal of \(Z\times Z\) is closed. The map \((p_n)\mapsto f_1(p_1)\) sends \(P\) continuously onto \(\bigcap_nL_n\). It is injective: \(f_1(p_1)=f_1(q_1)\) gives \(p_1=q_1\), then \(f_n(p_n)=f_n(q_n)\), so \(p_n=q_n\) for all \(n\). A product of zero-dimensional spaces is zero-dimensional, since boxes built from finitely many open and closed sets are open and closed and form a base; a subspace of a zero-dimensional space is zero-dimensional. Finally \(\bigcap_nL_n\subseteq L_1\) is metrizable.

(4) With \(f_n\) as before and the \(L_n\) pairwise disjoint, the disjoint sum of the \(P_n\) is zero-dimensional and Polish, and the map equal to \(f_n\) on \(P_n\) is a continuous bijection onto \(\bigcup_nL_n\). This union is metrizable, being a subset of a metrizable space.

(5) Let \(f:P\to L\) be a continuous bijection from a zero-dimensional Polish space. For \(U\) open in \(L\), \(f^{-1}(U)\) is open in \(P\), hence Polish (F3) and zero-dimensional, and \(f\) maps it bijectively onto \(U\). Closed sets are handled the same way, using (F2). A \(G_\delta\) subset of \(L\) is a countable intersection of open subsets, which are Lusin sets of the metrizable space \(L\); apply (3).

(6) The product of continuous bijections \(f_n:P_n\to L_n\) is a continuous bijection \(\prod_nP_n\to\prod_nL_n\). The domain is zero-dimensional and Polish, and the target is metrizable. \(\square\)

*Another proof of (2).* The irrational numbers \(J\) in \(I=[0,1]\) form a Lusin set. Indeed, \(J\) is a \(G_\delta\) subset of \(I\), hence Polish (F3). The sets \(J\cap(r,s)\) with \(r,s\) rational are open and closed in \(J\), because their endpoints are not in \(J\), and they form a neighbourhood base; so \(J\) is zero-dimensional. Then \(I\) is the disjoint union of \(J\) and countably many points, each a Lusin set, so \(I\) is a Lusin space by (4). Next \(I^{\mathbb N}\) is a Lusin space by (6). Finally a Polish space is homeomorphic to a \(G_\delta\) subset of \(I^{\mathbb N}\) (F3), and so it is a Lusin set by (5).

**Theorem 3.4** (Closed subsets of the Baire space).

1. Every zero-dimensional Polish space is homeomorphic to a closed subset of \(\Lambda\).
2. For every Lusin space \(X\), in particular for every Polish space, there are a closed set \(T\subseteq\Lambda\) and a continuous bijection of \(T\) onto \(X\).
3. The closed set \(T\) in (2) cannot in general be a product \(\prod_kN_k\) in which each \(N_k\) is \(\mathbb N\) or a finite set \(\{1,\dots,N_k\}\): the Polish space \(X=[0,1]\cup\{2\}\subseteq\mathbb R\) is not the image of any such product under a continuous bijection.

The explicit isolated-point argument in (3) proves that the closed tree in (2) cannot always be replaced by a product.

**Proof.** (1) Let \(P\) be a zero-dimensional Polish space with a complete compatible metric \(d\).

*Step 1: partitions.* Let \(Q\subseteq P\) be open and closed, and \(r>0\). Each \(x\in Q\) has an open and closed neighbourhood inside \(Q\cap\{y:d(x,y)<r/3\}\). These neighbourhoods cover \(Q\). Since \(Q\) is second countable, it is Lindelöf (B4), so countably many of them, \(D_1,D_2,\ldots\), cover \(Q\). The sets \(D_j\setminus(D_1\cup\cdots\cup D_{j-1})\) are open and closed, pairwise disjoint, of diameter at most \(r\), and they cover \(Q\). If there are only finitely many, add empty sets.

*Step 2: the tree.* By Step 1, choose open and closed sets \(P_s\), \(s\in\mathbb N^{<\mathbb N}\), with \(P_\varnothing=P\), each \(P_s\) the disjoint union of the sets \(P_{sn}\) (\(n\in\mathbb N\)), and \(\operatorname{diam}P_s\leq2^{-|s|}\) for \(|s|\geq1\). By induction, for each \(k\) the sets \(P_s\) with \(|s|=k\) partition \(P\). Let \(T=\{t\in\Lambda:P_{t|k}\neq\varnothing\text{ for all }k\}\). If \(t\notin T\), some \(P_{t|k}\) is empty and the whole cylinder \(\Lambda_{t|k}\) misses \(T\); so \(T\) is closed. For \(t\in T\), the sets \(P_{t|k}\) are nonempty, closed and decreasing with diameters tending to \(0\), so they have one common point \(\psi(t)\), by Cantor's intersection theorem (B1).

*Step 3: \(\psi:T\to P\) is a homeomorphism.* If \(t|k=u|k\), then \(d(\psi(t),\psi(u))\leq2^{-k}\); so \(\psi\) is continuous. If \(t\) and \(u\) first differ at place \(k+1\), then \(\psi(t)\) and \(\psi(u)\) lie in the disjoint sets \(P_{t|k+1}\) and \(P_{u|k+1}\); so \(\psi\) is injective. For \(x\in P\), at each level exactly one \(P_s\) contains \(x\), and these \(s\) extend each other; they define \(t\in T\) with \(\psi(t)=x\). The same argument shows \(\psi(T_s)=P_s\) for every \(s\), because a point of \(P_s\) is reached only along sequences that extend \(s\). The sets \(T_s\) form a base of \(T\) and the sets \(P_s\) are open, so \(\psi\) is open.

(2) By Proposition 3.3(1), some zero-dimensional Polish space \(P\) maps continuously and bijectively onto \(X\), say by \(f\). With \(\psi\) as in (1), \(f\circ\psi\) is a continuous bijection of the closed set \(T\) onto \(X\).

(3) Suppose \(\varphi:\prod_kN_k\to X\) is a continuous bijection. \(X\) is uncountable, so infinitely many \(N_k\) have at least two elements; otherwise the product would be countable. Then every nonempty open subset of the product has at least two points, because a basic open set restricts only finitely many coordinates. But \(2\) is an isolated point of \(X\), so \(\varphi^{-1}(\{2\})\) is open, and it has exactly one point because \(\varphi\) is bijective. This is a contradiction. \(\square\)

**Example 3.5** (A tree, not a product). By Theorem 3.4(3), no product \(\prod_kN_k\) maps continuously and bijectively onto \(X=[0,1]\cup\{2\}\). A closed subset of \(\Lambda\) does. Take a closed \(T_1\subseteq\Lambda\) and a continuous bijection \(\chi:T_1\to[0,1]\) (Theorem 3.4(2)), and let
\[
\begin{gathered}
T=\{(1,t_1,t_2,\dots):t\in T_1\}\\
\cup\{(2,1,1,1,\dots)\}.
\end{gathered}
\]
\(T\) is closed, \((2,1,1,\dots)\) is an isolated point of \(T\), and the map sending \((1,t_1,t_2,\dots)\) to \(\chi(t)\) and \((2,1,1,\dots)\) to \(2\) is a continuous bijection of \(T\) onto \(X\). Below the node \((2)\) the tree has a single branch, while below \((1)\) it has uncountably many. A product cannot express branching that depends on the node. This is why the partitions in the proof of Theorem 3.4 produce a closed subset of \(\Lambda\) and not a product: the number of nonempty pieces depends on the piece being divided, not only on the level.

#### The Lusin–Souslin theorem

**Theorem 3.6** (Lusin–Souslin). Let \(P\) be a Polish space, \(X\) a Hausdorff space and \(g:P\to X\) continuous and injective. Then \(g(B)\) is Borel in \(X\) for every Borel set \(B\subseteq P\). In particular \(g(P)\) is Borel, and \(g\) is a Borel isomorphism of \(P\) onto \(g(P)\).

**Proof.** *Reduction.* Let \(B\subseteq P\) be Borel. Lemma 3.1 gives a zero-dimensional Polish topology on \(P\), finer than the given one and with the same Borel sets, in which \(B\) is open and closed. With the finer relative topology, \(B\) is a zero-dimensional Polish space, and \(g\) restricted to \(B\) is still continuous and injective. So it suffices to prove that \(g(P)\) is Borel when \(P\) is zero-dimensional. By Theorem 3.4(1), we may then assume that \(P=T\) is a closed subset of \(\Lambda\).

*Separation along the tree.* For \(s\in\mathbb N^{<\mathbb N}\) put \(Y_s=g(T_s)\). Each \(T_s\) is closed in \(\Lambda\), hence Polish, so each \(Y_s\) is a Polish image in \(X\). Because \(g\) is injective, \(Y_s\) is the disjoint union of the sets \(Y_{sn}\). We choose Borel sets \(B_s\supseteq Y_s\) by induction on \(|s|\). Put \(B_\varnothing=X\). Given \(B_s\), the separation theorem ([Theorem 2.4](#oa-fnd-pb-03)) gives pairwise disjoint Borel sets \(E_{sn}\supseteq Y_{sn}\). Put
\[
B_{sn}=E_{sn}\cap B_s\cap\overline{Y_{sn}}.
\tag{3}
\]
Then \(Y_{sn}\subseteq B_{sn}\subseteq B_s\), the sets \(B_{sn}\) (\(n\in\mathbb N\)) are pairwise disjoint, and \(B_{sn}\subseteq\overline{Y_{sn}}\). By induction on \(k\), the sets \(B_s\) with \(|s|=k\) are pairwise disjoint: two different sequences of length \(k\) either have the same parent, or have disjoint ancestors.

*The Borel set.* Let \(B^*=\bigcap_k\bigcup_{|s|=k}B_s\), a Borel set. If \(t\in T\), then \(g(t)\in Y_{t|k}\subseteq B_{t|k}\) for every \(k\), so \(g(T)\subseteq B^*\). Conversely, let \(x\in B^*\). For each \(k\), exactly one \(s^{(k)}\) of length \(k\) has \(x\in B_{s^{(k)}}\), because these sets are pairwise disjoint. By (3), \(B_{s^{(k+1)}}\) lies inside the set indexed by the first \(k\) terms of \(s^{(k+1)}\), so uniqueness shows that \(s^{(k+1)}\) extends \(s^{(k)}\). So there is \(t\in\Lambda\) with \(x\in B_{t|k}\subseteq\overline{Y_{t|k}}\) for every \(k\). Each \(Y_{t|k}\) is then nonempty, so each \(T_{t|k}\) is nonempty, and \(t\in T\) because \(T\) is closed. Put \(y=g(t)\). If \(x\neq y\), choose disjoint open sets \(U\ni y\) and \(W\ni x\). By continuity \(T_{t|k}\subseteq g^{-1}(U)\) for large \(k\), so \(Y_{t|k}\subseteq U\) and \(\overline{Y_{t|k}}\subseteq\overline U\), which misses \(W\). This contradicts \(x\in\overline{Y_{t|k}}\cap W\). Hence \(x=g(t)\in g(T)\), and \(B^*=g(T)\).

Finally, \(g\) is Borel because it is continuous, and it carries Borel sets of \(P\) to Borel sets of \(X\), which are Borel in \(g(P)\). \(\square\)

**Corollary 3.7.**

1. Every Borel set in a Lusin space is itself a Lusin set.
2. A Lusin set in a Hausdorff space, in particular in a metrizable space, is Borel.
3. If \(L\) is a Lusin space and \(h:L\to X\) is a continuous injection into a Hausdorff space, then \(h(L)\) is Borel and \(h\) is a Borel isomorphism of \(L\) onto \(h(L)\).
4. A Lusin space, with its Borel sets, is a standard Borel space.

**Proof.** Let \(f:P\to L\) be a continuous bijection from a Polish space. (1) For Borel \(B\subseteq L\), the set \(f^{-1}(B)\) is Borel in \(P\). Refine the topology of \(P\) by Lemma 3.1, so that it becomes zero-dimensional and \(f^{-1}(B)\) becomes open and closed. Then \(f^{-1}(B)\) is a zero-dimensional Polish space that \(f\) maps continuously and bijectively onto \(B\), and \(B\) is metrizable. (2) Apply Theorem 3.6 to \(f\) followed by the inclusion. (3) Apply Theorem 3.6 to \(h\circ f\): for Borel \(B\subseteq L\), \(h(B)=(h\circ f)(f^{-1}(B))\). (4) By Theorem 3.6, \(f\) is a Borel isomorphism of \(P\) onto \(L\). \(\square\)

*Another proof of (1).* The Lusin sets of \(L\) whose complements are Lusin sets form a \(\sigma\)-algebra that contains the open sets; so this \(\sigma\)-algebra contains every Borel set. Complements are built into the definition. Finite intersections are Lusin sets by Proposition 3.3(3). A countable union \(\bigcup_nA_n\) is the disjoint union of the Lusin sets \(A_n\cap(L\setminus A_1)\cap\cdots\cap(L\setminus A_{n-1})\), hence a Lusin set by Proposition 3.3(4), and its complement \(\bigcap_n(L\setminus A_n)\) is a Lusin set by Proposition 3.3(3). Open sets are Lusin sets, and so are their complements, which are closed, by Proposition 3.3(5).

**Example 3.8** (Lusin sets in a space that is not Hausdorff). Let \(A\subseteq[0,1]\) be a set that is not Borel. It exists by the counting argument ([Corollary 2.8](#oa-fnd-pb-12)), because \([0,1]\) is Borel isomorphic to \(\mathcal C\) ([Theorem 5.2](#oa-fnd-pb-07)). Glue two copies of \([0,1]\) along \(A\): let \(X\) be the quotient of \([0,1]\times\{1,2\}\) by the relation \((a,1)\sim(a,2)\) for \(a\in A\), with quotient map \(q\) and the quotient topology. Put \(L_i=q([0,1]\times\{i\})\).

- For each \(i\), the map \(t\mapsto q(t,i)\) is a homeomorphism of \([0,1]\) onto \(L_i\) with its relative topology. It is continuous and injective. For \(V\subseteq[0,1]\) open, the preimage of \(q(V\times\{1,2\})\) is \(V\times\{1,2\}\), so \(q(V\times\{1,2\})\) is open in \(X\). Its intersection with \(L_1\) is \(q(V\times\{1\})\), because \(q(t,2)\) lies in \(L_1\) only when \(t\in A\), and then \(q(t,2)=q(t,1)\). So the map is open onto \(L_1\), and likewise onto \(L_2\).
- Hence \(L_1\) and \(L_2\) are Lusin sets (Proposition 3.3(2)).
- \(L_1\cap L_2=q(A\times\{1\})\) is homeomorphic to \(A\subseteq[0,1]\). If \(A\) were a Lusin space, it would be Borel in \([0,1]\) by Corollary 3.7(2). So \(L_1\cap L_2\) is not a Lusin set.
- \(X\) is not Hausdorff. \(A\) is not closed, so some \(a\notin A\) is a limit of points \(a_n\in A\). Then \(q(a,1)\neq q(a,2)\), but every neighbourhood of either point contains \(q(a_n,1)=q(a_n,2)\) for large \(n\).

So the intersection rule of Proposition 3.3(3) fails here. In its proof, the fibre product \(P\) is closed only because the diagonal of a Hausdorff space is closed.

### 4. Borel maps between Souslin spaces

A map is determined by its graph. When the target is countably separated, the graph of a Borel map is a Borel set. This turns questions about Borel maps into questions about Souslin sets, and gives the Borel form of the Lusin–Souslin theorem.

**Proposition 4.1** (Graphs of Borel maps). Let \((X,\Sigma)\) be a measurable space and \((Y,\mathcal B_Y)\) a Borel space whose points are separated by a sequence \((S_n)\) of Borel sets. For every measurable \(f:X\to Y\), with graph \(\operatorname{Gr}f=\{(x,f(x)):x\in X\}\),
\[
\begin{gathered}
(X\times Y)\setminus\operatorname{Gr}f\\
=\bigcup_n\Big(\big(f^{-1}(S_n)\times(Y\setminus S_n)\big)\\
\cup\big(f^{-1}(Y\setminus S_n)\times S_n\big)\Big),
\end{gathered}
\tag{4}
\]
so \(\operatorname{Gr}f\) belongs to \(\Sigma\otimes\mathcal B_Y\). Consequently:

1. If \(X\) and \(Y\) are topological spaces, \(f\) is Borel, and countably many Borel sets separate the points of \(Y\) (for example, \(Y\) separable metrizable), then \(\operatorname{Gr}f\) is a Borel subset of \(X\times Y\).
2. If \(Y\) is countably separated, the points fixed by a Borel map \(h:Y\to Y\) form a Borel set.
3. Conversely, if the diagonal \(\Delta_Y=\{(y,y):y\in Y\}\) lies in \(\mathcal B_Y\otimes\mathcal B_Y\), then \(Y\) is countably separated.

**Proof.** (4) holds because \(f(x)\neq y\) exactly when some \(S_n\) contains one of the two points and not the other.

(1) The projections of \(X\times Y\) are continuous, so a product of Borel sets is Borel in \(X\times Y\), and \(\mathcal B(X)\otimes\mathcal B(Y)\subseteq\mathcal B(X\times Y)\).

(2) The map \(y\mapsto(y,h(y))\) is measurable into \((Y\times Y,\mathcal B_Y\otimes\mathcal B_Y)\), because its two coordinates are measurable and the coordinate maps generate the product \(\sigma\)-algebra (F1). The fixed points form the preimage of \(\Delta_Y\). This diagonal is the graph of the identity, so it lies in \(\mathcal B_Y\otimes\mathcal B_Y\) by (4).

(3) For any family \(\mathcal G\) of sets, the sets that lie in the \(\sigma\)-algebra generated by some countable subfamily of \(\mathcal G\) form a \(\sigma\)-algebra containing \(\mathcal G\). Hence \(\Delta_Y\) lies in the \(\sigma\)-algebra generated by countably many products \(A_n\times B_n\) of Borel sets. Let \(x\neq y\). If no \(A_n\) contains exactly one of \(x,y\), then the points \((x,x)\) and \((y,x)\) lie in the same products \(A_n\times B_n\). The sets that contain both points or neither form a \(\sigma\)-algebra, so this \(\sigma\)-algebra contains \(\Delta_Y\). But \(\Delta_Y\) contains \((x,x)\) and not \((y,x)\). So the countable family \((A_n)\) separates points. \(\square\)

**Remark 4.2.** For separable metrizable \(X\) and \(Y\) one can also argue with open sets. Every open subset of \(X\times Y\) is then a countable union of open boxes, so \(\mathcal B(X\times Y)=\mathcal B(X)\otimes\mathcal B(Y)\) (F1), and the measurability of a map into \(X\times Y\) can be tested on preimages of open boxes. For instance, if \(\varphi\) is a Borel map of a separable metric space \(Z\) into itself, then \(z\mapsto(z,\varphi(z))\) is Borel into \(Z\times Z\), and the fixed points of \(\varphi\) form the Borel set \(\{z:d(z,\varphi(z))=0\}\). For nonseparable metrizable spaces the open boxes of a product can generate a strictly smaller \(\sigma\)-algebra than the open sets (Exercise 4), and then this argument does not apply. We do not treat that case. All our applications concern separable spaces, where part (1) applies, and part (1) needs no condition on \(X\) at all.

**Theorem 4.3** (Images and preimages under Borel maps). Let \(X\) be a Souslin space, \(Y\) a separable metrizable space and \(f:X\to Y\) a Borel map.

1. \(f(A)\) is a Souslin set in \(Y\) for every Souslin set \(A\subseteq X\), in particular for every Borel set.
2. \(f^{-1}(A')\) is a Souslin set in \(X\) for every Souslin set \(A'\subseteq Y\).
3. If \(f\) is injective, it is a Borel isomorphism of \(X\) onto \(f(X)\).
4. If \(X\) is a Lusin space and \(f\) is injective, then \(f(B)\) is Borel in \(Y\) for every Borel \(B\subseteq X\).
5. Let \(X'\) be a standard Borel space and \(f':X'\to Y\) an injective Borel map. Then \(f'(X')\) is Borel in \(Y\), and \(f'\) is a Borel isomorphism of \(X'\) onto \(f'(X')\). In particular, a Borel bijection between standard Borel spaces is a Borel isomorphism.

**Proof.** Let \(\overline Y\) be a Polish space that contains \(Y\) as a subspace, for instance the completion of \(Y\) for a compatible metric. (One can also embed \(Y\) into the cube \([0,1]^{\mathbb N}\) by \(y\mapsto(\min(1,d(a_n,y)))_n\), with \((a_n)\) a dense sequence. This is the embedding used in [the lesson on the Effros Borel structure](the-effros-borel-structure.md#oa-fnd-ef-02) for Polish spaces, and that part of the argument does not use completeness.) The map \(f\) is Borel as a map into \(\overline Y\), because the Borel sets of \(Y\) are the traces of those of \(\overline Y\). Since \(\overline Y\) is separable and metrizable, \(\operatorname{Gr}f\) is Borel in \(X\times\overline Y\) by Proposition 4.1(1).

(1) \(X\times\overline Y\) is a Souslin space, because countable products of Souslin spaces are Souslin spaces ([Proposition 2.2](#oa-fnd-pb-02)(3)). So its Borel subset \(\operatorname{Gr}f\) is a Souslin set ([Corollary 2.6](#oa-fnd-pb-12)). The set \(A\times\overline Y\) is a Souslin set by Proposition 2.2(3), and so is its intersection with \(\operatorname{Gr}f\), by Proposition 2.2(4). The projection of this intersection to \(\overline Y\) is \(f(A)\), which is therefore a Souslin set by Proposition 2.2(2). It is the same space whether we view it in \(\overline Y\) or in \(Y\).

(2) \(f^{-1}(A')\) is the projection to \(X\) of \(\operatorname{Gr}f\cap(X\times A')\), which is a Souslin set as in (1). So it is a Souslin set by Proposition 2.2(2).

(3) Let \(B\subseteq X\) be Borel. By (1), \(f(B)\) and \(f(X\setminus B)\) are Souslin sets. They are disjoint because \(f\) is injective, and their union is \(f(X)\). By the separation theorem ([Theorem 2.4](#oa-fnd-pb-03)), some Borel set \(E\subseteq Y\) contains \(f(B)\) and misses \(f(X\setminus B)\). So \(f(B)=f(X)\cap E\) is Borel in \(f(X)\), and \(f^{-1}:f(X)\to X\) is Borel.

(4) \(\overline Y\) is a Lusin space, being Polish, and so is \(X\times\overline Y\), as a product of Lusin spaces ([Proposition 3.3](#oa-fnd-pb-04)(2) and (6)). By [Corollary 3.7](#oa-fnd-pb-05)(1), the Borel set \(\operatorname{Gr}f\cap(B\times\overline Y)\) is a Lusin set. The projection to \(\overline Y\) is continuous, and it is injective on the graph because \(f\) is injective. By Corollary 3.7(3), its image \(f(B)\) is Borel in \(\overline Y\), hence in \(Y\).

(5) Choose a Borel isomorphism \(j\) of a Polish space \(P\) onto \(X'\). \(P\) is a Lusin space and a Souslin space (Proposition 3.3(2)). Apply (4) and (3) to the injective Borel map \(f'\circ j\). For the last sentence, let \(f':X'\to Y'\) be a Borel bijection between standard Borel spaces, and \(k\) a Borel isomorphism of \(Y'\) onto a Polish space \(Q\). Then \(k\circ f'\) is a Borel isomorphism of \(X'\) onto \(Q\), and so \(f'=k^{-1}\circ(k\circ f')\) is a Borel isomorphism onto \(Y'\). \(\square\)

### 5. Standard Borel spaces

With the Lusin–Souslin theorem in hand, standard Borel spaces can be classified completely: they are determined by their cardinality. The same tools show that a countable separating family of Borel sets already generates the whole Borel structure of a Souslin–Borel space.

#### The isomorphism theorem

**Lemma 5.1** (Borel Schröder–Bernstein). Let \(X\) and \(Y\) be Borel spaces, and let \(f:X\to Y\) and \(g:Y\to X\) be injective Borel maps that carry Borel sets to Borel sets. Then \(X\) and \(Y\) are isomorphic.

**Proof.** Put \(A_0=X\setminus g(Y)\), \(A_{n+1}=g(f(A_n))\) and \(A=\bigcup_nA_n\). These sets are Borel, because \(f\) and \(g\) carry Borel sets to Borel sets. Define \(h(x)=f(x)\) for \(x\in A\) and \(h(x)=g^{-1}(x)\) for \(x\notin A\); this makes sense because \(X\setminus A\subseteq X\setminus A_0=g(Y)\).

The map \(h\) is injective on \(A\) and on \(X\setminus A\). If \(f(a)=g^{-1}(x)\) with \(a\in A_n\) and \(x\notin A\), then \(x=g(f(a))\in A_{n+1}\), which is impossible; so \(h\) is injective. Let \(y\in Y\). If \(g(y)\notin A\), then \(h(g(y))=y\). If \(g(y)\in A_n\), then \(n\geq1\), because \(A_0\) misses \(g(Y)\); so \(g(y)=g(f(a))\) for some \(a\in A_{n-1}\), and \(y=f(a)=h(a)\). So \(h\) is a bijection. For Borel \(E\subseteq Y\), \(h^{-1}(E)=(A\cap f^{-1}(E))\cup((X\setminus A)\cap g(E))\) is Borel. For Borel \(B\subseteq X\), \(h(B)=f(A\cap B)\cup g^{-1}(B\setminus A)\) is Borel. \(\square\)

**Theorem 5.2** (Isomorphism theorem). Consider a standard Borel space \(X\).

1. When \(X\) is countable, every subset of \(X\) is Borel.
2. If \(X\) is uncountable, \(X\) is isomorphic to \(\mathcal C\), and therefore to \([0,1]\), to \(\mathbb R\), to \(\Lambda\), and to every other uncountable standard Borel space.
3. Two standard Borel spaces are isomorphic if and only if they have the same cardinality. The possible cardinalities are the finite ones, \(\aleph_0\) and \(2^{\aleph_0}\).

**Proof.** We may assume that \(X\) is a Polish space with its Borel sets.

(1) Points are closed, and every subset is a countable union of points.

(2) Let \((U_n)\) be a countable base and \(F(x)=(1_{U_n}(x))_n\in\mathcal C\). The map \(F\) is Borel, since its coordinates are Borel and the coordinates generate the Borel sets of \(\mathcal C\) (F1). It is injective, since the base separates points. By [Theorem 4.3](#oa-fnd-pb-06)(5), \(F\) is a Borel isomorphism of \(X\) onto the Borel set \(F(X)\); in particular it carries Borel sets to Borel sets. The perfect set lemma ([Lemma 1.3](#oa-fnd-pb-01)) gives a homeomorphism \(e\) of \(\mathcal C\) onto a compact set \(e(\mathcal C)\subseteq X\). Since \(e\) is a homeomorphism onto \(e(\mathcal C)\), it carries Borel sets of \(\mathcal C\) to Borel subsets of \(e(\mathcal C)\); these are Borel in \(X\), because the compact set \(e(\mathcal C)\) is closed. And \(e\) is continuous. The Borel Schröder–Bernstein lemma gives \(X\cong\mathcal C\). The spaces \([0,1]\), \(\mathbb R\) and \(\Lambda\) are uncountable and Polish.

(3) Any bijection between countable standard Borel spaces is an isomorphism by (1); uncountable ones are all isomorphic to \(\mathcal C\) by (2); and \(|\mathcal C|=2^{\aleph_0}\). \(\square\)

#### Souslin–Borel spaces and countable separating families

**Definition 5.3.** A *Souslin–Borel space* is a countably separated Borel space that is the image of some standard Borel space under a Borel map.

**Definition 5.4.** In a standard Borel space \(X\), call \(A\subseteq X\) a *Souslin set* if \(A=\varnothing\) or \(A=f(Z)\) for some standard Borel space \(Z\) and some Borel map \(f:Z\to X\).

**Lemma 5.5.**

1. For a Polish space \(X\) and a set \(A\subseteq X\), \(A\) is a Souslin set in the topological sense of Definition 2.1 exactly when it is one in the sense of Definition 5.4. So being a Souslin set of a standard Borel space does not depend on the Polish topology used to describe its Borel sets.
2. With its relative Borel structure, a Souslin set \(A\) of a standard Borel space is a Souslin–Borel space.
3. For a Souslin–Borel space \(X\) and a sequence \((B_n)\) of Borel sets that separates points, the formula \(\varphi(x)=(1_{B_n}(x))_n\) defines an injective Borel map \(\varphi:X\to\mathcal C\) whose image \(\varphi(X)\) is a Souslin set in \(\mathcal C\).

**Proof.** (1) A topological Souslin set is \(g(P)\) with \(g\) continuous, hence Borel, and \(P\) Polish, hence standard. Conversely, if \(f:Z\to X\) is Borel and \(j\) is a Borel isomorphism of a Polish space \(P\) onto \(Z\), then \(f(Z)=(f\circ j)(P)\) is a Souslin set by [Theorem 4.3](#oa-fnd-pb-06)(1). The second sentence follows, because Definition 5.4 mentions no topology.

(2) The traces on \(A\) of a countable separating family of \(X\) separate the points of \(A\). If \(A=f(Z)\), then \(f\) is Borel as a map into \(A\) with its relative structure.

(3) \(\varphi\) is injective because \((B_n)\) separates points. It is Borel because its coordinates \(1_{B_n}\) are Borel and the coordinates generate \(\mathcal B(\mathcal C)\) (F1). If \(X=f(Z)\) with \(Z\) standard and \(f\) Borel, then \(\varphi(X)=(\varphi\circ f)(Z)\) is a Souslin set by (1). \(\square\)

**Theorem 5.6** (Blackwell). Let \(X\) be a Souslin–Borel space, \((B_n)\) a countable family of Borel sets, and \(\mathcal B_0\) the \(\sigma\)-algebra they generate. A Borel set \(B\subseteq X\) belongs to \(\mathcal B_0\) exactly when it is a union of atoms of \(\mathcal B_0\), that is: whenever \(x\in B\) and \(y\notin B\), some \(B_n\) contains exactly one of \(x\) and \(y\). In particular:

1. every sequence of Borel sets that separates points generates the Borel structure of \(X\);
2. the map \(\varphi\) of Lemma 5.5(3) is a Borel isomorphism of \(X\) onto the Souslin set \(\varphi(X)\subseteq\mathcal C\).

Example 5.7 proves that the countability hypothesis in (1) is essential.

**Proof.** If no \(B_n\) separates \(x\) and \(y\), then no set of \(\mathcal B_0\) does, because the sets that contain both points or neither form a \(\sigma\)-algebra containing every \(B_n\). This proves "only if".

Conversely, let \(B\) be Borel and a union of atoms, and let \(\varphi=(1_{B_n})_n:X\to\mathcal C\), a Borel map (F1). The hypothesis says exactly that \(\varphi(B)\cap\varphi(X\setminus B)=\varnothing\). Both sets are Souslin sets in \(\mathcal C\). Indeed, write \(X=f(Z)\) with \(Z\) standard and \(f\) Borel. Then \(f^{-1}(B)\) is a Borel subset of \(Z\), hence standard (F4), and \(\varphi\circ f\) maps it onto \(\varphi(B)\) because \(f\) is onto; so Lemma 5.5(1) applies, and likewise to \(X\setminus B\). By the separation theorem ([Theorem 2.4](#oa-fnd-pb-03)), there is a Borel set \(D\subseteq\mathcal C\) with \(\varphi(B)\subseteq D\) and \(D\cap\varphi(X\setminus B)=\varnothing\). Then \(B=\varphi^{-1}(D)\), and \(\varphi^{-1}(D)\in\mathcal B_0\) because \(\varphi\) is \(\mathcal B_0\)-measurable (F1).

(1) If \((B_n)\) separates points, the atoms are single points, and every Borel set is a union of atoms.

(2) \(\varphi\) is injective and Borel. The sets \(E\subseteq X\) for which \(\varphi(E)\) is Borel in \(\varphi(X)\) include each \(B_n\), since \(\varphi(B_n)=\varphi(X)\cap\{c:c_n=1\}\). They are closed under complements and countable unions, since \(\varphi\) is injective. So they include \(\mathcal B_0\), which is the whole Borel structure by (1). \(\square\)

*Another proof of (1).* Let \((B_n)\) separate points, let \(B\) be Borel, and compare \(\varphi\) with \(\psi=(1_B,1_{B_1},1_{B_2},\dots)\). By Lemma 5.5(3), \(\psi(X)\) is a Souslin set in \(\mathcal C\). The map \(\varphi\circ\psi^{-1}\), which drops the first coordinate, is a one-to-one continuous map of \(\psi(X)\) onto \(\varphi(X)\). By [Theorem 4.3](#oa-fnd-pb-06)(3) it is a Borel isomorphism. So \(1_B\) is a Borel function of \(\varphi\): the set \(\varphi(B)\) is Borel in \(\varphi(X)\), say \(\varphi(B)=\varphi(X)\cap D\) with \(D\) Borel in \(\mathcal C\), and \(B=\varphi^{-1}(D)\) lies in the \(\sigma\)-algebra generated by the \(B_n\) (F1).

**Example 5.7** (Countability is needed in (1)). The singletons of \([0,1]\) are Borel sets, and they separate points. The countable sets and their complements form a \(\sigma\)-algebra that contains every singleton, and each of its members lies in the \(\sigma\)-algebra generated by the singletons; so it is the \(\sigma\)-algebra they generate. It does not contain \([0,\tfrac12]\), which is uncountable and has an uncountable complement.

**Corollary 5.8.**

1. Let \((X,\mathcal B)\) be a Souslin–Borel space and \(\mathcal B'\subseteq\mathcal B\) a \(\sigma\)-algebra that is countably generated and separates points. Then \(\mathcal B'=\mathcal B\).
2. Let \(f\) be a Borel bijection of a Souslin–Borel space onto a Borel space whose points are separated by countably many Borel sets. Then \(f\) is a Borel isomorphism.

**Proof.** (1) Let \(\mathcal B'\) be generated by \((G_n)\). Since \(\mathcal B'\) separates points, so does \((G_n)\), because the sets that do not separate two given points form a \(\sigma\)-algebra. Apply Theorem 5.6(1).

(2) Let \(f:X\to Y\) be the bijection and \((S_n)\) a sequence of Borel sets separating the points of \(Y\). As \(f\) is bijective, the sets \(f^{-1}(S_n)\) separate the points of \(X\), so they generate its Borel structure by Theorem 5.6(1). The \(\sigma\)-algebra they generate is \(\{f^{-1}(E):E\in\sigma(S_n:n)\}\). So each Borel \(B\subseteq X\) equals \(f^{-1}(E)\) for a Borel \(E\subseteq Y\), and \(f(B)=E\) because \(f\) is bijective. \(\square\)

**Example 5.9** (A Souslin–Borel space that is not standard). The Souslin set \(D\subseteq\mathcal C\) of [Example 2.9](#oa-fnd-pb-12), with its relative Borel structure, is a Souslin–Borel space, by Lemma 5.5(1) and (2). It is not standard. If it were, the inclusion \(D\to\mathcal C\) would be an injective Borel map on a standard Borel space, and \(D\) would be Borel by Theorem 4.3(5).

## B. Integrate over the encoded space

An image need not be Borel to be measurable for the completed measures under consideration. Keep the distinction between universal measurability and Borel measurability visible while reading the measure proofs. The sigma-finite standard-model theorem supplies the measure structure used in later operator-algebra decompositions.

### 6. Measures on Souslin sets

A Souslin set need not be Borel, but it is always measurable. For every \(\sigma\)-finite measure it is squeezed between two Borel sets of equal measure, and for every measure it is measurable in Carathéodory's sense. As a consequence, every \(\sigma\)-finite measure on a Souslin–Borel space lives on a standard Borel set.

Let \((X,\mathcal B)\) be a Borel space and \(\mu\) a measure on it, that is, a countably additive map \(\mathcal B\to[0,\infty]\). Put
\[
\begin{gathered}
\mu^*(E)\\
=\inf\{\mu(B):\\
B\in\mathcal B,\ E\subseteq B\},\\
E\subseteq X.
\end{gathered}
\tag{5}
\]
A set \(E\) is *\(\mu\)-measurable* if there are Borel sets \(B_1\subseteq E\subseteq B_2\) with \(\mu(B_2\setminus B_1)=0\). These sets form a \(\sigma\)-algebra, the completion of \(\mathcal B\) for \(\mu\): complements and countable unions of such sandwiches are again sandwiches, and the differences stay null. A set \(E\) is *\(\mu^*\)-measurable*, in Carathéodory's sense, if \(\mu^*(W)=\mu^*(W\cap E)+\mu^*(W\setminus E)\) for every \(W\subseteq X\). The \(\mu^*\)-measurable sets form a \(\sigma\)-algebra by Carathéodory's theorem, because \(\mu^*\) is an outer measure: it is monotone, \(\mu^*(\varnothing)=0\), and it is countably subadditive by Lemma 6.1(1).

**Lemma 6.1** (Outer measure).

1. The function \(\mu^*\) of (5) is countably subadditive, and every \(E\) has a Borel \(H\supseteq E\) with \(\mu(H)=\mu^*(E)\).
2. If \(E_1\subseteq E_2\subseteq\cdots\), then \(\mu^*(\bigcup_kE_k)=\lim_k\mu^*(E_k)\).
3. Borel sets are \(\mu^*\)-measurable.
4. If \(\mu\) is \(\sigma\)-finite, some finite measure \(\nu\) has the same null sets, and a set is \(\mu\)-measurable exactly when it is \(\nu\)-measurable.

**Proof.** (1) If \(\mu^*(E)=\infty\), take \(H=X\). Otherwise choose Borel \(H_j\supseteq E\) with \(\mu(H_j)<\mu^*(E)+1/j\) and let \(H=\bigcap_jH_j\). For subadditivity, the union of such sets for the \(E_k\) covers \(\bigcup_kE_k\).

(2) Choose \(H_k\) as in (1) for \(E_k\) and put \(H'_k=\bigcap_{j\geq k}H_j\). Then \(E_k\subseteq H'_k\subseteq H_k\), so \(\mu(H'_k)=\mu^*(E_k)\), and the \(H'_k\) increase. Hence \[
\begin{gathered}
\mu^*(\bigcup_kE_k)\\
\leq\mu(\bigcup_kH'_k)\\
=\lim_k\mu^*(E_k)\\
\leq\mu^*(\bigcup_kE_k).
\end{gathered}
\]

(3) Let \(K\) be Borel and \(W\subseteq X\) with \(\mu^*(W)<\infty\); otherwise there is nothing to prove. With \(H\) as in (1) for \(W\), \[
\begin{gathered}
\mu^*(W\cap K)+\mu^*(W\setminus K)\\
\leq\mu(H\cap K)+\mu(H\setminus K)\\
=\mu^*(W).
\end{gathered}
\] The reverse inequality is subadditivity.

(4) Write \(X\) as a disjoint union of Borel sets \(X_n\) with \(\mu(X_n)<\infty\), and put \(\nu(B)=\sum_n2^{-n}\mu(B\cap X_n)/(1+\mu(X_n))\). Then \(\nu(X)\leq1\), and \(\nu(B)=0\) exactly when \(\mu(B\cap X_n)=0\) for every \(n\), that is, when \(\mu(B)=0\). The completion depends only on the null sets. \(\square\)

**Theorem 6.2** (Souslin sets are measurable). Let \(X\) be a Hausdorff space, \(\mu\) a measure on \(\mathcal B(X)\), and \(A\) a Polish image in \(X\), for instance a Souslin set of a metrizable \(X\).

1. If \(\mu\) is finite, then \(\mu^*(A)=\sup\{\mu(K):K\subseteq A\text{ compact}\}\), and \(A\) is \(\mu\)-measurable.
2. If \(\mu\) is \(\sigma\)-finite, \(A\) is \(\mu\)-measurable.
3. For every measure \(\mu\), \(A\) is \(\mu^*\)-measurable.

In particular, in a standard Borel space every Souslin set is \(\mu\)-measurable for every \(\sigma\)-finite \(\mu\). By [Lemma 5.5](#oa-fnd-pb-08)(1), it does not matter which Polish topology is used to describe the Borel sets.



**Proof.** We may assume \(A\neq\varnothing\), so \(A=g(\Lambda)\) with \(g:\Lambda\to X\) continuous, as noted after [Definition 2.1](#oa-fnd-pb-02). For a finite sequence \(s=(n_1,\dots,n_k)\) let
\[
L_s=\{t\in\Lambda: \ t_i\leq n_i\text{ for }i\leq k\},
\tag{6}
\]
a closed set. \(L_\varnothing=\Lambda\), and \(L_{sm}\) increases with \(m\) and has union \(L_s\).

(1) Fix \(\varepsilon>0\). The sets \(g(L_{sm})\) increase in \(m\) with union \(g(L_s)\). So by Lemma 6.1(2) we can choose \(n_1,n_2,\ldots\) one at a time with \(\mu^*(g(L_{(n_1,\dots,n_k)}))>\mu^*(A)-\varepsilon\) for every \(k\). Write \(L_k=L_{(n_1,\dots,n_k)}\), with \(L_s\) as in (6), and \(K=\bigcap_kL_k=\prod_i\{1,\dots,n_i\}\), a compact set by (B2). Then \(C=g(K)\) is a compact subset of \(A\).

*Claim: \(\bigcap_k\overline{g(L_k)}\subseteq C\).* Let \(y\notin C\). Because \(C\) is compact and \(X\) is Hausdorff, there are disjoint open sets \(U\ni y\) and \(W\supseteq C\); then \(\overline U\cap W=\varnothing\). Let \(F=g^{-1}(\overline U)\). It is a closed subset of \(\Lambda\), and it is disjoint from \(K\), because \(g(K)=C\subseteq W\).

Suppose \(F\cap L_k\neq\varnothing\) for every \(k\). Call a finite sequence \(s=(s_1,\dots,s_j)\) *good* if \(s_i\leq n_i\) for \(i\leq j\) and \(F\cap L_k\cap\Lambda_s\neq\varnothing\) for all \(k\geq j\). The empty sequence is good, by our assumption. Let \(s\) be good with \(|s|=j\). For each \(k\geq j+1\), every point of \(L_k\cap\Lambda_s\) has \((j+1)\)-st entry at most \(n_{j+1}\), so it lies in some \(\Lambda_{sm}\) with \(m\leq n_{j+1}\). Hence some such \(m\) has \(F\cap L_k\cap\Lambda_{sm}\neq\varnothing\). There are only finitely many such \(m\), so one \(m\) serves infinitely many \(k\), and then all \(k\geq j+1\), because the \(L_k\) decrease. So every good sequence has a good one-step extension, and we obtain \(t\in K\) with every \(t|j\) good. Each cylinder \(\Lambda_{t|j}\) meets \(F\). These cylinders form a neighbourhood base at \(t\), and \(F\) is closed, so \(t\in F\cap K\), which is impossible. Hence \(F\cap L_k=\varnothing\) for some \(k\). Then \(U\) is a neighbourhood of \(y\) that misses \(g(L_k)\), so \(y\notin\overline{g(L_k)}\). This proves the claim.

Since \(\mu\) is finite and the closed sets \(\overline{g(L_k)}\) decrease,
\[
\begin{gathered}
\mu(C)\\
\geq\mu\Big(\bigcap_k\overline{g(L_k)}\Big)\\
=\lim_k\mu\big(\overline{g(L_k)}\big)\\
\geq\lim_k\mu^*\big(g(L_k)\big)\\
\geq\mu^*(A)-\varepsilon .
\end{gathered}
\]
Here the first inequality is the claim, the equality is continuity from above of the finite measure \(\mu\), and the next inequality holds because \(\overline{g(L_k)}\) is a Borel set containing \(g(L_k)\). So the supremum equals \(\mu^*(A)\). Choose compact \(C_j\subseteq A\) with \(\mu(C_j)>\mu^*(A)-1/j\), let \(K'=\bigcup_jC_j\), a Borel set because compact subsets of a Hausdorff space are closed, and let \(H\supseteq A\) be Borel with \(\mu(H)=\mu^*(A)\) (Lemma 6.1(1)). Then \(K'\subseteq A\subseteq H\) and \(\mu(H\setminus K')\leq\mu^*(A)-\mu(C_j)<1/j\) for every \(j\), so \(\mu(H\setminus K')=0\).

(2) Apply (1) to the finite measure \(\nu\) of Lemma 6.1(4), which has the same measurable sets as \(\mu\).

(3) Let \(W\subseteq X\) with \(\mu^*(W)<\infty\), and \(H\supseteq W\) Borel with \(\mu(H)=\mu^*(W)\). Part (1), for the finite measure \(\mu_H(B)=\mu(B\cap H)\), gives Borel sets \(K'\subseteq A\subseteq L'\) with \(\mu(H\cap(L'\setminus K'))=0\). Then \[
\begin{gathered}
\mu^*(W\cap A)\\
\leq\mu^*(W\cap K')+\mu(H\cap(L'\setminus K'))\\
=\mu^*(W\cap K'),
\end{gathered}
\] and \(W\setminus A\subseteq W\setminus K'\). By Lemma 6.1(3), \[
\begin{gathered}
\mu^*(W\cap A)+\mu^*(W\setminus A)\\
\leq\mu^*(W\cap K')+\mu^*(W\setminus K')\\
=\mu^*(W).
\end{gathered}
\] Subadditivity gives the reverse inequality. \(\square\)

**Corollary 6.3** (Standard measures). Let \(X\) be a Souslin–Borel space and \(\mu\) a \(\sigma\)-finite measure on it. Then \(\mu\) is standard: some Borel set \(N\subseteq X\) with \(\mu(N)=0\) has \(X\setminus N\) standard. One can take \(X\setminus N\) isomorphic to a \(\sigma\)-compact subset of \(\mathcal C\).

**Proof.** By [Theorem 5.6](#oa-fnd-pb-08)(2), we may assume that \(X\) is a Souslin set in \(\mathcal C\) with its relative Borel structure. Put \(\nu(E)=\mu(E\cap X)\) for Borel \(E\subseteq\mathcal C\). This is a \(\sigma\)-finite measure on \(\mathcal C\): if \(X=\bigcup_nX_n\) with \(\mu(X_n)<\infty\) and \(X_n=X\cap E_n\) with \(E_n\) Borel in \(\mathcal C\), then \(\nu(E_n)<\infty\) and \(\nu(\mathcal C\setminus\bigcup_nE_n)=0\). Apply Theorem 6.2(1) to a finite measure with the same null sets as \(\nu\) (Lemma 6.1(4)). It gives a \(\sigma\)-compact set \(X_0\subseteq X\) and a Borel set \(X_1\supseteq X\) with \(\nu(X_1\setminus X_0)=0\). Let \(N=X\setminus X_0=X\cap(\mathcal C\setminus X_0)\), a Borel subset of \(X\). Then \(\mu(N)=\nu(\mathcal C\setminus X_0)=\nu(X_1\setminus X_0)=0\), because \(\nu(\mathcal C\setminus X_1)=\mu(X\setminus X_1)=0\). Finally \(X\setminus N=X_0\) is a Borel subset of \(\mathcal C\), hence standard (F4). \(\square\)

**Example 6.4** (\(\sigma\)-finiteness is needed). Let \(D\subseteq\mathcal C\) be the Souslin set of [Example 2.9](#oa-fnd-pb-12). The counting measure on \(D\), which gives each subset its number of points, is a measure that is not standard: its only null set is \(\varnothing\), and \(D\) is not standard (Example 5.9). \(D\) is uncountable, since countable sets are Borel, so this measure is not \(\sigma\)-finite. Hence Corollary 6.3 needs \(\sigma\)-finiteness. On the other hand, every \(\sigma\)-finite Borel measure on \(\mathcal C\) still measures \(D\), by Theorem 6.2.

## C. Choose a representative with the right measurability

A section is a right inverse of a surjection. Its existence as a set map says nothing about its regularity. The proofs below construct representatives through shrinking choices and state exactly when the section is Borel and when it is measurable for all the specified measures. Closed equivalence classes and cosets are two separate applications of this mechanism.

### 7. Choosing points in a Borel way

Given an equivalence relation, or a map onto a set, we often need to choose one point from each class or fibre and to make the choice measurable. This section makes a Borel choice when the classes are closed and saturations of open sets are Borel. It applies this to coset spaces of Polish groups. For an arbitrary Borel surjection it makes a choice that is measurable for every \(\sigma\)-finite measure.

#### Borel transversals and coset spaces

**Theorem 7.1** (Borel transversals). Let \(X\) be a separable metrizable space with a compatible metric \(d\), and \(R\) an equivalence relation on \(X\) whose classes are complete for \(d\); for example, \(X\) Polish, \(d\) complete and every class closed. For \(E\subseteq X\) let \(R(E)\) be the set of points equivalent to a point of \(E\), and let \([x]\) be the class of \(x\). Assume that \(R(U)\) is Borel for every open \(U\subseteq X\). Then:

1. There is a Borel map \(\eta:X\to X\) with \(\eta(x)\in[x]\) for all \(x\), and \(\eta(x)=\eta(y)\) whenever \([x]=[y]\).
2. The set \(S=\{x:\eta(x)=x\}\) is Borel and meets every class exactly once.

If \(R(F)\) is Borel for every closed \(F\subseteq X\), then \(R(U)\) is Borel for every open \(U\), and the same conclusions hold.

Example 7.2 proves that replacing the open sets by their closures can lose a class. The closed-saturation hypothesis is therefore reduced to the open-saturation case before using the construction.

**Proof.** *A system of open sets.* Choose open sets \(X(s)\), for finite sequences \(s\) of length at least \(1\), with
\[
\begin{gathered}
X=\bigcup_nX(n),\\
X(s)=\bigcup_nX(sn),\\
\overline{X(sn)}\subseteq X(s),\\
\operatorname{diam}X(s)\leq2^{-|s|}.
\end{gathered}
\tag{7}
\]
This is possible. An open set \(V\) is a union of open balls \(\{y:d(x,y)<r_x\}\), \(x\in V\), with \(r_x\leq2^{-k-2}\) and the ball of radius \(2r_x\) inside \(V\). These balls have closures inside \(V\) and diameters at most \(2^{-k-1}\), and countably many of them cover \(V\), because \(V\) is second countable and hence Lindelöf (B4). Index them by \(\mathbb N\), adding empty sets if needed. By induction, for each \(k\) the sets \(X(s)\) with \(|s|=k\) cover \(X\).

*The lexicographic choice.* Order \(\mathbb N^k\) lexicographically: \(s\) comes before \(u\) if \(s_i<u_i\) at the first place where they differ. This is a well-ordering: in any nonempty subset choose the least first coordinate, then the least second coordinate among tuples with that first coordinate, and continue through the finitely many coordinates. For a class \(H\) and \(k\geq1\), let \(\kappa_k(H)\) be the first \(s\in\mathbb N^k\) with \(H\cap X(s)\neq\varnothing\).

(a) *\(\kappa_{k+1}(H)\) extends \(\kappa_k(H)\).* Write \(\kappa_{k+1}(H)=(u,m)\) with \(u\in\mathbb N^k\). \(H\) meets \(X(u,m)\subseteq X(u)\), so \(\kappa_k(H)\) is \(u\) or comes before \(u\). If some \(v\in\mathbb N^k\) before \(u\) had \(H\cap X(v)\neq\varnothing\), then \(H\) would meet some \(X(v,j)\), and \((v,j)\) comes before \((u,m)\), against the choice of \((u,m)\). So \(\kappa_k(H)=u\).

(b) For \(s\in\mathbb N^k\),
\[
\begin{gathered}
\{x:\kappa_k([x])=s\}\\
=R(X(s))\setminus\\
\bigcup\{R(X(v)):v\in\mathbb N^k\text{ comes before }s\},
\end{gathered}
\]
a Borel set, since \([x]\) meets \(X(v)\) exactly when \(x\in R(X(v))\), and the union is countable.

(c) The sets \(H\cap X(\kappa_k(H))\) are nonempty and decrease in \(k\), by (a). The closure in \(H\) of \(H\cap X(\kappa_{k+1}(H))\) lies in \(H\cap\overline{X(\kappa_{k+1}(H))}\subseteq H\cap X(\kappa_k(H))\). These closures are nonempty, closed in \(H\) and decreasing, with diameters at most \(2^{-k-1}\). As \((H,d)\) is complete, they have exactly one common point \(p(H)\), by Cantor's intersection theorem (B1), and \(p(H)\) is also the only point of \(\bigcap_k(H\cap X(\kappa_k(H)))\).

*The selector.* Put \(\eta(x)=p([x])\). Then \(\eta(x)\in[x]\), and \(\eta\) is constant on classes. For each finite \(u\) with \(X(u)\neq\varnothing\) fix a point \(c(u)\in X(u)\), and let \(\eta_k(x)=c(\kappa_k([x]))\). Each \(\eta_k\) is Borel, being constant on each of the countably many Borel sets of (b). Both \(\eta(x)\) and \(\eta_k(x)\) lie in \(X(\kappa_k([x]))\), so \(d(\eta(x),\eta_k(x))\leq2^{-k}\). A pointwise limit of Borel maps into a metric space is Borel: for closed \(F\), \[
\begin{gathered}
\eta^{-1}(F)\\
=\bigcap_j\bigcup_n\bigcap_{k\geq n}\eta_k^{-1}(\{y:d(y,F)<1/j\}).
\end{gathered}
\] So \(\eta\) is Borel.

(2) \(S\) consists of the points fixed by the Borel map \(\eta\). The separable metrizable space \(X\) is countably separated, so \(S\) is Borel by [Proposition 4.1](#oa-fnd-pb-06)(2). A point \(x\) lies in \(S\) exactly when it is the point \(p([x])\) of its class.

For the last sentence: an open set \(U\) is the union of the closed sets \(\{x:d(x,X\setminus U)\geq1/n\}\), and \(R\) commutes with unions. \(\square\)

*Remarks.* (a) The proof uses only the saturations of the countably many sets \(X(s)\). (b) The sets \(X(s)\) must be open. If one runs the construction with their closures instead, step (a) can fail: a class may meet \(\overline{X(u)}\) only in a boundary point that lies in no \(\overline{X(uj)}\), and then the choice at the next level moves to another branch. Example 7.2 gives a class that the resulting set misses entirely. This is why the version with closed sets is proved by showing that the saturations of open sets are then Borel, as in the last paragraph of the proof.

**Example 7.2** (Closures instead of open sets). Let \(X=[-1,1]\) with \(d(x,y)=|x-y|\), and let \(x\mathrel Ry\) mean \(|x|=|y|\). The classes \(\{x,-x\}\) are closed, and \(R(E)=E\cup(-E)\) is open for open \(E\) and closed for closed \(E\). So both forms of the hypothesis of Theorem 7.1 hold, and the theorem gives a Borel transversal, for instance \([0,1]\). Choose a system (7) with
\[
\begin{gathered}
X(1)=(0,\tfrac14),\\
X(2)=(-\tfrac38,-\tfrac18),\\
X(1,j)=(2^{-j-3},\tfrac14-2^{-j-3}),\\
X(2,j)=(-\tfrac38+2^{-j-3},-\tfrac18-2^{-j-3})\\
(j\geq1),
\end{gathered}
\]
and the remaining sets chosen in any way that satisfies (7). These sets do satisfy (7): the \(X(1,j)\) increase to \(X(1)\), the \(X(2,j)\) increase to \(X(2)\), their closures lie inside, and all their diameters are at most \(\tfrac14\). Now run the construction with closures. At level \(k\) it keeps, from each class, the points that lie in \(\overline{X(s)}\) for the first \(s\in\mathbb N^k\) whose closure meets the class. Take the class \(H=\{\tfrac14,-\tfrac14\}\).

- Level 1: \(\overline{X(1)}=[0,\tfrac14]\) meets \(H\), so the level-1 set keeps only the point \(\tfrac14\) of \(H\).
- Level 2: every \(\overline{X(1,j)}\) lies in \((0,\tfrac14)\) and misses \(H\), while \(\overline{X(2,1)}=[-\tfrac5{16},-\tfrac3{16}]\) contains \(-\tfrac14\). So the level-2 set keeps only the point \(-\tfrac14\) of \(H\).

The final set is the intersection of the sets of all levels, so it misses \(H\) entirely, and it is not a transversal. Writing \(S_k\) for the set kept at level \(k\), what fails is the inclusion of the closure of \(H\cap S_{k+1}\) in \(H\cap S_k\). With the open sets \(X(s)\), step (a) of the proof of Theorem 7.1 rules this out.

**Example 7.3** (Both hypotheses are needed).

(a) *Closed classes.* On \(X=\mathbb R\) let \(x\mathrel Ry\) mean \(x-y\in\mathbb Q\). The classes \(x+\mathbb Q\) are countable and dense, so not closed, and \(R(U)=U+\mathbb Q\) is open for open \(U\). No Lebesgue measurable set \(S\) meets every class exactly once. If one did, \(\mathbb R\) would be the disjoint union of the translates \(S+q\), \(q\in\mathbb Q\). If \(\lambda(S)=0\), then \(\lambda(\mathbb R)=0\). If \(\lambda(S)>0\), some \(S_0=S\cap[n,n+1]\) has \(\lambda(S_0)>0\), and the disjoint translates \(S_0+q\), \(q\in\mathbb Q\cap[0,1]\), all lie in \([n,n+2]\) and all have measure \(\lambda(S_0)\); infinitely many of them give infinite measure inside \([n,n+2]\). Both cases are absurd. In particular no Borel transversal exists.

(b) *Borel saturations.* Let \(A\subseteq\mathcal C\) be a set that is not Borel ([Corollary 2.8](#oa-fnd-pb-12)). On \(X=\mathcal C\times\{0,1\}\) let \((c,i)\mathrel R(c',i')\) mean that \(c=c'\) and either \(i=i'\) or \(c\in A\). The classes have one or two points, so they are closed. The saturation of the open set \(\mathcal C\times\{1\}\) is \((\mathcal C\times\{1\})\cup(A\times\{0\})\), which is not Borel, since its preimage under \(c\mapsto(c,0)\) is \(A\). Suppose \(S\) were a Borel transversal. For \(c\notin A\), both one-point classes \(\{(c,0)\}\) and \(\{(c,1)\}\) must meet \(S\); for \(c\in A\), exactly one of \((c,0),(c,1)\) lies in \(S\). So \(\{c:(c,0)\in S\text{ and }(c,1)\in S\}=\mathcal C\setminus A\), which would be Borel. This is a contradiction.

So countable classes do not suffice, and neither do finite classes with a saturation that is not Borel.

**Proposition 7.4** (Borel sections for coset spaces). Let \(G\) be a Polish group, that is, a topological group whose topology is Polish, and \(H\) a closed subgroup. Let \(q:G\to G/H\) be the map onto the space of left cosets, and give \(G/H\) the quotient topology and its Borel sets.

1. \(q\) is continuous and open, and \(G/H\) is Hausdorff.
2. There is a Borel set \(S\subseteq G\) that meets every left coset exactly once and contains \(1\).
3. The map \(\sigma:G/H\to G\) that sends each coset to its point in \(S\) is Borel, satisfies \(q\circ\sigma=\mathrm{id}\) and \(\sigma(H)=1\), and is a Borel isomorphism of \(G/H\) onto \(S\). In particular \(G/H\) is a standard Borel space.

The same holds for right cosets.

**Proof.** (1) \(q\) is continuous by definition. For open \(V\), \(q^{-1}(q(V))=VH\) is the union of the open sets \(Vh\), so \(q(V)\) is open. Let \(gH\neq g'H\). The set \(gHg'^{-1}\) is closed, because \(H\) is closed and translations are homeomorphisms. It does not contain \(1\), since \(1=gkg'^{-1}\) with \(k\in H\) would give \(g'H=gH\). By (B5), applied to the open neighbourhood \(G\setminus gHg'^{-1}\) of \(1\), there is an open neighbourhood \(V=V^{-1}\) of \(1\) with \(V^2\cap gHg'^{-1}=\varnothing\). If \(vgh=v'g'h'\) with \(v,v'\in V\) and \(h,h'\in H\), then \(v'^{-1}v=g'h'h^{-1}g^{-1}\in V^2\cap g'Hg^{-1}\). This set is empty, because \(g'Hg^{-1}=(gHg'^{-1})^{-1}\) and \(V^2\) is symmetric. So \(q(Vg)\) and \(q(Vg')\) are disjoint open neighbourhoods of \(gH\) and \(g'H\).

(2) Let \(x\mathrel Ry\) mean \(x^{-1}y\in H\). The classes are the cosets \(xH\), which are closed, and \(R(U)=UH\) is open for open \(U\). Theorem 7.1 gives a Borel transversal \(S_0\). Then \(S=(S_0\setminus H)\cup\{1\}\) is Borel and still a transversal, because \(H\) is the coset of \(1\).

(3) \(q\) restricted to \(S\) is a continuous bijection onto \(G/H\). \(S\) is a Borel subset of the Polish space \(G\), so by [Lemma 3.1](#oa-fnd-pb-04) it carries a Polish topology, finer than its relative topology, with the same Borel sets; \(q\) is still continuous and injective on it. By the Lusin–Souslin theorem ([Theorem 3.6](#oa-fnd-pb-05)), \(q\) carries Borel subsets of \(S\) to Borel subsets of the Hausdorff space \(G/H\). So \(\sigma=(q|_S)^{-1}\) is Borel. It carries Borel sets of \(G/H\) to Borel subsets of \(S\), because \(q\) is continuous. \(S\) is standard, being a Borel subset of a Polish space (F4), hence so is \(G/H\). For right cosets, compose with the homeomorphism \(g\mapsto g^{-1}\), which carries \(gH\) to \(Hg^{-1}\). \(\square\)

**Example 7.5** (Borel is the best one can ask). For \(G=\mathbb R\) and \(H=\mathbb Z\), \(S=[0,1)\) is a Borel transversal, and \(\sigma(x+\mathbb Z)\) is the fractional part of \(x\). No continuous section exists. Here \(G/H\) is a circle, and a continuous injective map \(\sigma\) from a circle into \(\mathbb R\) is impossible: it takes its largest and smallest values at two different points, each of the two arcs joining these points is mapped onto the whole interval between the two values, and so the values strictly between them are taken twice.

#### Measurable sections

**Lemma 7.6** (Lexicographic order on \(\Lambda\)). For \(t\neq u\) in \(\Lambda\) write \(t\prec u\) if \(t_i<u_i\) at the first index \(i\) with \(t_i\neq u_i\), and \(t\preceq u\) if \(t\prec u\) or \(t=u\).

1. \(\prec\) is a strict total order on \(\Lambda\).
2. For every \(u\in\Lambda\), the set \(\{t:t\prec u\}\) is open.
3. Every nonempty closed set \(F\subseteq\Lambda\) has a least element.
4. For \(s=(s_1,\dots,s_k)\) with \(k\geq1\), put \(a_s=(s_1,\dots,s_k,1,1,\dots)\) and \(b_s=(s_1,\dots,s_{k-1},s_k+1,1,1,\dots)\). Then
\[
\Lambda_s=\{t\in\Lambda: \ a_s\preceq t\prec b_s\}.
\tag{8}
\]

**Proof.** (1) Two different sequences have a first place of difference, so any two are comparable. If \(t\prec u\prec v\) with first differences at \(i\) (for \(t,u\)) and \(j\) (for \(u,v\)), then \(t\) and \(v\) agree before \(\min(i,j)\), and at \(\min(i,j)\) the entry of \(t\) is smaller; so \(t\prec v\).

(2) If \(t\prec u\) with first difference at \(i\), then every \(t'\in\Lambda_{t|i}\) satisfies \(t'\prec u\). So \(\{t:t\prec u\}\) is a union of cylinders.

(3) Let \(u_1\) be the least first entry of elements of \(F\), and, recursively, \(u_{k+1}\) the least \((k+1)\)-st entry among the elements of \(F\) that begin with \((u_1,\dots,u_k)\); such elements exist by the previous step. Every cylinder \(\Lambda_{u|k}\) meets \(F\) and \(F\) is closed, so \(u=(u_k)\in F\). If \(t\in F\), \(t\neq u\), first differs from \(u\) at \(i\), then \(t\) begins with \(u|i-1\), so \(t_i\geq u_i\) by the choice of \(u_i\), and \(t_i\neq u_i\); hence \(u\prec t\).

(4) If \(t\in\Lambda_s\), then \(t\) agrees with \(a_s\) up to place \(k\) and has entries at least \(1\) afterwards, so \(a_s\preceq t\); and \(t\) first differs from \(b_s\) at place \(k\), with \(t_k=s_k<s_k+1\), so \(t\prec b_s\). Conversely, let \(a_s\preceq t\prec b_s\), and suppose \(t|k\neq s\), with first difference at \(i\leq k\). Since \(a_s\preceq t\), \(t_i>s_i\). If \(i<k\), then \(t\) and \(b_s\) also first differ at \(i\), with \(t_i>s_i\), so \(b_s\prec t\). If \(i=k\), then \(t_k\geq s_k+1\): if \(t_k>s_k+1\), then \(b_s\prec t\); if \(t_k=s_k+1\), then \(t\) agrees with \(b_s\) up to \(k\) and every later entry of \(b_s\) is \(1\), at most the entry of \(t\), so \(b_s\preceq t\). Each case contradicts \(t\prec b_s\). \(\square\)

In (3) the entries must be minimized one after another, among the elements that begin with the entries already chosen. Minimizing each entry over all of \(F\) separately can leave \(F\): for the closed set \(F=\{(1,2,2,2,\dots),(2,1,1,1,\dots)\}\) it gives \((1,1,1,\dots)\notin F\).

**Theorem 7.7** (Measurable sections; Jankov–von Neumann). Let \(X\) be a Souslin space, \(Y\) a separable metrizable space and \(f:X\to Y\) a Borel map. Then \(f(X)\) is a Souslin set, and there is a map \(\varphi:f(X)\to X\) with \(f(\varphi(y))=y\) for every \(y\in f(X)\), such that for every Borel set \(B\subseteq X\) the set \(\varphi^{-1}(B)\) belongs to the \(\sigma\)-algebra generated by the Souslin subsets of \(f(X)\). Consequently \(\varphi^{-1}(B)\) is \(\mu^*\)-measurable for every measure \(\mu\) on \(\mathcal B(Y)\), and \(\mu\)-measurable for every \(\sigma\)-finite \(\mu\). One map \(\varphi\) serves all measures at once.

In particular, if \(X\) and \(Y\) are Souslin spaces, \(f\) maps \(X\) onto \(Y\), and \(\mu\) is a \(\sigma\)-finite measure on \(Y\), then there is a \(\mu\)-measurable map \(\varphi:Y\to X\) with \(f\circ\varphi=\mathrm{id}_Y\).

The two-point example after Lemma 7.6 proves that independent coordinate minima can leave a closed fibre; the proof below minimizes within the previously chosen prefix.

**Proof.** If \(X=\varnothing\) there is nothing to prove. Let \(\overline Y\) be a Polish space containing \(Y\), as in the proof of [Theorem 4.3](#oa-fnd-pb-06). As in the proof of part (1) there, \(\operatorname{Gr}f\) is a nonempty Souslin set in \(X\times\overline Y\). So there is a continuous map \(g\) of \(\Lambda\) onto \(\operatorname{Gr}f\), as noted after [Definition 2.1](#oa-fnd-pb-02). Let \(h=\pi_{\overline Y}\circ g\), with \(\pi_{\overline Y}\) the projection. Then \(h\) is continuous and \(h(\Lambda)=f(X)\), a Souslin set. For \(y\in f(X)\) the set \(h^{-1}(y)\) is nonempty and closed; let \(\psi(y)\) be its least element for \(\prec\) (Lemma 7.6(3)). Put \(\varphi=\pi_X\circ g\circ\psi\). The point \(g(\psi(y))\) lies on the graph and its second coordinate is \(h(\psi(y))=y\); so it equals \((\varphi(y),y)\), and \(f(\varphi(y))=y\).

Let \(\mathcal A\) be the \(\sigma\)-algebra on \(f(X)\) generated by its Souslin subsets. For \(u\in\Lambda\),
\[
\psi^{-1}(\{t:t\prec u\})=h(\{t:t\prec u\}),
\tag{9}
\]
because \(\psi(y)\prec u\) holds exactly when some \(t\in h^{-1}(y)\) has \(t\prec u\), \(\psi(y)\) being the least element of \(h^{-1}(y)\). The set \(\{t:t\prec u\}\) is open by Lemma 7.6(2), hence Polish (F3), so the right side of (9) is a Souslin set and lies in \(\mathcal A\). By (8), \[
\begin{gathered}
\psi^{-1}(\Lambda_s)\\
=\psi^{-1}(\{t:t\prec b_s\})\setminus\psi^{-1}(\{t:t\prec a_s\})
\end{gathered}
\] lies in \(\mathcal A\) for every \(s\). The sets \(E\subseteq\Lambda\) with \(\psi^{-1}(E)\in\mathcal A\) form a \(\sigma\)-algebra containing all cylinders. The cylinders form a countable base, which generates the Borel sets of \(\Lambda\) (F1), so this \(\sigma\)-algebra contains every Borel set of \(\Lambda\). For Borel \(B\subseteq X\), the set \((\pi_X\circ g)^{-1}(B)\) is Borel in \(\Lambda\), and \(\varphi^{-1}(B)=\psi^{-1}((\pi_X\circ g)^{-1}(B))\) lies in \(\mathcal A\).

Every Souslin subset of \(f(X)\) is a Souslin set in \(Y\). So it is \(\mu^*\)-measurable by [Theorem 6.2](#oa-fnd-pb-09)(3), and \(\mu\)-measurable for \(\sigma\)-finite \(\mu\) by Theorem 6.2(2). The \(\mu^*\)-measurable sets form a \(\sigma\)-algebra on \(Y\), and so do the \(\mu\)-measurable sets. The set \(f(X)\) is itself one of these Souslin subsets, so the \(\mu^*\)-measurable subsets of \(f(X)\) form a \(\sigma\)-algebra on \(f(X)\): the complement in \(f(X)\) of such a set \(E\) is \(f(X)\cap(Y\setminus E)\). The same holds for the \(\mu\)-measurable subsets, and both \(\sigma\)-algebras contain \(\mathcal A\). \(\square\)

**Remark 7.8** (Borel sections). We do not claim Borel sections in this generality. They exist in one case: if \(X\) is Polish, the fibres of \(f\) are closed, and \(f^{-1}(f(U))\) is Borel for every open \(U\subseteq X\), then Theorem 7.1 gives a Borel set \(S\subseteq X\) meeting each fibre exactly once, and \((f|_S)^{-1}\) is Borel on \(f(X)\) by Theorem 4.3(5).

## D. Recover topology on a group quotient

For a Polish group and a closed subgroup, the quotient must first be shown Polish in its quotient topology. The metric construction and the open-homomorphism theorem provide that topology; the Borel sections from the preceding route then apply to the resulting standard Borel space. A measurable representative does not replace either topological theorem.

### 8. Topological quotients and open homomorphisms

A Borel section answers a measurable question. For a closed subgroup we can say more: the quotient topology itself is Polish. A surjective continuous homomorphism between Polish groups also carries open sets to open sets. These two assertions have different proofs. Category gives the open mapping theorem; completeness of an open image gives the quotient theorem.

We use the Baire category theorem from Hahn–Banach, Baire and the basic theorems on Banach spaces. A set is *nowhere dense* if its closure has empty interior, and *meagre* if it is a countable union of nowhere dense sets. It is *comeagre in an open set* if its complement there is meagre. A set has the *Baire property* if its symmetric difference with an open set is meagre. Translations, inversion and other homeomorphisms preserve these notions.

 Invariant metrization is the Birkhoff–Kakutani theorem; the game criterion for completeness is due to Choquet. We prove the forms needed here.

#### Category and the open mapping theorem

**Lemma 8.1** (The Baire property of Polish images). A continuous image of a Polish space in a Polish space has the Baire property.

**Proof.** Write the image as \(A=f(P)\), and fix complete compatible metrics on \(P\) and on the target \(Y\). The empty image causes no difficulty. By Theorem 1.1, there is a countably branching family of nonempty closed sets \(F_s\) in \(P\), with \(F_s=\bigcup_jF_{sj}\), \(F_\varnothing=P\), and diameters tending to zero along branches. Set \(A_s=f(F_s)\). Thus \(A_s=\bigcup_jA_{sj}\).

First observe that if a subset \(E\) is nonmeagre in an open set \(W\), some nonempty open \(V\subseteq W\) has \(E\) nonmeagre in every nonempty open subset of \(V\). Indeed, let \(O\) be the union of the open subsets of \(W\) in which \(E\) is meagre. Second countability makes \(E\cap O\) meagre: a countable subfamily of these open sets covers \(O\). The relatively closed set \(W\setminus O\) cannot be nowhere dense in \(W\), for otherwise \(E\cap W\) would be meagre. Its relative interior contains the required \(V\).

Suppose \(A_s\) is nonmeagre in every nonempty open subset of a nonempty open set \(V_s\). In any nonempty open \(W\subseteq V_s\), some \(A_{sj}\cap W\) is nonmeagre, since their union is \(A_s\cap W\). The observation gives a nonempty open \(V\subseteq W\) where \(A_{sj}\) is nonmeagre in every nonempty open subset. Shrink \(V\) so that its closure lies in \(W\) and its diameter is at most \(2^{-|s|-1}\). There is a maximal pairwise disjoint family of such \(V\)'s, each labelled with its chosen \(j\). The family is countable, because disjoint nonempty open sets contain distinct members of a countable base. Its union is dense in \(V_s\): an open part of its complement would allow one more member. This constructs children of each \(V_s\). Distinct children may have the same source label; the tree of open sets retains the complete source label along each branch.

Starting in any open region \(V_\varnothing\) where \(A\) is everywhere nonmeagre, iterate this construction. At each level the union of the open sets is dense and open in \(V_\varnothing\). Their intersection is comeagre there by Baire. A point \(y\) in this intersection determines a unique nested branch of open sets and source labels \(s_n\). Since \(A_{s_n}\) is nonmeagre in every nonempty open subset of \(V_{s_n}\), it is dense in \(V_{s_n}\). Choose \(a_n\in F_{s_n}\) with \(d_Y(f(a_n),y)<1/n\). The sets \(F_{s_n}\) are nested, closed, and have diameters tending to zero. Hence \(a_n\to a\in\bigcap_nF_{s_n}\), by completeness. Continuity gives \(f(a)=y\). Thus \(A\) contains a comeagre subset of \(V_\varnothing\).

We have proved that every nonmeagre Polish image contains a comeagre subset of some nonempty open set. Let \(U\) be the union of all open sets in which \(A\) is comeagre. Second countability shows that \(U\setminus A\) is meagre. The remainder \(A\setminus U\) is again a Polish image: it is the image under \(f\) of the closed Polish subspace \(f^{-1}(Y\setminus U)\). If that remainder were nonmeagre, the assertion just proved would make it comeagre in a nonempty open \(V\). Then \(A\) would be comeagre in \(V\), so \(V\subseteq U\), whereas \(A\setminus U\) is empty there. This contradicts Baire. Consequently \(A\setminus U\) is meagre, and \(A\mathbin\triangle U\) is meagre. \(\square\)

**Theorem 8.2** (Pettis). Let \(G\) be a Polish group and \(A\subseteq G\) have the Baire property and be nonmeagre. Both \(A^{-1}A\) and \(AA^{-1}\) contain an open neighbourhood of the identity.

**Proof.** There is a nonempty open \(O\) in which \(A\) is comeagre. Fix \(x\in O\). Continuity of \(g\mapsto xg\) gives a neighbourhood \(V\) of the identity such that \(xV\subseteq O\). For \(g\in V\), the set \(O\cap Og^{-1}\) is nonempty and open: it contains \(x\). The sets \(A\) and \(Ag^{-1}\) are comeagre there. Their intersection is nonempty by Baire. A point \(a\in A\cap Ag^{-1}\) satisfies \(a\in A\) and \(ag\in A\), whence \(g=a^{-1}(ag)\in A^{-1}A\). Apply this result to \(A^{-1}\) to obtain a neighbourhood in \(AA^{-1}\). \(\square\)

**Theorem 8.3** (Open mapping for Polish groups). A continuous surjective homomorphism \(\phi:G\to L\) between Polish groups is open. It therefore induces a topological group isomorphism \(G/\ker\phi\cong L\).

**Proof.** Let \(U\) be a neighbourhood of the identity in \(G\). Choose an open symmetric neighbourhood \(V\) with \(V^{-1}V\subseteq U\). Separability gives a countable set \(D\) with \(G=DV\): for each \(g\), the open set \(gV^{-1}\) meets a countable dense set. Surjectivity gives \(L=\bigcup_{d\in D}\phi(d)\phi(V)\). The open subspace \(V\) is Polish by (F3), so its continuous image \(\phi(V)\) has the Baire property by Lemma 8.1. It cannot be meagre, since otherwise the nonempty Baire space \(L\) would be meagre in itself. Pettis gives an identity neighbourhood in
\[
\phi(V)^{-1}\phi(V)=\phi(V^{-1}V)\subseteq\phi(U).
\]
If \(W\subseteq G\) is open and \(g\in W\), choose such a \(U\) with \(gU\subseteq W\). The set \(\phi(g)\phi(U)\) contains a neighbourhood of \(\phi(g)\) lying in \(\phi(W)\). Hence \(\phi(W)\) is open. The kernel is closed. The induced bijection from the quotient is continuous by the definition of the quotient topology, and open by what we have just proved. \(\square\)

#### A quotient metric need not be complete

**Lemma 8.4** (Birkhoff–Kakutani invariant metrization). Every first countable Hausdorff topological group has a compatible right invariant metric. The metric is not asserted to be complete.

**Proof.** Choose symmetric identity neighbourhoods \(V_n\), \(n\geq0\), with \(V_0=G\), \(V_{n+1}^3\subseteq V_n\), and with \((V_n)\) a neighbourhood base. Continuity of multiplication and inversion permits this recursive choice, while intersection with the \(n\)-th member of an initial countable base ensures the base condition. Put
\[
\delta(x,y)=\inf\{2^{-n}:xy^{-1}\in V_n\},
\]
\[
d(x,y)=\inf_{\substack{m\geq1,\ x_0=x\\x_m=y}}
\sum_{i=1}^m\delta(x_{i-1},x_i).
\]
The infimum defining \(\delta\) is positive and attained when \(x\ne y\), since \(\bigcap_nV_n=\{1\}\); for \(x=y\) it is zero.

We need a finite product observation. If \(g_i\in V_{n_i}\) and \(\sum_i2^{-n_i}<2^{-n}\), then \(g_1\cdots g_m\in V_n\). Prove this by induction on \(m\), for all \(n\) at once. Let a middle term be one whose interval in the cumulative sum contains half the total. Each side has total at most half the original total, so by induction its product is in \(V_{n+1}\). The middle term itself has weight less than \(2^{-n}\), so it too is in \(V_{n+1}\). The product is in \(V_{n+1}^3\subseteq V_n\). Empty sides mean the identity.

Apply the observation to the increments \(x_{i-1}x_i^{-1}\), whose product telescopes to \(xy^{-1}\). It gives
\[
\tfrac12\delta(x,y)\leq d(x,y)\leq\delta(x,y).
\]
For the lower bound, if \(\delta(x,y)=2^{-k}\) and a chain had total less than \(2^{-k-1}\), the observation would put \(xy^{-1}\) in \(V_{k+1}\), a contradiction. The upper bound uses the one-edge chain. Chain concatenation proves the triangle inequality. Symmetry and right invariance hold for \(\delta\), and then for \(d\) by reversing or right translating chains. The comparison shows that \(d\) separates points and induces the given topology, because the \(V_n\)'s are a neighbourhood base. \(\square\)

**Lemma 8.5** (Metrizing cosets). If \(H\) is a closed subgroup of a first countable Hausdorff group \(G\), the space of left cosets \(G/H\) has a compatible metric
\[
\begin{aligned}
D(gH,kH)&=\inf_{h,l\in H}d(gh,kl)\\
&=\inf_{h\in H}d(gh,k),
\end{aligned}
\]
where \(d\) is a compatible right invariant metric on \(G\). The quotient map is open. If \(G\) is separable, so is \(G/H\).

**Proof.** The second formula follows by right translating both entries by \(l^{-1}\). It also shows positivity for distinct cosets: distance zero would put \(k\) in the closed set \(gH\). For the triangle inequality choose almost minimizing pairs from the first and second cosets and from the second and third. Right translate the first pair by an element of \(H\) so that the two middle representatives agree; this leaves its distance unchanged. Apply the triangle inequality for \(d\), then take infima. Symmetry is immediate. Moreover
\[
B_D(kH,r)=q(B_d(k,r)).
\]
Indeed, a coset is within \(r\) of \(kH\) precisely when one of its representatives is within \(r\) of \(k\). The map \(q\) is continuous for \(D\), since \(D(q(g),q(k))\leq d(g,k)\). It is open for the quotient topology because \(q^{-1}(q(W))=WH\) is open whenever \(W\) is open. The ball identity proves that the metric and quotient topologies coincide. The continuous image of a countable dense set is dense. \(\square\)

#### Completeness of an open image

For completeness we prove the topological tool used next. A *strong Choquet play* in a space \(Y\) consists of points and nonempty open sets
\[
\begin{gathered}
x_n\in U_n,\qquad x_n\in B_n\subseteq U_n,\\
U_{n+1}\subseteq B_n.
\end{gathered}
\]
The first player chooses \((x_n,U_n)\); the second chooses \(B_n\). A strategy for the second player is *winning* if every play following it has \(\bigcap_nB_n\ne\varnothing\).

#### Completing a metric space

**Lemma (Metric completion).** Every metric space \((Y,r)\) embeds isometrically as a dense subspace of a complete metric space \((Z,\bar r)\). If \(Y\) is separable, so is \(Z\). No compatibility with a group operation is asserted.

*Proof.* Let \(\mathscr S\) be the set of Cauchy sequences in \(Y\). For \(a=(a_n)\) and \(b=(b_n)\), the inequality
\[
|r(a_n,b_n)-r(a_m,b_m)|
\leq r(a_n,a_m)+r(b_n,b_m)
\]
shows that \(r(a_n,b_n)\) is a Cauchy sequence of real numbers. Its limit \(R(a,b)\) exists. Symmetry and the triangle inequality pass to this limit. Thus the relation \(a\sim b\) defined by \(R(a,b)=0\) is an equivalence relation. The triangle inequality also shows that replacing either sequence by an equivalent one preserves \(R\). The set \(Z=\mathscr S/\mathord\sim\), with \(\bar r([a],[b])=R(a,b)\), is therefore a metric space. Constant sequences embed \(Y\) isometrically.

For \(a\in\mathscr S\), let \(y_n\in Z\) denote the constant sequence at \(a_n\). Given \(\varepsilon>0\), the Cauchy condition gives \(r(a_n,a_m)<\varepsilon\) for all sufficiently large \(n,m\). Taking the limit in \(m\) gives \(\bar r(y_n,[a])\leq\varepsilon\) for all sufficiently large \(n\). Consequently \(y_n\to[a]\), and the embedded copy of \(Y\) is dense.

To prove completeness, let \((z_k)\) be a Cauchy sequence in \(Z\). By density choose \(y_k\in Y\) with \(\bar r(y_k,z_k)<1/k\). Then
\[
r(y_k,y_l)
\leq 1/k+\bar r(z_k,z_l)+1/l,
\]
so \((y_k)\) is Cauchy in \(Y\) and defines \(z=[(y_k)]\in Z\). The preceding paragraph gives \(y_k\to z\); the bound \(\bar r(z_k,z)\leq1/k+\bar r(y_k,z)\) gives \(z_k\to z\). Hence \(Z\) is complete. Finally a countable dense subset of \(Y\) remains dense in \(Z\): approximate first by a point of \(Y\), then by a point of that subset, using the triangle inequality. \(\square\)

**Lemma 8.6** (Completeness criterion). A second countable metrizable space with a winning strong Choquet strategy is Polish.

**Proof.** We give the construction, including its covering step. Fix a compatible metric \(r\), bounded by \(1\), and let \(Z\) be its completion. The metric-completion lemma just proved constructs \(Z\), proves its completeness, and shows that \(Y\) embeds densely and isometrically. A countable dense subset of \(Y\) remains dense in \(Z\), so \(Z\) is Polish.

*Locally finite refinements.* Every countable open cover \((O_i)\) of a metric space has a countable open refinement \((T_j)\) that covers the space, is locally finite, and has each \(\overline{T_j}\) contained in one \(O_i\). Here is a direct proof. Put \(A_n=\bigcup_{i\leq n}O_i\) and
\[
\begin{aligned}
F_n&=\{y:r(y,Y\setminus A_n)\geq1/n\},\\
L_n&=\operatorname{int}F_{n+1}\setminus F_{n-1},
\end{aligned}
\]
with \(F_0=\varnothing\) and distance to the empty set interpreted as infinity. The \(F_n\)'s increase, \(F_n\subseteq\operatorname{int}F_{n+1}\), and their interiors cover \(Y\). Hence the \(L_n\)'s cover \(Y\) and are locally finite. Write \(t_i(y)=\min(1,r(y,Y\setminus O_i))\), taking \(t_i=1\) if \(O_i=Y\). Refine \(L_n\) by the finitely many open sets
\[
\begin{aligned}
T_{n,i}&=L_n\cap\\
&\quad\left\{y:t_i(y)>
\frac{\max_{k\leq n+1}t_k(y)}{2(n+1)}\right\},
\end{aligned}
\]
where \(i\leq n+1\). They cover \(L_n\). Their closures lie in \(F_{n+1}\subseteq A_{n+1}\); on this closed set the displayed maximum is positive. The non-strict inequality on the closure therefore forces \(t_i>0\), so \(\overline{T_{n,i}}\subseteq O_i\). Local finiteness follows from that of the \(L_n\)'s. This proves the covering assertion, also for an open subspace with its relative metric.

*Extending a locally finite family.* If \((T_i)\) is a locally finite family of open sets in an open subspace \(V\subseteq Y\), its members have open extensions in \(Z\) that are locally finite on some open neighbourhood of \(V\) in \(Z\). To see this, the canonical extension of \(T_i\), considered as an open set of \(Y\), is
\[
\widehat T_i=Z\setminus\overline{Y\setminus T_i}^{\,Z}.
\]
Its trace on \(Y\) is \(T_i\). At each \(y\in V\), choose a ball in \(Y\) contained in \(V\) and meeting only finitely many \(T_i\)'s. A smaller corresponding ball in \(Z\) meets only these canonical extensions: any nonempty open intersection with another extension would meet the dense subset \(Y\), contradicting the choice of ball. The union of these smaller balls is the required open neighbourhood. Extensions may be intersected with any prescribed open sets containing their traces. They may also be kept within distance \(\varepsilon\) of their traces, by intersection with \(\bigcup_{t\in T_i}B_Z(t,\varepsilon)\). Thus a family of sufficiently small trace diameters has extensions of arbitrarily small prescribed diameters.

*A tree of plays.* Start with the empty play. For every \(y\in Y\), choose a first-player neighbourhood \(U_y\ni y\) of diameter less than \(1/4\), and let \(B_y\ni y\) be the response of the strategy. Choose a countable subcover from these responses. Refine it by the locally finite family just constructed, with each trace \(T_s\) having closure inside its assigned response \(B_s\). Attach the corresponding first move and response to \(s\).

Recursively, at a node \(s\), for each \(y\in T_s\) choose a next move \((y,U_y)\) with \(U_y\subseteq T_s\) and diameter less than \(2^{-|s|-3}\). Its strategy response contains \(y\). A countable subcover of these responses, refined as above, gives children whose traces cover \(T_s\); each child retains its assigned move, response and the previous history. Every descending branch is consequently a legal play of the strategy.

Use the extension step at each node. Extend its children inside the node's current open extension, with diameters at most \(2^{-|s|-1}\). Shrink the parent's extension to the open neighbourhood of its trace on which the children are locally finite, and restrict the child extensions to that neighbourhood. This shrinking does not change any trace on \(Y\). At the root the same step starts in \(Z\). Each node's final extension is fixed when its children are chosen; later shrinkings affect only descendants. Denote these final open extensions by \(W_s\). Children lie inside their final parent; the family of children is locally finite there; and \(\operatorname{diam}W_s\leq2^{-|s|}\). At each depth the traces cover \(Y\). Put
\[
O_n=\bigcup_{|s|=n}W_s.
\]
These are open sets in \(Z\) containing \(Y\).

Let \(z\in\bigcap_nO_n\). At each depth some node contains \(z\). There are only finitely many such first-level nodes, and only finitely many such children of any node containing \(z\), by local finiteness. Children have parents containing \(z\). The elementary finite-branching tree argument therefore gives an infinite branch \(s_1,s_2,\ldots\) with \(z\in W_{s_n}\): from a node having descendants at arbitrarily large depths, choose a child with the same property. Its associated play is won, so some \(y\in Y\) belongs to every response \(B_{s_n}\). Choose \(t_n\in T_{s_n}\subseteq B_{s_n}\). The diameter bounds on \(W_{s_n}\) and on the move containing \(B_{s_n}\) give \(r_Z(z,t_n)\to0\) and \(r(y,t_n)\to0\). Hence \(z=y\in Y\). We have proved \(Y=\bigcap_nO_n\), a \(G_\delta\) in the Polish space \(Z\). By (F3), \(Y\) is Polish. \(\square\)

**Theorem 8.7** (Open images). Let \(P\) be Polish, \(Y\) metrizable, and \(f:P\to Y\) continuous, open and surjective. Then \(Y\) is Polish.

**Proof.** The images of a countable base of \(P\) form a countable base of \(Y\). Fix a complete compatible metric on \(P\). The second player wins the strong Choquet game on \(Y\) by lifting moves. For the first move \((y_1,U_1)\), choose \(a_1\in f^{-1}(y_1)\), and a nonempty open \(V_1\ni a_1\) of diameter at most \(1/2\), whose closure lies in \(f^{-1}(U_1)\). Respond with \(B_1=f(V_1)\), which is open and contains \(y_1\).

For a later move \((y_n,U_n)\), with \(U_n\subseteq f(V_{n-1})\), choose \(a_n\in V_{n-1}\cap f^{-1}(y_n)\). Choose \(V_n\ni a_n\) of diameter at most \(2^{-n}\), with \(\overline{V_n}\subseteq V_{n-1}\cap f^{-1}(U_n)\), and respond with \(B_n=f(V_n)\). The closed sets \(\overline{V_n}\) are nonempty, nested, and have diameters tending to zero. Completeness gives a common point \(a\). Since \(\overline{V_{n+1}}\subseteq V_n\), this point lies in every \(V_n\), so \(f(a)\in\bigcap_nB_n\). Lemma 8.6 now proves that \(Y\) is Polish. \(\square\)

**Theorem 8.8** (Polish coset spaces). If \(G\) is a Polish group and \(H\subseteq G\) is a closed subgroup, \(G/H\), with the quotient topology, is Polish. The same holds for \(H\backslash G\). No normality is required. When \(H\) is normal, the quotient is a Polish topological group.

**Proof.** Lemmas 8.4 and 8.5 give a compatible metric on \(G/H\) and show that \(q:G\to G/H\) is continuous, open and surjective. Theorem 8.7 gives completeness for a compatible metric on the quotient. Inversion identifies the left and right coset spaces homeomorphically. If \(H\) is normal, multiplication and inversion descend continuously: \(q\times q\) is an open quotient map, and the group operations commute with the quotient maps. \(\square\)

The invariant metric in Lemma 8.4 was used only for metrization. Its completeness was never assumed. The complete metric on \(G\) used in Theorem 8.7 can be entirely different.

**Example 8.9** (A quotient and its section). The quotient \(\mathbb R/\mathbb Z\) is homeomorphic to the circle through \(x+\mathbb Z\mapsto e^{2\pi ix}\). The displayed map is well defined, continuous and bijective: two real numbers have the same exponential exactly when their difference is an integer. The quotient is compact since it is the image of \([0,1]\), and the circle is Hausdorff. The compact-to-Hausdorff argument (B3) therefore proves the homeomorphism. It is Polish by Theorem 8.8. The Borel section from Example 7.5 takes values in \([0,1)\), but is not continuous. Polish topology on the quotient does not make every Borel choice continuous.

**Example 8.10** (Why both Polish hypotheses matter for open mapping). Give \(\mathbb R\) its discrete topology. The identity homomorphism to \(\mathbb R\) with its usual topology is continuous and onto, but is not open, since the image of a singleton is not open. The discrete source is complete but is not separable. Separability cannot simply be omitted from Theorem 8.3.

## Exercises

**Exercise 1** (medium; Borel graphs). Let \(X\) and \(Y\) be standard Borel spaces and \(f:X\to Y\) a map. Show that \(f\) is Borel if and only if its graph is a Borel subset of \(X\times Y\), with the product Borel structure.

*Solution.* If \(f\) is Borel, the graph lies in the product \(\sigma\)-algebra by Proposition 4.1, since \(Y\) is countably separated. Conversely, let the graph \(G\) be Borel. Choose Polish topologies on \(X\) and \(Y\) that give their Borel sets; then the product \(\sigma\)-algebra is the Borel structure of the Polish space \(X\times Y\) (F1). For Borel \(E\subseteq Y\),
\[
\begin{gathered}
f^{-1}(E)\\
=\pi_X\big(G\cap(X\times E)\big),\\
X\setminus f^{-1}(E)\\
=\pi_X\big(G\cap(X\times(Y\setminus E))\big).
\end{gathered}
\]
The sets inside the brackets are Borel in \(X\times Y\), hence Souslin sets (Corollary 2.6), and the projection \(\pi_X\) is continuous. So \(f^{-1}(E)\) and its complement are Souslin sets of \(X\), and \(f^{-1}(E)\) is Borel by Souslin's theorem (Corollary 2.5).

**Exercise 2** (medium; Quotients by Borel surjections). Let \(Z\) be a standard Borel space, \(Y\) a Borel space whose points are separated by countably many Borel sets, and \(f:Z\to Y\) a Borel surjection. Show that \(E\subseteq Y\) is Borel if and only if \(f^{-1}(E)\) is Borel in \(Z\). Show by an example that the hypothesis "countably separated" cannot be dropped.

*Solution.* "Only if" is clear. \(Y\) is a Souslin–Borel space by definition; let \(\varphi:Y\to\mathcal C\) be the injective Borel map of Lemma 5.5(3). Suppose \(f^{-1}(E)\) is Borel. Then \(\varphi(E)=(\varphi\circ f)(f^{-1}(E))\) and \(\varphi(Y\setminus E)=(\varphi\circ f)(Z\setminus f^{-1}(E))\) are Souslin sets in \(\mathcal C\), by Lemma 5.5(1), because Borel subsets of \(Z\) are standard (F4). They are disjoint, since \(\varphi\) is injective and \(f\) is onto. By the separation theorem (Theorem 2.4), some Borel \(D\subseteq\mathcal C\) contains \(\varphi(E)\) and misses \(\varphi(Y\setminus E)\); then \(E=\varphi^{-1}(D)\) is Borel.

For the example, let \(Y=[0,1]\) with the \(\sigma\)-algebra of countable and co-countable sets, and let \(f\) be the identity map from \([0,1]\) with its Borel sets. \(f\) is Borel and onto, and \(f^{-1}([0,\tfrac12])\) is Borel, but \([0,\tfrac12]\) is not in the \(\sigma\)-algebra of \(Y\). This \(Y\) is not countably separated. Given countably many countable or co-countable sets, replace each co-countable one by its complement; a set and its complement separate the same pairs. The uncountably many points outside the union of the resulting countable sets are separated by none of them.

**Exercise 3** (medium; Orbits of a compact group). Let a compact metrizable group \(K\) act continuously on a Polish space \(X\), that is, \((k,x)\mapsto k\cdot x\) is a continuous action. Show that some Borel set meets every orbit exactly once, and that the orbit space \(X/K\), with the quotient topology and its Borel sets, is a standard Borel space.

*Solution.* Orbits \(K\cdot x\) are compact, hence closed, since \(X\) is Hausdorff. For open \(U\), the saturation \(K\cdot U=\bigcup_kk\cdot U\) is open, because each \(x\mapsto k\cdot x\) is a homeomorphism. So Theorem 7.1 gives a Borel transversal \(S\).

Next, \(X/K\) is Hausdorff. First, \(K\cdot F\) is closed for closed \(F\): if \(k_n\cdot z_n\to w\) with \(z_n\in F\), pass to a subsequence with \(k_n\to k\), which is possible because \(K\) is compact and metrizable; then \(z_n=k_n^{-1}\cdot(k_n\cdot z_n)\to k^{-1}\cdot w\) by continuity, so \(k^{-1}\cdot w\in F\) and \(w\in K\cdot F\). Now let \(K\cdot x\neq K\cdot y\). These disjoint compact sets have disjoint open neighbourhoods \(U\) and \(W\). The sets \(U'=X\setminus K\cdot(X\setminus U)\) and \(W'=X\setminus K\cdot(X\setminus W)\) are open and saturated, \(K\cdot x\subseteq U'\subseteq U\) and \(K\cdot y\subseteq W'\subseteq W\). Their images in \(X/K\) are open, since a saturated open set is the full preimage of its image, and they are disjoint.

Finally, the quotient map is continuous and injective on \(S\), and \(S\) is a Borel subset of a Polish space. As in the proof of Proposition 7.4(3), it is a Borel isomorphism of \(S\) onto \(X/K\), so \(X/K\) is standard.

**Exercise 4** (medium; Product \(\sigma\)-algebras). Let \(D\) be a set of cardinality greater than \(2^{\aleph_0}\), with the discrete topology. Show that the diagonal of \(D\times D\) is Borel in the discrete space \(D\times D\) but does not belong to \(\mathcal B(D)\otimes\mathcal B(D)\). Conclude that the open boxes of \(D\times D\) generate a strictly smaller \(\sigma\)-algebra than its open sets.

*Solution.* \(D\times D\) is discrete, so every subset is open. If the diagonal belonged to \(\mathcal B(D)\otimes\mathcal B(D)\), then \(D\) would be countably separated by Proposition 4.1(3). A countable separating family \((S_n)\) gives an injective map \(x\mapsto(1_{S_n}(x))_n\) of \(D\) into \(\mathcal C\), so \(|D|\leq2^{\aleph_0}\), which is false. The open boxes \(U\times V\) generate \(\mathcal B(D)\otimes\mathcal B(D)\), which misses the diagonal. So testing a map into \(D\times D\) on preimages of open boxes proves measurability for \(\mathcal B(D)\otimes\mathcal B(D)\) only, and not for \(\mathcal B(D\times D)\) (compare Remark 4.2).

**Exercise 5** (medium; An explicit isomorphism). Build a Borel isomorphism of \(\mathcal C\) onto \([0,1]\) by hand, using binary expansions and moving a countable set. Show that no homeomorphism exists.

*Solution.* Let \(\beta(c)=\sum_kc_k2^{-k}\). It is continuous and onto. Two different sequences have the same image exactly when one has the form \(w0111\cdots\) and the other \(w1000\cdots\) for a finite word \(w\); the common image is a dyadic rational in \((0,1)\). Indeed, if \(c\) and \(c'\) first differ at place \(k\), with \(c_k=0\) and \(c'_k=1\), then \[
\begin{gathered}
\beta(c')-\beta(c)\\
=2^{-k}+\sum_{j>k}(c'_j-c_j)2^{-j}\\
\geq2^{-k}-\sum_{j>k}2^{-j}\\
=0,
\end{gathered}
\] with equality exactly when \(c_j=1\) and \(c'_j=0\) for all \(j>k\).

Let \(E\) be the countable set of sequences that end in \(1\)'s but are not all \(1\)'s. Then \(\beta\) is a bijection of \(\mathcal C\setminus E\) onto \([0,1]\): a dyadic rational in \((0,1)\) keeps its preimage ending in \(0\)'s, the points \(0\) and \(1\) have the single preimages \(000\cdots\) and \(111\cdots\), and every other point has one preimage, which is not in \(E\). The inverse can be given explicitly. For \(0\leq t<1\), put
\[
b_n(t)=\lfloor2^nt\rfloor-2\lfloor2^{n-1}t\rfloor,
\qquad n\geq1,
\]
and put \(b_n(1)=1\). Each digit lies in \(\{0,1\}\). For \(t<1\), the first \(n\) binary terms sum to \(2^{-n}\lfloor2^nt\rfloor\), which tends to \(t\). Dyadic points receive an expansion ending in zeros; a nondyadic point cannot have an expansion ending in ones, since such an expansion sums to a dyadic number. Thus \(b(t)\in\mathcal C\setminus E\), and the uniqueness already proved gives \(b=\beta^{-1}\) on that set. The floor function is Borel because each integer level set is a half-open interval. Hence each digit is Borel, and (F1) shows that \(b\) is Borel. Therefore \(\beta\) is a Borel isomorphism of \(\mathcal C\setminus E\) onto \([0,1]\).

Next let \(e_n\in\mathcal C\) have a single \(1\), at place \(n\); these points are not in \(E\). Enumerate \(E=\{f_1,f_2,\dots\}\) and define \(\theta:\mathcal C\to\mathcal C\setminus E\) by \(\theta(f_n)=e_{2n-1}\), \(\theta(e_n)=e_{2n}\), and \(\theta(c)=c\) otherwise. \(\theta\) is a bijection that moves only a countable set, all of whose subsets are Borel, so \(\theta\) and \(\theta^{-1}\) are Borel. Then \(\beta\circ\theta\) is a Borel isomorphism of \(\mathcal C\) onto \([0,1]\). No homeomorphism exists, since \([0,1]\) is connected and \(\mathcal C\) is not.

**Exercise 6** (easy; First application). Let \(\phi:G\to L\) be a continuous bijective homomorphism of Polish groups. Prove that its inverse is continuous. Apply this to show that two Polish group topologies on the same group coincide whenever one is finer than the other.

*Solution.* By Theorem 8.3, \(\phi\) is open. Therefore \((\phi^{-1})^{-1}(U)=\phi(U)\) is open for every open \(U\subseteq G\). For the second assertion use the identity map from the finer topology to the coarser one. It is a continuous bijective homomorphism between Polish groups, so its inverse is continuous as well.

**Exercise 7** (easy; Closedness and quotient topology). Show that \(\mathbb R/\mathbb Q\), with the quotient topology, is not Hausdorff. In fact show that its only open sets are the empty set and the entire quotient. Explain why a standard Borel structure on a set, even if one is chosen separately, would not repair this topology.

*Solution.* A nonempty open saturated subset \(W\subseteq\mathbb R\) contains an interval \(I\). Since \(I+\mathbb Q=\mathbb R\), saturation forces \(W=\mathbb R\). Thus the quotient has the indiscrete topology and more than one point; it is not Hausdorff and cannot be Polish. A separately assigned sigma-algebra does not change its open sets. The closed-subgroup hypothesis in Theorem 8.8 is a topological requirement.

**Exercise 8** (medium; Compact orbits, a stronger conclusion). In Exercise 3, prove that the quotient \(X/K\) is Polish, rather than merely standard Borel.

*Solution.* Start with any bounded complete compatible metric \(r\) on \(X\), and set \(r_K(x,y)=\max_{k\in K}r(kx,ky)\). Compactness and continuity make the maximum finite. This is a \(K\)-invariant metric and dominates \(r\). It has the same topology as \(r\): if \(x_n\to x\), continuity of the action is uniform on the compact set \(K\times\{x\}\), so \(\max_k r(kx_n,kx)\to0\). For clarity, if this failed choose \(k_n\in K\) with a fixed positive lower bound; a convergent subsequence of \(k_n\) and joint continuity give a contradiction. An \(r_K\)-Cauchy sequence converges for \(r\), and hence for \(r_K\), so \(r_K\) is complete. Define \(D(Kx,Ky)=\min_{k\in K}r_K(x,ky)\). The minimum exists; it is positive for distinct compact orbits, and invariance proves the triangle inequality by aligning middle representatives. Its open balls are images of \(r_K\)-balls, so it induces the quotient topology. The quotient map is continuous, open and onto. Theorem 8.7 proves that \(X/K\) is Polish. This supplies the stronger topological conclusion while retaining the Borel transversal of Exercise 3.

## Where this leads

- *Decomposition theory.* By the isomorphism theorem (Theorem 5.2), an uncountable standard Borel space can always be replaced by \([0,1]\) or \(\mathcal C\). Direct integrals and disintegrations of measures are set up over standard Borel spaces for this reason. The measurable sections of Theorem 7.7 are used there to choose measurable families, for instance of unitaries.
- *The Borel space of von Neumann algebras.* The von Neumann algebras on a separable Hilbert space form a standard Borel space ([The Effros Borel structure](the-effros-borel-structure.md)). In the study of this space, Theorem 4.3(5) shows that a unitary orbit is Borel, once the orbit is written as a one-to-one Borel image of a standard Borel space. Proposition 7.4 and the separation theorem enter the same study.
- *Extensions of Polish groups.* If \(E\) is a Polish group and \(A\) a closed subgroup, Proposition 7.4 gives a Borel section \(\sigma:E/A\to E\) with \(\sigma(A)=1\). Such normalized sections are used in the study of crossed products and the flow of weights. Theorems 8.3 and 8.8 prove that \(E/A\) is Polish and that continuous surjective homomorphisms of Polish groups are open.
- *Unused extension, not proved here: countable-to-one maps.* Theorem 7.1 also gives Borel right inverses of continuous countable-to-one maps \(f\) from a Polish space into a Polish space, once one knows Lusin's theorem that such maps carry Borel sets to Borel sets, which is not proved here. The classes are the fibres of \(f\), and the saturation \(f^{-1}(f(U))\) of an open set \(U\) is Borel.
- *Closed sets.* The nonempty closed subsets of a Polish space form a standard Borel space for the Effros Borel structure; see [the lesson on the Effros Borel structure](the-effros-borel-structure.md#oa-fnd-ef-05).
- *Not treated here:* the Borel hierarchy, co-analytic and projective sets, the second separation theorem and finer uniformization theorems, Borel sections of arbitrary Borel surjections, and nonseparable spaces.

## References

Open ones first.


*Freely accessible reading:* [Anush Tserunyan, *Introduction to descriptive set theory*, §§1–6, 12A–12C and 13A–13C](https://www.math.mcgill.ca/atserunyan/Teaching_notes/dst_lectures.pdf) gives a route through Polish models, analytic separation and Borel inversion; the exercises and the group-quotient proof are supplied here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

For countable generators and the precise measurability of prefix selection, see [Fremlin, Chapter 42, 423J, 423N–423P and 424B–424G](https://www1.essex.ac.uk/maths/people/fremlin/chap42.pdf).

Open ones first.

- [Souslin 1917] M. Souslin, "Sur une définition des ensembles mesurables B sans nombres transfinis", *Comptes rendus de l'Académie des sciences* 164 (1917), 88–91. https://gallica.bnf.fr/ark:/12148/bpt6k31178/f88.item
- [Lusin 1917] N. Lusin, "Sur la classification de M. Baire", *Comptes rendus de l'Académie des sciences* 164 (1917), 91–94. https://gallica.bnf.fr/ark:/12148/bpt6k31178/f91.item
- [Lusin 1927] N. Lusin, "Sur les ensembles analytiques", *Fundamenta Mathematicae* 10 (1927), 1–95. https://doi.org/10.4064/fm-10-1-1-95
- [Mackey 1957] G. W. Mackey, "Borel structure in groups and their duals", *Transactions of the American Mathematical Society* 85 (1957), 134–165. https://doi.org/10.1090/S0002-9947-1957-0089999-2
- [Moschovakis] Y. N. Moschovakis, *Descriptive Set Theory*, 2nd ed., Mathematical Surveys and Monographs 155, American Mathematical Society, 2009. https://www.math.ucla.edu/~ynm/lectures/dst2009/dst2009.pdf
- [Blackwell 1956] D. Blackwell, ["On a class of probability spaces"](https://projecteuclid.org/euclid.bsmsp/1200502002), *Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability*, Vol. II, University of California Press, 1956, 1–6.
- [Takesaki I] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979; reprinted as Encyclopaedia of Mathematical Sciences 124, Springer, 2002.
