# Galois cohomology and the étale cohomology of a field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised, and the valuation step in section 7 written, by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

Over a field, the étale topology records separable field extensions and the ways their embeddings are permuted. A sheaf is determined by the resulting continuous action on one geometric stalk. Global sections become invariant elements. Once we prove this equivalence, étale cohomology and Galois cohomology are derived functors of the same functor.

Continuity is essential. We will construct the continuous cochain complex from an acyclic resolution, rather than replace a profinite group by its underlying abstract group. Finite quotient calculations then prove the cohomological-dimension results, with the inflation maps made explicit. Hilbert 90, Kummer and Artin–Schreier give concrete degree-one classes.

We use lesson 7, the sheafification and group-topos constructions of lessons 1–2, the derived-functor machinery of lesson 3, and the affine quasi-coherent vanishing theorem of lesson 5. Finite separable extensions, finite Galois theory and the finite Sylow theorems are algebra prerequisites. We prove the needed finite-étale/Galois-set correspondence here. All modules have the discrete topology, with continuous left group action. Put \(G_K=\operatorname{Gal}(K^s/K)\), where \(K^s\) is a chosen separable closure in an algebraic closure \(\Omega\).

## 1. Reconstructing a sheaf from its geometric stalk

An étale scheme over \(K\) is a disjoint union of spectra of finite separable extensions. This is the field-fibre theorem used in lesson 6: every point has an affine étale neighbourhood with a finite separable field as coordinate ring, so that point is open. Thus finite étale schemes give a basis for the small site; an arbitrary object is covered by its connected field components.

For a finite étale scheme \(V\), set \(S_V=V(K^s)\), with action by postcomposition on its residue embeddings. This is a finite \(G_K\)-set. Conversely a transitive finite continuous \(G_K\)-set is \(G_K/H\) with \(H\) open; it comes from \(\operatorname{Spec}(K^s)^H\). An arbitrary finite set is a disjoint union of these orbits.

This correspondence is fully faithful. An equivariant map \(G_K/H\to G_K/J\) is determined by a coset \(gJ\) fixed by \(H\), equivalently \(H\subseteq gJg^{-1}\). The associated \(K\)-embedding is
\((K^s)^J\to(K^s)^H\), \(a\mapsto g(a)\). Conversely every embedding between finite separable subextensions extends to an automorphism of \(K^s\), by finite normal closure and extension of embeddings, and gives precisely that coset. This proves both injectivity and surjectivity on maps between connected objects. Maps from disjoint unions amount to a map on each connected component, proving full faithfulness in general. Fibre products correspond to fibre products of the embedding sets, and covers correspond to jointly surjective maps of those sets. Both claims follow by splitting the finitely many field algebras over a common finite Galois extension; faithful base change detects the maps and their surjectivity.

Let \(M\) be any continuous discrete \(G_K\)-set, possibly infinite. Define

\[
\mathcal F_M(V)=\operatorname{Hom}_{G_K}(V(K^s),M).
\tag{1.1}
\]

The same formula applies to arbitrary étale \(V\), using its disjoint union of finite orbits. This is a sheaf: an equivariant function on the target of a jointly surjective family is exactly a family of equivariant functions agreeing on all pairwise fibre products. Indeed define its value using any preimage; overlap agreement makes it independent of that choice, and equivariance follows by translating the preimage. This proves the matching condition, including empty objects and arbitrary covering families.

**Theorem 1.1.** Taking the geometric stalk, with its change-of-embedding action, and (1.1) give inverse equivalences

\[
\operatorname{Sh}(\operatorname{Spec}K_{\mathrm{ét}})
\simeq G_K\text{-}\operatorname{Sets}_{\mathrm{disc,cont}}.
\tag{1.2}
\]

Under this equivalence \(\Gamma(\operatorname{Spec}K,F)=(F_{\bar s})^{G_K}\).

**Proof.** The action on a stalk is continuous by lesson 6: a representative on a finite separable pointed neighbourhood is fixed by the open subgroup fixing that embedding. For \(\mathcal F_M\), evaluate a germ at its selected lift. This gives a natural equivariant map \((\mathcal F_M)_{\bar s}\to M\). For \(m\in M\), choose an open stabilizer \(H\). The function \(gH\mapsto gm\) on the field object \(\operatorname{Spec}(K^s)^H\), with its identity embedding as lift, represents \(m\). Thus the map is surjective. For two germs with equal values, first restrict to the selected connected components of their objects and take a common finite field extension inside \(K^s\). On its transitive embedding orbit, two equivariant functions with the same value at one lift agree everywhere. Their germs are equal, proving injectivity. This also verifies its inverse and naturality, rather than only identifying the cardinalities.

For the other composite, put \(M=F_{\bar s}\). Send a section \(t\in F(V)\) to the function assigning to each embedding \(v\) its germ at \((V,v)\). The change-of-embedding action makes this function equivariant, and the construction commutes with restriction. We prove it is a bijection.

First, for a connected field object \(V=\operatorname{Spec}L\) and a selected embedding \(\iota:L\to K^s\), the map from \(F(V)\) to the stalk at \(\iota\) is injective. Equality of two germs is realized on a common pointed finite-field refinement; that refinement surjects onto \(V\), so the sheaf's separatedness gives equality of the original sections. Connected finite-field refinements are cofinal, as one can select the component of a fibre product containing the chosen lift. This proves the asserted injectivity and injectivity of the section-to-function map.

To prove surjectivity it suffices, on this transitive orbit, to start with \(m\in M^{H_L}\), where \(H_L=\operatorname{Gal}(K^s/\iota(L))\). Represent \(m\) on a finite field neighbourhood and refine to \(\operatorname{Spec}E\), where \(E/K\) is finite Galois and contains both that field and \(\iota(L)\). Write its representative as \(t\in F(E)\). If \(\sigma=h|_E\) with \(h\in H_L\), the map \(\operatorname{Spec}\sigma\) sends the selected identity embedding to the embedding \(\sigma\). Consequently the germ of \(\sigma^*t\) at the identity embedding is exactly the translated germ \(hm=m\). The injectivity just proved makes \(t\) invariant under every automorphism in \(\operatorname{Gal}(E/L)\). The two pullbacks of \(t\) to

\[
\operatorname{Spec}(E\otimes_LE)
=\coprod_{\sigma\in\operatorname{Gal}(E/L)}\operatorname{Spec}E
\tag{1.3}
\]

agree: on the \(\sigma\) component they are \(t\) and its \(\sigma\)-pullback. The sheaf condition for \(\operatorname{Spec}E\to\operatorname{Spec}L\) descends \(t\) to a unique section on \(V\), with germ \(m\). For a general object take the product of these bijections over its disjoint field components; sheaves turn their covering coproduct into that product. This proves the natural isomorphism \(F=\mathcal F_{F_{\bar s}}\).

At the final object \(\operatorname{Spec}K\), its embedding set is a singleton with trivial action, and (1.1) gives exactly \(M^{G_K}\). This proves the last assertion with its natural map. \(\square\)

Giving an internal abelian group on either side of (1.2) gives an abelian sheaf on the left and a discrete continuous \(G_K\)-module on the right. The two constructions preserve the operations and their identities, so they give an exact equivalence of abelian categories. It takes injectives to injectives. Since global sections are invariants, their injective section complexes agree, yielding naturally

\[
H^q(\operatorname{Spec}K_{\mathrm{ét}},F)
=H^q(G_K,F_{\bar s})
\quad(q\geq0).
\tag{1.4}
\]

Here the right side is initially defined as the right derived functor of invariants. The coefficient correspondences include \(\mathbf G_a\leftrightarrow(K^s,+)\), \(\mathbf G_m\leftrightarrow(K^s)^\times\), constant abelian sheaves \(\leftrightarrow\) trivial modules, and \(\mu_n\leftrightarrow\mu_n(K^s)\) with its actual root-permutation action. The units and additive identifications follow from the stalk rings of lesson 6. They use the separable closure, which need not be algebraically closed in positive characteristic.

## 2. An acyclic resolution by continuous functions

Let \(G\) now be any profinite group. A discrete \(G\)-module is an abelian group in which every element has open stabilizer. Kernels, cokernels and finite limits have their usual underlying groups and induced actions. Colimits have their usual underlying groups as well: any representative of an element already has an open stabilizer at a stage. We write \(H^q(G,M)=R^q(M\mapsto M^G)\).

For an abelian group \(A\), define

\[
I_G(A)=\operatorname{Maps}_{\mathrm{cont}}(G,A),
\qquad(a b)(g)=b(ga).
\tag{2.1}
\]

This is a discrete continuous \(G\)-module. A continuous function from compact \(G\) to discrete \(A\) has finite image and is constant on cosets of some open normal subgroup, using a finite subcover of its locally constant neighbourhoods. That subgroup fixes it in (2.1). Evaluation at \(1\) gives the adjunction between \(I_G\) and the exact forgetful functor, as proved for sets in lesson 2; the maps \(\psi\mapsto(m\mapsto[g\mapsto\psi(gm)])\) and evaluation are also additive.

The functor \(I_G\) is exact. Only surjectivity needs proof: lift the finitely many values of a continuous function through a surjection of abelian groups, using one chosen lift for each value. Its finitely many clopen fibres make the lifted function continuous. It preserves injectives because its left adjoint is exact. Every \(M\) embeds equivariantly in \(I_G(M)\) by \(m\mapsto[g\mapsto gm]\). Composing with an embedding of its underlying group into an injective abelian group gives an embedding in an injective \(G\)-module. Hence this category has enough injectives.

Moreover \(I_G(A)^G=A\), by constant functions and evaluation at \(1\). Apply \(I_G\) to an injective resolution of \(A\) in abelian groups: exactness and preservation of injectives give a \(G\)-injective resolution, and its invariant complex is the original resolution. Therefore

\[
H^q(G,I_G(A))=0\quad(q>0).
\tag{2.2}
\]

Consider the homogeneous augmented complex

\[
0\longrightarrow M\longrightarrow E^0(M)\longrightarrow E^1(M)
\longrightarrow\cdots,
\quad E^n(M)=\operatorname{Maps}_{\mathrm{cont}}(G^{n+1},M),
\tag{2.3}
\]

where \(M\to E^0\) sends \(m\) to the constant function, the group action is
\((a f)(g_0,\ldots,g_n)=a f(a^{-1}g_0,\ldots,a^{-1}g_n)\), and the differential is the alternating sum of deleting an argument. It is an exact complex of discrete \(G\)-modules. The identity \(d^2=0\) follows by pairing the two orders of deleting two arguments, whose signs are opposite. On underlying groups a contraction inserts \(1\) as the first argument; expanding the two alternating sums gives \(dh+hd=1\), including the augmented position. This insertion is continuous, so proves exactness here; the contraction need not be equivariant.

Each term is acyclic for invariants. To verify this, let \(A_n=\operatorname{Maps}_{\mathrm{cont}}(G^n,M)\), regarded just as an abelian group. The equivariant isomorphism \(E^n(M)\to I_G(A_n)\) is

\[
(\Theta f)(t)(x_1,\ldots,x_n)
=t f(t^{-1},t^{-1}x_1,\ldots,t^{-1}x_n).
\tag{2.4}
\]

Its inverse sends \(b\) to
\(f(g_0,\ldots,g_n)=g_0 b(g_0^{-1})(g_0^{-1}g_1,\ldots,g_0^{-1}g_n)\).
These formulas are continuous in the required discrete-function sense. Indeed a continuous function on a compact profinite product has finite image and factors through a finite quotient in all its arguments. An open normal subgroup fixing that finite image and preserving those quotient arguments makes \(t\mapsto(\Theta f)(t)\) locally constant as a map into the discrete group \(A_n\). Conversely a locally constant \(b\) has finitely many function values, each of which factors through a finite quotient; intersecting their quotient kernels and the stabilizers of their finitely many values gives joint continuity of the inverse formula. Substitution proves both inverse identities and \(\Theta(af)(t)=\Theta f(ta)\). This also proves continuity of the action on \(E^n(M)\). Now (2.2) applies.

Taking invariants of the acyclic resolution (2.3) computes derived invariants, by the acyclic-resolution argument of lesson 3. An invariant homogeneous function is determined by its values on \((1,g_1,g_1g_2,\ldots,g_1\cdots g_n)\). The resulting complex is the continuous inhomogeneous cochain complex

\[
C^n(G,M)=\operatorname{Maps}_{\mathrm{cont}}(G^n,M),
\tag{2.5}
\]

with \(C^0=M\) and differential

\[
\begin{aligned}
(dc)(g_1,\ldots,g_{n+1})={}&g_1c(g_2,\ldots,g_{n+1})\\
&+\sum_{i=1}^{n}(-1)^i c(g_1,\ldots,g_i g_{i+1},\ldots,g_{n+1})\\
&+(-1)^{n+1}c(g_1,\ldots,g_n).
\end{aligned}
\tag{2.6}
\]

For \(n=0\) this says \((dm)(g)=gm-m\). The formula follows by deleting each argument in the displayed homogeneous tuple; deleting the first uses equivariance and produces the \(g_1\) action, deleting an intermediate argument multiplies two adjacent group elements, and deleting the last gives the final term. We have proved

\[
H^q(G,M)=H^q(C^\bullet(G,M)).
\tag{2.7}
\]

No cochain on the underlying abstract group was substituted for a continuous one. Also, a short exact sequence of discrete modules gives a short exact sequence of these cochain complexes: every cochain has finite image, so the same finite-value lift argument proves surjectivity termwise. Thus the usual cocycle connecting maps are the derived-functor connecting maps under (2.7), by naturality of the acyclic construction.

## 3. Finite quotients, torsion and degree-one cocycles

**Proposition 3.1.** For a discrete continuous \(G\)-module \(M\),

\[
H^q(G,M)=\operatorname*{colim}_{U\trianglelefteq_{\mathrm{open}}G}
H^q(G/U,M^U).
\tag{3.1}
\]

For \(U'\subseteq U\), the transition map is inflation together with the inclusion \(M^U\subseteq M^{U'}\). Also cohomology commutes with filtered colimits of discrete \(G\)-modules.

**Proof.** A continuous \(c:G^n\to M\) has finite image. Compactness gives a finite cover by basic open rectangles on which it is constant; intersect open normal coordinate kernels to make it factor through \((G/U)^n\). Shrink \(U\) further to fix its finitely many values. It then lies in \(C^n(G/U,M^U)\). Conversely every such cochain pulls back continuously, and two representatives become identical precisely on a common smaller open normal subgroup. The differential respects these subcomplexes. Therefore the continuous complex is their filtered union. Filtered colimits of abelian groups are exact, so their cohomology gives (3.1).

For a filtered module colimit, a cochain in the limit has finite image; lift its finitely many values to a common stage and use its clopen fibre partition to obtain a continuous cochain there. Equality of two cochains is equality of finitely many values, hence holds at a later common stage. The same argument works for \(n=0\). Thus the cochain complexes commute with the filtered colimit, and exactness gives the cohomology assertion. \(\square\)

**Corollary 3.2.** The group \(H^q(G,M)\) is torsion for every \(q>0\). It is zero in those degrees when \(M\) is a rational vector space with continuous action.

**Proof.** For a finite group \(Q\), use equivariant homogeneous cochains. The operator
\((sf)(g_0,\ldots,g_{n-1})=\sum_{a\in Q}f(a,g_0,\ldots,g_{n-1})\)
is equivariant, by translating the summation index. The insertion contraction gives \(ds+sd=|Q|\) in positive degrees: it is the sum, over \(a\), of the contractions inserting \(a\). Hence \(|Q|\) annihilates every positive cohomology class. By (3.1) each class for \(G\) comes from such a finite quotient and is annihilated by its order. For rational coefficients these cochains, their kernels and their cohomology are rational vector spaces; a torsion rational vector space is zero. \(\square\)

In degree one, (2.6) identifies cocycles with continuous crossed homomorphisms
\(c(gh)=c(g)+g c(h)\), modulo \(c(g)=gm-m\). For a trivial action this becomes

\[
H^1(G,M)=\operatorname{Hom}_{\mathrm{cont}}(G,M).
\tag{3.2}
\]

For a multiplicative module use \(c(gh)=c(g)g(c(h))\) and coboundaries \(g(b)/b\). The quotient formula (3.1) does not say that positive finite-quotient cohomology persists: inflation can kill it. We will use precisely that phenomenon for \(\widehat{\mathbf Z}\).

There is also a useful finiteness check. If \(G\) has \(r\) topological generators and \(M\) is a finite-dimensional vector space over a finite field with continuous linear action, evaluation on those generators injects \(Z^1(G,M)\) into \(M^r\). The cocycle identity determines the values on words in the generators and their inverses; continuity then determines the values on their dense subgroup's closure. Hence \(\dim H^1(G,M)\leq r\dim M\). A similar assertion for an arbitrary finite coefficient group bounds the number of degree-one cocycles by \(|M|^r\).

## 4. Hilbert 90, Kummer and Artin–Schreier

**Theorem 4.1 (Hilbert 90).** For every field \(K\),

\[
H^1(G_K,(K^s)^\times)=0.
\tag{4.1}
\]

**Proof.** First let \(E/K\) be finite Galois with group \(Q\), and let \(c_\sigma\in E^\times\) satisfy \(c_{\sigma\tau}=c_\sigma\sigma(c_\tau)\). Distinct field automorphisms of \(E\) are linearly independent over \(E\), as functions on \(E\). To prove this, choose a nonzero relation of minimal length, \(\sum_{i=1}^r a_i\sigma_i(x)=0\) for all \(x\), with every \(a_i\neq0\). Length one is impossible. Choose \(y\) with \(\sigma_j(y)\neq\sigma_1(y)\) for some \(j>1\). Subtract \(\sigma_1(y)\) times the relation at \(x\) from the relation at \(yx\). The first term vanishes, the \(j\)th does not, and we get a shorter nonzero relation, a contradiction.

It follows that for some \(x\in E\) the element

\[
b=\sum_{\sigma\in Q}c_\sigma^{-1}\sigma(x)
\tag{4.2}
\]

is nonzero. The cocycle identity gives
\(\tau(c_\sigma^{-1})=c_\tau c_{\tau\sigma}^{-1}\), so changing the summation index proves \(\tau(b)=c_\tau b\). Thus \(c_\tau=\tau(b)/b\) is a coboundary, with the convention of §3.

For a continuous cocycle on \(G_K\), Proposition 3.1's cochain argument supplies an open normal \(U\) such that its values lie in \(((K^s)^\times)^U=E^\times\), \(E=(K^s)^U\), and it factors through \(G_K/U=\operatorname{Gal}(E/K)\). The finite argument supplies \(b\in E^\times\) with the required coboundary. This proves (4.1) without a finiteness hypothesis on \(K\). \(\square\)

Let \(n\geq1\) be invertible in \(K\). The sequence of discrete modules

\[
1\longrightarrow\mu_n(K^s)\longrightarrow(K^s)^\times
\xrightarrow{b\mapsto b^n}(K^s)^\times\longrightarrow1
\tag{4.3}
\]

is exact: the polynomial \(T^n-a\), for \(a\neq0\), is separable, so all its roots lie in \(K^s\). Theorem 1.1 makes (4.3) the Kummer sequence of étale sheaves. Its invariant sequence and Hilbert 90 give

\[
H^1(K,\mu_n)=K^\times/K^{\times n}.
\tag{4.4}
\]

If \(b^n=a\in K^\times\), the boundary class is the cocycle \(g\mapsto g(b)/b\). Replacing \(b\) by another root changes it by a \(\mu_n\)-coboundary; replacing \(a\) by an \(n\)th power multiple gives the same class. Geometrically its torsor is \(\operatorname{Spec}K[T]/(T^n-a)\), with right action multiplying the root by an \(n\)th root of unity. This agrees with lesson 6's Kummer construction and lesson 3's torsor convention.

**Proposition 4.2 (Artin–Schreier).** Suppose \(\operatorname{char}K=p>0\), and write \(\wp(a)=a^p-a\). Then

\[
H^1(K,\mathbf F_p)=K/\wp(K),
\qquad H^q(K,\mathbf F_p)=0\quad(q\geq2).
\tag{4.5}
\]

**Proof.** The additive map \(\wp:K^s\to K^s\) is surjective: \(T^p-T-a\) has derivative \(-1\), and therefore its roots lie in the separably closed field \(K^s\). Its kernel consists of precisely the \(p\) elements of the prime field. This proves the exact sequence

\[
0\longrightarrow\mathbf F_p\longrightarrow(K^s,+)
\xrightarrow{\wp}(K^s,+)\longrightarrow0.
\tag{4.6}
\]

The additive module corresponds to \(\mathbf G_a=\mathcal O\). The affine quasi-coherent vanishing theorem proved in lesson 5 gives
\(H^q(K,(K^s,+))=0\) for \(q>0\), by (1.4). Thus the beginning of the long exact sequence is \(K\xrightarrow{\wp}K\to H^1(K,\mathbf F_p)\to0\); its later terms give the vanishing in (4.5). The class of \(a\) is represented by \(g\mapsto g(b)-b\), where \(\wp(b)=a\). Its torsor is \(T^p-T=a\), with right action \(b\mapsto b+c\), \(c\in\mathbf F_p\). \(\square\)

Neither statement needs \(K\) perfect. The coefficient \(\mathbf F_p\) here is constant and additive. In characteristic \(p\), the étale sheaf \(\mu_p\) on a field has only its identity section on every finite separable extension; it cannot replace \(\mathbf F_p\) in (4.5).

## 5. Closed subgroups and cohomological dimension

For a prime \(\ell\), define \(\operatorname{cd}_\ell G\) as the least \(d\geq0\) such that \(H^q(G,M)=0\) for every discrete \(\ell\)-primary torsion module \(M\) and every \(q>d\), or \(\infty\) if none exists. Define \(\operatorname{cd}G=\sup_\ell\operatorname{cd}_\ell G\). Equivalently, \(\operatorname{cd}G\leq d\) means vanishing above \(d\) for every torsion discrete module. Indeed a torsion group is the direct sum of its primary parts, stable under every automorphism, and Proposition 3.1 permits cohomology to commute with that sum, expressed as a filtered union of finite subsums. We use \(\operatorname{cd}_\ell K=\operatorname{cd}_\ell G_K\), including imperfect fields. These definitions impose no vanishing condition on non-torsion modules.

We prove the subgroup facts needed for fields. Their continuity details matter even when \(H\) is closed but not open.

**Lemma 5.1 (continuous coinduction and Shapiro).** If \(H\subseteq G\) is a closed subgroup and \(N\) is a discrete \(H\)-module, put

\[
\operatorname{Coind}_H^G N
=\{b:G\to N\text{ continuous}:b(hg)=h b(g)\},
\qquad(a b)(g)=b(ga).
\tag{5.1}
\]

This is an exact functor, right adjoint to restriction, and

\[
H^q(G,\operatorname{Coind}_H^G N)=H^q(H,N).
\tag{5.2}
\]

**Proof.** Each \(b\) factors through the right cosets of some open normal \(U\subset G\), so (5.1) is a discrete continuous module. Evaluation at \(1\) takes a \(G\)-map \(M\to\operatorname{Coind}_H^G N\) to an \(H\)-map \(M\to N\). The inverse sends \(\psi\) to \(m\mapsto[g\mapsto\psi(gm)]\); the orbit of \(m\) is finite, so this function is continuous. Direct substitution proves the inverse identities and equivariance. This is the adjunction.

Kernels are computed pointwise. For surjectivity, let \(M\twoheadrightarrow N\) be a surjection of \(H\)-modules and let \(b\) belong to (5.1). Choose an open normal \(U\) for which \(b\) is constant on right \(U\)-cosets. Choose representatives \(r\) for the finitely many \(H\)-orbits on \(G/U\), and lifts \(m_r\in M\) of \(b(r)\). There is an open normal \(U'\subseteq U\) such that \(H\cap U'\) fixes every \(m_r\): each stabilizer is open in the subspace topology on \(H\), and an open normal subgroup of \(G\) can be chosen inside the finitely many corresponding neighbourhoods.

Choose one representative \(r_i\) for each \(H\)-orbit on \(G/U'\), adjusting it by an element of \(H\) so its image in \(G/U\) is one of the chosen \(rU\). Set \(\widetilde b(h r_i U')=h m_r\). This is well-defined, because the stabilizer of \(r_iU'\) in \(H\) is \(H\cap U'\), using normality of \(U'\). It is a continuous \(H\)-equivariant function and maps to \(b\). This proves exactness without choosing a continuous transversal for an arbitrary quotient.

Restriction is exact, so the adjunction makes coinduction preserve injectives. Its \(G\)-invariants are constant functions with value in \(N^H\). Apply this exact functor to an \(H\)-injective resolution of \(N\); the invariant complexes agree termwise, proving (5.2) naturally. This natural isomorphism is induced by restriction of cochains and evaluation at \(1\): both agree on invariants and on connecting maps, so the universal derived-functor comparison of lesson 3 identifies them in every degree. \(\square\)

Since a continuous function into an \(\ell\)-primary group has finitely many values, one power of \(\ell\) kills that function. Coinduction therefore preserves \(\ell\)-primary torsion. Equation (5.2) proves

\[
\operatorname{cd}_\ell H\leq\operatorname{cd}_\ell G
\quad\text{for every closed }H\subseteq G.
\tag{5.3}
\]

A pro-\(\ell\) group is an inverse limit of finite \(\ell\)-groups. A Sylow pro-\(\ell\) subgroup \(P\subseteq G\) has Sylow image in every finite quotient. Such a subgroup exists. For each open normal \(U\), let \(\mathcal S_U\) be the nonempty finite set of Sylow \(\ell\)-subgroups of \(G/U\). Quotient maps send Sylow groups to Sylow groups, giving an inverse system. Its inverse limit is nonempty by the finite-set compactness lemma proved in lesson 2: every finite collection of compatibility constraints is met by choosing a Sylow group at a common finer quotient. A compatible choice \((P_U)\) gives \(P=\varprojlim P_U\subset G\); the transition maps on these chosen groups are surjective, so its images are exactly \(P_U\). It is closed and pro-\(\ell\), and every index \([G/U:P_U]\) is prime to \(\ell\).

**Lemma 5.2.** For an \(\ell\)-primary discrete \(G\)-module \(M\), restriction
\(H^q(G,M)\to H^q(P,M)\) is injective. Consequently

\[
\operatorname{cd}_\ell G=\operatorname{cd}_\ell P.
\tag{5.4}
\]

**Proof.** Start with a finite group \(Q\) and subgroup \(S\) of index \(a\). There are \(Q\)-maps

\[
\eta:M\longrightarrow\operatorname{Coind}_S^Q M,
\quad\eta(m)(g)=gm,
\qquad
\varepsilon(b)=\sum_{g\in S\backslash Q}g^{-1}b(g).
\tag{5.5}
\]

The summand is unchanged by replacing \(g\) with \(hg\), since \(b(hg)=h b(g)\). For \(x\in Q\), put \(k=gx\) in the sum to get \(\varepsilon(xb)=x\varepsilon(b)\). Thus both maps are equivariant, and \(\varepsilon\eta=a\). Under Shapiro, \(H^q(\eta)\) is restriction: evaluation after the cochain comparison has \(\eta(c)(1)=c\) on restricted arguments. It follows that the kernel of restriction is killed by \(a\). If \(a\) is prime to \(\ell\), multiplication by \(a\) is an automorphism of any \(\ell\)-primary group: on each element killed by \(\ell^r\), use the inverse of \(a\) modulo \(\ell^r\). Restriction is then injective.

Now let \(q>0\) and let a continuous cocycle \(c\) represent a class for \(G\) whose restriction to \(P\) is zero. By (3.1), \(c\) factors through \((G/U)^q\) with values in \(M^U\). There is a continuous \((q-1)\)-cochain \(b\) on \(P\) with \(db=c|_P\). Choose an open normal \(W\subseteq U\) so that \(b\) factors through \((P/(P\cap W))^{q-1}\) and \(W\) fixes its finitely many values. This is possible by compactness on \(P\) and its induced topology; for degree zero it only requires fixing its single value. Then the class of \(c\) in \(H^q(G/W,M^W)\) restricts to zero on the finite Sylow group \(P_W\), since its primitive \(b\) is now a cochain there with values in \(M^W\). The finite case makes that class zero. Its image in (3.1) is our original class, which is therefore zero. Degree-zero restriction is the evident inclusion of invariants. Combine this injectivity with (5.3) to obtain (5.4). \(\square\)

**Lemma 5.3 (one-coefficient test for pro-\(\ell\) groups).** If \(P\) is pro-\(\ell\) and \(d\geq0\), then

\[
\operatorname{cd}_\ell P\leq d
\quad\Longleftrightarrow\quad
H^{d+1}(P,\mathbf F_\ell)=0,
\tag{5.6}
\]

where \(\mathbf F_\ell\) has trivial action.

**Proof.** Necessity is immediate. Every finite nonzero \(\ell\)-primary \(P\)-module \(A\) has a filtration with trivial \(\mathbf F_\ell\) quotients. Indeed \(A[\ell]\) is a nonzero finite vector space and the action factors through a finite \(\ell\)-group. All non-singleton orbits have sizes divisible by \(\ell\), so the cardinality of the fixed set is congruent to \(|A[\ell]|=0\) modulo \(\ell\). It contains zero, hence contains at least \(\ell\) elements. A nonzero fixed element spans a trivial line. Apply the same argument to the quotient and induct on \(|A|\). The long exact sequence and the assumed vanishing give \(H^{d+1}(P,A)=0\) along this filtration.

An arbitrary discrete \(\ell\)-primary module is a filtered union of finite \(P\)-stable submodules. The orbit of each of finitely many elements is finite, and their generated abelian group is finite because those elements have bounded \(\ell\)-power orders. Proposition 3.1 extends the one-degree vanishing to every such module \(A\).

Finally embed \(A\) in \(I_P(A)\) as in §2. Both that module and the quotient \(B=I_P(A)/A\) are \(\ell\)-primary torsion, since every continuous function has finite image. Acyclicity (2.2) and the exact sequence give \(H^{r+1}(P,A)=H^r(P,B)\) for \(r\geq1\). Apply the already proved vanishing in degree \(d+1\) to successive such quotients. This kills every degree greater than \(d\), including when \(d=0\), and proves sufficiency. \(\square\)

**Theorem 5.4.** If \(\operatorname{char}K=p>0\), then

\[
\operatorname{cd}_p G_K\leq1.
\tag{5.7}
\]

**Proof.** Let \(P\) be a Sylow pro-\(p\) subgroup, and let \(L=(K^s)^P\). The field \(K^s\) is a separable closure of \(L\): it is separably closed and algebraic separable over \(L\). Galois correspondence gives \(G_L=P\). The field \(L\) also has characteristic \(p\), so Proposition 4.2 gives \(H^2(P,\mathbf F_p)=0\). Lemma 5.3 gives \(\operatorname{cd}_pP\leq1\), and Lemma 5.2 gives (5.7). This proves vanishing for every discrete \(p\)-primary coefficient module, not just the constant module occurring in (4.5). \(\square\)

For the next lesson, define temporarily the *cohomological Brauer group*
\(B(E)=H^2(G_E,(E^s)^\times)\). Its identification with classes of central simple algebras belongs to lesson 9. The direction of Serre's criterion used there has the following complete cohomological proof.

**Proposition 5.5.** Let \(\ell\neq\operatorname{char}K\). If \(B(E)[\ell]=0\) for every finite separable \(E/K\), then \(\operatorname{cd}_\ell K\leq1\).

**Proof.** Kummer and Hilbert 90 identify
\(H^2(E,\mu_\ell)=B(E)[\ell]\). Let \(P\) be a Sylow pro-\(\ell\) subgroup of \(G_K\), and \(L=(K^s)^P\). Its action on \(\mu_\ell\) is trivial: the image is both an \(\ell\)-group and a subgroup of \(\operatorname{Aut}(\mu_\ell)\), of order \(\ell-1\). Thus all these roots belong to \(L\). Write \(L\) as the filtered union of its finite separable subextensions \(E/K\) containing \(\mu_\ell\). The affine-transition étale-cohomology continuity theorem, in the exact form used in lesson 7 §2, gives

\[
H^2(L,\mu_\ell)=\operatorname*{colim}_E H^2(E,\mu_\ell)=0.
\tag{5.8}
\]

Here the sheaves pull back correctly because \(\mu_\ell\) is represented by a finite étale scheme; this uses lesson 7's representable inverse-image formula, and does not assume an inverse-image formula for arbitrary units sheaves. Choose a primitive \(\ell\)th root in \(L\); it identifies this coefficient with the trivial \(P\)-module \(\mathbf F_\ell\). Lemmas 5.3 and 5.2 now imply the conclusion. \(\square\)

For reference, Serre's criterion in its usual Brauer-group formulation says that \(\operatorname{cd}_\ell K\leq1\) is equivalent to the vanishing of the \(\ell\)-primary parts of the Brauer groups of all finite separable extensions. The algebraic interpretation is deferred to lesson 9. The reverse cohomological implication also follows from what we have proved: (5.3) gives \(\operatorname{cd}_\ell E\leq1\), hence \(H^2(E,\mu_\ell)=0\), so \(B(E)[\ell]=0\) by Kummer. A nonzero \(\ell\)-primary torsion group has an element of order \(\ell\), so this annihilates its entire \(\ell\)-primary part.

## 6. Procyclic groups and finite fields

Let \(C_n=\langle F\mid F^n=1\rangle\) and put \(D=F-1\), \(N_n=1+F+\cdots+F^{n-1}\). The following free \(\mathbf Z[C_n]\)-resolution computes its cohomology:

\[
\cdots\xrightarrow{D}\mathbf Z[C_n]
\xrightarrow{N_n}\mathbf Z[C_n]
\xrightarrow{D}\mathbf Z[C_n]
\xrightarrow{\varepsilon}\mathbf Z\longrightarrow0.
\tag{6.1}
\]

Here \(\varepsilon\) sums coefficients; in degree one the differential is \(D\), in degree two it is \(N_n\), and the pattern repeats. To prove exactness, multiplication by \(D\) takes successive differences of the cyclic coefficient list. Its kernel consists of constant lists, precisely \(\mathbf Z N_n\); its image consists of coefficient lists with sum zero, since each such list is a sum of adjacent differences. Multiplication by \(N_n\) sends a list to its coefficient sum times \(N_n\). Thus its image is \(\ker D\), its kernel is \(\operatorname{im}D\), and the augmentation kernel is also \(\operatorname{im}D\). This proves every position of (6.1). Applying \(\operatorname{Hom}_{\mathbf Z[C_n]}(-,M)\) gives

\[
\begin{aligned}
H^0(C_n,M)&=M^F,\\
H^{2i+1}(C_n,M)&=\ker(N_n:M\to M)/(F-1)M\quad(i\geq0),\\
H^{2i}(C_n,M)&=M^F/N_nM\quad(i\geq1).
\end{aligned}
\tag{6.2}
\]

We need the inflation maps, not just these groups. Under the quotient \(C_{rn}\to C_n\), mapping a chosen generator to \(F\), a chain map from the large-group resolution to the small-group resolution sends its free generator in degree \(j\) to \(r^{\lfloor j/2\rfloor}\) times the free generator. It lifts the identity of \(\mathbf Z\). For odd \(j\), the chain-map equations use \(D\) and the equal powers in degrees \(j,j-1\); for even \(j\), they use the image \(N_{rn}=rN_n\) and powers differing by a factor \(r\). Thus it is a chain map in every degree. Any chain map between these resolutions lifting the identity computes inflation: compare with the standard resolution, using projectivity of the domain's free terms and exactness of the target to lift and construct the usual homotopy. Consequently on the representatives in (6.2) inflation acts by

\[
m\longmapsto r^{\lfloor q/2\rfloor}m
\quad\text{in degree }q.
\tag{6.3}
\]

It is the identity on degree-one representatives, while in every degree \(q\geq2\) a sufficiently divisible \(r\) annihilates finite torsion coefficients.

**Theorem 6.1.** Let \(G=\widehat{\mathbf Z}\), with topological generator \(F=1\), and let \(M\) be a torsion discrete continuous module. Then

\[
H^0(G,M)=M^F,\qquad
H^1(G,M)=M/(F-1)M,\qquad
H^q(G,M)=0\quad(q\geq2).
\tag{6.4}
\]

Hence \(\operatorname{cd}_\ell\widehat{\mathbf Z}=1\) for every prime \(\ell\), and \(\operatorname{cd}\widehat{\mathbf Z}=1\).

**Proof.** First suppose \(M\) finite. Its action factors through \(C_n\) for some \(n\). In (3.1) the quotients \(C_{rn}\) are cofinal among finite quotients, and their coefficients \(M^{rn\widehat{\mathbf Z}}\) are all \(M\). If \(r\) is a multiple of the exponent of \(M\), then \(N_{rn}=rN_n\) is zero on \(M\). The degree-one groups are therefore eventually all \(M/(F-1)M\), with identity transition maps by (6.3). Each higher-degree class is killed after multiplying \(r\) by that exponent, again by (6.3). Degree zero is \(M^F\); fixing the generator is the same as fixing its dense cyclic subgroup and then, by continuity, all of \(G\).

An arbitrary torsion \(M\) is a filtered union of finite \(G\)-stable submodules, by the finite-orbit argument of Lemma 5.3, now allowing all primes. Proposition 3.1 extends the three formulas to their union. They give \(\operatorname{cd}_\ell G\leq1\). For trivial \(M=\mathbf F_\ell\), degree one in (6.4) is \(\mathbf F_\ell\neq0\); hence equality holds for every \(\ell\). \(\square\)

For a finite field \(\mathbf F_q\), the separable closure is the union of the finite fields \(\mathbf F_{q^n}\), and their Galois groups are cyclic of order \(n\), generated compatibly by the *arithmetic Frobenius* \(F(a)=a^q\). To verify this, the roots of \(T^{q^n}-T\) are distinct and closed under addition, multiplication and inverses, hence form a field of \(q^n\) elements. Its degree over \(\mathbf F_q\) is \(n\), and Frobenius has order \(n\): a smaller power could not fix \(q^n\) elements because \(T^{q^d}-T\) has only \(q^d\) roots. Every algebraic element lies in a finite field extension, whose elements satisfy \(a^{q^d}=a\) by the order of its multiplicative group. This proves the union and the compatible cyclic descriptions. It follows that

\[
G_{\mathbf F_q}=\varprojlim_n\mathbf Z/n\mathbf Z
=\widehat{\mathbf Z},\qquad
\operatorname{cd}\mathbf F_q=1.
\tag{6.5}
\]

For every torsion coefficient module, not merely a finite one, (6.4) computes its cohomology. For example \(H^1(\mathbf F_q,\mathbf F_\ell)=\mathbf F_\ell\) with trivial action, including \(\ell=\operatorname{char}\mathbf F_q\). The Artin–Schreier quotient \(\mathbf F_q/\wp(\mathbf F_q)\) therefore has \(p\) elements: directly, \(\ker\wp=\mathbf F_p\) and the finite additive group has cokernel of the same size.

## 7. Two further fields and the coefficient restriction

For \(K=\mathbf R\), the separable closure is \(\mathbf C\), and \(G_K=C_2\) acts by complex conjugation \(s\). Formula (6.2), written multiplicatively, gives

\[
H^2(\mathbf R,\mathbf C^\times)
=\mathbf R^\times/\{z\overline z:z\in\mathbf C^\times\}
=\mathbf R^\times/\mathbf R_{>0}
\simeq\mathbf Z/2\mathbf Z.
\tag{7.1}
\]

The nontrivial class has normalized cocycle \(c(s,s)=-1\), with all entries involving the identity equal to \(1\). The only nontrivial cocycle equation is \(s(-1)=-1\); replacing a normalized one-cochain's value at \(s\) by \(z\) multiplies \(c(s,s)\) by \(z\overline z\), which is positive. The associated multiplication on the real vector space \(\mathbf C\oplus\mathbf C u\) is specified by \(u z=\overline z u\), \(u^2=-1\). The cocycle equation makes it associative: products of three homogeneous terms have the two scalar factors in that equation. With \(I=i\) and \(J=u\) it satisfies \(I^2=J^2=-1\), \(JI=-IJ\), giving Hamilton's quaternion algebra. This is a concrete preview of lesson 9's Brauer interpretation, which we do not use in the proof of (7.1). For trivial \(\mathbf F_2\) coefficients, both operators in the cyclic complex are zero, so \(H^q(\mathbf R,\mathbf F_2)=\mathbf F_2\) in every degree. Thus \(\operatorname{cd}_2\mathbf R=\infty\).

Now let \(K=\mathbf C((t))\), the fraction field of the complete discrete valuation ring \(R=\mathbf C[[t]]\), let \(L/K\) be a finite extension, and let \(B\) be the integral closure of \(R\) in \(L\). We first check that \(B\) is a complete discrete valuation ring with fraction field \(L\) and residue field \(\mathbf C\). Since \(K\) has characteristic zero, \(L/K\) is separable, so \(B\) is a finite \(R\)-module ([Stacks, Tag 032L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-normal-domain-finite-separable-extension)). Every element of \(L\) is a quotient of an element of \(B\) by a nonzero element of \(R\): if \(x\) has minimal polynomial \(X^n+a_1X^{n-1}+\cdots+a_n\) over \(K\) and \(0\neq r\in R\) satisfies \(ra_i\in R\) for all \(i\), then \(rx\) is a root of \(X^n+ra_1X^{n-1}+\cdots+r^na_n\), whose coefficients lie in \(R\). The complete local ring \(R\) is henselian ([Stacks, Tag 04GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-complete-henselian)), so the finite \(R\)-algebra \(B\) is a finite product of local rings ([Stacks, Tag 04GG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-henselian)); since \(B\) is a domain, it is local. It is Noetherian and normal, and it has dimension one because it is integral over its subring \(R\) ([Stacks, Tag 00OK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-sub-dim-equal)). Hence \(B\) is a discrete valuation ring ([Stacks, Tag 00PD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-dvr)). The element \(t\) is not a unit of \(B\), since \(t^{-1}\notin R\) is not integral over the normal ring \(R\). Thus \(B/tB\) is a nonzero finite-dimensional local \(\mathbf C\)-algebra. Its residue field, the residue field of \(B\), is a finite extension of \(\mathbf C\) and therefore equals \(\mathbf C\); its maximal ideal is nilpotent, so \(\mathfrak m_B^N\subseteq tB\subseteq\mathfrak m_B\) for some \(N\). As a finite \(R\)-module, \(B\) is \(t\)-adically complete ([Stacks, Tag 00MA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-tensor)); hence \(B\) is complete for its \(\mathfrak m_B\)-adic topology. We give the remaining Puiseux argument.

Choose a uniformizer \(\pi\) of \(L\). Its residue field is \(\mathbf C\), and the inclusion \(\mathbf C\subset L\) supplies representatives of all residue classes. Successively subtracting the constant residue, dividing by \(\pi\), and repeating expresses each element of the valuation ring uniquely as \(\sum_{j\geq0}a_j\pi^j\), \(a_j\in\mathbf C\). Completeness gives convergence and uniqueness; allowing a finite negative initial part gives \(L=\mathbf C((\pi))\). Write \(t=u\pi^e\), where \(e>0\) and \(u\) is a unit.

The unit \(u\) has an \(e\)th root in \(L\). Its residue has such a root in \(\mathbf C\); the derivative \(eX^{e-1}\) is a unit at that root. Simple-root lifting in a complete discrete valuation ring follows directly by Newton iteration: if \(f(a)\) has valuation at least \(r>0\) and \(f'(a)\) is a unit, replace \(a\) by \(a-f(a)/f'(a)\). Taylor expansion makes the new error have valuation at least \(2r\), while the derivative stays a unit. The Cauchy sequence converges to a root with the original residue. Apply this to \(f=X^e-u\).

Set \(s=\pi u^{1/e}\). Then \(t=s^e\), \(s\) is also a uniformizer, and the same expansion argument gives \(L=\mathbf C((s))\). Grouping Laurent powers by their residues modulo \(e\) proves that \(1,s,\ldots,s^{e-1}\) are a basis over \(\mathbf C((s^e))\): it gives spanning and uniqueness coefficient by coefficient. Thus \([L:K]=e\), and every finite extension is, as a \(K\)-subfield of a chosen algebraic closure, \(\mathbf C((t^{1/e}))\). Any two choices of the root differ by an \(e\)th root of unity in \(\mathbf C\) and give the same subfield. Conversely these are cyclic Galois extensions, with automorphisms \(s\mapsto\zeta s\), \(\zeta\in\mu_e\).

Their directed union is an algebraic closure. In characteristic zero every finite extension is separable, and the preceding argument describes each of them. A polynomial over the union has its finitely many coefficients in one finite subextension; a root in an algebraic closure is algebraic over \(K\), hence belongs to another of the described finite subextensions and therefore to the union. This verifies algebraic closedness. With compatible choices of roots of \(t\), the Galois group is \(\varprojlim_e\mu_e\), whose transition maps are \(\zeta\mapsto\zeta^{e'/e}\) for \(e\mid e'\). Choosing the compatible primitive roots \(\exp(2\pi i/e)\) identifies this limit with \(\widehat{\mathbf Z}\). Hence

\[
\operatorname{cd}\mathbf C((t))=1.
\tag{7.2}
\]

Finally, the word *torsion* in Theorem 6.1 is indispensable. For any profinite \(G\), with trivial action on the coefficients, the sequence \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\) and Corollary 3.2 give

\[
H^2(G,\mathbf Z)
\simeq H^1(G,\mathbf Q/\mathbf Z)
=\operatorname{Hom}_{\mathrm{cont}}(G,\mathbf Q/\mathbf Z).
\tag{7.3}
\]

For \(G=\widehat{\mathbf Z}\) this is \(\mathbf Q/\mathbf Z\): evaluation at \(1\) determines a homomorphism, and each torsion value defines one through a finite cyclic quotient. Thus this profinite group has cohomological dimension one and still has nonzero degree-two cohomology for \(\mathbf Z\). The distinction follows from the definition of cohomological dimension.

## 8. Exercises

1. **Easy — Frobenius and Kummer.** Let \(n\) be prime to \(q\). Compute \(H^1(\mathbf F_q,\mu_n)\) directly from Frobenius, compute it from Kummer, and identify the boundary class of \(a\in\mathbf F_q^\times\).
2. **Medium — trivial coefficients and infinitely many classes.** Prove \(H^1(G,M)=\operatorname{Hom}_{\mathrm{cont}}(G,M)\) for a trivial discrete module. Show that \(H^1(\mathbf Q,\mathbf Z/2\mathbf Z)\) is infinite by exhibiting infinitely many linearly independent classes.
3. **Medium — dimension zero.** Define the supernatural order of \(G\) as the least common multiple of the orders of its finite quotients, recording unbounded prime valuations as infinity. Prove that \(\operatorname{cd}_\ell G=0\) if and only if \(\ell\) does not divide this order.
4. **Medium — Artin–Schreier as a sheaf sequence.** In characteristic \(p\), prove surjectivity of \(\wp\) on \(K^s\), verify the exact Artin–Schreier sequence on the small étale site, and explain why adjoining a root gives an étale cover over every field object. Recover both statements of (4.5).
5. **Hard — an integral coefficient warning.** Prove \(H^q(G,\mathbf Q)=0\) for \(q\geq1\) and trivial action, and prove (7.3) with its actual connecting map. Apply it to a finite-field absolute Galois group and explain why the result does not contradict its cohomological dimension.

## 9. Solutions

**Solution 1.** Choose a primitive \(n\)th root in the separable closure to identify the underlying group \(\mu_n\) with \(\mathbf Z/n\mathbf Z\). Arithmetic Frobenius acts by multiplication by \(q\). Formula (6.4) gives

\[
H^1(\mathbf F_q,\mu_n)
=(\mathbf Z/n\mathbf Z)/(q-1)(\mathbf Z/n\mathbf Z),
\tag{9.1}
\]

a cyclic group of order \(\gcd(n,q-1)\). Kummer gives \(\mathbf F_q^\times/\mathbf F_q^{\times n}\), also cyclic of that order because \(\mathbf F_q^\times\) is cyclic of order \(q-1\). For completeness, the multiplicative group of a finite field is cyclic: let \(m\) be the exponent of that finite abelian group. For each prime dividing \(m\), select an element whose order has the largest corresponding prime power and raise it to remove other prime factors. The product of these commuting elements has order \(m\). Every group element is a root of \(T^m-1\), so the group has at most \(m\) elements; since the constructed element has \(m\) distinct powers, it generates the group.

If \(b^n=a\), the boundary cocycle has value \(F(b)/b=b^{q-1}\) at Frobenius. This lies in \(\mu_n\), since \((b^{q-1})^n=a^{q-1}=1\). A different root \(b\zeta\) changes the value by \(\zeta^{q-1}\), precisely an element of \((F-1)\mu_n\) in multiplicative notation. Replacing \(a\) by \(a d^n\), \(d\in\mathbf F_q^\times\), leaves this value unchanged after choosing \(bd\). Conversely the kernel of the boundary is exactly the \(n\)th powers, by (4.3) and Hilbert 90. Thus the two cyclic-group descriptions agree through this explicit boundary, not merely through their orders.

**Solution 2.** A degree-one cocycle for a trivial action satisfies \(c(gh)=c(g)+c(h)\), and every degree-one coboundary is zero. The allowed cochains are continuous, so this proves the claimed equality. For \(K=\mathbf Q\), the two roots \(\pm1\) are rational, giving a trivial-module identification \(\mu_2=\mathbf Z/2\mathbf Z\). Kummer identifies the desired group with \(\mathbf Q^\times/\mathbf Q^{\times2}\). The classes of the positive rational primes are linearly independent over \(\mathbf F_2\): if a finite product \(\prod p^{\epsilon_p}\) is a square, its valuation at each \(p\) is even, so every \(\epsilon_p\in\{0,1\}\) is zero. There are infinitely many such primes and therefore infinitely many independent classes. Under the cocycle description, the class of \(p\) is the character \(g\mapsto g(\sqrt p)/\sqrt p\), with values identified with \(\mathbf Z/2\mathbf Z\).

**Solution 3.** Suppose every finite quotient has order prime to \(\ell\). We show that invariants are exact on \(\ell\)-primary modules. Given a surjection \(A\twoheadrightarrow B\) and \(b\in B^G\), choose a lift \(a\in A\). An open normal subgroup \(U\) fixes \(a\); put \(Q=G/U\). Then \(v=\sum_{g\in Q}ga\) is invariant and maps to \(|Q|b\). Choose \(r\) with \(\ell^r a=0\) and an integer \(k\) such that \(k|Q|\equiv1\pmod{\ell^r}\). The invariant \(kv\) maps to \(b\). Kernels are already preserved by invariants, so they are exact. The acyclic resolution (2.3) of an \(\ell\)-primary module has \(\ell\)-primary terms, since its continuous functions have finite image; its cycles and quotients are also \(\ell\)-primary. Applying the now exact invariants functor to that resolution gives zero positive cohomology, proving \(\operatorname{cd}_\ell G=0\).

Conversely, if some finite quotient has order divisible by \(\ell\), a Sylow pro-\(\ell\) subgroup \(P\) is nontrivial. A nonidentity element is detected in a finite quotient, so \(P\) has a nontrivial finite \(\ell\)-group quotient \(Q\). Every nontrivial finite \(\ell\)-group maps onto \(C_\ell\). To prove this, the class equation shows that its center has order divisible by \(\ell\). An element of that center has an appropriate power of order \(\ell\), giving a central subgroup \(Z\) of order \(\ell\). If \(Q/Z\) is nontrivial, induction on the group order supplies its quotient \(C_\ell\); compose the quotient maps. If \(Q/Z\) is trivial, then \(Q=Z=C_\ell\). Thus \(H^1(P,\mathbf F_\ell)=\operatorname{Hom}_{\mathrm{cont}}(P,\mathbf F_\ell)\neq0\). Equation (5.3) makes \(\operatorname{cd}_\ell G\geq\operatorname{cd}_\ell P\geq1\), proving the converse.

**Solution 4.** The polynomial \(T^p-T-a\) has derivative \(-1\); each of its irreducible factors is separable. Since \(K^s\) is separably closed, the polynomial has a root there, proving surjectivity of \(\wp\). Its zero fibre consists of exactly the prime field, since \(T^p-T\) already has those \(p\) distinct roots. The map is additive because \((x+y)^p=x^p+y^p\), and equivariant because the prime field is fixed. This verifies exactness of (4.6) as modules. The exact equivalence (1.2) then verifies

\[
0\longrightarrow\underline{\mathbf F_p}\longrightarrow\mathbf G_a
\xrightarrow{\wp}\mathbf G_a\longrightarrow0
\tag{9.2}
\]

as étale sheaves. One can also see the epimorphism locally without the equivalence: for \(a\in L\) on a field object, \(L[T]/(T^p-T-a)\) is finite free of rank \(p\), is étale by its unit derivative, and has nonempty spectrum, so gives an étale cover on which \(a\) is \(\wp(T)\). For a disjoint union of field objects do this on each component. The kernel consists of locally chosen prime-field constants, exactly the constant sheaf. Affine quasi-coherent vanishing kills all positive cohomology of \(\mathbf G_a\); the long exact sequence therefore gives \(K/\wp(K)\) in degree one and zero in every degree at least two. This conclusion uses neither perfection nor algebraic closedness of \(K^s\).

**Solution 5.** On a finite quotient, summing insertion contractions as in Corollary 3.2 annihilates \(H^q\) by the quotient's order. For rational coefficients the continuous cochain complex is \(\mathbf Q\)-linear, so its cohomology is a rational vector space; multiplication by a nonzero integer is invertible. Thus those positive cohomology groups are zero. Proposition 3.1 gives \(H^q(G,\mathbf Q)=0\) for all \(q>0\).

The long exact sequence of \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\) gives the isomorphism \(\delta:H^1(G,\mathbf Q/\mathbf Z)\to H^2(G,\mathbf Z)\), since its two adjacent rational cohomology groups vanish. For a continuous character \(\chi\), choose rational lifts of its finitely many values, taking the lift of zero to zero. This gives a continuous function \(b:G\to\mathbf Q\), and

\[
(db)(g,h)=b(h)-b(gh)+b(g)\in\mathbf Z
\tag{9.3}
\]

represents \(\delta(\chi)\), with the differential of (2.6). Changing the lifts changes this integral two-cocycle by an integral coboundary. Degree one with the trivial action is exactly continuous characters, by Solution 2. This proves (7.3) and its actual map. For \(G_{\mathbf F_q}=\widehat{\mathbf Z}\), evaluation at Frobenius identifies these characters with \(\mathbf Q/\mathbf Z\), as explained after (7.3). Thus \(H^2(\mathbf F_q,\mathbf Z)=\mathbf Q/\mathbf Z\neq0\). Cohomological dimension one controls torsion coefficient modules, and \(\mathbf Z\) is not a torsion module, so the assertions are compatible.

## 10. Dependencies and the next lesson

The earlier course proofs used here are the group-topos construction and finite-set compactness in lessons 1–2; acyclic resolutions, connecting maps and derived-functor comparison in lesson 3; affine quasi-coherent vanishing in lesson 5; geometric stalks and finite separable field fibres in lesson 6; and the precisely stated affine-transition continuity theorem and representable inverse image in lesson 7. Finite Galois theory, extension of separable embeddings, finite Sylow theory and elementary finite abelian groups are algebra prerequisites. Section 1 supplies the full finite-étale/Galois-set correspondence and the reconstruction of arbitrary sheaves.

For the \(\mathbf C((t))\) example, section 7 derives the structure of the finite extensions from cited results of commutative algebra and proves the uniformizer expansion, root lifting, finite-extension classification and Galois-group computation. None of the field-topos, cochain, Hilbert 90, Artin–Schreier or dimension proofs depends on this example. Section 5 proves the cohomological direction of Serre's criterion needed next. Lesson 9 will construct the algebraic Brauer group and identify it with \(H^2(K,(K^s)^\times)\); here Hamilton's algebra only illustrates a cocycle.

## 11. References

- **[Stacks, field topoi]** The Stacks Project Authors, *The Stacks Project*, [Tags 03QW–03QX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-galois-action-stalks) and [Tags 03QQ, 03QT, 04JM, 04JQ and 03QU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cohomology-point). Section 1 constructs both inverse equivalences on all sheaves and then compares the injective complexes.
- **[Stacks, group cohomology]** [Tags 0A2H, 04JP, 04JR, 0DVF and 0DV3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-group-cohomology) and [Tag 0DVG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-continuous-group-cohomology). Sections 2–3 prove the continuous acyclic resolution, derived comparison, finite-quotient formula, filtered-colimit compatibility and positive-degree torsion.
- **[Stacks, fields and characteristic \(p\)]** [Tags 0A2M and 03R8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-galois-cohomology), [Tags 0A3J–0A3K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-artin-schreier), and [Tags 0F0P–0F0Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cd). Sections 4–6 supply the field calculations and the subgroup and Sylow arguments needed to extend constant-coefficient vanishing to cohomological dimension. The characteristic-\(p\) assertion is about \(\operatorname{cd}_pG_K\) for every field; this fixes the convention where other conventions for the dimension of a field require perfection.
- **[Stacks, complete discrete valuation rings]** [Tag 032L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-normal-domain-finite-separable-extension), [Tag 04GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-complete-henselian), [Tag 04GG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-henselian), [Tag 00OK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-sub-dim-equal), [Tag 00PD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-dvr) and [Tag 00MA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-tensor), used in section 7 for the finite extensions of \(\mathbf C((t))\).
- **[Milne, ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), [free from the author](https://www.jmilne.org/math/CourseNotes/ANT.pdf). Chapter 7 treats valuations and extensions of complete discretely valued fields.

The linked AI Integrated Stacks Project reader contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/). The original exposition, proofs, examples and exercises in this lesson are dedicated to CC0; the cited books retain their own copyrights.
