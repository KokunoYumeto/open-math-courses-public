# Décalage, nerves and the homotopy type of a category

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cohomology of diagrams, which governs the deformations of diagrams of ringed topoi and of group schemes, uses three simplicial constructions. The first is the décalage of a simplicial object, obtained by forgetting its last or its first face operator. It is homotopically trivial over its augmentation. The second is the nerve of a category, and more generally of a category object in a category with fibre products. Nerves are recognized by cartesian conditions on their décalages, and groupoids and monoid actions by further cartesian conditions. The third is Quillen's theorem that small categories and simplicial sets have the same homotopy theory.

This lesson proves the first two in the generality needed later: simplicial objects of an arbitrary category, and internal categories, groupoids and monoid actions in a category with fibre products. For the third it uses the results proved in [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), and deduces that a category and its opposite have the same homotopy type. Two limits of the theory are also established. The diagonal of the total décalage need not be homotopy equivalent to the original simplicial object, and a nerve is not characterized by its data in dimensions at most two.

**Prerequisites.** [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), Sections 1–3 and 5.4; [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), Sections 1, 3 and 5.3; homotopies of simplicial objects in an arbitrary category [[Stacks, Tag 019L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-relations-homotopy), [Tag 019M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-remark-homotopy-better)]; the normalized chain complex and the Dold–Kan theorem [[Stacks, Tag 0194](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-complexes), [Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)].

## 1. Décalage

### 1.1. Shifting a simplicial object

Let \(\bar\Delta\) be the category of finite totally ordered sets, the empty set included, with increasing maps, and let \(\Delta\subset\bar\Delta\) be the full subcategory of nonempty ones. Write \([n]=\{0<1<\cdots<n\}\) and \([-1]=\varnothing\). For totally ordered sets \(E,F\), let \(E\sqcup F\) be their disjoint union, ordered so that every element of \(E\) precedes every element of \(F\). For \(p,q\geq0\) define
\[
\begin{gathered}\operatorname{Dec}^p_q\colon\bar\Delta\to\bar\Delta,\\\operatorname{Dec}^p_q(E)=[q-1]\sqcup E\sqcup[p-1],\end{gathered}
\]
acting on maps by the identity of the added parts. Up to the canonical isomorphisms \([q-1]\sqcup[q'-1]\cong[q+q'-1]\), these functors commute and \(\operatorname{Dec}^p_q\operatorname{Dec}^{p'}_{q'}=\operatorname{Dec}^{p+p'}_{q+q'}\). Write \(\operatorname{Dec}^p=\operatorname{Dec}^p_0\) and \(\operatorname{Dec}_q=\operatorname{Dec}^0_q\). Thus \(\operatorname{Dec}^1(E)=E\sqcup[0]\) adds a greatest element and \(\operatorname{Dec}_1(E)=[0]\sqcup E\) adds a least element. Reversing the order, \(E\mapsto E^{\mathrm{op}}\), is an involution of \(\bar\Delta\), and it exchanges \(\operatorname{Dec}^1\) and \(\operatorname{Dec}_1\).

A simplicial object \(X\) of a category \(C\) is a functor \(\Delta^{\mathrm{op}}\to C\), and an augmented simplicial object is a functor \(\bar\Delta^{\mathrm{op}}\to C\). When \(p+q\geq1\), the functor \(\operatorname{Dec}^p_q\) takes \(\bar\Delta\) into \(\Delta\), so
\[
\operatorname{Dec}^p_q(X)=X\circ\operatorname{Dec}^p_q
\]
is an augmented simplicial object of \(C\). Its value at \(\varnothing\) is \(X([q-1]\sqcup[p-1])=X_{p+q-1}\). In particular \(\operatorname{Dec}^1(X)_n=\operatorname{Dec}_1(X)_n=X_{n+1}\) for \(n\geq-1\). In degree \(n\), the face and degeneracy operators of \(\operatorname{Dec}^1(X)\) are the \(d_i,s_i\) of \(X\) with \(i\leq n\), and those of \(\operatorname{Dec}_1(X)\) are \(d_{i+1},s_{i+1}\). So \(\operatorname{Dec}^1(X)\) forgets the last face operator of \(X\), and \(\operatorname{Dec}_1(X)\) forgets the first. The augmentation \(X_1\to X_0\) is \(d_0\) for \(\operatorname{Dec}^1(X)\) and \(d_1\) for \(\operatorname{Dec}_1(X)\). All of this applies to cosimplicial objects, with \(\Delta\) in place of \(\Delta^{\mathrm{op}}\).

**Homotopies.** Let \(a,b\colon U\to V\) be morphisms of simplicial objects of an arbitrary category. A *homotopy from \(a\) to \(b\)* is a family of morphisms \(h_{n,\alpha}\colon U_n\to V_n\), one for each \(n\geq0\) and each increasing \(\alpha\colon[n]\to[1]\), such that \(h_{n,0}=a_n\) and \(h_{n,1}=b_n\) for the constant maps \(0\) and \(1\), and, for every increasing \(\varphi\colon[m]\to[n]\),
\[
\begin{aligned}&V(\varphi)\circ h_{n,\alpha}\\&\quad=h_{m,\alpha\varphi}\circ U(\varphi).\end{aligned}
\tag{1.1}
\]
Faces and degeneracies generate \(\Delta\), so (1.1) is equivalent to the relations of [Stacks, Tag 019L]. This is the notion of homotopy of [Stacks, Tag 019M]; when \(C\) has finite coproducts, it is the same as a morphism \(U\times\Delta[1]\to V\). Two morphisms are *homotopic* if they are related by the equivalence relation generated by homotopies. This relation is compatible with composition and with every functor \(C\to C'\). A morphism \(f\colon U\to V\) is a *homotopy equivalence* if there is \(g\colon V\to U\) with \(gf\) and \(fg\) homotopic to the identities. If \(U\) and \(V\) are augmented to the same object \(S\), and \(f\), \(g\) and all the homotopies are compatible with the augmentations, \(f\) is an *\(S\)-homotopy equivalence*.

**Proposition 1.1.** Let \(X\) be a simplicial object of \(C\). Let \(\varepsilon\colon\operatorname{Dec}^1(X)\to X_0\) be the augmentation, with \(X_0\) regarded as a constant simplicial object. Let \(\sigma\colon X_0\to\operatorname{Dec}^1(X)\) be given in degree \(n\) by \(X\) of the unique map \([n]\sqcup[0]\to[0]\). Then \(\varepsilon\sigma=1\), and there is a homotopy from \(1\) to \(\sigma\varepsilon\) compatible with \(\varepsilon\). So \(\varepsilon\) is an \(X_0\)-homotopy equivalence. The same holds for \(\operatorname{Dec}_1(X)\), for every \(\operatorname{Dec}^p_q(X)\) with \(p+q\geq1\) over \(X_{p+q-1}\), and for cosimplicial objects.

**Proof.** Write \(\ast\) for the added greatest element of \(E\sqcup[0]\). The composite \([0]\to E\sqcup[0]\to[0]\) is the identity, so \(\varepsilon\sigma=1\). For \(E\) in \(\Delta\) and an increasing \(f\colon E\to[1]\), let \(u_f\colon E\sqcup\{\ast\}\to E\sqcup\{\ast\}\) be the identity on \(f^{-1}(0)\) and send \(f^{-1}(1)\cup\{\ast\}\) to \(\ast\). It is increasing, because \(f^{-1}(1)\) is a final segment of \(E\). For \(g\colon E'\to E\) in \(\Delta\),
\[
\begin{aligned}&(g\sqcup\ast)\circ u_{fg}\\&\quad=u_f\circ(g\sqcup\ast),\end{aligned}
\tag{1.2}
\]
since both sides send \(e'\in E'\) to \(g(e')\) if \(f(g(e'))=0\) and to \(\ast\) otherwise, and both fix \(\ast\). By (1.2), the morphisms \(h_{n,f}=X(u_f)\) satisfy (1.1) for \(U=V=\operatorname{Dec}^1(X)\). The map \(u_0\) is the identity, and \(u_1\) is the composite \(E\sqcup\ast\to[0]\to E\sqcup\ast\), so \(X(u_1)=\sigma\varepsilon\). Every \(u_f\) fixes \(\ast\), so \(\varepsilon\circ X(u_f)=\varepsilon\). This proves the statement for \(\operatorname{Dec}^1(X)\), and the involution \(E\mapsto E^{\mathrm{op}}\) carries it to \(\operatorname{Dec}_1(X)\). For \(p\geq1\), \(\operatorname{Dec}^p_q(X)=\operatorname{Dec}^1(\operatorname{Dec}^{p-1}_q(X))\), and the degree-\(0\) term of \(\operatorname{Dec}^{p-1}_q(X)\) is \(X([q-1]\sqcup[0]\sqcup[p-2])=X_{p+q-1}\), with the same augmentation. For \(p=0\), use \(\operatorname{Dec}_q=\operatorname{Dec}_1\operatorname{Dec}_{q-1}\) in the same way. Cosimplicial objects of \(C\) are simplicial objects of \(C^{\mathrm{op}}\). \(\square\)

**Corollary 1.2.** Let \(C\) be additive and \(X\) a simplicial object of \(C\).

1. The augmented chain complex of \(\operatorname{Dec}_1(X)\) is contractible, and the maps \(s_0\colon X_m\to X_{m+1}\) form a contracting homotopy. This complex is \(\cdots\to X_2\to X_1\to X_0\to0\), with differential \(\sum_{i=0}^n(-1)^id_{i+1}\colon X_{n+1}\to X_n\); for \(n=0\) this is the augmentation \(d_1\).
2. The augmented chain complex of \(\operatorname{Dec}^1(X)\) is contractible, and the maps \((-1)^ms_m\colon X_m\to X_{m+1}\) form a contracting homotopy. Its differential is \(\sum_{i=0}^n(-1)^id_i\colon X_{n+1}\to X_n\); for \(n=0\) this is the augmentation \(d_0\).

**Proof.** Write \(\partial\) for the differential. (1) The simplicial identities give \(d_1s_0=1\) and \(d_{i+1}s_0=s_0d_i\) for \(i\geq1\). On \(X_{n+1}\) the differential is \(\sum_{i=1}^{n+1}(-1)^{i-1}d_i\), and on \(X_0\) it is \(0\). Hence, on \(X_{n+1}\) with \(n\geq-1\),
\[
\begin{aligned}\partial s_0&=\sum_{i=0}^{n+1}(-1)^id_{i+1}s_0\\&=1+\sum_{i=1}^{n+1}(-1)^is_0d_i=1-s_0\partial.\end{aligned}
\]
(2) On \(X_{n+1}\), the identities \(d_{n+1}s_{n+1}=1\) and \(d_is_{n+1}=s_nd_i\) for \(i\leq n\) give
\[
\begin{aligned}\partial s_{n+1}&=\sum_{i=0}^{n}(-1)^is_nd_i+(-1)^{n+1}\\&=s_n\partial+(-1)^{n+1},\end{aligned}
\]
where \(s_n\partial\) is read as \(0\) for \(n=-1\). Multiplying by \((-1)^{n+1}\) shows that the maps \(H=(-1)^ms_m\) on \(X_m\) satisfy \(\partial H+H\partial=1\). \(\square\)

### 1.2. The total décalage

For a simplicial object \(X\) of \(C\), the *total décalage* is the functor \((E,F)\mapsto X(E\sqcup F)\) on pairs of objects of \(\bar\Delta\) that are not both empty. Restricted to \(\Delta\times\Delta\), it is a bisimplicial object \(\operatorname{Dec}^+(X)\) with \(\operatorname{Dec}^+(X)_{p,q}=X_{p+q+1}\). Its \(p\)-th column \(F\mapsto X([p]\sqcup F)\) is \(\operatorname{Dec}_{p+1}(X)\), augmented to \(X_p\). Its \(q\)-th row \(E\mapsto X(E\sqcup[q])\) is \(\operatorname{Dec}^{q+1}(X)\), augmented to \(X_q\). Its diagonal is the simplicial object \(\operatorname{dec}(X)\colon E\mapsto X(E\sqcup E)\), with \(\operatorname{dec}(X)_n=X_{2n+1}\). The inclusions of \(E\) as the first and as the second copy in \(E\sqcup E\) are natural in \(E\), and define morphisms
\[
h,v\colon\operatorname{dec}(X)\rightrightarrows X,
\]
the restrictions of the two augmentations to the diagonal.

**Proposition 1.3.** There is a homotopy from \(h\) to \(v\).

**Proof.** For an increasing \(f\colon E\to[1]\), let \(w_f\colon E\to E\sqcup E\) send \(e\) to \(e\) in the first copy if \(f(e)=0\), and to \(e\) in the second copy if \(f(e)=1\). It is increasing, since \(f^{-1}(0)\) precedes \(f^{-1}(1)\) in \(E\) and the first copy precedes the second. For \(g\colon E'\to E\), we have \((g\sqcup g)\circ w_{fg}=w_f\circ g\). Hence the morphisms \(X(w_f)\colon X(E\sqcup E)\to X(E)\) satisfy (1.1). Since \(w_0\) is the inclusion of the first copy and \(w_1\) that of the second, they form a homotopy from \(h\) to \(v\). \(\square\)

**Example 1.4 (the diagonal need not be equivalent).** In general, neither \(h\) nor \(v\) is a homotopy equivalence. Let \(C=\Delta^{\mathrm{op}}\), and let \(X\) be the simplicial object of \(C\) given by the identity functor of \(\Delta^{\mathrm{op}}\). A morphism \(X\to\operatorname{dec}(X)\) is a family of increasing maps \(r_E\colon E\sqcup E\to E\), natural in \(E\in\Delta\). For \(e\in E\), naturality with respect to \(e\colon[0]\to E\) forces \(r_E\) to send both copies of \(e\) to \(e\). For \(E=[1]\), the element \(1\) of the first copy precedes the element \(0\) of the second copy, but \(r_E\) would send them to \(1>0\). So there is no morphism \(X\to\operatorname{dec}(X)\) at all, and \(h\) and \(v\) have no homotopy inverses. The same example, read in \(\Delta\), gives the corresponding statement for cosimplicial objects.

## 2. Nerves

### 2.1. Nerves of small categories

Regard a totally ordered set as a category. The nerve \(N(C)\) of a small category \(C\) is the simplicial set \(E\mapsto\operatorname{Fun}(E,C)\). Thus \(N_0(C)\) is the set of objects. For \(n\geq1\), \(N_n(C)\) is the set of strings \((x_1,\ldots,x_n)\) of arrows \(x_i\colon c_{i-1}\to c_i\). On \(N_1(C)\), \(d_0\) is the target and \(d_1\) the source. For \(n\geq1\), \(d_0\) drops \(x_1\), \(d_n\) drops \(x_n\), \(d_i\) for \(0<i<n\) replaces \(x_i,x_{i+1}\) by \(x_{i+1}x_i\), and \(s_i\) inserts the identity of \(c_i\) between \(x_i\) and \(x_{i+1}\). The nerve functor is fully faithful ([*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), Proposition 2.1). It commutes with limits, because each \(\operatorname{Fun}(E,-)\) does.

For a simplicial object \(K\), let \(K^{\mathrm{op}}=K\circ\mathrm{op}\), where \(\mathrm{op}\) is the involution \(E\mapsto E^{\mathrm{op}}\) of \(\Delta\). Concretely \(K^{\mathrm{op}}_n=K_n\), with \(d_i\) and \(s_i\) replaced by \(d_{n-i}\) and \(s_{n-i}\). Since \(\operatorname{Fun}(E,C^{\mathrm{op}})=\operatorname{Fun}(E^{\mathrm{op}},C)\),
\[
N(C^{\mathrm{op}})=N(C)^{\mathrm{op}}.
\tag{2.1}
\]

**Proposition 2.1.** Let \(F,G\colon C\rightrightarrows D\) be functors of small categories. The nerve gives a bijection from natural transformations \(F\to G\) to homotopies from \(N(F)\) to \(N(G)\), that is, to morphisms \(\Delta[1]\times N(C)\to N(D)\) restricting to \(N(F)\) on \(\{0\}\times N(C)\) and to \(N(G)\) on \(\{1\}\times N(C)\).

**Proof.** A natural transformation \(F\to G\) is a functor \([1]\times C\to D\) restricting to \(F\) and \(G\). Since \(N([1]\times C)=\Delta[1]\times N(C)\) and \(N\) is fully faithful, these functors correspond to the morphisms described. \(\square\)

**Corollary 2.2.** If \(C\) has a final or an initial object, the identity of \(N(C)\) is homotopic to a constant map, so \(|N(C)|\) is contractible. In particular every \(\Delta[n]=N([n])\) is contractible.

**Proof.** For a final object \(t\), the arrows \(c\to t\) form a natural transformation from the identity to the constant functor at \(t\). For an initial object, use the arrows out of it. Apply Proposition 2.1. \(\square\)

### 2.2. Décalage of a nerve

For an object \(c\) of \(C\), let \(c/C\) be the category of arrows \(c\to c'\), and \(C/c\) the category of arrows \(c'\to c\), with commutative triangles as morphisms.

**Proposition 2.3.** There are isomorphisms of augmented simplicial sets
\[
\begin{gathered}\operatorname{Dec}_1N(C)\cong\coprod_{c}N(c/C),\\\operatorname{Dec}^1N(C)\cong\coprod_{c}N(C/c),\end{gathered}
\]
under which the augmentations to \(N_0(C)=\operatorname{Ob}(C)\) send the component of \(c\) to \(c\). In particular, the décalage of a nerve is again a nerve.

**Proof.** An \(n\)-simplex of \(\operatorname{Dec}_1N(C)\) is a functor \([0]\sqcup[n]\to C\), that is, a string \(c\to c_0\to\cdots\to c_n\), which is an \(n\)-simplex of \(N(c/C)\). The faces and degeneracies of \(\operatorname{Dec}_1N(C)\) do not touch the added least vertex, and they are those of \(N(c/C)\). The augmentation is the restriction to the added vertex. The second isomorphism is the first applied to \(C^{\mathrm{op}}\), using (2.1). \(\square\)

Each \(c/C\) has the initial object \(1_c\), and each \(C/c\) has the final object \(1_c\). So Corollary 2.2, applied to each component, gives a second proof of Proposition 1.1 for nerves.

### 2.3. Internal categories and their nerves

Let \(T\) be a category with fibre products. An *internal category* \(X\) of \(T\) consists of objects \(X_0\) (objects) and \(X_1\) (arrows) of \(T\), morphisms \(d_0\) (target) and \(d_1\) (source) from \(X_1\) to \(X_0\), a morphism \(s_0\colon X_0\to X_1\) (identities), and a composition morphism
\[
X_1\times_{X_0}X_1\to X_1.
\]
Here the fibre product is taken over \(d_0\) on the first factor and \(d_1\) on the second, so that its points are pairs \((x,y)\) with \(y\) composable after \(x\). The composite is written \(yx\). The usual axioms are required as equalities of morphisms: sources and targets of identities and of composites, associativity, and the two unit laws. Equivalently, by the Yoneda lemma, \(X\) is a presheaf of categories \(S\mapsto X(S)\) on \(T\) whose presheaves of objects and of arrows are represented by \(X_0\) and \(X_1\). A functor \(X\to X'\) is a pair of morphisms \(X_0\to X_0'\) and \(X_1\to X_1'\) compatible with the structure. These form a category \(\operatorname{Cat}(T)\).

The *nerve* of \(X\) is the simplicial object \(N(X)\) of \(T\) with \(N_0(X)=X_0\) and
\[
N_n(X)=X_1\times_{X_0}X_1\times_{X_0}\cdots\times_{X_0}X_1,
\]
with \(n\) factors and the conventions above, and with faces and degeneracies given by the formulas of Section 2.1. For every object \(S\) of \(T\), the simplicial set \(\operatorname{Hom}(S,N(X))\) is the nerve of the category \(X(S)\). In particular, all simplicial identities hold.

For a simplicial object \(Y\) of \(T\) and \(n\geq2\), the *Segal map* is
\[
Y_n\to Y_1\times_{Y_0}\cdots\times_{Y_0}Y_1,
\tag{2.2}
\]
given by the \(n\) edges \((i-1,i)\), \(1\leq i\leq n\). For a finite nonempty totally ordered set \(F\), write \(Y(F)\) for the value of \(Y\) at \(F\). For \(G\subseteq F\), the inclusion induces the *restriction* \(Y(F)\to Y(G)\).

A morphism \(u\colon A\to B\) of augmented simplicial objects is *cartesian* if for every increasing \(\psi\colon E\to E'\) in \(\bar\Delta\) the square
\[
\begin{array}{ccc}
A(E')&\xrightarrow{A(\psi)}&A(E)\\
\downarrow{\scriptstyle u_{E'}}&&\downarrow{\scriptstyle u_E}\\
B(E')&\xrightarrow{B(\psi)}&B(E)
\end{array}
\]
is a fibre product. The same definition applies to morphisms of simplicial objects, with \(\Delta\) in place of \(\bar\Delta\). A simplicial object \(Y\) of \(T\) is *2-coskeletal* if, for every \(S\), the canonical map from the simplicial set \(\operatorname{Hom}(S,Y)\) to the coskeleton of its 2-truncation is an isomorphism ([*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), (1.9)–(1.10)).

**Proposition 2.4 (nerves).** For a simplicial object \(Y\) of \(T\), the following conditions are equivalent.

1. \(Y\) is isomorphic to the nerve of an internal category of \(T\).
2. For all \(a,b\geq0\) and \(0\leq k\leq\min(a,b)\), the restriction map \(Y_{a+b-k}\to Y_a\times_{Y_k}Y_b\) to the initial segment \(\{0,\ldots,a\}\) and to the final segment \(\{a-k,\ldots,a+b-k\}\) is an isomorphism. These two segments overlap in the \(k+1\) vertices \(\{a-k,\ldots,a\}\), and the fibre product is taken over the restrictions to this common segment.
3. The Segal maps (2.2) are isomorphisms for all \(n\geq2\).
4. For all \(n\geq2\), the map \(Y_n\to Y_{n-1}\times_{Y_0}Y_1\) given by \(d_n\) and the last edge is an isomorphism.
5. The Segal maps in degrees \(2\) and \(3\) are isomorphisms, and \(Y\) is 2-coskeletal.
6. The morphism \(d_0\colon\operatorname{Dec}_2(Y)\to\operatorname{Dec}_1(Y)\) of augmented simplicial objects, which removes the least vertex, is cartesian.
7. For all \(n\geq1\) and \(0\leq i<n\), the morphism \(d_i\colon\operatorname{Dec}_{n+1}(Y)\to\operatorname{Dec}_n(Y)\), induced by the face map of the added part \([n]\) that omits \(i\), is cartesian.
8. The morphism \(\operatorname{Dec}^2(Y)\to\operatorname{Dec}^1(Y)\) which removes the greatest vertex is cartesian.
9. For all \(n\geq1\) and \(0<i\leq n\), the morphism \(\operatorname{Dec}^{n+1}(Y)\to\operatorname{Dec}^n(Y)\), induced by the face map of the added part \([n]\) that omits \(i\), is cartesian.

Moreover, the nerve functor \(\operatorname{Cat}(T)\to\operatorname{Simpl}(T)\) is fully faithful.

**Proof.** *Reduction to sets.* Conditions (2)–(4) and (6)–(9) say that certain morphisms built from fibre products are isomorphisms. Since \(\operatorname{Hom}(S,-)\) preserves fibre products, and a morphism of \(T\) is an isomorphism if and only if \(\operatorname{Hom}(S,-)\) of it is bijective for every \(S\), each condition holds for \(Y\) exactly when it holds for every simplicial set \(\operatorname{Hom}(S,Y)\). Condition (5) is defined in this way. Suppose that every \(\operatorname{Hom}(S,Y)\) is the nerve of a category \(C(S)\), naturally in \(S\). The composition \(Y_1\times_{Y_0}Y_1\cong Y_2\xrightarrow{d_1}Y_1\) and the identities \(s_0\) then make \((Y_0,Y_1)\) an internal category whose category of \(S\)-points is \(C(S)\). Its axioms hold because they hold on points, and \(Y\) is its nerve. In the same way, functors \(X\to X'\) of internal categories are the families of functors \(X(S)\to X'(S)\) natural in \(S\). So it suffices to treat \(T=\mathrm{Sets}\).

*(1)\(\Leftrightarrow\)(3) and full faithfulness.* This is Proposition 2.1 of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes).

*(3)\(\Leftrightarrow\)(4).* The string of \(n\) edges of a simplex is the string of \(n-1\) edges of its face \(d_n\), followed by its last edge. Induction on \(n\) gives the equivalence.

*(1)\(\Rightarrow\)(2)\(\Rightarrow\)(4).* For a nerve, the Segal maps identify \(Y_{a+b-k}\) with strings of \(a+b-k\) arrows, and \(Y_a\times_{Y_k}Y_b\) with pairs of strings of \(a\) and of \(b\) arrows such that the last \(k\) arrows of the first are the first \(k\) arrows of the second (for \(k=0\), such that the last object of the first is the first object of the second). These sets correspond. Condition (4) is the case \(a=n-1\), \(b=1\), \(k=0\) of (2).

*(3)\(\Rightarrow\)(5).* Let \(n\geq3\), and let \(z\) be an \(n\)-simplex of the coskeleton of the 2-truncation, that is, a compatible assignment of a simplex \(z(\alpha)\in Y_j\) to each increasing \(\alpha\colon[j]\to[n]\) with \(j\leq2\). Use the composition of the category of (1). For \(a<b\) in \([n]\), the edge \(z(a,b)\) is the composite of \(z(a,a+1),\ldots,z(b-1,b)\): for \(b>a+1\), the 2-simplex \(z(a,b-1,b)\) has edges \(z(a,b-1)\), \(z(b-1,b)\) and \(z(a,b)\), so \(z(a,b)=z(b-1,b)\,z(a,b-1)\), and we induct on \(b-a\). Let \(x\in Y_n\) be the simplex with edges \(z(i-1,i)\), \(1\le i\le n\). The edges of \(x\) are the same composites, so \(x\) and \(z\) have the same edges. Their 2-simplices then agree, by the Segal bijection in degree 2. Their values at non-injective \(\alpha\) agree by compatibility with degeneracies. So \(z\) is the image of \(x\), and \(x\) is unique because a simplex of a nerve is determined by its edges \((i-1,i)\).

*(5)\(\Rightarrow\)(3).* The proof of Proposition 2.1 of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes) constructs a category \(C\) from the Segal bijections in degrees 2 and 3 alone. Its objects are \(Y_0\), its arrows \(Y_1\), its composition is \(d_1\) on \(Y_2\cong Y_1\times_{Y_0}Y_1\), and its identities are given by \(s_0\). The 2-truncations of \(Y\) and of \(N(C)\) are then isomorphic. Indeed, the faces \(d_0,d_2\) of \(Y_2\) are the two projections, \(d_1\) is the composition, and the identities \(d_2s_0=s_0d_1\), \(d_0s_0=1\), \(d_2s_1=1\), \(d_0s_1=s_0d_0\) show that \(s_0,s_1\colon Y_1\to Y_2\) insert identities. Both \(Y\) and \(N(C)\) are 2-coskeletal, the second by (3)\(\Rightarrow\)(5). So \(Y\) and \(N(C)\) are both the coskeleton of the same 2-truncated simplicial set, and \(Y\cong N(C)\).

*(3)\(\Rightarrow\)(7).* Assume (3), so that (2) holds. For \(E\in\bar\Delta\), write \(D(E)=Y(\{n\}\sqcup E)\) for the value of \(\operatorname{Dec}_1(Y)\) at \(E\), where \(\{n\}\) is the last element of the added part \([n]\). Condition (2), with \(k=0\), gives an isomorphism
\[
\begin{aligned}\operatorname{Dec}_{n+1}(Y)(E)&=Y([n]\sqcup E)\\&\xrightarrow{\ \sim\ }Y_n\times_{Y_0}D(E)\end{aligned}
\]
by restriction, natural in \(E\). For \(E=\varnothing\) it is the identity of \(Y_n=Y_n\times_{Y_0}Y_0\). The fibre product is over the last vertex of \(Y_n\) and the first vertex of \(D(E)\). The same holds for \(\operatorname{Dec}_n(Y)\) with \(Y_{n-1}\). For \(i<n\), the face of the added part that omits \(i\) keeps the vertex \(n\). So under these isomorphisms, \(d_i\) becomes \(d_i\times1\colon Y_n\times_{Y_0}D(E)\to Y_{n-1}\times_{Y_0}D(E)\), and \(Y(\psi)\) becomes \(1\times D(\psi)\). Now let \((y',z')\in Y_{n-1}\times_{Y_0}D(E')\) and \((y,z)\in Y_n\times_{Y_0}D(E)\) satisfy \(y'=d_iy\) and \(z=D(\psi)z'\). The last vertex of \(y\) is that of \(y'\), which is the first vertex of \(z'\). So \((y,z')\) is an element of \(Y_n\times_{Y_0}D(E')\), and it is the only one with the two given images. Hence the square is cartesian.

*(7)\(\Rightarrow\)(6)\(\Rightarrow\)(3).* Condition (6) is the case \(n=1\), \(i=0\) of (7). In (6), take \(\psi\colon\varnothing\to[m]\). The square says that \(Y_{m+2}\to Y_1\times_{Y_0}Y_{m+1}\), given by the first edge and \(d_0\), is an isomorphism. For \(m=0\) this is the Segal map in degree 2, and induction on \(m\) gives (3).

*(6),(7)\(\Leftrightarrow\)(8),(9).* We have \(\operatorname{Dec}^n(Y)=(\operatorname{Dec}_n(Y^{\mathrm{op}}))^{\mathrm{op}}\), and reversal of the order carries the maps of (6) and (7) for \(Y^{\mathrm{op}}\) to those of (8) and (9) for \(Y\). The Segal maps of \(Y^{\mathrm{op}}\) are those of \(Y\) with the factors in reverse order, so \(Y^{\mathrm{op}}\) satisfies (3) exactly when \(Y\) does. \(\square\)

**Remark 2.5 (two limits of the criterion).** (a) Condition (2) concerns gluing along a common segment, and it does not extend to all pushouts in \(\Delta\). Collapse \([1]\) to \([0]\), and map \([1]\) to the edge \(\{0,2\}\) of \([2]\). Together with the maps \([0]\to[0]\) and \([2]\to[0]\), this square is a pushout in \(\Delta\), because an increasing map \([2]\to T\) taking the same value at \(0\) and \(2\) is constant. Let \(C\) be the groupoid with two objects and exactly one arrow between any two objects. The map \(N_0(C)\to N_0(C)\times_{N_1(C)}N_2(C)\) has \(2\) elements in its source and \(4\) in its target: the target consists of the pairs \((c,(x,y))\) with \(yx=1_c\), and \(x\colon c\to c'\) may end at either object.

(b) In condition (5), the Segal map in degree 3 cannot be omitted. Let \(M\) be a set with a binary operation that has a two-sided unit \(e\) but is not associative. For example, take \(M=\{e,a,b\}\) with unit \(e\) and \(aa=b\), \(ab=ba=b\), \(bb=a\), so that \((aa)b=a\) and \(a(ab)=b\). Put \(Y_0=\{\ast\}\), \(Y_1=M\) and \(Y_2=M\times M\), with \(d_0(x,y)=y\), \(d_1(x,y)=xy\), \(d_2(x,y)=x\), \(s_0(\ast)=e\), \(s_0(x)=(e,x)\) and \(s_1(x)=(x,e)\). The simplicial identities in these degrees hold, those involving degeneracies by the unit laws. Let \(Y\) be the coskeleton of this 2-truncated simplicial set. Then \(Y\) is 2-coskeletal, and its Segal map in degree 2 is bijective. A 3-simplex of \(Y\) is a compatible family of four 2-simplices. If its edges \((0,1),(1,2),(2,3)\) are \(x,y,z\), its faces force the edge \((0,3)\) to be both \((xy)z\) and \(x(yz)\). So \(Y_3\) is the set of associative triples, and the Segal map in degree 3 is not surjective. Hence \(Y\) is not a nerve.

### 2.4. Groupoids

An internal category \(X\) is an *internal groupoid* if there is a morphism \(t\colon X_1\to X_1\) with \(d_0t=d_1\), \(d_1t=d_0\), \(t(x)x=1_{d_1x}\) and \(x\,t(x)=1_{d_0x}\) on points. Such a \(t\) is unique, and it is a functor \(X\to X^{\mathrm{o}}\) to the opposite internal category which is the identity on objects.

**Proposition 2.6 (groupoids).** Let \(X\) be an internal category of \(T\) with nerve \(Y\). The following conditions are equivalent.

1. \(X\) is an internal groupoid.
2. On points with values in every object \(S\), for every pair \((x,z)\) of arrows with a common source there is an arrow \(y\) with \(z=yx\).
3. On points with values in every object \(S\), for every pair \((y,z)\) of arrows with a common target there is an arrow \(x\) with \(z=yx\).
4. The morphism \((d_1,d_2)\colon Y_2\to Y_1\times_{d_1,Y_0,d_1}Y_1\) to pairs of arrows with a common source is an isomorphism.
5. The morphism \((d_0,d_1)\colon Y_2\to Y_1\times_{d_0,Y_0,d_0}Y_1\) to pairs of arrows with a common target is an isomorphism.
6. For every increasing \(\varphi\colon[m]\to[n]\), the morphism \(\operatorname{Dec}_{n+1}(Y)\to\operatorname{Dec}_{m+1}(Y)\) induced by \(\varphi\sqcup\mathrm{id}\) is cartesian.
7. For every increasing \(\varphi\colon[m]\to[n]\), the morphism \(\operatorname{Dec}^{n+1}(Y)\to\operatorname{Dec}^{m+1}(Y)\) induced by \(\mathrm{id}\sqcup\varphi\) is cartesian.

For \(T=\mathrm{Sets}\), they are also equivalent to: \(Y\) is a Kan complex.

**Proof.** As in Proposition 2.4, every condition can be checked on \(S\)-points. For (1), inverses on points are unique, hence natural in \(S\), hence given by a morphism \(t\). So let \(T=\mathrm{Sets}\).

(1)\(\Rightarrow\)(2),(3): take \(y=zx^{-1}\), respectively \(x=y^{-1}z\). (2)\(\Rightarrow\)(1): applying (2) to \((x,1_{d_1x})\) gives \(y\) with \(yx=1\), and applying it to \((y,1_{d_1y})\) gives \(w\) with \(wy=1\). Then \(w=w(yx)=(wy)x=x\), so \(y\) is a two-sided inverse of \(x\). (3)\(\Rightarrow\)(1) is the same argument with right inverses: \(yx=1\) and \(xw=1\) give \(y=y(xw)=(yx)w=w\).

(4) and (5): a 2-simplex with edges \(x\) and \(y\), \(y\) after \(x\), has \(d_2=x\), \(d_1=yx\) and \(d_0=y\). So \((d_1,d_2)\) is surjective exactly when (2) holds, and (4) implies (2). Conversely (1) implies (4): (2) holds, and \(y=(yx)x^{-1}\) is determined by \(yx\) and \(x\). In the same way \((d_0,d_1)\) is surjective exactly when (3) holds, so (5) implies (3), and (1) implies (5) because \(x=y^{-1}(yx)\).

(1)\(\Rightarrow\)(6): let \(F\) be a finite nonempty totally ordered set and \(f\in F\). A simplex \(x\colon F\to X\) is determined by the object \(c=x(f)\) and the arrows \(a_g\colon c\to x(g)\), \(g\in F\), where \(a_g=x(f\le g)\) for \(g\geq f\) and \(a_g=x(g\le f)^{-1}\) for \(g<f\). Conversely, every object \(c\) and every map \(a\) from \(F\) to the set \(A_c\) of arrows with source \(c\), with \(a_f=1_c\), comes from the simplex \(g\le h\mapsto a_ha_g^{-1}\). So \(Y(F)\) is the disjoint union over \(c\) of the sets of pointed maps \((F,f)\to(A_c,1_c)\). Restriction along an increasing \(\theta\colon F'\to F\) with \(\theta(f')=f\) is composition with \(\theta\). In the square of (6) for \(\psi\colon E\to E'\), take the base points \(\varphi(0)\) in \([n]\sqcup E\) and \([n]\sqcup E'\), and \(0\) in \([m]\sqcup E\) and \([m]\sqcup E'\). All four maps preserve base points. The square of sets formed by \([m]\sqcup E\to[m]\sqcup E'\), \([n]\sqcup E\to[n]\sqcup E'\) and the two maps \(\varphi\sqcup\mathrm{id}\) is a pushout: it is the disjoint union of the pushout of \([n]\leftarrow[m]\to[m]\), which is \([n]\), and of \(E\leftarrow E\to E'\), which is \(E'\). Pointed maps out of a pushout form a fibre product, so the square of (6) is cartesian over each object \(c\).

(6)\(\Rightarrow\)(4): take \(m=0\), \(n=1\), \(\varphi(0)=0\) and \(\psi\colon\varnothing\to[0]\). The square becomes \(Y_2\to Y_1\times_{d_1,Y_0,d_1}Y_1\) by the edges \((0,2)\) and \((0,1)\), and it is cartesian. (1)\(\Leftrightarrow\)(7): apply (1)\(\Leftrightarrow\)(6) to \(X^{\mathrm{o}}\), using \(N(X^{\mathrm{o}})=N(X)^{\mathrm{op}}\) and \(\operatorname{Dec}^{n+1}(Y)=(\operatorname{Dec}_{n+1}(Y^{\mathrm{op}}))^{\mathrm{op}}\). \(X\) is a groupoid exactly when \(X^{\mathrm{o}}\) is. The Kan condition is Proposition 3.1 of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes). \(\square\)

**Corollary 2.7.** If \(X\) is a groupoid, then \(\pi_i(N(X),x)=0\) for every vertex \(x\) and every \(i\geq2\).

**Proof.** This is Proposition 5.3 of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes). \(\square\)

### 2.5. Actions of monoids

Let \(T\) have fibre products and a final object \(e\), so that \(T\) has finite limits. Let \(G\) be a monoid of \(T\), associative with unit \(1\), and let \(X\) be a left \(G\)-object, with action \(a\colon G\times X\to X\), written \(gx\) on points. The internal category \([G,X]\) has objects \(X\) and arrows \(G\times X\). The arrow \((g,x)\) has source \(x\) and target \(gx\), the identity of \(x\) is \((1,x)\), and the composite of \((g,x)\) and \((h,gx)\) is \((hg,x)\). Its nerve is denoted \(N(G,X)\). A string of \(n\) arrows is determined by \((g_1,\ldots,g_n,x)\), where \(x\) is its first object, so that
\[
N_n(G,X)=G^n\times X.
\]
For \(n\geq1\) and \(u=(g_1,\ldots,g_n,x)\),
\[
\begin{aligned}
d_0u&=(g_2,\ldots,g_n,g_1x),\\
d_iu&=(g_1,\ldots,g_{i-1},g_{i+1}g_i,\\&\qquad g_{i+2},\ldots,g_n,x)\quad(0<i<n),\\
d_nu&=(g_1,\ldots,g_{n-1},x),
\end{aligned}
\]
and \(s_iu\) inserts \(1\) between \(g_i\) and \(g_{i+1}\) (in front for \(i=0\)), with \(s_0x=(1,x)\). For \(X=e\) this is the nerve \(N(G)\) of the one-object category \([G]\). The projection \(X\to e\) induces \(p\colon N(G,X)\to N(G)\), the projection onto \(G^n\) in degree \(n\). A right action of \(G\) is a left action of the opposite monoid \(G^{\mathrm{o}}\), so right actions need no separate treatment.

**Proposition 2.8.** (a) The morphism \(\operatorname{Dec}_1(p)\colon\operatorname{Dec}_1N(G,X)\to\operatorname{Dec}_1N(G)\) of augmented simplicial objects is cartesian. (b) The morphism \(p\) is cartesian if and only if \((\mathrm{pr}_1,a)\colon G\times X\to G\times X\) is an isomorphism. For \(T=\mathrm{Sets}\), this means that every element of \(G\) acts bijectively.

**Proof.** (a) The value of \(\operatorname{Dec}_1N(G,X)\) at a set \(E\) with \(k+1\) elements is \(N_{k+1}(G,X)=G^{k+1}\times X\), where the factor \(X\) records the object at the added least vertex. For \(E=\varnothing\) it is \(X\). Every map \(\mathrm{id}\sqcup\psi\) preserves the added least vertex. So
\[
\begin{aligned}&\operatorname{Dec}_1N(G,X)(\psi)\\&\quad=\operatorname{Dec}_1N(G)(\psi)\times\mathrm{id}_X,\end{aligned}
\]
and \(\operatorname{Dec}_1(p)\) is the projection that forgets \(X\). A square of this form is cartesian.

(b) For \(\varphi\colon[m]\to[n]\), the object at the vertex \(\varphi(0)\) of the string \((g_1,\ldots,g_n,x)\) is \(g_{\varphi(0)}\cdots g_1x\). So
\[
\begin{aligned}&N(G,X)(\varphi)(g,x)\\&\quad=\bigl(N(G)(\varphi)(g),\,g_{\varphi(0)}\cdots g_1x\bigr),\end{aligned}
\]
and the square of \(p\) at \(\varphi\) is cartesian exactly when \((g,x)\mapsto(g,g_{\varphi(0)}\cdots g_1x)\) is an automorphism of \(G^n\times X\). For \(\varphi\colon[0]\to[1]\) with \(\varphi(0)=1\), this map is \((\mathrm{pr}_1,a)\). Conversely, if \((\mathrm{pr}_1,a)\) is an isomorphism, so is its base change \((g,x)\mapsto(g,g_jx)\) along the projection \(G^n\to G\) onto the \(j\)-th factor, for every \(j\). The map \((g,x)\mapsto(g,g_k\cdots g_1x)\) is a composite of these. \(\square\)

**Proposition 2.9.** For fixed \(G\), the functor \(X\mapsto N(G,X)\), from left \(G\)-objects of \(T\) to simplicial objects of \(T\) over \(N(G)\), is fully faithful. Its essential image consists of the \(q\colon Y\to N(G)\) such that, for every \(n\), the morphism
\[
(q_n,\;d_1\cdots d_n)\colon Y_n\to N_n(G)\times Y_0
\]
is an isomorphism; here \(d_1\cdots d_n\) is the restriction to the vertex \(0\).

**Proof.** By the Yoneda lemma it suffices to treat \(T=\mathrm{Sets}\). A \(G\)-equivariant map \(f\colon X\to X'\) gives the functor \((g,x)\mapsto(g,f(x))\) over \([G]\). Conversely, a functor \([G,X]\to[G,X']\) over \([G]\) sends \((g,x)\) to an arrow \((g,f(x))\), and compatibility with targets says \(f(gx)=gf(x)\). By the full faithfulness in Proposition 2.4, functors over \([G]\) are the morphisms of nerves over \(N(G)\). This proves full faithfulness.

The objects \(N(G,X)\) satisfy the condition by the formula for \(N_n(G,X)\). Conversely, let \(q\colon Y\to N(G)\) satisfy it. Then \(Y_1\cong G\times Y_0\), with source the second coordinate. Write \(a(g,y)\in Y_0\) for the target. Under these identifications, a string of \(n\) composable edges of \(Y\) is a tuple \((g_1,\ldots,g_n,y)\), the later sources being forced. The Segal map of \(Y\) composed with this identification is \((q_n,d_1\cdots d_n)\), since \(q\) sends the edge \((i-1,i)\) of a simplex to the \(i\)-th entry of its image in \(N_n(G)=G^n\). By hypothesis it is bijective, so \(Y\) satisfies condition (3) of Proposition 2.4 and is the nerve of a category over \([G]\) with objects \(Y_0\) and arrows \(G\times Y_0\). Since \(q\) is a functor to \([G]\), the composite of \((g,y)\) and \((h,a(g,y))\) is \((hg,y)\), and the identity of \(y\) is \((1,y)\). Comparing targets gives \(a(hg,y)=a(h,a(g,y))\) and \(a(1,y)=y\). So \(a\) is an action, and the category is \([G,Y_0]\). \(\square\)

### 2.6. Two examples

**Example 2.10.** For a set \(X\), let \(\operatorname{Sc}(X)\) be the groupoid with objects \(X\) and exactly one arrow \((x,y)\) from \(x\) to \(y\) for all \(x,y\). Its nerve is \(\operatorname{cosk}_0(X)\), with \(N_n(\operatorname{Sc}(X))=X^{n+1}\), \(d_i\) omitting the \(i\)-th entry and \(s_i\) repeating it. If \(X\) is nonempty, it is contractible ([*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), (1.11)). Exercise 4.3 compares it with the nerve of a group action.

**Example 2.11 (two-term complexes).** Let \(A\) be an abelian category and \(L=(L_1\xrightarrow{d}L_0)\) a complex in homological degrees \(1\) and \(0\). The group object \(L_1\) acts on \(L_0\) by \(g\cdot x=x+dg\), and \([L_1,L_0]\) is an internal groupoid of \(A\). Its nerve \(Y=N(L_1,L_0)\), with \(Y_n=L_1^n\oplus L_0\), is a simplicial object of \(A\), because all its faces and degeneracies are additive. Its normalized complex [Stacks, Tag 0194] has \(N(Y)_n=\bigcap_{i=0}^{n-1}\ker d_i\) with differential \((-1)^nd_n\), and it is isomorphic to \(L\). Indeed, \(N(Y)_0=L_0\). Next, \(N(Y)_1=\ker d_0=\{(g,-dg)\}\cong L_1\), on which \(-d_1\) is \(g\mapsto dg\). For \(n\geq2\), an element \((g_1,\ldots,g_n,x)\) of \(\ker d_0\) has \(g_2=\cdots=g_n=0\) and \(x=-dg_1\). If it also lies in \(\ker d_1\), then \(g_1+g_2=0\), so it is zero. By the Dold–Kan theorem [Stacks, Tag 019G], \(Y\) is the simplicial object corresponding to \(L\). In particular, for an object \(E\) of \(A\), the nerve \(N(E)\) of the group object \(E\) corresponds to \(E[1]\), the object \(E\) placed in homological degree \(1\).

## 3. The homotopy type of a category

A morphism \(f\) of simplicial sets is a *weak equivalence* if its realization \(|f|\) is a weak homotopy equivalence. A functor \(u\) of small categories is a *weak equivalence* if \(N(u)\) is one; this class is denoted \(W_\infty\) in ([*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), Section 1.1). For a simplicial set \(K\), let \(\Delta/K\) be its category of simplices: objects are pairs \(([n],x)\) with \(x\in K_n\), and a morphism \(([m],y)\to([n],x)\) is an increasing \(\alpha\colon[m]\to[n]\) with \(K(\alpha)x=y\). For a small category \(C\), the functors
\[
\begin{gathered}\sup\colon\Delta/N(C)\to C,\\\inf\colon(\Delta/N(C))^{\mathrm{op}}\to C\end{gathered}
\]
send \(([n],x)\) to \(x(n)\) and to \(x(0)\), respectively. On morphisms they are given by the arrows \(x(\alpha(m)\le n)\) and \(x(0\le\alpha(0))\).

**Lemma 3.1.** For every simplicial set \(K\) there is a homeomorphism \(|K^{\mathrm{op}}|\cong|K|\), natural in \(K\). Hence a morphism \(f\) of simplicial sets is a weak equivalence if and only if \(f^{\mathrm{op}}\) is, and a functor \(u\) is a weak equivalence if and only if \(u^{\mathrm{op}}\) is.

**Proof.** Let \(r_n\colon\Delta^n\to\Delta^n\) reverse the barycentric coordinates, \((t_0,\ldots,t_n)\mapsto(t_n,\ldots,t_0)\). For increasing \(\alpha\colon[m]\to[n]\), let \(\alpha^\vee(j)=n-\alpha(m-j)\). Then \(r_n\circ\alpha_*=\alpha^\vee_*\circ r_m\) for the induced affine maps. The realization is the colimit of the geometric simplices over the simplices of \(K\). Applying \(r\) on each simplex identifies the colimit defining \(|K^{\mathrm{op}}|\) with the one defining \(|K|\), naturally in \(K\). The second assertion follows, using (2.1) for functors. \(\square\)

**Theorem 3.2 (Quillen).** (i) For every small category \(C\), the functors \(\sup\) and \(\inf\) are weak equivalences. (ii) For every simplicial set \(K\), the last-vertex map \(\lambda_K\colon N(\Delta/K)\to K\) is a weak equivalence, natural in \(K\).

**Proof.** (i) The functor \(\sup\) is the last-object evaluation \(e_C\), which is a weak equivalence by Lemma 3.1 of [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme). For \(\inf\), define an isomorphism of categories \(\Theta\colon\Delta/N(C)\to\Delta/N(C^{\mathrm{op}})\) by \(([n],x)\mapsto([n],x^\vee)\), where \(x^\vee(j)=x(n-j)\) is read in \(C^{\mathrm{op}}\), and by \(\alpha\mapsto\alpha^\vee\) on morphisms. Then \(\sup_{C^{\mathrm{op}}}\circ\Theta\) sends \(([n],x)\) to \(x(0)\), and a morphism \(\alpha\) to the arrow of \(C^{\mathrm{op}}\) opposite to \(x(0\le\alpha(0))\). So \(\inf^{\mathrm{op}}=\sup_{C^{\mathrm{op}}}\circ\Theta\) is a weak equivalence, and by Lemma 3.1 so is \(\inf\). (ii) This is the last-vertex comparison (5.6) of [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), Section 5.3. \(\square\)

**Corollary 3.3.** The functors \(N\) and \(K\mapsto\Delta/K\) induce mutually inverse equivalences between the category of small categories localized at weak equivalences and the category of simplicial sets localized at weak equivalences.

**Proof.** The nerve preserves weak equivalences by definition. For a morphism \(f\colon K\to L\), naturality gives \(\lambda_L\circ N(\Delta/f)=f\circ\lambda_K\), and \(\lambda_K,\lambda_L\) are weak equivalences by Theorem 3.2 (ii). By two-out-of-three, \(\Delta/f\) is a weak equivalence when \(f\) is. So both functors descend to the localizations. There, \(\sup\colon\Delta/N(C)\to C\) and \(\lambda_K\colon N(\Delta/K)\to K\) become natural isomorphisms, by Theorem 3.2. \(\square\)

**Corollary 3.4.** For every small category \(C\), the functors
\[
C\xleftarrow{\ \sup\ }\Delta/N(C)\xrightarrow{\ \inf^{\mathrm{op}}\ }C^{\mathrm{op}}
\]
are weak equivalences. They are natural in \(C\), so \(C\) and \(C^{\mathrm{op}}\) are canonically isomorphic in the localized category of Corollary 3.3.

**Proof.** Combine Theorem 3.2 (i) with Lemma 3.1. Naturality holds because a functor \(u\colon C\to D\) commutes with \(\sup\) and \(\inf\). \(\square\)

**Remark 3.5.** Bisimplicial sets enter the later lessons through the diagonal. A morphism of bisimplicial sets which is a weak equivalence on every row induces a weak equivalence of the diagonals. This is the realization lemma of [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), Section 1.1, together with the homeomorphism there between the double realization and the realization of the diagonal.

## 4. Exercises

**Exercise 4.1.** Let \(G\) be a monoid of a category \(T\) with finite limits, acting on itself by left multiplication.

(a) Show that \((g_0,g_1,\ldots,g_n)\mapsto(g_1,\ldots,g_n,g_0)\) is an isomorphism \(\operatorname{Dec}_1N(G)\cong N(G,G)\), under which the face \(d_0\colon\operatorname{Dec}_1N(G)\to N(G)\), removing the added least vertex, becomes the projection \(p\).

(b) Deduce that \(N(G,G)\) is homotopy equivalent to the constant simplicial object \(e\).

(c) Show that \(\operatorname{Dec}^1N(G)\cong N(G^{\mathrm{o}},G)^{\mathrm{op}}\), where \(G^{\mathrm{o}}\) acts on \(G\) by \(h\ast g=gh\), via \((g_1,\ldots,g_{n+1})\mapsto(g_n,\ldots,g_1,g_{n+1})\).

**Exercise 4.2.** Let \(C\) be a small category with a final object \(t\). Using Propositions 1.1 and 2.3 instead of Proposition 2.1, show that \(N(C)\) is homotopy equivalent to a point.

**Exercise 4.3.** Let \(G\) be a group acting on a set \(X\). Show that \([G,X]\) is a groupoid, and that the functor \([G,X]\to\operatorname{Sc}(X)\), \((g,x)\mapsto(x,gx)\), induces a morphism \(N(G,X)\to N(\operatorname{Sc}(X))\) which is injective in every degree exactly when the action is free, and surjective in every degree exactly when for all \(x,y\in X\) there is \(g\) with \(gx=y\). Conclude that it is an isomorphism exactly when \(G\times X\to X\times X\), \((g,x)\mapsto(gx,x)\), is bijective.

## 5. Complete solutions

**4.1.** (a) An \(n\)-simplex of \(\operatorname{Dec}_1N(G)\) is a string \((g_0,g_1,\ldots,g_n)\) in \(N_{n+1}(G)\), and its faces are the \(d_1,\ldots,d_{n+1}\) of \(N(G)\). The face \(d_1\) of \(N(G)\) gives \((g_1g_0,g_2,\ldots,g_n)\), whose image \((g_2,\ldots,g_n,g_1g_0)\) is \(d_0\) of \((g_1,\ldots,g_n,g_0)\) in \(N(G,G)\). For \(0<i<n\), the face \(d_{i+1}\) of \(N(G)\) replaces \(g_i,g_{i+1}\) by \(g_{i+1}g_i\), which is \(d_i\) of \(N(G,G)\). The face \(d_{n+1}\) drops \(g_n\), which is \(d_n\). The degeneracies \(s_{i+1}\) of \(N(G)\) insert \(1\) after \(g_i\), as the \(s_i\) of \(N(G,G)\) do. Finally, \(d_0\) of \(N(G)\) drops \(g_0\), and this is the projection to \((g_1,\ldots,g_n)\). (b) By Proposition 1.1, \(\operatorname{Dec}_1N(G)\) is homotopy equivalent, over its augmentation, to the constant simplicial object \(N_0(G)=e\). (c) Reversing strings is an isomorphism \(N(G)^{\mathrm{op}}\cong N(G^{\mathrm{o}})\). Since \(\operatorname{Dec}^1(Z)=(\operatorname{Dec}_1(Z^{\mathrm{op}}))^{\mathrm{op}}\), part (a) for \(G^{\mathrm{o}}\) gives \(\operatorname{Dec}^1N(G)\cong N(G^{\mathrm{o}},G^{\mathrm{o}})^{\mathrm{op}}\). Left multiplication by \(h\) in \(G^{\mathrm{o}}\) is \(g\mapsto gh\). Following a string through the two isomorphisms gives the formula stated.

**4.2.** By Proposition 2.3, \(\operatorname{Dec}^1N(C)\) is the disjoint union of the \(N(C/c)\) over \(\operatorname{Ob}(C)\), and its augmentation sends the component of \(c\) to \(c\). The homotopy of Proposition 1.1 is compatible with the augmentation, so it restricts to the component of \(t\). There it shows that \(N(C/t)\) is homotopy equivalent to the point \(t\). Since \(t\) is final, every object has exactly one arrow to \(t\), and the source functor \(C/t\to C\) is an isomorphism of categories. Hence \(N(C)\cong N(C/t)\).

**4.3.** The arrow \((g,x)\) has inverse \((g^{-1},gx)\). In degree \(n\), the morphism is
\[
\begin{gathered}G^n\times X\to X^{n+1},\\(g_1,\ldots,g_n,x)\mapsto\\(x,\,g_1x,\,g_2g_1x,\ldots,g_n\cdots g_1x).\end{gathered}
\]
Both sides are nerves, so by Proposition 2.4 this map is the \(n\)-fold fibre product over \(X\) of the map in degree \(1\), \((g,x)\mapsto(x,gx)\). Hence it is injective, surjective or bijective in every degree exactly when the degree-\(1\) map is. The degree-\(1\) map is injective exactly when \(gx=hx\) implies \(g=h\), which is freeness. It is surjective exactly when every pair \((x,y)\) has the form \((x,gx)\). It is bijective exactly when both hold, that is, when \((g,x)\mapsto(gx,x)\) is bijective.

## Sources

The décalage functors and their use for the cohomology and deformations of diagrams are due to Illusie, in his work on the cotangent complex. The classifying space of a category, and the fact that a natural transformation between two functors induces homotopic maps of classifying spaces, are in G. Segal, *Classifying spaces and spectral sequences*, Publ. Math. IHÉS 34 (1968), 105–112, [Numdam](http://www.numdam.org/item/PMIHES_1968__34__105_0/). Theorem A and the comparison of the homotopy theories of categories and simplicial sets are due to Quillen; their proofs are in the programme lessons cited in Section 3. A modern treatment of décalage and its relation to Kan's loop group functor is D. Stevenson, *Décalage and Kan's simplicial loop group functor*, [arXiv:1112.0474](https://arxiv.org/abs/1112.0474).
