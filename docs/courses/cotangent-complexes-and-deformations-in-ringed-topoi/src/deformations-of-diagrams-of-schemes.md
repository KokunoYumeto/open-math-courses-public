# Deformations of diagrams of schemes

*Written by Claude Opus 5.5 (Anthropic) on 21 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagram of schemes is a family of schemes indexed by a small category, with a morphism for every arrow. Commutative squares of schemes and simplicial schemes, such as the nerve of a group scheme acting on a scheme, are diagrams of this kind, and their first-order deformations are deformations of diagrams. A diagram has one ringed topos, the total topos of the Zariski topoi of its schemes, and a morphism of diagrams has a cotangent complex on it, made by the sheaf construction of the cotangent complex. This lesson shows that this complex governs the deformations of diagrams as the cotangent complex of a morphism of schemes governs those of schemes. Square-zero extensions of a diagram are classified by the first Ext group of the cotangent complex. Lifting a morphism of diagrams over a square-zero thickening of its target is obstructed by a class in the second Ext group, and this class is the product of the Kodaira–Spencer class with the class of the thickening. The point that makes the ringed-topos theorems apply is that the levels of an extension of ringed topoi by a termwise quasi-coherent ideal are schemes.

A deformation of a diagram is an extension whose ideal is cartesian. For a morphism of schemes this means that the square formed with the two thickenings is cartesian and that a Tor group vanishes. Deformations carry cartesian squares to cartesian squares (Corollary 3.7, Proposition 4.4), so the fibre products that express group laws and actions survive deformation.

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Definition 2.1, Proposition 2.2, Theorem 4.2); [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md) (Definition 1.1, Propositions 1.2, 2.1 and 4.2); [*Quasi-coherent and perfect complexes on big fppf sites*](quasi-coherent-and-perfect-complexes-on-big-fppf-sites.md) (Construction 4.1, Lemma 4.2). From the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex#10-morphisms-of-schemes): its functoriality (Theorem 2.2), Tor-independent base change (Proposition 3.1), the transitivity triangle (Theorem 4.1), localization and étale maps (Proposition 5.1), Koszul-regular quotients (Lemma 7.1), the sheaf construction on a site with Proposition 10.1, and the classification of extensions and the obstruction theorem for ringed topoi, [Theorems 10.3 and 10.4](course:AG-HP/the-cotangent-complex#extensions-of-sheaves-of-algebras). From the AI-integrated Stacks project: thickenings [[Stacks, Tag 04EX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-thickening)]; closed immersions and their ideals [[Tag 01IN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-closed-subspace-scheme), [Tag 01QY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-i-star-equivalence), [Tag 01JU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-immersion)]; fibre products and pullbacks of affine schemes [[Tag 01I4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-affine-schemes), [Tag 01JR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-open-fibre-product), [Tag 01JS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-affine-covering-fibre-product), [Tag 01I9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-widetilde-pullback), [Tag 01IC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-kernel-cokernel-quasi-coherent)]; stalks of pullbacks [[Tag 008H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-stalk-pullback), [Tag 01CB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-stalk-tensor-product)]; flat pullback and faithful flatness [[Tag 02N4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-pullback-flat), [Tag 00HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-local-flat-ff)]; étale morphisms [[Tag 02GI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-etale)]; Tor independence [[Tag 0660](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-tor-independent), [Tag 08IA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-definition-tor-independent)]; flat resolutions, K-flat complexes and derived pullback [[Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution), [Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat), [Tag 06YY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-base-change)]; maps out of truncated objects and the long exact sequence of a triangle [[Tag 06XS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-negative-exts), [Tag 0149](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-representable-homological)].

## Conventions

All rings are commutative. A *diagram of schemes* is a functor \(X\colon I\to(\mathrm{Sch})\) from a small category \(I\), with the schemes \(X_i\) and the morphisms \(X_\alpha\colon X_i\to X_j\) for the arrows \(\alpha\colon i\to j\). Let \(Y\colon J\to(\mathrm{Sch})\) be another diagram and \(u\colon I\to J\) a functor. A *morphism of diagrams* \(f\colon X\to Y\) *of type \(u\)* is a family of morphisms of schemes \(f_i\colon X_i\to Y_{u(i)}\) with
\[
f_j\circ X_\alpha=Y_{u(\alpha)}\circ f_i\qquad(\alpha\colon i\to j).
\]
If \(I=J\) and \(u\) is the identity, \(f\) is an *\(I\)-morphism*. Morphisms compose: for \(g\colon Y\to Z\) of type \(v\), \(gf\) has type \(vu\) and components \(g_{u(i)}\circ f_i\). The *final diagram* is \(\operatorname{Spec}\mathbb Z\), indexed by the category with one object and one arrow; every diagram has a unique morphism to it. A morphism of schemes \(h\colon X\to Z\) is a diagram indexed by \(\{0\to1\}\); a commutative triangle or square of schemes is a diagram indexed by \(\{0\to1\to2\}\) or by \(\{0\to1\}\times\{0\to1\}\).

The *Zariski topos* \(\operatorname{Top}(X_{\mathrm{Zar}})\) of \(X\), ringed by \(\mathcal O_X\), is the total topos of the topoi \((X_i)_{\mathrm{Zar}}\) (Construction 4.1 of [*Quasi-coherent and perfect complexes on big fppf sites*](quasi-coherent-and-perfect-complexes-on-big-fppf-sites.md)). An object \(E\) is a family of sheaves \(E_i\) on \(X_i\) with maps \(E_\alpha\colon X_\alpha^{-1}E_j\to E_i\) compatible with composites, colimits and finite limits are computed levelwise, and \(\operatorname{Top}(X_{\mathrm{Zar}})\) is the topos of sheaves on a small site (Definition 2.1, Proposition 2.2 and Theorem 4.2 of [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md)). So the sheaf constructions of Section 10 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#10-morphisms-of-schemes) apply in it. An \(\mathcal O_X\)-module \(M\) is a family of \(\mathcal O_{X_i}\)-modules \(M_i\) with \(\mathcal O_{X_i}\)-linear maps \(M_\alpha\colon X_\alpha^*M_j\to M_i\) compatible with composites (Proposition 4.2 (a) of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md)); it is *termwise quasi-coherent* if every \(M_i\) is quasi-coherent and *cartesian* if every \(M_\alpha\) is an isomorphism. The restriction \(i^*\colon E\mapsto E_i\) is the inverse image of a morphism of topoi \((X_i)_{\mathrm{Zar}}\to\operatorname{Top}(X_{\mathrm{Zar}})\) (Theorem 4.2 there), with \(i^*\mathcal O_X=\mathcal O_{X_i}\); it is exact and commutes with tensor products (Proposition 4.2 (c) of the lesson on morphisms of fibred topoi). A module is zero if and only if all its levels are, so a complex of modules is acyclic if and only if all its levels are. An object \(E\) of \(D^-(X_{\mathrm{Zar}})\) is *quasi-cartesian* if every map \(LX_\alpha^*E_j\to E_i\) is an isomorphism.

A morphism \(f\colon X\to Y\) of type \(u\) gives a morphism of fibred topoi in the sense of Definition 1.1 of the lesson on morphisms of fibred topoi: the functor \(u\), the morphisms of Zariski topoi defined by the \(f_i\), and the isomorphisms \(X_\alpha^{-1}f_j^{-1}\cong f_i^{-1}Y_{u(\alpha)}^{-1}\) given by \(f_jX_\alpha=Y_{u(\alpha)}f_i\). By Propositions 1.2 and 2.1 there it gives a morphism of topoi \(f\colon\operatorname{Top}(X_{\mathrm{Zar}})\to\operatorname{Top}(Y_{\mathrm{Zar}})\) with \((f^{-1}G)_i=f_i^{-1}G_{u(i)}\). The ring maps \(f_i^\sharp\colon f_i^{-1}\mathcal O_{Y_{u(i)}}\to\mathcal O_{X_i}\) are compatible with the structure maps, again because \(f_jX_\alpha=Y_{u(\alpha)}f_i\), so they form a ring map \(f^\sharp\colon f^{-1}\mathcal O_Y\to\mathcal O_X\), and \(f\) is a morphism of ringed topoi. Its module pullback \(f^*G=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}G\) has the levels \(f_i^*G_{u(i)}\), and \(Lf^*\) denotes its derived functor [Stacks, Tag 06YY]. For \(g\colon Y\to Z\) as above, \((gf)^{-1}=f^{-1}g^{-1}\).

**Cotangent complexes of scheme morphisms.** For a morphism of schemes \(f\colon X\to Y\), \(L_{X/Y}\) is the cotangent complex of \(f^{-1}\mathcal O_Y\to\mathcal O_X\) on the Zariski site of \(X\) (Section 10 of *The cotangent complex*). Inverse images under morphisms of topoi are exact and preserve the polynomial constructions (Section 10 there). For a commutative square of schemes with \(f\circ a=b\circ f_1\), where \(a\colon X_1\to X\), \(b\colon Y_1\to Y\) and \(f_1\colon X_1\to Y_1\), the ring maps \(a^{-1}f^{-1}\mathcal O_Y=f_1^{-1}b^{-1}\mathcal O_Y\to f_1^{-1}\mathcal O_{Y_1}\) and \(a^{-1}\mathcal O_X\to\mathcal O_{X_1}\) form a map of ring pairs on \(X_1\). The functoriality of the construction (Theorem 2.2 there, applied on the site) gives an \(a^{-1}\mathcal O_X\)-linear map \(a^{-1}L_{X/Y}=L_{a^{-1}\mathcal O_X/a^{-1}f^{-1}\mathcal O_Y}\to L_{X_1/Y_1}\); its \(\mathcal O_{X_1}\)-linear extension
\[
La^*L_{X/Y}=a^*L_{X/Y}\longrightarrow L_{X_1/Y_1}
\]
is the *functoriality map* of the square. Here \(a^*L_{X/Y}\) computes \(La^*L_{X/Y}\) because \(L_{X/Y}\) is a bounded above complex of flat modules (Section 10 there: normalized differential modules are retracts of flat modules), hence K-flat [Tags 06YQ, 06YY].

**Thickenings and conormal truncations.** A first-order thickening is a closed immersion \(\iota\colon X\to X'\) whose quasi-coherent ideal \(\mathcal I\subseteq\mathcal O_{X'}\) has square zero [Tag 04EX]. On an affine open \(\operatorname{Spec}A'\) of \(X'\), \(\iota\) is \(\operatorname{Spec}(A'/I)\to\operatorname{Spec}A'\) for an ideal \(I\) of square zero [Tag 01IN]; every prime ideal of \(A'\) contains \(I\), so \(\iota\) is a homeomorphism. The underlying spaces of \(X\) and \(X'\) are identified through \(\iota\). Then \(\mathcal I\) is a quasi-coherent \(\mathcal O_X\)-module [Tag 01QY], and an element of a stalk of \(\mathcal O_{X'}\) is a unit if and only if its image in the stalk of \(\mathcal O_X\) is one, because \(\mathcal I\) consists of nilpotent elements. For a surjection \(\mathcal A'\to\mathcal A\) of rings of a topos with kernel \(\mathcal J\) of square zero, \(L_{\mathcal A/\mathcal A'}\) has \(H^0=\Omega_{\mathcal A/\mathcal A'}=0\) and \(H^{-1}=\mathcal J/\mathcal J^2=\mathcal J\), and no cohomology in degrees \(>0\) (Theorem 6.1 of *The cotangent complex*, in the sheaf form of its Section 10). So \(L_{\mathcal A/\mathcal A'}\) lies in \(D^{\leq-1}\), and its *conormal truncation* is the map
\[
t\colon L_{\mathcal A/\mathcal A'}\longrightarrow\mathcal J[1]
\]
inducing the identity on \(H^{-1}\). It exists and is unique, because for \(K\in D^{\leq-1}\) and a module \(N\), \(\varphi\mapsto H^{-1}(\varphi)\) is a bijection \(\operatorname{Hom}(K,N[1])\to\operatorname{Hom}(H^{-1}K,N)\) [Tag 06XS].

We also use the following form of right exactness. Let \(\mathcal A\to\mathcal B\) be a map of rings of a topos and \(K\in D^{\leq n}(\mathcal A)\). By [Tag 05T7] \(K\) is represented by a complex \(P\) of flat modules with \(P^m=0\) for \(m>n\) (every module is a quotient of a flat one, a sum of free modules on objects of the topos). \(P\) is K-flat [Tag 06YQ], so \(K\otimes^{\mathbf L}_{\mathcal A}\mathcal B=P\otimes_{\mathcal A}\mathcal B\) lies in \(D^{\leq n}(\mathcal B)\), and \(H^n(P\otimes\mathcal B)=\) \(\operatorname{coker}(P^{n-1}\otimes\mathcal B\to P^n\otimes\mathcal B)=\) \(H^n(P)\otimes\mathcal B\). This gives an isomorphism
\[
\begin{aligned}&H^n(K\otimes^{\mathbf L}_{\mathcal A}\mathcal B)\\&\quad \cong H^n(K)\otimes_{\mathcal A}\mathcal B,\end{aligned} \tag{0.1}
\]
natural in \(K\in D^{\leq n}(\mathcal A)\). The same holds for \(Lf^*\) of a morphism of ringed topoi: \(H^n(Lf^*K)\cong f^*H^n(K)\) for \(K\in D^{\leq n}\).

## 1. The cotangent complex of a morphism of diagrams

**Definition 1.1.** Let \(f\colon X\to Y\) be a morphism of diagrams of schemes. Its *cotangent complex* is
\[
L_{X/Y}=L_{\mathcal O_X/f^{-1}\mathcal O_Y}\in D(\mathcal O_X),
\]
the cotangent complex of the ring map \(f^\sharp\colon f^{-1}\mathcal O_Y\to\mathcal O_X\) of the topos \(\operatorname{Top}(X_{\mathrm{Zar}})\), made by the sheaf construction of Section 10 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#10-morphisms-of-schemes). It is a complex of flat \(\mathcal O_X\)-modules, zero in positive degrees, hence K-flat [Tag 06YQ]. We write \(\Omega_{X/Y}=\Omega_{\mathcal O_X/f^{-1}\mathcal O_Y}\). For a morphism of schemes this is the cotangent complex of Section 10 of *The cotangent complex*.

**Proposition 1.2.** Let \(f\colon X\to Y\) be a morphism of diagrams of type \(u\colon I\to J\).

1. For every object \(i\) of \(I\), \(i^*L_{X/Y}=L_{X_i/Y_{u(i)}}\). For every arrow \(\alpha\colon i\to j\) of \(I\), the structure map \(X_\alpha^*L_{X_j/Y_{u(j)}}\to L_{X_i/Y_{u(i)}}\) of \(L_{X/Y}\) is the functoriality map of the square formed by \(X_\alpha\), \(Y_{u(\alpha)}\), \(f_i\) and \(f_j\).
2. The cohomology modules of \(L_{X/Y}\) are termwise quasi-coherent, and \(H^0L_{X/Y}=\Omega_{X/Y}\), with the levels \(\Omega_{X_i/Y_{u(i)}}\).
3. \(L_{X/Y}\) is quasi-cartesian if and only if, for every arrow \(\alpha\colon i\to j\) of \(I\), the functoriality map
\[
LX_\alpha^*L_{X_j/Y_{u(j)}}\longrightarrow L_{X_i/Y_{u(i)}}
\]
is an isomorphism in \(D(\mathcal O_{X_i})\).

**Proof.** (1) The functor \(i^*\) is the inverse image of a morphism of topoi, with \(i^*\mathcal O_X=\mathcal O_{X_i}\) and \(i^*f^{-1}\mathcal O_Y=f_i^{-1}\mathcal O_{Y_{u(i)}}\). Inverse images preserve the polynomial constructions, so \(i^*\) carries the standard resolution of \(\mathcal O_X\) over \(f^{-1}\mathcal O_Y\), its modules of differentials and their normalization to the same constructions for \(f_i^\sharp\). Thus \(i^*L_{X/Y}=L_{X_i/Y_{u(i)}}\) as complexes. For a ring \(\mathcal A\) and an object \(S\) of \(\operatorname{Top}(X_{\mathrm{Zar}})\), the free polynomial algebra \(\mathcal A[S]\) is made from finite products and colimits of copies of \(\mathcal A\) and \(S\), which are formed levelwise; so its structure map at \(\alpha\) is the ring map
\[
\begin{aligned}&X_\alpha^{-1}(\mathcal A_j[S_j])\\&\quad =(X_\alpha^{-1}\mathcal A_j)[X_\alpha^{-1}S_j]\\&\quad \longrightarrow\mathcal A_i[S_i]\end{aligned}
\]
induced by \(\mathcal A_\alpha\) and \(S_\alpha\). By induction on the simplicial degree, the structure maps of the standard resolution of \(\mathcal O_X\) over \(f^{-1}\mathcal O_Y\) are the maps of standard resolutions induced by the map of ring pairs
\[
\begin{aligned}&\bigl(X_\alpha^{-1}f_j^{-1}\mathcal O_{Y_{u(j)}}\to X_\alpha^{-1}\mathcal O_{X_j}\bigr)\\&\quad \longrightarrow\bigl(f_i^{-1}\mathcal O_{Y_{u(i)}}\to\mathcal O_{X_i}\bigr),\end{aligned}
\]
and the structure maps of \(L_{X/Y}\) are the functoriality maps of the squares.

(2) The levels of \(H^qL_{X/Y}\) are the \(H^qL_{X_i/Y_{u(i)}}\), by (1) and the exactness of \(i^*\), and these are quasi-coherent by Proposition 10.1 of *The cotangent complex*. The sheaf form of its Theorem 6.1 gives \(H^0L_{\mathcal B/\mathcal A}=\Omega_{\mathcal B/\mathcal A}\) for every ring map \(\mathcal A\to\mathcal B\) of a topos.

(3) Since \(L_{X_j/Y_{u(j)}}\) is K-flat, the map \(LX_\alpha^*(L_{X/Y})_j\to(L_{X/Y})_i\) of the definition of quasi-cartesian objects is the structure map of the complex \(L_{X/Y}\), and (1) identifies it with the functoriality map. \(\square\)

**Proposition 1.3 (transitivity triangle).** Let \(f\colon X\to Y\) be a morphism of diagrams of type \(u\) and \(g\colon Y\to Z\) one of type \(v\). There is a distinguished triangle in \(D(\mathcal O_X)\)
\[
\begin{aligned}&Lf^*L_{Y/Z} \longrightarrow L_{X/Z}\\&\quad \longrightarrow L_{X/Y}\\&\quad \xrightarrow{\ K(X/Y/Z)\ }Lf^*L_{Y/Z}[1],\end{aligned} \tag{1.1}
\]
whose first two arrows are functoriality maps. It is natural for maps of triples of rings of \(\operatorname{Top}(X_{\mathrm{Zar}})\), and its restriction to every level \(i\) is the triangle (10.3) of *The cotangent complex* for \(X_i\to Y_{u(i)}\to Z_{vu(i)}\). The arrow \(K(X/Y/Z)\in\operatorname{Ext}^1(L_{X/Y},Lf^*L_{Y/Z})\) is the *Kodaira–Spencer class* of \(X\to Y\to Z\).

**Proof.** Apply the sheaf form of Theorem 4.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#4-the-fundamental-triangle) (Section 10 there) to the ring maps
\[
\begin{aligned}&(gf)^{-1}\mathcal O_Z =f^{-1}g^{-1}\mathcal O_Z\\&\quad \longrightarrow f^{-1}\mathcal O_Y \longrightarrow\mathcal O_X\end{aligned}
\]
of \(\operatorname{Top}(X_{\mathrm{Zar}})\). The triangle is natural for maps of the triple of rings (the last paragraph of the proof of Theorem 4.1). Since \(f^{-1}\) preserves the polynomial constructions, \(L_{f^{-1}\mathcal O_Y/f^{-1}g^{-1}\mathcal O_Z}=f^{-1}L_{Y/Z}\), a complex of flat \(f^{-1}\mathcal O_Y\)-modules, zero in positive degrees. So the first term is \(f^{-1}L_{Y/Z}\otimes_{f^{-1}\mathcal O_Y}\mathcal O_X=f^*L_{Y/Z}\), which computes \(Lf^*L_{Y/Z}\) because \(L_{Y/Z}\) is K-flat [Tag 06YY]. The construction commutes with the exact functor \(i^*\), which carries these rings to \(f_i^{-1}g_{u(i)}^{-1}\mathcal O_{Z_{vu(i)}}\to f_i^{-1}\mathcal O_{Y_{u(i)}}\to\mathcal O_{X_i}\). \(\square\)

**Proposition 1.4 (Tor-independent base change).** Let
\[
\begin{array}{ccc}
X_1&\xrightarrow{\ a\ }&X\\
{\scriptstyle f_1}\downarrow&&\downarrow{\scriptstyle f}\\
Y_1&\xrightarrow{\ b\ }&Y
\end{array}
\]
be a cartesian square of schemes such that \(X\) and \(Y_1\) are Tor independent over \(Y\) [Tag 08IA]. Then the functoriality map \(La^*L_{X/Y}\to L_{X_1/Y_1}\) is an isomorphism. Consequently, if \(f\colon X\to Y\) is a morphism of diagrams of type \(u\) such that for every arrow \(\alpha\colon i\to j\) of \(I\) the square formed by \(X_\alpha\), \(Y_{u(\alpha)}\), \(f_i\), \(f_j\) is cartesian and \(X_j\) and \(Y_{u(i)}\) are Tor independent over \(Y_{u(j)}\), then \(L_{X/Y}\) is quasi-cartesian. This holds in particular when these squares are cartesian and every \(f_j\), or every \(Y_{u(\alpha)}\), is flat.

**Proof.** The Zariski topos of \(X_1\) has enough points, so it suffices to show that the map is an isomorphism on the stalks at every \(x_1\in X_1\). Let \(x\), \(y_1\), \(y\) be the images of \(x_1\) in \(X\), \(Y_1\), \(Y\). Since \(L_{X/Y}\) is a complex of flat modules, \(La^*L_{X/Y}=a^*L_{X/Y}\), whose stalk at \(x_1\) is \((L_{X/Y})_x\otimes_{\mathcal O_{X,x}}\mathcal O_{X_1,x_1}\) [Tags 008H, 01CB]. Stalks commute with the polynomial constructions (proof of Proposition 10.1 of *The cotangent complex*), so \((L_{X/Y})_x=L_{\mathcal O_{X,x}/\mathcal O_{Y,y}}\), a complex of flat \(\mathcal O_{X,x}\)-modules, \((L_{X_1/Y_1})_{x_1}=L_{\mathcal O_{X_1,x_1}/\mathcal O_{Y_1,y_1}}\), and the stalk of the functoriality map is the functoriality map (2.6) of Theorem 2.2 there for the square of local rings.

Choose affine opens \(W=\operatorname{Spec}C\) of \(Y\) containing \(y\), \(U=\operatorname{Spec}A\subseteq f^{-1}(W)\) containing \(x\) and \(V=\operatorname{Spec}B_1\subseteq b^{-1}(W)\) containing \(y_1\). Then \(U\times_WV=\operatorname{Spec}(A\otimes_CB_1)\) is an open subscheme of \(X_1\) containing \(x_1\) [Tags 01I4, 01JR]. Let \(\mathfrak q\) be the prime of \(x_1\) in \(A\otimes_CB_1\), and \(\mathfrak p\), \(\mathfrak s\), \(\mathfrak r\) its images in \(A\), \(B_1\), \(C\). The images of \(A\setminus\mathfrak p\) and \(B_1\setminus\mathfrak s\) are invertible in \((A\otimes_CB_1)_{\mathfrak q}=\mathcal O_{X_1,x_1}\), so \(\mathcal O_{X_1,x_1}\) is a localization of
\[
R=A_{\mathfrak p}\otimes_C(B_1)_{\mathfrak s}=\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}\mathcal O_{Y_1,y_1},
\]
where the two tensor products agree because \(C\to C_{\mathfrak r}\) is an epimorphism of rings. The rings \(\mathcal O_{X,x}\) and \(\mathcal O_{Y_1,y_1}\) are Tor independent over \(\mathcal O_{Y,y}\) [Tags 08IA, 0660], so Proposition 3.1 of *The cotangent complex* gives an isomorphism \(L_{\mathcal O_{X,x}/\mathcal O_{Y,y}}\otimes_{\mathcal O_{X,x}}R\to L_{R/\mathcal O_{Y_1,y_1}}\), and its localization formula (5.1) gives \(L_{R/\mathcal O_{Y_1,y_1}}\otimes_R\mathcal O_{X_1,x_1}\cong L_{\mathcal O_{X_1,x_1}/\mathcal O_{Y_1,y_1}}\). Both are functoriality maps, and functoriality maps compose (Theorem 2.2 there); their composite is the stalk of our map, which is therefore an isomorphism.

The consequence follows from Proposition 1.2 (3). If \(f_j\) or \(Y_{u(\alpha)}\) is flat, the local rings of \(X_j\), or those of \(Y_{u(i)}\), are flat over the local rings of \(Y_{u(j)}\), and the higher Tor groups vanish; this gives the flat case. \(\square\)

## 2. Extensions of diagrams

**Definition 2.1.** Let \(f\colon X\to Y\) be a morphism of diagrams of type \(u\colon I\to J\). A *\(Y\)-extension* of \(X\) is a triple \((X',\iota,f')\) of a diagram \(X'\colon I\to(\mathrm{Sch})\), an \(I\)-morphism \(\iota\colon X\to X'\) and a morphism \(f'\colon X'\to Y\) of type \(u\) with \(f'\iota=f\), such that every \(\iota_i\colon X_i\to X'_i\) is a first-order thickening. When \(Y\) is the final diagram we say *extension* of \(X\).

Let \(\mathcal I_i\subseteq\mathcal O_{X'_i}\) be the ideal of \(\iota_i\); identify the spaces of \(X_i\) and \(X'_i\). For \(\alpha\colon i\to j\), \(X'_\alpha\iota_i=\iota_jX_\alpha\), so \(X'_\alpha\) has the underlying map of \(X_\alpha\). The composite
\[
X_\alpha^{-1}\mathcal I_j\to X_\alpha^{-1}\mathcal O_{X'_j}\to\mathcal O_{X'_i}\to\mathcal O_{X_i}
\]
equals \(X_\alpha^{-1}\mathcal I_j\to X_\alpha^{-1}\mathcal O_{X'_j}\to X_\alpha^{-1}\mathcal O_{X_j}\to\mathcal O_{X_i}\), which is zero, so \(X'^\sharp_\alpha\) carries \(X_\alpha^{-1}\mathcal I_j\) into \(\mathcal I_i\). The resulting maps \(X_\alpha^{-1}\mathcal I_j\to\mathcal I_i\) are linear over \(X_\alpha^{-1}\mathcal O_{X_j}\to\mathcal O_{X_i}\), and their \(\mathcal O_{X_i}\)-linear extensions \(\mathcal I_\alpha\colon X_\alpha^*\mathcal I_j\to\mathcal I_i\) are compatible with composites because the \(X'^\sharp_\alpha\) are. So the \(\mathcal I_i\) form a termwise quasi-coherent \(\mathcal O_X\)-module \(\mathcal I\), the *ideal* of the extension. A *\(Y\)-extension of \(X\) by* an \(\mathcal O_X\)-module \(M\) is a \(Y\)-extension with an isomorphism \(\mathcal I\cong M\). An *isomorphism* \((X'_1,\iota_1,f'_1)\to(X'_2,\iota_2,f'_2)\) of \(Y\)-extensions of \(X\) by \(M\) is an \(I\)-morphism \(h\colon X'_1\to X'_2\) with \(h\iota_1=\iota_2\) and \(f'_2h=f'_1\), compatible with the identifications of the ideals with \(M\); Proposition 2.3 shows that it is an isomorphism of diagrams.

**Construction 2.2.** Let \((X',\iota,f')\) be a \(Y\)-extension of \(X\) with ideal \(\mathcal I\). The rings \(\mathcal O_{X'_i}\), on the spaces of the \(X_i\), with the ring maps \(X'^\sharp_\alpha\colon X_\alpha^{-1}\mathcal O_{X'_j}\to\mathcal O_{X'_i}\), form a ring \(\mathcal O_{X'}\) of \(\operatorname{Top}(X_{\mathrm{Zar}})\). The maps \(\iota_i^\sharp\) form a surjection \(\mathcal O_{X'}\to\mathcal O_X\) with kernel \(\mathcal I\), and since \(f'_i\) has the underlying map of \(f_i\), the maps \(f'^\sharp_i\colon f_i^{-1}\mathcal O_{Y_{u(i)}}\to\mathcal O_{X'_i}\) form a ring map \(f^{-1}\mathcal O_Y\to\mathcal O_{X'}\), compatible with the structure maps because \(f'_jX'_\alpha=Y_{u(\alpha)}f'_i\). So
\[
0\longrightarrow\mathcal I\longrightarrow\mathcal O_{X'}\longrightarrow\mathcal O_X\longrightarrow0
\]
is an extension of \(f^{-1}\mathcal O_Y\)-algebras of \(\mathcal O_X\) by \(\mathcal I\) on \(\operatorname{Top}(X_{\mathrm{Zar}})\) in the sense of [*The cotangent complex*, Section 10](course:AG-HP/the-cotangent-complex#extensions-of-sheaves-of-algebras): \(\mathcal I^2=0\), and the \(\mathcal O_X\)-module structure induced on \(\mathcal I\) is the given one. An isomorphism \(h\) of \(Y\)-extensions gives the isomorphism of algebra extensions \(h^\sharp\colon\mathcal O_{X'_2}\to\mathcal O_{X'_1}\).

**Proposition 2.3.** Let \(f\colon X\to Y\) be a morphism of diagrams and \(M\) a termwise quasi-coherent \(\mathcal O_X\)-module.

1. For \(Y\)-extensions \(X'_1\), \(X'_2\) of \(X\) by \(M\), \(h\mapsto h^\sharp\) is a bijection from the isomorphisms \(X'_1\to X'_2\) of \(Y\)-extensions by \(M\) onto the isomorphisms \(\mathcal O_{X'_2}\to\mathcal O_{X'_1}\) of extensions of \(f^{-1}\mathcal O_Y\)-algebras inducing the identity on \(M\) and on \(\mathcal O_X\).
2. Every extension of \(f^{-1}\mathcal O_Y\)-algebras of \(\mathcal O_X\) by \(M\) on \(\operatorname{Top}(X_{\mathrm{Zar}})\) is \(\mathcal O_{X'}\) for a \(Y\)-extension \(X'\) of \(X\) by \(M\).

In particular \(X'\mapsto\mathcal O_{X'}\) is a bijection between isomorphism classes, and \(h\mapsto(h^\sharp)^{-1}\) is an isomorphism from the automorphism group of \(X'\) onto that of the algebra extension \(\mathcal O_{X'}\).

**Proof.** (1) Let \(h\) be a morphism with \(h\iota_1=\iota_2\) and \(f'_2h=f'_1\). Since the \(\iota\) are homeomorphisms, every \(h_i\) has the identity as its underlying map, so \(h\) is determined by the ring maps \(h_i^\sharp\colon\mathcal O_{X'_{2,i}}\to\mathcal O_{X'_{1,i}}\). The conditions that \(h\) be an \(I\)-morphism, that \(h\iota_1=\iota_2\), that \(f'_2h=f'_1\), and that \(h\) be compatible with the identifications of the ideals with \(M\), say that the \(h_i^\sharp\) form a map of rings of \(\operatorname{Top}(X_{\mathrm{Zar}})\) under \(f^{-1}\mathcal O_Y\), over \(\mathcal O_X\), inducing the identity on \(M\). Conversely, let \(\varphi\colon\mathcal O_{X'_2}\to\mathcal O_{X'_1}\) be such a map. At every level it is an isomorphism, by the five lemma, so \((\mathrm{id},\varphi_i)\colon X'_{1,i}\to X'_{2,i}\) is an isomorphism of locally ringed spaces, and these form an isomorphism of \(Y\)-extensions with \(h^\sharp=\varphi\).

(2) Let \(0\to M\to\mathcal E\to\mathcal O_X\to0\) be an extension of \(f^{-1}\mathcal O_Y\)-algebras. Restriction to the level \(i\) is exact, so \(\mathcal E_i\) is a sheaf of \(f_i^{-1}\mathcal O_{Y_{u(i)}}\)-algebras on the space of \(X_i\), and \(0\to M_i\to\mathcal E_i\to\mathcal O_{X_i}\to0\) is a square-zero extension with quasi-coherent kernel. By the paragraph on schemes at the end of [Section 10 of *The cotangent complex*](course:AG-HP/the-cotangent-complex#global-lifting-over-a-thickened-base), the ringed space \(X'_i\) formed by the space of \(X_i\) and \(\mathcal E_i\) is a scheme, every affine open \(\operatorname{Spec}R\) of \(X_i\) being the affine open \(\operatorname{Spec}E\) of \(X'_i\), with \(E=\mathcal E_i(\operatorname{Spec}R)\) and \(E/M_i(\operatorname{Spec}R)=R\); and the morphism \(f'_i\colon X'_i\to Y_{u(i)}\) defined by \(f_i\) and the ring map \(f_i^{-1}\mathcal O_{Y_{u(i)}}\to\mathcal E_i\) is a morphism of schemes. On these affine opens, \(\iota_i\colon X_i\to X'_i\), given by the identity of spaces and \(\mathcal E_i\to\mathcal O_{X_i}\), is \(\operatorname{Spec}(E/M_i(\operatorname{Spec}R))\to\operatorname{Spec}E\); so it is a first-order thickening with ideal \(M_i\).

For \(\alpha\colon i\to j\), the ring map \(\mathcal E_\alpha\colon X_\alpha^{-1}\mathcal E_j\to\mathcal E_i\) defines a morphism of ringed spaces \(X'_\alpha\colon X'_i\to X'_j\) with the underlying map of \(X_\alpha\). It is a morphism of locally ringed spaces. Let \(x\in X_i\), \(y=X_\alpha(x)\), and let \(e\) be a non-unit of the stalk \(\mathcal E_{j,y}\). Its image in \(\mathcal O_{X_j,y}\) is a non-unit, hence so is its image in \(\mathcal O_{X_i,x}\), \(X_\alpha\) being a morphism of locally ringed spaces. Since \(\mathcal E\to\mathcal O_X\) is compatible with the structure maps, this is also the image of \(\mathcal E_\alpha(e)\in\mathcal E_{i,x}\), so \(\mathcal E_\alpha(e)\) is a non-unit. The compatibility of \(\mathcal E\), of \(\mathcal E\to\mathcal O_X\) and of \(f^{-1}\mathcal O_Y\to\mathcal E\) with composites and structure maps says that \(X'\) is a diagram, \(\iota\) an \(I\)-morphism and \(f'\) a morphism of type \(u\) with \(f'\iota=f\). Construction 2.2 applied to \(X'\) returns \(\mathcal E\). \(\square\)

**Theorem 2.4.** Let \(f\colon X\to Y\) be a morphism of diagrams and \(M\) a termwise quasi-coherent \(\mathcal O_X\)-module. For a \(Y\)-extension \(X'\) of \(X\) by \(M\), let
\[
e(X')\colon L_{X/Y}\longrightarrow L_{\mathcal O_X/\mathcal O_{X'}}\xrightarrow{\ t\ }M[1]
\]
be the composite of the functoriality map, for the map of ring pairs \((f^{-1}\mathcal O_Y\to\mathcal O_X)\to(\mathcal O_{X'}\to\mathcal O_X)\), and the conormal truncation (the class \(\kappa_M\) of (10.6) of *The cotangent complex*).

1. \(e(X')\in\operatorname{Ext}^1(L_{X/Y},M)\) depends only on the isomorphism class of \(X'\), and \(X'\mapsto e(X')\) is a bijection from the set of isomorphism classes of \(Y\)-extensions of \(X\) by \(M\) onto \(\operatorname{Ext}^1(L_{X/Y},M)\). The extension whose levels are the spaces of the \(X_i\) with the rings \(\mathcal O_{X_i}\oplus M_i\) has class \(0\).
2. The automorphism group of a \(Y\)-extension of \(X\) by \(M\) is isomorphic to \(\operatorname{Ext}^0(L_{X/Y},M)=\operatorname{Hom}(\Omega_{X/Y},M)\), the group of \(f^{-1}\mathcal O_Y\)-derivations of \(\mathcal O_X\) into \(M\).
3. For every \(q\), \(\operatorname{Ext}^q(L_{X/Y},M)\cong\) \(\operatorname{Ext}^q(L\varepsilon^*L_{X/Y},\varepsilon^*M)\), where \(\varepsilon\colon\operatorname{Top}(X_{\mathrm{fppf}})\to\operatorname{Top}(X_{\mathrm{Zar}})\) is the comparison morphism of Construction 4.1 of the lesson on big fppf sites.

The Ext groups are formed in the categories of modules of the ringed topoi \(\operatorname{Top}(X_{\mathrm{Zar}})\) and \(\operatorname{Top}(X_{\mathrm{fppf}})\).

**Proof.** (1) and (2) By Proposition 2.3, the isomorphism classes and automorphism groups of \(Y\)-extensions of \(X\) by \(M\) are those of extensions of \(f^{-1}\mathcal O_Y\)-algebras of \(\mathcal O_X\) by \(M\) on \(\operatorname{Top}(X_{\mathrm{Zar}})\), the topos of sheaves on a small site. Theorem 10.3 of *The cotangent complex*, applied to \(f^{-1}\mathcal O_Y\to\mathcal O_X\), shows that \(\kappa_M\) is a bijection onto \(\operatorname{Ext}^1(L_{X/Y},M)\), carrying the split algebra \(\mathcal O_X\oplus M\) to \(0\), and identifies the automorphism groups with \(\operatorname{Ext}^0(L_{X/Y},M)\). Since \(L_{X/Y}\in D^{\leq0}\), \(\operatorname{Ext}^0(L_{X/Y},M)=\operatorname{Hom}(H^0L_{X/Y},M)\) [Tag 06XS], and \(H^0L_{X/Y}=\Omega_{X/Y}\) (Proposition 1.2 (2)) represents the derivations. The split extension is the \(\mathcal O_{X'}\) of the extension with levels \(\mathcal O_{X_i}\oplus M_i\) (Proposition 2.3 (2)).

(3) \(L_{X/Y}\in D^-(X_{\mathrm{Zar}})\) and \(M\in D^b_{\mathrm{qc}}(X_{\mathrm{Zar}})\) with \(H^qM=0\) for \(q<0\). Lemma 4.2 (2) of the lesson on big fppf sites (the diagram form of its Corollary 2.2 (1)), with \(n=0\), gives \(\operatorname{RHom}(L_{X/Y},M)\cong\) \(\operatorname{RHom}(L\varepsilon^*L_{X/Y},t_{[0}L\varepsilon^*M)\). By (0.1) applied to \(\varepsilon\), \(L\varepsilon^*M\in D^{\leq0}\) and \(H^0L\varepsilon^*M=\varepsilon^*M\), so \(t_{[0}L\varepsilon^*M=\varepsilon^*M\). \(\square\)

The group \(\operatorname{Ext}^1(L_{X/Y},M)\) is not the product of the groups of the levels. An extension of \(X\) gives an extension of every \(X_i\), and the structure maps of \(X'\) are additional data, constrained by the structure maps of \(L_{X/Y}\) (Proposition 1.2 (1)).

## 3. Deformations

**Definition 3.1.** An extension \(X'\) of a diagram \(X\) (over the final diagram) is a *deformation* of \(X\) if its ideal \(\mathcal I\) is cartesian. For a morphism of schemes \(h\colon X\to Z\), an extension is a commutative square
\[
\begin{array}{ccc}
X&\xrightarrow{\ \iota_X\ }&X'\\
{\scriptstyle h}\downarrow&&\downarrow{\scriptstyle h'}\\
Z&\xrightarrow{\ \iota_Z\ }&Z'
\end{array}
\]
whose rows are first-order thickenings, with ideals \(\mathcal I_X\) and \(\mathcal I_Z\). It is a deformation, and \(h'\) is a *deformation of* \(h\), if the map \(\mathcal I_h\colon h^*\mathcal I_Z\to\mathcal I_X\) of Definition 2.1 is an isomorphism.

**Lemma 3.2.** In the situation of Definition 3.1:

1. \(h^*\mathcal I_Z\to\mathcal I_X\) is surjective if and only if the square is cartesian, that is, \(X\to Z\times_{Z'}X'\) is an isomorphism.
2. \(h^*\mathcal I_Z\to\mathcal I_X\) is an isomorphism if and only if the square is cartesian and \(\operatorname{Tor}_1^{C'}(C'/I,A')=0\) for all affine opens \(\operatorname{Spec}C'\) of \(Z'\) and \(\operatorname{Spec}A'\subseteq h'^{-1}(\operatorname{Spec}C')\), where \(I=\mathcal I_Z(\operatorname{Spec}C')\).

**Proof.** (1) By [Tag 01JU], \(Z\times_{Z'}X'\to X'\) is the closed immersion with ideal \(\mathcal I_Z\mathcal O_{X'}\), the image of \(h'^*\mathcal I_Z\to\mathcal O_{X'}\). Since \(h'\iota_X=\iota_Zh\), this image lies in \(\mathcal I_X\), and \(X\to Z\times_{Z'}X'\) is the closed immersion of closed subschemes of \(X'\) defined by \(\mathcal I_Z\mathcal O_{X'}\subseteq\mathcal I_X\). A closed subscheme is determined by its ideal [Tag 01IN], so the square is cartesian if and only if \(\mathcal I_Z\mathcal O_{X'}=\mathcal I_X\). The map \(h'^*\mathcal I_Z\to\mathcal I_X\) factors through the surjection
\[
\begin{aligned}&h'^*\mathcal I_Z =h'^{-1}\mathcal I_Z\otimes_{h'^{-1}\mathcal O_{Z'}}\mathcal O_{X'}\\&\quad \longrightarrow h^{-1}\mathcal I_Z\otimes_{h^{-1}\mathcal O_Z}\mathcal O_X\\&\quad =h^*\mathcal I_Z,\end{aligned}
\]
since \(\mathcal I_Z\) is an \(\mathcal O_Z\)-module and \(\mathcal I_X\) an \(\mathcal O_X\)-module. So \(h^*\mathcal I_Z\to\mathcal I_X\) and \(h'^*\mathcal I_Z\to\mathcal I_X\) have the same image \(\mathcal I_Z\mathcal O_{X'}\), and (1) follows.

(2) The open subsets \(\operatorname{Spec}A'\) of the statement cover \(X'\). Fix one, let \(I'=\mathcal I_X(\operatorname{Spec}A')\), \(C=C'/I\) and \(A=A'/I'\); then \(Z\cap\operatorname{Spec}C'=\operatorname{Spec}C\) and \(X\cap\operatorname{Spec}A'=\operatorname{Spec}A\) [Tag 01IN]. On \(\operatorname{Spec}A\) the map \(h^*\mathcal I_Z\to\mathcal I_X\) is the map of modules [Tag 01I9]
\[
I\otimes_CA\longrightarrow I',\qquad x\otimes a\longmapsto h'^\sharp(x)\,\tilde a,
\]
with \(\tilde a\in A'\) any lift of \(a\). Suppose the square is cartesian. By (1) and its local form \(I'=IA'\), so \(A=C\otimes_{C'}A'\) and \(I\otimes_CA=I\otimes_C(C\otimes_{C'}A')=I\otimes_{C'}A'\). Tensoring \(0\to I\to C'\to C\to0\) with \(A'\) over \(C'\) gives the exact sequence
\[
\begin{aligned}&0 \to\operatorname{Tor}_1^{C'}(C,A') \to I\otimes_{C'}A'\\&\quad \to A' \to C\otimes_{C'}A' \to0,\end{aligned}
\]
whose second map is \(I\otimes_CA\to I'\subseteq A'\). So this map is injective if and only if \(\operatorname{Tor}_1^{C'}(C,A')=0\). If \(h^*\mathcal I_Z\to\mathcal I_X\) is an isomorphism, the square is cartesian by (1), and the Tor groups vanish on every such chart. Conversely, if the square is cartesian and all these Tor groups vanish, the map is surjective by (1) and injective on a covering of \(X'\). \(\square\)

**Lemma 3.3.** A deformation of an isomorphism of schemes is an isomorphism: in Definition 3.1, if \(h\) is an isomorphism and \(h'\) is a deformation of \(h\), then \(h'\) is an isomorphism.

**Proof.** The underlying map of \(h'\) is that of \(h\), a homeomorphism. The map \(h'^\sharp\) is a map of short exact sequences of sheaves on the space of \(X\), from
\[
0\to h^{-1}\mathcal I_Z\to h^{-1}\mathcal O_{Z'}\to h^{-1}\mathcal O_Z\to0
\]
to
\[
0\to\mathcal I_X\to\mathcal O_{X'}\to\mathcal O_X\to0,
\]
inducing \(h^\sharp\) on the quotients. The map on the quotients is an isomorphism because \(h\) is one. Since \(h^\sharp\) is an isomorphism, \(h^*\mathcal I_Z=h^{-1}\mathcal I_Z\otimes_{h^{-1}\mathcal O_Z}\mathcal O_X=h^{-1}\mathcal I_Z\), and the map on the kernels is \(h^*\mathcal I_Z\to\mathcal I_X\), an isomorphism. By the five lemma \(h'^\sharp\) is an isomorphism, so \(h'\) is an isomorphism of ringed spaces, hence of schemes. \(\square\)

**Lemma 3.4.** Let
\[
\begin{array}{ccc}
X&\xrightarrow{\ \iota_X\ }&X'\\
{\scriptstyle f}\downarrow&&\downarrow{\scriptstyle f'}\\
Y&\xrightarrow{\ \iota_Y\ }&Y'\\
{\scriptstyle g}\downarrow&&\downarrow{\scriptstyle g'}\\
Z&\xrightarrow{\ \iota_Z\ }&Z'
\end{array}
\]
be an extension of the commutative triangle \((f,g,h=gf)\), with \(h'=g'f'\).

1. If \(f'\) and \(g'\) are deformations of \(f\) and \(g\), then \(h'\) is a deformation of \(h\). If \(g'\) and \(h'\) are deformations of \(g\) and \(h\), then \(f'\) is a deformation of \(f\).
2. Suppose that the square formed by \(\iota_Y\), \(\iota_Z\), \(g\), \(g'\) is cartesian and that \(f^*\) is faithful on quasi-coherent \(\mathcal O_Y\)-modules. If \(h'\) is a deformation of \(h\), then \(g'\) is a deformation of \(g\), and \(f'\) is a deformation of \(f\).

**Proof.** (1) The ideal of the extension is a module on the total topos of the triangle, so its structure maps satisfy \(\mathcal I_h=\mathcal I_f\circ f^*(\mathcal I_g)\) through \(h^*=f^*g^*\) (Proposition 4.2 (a) of the lesson on morphisms of fibred topoi); directly, \(h'^\sharp=f'^\sharp\circ f^{-1}(g'^\sharp)\) carries \(h^{-1}\mathcal I_Z\) into \(\mathcal I_X\) through \(f^{-1}\mathcal I_Y\). If \(\mathcal I_f\) and \(\mathcal I_g\) are isomorphisms, so is \(\mathcal I_h\). If \(\mathcal I_g\) and \(\mathcal I_h\) are, then \(f^*(\mathcal I_g)\) is, and \(\mathcal I_f=\mathcal I_h\circ f^*(\mathcal I_g)^{-1}\).

(2) By Lemma 3.2 (1), \(\mathcal I_g\colon g^*\mathcal I_Z\to\mathcal I_Y\) is surjective. Let \(K\) be its kernel, a quasi-coherent \(\mathcal O_Y\)-module [Tag 01IC], so that \(0\to K\to g^*\mathcal I_Z\to\mathcal I_Y\to0\) is exact. The functor \(f^*\) is right exact, so
\[
f^*K\longrightarrow f^*g^*\mathcal I_Z\xrightarrow{\ f^*(\mathcal I_g)\ }f^*\mathcal I_Y\longrightarrow0
\]
is exact. The composite of \(f^*(\mathcal I_g)\) with \(\mathcal I_f\) is \(\mathcal I_h\), an isomorphism, so \(f^*(\mathcal I_g)\) is injective and \(f^*K\to f^*g^*\mathcal I_Z\) is zero. This map is \(f^*\) of the inclusion \(K\to g^*\mathcal I_Z\); by faithfulness the inclusion is zero, so \(K=0\) and \(\mathcal I_g\) is an isomorphism. Then (1) shows that \(f'\) is a deformation of \(f\). \(\square\)

**Remark 3.5.** The functor \(f^*\) is faithful on quasi-coherent modules when \(f\) is an isomorphism, and when \(f\) is flat and surjective. In the second case, let \(\varphi\colon F\to G\) be a map of quasi-coherent \(\mathcal O_Y\)-modules with \(f^*\varphi=0\). Since \(f^*\) is exact [Tag 02N4], \(f^*(\operatorname{Im}\varphi)=\operatorname{Im}(f^*\varphi)=0\). For \(x\in X\), \(\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}\) is flat and local, hence faithfully flat [Tag 00HR], and \((\operatorname{Im}\varphi)_{f(x)}\otimes\mathcal O_{X,x}=(f^*\operatorname{Im}\varphi)_x=0\) [Tags 008H, 01CB], so \((\operatorname{Im}\varphi)_{f(x)}=0\). As \(f\) is surjective, \(\operatorname{Im}\varphi=0\).

**Corollary 3.6.** Let
\[
\begin{array}{ccc}
X&\xrightarrow{\ a\ }&Y\\
{\scriptstyle b}\downarrow&&\downarrow{\scriptstyle c}\\
Z&\xrightarrow{\ d\ }&T
\end{array}
\]
be a commutative square of schemes. Let \(\iota_X\colon X\to X'\) and \(\iota_Y\colon Y\to Y'\) be first-order thickenings and \(a'\colon X'\to Y'\), \(b'\colon X'\to Z\), \(c'\colon Y'\to T\) morphisms with \(a'\iota_X=\iota_Ya\), \(b'\iota_X=b\), \(c'\iota_Y=c\) and \(c'a'=db'\). If the square \(XYZT\) is cartesian and \(a'\) is a deformation of \(a\), then the square formed by \(a'\), \(b'\), \(c'\), \(d\) is cartesian.

**Proof.** Let \(X'_1=Y'\times_TZ\), with the projections \(p\colon X'_1\to Y'\) and \(q\colon X'_1\to Z\), and let \(k\colon X'\to X'_1\) be the map with \(pk=a'\) and \(qk=b'\). The morphism \(X=Y\times_TZ\to Y'\times_TZ=X'_1\) induced by \(\iota_Y\) is the base change of \(\iota_Y\) along \(p\), because \(X'_1\times_{Y'}Y=Y\times_TZ=X\). So it is a closed immersion whose ideal is the image of \(p^*\mathcal I_Y\) [Tag 01JU], an ideal of square zero: a first-order thickening \(\iota_1\colon X\to X'_1\), with \(k\iota_X=\iota_1\), and the square formed by \(\iota_1\), \(\iota_Y\), \(a\), \(p\) is cartesian. Apply Lemma 3.4 (2) to the triangle \((\mathrm{id}_X,a,a)\) with the extension \((k,p,a'=pk)\): the square formed by \(\iota_1\), \(\iota_Y\), \(a\), \(p\) is cartesian, \(\mathrm{id}_X^*\) is faithful, and \(a'\) is a deformation of \(a\). So \(k\) is a deformation of \(\mathrm{id}_X\), and an isomorphism by Lemma 3.3. \(\square\)

**Corollary 3.7.** Let \(X'Y'Z'T'\), with morphisms \(a',b',c',d'\), be an extension of the commutative square \(XYZT\) of Corollary 3.6 in which all four schemes are thickened.

1. If \(b'\), \(c'\) and \(d'\) are deformations of \(b\), \(c\) and \(d\), the extension is a deformation of the square.
2. If the extension is a deformation of the square and the square \(XYZT\) is cartesian, then the square \(X'Y'Z'T'\) is cartesian.

**Proof.** (1) The arrows of the square category are the four sides, the diagonal \(X\to T\) and the identities. Lemma 3.4 (1) applied to the triangle \(X\to Z\to T\) shows that \(d'b'\) is a deformation of \(db\). Since \(c'a'=d'b'\), the same lemma applied to the triangle \(X\to Y\to T\) shows that \(a'\) is a deformation of \(a\).

(2) The square formed by \(\iota_Z\), \(\iota_T\), \(d\), \(d'\) is cartesian by Lemma 3.2 (1), so \(Y\times_{T'}Z'=\) \(Y\times_T(T\times_{T'}Z')=\) \(Y\times_TZ=\) \(X\): the square formed by \(a\), \(\iota_Zb\), \(\iota_Tc\), \(d'\) is cartesian. The thickenings \(X'\), \(Y'\), with \(a'\), \(b'\), \(c'\), form an extension of this square in which \(Z'\) and \(T'\) are not thickened, and \(a'\) is a deformation of \(a\). Corollary 3.6 shows that \(X'Y'Z'T'\) is cartesian. \(\square\)

## 4. Deformations of a morphism over a thickened target

In this section \(f\colon X\to Y\) is a morphism of diagrams of type \(u\colon I\to J\), and \((Y',\iota_Y)\) is an extension of \(Y\) with ideal \(\mathcal J\), a termwise quasi-coherent \(\mathcal O_Y\)-module. By Construction 2.2 the \(\mathcal O_{Y'_j}\) form a ring \(\mathcal O_{Y'}\) of \(\operatorname{Top}(Y_{\mathrm{Zar}})\) with a surjection onto \(\mathcal O_Y\) of kernel \(\mathcal J\).

**Definition 4.1.** A *deformation of \(f\) over \(Y'\)* is a triple \((X',\iota,f')\) which is a \(Y'\)-extension of \(X\) for the morphism \(\iota_Yf\colon X\to Y'\), such that the map \(f^*\mathcal J\to\mathcal I\) to its ideal, induced by \(f'\), is an isomorphism. Here \(f'^\sharp_i\) carries \(f_i^{-1}\mathcal J_{u(i)}\) into \(\mathcal I_i\), by the argument of Definition 2.1, and the induced maps form an \(\mathcal O_X\)-linear map \(f^*\mathcal J\to\mathcal I\). A deformation of \(f\) over \(Y'\) is thus a \(Y'\)-extension of \(X\) by \(f^*\mathcal J\), the identification being induced by \(f'\). Isomorphisms of deformations are isomorphisms of these \(Y'\)-extensions; they are automatically compatible with the identifications, since these are induced by the \(f'\).

**Construction 4.2.** On \(\operatorname{Top}(X_{\mathrm{Zar}})\) put
\[
\begin{gathered}\mathcal A'=f^{-1}\mathcal O_{Y'},\\ \mathcal A=f^{-1}\mathcal O_Y,\\ \mathcal B=\mathcal O_X.\end{gathered}
\]
Since \(f^{-1}\) is exact, \(\mathcal A'\to\mathcal A\) is surjective with kernel \(f^{-1}\mathcal J\) of square zero, and \(L_{\mathcal A/\mathcal A'}\in D^{\leq-1}\) with \(H^{-1}=f^{-1}\mathcal J\). Let
\[
D=L_{\mathcal A/\mathcal A'}\otimes^{\mathbf L}_{\mathcal A}\mathcal B.
\]
By (0.1), \(D\in D^{\leq-1}\) and \(H^{-1}D=f^{-1}\mathcal J\otimes_{\mathcal A}\mathcal B=f^*\mathcal J\). Let \(\tilde c\colon D\to f^*\mathcal J[1]\) be the map inducing the identity on \(H^{-1}\) [Tag 06XS]. Let
\[
D\longrightarrow L_{\mathcal B/\mathcal A'}\longrightarrow L_{X/Y}\xrightarrow{\ w\ }D[1]
\]
be the transitivity triangle of \(\mathcal A'\to\mathcal A\to\mathcal B\), with \(L_{\mathcal B/\mathcal A}=L_{X/Y}\). The *obstruction* of \(f\) over \(Y'\) is
\[
\begin{aligned}&\omega(f,Y') =\tilde c[1]\circ w\\&\quad \in\operatorname{Hom}(L_{X/Y},f^*\mathcal J[2])\\&\quad =\operatorname{Ext}^2(L_{X/Y},f^*\mathcal J).\end{aligned}
\]

**Theorem 4.3.** Let \(f\colon X\to Y\) be a morphism of diagrams of type \(u\) and \(Y'\) an extension of \(Y\) with termwise quasi-coherent ideal \(\mathcal J\).

1. A deformation of \(f\) over \(Y'\) exists if and only if \(\omega(f,Y')=0\).
2. If \(\omega(f,Y')=0\), the set of isomorphism classes of deformations of \(f\) over \(Y'\) is a torsor under \(\operatorname{Ext}^1(L_{X/Y},f^*\mathcal J)\), and the automorphism group of each deformation is isomorphic to \(\operatorname{Ext}^0(L_{X/Y},f^*\mathcal J)\).
3. Let \(g\colon Y\to Z\) be a morphism of diagrams of type \(v\), and \(g'\colon Y'\to Z\) one of type \(v\) with \(g'\iota_Y=g\), so that \(Y'\) is a \(Z\)-extension of \(Y\) by \(\mathcal J\), with class \(e(Y')\in\operatorname{Ext}^1(L_{Y/Z},\mathcal J)\) (Theorem 2.4). Let \(f^*e(Y')\colon Lf^*L_{Y/Z}\to f^*\mathcal J[1]\) be \(Lf^*(e(Y'))\) followed by the map \(Lf^*\mathcal J[1]\to f^*\mathcal J[1]\) inducing the identity on \(H^{-1}\). Then
\[
\begin{aligned}&\omega(f,Y')\\&\quad =f^*e(Y')[1]\circ K(X/Y/Z)\\&\quad \colon L_{X/Y} \longrightarrow Lf^*L_{Y/Z}[1]\\&\quad \longrightarrow f^*\mathcal J[2].\end{aligned}
\]

Every extension of \(Y\) is a \(Z\)-extension for the final diagram \(Z=\operatorname{Spec}\mathbb Z\), so (3) always expresses \(\omega(f,Y')\) through the Kodaira–Spencer class of \(X\to Y\to\operatorname{Spec}\mathbb Z\) and the class of \(Y'\) as an extension.

**Proof.** (1) and (2) The morphism \(\iota_Yf\colon X\to Y'\) has type \(u\), and its ring map is \(\mathcal A'\to\mathcal B\), since \(\iota_Y\) is the identity on spaces. The module \(f^*\mathcal J\) is termwise quasi-coherent, its levels being pullbacks of quasi-coherent modules. By Proposition 2.3 for \(\iota_Yf\), deformations of \(f\) over \(Y'\), with their isomorphisms, correspond to the extensions of \(\mathcal A'\)-algebras
\[
0\longrightarrow f^*\mathcal J\longrightarrow\mathcal E\longrightarrow\mathcal B\longrightarrow0
\]
whose structure map carries \(f^{-1}\mathcal J=\ker(\mathcal A'\to\mathcal A)\) into \(f^*\mathcal J\) by the canonical map \(c\colon f^{-1}\mathcal J\to f^*\mathcal J\), \(x\mapsto1\otimes x\), with their isomorphisms. Theorem 10.4 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#global-lifting-over-a-thickened-base), with \(M=f^*\mathcal J\) and this \(c\), describes these. In its proof \(\operatorname{Ext}^1(D,M)\) is identified with \(\operatorname{Hom}_{\mathcal A}(f^{-1}\mathcal J,M)\) by composing \(D\to(\mathcal B\otimes_{\mathcal A}f^{-1}\mathcal J)[1]\) with the \(\mathcal B\)-linear extension of a map; \(c\) extends to the identity of \(f^*\mathcal J=\mathcal B\otimes_{\mathcal A}f^{-1}\mathcal J\), so \(c\) corresponds to \(\tilde c\). The exact sequence (10.9) there has \(\partial\) the composition with \(w\): for a distinguished triangle \(K_1\xrightarrow{p}K_2\to K_3\xrightarrow{w}K_1[1]\) and an object \(N\), the sequence
\[
\begin{aligned}&\operatorname{Hom}(K_2,N[1]) \xrightarrow{\ p^*\ }\operatorname{Hom}(K_1,N[1])\\&\quad \xrightarrow{\ \varphi\mapsto\varphi[1]\circ w\ }\operatorname{Hom}(K_3,N[2])\end{aligned}
\]
is exact, by [Tag 0149] applied to the distinguished triangle \(K_3\xrightarrow{w}K_1[1]\xrightarrow{-p[1]}K_2[1]\to K_3[1]\) obtained by rotation. Thus the obstruction of Theorem 10.4 is \(\partial c=\tilde c[1]\circ w=\omega(f,Y')\). Theorem 10.4 says that an extension with structure map \(c\) exists if and only if \(\partial c=0\), that the isomorphism classes then form a torsor under \(\operatorname{Ext}^1(L_{X/Y},f^*\mathcal J)\), and that the automorphism group of each is \(\operatorname{Ext}^0(L_{X/Y},f^*\mathcal J)\). Proposition 2.3 transfers these statements to deformations.

(3) Put \(\mathcal Z=(gf)^{-1}\mathcal O_Z=f^{-1}g^{-1}\mathcal O_Z\). The ring map \(g'^\sharp\colon g^{-1}\mathcal O_Z=g'^{-1}\mathcal O_Z\to\mathcal O_{Y'}\) of \(\operatorname{Top}(Y_{\mathrm{Zar}})\) gives \(\mathcal Z\to\mathcal A'\), whose composite with \(\mathcal A'\to\mathcal A\) is \(f^{-1}(g^\sharp)\), because \(g'\iota_Y=g\). So \((\mathcal Z\to\mathcal A'\to\mathcal A\to\mathcal B)\) gives a map of triples \((\mathcal Z,\mathcal A,\mathcal B)\to(\mathcal A',\mathcal A,\mathcal B)\), equal to the identity on \(\mathcal A\) and \(\mathcal B\). By the naturality of the transitivity triangle (Proposition 1.3), the triangle of the first triple,
\[
\begin{gathered}Lf^*L_{Y/Z}\to L_{X/Z}\to L_{X/Y}\\ \xrightarrow{K(X/Y/Z)}Lf^*L_{Y/Z}[1],\end{gathered}
\]
maps to the triangle of the second,
\[
D\to L_{\mathcal B/\mathcal A'}\to L_{X/Y}\xrightarrow{\ w\ }D[1],
\]
by the maps \(\varphi\otimes1\), the functoriality map \(L_{X/Z}\to L_{\mathcal B/\mathcal A'}\), the identity of \(L_{X/Y}\) and \((\varphi\otimes1)[1]\), where \(\varphi\colon L_{\mathcal A/\mathcal Z}\to L_{\mathcal A/\mathcal A'}\) is the functoriality map and \(Lf^*L_{Y/Z}=L_{\mathcal A/\mathcal Z}\otimes_{\mathcal A}\mathcal B\). Hence \(w=(\varphi\otimes1)[1]\circ K(X/Y/Z)\), and
\[
\begin{aligned}&\omega(f,Y')\\&\quad =\bigl(\tilde c\circ(\varphi\otimes1)\bigr)[1]\circ K(X/Y/Z).\end{aligned}
\]
It remains to show \(\tilde c\circ(\varphi\otimes1)=f^*e(Y')\). By definition \(e(Y')=t\circ\psi\), where \(\psi\colon L_{Y/Z}=L_{\mathcal O_Y/g^{-1}\mathcal O_Z}\to L_{\mathcal O_Y/\mathcal O_{Y'}}\) is the functoriality map and \(t\colon L_{\mathcal O_Y/\mathcal O_{Y'}}\to\mathcal J[1]\) the conormal truncation. The complexes \(L_{Y/Z}\) and \(L_{\mathcal O_Y/\mathcal O_{Y'}}\) are K-flat, so \(Lf^*\) of them is \(f^{-1}(-)\otimes_{\mathcal A}\mathcal B\), and \(f^{-1}\psi=\varphi\) because \(f^{-1}\) preserves the polynomial constructions and their functoriality. Hence \(Lf^*(\psi)=\varphi\otimes1\), \(Lf^*L_{\mathcal O_Y/\mathcal O_{Y'}}=D\), and
\[
f^*e(Y')=\tau\circ Lf^*(t)\circ(\varphi\otimes1),
\]
with \(\tau\colon Lf^*\mathcal J[1]\to f^*\mathcal J[1]\) the map inducing the identity on \(H^{-1}\). The maps \(\tilde c\) and \(\tau\circ Lf^*(t)\) go from \(D\in D^{\leq-1}\) to \(f^*\mathcal J[1]\), so by [Tag 06XS] they are equal if they induce the same map on \(H^{-1}\). For \(\tilde c\) it is the identification \(H^{-1}D=f^*H^{-1}(L_{\mathcal O_Y/\mathcal O_{Y'}})=f^*\mathcal J\) of (0.1). For \(\tau\circ Lf^*(t)\) it is \(f^*H^{-1}(t)=f^*(\mathrm{id}_{\mathcal J})\) under the same identification, by the naturality of (0.1) in \(K\). So the two maps are equal. \(\square\)

**Proposition 4.4 (the diagram of a deformed morphism).** Let \(C(u)\) be the category whose objects are those of \(I\) and of \(J\), with \(\operatorname{Hom}(i,i')=\operatorname{Hom}_I(i,i')\), \(\operatorname{Hom}(j,j')=\operatorname{Hom}_J(j,j')\), \(\operatorname{Hom}(i,j)=\operatorname{Hom}_J(u(i),j)\) and \(\operatorname{Hom}(j,i)=\emptyset\), composition being that of \(I\) and \(J\) and \(\beta\circ\alpha=\beta\circ u(\alpha)\) for \(\alpha\colon i'\to i\) in \(I\) and \(\beta\colon u(i)\to j\). Let \(\operatorname{Cyl}(f)\colon C(u)\to(\mathrm{Sch})\) be the diagram with values \(X_i\), \(Y_j\), \(X_\alpha\), \(Y_\gamma\), and \(Y_\beta\circ f_i\colon X_i\to Y_j\) for \(\beta\colon u(i)\to j\). Suppose that \(Y'\) is a deformation of \(Y\) and that \((X',\iota,f')\) is a deformation of \(f\) over \(Y'\). Then \(\operatorname{Cyl}(f')\), with \(\iota\) and \(\iota_Y\), is a deformation of \(\operatorname{Cyl}(f)\). Moreover, for every commutative square of \(C(u)\) whose image under \(\operatorname{Cyl}(f)\) is a cartesian square of schemes, its image under \(\operatorname{Cyl}(f')\) is cartesian.

**Proof.** \(\operatorname{Cyl}(f)\) is a functor because \(Y_{u(\alpha)}f_{i'}=f_iX_\alpha\) for \(\alpha\colon i'\to i\), and so is \(\operatorname{Cyl}(f')\). The thickenings \(\iota_i\) and \(\iota_{Y,j}\) make \(\operatorname{Cyl}(f')\) an extension of \(\operatorname{Cyl}(f)\), whose ideal has the levels \(\mathcal I_i\) and \(\mathcal J_j\). Its structure maps along arrows of \(I\) and of \(J\) are those of \(\mathcal I\) and \(\mathcal J\); along \(\beta\colon u(i)\to j\) it is the composite of \(f_i^*(\mathcal J_\beta)\colon f_i^*Y_\beta^*\mathcal J_j\to f_i^*\mathcal J_{u(i)}\) with the map \(f_i^*\mathcal J_{u(i)}\to\mathcal I_i\) induced by \(f'_i\), by the composition rule of Lemma 3.4 (1). The module \(\mathcal J\) is cartesian, and the isomorphism \(f^*\mathcal J\cong\mathcal I\) is a map of modules, so the structure maps of \(\mathcal I\) are identified with the \(f_{i'}^*(\mathcal J_{u(\alpha)})\), which are isomorphisms. So all structure maps are isomorphisms. For the second statement, the restriction of \(\operatorname{Cyl}(f')\) to a commutative square of \(C(u)\) is an extension of the image square whose ideal is cartesian along all its arrows, that is, a deformation of that square; Corollary 3.7 (2) applies. \(\square\)

## 5. Exercises

**5.1.** Let \(f\colon X\to Y\) be a morphism of diagrams of type \(u\) such that every \(f_i\) is étale. Show that \(L_{X/Y}\) is acyclic. Deduce that for every extension \(Y'\) of \(Y\) with termwise quasi-coherent ideal \(\mathcal J\) there is a deformation of \(f\) over \(Y'\), and that any two are isomorphic by a unique isomorphism.

**5.2.** Let \(p\) be a prime.

(a) Let \(Z'=\operatorname{Spec}\mathbb Z/p^2\), with the first-order thickening \(Z=\operatorname{Spec}\mathbb F_p\to Z'\), and let \(X=X'=\operatorname{Spec}\mathbb F_p\), with \(\iota_X=\mathrm{id}\), \(h=\mathrm{id}\) and \(h'\colon X'\to Z'\) the closed immersion. Show that the square of Definition 3.1 is cartesian, that \(h'\) is not a deformation of \(h\), and that \(\operatorname{Tor}_1^{\mathbb Z/p^2}(\mathbb F_p,\mathbb F_p)\cong\mathbb F_p\).

(b) Show that the faithfulness of \(f^*\) cannot be omitted in Lemma 3.4 (2).

(c) Show that the condition that \(a'\) is a deformation of \(a\) cannot be omitted in Corollary 3.6.

**5.3.** Let \(I=\{0\to1\}\).

(a) Let \(X\) be the diagram \(\operatorname{Spec}\mathbb F_p\to\operatorname{Spec}\mathbb Z\) and \(f\colon X\to\operatorname{Spec}\mathbb Z\) the morphism to the final diagram. Determine the levels and the structure map of \(L_{X/\operatorname{Spec}\mathbb Z}\), and show that it is not quasi-cartesian.

(b) Let \(Y\) be the same diagram \(\operatorname{Spec}\mathbb F_p\to\operatorname{Spec}\mathbb Z\), let \(X\) be the diagram with \(X_i=Y_i\times_{\operatorname{Spec}\mathbb Z}\operatorname{Spec}\mathbb Z[t]\), and \(f\colon X\to Y\) the \(I\)-morphism given by the projections. Show that \(L_{X/Y}\) is quasi-cartesian and that its levels are free modules of rank one in degree \(0\).

## 6. Complete solutions

**5.1.** Let \(i\) be an object of \(I\). Every point of \(X_i\) has an affine open neighbourhood \(U=\operatorname{Spec}B\) mapping into an affine open \(V=\operatorname{Spec}A\) of \(Y_{u(i)}\) with \(A\to B\) étale [Tag 02GI]. By Proposition 10.1 of *The cotangent complex* the restriction of \(L_{X_i/Y_{u(i)}}\) to \(U\) is associated with \(L_{B/A}\), which is \(0\) in \(D(B)\) by its Proposition 5.1. So the cohomology sheaves of \(L_{X_i/Y_{u(i)}}=i^*L_{X/Y}\) vanish (Proposition 1.2 (1)), for every \(i\), and \(L_{X/Y}\) is acyclic. Hence \(\operatorname{Ext}^q(L_{X/Y},f^*\mathcal J)=0\) for every \(q\). By Theorem 4.3, \(\omega(f,Y')=0\), so a deformation exists; its isomorphism classes form a torsor under the zero group, so any two deformations are isomorphic; and every deformation has trivial automorphism group, so if \(h_1\), \(h_2\) are two isomorphisms between deformations, \(h_2^{-1}h_1\) is the identity.

**5.2.** (a) \(Z\times_{Z'}X'=\) \(\operatorname{Spec}(\mathbb F_p\otimes_{\mathbb Z/p^2}\mathbb F_p)=\) \(\operatorname{Spec}\mathbb F_p\) [Tag 01I4], and the map \(X\to Z\times_{Z'}X'\) is the identity: the square is cartesian. The ideal of \(Z\) is \(p\mathbb Z/p^2\mathbb Z\cong\mathbb F_p\) and that of \(X\) is \(0\), so \(h^*\mathcal I_Z=\mathbb F_p\to\mathcal I_X=0\) is not injective and \(h'\) is not a deformation of \(h\). The complex \(\cdots\xrightarrow{p}\mathbb Z/p^2\xrightarrow{p}\mathbb Z/p^2\to\mathbb F_p\to0\) is a free resolution, because the kernel of multiplication by \(p\) on \(\mathbb Z/p^2\) is its image \(p\mathbb Z/p^2\). Tensored with \(\mathbb F_p\) it becomes \(\cdots\xrightarrow{0}\mathbb F_p\xrightarrow{0}\mathbb F_p\), so \(\operatorname{Tor}_1^{\mathbb Z/p^2}(\mathbb F_p,\mathbb F_p)=\mathbb F_p\), in agreement with Lemma 3.2 (2).

(b) In Lemma 3.4 take \(Y=Y'=\operatorname{Spec}\mathbb F_p\), \(Z=\operatorname{Spec}\mathbb F_p\), \(Z'=\operatorname{Spec}\mathbb Z/p^2\), \(g=\mathrm{id}\), \(g'\) the closed immersion, and \(X=X'=\emptyset\). The square formed by \(\iota_Y\), \(\iota_Z\), \(g\), \(g'\) is cartesian by (a), and \(h'\) is a deformation of \(h\), since all modules on the empty scheme are zero. But \(g'\) is not a deformation of \(g\), by (a). Here \(f^*\) is not faithful: it carries the identity and the zero endomorphism of \(\mathcal O_Y\) to the same map.

(c) Take \(X=Y=Z=T=\operatorname{Spec}\mathbb F_p\) with identity maps, a cartesian square; \(Y'=\operatorname{Spec}\mathbb F_p[\epsilon]\), \(\epsilon^2=0\), with \(c'\colon Y'\to T\) the structure morphism; \(X'=X\), \(\iota_X=\mathrm{id}\), \(b'=\mathrm{id}\), and \(a'\colon X'\to Y'\) the closed immersion \(\epsilon\mapsto0\). The conditions of Corollary 3.6 other than the deformation condition hold. The map \(a^*\mathcal I_Y=\mathbb F_p\epsilon\to\mathcal I_X=0\) is not injective, and \(Y'\times_TZ=Y'\) while \(X'=\operatorname{Spec}\mathbb F_p\): the map \(X'\to Y'\times_TZ\) is the closed immersion \(\epsilon\mapsto0\), not an isomorphism, so the square formed by \(a'\), \(b'\), \(c'\), \(d\) is not cartesian.

**5.3.** (a) By Proposition 1.2 (1) the levels are \(L_{\operatorname{Spec}\mathbb Z/\operatorname{Spec}\mathbb Z}=0\) at \(1\) and \(L_{\mathbb F_p/\mathbb Z}\) at \(0\). The quotient \(\mathbb Z\to\mathbb F_p=\mathbb Z/(p)\) is by the nonzerodivisor \(p\), a Koszul-regular sequence, so Lemma 7.1 of *The cotangent complex* gives \(L_{\mathbb F_p/\mathbb Z}\cong(p\mathbb Z/p^2\mathbb Z)[1]\cong\mathbb F_p[1]\). The structure map is \(X_\alpha^*0=0\to\mathbb F_p[1]\), not an isomorphism, so \(L_{X/\operatorname{Spec}\mathbb Z}\) is not quasi-cartesian.

(b) The square formed by \(X_\alpha\colon\operatorname{Spec}\mathbb F_p[t]\to\operatorname{Spec}\mathbb Z[t]\), \(Y_\alpha\) and the projections is cartesian, since \(\mathbb F_p\otimes_{\mathbb Z}\mathbb Z[t]=\mathbb F_p[t]\), and \(f_1\colon\operatorname{Spec}\mathbb Z[t]\to\operatorname{Spec}\mathbb Z\) is flat, \(\mathbb Z[t]\) being a free \(\mathbb Z\)-module. By Proposition 1.4, \(L_{X/Y}\) is quasi-cartesian. Its levels are \(L_{\mathbb Z[t]/\mathbb Z}\) and \(L_{\mathbb F_p[t]/\mathbb F_p}\) (on the affine schemes, by Proposition 10.1 of *The cotangent complex*), which are \(\mathbb Z[t]\,dt\) and \(\mathbb F_p[t]\,dt\) in degree \(0\) by its formula (2.5) for polynomial algebras. The structure map sends \(dt\) to \(dt\).

## Sources

The cotangent complex of a morphism of diagrams of schemes, the classification of extensions and deformations of diagrams, the lemmas on deformations of triangles and squares and the product formula for the obstruction are due to Illusie, in his work on the cotangent complex. The extension and obstruction theorems for ringed topoi used here are proved in the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex).
