# Cap products and cohomology with compact supports

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0). Prerequisite exposition revised by GPT-6 Astra (OpenAI), October 2026.*

Poincaré duality compares cohomology in degree \(k\) with homology in degree \(n-k\) on an oriented \(n\)-manifold. The comparison map is the cap product with the fundamental class. On a noncompact manifold there is no fundamental class, but there are classes \(\mu_K\) for every compact \(K\), and the correct cohomology to pair with them is cohomology with compact supports. This lesson defines the cap product, establishes its formal properties, defines compactly supported cohomology of a manifold as a direct limit, proves its Mayer–Vietoris sequence, and constructs the duality map together with its compatibility with the two Mayer–Vietoris sequences.

We use [Orientations and fundamental classes](orientations-and-fundamental-classes.md) and singular homology and cohomology with coefficients in a commutative ring \(R\) from the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60): from D. M. Roberts's notes the long exact sequence of a pair [Roberts, Proposition 24], the Mayer–Vietoris sequence [Roberts, Theorem 14], excision [Roberts, Theorem 15] and the cohomology of spheres [Roberts, Proposition 27]; from Y. Fomberg's notes small chains [Fomberg, Proposition 1.25]. As explained in Section 1 of the previous lesson, these hold with coefficients in \(R\). Complete chain-level proofs of homotopy invariance, small chains, excision and the exact sequences are in [Thom classes and Euler classes, Lemma 1.1, Lemma 2.1, Corollary 2.2 and Section 3](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/DG-CHAR/thom-classes-and-euler-classes.md#2-making-singular-chains-small).

Basic references are [Hatcher] and [Miller].

For an open cover \(\mathcal U\) of \(X\) and an abelian group \(G\), small cochains mean \(\operatorname{Hom}(C_*^{\mathcal U}(X),G)\). In [Thom classes and Euler classes, Lemma 2.1](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/DG-CHAR/thom-classes-and-euler-classes.md#2-making-singular-chains-small), the inclusion \(\iota\) has a chain retraction \(\rho\) with \(\rho\iota=1\) and \(1-\iota\rho=\partial D+D\partial\). Precomposition therefore gives a cochain homotopy equivalence \(\iota^*:C^*(X;G)\to\operatorname{Hom}(C_*^{\mathcal U}(X),G)\), with inverse \(\rho^*\); its cochain homotopy is precomposition with \(D\). The restriction \(\iota^*\) is surjective in each degree because a function on the small simplices extends by zero to the remaining simplices.

## 1. The cap product

For a singular \(k\)-simplex \(\sigma:\Delta^k\to X\) and \(0\leq l\leq k\), write \(\sigma|[v_0,\ldots,v_l]\) and \(\sigma|[v_l,\ldots,v_k]\) for its front \(l\)-face and back \((k-l)\)-face. For a cochain \(\varphi\in C^l(X;R)\) define

\[
\sigma\frown\varphi=\varphi\bigl(\sigma|[v_0,\ldots,v_l]\bigr)\ \sigma|[v_l,\ldots,v_k]\ \in C_{k-l}(X;R),
\tag{1.1}
\]

extended \(R\)-linearly to chains. Then

\[
\partial(\sigma\frown\varphi)=(-1)^l\bigl(\partial\sigma\frown\varphi-\sigma\frown\delta\varphi\bigr).
\tag{1.2}
\]

**Proof of (1.2).** Write \(\sigma_{\hat\imath}\) for the \(i\)-th face of \(\sigma\) and \(F=\varphi(\sigma|[v_0,\ldots,v_l])\). The front \(l\)-face of \(\sigma_{\hat\imath}\) is \(\sigma|[v_0,\ldots,\hat v_i,\ldots,v_{l+1}]\) with back face \(\sigma|[v_{l+1},\ldots,v_k]\) if \(i\leq l\), and is \(\sigma|[v_0,\ldots,v_l]\) with back face \(\sigma|[v_l,\ldots,\hat v_i,\ldots,v_k]\) if \(i>l\). Hence
\[
\partial\sigma\frown\varphi=\sum_{i=0}^{l}(-1)^i\varphi\bigl(\sigma|[v_0,\ldots,\hat v_i,\ldots,v_{l+1}]\bigr)\,\sigma|[v_{l+1},\ldots,v_k]
+\sum_{i=l+1}^{k}(-1)^iF\,\sigma|[v_l,\ldots,\hat v_i,\ldots,v_k].
\]
By definition of the coboundary, the first sum is \(\sigma\frown\delta\varphi-(-1)^{l+1}F\,\sigma|[v_{l+1},\ldots,v_k]\). Since \(\partial(\sigma|[v_l,\ldots,v_k])=\sigma|[v_{l+1},\ldots,v_k]+\sum_{i>l}(-1)^{i-l}\sigma|[v_l,\ldots,\hat v_i,\ldots,v_k]\), the second sum is \((-1)^lF\bigl(\partial(\sigma|[v_l,\ldots,v_k])-\sigma|[v_{l+1},\ldots,v_k]\bigr)=(-1)^l\partial(\sigma\frown\varphi)-(-1)^lF\,\sigma|[v_{l+1},\ldots,v_k]\). Adding, the terms with \(\sigma|[v_{l+1},\ldots,v_k]\) cancel and \(\partial\sigma\frown\varphi=\sigma\frown\delta\varphi+(-1)^l\partial(\sigma\frown\varphi)\), which is (1.2). \(\square\)

Hence the cap product of a cycle and a cocycle is a cycle; of a boundary and a cocycle, or a cycle and a coboundary, is a boundary. So (1.1) induces \(H_k(X;R)\times H^l(X;R)\to H_{k-l}(X;R)\). Relative versions: if \(A\subset X\), a chain in \(A\) capped with any cochain is a chain in \(A\), since faces of a simplex in \(A\) lie in \(A\); and a chain in \(A\) capped with a cochain vanishing on simplices in \(A\) is zero. So (1.1) induces

\[
H_k(X,A)\times H^l(X)\to H_{k-l}(X,A),\qquad H_k(X,A)\times H^l(X,A)\to H_{k-l}(X).
\tag{1.3}
\]

More generally, if \(\mathcal A\) is a set of subspaces of \(X\), a chain \(c\) whose boundary is a sum of chains in members of \(\mathcal A\), capped with a cocycle vanishing on all simplices contained in members of \(\mathcal A\), is a cycle, and its homology class changes by a boundary when the cocycle changes by the coboundary of a cochain with the same vanishing property; both follow from (1.2) in the same way.

**Proposition 1.1.**

1. (Naturality) For \(f:X\to Y\), \(f_*(\alpha)\frown\varphi=f_*(\alpha\frown f^*\varphi)\), in all the versions (1.3) with \(f(A)\subset B\).
2. (Relation to the cup product) \(\psi(\alpha\frown\varphi)=(\varphi\smile\psi)(\alpha)\) for \(\alpha\in H_{k+l}\), \(\varphi\in H^k\), \(\psi\in H^l\), where \((\varphi\smile\psi)(\sigma)=\varphi(\sigma|[v_0..v_k])\psi(\sigma|[v_k..v_{k+l}])\).

**Proof.** Both identities hold already for chains and cochains, directly from the definitions: in (1), faces of \(f\circ\sigma\) are \(f\) composed with faces of \(\sigma\); in (2), both sides evaluate \(\varphi\) on the front \(k\)-face and \(\psi\) on the back \(l\)-face of each simplex. \(\square\)

## 2. Cohomology with compact supports

Let \(M\) be a manifold. The compact subsets of \(M\) are directed by inclusion, and for \(K\subset L\) restriction gives maps \(H^i(M,M\setminus K)\to H^i(M,M\setminus L)\).

**Definition 2.1.** The **cohomology with compact supports** of \(M\) is \(H^i_c(M;R)=\varinjlim_KH^i(M,M\setminus K;R)\), the direct limit over the compact subsets \(K\subset M\).

If \(M\) is compact, \(K=M\) is cofinal and \(H^i_c(M)=H^i(M)\).

**Example 2.2.** For \(M=\mathbf R^n\), the closed balls \(\overline B_r\) about \(0\) are cofinal, and each restriction \(H^i(\mathbf R^n,\mathbf R^n\setminus\overline B_r)\to H^i(\mathbf R^n,\mathbf R^n\setminus\overline B_s)\), \(r<s\), is an isomorphism, the inclusions of complements being homotopy equivalences. Using the long exact sequence [Roberts, Proposition 24], the contractibility of \(\mathbf R^n\) and \(\mathbf R^n\setminus\overline B_r\simeq S^{n-1}\) [Roberts, Proposition 27], \(H^i_c(\mathbf R^n;R)\cong R\) for \(i=n\) and \(0\) otherwise.

**Functoriality for open embeddings.** Let \(U\subset M\) be open and \(K\subset U\) compact. Excision [Roberts, Theorem 15] identifies \(H^i(M,M\setminus K)\cong H^i(U,U\setminus K)\), since the closed set \(M\setminus U\) lies in the open set \(M\setminus K\). Composing the inverse of this isomorphism with the map to the direct limit defines \(H^i_c(U)\to H^i_c(M)\), "extension by zero". These maps are compatible with compositions \(U\subset V\subset M\).

**Proposition 2.3 (Mayer–Vietoris for compact supports).** For open \(U,V\subset M\) there is a long exact sequence

\[
\cdots\to H^i_c(U\cap V)\to H^i_c(U)\oplus H^i_c(V)\to H^i_c(U\cup V)\xrightarrow{\ \delta\ }H^{i+1}_c(U\cap V)\to\cdots,
\tag{2.1}
\]

whose first map is \(\varphi\mapsto(\varphi,-\varphi)\) and whose second is the sum of the extensions by zero.

**Proof.** *A finite stage.* Let \(K\subset U\) and \(L\subset V\) be compact and put \(P=M\setminus K\), \(Q=M\setminus L\), so that \(P\cup Q=M\setminus(K\cap L)\) and \(P\cap Q=M\setminus(K\cup L)\). Write \(C=C_\bullet(M;R)\) and \(C^\bullet(M,X)=\operatorname{Hom}(C/C_\bullet(X),R)\) for the cochains vanishing on simplices in \(X\). The sequence of chain complexes
\[
0\to C/C_\bullet(P\cap Q)\xrightarrow{c\mapsto(c,c)}C/C_\bullet(P)\oplus C/C_\bullet(Q)\xrightarrow{(a,b)\mapsto a-b}C/\bigl(C_\bullet(P)+C_\bullet(Q)\bigr)\to0
\]
is exact, and each term is free on a set of simplices, so it splits in each degree and remains exact after applying \(\operatorname{Hom}(-,R)\):
\[
0\to C^\bullet(M,P\cup Q)'\xrightarrow{\psi\mapsto(\psi,-\psi)}C^\bullet(M,P)\oplus C^\bullet(M,Q)\xrightarrow{(a,b)\mapsto a+b}C^\bullet(M,P\cap Q)\to0,
\tag{2.2}
\]
where \(C^\bullet(M,P\cup Q)'\) consists of the cochains vanishing on all simplices contained in \(P\) or in \(Q\). It contains \(C^\bullet(M,P\cup Q)\), and the inclusion is a quasi-isomorphism: the short exact sequences \(0\to C^\bullet(M,P\cup Q)\to C^\bullet(M)\to C^\bullet(P\cup Q)\to0\) and \(0\to C^\bullet(M,P\cup Q)'\to C^\bullet(M)\to\operatorname{Hom}(C_\bullet(P)+C_\bullet(Q),R)\to0\) (both split, as above) map to each other with the identity in the middle and, on the right, the restriction to cochains on simplices contained in \(P\) or \(Q\), which is a quasi-isomorphism by the small-cochain argument above; the five lemma applies to their long exact sequences. So (2.2) gives the long exact sequence
\[
\cdots\to H^i(M,M\setminus(K\cap L))\to H^i(M,M\setminus K)\oplus H^i(M,M\setminus L)\to H^i(M,M\setminus(K\cup L))\xrightarrow{\delta}H^{i+1}(M,M\setminus(K\cap L))\to\cdots .
\tag{2.3}
\]
Its connecting map is computed as follows: for a cocycle \(\varphi\in C^i(M,M\setminus(K\cup L))\), choose \(a\in C^i(M,P)\), \(b\in C^i(M,Q)\) with \(a+b=\varphi\); then \(\delta a=-\delta b\) vanishes on simplices contained in \(P\) or in \(Q\), and \(\delta[\varphi]\) is the class of \(\delta a\) in \(H^{i+1}(C^\bullet(M,P\cup Q)')=H^{i+1}(M,M\setminus(K\cap L))\). A choice is \(a(\sigma)=\varphi(\sigma)\) for \(\sigma\not\subset P\) and \(a(\sigma)=0\) for \(\sigma\subset P\): then \(b=\varphi-a\) vanishes on simplices in \(Q\), because a simplex in \(P\cap Q\) has \(\varphi(\sigma)=0\).

*The limit.* By excision, \(H^i(M,M\setminus(K\cap L))=H^i(U\cap V,(U\cap V)\setminus(K\cap L))\), \(H^i(M,M\setminus K)=H^i(U,U\setminus K)\), \(H^i(M,M\setminus L)=H^i(V,V\setminus L)\), and \(H^i(M,M\setminus(K\cup L))=H^i(U\cup V,(U\cup V)\setminus(K\cup L))\), and under these identifications the first two maps of (2.3) are those of (2.1). As \(K\) and \(L\) range over compact subsets of \(U\) and \(V\), the sets \(K\cap L\) are cofinal among compact subsets of \(U\cap V\) (take \(K=L\)), and the sets \(K\cup L\) among compact subsets of \(U\cup V\) (a compact subset of \(U\cup V\) is the union of a compact subset of \(U\) and one of \(V\): each point has a compact neighbourhood inside \(U\) or inside \(V\), and finitely many cover). The sequences (2.3) are natural in \((K,L)\), and direct limits of exact sequences over directed sets are exact, so passing to the limit gives (2.1). \(\square\)

**Proposition 2.4.** If \(M=\bigcup_\nu U_\nu\) is an increasing union of open sets, then \(H^i_c(M)=\varinjlim_\nu H^i_c(U_\nu)\).

**Proof.** Every compact subset of \(M\) lies in some \(U_\nu\), so the directed system of all compact subsets of \(M\) is the union of those of the \(U_\nu\), and the excision identifications are compatible. \(\square\)

## 3. The duality map

Let \(M\) be an \(R\)-oriented \(n\)-manifold, with classes \(\mu_K\in H_n(M,M\setminus K)\) from [Orientations and fundamental classes, Theorem 4.1](orientations-and-fundamental-classes.md#4-classes-on-compact-subsets). For compact \(K\subset L\), the restriction of \(\mu_L\) is \(\mu_K\), by uniqueness. Define

\[
D_K:H^k(M,M\setminus K)\to H_{n-k}(M),\qquad D_K(\varphi)=\mu_K\frown\varphi,
\tag{3.1}
\]

using the second pairing of (1.3). For \(K\subset L\), naturality of the cap product (Proposition 1.1) applied to the identity of \(M\), viewed as a map of pairs \((M,M\setminus L)\to(M,M\setminus K)\), gives \(D_L(\varphi|_L)=\mu_L\frown\varphi|_L=\mu_K\frown\varphi=D_K(\varphi)\). So the \(D_K\) induce the **duality map**

\[
D_M:H^k_c(M;R)\longrightarrow H_{n-k}(M;R).
\tag{3.2}
\]

**Proposition 3.1.** For an open subset \(U\subset M\), with the induced orientation, the square formed by \(D_U\), \(D_M\), extension by zero \(H^k_c(U)\to H^k_c(M)\) and the map \(H_{n-k}(U)\to H_{n-k}(M)\) induced by inclusion commutes.

**Proof.** For compact \(K\subset U\), the class \(\mu_K\) of \(U\) maps to the class \(\mu_K\) of \(M\) under the excision isomorphism \(H_n(U,U\setminus K)\cong H_n(M,M\setminus K)\), since both restrict to the same local orientations. Naturality of the cap product for the inclusion \((U,U\setminus K)\to(M,M\setminus K)\) gives the claim. \(\square\)

We use the homology Mayer–Vietoris sequence of an open cover \(\{U,V\}\) of \(U\cup V\) in the form coming from the short exact sequence \(0\to C_\bullet(U\cap V)\to C_\bullet(U)\oplus C_\bullet(V)\to C_\bullet(U)+C_\bullet(V)\to0\), with maps \(x\mapsto(x,-x)\) and \((y,z)\mapsto y+z\), and the small-chain theorem [Fomberg, Proposition 1.25]:

\[
\cdots\to H_{j}(U\cap V)\to H_{j}(U)\oplus H_{j}(V)\to H_{j}(U\cup V)\xrightarrow{\ \partial\ }H_{j-1}(U\cap V)\to\cdots .
\]

Its connecting map sends the class of a cycle \(z=z_U+z_V\), with \(z_U\) a chain in \(U\) and \(z_V\) a chain in \(V\), to the class of \(\partial z_U\), a cycle in \(U\cap V\).

**Proposition 3.2.** The duality maps for \(U\cap V\), \(U\), \(V\) and \(U\cup V\) give a map from the compact-support Mayer–Vietoris sequence (2.1) to the homology Mayer–Vietoris sequence with \(j=n-i\). The two squares not involving connecting maps commute, and \(D_{U\cap V}\circ\delta=(-1)^{i+1}\,\partial\circ D_{U\cup V}\) on \(H^i_c(U\cup V)\).

**Proof.** The squares not involving connecting maps commute by Proposition 3.1, since both sequences use the maps \(x\mapsto(x,-x)\) and the sum. All four duality maps only involve \(U\cup V\) with its induced orientation, so we may assume \(M=U\cup V\). It suffices to prove the identity at a finite stage: for compact \(K\subset U\), \(L\subset V\) and a cocycle \(\varphi\in C^i(M,M\setminus(K\cup L))\), we show
\[
D_{K\cap L}(\delta[\varphi])=(-1)^{i+1}\,\partial\,D_{K\cup L}[\varphi]
\]
in \(H_{n-i-1}(U\cap V)\), where \(D_{K\cap L}\) uses the class \(\mu_{K\cap L}\) of the orientation of \(U\cap V\).

*A representing chain.* The open sets \(U\setminus L\), \(U\cap V\) and \(V\setminus K\) cover \(M\). Let \(\alpha\) be a relative cycle representing \(\mu_{K\cup L}\), so \(\partial\alpha\) is a chain in \(M\setminus(K\cup L)\). Iterated barycentric subdivision changes \(\alpha\) by \(\partial T\alpha+T\partial\alpha\), where \(T\) maps each simplex to a chain carried by its image [Thom classes and Euler classes, Lemma 2.1](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/DG-CHAR/thom-classes-and-euler-classes.md#2-making-singular-chains-small); the term \(T\partial\alpha\) is a chain in \(M\setminus(K\cup L)\), so the class is unchanged. Hence we may assume that every simplex of \(\alpha\) lies in one of the three open sets, and write
\[
\alpha=\alpha_{U\setminus L}+\alpha_{U\cap V}+\alpha_{V\setminus K}
\]
with chains carried by the indicated sets. Then:

- \(\partial\alpha_{U\cap V}=\partial\alpha-\partial\alpha_{U\setminus L}-\partial\alpha_{V\setminus K}\) is a sum of chains in \(M\setminus K\) and in \(M\setminus L\); in particular it is a chain in \((U\cap V)\setminus(K\cap L)\). At a point \(x\in K\cap L\), the chains \(\alpha_{U\setminus L}\) and \(\alpha_{V\setminus K}\) lie in \(M\setminus x\), so \(\alpha_{U\cap V}\) has the same local class as \(\alpha\), namely \(\mu_x\). By the uniqueness in Theorem 4.1 of the previous lesson (applied in \(U\cap V\)), \(\alpha_{U\cap V}\) represents \(\mu_{K\cap L}\).
- \(\alpha=\alpha_{U\setminus L}+(\alpha_{U\cap V}+\alpha_{V\setminus K})\) splits \(\alpha\) into a chain in \(U\) and a chain in \(V\).

*The homology side.* \(D_{K\cup L}[\varphi]\) is the class of the cycle \(\alpha\frown\varphi\). With \(z_U=\alpha_{U\setminus L}\frown\varphi\) (a chain in \(U\)) and \(z_V=(\alpha_{U\cap V}+\alpha_{V\setminus K})\frown\varphi\) (a chain in \(V\)), the connecting map gives \(\partial D_{K\cup L}[\varphi]=[\partial z_U]\). By (1.2) and \(\delta\varphi=0\), \(\partial z_U=(-1)^i\,\partial\alpha_{U\setminus L}\frown\varphi\).

*The cohomology side.* Take \(a(\sigma)=\varphi(\sigma)\) for \(\sigma\not\subset M\setminus K\) and \(a(\sigma)=0\) otherwise, as in the proof of Proposition 2.3; then \(\delta[\varphi]\) is represented by \(\delta a\), which vanishes on simplices contained in \(M\setminus K\) or in \(M\setminus L\). Since \(\partial\alpha_{U\cap V}\) is a sum of chains in these two sets, the general form of (1.3) shows that \(\alpha_{U\cap V}\frown\delta a\) is a cycle representing \(D_{K\cap L}(\delta[\varphi])\): an honest representative of \(\delta[\varphi]\) differs from \(\delta a\) by the coboundary of a cochain vanishing on simplices in \(M\setminus K\) or \(M\setminus L\), which changes the cap product by a boundary. By (1.2),
\[
\alpha_{U\cap V}\frown\delta a=\partial\alpha_{U\cap V}\frown a-(-1)^i\,\partial(\alpha_{U\cap V}\frown a),
\]
and \(\alpha_{U\cap V}\frown a\) is a chain in \(U\cap V\). Now \(\partial\alpha_{U\cap V}\frown a=(\partial\alpha-\partial\alpha_{U\setminus L}-\partial\alpha_{V\setminus K})\frown a\). The simplices of \(\partial\alpha\) and of \(\partial\alpha_{V\setminus K}\) lie in \(M\setminus K\), and so do their front faces, on which \(a\) vanishes; so these terms are zero. The front faces \(\tau\) of the simplices of \(\partial\alpha_{U\setminus L}\) lie in \(M\setminus L\), and there \(a(\tau)=\varphi(\tau)\): if \(\tau\not\subset M\setminus K\) this is the definition, and if \(\tau\subset M\setminus K\) then \(\tau\subset M\setminus(K\cup L)\), where both vanish. Hence \(\partial\alpha_{U\cap V}\frown a=-\partial\alpha_{U\setminus L}\frown\varphi\), and in \(H_{n-i-1}(U\cap V)\)
\[
D_{K\cap L}(\delta[\varphi])=-[\partial\alpha_{U\setminus L}\frown\varphi]=(-1)^{i+1}[\partial z_U]=(-1)^{i+1}\,\partial D_{K\cup L}[\varphi].
\]
Passing to the direct limit over \(K\) and \(L\) proves the proposition. \(\square\)

This is the argument of [Hatcher, Lemma 3.36], with the cochain choices made explicit.

## 4. Exercises

**Exercise 4.1.** Compute \(H^i_c\) of an open interval and of a circle with coefficients in \(\mathbf Z\), and compare with the homology in complementary degree.

*Solution.* The interval is homeomorphic to \(\mathbf R\), so \(H^1_c=\mathbf Z\) and \(H^0_c=0\) by Example 2.2; its homology is \(\mathbf Z\) in degree \(0\) and zero in degree \(1\), so \(H^i_c\cong H_{1-i}\). The circle is compact, so \(H^i_c(S^1)=H^i(S^1)\), which is \(\mathbf Z\) in degrees \(0\) and \(1\), matching \(H_1\) and \(H_0\).

**Exercise 4.2.** Show that \(H^0_c(M)=0\) for a connected noncompact manifold \(M\).

*Solution.* \(H^0(M,M\setminus K)\) consists of the \(0\)-cocycles vanishing on \(M\setminus K\), that is, functions on points that are constant along paths and vanish on \(M\setminus K\). A manifold is locally path connected, so a connected manifold is path connected and such a function is constant; it vanishes because \(M\setminus K\neq\emptyset\) for a noncompact \(M\).

## References

- [Fomberg] Y. Fomberg, *Algebraic Topology*, notes on lectures by Nir Lazarovich, Spring 2025; the homology part of the core course *Algebraic Topology*. [Native source](https://yp.srht.site/notes/math/algebraic_topology.tex), [PDF](https://yp.srht.site/notes/math/algebraic_topology.pdf).
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002; freely available from the author. <https://pi.math.cornell.edu/~hatcher/AT/ATpage.html>
- [Miller] H. Miller, *Algebraic Topology I: Lecture Notes* (MIT 18.905, 2016). <https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/>
- [Roberts] D. M. Roberts, *Algebraic Topology* (lecture notes, 2019); the cohomology part of the core course *Algebraic Topology*. <https://github.com/DavidMichaelRoberts/AlgebraicTopology2019>
