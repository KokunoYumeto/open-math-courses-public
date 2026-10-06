# Covering dimension and finite trivializing covers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A vector bundle over a compact manifold is trivial over each set of a finite open cover. This lesson proves the same for every manifold, compact or not, with a number of sets that depends only on the dimension: a vector bundle over an \(n\)-dimensional manifold is trivial over each of \(3(n+1)\) open sets that cover the manifold (Corollary 6.2). Consequently every vector bundle over a manifold is a direct summand of a trivial bundle of finite rank (Corollary 6.3), which extends the stable complements of the lesson on the Bott operator to bases that are not compact.

The proof is a piece of dimension theory. A space has *covering dimension* at most \(n\) if every finite open cover has an open refinement in which each point lies in at most \(n+1\) sets (Definition 2.1). Compact subsets of \(\mathbb R^n\) have covering dimension at most \(n\), by an explicit arrangement of small open sets around the faces of a cubical lattice (Lemma 4.1 and Theorem 4.2). Hemmingsen's characterization of dimension (Theorem 2.3) gives a sum theorem for closed sets (Theorem 3.2), and from it every compact subset of a manifold has dimension at most \(n\). Finally a cover of bounded order is turned into \(n+1\) *colours*, each a disjoint union of small open sets (Lemma 5.1), and compact shells of the manifold are combined three at a time (Theorem 5.2).

Covering dimension goes back to Lebesgue [Lebesgue 1911]; the characterization by shrinkings is due to Hemmingsen, and the passage from bounded order to colours to Ostrand [Ostrand 1971].

We assume the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): compactness, the Heine–Borel theorem, and the Urysohn metrization theorem in its completion module *Metrization: from pseudometrics to Urysohn's theorem*. The last section uses Lemma 12.5 of [The Bott operator, suspension, and reduction of the index to Euclidean space](the-bott-operator-suspension-and-reduction-of-the-index-to-euclidean-space.md#AN-FND-BO-12).

## 1. Conventions and first facts

A *manifold of dimension \(n\)* is a Hausdorff topological space with a countable base in which every point has an open neighbourhood homeomorphic to an open subset of \(\mathbb R^n\). By the Urysohn metrization theorem it is metrizable: a regular space with a countable base has a compatible metric, and a manifold is regular because every point has a basis of compact neighbourhoods, the preimages of closed balls under charts.

A *cover* of a space \(X\) is a family of subsets whose union is \(X\). A cover \(\mathcal V\) *refines* a cover \(\mathcal U\) if every member of \(\mathcal V\) lies in some member of \(\mathcal U\). A family of sets has *order at most \(m\)* if every point lies in at most \(m\) of its members. A *shrinking* of a cover \((U_i)_{i\in I}\) is a cover \((V_i)_{i\in I}\) with the same index set and \(V_i\subseteq U_i\). For a subset \(A\) of a metric space and a point \(x\), \(d(x,A)=\inf_{a\in A}d(x,a)\), with \(d(x,\varnothing)=\infty\); it is a continuous function of \(x\), and \(d(x,A)=0\) exactly when \(x\in\overline A\).

**Lemma 1.1** (Metric spaces). Let \(X\) be a metric space.

1. Disjoint closed sets \(A,B\) have disjoint open neighbourhoods; indeed \(U=\{x:d(x,A)<d(x,B)\}\) and \(V=\{x:d(x,B)<d(x,A)\}\) are such neighbourhoods. So \(X\) is *normal*.
2. (*Lebesgue number.*) If \(X\) is compact and \(\{A_1,\dots,A_k\}\) is an open cover, there is \(\lambda>0\) such that every subset of \(X\) with diameter less than \(\lambda\) lies in some \(A_i\).
3. (*Separating relatively open sets.*) Let \(L\subseteq X\), and let \((W_s)\) be pairwise disjoint subsets of \(L\) that are open in \(L\). Then the sets \(\tilde W_s=\{x\in X:d(x,W_s)<d(x,L\setminus W_s)\}\) are open in \(X\), pairwise disjoint, and \(\tilde W_s\cap L=W_s\).

**Proof.** (1) If \(x\in A\), then \(d(x,A)=0<d(x,B)\), because \(B\) is closed and does not contain \(x\); so \(A\subseteq U\), and likewise \(B\subseteq V\). The sets are open by continuity and disjoint by definition.

(2) The function \(f(x)=\max_id(x,X\setminus A_i)\) is continuous and positive: each \(x\) lies in some open \(A_i\), at positive distance from its closed complement. On the compact space \(X\) it has a positive minimum \(\lambda\). If \(\operatorname{diam}S<\lambda\) and \(x\in S\), choose \(i\) with \(d(x,X\setminus A_i)\ge\lambda\); then \(S\subseteq A_i\).

(3) Openness follows from continuity. For \(x\in W_s\), \(d(x,W_s)=0<d(x,L\setminus W_s)\), because \(L\setminus W_s\) is closed in \(L\) and does not contain \(x\); points of \(L\setminus W_s\) satisfy the reverse; so \(\tilde W_s\cap L=W_s\). If \(x\in\tilde W_s\cap\tilde W_t\) with \(s\ne t\), then \(W_t\subseteq L\setminus W_s\) and \(W_s\subseteq L\setminus W_t\) give
\[
d(x,L\setminus W_s)\le d(x,W_t)<d(x,L\setminus W_t)\le d(x,W_s)<d(x,L\setminus W_s),
\]
which is impossible. \(\square\)

**Lemma 1.2** (Shrinking and swelling). Let \(X\) be a normal space.

1. Every finite open cover \(\{U_1,\dots,U_k\}\) has an open shrinking \(\{V_i\}\) with \(\overline{V_i}\subseteq U_i\); so \(\{\overline{V_i}\}\) is a closed shrinking.
2. Let \(F_1,\dots,F_k\) be closed sets with \(\bigcap_iF_i=\varnothing\) and \(F_i\subseteq U_i\) for open \(U_i\). There are open sets \(O_i\) with \(F_i\subseteq O_i\subseteq\overline{O_i}\subseteq U_i\) and \(\bigcap_i\overline{O_i}=\varnothing\).

**Proof.** (1) The closed set \(X\setminus(U_2\cup\dots\cup U_k)\) lies in \(U_1\). By normality there is an open \(V_1\) containing it with \(\overline{V_1}\subseteq U_1\), and \(\{V_1,U_2,\dots,U_k\}\) is again a cover. Repeat with \(U_2,\dots,U_k\) in turn.

(2) Suppose \(O_1,\dots,O_{i-1}\) have been chosen with \(\overline{O_j}\subseteq U_j\), such that \(\overline{O_1},\dots,\overline{O_{i-1}},F_i,\dots,F_k\) have empty intersection. The closed set \(C=\overline{O_1}\cap\dots\cap\overline{O_{i-1}}\cap F_{i+1}\cap\dots\cap F_k\) is disjoint from \(F_i\), and so is \(X\setminus U_i\). By normality there is an open \(O_i\supseteq F_i\) whose closure misses \(C\cup(X\setminus U_i)\). Then \(\overline{O_1},\dots,\overline{O_i},F_{i+1},\dots,F_k\) have empty intersection. After \(k\) steps we are done. \(\square\)

## 2. Covering dimension

**Definition 2.1.** A normal space \(X\) has *covering dimension at most \(n\)*, written \(\dim X\le n\), if every finite open cover of \(X\) has an open refinement of order at most \(n+1\).

The property is invariant under homeomorphisms. A subset of \(X\) carries the relative topology, and \(\dim\) of a closed subset refers to that topology; closed subsets of normal spaces are normal.

**Lemma 2.2.** Let \(X\) be normal. If every open cover \(\{U_1,\dots,U_{n+2}\}\) of \(X\) by \(n+2\) sets has an open shrinking with empty intersection, then every finite open cover \(\{U_1,\dots,U_k\}\) of \(X\) has an open shrinking of order at most \(n+1\).

**Proof.** Take the \((n+2)\)-element subsets \(S\) of \(\{1,\dots,k\}\) one after another, and replace the current cover by a shrinking in which \(\bigcap_{i\in S}U_i=\varnothing\). Since every step shrinks the sets, intersections that are already empty stay empty, and at the end every point lies in at most \(n+1\) sets.

For one step, write \(S=\{s_1,\dots,s_{n+2}\}\) and consider the open cover of \(X\) by
\[
W_l=U_{s_l}\ (l\le n+1),\qquad W_{n+2}=U_{s_{n+2}}\cup\bigcup_{j\notin S}U_j .
\]
By hypothesis it has an open shrinking \(\{O_l\}\) with \(\bigcap_lO_l=\varnothing\). Put \(U'_{s_l}=O_l\) for \(l\le n+1\), \(U'_{s_{n+2}}=O_{n+2}\cap U_{s_{n+2}}\), and \(U'_j=U_j\) for \(j\notin S\). A point in some \(O_l\) with \(l\le n+1\) is covered; a point in \(O_{n+2}\subseteq W_{n+2}\) lies in \(U'_{s_{n+2}}\) or in some \(U'_j=U_j\) with \(j\notin S\). So \(\{U'_i\}\) is a shrinking of \(\{U_i\}\), and \(\bigcap_{i\in S}U'_i\subseteq\bigcap_lO_l=\varnothing\). \(\square\)

**Theorem 2.3** (Hemmingsen). For a normal space \(X\) and \(n\ge0\) the following are equivalent.

1. \(\dim X\le n\).
2. Every open cover \(\{U_1,\dots,U_{n+2}\}\) has an open shrinking \(\{V_i\}\) with \(\bigcap_iV_i=\varnothing\).
3. Every open cover \(\{U_1,\dots,U_{n+2}\}\) has a closed shrinking \(\{F_i\}\) with \(\bigcap_iF_i=\varnothing\).

Moreover, if these hold, every finite open cover has an open shrinking of order at most \(n+1\).

**Proof.** (1)\(\Rightarrow\)(2). Let \(\mathcal W\) be an open refinement of order at most \(n+1\). Assign to each \(W\in\mathcal W\) one index \(i(W)\) with \(W\subseteq U_{i(W)}\), and let \(V_i\) be the union of the \(W\) with \(i(W)=i\). Then \(\{V_i\}\) is an open shrinking. A point of \(\bigcap_iV_i\) would lie in \(n+2\) different members of \(\mathcal W\), one assigned to each \(i\).

(2)\(\Rightarrow\)(3). Apply Lemma 1.2(1) to the shrinking \(\{V_i\}\): the closed sets \(\overline{V'_i}\subseteq V_i\) cover \(X\), and their intersection lies in \(\bigcap_iV_i=\varnothing\).

(3)\(\Rightarrow\)(2). Given a closed shrinking \(\{F_i\}\) with empty intersection, Lemma 1.2(2) gives open \(O_i\) with \(F_i\subseteq O_i\subseteq U_i\) and \(\bigcap_iO_i=\varnothing\); they cover \(X\) because the \(F_i\) do.

(2)\(\Rightarrow\)(1) and the last statement are Lemma 2.2: a shrinking is a refinement. \(\square\)

**Corollary 2.4** (Closed subspaces). If \(X\) is normal, \(\dim X\le n\), and \(F\subseteq X\) is closed, then \(\dim F\le n\).

**Proof.** Let \(\{A_1,\dots,A_{n+2}\}\) be a cover of \(F\) by relatively open sets, \(A_i=U_i\cap F\) with \(U_i\) open in \(X\). Then \(\{U_1\cup(X\setminus F),U_2,\dots,U_{n+2}\}\) is an open cover of \(X\). Theorem 2.3(3) gives a closed shrinking \(\{G_i\}\) with empty intersection. The sets \(G_i\cap F\) are closed in \(F\), cover \(F\), lie in \(A_i\) (for \(i=1\) because \(G_1\cap F\subseteq(U_1\cup(X\setminus F))\cap F=A_1\)), and have empty intersection. By Theorem 2.3, applied to the normal space \(F\), \(\dim F\le n\). \(\square\)

## 3. A sum theorem

**Lemma 3.1.** Let \(X\) be normal, \(F\subseteq X\) closed with \(\dim F\le n\), and \(\{W_1,\dots,W_{n+2}\}\) an open cover of \(X\). There is an open cover \(\{W'_1,\dots,W'_{n+2}\}\) with \(\overline{W'_i}\subseteq W_i\) and \(F\cap\bigcap_i\overline{W'_i}=\varnothing\).

**Proof.** By Lemma 1.2(1) there is an open cover \(\{W''_i\}\) with \(\overline{W''_i}\subseteq W_i\). The sets \(W''_i\cap F\) cover \(F\) and are open in \(F\). Theorem 2.3(3), applied to \(F\), gives sets \(E_i\subseteq W''_i\cap F\), closed in \(F\) and hence in \(X\), that cover \(F\) and have empty intersection. Lemma 1.2(2), applied in \(X\), gives open \(O_i\) with \(E_i\subseteq O_i\subseteq\overline{O_i}\subseteq W''_i\) and \(\bigcap_i\overline{O_i}=\varnothing\). Since \(F\subseteq\bigcup_iE_i\subseteq\bigcup_iO_i\), normality gives an open \(P\) with \(F\subseteq P\subseteq\overline P\subseteq\bigcup_iO_i\). Put
\[
W'_i=O_i\cup\bigl(W''_i\setminus\overline P\bigr).
\]
These sets are open. They cover \(X\): a point of \(\overline P\) lies in some \(O_i\), and a point outside \(\overline P\) lies in some \(W''_i\setminus\overline P\). Since \(W'_i\subseteq W''_i\), \(\overline{W'_i}\subseteq W_i\). The closure of \(W''_i\setminus\overline P\) lies in the closed set \(X\setminus P\), so a point of \(F\subseteq P\) that lies in \(\overline{W'_i}\) lies in \(\overline{O_i}\). Hence \(F\cap\bigcap_i\overline{W'_i}\subseteq\bigcap_i\overline{O_i}=\varnothing\). \(\square\)

**Theorem 3.2** (Finite sum theorem). Let \(X\) be normal and \(X=F_1\cup\dots\cup F_m\) with closed \(F_k\) and \(\dim F_k\le n\). Then \(\dim X\le n\).

**Proof.** We verify Theorem 2.3(3). Let \(\{U_1,\dots,U_{n+2}\}\) be an open cover, and put \(U_i^{(0)}=U_i\). For \(k=1,\dots,m\), Lemma 3.1 with \(F=F_k\) gives an open cover \(\{U_i^{(k)}\}\) with \(\overline{U_i^{(k)}}\subseteq U_i^{(k-1)}\) and \(F_k\cap\bigcap_i\overline{U_i^{(k)}}=\varnothing\). The closed sets \(G_i=\overline{U_i^{(m)}}\) lie in \(U_i\) and cover \(X\). For each \(k\), \(G_i\subseteq\overline{U_i^{(k)}}\), so \(F_k\cap\bigcap_iG_i=\varnothing\). As the \(F_k\) cover \(X\), \(\bigcap_iG_i=\varnothing\). \(\square\)

## 4. Cubes

Fix \(\delta>0\) and the lattice \(\delta\mathbb Z^n\). A *face* of the lattice is a set \(\sigma=J_1\times\dots\times J_n\) in which every \(J_i\) is either a point \(\{k_i\delta\}\) or an interval \([k_i\delta,(k_i+1)\delta]\) with \(k_i\in\mathbb Z\); its dimension is the number of intervals among the \(J_i\). Let \(S_j\) be the union of the faces of dimension at most \(j\), and \(S_{-1}=\varnothing\); then \(S_n=\mathbb R^n\), and each \(S_j\) is closed, because every bounded set meets only finitely many faces. Distances are Euclidean.

**Lemma 4.1** (Cubical colouring). Put \(\rho_j=4^{-(j+1)}\delta\) for \(j=0,\dots,n\). For a face \(\sigma\) of dimension \(j\) let
\[
P_\sigma=\{x:d(x,\sigma)<\rho_j\}\ \text{if }j=0,\qquad
P_\sigma=\{x:d(x,\sigma)<\rho_j\ \text{and}\ d(x,S_{j-1})>\tfrac12\rho_{j-1}\}\ \text{if }j\ge1,
\]
and let \(V_j\) be the union of the \(P_\sigma\) over the faces of dimension \(j\). Then each \(P_\sigma\) is open with diameter less than \((\sqrt n+1)\delta\), the sets \(P_\sigma\) with \(\sigma\) of one dimension are pairwise disjoint, and \(V_0\cup\dots\cup V_n=\mathbb R^n\).

**Proof.** *Two facts about faces.* First, if two faces \(\sigma,\sigma'\) are disjoint, then \(d(\sigma,\sigma')\ge\delta\): some coordinate factors \(J_i\) and \(J_i'\) are disjoint, and two disjoint lattice points or intervals are at distance at least \(\delta\). Second, if \(\tau=\sigma\cap\sigma'\) is not empty, then it is the face \(\prod_i(J_i\cap J'_i)\), and
\[
d(x,\tau)\le\sqrt2\,\max\bigl(d(x,\sigma),d(x,\sigma')\bigr).
\tag{4.1}
\]
Indeed, for closed intervals \(I=[a,b]\) and \(I'=[a',b']\) that meet, \(d(t,I)=\max(a-t,0,t-b)\), so \(d(t,I\cap I')=\max(\max(a,a')-t,0,t-\min(b,b'))=\max(d(t,I),d(t,I'))\), and the distance to a product of intervals is computed coordinatewise: \(d(x,\tau)^2=\sum_i\max(d(x_i,J_i),d(x_i,J'_i))^2\le d(x,\sigma)^2+d(x,\sigma')^2\).

*Open and small.* The functions \(d(\cdot,\sigma)\) and \(d(\cdot,S_{j-1})\) are continuous, so \(P_\sigma\) is open. It lies within \(\rho_j\le\delta/4\) of \(\sigma\), whose diameter is at most \(\sqrt n\,\delta\).

*Disjoint.* Let \(\sigma\ne\sigma'\) have dimension \(j\) and \(x\in P_\sigma\cap P_{\sigma'}\). Then \(d(\sigma,\sigma')<2\rho_j\le\delta/2\), so \(\sigma\) and \(\sigma'\) meet, and \(\tau=\sigma\cap\sigma'\) is a face of dimension less than \(j\), because a face of dimension \(j\) contained in both would equal both. For \(j=0\) this is already impossible. For \(j\ge1\), \(\tau\subseteq S_{j-1}\) and (4.1) gives \(d(x,S_{j-1})\le d(x,\tau)<\sqrt2\rho_j=\frac{\sqrt2}4\rho_{j-1}<\frac12\rho_{j-1}\), against \(x\in P_\sigma\).

*Covering.* Let \(x\in\mathbb R^n\), and let \(j\) be the least index with \(d(x,S_j)<\rho_j\); it exists because \(d(x,S_n)=0\). The distance \(d(x,S_j)\) is attained at some face \(\sigma\) of dimension at most \(j\). If \(\dim\sigma<j\), then \(d(x,S_{j-1})\le d(x,\sigma)<\rho_j<\rho_{j-1}\), against the minimality of \(j\). So \(\dim\sigma=j\), and \(d(x,\sigma)<\rho_j\). If \(j\ge1\), minimality also gives \(d(x,S_{j-1})\ge\rho_{j-1}>\frac12\rho_{j-1}\). So \(x\in P_\sigma\subseteq V_j\). \(\square\)

**Theorem 4.2** (Compact subsets of \(\mathbb R^n\)). Every compact \(K\subseteq\mathbb R^n\) has \(\dim K\le n\).

**Proof.** Let \(\{A_1,\dots,A_k\}\) be a cover of \(K\) by relatively open sets, and \(\lambda\) a Lebesgue number for it (Lemma 1.1(2)). Choose \(\delta\) with \((\sqrt n+1)\delta<\lambda\), and take the sets \(P_\sigma\) of Lemma 4.1. The nonempty sets \(P_\sigma\cap K\) are relatively open in \(K\), have diameter less than \(\lambda\), hence each lies in some \(A_i\), and they cover \(K\). A point lies in at most one \(P_\sigma\) for each of the \(n+1\) dimensions of \(\sigma\), so the order is at most \(n+1\). \(\square\)

## 5. Manifolds

**Lemma 5.1** (From bounded order to colours). Let \(L\) be a metric space and \(\{A_1,\dots,A_p\}\) a finite open cover of order at most \(n+1\). There are open sets \(Y_0,\dots,Y_n\) covering \(L\) such that each \(Y_j\) is a union of pairwise disjoint open sets, each contained in some \(A_i\).

**Proof.** If some \(A_i\) equals \(L\), take \(Y_0=A_i\) and \(Y_j=\varnothing\) for \(j\ge1\). Otherwise put \(\varphi_i(x)=d(x,L\setminus A_i)\). These functions are continuous, and \(\varphi_i(x)>0\) exactly when \(x\in A_i\). For a set \(S\) of indices with \(1\le|S|\le n+1\), let
\[
W_S=\{x\in L:\ \varphi_s(x)>0\ \text{and}\ \varphi_s(x)>\varphi_t(x)\ \text{for all }s\in S,\ t\notin S\},
\]
an open set contained in \(A_s\) for every \(s\in S\). If \(S\ne S'\) and \(|S|=|S'|\), there are \(s\in S\setminus S'\) and \(t\in S'\setminus S\), and a point of \(W_S\cap W_{S'}\) would satisfy both \(\varphi_s>\varphi_t\) and \(\varphi_t>\varphi_s\); so these sets are disjoint. For \(x\in L\), the set \(S(x)=\{i:x\in A_i\}\) has between \(1\) and \(n+1\) elements, and \(x\in W_{S(x)}\), because \(\varphi_s(x)>0=\varphi_t(x)\) for \(s\in S(x)\), \(t\notin S(x)\). So \(Y_j=\bigcup_{|S|=j+1}W_S\) does what is required. \(\square\)

**Theorem 5.2** (Colouring a manifold). Let \(M\) be a manifold of dimension \(n\) and \(\mathcal U\) an open cover of \(M\).

1. Every compact subset \(C\) of \(M\) has \(\dim C\le n\).
2. There are \(3(n+1)\) open sets covering \(M\), each a union of pairwise disjoint open sets each contained in some member of \(\mathcal U\).

**Proof.** Fix a metric \(d\) on \(M\) (Section 1).

(1) Every point of \(C\) has a chart around it and inside the chart a compact neighbourhood homeomorphic to a closed ball of \(\mathbb R^n\). Finitely many of these, \(B_1,\dots,B_m\), cover \(C\). Each \(C\cap B_k\) is closed in \(C\) and homeomorphic to a compact subset of \(\mathbb R^n\), so \(\dim(C\cap B_k)\le n\) by Theorem 4.2. The compact metric space \(C\) is normal (Lemma 1.1(1)), and Theorem 3.2 gives \(\dim C\le n\).

(2) *An exhaustion.* \(M\) has a countable base, and the members with compact closure still form a base, since every point has a relatively compact open neighbourhood. Enumerate them as \(B_1,B_2,\dots\). Put \(C_1=\overline{B_1}\) and, given the compact set \(C_k\), choose \(m_k\ge k+1\) with \(C_k\subseteq B_1\cup\dots\cup B_{m_k}\) and put \(C_{k+1}=\overline{B_1\cup\dots\cup B_{m_k}}\). Then the \(C_k\) are compact, \(C_k\subseteq\operatorname{int}C_{k+1}\), and \(\bigcup_kC_k=M\). Put \(C_0=C_{-1}=\varnothing\), and for \(k\ge1\)
\[
L_k=C_k\setminus\operatorname{int}C_{k-1},\qquad O_k=\operatorname{int}C_{k+1}\setminus C_{k-2}.
\]
Each \(L_k\) is compact, the \(L_k\) cover \(M\), \(L_k\subseteq O_k\) (because \(C_{k-2}\subseteq\operatorname{int}C_{k-1}\)), each \(O_k\) is open, and \(O_k\cap O_{k'}=\varnothing\) when \(k'\ge k+3\), because \(O_{k'}\cap C_{k+1}=\varnothing\) and \(O_k\subseteq C_{k+1}\).

*One shell.* Finitely many members \(U_1,\dots,U_q\) of \(\mathcal U\) cover \(L_k\). By (1) and Theorem 2.3, the cover \(\{U_l\cap L_k\}\) of \(L_k\) has a shrinking \(\{A_l\}\) by relatively open sets of order at most \(n+1\). Lemma 5.1 gives relatively open sets \(Y_{k,0},\dots,Y_{k,n}\) of \(L_k\) covering \(L_k\), each \(Y_{k,j}\) a union of pairwise disjoint relatively open sets \(W\), each \(W\) contained in some \(A_l\subseteq U_l\). For each such \(W\), with a chosen \(U_l\supseteq W\), put
\[
\tilde W=\{x\in O_k\cap U_l:\ d(x,W)<d(x,L_k\setminus W)\}.
\]
It is open, contains \(W\) and lies in \(U_l\). For fixed \(k\) and \(j\), the sets \(\tilde W\) are pairwise disjoint, by Lemma 1.1(3) applied to \(L=L_k\).

*Three families of shells.* For \(r\in\{0,1,2\}\) and \(j\in\{0,\dots,n\}\), let \(V_{r,j}\) be the union of the sets \(\tilde W\) for all \(k\equiv r\pmod3\) and all pieces \(W\) of \(Y_{k,j}\). Sets \(\tilde W\) belonging to different \(k\) with \(k\equiv r\pmod 3\) lie in disjoint sets \(O_k\). So each \(V_{r,j}\) is a union of pairwise disjoint open sets, each in a member of \(\mathcal U\). Every point lies in some \(L_k\), hence in some piece \(W\) of some \(Y_{k,j}\), hence in \(\tilde W\). The \(3(n+1)\) sets \(V_{r,j}\) therefore cover \(M\). \(\square\)

**Remark 5.3.** On \(\mathbb R^n\) itself, \(n+1\) colours suffice for every open cover \(\mathcal U\) with a *Lebesgue number*, that is, a number \(\lambda>0\) such that every set of diameter less than \(\lambda\) lies in a member of \(\mathcal U\). Indeed, choose \(\delta\) with \((\sqrt n+1)\delta<\lambda\): the \(n+1\) sets \(V_j\) of Lemma 4.1 cover \(\mathbb R^n\), and each is a disjoint union of open sets \(P_\sigma\) of diameter less than \(\lambda\), each contained in a member of \(\mathcal U\). In Theorem 5.2 the factor \(3\) comes from combining the compact shells three at a time.

## 6. Vector bundles

Vector bundles here are real or complex, continuous or smooth, of constant rank \(r\). A bundle \(E\to M\) is *trivial over* an open set \(V\) if \(E|_V\cong V\times\mathbb K^r\), with \(\mathbb K=\mathbb R\) or \(\mathbb C\).

**Lemma 6.1.** If \(V\) is a union of pairwise disjoint open sets \(V_s\) and \(E\) is trivial over each \(V_s\), then \(E\) is trivial over \(V\).

**Proof.** Choose isomorphisms \(\psi_s:E|_{V_s}\to V_s\times\mathbb K^r\) and let \(\psi\) be \(\psi_s\) over \(V_s\). Each point of \(V\) has an open neighbourhood, namely its \(V_s\), on which \(\psi\) and \(\psi^{-1}\) agree with continuous (or smooth) maps. So \(\psi\) is an isomorphism \(E|_V\to V\times\mathbb K^r\). \(\square\)

**Corollary 6.2** (Finite trivializing covers). Every vector bundle over a manifold of dimension \(n\) is trivial over each of \(3(n+1)\) open sets that cover the manifold.

**Proof.** Apply Theorem 5.2(2) to the cover by open sets over which the bundle is trivial, and Lemma 6.1 to each of the \(3(n+1)\) sets. \(\square\)

**Corollary 6.3** (Stable complements). Let \(E\) be a smooth vector bundle of rank \(r\) over a smooth manifold \(M\) of dimension \(n\). There is a smooth vector bundle \(G\) over \(M\) with \(E\oplus G\cong M\times\mathbb K^N\), where \(N=3(n+1)r\).

**Proof.** By Corollary 6.2 the hypothesis of [The Bott operator, suspension, and reduction of the index to Euclidean space, Lemma 12.5](the-bott-operator-suspension-and-reduction-of-the-index-to-euclidean-space.md#AN-FND-BO-12) holds with \(J=3(n+1)\) open sets. \(\square\)

**Example 6.4** (Colours on the line). Let \(M=\mathbb R\) and let \(\mathcal U\) consist of the intervals \(I_k=(k-1,k+1)\), \(k\in\mathbb Z\). The intervals \(I_k\) with \(k\) even are pairwise disjoint, and so are those with \(k\) odd. Every point lies in an interval of each parity, except the integers, which lie only in \(I_k\) for \(k\) equal to the integer. So the two sets \(V_{\mathrm{even}}=\bigcup_{k\text{ even}}I_k\) and \(V_{\mathrm{odd}}=\bigcup_{k\text{ odd}}I_k\) cover \(\mathbb R\), each a disjoint union of members of \(\mathcal U\): here \(n+1=2\) colours suffice. Remark 5.3 predicts this, because \(1\) is a Lebesgue number of \(\mathcal U\): a set \(S\) of diameter less than \(1\) lies in \([a,b]\) with \(b-a<1\), the open interval \((b-1,a+1)\) has length greater than \(1\) and so contains an integer \(k\), and then \(S\subseteq(k-1,k+1)=I_k\).

## 7. Exercises

**Exercise 7.1.** Show that \(\dim\{0,1,\dots,m\}\le0\) for a finite discrete space, and that \(\dim[0,1]\le1\) directly: refine a finite open cover by intervals of length less than a Lebesgue number, arranged so that each point lies in at most two.

*Solution.* In a finite discrete space the singletons are open and form a refinement of every cover, of order \(1\). For \([0,1]\), let \(\lambda\) be a Lebesgue number and \(m>3/\lambda\); the relatively open intervals \(\big((i-1)/m,(i+1)/m\big)\cap[0,1]\), \(i=0,\dots,m\), have length at most \(2/m<\lambda\), so each lies in a member of the cover, they cover \([0,1]\), and every point lies in at most two of them.

**Exercise 7.2.** Let \(X=F_1\cup F_2\), where \(F_1=[0,1]\times\{0\}\) and \(F_2=\{0\}\times[0,1]\) in \(\mathbb R^2\). Use Theorem 3.2 and Exercise 7.1 to show \(\dim X\le1\).

*Solution.* Both \(F_k\) are closed and homeomorphic to \([0,1]\), so \(\dim F_k\le1\); \(X\) is a compact metric space, hence normal, and Theorem 3.2 applies.

**Exercise 7.3.** (a) In Lemma 5.1, show that \(W_S\) is empty unless \(\bigcap_{s\in S}A_s\ne\varnothing\). (b) Take \(L=[0,1]\), \(n=1\), \(A_1=[0,\tfrac23)\) and \(A_2=(\tfrac13,1]\). Compute the sets \(W_S\) and the colours \(Y_0,Y_1\) of Lemma 5.1.

*Solution.* (a) By definition \(W_S\subseteq A_s\) for every \(s\in S\). (b) Neither set is all of \(L\), and \(\varphi_1(x)=d(x,[\tfrac23,1])=\max(\tfrac23-x,0)\), \(\varphi_2(x)=d(x,[0,\tfrac13])=\max(x-\tfrac13,0)\). For \(x\le\frac13\) we have \(\varphi_1(x)>0=\varphi_2(x)\); for \(\frac13<x<\frac23\), \(\varphi_1(x)>\varphi_2(x)\) exactly when \(x<\frac12\); for \(x\ge\frac23\), \(\varphi_1(x)=0\). So \(W_{\{1\}}=[0,\tfrac12)\) and, symmetrically, \(W_{\{2\}}=(\tfrac12,1]\), while \(W_{\{1,2\}}=\{x:\varphi_1(x)>0,\ \varphi_2(x)>0\}=(\tfrac13,\tfrac23)\). Hence \(Y_0=[0,\tfrac12)\cup(\tfrac12,1]\), a union of two disjoint sets, and \(Y_1=(\tfrac13,\tfrac23)\); together they cover \([0,1]\).

## Where this leads

Corollary 6.3 removes the compactness assumption from the stable complements of the lesson on the Bott operator: every smooth vector bundle over a manifold is a direct summand of a trivial bundle of rank \(3(n+1)r\). The next lesson, Lebesgue's covering theorem and the dimension of cubes, proves the reverse inequality for cubes, \(\dim[0,1]^n=n\), and the invariance of dimension. Dimension theory goes much further.

## References

- [Lebesgue 1911] H. Lebesgue, Sur la non-applicabilité de deux domaines appartenant respectivement à des espaces à \(n\) et \(n+p\) dimensions, *Mathematische Annalen* 70 (1911), 166–168; free scan at the [Göttingen digitization centre](https://resolver.sub.uni-goettingen.de/purl?GDZPPN002263718).
- [Ostrand 1971]. A. Ostrand, Covering dimension in general spaces, *General Topology and its Applications* 1 (1971), 209–221, [doi:10.1016/0016-660X(71)90093-6](https://doi.org/10.1016/0016-660X(71)90093-6) (free to read in the publisher's open archive). Free at https://linkinghub.elsevier.com/retrieve/pii/0016660X71900936
