# Γ-sets and algebras over the sphere

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

In the lessons on monoids and monoid schemes the field with one element is the monoid \(\mathbb F_1=\{0,1\}\): one forgets the addition of a ring and keeps its multiplication. This lesson describes a base that lies below the integers and still remembers addition. The base is the functor \(\mathbb S\) that sends a finite pointed set to itself. The objects over it are the *Γ-sets*: functors \(F\) from finite pointed sets to pointed sets that send a point to a point. A Γ-set consists of a set \(F(1_+)\) and of a record of which finite families of its elements can be added, and with which results. For an abelian group every family has exactly one sum. For \(\mathbb S\) a family has a sum only when at most one of its members is not zero. Between these two cases lie the unit balls of normed rings, where a family can be added when the sum of the norms of its members is at most \(1\), and the quotients of rings by groups of units, where a sum can have several values.

An *\(\mathbb S\)-algebra* is a Γ-set with a multiplication. Monoids, semirings and rings become \(\mathbb S\)-algebras, and this changes none of their morphisms (Theorems 4.1, 4.3 and 4.4). The \(\mathbb S\)-algebra of the monoid \(\mathbb F_1\) is \(\mathbb S\) itself. It is the initial \(\mathbb S\)-algebra and the unit of the smash product, so it plays for \(\mathbb S\)-algebras the role that \(\mathbb Z\) plays for rings. Three results show what this base achieves.

- The smash square of the integers over \(\mathbb S\) is not the integers (Theorem 4.7). For generalized rings the tensor square of \(\mathbb Z\) over \(\mathbb F_1\) is \(\mathbb Z\) again; see *Generalized rings*.
- The local ring at the archimedean place exists as an \(\mathbb S\)-algebra. It is the unit ball \(\{(q_j):\sum|q_j|\le1\}\) of the rational numbers, and it extends the structure sheaf of \(\operatorname{Spec}\mathbb Z\) to the compactification \(\overline{\operatorname{Spec}\mathbb Z}\) (Section 6). It is the unit ball monad of [Durov 2007] in another form (Theorem 6.3, Example 6.4).
- For divisors on \(\overline{\operatorname{Spec}\mathbb Z}\) there is a Riemann–Roch theorem in which the two cohomologies have integer dimensions (Theorem 8.9).

Sections 1–3 define Γ-sets, the smash product, \(\mathbb S\)-algebras and their modules. Section 4 treats the functors from monoids, semirings and rings, the base changes between them, and the reasons why \(\mathbb S\) plays the role of \(\mathbb F_1\). Section 5 explains sums with several values and the link with hyperrings. Section 6 treats the archimedean place. Section 7 constructs the spectrum of an \(\mathbb S\)-algebra following [Connes–Consani 2021]. Section 8 proves the Riemann–Roch theorem of [Connes–Consani 2023] from its definitions.

The lesson assumes categories, functors, natural transformations and the Yoneda lemma, and also commutative rings, their prime spectra and sheaves on a topological space. The smash product of Γ-sets is a Day convolution; the lesson constructs it from the definition, so no knowledge of Day convolution is needed. The lesson builds on *Commutative monoids and their spectra*, from which it takes monoids, prime ideals, the open sets \(D(f)\) and localization. Section 8 uses the adèles of \(\mathbb Q\) in one proof and recalls what it needs. Basic references are [Connes–Consani 2016a], [Connes–Consani 2021] and [Connes–Consani 2023]. In homotopy theory simplicial Γ-sets are the Γ-spaces of [Segal 1974]. They model connective spectra, and \(\mathbb S\) corresponds to the sphere spectrum [Segal 1974]. This explains the title. The lesson uses no homotopy theory.

## 1. Γ-sets

### Conventions

Rings are commutative with 1. Semirings are commutative, with 0 and 1, and 0 is absorbing. A *monoid* is a commutative monoid written multiplicatively, with a unit 1 and an absorbing element 0; morphisms preserve 1 and 0. The monoid \(\mathbb F_1\) is \(\{0,1\}\), and \(\mathbb F_{1^n}=\{0\}\cup\mu_n\) with \(\mu_n\) the group of \(n\)-th roots of unity. An *additive monoid* is a set with a commutative and associative operation \(+\) and a neutral element 0, for example the additive structure of a semiring.

A *pointed set* is a set with a chosen base point, written \(\ast\), or 0 when the set is a monoid or a semiring. Maps of pointed sets preserve base points. For a pointed set \(X\) we write \(X^\circ=X\setminus\{\ast\}\). For \(k\ge0\) let \(k_+=\{0,1,\dots,k\}\) with base point 0. The *wedge* \(X\vee Y\) is the disjoint union of \(X\) and \(Y\) with the two base points identified. The *smash product* \(X\wedge Y\) is the quotient of \(X\times Y\) in which all pairs \((x,\ast)\) and \((\ast,y)\) become the base point; the class of \((x,y)\) is written \(x\wedge y\), and \((X\wedge Y)^\circ=X^\circ\times Y^\circ\). The smash product is associative and commutative up to canonical bijections, and \(1_+\wedge X=X=X\wedge1_+\). We use these identifications without comment. A *zero map* sends every element to the base point.

Let \(\mathrm{Fin}_\ast\) be a small category of finite pointed sets that contains every \(k_+\) and is closed under \(\vee\) and \(\wedge\) (for instance the hereditarily finite pointed sets). Every finite pointed set is isomorphic to exactly one \(k_+\). For a finite set \(J\) we write \(J_+=J\sqcup\{\ast\}\). If \(J_+\) is not an object of \(\mathrm{Fin}_\ast\), a functor on \(\mathrm{Fin}_\ast\) is applied to \(J_+\) through a bijection of \(J\) with \(\{1,\dots,k\}\); the statements below do not depend on the bijection. For \(X\) in \(\mathrm{Fin}_\ast\) we use three kinds of maps:
\[
\hat x:1_+\to X,\ 1\mapsto x\quad(x\in X);\qquad
\delta_x:X\to1_+,\ \delta_x(y)=\begin{cases}1&y=x\\0&y\ne x\end{cases}\quad(x\in X^\circ);\qquad
\sigma_X:X\to1_+,\ \sigma_X(y)=1\ \ (y\in X^\circ).
\]

### Definition and first examples

**Definition 1.1.** A *Γ-set* is a functor \(F:\mathrm{Fin}_\ast\to\mathrm{Set}_\ast\) to pointed sets such that \(F(0_+)\) has one element. A morphism of Γ-sets is a natural transformation. The category of Γ-sets is written \(\Gamma\mathrm{Set}\).

The name comes from the category Γ of [Segal 1974], whose opposite is equivalent to \(\mathrm{Fin}_\ast\). Definition 1.1 is [Connes–Consani 2016a, Definition 2.1]. Following [Connes–Consani 2021, §5.2] we call \(F(k_+)\) the *\(k\)-th level* of \(F\); the first level is \(F(1_+)\). In [Connes–Consani 2016a, §5.3] level 1 and level 2 mean the restrictions of \(F\) to the pointed sets with at most two and at most three elements. Three remarks follow at once. A zero map factors through \(0_+\), so a Γ-set sends zero maps to zero maps. The constant functor with value a point, written \(\ast\), is both initial and terminal in \(\Gamma\mathrm{Set}\), so every pair of Γ-sets has a zero morphism. A Γ-set is determined, up to a unique isomorphism, by its restriction to the objects \(k_+\).

**Example 1.2.** (a) The inclusion functor \(\mathbb S(X)=X\) is a Γ-set.

(b) For a pointed set \(P\), the functor \(P\wedge\mathbb S:X\mapsto P\wedge X\) is a Γ-set. For \(P=n_+\) it is the wedge of \(n\) copies of \(\mathbb S\).

(c) Let \(A\) be an additive monoid. Put
\[
HA(X)=\{\varphi:X\to A\ \text{with}\ \varphi(\ast)=0\},\qquad
(HA(f)\varphi)(y)=\sum_{x\in f^{-1}(y)}\varphi(x)\quad(f:X\to Y,\ y\in Y^\circ).
\tag{1.1}
\]
The base point of \(HA(X)\) is \(\varphi=0\), and an empty sum is 0. The values \(\varphi(x)\) at the points \(x\) with \(f(x)=\ast\) are dropped. For \(g:Y\to Z\) and \(z\in Z^\circ\), the points \(x\) with \(g(f(x))=z\) are those with \(f(x)=y\) for some \(y\in g^{-1}(z)\), so \(HA(g\circ f)=HA(g)\circ HA(f)\). Also \(HA(0_+)=\{0\}\). So \(HA\) is a Γ-set, with \(HA(k_+)=A^k\). For the Boolean semiring \(\mathbb B=\{0,1\}\), \(1+1=1\), the set \(H\mathbb B(X)\) is the set of subsets of \(X^\circ\) and \(H\mathbb B(f)\) sends a subset \(T\) to \(f(T)\cap Y^\circ\), the direct image without the base point [Connes–Consani 2016a, Lemma 4.1]. For the field \(\mathbb F_2\) the sets are the same, but \(H\mathbb F_2(f)\) sends a subset \(T\) to the set of those \(y\) for which \(T\cap f^{-1}(y)\) has an odd number of elements [Connes–Consani 2016a, Remark 4.2].

(d) A *sub-Γ-set* of \(F\) is a choice of pointed subsets \(G(X)\subseteq F(X)\) with \(F(f)(G(X))\subseteq G(Y)\) for all \(f:X\to Y\). The product \(F\times G\) is defined objectwise. For \(Z\) in \(\mathrm{Fin}_\ast\) the *shift* \(F_Z(X)=F(X\wedge Z)\) is a Γ-set, because \(0_+\wedge Z\) is a point.

**Lemma 1.3** (Yoneda). Let \(P\) be a pointed set and \(F\) a Γ-set. The map \(\theta\mapsto\theta_{1_+}\) is a bijection from \(\operatorname{Hom}(P\wedge\mathbb S,F)\) to the set of pointed maps \(P\to F(1_+)\). The morphism that corresponds to \(t:P\to F(1_+)\) is \(\theta_X(p\wedge x)=F(\hat x)(t(p))\). In particular \(\operatorname{Hom}(\mathbb S,F)=F(1_+)\).

**Proof.** Let \(t\) be given. The formula is well defined on \(P\wedge X\): if \(p=\ast\) then \(t(p)=\ast\), and if \(x=\ast\) then \(\hat x\) is a zero map. It is natural because \(F(f)F(\hat x)=F(\widehat{f(x)})\). Its value on \(1_+\) is \(t\). Conversely, a morphism \(\theta\) satisfies \(\theta_X(p\wedge x)=\theta_X((P\wedge\hat x)(p\wedge1))=F(\hat x)(\theta_{1_+}(p))\), so it is determined by \(\theta_{1_+}\). \(\square\)

### Components and sums

**Definition 1.4.** Let \(F\) be a Γ-set, \(X\) in \(\mathrm{Fin}_\ast\) and \(\xi\in F(X)\). The *components* of \(\xi\) are the elements \(\xi_x=F(\delta_x)(\xi)\in F(1_+)\), \(x\in X^\circ\). The *total* of \(\xi\) is \(\operatorname{tot}\xi=F(\sigma_X)(\xi)\in F(1_+)\). The *Segal map* is
\[
s_X:F(X)\to F(1_+)^{X^\circ},\qquad\xi\mapsto(\xi_x)_{x\in X^\circ}.
\]
An element \(\xi\) with \(s_X(\xi)=(a_x)\) is a *witness* for the family \((a_x)\), and \(\operatorname{tot}\xi\) is then called *a sum* of the family.

**Example 1.5.** (a) In \(HA\) the components of \(\varphi\) are its values and \(\operatorname{tot}\varphi=\sum_x\varphi(x)\). The Segal maps are bijective: every family has exactly one witness and one sum, the sum in \(A\).

(b) In \(\mathbb S\) the element \(x\in X^\circ\) has components \(\delta_y(x)\), so exactly one component is 1 and the others are 0; its total is 1. The base point has all components 0. Hence a family in \(\mathbb S(1_+)=\{0,1\}\) has a witness exactly when at most one of its members is 1. The Γ-set \(\mathbb S\) knows the sums \(a+0+\dots+0=a\) and no others.

(c) For a sub-Γ-set \(G\subseteq HA\) the Segal maps are injective. A family of elements of \(G(1_+)\) has at most one sum in \(G\), and it has one exactly when the family, seen as an element of \(HA(X)\), lies in \(G(X)\). The addition of \(A\) becomes a partially defined addition.

So a Γ-set is a set \(F(1_+)\) together with, for every finite family of its elements, the set of its witnesses: there may be none, one or several, and different witnesses can have the same total. The next theorem says that additive monoids are exactly the Γ-sets in which every finite family has exactly one witness, that is, in which all Segal maps are bijective. Uniqueness of the total alone is not enough: in the Γ-set \(Q\) with \(Q(X)\) the base point together with the two-element subsets of \(X^\circ\), where a pointed map sends a subset to its image if that image consists of two elements other than the base point and to the base point otherwise, every family in \(Q(1_+)=\{0\}\) has the single total \(0\), but \(Q(2_+)\) has two elements, so the Segal map \(s_{2_+}\) is not injective.

**Theorem 1.6** (Additive monoids among Γ-sets). (1) For additive monoids \(A\) and \(B\), the map \(u\mapsto H(u)\), \(H(u)_X(\varphi)=u\circ\varphi\), is a bijection from the additive maps \(A\to B\) to \(\operatorname{Hom}(HA,HB)\).

(2) A Γ-set \(F\) is isomorphic to \(HA\) for some additive monoid \(A\) if and only if all its Segal maps are bijective. In that case \(A=F(1_+)\), and \(a+b\) is the total of the element of \(F(2_+)\) with components \((a,b)\).

*Reference:* for semirings, part (1) is in [Connes–Consani 2016a, Proposition 3.5]. The condition in (2) is the one that [Segal 1974] imposes on Γ-spaces, up to homotopy.

**Proof.** (1) An additive map \(u\) commutes with finite sums and sends 0 to 0, so \(H(u)\) is natural. It determines \(u=H(u)_{1_+}\). Let \(\rho:HA\to HB\) be a morphism and \(u=\rho_{1_+}:A\to B\), a pointed map. Naturality for \(\delta_x\) gives \((\rho_X\varphi)(x)=u(\varphi(x))\) for \(\varphi\in HA(X)\), so \(\rho_X(\varphi)=u\circ\varphi\). Naturality for \(\sigma_{2_+}\), applied to \(\varphi=(a,b)\in HA(2_+)\), gives \(u(a+b)=u(a)+u(b)\). So \(u\) is additive and \(\rho=H(u)\).

(2) The Segal maps of \(HA\) are bijective, and this property passes to isomorphic Γ-sets. Conversely let all Segal maps of \(F\) be bijective. Put \(A=F(1_+)\) and write 0 for its base point. For \(a,b\in A\) let \(\xi(a,b)\in F(2_+)\) be the element with components \((a,b)\), and put \(a+b=\operatorname{tot}\xi(a,b)\). For a subset \(T\subseteq X^\circ\) let \(\chi_T:X\to1_+\) send the points of \(T\) to 1 and all other points to 0. So \(\chi_{\{x\}}=\delta_x\), \(\chi_{X^\circ}=\sigma_X\), and \(\chi_\emptyset\) is a zero map.

*Commutativity and neutral element.* Let \(\tau\) exchange 1 and 2 in \(2_+\). Then \(\delta_1\tau=\delta_2\) and \(\delta_2\tau=\delta_1\), so \(F(\tau)\xi(a,b)=\xi(b,a)\), and \(\sigma\tau=\sigma\) gives \(b+a=a+b\). Let \(\iota:1_+\to2_+\), \(\iota(1)=2\). Then \(\delta_1\iota\) is a zero map and \(\delta_2\iota\) is the identity, so \(F(\iota)(a)=\xi(0,a)\), and \(\sigma\iota=\mathrm{id}\) gives \(0+a=a\).

*A formula.* Let \(\xi\in F(X)\), \(T\subseteq X^\circ\) and \(t\in X^\circ\setminus T\). Then
\[
F(\chi_{T\cup\{t\}})(\xi)=F(\chi_T)(\xi)+\xi_t.
\tag{1.2}
\]
Indeed, let \(p:X\to2_+\) send \(T\) to 1, \(t\) to 2 and all other points to 0. Then \(\delta_1p=\chi_T\), \(\delta_2p=\delta_t\) and \(\sigma p=\chi_{T\cup\{t\}}\). So \(F(p)\xi=\xi(F(\chi_T)\xi,\xi_t)\), and applying \(F(\sigma)\) gives (1.2).

*Associativity.* Let \(\xi\in F(3_+)\) have components \((a,b,c)\). Two uses of (1.2) give \(F(\chi_{\{1,2,3\}})\xi=(a+b)+c\), adding first 2 and then 3 to \(T=\{1\}\). They also give \(F(\chi_{\{1,2,3\}})\xi=(b+c)+a\), adding first 3 and then 1 to \(T=\{2\}\). With commutativity, \((a+b)+c=a+(b+c)\).

So \(A\) is an additive monoid, and (1.2) gives by induction on the size of \(T\) that \(F(\chi_T)(\xi)=\sum_{x\in T}\xi_x\); for empty \(T\) both sides are 0. Now let \(f:X\to Y\) and \(y\in Y^\circ\). Since \(\delta_yf=\chi_{f^{-1}(y)}\),
\[
(F(f)\xi)_y=F(\chi_{f^{-1}(y)})(\xi)=\sum_{x\in f^{-1}(y)}\xi_x .
\]
By (1.1) this says that the Segal maps form a morphism \(F\to HA\). It is bijective on every \(X\), so it is an isomorphism. \(\square\)

## 2. The smash product and its unit

A reference for this section is [Connes–Consani 2016a, §2].

**Definition 2.1.** Let \(F,G,E\) be Γ-sets. A *pairing* \(\beta:(F,G)\to E\) is a family of pointed maps
\[
\beta_{X,Y}:F(X)\wedge G(Y)\to E(X\wedge Y)
\]
that is natural in \(X\) and in \(Y\): \(E(f\wedge g)\beta_{X,Y}(a\wedge b)=\beta_{X',Y'}(F(f)a\wedge G(g)b)\) for \(f:X\to X'\) and \(g:Y\to Y'\). A *triple pairing* \((F,G,H)\to E\) is a family of pointed maps \(F(X)\wedge G(Y)\wedge H(Z)\to E(X\wedge Y\wedge Z)\) natural in the three variables.

Pairings are the bilinear maps of this theory. The smash product is the Γ-set that represents them, as the tensor product represents bilinear maps.

**Proposition 2.2** (The smash product). For Γ-sets \(F\) and \(G\) there are a Γ-set \(F\wedge G\) and a pairing \(u:(F,G)\to F\wedge G\) such that every pairing \(\beta:(F,G)\to E\) is \(\bar\beta\circ u\) for a unique morphism \(\bar\beta:F\wedge G\to E\). The pair \((F\wedge G,u)\) is unique up to a unique isomorphism.

**Proof.** For \(Z\) in \(\mathrm{Fin}_\ast\) consider the tuples \((X,Y,v,a,b)\) with \(X,Y\) in \(\mathrm{Fin}_\ast\), \(v:X\wedge Y\to Z\), \(a\in F(X)\) and \(b\in G(Y)\). Let \(\sim\) be the equivalence relation generated by
\[
(X,Y,v'\circ(f\wedge g),a,b)\sim(X',Y',v',F(f)a,G(g)b)\qquad(f:X\to X',\ g:Y\to Y',\ v':X'\wedge Y'\to Z).
\tag{2.1}
\]
Let \((F\wedge G)(Z)\) be the set of classes \([X,Y,v,a,b]\), and let \(h:Z\to Z'\) act by \(v\mapsto h\circ v\), which respects (2.1).

*Base point.* Every tuple with \(a=\ast\) or \(b=\ast\) lies in the class of \((0_+,0_+,0,\ast,\ast)\). For \(a=\ast\): with \(f:0_+\to X\) and \(g=\mathrm{id}\), (2.1) gives \((X,Y,v,\ast,b)\sim(0_+,Y,v\circ(f\wedge\mathrm{id}),\ast,b)\). The map \(v\circ(f\wedge\mathrm{id})\) is defined on the point \(0_+\wedge Y\), so it equals \(v''\circ(\mathrm{id}\wedge g')\) for \(g':Y\to0_+\) and \(v'':0_+\wedge0_+\to Z\), and (2.1) gives \((0_+,Y,v''(\mathrm{id}\wedge g'),\ast,b)\sim(0_+,0_+,v'',\ast,\ast)\). The case \(b=\ast\) is symmetric. We take this class as base point. If \(Z=0_+\), every \(v\) factors as \(v''\circ(f\wedge g)\) with \(f:X\to0_+\) and \(g:Y\to0_+\), so every tuple is equivalent to the base point. Hence \(F\wedge G\) is a Γ-set.

*The pairing.* Put \(u_{X,Y}(a\wedge b)=[X,Y,\mathrm{id},a,b]\). It is pointed by the last paragraph. It is natural: \((F\wedge G)(f\wedge g)[X,Y,\mathrm{id},a,b]=[X,Y,f\wedge g,a,b]=[X',Y',\mathrm{id},F(f)a,G(g)b]\) by (2.1).

*Universal property.* Given \(\beta\), put \(\bar\beta_Z[X,Y,v,a,b]=E(v)(\beta_{X,Y}(a\wedge b))\). The two sides of (2.1) have the same image, because \(E(v')E(f\wedge g)\beta_{X,Y}(a\wedge b)=E(v')\beta_{X',Y'}(F(f)a\wedge G(g)b)\). So \(\bar\beta\) is well defined. It is natural in \(Z\), pointed, and \(\bar\beta\circ u=\beta\). It is unique because \([X,Y,v,a,b]=(F\wedge G)(v)(u_{X,Y}(a\wedge b))\). Uniqueness of \((F\wedge G,u)\) follows from the universal property. \(\square\)

In other words \((F\wedge G)(Z)\) is the colimit of the sets \(F(X)\wedge G(Y)\) over all maps \(X\wedge Y\to Z\). This is Day's convolution product for the category \(\mathrm{Fin}_\ast\) with its smash product. Exchanging the two factors shows \(F\wedge G\cong G\wedge F\). The value \((F\wedge G)(1_+)\) is in general much bigger than \(F(1_+)\wedge G(1_+)\): by [Connes–Consani 2016a, Corollary 4.10] the set \((H\mathbb B\wedge H\mathbb B)(1_+)\) is infinite. In one case the smash product is computed objectwise.

**Proposition 2.3** (Smash product with \(P\wedge\mathbb S\)). Let \(P\) be a pointed set and \(F\) a Γ-set. Let \(P\wedge F\) be the Γ-set \(X\mapsto P\wedge F(X)\). For \(x\in X\) and \(b\in F(Y)\) put \(x\otimes b=F(\hat x\wedge\mathrm{id}_Y)(b)\in F(X\wedge Y)\). Then
\[
(P\wedge X)\wedge F(Y)\to P\wedge F(X\wedge Y),\qquad(p\wedge x)\wedge b\mapsto p\wedge(x\otimes b),
\]
is a pairing \((P\wedge\mathbb S,F)\to P\wedge F\), and it has the universal property of Proposition 2.2. So \((P\wedge\mathbb S)\wedge F\cong P\wedge F\). In particular \(\mathbb S\wedge F\cong F\): the Γ-set \(\mathbb S\) is a unit for the smash product.

**Proof.** Let \(\beta:(P\wedge\mathbb S,F)\to E\) be a pairing. Its restriction to \(X=1_+\) is a family of pointed maps \(\gamma_Y:P\wedge F(Y)\to E(Y)\), natural in \(Y\), that is, a morphism \(\gamma:P\wedge F\to E\). Since \(p\wedge x=(P\wedge\hat x)(p\wedge1)\), naturality in \(X\) gives
\[
\beta_{X,Y}((p\wedge x)\wedge b)=E(\hat x\wedge\mathrm{id}_Y)(\gamma_Y(p\wedge b)).
\tag{2.2}
\]
So \(\beta\) is determined by \(\gamma\). Conversely, for any morphism \(\gamma:P\wedge F\to E\), formula (2.2) defines a pairing. It is well defined because \(\gamma\) is pointed and \(\hat x\wedge\mathrm{id}\) is a zero map for \(x=\ast\). It is natural in \(Y\) because \(\gamma\) is, and natural in \(X\) because \((f\wedge\mathrm{id})(\hat x\wedge\mathrm{id})=\widehat{f(x)}\wedge\mathrm{id}\). For \(\gamma=\mathrm{id}\) it is the pairing of the statement, and \(\beta=\gamma\circ(\text{this pairing})\) in general. \(\square\)

**Proposition 2.4** (Triple pairings). Let \(F,G,H,E\) be Γ-sets. Composition with \(u\) is a bijection from the pairings \((F\wedge G,H)\to E\) to the triple pairings \((F,G,H)\to E\), and likewise for the pairings \((F,G\wedge H)\to E\). Hence \((F\wedge G)\wedge H\) and \(F\wedge(G\wedge H)\) are canonically isomorphic.

**Proof.** Let \(t\) be a triple pairing. Fix \(Z\) and \(c\in H(Z)\). Then \(a\wedge b\mapsto t(a\wedge b\wedge c)\) is a pairing \((F,G)\to E_Z\) into the shift of \(E\). By Proposition 2.2 it is \(b_c\circ u\) for a unique morphism \(b_c:F\wedge G\to E_Z\). Put \(\beta_{W,Z}(w\wedge c)=(b_c)_W(w)\). This is pointed: \(b_c(\ast)=\ast\), and \(b_\ast\) is the zero morphism. It is natural in \(W\) because \(b_c\) is a morphism. It is natural in \(Z\): for \(g:Z\to Z'\) the morphisms \(E(-\wedge g)\circ b_c\) and \(b_{H(g)c}\) from \(F\wedge G\) to \(E_{Z'}\) agree after composition with \(u\), since \(t\) is natural in \(Z\); so they are equal. Thus \(\beta\) is a pairing with \(\beta(u(a\wedge b)\wedge c)=t(a\wedge b\wedge c)\). A pairing \(\beta\) with this property is unique, because each \(\beta(-\wedge c)\) is determined by its composite with \(u\). The second case is symmetric. Both \((F\wedge G)\wedge H\) and \(F\wedge(G\wedge H)\) therefore represent triple pairings, and two representing objects are canonically isomorphic. \(\square\)

The same argument works with any number of factors: all ways of bracketing a smash product of \(n\) Γ-sets represent the \(n\)-fold pairings. With these isomorphisms, the isomorphisms \(\mathbb S\wedge F\cong F\) of Proposition 2.3 and the exchange \(F\wedge G\cong G\wedge F\), the category \((\Gamma\mathrm{Set},\wedge,\mathbb S)\) is symmetric monoidal. Each coherence condition compares two isomorphisms between objects that represent the same pairings, and both respect the universal pairings; such an isomorphism is unique. For the conditions that contain \(\mathbb S\) one uses that the triple pairings \(t:(F,\mathbb S,G)\to E\) correspond to the pairings \(\beta:(F,G)\to E\), by \(\beta(a\wedge b)=t(a\wedge1\wedge b)\) and \(t(a\wedge x\wedge b)=E(\mathrm{id}\wedge\hat x\wedge\mathrm{id})(\beta(a\wedge b))\), as in the proof of Proposition 2.3; so \((F\wedge\mathbb S)\wedge G\) and \(F\wedge(\mathbb S\wedge G)\) represent the pairings \((F,G)\to E\), as \(F\wedge G\) does. The category is also closed:

**Proposition 2.5** (Inner Hom). For Γ-sets \(G\) and \(E\) let \(\underline{\operatorname{Hom}}(G,E)\) be the Γ-set \(X\mapsto\operatorname{Hom}(G,E_X)\), where \(E_X(Y)=E(X\wedge Y)\) is the shift of Example 1.2(d), with the fixed factor written on the left. Then the pairings \((F,G)\to E\) correspond to the morphisms \(F\to\underline{\operatorname{Hom}}(G,E)\), by \(\beta\mapsto(a\mapsto\beta(a\wedge-))\). Hence \(\operatorname{Hom}(F\wedge G,E)=\operatorname{Hom}(F,\underline{\operatorname{Hom}}(G,E))\).

**Proof.** A map \(f:X\to X'\) induces the morphism \(E(f\wedge-):E_X\to E_{X'}\), which makes \(\underline{\operatorname{Hom}}(G,E)\) a functor; its value at \(0_+\) is a point because \(E_{0_+}=\ast\). Let \(\beta\) be a pairing and \(a\in F(X)\). Naturality of \(\beta\) in \(Y\) says that \(\beta(a\wedge-)\) is a morphism \(G\to E_X\). Naturality in \(X\) says that \(a\mapsto\beta(a\wedge-)\) is natural in \(X\). It is pointed because \(\beta(\ast\wedge b)=\ast\). Conversely a morphism \(\theta:F\to\underline{\operatorname{Hom}}(G,E)\) gives the pairing \(\beta(a\wedge b)=\theta_X(a)_Y(b)\), and the two constructions are inverse to each other. \(\square\)

This formula for the inner Hom is [Connes–Consani 2016a, §2.1], where the closed monoidal structure is quoted from work of Lydakis.

## 3. \(\mathbb S\)-algebras and their modules

**Definition 3.1.** An *\(\mathbb S\)-algebra* is a Γ-set \(A\) with a pairing \(\mu:(A,A)\to A\) and an element \(1\in A(1_+)\) such that, with the notation \(a\cdot b=\mu_{X,Y}(a\wedge b)\in A(X\wedge Y)\) for \(a\in A(X)\) and \(b\in A(Y)\),
\[
(a\cdot b)\cdot c=a\cdot(b\cdot c)\ \text{ in }A(X\wedge Y\wedge Z),\qquad1\cdot a=a=a\cdot1\ \text{ in }A(X).
\]
It is *commutative* if \(b\cdot a=A(\tau)(a\cdot b)\), where \(\tau:X\wedge Y\to Y\wedge X\) exchanges the factors. A morphism of \(\mathbb S\)-algebras is a morphism \(\rho\) of Γ-sets with \(\rho(1)=1\) and \(\rho(a\cdot b)=\rho(a)\cdot\rho(b)\). A *sub-\(\mathbb S\)-algebra* is a sub-Γ-set that contains 1 and is closed under products.

By Propositions 2.2–2.4 and Lemma 1.3, such a structure is the same as morphisms \(A\wedge A\to A\) and \(\mathbb S\to A\) that satisfy the associativity and unit laws of a monoid in \((\Gamma\mathrm{Set},\wedge,\mathbb S)\). This is the definition of [Connes–Consani 2016a, Definition 2.2]. *From now on all \(\mathbb S\)-algebras are commutative, except in Theorem 6.3.*

**Example 3.2.** (a) \(\mathbb S\) is an \(\mathbb S\)-algebra: \(\mu\) is the identity of \(X\wedge Y\) and \(1\in1_+\).

(b) Let \(M\) be a monoid. The Γ-set \(\mathbb SM=M\wedge\mathbb S\) with
\[
(m\wedge x)\cdot(n\wedge y)=mn\wedge(x\wedge y),\qquad1=1\wedge1,
\]
is an \(\mathbb S\)-algebra, the *spherical monoid algebra* of \(M\) [Connes–Consani 2016a, Proposition 3.2]. Its first level is \(\mathbb SM(1_+)=M\). For \(M=\mathbb F_1\) we get \(\mathbb S\mathbb F_1=\mathbb S\). We write \(\mathbb S[\mu_n]=\mathbb S\mathbb F_{1^n}\), \(\mathbb S[\pm1]=\mathbb S\mathbb F_{1^2}\), and \(\mathbb S[T]=\mathbb SM\) for the free monoid \(M=\{0,1,T,T^2,\dots\}\).

(c) Let \(R\) be a semiring. The Γ-set \(HR\) with
\[
(\varphi\cdot\psi)(x\wedge y)=\varphi(x)\psi(y),\qquad1\in R=HR(1_+),
\]
is an \(\mathbb S\)-algebra [Connes–Consani 2016a, Lemma 3.4]. The product is a pairing because multiplication in \(R\) distributes over finite sums and \(0\) is absorbing:
\[
\sum_{f(x)=x',\ g(y)=y'}\varphi(x)\psi(y)=\Big(\sum_{f(x)=x'}\varphi(x)\Big)\Big(\sum_{g(y)=y'}\psi(y)\Big).
\]

(d) Products of \(\mathbb S\)-algebras are \(\mathbb S\)-algebras. The Γ-set \(\ast\) is the *zero* \(\mathbb S\)-algebra; it is \(H\) of the zero ring, and the only \(\mathbb S\)-algebra with \(1=\ast\).

**Lemma 3.3.** Let \(A\) be an \(\mathbb S\)-algebra.

1. The set \(A(1_+)\) is a monoid under the product, with unit 1 and absorbing element \(\ast\). It acts on every \(A(X)=A(1_+\wedge X)\), and \(A(f)(a\cdot\xi)=a\cdot A(f)(\xi)\) for \(a\in A(1_+)\), \(\xi\in A(X)\) and \(f:X\to Y\).
2. (Distributivity.) For \(\xi\in A(X)\) and \(\eta\in A(Y)\), the components and the total of the product are \((\xi\cdot\eta)_{x\wedge y}=\xi_x\eta_y\) and \(\operatorname{tot}(\xi\cdot\eta)=\operatorname{tot}(\xi)\operatorname{tot}(\eta)\).
3. The map \(x\mapsto A(\hat x)(1)\) is the only morphism of \(\mathbb S\)-algebras \(\mathbb S\to A\). So \(\mathbb S\) is the initial \(\mathbb S\)-algebra.

**Proof.** (1) Since \(1_+\wedge1_+=1_+\), the product is an associative operation on \(A(1_+)\) with unit 1. It is commutative because the exchange map of \(1_+\wedge1_+\) is the identity. The base point is absorbing because \(\mu\) is defined on a smash product. The last formula is the naturality of \(\mu\) in its second variable.

(2) Apply the naturality of \(\mu\) to the pair \((\delta_x,\delta_y)\), for which \(\delta_x\wedge\delta_y=\delta_{x\wedge y}\), and to the pair \((\sigma_X,\sigma_Y)\), for which \(\sigma_X\wedge\sigma_Y=\sigma_{X\wedge Y}\).

(3) By Lemma 1.3 the morphisms of Γ-sets \(\rho:\mathbb S\to A\) with \(\rho(1)=1\) are given by this formula, and there is just one. It is multiplicative: \(\rho(x)\cdot\rho(y)=A(\hat x\wedge\hat y)(1\cdot1)=A(\widehat{x\wedge y})(1)\). \(\square\)

Part (2) says: if \(\xi\) is a witness for a family \((a_x)\) with sum \(s\), and \(\eta\) a witness for \((b_y)\) with sum \(t\), then \(\xi\cdot\eta\) is a witness for the family \((a_xb_y)\) with sum \(st\). This is the distributive law of an \(\mathbb S\)-algebra.

**Definition 3.4.** Let \(A\) be an \(\mathbb S\)-algebra. An *\(A\)-module* is a Γ-set \(N\) with a pairing \((A,N)\to N\), written \(a\wedge n\mapsto a\cdot n\), such that \(1\cdot n=n\) and \((a\cdot b)\cdot n=a\cdot(b\cdot n)\). Morphisms of \(A\)-modules are the morphisms of Γ-sets that commute with the action.

**Proposition 3.5.** (1) Every Γ-set \(N\) is an \(\mathbb S\)-module in exactly one way, by \(x\cdot n=x\otimes n\), and every morphism of Γ-sets is \(\mathbb S\)-linear. So \(\mathbb S\)-modules and Γ-sets are the same thing.

(2) Let \(M\) be a monoid. An \(\mathbb SM\)-module is a Γ-set \(N\) with an action of \(M\): endomorphisms \(m_N\) of the Γ-set \(N\) with \((mm')_N=m_Nm'_N\), \(1_N=\mathrm{id}\) and \(0_N=0\). The action is \((m\wedge x)\cdot n=x\otimes m_N(n)\).

(3) Let \(R\) be a semiring and \(E\) an \(R\)-semimodule. Then \(HE\) is an \(HR\)-module by \((\varphi\cdot\psi)(x\wedge y)=\varphi(x)\psi(y)\), and the \(HR\)-linear morphisms \(HE\to HE'\) are the maps \(H(u)\) with \(u:E\to E'\) an \(R\)-linear map.

(4) For a pointed set \(P\), the Γ-set \(P\wedge A\) with \(a\cdot(p\wedge b)=p\wedge(a\cdot b)\) is an \(A\)-module, and \(\theta\mapsto(p\mapsto\theta(p\wedge1))\) is a bijection from the \(A\)-linear morphisms \(P\wedge A\to N\) to the pointed maps \(P\to N(1_+)\). It is the *free \(A\)-module* on \(P\).

**Proof.** (1) and (2). By Proposition 2.3 a pairing \((\mathbb SM,N)\to N\) has the form \((m\wedge x)\wedge n\mapsto x\otimes\gamma(m\wedge n)\) for a unique morphism \(\gamma:M\wedge N\to N\). Such a \(\gamma\) is a family of endomorphisms \(m_N=\gamma(m\wedge-)\) of \(N\) with \(0_N=0\). The unit law says \(1_N=\mathrm{id}\). Since \(m_N\) is natural and \(x\otimes(y\otimes n)=(x\wedge y)\otimes n\), we get \((m\wedge x)\cdot((m'\wedge y)\cdot n)=(x\wedge y)\otimes m_Nm'_N(n)\), while \(((m\wedge x)\cdot(m'\wedge y))\cdot n=(x\wedge y)\otimes(mm')_N(n)\). These agree for all \(x,y,n\) exactly when \((mm')_N=m_Nm'_N\). This is (2). For \(M=\mathbb F_1\) the only action is the trivial one, which is (1); a morphism of Γ-sets commutes with the maps \(N(\hat x\wedge\mathrm{id})\), so it is \(\mathbb S\)-linear.

(3) The action is a pairing for the reason given in Example 3.2(c), and the module laws hold because they hold in \(E\). By Theorem 1.6 a morphism of Γ-sets \(HE\to HE'\) is \(H(u)\) with \(u\) additive. It is \(HR\)-linear exactly when \(u(re)=ru(e)\), as one sees at the first level.

(4) The module laws for \(P\wedge A\) follow from those of \(A\). Let \(\theta\) be \(A\)-linear and \(t(p)=\theta(p\wedge1)\). Since \(p\wedge b=b\cdot(p\wedge1)\), we get \(\theta(p\wedge b)=b\cdot t(p)\), so \(\theta\) is determined by \(t\). Conversely, for a pointed map \(t\) the formula \(\theta(p\wedge b)=b\cdot t(p)\) defines a morphism of Γ-sets, which is \(A\)-linear by associativity. \(\square\)

Not every \(HR\)-module has the form \(HE\). For \(R\ne0\) the free module \(2_+\wedge HR=HR\vee HR\) does not: its first level is \(R\vee R\), and the family \((1,1')\), made of the units of the two copies of \(R\), has no witness in \((HR\vee HR)(2_+)=R^2\vee R^2\). So the Segal map at \(2_+\) is not surjective.

## 4. Monoids, semirings and rings as \(\mathbb S\)-algebras

### The functor from monoids

**Theorem 4.1** (The adjunction for monoids). Let \(M\) be a monoid and \(A\) an \(\mathbb S\)-algebra. The map \(\rho\mapsto\rho_{1_+}\) is a bijection
\[
\operatorname{Hom}_{\mathbb S\text{-alg}}(\mathbb SM,A)\ \longrightarrow\ \operatorname{Hom}_{\mathrm{monoids}}(M,A(1_+)).
\]
The morphism that corresponds to \(t:M\to A(1_+)\) is \(\rho(m\wedge x)=A(\hat x)(t(m))\).

*Reference:* [Connes–Consani 2016a, Proposition 3.3]; [Connes–Consani 2021, Proposition 2.2].

**Proof.** By Lemma 1.3 the morphisms of Γ-sets \(\mathbb SM\to A\) are the maps \(\rho(m\wedge x)=A(\hat x)(t(m))\) for pointed maps \(t:M\to A(1_+)\). The condition \(\rho(1)=1\) says \(t(1)=1\). By the naturality of \(\mu\),
\[
\rho(m\wedge x)\cdot\rho(n\wedge y)=A(\hat x\wedge\hat y)(t(m)t(n)),\qquad\rho((m\wedge x)\cdot(n\wedge y))=A(\widehat{x\wedge y})(t(mn)).
\]
Since \(\hat x\wedge\hat y=\widehat{x\wedge y}\), the two agree for all \(x,y\) exactly when \(t(m)t(n)=t(mn)\): take \(x=y=1\). \(\square\)

**Corollary 4.2.** (1) The functor \(M\mapsto\mathbb SM\) from monoids to \(\mathbb S\)-algebras is fully faithful, and it is left adjoint to \(A\mapsto A(1_+)\).

(2) \(\operatorname{Hom}(\mathbb S[T],A)=A(1_+)\) and \(\operatorname{Hom}(\mathbb S[\mu_n],A)=\{a\in A(1_+):a^n=1\}\).

**Proof.** (1) Take \(A=\mathbb SN\), for which \(A(1_+)=N\). (2) A morphism from the free monoid on \(T\) is the choice of the image of \(T\), and a morphism from \(\mathbb F_{1^n}=\{0\}\cup\mu_n\) is the choice of the image of a generator of the cyclic group \(\mu_n\). \(\square\)

By Lemma 3.3 every \(\mathbb S\)-algebra has a first level \(A(1_+)\), which is a monoid. The counit of the adjunction is a morphism \(\mathbb S(A(1_+))\to A\). The monoid \(A(1_+)\) is what the geometry of monoids sees of \(A\).

### The functor from semirings and rings

**Theorem 4.3** (Semirings). For semirings \(R\) and \(R'\), the map \(u\mapsto H(u)\) is a bijection from the semiring morphisms \(R\to R'\) to the morphisms of \(\mathbb S\)-algebras \(HR\to HR'\). So \(H\) is a fully faithful functor from semirings, and from rings, to \(\mathbb S\)-algebras.

*Reference:* [Connes–Consani 2016a, Proposition 3.5].

**Proof.** By Theorem 1.6 the morphisms of Γ-sets \(HR\to HR'\) are the maps \(H(u)\) with \(u\) additive. Then \(H(u)(1)=u(1)\), and \(H(u)\) respects products exactly when \(u\) does, because \(H(u)(\varphi\cdot\psi)(x\wedge y)=u(\varphi(x)\psi(y))\). \(\square\)

**Theorem 4.4** (Between monoids and semirings). Let \(M\) be a monoid and \(R\) a semiring. Let \(\mathbb N[M]\) be the monoid semiring of \(M\) and \(\mathbb Z[M]\) its monoid ring, both modulo the zero of \(M\).

1. \(\operatorname{Hom}_{\mathbb S\text{-alg}}(\mathbb SM,HR)\) is the set of monoid morphisms from \(M\) to the multiplicative monoid of \(R\). It is also the set of semiring morphisms \(\mathbb N[M]\to R\) and, when \(R\) is a ring, the set of ring morphisms \(\mathbb Z[M]\to R\).
2. Let \(A\) be an additive monoid and \(P\) a pointed set. Every morphism of Γ-sets \(HA\to P\wedge\mathbb S\) is zero. Hence, if \(M\) is not the zero monoid \(\{0\}\), that is, if \(1\ne0\) in \(M\), there is no morphism of \(\mathbb S\)-algebras \(HR\to\mathbb SM\).

*Reference:* [Connes–Consani 2021, Lemma 2.1, Proposition 2.2, Corollary 2.3]. The proof of [Connes–Consani 2021, Theorem 3.1] states that there is no morphism \(HR\to\mathbb SM\) for any monoid \(M\) and any ring \(R\); this fails for the zero monoid, because then \(\mathbb SM=\ast\) receives one morphism from every \(\mathbb S\)-algebra, so part (2) excludes it.

**Proof.** (1) This is Theorem 4.1 for \(A=HR\), together with the universal property of \(\mathbb N[M]\) and \(\mathbb Z[M]\).

(2) Let \(\theta:HA\to P\wedge\mathbb S\) be a morphism and \(\varphi\in HA(X)\). Let \(\tau\) be the exchange of the two copies of \(X\) in \(X\vee X\), and let \(p:X\vee X\to X\) be the identity on the first copy and a zero map on the second. Let \(\varphi'\in HA(X\vee X)\) be equal to \(\varphi\) on both copies. Then \(HA(\tau)\varphi'=\varphi'\) and \(HA(p)\varphi'=\varphi\). By naturality \(\theta(\varphi')\in P\wedge(X\vee X)\) is fixed by \(P\wedge\tau\). But \(P\wedge\tau\) moves every element \(q\wedge z\) other than the base point, because \(\tau\) moves \(z\) to the other copy. So \(\theta(\varphi')=\ast\), and \(\theta(\varphi)=(P\wedge p)(\theta(\varphi'))=\ast\). A morphism of \(\mathbb S\)-algebras \(HR\to\mathbb SM\) would be zero as a morphism of Γ-sets and would send 1 to 1, so \(1=0\) in \(M\). \(\square\)

Theorems 4.1, 4.3 and 4.4 describe all morphisms between the \(\mathbb S\)-algebras \(\mathbb SM\), with \(M\) a non-zero monoid, and \(HR\), with \(R\) a ring: monoid morphisms between the \(\mathbb SM\), ring morphisms between the \(HR\), ring morphisms \(\mathbb Z[M]\to R\) from \(\mathbb SM\) to \(HR\), and nothing from \(HR\) to \(\mathbb SM\). This is the category that [Connes–Consani 2010] obtains by gluing the category of monoids and the category of rings along the adjunction \(M\mapsto\mathbb Z[M]\), as recalled in [Connes–Consani 2021, §3.1]. With the zero monoid left out, it is a full subcategory of the category of \(\mathbb S\)-algebras [Connes–Consani 2021, Theorem 3.1].

### Base change

**Theorem 4.5** (Adjoining a monoid). Let \(M\) be a monoid and \(B\) an \(\mathbb S\)-algebra. Let \(B[M]\) be the Γ-set \(M\wedge B\) with the product \((m\wedge b)\cdot(n\wedge b')=mn\wedge(b\cdot b')\) and the unit \(1\wedge1\).

1. \(B[M]\) is an \(\mathbb S\)-algebra, and \(B[M]\cong\mathbb SM\wedge B\) as Γ-sets.
2. \(B[M]\) is the coproduct of \(\mathbb SM\) and \(B\): for every \(\mathbb S\)-algebra \(C\),
\[
\operatorname{Hom}(B[M],C)=\operatorname{Hom}_{\mathrm{monoids}}(M,C(1_+))\times\operatorname{Hom}(B,C).
\]

**Proof.** (1) The laws of an \(\mathbb S\)-algebra follow from those of \(M\) and \(B\). The isomorphism is Proposition 2.3 with \(P=M\).

(2) The maps \(i(m\wedge x)=m\wedge B(\hat x)(1)\) and \(j(b)=1\wedge b\) are morphisms of \(\mathbb S\)-algebras \(\mathbb SM\to B[M]\) and \(B\to B[M]\), and \(m\wedge b=i(m\wedge1)\cdot j(b)\). So a morphism \(h:B[M]\to C\) is determined by \(h\circ i\) and \(h\circ j\). Conversely let \(t:M\to C(1_+)\) be a monoid morphism and \(g:B\to C\) a morphism. Put \(h(m\wedge b)=t(m)\cdot g(b)\), with the action of \(C(1_+)\) on \(C(X)\). This is a morphism of Γ-sets by Lemma 3.3(1). It respects products because \(C\) is associative and commutative: \((t(m)\cdot g(b))\cdot(t(n)\cdot g(b'))=t(mn)\cdot g(b\cdot b')\). It restricts to the morphism of Theorem 4.1 on \(\mathbb SM\) and to \(g\) on \(B\). \(\square\)

**Example 4.6** (Base change to a semiring). For \(B=\mathbb S\) we get \(\mathbb S[M]=\mathbb SM\). For a semiring \(R\), the \(\mathbb S\)-algebra \((HR)[M]\) has
\
(HR)[M=M\wedge R^k .
\]
Its elements are 0 and the vectors \(m\wedge(r_1,\dots,r_k)\), which carry a single element \(m\ne0\) of \(M\). Let \(R[M]\) be the monoid semiring of \(M\) over \(R\), modulo the zero of \(M\). The map \(m\wedge(r_j)\mapsto(r_jm)\) embeds \((HR)[M]\) into \(H(R[M])\), whose value at \(k_+\) is \(R[M]^k\). If \(R\ne0\) and \(M\) has two elements \(m\ne m'\) other than 0, the two are different: the elements \(m\wedge1\) and \(m'\wedge1\) of the first level have the sum \(m+m'\) in \(H(R[M])\), and the family they form has no witness in \((HR)M=M\wedge R^2\). So the coproduct of \(\mathbb SM\) and \(HR\) is not of the form \(HR'\). Nevertheless both have the same morphisms to the \(\mathbb S\)-algebras of semirings. By Theorems 4.5 and 4.3 and the universal property of \(R[M]\),
\[
\operatorname{Hom}((HR)[M],HR')=\operatorname{Hom}(M,R')\times\operatorname{Hom}(R,R')=\operatorname{Hom}(R[M],R')=\operatorname{Hom}(H(R[M]),HR').
\]
In this sense the base change of the monoid \(M\) from \(\mathbb S\) to \(H\mathbb Z\) is the ring \(\mathbb Z[M]\) of *Commutative monoids and their spectra*. For \(M=\mathbb F_{1^n}\) it is the group ring \(\mathbb Z[T]/(T^n-1)\) of \(\mu_n\).

The next theorem shows the same feature for the smash product of two \(\mathbb S\)-algebras of semirings: it is not of the form \(HR''\).

**Theorem 4.7** (Smash squares). Let \(R\) be a semiring with \(1\ne0\). The Segal map of \(HR\wedge HR\) at \(2_+\) is not injective. Hence \(HR\wedge HR\) is not isomorphic, even as a Γ-set, to \(HA\) for any additive monoid \(A\). In particular \(H\mathbb Z\wedge H\mathbb Z\) is not isomorphic to \(H\mathbb Z\).

*Reference:* [Connes–Consani 2016a, Proposition 7.4] proves that \(H\mathbb Z\wedge H\mathbb Z\) and \(H\mathbb Z\) are not isomorphic \(\mathbb S\)-algebras, by another argument.

**Proof.** We need a pairing that separates two elements. For \(X\) in \(\mathrm{Fin}_\ast\) let \(L(X)\) be the set of formal linear combinations \(\sum_ic_i[\varphi_i]\) with \(c_i\in R\) and \(\varphi_i\) non-zero elements of \(HR(X)\); that is, the finitely supported functions \(HR(X)^\circ\to R\). For \(f:X\to Y\) put \(L(f)(\sum c_i[\varphi_i])=\sum c_i[HR(f)\varphi_i]\), with the convention \([0]=0\). Then \(L\) is a Γ-set. For \(x\in X^\circ\) and \(\psi\in HR(Y)\), the element \(x\otimes\psi\in HR(X\wedge Y)\) is the function that equals \(\psi\) on \(\{x\}\times Y^\circ\) and 0 elsewhere. Put
\[
\alpha_{X,Y}(\varphi\wedge\psi)=\sum_{x\in X^\circ}\varphi(x)\,[x\otimes\psi]\ \in L(X\wedge Y).
\]
This is pointed. It is natural in \(Y\), because \(HR(\mathrm{id}\wedge g)(x\otimes\psi)=x\otimes HR(g)\psi\). It is natural in \(X\), because \(HR(f\wedge\mathrm{id})(x\otimes\psi)=f(x)\otimes\psi\), which is 0 when \(f(x)=\ast\), so that
\[
L(f\wedge\mathrm{id})\,\alpha(\varphi\wedge\psi)=\sum_{x'\in X'^\circ}\Big(\sum_{f(x)=x'}\varphi(x)\Big)[x'\otimes\psi]=\alpha(HR(f)\varphi\wedge\psi).
\]
So \(\alpha\) is a pairing \((HR,HR)\to L\), and it induces \(\bar\alpha:HR\wedge HR\to L\).

Now let \(\xi=u(1\wedge(1,1))\) and \(\eta=u((1,1)\wedge1)\), with \(1\in R=HR(1_+)\) and \((1,1)\in R^2=HR(2_+)\). Both lie in \((HR\wedge HR)(2_+)\), since \(1_+\wedge2_+=2_+=2_+\wedge1_+\). By the naturality of \(u\), both components of \(\xi\) and both components of \(\eta\) equal \(u(1\wedge1)\). So \(\xi\) and \(\eta\) have the same image under the Segal map. But
\[
\bar\alpha(\xi)=[(1,1)],\qquad\bar\alpha(\eta)=[(1,0)]+[(0,1)],
\]
and these are different elements of \(L(2_+)\), because \((1,1)\), \((1,0)\) and \((0,1)\) are three different non-zero elements of \(R^2\). Hence \(\xi\ne\eta\). The last statements follow from Theorem 1.6(2). \(\square\)

**Remark 4.8.** The proof shows that the two morphisms of Γ-sets \(HR\to HR\wedge HR\), \(\varphi\mapsto u(\varphi\wedge1)\) and \(\varphi\mapsto u(1\wedge\varphi)\), are different: they send \((1,1)\) to \(\eta\) and to \(\xi\). The contrast with generalized rings is the following. There a generalized ring receives at most one morphism from \(\mathbb Z\), and therefore the tensor product of \(\mathbb Z\) with itself over the initial object is \(\mathbb Z\) [Durov 2007, 5.1.22]; see *Generalized rings*. The full structure of a smash square is known in one case: \((H\mathbb B\wedge H\mathbb B)(k_+)\) is, apart from its base point, the set of matrices with entries in \(k_+\) that have no zero row, no zero column, no repeated row and no repeated column, taken up to permutations of the rows and of the columns [Connes–Consani 2016a, Theorem 4.9].

The proof of Theorem 4.7 uses the multiplication of \(R\) only to write the coefficients of \(L\). Let \(A\) and \(B\) be additive monoids, let \(L(X)\) be the set of finitely supported functions \(HB(X)^\circ\to A\), written \(\sum a_i[\psi_i]\), and define \(L(f)\) and \(\alpha:(HA,HB)\to L\) by the same formulas. For \(a\ne0\) in \(A\) and \(b\ne0\) in \(B\), the elements \(u(a\wedge(b,b))\) and \(u((a,a)\wedge b)\) of \((HA\wedge HB)(2_+)\) have the same components, and \(\bar\alpha\) sends them to \(a[(b,b)]\) and to \(a[(b,0)]+a[(0,b)]\), which are different. So \(HA\wedge HB\) is of the form \(HC\) only when \(A\) or \(B\) is zero. For example \(H(\mathbb Z/2)\wedge H(\mathbb Z/3)\) is not a point, although \(\mathbb Z/2\otimes\mathbb Z/3=0\): the functor \(H\) does not take tensor products to smash products.

### Why \(\mathbb S\) plays the role of \(\mathbb F_1\)

We collect what has been proved.

1. \(\mathbb S\) is the \(\mathbb S\)-algebra of the monoid \(\mathbb F_1\) (Example 3.2), and the extensions \(\mathbb F_{1^n}\) give \(\mathbb S[\mu_n]\). It is also the \(\mathbb S\)-algebra of the generalized ring \(\mathbb F_1\) (Example 6.4).
2. \(\mathbb S\) is the unit of the smash product (Proposition 2.3) and the initial \(\mathbb S\)-algebra (Lemma 3.3). Every Γ-set is an \(\mathbb S\)-module in exactly one way (Proposition 3.5). These are the properties of \(\mathbb Z\) among rings and abelian groups.
3. The monoids, which are the algebras over \(\mathbb F_1\) in the lessons on monoid schemes, form a full subcategory of \(\mathbb S\)-algebras (Corollary 4.2). So do the rings and the semirings (Theorem 4.3). The base change \(M\mapsto\mathbb Z[M]\) is expressed by the morphisms from \(\mathbb SM\) to \(HR\) (Theorem 4.4, Example 4.6).
4. Pointed sets are the free \(\mathbb S\)-modules: \(\operatorname{Hom}(P\wedge\mathbb S,Q\wedge\mathbb S)\) is the set of pointed maps \(P\to Q\), by Lemma 1.3. The finite pointed sets are the vector spaces over \(\mathbb F_1\) of *Counting over finite fields and the limit q → 1*, and the automorphism group of \(n_+\wedge\mathbb S\) is the symmetric group on \(n\) letters. Abelian groups are \(\mathbb S\)-modules too (Theorem 1.6), and for an abelian group \(V\) the set \(\operatorname{Hom}(n_+\wedge\mathbb S,HV)=V^n\) is the set of additive maps \(\mathbb Z^n\to V\).
5. The smash square of \(H\mathbb Z\) over \(\mathbb S\) does not collapse (Theorem 4.7).

Two cautions are needed. \(\mathbb S\) is not a field in the sense of module theory: its modules are all Γ-sets, and most of them are not free. And an \(\mathbb S\)-algebra is more than its first level: Section 5 gives four \(\mathbb S\)-algebras whose first level is the monoid \(\mathbb F_1\).

## 5. Sums with several values

The first level \(A(1_+)\) of an \(\mathbb S\)-algebra is a monoid. The second level \(A(2_+)\) records the sums of two elements.

**Definition 5.1.** Let \(F\) be a Γ-set and \(a,b\in F(1_+)\). The *sum set* of \(a\) and \(b\) is
\[
a\oplus b=\{\operatorname{tot}\xi:\ \xi\in F(2_+),\ \xi_1=a,\ \xi_2=b\}\subseteq F(1_+).
\]

This is the operation of [Connes–Consani 2016a, §3.2]. In \(HA\) the sum set is \(\{a+b\}\). In general it can be empty or have several elements. The exchange of 1 and 2 in \(2_+\) gives \(a\oplus b=b\oplus a\), and \(a\in a\oplus0\) always holds, with the witness \(F(\iota)(a)\) for \(\iota:1_+\to2_+\), \(\iota(1)=1\). In an \(\mathbb S\)-algebra, \(c\cdot(a\oplus b)\subseteq ca\oplus cb\) by Lemma 3.3.

**Proposition 5.2** (Quotient by a group of units). Let \(A\) be an \(\mathbb S\)-algebra and \(G\) a subgroup of the group of invertible elements of the monoid \(A(1_+)\). The sets of orbits \((A/G)(X)=A(X)/G\) form an \(\mathbb S\)-algebra \(A/G\), and the quotient maps form a morphism of \(\mathbb S\)-algebras \(A\to A/G\). For \(A=HR\) with \(R\) a semiring, the first level of \(HR/G\) is the monoid \(R/G\), and
\[
aG\oplus bG=\{cG:\ c\in aG+bG\}.
\]

*Reference:* [Connes–Consani 2016a, Propositions 5.1 and 5.2] for rings; [Connes–Consani 2021, §7.5] for a general \(A\).

**Proof.** By Lemma 3.3 the group \(G\) acts on each pointed set \(A(X)\), and the maps \(A(f)\) commute with the action. So the orbits form a Γ-set and \(A\to A/G\) is a morphism of Γ-sets. Associativity and commutativity give \((g\cdot\xi)\cdot(h\cdot\eta)=(gh)\cdot(\xi\cdot\eta)\) for \(g,h\in G\). So the product of two orbits is well defined, and \(A/G\) inherits the laws of an \(\mathbb S\)-algebra. For \(A=HR\) we get \((HR/G)(X)=R^{X^\circ}/G\) with \(G\) acting on all entries at once. A witness for the family \((aG,bG)\) is the orbit of a pair \((a',b')\) with \(a'\in aG\) and \(b'\in bG\), and its total is \((a'+b')G\). \(\square\)

For a ring \(R\) this is the addition of the quotient hyperring \(R/G\) of *Characteristic one and hyperrings*: the sum of two classes is the set of classes that meet \(aG+bG\). So these hyperrings are the first two levels of \(\mathbb S\)-algebras. The \(\mathbb S\)-algebra \(HR/G\) contains more: it depends on the pair \((R,G)\), not only on the hyperring.

**Example 5.3** (Four \(\mathbb S\)-algebras with first level \(\mathbb F_1\)). Let \(K\) be a field with at least three elements. The following \(\mathbb S\)-algebras all have the monoid \(\{0,1\}\) as first level.

- \(\mathbb S\), with \(\mathbb S(k_+)=k_+\). Here \(1\oplus1=\emptyset\).
- \(H\mathbb B\), with \(H\mathbb B(k_+)\) the set of subsets of \(\{1,\dots,k\}\). Here \(1\oplus1=\{1\}\).
- \(H\mathbb F_2\), with \(H\mathbb F_2(k_+)=\mathbb F_2^k\). Here \(1\oplus1=\{0\}\).
- \(HK/K^\times\), with \((HK/K^\times)(k_+)=K^k/K^\times\), which is a point together with the projective space \(\mathbb P^{k-1}(K)\). Here \(1\oplus1=\{0,1\}\): for \(g,h\in K^\times\) the sum \(g+h\) is 0 when \(h=-g\), and it is not 0 for some pair because \(K\) has at least three elements. Its first two levels form the Krasner hyperfield.

The sum set \(1\oplus1\) is preserved by isomorphisms of Γ-sets, so the four are pairwise non-isomorphic. The first level does not determine an \(\mathbb S\)-algebra. In the same way \(H\mathbb Q/\mathbb Q_{>0}\) has first level \(\{0,1,-1\}\) with \(1\oplus1=\{1\}\) and \(1\oplus(-1)=\{-1,0,1\}\), the hyperfield of signs [Connes–Consani 2016a, Example 5.3].

## 6. The archimedean place

### Unit balls

Let \(R\) be a semiring. A *seminorm* on \(R\) is a map \(N:R\to[0,\infty)\) with
\[
N(0)=0,\qquad N(1)=1,\qquad N(x+y)\le N(x)+N(y),\qquad N(xy)\le N(x)N(y).
\]
A seminorm on an \(R\)-semimodule \(E\) is a map \(N_E:E\to[0,\infty)\) with \(N_E(0)=0\), \(N_E(e+e')\le N_E(e)+N_E(e')\) and \(N_E(re)\le N(r)N_E(e)\). For a real number \(\lambda\ge0\) put
\[
\|HE\|_\lambda(X)=\Big\{\varphi\in HE(X):\ \sum_{x\in X^\circ}N_E(\varphi(x))\le\lambda\Big\}.
\]

**Proposition 6.1** (Unit balls). (1) \(\|HE\|_\lambda\) is a sub-Γ-set of \(HE\).

(2) If \(\varphi\in\|HR\|_\lambda(X)\) and \(\psi\in\|HE\|_\mu(Y)\), then \(\varphi\cdot\psi\in\|HE\|_{\lambda\mu}(X\wedge Y)\).

(3) \(\|HR\|_1\) is a sub-\(\mathbb S\)-algebra of \(HR\), and every \(\|HE\|_\lambda\) is a module over it.

*Reference:* [Connes–Consani 2016a, Proposition 6.1].

**Proof.** (1) For \(f:X\to Y\) and \(y\in Y^\circ\) the triangle inequality gives \(N_E((HE(f)\varphi)(y))\le\sum_{f(x)=y}N_E(\varphi(x))\); an empty sum is covered by \(N_E(0)=0\). Summing over \(y\) gives at most \(\sum_{x\in X^\circ}N_E(\varphi(x))\le\lambda\).

(2) \(\sum_{x,y}N_E(\varphi(x)\psi(y))\le\sum_xN(\varphi(x))\cdot\sum_yN_E(\psi(y))\le\lambda\mu\).

(3) The unit \(1\in R\) has \(N(1)=1\), so it lies in \(\|HR\|_1(1_+)\). The rest follows from (1) and (2). \(\square\)

**Example 6.2.** (a) Take the usual absolute value on \(\mathbb Z\). A vector of integers with \(\sum|\varphi_j|\le1\) is 0 or has a single entry \(\pm1\). So \(\|H\mathbb Z\|_1=\mathbb S[\pm1]\), the spherical monoid algebra of \(\{0,1,-1\}\).

(b) On \(\mathbb B\) the map \(N(0)=0\), \(N(1)=1\) is a seminorm, and \(\|H\mathbb B\|_1(X)\) is the set of subsets of \(X^\circ\) with at most one element. So \(\|H\mathbb B\|_1=\mathbb S\) [Connes–Consani 2016a, Remark 6.2]: the base \(\mathbb S\) is itself a unit ball.

(c) For the real numbers, \(\|H\mathbb R\|_1(k_+)\) is the octahedron \(\{x\in\mathbb R^k:\sum|x_j|\le1\}\). Its first level is the interval \([-1,1]\) with its multiplication. The sum set is \(a\oplus b=\{a+b\}\) when \(|a|+|b|\le1\) and is empty otherwise. The same holds for \(\|H\mathbb Q\|_1\) with rational entries.

(d) The sum of the \(N(\varphi(x))\) cannot be replaced by their maximum: for the usual absolute value the sets \(\{\max|\varphi(x)|\le1\}\) are not stable under the maps \(H\mathbb Q(f)\). Exercise 3 treats this and the \(p\)-adic case.

### The relation with the unit ball monad

[Durov 2007] describes a ring \(R\) by the monad on sets that sends \(S\) to the set \(R^{(S)}\) of formal linear combinations of elements of \(S\), and defines a generalized ring as a commutative monad on sets that commutes with filtered colimits [Durov 2007, 4.1.1 and 5.1.1]; see *Generalized rings*. The object at the archimedean place is the monad \(\mathbb Z_\infty\) of *octahedral combinations*:
\[
\mathbb Z_\infty(S)=\Big\{\sum_s\lambda_s\{s\}:\ \lambda_s\in\mathbb R,\ \text{almost all }\lambda_s=0,\ \sum_s|\lambda_s|\le1\Big\}
\]
[Durov 2007, 3.4.12]. For a finite set \(S\) and the pointed set \(S_+=S\sqcup\{\ast\}\), this is the set \(\|H\mathbb R\|_1(S_+)\). We now show that the monad structure and the \(\mathbb S\)-algebra structure correspond as well. It is convenient to use monads on pointed sets.

Let \((T,m,e)\) be a monad on \(\mathrm{Set}_\ast\): a functor \(T\) with natural maps \(e_X:X\to T(X)\) and \(m_X:T(T(X))\to T(X)\) such that \(m\circ T(m)=m\circ m_T\) and \(m\circ T(e)=\mathrm{id}=m\circ e_T\). For \(a\in T(X)\) and a pointed map \(k:X\to T(W)\) put
\[
a\rhd k=m_W(T(k)(a))\in T(W).
\]
The monad laws and the naturality of \(e\) and \(m\) give, for \(h:W\to T(V)\), \(f:X\to Y\) and \(g:W\to W'\),
\[
e_X(x)\rhd k=k(x),\qquad a\rhd e_X=a,\qquad(a\rhd k)\rhd h=a\rhd(x\mapsto k(x)\rhd h),
\tag{6.1}
\]
\[
T(f)(a)=a\rhd(e_Y\circ f),\qquad T(g)(a\rhd k)=a\rhd(T(g)\circ k).
\tag{6.2}
\]

**Theorem 6.3** (Monads give \(\mathbb S\)-algebras). Let \((T,m,e)\) be a monad on pointed sets such that \(T\) of a point is a point. For \(x\in X\) and \(b\in T(Y)\) write \(x\otimes b=T(\hat x\wedge\mathrm{id}_Y)(b)\in T(X\wedge Y)\). Then the restriction of \(T\) to \(\mathrm{Fin}_\ast\), with
\[
a\cdot b=a\rhd(x\mapsto x\otimes b)\qquad(a\in T(X),\ b\in T(Y))
\]
and with the unit \(e_{1_+}(1)\), is an \(\mathbb S\)-algebra, in general not commutative.

*Reference:* [Connes–Consani 2016a, Proposition 7.3], for monads that commute with filtered colimits, as a consequence of the properties of Lydakis's assembly map.

**Proof.** Since \(T\) of a point is a point, \(T\) sends zero maps to zero maps. The map \(x\mapsto x\otimes b\) is pointed, because \(\hat x\wedge\mathrm{id}\) is a zero map for \(x=\ast\).

*Pointed.* If \(b=\ast\), then \(x\otimes b=\ast\) for all \(x\), and \(a\rhd k=\ast\) for a zero map \(k\). If \(a=\ast\), then \(a\) comes from \(T\) of a point and \(a\rhd k=\ast\).

*Natural.* For \(g:Y\to Y'\), the second formula of (6.2) and \(T(\mathrm{id}\wedge g)(x\otimes b)=x\otimes T(g)b\) give \(T(\mathrm{id}\wedge g)(a\cdot b)=a\cdot T(g)b\). For \(f:X\to X'\), the first formula of (6.2) and the first and third of (6.1) give \(T(f)a\cdot b=a\rhd(x\mapsto f(x)\otimes b)\). Since \(f(x)\otimes b=T(f\wedge\mathrm{id})(x\otimes b)\), this is \(T(f\wedge\mathrm{id})(a\cdot b)\) by (6.2).

*Unit.* By (6.1), \(e(1)\cdot b=1\otimes b=b\). Since \(x\otimes e_{1_+}(1)=e_X(x)\) by the naturality of \(e\), also \(a\cdot e(1)=a\rhd e_X=a\).

*Associative.* Let \(c\in T(Z)\). By (6.1) and (6.2),
\[
(a\cdot b)\cdot c=a\rhd\big(x\mapsto(x\otimes b)\rhd(w\mapsto w\otimes c)\big),\qquad(x\otimes b)\rhd(w\mapsto w\otimes c)=b\rhd(y\mapsto(x\wedge y)\otimes c),
\]
where the second equality uses \(x\otimes b=b\rhd(y\mapsto e(x\wedge y))\). On the other side \(a\cdot(b\cdot c)=a\rhd(x\mapsto x\otimes(b\cdot c))\), and by (6.2)
\[
x\otimes(b\cdot c)=b\rhd(y\mapsto x\otimes(y\otimes c))=b\rhd(y\mapsto(x\wedge y)\otimes c).
\]
The two sides agree. \(\square\)

**Example 6.4.** (a) Let \(R\) be a semiring. The functor \(T_R(X)=HR(X)\), extended to all pointed sets by finitely supported functions, is a monad: \(e(x)\) is the function with value 1 at \(x\), and \(m\) sends a formal combination \(\sum c_i[\varphi_i]\) of elements of \(T_R(X)\) to the element \(\sum c_i\varphi_i\). Here \(\varphi\rhd k=\sum_x\varphi(x)k(x)\). The \(\mathbb S\)-algebra of Theorem 6.3 has \(\varphi\cdot\psi=\sum_x\varphi(x)\,(x\otimes\psi)\), which is the function \(x\wedge y\mapsto\varphi(x)\psi(y)\). So it is \(HR\).

(b) For \(R=\mathbb R\) the subsets \(\{\sum|\varphi(x)|\le1\}\) are stable under \(e\) and \(m\): a combination with coefficients of total absolute value at most 1, of functions of total absolute value at most 1, has total absolute value at most 1. This monad on pointed sets has the same values on the sets \(S_+\) as the monad \(\mathbb Z_\infty\). Its \(\mathbb S\)-algebra is \(\|H\mathbb R\|_1\), with the product of Proposition 6.1.

(c) In the same way \(\|H\mathbb Q\|_1\) corresponds to the generalized ring \(\mathbb Z_{(\infty)}=\mathbb Z_\infty\cap\mathbb Q\), and \(\|H\mathbb Z\|_1=\mathbb S[\pm1]\) corresponds to \(\mathbb F_{\pm1}=\mathbb Z\cap\mathbb Z_\infty\), for which \(\mathbb F_{\pm1}(S)=0\sqcup S\sqcup-S\) [Durov 2007, 3.4.12]. The identity monad on pointed sets gives \(\mathbb S\). On sets it is the monad \(S\mapsto S\sqcup\{0\}\), whose modules are the pointed sets; this is the generalized ring \(\mathbb F_1\) of *Generalized rings* [Connes–Consani 2016a, §7.3].

(d) For a monoid \(M\), the functor \(X\mapsto M\wedge X\) is a monad on pointed sets, with \(e(x)=1\wedge x\) and \(m(m_1\wedge(m_2\wedge x))=m_1m_2\wedge x\). Here \((m_1\wedge x)\rhd k=m_1\cdot k(x)\), so the product of Theorem 6.3 is \((m_1\wedge x)\cdot(m_2\wedge y)=m_1m_2\wedge(x\wedge y)\), and the \(\mathbb S\)-algebra is \(\mathbb SM\). So the three kinds of \(\mathbb S\)-algebras met so far, those of monoids, of semirings and of unit balls, all come from monads.

So the \(\mathbb S\)-algebra at the archimedean place and the unit ball monad consist of the same sets, and the product of the first is obtained from the substitution of the second. The two theories differ in what is built on these objects. A module over the monad \(\mathbb Z_\infty\) is a set in which octahedral combinations can be evaluated; a module over \(\|H\mathbb R\|_1\) is a Γ-set with an action. And tensor products differ: over the initial generalized ring the tensor square of \(\mathbb Z\) is \(\mathbb Z\), while the smash square of \(H\mathbb Z\) is not \(H\mathbb Z\) (Theorem 4.7 and Remark 4.8).

### The structure sheaf of the compactification

**Definition 6.5.** Let \(\overline{\operatorname{Spec}\mathbb Z}\) be the set \(\operatorname{Spec}\mathbb Z\cup\{\infty\}\). Its closed points are the primes \(p\) and \(\infty\). Its non-empty open sets are the subsets that contain the generic point and miss only finitely many closed points. For a non-empty open set \(U\) let \(\mathbb Z_U\) be the ring of rational numbers \(q\) with \(\operatorname{ord}_p(q)\ge0\) for all primes \(p\in U\). Put
\[
\mathcal O(U)=\begin{cases}H(\mathbb Z_U)&\text{if }\infty\notin U,\\ \|H(\mathbb Z_U)\|_1&\text{if }\infty\in U,\end{cases}
\]
with the usual absolute value, and \(\mathcal O(\emptyset)=\ast\). Restriction maps are inclusions.

A *sheaf of Γ-sets* on a space is a presheaf \(P\) of Γ-sets such that \(U\mapsto P(U)(X)\) is a sheaf of sets for every \(X\) in \(\mathrm{Fin}_\ast\); sheaves of \(\mathbb S\)-algebras and of modules are defined in the same way.

**Proposition 6.6.** \(\mathcal O\) is a sheaf of \(\mathbb S\)-algebras on \(\overline{\operatorname{Spec}\mathbb Z}\). On \(\operatorname{Spec}\mathbb Z\) it is \(H\) of the structure sheaf. Its \(\mathbb S\)-algebra of global sections is \(\|H\mathbb Z\|_1=\mathbb S[\pm1]\). Its stalk at \(\infty\) is \(\|H\mathbb Q\|_1\), its stalk at a prime \(p\) is \(H(\mathbb Z_{(p)})\), and its stalk at the generic point is \(H\mathbb Q\).

*Reference:* [Connes–Consani 2016a, Proposition 6.3].

**Proof.** Each \(\mathcal O(U)\) is a sub-\(\mathbb S\)-algebra of \(H\mathbb Q\) by Proposition 6.1, and \(\mathcal O(U)\subseteq\mathcal O(V)\) for \(V\subseteq U\). Fix \(X\). Two non-empty open sets always meet, and all the sets \(\mathcal O(U)(X)\) lie in \(\mathbb Q^{X^\circ}\). So sections \(s_i\in\mathcal O(U_i)(X)\) over non-empty open sets \(U_i\) that agree on the intersections are one and the same element \(s\) of \(\mathbb Q^{X^\circ}\). It lies in \(\mathcal O(\bigcup U_i)(X)\): the ring \(\mathbb Z_{\bigcup U_i}\) is the intersection of the rings \(\mathbb Z_{U_i}\), and \(\infty\) lies in the union exactly when it lies in some \(U_i\). This is the sheaf condition; empty members of a cover impose nothing, because \(\mathcal O(\emptyset)\) is a point. The stalks are the unions of the \(\mathcal O(U)\) over the neighbourhoods \(U\). A vector of rational numbers has its entries in \(\mathbb Z_U\) for some \(U\) that contains \(\infty\), which gives the stalk at \(\infty\). For \(U=\overline{\operatorname{Spec}\mathbb Z}\) we have \(\mathbb Z_U=\mathbb Z\), and Example 6.2(a) gives the global sections. \(\square\)

The stalk at \(\infty\) is the \(\mathbb S\)-algebra that corresponds to \(\mathbb Z_{(\infty)}\). The generalized rings \(A_N=\mathbb Z[1/N]\cap\mathbb Z_{(\infty)}\) of [Durov 2007, 7.1.1] correspond to the \(\mathbb S\)-algebras \(\mathcal O(U)\) for the open sets \(U\) that contain \(\infty\). [Durov 2007, 7.1.3–7.1.15] glues \(\operatorname{Spec}\mathbb Z\) and \(\operatorname{Spec}A_N\) and passes to the limit over \(N\); the limit space has the topology of Definition 6.5 and the stalk \(\mathbb Z_{(\infty)}\) at \(\infty\). See *Generalized rings*.

**Definition 6.7.** An *Arakelov divisor* is a formal sum \(D=\sum_pa_p\{p\}+a\{\infty\}\) with integers \(a_p\), almost all zero, and a real number \(a\). Its *degree* is \(\deg D=\sum_pa_p\log p+a\). It is *effective*, written \(D\ge0\), if all \(a_p\ge0\) and \(a\ge0\). The *principal divisor* of \(q\in\mathbb Q^\times\) is \((q)=\sum_p\operatorname{ord}_p(q)\{p\}-\log|q|\,\{\infty\}\); it has degree 0. For a non-empty open set \(U\) put
\[
\mathcal O(D)(U)(X)=\Big\{\varphi\in\mathbb Q^{X^\circ}:\ \operatorname{ord}_p(\varphi(x))\ge-a_p\ \text{for all }p\in U\text{ and all }x,\ \text{ and }\sum_x|\varphi(x)|\le e^a\text{ if }\infty\in U\Big\},
\]
and \(\mathcal O(D)(\emptyset)=\ast\).

**Proposition 6.8.** (1) \(\mathcal O(D)\) is a sheaf of modules over \(\mathcal O\), and \(\mathcal O(0)=\mathcal O\). Its Γ-set of global sections is \(\|H(c_D\mathbb Z)\|_{e^a}\) with \(c_D=\prod_pp^{-a_p}\). The non-zero elements of its first level are the \(q\in\mathbb Q^\times\) with \((q)+D\ge0\).

(2) The morphisms of sheaves of Γ-sets \(\mathcal O(D)\to\mathcal O(D')\) are the multiplications by the rational numbers \(q\) with \(q=0\) or \((q)+D'-D\ge0\). They are morphisms of \(\mathcal O\)-modules.

(3) \(\mathcal O(D)\) and \(\mathcal O(D')\) are isomorphic if and only if \(D-D'\) is principal, and this holds if and only if \(\deg D=\deg D'\). The automorphisms of \(\mathcal O(D)\) are \(\pm1\).

*Reference:* [Connes–Consani 2016a, Propositions 6.3 and 6.4].

**Proof.** (1) The sheaf property is proved as in Proposition 6.6. The action \(\varphi\cdot\psi\) maps \(\mathcal O(U)\) and \(\mathcal O(D)(U)\) to \(\mathcal O(D)(U)\) by Proposition 6.1(2) and because \(\operatorname{ord}_p\) is additive. For the whole space the conditions say that the entries lie in \(c_D\mathbb Z\) and that \(\sum|\varphi(x)|\le e^a\). A rational \(q\ne0\) satisfies them at the first level when \(\operatorname{ord}_p(q)+a_p\ge0\) for all \(p\) and \(-\log|q|+a\ge0\).

(2) Let \(\theta\) be a morphism. Let \(U\) be a non-empty open set without \(\infty\). Then \(\mathcal O(D)(U)=H(E_U)\) for a non-zero subgroup \(E_U\) of \(\mathbb Q\), and likewise \(\mathcal O(D')(U)=H(E'_U)\). By Theorem 1.6, \(\theta_U=H(t_U)\) for an additive map \(t_U:E_U\to E'_U\). An additive map between subgroups of \(\mathbb Q\) is the multiplication by a rational number: if \(r_0\ne0\) and \(nr=mr_0\) with integers \(n\ne0\) and \(m\), then \(nt(r)=mt(r_0)\), so \(t(r)=r\,t(r_0)/r_0\). So \(t_U\) is the multiplication by some \(q_U\). For \(V\subseteq U\) the restriction maps are inclusions, so \(q_V=q_U\); since two non-empty open sets contain a common one, \(q_U=q\) does not depend on \(U\). If \(\infty\in U\), then \(\mathcal O(D)(U)\subseteq\mathcal O(D)(U\setminus\{\infty\})\) and \(\theta_U\) is again the multiplication by \(q\).

Let \(q\ne0\). For \(U=\operatorname{Spec}\mathbb Z\) we have \(E_U=c_D\mathbb Z\) and \(E'_U=c_{D'}\mathbb Z\), and \(qc_D\in c_{D'}\mathbb Z\) says \(\operatorname{ord}_p(q)+a'_p-a_p\ge0\) for all \(p\). Let \(U\) be the complement of one prime \(p_0\). The first level of \(\mathcal O(D)(U)\) contains the numbers \(r\in c_D\mathbb Z[1/p_0]\) with \(|r|\le e^a\). They are dense in \([-e^a,e^a]\) and are sent to numbers with \(|qr|\le e^{a'}\). So \(|q|e^a\le e^{a'}\), that is, \(-\log|q|+a'-a\ge0\). Conversely, if \((q)+D'-D\ge0\), the multiplication by \(q\) maps \(\mathcal O(D)(U)\) into \(\mathcal O(D')(U)\) for every \(U\), and it commutes with the action of \(\mathcal O\).

(3) By (2) an isomorphism is the multiplication by some \(q\ne0\) whose inverse is also a morphism: \((q)+D'-D\ge0\) and \(-(q)+D-D'\ge0\), that is, \(D-D'=(q)\). For \(D=D'\) this gives \(q=\pm1\). A principal divisor has degree 0 by the product formula. If \(\deg D=\deg D'\), then \(D-D'=(q)\) for \(q=\prod_pp^{a_p-a'_p}\). \(\square\)

So the sheaves \(\mathcal O(D)\) are classified by the degree, a real number, as the line bundles on the projective line over a field are classified by their degree, an integer. Every \(D\) is equivalent to \((\deg D)\{\infty\}\). For the smash product of these modules over \(\mathcal O\), see the last section.

## 7. The spectrum of an \(\mathbb S\)-algebra

A reference for this section is [Connes–Consani 2021, §5–§7]. The spectrum of an \(\mathbb S\)-algebra \(A\) is not a topological space. It is a partially ordered set, which depends only on the monoid \(A(1_+)\), together with a notion of cover, which depends on the sums in \(A\). Sheaves are defined with respect to these covers.

### The partially ordered set

Recall from *Commutative monoids and their spectra* that an ideal of a monoid \(M\) is a subset \(I\) with \(0\in I\) and \(MI\subseteq I\); that it is prime if \(I\ne M\) and \(ab\in I\) implies \(a\in I\) or \(b\in I\); and that \(\operatorname{Spec}M\) is the set of prime ideals, with the topology generated by the sets \(D(f)=\{\mathfrak p:f\notin\mathfrak p\}\).

**Definition 7.1.** Let \(A\) be an \(\mathbb S\)-algebra and \(M=A(1_+)\). For \(b\in M\) put
\[
\operatorname{rad}(b)=\{c\in M:\ c^n\in bM\ \text{for some }n\ge1\}.
\]
Let \(C^\infty(A)\) be the set of the subsets \(\operatorname{rad}(b)\), \(b\in M\), ordered by inclusion. We write \(b^\infty\) for \(\operatorname{rad}(b)\) as an element of \(C^\infty(A)\). So
\[
c^\infty\le b^\infty\iff c\in\operatorname{rad}(b)\iff c^n\in bM\ \text{for some }n\ge1 .
\]

The first equivalence holds because \(c^n=bu\) and \(x^k=cv\) give \(x^{kn}=buv^n\). [Connes–Consani 2021, Definition 5.2] introduces \(C^\infty(A)\) as the opposite of a category of points of a topos of presheaves attached to \(M\). By [Connes–Consani 2021, Proposition 5.1] there is a morphism from the object of \(c\) to the object of \(b\) exactly when \(c^n\in bM\) for some \(n\), and then only one. So that category is this partially ordered set.

**Lemma 7.2.** (1) \(\operatorname{rad}(b)\) is the intersection of the prime ideals of \(M\) that contain \(b\).

(2) The map \(b^\infty\mapsto D(b)\) is an isomorphism from \(C^\infty(A)\) to the set of basic open sets of \(\operatorname{Spec}M\), ordered by inclusion.

(3) \(C^\infty(A)\) has a largest element \(1^\infty\) and a smallest element \(0^\infty\), and any two elements have the meet \(b^\infty\wedge c^\infty=(bc)^\infty\).

**Proof.** (1) A prime ideal that contains \(b\) contains \(\operatorname{rad}(b)\). Conversely let \(c\notin\operatorname{rad}(b)\). Let \(\mathfrak p\) be the union of all ideals of \(M\) that contain \(b\) and contain no power \(c^n\), \(n\ge1\); the ideal \(bM\) is one of them. A union of ideals of a monoid is an ideal, so \(\mathfrak p\) is the largest ideal of this kind, and \(c\notin\mathfrak p\). It is prime: if \(xy\in\mathfrak p\) with \(x,y\notin\mathfrak p\), the ideals \(\mathfrak p\cup xM\) and \(\mathfrak p\cup yM\) are strictly larger, so \(c^i\in xM\) and \(c^j\in yM\) for some \(i,j\ge1\), and \(c^{i+j}\in xyM\subseteq\mathfrak p\), a contradiction.

(2) \(D(c)\subseteq D(b)\) says that every prime ideal that contains \(b\) contains \(c\). By (1) this says \(c\in\operatorname{rad}(b)\), that is, \(c^\infty\le b^\infty\).

(3) \(\operatorname{rad}(1)=M\). The set \(\operatorname{rad}(0)\) of nilpotent elements lies in every \(\operatorname{rad}(b)\), because \(0\in bM\). Finally \(\operatorname{rad}(bc)=\operatorname{rad}(b)\cap\operatorname{rad}(c)\): one inclusion holds because \(bcM\subseteq bM\cap cM\), and if \(x^i=bu\) and \(x^j=cv\) then \(x^{i+j}=bcuv\). \(\square\)

So for every \(\mathbb S\)-algebra the partially ordered set \(C^\infty(A)\) is that of the basic open sets of the spectrum of the monoid \(A(1_+)\). It does not see the sums of \(A\). The covers do.

### Partitions and covers

**Definition 7.3.** Let \(f\in C^\infty(A)\). A *partition* of \(f\) is a finite family \((f_j)_{j\in J}\) of elements \(f_j\le f\) for which there is an element \(\xi\in A(J_+)\) with
\[
(\xi_j)^\infty=f_j\ \text{ for all }j\in J\qquad\text{and}\qquad(\operatorname{tot}\xi)^\infty=f .
\]
The set \(J\) may be empty. Since \(A(0_+)\) is a point with total 0, the empty family is a partition of \(0^\infty\), and of no other element.

This is [Connes–Consani 2021, Definition 5.5]. In words: \(f\) is the class of a sum of elements whose classes are the \(f_j\), and the sum has a witness in \(A\).

**Lemma 7.4.** If \((f_i)_{i\in I}\) is a partition of \(f\) and \((g_j)_{j\in J}\) a partition of \(g\), then \((f_i\wedge g_j)_{(i,j)\in I\times J}\) is a partition of \(f\wedge g\). In particular, if \(d\le f\), then \((f_i\wedge d)_{i\in I}\) is a partition of \(d\).

*Reference:* [Connes–Consani 2021, Lemma 5.6].

**Proof.** Let \(\xi\) and \(\eta\) be elements as in Definition 7.3. By Lemma 3.3(2), \(\xi\cdot\eta\in A(I_+\wedge J_+)\) has the components \(\xi_i\eta_j\) and the total \(\operatorname{tot}\xi\operatorname{tot}\eta\). By Lemma 7.2(3) their classes are \(f_i\wedge g_j\le f\wedge g\) and \(f\wedge g\). For the last statement take for \((g_j)\) the partition \((d)\) of \(d\), given by any \(y\in A(1_+)\) with \(y^\infty=d\). \(\square\)

**Definition 7.5.** Let \(c\in C^\infty(A)\). The *iterated partitions* of \(c\) are the finite families obtained from the family \((c)\) by finitely many steps of the following kind: replace one member of the family by a partition of this member. A family \((x_k)_{k\in K}\) of elements \(x_k\le c\), indexed by any set \(K\), *covers* \(c\) if there is an iterated partition of \(c\) each of whose members is \(\le x_k\) for some \(k\). The partially ordered set \(C^\infty(A)\) with these covers is the *spectrum* \(\mathfrak{Spec}(A)\).

A *presheaf* on \(\mathfrak{Spec}(A)\) is a contravariant functor \(P\) from \(C^\infty(A)\) to sets, or to Γ-sets. It is a *sheaf* if, for every cover \((x_k)\) of \(c\), the restrictions identify \(P(c)\) with the set of families \((s_k)\in\prod_kP(x_k)\) such that \(s_k\) and \(s_l\) have the same restriction to \(x_k\wedge x_l\) for all \(k,l\).

The empty family is an iterated partition of \(0^\infty\), by Definition 7.3. So the empty family covers \(0^\infty\), as it covers the empty set in a topological space, and a sheaf has a point as its value at \(0^\infty\).

*Reference:* [Connes–Consani 2021, Definition 5.7 and §5.4] describes the iterated partitions by rooted trees whose vertices without successors are the members, which leaves out the empty partition of \(0^\infty\); without it every presheaf on \(C^\infty(HR)=\{0^\infty<1^\infty\}\), for a field \(R\), would be a sheaf, against Theorem 7.8, so we include it.

**Proposition 7.6** (Covers form a pretopology). (1) The family \((c)\) covers \(c\).

(2) If \((x_k)\) covers \(c\) and \(d\le c\), then \((x_k\wedge d)\) covers \(d\).

(3) If \((x_k)_k\) covers \(c\) and \((y_{kl})_l\) covers \(x_k\) for every \(k\), then \((y_{kl})_{k,l}\) covers \(c\).

*Reference:* [Connes–Consani 2021, Lemma 5.8].

**Proof.** We first note two facts. (a) If \((c_i)\) is an iterated partition of \(c\) and \(d\le c\), then \((c_i\wedge d)\) is an iterated partition of \(d\). This follows by induction on the number of steps from Lemma 7.4. (b) If \((c_i)_{i\in I}\) is an iterated partition of \(c\) and \((e_{il})_l\) is an iterated partition of \(c_i\) for each \(i\), then \((e_{il})_{i,l}\) is an iterated partition of \(c\): perform the steps for one member after the other.

(1) is clear. (2) follows from (a), because \(c_i\le x_k\) implies \(c_i\wedge d\le x_k\wedge d\). For (3), let \((c_i)\) be an iterated partition of \(c\) with \(c_i\le x_{k(i)}\), and let \((z_{km})_m\) be an iterated partition of \(x_k\) with each \(z_{km}\) below some \(y_{kl}\). By (a), \((z_{k(i)m}\wedge c_i)_m\) is an iterated partition of \(c_i\). By (b) these families together form an iterated partition of \(c\), and each of its members is below some \(y_{kl}\). \(\square\)

### Three computations

An ideal of a semiring \(R\) is an additive submonoid \(I\) with \(RI\subseteq I\). It is prime if \(I\ne R\) and \(ab\in I\) implies \(a\in I\) or \(b\in I\). The prime ideals form the space \(\operatorname{Spec}R\) with the basic open sets \(D(f)\).

**Lemma 7.7.** Let \(I\) be an ideal of a semiring \(R\) and \(c\in R\). If no power \(c^n\), \(n\ge1\), lies in \(I\), there is a prime ideal that contains \(I\) and does not contain \(c\).

**Proof.** The ideals that contain \(I\) and no power of \(c\) form a set that is closed under unions of chains. By Zorn's lemma it has a maximal element \(\mathfrak p\). Let \(xy\in\mathfrak p\) with \(x,y\notin\mathfrak p\). The ideals \(\mathfrak p+xR\) and \(\mathfrak p+yR\) are strictly larger, so \(c^i=p+xr\) and \(c^j=p'+yr'\) with \(p,p'\in\mathfrak p\). Then \(c^{i+j}=pp'+pyr'+p'xr+xyrr'\in\mathfrak p\), a contradiction. So \(\mathfrak p\) is prime. \(\square\)

For rings this is the statement that the radical of an ideal is the intersection of the prime ideals that contain it [Stacks, Tag [00E0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Zariski-topology)].

**Theorem 7.8** (Semirings and rings). Let \(R\) be a semiring, and let \(c\) and \(x_k\) (\(k\in K\)) be elements of \(R\) with \(x_k^\infty\le c^\infty\).

1. The family \((x_k^\infty)\) covers \(c^\infty\) in \(\mathfrak{Spec}(HR)\) if and only if some power \(c^n\), \(n\ge1\), lies in the ideal generated by the \(x_k\).
2. The map \(b^\infty\mapsto D(b)\) is an isomorphism from \(C^\infty(HR)\) to the partially ordered set of basic open sets of \(\operatorname{Spec}R\), and \((x_k^\infty)\) covers \(c^\infty\) if and only if \(D(c)=\bigcup_kD(x_k)\).

Hence the sheaves on \(\mathfrak{Spec}(HR)\) are the sheaves on the topological space \(\operatorname{Spec}R\), restricted to the basic open sets [Stacks, Tag [009O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-restrict-basis-equivalence)].

*Reference:* [Connes–Consani 2021, Lemma 5.10, Propositions 6.1 and 6.5].

**Proof.** We use an elementary fact. (F) If \(w=\sum_{j\in J}v_j\) in \(R\) and \(m\ge1\), then \(w^{m|J|+1}\) lies in the ideal generated by the \(v_j^m\). Indeed every monomial of degree \(m|J|+1\) in the \(v_j\) contains some \(v_j\) with exponent at least \(m\); for empty \(J\) the statement reads \(0\in\{0\}\).

(1) *Claim.* Let \((c_i)_{i\in I}\) be an iterated partition of \(c^\infty\) and let \(y_i\in R\) be any elements with \(y_i^\infty=c_i\). Then some power of \(c\) lies in the ideal \((y_i:i\in I)\). For the family \((c^\infty)\) this holds because \(y^\infty=c^\infty\) gives \(c\in\operatorname{rad}(y)\). Suppose the claim holds for \((c_i)\), and replace \(c_{i_0}\) by a partition \((d_j)_{j\in J}\), given by \(\xi\in R^J=HR(J_+)\). Put \(s=\operatorname{tot}\xi=\sum_j\xi_j\), so \(s^\infty=c_{i_0}\). Let \(z_j\) be any elements with \(z_j^\infty=d_j=\xi_j^\infty\). There is \(m\ge1\) with \(\xi_j^m\in z_jR\) for all \(j\), and by (F) the element \(s^{m|J|+1}\) lies in \((z_j:j\in J)\). The claim for \((c_i)\), with \(s\) as the element for \(i_0\), gives \(c^n=as+w\) with \(w\in(y_i:i\ne i_0)\). Expanding \((as+w)^{m|J|+1}\) shows that \(c^{n(m|J|+1)}\) lies in \((z_j:j\in J)+(y_i:i\ne i_0)\). This proves the claim.

Now let \((x_k^\infty)\) cover \(c^\infty\), by an iterated partition \((c_i)\) with \(c_i\le x_{k(i)}^\infty\). Choose \(y_i\) with \(y_i^\infty=c_i\). Then \(y_i^m\in x_{k(i)}R\) for some \(m\ge1\) and all \(i\), and \(c^n=\sum_ia_iy_i\) by the claim. By (F), \(c^{n(m|I|+1)}\) lies in the ideal generated by the \(y_i^m\), hence in the ideal generated by the \(x_k\).

Conversely let \(c^n=\sum_{k\in K_0}a_kx_k\) with \(K_0\subseteq K\) finite. The element \(\xi=(a_kx_kc)_{k\in K_0}\) of \(HR((K_0)_+)\) has total \(c^{n+1}\), whose class is \(c^\infty\), and its components have classes \((a_kx_kc)^\infty\), which are below \(c^\infty\) and below \(x_k^\infty\). So these classes form a partition of \(c^\infty\) whose members are below the \(x_k^\infty\). If \(K_0\) is empty, then \(c\) is nilpotent and this is the empty partition of \(0^\infty\).

(2) By Lemma 7.7 for the ideal \(bR\), \(D(c)\subseteq D(b)\) holds exactly when \(c^n\in bR\) for some \(n\), that is, when \(c^\infty\le b^\infty\). By Lemma 7.7 for the ideal generated by the \(x_k\), \(D(c)\subseteq\bigcup_kD(x_k)\) holds exactly when some power of \(c\) lies in this ideal. By (1) this is the condition for a cover. The basic open sets are closed under finite intersections, since \(D(b)\cap D(c)=D(bc)\), so a sheaf on them is the same as a sheaf on the space. \(\square\)

**Theorem 7.9** (Monoids). Let \(M\) be a monoid. In \(\mathfrak{Spec}(\mathbb SM)\) a family covers an element \(c\ne0^\infty\) if and only if \(c\) is one of its members, and every family covers \(0^\infty\), also the empty one. Hence the sheaves on \(\mathfrak{Spec}(\mathbb SM)\) are the presheaves on the basic open sets of \(\operatorname{Spec}M\) whose value on the empty set is a point. They are the sheaves on the topological space \(\operatorname{Spec}M\), restricted to the basic open sets.

*Reference:* [Connes–Consani 2021, Proposition 6.2].

**Proof.** An element of \(\mathbb SM(J_+)=M\wedge J_+\) is the base point, with all components and the total equal to 0, or an element \(m\wedge j_0\) with \(m\ne0\), which has the component \(m\) at \(j_0\), the components 0 elsewhere, and the total \(m\). So a partition of \(f\ne0^\infty\) consists of \(f\) and of copies of \(0^\infty\), and a partition of \(0^\infty\) consists of copies of \(0^\infty\) or is empty. By induction every iterated partition of \(c\ne0^\infty\) has \(c\) as a member. So a cover of \(c\) has a member \(\ge c\), hence equal to \(c\); conversely a family with the member \(c\) covers \(c\). The empty family is an iterated partition of \(0^\infty\), so every family covers \(0^\infty\).

If \(c\) is a member of the cover, a family \((s_k)\) as in Definition 7.5 is determined by its entry at \(c\), which is arbitrary. So the sheaf condition holds for these covers, and for \(0^\infty\) it says that \(P(0^\infty)\) is a point. In the space \(\operatorname{Spec}M\), a non-empty basic open set \(D(b)\) has a largest point, the prime ideal of the elements that divide no power of \(b\), and an open set that contains this point contains \(D(b)\). So every open cover of \(D(b)\) has a member that contains \(D(b)\), and the sheaves on the space are described by the same conditions. \(\square\)

**Example 7.10** (The local \(\mathbb S\)-algebra at infinity). Let \(A=\|H\mathbb Q\|_1\), so \(M=A(1_+)\) is the set of rational numbers \(r\) with \(|r|\le1\). For \(s\ne0\) we have \(r\in sM\) exactly when \(|r|\le|s|\). Hence \(\operatorname{rad}(s)=M\) if \(|s|=1\), \(\operatorname{rad}(s)=\{r:|r|<1\}\) if \(0<|s|<1\), and \(\operatorname{rad}(0)=\{0\}\). So
\[
C^\infty(A)=\{0^\infty<u<1^\infty\},\qquad u=s^\infty\ \text{for }0<|s|<1 .
\]
This is the partially ordered set of open sets of a space with a generic point and a closed point, as for a discrete valuation ring; the two points are the prime ideals \(\{0\}\) and \(\{r:|r|<1\}\) of \(M\). But the element \(\xi=(\tfrac12,\tfrac12)\) of \(A(2_+)\) has two components of class \(u\) and the total 1. So \((u,u)\) is a partition of \(1^\infty\), and the single element \(u\) covers \(1^\infty\). For a sheaf \(P\) the restriction \(P(1^\infty)\to P(u)\) is therefore bijective: sheaves do not see the closed point. The same holds for \(\|H\mathbb R\|_1\). This is [Connes–Consani 2021, Proposition 7.16].

### The structure presheaf

**Definition 7.11.** Let \(W\subseteq A(1_+)\) be a multiplicative subset: \(1\in W\) and \(WW\subseteq W\). For \(X\) in \(\mathrm{Fin}_\ast\) let \((W^{-1}A)(X)\) be the quotient of \(W\times A(X)\) by the relation
\[
(s,\xi)\sim(t,\eta)\iff u\cdot t\cdot\xi=u\cdot s\cdot\eta\ \text{ for some }u\in W,
\]
and write \(\xi/s\) for the class of \((s,\xi)\).

As for rings, this is an equivalence relation: if \(u\cdot t\cdot\xi=u\cdot s\cdot\eta\) and \(v\cdot r\cdot\eta=v\cdot t\cdot\zeta\), then \(uvt\cdot r\cdot\xi=uvt\cdot s\cdot\zeta\). The maps \(A(f)\) commute with the action of \(A(1_+)\), so \(W^{-1}A\) is a Γ-set, with base point \(\ast/1\). The product \((\xi/s)\cdot(\eta/t)=(\xi\cdot\eta)/(st)\) is well defined, because \((a\cdot\xi)\cdot(b\cdot\eta)=ab\cdot(\xi\cdot\eta)\) for \(a,b\in A(1_+)\), as in the proof of Proposition 5.2. It makes \(W^{-1}A\) an \(\mathbb S\)-algebra with unit \(1/1\), and \(\xi\mapsto\xi/1\) is a morphism \(A\to W^{-1}A\) [Connes–Consani 2021, Lemmas 7.1 and 7.2]. If \(0\in W\), then \(W^{-1}A=\ast\).

**Proposition 7.12.** (1) For a semiring \(R\) and a multiplicative subset \(W\), the map \((r_x)_x/s\mapsto(r_x/s)_x\) is an isomorphism \(W^{-1}(HR)\cong H(W^{-1}R)\).

(2) For a monoid \(M\) and a multiplicative subset \(W\), \(W^{-1}(\mathbb SM)=\mathbb S(W^{-1}M)\).

*Reference:* [Connes–Consani 2021, Proposition 7.3].

**Proof.** (1) The map is well defined and compatible with sums, products and the maps \(HR(f)\). It is surjective, because finitely many fractions have a common denominator. It is injective: if \(r_x/s=r'_x/t\) for all \(x\in X^\circ\), there are \(u_x\in W\) with \(u_xtr_x=u_xsr'_x\), and the product \(u\) of the finitely many \(u_x\) satisfies \(utr_x=usr'_x\) for all \(x\). (2) Both sides have the value \((W^{-1}M)\wedge X\) at \(X\). \(\square\)

**Definition 7.13.** For \(f\in A(1_+)\) let \(W_f\) be the set of the elements \(g\) that divide a power \(f^n\), \(n\ge1\); that is, the \(g\) with \(f^\infty\le g^\infty\). It is a multiplicative subset that depends only on \(f^\infty\). The *structure presheaf* of \(\mathfrak{Spec}(A)\) is
\[
\mathcal O_A(f^\infty)=W_f^{-1}A .
\]
If \(f^\infty\le g^\infty\), then \(W_g\subseteq W_f\), which gives the restriction map \(\mathcal O_A(g^\infty)\to\mathcal O_A(f^\infty)\).

This is [Connes–Consani 2021, Lemma 7.4 and Definition 7.8]; the structure sheaf is defined there as the sheaf associated with \(\mathcal O_A\).

**Proposition 7.14.** (1) For a ring \(R\), \(\mathcal O_{HR}(f^\infty)=H(R_f)\). The presheaf \(\mathcal O_{HR}\) is a sheaf: it is \(H\) of the structure sheaf of \(\operatorname{Spec}R\).

(2) For a monoid \(M\), \(\mathcal O_{\mathbb SM}(f^\infty)=\mathbb S(M_f)\). This presheaf is a sheaf: it is \(\mathbb S\) of the structure sheaf of the monoid scheme \(\operatorname{Spec}M\).

(3) For \(A=\|H\mathbb Q\|_1\), \(\mathcal O_A(1^\infty)=A\), \(\mathcal O_A(u)=H\mathbb Q\) and \(\mathcal O_A(0^\infty)=\ast\), with the inclusion \(A\subseteq H\mathbb Q\) as restriction. This presheaf is not a sheaf.

*Reference:* [Connes–Consani 2021, Propositions 7.9 and 7.16].

**Proof.** (1) The elements of \(W_f\) are invertible in \(R_f\), so \(W_f^{-1}R=R_f\), and Proposition 7.12 applies. The presheaf \(D(f)\mapsto R_f\) on the basic open sets is the structure sheaf of \(\operatorname{Spec}R\) [Stacks, Tag [01HV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-spec-sheaves)], and a finite product of sheaves is a sheaf, which gives the sheaf property at each level \(X\) for the covers of Theorem 7.8.

(2) This follows from Proposition 7.12 and Theorem 7.9; the value at \(0^\infty\) is \(\mathbb S\) of the zero monoid, a point.

(3) \(W_1=\{\pm1\}\) consists of invertible elements, so \(\mathcal O_A(1^\infty)=A\). \(W_u\) is the set of non-zero elements of \(M\). The map \(\xi/s\mapsto s^{-1}\xi\) from \(W_u^{-1}A\) to \(H\mathbb Q\) is injective because \(A\subseteq H\mathbb Q\). It is surjective because \(\psi=(\psi/n)/(1/n)\) for an integer \(n\ge1\) with \(n\ge\sum|\psi(x)|\). Since \(0\in W_0\), \(\mathcal O_A(0^\infty)=\ast\). By Example 7.10 a sheaf has the same values at \(1^\infty\) and at \(u\), and \(\|H\mathbb Q\|_1\ne H\mathbb Q\). \(\square\)

So at the archimedean place the structure presheaf carries more information than any sheaf: a sheaf that agrees with \(\mathcal O_A\) at \(u\) has the value \(H\mathbb Q\) at \(1^\infty\). For this reason [Connes–Consani 2021, §5.4 and §7.6] keeps the partially ordered set with its covers and the presheaf, and does not pass to the topos of sheaves.

**Proposition 7.15** (Morphisms and quotients). (1) A morphism of \(\mathbb S\)-algebras \(\rho:A\to B\) induces a map \(C^\infty(A)\to C^\infty(B)\), \(b^\infty\mapsto\rho(b)^\infty\), which preserves the order, the elements \(1^\infty\) and \(0^\infty\), meets, partitions and covers.

(2) Let \(G\) be a subgroup of the invertible elements of \(A(1_+)\). The map of (1) for the quotient morphism \(A\to A/G\) is an isomorphism of partially ordered sets, and partitions and covers correspond. So \(\mathfrak{Spec}(A/G)\) and \(\mathfrak{Spec}(A)\) are the same.

*Reference:* [Connes–Consani 2021, Theorem 5.11 and Proposition 7.11].

**Proof.** (1) If \(c^n=ba\), then \(\rho(c)^n=\rho(b)\rho(a)\), so the map is well defined and preserves the order. It preserves meets because \(\rho(bc)=\rho(b)\rho(c)\). If \(\xi\) gives a partition of \(f\), then \(\rho(\xi)\) has the components \(\rho(\xi_j)\) and the total \(\rho(\operatorname{tot}\xi)\), so it gives a partition of the image of \(f\). Hence iterated partitions and covers are preserved.

(2) Let \(M=A(1_+)\). In \(M/G\) the relation \(\bar c^n\in\bar b\,(M/G)\) says \(c^n\in bMG=bM\). So the map is an isomorphism of partially ordered sets. Every element of \((A/G)(J_+)\) is the class of an element \(\xi\) of \(A(J_+)\), and its components and its total are the classes of those of \(\xi\). So the partitions in \(A/G\) are the images of the partitions in \(A\). \(\square\)

For example, let \(\mathbb A_K\) be the ring of adèles of a global field \(K\). The \(\mathbb S\)-algebra \(H\mathbb A_K/K^\times\) has the adèle class space \(\mathbb A_K/K^\times\) as its first level, with the sum sets of Proposition 5.2. Its spectrum is that of the ring \(\mathbb A_K\): the basic open sets of \(\operatorname{Spec}\mathbb A_K\) with their open covers [Connes–Consani 2021, Corollary 7.12]. The quotient of a ring by a subgroup of its units has no meaning in the category of rings; in the category of \(\mathbb S\)-algebras it is an object with a spectrum.

## 8. Riemann–Roch for the compactification of \(\operatorname{Spec}\mathbb Z\)

A reference for this section is [Connes–Consani 2023]. For a curve over a finite field \(\mathbb F_q\), the Riemann–Roch theorem compares the dimensions over \(\mathbb F_q\) of two spaces \(H^0(D)\) and \(H^1(D)\) attached to a divisor; see *Weil's proof for curves and what is missing over the integers*. On \(\overline{\operatorname{Spec}\mathbb Z}\) the constants are the global sections of \(\mathcal O\), the \(\mathbb S\)-algebra \(\mathbb S[\pm1]\) (Proposition 6.6). We define modules \(H^0(D)\) and \(H^1(D)\) over \(\mathbb S[\pm1]\), the second with an additional relation, and a dimension with integer values. The Riemann–Roch formula is then proved from these definitions.

### Tolerant modules and their dimension

By Proposition 3.5(2), a module over \(\mathbb S[\pm1]\) is a Γ-set \(E\) with an involution, written \(\xi\mapsto-\xi\). Examples are \(HA\) for an abelian group \(A\), and the sub-Γ-sets of \(HA\) that are stable under the sign, such as \(\|H\mathbb Z\|_\lambda\).

**Definition 8.1.** A *tolerance relation* on a set is a reflexive and symmetric relation. A *tolerant \(\mathbb S[\pm1]\)-module* is an \(\mathbb S[\pm1]\)-module \(E\) with a tolerance relation \(\mathcal R_X\) on every set \(E(X)\), such that the maps \(E(f)\) and the involution preserve the relations. An \(\mathbb S[\pm1]\)-module without further data is considered as a tolerant one, with equality as relation.

**Example 8.2.** Let \(A\) be an abelian group with a metric \(d\) that is invariant under translations, and let \(\lambda>0\). On \(HA\) put
\[
(\varphi,\psi)\in\mathcal R_X\iff\sum_{x\in X^\circ}d(\varphi(x),\psi(x))\le\lambda .
\]
The maps \(HA(f)\) preserve these relations, because \(d(a+b,a'+b')\le d(a,a')+d(b,b')\). This tolerant module is written \((A,d)_\lambda\). For the circle \(\mathbb R/\mathbb Z\), with \(d(x,y)\) the distance from a representative of \(x-y\) to the nearest integer, we write \(U(1)_\lambda=(\mathbb R/\mathbb Z,d)_\lambda\). If \(p:A'\to A\) is a surjective morphism of abelian groups and \((HA,\mathcal R)\) is a tolerant module, the *pullback* \(p^\ast(HA,\mathcal R)\) is \(HA'\) with the relations \(\{(\varphi,\psi):(p\circ\varphi,p\circ\psi)\in\mathcal R_X\}\).

**Definition 8.3.** Let \((E,\mathcal R)\) be a tolerant \(\mathbb S[\pm1]\)-module. A finite subset \(F\subseteq E(1_+)\) is *generating* if

1. two different elements of \(F\) are never related by \(\mathcal R_{1_+}\), and
2. for every \(x\in E(1_+)\) there are coefficients \(\alpha_f\in\{-1,0,1\}\), \(f\in F\), and an element \(y\in E(1_+)\) that is a sum of the family \((\alpha_ff)_{f\in F}\), in the sense of Definition 1.4, with \((x,y)\in\mathcal R_{1_+}\).

The *dimension* \(\dim(E,\mathcal R)\) is the smallest number of elements of a generating set, and \(\infty\) if there is none.

Definitions 8.1 and 8.3 are those of [Connes–Consani 2023, Appendix A]. Here \(\alpha_ff\) is \(f\), \(-f\) or the base point, and the sum needs a witness in \(E(F_+)\). For a vector space \(V\) over \(\mathbb F_3\), the module \(HV\) with equality as relation has the generating sets that span \(V\), because \(\mathbb F_3=\{-1,0,1\}\); so \(\dim HV=\dim_{\mathbb F_3}V\). The first level of \(\mathbb S[\pm1]\) is the multiplicative monoid of \(\mathbb F_3\). This is why the number 3 appears below.

**Lemma 8.4** (Pullback). Let \(p:A'\to A\) be a surjective morphism of abelian groups and \((HA,\mathcal R)\) a tolerant module. Then \(\dim p^\ast(HA,\mathcal R)=\dim(HA,\mathcal R)\).

**Proof.** In \(HA\) and \(HA'\) every family has exactly one sum, and \(p\) commutes with sums and signs. Let \(F\) be generating for \((HA,\mathcal R)\), and let \(F'\) contain one preimage of each element of \(F\). Different elements of \(F'\) have different, hence unrelated, images, so they are unrelated. For \(x'\in A'\) there are \(\alpha_f\) with \(p(x')\) related to \(\sum\alpha_ff=p(\sum\alpha_ff')\), so \(x'\) is related to \(\sum\alpha_ff'\). Hence \(F'\) is generating. Conversely let \(F'\) be generating for the pullback. Two different elements of \(F'\) with the same image would be related, by reflexivity. So \(p\) is injective on \(F'\), the set \(p(F')\) satisfies (1), and it satisfies (2) because \(p\) is surjective. \(\square\)

### Two computations

**Theorem 8.5** (The dimension of \(\|H\mathbb Z\|_n\)). For every integer \(n\ge0\),
\[
\dim\|H\mathbb Z\|_n=\big\lceil\log_3(2n+1)\big\rceil .
\]
For \(n\notin\{2,5\}\) there is a generating set of this size that consists of positive integers with sum \(n\). For \(n=2\) and \(n=5\) there is none.

*Reference:* [Connes–Consani 2023, Proposition 3.3]. The proof below is different.

**Proof.** The first level of \(\|H\mathbb Z\|_n\) is the set of integers \(x\) with \(|x|\le n\). A family \((x_f)\) of such integers has a witness exactly when \(\sum|x_f|\le n\), and its sum is then \(\sum x_f\). So a finite set \(F\) is generating if and only if every integer \(x\) with \(|x|\le n\) can be written
\[
x=\sum_{f\in F}\alpha_ff\qquad\text{with }\alpha_f\in\{-1,0,1\}\text{ and }\sum_{f\in F}|\alpha_ff|\le n .
\tag{8.1}
\]

*Lower bound.* There are \(3^{|F|}\) choices of coefficients and \(2n+1\) integers to reach. So \(3^{|F|}\ge2n+1\).

*Chains.* Call integers \(1\le f_1<f_2<\dots<f_\kappa\) a *chain* if \(f_i\le2s_{i-1}+1\) for all \(i\), where \(s_i=f_1+\dots+f_i\) and \(s_0=0\). We prove three facts.

(a) For a chain, every integer \(x\) with \(|x|\le s_\kappa\) is a sum \(\sum\alpha_if_i\) with \(\alpha_i\in\{-1,0,1\}\). This is clear for \(\kappa=0\). Let \(\kappa\ge1\). If \(|x|\le s_{\kappa-1}\), use the chain \(f_1,\dots,f_{\kappa-1}\). Otherwise we may assume \(s_{\kappa-1}<x\le s_\kappa\), replacing \(x\) by \(-x\) if necessary. Then \(x-f_\kappa\le s_{\kappa-1}\) and \(x-f_\kappa\ge s_{\kappa-1}+1-(2s_{\kappa-1}+1)=-s_{\kappa-1}\), and induction applies to \(x-f_\kappa\).

(b) A chain has \(s_i\le3s_{i-1}+1\), hence \(s_\kappa\le(3^\kappa-1)/2\). If \(s_\kappa<(3^\kappa-1)/2\), there is a chain of length \(\kappa\) with sum \(s_\kappa+1\). Indeed \(f_i<2s_{i-1}+1\) for some \(i\), since otherwise \(s_\kappa=(3^\kappa-1)/2\); take the largest such \(i\) and replace \(f_i\) by \(f_i+1\). The inequality for \(i\) still holds. For \(j>i\) we have \(f_j=2s_{j-1}+1\), and the inequality for \(j\) still holds because the partial sums have grown. The sequence is still strictly increasing, because \(f_{i+1}=2s_i+1\ge2f_i+1>f_i+1\) when \(i<\kappa\).

(c) The integers \(1,2,\dots,\kappa\) form a chain with sum \(\kappa(\kappa+1)/2\), since \(i\le(i-1)i+1\). By (b), every integer \(n\) with \(\kappa(\kappa+1)/2\le n\le(3^\kappa-1)/2\) is the sum of a chain of length \(\kappa\).

*Upper bound.* For \(n=0\) the empty set is generating. Let \(n\ge1\) and \(\kappa=\lceil\log_3(2n+1)\rceil\), so that \(\kappa\ge1\) and \((3^{\kappa-1}-1)/2<n\le(3^\kappa-1)/2\). Suppose \(n\ge\kappa(\kappa+1)/2\). By (c) there is a chain of length \(\kappa\) with sum \(n\). By (a) every \(x\) with \(|x|\le n\) is \(\sum\alpha_if_i\), and \(\sum|\alpha_if_i|\le s_\kappa=n\). So (8.1) holds, and the chain is a generating set with \(\kappa\) positive elements of sum \(n\).

The inequality \(n\ge\kappa(\kappa+1)/2\) holds for \(\kappa=1\), where \(n=1\). It holds for \(\kappa\ge4\), because \(n\ge(3^{\kappa-1}+1)/2\) and \(3^{\kappa-1}+1\ge\kappa(\kappa+1)\) for \(\kappa\ge4\): this is \(28\ge20\) for \(\kappa=4\), and if it holds for \(\kappa\), then \(3^\kappa+1=3(3^{\kappa-1}+1)-2\ge3\kappa(\kappa+1)-2\ge(\kappa+1)(\kappa+2)\), since the difference of the last two terms is \(2\kappa^2-4\). For \(\kappa=2\) the possible values are \(n=2,3,4\), and the inequality fails only for \(n=2\). For \(\kappa=3\) they are \(n=5,\dots,13\), and it fails only for \(n=5\). For \(n=2\) the set \(\{1,2\}\) is generating. For \(n=5\) the set \(\{1,2,3\}\) is generating: \(4=1+3\) and \(5=2+3\), and these sums satisfy (8.1). In these two cases \(\kappa\) different positive integers have a sum of at least \(\kappa(\kappa+1)/2>n\), so there is no generating set with \(\kappa\) positive elements of sum \(n\). \(\square\)

For \(n=(3^\kappa-1)/2\) the chain is \(1,3,\dots,3^{\kappa-1}\), and the representation of (a) is unique, since \(3^\kappa\) choices of coefficients reach \(3^\kappa\) integers. This is the balanced ternary expansion of integers [Connes–Consani 2023, Lemma 3.1]. The two exceptions concern generating sets of positive integers only: \(\{1,-1\}\) for \(n=2\) and \(\{1,-1,3\}\) for \(n=5\) are generating sets of minimal size whose elements have absolute values of sum \(n\), since \(2=1-(-1)\) and \(5=3+1-(-1)\).

**Theorem 8.6** (The dimension of \(U(1)_\lambda\)). For \(\lambda\ge\tfrac12\), \(\dim U(1)_\lambda=0\). For \(0<\lambda<\tfrac12\),
\[
\dim U(1)_\lambda=\Big\lceil\log_3\frac1{2\lambda}\Big\rceil .
\]

*Reference:* [Connes–Consani 2023, Proposition 4.1].

**Proof.** In \(U(1)_\lambda\) all sums exist. Condition (2) of Definition 8.3 says that every point of the circle is at distance at most \(\lambda\) from some \(\sum\alpha_ff\). If \(\lambda\ge\frac12\), every point is at distance at most \(\lambda\) from 0, which is the empty sum. So the empty set is generating.

Let \(\lambda<\frac12\) and \(m=\lceil\log_3(1/(2\lambda))\rceil\). Then \(m\ge1\) and
\[
\tfrac12\,3^{-m}\le\lambda<\tfrac32\,3^{-m}.
\]
*Lower bound.* If \(F\) is generating, the \(3^{|F|}\) closed arcs of length \(2\lambda\) centred at the points \(\sum\alpha_ff\) cover the circle, which has length 1. So \(3^{|F|}\cdot2\lambda\ge1\), and \(|F|\ge m\).

*Upper bound.* Let \(F\) be the set of the classes of \(3^{-1},3^{-2},\dots,3^{-m}\). For \(i < j\le m\) the distance between the classes of \(3^{-i}\) and \(3^{-j}\) is \(3^{-i}-3^{-j}\), which is at least \(2\cdot3^{-m}\) and therefore bigger than \(\lambda\). This is condition (1). Let \(x\) be a point of the circle, with a representative \(t\in[-\frac12,\frac12]\). Put \(N=(3^m-1)/2\). Since \(|3^mt|\le N+\frac12\), there is an integer \(q\) with \(|q|\le N\) and \(|3^mt-q|\le\frac12\). By fact (a) of the last proof for the chain \(1,3,\dots,3^{m-1}\), \(q=\sum_{i=0}^{m-1}\alpha_i3^i\) with \(\alpha_i\in\{-1,0,1\}\). So \(y=q3^{-m}=\sum_i\alpha_i3^{i-m}\) is a sum of elements \(\pm f\) with \(f\in F\), and \(d(x,y)\le\frac12\,3^{-m}\le\lambda\). This is condition (2). \(\square\)

### The cohomology of a divisor

We use the adèles of \(\mathbb Q\). Let \(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\), let \(\mathbb A_f\) be the ring of finite adèles, that is, of the families \((x_p)\) with \(x_p\in\mathbb Q_p\) and \(x_p\in\mathbb Z_p\) for almost all \(p\), and let \(\mathbb A=\mathbb A_f\times\mathbb R\). The field \(\mathbb Q\) is embedded diagonally in \(\mathbb A_f\) and in \(\mathbb A\). For every rational number \(c>0\),
\[
\mathbb A_f=\mathbb Q+c\widehat{\mathbb Z},\qquad\mathbb Q\cap c\widehat{\mathbb Z}=c\mathbb Z.
\tag{8.2}
\]
It suffices to take \(c=1\). A rational number that is a \(p\)-adic integer for all \(p\) is an integer. Let \(x\in\mathbb A_f\), and let \(S\) be the finite set of primes with \(x_p\notin\mathbb Z_p\). For \(p\in S\) write \(x_p=r_p+z_p\) with \(r_p\in\mathbb Z[1/p]\) and \(z_p\in\mathbb Z_p\), and put \(r=\sum_{p\in S}r_p\). Then \(x-r\in\widehat{\mathbb Z}\), because \(r_p\) is an \(\ell\)-adic integer for every prime \(\ell\ne p\).

**Definition 8.7.** Let \(D=\sum_pa_p\{p\}+a\{\infty\}\) be an Arakelov divisor and \(c_D=\prod_pp^{-a_p}\). Let \(\mathcal O_D\subseteq H\mathbb A\) be the sub-Γ-set of the \(\varphi\in H\mathbb A(X)\) whose finite components lie in \(c_D\widehat{\mathbb Z}\) and whose real components satisfy \(\sum_{x\in X^\circ}|\varphi(x)_\infty|\le e^a\). Let
\[
\psi_D:H\mathbb Q\times\mathcal O_D\to H\mathbb A,\qquad(q,\varphi)\mapsto q+\varphi .
\]
Then \(H^0(D)\) is the kernel of \(\psi_D\), that is, the \(\mathbb S[\pm1]\)-module of the pairs \((q,\varphi)\) with \(q+\varphi=0\). And \(H^1(D)\) is the tolerant \(\mathbb S[\pm1]\)-module \((H\mathbb A,\mathcal R^D)\) with
\[
(z,z')\in\mathcal R^D_X\iff z-z'\ \text{lies in the image of }\psi_D\text{ at }X .
\]
We write \(h^i(D)=\dim H^i(D)\).

The relations \(\mathcal R^D\) are reflexive and symmetric, and the maps \(H\mathbb A(f)\) preserve them, because the image of \(\psi_D\) is a sub-Γ-set of \(H\mathbb A\) that contains 0 and is stable under the sign. In \(H^0(D)\) the element \(q\) determines \(\varphi=-q\), and by (8.2) the conditions on \(q\) are \(q(x)\in c_D\mathbb Z\) and \(\sum|q(x)|\le e^a\). So \(H^0(D)\) is the module of global sections of \(\mathcal O(D)\) of Proposition 6.8.

These are the descriptions of [Connes–Consani 2023, Proposition 2.2], which we take as definitions. They follow the adèlic form of the cohomology of a divisor on a curve with function field \(K\), where \(H^0(D)=K\cap\mathcal O_D\) and \(H^1(D)=\mathbb A_K/(K+\mathcal O_D)\). Here the real component of \(\mathcal O_D\) is an interval, not a group. So \(\mathcal O_D\) is kept as a Γ-set, and the quotient is replaced by a tolerance relation.

**Proposition 8.8** (Reduction to the archimedean part). Let \(D\) be an Arakelov divisor and \(\lambda=e^{\deg D}\).

1. \(H^0(D)\cong\|H\mathbb Z\|_{\lfloor\lambda\rfloor}\) as \(\mathbb S[\pm1]\)-modules.
2. There is a surjective morphism of groups \(\pi:\mathbb A\to\mathbb R/\mathbb Z\) such that \(H^1(D)=\pi^\ast U(1)_\lambda\). Hence \(h^1(D)=\dim U(1)_\lambda\).

In particular \(h^0(D)\) and \(h^1(D)\) depend only on the degree of \(D\).

*Reference:* [Connes–Consani 2023, Proposition 2.2 and Appendix A]. There \(\pi\) is described as the projection of an adèle to its real component modulo a lattice; that map does not vanish on \(\mathbb Q\), although every rational number is related to 0, so we define \(\pi\) differently.

**Proof.** Write \(c=c_D\). Then \(\deg D=a-\log c\), so \(e^a=c\lambda\).

(1) Division by \(c\) identifies \(H^0(D)(X)\) with the set of \(n\in\mathbb Z^{X^\circ}\) with \(\sum|n(x)|\le\lambda\). Since the sum is an integer, this is \(\|H\mathbb Z\|_{\lfloor\lambda\rfloor}(X)\).

(2) For an adèle \(w=(w_f,w_\infty)\) choose by (8.2) a rational number \(r\) with \(w_f-r\in c\widehat{\mathbb Z}\), and put
\[
\pi(w)=\text{the class of }(w_\infty-r)/c\text{ in }\mathbb R/\mathbb Z .
\]
By (8.2), \(r\) is unique up to \(c\mathbb Z\), so \(\pi\) is well defined. It is a surjective morphism of groups, \(\pi(q)=0\) for \(q\in\mathbb Q\), and \(\pi(w)\) is the class of \(w_\infty/c\) when \(w_f\in c\widehat{\mathbb Z}\).

Let \(z\in H\mathbb A(X)\). If \(z=q+\varphi\) with \(q\in H\mathbb Q(X)\) and \(\varphi\in\mathcal O_D(X)\), then \(\pi(z(x))\) is the class of \(\varphi(x)_\infty/c\), so \(\sum_xd(\pi(z(x)),0)\le e^a/c=\lambda\). Conversely suppose \(\sum_xd(\pi(z(x)),0)\le\lambda\). For each \(x\) choose \(r_x\in\mathbb Q\) with \(z(x)_f-r_x\in c\widehat{\mathbb Z}\), and a real number \(t_x\) in the class \(\pi(z(x))\) with \(|t_x|=d(\pi(z(x)),0)\). Then \(z(x)_\infty-r_x=ct_x+cn_x\) with \(n_x\in\mathbb Z\). Put \(q(x)=r_x+cn_x\) and \(\varphi(x)=z(x)-q(x)\). The finite component of \(\varphi(x)\) lies in \(c\widehat{\mathbb Z}\), its real component is \(ct_x\), and \(\sum_x|ct_x|\le c\lambda=e^a\). So \(z=q+\varphi\) lies in the image of \(\psi_D\).

Hence \((z,z')\in\mathcal R^D_X\) if and only if \(\sum_xd(\pi(z(x)),\pi(z'(x)))\le\lambda\). This says \(H^1(D)=\pi^\ast U(1)_\lambda\), and Lemma 8.4 gives the dimension. \(\square\)

**Theorem 8.9** (Riemann–Roch for \(\overline{\operatorname{Spec}\mathbb Z}\)). Let \(D\) be an Arakelov divisor of degree \(\delta\), and \(\lambda=e^\delta\). Then
\[
h^0(D)=\big\lceil\log_3(2\lfloor\lambda\rfloor+1)\big\rceil,\qquad
h^1(D)=\begin{cases}0&\lambda\ge\frac12\\ \big\lceil\log_3\frac1{2\lambda}\big\rceil&\lambda<\frac12\end{cases}
\]
and
\[
h^0(D)-h^1(D)=\Big\lceil\frac{\delta+\log2}{\log3}\Big\rceil'-\mathbf 1_L(\delta).
\tag{8.3}
\]
Here \(\lceil t\rceil'=\lceil t\rceil\) for \(t\ge0\) and \(\lceil t\rceil'=-\lceil-t\rceil\) for \(t\le0\), and \(\mathbf 1_L\) is the indicator function of the set \(L\) of the real numbers \(\delta\) with \(3^k<2e^\delta<3^k+1\) for some integer \(k\ge0\).

*Reference:* [Connes–Consani 2023, Theorem 4.3].

**Proof.** The formulas for \(h^0\) and \(h^1\) follow from Proposition 8.8 and Theorems 8.5 and 8.6. Put \(t=\log_3(2\lambda)=(\delta+\log2)/\log3\).

Let \(\lambda<\frac12\), so \(t<0\). Then \(\lfloor\lambda\rfloor=0\) and \(h^0=0\), and \(h^1=\lceil-t\rceil\). Also \(\delta\notin L\), because \(2\lambda<1\). So both sides of (8.3) are \(-\lceil-t\rceil\).

Let \(\lambda\ge\frac12\), so \(h^1=0\). Let \(k\ge0\) be the integer with \(3^k\le2\lambda<3^{k+1}\). There are three cases.

- \(2\lambda=3^k\). Then \(t=k\), \(\lfloor\lambda\rfloor=(3^k-1)/2\), \(h^0=k\) and \(\delta\notin L\).
- \(3^k<2\lambda<3^k+1\). Then \(\delta\in L\) and \(\lceil t\rceil=k+1\). Since \((3^k-1)/2<\lambda<(3^k+1)/2\), we get \(\lfloor\lambda\rfloor=(3^k-1)/2\) and \(h^0=k\).
- \(3^k+1\le2\lambda<3^{k+1}\). Then \(\delta\notin L\) and \(\lceil t\rceil=k+1\). Since \((3^k+1)/2\le\lfloor\lambda\rfloor\le(3^{k+1}-1)/2\), we get \(3^k+2\le2\lfloor\lambda\rfloor+1\le3^{k+1}\) and \(h^0=k+1\).

In each case (8.3) holds. \(\square\)

**Remark 8.10.** (1) The first level of \(H^0(D)\) has \(2\lfloor\lambda\rfloor+1\) elements, about \(2e^\delta=e^{\delta+\log2}\). The dimension is about the logarithm in base 3 of this number, as for a vector space over \(\mathbb F_3\). So (8.3) has the form of the Riemann–Roch formula \(h^0-h^1=\deg D+1\) of a curve of genus 0, with the degree measured in units of \(\log3\) and the constant \(\log2/\log3\) in place of 1. The correction \(\mathbf 1_L\) comes from the integer part: \(L\) is a union of intervals of lengths \(\log(1+3^{-k})\), of total length about \(1.141\).

(2) Let \(K=-2\{2\}\), a divisor of degree \(-2\log2\). The number \(t\) of the proof changes its sign when \(D\) is replaced by \(K-D\), so the first term on the right of (8.3) does too. This symmetry is explained by a duality between \(H^0(K-D)\) and \(H^1(D)\) [Connes–Consani 2023, Theorem 5.3]; see the last section.

## Exercises

**Exercise 1 (products and coproducts of Γ-sets).** (a) Let \(P\) and \(Q\) be pointed sets. Show that \(\operatorname{Hom}(P\wedge\mathbb S,Q\wedge\mathbb S)\) is the set of pointed maps \(P\to Q\), and that the automorphism group of \(n_+\wedge\mathbb S\) is the symmetric group on \(n\) letters. (b) Show that \(2_+\wedge\mathbb S=\mathbb S\vee\mathbb S\) is the coproduct of two copies of \(\mathbb S\) in \(\Gamma\mathrm{Set}\), and that it is not isomorphic to the product \(\mathbb S\times\mathbb S\).

*Solution.* (a) By Lemma 1.3 the morphisms \(P\wedge\mathbb S\to Q\wedge\mathbb S\) correspond to the pointed maps \(t:P\to(Q\wedge\mathbb S)(1_+)=Q\), and the morphism of \(t\) is \(p\wedge x\mapsto t(p)\wedge x\). So composition of morphisms is composition of maps, and the automorphisms of \(n_+\wedge\mathbb S\) are the pointed bijections of \(n_+\), that is, the permutations of \(\{1,\dots,n\}\). (b) By Lemma 1.3, \(\operatorname{Hom}(2_+\wedge\mathbb S,F)=F(1_+)\times F(1_+)=\operatorname{Hom}(\mathbb S,F)\times\operatorname{Hom}(\mathbb S,F)\), which is the universal property of the coproduct. The set \((\mathbb S\vee\mathbb S)(k_+)=k_+\vee k_+\) has \(2k+1\) elements and \((\mathbb S\times\mathbb S)(k_+)\) has \((k+1)^2\). These numbers differ for \(k\ge1\). So \(\Gamma\mathrm{Set}\) has a zero object, but finite coproducts and finite products differ, unlike in the category of abelian groups.

**Exercise 2 (\(H\mathbb B\) and \(H\mathbb F_2\)).** The sets \(H\mathbb B(X)\) and \(H\mathbb F_2(X)\) are both the set of subsets of \(X^\circ\). (a) Describe the components, the total and the product of subsets in both cases. (b) Show that the only morphisms of Γ-sets \(H\mathbb B\to H\mathbb F_2\) and \(H\mathbb F_2\to H\mathbb B\) are the zero morphisms. (c) Show that the unit morphisms embed \(\mathbb S\) in \(H\mathbb B\) and in \(H\mathbb F_2\), with the same image.

*Solution.* (a) In both cases the component of a subset \(T\) at \(x\) is 1 if \(x\in T\) and 0 otherwise, and the product of \(T\) and \(T'\) is \(T\times T'\subseteq(X\wedge Y)^\circ\), because the products of \(\mathbb B\) and \(\mathbb F_2\) agree. The total of \(T\) is 1 in \(H\mathbb B\) if \(T\) is not empty, and it is the parity of the number of elements of \(T\) in \(H\mathbb F_2\). (b) By Theorem 1.6 a morphism is \(H(u)\) for an additive map \(u\). If \(u:\mathbb B\to\mathbb F_2\), then \(u(1)=u(1+1)=u(1)+u(1)=0\). If \(u:\mathbb F_2\to\mathbb B\), then \(u(1)+u(1)=u(0)=0\), and \(a+a=a\) in \(\mathbb B\), so \(u(1)=0\). (c) By Lemma 3.3 the unit morphism sends \(x\in X^\circ\) to the subset \(\{x\}\). It is injective, and its image is the set of subsets with at most one element in both cases. On these subsets the maps \(H\mathbb B(f)\) and \(H\mathbb F_2(f)\) agree. So \(\mathbb B\) and \(\mathbb F_2\) are two ways to extend \(\mathbb S\) by a value for the sum \(1+1\).

**Exercise 3 (sum and maximum).** Let \(p\) be a prime, \(|\cdot|_p\) the \(p\)-adic absolute value of \(\mathbb Q\) and \(|\cdot|\) the usual one. (a) Show that the sets \(\{\varphi\in H\mathbb Q(X):\max_x|\varphi(x)|_p\le1\}\) form the sub-\(\mathbb S\)-algebra \(H(\mathbb Z_{(p)})\) of \(H\mathbb Q\). (b) Show that the sets \(\{\varphi:\max_x|\varphi(x)|\le1\}\) do not form a sub-Γ-set of \(H\mathbb Q\). (c) Show that \(|\cdot|_p\) is a seminorm in the sense of Section 6 and that its unit ball \(B\) is a sub-\(\mathbb S\)-algebra of \(H(\mathbb Z_{(p)})\) with the same first level. Compute \(1\oplus1\) in \(B\) and in \(H(\mathbb Z_{(p)})\).

*Solution.* (a) The condition says that all values of \(\varphi\) lie in the subring \(\mathbb Z_{(p)}\). (b) The element \((1,1)\) of \(H\mathbb Q(2_+)\) satisfies the condition, and its image under \(H\mathbb Q(\sigma)\) is 2, which does not. (c) \(|0|_p=0\), \(|1|_p=1\), \(|xy|_p=|x|_p|y|_p\) and \(|x+y|_p\le\max(|x|_p,|y|_p)\le|x|_p+|y|_p\). By Proposition 6.1, \(B\) is a sub-\(\mathbb S\)-algebra of \(H\mathbb Q\). If \(\sum_x|\varphi(x)|_p\le1\), then every \(|\varphi(x)|_p\le1\), so \(B\subseteq H(\mathbb Z_{(p)})\), and the first levels agree. A witness for the family \((1,1)\) in \(H\mathbb Q\) is the vector \((1,1)\) only, and \(|1|_p+|1|_p=2\). So \(1\oplus1=\emptyset\) in \(B\) and \(1\oplus1=\{2\}\) in \(H(\mathbb Z_{(p)})\). At a finite place the valuation ring is the ball for the maximum; at the archimedean place only the ball for the sum is a Γ-set.

**Exercise 4 (the multiplication of \(H\mathbb Z\)).** Let \(\bar\mu:H\mathbb Z\wedge H\mathbb Z\to H\mathbb Z\) be the morphism that corresponds to the product of \(H\mathbb Z\) by Proposition 2.2. Show that \(\bar\mu\) is surjective on every level and not injective on the second level.

*Solution.* For \(\varphi\in H\mathbb Z(X)\), \(\bar\mu(u(1\wedge\varphi))=1\cdot\varphi=\varphi\). So \(\bar\mu\) is surjective. The elements \(\xi\) and \(\eta\) of the proof of Theorem 4.7 are different, and \(\bar\mu(\xi)=1\cdot(1,1)=(1,1)=(1,1)\cdot1=\bar\mu(\eta)\).

**Exercise 5 (a spectrum at the archimedean place).** Let \(A=\|H(\mathbb Z[\tfrac12])\|_1\) for the usual absolute value, so \(M=A(1_+)\) is the set of \(q\in\mathbb Z[\tfrac12]\) with \(|q|\le1\). For \(b\in M\) let \(T(b)\) be the set of odd primes that divide \(b\). (a) Show that for \(0<|b|<1\), \(\operatorname{rad}(b)\) is the set of \(c\in M\) with \(|c|<1\) and \(T(b)\subseteq T(c)\), or \(c=0\). Deduce that \(C^\infty(A)\) consists of \(0^\infty\), \(1^\infty\) and one element \(u_T\) for every finite set \(T\) of odd primes, with \(u_T\le u_{T'}\) exactly when \(T\supseteq T'\). (b) Show that \(u_\emptyset\) covers \(1^\infty\). (c) Show that \((u_{\{3\}},u_{\{5\}})\) covers \(u_\emptyset\).

*Solution.* (a) \(c\in\operatorname{rad}(b)\) means that \(c^n/b\in\mathbb Z[\tfrac12]\) and \(|c|^n\le|b|\) for some \(n\ge1\). This fails if \(|c|=1\). Let \(0<|c|<1\). Then \(|c|^n\le|b|\) for large \(n\). Elements of \(\mathbb Z[\tfrac12]\) have \(\operatorname{ord}_p\ge0\) for odd \(p\), and \(c^n/b\in\mathbb Z[\tfrac12]\) says \(n\operatorname{ord}_p(c)\ge\operatorname{ord}_p(b)\) for all odd \(p\). For large \(n\) this holds exactly when \(\operatorname{ord}_p(c)\ge1\) for all \(p\in T(b)\). So \(\operatorname{rad}(b)\) depends only on \(T(b)\), and \(\operatorname{rad}(b)\subseteq\operatorname{rad}(b')\) exactly when \(T(b)\supseteq T(b')\). Every finite set \(T\) of odd primes occurs, for \(b=2^{-k}\prod_{p\in T}p\) with \(k\) large. Finally \(\operatorname{rad}(\pm1)=M\) and \(\operatorname{rad}(0)=\{0\}\). (b) The element \((\tfrac12,\tfrac12)\) of \(A(2_+)\) has total 1 and components of class \(u_\emptyset\). So \((u_\emptyset,u_\emptyset)\) is a partition of \(1^\infty\). (c) The element \((\tfrac3{16},\tfrac5{16})\) of \(A(2_+)\) has total \(\tfrac12\), of class \(u_\emptyset\), and components of classes \(u_{\{3\}}\) and \(u_{\{5\}}\). So \((u_{\{3\}},u_{\{5\}})\) is a partition of \(u_\emptyset\). Part (c) corresponds to the cover of \(\operatorname{Spec}\mathbb Z[\tfrac12]\) by \(D(3)\) and \(D(5)\). Part (b) says, as in Example 7.10, that sheaves do not see the point \(\infty\).

**Exercise 6 (Riemann–Roch in examples).** (a) Let \(D=2\{3\}-(\log2)\{\infty\}\). Compute \(\deg D\), the first level of \(H^0(D)\) and a generating set with \(h^0(D)\) elements, and check (8.3). (b) Check (8.3) for \(D=a\{\infty\}\) with \(e^a=4.7\) and with \(e^a=\tfrac1{10}\), and give a generating set of \(U(1)_{1/10}\) of minimal size.

*Solution.* (a) \(\deg D=2\log3-\log2=\log\tfrac92\), so \(\lambda=\tfrac92\). Here \(c_D=\tfrac19\) and \(e^a=\tfrac12\), so the first level of \(H^0(D)\) is the set of the numbers \(k/9\) with \(|k|\le4\), and \(H^0(D)\cong\|H\mathbb Z\|_4\). By Theorem 8.5, \(h^0(D)=\lceil\log_39\rceil=2\), and \(\{\tfrac19,\tfrac39\}\) is a generating set, from the chain \(1,3\). Also \(h^1(D)=0\). On the right of (8.3), \(2\lambda=9=3^2\), so \(\delta\notin L\) and the value is \(\lceil2\rceil'=2\). (b) For \(\lambda=4.7\): \(\lfloor\lambda\rfloor=4\), so \(h^0=2\) and \(h^1=0\). Here \(2\lambda=9.4\) lies between \(3^2\) and \(3^2+1\), so \(\delta\in L\), and the right side is \(\lceil\log_39.4\rceil-1=3-1=2\). For \(\lambda=\tfrac1{10}\): \(h^0=0\) and \(h^1=\lceil\log_35\rceil=2\). The right side is \(-\lceil\log_35\rceil=-2\). The set \(\{\tfrac13,\tfrac19\}\) is generating for \(U(1)_{1/10}\): its two elements are at distance \(\tfrac29>\tfrac1{10}\), and the nine sums \(k/9\), \(|k|\le4\), are spaced by \(\tfrac19\), so every point of the circle is at distance at most \(\tfrac1{18}\) from one of them.

## What this lesson does not prove

The following results are stated or used for orientation only.

1. *Homotopy theory.* Simplicial Γ-sets model connective spectra, and \(\mathbb S\) corresponds to the sphere spectrum [Segal 1974]. The lesson does not use this.
2. *The smash square of \(H\mathbb B\).* \((H\mathbb B\wedge H\mathbb B)(k_+)\) is described by matrices with entries in \(k_+\) [Connes–Consani 2016a, Theorem 4.9], and \((H\mathbb B\wedge H\mathbb B)(1_+)\) is infinite [Connes–Consani 2016a, Corollary 4.10].
3. *The assembly map.* For Γ-sets \(F\) and \(G\) there is a natural morphism from \(F\wedge G\) to the composite of \(G\) with the extension of \(F\) to all pointed sets; it is surjective for \(F=G=HR\) [Connes–Consani 2016a, Definition 7.1 and Proposition 7.2]. [Connes–Consani 2016a, Proposition 7.3] uses it to pass from monads to \(\mathbb S\)-algebras; Theorem 6.3 is proved here without it.
4. *Products of the sheaves \(\mathcal O(D)\).* For modules \(N\) and \(N'\) over an \(\mathbb S\)-algebra \(A\), the smash product \(N\wedge_AN'\) is the coequalizer of the two morphisms \(N\wedge A\wedge N'\to N\wedge N'\) given by the actions. [Connes–Consani 2016a, Proposition 6.4] states that \(\mathcal O(D)\wedge_{\mathcal O}\mathcal O(D')\cong\mathcal O(D+D')\), except when \(e^a\) and \(e^{a'}\) are irrational and their product is rational; in that case the left side is \(\mathcal O_\epsilon\wedge_{\mathcal O}\mathcal O(D+D')\), where \(\mathcal O_\epsilon\subseteq\mathcal O\) is defined by the strict inequality \(\sum|\varphi(x)|<1\) at \(\infty\).
5. *The spectrum.* A morphism of \(\mathbb S\)-algebras induces a geometric morphism between the toposes of sheaves on the spectra [Connes–Consani 2021, Theorem 5.11]. The sheaf associated with a presheaf of \(\mathbb S\)-algebras is a sheaf of \(\mathbb S\)-algebras, and the structure sheaf is functorial [Connes–Consani 2021, Lemma 7.7 and Theorem 7.10]. The points of the topos of sheaves on \(\mathfrak{Spec}(HR)\), for a semiring \(R\), are the prime ideals of \(R\) [Connes–Consani 2021, Proposition 6.5]. The structure presheaf of a quotient \(HR/G\) need not be a sheaf; it is one when the ring \(R\) has no zero divisors [Connes–Consani 2021, Remark 7.13 and Proposition 7.14]. For the semiring of continuous convex piecewise affine functions with integral slopes and finitely many pieces on a bounded open interval, together with the constant \(-\infty\) as zero, with the operations maximum and sum, the points of the spectrum are the convex subsets of the interval [Connes–Consani 2021, Proposition 6.4]. The schemes relative to the category of Γ-sets in the sense of [Toën–Vaquié 2009] do not give back the schemes over rings: for a field \(K\ne\mathbb F_2\), the two projections \(H(K\times K)\to HK\) are not a Zariski cover in that sense [Connes–Consani 2021, Lemma 8.1]; see *Schemes relative to a symmetric monoidal category*.
6. *The cohomology of a divisor.* In [Connes–Consani 2023, Appendix B] the modules \(H^0(D)\) and \(H^1(D)\) of Definition 8.7 are obtained from a Γ-space attached to \(\psi_D\) by the Dold–Kan correspondence, as its homotopy in degrees 1 and 0; the homotopy relation of this Γ-space is not transitive, which is the origin of the tolerance relation. Serre duality [Connes–Consani 2023, Theorem 5.3]: for \(K=-2\{2\}\) and every Arakelov divisor \(D\) there is an isomorphism of \(\mathbb S[\pm1]\)-modules between \(H^0(K-D)\) and the inner Hom from \(H^1(D)\) to \(U(1)_{1/4}\), formed as in Proposition 2.5 with the morphisms that preserve the tolerance relations.
7. *Generalized rings.* The tensor square of \(\mathbb Z\) over the initial generalized ring [Durov 2007, 5.1.22] and the construction of the compactification of \(\operatorname{Spec}\mathbb Z\) by generalized schemes [Durov 2007, 7.1] are treated in *Generalized rings*.

## References

The numbers of results in the works of Connes and Consani and of Durov are those of the arXiv versions.

- [Connes–Consani 2016a] A. Connes and C. Consani, *Absolute algebra and Segal's Γ-rings*, [arXiv:1502.05585](https://arxiv.org/abs/1502.05585). Free at https://alainconnes.org/wp-content/uploads/Segalgammarings.pdf
- [Connes–Consani 2021] A. Connes and C. Consani, *On absolute algebraic geometry: the affine case*, [arXiv:1909.09796](https://arxiv.org/abs/1909.09796). Free at https://alainconnes.org/wp-content/uploads/JAG2020-1.pdf
- [Connes–Consani 2023] A. Connes and C. Consani, *Riemann–Roch for \(\overline{\operatorname{Spec}\mathbb Z}\)*, [arXiv:2205.01391](https://arxiv.org/abs/2205.01391).
- [Connes–Consani 2010] A. Connes and C. Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024](https://arxiv.org/abs/0903.2024). Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Durov 2007] N. Durov, *New approach to Arakelov geometry*, [arXiv:0704.2030](https://arxiv.org/abs/0704.2030).
- [Toën–Vaquié 2009] B. Toën and M. Vaquié, *Au-dessous de \(\operatorname{Spec}\mathbb Z\)*, [arXiv:math/0509684](https://arxiv.org/abs/math/0509684).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 009O and 00E0 carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Segal 1974] G. Segal, Categories and cohomology theories, *Topology* 13 (1974), 293–312. Free at https://linkinghub.elsevier.com/retrieve/pii/0040938374900226
