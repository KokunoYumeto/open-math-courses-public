# Sheaf cohomology and singular cohomology on manifolds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a manifold, the cohomology of a constant sheaf is singular cohomology. The comparison runs through the sheaf of singular cochains: it resolves the constant sheaf, its sections compute singular cohomology, and its terms are flasque. The same resolution identifies cohomology with supports in a closed set with relative singular cohomology, and compactly supported sheaf cohomology with the compactly supported singular cohomology of the previous lessons. Finally, for a manifold embedded as an open subset of a compact Hausdorff space, the cohomology of the extension by zero of a sheaf is its compactly supported cohomology. Together with Poincaré duality these facts give duality and dimension statements for the sheaf cohomology of manifolds, in the form used in étale cohomology. The last section matches connecting maps of sheaf sequences with singular ones and computes the class of the coordinate function of the punctured plane under the exponential and Kummer sequences, including its sign.

We use [Orientations and fundamental classes](orientations-and-fundamental-classes.md), [Cap products and cohomology with compact supports](cap-products-and-cohomology-with-compact-supports.md) and [Poincaré duality](poincare-duality.md). From the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) we use the homotopy invariance of singular cochains [Roberts, Theorem 13], the long exact sequence of a pair [Roberts, Proposition 24] and small cochains [Roberts, Proposition 26]. From the course on derived categories of sheaves we use: in [Injective modules and bounded-below derived functors](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors), Lemma 1.1 (injective sheaves are flasque, and restrict to injective sheaves on open subsets), Proposition 1.3 (flasque sheaves have no higher cohomology) and Theorem 4.1(4) (a bounded-below resolution by acyclic objects computes a left exact functor's derived functor); in [Sections with support and the localization triangle](course:derived-categories-and-sheaf-operations/sections-with-support-and-the-localization-triangle), sections with support in a closed set (Section 1) and the localization sequence (2.2) of Theorem 2.1. For open subsets of \(\mathbf R^n\), Lemma 4.1 of that lesson proves the comparison of Section 1 by the same resolution. Section 6 also uses Lemma 3.2 and Theorem 3.3 of the first of these lessons (maps from a resolution into a bounded-below complex of injectives), the horseshoe lemma [Resolutions, Tor and Ext, Lemma 4.1](course:AG-CA/resolutions-tor-and-ext), holomorphic logarithms and roots on simply connected domains [Lebl, Corollaries 4.3.4 and 4.3.5], and Exercise 6.2 and Corollary 3.5 of [Orientations and fundamental classes](orientations-and-fundamental-classes.md). From the [AI Integrated Stacks Project, *Cohomology of Sheaves*](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cohomology-of-closed) we use: for a quasi-compact subset \(Z\) of a space \(X\) any two of whose points have disjoint neighbourhoods in \(X\), and an abelian sheaf \(G\) on \(X\), the map \(\varinjlim_UH^p(U,G)\to H^p(Z,G|_Z)\), over the open neighbourhoods \(U\) of \(Z\), is an isomorphism.

Sheaves are sheaves of abelian groups, and \(A\) denotes an abelian group; \(A_X\) is the constant sheaf.

## 1. The sheaf of singular cochains

Let \(X\) be a space. For open \(W\subset X\) let \(C^q(W;A)\) be the singular cochains of \(W\); restriction of cochains to simplices in a smaller open set makes \(W\mapsto C^q(W;A)\) a presheaf, compatible with the coboundary. Let \(\mathcal C^q\) be its sheafification, \(\delta:\mathcal C^q\to\mathcal C^{q+1}\) the induced coboundary, and \(A_X\to\mathcal C^0\) the map sending a locally constant function to the corresponding \(0\)-cochains. A cochain \(c\in C^q(W;A)\) is **locally zero** if every point of \(W\) has a neighbourhood \(O\subset W\) such that \(c(\sigma)=0\) for every simplex \(\sigma\) in \(O\). The locally zero cochains form a subgroup \(N^q(W)\), and \(\delta N^q(W)\subset N^{q+1}(W)\), since the faces of a simplex in \(O\) lie in \(O\).

**Lemma 1.1.** For every space \(W\), the complex \(N^\bullet(W)\) is acyclic.

**Proof.** For an open cover \(\mathcal U\) of \(W\), let \(N_{\mathcal U}\) be the cochains vanishing on every simplex contained in a member of \(\mathcal U\). It is the kernel of the restriction from all cochains to cochains on such small simplices, which is surjective (extend by zero) and a quasi-isomorphism [Roberts, Proposition 26]; by the long exact sequence, \(N_{\mathcal U}\) is acyclic. A cochain is locally zero exactly when it lies in \(N_{\mathcal U}\) for some cover \(\mathcal U\); if \(\mathcal U'\) refines \(\mathcal U\), then \(N_{\mathcal U}\subset N_{\mathcal U'}\); and two covers have a common refinement. So \(N^\bullet(W)\) is a directed union of acyclic complexes, hence acyclic. \(\square\)

**Lemma 1.2.** Let \(W\) be a manifold and \((W_a)\) an open cover of \(W\). There is a countable, locally finite open cover \((V_b)\) of \(W\) such that the closure of each \(V_b\) in \(W\) is compact and contained in some \(W_{a(b)}\).

**Proof.** \(W\) is the union of the interiors of countably many compact sets \(L_1,L_2,\ldots\), for instance closures of chart balls from a countable basis. Put \(K_1=L_1\) and let \(K_{m+1}\) be a finite union of sets \(L_i\) whose interiors cover \(K_m\cup L_{m+1}\). Then \(K_m\subset\operatorname{int}K_{m+1}\) and \(\bigcup_mK_m=W\); put \(K_0=K_{-1}=\emptyset\). For each \(m\geq1\), each point of the compact set \(K_m\setminus\operatorname{int}K_{m-1}\) has an open neighbourhood with compact closure contained in some \(W_a\) and in \(\operatorname{int}K_{m+1}\setminus K_{m-2}\); finitely many of these cover the set. All these neighbourhoods, for all \(m\), form the cover \((V_b)\). A point of \(\operatorname{int}K_p\) has the neighbourhood \(\operatorname{int}K_p\), which meets the sets of layer \(m\) only for \(m\leq p+1\), finitely many in all. \(\square\)

**Theorem 1.3.** Let \(M\) be a manifold and \(W\subset M\) open.

1. The augmented complex \(0\to A_M\to\mathcal C^0\to\mathcal C^1\to\cdots\) is exact, and each \(\mathcal C^q\) is flasque.
2. The map \(C^q(W;A)\to\Gamma(W,\mathcal C^q)\) is surjective, with kernel \(N^q(W)\); hence \(C^\bullet(W;A)\to\Gamma(W,\mathcal C^\bullet)\) is a quasi-isomorphism.
3. There are isomorphisms \(H^q(W,A_W)\cong H^q(W;A)\) between sheaf cohomology and singular cohomology, natural with respect to restriction to smaller open sets and with respect to homomorphisms of coefficient groups.

**Proof.** *Stalks.* The stalk of \(\mathcal C^\bullet\) at \(x\) is the direct limit of \(C^\bullet(O;A)\) over the open neighbourhoods \(O\) of \(x\), and the chart balls about \(x\) are cofinal among them. A chart ball is contractible, so by homotopy invariance [Roberts, Theorem 13] its singular cochain complex has the cohomology of a point: \(A\), spanned by the constant cochains, in degree \(0\), and zero in positive degrees. (For a point, the \(q\)-simplex is unique, the coboundary \(C^{q-1}\to C^q\) is the identity for even \(q\geq2\) and zero for odd \(q\).) Direct limits are exact, so the augmented stalk complex \(A\to\mathcal C^\bullet_x\) is exact.

*Surjectivity in (2).* A section \(s\in\Gamma(W,\mathcal C^q)\) is given by an open cover \((W_a)\) of \(W\) and cochains \(c_a\in C^q(W_a;A)\) whose germ at every point \(y\in W_a\) is \(s_y\). Choose \((V_b)\) as in Lemma 1.2 and enumerate it. For a simplex \(\sigma\) of \(W\) contained in some \(V_b\), let \(b(\sigma)\) be the first such index and put \(c(\sigma)=c_{a(b(\sigma))}(\sigma)\); put \(c(\sigma)=0\) if \(\sigma\) lies in no \(V_b\). We show that the germ of \(c\) at every \(x\in W\) is \(s_x\). Let \(O\) be a neighbourhood of \(x\) meeting only finitely many \(V_b\), and shrink it to avoid the closures of those that do not contain \(x\) in their closure; let \(F\) be the finite set of the remaining indices. For \(b\in F\), \(x\) lies in \(\overline{V_b}\subset W_{a(b)}\), so all the cochains \(c_{a(b)}\), \(b\in F\), are defined near \(x\) and have the germ \(s_x\) there; choose a neighbourhood \(O''\) of \(x\) on whose simplices they all agree. Choose \(b_0\) with \(x\in V_{b_0}\); then \(b_0\in F\). Put \(O'=O\cap O''\cap V_{b_0}\). A simplex \(\sigma\) in \(O'\) lies in \(V_{b_0}\), so \(b(\sigma)\) is defined, and \(V_{b(\sigma)}\) meets \(O\), so \(b(\sigma)\in F\); hence \(c(\sigma)=c_{a(b(\sigma))}(\sigma)=c_{a(b_0)}(\sigma)\). So \(c\) agrees with \(c_{a(b_0)}\) near \(x\), and its germ is \(s_x\).

*Kernel, flasqueness, quasi-isomorphism.* A cochain maps to zero in \(\Gamma(W,\mathcal C^q)\) exactly when all its germs vanish, that is, when it is locally zero. If \(W'\subset W\) is open and \(t\in\Gamma(W',\mathcal C^q)\), lift \(t\) to a cochain on \(W'\) by surjectivity for \(W'\), extend it by zero to the simplices of \(W\) not in \(W'\), and map it to \(\Gamma(W,\mathcal C^q)\): the result restricts to \(t\). So \(\mathcal C^q\) is flasque. The short exact sequence \(0\to N^\bullet(W)\to C^\bullet(W;A)\to\Gamma(W,\mathcal C^\bullet)\to0\) and Lemma 1.1 give the quasi-isomorphism.

*(3).* The restriction of \(\mathcal C^\bullet\) to \(W\) is a resolution of \(A_W\) by flasque sheaves, which have no higher cohomology [Injective modules and bounded-below derived functors, Proposition 1.3]. By Theorem 4.1(4) there, \(\Gamma(W,\mathcal C^\bullet)\) computes \(H^q(W,A_W)\); combine with (2). All maps used are restrictions or are induced by the coefficient homomorphism, which gives the naturality. \(\square\)

## 2. Supports in a closed set

For a closed set \(Z\subset M\) and a sheaf \(F\), let \(\Gamma_Z(M,F)\) be the sections of \(F\) over \(M\) with support in \(Z\), and \(H^q_Z(M,F)\) its derived functors.

**Lemma 2.1.** If \(F\) is flasque, then \(0\to\Gamma_Z(M,F)\to\Gamma(M,F)\to\Gamma(M\setminus Z,F)\to0\) is exact and \(H^q_Z(M,F)=0\) for \(q>0\).

**Proof.** A section vanishing on \(M\setminus Z\) is exactly a section supported in \(Z\), and restriction is surjective because \(F\) is flasque. The localization sequence (2.2) gives the exact sequence
\[
0\to H^0_Z(M,F)\to H^0(M,F)\to H^0(M\setminus Z,F)\to H^1_Z(M,F)\to H^1(M,F)\to\cdots .
\]
Restrictions of flasque sheaves are flasque, so \(H^q(M,F)=H^q(M\setminus Z,F)=0\) for \(q>0\). Hence \(H^1_Z(M,F)\) is the cokernel of the surjective restriction, which is zero, and \(H^q_Z(M,F)\) lies between \(H^{q-1}(M\setminus Z,F)=0\) and \(H^q(M,F)=0\) for \(q\geq2\). \(\square\)

**Theorem 2.2.** For a closed set \(Z\subset M\), the map \(C^\bullet(M,M\setminus Z;A)\to\Gamma_Z(M,\mathcal C^\bullet)\) induced by Theorem 1.3(2) is a quasi-isomorphism, and
\[
H^q_Z(M,A_M)\cong H^q(M,M\setminus Z;A).
\]
These isomorphisms are natural in \(Z\) (for \(Z\subset Z'\)) and in \(A\), and compatible with the maps \(H^q_Z(M,A_M)\to H^q(M,A_M)\) and \(H^q(M,M\setminus Z;A)\to H^q(M;A)\), and with the connecting maps \(H^q(M\setminus Z,A_M)\to H^{q+1}_Z(M,A_M)\) of the localization sequence and \(H^q(M\setminus Z;A)\to H^{q+1}(M,M\setminus Z;A)\) of the pair.

**Proof.** A cochain vanishing on all simplices in the open set \(M\setminus Z\) has zero germ at every point of \(M\setminus Z\), so its section is supported in \(Z\). This gives a map from the short exact sequence of the pair,
\[
0\to C^\bullet(M,M\setminus Z;A)\to C^\bullet(M;A)\to C^\bullet(M\setminus Z;A)\to0,
\]
to the sequence \(0\to\Gamma_Z(M,\mathcal C^\bullet)\to\Gamma(M,\mathcal C^\bullet)\to\Gamma(M\setminus Z,\mathcal C^\bullet)\to0\), which is exact by Lemma 2.1. The middle and right maps are quasi-isomorphisms by Theorem 1.3(2), so the five lemma, applied to the long exact sequences, shows that the left map is one. By Lemma 2.1 the flasque resolution \(\mathcal C^\bullet\) consists of \(\Gamma_Z\)-acyclic sheaves, so by [Injective modules and bounded-below derived functors, Theorem 4.1(4)] \(\Gamma_Z(M,\mathcal C^\bullet)\) computes \(H^q_Z(M,A_M)\). The maps used are inclusions and restrictions, which gives the naturality and compatibility. A map of short exact sequences of complexes commutes with their connecting maps. Finally, the localization sequence (2.2) may be computed with \(\mathcal C^\bullet\): choose an injective resolution \(A_M\to I^\bullet\); by Lemma 3.2 and Theorem 3.3 of [Injective modules and bounded-below derived functors](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors) there is a map of complexes \(\mathcal C^\bullet\to I^\bullet\) compatible with the augmentations. It maps the exact sequence of Lemma 2.1 for \(\mathcal C^\bullet\) to that for \(I^\bullet\), and induces isomorphisms on the cohomology of all three terms, since both resolutions compute the three derived functors. \(\square\)

## 3. Compact supports

For a sheaf \(F\) on \(M\), let \(\Gamma_c(M,F)\) be the sections with compact support and \(H^q_c(M,F)\) its derived functors.

**Proposition 3.1.** \(H^q_c(M,F)\cong\varinjlim_KH^q_K(M,F)\), the direct limit over the compact subsets \(K\subset M\).

**Proof.** The support of a section is closed, so a section has compact support exactly when it is supported in some compact \(K\); thus \(\Gamma_c(M,-)=\varinjlim_K\Gamma_K(M,-)\), a directed union. Apply this to an injective resolution of \(F\) and use that direct limits are exact. \(\square\)

**Corollary 3.2.** There are isomorphisms \(H^q_c(M,A_M)\cong H^q_c(M;A)\), the right side being the compactly supported singular cohomology \(\varinjlim_KH^q(M,M\setminus K;A)\), natural in \(A\).

**Proof.** Combine Proposition 3.1 with Theorem 2.2 for compact \(K\), using its naturality in \(K\). \(\square\)

## 4. Open embeddings into compact spaces

**Theorem 4.1.** Let \(j:M\to T\) be an open embedding of a manifold into a compact Hausdorff space. For every sheaf \(F\) on \(M\),
\[
H^q(T,j_!F)\cong H^q_c(M,F);
\]
in particular \(H^q(T,j_!A_M)\cong H^q_c(M;A)\).

**Proof.** Put \(Z=T\setminus M\), a compact set, and \(G=j_!F\), so that \(G|_M=F\) and \(G|_Z=0\).

*Excision for supports.* Let \(K\subset M\) be compact; it is closed in \(T\). A section of a sheaf \(G'\) on \(T\) supported in \(K\) is determined by its restriction to \(M\), and a section on \(M\) supported in \(K\) extends by zero across \(T\setminus K\). So \(\Gamma_K(T,G')=\Gamma_K(M,G'|_M)\). Injective sheaves on \(T\) restrict to injective sheaves on \(M\) [Injective modules and bounded-below derived functors, Lemma 1.1], so the derived functors agree: \(H^q_K(T,G)\cong H^q_K(M,F)\), naturally in \(K\).

*The limit.* The localization sequence (2.2) for the closed set \(K\subset T\) reads
\[
\cdots\to H^q_K(T,G)\to H^q(T,G)\to H^q(T\setminus K,G)\to H^{q+1}_K(T,G)\to\cdots .
\]
Pass to the direct limit over the compact sets \(K\subset M\); it is exact. The open sets \(T\setminus K\) are cofinal among the open neighbourhoods of \(Z\): if \(U\supset Z\) is open, then \(T\setminus U\) is compact and contained in \(M\). By the Stacks lemma recalled above, \(\varinjlim_KH^q(T\setminus K,G)=H^q(Z,G|_Z)=0\), since \(T\) is Hausdorff and \(Z\) is compact. Hence \(\varinjlim_KH^q_K(T,G)\to H^q(T,G)\) is an isomorphism, and by excision and Proposition 3.1 the left side is \(H^q_c(M,F)\). The last assertion follows from Corollary 3.2. \(\square\)

## 5. Duality and dimension for sheaf cohomology

**Corollary 5.1 (dimension).** For an \(n\)-manifold \(M\) and every abelian group \(A\), \(H^q(M,A_M)=0\) for \(q>n\).

**Proof.** Theorem 1.3(3) and [Poincaré duality, Corollary 2.4](poincare-duality.md#2-consequences). \(\square\)

**Corollary 5.2 (duality).** Let \(\Lambda\) be a commutative ring that is injective as a module over itself, for example \(\mathbf Z/m\), and let \(M\) be a \(\Lambda\)-oriented \(n\)-manifold, for example a complex manifold of complex dimension \(n/2\) with its canonical orientation.

1. \(H^q(M,\Lambda_M)\cong\operatorname{Hom}_\Lambda\bigl(H^{n-q}_c(M,\Lambda_M),\Lambda\bigr)\) for every \(q\).
2. If \(M\) is connected, \(H^n_c(M,\Lambda_M)\cong\Lambda\).
3. For \(\Lambda=\mathbf Z/m\): if \(H^{n-q}_c(M,\Lambda_M)\) is finite, then \(H^q(M,\Lambda_M)\) is finite of the same order.
4. If \(j:M\to T\) is an open embedding into a compact Hausdorff space, \(H^{n-q}_c(M,\Lambda_M)\) may be replaced by \(H^{n-q}(T,j_!\Lambda_M)\) in (1)–(3).

**Proof.** Translate [Poincaré duality, Corollary 2.3](poincare-duality.md#2-consequences) by Theorem 1.3(3) and Corollary 3.2, which gives (1) and (3). For (2), Poincaré duality gives \(H^n_c(M;\Lambda)\cong H_0(M;\Lambda)\cong\Lambda\) for connected \(M\). Theorem 4.1 gives (4). Complex manifolds are canonically oriented by [Orientations and fundamental classes, Corollary 3.5](orientations-and-fundamental-classes.md#3-orientations-from-charts). \(\square\)

## 6. Connecting maps and the exponential sequence

Every connecting map in this section is formed in the same way. For a short exact sequence \(0\to K'\to K\to K''\to0\) of cochain complexes, the connecting map sends the class of a cocycle \(z''\) of \(K''\) to the class of the cocycle \(z'\) of \(K'\) whose image is \(dz\), where \(z\in K\) is any lift of \(z''\). Singular coboundaries are \(\delta\varphi=\varphi\circ\partial\). For a short exact sequence of sheaves \(0\to A\to B\to C\to0\), choose injective resolutions of \(A\) and \(C\) and form the resolution of \(B\) given by the horseshoe lemma, [Resolutions, Tor and Ext, Lemma 4.1](course:AG-CA/resolutions-tor-and-ext) in its dual form for injective resolutions, which has the same proof. The result is a short exact sequence of injective resolutions that is split in each degree, so its sections over every open set form a short exact sequence of complexes; the cohomology sequence of these complexes over \(M\) is the long exact sequence of the derived functors [Injective modules and bounded-below derived functors, Theorem 4.1(4)].

**Proposition 6.1 (Mayer–Vietoris).** Let \(M=U\cup V\) with \(U,V\) open. For a flasque sheaf \(I\) the sequence

\[
0\to\Gamma(M,I)\to\Gamma(U,I)\oplus\Gamma(V,I)\to\Gamma(U\cap V,I)\to0,\qquad s\mapsto(s|_U,s|_V),\quad(s,t)\mapsto t|_{U\cap V}-s|_{U\cap V},
\]

is exact. For a sheaf \(F\) with a flasque resolution \(F\to I^\bullet\), the cohomology sequence of these sequences is a long exact sequence

\[
\cdots\to H^q(M,F)\to H^q(U,F)\oplus H^q(V,F)\to H^q(U\cap V,F)\xrightarrow{\ \delta_{MV}\ }H^{q+1}(M,F)\to\cdots,
\]

the **Mayer–Vietoris sequence**, which does not depend on the flasque resolution. For \(F=A_M\) the isomorphisms of Theorem 1.3(3) carry it to the Mayer–Vietoris sequence of singular cohomology formed with the same maps on cochains, connecting maps included.

**Proof.** Exactness on the left and in the middle is the sheaf property. Given \(t\in\Gamma(U\cap V,I)\), extend it to \(\tilde t\in\Gamma(V,I)\), since \(I\) is flasque; then \((0,\tilde t)\) maps to \(t\). Restrictions of flasque sheaves are flasque, so \(I^\bullet\) computes the cohomology of \(F\) on all four open sets. For a second flasque resolution, compare both with an injective resolution \(F\to J^\bullet\): by Lemma 3.2 and Theorem 3.3 of [Injective modules and bounded-below derived functors](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors) there are maps of complexes \(I^\bullet\to J^\bullet\) compatible with the augmentations; they map one family of short exact sequences to the other and induce isomorphisms on the cohomology over each open set, so they identify the long exact sequences. For \(F=A_M\), let \(C^\bullet_{\mathcal U}(M;A)\) be the cochains on the simplices contained in \(U\) or in \(V\). Such a cochain defines sections of \(\mathcal C^\bullet\) over \(U\) and over \(V\) that agree on \(U\cap V\), hence a section over \(M\). This gives a map of short exact sequences from

\[
0\to C^\bullet_{\mathcal U}(M;A)\to C^\bullet(U;A)\oplus C^\bullet(V;A)\to C^\bullet(U\cap V;A)\to0
\]

to the sequence above for \(I=\mathcal C^\bullet\). Its components on \(U\), \(V\) and \(U\cap V\) are quasi-isomorphisms by Theorem 1.3(2), hence so is the first by the five lemma, and the restriction \(C^\bullet(M;A)\to C^\bullet_{\mathcal U}(M;A)\) is a quasi-isomorphism [Roberts, Proposition 26]. The cohomology sequence of the displayed sequence is the singular Mayer–Vietoris sequence, and a map of short exact sequences commutes with the connecting maps. \(\square\)

**Lemma 6.2 (connecting maps from local lifts).** Let \(0\to A_M\xrightarrow{i}B\xrightarrow{p}C\to0\) be an exact sequence of sheaves on \(M\) with \(A_M\) constant, let \(M=U\cup V\) be an open cover, \(c\in\Gamma(M,C)\), and let \(b_U\in\Gamma(U,B)\), \(b_V\in\Gamma(V,B)\) satisfy \(p(b_U)=c|_U\) and \(p(b_V)=c|_V\). Then \(b_U-b_V\) on \(U\cap V\) is \(i(g)\) for a locally constant function \(g:U\cap V\to A\), and the connecting map \(\delta:\Gamma(M,C)\to H^1(M,A_M)\) of the sequence satisfies

\[
\delta(c)=\delta_{MV}(g).
\]

**Proof.** Since \(p(b_U-b_V)=0\) on \(U\cap V\), the section \(g\) exists. Take the degreewise split sequence of injective resolutions \(0\to I_A^\bullet\to I_B^\bullet\to I_C^\bullet\to0\) described above, and regard sections of \(A_M\), \(B\), \(C\) as \(0\)-cocycles through the augmentations. Lift \(c\) to \(x\in\Gamma(M,I_B^0)\); then \(dx\) is the image of a cocycle \(y\in\Gamma(M,I_A^1)\), and \(\delta(c)=[y]\). On \(U\), \(x|_U-b_U\) maps to zero in \(I_C^0\), so it is the image of some \(p_U\in\Gamma(U,I_A^0)\), and \(dp_U=y|_U\) because \(db_U=0\). Likewise \(x|_V-b_V\) is the image of \(p_V\in\Gamma(V,I_A^0)\) with \(dp_V=y|_V\). On \(U\cap V\), \(p_V-p_U=b_U-b_V=g\). So \((p_U,p_V)\) lifts \(g\) in the sequence of Proposition 6.1 for \(I_A^\bullet\), and its coboundary \((y|_U,y|_V)\) is the image of \(y\). By definition \(\delta_{MV}(g)=[y]\). \(\square\)

**Proposition 6.3 (the exponential sequence and the winding number).** Let \(\mathcal O\) be the sheaf of holomorphic functions on \(M=\mathbf C\setminus\{0\}\), and

\[
0\to\mathbf Z\to\mathcal O\xrightarrow{\ e\ }\mathcal O^*\to1,\qquad e(f)=\exp(2\pi if),
\]

the exponential sequence. Let \(\delta(z)\in H^1(M,\mathbf Z)\cong H^1(M;\mathbf Z)\) be the image of the coordinate function \(z\) under its connecting map and Theorem 1.3(3), and let \(\gamma(s)=e^{2\pi is}\), \(0\leq s\leq1\), be the counterclockwise unit circle. Then

\[
\langle\delta(z),[\gamma]\rangle=-1 .
\]

**Proof.** The sequence is exact: the kernel of \(e\) consists of the locally constant integer functions, and \(e\) is surjective on stalks because a nowhere zero holomorphic function on a disc has a holomorphic logarithm [Lebl, Corollary 4.3.4]. Let \(U=M\setminus(-\infty,0)\) and \(V=M\setminus(0,\infty)\). Both are simply connected (star-shaped about \(1\) and \(-1\)), so \(z\) has holomorphic logarithms \(L_U\) on \(U\) and \(L_V\) on \(V\) [Lebl, Corollary 4.3.4], normalized by \(L_U(1)=0\) and \(L_V(-1)=i\pi\). Their imaginary parts are continuous arguments on the connected sets \(U\) and \(V\); two continuous arguments on a connected set differ by a constant multiple of \(2\pi\), so \(\operatorname{Im}L_U\) takes values in \((-\pi,\pi)\) and \(\operatorname{Im}L_V\) in \((0,2\pi)\). Put \(b_U=L_U/2\pi i\) and \(b_V=L_V/2\pi i\), so that \(e(b_U)=z\) and \(e(b_V)=z\). The intersection \(U\cap V\) is the union of the open upper and lower half planes \(H_+\) and \(H_-\). On \(H_+\) the two arguments agree; on \(H_-\), \(\operatorname{Im}L_V=\operatorname{Im}L_U+2\pi\). Hence \(g=b_U-b_V\) is \(0\) on \(H_+\) and \(-1\) on \(H_-\), and \(\delta(z)=\delta_{MV}(g)\) by Lemma 6.2.

By Proposition 6.1 we compute \(\delta_{MV}(g)\) with singular cochains. The pair \((0,q)\in C^0(U;\mathbf Z)\oplus C^0(V;\mathbf Z)\), where \(q\) is \(g\) on \(U\cap V\) and \(0\) on the negative real axis, lifts \(g\). So \(\delta_{MV}(g)\) is represented by the cocycle on small simplices that is \(\delta0=0\) on simplices in \(U\) and \(\delta q\) on simplices in \(V\). The loop \(\gamma\) is homologous to \(\gamma_1+\gamma_2+\gamma_3\), the restrictions of \(\gamma\) to \([0,\tfrac14]\), \([\tfrac14,\tfrac34]\), \([\tfrac34,1]\), reparametrized (as in the solution of Exercise 6.2 of [Orientations and fundamental classes](orientations-and-fundamental-classes.md#6-exercises)). Here \(\gamma_1\) and \(\gamma_3\) lie in \(U\), and \(\gamma_2\), which runs from \(i\) through \(-1\) to \(-i\), lies in \(V\). Therefore \(\langle\delta(z),[\gamma]\rangle=(\delta q)(\gamma_2)=q(-i)-q(i)=-1\). \(\square\)

So the connecting map is the negative of the monodromy: continuing \(\log z/2\pi i\) once counterclockwise around \(\gamma\) increases it by \(1\).

**Corollary 6.4 (the Kummer class of \(z\)).** Let \(n\geq1\), let \(\mu_n\subset\mathbf C^*\) be the group of \(n\)-th roots of unity, and let \(\kappa(z)\in H^1(\mathbf C\setminus\{0\},\mu_n)\) be the image of \(z\) under the connecting map of the Kummer sequence \(1\to\mu_n\to\mathcal O^*\xrightarrow{f\mapsto f^n}\mathcal O^*\to1\). Identify the singular groups with \(\mu_n\) coefficients with \(\operatorname{Hom}(H_1(\mathbf C\setminus\{0\}),\mu_n)\) and \(\operatorname{Hom}(H_2(\mathbf C,\mathbf C\setminus\{0\}),\mu_n)\) by the universal coefficient sequence (the homology groups below these degrees are free). Then:

1. \(\langle\kappa(z),[\gamma]\rangle=e^{-2\pi i/n}\);
2. the connecting map \(\partial:H^1(\mathbf C\setminus\{0\},\mu_n)\to H^2_{\{0\}}(\mathbf C,\mu_n)\) of the localization sequence, followed by the isomorphism \(H^2_{\{0\}}(\mathbf C,\mu_n)\cong H^2(\mathbf C,\mathbf C\setminus\{0\};\mu_n)\) of Theorem 2.2, satisfies \(\langle\partial\kappa(z),o_2\rangle=e^{-2\pi i/n}\), where \(o_2\) is the standard generator of \(H_2(\mathbf C,\mathbf C\setminus\{0\};\mathbf Z)\), which is the complex orientation of \(\mathbf C\) at \(0\).

**Proof.** (1) The Kummer sequence is exact, since a nowhere zero holomorphic function on a disc has holomorphic \(n\)-th roots [Lebl, Corollary 4.3.5]. The maps \(k\mapsto e^{2\pi ik/n}\) from \(\mathbf Z\) to \(\mu_n\), \(f\mapsto e^{2\pi if/n}\) from \(\mathcal O\) to \(\mathcal O^*\), and the identity of \(\mathcal O^*\) form a map from the exponential sequence to the Kummer sequence, because \((e^{2\pi if/n})^n=e^{2\pi if}\). Connecting maps are natural for maps of short exact sequences, so \(\kappa(z)\) is the image of \(\delta(z)\) under \(k\mapsto e^{2\pi ik/n}\), and Proposition 6.3 gives (1). (2) By Theorem 2.2, \(\partial\) is the connecting map of the pair \((\mathbf C,\mathbf C\setminus\{0\})\). For a cocycle \(a\) on \(\mathbf C\setminus\{0\}\), extended by zero to a cochain \(\tilde a\) on \(\mathbf C\), it sends \([a]\) to the class of \(\delta\tilde a\), and \((\delta\tilde a)(c)=\tilde a(\partial c)=a(\partial c)\) for a relative cycle \(c\). Take \(c=\tau_2\), which represents \(o_2\). By Exercise 6.2 of [Orientations and fundamental classes](orientations-and-fundamental-classes.md#6-exercises), \(\partial\tau_2\) is homologous in \(\mathbf C\setminus\{0\}\) to \(\gamma\), so \(\langle\partial\kappa(z),o_2\rangle=\langle\kappa(z),[\gamma]\rangle\). The complex orientation of \(\mathbf C\) is the standard orientation of \(\mathbf R^2\) [Orientations and fundamental classes, Corollary 3.5](orientations-and-fundamental-classes.md#3-orientations-from-charts). \(\square\)

## 7. Exercises

**Exercise 7.1.** Compute the sheaf cohomology \(H^q(S^1,\mathbf Z)\) and \(H^q_c(\mathbf R,\mathbf Z)\).

*Solution.* By Theorem 1.3(3), \(H^q(S^1,\mathbf Z)\) is singular cohomology: \(\mathbf Z\) for \(q=0,1\) and zero otherwise. By Corollary 3.2 and Example 2.2 of the lesson on cap products, \(H^q_c(\mathbf R,\mathbf Z)\) is \(\mathbf Z\) for \(q=1\) and zero otherwise.

**Exercise 7.2.** Let \(C\) be a compact connected Riemann surface. Show that the sheaf cohomology groups satisfy \(H^q(C,\mathbf Z)=0\) for \(q\geq3\) and \(H^2(C,\mathbf Z/m)\cong\mathbf Z/m\).

*Solution.* \(C\) is a compact connected \(2\)-manifold with its canonical orientation. Corollary 5.1 gives the vanishing. Since \(C\) is compact, \(H^2_c=H^2\), and Corollary 5.2(2) gives \(H^2(C,\mathbf Z/m)\cong\mathbf Z/m\).

**Exercise 7.3.** Let \(M\) be the open unit disc in \(\mathbf C\) and \(j:M\to T\) its inclusion into the closed disc. Compute \(H^q(T,j_!\mathbf Z)\).

*Solution.* By Theorem 4.1 it is \(H^q_c(M;\mathbf Z)\), and \(M\) is homeomorphic to \(\mathbf R^2\), so by Example 2.2 of the lesson on cap products it is \(\mathbf Z\) for \(q=2\) and zero otherwise.

## References

- [Roberts] D. M. Roberts, *Algebraic Topology* (lecture notes, 2019), licensed CC BY 4.0; the cohomology part of the core course *Algebraic Topology*. <https://github.com/DavidMichaelRoberts/AlgebraicTopology2019>
- [Stacks] The Stacks project authors, *Cohomology of Sheaves*, in the AI Integrated Stacks Project. <https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html>
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002; freely available from the author. <https://pi.math.cornell.edu/~hatcher/AT/ATpage.html>
- [Lebl] J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9 (2026), open textbook dual licensed CC BY-SA 4.0 and CC BY-NC-SA 4.0; the text of the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). <https://www.jirka.org/ca/>
