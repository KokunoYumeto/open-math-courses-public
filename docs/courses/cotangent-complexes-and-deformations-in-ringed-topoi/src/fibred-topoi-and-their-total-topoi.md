# Fibred topoi and their total topoi

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagram of topoi indexed by a small category, for example a morphism of ringed topoi, a diagram of schemes with their étale topoi, or a simplicial object of a topos, is organized as a topos fibred over the index category. Two categories are attached to it. In the *total topos* \(\operatorname{Top}(X)\), an object is a family of objects \(E_i\) with maps from the inverse images \(f^*E_j\) to \(E_i\). In the category \(\operatorname{Top}^{\mathrm o}(X)\), the maps go from \(E_i\) to \(f^*E_j\). Cosimplicial sheaves form a category of the first kind and simplicial sheaves one of the second, and the coefficient systems on a simplicial set are of both kinds. The cohomology of diagrams, and with it the deformation theory of diagrams of ringed topoi and of group schemes, takes place in these categories.

This lesson defines them, computes their limits and colimits, and constructs the adjoints of the functors that restrict to one level. It proves that \(\operatorname{Top}(X)\) is a topos by exhibiting a site for it. The same method proves that \(\operatorname{Top}^{\mathrm o}(X)\) is a topos when the inverse images have left adjoints that preserve fibre products, which holds for diagrams in a topos. Finally, it identifies \(\operatorname{Top}^{\mathrm o}(X)\) for a diagram in a topos with a category of diagrams over it.

**Prerequisites.** Sites, sheaves and topoi in the sense of the Stacks project [[Tag 00VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-site), [Tag 00XA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-topos)]: a topos is a category equivalent to the category of sheaves on a site, and a morphism of topoi \(f\colon X\to Y\) is an adjoint pair \((f^*,f_*)\) with \(f^*\) exact. The comparison lemma [[Stacks, Tag 03A1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-special-equivalence)] and the localization of a topos at an object [[Stacks, Tag 04GZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-localize-topos)].

In a topos, coproducts are disjoint and stable under pullback, epimorphisms are stable under pullback, and a family of morphisms \(\{U_\alpha\to U\}\) is called *surjective* when \(\coprod U_\alpha\to U\) is an epimorphism. The inverse image \(f^*\) of a morphism of topoi preserves colimits, finite limits and surjective families.

## 1. Fibred topoi

**Definition 1.1.** Let \(I\) be a small category. A *topos fibred over \(I\)* consists of

- a topos \(X_i\) for every object \(i\), called the \(i\)-th *level*;
- a morphism of topoi \(X_f=(f^*,f_*)\colon X_i\to X_j\) for every arrow \(f\colon i\to j\);
- isomorphisms of functors \(c_{f,g}\colon f^*g^*\to(gf)^*\) for composable arrows \(i\xrightarrow{f}j\xrightarrow{g}k\), and \(e_i\colon(\mathrm{id}_i)^*\to\mathrm{id}\);

such that for \(i\xrightarrow{f}j\xrightarrow{g}k\xrightarrow{h}l\) the two isomorphisms \(f^*g^*h^*\to(hgf)^*\) obtained from \(c\) agree, \(c_{f,hg}\circ f^*(c_{g,h})=c_{gf,h}\circ c_{f,g}h^*\), and \(c_{\mathrm{id},f}\) and \(c_{f,\mathrm{id}}\) are induced by \(e\).

In formulas below, the isomorphisms \(c\) and \(e\) are inserted wherever two inverse images are composed, and they are not written. Every verification below uses only the two conditions just stated. When \(X_f^*\) has a left adjoint, it is written \(f_!\).

**Examples 1.2.** (a) For \(I=\{0\to1\}\), a fibred topos is a morphism of topoi \(X_0\to X_1\).

(b) The *constant* fibred topos with value a topos \(T\) has \(X_i=T\) and \(X_f=\mathrm{id}\).

(c) *Diagrams in a topos.* Let \(T\) be a topos and \(Y\colon I\to T\) a functor. For \(f\colon i\to j\), the localization morphism \(T/Y(i)\to T/Y(j)\) defined by \(Y(f)\) [Stacks, Tag 04GZ, applied to the topos \(T/Y(j)\) and its object \(Y(f)\colon Y(i)\to Y(j)\)] has inverse image \(V\mapsto V\times_{Y(j)}Y(i)\). Its left adjoint \(f_!\) composes with \(Y(f)\). With the canonical isomorphisms between iterated fibre products, this is a fibred topos \(i\mapsto T/Y(i)\), again written \(Y\).

## 2. The two total categories

**Definition 2.1.** Let \(X\) be a topos fibred over \(I\).

1. An object \(E\) of \(\operatorname{Top}(X)\) is a family of objects \(E_i\in X_i\) with morphisms \(E_f\colon f^*E_j\to E_i\) for \(f\colon i\to j\), such that \(E_{gf}=E_f\circ f^*(E_g)\) for \(i\xrightarrow{f}j\xrightarrow{g}k\) and \(E_{\mathrm{id}_i}=\mathrm{id}\). A morphism \(u\colon E\to E'\) is a family \(u_i\colon E_i\to E'_i\) with \(u_i\circ E_f=E'_f\circ f^*(u_j)\).
2. An object \(E\) of \(\operatorname{Top}^{\mathrm o}(X)\) is a family \(E_i\in X_i\) with morphisms \(E_f\colon E_i\to f^*E_j\), such that \(E_{gf}=f^*(E_g)\circ E_f\) and \(E_{\mathrm{id}}=\mathrm{id}\). Morphisms are families \(u_i\) with \(f^*(u_j)\circ E_f=E'_f\circ u_i\).

The functors \(i^*\colon\operatorname{Top}(X)\to X_i\) and \(i^{\mathrm o*}\colon\operatorname{Top}^{\mathrm o}(X)\to X_i\), \(E\mapsto E_i\), restrict to the \(i\)-th level. An object is *cartesian* if all its maps \(E_f\) are isomorphisms. The fibred topos \(X\) is *good* if every \(f^*\) has a left adjoint \(f_!\). Every \(f^*\) then preserves all small limits; the converse holds by the adjoint functor theorem for topoi, which is not used here.

**Proposition 2.2.** (a) \(\operatorname{Top}(X)\) has all small limits and colimits, computed levelwise. (b) \(\operatorname{Top}^{\mathrm o}(X)\) has all small colimits and finite limits, computed levelwise. If \(X\) is good, it has all small limits, computed levelwise.

**Proof.** (a) Let \(\lambda\mapsto E^\lambda\) be a small diagram. For a colimit, put \(E_i=\varinjlim_\lambda E^\lambda_i\). Since \(f^*\) preserves colimits, \(f^*E_j=\varinjlim f^*E^\lambda_j\), and \(E_f=\varinjlim E^\lambda_f\). For a limit, put \(E_i=\varprojlim E^\lambda_i\), and let \(E_f\) be the composite of the canonical map \(f^*\varprojlim E^\lambda_j\to\varprojlim f^*E^\lambda_j\) with \(\varprojlim E^\lambda_f\). In both cases the conditions on composites follow from those of the \(E^\lambda\) and the naturality of the canonical maps. The universal properties hold levelwise and are compatible with the maps \(E_f\). (b) Here a colimit needs \(\varinjlim E^\lambda_i\to\varinjlim f^*E^\lambda_j\cong f^*\varinjlim E^\lambda_j\), which exists because \(f^*\) preserves colimits. A limit needs \(\varprojlim E^\lambda_i\to\varprojlim f^*E^\lambda_j\cong f^*\varprojlim E^\lambda_j\), which exists when \(f^*\) preserves the limit in question: always for finite limits, and for all small limits when \(X\) is good. \(\square\)

## 3. Adjoints of the level functors

**Proposition 3.1.** Let \(i\in\operatorname{Ob}I\) and \(L\in X_i\).

1. The functor \(i^*\colon\operatorname{Top}(X)\to X_i\) has a left adjoint \(i_!\) and a right adjoint \(i_*\), with
\[
\begin{gathered}i_!(L)_j=\coprod_{f\colon j\to i}f^*L,\\i_*(L)_j=\prod_{f\colon i\to j}f_*L.\end{gathered}
\]
For \(g\colon k\to j\), the map \(i_!(L)_g\colon g^*i_!(L)_j\to i_!(L)_k\) sends the summand \(g^*f^*L\) to the summand \((fg)^*L\). For \(g\colon j\to k\), the component of \(i_*(L)_g\colon g^*i_*(L)_k\to i_*(L)_j\) at \(f\colon i\to j\) is adjoint to the projection \(i_*(L)_k\to(gf)_*L=g_*f_*L\).
2. If \(X\) is good, \(i^{\mathrm o*}\colon\operatorname{Top}^{\mathrm o}(X)\to X_i\) has a left adjoint \(i^{\mathrm o}_!\) and a right adjoint \(i^{\mathrm o}_*\), with
\[
\begin{gathered}i^{\mathrm o}_!(L)_j=\coprod_{f\colon i\to j}f_!L,\\i^{\mathrm o}_*(L)_j=\prod_{f\colon j\to i}f^*L.\end{gathered}
\]
For \(g\colon j\to k\), the component of \(i^{\mathrm o}_!(L)_g\) at \(f\) is the map \(f_!L\to g^*i^{\mathrm o}_!(L)_k\) adjoint to the inclusion \(g_!f_!L=(gf)_!L\to i^{\mathrm o}_!(L)_k\). For \(g\colon k\to j\), the map \(i^{\mathrm o}_*(L)_g\colon i^{\mathrm o}_*(L)_k\to g^*i^{\mathrm o}_*(L)_j\), where \(g^*i^{\mathrm o}_*(L)_j=\prod_{f\colon j\to i}g^*f^*L\), has as component at \(f\) the projection onto the factor \((fg)^*L\).

**Proof.** (1) The conditions on composites for \(i_!(L)\) and \(i_*(L)\) follow from the coherence of \(c\). Let \(E\in\operatorname{Top}(X)\). Given \(\varphi\colon L\to E_i\), define \(i_!(L)\to E\) on the summand \(f^*L\) of level \(j\) by \(E_f\circ f^*\varphi\colon f^*L\to f^*E_i\to E_j\). It is a morphism of \(\operatorname{Top}(X)\) because \(E_{fg}=E_g\circ g^*(E_f)\). Conversely, a morphism \(i_!(L)\to E\) restricts to \(L\to E_i\) on the summand of \(\mathrm{id}_i\), and it is determined by this restriction because of its compatibility with the maps of \(i_!(L)\). This gives \(\operatorname{Hom}(i_!L,E)=\operatorname{Hom}(L,E_i)\). Given \(\psi\colon E_i\to L\), define \(E_j\to i_*(L)_j\) by the components \(E_j\to f_*L\) adjoint to \(\psi\circ E_f\colon f^*E_j\to E_i\to L\). Conversely, the component at \(j=i\), \(f=\mathrm{id}\), is a map \(E_i\to L\). The same verification gives \(\operatorname{Hom}(E,i_*L)=\operatorname{Hom}(E_i,L)\).

(2) The same arguments apply, with \(f_!\) adjoint to \(f^*\). In the formula for \(i^{\mathrm o}_*\), the identification \(g^*\prod_ff^*L=\prod_fg^*f^*L\) uses that \(g^*\) preserves products. \(\square\)

When every \(\operatorname{Hom}(j,i)\) is finite, the formula for \(i^{\mathrm o}_*\) involves only finite products, and it defines a right adjoint without assuming that \(X\) is good.

## 4. The total topoi are topoi

**Lemma 4.1.** Choose sites \(D_i\) with \(X_i=\operatorname{Sh}(D_i)\). There are small full subcategories \(C_i\subseteq X_i\) such that:

1. \(h_U^\#\in C_i\) for every \(U\in D_i\);
2. \(C_i\) contains a chosen fibre product, in \(X_i\), of every diagram \(U\to W\leftarrow V\) in \(C_i\);
3. \(f^*V\in C_i\) for every arrow \(f\colon i\to j\) and every \(V\in C_j\);
4. if \(X\) is good, \(f_!U\in C_j\) for every arrow \(f\colon i\to j\) and every \(U\in C_i\).

With the topology whose coverings are the surjective families, every \(C_i\) is a site, and \(E\mapsto h_E|_{C_i}=\operatorname{Hom}_{X_i}(-,E)|_{C_i}\) is an equivalence \(X_i\to\operatorname{Sh}(C_i)\).

**Proof.** Let \(C^{(0)}_i\) be the set of the \(h_U^\#\), \(U\in D_i\). Given small sets \(C^{(n)}_i\), let \(C^{(n+1)}_i\) consist of \(C^{(n)}_i\), a chosen fibre product of every diagram in \(C^{(n)}_i\), the objects \(f^*V\) for \(f\colon i\to j\) and \(V\in C^{(n)}_j\), and, if \(X\) is good, the objects \(f_!U\) for \(f\colon j\to i\) and \(U\in C^{(n)}_j\). Since \(I\) is small, each \(C^{(n+1)}_i\) is small. The full subcategories on \(C_i=\bigcup_nC^{(n)}_i\) satisfy (1)–(4), because each of the finitely many objects involved in a condition already lies in some \(C^{(n)}\). The last assertion is [Stacks, Tag 03A1]. That lemma gives an equivalence \(g\colon X_i\to\operatorname{Sh}(C_i)\) with \(g^{-1}h_F=F\) for \(F\in C_i\). Hence \(g_*E(F)=\operatorname{Hom}(h_F,g_*E)=\operatorname{Hom}(F,E)\). \(\square\)

**Theorem 4.2.** Let \(C_i\) be as in Lemma 4.1. Let \(\int C\) be the category whose objects are the pairs \((i,U)\) with \(U\in C_i\), and whose morphisms \((i,U)\to(j,V)\) are the pairs \((f,\varphi)\) with \(f\colon i\to j\) and \(\varphi\colon U\to f^*V\). The composite of \((f,\varphi)\) and \((g,\psi)\colon(j,V)\to(k,W)\) is \((gf,f^*(\psi)\circ\varphi)\). Declare a covering of \((i,U)\) to be a family \((f_\alpha,\varphi_\alpha)\colon(i_\alpha,U_\alpha)\to(i,U)\) such that every \(f_\alpha\) is an isomorphism of \(I\) and the maps \((f_\alpha^{-1})^*(\varphi_\alpha)\colon(f_\alpha^{-1})^*U_\alpha\to U\) form a surjective family in \(X_i\). A morphism \((f,\varphi)\colon(i',U')\to(i,U)\) with \(f\) an isomorphism is the composite of the isomorphism \((i',U')\to(i,(f^{-1})^*U')\) given by \(f\) with \((\mathrm{id}_i,(f^{-1})^*\varphi)\), and \((f^{-1})^*U'\in C_i\) by Lemma 4.1 (3). So, up to isomorphism, the coverings of \((i,U)\) are the families \((\mathrm{id}_i,\varphi_\alpha)\colon(i,U_\alpha)\to(i,U)\) with \(\{\varphi_\alpha\}\) surjective. Then \(\int C\) is a site, and
\[
\begin{gathered}E\longmapsto F_E,\\F_E(i,U)=\operatorname{Hom}_{X_i}(U,E_i),\end{gathered}
\]
with \(F_E(f,\varphi)(v)=E_f\circ f^*(v)\circ\varphi\) for \(v\colon V\to E_j\), is an equivalence \(\operatorname{Top}(X)\to\operatorname{Sh}(\int C)\). In particular \(\operatorname{Top}(X)\) is a topos, and \((i^*,i_*)\) is a morphism of topoi \(X_i\to\operatorname{Top}(X)\).

**Proof.** *The site.* Associativity of composition follows from the coherence of \(c\). Isomorphisms are coverings, and coverings of coverings are coverings. Fibre products are invariant under isomorphism, so for stability under base change it suffices to treat a covering of the form \(\{(\mathrm{id}_i,\varphi_\alpha)\colon(i,U_\alpha)\to(i,U)\}\) and a morphism \((f,\varphi)\colon(k,W)\to(i,U)\). Put \(W_\alpha=W\times_{f^*U}f^*U_\alpha\), which lies in \(C_k\) by Lemma 4.1 (2) and (3). We claim that \((k,W_\alpha)\), with \((\mathrm{id},\mathrm{pr}_1)\) and \((f,\mathrm{pr}_2)\), is a fibre product in \(\int C\). A pair of morphisms \((g,\gamma)\colon(l,Z)\to(k,W)\) and \((h,\eta)\colon(l,Z)\to(i,U_\alpha)\) that agree in \((i,U)\) has \(h=fg\), and \(\gamma\) and \(\eta\) agree as maps \(Z\to(fg)^*U=g^*f^*U\). Since \(g^*\) preserves fibre products, such pairs correspond to maps \(Z\to g^*W_\alpha\). The family \(\{W_\alpha\to W\}\) is surjective, because \(f^*\) preserves surjective families and these are stable under pullback. So the coverings are stable under base change, and \(\int C\) is a site [Stacks, Tag 00VH].

*\(F_E\) is a sheaf.* It is a presheaf, by the condition on composites of \(E\). Up to isomorphism, a covering lives in one level \(i\), and so do the fibre products of its members. So the sheaf condition for \(F_E\) at a covering of \((i,U)\) is the sheaf condition for \(h_{E_i}|_{C_i}\), which holds by Lemma 4.1.

*Full faithfulness.* A morphism \(u\colon E\to E'\) gives \(F_u\colon F_E\to F_{E'}\) by composition with the \(u_i\). Conversely, let \(\alpha\colon F_E\to F_{E'}\) be a morphism of sheaves. On level \(i\), it is a morphism \(h_{E_i}|_{C_i}\to h_{E'_i}|_{C_i}\), hence comes from a unique \(u_i\colon E_i\to E'_i\) by Lemma 4.1. Compatibility of \(\alpha\) with \(F(f,\mathrm{id}_{f^*V})\), for \(V\in C_j\) (note \(f^*V\in C_i\)), says \(u_iE_ff^*(v)=E'_ff^*(u_j)f^*(v)\) for all \(v\colon V\to E_j\). The maps \(v\colon V\to E_j\) with \(V\in C_j\) form a surjective family, since \(C_j\) contains the generators \(h_U^\#\), and \(f^*\) preserves surjective families. So \(u_iE_f=E'_ff^*(u_j)\), and \(u\) is a morphism of \(\operatorname{Top}(X)\) with \(F_u=\alpha\).

*Essential surjectivity.* Let \(F\) be a sheaf on \(\int C\). Its restriction to level \(i\), along \(U\mapsto(i,U)\), is a sheaf on \(C_i\), so it is isomorphic to \(h_{E_i}|_{C_i}\) for an object \(E_i\) (Lemma 4.1). Let \(f\colon i\to j\), \(V\in C_j\) and \(v\in F(j,V)=\operatorname{Hom}(V,E_j)\). The elements \(F(f,\varphi)(v)\in F(i,U)\), for \(U\in C_i\) and \(\varphi\colon U\to f^*V\), form a morphism of sheaves \(h_{f^*V}|_{C_i}\to h_{E_i}|_{C_i}\), because \((f,\varphi)\circ(\mathrm{id},\psi)=(f,\varphi\psi)\). So they come from a unique map \(\theta(v)\colon f^*V\to E_i\). The rule \(v\mapsto\theta(v)\) is natural in \(V\in C_j\). So it is a morphism of sheaves on \(C_j\), from \(h_{E_j}|_{C_j}\) to \(V\mapsto\operatorname{Hom}(f^*V,E_i)=\operatorname{Hom}(V,f_*E_i)\), that is, to \(h_{f_*E_i}|_{C_j}\). Hence it comes from a morphism \(E_j\to f_*E_i\), whose adjoint we call \(E_f\colon f^*E_j\to E_i\). The functoriality of \(F\) for composites \((g,\psi)\circ(f,\varphi)\) gives \(E_{gf}=E_f\circ f^*(E_g)\), and \(F(\mathrm{id},\mathrm{id})=\mathrm{id}\) gives \(E_{\mathrm{id}}=\mathrm{id}\). By construction \(F\cong F_E\).

Finally, \(i^*\) has a left and a right adjoint by Proposition 3.1, so it is exact, and \((i^*,i_*)\) is a morphism of topoi. \(\square\)

**Theorem 4.3.** Suppose \(X\) is good and every \(f_!\) preserves fibre products. Let \(C_i\) be as in Lemma 4.1. Let \(\int^{\mathrm o}C\) have objects \((i,U)\) with \(U\in C_i\), and morphisms \((j,V)\to(i,U)\) the pairs \((f,\psi)\) with \(f\colon i\to j\) and \(\psi\colon V\to f_!U\). Composition is through \(g_!f_!=(gf)_!\). The coverings are defined as in Theorem 4.2: up to isomorphism, they are the surjective families inside one level. Then \(\int^{\mathrm o}C\) is a site, and
\[
\begin{gathered}E\longmapsto F^{\mathrm o}_E,\\F^{\mathrm o}_E(i,U)=\operatorname{Hom}_{X_i}(U,E_i),\end{gathered}
\]
with \(F^{\mathrm o}_E(f,\psi)(u)=E^\flat_f\circ f_!(u)\circ\psi\), is an equivalence \(\operatorname{Top}^{\mathrm o}(X)\to\operatorname{Sh}(\int^{\mathrm o}C)\). Here \(E^\flat_f\colon f_!E_i\to E_j\) is adjoint to \(E_f\). In particular \(\operatorname{Top}^{\mathrm o}(X)\) is a topos.

**Proof.** The proof of Theorem 4.2 applies with \(f_!\) in place of \(f^*\) and the direction of the arrows of \(I\) reversed. The fibre product of a covering \(\{(i,U_\alpha)\to(i,U)\}\) with \((f,\psi)\colon(j,V)\to(i,U)\) is \((j,V\times_{f_!U}f_!U_\alpha)\). It lies in \(\int^{\mathrm o}C\) by Lemma 4.1 (2) and (4). It has the universal property because every \(g_!\) preserves fibre products, and the base-changed family is surjective because \(f_!\), a left adjoint, preserves surjective families. In the faithfulness and surjectivity arguments, the surjective families \(\{f_!(u)\colon f_!U\to f_!E_i\}\) replace the families \(\{f^*(v)\}\). \(\square\)

For a good fibred topos whose functors \(f_!\) do not preserve fibre products, the category \(\operatorname{Top}^{\mathrm o}(X)\) is still a topos. The standard proof uses Giraud's characterization of topoi: Proposition 2.2 gives the exactness properties, and Proposition 3.1 gives the generators \(i^{\mathrm o}_!(U)\). That characterization is not proved here, and this lesson uses \(\operatorname{Top}^{\mathrm o}(X)\) as a topos only under the hypothesis of Theorem 4.3.

## 5. Diagrams in a topos

**Proposition 5.1.** Let \(T\) be a topos and \(Y\colon I\to T\) a diagram, with the fibred topos of Example 1.2 (c). Then \(Y\) is good, every \(f_!\) preserves fibre products, and \(\operatorname{Top}^{\mathrm o}(Y)\) is equivalent to the category \(T^I/Y\) of diagrams \(Z\colon I\to T\) with a morphism \(Z\to Y\).

**Proof.** Each \(f^*\) has the left adjoint \(f_!\), composition with \(Y(f)\). Fibre products in \(T/Y(i)\) are computed in \(T\), so \(f_!\) preserves them. An object of \(\operatorname{Top}^{\mathrm o}(Y)\) consists of objects \(E_i\to Y(i)\) and maps \(E_i\to E_j\times_{Y(j)}Y(i)\) over \(Y(i)\). By the universal property of the fibre product, such a map is the same as a map \(E_i\to E_j\) lying over \(Y(f)\). The conditions on composites and identities say that \(i\mapsto E_i\) is a functor and \(E\to Y\) a natural transformation. Morphisms correspond in the same way. \(\square\)

The category \(T^I\) is a topos: if \(T=\operatorname{Sh}(D)\), it is the category of sheaves on \(D\times I^{\mathrm{op}}\) for the topology whose coverings are the families \(\{(U_\alpha,i)\to(U,i)\}\) with identity second component and \(\{U_\alpha\to U\}\) a covering of \(D\). Its localization \(T^I/Y\) is a topos [Stacks, Tag 04GZ]. This gives a second proof that \(\operatorname{Top}^{\mathrm o}(Y)\) is a topos.

**Examples 5.2.** (a) Let \(I=\Delta^{\mathrm{op}}\) and let \(Y\) be the constant simplicial object at the final object \(e\) of \(T\). Then \(T/e=T\), all inverse images are identities, and \(\operatorname{Top}^{\mathrm o}(Y)\) is the category of simplicial objects of \(T\). An object of \(\operatorname{Top}(Y)\) has maps \(E_m\to E_n\) for every arrow \([n]\to[m]\) of \(\Delta^{\mathrm{op}}\), that is, for every increasing map \([m]\to[n]\). So \(\operatorname{Top}(Y)\) is the category of cosimplicial objects of \(T\). The same holds for multisimplicial objects with \(I=(\Delta^{\mathrm{op}})^n\).

(b) Let \(T\) be the category of sets and \(Y=K\) a simplicial set. An object of \(\operatorname{Top}(K)\) is a family of sets \(E_{n,x}\), \(x\in K_n\), with maps \(E_{m,\alpha^*x}\to E_{n,x}\) for every increasing \(\alpha\colon[m]\to[n]\), compatible with composition. This is a functor on the category of simplices \(\Delta/K\), a covariant coefficient system on \(K\). In the same way, \(\operatorname{Top}^{\mathrm o}(K)\) is the category of presheaves on \(\Delta/K\), the contravariant coefficient systems.

(c) For the constant fibred topos with value \(T\) (Example 1.2 (b)), \(\operatorname{Top}(X)\) is the category of functors \(I^{\mathrm{op}}\to T\), and \(\operatorname{Top}^{\mathrm o}(X)\) that of functors \(I\to T\).

## 6. Exercises

**Exercise 6.1.** Let \(f\colon X_0\to X_1\) be a morphism of topoi, viewed as a fibred topos over \(\{0\to1\}\). Describe \(\operatorname{Top}(X)\) and the adjoints \(i_!\), \(i_*\) of Proposition 3.1 for \(i=0,1\).

**Exercise 6.2.** Show that \(i_!\colon X_i\to\operatorname{Top}(X)\) preserves fibre products. Show that it preserves the final object if and only if \(\operatorname{Hom}(j,i)\) has exactly one element for every \(j\).

**Exercise 6.3.** Let \(K\) be a simplicial set and \(L\) a covariant coefficient system on \(K\), viewed as an object of \(\operatorname{Top}(K)\) as in Example 5.2 (b). Show that \(L\) is cartesian if and only if every \(L(\alpha)\) is bijective.

## 7. Complete solutions

**6.1.** An object of \(\operatorname{Top}(X)\) is a triple \((E_0,E_1,E_0'\colon f^*E_1\to E_0)\). For \(L\in X_0\): \(0_!(L)=(L,0_{X_1},f^*0_{X_1}\to L)\), where \(0_{X_1}\) is the initial object, since there is no arrow \(1\to0\); the map is the unique map from the initial object \(f^*0_{X_1}\) of \(X_0\). Also \(0_*(L)=(L,f_*L,f^*f_*L\to L)\), the counit. For \(M\in X_1\): \(1_!(M)=(f^*M,M,\mathrm{id})\), and \(1_*(M)=(e,M,f^*M\to e)\), where \(e\) is the final object of \(X_0\), since the only arrows out of \(1\) are identities.

**6.2.** Coproducts in a topos are disjoint and stable under pullback, so \(\coprod_f\) commutes with fibre products of coproduct diagrams indexed by the same set. Each \(f^*\) preserves fibre products, and fibre products in \(\operatorname{Top}(X)\) are computed levelwise (Proposition 2.2). So \(i_!\) preserves fibre products. The final object of \(\operatorname{Top}(X)\) is \(e_j\) in every level, and \(i_!(e_i)_j=\coprod_{f\colon j\to i}e_j\). This is final exactly when there is exactly one arrow \(j\to i\).

**6.3.** The map \(L_f\) of the object of \(\operatorname{Top}(K)\), for \(f\) the arrow of \(\Delta^{\mathrm{op}}\) given by \(\alpha\colon[m]\to[n]\), consists of the maps \(L(\alpha)\colon E_{m,\alpha^*x}\to E_{n,x}\) for \(x\in K_n\). It is an isomorphism of sets over \(K_n\) exactly when every \(L(\alpha)\) is bijective.

## Sources

Fibred topoi and the total topos were introduced by Grothendieck and Verdier in SGA 4 (Exposé VI). The category \(\operatorname{Top}^{\mathrm o}(X)\), the formulas for the adjoints of the level functors and the description of diagrams in a topos are in Illusie's work on the cotangent complex. The comparison lemma used for the total sites is in the Stacks project, Chapter *Sites and Sheaves*.
