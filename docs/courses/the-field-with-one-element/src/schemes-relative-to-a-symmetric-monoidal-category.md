# Schemes relative to a symmetric monoidal category

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. Public domain (CC0).*

## Introduction

A commutative ring is a commutative monoid in the category of abelian groups with its tensor product. The functor of
points of a scheme can be described in these terms alone. Affine schemes form the opposite of the category of rings.
An open immersion of affine schemes is a ring homomorphism that is flat, an epimorphism and of finite presentation.
A scheme is a sheaf for the Zariski topology that is covered by open affine subfunctors. [Toën–Vaquié 2009] turn this
description into a definition. For a symmetric monoidal category \(\mathcal C\) with enough limits and colimits they
construct a category \(\mathrm{Sch}(\mathcal C)\) of *schemes relative to \(\mathcal C\)*.

This lesson develops the construction with proofs and then computes it in three cases.

- For abelian groups, \(\mathrm{Sch}(\mathcal C)\) is the category of ordinary schemes (Theorem 5.3).
- For sets with the cartesian product, the commutative monoids of \(\mathcal C\) are the commutative monoids in
  which no zero is required. The relative schemes are the \(\mathbb F_1\)-schemes of
  [Toën–Vaquié 2009, Définition 3.5]. Their category is equivalent to the category of schemes over \(\mathbb F_1\)
  of [Deitmar 2005]. This is the theorem of [Vezzani 2012] (Theorem 6.10).
- For pointed sets with the smash product, the commutative monoids are the monoids with zero of this course, and
  the relative schemes are the monoid schemes of the lesson *Monoid schemes* (Theorem 6.12).

The relative point of view adds three things to the lesson *Monoid schemes*. First, a monoid scheme is determined by
its functor of points on monoids, and the functors that arise in this way are characterized. Second, base change to
the integers is a formal operation on functors (Section 7). Third, a group functor such as the general linear group
is defined over \(\mathbb F_1\) by the same formula as over a ring (Section 8). Its group of
\(\mathbb F_1\)-points is the symmetric group, which is what the lesson *Counting over finite fields and the limit
q → 1* asks for. Its base change to the integers is the group of monomial matrices and not the general linear group.

**What is assumed.** From category theory: symmetric monoidal categories, limits and colimits, adjoint functors, and
sheaves of sets on a site given by a pretopology. From this course: *Commutative monoids and their spectra* and
*Monoid schemes*; the facts used from them are restated in Section 6. Schemes are used in Sections 5, 7 and 8, and
the facts about them that are not proved here are quoted from [Stacks] with their tags.

Basic references are [Toën–Vaquié 2009], [Vezzani 2012], [Deitmar 2005] and [Stacks].

**Conventions.** Rings are commutative with \(1\), and \(\mathbb N=\{0,1,2,\dots\}\). A *directed set* is a
non-empty preordered set in which any two elements have an upper bound [Stacks, Tag [00D3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-directed-set)]; a *directed system* is a
functor from a directed set, and a *directed colimit* is the colimit of a directed system. The category
\(\mathrm{Comm}(\mathcal C)\) of Section 1 is not small. As in [Toën–Vaquié 2009], we do not discuss the choice of a
universe in which the presheaves on its opposite category are formed.

## 1. Monoids and modules in a symmetric monoidal category

Throughout, \((\mathcal C,\otimes,\mathbf 1)\) is a symmetric monoidal category [Stacks, Tag [0FFW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-symmetric-monoidal-category)]. The symmetry is
written \(\sigma_{X,Y}\colon X\otimes Y\to Y\otimes X\). By Mac Lane's coherence theorem [Stacks, Tag [0HB0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-symmetric-monoidal-coherence)] we write
iterated tensor products without brackets and identify \(\mathbf 1\otimes X\) with \(X\).

**Hypothesis 1.1.**

(a) \(\mathcal C\) has finite limits and small colimits.

(b) For every object \(X\) the functor \(X\otimes-\colon\mathcal C\to\mathcal C\) preserves small colimits.

By symmetry the functors \(-\otimes X\) preserve colimits too. Condition (b) holds if the monoidal structure is
*closed*, that is, if every functor \(X\otimes-\) has a right adjoint. [Toën–Vaquié 2009, Hypothèse 2.6] assumes that
\(\mathcal C\) has all limits and all colimits and is closed. Every statement of this lesson uses Hypothesis 1.1 only.

**Example 1.2.** The following four categories satisfy Hypothesis 1.1. Each of them is complete, cocomplete and
closed.

1. \(\mathrm{Ab}\): abelian groups with the tensor product over \(\mathbb Z\). The unit is \(\mathbb Z\).
2. \(\mathrm{Set}\): sets with the cartesian product. The unit is a set with one element.
3. \(\mathrm{Set}_{\ast}\): pointed sets \((X,\ast)\) with the smash product \(X\wedge Y\), the quotient of
   \(X\times Y\) in which all pairs \((x,\ast)\) and \((\ast,y)\) are identified with the base point. The unit is
   \(S^0=\{\ast,1\}\).
4. \(\mathrm{CMon}\): commutative monoids written additively, with the tensor product that represents biadditive
   maps. The unit is \(\mathbb N\).

**Definition 1.3.** A *commutative monoid in \(\mathcal C\)* is an object \(A\) with morphisms
\(\mu\colon A\otimes A\to A\) and \(\eta\colon\mathbf 1\to A\) such that
\[
\mu(\mu\otimes A)=\mu(A\otimes\mu),\qquad\mu(\eta\otimes A)=\mathrm{id}_A,\qquad\mu\,\sigma_{A,A}=\mu .
\]
A *morphism* of commutative monoids is a morphism \(f\colon A\to B\) of \(\mathcal C\) with
\(f\mu_A=\mu_B(f\otimes f)\) and \(f\eta_A=\eta_B\). The category of commutative monoids in \(\mathcal C\) is written
\(\mathrm{Comm}(\mathcal C)\).

An *\(A\)-module* is an object \(M\) with a morphism \(\rho\colon A\otimes M\to M\) such that
\(\rho(\mu\otimes M)=\rho(A\otimes\rho)\) and \(\rho(\eta\otimes M)=\mathrm{id}_M\). A morphism of \(\mathcal C\)
between \(A\)-modules is *\(A\)-linear* if it commutes with the actions. The category of \(A\)-modules and
\(A\)-linear morphisms is written \(\mathrm{Mod}_A\).

An *\(A\)-algebra* is a commutative monoid \(B\) with a morphism \(A\to B\) of \(\mathrm{Comm}(\mathcal C)\). A
morphism of \(A\)-algebras is a morphism of commutative monoids that is compatible with the morphisms from \(A\).
The category of \(A\)-algebras is written \(\mathrm{Alg}_A\).

The *category of affine schemes relative to \(\mathcal C\)* is
\(\mathrm{Aff}_{\mathcal C}=\mathrm{Comm}(\mathcal C)^{\mathrm{op}}\). The object of \(\mathrm{Aff}_{\mathcal C}\)
that corresponds to \(A\) is written \(\operatorname{Spec}A\).

The unit object \(\mathbf 1\) is a commutative monoid, with \(\mu\) the identification
\(\mathbf 1\otimes\mathbf 1=\mathbf 1\) and \(\eta=\mathrm{id}\). For a commutative monoid \(A\), the unit \(\eta_A\)
is a morphism of commutative monoids \(\mathbf 1\to A\), and it is the only one, because such a morphism must carry
the unit of \(\mathbf 1\) to the unit of \(A\). So \(\mathbf 1\) is an initial object of \(\mathrm{Comm}(\mathcal C)\)
and \(\operatorname{Spec}\mathbf 1\) is a terminal object of \(\mathrm{Aff}_{\mathcal C}\).

**Example 1.4.** We describe the commutative monoids and their modules in the four categories of Example 1.2.

1. In \(\mathrm{Ab}\) a commutative monoid is a commutative ring, and modules and algebras have their usual meaning.
2. In \(\mathrm{Set}\) a commutative monoid is a commutative monoid in the ordinary sense. This course reserves the
   word "monoid" for monoids with zero. So we call the objects of \(\mathrm{Mon}:=\mathrm{Comm}(\mathrm{Set})\)
   *plain monoids*. A plain monoid need not have an absorbing element, and a morphism of plain monoids is a map that
   preserves products and \(1\). These are the monoids of [Deitmar 2005]. The initial object is the trivial monoid
   \(\{1\}\). A module over a plain monoid \(M\) is an *\(M\)-set*: a set \(T\) with a map \(M\times T\to T\) such
   that \(1t=t\) and \((mm')t=m(m't)\).
3. In \(\mathrm{Set}_{\ast}\) a commutative monoid is a pointed set \((A,0)\) with a commutative and associative
   product that has a unit \(1\) and satisfies \(a\cdot0=0\); the base point is absorbing because \(\mu\) is defined
   on \(A\wedge A\). A morphism preserves products, \(1\) and \(0\). So
   \(\mathrm{Mon}_0:=\mathrm{Comm}(\mathrm{Set}_{\ast})\) is the category of monoids of this course. It contains the
   zero monoid \(0=\{0\}\), in which \(0=1\). The initial object is \(\mathbb F_1=\{0,1\}\). A module over a monoid
   \(M\) is a *pointed \(M\)-set*: an \(M\)-set \(T\) with a base point \(\ast\) such that \(m\ast=\ast\) and
   \(0t=\ast\) for all \(m\in M\), \(t\in T\).
4. In \(\mathrm{CMon}\) a commutative monoid is a commutative semiring, and a module is a semimodule.

In the two cases \(\mathrm{Set}\) and \(\mathrm{Set}_{\ast}\) we write \(\mathbb F_1\) for the initial commutative
monoid \(\mathbf 1\): it is \(\{1\}\) among plain monoids and \(\{0,1\}\) among monoids.

**Elements.** We describe morphisms between tensor products by their effect on elements, as in
\(\mu(a\otimes b)=ab\) and \(\rho(a\otimes m)=am\). In the four examples the formulas can be read literally. In
general a formula is shorthand for a morphism of \(\mathcal C\) built from structure morphisms and symmetries, and an
identity between formulas is shorthand for a commutative diagram. Every variable occurs exactly once on each side of
such an identity, so the translation is mechanical.

**Proposition 1.5 (modules).** Let \(A\) be a commutative monoid in \(\mathcal C\) and let
\(U\colon\mathrm{Mod}_A\to\mathcal C\) be the forgetful functor.

(a) \(\mathrm{Mod}_A\) has finite limits and small colimits, and \(U\) preserves them.

(b) \(U\) is conservative: an \(A\)-linear morphism that is an isomorphism in \(\mathcal C\) is an isomorphism of
\(A\)-modules. Hence \(U\) reflects finite limits and small colimits: a cone or cocone in \(\mathrm{Mod}_A\) is
limiting if its image in \(\mathcal C\) is.

(c) The functor \(X\mapsto A\otimes X\), with the action \(\mu\otimes X\), is left adjoint to \(U\).

*Proof.* (a) Let \((M_i)\) be a finite diagram of \(A\)-modules, with limit \(L\) in \(\mathcal C\) and projections
\(p_i\colon L\to M_i\). The morphisms \(\rho_i(A\otimes p_i)\colon A\otimes L\to M_i\) form a cone. So there is
exactly one morphism \(\rho\colon A\otimes L\to L\) with \(p_i\rho=\rho_i(A\otimes p_i)\) for all \(i\). The two
module axioms hold for \(\rho\), because they hold after composition with every \(p_i\). The \(p_i\) are
\(A\)-linear. A cone of \(A\)-linear morphisms \(N\to M_i\) induces one morphism \(N\to L\) of \(\mathcal C\), and
this morphism is \(A\)-linear, because linearity can be tested after composition with the \(p_i\). So \((L,\rho)\) is
a limit in \(\mathrm{Mod}_A\). Now let \((M_i)\) be a small diagram of \(A\)-modules, with colimit \(K\) in
\(\mathcal C\) and injections \(q_i\colon M_i\to K\). By Hypothesis 1.1(b), \(A\otimes K\) is the colimit of the
objects \(A\otimes M_i\), and \(A\otimes A\otimes K\) is the colimit of the objects \(A\otimes A\otimes M_i\). So
there is exactly one morphism \(\rho\colon A\otimes K\to K\) with \(\rho(A\otimes q_i)=q_i\rho_i\) for all \(i\).
The module axioms hold, because they hold after composition with the morphisms \(A\otimes A\otimes q_i\) and
\(q_i\). In the same way \((K,\rho)\) is a colimit in \(\mathrm{Mod}_A\).

(b) Let \(u\colon M\to N\) be \(A\)-linear with inverse \(v\) in \(\mathcal C\). Then
\(v\rho_N=v\rho_N(A\otimes u)(A\otimes v)=vu\rho_M(A\otimes v)=\rho_M(A\otimes v)\). So \(v\) is \(A\)-linear. Now
let a cone in \(\mathrm{Mod}_A\) have a limiting image in \(\mathcal C\). Compare it with the limit built in (a). The
comparison morphism is \(A\)-linear and is an isomorphism in \(\mathcal C\), so it is an isomorphism of
\(A\)-modules, and the cone is limiting. The same argument works for cocones.

(c) Let \(N\) be an \(A\)-module and \(\psi\colon X\to N\) a morphism of \(\mathcal C\). The morphism
\(a\otimes x\mapsto a\psi(x)\) from \(A\otimes X\) to \(N\) is \(A\)-linear, and its composite with
\(\eta\otimes X\colon X\to A\otimes X\) is \(\psi\). It is the only \(A\)-linear morphism with this property, because
an \(A\)-linear \(\varphi\) satisfies \(\varphi(a\otimes x)=a\varphi(1\otimes x)\). \(\square\)

**Definition 1.6.** Let \(f\colon A\to B\) be a morphism of \(\mathrm{Comm}(\mathcal C)\).

*Restriction of scalars* is the functor \(f_{\ast}\colon\mathrm{Mod}_B\to\mathrm{Mod}_A\) that keeps the underlying
object and lets \(a\) act as \(f(a)\).

*Base change.* For an \(A\)-module \(M\) let \(B\otimes_AM\) be the coequalizer in \(\mathcal C\) of the two
morphisms
\[
B\otimes A\otimes M\rightrightarrows B\otimes M,\qquad b\otimes a\otimes m\mapsto bf(a)\otimes m,\qquad
b\otimes a\otimes m\mapsto b\otimes am .
\]
We write \(b\otimes m\) also for the elements of \(B\otimes_AM\). By Hypothesis 1.1(b), \(B\otimes(B\otimes_AM)\) is
the coequalizer of the corresponding two morphisms
\(B\otimes B\otimes A\otimes M\rightrightarrows B\otimes B\otimes M\). So the rule
\(b'(b\otimes m)=b'b\otimes m\) defines an action of \(B\) on \(B\otimes_AM\). This \(B\)-module is written
\(f^{\ast}M\), and \(f^{\ast}\colon\mathrm{Mod}_A\to\mathrm{Mod}_B\) is the base change functor.

**Proposition 1.7 (base change).** Let \(f\colon A\to B\) and \(g\colon B\to B'\) be morphisms of
\(\mathrm{Comm}(\mathcal C)\).

(a) \(f_{\ast}\) preserves finite limits and small colimits, and it is conservative.

(b) \(f^{\ast}\) is left adjoint to \(f_{\ast}\). The bijection
\(\mathrm{Hom}_B(B\otimes_AM,N)\to\mathrm{Hom}_A(M,f_{\ast}N)\) sends \(\varphi\) to \(m\mapsto\varphi(1\otimes m)\).

(c) There are natural isomorphisms \((gf)^{\ast}\cong g^{\ast}f^{\ast}\), given by
\(b'\otimes(b\otimes m)\mapsto b'g(b)\otimes m\), and \((\mathrm{id}_A)^{\ast}\cong\mathrm{id}\).

(d) \(f^{\ast}(A\otimes X)\cong B\otimes X\), naturally in the object \(X\) of \(\mathcal C\). In particular
\(f^{\ast}\) carries the free module \(A^{\oplus n}\), the coproduct of \(n\) copies of \(A\), to \(B^{\oplus n}\).

*Proof.* (a) The forgetful functors satisfy \(U_Af_{\ast}=U_B\). By Proposition 1.5, \(U_B\) preserves finite limits
and small colimits and \(U_A\) reflects them; so \(f_{\ast}\) preserves them. If \(f_{\ast}(u)\) is an isomorphism,
then \(U_B(u)=U_Af_{\ast}(u)\) is one, and \(u\) is an isomorphism by Proposition 1.5(b).

(b) Let \(\psi\colon M\to f_{\ast}N\) be \(A\)-linear. The morphism \(B\otimes M\to N\),
\(b\otimes m\mapsto b\psi(m)\), sends \(bf(a)\otimes m\) and \(b\otimes am\) to the same element
\(bf(a)\psi(m)\). So it induces a morphism \(\varphi\colon B\otimes_AM\to N\), which is \(B\)-linear. Conversely,
if \(\varphi\) is \(B\)-linear, then \(\psi(m)=\varphi(1\otimes m)\) satisfies
\(\psi(am)=\varphi(1\otimes am)=\varphi(f(a)\otimes m)=f(a)\psi(m)\). The two constructions are inverse to each
other, because \(\varphi(b\otimes m)=b\varphi(1\otimes m)\).

(c) and (d) We have \((gf)_{\ast}=f_{\ast}g_{\ast}\), \((\mathrm{id}_A)_{\ast}=\mathrm{id}\) and
\(U_Af_{\ast}=U_B\). Left adjoints are unique up to a unique isomorphism, and the left adjoint of a composite is the
composite of the left adjoints. With (b) and Proposition 1.5(c) this gives (c) and (d). Finally
\(A^{\oplus n}=A\otimes(\mathbf 1\sqcup\dots\sqcup\mathbf 1)\) by Hypothesis 1.1(b). \(\square\)

**Proposition 1.8 (algebras).**

(a) \(\mathrm{Comm}(\mathcal C)\) has finite limits and directed colimits, and the forgetful functor
\(\mathrm{Comm}(\mathcal C)\to\mathcal C\) preserves and reflects them. A directed system of \(A\)-algebras has a
colimit in \(\mathrm{Alg}_A\), with the same underlying object.

(b) Let \(f\colon A\to B\) and \(f'\colon A\to B'\) be \(A\)-algebras. The object \(B\otimes_AB'\) has exactly one
structure of commutative monoid with \((b\otimes b')(c\otimes c')=bc\otimes b'c'\) and unit \(1\otimes1\). With the
morphisms \(b\mapsto b\otimes1\) and \(b'\mapsto1\otimes b'\) it is the pushout of \(B\leftarrow A\to B'\) in
\(\mathrm{Comm}(\mathcal C)\).

(c) (Base change formula.) Let \(f\colon A\to B\) and \(g\colon A\to A'\) be morphisms, put \(B'=A'\otimes_AB\), and
let \(f'\colon A'\to B'\) and \(g'\colon B\to B'\) be the two morphisms of (b). For every \(B\)-module \(N\) the rule
\(a'\otimes n\mapsto(a'\otimes1)\otimes n\) defines an isomorphism of \(A'\)-modules
\[
A'\otimes_Af_{\ast}N\longrightarrow f'_{\ast}(B'\otimes_BN),
\]
natural in \(N\). In short, \(g^{\ast}f_{\ast}\cong f'_{\ast}g'^{\ast}\).

*Proof.* (a) For a finite diagram \((B_i)\) in \(\mathrm{Comm}(\mathcal C)\) with limit \(L\) in \(\mathcal C\) and
projections \(p_i\), the cones \(\mu_i(p_i\otimes p_i)\) and \(\eta_i\) induce \(\mu\colon L\otimes L\to L\) and
\(\eta\colon\mathbf 1\to L\). As in Proposition 1.5(a), the axioms hold and \((L,\mu,\eta)\) is the limit. Let
\((B_\alpha)\) be a directed system in \(\mathrm{Comm}(\mathcal C)\) with colimit \(B\) in \(\mathcal C\). By
Hypothesis 1.1(b), used in each variable, \(B\otimes B\) is the colimit of the objects \(B_\alpha\otimes B_\beta\)
over all pairs \((\alpha,\beta)\). Since the index set is directed, the pairs \((\alpha,\alpha)\) are cofinal, so
\(B\otimes B\) is the colimit of the objects \(B_\alpha\otimes B_\alpha\). Hence the \(\mu_\alpha\) induce
\(\mu\colon B\otimes B\to B\). The unit is the composite \(\mathbf 1\to B_\alpha\to B\), for any \(\alpha\). The
axioms are checked on \(B\otimes B\otimes B\), which is the colimit of the objects
\(B_\alpha\otimes B_\alpha\otimes B_\alpha\), and \((B,\mu,\eta)\) is the colimit in \(\mathrm{Comm}(\mathcal C)\).
The forgetful functor is conservative, by the computation of Proposition 1.5(b) applied to \(\mu\) and \(\eta\); so
it reflects these limits and colimits, as in Proposition 1.5(b). For a directed system of \(A\)-algebras the colimit
receives a morphism from \(A\) and is the colimit in \(\mathrm{Alg}_A\).

(b) Let \(q\colon B\otimes B'\to B\otimes_AB'\) be the coequalizer of Definition 1.6. The object \(B\otimes B'\) is
a commutative monoid with \((b\otimes b')(c\otimes c')=bc\otimes b'c'\). By Hypothesis 1.1(b), \(q\otimes q\) is the
composite of the two coequalizers \(q\otimes\mathrm{id}\) and \(\mathrm{id}\otimes q\). So it is an epimorphism, and
a morphism out of \((B\otimes B')\otimes(B\otimes B')\) factors through \(q\otimes q\) if it coequalizes the pairs of
morphisms that define these two coequalizers. The morphism
\((b\otimes b')\otimes(c\otimes c')\mapsto q(bc\otimes b'c')\) has this property: replacing \(c\otimes c'\) by
\(cf(a)\otimes c'\) or by \(c\otimes f'(a)c'\) gives \(q(bcf(a)\otimes b'c')\) and
\(q(bc\otimes b'f'(a)c')\), and these agree by the definition of \(q\) and the commutativity of \(B'\); the first
variable is treated in the same way. So the product descends to \(B\otimes_AB'\). Associativity, commutativity and
the unit law descend too, because \(q\otimes q\otimes q\) is an epimorphism. The product is unique, because
\(q\otimes q\) is an epimorphism. The two morphisms \(b\mapsto b\otimes1\) and \(b'\mapsto1\otimes b'\) are
morphisms of commutative monoids, and they agree on \(A\), because \(f(a)\otimes1=1\otimes f'(a)\) in
\(B\otimes_AB'\).

Let \(u\colon B\to E\) and \(u'\colon B'\to E\) be morphisms of commutative monoids with \(uf=u'f'\). The morphism
\(b\otimes b'\mapsto u(b)u'(b')\) coequalizes the two morphisms of Definition 1.6, since
\(u(bf(a))u'(b')=u(b)u'(f'(a)b')\). So it induces \(w\colon B\otimes_AB'\to E\). It preserves products because \(E\)
is commutative: \(u(b)u'(b')u(c)u'(c')=u(bc)u'(b'c')\). It restricts to \(u\) and \(u'\). It is the only such
morphism, because \(b\otimes b'=(b\otimes1)(1\otimes b')\).

(c) The rule \(a'\otimes n\mapsto(a'\otimes1)\otimes n\) is compatible with the relation that defines
\(A'\otimes_Af_{\ast}N\):
\[
(a'g(a)\otimes1)\otimes n=(a'\otimes f(a))\otimes n=(a'\otimes1)\otimes f(a)n .
\]
The first equality holds in \(B'=A'\otimes_AB\), and the second in \(B'\otimes_BN\), where \(B\) acts on \(B'\)
through \(g'\). So the rule defines an \(A'\)-linear morphism \(\alpha\). In the other direction, by
Hypothesis 1.1(b) the object \(B'\otimes N\) is the coequalizer of two morphisms
\(A'\otimes A\otimes B\otimes N\rightrightarrows A'\otimes B\otimes N\). The rule
\(a'\otimes b\otimes n\mapsto a'\otimes bn\), with values in \(A'\otimes_Af_{\ast}N\), coequalizes them, because
\(a'g(a)\otimes bn=a'\otimes f(a)bn\) there. The resulting morphism \(B'\otimes N\to A'\otimes_Af_{\ast}N\) sends
\((a'\otimes b)g'(c)\otimes n\) and \((a'\otimes b)\otimes cn\) to the same element \(a'\otimes bcn\). So it
induces \(\beta\colon B'\otimes_BN\to A'\otimes_Af_{\ast}N\). We have \(\beta\alpha(a'\otimes n)=a'\otimes n\) and
\[
\alpha\beta((a'\otimes b)\otimes n)=(a'\otimes1)\otimes bn=(a'\otimes1)g'(b)\otimes n=(a'\otimes b)\otimes n .
\]
So \(\alpha\) and \(\beta\) are inverse isomorphisms. They are natural in \(N\). \(\square\)

For a morphism \(f\colon A\to B\) and an \(A\)-algebra \(D\), part (b) shows that \(B\otimes_AD\) is a
\(B\)-algebra. We use the pushout square of (c) in both directions: it is symmetric in \(B\) and \(A'\).

**Proposition 1.9 (epimorphisms).** For a morphism \(f\colon A\to B\) of \(\mathrm{Comm}(\mathcal C)\) the following
are equivalent.

(i) \(f\) is an epimorphism of \(\mathrm{Comm}(\mathcal C)\).

(ii) The two morphisms \(i_1,i_2\colon B\to B\otimes_AB\), \(b\mapsto b\otimes1\) and \(b\mapsto1\otimes b\), are
equal.

(iii) The multiplication \(m\colon B\otimes_AB\to B\), \(b\otimes c\mapsto bc\), is an isomorphism.

If they hold, then for every \(B\)-module \(N\) the counit \(B\otimes_Af_{\ast}N\to N\), \(b\otimes n\mapsto bn\), is
an isomorphism, and \(f_{\ast}\) is fully faithful.

*Proof.* By Proposition 1.8(b), \(B\otimes_AB\) with \(i_1,i_2\) is the pushout of \(B\leftarrow A\to B\). In
particular \(i_1f=i_2f\), so (i) implies (ii). Conversely assume (ii) and let \(u,v\colon B\to E\) be morphisms with
\(uf=vf\). The pushout property gives \(w\) with \(wi_1=u\) and \(wi_2=v\), so \(u=v\); this is (i). The morphism
\(m\) is the one induced by the pair \((\mathrm{id}_B,\mathrm{id}_B)\), so \(mi_1=mi_2=\mathrm{id}_B\). If
\(i_1=i_2\), then \(i_1mi_1=i_1\) and \(i_1mi_2=i_1=i_2\), so \(i_1m=\mathrm{id}\) by the uniqueness in the pushout
property; hence (ii) implies (iii). If \(m\) is an isomorphism, \(mi_1=mi_2\) gives \(i_1=i_2\).

Assume (i)–(iii) and let \(N\) be a \(B\)-module. Proposition 1.8(c), with \(A'=B\) and \(g=f\), gives an
isomorphism \(B\otimes_Af_{\ast}N\to(B\otimes_AB)\otimes_BN\), \(b\otimes n\mapsto(b\otimes1)\otimes n\). Here \(B\)
acts on \(B\otimes_AB\) through \(i_2\), and \(m\) is an isomorphism of \(B\)-algebras for this structure, since
\(mi_2=\mathrm{id}\). So \((B\otimes_AB)\otimes_BN\cong B\otimes_BN=N\) by \((b\otimes c)\otimes n\mapsto bcn\). The
composite is \(b\otimes n\mapsto bn\), the counit. A right adjoint is fully faithful if and only if the counit is an
isomorphism [Stacks, Tag [07RB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-adjoint-fully-faithful)]. \(\square\)

## 2. Flat morphisms and descent

**Definition 2.1.** A morphism \(f\colon A\to B\) of \(\mathrm{Comm}(\mathcal C)\) is *flat* if the functor
\(f^{\ast}=B\otimes_A-\) preserves finite limits.

A family \((f_i\colon A\to A_i)_{i\in I}\) is a *flat cover* if every \(f_i\) is flat and there is a finite subset
\(J\subseteq I\) such that the functors \(f_j^{\ast}\), \(j\in J\), are *jointly conservative*: a morphism \(u\) of
\(A\)-modules is an isomorphism as soon as \(f_j^{\ast}(u)\) is an isomorphism for every \(j\in J\). We also say
that the family \((\operatorname{Spec}A_i\to\operatorname{Spec}A)_{i\in I}\) is a flat cover of
\(\operatorname{Spec}A\).

[Toën–Vaquié 2009, Définition 2.10] calls these families fpqc covers. The functor \(f^{\ast}\) preserves all
colimits, because it is a left adjoint.

**Example 2.2.**

(a) In \(\mathrm{Ab}\), a ring homomorphism \(A\to B\) is flat in the sense of Definition 2.1 if and only if \(B\) is
a flat \(A\)-module. Indeed \(B\otimes_A-\) is additive and right exact, so it preserves finite limits if and only
if it preserves kernels, that is, if and only if it is exact.

(b) In \(\mathrm{Set}\) the terminal object of \(\mathrm{Mod}_A\) is a set with one element, and a flat morphism
must preserve it. This makes flatness a strong condition; see Example 6.7.

(c) The subset \(J\) may be empty. The empty family is a flat cover of \(\operatorname{Spec}A\) if and only if every
morphism of \(A\)-modules is an isomorphism. In \(\mathrm{Ab}\) this happens exactly for \(A=0\). In
\(\mathrm{Set}\) it never happens: the map from the empty \(A\)-set to a one-point \(A\)-set is not bijective. In
\(\mathrm{Set}_{\ast}\) it happens exactly for the zero monoid (Proposition 6.11).

**Lemma 2.3.**

(a) Isomorphisms are flat, and a composite of flat morphisms is flat.

(b) If \(f\colon A\to B\) is flat and \(g\colon A\to A'\) is a morphism, then \(A'\to A'\otimes_AB\) is flat.

(c) Let \(\varphi=\psi\lambda\) in \(\mathrm{Comm}(\mathcal C)\). If \(\lambda\) is an epimorphism and \(\varphi\)
is flat, then \(\psi\) is flat.

(d) An isomorphism is a flat cover. If \((A\to A_i)_{i\in I}\) is a flat cover and \(A\to A'\) is a morphism, then
\((A'\to A'\otimes_AA_i)_{i\in I}\) is a flat cover. If \((A\to A_i)_{i\in I}\) is a flat cover and
\((A_i\to A_{ik})_{k\in K_i}\) is a flat cover for every \(i\), then \((A\to A_{ik})_{i,k}\) is a flat cover.

*Proof.* (a) follows from Proposition 1.7(c).

(b) Let \(f'\colon A'\to B'=A'\otimes_AB\) and \(g'\colon B\to B'\) be as in Proposition 1.8(c). That proposition,
with the roles of \(B\) and \(A'\) exchanged, gives \(g'_{\ast}f'^{\ast}\cong f^{\ast}g_{\ast}\). Let \((N_\alpha)\)
be a finite diagram of \(A'\)-modules and let \(c\colon f'^{\ast}(\lim N_\alpha)\to\lim f'^{\ast}N_\alpha\) be the
comparison morphism. The functor \(g'_{\ast}\) preserves finite limits. So \(g'_{\ast}(c)\) is the comparison
morphism of the functor \(g'_{\ast}f'^{\ast}\cong f^{\ast}g_{\ast}\). This functor preserves finite limits, because
\(g_{\ast}\) and \(f^{\ast}\) do. So \(g'_{\ast}(c)\) is an isomorphism, and \(c\) is an isomorphism because
\(g'_{\ast}\) is conservative.

(c) By Proposition 1.9 the counit \(\lambda^{\ast}\lambda_{\ast}\to\mathrm{id}\) is an isomorphism. So
\(\psi^{\ast}\cong\psi^{\ast}\lambda^{\ast}\lambda_{\ast}\cong\varphi^{\ast}\lambda_{\ast}\), and both
\(\lambda_{\ast}\) and \(\varphi^{\ast}\) preserve finite limits.

(d) The first statement is clear. For the second, flatness is (b). Let \(J\) be as in Definition 2.1, and for
\(j\in J\) let \(f'_j\colon A'\to A'\otimes_AA_j\) and \(g'_j\colon A_j\to A'\otimes_AA_j\) be the canonical
morphisms. Let \(u\) be a morphism of \(A'\)-modules such that every \(f'^{\ast}_j(u)\), \(j\in J\), is an
isomorphism. Then \(g'_{j\ast}f'^{\ast}_j(u)\cong f_j^{\ast}g_{\ast}(u)\) is an isomorphism for every \(j\in J\). So
\(g_{\ast}(u)\) is an isomorphism, and then \(u\) is one. For the third statement, flatness is (a). Choose finite
sets \(J\subseteq I\) and \(L_j\subseteq K_j\), \(j\in J\), as in Definition 2.1. If the base change of \(u\) to
every \(A_{jk}\), \(j\in J\), \(k\in L_j\), is an isomorphism, then by Proposition 1.7(c) every \(f_j^{\ast}(u)\) is
an isomorphism, and so is \(u\). \(\square\)

By part (d) the flat covers are the coverings of a pretopology on \(\mathrm{Aff}_{\mathcal C}\) in the sense of
[Stacks, Tag [00VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-site)]; note that fibre products in \(\mathrm{Aff}_{\mathcal C}\) are pushouts in
\(\mathrm{Comm}(\mathcal C)\). We call it the *flat topology*.

For an \(A\)-module \(M\) and an \(A\)-algebra \(D\) we write \(M_D\) for \(D\otimes_AM\), regarded as an
\(A\)-module. A morphism \(h\colon D\to D'\) of \(A\)-algebras induces the \(A\)-linear morphism
\(h_M\colon M_D\to M_{D'}\), \(d\otimes m\mapsto h(d)\otimes m\).

**Theorem 2.4 (descent for modules).** Let \((f_i\colon A\to A_i)_{i\in J}\) be a family of flat morphisms indexed by
a finite set \(J\), such that the functors \(f_i^{\ast}\) are jointly conservative. Let \(M\) be an \(A\)-module.
Then
\[
M\xrightarrow{\ e\ }\prod_{i\in J}M_{A_i}\rightrightarrows\prod_{(i,j)\in J\times J}M_{A_i\otimes_AA_j}
\]
is an equalizer diagram in \(\mathrm{Mod}_A\), and so in \(\mathcal C\). Here \(e\) has the components
\(m\mapsto1\otimes m\). The two parallel morphisms \(d_0,d_1\) have the following \((i,j)\)-components: for \(d_0\),
the projection to \(M_{A_i}\) followed by the morphism induced by \(A_i\to A_i\otimes_AA_j\), \(x\mapsto x\otimes1\);
for \(d_1\), the projection to \(M_{A_j}\) followed by the morphism induced by \(A_j\to A_i\otimes_AA_j\),
\(y\mapsto1\otimes y\).

*Proof.* First, \(d_0e=d_1e\): the \((i,j)\)-components of both composites are induced by the structure morphism
\(A\to A_i\otimes_AA_j\), which is the same through \(A_i\) and through \(A_j\).

Step 1. Assume that for some \(k\in J\) there is a morphism of \(A\)-algebras \(r\colon A_k\to A\). Let
\(\mathrm{pr}\) denote projections from the two products, and define
\[
s=r_M\circ\mathrm{pr}_k\colon\prod_{i}M_{A_i}\to M,\qquad
t\colon\prod_{(i,j)}M_{A_i\otimes_AA_j}\to\prod_iM_{A_i},\quad\mathrm{pr}_i\circ t=(\rho_i)_M\circ\mathrm{pr}_{(i,k)},
\]
where \(\rho_i\colon A_i\otimes_AA_k\to A_i\) is the morphism of \(A\)-algebras \(x\otimes y\mapsto xf_i(r(y))\).
Then \(se=(rf_k)_M=\mathrm{id}_M\). Next \(\rho_i(x\otimes1)=x\), so \(td_0=\mathrm{id}\). Finally
\(\rho_i(1\otimes y)=f_i(r(y))\), so the \(i\)-th component of \(td_1\) is
\((f_i)_Mr_M\mathrm{pr}_k\), which is the \(i\)-th component of \(es\); hence \(td_1=es\). Now let
\(x\colon X\to\prod_iM_{A_i}\) be a morphism with \(d_0x=d_1x\). Then \(x=td_0x=td_1x=e(sx)\). The morphism \(e\) is
a monomorphism, because \(se=\mathrm{id}\). So \(x\) factors through \(e\) in exactly one way, and the diagram is an
equalizer. This step uses neither flatness nor conservativity.

Step 2. In general, fix \(k\in J\) and put \(A'=A_k\), \(A'_i=A_k\otimes_AA_i\) and \(M'=A_k\otimes_AM\). For every
\(A\)-algebra \(D\) there is an isomorphism of \(A_k\)-modules
\[
A_k\otimes_AM_D\longrightarrow(A_k\otimes_AD)\otimes_{A_k}M',\qquad
a\otimes(d\otimes m)\mapsto(a\otimes d)\otimes(1\otimes m),
\]
natural in \(D\): by Proposition 1.8(c) and Proposition 1.7(c), both sides are identified with
\((A_k\otimes_AD)\otimes_AM\). Moreover \(A'_i\otimes_{A'}A'_j=A_k\otimes_A(A_i\otimes_AA_j)\). The functor
\(f_k^{\ast}=A_k\otimes_A-\) preserves the two finite products, because \(f_k\) is flat and \(J\) is finite. So, by
the naturality in \(D\), the functor \(f_k^{\ast}\) carries the objects and the three morphisms \(e,d_0,d_1\) of the
diagram of the theorem to those of the same diagram for \(A'\), the family \((A'\to A'_i)_{i\in J}\) and the module
\(M'\). The \(A'\)-algebra \(A'_k=A_k\otimes_AA_k\) has the morphism of \(A'\)-algebras \(A'_k\to A'\),
\(x\otimes y\mapsto xy\). By Step 1 the image diagram is an equalizer.

Step 3. Let \(E\) be the equalizer of \(d_0\) and \(d_1\) in \(\mathrm{Mod}_A\), and let \(\bar e\colon M\to E\) be
the morphism induced by \(e\). For every \(k\in J\) the functor \(f_k^{\ast}\) preserves equalizers. So
\(f_k^{\ast}E\) is the equalizer of the image diagram, and \(f_k^{\ast}(\bar e)\) is an isomorphism by Step 2. Since
the functors \(f_k^{\ast}\) are jointly conservative, \(\bar e\) is an isomorphism. \(\square\)

*Reference:* [Toën–Vaquié 2009, Corollaire 2.11], where the statement is deduced from a descent theorem for stacks.

**Corollary 2.5 (the flat topology is subcanonical).** For every commutative monoid \(B\) the functor
\(h_B=\mathrm{Hom}_{\mathrm{Comm}(\mathcal C)}(B,-)\) is a sheaf for the flat topology: for every flat cover
\((f_i\colon A\to A_i)_{i\in I}\) the diagram
\[
\mathrm{Hom}(B,A)\longrightarrow\prod_{i\in I}\mathrm{Hom}(B,A_i)\rightrightarrows
\prod_{(i,j)\in I\times I}\mathrm{Hom}(B,A_i\otimes_AA_j)
\]
is an equalizer of sets.

*Proof.* Let \(J\subseteq I\) be as in Definition 2.1. Theorem 2.4 with \(M=A\) says that
\(A\to\prod_{J}A_i\rightrightarrows\prod_{J\times J}A_i\otimes_AA_j\) is an equalizer in \(\mathcal C\). All
morphisms in it are morphisms of commutative monoids. By Proposition 1.8(a) it is an equalizer in
\(\mathrm{Comm}(\mathcal C)\), and the products are products in \(\mathrm{Comm}(\mathcal C)\). Applying
\(\mathrm{Hom}(B,-)\) gives the claim for the subfamily indexed by \(J\).

Now let \((x_i)_{i\in I}\) be a family of morphisms \(x_i\colon B\to A_i\) such that \(x_i\) and \(x_j\) have the
same image in \(\mathrm{Hom}(B,A_i\otimes_AA_j)\) for all \(i,j\in I\). By the first part there is exactly one
\(x\colon B\to A\) with \(f_jx=x_j\) for all \(j\in J\). Fix \(i\in I\). By Lemma 2.3(d) the family
\((A_i\to A_i\otimes_AA_j)_{j\in J}\) satisfies the hypotheses of Theorem 2.4, so the first part applies to it. The
morphisms \(f_ix\) and \(x_i\) have the same composite with \(A_i\to A_i\otimes_AA_j\) for every \(j\in J\): the
composite for \(f_ix\) equals the composite of \(f_jx=x_j\) with \(A_j\to A_i\otimes_AA_j\), and this is the
composite for \(x_i\) by the assumption on the family. Hence \(f_ix=x_i\). \(\square\)

*Reference:* [Toën–Vaquié 2009, Corollaire 2.11(1)].

## 3. Zariski open immersions and relative schemes

**Definition 3.1.** A morphism \(f\colon A\to B\) of \(\mathrm{Comm}(\mathcal C)\) is *of finite presentation* if for
every directed system \((D_\alpha)\) of \(A\)-algebras the canonical map
\[
\operatorname{colim}_\alpha\mathrm{Hom}_{\mathrm{Alg}_A}(B,D_\alpha)\longrightarrow
\mathrm{Hom}_{\mathrm{Alg}_A}(B,\operatorname{colim}_\alpha D_\alpha)
\]
is bijective. The morphism \(f\) is a *Zariski open immersion* if it is flat, an epimorphism and of finite
presentation; we then also say that \(\operatorname{Spec}B\to\operatorname{Spec}A\) is a Zariski open immersion. A
*Zariski cover* is a flat cover \((A\to A_i)_{i\in I}\) in which every \(A\to A_i\) is a Zariski open immersion.

[Toën–Vaquié 2009, Définition 2.9] states the finiteness condition with filtered diagrams, and
[Vezzani 2012, Definition 15] with directed systems, as we do. The two conditions are equivalent. A directed set is
a filtered category, and every small filtered category receives a functor from a directed set such that each diagram on
the category has the same colimit as its restriction to the directed set [Stacks, Tag [0032](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-directed-category-system)]. So, for the categories
\(\mathcal C\) considered in [Toën–Vaquié 2009], the Zariski open immersions, the Zariski covers and the relative
schemes of this lesson are those of that work.

If \(f\) is an epimorphism, then \(\mathrm{Hom}_{\mathrm{Alg}_A}(B,D)\) has at most one element for every
\(A\)-algebra \(D\). So an epimorphism \(f\) is of finite presentation if and only if the following holds.

(FP) For every directed system \((D_\alpha)\) of \(A\)-algebras: if there is a morphism of \(A\)-algebras
\(B\to\operatorname{colim}_\alpha D_\alpha\), then there is a morphism of \(A\)-algebras \(B\to D_\alpha\) for some
\(\alpha\).

**Lemma 3.2.**

(a) Isomorphisms are Zariski open immersions. A composite of Zariski open immersions is one. If \(A\to B\) is a
Zariski open immersion and \(A\to A'\) is a morphism, then \(A'\to A'\otimes_AB\) is a Zariski open immersion.

(b) The Zariski covers are the coverings of a pretopology on \(\mathrm{Aff}_{\mathcal C}\).

*Proof.* (a) Flatness is Lemma 2.3. A composite of epimorphisms is an epimorphism. Let \(f\colon A\to B\) be an
epimorphism, \(g\colon A\to A'\) a morphism, and \(f'\colon A'\to B'\), \(g'\colon B\to B'\) as in
Proposition 1.8(c). If \(u,v\colon B'\to E\) satisfy \(uf'=vf'\), then \(ug'f=uf'g=vf'g=vg'f\), so \(ug'=vg'\),
and \(u=v\) by the pushout property. So \(f'\) is an epimorphism.

For finite presentation we use (FP). Let \(f\colon A\to B\) and \(g\colon B\to B''\) be Zariski open immersions, let
\((D_\alpha)\) be a directed system of \(A\)-algebras with colimit \(D\), and let \(h\colon B''\to D\) be a morphism
of \(A\)-algebras. By (FP) for \(f\) there is an index \(\alpha_0\) and a morphism of \(A\)-algebras
\(B\to D_{\alpha_0}\). It makes the \(D_\alpha\) with \(\alpha\ge\alpha_0\) a directed system of \(B\)-algebras with
colimit \(D\). The resulting morphism \(B\to D\) equals \(hg\), because both are morphisms of \(A\)-algebras and
\(f\) is an epimorphism. So \(h\) is a morphism of \(B\)-algebras. By (FP) for \(g\) there is a morphism of
\(B\)-algebras \(B''\to D_\alpha\) for some \(\alpha\ge\alpha_0\), and this is a morphism of \(A\)-algebras.

Now let \(f\colon A\to B\) be a Zariski open immersion, \(A\to A'\) a morphism and \(B'=A'\otimes_AB\). Let
\((D_\alpha)\) be a directed system of \(A'\)-algebras with colimit \(D\), and \(h\colon B'\to D\) a morphism of
\(A'\)-algebras. Its composite with \(B\to B'\) is a morphism of \(A\)-algebras \(B\to D\). By (FP) for \(f\) there
is a morphism of \(A\)-algebras \(B\to D_\alpha\) for some \(\alpha\). Together with \(A'\to D_\alpha\) it induces a
morphism of \(A'\)-algebras \(B'\to D_\alpha\), by Proposition 1.8(b).

(b) follows from (a) and Lemma 2.3(d). \(\square\)

**Sheaves.** The pretopology of Lemma 3.2 defines the *Zariski topology* on \(\mathrm{Aff}_{\mathcal C}\). A
*presheaf* is a functor \(F\colon\mathrm{Comm}(\mathcal C)\to\mathrm{Set}\). For \(s\in F(A)\) and a morphism
\(A\to A'\) we write \(s|_{A'}\in F(A')\) for the image of \(s\). A presheaf \(F\) is a *sheaf* if for every Zariski
cover \((A\to A_i)_{i\in I}\) the diagram
\[
F(A)\longrightarrow\prod_{i\in I}F(A_i)\rightrightarrows\prod_{(i,j)\in I\times I}F(A_i\otimes_AA_j)
\]
is an equalizer [Stacks, Tag [00VM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-sheaf-sets)]. The sheaves form a full subcategory \(\mathrm{Sh}(\mathrm{Aff}_{\mathcal C})\)
of the category of presheaves. We use three standard facts [Stacks, Tags [00W2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-limit-sheaf), [00WH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-sheafification-adjoint), [00WJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-sheafification-exact), [00WK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-sections-sheafification), [00WN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-mono-epi-sheaves)].

(S1) Limits of sheaves are computed objectwise. A morphism of sheaves \(F\to G\) is a monomorphism if and only if
\(F(A)\to G(A)\) is injective for every \(A\).

(S2) For every presheaf \(P\) there are a sheaf \(P^{a}\) and a morphism \(c\colon P\to P^{a}\) such that every
morphism from \(P\) to a sheaf factors through \(c\) in exactly one way. The functor \(P\mapsto P^{a}\) preserves
finite limits.

(S3) For every section \(t\in P^{a}(A)\) there is a Zariski cover \((A\to A_k)\) such that every \(t|_{A_k}\) lies
in the image of \(c\). If two sections of \(P\) over \(A\) have the same image in \(P^{a}(A)\), then they have the
same restriction to every member of a suitable Zariski cover of \(\operatorname{Spec}A\).

Zariski covers are flat covers. So by Corollary 2.5 every representable functor
\(h_B=\mathrm{Hom}_{\mathrm{Comm}(\mathcal C)}(B,-)\) is a sheaf. By the Yoneda lemma [Stacks, Tag [001P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-yoneda)], the
category \(\mathrm{Aff}_{\mathcal C}\) is a full subcategory of \(\mathrm{Sh}(\mathrm{Aff}_{\mathcal C})\), and for a
sheaf \(F\) the morphisms \(\operatorname{Spec}A\to F\) correspond to the elements of \(F(A)\). We write
\(\operatorname{Spec}B\) for the sheaf \(h_B\), and we call a sheaf an *affine scheme* if it is isomorphic to some
\(\operatorname{Spec}B\). By Proposition 1.8(b), a fibre product of affine schemes over an affine scheme is affine:
\(\operatorname{Spec}B\times_{\operatorname{Spec}A}\operatorname{Spec}B'=\operatorname{Spec}(B\otimes_AB')\).

**Definition 3.3.** Let \((u_i\colon F_i\to G)_{i\in I}\) be a family of morphisms of sheaves. A section
\(s\in G(A)\) is *locally in the image* of the family if there is a Zariski cover \((A\to A_k)_{k\in K}\) such
that for every \(k\) the section \(s|_{A_k}\) lies in \(u_i(F_i(A_k))\) for some \(i\in I\). The sections that are locally
in the image form a subsheaf of \(G\), called the *image* of the family. The family is *jointly surjective* if its
image is \(G\).

The image is a subpresheaf, because a Zariski cover can be pulled back along any morphism \(A\to A'\). It is a
subsheaf, because Zariski covers can be composed: if \(s\) is locally in the image on every member of a Zariski
cover, then \(s\) is locally in the image. If \(j\colon F\to G\) is a monomorphism, then the image of the family
\((j)\) is \(j(F)\), and \(j\) is an isomorphism from \(F\) onto it: if \(s|_{A_k}=j(t_k)\) for all \(k\), then the
\(t_k\) agree on the overlaps because \(j\) is injective, so they glue to a section \(t\) of \(F\) with \(j(t)=s\).

**Lemma 3.4 (a sheaf is glued from a jointly surjective family).** Let \((u_i\colon F_i\to F)_{i\in I}\) be a
jointly surjective family of morphisms of sheaves, and let \(G\) be a sheaf. Then \(v\mapsto(vu_i)_{i\in I}\) is a
bijection from \(\mathrm{Hom}(F,G)\) to the set of families \((v_i\colon F_i\to G)_{i\in I}\) such that for all
\(i,j\) the two composites \(F_i\times_FF_j\to F_i\to G\) and \(F_i\times_FF_j\to F_j\to G\) are equal.

*Proof.* Call a *local lifting* of \(s\in F(A)\) a Zariski cover \((A\to A_k)_{k\in K}\) together with indices
\(i(k)\) and sections \(s_k\in F_{i(k)}(A_k)\) such that \(u_{i(k)}(s_k)=s|_{A_k}\). Every section has a local
lifting, because the family is jointly surjective.

Injectivity. Let \(v,v'\colon F\to G\) with \(vu_i=v'u_i\) for all \(i\). For a local lifting of \(s\) we get
\(v(s)|_{A_k}=vu_{i(k)}(s_k)=v'u_{i(k)}(s_k)=v'(s)|_{A_k}\) for all \(k\). Since \(G\) is a sheaf, \(v(s)=v'(s)\).

Surjectivity. Let \((v_i)\) be a family as in the statement. For a local lifting of \(s\) put
\(w_k=v_{i(k)}(s_k)\in G(A_k)\). The pair of restrictions of \(s_k\) and \(s_l\) to \(A_k\otimes_AA_l\) is a section
of \(F_{i(k)}\times_FF_{i(l)}\). So \(w_k\) and \(w_l\) have the same restriction to \(A_k\otimes_AA_l\), and there
is exactly one \(w\in G(A)\) with \(w|_{A_k}=w_k\) for all \(k\). The section \(w\) does not depend on the local
lifting: the union of two local liftings is a local lifting, and its glued section restricts to the \(w_k\) of
both. Put \(v(s)=w\). This is compatible with a morphism \(A\to A'\), because a local lifting of \(s\) can be pulled
back to a local lifting of \(s|_{A'}\). So \(v\) is a morphism of sheaves. For \(s=u_i(a)\) the trivial cover with
the section \(a\) is a local lifting; so \(vu_i=v_i\). \(\square\)

**Definition 3.5.**

(a) Let \(X\) be an affine scheme. A subsheaf \(U\subseteq X\) is a *Zariski open* of \(X\) if it is the image of a
family \((X_i\to X)_{i\in I}\) of Zariski open immersions of affine schemes, in the sense of Definition 3.1. The
index set may be infinite, and it may be empty.

(b) A morphism of sheaves \(f\colon F\to G\) is a *Zariski open immersion* if for every affine scheme \(X\) and
every morphism \(X\to G\) the projection \(F\times_GX\to X\) is a monomorphism whose image is a Zariski open of
\(X\).

**Lemma 3.6.**

(a) A Zariski open immersion of sheaves is a monomorphism.

(b) If \(F\to G\) is a Zariski open immersion and \(G'\to G\) is a morphism of sheaves, then \(F\times_GG'\to G'\)
is a Zariski open immersion.

(c) Let \(X\) be an affine scheme and \(U\subseteq X\) a Zariski open. Then the inclusion \(U\to X\) is a Zariski
open immersion, and for every morphism of affine schemes \(X'\to X\) the subsheaf \(U\times_XX'\) of \(X'\) is a
Zariski open of \(X'\).

(d) A composite of two Zariski open immersions of sheaves is a Zariski open immersion.

(e) If \(g\circ h\) is a Zariski open immersion and \(g\) is a monomorphism, then \(h\) is a Zariski open immersion.

(f) Let \(X\) be an affine scheme, \((X_k\to X)_{k\in K}\) a Zariski cover and \(W\subseteq X\) a subsheaf. If
\(W\times_XX_k\) is a Zariski open of \(X_k\) for every \(k\), then \(W\) is a Zariski open of \(X\).

*Proof.* (a) Let \(f\colon F\to G\) be a Zariski open immersion and let \(a,b\in F(A)\) with \(f(a)=f(b)\). This
common value is a morphism \(X=\operatorname{Spec}A\to G\). The pairs \((a,\mathrm{id}_A)\) and
\((b,\mathrm{id}_A)\) are sections of \(F\times_GX\) over \(A\) with the same image \(\mathrm{id}_A\) in \(X(A)\).
Since \(F\times_GX\to X\) is a monomorphism, \(a=b\).

(b) For a morphism \(X\to G'\) from an affine scheme we have \((F\times_GG')\times_{G'}X=F\times_GX\).

(c) Let \(U\) be the image of the Zariski open immersions \((X_i\to X)_{i\in I}\) of affine schemes, let
\(t\colon X'\to X\) be a morphism of affine schemes and put \(X'_i=X_i\times_XX'\). The morphisms \(X'_i\to X'\) are
Zariski open immersions of affine schemes by Lemma 3.2. A section \(s\in X'(A)\) lies in \(U\times_XX'\) if and only
if \(t(s)\in U(A)\), that is, if and only if there is a Zariski cover \((A\to A_k)\) such that every
\(t(s)|_{A_k}\) factors through some \(X_i\). By the definition of the fibre product this holds if and only if every
\(s|_{A_k}\) factors through some \(X'_i\). So \(U\times_XX'\) is the image of the family \((X'_i\to X')\), which is
a Zariski open of \(X'\). The inclusion \(U\to X\) is a monomorphism. So it is a Zariski open immersion.

(d) Let \(f\colon F\to G\) and \(g\colon G\to H\) be Zariski open immersions and let \(X\to H\) be a morphism from
an affine scheme. Put \(G_X=G\times_HX\) and \(F_X=F\times_HX=F\times_GG_X\). By (a) and (b) the morphisms
\(F_X\to G_X\) and \(G_X\to X\) are monomorphisms, and we regard \(F_X\subseteq G_X\subseteq X\) as subsheaves. The
subsheaf \(G_X\) is the image of a family \((X_i\to X)_{i\in I}\) of Zariski open immersions of affine schemes. Each
\(X_i\to X\) factors through \(G_X\). So \(X_i\) maps to \(G\), and the subsheaf
\(F\times_GX_i=F_X\times_{G_X}X_i\) of \(X_i\) is the image of a family \((X_{ij}\to X_i)_j\) of Zariski open
immersions of affine schemes. The composites \(X_{ij}\to X\) are Zariski open immersions of affine schemes, by
Lemma 3.2, and they factor through \(F_X\). We show that \(F_X\) is the image of the family \((X_{ij}\to X)_{i,j}\).
Let \(s\in F_X(A)\). Since \(s\in G_X(A)\), there is a Zariski cover \((A\to A_k)\) such that every \(s|_{A_k}\) is
the image of a section \(s_k\) of some \(X_{i(k)}\). Since \(s|_{A_k}\) lies in \(F_X\), the section \(s_k\) lies in
\(F_X\times_{G_X}X_{i(k)}\). So there are Zariski covers \((A_k\to A_{kl})_l\) such that every \(s_k|_{A_{kl}}\)
factors through some \(X_{i(k)j}\). The composite family \((A\to A_{kl})_{k,l}\) is a Zariski cover, and it shows
that \(s\) is locally in the image of the family \((X_{ij}\to X)\).

(e) Let \(h\colon E\to F\) and \(g\colon F\to G\). Since \(g\) is a monomorphism, the morphism
\((\mathrm{id},h)\colon E\to E\times_GF\) is an isomorphism, and under it the projection \(E\times_GF\to F\)
becomes \(h\). So \(h\) is the base change of \(gh\) along \(g\), and (b) applies.

(f) Let \(W\times_XX_k\) be the image of the Zariski open immersions \((X_{kl}\to X_k)_l\) of affine schemes. The
composites \(X_{kl}\to X\) are Zariski open immersions of affine schemes, and they factor through \(W\). Let
\(s\in W(A)\subseteq X(A)\) and let \(\operatorname{Spec}A_k=\operatorname{Spec}A\times_XX_k\). Then
\((A\to A_k)_k\) is a Zariski cover, and \(s|_{A_k}\) is a section of \(W\times_XX_k\). So \(s|_{A_k}\) is locally
in the image of the \(X_{kl}\), and \(s\) is locally in the image of the family \((X_{kl}\to X)_{k,l}\). Hence \(W\)
is the image of this family. \(\square\)

*Reference:* [Toën–Vaquié 2009, Lemme 2.13] for (b) and (d).

Definitions 3.1 and 3.5 both speak of Zariski open immersions between affine schemes. The next proposition compares
them.

**Proposition 3.7.** Let \(f\colon A\to B\) be a morphism of \(\mathrm{Comm}(\mathcal C)\) and let
\(\varphi\colon\operatorname{Spec}B\to\operatorname{Spec}A\) be the corresponding morphism of affine schemes.

(a) If \(f\) is a Zariski open immersion in the sense of Definition 3.1, then \(\varphi\) is a Zariski open immersion
in the sense of Definition 3.5.

(b) If \(\varphi\) is a Zariski open immersion in the sense of Definition 3.5, then \(f\) is a flat epimorphism, and
there is a finite Zariski cover \((B\to B_k)_{k\in K}\) such that every composite \(A\to B_k\) is a Zariski open
immersion in the sense of Definition 3.1.

*Proof.* (a) Let \(X'\to\operatorname{Spec}A\) be a morphism of affine schemes. By Lemma 3.2 the projection
\(\operatorname{Spec}B\times_{\operatorname{Spec}A}X'\to X'\) is a Zariski open immersion of affine schemes. It is a
monomorphism of sheaves, because it comes from an epimorphism of \(\mathrm{Comm}(\mathcal C)\). Its image is the
image of a family with one member, so it is a Zariski open of \(X'\).

(b) Put \(Y=\operatorname{Spec}A\) and \(Z=\operatorname{Spec}B\). Apply Definition 3.5(b) to the identity of \(Y\):
the morphism \(\varphi\) is a monomorphism, and its image \(U\) is the image of a family \((Y_i\to Y)_{i\in I}\) of
Zariski open immersions of affine schemes, \(Y_i=\operatorname{Spec}B_i\). Since
\(\mathrm{Hom}(B,D)\to\mathrm{Hom}(A,D)\) is injective for all \(D\), the morphism \(f\) is an epimorphism. The
morphism \(\varphi\) is an isomorphism from \(Z\) onto \(U\). Each \(Y_i\to Y\) factors through \(U\), so it is
\(\varphi\circ g_i\) for a morphism \(g_i\colon Y_i\to Z\), given by a morphism \(B\to B_i\) of
\(\mathrm{Comm}(\mathcal C)\). Since \(\varphi\) is a monomorphism, \(Y_i\cong Y_i\times_YZ\), and \(g_i\) is the
base change of \(Y_i\to Y\) along \(\varphi\). By Lemma 3.2, \(B\to B_i\) is a Zariski open immersion in the sense
of Definition 3.1.

The family \((g_i)\) is jointly surjective. So the section \(\mathrm{id}_B\in Z(B)\) is locally in its image: there
are a Zariski cover \((B\to D_k)_{k\in K}\), indices \(i(k)\) and morphisms \(B_{i(k)}\to D_k\) such that the
composite \(B\to B_{i(k)}\to D_k\) is the given morphism \(B\to D_k\). By Definition 2.1 we may assume that \(K\) is
finite and that the base change functors to the \(D_k\) are jointly conservative. Let \(u\) be a morphism of
\(B\)-modules such that \(B_{i(k)}\otimes_Bu\) is an isomorphism for every \(k\). By Proposition 1.7(c), every
\(D_k\otimes_Bu\) is then an isomorphism, so \(u\) is an isomorphism. Hence \((B\to B_{i(k)})_{k\in K}\) is a finite
Zariski cover, and every composite \(A\to B_{i(k)}\) is a Zariski open immersion in the sense of Definition 3.1.

It remains to show that \(f\) is flat. Write \(g_k\colon B\to B_{i(k)}\). Let \((M_\alpha)\) be a finite diagram of
\(A\)-modules and \(c\colon f^{\ast}(\lim M_\alpha)\to\lim f^{\ast}M_\alpha\) the comparison morphism. The
comparison morphism of the functor \(g_k^{\ast}f^{\ast}\cong(g_kf)^{\ast}\) is the composite of \(g_k^{\ast}(c)\)
with the comparison morphism of \(g_k^{\ast}\) for the diagram \((f^{\ast}M_\alpha)\). Both \(g_kf\) and \(g_k\) are
flat. So \(g_k^{\ast}(c)\) is an isomorphism for every \(k\in K\), and \(c\) is an isomorphism because the functors
\(g_k^{\ast}\) are jointly conservative. \(\square\)

*Reference:* [Toën–Vaquié 2009, Lemme 2.14] states in addition that \(f\) is of finite presentation in (b). The
argument given there for this step forms \(B'_\alpha\otimes_BB_i\) for algebras \(B'_\alpha\) that are
\(A\)-algebras and are not known to be \(B\)-algebras. So we prove (b) in the form above, and we prove the full
converse of (a) in Corollary 4.3 for the categories treated in Sections 5 and 6.

**Definition 3.8.** A sheaf \(F\) on \(\mathrm{Aff}_{\mathcal C}\) is a *scheme relative to \(\mathcal C\)* if there
is a jointly surjective family \((u_i\colon X_i\to F)_{i\in I}\) of Zariski open immersions from affine schemes
\(X_i\). Such a family is called an *atlas* of \(F\). The category \(\mathrm{Sch}(\mathcal C)\) of schemes relative
to \(\mathcal C\) is the full subcategory of \(\mathrm{Sh}(\mathrm{Aff}_{\mathcal C})\) on these sheaves.

[Toën–Vaquié 2009, Définition 2.15] asks that the morphism from the coproduct of the sheaves \(X_i\) to \(F\) be an
epimorphism of sheaves. This is the same condition: an epimorphism of sheaves is a morphism for which every section
of the target is locally in the image [Stacks, Tag [00WN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-mono-epi-sheaves)], and by (S3) a section of the coproduct sheaf is locally a
section of some \(X_i\).

**Proposition 3.9.**

(a) Every affine scheme is a scheme relative to \(\mathcal C\).

(b) If \(F\) is a scheme and \(U\to F\) is a Zariski open immersion, then \(U\) is a scheme.

(c) Let \(F_1\to F_0\) be a morphism of sheaves, where \(F_0\) is a scheme with an atlas \((X_i\to F_0)_{i\in I}\).
If \(F_1\times_{F_0}X_i\) is a scheme for every \(i\), then \(F_1\) is a scheme.

(d) If \(F\to H\) and \(G\to H\) are morphisms of schemes, then the sheaf \(F\times_HG\) is a scheme. So
\(\mathrm{Sch}(\mathcal C)\) has fibre products, and they are computed objectwise.

*Proof.* (a) The identity of an affine scheme is an atlas, by Proposition 3.7(a).

(b) Let \((X_i\to F)\) be an atlas and put \(U_i=U\times_FX_i\). By Lemma 3.6(b), \(U_i\to X_i\) is a Zariski open
immersion. So \(U_i\) is isomorphic to a Zariski open of \(X_i\), the image of a family \((X_{ij}\to X_i)_j\) of
Zariski open immersions of affine schemes. The morphism \(X_{ij}\to X_i\) is a Zariski open immersion of sheaves by
Proposition 3.7(a), and it factors through the monomorphism \(U_i\to X_i\). So \(X_{ij}\to U_i\) is a Zariski open
immersion by Lemma 3.6(e). The morphism \(U_i\to U\) is one by Lemma 3.6(b), as the base change of \(X_i\to F\). So
\(X_{ij}\to U\) is a Zariski open immersion by Lemma 3.6(d). The family \((X_{ij}\to U)_{i,j}\) is jointly
surjective: for \(s\in U(A)\) the image of \(s\) in \(F(A)\) lifts to some \(X_i\) on each member \(A_k\) of a
Zariski cover; this gives sections of \(U_i\) over the \(A_k\), and they are locally in the image of the \(X_{ij}\).

(c) Let \((X_{ij}\to F_1\times_{F_0}X_i)_j\) be atlases. The morphism \(F_1\times_{F_0}X_i\to F_1\) is a Zariski open
immersion, as the base change of \(X_i\to F_0\). So the composites \(X_{ij}\to F_1\) are Zariski open immersions by
Lemma 3.6(d). They are jointly surjective by the argument used in (b).

(d) Step 1. Let \(X\) and \(Y\) be affine, and assume that \(Y\to H\) factors through a Zariski open immersion
\(Z\to H\) with \(Z\) affine. Since \(Z\to H\) is a monomorphism, \(X\times_HY=V\times_ZY\) with \(V=X\times_HZ\).
The morphism \(V\to X\) is a Zariski open immersion. As in (b), \(V\) has an atlas \((W_a\to V)_a\) in which every
\(W_a\) is affine. The fibre of \(V\times_ZY\to V\) over \(W_a\) is \(W_a\times_ZY\), which is affine. By (c),
\(V\times_ZY\) is a scheme.

Step 2. Let \(X\) and \(Y\) be affine and let \((Z_l\to H)_l\) be an atlas of \(H\). As in (b), applied to the
Zariski open immersions \(Y\times_HZ_l\to Y\), there are Zariski open immersions \(Y_{lb}\to Y\) of affine schemes
that factor through \(Y\times_HZ_l\) and are jointly surjective onto it. The family \((Y_{lb}\to Y)_{l,b}\) is an
atlas of \(Y\): it is jointly surjective, because the atlas of \(H\) is. Each \(Y_{lb}\to H\) factors through
\(Z_l\). By Step 1 the fibres \(X\times_HY_{lb}\) of \(X\times_HY\to Y\) are schemes, and by (c) \(X\times_HY\) is a
scheme.

Step 3. In general let \((X_i\to F)\) and \((Y_j\to G)\) be atlases. By (c), applied to \(F\times_HG\to G\), it is
enough to show that every \(F\times_HY_j\) is a scheme. By (c), applied to \(F\times_HY_j\to F\), it is enough to
show that every \(X_i\times_HY_j\) is a scheme. This is Step 2. The last statement follows from (S1). \(\square\)

*Reference:* [Toën–Vaquié 2009, Propositions 2.17 and 2.18].

**Example 3.10 (the empty scheme).** Let \(E\) be the presheaf for which \(E(A)\) has one element if the empty
family is a Zariski cover of \(\operatorname{Spec}A\), and \(E(A)=\emptyset\) otherwise. It is a presheaf, because
the base change of the empty cover is the empty cover. It is a sheaf. Let \((A\to A_i)\) be a Zariski cover. If all
\(E(A_i)\) are non-empty, then composing the cover with the empty covers of the \(\operatorname{Spec}A_i\) shows
that the empty family covers \(\operatorname{Spec}A\); so \(E(A)\) has one element, as do all sets in the sheaf
condition. If some \(E(A_i)\) is empty, then \(E(A)\) is empty, because there is a map \(E(A)\to E(A_i)\), and the
product of the \(E(A_i)\) is empty too. In both cases the sheaf condition holds. The sheaf \(E\) is an initial
object of \(\mathrm{Sh}(\mathrm{Aff}_{\mathcal C})\): if the empty family covers \(\operatorname{Spec}A\), then
\(G(A)\) has exactly one element for every sheaf \(G\) [Stacks, Tag [04B3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-remark-sheaf-condition-empty-covering)]. And \(E\) is a scheme, with the empty
family as atlas: every section of \(E\) is locally in the image of the empty family, on the empty cover.

For \(\mathrm{Ab}\) the empty family covers \(\operatorname{Spec}A\) exactly when \(A=0\) (Example 2.2(c)), and a
ring homomorphism \(0\to A\) exists exactly when \(A=0\). So \(E=\operatorname{Spec}0\), the spectrum of the zero
ring. In the same way, for \(\mathrm{Set}_{\ast}\) the sheaf \(E\) is the spectrum of the zero monoid. For
\(\mathrm{Set}\) it is the empty functor. The empty functor is not representable, because every plain monoid \(N\)
has a morphism to the trivial monoid. So relative to \(\mathrm{Set}\) the empty scheme is a scheme that is not
affine.

## 4. A comparison principle

In the two cases that matter to us, relative schemes can be compared with spaces that carry a structure sheaf:
schemes in the case of abelian groups, monoid schemes in the case of sets. Both comparisons follow from one
statement, which isolates what is needed from the spaces.

**Definition 4.1.** A *geometric model* for \(\mathcal C\) consists of a category \(\mathcal G\), a functor
\(X\mapsto|X|\) from \(\mathcal G\) to topological spaces, and a fully faithful functor
\(\operatorname{Spec}\colon\mathrm{Aff}_{\mathcal C}\to\mathcal G\), with the properties (G1)–(G5) below. An object
of \(\mathcal G\) is *affine* if it is isomorphic to \(\operatorname{Spec}A\) for some \(A\).

(G1) *Open subobjects.* For every object \(X\) and every open subset \(V\subseteq|X|\) there is a morphism
\(j_V\colon X_V\to X\) such that \(|j_V|\) is a homeomorphism from \(|X_V|\) onto \(V\), and such that a morphism
\(t\colon T\to X\) factors through \(j_V\) if and only if \(|t|(|T|)\subseteq V\); the factorization is then unique.
A morphism is an *open immersion* if it is the composite of an isomorphism \(Y\to X_V\) and \(j_V\), for some \(V\).

(G2) *Affine opens.* For every object \(X\), the open subsets \(V\subseteq|X|\) for which \(X_V\) is affine form a
basis of the topology of \(|X|\). We call them the *affine opens* of \(X\).

(G3) *Morphisms glue.* Let \(X,Y\) be objects and \((V_k)_{k\in K}\) an open cover of \(|X|\). Restriction is a
bijection from the set of morphisms \(X\to Y\) to the set of families of morphisms \(f_k\colon X_{V_k}\to Y\) such
that \(f_k\) and \(f_l\) have the same restriction to \(X_{V_k\cap V_l}\) for all \(k,l\).

(G4) *Objects glue.* Let \((X_i)_{i\in I}\) be objects, \(U_{ij}\subseteq|X_i|\) open subsets with
\(U_{ii}=|X_i|\), and \(\varphi_{ij}\colon(X_i)_{U_{ij}}\to(X_j)_{U_{ji}}\) isomorphisms with
\(\varphi_{ii}=\mathrm{id}\), such that for all \(i,j,k\) we have
\(|\varphi_{ij}|(U_{ij}\cap U_{ik})=U_{ji}\cap U_{jk}\) and \(\varphi_{jk}\circ\varphi_{ij}=\varphi_{ik}\) on
\((X_i)_{U_{ij}\cap U_{ik}}\). Then there are an object \(X\) and open immersions \(\psi_i\colon X_i\to X\) such
that the sets \(|\psi_i|(|X_i|)\) cover \(|X|\), such that
\(|\psi_i|(U_{ij})=|\psi_i|(|X_i|)\cap|\psi_j|(|X_j|)\), and such that \(\psi_j\circ\varphi_{ij}=\psi_i\) on
\((X_i)_{U_{ij}}\).

(G5) *Dictionary.* A morphism \(A\to B\) of \(\mathrm{Comm}(\mathcal C)\) is a Zariski open immersion in the sense
of Definition 3.1 if and only if \(\operatorname{Spec}B\to\operatorname{Spec}A\) is an open immersion of
\(\mathcal G\). A family \((A\to A_i)_{i\in I}\) of Zariski open immersions is a Zariski cover if and only if the
images of the spaces \(|\operatorname{Spec}A_i|\) cover \(|\operatorname{Spec}A|\).

In (G1) we identify \(|X_V|\) with \(V\). For open sets \(W\subseteq V\), the universal property in (G1) shows that
\((X_V)_W\) and \(X_W\) are canonically isomorphic over \(X\). The *restriction* of a morphism \(f\colon X_V\to Y\)
to \(W\) is its composite with \(X_W\to X_V\). A morphism \(j_V\) is a monomorphism, by the uniqueness in (G1), and
so is every open immersion.

**Theorem 4.2 (comparison principle).** Let \((\mathcal G,|\cdot|,\operatorname{Spec})\) be a geometric model for
\(\mathcal C\). For an object \(X\) of \(\mathcal G\) let \(h_X\) be the presheaf on \(\mathrm{Aff}_{\mathcal C}\)
with \(h_X(A)=\mathrm{Hom}_{\mathcal G}(\operatorname{Spec}A,X)\).

(a) \(h_X\) is a scheme relative to \(\mathcal C\). If \((V_i)_{i\in I}\) is a cover of \(|X|\) by affine opens,
then \((h_{X_{V_i}}\to h_X)_{i\in I}\) is an atlas.

(b) The functor \(X\mapsto h_X\) is an equivalence of categories from \(\mathcal G\) to \(\mathrm{Sch}(\mathcal C)\).

(c) Let \(T=\operatorname{Spec}A\). The map \(V\mapsto h_{T_V}\) is a bijection from the set of open subsets of
\(|T|\) to the set of Zariski opens of the affine scheme \(T\), and it preserves inclusions in both directions.

(d) A morphism \(j\) of \(\mathcal G\) is an open immersion if and only if \(h_j\) is a Zariski open immersion.

*Proof.* Since \(\operatorname{Spec}\) is fully faithful, \(h_{\operatorname{Spec}B}=\mathrm{Hom}(B,-)\) is the
affine scheme \(\operatorname{Spec}B\) of Section 3. For an affine object \(T\) of \(\mathcal G\) we write \(F(T)\)
for \(F(A)\), where \(T\cong\operatorname{Spec}A\); in particular \(h_X(T)=\mathrm{Hom}_{\mathcal G}(T,X)\).

Step 0 (open sets and subfunctors). Let \(V,W\subseteq|X|\) be open. By (G1) the map \(h_{X_V}\to h_X\) is
injective, and its image consists of the morphisms \(t\colon T\to X\) with \(|t|(|T|)\subseteq V\). We regard
\(h_{X_V}\) as a subfunctor of \(h_X\). It follows that \(h_{X_V}\cap h_{X_W}=h_{X_{V\cap W}}\), and that for every
morphism \(f\colon Y\to X\) of \(\mathcal G\) we have \(h_Y\times_{h_X}h_{X_V}=h_{Y_{V'}}\) with
\(V'=|f|^{-1}(V)\). Moreover \(V\subseteq W\) if and only if \(h_{X_V}\subseteq h_{X_W}\). Indeed, assume
\(h_{X_V}\subseteq h_{X_W}\) and let \(V_0\subseteq V\) be an affine open. The morphism \(j_{V_0}\) is a section of
\(h_{X_V}\) over the affine object \(X_{V_0}\), so it is a section of \(h_{X_W}\), and \(V_0\subseteq W\). By (G2),
\(V\) is a union of affine opens. So \(V\subseteq W\).

Step 1 (\(h_X\) is a sheaf). Let \((A\to A_k)_{k\in K}\) be a Zariski cover and \(T=\operatorname{Spec}A\). By
(G5) each \(\operatorname{Spec}A_k\to T\) is an open immersion; let \(V_k\subseteq|T|\) be its image, so that
\(\operatorname{Spec}A_k\cong T_{V_k}\) over \(T\), and the \(V_k\) cover \(|T|\). By Lemma 3.2 and (G5),
\(\operatorname{Spec}(A_k\otimes_AA_l)\to T\) is an open immersion too, with some image \(V_{kl}\). A morphism
\(A\to D\) factors through \(A\to A_k\otimes_AA_l\) if and only if it factors through \(A\to A_k\) and through
\(A\to A_l\), by the pushout property. So \(h_{T_{V_{kl}}}=h_{T_{V_k}}\cap h_{T_{V_l}}=h_{T_{V_k\cap V_l}}\), and
\(V_{kl}=V_k\cap V_l\) by Step 0. The sheaf condition for \(h_X\) and the given cover therefore says: the morphisms
\(T\to X\) correspond to the families of morphisms \(T_{V_k}\to X\) that agree on the \(T_{V_k\cap V_l}\). This is
(G3).

Step 2 (unions). Let \((V_k)_{k\in K}\) be open subsets of \(|X|\) with union \(V\). Then \(h_{X_V}\) is the image
of the family \((h_{X_{V_k}}\to h_X)_{k\in K}\). Indeed, \(h_{X_V}\) is a subsheaf of \(h_X\) that contains every
\(h_{X_{V_k}}\), so it contains the image. Conversely let \(t\colon T\to X\) be a section of \(h_{X_V}\) over
\(T=\operatorname{Spec}A\). The open sets \(|t|^{-1}(V_k)\) cover \(|T|\). By (G2) there are affine opens
\(O_l\subseteq|T|\), \(l\in L\), that cover \(|T|\), each contained in some \(|t|^{-1}(V_k)\). Write
\(T_{O_l}\cong\operatorname{Spec}A_l\). Since \(\operatorname{Spec}\) is fully faithful, the open immersion
\(T_{O_l}\to T\) comes from a morphism \(A\to A_l\). By (G5) it is a Zariski open immersion, and
\((A\to A_l)_{l\in L}\) is a Zariski cover. The restriction of \(t\) to \(A_l\) is a section of some
\(h_{X_{V_k}}\). So \(t\) is locally in the image.

Step 3 (proof of (c)). By (G5), the Zariski open immersions of affine schemes with target \(T\) are, up to
isomorphism, the morphisms \(T_{V}\to T\) with \(V\) an affine open. By Step 2 the image of a family of them is
\(h_{T_V}\), where \(V\) is the union of the corresponding open sets. Conversely every open \(V\subseteq|T|\) is a
union of affine opens by (G2), so \(h_{T_V}\) is a Zariski open of \(T\) by Step 2. Injectivity and the statement on
inclusions are in Step 0.

Step 4 (open immersions give Zariski open immersions). Let \(j\colon Y\to X\) be an open immersion of
\(\mathcal G\), with image \(V\). Then \(h_j\) is injective with image \(h_{X_V}\). For a morphism
\(t\colon T\to X\) from an affine object, Step 0 gives \(h_Y\times_{h_X}h_T\cong h_{T_{V'}}\) with
\(V'=|t|^{-1}(V)\). By Step 3 this is a Zariski open of \(T\). So \(h_j\) is a Zariski open immersion.

Step 5 (proof of (a)). By (G2) there is a cover \((V_i)\) of \(|X|\) by affine opens. The sheaves \(h_{X_{V_i}}\)
are affine schemes. The morphisms \(h_{X_{V_i}}\to h_X\) are Zariski open immersions by Step 4, and they are
jointly surjective by Step 2.

Step 6 (\(h\) is fully faithful). Let \(f,g\colon X\to Y\) be morphisms with \(h_f=h_g\). For every affine open
\(V\) of \(X\) we get \(f\circ j_V=h_f(j_V)=h_g(j_V)=g\circ j_V\). The affine opens cover \(|X|\), so \(f=g\) by
(G3). Now let \(\tau\colon h_X\to h_Y\) be a morphism of sheaves. For an affine open \(V\) of \(X\) put
\(f_V=\tau(j_V)\colon X_V\to Y\). If \(V_0\subseteq V\) are affine opens, then \(f_{V_0}\) is the restriction of
\(f_V\), because \(\tau\) is natural. If \(V_1,V_2\) are affine opens, then \(V_1\cap V_2\) is a union of affine
opens \(V_0\), and \(f_{V_1}\) and \(f_{V_2}\) both restrict to \(f_{V_0}\) on \(X_{V_0}\); by (G3) they have the
same restriction to \(X_{V_1\cap V_2}\). By (G3) again there is a morphism \(f\colon X\to Y\) with
\(f\circ j_V=f_V\) for all affine opens \(V\). We claim \(h_f=\tau\). Let \(t\in h_X(A)\). By Step 2 there is a
Zariski cover \((A\to A_l)\) such that every \(t|_{A_l}\) is \(j_V\circ t_l\) for some affine open \(V\) and some
\(t_l\colon\operatorname{Spec}A_l\to X_V\). Then
\(\tau(t)|_{A_l}=\tau(j_V\circ t_l)=f_V\circ t_l=f\circ t|_{A_l}=h_f(t)|_{A_l}\). Since \(h_Y\) is a sheaf,
\(\tau(t)=h_f(t)\).

Step 7 (\(h\) is essentially surjective). Let \(F\) be a scheme relative to \(\mathcal C\) with an atlas
\((u_i\colon X_i\to F)_{i\in I}\), \(X_i=\operatorname{Spec}A_i\). We regard \(X_i\) also as an object of
\(\mathcal G\), so that \(h_{X_i}=X_i\).

The projection \(X_i\times_FX_j\to X_i\) is a base change of the Zariski open immersion \(u_j\). So it is a
monomorphism whose image is a Zariski open of \(X_i\). By Step 3 this image is \(h_{(X_i)_{U_{ij}}}\) for exactly
one open subset \(U_{ij}\subseteq|X_i|\). We write \(h_{U_{ij}}\) for it. Since \(u_i\) is a monomorphism,
\(U_{ii}=|X_i|\). A section \(t\) of \(X_i\) over \(A\) lies in \(h_{U_{ij}}\) if and only if there is a section
\(t'\) of \(X_j\) over \(A\) with \(u_j(t')=u_i(t)\); then \(t'\) is unique, because \(u_j\) is a monomorphism, and
\(t'\) lies in \(h_{U_{ji}}\). So \(t\mapsto t'\) is an isomorphism of sheaves
\(\sigma_{ij}\colon h_{U_{ij}}\to h_{U_{ji}}\), with inverse \(\sigma_{ji}\), and \(\sigma_{ii}=\mathrm{id}\). By
Step 6 there is exactly one isomorphism \(\varphi_{ij}\colon(X_i)_{U_{ij}}\to(X_j)_{U_{ji}}\) of \(\mathcal G\) with
\(h_{\varphi_{ij}}=\sigma_{ij}\), and \(\varphi_{ii}=\mathrm{id}\).

We check the conditions of (G4). Let \(t\) be a section of \(h_{U_{ij}}\cap h_{U_{ik}}=h_{U_{ij}\cap U_{ik}}\).
Then \(t'=\sigma_{ij}(t)\) and \(t''=\sigma_{ik}(t)\) satisfy \(u_j(t')=u_i(t)=u_k(t'')\). So \(t'\) lies in
\(h_{U_{ji}}\cap h_{U_{jk}}\), and \(\sigma_{jk}(t')=t''\). Hence \(\sigma_{ij}\) maps \(h_{U_{ij}\cap U_{ik}}\)
into \(h_{U_{ji}\cap U_{jk}}\), and \(\sigma_{jk}\sigma_{ij}=\sigma_{ik}\) there. By symmetry \(\sigma_{ji}\) maps
\(h_{U_{ji}\cap U_{jk}}\) into \(h_{U_{ij}\cap U_{ik}}\). So the open subsets \(U_{ij}\cap U_{ik}\) and
\(|\varphi_{ij}|^{-1}(U_{ji}\cap U_{jk})\) of \(U_{ij}\) define the same subfunctor of \(h_{U_{ij}}\), and they are
equal by Step 0. Step 6 then gives \(\varphi_{jk}\circ\varphi_{ij}=\varphi_{ik}\) on
\((X_i)_{U_{ij}\cap U_{ik}}\).

Let \(X\) and \(\psi_i\colon X_i\to X\) be as in (G4). The family \((h_{\psi_i}\colon X_i\to h_X)\) is jointly
surjective by Step 2. We compute its fibre products. Let \(t\in X_i(A)\) and \(t'\in X_j(A)\) with
\(\psi_it=\psi_jt'\). This morphism has its image in \(|\psi_i|(|X_i|)\cap|\psi_j|(|X_j|)=|\psi_i|(U_{ij})\), so
\(t\) lies in \(h_{U_{ij}}\). Then \(\psi_j\varphi_{ij}t=\psi_it=\psi_jt'\), and \(t'=\varphi_{ij}t\) because
\(\psi_j\) is a monomorphism. Conversely \(\psi_it=\psi_j\varphi_{ij}t\) for every section \(t\) of \(h_{U_{ij}}\).
So \(X_i\times_{h_X}X_j\) and \(X_i\times_FX_j\) are the same subfunctor of \(X_i\times X_j\), namely the set of
pairs \((t,\sigma_{ij}(t))\) with \(t\) in \(h_{U_{ij}}\). By Lemma 3.4, applied to \(F\) and to \(h_X\), for every
sheaf \(G\) the sets \(\mathrm{Hom}(F,G)\) and \(\mathrm{Hom}(h_X,G)\) are both in bijection with the same set of
families \((v_i\colon X_i\to G)\), naturally in \(G\). By the Yoneda lemma there is an isomorphism \(h_X\cong F\)
that carries \(h_{\psi_i}\) to \(u_i\).

Step 8 (Zariski open immersions come from open immersions). Let \(j\colon Y\to X\) be a morphism of \(\mathcal G\)
such that \(h_j\) is a Zariski open immersion. Then \(h_j\) is a monomorphism, and \(j\) is a monomorphism because
\(h\) is faithful. Let \(V\) be an affine open of \(X\) and \(V'=|j|^{-1}(V)\). By Step 0 and Step 3,
\(h_{Y_{V'}}=h_Y\times_{h_X}h_{X_V}\) maps isomorphically onto \(h_{X_{W}}\) for an open subset
\(W=W(V)\subseteq V\). By Step 6 the restriction of \(j\) is an isomorphism
\(\theta_V\colon Y_{V'}\to X_{W(V)}\) over \(X\). Let
\(\Omega\) be the union of the sets \(W(V)\). Every point of \(|Y|\) lies in some \(V'\), so
\(|j|(|Y|)\subseteq\Omega\) and \(j=j_\Omega\circ j'\) with \(j'\colon Y\to X_\Omega\). Let
\(g_V\colon X_{W(V)}\to Y\) be the composite of \(\theta_V^{-1}\) and \(Y_{V'}\to Y\). Then \(j\circ g_V\) is the
inclusion \(X_{W(V)}\to X\). Since \(j\) is a monomorphism, two morphisms \(g_{V_1}\) and \(g_{V_2}\) agree on
\(X_{W(V_1)\cap W(V_2)}\). By (G3) they glue to \(g\colon X_\Omega\to Y\) with \(j\circ g=j_\Omega\). Then
\(j_\Omega j'g=j_\Omega\) gives \(j'g=\mathrm{id}\), and \(jgj'=j_\Omega j'=j\) gives \(gj'=\mathrm{id}\). So \(j'\)
is an isomorphism and \(j\) is an open immersion. With Step 4 this proves (d). Steps 1, 5, 6 and 7 prove (a) and
(b). \(\square\)

**Corollary 4.3.** Assume that \(\mathcal C\) has a geometric model. Let \(f\colon A\to B\) be a morphism of
\(\mathrm{Comm}(\mathcal C)\). Then \(\operatorname{Spec}B\to\operatorname{Spec}A\) is a Zariski open immersion of
sheaves in the sense of Definition 3.5 if and only if \(f\) is a Zariski open immersion in the sense of
Definition 3.1.

*Proof.* One direction is Proposition 3.7(a). For the other, Theorem 4.2(d) shows that
\(\operatorname{Spec}B\to\operatorname{Spec}A\) is an open immersion of \(\mathcal G\), and (G5) shows that \(f\) is
a Zariski open immersion in the sense of Definition 3.1. \(\square\)

## 5. Abelian groups: ordinary schemes

In this section \(\mathcal C=\mathrm{Ab}\). So \(\mathrm{Comm}(\mathcal C)\) is the category of rings, and
\(\mathrm{Aff}_{\mathcal C}\) is equivalent to the category of affine schemes [Stacks, Tag [01I2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-category-affine-schemes)].

**Proposition 5.1 (dictionary).** Let \(\varphi\colon A\to B\) be a ring homomorphism.

(a) \(\varphi\) is flat in the sense of Definition 2.1 if and only if \(B\) is a flat \(A\)-module.

(b) \(\varphi\) is an epimorphism of rings if and only if \(\operatorname{Spec}B\to\operatorname{Spec}A\) is a
monomorphism of schemes.

(c) \(\varphi\) is of finite presentation in the sense of Definition 3.1 if and only if \(B\) is an \(A\)-algebra of
finite presentation, that is, \(B\cong A[x_1,\dots,x_n]/(g_1,\dots,g_m)\).

(d) \(\varphi\) is a Zariski open immersion in the sense of Definition 3.1 if and only if
\(\operatorname{Spec}B\to\operatorname{Spec}A\) is an open immersion of schemes.

(e) A family \((A\to A_i)_{i\in I}\) of Zariski open immersions is a Zariski cover if and only if the open subsets
\(\operatorname{Spec}A_i\) cover \(\operatorname{Spec}A\).

*Proof.* (a) is Example 2.2(a).

(b) A morphism is a monomorphism if and only if its diagonal is an isomorphism [Stacks, Tag [08LR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-mono-epi)]. The fibre
product of \(\operatorname{Spec}B\) with itself over \(\operatorname{Spec}A\) is
\(\operatorname{Spec}(B\otimes_AB)\) [Stacks, Tag [01I4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-affine-schemes)], and the diagonal is given by the multiplication
\(B\otimes_AB\to B\). Now use Proposition 1.9.

(c) is [Stacks, Tag [00QO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-finite-presentation)].

(d) Let \(\varphi\) be flat, an epimorphism and of finite presentation. Then the morphism
\(f\colon\operatorname{Spec}B\to\operatorname{Spec}A\) is flat [Stacks, Tag [01U5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-characterize)], a monomorphism by (b), and
locally of finite presentation by (c) and [Stacks, Tag [01TQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-presentation-characterize)]. We show that such a morphism is an open immersion.
A flat morphism that is locally of finite presentation is open [Stacks, Tag [01UA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fppf-open)]. So the image \(V\) of \(f\) is
open. A monomorphism of schemes is injective on points. Indeed, let two points \(y_1,y_2\) have the same image
\(x\), and choose a field \(K\) that contains the residue fields of \(y_1\) and \(y_2\) as extensions of the
residue field of \(x\). The two resulting morphisms \(\operatorname{Spec}K\to\operatorname{Spec}B\) have the same
composite with \(f\), so they are equal, and \(y_1=y_2\). Hence \(f\) is a homeomorphism from
\(\operatorname{Spec}B\) onto \(V\). As a morphism to the open subscheme \(V\), it is a flat, surjective and
quasi-compact monomorphism, and such a morphism is an isomorphism [Stacks, Tag [06NC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-flat-surjective-quasi-compact-monomorphism-isomorphism)]. So \(f\) is an open
immersion; compare [Stacks, Tag [025G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-etale-radicial-open)]. Conversely let \(\operatorname{Spec}B\to\operatorname{Spec}A\)
be an open immersion. Its maps on local rings are isomorphisms, so it is flat, and \(\varphi\) is flat by
[Stacks, Tag [01U5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-characterize)]. It is a monomorphism [Stacks, Tag [01L7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-immersions-monomorphisms)], so \(\varphi\) is an epimorphism by (b). It is locally
of finite presentation [Stacks, Tag [01TT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-open-immersion-locally-finite-presentation)], so \(\varphi\) is of finite presentation by [Stacks, Tag [01TQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-presentation-characterize)] and (c).

(e) Let \(U_i\subseteq\operatorname{Spec}A\) be the image of \(\operatorname{Spec}A_i\); it is open by (d). Assume
that the \(U_i\) cover \(\operatorname{Spec}A\). Since \(\operatorname{Spec}A\) is quasi-compact
[Stacks, Tag [00E8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-compact)], there is a finite set \(J\subseteq I\) such that the \(U_j\), \(j\in J\), cover. Let
\(u\colon M\to N\) be a homomorphism of \(A\)-modules such that every \(u\otimes_AA_j\), \(j\in J\), is an
isomorphism. Let
\(\mathfrak p\) be a prime ideal of \(A\). Choose \(j\in J\) and a prime ideal \(\mathfrak q\) of \(A_j\) over
\(\mathfrak p\). Since \(\operatorname{Spec}A_j\to\operatorname{Spec}A\) is an open immersion,
\(A_{\mathfrak p}\to(A_j)_{\mathfrak q}\) is an isomorphism. So the localization \(u_{\mathfrak p}\) is identified
with the localization of \(u\otimes_AA_j\) at \(\mathfrak q\), and it is an isomorphism. Hence \(u\) is an
isomorphism [Stacks, Tag [00HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-zero-local)], and the family is a Zariski cover.

Conversely let \(J\subseteq I\) be a finite subset such that the \(U_j\), \(j\in J\), do not cover, and let
\(\mathfrak p\) be a prime ideal outside their union, with residue field \(\kappa\). Then
\(\kappa\otimes_AA_j=0\) for every \(j\in J\) [Stacks, Tag [00E7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-in-image)]. So the homomorphism \(\kappa\to0\) becomes an
isomorphism after base change to every \(A_j\), \(j\in J\), and it is not an isomorphism. Hence the functors
\(-\otimes_AA_j\), \(j\in J\), are not jointly conservative. So if the family is a Zariski cover, then the \(U_i\)
cover \(\operatorname{Spec}A\). \(\square\)

**Example 5.2 (the three conditions are independent).** The homomorphism \(\mathbb Z\to\mathbb Q\) is flat and an
epimorphism, as a localization. It is not of finite presentation: otherwise
\(\operatorname{Spec}\mathbb Q\to\operatorname{Spec}\mathbb Z\) would be an open immersion by Proposition 5.1(d),
but its image is the generic point, and a non-empty open subset of \(\operatorname{Spec}\mathbb Z\) contains all
but finitely many of the infinitely many prime numbers. The homomorphism \(\mathbb Z\to\mathbb Z/2\) is an
epimorphism of finite presentation. It is not flat, because tensoring with \(\mathbb Z/2\) does not preserve the
kernel of the multiplication by \(2\) on \(\mathbb Z\). The homomorphism \(\mathbb Z\to\mathbb Z[x]\) is flat and
of finite presentation. It is not an epimorphism: the homomorphisms \(\mathbb Z[x]\to\mathbb Z\) with
\(x\mapsto0\) and \(x\mapsto1\) agree on \(\mathbb Z\).

**Theorem 5.3 (relative schemes over abelian groups).** The category of schemes, with the functor that sends a
scheme to its underlying topological space and with the functor \(\operatorname{Spec}\), is a geometric model for
\(\mathrm{Ab}\). Consequently:

(a) for every scheme \(X\) the functor \(h_X\colon A\mapsto\mathrm{Hom}(\operatorname{Spec}A,X)\) on rings is a
scheme relative to \(\mathrm{Ab}\);

(b) \(X\mapsto h_X\) is an equivalence from the category of schemes to \(\mathrm{Sch}(\mathrm{Ab})\);

(c) a morphism of schemes is an open immersion if and only if the induced morphism of sheaves is a Zariski open
immersion, and the Zariski opens of \(\operatorname{Spec}A\) are the functors of points of the open subschemes of
\(\operatorname{Spec}A\).

*Proof.* The functor \(\operatorname{Spec}\) is fully faithful [Stacks, Tag [01I2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-category-affine-schemes)]. (G1): an open subset \(V\) of a
scheme \(X\), with the restricted structure sheaf, is a scheme [Stacks, Tag [01IK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-open-subspace-scheme)], and a morphism of locally ringed
spaces \(T\to X\) whose image lies in \(V\) factors uniquely through \(V\), by the definition of such morphisms.
(G2): the affine opens form a basis [Stacks, Tag [01IT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-basis-affine-opens)]. (G3) and (G4): morphisms and schemes can be glued
[Stacks, Tags [01JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue) and [01JC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue-schemes)]. (G5) is Proposition 5.1(d) and (e). Now apply Theorem 4.2. \(\square\)

*Reference:* [Toën–Vaquié 2009, Section 3.1] states (b) without proof. [Vezzani 2012, Introduction] discusses the
comparison between schemes as ringed spaces and schemes as functors, crediting Demazure and Gabriel for the historical formulation. The representability criterion behind
(b), that a Zariski sheaf covered by open representable subfunctors is representable, is
[Stacks, Tag [01JJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue-functors)].

## 6. Sets and pointed sets: schemes over \(\mathbb F_1\)

Until Proposition 6.11 we take \(\mathcal C=\mathrm{Set}\). So \(\mathrm{Comm}(\mathcal C)=\mathrm{Mon}\) is the
category of plain monoids (Example 1.4), and the modules over a plain monoid \(M\) are the \(M\)-sets.
[Toën–Vaquié 2009, Définition 3.5] calls the schemes relative to \(\mathrm{Set}\) the \(\mathbb F_1\)-schemes.

### The algebra of \(M\)-sets

We fix notation. \(M^\times\) is the group of units of \(M\). A morphism \(\varphi\colon M\to N\) is *local* if
\(\varphi^{-1}(N^\times)=M^\times\). A subset \(S\subseteq M\) is *multiplicative* if \(1\in S\) and
\(SS\subseteq S\). The *localization* \(S^{-1}M\) is the set of fractions \(m/s\) with \(m\in M\), \(s\in S\), where
\(m/s=m'/s'\) if and only if \(s''s'm=s''sm'\) for some \(s''\in S\); its product is \((m/s)(m'/s')=mm'/ss'\). The
morphism \(\lambda\colon M\to S^{-1}M\), \(m\mapsto m/1\), has the following universal property: a morphism
\(\varphi\colon M\to P\) factors through \(\lambda\) if and only if \(\varphi(S)\subseteq P^\times\), and the
factorization is then unique [Deitmar 2005, Lemma 1.2]. For \(a\in M\) we write \(M_a\) for the localization at
\(S=\{1,a,a^2,\dots\}\). For an \(M\)-set \(T\), the set \(S^{-1}T\) consists of the fractions \(t/s\) with
\(t\in T\), \(s\in S\), where \(t/s=t'/s'\) if and only if \(s''s't=s''st'\) for some \(s''\in S\). It is an
\(S^{-1}M\)-set by \((m/s)(t/s')=mt/ss'\).

By Proposition 1.5, limits and colimits of \(M\)-sets are computed on the underlying sets. The terminal \(M\)-set is
a set with one element, written \(\{\ast\}\). For a morphism \(\varphi\colon M\to N\) and an \(M\)-set \(T\),
Definition 1.6 says that \(N\otimes_MT\) is the quotient of \(N\times T\) by the equivalence relation generated by
\((n\varphi(m),t)\sim(n,mt)\).

**Lemma 6.1.** Let \(S\subseteq M\) be multiplicative and \(T\) an \(M\)-set. The map
\[
S^{-1}M\otimes_MT\longrightarrow S^{-1}T,\qquad(m/s)\otimes t\mapsto mt/s,
\]
is an isomorphism of \(S^{-1}M\)-sets, natural in \(T\).

*Proof.* The map \((m/s,t)\mapsto mt/s\) is well defined on \(S^{-1}M\times T\): if \(s''s'm=s''sm'\), then
\(s''s'mt=s''sm't\). It sends \(((m/s)m_0,t)\) and \((m/s,m_0t)\) to the same element. So it induces a map
\(\alpha\) on \(S^{-1}M\otimes_MT\). Define \(\beta\colon S^{-1}T\to S^{-1}M\otimes_MT\) by
\(\beta(t/s)=(1/s)\otimes t\). It is well defined: if \(s''s't=s''st'\), then
\[
\frac1s\otimes t=\frac{s''s'}{s''s's}\otimes t=\frac1{s''s's}\otimes s''s't=\frac1{s''s's}\otimes s''st'
=\frac{s''s}{s''s's}\otimes t'=\frac1{s'}\otimes t' .
\]
We have \(\alpha\beta(t/s)=t/s\) and \(\beta\alpha((m/s)\otimes t)=(1/s)\otimes mt=(m/s)\otimes t\). Both maps are
compatible with the actions of \(S^{-1}M\). \(\square\)

**Proposition 6.2 (localizations).** Let \(S\subseteq M\) be multiplicative and \(a\in M\).

(a) \(\lambda\colon M\to S^{-1}M\) is a flat epimorphism.

(b) \(M\to M_a\) is of finite presentation. So it is a Zariski open immersion.

(c) Order \(S\) by divisibility: \(a\le b\) if \(b=ac\) for some \(c\in M\). Then \((M_a)_{a\in S}\) is a directed
system of \(M\)-algebras, and its colimit in \(\mathrm{Alg}_M\) is \(S^{-1}M\).

*Proof.* (a) By the universal property, two morphisms out of \(S^{-1}M\) that agree on \(M\) are equal. So
\(\lambda\) is an epimorphism. By Lemma 6.1 it remains to show that \(T\mapsto S^{-1}T\) preserves finite limits. It
is enough to treat the terminal object, products of two factors and equalizers [Stacks, Tag [0035](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-left-exact)]. Clearly
\(S^{-1}\{\ast\}=\{\ast\}\). The map \(S^{-1}(T\times T')\to S^{-1}T\times S^{-1}T'\),
\((t,t')/s\mapsto(t/s,t'/s)\), is surjective, because \((t/s,t'/s')\) is the image of \((s't,st')/ss'\). It is
injective: if \(t/s=u/r\) and \(t'/s=u'/r\), choose \(s_1,s_2\in S\) with \(s_1rt=s_1su\) and
\(s_2rt'=s_2su'\); then \(s_1s_2r(t,t')=s_1s_2s(u,u')\). Let \(E\subseteq T\) be the equalizer of two morphisms
\(\varphi,\psi\colon T\to T'\). The map \(S^{-1}E\to S^{-1}T\) is injective, and its image lies in the equalizer of
\(S^{-1}\varphi\) and \(S^{-1}\psi\). If \(t/s\) lies in that equalizer, then \(\varphi(t)/s=\psi(t)/s\), so
\(s'\varphi(t)=s'\psi(t)\) for some \(s'\in S\). Then \(s't\in E\) and \(t/s=s't/s's\).

(b) By (a), \(M\to M_a\) is a flat epimorphism, so we check (FP). Let \((D_\alpha)\) be a directed system of
\(M\)-algebras with colimit \(D\). By Proposition 1.8(a), \(D\) is the colimit of the underlying sets. A morphism of
\(M\)-algebras \(M_a\to D\) exists if and only if the image of \(a\) in \(D\) is a unit. Assume this, and let
\(y\in D\) with \(ay=1\). Then \(y\) is the image of some \(y_\alpha\in D_\alpha\), and the equation \(ay_\alpha=1\) holds
in \(D\), hence in \(D_\beta\) for some \(\beta\ge\alpha\). So the image of \(a\) in \(D_\beta\) is a unit, and
there is a morphism of \(M\)-algebras \(M_a\to D_\beta\).

(c) The set \(S\) is directed, because \(a\le ab\) and \(b\le ab\). If \(a\le b\), then \(a\) is a unit in \(M_b\),
so there is exactly one morphism of \(M\)-algebras \(M_a\to M_b\). An \(M\)-algebra \(P\) admits morphisms of
\(M\)-algebras from all \(M_a\), \(a\in S\), if and only if the elements of \(S\) are units in \(P\), that is, if
and only if it admits one from \(S^{-1}M\). All these morphisms are unique. So \(S^{-1}M\) is the colimit.
\(\square\)

*Reference:* [Vezzani 2012, Corollary 26 and Proposition 27].

**Lemma 6.3.** Let \(\varphi\colon M\to N\) be a local epimorphism of plain monoids. Then
\(\varphi(M^\times)=N^\times\).

*Proof.* Let \(H=N^\times/\varphi(M^\times)\) and let \(H_0=H\sqcup\{0\}\) be the plain monoid in which \(0\) is
absorbing. Define \(u,v\colon N\to H_0\) as follows. Both send the non-units of \(N\) to \(0\). On a unit \(n\), \(u\)
takes the class of \(n\) in \(H\) as its value, and \(v\) takes the value \(1\). A product in \(N\) is a unit if
and only if both factors are units. So \(u\) and \(v\) are morphisms. They agree on \(\varphi(M)\): an element of
\(\varphi(M^\times)\) has trivial class, and an element \(\varphi(m)\) with \(m\notin M^\times\) is a non-unit,
because \(\varphi\) is local. Since \(\varphi\) is an epimorphism, \(u=v\). So every unit of \(N\) has trivial
class in \(H\). \(\square\)

**Proposition 6.4.** Let \(\varphi\colon M\to N\) be a morphism of plain monoids.

(a) If \(\varphi\) is local and flat, then \(\varphi\) is injective.

(b) If \(\varphi\) is a local flat epimorphism, then \(\varphi\) is an isomorphism.

*Proof.* (a) Let \(a,b\in M\) with \(\varphi(a)=\varphi(b)\). Multiplication by \(a\) and multiplication by \(b\)
are two morphisms of \(M\)-sets \(M\to M\). Their equalizer is \(E=\{x\in M\mid ax=bx\}\). After base change to
\(N\) both become multiplication by \(\varphi(a)\) on \(N\otimes_MM=N\), so their equalizer is \(N\). Since
\(\varphi\) is flat, the map \(N\otimes_ME\to N\), \(n\otimes x\mapsto n\varphi(x)\), is bijective. So
\(n\varphi(x)=1\) for some \(n\in N\) and \(x\in E\). Then \(\varphi(x)\) is a unit, so \(x\) is a unit, because
\(\varphi\) is local. From \(ax=bx\) we get \(a=b\).

(b) By (a) we may regard \(M\) as a submonoid of \(N\). By Lemma 6.3, \(N^\times=M^\times\). By Proposition 1.9 the
map \(N\otimes_MN\to N\), \(n\otimes n'\mapsto nn'\), is bijective, and so is its right inverse
\(n\mapsto n\otimes1\). Let \(Q\) be the quotient of \(N\) by the equivalence relation that identifies all
elements of \(M\) with each other. The relation is stable under the action of \(M\), so \(Q\) is an \(M\)-set and
\(\pi\colon N\to Q\) is a morphism of \(M\)-sets. The \(M\)-set \(Q\) is the pushout of
\(\{\ast\}\leftarrow M\to N\) in \(\mathrm{Mod}_M\). The functor \(N\otimes_M-\) preserves pushouts, and it
preserves the terminal object because \(\varphi\) is flat. So
\(N\otimes_MQ\) is the pushout of \(\{\ast\}\leftarrow N\to N\otimes_MN\), where the second map is the bijection
\(n\mapsto n\otimes1\). Hence \(N\otimes_MQ=\{\ast\}\).

Let \(K=\{(x,y)\in N\times N\mid\pi(x)=\pi(y)\}\) be the kernel pair of \(\pi\). A pair \((x,y)\) lies in \(K\) if
and only if \(x=y\) or \(x,y\in M\). Since \(\varphi\) is flat, \(N\otimes_MK\) is the kernel pair of
\(N\otimes_MN\to N\otimes_MQ=\{\ast\}\), which is \((N\otimes_MN)\times(N\otimes_MN)\). So the map
\[
N\otimes_MK\longrightarrow N\times N,\qquad n\otimes(x,y)\mapsto(nx,ny),
\]
is bijective. Let \(z\in N\). There are \(n\in N\) and \((x,y)\in K\) with \(nx=1\) and \(ny=z\). Then \(n\) and
\(x\) are units of \(N\), so they lie in \(M\). Since \((x,y)\in K\) and \(x\in M\), also \(y\in M\). So
\(z=ny\in M\). Hence \(M=N\). \(\square\)

*Reference:* [Vezzani 2012, Lemma 28 and Proposition 29].

**Theorem 6.5 (flat epimorphisms and Zariski open immersions of plain monoids).** Let \(\varphi\colon M\to N\) be a
morphism of plain monoids.

(a) \(\varphi\) is a flat epimorphism if and only if \(N\) is isomorphic, as an \(M\)-algebra, to \(S^{-1}M\) for a
multiplicative subset \(S\subseteq M\). One can take \(S=\varphi^{-1}(N^\times)\).

(b) \(\varphi\) is a Zariski open immersion if and only if \(N\) is isomorphic, as an \(M\)-algebra, to \(M_a\) for
some \(a\in M\).

*Proof.* (a) Localizations are flat epimorphisms by Proposition 6.2. Conversely let \(\varphi\) be a flat
epimorphism and \(S=\varphi^{-1}(N^\times)\), a multiplicative subset. By the universal property,
\(\varphi=\psi\lambda\) with \(\psi\colon S^{-1}M\to N\). The morphism \(\psi\) is local: if \(\psi(m/s)\) is a
unit, then \(\varphi(m)=\psi(m/s)\varphi(s)\) is a unit, so \(m\in S\) and \(m/s\) is a unit. It is an
epimorphism, because \(\psi\lambda\) is one. It is flat by Lemma 2.3(c), because \(\lambda\) is an epimorphism. By
Proposition 6.4(b), \(\psi\) is an isomorphism.

(b) The morphisms \(M\to M_a\) are Zariski open immersions by Proposition 6.2. Conversely let \(\varphi\) be a
Zariski open immersion. By (a) we may assume \(N=S^{-1}M\). By Proposition 6.2(c) and (FP) there is a morphism of
\(M\)-algebras \(N\to M_a\) for some \(a\in S\). There is also a morphism of \(M\)-algebras \(M_a\to N\), because
\(a\) is a unit in \(N\). The composites \(N\to M_a\to N\) and \(M_a\to N\to M_a\) are morphisms of \(M\)-algebras,
and \(M\to N\) and \(M\to M_a\) are epimorphisms. So both composites are identities. \(\square\)

*Reference:* [Vezzani 2012, Theorem 30] for (b). Part (a) is contained in the proof given there.

**Proposition 6.6 (covers are trivial).**

(a) A family \((M\to M_{a_i})_{i\in I}\) is a Zariski cover if and only if some \(a_i\) is a unit of \(M\). So a
family of Zariski open immersions with source \(M\) is a Zariski cover if and only if one of its members is an
isomorphism.

(b) Every presheaf on \(\mathrm{Aff}_{\mathrm{Set}}\) is a sheaf. So
\(\mathrm{Sh}(\mathrm{Aff}_{\mathrm{Set}})\) is the category of all functors \(\mathrm{Mon}\to\mathrm{Set}\), and
a family of morphisms \((F_i\to G)\) is jointly surjective if and only if the maps \(F_i(N)\to G(N)\) are jointly
surjective for every plain monoid \(N\).

*Proof.* (a) If \(a_i\) is a unit, then \(M\to M_{a_i}\) is an isomorphism, and its base change functor is
conservative. Conversely assume that no \(a_i\) is a unit, and let \(J\subseteq I\) be finite. If \(J=\emptyset\),
the functors indexed by \(J\) are not jointly conservative, because the map from the empty \(M\)-set to
\(\{\ast\}\) is not bijective. Let \(J\neq\emptyset\). Then \(\mathfrak m=M\setminus M^\times\) is not empty. It
satisfies \(M\mathfrak m\subseteq\mathfrak m\). Let \(Q\) be the \(M\)-set obtained from \(M\) by identifying all
elements of \(\mathfrak m\) with one point \(q\). It has at least two elements, \(q\) and the class of \(1\). Let
\(a=a_j\) with \(j\in J\). For every \(x\in Q\) we have \(ax=q\), so \(x/a^k=ax/a^{k+1}=q/a^{k+1}\), and
\(q/a^{k+1}=q/1\) because \(a^{k+1}q=q\). So \(Q_a\) has one element, and by Lemma 6.1 the map \(Q\to\{\ast\}\)
becomes bijective after base change to every \(M_{a_j}\), \(j\in J\). It is not bijective. So the functors indexed
by \(J\) are not jointly conservative. The last statement of (a) follows with Theorem 6.5(b).

(b) Let \(F\) be a presheaf and \((f_i\colon M\to M_i)_{i\in I}\) a Zariski cover. By (a) some \(f_{i_0}\) is an
isomorphism. Let \((x_i)\) be a family of sections \(x_i\in F(M_i)\) such that \(x_i\) and \(x_j\) have the same
image in \(F(M_i\otimes_MM_j)\) for all \(i,j\). Let \(x\in F(M)\) be the section with \(x|_{M_{i_0}}=x_{i_0}\). The
morphism \(M_i\to M_i\otimes_MM_{i_0}\) is an isomorphism, and \(x|_{M_i}\) and \(x_i\) have the same image under
it: both images equal the image of \(x_{i_0}\). So \(x|_{M_i}=x_i\) for all \(i\). The section \(x\) is unique,
because \(F(M)\to F(M_{i_0})\) is bijective. For the last statement, a section that is locally in the image is in
the image, because a Zariski cover contains an isomorphism. \(\square\)

*Reference:* [Vezzani 2012, Theorem 32].

**Example 6.7 (nothing is flat over \(\mathbb F_1\)).** Let \(N\) be a plain monoid and \(\varphi\colon\{1\}\to N\)
the unique morphism. Modules over \(\{1\}\) are sets, and \(\varphi^{\ast}T=N\times T\). If \(\varphi\) is flat,
then \(\varphi^{\ast}\) preserves the terminal object, so \(N=N\times\{\ast\}\) has one element. Hence
\(\{1\}\to N\) is flat only for \(N=\{1\}\). Over a field every algebra is flat; over \(\mathbb F_1\) none is,
except \(\mathbb F_1\). Exercise 2 treats monoids with zero.

**Example 6.8 (the Zariski opens of \(\operatorname{Spec}M\)).** By Theorem 6.5(b) and Proposition 6.6(b), the
Zariski opens of \(\operatorname{Spec}M\) are the functors \(U_I\), \(I\subseteq M\) a subset, with
\[
U_I(P)=\{\varphi\colon M\to P\mid\varphi(a)\in P^\times\ \text{for some}\ a\in I\}.
\]
For \(I=\{a\}\) this is \(\operatorname{Spec}M_a\). For \(I=\emptyset\) it is the empty functor. Let
\(M=\langle x,y\rangle\) be the free plain monoid on two generators. Then
\(\operatorname{Spec}M\) is the functor \(P\mapsto P\times P\), and \(U_{\{x,y\}}(P)\) is the set of pairs in which
at least one entry is a unit. Exercise 3 shows that \(U_{\{x,y\}}\) is not affine.

### The comparison with monoid schemes

**Recollection 6.9 (plain monoid schemes).** We recall the monoid schemes of [Deitmar 2005], which are built from
plain monoids. [Deitmar 2005] calls them schemes over \(\mathbb F_1\); we call them *plain monoid schemes*. The
definitions are those of the lessons *Commutative monoids and their spectra* and *Monoid schemes*, with plain
monoids in place of monoids.

An *ideal* of a plain monoid \(M\) is a subset \(\mathfrak a\) with \(\mathfrak aM\subseteq\mathfrak a\); the empty
set is an ideal. An ideal \(\mathfrak p\neq M\) is *prime* if \(M\setminus\mathfrak p\) is closed under
multiplication. The space \(\operatorname{Spec}M\) is the set of prime ideals, with the topology that has the sets
\(D(a)=\{\mathfrak p\mid a\notin\mathfrak p\}\), \(a\in M\), as a basis. The set \(\mathfrak m=M\setminus M^\times\)
is a prime ideal, and it contains every prime ideal. It lies in \(D(a)\) only if \(a\) is a unit, and then
\(D(a)=\operatorname{Spec}M\). So \(\operatorname{Spec}M\) is the only open subset of \(\operatorname{Spec}M\) that
contains \(\mathfrak m\) [Deitmar 2005, Section 1.2]. The space \(\operatorname{Spec}M\) carries a sheaf of plain
monoids with global sections \(M\) [Deitmar 2005, Proposition 2.1]. A *monoidal space* is a topological space with a
sheaf of plain monoids. A morphism of monoidal spaces is a continuous map \(f\) with a morphism of sheaves
\(f^\#\) that induces local morphisms on all stalks. A *plain monoid scheme* is a monoidal space in which every
point has an open neighbourhood isomorphic to \(\operatorname{Spec}M\) for some plain monoid \(M\). We use the
following facts.

(M1) The functor \(M\mapsto\operatorname{Spec}M\) from \(\mathrm{Mon}^{\mathrm{op}}\) to plain monoid schemes is
fully faithful [Deitmar 2005, Proposition 2.2].

(M2) For \(a\in M\), the morphism \(\operatorname{Spec}M_a\to\operatorname{Spec}M\) induced by \(M\to M_a\) is an
isomorphism onto the open subspace \(D(a)\) with the restricted sheaf [Deitmar 2005, Lemma 2.3].

(M3) An open subspace of a plain monoid scheme, with the restricted sheaf, is a plain monoid scheme, by (M2). A
morphism \(T\to X\) whose image lies in an open subspace \(V\) factors through \(V\) in exactly one way. Morphisms
glue along open covers, and plain monoid schemes glue along open subspaces. The proofs are those for locally ringed
spaces [Stacks, Tag [01JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue)]; they use only sheaves on topological spaces and a condition on stalks.

**Theorem 6.10 (plain monoid schemes and \(\mathbb F_1\)-schemes).** The category of plain monoid schemes, with the
underlying space and the functor \(\operatorname{Spec}\), is a geometric model for \(\mathrm{Set}\). Consequently:

(a) for every plain monoid scheme \(X\), the functor \(h_X\colon N\mapsto\mathrm{Hom}(\operatorname{Spec}N,X)\) on
plain monoids is a scheme relative to \(\mathrm{Set}\);

(b) \(X\mapsto h_X\) is an equivalence from the category of plain monoid schemes to
\(\mathrm{Sch}(\mathrm{Set})\);

(c) a morphism \(j\) of plain monoid schemes is an open immersion if and only if \(h_j\) is a Zariski open
immersion, and the Zariski opens of \(\operatorname{Spec}M\) correspond to the open subsets of the space
\(\operatorname{Spec}M\): the open set \(\bigcup_{a\in I}D(a)\) corresponds to the functor \(U_I\) of Example 6.8;

(d) a family of open immersions \((X_i\to X)\) is jointly surjective on the underlying spaces if and only if the
family \((h_{X_i}\to h_X)\) is jointly surjective.

*Proof.* (G1), (G3) and (G4) are (M3), and \(\operatorname{Spec}\) is fully faithful by (M1). (G2): a plain monoid
scheme is covered by open subspaces of the form \(\operatorname{Spec}M\), in these the sets \(D(a)\) form a basis,
and the open subspaces \(D(a)\) are affine by (M2).

(G5), first part. If \(M\to N\) is a Zariski open immersion, then \(N\cong M_a\) over \(M\) by Theorem 6.5(b), and
\(\operatorname{Spec}N\to\operatorname{Spec}M\) is an open immersion by (M2). Conversely let
\(\operatorname{Spec}N\to\operatorname{Spec}M\) be an isomorphism onto an open subspace \(V\). Let \(z\in V\) be
the image of the point \(N\setminus N^\times\). Then \(V\) is the only open subset of \(V\) that contains \(z\).
Choose \(a\in M\) with \(z\in D(a)\subseteq V\). Then \(D(a)=V\). By (M2) and (M1), \(N\cong M_a\) as
\(M\)-algebras, and \(M\to N\) is a Zariski open immersion by Proposition 6.2.

(G5), second part. By Proposition 6.6(a), a family \((M\to M_{a_i})\) is a Zariski cover if and only if some
\(a_i\) is a unit. This holds if and only if some \(D(a_i)\) contains \(\mathfrak m=M\setminus M^\times\), that is,
if and only if the sets \(D(a_i)\) cover \(\operatorname{Spec}M\).

Now Theorem 4.2 gives (a), (b) and (c); the last statement of (c) follows from Step 2 of its proof and
Proposition 6.6(b). For (d), one direction is Step 2 of the proof of Theorem 4.2. For the other, let the family
\((h_{X_i}\to h_X)\) be jointly surjective and let \(x\) be a point of \(X\). Choose an open neighbourhood of
\(x\) isomorphic to \(\operatorname{Spec}N\), and let \(\mathfrak p\subseteq N\) be the prime ideal corresponding
to \(x\). Let \(N_{\mathfrak p}\) be the localization of \(N\) at \(N\setminus\mathfrak p\). An element \(n/1\) of
\(N_{\mathfrak p}\) is a unit if and only if \(n\) divides an element of \(N\setminus\mathfrak p\), that is, if and
only if \(n\notin\mathfrak p\). So the morphism
\(t\colon\operatorname{Spec}N_{\mathfrak p}\to\operatorname{Spec}N\to X\) sends the point
\(N_{\mathfrak p}\setminus N_{\mathfrak p}^\times\) to \(x\). By Proposition 6.6(b), \(t\) factors through some
\(X_i\to X\). So \(x\) lies in the image of \(X_i\). \(\square\)

*Reference:* [Vezzani 2012, Theorem 36] for (b), and [Vezzani 2012, Proposition 37] for (c) and (d).

So an \(\mathbb F_1\)-scheme in the sense of [Toën–Vaquié 2009] and a scheme over \(\mathbb F_1\) in the sense of
[Deitmar 2005] are the same thing. The theorem also describes the functors \(\mathrm{Mon}\to\mathrm{Set}\) that
come from plain monoid schemes: they are the functors with a jointly surjective family of Zariski open immersions
from representable functors, and by Proposition 6.6(b) no sheaf condition has to be checked.

### Monoids with zero

Now let \(\mathcal C=\mathrm{Set}_{\ast}\). So \(\mathrm{Comm}(\mathcal C)=\mathrm{Mon}_0\) is the category of
monoids of this course, and the modules over a monoid \(M\) are the pointed \(M\)-sets (Example 1.4). Units, local
morphisms, multiplicative subsets and the localizations \(S^{-1}M\) and \(S^{-1}T\) are defined as before; the base
point of \(S^{-1}T\) is \(\ast/1\). If \(0\in S\), then \(S^{-1}M\) is the zero monoid and \(S^{-1}T=\{\ast\}\).
Finite limits of pointed \(M\)-sets are computed on the underlying sets. The one-point set \(\{\ast\}\) is both the
terminal and the initial pointed \(M\)-set. For \(\varphi\colon M\to N\) and a pointed \(M\)-set \(T\), the pointed
\(N\)-set \(N\otimes_MT\) is the quotient of \(N\times T\) by the equivalence relation generated by
\((n\varphi(m),t)\sim(n,mt)\) and by \((n,\ast)\sim(0,t)\) for all \(n,t\).

**Proposition 6.11.** For monoids with zero and pointed \(M\)-sets, the statements of Lemma 6.1, Proposition 6.2,
Lemma 6.3, Proposition 6.4 and Theorem 6.5 hold. Proposition 6.6 takes the following form.

(a) A family \((M\to M_{a_i})_{i\in I}\) is a Zariski cover if and only if \(M=0\) or some \(a_i\) is a unit of
\(M\). In particular the empty family is a Zariski cover of \(\operatorname{Spec}M\) if and only if \(M=0\).

(b) A presheaf \(F\) on \(\mathrm{Aff}_{\mathrm{Set}_{\ast}}\) is a sheaf if and only if \(F(0)\) has exactly one
element. A family of morphisms of sheaves \((F_i\to G)\) is jointly surjective if and only if the maps
\(F_i(N)\to G(N)\) are jointly surjective for every monoid \(N\neq0\).

*Proof.* We go through the proofs and note what changes.

Lemma 6.1: the maps \(\alpha\) and \(\beta\) send base points to base points, and \(\alpha\) is compatible with the
additional relation \((n,\ast)\sim(0,t)\). Proposition 6.2: the proof is unchanged; directed colimits of monoids
are computed on the underlying sets by Proposition 1.8(a). Lemma 6.3: if \(N=0\) the statement is clear, since
\(1=0\) is the only element of \(N\). If \(N\neq0\), then \(0\) is a non-unit of \(N\), and \(u\) and \(v\) are
morphisms of monoids to the monoid \(H_0\). Proposition 6.4: in (a) the equalizer \(E\) contains \(0\) and is a
pointed \(M\)-set. In (b) the submonoid \(M\) of \(N\) contains \(0\), so \(Q\) is the pointed \(M\)-set obtained by
collapsing \(M\) to the base point, and it is the pushout of \(\{\ast\}\leftarrow M\to N\) in pointed \(M\)-sets.
The rest is unchanged. Theorem 6.5: unchanged.

(a) If \(M=0\), then every pointed \(M\)-set \(T\) has one element, because \(t=1t=0t=\ast\). So every morphism of
\(M\)-modules is an isomorphism, and every family of Zariski open immersions with source \(M\) is a Zariski cover.
If some \(a_i\) is a unit, the family is a Zariski cover as before. Let \(M\neq0\) and let no \(a_i\) be a unit.
Then \(\mathfrak m=M\setminus M^\times\) contains \(0\), and the pointed \(M\)-set \(Q\) obtained by collapsing
\(\mathfrak m\) to the base point has at least two elements, the base point and the class of \(1\). As in the proof
of Proposition 6.6, \(Q_{a_i}=\{\ast\}\) for all \(i\), and the map \(Q\to\{\ast\}\) is not bijective. So no finite
subfamily is jointly conservative, not even the empty one.

(b) Let \(F\) be a sheaf. The empty family is a Zariski cover of \(\operatorname{Spec}0\), so \(F(0)\) has one
element. Conversely let \(F(0)\) have one element, and let \((M\to M_i)\) be a Zariski cover. If \(M\neq0\), one
member is an isomorphism and the sheaf condition holds as in Proposition 6.6(b). If \(M=0\), then every \(M_i\) is
\(0\), all sets in the sheaf condition have one element, and it holds. For the last statement, a section over
\(N\neq0\) that is locally in the image is in the image, and every section over \(0\) is locally in the image, on
the empty cover. \(\square\)

We use the following facts from *Commutative monoids and their spectra* and *Monoid schemes*. For a monoid
\(M\neq0\), the set \(\mathfrak m=M\setminus M^\times\) is the largest prime ideal, and
\(\operatorname{Spec}M\) is the only open subset of \(\operatorname{Spec}M\) that contains it; the spectrum of the
zero monoid is empty. The sets \(D(a)\) form a basis of \(\operatorname{Spec}M\). The functor
\(M\mapsto\operatorname{Spec}M\) from \(\mathrm{Mon}_0^{\mathrm{op}}\) to monoid schemes is fully faithful. The
morphism \(\operatorname{Spec}M_a\to\operatorname{Spec}M\) is an isomorphism onto the open subspace \(D(a)\). Open
subspaces of monoid schemes are monoid schemes, morphisms glue along open covers, and monoid schemes glue along
open subspaces. A morphism of monoid schemes whose image lies in an open subspace factors through that subspace in
exactly one way, by the definition of a morphism of monoidal spaces.

**Theorem 6.12 (monoid schemes and schemes relative to pointed sets).** The category of monoid schemes, with the
underlying space and the functor \(\operatorname{Spec}\), is a geometric model for \(\mathrm{Set}_{\ast}\).
Consequently:

(a) for every monoid scheme \(X\), the functor \(h_X\colon N\mapsto\mathrm{Hom}(\operatorname{Spec}N,X)\) on monoids
is a scheme relative to \(\mathrm{Set}_{\ast}\);

(b) \(X\mapsto h_X\) is an equivalence from the category of monoid schemes to
\(\mathrm{Sch}(\mathrm{Set}_{\ast})\);

(c) a morphism \(j\) of monoid schemes is an open immersion if and only if \(h_j\) is a Zariski open immersion, and
the Zariski opens of \(\operatorname{Spec}M\) correspond to the open subsets of the space \(\operatorname{Spec}M\);

(d) a family of open immersions \((X_i\to X)\) is jointly surjective on the underlying spaces if and only if the
family \((h_{X_i}\to h_X)\) is jointly surjective.

*Proof.* (G1)–(G4) and the full faithfulness of \(\operatorname{Spec}\) are the facts just listed. (G5), first
part: a Zariski open immersion \(M\to N\) has \(N\cong M_a\) by Proposition 6.11, so it gives an open immersion.
Conversely let \(\operatorname{Spec}N\to\operatorname{Spec}M\) be an isomorphism onto an open subspace \(V\). If
\(N=0\), then \(V=\emptyset=D(0)\), and \(N\) is isomorphic to the localization of \(M\) at the element \(0\), which
is the zero monoid. If \(N\neq0\), the argument of Theorem 6.10 gives \(V=D(a)\) and \(N\cong M_a\). (G5), second
part: by Proposition 6.11(a), the family \((M\to M_{a_i})\) is a Zariski cover if and only if \(M=0\) or some
\(a_i\) is a unit, that is, if and only if the sets \(D(a_i)\) cover \(\operatorname{Spec}M\). Now apply
Theorem 4.2. Statement (d) is proved as in Theorem 6.10, with Proposition 6.11(b); the monoid
\(N_{\mathfrak p}\) is not zero. \(\square\)

**Remark 6.13 (the two settings).** Let \(M\) be a plain monoid and \(M_0=M\sqcup\{0\}\) the monoid obtained by
adjoining a zero. For every monoid \(N\), restriction to \(M\) is a bijection from the set of morphisms of monoids
\(M_0\to N\) to the set of morphisms of plain monoids \(M\to N\). So the affine scheme \(\operatorname{Spec}M_0\)
relative to \(\mathrm{Set}_{\ast}\) is the restriction of the functor \(\operatorname{Spec}M\) to monoids with
zero. The extension by zero is a bijection from the prime ideals of \(M\) to those of \(M_0\), namely
\(\mathfrak p\mapsto\mathfrak p\sqcup\{0\}\).

## 7. Base change to the integers

Let \(g\colon\mathrm{Ring}\to\mathrm{Mon}\) be the functor that sends a ring \(R\) to its multiplicative monoid
\((R,\cdot)\), regarded as a plain monoid. It has a left adjoint \(M\mapsto\mathbb Z[M]\), the monoid ring: the free
abelian group on the set \(M\), with the product that extends the product of \(M\). Ring homomorphisms
\(\mathbb Z[M]\to R\) correspond to morphisms of plain monoids \(M\to g(R)\) [Deitmar 2005, Theorem 1.1]. For
\(a\in M\) there is a canonical isomorphism \(\mathbb Z[M_a]\cong\mathbb Z[M]_a\) of \(\mathbb Z[M]\)-algebras: by
the adjunction and the universal properties of the two localizations, homomorphisms from either ring to a ring
\(R\) correspond to the morphisms \(M\to g(R)\) that send \(a\) to a unit.

**Definition 7.1.** For a functor \(F\colon\mathrm{Mon}\to\mathrm{Set}\), the *base change of \(F\) to the
integers* is the sheaf
\[
F_{\mathbb Z}=(F\circ g)^{a}
\]
on \(\mathrm{Aff}_{\mathrm{Ab}}\) associated with the presheaf \(R\mapsto F(g(R))\) on rings. We write
\(c\colon F\circ g\to F_{\mathbb Z}\) for the canonical morphism.

**Theorem 7.2 (base change).**

(a) For every sheaf \(G\) on \(\mathrm{Aff}_{\mathrm{Ab}}\) there is a bijection
\(\mathrm{Hom}(F_{\mathbb Z},G)\cong\mathrm{Hom}(F,G\circ\mathbb Z[-])\), natural in \(F\) and \(G\). So
\(F\mapsto F_{\mathbb Z}\) preserves colimits. It also preserves finite limits, monomorphisms and jointly surjective
families.

(b) \((\operatorname{Spec}M)_{\mathbb Z}=\operatorname{Spec}\mathbb Z[M]\) for every plain monoid \(M\).

(c) Let \(U\subseteq\operatorname{Spec}M\) be the Zariski open that is the image of the family
\((\operatorname{Spec}M_a\to\operatorname{Spec}M)_{a\in I}\). Then
\(U_{\mathbb Z}\to\operatorname{Spec}\mathbb Z[M]\) is a monomorphism, and its image is the functor of points of
the open subscheme \(\bigcup_{a\in I}D(a)\) of \(\operatorname{Spec}\mathbb Z[M]\).

(d) If \(F'\to F\) is a Zariski open immersion of sheaves on \(\mathrm{Aff}_{\mathrm{Set}}\), then
\(F'_{\mathbb Z}\to F_{\mathbb Z}\) is a Zariski open immersion of sheaves on \(\mathrm{Aff}_{\mathrm{Ab}}\).

(e) If \(F\) is a scheme relative to \(\mathrm{Set}\) with atlas \((\operatorname{Spec}M_i\to F)_{i\in I}\), then
\(F_{\mathbb Z}\) is a scheme relative to \(\mathrm{Ab}\) with atlas
\((\operatorname{Spec}\mathbb Z[M_i]\to F_{\mathbb Z})_{i\in I}\).

So base change is a functor \(\mathrm{Sch}(\mathrm{Set})\to\mathrm{Sch}(\mathrm{Ab})\). By Theorem 5.3 we may
regard \(F_{\mathbb Z}\) as a scheme.

*Proof.* (a) By (S2), \(\mathrm{Hom}(F_{\mathbb Z},G)=\mathrm{Hom}(F\circ g,G)\), the second set being formed in
presheaves on rings. Since \(\mathbb Z[-]\) is left adjoint to \(g\), composition with \(g\) is left adjoint to
composition with \(\mathbb Z[-]\): a morphism \(F\circ g\to G\) gives
\(F\to F\circ g\circ\mathbb Z[-]\to G\circ\mathbb Z[-]\), using the unit \(M\to g(\mathbb Z[M])\), and a morphism
\(F\to G\circ\mathbb Z[-]\) gives \(F\circ g\to G\circ\mathbb Z[-]\circ g\to G\), using the counit
\(\mathbb Z[g(R)]\to R\); the two constructions are inverse to each other by the triangle identities. A functor
with a right adjoint preserves colimits. The functor \(F\mapsto F\circ g\) preserves limits, and \(P\mapsto P^{a}\)
preserves finite limits by (S2); so \(F\mapsto F_{\mathbb Z}\) preserves finite limits. A morphism is a
monomorphism if and only if its diagonal is an isomorphism, so monomorphisms are preserved. Let
\((u_i\colon F_i\to F)\) be jointly surjective and \(t\in F_{\mathbb Z}(R)\). By (S3) there is a Zariski cover
\((R\to R_k)\) with
\(t|_{R_k}=c(p_k)\) for some \(p_k\in F(g(R_k))\). By Proposition 6.6(b), \(p_k=u_i(q)\) for some \(i\) and some
\(q\in F_i(g(R_k))\). So \(t|_{R_k}\) is the image of \(c(q)\in(F_i)_{\mathbb Z}(R_k)\).

(b) \((\operatorname{Spec}M)(g(R))=\mathrm{Hom}(M,g(R))=\mathrm{Hom}(\mathbb Z[M],R)\). This presheaf is
representable, so it is a sheaf.

(c) The morphisms \(\operatorname{Spec}M_a\to U\), \(a\in I\), are jointly surjective, and
\(U\to\operatorname{Spec}M\) is a monomorphism. By (a) and (b), and because
\(\mathbb Z[M_a]=\mathbb Z[M]_a\), the morphisms
\(\operatorname{Spec}\mathbb Z[M]_a\to U_{\mathbb Z}\) are jointly surjective and
\(U_{\mathbb Z}\to\operatorname{Spec}\mathbb Z[M]\) is a monomorphism. So the image of \(U_{\mathbb Z}\) is the
image of the family \((\operatorname{Spec}\mathbb Z[M]_a\to\operatorname{Spec}\mathbb Z[M])_{a\in I}\). The morphism
\(\operatorname{Spec}\mathbb Z[M]_a\to\operatorname{Spec}\mathbb Z[M]\) is an isomorphism onto the open subscheme
\(D(a)\) [Stacks, Tag [01I3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-standard-open-affine)]. By Step 2 of the proof of Theorem 4.2, for the geometric model of Theorem 5.3, the
image of the family is the functor of points of the union of the open subschemes \(D(a)\).

(d) Let \(t\in F_{\mathbb Z}(R)\), regarded as a morphism \(\operatorname{Spec}R\to F_{\mathbb Z}\), and put
\(W=\operatorname{Spec}R\times_{F_{\mathbb Z}}F'_{\mathbb Z}\). By (a), \(W\to\operatorname{Spec}R\) is a
monomorphism; we regard \(W\) as a subsheaf of \(\operatorname{Spec}R\). We must show that \(W\) is a Zariski open
of \(\operatorname{Spec}R\). By (S3) there are a Zariski cover \((R\to R_k)\) and sections \(p_k\in F(g(R_k))\)
with \(t|_{R_k}=c(p_k)\). Regard \(p_k\) as a morphism \(\operatorname{Spec}g(R_k)\to F\). Its base change is a
morphism \((p_k)_{\mathbb Z}\colon\operatorname{Spec}\mathbb Z[g(R_k)]\to F_{\mathbb Z}\). Under the adjunction,
the identity of \(g(R_k)\) corresponds to the counit \(\varepsilon\colon\mathbb Z[g(R_k)]\to R_k\). So
\((p_k)_{\mathbb Z}\) sends the section \(\varepsilon\) of \(\operatorname{Spec}\mathbb Z[g(R_k)]\) over \(R_k\) to
\(c(p_k)=t|_{R_k}\). In other words, \(t|_{R_k}\) is the composite
\[
\operatorname{Spec}R_k\xrightarrow{\ \varepsilon\ }\operatorname{Spec}\mathbb Z[g(R_k)]
\xrightarrow{\ (p_k)_{\mathbb Z}\ }F_{\mathbb Z}.
\]
The sheaf \(U_k=\operatorname{Spec}g(R_k)\times_FF'\) is a Zariski open of \(\operatorname{Spec}g(R_k)\), because
\(F'\to F\) is a Zariski open immersion. By (a) and (c),
\((U_k)_{\mathbb Z}=\operatorname{Spec}\mathbb Z[g(R_k)]\times_{F_{\mathbb Z}}F'_{\mathbb Z}\) is a Zariski open of
\(\operatorname{Spec}\mathbb Z[g(R_k)]\). Hence
\[
W\times_{\operatorname{Spec}R}\operatorname{Spec}R_k
=\operatorname{Spec}R_k\times_{\operatorname{Spec}\mathbb Z[g(R_k)]}(U_k)_{\mathbb Z}
\]
is a Zariski open of \(\operatorname{Spec}R_k\), by Lemma 3.6(c). By Lemma 3.6(f), \(W\) is a Zariski open of
\(\operatorname{Spec}R\).

(e) The morphisms \(\operatorname{Spec}\mathbb Z[M_i]\to F_{\mathbb Z}\) are Zariski open immersions by (b) and
(d), and they are jointly surjective by (a). \(\square\)

*Reference:* [Toën–Vaquié 2009, Corollaire 2.22 and Section 3.3] construct the base change in two steps, through
semirings, from a general criterion. The proof above is direct and uses Theorem 6.5.

**Proposition 7.3 (points in local rings).** Let \(F\colon\mathrm{Mon}\to\mathrm{Set}\) be a functor and \(R\) a
local ring. Then \(c\colon F(g(R))\to F_{\mathbb Z}(R)\) is bijective. In particular
\(F_{\mathbb Z}(k)=F((k,\cdot))\) for every field \(k\).

*Proof.* Let \((R\to R_i)_{i\in I}\) be a Zariski cover. By Proposition 5.1 the open subsets
\(\operatorname{Spec}R_i\) cover \(\operatorname{Spec}R\). One of them contains the maximal ideal. Its complement
is a closed set \(V(\mathfrak a)\) that does not contain the maximal ideal, so \(\mathfrak a=R\) and the complement
is empty. Hence some \(R\to R_{i_0}\) is an isomorphism. Now (S3) gives the claim: a section of \(F_{\mathbb Z}\)
over \(R\) comes from \(F(g(R_{i_0}))=F(g(R))\), and two sections of \(F\circ g\) over \(R\) with the same image
in \(F_{\mathbb Z}(R)\) agree on some \(R_{i_0}\cong R\). \(\square\)

**Corollary 7.4 (base change by gluing).** Let \(X\) be a plain monoid scheme with a cover by affine opens
\(U_i\cong\operatorname{Spec}M_i\), \(i\in I\). Let \(X_{\mathbb Z}\) be the scheme with
\(h_{X_{\mathbb Z}}\cong(h_X)_{\mathbb Z}\). Then \(X_{\mathbb Z}\) is covered by open subschemes isomorphic to
\(\operatorname{Spec}\mathbb Z[M_i]\). Inside \(\operatorname{Spec}\mathbb Z[M_i]\), the intersection of the
\(i\)-th and the \(j\)-th of them is the union of the open sets \(D(a)\) of \(\operatorname{Spec}\mathbb Z[M_i]\),
taken over all \(a\in M_i\) for which the open set \(D(a)\) of \(\operatorname{Spec}M_i\) lies in \(U_i\cap U_j\).
So \(X_{\mathbb Z}\) is the scheme obtained by gluing the schemes
\(\operatorname{Spec}\mathbb Z[M_i]\) along these open subschemes, as in [Deitmar 2005, Section 2.3], and the
result of that gluing does not depend on the cover.

*Proof.* By Theorem 6.10, \((h_{U_i}\to h_X)\) is an atlas, and \(h_{U_i}\times_{h_X}h_{U_j}=h_{U_i\cap U_j}\) is the
Zariski open of \(\operatorname{Spec}M_i\) that is the image of the \(\operatorname{Spec}(M_i)_a\) with
\(D(a)\subseteq U_i\cap U_j\). By Theorem 7.2, \((\operatorname{Spec}\mathbb Z[M_i]\to(h_X)_{\mathbb Z})\) is an
atlas, and the fibre product of its \(i\)-th and \(j\)-th members is \((h_{U_i\cap U_j})_{\mathbb Z}\), which is
the functor of points of the union of the sets \(D(a)\). By Theorem 5.3 the members of the atlas correspond to open
subschemes that cover \(X_{\mathbb Z}\), and fibre products correspond to intersections. \(\square\)

*Reference:* [Vezzani 2012, Proposition 42].

**Remark 7.5 (monoids with zero).** Let \(g_0\colon\mathrm{Ring}\to\mathrm{Mon}_0\) send a ring to its
multiplicative monoid, with its zero. Its left adjoint is the functor \(M\mapsto\mathbb Z[M]\) of the lesson
*Commutative monoids and their spectra*: the free abelian group on \(M\setminus\{0\}\), with the product of \(M\).
For a sheaf \(F\) on \(\mathrm{Aff}_{\mathrm{Set}_{\ast}}\) put \(F_{\mathbb Z}=(F\circ g_0)^{a}\). Theorem 7.2,
Proposition 7.3 and Corollary 7.4 hold in this setting, with the same proofs and two remarks. First, if \(G\) is a
sheaf on rings, then \(G\circ\mathbb Z[-]\) is a sheaf on \(\mathrm{Aff}_{\mathrm{Set}_{\ast}}\), because
\(\mathbb Z[0]\) is the zero ring and \(G(0)\) has one element. Second, in the proof that jointly surjective
families are preserved, Proposition 6.11(b) applies to the rings \(R_k\neq0\); a ring \(R_k=0\) is covered by the
empty family. For a plain monoid \(M\) we have \(\mathbb Z[M_0]=\mathbb Z[M]\), so the base changes of
\(\operatorname{Spec}M\) and of \(\operatorname{Spec}M_0\) agree.

In the lesson *Monoid schemes*, the base change \(X_{\mathbb Z}\) of a monoid scheme \(X\) is the scheme glued from
the schemes \(\operatorname{Spec}\mathbb Z[M_i]\), for an affine open cover \(U_i\cong\operatorname{Spec}M_i\) of
\(X\), along the open subschemes that correspond to the sets \(U_i\cap U_j\). By Corollary 7.4 for monoid schemes,
the scheme with functor of points \((h_X)_{\mathbb Z}\) is glued from the same schemes along the same open
subschemes, and in both constructions the gluing isomorphisms are the ones induced by the open subspaces
\(U_i\cap U_j\) of \(X\). So the two base changes agree.

## 8. Examples

All examples are stated for \(\mathcal C=\mathrm{Set}\). For symbols \(x_1,\dots,x_n\) we write
\(\langle x_1,\dots,x_n\rangle\) for the free plain monoid on them; its elements are the monomials
\(x_1^{d_1}\cdots x_n^{d_n}\) with \(d_i\in\mathbb N\). We write \(\langle t,t^{-1}\rangle\) for the infinite cyclic
group generated by \(t\).

**Example 8.1 (diagonalizable groups).** Let \(\Gamma\) be an abelian group, regarded as a plain monoid, and put
\(D(\Gamma)=\operatorname{Spec}\Gamma\). A morphism of plain monoids sends units to units. So for every plain monoid
\(P\),
\[
D(\Gamma)(P)=\mathrm{Hom}_{\mathrm{Mon}}(\Gamma,P)=\mathrm{Hom}_{\mathrm{groups}}(\Gamma,P^\times).
\]
This set is an abelian group under pointwise multiplication, naturally in \(P\). So \(D(\Gamma)\) is a commutative
group object of \(\mathrm{Sch}(\mathrm{Set})\). By Theorem 7.2(b), its base change is
\(\operatorname{Spec}\mathbb Z[\Gamma]\), the spectrum of the group ring. This is the diagonalizable group scheme
with character group \(\Gamma\).

For \(\Gamma=\langle t,t^{-1}\rangle\) we get the *multiplicative group* \(\mathbb G_m\), with
\(\mathbb G_m(P)=P^\times\) and base change \(\operatorname{Spec}\mathbb Z[t,t^{-1}]\). For the cyclic group
\(\mu_n\) of order \(n\) with generator \(\zeta\), a morphism \(\mu_n\to P\) is determined by the image \(x\) of
\(\zeta\), and \(x\) is any element with \(x^n=1\). So \(D(\mu_n)(P)=\{x\in P\mid x^n=1\}\), and the base change is
\(\operatorname{Spec}\mathbb Z[t]/(t^n-1)\), the group scheme of \(n\)-th roots of unity. In the notation of this
course, \(\mathbb F_{1^n}\) is the monoid \(\mu_n\sqcup\{0\}\). By Remarks 6.13 and 7.5, the affine scheme
\(\operatorname{Spec}\mathbb F_{1^n}\) relative to \(\mathrm{Set}_{\ast}\) has the same points with values in a
monoid, and the same base change to the integers.

*Reference:* [Toën–Vaquié 2009, Section 4.1].

**Example 8.2 (affine spaces and the projective line).** Put
\(\mathbb A^n=\operatorname{Spec}\langle x_1,\dots,x_n\rangle\). Then \(\mathbb A^n(P)=P^n\), and the base change is
\(\operatorname{Spec}\mathbb Z[x_1,\dots,x_n]\). The localization of \(\langle x\rangle\) at \(x\) is
\(\langle x,x^{-1}\rangle\), so \(\mathbb G_m\) is the Zariski open \(U_{\{x\}}\) of \(\mathbb A^1\) (Example 6.8).

The projective line \(\mathbb P^1\) is the plain monoid scheme obtained by gluing
\(U_0=\operatorname{Spec}\langle t\rangle\) and \(U_\infty=\operatorname{Spec}\langle t^{-1}\rangle\) along their
open subspaces \(D(t)\) and \(D(t^{-1})\), which are both isomorphic to
\(\operatorname{Spec}\langle t,t^{-1}\rangle\) [Deitmar 2005, Section 2.3]. We compute its functor of points. By
Theorem 6.10 the morphisms
\(h_{U_0}\to h_{\mathbb P^1}\) and \(h_{U_\infty}\to h_{\mathbb P^1}\) are monomorphisms, they are jointly surjective
on every plain monoid \(P\), and their fibre product is \(h_{U_0\cap U_\infty}\). Now \(h_{U_0}(P)=P\) by the image
of \(t\), \(h_{U_\infty}(P)=P\) by the image of \(t^{-1}\), and \(h_{U_0\cap U_\infty}(P)=P^\times\). So
\[
\mathbb P^1(P)=(P\sqcup P)/{\sim},
\]
where a unit \(u\) in the first copy is identified with \(u^{-1}\) in the second copy. For a finite plain monoid
\(P\) this set has \(|P^\times|+2\,|P\setminus P^\times|\) elements. For \(P=(\mathbb F_q,\cdot)\) the number is
\((q-1)+2=q+1\). By Corollary 7.4 the base change of \(\mathbb P^1\) is the scheme glued from
\(\operatorname{Spec}\mathbb Z[t]\) and \(\operatorname{Spec}\mathbb Z[t^{-1}]\) along
\(\operatorname{Spec}\mathbb Z[t,t^{-1}]\), the projective line over \(\mathbb Z\). By Proposition 7.3 its points in
a field \(k\) are the elements of \(\mathbb P^1((k,\cdot))\); this recovers the count \(q+1\) for \(k=\mathbb F_q\).

**Definition 8.3 (the general linear group).** Let \(\mathcal C\) satisfy Hypothesis 1.1 and let \(n\ge1\). For a
commutative monoid \(A\) in \(\mathcal C\) put
\[
GL_{n,\mathcal C}(A)=\mathrm{Aut}_{\mathrm{Mod}_A}(A^{\oplus n}),
\]
the group of automorphisms of the free \(A\)-module of rank \(n\). For a morphism \(f\colon A\to B\), the functor
\(f^{\ast}\) and the isomorphism \(f^{\ast}(A^{\oplus n})\cong B^{\oplus n}\) of Proposition 1.7(d) give a group
homomorphism \(GL_{n,\mathcal C}(A)\to GL_{n,\mathcal C}(B)\). So \(GL_{n,\mathcal C}\) is a functor from
\(\mathrm{Comm}(\mathcal C)\) to groups.

For \(\mathcal C=\mathrm{Ab}\) this is the usual functor \(R\mapsto GL_n(R)\) of invertible matrices. It is
represented by the ring \(\mathbb Z[x_{ij}][1/\det]\), where \(1\le i,j\le n\), so it is the affine scheme
\(GL_{n,\mathbb Z}\).

**Proposition 8.4 (the general linear group over \(\mathbb F_1\)).** Let \(\mathcal C=\mathrm{Set}\), let
\(n\ge1\), and let \(\Sigma_n\) be the symmetric group.

(a) Let \(M\) be a plain monoid. The free \(M\)-set of rank \(n\) is \(M\times\{1,\dots,n\}\), with basis
\(e_i=(1,i)\). Its automorphisms are the maps \(e_i\mapsto m_ie_{\tau(i)}\) with \(\tau\in\Sigma_n\) and
\(m=(m_1,\dots,m_n)\in(M^\times)^n\). Writing \((\tau,m)\) for this automorphism, the product is
\[
(\tau',m')(\tau,m)=(\tau'\tau,(m_im'_{\tau(i)})_i).
\]
So \(GL_{n,\mathrm{Set}}(M)\) is a semidirect product of \(\Sigma_n\) and the normal subgroup \((M^\times)^n\). In
particular \(GL_{n,\mathrm{Set}}(\mathbb F_1)=\Sigma_n\).

(b) As a functor to sets, \(GL_{n,\mathrm{Set}}\) is the disjoint union of \(n!\) copies of
\(\mathbb G_m^n=\operatorname{Spec}(\mathbb Z^n)\), indexed by \(\Sigma_n\); here \(\mathbb Z^n\) is the free abelian
group of rank \(n\), regarded as a plain monoid. It is a scheme relative to \(\mathrm{Set}\). It is affine only for
\(n=1\).

(c) The base change \((GL_{n,\mathrm{Set}})_{\mathbb Z}\) is the disjoint union of \(n!\) copies of the torus
\(\operatorname{Spec}\mathbb Z[t_1^{\pm1},\dots,t_n^{\pm1}]\). It is a group scheme. For a local ring \(R\), its
group of \(R\)-points is the group of monomial matrices in \(GL_n(R)\): the matrices with exactly one non-zero
entry in each row and each column, all non-zero entries being units.

(d) For \(n\ge2\) the scheme \((GL_{n,\mathrm{Set}})_{\mathbb Z}\) is not isomorphic to \(GL_{n,\mathbb Z}\).

*Proof.* (a) By Proposition 1.5 the coproduct of \(n\) copies of \(M\) is the disjoint union, with \(M\) acting on
each copy. A morphism of \(M\)-sets from \(M\times\{1,\dots,n\}\) to itself is determined by the images of the
\(e_i\), and these can be arbitrary elements \(m_ie_{\tau(i)}\), with \(\tau\) any map from \(\{1,\dots,n\}\) to
itself and \(m_i\in M\). Composing \(e_i\mapsto m_ie_{\tau(i)}\) with \(e_j\mapsto m'_je_{\tau'(j)}\) gives
\(e_i\mapsto m_im'_{\tau(i)}e_{\tau'\tau(i)}\). If \((\tau,m)\) has the inverse \((\tau',m')\), then
\(\tau'\tau=\mathrm{id}=\tau\tau'\) and \(m_im'_{\tau(i)}=1\), so \(\tau\) is a permutation and every \(m_i\) is a
unit. Conversely, such a pair has the inverse \((\tau^{-1},m')\) with \(m'_j=m_{\tau^{-1}(j)}^{-1}\). The pairs
\((\mathrm{id},m)\) form a normal subgroup isomorphic to \((M^\times)^n\), the pairs \((\tau,1)\) form a subgroup
isomorphic to \(\Sigma_n\), and every element is a product \((\tau,1)(\mathrm{id},m)\) in exactly one way. For
\(M=\{1\}\) only the pairs \((\tau,1)\) remain.

(b) A morphism \(\varphi\colon M\to N\) sends \((\tau,m)\) to \((\tau,\varphi(m))\). So, as a functor to sets,
\(GL_{n,\mathrm{Set}}\) is the disjoint union over \(\tau\in\Sigma_n\) of the functors
\(X_\tau\colon M\mapsto(M^\times)^n\), and \((M^\times)^n=\mathrm{Hom}(\mathbb Z^n,M)\). Let \(s\) be a section of
\(GL_{n,\mathrm{Set}}\) over \(P\), lying in the copy \(X_{\tau_0}\). Then
\(\operatorname{Spec}P\times_{GL_{n,\mathrm{Set}}}X_\tau\) is \(\operatorname{Spec}P\) if \(\tau=\tau_0\), and the
empty functor otherwise. Both are Zariski opens of \(\operatorname{Spec}P\) (Example 6.8). So every
\(X_\tau\to GL_{n,\mathrm{Set}}\) is a Zariski open immersion, and the \(X_\tau\) form an atlas. A representable
functor has
exactly one point with values in the trivial monoid \(\{1\}\), and \(GL_{n,\mathrm{Set}}(\{1\})\) has \(n!\)
elements. So \(GL_{n,\mathrm{Set}}\) is not affine for \(n\ge2\). For \(n=1\) it is \(\mathbb G_m\).

(c) By Theorem 7.2, the base change has the atlas
\((\operatorname{Spec}\mathbb Z[\mathbb Z^n]\to(GL_{n,\mathrm{Set}})_{\mathbb Z})_{\tau\in\Sigma_n}\), and
\(\mathbb Z[\mathbb Z^n]=\mathbb Z[t_1^{\pm1},\dots,t_n^{\pm1}]\). For \(\tau\neq\tau'\) the fibre product of
\(X_\tau\) and \(X_{\tau'}\) over \(GL_{n,\mathrm{Set}}\) is the empty functor. Base change preserves fibre
products and the initial object. So the corresponding fibre product after base change is the initial sheaf, which
is the functor of points of the empty scheme (Example 3.10). By Theorem 5.3, the scheme
\((GL_{n,\mathrm{Set}})_{\mathbb Z}\) is covered by \(n!\) pairwise disjoint open subschemes isomorphic to the
torus. So it is their disjoint union. Base change preserves finite products, so it carries the group object
\(GL_{n,\mathrm{Set}}\) to a group object. For a local ring \(R\), Proposition 7.3 gives
\((GL_{n,\mathrm{Set}})_{\mathbb Z}(R)=GL_{n,\mathrm{Set}}((R,\cdot))\), the group of pairs \((\tau,r)\) with
\(r\in(R^\times)^n\). Sending \((\tau,r)\) to the matrix of the \(R\)-linear map \(e_i\mapsto r_ie_{\tau(i)}\) of
\(R^n\) is an injective group homomorphism to \(GL_n(R)\), and its image is the group of monomial matrices.

(d) The torus is not empty. So for \(n\ge2\) the scheme \((GL_{n,\mathrm{Set}})_{\mathbb Z}\) is the disjoint union
of at least two non-empty open subschemes, and it is not connected. The ring \(\mathbb Z[x_{ij}][1/\det]\) is an
integral domain, as a localization of a polynomial ring over \(\mathbb Z\). Its zero ideal is a prime ideal, and it
lies in every non-empty open subset of the spectrum, because such a subset contains a non-empty set \(D(h)\) and
\(h\neq0\). So any two non-empty open subsets of \(GL_{n,\mathbb Z}\) meet, and \(GL_{n,\mathbb Z}\) is connected.
\(\square\)

*Reference:* [Toën–Vaquié 2009, Proposition 4.1]; [Deitmar 2005, Section 5.1].

**Remark 8.5.**

(a) Part (a) of the proposition realizes, for the group \(GL_n\), the proposal of Tits discussed in
*Counting over finite fields and the limit q → 1*: the group of \(\mathbb F_1\)-points is the Weyl group
\(\Sigma_n\).

(b) Part (d) says that the functor of automorphisms of the free module of rank \(n\) over \(\mathbb F_1\) does not
give \(GL_{n,\mathbb Z}\) after base change; it gives the subgroup of monomial matrices. It does not say that no
other scheme relative to \(\mathrm{Set}\) has base change \(GL_{n,\mathbb Z}\). That question is taken up in the
lesson *Torified varieties and the limits of monoid schemes*.

(c) For monoids with zero the result is the same. The free pointed \(M\)-set of rank \(n\) is a wedge of \(n\)
copies of \(M\), its automorphisms for \(M\neq0\) are again the maps \(e_i\mapsto m_ie_{\tau(i)}\) with
\(\tau\in\Sigma_n\) and \(m_i\in M^\times\), and \(GL_n(\mathbb F_1)=\Sigma_n\) for \(\mathbb F_1=\{0,1\}\).

## 9. Exercises

**Exercise 1 (descent by hand).** Let \(\mathcal C=\mathrm{Ab}\), \(A=\mathbb Z\), \(A_1=\mathbb Z[1/2]\) and
\(A_2=\mathbb Z[1/3]\).

(a) Show that \((\mathbb Z\to A_1,\mathbb Z\to A_2)\) is a Zariski cover.

(b) Verify the statement of Theorem 2.4 for \(M=\mathbb Z\) by a direct computation.

(c) Show that the family with the single member \(\mathbb Z\to A_1\) is not a flat cover.

*Solution.* (a) The morphism \(\operatorname{Spec}\mathbb Z[1/m]\to\operatorname{Spec}\mathbb Z\) is an open
immersion onto \(D(m)\) [Stacks, Tag [01I3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-standard-open-affine)]. So both morphisms are Zariski open immersions by Proposition 5.1(d). No
prime ideal of \(\mathbb Z\) contains both \(2\) and \(3\), so \(D(2)\cup D(3)=\operatorname{Spec}\mathbb Z\). Now
apply Proposition 5.1(e).

(b) We have \(A_1\otimes A_2=\mathbb Z[1/6]\). Since \(\mathbb Z\to A_i\) is an epimorphism,
\(A_i\otimes A_i=A_i\) and the two morphisms \(A_i\to A_i\otimes A_i\) are equal (Proposition 1.9). So the
components of \(d_0\) and \(d_1\) with indices \((1,1)\) and \((2,2)\) agree, and the components with indices
\((1,2)\) and \((2,1)\) give the same condition. The equalizer of \(d_0\) and \(d_1\) is therefore the set of pairs
\((a,b)\in\mathbb Z[1/2]\times\mathbb Z[1/3]\) with \(a=b\) in \(\mathbb Z[1/6]\). Such a rational number has, in
lowest terms, a denominator that is a power of \(2\) and a power of \(3\). So it is an integer, and the equalizer
is \(\mathbb Z\), embedded by \(e\).

(c) The homomorphism \(\mathbb Z/2\to0\) is not an isomorphism, and
\(\mathbb Z[1/2]\otimes\mathbb Z/2=0\). So the base change to \(A_1\) is not conservative. The empty subfamily is
not jointly conservative either, because \(\mathbb Z\neq0\) (Example 2.2(c)).

**Exercise 2 (flatness over \(\mathbb F_1\), with zero).** Let \(\mathcal C=\mathrm{Set}_{\ast}\), let \(N\) be a
monoid and \(\varphi\colon\mathbb F_1=\{0,1\}\to N\) the unique morphism. Show that \(\varphi\) is flat if and only
if \(N=0\) or \(N=\mathbb F_1\).

*Solution.* Modules over \(\mathbb F_1\) are pointed sets, and \(\varphi^{\ast}T=N\wedge T\). If \(N=0\), every
\(N\)-module has one element, so there is exactly one morphism between any two \(N\)-modules and every functor to
\(\mathrm{Mod}_N\) preserves limits. If \(N=\mathbb F_1\), then \(\varphi^{\ast}\) is the identity. Otherwise
\(N\) contains an element \(x\) different from \(0\) and \(1\), and \(1\neq0\). Let \(T=S^0=\{\ast,1\}\). We
identify \(N\wedge T\) with \(N\), by \(n\wedge1\mapsto n\). The product \(T\times T\) has the four elements
\((\ast,\ast)\), \((1,\ast)\), \((\ast,1)\), \((1,1)\) and the base point \((\ast,\ast)\). The comparison map
\(N\wedge(T\times T)\to(N\wedge T)\times(N\wedge T)=N\times N\) sends \(n\wedge(1,1)\) to \((n,n)\),
\(n\wedge(1,\ast)\) to \((n,0)\) and \(n\wedge(\ast,1)\) to \((0,n)\). The pair \((1,x)\) is not of any of these
forms. So \(\varphi^{\ast}\) does not preserve the product \(T\times T\), and \(\varphi\) is not flat.

**Exercise 3 (the punctured plane).** Let \(M=\langle x,y\rangle\) and let \(U=U_{\{x,y\}}\) be the Zariski open of
\(\mathbb A^2=\operatorname{Spec}M\) of Example 6.8.

(a) Show that \(U\) is a scheme relative to \(\mathrm{Set}\).

(b) Show that \(U\) is not affine.

(c) Describe \(U_{\mathbb Z}\) and its points in a field \(k\).

*Solution.* (a) The inclusion \(U\to\mathbb A^2\) is a Zariski open immersion by Lemma 3.6(c). So \(U\) is a scheme
by Proposition 3.9(a) and (b).

(b) Suppose \(U\cong\operatorname{Spec}N\). An isomorphism is a Zariski open immersion, so by Lemma 3.6(c) and (d)
the composite \(\operatorname{Spec}N\to U\to\operatorname{Spec}M\) is a Zariski open immersion of sheaves. By
Theorem 6.10 the category \(\mathrm{Set}\) has a geometric model. So Corollary 4.3 and Theorem 6.5(b) show that
\(N\cong M_a\) as \(M\)-algebras, for some \(a\in M\). Then \(U=\operatorname{Spec}M_a\) as subfunctors of
\(\operatorname{Spec}M\). The canonical morphism \(M\to M_x\) is a section of \(\operatorname{Spec}M_x\subseteq U\)
over \(M_x\). So it is a section of \(\operatorname{Spec}M_a\), which means that \(a\) is a unit of \(M_x\). The
monoid \(M_x\) consists of the monomials \(x^iy^j\) with \(i\in\mathbb Z\), \(j\ge0\), and its units are the
powers of \(x\). So \(a=x^i\) with \(i\ge0\). In the same way \(a=y^j\) with \(j\ge0\). Hence \(a=1\) and
\(U=\operatorname{Spec}M\). But the identity of \(M\) is a section of \(\operatorname{Spec}M\) over \(M\), it
corresponds to the pair \((x,y)\in M\times M\), and neither \(x\) nor \(y\) is a unit of \(M\). So it is not a
section of \(U\). This is a contradiction.

(c) By Theorem 7.2(c), \(U_{\mathbb Z}\) is the open subscheme \(D(x)\cup D(y)\) of
\(\operatorname{Spec}\mathbb Z[x,y]\), the complement of the closed subset defined by \(x=y=0\). By
Proposition 7.3, \(U_{\mathbb Z}(k)=U((k,\cdot))\) is the set of pairs \((p,q)\in k\times k\) with \(p\neq0\) or
\(q\neq0\).

**Exercise 4 (the general linear group of the semiring \(\mathbb N\)).** Let \(\mathcal C=\mathrm{CMon}\). The
unit object \(\mathbb N\) is the semiring of natural numbers, \(\mathrm{Mod}_{\mathbb N}=\mathrm{CMon}\), and the
free module of rank \(n\) is \(\mathbb N^n\).

(a) Show that the endomorphisms of \(\mathbb N^n\) are the \(n\times n\) matrices with entries in \(\mathbb N\),
and that composition is the matrix product.

(b) Show that \(GL_{n,\mathrm{CMon}}(\mathbb N)\) is the group of permutation matrices, so that it is isomorphic to
\(\Sigma_n\).

*Solution.* (a) \(\mathbb N^n\) is the free commutative monoid on the basis vectors \(e_1,\dots,e_n\). So an
endomorphism is determined by the images of the \(e_j\), which are arbitrary vectors; they are the columns of a
matrix, and composition is the matrix product.

(b) Let \(A=(a_{ij})\) and \(B=(b_{ij})\) be matrices with entries in \(\mathbb N\) and \(AB=BA=I\). Fix \(i\).
The sum \(\sum_ka_{ik}b_{ki}\) equals \(1\) and its terms lie in \(\mathbb N\). So there is exactly one index
\(k=\pi(i)\) with \(a_{ik}b_{ki}=1\), that is, \(a_{i\pi(i)}=b_{\pi(i)i}=1\), and \(a_{ik}b_{ki}=0\) for
\(k\neq\pi(i)\). Suppose \(a_{il}\ge1\) for some \(l\neq\pi(i)\). Then \(b_{li}=0\). For \(j\neq i\) we have
\(0=\sum_ka_{ik}b_{kj}\ge a_{il}b_{lj}\), so \(b_{lj}=0\). So the \(l\)-th row of \(B\) is zero, which contradicts
\(\sum_jb_{lj}a_{jl}=1\). Hence the \(i\)-th row of \(A\) has the single non-zero entry \(a_{i\pi(i)}=1\). If
\(\pi(i)=\pi(j)\) for some \(i\neq j\), then the rows \(i\) and \(j\) of \(A\) are equal, and so are the rows \(i\)
and \(j\) of \(AB=I\), which is false. So \(\pi\) is a permutation and \(A\) is a permutation matrix. Conversely a
permutation matrix is invertible, with its transpose as inverse.

*Reference:* [Toën–Vaquié 2009, Proposition 4.1(4)].

**Exercise 5 (signed permutations).** Let \(P=\{1,-1\}\), the cyclic group of order \(2\), regarded as a plain
monoid.

(a) Show that \(GL_{n,\mathrm{Set}}(P)\) is isomorphic to the group of signed permutation matrices, of order
\(2^nn!\), and that for \(n=2\) it is a dihedral group of order \(8\).

(b) Compare the number of points of \(GL_{2,\mathrm{Set}}\) in \((\mathbb F_q,\cdot)\) with the order of
\(GL_2(\mathbb F_q)\).

*Solution.* (a) By Proposition 8.4(a) the group consists of the pairs \((\tau,m)\) with \(\tau\in\Sigma_n\) and
\(m\in\{1,-1\}^n\). There are \(2^nn!\) of them. As in the proof of Proposition 8.4(c), sending \((\tau,m)\) to the
matrix of the linear map \(e_i\mapsto m_ie_{\tau(i)}\) of \(\mathbb Z^n\) identifies the group with the group of
matrices that have exactly one non-zero entry in each row and column, equal to \(1\) or \(-1\). For \(n=2\) let
\(s\) be the permutation matrix of
the transposition, \(d\) the diagonal matrix with entries \(-1,1\), and \(r=sd\). Then \(r^2=-I\), so \(r\) has
order \(4\), and \(srs=ds=r^{-1}\). The group has order \(8\) and is generated by \(r\) and \(s\). So it is
dihedral.

(b) By Proposition 8.4(a), \(GL_{2,\mathrm{Set}}((\mathbb F_q,\cdot))\) has \(2(q-1)^2\) elements. The group
\(GL_2(\mathbb F_q)\) has \((q^2-1)(q^2-q)=q(q+1)(q-1)^2\) elements. Since \(q(q+1)\ge6\), the two numbers are
different for every \(q\). This agrees with Proposition 8.4(d).

**Exercise 6 (the three conditions for plain monoids).**

(a) Show that the inclusion \(\langle x\rangle\to\langle x,x^{-1}\rangle\) is an epimorphism that is not
surjective, and compute \(\langle x,x^{-1}\rangle\otimes_{\langle x\rangle}\langle x,x^{-1}\rangle\).

(b) Show that the morphism \(\langle x\rangle\to\{1\}\) is an epimorphism of finite presentation that is not flat.

(c) Let \(M\) be the free plain monoid on infinitely many generators \(x_1,x_2,\dots\) and \(\Gamma\) the free
abelian group on the same generators. Show that \(M\to\Gamma\) is a flat epimorphism that is not of finite
presentation.

*Solution.* (a) The inclusion is the localization of \(\langle x\rangle\) at \(x\). It is an epimorphism by
Proposition 6.2(a), and \(x^{-1}\) is not in its image. By Proposition 1.9 the multiplication map from the tensor
product to \(\langle x,x^{-1}\rangle\) is bijective.

(b) A surjective morphism is an epimorphism. We check (FP). Let \((D_\alpha)\) be a directed system of
\(\langle x\rangle\)-algebras with colimit \(D\). A morphism of \(\langle x\rangle\)-algebras \(\{1\}\to D\) exists
if and only if the image of \(x\) in \(D\) is \(1\). Since \(D\) is the colimit of the underlying sets, this then
holds in some \(D_\alpha\). So the morphism is of finite presentation. If it were flat, it would be a Zariski open
immersion, and \(\{1\}\) would be isomorphic to \(\langle x\rangle_a\) for some \(a=x^k\) by Theorem 6.5(b). But
\(\langle x\rangle_{x^k}\) is \(\langle x\rangle\) for \(k=0\) and \(\langle x,x^{-1}\rangle\) for \(k\ge1\), and
both are infinite.

(c) \(\Gamma\) is the localization \(S^{-1}M\) for \(S=M\). So \(M\to\Gamma\) is a flat epimorphism by
Proposition 6.2(a). Suppose it is of finite presentation. By Theorem 6.5(b), \(\Gamma\cong M_a\) as \(M\)-algebras
for some \(a\in M\). Choose \(j\) such that \(x_j\) does not occur in the monomial \(a\). If \(x_j\) were a unit in \(M_a\),
then \(a^lx_jm=a^{l+k}\) in \(M\) for some \(m\in M\) and \(k,l\ge0\), and \(x_j\) would divide a power of \(a\) in
the free monoid \(M\). So \(x_j\) is not a unit in \(M_a\). But \(x_j\) is a unit in \(\Gamma\). This is a
contradiction.

## 10. What this lesson does not prove

1. *Effective descent.* [Toën–Vaquié 2009, Théorème 2.5 and Corollaire 2.11(2)] state that the modules form a
   stack for the flat topology: for a flat cover \((A\to A_i)\), base change is an equivalence from
   \(\mathrm{Mod}_A\) to the category of descent data, that is, of families of \(A_i\)-modules \(M_i\) with
   isomorphisms between the base changes of \(M_i\) and \(M_j\) to \(A_i\otimes_AA_j\) that satisfy the cocycle
   condition over the triple tensor products. The lesson proves and uses only Theorem 2.4.
2. *Finite presentation in Proposition 3.7(b).* [Toën–Vaquié 2009, Lemme 2.14] states, for every \(\mathcal C\)
   that is complete, cocomplete and closed: if a morphism \(\operatorname{Spec}B\to\operatorname{Spec}A\) is a
   Zariski open immersion in the sense of Definition 3.5, then \(A\to B\) is a flat epimorphism of finite
   presentation. The lesson proves that \(A\to B\) is a flat epimorphism (Proposition 3.7). It proves finite
   presentation when \(\mathcal C\) has a geometric model (Corollary 4.3), in particular for abelian groups, sets
   and pointed sets. It does not prove finite presentation for general \(\mathcal C\).
3. *Base change in general.* [Toën–Vaquié 2009, Corollaire 2.22] states the following. Let
   \(f\colon\mathcal C\to\mathcal D\) be a symmetric monoidal functor between complete, cocomplete and closed
   symmetric monoidal categories, with a right adjoint \(g\). Assume that \(g\) is conservative and commutes with
   filtered colimits, and that for every flat morphism \(A\to B\) of \(\mathrm{Comm}(\mathcal C)\) and every
   \(f(A)\)-module \(N\) the natural morphism \(g(N)\otimes_AB\to g(N\otimes_{f(A)}f(B))\) is an isomorphism. Then
   \(f\) induces a functor \(\mathrm{Sch}(\mathcal C)\to\mathrm{Sch}(\mathcal D)\) that sends
   \(\operatorname{Spec}A\) to \(\operatorname{Spec}f(A)\). The lesson proves the cases of the functors from sets
   and from pointed sets to abelian groups (Theorem 7.2 and Remark 7.5), by a direct argument.
4. *Disjoint unions.* [Toën–Vaquié 2009, Proposition 2.18(1)] states that a disjoint union of schemes relative to
   \(\mathcal C\) is a scheme relative to \(\mathcal C\). The lesson proves this only for the disjoint union in
   Proposition 8.4.
5. *Facts quoted from other places.* The coherence theorem [Stacks, Tag [0HB0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-symmetric-monoidal-coherence)], the Yoneda lemma
   [Stacks, Tag [001P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-yoneda)], the criterion for a fully faithful adjoint [Stacks, Tag [07RB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-adjoint-fully-faithful)], the criterion for left exact
   functors [Stacks, Tag [0035](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-left-exact)] and the comparison of filtered and directed colimits [Stacks, Tag [0032](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-directed-category-system)]. The facts
   (S1)–(S3) on sheaves [Stacks, Tags [00W2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-limit-sheaf), [00WH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-sheafification-adjoint), [00WJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-sheafification-exact), [00WK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-sections-sheafification), [00WN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-mono-epi-sheaves)], the description of epimorphisms of sheaves
   [Stacks, Tag [00WN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-mono-epi-sheaves)] and the sheaf condition for the empty cover [Stacks, Tag [04B3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-remark-sheaf-condition-empty-covering)]. The facts on rings and schemes
   used in Section 5 and in Theorem 7.2: [Stacks, Tags [00E7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-in-image), [00E8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-compact), [00HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-zero-local), [00QO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-finite-presentation), [01I2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-category-affine-schemes), [01I3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-standard-open-affine), [01I4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-affine-schemes), [01IK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-open-subspace-scheme), [01IT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-basis-affine-opens), [01JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue),
   [01JC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue-schemes), [01L7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-immersions-monomorphisms), [01TQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-presentation-characterize), [01TT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-open-immersion-locally-finite-presentation), [01U5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-characterize), [01UA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fppf-open), [025G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-etale-radicial-open), [06NC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-flat-surjective-quasi-compact-monomorphism-isomorphism), [08LR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-mono-epi)]. The facts (M1)–(M3) on plain monoid schemes
   [Deitmar 2005], and the corresponding facts on monoids with zero and monoid schemes from *Commutative monoids and
   their spectra* and *Monoid schemes*.
6. *The general linear group.* The lesson does not decide whether \(GL_{n,\mathbb Z}\) is the base change of some
   scheme relative to \(\mathrm{Set}\) or to \(\mathrm{Set}_{\ast}\); see Remark 8.5(b).
7. *Other base categories.* [Toën–Vaquié 2009] also treats the base category \(\mathrm{CMon}\), whose affine
   schemes correspond to commutative semirings (its Section 3.2), and homotopical versions of the theory (its
   Section 5). They are not covered here, apart from Exercise 4.

## References

- [Toën–Vaquié 2009] B. Toën, M. Vaquié, *Au-dessous de Spec Z* (English: *Under Spec Z*), [arXiv:math/0509684](https://arxiv.org/pdf/math/0509684v4).
  Results are cited by their numbers in version 4.
- [Vezzani 2012] A. Vezzani, *Deitmar's versus Toën–Vaquié's schemes over F_1*,
  [arXiv:1005.0287v2](https://arxiv.org/pdf/1005.0287v2), 11 June 2011. Results are cited by their numbers in this preprint version.
- [Deitmar 2005] A. Deitmar, *Schemes over F_1*, [arXiv:math/0404185](https://arxiv.org/pdf/math/0404185).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 0032, 00W2, 00WJ, 08LR and 0FFW carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
