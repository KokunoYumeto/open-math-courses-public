# Cap products and cohomology with compact supports

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Poincaré duality compares cohomology in degree \(k\) with homology in degree \(n-k\) on an oriented \(n\)-manifold. The comparison map is the cap product with the fundamental class. On a noncompact manifold there is no fundamental class, but there are classes \(\mu_K\) for every compact \(K\), and the correct cohomology to pair with them is cohomology with compact supports. This lesson defines the cap product, establishes its formal properties, defines compactly supported cohomology of a manifold as a direct limit, proves its Mayer–Vietoris sequence, and constructs the duality map.

We use [Orientations and fundamental classes](orientations-and-fundamental-classes.md), singular homology and cohomology with coefficients in a commutative ring \(R\) from the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) (homology after [Fomberg], cohomology after [Roberts]), including excision and the Mayer–Vietoris sequences [Roberts, Theorems 14 and 15], [Fomberg, Proposition 1.25 and Theorem 1.26].

Basic references are [Hatcher] and [Miller].

## 1. The cap product

For a singular \(k\)-simplex \(\sigma:\Delta^k\to X\) and \(0\leq l\leq k\), write \(\sigma|[v_0,\ldots,v_l]\) and \(\sigma|[v_l,\ldots,v_k]\) for its front \(l\)-face and back \((k-l)\)-face. For a cochain \(\varphi\in C^l(X;R)\) define

\[
\sigma\frown\varphi=\varphi\bigl(\sigma|[v_0,\ldots,v_l]\bigr)\ \sigma|[v_l,\ldots,v_k]\ \in C_{k-l}(X;R),
\tag{1.1}
\]

extended \(R\)-linearly to chains. A direct computation with the faces of \(\sigma\), splitting the boundary sum at the index \(l\), gives

\[
\partial(\sigma\frown\varphi)=(-1)^l\bigl(\partial\sigma\frown\varphi-\sigma\frown\delta\varphi\bigr).
\tag{1.2}
\]

Hence the cap product of a cycle and a cocycle is a cycle; of a boundary and a cocycle, or a cycle and a coboundary, is a boundary. So (1.1) induces \(H_k(X;R)\times H^l(X;R)\to H_{k-l}(X;R)\). Relative versions: if \(A\subset X\), a chain in \(A\) capped with any cochain lies in \(A\), and a chain capped with a cochain vanishing on \(A\) depends only on the chain modulo \(A\); so (1.1) induces

\[
H_k(X,A)\times H^l(X)\to H_{k-l}(X,A),\qquad H_k(X,A)\times H^l(X,A)\to H_{k-l}(X).
\tag{1.3}
\]

**Proposition 1.1.**

1. (Naturality) For \(f:X\to Y\), \(f_*(\alpha)\frown\varphi=f_*(\alpha\frown f^*\varphi)\), in all the versions (1.3) with \(f(A)\subset B\).
2. (Relation to the cup product) \(\psi(\alpha\frown\varphi)=(\varphi\smile\psi)(\alpha)\) for \(\alpha\in H_{k+l}\), \(\varphi\in H^k\), \(\psi\in H^l\), where \((\varphi\smile\psi)(\sigma)=\varphi(\sigma|[v_0..v_k])\psi(\sigma|[v_k..v_{k+l}])\).

**Proof.** Both identities hold already for chains and cochains, directly from the definitions: in (1), faces of \(f\circ\sigma\) are \(f\) composed with faces of \(\sigma\); in (2), both sides evaluate \(\varphi\) on the front \(k\)-face and \(\psi\) on the back \(l\)-face of each simplex. \(\square\)

## 2. Cohomology with compact supports

Let \(M\) be a manifold. The compact subsets of \(M\) are directed by inclusion, and for \(K\subset L\) restriction gives maps \(H^i(M,M\setminus K)\to H^i(M,M\setminus L)\).

**Definition 2.1.** The **cohomology with compact supports** of \(M\) is \(H^i_c(M;R)=\varinjlim_KH^i(M,M\setminus K;R)\), the direct limit over the compact subsets \(K\subset M\).

If \(M\) is compact, \(K=M\) is cofinal and \(H^i_c(M)=H^i(M)\).

**Example 2.2.** For \(M=\mathbf R^n\), the closed balls \(\overline B_r\) about \(0\) are cofinal, and each restriction \(H^i(\mathbf R^n,\mathbf R^n\setminus\overline B_r)\to H^i(\mathbf R^n,\mathbf R^n\setminus\overline B_s)\), \(r<s\), is an isomorphism, the inclusions of complements being homotopy equivalences. Using the long exact sequence and \(\mathbf R^n\setminus\overline B_r\simeq S^{n-1}\), \(H^i_c(\mathbf R^n;R)\cong R\) for \(i=n\) and \(0\) otherwise.

**Functoriality for open embeddings.** Let \(U\subset M\) be open and \(K\subset U\) compact. Excision [Roberts, Theorem 15] identifies \(H^i(M,M\setminus K)\cong H^i(U,U\setminus K)\), since the closed set \(M\setminus U\) lies in the interior \(M\setminus K\) of \(M\setminus K\). Composing the inverse of this isomorphism with the map to the direct limit defines \(H^i_c(U)\to H^i_c(M)\), "extension by zero". These maps are compatible with compositions \(U\subset V\subset M\).

**Proposition 2.3 (Mayer–Vietoris for compact supports).** For open \(U,V\subset M\) there is a long exact sequence

\[
\cdots\to H^i_c(U\cap V)\to H^i_c(U)\oplus H^i_c(V)\to H^i_c(U\cup V)\to H^{i+1}_c(U\cap V)\to\cdots,
\tag{2.1}
\]

whose first map is \(\varphi\mapsto(\varphi,-\varphi)\) and whose second is the sum of the extensions by zero.

**Proof.** For compact \(K\subset U\) and \(L\subset V\), apply the Mayer–Vietoris sequence for the cover of \(M\setminus(K\cap L)\) by \(M\setminus K\) and \(M\setminus L\) to relative cohomology, exactly as in the homological version (3.1) of the previous lesson, using the subordinate cochains [Roberts, Proposition 26]:

\[
\cdots\to H^i(M,M\setminus(K\cap L))\to H^i(M,M\setminus K)\oplus H^i(M,M\setminus L)\to H^i(M,M\setminus(K\cup L))\to H^{i+1}(M,M\setminus(K\cap L))\to\cdots .
\]

By excision, \(H^i(M,M\setminus(K\cap L))=H^i(U\cap V,U\cap V\setminus K\cap L)\), \(H^i(M,M\setminus K)=H^i(U,U\setminus K)\), \(H^i(M,M\setminus L)=H^i(V,V\setminus L)\), and \(H^i(M,M\setminus(K\cup L))=H^i(U\cup V,U\cup V\setminus(K\cup L))\). As \(K\) and \(L\) range over compact subsets of \(U\) and \(V\), the sets \(K\cap L\) are cofinal among compact subsets of \(U\cap V\), and the sets \(K\cup L\) among compact subsets of \(U\cup V\) (a compact subset of \(U\cup V\) is the union of compact subsets of \(U\) and of \(V\)). Direct limits of exact sequences over directed sets are exact, so passing to the limit gives (2.1). \(\square\)

**Proposition 2.4.** If \(M=\bigcup_\nu U_\nu\) is an increasing union of open sets, then \(H^i_c(M)=\varinjlim_\nu H^i_c(U_\nu)\).

**Proof.** Every compact subset of \(M\) lies in some \(U_\nu\), so the directed system of all compact subsets of \(M\) is the union of those of the \(U_\nu\), and the excision identifications are compatible. \(\square\)

## 3. The duality map

Let \(M\) be an \(R\)-oriented \(n\)-manifold, with classes \(\mu_K\in H_n(M,M\setminus K)\) from [Orientations and fundamental classes, Theorem 3.1](orientations-and-fundamental-classes.md#3-classes-on-compact-subsets). For compact \(K\subset L\), the restriction of \(\mu_L\) is \(\mu_K\), by uniqueness. Define

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

**Proposition 3.2.** The duality maps for \(U\), \(V\) and \(U\cap V\), \(U\cup V\) give a map from the compact-support Mayer–Vietoris sequence (2.1) to the homology Mayer–Vietoris sequence

\[
\cdots\to H_{n-i}(U\cap V)\to H_{n-i}(U)\oplus H_{n-i}(V)\to H_{n-i}(U\cup V)\to H_{n-i-1}(U\cap V)\to\cdots
\]

whose squares commute up to sign.

**Proof.** The two squares not involving the connecting maps commute by Proposition 3.1. For the square with connecting maps, fix compact \(K\subset U\), \(L\subset V\). Represent \(\mu_{K\cup L}\) by a chain \(\alpha\) and write it, after subdivision, as \(\alpha=\alpha_{U\setminus L}+\alpha_{U\cap V}+\alpha_{V\setminus K}\), with chains carried by \(U\setminus L\), \(U\cap V\) and \(V\setminus K\) respectively; then \(\alpha_{U\cap V}\) represents \(\mu_{K\cap L}\), the sum \(\alpha_{U\setminus L}+\alpha_{U\cap V}\) represents \(\mu_K\) in \(H_n(U,U\setminus K)\), and similarly for \(L\). The connecting maps of both sequences are computed by splitting a cocycle (respectively a cycle) along the cover, and evaluating the defining formulas with this decomposition shows that the square commutes up to the sign \((-1)^{i+1}\). The details are the same as in [Hatcher, Lemma 3.36], whose proof applies verbatim. \(\square\)

## 4. Exercises

**Exercise 4.1.** Compute \(H^i_c\) of an open interval and of a circle with coefficients in \(\mathbf Z\), and compare with the homology in complementary degree.

*Solution.* The interval is homeomorphic to \(\mathbf R\), so \(H^1_c=\mathbf Z\) and \(H^0_c=0\) by Example 2.2; its homology is \(\mathbf Z\) in degree \(0\) and zero in degree \(1\), so \(H^i_c\cong H_{1-i}\). The circle is compact, so \(H^i_c(S^1)=H^i(S^1)\), which is \(\mathbf Z\) in degrees \(0\) and \(1\), matching \(H_1\) and \(H_0\).

**Exercise 4.2.** Show that \(H^0_c(M)=0\) for a connected noncompact manifold \(M\).

*Solution.* \(H^0(M,M\setminus K)\) consists of locally constant functions on \(M\) vanishing on \(M\setminus K\). On the connected space \(M\), a locally constant function is constant, and \(M\setminus K\neq\emptyset\) because \(M\) is not compact; so the function is zero.

## References

- [Fomberg] Y. Fomberg, *Algebraic topology* (lecture notes, 2023); the homology part of the core course *Algebraic Topology*. <https://yp.srht.site/notes/>
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002; freely available from the author. <https://pi.math.cornell.edu/~hatcher/AT/ATpage.html>
- [Miller] H. Miller, *Algebraic Topology I: Lecture Notes* (MIT 18.905, 2016). <https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/>
- [Roberts] D. M. Roberts, *Algebraic Topology* (lecture notes, 2019); the cohomology part of the core course *Algebraic Topology*. <https://github.com/DavidMichaelRoberts/AlgebraicTopology2019>
