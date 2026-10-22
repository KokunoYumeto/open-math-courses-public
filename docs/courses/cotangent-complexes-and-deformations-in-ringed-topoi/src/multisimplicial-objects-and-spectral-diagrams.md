# Multisimplicial objects and spectral diagrams

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A functor \(F\) between abelian categories that is not additive has derived functors that depend on the degree in which its argument is placed. Dold and Puppe showed that the groups \(H_{i+n}F(X[n])\) become independent of \(n\) once \(n>i\). The limit values are the stable homology groups of \(F\). Illusie collected the suspensions of all orders into a single object, a *spectral diagram*. This is a family of \(n\)-simplicial objects, one for each \(n\geq0\), connected by maps into their faces of degree one. The spectrum of an abelian group is the family of its iterated nerves. Applying a functor to a spectrum, killing the faces of degree zero and translating down gives a *large simplicial diagram*. Its derived colimit over the category of finite ordinals and injective maps is the stabilized functor.

This lesson sets up these objects: reduced multisimplicial objects and their translations; the categories of large simplicial and spectral diagrams and the equivalence between them; iterated nerves of abelian group objects and the characterization of their spectra; and the derived categories of large simplicial and spectral diagrams, with their adjunction formulas. The stabilization of functors is constructed in [*Stabilization of non-additive functors*](stabilization-of-non-additive-functors.md).

**Prerequisites.** [*Derived colimits over a small category*](derived-colimits-over-a-small-category.md); Section 1 and Proposition 3.1 of [*Strict simplicial objects and Deligne's contractibility theorem*](strict-simplicial-objects-and-deligne-s-contractibility-theorem.md); Corollary 2.2 and Propositions 2.4 and 2.6 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md); Theorems 1.1–1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution) (normalization, Dold–Kan, Eilenberg–Zilber). From the AI-integrated Stacks project: Dold–Kan in abelian categories [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)]; derived functors computed by acyclic objects [[Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution), [Tag 05T9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-acyclics), [Tag 05TA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-proposition-enough-acyclics)] and their adjunctions [[Tag 0DVC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors)]; right adjoints of exact functors preserve injectives [[Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)].

## Conventions

\(\mathcal A\) is an abelian category. For \(n\geq0\), \(\operatorname{Simpl}_n(\mathcal A)\) is the category of *\(n\)-simplicial objects*, the functors \((\Delta^{\mathrm{op}})^n\to\mathcal A\). Their coordinates are numbered \(0,\ldots,n-1\), the elements of \([n-1]\), and \(X(p_0,\ldots,p_{n-1})\) is the value at \(([p_0],\ldots,[p_{n-1}])\). Thus \(\operatorname{Simpl}_0(\mathcal A)=\mathcal A\) and \(\operatorname{Simpl}_1(\mathcal A)=\operatorname{Simpl}(\mathcal A)\). We write \(\mathbf 0=(0,\ldots,0)\) and \(\mathbf 1=(1,\ldots,1)\).

An *\(n\)-complex* \(C\) is a family \((C_q)_{q\in\mathbb N^n}\) of objects with differentials \(\partial_k\colon C_q\to C_{q-e_k}\), one for each coordinate, such that \(\partial_k\partial_k=0\) and \(\partial_k\partial_l=\partial_l\partial_k\); terms with a negative index are \(0\). They form an abelian category \(C_n(\mathcal A)\). The *total complex* \(\operatorname{Tot}C\) is the chain complex with \((\operatorname{Tot}C)_m=\bigoplus_{|q|=m}C_q\), where \(|q|=q_0+\cdots+q_{n-1}\), and differential \(\sum_k(-1)^{q_0+\cdots+q_{k-1}}\partial_k\). For \(r\in\mathbb Z^n\), the *translate* \(C[r]\) is given by \(C[r]_q=C_{q-r}\), with the same differentials, when this is again concentrated in \(\mathbb N^n\).

The *normalization* \(NX\) of \(X\in\operatorname{Simpl}_n(\mathcal A)\) is the \(n\)-complex obtained by applying the Moore normalization \(N_pV=\bigcap_{j=1}^p\ker d_j\), with differential \(d_0\), in each coordinate. Normalizations in different coordinates commute, because faces in different coordinates commute. \(\Gamma\colon C_n(\mathcal A)\to\operatorname{Simpl}_n(\mathcal A)\) is the Dold–Kan construction applied in each coordinate.

## 1. Reduced multisimplicial objects

**Lemma 1.1 (multisimplicial Dold–Kan).** \(N\colon\operatorname{Simpl}_n(\mathcal A)\to C_n(\mathcal A)\) is an equivalence with quasi-inverse \(\Gamma\). We have \(N\Gamma=1\) and a natural isomorphism \(\Gamma N\cong1\). Both functors are exact.

**Proof.** For \(n=1\) this is the Dold–Kan correspondence [Stacks, Tag 019G]. The formulas of Theorems 1.1 and 1.2 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex) use only finite direct sums and integer combinations of faces and degeneracies. So \(N\Gamma=1\) and \(\Gamma N\cong1\) hold in every abelian category. For \(n\geq2\), write \(\operatorname{Simpl}_n(\mathcal A)=\operatorname{Simpl}(\operatorname{Simpl}_{n-1}(\mathcal A))\), the last coordinate being the outer one, and \(C_n(\mathcal A)=C_1(C_{n-1}(\mathcal A))\). Normalizing in the last coordinate is an equivalence by the case \(n=1\) in the abelian category \(\operatorname{Simpl}_{n-1}(\mathcal A)\). Normalizing the other coordinates termwise is an equivalence by induction. An equivalence between abelian categories is exact. \(\square\)

**Faces.** Let \(\delta\colon[m-1]\to[n-1]\) be an injective increasing map, an arrow of the category \(\bar\Delta'\) of the lesson on strict simplicial objects, and let \(a\geq0\). Let \(\delta_a\colon(\Delta^{\mathrm{op}})^m\to(\Delta^{\mathrm{op}})^n\) put the \(k\)-th coordinate in position \(\delta(k)\) and \([a]\) in every position outside the image of \(\delta\). For \(X\in\operatorname{Simpl}_n(\mathcal A)\) put
\[
\partial^a_\delta X=X\circ\delta_a\in\operatorname{Simpl}_m(\mathcal A).
\]
For the coface \(\delta^i\colon[n-2]\to[n-1]\) omitting \(i\), this is the *\(i\)-th face of degree \(a\)*, written \(\partial^a_iX\): the \(i\)-th coordinate is fixed at \([a]\). Since \((\varepsilon\delta)_a=\varepsilon_a\delta_a\), we have \(\partial^a_{\varepsilon\delta}=\partial^a_\delta\partial^a_\varepsilon\).

An \(n\)-simplicial object \(X\) is *reduced* if \(\partial^0_iX=0\) for every \(i\). Every object of \(\operatorname{Simpl}_0(\mathcal A)=\mathcal A\) is reduced. The reduced objects form a full subcategory \(\operatorname{Simpl}_n(\mathcal A)_{\mathrm{red}}\).

**Faces of degree zero as subobjects.** Let \(c_i\) make an \((n-1)\)-simplicial object constant in a new \(i\)-th coordinate. The unique maps \([p]\to[0]\) of \(\Delta\) give a map \(\iota_i\colon c_i\partial^0_iX\to X\), which in each multidegree is an iterated degeneracy \(X(\ldots,0,\ldots)\to X(\ldots,p_i,\ldots)\). A vertex \([0]\to[p_i]\) gives a left inverse in each multidegree, so \(\iota_i\) is a monomorphism. Put
\[
\partial^0X=\sum_i\operatorname{im}\iota_i,\qquad X^{\mathrm{red}}=X/\partial^0X.
\]
For an \(n\)-complex \(C\), let \(C_{\geq\mathbf 1}\) be its quotient by the subcomplex of the terms with some \(q_i=0\). So \((C_{\geq\mathbf 1})_q=C_q\) when every \(q_i\geq1\), and \(0\) otherwise.

**Lemma 1.2.** Let \(X\in\operatorname{Simpl}_n(\mathcal A)\).

1. \(N(\partial^0_iX)\) is the restriction of \(NX\) to the hyperplane \(q_i=0\), and \(N(\iota_i)\) is the inclusion of this hyperplane in \(NX\).
2. \(X\) is reduced if and only if \(NX=(NX)_{\geq\mathbf 1}\).
3. \(N(X^{\mathrm{red}})=(NX)_{\geq\mathbf 1}\). The functor \(X\mapsto X^{\mathrm{red}}\) is exact and left adjoint to the inclusion of \(\operatorname{Simpl}_n(\mathcal A)_{\mathrm{red}}\).
4. Let \(\delta\colon[m-1]\to[n-1]\), and suppose \(\partial^0_lX=0\) for every \(l\) outside the image of \(\delta\). Then \(N(\partial^1_\delta X)\) is the restriction of \(NX\) to the multidegrees with \(q_l=1\) for every \(l\) outside the image of \(\delta\).
5. For \(\delta\colon[m-1]\to[n-1]\) and \(a\geq0\), \(\partial^0(\partial^a_\delta X)\subseteq\partial^a_\delta(\partial^0X)\). This gives a canonical epimorphism \((\partial^a_\delta X)^{\mathrm{red}}\to\partial^a_\delta(X^{\mathrm{red}})\), natural in \(X\).

**Proof.** (1) In the Moore model, normalizing a simplicial object changes nothing in degree \(0\), and the normalization of a constant simplicial object is its degree-\(0\) term placed in degree \(0\). Normalizing the other coordinates commutes with fixing the \(i\)-th. So \(N(\partial^0_iX)\) is the part of \(NX\) with \(q_i=0\), and \(N(c_i\partial^0_iX)\) is that part placed in \(q_i=0\). In degree \(0\) of the \(i\)-th coordinate, \(\iota_i\) is the identity of \(X(\ldots,0,\ldots)\).

(2) By (1), since an object \(Y\) of \(\operatorname{Simpl}_{n-1}(\mathcal A)\) is \(0\) exactly when \(NY=0\).

(3) \(N\) is exact (Lemma 1.1), so \(N(\partial^0X)\) is the sum of the images of the \(N(\iota_i)\), the part of \(NX\) on the hyperplanes \(q_i=0\), and \(N(X^{\mathrm{red}})\) is the quotient \((NX)_{\geq\mathbf 1}\). The functor \(C\mapsto C_{\geq\mathbf 1}\) is exact, and so is \(X\mapsto X^{\mathrm{red}}\). The object \(X^{\mathrm{red}}\) is reduced by (2). If \(Y\) is reduced and \(f\colon X\to Y\), then \(f\iota_i=\iota_i\circ c_i\partial^0_i(f)=0\), because \(\partial^0_iY=0\). So \(f\) factors uniquely through \(X^{\mathrm{red}}\).

(4) In the Moore model \(N_1V=\ker(d_1\colon V_1\to V_0)\), which is \(V_1\) when \(V_0=0\). Apply this in each coordinate outside the image of \(\delta\), and commute with the normalizations in the other coordinates.

(5) The functor \(\partial^a_\delta\) is exact and commutes with sums of subobjects. For \(k\in[m-1]\), the face \(\partial^0_k(\partial^a_\delta X)\) fixes the coordinate \(\delta(k)\) at \([0]\) and the coordinates outside the image of \(\delta\) at \([a]\), and its map \(\iota_k\) is the restriction of \(\iota_{\delta(k)}\) for \(X\). So \(\operatorname{im}\iota_k\subseteq\partial^a_\delta(\operatorname{im}\iota_{\delta(k)})\), and summing over \(k\) gives the inclusion. The epimorphism is
\[
\begin{aligned}&(\partial^a_\delta X)^{\mathrm{red}} =\partial^a_\delta X/\partial^0(\partial^a_\delta X)\\&\quad \to\partial^a_\delta X/\partial^a_\delta(\partial^0X)\\&\quad =\partial^a_\delta(X^{\mathrm{red}}).\qquad\square\end{aligned}
\]

The epimorphism of (5) need not be an isomorphism. For \(n=1\), let \(X\) be the constant simplicial object with value \(M\ne0\), \(\delta\colon[-1]\to[0]\) and \(a=1\). Then \(\partial^1_\delta X=M\) is an object, equal to its reduction, while \(X^{\mathrm{red}}=0\).

**Translations.** For \(r\in\mathbb N^n\) and \(X\in\operatorname{Simpl}_n(\mathcal A)\), put \(X[r]=\Gamma((NX)[r])\). If \(X\) is reduced, \((NX)[-\mathbf 1]\) is concentrated in \(\mathbb N^n\) by Lemma 1.2 (2), and we put \(X[-\mathbf 1]=\Gamma((NX)[-\mathbf 1])\).

**Proposition 1.3.**

1. \(X[\mathbf 1]\) is reduced, and \(X\mapsto X[\mathbf 1]\) and \(X'\mapsto X'[-\mathbf 1]\) are quasi-inverse equivalences between \(\operatorname{Simpl}_n(\mathcal A)\) and \(\operatorname{Simpl}_n(\mathcal A)_{\mathrm{red}}\).
2. Let \(\delta\colon[m-1]\to[n-1]\) and \(Y\in\operatorname{Simpl}_n(\mathcal A)\). Then \(\partial^1_\delta(Y[\mathbf 1])\) is reduced, and there is a canonical isomorphism
\[
\bigl(\partial^1_\delta(Y[\mathbf 1])\bigr)[-\mathbf 1]\cong\partial^0_\delta Y,
\]
natural in \(Y\). For \(\varepsilon\colon[n-1]\to[l-1]\), the isomorphisms for \(\varepsilon\delta\), \(\varepsilon\) and \(\delta\) are compatible through \(\partial_{\varepsilon\delta}=\partial_\delta\partial_\varepsilon\).
3. There are bijections, natural in \(X\in\operatorname{Simpl}_m(\mathcal A)\), \(X'\in\operatorname{Simpl}_m(\mathcal A)_{\mathrm{red}}\), \(Y\in\operatorname{Simpl}_n(\mathcal A)\) and \(Y'\in\operatorname{Simpl}_n(\mathcal A)_{\mathrm{red}}\):
\[
\begin{gathered}\operatorname{Hom}(X,\partial^0_\delta Y)\\ \cong\operatorname{Hom}\bigl(X[\mathbf 1],\partial^1_\delta(Y[\mathbf 1])\bigr),\\\operatorname{Hom}(X',\partial^1_\delta Y')\\ \cong\operatorname{Hom}\bigl(X'[-\mathbf 1],\partial^0_\delta(Y'[-\mathbf 1])\bigr).\end{gathered}
\]

**Proof.** (1) \(N(X[\mathbf 1])=(NX)[\mathbf 1]\) vanishes on the hyperplanes \(q_i=0\), so \(X[\mathbf 1]\) is reduced by Lemma 1.2 (2). Since \(N\Gamma=1\), the normalizations of \(X[\mathbf 1][-\mathbf 1]\) and \(X'[-\mathbf 1][\mathbf 1]\) are \(NX\) and \(NX'\). Apply \(\Gamma N\cong1\).

(2) The object \(Y[\mathbf 1]\) is reduced, with normalization \((NY)[\mathbf 1]\). By Lemma 1.2 (4), \(N(\partial^1_\delta(Y[\mathbf 1]))\) is the restriction of \((NY)[\mathbf 1]\) to \(q_l=1\) for \(l\) outside the image of \(\delta\). This is the restriction of \(NY\) to \(q_l=0\) for those \(l\), translated by \(\mathbf 1\) in the remaining \(m\) coordinates. By Lemma 1.2 (1), applied to one coordinate at a time, it is \(N(\partial^0_\delta Y)[\mathbf 1]\). This vanishes on hyperplanes, so \(\partial^1_\delta(Y[\mathbf 1])\) is reduced. The normalization of its translate by \(-\mathbf 1\) is \(N(\partial^0_\delta Y)\). Apply \(\Gamma N\cong1\). On normalizations the isomorphism is an identity, which gives naturality and the compatibility with composition.

(3) Combine (1) and (2). \(\square\)

## 2. Large simplicial diagrams and spectral diagrams

**Definition 2.1.** Let \(a\in\{0,1\}\). A *large diagram of type \(a\)* in \(\mathcal A\) is a family \(X=(X^{(n)})_{n\geq0}\) with \(X^{(n)}\in\operatorname{Simpl}_n(\mathcal A)\), together with a map
\[
X_\delta\colon X^{(m)}\to\partial^a_\delta X^{(n)}
\]
for every arrow \(\delta\colon[m-1]\to[n-1]\) of \(\bar\Delta'\), such that \(X_{\mathrm{id}}=1\) and \(X_{\varepsilon\delta}=\partial^a_\delta(X_\varepsilon)\circ X_\delta\). A morphism is a family of maps commuting with the \(X_\delta\). For \(a=0\) these are the *large simplicial diagrams*, forming the category \(\operatorname{SIMPL}(\mathcal A)\). For \(a=1\) they are the *spectral diagrams*, forming \(\operatorname{SPEC}(\mathcal A)\).

The definition makes sense in any category \(\mathcal A\). Since \(\bar\Delta'\) is generated by the cofaces with the relations \(\delta^j\delta^i=\delta^i\delta^{j-1}\) for \(i<j\) (facts (1) and (3) of Section 1 of the lesson on strict simplicial objects), a large diagram is determined by the maps \(d^i=X_{\delta^i}\colon X^{(m)}\to\partial^a_iX^{(m+1)}\), \(0\le i\le m\).

Large diagrams are functors on a small category. Let \(\mathbb S_a\) have as objects the pairs \((m,p)\) with \(m\geq0\) and \(p\in(\Delta^{\mathrm{op}})^m\). An arrow \((m,p)\to(n,p')\) is a pair \((\delta,u)\) of an arrow \(\delta\colon[m-1]\to[n-1]\) of \(\bar\Delta'\) and an arrow \(u\colon\delta_a(p)\to p'\) of \((\Delta^{\mathrm{op}})^n\). Composition is \((\varepsilon,v)(\delta,u)=(\varepsilon\delta,v\circ\varepsilon_a(u))\). A functor \(X\colon\mathbb S_a\to\mathcal A\) gives the multisimplicial objects \(X^{(m)}=X(m,-)\) and the maps \((X_\delta)_p=X(\delta,1_{\delta_a(p)})\). The functoriality of \(X\) is exactly the naturality of the \(X_\delta\) and the composition rule. So
\[
\begin{gathered}\operatorname{SIMPL}(\mathcal A)=\mathcal A^{\mathbb S_0},\\ \operatorname{SPEC}(\mathcal A)=\mathcal A^{\mathbb S_1}.\end{gathered}
\]
For \(\mathcal A\) abelian these are abelian categories in which kernels, cokernels, limits and colimits are computed objectwise.

**Lemma 2.2.** Let \(I\) be a small category and \(\mathcal A\) an abelian category with products and enough injectives. Then \(\mathcal A^I\) has enough injectives.

**Proof.** For an object \(i\), the evaluation \(\Phi\mapsto\Phi(i)\) is exact. It has the right adjoint \(R_i(J)(k)=\prod_{\operatorname{Hom}_I(k,i)}J\): by the Yoneda lemma, a map \(\Phi\to R_i(J)\) is the same as a map \(\Phi(i)\to J\). So \(R_i\) preserves injectives [Stacks, Tag 015Z]. Choose monomorphisms \(\Phi(i)\to J_i\) into injectives. The induced map \(\Phi\to\prod_iR_i(J_i)\) is a monomorphism: at \(k\), one of its components is \(\Phi(k)\to J_k\), indexed by the identity of \(k\). \(\square\)

**Trivial diagrams.** For \(M\in\mathcal A\), the constant functor \(\mathbb S_0\to\mathcal A\) with value \(M\) is the *trivial* large simplicial diagram \(cM\): every \(X^{(n)}\) is constant with value \(M\), and every structure map is the identity.

**Lemma 2.3.** The functor \(c\colon\mathcal A\to\operatorname{SIMPL}(\mathcal A)\) is fully faithful. Its essential image consists of the large simplicial diagrams whose structure maps are all isomorphisms: every \(X^{(n)}\) sends every arrow to an isomorphism, and every \(X_\delta\) is an isomorphism.

**Proof.** Let \(o_n=(0,\ldots,0)\in(\Delta^{\mathrm{op}})^n\). It is an initial object, because \([0]\) is final in \(\Delta\), and \(\delta_0(o_m)=o_n\). The objects \((n,o_n)\) and the arrows \((\delta,1)\) form a subcategory \(D\) of \(\mathbb S_0\) isomorphic to \(\bar\Delta'\). The functor \(r\colon\mathbb S_0\to D\) with \(r(n,p)=(n,o_n)\) and \(r(\delta,u)=(\delta,1)\) restricts to the identity of \(D\). The unique arrows \((n,o_n)\to(n,p)\) form a natural transformation from \(r\) to the identity: for \((\delta,u)\colon(n,p)\to(n',p')\), both composites \((n,o_n)\to(n',p')\) have first component \(\delta\) and second component an arrow out of the initial object \(o_{n'}\). Every object receives an arrow from \((0,o_0)\), so \(\mathbb S_0\) is connected and \(c\) is fully faithful. If \(X\) sends every arrow to an isomorphism, the transformation gives \(X\cong X\circ r\). The restriction of \(X\) to \(D\cong\bar\Delta'\) is locally constant, hence isomorphic to a constant functor by Proposition 3.1 of the lesson on strict simplicial objects. So \(X\) is isomorphic to a constant functor. \(\square\)

**Reduced spectral diagrams.** A spectral diagram \(X\) is *reduced* if every \(X^{(n)}\) is reduced; these form a full subcategory \(\operatorname{SPEC}(\mathcal A)_{\mathrm{red}}\). For \(X\) reduced and \(\delta\colon[m-1]\to[n-1]\), the object \(\partial^1_\delta X^{(n)}\) is reduced, because its faces of degree \(0\) are faces of degree \(0\) of \(X^{(n)}\).

**Proposition 2.4.** There are quasi-inverse exact equivalences
\[
\begin{gathered}
\operatorname{SPEC}(\mathcal A)_{\mathrm{red}}\rightleftarrows\operatorname{SIMPL}(\mathcal A),\\
X\mapsto X(-1),\qquad Y\mapsto Y(1),
\end{gathered}
\]
with \(X(-1)^{(n)}=X^{(n)}[-\mathbf 1]\) and \(Y(1)^{(n)}=Y^{(n)}[\mathbf 1]\). The structure map \(X(-1)_\delta\) corresponds to \(X_\delta\) under the second bijection of Proposition 1.3 (3), and \(Y(1)_\delta\) corresponds to \(Y_\delta\) under the first.

**Proof.** The bijections of Proposition 1.3 (3) are natural and compatible with composition by Proposition 1.3 (2), so \(X(-1)\) and \(Y(1)\) satisfy the composition rule of Definition 2.1. They are quasi-inverse by Proposition 1.3 (1). Both are exact because \(N\), \(\Gamma\) and translations are. \(\square\)

**Proposition 2.5.** The inclusion \(\operatorname{SPEC}(\mathcal A)_{\mathrm{red}}\subseteq\operatorname{SPEC}(\mathcal A)\) has an exact left adjoint \(X\mapsto X^{\mathrm{red}}\). Here \((X^{\mathrm{red}})^{(n)}=(X^{(n)})^{\mathrm{red}}\), and the structure map for \(\delta\colon[m-1]\to[n-1]\) is the composite
\[
\begin{aligned}
(X^{(m)})^{\mathrm{red}}&\xrightarrow{(X_\delta)^{\mathrm{red}}}(\partial^1_\delta X^{(n)})^{\mathrm{red}}\\
&\longrightarrow\partial^1_\delta\bigl((X^{(n)})^{\mathrm{red}}\bigr)
\end{aligned}
\]
with the epimorphism of Lemma 1.2 (5). For \(X\in\operatorname{SPEC}(\mathcal A)\) and \(Y\in\operatorname{SIMPL}(\mathcal A)\) there is a natural bijection
\[
\begin{aligned}
&\operatorname{Hom}_{\operatorname{SPEC}(\mathcal A)}(X,Y(1))\\
&\quad\cong\operatorname{Hom}_{\operatorname{SIMPL}(\mathcal A)}\bigl(X^{\mathrm{red}}(-1),Y\bigr).
\end{aligned}
\]

**Proof.** The structure maps of \(X^{\mathrm{red}}\) are induced on quotients by those of \(X\). Since the quotient maps are epimorphisms, they satisfy the composition rule. Exactness holds componentwise by Lemma 1.2 (3). A map from \(X\) to a reduced spectral diagram factors uniquely through \(X^{\mathrm{red}}\) in each component (Lemma 1.2 (3)), and the factorizations commute with the structure maps, again because \(X^{(m)}\to(X^{(m)})^{\mathrm{red}}\) is an epimorphism. The last bijection is \(\operatorname{Hom}(X,Y(1))=\operatorname{Hom}(X^{\mathrm{red}},Y(1))\), since \(Y(1)\) is reduced, followed by Proposition 2.4. \(\square\)

**The diagonal and the total complex.** For \(Z\in\operatorname{Simpl}_n(\mathcal A)\), the *diagonal* \(\operatorname{diag}Z\in\operatorname{Simpl}(\mathcal A)\) has \((\operatorname{diag}Z)_p=Z(p,\ldots,p)\); for \(n=0\) it is the constant simplicial object. For \(\delta\colon[m-1]\to[n-1]\), the maps \([p]\to[0]\) in the coordinates outside the image of \(\delta\) give the *face inclusion*
\[
j_\delta\colon\operatorname{diag}\partial^0_\delta Z\to\operatorname{diag}Z.
\]
On normalizations there is also the inclusion \(t_\delta\colon\operatorname{Tot}N\partial^0_\delta Z\to\operatorname{Tot}NZ\) of the terms with \(q_l=0\) for \(l\) outside the image of \(\delta\) (Lemma 1.2 (1)). It is a chain map, because inserting coordinates equal to \(0\) changes none of the signs in the differential of \(\operatorname{Tot}\).

For \(X\in\operatorname{SIMPL}(\mathcal A)\), define functors \(\Delta X\colon\bar\Delta'\to\operatorname{Simpl}(\mathcal A)\) and \(\int NX\colon\bar\Delta'\to C_{\geq0}(\mathcal A)\), the latter with values in chain complexes, by
\[
\begin{gathered}
\Delta X([n-1])=\operatorname{diag}X^{(n)},\\
{\textstyle\int}NX([n-1])=\operatorname{Tot}NX^{(n)}.
\end{gathered}
\]
For \(\delta\colon[m-1]\to[n-1]\), the maps are \(j_\delta\circ\operatorname{diag}(X_\delta)\) and \(t_\delta\circ\operatorname{Tot}N(X_\delta)\).

**Lemma 2.6 (Eilenberg–Zilber for multisimplicial objects).** For \(Z\in\operatorname{Simpl}_n(\mathcal A)\) there are chain maps
\[
\begin{gathered}
\operatorname{AW}_Z\colon N\operatorname{diag}Z\to\operatorname{Tot}NZ,\\
\operatorname{sh}_Z\colon\operatorname{Tot}NZ\to N\operatorname{diag}Z,
\end{gathered}
\]
natural in \(Z\), which are mutually inverse homotopy equivalences. They commute with the face inclusions: \(\operatorname{AW}_Z\circ N(j_\delta)=t_\delta\circ\operatorname{AW}_{\partial^0_\delta Z}\) and \(\operatorname{sh}_Z\circ t_\delta=N(j_\delta)\circ\operatorname{sh}_{\partial^0_\delta Z}\).

**Proof.** For \(n=2\) and bisimplicial modules over a ring this is Theorem 1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex), whose proof constructs natural homotopies. The Alexander–Whitney and shuffle maps are integer combinations of composites of faces and degeneracies, and so are the homotopies. Indeed, the normalized terms are images of natural idempotents of this form (Theorem 1.1 there). A natural map from \(Z\mapsto Z(p,q)\) to \(Z\mapsto Z(p',q')\) on bisimplicial abelian groups is an integer combination of the operators of pairs of maps \([p']\to[p]\), \([q']\to[q]\). This is the Yoneda lemma for the free bisimplicial abelian group on the bisimplicial set \((k,l)\mapsto\operatorname{Hom}([k],[p])\times\operatorname{Hom}([l],[q])\), which represents \(Z\mapsto Z(p,q)\). The same combinations define maps and homotopies for bisimplicial objects of \(\mathcal A\). The identities between them hold in \(\mathcal A\), because they hold after applying \(\operatorname{Hom}_{\mathcal A}(M,-)\) for every object \(M\). For \(n\geq3\), apply the case \(n=2\) to the bisimplicial object \((p,p')\mapsto Z(p,\ldots,p,p')\), diagonal in the first \(n-1\) coordinates, and then the case \(n-1\) in the first coordinate, termwise.

For the face inclusions, \(j_\delta\) is the diagonal of the map \(c_\delta\partial^0_\delta Z\to Z\) of \(n\)-simplicial objects, where \(c_\delta\) makes the coordinates outside the image of \(\delta\) constant. By naturality it suffices to compare the maps for \(c_\delta W\) with those for \(W\). The diagonals of \(c_\delta W\) and \(W\) coincide, and so do \(\operatorname{Tot}Nc_\delta W\) and \(\operatorname{Tot}NW\), because a constant coordinate contributes only its degree \(0\). In the case \(n=2\) with a constant coordinate, the Alexander–Whitney map is the identity, since the vertex maps of a constant coordinate are identities. The shuffle map is the identity too, since a degree-\(0\) element has only the trivial shuffle. Induction on \(n\) gives the general case. \(\square\)

**Proposition 2.7.** For \(X\in\operatorname{SIMPL}(\mathcal A)\), the maps \(\operatorname{AW}_{X^{(n)}}\) and \(\operatorname{sh}_{X^{(n)}}\) form natural transformations \(N\Delta X\rightleftarrows\int NX\) of functors \(\bar\Delta'\to C_{\geq0}(\mathcal A)\). These are homotopy equivalences at every object and natural in \(X\).

**Proof.** Lemma 2.6 gives naturality with respect to \(\operatorname{diag}(X_\delta)\) and compatibility with the face inclusions. \(\square\)

## 3. Spectra of abelian group objects

Let \(T\) be a category with finite products and final object \(e\). For a group object \(G\) of \(T\), its *nerve* \(\operatorname{Ner}(G)\) is the simplicial object with \(\operatorname{Ner}(G)_p=G^p\). On points with values in any object, for \(g=(g_1,\ldots,g_p)\), the faces and degeneracies are
\[
\begin{gathered}d_0g=(g_2,\ldots,g_p),\\ d_pg=(g_1,\ldots,g_{p-1}),\\ d_ig\\ =(g_1,\ldots,g_{i+1}g_i,\ldots,g_p)\ (0<i<p),\\ s_ig=(g_1,\ldots,g_i,1,g_{i+1},\ldots,g_p).\end{gathered}
\]
It is the nerve of \(G\) regarded as an internal category with object of objects \(e\).

**Proposition 3.1.** The functor \(\operatorname{Ner}\colon\operatorname{Group}(T)\to\operatorname{Simpl}(T)\) is fully faithful. Its essential image consists of the \(X\) such that (i) \(X_0\to e\) is an isomorphism; (ii) for \(p\geq2\) the Segal map \(X_p\to X_1\times\cdots\times X_1\), given by the edges \((i-1,i)\), is an isomorphism; (iii) \((d_1,d_2)\colon X_2\to X_1\times X_1\) is an isomorphism. In (iii), \((d_1,d_0)\) may replace \((d_1,d_2)\).

**Proof.** By Proposition 2.4 of the lesson on décalage, the nerve is fully faithful on internal categories, with essential image characterized by the Segal condition. Internal functors between internal categories with object of objects \(e\) are homomorphisms of monoids, and condition (i) says that the object of objects is \(e\). By Proposition 2.6 there, condition (iii) or its variant says that the category is a groupoid, that is, the monoid is a group. These propositions are stated for categories with finite limits. Their proofs reduce to sets through the functors \(\operatorname{Hom}(S,-)\) and use only fibre products over \(X_0\), which are products when \(X_0=e\). \(\square\)

**Iterated nerves.** Let \(T^{\mathrm{ab}}\) be the category of commutative group objects of \(T\). For \(G\in T^{\mathrm{ab}}\), the faces and degeneracies of \(\operatorname{Ner}(G)\) are homomorphisms, so \(\operatorname{Ner}(G)\) is a commutative group object of \(\operatorname{Simpl}(T)\). Define \(G\langle0\rangle=G\) and \(G\langle n\rangle=\operatorname{Ner}(G\langle n-1\rangle)\), the nerve of the commutative group object \(G\langle n-1\rangle\) of \(\operatorname{Simpl}_{n-1}(T)\), placed in the last coordinate. Concretely, \(G\langle n\rangle(p_0,\ldots,p_{n-1})\) is the product of copies of \(G\) indexed by \(\{1,\ldots,p_0\}\times\cdots\times\{1,\ldots,p_{n-1}\}\), and in each coordinate the faces and degeneracies act by the formulas of the nerve.

**Lemma 3.2 (Eckmann–Hilton).** Let \(G\) be a group object of \(T\) with law \(\mu\), and let \(\mu'\) be a second group law on \(G\) which is a homomorphism \((G,\mu)\times(G,\mu)\to(G,\mu)\). Then \(\mu'=\mu\), and \(\mu\) is commutative.

**Proof.** It suffices to argue on points, writing \(xy\) for \(\mu\) and \(x\ast y\) for \(\mu'\). The hypothesis is \((ab)\ast(cd)=(a\ast c)(b\ast d)\). Let \(1\) and \(1'\) be the units. Then \(1'=\) \(1'\ast1'=\) \((1'1)\ast(11')=\) \((1'\ast1)(1\ast1')=\) \(11=\) \(1\). Hence \(a\ast d=(a1)\ast(1d)=(a\ast1)(1\ast d)=ad\), and \(bc=(1b)\ast(c1)=(1\ast c)(b\ast1)=cb\). \(\square\)

**Proposition 3.3.** The functor \(G\mapsto G\langle n\rangle\), \(T^{\mathrm{ab}}\to\operatorname{Simpl}_n(T)\), is faithful, and fully faithful for \(n\geq1\). For \(n\geq2\) its essential image consists of the \(X\in\operatorname{Simpl}_n(T)\) such that every simplicial object obtained by fixing all coordinates but one satisfies (i)–(iii) of Proposition 3.1.

**Proof.** For \(n=0\) the functor forgets the group structure, which is faithful. For \(n\geq1\), the functor \(G\mapsto G\langle n-1\rangle\) is fully faithful as a functor to commutative group objects of \(\operatorname{Simpl}_{n-1}(T)\): for \(n=1\) because \(T^{\mathrm{ab}}\) is a full subcategory of \(\operatorname{Group}(T)\), and for \(n\geq2\) by induction, a map \(G\langle n-1\rangle\to H\langle n-1\rangle\) coming from a homomorphism and therefore preserving the group laws. By Proposition 3.1 in the category \(\operatorname{Simpl}_{n-1}(T)\), which has finite products computed objectwise, the nerve is fully faithful on its group objects. The composite is fully faithful.

Let \(n\geq2\) and let \(X\) satisfy the condition. The functors \(\operatorname{Hom}(S,-)\) commute with the products in (i)–(iii), so these conditions for a simplicial object of \(\operatorname{Simpl}_{n-1}(T)\) hold if and only if they hold objectwise. Regard \(X\) as a simplicial object of \(\operatorname{Simpl}_{n-1}(T)\) through its last coordinate. By hypothesis it satisfies (i)–(iii), so \(X\cong\operatorname{Ner}(Y)\) for a group object \(Y\) of \(\operatorname{Simpl}_{n-1}(T)\). The underlying object of \(Y\) is the face of \(X\) with last coordinate \([1]\), and it again satisfies the condition. If \(n=2\), Proposition 3.1 gives \(Y\cong\operatorname{Ner}(G)\) for a group \(G\) of \(T\). If \(n\geq3\), induction gives \(Y\cong G\langle n-1\rangle\) with \(G\in T^{\mathrm{ab}}\). In both cases the group law of \(Y\), a map \(Y\times Y\to Y\) of \((n-1)\)-simplicial objects, corresponds by full faithfulness to a homomorphism \(\mu'\colon G\times G\to G\), which is a group law on \(G\). By Lemma 3.2, \(\mu'\) is the law of \(G\) and \(G\) is commutative. So \(Y\cong G\langle n-1\rangle\) as group objects, and \(X\cong G\langle n\rangle\). Conversely every line of \(G\langle n\rangle\) is the nerve of a product of copies of \(G\). \(\square\)

For \(n=1\) the essential image is the class of nerves of commutative groups, which conditions (i)–(iii) do not describe: they hold for the nerve of every group (Exercise 6.2).

**Lemma 3.4.** Suppose \(T^{\mathrm{ab}}\) is an abelian category, and let \(G\in T^{\mathrm{ab}}\). Then \(N\operatorname{Ner}(G)\) is \(G\) placed in degree \(1\), and \(NG\langle n\rangle\) is \(G\) placed in multidegree \(\mathbf 1\). So \(G\langle n\rangle\cong G[\mathbf 1]\) canonically, where \(G\) is regarded as a constant \(n\)-simplicial object of \(T^{\mathrm{ab}}\).

**Proof.** In \(\operatorname{Ner}(G)\), the degree-\(0\) term is \(0\) and \(N_1=\ker(d_1\colon G\to0)=G\). Let \(p\geq2\) and let \(g\in N_p\) on points. Then \(d_pg=(g_1,\ldots,g_{p-1})=0\), and \(d_{p-1}g=\) \((0,\ldots,0,g_p+g_{p-1})=\) \((0,\ldots,0,g_p)=\) \(0\). So \(N_p=0\). For \(G\langle n\rangle\), normalize the last coordinate first, in the abelian category of \((n-1)\)-simplicial objects of \(T^{\mathrm{ab}}\), and then induct. The constant \(n\)-simplicial object \(G\) has normalization \(G\) in multidegree \(\mathbf 0\), so \(G[\mathbf 1]=\) \(\Gamma(G\text{ in multidegree }\mathbf 1)\cong\) \(\Gamma NG\langle n\rangle\cong\) \(G\langle n\rangle\). \(\square\)

**The spectrum of a commutative group object.** For \(G\in T^{\mathrm{ab}}\), let \(G(1)\in\operatorname{SPEC}(T)\) have components \(G(1)^{(n)}=G\langle n\rangle\). For \(\delta\colon[m-1]\to[n-1]\), fixing the coordinates of \(G\langle n\rangle\) outside the image of \(\delta\) at \([1]\) replaces the corresponding factors of the index set by one-element sets, so \(\partial^1_\delta G\langle n\rangle=G\langle m\rangle\). The structure maps are these identities. If \(T=\mathcal A\) is abelian, then \(\mathcal A^{\mathrm{ab}}=\mathcal A\), and \(G(1)\) is the spectral diagram \((cG)(1)\) of Proposition 2.4 for the trivial diagram \(cG\). Indeed, Lemma 3.4 identifies the components, and on normalizations both structure maps are the identity of \(G\) in multidegree \(\mathbf 1\).

**Proposition 3.5.** The functor \(G\mapsto G(1)\), \(T^{\mathrm{ab}}\to\operatorname{SPEC}(T)\), is fully faithful. Its essential image consists of the spectral diagrams \(X\) such that (i) for every \(n\geq1\), \(X^{(n)}\) is isomorphic to \(H\langle n\rangle\) for some \(H\in T^{\mathrm{ab}}\); (ii) every structure map \(X_\delta\) is an isomorphism.

**Proof.** A map \(f\colon G(1)\to H(1)\) consists of maps \(f^{(n)}\colon G\langle n\rangle\to H\langle n\rangle\) commuting with the structure maps. By Proposition 3.3, \(f^{(1)}=\varphi\langle1\rangle\) for a unique homomorphism \(\varphi\colon G\to H\). Compatibility with \(d^0\colon G(1)^{(0)}\to\partial^1_0G(1)^{(1)}\), both sides being \(G\), gives \(f^{(0)}=\varphi\). For \(n\geq1\), \(f^{(n)}=\varphi_n\langle n\rangle\), and compatibility with \(d^0\colon G\langle n\rangle\to\partial^1_0G\langle n+1\rangle\) gives \(\varphi_{n+1}=\varphi_n\). So \(f=\varphi(1)\).

Let \(X\) satisfy (i) and (ii). The face \(d^0\colon X^{(0)}\to\partial^1_0X^{(1)}\) is an isomorphism, so \(X^{(0)}\cong H_1\) where \(X^{(1)}\cong H_1\langle1\rangle\). Choose inductively isomorphisms \(\varphi_n\colon X^{(n)}\to G\langle n\rangle\) with \(G=H_1\), such that the transported face \(d^0\) is the identity. At each step the transported face \(d^0\colon G\langle n\rangle\to\partial^1_0X^{(n+1)}\) is an isomorphism. Together with \(X^{(n+1)}\cong H_{n+1}\langle n+1\rangle\) and full faithfulness, it gives an isomorphism \(G\cong H_{n+1}\) of group objects. Choose \(\varphi_{n+1}\) to make \(d^0\) the identity. After transport, each \(d^i\colon G\langle n\rangle\to G\langle n\rangle\) is an automorphism, so \(d^i=\alpha^{(n)}_i\langle n\rangle\) for automorphisms \(\alpha^{(n)}_i\) of \(G\), with \(\alpha^{(n)}_0=1\). The relation \(X_{\delta^j\delta^0}=X_{\delta^0\delta^{j-1}}\) for \(j\geq1\) gives \(\alpha^{(n+1)}_j=\alpha^{(n)}_{j-1}\). Hence \(\alpha^{(n)}_j=\alpha^{(n-j)}_0=1\), and \(X\cong G(1)\). Conversely \(G(1)\) satisfies (i) and (ii). \(\square\)

## 4. Derived categories and adjunction formulas

In this section \(\mathcal A\) is an abelian category with small colimits, exact filtered colimits, products and enough injectives. Modules over a ring of a topos form such a category. So do \(\mathcal A^I\) for a small category \(I\), and in particular \(\operatorname{SIMPL}(\mathcal A)\), \(\operatorname{SPEC}(\mathcal A)\) and \(\mathcal A^{\bar\Delta'}\), by Lemma 2.2 and the objectwise computation of colimits.

**Proposition 4.1.** For \(X\in D(\operatorname{SPEC}(\mathcal A))\) and \(Y\in D(\operatorname{SIMPL}(\mathcal A))\) there is a natural bijection
\[
\begin{aligned}
&\operatorname{Hom}_{D(\operatorname{SPEC}(\mathcal A))}(X,Y(1))\\
&\quad\cong\operatorname{Hom}_{D(\operatorname{SIMPL}(\mathcal A))}\bigl(X^{\mathrm{red}}(-1),Y\bigr),
\end{aligned}
\]
and for \(Y\in D^+(\operatorname{SIMPL}(\mathcal A))\) a natural isomorphism \(R\operatorname{Hom}(X,Y(1))\cong\) \(R\operatorname{Hom}(X^{\mathrm{red}}(-1),Y)\).

**Proof.** The functors \(X\mapsto X^{\mathrm{red}}(-1)\) and \(Y\mapsto Y(1)\) are exact (Propositions 2.4 and 2.5), so they act termwise on complexes and on derived categories. The unit and counit of the adjunction of Proposition 2.5 act termwise too, and satisfy the triangle identities. This gives the first bijection. The right adjoint \(Y\mapsto Y(1)\) of an exact functor preserves injectives [Stacks, Tag 015Z]. If \(J\) is a bounded below complex of injectives representing \(Y\), then \(J(1)\) is one representing \(Y(1)\), and
\[
\begin{aligned}&R\operatorname{Hom}(X,Y(1)) =\operatorname{Hom}^\bullet(X,J(1))\\&\quad =\operatorname{Hom}^\bullet\bigl(X^{\mathrm{red}}(-1),J\bigr).\qquad\square\end{aligned}
\]

**The functor \(H_0\).** Let \(\pi\colon\mathbb S_0\to\bar\Delta'\) be the functor \((n,p)\mapsto[n-1]\), \((\delta,u)\mapsto\delta\). For \(W\in\mathcal A^{\bar\Delta'}\), the large simplicial diagram \(\pi^*W=W\circ\pi\) has constant components \(W([n-1])\) and structure maps \(W(\delta)\). This embeds \(\mathcal A^{\bar\Delta'}\) in \(\operatorname{SIMPL}(\mathcal A)\). For \(X\in\operatorname{SIMPL}(\mathcal A)\), let \(H_0X\in\mathcal A^{\bar\Delta'}\) have the values \(H_0X([n-1])=\varinjlim_{(\Delta^{\mathrm{op}})^n}X^{(n)}\), with the maps induced by the \(X_\delta\).

**Lemma 4.2.**

1. For \(Z\in\operatorname{Simpl}_n(\mathcal A)\) there are natural isomorphisms \(\varinjlim_{(\Delta^{\mathrm{op}})^n}Z\cong\) \(H_0(\operatorname{Tot}NZ)\cong\) \(H_0(N\operatorname{diag}Z)\).
2. \(H_0\colon\operatorname{SIMPL}(\mathcal A)\to\mathcal A^{\bar\Delta'}\) is left adjoint to \(\pi^*\).

**Proof.** (1) Let \(V\) be a simplicial object. A cocone \((f_p\colon V_p\to M)\) is determined by \(f_0\), since \(f_p=f_0\circ V(v)\) for the vertex \(v\colon[0]\to[p]\), \(v(0)=0\). Conversely \(f_0\) extends to a cocone if \(f_0d_0=f_0d_1\): the two vertex maps of an edge are \(d_1\) and \(d_0\) of that edge, so \(f_0\circ V(v)\) does not depend on the vertex \(v\). Hence \(\varinjlim V=\operatorname{coker}(d_0-d_1\colon V_1\to V_0)\). In the Moore model \(H_0(NV)=V_0/d_0(\ker d_1)\), and this is the same quotient: for \(x\in V_1\), \(x-s_0d_1x\in\ker d_1\) and \(d_0(x-s_0d_1x)=d_0x-d_1x\). A colimit over a product of categories is an iterated colimit, and \(H_0(\operatorname{Tot}NZ)\) is the corresponding iterated cokernel of \((NZ)_{\mathbf 0}=Z(\mathbf 0)\). The last isomorphism is Lemma 2.6.

(2) A map \(X\to\pi^*W\) is a family of maps from the \(X^{(n)}\) to the constant objects \(W([n-1])\), that is, of maps \(\varinjlim X^{(n)}\to W([n-1])\), compatible with the structure maps. \(\square\)

Call \(Z\in\operatorname{Simpl}_n(\mathcal A)\) *colimit-acyclic* if it is colimit-acyclic as a diagram on \((\Delta^{\mathrm{op}})^n\) in the sense of Section 2 of the lesson on derived colimits. For a bounded above complex \(Z^\bullet\) of \(n\)-simplicial objects, let \(\operatorname{Tot}NZ^\bullet\) be the total complex in which \(NZ^q\) in multidegree \(r\) sits in cohomological degree \(q-|r|\).

**Lemma 4.3.** For every bounded above complex \(Z^\bullet\) of \(n\)-simplicial objects there is a natural isomorphism \(L\varinjlim_{(\Delta^{\mathrm{op}})^n}Z^\bullet\cong\operatorname{Tot}NZ^\bullet\) in \(D^-(\mathcal A)\). In particular \(Z\) is colimit-acyclic if and only if \(H_m(\operatorname{Tot}NZ)=0\) for all \(m>0\).

**Proof.** Let \(I=(\Delta^{\mathrm{op}})^n\). Since \(\operatorname{Hom}_I(p',p)=\prod_k\operatorname{Hom}_\Delta([p_k],[p'_k])\), an induced diagram of \(I\) is a sum of diagrams \(Y\otimes\mathbb Z(\Delta[p'_0]\times\cdots\times\Delta[p'_{n-1}])\), with \(Y\in\mathcal A\) and the free multisimplicial abelian group on the product of the standard simplices, one in each coordinate. Its normalization is \(Y\otimes N\mathbb Z(\Delta[p'_0])\otimes\cdots\otimes N\mathbb Z(\Delta[p'_{n-1}])\), normalized in separate coordinates. Each \(\Delta[p']\) is contractible (Corollary 2.2 of the lesson on décalage), so the augmentation \(N\mathbb Z(\Delta[p'])\to\mathbb Z\) is a chain homotopy equivalence, and so is the tensor product of these augmentations. Hence, for an induced diagram \(P\), the map \(\operatorname{Tot}NP\to\varinjlim P\) given by Lemma 4.2 (1) is a homotopy equivalence.

Choose a quasi-isomorphism \(P^\bullet\to Z^\bullet\) from a bounded above complex of induced diagrams [Stacks, Tag 05T7]. By Theorem 2.3 of the lesson on derived colimits, \(L\varinjlim Z^\bullet\cong\varinjlim P^\bullet\). The cone of \(\operatorname{Tot}NP^\bullet\to\varinjlim P^\bullet\) is the total complex of a double complex whose rows \(\operatorname{Tot}NP^q\to\varinjlim P^q\) are acyclic and which is bounded above in \(q\). The sums \(G_k\) of the rows \(q\geq Q-k\), where \(P^q=0\) for \(q>Q\), are subcomplexes, each acyclic by induction on \(k\), and their union is acyclic by exactness of filtered colimits, as in Lemma 2.2 of the lesson on derived colimits. The same argument, applied to the normalization of the cone of \(P^\bullet\to Z^\bullet\), whose rows are acyclic because \(N\) is exact, shows that \(\operatorname{Tot}NP^\bullet\to\operatorname{Tot}NZ^\bullet\) is a quasi-isomorphism. The resulting isomorphism does not depend on the choice of \(P^\bullet\), because the maps involved are natural. \(\square\)

**Proposition 4.4.** The functor \(H_0\) has a left derived functor \(LH_0\colon D^-(\operatorname{SIMPL}(\mathcal A))\to D^-(\mathcal A^{\bar\Delta'})\). There are natural isomorphisms
\[
LH_0X\cong\operatorname{Tot}{\textstyle\int}NX\cong\operatorname{Tot}N\Delta X,
\]
where \(\int N\) and \(N\Delta\) are applied termwise to the bounded above complex \(X\) and totalized as in Lemma 4.3.

**Proof.** Call \(X\in\operatorname{SIMPL}(\mathcal A)\) *\(H_0\)-acyclic* if every \(X^{(n)}\) is colimit-acyclic. The induced objects of \(\mathcal A^{\mathbb S_0}\) are \(H_0\)-acyclic: restricted to the objects \((n,p)\) with fixed \(n\), the induced object on \(Y\in\mathcal A^{\operatorname{Ob}\mathbb S_0}\) is the sum, over the objects \(b=(m,p')\) and the arrows \(\delta\colon[m-1]\to[n-1]\), of the induced diagrams \(Y_b\otimes\mathbb Z[\operatorname{Hom}_{(\Delta^{\mathrm{op}})^n}(\delta_0(p'),-)]\). Every object is a quotient of an induced one. The long exact sequences of \(L\varinjlim\) on each \((\Delta^{\mathrm{op}})^n\) show, as in the proof of Theorem 2.3 of the lesson on derived colimits, that the kernel of an epimorphism between \(H_0\)-acyclic objects is \(H_0\)-acyclic and that \(H_0\) is exact on short exact sequences of \(H_0\)-acyclic objects. By [Stacks, Tags 05T9, 05TA], \(LH_0\) exists and is computed by bounded above complexes of \(H_0\)-acyclic objects. For such a complex \(P\), Lemmas 4.2 (1) and 4.3 give quasi-isomorphisms \(\operatorname{Tot}\int NP\to H_0P\), natural in \(\bar\Delta'\). The functor \(\operatorname{Tot}\int N\) is exact and preserves quasi-isomorphisms, by the row filtration of Lemma 4.3. So for a resolution \(P\to X\), \(LH_0X=\) \(H_0P\cong\) \(\operatorname{Tot}\int NP\cong\) \(\operatorname{Tot}\int NX\). The second isomorphism is Proposition 2.7. \(\square\)

Let \(L\varinjlim\colon D^-(\operatorname{SIMPL}(\mathcal A))\to D^-(\mathcal A)\) be the composite of \(LH_0\) and the derived colimit \(L\varinjlim_{\bar\Delta'}\) of Theorem 2.3 of the lesson on derived colimits.

**Corollary 4.5 (adjunction formulas).** Let \(X\in D^-(\operatorname{SIMPL}(\mathcal A))\) and \(X'\in D^-(\operatorname{SPEC}(\mathcal A))\). There are natural bijections and isomorphisms
\[
\begin{aligned}
&\operatorname{Hom}_{D(\mathcal A^{\bar\Delta'})}(LH_0X,W)\\
&\quad\cong\operatorname{Hom}_{D(\operatorname{SIMPL}(\mathcal A))}(X,\pi^*W),\\
&\operatorname{Hom}_{D(\mathcal A)}(L\varinjlim X,M)\\
&\quad\cong\operatorname{Hom}_{D(\operatorname{SIMPL}(\mathcal A))}(X,cM),\\
&\operatorname{Hom}_{D(\mathcal A)}\bigl(L\varinjlim X'^{\mathrm{red}}(-1),M\bigr)\\
&\quad\cong\operatorname{Hom}_{D(\operatorname{SPEC}(\mathcal A))}\bigl(X',(cM)(1)\bigr),
\end{aligned}
\]
for \(W\in D(\mathcal A^{\bar\Delta'})\) and \(M\in D(\mathcal A)\). For \(W\) and \(M\) bounded below, the corresponding isomorphisms of \(R\operatorname{Hom}\) hold.

**Proof.** The functor \(\pi^*\) is exact, and its left adjoint \(H_0\) has the left derived functor \(LH_0\) on \(D^-\). So [Stacks, Tag 0DVC] gives the first bijection, as in Corollary 2.4 of the lesson on derived colimits. Composing with that corollary, applied to \(\bar\Delta'\), gives the second, since \(cM=\pi^*(\text{constant diagram }M)\). Composing with Proposition 4.1 gives the third. For \(R\operatorname{Hom}\), consider the composite of the map \(R\operatorname{Hom}(LH_0X,W)\to\) \(R\operatorname{Hom}(\pi^*LH_0X,\pi^*W)\), induced by the exact functor \(\pi^*\), with the map induced by the unit \(X\to\pi^*LH_0X\). In cohomological degree \(k\) it induces the first bijection for \(W[k]\), so it is a quasi-isomorphism. The other two follow in the same way. \(\square\)

**Proposition 4.6.** The functors
\[
\begin{gathered}D^-(\mathcal A) \xrightarrow{\ c\ }D^-(\mathcal A^{\bar\Delta'})\\ \xrightarrow{\ \pi^*\ }D^-(\operatorname{SIMPL}(\mathcal A))\\\xrightarrow{\ (1)\ }D^-(\operatorname{SPEC}(\mathcal A))\end{gathered}
\]
are fully faithful, where \(c\) is the constant diagram and \((1)\) is \(Y\mapsto Y(1)\). The essential image of the composite consists of the \(X\) for which the unit \(X\to\bigl(cL\varinjlim X^{\mathrm{red}}(-1)\bigr)(1)\) is an isomorphism. Equivalently, every \(H^iX\) is isomorphic to a spectral diagram \(G(1)\), \(G\in\mathcal A\).

**Proof.** A functor with a left adjoint is fully faithful if the counit is an isomorphism. For \(c\): the constant diagram \(M\) on \(\bar\Delta'\) is colimit-acyclic with colimit \(M\), by Lemma 3.1 (b) of the lesson on derived colimits with \(n=-1\), so \(L\varinjlim_{\bar\Delta'}cM\cong M\). For \(\pi^*\): by Proposition 4.4, \(LH_0\pi^*W=\operatorname{Tot}\int N\pi^*W\), and the normalization of a constant multisimplicial object is its value in multidegree \(\mathbf 0\), so \(LH_0\pi^*W\cong W\). For \((1)\): \(Y(1)\) is reduced, and \(Y(1)^{\mathrm{red}}(-1)=Y(1)(-1)\cong Y\), so the counit of Proposition 4.1 is an isomorphism.

Let \(\Phi(X)=\bigl(cL\varinjlim X^{\mathrm{red}}(-1)\bigr)(1)\). By Corollary 4.5, \(\Phi\) is the composite of the left adjoint of the composite functor with the composite functor itself. The essential image of a fully faithful functor with a left adjoint consists of the objects at which the unit is an isomorphism. All the functors involved are exact, so the composite carries \(H^i\) of \(M\in D^-(\mathcal A)\) to \(H^i\), and objects of the image have every \(H^iX\) of the form \((c\,H^iM)(1)\). Conversely, suppose every \(H^iX\cong(cG_i)(1)\). The functor \(\Phi\) is exact and takes \(D^{\leq k}\) into \(D^{\leq k}\), because \(L\varinjlim\) does (Theorem 2.3 of the lesson on derived colimits and Proposition 4.4). On objects \((cG)(1)\) in a single degree the unit is an isomorphism. By the triangles of truncations and induction on the number of nonzero cohomology objects, the unit is an isomorphism on \(\tau_{\geq i}X\) for every \(i\). From the triangle \(\tau_{\leq i-1}X\to X\to\tau_{\geq i}X\) and \(H^i\Phi(\tau_{\leq i-1}X)=H^{i+1}\Phi(\tau_{\leq i-1}X)=0\), the map \(H^iX\to H^i\Phi(X)\) is an isomorphism for every \(i\). So the unit is an isomorphism. By Proposition 3.5 with \(T=\mathcal A\), the objects \((cG)(1)=G(1)\) are the spectral diagrams described there. \(\square\)

## 5. Examples

**Example 5.1 (\(n=1\)).** A simplicial object \(X\) is reduced exactly when \(X_0=0\). Then \(X^{\mathrm{red}}=X/cX_0\), with \(cX_0\) the constant simplicial object, and \(N(X^{\mathrm{red}})\) is \(NX\) with its degree-\(0\) term removed. For \(G\in\mathcal A\), \(\operatorname{Ner}(G)[-1]\) is the constant simplicial object \(G\), by Lemma 3.4.

**Example 5.2 (the spectrum of \(\mathbb Z/2\)).** Let \(\mathcal A\) be abelian groups and \(G=\mathbb Z/2\). Then \(G\langle2\rangle(p_0,p_1)=G^{p_0p_1}\), the \(p_0\times p_1\) matrices over \(\mathbb F_2\). The faces in the first coordinate act on rows by the nerve formulas, the faces in the second on columns. The normalization is \(G\) in bidegree \((1,1)\). The spectrum \(G(1)\) has the components \(G\), \(\operatorname{Ner}(G)\), \(G\langle2\rangle,\ldots\), and its structure map for \(\delta^0\colon[0]\to[1]\) identifies \(\operatorname{Ner}(G)\) with the face of \(G\langle2\rangle\) formed by the matrices with a single row.

## 6. Exercises

**6.1.** Let \(X\in\operatorname{Simpl}_2(\mathcal A)\) be constant in the second coordinate, \(X(p,q)=V_p\) for a simplicial object \(V\). Compute \(\partial^0X\) and \(X^{\mathrm{red}}\). Then compute the epimorphism of Lemma 1.2 (5) for \(\delta=\delta^1\colon[0]\to[1]\) and \(a=1\).

**6.2.** Show that the nerve of any group satisfies (i)–(iii) of Proposition 3.1. Deduce that for \(n=1\) the essential image of \(G\mapsto G\langle1\rangle\), \(\mathrm{Sets}^{\mathrm{ab}}\to\operatorname{Simpl}(\mathrm{Sets})\), is not described by these conditions.

**6.3.** Let \(\mathcal A\) be as in Section 4 and \(M,M'\in\mathcal A\). Show that \(\operatorname{Hom}_{D(\operatorname{SPEC}(\mathcal A))}(M(1),M'(1)[k])\cong\) \(\operatorname{Ext}^k_{\mathcal A}(M,M')\) for every \(k\).

**6.4.** Let \(X\in\operatorname{SIMPL}(\mathcal A)\) be trivial, \(X=cM\). Compute \(\Delta X\), \(\int NX\) and \(LH_0X\).

## 7. Complete solutions

**6.1.** The face \(\partial^0_1X\) is \(V\) itself, and \(\iota_1\colon c_1\partial^0_1X\to X\) is the identity, so \(\partial^0X=X\) and \(X^{\mathrm{red}}=0\). For \(\delta=\delta^1\colon[0]\to[1]\), which omits the coordinate \(1\), and \(a=1\), the face \(\partial^1_\delta X\) fixes the second coordinate at \([1]\) and is \(V\). Its reduction is \(V/cV_0\). The epimorphism of Lemma 1.2 (5) is \(V/cV_0\to\partial^1_\delta(X^{\mathrm{red}})=0\). It is an isomorphism only when \(V=cV_0\).

**6.2.** For a group \(G\), \(\operatorname{Ner}(G)_0\) is a point, and the Segal map is the identity of \(G^p\). The map \((d_1,d_2)\colon G^2\to G^2\), \((g_1,g_2)\mapsto(g_2g_1,g_1)\), is bijective with inverse \((h,g)\mapsto(g,hg^{-1})\). If \(G\) is not commutative, \(\operatorname{Ner}(G)\) is not isomorphic to \(H\langle1\rangle\) for a commutative \(H\): an isomorphism would be \(\operatorname{Ner}\) of a group isomorphism \(G\cong H\), by Proposition 3.1.

**6.3.** By Proposition 4.6, the composite functor \(D^-(\mathcal A)\to D^-(\operatorname{SPEC}(\mathcal A))\) is fully faithful and carries \(M\) to \((cM)(1)=M(1)\). It is exact, so it carries \(M'[k]\) to \(M'(1)[k]\). Hence \(\operatorname{Hom}(M(1),M'(1)[k])=\) \(\operatorname{Hom}_{D(\mathcal A)}(M,M'[k])=\) \(\operatorname{Ext}^k(M,M')\).

**6.4.** Every \(X^{(n)}\) is constant with value \(M\), so \(\operatorname{diag}X^{(n)}\) is the constant simplicial object \(M\). The face inclusions are identities, and \(\Delta X\) is the constant functor with value the constant simplicial object \(M\). Likewise \(\operatorname{Tot}NX^{(n)}=M\) in degree \(0\), so \(\int NX\) is the constant diagram \(M\) in degree \(0\), and \(LH_0X\cong\int NX\) is the constant diagram \(M\) by Proposition 4.4. Then \(L\varinjlim X\cong M\), as in the proof of Proposition 4.6.

## Sources

Multisimplicial normalization and the theorem of Eilenberg–Zilber–Cartier for multisimplicial objects are treated, with explicit formulas valid in additive categories, by A. Dold and D. Puppe, *Homologie nicht-additiver Funktoren. Anwendungen*, Annales de l'Institut Fourier 11 (1961), 201–312 ([Numdam](https://www.numdam.org/articles/10.5802/aif.114/)), Sections 1–2. Spectral diagrams, the equivalence between reduced spectral diagrams and large simplicial diagrams, and the adjunction formulas are due to Illusie, in his work on the cotangent complex. The argument of Lemma 3.2 is due to Eckmann and Hilton.
