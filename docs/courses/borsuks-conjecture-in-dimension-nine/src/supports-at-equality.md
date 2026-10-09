# Supports at equality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An admissible map on the lines of \(\mathbb R^k\) needs at least \(N_k=k(k+1)/2\) labels (Proposition 1.1). This lesson shows that when it has exactly \(N_k\) labels, its support complex is rigid: every facet has exactly \(k\) labels, every facet is hit an odd number of times over each regular value of its interior (Theorem 2.1), and the sum of the facets is a cycle modulo two (Theorem 3.3). For \(k=4\) these are the ten-label complexes that [Six and ten labels](six-and-ten-labels.md) rules out.

The proof extends the admissible map to the odd map \(F_V\) of [An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md), whose degree modulo two is one. Over a facet \(I\), the operators of trace norm one with positive part supported on a line of the set \(U_I\) form a sphere bundle over a level set of \(f\); counting preimages there in two ways, with [Double covers and odd maps](double-covers-and-odd-maps.md), forces the level set to be finite. Notation: \(V\) is Euclidean of dimension \(k\), \(f:\mathbb P(V)\to\Delta^{m-1}\) is admissible with supports \(S(x)\) and support complex \(K\), \(F_V\), \(\Sigma(V)\), \(\Sigma_m\), \(\widehat F\) are as in [An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md), and homology has coefficients in \(\mathbb F_2\).

## 1. The number of labels

**Proposition 1.1.** Let \(k\ge2\). Every admissible map \(f:\mathbb P(\mathbb R^k)\to\Delta^{m-1}\) has \(m\ge N_k\). If \(m=N_k\), then \(\deg_2\widehat F=1\), \(F_V\) maps \(\Sigma(V)\) onto \(\Sigma_m\), and every pair of labels is a face of \(K\).

*Proof.* \(\widehat F:S^{N_k-1}\to S^{m-1}\) is odd, so \(N_k-1\le m-1\) by the Borsuk–Ulam theorem (Corollary 4.2 of [Double covers and odd maps](double-covers-and-odd-maps.md)). If \(m=N_k\), it is an odd self-map of a sphere of dimension at least two, so it has degree one modulo two and is surjective (Theorem 4.1 there). Let \(i\ne j\) be labels, and choose \(y\in\Sigma_m\) with all coordinates nonzero and with positive coordinates exactly at \(i\) and \(j\); this is possible because \(m\ge3\). Let \(A\in\Sigma(V)\) with \(F_V(A)=y\), and let \(W_+\ne0\) be its positive spectral subspace. By Proposition 3.1(a) of [An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md), every line of \(W_+\) has support in \(\{i,j\}\). If \(\dim W_+\ge2\), the restriction of \(f\) to the lines of a plane in \(W_+\) would be an admissible map with at most two labels (Lemma 2.2 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md)), contradicting the first statement for \(k=2\), \(N_2=3\). So \(W_+\) is a line \(x\), and since both coordinates \(i,j\) of \(F_V(A)\) are positive, \(S(x)=\{i,j\}\). \(\square\)

**Corollary 1.2.** If \(f:\mathbb P(V)\to\Delta^{m-1}\) is admissible and \(W\subseteq V\) has dimension \(r\ge2\), then at least \(N_r\) labels occur in supports of lines of \(W\). In particular, if \(m=N_k\), every label occurs.

*Proof.* Apply Proposition 1.1 to the restriction to \(\mathbb P(W)\), with the labels that occur there (Lemma 2.2 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md)). \(\square\)

## 2. Facets at equality

For a face \(I\) let \(\Delta_I\) be the closed face of \(\Delta^{m-1}\) spanned by the \(e_i\), \(i\in I\), and \(\mathring\Delta_I\) its relative interior, an open subset of an affine space of dimension \(|I|-1\). For \(r\in\mathring\Delta_I\), \(\tilde r\in\Delta^{m-1}\) is \(r\) extended by zeros. For a facet \(I\), \(U_I\) is the open set of lines where all coordinates in \(I\) are positive, and \(f_I=(f_i)_{i\in I}:U_I\to\mathring\Delta_I\) is smooth (Lemma 3.2 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md): \(S(x)=I\) on \(U_I\)).

**Theorem 2.1** (Supports at equality). Let \(k\ge3\), \(m=N_k\) and \(f:\mathbb P(V)\to\Delta^{m-1}\) admissible. Then every facet \(I\) of \(K\) has exactly \(k\) labels. For every regular value \(r\in\mathring\Delta_I\) of \(f_I:U_I\to\mathring\Delta_I\), the fibre \(f^{-1}(\tilde r)\) is finite with an odd number of points.

*Proof.* Fix a facet \(I\), a witness \(x_0\) with \(S(x_0)=I\), and put
\[
s=|I|,\qquad J=[m]\setminus I,\qquad a=|J|,\qquad h=N_{k-1}.
\]

*Step 1: \(s\le k\).* Every line of \(x_0^\perp\) uses only labels of \(J\) (Lemma 3.2 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md)), and at least \(h\) labels occur there (Corollary 1.2, \(\dim x_0^\perp=k-1\ge2\)). So \(a\ge h\) and \(s=N_k-a\le N_k-N_{k-1}=k\).

*Step 2: the level set.* Let \(r\in\mathring\Delta_I\) be a regular value of \(f_I\) on \(U_I\); regular values exist by Sard's theorem (Corollary 2.2 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)). Put \(L=f^{-1}(\tilde r)\). A line with \(f(x)=\tilde r\) has \(f_i(x)=r_i>0\) for \(i\in I\), so \(L=f_I^{-1}(r)\subseteq U_I\). It is closed in the compact space \(\mathbb P(V)\), and by Proposition 3.1 there it is a compact smooth manifold of dimension \((k-1)-(s-1)=k-s=a-h\). Moreover \(U_I\) lies in the affine chart \(\mathbb P(V)\setminus\mathbb P(x_0^\perp)\).

*Step 3: a sphere bundle and an odd map.* For \(x\in U_I\), lines orthogonal to \(x\) use only labels in \(J\), so \(f|_{\mathbb P(x^\perp)}\), in the coordinates \(J\), is an admissible map to \(\Delta_J\cong\Delta^{a-1}\); let \(F_{x^\perp}\) be its odd extension, mapping \(\Sigma(x^\perp)\) to \(\Sigma_a\). Let \(\mathcal S_x\) be the set of \(B\in\operatorname{Sym}(V)\) that vanish on \(x\) and map \(x^\perp\) into itself; restriction identifies \(\mathcal S_x\) with \(\operatorname{Sym}(x^\perp)\), and by Proposition 3.1(e) of [An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md), \(F_V(B)\) has zero \(I\)-coordinates and \(J\)-coordinates \(F_{x^\perp}(B|_{x^\perp})\). Put
\[
M=\{(x,B):x\in L,\ B\in\mathcal S_x,\ \operatorname{tr}|B|=1\},\qquad G(x,B)=F_V(B)_J\in\Sigma_a .
\]
\(G\) is continuous, and \(G(x,-B)=-G(x,B)\).

The bundle is trivial over the affine chart. Let \(u_0\) be a unit vector of \(x_0\). For \(x\) not orthogonal to \(x_0\), the operator \(I-P_x\) maps \(x_0^\perp\) injectively into \(x^\perp\): if \(w\in x_0^\perp\) and \(w=P_xw\), then \(w\in x\) is orthogonal to \(u_0\), and \(x\not\perp x_0\) forces \(w=0\). Both spaces have dimension \(k-1\), so this is an isomorphism, depending smoothly on \(x\). Applying the Gram–Schmidt process to the images of a fixed orthonormal basis of \(x_0^\perp\) gives a smooth isometry \(T_x:\mathbb R^{k-1}\to V\) with range \(x^\perp\). Then \(B\mapsto D=T_x^{\mathsf T}BT_x\) identifies \(\mathcal S_x\) with \(\operatorname{Sym}(\mathbb R^{k-1})\cong\mathbb R^h\), preserving trace norms, and with the radial projection \(\rho\) onto the unit sphere \(S^{h-1}\) of \(\operatorname{Sym}(\mathbb R^{k-1})\) we get a homeomorphism
\[
\Theta:M\to L\times S^{h-1},\qquad(x,B)\mapsto\bigl(x,\rho(T_x^{\mathsf T}BT_x)\bigr),
\]
which turns \((x,B)\mapsto(x,-B)\) into \((x,z)\mapsto(x,-z)\). We give \(M\) the smooth structure of \(L\times S^{h-1}\); it is a closed manifold of dimension \((a-h)+(h-1)=a-1\). Then \(\Psi=\rho_a\circ G\circ\Theta^{-1}:L\times S^{h-1}\to S^{a-1}\) satisfies \(\Psi(x,-z)=-\Psi(x,z)\).

*Step 4: an odd count.* Let \(O_-\subseteq\Sigma_a\) be the open set of vectors with all coordinates negative. If \(G(x,B)\in O_-\), then \(B|_{x^\perp}\) is negative definite (Proposition 3.1(c) there, for \(F_{x^\perp}\)), so \(B_+=0\) and \(G(x,B)=-E_V(-B)_J\). Writing \(-B=T_x(-D)T_x^{\mathsf T}\) with \(-D\succ0\), Lemma 2.1(e) there shows that \(G\) is smooth in \((x,D)\), and \(D=z/\operatorname{tr}|z|=-z/\operatorname{tr}z\) is smooth in \(z\) near negative definite \(z\). So \(G\) is smooth on the open set \(G^{-1}(O_-)\subseteq M\), whose dimension \(a-1\) equals that of \(O_-\). Choose a regular value \(g\in O_-\) of \(G\) on \(G^{-1}(O_-)\) (Sard). Its preimage \(G^{-1}(g)\) is finite (Corollary 3.2 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)).

Fix \(0<\lambda<1\) and let \(y\in\Sigma_m\) have \(I\)-coordinates \(\lambda r\) and \(J\)-coordinates \((1-\lambda)g\). All coordinates of \(y\) are nonzero. We claim that
\[
(x,B)\longmapsto A=\lambda P_x+(1-\lambda)B \tag{2.1}
\]
is a bijection from \(G^{-1}(g)\) onto \(F_V^{-1}(y)\cap\Sigma(V)\).

If \((x,B)\in G^{-1}(g)\), then \(B\) is negative definite on \(x^\perp\), so \(A_+=\lambda P_x\), \(A_-=-(1-\lambda)B\), \(\operatorname{tr}|A|=\lambda+(1-\lambda)=1\), and \(F_V(A)=\lambda f(x)+(1-\lambda)F_V(B)\) has \(I\)-coordinates \(\lambda r\) and \(J\)-coordinates \((1-\lambda)g\). Conversely let \(A\in\Sigma(V)\) with \(F_V(A)=y\). By Proposition 3.1(c) there, \(A\) is nonsingular. Its positive labels are exactly \(I\), so every line of its positive spectral subspace \(W_+\ne0\) has support in \(I\). If \(\dim W_+\ge2\), then \(W_+\) meets the hyperplane \(x_0^\perp\) in a line, whose support lies in \(I\cap J=\varnothing\), which is impossible. So \(W_+\) is a line \(x\), and since every coordinate in \(I\) is positive, \(S(x)=I\) and \(x\in U_I\). The positive eigenvalue is \(\operatorname{tr}A_+=\sum_{i\in I}F_V(A)_i=\lambda\), and \(A_-\) is positive definite on \(x^\perp\) with \(\operatorname{tr}A_-=1-\lambda\). So \(A=\lambda P_x+(1-\lambda)B\) with \(B=-A_-/(1-\lambda)\in\mathcal S_x\), \(\operatorname{tr}|B|=1\). Comparing coordinates, \(f_I(x)=r\), so \(x\in L\), and \(G(x,B)=g\). The pair \((x,B)\) is determined by \(A\), which proves the claim.

Each \(A\) in (2.1) is a regular point. Near \(A^*=\lambda P_{x^*}+(1-\lambda)B^*\), the operators of \(\Sigma(V)\) are nonsingular with exactly one positive eigenvalue, and
\[
(\lambda',x',D')\longmapsto\lambda'P_{x'}+(1-\lambda')T_{x'}D'T_{x'}^{\mathsf T},
\]
with \(\lambda'\) near \(\lambda\), \(x'\) near \(x^*\) in \(U_I\), and \(D'\) negative definite with \(\operatorname{tr}D'=-1\), is a system of smooth coordinates on the hypersurface \(\Sigma(V)\) (Lemma 4.1 there): its inverse sends \(A\) to the positive eigenvalue \(\operatorname{tr}A_+\), the line \(\operatorname{ran}\Pi_+(A)\), and \(T_{x'}^{\mathsf T}(-A_-)T_{x'}/(1-\lambda')\), all smooth by Lemma 1.2 there. The number of coordinates is \(1+(k-1)+(h-1)=N_k-1\). Near \(y\), the vectors of \(\Sigma_m\) with positive \(I\)-coordinates and negative \(J\)-coordinates have smooth coordinates \((\mu,y_I/\mu,y_J/(1-\mu))\) with \(\mu=\sum_{i\in I}y_i\). By the computation above, valid for every \(x'\in U_I\), the map \(F_V\) reads in these coordinates
\[
(\lambda',x',D')\longmapsto\bigl(\lambda',\ f_I(x'),\ G(x',D')\bigr),
\]
where \(G(x',D')=-E_V(T_{x'}(-D')T_{x'}^{\mathsf T})_J\) is smooth for \(x'\in U_I\). Its derivative is surjective. Let \((\alpha,\varrho,\gamma)\) be a target vector. Take \(\dot\lambda=\alpha\). Choose a tangent vector \(\xi\) at \(x^*\) with \(Df_I(\xi)=\varrho\), which exists because \(r\) is a regular value. The tangent directions of \(M\) at \((x^*,D^*)\) are the vectors \(\xi'\in\ker Df_I\) together with the \(D'\)-directions (Proposition 3.1 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)), and the derivative of \(G\) restricted to \(M\) is surjective there because \(g\) is a regular value. So there are \(\xi'\in\ker Df_I\) and \(\dot D\) with \(D_xG(\xi')+D_DG(\dot D)=\gamma-D_xG(\xi)\). The vector \((\alpha,\xi+\xi',\dot D)\) maps to \((\alpha,\varrho,\gamma)\). Source and target dimensions are both \(m-1\), so the derivative is invertible.

By Proposition 1.1, \(\deg_2\widehat F=1\). The local counting lemma (Lemma 4.2 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)), applied to \(\widehat F\) at \(\rho_m(y)\) with Lemma 4.1(c) of [An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md), gives
\[
|G^{-1}(g)|=|F_V^{-1}(y)\cap\Sigma(V)|\equiv1\pmod2 . \tag{2.2}
\]
In particular \(L\ne\varnothing\).

*Step 5: \(a=h\).* Suppose \(a>h\). Then \(L\) is a nonempty closed manifold of dimension \(a-h\ge1\), and by Proposition 5.1 of [Double covers and odd maps](double-covers-and-odd-maps.md), the map \(\bar\Psi:L\times\mathbb{RP}^{h-1}\to\mathbb{RP}^{a-1}\) induced by \(\Psi\) has degree zero modulo two. On the other hand, consider the point \(\hat g=[\rho_a(g)]\in\mathbb{RP}^{a-1}\). A point \([(x,z)]\) of its preimage has \(\Psi(x,z)=\pm\rho_a(g)\), and since \(\Psi(x,-z)=-\Psi(x,z)\), exactly one of its two representatives maps to \(\rho_a(g)\). So \(|\bar\Psi^{-1}(\hat g)|=|\Psi^{-1}(\rho_a(g))|=|G^{-1}(g)|\). The quotient maps \(S^{a-1}\to\mathbb{RP}^{a-1}\) and \(L\times S^{h-1}\to L\times\mathbb{RP}^{h-1}\) are local diffeomorphisms (on an open hemisphere \(\{u_i>0\}\), \(u\mapsto[u]\) is inverse to the chart \(\varphi_i\) followed by normalization), and \(\Psi\) is smooth with invertible derivative near each point of \(\Psi^{-1}(\pm\rho_a(g))\) (by oddness, near the points over \(-\rho_a(g)\) as well). The local counting lemma gives \(\deg_2\bar\Psi\equiv|G^{-1}(g)|\equiv1\), a contradiction. Hence \(a=h\) and \(s=k\).

*Step 6: the odd fibre.* Since \(a=h\), \(\dim L=0\), so \(L\) is finite and \(M\) is the disjoint union of the spheres \(\{x\}\times\Sigma(x^\perp)\), \(x\in L\), on which \(G\) is \(F_{x^\perp}\), an odd map between spheres of the same dimension \(h-1=a-1\ge2\). Each has degree one modulo two (Theorem 4.1 of [Double covers and odd maps](double-covers-and-odd-maps.md)), \(g\) is a regular value of each, and the local counting lemma gives \(|F_{x^\perp}^{-1}(g)|\) odd for each \(x\in L\). With (2.2), \(|L|\equiv|G^{-1}(g)|\equiv1\pmod2\). The argument applies to every regular value \(r\) of \(f_I\). \(\square\)

## 3. The facet cycle

Order the labels \(1<\dots<m\). For a face \(I=\{i_0<\dots<i_d\}\) let \(\sigma_I:\Delta^d\to|K|\) be the affine map sending the \(j\)-th vertex to \(e_{i_j}\). These maps make \(|K|\) a \(\Delta\)-complex, and simplicial chains (with \(\mathbb F_2\) coefficients) are the sums of faces, with boundary \(\partial I=\sum_jI\setminus\{i_j\}\).

**Lemma 3.1** (Simplicial and singular homology modulo two). The chain map \(I\mapsto\sigma_I\) from simplicial chains of \(K\) to singular chains of \(|K|\) induces isomorphisms in homology with \(\mathbb F_2\) coefficients.

*Proof.* With integer coefficients this is Proposition 1.32 of Fomberg's notes (core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60)). Let \(\phi:C\to D\) be this integral chain map; both complexes consist of free abelian groups and vanish in negative degrees. Its mapping cone \(\operatorname{Cone}(\phi)_n=C_{n-1}\oplus D_n\), \(d(c,e)=(-dc,de+\phi c)\), sits in a short exact sequence \(0\to D\to\operatorname{Cone}(\phi)\to C[-1]\to0\) whose connecting map is \(\phi_*\); so \(\phi\) induces isomorphisms exactly when the cone is acyclic. The cone is a complex of free abelian groups with zero, hence free, homology, so by Lemma 1.1 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes) its homology with \(\mathbb F_2\) coefficients is \(0\otimes\mathbb F_2=0\). The same short exact sequence tensored with \(\mathbb F_2\), which stays exact because it splits in each degree, shows that \(\phi\otimes\mathbb F_2\) induces isomorphisms. \(\square\)

**Lemma 3.2** (Reading coefficients). Let \(K\) have dimension \(d\), let \(I\) be a face with \(d+1\) labels, and \(t\in\mathring\Delta_I\). Then \(\mathring\Delta_I\) is open in \(|K|\), \(H_d(|K|,|K|\setminus t)\cong\mathbb F_2\), and the image of the class of a simplicial cycle \(\sum_Jc_JJ\) in this group is \(c_I\) times the generator.

*Proof.* A point of \(|K|\) close to \(t\) has positive coordinates in \(I\), so it lies in some \(\Delta_J\) with \(J\supseteq I\), \(J\in K\); by maximality \(J=I\). So a neighbourhood of \(t\) in \(|K|\) lies in \(\mathring\Delta_I\). Let \(E\) be the affine span of \(\Delta_I\), a Euclidean space of dimension \(d\). Excision of \(|K|\setminus\Delta_I\), whose closure misses \(\mathring\Delta_I\), and of \(E\setminus\Delta_I\), gives
\[
H_d(|K|,|K|\setminus t)\cong H_d(\Delta_I,\Delta_I\setminus t)\cong H_d(E,E\setminus t),
\]
and by Lemma 1.2(3) of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes), the class of \(\sigma_I\) generates the last group. For \(J\ne I\) of dimension \(d\), \(\sigma_J\) has image \(\Delta_J\), which does not contain \(t\), so its class in \(H_d(|K|,|K|\setminus t)\) is zero. \(\square\)

**Theorem 3.3** (The facet cycle). Let \(k\ge3\), \(m=N_k\) and \(f:\mathbb P(V)\to\Delta^{m-1}\) admissible. Then the sum of all facets of \(K\) is a simplicial cycle modulo two. Equivalently, every face with \(k-1\) labels lies in a positive even number of facets.

*Proof.* By Theorem 2.1 every facet has \(k\) labels, so \(K\) has dimension \(k-1\) and no faces of \(k+1\) labels; its simplicial homology in degree \(k-1\) is therefore the group of simplicial cycles. By Lemma 3.1 the class \(f_*[\mathbb P(V)]\in H_{k-1}(|K|)\) is represented by a unique simplicial cycle \(\sum_Ic_II\). Let \(I\) be a facet, \(r\) a regular value of \(f_I\) on \(U_I\), and \(t=\tilde r\). The open set \(\mathring\Delta_I\subseteq|K|\) is homeomorphic to an open subset of \(\mathbb R^{k-1}\), \(f\) maps a neighbourhood of \(f^{-1}(t)\subseteq U_I\) smoothly into it, and the derivative of \(f_I\) at points of \(f^{-1}(t)\) is surjective between spaces of the same dimension \(k-1\), hence invertible. The local counting lemma (Lemma 4.2 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md)) and Theorem 2.1 show that the image of \(f_*[\mathbb P(V)]\) in \(H_{k-1}(|K|,|K|\setminus t)\) is the generator, and Lemma 3.2 gives \(c_I=1\). So the sum of all facets is a cycle, and its boundary, \(\sum_D(\text{number of facets containing }D)\,D\) over faces \(D\) with \(k-1\) labels, vanishes modulo two. Every such \(D\) lies in some facet, which has \(k\) labels. \(\square\)

## 4. Exercises

**4.1.** Let \(k=2\) and \(f:\mathbb P(\mathbb R^2)\to\Delta^2\) admissible. Show that no line uses all three labels, and that the facets of \(K\) are exactly the three pairs. Check that their sum is a cycle.

**4.2.** Verify \(N_k-N_{k-1}=k\) and \(1+(k-1)+(N_{k-1}-1)=N_k-1\), the two dimension counts used in the proof of Theorem 2.1.

**4.3.** In Step 4, why can the positive spectral subspace of \(A\) not have dimension two or more? Which property of the facet \(I\) and of its witness \(x_0\) does this use?

**4.4.** Use Theorem 3.3 and Proposition 1.1 to show that for \(k=3\) the support complex of an admissible map \(\mathbb P(\mathbb R^3)\to\Delta^5\) has at least ten triangles.

## 5. Solutions

**4.1.** If \(S(x)=\{1,2,3\}\), a line orthogonal to \(x\) would have empty support. By Proposition 1.1 every pair is a face, so the facets are the three pairs. Each label lies in exactly two of them, so the boundary of their sum vanishes modulo two.

**4.2.** \(N_k-N_{k-1}=\frac{k(k+1)-(k-1)k}2=k\), and \(1+(k-1)+N_{k-1}-1=k+N_{k-1}-1=N_k-1\).

**4.3.** A subspace of dimension at least two meets every hyperplane, in particular \(x_0^\perp\), in a nonzero vector. Lines of \(x_0^\perp\) use only labels outside \(S(x_0)=I\), by admissibility; lines of the positive spectral subspace use only labels in \(I\), because the positive coordinates of \(F_V(A)\) are exactly those in \(I\). A line in both would have empty support. This uses that \(x_0\) witnesses \(I\) exactly.

**4.4.** By Theorem 2.1 the facets are triangles, by Proposition 1.1 all fifteen pairs are faces, and by Theorem 3.3 each pair lies in at least two triangles. Each triangle contains three pairs, so there are at least \(2\cdot15/3=10\) triangles.

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
- [Hat] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002 (author's page). https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
