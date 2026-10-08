# Injective modules, flasque sheaves and bounded-below derived functors

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

A global lifting problem can be replaced by an exact complex of sheaves for which global lifting is easy. Injective modules make extensions of maps possible; flasque sheaves make extensions of sections possible. This lesson relates the two ideas and constructs the bounded-below resolutions used to define right derived functors.

The prerequisite is [Sheaves of modules on a ringed space](sheaves-of-modules-on-a-ringed-space.md), especially Theorem 2.1, Theorem 3.1 and Lemmas 5.1–5.2, together with [Complexes, cones and localization](complexes-cones-and-localization.md), Lemmas 1.1–1.2, 2.4, Theorems 3.1, 4.2, 5.1 and Proposition 5.2. We work with left modules over an arbitrary sheaf \(\mathcal O\) of associative unital rings. No separation condition is imposed on the space. Commutativity is unnecessary throughout this lesson.

The construction sources are the Stacks project authors’ *Injectives*, *Derived Categories* and *Cohomology of Sheaves*, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). The flasque extension argument corresponds to Tag 09SY. Spaltenstein’s *Resolutions of unbounded complexes* provides historical background. Source attribution appears in the [course notice](../LICENCE.md).
## 1. Extending maps and extending sections

An object \(I\) of an abelian category is **injective** if each map from a subobject \(M\subset N\) into \(I\) extends to \(N\). Equivalently, the contravariant functor \(\operatorname{Hom}(-,I)\) is exact: surjectivity at \(\operatorname{Hom}(M,I)\) is precisely the extension condition, while exactness at the earlier two terms follows from kernels and cokernels. A sheaf \(F\) is **flasque**, or **flabby**, if every restriction \(F(V)\to F(U)\), for opens \(U\subset V\), is onto. It suffices that every \(F(X)\to F(U)\) be onto, since this map factors through \(F(V)\).

**Lemma 1.1 (injectives are flasque and restrict to injectives).** An injective module sheaf is flasque. Its restriction to any open subset is injective in the module category of that open subset.

**Proof.** For opens \(U\subset V\), Lemma 5.1 of the preceding lesson constructs a monomorphism \(j_{U!}\mathcal O_U\to j_{V!}\mathcal O_V\). Under the isomorphisms \(\operatorname{Hom}(j_{W!}\mathcal O_W,I)=I(W)\), precomposition is restriction \(I(V)\to I(U)\). Injectivity therefore makes this restriction onto. For the second claim, extension by zero is exact and left adjoint to restriction. Consequently

\[
\operatorname{Hom}_{\mathcal O_U}(-,I|_U)
\cong\operatorname{Hom}_{\mathcal O}(j_{U!}(-),I)
\]

is a composite of exact functors. This is the required injectivity. \(\square\)

**Lemma 1.2 (sections lift across a flasque kernel).** Suppose

\[
0\longrightarrow F\longrightarrow G\longrightarrow H\longrightarrow0
\]

is an exact sequence of module sheaves and \(F\) is flasque. For every open \(U\), the sequence \(0\to F(U)\to G(U)\to H(U)\to0\) is exact. If \(G\) is also flasque, then \(H\) is flasque.

**Proof.** Kernels are computed on sections, so only surjectivity on sections requires proof. Fix \(s\in H(U)\). Consider pairs \((V,t)\) where \(V\subset U\) is open and \(t\in G(V)\) maps to \(s|_V\). Order the pairs by extension: \((V,t)\le(V',t')\) if \(V\subset V'\) and \(t'|_V=t\). This is a set, because opens and sections are sets. It is nonempty, containing the zero section on the empty open. A chain of pairs has an upper bound. Take the union of its opens and glue its compatible sections there. Any two chain members are comparable, which gives compatibility on their intersection. The sheaf condition gives the glued section and its uniqueness. Zorn's lemma gives a maximal pair \((V,t)\).

Choose \(x\in U\). The epimorphism of sheaves \(G\to H\) is onto on stalks. Lift the germ of \(s\) at \(x\), represent the lift on an open neighbourhood, and shrink until its image equals \(s\) there. We obtain an open \(W\subset U\) containing \(x\) and a section \(t'\in G(W)\) mapping to \(s|_W\). On \(W\cap V\), the difference \(t'-t\) has zero image in \(H\). Since \(F\) is the kernel sheaf, it is the image of a unique section \(r'\in F(W\cap V)\). Flasqueness extends \(r'\) to \(r\in F(W)\). Replace \(t'\) by \(t'-r\), where \(r\) is mapped into \(G(W)\). Its image in \(H\) is unchanged, and it now agrees with \(t\) on \(W\cap V\). Glue the two sections to a lift of \(s\) on \(W\cup V\). Maximality forces \(W\cup V=V\); thus \(x\in V\). Since \(x\) was arbitrary, \(V=U\). This proves surjectivity.

If \(G\) is flasque, take opens \(U\subset V\) and \(s\in H(U)\). Lift it to \(G(U)\) by the first part. Extend that lift to \(G(V)\), then map it to \(H(V)\). The result restricts to \(s\). Thus \(H\) is flasque. The proof uses neither commutativity of \(\mathcal O\) nor separation of \(X\). \(\square\)

The first assertion needs only the kernel to be flasque. This is useful even when the middle sheaf is not flasque. In particular, an exact sequence beginning with a flasque sheaf has an exact section sequence on every open; an arbitrary exact sheaf sequence need not, as the endpoint quotient in Example 6.2 of the preceding lesson shows.

**Proposition 1.3 (flasque resolutions compute zero higher cohomology of a flasque sheaf).** Suppose module sheaves have enough injectives. Resolve a flasque sheaf \(F\) by injectives,

\[
0\longrightarrow F\longrightarrow I^0\longrightarrow I^1\longrightarrow\cdots.
\]

For every open \(U\), the augmented complex of sections is exact. For every continuous map with a compatible coefficient-ring morphism \(f:X\to Y\), the augmented complex \(0\to f_*F\to f_*I^0\to f_*I^1\to\cdots\) is exact. Consequently \(F\) is acyclic for \(\Gamma(U,-)\) and \(f_*\), once these right derived functors are constructed below.

**Proof.** Set \(F^0=F\) and \(F^{n+1}=\operatorname{coker}(F^n\to I^n)\). The resolution gives short exact sequences \(0\to F^n\to I^n\to F^{n+1}\to0\). By Lemma 1.1, \(I^n\) is flasque. Starting from \(F^0\), Lemma 1.2 inductively makes each \(F^{n+1}\) flasque and makes each of these short exact sequences exact on \(U\). The image of \(I^{n-1}(U)\to I^n(U)\) is therefore \(F^n(U)\), which is also the kernel of the next map. This proves exactness of the section complex.

For an open \(V\subset Y\), apply the same argument to \(U=f^{-1}V\). These section modules are exactly \((f_*I^n)(V)\). Thus the augmented pushforward complex is exact even on every open's sections, and in particular is exact as a complex of sheaves. Applying the later definition \(R^q\Phi(F)=H^q(\Phi(I^\bullet))\) gives zero for \(q>0\) for either functor \(\Phi\). There is no need for a description of higher direct images to prove this consequence, so it does not depend on a later local-description theorem. \(\square\)

The existence assumption in Proposition 1.3 will be discharged by the explicit functorial embedding construction in the next section. Its statement separates an elementary lifting argument from the choice of a resolution. It is not an appeal to an unproved acyclicity theorem.

## 2. Functorial injective embeddings

We now discharge the existence assumption of Proposition 1.3. First we prove an extension test for modules over a ring. Then we construct a functorial embedding using character modules. Choosing injective hulls independently would not supply this functoriality.

**Lemma 2.1 (Baer's criterion).** A left module \(E\) over a ring \(A\) is injective if every \(A\)-linear map from a left ideal of \(A\) to \(E\) extends to \(A\). 
**Proof.** Injectivity immediately gives the stated extension property. Conversely, suppose that property holds. Let \(N\subset M\) be left \(A\)-modules and \(f:N\to E\) linear. Order its extensions \((N',f')\), with \(N\subset N'\subset M\), by restriction. A chain has an upper bound: take the union of its submodules and the compatible union of its maps. Zorn's lemma gives a maximal extension \((N',f')\). If \(x\in M\setminus N'\), put \(J=\{a\in A:ax\in N'\}\). This is a left ideal, and \(a\mapsto f'(ax)\) is a linear map \(J\to E\). By assumption it extends to \(b:A\to E\). Define
\[
f''(n+ax)=f'(n)+b(a)\quad(n\in N',\ a\in A).
\]
If \(n+ax=n'+a'x\), then \((a-a')x=n'-n\), so \(a-a'\in J\) and \(b(a-a')=f'(n'-n)\). Thus the formula is well defined. It is linear and extends \(f'\) to the strictly larger submodule \(N'+Ax\), contradicting maximality. Hence \(N'=M\), and every map from a submodule extends. This is injectivity. Only the usual axiom of choice, in its Zorn form, is used; no existence theorem for injectives is assumed. \(\square\)

**Lemma 2.2 (functorial injective embeddings of modules).** Let \(A\) be a ring. Put \(E_A=\operatorname{Hom}_{\mathbb Z}(A,\mathbb Q/\mathbb Z)\), a left \(A\)-module by \((a\varphi)(b)=\varphi(ba)\). For a left \(A\)-module \(M\) put
\[
I_A(M)=\prod_{\varphi\in\operatorname{Hom}_A(M,E_A)}E_A,\qquad \iota_M(m)=(\varphi(m))_\varphi .
\tag{2.1}
\]
Then \(I_A(M)\) is injective and \(\iota_M\) is injective. For \(u:M\to N\), the formula \(I_A(u)\bigl((y_\varphi)_\varphi\bigr)=(y_{\chi\circ u})_{\chi}\), with \(\chi\) running over \(\operatorname{Hom}_A(N,E_A)\), makes \(I_A\) a functor and \(\iota\) a natural transformation.

**Proof.** \(E_A\) is a left module: \(((aa')\varphi)(b)=\varphi(baa')=(a(a'\varphi))(b)\). The maps
\[
\Phi(\varphi)=\bigl(m\mapsto\varphi(m)(1)\bigr),\qquad \Psi(\psi)=\bigl(m\mapsto(b\mapsto\psi(bm))\bigr)
\]
are inverse bijections between \(\operatorname{Hom}_A(M,E_A)\) and \(\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z)\), natural in \(M\). Here \(\Psi(\psi)\) is \(A\)-linear, since \(\Psi(\psi)(am)(b)=\psi(bam)=(a\,\Psi(\psi)(m))(b)\). The group \(\mathbb Q/\mathbb Z\) is an injective \(\mathbb Z\)-module. To see this, use Baer's criterion (Lemma 2.1): the ideals of \(\mathbb Z\) are the \(n\mathbb Z\). For \(n=0\) there is nothing to extend. For \(n\geq1\), a map \(n\mathbb Z\to\mathbb Q/\mathbb Z\) sending \(n\) to \(q\) extends to \(\mathbb Z\) by sending \(1\) to any \(q'\) with \(nq'=q\), which exists since \(\mathbb Q/\mathbb Z\) is divisible. Exact sequences of \(A\)-modules are exact as groups. So \(\operatorname{Hom}_A(-,E_A)\cong\operatorname{Hom}_{\mathbb Z}(-,\mathbb Q/\mathbb Z)\) is exact, and \(E_A\) is injective. A product of injectives is injective, because \(\operatorname{Hom}(-,\prod E)=\prod\operatorname{Hom}(-,E)\) and products of exact sequences of groups are exact: injectivity and kernels are coordinatewise, and a preimage of each coordinate of a target element can be chosen independently. This last assertion uses choice for a set-indexed family, and concerns groups, not exactness of products of sheaves. So \(I_A(M)\) is injective. If \(m\neq0\), define \(\psi\) on the subgroup \(\mathbb Zm\) by \(\psi(m)=1/n+\mathbb Z\) if \(m\) has finite order \(n\geq2\), and \(\psi(m)=1/2+\mathbb Z\) if \(m\) has infinite order. Extend \(\psi\) to \(M\), as \(\mathbb Q/\mathbb Z\) is injective. Then \(\varphi=\Psi(\psi)\) has \(\varphi(m)(1)=\psi(m)\neq0\), so \(\iota_M(m)\neq0\). Finally \(I_A(u)(\iota_M(m))=(\chi(u(m)))_\chi=\iota_N(u(m))\), and the displayed formula gives \(I_A(vu)=I_A(v)I_A(u)\) and \(I_A(\mathrm{id})=\mathrm{id}\). \(\square\)

**Theorem 2.3 (functorial injective embeddings).** Let \(\mathcal O\) be any sheaf of rings on \(X\). Put
\[
E(F)=\prod_{x\in X}x_*\bigl(I_{\mathcal O_x}(F_x)\bigr),
\]
where \(I_{\mathcal O_x}\) is the functor (2.1) for the ring \(\mathcal O_x\), and let \(\iota_F:F\to E(F)\) have \(x\)-component the morphism that corresponds under (5.2) of the preceding lesson to \(\iota_{F_x}:F_x\to I_{\mathcal O_x}(F_x)\). Then \(E(F)\) is injective, \(\iota_F\) is a monomorphism, and \(E\) is a functor with \(\iota\) natural. So \(\operatorname{Mod}(\mathcal O)\) has enough injectives, with functorial injective embeddings.

*Source:* the Stacks project, [Tag 01DI in its AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/injectives.tex#L498), gives the commutative-ring construction. The full character-module proof here also checks the associative unital-ring generality; proof contributions by GPT-6 Astra at Ultra are edited by GPT-6.1 Sol at Ultra.

**Proof.** Products exist and are computed on sections ([Theorem 3.1 of the preceding lesson](sheaves-of-modules-on-a-ringed-space.md#3-limits-colimits-stalks-and-sections-of-sums)(1)), and a product of injectives is injective, as in the proof of Lemma 2.2. Each factor is injective: for an injective stalk module J, the adjunction of Lemma 5.2 of the preceding lesson identifies Hom(-, x_*J) with Hom over the stalk ring from the exact stalk functor into J. This is an exact contravariant functor. A product of injective sheaves is injective because its Hom functor is the product of their exact group-valued Hom functors; coordinatewise preimages prove surjectivity. Thus no assertion that products of sheaves are exact is needed. Explicitly, \(\iota_F\) sends \(s\in F(V)\) to \((\iota_{F_x}(s_x))_{x\in V}\). If this is zero, each \(s_x=0\), as \(\iota_{F_x}\) is injective, so \(s=0\). Kernels are computed on sections ([Theorem 2.1 of the preceding lesson](sheaves-of-modules-on-a-ringed-space.md#2-the-abelian-category-of-module-sheaves)(1)), so \(\iota_F\) is a monomorphism. For \(u:F\to G\) put \(E(u)=\prod_xx_*(I_{\mathcal O_x}(u_x))\). Naturality of \(\iota\) holds factor by factor, by Lemma 2.2. \(\square\)


The construction gives an injective embedding, not an injective hull. For example, over the field with two elements, the character module of the ring has two elements. For the one-dimensional module, there are two linear maps into that character module, including the zero map. The indicated product is two-dimensional, and evaluation embeds the original one-dimensional module into it. A different one-dimensional subspace has zero intersection with the embedded image. Thus the embedding is not essential, while a hull would require essentiality. The functorial construction is useful precisely without a claim of minimality.

The embedding functor need not be additive in the morphism variable. Its product coordinates are indexed by all maps into a fixed injective cogenerator, and a module map changes coordinates by precomposition. Identities, composition and naturality of the embedding hold by the explicit formula. The later passage to derived functors uses comparison maps unique up to chain homotopy, not additivity of this embedding functor.

## 3. Complexes that admit comparison maps

A complex \(I\) is **K-injective** if every chain map \(A\to I\) from an acyclic complex is null-homotopic. Equivalently, \(\operatorname{Hom}^{\bullet}(A,I)\) is acyclic for every acyclic \(A\): by Lemma 1.1 of the common reading, its degree-\(r\) cohomology is \(\operatorname{Hom}_K(A,I[r])\), and shifting the acyclic source gives the equivalence. This definition concerns a complex, not just its individual terms.

**Lemma 3.1 (closure properties).** Shifts, cones of maps between K-injectives, homotopy-equivalent complexes and degreewise products of K-injective complexes are K-injective, whenever the indicated products exist.

**Proof.** Shifting the source in (1.2) of the common reading proves the shift assertion. For a map \(I\to J\), the covariant Hom-cone identity of its Lemma 2.4 identifies \(\operatorname{Hom}^{\bullet}(A,C(I\to J))\) with the cone of a map between two acyclic group complexes. It is therefore acyclic. A homotopy equivalence induces inverse maps up to homotopy after applying Hom, so it preserves the condition. Finally,

\[
\operatorname{Hom}^{\bullet}\left(A,\prod_\lambda I_\lambda\right)
\cong\prod_\lambda\operatorname{Hom}^{\bullet}(A,I_\lambda).
\]

Products of exact sequences of groups are exact by coordinatewise lifting and choice, as proved in Lemma 2.2. The product on the right is consequently acyclic. This uses exactness of products of groups, and does not presume that products of module sheaves are exact. \(\square\)

**Lemma 3.2 (bounded-below complexes of injectives are K-injective).** Let \(I\) be a complex of injectives with \(I^n=0\) for \(n<a\), and let \(A\) be acyclic. Then every chain map \(f:A\to I\) is null-homotopic.

**Proof.** We build maps \(s^n:A^n\to I^{n-1}\) with
\[
f^n=d\,s^n+s^{n+1}d\qquad\text{for all }n .
\tag{3.1}
\]
Put \(s^n=0\) for \(n\leq a\). Then (3.1) holds for \(n<a\), where both sides are \(0\). Suppose \(s^k\) is built for \(k\leq n\) and (3.1) holds for all indices below \(n\). Put \(g=f^n-d\,s^n:A^n\to I^n\). Using (3.1) at \(n-1\), and \(d^2=0\),
\[
g\,d=f^nd-d\,s^nd=d\,f^{n-1}-d\bigl(f^{n-1}-d\,s^{n-1}\bigr)=0 .
\]
So \(g\) vanishes on the image of \(d:A^{n-1}\to A^n\). As \(A\) is acyclic, that image is the kernel of \(d:A^n\to A^{n+1}\). Thus \(g\) factors uniquely through the epimorphism from \(A^n\) onto \(\operatorname{im}d\), giving a map from that subobject of \(A^{n+1}\) to \(I^n\). Since \(I^n\) is injective, the factored map extends to \(s^{n+1}:A^{n+1}\to I^n\). Then \(s^{n+1}d=g\), which is (3.1) at \(n\). \(\square\)

The induction needs a lower bound. An acyclic K-injective complex is contractible, since its own identity is one of the maps to which the defining vanishing condition applies. A termwise injective complex without a lower bound need not have this property; the singular-ring example below gives a counterexample.

**Theorem 3.3 (maps into a K-injective complex).** For a K-injective \(I\), a quasi-isomorphism \(s:M\to N\) induces a bijection
\[
s^*:\operatorname{Hom}_{K(\mathcal A)}(N,I)
\longrightarrow\operatorname{Hom}_{K(\mathcal A)}(M,I).
\]
Consequently the natural map from either homotopy-category Hom group to the corresponding derived-category Hom group with target \(I\) is bijective. 

**Proof.** The complex \(\operatorname{Hom}^\bullet(A,I)\) is acyclic when \(A\) is acyclic: its degree-\(r\) cohomology is \(\operatorname{Hom}_{K(\mathcal A)}(A,I[r])\), which vanishes because a shift of \(A\) is again acyclic. Put \(U=\operatorname{Hom}^\bullet(N,I)\), \(V=\operatorname{Hom}^\bullet(M,I)\), and \(u=s^*:U\to V\). In degree \(r\), write a map out of \(\operatorname{Cone}(s)\) as \((a,b)\in U^r\oplus V^{r-1}\). Its differential is
\[
(a,b)\longmapsto (d_Ua,\ d_Vb+(-1)^{r+1}u(a)).
\]
Thus \((a,b)\mapsto((-1)^{r-1}b,a)\) is a chain isomorphism onto \(\operatorname{Cone}(u)[-1]\): its differential is \((v,a)\mapsto(-d_Vv-u(a),d_Ua)\). This explicitly identifies the Hom complex out of \(\operatorname{Cone}(s)\) with the shifted cone of
\[
\operatorname{Hom}^\bullet(N,I)\longrightarrow
\operatorname{Hom}^\bullet(M,I).
\]
The cone of \(s\) is acyclic. Thus this map of Hom complexes is a quasi-isomorphism; its degree-zero cohomology gives the displayed bijection.

Here is a direct use of the localization universal property that avoids assuming a choice of roofs. The contravariant functor \(H(L)=\operatorname{Hom}_K(L,I)\) sends every quasi-isomorphism to an isomorphism by the first paragraph, so it factors through \(D(\mathcal A)^{\mathrm{op}}\). For \(v:L\to I\) in \(D\), apply this factored functor to \(v\) and to the element \(1_I\); this gives an element of \(\operatorname{Hom}_K(L,I)\). The resulting map is inverse to the natural map into \(\operatorname{Hom}_D(L,I)\): one composite fixes every chain-homotopy class, and the other is a natural endomorphism of the representable functor \(\operatorname{Hom}_D(-,I)\) fixing \(1_I\). Naturality for inverted quasi-isomorphisms follows by inverting their naturality squares. Every derived morphism is generated by ordinary morphisms and these inverses, so the second composite fixes all morphisms too. \(\square\)

**Corollary 3.4 (the full characterization).** For a complex \(I\), the following are equivalent: it is K-injective; \(\operatorname{Hom}_K(A,I)=0\) for every acyclic \(A\); every quasi-isomorphism into the source induces a bijection on homotopy classes of maps to \(I\); the natural map \(\operatorname{Hom}_K(L,I)\to\operatorname{Hom}_D(L,I)\) is bijective for every \(L\).

**Proof.** The first two conditions are the definition. Theorem 3.3 proves the third and fourth from them. Conversely, the third condition applied to \(0\to A\) makes \(\operatorname{Hom}_K(A,I)=0\). The fourth does too, since any acyclic \(A\) becomes a zero object in \(D\) by the quasi-isomorphism \(0\to A\). Thus all conditions are equivalent. A quasi-isomorphism between K-injectives is a homotopy equivalence: the third condition supplies an inverse on one side, and its injectivity forces the other composite to be the identity. \(\square\)

## 4. Right derived functors on bounded-below complexes

For an additive functor \(\Phi\), applying it degreewise gives a functor on homotopy categories, but it need not preserve quasi-isomorphisms. We seek \(R\Phi:D^+(\mathcal A)\to D^+(\mathcal B)\) with a comparison on \(K^+(\mathcal A)\). Its **right-derived universal property** is this: every natural comparison \(\Phi\to T\circ Q\), with \(T\) a functor on \(D^+(\mathcal A)\), factors uniquely as \(\Phi\to R\Phi\circ Q\to T\circ Q\). This makes \(R\Phi\) the initial comparison out of \(\Phi\).

**Theorem 4.1.** Let \(\mathcal A\) and \(\mathcal B\) be abelian, and assume that every object of \(\mathcal A\) embeds in an injective object. Let \(\Phi:\mathcal A\to\mathcal B\) be additive.

1. Every bounded-below complex \(K\) has a qis \(K\to I\) into a bounded-below complex of injectives. If \(K^n=0\) for \(n<a\), it can be chosen injective in each degree, with \(I^n=0\) for \(n<a\).
2. Such an \(I\) is K-injective (Lemma 3.2). Hence \(\operatorname{Hom}_{K(\mathcal A)}(L,I)=\operatorname{Hom}_{D(\mathcal A)}(L,I)\) for every \(L\). A morphism into \(I\) extends along a qis, uniquely up to homotopy.
3. The rule \(R\Phi(K)=\Phi(I)\) gives a triangulated functor \(D^+(\mathcal A)\to D^+(\mathcal B)\), and this functor is the right derived functor \(R\Phi\). If \(\Phi\) is left exact, \(R^0\Phi=\Phi\) and \((R^i\Phi)_i\) is a universal \(\delta\)-functor.
4. (Leray) If \(\Phi\) is left exact and \(J\) is a bounded-below complex with \(R^i\Phi(J^n)=0\) for all \(i>0\) and all \(n\), then \(\Phi(J)\to R\Phi(J)\) is an isomorphism. Left exactness cannot be dropped. For a general additive \(\Phi\), the terms must also satisfy \(\Phi(J^n)\cong R^0\Phi(J^n)\), which holds by (3) when \(\Phi\) is left exact. For \(\Phi=-\otimes_{\mathbb Z}\mathbb Z/2\) on \(\operatorname{Mod}(\mathbb Z)\) and \(J=\mathbb Z\) in degree \(0\), the injective resolution \(\mathbb Q\to\mathbb Q/\mathbb Z\) gives \(R\Phi(\mathbb Z)=0\), because \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are divisible, while \(\Phi(\mathbb Z)=\mathbb Z/2\).
5. For \(\mathcal A=\operatorname{Mod}(\mathcal O)\), with \(\mathcal O\) any sheaf of rings, (1)–(4) hold by Theorem 2.3. This gives \(Rf_*\), \(R\Gamma(U,-)\), and \(R\operatorname{Hom}_{\mathcal O}(G,-)\) on \(D^+\). The support functor is treated in *Sections with support and the localization triangle*.

We have proved the comparison assertion in Section 3. We now construct resolutions and establish the derived-functor properties. The localization, triangulated structure and cohomology exact sequences used in these proofs are Theorems 3.1, 4.2, 5.1 and Lemma 1.2 of *Complexes, cones and localization*. The full proofs of [injective resolutions](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex#L6630), [K-injective comparison](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex#L9987) and [acyclic terms](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex#L6075) in AI Integrated Stacks Project are proof sources. The explicit construction and expanded checks are by GPT-6 Astra at Ultra, checked and edited by GPT-6.1 Sol at Ultra.

### Constructing the resolution one degree at a time

**Proof of Theorem 4.1(1).** The elementary operation is to replace one term of a complex by an injective object. Suppose \(C\) is a complex and choose a monomorphism \(u:C^n\to E\), with \(E\) injective. Form the pushout
\[
P=(E\oplus C^{n+1})/\operatorname{im}(u,-d_C^n).
\]
Replace \(C^n\) by \(E\) and \(C^{n+1}\) by \(P\). The incoming differential is \(u d_C^{n-1}\), the new differential \(E\to P\) sends \(e\) to \([e,0]\), and the outgoing differential sends \([e,c]\) to \(d_C^{n+1}c\). These maps square to zero: \([u(c),0]=[0,d_Cc]\), and \(d_C^2=0\). This gives a complex \(C'\) and a chain map \(C\to C'\).

The map \(C^{n+1}\to P\) is a monomorphism. Indeed, the pullback of the monomorphism \((u,-d_C):C^n\to E\oplus C^{n+1}\) along the second-summand inclusion is zero, because its projection to \(E\) has kernel \(\ker u=0\). Thus that summand has zero intersection with the subobject being quotiented. This is an argument by kernels and pullbacks in an arbitrary abelian category. The map of complexes is termwise monic. Quotienting in degree \(n+1\) also by the image of \(C^{n+1}\) leaves \(E/u(C^n)\). The induced differential from degree \(n\) is the identity of that quotient. Consequently the quotient complex is
\[
E/u(C^n)\ \xrightarrow{\ 1\ }\ E/u(C^n)
\]
in degrees \(n,n+1\), and zero in other degrees. It is contractible, so the cohomology exact sequence proves that \(C\to C'\) is a quasi-isomorphism.

Start at \(n=a\), then perform the operation at \(a+1,a+2,\ldots\). Once degree \(n\) has been replaced, later operations leave that object unchanged; once degree \(n+1\) has been replaced, the differential out of degree \(n\) is unchanged as well. Define \(I\) using these eventual objects and differentials. This uses no infinite colimit in \(\mathcal A\): each degree is defined at a finite stage. All its terms are injective, it is zero below \(a\), and the map \(K\to I\) is termwise monic. For fixed \(r\), the three terms and two differentials computing \(H^r\) have stabilized after finitely many steps. Every step was a quasi-isomorphism, so \(H^r(K)\to H^r(I)\) is an isomorphism. This proves (1). \(\square\)

### Comparison, triangulation and universality

**Proof of Theorem 4.1(2)–(3).** Choose a resolution \(q_K:K\to I_K\). Use part (1). A chain map \(f:K\to L\) has a unique homotopy-class extension \(\bar f:I_K\to I_L\) satisfying \(\bar f q_K=q_L f\) in \(K(\mathcal A)\), by Theorem 3.3. Uniqueness proves compatibility with composition and identities. If \(f\) is a quasi-isomorphism, \(\bar f\) is one too. A quasi-isomorphism between K-injectives is a homotopy equivalence: apply Theorem 3.3 first to obtain a left inverse and again to show the other composite is the identity.

An additive \(\Phi\) preserves chain homotopies, shifts and mapping cones, since these involve only finite direct sums, differentials and sums of maps. Therefore \(\Phi(\bar f)\) is invertible in \(K(\mathcal B)\) whenever \(\bar f\) is a homotopy equivalence. The assignment consequently factors through the localization of \(K^+(\mathcal A)\). This localization identifies with the full \(D^+(\mathcal A)\): Proposition 5.2 of the common reading gives its bounded-below representatives, while Theorem 3.3 applied both in \(K^+\) and in \(K\) computes all maps between such representatives by the same maps into their bounded-below injective resolutions. Thus inclusion is fully faithful as well as essentially surjective. All images lie in \(D^+(\mathcal B)\). Different choices of \(I_K\) give a unique natural comparison isomorphism: extend the identity between resolutions and apply the preceding argument. These comparisons satisfy the cocycle identity by uniqueness.

The functor is additive because the unique extension of \(f+g\) is the sum of the unique extensions of \(f\) and \(g\). It is triangulated as follows. A triangle in \(D^+\) is an image of a cone triangle up to isomorphism, by Theorem 5.1 of the common reading. Replace its first two objects by bounded-below injective resolutions. Theorem 3.3 extends its first map, and Lemma 2.1 of the common reading compares its cone with the cone of the extended map. The comparison is a quasi-isomorphism by the cohomology exact sequences. Shifts and cones of K-injectives are K-injective by Lemma 3.1, and those resolutions' cones remain bounded below with injective terms, since finite sums of injectives are injective. Thus the triangle can be computed by this triangle of resolutions. Applying \(\Phi\) preserves its cone and shift, proving the claim.

We verify the stated universal property. Applying \(\Phi\) to \(q_K\) gives a natural comparison
\(\eta_K:\Phi(K)\to R\Phi(K)\) in \(D(\mathcal B)\).
If \(T:D^+(\mathcal A)\to D^+(\mathcal B)\) is another functor with a natural map \(\theta_K:\Phi(K)\to T(K)\) on \(K^+(\mathcal A)\), the only possible induced map \(R\Phi(K)\to T(K)\) is
\[
\Phi(I_K)\xrightarrow{\theta_{I_K}}T(I_K)
\xrightarrow{T(q_K)^{-1}}T(K).
\]
It is natural by the comparison equation for \(\bar f\), it composes with \(\eta\) to \(\theta\), and it is forced by that equation at \(q_K\). To see uniqueness explicitly, at a K-injective resolution we may use the identity as its resolution, so the comparison there is the identity. Naturality at \(q_K\) then forces the displayed formula. The result is independent of that choice by the unique resolution comparison. This is the right-derived-functor property.

Define \(R^i\Phi(M)=H^i(R\Phi(M[0]))\). If \(\Phi\) is left exact, the initial exact sequence \(0\to M\to I^0\to I^1\) gives \(R^0\Phi(M)=\Phi(M)\). The resolution has no negative terms, so \(R^i\Phi=0\) for \(i<0\). Short exact sequences give distinguished triangles by Proposition 5.2 of the common reading. Their images under \(R\Phi\) give natural long exact cohomology sequences. Thus the nonnegative functors \(R^i\Phi\), with these connecting maps, form a cohomological \(\delta\)-functor. Universality means that a natural transformation in degree zero into any other such \(\delta\)-functor extends uniquely to every degree, commuting with all connecting maps.

Here are the details of universality of that \(\delta\)-functor. Each monomorphism \(M\to E\) into an injective kills \(R^i\Phi(M)\) after mapping to \(R^i\Phi(E)\) for \(i>0\), because \(E[0]\) is already a resolution. Let \(T^i\) be any other cohomological \(\delta\)-functor and choose a natural map \(R^0\Phi\to T^0\). In \(0\to M\to E\to C\to0\), exactness says that
\[
R^0\Phi(C)\longrightarrow R^1\Phi(M)
\quad\text{is onto},\qquad
R^{i-1}\Phi(C)\xrightarrow{\ \sim\ }R^i\Phi(M)\quad(i>1).
\]
For \(i=1\), compose the chosen degree-zero map at \(C\) with the boundary into \(T^1(M)\). This vanishes on the image of \(R^0\Phi(E)\), by naturality and exactness of \(T\), so it descends uniquely. Inductively, compose the degree-\((i-1)\) map at \(C\) with the boundary into \(T^i(M)\) and the inverse of the displayed isomorphism. Given a map \(M\to M'\), extend its composite into an injective containing \(M'\) across \(M\to E\); this gives a morphism of the two short exact sequences. Induction and naturality of boundary maps prove naturality of the constructed degree-\(i\) map. Two embeddings of the same \(M\) are compared with their diagonal embedding into the finite sum of the two injectives. The same argument proves independence of the embedding. Compatibility with arbitrary connecting maps follows by embedding the middle term of a short exact sequence into an injective and using the induced diagram of cokernels; the defining construction is precisely the connecting-map square in that diagram. Finally the displayed surjection and isomorphisms force every degree of any extension. Thus the extension exists uniquely as a morphism of \(\delta\)-functors. This proves universality. \(\square\)

### Why acyclic terms suffice in the bounded-below case

In the universality argument above, compatibility with an arbitrary boundary can be checked without any further resolution theorem. For \(0\to M\to N\to P\to0\), embed \(N\) in an injective \(E\) and put \(C=E/M\). The identity on \(M\), the embedding \(N\to E\), and the induced map \(P\to C\) give a morphism to \(0\to M\to E\to C\to0\). Naturality of each \(\delta\)-functor gives
\[
\delta_{M,N,P}^i=\delta_{M,E,C}^i\circ R^i\Phi(P\to C),
\]
and the same formula for \(T\). The constructed maps commute with the second boundary by their definition and with \(P\to C\) by their established naturality. They therefore commute with the first boundary as well.

**Proof of Theorem 4.1(4)–(5).** Call an object \(A\) right \(\Phi\)-acyclic when the comparison \(\Phi(A)[0]\to R\Phi(A[0])\) is an isomorphism. For left exact \(\Phi\), part (3) shows that this is equivalent to \(R^i\Phi(A)=0\) for \(i>0\). For a general additive functor the degree-zero comparison must additionally be an isomorphism, as the statement requires.

First let \(J\) have only finitely many nonzero terms, all right \(\Phi\)-acyclic. Remove its bottom term using the degreewise split sequence
\[
0\longrightarrow \sigma_{\ge a+1}J\longrightarrow J
\longrightarrow J^a[-a]\longrightarrow0,
\]
where \(\sigma\) denotes brutal truncation, with the indicated boundary differential set to zero. Applying \(\Phi\) still gives a degreewise split exact sequence. The associated cone triangles and the natural comparison with \(R\Phi\) show, by induction on the number of terms and the cohomology exact sequences, that \(\Phi(J)\to R\Phi(J)\) is an isomorphism.

For a bounded-below \(J\), fix an integer \(r\) and use
\[
0\longrightarrow \sigma_{\ge r+2}J\longrightarrow J
\longrightarrow \sigma_{\le r+1}J\longrightarrow0.
\]
The last complex is bounded. The first, and also its image under \(\Phi\), vanish in degrees below \(r+2\). By (1) it has an injective resolution vanishing below \(r+2\), so its derived image also has no cohomology below \(r+2\). The two long exact sequences therefore identify degree-\(r\) cohomology of both middle terms with that of the bounded last terms. The already proved bounded case gives the desired isomorphism in degree \(r\). This holds for every \(r\), proving (4). Part (5) now follows by applying the construction with the injective embeddings of Theorem 2.3. No countability, commutativity, spectral sequence, or exactness of infinite products of sheaves was used. \(\square\)

## 5. Examples: ordinary, flasque and unbounded resolutions

On a one-point space with coefficient ring \(R\), sheaves are simply \(R\)-modules. Theorem 2.3 reduces to the character-module product of Lemma 2.2. It is a functorial injective embedding. It is not generally a hull, as the example over the field with two elements in Section 2 demonstrates. For \(R=\mathbb Z\), an ordinary injective resolution of \(\mathbb Z\) is

\[
0\longrightarrow\mathbb Z\longrightarrow\mathbb Q
\longrightarrow\mathbb Q/\mathbb Z\longrightarrow0.
\]

Both nonzero resolution terms are divisible, and Baer's criterion makes them injective. Thus, for \(\Phi=\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,-)\), the degree-zero term after applying \(\Phi\) is zero and the degree-one term is the subgroup of \(\mathbb Q/\mathbb Z\) killed by \(n\). It is cyclic of order \(n\), by the map \(1\mapsto 1/n+\mathbb Z\). Hence \(R^1\Phi(\mathbb Z)=\mathbb Z/n\) and all other nonnegative derived values vanish. The right derived functor detects the extension information absent from the original Hom group.

For a different additive functor, \(\Phi=-\otimes_{\mathbb Z}\mathbb Z/2\), the same resolution has zero image: a divisible group has zero quotient by twice itself. Thus its right derived value at \(\mathbb Z[0]\) is zero, although \(\Phi(\mathbb Z)=\mathbb Z/2\). This is precisely why higher vanishing alone does not define right acyclicity for a general additive functor. Later, left resolutions will give the derived tensor functor appropriate to tensor's right exactness.

The constant sheaf \(\underline{\mathbb Z}\) on \([0,1]\) is not flasque. On the disconnected open \((0,1/3)\cup(2/3,1)\), the section with value zero on the first component and one on the second cannot extend to a locally constant function on the connected interval. There is nevertheless a direct flasque resolution. Put

\[
C^0(F)=\prod_{x\in X}x_*F_x.
\]

Its sections on \(U\) are \(\prod_{x\in U}F_x\). Restriction forgets coordinates, so it is onto: fill missing coordinates with zero. These sections form a sheaf because compatible families glue coordinate by coordinate. The germ map \(F\to C^0(F)\) is monic by the stalk criterion. Let \(F^1\) be its cokernel, form \(C^0(F^1)\), and continue with successive cokernels. The resulting augmented complex

\[
0\to F\to C^0(F)\to C^0(F^1)\to C^0(F^2)\to\cdots
\]

is exact by its construction, and all its resolution terms are flasque. It is the Godement flasque resolution. Proposition 1.3 and Theorem 4.1(4) show that its section or pushforward complex computes the corresponding derived functor. Its terms need not be injective; acyclicity suffices because the resolution is bounded below.

An unbounded K-injective example goes in the other direction. On a point, put

\[
I=\prod_{m\ge0}(\mathbb Q/\mathbb Z)[m].
\]

Each factor is bounded below and injective, hence K-injective by Lemma 3.2. Lemma 3.1 makes the product K-injective. In degree \(n\le0\), exactly the factor with \(m=-n\) is nonzero, so \(I^n=\mathbb Q/\mathbb Z\); in positive degrees it is zero. Its differentials are zero. Thus it is not bounded below. In fact this product represents the product in the derived category too: Theorem 3.3 and the Hom-product identity of Lemma 3.1 give

\[
\operatorname{Hom}_D(K,I)
\cong\prod_{m\ge0}\operatorname{Hom}_D(K,(\mathbb Q/\mathbb Z)[m])
\]

for every \(K\).

Termwise injectivity alone does not give such a conclusion. Let \(R=k[\epsilon]/(\epsilon^2)\) for a field \(k\). Its only proper nonzero ideal is \((\epsilon)\): an element with nonzero constant term is a unit, while a nonzero scalar multiple of \(\epsilon\) generates that ideal. An \(R\)-linear map \((\epsilon)\to R\) sends \(\epsilon\) to \(c\epsilon\), because its image is killed by \(\epsilon\). Multiplication by \(c\) extends it to \(R\). Baer's criterion therefore proves that \(R\) is injective over itself. The bi-infinite complex

\[
\cdots\xrightarrow\epsilon R\xrightarrow\epsilon R
\xrightarrow\epsilon R\xrightarrow\epsilon\cdots
\]

is termwise injective and acyclic, since \(\ker(\epsilon)=\epsilon R=\operatorname{im}(\epsilon)\). A contraction would require \(1=\epsilon s^n+s^{n+1}\epsilon\) in every degree. Each \(R\)-endomorphism is multiplication by an element of \(R\), so the right side has image in \(\epsilon R\) and cannot be the identity. Its identity is a non-null-homotopic map from an acyclic complex into itself. It is not K-injective. The failure comes from the missing starting degree in Lemma 3.2's induction.

## 6. Exercises with complete solutions

**Exercise 1 (easy).** At an arbitrary point \(x\), prove directly that a skyscraper \(x_*J\) of an injective \(\mathcal O_x\)-module is injective. Do not assume that \(x\) is a closed point.

**Solution.** For a monomorphism \(F\to G\), exactness of stalks gives \(F_x\to G_x\) monic. A map \(F\to x_*J\) corresponds, under the stalk-skyscraper adjunction in Lemma 5.2 of the preceding lesson, to \(F_x\to J\). Extend it to \(G_x\to J\) by injectivity and transport back through that adjunction. This extends the original sheaf map. No assertion about the closure of \(x\) occurs in the proof; the sheaf's values and the adjunction already apply to every point.

**Exercise 2 (medium).** Give a second proof that injective module sheaves are flasque, using their embedding in Theorem 2.3 and a splitting, instead of extension by zero.

**Solution.** An injective \(I\) embeds into \(E(I)\). Extend \(1_I\) across this monomorphism to a retraction \(r:E(I)\to I\). Each \(E(I)(U)\) is a product of stalk injectives indexed by \(x\in U\); its restrictions are onto by filling missing coordinates with zero. For \(U\subset V\), include a section \(s\in I(U)\) in \(E(I)(U)\), extend it to \(E(I)(V)\), and apply \(r(V)\). Naturality of the retraction makes its restriction equal \(s\). This proves flasqueness.

**Exercise 3 (medium).** Use dimension shifting to prove that a flasque \(F\) has \(H^q(U,F)=0\) for \(q>0\), where \(H^q(U,F)=R^q\Gamma(U,F)\).

**Solution.** Embed \(F\) into an injective \(I\) and put \(C=I/F\). By Lemmas 1.1 and 1.2, \(C\) is flasque and \(I(U)\to C(U)\) is onto. Since \(I\) is already its own injective resolution, all its positive derived section functors vanish. The long exact sequence therefore makes \(H^1(U,F)\) the cokernel of \(I(U)\to C(U)\), hence zero, and gives \(H^q(U,F)\cong H^{q-1}(U,C)\) for \(q>1\). Induct on \(q\), applying the same first-step proof to each flasque quotient. This proves vanishing on every open, without an assumption of compactness or separation.

**Exercise 4 (hard).** Prove all implications in Corollary 3.4, including injectivity and surjectivity of the map to derived Hom, using the roofs of the common reading.

**Solution.** Assume every map from an acyclic complex to \(I\) is null-homotopic. Shifts have the same property, so both outer groups in the contravariant cone exact sequence for a quasi-isomorphism \(s:M\to N\) vanish. Thus \(s^*:\operatorname{Hom}_K(N,I)\to\operatorname{Hom}_K(M,I)\) is bijective. A derived map \(L\to I\) has a roof \(L\xleftarrow{s}M\xrightarrow{f}I\). The unique homotopy class \(g:L\to I\) with \(gs=f\) maps to this roof, proving surjectivity. If two homotopy classes have the same derived image, the equality criterion in Theorem 4.2 of the common reading equalizes them after some quasi-isomorphism into \(L\). Injectivity of its induced \(s^*\) equalizes the two classes before localization, proving injectivity. Conversely, bijectivity to derived Hom implies vanishing from acyclic sources because those sources are zero in \(D\). The source-comparison condition implies the same vanishing by applying it to \(0\to A\) for acyclic \(A\). Vanishing is exactly K-injectivity, completing the equivalences.

**Exercise 5 (hard).** Suppose \(\Phi\) is left exact, \(J\) is bounded below, and every term \(J^n\) is \(\Phi\)-acyclic. Explain precisely why one cannot prove the comparison in degree \(r\) by truncating only at degree \(r\). Give the correct truncation and prove the comparison.

**Solution.** A quotient brutal truncation ending at degree \(r\) deletes \(d^r\), which is needed to determine \(\ker d^r\) and hence \(H^r\). Moreover the removed tail starts at degree \(r+1\), whose derived cohomology in degree \(r+1\) can occur as the next term of the long exact sequence. Instead use the split sequence with tail \(\sigma_{\ge r+2}J\) and quotient \(\sigma_{\le r+1}J\). Both the tail's ordinary image and its derived image have zero cohomology in degrees \(r,r+1\), because the bounded-below resolution preserves its lower term bound. The long exact sequences identify the degree-\(r\) middle cohomologies with those of the bounded quotient. Induction on the quotient's finitely many terms, using the split bottom-term sequence, proves its comparison. Thus the degree-\(r\) comparison for \(J\) is an isomorphism. The two-degree buffer is the reason this argument works without a spectral sequence.

The next lesson proves the existence of resolutions for all complexes in a Grothendieck abelian category. The unbounded existence proof supplies a replacement for the lower-bound induction; the comparison theorem already established here continues to apply unchanged.

