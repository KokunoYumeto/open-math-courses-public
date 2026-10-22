# The Atiyah class of filtered complexes

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a map of rings \(A\to B\) of a topos, the lesson on the Atiyah class attaches to a simplicial \(B\)-module \(M\) a morphism \(M\to L_{B/A}\otimes^{\mathbf L}_BM[1]\). Chern classes of perfect complexes need this class for complexes with cohomology in positive degrees, written as \(E\to E\otimes^{\mathbf L}_BL_{B/A}[1]\), and for filtered complexes, with the class of a filtered complex inducing the classes of its graded pieces. A filtered complex with filtration in \([0,n]\) is a chain \(F^nE\to\cdots\to F^0E\), that is, a module on the topos of chains of objects of \(T\); the Atiyah class of the chain, taken on that topos, is the filtered Atiyah class. The lesson proves:

- for complexes in degrees \(\leq0\) the class is natural, additive, compatible with base change along squares of rings and along morphisms of topoi, and zero for complexes extended from flat complexes over \(A\);
- normalization identifies filtered simplicial objects of an abelian category with filtered complexes in degrees \(\leq0\), and their localization with \(D^{\leq0}F\);
- the filtered derived category of objects with filtration in \([0,n]\) is equivalent to the derived category of chains of \(n+1\) modules;
- every object \(E\) of \(D^-F(B)\) has a filtered Atiyah class whose underlying morphism is \(\operatorname{at}(E)\) and whose graded pieces are \(\operatorname{at}(\operatorname{gr}^pE)\); the class of a graded object is the sum of the classes of its components;
- \(\operatorname{at}(E[1])=\operatorname{at}(E)[1]\), with no sign in the form \(E\to E\otimes L_{B/A}[1]\);
- the image of \(\operatorname{at}(E)\) in \(E\otimes\Omega_{B/A}[1]\) is the class of the sequence of principal parts of \(B\) over \(A\) tensored with \(E\), which is defined for every complex and every filtered complex.

**Prerequisites.** [*The Atiyah class of a module*](the-atiyah-class-of-a-module.md) (Lemma 1.2, Construction 2.1, Definition 2.2, Proposition 2.3, Corollaries 3.1, 3.3); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md) (Theorem 4.2); [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md) (Proposition 2.4, Lemma 3.2, Proposition 3.10); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Propositions 3.4, 4.2, Corollary 4.3); [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Definition 2.1, Examples 1.2 (b), 5.2 (c), Proposition 3.1); [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md) (Definition 1.1, Propositions 1.2, 2.1, 4.2, Corollary 2.2); [*Filtered derived categories*](filtered-derived-categories.md) (the conventions on cones, Lemma 2.1, Propositions 3.3, 3.5, Definition 5.1); [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md) (Definition 2.1, Proposition 3.2); [*L-series of endomorphisms of perfect complexes*](l-series-of-endomorphisms-of-perfect-complexes.md) (the conventions on \(\tau\) and on shifted morphisms). From the AI-integrated Stacks project: the Dold–Kan theorem [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)]; localization of categories [[Tag 04VB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-section-localization)]; Verdier quotients [[Tag 05R6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-proposition-construct-localization)]; the triangle of a short exact sequence of complexes [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)]; K-flat resolutions [[Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution)]; morphisms out of a bounded above complex of projectives [[Tag 064B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-from-projective-complex)]; the cotangent complex and inverse images of topoi [[Tag 08SV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-pullback-cotangent-morphism-topoi)].

## Conventions

\(T\) is a topos, \(A\to B\) a map of rings of \(T\), \(P=P_A(B)\) the standard resolution, \(L=L_{B/A}\), regarded through normalization as a complex of flat \(B\)-modules in degrees \(\leq0\), \(\Omega=\Omega_{B/A}\), and \(\alpha\colon L\to\Omega\) the augmentation. In \(D(B)\), \(DF(B)\), \(DG(B)\) tensor products are derived and written \(\otimes\); \(\sigma_{X,Y}\) is the symmetry and \(\tau\colon X[a]\otimes Y[b]\to(X\otimes Y)[a+b]\), \(x\otimes y\mapsto(-1)^{b|x|}x\otimes y\), is the isomorphism of the lesson on L-series; \(E\otimes L[1]\) means \(E\otimes(L[1])\), and for a morphism \(g\colon E\to E\otimes M\), \(g[a]\colon E[a]\to E[a]\otimes M\) is the shifted morphism, with \(E[a]\otimes M=(E\otimes M)[a]\) without sign. For complexes \(E\), \(K\) put
\[
\begin{aligned}&\kappa_E=\tau^{-1}\circ\sigma_{K,E}[1]\\
&\quad\colon(K\otimes E)[1]\to E\otimes K[1],\end{aligned}
\]
with \(\tau\colon E\otimes K[1]\to(E\otimes K)[1]\), so that \(\kappa_E(k\otimes e)=(-1)^{|k||e|+|e|}e\otimes k\) for \(k\), \(e\) of degrees \(|k|\), \(|e|\) in \(K\), \(E\); it is natural in \(E\) and \(K\). Cones are \(C(u)^n=Y^n\oplus X^{n+1}\), \(d(y,x)=(dy+u(x),-dx)\) for \(u\colon X\to Y\), and short exact sequences give triangles with the connecting morphism \(\delta=-p\circ q^{-1}\) [Tag 0152], as in the lesson on filtered derived categories. For \(D_\bullet(B)\), the suspension \(\sigma\), the isomorphisms \(\theta\colon N\sigma\to(N-)[1]\) and the identification \(D_\bullet(B)=D^{\leq0}(B)\) we follow the lesson on triangles (Proposition 2.4 there).

## 1. The Atiyah class of a complex in degrees \(\leq0\)

**Definition 1.1.** Let \(E\in D^{\leq0}(B)\), and choose a simplicial \(B\)-module \(M\) with an isomorphism \(NM\cong E\) (Proposition 2.4 of the lesson on triangles). The Atiyah class \(\operatorname{at}_{B/A}(M)\colon M\to\sigma(L\otimes^\ell_BM)\) of Definition 2.2 of the lesson on the Atiyah class gives the morphism of \(D(B)\)
\[
\begin{aligned}&\operatorname{at}^L(E)\colon E\cong NM\xrightarrow{N\operatorname{at}(M)}N\sigma(L\otimes^\ell_BM)\\
&\qquad\xrightarrow{\ \theta\ }N(L\otimes^\ell_BM)[1]\cong(L\otimes E)[1],\end{aligned}
\]
the last isomorphism being that of Proposition 3.4 of the lesson on derived tensor products. The *Atiyah class* of \(E\) is
\[
\begin{aligned}&\operatorname{at}(E)=\operatorname{at}_{B/A}(E)\\
&\quad=\kappa_E\circ\operatorname{at}^L(E)\colon E\to E\otimes L[1].\end{aligned}
\]
By the naturality of \(\operatorname{at}(M)\), \(\theta\) and the isomorphism of Proposition 3.4, \(\operatorname{at}(E)\) does not depend on \(M\). For a \(B\)-module \(E\), \(\operatorname{at}^L(E)\) is the class of the lesson on the Atiyah class.

**Proposition 1.2.** Let \(E,E'\in D^{\leq0}(B)\).

1. (*Naturality*) For \(u\colon E\to E'\), \(\operatorname{at}(E')\circ u=(u\otimes1)\circ\operatorname{at}(E)\), and \(\operatorname{at}(E\oplus E')=\operatorname{at}(E)\oplus\operatorname{at}(E')\).
2. (*Squares of rings*) Let \((A\to B)\to(A'\to B')\) be a commutative square of rings of \(T\), \(c\colon L_{B/A}\otimes B'\to L_{B'/A'}\) the functoriality map, \(E'\in D^{\leq0}(B')\), and \(u\colon E\otimes^{\mathbf L}_BB'\to E'\) a morphism of \(D(B')\). Then
\[
\begin{aligned}&\operatorname{at}_{B'/A'}(E')\circ u\\
&\quad=(u\otimes c[1])\\
&\qquad\circ\bigl(\operatorname{at}_{B/A}(E)\otimes^{\mathbf L}_BB'\bigr).\end{aligned}
\]
3. (*Morphisms of topoi*) For a morphism of topoi \(f\colon T'\to T\), \(f^{-1}\operatorname{at}_{B/A}(E)=\operatorname{at}_{f^{-1}B/f^{-1}A}(f^{-1}E)\), through \(f^{-1}L_{B/A}=L_{f^{-1}B/f^{-1}A}\) [Tag 08SV].
4. If \(E\cong B\otimes_AN\) for a complex \(N\) of flat \(A\)-modules in degrees \(\leq0\), then \(\operatorname{at}(E)=0\).

**Proof.** (1) Proposition 2.3 (1) of the lesson on the Atiyah class, the naturality of \(\theta\) and of Proposition 3.4 of the lesson on derived tensor products, and the naturality of \(\kappa\).

(2) Choose \(M\), \(M'\) for \(E\), \(E'\). By Proposition 4.2 of the lesson on derived tensor products, \(u\) corresponds to a morphism \(v\colon M\to M'\) of \(D_\bullet(B)\), \(M'\) regarded as a \(B\)-module, with \(u=\varepsilon\circ(B'\otimes v)\) for the counit \(\varepsilon\). By the calculus of fractions (Theorem 4.2 (1) of the lesson on simplicial rings and modules) and Proposition 2.3 (1) of the lesson on the Atiyah class, after replacing \(M\) by a quasi-isomorphic simplicial module we may take \(v\) to be a map of simplicial modules. Proposition 2.3 (2) of the lesson on the Atiyah class gives \(\operatorname{at}(M')\circ v=\sigma(c\otimes v)\circ\operatorname{at}(M)\) in \(D_\bullet(B)\); its adjoint form in \(D_\bullet(B')\) is the stated equality, after \(N\), \(\theta\) and \(\kappa\), which are natural and compatible with extension of scalars.

(3) The standard resolution is built from free algebras and the free-algebra adjunction commutes with \(f^{-1}\), so \(f^{-1}P_A(B)=P_{f^{-1}A}(f^{-1}B)\) (proof of [Tag 08SV]). The exact functor \(f^{-1}\) commutes with principal parts, with the sequence (2.1) of the lesson on the Atiyah class, with the cones and maps of Lemma 3.2 of the lesson on triangles, with normalization, \(\theta\) and \(\kappa\).

(4) Choose \(M=B\otimes_AN'\) with \(N'\) the simplicial \(A\)-module of \(N\), whose terms are flat; Proposition 2.3 (3) of the lesson on the Atiyah class applies termwise, as in its proof. \(\square\)

## 2. Filtered complexes, simplicial objects and chains

**Proposition 2.1 (filtered Dold–Puppe).** Let \(\mathcal A\) be an abelian category.

1. Normalization induces an equivalence from the category of simplicial objects of \(\mathcal A\) with finite filtrations by simplicial subobjects to the category of filtered complexes of \(\mathcal A\) concentrated in degrees \(\leq0\) (finite filtrations), with \(N(\operatorname{gr}^pX)=\operatorname{gr}^pNX\). The same holds for graded objects.
2. Call a morphism \(f\) of filtered simplicial objects a *quasi-isomorphism* if every \(N(\operatorname{gr}^pf)\) is a quasi-isomorphism; equivalently, \(Nf\) is a filtered quasi-isomorphism. The localization of filtered simplicial objects at the quasi-isomorphisms is equivalent, through \(N\), to \(D^{\leq0}F(\mathcal A)\), and likewise for graded objects and \(D^{\leq0}G(\mathcal A)\).

**Proof.** (1) \(N\) is an equivalence of abelian categories from simplicial objects of \(\mathcal A\) to chain complexes in degrees \(\geq0\) [Tag 019G], which we regard as complexes in degrees \(\leq0\). An equivalence of abelian categories is exact and induces bijections between the lattices of subobjects, so it carries finite filtrations to finite filtrations and commutes with \(\operatorname{gr}^p\). (2) The equivalence of the two conditions is (1) with Lemma 2.1 of the lesson on filtered derived categories. By (1), the localization of filtered simplicial objects is the localization of the category of filtered complexes with terms in degrees \(\leq0\) at the filtered quasi-isomorphisms, which Proposition 3.3 of the lesson on filtered derived categories, for the interval \([-\infty,0]\), identifies with \(D^{\leq0}F(\mathcal A)\). The graded case is the same. \(\square\)

**Definition 2.2 (chains).** For \(n\geq0\) let \([n]\) be the ordered set \(\{0<1<\cdots<n\}\), regarded as a category. Let \(T_{[n]}\) be the total topos \(\operatorname{Top}\) of the constant fibred topos over \([n]\) with value \(T\) (Examples 1.2 (b) and 5.2 (c) of the lesson on fibred topoi): its objects are the chains \(X_n\to X_{n-1}\to\cdots\to X_0\) of objects of \(T\). For \(0\leq p\leq n\), \(e_p\colon T\to T_{[n]}\) is the morphism of topoi with \(e_p^{-1}X=X_p\) (Proposition 3.1 there), and \(\pi\colon T_{[n]}\to T\) the morphism with \(\pi^{-1}Y\) the constant chain (Proposition 1.2 and Corollary 2.2 of the lesson on modules on total topoi). For a ring \(R\) of \(T\), \(R_{[n]}=\pi^{-1}R\), and an \(R_{[n]}\)-module is a chain of \(R\)-modules (Proposition 4.2 there); tensor products and acyclicity are computed vertex by vertex. By [Tag 08SV], \(L_{B_{[n]}/A_{[n]}}=\pi^{-1}L_{B/A}\).

For complexes of \(R_{[n]}\)-modules and \(0\leq p<n\) put \(G_p(X)=C(X_{p+1}\to X_p)\), and \(G_n(X)=X_n\). These functors preserve quasi-isomorphisms and define functors \(G_p\colon D(R_{[n]})\to D(R)\). For a map of complexes \(f\colon U\to V\), the *mapping cylinder* is \(\operatorname{Cyl}(f)^k=U^k\oplus U^{k+1}\oplus V^k\) with \(d(a,b,c)=(da+b,-db,dc-f(b))\), with the maps \(j(a)=(a,0,0)\), \(q(a,b,c)=f(a)+c\) and \(i(c)=(0,0,c)\).

**Lemma 2.3.** In Definition 2.2, \(j\) is injective, \(q\circ j=f\), \(q\circ i=1_V\), and \(1-i\circ q=dh+hd\) for \(h(a,b,c)=(0,a,0)\); so \(q\) is a homotopy equivalence. The quotient \(\operatorname{Cyl}(f)/j(U)\) is the cone \(C(-f)\), which \((b,c)\mapsto(c,-b)\) identifies with \(C(f)\).

**Proof.** The components of \(d^2(a,b,c)\) are \(d(da+b)-db=0\), \(d^2b=0\) and \(d(dc-f(b))+f(db)=0\), the last because \(f\) is a map of complexes. \(q\) is a map of complexes: \(q(d(a,b,c))=\) \(f(da)+f(b)+dc-f(b)=\) \(d(f(a)+c)\). Then
\[
\begin{aligned}&(dh+hd)(a,b,c)\\
&\quad=(a,-da,-f(a))+(0,da+b,0)\\
&\quad=(a,b,-f(a))\\
&\quad=(1-iq)(a,b,c).\end{aligned}
\]
The quotient has terms \(U^{k+1}\oplus V^k\) and differential \((b,c)\mapsto(-db,dc-f(b))\), which is \(C(-f)\), and \((b,c)\mapsto(c,-b)\) commutes with the differentials of \(C(-f)\) and \(C(f)\). \(\square\)

**Theorem 2.4 (filtered complexes and chains).** Let \(R\) be a ring of \(T\) and \(n\geq0\). The functor \(\Phi_n\) from filtered complexes of \(R\)-modules with filtration in \([0,n]\) to complexes of \(R_{[n]}\)-modules, \(L\mapsto(F^nL\subset\cdots\subset F^0L)\), induces an equivalence
\[
\overline\Phi_n\colon DF^{[0,n]}(R)\longrightarrow D(R_{[n]}),
\]
with the following properties.

1. \(e_p^{-1}\overline\Phi_nL=F^pL\); in particular \(e_0^{-1}\overline\Phi_nL\) is the underlying object of \(L\).
2. There are isomorphisms \(G_p(\overline\Phi_nL)\cong\operatorname{gr}^pL\), natural in \(L\).
3. For \(K\in D(R)\), placed in \(DF(R)\) with filtration in \([0,0]\), \(\overline\Phi_n(L\otimes K)=\overline\Phi_n(L)\otimes\pi^{-1}K\), naturally in \(L\) and \(K\).
4. \(\overline\Phi_n\) commutes with shifts and restricts to an equivalence \(D^{\leq0}F^{[0,n]}(R)\to D^{\leq0}(R_{[n]})\).

**Proof.** Filtered homotopies restrict to homotopies of chains, and a filtered quasi-isomorphism is a quasi-isomorphism on every \(F^p\) (Lemma 2.1 of the lesson on filtered derived categories). So \(\Phi_n\) induces a functor on \(DF^{[0,n]}(R)\), the localization of the filtered complexes with filtration in \([0,n]\) at the filtered quasi-isomorphisms (Proposition 3.5 (1) there).

For a complex \(X\) of \(R_{[n]}\)-modules define complexes \(Y_n=X_n\) and \(Y_p=\operatorname{Cyl}(Y_{p+1}\to X_p)\) for \(p<n\), where \(Y_{p+1}\to X_p\) is \(q\colon Y_{p+1}\to X_{p+1}\) followed by \(X_{p+1}\to X_p\). The maps \(j\) embed \(Y_{p+1}\) in \(Y_p\), and \(\Psi_n(X)=Y_0\), filtered by the images of the \(Y_p\), has filtration in \([0,n]\). The construction is functorial and additive in \(X\). The maps \(q\colon Y_p\to X_p\) are quasi-isomorphisms commuting with the maps of the chains (Lemma 2.3, \(qj=f\)), so they form a quasi-isomorphism \(\Phi_n\Psi_n(X)\to X\), natural in \(X\). For a filtered \(L\) and \(X=\Phi_nL\) they form a filtered map \(\Psi_n\Phi_n(L)\to L\) which is a quasi-isomorphism on every \(F^p\), hence a filtered quasi-isomorphism. A quasi-isomorphism \(X\to X'\) induces quasi-isomorphisms \(Y_p\to Y'_p\), so \(\Psi_n\) carries quasi-isomorphisms to filtered quasi-isomorphisms. A null-homotopic map \(g\colon X\to X'\) factors through \(X\to C(1_X)\), and \(\Psi_n(C(1_X))\) has acyclic \(F^p\), so \(\Psi_n(g)\) factors through a zero object of \(DF(R)\). Hence \(\Psi_n\) induces a functor on the homotopy category, and then on its localization \(D(R_{[n]})\) at the quasi-isomorphisms [Tag 05R6], [Tag 04VB]. The two natural quasi-isomorphisms show that \(\overline\Phi_n\) and the induced \(\overline\Psi_n\) are quasi-inverse.

(1) is clear. (2) For \(p<n\), \(C(F^{p+1}L\to F^pL)\to\operatorname{gr}^pL\), \((y,x)\mapsto\bar y\), is a quasi-isomorphism, natural in \(L\) [Tag 0152]; for \(p=n\), \(G_n=e_n^{-1}\). (3) Represent \(K\) by a K-flat complex; it is filtered K-flat with filtration in \([0,0]\), so \(L\otimes K\) is the complex \(L\otimes K\) with \(F^p(L\otimes K)=F^pL\otimes K\) (Proposition 3.2 of the lesson on filtered tensor products), and \(\pi^{-1}K\) is K-flat on \(T_{[n]}\), tensor products being computed vertex by vertex. (4) \(\Phi_n\) and \(\Psi_n\) commute with shifts, and \(\operatorname{Cyl}\) of maps between complexes in degrees \(\leq0\) is in degrees \(\leq0\). \(\square\)

## 3. The filtered Atiyah class

**Theorem 3.1.** Let \(E\in D^{\leq0}F(B)\) have filtration in \([0,n]\), and let \(\operatorname{at}^F(E)\colon E\to E\otimes L[1]\) be the morphism of \(DF(B)\) that \(\overline\Phi_n\) carries to \(\operatorname{at}_{B_{[n]}/A_{[n]}}(\overline\Phi_nE)\colon\overline\Phi_nE\to\) \(\overline\Phi_nE\otimes\pi^{-1}L[1]=\overline\Phi_n(E\otimes L[1])\) (Theorem 2.4 (3), (4); \(L[1]\) in filtration \([0,0]\)). Then:

1. the underlying morphism of \(\operatorname{at}^F(E)\) is \(\operatorname{at}(E)\);
2. \(\operatorname{gr}^p\operatorname{at}^F(E)=\operatorname{at}(\operatorname{gr}^pE)\) for every \(p\), through \(\operatorname{gr}^p(E\otimes L[1])=\operatorname{gr}^pE\otimes L[1]\);
3. \(\operatorname{at}^F(E)\) is natural in \(E\), and it does not change when \(E\) is regarded as an object with filtration in \([0,n+1]\);
4. for \(E\in D^{\leq0}G(B)\) with components \(E_i\), \(\operatorname{at}(\bigoplus_iE_i)=\bigoplus_i\operatorname{at}(E_i)\) is a morphism of \(DG(B)\).

**Proof.** (1) By Theorem 2.4 (1) the underlying morphism is \(e_0^{-1}\operatorname{at}(\overline\Phi_nE)\), which is \(\operatorname{at}(E)\) by Proposition 1.2 (3) for \(e_0\), since \(e_0^{-1}A_{[n]}=A\), \(e_0^{-1}B_{[n]}=B\).

(2) By Theorem 2.4 (2), \(\operatorname{gr}^p\operatorname{at}^F(E)\) corresponds to \(G_p(\operatorname{at}(X))\), \(X=\Phi_nE\). Let \(X'\subset X\) be the subchain with \(X'_q=F^{\max(q,p+1)}E\) and \(Q=X/X'\), so that \(Q_q=F^qE/F^{\max(q,p+1)}E\): \(Q_{p+1}=0\) and \(Q_p=\operatorname{gr}^pE\). The quotient map \(g\colon X\to Q\) induces an isomorphism \(G_p(X)\to G_p(Q)\), both being identified with \(\operatorname{gr}^pE\). On the objects \(Z\) of \(D(B_{[n]})\) with \(e_{p+1}^{-1}Z\cong0\), the inclusion \(Z_p\to C(Z_{p+1}\to Z_p)\) is a natural isomorphism \(e_p^{-1}\to G_p\); \(Q\) and \(Q\otimes\pi^{-1}L[1]\) are such objects. By Proposition 1.2 (1) on \(T_{[n]}\), \(\operatorname{at}(Q)\circ g=(g\otimes1)\circ\operatorname{at}(X)\), so
\[
\begin{aligned}&G_p(\operatorname{at}(X))\\
&\quad=G_p(g\otimes1)^{-1}\circ G_p(\operatorname{at}(Q))\circ G_p(g)\\
&\quad=G_p(g\otimes1)^{-1}\circ e_p^{-1}\operatorname{at}(Q)\circ G_p(g),\end{aligned}
\]
and \(e_p^{-1}\operatorname{at}(Q)=\operatorname{at}(\operatorname{gr}^pE)\) by Proposition 1.2 (3) for \(e_p\).

(3) Naturality follows from Proposition 1.2 (1) on \(T_{[n]}\). For \([n]\subset[n+1]\), the restriction of chains along the inclusion is the inverse image of a morphism of topoi \(T_{[n]}\to T_{[n+1]}\) (Propositions 1.2 and 2.1 of the lesson on modules on total topoi), which carries \(\Phi_{n+1}E\), whose last term is \(0\), to \(\Phi_nE\); Proposition 1.2 (3) applies.

(4) Proposition 1.2 (1). \(\square\)

An object with filtration in \([a,b]\) has filtration in \([0,b-a]\) after renumbering \(F^p\) as \(F^{p-a}\); \(\operatorname{at}^F\) is defined through this renumbering.

**Corollary 3.2 (shift).** For \(E\in D^{\leq0}(B)\), \(\operatorname{at}(E[1])=\operatorname{at}(E)[1]\), as morphisms \(E[1]\to E[1]\otimes L[1]\). The same holds for \(\operatorname{at}^F\) on \(D^{\leq0}F(B)\).

**Proof.** Represent \(E\) by a complex in degrees \(\leq0\) and let \(Z=C(1_E)\), filtered by \(F^1Z=E\) (the first summand), \(F^0Z=Z\), \(F^2Z=0\). Then \(\operatorname{gr}^1Z=E\), and \((y,x)\mapsto x\) identifies \(\operatorname{gr}^0Z\) with \(E[1]\); both lie in \(D^{\leq0}(B)\). For an object \(X\) with filtration in \([0,1]\), the sequence \(0\to F^1X\to X\to\operatorname{gr}^0X\to0\) has a connecting morphism \(\delta_X\colon\operatorname{gr}^0X\to F^1X[1]\) (Definition 5.1 of the lesson on filtered derived categories). It is natural for morphisms of \(DF(B)\): a filtered map of complexes gives a map of short exact sequences, and a filtered quasi-isomorphism induces quasi-isomorphisms on \(F^1\) and \(\operatorname{gr}^0\) [Tag 0152]. For \(Z\), a cycle \(z\) of \(E[1]\) lifts to the cycle \(((0,z),-z)\) of the cone of \(F^1Z\to Z\), so \(\delta_Z=-(-z)\) is the identity of \(E[1]\). For \(Z\otimes L[1]=C(1_{E\otimes L[1]})\), with \((y,x)\otimes l\mapsto(y\otimes l,x\otimes l)\), the same computation gives the identity of \(E[1]\otimes L[1]\). Naturality of \(\delta\) for \(f=\operatorname{at}^F(Z)\) gives \(\delta_{Z\otimes L[1]}\circ\operatorname{gr}^0f=\operatorname{gr}^1f[1]\circ\delta_Z\), that is \(\operatorname{at}(E[1])=\operatorname{at}(E)[1]\) by Theorem 3.1 (2). The filtered statement follows from the statement on \(T_{[n]}\), since \(\overline\Phi_n\) is fully faithful and commutes with shifts. \(\square\)

**Definition 3.3.** For \(E\in D^-(B)\) (resp. \(D^-F(B)\)) choose \(k\) with \(E[k]\) in \(D^{\leq0}(B)\) (resp. \(D^{\leq0}F(B)\)) and put \(\operatorname{at}(E)=\operatorname{at}(E[k])[-k]\) (resp. \(\operatorname{at}^F(E)=\operatorname{at}^F(E[k])[-k]\)). By Corollary 3.2 this does not depend on \(k\).

**Proposition 3.4.** On \(D^-(B)\), \(D^-F(B)\) and \(D^-G(B)\), the Atiyah class satisfies Proposition 1.2 (1)–(3), Theorem 3.1 (1)–(4), and \(\operatorname{at}(E[k])=\operatorname{at}(E)[k]\) for every integer \(k\).

**Proof.** Each statement is compatible with shifting by \(k\), and holds after a shift by Proposition 1.2, Theorem 3.1 and Corollary 3.2. \(\square\)

**Remark 3.5 (the other form).** In the form \(\operatorname{at}^L(E)\colon E\to(L\otimes E)[1]\) of Definition 1.1, Corollary 3.2 reads
\[
\operatorname{at}^L(E[1])=-\tau[1]^{-1}\circ\operatorname{at}^L(E)[1],
\]
with \(\tau\colon L\otimes E[1]\to(L\otimes E)[1]\), \(l\otimes e\mapsto(-1)^{|l|}l\otimes e\). Indeed, on \(e\otimes l\) with \(e\), \(l\) of degrees \(i\), \(j\) in \(E\), \(L\), the composite \(\kappa_{E[1]}\circ\tau[1]^{-1}\circ\kappa_E[1]^{-1}\) is multiplication by \((-1)^{(ij+i)+j+(j(i-1)+(i-1))}=-1\), so \(\kappa_{E[1]}^{-1}\circ\kappa_E[1]=-\tau[1]^{-1}\). Applied twice, the formula gives \(\operatorname{at}^L(E[2])=\operatorname{at}^L(E)[2]\), the two signs \(-1\) and the two factors \((-1)^{|l|}\) cancelling.

## 4. Principal parts of \(B\)

By Lemma 1.2 of the lesson on the Atiyah class, \(0\to\Omega\to P^1_{B/A}\to B\to0\) is an exact sequence of \(B\)-bimodules which splits as a sequence of right \(B\)-modules. So for every complex \(F\) of \(B\)-modules,
\[
\begin{aligned}&0\to\Omega\otimes_BF\\
&\quad\to P^1_{B/A}\otimes_BF\\
&\quad\to F\to0,\end{aligned}\tag{4.1}
\]
formed with the right structure of \(P^1_{B/A}\), is an exact sequence of complexes of \(B\)-modules, functorial in \(F\), and exact on every filtration step and graded piece when \(F\) is filtered.

**Definition 4.1.** For \(E\in D(B)\), represent \(E\) by a K-flat complex \(F\) [Tag 06YS]. The *principal parts class* \(\operatorname{at}^\Omega(E)\colon E\to E\otimes\Omega[1]\) is \(\kappa_E\) composed with the connecting morphism \(E\to(\Omega\otimes E)[1]\) of (4.1). For \(E\in DF(B)\), represented by a filtered K-flat complex \(F\) (Definition 2.1 of the lesson on filtered tensor products), (4.1) is a sequence of filtered complexes with exact graded pieces, and its connecting morphism in \(DF(B)\), composed with \(\kappa\), is \(\operatorname{at}^{\Omega,F}(E)\).

A quasi-isomorphism of K-flat complexes induces a map of the sequences (4.1) whose first component is a quasi-isomorphism, so \(\operatorname{at}^\Omega(E)\) does not depend on \(F\) and is natural in \(E\); the same holds for filtered complexes, and \(\operatorname{gr}^p\operatorname{at}^{\Omega,F}(E)=\operatorname{at}^\Omega(\operatorname{gr}^pE)\), the sequence (4.1) of \(\operatorname{gr}^pF\) being \(\operatorname{gr}^p\) of the sequence of \(F\).

**Proposition 4.2.**

1. For every \(E\in D(B)\), \(\operatorname{at}^\Omega(E[1])=\operatorname{at}^\Omega(E)[1]\).
2. For \(E\in D^-(B)\), \((1\otimes\alpha[1])\circ\operatorname{at}(E)=\operatorname{at}^\Omega(E)\); for \(E\in D^-F(B)\), \((1\otimes\alpha[1])\circ\operatorname{at}^F(E)=\operatorname{at}^{\Omega,F}(E)\).

**Proof.** (1) The sequence (4.1) of \(F[1]\) is the sequence of \(F\) shifted, with the same maps, because \(\Omega\) is in degree \(0\). The connecting morphism of a shifted sequence is \(-\delta[1]\): the isomorphism \(C(u[1])\to C(u)[1]\), \((y,x)\mapsto(y,-x)\), carries \(p\) to \(-p[1]\) and \(q\) to \(q[1]\). And \(\kappa_{F[1]}=-\kappa_F[1]\), since \(\kappa_F(\omega\otimes e)=(-1)^{|e|}e\otimes\omega\) for \(\omega\) in degree \(0\). The two signs cancel.

(2) By (1), Corollary 3.2 and Definition 3.3 we may assume \(E\in D^{\leq0}(B)\), represented by a complex \(F\) of flat \(B\)-modules in degrees \(\leq0\), and \(F=NM\) with \(M\) the simplicial module of \(F\). By Corollary 3.1 (1) of the lesson on the Atiyah class, \(\sigma(\alpha\otimes1)\circ\operatorname{at}(M)\) is the third map of the triangle of the sequence \(0\to\Omega\otimes_BM\to P^1_{B/A}(M)\to M\to0\) of simplicial \(B\)-modules, and by Proposition 3.10 (1) of the lesson on triangles, \(\theta\circ N\) of that third map is the connecting morphism of the normalized sequence, which is (4.1) for \(F\). Composing with \(\kappa\) gives the first statement. The filtered statement follows in the same way on \(T_{[n]}\), where the sequence (4.1) of the chain \(\Phi_nF\) is \(\Phi_n\) of the filtered sequence (4.1) of \(F\), through Theorem 2.4. \(\square\)

**Remark 4.3.** When \(\alpha\) is a quasi-isomorphism and \(\Omega\) is flat, for instance for a polynomial algebra \(B\) over \(A\) or for \(A\to B\) induced by a smooth morphism of schemes, Proposition 4.2 (2) determines \(\operatorname{at}(E)\) by \(\operatorname{at}^\Omega(E)\), as in Corollary 3.3 of the lesson on the Atiyah class.

## 5. Exercises

**Exercise 5.1.** Let \(T\) be the punctual topos, \(A=k\) a field, \(B=k[x]\) and \(E=k=B/(x)\). Show that \(P^1_{B/A}\otimes_Bk\cong B/(x^2)\) as a left \(B\)-module, that (4.1) for \(F=k\) is the extension \(0\to k\,dx\to B/(x^2)\to k\to0\), and that \(\operatorname{at}(k)\ne0\).

**Exercise 5.2.** In the situation of Exercise 5.1, let \(F\) be the complex \(B\xrightarrow{x}B\) in degrees \(-1,0\), a free resolution of \(k\). Choose \(B\)-linear splittings of (4.1) in each degree and compute the connecting morphism \(F\to(\Omega\otimes F)[1]\) as a map of complexes. Do the same for \(F[1]\) with the same splittings, and check by hand the two signs of the proof of Proposition 4.2 (1).

**Exercise 5.3.** Prove the identities of Lemma 2.3 for \(U=V=A\) in degree \(0\) and \(f\) the multiplication by an element \(s\), by writing \(\operatorname{Cyl}(f)\) as a complex of free modules in degrees \(-1\) and \(0\).

## 6. Complete solutions

**Solution 5.1.** \(P^1_{B/A}=(B\otimes_kB)/J^2\) is free as a left \(B\)-module on \(1\) and \(\mathrm dx=1\otimes x-x\otimes1\). The right action of \(x\) is \((a+b\,\mathrm dx)\cdot x=ax+a\,\mathrm dx+bx\,\mathrm dx\), because \(1\otimes x=x\otimes1+\mathrm dx\) and \(\mathrm dx\cdot\mathrm dx=0\). So \(P^1_{B/A}\otimes_Bk=P^1_{B/A}/P^1_{B/A}x\) is the left \(B\)-module on \(e=1\), \(f=\mathrm dx\) with the relations \(xe+f=0\) and \(xf=0\). Hence \(f=-xe\), \(x^2e=0\), and \(e\mapsto1\) gives \(P^1_{B/A}\otimes_Bk\cong B/(x^2)\), with \(\Omega\otimes_Bk=k\,\mathrm dx\) mapped to \(xB/(x^2)\) by \(\mathrm dx\mapsto-x\). The extension \(0\to k\to B/(x^2)\to k\to0\) does not split, since \(x\) acts nontrivially on \(B/(x^2)\) and by \(0\) on \(k\oplus k\); its class in \(\operatorname{Ext}^1_B(k,k\,\mathrm dx)\) is nonzero. A free resolution \(F\to k\) induces a map from the sequence (4.1) of \(F\) to that of \(k\), whose first component \(\Omega\otimes F\to\Omega\otimes k\) is a quasi-isomorphism because \(\Omega=B\,\mathrm dx\) is free; so \(\operatorname{at}^\Omega(k)\) is \(\kappa\) composed with the class of this extension, and it is nonzero. For a polynomial algebra \(\alpha\) is an isomorphism \(L_{B/A}\to\Omega_{B/A}\), so by Proposition 4.2 (2), \(\operatorname{at}(k)\ne0\).

**Solution 5.2.** For an exact sequence of complexes \(0\to X\xrightarrow{u}Y\xrightarrow{v}Z\to0\) with maps \(s\colon Z^n\to Y^n\), \(vs=1\), in each degree, \(\zeta(z)=(s(z),-u^{-1}(ds(z)-s(dz)))\) is a map of complexes \(Z\to C(u)\) with \(q\zeta=1\), so \(\zeta\) is inverse to \(q\) in \(D(B)\), and the connecting morphism is \(\delta=-p\zeta\colon z\mapsto u^{-1}(ds(z)-s(dz))\). Write \(F^{-1}=Be_1\), \(F^0=Be_0\), \(d(e_1)=xe_0\). In each degree \(s(e_i)=1\otimes e_i\) is a \(B\)-linear splitting of \(P^1_{B/A}\otimes F^i\to F^i\). In \(P^1_{B/A}\otimes_BF\), \(d(1\otimes e_1)=1\otimes xe_0=(x+\mathrm dx)\otimes e_0\), since \((1\otimes1)\cdot x=x(1\otimes1)+\mathrm dx\) in \(P^1_{B/A}\), while \(s(de_1)=x(1\otimes e_0)\). So \(\delta(e_1)=\mathrm dx\otimes e_0\) and \(\delta(e_0)=0\). This map \(F\to(\Omega\otimes F)[1]\) is not null-homotopic: a homotopy with \(h(e_1)=c\,\mathrm dx\otimes e_1\), \(h(e_0)=c'\,\mathrm dx\otimes e_0\) gives \((dh+hd)(e_1)=\) \(x(c'-c)\,\mathrm dx\otimes e_0\ne\mathrm dx\otimes e_0\); and \(F\) is a bounded complex of free modules, so \(\operatorname{Hom}_{D(B)}(F,-)=\operatorname{Hom}_{K(B)}(F,-)\) [Tag 064B]. With \(\kappa_F(\mathrm dx\otimes e_0)=e_0\otimes\mathrm dx\) (\(|e_0|=0\)), \(\operatorname{at}^\Omega(F)\) sends \(e_1\) to \(e_0\otimes\mathrm dx\).

For \(F[1]\) the terms are \(Be_1\) in degree \(-2\) and \(Be_0\) in degree \(-1\), with differential \(-d\), and the same splittings give \(d(1\otimes e_1)-s(d e_1)=\) \(-(x+\mathrm dx)\otimes e_0+x(1\otimes e_0)=\) \(-\mathrm dx\otimes e_0\): the connecting morphism of the shifted sequence is \(-\delta[1]\). Since \(|e_0|=-1\) in \(F[1]\), \(\kappa_{F[1]}(\mathrm dx\otimes e_0)=-e_0\otimes\mathrm dx\), so \(\kappa_{F[1]}=-\kappa_F[1]\). Hence \(\operatorname{at}^\Omega(F[1])\) sends \(e_1\) to \((-1)(-1)\,e_0\otimes\mathrm dx=e_0\otimes\mathrm dx\), which is \(\operatorname{at}^\Omega(F)[1]\), as in Proposition 4.2 (1).

**Solution 5.3.** \(\operatorname{Cyl}(f)\) has \(A\oplus A\) in degree \(0\) (coordinates \(a\), \(c\)) and \(A\) in degree \(-1\) (coordinate \(b\)), with \(d(b)=(b,-sb)\). Then \(j(a)=(a,0)\), \(q(a,c)=sa+c\), \(i(c)=(0,c)\), \(qj=s=f\), \(qi=1\), and \(h(a,c)=a\) in degree \(-1\): \((dh)(a,c)=(a,-sa)=(1-iq)(a,c)\) in degree \(0\), and \((hd)(b)=b=(1-iq)(b)\) in degree \(-1\). The quotient by \(j(A)\) is \(A\xrightarrow{-s}A\), the cone of \(-f\).

## Sources

The Atiyah class of complexes, its version for filtered complexes with the compatibility with graded pieces, and its use for Chern classes are due to Illusie, in his work on the cotangent complex, where the filtered class is obtained from filtered simplicial modules and a filtered extension of scalars whose details are left to the reader; here it is obtained from the class on the topos of chains. The class of a module and its relation to principal parts and connections go back to Atiyah, for holomorphic vector bundles. The normalization of simplicial objects is the Dold–Kan correspondence.
