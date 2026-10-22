# Diagonal rings and adjunction formulas

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A ring of type \(C_\bullet(S_0)\) is a system of multisimplicial rings indexed by the strings of injective maps between finite ordinals ([*Graded rings and the spectra of modules*](graded-rings-and-the-spectra-of-modules.md)). Taking diagonals twice turns it into a simplicial ring \(\Delta^2R\), and normalizing gives a differential graded ring \(N\Delta^2R\) in nonpositive degrees. This lesson compares the derived category of \(R\)-modules with that of differential graded \(N\Delta^2R\)-modules. The comparison is not an equivalence: the multisimplicial and simplicial directions carry more information than the diagonal. The main theorem says that it is fully faithful on the maps into modules whose underlying object is constant, up to quasi-isomorphism, along the strings and the multisimplicial directions.

The proof rests on adjunction formulas. The constant functor from complexes of abelian sheaves to complexes of type \(C_\bullet(S_0)\) is fully faithful on bounded above derived categories, and its left adjoint is the total complex of the normalized double diagonal. This adjoint is built from two derived colimits: over the multisimplicial directions, and over the category of simplices of the nerve of the finite ordinals with injective maps, which is contractible. The lesson also translates the results between rings of type \(C_\bullet(S_0)\) and reduced rings of type \(C_\bullet(S_1)\), which is the form in which they are applied to the spectra of rings and modules.

**Prerequisites.** [*Graded rings and the spectra of modules*](graded-rings-and-the-spectra-of-modules.md) (Lemma 1.1, Definition 1.2, Propositions 1.4, 2.1 and 2.2) and Definition 2.1 of [*Graded monoids and the nerves of their actions*](graded-monoids-and-the-nerves-of-their-actions.md); Sections 2 and 4 of [*Multisimplicial objects and spectral diagrams*](multisimplicial-objects-and-spectral-diagrams.md) (Lemmas 1.2, 2.6, 4.2 and 4.3, Propositions 2.4, 4.1, 4.4 and 4.6, Corollary 4.5); [*Derived colimits over a small category*](derived-colimits-over-a-small-category.md) (Theorem 2.3 and Corollary 2.4); Sections 1–3 of [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md); Proposition 2.1 of [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md); Corollary 2.2 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md); Theorems 1.1–1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution). From the AI-integrated Stacks project: filtered colimits of abelian sheaves [[Stacks, Tag 03CO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-limits-colimits-abelian-sheaves)]; K-injective resolutions in Grothendieck abelian categories [[Tag 079P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-theorem-K-injective-embedding-grothendieck)]; bounded below complexes of injectives [[Tag 070J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-bounded-below-injectives-K-injective)]; right adjoints of exact functors preserve injectives [[Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)]; resolutions by a generating class [[Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution)]; bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)].

## Conventions

\(T\) is the topos of sheaves on a site, \(\mathcal A=\operatorname{Ab}(T)\), and \(\otimes=\otimes_{\mathbb Z}\). For a small category \(K\), the category \(\mathcal A^K\) has all small colimits, computed objectwise, exact filtered colimits [Tag 03CO], products and enough injectives (Lemma 2.2 of the lesson on multisimplicial objects); every complex has a K-injective resolution [Tag 079P]. \(D\) denotes unbounded derived categories, and \(D^-\), \(D^+\), \(D^b\), \(D^{\leq a}\), \(D^{\geq a}\) the usual full subcategories.

For \(a\in\{0,1\}\) write \(\mathcal M_a=\mathcal A^{\int C_\bullet(S_a)}\) for the category of objects of type \(C_\bullet(S_a)\) (2.2 of the lesson on graded rings): an object \(L\) consists of \(k_0\)-simplicial objects \(L_q(\sigma)\), one for each \(q\)-simplex \(\sigma=([k_0-1]\to\cdots\to[k_q-1])\) of the nerve of \(\bar\Delta'\), with maps \(L_q(\sigma)\to\partial^a_{\sigma(0,\alpha(0))}L_m(\sigma\alpha)\) for \(\alpha\colon[m]\to[q]\). Rings and modules of type \(C_\bullet(S_a)\), the functors \(L\mapsto L(1)\), \(L\mapsto L(-1)\) and \(L\mapsto L^{\mathrm{red}}\), and induced modules are those of that lesson. Modules are left modules. For a ring \(R\) of type \(C_\bullet(S_a)\), \(D(R)\) is the derived category of the Grothendieck abelian category of \(R\)-modules (Proposition 1.4 there), and \(U\colon D(R)\to D(\mathcal M_a)\) forgets the module structure. The constant functor \(c\colon\mathcal A\to\mathcal M_0\) has every component constant and every structure map an identity.

For a differential graded ring \(B\), left \(B\)-modules are the modules over the opposite ring, and the results of the lesson on differential graded modules apply to them; \(D(B)\) is their derived category. A ring \(B\) concentrated in degree \(0\) with value \(\mathbb Z\) has \(D(B)=D(\mathcal A)\).

For a complex \(E\) of simplicial objects of \(\mathcal A\), \(\operatorname{Tot}NE\) is the complex with \(N_kE^i\) in degree \(i-k\), formed with direct sums, and differential \(d_N+(-1)^kd_E\) on \(N_kE^i\), where \(d_N\colon N_k\to N_{k-1}\) is the differential of the normalized complex. Since \(d_N\) lowers \(k\), the sums over \(k\leq K\) are subcomplexes; a map of complexes of simplicial objects that is a quasi-isomorphism in each simplicial degree therefore induces a quasi-isomorphism of total complexes, by induction on \(K\) and exactness of filtered colimits. This is the row filtration used throughout.

## 1. Reduction and translation in derived categories

Let \(Q\) be a ring of type \(C_\bullet(S_1)\). Then \(Q^{\mathrm{red}}\) is a ring, and \(Q^{\mathrm{red}}(-1)\) is a ring of type \(C_\bullet(S_0)\) (Propositions 2.1 (2) and 2.2 of the lesson on graded rings).

**Proposition 1.1.**

1. For \(X\in D(Q)\) and \(Y\in D(Q^{\mathrm{red}}(-1))\) there is a natural bijection
\[
\begin{aligned}&\operatorname{Hom}_{D(Q)}\bigl(X,Y(1)\bigr)\\&\quad\cong\operatorname{Hom}_{D(Q^{\mathrm{red}}(-1))}\bigl(X^{\mathrm{red}}(-1),Y\bigr),\end{aligned}
\]
and for \(Y\in D^+(Q^{\mathrm{red}}(-1))\) a natural isomorphism \(\operatorname{RHom}_Q(X,Y(1))\cong\) \(\operatorname{RHom}(X^{\mathrm{red}}(-1),Y)\).
2. The functor \(Y\mapsto Y(1)\), \(D(Q^{\mathrm{red}}(-1))\to D(Q)\), is fully faithful. Its essential image consists of the \(X\) whose cohomology objects \(H^iX\), objects of \(\mathcal M_1\), are reduced.
3. The same statements hold for the functor \(Y\mapsto Y(1)\colon D(\mathcal M_0)\to D(\mathcal M_1)\), without rings.

**Proof.** By Propositions 2.1 (2) and 2.2 of the lesson on graded rings, \(X\mapsto X^{\mathrm{red}}\) is left adjoint to the inclusion of the reduced \(Q\)-modules, which are the reduced \(Q^{\mathrm{red}}\)-modules, and \((-1)\) and \((1)\) are inverse equivalences between these and the \(Q^{\mathrm{red}}(-1)\)-modules. So \(X\mapsto X^{\mathrm{red}}(-1)\) is left adjoint to \(Y\mapsto Y(1)\). Both functors are exact, termwise by Lemma 1.2 (3) and Proposition 2.4 of the lesson on multisimplicial objects. The rest of the proof of Proposition 4.1 there applies word for word: the functors, the unit and the counit act termwise on complexes and give the bijection; the right adjoint \(Y\mapsto Y(1)\) of an exact functor preserves injectives [Tag 015Z], and a bounded below complex of injectives is K-injective [Tag 070J], which gives the isomorphism of \(\operatorname{RHom}\).

(2) The counit \(Y(1)^{\mathrm{red}}(-1)\to Y\) is an isomorphism, because \(Y(1)\) is reduced, so \(Y\mapsto Y(1)\) is fully faithful. An object \(X\) is in the essential image exactly when the unit \(X\to X^{\mathrm{red}}(-1)(1)=X^{\mathrm{red}}\) is an isomorphism in \(D(Q)\). Reduction is exact, so \(H^i(X^{\mathrm{red}})=(H^iX)^{\mathrm{red}}\), and the unit is a quasi-isomorphism exactly when every \(H^iX\) is reduced.

(3) The proof uses only the adjunction between reduction followed by \((-1)\) and \((1)\), and their exactness. \(\square\)

## 2. Diagonal rings

**Construction 2.1.** For \(L\in\mathcal M_0\) and \(q\geq0\), let
\[
\Delta L_q=\bigoplus_{\sigma\in N_q(\bar\Delta')}\operatorname{diag}L_q(\sigma),
\]
a simplicial object of \(\mathcal A\); when \(\sigma\) starts at \([-1]\), \(L_q(\sigma)\) is an object of \(\mathcal A\) and its diagonal is the constant simplicial object. For \(\alpha\colon[m]\to[q]\) and \(\delta=\sigma(0,\alpha(0))\), the map \(\Delta L_q\to\Delta L_m\) on the summand of \(\sigma\) is the composite
\[
\begin{aligned}&\operatorname{diag}L_q(\sigma) \to\operatorname{diag}\partial^0_\delta L_m(\sigma\alpha)\\&\quad \xrightarrow{\ j_\delta\ }\operatorname{diag}L_m(\sigma\alpha)\end{aligned}
\]
of the diagonal of the structure map and the face inclusion \(j_\delta\) of Section 2 of the lesson on multisimplicial objects. As for the functor \(\Delta X\) of that section, these maps compose correctly, so \(q\mapsto\Delta L_q\) is a simplicial object of \(\operatorname{Simpl}(\mathcal A)\), the bisimplicial object \((q,p)\mapsto\bigoplus_\sigma L_q(\sigma)(p,\ldots,p)\). Its diagonal is written \(\Delta^2L\):
\[
(\Delta^2L)_n=\bigoplus_{\sigma\in N_n(\bar\Delta')}L_n(\sigma)(n,\ldots,n).
\]
The functor \(L\mapsto\Delta^2L\), \(\mathcal M_0\to\operatorname{Simpl}(\mathcal A)\), is exact, since sums and evaluations are.

Let \(R\) be a ring of type \(C_\bullet(S_0)\). Its multiplication \(R_q(\sigma)\mathbin{\underline\otimes}R_q(\tau)\to R_q(\sigma+\tau)\) has as diagonal a map \(\operatorname{diag}R_q(\sigma)\otimes\operatorname{diag}R_q(\tau)\to\) \(\operatorname{diag}R_q(\sigma+\tau)\), by Lemma 1.1 (1) of the lesson on graded rings. These maps make \(\Delta R_q\) a simplicial ring, with unit in the summand of the string of identities of \([-1]\). They are compatible with the maps of Construction 2.1, because the structure maps of \(R\) are multiplicative and \(j_{\delta+\varepsilon}=j_\delta\otimes j_\varepsilon\). So \(\Delta R\) is a simplicial object of simplicial rings and \(\Delta^2R\) a simplicial ring, not commutative in general. For an \(R\)-module \(E\), \(\Delta^2E\) is a left \(\Delta^2R\)-module in the same way.

**Lemma 2.2.** Let \(A\) be an \(S_0\)-graded ring and \(M\) an \(S_0\)-graded \(A\)-module. The functor \(\Delta A\colon\bar\Delta'\to\operatorname{Simpl}(\mathcal A)\), \([k-1]\mapsto\operatorname{diag}A^{(k)}\), is a ring graded by the monoidal category \(\bar\Delta'\) over its one-point grading, and \(\Delta M\) is a \(\Delta A\)-module. Applying \(C_\bullet\) relative to \(\bar\Delta'\) gives a bisimplicial ring \(C_\bullet(\Delta A)\), and
\[
\begin{gathered}\Delta C_\bullet(\Delta A)=\Delta^2C_\bullet(A),\\ \Delta C_\bullet(\Delta M)=\Delta^2C_\bullet(M),\end{gathered}
\]
the first as simplicial rings and the second as modules over them.

**Proof.** The multiplications of \(\Delta A\) are the diagonals of those of \(A\), by Lemma 1.1 (1) of the lesson on graded rings. For the one-point grading, \(C_q(\Delta A)=\bigoplus_\sigma\operatorname{diag}A^{(k_0)}\), the sum over the \(q\)-simplices \(\sigma\) of the nerve of \(\bar\Delta'\), with \(k_0\) the size of the first vertex of \(\sigma\), and its map for \(\alpha\) is \(\Delta A(\sigma(0,\alpha(0)))=j_\delta\circ\operatorname{diag}(A_\delta)\) on the summand of \(\sigma\). On the other hand \(C_q(A)(\sigma)=A^{(k_0)}\), with the structure map \(A_\delta\) for \(\alpha\) (Definition 2.1 of the lesson on graded monoids). So \(\Delta C_\bullet(A)_q=C_q(\Delta A)\), with the same maps and multiplications, and taking diagonals gives the first equality. The second is the same computation. \(\square\)

**Proposition 2.3.** Let \(R\) be a ring of type \(C_\bullet(S_0)\), and \(B=N\Delta^2R\).

1. \(B\) is a differential graded ring in nonpositive degrees, and for every \(R\)-module \(E\), \(N\Delta^2E\) is a left differential graded \(B\)-module, functorially and exactly in \(E\).
2. For a complex \(E\) of \(R\)-modules, \(\operatorname{Tot}N\Delta^2E\) is a left \(B\)-module, and \(E\mapsto\operatorname{Tot}N\Delta^2E\) carries quasi-isomorphisms to quasi-isomorphisms. It defines an exact functor
\[
\Phi\colon D(R)\to D(B).
\]
3. \(\Phi\) maps \(D^{\leq a}(R)\) into \(D^{\leq a}(B)\) for every \(a\), and \(D^-(R)\) into \(D^-(B)\).
4. Forgetting the module structures, \(\Phi(E)\) is \(\Lambda(UE)\), where \(\Lambda\colon D(\mathcal M_0)\to D(\mathcal A)\) is the exact functor \(L\mapsto\operatorname{Tot}N\Delta^2L\).

**Proof.** (1) Proposition 2.1 of the lesson on simplicial rings makes the normalized complex of a simplicial ring a differential graded ring, through the shuffle map followed by the multiplication, and the normalized complex of a module a module over it. Its proof uses commutativity only for the graded commutativity of the result, so it applies to \(\Delta^2R\), and \(B\) lies in degrees \(\leq0\). Normalization is exact (Theorem 1.1 of *The cotangent complex*), and so is \(\Delta^2\).

(2) On \(N_k\Delta^2E^i\), the action of \(b\in B\) of degree \(-k'\) lands in \(N_{k+k'}\Delta^2E^i\). It commutes with \(d_E\), because the differential of \(E\) is \(R\)-linear, and satisfies the Leibniz rule for \(d_N\). With the sign \((-1)^k\) on \(d_E\), the Leibniz rule \(D(bx)=(db)x+(-1)^{k'}bD(x)\) holds for the total differential \(D\): both sides equal \((db)x+(-1)^{k'}b\,d_Nx+(-1)^{k+k'}b\,d_Ex\). If \(E\) is acyclic, each row \(N_k\Delta^2E^\bullet\) is acyclic, because \(N_k\Delta^2\) is exact, so \(\operatorname{Tot}N\Delta^2E\) is acyclic by the row filtration. Since the construction commutes with cones, it preserves quasi-isomorphisms and defines an exact functor on derived categories.

(3) An object of \(D^{\leq a}(R)\) is isomorphic to its truncation, a complex of \(R\)-modules vanishing in degrees \(>a\), and then \(\operatorname{Tot}N\Delta^2E\) vanishes in degrees \(>a\). (4) holds by construction. \(\square\)

**Construction 2.4 (the comparison maps).** For complexes \(E\) and \(F\) of \(R\)-modules, a family \(f=(f^i\colon E^i\to F^{i+k})\) of \(R\)-linear maps, an element of degree \(k\) of \(\operatorname{Hom}^\bullet_R(E,F)\), gives the map that is \((-1)^{km}N\Delta^2(f^i)\) on \(N_m\Delta^2E^i\). This is a \(B\)-linear map of degree \(k\) from \(\operatorname{Tot}N\Delta^2E\) to \(\operatorname{Tot}N\Delta^2F\), and the assignment is a map of complexes
\[
\begin{aligned}&\operatorname{Hom}^\bullet_R(E,F)\\&\quad \to\operatorname{Hom}^\bullet_B\bigl(\operatorname{Tot}N\Delta^2E,\operatorname{Tot}N\Delta^2F\bigr).\end{aligned}
\]
Indeed, with \(D\) the total differentials and \(\Phi_f\) the map defined by \(f\), the terms with \(d_N\) in \(D\Phi_f-(-1)^k\Phi_fD\) cancel because \((-1)^{k(m-1)}=(-1)^k(-1)^{km}\), and the remaining terms give \(\Phi_{df}\). Let \(F\to I\) be a K-injective resolution of \(R\)-modules and \(\Phi(I)\to J\) a K-injective resolution of \(B\)-modules. The composite
\[
\begin{aligned}\operatorname{Hom}^\bullet_R(E,I)&\to\operatorname{Hom}^\bullet_B(\Phi E,\Phi I)\\&\to\operatorname{Hom}^\bullet_B(\Phi E,J)\end{aligned}
\]
defines a morphism of \(D(\mathrm{Ab})\)
\[
\begin{aligned}&\theta_{E,F} \colon\operatorname{RHom}_R(E,F)\\&\quad \to\operatorname{RHom}_B(\Phi E,\Phi F),\end{aligned}
\]
natural in \(E\) and \(F\) and independent of the choices up to canonical isomorphism (Proposition 2.3 of the lesson on differential graded modules). On \(H^j\) it is the map \(\operatorname{Hom}_{D(R)}(E,F[j])\to\) \(\operatorname{Hom}_{D(B)}(\Phi E,\Phi F[j])\) induced by the functor \(\Phi\), since an element of \(H^j\operatorname{Hom}^\bullet_R(E,I)=\operatorname{Hom}_{K(R)}(E,I[j])\) goes to the class of \(\Phi\) of it. So \(\theta_{E,F}\) is an isomorphism exactly when \(\Phi\) induces bijections \(\operatorname{Hom}_{D(R)}(E,F[j])\to\) \(\operatorname{Hom}_{D(B)}(\Phi E,\Phi F[j])\) for all \(j\).

## 3. Derived colimits and the constant functor

Let \(\mathfrak N\) be the total category of the nerve of \(\bar\Delta'\), regarded as a simplicial object of discrete categories: its objects are the pairs \((q,\sigma)\) with \(\sigma\in N_q(\bar\Delta')\), and its arrows \((q,\sigma)\to(m,\sigma\alpha)\) correspond to the maps \(\alpha\colon[m]\to[q]\) of \(\Delta\). A functor \(W\colon\mathfrak N\to\mathcal A\) is a family of objects \(W_q(\sigma)\) with maps \(W_q(\sigma)\to W_m(\sigma\alpha)\), a contravariant coefficient system on the nerve of \(\bar\Delta'\) (Examples 5.2 (b) of the lesson on fibred topoi). Let \(\pi\colon\int C_\bullet(S_0)\to\mathfrak N\) send \((q,(\sigma,x))\) to \((q,\sigma)\). Then \(\pi^*\colon\mathcal A^{\mathfrak N}\to\mathcal M_0\) embeds \(\mathcal A^{\mathfrak N}\) as the objects whose components are constant multisimplicial objects, and the constant functor is \(c=\pi^*c_{\mathfrak N}\), where \(c_{\mathfrak N}\colon\mathcal A\to\mathcal A^{\mathfrak N}\) is constant.

**Lemma 3.1.** The functor \(\pi^*\) has the left adjoint \(H_0\), with \(H_0(L)_q(\sigma)=\) \(\varinjlim_{(\Delta^{\mathrm{op}})^{k_0}}L_q(\sigma)\cong\) \(H_0(N\operatorname{diag}L_q(\sigma))\) and the maps induced by the structure maps of \(L\).

**Proof.** As in Lemma 4.2 of the lesson on multisimplicial objects: a map \(L\to\pi^*W\) is a family of maps from the multisimplicial objects \(L_q(\sigma)\) to the constant objects \(W_q(\sigma)\), compatible with the structure maps, that is, a family of maps \(\varinjlim L_q(\sigma)\to W_q(\sigma)\) compatible with the induced maps. The second description of the colimit is Lemma 4.2 (1) there. \(\square\)

**Proposition 3.2.** The functor \(H_0\) has a left derived functor \(LH_0\colon D^-(\mathcal M_0)\to D^-(\mathcal A^{\mathfrak N})\), and \(LH_0(L)\cong\operatorname{Tot}N\Delta L\), the functor on \(\mathfrak N\) whose value at \((q,\sigma)\) is \(\operatorname{Tot}N\operatorname{diag}L_q(\sigma)\), with the maps of Construction 2.1. For \(W\in D(\mathcal A^{\mathfrak N})\) there is a natural bijection \(\operatorname{Hom}(LH_0L,W)\cong\operatorname{Hom}(L,\pi^*W)\), and for \(W\in D^+(\mathcal A^{\mathfrak N})\) a natural isomorphism \(\operatorname{RHom}(LH_0L,W)\cong\operatorname{RHom}(L,\pi^*W)\).

**Proof.** The proofs of Proposition 4.4 and Corollary 4.5 of the lesson on multisimplicial objects apply, with \(\mathbb S_0\) replaced by \(\int C_\bullet(S_0)\) and \(\bar\Delta'\) by \(\mathfrak N\). The one point to check is that the induced objects of \(\mathcal M_0\) are \(H_0\)-acyclic, that is, that their components are colimit-acyclic multisimplicial objects. The arrows of \(\int C_\bullet(S_0)\) from \((q',(\sigma',x'))\) to \((q,(\sigma,x))\) are the pairs of a map \(\alpha\colon[q]\to[q']\) with \(\sigma'\alpha=\sigma\) and an arrow \(y_\alpha\to x\) of \((\Delta^{\mathrm{op}})^{k_0}\), where \(y_\alpha=(\sigma'(0,\alpha(0)))_0(x')\). So at fixed \((q,\sigma)\) the induced object on an object \(Y\) placed at \((q',(\sigma',x'))\) is the sum over \(\alpha\) of the induced diagrams of \((\Delta^{\mathrm{op}})^{k_0}\) on \(Y\) placed at \(y_\alpha\), which are colimit-acyclic by the proof of Lemma 4.3 there. \(\square\)

**Proposition 3.3.** The constant functor \(c_{\mathfrak N}\) has a left adjoint \(\varinjlim_{\mathfrak N}\), whose left derived functor \(L\varinjlim_{\mathfrak N}\colon D^-(\mathcal A^{\mathfrak N})\to D^-(\mathcal A)\) satisfies, for \(W\in D^-(\mathcal A^{\mathfrak N})\),
\[
\begin{gathered}L\varinjlim_{\mathfrak N}W\cong\operatorname{Tot}NW^\nabla,\\ W^\nabla_n=\bigoplus_{\sigma\in N_n(\bar\Delta')}W_n(\sigma),\end{gathered}
\]
where the simplicial object \(W^\nabla\) has the face \(d_i\) given on the summand of \(\sigma\) by the map \(W_n(\sigma)\to W_{n-1}(\sigma\delta^i)\), and the degeneracies in the same way. There are natural bijections \(\operatorname{Hom}(L\varinjlim_{\mathfrak N}W,G)\cong\operatorname{Hom}(W,c_{\mathfrak N}G)\) for \(G\in D(\mathcal A)\), and isomorphisms of \(\operatorname{RHom}\) for \(G\in D^+(\mathcal A)\).

**Proof.** The derived colimit and its adjunction are Theorem 2.3 and Corollary 2.4 of the lesson on derived colimits; the statement for \(\operatorname{RHom}\) follows as in Corollary 4.5 of the lesson on multisimplicial objects. For the formula, note first that \(H_0(sW^\nabla)\) is \(\varinjlim_{\mathfrak N}W\). Indeed, the full subcategory \(\mathfrak N_{\leq1}\) of the objects \((0,\sigma)\) and \((1,\sigma)\) is final in \(\mathfrak N\): for an object \((n,\sigma)\), the arrows from it to objects of \(\mathfrak N_{\leq1}\) form the opposite of the category of the simplices of dimension at most \(1\) of \(\Delta[n]\), which is nonempty and connected. Over \(\mathfrak N_{\leq1}\), the colimit is the cokernel of \(d_0-d_1\colon W^\nabla_1\to W^\nabla_0\); the degenerate edges give no further relations.

Let \(Y\) be an object placed at \((m,\tau)\), and \(P\) the induced diagram on it. The arrows \((m,\tau)\to(n,\sigma)\) are the maps \(\beta\colon[n]\to[m]\) with \(\tau\beta=\sigma\), so \(P^\nabla_n=\bigoplus_{\beta\colon[n]\to[m]}Y\), and \(P^\nabla\) is \(Y\otimes\mathbb Z(\Delta[m])\), the sum of copies of \(Y\) indexed by the simplices of \(\Delta[m]\). Since \(\Delta[m]\) is contractible (Corollary 2.2 of the lesson on décalage), \(sP^\nabla\to Y=\varinjlim_{\mathfrak N}P\) is a homotopy equivalence. The argument of Lemma 4.3 of the lesson on multisimplicial objects, with a bounded above resolution by induced diagrams and the row filtration, gives the formula. \(\square\)

**Proposition 3.4.** For \(L\in D^-(\mathcal M_0)\) there is a natural isomorphism
\[
L\varinjlim_{\mathfrak N}LH_0L\cong\Lambda L=\operatorname{Tot}N\Delta^2L.
\]
Consequently:

1. \(\Lambda\) is a left derived functor of the colimit over \(\int C_\bullet(S_0)\), and it is left adjoint to \(c\): there are natural bijections \(\operatorname{Hom}_{D(\mathcal A)}(\Lambda L,G)\cong\) \(\operatorname{Hom}_{D(\mathcal M_0)}(L,cG)\) for \(L\in D^-(\mathcal M_0)\) and \(G\in D(\mathcal A)\), and isomorphisms \(\operatorname{RHom}(\Lambda L,G)\cong\operatorname{RHom}(L,cG)\) for \(G\in D^+(\mathcal A)\).
2. For every complex \(G\) of \(\mathcal A\), the augmentation \(\Lambda cG\to G\) is a quasi-isomorphism.
3. \(c\colon D^-(\mathcal A)\to D^-(\mathcal M_0)\) is fully faithful: the counit of the adjunction of (1) is an isomorphism.

**Proof.** By Propositions 3.2 and 3.3, \(L\varinjlim_{\mathfrak N}LH_0L\) is the total complex of \(N\) applied to \(n\mapsto\bigoplus_\sigma\operatorname{Tot}N\operatorname{diag}L_n(\sigma)\). For an object \(L\), this is the total complex of the normalized double complex of the bisimplicial object \((n,p)\mapsto\bigoplus_{\sigma\in N_n(\bar\Delta')}L_n(\sigma)(p,\ldots,p)\), and the Eilenberg–Zilber theorem (Lemma 2.6 of the lesson on multisimplicial objects) identifies the normalized total complex with the normalized diagonal, which is \(N\Delta^2L\). For a complex \(L\), apply this termwise and use the row filtration.

(1) The colimit over \(\int C_\bullet(S_0)\) is \(\varinjlim_{\mathfrak N}\circ H_0\), since \(c=\pi^*c_{\mathfrak N}\). The functor \(H_0\) carries the induced objects of \(\mathcal M_0\) to induced objects of \(\mathcal A^{\mathfrak N}\), as a composite of left adjoints. Hence, for a bounded above complex \(P\) of induced objects, which computes all three derived functors, both \(L\varinjlim_{\int C_\bullet(S_0)}P\) and \(L\varinjlim_{\mathfrak N}LH_0P\) are \(\varinjlim_{\mathfrak N}H_0P\). The adjunctions are the composites of those of Propositions 3.2 and 3.3.

(2) The components of \(cG\) are constant with identity structure maps, and the face inclusions of constant multisimplicial objects are identities. So \(\Delta^2cG=G\otimes\mathbb Z(N(\bar\Delta'))\), with the faces and degeneracies of the nerve. The category \(\bar\Delta'\) has the initial object \([-1]\), so its nerve is contractible (Corollary 2.2 of the lesson on décalage), and the augmentation \(N\mathbb Z(N(\bar\Delta'))\to\mathbb Z\) is a chain homotopy equivalence. Tensoring with \(G\) and totalizing preserves this.

(3) By (1) and Theorem 2.3 of the lesson on derived colimits, \(H_n\) of the simplicial replacement of \(cG\) over \(\int C_\bullet(S_0)\) is \(H^{-n}\Lambda cG\), for \(G\in\mathcal A\). By (2) it vanishes for \(n\neq0\), so \(cG\) is colimit-acyclic, and \(\varinjlim cG=H^0\Lambda cG=G\). For a bounded above complex \(G\), \(cG\) is then a bounded above complex of colimit-acyclic objects, which computes \(L\varinjlim\); so the counit at \(G\) is the counit of the adjunction between the colimit and \(c\), which is the identity of \(G\). A right adjoint whose counit is an isomorphism is fully faithful. \(\square\)

**Proposition 3.5.** For \(X\in D^-(\operatorname{SIMPL}(\mathcal A))\) there is a natural isomorphism \(\Lambda C_\bullet(X)\cong L\varinjlim X\), where \(L\varinjlim\) is the derived colimit of large simplicial diagrams of the lesson on multisimplicial objects (the composite of \(LH_0\) and \(L\varinjlim_{\bar\Delta'}\)).

**Proof.** For an object \(X\), Lemma 2.2 gives \(\Delta^2C_\bullet(X)=\Delta C_\bullet(\Delta X)\). The simplicial object \(C_\bullet(\Delta X)\) of \(\operatorname{Simpl}(\mathcal A)\) is the simplicial replacement of the diagram \(\Delta X\) of \(\bar\Delta'\) (Section 1 of the lesson on derived colimits), computed in each simplicial degree: both have \(\bigoplus_\sigma\Delta X(\sigma(0))\) in degree \(n\), the face \(d_0\) uses \(\Delta X(\sigma(0,1))\), and the other faces and the degeneracies are identities on the summands. By the Eilenberg–Zilber theorem, as in Proposition 3.4, \(\Lambda C_\bullet(X)\) is quasi-isomorphic to the total complex of the simplicial replacement of the diagram \(\operatorname{Tot}N\Delta X\) of complexes. By Proposition 4.4 of the lesson on multisimplicial objects this diagram is \(LH_0X\), and by Theorem 2.3 of the lesson on derived colimits the total complex is \(L\varinjlim_{\bar\Delta'}LH_0X\). For complexes \(X\), apply this termwise and use the row filtration. \(\square\)

**Proposition 3.6.**

1. The essential image of \(c\colon D^-(\mathcal A)\to D^-(\mathcal M_0)\) consists of the \(X\) such that every \(H^iX\) is isomorphic to a constant object \(cG_i\), \(G_i\in\mathcal A\).
2. The composite of \(c\) and \(Y\mapsto Y(1)\), \(D^-(\mathcal A)\to D^-(\mathcal M_1)\), is fully faithful. Its essential image consists of the \(Y\) such that every \(H^iY\) is isomorphic to \(C_\bullet(G_i(1))\) for some \(G_i\in\mathcal A\), where \(G_i(1)\) is the spectrum of \(G_i\).

**Proof.** (1) The argument of Proposition 4.6 of the lesson on multisimplicial objects applies. An object \(X\) is in the essential image exactly when the unit \(X\to c\Lambda X\) is an isomorphism. Objects of the image have constant cohomology, because \(c\) is exact. Conversely, let every \(H^iX\cong cG_i\). The functor \(c\Lambda\) is exact and takes \(D^{\leq k}\) into \(D^{\leq k}\). On objects \(cG[-i]\) the unit is an isomorphism, by Proposition 3.4 (3). By the triangles of truncations and induction, it is an isomorphism on \(\tau_{\geq i}X\) for every \(i\). From the triangle \(\tau_{\leq i-1}X\to X\to\tau_{\geq i}X\), and since \(H^i\) and \(H^{i+1}\) of \(c\Lambda\tau_{\leq i-1}X\) vanish, \(H^iX\to H^ic\Lambda X\) is an isomorphism for every \(i\).

(2) Full faithfulness: Proposition 3.4 (3) and Proposition 1.1 (3). By Proposition 2.2 (3) of the lesson on graded rings, \((cG)(1)=\) \(C_\bullet(c'G)(1)=\) \(C_\bullet((c'G)(1))=\) \(C_\bullet(G(1))\), where \(c'G\) is the trivial large simplicial diagram, whose translate is the spectrum of \(G\) (Section 3 of the lesson on multisimplicial objects). If \(Y\cong X(1)\) with \(X\) in the image of \(c\), then \(H^iY=(H^iX)(1)\) has this form, because \((1)\) is exact. Conversely, if every \(H^iY\cong C_\bullet(G_i(1))\), then the \(H^iY\) are reduced, so \(Y\cong X(1)\) with \(X=Y^{\mathrm{red}}(-1)\) (Proposition 1.1 (3)), and \(H^iX=(H^iY)^{\mathrm{red}}(-1)\cong cG_i\). By (1), \(X\) is in the image of \(c\). \(\square\)

## 4. The comparison theorem

**Theorem 4.1.** Let \(R\) be a ring of type \(C_\bullet(S_0)\) whose components \(R_q(\sigma)(x)\) are flat abelian sheaves, and \(B=N\Delta^2R\). Let \(E\in D^-(R)\) and \(F\in D^+(R)\), and suppose that \(UF\cong cG\) in \(D(\mathcal M_0)\) for some \(G\in D(\mathcal A)\). Then
\[
\begin{aligned}&\theta_{E,F} \colon\operatorname{RHom}_R(E,F)\\&\quad \to\operatorname{RHom}_B(\Phi E,\Phi F)\end{aligned}
\]
is an isomorphism; equivalently, \(\Phi\) induces bijections \(\operatorname{Hom}_{D(R)}(E,F[j])\to\) \(\operatorname{Hom}_{D(B)}(\Phi E,\Phi F[j])\) for all \(j\).

By Proposition 3.6 (1), for \(F\in D^b(R)\) the hypothesis says that every \(H^i(UF)\) is isomorphic to a constant object.

**Proof.** *Adjunctions.* Let \(\operatorname{ind}\) be the induced module functor of Proposition 1.4 of the lesson on graded rings. It is exact, because the components of \(R\) are flat, and left adjoint to the exact forgetful functor. As in Proposition 1.1, it induces a left adjoint \(\operatorname{ind}\colon D(\mathcal M_0)\to D(R)\) of \(U\), with the termwise unit \(\eta\). Let \(U'\colon D(B)\to D(\mathcal A)\) forget the module structure. The terms of \(B\) are direct summands of sums of components of \(R\), so \(B\) is a bounded above complex of flat sheaves and is K-flat [Tag 06YQ]. Hence the extension of scalars \(\operatorname{ind}'=B\otimes_{\mathbb Z}-\) is computed on every complex, and it is left adjoint to \(U'\), the bijection sending \(g\) to \(\epsilon'\circ\operatorname{ind}'(g)\), where \(\epsilon'\colon\operatorname{ind}'U'\to\mathrm{id}\) is the action (Proposition 2.5 (1) of the lesson on differential graded modules, for the map \(\mathbb Z\to B\)).

*Induced modules.* Let \(L\in\mathcal M_0\), placed in degree \(0\). The module \(\operatorname{ind}(L)\) has \(\operatorname{ind}(L)_q(\sigma)=\) \(\bigoplus_{\sigma=\sigma_1+\sigma_2}R_q(\sigma_1)\mathbin{\underline\otimes}L_q(\sigma_2)\), so Lemma 1.1 (1) of the lesson on graded rings gives \(\Delta\operatorname{ind}(L)_q=\Delta R_q\otimes\Delta L_q\), and
\[
\Delta^2\operatorname{ind}(L)=\Delta^2R\otimes\Delta^2L
\]
as \(\Delta^2R\)-modules, with \(\Delta^2R\) acting on the left factor. Let \(\nu_L\colon B\otimes N\Delta^2L\to N\Delta^2\operatorname{ind}(L)\) be the shuffle map. It is \(B\)-linear by associativity of shuffle maps, and a quasi-isomorphism by the Eilenberg–Zilber theorem. Since the unit \(\eta_L\) sends \(\xi\) to \(1\otimes\xi\), the composite
\[
\begin{aligned}&B\otimes N\Delta^2L\\&\quad \xrightarrow{\operatorname{ind}'(\Lambda\eta_L)}B\otimes N\Delta^2\operatorname{ind}(L)\\&\quad \xrightarrow{\ \epsilon'\ }N\Delta^2\operatorname{ind}(L)\end{aligned}
\]
sends \(b\otimes x\) to the product of \(b\) with \(1\otimes x\) after the shuffle map, which is the shuffle of \(b\) and \(x\). So it equals \(\nu_L\).

Let \(f\in\operatorname{Hom}_{D(R)}(\operatorname{ind}(L),F[j])\) and \(f^\flat=U(f)\circ\eta_L\), its adjoint. Since \(\Lambda U=U'\Phi\) (Proposition 2.3 (4)) and \(\epsilon'\) is natural,
\[
\begin{aligned}&\epsilon'\circ\operatorname{ind}'(\Lambda f^\flat)\\ &\quad =\epsilon'\circ\operatorname{ind}'(U'\Phi f)\circ\operatorname{ind}'(\Lambda\eta_L)\\ &\quad =\Phi(f)\circ\epsilon'\circ\operatorname{ind}'(\Lambda\eta_L)\\ &\quad =\Phi(f)\circ\nu_L.\end{aligned}
\]
The map \(f\mapsto f^\flat\) and the map \(g\mapsto\epsilon'\circ\operatorname{ind}'(g)\) are bijections, and \(\nu_L\) is an isomorphism of \(D(B)\). So \(\Phi\colon\) \(\operatorname{Hom}(\operatorname{ind}L,F[j])\to\) \(\operatorname{Hom}(\Phi\operatorname{ind}L,\Phi F[j])\) is bijective if and only if
\[
\begin{aligned}&\Lambda \colon\operatorname{Hom}_{D(\mathcal M_0)}(L,UF[j])\\&\quad \to\operatorname{Hom}_{D(\mathcal A)}(\Lambda L,\Lambda UF[j])\end{aligned}
\]
is bijective.

*The constant case.* Transport along \(UF\cong cG\). Since \(L\) and \(\Lambda L\) lie in \(D^{\leq0}\), maps from them into an object depend only on its truncation \(\tau^{\leq0}\). Moreover \(\tau^{\leq0}(cG[j])=c(\tau^{\leq j}G)[j]\), and \(\tau^{\leq0}(\Lambda cG[j])\cong\Lambda c(\tau^{\leq j}G)[j]\) by Proposition 3.4 (2), compatibly with \(\Lambda\). So we may assume \(G\in D^-(\mathcal A)\). Then, by Proposition 3.4 (1) and (3), the map \(\psi\mapsto\epsilon_G\circ\Lambda(\psi)\), with \(\epsilon\) the counit, is the adjunction bijection \(\operatorname{Hom}(L,cG[j])\to\operatorname{Hom}(\Lambda L,G[j])\), and \(\epsilon_G\) is an isomorphism. Hence \(\Lambda\) is bijective on these maps, and \(\Phi\) is bijective on \(\operatorname{Hom}(\operatorname{ind}L,F[j])\) for every \(j\). The same holds for \(\operatorname{ind}(L)[k]\), by replacing \(j\) with \(j-k\).

*Dévissage.* Let \(\mathcal C\) be the class of the \(E\in D^-(R)\) for which \(\Phi\) is bijective on \(\operatorname{Hom}(E,F[j])\) for all \(j\). Since \(\Phi\) is exact and both sides are cohomological functors of \(E\), the five lemma shows that \(\mathcal C\) is closed under extensions, and it contains the shifted induced modules. So it contains every bounded complex of induced modules. Every \(E\in D^-(R)\) is isomorphic to a bounded above complex \(P\) of induced modules [Tag 05T7], because every module \(M\) is a quotient of \(\operatorname{ind}(UM)\). Let \(F\in D^{\geq b}(R)\). Then \(cG\cong UF\in D^{\geq b}\), so \(G\in D^{\geq b}\), and \(U'\Phi F=\Lambda UF\cong G\), so \(\Phi F\in D^{\geq b}(B)\). Fix \(j\), and let \(\sigma_{\geq-m}P\subseteq P\) be the subcomplex of the terms of degree \(\geq-m\), with quotient \(\sigma_{<-m}P\). For \(m\) large, \(\sigma_{<-m}P\) and \(\sigma_{<-m}P[-1]\) lie in \(D^{\leq b-j-1}\), and so do their images under \(\Phi\) (Proposition 2.3 (3)). So they have no maps to \(F[j]\), respectively \(\Phi F[j]\) (Proposition 2.3 (3) of the lesson on differential graded modules for \(B\)). The long exact sequences of the triangle \(\sigma_{\geq-m}P\to P\to\sigma_{<-m}P\) then identify the maps induced by \(\Phi\) on \(\operatorname{Hom}(P,F[j])\) and on \(\operatorname{Hom}(\sigma_{\geq-m}P,F[j])\), naturally, and the latter is bijective. So \(E\in\mathcal C\). By Construction 2.4, \(\theta_{E,F}\) is an isomorphism. \(\square\)

Let \(Q\) be a ring of type \(C_\bullet(S_1)\). The functor \(L\mapsto L^{\mathrm{red}}(-1)\) is exact, and so gives a natural map
\[
\begin{aligned}&\operatorname{RHom}_Q(X,Y)\\&\quad\to\operatorname{RHom}_{Q^{\mathrm{red}}(-1)}\bigl(X^{\mathrm{red}}(-1),\\&\qquad Y^{\mathrm{red}}(-1)\bigr)\end{aligned}
\]
for \(X,Y\in D(Q)\), defined as in Construction 2.4. Composed with \(\theta\) for the ring \(Q^{\mathrm{red}}(-1)\), it gives a natural map
\[
\begin{aligned}&\operatorname{RHom}_Q(X,Y)\to\operatorname{RHom}_{B'}\bigl(\\ &\quad \Phi(X^{\mathrm{red}}(-1)),\\ &\quad \Phi(Y^{\mathrm{red}}(-1))\bigr),\end{aligned}
\]
where \(B'=N\Delta^2(Q^{\mathrm{red}}(-1))\).

**Corollary 4.2.** Suppose that the components of \(Q\) are flat abelian sheaves, and let \(X\in D^-(Q)\) and \(Y\in D^+(Q)\) such that \(UY\cong(cG)(1)\) in \(D(\mathcal M_1)\) for some \(G\in D(\mathcal A)\). Then this map is an isomorphism.

**Proof.** The components of \(Q^{\mathrm{red}}(-1)\) are finite sums of direct summands of components of \(Q\): the normalization, the restriction to multidegrees \(\geq\mathbf 1\) and the Dold–Kan construction take direct summands and finite sums. So they are flat. The cohomology of \(UY\) is reduced, so \(Y\cong Y'(1)\) with \(Y'=Y^{\mathrm{red}}(-1)\) (Proposition 1.1 (2)), and \(UY'\cong cG\). Under \(Y\cong Y'(1)\), the first map is the bijection of Proposition 1.1 (1): on \(H^j\) it sends \(f\colon X\to Y'(1)[j]\) to \(f^{\mathrm{red}}(-1)\), followed by the counit \(Y'(1)^{\mathrm{red}}(-1)=Y'\), which is the identity. The second map is an isomorphism by Theorem 4.1. \(\square\)

## 5. Exercises

**5.1.** Let \(G\) be an abelian group (\(T\) the topos of sets). Write out \(\Delta^2cG\) in degrees \(0\) and \(1\), and give an explicit contracting homotopy of the augmented complex \(s\mathbb Z(N(\bar\Delta'))\to\mathbb Z\), using the initial object \([-1]\) of \(\bar\Delta'\).

**5.2.** Let \(\mathbb 1\) be the ring of type \(C_\bullet(S_0)\) with \(\mathbb 1_q(\sigma)=\mathbb Z\) when \(\sigma\) is the string of identities of \([-1]\), and \(0\) otherwise. Show that every object of \(\mathcal M_0\) is, in exactly one way, an \(\mathbb 1\)-module, that \(N\Delta^2\mathbb 1=\mathbb Z\), and that \(\Phi=\Lambda\). Let \(a=(0,([0],(1)))\), an object of \(\int C_\bullet(S_0)\), and \(P\) the induced object on \(\mathbb Z\) placed at \(a\) (\(T\) the topos of sets). Show that \(\operatorname{Hom}_{D(\mathcal M_0)}(P,P)\cong\mathbb Z^3\), that \(\Lambda P\cong\mathbb Z\), and conclude that Theorem 4.1 fails for \(E=F=P\). Which hypothesis is not satisfied?

**5.3.** Let \(G\ne0\) be an abelian group, and let \(cG\) also denote the constant object of \(\mathcal M_1\). Compute \((cG)^{\mathrm{red}}\), and show that \(cG\) is not in the essential image of \(Y\mapsto Y(1)\).

## 6. Complete solutions

**5.1.** In degree \(0\) the simplices of \(N(\bar\Delta')\) are the ordinals \([k-1]\), \(k\geq0\), and \((\Delta^2cG)_0=\bigoplus_kG\). In degree \(1\) they are the injective maps \(\delta\colon[k-1]\to[l-1]\), with \(d_0\delta=[l-1]\) and \(d_1\delta=[k-1]\). For each simplex \(\sigma=(i_0\to\cdots\to i_n)\), let \(h(\sigma)\) be the \((n+1)\)-simplex \(([-1]\to i_0\to\cdots\to i_n)\), whose first arrow is the unique map from \([-1]\). Then \(d_0h(\sigma)=\sigma\) and \(d_ih(\sigma)=h(d_{i-1}\sigma)\) for \(i\geq1\), and \(d_1h(\sigma)=h(d_0\sigma)\) when \(n\geq1\), while for a vertex \(d_1h(i_0)=[-1]\). So with \(\varepsilon(i_0)=1\) and \(s(1)=[-1]\) in degree \(-1\), the maps \(h\) and \(s\) form a contracting homotopy: \(\partial h+h\partial=\mathrm{id}\) in positive degrees and \(\partial h+s\varepsilon=\mathrm{id}\) in degree \(0\), with \(\partial=\sum(-1)^id_i\).

**5.2.** The multiplication \(\mathbb 1\mathbin{\underline\otimes}L\to L\) is nonzero only on the summand of the string of identities of \([-1]\), whose sum with \(\tau\) is \(\tau\), and the unit law forces it to be the identity of \(L_q(\tau)\). So the module structure exists and is unique. In each degree only the summand of the string of identities contributes to \(\Delta^2\mathbb 1\), which is the constant simplicial ring \(\mathbb Z\), so \(N\Delta^2\mathbb 1=\mathbb Z\) and \(\Phi=\Lambda\). The endomorphisms of \(a\) in \(\int C_\bullet(S_0)\) are the pairs of the identity of \([0]\) and an endomorphism of \([1]\) in \(\Delta\), so there are three. Hence \(\operatorname{Hom}(P,P)=P(a)=\mathbb Z^{\operatorname{End}(a)}=\mathbb Z^3\), and \(\operatorname{Hom}_{D(\mathcal M_0)}(P,P)\) is the same, since \(P\) is an object. By Proposition 3.4 (1), \(\Lambda P\cong L\varinjlim P\), and an induced object is colimit-acyclic with colimit \(\mathbb Z\), so \(\Lambda P\cong\mathbb Z\) and \(\operatorname{Hom}(\Lambda P,\Lambda P)=\mathbb Z\). A map \(\mathbb Z^3\to\mathbb Z\) is not injective, so \(\Phi\) is not bijective. The ring \(\mathbb 1\) has flat components and \(P\in D^b\), so the failing hypothesis is \(UF\cong cG\): by Proposition 3.6 (1) it would make \(P\) constant, but \(P\) is \(0\) at \((0,([-1],()))\), which receives no arrow from \(a\), and not at \(a\).

**5.3.** On the summands of the strings starting at \([k_0-1]\) with \(k_0\geq1\), the component of \(cG\) is the constant \(k_0\)-simplicial object \(G\), whose normalization is \(G\) in multidegree \(\mathbf 0\); by Lemma 1.2 (3) of the lesson on multisimplicial objects its reduction is \(0\). On the summands with \(k_0=0\) the component is the object \(G\), which is reduced. So \((cG)^{\mathrm{red}}\) is \(G\) on the strings starting at \([-1]\) and \(0\) elsewhere, and \(cG\to(cG)^{\mathrm{red}}\) is not an isomorphism. By Proposition 1.1 (3), an object in the essential image of \((1)\) is isomorphic to its reduction; so \(cG\) is not in it.

## Sources

The derived categories of modules over rings of type \(C_\bullet(S_a)\), the diagonal differential graded ring \(N\Delta^2R\) and the comparison theorem are due to Illusie, in his work on the cotangent complex. The Eilenberg–Zilber theorem for bisimplicial objects is due to Eilenberg, Mac Lane and Zilber, and in the generality used here to Dold and Puppe, *Homologie nicht-additiver Funktoren. Anwendungen*, Annales de l'Institut Fourier 11 (1961), 201–312 ([Numdam](https://www.numdam.org/articles/10.5802/aif.114/)).
