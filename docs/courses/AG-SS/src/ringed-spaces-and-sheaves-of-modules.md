# Ringed spaces and sheaves of modules

*Written by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol. Public domain (CC0).*

A geometric space carries a notion of functions. The functions need not be determined by their values: they may retain derivatives or nilpotent information. A ringed space records functions as a sheaf of rings. Its module sheaves then describe objects on which functions act. This lesson explains how modules combine and how they move along a map of spaces.

We use Sheaves on topological spaces, especially sheafification, the stalk criterion and inverse image. The algebraic background is the tensor-product and localization language in Localization, local properties and support. Basic references are [Stacks], [Vakil] and [Module sheaves]. The rings in this lesson are commutative with identity. A local ring is nonzero and has one maximal ideal.

## 1. The rings carried by a space

A **ringed space** is a pair \((X,\mathcal O_X)\) with \(X\) a topological space and \(\mathcal O_X\) a sheaf of rings. A morphism

\[
(f,f^\sharp):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]

consists of a continuous map \(f:X\to Y\) and a sheaf morphism \(f^\sharp:\mathcal O_Y\to f_*\mathcal O_X\). Thus functions on an open subset \(V\) of \(Y\) pull back to functions on \(f^{-1}V\). By the inverse-image adjunction, the same datum is a ring-sheaf map

\[
f^{-1}\mathcal O_Y\longrightarrow\mathcal O_X.
\tag{1.1}
\]

For composable morphisms \(f:X\to Y\), \(g:Y\to Z\), the structure map of the composite is
\(\mathcal O_Z\xrightarrow{g^\sharp}g_*\mathcal O_Y\xrightarrow{g_*f^\sharp}g_*f_*\mathcal O_X\).

A ringed space is **locally ringed** if every stalk \(\mathcal O_{X,x}\) is a local ring. Its unique maximal ideal is \(\mathfrak m_x\); its **residue field** is \(\kappa(x)=\mathcal O_{X,x}/\mathfrak m_x\). A homomorphism \(A\to B\) between local rings is **local** if the inverse image of the maximal ideal of \(B\) is the maximal ideal of \(A\). Equivalently, it sends the maximal ideal of \(A\) into that of \(B\): every element outside the maximal ideal of \(A\) is a unit and hence maps outside the maximal ideal of \(B\).

A morphism of **locally ringed spaces** is a morphism of ringed spaces whose maps
\(\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}\) are local for every \(x\). It then induces a field homomorphism \(\kappa(f(x))\to\kappa(x)\). Composition preserves locality, because inverse images of maximal ideals compose.

**Example 1.1 (smooth functions).** A smooth manifold \(M\) with its sheaf \(\mathcal C^\infty_M\) is locally ringed. Evaluation at \(x\) maps the stalk onto \(\mathbb R\). A germ with nonzero value has a smooth reciprocal on a sufficiently small neighbourhood; a germ with zero value cannot be a unit. Thus the nonunits are exactly the kernel of evaluation, which is the unique maximal ideal. Pullback by a smooth map respects evaluation, so its stalk maps are local. The same argument gives a locally ringed space from continuous real functions on any topological space, or holomorphic functions on a complex manifold.

**Example 1.2 (a constant sheaf of rings).** The stalks of \(R_X\) are \(R\). Consequently, on a nonempty space, \((X,R_X)\) is locally ringed precisely when \(R\) is local. If \(X\) is empty there is no stalk condition to check.

**Example 1.3 (locality is an additional condition).** Fix a prime integer \(p\). The inclusion \(\mathbb Z_{(p)}\to\mathbb Q\) gives a morphism of one-point ringed spaces

\[
(\{*\},\mathbb Q)\longrightarrow(\{*\},\mathbb Z_{(p)}).
\]

Both spaces are locally ringed, but the morphism is not local. The maximal ideal of \(\mathbb Q\) is zero; its inverse image is zero, rather than \(p\mathbb Z_{(p)}\). In geometric terms, the map has inverted an element that was noninvertible at the target point.

**Theorem 1.4 (recognizing an isomorphism).** A morphism of locally ringed spaces is an isomorphism if and only if its underlying map is a homeomorphism and all its stalk maps are isomorphisms.

**Proof.** An isomorphism has both properties. Conversely, use the homeomorphism to identify the two underlying spaces. The structure map becomes a morphism of sheaves of rings on one space. Its stalk maps are isomorphisms, so the stalk criterion gives a sheaf isomorphism. Its inverse, together with the inverse homeomorphism, gives an inverse ringed-space morphism. An isomorphism of local rings identifies their unique maximal ideals, so the inverse maps are local. Thus the inverse is a morphism of locally ringed spaces. \(\square\)

## 2. Bilinear operations require sheafification

An **\(\mathcal O_X\)-module** is a sheaf \(F\) of abelian groups with actions \(\mathcal O_X(U)\times F(U)\to F(U)\) making each \(F(U)\) a module and satisfying \((as)|_V=a|_V\,s|_V\). Morphisms preserve these actions. Each stalk \(F_x\) is an \(\mathcal O_{X,x}\)-module, by multiplying representatives after restricting to a common neighbourhood.

The category \(\operatorname{Mod}(\mathcal O_X)\) is abelian, and exactness is checked on stalks; these facts are [Module sheaves, Theorem 2.1]. We use them without repeating their proof. A direct sum of an arbitrary family of module sheaves is the sheafification of the sectionwise direct sum. In particular, the free module \(\mathcal O_X^{(I)}\) has stalk \(\bigoplus_{i\in I}\mathcal O_{X,x}\). A section of this free module need have only locally finite, rather than globally finite, support in its indices.

For two module sheaves \(F,G\), form the presheaf

\[
T(U)=F(U)\otimes_{\mathcal O_X(U)}G(U).
\tag{2.1}
\]

Restrictions send \(s\otimes t\) to \(s|_V\otimes t|_V\); the change of scalar ring causes no problem because the restrictions are linear over \(\mathcal O_X(U)\to\mathcal O_X(V)\). Define the **tensor product sheaf** \(F\otimes_{\mathcal O_X}G=T^{\#}\).

An \(\mathcal O_X\)-bilinear morphism from \(F,G\) to \(H\) means maps \(F(U)\times G(U)\to H(U)\), bilinear over \(\mathcal O_X(U)\) and compatible with restriction.

**Theorem 2.1 (tensor products).** The tensor product sheaf represents such bilinear morphisms. Its stalks satisfy the natural identity

\[
(F\otimes_{\mathcal O_X}G)_x
\cong F_x\otimes_{\mathcal O_{X,x}}G_x.
\tag{2.2}
\]

Tensor product is associative and symmetric up to its canonical isomorphisms, has unit \(\mathcal O_X\), and is right exact in each variable.

**Proof.** Bilinear maps into \(H(U)\) factor uniquely through (2.1). Their compatibility is exactly the condition that the resulting maps form a presheaf morphism \(T\to H\). The sheafification universal property gives the asserted bijection of maps from \(T^{\#}\) to \(H\).

For (2.2), sheafification does not alter stalks. The map from the stalk of \(T\) sends the germ of \(\sum_j s_j\otimes t_j\) to \(\sum_j(s_j)_x\otimes(t_j)_x\). Every tensor on the right is a finite sum, so its finitely many entries can be represented on one neighbourhood of \(x\), proving surjectivity.

For injectivity, construct tensor products of modules as the free abelian group on pairs, modulo the additive and balancing relations. An equality to zero uses finitely many of these relations and finitely many ring or module elements. Represent all of them on a common neighbourhood. Every equality among the representatives that holds as germs holds after further shrinking; only finitely many equalities are involved. The same finite relation certificate then proves that the sectionwise tensor is zero on that smaller neighbourhood. This proves injectivity even though the ring of scalars varies with the neighbourhood.

The module-level associativity, symmetry and unit maps on sections descend to sheaf maps and are isomorphisms on stalks by (2.2). Hence they are sheaf isomorphisms. A right-exact sequence remains right exact after tensoring on each stalk, because tensor product of ordinary modules is right exact. The stalk exactness criterion proves the sheaf assertion. \(\square\)

**Example 2.2 (why the presheaf in (2.1) can fail).** Let \(X=\mathbb N_{>0}\) with the discrete topology, and \(\mathcal O=k_X\) for a field \(k\). Put \(V=\bigoplus_{j\geq1}ke_j\), and let \(F(U)=G(U)=\prod_{n\in U}V\). These are module sheaves, since a sheaf on a discrete space is a collection of stalks with unrestricted componentwise gluing.

On the singleton \(\{n\}\), choose

\[
t_n=\sum_{j=1}^n e_j\otimes e_j\in V\otimes_kV.
\]

These sections are automatically compatible on the disjoint singleton cover of \(X\). If they came from \(F(X)\otimes_{k^X}G(X)\), that element would be a finite sum of, say, \(r\) pure tensors. Its component at every \(n\) would then be a sum of at most \(r\) pure tensors. But the tensor \(t_n\) has rank \(n\): contraction by the first \(n\) coordinate functionals gives the \(n\) linearly independent vectors \(e_1,\ldots,e_n\), whereas contraction of a sum of \(r\) pure tensors has image in the span of at most \(r\) vectors. Taking \(n>r\) is a contradiction. Sheafification supplies exactly the missing ability to use different finite expressions on different open pieces.

## 3. Hom as a sheaf of local maps

Define the **sheaf Hom** by

\[
\mathcal Hom_{\mathcal O_X}(G,H)(U)
=\operatorname{Hom}_{\mathcal O_U}(G|_U,H|_U).
\tag{3.1}
\]

Its restriction forgets components outside the smaller open set. It is a sheaf: maps on an open cover that agree on overlaps glue uniquely by the morphism-gluing theorem. Addition and the action of a function on the images make it an \(\mathcal O_X\)-module. Notice that (3.1) means maps of sheaves on \(U\), not merely maps \(G(U)\to H(U)\).

Evaluation gives a bilinear sheaf morphism \(\mathcal Hom(G,H)\times G\to H\), and hence a tensor morphism. Evaluation at the section \(1\) gives a sheaf isomorphism \(\mathcal Hom(\mathcal O_X,H)\cong H\); its inverse sends \(h\) to multiplication \(a\mapsto ah\).

**Theorem 3.1 (tensor–Hom adjunction).** There are natural bijections

\[
\operatorname{Hom}_{\mathcal O_X}(F\otimes G,H)
\cong\operatorname{Hom}_{\mathcal O_X}(F,\mathcal Hom(G,H))
\tag{3.2}
\]

and, more strongly, a natural sheaf isomorphism

\[
\mathcal Hom(F\otimes G,H)
\cong\mathcal Hom(F,\mathcal Hom(G,H)).
\tag{3.3}
\]

**Proof.** Let \(b:F\times G\to H\) be bilinear. For \(s\in F(U)\), define a morphism \(G|_U\to H|_U\) whose component on \(V\subset U\) sends \(t\) to \(b_V(s|_V,t)\). These components respect restriction and define an element of (3.1). Sending \(s\) to that element is linear and compatible with restriction, giving the right side of (3.2).

Conversely, for \(c:F\to\mathcal Hom(G,H)\), put \(b_U(s,t)=(c_U(s))_U(t)\). Linearity of \(c\), linearity of each local map, and compatibility with restrictions make \(b\) a bilinear morphism. The two formulas are inverse on every pair of local sections. Apply Theorem 2.1 to obtain (3.2). Perform the same constructions after restriction to every open \(U\); they commute with shrinking \(U\), which proves (3.3). \(\square\)

There is a natural map \(\mathcal Hom(G,H)_x\to\operatorname{Hom}_{\mathcal O_{X,x}}(G_x,H_x)\), but we have not claimed it is always an isomorphism. A germ of a local sheaf map must act on all nearby stalks in a compatible way. An arbitrary map of just one stalk need not extend. Finiteness conditions that make this comparison an isomorphism will be treated in the next lesson.

## 4. Changing the functions as well as the space

Let \((f,f^\sharp):X\to Y\) be a morphism of ringed spaces. For an \(\mathcal O_X\)-module \(F\), the sheaf \(f_*F\) becomes an \(\mathcal O_Y\)-module by

\[
a\cdot s=f^\sharp_V(a)s,
\qquad a\in\mathcal O_Y(V),\quad s\in F(f^{-1}V).
\]

For an \(\mathcal O_Y\)-module \(G\), the inverse image \(f^{-1}G\) is a module over \(f^{-1}\mathcal O_Y\). To make it a module over the actual functions on \(X\), extend scalars through (1.1). This defines the **module pullback**

\[
f^*G=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}G.
\tag{4.1}
\]

The inverse image and module pullback perform different operations. The first moves local information; the second also changes the scalar ring.

**Theorem 4.1 (module pullback and pushforward).** For every morphism of ringed spaces, the following hold naturally.

1. \(f^*\) is left adjoint to \(f_*\) on module sheaves.
2. For \(x\in X\),
   \[
   (f^*G)_x\cong\mathcal O_{X,x}\otimes_{\mathcal O_{Y,f(x)}}G_{f(x)}.
   \tag{4.2}
   \]
3. \(f^*\mathcal O_Y\cong\mathcal O_X\), and
   \(f^*(G\otimes_{\mathcal O_Y}H)\cong f^*G\otimes_{\mathcal O_X}f^*H\).
4. \(f^*\) preserves all small colimits and is right exact. It need not be left exact.
5. If \(g:Y\to Z\), then \((g\circ f)^*\cong f^*g^*\), canonically and compatibly with triple compositions.

**Proof.** First consider any ring-sheaf map \(\mathcal R\to\mathcal S\) on one space. A map \(\mathcal S\otimes_{\mathcal R}M\to N\) of \(\mathcal S\)-modules gives an \(\mathcal R\)-linear map \(M\to N\) by \(m\mapsto1\otimes m\) followed by that map. Conversely, an \(\mathcal R\)-linear map \(b:M\to N\) defines the balanced bilinear rule \(s\otimes m\mapsto s b(m)\). The tensor universal property extends it to a sheaf morphism. These formulas are inverse, proving extension of scalars is left adjoint to restriction of scalars.

Apply this with \(\mathcal R=f^{-1}\mathcal O_Y\), \(\mathcal S=\mathcal O_X\). Then

\[
\begin{aligned}
\operatorname{Hom}_{\mathcal O_X}(f^*G,F)
&\cong\operatorname{Hom}_{f^{-1}\mathcal O_Y}(f^{-1}G,F)\\
&\cong\operatorname{Hom}_{\mathcal O_Y}(G,f_*F).
\end{aligned}
\tag{4.3}
\]

For the second bijection, start with an \(\mathcal O_Y\)-linear map \(b:G\to f_*F\). A local representative \(g\in G(V)\) for \(f^{-1}G\) on \(U\subset f^{-1}V\) maps to \(b_V(g)|_U\). For a scalar represented by \(a\in\mathcal O_Y(V')\), restrict both representatives to \(V\cap V'\). Linearity of \(b\) gives \(b(ag)=f^\sharp(a)b(g)\), so the local rule is \(f^{-1}\mathcal O_Y\)-linear. It respects the colimit identifications and extends by sheafification. Conversely, compose \(G(V)\to f^{-1}G(f^{-1}V)\) with an \(f^{-1}\mathcal O_Y\)-linear map to \(F\). The induced map to \(F(f^{-1}V)\) is \(\mathcal O_Y(V)\)-linear under \(f^\sharp\). Restriction compatibility gives a morphism \(G\to f_*F\). The two constructions are inverse by the explicit adjunction in *Sheaves on topological spaces*, and their linearity checks prove this bijection in the module categories. This proves (1).

Take stalks of (4.1). Theorem 2.1 and the inverse-image stalk formula identify the two scalar rings and the module with those in (4.2), proving (2). For (3), multiplication gives \(\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal O_Y\cong\mathcal O_X\). The tensor comparison is induced by the local rule

\[
(a\otimes g)\otimes(b\otimes h)\longmapsto ab\otimes(g\otimes h).
\]

At a stalk, its inverse sends \(c\otimes(g\otimes h)\) to \((c\otimes g)\otimes(1\otimes h)\). Balancing relations make both formulas well-defined. Thus the comparison is an isomorphism on stalks and hence on sheaves.

For (4), an adjunction gives colimit preservation directly: for a diagram \((G_i)\) and any \(F\), maps from \(f^*(\varinjlim_iG_i)\) to \(F\) are compatible families of maps from \(G_i\) to \(f_*F\), hence compatible maps from \(f^*G_i\) to \(F\). This is the universal property of \(\varinjlim_if^*G_i\). The module categories have these colimits by [Module sheaves, Theorem 3.1]. In particular, cokernels are preserved; additivity then gives right exactness. Alternatively, (4.2) and right exactness of tensor product check it on stalks. Example 5.1 below proves left exactness can fail.

Pushforwards compose, including their scalar actions, because the composite structure map was defined by composing pullbacks of functions. Therefore both \(f^*g^*\) and \((g\circ f)^*\) are left adjoints to \(g_*f_*\). Uniqueness of the adjoint-compatible isomorphism proves (5), with coherence for a triple composition. \(\square\)

The unit of the adjunction is \(G\to f_*f^*G\), locally \(g\mapsto1\otimes g\). The counit \(f^*f_*F\to F\) multiplies functions by the restrictions of sections: \(a\otimes s\mapsto as|_U\) on any open where the representative is defined. These formulas clarify that (4.3) uses the given map of structure sheaves, not merely the underlying continuous map.

If (1.1) is an isomorphism, the extension of scalars in (4.1) does nothing and \(f^*=f^{-1}\) under that identification. For a general morphism the distinction remains. If every stalk \(\mathcal O_{X,x}\) is flat over \(\mathcal O_{Y,f(x)}\), (4.2) shows that \(f^*\) is exact. Flatness is sufficient here; the inverse-image functor itself is exact without that additional hypothesis.

## 5. Open pieces and quotient functions

An **open immersion** of locally ringed spaces identifies its source with an open subset \(U\subset X\) and its structure sheaf with \(\mathcal O_X|_U\). Its pullback is restriction, since both inverse image and the scalar-ring identification are restriction. Conversely, a locally ringed-space map with an open embedding underneath and isomorphisms on the corresponding stalks is an open immersion by the sheaf stalk criterion. The locality condition then follows from the ring isomorphisms.

For closed immersions we use the convention in [Stacks, Tag 01HK]. A module sheaf is **locally generated by sections** if every point has a neighbourhood \(U\) and a family of sections \((s_i)_{i\in I}\) on that same neighbourhood whose germs generate the module at every point of \(U\). The index set may be infinite. Equivalently, on \(U\) there is a surjection \(\mathcal O_U^{(I)}\to F|_U\). This means that local sections can be written as finite linear combinations after shrinking; it does not assert that the map on sections over all of \(U\) is onto.

A **closed immersion** \(i:Z\to X\) of locally ringed spaces is a homeomorphism onto a closed subset for which \(\mathcal O_X\to i_*\mathcal O_Z\) is surjective on stalks and its kernel \(\mathcal I\) is locally generated by sections. This last condition is not a finite-generation condition. Closed subschemes will have quasi-coherent kernels, and their relationship to this definition will be proved when affine schemes are constructed.

The surjective stalk map at \(z\) identifies \(\mathcal O_{Z,z}\) with a quotient of \(\mathcal O_{X,i(z)}\). The ideal is proper, since the quotient is a nonzero local ring. A surjection between local rings is local: the inverse image of the maximal ideal of the quotient is the unique maximal ideal of the source. Thus quotient functions give the required local morphisms.

**Example 5.1 (a closed immersion makes pullback nonexact).** Let \(R=k[\epsilon]/(\epsilon^2)\), with maximal ideal \((\epsilon)\), and consider the map of one-point locally ringed spaces

\[
i:(\{*\},k)\longrightarrow(\{*\},R)
\]

given by the quotient \(R\to k\). It is a closed immersion: the topology is a homeomorphism, the ring map is surjective, and the kernel is generated by the section \(\epsilon\). Modules on these one-point spaces are ordinary modules. Pullback is \(k\otimes_R(-)\).

The inclusion \((\epsilon)\hookrightarrow R\) is injective. But its pullback is

\[
k\otimes_R(\epsilon)\longrightarrow k\otimes_RR=k,
\]

which is the zero map from a nonzero one-dimensional \(k\)-vector space. Indeed, \((\epsilon)\cong k\) as an \(R\)-module, while the included element \(\epsilon\) maps to zero in \(k\). The same underlying continuous map is the identity of a point; its inverse image on abelian sheaves is exact. Only the change of scalar ring has destroyed injectivity.

The more elementary quotient \(\mathbb Z\to\mathbb Z/2\mathbb Z\), considered in [Module sheaves, Example 5], has the same mechanism: the injective map \(\mathbb Z\xrightarrow{2}\mathbb Z\) becomes zero after tensoring with \(\mathbb Z/2\mathbb Z\).

## 6. Exercises

**Exercise 1 (easy).** Prove the stalk tensor identity (2.2) by constructing inverse maps on generators and checking the balancing relation over the stalk ring. Use it to compute the tensor of the two skyscraper modules with values \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/6\mathbb Z\) at one closed point, for the constant structure sheaf \(\mathbb Z_X\).

**Exercise 2 (easy).** Verify the failure of locality in Example 1.3. Contrast it with the quotient \(R\to R/\mathfrak m\) for a local ring \((R,\mathfrak m)\).

**Exercise 3 (medium).** For Example 5.1, compute the pullback of the full exact sequence \(0\to(\epsilon)\to R\to k\to0\). Locate the failure of exactness, and prove directly that module pullback preserves every right-exact sequence.

**Exercise 4 (medium).** Prove that (3.1) is a sheaf by writing its glued map on an arbitrary open subset. Show \(\mathcal Hom(\mathcal O_X,F)\cong F\), as sheaves, rather than just as sets of global sections.

**Exercise 5 (medium).** Construct both directions of (3.2) on local sections, and check that the constructions commute with restriction. Deduce (3.3).

**Exercise 6 (hard).** In Example 2.2, identify the sheafification of the tensor presheaf on every open subset. Show that the presheaf's sections map only to families of tensors of uniformly bounded rank, whereas the sheaf permits arbitrary ranks at the different points. Explain why no finiteness restriction on the open set appears in the sheafified answer.

## 7. Solutions

**Solution 1.** Send \(s_x\otimes t_x\) to the germ of \(s\otimes t\), after choosing representatives on a common neighbourhood. Changing a representative changes nothing after shrinking. An element \(a_x\) of the scalar ring also has a local representative \(a\), and the relation \((as)\otimes t=s\otimes(at)\) holds on that neighbourhood. Thus the rule defines a balanced map from the stalk tensor to the stalk of the presheaf tensor. The reverse map takes germs of sectionwise tensors to tensors of germs. Both composites fix the pure generators, so they are inverse; sheafification preserves that stalk.

For the skyscrapers at a closed point \(x\), their stalks vanish away from \(x\) and are the indicated cyclic groups at \(x\). Their tensor stalk is therefore zero elsewhere and \(\mathbb Z/4\otimes\mathbb Z/6\cong\mathbb Z/2\) at \(x\). To identify the sheaf, multiplication of the two sections on each neighbourhood of \(x\) gives a map from the skyscraper \(\mathbb Z/2\) to the tensor sheaf, which is an isomorphism on all stalks. Closedness matters: it ensures that the original skyscrapers have no nonzero stalks at other points.

**Solution 2.** The inverse image of \((0)\subset\mathbb Q\) under the injection is \((0)\). This is strictly smaller than \((p)\subset\mathbb Z_{(p)}\), since \(p\ne0\). Thus the map is not local. For \(R\to R/\mathfrak m\), the target field has maximal ideal zero and its inverse image is exactly \(\mathfrak m\); the quotient map is local.

**Solution 3.** The pulled-back terms are \(k,k,k\), and the maps are zero followed by the identity: the first is zero by Example 5.1, and the second is the canonical \(k\otimes_RR\to k\otimes_Rk\). The sequence \(k\xrightarrow{0}k\xrightarrow{1}k\to0\) is right exact but cannot be preceded by an injective arrow from the first \(k\). For any right-exact sequence on \(Y\), take stalks at \(f(x)\), tensor over \(\mathcal O_{Y,f(x)}\) with \(\mathcal O_{X,x}\), and use ordinary module right exactness. Formula (4.2) identifies this with the stalk sequence after pullback. Stalkwise exactness proves right exactness of the sheaf sequence.

**Solution 4.** Given compatible morphisms \(b_i:G|_{U_i}\to H|_{U_i}\), and a section \(s\in G(W)\), apply \(b_i\) to \(s|_{W\cap U_i}\). Their images agree on the overlaps, so they glue to a unique section of \(H(W)\). Restricting \(W\) restricts the glued section, by uniqueness. Addition and scalar multiplication commute with this gluing locally and hence globally. This gives the unique sheaf morphism on the union. For \(G=\mathcal O_X\), a morphism on \(U\) is determined by the image \(t\in F(U)\) of \(1\); its component on \(W\subset U\) sends \(a\) to \(a(t|_W)\). These inverse formulas respect restriction in \(U\), proving the sheaf isomorphism.

**Solution 5.** A tensor morphism gives a bilinear rule \(b_U(s,t)\). Associate to \(s\in F(U)\) the local map with component \(t\mapsto b_V(s|_V,t)\) on \(V\subset U\). This is a section of \(\mathcal Hom(G,H)(U)\) and depends linearly on \(s\). Conversely, evaluate the local map associated to \(s\) on \(t\) over \(U\). Bilinearity supplies the unique tensor morphism. The composites return the same values on all pure local tensors and on all sections of the local Hom. Restriction of either formula is the same formula over the smaller open, so the adjunction applies on every \(U\) compatibly and yields (3.3).

**Solution 6.** On a discrete space a sheaf is determined by its values on the singleton basis. The tensor presheaf has value \(V\otimes_kV\) on \(\{n\}\), so its sheafification has
\[
(F\otimes_{\mathcal O}G)(U)=\prod_{n\in U}(V\otimes_kV).
\]
The canonical map from the presheaf sends a finite sum \(\sum_{j=1}^r s_j\otimes t_j\) to its coordinate tensors, each of rank at most \(r\). Conversely, if a family has a uniform bound \(r\) on its ranks, choose at each point an expression with at most \(r\) pure tensors and pad it with zeros. For each \(j\), the chosen first and second factors at every point give sections \(s_j,t_j\in\prod_{n\in U}V\). Their sectionwise tensor maps to the family. Hence the image is exactly the uniformly bounded-rank families. Each tensor at an individual point is finite, but no common bound is imposed by gluing on the singleton cover. That is why the sheafified answer is the full product.

## What this lesson does not prove

The abelian category of module sheaves and stalkwise exactness are Sheaves of modules and their derived categories, Theorem 2.1. The existence and sectionwise-sheafification descriptions of colimits are its Theorem 3.1. Exact inverse image is that lesson's Theorem 4.1, parts (1)–(3). These are already written internal prerequisites. The inverse-image module adjunction, tensor product and all module-pullback assertions taught here have been proved here.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, chapters *Sheaves on Spaces*, *Sheaves of Modules* and *Schemes*: [Tag 0091](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#definition-ringed-space), [Tag 0096](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#lemma-adjoint-pullback-pushforward-modules), [Tag 0098](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#lemma-stalk-pullback-modules), [Tag 01CB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#lemma-stalk-tensor-product), [Tag 01CN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#lemma-internal-hom), [Tag 01HB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#definition-locally-ringed-space), and [Tag 01HK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#definition-closed-immersion-locally-ringed-spaces). Links use the AI Integrated Stacks Project English edition.
- **[Vakil]** Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Sections 2.3, 2.6–2.7 and 7.2–7.3. [Author's book page](https://math.stanford.edu/~vakil/216blog/); [consulted public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf) (personal viewing and downloading only; no redistribution or derivative works).
- **[Module sheaves]** *Sheaves of modules and their derived categories*, in *Derived categories and sheaf operations*, Theorems 2.1, 3.1 and 4.1, and Example 5. Open lesson.
