# Monoid schemes

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. The proofs of Sumihiro's theorem (Section 6.4) and of (C1) in Facts 6.10, Section 6.6, and Example 8.9, were drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

## Introduction

A scheme is a space that is locally the spectrum of a ring. A monoid scheme is a space that is locally the spectrum of a commutative monoid. Addition is forgotten and only multiplication is kept. Monoid schemes are the simplest objects that carry the name "schemes over the field with one element" \(\mathbb{F}_1\), and the later lessons of this course either contain them or map to them.

This lesson builds the theory with full proofs and tests it on examples.

- Section 1 proves that a morphism from a monoidal space to \(\operatorname{Spec} M\) is the same as a morphism from \(M\) to the monoid of global sections. So affine monoid schemes are the same as monoids.
- Section 2 defines monoid schemes and treats affine open subsets, finite type, integrality and glueing.
- Section 3 computes the points of a monoid scheme with values in a monoid, in particular in \(\mathbb{F}_1\) and \(\mathbb{F}_{1^n}\), and constructs fibre products. The space of a fibre product is the fibre product of the spaces.
- Section 4 constructs the base change \(X_k\) to a ring \(k\) and counts points over finite fields.
- Section 5 treats projective space over \(\mathbb{F}_1\).
- Section 6 proves, in a precise form, the theorem of [Deitmar 2008] that connected integral monoid schemes of finite type give toric varieties, and that every toric variety arises in this way. Section 6.6 proves that the strong congruence spaces of [Jarra 2023a] see the dimension of toric varieties.
- Section 7 defines the zeta function of a monoid scheme and computes it.
- Section 8 defines sheaves of modules and states exactly what changes compared with rings.

The lesson assumes *Commutative monoids and their spectra*: monoids with zero, prime ideals, the spectrum, localization, the structure sheaf and the monoid algebra. It also assumes the language of schemes (glueing, fibre products, separated and normal schemes). Facts about schemes are cited from [Stacks] by tag.

Basic references are [Deitmar 2005], [Deitmar 2008], [Connes–Consani 2010], [Cortiñas–Haesemeyer–Walker–Weibel 2015] and [Chu–Lorscheid–Santhanam 2012]. The objects of this lesson are called "schemes over \(\mathbb{F}_1\)" in [Deitmar 2005], "\(\mathfrak{Mo}\)-schemes" in [Connes–Consani 2010], "\(\mathcal{M}_0\)-schemes" in [Chu–Lorscheid–Santhanam 2012] and "monoid schemes" in [Cortiñas–Haesemeyer–Walker–Weibel 2015].

**Conventions.** A *monoid* is a commutative monoid, written multiplicatively, with a unit \(1\) and an absorbing element \(0\). Morphisms of monoids preserve \(1\) and \(0\). The zero monoid \(\{0\}\), in which \(0 = 1\), is allowed. The group of units of \(M\) is \(M^\times\). For an abelian group \(H\) we write \(H_0 = H \sqcup \{0\}\), and more generally \(A_0 = A \sqcup \{0\}\) for a commutative monoid \(A\) without zero. The field with one element is the monoid \(\mathbb{F}_1 = \{0, 1\}\), and \(\mathbb{F}_{1^n} = (\mu_n)_0\), where \(\mu_n\) is a cyclic group of order \(n\). Rings are commutative with \(1\). For a ring \(k\), the monoid algebra \(k[M]\) is the free \(k\)-module on \(M \setminus \{0\}\), with the multiplication of \(M\); the zero of \(M\) is the zero of \(k[M]\). The multiplicative monoid of a ring \(R\) is written \((R,\cdot)\).

[Deitmar 2005], [Deitmar 2006] and [Deitmar 2008] work with monoids without zero. We translate their statements by \(A \mapsto A_0\). Remark 3.3 says what this changes.

## 1. Monoidal spaces and affine monoid schemes

### What is used from the previous lesson

Let \(M\) be a monoid. We use the following from *Commutative monoids and their spectra*.

- An ideal is a subset \(I\) with \(0 \in I\) and \(MI \subseteq I\). It is prime if \(I \neq M\) and \(ab \in I\) implies \(a \in I\) or \(b \in I\). The preimage of a prime ideal under a morphism of monoids is a prime ideal.
- \(\operatorname{Spec} M\) is the set of prime ideals. The sets \(D(f) = \{\mathfrak{p} : f \notin \mathfrak{p}\}\), \(f \in M\), form a basis of its topology, and \(D(f) \cap D(g) = D(fg)\).
- For a multiplicative subset \(S\) there is the localization \(\iota\colon M \to S^{-1}M\). It is universal among morphisms that send \(S\) to units. In particular two morphisms out of \(S^{-1}M\) that agree on \(M\) are equal. We write \(M_f\) and \(M_{\mathfrak{p}}\) as for rings. The units of \(M_{\mathfrak{p}}\) are the fractions \(a/s\) with \(a \notin \mathfrak{p}\).
- The map \(\mathfrak{Q} \mapsto \iota^{-1}(\mathfrak{Q})\) from \(\operatorname{Spec} S^{-1}M\) to \(\operatorname{Spec} M\) is a homeomorphism onto the set of prime ideals that do not meet \(S\). This set is \(D(f)\) for \(S = \{f^n : n \geq 0\}\), and it is \(\{\mathfrak{q} : \mathfrak{q} \subseteq \mathfrak{p}\}\) for \(S = M \setminus \mathfrak{p}\).
- The structure sheaf \(\mathcal{O}_M\) is the sheaf of monoids on \(\operatorname{Spec} M\) with \(\mathcal{O}_M(D(f)) = M_f\). Its stalk at \(\mathfrak{p}\) is \(M_{\mathfrak{p}}\), and its monoid of global sections is \(M\). We write \(\operatorname{Spec} M\) also for the pair \((\operatorname{Spec} M, \mathcal{O}_M)\).
- The closure of a point \(\mathfrak{p}\) of \(\operatorname{Spec} M\) is \(\{\mathfrak{q} : \mathfrak{q} \supseteq \mathfrak{p}\}\).

The spectrum of the zero monoid is empty. If \(M \neq 0\), the set \(\mathfrak{m}_M = M \setminus M^\times\) is a prime ideal.

### The closed point

The next lemma is the main difference between monoids and rings. It is used in every section.

**Lemma 1.1.** Let \(M\) be a nonzero monoid.

1. Every prime ideal of \(M\) is contained in \(\mathfrak{m}_M\). The point \(\mathfrak{m}_M\) is the only closed point of \(\operatorname{Spec} M\), and it lies in the closure of every point.
2. The only open subset of \(\operatorname{Spec} M\) that contains \(\mathfrak{m}_M\) is \(\operatorname{Spec} M\). So every open cover of \(\operatorname{Spec} M\) has \(\operatorname{Spec} M\) as one of its members.
3. For every sheaf \(\mathcal{F}\) on \(\operatorname{Spec} M\), the map from \(\mathcal{F}(\operatorname{Spec} M)\) to the stalk of \(\mathcal{F}\) at \(\mathfrak{m}_M\) is bijective.

*Proof.* (1) A prime ideal is a proper ideal, so it contains no unit and lies in \(\mathfrak{m}_M\). The closure of \(\mathfrak{p}\) is \(\{\mathfrak{q} \supseteq \mathfrak{p}\}\), which contains \(\mathfrak{m}_M\). The closure of \(\mathfrak{m}_M\) is \(\{\mathfrak{m}_M\}\). If \(\mathfrak{p}\) is a closed point, then \(\mathfrak{m}_M\) lies in its closure \(\{\mathfrak{p}\}\), so \(\mathfrak{p} = \mathfrak{m}_M\). (2) An open set that contains \(\mathfrak{m}_M\) contains some \(D(f)\) with \(f \notin \mathfrak{m}_M\). Then \(f\) is a unit and \(D(f) = \operatorname{Spec} M\). (3) The stalk is the colimit of \(\mathcal{F}(U)\) over the open neighbourhoods \(U\) of \(\mathfrak{m}_M\), and by (2) there is only one. \(\square\)

*Reference:* [Connes–Consani 2010, Lemma 3.2].

### Monoidal spaces

**Definition 1.2.** A morphism \(\varphi\colon M \to N\) of nonzero monoids is *local* if \(\varphi^{-1}(N^\times) = M^\times\), that is, if \(\varphi(\mathfrak{m}_M) \subseteq \mathfrak{m}_N\).

A *monoidal space* is a pair \((X, \mathcal{O}_X)\) of a topological space and a sheaf of monoids on it, all of whose stalks are nonzero. A *morphism* of monoidal spaces \((X,\mathcal{O}_X) \to (Y,\mathcal{O}_Y)\) is a pair \((f, f^\#)\), where \(f\colon X \to Y\) is continuous and \(f^\#\colon \mathcal{O}_Y \to f_*\mathcal{O}_X\) is a morphism of sheaves of monoids, such that for every \(x \in X\) the induced map of stalks \(f^\#_x\colon \mathcal{O}_{Y,f(x)} \to \mathcal{O}_{X,x}\) is local. The category of monoidal spaces is written \(\mathsf{MS}\).

An open subset \(U \subseteq Y\) with the restricted sheaf \(\mathcal{O}_Y|_U\) is a monoidal space, called an *open subspace* of \(Y\). A morphism \(X \to Y\) whose image lies in \(U\) factors through the open subspace \(U\) in exactly one way. An *open immersion* is a morphism that is an isomorphism onto an open subspace.

For rings one asks that the stalks be local rings. For monoids there is nothing to ask, because every nonzero monoid has exactly one maximal ideal. The condition on morphisms is a real one: the inclusion \(\mathbb{F}_1[t] \to \mathbb{F}_1[t, t^{-1}]\) is not local.

**Examples 1.3.**

1. For every monoid \(M\) the pair \(\operatorname{Spec} M\) is a monoidal space. Its stalks \(M_{\mathfrak{p}}\) are nonzero because \(0 \notin M \setminus \mathfrak{p}\).
2. Let \((Y, \mathcal{O}_Y)\) be a locally ringed space, for example a scheme. Forget the addition of \(\mathcal{O}_Y\). The result is a monoidal space, written \(Y^{\mathrm{mon}}\). For a local ring \(R\) the units of \((R,\cdot)\) are the units of \(R\), so a local homomorphism of local rings is a local morphism of monoids. Hence \(Y \mapsto Y^{\mathrm{mon}}\) is a functor from locally ringed spaces to \(\mathsf{MS}\).

**Theorem 1.4.** Let \((X, \mathcal{O}_X)\) be a monoidal space and \(M\) a monoid. The map
\[
\operatorname{Hom}_{\mathsf{MS}}(X, \operatorname{Spec} M) \longrightarrow \operatorname{Hom}(M, \mathcal{O}_X(X)), \qquad (f, f^\#) \longmapsto f^\#(\operatorname{Spec} M),
\]
is bijective.

*Proof.* Let \(\varphi\colon M \to \mathcal{O}_X(X)\) be a morphism of monoids. We construct the unique morphism of monoidal spaces that maps to \(\varphi\).

For \(x \in X\) let \(\varphi_x\colon M \to \mathcal{O}_{X,x}\) be \(\varphi\) followed by the germ map, and let \(\mathfrak{m}_x\) be the set of non-units of \(\mathcal{O}_{X,x}\). The stalk is nonzero, so \(\mathfrak{m}_x\) is a prime ideal. Put \(f(x) = \varphi_x^{-1}(\mathfrak{m}_x)\), a prime ideal of \(M\).

*Step 1: \(f\) is continuous.* For \(a \in M\) put \(X_a = \{x \in X : \varphi_x(a) \in \mathcal{O}_{X,x}^\times\}\). Then \(X_a = f^{-1}(D(a))\). If the germ of \(s = \varphi(a)\) at \(x\) is a unit, there are an open neighbourhood \(V\) of \(x\) and \(t \in \mathcal{O}_X(V)\) with \(s|_V \cdot t = 1\). So \(V \subseteq X_a\), and \(X_a\) is open. Inverses are unique. So these local inverses agree on overlaps and glue to an inverse of \(s|_{X_a}\) in \(\mathcal{O}_X(X_a)\).

*Step 2: the map of sheaves.* By Step 1 the morphism \(M \to \mathcal{O}_X(X) \to \mathcal{O}_X(X_a)\) sends \(a\) to a unit. So it factors through a unique morphism \(f^\#_a\colon M_a \to \mathcal{O}_X(X_a) = (f_*\mathcal{O}_X)(D(a))\). If \(D(b) \subseteq D(a)\), the two composites \(M_a \to M_b \to \mathcal{O}_X(X_b)\) and \(M_a \to \mathcal{O}_X(X_a) \to \mathcal{O}_X(X_b)\) agree on \(M\), hence they are equal. So the \(f^\#_a\) form a morphism of sheaves on the basis \(\{D(a)\}\). It extends uniquely to a morphism of sheaves \(f^\#\colon \mathcal{O}_M \to f_*\mathcal{O}_X\) [Stacks, Tag [009H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-bases)].

*Step 3: \((f,f^\#)\) is a morphism and maps to \(\varphi\).* The map on stalks \(f^\#_x\colon M_{f(x)} \to \mathcal{O}_{X,x}\) sends \(m/s\) to \(\varphi_x(m)\varphi_x(s)^{-1}\). This is a unit if and only if \(\varphi_x(m)\) is a unit, if and only if \(m \notin f(x)\), if and only if \(m/s\) is a unit. So \(f^\#_x\) is local. Taking \(a = 1\) gives \(f^\#(\operatorname{Spec} M) = \varphi\).

*Step 4: uniqueness.* Let \((g, g^\#)\) be a morphism with \(g^\#(\operatorname{Spec} M) = \varphi\). For \(x \in X\) the local morphism \(g^\#_x\colon M_{g(x)} \to \mathcal{O}_{X,x}\) sends \(m/1\) to \(\varphi_x(m)\). So \(m \in g(x)\) if and only if \(m/1\) is a non-unit, if and only if \(\varphi_x(m) \in \mathfrak{m}_x\), if and only if \(m \in f(x)\). Hence \(g = f\). For \(a \in M\) the map \(g^\#(D(a))\colon M_a \to \mathcal{O}_X(X_a)\) restricts to \(\varphi\) on \(M\), so it equals \(f^\#_a\). Hence \(g^\# = f^\#\). \(\square\)

*Reference:* [Deitmar 2005, Proposition 2.5]; for rings, [Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)].

**Corollary 1.5.**

1. For monoids \(M, N\) the map \(\varphi \mapsto \operatorname{Spec}\varphi\) is a bijection from \(\operatorname{Hom}(M,N)\) to \(\operatorname{Hom}_{\mathsf{MS}}(\operatorname{Spec} N, \operatorname{Spec} M)\). On points, \(\operatorname{Spec}\varphi\) is \(\mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})\).
2. Call a monoidal space an *affine monoid scheme* if it is isomorphic to \(\operatorname{Spec} M\) for some monoid \(M\). Then \(M \mapsto \operatorname{Spec} M\) and \(X \mapsto \mathcal{O}_X(X)\) are mutually inverse anti-equivalences between the category of monoids and the category of affine monoid schemes.
3. \(\operatorname{Spec}\mathbb{F}_1\), a single point with stalk \(\mathbb{F}_1\), is a terminal object of \(\mathsf{MS}\).

*Proof.* (1) Apply Theorem 1.4 to \(X = \operatorname{Spec} N\), whose monoid of global sections is \(N\). The morphism constructed in the proof sends \(\mathfrak{q}\) to the preimage in \(M\) of the non-units of \(N_{\mathfrak{q}}\), which is \(\varphi^{-1}(\mathfrak{q})\). (2) follows from (1). (3) \(\mathbb{F}_1\) is an initial object of the category of monoids, so \(\operatorname{Hom}(\mathbb{F}_1, \mathcal{O}_X(X))\) has one element. \(\square\)

*Reference:* [Deitmar 2005, Proposition 2.2].

**Lemma 1.6 (localizations).** Let \(S\) be a multiplicative subset of a monoid \(M\) and \(\iota\colon M \to S^{-1}M\) the localization.

1. The morphism \(\operatorname{Spec}\iota\colon \operatorname{Spec} S^{-1}M \to \operatorname{Spec} M\) is a homeomorphism onto the set of prime ideals that do not meet \(S\), and all its maps of stalks are isomorphisms.
2. For \(f \in M\), the morphism \(\operatorname{Spec} M_f \to \operatorname{Spec} M\) is an open immersion with image \(D(f)\). So the open subset \(D(f)\), with the restricted sheaf, is isomorphic to \(\operatorname{Spec} M_f\).

*Proof.* (1) By Corollary 1.5 the map of spaces is \(\mathfrak{Q} \mapsto \iota^{-1}(\mathfrak{Q})\), so the statement on the spaces is recalled above. Let \(\mathfrak{Q}\) be a prime ideal of \(S^{-1}M\) and \(\mathfrak{p} = \iota^{-1}(\mathfrak{Q})\). An element \(a/s\) lies in \(\mathfrak{Q}\) if and only if \(a/1 = (a/s)(s/1)\) does, that is, if and only if \(a \in \mathfrak{p}\). By the proof of Theorem 1.4, the map of stalks at \(\mathfrak{Q}\) is the morphism \(M_{\mathfrak{p}} \to (S^{-1}M)_{\mathfrak{Q}}\) induced by \(\iota\). It is an isomorphism if the morphism \(M \to (S^{-1}M)_{\mathfrak{Q}}\) is universal among the morphisms that send \(M \setminus \mathfrak{p}\) to units. It sends \(M \setminus \mathfrak{p}\) to units, because \(\iota(a) \notin \mathfrak{Q}\) for \(a \notin \mathfrak{p}\). Let \(\varphi\colon M \to N\) be a morphism that sends \(M \setminus \mathfrak{p}\) to units. Since \(S \subseteq M \setminus \mathfrak{p}\), it factors through a unique morphism \(\varphi_1\colon S^{-1}M \to N\). If \(a/s \notin \mathfrak{Q}\), then \(a \notin \mathfrak{p}\), so \(\varphi_1(a/s) = \varphi(a)\varphi(s)^{-1}\) is a unit. So \(\varphi_1\) factors through a unique morphism \((S^{-1}M)_{\mathfrak{Q}} \to N\).

(2) By (1) the map of spaces is a homeomorphism onto \(D(f)\). The sets \(D(fg)\), \(g \in M\), form a basis of \(D(f)\), and the preimage of \(D(fg)\) is the basic open subset \(D(g/1)\) of \(\operatorname{Spec} M_f\). On \(D(fg)\) the map of sheaves is the morphism \(M_{fg} \to (M_f)_{g/1}\) induced by \(\iota\) (proof of Theorem 1.4). It is an isomorphism, because both monoids are universal among the morphisms out of \(M\) that send \(f\) and \(g\) to units. A morphism of sheaves that is an isomorphism on a basis is an isomorphism [Stacks, Tag [009H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-bases)]. \(\square\)

## 2. Monoid schemes

**Definition 2.1.** A *monoid scheme* is a monoidal space \((X, \mathcal{O}_X)\) in which every point has an open neighbourhood \(U\) such that \((U, \mathcal{O}_X|_U)\) is an affine monoid scheme. Such a \(U\) is called an *affine open subset*. A morphism of monoid schemes is a morphism of monoidal spaces. The empty space is a monoid scheme; it is \(\operatorname{Spec}\) of the zero monoid.

For a point \(x\) of a monoid scheme we write \(G(x)\) for the set of *generalizations* of \(x\): the points \(y\) with \(x \in \overline{\{y\}}\). Every open set that contains \(x\) contains \(G(x)\).

**Lemma 2.2.** Let \(X\) be a monoid scheme.

1. The affine open subsets form a basis of the topology. Every open subset of \(X\), with the restricted sheaf, is a monoid scheme. The space \(X\) is \(T_0\).
2. For every \(x \in X\) there is a canonical morphism \(i_x\colon \operatorname{Spec}\mathcal{O}_{X,x} \to X\). It maps the closed point to \(x\), it is a homeomorphism onto \(G(x)\), and it induces isomorphisms on all stalks.

*Proof.* (1) If \(U \cong \operatorname{Spec} M\) is an affine open subset, the sets \(D(f) \cong \operatorname{Spec} M_f\) are affine (Lemma 1.6) and form a basis of \(U\). Two different points of \(X\) that lie in a common affine open subset \(\operatorname{Spec} M\) are different prime ideals of \(M\), and these are separated by some \(D(f)\). If no affine open subset contains both points, an affine open neighbourhood of one of them separates them. So \(X\) is \(T_0\). (2) Choose an affine open neighbourhood \(U = \operatorname{Spec} M\) of \(x = \mathfrak{p}\). Then \(\mathcal{O}_{X,x} = M_{\mathfrak{p}}\), and \(i_x\) is \(\operatorname{Spec}(M \to M_{\mathfrak{p}})\) followed by the inclusion of \(U\). By Lemma 1.6 it is a homeomorphism onto \(\{\mathfrak{q} \subseteq \mathfrak{p}\} = G(x) \cap U = G(x)\), and its maps of stalks are isomorphisms. Under Theorem 1.4 the morphism \(\operatorname{Spec}\mathcal{O}_{X,x} \to U\) corresponds to the map \(\mathcal{O}_X(U) \to \mathcal{O}_{X,x}\) that sends a section to its germ at \(x\). If \(U' \subseteq U\) is a smaller affine open neighbourhood of \(x\), the morphism defined with \(U'\), followed by the inclusion of \(U'\) in \(U\), corresponds to the same map. Two affine open neighbourhoods of \(x\) contain a common one by (1). So \(i_x\) does not depend on \(U\). \(\square\)

### Affine open subsets

**Proposition 2.3.** Let \(X\) be a monoid scheme and \(U \subseteq X\) a nonempty open subset. The following are equivalent.

1. \(U\) is affine.
2. There is a point \(x \in U\) such that every point of \(U\) is a generalization of \(x\).

If they hold, then \(U = G(x)\), the point \(x\) is the only closed point of \(U\), the morphism \(i_x\colon \operatorname{Spec}\mathcal{O}_{X,x} \to U\) is an isomorphism, and \(\mathcal{O}_X(U) \to \mathcal{O}_{X,x}\) is an isomorphism. Moreover, every nonempty affine open subset of an affine monoid scheme \(\operatorname{Spec} M\) is of the form \(D(s)\) with \(s \in M\).

*Proof.* (1) implies (2): if \(U \cong \operatorname{Spec} M\), take for \(x\) the closed point and use Lemma 1.1(1). (2) implies (1): let \(V \subseteq U\) be an affine open neighbourhood of \(x\) (Lemma 2.2). Every \(y \in U\) is a generalization of \(x\), so \(y \in V\). Hence \(U = V\) is affine. Now assume (1) and (2). Then \(U \subseteq G(x) \subseteq U\). Write \(U = \operatorname{Spec} M\). The closed point \(\mathfrak{m}_M\) is a generalization of \(x\), and \(x\) lies in its closure \(\{\mathfrak{m}_M\}\); so \(x = \mathfrak{m}_M\). The remaining claims follow from \(M = M_{\mathfrak{m}_M}\). For the last claim, let \(U \subseteq \operatorname{Spec} M\) be a nonempty affine open subset with closed point \(\mathfrak{p}\). There is \(s \in M\) with \(\mathfrak{p} \in D(s) \subseteq U\). Since \(D(s)\) is open and contains \(\mathfrak{p}\), it contains \(G(\mathfrak{p}) = U\). \(\square\)

**Example 2.4 (a unique closed point is not enough).** For \(n \geq 1\) let \(A_n\) be the monoid of monomials \(t_1^{a_1} t_2^{a_2} \cdots\) with finitely many nonzero integer exponents and \(a_i \geq 0\) for \(i \leq n\), together with \(0\). Then \(A_n = A_{n+1}[t_{n+1}^{-1}]\), so \(\operatorname{Spec} A_n\) is the open subset \(D(t_{n+1})\) of \(\operatorname{Spec} A_{n+1}\). Let \(X'\) be the union of the chain \(\operatorname{Spec} A_1 \subset \operatorname{Spec} A_2 \subset \cdots\), a monoid scheme. The prime ideals of \(A_n\) are the ideals generated by a subset of \(\{t_1, \dots, t_n\}\). So the points of \(X'\) are the finite subsets \(I\) of \(\{1, 2, \dots\}\), and \(I'\) lies in the closure of \(I\) if and only if \(I \subseteq I'\). No finite subset is maximal. So \(X'\) has no closed point. The monoid scheme \(X' \sqcup \operatorname{Spec}\mathbb{F}_1\) has exactly one closed point, but it is not affine: it does not satisfy condition (2).

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 2.4] states that an open subscheme is affine if and only if it has a unique closed point. This fails for \(X' \sqcup \operatorname{Spec}\mathbb{F}_1\), so we prove Proposition 2.3. For monoid schemes of finite type the two criteria agree (Proposition 2.6).

### Finite type

**Definition 2.5.** A monoid \(M\) is *finitely generated* if there are \(g_1, \dots, g_n \in M\) such that every nonzero element of \(M\) is a product of the \(g_i\). A monoid scheme is *of finite type* if it has a finite cover by affine open subsets \(\operatorname{Spec} M_i\) with all \(M_i\) finitely generated.

**Proposition 2.6.** Let \(X\) be a monoid scheme of finite type.

1. \(X\) is a finite set.
2. For every \(x \in X\) the set \(U_x := G(x)\) is open. It is the smallest open neighbourhood of \(x\), and \(U_x \cong \operatorname{Spec}\mathcal{O}_{X,x}\). The monoid \(\mathcal{O}_{X,x}\) is finitely generated, and \(\mathcal{O}_{X,x}^\times\) is a finitely generated abelian group.
3. The nonempty affine open subsets of \(X\) are exactly the sets \(U_x\). A nonempty open subset is affine if and only if it has exactly one closed point.

*Proof.* Let \(M\) be generated by \(g_1, \dots, g_n\) and let \(\mathfrak{p}\) be a prime ideal. A nonzero element of \(\mathfrak{p}\) is a product of generators, and one of the factors lies in \(\mathfrak{p}\). So \(\mathfrak{p}\) is generated by the \(g_i\) it contains, and \(M\) has at most \(2^n\) prime ideals. This proves (1).

Let \(s\) be the product of the \(g_i\) that are not in \(\mathfrak{p}\). A prime \(\mathfrak{q}\) does not contain \(s\) if and only if it contains none of these \(g_i\), if and only if \(\mathfrak{q} \subseteq \mathfrak{p}\). So \(D(s) = G(\mathfrak{p})\) is open. Every element of \(M \setminus \mathfrak{p}\) is a product of generators outside \(\mathfrak{p}\), so it divides a power of \(s\). Hence \(M_s = M_{\mathfrak{p}}\), so \(D(s) \cong \operatorname{Spec} M_{\mathfrak{p}}\) by Lemma 1.6, and this monoid is generated by the \(g_i\) and \(s^{-1}\). A unit of a finitely generated monoid is a product of generators, and these generators are units. So the unit group is finitely generated. This proves (2).

(3) By Proposition 2.3 the nonempty affine open subsets are the open sets of the form \(G(x)\). Let \(U\) be open with exactly one closed point \(x\). The space \(U\) is finite and \(T_0\), so the closure in \(U\) of any point contains a closed point of \(U\). Hence every point of \(U\) is a generalization of \(x\), and \(U\) is affine by Proposition 2.3. \(\square\)

### Integral monoid schemes

**Definition 2.7.** A monoid \(M\) is *integral* if \(M \neq 0\) and \(ab = ac\) with \(a \neq 0\) implies \(b = c\). This property is called "cancellative" in [Cortiñas–Haesemeyer–Walker–Weibel 2015] and "integral" in [Deitmar 2008] and [Chu–Lorscheid–Santhanam 2012]. If \(M\) is integral, then \(M \setminus \{0\}\) is a cancellative monoid, and it embeds in its group of fractions \(G\). The ideal \(\{0\}\) is prime, \(M_{\{0\}} = G_0\), and every localization \(M_{\mathfrak{p}}\) is an integral submonoid of \(G_0\) with the same group \(G\).

A monoid scheme is *integral* if all its stalks are integral. Equivalently, \(\mathcal{O}_X(U)\) is integral for every nonempty affine open \(U\).

In this lesson, as in the Stacks project, a connected topological space is nonempty. The empty monoid scheme of
Definition 2.1 is therefore not connected.

**Proposition 2.8.** Let \(X\) be a connected integral monoid scheme.

1. There is a unique point \(\eta \in X\) that lies in every nonempty open subset. The stalk \(\mathcal{O}_{X,\eta}\) is \(G_0\) for an abelian group \(G = G_X\).
2. Every open neighbourhood of a point \(x \in X\) contains \(\eta\), so a germ at \(x\) has a germ at \(\eta\). This *generization map* \(\mathcal{O}_{X,x} \to \mathcal{O}_{X,\eta}\) is injective and identifies \(\mathcal{O}_{X,\eta}\) with the localization of \(\mathcal{O}_{X,x}\) at \(\{0\}\). We regard \(A_x := \mathcal{O}_{X,x}\) as a submonoid of \((G_X)_0\) and put \(S_x := A_x \setminus \{0\}\). Then \(S_x\) is a submonoid of \(G_X\) that generates \(G_X\) as a group.
3. For every nonempty open \(U \subseteq X\) the map \(\mathcal{O}_X(U) \to \mathcal{O}_{X,\eta}\) is injective, with image \(\bigcap_{x \in U} A_x\).

*Proof.* (1) Let \(U = \operatorname{Spec} A\) be a nonempty affine open subset. The point \(\eta_U = \{0\}\) lies in every nonempty open subset of \(U\). Let \(V\) be another such subset with \(U \cap V \neq \emptyset\). Every nonempty open subset of \(U \cap V\) contains \(\eta_U\) and \(\eta_V\). Since \(X\) is \(T_0\), this forces \(\eta_U = \eta_V\). For a point \(\eta\) let \(X_\eta\) be the union of the affine opens \(U\) with \(\eta_U = \eta\). The sets \(X_\eta\) are open, they cover \(X\), and two different ones are disjoint. As \(X\) is connected there is only one. (2) holds in an affine open neighbourhood of \(x\) by Definition 2.7. (3) A section \(s \in \mathcal{O}_X(U)\) is determined by its germs, and the germ at \(x\) maps to the germ at \(\eta\) under the injective map of (2). So \(s\) is determined by its germ at \(\eta\), which lies in every \(A_x\). Conversely let \(g \in \bigcap_{x \in U} A_x\). For each \(x \in U\) the element \(g\) is the germ of a section over a neighbourhood of \(x\) in \(U\). Two such sections have the same germ at \(\eta\), so they agree on the overlap, which is a nonempty open set. They glue to a section over \(U\) with germ \(g\). \(\square\)

### Glueing

**Proposition 2.9.** Let \((X_i)_{i \in I}\) be monoid schemes. For each pair \(i, j\) let \(X_{ij} \subseteq X_i\) be an open subset and \(\varphi_{ij}\colon X_{ij} \to X_{ji}\) an isomorphism, such that \(X_{ii} = X_i\), \(\varphi_{ii} = \mathrm{id}\), \(\varphi_{ij}(X_{ij} \cap X_{il}) = X_{ji} \cap X_{jl}\), and \(\varphi_{jl} \circ \varphi_{ij} = \varphi_{il}\) on \(X_{ij} \cap X_{il}\). Then there are a monoid scheme \(X\) and open immersions \(\psi_i\colon X_i \to X\) with \(X = \bigcup \psi_i(X_i)\), \(\psi_i(X_{ij}) = \psi_i(X_i) \cap \psi_j(X_j)\) and \(\psi_j \circ \varphi_{ij} = \psi_i\) on \(X_{ij}\). The pair \((X, (\psi_i))\) is unique up to a unique isomorphism. Morphisms glue as well: for monoidal spaces \(Z, Y\) the assignment \(U \mapsto \operatorname{Hom}_{\mathsf{MS}}(U, Y)\) is a sheaf on \(Z\).

*Proof.* The proof of [Stacks, Tag [01JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue)], which treats locally ringed spaces, uses only the glueing of topological spaces and the glueing of sheaves [Stacks, Tag [00AK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-glueing-sheaves)]. It applies to sheaves of monoids without change. The glued space is locally isomorphic to the \(X_i\), so it is a monoid scheme. \(\square\)

**Examples 2.10.**

1. *Affine space.* \(\mathbb{A}^n = \operatorname{Spec}\mathbb{F}_1[t_1, \dots, t_n]\), where \(\mathbb{F}_1[t_1,\dots,t_n]\) is the monoid of monomials in \(t_1, \dots, t_n\) together with \(0\). Its prime ideals are the ideals \(\mathfrak{p}_I\) generated by \(\{t_i : i \in I\}\), \(I \subseteq \{1,\dots,n\}\). So \(\mathbb{A}^n\) has \(2^n\) points, and \(\mathfrak{p}_J\) lies in the closure of \(\mathfrak{p}_I\) if and only if \(I \subseteq J\).
2. *Tori and groups.* For an abelian group \(H\) the scheme \(\operatorname{Spec} H_0\) is a single point with stalk \(H_0\). Examples are \(\mathbb{G}_m^n = \operatorname{Spec}\mathbb{F}_1[t_1^{\pm 1}, \dots, t_n^{\pm 1}]\) and \(\operatorname{Spec}\mathbb{F}_{1^n}\).
3. *The projective line.* Glue \(\operatorname{Spec}\mathbb{F}_1[t]\) and \(\operatorname{Spec}\mathbb{F}_1[t^{-1}]\) along \(D(t) = \operatorname{Spec}\mathbb{F}_1[t,t^{-1}] = D(t^{-1})\). The result \(\mathbb{P}^1\) has three points: one point \(\eta\) that lies in every nonempty open set, and two closed points. *Reference:* [Deitmar 2005, Section 2.3].
4. *The line with a doubled origin.* Glue two copies of \(\operatorname{Spec}\mathbb{F}_1[t]\) along \(D(t)\) by the identity. The result \(L\) has the same underlying space as \(\mathbb{P}^1\), and the stalks at corresponding points are isomorphic monoids. But \(L\) and \(\mathbb{P}^1\) are not isomorphic. Both are connected and integral with \(G = t^{\mathbb{Z}}\). For \(\mathbb{P}^1\) the two closed points have \(S_x = \{t^i : i \geq 0\}\) and \(\{t^i : i \leq 0\}\). For \(L\) both closed points have \(S_x = \{t^i : i \geq 0\}\). An isomorphism would induce an automorphism of \(G\) that carries one pair of submonoids to the other. So a monoid scheme is more than a space with stalks: the generization maps matter.

## 3. Points and fibre products

### Points with values in a monoid

For a monoid scheme \(X\) and a monoid \(B\) put \(X(B) = \operatorname{Hom}(\operatorname{Spec} B, X)\). For nonzero monoids \(A, B\) let \(\operatorname{Hom}_{\mathrm{loc}}(A, B)\) be the set of local morphisms.

**Theorem 3.1.** Let \(X\) be a monoid scheme and \(B\) a nonzero monoid, with closed point \(c = \mathfrak{m}_B\) of \(\operatorname{Spec} B\). The map
\[
X(B) \longrightarrow \bigsqcup_{x \in X} \operatorname{Hom}_{\mathrm{loc}}(\mathcal{O}_{X,x}, B), \qquad g \longmapsto \bigl(g(c),\ g^\#_c\colon \mathcal{O}_{X,g(c)} \to B\bigr),
\]
is bijective. Its inverse sends \((x, \psi)\) to \(i_x \circ \operatorname{Spec}\psi\).

*Proof.* Let \(g\colon \operatorname{Spec} B \to X\) be a morphism, \(x = g(c)\), and \(U = \operatorname{Spec} A\) an affine open neighbourhood of \(x\), with \(x = \mathfrak{p}\). The open set \(g^{-1}(U)\) contains \(c\), so it is \(\operatorname{Spec} B\) by Lemma 1.1. So \(g\) factors through \(U\), and by Corollary 1.5 it is \(\operatorname{Spec}\varphi\) for a unique \(\varphi\colon A \to B\), with \(\varphi^{-1}(\mathfrak{m}_B) = \mathfrak{p}\). Then \(\varphi\) sends \(A \setminus \mathfrak{p}\) to units, so it factors uniquely as \(A \to A_{\mathfrak{p}} \xrightarrow{\psi} B\), and \(\psi\) is local. Under \(\mathcal{O}_{X,x} = A_{\mathfrak{p}}\) and \(B = B_{\mathfrak{m}_B}\) the map \(\psi\) is \(g^\#_c\), and \(g = i_x \circ \operatorname{Spec}\psi\). Conversely, for a local \(\psi\colon \mathcal{O}_{X,x} \to B\) the morphism \(i_x \circ \operatorname{Spec}\psi\) maps \(c\) to \(i_x(\psi^{-1}(\mathfrak{m}_B)) = x\), and its map of stalks at \(c\) is \(\psi\). \(\square\)

**Corollary 3.2.** Let \(X\) be a monoid scheme.

1. The map \(X(\mathbb{F}_1) \to X\), \(g \mapsto g(c)\), is a bijection onto the underlying set of \(X\). It is natural in \(X\).
2. For an abelian group \(H\),
\[
X(H_0) = \bigsqcup_{x \in X} \operatorname{Hom}_{\mathrm{groups}}(\mathcal{O}_{X,x}^\times, H), \qquad\text{in particular}\qquad X(\mathbb{F}_{1^n}) = \bigsqcup_{x \in X}\operatorname{Hom}(\mathcal{O}_{X,x}^\times, \mu_n).
\]

*Proof.* A local morphism \(\psi\colon \mathcal{O}_{X,x} \to H_0\) sends units to \(H\) and non-units to \(0\). So it is determined by the group homomorphism \(\psi|_{\mathcal{O}_{X,x}^\times}\). Conversely a group homomorphism \(\chi\colon \mathcal{O}_{X,x}^\times \to H\), extended by \(0\) on the non-units, is a local morphism of monoids, because the non-units form a prime ideal. This gives (2), and (1) is the case \(H = 1\). \(\square\)

*Reference:* [Connes–Consani 2010, Proposition 3.18]; [Deitmar–Koyama–Kurokawa 2008, Lemma 1.3].

**Remark 3.3 (with and without zero).** Let \(A\) be a commutative monoid without zero. The prime ideals of \(A_0\) are the sets \(\mathfrak{p} \cup \{0\}\), where \(\mathfrak{p}\) is a prime ideal of \(A\) in the sense of [Deitmar 2005], the empty ideal included. So the spaces agree. The morphisms do not. A morphism \(A_0 \to B_0\) may send nonzero elements to \(0\), and \(\operatorname{Hom}(A, B)\) is only a subset of \(\operatorname{Hom}(A_0, B_0)\). For example, in [Deitmar 2005] the field with one element is the trivial monoid \(\{1\}\), and [Deitmar 2005, Proposition 2.4] shows that \(X(\mathbb{F}_1)\) is the set of connected components of \(X\). With zero, \(X(\mathbb{F}_1)\) is the set of all points of \(X\), by Corollary 3.2. For \(X = \mathbb{A}^n\) this is one point in the first convention and \(2^n\) points in the second. Point counts over finite fields are not affected, because the multiplicative monoid of a field has a zero in both conventions.

### Fibre products

We first record that representable functors glue. Call a functor \(F\colon \mathsf{MS}^{\mathrm{op}} \to \mathsf{Sets}\) a *sheaf* if for every monoidal space \(Z\) the assignment \(U \mapsto F(U)\) is a sheaf on \(Z\). A subfunctor \(F' \subseteq F\) is *open* if for every \(Z\) and every \(\xi \in F(Z)\) there is an open subset \(Z_\xi \subseteq Z\) such that, for every morphism \(h\colon Z' \to Z\), the element \(h^*\xi\) lies in \(F'(Z')\) if and only if \(h(Z') \subseteq Z_\xi\).

**Lemma 3.4.** Let \(F\colon \mathsf{MS}^{\mathrm{op}} \to \mathsf{Sets}\) be a sheaf and \((F_i)_{i \in I}\) open subfunctors. Assume that each \(F_i\) is representable by a monoid scheme \(X_i\), and that for every \(Z\) and \(\xi \in F(Z)\) the open sets \(Z_{\xi,i}\) cover \(Z\). Then \(F\) is representable by a monoid scheme \(X\), and \(X\) has an open cover by subschemes isomorphic to the \(X_i\).

*Proof.* This is the argument of [Stacks, Tag [01JJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue-functors)]. Let \(\xi_i \in F_i(X_i)\) be the universal element. The openness of \(F_j\), applied to \(\xi_i\), gives an open \(X_{ij} \subseteq X_i\) that represents \(F_i \cap F_j\). By the Yoneda lemma there is a unique isomorphism \(\varphi_{ij}\colon X_{ij} \to X_{ji}\) with \(\varphi_{ij}^*\xi_j = \xi_i\). In the same way \(X_{ij} \cap X_{il}\) represents \(F_i \cap F_j \cap F_l\), which gives the conditions of Proposition 2.9. Let \(X\) be the glued monoid scheme. The \(\xi_i\) agree on the overlaps, so they glue to \(\xi \in F(X)\), because \(F\) is a sheaf. Given \(Z\) and \(\zeta \in F(Z)\), the restriction of \(\zeta\) to \(Z_{\zeta,i}\) lies in \(F_i\), so it is \(h_i^*\xi_i\) for a unique \(h_i\colon Z_{\zeta,i} \to X_i\). On overlaps \(h_i\) and \(h_j\) agree, by the universal property of \(X_{ij}\). They glue to \(h\colon Z \to X\) with \(h^*\xi = \zeta\). For uniqueness, note first that \(X_i\) is the open subset of \(X\) attached to \(\xi\) and \(F_i\): it contains \(X_i\) because \(\xi|_{X_i} = \xi_i\), and its intersection with each \(X_j\) lies in \(X_{ji} = X_j \cap X_i\) by the choice of \(X_{ji}\). So if \(h'\colon Z \to X\) is another morphism with \(h'^*\xi = \zeta\), then \(h'^{-1}(X_i) = Z_{\zeta,i}\), and \(h' = h_i\) there. Hence \(h' = h\). \(\square\)

**The tensor product.** Let \(C \to A\) and \(C \to B\) be morphisms of monoids. Let \(A \otimes_C B\) be the quotient of the product monoid \(A \times B\) by the congruence generated by \((ac, b) \sim (a, cb)\) for \(c \in C\). The class of \((a,b)\) is written \(a \otimes b\). Taking \(c = 0\) shows that all pairs with a zero coordinate are identified; their class is the zero. With \(a \mapsto a \otimes 1\) and \(b \mapsto 1 \otimes b\) this is the pushout of \(A \leftarrow C \to B\) in the category of monoids: if \(u\colon A \to P\) and \(v\colon B \to P\) agree on \(C\), then \((a,b) \mapsto u(a)v(b)\) is a morphism \(A \times B \to P\) that is constant on the generating relations. For \(C = \mathbb{F}_1\) no other pairs are identified, and \(A \otimes_{\mathbb{F}_1} B\) is the set of pairs of nonzero elements together with \(0\).

**Theorem 3.5.** Let \(f\colon X \to S\) and \(g\colon Y \to S\) be morphisms of monoid schemes.

1. The fibre product \(X \times_S Y\) exists in the category of monoid schemes. It is also a fibre product in \(\mathsf{MS}\). If \(X = \operatorname{Spec} A\), \(Y = \operatorname{Spec} B\) and \(S = \operatorname{Spec} C\), then \(X \times_S Y = \operatorname{Spec}(A \otimes_C B)\).
2. The map from the underlying space of \(X \times_S Y\) to the fibre product of the underlying spaces of \(X\) and \(Y\) over that of \(S\) is a homeomorphism.

*Proof.* (1) In the affine case, Theorem 1.4 gives for every monoidal space \(Z\)
\[
\operatorname{Hom}(Z, \operatorname{Spec}(A\otimes_C B)) = \operatorname{Hom}(A \otimes_C B, \mathcal{O}_Z(Z)) = \operatorname{Hom}(Z, X) \times_{\operatorname{Hom}(Z,S)} \operatorname{Hom}(Z, Y).
\]
In general let \(F(Z) = \operatorname{Hom}(Z, X) \times_{\operatorname{Hom}(Z,S)} \operatorname{Hom}(Z,Y)\). It is a sheaf because morphisms glue. For affine opens \(W \subseteq S\), \(U \subseteq f^{-1}(W)\) and \(V \subseteq g^{-1}(W)\) let \(F_{U,V,W}(Z)\) be the set of pairs \((a, b) \in F(Z)\) with \(a(Z) \subseteq U\) and \(b(Z) \subseteq V\). By the affine case it is representable by \(\operatorname{Spec}(\mathcal{O}_X(U) \otimes_{\mathcal{O}_S(W)} \mathcal{O}_Y(V))\). It is an open subfunctor, with \(Z_{(a,b)} = a^{-1}(U) \cap b^{-1}(V)\). For \(z \in Z\) choose \(W\) around the image of \(z\) in \(S\), then \(U\) around \(a(z)\) and \(V\) around \(b(z)\). So these open sets cover \(Z\), and Lemma 3.4 applies.

(2) Let \(p\) and \(q\) be the projections of \(X \times_S Y\). By Corollary 3.2(1) and the universal property,
\[
(X \times_S Y)(\mathbb{F}_1) = X(\mathbb{F}_1) \times_{S(\mathbb{F}_1)} Y(\mathbb{F}_1),
\]
so \(z \mapsto (p(z), q(z))\) is a bijection onto the fibre product of sets. It is continuous. The open subschemes \(p^{-1}(U) \cap q^{-1}(V) = \operatorname{Spec}(A \otimes_C B)\) from (1) cover \(X \times_S Y\). In such a subscheme every element is of the form \(a \otimes b = (a \otimes 1)(1 \otimes b)\), so \(D(a \otimes b) = p^{-1}(D(a)) \cap q^{-1}(D(b))\). Hence the image of a basic open set is the intersection of the fibre product with \(D(a) \times D(b)\), which is open. So the map is open. \(\square\)

*Reference:* [Deitmar 2005, Proposition 3.1] for (1); [Cortiñas–Haesemeyer–Walker–Weibel 2015, Proposition 3.1] for (2).

Part (2) has no analogue for schemes. For example \(\mathbb{A}^1 \times \mathbb{A}^1 = \mathbb{A}^2\) has \(4 = 2 \cdot 2\) points, while the affine plane over a field has many points that are not pairs of points of the line.

### Separated monoid schemes

**Definition 3.6.** A monoid scheme \(X\) is *separated* if for all affine open subsets \(U, V \subseteq X\) the intersection \(U \cap V\) is affine and the morphism
\[
\mathcal{O}_X(U) \otimes_{\mathbb{F}_1} \mathcal{O}_X(V) \longrightarrow \mathcal{O}_X(U \cap V), \qquad a \otimes b \longmapsto a|_{U\cap V}\cdot b|_{U \cap V},
\]
is surjective.

This is the form of the definition that [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)] proves to be equivalent to separatedness for schemes. [Cortiñas–Haesemeyer–Walker–Weibel 2015, Definition 3.3] asks instead that the diagonal be a closed immersion; by [Cortiñas–Haesemeyer–Walker–Weibel 2015, Corollary 3.7] the two definitions agree for monoid schemes of finite type. We do not use this.

**Examples 3.7.**

1. An affine monoid scheme \(\operatorname{Spec} M\) is separated. By Proposition 2.3 two nonempty affine open subsets are \(D(s)\) and \(D(t)\). Their intersection is \(D(st)\), and \(M_s \otimes M_t \to M_{st}\) is surjective.
2. \(\mathbb{P}^1\) is separated. Its nonempty affine open subsets are the two charts and \(\{\eta\}\) (Proposition 2.6). If one of two affine open subsets contains the other, the condition of Definition 3.6 holds. For the two charts, \(\mathbb{F}_1[t] \otimes \mathbb{F}_1[t^{-1}] \to \mathbb{F}_1[t, t^{-1}]\) is surjective.
3. The line with a doubled origin \(L\) is not separated: for its two charts the image of \(\mathbb{F}_1[t] \otimes \mathbb{F}_1[t] \to \mathbb{F}_1[t,t^{-1}]\) is \(\mathbb{F}_1[t]\).
4. The intersection of two affine open subsets need not be affine. Glue two copies of \(\mathbb{A}^2\) along the open subset \(U = D(t_1) \cup D(t_2)\) by the identity. The two charts are affine and their intersection is \(U\), which has two closed points and is not affine (Exercise 4). *Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Example 3.5]. [Chu–Lorscheid–Santhanam 2012, Section 3.1.2] states that the intersection of two affine open subsets of an \(\mathcal{M}_0\)-scheme is always affine; this fails for the present example, so Definition 3.6 contains it as a condition.

### Integral monoid schemes from families of submonoids

Most examples in this lesson are connected and integral. Such a scheme can be written down as a family of submonoids of one group. For a submonoid \(S\) of an abelian group \(G\) and \(a \in S\) we write \(S[a^{-1}] = \{s a^{-m} : s \in S,\ m \geq 0\}\), and \(SS' = \{ss'\}\) for two submonoids.

**Lemma 3.8.** Let \(G\) be a finitely generated abelian group. Let \((S_i)_{i \in I}\) be a finite nonempty family of finitely generated submonoids of \(G\), each of which generates \(G\) as a group. Assume that for all \(i, j \in I\) there is \(a \in S_i\) with \(S_iS_j = S_i[a^{-1}]\).

1. There are a connected integral monoid scheme \(X\) of finite type, an isomorphism \(\mathcal{O}_{X,\eta} \cong G_0\), and an affine open cover \((X_i)_{i \in I}\) of \(X\), such that inside \(G_0\) we have \(\mathcal{O}_X(X_i) = (S_i)_0\), and \(X_i \cap X_j\) is affine with \(\mathcal{O}_X(X_i \cap X_j) = (S_iS_j)_0\).
2. \(X\) is separated.
3. If \(X'\) with \((X'_i)_{i\in I}\) has the same properties, there is an isomorphism \(X \to X'\) that maps \(X_i\) onto \(X'_i\) and induces the identity of \(G_0\).

*Proof.* (1) Put \(X_i = \operatorname{Spec}(S_i)_0\). For \(i, j\) choose \(a\) with \(S_iS_j = S_i[a^{-1}]\) and put \(X_{ij} = D(a) \subseteq X_i\). This is the image of \(\operatorname{Spec}(S_iS_j)_0 \to X_i\), so it does not depend on \(a\), and \(X_{ij} \cong \operatorname{Spec}(S_iS_j)_0 \cong X_{ji}\). Let \(\varphi_{ij}\) be this isomorphism. For three indices, \(X_{ij} \cap X_{il}\) is a principal open subset of \(X_i\) with monoid \((S_iS_jS_l)_0\), and so is \(X_{ji} \cap X_{jl}\) in \(X_j\). All the maps are induced by identities between submonoids of \(G_0\), so the conditions of Proposition 2.9 hold. Let \(X\) be the glued scheme. Its stalks are localizations of the \((S_i)_0\), so it is integral. It is of finite type. Each \(X_i\) is connected and \(X_i \cap X_j \neq \emptyset\), so \(X\) is connected. The stalk of every \(X_i\) at \(\{0\}\) is \(G_0\).

(2) Let \(U, V\) be nonempty affine open subsets of \(X\), with closed points \(x \in X_i\) and \(y \in X_j\). By Propositions 2.3 and 2.6, \(U = D(b) \subseteq X_i\) and \(V = D(c) \subseteq X_j\) with \(b \in S_i\), \(c \in S_j\). Inside \(X_i \cap X_j = \operatorname{Spec}(S_iS_j)_0\) the set \(U \cap V\) is \(D(bc)\). It is affine, and its monoid of sections is generated by \(S_i[b^{-1}]\) and \(S_j[c^{-1}]\). So the map of Definition 3.6 is surjective.

(3) The identifications \(X_i = \operatorname{Spec}(S_i)_0 = X'_i\) agree on \(X_i \cap X_j\), which on both sides is the same principal open subset of \(\operatorname{Spec}(S_i)_0\). They glue by Proposition 2.9. \(\square\)

**Proposition 3.9.** Let \(X\) be a connected integral monoid scheme of finite type. Let \(G = G_X\), and let \(S_x \subseteq G\), for \(x \in X\), be the submonoids of Proposition 2.8.

1. \(X\) is separated if and only if for all \(x, y \in X\) there is \(z \in X\) with \(U_x \cap U_y = U_z\) and \(S_z = S_xS_y\).
2. If \(X\) is separated, then the map \(x \mapsto S_x\) is injective, the family \((S_x)_{x \in X}\) satisfies the hypotheses of Lemma 3.8, and \(X\) with the cover \((U_x)\) is the monoid scheme of that lemma.
3. Two separated connected integral monoid schemes of finite type \(X\) and \(X'\) are isomorphic if and only if there is a group isomorphism \(\psi\colon G_{X'} \to G_X\) such that \(\{\psi(S_{x'}) : x' \in X'\} = \{S_x : x \in X\}\). Every such \(\psi\) is induced by an isomorphism \(X \to X'\).

*Proof.* (1) By Proposition 2.6 the nonempty affine open subsets are the \(U_x\). The set \(U_x \cap U_y\) contains \(\eta\), so it is affine if and only if it is \(U_z\) for some \(z\). The map \(A_x \otimes A_y \to A_z\), \(a \otimes b \mapsto ab\), is surjective if and only if \(S_z = S_xS_y\).

(2) Let \(S_x = S_y\), and let \(U_x \cap U_y = U_z\) with \(S_z = S_xS_y = S_x\). By Proposition 2.3, \(U_z = D(t)\) in \(U_x = \operatorname{Spec} A_x\) for some \(t \in S_x\), and \(S_z = S_x[t^{-1}]\). So \(t^{-1} \in S_x\), hence \(D(t) = U_x\) and \(z = x\). In the same way \(z = y\). The groups \(G\) and the monoids \(S_x\) are finitely generated by Proposition 2.6, and \(S_xS_y = S_z = S_x[t^{-1}]\). So Lemma 3.8 applies, and \(X\) with the cover \((U_x)\) has the properties listed there.

(3) An isomorphism \(h\colon X \to X'\) maps \(\eta\) to \(\eta'\). Its map of stalks at \(\eta\) restricts to a group isomorphism \(\psi\), and \(\psi(S_{h(x)}) = S_x\) because the maps of stalks commute with the generization maps. Conversely, given \(\psi\), use it to identify \(G_{X'}\) with \(G_X\). By (2), both \(X\) and \(X'\) are then the monoid scheme attached to the same family of submonoids of \(G_X\). Lemma 3.8(3) gives an isomorphism \(X \to X'\) that induces the identity of \((G_X)_0\) after this identification, that is, it induces \(\psi\). \(\square\)

**Example 3.10 (injectivity is not enough).** Glue \(\operatorname{Spec}\mathbb{F}_1[t]\) and \(\operatorname{Spec}\mathbb{F}_1[t^2,t^3]\) along their generic points \(D(t)\) and \(D(t^2)\), which are both \(\operatorname{Spec}\mathbb{F}_1[t,t^{-1}]\). Here \(\mathbb{F}_1[t^2,t^3]\) is the monoid of the \(t^i\) with \(i \neq 1\), together with \(0\). The result \(X\) is connected, integral and of finite type. The spectrum of \(\mathbb{F}_1[t^2,t^3]\) has two points (Exercise 2). So \(X\) has three points \(\eta, c_1, c_2\), with \(S_{c_1} = \{t^i : i \geq 0\}\) and \(S_{c_2} = \{t^i : i = 0 \text{ or } i \geq 2\}\). So \(x \mapsto S_x\) is injective. But \(X\) is not separated: \(U_{c_1} \cap U_{c_2} = U_\eta\), and \(S_{c_1}S_{c_2} = S_{c_1} \neq S_\eta\). Its base change \(X_{\mathbb{Z}}\) to the integers (Section 4) is not separated either: it is glued from \(\operatorname{Spec}\mathbb{Z}[t]\) and \(\operatorname{Spec}\mathbb{Z}[t^2,t^3]\) along \(\operatorname{Spec}\mathbb{Z}[t,t^{-1}]\), and \(\mathbb{Z}[t] \otimes \mathbb{Z}[t^2,t^3] \to \mathbb{Z}[t,t^{-1}]\) is not surjective [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)].

*Reference:* [Chu–Lorscheid–Santhanam 2012, Section 3.1.2] calls \(X\) separated if \(X_{\mathbb{Z}}\) is separated, and conjectures that this is equivalent to the following condition: two points \(x, y\) with a common generalization \(z\) are equal if \(\mathcal{O}_{X,x}\) and \(\mathcal{O}_{X,y}\) have the same image in \(\mathcal{O}_{X,z}\). The scheme \(X\) of Example 3.10 satisfies this condition, and \(X_{\mathbb{Z}}\) is not separated. So the condition is not sufficient. A connected integral monoid scheme of finite type that is separated in the sense of Definition 3.6 satisfies the condition, by Proposition 3.9(2) and because the generization maps are injective.

## 4. Base change to rings and point counts

### The monoid algebra

Let \(k\) be a ring and \(M\) a monoid. For every \(k\)-algebra \(R\), restriction to \(M\) gives a bijection
\[
\operatorname{Hom}_{k\text{-alg}}(k[M], R) = \operatorname{Hom}(M, (R,\cdot)). \tag{4.1}
\]
So \(M \mapsto \mathbb{Z}[M]\) is left adjoint to \(R \mapsto (R,\cdot)\). *Reference:* [Deitmar 2005, Theorem 1.1]. Since both sides represent the same functor, (4.1) gives
\[
k[S^{-1}M] = S^{-1}k[M], \qquad k[A \otimes_C B] = k[A] \otimes_{k[C]} k[B], \qquad k[M] = k \otimes_{\mathbb{Z}} \mathbb{Z}[M].
\]

### The base change

Recall the functor \(Y \mapsto Y^{\mathrm{mon}}\) of Examples 1.3.

**Theorem 4.1.** Let \(X\) be a monoid scheme.

1. The functor \(Y \mapsto \operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, X)\) on the category of schemes is representable by a scheme \(X_{\mathbb{Z}}\). So there is a morphism \(\beta\colon (X_{\mathbb{Z}})^{\mathrm{mon}} \to X\) such that, for every scheme \(Y\), the map \(g \mapsto \beta \circ g^{\mathrm{mon}}\) is a bijection from \(\operatorname{Hom}(Y, X_{\mathbb{Z}})\) to \(\operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, X)\).
2. \((\operatorname{Spec} M)_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[M]\), and \(\beta(P) = P \cap M\) for a prime ideal \(P\) of \(\mathbb{Z}[M]\).
3. For an open \(U \subseteq X\), the open subscheme \(\beta^{-1}(U)\) of \(X_{\mathbb{Z}}\), with the restriction of \(\beta\), is \(U_{\mathbb{Z}}\). So \(U_{\mathbb{Z}} \cap V_{\mathbb{Z}} = (U \cap V)_{\mathbb{Z}}\) for open subsets \(U, V \subseteq X\), and the \(U_{\mathbb{Z}}\) cover \(X_{\mathbb{Z}}\) when the \(U\) cover \(X\). In particular \(X_{\mathbb{Z}}\) is covered by the affine open subschemes \(U_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[\mathcal{O}_X(U)]\), for \(U \subseteq X\) affine open.
4. \(X \mapsto X_{\mathbb{Z}}\) is a functor from monoid schemes to schemes. For a morphism \(h\colon X \to X'\), with \(\beta'\) the morphism of (1) for \(X'\), we have \(\beta' \circ (h_{\mathbb{Z}})^{\mathrm{mon}} = h \circ \beta\). The base change of the inclusion of an open subset \(U \subseteq X\) is the inclusion of \(U_{\mathbb{Z}}\) in \(X_{\mathbb{Z}}\).

For a ring \(k\) put \(X_k = X_{\mathbb{Z}} \times_{\operatorname{Spec}\mathbb{Z}} \operatorname{Spec} k\), the *base change* of \(X\) to \(k\). Then \(\operatorname{Hom}_k(Y, X_k) = \operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, X)\) for every \(k\)-scheme \(Y\), \((\operatorname{Spec} M)_k = \operatorname{Spec} k[M]\), and (3) and (4) hold for \(X_k\). We write \(\beta\) also for the map \(X_k \to X\).

*Proof.* (2) For a scheme \(Y\), Theorem 1.4, the adjunction (4.1) and [Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)] give
\[
\operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, \operatorname{Spec} M) = \operatorname{Hom}(M, (\mathcal{O}_Y(Y),\cdot)) = \operatorname{Hom}(\mathbb{Z}[M], \mathcal{O}_Y(Y)) = \operatorname{Hom}(Y, \operatorname{Spec}\mathbb{Z}[M]).
\]
The universal morphism \(\beta\) corresponds to the inclusion \(M \to \mathbb{Z}[M]\). By the construction in the proof of Theorem 1.4, \(\beta(P)\) is the preimage in \(M\) of the maximal ideal of \(\mathbb{Z}[M]_P\), which is \(P \cap M\).

(1) Let \(F_X(Y) = \operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, X)\). It is a sheaf for the Zariski topology, because morphisms of monoidal spaces glue. For an open \(U \subseteq X\) let \(F_U \subseteq F_X\) be the subfunctor of morphisms with image in \(U\). Let \(g \in F_X(Y)\). A morphism of schemes \(h\colon Y' \to Y\) satisfies \(g \circ h^{\mathrm{mon}} \in F_U(Y')\) if and only if \(h(Y') \subseteq g^{-1}(U)\). So \(F_U \subseteq F_X\) is representable by open immersions. For affine \(U\) the functor \(F_U\) is representable by (2). The open sets \(g^{-1}(U)\), for \(U\) affine, cover \(Y\). By [Stacks, Tag [01JJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue-functors)], \(F_X\) is representable.

(3) Apply the last argument to \(g = \beta\): the open subscheme \(\beta^{-1}(U)\) represents \(F_U\). A morphism to \(X\) with image in \(U\) is the same as a morphism to the open subspace \(U\), so \(F_U(Y) = \operatorname{Hom}_{\mathsf{MS}}(Y^{\mathrm{mon}}, U)\), and \(\beta^{-1}(U)\) is \(U_{\mathbb{Z}}\). The other statements follow, because \(\beta^{-1}\) commutes with intersections and unions. (4) A morphism \(h\colon X \to X'\) induces a morphism of functors \(F_X \to F_{X'}\), hence a morphism \(h_{\mathbb{Z}}\colon X_{\mathbb{Z}} \to X'_{\mathbb{Z}}\) by the Yoneda lemma. It is the morphism that corresponds to the element \(h \circ \beta\) of \(F_{X'}(X_{\mathbb{Z}})\), that is, \(\beta' \circ (h_{\mathbb{Z}})^{\mathrm{mon}} = h \circ \beta\). For the inclusion of an open subset \(U\), the morphism of functors is the inclusion of \(F_U\) in \(F_X\), which corresponds to the inclusion of \(\beta^{-1}(U)\). The statements for \(k\) follow from the universal property of the fibre product and from \(k[M] = k \otimes \mathbb{Z}[M]\). \(\square\)

By (3) and (4), for every affine open cover \((U_i)\) of \(X\) the scheme \(X_{\mathbb{Z}}\) is glued from the affine schemes \(\operatorname{Spec}\mathbb{Z}[\mathcal{O}_X(U_i)]\) along the open subschemes \((U_i \cap U_j)_{\mathbb{Z}}\). This is the description in [Deitmar 2005, Section 2.3]. A functor of points is used in [Cortiñas–Haesemeyer–Walker–Weibel 2015, Theorem 5.2].

**Proposition 4.2.** Let \(X\) be a monoid scheme and \(k\) a nonzero ring.

1. Let \(R\) be a \(k\)-algebra that is a local ring. The map that sends \(g \in X_k(R)\) to the image \(x\) of the closed point and the map of stalks \(\mathcal{O}_{X,x} \to (R,\cdot)\) is a bijection
\[
X_k(R) = \bigsqcup_{x \in X} \operatorname{Hom}_{\mathrm{loc}}(\mathcal{O}_{X,x}, (R,\cdot)) = X((R,\cdot)).
\]
For a field \(K\) over \(k\) this gives \(X_k(K) = \bigsqcup_{x \in X}\operatorname{Hom}(\mathcal{O}_{X,x}^\times, K^\times)\).
2. The map \(\beta\colon X_k \to X\) is surjective.
3. \((X \times_S Y)_k = X_k \times_{S_k} Y_k\) for morphisms \(X \to S\) and \(Y \to S\) of monoid schemes.
4. \(X\) is of finite type if and only if \(X_k\) is of finite type over \(k\).
5. If \(X\) is separated, then \(X_k\) is separated over \(k\).

*Proof.* (1) We have \(X_k(R) = \operatorname{Hom}_{\mathsf{MS}}((\operatorname{Spec} R)^{\mathrm{mon}}, X)\). Let \(g\) be such a morphism, \(x\) the image of the closed point, and \(U = \operatorname{Spec} A\) an affine open neighbourhood of \(x\). Every nonempty closed subset of \(\operatorname{Spec} R\) contains the closed point, so \(g^{-1}(U) = \operatorname{Spec} R\). By Theorem 1.4, \(g\) corresponds to a morphism \(\varphi\colon A \to (R,\cdot)\), and the preimage of the non-units of \(R\) is the prime ideal of \(x\). As in the proof of Theorem 3.1, \(\varphi\) factors through a unique local morphism \(\psi\colon \mathcal{O}_{X,x} \to (R,\cdot)\), and \(g\) is recovered from \((x, \psi)\). Conversely every pair \((x, \psi)\) arises: compose the morphism \((\operatorname{Spec} R)^{\mathrm{mon}} \to \operatorname{Spec}\mathcal{O}_{X,x}\) that Theorem 1.4 attaches to \(\psi\) with \(i_x\). The second equality is Theorem 3.1, and the statement for fields is Corollary 3.2, because \((K,\cdot) = (K^\times)_0\).

(2) Let \(x \in X\). Since \(k \neq 0\), there is a field \(K\) with a ring homomorphism \(k \to K\). The map \(\mathcal{O}_{X,x} \to (K,\cdot)\) that sends units to \(1\) and non-units to \(0\) is a local morphism. By (1) it is a point of \(X_k(K)\), and \(\beta\) maps its image to \(x\).

(3) For a \(k\)-scheme \(T\), Theorem 3.5(1) gives \(\operatorname{Hom}_{\mathsf{MS}}(T^{\mathrm{mon}}, X \times_S Y) = \operatorname{Hom}(T^{\mathrm{mon}}, X) \times_{\operatorname{Hom}(T^{\mathrm{mon}}, S)} \operatorname{Hom}(T^{\mathrm{mon}}, Y)\). So both sides of (3) represent the same functor.

(4) If \(X\) is covered by finitely many \(\operatorname{Spec} M_i\) with \(M_i\) finitely generated, then \(X_k\) is covered by the \(\operatorname{Spec} k[M_i]\), and \(k[M_i]\) is a finitely generated \(k\)-algebra. Conversely let \(X_k\) be of finite type. It is quasi-compact, so finitely many open sets \((U_i)_k\), with \(U_i \subseteq X\) affine, cover it. By (2) the \(U_i\) cover \(X\). Let \(M_i = \mathcal{O}_X(U_i)\). The ring \(k[M_i]\) is a finitely generated \(k\)-algebra [Stacks, Tag [01T2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-type-characterize)]. Finitely many generators involve only a finite subset \(T_i \subseteq M_i \setminus \{0\}\). Every nonzero \(a \in M_i\) is then a \(k\)-linear combination of products of elements of \(T_i\). These products lie in \(M_i\), and \(M_i \setminus \{0\}\) is a basis of \(k[M_i]\). So \(a\) is one of these products, and \(T_i\) generates \(M_i\).

(5) The affine open subschemes \(U_k\), for \(U \subseteq X\) affine open, cover \(X_k\). For two of them, \(U_k \cap V_k = (U \cap V)_k\) is affine, and \(k[\mathcal{O}_X(U)] \otimes_{\mathbb{Z}} k[\mathcal{O}_X(V)] \to k[\mathcal{O}_X(U \cap V)]\) is surjective, because every basis element of the target is a product \(a|_{U \cap V} \cdot b|_{U\cap V}\). By [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)], \(X_k\) is separated over \(k\). \(\square\)

*Reference:* (4), for \(k = \mathbb{Z}\), is [Deitmar 2006, Lemma 2]. The converse of (5) is stated in general in [Cortiñas–Haesemeyer–Walker–Weibel 2015, Proposition 5.13], where a monoid scheme is called separated if its diagonal is a closed immersion; it fails in general (Section 10 gives an example), and we prove it for connected integral torsion-free monoid schemes of finite type in Proposition 6.6.

For a prime power \(q\) let \(N_X(q)\) be the number of \(\mathbb{F}_q\)-points of \(X_{\mathbb{Z}}\). The group \(\mathbb{F}_q^\times\) is cyclic of order \(q - 1\), so \((\mathbb{F}_q,\cdot) \cong \mathbb{F}_{1^{q-1}}\), and Proposition 4.2(1) gives
\[
X_{\mathbb{Z}}(\mathbb{F}_q) = X(\mathbb{F}_{1^{q-1}}), \qquad N_X(q) = \# X(\mathbb{F}_{1^{q-1}}). \tag{4.2}
\]
So the monoids \(\mathbb{F}_{1^n}\) play the role of the finite fields, and they do so for every \(n\), not only for \(n = q - 1\). *Reference:* [Deitmar–Koyama–Kurokawa 2008, Section 2].

**Remark 4.3 (the other direction).** By (4.1), \(\operatorname{Hom}(\operatorname{Spec} R, (\operatorname{Spec} M)_{\mathbb{Z}}) = \operatorname{Hom}(\operatorname{Spec}(R,\cdot), \operatorname{Spec} M)\) for a ring \(R\) and a monoid \(M\). For a ring \(R\) there is a canonical morphism \((\operatorname{Spec} R)^{\mathrm{mon}} \to \operatorname{Spec}(R,\cdot)\), by Theorem 1.4. On points it sends a prime ideal of the ring \(R\) to the same set, which is a prime ideal of the monoid \((R,\cdot)\). It is not an isomorphism in general, and \(R \mapsto \operatorname{Spec}(R,\cdot)\) does not take open covers to open covers. For example \(\operatorname{Spec}\mathbb{Z} = D(2) \cup D(3)\). The monoid schemes \(\operatorname{Spec}(\mathbb{Z}[1/2],\cdot)\) and \(\operatorname{Spec}(\mathbb{Z}[1/3],\cdot)\) are the open subsets \(D(2)\) and \(D(3)\) of \(\operatorname{Spec}(\mathbb{Z},\cdot)\). They do not cover it, because the closed point \(\mathbb{Z} \setminus \{1, -1\}\) contains \(2\) and \(3\). Their union has the two closed points \(\mathbb{Z} \setminus \{\pm 2^i\}\) and \(\mathbb{Z} \setminus \{\pm 3^i\}\), so it is not affine.

*Reference:* [Deitmar 2005, Section 2.3] extends \(R \mapsto \operatorname{Spec}(R,\cdot)\) to all schemes by glueing over an affine cover and states that the result does not depend on the cover. This fails for the covers \(\{\operatorname{Spec}\mathbb{Z}\}\) and \(\{D(2), D(3)\}\) of \(\operatorname{Spec}\mathbb{Z}\), which give \(\operatorname{Spec}(\mathbb{Z},\cdot)\) and \(D(2) \cup D(3)\). The statement that holds for all schemes is Theorem 4.1(1).

### Counting points

**Theorem 4.4.** Let \(X\) be a monoid scheme of finite type. For \(x \in X\) write \(\mathcal{O}_{X,x}^\times \cong \mathbb{Z}^{r(x)} \times T_x\) with \(T_x\) finite (Proposition 2.6), and put \(h_x(n) = \#\operatorname{Hom}(T_x, \mu_n)\). Then, for every \(n \geq 1\) and every prime power \(q\),
\[
\# X(\mathbb{F}_{1^n}) = \sum_{x \in X} n^{r(x)}\, h_x(n), \qquad N_X(q) = \sum_{x \in X} (q-1)^{r(x)}\, h_x(q-1).
\]
If \(T_x \cong \bigoplus_j \mathbb{Z}/d_j\), then \(h_x(n) = \prod_j \gcd(d_j, n)\).

*Proof.* By Corollary 3.2, \(X(\mathbb{F}_{1^n})\) is the disjoint union of the sets \(\operatorname{Hom}(\mathbb{Z}^{r(x)} \times T_x, \mu_n)\), which have \(n^{r(x)} h_x(n)\) elements. A homomorphism \(\mathbb{Z}/d \to \mu_n\) is an element of \(\mu_n\) of order dividing \(d\), and a cyclic group of order \(n\) has \(\gcd(d,n)\) such elements. The formula for \(N_X(q)\) follows from (4.2). \(\square\)

*Reference:* [Deitmar–Koyama–Kurokawa 2008, Lemma 1.3 and the proof of Proposition 2.1].

**Corollary 4.5.** Let \(X\) be of finite type. Let \(e_X\) be the least common multiple of the exponents of the groups \(T_x\), and put
\[
P_X(t) = \sum_{x \in X} t^{r(x)} \in \mathbb{Z}[t].
\]

1. If \(\gcd(n, e_X) = 1\), then \(\# X(\mathbb{F}_{1^n}) = P_X(n)\).
2. If \(q\) is a prime power with \(\gcd(q-1, e_X) = 1\), then \(N_X(q) = P_X(q-1)\).
3. For every \(e \geq 1\) there are infinitely many prime powers \(q\) with \(\gcd(q-1,e) = 1\). So \(P_X(t-1)\) is the only polynomial \(N(t)\) for which there is an \(e \geq 1\) such that \(N_X(q) = N(q)\) whenever \(\gcd(q-1,e) = 1\).

*Proof.* Let \(\gcd(n,e_X) = 1\). Every element in the image of a homomorphism \(T_x \to \mu_n\) has an order that divides both \(e_X\) and \(n\). So the homomorphism is trivial and \(h_x(n) = 1\). This gives (1) and (2). For (3) write \(e = 2^a e'\) with \(e'\) odd, and let \(c\) be the order of \(2\) in \((\mathbb{Z}/e')^\times\). For \(q = 2^{1 + cm}\), \(m \geq 0\), the number \(q - 1\) is odd and congruent to \(1\) modulo \(e'\), so it is prime to \(e\). If \(N\) and \(e\) are as in (3), then \(N(q) = P_X(q-1)\) for the infinitely many \(q\) with \(\gcd(q-1, e\,e_X) = 1\). \(\square\)

*Reference:* [Deitmar 2006, Theorem 1] and [Deitmar–Koyama–Kurokawa 2008, Theorem 1.1], where \(P_X(t-1)\) is called the zeta-polynomial of \(X\).

**Example 4.6 (the count is not always a polynomial in \(q\)).** Let \(X = \operatorname{Spec}\mathbb{F}_{1^2}\). It has one point, with unit group \(\mu_2\). So \(\# X(\mathbb{F}_{1^n}) = \gcd(2, n)\), and \(N_X(q)\) is \(2\) for odd \(q\) and \(1\) for even \(q\). Indeed \(X_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[x]/(x^2 - 1)\), and the equation \(x^2 = 1\) has two solutions in \(\mathbb{F}_q\) for odd \(q\) and one for even \(q\). Here \(e_X = 2\) and \(P_X = 1\). No polynomial gives \(N_X(q)\) for all \(q\).

The torsion need not show at a generic point. Let \(M = \{0, 1, \tau, \varepsilon\}\) be the submonoid of \((\mathbb{Z} \times \mathbb{Z}, \cdot)\) with \(0 = (0,0)\), \(1 = (1,1)\), \(\tau = (-1, 1)\) and \(\varepsilon = (0, 1)\). So \(\tau^2 = 1\), \(\tau\varepsilon = \varepsilon\) and \(\varepsilon^2 = \varepsilon\). Its prime ideals are \(\{0\}\) and \(\{0, \varepsilon\}\). The stalk at \(\{0\}\) is \(M_\varepsilon = \mathbb{F}_1\): in \(M_\varepsilon\) the idempotent \(\varepsilon\) is invertible, so \(\varepsilon = 1\) and \(\tau = \tau\varepsilon = 1\). The stalk at \(\{0, \varepsilon\}\) is \(M\), with unit group \(\{1, \tau\}\). So \(Y = \operatorname{Spec} M\) has \(\# Y(\mathbb{F}_{1^n}) = 1 + \gcd(2, n)\), and \(N_Y(q)\) is \(3\) for odd \(q\) and \(2\) for even \(q\). Indeed \(Y_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[\tau, \varepsilon]/(\tau^2 - 1,\ \tau\varepsilon - \varepsilon,\ \varepsilon^2 - \varepsilon)\), and the solutions in a field are \((\tau, \varepsilon) = (1, 1)\) and \((\pm 1, 0)\). Here \(e_Y = 2\) and \(P_Y = 2\).

*Reference:* [Deitmar 2006, Section 2 and Remark 1] states Corollary 4.5(2) with, in place of \(e_X\), the least common multiple of the exponents of the group completions of the stalks, that is, of the groups obtained from the stalks by inverting all elements. In the convention without zero of that work the stalks of \(Y\) are \(\{1\}\) and \(\{1, \tau, \varepsilon\}\), and both have the trivial group completion. So that number is \(1\), but \(N_Y(q)\) is not a polynomial in \(q\). This is why \(e_X\) is defined with the unit groups of the stalks. For integral monoid schemes the unit groups are subgroups of the group completions, and the two statements agree.

The next theorem says when the count is a polynomial. It answers the question at the end of [Deitmar 2005, Section 6] for monoid schemes of finite type. The implication from (2) to (1) and (3) is [Connes–Consani 2010, Theorem 4.10].

**Theorem 4.7.** Let \(X\) be a monoid scheme of finite type. The following are equivalent.

1. There is a polynomial \(N\) with \(N_X(q) = N(q)\) for all prime powers \(q\).
2. The group \(\mathcal{O}_{X,x}^\times\) is torsion-free for every \(x \in X\).
3. There is a polynomial \(P\) with \(\# X(\mathbb{F}_{1^n}) = P(n)\) for all \(n \geq 1\).

If they hold, then \(P = P_X\) and \(N(t) = P_X(t-1)\).

*Proof.* (2) implies (3) with \(P = P_X\), by Theorem 4.4. (3) implies (1) with \(N(t) = P(t-1)\), by (4.2). Assume (1). By Corollary 4.5, \(N(t) = P_X(t-1)\). So for every prime power \(q\),
\[
\sum_{x \in X} (q-1)^{r(x)}\,\bigl(h_x(q-1) - 1\bigr) = 0 .
\]
All terms are \(\geq 0\) and \((q-1)^{r(x)} > 0\). So \(h_x(q-1) = 1\) for all \(x\) and all \(q\). Suppose some \(T_x\) is not trivial, and let \(\ell\) be a prime that divides its order. Then \(T_x\) has a quotient of order \(\ell\). Take \(q = 3\) if \(\ell = 2\) and \(q = 2^{\ell - 1}\) if \(\ell\) is odd. Then \(\ell\) divides \(q - 1\), so \(\mu_{q-1}\) has a subgroup of order \(\ell\), and there is a nontrivial homomorphism \(T_x \to \mu_{q-1}\). This contradicts \(h_x(q-1) = 1\). \(\square\)

**Example 4.8 (finite type is needed).** Let \(X = \operatorname{Spec}(\mathbb{Q}/\mathbb{Z})_0\), one point with unit group \(\mathbb{Q}/\mathbb{Z}\). A homomorphism from a divisible group to a finite group is trivial. So \(\# X(\mathbb{F}_{1^n}) = 1\) for all \(n\), and (1) and (3) hold, but the unit group is a torsion group. In the other direction, \(\mathbb{A}^\infty = \operatorname{Spec}\mathbb{F}_1[t_1, t_2, \dots]\) has infinitely many points with values in every \(\mathbb{F}_{1^n}\).

## 5. Projective space over \(\mathbb{F}_1\)

**Construction 5.1.** Fix \(n \geq 0\). Let \(G_n\) be the group of Laurent monomials \(T^a = T_0^{a_0} \cdots T_n^{a_n}\) with \(a \in \mathbb{Z}^{n+1}\) and \(a_0 + \dots + a_n = 0\). It is free abelian of rank \(n\). For a nonempty subset \(I \subseteq \{0, \dots, n\}\) put
\[
S_I = \{T^a \in G_n : a_j \geq 0 \text{ for all } j \notin I\}, \qquad A_I = (S_I)_0 .
\]
Then:

- \(S_{\{i\}}\) is the free commutative monoid on the \(n\) elements \(T_j/T_i\), \(j \neq i\). So \(\operatorname{Spec} A_{\{i\}} \cong \mathbb{A}^n\).
- For \(i \in I\) and any nonempty \(I'\), let \(a = \prod_{j \in I' \setminus I} T_j/T_i\), an element of \(S_I\). Then \(S_{I \cup I'} = S_I[a^{-1}] = S_IS_{I'}\). Indeed, \(S_IS_{I'} \subseteq S_{I \cup I'}\) is clear. Multiplying an element of \(S_{I\cup I'}\) by a high power of \(a\) makes the exponents at \(j \in I' \setminus I\) non-negative, so \(S_{I \cup I'} \subseteq S_I[a^{-1}]\). And \(a^{-1} = \prod_{j \in I'\setminus I} T_i/T_j\) lies in \(S_{I'}\), so \(S_I[a^{-1}] \subseteq S_IS_{I'}\).
- In particular \(S_I = S_{\{i\}}[a^{-1}]\) for \(i \in I\) and \(a = \prod_{j \in I \setminus \{i\}} T_j/T_i\). So \(S_I\) is finitely generated, and it generates \(G_n\) as a group, because the \(T_j/T_i\) do.

So the family \((S_I)_I\) satisfies the hypotheses of Lemma 3.8. The resulting monoid scheme is *projective space* \(\mathbb{P}^n = \mathbb{P}^n_{\mathbb{F}_1}\). We write \(U_i\) for the chart with monoid \(A_{\{i\}}\). For \(n = 1\) and \(t = T_1/T_0\) this is the projective line of Examples 2.10.

**Proposition 5.2.**

1. \(\mathbb{P}^n\) is connected, integral, separated and of finite type, with \(G_{\mathbb{P}^n} = G_n\). It is covered by the \(n+1\) charts \(U_i \cong \mathbb{A}^n\).
2. For every nonempty \(I \subseteq \{0,\dots,n\}\) there is exactly one point \(x_I\) with \(S_{x_I} = S_I\), and every point is of this form. So \(\mathbb{P}^n\) has \(2^{n+1} - 1\) points. The smallest open neighbourhood of \(x_I\) is \(\{x_K : K \supseteq I\} = \bigcap_{i \in I} U_i\), and \(x_J\) lies in the closure of \(x_I\) if and only if \(J \subseteq I\).
3. \(\mathcal{O}_{x_I}^\times = \{T^a \in G_n : a_j = 0 \text{ for } j \notin I\}\) is free abelian of rank \(|I| - 1\).
4. For all \(m \geq 1\) and all prime powers \(q\),
\[
\#\mathbb{P}^n(\mathbb{F}_{1^m}) = \sum_{j=0}^{n} \binom{n+1}{j+1} m^j = \frac{(m+1)^{n+1} - 1}{m}, \qquad N_{\mathbb{P}^n}(q) = \frac{q^{n+1} - 1}{q - 1} = [n+1]_q .
\]
5. For every ring \(k\), \((\mathbb{P}^n)_k\) is the projective space \(\mathbb{P}^n_k = \operatorname{Proj} k[T_0, \dots, T_n]\).

*Proof.* (1) is Lemma 3.8. (2) By Proposition 3.9 the map \(x \mapsto S_x\) is injective. A point \(x\) lies in some chart \(U_i = \operatorname{Spec} A_{\{i\}}\). There it is the prime ideal generated by the \(T_j/T_i\) with \(j \in J\), for a subset \(J\) of \(\{0,\dots,n\} \setminus \{i\}\). The monoid \(S_x\) is the localization of \(S_{\{i\}}\) at the elements \(T_l/T_i\) with \(l \notin J\), which is \(S_I\) for \(I = \{0,\dots,n\} \setminus J\). Every nonempty \(I\) occurs, for any \(i \in I\). The monoid \(S_I\) determines \(I\): for \(n \geq 1\), \(I\) is the set of \(i\) such that \(T_j/T_i \in S_I\) for some \(j \neq i\). The smallest open neighbourhood of \(x_I\) is \(\operatorname{Spec} A_I\). For \(i \in I\) it is the principal open subset of \(U_i\) where the \(T_l/T_i\), \(l \in I\), do not vanish. So it consists of the \(x_K\) with \(K \supseteq I\), and \(x_K \in U_i\) if and only if \(i \in K\). The point \(x_J\) lies in the closure of \(x_I\) if and only if \(x_I\) lies in the smallest neighbourhood of \(x_J\). (3) \(T^a\) and \(T^{-a}\) both lie in \(S_I\) if and only if \(a_j = 0\) for \(j \notin I\). (4) follows from Theorem 4.4 and (4.2), since there are \(\binom{n+1}{j+1}\) subsets with \(j+1\) elements. (5) By Theorem 4.1(3), \((\mathbb{P}^n)_k\) is glued from the affine spaces \(\operatorname{Spec} k[T_j/T_i : j \neq i]\) along the open subschemes where \(T_j/T_i\) is invertible. This is the standard cover of \(\operatorname{Proj} k[T_0,\dots,T_n]\) [Stacks, Tag [01ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-projective-space)]. \(\square\)

**Remark 5.3 (which set is "the set of points of projective space").** Three sets occur.

- The underlying set of \(\mathbb{P}^n\), which is also \(\mathbb{P}^n(\mathbb{F}_1)\) by Corollary 3.2. It has \(2^{n+1} - 1\) elements, the nonempty subsets of \(\{0,\dots,n\}\). The closure of \(x_I\) is \(\{x_J : \emptyset \neq J \subseteq I\}\), which is the underlying space of a \(\mathbb{P}^{|I|-1}\). So the points of the space \(\mathbb{P}^n\) are the coordinate subspaces. There are \(\binom{n+1}{j+1}\) of them of dimension \(j\). This is the value at \(q = 1\) of the Gaussian binomial coefficient \(\binom{n+1}{j+1}_q\), the number of \(j\)-dimensional linear subspaces of \(\mathbb{P}^n(\mathbb{F}_q)\); see *Counting over finite fields and the limit q → 1*.
- The closed points \(x_{\{0\}}, \dots, x_{\{n\}}\). There are \(n+1\) of them, the value at \(q = 1\) of \([n+1]_q\). In general the value at \(t = 1\) of the polynomial \(P_X(t-1)\) of Corollary 4.5 is \(P_X(0)\), the number of points \(x\) with \(r(x) = 0\).
- In the convention without zero of [Deitmar 2005], \(\mathbb{P}^n(\mathbb{F}_1)\) is a single point (Remark 3.3).

Exercise 6 shows that the automorphism group of \(\mathbb{P}^n\) is the symmetric group on the \(n+1\) closed points.

## 6. Integral monoid schemes and toric varieties

Throughout this section \(X\) is a connected integral monoid scheme of finite type and \(k\) is a field. We use the notation of Propositions 2.6 and 2.8: \(G = G_X\), a finitely generated abelian group; \(A_x = \mathcal{O}_{X,x} \subseteq G_0\) and \(S_x = A_x \setminus \{0\}\); \(U_x\), the smallest open neighbourhood of \(x\). For a submonoid \(S \subseteq G\) we write \(k[S]\) for the \(k\)-span of \(S\) in the group algebra \(k[G]\). So \(k[S_x] = k[A_x]\), and \(X_k\) is covered by the affine open subschemes \((U_x)_k = \operatorname{Spec} k[S_x]\).

### 6.1 The torus action

The group algebra \(k[G]\) is a Hopf algebra with comultiplication \(\Delta(g) = g \otimes g\), counit \(g \mapsto 1\) and antipode \(g \mapsto g^{-1}\). So \(D = \operatorname{Spec} k[G]\) is a commutative group scheme over \(k\). If \(G \cong \mathbb{Z}^r\), then \(D \cong \mathbb{G}_{m,k}^r\) is a split torus.

**Theorem 6.1.** Let \(X\), \(G\), \(k\) and \(D\) be as above.

1. \(U_\eta = \{\eta\}\), and \(D = (U_\eta)_k\) is a dense open subscheme of \(X_k\). For every \(x \in X\) the restriction map \(k[S_x] \to k[G]\) is the inclusion.
2. There is a unique action \(a\colon D \times_k X_k \to X_k\) such that every \((U_x)_k\) is stable and the action on it is given by the \(k\)-algebra homomorphism \(c_x\colon k[S_x] \to k[G] \otimes_k k[S_x]\) with \(c_x(s) = s \otimes s\) for \(s \in S_x\). On \(D\) it is the group law.
3. If \(G\) is torsion-free, then \(X_k\) is integral and \(D\) is a split torus.
4. If \(k\) has characteristic \(p > 0\) and \(G\) has an element of order \(p\), then \(X_k\) is not reduced.
5. Let \(k\) be algebraically closed, let \(F\) be the torsion subgroup of \(G\), and assume that the characteristic of \(k\) does not divide \(|F|\). Choose a splitting \(G = \Lambda \times F\) with \(\Lambda\) free. Then \(X_k\) is reduced. The group scheme \(D\) is the disjoint union of open subschemes \(T_\chi \cong \operatorname{Spec} k[\Lambda]\), one for each character \(\chi\colon F \to k^\times\). The irreducible components of \(X_k\) are the closures \(Z_\chi\) of the \(T_\chi\). For a \(k\)-point \(d\colon G \to k^\times\) of \(D\) the translation by \(d\) is an automorphism of \(X_k\) that maps \(Z_\chi\) onto \(Z_{\chi \cdot d|_F}\). So the components are isomorphic to each other, each contains a torus as a dense open subset, and each is stable under the translations by the \(k\)-points of \(T_1\).

*Proof.* (1) The ideal \(\{0\}\) is the smallest prime ideal of every \(A_x\), so \(U_\eta = \{\eta\} = \operatorname{Spec} G_0\). Let \(s\) be the product of a finite set of generators of \(S_x\). Then \(A_x[s^{-1}] = G_0\). So \((U_\eta)_k = \operatorname{Spec} k[G]\) is the principal open subset \(D(s)\) of \(\operatorname{Spec} k[S_x]\), and the restriction map is the inclusion. The element \(s\) is a unit of \(k[G]\), so it is not a zero divisor of \(k[S_x]\), and \(D(s)\) is dense in \(\operatorname{Spec} k[S_x]\). The \((U_x)_k\) cover \(X_k\).

(2) By (4.1), \(c_x\) is the homomorphism attached to the morphism of monoids \(A_x \to (k[G] \otimes_k k[S_x], \cdot)\), \(s \mapsto s \otimes s\). The identities \((\Delta \otimes \mathrm{id}) \circ c_x = (\mathrm{id} \otimes c_x) \circ c_x\) and \((\varepsilon \otimes \mathrm{id}) \circ c_x = \mathrm{id}\), with \(\varepsilon\) the counit, hold on the elements \(s\). So \(c_x\) defines an action \(a_x\) of \(D\) on \((U_x)_k\). Let \(y \in U_x\). Then \(U_y = D(t)\) for some \(t \in S_x\), and \(S_y = S_x[t^{-1}]\). Since \(c_x(t) = t \otimes t\) and \(t\) is a unit of \(k[G]\), the preimage of \((U_y)_k\) under \(a_x\) is \(D \times (U_y)_k\), and \(a_x\) restricts to \(a_y\) there. The open sets \(D \times (U_x)_k\) cover \(D \times X_k\), and \(D \times ((U_x)_k \cap (U_{x'})_k)\) is covered by the \(D \times (U_y)_k\) with \(y \in U_x \cap U_{x'}\). So the \(a_x\) glue to a morphism \(a\). It is an action because it is one on each \(D \times (U_x)_k\). For \(x = \eta\) the map \(c_\eta\) is \(\Delta\).

(3) If \(G \cong \mathbb{Z}^r\), then \(k[G]\) is a Laurent polynomial ring. So \(k[G]\) and its subrings \(k[S_x]\) are domains, and \(X_k\) is reduced. A nonempty open subset of \(X_k\) meets some \((U_x)_k\), which is irreducible with dense open subset \(D\). So it meets \(D\). Since \(D\) is irreducible, any two nonempty open subsets of \(X_k\) meet.

(4) If \(g \in G\) has order \(p\), then \(g - 1 \neq 0\) and \((g-1)^p = g^p - 1 = 0\) in \(k[G]\). So the open subscheme \(D\) is not reduced.

(5) For a cyclic group of order \(d\) prime to the characteristic, \(k[\mathbb{Z}/d] = k[x]/(x^d - 1)\) is a product of \(d\) copies of \(k\), because \(x^d - 1\) has \(d\) different roots. So \(k[F] \cong \prod_\chi k\), by \(f \mapsto (\chi(f))_\chi\), and \(k[G] = k[\Lambda] \otimes_k k[F] = \prod_\chi k[\Lambda]\). This gives the decomposition of \(D\), where \(T_\chi\) is the locus on which each \(f \in F\) takes the value \(\chi(f)\). The ring \(k[G]\) is reduced, so its subrings \(k[S_x]\) are reduced and \(X_k\) is reduced. The \(T_\chi\) are irreducible and are open and closed in \(D\). Their closures \(Z_\chi\) are irreducible, their union is the closure of \(D\), which is \(X_k\) by (1), and \(Z_\chi \cap D = T_\chi\), so none contains another. Hence the \(Z_\chi\) are the irreducible components. The translation by \(d\) is given on \(k[S_x]\) by \(s \mapsto d(s)s\), and its inverse is the translation by \(d^{-1}\). It maps \(D\) to \(D\). It sends \(f - c\) to \(d(f)f - c\) for \(f \in F\) and \(c \in k\), so it maps \(T_\chi\) onto \(T_{\chi \cdot d|_F}\), and \(Z_\chi\) onto \(Z_{\chi\cdot d|_F}\). \(\square\)

*Reference:* for \(k = \mathbb{C}\), parts (1), (2) and (5) are [Deitmar 2008, Theorem 4.1].

### 6.2 Normality

**Definition 6.2.** Let \(A\) be an integral monoid with group \(G\) and \(S = A \setminus \{0\}\). It is *torsion-free* if \(G\) is torsion-free. It is *normal* if every \(g \in G\) with \(g^d \in S\) for some \(d \geq 1\) lies in \(S\). An integral monoid scheme is torsion-free, or normal, if all its stalks are.

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Section 1 and Definition 1.6]. There a monoid is called torsion-free if \(a^n = b^n\) implies \(a = b\). For an integral monoid this is equivalent to our definition: if \(g = a/b\) satisfies \(g^n = 1\), then \(a^n = b^n\).

A localization of a normal monoid is normal: if \(g^d \in S[t^{-1}]\), then \(g^dt^m \in S\) for some \(m \geq 0\), so \((gt^m)^d \in S\), so \(gt^m \in S\) and \(g \in S[t^{-1}]\). A connected integral monoid scheme is torsion-free if and only if \(G_X\) is torsion-free.

**Lemma 6.3.** Let \(A\) be a finitely generated monoid. Every ascending chain of ideals \(I_0 \subseteq I_1 \subseteq \cdots\) of \(A\) is stationary.

*Proof.* Let \(I\) be the union of the \(I_j\). The span \(k[I]\) of \(I \setminus \{0\}\) is an ideal of \(k[A]\), which is a Noetherian ring [Stacks, Tag [00FN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-permanence)]. So \(k[I]\) is generated by finitely many elements, and each of them involves only finitely many elements of \(I\). So \(k[I]\) is generated, as an ideal, by finitely many \(a_1, \dots, a_m \in I \setminus \{0\}\), and these lie in some \(I_J\). Let \(b \in I \setminus \{0\}\). Then \(b\) is a \(k\)-linear combination of elements \(ca_l\) with \(c \in A\). Since \(A \setminus \{0\}\) is a basis of \(k[A]\), we get \(b = ca_l\) for some \(c\) and \(l\). So \(b \in I_J\), and \(I = I_J\). \(\square\)

**Proposition 6.4.**

1. Let \(A\) be a finitely generated integral monoid whose group \(G\) is torsion-free. Then \(k[A]\) is a normal domain if and only if \(A\) is normal.
2. Let \(X\) be torsion-free. Then \(X_k\) is normal if and only if \(X\) is normal.

*Proof.* (1) Put \(S = A \setminus \{0\}\), so \(k[A] = k[S] \subseteq k[G]\). The ring \(k[G]\) is a Laurent polynomial ring over a field, hence a normal domain [Stacks, Tags [00H1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-polynomial-ring-normal) and [00GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-normal-domain)]. The monoid \(S\) generates \(G\), so \(k[S]\) and \(k[G]\) have the same field of fractions \(K\).

Let \(k[S]\) be normal and \(g \in G\) with \(g^d \in S\). Then \(g \in K\) is a root of the monic polynomial \(Y^d - g^d\) over \(k[S]\), so \(g \in k[S]\). Since \(G\) is a basis of \(k[G]\), this means \(g \in S\).

Let \(A\) be normal and let \(f \in K\) be integral over \(k[S]\). Then \(f \in k[G]\), because \(k[G]\) is normal. We show \(f \in k[S]\) by induction on the number of elements of \(G\) that occur in \(f\) with a nonzero coefficient. Choose an isomorphism \(G \cong \mathbb{Z}^r\) and order \(G\) lexicographically. This is a total order compatible with the group law. For \(h \neq 0\) in \(k[G]\) let \(\operatorname{lead}(h) \in G\) be the largest element that occurs in \(h\). Then \(\operatorname{lead}(hh') = \operatorname{lead}(h)\operatorname{lead}(h')\). The ring \(k[S][f]\) is a finitely generated \(k[S]\)-module, because \(f\) is integral, and it lies in \(K\). Multiplying by a common denominator of a finite set of generators, we find \(h \neq 0\) in \(k[S]\) with \(hf^j \in k[S]\) for all \(j \geq 0\). Let \(u = \operatorname{lead}(h)\) and \(m = \operatorname{lead}(f)\). Then \(um^j = \operatorname{lead}(hf^j) \in S\) for all \(j \geq 0\). The sets \(I_j = \{0\} \cup \bigcup_{i \leq j} um^iS\) form an ascending chain of ideals of \(A\). By Lemma 6.3 there is \(J\) with \(um^{J+1} \in I_J\). So \(um^{J+1} = um^is\) with \(i \leq J\) and \(s \in S\). Hence \(m^{J+1-i} = s \in S\), and \(m \in S\) because \(A\) is normal. Let \(c\) be the coefficient of \(m\) in \(f\). Then \(f - cm\) is integral over \(k[S]\) [Stacks, Tag [00GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-closure-is-ring)] and has fewer terms. By induction \(f - cm \in k[S]\), so \(f \in k[S]\).

(2) By Theorem 6.1, \(X_k\) is an integral scheme covered by the \(\operatorname{Spec} k[S_x]\). It is normal if and only if all its local rings are normal domains [Stacks, Tag [033I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-definition-normal)]. Localizations of normal domains are normal [Stacks, Tag [00GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-normal-domain)], and a domain whose localizations at all prime ideals are normal is normal [Stacks, Tag [030B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-normality-is-local)]. So \(X_k\) is normal if and only if every \(k[S_x]\) is normal, and by (1) this holds if and only if every \(A_x\) is normal. \(\square\)

### 6.3 Open immersions and affine open subsets

**Lemma 6.5.** Let \(G\) be a free abelian group of finite rank and \(S \subseteq S'\) submonoids of \(G\), with \(S\) finitely generated. Assume that the morphism \(j\colon \operatorname{Spec} k[S'] \to \operatorname{Spec} k[S]\) induced by the inclusion is an open immersion. Then \(S' = S[a^{-1}]\) for some \(a \in S\), and the image of \(j\) is \(D(a)\).

*Proof.* Let \(S'^\times\) be the group of units of \(S'\) and \(F = S \cap S'^\times\). If \(s_1s_2 \in F\) with \(s_1, s_2 \in S\), then \(s_1^{-1} = (s_1s_2)^{-1}s_2 \in S'\), so \(s_1 \in F\). Hence \(F\) is generated by the generators of \(S\) that lie in \(F\). Let \(a\) be their product, and put \(S_1 = S[a^{-1}] = SF^{-1}\). Then \(S_1 \subseteq S'\). Moreover \(S_1 \cap S'^\times = S_1^\times\): if \(sf^{-1} \in S'^\times\) with \(s \in S\) and \(f \in F\), then \(s \in S \cap S'^\times = F\), so \(sf^{-1}\) is a unit of \(S_1\).

The inclusions \(k[S] \subseteq k[S_1] \subseteq k[S']\) factor \(j\) through \(j_1\colon \operatorname{Spec} k[S'] \to \operatorname{Spec} k[S_1] = D(a)\), and \(j_1\) is an open immersion. We show \(S' = S_1\).

Let \(\varepsilon\colon k[S'] \to k\) be the \(k\)-algebra homomorphism with \(\varepsilon(m) = 1\) for \(m \in S'^\times\) and \(\varepsilon(m) = 0\) for \(m \in S' \setminus S'^\times\). It exists by (4.1), because the non-units of \(S'_0\) form a prime ideal. Its kernel is a point of \(\operatorname{Spec} k[S']\). The image of \(j_1\) is open. So there is \(f \in k[S_1]\) such that \(D(f)\) contains the image of this point and lies in the image of \(j_1\). Then \(\varepsilon(f) \neq 0\), and \(k[S_1]_f \to k[S']_f\) is an isomorphism. Write \(f = f_0 + f_1\), where \(f_0\) involves only elements of \(S_1^\times\) and \(f_1\) only elements of \(S_1 \setminus S_1^\times\). Since \(S_1 \setminus S_1^\times \subseteq S' \setminus S'^\times\), we have \(\varepsilon(f_1) = 0\). So \(\varepsilon(f_0) \neq 0\), and \(f_0 \neq 0\).

Let \(m' \in S'\). Since \(k[G]\) is a domain, there is \(N \geq 0\) with \(f^Nm' \in k[S_1]\). Write \(f^N = f_0^N + h_1\), where \(h_1\) involves only elements of the ideal \(S_1 \setminus S_1^\times\), and \(f_0^N \neq 0\) involves only elements of \(S_1^\times\). The sets \(m'S_1^\times\) and \(m'(S_1 \setminus S_1^\times)\) are disjoint. So no term of \(f_0^Nm'\) cancels against a term of \(h_1m'\). Take \(u \in S_1^\times\) that occurs in \(f_0^N\). Then \(um'\) occurs in \(f^Nm' \in k[S_1]\), so \(um' \in S_1\) and \(m' \in S_1\). \(\square\)

**Proposition 6.6.** Let \(X\) be torsion-free.

1. For a nonempty open \(U \subseteq X\), the ring of functions on \(U_k\) is \(k[B]\), where \(B = \bigcap_{x \in U} S_x = \mathcal{O}_X(U) \setminus \{0\}\).
2. If \(U \subseteq X\) is a nonempty open subset and \(U_k\) is affine, then \(U\) is affine.
3. \(X\) is separated if and only if \(X_k\) is separated over \(k\).

*Proof.* (1) \(U_k\) is covered by the \((U_x)_k\) with \(x \in U\). A function on \(U_k\) is a family of elements \(h_x \in k[S_x]\) that agree on the overlaps. The overlap of \((U_x)_k\) and \((U_y)_k\) is covered by the \((U_z)_k\) with \(z \in U_x \cap U_y\), and the restriction maps are inclusions into \(k[G]\). So the condition is that all \(h_x\) are the same element of \(k[G]\). Hence the ring is \(\bigcap_{x \in U} k[S_x] = k[B]\). The description of \(B\) is Proposition 2.8(3).

(2) By (1), \(U_k = \operatorname{Spec} k[B]\). It is of finite type over \(k\), so \(k[B]\) is a finitely generated \(k\)-algebra, and \(B\) is a finitely generated monoid by the argument in the proof of Proposition 4.2(4). For \(x \in U\) the inclusion of \((U_x)_k\) in \(U_k\) is an open immersion induced by \(k[B] \subseteq k[S_x]\). By Lemma 6.5, \(S_x = B[a_x^{-1}]\) for some \(a_x \in B\), and \((U_x)_k = D(a_x)\). Let \(\varepsilon\colon k[B] \to k\) be \(1\) on \(B^\times\) and \(0\) on \(B \setminus B^\times\). Its kernel lies in some \(D(a_x)\). Then \(\varepsilon(a_x) \neq 0\), so \(a_x \in B^\times\) and \((U_x)_k = U_k\). Since \(\beta\) is surjective, \(U_x = U\).

(3) One direction is Proposition 4.2(5). Let \(X_k\) be separated and \(x, y \in X\). Then \((U_x)_k \cap (U_y)_k = (U_x \cap U_y)_k\) is affine and \(k[S_x] \otimes_{\mathbb{Z}} k[S_y]\) maps onto its ring of functions [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)]. By (2), \(U_x \cap U_y = U_z\) for some \(z\). The image of \(k[S_x] \otimes k[S_y] \to k[S_z]\) is \(k[S_xS_y]\). So \(S_z = S_xS_y\), and \(X\) is separated by Proposition 3.9(1). \(\square\)

### 6.4 The toric dictionary

**Definition 6.7.** A *toric variety* over \(k\) is a normal variety \(V\) over \(k\), that is, an integral separated scheme of finite type over \(k\) [Stacks, Tag [020D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-variety)] that is normal [Stacks, Tag [033I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-definition-normal)], together with a dense open subscheme \(T \subseteq V\), an isomorphism \(T \cong \operatorname{Spec} k[M]\) for a free abelian group \(M\) of finite rank, and an action \(T \times_k V \to V\) that extends the group law of \(T\). For \(k = \mathbb{C}\) this is the definition of [Brasselet 2001, Theorem 4.3]. An *isomorphism* of toric varieties \((V, T) \to (V', T')\) is an isomorphism of \(k\)-schemes \(V \to V'\) that restricts to an isomorphism of group schemes \(T \to T'\) and commutes with the actions.

A *toric monoid scheme* is a connected, separated, integral, torsion-free, normal monoid scheme of finite type [Cortiñas–Haesemeyer–Walker–Weibel 2015, Definition 4.1].

**Theorem 6.8.** Let \(k\) be a field.

1. Let \(X\) be a connected integral torsion-free monoid scheme of finite type, and \(T = \operatorname{Spec} k[G_X] \subseteq X_k\) with the action of Theorem 6.1. Then \((X_k, T)\) is a toric variety if and only if \(X\) is normal and separated, that is, if and only if \(X\) is a toric monoid scheme.
2. Let \(k\) be algebraically closed. Every toric variety over \(k\) is isomorphic to \((X_k, T)\) for a toric monoid scheme \(X\), and \(X\) is unique up to isomorphism.

So for an algebraically closed field \(k\), base change is a bijection between the isomorphism classes of toric monoid schemes and the isomorphism classes of toric varieties over \(k\).

The proof of (2) uses a theorem of Sumihiro on torus actions, which we prove first.

**Sumihiro's theorem.** Let \(k\) be algebraically closed and let a torus \(T\) over \(k\) act on a normal variety \(V\) over \(k\). Then every point of \(V\) has an affine open neighbourhood \(W\) that is \(T\)-stable, that is, the action maps \(T \times W\) into \(W\). *Reference:* [Sumihiro 1974]; for actions of connected algebraic groups on normal varieties see [Brion 2017].

The point need not be closed, and the action need not be faithful. The proof makes an affine neighbourhood stable in two moves: its complement is the support of a divisor, whose line bundle can be made \(T\)-equivariant; then one weight component of the canonical section cuts out a stable affine set.

*Proof.* Write \(T = \operatorname{Spec} k[M]\) with \(M\) free abelian of finite rank, \(\chi^m \in k[M]\) for \(m \in M\), \(e\) for the unit of \(T\), \(a\colon T \times V \to V\) for the action and \(p\colon T \times V \to V\) for the projection; products are over \(k\). For an invertible sheaf \(L\) on a variety \(Y\) and \(s \in \Gamma(Y, L)\), let \(Y_s\) be the open set where \(s\) generates \(L\).

*Step 1: divisors on normal varieties.* Let \(Y\) be a normal variety. Its local rings at points of codimension one are discrete valuation rings, and \(A = \bigcap_{\operatorname{ht}\mathfrak{p} = 1} A_{\mathfrak{p}}\) for every affine open \(\operatorname{Spec} A \subseteq Y\) [Stacks, Tags [031S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-normal), [031T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-normal-domain-intersection-localizations-height-1)]. So a rational function is regular on an open set if it has no pole at a point of codimension one of that set. Hence, if a closed set \(Z \subseteq Y\) contains no point of codimension \(\leq 1\), restriction \(\Gamma(Y, L) \to \Gamma(Y \setminus Z, L)\) is bijective for every invertible sheaf \(L\) (check it on affine open sets that trivialize \(L\)); applied to sheaves of homomorphisms, it shows that an isomorphism of invertible sheaves on \(Y \setminus Z\) extends uniquely to \(Y\). A *prime divisor* is an irreducible closed subset of codimension one, a *Weil divisor* is a finite integral combination of prime divisors, and \(\operatorname{div}(f)\), for \(f \in k(Y)^\times\), records the valuations of \(f\). A Cartier divisor is determined by its Weil divisor, and it is effective when its Weil divisor is, because a local equation without zeros or poles in codimension one is a unit. For a Cartier divisor \(D\), \(\mathcal{O}_Y(D)\) is the sheaf of rational functions \(f\) with \(\operatorname{div}(f) + D \geq 0\). Every invertible sheaf is isomorphic to some \(\mathcal{O}_Y(D)\) (use a nonzero rational section), and \(\mathcal{O}_Y(D) \cong \mathcal{O}_Y(D')\) if and only if \(D - D'\) is principal. If \(D \geq 0\), the section \(1\) of \(\mathcal{O}_Y(D)\) vanishes exactly on the support of \(D\): locally \(D = \operatorname{div}(h)\) with \(h\) regular, and all associated primes of \(A/hA\) have height one [Stacks, Tag [031T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-normal-domain-intersection-localizations-height-1)]. The regular points of \(Y\) form a dense open set \(Y_{\mathrm{reg}}\) [Stacks, Tag [0B8X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-dense-smooth-open-variety-over-perfect-field)], whose complement contains no point of codimension \(\leq 1\) by the condition \((R_1)\) in Serre's criterion. On \(Y_{\mathrm{reg}}\) every Weil divisor is Cartier: regular local rings are factorial [Stacks, Tag [0AG0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-local-UFD)], and in a factorial domain a prime of height one is principal. The variety \(T \times Y\) is normal and integral: over an affine open \(\operatorname{Spec} A \subseteq Y\) its ring is \(A[M]\), a localization of a polynomial ring over \(A\) [Stacks, Tags [00H1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-polynomial-ring-normal), [00GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-normal-domain)]. If \(Z \subseteq Y\) contains no point of codimension \(\leq 1\), neither does \(T \times Z\): a prime \(P \subseteq A[M]\) over \(\mathfrak{q}\), with a chain \(0 \subsetneq \mathfrak{q}_1 \subsetneq \mathfrak{q}\), contains the chain of primes \(0 \subsetneq \mathfrak{q}_1A[M] \subsetneq \mathfrak{q}A[M]\).

*The complement of an affine open set.* Let \(U\) be a nonempty affine open subset of a normal variety \(Y\). Let \(B_1, \dots, B_q\) be the irreducible components of \(Y \setminus U\) of codimension one, and \(Y' = Y \setminus (B_1 \cup \dots \cup B_q)\). For an affine open \(A \subseteq Y'\), the intersection \(A \cap U\) is affine because \(Y\) is separated [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)], and \(A \setminus U\) contains no point of codimension \(\leq 1\). So \(\Gamma(A, \mathcal{O}) \to \Gamma(A \cap U, \mathcal{O})\) is bijective, the open immersion \(A \cap U \to A\) of affine schemes is an isomorphism, and \(A \subseteq U\). Hence \(Y' = U\), and \(Y \setminus U\) is the support of the effective Weil divisor \(D_U = B_1 + \dots + B_q\). For a Weil divisor \(D\), let \(C(D)\) be the open set of points near which \(D\) is Cartier; adding a principal divisor does not change it.

*Step 2: sections.* Let \(Y\) be a variety, \(A = \Gamma(Y, \mathcal{O}_Y)\) and \(g \in A\). Then \(\Gamma(Y_g, \mathcal{O}_Y) = A_g\): for a finite affine open cover, whose pairwise intersections are affine, \(A\) is the kernel of the difference of the two restriction maps, and localization at \(g\) is exact and computes the sections on principal open sets. Consequently, if \(g_1, \dots, g_n \in A\) generate the unit ideal and every \(Y_{g_i}\) is affine, then \(Y\) is affine: the canonical morphism \(Y \to \operatorname{Spec} A\) [Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)] restricts to isomorphisms \(Y_{g_i} \to D(g_i)\), and the \(D(g_i)\) cover \(\operatorname{Spec} A\). The same kernel description, with a cover that trivializes an invertible sheaf \(L\) and tensored with the flat \(k\)-module \(k[M]\), gives \(\Gamma(T \times Y, p^*L) = k[M] \otimes_k \Gamma(Y, L)\), and similarly for \(T \times T \times Y\).

*Step 3: weights.* Let \(T\) act on a variety \(Y\). An open set \(O \subseteq Y\) that is mapped into itself by the translation by every \(t \in T(k)\) is \(T\)-stable: otherwise \(a^{-1}(Y \setminus O) \cap (T \times O)\) is a nonempty locally closed subset of a scheme of finite type over \(k\), so it contains a \(k\)-point \((t, y)\) [Stacks, Tag [00FV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-nullstellensatz)], and \(ty \notin O\). A *\(T\)-linearization* of an invertible sheaf \(L\) on \(Y\) is an isomorphism \(\lambda\colon p^*L \to a^*L\) that is the identity over \(\{e\} \times Y\) and satisfies \(\lambda(tu, y) = \lambda(t, uy) \circ \lambda(u, y)\) on \(T \times T \times Y\); on fibres, \(\lambda(t, y)\colon L_y \to L_{ty}\). For \(s \in \Gamma(Y, L)\), the formula \((t \cdot s)(y) = \lambda(t, t^{-1}y)(s(t^{-1}y))\) defines a section of \(p^*L\) on \(T \times Y\): the pull-back of \(s\) and \(\lambda\) along \((t, y) \mapsto (t, t^{-1}y)\). By Step 2, \(t \cdot s = \sum_{m \in F} \chi^m(t)s_m\) with \(F \subseteq M\) finite and \(s_m \in \Gamma(Y, L)\). Taking \(t = e\) gives \(s = \sum_m s_m\), and comparing the coefficients of the characters of \(u\) in \((tu) \cdot s = t \cdot (u \cdot s)\) gives \(t \cdot s_m = \chi^m(t)s_m\). The vectors \((\chi^m(t))_{m \in F}\), \(t \in T(k)\), span \(k^F\), because a Laurent polynomial that vanishes at all \(k\)-points is zero; so each \(s_m\) is a linear combination \(\sum_j c_j\, t_j \cdot s\) with \(t_j \in T(k)\).

*Lemma.* If \(L\) is \(T\)-linearized and \(Y_s\) is affine, then for every \(m\) the open set \(W = Y_{s_m}\) is \(T\)-stable and affine.

Indeed, \(t \cdot s_m = \chi^m(t)s_m\) with \(\chi^m(t) \neq 0\) gives \(tW = W\) for \(t \in T(k)\), so \(W\) is \(T\)-stable. Write \(s_m = \sum_j c_j\, t_j \cdot s\). The functions \(g_j = (t_j \cdot s)/s_m\) are regular on \(W\), and \(\sum_j c_jg_j = 1\). Moreover \(W_{g_j} = W \cap Y_{t_j \cdot s} = W \cap t_jY_s\). The set \(t_jY_s\) is affine and \(L\) is trivialized on it by \(t_j \cdot s\), so \(W_{g_j}\) is the principal open subset of \(t_jY_s\) where the function \(s_m/(t_j \cdot s)\) does not vanish; it is affine. By Step 2, \(W\) is affine. Every point \(x \in Y_s\) lies in some \(Y_{s_m}\), since \(s(x) = \sum_m s_m(x) \neq 0\).

*Step 4: invertible sheaves on \(T \times Y\).* Let \(Y\) be a normal variety and \(i_e(y) = (e, y)\). Then \(p^*\colon \operatorname{Pic}(Y) \to \operatorname{Pic}(T \times Y)\) is bijective with inverse \(i_e^*\); injectivity follows from \(p \circ i_e = \operatorname{id}\). Let first \(Y\) be regular, \(K = k(Y)\), and \(F \cong \mathcal{O}(H)\) an invertible sheaf on \(T \times Y\). The generic fibre \(\operatorname{Spec} K[M]\) has a factorial ring, so on it \(H = \operatorname{div}(h)\) for some \(h \in K(M)^\times = k(T \times Y)^\times\). Every prime divisor in the support of \(H - \operatorname{div}(h)\) is vertical: over an affine \(\operatorname{Spec} A \subseteq Y\), a prime \(P \subseteq A[M]\) of height one with \(P \cap A = 0\) survives in \(K[M]\), with the same local ring. If \(P\) has height one and \(\mathfrak{q} = P \cap A \neq 0\), then the prime \(\mathfrak{q}A[M] \neq 0\) lies in \(P\), so \(P = \mathfrak{q}A[M]\), and \(\mathfrak{q}\) has height one. So the vertical prime divisors are the \(T \times B\) with \(B\) a prime divisor of \(Y\), and a uniformizer at \(B\) is one along \(T \times B\). Hence \(H - \operatorname{div}(h) = p^*D\) for a Weil divisor \(D\) on \(Y\), which is Cartier because \(Y\) is regular, and \(F \cong p^*\mathcal{O}_Y(D)\). For normal \(Y\), apply this on \(R = Y_{\mathrm{reg}}\): with \(L = i_e^*F\) we get \(F|_{T \times R} \cong p^*(L|_R)\), and this isomorphism extends across \(T \times (Y \setminus R)\), which contains no point of codimension \(\leq 1\) (Step 1).

*Step 5: every invertible sheaf on a normal variety with a \(T\)-action has a \(T\)-linearization.* Let \(L\) be invertible on \(Y\). By Step 4, \(a^*L \cong p^*i_e^*a^*L = p^*L\); let \(\lambda\colon p^*L \to a^*L\) be an isomorphism. Over \(\{e\} \times Y\) it is multiplication by a unit \(v\) of \(\Gamma(Y, \mathcal{O}_Y)\); replacing \(\lambda\) by \(\lambda \circ p^*(v^{-1})\), it is the identity there. The isomorphisms \(\lambda(tu, y)\) and \(\lambda(t, uy) \circ \lambda(u, y)\) differ by a unit \(c\) of \(\Gamma(T \times T \times Y, \mathcal{O}) = A[M \oplus M]\), where \(A = \Gamma(Y, \mathcal{O}_Y)\) is a domain, and \(c(e, u, y) = c(t, e, y) = 1\). The units of a Laurent polynomial ring over a domain are the monomials with unit coefficients: in a product \(fg = 1\), compare the lexicographically largest and the smallest exponents. So \(c = w\,\chi^m(t)\chi^n(u)\), and the two normalizations force \(w = 1\) and \(m = n = 0\).

*Step 6: Cartier loci are \(T\)-stable.* Let \(D\) be a Weil divisor on \(V\). The regular locus \(R\) is mapped into itself by all translations, so it is \(T\)-stable (Step 3); \(D|_R\) is Cartier, and \(\mathcal{O}_R(D|_R)\) has a \(T\)-linearization (Step 5). For \(t \in T(k)\) the linearization gives \(t^*\mathcal{O}_R(D|_R) \cong \mathcal{O}_R(D|_R)\), so \(t^*D - D = \operatorname{div}(h_t)\) on \(R\), and therefore on \(V\), since \(V \setminus R\) contains no point of codimension one. Hence \(t^{-1}C(D) = C(t^*D) = C(D)\) for all \(t \in T(k)\), and \(C(D)\) is \(T\)-stable (Step 3).

*Step 7: the stable neighbourhood.* Let \(x \in V\), and let \(U\) be an affine open neighbourhood of \(x\). Put \(D = D_U\) and \(Y = C(D)\), a \(T\)-stable open set that contains \(U\) (Step 6). On \(Y\), \(D\) is an effective Cartier divisor, and the section \(s = 1\) of \(L = \mathcal{O}_Y(D|_Y)\) has \(Y_s = Y \setminus \operatorname{Supp} D = U\), which is affine. Choose a \(T\)-linearization of \(L\) (Step 5). Some weight component \(s_m\) does not vanish at \(x\), and by the lemma of Step 3, \(W = Y_{s_m}\) is a \(T\)-stable affine open neighbourhood of \(x\). \(\square\)

*Proof of Theorem 6.8.* (1) By Theorem 6.1 and Proposition 4.2(4), \(X_k\) is an integral scheme of finite type over \(k\), \(T\) is a dense open split torus, and the action extends its group law. By Proposition 6.4, \(X_k\) is normal if and only if \(X\) is normal. By Proposition 6.6, \(X_k\) is separated if and only if \(X\) is separated.

(2) *Existence.* Let \((V, T)\) be a toric variety with \(T = \operatorname{Spec} k[M]\).

*Step 1: stable open subsets contain \(T\).* Let \(W \subseteq V\) be a nonempty \(T\)-stable open subset. Then \(W \cap T\) is a nonempty open subset of \(T\). It contains a closed point \(w\), and closed points of schemes of finite type over \(k\) are \(k\)-points [Stacks, Tag [00FV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-nullstellensatz)]. For a \(k\)-point \(t\) of \(T\), the translation by \(tw^{-1}\) is an automorphism of \(V\) that maps \(W\) into \(W\) and \(w\) to \(t\). So \(W \cap T\) contains all closed points of \(T\), and its closed complement in \(T\) is empty.

*Step 2: stable affine open subsets are monoid algebras.* Let \(W\) be a nonempty \(T\)-stable affine open subscheme of \(V\), with ring of functions \(k[W]\). Since \(V\) is integral and \(T \subseteq W\) is dense, restriction to \(T\) is an inclusion \(k[W] \subseteq k[M]\). The action restricts to \(T \times W \to W\) and extends the group law of \(T\). So the comultiplication \(\Delta\) of \(k[M]\) maps \(k[W]\) into \(k[M] \otimes_k k[W]\). Let \(f = \sum c_m m \in k[W]\). Then \(\Delta(f) = \sum c_m\, m \otimes m\). Apply to the first factor the linear form that takes the coefficient of a fixed \(m_0\). The result \(c_{m_0}m_0\) lies in \(k[W]\). So \(k[W]\) is spanned by the elements of \(M\) that it contains: \(k[W] = k[S_W]\) for the submonoid \(S_W = M \cap k[W]\). The algebra \(k[S_W]\) is finitely generated, so \(S_W\) is a finitely generated monoid, as in the proof of Proposition 4.2(4).

*Step 3: the family of submonoids.* By Sumihiro's theorem and because \(V\) is quasi-compact, \(V = V_1 \cup \dots \cup V_m\) with nonempty \(T\)-stable affine open subschemes \(V_i\). Put \(S_i = S_{V_i}\). The inclusion \(T \subseteq V_i\) is an open immersion \(\operatorname{Spec} k[M] \to \operatorname{Spec} k[S_i]\) induced by the inclusion of rings. By Lemma 6.5, \(M = S_i[a^{-1}]\) for some \(a \in S_i\). So \(S_i\) generates the group \(M\). The ring \(k[S_i]\) is a normal domain because \(V\) is normal [Stacks, Tag [030B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-normality-is-local)], so \(S_i\) is normal by Proposition 6.4. Since \(V\) is separated, \(V_i \cap V_j\) is affine and \(k[S_i] \otimes_{\mathbb{Z}} k[S_j]\) maps onto its ring of functions [Stacks, Tag [01KP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-characterize-separated)]. All restriction maps are inclusions in \(k[M]\). So this ring is \(k[S_iS_j]\). The inclusion of \(V_i \cap V_j\) in \(V_i\) is an open immersion induced by \(k[S_i] \subseteq k[S_iS_j]\). By Lemma 6.5, \(S_iS_j = S_i[a^{-1}]\) for some \(a \in S_i\).

*Step 4: the monoid scheme.* By Step 3 the family \((S_i)\) satisfies the hypotheses of Lemma 3.8 with \(G = M\). Let \(X\) be the resulting monoid scheme, with affine open cover \((X_i)\). It is connected, integral, separated and of finite type. It is torsion-free, and it is normal, because its stalks are localizations of the normal monoids \((S_i)_0\). So \(X\) is a toric monoid scheme. By Theorem 4.1(3), \(X_k\) is covered by the \((X_i)_k = \operatorname{Spec} k[S_i]\), with intersections \(\operatorname{Spec} k[S_iS_j]\). The identifications \((X_i)_k = V_i\) agree on the intersections. They glue to an isomorphism \(X_k \to V\). It is the identity on \(T\), and it commutes with the actions, because on \(V_i\) both actions are given by \(s \mapsto s \otimes s\).

*Uniqueness.* Let \(X\) and \(X'\) be toric monoid schemes and \(\varphi\colon X_k \to X'_k\) an isomorphism of toric varieties. On the tori it is an isomorphism of Hopf algebras \(k[G_{X'}] \to k[G_X]\). An element \(f\) of \(k[G]\) with \(\Delta(f) = f \otimes f\) and counit \(1\) is an element of \(G\): comparing coefficients in \(\sum c_g\, g \otimes g = \sum c_gc_h\, g \otimes h\) shows that only one \(c_g\) is nonzero and that it is \(1\). So the isomorphism is induced by a group isomorphism \(\psi\colon G_{X'} \to G_X\).

We claim that every nonempty \(T\)-stable affine open subscheme \(W\) of \(X_k\) is \((U_x)_k\) for exactly one \(x \in X\). Let \(x \in X\). Since \(X_k\) is separated, \(W \cap (U_x)_k\) is an affine open subscheme of \((U_x)_k\), and it is \(T\)-stable. By Step 2 its ring is \(k[S']\) for a submonoid \(S' \supseteq S_x\). By Lemma 6.5 it is \(D(a)\) for some \(a \in S_x\), so it is \((U_y)_k\) for the point \(y\) with \(U_y = D(a) \subseteq U_x\). Hence \(W\) is the union of some of the \((U_y)_k\), that is, \(W = U_k\) for an open subset \(U \subseteq X\). By Proposition 6.6(2), \(U\) is affine, so \(U = U_z\) for a point \(z\), and \(W = (U_z)_k\). The point \(z\) is unique because \(\beta\) is surjective.

Now let \(x' \in X'\). By the claim, \(\varphi^{-1}((U_{x'})_k) = (U_x)_k\) for a unique \(x \in X\), and \(\varphi\) induces an isomorphism \(k[S_{x'}] \to k[S_x]\) that is the restriction of \(\psi\). So \(\psi(S_{x'}) = S_x\). By symmetry every \(S_x\) arises in this way. By Proposition 3.9(3), \(X \cong X'\). \(\square\)

**Examples 6.9 (each hypothesis is needed).**

1. *Not normal.* Let \(A = \mathbb{F}_1[t^2, t^3]\), the submonoid of \(\mathbb{F}_1[t]\) of all \(t^j\) with \(j \neq 1\), together with \(0\). It is integral, torsion-free and finitely generated, but not normal: \(t \notin A\) and \(t^2 \in A\). Its base change is the cuspidal cubic curve \(\operatorname{Spec} k[t^2, t^3]\). This is an integral separated curve on which \(\mathbb{G}_m\) acts with a dense orbit, but it is not normal.
2. *Not separated.* The line with a doubled origin \(L\) of Examples 2.10 is connected, integral, torsion-free, normal and of finite type, and \(L_k\) is the affine line over \(k\) with a doubled origin.
3. *Torsion.* Exercise 3 gives a connected integral monoid scheme \(X\) with \(G_X = \mathbb{Z} \times \mathbb{Z}/2\). Its base change is the union of two lines if the characteristic of \(k\) is not \(2\), and a double line if it is \(2\), in agreement with Theorem 6.1(4) and (5).
4. *A torus action that does not come from a monoid scheme.* Let \(k\) be algebraically closed and let \(C\) be the rational curve with one node \(p\) obtained from \(\mathbb{P}^1_k\) by identifying \(0\) and \(\infty\). The action of \(\mathbb{G}_m\) on \(\mathbb{P}^1_k\) by multiplication on the coordinate fixes \(0\) and \(\infty\). It induces an action on \(C\), because the functions on an open subset of \(C\) are the functions on its preimage that take the same value at \(0\) and \(\infty\). There are two orbits: \(\{p\}\) and \(C \setminus \{p\} \cong \mathbb{G}_m\), which is open and not closed. The complement of a stable open neighbourhood of \(p\) is a closed stable subset of \(C \setminus \{p\}\), so it is empty. But \(C\) is a proper curve, so it is not affine. Hence \(p\) has no stable affine open neighbourhood. By Theorem 6.1(2), every point of \(X_k\) has an affine open neighbourhood that is stable under \(D\). So \(C\) with its action is not isomorphic to any \((X_k, D)\). The curve \(C\) is not normal at \(p\), so this does not contradict Sumihiro's theorem.

More is true for the curve \(C\) of (4): it is not isomorphic to \(X_k\) for any monoid scheme \(X\), with or without an action. Suppose that \(X_k \cong C\), and identify the two. By Proposition 4.2, \(X\) is of finite type, and \(X\) is connected, because \(\beta\) is continuous and surjective. For a nonempty affine open \(U \subseteq X\) the ring \(k[\mathcal{O}_X(U)]\) is a domain, because \(U_k\) is a nonempty open subscheme of the integral scheme \(C\). The monoid \(\mathcal{O}_X(U)\) is a nonzero submonoid of the multiplicative monoid of this domain, so it is integral. Hence Theorem 6.1 applies to \(X\). The ring \(k[G]\) of the open subscheme \(D\) is a domain. So \(G\) is torsion-free: if \(g \in G\) had order \(m > 1\), then \((g - 1)(1 + g + \dots + g^{m-1}) = 0\) with both factors nonzero. Hence \(G \cong \mathbb{Z}^r\), and \(D\) is a torus of dimension \(r\). Since \(D\) is a nonempty open subscheme of the curve \(C\), we get \(r = 1\) and \(D \cong \operatorname{Spec} k[u, u^{-1}]\). The scheme \(D\) is normal and \(C\) is not normal at \(p\), so \(D\) lies in \(C \setminus \{p\} = \operatorname{Spec} k[t, t^{-1}]\). Its complement there is a finite set of closed points, given by \(t = c_1, \dots, t = c_m\) with \(c_i \in k^\times\). Suppose that \(m \geq 1\). Then \(t\) and \(t - c_1\) are units on \(D\), and no product \(t^a(t - c_1)^b\) with \((a, b) \neq (0, 0)\) is constant. So the units on \(D\), modulo the constants, contain a free abelian group of rank \(2\). But the units of \(k[u, u^{-1}]\) are the elements \(cu^n\) with \(c \in k^\times\), as one sees from the highest and the lowest term of a product; modulo the constants they form a cyclic group. This is a contradiction. So \(m = 0\) and \(D = C \setminus \{p\}\). Let \(x = \beta(p)\). The affine open subscheme \((U_x)_k\) of \(C\) contains \(p\), and it contains \(D = (U_\eta)_k\). So it is \(C\), which is not affine.

*Reference:* [Deitmar 2008, Section 4] calls an irreducible complex variety with a torus action and an open orbit a toric variety. It asserts that every irreducible component of the base change to \(\mathbb{C}\) of a connected integral monoid scheme of finite type is one (Theorem 4.1), that every toric variety is the base change of a monoid scheme, and that every toric variety is given by a fan. With this definition the second assertion fails for the curve of Examples 6.9(4) and the third for the curve of Examples 6.9(1), and if varieties are separated the first fails for \(L\). So we prove Theorems 6.1 and 6.8. The problem with normality is noted in [Cortiñas–Haesemeyer–Walker–Weibel 2015, Remark 4.4.1].

### 6.5 Fans

Toric varieties are described by fans [Telen 2022, Section 4.2]. We recall the definitions and the facts about cones that are used, and then translate.

Let \(N\) be a free abelian group of rank \(n\) and \(M = \operatorname{Hom}(N, \mathbb{Z})\). Write \(N_{\mathbb{R}} = N \otimes \mathbb{R}\), \(M_{\mathbb{R}} = M \otimes \mathbb{R}\), and \(\langle u, v\rangle\) for the pairing. A *rational polyhedral cone* in \(N_{\mathbb{R}}\) is a set \(\sigma = \mathbb{R}_{\geq 0}v_1 + \dots + \mathbb{R}_{\geq 0}v_s\) with \(v_i \in N\). Its *dual* is \(\sigma^\vee = \{u \in M_{\mathbb{R}} : \langle u, v\rangle \geq 0 \text{ for all } v \in \sigma\}\). A *face* of \(\sigma\) is a subset \(\sigma \cap u^\perp = \{v \in \sigma : \langle u, v\rangle = 0\}\) with \(u \in \sigma^\vee\). The cone \(\sigma\) is *strongly convex* if \(\sigma \cap (-\sigma) = \{0\}\). Put \(S_\sigma = \sigma^\vee \cap M\), a submonoid of \(M\), written additively. A *fan* in \(N\) is a finite nonempty set \(\Delta\) of strongly convex rational polyhedral cones in \(N_{\mathbb{R}}\) such that every face of a cone in \(\Delta\) is in \(\Delta\), and the intersection of two cones in \(\Delta\) is a face of each.

**Facts 6.10.** Let \(\sigma, \sigma'\) be rational polyhedral cones in \(N_{\mathbb{R}}\). Then the following hold. They hold as well with the roles of \(N\) and \(M\) exchanged.

- (C1) \(\sigma^\vee\) is a rational polyhedral cone in \(M_{\mathbb{R}}\), and \((\sigma^\vee)^\vee = \sigma\).
- (C2) \(S_\sigma\) is a finitely generated monoid (Gordan's lemma).
- (C3) For \(u \in S_\sigma\) the set \(\tau = \sigma \cap u^\perp\) is a rational polyhedral cone, every face of \(\sigma\) is of this form, and \(S_\tau = S_\sigma + \mathbb{Z}_{\geq 0}(-u)\).
- (C4) If \(\sigma \cap \sigma'\) is a face of \(\sigma\) and of \(\sigma'\), then \(S_{\sigma \cap \sigma'} = S_\sigma + S_{\sigma'}\).
- (C5) If \(\sigma\) is strongly convex, then \(\{0\}\) is a face of \(\sigma\), and it is cut out by an element of \(S_\sigma\).

(C1) is the duality theorem for polyhedral cones. [Telen 2022, Section 2.6] states both parts and [Brasselet 2001, Property 1.1] states the first part, without proofs; we prove it by Fourier–Motzkin elimination and by separation from a closed cone. The other four facts are also in these works: (C2) is [Brasselet 2001, Lemma 1.3] and Gordan's lemma in [Telen 2022, Section 2.7], the statements of (C3) on \(\tau\) and \(S_\tau\) are [Brasselet 2001, Property 1.2 and Proposition 1.1], and (C5) is part of the definition of strong convexity in [Telen 2022, Section 2.6]. They follow from (C1) by short arguments.

*Proof of (C1).* For vectors \(w_1, \dots, w_r\) in a finite-dimensional real vector space write \(\operatorname{cone}(w_1, \dots, w_r)\) for the set of their combinations with coefficients \(\geq 0\); the empty family generates \(\{0\}\).

(i) *Finitely generated cones are closed.* An element \(x = \sum_{i \in S}\lambda_iw_i\) with all \(\lambda_i > 0\) is a combination of a linearly independent subfamily: if \(\sum_{i \in S}c_iw_i = 0\) is a nontrivial relation, with some \(c_i > 0\) after a change of sign, subtract \(t\sum c_iw_i\) with \(t = \min\{\lambda_i/c_i : c_i > 0\}\); the coefficients stay \(\geq 0\) and one more vanishes. The cone on a linearly independent family is closed: after extending the family to a basis, it is given by sign conditions and by the vanishing of the other coordinates. So \(\operatorname{cone}(w_1, \dots, w_r)\) is a finite union of closed sets.

(ii) *Cutting by a half-space.* Let \(\ell\) be a linear form, let \(P\), \(Q\), \(O\) be the sets of \(i\) with \(\ell(w_i) > 0\), \(< 0\), \(= 0\), and put \(p_i = \ell(w_i)\) for \(i \in P\) and \(q_j = -\ell(w_j)\) for \(j \in Q\). Then
\[
\operatorname{cone}(w_1, \dots, w_r) \cap \{\ell \geq 0\} = \operatorname{cone}\big(\{w_i\}_{i \in P \cup O} \cup \{q_jw_i + p_iw_j\}_{i \in P,\ j \in Q}\big).
\]
The generators on the right lie on the left. Conversely, let \(x = \sum\lambda_iw_i\) with \(\lambda_i \geq 0\) and \(\ell(x) \geq 0\), and put \(A = \sum_{i \in P}\lambda_ip_i\) and \(B = \sum_{j \in Q}\lambda_jq_j\), so that \(B \leq A\). If \(A = 0\), all \(\lambda_i\) with \(i \in P \cup Q\) vanish. Otherwise
\[
x = \sum_{i \in O}\lambda_iw_i + \sum_{i \in P}\lambda_i\Big(1 - \frac{B}{A}\Big)w_i + \sum_{i \in P,\ j \in Q}\frac{\lambda_i\lambda_j}{A}(q_jw_i + p_iw_j),
\]
as one checks coefficient by coefficient. If the \(w_i\) lie in a lattice on which \(\ell\) takes integer values, so do the new generators.

(iii) *The dual is finitely generated.* Let \(e_1, \dots, e_n\) be a basis of \(M\) and \(v_1, \dots, v_s \in N\) generators of \(\sigma\). Then \(M_{\mathbb{R}} = \operatorname{cone}(\pm e_1, \dots, \pm e_n)\), and \(\sigma^\vee\) is its intersection with the half-spaces \(\langle u, v_k\rangle \geq 0\), \(k = 1, \dots, s\), on which the forms take integer values on \(M\). Applying (ii) \(s\) times, \(\sigma^\vee\) is generated by finitely many elements of \(M\).

(iv) *Duality.* Clearly \(\sigma \subseteq (\sigma^\vee)^\vee\). Let \(x \in N_{\mathbb{R}} \setminus \sigma\), and fix a Euclidean inner product on \(N_{\mathbb{R}}\). By (i), \(\sigma\) is closed, so it has a point \(p\) nearest to \(x\): minimize the distance over the compact set of \(y \in \sigma\) with \(\|y\| \leq 2\|x\| + 1\), which contains \(0\). For \(v \in \sigma\) and \(0 < t \leq 1\), the point \(p + t(v - p)\) lies in \(\sigma\), so \(\|x - p - t(v - p)\|^2 \geq \|x - p\|^2\); dividing by \(t\) and letting \(t \to 0\) gives \((x - p, v - p) \leq 0\). With \(v = 0\) and \(v = 2p\) this gives \((x - p, p) = 0\). So the linear form \(u = (p - x, \cdot\,)\) is \(\geq 0\) on \(\sigma\) and \(u(x) = -\|x - p\|^2 < 0\). As an element of \(M_{\mathbb{R}}\) it lies in \(\sigma^\vee\), so \(x \notin (\sigma^\vee)^\vee\).

The same arguments apply with \(N\) and \(M\) exchanged, because \(N = \operatorname{Hom}(M, \mathbb{Z})\). \(\square\)

*Proof of (C2)–(C5).* Let \(v_1, \dots, v_s \in N\) generate \(\sigma\).

(C2) By (C1) the cone \(\sigma^\vee\) is generated by finitely many elements of \(M\). So \(S_\sigma = \sigma^\vee \cap M\) is finitely generated by Gordan's lemma, which is proved in *Commutative monoids and their spectra*.

(C3) Let \(u \in \sigma^\vee\), not necessarily in \(M\), and let \(I\) be the set of all \(i\) with \(\langle u, v_i\rangle = 0\). If \(x = \sum \lambda_iv_i\) with \(\lambda_i \geq 0\) and \(\langle u, x\rangle = 0\), then \(\lambda_i\langle u, v_i\rangle = 0\) for all \(i\), because these numbers are \(\geq 0\) and their sum is \(0\). So \(\sigma \cap u^\perp\) is the cone generated by the \(v_i\) with \(i \in I\). It is a rational polyhedral cone. Let \(W \subseteq M_{\mathbb{R}}\) be the subspace of all \(u'\) with \(\langle u', v_i\rangle = 0\) for \(i \in I\). It is defined by linear equations with integer coefficients, so its points with rational coordinates, with respect to a basis of \(M\), are dense in it. The \(u' \in W\) with \(\langle u', v_i\rangle > 0\) for all \(i \notin I\) form an open subset of \(W\) that contains \(u\). So this subset contains a point with rational coordinates, and a positive multiple \(u'\) of that point lies in \(M\). Then \(u' \in S_\sigma\), and \(\sigma \cap u'^\perp = \sigma \cap u^\perp\) by the first step. So every face of \(\sigma\) is cut out by an element of \(S_\sigma\). Now let \(u \in S_\sigma\) and \(\tau = \sigma \cap u^\perp\). Then \(S_\sigma \subseteq S_\tau\) and \(-u \in S_\tau\). Let \(w \in S_\tau\). For \(i \in I\) we have \(\langle w, v_i\rangle \geq 0\), because \(v_i \in \tau\). For \(i \notin I\) the integer \(\langle u, v_i\rangle\) is \(\geq 1\). So there is an integer \(p \geq 0\) with \(\langle w + pu, v_i\rangle \geq 0\) for all \(i\). Then \(w + pu \in S_\sigma\) and \(w = (w + pu) + p(-u)\).

(C5) Let \(\sigma\) be strongly convex. If \(v \in N_{\mathbb{R}}\) satisfies \(\langle u, v\rangle = 0\) for all \(u \in \sigma^\vee\), then \(v\) and \(-v\) lie in \((\sigma^\vee)^\vee = \sigma\), so \(v = 0\). Hence \(\sigma^\vee\) spans \(M_{\mathbb{R}}\). By (C1) there are \(u_1, \dots, u_t \in M\) that generate \(\sigma^\vee\). Put \(u = u_1 + \dots + u_t \in S_\sigma\). If \(x \in \sigma\) and \(\langle u, x\rangle = 0\), then \(\langle u_j, x\rangle = 0\) for all \(j\), because these numbers are \(\geq 0\). So \(x = 0\), and \(\sigma \cap u^\perp = \{0\}\).

(C4) Let \(\tau = \sigma \cap \sigma'\) be a face of \(\sigma\) and of \(\sigma'\). The set \(\gamma = \{x - x' : x \in \sigma,\ x' \in \sigma'\}\) is a rational polyhedral cone: it is generated by the generators of \(\sigma\) and the negatives of the generators of \(\sigma'\). By (C1) there are \(u_1, \dots, u_t \in M\) that generate \(\gamma^\vee\). Put \(u = u_1 + \dots + u_t\). Since \(\sigma \subseteq \gamma\) and \(-\sigma' \subseteq \gamma\), we have \(u \in S_\sigma\) and \(-u \in S_{\sigma'}\). We claim that \(\sigma \cap u^\perp = \tau\). If \(x \in \tau\), then \(x\) and \(-x\) lie in \(\gamma\), so \(\langle u_j, x\rangle = 0\) for all \(j\), and \(\langle u, x\rangle = 0\). Conversely let \(x \in \sigma\) with \(\langle u, x\rangle = 0\). Then \(\langle u_j, x\rangle = 0\) for all \(j\), because these numbers are \(\geq 0\). So \(-x\) lies in \((\gamma^\vee)^\vee = \gamma\), say \(-x = y - y'\) with \(y \in \sigma\) and \(y' \in \sigma'\). Then \(x + y = y'\) lies in \(\sigma \cap \sigma' = \tau\). Write \(\tau = \sigma \cap w^\perp\) with \(w \in \sigma^\vee\). From \(\langle w, x\rangle + \langle w, y\rangle = 0\) and \(\langle w, x\rangle \geq 0\), \(\langle w, y\rangle \geq 0\) we get \(\langle w, x\rangle = 0\), so \(x \in \tau\). This proves the claim. By (C3), \(S_\tau = S_\sigma + \mathbb{Z}_{\geq 0}(-u)\). Since \(-u \in S_{\sigma'}\) and \(S_\sigma, S_{\sigma'} \subseteq S_\tau\), this gives \(S_\tau \subseteq S_\sigma + S_{\sigma'} \subseteq S_\tau\). \(\square\)

An element \(u \in S_\sigma\) with \(-u \in S_{\sigma'}\) and \(\sigma \cap u^\perp = \tau\), as in the proof of (C4), is also used in [Telen 2022, Section 4.2], where its existence is quoted without proof.

To use the multiplicative notation of this lesson, write \(\chi^u\) for the element \(u \in M\) regarded as an element of the multiplicative group \(\chi^M \cong M\), and \(\chi^S\) for the image of a subset \(S\).

**Theorem 6.11.**

1. Let \(\Delta\) be a fan in \(N\). The family \((\chi^{S_\sigma})_{\sigma \in \Delta}\) satisfies the hypotheses of Lemma 3.8 with \(G = \chi^M\). The resulting monoid scheme \(X(\Delta)\) is a toric monoid scheme. For every \(\sigma \in \Delta\) there is exactly one point \(x_\sigma\) with \(S_{x_\sigma} = \chi^{S_\sigma}\), and every point is of this form. The point \(x_\tau\) lies in \(U_{x_\sigma}\) if and only if \(\tau\) is a face of \(\sigma\), and \(\mathcal{O}_{x_\sigma}^\times\) is free abelian of rank \(n - \dim\sigma\).
2. For every ring \(k\), not only for a field, \(X(\Delta)_k\) is the scheme glued from the affine schemes \(\operatorname{Spec} k[S_\sigma]\) along the open subschemes \(\operatorname{Spec} k[S_{\sigma \cap \sigma'}]\); here \(k[S_\sigma]\) is the monoid algebra of \((\chi^{S_\sigma})_0\). For \(k = \mathbb{C}\) this is the construction of the toric variety of the fan \(\Delta\) in [Brasselet 2001, Theorem 3.1] and [Telen 2022, Section 4.2].
3. Every toric monoid scheme \(X\) is isomorphic to \(X(\Delta)\) for a fan \(\Delta\) in \(N = \operatorname{Hom}(G_X, \mathbb{Z})\).

*Proof.* (1) \(S_\sigma\) is finitely generated by (C2). By (C5) and (C3), \(\{0\} = \sigma \cap u^\perp\) for some \(u \in S_\sigma\), and \(M = S_{\{0\}} = S_\sigma + \mathbb{Z}_{\geq 0}(-u)\). So \(S_\sigma\) generates \(M\). For \(\sigma, \sigma' \in \Delta\) the cone \(\tau = \sigma \cap \sigma'\) is a face of both. By (C3), \(\tau = \sigma \cap u^\perp\) with \(u \in S_\sigma\), and by (C3) and (C4), \(S_\sigma + S_{\sigma'} = S_\tau = S_\sigma + \mathbb{Z}_{\geq 0}(-u)\). So Lemma 3.8 applies. It gives a connected, integral, separated monoid scheme \(X(\Delta)\) of finite type, with the torsion-free group \(\chi^M\), and affine open subsets \(X_\sigma = \operatorname{Spec}(\chi^{S_\sigma})_0\). Each \(S_\sigma\) is normal, because \(du \in \sigma^\vee\) implies \(u \in \sigma^\vee\). The stalks are localizations of the \((\chi^{S_\sigma})_0\), so \(X(\Delta)\) is normal.

Let \(x_\sigma\) be the closed point of \(X_\sigma\). Let \(x\) be any point. It lies in some \(X_\sigma\), and \(U_x = D(\chi^u) \subseteq X_\sigma\) for some \(u \in S_\sigma\) by Proposition 2.3. By (C3), \(S_x = \chi^{S_\tau}\) for the face \(\tau = \sigma \cap u^\perp\), which lies in \(\Delta\). By Proposition 3.9(2) the point \(x\) is determined by \(S_x\), so \(x = x_\tau\). The monoid \(S_\sigma\) determines \(\sigma\): by (C1) the cone \(\sigma^\vee\) is generated by finitely many elements of \(M\), so it is the cone generated by \(S_\sigma\), and \(\sigma = (\sigma^\vee)^\vee\). So \(\sigma \mapsto x_\sigma\) is a bijection from \(\Delta\) to \(X(\Delta)\). By (C3) every face of \(\sigma\) is \(\sigma \cap u^\perp\) with \(u \in S_\sigma\), so the points of \(U_{x_\sigma} = X_\sigma\) are the \(x_\tau\) with \(\tau\) a face of \(\sigma\). The units of \(S_\sigma\) are the \(u \in M\) that vanish on \(\sigma\). They are the lattice points of a subspace of dimension \(n - \dim\sigma\) defined by linear equations with integer coefficients, so they form a free abelian group of this rank.

(2) follows from Theorem 4.1(3), in its form for \(k\), and Lemma 3.8.

(3) Let \(X\) be a toric monoid scheme. Write \(M = G_X\) additively, so that the \(S_x\) are submonoids of \(M\), and put \(N = \operatorname{Hom}(M, \mathbb{Z})\). For \(x \in X\) let \(C_x \subseteq M_{\mathbb{R}}\) be the cone generated by \(S_x\), and \(\sigma_x = C_x^\vee \subseteq N_{\mathbb{R}}\). The cone \(C_x\) is generated by a finite set of generators of \(S_x\). By (C1), with \(M\) and \(N\) exchanged, \(\sigma_x\) is a rational polyhedral cone and \(\sigma_x^\vee = C_x\). It is strongly convex: if \(v\) and \(-v\) lie in \(\sigma_x\), then \(v\) vanishes on \(S_x\), which spans \(M_{\mathbb{R}}\), so \(v = 0\).

*Claim a: \(S_x = C_x \cap M = S_{\sigma_x}\).* Let \(u \in C_x \cap M\), and let \(g_1, \dots, g_p\) generate \(S_x\). Write \(u = \sum \lambda_ig_i\) with real \(\lambda_i \geq 0\) and as few nonzero \(\lambda_i\) as possible. Then the \(g_i\) with \(\lambda_i > 0\) are linearly independent. Otherwise a linear relation among them could be subtracted, with a suitable factor, to make one more coefficient zero while all stay \(\geq 0\). So the \(\lambda_i\) are the unique solution of a system of linear equations with rational coefficients, and they are rational. Hence \(du \in S_x\) for some \(d \geq 1\), and \(u \in S_x\) because \(S_x\) is normal.

*Claim b: for \(y \in U_x\) the cone \(\sigma_y\) is a face of \(\sigma_x\), and every face of \(\sigma_x\) is \(\sigma_y\) for some \(y \in U_x\).* We have \(U_y = D(\chi^u)\) in \(U_x\) for some \(u \in S_x\), so \(S_y = S_x + \mathbb{Z}_{\geq 0}(-u)\). By (C3) and Claim a, \(S_y = S_\tau\) for the face \(\tau = \sigma_x \cap u^\perp\). Then \(\sigma_y^\vee = C_y\) and \(\tau^\vee\) are both the cone generated by \(S_y = S_\tau\), so \(\sigma_y = \tau\) by (C1). Conversely a face of \(\sigma_x\) is \(\tau = \sigma_x \cap u^\perp\) with \(u \in S_{\sigma_x} = S_x\) by (C3), and then \(\tau = \sigma_y\) for the closed point \(y\) of \(D(\chi^u)\).

*Claim c: \(\sigma_x \cap \sigma_{x'} = \sigma_z\), where \(U_x \cap U_{x'} = U_z\).* Such a \(z\) exists by Proposition 3.9(1), and \(S_z = S_x + S_{x'}\). So \(C_z = C_x + C_{x'}\). A linear form is \(\geq 0\) on \(C_x + C_{x'}\) if and only if it is \(\geq 0\) on \(C_x\) and on \(C_{x'}\). By Claim b, \(\sigma_z\) is a face of \(\sigma_x\) and of \(\sigma_{x'}\).

So \(\Delta = \{\sigma_x : x \in X\}\) is a fan. By Claim a, the monoids \(S_x\), \(x \in X\), are the monoids \(S_\sigma\), \(\sigma \in \Delta\). By Proposition 3.9(3), \(X \cong X(\Delta)\). \(\square\)

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Construction 4.2 and Theorem 4.4].

Together, Theorems 6.8 and 6.11 show that every toric variety over an algebraically closed field is the toric variety of a fan. For \(k = \mathbb{C}\) this statement is given without proof in [Telen 2022, Section 4.2] and in [Brasselet 2001, Theorem 4.3].

**Example 6.12.** \(\mathbb{P}^n\) is a toric monoid scheme: by Proposition 5.2 it is connected, integral, separated and of finite type, the group \(G_n\) is torsion-free, and the monoids \(S_I\) are normal. Its fan lies in \(N = \mathbb{Z}^{n+1}/\mathbb{Z}(1, \dots, 1)\), whose dual is \(M = \{a \in \mathbb{Z}^{n+1} : \sum a_j = 0\}\). The cone of \(x_I\) is generated by the classes of the basis vectors \(e_j\) with \(j \notin I\), because the dual of this cone is \(\{a \in M_{\mathbb{R}} : a_j \geq 0 \text{ for } j \notin I\}\), the cone generated by \(S_I\). By Proposition 5.2(5) and Theorem 6.8, \(\mathbb{P}^n_k\) is a toric variety. Affine space \(\mathbb{A}^n\) and the tori \(\mathbb{G}_m^n\) are toric monoid schemes as well.

### 6.6 Strong congruences and dimension

The spectrum of a monoid does not see dimension: the spectrum of a group with zero is a point
(*Commutative monoids and their spectra*, Remark 6.8). That remark describes the strong congruence spaces of
[Jarra 2023a], which repair this. We prove here that for toric monoid schemes they have the expected dimension.

Throughout, \(F\) is a commutative group with zero such that for every \(\alpha\in F^\times\) and every \(n\geq1\) the
equation \(x^n=\alpha\) has exactly \(n\) solutions in \(F\); for example, the complex roots of unity together with
\(0\). A monoid is a *domain* if it is isomorphic to a submonoid of the multiplicative monoid of a field. For an
additive submonoid \(S\) of a lattice put
\[
F[S]=\{0\}\sqcup\{\lambda\chi^s\ :\ \lambda\in F^\times,\ s\in S\},\qquad(\lambda\chi^s)(\mu\chi^t)=\lambda\mu\chi^{s+t},
\]
with \(0\) absorbing; \(F=F[\{0\}]\) is a submonoid. An *\(F\)-congruence* on \(F[S]\), or on a localization of it, is
a congruence \(\mathfrak c\) such that the quotient is a domain and \(F\) maps injectively to it. The *strong congruence
space* \(\operatorname{SCong}_FF[S]\) is the set of \(F\)-congruences, with the topology generated by the sets
\(U_{a,b}=\{\mathfrak c:a\not\sim_{\mathfrak c}b\}\). A *face* of \(S\) is a submonoid \(P\ni0\) such that \(s+t\in P\)
with \(s,t\in S\) implies \(s,t\in P\).

**Lemma 6.13 (the base).** (a) \(F\) is isomorphic to a submonoid of the multiplicative monoid of a field \(K\).
(b) Let \(B\) be a domain into which \(F\) maps injectively, and \(G_B\) the group of units of its group completion. If
\(g\in G_B\) and \(g^m\in F^\times\) for some \(m\geq1\), then \(g\in F^\times\).
(c) \(F[S]\) is a domain for every submonoid \(S\) of a lattice.

*Proof.* (a) Let \(G=F^\times\) and \(T\) its torsion subgroup. The hypothesis makes \(G\) and \(T\) divisible. For a
prime \(p\) the solutions of \(x^{p^k}=1\) form a group \(\mu_{p^k}\) with exactly \(p^k\) elements; a generator
\(\zeta_1\) of the group \(\mu_p\) of order \(p\) and successive roots \(\zeta_{k+1}^p=\zeta_k\) show that \(\mu_{p^k}\) is
cyclic. So the \(p\)-primary part of \(T\) is the Prüfer group, and \(T\) is isomorphic to the group of complex roots
of unity. A divisible group is a direct summand of every abelian group containing it: by Zorn's lemma extend the
identity of \(T\) to a maximal homomorphism \(\varphi\colon A'\to T\) with \(T\subseteq A'\subseteq G\); if \(b\notin A'\),
let \(m\) be the least positive integer with \(b^m\in A'\), or \(m=0\) if there is none, choose \(d\in T\) with
\(d^m=\varphi(b^m)\) (any \(d\) if \(m=0\)), and extend by \(ab^k\mapsto\varphi(a)d^k\), which is well defined because the
\(k\) with \(b^k\in A'\) form \(m\mathbb Z\); maximality forces \(A'=G\). So \(G\cong T\times V\) with \(V\)
torsion-free. The group algebra \(\mathbb C[V]\) is a domain, since two of its elements lie in \(\mathbb C[V_0]\) for a
finitely generated, hence free, subgroup \(V_0\), and \(\mathbb C[V_0]\) is a ring of Laurent polynomials. Then
\((t,v)\mapsto tX^v\), extended by \(0\mapsto0\), embeds \(F\) into \(K=\operatorname{Frac}\mathbb C[V]\).

(b) \(G_B\) embeds into the multiplicative group of a field containing \(B\) (*Commutative monoids and their spectra*,
Proposition 7.5). If \(g^m=\lambda\in F^\times\), the \(m\) distinct roots of \(x^m=\lambda\) in \(F\) are all the roots
of this polynomial in that field, so \(g\) is one of them.

(c) By (a), \(F[S]\) embeds into the field of fractions of the Laurent polynomial ring over \(K\) of the lattice.
\(\square\)

**Lemma 6.14 (faces of lattice monoids).** Let \(S\) be a finitely generated submonoid of a lattice, \(L\) the group it
generates, \(d=\operatorname{rank}L\), and \(C=\mathbb R_{\geq0}S\subseteq L_{\mathbb R}\).

(a) \(P\mapsto\mathbb R_{\geq0}P\) is a bijection from the faces of \(S\) onto the faces of \(C\), with inverse
\(D\mapsto S\cap D\), and the group generated by \(P\) has rank \(\dim\mathbb R_{\geq0}P\). A face \(P\neq S\) has
rank less than \(d\).

(b) If \(P\) is a face of rank at most \(d-2\), there is a face \(E\) with \(P\subsetneq E\subsetneq S\).

*Proof.* (a) Let \(s_1,\dots,s_r\) generate \(S\). A face \(P\) is generated by the \(s_i\) that lie in it. Let
\(D=\mathbb R_{\geq0}P\), and let \(x,y\in C\) with \(x+y\in D\). Writing \(x\) and \(y\) with the \(s_i\) and \(x+y\) with
the generators of \(P\), we get an equation with positive real coefficients; by *Commutative monoids and their
spectra*, Lemma 9.5, applied to the difference, there is one with positive integer coefficients and the same vectors.
Its right side lies in \(P\), so by the face property every \(s_i\) used for \(x\) or \(y\) lies in \(P\), and
\(x,y\in D\). If \(s\in S\cap D\), the same lemma gives \(ms\in P\) for some \(m\geq1\), and the face property gives
\(s\in P\). Conversely, for a face \(D\) of \(C\), \(S\cap D\) is a face of \(S\), and \(D=\mathbb R_{\geq0}(S\cap D)\) by
Lemma 9.9 of that lesson. The rank statement holds because \(P\) spans \(\mathbb R_{\geq0}P-\mathbb R_{\geq0}P\). A face
\(D\neq C\) contains no interior point of \(C\): if \(x\in D\) were interior, then for \(c\in C\) and small
\(\varepsilon>0\), \(x=(x-\varepsilon c)+\varepsilon c\) with both terms in \(C\) would give \(c\in D\). As \(C\) spans
\(L_{\mathbb R}\), a face of full dimension would contain interior points; so \(\dim D<d\).

(b) By Facts 6.10(C1), applied to the lattice \(L\), \(C^\vee\) is generated by finitely many \(u_1,\dots,u_t\) and
\(C=\{x:u_k(x)\geq0\text{ for all }k\}\). Discard zero forms and, one at a time, redundant inequalities, to get an
irredundant description \(C=\{x:\ell_1(x)\geq0,\dots,\ell_q(x)\geq0\}\). Let \(D=\mathbb R_{\geq0}P\), \(x\) the sum of
the generators of \(D\), and \(c_0\) an interior point of \(C\), so that every \(\ell_j(c_0)>0\). Since \(x\) is not
interior, some \(\ell_i(x)=0\), and then \(\ell_i\) vanishes on \(D\), the \(\ell_i\) of the generators being
\(\geq0\). Let \(E'=C\cap\ker\ell_i\), a face of \(C\) containing \(D\). By irredundancy there is \(y\) with
\(\ell_i(y)<0\) and \(\ell_j(y)\geq0\) for \(j\neq i\); on the segment from \(c_0\) to \(y\) the point \(w\) with
\(\ell_i(w)=0\) has \(\ell_j(w)>0\) for \(j\neq i\), so a neighbourhood of \(w\) in \(\ker\ell_i\) lies in \(E'\), and
\(\dim E'=d-1\). If \(\dim D\leq d-2\), then \(D\subsetneq E'\subsetneq C\), and \(E=S\cap E'\) is the required face.
\(\square\)

**Theorem 6.15 (\(F\)-congruences on \(F[S]\)).** Let \(S\) be a finitely generated submonoid of a lattice, generating
\(L\), with \(d=\operatorname{rank}L\).

(a) For an \(F\)-congruence \(\mathfrak c\), let \(P_{\mathfrak c}=\{s:\chi^s\not\sim_{\mathfrak c}0\}\), \(L_{\mathfrak c}\) the
group generated by \(P_{\mathfrak c}\), \(\varphi_{\mathfrak c}\colon L_{\mathfrak c}\to G_B\), \(s-t\mapsto[\chi^s][\chi^t]^{-1}\),
where \(B=F[S]/\mathfrak c\), \(H_{\mathfrak c}=\varphi_{\mathfrak c}^{-1}(F^\times)\) and \(\rho_{\mathfrak c}=\varphi_{\mathfrak c}|_{H_{\mathfrak c}}\).
Then \(P_{\mathfrak c}\) is a face, \(H_{\mathfrak c}\) is primitive in \(L_{\mathfrak c}\) (the quotient is torsion-free),
all \(\chi^s\) with \(s\notin P_{\mathfrak c}\) are equivalent to \(0\), and for \(s,t\in P_{\mathfrak c}\),
\(a,b\in F^\times\),
\[
a\chi^s\sim_{\mathfrak c}b\chi^t\iff s-t\in H_{\mathfrak c}\ \text{ and }\ a\rho_{\mathfrak c}(s-t)=b.
\tag{6.4}
\]
(b) Conversely, every triple \((P,H,\rho)\) of a face \(P\), a primitive subgroup \(H\) of the group \(L_P\) generated by
\(P\), and a homomorphism \(\rho\colon H\to F^\times\) comes from exactly one \(F\)-congruence, whose quotient is
isomorphic to \(F[Q]\), \(Q\) the image of \(P\) in the lattice \(L_P/H\).

(c) Put \(h_S(\mathfrak c)=d-\operatorname{rank}L_{\mathfrak c}+\operatorname{rank}H_{\mathfrak c}\). Then
\(0\leq h_S(\mathfrak c)\leq d\), and \(h_S(\mathfrak c)=0\) only for the equality congruence \(\Delta_S\). If
\(\mathfrak c\subsetneq\mathfrak c'\), then \(h_S(\mathfrak c)<h_S(\mathfrak c')\).

*Proof.* (a) In the domain \(B\) a product is \(0\) only if a factor is, so \(P_{\mathfrak c}\) is a face. If
\(mh\in H_{\mathfrak c}\), then \(\varphi_{\mathfrak c}(h)^m\in F^\times\), so \(\varphi_{\mathfrak c}(h)\in F^\times\) by
Lemma 6.13(b). In \(B\), \([a\chi^s]=[b\chi^t]\) means \([\chi^s][\chi^t]^{-1}=b/a\) in \(G_B\), which is (6.4).

(b) Write \(L_P=H\oplus H'\) (as \(L_P/H\) is free), extend \(\rho\) by \(1\) on \(H'\) to \(\tilde\rho\), let
\(\pi\colon L_P\to L_P/H\), and define \(q\colon F[S]\to F[Q]\) by \(q(a\chi^s)=a\tilde\rho(s)\chi^{\pi(s)}\) for \(s\in P\) and
\(q(a\chi^s)=0\) otherwise. It is multiplicative by the face property, surjective, the identity on \(F\), and \(F[Q]\) is
a domain by Lemma 6.13(c). Its kernel congruence has the triple \((P,H,\rho)\), by (6.4); and by (a) a congruence is
determined by its triple.

(c) The group \(G_B\) is generated by \(F^\times\) and the classes of the \(\chi^s\), \(s\in P_{\mathfrak c}\), so
\(G_B/F^\times\cong L_{\mathfrak c}/H_{\mathfrak c}\) has rank \(\delta(\mathfrak c)=\operatorname{rank}L_{\mathfrak c}-
\operatorname{rank}H_{\mathfrak c}\), and \(h_S=d-\delta\). If \(h_S(\mathfrak c)=0\), then \(\operatorname{rank}L_{\mathfrak c}=
d\) and \(H_{\mathfrak c}=0\); so \(P_{\mathfrak c}=S\) by Lemma 6.14(a), and (6.4) says that \(\mathfrak c=\Delta_S\). If
\(\mathfrak c\subseteq\mathfrak c'\), the congruences on \(B=F[S]/\mathfrak c\cong F[Q]\) correspond to the congruences on
\(F[S]\) that contain \(\mathfrak c\), with the same quotients (*Commutative monoids and their spectra*, Proposition 6.2);
let \(\mathfrak d\) correspond to \(\mathfrak c'\). The group generated by \(Q\) has rank \(\delta(\mathfrak c)\), so
\(h_Q(\mathfrak d)=\delta(\mathfrak c)-\delta(\mathfrak c')=h_S(\mathfrak c')-h_S(\mathfrak c)\). If \(\mathfrak c\neq\mathfrak c'\),
then \(\mathfrak d\neq\Delta_Q\), and \(h_Q(\mathfrak d)>0\). \(\square\)

**Lemma 6.16 (covers).** If \(\mathfrak c\subsetneq\mathfrak c'\) are \(F\)-congruences on \(F[S]\) with no \(F\)-congruence
strictly between them, then \(h_S(\mathfrak c')=h_S(\mathfrak c)+1\).

*Proof.* As in the proof of Theorem 6.15(c), it suffices to show \(h_Q(\mathfrak d)=1\) for a minimal \(F\)-congruence
\(\mathfrak d\neq\Delta_Q\) on \(F[Q]\), with \(Q\) a finitely generated submonoid of a lattice of rank \(r\) generated by
\(Q\). Let \((P,H,\rho)\) be its triple. For a face \(E\) let \(\mathfrak e_E\) be the congruence with triple
\((E,0,1)\), which identifies all \(\chi^s\), \(s\notin E\), with \(0\) and nothing else. If \(P\neq Q\), then
\(\Delta_Q\subsetneq\mathfrak e_P\subseteq\mathfrak d\), so \(\mathfrak d=\mathfrak e_P\) and \(H=0\); if \(P\) had rank at
most \(r-2\), Lemma 6.14(b) would give a face \(E\) with \(\Delta_Q\subsetneq\mathfrak e_E\subsetneq\mathfrak e_P\); so
\(P\) has rank \(r-1\) and \(h_Q(\mathfrak d)=1\). If \(P=Q\), then \(H\neq0\); for an element \(z\) of a basis of \(H\),
which extends to a basis of the group generated by \(Q\) since \(H\) is primitive, the triple \((Q,\mathbb Zz,\rho|_{\mathbb Zz})\)
gives a congruence \(\neq\Delta_Q\) contained in \(\mathfrak d\); so \(H=\mathbb Zz\) and \(h_Q(\mathfrak d)=1\). \(\square\)

So, by Theorem 6.15(c) and Lemma 6.16, every maximal chain of \(F\)-congruences from \(\mathfrak c\) to
\(\mathfrak c'\supseteq\mathfrak c\) has length \(h_S(\mathfrak c')-h_S(\mathfrak c)\).

**Theorem 6.17 (affine strong congruence spaces).** Let \(S\) be a finitely generated submonoid of a lattice. Then
\(Y=\operatorname{SCong}_FF[S]\) is a Noetherian, sober and catenary space of Krull dimension equal to the rank of the
group generated by \(S\). In particular, for a strongly convex rational polyhedral cone \(\sigma\subseteq N_{\mathbb R}\)
of a lattice \(N\) of rank \(n\), \(\operatorname{SCong}_FF[S_\sigma]\) is catenary of dimension \(n\).

*Proof.* The closure of a point \(\mathfrak c\) is \(\{\mathfrak d:\mathfrak c\subseteq\mathfrak d\}\): if
\(\mathfrak c\subseteq\mathfrak d\), every \(U_{a,b}\) containing \(\mathfrak d\) contains \(\mathfrak c\); if
\((a,b)\in\mathfrak c\setminus\mathfrak d\), then \(U_{a,b}\) contains \(\mathfrak d\) but not \(\mathfrak c\). So \(Y\) is
\(T_0\). With \(K\) as in Lemma 6.13(a) and \(\iota\colon F[S]\to K[S]\) into the monoid algebra, send a prime ideal
\(\mathfrak p\) of \(K[S]\) to the kernel congruence of \(F[S]\to\operatorname{Frac}(K[S]/\mathfrak p)\). This map
\(\gamma\colon\operatorname{Spec}K[S]\to Y\) is continuous, as \(\gamma^{-1}(U_{a,b})=D(\iota(a)-\iota(b))\), and
surjective: for the triple \((P,H,\rho)\) of a congruence, the map \(q\) of Theorem 6.15(b) extends \(K\)-linearly to a ring
homomorphism \(K[S]\to K[Q]\) onto a domain, whose kernel is a prime ideal with image the given congruence. As
\(K[S]\) is a finitely generated \(K\)-algebra, it is Noetherian (Hilbert's basis theorem), so \(\operatorname{Spec}K[S]\)
and its continuous image \(Y\) are Noetherian spaces. If \(Z\subseteq Y\) is closed and irreducible, \(\gamma^{-1}(Z)\) has
finitely many irreducible components, with generic points \(\eta_i\), and \(Z\) is the union of the closures of the
\(\gamma(\eta_i)\); by irreducibility \(Z\) is one of them, so \(Y\) is sober. Hence chains of irreducible closed subsets
are chains of congruences in the reverse order, and the remark after Lemma 6.16 gives catenarity and dimension at most
\(d\). For a basis \(z_1,\dots,z_d\) of the group \(L\) generated by \(S\), the triples \((S,\mathbb Zz_1+\dots+\mathbb Zz_i,1)\)
give a chain of length \(d\). For \(S_\sigma=\sigma^\vee\cap M\), \(S_\sigma\) is finitely generated and generates \(M\),
by Facts 6.10(C2) and the proof of Theorem 6.11(1). \(\square\)

**Lemma 6.18 (localization).** Let \(A=F[S]\) and \(f\in A\). Restriction along \(A\to A_f\) is a homeomorphism from
\(\operatorname{SCong}_FA_f\) onto the open subset \(U_{f,0}\) of \(\operatorname{SCong}_FA\).

*Proof.* For an \(F\)-congruence \(\mathfrak c\) on \(A\) with \(f\not\sim_{\mathfrak c}0\), embed \(A/\mathfrak c\) into a field
and invert the image of \(f\): this gives the \(F\)-congruence \(a/f^r\sim b/f^s\iff af^s\sim_{\mathfrak c}bf^r\) on
\(A_f\), the only one restricting to \(\mathfrak c\). The two constructions are inverse, and
\(U_{a/f^r,b/f^s}\) corresponds to \(U_{f,0}\cap U_{af^s,bf^r}\). \(\square\)

For a fan \(\Delta\) in \(N\) (Section 6.5), let \(X_F(\Delta)\) be the toric monoid scheme over \(F\), glued from the
\(\operatorname{Spec}F[S_\sigma]\), \(\sigma\in\Delta\), as in Theorem 6.11(1) with the group \(F^\times\times\chi^M\) in place of
\(\chi^M\). For a face \(\tau\) of \(\sigma\),
\(F[S_\tau]=F[S_\sigma]_{\chi^u}\) by Facts 6.10(C3), so Lemma 6.18 identifies
\(\operatorname{SCong}_FF[S_\tau]\) with an open subspace of \(\operatorname{SCong}_FF[S_\sigma]\); these identifications
are compatible, and the strong congruence space \(\operatorname{SCong}_FX_F(\Delta)\) is the space glued from the
\(\operatorname{SCong}_FF[S_\sigma]\) along them. An affine open subset of \(X_F(\Delta)\) lies in every chart that contains its closed point, and is principal
there (Proposition 2.3); so gluing over all affine open subsets gives the same space, which is how [Jarra 2023a]
defines it.

**Theorem 6.19 (Jarra's dimension theorem).** For a fan \(\Delta\) in a lattice \(N\) of rank \(n\),
\(\operatorname{SCong}_FX_F(\Delta)\) is sober and catenary, and its Krull dimension is \(n\), the dimension of the complex
toric variety of \(\Delta\).

*Proof.* The charts \(Y_\sigma=\operatorname{SCong}_FF[S_\sigma]\) are open, sober and \(T_0\) (Theorem 6.17), so the glued
space \(Y\) is \(T_0\) and sober: an irreducible closed \(Z\) meets some chart \(Y_\sigma\), the generic point of
\(Z\cap Y_\sigma\) is dense in \(Z\), and its closure is \(Z\). Open sets are stable under generalization, so a chain of
points ending in a point \(y\) lies in every chart containing \(y\), and its maximal refinements are those in that chart.
By Theorem 6.17, \(Y\) is catenary, every chain has length at most \(n\), and each chart contains one of length \(n\). The
complex toric variety of \(\Delta\) is glued from the \(\operatorname{Spec}\mathbb C[S_\sigma]\) (Theorem 6.11(2)); as
\(S_\sigma\) generates \(M\), each \(\mathbb C[S_\sigma]\) is a finitely generated domain with fraction field
\(\mathbb C(M)\), of transcendence degree \(n\), so it has dimension \(n\) ([Stacks, Tag [00P0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-prime-polynomial-ring)]), and so has the variety
([Stacks, Tag [0B7I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-dimension-supremum-local-dimensions)]). \(\square\)

**Corollary 6.20 (the torus).** The \(F\)-congruences on \(F[\mathbb Z^n]\) are exactly the congruences generated by
relations \(\chi^{z_i}\sim\lambda_i\), \(1\le i\le c\), where \(z_1,\dots,z_c\) is part of a basis of \(\mathbb Z^n\) and
\(\lambda_i\in F^\times\).

*Proof.* Every nonzero element of \(F[\mathbb Z^n]\) is a unit, so the face of an \(F\)-congruence is \(\mathbb Z^n\), and its
triple is \((\mathbb Z^n,H,\rho)\). For a basis \(z_1,\dots,z_c\) of the primitive subgroup \(H\), which extends to a basis
of \(\mathbb Z^n\), the relations \(\chi^{z_i}\sim\rho(z_i)\) generate \(\chi^h\sim\rho(h)\) for all \(h\in H\), because the
\(\chi^{z_i}\) and \(\rho(z_i)\) are units; by (6.4) the congruence they generate is the given one. Conversely, for such
\(z_i\) and \(\lambda_i\), the quotient is \(F[\mathbb Z^{n-c}]\), a domain containing \(F\). \(\square\)

**Remark 6.21 (the argument of [Jarra 2023a]).** Theorems 5.13 and 5.15 of [Jarra 2023a] (third arXiv version) state
Theorem 6.17 for the monoids \(S_\sigma\) and Theorem 6.19, and Proposition 6.1 there is Corollary 6.20. The proof of
Theorem 5.13 there extends concatenated bases of two primitive subgroups \(H\), \(K\) with \(H\cap K=0\) to a basis of the
lattice, by its Lemma 5.12, which is false (*Commutative monoids and their spectra*, Remark 6.8). The failure occurs in
the situation of that proof. Take \(L=\mathbb Z^3\), \(v=(1,1,2)\), \(C=\operatorname{cone}(e_1,e_2,v)\),
\(S=C\cap L\), \(H=\mathbb Z(1,-1,0)\), \(K=\mathbb Zv\). The kernel congruence \(\mathfrak r\) of
\(F[S]\to F[\pi(S)]\), \(\pi(x,y,z)=(x+y,z)\), has triple \((S,H,1)\), and the congruence \(\mathfrak r'\) with triple
\((\mathbb Nv,0,1)\) contains it, because \(\ell=x+y-z\) is \(\geq0\) on \(C\), vanishes exactly on \(\mathbb R_{\geq0}v\),
and is constant on the fibres of \(\pi\), which is injective on \(\mathbb Nv\). Their heights are \(1\) and \(2\), so
\(\mathfrak r\subsetneq\mathfrak r'\) is a cover. Yet \(w=(1,0,1)\) satisfies \(2w=(1,-1,0)+v\in H+K\) and \(w\notin H+K\),
so \(L/(H+K)\) has torsion and no concatenation of bases of \(H\) and \(K\) extends to a basis of \(L\). The quotient
monoids need not be saturated either: for \(S=\mathbb N^3\) and \(\pi(x,y,z)=(3x+2y,z)\), the image \(\pi(S)\) misses
\((1,0)\) although \(2(1,0)\in\pi(S)\). The proof above therefore works with arbitrary finitely generated submonoids of
lattices and replaces the basis extension by Lemma 6.16.

## 7. The zeta function

The zeta function of a variety over \(\mathbb{F}_q\) is built from its numbers of points over the fields \(\mathbb{F}_{q^r}\). When these numbers are given by a polynomial in \(q^r\), one can let \(q\) tend to \(1\).

**Lemma 7.1.** Let \(N(t) = \sum_{j=0}^d a_jt^j\) be a polynomial with integer coefficients.

1. In the ring of formal power series in \(T\) over \(\mathbb{Q}[q]\),
\[
Z(q, T) := \exp\Bigl(\sum_{r \geq 1} N(q^r)\frac{T^r}{r}\Bigr) = \prod_{j=0}^d (1 - q^jT)^{-a_j}.
\]
2. For a real number \(q > 1\) and \(s \in \mathbb{C}\) put \(Z(q, q^{-s}) = \prod_j (1 - q^{j-s})^{-a_j}\). For \(\operatorname{Re}(s) > d\) this is the value of the series at \(T = q^{-s}\). Let \(s \in \mathbb{C}\) be different from every \(j\) with \(a_j < 0\). Then
\[
\lim_{q \to 1}\ (q-1)^{-N(1)}\, Z(q, q^{-s})^{-1} = \prod_{j=0}^d (s - j)^{a_j}.
\]

*Proof.* (1) \(\sum_{r \geq 1} q^{jr}T^r/r = -\log(1 - q^jT)\). (2) If \(\operatorname{Re}(s) > d\) and \(q > 1\), then \(|q^{j-s}| < 1\) for \(j \leq d\), so the series converges to \(-\sum_j a_j\log(1 - q^{j-s})\). For each \(j\) we have \(q^{j-s} = \exp((j-s)\log q) = 1 + (j-s)(q-1) + O((q-1)^2)\) as \(q \to 1\). So \((1 - q^{j-s})/(q-1)\) tends to \(s - j\). The product of the \(a_j\)-th powers of these quotients is \((q-1)^{-N(1)}Z(q,q^{-s})^{-1}\). The power with exponent \(a_j\) is continuous at \(s - j\) if \(a_j \geq 0\) or \(s \neq j\). \(\square\)

*Reference:* [Soulé 2004, Section 6, Lemme 1].

**Definition 7.2.** Let \(X\) be a monoid scheme of finite type, and write \(P_X(t-1) = \sum_{j=0}^d a_jt^j\) with \(P_X\) as in Corollary 4.5. The *zeta function* of \(X\) is the rational function
\[
\zeta_X(s) = \prod_{j=0}^{d} (s - j)^{a_j}.
\]

Suppose that all groups \(\mathcal{O}_{X,x}^\times\) are torsion-free. Then \(N_X(q) = P_X(q-1)\) for all prime powers \(q\) by Theorem 4.7. For a prime power \(q\) the series \(Z(q,T)\) of Lemma 7.1, for \(N(t) = P_X(t-1)\), is the zeta function \(\exp(\sum_r \# X_{\mathbb{F}_q}(\mathbb{F}_{q^r})T^r/r)\) of the scheme \(X_{\mathbb{F}_q}\) over \(\mathbb{F}_q\). Lemma 7.1 says that \(\zeta_X(s)\) is the limit of \((q-1)^{-N(1)}Z(q, q^{-s})^{-1}\) for \(q \to 1\), after \(q\) is made a real variable. If some unit group has torsion, \(P_X(t-1)\) gives the number of points only for the \(q\) with \(\gcd(q-1, e_X) = 1\) (Corollary 4.5), and \(\zeta_X\) is defined by the same formula. *Reference:* [Deitmar 2006]; [Deitmar–Koyama–Kurokawa 2008, Section 1].

**Remark 7.3 (two conventions).** This lesson uses the convention of [Soulé 2004, Section 6, Lemme 1], which is also that of [Deitmar 2006] and [Deitmar–Koyama–Kurokawa 2008, Section 1]: \(\zeta_X(s)\) is the limit of \((q-1)^{-N(1)}Z(q,q^{-s})^{-1}\), that is, \(\prod_j (s-j)^{a_j}\). It is a polynomial when all \(a_j \geq 0\). [Connes–Consani 2010, Section 2] defines the zeta function as the limit of \((q-1)^{N(1)}Z(q,q^{-s})\), that is, \(\prod_j (s-j)^{-a_j}\). This is the reciprocal of ours. For \(N(t) = t^d\) we have \(Z(q, q^{-s}) = (1 - q^{d-s})^{-1}\) and \(1 - q^{d-s} = (s-d)(q-1) + O((q-1)^2)\). So our convention gives \(s - d\) and the other gives \(1/(s-d)\). With the convention of [Connes–Consani 2010] the zeta function of \(\mathbb{P}^1\) is \(1/(s(s-1))\); it has poles where ours has zeros.

**Proposition 7.4 (localization formula).** Let \(X\) be of finite type. Then
\[
\zeta_X(s) = \prod_{x \in X} \zeta_{r(x)}(s), \qquad \zeta_r(s) := \prod_{j=0}^{r} (s-j)^{(-1)^{r-j}\binom{r}{j}} ,
\]
where \(r(x)\) is the rank of \(\mathcal{O}_{X,x}^\times\). The factor \(\zeta_r\) is the zeta function of the torus \(\mathbb{G}_m^r\).

*Proof.* \(P_X(t-1) = \sum_x (t-1)^{r(x)}\) and \((t-1)^r = \sum_j (-1)^{r-j}\binom{r}{j}t^j\). The exponents \(a_j\) are additive in the polynomial. \(\square\)

*Reference:* [Deitmar–Koyama–Kurokawa 2008, Proposition 1.2].

**Examples 7.5.** In each case we give \(P_X(t)\), the polynomial \(P_X(t-1)\) and \(\zeta_X(s)\).

1. \(\operatorname{Spec}\mathbb{F}_1\): \(1\), \(1\), and \(\zeta(s) = s\).
2. \(\mathbb{A}^n\): the point \(\mathfrak{p}_I\) has unit group of rank \(n - |I|\). So \(P(t) = (t+1)^n\), \(P(t-1) = t^n\), and \(\zeta(s) = s - n\).
3. \(\mathbb{G}_m^n\): \(t^n\), \((t-1)^n\), and \(\zeta = \zeta_n\). For example \(\zeta_1(s) = (s-1)/s\) and \(\zeta_2(s) = s(s-2)/(s-1)^2\). *Reference:* [Deitmar 2005, Section 6] prints \(s/(s-1)\) for \(\mathbb{G}_m\); the formula of that section gives \((s-1)/s\), as in [Soulé 2004, 6.3.3].
4. \(\mathbb{P}^n\): by Proposition 5.2, \(P(t-1) = 1 + t + \dots + t^n\) and \(\zeta(s) = s(s-1)\cdots(s-n)\).
5. The line with a doubled origin \(L\): \(P(t) = t + 2\), \(P(t-1) = t + 1\), \(\zeta(s) = s(s-1)\), as for \(\mathbb{P}^1\). The zeta function does not see separatedness.
6. The cusp \(\operatorname{Spec}\mathbb{F}_1[t^2,t^3]\): two points, with unit groups \(t^{\mathbb{Z}}\) and \(1\). So \(P(t-1) = t\) and \(\zeta(s) = s - 1\), as for \(\mathbb{A}^1\). The zeta function does not see normality.
7. \(\operatorname{Spec}\mathbb{F}_{1^2}\): \(P = 1\) and \(\zeta(s) = s\), as for a point, although \(N_X(q)\) is not constant (Example 4.6). The zeta function does not see torsion.
8. The monoid scheme \(X(\Delta)\) of a fan in a lattice of rank \(n\) with \(f_i\) cones of dimension \(i\): by Theorem 6.11, \(P(t) = \sum_i f_it^{n-i}\) and \(P(t-1) = \sum_i f_i(t-1)^{n-i}\). So \(\zeta(s) = \prod_j (s-j)^{a_j}\) with \(a_j = \sum_{i=0}^{n-j} (-1)^{n-i-j}\binom{n-i}{j}f_i\). *Reference:* [Deitmar 2008, Proposition 4.3].
9. A singular example. Let \(\sigma \subseteq \mathbb{R}^2\) be the cone generated by \((0,1)\) and \((2,-1)\), and \(\Delta\) the fan of its faces. Then \(S_\sigma = \{(a,b) \in \mathbb{Z}^2 : 0 \leq b \leq 2a\}\) is generated by \((1,0)\), \((1,1)\), \((1,2)\): if \(b \leq a\) then \((a,b) = (a-b)(1,0) + b(1,1)\), and if \(b > a\) then \((a,b) = (2a-b)(1,1) + (b-a)(1,2)\). These three elements are not sums of two nonzero elements of \(S_\sigma\), because every nonzero element has \(a \geq 1\). A free commutative monoid with group \(\mathbb{Z}^2\) has only two such elements. So \(S_\sigma\) is not free, and \(X(\Delta) = \operatorname{Spec}(\chi^{S_\sigma})_0\) is not isomorphic to \(\mathbb{A}^2\). But \(f_0 = 1\), \(f_1 = 2\), \(f_2 = 1\) give \(P(t-1) = (t-1)^2 + 2(t-1) + 1 = t^2\) and \(\zeta(s) = s - 2\), as for \(\mathbb{A}^2\).

**Proposition 7.6 (sums and products).** Let \(X\) and \(Y\) be monoid schemes of finite type, and \(X \times Y = X \times_{\operatorname{Spec}\mathbb{F}_1} Y\).

1. \(P_{X \sqcup Y} = P_X + P_Y\) and \(\zeta_{X \sqcup Y} = \zeta_X\zeta_Y\).
2. \(P_{X \times Y} = P_XP_Y\). If \(P_X(t-1) = \sum_i a_it^i\) and \(P_Y(t-1) = \sum_j b_jt^j\), then \(\zeta_{X \times Y}(s) = \prod_{i,j} (s - i - j)^{a_ib_j}\).

*Proof.* (1) is clear. (2) The monoid scheme \(X \times Y\) is of finite type: it is covered by finitely many open subschemes \(\operatorname{Spec}(M \otimes_{\mathbb{F}_1} M')\) with \(M\) and \(M'\) finitely generated, and then \(M \otimes_{\mathbb{F}_1} M'\) is finitely generated. By Theorem 3.5 the points of \(X \times Y\) are the pairs \((x,y)\). The open subset \(U_x \times U_y = \operatorname{Spec}(A_x \otimes_{\mathbb{F}_1} A_y)\) is affine, and every point of it is a generalization of \((x,y)\). So \((x,y)\) is its closed point and \(\mathcal{O}_{(x,y)} = A_x \otimes_{\mathbb{F}_1} A_y\). An element \(a \otimes b\) of this monoid is a unit if and only if \(a\) and \(b\) are units. So \(\mathcal{O}_{(x,y)}^\times = \mathcal{O}_x^\times \times \mathcal{O}_y^\times\) and \(r(x,y) = r(x) + r(y)\). Hence \(P_{X \times Y}(t) = \sum_{x,y} t^{r(x) + r(y)} = P_X(t)P_Y(t)\). \(\square\)

So under products the zeros of the zeta function are added. For example \(\zeta_{\mathbb{P}^1 \times \mathbb{P}^1}(s) = s(s-1)^2(s-2)\).

*Reference:* [Soulé 2004, 6.3.4] writes the zeta function of a product as \(\zeta_X(s) \times \zeta_{X'}(s)\). For the product of functions this fails for \(\mathbb{A}^1 \times \mathbb{A}^1\), where \(s - 2 \neq (s-1)^2\). The formula that holds is Proposition 7.6(2).

**Remark 7.7 (where the shape comes from, and two variants).**

1. [Manin 1995, Section 1.6] introduces an absolute Tate motive \(\mathbb{T}\) with zeta function \((s-1)/2\pi\) (formula (1.29)) and zeta functions \((s-n)/2\pi\) for its powers (formula (1.30), stated there for \(n \leq 0\)). It describes \(\mathbb{T}\) as the motive of an affine line over an absolute point \(\operatorname{Spec}\mathbb{F}_1\), whose zeta function is \(s/2\pi\). Up to the factors \(2\pi\) these are the functions \(s - 1\) and \(s\) of Examples 7.5. [Soulé 2004, Section 6] obtains them from point counts by the limit of Lemma 7.1. The two conventions of Remark 7.3 are both present in [Manin 1995, Section 1.1]: over \(\mathbb{F}_q\) the function \((1 - q^{-s})(1 - q^{1-s})\) is called there the zeta function of the motive \(\mathbb{L}^0 \oplus \mathbb{L}^1\), with \(\mathbb{L}\) the Tate motive, and the inverse zeta function of the projective line. The convention of this lesson is the one for motives, and that of [Connes–Consani 2010] is the one for varieties.
2. [Deitmar–Koyama–Kurokawa 2008] defines two further zeta functions of a monoid scheme \(X\) of finite type from the numbers \(\# X(\mathbb{F}_{1^m})\) for all \(m \geq 1\): the absolute Weil zeta function \(\exp(\sum_{m \geq 1} \# X(\mathbb{F}_{1^m})T^m/m)\) (Section 2) and the function \(\sum_{m \geq 1} \# X(\mathbb{F}_{1^m})m^{-s}\) of Igusa type (Section 3). By Theorem 4.4 both are determined by the groups \(\mathcal{O}_{X,x}^\times\), and unlike \(\zeta_X\) they depend on the torsion. If all unit groups are torsion-free, the second is \(\sum_x \zeta(s - r(x))\), with \(\zeta\) the Riemann zeta function: for \(\mathbb{A}^1\) it is \(\zeta(s) + \zeta(s-1)\) and for \(\mathbb{P}^1\) it is \(2\zeta(s) + \zeta(s-1)\) [Deitmar–Koyama–Kurokawa 2008, Proposition 3.3]. For \(\operatorname{Spec}\mathbb{F}_{1^2}\) it is \(\sum_m \gcd(2,m)m^{-s} = (1 + 2^{-s})\zeta(s)\), which differs from the value \(\zeta(s)\) for a point.
3. The varieties over \(\mathbb{F}_1\) of [Soulé 2004] have points with values in the rings \(\mathbb{Z}[T]/(T^n - 1)\), whose roots of unity are the \(2n\) elements \(\pm T^i\). The hypothesis of [Soulé 2004, Section 6] is therefore that the number of these points is \(N(2n+1)\). For a monoid scheme with torsion-free unit groups the number of \(\mathbb{F}_{1^n}\)-points is \(N(n+1)\), by Theorem 4.7. See *Varieties over the field with one element after Soulé and Connes–Consani*.

## 8. Sheaves of modules

### Modules over a monoid

**Definition 8.1.** Let \(A\) be a monoid. An *\(A\)-module* is a set \(M\) with a base point \(\ast\) and a map \(A \times M \to M\), \((a, m) \mapsto am\), such that \(1m = m\), \((ab)m = a(bm)\), \(0m = \ast\) and \(a\ast = \ast\). A morphism of \(A\)-modules is a map \(f\) with \(f(am) = af(m)\); then \(f(\ast) = \ast\).

These objects are the \(A\)-sets of [Chu–Lorscheid–Santhanam 2012, Section 2.2] and the pointed modules of [Deitmar 2008]. [Deitmar 2005, Section 4] uses sets without a base point. Without a base point there is no zero object, and kernels and cokernels are not defined.

The constructions of linear algebra that do not use addition carry over.

- The zero module is \(0 = \{\ast\}\). Between any two modules there is the zero morphism.
- For a submodule \(M' \subseteq M\) the quotient \(M/M'\) is obtained by identifying \(M'\) to one point. The *kernel* of \(f\colon M \to N\) is \(f^{-1}(\ast)\), and the *cokernel* is \(N/f(M)\).
- The product \(M \times N\) has the componentwise action. The coproduct is the wedge sum \(M \vee N\), the disjoint union with the two base points identified.
- The free module on a set \(I\) is \(A^{\vee I} = \bigvee_{i \in I} Ae_i\). It has rank \(|I|\), and \(\operatorname{Hom}(A^{\vee I}, N) = N^I\).
- The tensor product \(M \otimes_A N\) is the quotient of \(M \times N\) by the equivalence relation generated by \((am, n) \sim (m, an)\). Taking \(a = 0\) shows that all pairs with a base point are identified.
- For a multiplicative subset \(S \subseteq A\) the localization \(S^{-1}M\) is the set of fractions \(m/s\), with \(m/s = m'/s'\) if \(tms' = tm's\) for some \(t \in S\). It is an \(S^{-1}A\)-module. We write \(M_f\) and \(M_{\mathfrak{p}}\).
- For a ring \(k\), let \(k[M]\) be the free \(k\)-module on \(M \setminus \{\ast\}\). It is a \(k[A]\)-module, and \(\operatorname{Hom}_{k[A]}(k[M], V) = \operatorname{Hom}_A(M, V)\) for every \(k[A]\)-module \(V\), regarded as an \(A\)-module with base point \(0\). Also \(k[S^{-1}M] = S^{-1}k[M]\).

### Modules over the structure sheaf

**Definition 8.2.** Let \(X\) be a monoid scheme. An *\(\mathcal{O}_X\)-module* is a sheaf \(\mathcal{F}\) of pointed sets on \(X\) with the structure of an \(\mathcal{O}_X(U)\)-module on \(\mathcal{F}(U)\) for every open \(U\), such that the restriction maps are compatible with the actions. Morphisms are morphisms of sheaves that are compatible with the actions. The stalk \(\mathcal{F}_x\) is an \(\mathcal{O}_{X,x}\)-module.

For an \(A\)-module \(M\) let \(\widetilde{M}\) be the \(\mathcal{O}\)-module on \(\operatorname{Spec} A\) with \(\widetilde{M}(D(f)) = M_f\). This is a sheaf on the basis \(\{D(f)\}\) without any verification, because every cover of \(D(f)\) contains \(D(f)\) (Lemma 1.1). Its stalk at \(\mathfrak{p}\) is \(M_{\mathfrak{p}}\) and its module of global sections is \(M\).

An \(\mathcal{O}_X\)-module \(\mathcal{F}\) is *quasi-coherent* if every point has an affine open neighbourhood \(U\) with \(\mathcal{F}|_U \cong \widetilde{M}\) for some \(\mathcal{O}_X(U)\)-module \(M\). It is *locally free of rank \(r\)* if \(M\) can be taken free of rank \(r\), and *invertible* if it is locally free of rank \(1\).

*Reference:* [Deitmar 2005, Section 4]; [Chu–Lorscheid–Santhanam 2012, Sections 3.2 and 3.3].

**Proposition 8.3.**

1. Let \(X\) be a monoid scheme. An \(\mathcal{O}_X\)-module \(\mathcal{F}\) is quasi-coherent if and only if \(\mathcal{F}|_U \cong \widetilde{\mathcal{F}(U)}\) for every affine open subset \(U\).
2. For \(X = \operatorname{Spec} A\), the functors \(M \mapsto \widetilde{M}\) and \(\mathcal{F} \mapsto \mathcal{F}(X)\) are mutually inverse equivalences between the category of \(A\)-modules and the category of quasi-coherent \(\mathcal{O}_X\)-modules.

*Proof.* (1) Let \(\mathcal{F}\) be quasi-coherent and \(U\) a nonempty affine open subset with closed point \(c\). There is an affine open neighbourhood \(V = \operatorname{Spec} B\) of \(c\) with \(\mathcal{F}|_V \cong \widetilde{N}\). The set \(U \cap V\) is an open neighbourhood of \(c\) in \(U\), so \(U \subseteq V\) by Lemma 1.1. By Proposition 2.3, \(U = D(s)\) for some \(s \in B\). Then \(\mathcal{F}|_U\) is the module attached to \(N_s = \mathcal{F}(U)\), because \(\widetilde{N}(D(st)) = N_{st} = (N_s)_t\). (2) A morphism \(g\colon \widetilde{M} \to \widetilde{N}\) is determined by \(g(X)\colon M \to N\): the map \(g(D(f))\colon M_f \to N_f\) is a morphism of \(A_f\)-modules compatible with \(g(X)\), so it is the localization of \(g(X)\). So \(M \mapsto \widetilde{M}\) is fully faithful. By (1) with \(U = X\), every quasi-coherent module is \(\widetilde{\mathcal{F}(X)}\). \(\square\)

So far nothing has changed, except that the proofs are shorter. For rings, the analogue of (1) needs a glueing argument over a cover by principal open sets; here it follows from Lemma 1.1.

### What changes compared with rings

**Theorem 8.4.** Let \(A\) be a nonzero monoid and \(k\) a nonzero ring.

1. *There is no addition.* For \(A\)-modules \(M\) and \(N\) the canonical map \(M \vee N \to M \times N\) is injective, and it is bijective only if \(M = 0\) or \(N = 0\). So finite coproducts and finite products of \(A\)-modules differ, and the category of \(A\)-modules is not additive.
2. *Kernels do not detect injectivity.* For a morphism \(f\colon M \to N\) the following are equivalent: (a) the map \(M/\ker f \to f(M)\) is bijective; (b) \(f\) is injective on \(M \setminus \ker f\); (c) the inclusion \(k[\ker f] \subseteq \ker(k[f])\) is an equality. A morphism with these properties is called *normal*. Injective morphisms are normal, and a surjective morphism is a cokernel if and only if it is normal. The fold map \(\nabla\colon A \vee A \to A\), which is the identity on both summands, is surjective with kernel \(0\), but it is not injective and not normal.
3. *Base change is not exact.* The functor \(M \mapsto k[M]\) sends injective morphisms to injective maps and surjective morphisms to surjective maps, and it commutes with cokernels. It commutes with the kernel of \(f\) if and only if \(f\) is normal.
4. *Affine monoid schemes are local.* Let \(X = \operatorname{Spec} A\) with closed point \(c\). For every sheaf \(\mathcal{F}\) on \(X\) the map \(\mathcal{F}(X) \to \mathcal{F}_c\) is bijective. Hence every locally free \(\mathcal{O}_X\)-module of rank \(r\) is isomorphic to the free module \(\widetilde{A^{\vee r}}\). And for every sheaf of abelian groups \(\mathcal{F}\) on \(X\), the cohomology groups \(H^i(X, \mathcal{F})\) vanish for \(i > 0\).

*Proof.* (1) The map sends \(m\) to \((m, \ast)\) and \(n\) to \((\ast, n)\). Its image is the set of pairs with a base point as a coordinate. In an additive category finite products and coproducts agree.

(2) The map in (a) is surjective. It is injective if and only if \(f\) does not identify two different elements outside the kernel. So (a) and (b) are equivalent. The set \(M \setminus \{\ast\}\) is a basis of \(k[M]\), and \(k[f]\) sends \(m \notin \ker f\) to the basis element \(f(m)\) and \(m \in \ker f\) to \(0\). If (b) holds, the elements \(f(m)\), \(m \notin \ker f\), are different basis elements, so \(\ker k[f] = k[\ker f]\). If \(f(m) = f(m')\) for two different elements outside the kernel, then \(m - m'\) lies in \(\ker k[f]\) and not in \(k[\ker f]\). So (b) and (c) are equivalent. If \(f\) is surjective and normal, then \(N = M/\ker f\) is the cokernel of \(\ker f \subseteq M\); conversely a quotient map \(N' \to N'/N''\) satisfies (b). For the fold map, \(\nabla(e_1) = \nabla(e_2) = 1 \neq \ast\).

(3) An injective morphism maps the basis \(M \setminus \{\ast\}\) injectively to the basis of \(k[N]\). The image of \(k[f]\) is the span of \(f(M) \setminus \{\ast\}\), and \(k[N/f(M)]\) is the quotient of \(k[N]\) by this span. The statement on kernels is (2)(c).

(4) The first statement is Lemma 1.1(3). Let \(\mathcal{F}\) be locally free of rank \(r\). The point \(c\) has an affine open neighbourhood \(U\) with \(\mathcal{F}|_U\) free, and \(U = X\) by Lemma 1.1. The functor of global sections on sheaves of abelian groups is the stalk functor at \(c\), which is exact. So its higher derived functors vanish. \(\square\)

*Reference:* (2) and (3) are in [Chu–Lorscheid–Santhanam 2012, Sections 2.2.2 and 2.2.4]; the statement on locally free modules in (4) is [Deitmar 2005, Proposition 4.2].

For rings, (4) fails in both parts. A locally free module on an affine scheme need not be free; a non-principal ideal of a Dedekind domain is an example. And the cohomology of an affine scheme vanishes for quasi-coherent sheaves, but not for all sheaves of abelian groups. For example, let \(Y\) be the affine line over a field, \(p \neq q\) two closed points, and \(\mathcal{G}\) the subsheaf of the constant sheaf \(\mathbb{Z}\) of the sections that vanish at \(p\) and \(q\). The quotient \(\mathbb{Z}/\mathcal{G}\) has global sections \(\mathbb{Z}^2\), and \(\mathbb{Z} = H^0(Y, \mathbb{Z}) \to \mathbb{Z}^2\) is not surjective, so \(H^1(Y, \mathcal{G}) \neq 0\).

**Proposition 8.5.** Let \(X\) be a connected integral monoid scheme and \(\mathcal{F}\) a locally free \(\mathcal{O}_X\)-module of rank \(r\). Then there are invertible submodules \(\mathcal{L}_1, \dots, \mathcal{L}_r\) of \(\mathcal{F}\) such that \(\mathcal{F}(U) = \mathcal{L}_1(U) \vee \dots \vee \mathcal{L}_r(U)\) for every nonempty open \(U\). They are unique up to order.

*Proof.* The stalk \(\mathcal{F}_\eta\) is a free module of rank \(r\) over \(\mathcal{O}_{X,\eta} = G_0\). So the group \(G\) acts freely on \(\mathcal{F}_\eta \setminus \{\ast\}\), with \(r\) orbits. Let \(E\) be the set of orbits. For a nonempty open \(U\) the map \(\mathcal{F}(U) \to \mathcal{F}_\eta\) is injective: \(U\) is covered by affine open subsets \(V = \operatorname{Spec} A\) on which \(\mathcal{F}\) is free, and \(\mathcal{F}(V) = A^{\vee r} \to G_0^{\vee r}\) is injective because \(A \subseteq G_0\). For \(e \in E\) let \(\mathcal{L}_e(U)\) be the set of sections in \(\mathcal{F}(U)\) whose germ at \(\eta\) lies in \(e \cup \{\ast\}\). This is a submodule, and \(\mathcal{L}_e\) is a subsheaf of \(\mathcal{F}\), because the germ at \(\eta\) can be computed on any nonempty open subset. Every section lies in \(\mathcal{L}_e(U)\) for the orbit \(e\) of its germ, so \(\mathcal{F}(U) = \bigvee_e \mathcal{L}_e(U)\). On an affine open \(V = \operatorname{Spec} A\) with a basis \(e_1, \dots, e_r\) of \(\mathcal{F}(V)\), the germs of the \(e_i\) form a basis of \(\mathcal{F}_\eta\). So they lie in \(r\) different orbits \(\epsilon_1, \dots, \epsilon_r\), and \(\mathcal{L}_{\epsilon_i}|_V\) is the module attached to \(Ae_i \cong A\). Hence the \(\mathcal{L}_e\) are invertible. If \(\mathcal{F} = \mathcal{L}'_1 \vee \dots \vee \mathcal{L}'_r\) is another such decomposition, the nonzero germs of \(\mathcal{L}'_j\) at \(\eta\) form one orbit \(e_j\). So \(\mathcal{L}'_j \subseteq \mathcal{L}_{e_j}\), and equality follows because both families decompose every \(\mathcal{F}(U)\). \(\square\)

*Reference:* [Chu–Lorscheid–Santhanam 2012, Section 5.4.3].

So on a connected integral monoid scheme the locally free modules are the wedge sums of invertible modules. After base change to a ring they become direct sums of invertible modules.

**Example 8.6 (integrality is needed).** Let \(A = \mathbb{F}_1[s,t]/(st)\), the monoid with elements \(0\), \(1\), \(s^i\), \(t^j\) (\(i, j \geq 1\)) and \(s^it^j = 0\). It has three prime ideals: \(sA\), \(tA\) and \(\mathfrak{m} = sA \cup tA\). The open subset \(V = D(s) \cup D(t)\) consists of the two points \(tA\) and \(sA\), and it is the disjoint union of \(D(s) = \operatorname{Spec}\mathbb{F}_1[s, s^{-1}]\) and \(D(t) = \operatorname{Spec}\mathbb{F}_1[t, t^{-1}]\). Let \(X\) be obtained by glueing two copies \(U_1, U_2\) of \(\operatorname{Spec} A\) along \(V\) by the identity. It is a connected monoid scheme of finite type with four points, and it is not integral. Let \(\mathcal{F}\) be obtained by glueing the free modules \(\mathcal{O}_{U_1}e_1 \vee \mathcal{O}_{U_1}e_2\) and \(\mathcal{O}_{U_2}e'_1 \vee \mathcal{O}_{U_2}e'_2\) along \(V\) by the isomorphism that sends \(e_1, e_2\) to \(e'_1, e'_2\) on \(D(s)\) and to \(e'_2, e'_1\) on \(D(t)\) [Stacks, Tag [00AK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-glueing-sheaves)]. Then \(\mathcal{F}\) is locally free of rank \(2\).

It is not a wedge sum of two invertible modules. Suppose that \(\mathcal{L}\) and \(\mathcal{L}'\) are invertible submodules of \(\mathcal{F}\) with \(\mathcal{F}(U) = \mathcal{L}(U) \vee \mathcal{L}'(U)\) for every affine open \(U\). By Theorem 8.4(4), \(\mathcal{L}(U_1)\) and \(\mathcal{L}'(U_1)\) are free of rank one, with generators \(\ell\) and \(\ell'\), and \(Ae_1 \vee Ae_2 = A\ell \vee A\ell'\). Say \(e_1 \in A\ell\), so \(e_1 = a\ell\). If \(\ell = be_2\), then \(e_1 = abe_2\), which is impossible. So \(\ell = be_1\) and \(ab = 1\). Hence \(\mathcal{L}(U_1) = Ae_1\) or \(Ae_2\); say \(Ae_1\). In the same way \(\mathcal{L}(U_2) = Ae'_i\) for \(i = 1\) or \(2\). On \(D(s)\) the glueing gives \(i = 1\), and on \(D(t)\) it gives \(i = 2\). This is a contradiction.

*Reference:* [Flores–Lorscheid–Szczesny 2017, Remark 5.7] states that every locally free sheaf on a monoidal scheme is a wedge of line bundles. This holds for connected integral schemes (Proposition 8.5) and fails for \(X\).

**Example 8.7 (invertible modules on \(\mathbb{P}^1\)).** Write \(\mathbb{P}^1 = U_0 \cup U_1\) with \(U_0 = \operatorname{Spec}\mathbb{F}_1[t]\) and \(U_1 = \operatorname{Spec}\mathbb{F}_1[t^{-1}]\). For \(d \in \mathbb{Z}\) let \(\mathcal{O}(d)\) be the module obtained by glueing \(\mathcal{O}_{U_0}e_0\) and \(\mathcal{O}_{U_1}e_1\) along \(U_0 \cap U_1\) by \(e_0 = t^{-d}e_1\).

Every invertible module \(\mathcal{L}\) on \(\mathbb{P}^1\) is isomorphic to \(\mathcal{O}(d)\) for exactly one \(d\). Indeed, by Theorem 8.4(4) the restrictions of \(\mathcal{L}\) to \(U_0\) and \(U_1\) are free. Their generators \(e_0\) and \(e_1\) are unique, because \(\mathbb{F}_1[t]\) and \(\mathbb{F}_1[t^{-1}]\) have no units other than \(1\). On \(U_0 \cap U_1 = \operatorname{Spec}\mathbb{F}_1[t,t^{-1}]\) both generate a free module of rank one, so \(e_0 = ue_1\) for a unit \(u = t^{-d}\). *Reference:* [Deitmar 2005, Proposition 4.3].

A nonzero global section of \(\mathcal{O}(d)\) is a pair \((t^ie_0, t^je_1)\) with \(i \geq 0\), \(j \leq 0\) and \(t^it^{-d} = t^j\). So there are \(d + 1\) nonzero global sections \(t^ie_0\), \(0 \leq i \leq d\), if \(d \geq 0\), and none if \(d < 0\). This is the dimension of the space of global sections of \(\mathcal{O}(d)\) on the projective line over a field [Stacks, Tag [01XT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-cohomology-projective-space-over-ring)]. Exercise 7 treats \(\mathbb{P}^n\).

**Remark 8.8 (cohomology).** For \(\mathcal{O}_X\)-modules, which are sheaves of pointed sets, there is no cohomology theory with the usual properties. [Deitmar 2008, Section 6] gives an example, attributed there to Gabber, on the three-point space of \(\mathbb{P}^1\): for a suitable sheaf of abelian groups, the exchange of the two closed points acts on the first cohomology group by \(-1\); if the sheaves and their cohomology came from sheaves of sets through free abelian groups, this action would be induced by a self-map of a set \(S\), but the inversion of \(\mathbb Z[S]\) is not induced by a self-map of \(S\). [Flores–Lorscheid–Szczesny 2017, Appendix A] shows that a cohomology defined by injective resolutions of pointed modules gives an infinite set for the first cohomology of \(\mathcal{O}\) on \(\mathbb{P}^1\). [Flores–Lorscheid–Szczesny 2017] defines Čech cohomology over \(\mathbb{F}_{1^2}=\{0,1,-1\}\) with the relation \(1+(-1)\equiv0\): a Čech cochain of degree \(q\) is a family of sections over the intersections of \(q+1\) members of the cover, it is a cocycle if the alternating sum of its restrictions is \(\equiv0\), that is, zero after additive completion, and the comparison map sends its class to the class of the same family in the Čech complex of the associated scheme \(X^+\) over \(\mathbb Z\). Its Theorem A states that for a locally free sheaf \(\mathcal F\) the Čech cohomology of \(X^+\) is the additive completion of that of \(X\), \(H^q(X,\mathcal F)^+=H^q(X^+,\mathcal F^+)\), if \(X\) has a finite affine cover by monoid blueprints with injective restriction maps; connected integral monoid schemes of finite type have such covers. Example 8.9 shows that this comparison fails in degree \(2\) already for the structure sheaf of such a scheme. The proof in that work uses, in degree zero, that the stalk of the sheaf at the generic point is generated by global sections ([Flores–Lorscheid–Szczesny 2017, Lemma 5.4]), which fails for \(\mathcal{O}(-1)\) on \(\mathbb{P}^1\): its only global section is \(0\), while its stalk at the generic point is free of rank one. In higher degrees it uses that additive completion commutes with the intersection of the cochains with the cocycles of the complex over \(\mathbb Z\); Example 8.9 shows that it does not.

**Example 8.9 (the comparison fails in degree two).** Let \(K\) be the simplicial complex on \(\{1,\dots,6\}\) whose maximal faces are the nine triples
\[
124,\ 135,\ 146,\ 156,\ 236,\ 245,\ 256,\ 345,\ 346 .
\]
Every pair is a face of \(K\), and no four-element set is. Take nine variables \(x_F\), one for each triple \(F\) above. For \(i\in\{1,\dots,6\}\) let \(f_i\) be the product of the \(x_F\) with \(i\notin F\), and let \(X_0=U_1\cup\dots\cup U_6\subseteq\operatorname{Spec}\mathbb F_1[x_F]\) with \(U_i=D(f_i)\). For a set \(J\) of indices, \(U_J=D(\prod_{i\in J}f_i)\), and \(\mathcal O_{X_0}(U_J)\) is the monoid of the monomials in which the variables \(x_F\) with \(F\not\supseteq J\) may have negative exponents. All these monoids lie in the group of Laurent monomials, so \(X_0\) is a connected integral monoid scheme of finite type, and its restriction maps are injective. Let \(X\) be \(X_0\) with \(-1\) adjoined: the same space, with \(\mathcal O_X(U)\) consisting of \(0\) and the signed elements \(\pm s\), \(s\in\mathcal O_{X_0}(U)\setminus\{0\}\), and the relation \(1+(-1)\equiv0\). Its additive completion \(X^+\) is the open subscheme \(\bigcup_iD(f_i)\) of \(\operatorname{Spec}\mathbb Z[x_F]\). The cover \(\mathcal U=(U_i)\) has the injective restriction maps required in Theorem A.

Let \(m=\prod_Fx_F^{-1}\). It lies in \(\mathcal O_X(U_J)\) exactly when every \(x_F\) is inverted on \(U_J\), that is, when \(J\) is not contained in any \(F\), that is, when \(J\notin K\); the same holds in the ring \(\mathcal O_{X^+}(U_J^+)\), whose monomials form a basis. The Čech complexes are graded by monomials, and their parts in degree \(m\) are as follows. In cochain degrees \(0\) and \(1\) they are \(0\), since all singletons and pairs lie in \(K\). In cochain degree \(2\) the coordinates are the eleven triples outside \(K\),
\[
123,\ 125,\ 126,\ 134,\ 136,\ 145,\ 234,\ 235,\ 246,\ 356,\ 456,
\]
with coefficients \(a,b,c,d,e,f,g,h,i,j,k\) in this order, and in cochain degree \(3\) they are all fifteen four-element sets. The coboundary \((dc)_L=\sum_{k=0}^3(-1)^kc_{L\setminus\{l_k\}}\), for \(L=\{l_0<l_1<l_2<l_3\}\), gives the fifteen equations
\[
\begin{gathered}
-a-d+g=0,\quad -a+b+h=0,\quad -a+c-e=0,\quad b-f=0,\quad c+i=0,\\
-b+c=0,\quad -d-f=0,\quad -d+e=0,\quad e+j=0,\quad -f+k=0,\\
-g+h=0,\quad -g-i=0,\quad -h+j=0,\quad i+k=0,\quad -j+k=0,
\end{gathered}
\]
for the sets \(1234,1235,\dots,3456\) in lexicographic order, where a coefficient on a triple of \(K\) is \(0\). They force \(c=f=b\), \(d=e=i=-b\), \(g=h=j=k=b\) and \(a=2b\), and these values satisfy all fifteen. So the cocycles over \(\mathbb Z\) in this degree are the multiples of
\[
v=(2,1,1,-1,-1,1,1,1,-1,1,1),
\]
and there are no coboundaries, because cochain degree \(1\) is \(0\). Hence the class of \(mv\) is a nonzero element of \(H^2(X^+,\mathcal O_{X^+};\mathcal U^+)\), which is \(H^2(X^+,\mathcal O_{X^+})\) because all intersections \(U_J^+\) are affine [Stacks, Tag [01XD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-cech-cohomology-quasi-coherent)].

On the other hand, a cochain over \(\mathbb F_{1^2}\) has in each coordinate \(0\) or a signed monomial, so its part in degree \(m\) has entries in \(\{0,1,-1\}\). If it is a cocycle, this part is a cocycle in degree \(m\), hence equal to \(tv\) with \(t\in\mathbb Z\), and its first entry \(2t\in\{0,1,-1\}\) forces \(t=0\). So the classes from \(X\), and their sums, have no component in degree \(m\), and the class of \(mv\) is not in the image of \(H^2(X,\mathcal O_X;\mathcal U)^+\). Finally, \(\mathcal U\) refines every open cover of \(X\): a member of the cover that contains the closed point of the affine set \(U_i\) contains \(U_i\), by Lemma 1.1(2). Hence \(H^2(X,\mathcal O_X)^+\to H^2(X^+,\mathcal O_{X^+})\) is not surjective.

## 9. Exercises

**Exercise 1 (two crossing lines).** Let \(A = \mathbb{F}_1[s,t]/(st)\) be the monoid of Example 8.6 and \(X = \operatorname{Spec} A\). Determine the topology and the stalks of \(X\). Show that \(X\) is connected but has no point that lies in every nonempty open set. Compute \(\# X(\mathbb{F}_{1^n})\), \(N_X(q)\) and \(\zeta_X\), and check the count on \(X_{\mathbb{Z}}\).

*Solution.* The monoid is generated by \(s\) and \(t\), so a prime ideal is generated by a subset of \(\{s,t\}\) (proof of Proposition 2.6). The ideal \(\{0\}\) is not prime because \(st = 0\). The ideal \(sA = \{0, s, s^2, \dots\}\) is prime: its complement \(\{1, t, t^2, \dots\}\) is closed under products. In the same way \(tA\) and \(\mathfrak{m} = sA \cup tA\) are prime. The open sets are \(\emptyset\), \(D(s) = \{tA\}\), \(D(t) = \{sA\}\), their union, and \(X\). The stalks are \(A_{tA} = A_s = \mathbb{F}_1[s,s^{-1}]\), because \(t = ts \cdot s^{-1} = 0\) in \(A_s\); \(A_{sA} = \mathbb{F}_1[t, t^{-1}]\); and \(A_{\mathfrak{m}} = A\). The space is connected, because it is affine (Lemma 1.1). The open sets \(D(s)\) and \(D(t)\) are disjoint, so no point lies in every nonempty open set. The unit groups have ranks \(1\), \(1\), \(0\) and no torsion. So \(\# X(\mathbb{F}_{1^n}) = 2n + 1\), \(N_X(q) = 2(q-1) + 1 = 2q - 1\), \(P_X(t-1) = 2t - 1\) and \(\zeta_X(s) = (s-1)^2/s\). Check: a morphism \(A \to \mathbb{F}_{1^n}\) is a pair of elements of \(\mathbb{F}_{1^n}\) with product \(0\), and there are \(2(n+1) - 1\) such pairs. And \(X_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[s,t]/(st)\) is the union of two lines that meet in one point, with \(2q - 1\) points over \(\mathbb{F}_q\).

**Exercise 2 (extensions by roots).** Let \(B \subseteq A\) be a submonoid containing \(0\), such that every \(a \in A\) has a power \(a^n\), \(n \geq 1\), in \(B\). Show that \(\mathfrak{p} \mapsto \mathfrak{p} \cap B\) is a homeomorphism \(\operatorname{Spec} A \to \operatorname{Spec} B\). Deduce that \(\operatorname{Spec}\mathbb{F}_1[t^2, t^3]\) has two points.

*Solution.* The map is continuous, as the map of spaces of \(\operatorname{Spec}(B \to A)\). *Injective:* let \(\mathfrak{p} \cap B = \mathfrak{q} \cap B\) and \(a \in \mathfrak{p}\). Some power \(a^n\) lies in \(B \cap \mathfrak{p} \subseteq \mathfrak{q}\), so \(a \in \mathfrak{q}\). By symmetry \(\mathfrak{p} = \mathfrak{q}\). *Surjective:* let \(\mathfrak{p}_B\) be a prime ideal of \(B\), and let \(\mathfrak{p}\) be the set of \(a \in A\) such that \(a^n \in \mathfrak{p}_B\) for some \(n \geq 1\). It contains \(0\) and not \(1\). If \(a \in \mathfrak{p}\) with \(a^n \in \mathfrak{p}_B\), and \(c \in A\) with \(c^m \in B\), then \((ac)^{nm} = (a^n)^m(c^m)^n \in \mathfrak{p}_B\). So \(\mathfrak{p}\) is an ideal. If \(ab \in \mathfrak{p}\), say \((ab)^n \in \mathfrak{p}_B\), and \(a^m, b^l \in B\), then \((a^m)^{nl}(b^l)^{nm} = (ab)^{nml} \in \mathfrak{p}_B\), so \(a^m \in \mathfrak{p}_B\) or \(b^l \in \mathfrak{p}_B\). So \(\mathfrak{p}\) is prime. Clearly \(\mathfrak{p} \cap B = \mathfrak{p}_B\), because \(\mathfrak{p}_B\) is prime. *Open:* if \(a^n \in B\), the image of \(D(a)\) is \(D(a^n)\), because \(a \notin \mathfrak{p}\) if and only if \(a^n \notin \mathfrak{p} \cap B\). For \(B = \mathbb{F}_1[t^2,t^3] \subseteq A = \mathbb{F}_1[t]\) every element of \(A\) has its square in \(B\), and \(\operatorname{Spec} A\) has the two points \(\{0\}\) and \(tA\).

*Reference:* [Deitmar 2008, Lemma 4.2] proves the bijection when one exponent \(n\) works for all \(a\); the same proof works in general. For the normalization of a monoid the statement is [Cortiñas–Haesemeyer–Walker–Weibel 2015, Remark 1.6.1]. The statement of this exercise is also proved as a theorem in *Commutative monoids and their spectra*.

**Exercise 3 (a fibre product with torsion).** Let \(f\colon \mathbb{A}^1 \to \mathbb{A}^1\) be the morphism given by \(t \mapsto t^2\), and \(X = \mathbb{A}^1 \times_{\mathbb{A}^1} \mathbb{A}^1\) the fibre product of \(f\) with itself. Describe the monoid of \(X\) and its points. Show that \(X\) is integral and that \(G_X \cong \mathbb{Z} \times \mathbb{Z}/2\). Compute \(\# X(\mathbb{F}_{1^n})\) and \(N_X(q)\), and compare with \(X_{\mathbb{Z}}\).

*Solution.* By Theorem 3.5, \(X = \operatorname{Spec} B\) with \(B = \mathbb{F}_1[x] \otimes_{\mathbb{F}_1[t]} \mathbb{F}_1[y]\), where \(t\) maps to \(x^2\) and to \(y^2\). By the universal property, \(B\) is the monoid with zero generated by \(x\) and \(y\) with the one relation \(x^2 = y^2\). Every nonzero element is \(x^iy^\epsilon\) with \(i \geq 0\) and \(\epsilon \in \{0,1\}\). The morphism \(B \setminus \{0\} \to \mathbb{Z} \times \mathbb{Z}/2\) with \(x \mapsto (1,0)\) and \(y \mapsto (1,1)\) sends \(x^iy^\epsilon\) to \((i + \epsilon, \epsilon)\), so it is injective. Hence these elements are different, \(B\) is integral, and its group is generated by \(x\) and \(u = y/x\) with \(u^2 = 1\). So \(G_X \cong \mathbb{Z} \times \mathbb{Z}/2\). A prime ideal is generated by a subset of \(\{x, y\}\). The ideal \(xB\) is not prime, because \(y^2 = x^2 \in xB\) and \(y \notin xB\); in the same way \(yB\) is not prime. So the points are \(\{0\}\) and \(\mathfrak{m} = xB \cup yB\). This agrees with Theorem 3.5(2): \(f\) maps the generic point to the generic point and the closed point to the closed point, so the fibre product of the spaces has two points. The unit groups are \(\mathbb{Z} \times \mathbb{Z}/2\) and \(1\). By Theorem 4.4,
\[
\# X(\mathbb{F}_{1^n}) = n\gcd(2, n) + 1, \qquad N_X(q) = (q-1)\gcd(2, q-1) + 1 .
\]
So \(N_X(q) = 2q - 1\) for odd \(q\) and \(N_X(q) = q\) for even \(q\). By Proposition 4.2(3), \(X_{\mathbb{Z}} = \operatorname{Spec}\mathbb{Z}[x,y]/(x^2 - y^2)\). Over a field of odd characteristic this is the union of the lines \(x = y\) and \(x = -y\), with \(2q - 1\) points. In characteristic \(2\) it is the double line \((x-y)^2 = 0\), with \(q\) points. Here \(e_X = 2\), \(P_X(t-1) = t\) and \(\zeta_X(s) = s - 1\).

**Exercise 4 (the punctured plane).** Let \(\Delta\) be the fan in \(\mathbb{Z}^2\) with the cones \(\{0\}\), \(\rho_1 = \mathbb{R}_{\geq 0}e_1\) and \(\rho_2 = \mathbb{R}_{\geq 0}e_2\). Show that \(X(\Delta)\) is isomorphic to the open subscheme \(U = D(t_1) \cup D(t_2)\) of \(\mathbb{A}^2\). Show that \(U\) is not affine, that \(\mathcal{O}(U) = \mathbb{F}_1[t_1, t_2]\), and compute \(\zeta_U\).

*Solution.* The dual cones give \(S_{\rho_1} = \{t_1^at_2^b : a \geq 0\}\), \(S_{\rho_2} = \{t_1^at_2^b : b \geq 0\}\) and \(S_{\{0\}} = \{t_1^at_2^b\}\). The open subscheme \(U\) of \(\mathbb{A}^2\) is connected and integral, it is covered by \(D(t_2) = \operatorname{Spec}\mathbb{F}_1[t_1, t_2^{\pm 1}]\) and \(D(t_1) = \operatorname{Spec}\mathbb{F}_1[t_1^{\pm 1}, t_2]\), and their intersection is \(D(t_1t_2) = \operatorname{Spec}\mathbb{F}_1[t_1^{\pm 1}, t_2^{\pm 1}]\). So \(U\), with the cover by \(D(t_2)\), \(D(t_1)\) and \(D(t_1t_2)\), has the properties of Lemma 3.8 for the family of the three monoids, and \(U \cong X(\Delta)\) by Lemma 3.8(3). The points of \(U\) are \(\{0\}\), \(t_1A\) and \(t_2A\), where \(A = \mathbb{F}_1[t_1,t_2]\). The last two are closed in \(U\), because the only other point in their closure in \(\mathbb{A}^2\) is the maximal ideal. So \(U\) has two closed points and is not affine (Proposition 2.6). By Proposition 2.8(3), \(\mathcal{O}(U) \setminus \{0\}\) is the intersection of the three monoids, which is \(\{t_1^at_2^b : a, b \geq 0\}\). The unit groups have ranks \(2\), \(1\), \(1\). So \(P_U(t) = t^2 + 2t\), \(P_U(t-1) = t^2 - 1\) and \(\zeta_U(s) = (s-2)/s\). Indeed the punctured plane has \(q^2 - 1\) points over \(\mathbb{F}_q\).

**Exercise 5 (a functional equation).** Let \(X\) be of finite type with \(P_X(t-1) = N(t) = \sum_{j=0}^d a_jt^j\), and assume \(t^dN(1/t) = N(t)\). Show that \(\zeta_X(d - s) = (-1)^{N(1)}\zeta_X(s)\). Check this for \(\mathbb{P}^n\) and for \(\mathbb{P}^1 \times \mathbb{P}^1\), with \(d\) the degree of \(N\). Show that for \(\mathbb{A}^n\), \(n \geq 1\), the assumption fails when \(d\) is the degree of \(N\), and that \(\zeta(n - s)\) is not \(\pm\zeta(s)\).

*Solution.* The assumption says \(a_{d-j} = a_j\). So
\[
\zeta_X(d-s) = \prod_j (d - s - j)^{a_j} = \prod_j (-1)^{a_j}(s - (d-j))^{a_j} = (-1)^{N(1)}\prod_i (s-i)^{a_{d-i}} = (-1)^{N(1)}\zeta_X(s).
\]
For \(\mathbb{P}^n\): \(N(t) = 1 + \dots + t^n\), \(d = n\), \(N(1) = n+1\), and indeed \((n-s)(n-s-1)\cdots(-s) = (-1)^{n+1}s(s-1)\cdots(s-n)\). For \(\mathbb{P}^1 \times \mathbb{P}^1\): \(N(t) = (t+1)^2\), \(d = 2\), \(N(1) = 4\), and \(\zeta(2-s) = (2-s)(1-s)^2(-s) = \zeta(s)\). For \(\mathbb{A}^n\): \(N(t) = t^n\) has degree \(n\), and \(t^nN(1/t) = 1 \neq N(t)\). Here \(\zeta(s) = s - n\) and \(\zeta(n-s) = -s\), which is not \(\pm\zeta(s)\). The assumption does hold for \(d = 2n\), with \(a_n = 1\) and all other \(a_j = 0\), and it gives \(\zeta(2n - s) = -\zeta(s)\). This is the symmetry of a linear function about its zero. It is not a symmetry about the point \(s = n/2\), which is the centre for a projective space of the same dimension.

**Exercise 6 (automorphisms of projective space).** Show that the automorphism group of the monoid scheme \(\mathbb{P}^n\) is isomorphic to the symmetric group \(S_{n+1}\).

*Solution.* For \(n = 0\) both groups are trivial. Let \(n \geq 1\). We use the notation of Section 5. Let \(h\) be an automorphism of \(\mathbb{P}^n\). It fixes \(\eta\), and its map of stalks at \(\eta\) restricts to an automorphism \(\theta\) of \(G_n\). The maps of stalks commute with the generization maps, so \(\theta(S_{h(x)}) = S_x\) for all \(x\). Since \(x \mapsto S_x\) is injective, \(h\) is determined by \(\theta\). The closed points are permuted by \(h\): there is a permutation \(\sigma\) with \(h(x_{\{i\}}) = x_{\{\sigma(i)\}}\), and \(\theta(S_{\{\sigma(i)\}}) = S_{\{i\}}\). The monoid \(S_{\{i\}}\) is free on the elements \(T_l/T_i\), \(l \neq i\). These are its irreducible elements, so \(\theta\) maps the generators of \(S_{\{\sigma(i)\}}\) bijectively to those of \(S_{\{i\}}\): there is a bijection \(\pi_i\) with \(\theta(T_j/T_{\sigma(i)}) = T_{\pi_i(j)}/T_i\) for \(j \neq \sigma(i)\). Fix such a \(j\) and put \(i' = \sigma^{-1}(j) \neq i\). Then \(T_{\sigma(i)}/T_j = T_{\sigma(i)}/T_{\sigma(i')}\) is a generator of \(S_{\{\sigma(i')\}}\), so \(\theta\) maps it to an element of the form \(T_l/T_{i'}\). On the other hand it is the inverse of \(T_j/T_{\sigma(i)}\), so \(\theta\) maps it to \(T_i/T_{\pi_i(j)}\). Hence \(\pi_i(j) = i' = \sigma^{-1}(j)\). So \(\theta(T_a/T_b) = T_{\sigma^{-1}(a)}/T_{\sigma^{-1}(b)}\) for all \(a \neq b\): the automorphism \(\theta\) is induced by a permutation of the variables.

Conversely let \(\tau\) be a permutation of \(\{0, \dots, n\}\) and \(\theta_\tau\) the automorphism of \(G_n\) that replaces \(T_a\) by \(T_{\tau(a)}\). It maps \(S_I\) onto \(S_{\tau(I)}\), so it permutes the family \((S_I)\). By Proposition 3.9(3) it is induced by an automorphism of \(\mathbb{P}^n\). Different permutations give different \(\theta_\tau\) because \(n \geq 1\). So \(h \mapsto \theta\) is a bijection from the automorphism group onto \(\{\theta_\tau\}\), and it reverses the order of composition. Hence the automorphism group is isomorphic to \(S_{n+1}\).

Over a field \(k\) the group \(\mathrm{PGL}_{n+1}(k)\) acts on \(\mathbb{P}^n_k\). The symmetric group \(S_{n+1}\) found here is the group that takes its place at \(q = 1\); compare *Counting over finite fields and the limit q → 1*.

**Exercise 7 (invertible modules on projective space).** Let \(n \geq 1\) and \(d \in \mathbb{Z}\). Let \(\mathcal{O}(d)\) be the \(\mathcal{O}\)-module on \(\mathbb{P}^n\) obtained by glueing the free modules \(\mathcal{O}_{U_i}e_i\) on the charts along \(U_i \cap U_j\) by \(e_i = (T_i/T_j)^de_j\). Show that every invertible module on \(\mathbb{P}^n\) is isomorphic to \(\mathcal{O}(d)\) for exactly one \(d\), and that \(\mathcal{O}(d)\) has \(\binom{n+d}{n}\) nonzero global sections if \(d \geq 0\) and none if \(d < 0\).

*Solution.* The glueing is allowed, because \((T_i/T_j)^d(T_j/T_l)^d = (T_i/T_l)^d\) [Stacks, Tag [00AK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-glueing-sheaves)]. Let \(\mathcal{L}\) be invertible. By Theorem 8.4(4), \(\mathcal{L}|_{U_i}\) is free with a generator \(e_i\), which is unique because \(A_{\{i\}}\) has no units other than \(1\). On the affine open \(U_i \cap U_j\) both \(e_i\) and \(e_j\) generate the free module \(\mathcal{L}(U_i \cap U_j)\). So \(e_i = u_{ij}e_j\) with a unit \(u_{ij}\) of \(A_{\{i,j\}}\). By Proposition 5.2(3) these units are the powers of \(T_i/T_j\), so \(u_{ij} = (T_i/T_j)^{d_{ij}}\), and \(d_{ji} = d_{ij}\). For three different indices, comparing \(e_i = u_{ij}u_{jl}e_l\) and \(e_i = u_{il}e_l\) on \(U_i \cap U_j \cap U_l\) gives \((T_i/T_j)^{d_{ij}}(T_j/T_l)^{d_{jl}} = (T_i/T_l)^{d_{il}}\) in \(G_n\). The exponents of \(T_i\) and \(T_j\) give \(d_{ij} = d_{il}\) and \(d_{ij} = d_{jl}\). So all \(d_{ij}\) are equal to one integer \(d\), and \(\mathcal{L} \cong \mathcal{O}(d)\). The integer \(d\) is determined by \(\mathcal{L}\) because the generators \(e_i\) are unique.

A global section of \(\mathcal{O}(d)\) is a family \((a_ie_i)\) with \(a_i \in A_{\{i\}}\) and \(a_i(T_i/T_j)^d = a_j\). If one \(a_i\) is \(0\), all are. Otherwise \(a_i = T^{b(i)}\) with \(b(i) \in \mathbb{Z}^{n+1}\) of sum \(0\) and \(b(i)_l \geq 0\) for \(l \neq i\), and \(b(j) = b(i) + d\varepsilon_i - d\varepsilon_j\), where \(\varepsilon_i\) is the \(i\)-th basis vector. So \(c = b(i) + d\varepsilon_i\) does not depend on \(i\). It has sum \(d\), and \(c_l = b(i)_l \geq 0\) for any \(i \neq l\). Conversely every \(c \in \mathbb{Z}_{\geq 0}^{n+1}\) with sum \(d\) gives the section with \(a_i = T^{c - d\varepsilon_i}\). So the nonzero sections correspond to the monomials of degree \(d\) in \(T_0, \dots, T_n\). Their number is \(\binom{n+d}{n}\) for \(d \geq 0\) and \(0\) for \(d < 0\). This is the dimension of the space of global sections of \(\mathcal{O}(d)\) on \(\mathbb{P}^n_k\) [Stacks, Tag [01XT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-cohomology-projective-space-over-ring)].

## 10. What this lesson does not prove

- **Glueing** (Proposition 2.9). The proof is the one of [Stacks, Tag [01JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-glue)] and [Stacks, Tag [00AK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-glueing-sheaves)], which the lesson does not repeat.
- **Separatedness in general.** That Definition 3.6 agrees with the definition by the diagonal for monoid schemes of finite type is [Cortiñas–Haesemeyer–Walker–Weibel 2015, Corollary 3.7]. [Cortiñas–Haesemeyer–Walker–Weibel 2015, Proposition 5.13] states that \(X\) is separated, in the sense of the diagonal, if \(X_k\) is separated, for every monoid scheme \(X\). This needs an additional hypothesis. Let \(A=\{0,1,e,f\}\) with \(e^2=e\), \(f^2=f\) and \(ef=0\). The points of \(\operatorname{Spec}A\) are \(\{0,e\}\), \(\{0,f\}\) and \(\{0,e,f\}\); the open set \(V=D(e)\cup D(f)\) is the disjoint union of two copies of \(\operatorname{Spec}\mathbb{F}_1\), and it is not affine, since it has two closed points. Glue two copies of \(\operatorname{Spec}A\) along \(V\) by the identity. The resulting monoid scheme \(X\) is of finite type and not separated: the intersection of its two affine charts is \(V\). For every nonzero ring \(k\), \(k[A]\cong k^3\), through the idempotents \(e\), \(f\) and \(1-e-f\); so \(V_k\) is the union of two of the three components of \(\operatorname{Spec}k^3\), and \(X_k\) is the disjoint union of four copies of \(\operatorname{Spec}k\), which is separated. The example is not integral. The lesson proves the converse of Proposition 4.2(5) only for connected integral torsion-free monoid schemes of finite type (Proposition 6.6).
- **Cohomology.** The statements quoted in Remark 8.8: [Deitmar 2008, Section 6]; [Flores–Lorscheid–Szczesny 2017, Appendix A]. Example 8.9 shows that [Flores–Lorscheid–Szczesny 2017, Theorem A] does not hold as stated.
- **Facts about schemes and rings.** They are cited from [Stacks]: morphisms to affine schemes (Tag 01I1), representable functors (Tag 01JJ), separated morphisms (Tag 01KP), finite type (Tag 01T2), projective space (Tag 01ND) and the sections of \(\mathcal{O}(d)\) (Tag 01XT), varieties and normal schemes (Tags 020D, 033I), normal domains (Tags 00GY, 00H1, 030B), Serre's criterion and the intersection of the localizations at primes of height one (Tags 031S, 031T), the regular locus of a variety (Tag 0B8X), factoriality of regular local rings (Tag 0AG0), integral closure (Tag 00GO), Noetherian rings (Tag 00FN), the Nullstellensatz (Tag 00FV), sheaves on a basis (Tag 009H), and, in Section 6.6, the dimension of a finitely generated domain over a field (Tag 00P0), the dimension of a space as a supremum of local dimensions (Tag 0B7I) and the structure of finitely generated abelian groups (Tag 0ASV).
- **Illustrations.** Three facts are used only in illustrations and are not proved: a non-principal ideal of a Dedekind domain is a locally free module that is not free (after Theorem 8.4); a proper curve over a field is not affine; and the rational curve with one node is not normal at the node (Examples 6.9).

## References

- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 009H, 00AK, 01I1, 01JJ, 031S and 031T carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Soulé 2004] C. Soulé, *Les variétés sur le corps à un élément*, Mosc. Math. J. 4 (2004), no. 1, 217–244, 312. [arXiv:math/0304444](https://arxiv.org/pdf/math/0304444).
- [Deitmar 2005] A. Deitmar, *Schemes over \(\mathbb{F}_1\)*, in: Number fields and function fields — two parallel worlds, Progr. Math. 239, Birkhäuser, 2005, 87–100. [arXiv:math/0404185](https://arxiv.org/pdf/math/0404185).
- [Deitmar 2006] A. Deitmar, *Remarks on zeta functions and K-theory over \(\mathbb{F}_1\)*, Proc. Japan Acad. Ser. A Math. Sci. 82 (2006), no. 8, 141–146. [arXiv:math/0605429](https://arxiv.org/pdf/math/0605429).
- [Deitmar 2008] A. Deitmar, *\(\mathbb{F}_1\)-schemes and toric varieties*, Beiträge Algebra Geom. 49 (2008), no. 2, 517–525. [arXiv:math/0608179](https://arxiv.org/pdf/math/0608179).
- [Connes–Consani 2010] A. Connes, C. Consani, *Schemes over \(\mathbb{F}_1\) and zeta functions*, Compos. Math. 146 (2010), no. 6, 1383–1415. arXiv:0903.2024. Theorem and section numbers are those of the arXiv version. Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Chu–Lorscheid–Santhanam 2012] C. Chu, O. Lorscheid, R. Santhanam, *Sheaves and K-theory for \(\mathbb{F}_1\)-schemes*, Adv. Math. 229 (2012), no. 4, 2239–2286. [arXiv:1010.2896](https://arxiv.org/pdf/1010.2896). Section numbers are those of the arXiv version.
- [Cortiñas–Haesemeyer–Walker–Weibel 2015] G. Cortiñas, C. Haesemeyer, M. Walker, C. Weibel, *Toric varieties, monoid schemes and cdh descent*, [arXiv:1106.1389](https://arxiv.org/pdf/1106.1389). Numbers are those of the arXiv version.
- [Flores–Lorscheid–Szczesny 2017] J. Flores, O. Lorscheid, M. Szczesny, *Čech cohomology over \(\mathbb{F}_{1^2}\)*, [arXiv:1511.06875](https://arxiv.org/pdf/1511.06875).
- [Telen 2022] S. Telen, *Introduction to toric geometry*, lecture notes, [arXiv:2203.01690](https://arxiv.org/pdf/2203.01690).
- [Jarra 2023a] M. Jarra, *Strong congruence spaces and dimension in \(\mathbb{F}_1\)-geometry*, arXiv:2305.15953,
  version 3 (15 January 2024). Free at https://arxiv.org/abs/2305.15953
- [Brasselet 2001] J.-P. Brasselet, *Introduction to toric varieties*, notes of a course at the 23rd Colóquio Brasileiro de Matemática (Rio de Janeiro, 2001), Publicações Matemáticas, IMPA, Rio de Janeiro. Free at https://impa.br/wp-content/uploads/2017/04/PM_15.pdf (IMPA, 2008 edition)
- [Deitmar–Koyama–Kurokawa 2008] A. Deitmar, S. Koyama, N. Kurokawa, *Absolute zeta functions*, Proc. Japan Acad. Ser. A Math. Sci. 84 (2008), 138–142. Free at https://doi.org/10.3792/pjaa.84.138
- [Manin 1995] Yu. Manin, *Lectures on zeta functions and motives (according to Deninger and Kurokawa)*, Astérisque 228 (1995), 121–163. Free at https://www.numdam.org/item/AST_1995__228__121_0/
- [Brion 2017] M. Brion, *Algebraic group actions on normal varieties*, arXiv:1703.09506, version 3 (20 April 2017). Free at https://arxiv.org/abs/1703.09506
- [Sumihiro 1974] H. Sumihiro, *Equivariant completion*, J. Math. Kyoto Univ. 14 (1974), 1–28. Free at https://projecteuclid.org/journals/journal-of-mathematics-of-kyoto-university/volume-14/issue-1/Equivariant-completion/10.1215/kjm/1250523277.pdf
