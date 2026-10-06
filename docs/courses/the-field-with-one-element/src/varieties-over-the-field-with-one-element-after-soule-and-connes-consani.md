# Varieties over the field with one element after Soulé and Connes–Consani

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Proposition 5.6, Example 5.7 and Theorem 5.8 were drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

## Introduction

A variety over the field with one element should have an extension of scalars to the integers, and this extension
should be an ordinary variety over \(\mathbb Z\). Soulé turned this expectation into a definition. A variety over
\(\mathbb F_1\) is described by the data one expects to know about it: its points with values in the finite extensions
\(\mathbb F_{1^n}\), whose non-zero elements are roots of unity, and an algebra of complex functions that can be
evaluated at these points. The definition requires that these data single out one variety over \(\mathbb Z\) by a
universal property. The data are now called a *gadget*. Connes and Consani took finite abelian groups as test
objects, added a grading that makes the points of lowest degree agree with the count of Tits, and proved that
Chevalley groups give varieties over the quadratic extension \(\mathbb F_{1^2}\).

This lesson develops the definition and tests it. Its main tool is the *ring of integral functions* of a gadget
(Section 3). A universal morphism to the gadget of an affine variety exists exactly when this ring is finitely
generated, and the variety is then its spectrum; the gadget is an affine variety when, moreover, it is finite and this
morphism is an immersion. Every example then becomes the computation of one ring. The lesson proves the following.

1. A gadget has a universal morphism to the gadget of an affine variety if and only if its ring of integral
   functions is finitely generated. It is an affine variety if and only if, moreover, it is finite and this morphism
   is an immersion. The extension of scalars is then flat over \(\mathbb Z\), and the points of the gadget are dense
   in it (Theorem 3.3 and Corollary 3.4).
2. Every finitely generated cancellative monoid gives an affine variety over \(\mathbb F_1\). This covers tori,
   affine spaces and the spectra \(\operatorname{Spec}\mathbb F_{1^n}\) (Theorem 4.4). Projective space is covered by
   such varieties (Proposition 4.13).
3. The definition bounds the set of points from below only. The same functor of points can belong to the torus and to
   the affine line, and \(\operatorname{Spec}\mathbb Z[i]\) is a variety over \(\mathbb F_{1^2}\) and not over
   \(\mathbb F_1\) (Examples 4.8, 4.11 and 7.6).
4. If the number of points over \(\mathbb F_{1^n}\) is \(N(n+1)\) for a polynomial \(N\), the zeta function of the
   variety is a rational function with integer zeros and poles, given by a limit \(q\to1\) (Theorem 6.2).
5. The theorem of [Connes–Consani 2011a] that Chevalley groups are varieties over \(\mathbb F_{1^2}\) follows from
   five quoted facts about Chevalley group schemes. For \(\mathrm{SL}_2\) all five are checked by hand, so the theorem
   is proved completely in this case (Section 8).
6. For a monoid scheme of finite type the number of points over \(\mathbb F_{1^n}\) is a polynomial in \(n\) exactly
   when the groups of units of its stalks are torsion-free (Theorem 9.3). This is the counting theorem of
   [Connes–Consani 2010] with its converse.

**What is assumed.** Schemes and their functors of points [Stacks, Tag [01J5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-points)], morphisms into affine schemes
[Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)], and the characters of finite abelian groups. Sections 4 and 9 use monoids and monoid schemes as
in *Commutative monoids and their spectra* and *Monoid schemes*; each definition taken from there is restated.
Section 5 uses Fourier series of continuous functions on the circle. Section 8 uses facts about Chevalley group
schemes; they are quoted, and all of them are checked for \(\mathrm{SL}_2\). The lesson *Counting over finite fields
and the limit q → 1* explains the counts that the definitions are meant to reproduce; it is not used in the proofs.

Basic references are [Soulé 2004], [Connes–Consani 2011a] and [Connes–Consani 2010].

**Conventions.** Rings are commutative with \(1\). For a ring \(k\), a *variety over \(k\)* is a scheme of finite
type over \(\operatorname{Spec}k\) [Stacks, Tag [01T1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-finite-type)]; for \(k=\mathbb Z\) this is the convention of
[Soulé 2004, §3.3]. If \(V\) is a scheme over \(k\) and \(A\) is a \(k\)-algebra, \(V(A)\) is the set of morphisms
\(\operatorname{Spec}A\to V\) over \(k\). For \(V=\operatorname{Spec}O\) it is the set
\(\operatorname{Hom}_k(O,A)\) of homomorphisms of \(k\)-algebras. An abelian group \(A\) is *torsion-free* if
\(na=0\) with \(n\ge1\) implies \(a=0\). We write \(A_{\mathbb C}=A\otimes_{\mathbb Z}\mathbb C\). A torsion-free
abelian group is flat over \(\mathbb Z\) [Stacks, Tag [0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dedekind-torsion-free-flat)], so the map \(A\to A_{\mathbb C}\),
\(a\mapsto a\otimes1\), is then injective, and we regard \(A\) as a subgroup of \(A_{\mathbb C}\).

## 1. Test rings and characters

A variety over \(\mathbb F_1\) will be tested on a small class of rings. This section describes these rings.

### Group rings of finite abelian groups

Let \(D\) be a finite abelian group, written multiplicatively. The group ring \(\mathbb Z[D]\) is the free
\(\mathbb Z\)-module with basis \(D\), with the multiplication of \(D\) extended bilinearly, and
\(\mathbb C[D]=\mathbb Z[D]_{\mathbb C}\). A *character* of \(D\) is a homomorphism \(\chi:D\to\mathbb C^\times\).
The characters form a group \(\widehat D\). A character extends linearly to ring homomorphisms
\(\mathbb Z[D]\to\mathbb C\) and \(\mathbb C[D]\to\mathbb C\), which we also call \(\chi\). We use three standard
facts, which follow from the decomposition of \(D\) into cyclic groups: \(\widehat D\) has \(|D|\) elements; for
\(g\neq1\) in \(D\) there is a character with \(\chi(g)\neq1\); every character of a subgroup \(H\) of \(D\) extends
to \(D\). For the third fact, note that the restriction map \(\widehat D\to\widehat H\) has the kernel
\(\widehat{D/H}\), of order \(|D|/|H|\), so its image has \(|H|\) elements.

**Lemma 1.1.** Let \(D\) be a finite abelian group.

(a) For \(g\in D\), the sum \(\sum_{\chi\in\widehat D}\chi(g)\) is \(|D|\) if \(g=1\) and \(0\) otherwise.

(b) The map \(\mathbb C[D]\to\mathbb C^{\widehat D}\), \(f\mapsto(\chi(f))_\chi\), is an isomorphism of
\(\mathbb C\)-algebras. If \(f=\sum_{g\in D}b_g\,g\), then
\[
b_h=\frac1{|D|}\sum_{\chi\in\widehat D}\chi(f)\,\chi(h)^{-1}\qquad\text{for every }h\in D. \tag{1.1}
\]

(c) Every ring homomorphism \(\mathbb Z[D]\to\mathbb C\) is a character.

*Proof.* (a) For \(g=1\) every term is \(1\). For \(g\neq1\) choose \(\chi_0\) with \(\chi_0(g)\neq1\).
Multiplication by \(\chi_0\) permutes \(\widehat D\), so the sum \(\Sigma\) satisfies \(\Sigma=\chi_0(g)\Sigma\), and
\(\Sigma=0\). (b) The map is a homomorphism of algebras, because each \(\chi\) is one. By (a),
\(\sum_\chi\chi(f)\chi(h)^{-1}=\sum_gb_g\sum_\chi\chi(gh^{-1})=|D|\,b_h\). This is (1.1), and it shows that the map
is injective. Both sides have dimension \(|D|\), so the map is bijective. (c) Such a homomorphism restricts to a
homomorphism \(D\to\mathbb C^\times\), and it is determined by this restriction. \(\square\)

So \(\mathbb C[D]\) is a product of \(|D|\) copies of \(\mathbb C\), one for each character. In particular it is a
reduced ring, and an element of \(\mathbb C[D]\) is known when its values under all characters are known.

For \(n\ge1\) let \(\mu_n\) be the group of \(n\)-th roots of unity and \(R_n=\mathbb Z[T]/(T^n-1)\). A generator
of \(\mu_n\) gives an isomorphism \(\mathbb Z[\mu_n]\cong R_n\). For an abelian group \(D\) we write
\(D_0=D\sqcup\{0\}\) for the monoid obtained by adding an absorbing element \(0\); [Connes–Consani 2010] writes
\(\mathbb F_1[D]\). Thus \(\mathbb F_{1^n}=(\mu_n)_0\) and \(\mathbb F_1=\{0,1\}\). The inclusion
\(D_0\subset\mathbb Z[D]\), which sends the zero of \(D_0\) to \(0\), is multiplicative.

### Reduced group rings

Let \(\epsilon\in D\) be an element of order \(2\). The *reduced group ring* is
\[
\mathbb Z[D,\epsilon]=\mathbb Z[D]/(1+\epsilon),
\]
the quotient in which \(\epsilon\) becomes \(-1\). We write \(\bar g\) for the image of \(g\in D\), and
\(\widehat D_-\) for the set of characters with \(\chi(\epsilon)=-1\).

**Lemma 1.2.** Let \(S\subset D\) be a set of representatives of the cosets of \(\{1,\epsilon\}\).

(a) \(\mathbb Z[D,\epsilon]\) is a free \(\mathbb Z\)-module with basis \(\{\bar g:g\in S\}\), and
\(\overline{\epsilon g}=-\bar g\).

(b) The map \(D\to\mathbb Z[D,\epsilon]\), \(g\mapsto\bar g\), is injective.

(c) The characters that factor through \(\mathbb Z[D,\epsilon]\) are those of \(\widehat D_-\), and
\(f\mapsto(\chi(f))_\chi\) is an isomorphism \(\mathbb Z[D,\epsilon]_{\mathbb C}\to\mathbb C^{\widehat D_-}\).

(d) For \(g\neq h\) in \(D\) there is a \(\chi\in\widehat D_-\) with \(\chi(g)\neq\chi(h)\).

*Proof.* (a) For \(f=\sum_{g\in S}(b_g\,g+c_g\,\epsilon g)\) we have
\((1+\epsilon)f=\sum_{g\in S}(b_g+c_g)(g+\epsilon g)\). So the ideal \((1+\epsilon)\) is the direct sum of the
groups \(\mathbb Z(g+\epsilon g)\), \(g\in S\), and \(\mathbb Z[D]\) is the direct sum of this ideal and of the
groups \(\mathbb Zg\), \(g\in S\). (b) Write \(g=\epsilon^as\) and \(h=\epsilon^bs'\) with \(s,s'\in S\) and
\(a,b\in\{0,1\}\). Then \(\bar g=(-1)^a\bar s\) and \(\bar h=(-1)^b\bar s'\). By (a) these are equal only if
\(s=s'\) and \(a=b\). (c) Under the isomorphism of Lemma 1.1(b), \(1+\epsilon\) becomes the family
\((1+\chi(\epsilon))_\chi\), whose entries are \(2\) or \(0\). The ideal it generates in \(\mathbb C^{\widehat D}\)
is the set of families that vanish on \(\widehat D_-\), and the quotient is \(\mathbb C^{\widehat D_-}\). (d) The
character \(\epsilon\mapsto-1\) of \(\{1,\epsilon\}\) extends to a character \(\chi_0\) of \(D\). Put
\(u=gh^{-1}\neq1\). If \(\chi_0(u)\neq1\) we are done. Otherwise \(u\neq\epsilon\), so the image of \(u\) in
\(D/\{1,\epsilon\}\) is not trivial, and there is a character \(\eta\) of \(D\) with \(\eta(\epsilon)=1\) and
\(\eta(u)\neq1\). Then \(\chi=\chi_0\eta\) lies in \(\widehat D_-\) and \(\chi(u)=\eta(u)\neq1\). \(\square\)

### Systems of test rings

Several choices of test rings appear in the works on which this lesson is based. We treat them together.

**Definition 1.3.** A *system of test rings* \(\beta=(k,\mathcal T,\beta)\) consists of a countable ring \(k\), a
category \(\mathcal T\), and a functor \(\beta\) from \(\mathcal T\) to the category of \(k\)-algebras, such that
every ring \(\beta(t)\) is torsion-free as an abelian group. The objects of \(\mathcal T\) are the *test objects*
and the rings \(\beta(t)\) are the *test rings*. We put \(k_{\mathbb C}=k\otimes_{\mathbb Z}\mathbb C\).

The lesson uses four systems.

- **\(\beta_1\), the test rings over \(\mathbb F_1\).** \(k=\mathbb Z\); \(\mathcal T\) is the category of finite
  abelian groups; \(\beta_1(D)=\mathbb Z[D]\). This is the choice of [Connes–Consani 2011a, §2.2] and of
  Soulé's lectures at Vanderbilt University in 2009, with notes by D. Penneys.
- **\(\beta_n\), the test rings over \(\mathbb F_{1^n}\)**, for \(n\ge1\). \(k=R_n\); the test objects are the
  pairs \((D,\epsilon)\) of a finite abelian group and an element \(\epsilon\in D\) of order exactly \(n\); a
  morphism \((D,\epsilon)\to(D',\epsilon')\) is a homomorphism that sends \(\epsilon\) to \(\epsilon'\);
  \(\beta_n(D,\epsilon)=\mathbb Z[D]\), which is an \(R_n\)-algebra by \(T\mapsto\epsilon\). This is the variant
  indicated in [Soulé 2004, §3.8.2] and [Connes–Consani 2011a, §2.4]. For \(n=1\) it is \(\beta_1\).
- **\(\beta_2^-\), the reduced test rings over \(\mathbb F_{1^2}\).** \(k=\mathbb Z\); the test objects are the
  pairs \((D,\epsilon)\) with \(\epsilon\) of order \(2\), as for \(\beta_2\);
  \(\beta_2^-(D,\epsilon)=\mathbb Z[D,\epsilon]\). This is the choice made for Chevalley groups in
  [Connes–Consani 2011a, §2.4].
- **\(\beta_S\), rings as test objects.** \(k=\mathbb Z\); \(\mathcal T\) is the category
  \(\mathcal R_{\mathrm{red}}\) of reduced rings whose additive group is free of finite rank; \(\beta_S\) is the
  identity. This is the choice of [Soulé 2004, §2.4], restricted to reduced rings; see Section 5.

The rings \(\mathbb Z[D]\) and \(\mathbb Z[D,\epsilon]\) are free abelian groups (Lemma 1.2), so the condition of
Definition 1.3 holds. On a first reading one may take \(\beta=\beta_1\) everywhere: the test objects are the finite
abelian groups \(D\), and the test rings are the group rings \(\mathbb Z[D]\).

## 2. Gadgets and affine varieties

Let \(\beta=(k,\mathcal T,\beta)\) be a system of test rings.

**Definition 2.1.** A *gadget over \(\beta\)* is a triple \(X=(X,\mathcal A_X,e_X)\) of

(a) a functor \(X\) from \(\mathcal T\) to sets; the elements of \(X(t)\) are the *points of \(X\) over \(t\)*;

(b) a \(k_{\mathbb C}\)-algebra \(\mathcal A_X\);

(c) for every test object \(t\) and every point \(x\in X(t)\), a homomorphism of \(k_{\mathbb C}\)-algebras
\(e_X(x):\mathcal A_X\to\beta(t)_{\mathbb C}\), the *evaluation at \(x\)*, such that
\(e_X(X(u)x)=\beta(u)_{\mathbb C}\circ e_X(x)\) for every morphism \(u:t\to t'\) of \(\mathcal T\).

We write \(f(x)=e_X(x)(f)\in\beta(t)_{\mathbb C}\) and call it the *value of \(f\) at \(x\)*. The gadget is *finite*
if every set \(X(t)\) is finite. A gadget over \(\beta_1\) is called a *gadget over \(\mathbb F_1\)*.

For a gadget over \(\mathbb F_1\), the value \(f(x)\) of a function at a point \(x\in X(D)\) lies in
\(\mathbb C[D]\). By Lemma 1.1 it is the same as the family of complex numbers \(\chi(f(x))\),
\(\chi\in\widehat D\). In the examples \(\mathcal A_X\) is an algebra of functions on a set of complex points, a
point \(x\) and a character \(\chi\) determine a complex point \(x_\chi\), and \(\chi(f(x))=f(x_\chi)\). One should
think of \(x\) as a point with coordinates in \(D_0\), and of \(x_\chi\) as the complex point obtained when the
elements of \(D\) are replaced by roots of unity through \(\chi\).

**Definition 2.2.** Let \(V=\operatorname{Spec}O\) be an affine variety over \(k\). Its gadget \(\mathcal G(V)\) has
the points \(\mathcal G(V)(t)=V(\beta(t))=\operatorname{Hom}_k(O,\beta(t))\), the algebra
\(O_{\mathbb C}=O\otimes_kk_{\mathbb C}\), and the evaluation \(f(y)=y_{\mathbb C}(f)\), where
\(y_{\mathbb C}:O_{\mathbb C}\to\beta(t)_{\mathbb C}\) is the \(\mathbb C\)-linear extension of \(y\).

**Definition 2.3.** A *morphism of gadgets* \(\varphi:X\to Y\) is a pair of a natural transformation
\((\varphi_t:X(t)\to Y(t))_t\) and a homomorphism of \(k_{\mathbb C}\)-algebras
\(\varphi^*:\mathcal A_Y\to\mathcal A_X\) such that
\[
(\varphi^*f)(x)=f(\varphi_t(x))\qquad\text{for all }t,\ x\in X(t),\ f\in\mathcal A_Y.
\]
Morphisms are composed componentwise. A morphism is an *immersion* if every \(\varphi_t\) is injective and
\(\varphi^*\) is injective.

A morphism \(f:V\to W\) of affine varieties over \(k\), given by \(g:O(W)\to O(V)\), induces the morphism
\(\mathcal G(f):\mathcal G(V)\to\mathcal G(W)\) with \(\mathcal G(f)_t(y)=y\circ g\) and
\(\mathcal G(f)^*=g_{\mathbb C}\).

**Definition 2.4.** An *affine variety over \(\beta\)* is a finite gadget \(X\) over \(\beta\) for which there exist
an affine variety \(X_k\) over \(k\) and an immersion \(i:X\to\mathcal G(X_k)\) with the following universal
property: for every affine variety \(V\) over \(k\) and every morphism of gadgets \(\varphi:X\to\mathcal G(V)\)
there is exactly one morphism \(\varphi_k:X_k\to V\) of schemes over \(k\) with
\(\varphi=\mathcal G(\varphi_k)\circ i\). The scheme \(X_k\) is the *extension of scalars* of \(X\).

An affine variety over \(\beta_1\) is an *affine variety over \(\mathbb F_1\)*, and its extension of scalars is
written \(X_{\mathbb Z}\) or \(X\otimes_{\mathbb F_1}\mathbb Z\). An affine variety over \(\beta_n\) is an *affine
variety over \(\mathbb F_{1^n}\)*; its extension of scalars is a variety over \(R_n\). An affine variety over
\(\beta_2^-\) is an *affine variety over \(\mathbb F_{1^2}\) in the reduced sense*; its extension of scalars is a
variety over \(\mathbb Z\).

As for every universal property, the pair \((X_k,i)\) is unique up to a unique isomorphism. Theorem 3.3 describes
it.

**Where the definition comes from.** The definition has appeared in several forms, and they should be kept apart.

- [Soulé 2004, Définitions 1–3] is the definition above for rings as test objects: the functor is defined on all
  rings whose additive group is free of finite rank, the algebra \(\mathcal A_X\) comes with evaluations
  \(e_{x,\sigma}:\mathcal A_X\to\mathbb C\) for the homomorphisms \(\sigma:R\to\mathbb C\), and the objects are
  called *trucs*. On reduced rings a truc is the same as a gadget over \(\beta_S\) (Section 5).
- [Connes–Consani–Marcolli 2009b, §3.1] restricts the functor to the group rings \(\mathbb Z[D]\), with all ring
  homomorphisms between them, and translates "truc" as "gadget".
- [Connes–Consani 2011a, Definitions 2.5–2.8] takes the finite abelian groups as test objects and replaces the
  algebra by a complex variety; see Remark 2.5.
- Soulé's 2009 Vanderbilt lectures give Definitions 2.1–2.4 for \(\beta_1\): finite abelian groups as test objects, a
  complex algebra, and immersions that are injective on points and on algebras. There the objects are called
  *affine gadgets over \(\mathbb F_1\)*. [López Peña–Lorscheid 2011a, §1.5.2] describes this version as the affine
  varieties of [Soulé 2004] with a functor on finite abelian groups \(D\) in place of finite flat rings \(R\), and with
  \(\mathbb C[D]\) and \(\mathbb Z[D]\) in place of \(R\otimes\mathbb C\) and \(R\); it calls these objects affine
  \(\mathrm S^{\ast}\)-varieties.

**Remark 2.5 (complex varieties instead of algebras).** In [Connes–Consani 2011a, Definition 2.5] a gadget over
\(\mathbb F_1\) is a triple \((X,X_{\mathbb C},e_X)\), where \(X\) is a functor on finite abelian groups,
\(X_{\mathbb C}\) is a variety over \(\mathbb C\), and \(e_X\) is a natural transformation from \(X\) to the functor
\(D\mapsto X_{\mathbb C}(\mathbb C[D])\). We call this a *geometric gadget*. It has an underlying gadget in the
sense of Definition 2.1: the algebra is \(\Gamma(X_{\mathbb C},\mathcal O_{X_{\mathbb C}})\), and the evaluation at
\(x\) is the pull-back of functions along \(e_X(x):\operatorname{Spec}\mathbb C[D]\to X_{\mathbb C}\). If
\(X_{\mathbb C}\) is affine, nothing is lost. A morphism of geometric gadgets has a morphism of complex varieties
\(\varphi_{\mathbb C}\) as its second component. [Connes–Consani 2011a, Definition 2.7] calls it an immersion if it
is injective on points and \(\varphi_{\mathbb C}\) is an embedding, and [Connes–Consani 2011a, Definition 2.8]
defines affine varieties over \(\mathbb F_1\) as in Definition 2.4 with this notion of immersion, for finite gadgets
that carry a grading (Section 7). The two notions of immersion ask different things of \(i^*\): injectivity here,
and surjectivity there when the embedding is closed. In all examples of [Connes–Consani 2011a], and in the examples
of Sections 4, 7 and 8 below, the algebra of \(X\) is \(O(X_k)_{\mathbb C}\) and \(i^*\) is the identity. Then both
conditions hold, and the two definitions give the same affine varieties.

## 3. The ring of integral functions

Let \(X\) be a gadget over a system of test rings \(\beta=(k,\mathcal T,\beta)\).

**Definition 3.1.** A function \(f\in\mathcal A_X\) is *integral* if \(f(x)\in\beta(t)\) for every test object
\(t\) and every point \(x\in X(t)\). The integral functions form the set \(\mathcal A_X^{\mathrm{int}}\).

Each evaluation is a homomorphism of \(k\)-algebras and \(\beta(t)\) is a \(k\)-subalgebra of
\(\beta(t)_{\mathbb C}\). So \(\mathcal A_X^{\mathrm{int}}\) is a \(k\)-subalgebra of \(\mathcal A_X\). For a gadget
over \(\mathbb F_1\), a function is integral if all its values \(f(x)\in\mathbb C[D]\) have integer coefficients.

**Theorem 3.2 (morphisms to the gadget of an affine variety).** Let \(V=\operatorname{Spec}O\) be an affine variety
over \(k\). For a morphism of gadgets \(\varphi:X\to\mathcal G(V)\) let \(\psi_\varphi:O\to\mathcal A_X\) be the
homomorphism of \(k\)-algebras \(h\mapsto\varphi^*(h\otimes1)\).

(a) \(\varphi\) is determined by \(\varphi^*\), and hence by \(\psi_\varphi\).

(b) \(\psi_\varphi(O)\subseteq\mathcal A_X^{\mathrm{int}}\), and \(\varphi\mapsto\psi_\varphi\) is a bijection from
the set of morphisms of gadgets \(X\to\mathcal G(V)\) onto \(\operatorname{Hom}_k(O,\mathcal A_X^{\mathrm{int}})\).

(c) If \(f:V\to V'=\operatorname{Spec}O'\) is a morphism of affine varieties over \(k\), given by
\(g:O'\to O\), then \(\psi_{\mathcal G(f)\circ\varphi}=\psi_\varphi\circ g\).

*Proof.* Since \(O_{\mathbb C}=O\otimes_kk_{\mathbb C}\), homomorphisms of \(k_{\mathbb C}\)-algebras
\(\varphi^*:O_{\mathbb C}\to\mathcal A_X\) correspond to homomorphisms of \(k\)-algebras
\(\psi:O\to\mathcal A_X\), by \(\psi(h)=\varphi^*(h\otimes1)\).

Let \(\varphi^*\) be given, with associated \(\psi\). Let \(x\in X(t)\) and
\(y\in\mathcal G(V)(t)=\operatorname{Hom}_k(O,\beta(t))\). The condition \((\varphi^*f)(x)=f(y)\) for all
\(f\in O_{\mathbb C}\) compares two homomorphisms of \(k_{\mathbb C}\)-algebras
\(O_{\mathbb C}\to\beta(t)_{\mathbb C}\). They agree if they agree on the elements \(h\otimes1\). So the condition
is equivalent to
\[
y(h)=\psi(h)(x)\quad\text{in }\beta(t)_{\mathbb C},\qquad\text{for all }h\in O. \tag{3.1}
\]
Since \(\beta(t)\subseteq\beta(t)_{\mathbb C}\), there is at most one such \(y\), and there is one if and only if
\(\psi(h)(x)\in\beta(t)\) for all \(h\in O\).

Hence, if \(\varphi\) is a morphism, then \(\varphi_t(x)\) is the \(y\) of (3.1). This proves (a) and the inclusion
\(\psi_\varphi(O)\subseteq\mathcal A_X^{\mathrm{int}}\). Conversely, let
\(\psi:O\to\mathcal A_X^{\mathrm{int}}\) be a homomorphism of \(k\)-algebras, let \(\varphi^*\) be its
\(k_{\mathbb C}\)-linear extension, and define \(\varphi_t(x)\) by (3.1). It is the composite of \(\psi\) with the
evaluation at \(x\), so it is a homomorphism of \(k\)-algebras \(O\to\beta(t)\). For a morphism \(u:t\to t'\) we
have \(f(X(u)x)=\beta(u)_{\mathbb C}(f(x))\), so \(\varphi_{t'}(X(u)x)=\beta(u)\circ\varphi_t(x)\). Thus the maps
\(\varphi_t\) are natural, and \(\varphi=(\varphi_t,\varphi^*)\) is a morphism of gadgets with
\(\psi_\varphi=\psi\). This proves (b). For (c), \((\mathcal G(f)\circ\varphi)^*=\varphi^*\circ g_{\mathbb C}\)
sends \(h'\otimes1\) to \(\varphi^*(g(h')\otimes1)\). \(\square\)

**Theorem 3.3 (the extension of scalars).**

(a) Suppose that \(\mathcal A_X^{\mathrm{int}}\) is a finitely generated \(k\)-algebra. Put
\(X^{\mathrm{int}}=\operatorname{Spec}\mathcal A_X^{\mathrm{int}}\), and let
\(i_X:X\to\mathcal G(X^{\mathrm{int}})\) be the morphism with \(\psi_{i_X}=\mathrm{id}\). Then
\((X^{\mathrm{int}},i_X)\) has the universal property of Definition 2.4.

(b) Let \(W=\operatorname{Spec}B\) be an affine variety over \(k\) and \(j:X\to\mathcal G(W)\) a morphism of
gadgets. The pair \((W,j)\) has the universal property of Definition 2.4 if and only if
\(\psi_j:B\to\mathcal A_X^{\mathrm{int}}\) is an isomorphism.

(c) \(X\) is an affine variety over \(\beta\) if and only if \(X\) is finite,
\(\mathcal A_X^{\mathrm{int}}\) is a finitely generated \(k\)-algebra, and \(i_X\) is an immersion. Its extension of
scalars is then \(\operatorname{Spec}\mathcal A_X^{\mathrm{int}}\).

Explicitly, \((i_X)_t\) sends a point \(x\in X(t)\) to the homomorphism \(f\mapsto f(x)\) from
\(\mathcal A_X^{\mathrm{int}}\) to \(\beta(t)\), and \(i_X^*\) is the map
\(\mathcal A_X^{\mathrm{int}}\otimes_kk_{\mathbb C}\to\mathcal A_X\), \(a\otimes c\mapsto ca\). So \(i_X\) is an
immersion if and only if distinct points of \(X(t)\) are separated by integral functions, for every \(t\), and the
map \(\mathcal A_X^{\mathrm{int}}\otimes_kk_{\mathbb C}\to\mathcal A_X\) is injective.

*Proof.* Let \((W,j)\) be as in (b) and let \(V=\operatorname{Spec}O\) be an affine variety over \(k\). Morphisms
\(f:W\to V\) over \(k\) correspond to homomorphisms \(g:O\to B\), and
\(\psi_{\mathcal G(f)\circ j}=\psi_j\circ g\) by Theorem 3.2(c). By Theorem 3.2(b), the universal property of
\((W,j)\) says that for every finitely generated \(k\)-algebra \(O\) the map
\[
\operatorname{Hom}_k(O,B)\longrightarrow\operatorname{Hom}_k(O,\mathcal A_X^{\mathrm{int}}),\qquad
g\mapsto\psi_j\circ g,
\]
is bijective. This holds if \(\psi_j\) is an isomorphism. Conversely, take \(O=k[T]\). A homomorphism from \(k[T]\)
is given by the image of \(T\), so for \(O=k[T]\) the displayed map is \(\psi_j\) itself, and \(\psi_j\) is
bijective. This proves (b), and (a) is the case \(B=\mathcal A_X^{\mathrm{int}}\), \(\psi_j=\mathrm{id}\). The
description of \(i_X\) is formula (3.1) for \(\psi=\mathrm{id}\). For (c), let \(X\) be an affine variety over
\(\beta\), with \((X_k,i)\). By (b), \(\psi_i\) is an isomorphism from \(O(X_k)\) onto
\(\mathcal A_X^{\mathrm{int}}\). So this ring is finitely generated, and \(\psi_i\) identifies \((X_k,i)\) with
\((X^{\mathrm{int}},i_X)\); hence \(i_X\) is an immersion. The converse is (a). \(\square\)

So the extension of scalars is not an extra datum. A pair with the universal property exists exactly when the ring
of integral functions is finitely generated, and then it is the spectrum of this ring; the gadget is an affine
variety, with this extension of scalars, exactly when moreover it is finite and \(i_X\) is an immersion. The last
condition is not automatic. Let \(X\) be the gadget over \(\beta_1\) with the two points \(a,b\) over every \(D\),
fixed by every \(X(u)\), with the algebra \(\mathbb C\) and the inclusion \(\mathbb C\to\mathbb C[D]\) as the
evaluation at both points. A function \(c\in\mathbb C\) is integral exactly when \(c\in\mathbb Z\), already by the
trivial group, so \(\mathcal A_X^{\mathrm{int}}=\mathbb Z\); but \(i_X\) sends \(a\) and \(b\) to the same point of
\(\mathcal G(\operatorname{Spec}\mathbb Z)\), so \(X\) is not an affine variety. The points of the gadget enter only
through the integrality conditions that they impose.

**Corollary 3.4.** Suppose that \(\mathcal A_X^{\mathrm{int}}\) is a finitely generated \(k\)-algebra; this holds if
\(X\) is an affine variety over \(\beta\). Put \(X^{\mathrm{int}}=\operatorname{Spec}\mathcal A_X^{\mathrm{int}}\).

(a) \(\mathcal A_X^{\mathrm{int}}\) is torsion-free. If \(k=\mathbb Z\), then \(X^{\mathrm{int}}\) is flat over
\(\mathbb Z\).

(b) If \(\mathcal A_X\) is reduced, then \(X^{\mathrm{int}}\) is reduced.

(c) If \(f\in\mathcal A_X\) satisfies \(f(x)=0\) for all test objects \(t\) and all \(x\in X(t)\), then \(f=0\).

(d) Let \(\beta=\beta_1\). If \(X^{\mathrm{int}}\) is not empty, then it has a point with values in \(\mathbb Z\).

*Proof.* (a) \(\mathcal A_X\) is a complex vector space, so it is torsion-free, and so is every subgroup. A
torsion-free \(\mathbb Z\)-module is flat [Stacks, Tag [0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dedekind-torsion-free-flat)]. (b) A subring of a reduced ring is reduced. (c) The
set \(I\) of these functions is a complex subspace of \(\mathcal A_X\), and \(I\subseteq\mathcal A_X^{\mathrm{int}}\)
because \(0\in\beta(t)\). A finitely generated algebra over the countable ring \(k\) is countable, and a non-zero
complex vector space is not. So \(I=0\). (d) We have \(\mathcal A_X^{\mathrm{int}}\neq0\), so
\(\mathcal A_X\neq0\). If all sets \(X(D)\) were empty, the condition of (c) would hold for every \(f\), and
\(\mathcal A_X\) would be \(0\). So there are a group \(D\) and a point \(x\in X(D)\). Then \((i_X)_D(x)\) is a ring
homomorphism \(\mathcal A_X^{\mathrm{int}}\to\mathbb Z[D]\). Its composite with the homomorphism
\(\mathbb Z[D]\to\mathbb Z\) that sends every \(g\in D\) to \(1\) is a point of \(X^{\mathrm{int}}\) with values in
\(\mathbb Z\). \(\square\)

Statement (c) says that the points of the gadget are dense: a function that vanishes at all of them is zero. For a
gadget over \(\mathbb F_1\) whose algebra consists of functions on a set of complex points, this means that no
non-zero function of \(\mathcal A_X\) vanishes at all the complex points \(x_\chi\).

Most gadgets of this lesson are of the following kind.

**Corollary 3.5 (algebraic sub-gadgets).** Let \(W=\operatorname{Spec}B\) be an affine variety over \(k\) with \(B\)
torsion-free. An *algebraic sub-gadget of \(\mathcal G(W)\)* is a gadget \(X\) with
\(X(t)\subseteq W(\beta(t))=\operatorname{Hom}_k(B,\beta(t))\) for all \(t\), compatibly with the morphisms of
\(\mathcal T\), with the algebra \(\mathcal A_X=B_{\mathbb C}\), and with the evaluation
\(f(x)=x_{\mathbb C}(f)\). For such an \(X\),
\[
\mathcal A_X^{\mathrm{int}}=\{f\in B_{\mathbb C}:x_{\mathbb C}(f)\in\beta(t)\text{ for all }t\text{ and all }
x\in X(t)\}\ \supseteq\ B .
\]
If \(X\) is finite, the following are equivalent:

(i) \(X\) is an affine variety over \(\beta\) with extension of scalars \(W\) and with the inclusion
\(X\to\mathcal G(W)\) as immersion;

(ii) \(\mathcal A_X^{\mathrm{int}}=B\): a function \(f\in B_{\mathbb C}\) whose values at all points of \(X\) lie in
the test rings belongs to \(B\).

*Proof.* The inclusion \(j:X\to\mathcal G(W)\) is an immersion: the maps \(j_t\) are inclusions and
\(j^*=\mathrm{id}\). The homomorphism \(\psi_j\) is the inclusion \(B\subseteq B_{\mathbb C}\), and its image lies
in \(\mathcal A_X^{\mathrm{int}}\) because \(x_{\mathbb C}(b)=x(b)\in\beta(t)\) for \(b\in B\). By Theorem 3.3(b),
\((W,j)\) has the universal property if and only if \(B=\mathcal A_X^{\mathrm{int}}\). \(\square\)

**Corollary 3.6 (more points do no harm).** Let \(X\subseteq X'\) be finite algebraic sub-gadgets of
\(\mathcal G(W)\), that is, \(X(t)\subseteq X'(t)\) for all \(t\). If \(X\) satisfies the conditions of
Corollary 3.5, so does \(X'\).

*Proof.* \(B\subseteq\mathcal A_{X'}^{\mathrm{int}}\subseteq\mathcal A_X^{\mathrm{int}}=B\). \(\square\)

*Reference:* [Soulé 2004, Proposition 4] is the corresponding statement for the objects over \(\mathbb F_1\) of
that work (Section 5.3).

So the universal property asks for enough points, and it puts no upper bound on the sets \(X(t)\) other than
finiteness. [Connes–Consani 2011a, §5] makes this remark and proposes a stronger notion; see Sections 4.3 and 9.

**Proposition 3.7 (functoriality).** Let \(\varphi:X\to Y\) be a morphism of gadgets over \(\beta\).

(a) \(\varphi^*\) maps \(\mathcal A_Y^{\mathrm{int}}\) into \(\mathcal A_X^{\mathrm{int}}\).

(b) If \(X\) and \(Y\) are affine varieties over \(\beta\), there is exactly one morphism
\(\varphi_k:X_k\to Y_k\) with \(i_Y\circ\varphi=\mathcal G(\varphi_k)\circ i_X\). This makes \(X\mapsto X_k\) a
functor from affine varieties over \(\beta\) to affine varieties over \(k\), and the functor is faithful.

*Proof.* (a) For \(f\in\mathcal A_Y^{\mathrm{int}}\) and \(x\in X(t)\) we have
\((\varphi^*f)(x)=f(\varphi_t(x))\in\beta(t)\). (b) Existence and uniqueness of \(\varphi_k\) follow from the
universal property of \(X\) for the morphism \(i_Y\circ\varphi\); it is the morphism given by the restriction
\(\mathcal A_Y^{\mathrm{int}}\to\mathcal A_X^{\mathrm{int}}\) of \(\varphi^*\). Uniqueness gives
\((\psi\circ\varphi)_k=\psi_k\circ\varphi_k\). Let \(\varphi,\varphi'\) be morphisms with
\(\varphi_k=\varphi'_k\). Then \(i_Y\circ\varphi=i_Y\circ\varphi'\). Since the maps \((i_Y)_t\) are injective,
\(\varphi_t=\varphi'_t\) for all \(t\). Then, for \(f\in\mathcal A_Y\), the function
\(\varphi^*f-\varphi'^*f\) has the value \(f(\varphi_t(x))-f(\varphi'_t(x))=0\) at every point \(x\) of \(X\), so
it is \(0\) by Corollary 3.4(c). Hence \(\varphi=\varphi'\). \(\square\)

*Reference:* [Soulé 2004, §3.7] states that the extension of scalars is a faithful functor.

The functor is not full; Exercise 2 computes an example.

The following lemma computes the integral functions in the algebraic examples. It needs only one test object.

**Lemma 3.8 (Laurent polynomials at generic roots of unity).** Let \(A\) be a torsion-free ring and
\[
f=\sum_{I\in S}b_I\,T^I\ \in\ A_{\mathbb C}[T_1^{\pm1},\dots,T_d^{\pm1}],
\]
with \(S\subset\mathbb Z^d\) finite and \(b_I\in A_{\mathbb C}\). Let \(n\ge1\) be such that the elements of \(S\)
are pairwise incongruent modulo \(n\). Let \(\xi_1,\dots,\xi_d\) be the standard generators of the group
\((\mu_n)^d\), and \(f(\xi)=\sum_Ib_I\,\xi^I\in A_{\mathbb C}[(\mu_n)^d]\). If \(f(\xi)\) lies in
\(A[(\mu_n)^d]\), then \(b_I\in A\) for all \(I\in S\).

*Proof.* The group ring \(A_{\mathbb C}[(\mu_n)^d]\) is a free \(A_{\mathbb C}\)-module with the group elements as
basis, and \(A[(\mu_n)^d]\) is the set of elements with all coefficients in \(A\). The group elements \(\xi^I\),
\(I\in S\), are pairwise distinct by the choice of \(n\). So \(b_I\) is the coefficient of \(\xi^I\) in
\(f(\xi)\). \(\square\)

The condition on \(n\) holds for every \(n\) larger than all the differences of the coordinates of the exponents
in \(S\).

## 4. Examples

### 4.1 Representable gadgets and the spectrum of \(\mathbb F_{1^n}\)

**Proposition 4.1.** Let \(t_0\) be a test object such that \(\beta(t_0)\) is a finitely generated \(k\)-algebra. Let
\(h_{t_0}\) be the gadget with the points \(h_{t_0}(t)=\operatorname{Hom}_{\mathcal T}(t_0,t)\), the algebra
\(\beta(t_0)_{\mathbb C}\), and the evaluation \(f(u)=\beta(u)_{\mathbb C}(f)\).

(a) For every gadget \(X\) over \(\beta\), the map \(\varphi\mapsto\varphi_{t_0}(\mathrm{id})\) is a bijection from
the set of morphisms \(h_{t_0}\to X\) onto \(X(t_0)\).

(b) The ring of integral functions of \(h_{t_0}\) is \(\beta(t_0)\).

(c) If the sets \(\operatorname{Hom}_{\mathcal T}(t_0,t)\) are finite and \(\beta\) is injective on each of them,
then \(h_{t_0}\) is an affine variety over \(\beta\) with extension of scalars \(\operatorname{Spec}\beta(t_0)\).

*Proof.* (a) By the Yoneda lemma [Stacks, Tag [001P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-yoneda)], the natural transformations from
\(\operatorname{Hom}_{\mathcal T}(t_0,-)\) to \(X\) correspond to the points \(x\in X(t_0)\), by
\(\varphi_t(u)=X(u)x\). A homomorphism \(\varphi^*:\mathcal A_X\to\beta(t_0)_{\mathbb C}\) completes such a
transformation to a morphism of gadgets if and only if \(\beta(u)_{\mathbb C}(\varphi^*f)=f(X(u)x)\) for all
\(u:t_0\to t\) and all \(f\). For \(u=\mathrm{id}\) this says \(\varphi^*=e_X(x)\). Conversely \(e_X(x)\)
satisfies the condition for all \(u\), because \(f(X(u)x)=\beta(u)_{\mathbb C}(f(x))\). (b) A function
\(f\in\beta(t_0)_{\mathbb C}\) is integral if \(\beta(u)_{\mathbb C}(f)\in\beta(t)\) for all \(u\). For
\(u=\mathrm{id}\) this gives \(f\in\beta(t_0)\), and every \(f\in\beta(t_0)\) satisfies the condition. (c) By (b)
and Theorem 3.3 it remains to see that \(i_X\) is an immersion for \(X=h_{t_0}\). Here \((i_X)_t(u)=\beta(u)\),
and \(i_X^*\) is the identity of \(\beta(t_0)_{\mathbb C}\). \(\square\)

**Example 4.2 (\(\operatorname{Spec}E\) and \(\operatorname{Spec}\mathbb F_{1^n}\)).** Take \(\beta=\beta_1\) and
let \(E\) be a finite abelian group. The sets \(\operatorname{Hom}(E,D)\) are finite, the ring \(\mathbb Z[E]\) is
finitely generated, and a homomorphism \(u\) is determined by \(\mathbb Z[u]\). So
\(\operatorname{Spec}E:=h_E\) is an affine variety over \(\mathbb F_1\) with extension of scalars
\(\operatorname{Spec}\mathbb Z[E]\).

*Reference:* [Connes–Consani 2011a, §3.1].

For \(E=\mu_n\) we write \(\operatorname{Spec}\mathbb F_{1^n}\). Its extension of scalars is
\(\operatorname{Spec}R_n\). In this sense
\[
\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z=\mathbb Z[T]/(T^n-1),
\]
which is the formula that [Soulé 1999, §4.1] and [Soulé 2004, §2.4] take as their starting point. By
Proposition 4.1(a), the morphisms \(\operatorname{Spec}\mathbb F_{1^n}\to X\) are the points of \(X(\mu_n)\), for
every gadget \(X\) over \(\mathbb F_1\). We write
\[
X(\mathbb F_{1^n})=X(\mu_n)
\]
and call it the set of *points of \(X\) over \(\mathbb F_{1^n}\)*. For example
\((\operatorname{Spec}\mathbb F_{1^m})(\mathbb F_{1^n})=\operatorname{Hom}(\mu_m,\mu_n)\) has \(\gcd(m,n)\)
elements.

### 4.2 The gadget of a monoid

In this lesson a *monoid* is a commutative monoid, written multiplicatively, with \(1\) and with an absorbing
element \(0\); morphisms preserve \(1\) and \(0\). We recall some notions from *Commutative monoids and their
spectra*. The monoid ring \(\mathbb Z[M]\) is the free abelian group with basis \(M\setminus\{0\}\), with the
product of \(M\), the zero of \(M\) being \(0\). Ring homomorphisms \(\mathbb Z[M]\to R\) are the same as
morphisms from \(M\) to the multiplicative monoid \((R,\cdot)\). A subset generates \(M\) if every non-zero element
is a product of its elements. The monoid \(M\) is *cancellative* if \(M\neq\{0\}\) and \(ab=ac\) with \(a\neq0\)
implies \(b=c\). Then the non-zero elements are closed under multiplication, and they embed into the group \(G\)
of fractions \(a/s\) with \(a,s\neq0\).

**Definition 4.3.** Let \(M\) be a finitely generated monoid. The gadget \(X_M\) over \(\mathbb F_1\) has the points
\(X_M(D)=\operatorname{Hom}(M,D_0)\), the algebra \(\mathbb C[M]=\mathbb Z[M]_{\mathbb C}\), and the evaluation
\(f(x)=x_{\mathbb C}(f)\), where \(x_{\mathbb C}:\mathbb C[M]\to\mathbb C[D]\) is the linear map with
\(m\mapsto x(m)\in D_0\subset\mathbb C[D]\).

A morphism \(x:M\to D_0\) is in particular a morphism \(M\to(\mathbb Z[D],\cdot)\), that is, a ring homomorphism
\(\mathbb Z[M]\to\mathbb Z[D]\). So \(X_M\) is an algebraic sub-gadget of
\(\mathcal G(\operatorname{Spec}\mathbb Z[M])\) in the sense of Corollary 3.5. It is finite, because a morphism is
determined by its values on a finite generating set. The functor \(D\mapsto X_M(D)\) is the functor of points of
the monoid scheme \(\operatorname{Spec}M\), restricted to the monoids \(D_0\).

**Theorem 4.4.** Let \(M\) be a finitely generated cancellative monoid. Then \(X_M\) is an affine variety over
\(\mathbb F_1\), and \(X_M\otimes_{\mathbb F_1}\mathbb Z=\operatorname{Spec}\mathbb Z[M]\).

*Proof.* By Corollary 3.5 we must show that an integral function \(f\in\mathbb C[M]\) lies in \(\mathbb Z[M]\).
Write \(f=\sum_{m\in S}b_m\,m\) with \(S\subset M\setminus\{0\}\) finite. Let \(G\) be the group of fractions of
\(M\setminus\{0\}\). It is a finitely generated abelian group, so, written additively,
\(G\cong\mathbb Z^r\oplus F\) with \(F\) finite [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. Let \(e\) be the exponent of \(F\), let \(c\) be
an integer larger than the absolute values of all coordinates of the \(\mathbb Z^r\)-components of the differences
\(s-s'\) with \(s,s'\in S\), and put \(n=ec\). Then \(nG=n\mathbb Z^r\oplus0\). If a difference \(s-s'=(v,w)\) lies
in \(nG\), then \(w=0\), and \(v\in n\mathbb Z^r\) has coordinates of absolute value less than \(n\), so \(v=0\)
and \(s=s'\). Hence the elements of \(S\) have pairwise distinct images in the finite abelian group \(D=G/nG\).

Let \(x:M\to D_0\) be the map with \(x(0)=0\) that sends \(m\neq0\) to its class in \(D\). It is a morphism of
monoids, so \(x\in X_M(D)\). Its value is \(f(x)=\sum_{m\in S}b_m\,x(m)\), and the group elements \(x(m)\),
\(m\in S\), are pairwise distinct. Since \(f(x)\in\mathbb Z[D]\), every \(b_m\) is an integer. \(\square\)

*Reference:* [Soulé 2004, Théorème 1(i)], with rings as test objects, and Soulé's 2009 Vanderbilt lectures, with
finite abelian groups, treat the monoids of smooth affine toric varieties, with algebras of continuous functions
(Section 5). [Connes–Consani 2011a, Propositions 3.1 and 3.2]
treat the torus and the affine spaces. [López Peña–Lorscheid 2011b, Theorem 2.10] states the result for all
affinely torified varieties. It holds when the fibres over all primes are reduced, and this condition is needed;
see *Torified varieties and the limits of monoid schemes*.

The next proposition describes the points. An *ideal* of \(M\) is a subset \(I\) with \(0\in I\) and
\(MI\subseteq I\); it is *prime* if \(I\neq M\) and \(ab\in I\) implies \(a\in I\) or \(b\in I\). For a prime ideal
\(\mathfrak p\), the localization \(M_{\mathfrak p}\) consists of the fractions \(a/s\) with \(s\notin\mathfrak p\),
and \(G_{\mathfrak p}=(M_{\mathfrak p})^\times\) is its group of units, the set of fractions \(a/s\) with
\(a,s\notin\mathfrak p\).

**Proposition 4.5 (points).** Let \(M\) be a monoid.

(a) For every abelian group \(H\), the set \(\operatorname{Hom}(M,H_0)\) is the disjoint union of the sets
\(\operatorname{Hom}(G_{\mathfrak p},H)\) of group homomorphisms, over the prime ideals \(\mathfrak p\) of \(M\).
A morphism \(x\) corresponds to \(\mathfrak p=x^{-1}(0)\) and to the homomorphism \(a/s\mapsto x(a)x(s)^{-1}\).

(b) For a field \(K\), the \(K\)-points of \(\operatorname{Spec}\mathbb Z[M]\) are the morphisms
\(M\to(K^\times)_0\). So, if \(M\) is finitely generated and \(q\) is a prime power,
\[
\#(\operatorname{Spec}\mathbb Z[M])(\mathbb F_q)=\#X_M(\mathbb F_{1^{q-1}}).
\]

*Proof.* (a) is proved in *Commutative monoids and their spectra*; here is the argument. The set
\(\mathfrak p=x^{-1}(0)\) is an ideal, it does not contain \(1\), and its complement is closed under
multiplication because \(H\) is. So it is prime. The morphism \(x\) maps \(M\setminus\mathfrak p\) into the group
\(H\), so \(a/s\mapsto x(a)x(s)^{-1}\) is a well-defined homomorphism \(G_{\mathfrak p}\to H\). Conversely, given
\(\mathfrak p\) and \(\rho:G_{\mathfrak p}\to H\), put \(x(a)=\rho(a/1)\) for \(a\notin\mathfrak p\) and
\(x(a)=0\) for \(a\in\mathfrak p\). This is a morphism because \(\mathfrak p\) is prime, and the two constructions
are inverse to each other. (b) A \(K\)-point is a ring homomorphism \(\mathbb Z[M]\to K\), that is, a morphism
\(M\to(K,\cdot)\), and \((K,\cdot)=(K^\times)_0\). The group \(\mathbb F_q^\times\) is cyclic of order \(q-1\).
\(\square\)

**Corollary 4.6 (tori and affine spaces).** Let \(a,b\ge0\), and let \(M\) be the monoid of the monomials
\(T_1^{i_1}\cdots T_a^{i_a}S_1^{j_1}\cdots S_b^{j_b}\) with \(i_1,\dots,i_a\in\mathbb Z\) and
\(j_1,\dots,j_b\ge0\), together with \(0\). Then \(X_M\) is an affine variety over \(\mathbb F_1\) with
\[
X_M(D)=D^a\times(D_0)^b,\qquad X_M\otimes_{\mathbb F_1}\mathbb Z=\mathbb G_{m,\mathbb Z}^a\times\mathbb A^b_{\mathbb Z}.
\]
It has \(n^a(n+1)^b\) points over \(\mathbb F_{1^n}\), and its extension of scalars has \((q-1)^aq^b\) points over
\(\mathbb F_q\). We write \(\mathbb G_m^a\times\mathbb A^b\) for this gadget. For a finite set \(F\), the gadget
\(\mathbb A^F\) has the points \((D_0)^F\) and the extension of scalars \(\mathbb A^F_{\mathbb Z}\).

*Proof.* The monoid is generated by the \(T_i^{\pm1}\) and the \(S_j\), and it is cancellative, because its
non-zero elements form a submonoid of a group. A morphism \(M\to D_0\) sends the units \(T_i\) to units and the
\(S_j\) to arbitrary elements of \(D_0\), and these images can be chosen freely. Now apply Theorem 4.4 with
\(\mathbb Z[M]=\mathbb Z[T_1^{\pm1},\dots,T_a^{\pm1},S_1,\dots,S_b]\). \(\square\)

*Reference:* [Connes–Consani 2011a, Propositions 3.1 and 3.2].

In these gadgets the algebra is \(\mathbb C[T_1^{\pm1},\dots,S_b]\), and the value of \(f\) at a point
\((g,h)\in D^a\times(D_0)^b\) is \(f(g,h)\in\mathbb C[D]\).

**Example 4.7 (a cuspidal curve).** Let \(M=\{0,1,T^2,T^3,T^4,\dots\}\), a submonoid of the monoid of the powers of
\(T\). It is generated by \(T^2\) and \(T^3\), it is cancellative, and
\(\mathbb Z[M]=\mathbb Z[T^2,T^3]\cong\mathbb Z[x,y]/(y^2-x^3)\). By Theorem 4.4, \(X_M\) is an affine variety over
\(\mathbb F_1\) whose extension of scalars is the cuspidal cubic \(C=\operatorname{Spec}\mathbb Z[x,y]/(y^2-x^3)\).
The monoid \(M\) has two prime ideals: \(\{0\}\), with \(G_{\{0\}}=\{T^j:j\in\mathbb Z\}\), and
\(M\setminus\{1\}\), with trivial group of units. By Proposition 4.5, \(X_M(D)\) consists of the morphisms
\(T^j\mapsto g^j\) for \(g\in D\), and of the morphism that sends every \(T^j\), \(j\ge2\), to \(0\). So the
functor \(X_M\) is isomorphic to \(D\mapsto D_0\), the functor of the affine line \(\mathbb A^1\). The gadgets
\(X_M\) and \(\mathbb A^1\) are not isomorphic: by Proposition 3.7 an isomorphism would induce an isomorphism
\(\mathbb Z[T]\cong\mathbb Z[T^2,T^3]\), but the second ring is not integrally closed, since \(T=T^3/T^2\) is a
root of \(X^2-T^2\). So two affine varieties over \(\mathbb F_1\) with the same functor of points can have
different extensions of scalars. The algebra decides. Both have \(n+1\) points over \(\mathbb F_{1^n}\), and both
extensions have \(q\) points over \(\mathbb F_q\) by Proposition 4.5(b).

### 4.3 What the definition does not control

**Example 4.8 (the same points, the torus and the line).** Let \(X(D)=D\) for all \(D\). With the algebra
\(\mathbb C[T,T^{-1}]\) and the evaluation \(f(g)\) this is the torus \(\mathbb G_m\) of Corollary 4.6. Now take
the algebra \(\mathbb C[T]\) with the same evaluation. This gadget \(X'\) is an algebraic sub-gadget of
\(\mathcal G(\mathbb A^1_{\mathbb Z})\). Let \(f\in\mathbb C[T]\) be integral. Take \(n\) larger than the degree of
\(f\), \(D=\mu_n\), and \(g\) a generator. By Lemma 3.8 the coefficients of \(f\) are integers. So
\(\mathcal A_{X'}^{\mathrm{int}}=\mathbb Z[T]\), and \(X'\) is an affine variety over \(\mathbb F_1\) with
\(X'\otimes_{\mathbb F_1}\mathbb Z=\mathbb A^1_{\mathbb Z}\). It has \(n\) points over \(\mathbb F_{1^n}\), while
\(\mathbb A^1_{\mathbb Z}\) has \(q\) points over \(\mathbb F_q\). In the same way \(D\mapsto D^d\) with the algebra
\(\mathbb C[T_1,\dots,T_d]\) is an affine variety over \(\mathbb F_1\) with extension of scalars
\(\mathbb A^d_{\mathbb Z}\).

*Reference:* [López Peña–Lorscheid 2011b, Remark 2.11].

So an affine variety over \(\mathbb F_1\) need not have the number of points that its extension of scalars
suggests. By Corollary 3.6 its set of points can be enlarged, and by this example it can be too small.
[Connes–Consani 2011a, §5] and [Connes–Consani 2010, Definition 4.7] add the condition that the points with values
in a field are in bijection with the points of the extension of scalars; see Section 9.

**Example 4.9 (too few points).** Let \(X(D)=\{1\}\subseteq D\), with the algebra \(\mathbb C[T,T^{-1}]\) and the
evaluation \(f\mapsto f(1)\). A function is integral if \(f(1)\in\mathbb Z\). The ring of integral functions
contains the complex vector space \((T-1)\mathbb C[T,T^{-1}]\), so it is uncountable and not finitely generated.
By Theorem 3.3 this gadget has no extension of scalars.

**Example 4.10 (nilpotent elements).** Let \(M=\{0,1,a\}\) with \(a^2=0\). It is finitely generated and not
cancellative, and \(\mathbb Z[M]=\mathbb Z[a]/(a^2)\). Every morphism \(M\to D_0\) sends \(a\) to \(0\), because
\(D_0\) has no nilpotent element other than \(0\). So \(X_M(D)\) is one point \(x_0\), and the value of
\(f=b+ca\) at \(x_0\) is \(b\). The ring of integral functions is \(\mathbb Z+\mathbb Ca\), which is not finitely
generated. So \(X_M\) is not an affine variety over \(\mathbb F_1\), and the hypothesis of Theorem 4.4 cannot be
dropped. Exercise 6 shows that it is not a necessary condition. The example illustrates Corollary 3.4: the test
rings are reduced, so a nilpotent function vanishes at all points, and must be zero.

**Example 4.11 (no integer points).** The scheme \(\operatorname{Spec}\mathbb Z[i]\) is not the extension of
scalars of any affine variety over \(\mathbb F_1\). By Corollary 3.4(d) it would have a point with values in
\(\mathbb Z\), and there is no ring homomorphism \(\mathbb Z[i]\to\mathbb Z\), because \(-1\) is not a square in
\(\mathbb Z\). The reason is that every test ring \(\mathbb Z[D]\) has a homomorphism to \(\mathbb Z\). In
contrast, \(\operatorname{Spec}\mathbb Z[i]\) is an affine variety when rings are the test objects
(Proposition 5.3), and it is an affine variety over \(\mathbb F_{1^2}\) (Example 7.6).

### 4.4 Projective space

Projective space is not affine, and its only global functions are constants. So an algebra is not enough to
describe it. There are two ways to proceed. [Soulé 2004] uses functors on the category of affine varieties over
\(\mathbb F_1\); see Section 5.3. [Connes–Consani 2011a, §3.4] keeps the geometric gadgets of Remark 2.5 and asks
for a cover by affine varieties. We follow the second way, which is enough to count points.

**Definition 4.12.** Let \(X=(X,X_{\mathbb C},e_X)\) be a geometric gadget over \(\mathbb F_1\) and
\(U\subseteq X_{\mathbb C}\) an affine open subscheme. The *restriction* \(X|_U\) is the gadget with the points
\(\{x\in X(D):e_X(x)\text{ factors through }U\}\), the algebra \(\Gamma(U,\mathcal O_U)\), and the evaluation by
pull-back along \(e_X(x)\). The gadget \(X\) is *covered by affine varieties over \(\mathbb F_1\)* if there are
affine open subschemes \(U_1,\dots,U_r\) that cover \(X_{\mathbb C}\) such that every \(X|_{U_j}\) is an affine
variety over \(\mathbb F_1\) and \(X(D)=\bigcup_jX|_{U_j}(D)\) for every \(D\).

For a ring \(A\) and a vector \((a_0,\dots,a_d)\in A^{d+1}\) with at least one coordinate \(a_j\) in \(A^\times\),
we write \([a_0:\dots:a_d]\) for the point of \(\mathbb P^d_{\mathbb Z}(A)\) that lies in the chart
\(U_j=\operatorname{Spec}\mathbb Z[T_i/T_j:i\neq j]\) and has the coordinates \(T_i/T_j\mapsto a_ia_j^{-1}\). It
does not depend on the choice of \(j\), and it does not change when the vector is multiplied by a unit
[Stacks, Tag [01ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-projective-space)].

**Proposition 4.13 (projective space).** Let \(d\ge0\). For a finite abelian group \(D\) let
\(\mathbb P^d(D)\) be the set of orbits of \(D\) on \((D_0)^{d+1}\setminus\{0\}\), where \(D\) acts by
multiplication on all coordinates. For an orbit \([g]=[g_0:\dots:g_d]\) let \(e([g])\) be the point
\([g_0:\dots:g_d]\) of \(\mathbb P^d_{\mathbb C}(\mathbb C[D])\). Then \((\mathbb P^d,\mathbb P^d_{\mathbb C},e)\)
is a geometric gadget over \(\mathbb F_1\), and:

(a) it is covered by \(d+1\) affine varieties over \(\mathbb F_1\), the restrictions to the charts
\(U_{j,\mathbb C}\); each of them is isomorphic to the gadget \(\mathbb A^d\) of Corollary 4.6, and its extension
of scalars is the chart \(U_j\cong\mathbb A^d_{\mathbb Z}\) of \(\mathbb P^d_{\mathbb Z}\);

(b) \(\#\mathbb P^d(D)=\sum_{k=0}^d\binom{d+1}{k+1}|D|^k=1+(|D|+1)+\dots+(|D|+1)^d\).

So \(\mathbb P^d\) has \(N(n+1)\) points over \(\mathbb F_{1^n}\), where \(N(x)=1+x+\dots+x^d\) is the polynomial
that counts the points of \(\mathbb P^d\) over \(\mathbb F_q\) at \(x=q\).

*Proof.* A non-zero vector \(g\) has a coordinate in \(D\), which is a unit of \(\mathbb C[D]\). So \(e([g])\) is
defined, it does not depend on the representative, and it is natural in \(D\). (a) By Lemma 1.1 the scheme
\(\operatorname{Spec}\mathbb C[D]\) is the finite set of the characters \(\chi\), and \(e([g])\) maps the point
\(\chi\) to \([\chi(g_0):\dots:\chi(g_d)]\). This point lies in \(U_j\) if and only if \(\chi(g_j)\neq0\), that is,
\(g_j\neq0\). So the points of the restriction to \(U_{j,\mathbb C}\) are the orbits with \(g_j\neq0\). The map
\([g]\mapsto(g_ig_j^{-1})_{i\neq j}\) is a bijection from this set onto \((D_0)^d\). It is natural in \(D\), and it
is compatible with the evaluations when \(\Gamma(U_{j,\mathbb C},\mathcal O)=\mathbb C[T_i/T_j:i\neq j]\) is
identified with a polynomial ring in \(d\) variables. So the restriction is isomorphic to \(\mathbb A^d\), and
Corollary 4.6 applies. Every orbit has a non-zero coordinate, so the restrictions cover \(\mathbb P^d\). (b) The
orbits whose non-zero coordinates are in the positions of a given set \(Y\) with \(k+1\) elements form the set
\(D^Y/D\), which has \(|D|^k\) elements because \(D\) acts freely on \(D^Y\). There are \(\binom{d+1}{k+1}\) sets
\(Y\). For \(m=|D|\), the binomial theorem gives
\(\sum_{k=0}^d\binom{d+1}{k+1}m^k=((m+1)^{d+1}-1)/m\). \(\square\)

*Reference:* [Connes–Consani 2011a, §3.4].

The extensions of scalars of the \(d+1\) affine varieties are the charts of \(\mathbb P^d_{\mathbb Z}\), and they
glue to \(\mathbb P^d_{\mathbb Z}\). A universal property for glued objects belongs to the theory described in
Section 5.3.

## 5. The formulations of Soulé: continuous functions and rings as test objects

### 5.1 Algebras of continuous functions

In Section 4 the algebra of a gadget is \(O(X_{\mathbb Z})_{\mathbb C}\), so the extension of scalars is visible
from the start. In [Soulé 2004] and in Soulé's 2009 Vanderbilt lectures the algebra is chosen differently. It is an algebra of continuous
functions on a compact set of complex points. That the integral functions are algebraic is then a theorem of
analysis.

**Lemma 5.1.** Let \(\alpha\) be a continuous complex function on the unit circle \(S^1\). Suppose that for every
\(n\ge1\) there is a polynomial \(P_n\in\mathbb Z[T]\) with \(\alpha(\zeta)=P_n(\zeta)\) for all
\(\zeta\in\mu_n\). Then \(\alpha\) is the restriction to \(S^1\) of a Laurent polynomial with integer
coefficients.

*Proof.* For \(j\in\mathbb Z\) let
\(a_j=\frac1{2\pi}\int_0^{2\pi}\alpha(e^{i\theta})e^{-ij\theta}\,d\theta\) be the \(j\)-th Fourier coefficient of
\(\alpha\). The integrand is continuous, so \(a_j\) is the limit of the Riemann sums
\[
a_j(n)=\frac1n\sum_{\zeta\in\mu_n}\alpha(\zeta)\zeta^{-j}=\frac1n\sum_{\zeta\in\mu_n}P_n(\zeta)\zeta^{-j}.
\]
Replacing \(P_n\) by its remainder modulo \(T^n-1\), we may assume \(P_n=\sum_{m=0}^{n-1}c_mT^m\) with
\(c_m\in\mathbb Z\). The sum of \(\zeta^l\) over \(\zeta\in\mu_n\) is \(n\) if \(n\) divides \(l\) and \(0\)
otherwise. So \(a_j(n)=c_m\) for the \(m\) with \(m\equiv j\) modulo \(n\). Thus \(a_j\) is a limit of integers,
and it is an integer. By Bessel's inequality, \(\sum_j|a_j|^2\le\frac1{2\pi}\int_0^{2\pi}|\alpha|^2\,d\theta\), so
\(a_j=0\) for all but finitely many \(j\). Let \(P=\sum_ja_jT^j\). The continuous function \(\alpha-P\) on \(S^1\)
has all Fourier coefficients equal to \(0\). By Fejér's theorem a continuous function on the circle is the uniform
limit of the Cesàro means of its Fourier series. So \(\alpha=P\) on \(S^1\). \(\square\)

**Proposition 5.2 (the torus with continuous functions).** Let \(X\) be the gadget over \(\mathbb F_1\) with
\(X(D)=D\), with the algebra \(C(S^1)\) of continuous complex functions on the circle, and with the evaluation
given by \(\chi(f(g))=f(\chi(g))\) for all \(\chi\in\widehat D\). Then \(X\) is an affine variety over
\(\mathbb F_1\), and \(X\otimes_{\mathbb F_1}\mathbb Z=\mathbb G_{m,\mathbb Z}\).

*Proof.* By Lemma 1.1(b) there is exactly one element \(f(g)\in\mathbb C[D]\) with the prescribed values, and
\(f\mapsto f(g)\) is a homomorphism of algebras. For \(u:D\to D'\) and \(\chi'\in\widehat{D'}\) we have
\(\chi'(f(u(g)))=f(\chi'(u(g)))=(\chi'\circ u)(f(g))\), so \(f(u(g))\) is the image of \(f(g)\) in
\(\mathbb C[D']\). So \(X\) is a gadget. Let \(f\) be integral. For \(D=\mu_n\) and a generator \(\xi\), the value
\(f(\xi)\in\mathbb Z[\mu_n]\) is \(P_n(\xi)\) for a polynomial \(P_n\in\mathbb Z[T]\). The characters of
\(\mu_n\) send \(\xi\) to the elements \(\zeta\) of \(\mu_n\), so \(f(\zeta)=P_n(\zeta)\) for all
\(\zeta\in\mu_n\). By Lemma 5.1, \(f\) is the restriction of a Laurent polynomial with integer coefficients.
Conversely, the restriction of \(P\in\mathbb Z[T,T^{-1}]\) has the value \(P(g)\in\mathbb Z[D]\) at \(g\). A
non-zero Laurent polynomial has finitely many zeros, so restriction to \(S^1\) is injective, and
\(\mathcal A_X^{\mathrm{int}}\cong\mathbb Z[T,T^{-1}]\). This ring is finitely generated. The morphism \(i_X\)
sends \(g\in D\) to the homomorphism \(T\mapsto g\), which determines \(g\), and
\(i_X^*:\mathbb C[T,T^{-1}]\to C(S^1)\) is injective. Now apply Theorem 3.3(c). \(\square\)

*Reference:* Soulé's 2009 Vanderbilt lectures. With rings as test objects and the points \(\mu(R)\), the same algebra
gives the torus of [Soulé 2004, §5.2.2] (Proposition 5.5).

Soulé's 2009 Vanderbilt lectures treat the affine line in the same way: the points are \(D_0\),
and the algebra consists of the continuous functions on the closed unit disc that are holomorphic in the open
disc. Exercise 4 computes its integral functions. Continuity cannot be dropped. In the algebra of all complex
functions on \(S^1\), the function that is \(0\) at the roots of unity and \(1\) elsewhere vanishes at all points
of \(X\). By Corollary 3.4(c) the gadget with this algebra has no extension of scalars.

### 5.2 Rings as test objects

Let \(\mathcal R\) be the category of rings whose additive group is free of finite rank, and
\(\mathcal R_{\mathrm{red}}\) the full subcategory of reduced rings. In [Soulé 2004, Définition 1] a *truc* is a
functor \(X\) from \(\mathcal R\) to sets together with a complex algebra \(\mathcal A_X\) and, for every
\(R\), every \(x\in X(R)\) and every ring homomorphism \(\sigma:R\to\mathbb C\), a homomorphism of algebras
\(e_{x,\sigma}:\mathcal A_X\to\mathbb C\), such that \(e_{X(f)y,\sigma}=e_{y,\sigma\circ f}\) for \(f:R'\to R\) and
\(y\in X(R')\). Morphisms, immersions and affine varieties over \(\mathbb F_1\) are defined as in Definitions 2.3
and 2.4 [Soulé 2004, Définitions 2 and 3]. The truc of a variety \(V\) over \(\mathbb Z\) has the points \(V(R)\)
and the algebra of global functions on \(V_{\mathbb C}\) [Soulé 2004, §3.3].

For \(R\) in \(\mathcal R_{\mathrm{red}}\), the ring \(R\otimes\mathbb Q\) is a reduced algebra of finite dimension
over \(\mathbb Q\), hence a product of number fields, and \(R_{\mathbb C}\) is a product of copies of
\(\mathbb C\), one for each homomorphism \(\sigma:R\to\mathbb C\). So a family \((e_{x,\sigma})_\sigma\) is the
same as one homomorphism \(\mathcal A_X\to R_{\mathbb C}\), and a truc restricted to
\(\mathcal R_{\mathrm{red}}\) is a gadget over the system \(\beta_S\) of Definition 1.3. From now on we take the
reduced rings as test objects; the reference line after Proposition 5.3 explains why. All results of Section 3
apply.

**Proposition 5.3 (finite reduced rings).** Let \(R_0\) be a ring in \(\mathcal R_{\mathrm{red}}\). The gadget
\(\mathcal G(\operatorname{Spec}R_0)\) over \(\beta_S\) is an affine variety over \(\beta_S\), and its extension
of scalars is \(\operatorname{Spec}R_0\).

*Proof.* This gadget is the representable gadget \(h_{R_0}\) of Proposition 4.1, and \(\beta_S\) is the identity.
So it suffices to show that \(\operatorname{Hom}(R_0,R)\) is finite for \(R\) in \(\mathcal R_{\mathrm{red}}\).
Let \(r_1,\dots,r_s\) be a basis of the additive group of \(R_0\). Each \(r_j\) is a root of a monic polynomial
\(P_j\in\mathbb Z[T]\), the characteristic polynomial of the multiplication by \(r_j\). A homomorphism
\(u:R_0\to R\) is determined by the elements \(u(r_j)\), and \(u(r_j)\) is a root of \(P_j\) in
\(R\subseteq R_{\mathbb C}\cong\mathbb C^m\). A non-zero polynomial has finitely many roots in
\(\mathbb C^m\). \(\square\)

*Reference:* [Soulé 2004, Proposition 2] states this for all rings of \(\mathcal R\). For \(R=\mathbb Z[a]/(a^2)\)
the homomorphisms \(a\mapsto ca\), \(c\in\mathbb Z\), show that \(\operatorname{Hom}(R,R)\) is infinite, so the
functor is not finite; so we take reduced rings.

For example \(\operatorname{Spec}\mathbb Z[i]\) is an affine variety in this setting, in contrast with
Example 4.11. The two settings give different classes of varieties.

In [Soulé 2004] the points of the torus over \(R\) are the roots of unity of \(R\). For a group ring they are
known.

**Proposition 5.4 (Higman's theorem for finite abelian groups).** Let \(D\) be a finite abelian group and
\(u\in\mathbb Z[D]\) an element with \(u^m=1\) for some \(m\ge1\). Then \(u=\pm g\) for some \(g\in D\).

*Proof.* Write \(u=\sum_gu_g\,g\). For every character, \(\chi(u)^m=1\), so \(|\chi(u)|=1\). By (1.1),
\(u_h=|D|^{-1}\sum_\chi\chi(u)\chi(h)^{-1}\) is the mean of \(|D|\) complex numbers of absolute value \(1\). So
\(|u_h|\le1\), with equality only if all these numbers are equal to \(u_h\). Since \(u\neq0\), some coefficient
\(u_h\) is a non-zero integer. Then \(|u_h|=1\), so \(u_h=\pm1\) and \(\chi(u)=\pm\chi(h)\) for all \(\chi\), with
the sign of \(u_h\). By Lemma 1.1(b), \(u=\pm h\). \(\square\)

So the set \(\mu(\mathbb Z[D])\) of roots of unity of \(\mathbb Z[D]\) is \(\{\pm g:g\in D\}\), with \(2|D|\)
elements.

**Proposition 5.5 (the torus of [Soulé 2004]).** Let \(X\) be the gadget over \(\beta_S\) with the points
\(X(R)=\mu(R)\), the roots of unity of \(R\), with the algebra \(C(S^1)\), and with the evaluation given by
\(\sigma(f(x))=f(\sigma(x))\) for all homomorphisms \(\sigma:R\to\mathbb C\). Then \(X\) is an affine variety over
\(\beta_S\) with extension of scalars \(\mathbb G_{m,\mathbb Z}\), and \(\#X(R_n)=2n\).

*Proof.* A ring \(R\) in \(\mathcal R_{\mathrm{red}}\) embeds in a product of number fields, and a number field
has finitely many roots of unity. So \(X\) is finite. As in the proof of Proposition 5.2, \(X\) is a gadget. Let
\(f\) be integral. The ring \(R_n=\mathbb Z[\mu_n]\) is reduced, and \(T\in\mu(R_n)\). The value
\(f(T)\in R_n\) is \(P_n(T)\) for some \(P_n\in\mathbb Z[T]\), and applying the homomorphisms
\(T\mapsto\zeta\), \(\zeta\in\mu_n\), gives \(f(\zeta)=P_n(\zeta)\). By Lemma 5.1, \(f\) is the restriction of a
Laurent polynomial with integer coefficients. Conversely the restriction of \(P\in\mathbb Z[T,T^{-1}]\) has the
value \(P(x)\in R\) at \(x\in\mu(R)\). So \(\mathcal A_X^{\mathrm{int}}\cong\mathbb Z[T,T^{-1}]\). The morphism
\(i_X\) is the inclusion \(\mu(R)\subseteq R^\times\) on points, and \(i_X^*\) is the restriction
\(\mathbb C[T,T^{-1}]\to C(S^1)\). Both are injective, and Theorem 3.3(c) applies. By Proposition 5.4,
\(\mu(R_n)=\{\pm T^j\}\) has \(2n\) elements. \(\square\)

*Reference:* [Soulé 2004, §5.2.2].

[Soulé 2004, §5.2.1] defines the affine line by the points \(\mu(R)\cup\{0\}\) and the algebra of continuous
functions on the closed unit disc that are holomorphic inside. It has \(2n+1\) points over \(R_n\).

**The numbers \(2n+1\) and \(n+1\).** With rings as test objects, the points over \(\mathbb F_{1^n}\) are the
points over \(R_n=\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z\), and the affine line has \(2n+1\) of them. So a
variety whose extension of scalars has \(N(q)\) points over \(\mathbb F_q\), for a polynomial \(N\), is expected to
have \(N(2n+1)\) points over \(R_n\). Condition (Z) of [Soulé 2004, §6.1] asks for a polynomial \(N\) with
\(\#X(R_n)=N(2n+1)\) for all \(n\ge1\); it is a condition on the functor \(X\), and it does not mention the points
over finite fields. With finite abelian groups as test objects the affine line has \(n+1\) points over
\(\mathbb F_{1^n}\), as many as \(\mathbb F_{1^n}\) has elements, and the expected number is \(N(n+1)\).
[Connes–Consani 2011a, Introduction] observes that \(N(2n+1)\)
gives \((3^{d+1}-1)/2\) points of \(\mathbb P^d\) for \(n=1\), against the \(d+1\) points of the projective
geometry of dimension \(d\) over \(\mathbb F_1\) that it quotes from Tits. It resolves the conflict by
a grading of the functor, in which \(\mathbb P^d\) has \(d+1\) points of degree \(0\) (Section 7). The
replacement of rings by finite abelian groups is attributed there to a suggestion of Soulé
[Connes–Consani 2011a, §2.2]. This replacement is more than a restriction. The functor \(D\mapsto D\) of the torus
is not the restriction of \(R\mapsto\mu(R)\) to group rings, which is \(D\mapsto\{\pm g\}\) by Proposition 5.4,
and it is not functorial for ring homomorphisms: the automorphism \(g\mapsto-g\) of \(\mathbb Z[\mu_2]\), for the
generator \(g\) of \(\mu_2\), does not preserve the subset \(\mu_2\).

### 5.3 Varieties that are not affine

[Soulé 2004, Définitions 4 and 5] and Soulé's 2009 Vanderbilt lectures define varieties over
\(\mathbb F_1\) that need not be affine. We state the definitions for \(\beta=\beta_1\) or \(\beta=\beta_S\), and
write \(\operatorname{Aff}_\beta\) for the category of affine varieties over \(\beta\) with the morphisms of
gadgets. For a test object \(t\), \(h_t\) is the representable gadget of Proposition 4.1; it is an affine variety
(Example 4.2, Proposition 5.3), and the morphisms \(h_t\to Y\) are the points of \(Y(t)\).

An *object over \(\beta\)* is a triple \((F,\mathcal B,e)\) of a contravariant functor \(F\) from
\(\operatorname{Aff}_\beta\) to sets, a complex algebra \(\mathcal B\), and homomorphisms
\(e_A(x):\mathcal B\to\mathcal A_A\) for \(A\in\operatorname{Aff}_\beta\) and \(x\in F(A)\), with
\(e_{A'}(F(a)x)=a^*\circ e_A(x)\) for every \(a:A'\to A\). A *morphism* of objects is a natural transformation with a
homomorphism of algebras in the opposite direction, compatible with the evaluations; it is an *immersion* if all its
maps are injective. The object is *finite* if every \(F(h_t)\) is finite. For a scheme \(W\) of finite type over
\(\mathbb Z\), the object \(\operatorname{Ob}(W)\) has \(\operatorname{Ob}(W)(A)=\operatorname{Hom}(A_{\mathbb Z},W)\),
the algebra \(\Gamma(W_{\mathbb C},\mathcal O)\), and the evaluation \(f\mapsto i_A^*(v_{\mathbb C}^*f)\) at
\(v:A_{\mathbb Z}\to W\). A *variety over \(\beta\)* is a finite object \(X\) with an immersion
\(X\to\operatorname{Ob}(W)\) through which every morphism from \(X\) to an object \(\operatorname{Ob}(W')\) factors
as \(\operatorname{Ob}(g)\) for exactly one morphism of schemes \(g:W\to W'\); the scheme \(W\) is its *extension
of scalars*. Soulé's 2009 Vanderbilt lectures ask that \(X\) be finite, [Soulé 2004, Définition 5] does not.

*Affine varieties are varieties.* An affine variety \(Y\) gives the object \(\tilde Y\) with
\(\tilde Y(A)=\operatorname{Hom}(A,Y)\), the algebra \(\mathcal A_Y\) and \(e_A(a)=a^*\). The map
\(a\mapsto a_{\mathbb Z}\) is injective (Proposition 3.7(b)), and with \(i_Y^*\) it is an immersion
\(\tilde Y\to\operatorname{Ob}(Y_{\mathbb Z})\); and \(\tilde Y(h_t)=Y(t)\) is finite. Let
\(\Phi:\tilde Y\to\operatorname{Ob}(W)\) be a morphism and \(f=\Phi_Y(\mathrm{id}_Y):Y_{\mathbb Z}\to W\). By
naturality \(\Phi_A(a)=f\circ a_{\mathbb Z}\) for every \(a:A\to Y\), and compatibility with the evaluation at
\(\mathrm{id}_Y\) gives \(\Phi^*=i_Y^*\circ f_{\mathbb C}^*\). So \(\Phi=\operatorname{Ob}(f)\circ(\tilde Y\to
\operatorname{Ob}(Y_{\mathbb Z}))\), and \(f\) is unique, being the value at \(\mathrm{id}_Y\). So \(\tilde Y\) is a
variety with extension of scalars \(Y_{\mathbb Z}\). [Soulé 2004, Proposition 3] states the converse: a variety
whose extension of scalars is affine comes from an affine variety.

**Proposition 5.6 (gluing).** Let \(V=\bigcup_{i\in I}U_i\) be a finite open cover of a scheme of finite type over
\(\mathbb Z\). Let \(Y_i\) and \(Y_{ij}=Y_{ji}\), for \(i\neq j\), be varieties over \(\beta\) with extensions of
scalars \(U_i\) and \(U_i\cap U_j\), and let \(p_{ij}:Y_{ij}\to Y_i\) and \(j_i:Y_i\to\operatorname{Ob}(V)\) be
immersions that induce the inclusions of schemes, with \(j_i\circ p_{ij}=j_j\circ p_{ji}\). Let \(\mathcal B\) be the
algebra of the families \((b_i)\in\prod_i\mathcal B_i\) with \(p_{ij}^*b_i=p_{ji}^*b_j\) for \(i\neq j\), where
\(\mathcal B_i\) is the algebra of \(Y_i\). Suppose:

(E) if \(x_i\in Y_i(A)\) and \(x_j\in Y_j(A)\) have the same image in \(\operatorname{Hom}(A_{\mathbb Z},V)\), then
\(e(x_i)(b_i)=e(x_j)(b_j)\) for all \((b_k)\in\mathcal B\).

Then \(F(A)=\bigcup_ij_i(Y_i(A))\subseteq\operatorname{Hom}(A_{\mathbb Z},V)\), with the algebra \(\mathcal B\) and the
evaluations \(e(j_i(x_i))((b_k))=e(x_i)(b_i)\), is a variety over \(\beta\) with extension of scalars \(V\), and the
maps \(Y_i\to F\) are immersions.

*Proof.* By (E) the evaluations are well defined, and they are natural because those of the \(Y_i\) are. Each
\(F(h_t)\) is a finite union of finite sets. The maps \(j_i^*\) combine to a homomorphism
\(\Gamma(V_{\mathbb C},\mathcal O)\to\mathcal B\), which is injective because a section that vanishes on every
\(U_{i,\mathbb C}\) is zero; with the inclusions of the sets it is an immersion \(F\to\operatorname{Ob}(V)\). The
inclusion \(q_i:Y_i\to F\), with the projection \(\mathcal B\to\mathcal B_i\), is a morphism and an immersion: if
\(b_i=0\), then \(p_{ji}^*b_j=p_{ij}^*b_i=0\), so \(b_j=0\) for all \(j\). Let
\(\Phi:F\to\operatorname{Ob}(W)\) be a morphism. The universal property of \(Y_i\) gives one morphism
\(f_i:U_i\to W\) that induces \(\Phi\circ q_i\); since \(q_i\circ p_{ij}=q_j\circ p_{ji}\), the universal property
of \(Y_{ij}\) gives \(f_i=f_j\) on \(U_i\cap U_j\). So the \(f_i\) glue to \(f:V\to W\). The morphism induced by
\(f\) agrees with \(\Phi\) on every \(j_i(Y_i(A))\), and its algebra map agrees with \(\Phi^*\) after each projection
to \(\mathcal B_i\), hence on \(\mathcal B\subseteq\prod_i\mathcal B_i\). Restriction to the \(U_i\) shows that
\(f\) is unique. \(\square\)

**Example 5.7 (condition (E) is needed).** [Soulé 2004, Proposition 5] and Soulé's 2009 Vanderbilt lectures glue with
the evident evaluations and do not assume (E). In the following example all the other hypotheses hold, and the
evaluations on the union are not well defined. Take \(\beta=\beta_1\) and \(B=\mathbb C[t,s]\). Let \(Y\) be the
gadget with \(Y(D)=D\cup\{0\}\subseteq\mathbb Z[D]\), the algebra \(B\), and the evaluation at a point \(g\) given
by \(\chi(t(g))=\chi(g)\) and \(\chi(s(g))=\exp\chi(g)\) for \(\chi\in\widehat D\), with \(\chi(0)=0\). Its integral
functions are \(\mathbb Z[t]\). Indeed, let \(P\in B\) be integral. For \(D=\mu_n\) with generator \(\xi\), the
value of \(P\) at \(\xi\) lies in \(\mathbb Z[\mu_n]\), so \(\alpha(z)=P(z,e^z)\) satisfies the hypothesis of
Lemma 5.1, and \(\alpha=p\) on \(S^1\) for a Laurent polynomial \(p\) with integer coefficients. By the identity
theorem \(P(z,e^z)=p(z)\) for all \(z\neq0\); as the left side is entire, \(p\) is a polynomial. Write
\(P(t,s)-p(t)=\sum_{j=0}^kq_j(t)s^j\) with \(q_k\neq0\) if this is nonzero; then
\(q_k(x)=-\sum_{j<k}q_j(x)e^{-(k-j)x}\to0\) for real \(x\to\infty\), which a nonzero polynomial does not do. So
\(P=p(t)\in\mathbb Z[t]\), and conversely every \(p(t)\in\mathbb Z[t]\) is integral. The inclusions
\(Y(D)\subseteq\mathbb Z[D]=\mathbb A^1(\mathbb Z[D])\) and \(\mathbb C[t]\subseteq B\) show that \(i_Y\) is an
immersion, so \(Y\) is an affine variety with extension of scalars \(\mathbb A^1_{\mathbb Z}\) (Theorem 3.3(c)). For
\(c\in\{0,1\}\) let \(Y_c\) have the points \(D\cup\{0,2\}\), the same algebra and the same evaluations at the old
points, and at the point \(2\) the evaluation \(t\mapsto2\), \(s\mapsto c\). Homomorphisms of group rings fix \(2\), so
\(Y_c\) is a gadget; its integral functions are again \(\mathbb Z[t]\), and it is an affine variety with extension of
scalars \(\mathbb A^1_{\mathbb Z}\). The inclusions \(Y\to Y_c\), with the identity of \(B\), are immersions that
induce the identity of \(\mathbb A^1_{\mathbb Z}\). Glue \(\tilde Y_0\) and \(\tilde Y_1\) along \(\tilde Y\) for
the cover of \(V=\mathbb A^1_{\mathbb Z}\) by \(U_0=U_1=V\). Then \(\mathcal B\) is the diagonal copy of \(B\). Over
the trivial group, the point \(2\) of \(Y_0\) and the point \(2\) of \(Y_1\) give the same morphism
\(\operatorname{Spec}\mathbb Z\to\mathbb A^1_{\mathbb Z}\), but \((s,s)\) has the value \(0\) at the first and
\(1\) at the second. The same example works with reduced rings as test objects, with the points \(\mu(R)\cup\{0\}\)
and \(\mu(R)\cup\{0,2\}\).

The main example is [Soulé 2004, Théorème 1]; Soulé's 2009 Vanderbilt lectures give its version
for finite abelian groups, as [López Peña–Lorscheid 2011a, §1.5.2] reports. Let \(N\cong\mathbb Z^d\), \(M=\operatorname{Hom}(N,\mathbb Z)\), let \(\Delta\) be a
regular fan in \(N\) (as in *Monoid schemes*, Section 6.5), and let \(V=\mathbb P(\Delta)\) be its toric variety
over \(\mathbb Z\), glued from the charts \(U_\tau=\operatorname{Spec}\mathbb Z[S_\tau]\), \(\tau\in\Delta\), where
\(S_\tau=\tau^\vee\cap M\), with characters \(\chi^m\), \(m\in S_\tau\). For a test object \(t\) put
\((R_t,H_t)=(\mathbb Z[D],D)\) if \(\beta=\beta_1\) and \(t=D\), and \((R_t,H_t)=(R,\mu(R))\) if \(\beta=\beta_S\) and
\(t=R\). Let
\[
X_\tau(t)=\{x\in U_\tau(R_t):\chi^m(x)\in H_t\cup\{0\}\text{ for all }m\in S_\tau\},
\]
and let \(\mathcal A_\tau\) be the algebra of the continuous functions on
\(C_\tau=\{x\in U_\tau(\mathbb C):|\chi^m(x)|\le1\text{ for all }m\in S_\tau\}\) that are holomorphic in the
partial interior of \(C_\tau\). The partial interior is defined through coordinates: since \(\Delta\) is regular, a
basis of \(S_\tau\) identifies \(U_\tau\) with \(\mathbb A^r\times\mathbb G_m^{d-r}\), where \(r=\dim\tau\), and
\(C_\tau\) with \(\bar{\mathbb D}^r\times(S^1)^{d-r}\); a function \(f\) is holomorphic in the partial interior if
\(f(\cdot,u)\) is holomorphic on the open polydisc \(\mathbb D^r\) for every \(u\in(S^1)^{d-r}\), as in Soulé's
2009 Vanderbilt lectures. [Soulé 2004, §5.1] asks for holomorphy in the interior of \(C_\tau\), and the proof of
[Soulé 2004, Théorème 1] describes this interior in coordinates as a product of open discs and circles. The interior of \(C_\tau\) in \(U_\tau(\mathbb C)\) is empty when \(r<d\), so holomorphy in that
interior would be no condition. The value of \(f\in\mathcal A_\tau\) at \(x\in X_\tau(t)\) is the family
\((f(\sigma\circ x))_\sigma\in\prod_\sigma\mathbb C=(R_t)_{\mathbb C}\) over the homomorphisms \(\sigma:R_t\to\mathbb C\)
(Lemma 1.1 and Section 5.2); the complex points \(\sigma\circ x\) lie in \(C_\tau\) because roots of unity have
absolute value \(1\).

**Theorem 5.8 (regular toric varieties).** Let \(\beta\) be \(\beta_1\) or \(\beta_S\).

(a) Each \(X_\tau\) is an affine variety over \(\beta\), with \(\mathcal A_{X_\tau}^{\mathrm{int}}=\mathbb Z[S_\tau]\) and
extension of scalars \(U_\tau\).

(b) If \(\sigma\) is a face of \(\tau\), inclusion of points and restriction of functions form an immersion
\(X_\sigma\to X_\tau\) that induces the open immersion \(U_\sigma\to U_\tau\), and \(X_\sigma(t)=X_\tau(t)\cap
U_\sigma(R_t)\).

(c) The varieties \(\tilde X_\tau\), with the overlaps \(\tilde X_{\tau\cap\nu}\), satisfy the hypotheses of
Proposition 5.6, condition (E) included, for the cover of \(V\) by the \(U_\tau\). The resulting variety
\(X(\Delta)\) over \(\beta\) has extension of scalars \(V\), and \(X(\Delta)(A)=\bigcup_\tau\operatorname{Hom}(A,
X_\tau)\subseteq\operatorname{Hom}(A_{\mathbb Z},V)\). Its algebra consists of the families \((f_\tau)\) with
\(f_\tau=f_\nu\) on \(C_{\tau\cap\nu}\), that is, of the continuous functions on \(\bigcup_\tau C_\tau\subseteq
V(\mathbb C)\) whose restrictions to the \(C_\tau\) lie in the \(\mathcal A_\tau\).

*Proof.* *Coordinates.* Let \(\tau\) have dimension \(r\). Its primitive ray generators extend to a basis
\(n_1,\dots,n_d\) of \(N\), with \(\tau\) generated by \(n_1,\dots,n_r\). For the dual basis \(m_1,\dots,m_d\),
\(S_\tau=\mathbb Nm_1\oplus\dots\oplus\mathbb Nm_r\oplus\mathbb Zm_{r+1}\oplus\dots\oplus\mathbb Zm_d\), so
\(\mathbb Z[S_\tau]=\mathbb Z[z_1,\dots,z_r,u_{r+1}^{\pm1},\dots,u_d^{\pm1}]\) with \(z_j=\chi^{m_j}\) and
\(u_j=\chi^{m_j}\). Then \(C_\tau=\bar{\mathbb D}^r\times(S^1)^{d-r}\), and
\(X_\tau(t)=(H_t\cup\{0\})^r\times H_t^{d-r}\): a coordinate \(u_j\) has its inverse among the characters, and the
nonzero elements of \(H_t\cup\{0\}\) are units. Another such basis permutes the disc coordinates and multiplies them
by monomials in the circle coordinates, and it changes the circle coordinates by an invertible monomial
substitution; so holomorphy in the partial interior does not depend on the basis.

*Functions on \(C_\tau\).* For \(f\in\mathcal A_\tau\), \(z\in\mathbb D^r\) and \(u\in(S^1)^{d-r}\),
\[
f(z,u)=\int_{(S^1)^r}f(w,u)\prod_{j=1}^r\frac1{1-z_j/w_j}\,d\lambda(w),
\]
where \(\lambda\) is the normalized Haar measure: apply Cauchy's formula in each disc variable on circles of radius
\(\rho<1\), and let \(\rho\to1\), using uniform continuity on the compact set \(C_\tau\). So \(f\) is determined by its
restriction to the torus \(T^d=(S^1)^d\). Its Fourier coefficients \(\int_{T^d}f(w)w^{-k}\,d\lambda(w)\) vanish when
\(k_j<0\) for some \(j\le r\), by Cauchy's theorem in \(w_j\) on the circle of radius \(\rho\) and the same limit. If
some disc variables are fixed on their boundary circles, \(f\) is still holomorphic in the remaining disc variables,
as a locally uniform limit of holomorphic functions.

*Integral sampling.* Let \(F\in C(T^d)\). Suppose that for every \(n\ge1\) there is \(Q_n\in\mathbb Z[D_n]\), where
\(D_n=(\mu_n)^d\) with standard generators \(\xi_1,\dots,\xi_d\), such that \(\chi(Q_n)=F(\chi(\xi_1),\dots,
\chi(\xi_d))\) for all characters \(\chi\) of \(D_n\). Then \(F\) is the restriction of a Laurent polynomial with
integer coefficients. Indeed, as in the proof of Lemma 5.1, the Fourier coefficient \(c_k\) of \(F\) is the limit of
the Riemann sums \(n^{-d}\sum_aF(\zeta^{a_1},\dots,\zeta^{a_d})\zeta^{-a\cdot k}\), \(\zeta=e^{2\pi i/n}\), and each
of these is a coefficient of \(Q_n\) by Lemma 1.1. So \(c_k\in\mathbb Z\); only finitely many \(c_k\) are nonzero, by
Bessel's inequality; and \(F-\sum_kc_kw^k\) has all its Fourier coefficients equal to \(0\), so it vanishes, because
the trigonometric polynomials are dense in \(C(T^d)\) by the Stone–Weierstrass theorem.

*(a)* The sets \(X_\tau(t)\) are finite: \(D\) is finite, and so is \(\mu(R)\) for \(R\) in \(\mathcal R_{\mathrm{red}}\)
(proof of Proposition 5.5). The evaluations are homomorphisms and natural in \(t\), so \(X_\tau\) is a finite gadget.
Every \(g\in\mathbb Z[S_\tau]\) is integral, since its value at \(x\) is \(g(x)\in R_t\). Conversely, let \(f\) be
integral. For \(\beta_1\) use the test object \(D_n\), for \(\beta_S\) the ring \(\mathbb Z[D_n]\), which lies in
\(\mathcal R_{\mathrm{red}}\) by Lemma 1.1; in both cases use the point with coordinates \(\xi_1,\dots,\xi_d\).
Integrality and the preceding paragraph show that \(f|_{T^d}\) is an integer Laurent polynomial. It has no negative
exponents in the disc variables, so it is the restriction of some \(g\in\mathbb Z[S_\tau]\), and \(f=g\), since both
lie in \(\mathcal A_\tau\) and agree on \(T^d\). Hence \(\mathcal A_{X_\tau}^{\mathrm{int}}=\mathbb Z[S_\tau]\), a
finitely generated ring. The map \(i_{X_\tau}\) is injective on points, since a point is determined by its
coordinates, and \(i_{X_\tau}^*:\mathbb C[S_\tau]\to\mathcal A_\tau\) is injective, since restriction to \(T^d\)
recovers the coefficients. Theorem 3.3(c) proves (a).

*(b)* After reordering, \(\sigma\) is generated by \(n_1,\dots,n_q\) with \(q\le r\). Then \(\mathbb Z[S_\sigma]=
\mathbb Z[S_\tau][(z_{q+1}\cdots z_r)^{-1}]\), so \(U_\sigma=D(z_{q+1}\cdots z_r)\subseteq U_\tau\), and
\(C_\sigma=\bar{\mathbb D}^q\times(S^1)^{d-q}\subseteq C_\tau\). Restriction maps \(\mathcal A_\tau\) into
\(\mathcal A_\sigma\), by the last remark on functions, and injectively, since both algebras are determined on
\(T^d\). A point of \(X_\tau(t)\) lies in \(U_\sigma(R_t)\) exactly when \(z_{q+1},\dots,z_r\) are units, that is, lie
in \(H_t\); so \(X_\sigma(t)=X_\tau(t)\cap U_\sigma(R_t)\). The two maps are compatible with the evaluations, so they
form an immersion; on integral functions it is the localization, which induces \(U_\sigma\to U_\tau\).

*(c)* For \(\tau,\nu\in\Delta\), the cone \(\sigma=\tau\cap\nu\) is a face of both, and \(S_\sigma=S_\tau+S_\nu\) by
Facts 6.10(C4) of *Monoid schemes*. So \(U_\tau\cap U_\nu=U_\sigma\) in \(V\);
\(C_\tau\cap C_\nu=C_\sigma\) in \(V(\mathbb C)\), because \(|\chi^{m+m'}|=|\chi^m||\chi^{m'}|\); and
\(X_\tau(t)\cap X_\nu(t)=X_\sigma(t)\) in \(V(R_t)\), by (b). The space \(V(\mathbb C)\) is Hausdorff: on
\(U_\tau(\mathbb C)\times U_\nu(\mathbb C)\) the diagonal is the image of \(U_\sigma(\mathbb C)\), which is closed,
because \(\mathbb C[S_\tau]\otimes\mathbb C[S_\nu]\to\mathbb C[S_\sigma]\) is onto. So the compact sets \(C_\tau\) are
closed, and the families \((f_\tau)\) that agree on the \(C_{\tau\cap\nu}\) are the continuous functions described in
(c). By (a) and the paragraph *Affine varieties are varieties*, the \(\tilde X_\tau\) and \(\tilde X_{\tau\cap\nu}\)
are varieties with the right extensions of scalars. The maps of (b) give immersions
\(\tilde X_{\tau\cap\nu}\to\tilde X_\tau\): on sets because extension of scalars is faithful (Proposition 3.7(b))
and \(U_{\tau\cap\nu}\to U_\tau\) is a monomorphism, on algebras by (b). The maps \(\tilde X_\tau\to\operatorname{Ob}(V)\)
are immersions: on sets for the same reasons, and on algebras because \(\Gamma(V_{\mathbb C},\mathcal O)\to\mathbb
C[S_\tau]\to\mathcal A_\tau\) is injective, all charts containing the torus \(U_{\{0\}}\). It remains to check (E).
Let \(a:A\to X_\tau\) and \(b:A\to X_\nu\) induce the same morphism \(A_{\mathbb Z}\to V\), and let \((f_\lambda)\) lie
in the algebra. For every test object \(t\) and every \(p\in A(t)\), the points \(a_t(p)\) and \(b_t(p)\) are the same
point of \(V(R_t)\), because \(i_{X_\tau}\circ a=\mathcal G(a_{\mathbb Z})\circ i_A\), and likewise for \(b\)
(Proposition 3.7(b)). This point lies in \(X_\sigma(t)\), and \(f_\tau=f_\nu\) on \(C_\sigma\); so
\(f_\tau(a_t(p))=f_\nu(b_t(p))\), that is, \(a^*f_\tau-b^*f_\nu\) vanishes at every point of \(A\). By Corollary 3.4(c),
\(a^*f_\tau=b^*f_\nu\). Proposition 5.6 now gives (c). \(\square\)

So the functor of \(X(\Delta)\) on affine varieties \(A\) is the union over the cones \(\tau\) of the sets of
morphisms of gadgets \(A\to X_\tau\), as in Soulé's 2009 Vanderbilt lectures. The proof of [Soulé 2004,
Théorème 1] describes it through the morphisms of schemes \(A_{\mathbb Z}\to U_\tau\) instead; these are more. With
reduced rings as test objects, take for \(A\) the gadget of \(\operatorname{Spec}\mathbb Z\) and the chart
\(U=\mathbb A^1\): the morphisms of schemes \(\operatorname{Spec}\mathbb Z\to\mathbb A^1_{\mathbb Z}\) correspond to
the integers, while a morphism of gadgets sends the point of \(A\) over \(\mathbb Z\) to a point of
\(X_U(\mathbb Z)=\{0,1,-1\}\). In a lattice of rank one, Proposition 5.5 is the case of
the zero cone with reduced rings as test objects, and Proposition 5.2 and Exercise 4 are the cases of the zero cone
and of a half-line with finite abelian groups as test objects. With the algebra \(O(U_\tau)_{\mathbb C}\) in place
of the continuous functions, Theorem 4.4 covers the charts of all toric varieties, regular or not, because the
monoids \((S_\tau)_0\) are finitely generated and cancellative; see *Commutative monoids and their spectra*.

[Soulé 2004, §5.4] asks whether Chevalley group schemes and their flag varieties can be defined over
\(\mathbb F_1\). Section 8 presents the answer of [Connes–Consani 2011a] for Chevalley groups.

### 5.4 Three versions of the definition

Soulé gave the definition in three forms, and they are different.

The first is [Soulé 1999, §4]. The test rings are the rings \(R_n\) and their tensor products, that is, the group
rings of finite abelian groups, with all ring homomorphisms between them. A variety over \(\mathbb F_1\) is a
functor \(X\) from these rings to finite sets with natural inclusions \(X(R)\subseteq X_{\mathbb Z}(R)\), for a
variety \(X_{\mathbb Z}\) over \(\mathbb Z\). No algebra is part of the data. The universal property is asked only
for "good" natural transformations from \(X\) to the functors of varieties over \(\mathbb Z\). Three meanings of
"good" are proposed; the first asks that the transformation be induced by a continuous map on the closure of the
set of complex points of \(X\). [Soulé 1999, Lemma 2] sketches the universal property for the functor
\(R\mapsto\mu(R)\) and affine targets, with the argument of Lemma 5.1.

The second is [Soulé 2004], described in Section 5.2. All rings of \(\mathcal R\) are test rings, the algebra
with its evaluations is part of the object, and the universal property is asked for all morphisms.

The third is in Soulé's 2009 Vanderbilt lectures. It takes up the changes of [Connes–Consani 2011a], namely finite abelian groups as
test objects and the count \(N(n+1)\), and it keeps the complex algebra. It is the definition of Section 2.

A statement proved for one of the three does not transfer to the others without an argument. This lesson uses the
third, and the second in Section 5.2.

## 6. The zeta function

The zeta function of a variety over \(\mathbb F_q\) is built from its numbers of points over the fields
\(\mathbb F_{q^r}\). For a variety over \(\mathbb F_1\) whose numbers of points are the values of a polynomial, the
same recipe has a limit as \(q\to1\). References for this section are [Soulé 2004, §6] and [Kurokawa 2005].

**Definition 6.1.** Let \(X\) be a finite gadget over \(\mathbb F_1\). A polynomial \(N\in\mathbb Z[x]\) is the
*counting polynomial* of \(X\) if
\[
\#X(\mathbb F_{1^n})=N(n+1)\qquad\text{for all }n\ge1 .
\]

A polynomial is determined by infinitely many of its values, so \(X\) has at most one counting polynomial. The
argument \(n+1\) is the number of elements of \(\mathbb F_{1^n}\). If \(q\) is a prime power, the multiplicative
monoid of \(\mathbb F_q\) is isomorphic to \(\mathbb F_{1^{q-1}}\), and \(N(q)\) is the number one expects for the
points of the extension of scalars over \(\mathbb F_q\). For the gadget of a monoid this expectation is a theorem
(Proposition 4.5(b)); in general it can fail (Example 4.8). Three conditions of this kind are in use, and they
must be kept apart.

- \(\#X(\mathbb F_{1^n})=N(n+1)\), for finite abelian groups as test objects: Soulé's 2009 Vanderbilt lectures and
  [Connes–Consani 2010, Theorem 4.10].
- \(\#X(R_n)=N(2n+1)\), for rings as test objects: [Soulé 1999, §6] and [Soulé 2004, §6.1, condition (Z)]; see
  Section 5.2.
- \(\#X_{\mathbb Z}(\mathbb F_q)=N(q)\) for all prime powers \(q\), a condition on a scheme over \(\mathbb Z\)
  alone: [Kurokawa 2005, Theorem 1], [Deitmar 2006] and [Deitmar–Koyama–Kurokawa 2008, §1].

For the torus \(\mathbb G_m\) and the affine line the three conditions hold with the same polynomial, \(x-1\) and
\(x\) (Corollary 4.6 and Section 5.2). The gadget \(\mathbb G_m^a\times\mathbb A^b\) has the counting polynomial
\((x-1)^ax^b\), and \(\mathbb P^d\) has the counting polynomial \(1+x+\dots+x^d\) (Proposition 4.13); in both
cases the third condition holds with the same polynomial, and [Soulé 2004, Théorème 2(i)] proves the second
condition for smooth toric varieties. The cuspidal curve of Example 4.7 has the counting polynomial \(x\). The
gadget \(\operatorname{Spec}\mathbb F_{1^m}\), \(m\ge2\), has \(\gcd(m,n)\) points over \(\mathbb F_{1^n}\), which
is not a polynomial in \(n\), so it has no counting polynomial.

**Theorem 6.2 (the limit formula).** Let \(N(x)=\sum_{i=0}^da_ix^i\in\mathbb Z[x]\).

(a) Let \(q>1\) be real and \(T\in\mathbb C\) with \(|T|<q^{-d}\). Then the series \(\sum_{r\ge1}N(q^r)T^r/r\)
converges absolutely, and
\[
Z_N(q,T):=\exp\Big(\sum_{r\ge1}N(q^r)\frac{T^r}{r}\Big)=\prod_{i=0}^d(1-q^iT)^{-a_i}.
\]

(b) Let \(s\in\mathbb C\) be different from every \(i\) with \(a_i\neq0\). Then for all \(q>1\) close enough to
\(1\) the number \(Z_N(q,q^{-s}):=\prod_i(1-q^{i-s})^{-a_i}\) is defined, and, as \(q\) tends to \(1\) from above,
\[
\lim_{q\to1}Z_N(q,q^{-s})\,(q-1)^{N(1)}=\prod_{i=0}^d(s-i)^{-a_i}.
\]
For \(\operatorname{Re}s>d\) the number \(Z_N(q,q^{-s})\) is the value of the series of (a) at \(T=q^{-s}\).

*Proof.* (a) For \(u\ge1\) we have \(|N(u)|\le Cu^d\) with \(C=\sum_i|a_i|\). So the terms of the series are
bounded by \(C(q^d|T|)^r\), and \(q^d|T|<1\). For \(|w|<1\) we have \(\sum_{r\ge1}w^r/r=-\log(1-w)\), with the
principal branch of the logarithm. For \(w=q^iT\) this gives
\[
\sum_{r\ge1}N(q^r)\frac{T^r}r=\sum_ia_i\sum_{r\ge1}\frac{(q^iT)^r}{r}=-\sum_ia_i\log(1-q^iT),
\]
and the formula follows by taking exponentials. (b) Let \(c=i-s\neq0\). The function \(q\mapsto q^c=\exp(c\log q)\)
has the derivative \(c\) at \(q=1\), so
\[
\frac{1-q^{i-s}}{q-1}\longrightarrow s-i\qquad(q\to1).
\]
In particular \(1-q^{i-s}\neq0\) for \(q\neq1\) close to \(1\). Since \(\sum_ia_i=N(1)\),
\[
Z_N(q,q^{-s})\,(q-1)^{N(1)}=\prod_i\Big(\frac{1-q^{i-s}}{q-1}\Big)^{-a_i}\longrightarrow\prod_i(s-i)^{-a_i}.
\]
Only the factors with \(a_i\neq0\) occur. The last statement holds because
\(|q^{-s}|=q^{-\operatorname{Re}s}<q^{-d}\). \(\square\)

*Reference:* [Soulé 2004, Lemme 1]; [Kurokawa 2005, Theorem 2]. [Soulé 2004, Lemme 1]
states that the limit is a polynomial in \(s\), for every real \(s\); for \(N(x)=x-1\) the limit is a quotient of
two polynomials of degree one [Soulé 2004, §6.3.3], and at \(s=i\) with \(a_i\neq0\) the function of \(q\) is
identically zero or not defined, so the theorem is stated for the other values of \(s\), with a rational function
as the limit.

**Definition 6.3.** For \(N=\sum_ia_ix^i\in\mathbb Z[x]\) put
\[
\zeta_N(s)=\prod_{i}(s-i)^{-a_i},
\]
a rational function of \(s\). If \(X\) is a finite gadget over \(\mathbb F_1\) with counting polynomial \(N\), then
\(\zeta_X=\zeta_N\) is the *zeta function of \(X\)*.

**The two conventions.** Two reciprocal functions carry the name of zeta function over \(\mathbb F_1\). This lesson
uses
\[
\zeta_N(s)=\lim_{q\to1}Z_N(q,q^{-s})\,(q-1)^{N(1)}=\prod_i(s-i)^{-a_i},
\]
which is the convention of [Kurokawa 2005, Definition 2], [Connes–Consani 2010, §2] and Soulé's 2009 Vanderbilt lectures. The
other convention is the reciprocal,
\[
\lim_{q\to1}Z_N(q,q^{-s})^{-1}(q-1)^{-N(1)}=\prod_i(s-i)^{a_i}=\zeta_N(s)^{-1},
\]
used in [Soulé 2004, Lemme 1], [Deitmar 2006] and [Deitmar–Koyama–Kurokawa 2008, §1]. A formula quoted from these
three works must be inverted: for \(\mathbb P^d\) their convention gives \(s(s-1)\cdots(s-d)\)
[Soulé 2004, §6.3.5], and this lesson gives \(1/(s(s-1)\cdots(s-d))\). [Soulé 1999, §6] prints the relation
\(Z(q,q^{-s})\sim(q-1)^\chi\zeta_X(s)\) together with \(\zeta_{\mathbb P^N}(s)=s(s-1)\cdots(s-N)\). By Theorem 6.2
the two agree when \(Z\) is replaced by \(Z^{-1}\), so that work belongs to the second convention.
[Manin 1995, §1.6] attaches the function \((s-1)/2\pi\) to an "absolute Tate motive" \(\mathbb T\), which it
describes as the motive of an affine line over an "absolute point", and the function \(s/2\pi\) to the absolute
point; its formula (1.30) gives \((s-n)/2\pi\) for the \(n\)-th power of \(\mathbb T\) when \(n\le0\). In
[Manin 1995, §1.1–1.2] the zeta function of a variety is the alternating product of the zeta functions of its
motives, and the motives of even weight carry the exponent \(-1\). So the functions \(1/s\) of the point and
\(1/(s-1)\) of the affine line in the first convention are the inverses of Manin's factors, up to the constant
\(2\pi\), as it should be for the zeta function of a variety. [Connes–Consani 2011a, Introduction] makes this
remark.

**Proposition 6.4 (rules).** Let \(N,N'\in\mathbb Z[x]\), \(N=\sum_{i=0}^da_ix^i\).

(a) \(\zeta_{N+N'}=\zeta_N\zeta_{N'}\) and \(\zeta_{-N}=\zeta_N^{-1}\). The order of \(\zeta_N\) at \(s=i\) is
\(-a_i\), so \(\zeta_N\) determines \(N\).

(b) \(\zeta_{xN}(s)=\zeta_N(s-1)\).

(c) \(\zeta_{(x-1)N}(s)=\zeta_N(s-1)/\zeta_N(s)\).

(d) \(\zeta_N(s)\,s^{N(1)}\to1\) as \(|s|\to\infty\).

(e) For \(\operatorname{Re}s>d\),
\[
\frac{\zeta_N'(s)}{\zeta_N(s)}=-\sum_i\frac{a_i}{s-i}=-\int_1^\infty N(u)\,u^{-s}\,\frac{du}u .
\]

(f) For \(b\ge0\), \(\zeta_{(x-1)^b}(s)=\prod_{j=0}^b(s-j)^{(-1)^{b-j+1}\binom bj}\).

*Proof.* (a) The exponents add. (b) The coefficient of \(x^i\) in \(xN\) is \(a_{i-1}\), and
\(\prod_i(s-i)^{-a_{i-1}}=\prod_i(s-1-i)^{-a_i}\). (c) follows from \((x-1)N=xN-N\), (a) and (b). (d)
\(\zeta_N(s)s^{N(1)}=\prod_i(1-i/s)^{-a_i}\). (e) The first equality is the logarithmic derivative of the product.
For the second, \(\int_1^\infty u^{i-s-1}du=1/(s-i)\) for \(\operatorname{Re}s>i\). (f) The coefficient of
\(x^j\) in \((x-1)^b\) is \((-1)^{b-j}\binom bj\). \(\square\)

*Reference:* [Kurokawa 2005, Theorem 3] contains (c) for the general and special linear groups, and
[Kurokawa 2005, Theorem 4] follows from (d); [Connes–Consani 2010, Lemma 2.1] is (e), for continuous functions
\(N\) of polynomial growth.

The integral in (e) makes sense for counting functions that are not polynomials. [Connes–Consani 2010, §2] uses
it to determine the counting function of a curve whose zeta function is the completed Riemann zeta function; see
*Weil's proof for curves and what is missing over the integers*.

**Example 6.5 (computations).** Here \(N\) is the counting polynomial and \(\zeta\) the zeta function.

- The point \(\operatorname{Spec}\mathbb F_1\): \(N=1\), \(\zeta(s)=1/s\).
- The affine space \(\mathbb A^b\): \(N=x^b\), \(\zeta(s)=1/(s-b)\).
- The torus \(\mathbb G_m\): \(N=x-1\), \(\zeta(s)=s/(s-1)\).
- The torus \(\mathbb G_m^2\): \(N=(x-1)^2=x^2-2x+1\), \(\zeta(s)=(s-1)^2/(s(s-2))\).
- \(\mathbb G_m^a\times\mathbb A^b\): \(N=(x-1)^ax^b\), and \(\zeta(s)=\zeta_{(x-1)^a}(s-b)\) by
  Proposition 6.4(b), with \(\zeta_{(x-1)^a}\) given by Proposition 6.4(f).
- The projective space \(\mathbb P^d\): \(N=1+x+\dots+x^d\), \(\zeta(s)=1/(s(s-1)\cdots(s-d))\).
- The cuspidal curve of Example 4.7: \(N=x\), \(\zeta(s)=1/(s-1)\), as for the affine line.
- The gadget \(X'\) of Example 4.8: \(N=x-1\) and \(\zeta(s)=s/(s-1)\), although its extension of scalars is the
  affine line.
- The group \(\mathrm{SL}_2\) (Section 8): \(N=x^3-x\), \(\zeta(s)=(s-1)/(s-3)\).

In [Soulé 2004, §6.3] the point, the affine line, the torus \(\mathbb G_m\) and \(\mathbb P^d\) appear with the
functions \(s\), \(s-1\), \((s-1)/s\) and \(s(s-1)\cdots(s-d)\), in the reciprocal convention. In
Soulé's 2009 Vanderbilt lectures the torus has \(s/(s-1)\), as here. The value \(N(1)\) is the exponent of \(q-1\) in
Theorem 6.2(b): \(Z_N(q,q^{-s})\) has a pole of order \(N(1)\) at \(q=1\) if \(N(1)>0\). It is \(1\) for the affine
spaces, \(0\) for the tori of positive dimension, and \(d+1\) for \(\mathbb P^d\). For smooth toric varieties
[Soulé 2004, Théorème 2(i)] identifies \(N(1)\) with the Euler characteristic of the space of complex points.

The definition also applies to a polynomial that counts points over finite fields. For example the Grassmannian of
lines in \(\mathbb P^3\) has \(N(q)=(q^2+1)(q^2+q+1)=q^4+q^3+2q^2+q+1\) points over \(\mathbb F_q\) (see *Counting
over finite fields and the limit q → 1*), and \(\zeta_N(s)=1/(s(s-1)(s-2)^2(s-3)(s-4))\), with \(N(1)=6\).
[Soulé 2004, §5.4 and Théorème 2(iii)] defines a functor with \(N(2n+1)\) points over \(R_n\) from a cell
decomposition of this Grassmannian, and asks whether it is a variety over \(\mathbb F_1\).

**Other zeta functions.** [Deitmar–Koyama–Kurokawa 2008, §2–3] and [Kim–Koyama–Kurokawa 2009] study different
functions, which use the numbers of points over all \(\mathbb F_{1^m}\) directly, such as
\(\exp\big(\sum_{m\ge1}\#X(\mathbb F_{1^m})T^m/m\big)\). These functions are sensitive to torsion, and
[Kim–Koyama–Kurokawa 2009, Theorems 2 and 3] prove functional equations and an analogue of the Riemann hypothesis
for them when \(X\) is the spectrum of a finitely generated abelian group with zero. They are not used in this
lesson.

## 7. Gradings and the extensions \(\mathbb F_{1^n}\)

### 7.1 Graded gadgets

[Connes–Consani 2011a] refines the functor of a gadget by a grading. The guiding principle, stated in
[Connes–Consani 2011a, §3], is the Taylor expansion of the counting polynomial at \(q=1\): if
\(N(q)=\sum_jc_j(q-1)^j\), there should be \(c_j|D|^j\) points of degree \(j\) over \(D\).

**Definition 7.1.** A *grading* of a gadget \(X\) over \(\mathbb F_1\) is a decomposition
\(X(D)=\coprod_{j\ge0}X^{(j)}(D)\) for every \(D\), such that the maps \(X(u)\) preserve the degree \(j\). A
*graded gadget* is a gadget with a grading. The grading is a *counting grading* if there are integers \(c_j\),
\(j\ge0\), with
\[
\#X^{(j)}(D)=c_j\,|D|^j\qquad\text{for all }D\text{ and }j .
\]

*Reference:* [Connes–Consani 2011a, Definition 2.6] for graded gadgets.

[Connes–Consani 2011a, Definition 2.8] asks that an affine variety over \(\mathbb F_1\) be graded. The grading
plays no role in the universal property. Morphisms of gadgets are not required to preserve degrees, and every
gadget has the grading in which all points have degree \(0\). The content of the refinement lies in the gradings
chosen in the examples. Those of the affine spaces, the tori and the projective spaces are counting gradings; that of
\(\operatorname{Spec}E\), for a nontrivial finite abelian group \(E\), is not (Example 7.3).

**Proposition 7.2.** Let \(X\) be a finite gadget over \(\mathbb F_1\) with a counting grading, with constants
\(c_j\).

(a) \(c_j\ge0\), and \(c_j=0\) for all but finitely many \(j\).

(b) \(\#X(D)=N(|D|+1)\) for every finite abelian group \(D\), where \(N(x)=\sum_jc_j(x-1)^j\). In particular \(N\)
is the counting polynomial of \(X\).

(c) The set \(X^{(0)}(D)\) has \(N(1)=c_0\) elements for every \(D\).

(d) \(\zeta_X(s)=\prod_j\zeta_{(x-1)^j}(s)^{c_j}\).

*Proof.* For the trivial group, \(c_j=\#X^{(j)}(1)\ge0\) and \(\sum_jc_j=\#X(1)\) is finite. This gives (a). (b) and
(c) follow by summing over \(j\), and (d) follows from Proposition 6.4(a). \(\square\)

So the Taylor coefficients of \(N\) at \(1\) are non-negative. For example, no gadget with a counting grading has
the counting polynomial \(x-2=(x-1)-1\), which counts the points of the projective line minus three points over
\(\mathbb F_q\). By (c) the number of points of degree \(0\) does not depend on \(D\); it is \(N(1)\). For
\(\mathbb P^d\) these are \(d+1\) points, as in the projective space over \(\mathbb F_1\) of Tits (Example 7.3).
For a Chevalley group of positive rank there are no points of degree \(0\), and the points of lowest degree carry
the group structure that goes back to Tits (Section 8).

**Example 7.3.** The gadgets of Section 4 carry the following gradings, taken from [Connes–Consani 2011a, §3].

- \(\mathbb A^F\): the degree of a point of \((D_0)^F\) is the number of its non-zero coordinates. There are
  \(\binom{|F|}j|D|^j\) points of degree \(j\), in agreement with \(x^{|F|}=\sum_j\binom{|F|}j(x-1)^j\).
- \(\mathbb G_m^a\): all points have degree \(a\). For \(\mathbb G_m^a\times\mathbb A^b\) the degree is \(a\) plus
  the number of non-zero coordinates in \((D_0)^b\).
- \(\mathbb P^d\): the degree of an orbit is the number of its non-zero coordinates minus one. By the proof of
  Proposition 4.13(b) there are \(\binom{d+1}{k+1}|D|^k\) points of degree \(k\). The \(d+1\) points of degree
  \(0\) are the coordinate points \([0:\dots:1:\dots:0]\), for every \(D\).
- \(\operatorname{Spec}E\): all points have degree \(0\). This is a counting grading only if \(E\) is trivial,
  because \(\#\operatorname{Hom}(E,D)\) depends on \(D\) otherwise.

All these are instances of one construction.

**Proposition 7.4 (the grading of the gadget of a monoid).** Let \(M\) be a finitely generated monoid. Then \(M\)
has finitely many prime ideals, and the groups \(G_{\mathfrak p}\) are finitely generated; let
\(r(\mathfrak p)\) be the rank of \(G_{\mathfrak p}\). Give the points of \(X_M(D)\) that belong to
\(\mathfrak p\) in Proposition 4.5(a) the degree \(r(\mathfrak p)\). This is a grading of \(X_M\). It is a counting
grading if and only if all groups \(G_{\mathfrak p}\) are torsion-free. In this case \(c_j\) is the number of prime
ideals with \(r(\mathfrak p)=j\), and \(X_M\) has the counting polynomial
\(N(x)=\sum_{\mathfrak p}(x-1)^{r(\mathfrak p)}\).

*Proof.* Let \(\Gamma\) be a finite generating set. A product of elements of \(\Gamma\) lies outside a prime ideal
\(\mathfrak p\) if and only if all its factors do. So \(\mathfrak p\) is determined by
\(\Gamma\cap\mathfrak p\), and \(G_{\mathfrak p}\) is generated by the fractions \(\gamma/1\) with
\(\gamma\in\Gamma\setminus\mathfrak p\). A homomorphism \(u:D\to D'\) does not change the prime ideal
\(x^{-1}(0)\) of a point \(x\), so the degrees are preserved. Write
\(G_{\mathfrak p}\cong\mathbb Z^{r(\mathfrak p)}\times F_{\mathfrak p}\) with \(F_{\mathfrak p}\) finite. Then
\(\#\operatorname{Hom}(G_{\mathfrak p},D)=|D|^{r(\mathfrak p)}\cdot\#\operatorname{Hom}(F_{\mathfrak p},D)\). If all
\(F_{\mathfrak p}\) are trivial, the grading is a counting grading with the stated constants. Conversely, suppose
that it is a counting grading with constants \(c_j\). For the trivial group we get
\(c_j=\#\{\mathfrak p:r(\mathfrak p)=j\}\). For a general \(D\) this gives
\(\sum_{r(\mathfrak p)=j}(\#\operatorname{Hom}(F_{\mathfrak p},D)-1)=0\), and all terms are non-negative. So
\(\operatorname{Hom}(F_{\mathfrak p},D)\) is trivial for all \(D\), and \(D=F_{\mathfrak p}\) shows that
\(F_{\mathfrak p}\) is trivial. \(\square\)

*Reference:* [Connes–Consani 2010, Definition 3.19 and Proposition 3.20].

For \(\mathbb A^F\) the prime ideals correspond to the subsets \(J\subseteq F\) of coordinates that are sent to
\(0\), and \(G_{\mathfrak p}\) is free of rank \(|F\setminus J|\). So the grading of Proposition 7.4 is the one of
Example 7.3.

### 7.2 Varieties over \(\mathbb F_{1^n}\)

Definitions 2.1 to 2.4 for the systems \(\beta_n\) and \(\beta_2^-\) give gadgets and affine varieties over
\(\mathbb F_{1^n}\). The test objects are the pairs \((D,\epsilon)\) with \(\epsilon\in D\) of order \(n\). For
\(\beta_n\) the extension of scalars is a variety over
\(R_n=\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z\). For \(\beta_2^-\) it is a variety over \(\mathbb Z\). The
scheme \(\operatorname{Spec}R_2\) is the union of two copies of \(\operatorname{Spec}\mathbb Z\), given by
\(T=1\) and \(T=-1\), and [Connes–Consani 2011a, §2.4] describes the reduced test rings as the restriction to the
copy \(T=-1\). Gradings and counting gradings are defined as in Definition 7.1, with
\(\#X^{(j)}(D,\epsilon)=c_j|D|^j\). For a counting grading we call \(N(x)=\sum_jc_j(x-1)^j\) the counting
polynomial; then \(\#X(D,\epsilon)=N(|D|+1)\) for all pairs \((D,\epsilon)\), as in Proposition 7.2.

**Proposition 7.5.** Let \(n\ge1\) and \(a,b\ge0\).

(a) Let \(m\) be a multiple of \(n\), \(\xi\) a generator of \(\mu_m\) and \(\epsilon_0=\xi^{m/n}\). The
representable gadget of \((\mu_m,\epsilon_0)\) over \(\beta_n\) is an affine variety over \(\mathbb F_{1^n}\). Its
points over \((D,\epsilon)\) are the \(g\in D\) with \(g^{m/n}=\epsilon\), and its extension of scalars is
\(\operatorname{Spec}R_m\), which is a scheme over \(R_n\) by \(T\mapsto T^{m/n}\).

(b) The gadget over \(\beta_n\) with the points \(D^a\times(D_0)^b\) over \((D,\epsilon)\), the algebra
\((R_n)_{\mathbb C}[T_1^{\pm1},\dots,T_a^{\pm1},S_1,\dots,S_b]\) and the evaluation \(f\mapsto f(g,h)\) is an affine
variety over \(\mathbb F_{1^n}\). Its extension of scalars is \(\mathbb G_m^a\times\mathbb A^b\) over \(R_n\).

(c) The gadget over \(\beta_2^-\) with the points \(D^a\times(D_0)^b\) over \((D,\epsilon)\), the algebra
\(\mathbb C[T_1^{\pm1},\dots,T_a^{\pm1},S_1,\dots,S_b]\) and the evaluation \(f\mapsto f(\bar g,\bar h)\) in
\(\mathbb Z[D,\epsilon]_{\mathbb C}\) is an affine variety over \(\mathbb F_{1^2}\) in the reduced sense. Its
extension of scalars is \(\mathbb G_m^a\times\mathbb A^b\) over \(\mathbb Z\).

*Proof.* (a) A morphism \((\mu_m,\epsilon_0)\to(D,\epsilon)\) is given by the image \(g\) of \(\xi\), which
satisfies \(g^{m/n}=\epsilon\); then \(g^m=\epsilon^n=1\). The test ring of \((\mu_m,\epsilon_0)\) is
\(\mathbb Z[\mu_m]=R_m\), which is finitely generated over \(R_n\). The sets of morphisms are finite, and a
morphism is determined by its homomorphism of group rings. So Proposition 4.1(c) applies. (b) Let
\(B=R_n[T_1^{\pm1},\dots,S_b]\) and \(W=\operatorname{Spec}B\). The gadget is an algebraic sub-gadget of
\(\mathcal G(W)\): a point \((g,h)\) gives the homomorphism of \(R_n\)-algebras \(B\to\mathbb Z[D]\) with
\(T_i\mapsto g_i\), \(S_j\mapsto h_j\). Let \(f=\sum_Ib_I\,T^{I'}S^{I''}\in B_{\mathbb C}\) be integral, with
\(b_I\in(R_n)_{\mathbb C}\). Choose \(N\) as in Lemma 3.8 for the exponents of \(f\), and let
\(D=\mu_n\times(\mu_N)^{a+b}\), with \(\epsilon\) a generator of the factor \(\mu_n\). Then
\(\mathbb Z[D]=R_n[(\mu_N)^{a+b}]\) as an \(R_n\)-algebra. Let \(x\) be the point whose coordinates are the
standard generators of \((\mu_N)^{a+b}\). Then \(f(x)=\sum_Ib_I\,\xi^I\) lies in \(R_n[(\mu_N)^{a+b}]\), and
Lemma 3.8 for \(A=R_n\) gives \(b_I\in R_n\). So \(f\in B\), and Corollary 3.5 applies. (c) The proof is the same
with \(D=\mu_2\times(\mu_N)^{a+b}\) and \(\epsilon\) the generator of \(\mu_2\). By Lemma 1.2(a), with the set of
representatives \((\mu_N)^{a+b}\), the ring \(\mathbb Z[D,\epsilon]\) is isomorphic to
\(\mathbb Z[(\mu_N)^{a+b}]\), and Lemma 3.8 is used for \(A=\mathbb Z\). The points are mapped injectively to
homomorphisms by Lemma 1.2(b).
\(\square\)

In particular \(\operatorname{Spec}\mathbb F_{1^m}\) is an affine variety over \(\mathbb F_{1^n}\) when \(n\)
divides \(m\). The gadgets of (c) carry the gradings of Example 7.3.

**Example 7.6 (a square root of \(-1\)).** Let \(X\) be the representable gadget of \((\mu_4,\epsilon_0)\) over
\(\beta_2^-\), where \(\epsilon_0\) is the element of order \(2\) of \(\mu_4\). Its points over \((D,\epsilon)\) are
the \(g\in D\) with \(g^2=\epsilon\). The test ring of \((\mu_4,\epsilon_0)\) is
\[
\mathbb Z[T]/(T^4-1,\,T^2+1)=\mathbb Z[T]/(T^2+1)=\mathbb Z[i].
\]
A morphism is determined by \(g\), and the induced homomorphism \(\mathbb Z[i]\to\mathbb Z[D,\epsilon]\) sends
\(i\) to \(\bar g\), which determines \(g\) by Lemma 1.2(b). By Proposition 4.1(c), \(X\) is an affine variety over
\(\mathbb F_{1^2}\) in the reduced sense, with extension of scalars \(\operatorname{Spec}\mathbb Z[i]\). By
Example 4.11 this scheme is not the extension of scalars of an affine variety over \(\mathbb F_1\). The element
\(\epsilon\), which becomes \(-1\), provides test rings without a homomorphism to \(\mathbb Z\). Over the pair
\((\mu_n,\epsilon)\), with \(n\) even, \(X\) has two points if \(4\) divides \(n\) and none otherwise, so it has no
counting polynomial.

## 8. Chevalley groups

[Soulé 1999, §5.5] proposes a functor for a Chevalley group scheme and leaves its universal property unchecked,
and [Soulé 2004, §5.4] asks whether the Chevalley group schemes can be defined over \(\mathbb F_1\).
[Connes–Consani 2011a, Theorem 4.10] answers that they are varieties over \(\mathbb F_{1^2}\). This
section states the theorem and proves it from five facts about Chevalley group schemes. Section 8.6 proves the
five facts from the course on reductive group schemes, and Section 8.4 checks them by hand for \(\mathrm{SL}_2\).
A reference for this section is [Connes–Consani 2011a, §4].

### 8.1 Root systems and the facts that are quoted

A *root system* \((L,\Phi,(n_r)_{r\in\Phi})\), in the form used in [Connes–Consani 2011a, §4.1], consists of a free
abelian group \(L\) of finite rank \(\ell\), a finite subset \(\Phi\subset L\) of *roots*, and a linear form
\(n_r:L\to\mathbb Z\) for every root \(r\), such that: \(L\otimes\mathbb Q\) is spanned by \(\Phi\) and the
intersection of the kernels of the \(n_r\); \(n_r(r)=2\); if \(r\) and \(ar\) are roots with \(a\in\mathbb Q\),
then \(a=\pm1\); and \(r-n_s(r)s\in\Phi\) for all roots \(r,s\). The reflection of a root is
\(s_r(x)=x-n_r(x)r\). Since \(n_r(r)=2\), we have \(s_r(s_r(x))=x\), so \(s_r\) is an automorphism of \(L\). The
reflections generate a group \(W\) of automorphisms of \(L\), the *Weyl group*. It is finite. Indeed, by the last
condition every reflection maps \(\Phi\) into itself, so \(W\) permutes the finite set \(\Phi\). Every reflection fixes
the elements of \(L\otimes\mathbb Q\) on which all the forms \(n_r\) vanish, and these elements together with
\(\Phi\) span \(L\otimes\mathbb Q\). So an element of \(W\) that fixes every root is the identity, and \(W\) embeds
into the group of permutations of \(\Phi\).

We fix a total order on \(L\) that is compatible with addition, and let \(\Phi^+\) be the set of positive roots;
then \(\Phi\) is the disjoint union of \(\Phi^+\) and \(-\Phi^+\). Put
\[
N=|\Phi^+|,\qquad\Phi_w=\{r\in\Phi^+:w(r)<0\},\qquad N(w)=|\Phi_w|\qquad(w\in W).
\]
There is exactly one \(w_0\in W\) with \(w_0(\Phi^+)=-\Phi^+\); thus \(\Phi_{w_0}=\Phi^+\). That \(w_0\) exists
and is unique is proved in Lemma 8.8(c).

To a root system [Connes–Consani 2011a, §4.3] associates a group scheme \(\mathfrak G\) over \(\mathbb Z\), the
*Chevalley group scheme*, with references to [Chevalley 1961] and [SGA3]; it is the pinned split reductive group
scheme over \(\mathbb Z\) with the root datum of the root system (Section 8.6). We write \(\mathbb G_a\) for the
additive group scheme. The lesson uses the following five facts. Proposition 8.9 in Section 8.6 proves them for
every root system, and Section 8.4 checks them by hand for \(\mathrm{SL}_2\).

**(C1)** \(\mathfrak G\) is an affine group scheme of finite type over \(\mathbb Z\). It contains the torus
\(\mathcal T=\operatorname{Spec}\mathbb Z[L]\) as a subgroup scheme, so
\(\mathcal T(A)=\operatorname{Hom}(L,A^\times)\) for every ring \(A\). For every root \(r\) there is a homomorphism
of group schemes \(x_r:\mathbb G_a\to\mathfrak G\) with \(h\,x_r(a)\,h^{-1}=x_r(h(r)a)\) for
\(h\in\mathcal T(A)\) and \(a\in A\).

**(C2)** The ring \(O(\mathfrak G)\) is torsion-free, and the rings \(O(\mathfrak G)\otimes\mathbb Q\) and
\(O(\mathfrak G)/pO(\mathfrak G)\), for every prime \(p\), are integral domains.

**(C3)** There are a subgroup \(\mathcal N(\mathbb Z)\) of \(\mathfrak G(\mathbb Z)\) and a surjective homomorphism
\(\mathcal N(\mathbb Z)\to W\) with kernel \(\mathcal T(\mathbb Z)=\operatorname{Hom}(L,\{\pm1\})\), such that for
every ring \(A\), every \(n\in\mathcal N(\mathbb Z)\) with image \(w\), and every \(h\in\mathcal T(A)\),
\[
n\,h\,n^{-1}=w\cdot h,\qquad\text{where }(w\cdot h)(l)=h(w^{-1}l).
\]

For the next two facts, the roots of \(\Phi^+\) are taken in increasing order for the total order of \(L\). For a
ring \(A\) and \(w\in W\) let
\[
\psi_w:A^{\Phi_w}\to\mathfrak G(A),\qquad(a_r)\mapsto\prod_{r\in\Phi_w}x_r(a_r),
\]
the product being taken in this order; put \(\psi=\psi_{w_0}:A^{\Phi^+}\to\mathfrak G(A)\). Choose for every
\(w\in W\) an element \(n_w\in\mathcal N(\mathbb Z)\) with image \(w\).

**(C4) (Bruhat decomposition.)** Let \(K\) be a field. Every \(g\in\mathfrak G(K)\) can be written as
\[
g=\psi(a)\,h\,n_w\,\psi_w(b)
\]
with exactly one \(w\in W\), \(a\in K^{\Phi^+}\), \(h\in\mathcal T(K)\) and \(b\in K^{\Phi_w}\).

**(C5) (The big cell.)** Put \(n_0=n_{w_0}\). The morphism
\[
\theta:\mathbb A^{\Phi^+}\times\mathcal T\times\mathbb A^{\Phi^+}\to\mathfrak G,\qquad
(a,h,b)\mapsto\psi(a)\,h\,n_0\,\psi(b),
\]
is an open immersion. Its image is the open subscheme
\(\operatorname{Spec}O(\mathfrak G)[d^{-1}]\) for a function \(d\in O(\mathfrak G)\) with \(d(n_0)=1\).

The facts (C1), (C3), (C4) and (C5) are stated in [Connes–Consani 2011a, §4.3, §4.4, Theorem 4.5, Lemmas 4.6
and 4.7, and Proposition 4.9]. Fact (C2) says that \(\mathfrak G\) is flat over
\(\mathbb Z\) and that its fibres over \(\mathbb Q\) and over the fields \(\mathbb F_p\) are integral schemes. It is
used in Lemma 8.2 below, and it is not stated in [Connes–Consani 2011a].

By (C4), \(\mathfrak G(\mathbb F_q)\) has
\[
N_{\mathfrak G}(q)=(q-1)^\ell\,q^N\sum_{w\in W}q^{N(w)}
\]
elements, because \(\mathcal T(\mathbb F_q)=\operatorname{Hom}(L,\mathbb F_q^\times)\) has \((q-1)^\ell\) elements.
This is the formula of [Connes–Consani 2011a, Introduction]. The exponent of \(q-1\) is \(\ell\), and
\(N_{\mathfrak G}(q)/(q-1)^\ell\) has the value \(|W|\) at \(q=1\). [Soulé 1999, §1] recalls this behaviour as the
background of the proposal of Tits to regard \(W\) as the group of points of \(\mathfrak G\) over
\(\mathbb F_1\); see *Counting over finite fields and the limit q → 1*.

### 8.2 The group of Tits and the gadget

Let \(D\) be an abelian group and \(\epsilon\in D\) an element with \(\epsilon^2=1\). Put
\(T_D=\operatorname{Hom}(L,D)\), with the action \((w\cdot t)(l)=t(w^{-1}l)\) of \(W\). The group
\(\mathcal N(\mathbb Z)\) acts on \(T_D\) through \(W\). Let
\(\iota:\mathcal T(\mathbb Z)=\operatorname{Hom}(L,\{\pm1\})\to T_D\) be the homomorphism induced by
\(-1\mapsto\epsilon\). Define
\[
\mathcal N_{D,\epsilon}=\big(T_D\rtimes\mathcal N(\mathbb Z)\big)\big/
\{(\iota(t_0)^{-1},t_0):t_0\in\mathcal T(\mathbb Z)\}.
\]
The set that is divided out is a normal subgroup, because \(\mathcal T(\mathbb Z)\) is normal in
\(\mathcal N(\mathbb Z)\) and acts trivially on \(T_D\), and \(\iota\) is compatible with the actions of
\(\mathcal N(\mathbb Z)\). The map \(t\mapsto(t,1)\) embeds \(T_D\) as a normal subgroup of
\(\mathcal N_{D,\epsilon}\), and the quotient is \(\mathcal N(\mathbb Z)/\mathcal T(\mathbb Z)=W\). So there is an
exact sequence
\[
1\to\operatorname{Hom}(L,D)\to\mathcal N_{D,\epsilon}\xrightarrow{\ p\ }W\to1,
\]
which is functorial in \((D,\epsilon)\). Every element of \(p^{-1}(w)\) is the class of \((t,n_w)\) for exactly
one \(t\in T_D\). For \(D=\{\pm1\}\) and \(\epsilon=-1\) we get
\(\mathcal N_{D,\epsilon}=\mathcal N(\mathbb Z)\).

This is the group \(\mathcal N_{D,\epsilon}(L,\Phi)\) that [Connes–Consani 2011a, §4.2] takes from [Tits 1966],
in the description as an amalgamated semi-direct product given in [Connes–Consani 2011a, §4.3].

Let \(A\) be a ring and \(\lambda:D\to A^\times\) a homomorphism with \(\lambda(\epsilon)=-1\). Then
\[
e_\lambda:\mathcal N_{D,\epsilon}\to\mathfrak G(A),\qquad\text{class of }(t,n)\mapsto(\lambda\circ t)\cdot n,
\]
is a well-defined homomorphism of groups. Here \(\lambda\circ t\in\operatorname{Hom}(L,A^\times)=\mathcal T(A)\),
and \(n\) is mapped to \(\mathfrak G(A)\). It is well defined because \(\lambda\circ\iota(t_0)=t_0\) in
\(\mathcal T(A)\), and it is a homomorphism by (C3).

**Definition 8.1 (the gadget of a Chevalley group).** Let \((D,\epsilon)\) be a pair of a finite abelian group and
an element of order \(2\). Put \(R=\mathbb Z[D,\epsilon]\) and \(\lambda(g)=\bar g\in R^\times\), so that
\(\lambda(\epsilon)=-1\). The gadget \(G\) over \(\beta_2^-\) has the points
\[
G(D,\epsilon)=(D_0)^{\Phi^+}\times\coprod_{w\in W}\big(p^{-1}(w)\times(D_0)^{\Phi_w}\big),
\]
the algebra \(O(\mathfrak G)_{\mathbb C}\), and the evaluation \(f(x)=i(x)_{\mathbb C}(f)\), where
\[
i(a,n,b)=\psi(\bar a)\;e_\lambda(n)\;\psi_w(\bar b)\ \in\ \mathfrak G(R)=\operatorname{Hom}(O(\mathfrak G),R)
\]
and \(\bar a\), \(\bar b\) are the images of \(a\), \(b\) in \(R^{\Phi^+}\), \(R^{\Phi_w}\). The *degree* of
\((a,n,b)\) is \(\ell\) plus the number of non-zero coordinates of \(a\) and \(b\).

*Reference:* [Connes–Consani 2011a, Definition 4.8 and §4.5]. There the functor is described on pairs with
\(\epsilon^2=1\); for \(\epsilon=1\) the ring \(\mathbb Z[D]/(1+\epsilon)\) has characteristic \(2\) and no
homomorphism to \(\mathbb C\), so as a gadget over \(\mathbb F_{1^2}\) it is defined on the pairs with
\(\epsilon\) of order \(2\), as in [Connes–Consani 2011a, §2.4].

The maps \(i\) are natural in \((D,\epsilon)\), so \(G\) is a gadget, and it is finite. The points of lowest degree
\(\ell\) are the points \((0,n,0)\); they form the group \(\mathcal N_{D,\epsilon}\).

**Lemma 8.2 (denominators).** Let \(O\) be a torsion-free ring and \(d\in O\). Suppose that \(d\) is a
non-zero-divisor in \(O\otimes\mathbb Q\) and in \(O/pO\) for every prime \(p\). If \(f\in O_{\mathbb C}\) and
\(d^mf\in O\) for some \(m\ge0\), then \(f\in O\).

*Proof.* Choose a basis \((c_\kappa)\) of \(\mathbb C\) as a vector space over \(\mathbb Q\) with one element
\(c_{\kappa_0}=1\). Then \(O_{\mathbb C}=(O\otimes\mathbb Q)\otimes_{\mathbb Q}\mathbb C\) is the direct sum of
the subgroups \((O\otimes\mathbb Q)c_\kappa\), and \(O\otimes\mathbb Q\) is the summand of \(\kappa_0\). Write
\(f=\sum_\kappa f_\kappa c_\kappa\) with \(f_\kappa\in O\otimes\mathbb Q\). Since
\(d^mf=\sum_\kappa(d^mf_\kappa)c_\kappa\) lies in \(O\), we get \(d^mf_\kappa=0\) for
\(\kappa\neq\kappa_0\), hence \(f_\kappa=0\), and \(f\in O\otimes\mathbb Q\). Let \(M\ge1\) be the smallest
integer with \(Mf\in O\). Suppose \(M>1\), let \(p\) be a prime factor of \(M\), and put \(b=Mf\). Then
\(d^mb=M\,d^mf\in pO\). Since \(d\) is a non-zero-divisor in \(O/pO\), we get \(b=pb'\) with \(b'\in O\). Then
\((M/p)f=b'\in O\), because \(O\otimes\mathbb Q\) is torsion-free. This contradicts the choice of \(M\). So
\(M=1\). \(\square\)

*Reference:* [Connes–Consani 2011a, proof of Theorem 4.10] uses the equality
\(O(\mathfrak G)_{\mathbb C}\cap O(\mathfrak G)[d^{-1}]=O(\mathfrak G)\) and states no condition at the primes. Such
a condition is needed: for \(O=\mathbb Z[x]\), \(d=2\) and \(f=x/2\) the corresponding equality
\(O_{\mathbb C}\cap O[d^{-1}]=O\) fails. So we prove the equality under the hypothesis of the lemma, which holds
for \(\mathfrak G\) by (C2) and \(d(n_0)=1\).

### 8.3 The theorem

**Theorem 8.3.** Let \(\mathfrak G\) be the Chevalley group scheme of a root system.

(a) The gadget \(G\) of Definition 8.1 is an affine variety over \(\mathbb F_{1^2}\) in the reduced sense. Its
extension of scalars is the Chevalley group scheme \(\mathfrak G\), with the immersion \(i\).

(b) The grading of \(G\) is a counting grading: \(\#G^{(j)}(D,\epsilon)=c_j|D|^j\), where
\(\sum_jc_jy^j=y^\ell(1+y)^N\sum_{w\in W}(1+y)^{N(w)}\). So
\(\#G(D,\epsilon)=N_{\mathfrak G}(|D|+1)\), and \(N_{\mathfrak G}(q)=\#\mathfrak G(\mathbb F_q)\) for every prime
power \(q\).

*Reference:* [Connes–Consani 2011a, Theorem 4.10] is (a); the count (b) is stated in
[Connes–Consani 2011a, Introduction]. The algebra of \(G\) is \(O(\mathfrak G)_{\mathbb C}\), so (a) holds for
both notions of immersion of Remark 2.5.

*Proof.* Put \(R=\mathbb Z[D,\epsilon]\). Recall that the characters in \(\widehat D_-\) are ring homomorphisms
\(R\to\mathbb C\).

*Step 1: \(i\) is injective.* Let \(x=(a,n,b)\) and \(x'=(a',n',b')\) be points of \(G(D,\epsilon)\) with
\(i(x)=i(x')\). Write \(n\) as the class of \((t,n_w)\) and \(n'\) as the class of \((t',n_{w'})\). Applying a
character \(\chi\in\widehat D_-\) to the equation \(i(x)=i(x')\) gives, in \(\mathfrak G(\mathbb C)\),
\[
\psi(\chi(a))\,(\chi\circ t)\,n_w\,\psi_w(\chi(b))=\psi(\chi(a'))\,(\chi\circ t')\,n_{w'}\,\psi_{w'}(\chi(b')).
\]
By (C4) for \(K=\mathbb C\) we get \(w=w'\), \(\chi(a)=\chi(a')\), \(\chi\circ t=\chi\circ t'\) and
\(\chi(b)=\chi(b')\), for every \(\chi\in\widehat D_-\). These characters separate the elements of \(D\)
(Lemma 1.2(d)), and they do not vanish on \(D\). So \(a=a'\), \(t=t'\) and \(b=b'\).

By Step 1 and (C2), \(G\) is a finite algebraic sub-gadget of \(\mathcal G(\mathfrak G)\) in the sense of
Corollary 3.5. So it remains to show that an integral function \(f\in O(\mathfrak G)_{\mathbb C}\) lies in
\(O(\mathfrak G)\).

*Step 2: coordinates on the big cell.* Choose a basis \(v_1,\dots,v_\ell\) of \(L\). By (C5), \(\theta\) induces an
isomorphism
\[
\theta^*:O(\mathfrak G)[d^{-1}]\longrightarrow
P:=\mathbb Z[a_r,\,u_1^{\pm1},\dots,u_\ell^{\pm1},\,b_r\;:\;r\in\Phi^+],
\]
where the \(a_r\) and \(b_r\) are the coordinates of the two factors \(\mathbb A^{\Phi^+}\) and \(u_j\) is the
function \(h\mapsto h(v_j)\) on \(\mathcal T\). Let \(F\in P_{\mathbb C}\) be the image of \(f\).

*Step 3: generic points.* Let \(k\ge1\), let \(D_1=(\mu_k)^{2N+\ell}\) with standard generators
\(\xi_r,\eta_j,\xi'_r\) (\(r\in\Phi^+\), \(1\le j\le\ell\)), and let \(D=D_1\times\mu_2\) with \(\epsilon\) the
generator of \(\mu_2\). By Lemma 1.2(a) the composite \(\mathbb Z[D_1]\to\mathbb Z[D]\to R\) is an isomorphism of
rings. Let \(x=(a,n,b)\) be the point of \(G(D,\epsilon)\) with \(a_r=\xi_r\), \(b_r=\xi'_r\), and \(n\) the class
of \((t,n_0)\) with \(t(v_j)=\eta_j\); recall that \(\Phi_{w_0}=\Phi^+\). Then
\[
i(x)=\psi(\xi)\,(\lambda\circ t)\,n_0\,\psi(\xi')=\theta(\xi,\lambda\circ t,\xi').
\]
So the homomorphism \(i(x):O(\mathfrak G)\to R\) factors through \(O(\mathfrak G)[d^{-1}]\), and it becomes, under
\(\theta^*\), the homomorphism \(P\to R\) with \(a_r\mapsto\xi_r\), \(u_j\mapsto\eta_j\), \(b_r\mapsto\xi'_r\).
Hence \(f(x)=F(\xi,\eta,\xi')\) in \(R_{\mathbb C}=\mathbb C[D_1]\). Since \(f\) is integral,
\(F(\xi,\eta,\xi')\in\mathbb Z[D_1]\). For \(k\) large enough, Lemma 3.8 shows that \(F\) has integer
coefficients, that is, \(F\in P\).

*Step 4: from the big cell to \(\mathfrak G\).* The element \(n_0\) is a ring homomorphism
\(O(\mathfrak G)\to\mathbb Z\) that sends \(d\) to \(1\). So \(d\) is not zero in the domains
\(O(\mathfrak G)\otimes\mathbb Q\) and \(O(\mathfrak G)/pO(\mathfrak G)\) of (C2), and it is a non-zero-divisor in
these rings, and also in \(O(\mathfrak G)_{\mathbb C}\), which is a direct sum of copies of
\(O(\mathfrak G)\otimes\mathbb Q\). By Step 3 the image of \(f\) in \(O(\mathfrak G)_{\mathbb C}[d^{-1}]\) lies in
\(O(\mathfrak G)[d^{-1}]\). So there are \(m\ge0\) and \(g\in O(\mathfrak G)\) with \(d^mf=g\) in
\(O(\mathfrak G)_{\mathbb C}\). By Lemma 8.2, \(f\in O(\mathfrak G)\). This proves (a).

(b) The fibre \(p^{-1}(w)\) has \(|D|^\ell\) elements. The number of points \((a,n,b)\) with \(p(n)=w\), with
\(j_1\) non-zero coordinates in \(a\) and \(j_2\) in \(b\), is
\(\binom N{j_1}|D|^{j_1}\cdot|D|^\ell\cdot\binom{N(w)}{j_2}|D|^{j_2}\). Summing over \(w\) gives the generating
polynomial, and its value at \(y=|D|\) is \(N_{\mathfrak G}(|D|+1)\). The last statement was shown in
Section 8.1. \(\square\)

The proof in [Connes–Consani 2011a, Theorem 4.10] computes the coefficients of \(F\) as limits, for
\(k\to\infty\), of averages over the points with coordinates in \(\mu_k\), as in Lemma 5.1. Since \(F\) is a
Laurent polynomial, one large \(k\) is enough.

The element \(\epsilon\) is not needed for the universal property.

**Proposition 8.4 (Chevalley groups over \(\mathbb F_1\)).** Let \(G^\flat\) be the gadget
over \(\mathbb F_1\) with the points
\[
G^\flat(D)=(D_0)^{\Phi^+}\times\coprod_{w\in W}\big(\operatorname{Hom}(L,D)\times(D_0)^{\Phi_w}\big),
\]
the algebra \(O(\mathfrak G)_{\mathbb C}\), and the evaluation through
\(i^\flat(a,t,b)=\psi(a)\,t\,n_w\,\psi_w(b)\in\mathfrak G(\mathbb Z[D])\), where \(t\) is regarded as an element
of \(\mathcal T(\mathbb Z[D])\). Then \(G^\flat\) is an affine variety over \(\mathbb F_1\) with extension of
scalars \(\mathfrak G\). With the degree defined as in Definition 8.1 it has a counting grading, and its counting
polynomial is \(N_{\mathfrak G}\).

*Proof.* The proof of Theorem 8.3 applies, with \(\mathbb Z[D]\) and Lemma 1.1 in place of \(R\) and Lemma 1.2,
and with \(D=D_1\) in Step 3. \(\square\)

*Reference:* [López Peña–Lorscheid 2011b, Theorem 2.10] states this for all affinely torified varieties. The
statement needs the fibres over all primes to be reduced, which holds for \(\mathfrak G\) by (C2); see *Torified
varieties and the limits of monoid schemes*.

The gadget \(G^\flat\) depends on the choice of the elements \(n_w\). What the quadratic extension adds is a group
structure in lowest degree.

**Proposition 8.5 (the role of \(\epsilon\)).**

(a) The map \(i\) of Definition 8.1 restricts to an injective homomorphism of groups
\(e_\lambda:\mathcal N_{D,\epsilon}\to\mathfrak G(\mathbb Z[D,\epsilon])\) on the points of degree \(\ell\), and
this homomorphism is natural in \((D,\epsilon)\).

(b) Let \(\mathfrak G=\mathrm{SL}_2\), with the notation of Section 8.4. For every choice of \(n_1\) and \(n_s\)
and every \(D\), the image under \(i^\flat\) of the points of degree \(1\) of \(G^\flat(D)\) is not closed under
multiplication in \(\mathrm{SL}_2(\mathbb Z[D])\).

*Proof.* (a) follows from the construction of \(e_\lambda\) and Step 1 of the proof of Theorem 8.3. (b) Here
\(n_1=\pm1\) and \(n_s=\pm\sigma\), and the image consists of the matrices \(h(t)n_1\) and \(h(t)n_s\) with
\(t\in D\). If \(n_1=1\), the square of \(n_s\) is \(-1=h(-1)\), which is not of the form \(h(t)\) or
\(h(t)n_s\) with \(t\in D\), because \(-1\notin D\). If \(n_1=-1\), the square of \(n_1\) is \(1=-h(-1)\), which
is not of the form \(-h(t)\) or \(h(t)n_s\) with \(t\in D\). \(\square\)

*Reference:* [Connes–Consani 2011a, §5] for (a). [López Peña–Lorscheid 2011b, §6.1] shows for \(\mathrm{SL}_2\)
that the gadget of \(\mathcal N\) over \(\mathbb F_1\) has no multiplication that is a morphism of gadgets.

So the theorem realizes \(\mathfrak G\) over \(\mathbb F_{1^2}\) as a variety, and the normalizer of the torus as a
group. It does not realize the group law of \(\mathfrak G\): [Connes–Consani 2011a, §5] states that the group
operation is not shown to be defined over \(\mathbb F_{1^2}\). The lessons *Torified varieties and the limits of
monoid schemes* and *Blueprints and blue schemes* return to this problem.

### 8.4 The group \(\mathrm{SL}_2\)

Let \(\mathfrak G=\mathrm{SL}_2=\operatorname{Spec}O\) with
\[
O=\mathbb Z[x_{11},x_{12},x_{21},x_{22}]/(x_{11}x_{22}-x_{12}x_{21}-1).
\]
The root system is \(L=\mathbb Z\), \(\Phi=\{\alpha,-\alpha\}\) with \(\alpha=2\), and
\(n_{\pm\alpha}(l)=\pm l\). Then \(W=\{1,s\}\) with \(s(l)=-l\), \(\ell=1\), \(\Phi^+=\{\alpha\}\), \(N=1\),
\(\Phi_1=\emptyset\), \(\Phi_s=\{\alpha\}\) and \(w_0=s\). Put
\[
h(t)=\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix},\quad
x_\alpha(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\quad
x_{-\alpha}(a)=\begin{pmatrix}1&0\\a&1\end{pmatrix},\quad
\sigma=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The torus \(\mathcal T\) consists of the matrices \(h(t)\); the element \(h(t)\) corresponds to the homomorphism
\(l\mapsto t^l\) in \(\operatorname{Hom}(L,A^\times)\). Let \(\mathcal N(\mathbb Z)=\{\pm1,\pm\sigma\}\), with
\(\pm1\mapsto1\) and \(\pm\sigma\mapsto s\). Take \(n_1=1\) and \(n_s=n_0=\sigma\).

**Proposition 8.6.** For \(\mathrm{SL}_2\) with these data, the facts (C1) to (C5) hold. This is the case of
\(\mathrm{SL}_2\) of Proposition 8.9 below, checked here by direct computation.

*Proof.* (C1) The torus is the closed subscheme \(x_{12}=x_{21}=0\), and it is isomorphic to
\(\operatorname{Spec}\mathbb Z[t,t^{-1}]\). A computation gives \(h(t)x_{\pm\alpha}(a)h(t)^{-1}=x_{\pm\alpha}(t^{\pm2}a)\),
and \(h(t)\) takes the value \(t^{\pm2}\) at \(\pm\alpha=\pm2\).

(C2) Let \(K\) be a field. The polynomial \(x_{11}x_{22}-x_{12}x_{21}-1\) has degree one in \(x_{11}\), and its
coefficients \(x_{22}\) and \(-(x_{12}x_{21}+1)\) have no common factor in \(K[x_{12},x_{21},x_{22}]\). So it is
irreducible in \(K[x_{11},x_{12},x_{21},x_{22}]\), and \(O\otimes K\) is an integral domain. This applies to
\(K=\mathbb Q\) and \(K=\mathbb F_p\). To see that \(O\) is torsion-free, let \(pg=Fh\) in
\(\mathbb Z[x_{11},\dots,x_{22}]\), where \(F\) is the defining polynomial. Modulo \(p\) we get
\(\bar F\bar h=0\) in a domain, and \(\bar F\neq0\), so \(p\) divides \(h\), and \(g\) is a multiple of \(F\).

(C3) \(\sigma^2=-1\), so \(\mathcal N(\mathbb Z)\) is a cyclic group of order \(4\) and the map to \(W\) is a
surjective homomorphism with kernel \(\{\pm1\}=\mathcal T(\mathbb Z)\). Further
\(\sigma h(t)\sigma^{-1}=h(t^{-1})=s\cdot h(t)\), and \(\pm1\) is central.

(C5) For a ring \(A\) and \((a,t,b)\in A\times A^\times\times A\),
\[
\theta(a,t,b)=x_\alpha(a)\,h(t)\,\sigma\,x_\alpha(b)=
\begin{pmatrix}-at^{-1}&t-at^{-1}b\\-t^{-1}&-t^{-1}b\end{pmatrix}.
\]
Its entry \(x_{21}=-t^{-1}\) is a unit. Conversely, let \(g\in\mathrm{SL}_2(A)\) have entries \(g_{ij}\) with
\(g_{21}\in A^\times\). Then \(g=\theta(a,t,b)\) holds exactly for \(t=-g_{21}^{-1}\), \(a=g_{11}g_{21}^{-1}\),
\(b=g_{22}g_{21}^{-1}\): these values are forced by three of the entries, and the fourth entry agrees because
\(t-at^{-1}b=(g_{11}g_{22}-1)g_{21}^{-1}=g_{12}\). So \(\theta\) is an isomorphism of
\(\mathbb A^1\times\mathbb G_m\times\mathbb A^1\) onto the open subscheme of \(\mathrm{SL}_2\) where
\(d=-x_{21}\) is invertible, and \(d(\sigma)=1\).

(C4) Let \(K\) be a field and \(g\in\mathrm{SL}_2(K)\). If \(g_{21}\neq0\), then \(g=\theta(a,t,b)=
\psi(a)h(t)n_s\psi_s(b)\) for exactly one \((a,t,b)\), by the computation for (C5). If \(g_{21}=0\), then
\(g_{22}=g_{11}^{-1}\), and \(g=x_\alpha(a)h(t)=\psi(a)h(t)n_1\) exactly for \(t=g_{11}\) and
\(a=g_{12}g_{11}\), because
\(x_\alpha(a)h(t)=\begin{pmatrix}t&at^{-1}\\0&t^{-1}\end{pmatrix}\). The two cases exclude each other. \(\square\)

For \(\mathrm{SL}_2\) the objects of Section 8.2 are explicit. The group \(\mathcal N_{D,\epsilon}\) is the union
of \(D\) and \(D\bar\sigma\), with \(\bar\sigma^2=\epsilon\) and \(\bar\sigma t\bar\sigma^{-1}=t^{-1}\). The
points of the gadget and their images in \(\mathrm{SL}_2(\mathbb Z[D,\epsilon])\) are
\[
(a,t)\mapsto\begin{pmatrix}t&at^{-1}\\0&t^{-1}\end{pmatrix},\qquad
(a,t\bar\sigma,b)\mapsto\begin{pmatrix}-at^{-1}&t-at^{-1}b\\-t^{-1}&-t^{-1}b\end{pmatrix},
\]
with \(a,b\in D_0\) and \(t\in D\), where the bars on the right are omitted. With \(m=|D|\) there are \(2m\) points
of degree \(1\), \(3m^2\) of degree \(2\) and \(m^3\) of degree \(3\), in agreement with
\(y(1+y)(2+y)=2y+3y^2+y^3\). The counting polynomial is \(N_{\mathfrak G}(x)=(x-1)x(x+1)=x^3-x\), the number of
elements of \(\mathrm{SL}_2(\mathbb F_q)\) at \(x=q\), and
\[
\zeta_{\mathrm{SL}_2}(s)=\frac{s-1}{s-3}.
\]
The coefficient \(c_1=2\) is the order of the Weyl group. Exercise 5 treats the pair \((\mu_2,\epsilon)\), which
corresponds to the field \(\mathbb F_3\).

### 8.5 Points with values in a field

**Proposition 8.7.** Let \(K\) be a field and \(p:\mathcal N_{K^\times,-1}\to W\) the
projection for the pair \((K^\times,-1)\). Then the map
\[
K^{\Phi^+}\times\coprod_{w\in W}\big(p^{-1}(w)\times K^{\Phi_w}\big)\longrightarrow\mathfrak G(K),\qquad
(a,n,b)\mapsto\psi(a)\,e_{\mathrm{id}}(n)\,\psi_w(b),
\]
is a bijection.

*Proof.* Every element of \(p^{-1}(w)\) is the class of \((t,n_w)\) for exactly one
\(t\in\operatorname{Hom}(L,K^\times)=\mathcal T(K)\), and \(e_{\mathrm{id}}\) maps it to \(t\,n_w\). So the map is
\((a,t,b)\mapsto\psi(a)\,t\,n_w\,\psi_w(b)\), which is bijective by (C4). \(\square\)

*Reference:* [Connes–Consani 2011a, Theorem 5.1].

The left-hand side is given by the formula of Definition 8.1, with the monoid \(D_0\) replaced by the
multiplicative monoid of \(K\) and \(\epsilon\) by \(-1\). [Connes–Consani 2011a, Theorem 5.1] states more: the
functor \(G\) extends to the pairs \((M,\epsilon)\) of a monoid and an element with \(\epsilon^2=1\), and for every
ring \(A\) there is a map \(G(A,-1)\to\mathfrak G(A)\), which is bijective if \(A\) is a field. This is the model
for the \(\mathbb F_1\)-schemes of the next section, in which the number of points is controlled.

### 8.6 Proof of the five facts

This section proves (C1) to (C5) for every root system, using the course on reductive group schemes. Fix a root
system \((L,\Phi,(n_r))\) as in Section 8.1, with its total order on \(L\) and its positive roots \(\Phi^+\).

**Lemma 8.8 (root data, positive systems and the longest element).**

(a) There is a linear form \(f:L\otimes\mathbb R\to\mathbb R\) with \(f(r)>0\) for every \(r\in\Phi^+\).

(b) Put \(L^\vee=\operatorname{Hom}(L,\mathbb Z)\) and take \(n_r\) as the coroot of \(r\). Then
\((L,\Phi,L^\vee,\{n_r\})\) is a reduced root datum, its Weyl group is the group \(W\) of Section 8.1, and
\(\Phi^+\) is a positive system of it.

(c) There is exactly one \(w_0\in W\) with \(w_0(\Phi^+)=-\Phi^+\). For every \(w\in W\), the number \(N(w)\) is the
length of \(w\) for the simple reflections of \(\Phi^+\).

*Proof.* If \(\Phi=\varnothing\), take \(f=0\). Part (a) is vacuous; the empty root and coroot sets give the torus root datum in (b), and the group generated by no reflections is \(W=\{1\}\). Thus \(w_0=1\), and its length and \(N(1)\) are zero, proving (c). Assume from now on that \(\Phi\ne\varnothing\). (a) Choose an inner product on \(L\otimes\mathbb R\), and let \(C\) be the convex hull of \(\Phi^+\).
Suppose \(0\in C\). The set of \((c_r)\in\mathbb R^{\Phi^+}\) with \(c_r\ge0\), \(\sum_rc_r=1\) and
\(\sum_rc_rr=0\) is then a nonempty bounded polyhedron defined by linear equations and inequalities with rational
coefficients. Its vertices are the unique solutions of rational linear systems, so it has a rational point.
Clearing denominators gives integers \(m_r\ge0\), not all zero, with \(\sum_rm_rr=0\). This contradicts the
compatibility of the order with addition, by which a sum of positive elements is positive. So \(0\notin C\). Let
\(x\) be the point of the compact convex set \(C\) nearest to \(0\). For \(y\in C\) and \(0<\lambda\le1\), the point
\(x+\lambda(y-x)\) lies in \(C\), so \(|x+\lambda(y-x)|^2\ge|x|^2\); dividing by \(\lambda\) and letting
\(\lambda\to0\) gives \((x,y-x)\ge0\). Hence \(f=(x,\cdot)\) satisfies \(f(y)\ge|x|^2>0\) on \(C\).

(b) Section 8.1 shows that the reflections \(s_r(x)=x-n_r(x)r\) permute \(\Phi\) and generate the finite group
\(W\). Average an inner product on \(L\otimes\mathbb R\) over \(W\). Each \(s_r\) is then an orthogonal reflection:
its \((-1)\)-eigenspace is \(\mathbb Rr\) and its \((+1)\)-eigenspace is \(\ker n_r\), and these are orthogonal.
Hence
\[
n_r(x)=\frac{2(x,r)}{(r,r)},\qquad n_{w(r)}(w(x))=n_r(x)\qquad(x\in L\otimes\mathbb R,\ w\in W).
\]
The map \(r\mapsto n_r\) is injective: if \(n_r=n_s\), the formula makes \(r\) and \(s\) proportional, and then
\(r=s\). The pairing between \(L\) and \(L^\vee\) is perfect, and \(n_r(r)=2\). The dual reflection
\(s_r^\vee(y)=y-y(r)n_r\) satisfies \(s_r^\vee(n_s)(x)=n_s(s_r(x))=n_{s_r(s)}(x)\), so it permutes the coroots, and
\(r\mapsto n_r\) is compatible with the reflections. The axiom that only \(\pm r\) are roots proportional to \(r\) is
reducedness. These are the axioms of a reduced root datum in
Root data, Weyl chambers and the Bruhat decomposition, Section 1, and its Weyl group,
generated by the \(s_r\), is \(W\). By (a), \(\Phi^+=\{r\in\Phi:f(r)>0\}\) and \(-\Phi^+=\{r\in\Phi:f(r)<0\}\), since
\(f\) is nonzero on every root; so \(\Phi^+\) is a positive system.

(c) By Pinnings and the classification of split reductive groups, Theorem 10.1, the datum
of (b) is the datum of a split reductive group over \(\mathbb Q\). By
Root data, Weyl chambers and the Bruhat decomposition, Theorem 4.1, its Weyl group \(W\)
acts simply transitively on the positive systems. Since \(-\Phi^+\) is a positive system (for \(-f\)), there is
exactly one \(w_0\) with \(w_0(\Phi^+)=-\Phi^+\). By Proposition 3.1 there, the length of \(w\) is the number of
\(r\in\Phi^+\) with \(w^{-1}(r)<0\). The map \(r\mapsto-w^{-1}(r)\) is a bijection from that set onto \(\Phi_w\), so
the length of \(w\) is \(N(w)\). \(\square\)

From now on \(\mathfrak G\) is the pinned split reductive group scheme over \(\mathbb Z\) with the root datum of
Lemma 8.8 and the positive system \(\Phi^+\). It exists, and is unique up to a unique isomorphism preserving the
pinnings, by Pinnings and the classification of split reductive groups, Theorems 10.1 and 5.1.
This is the group scheme that [Connes–Consani 2011a, §4.3] attaches to the root system. Its root homomorphisms
\(x_r\) are the parametrizations of the root groups of
Roots and reductive groups of rank one, Theorem 4.1, normalized by the pinning.

**Proposition 8.9 (the five facts).** The group scheme \(\mathfrak G\) satisfies (C1) to (C5), with
\(\mathcal N(\mathbb Z)=N_{\mathfrak G}(\mathcal T)(\mathbb Z)\).

*Proof.* (C1) A reductive group scheme is affine and of finite presentation, hence of finite type over
\(\mathbb Z\). Its split torus is \(\mathcal T=\operatorname{Spec}\mathbb Z[L]\). A ring homomorphism
\(\mathbb Z[L]\to A\) sends each basis element \(e^l\) to a unit, because \(e^le^{-l}=1\), and multiplicativity says
that these values form a homomorphism \(L\to A^\times\); conversely such a homomorphism extends linearly. Hence
\(\mathcal T(A)=\operatorname{Hom}(L,A^\times)\). The root parametrizations are \(\mathcal T\)-equivariant:
conjugation by \(h\) scales the root group of \(r\) by the character \(r\), which in the parameter reads
\(h\,x_r(a)\,h^{-1}=x_r(h(r)a)\) for every ring \(A\).

(C2) A reductive group scheme is smooth over \(\mathbb Z\), so it is flat, and \(O(\mathfrak G)\) is a flat, hence
torsion-free, \(\mathbb Z\)-module. Let \(K\) be \(\mathbb Q\) or \(\mathbb F_p\). The fibre \(\mathfrak G_K\) is
smooth of finite type over \(K\), so its local rings are regular, hence domains, and \(\mathfrak G_K\) is reduced.
Its coordinate ring is Noetherian and has finitely many minimal primes. Two distinct irreducible components cannot
meet: at a common point their minimal primes would give two minimal primes of a local ring that is a domain. So the
components are disjoint, open and closed. The geometric fibres of a reductive group scheme are connected, and a
nontrivial idempotent of \(O(\mathfrak G_K)\) would stay nontrivial over an algebraic closure. So \(\mathfrak G_K\)
is connected, it has one component, and it is integral. Thus \(O(\mathfrak G)\otimes\mathbb Q\) and
\(O(\mathfrak G)/pO(\mathfrak G)\) are integral domains.

(C3) This is Pinnings and the classification of split reductive groups, Proposition 1.1,
applied to \(\mathfrak G\) with \(X=L\) and \(\mathcal N=N_{\mathfrak G}(\mathcal T)\): the sequence
\(1\to\operatorname{Hom}(L,\{\pm1\})\to\mathcal N(\mathbb Z)\to W\to1\) is exact, so the kernel of the
surjection \(\mathcal N(\mathbb Z)\to W\) is \(\mathcal T(\mathbb Z)=\operatorname{Hom}(L,\mathbb Z^\times)
=\operatorname{Hom}(L,\{\pm1\})\), and an element \(n\in\mathcal N(\mathbb Z)\) above \(w\) acts on
\(\mathcal T(A)\), for every ring \(A\), by \((n\,h\,n^{-1})(l)=h(w^{-1}l)\). This is the formula of (C3). The
chosen representatives \(n_w\) need not form a subgroup; for \(\mathrm{SL}_2\) this is visible in Proposition 8.6.

(C4) Let \(K\) be a field. By *Counting over finite fields and the limit q → 1*, Theorem 6.4, applied to
\(\mathfrak G\), every \(g\in\mathfrak G(K)\) is \(u\,h\,n_w\,u'\) for exactly one \(w\in W\) and exactly one triple
with \(u\in\mathcal U(K)\), \(h\in\mathcal T(K)\), \(u'\in\mathcal U_w(K)\). By
Root data, Weyl chambers and the Bruhat decomposition, Section 5, the ordered products
\(\psi:K^{\Phi^+}\to\mathcal U(K)\) and \(\psi_w:K^{\Phi_w}\to\mathcal U_w(K)\) are bijections; \(\Phi_w\) is closed
under addition within \(\Phi^+\), since a root that is a sum of roots made negative by \(w\) is made negative by
\(w\). This is (C4).

(C5) By Root data, Weyl chambers and the Bruhat decomposition, Proposition 8.2, there
is a function \(d\in O(\mathfrak G)\) with \(d(n_0)=1\) such that \((a,h,b)\mapsto\psi'(a)\,h\,n_0\,\psi'(b)\) is
an isomorphism of \(\mathbb A^{\Phi^+}\times\mathcal T\times\mathbb A^{\Phi^+}\) onto the principal open subscheme
\(D(d)=\operatorname{Spec}O(\mathfrak G)[d^{-1}]\), where \(\psi'\) is the ordered product of positive root
groups used there. The function is \(d(g)=\varepsilon\,\varphi_-\bigl((\bigwedge^N\operatorname{Ad})(g)v_+\bigr)\),
where \(v_\pm\) are the wedges of the positive and the negative root vectors and \(\varepsilon=\pm1\) normalizes
\(d(n_0)=1\). The statement holds for every reduced root datum and after every base change. By the ordered
root-product theorem of Root data, Weyl chambers and the Bruhat decomposition, Section 5,
both \(\psi\) and \(\psi'\) are isomorphisms of \(\mathbb A^{\Phi^+}\) onto \(\mathcal U\), so
\(\alpha=\psi'^{-1}\circ\psi\) is an automorphism of the scheme \(\mathbb A^{\Phi^+}\). Then \(\theta\) is the
isomorphism above composed with \(\alpha\times\mathrm{id}\times\alpha\). So \(\theta\) is an open immersion with
image \(D(d)\). \(\square\)

For \(\mathrm{PGL}_2\), with \(n_0\) the class of \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), the
function is \(d\bigl[\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)\bigr]=c^2/(ae-bc)\). So (C5) holds
also when the Picard group of \(\mathfrak G\) is not trivial; the construction needs only the weight \(\eta\), which
lies in the root lattice.

## 9. \(\mathbb F_1\)-schemes and their counting functions

The gadgets \(X_M\) of Section 4.2 and the gadget of a Chevalley group in Section 8 have more structure than
Definition 2.4 asks for. Their points are the values, on the monoids \(D_0\), of a functor that is defined on all
monoids, or on all pairs \((M,\epsilon)\) in the case of Section 8.5, and over a field these values are exactly the
points of the extension of scalars (Propositions 4.5(b) and 8.7). The gadget \(X'\) of Example 4.8 does not have
this property: it has \(q-1\) points over \(\mathbb F_{1^{q-1}}\), and its extension of scalars has \(q\) points
over \(\mathbb F_q\). [Connes–Consani 2011a, §5] and [Connes–Consani 2010] make this the definition
of a scheme over \(\mathbb F_1\). A reference for this section is [Connes–Consani 2010, §3–4].

### 9.1 The points of a monoid scheme

A *monoid scheme* is a topological space \(X\) with a sheaf of monoids \(\mathcal O_X\) that is locally isomorphic
to the spectrum of a monoid with its structure sheaf; see *Monoid schemes*. [Connes–Consani 2010] calls these
objects geometric \(\mathfrak{Mo}\)-schemes, a name that is also written \(\mathcal M_0\)-schemes, and
[Deitmar 2006] calls them schemes over \(\mathbb F_1\). In [Deitmar 2006] a monoid need not have a zero; its monoid
\(A\) corresponds to the monoid \(A_0\) here, and its statements on the points with values in the monoids \(D_0\)
translate directly. We recall what is needed. The spectrum \(\operatorname{Spec}M\) is the set of prime
ideals of \(M\), with the topology generated by the sets \(D(f)=\{\mathfrak p:f\notin\mathfrak p\}\), and the stalk
of its structure sheaf at \(\mathfrak p\) is \(M_{\mathfrak p}\). A morphism of monoid schemes \(X\to Y\) is a
continuous map \(\varphi\) with a morphism of sheaves of monoids \(\mathcal O_Y\to\varphi_*\mathcal O_X\) such that
the maps on stalks \(\mathcal O_{Y,\varphi(x)}\to\mathcal O_{X,x}\) are *local*: they map non-units to non-units.
For a monoid \(M\) we write \(X(M)\) for the set of morphisms \(\operatorname{Spec}M\to X\). For an abelian group
\(H\), the monoid \(H_0\) has the single prime ideal \(\{0\}\), so \(\operatorname{Spec}H_0\) is a point with the
stalk \(H_0\).

**Proposition 9.1.** Let \(X\) be a monoid scheme and \(H\) an abelian group. Then \(X(H_0)\) is the disjoint
union of the sets \(\operatorname{Hom}(\mathcal O_{X,x}^\times,H)\) of group homomorphisms, over the points
\(x\in X\).

*Proof.* A morphism \(\operatorname{Spec}H_0\to X\) consists of a point \(x\), the image of the unique point, and
of a morphism of monoids \(\mathcal O_{X,x}\to H_0\) that is local. A local morphism sends the non-units to
non-units, that is, to \(0\), and the units to units. So it is determined by its restriction
\(\rho:\mathcal O_{X,x}^\times\to H\). Conversely, for \(x\) and a homomorphism \(\rho\), the map that is \(\rho\)
on the units and \(0\) on the non-units is a morphism of monoids, because a product in a monoid is a unit only if
both factors are units, and it is local. \(\square\)

*Reference:* [Connes–Consani 2010, Proposition 3.18]; [Deitmar 2006, proof of Theorem 1];
[Deitmar–Koyama–Kurokawa 2008, Lemma 1.3].

For \(X=\operatorname{Spec}M\) this is Proposition 4.5(a), because \(\mathcal O_{X,\mathfrak p}^\times=G_{\mathfrak p}\).

**Definition 9.2.** A monoid scheme \(X\) is *of finite type* if it has a finite cover by open subschemes
\(\operatorname{Spec}M_i\) with \(M_i\) finitely generated. Then \(X\) is a finite set and every group
\(\mathcal O_{X,x}^\times\) is finitely generated (proof of Proposition 7.4), so
\(\mathcal O_{X,x}^\times\cong\mathbb Z^{n(x)}\times F_x\) with \(F_x\) finite. The number \(n(x)\) is the *local
dimension* of \(X\) at \(x\). The scheme \(X\) is *torsion free* if all groups \(F_x\) are trivial. The *exponent*
\(e(X)\) is the least common multiple of the exponents of the groups \(F_x\).

*Reference:* [Connes–Consani 2010, Definitions 3.19 and 4.9], where these schemes are called Noetherian: a monoid
is called Noetherian there if every strictly increasing sequence of congruences is finite, and
[Connes–Consani 2010, §4.4] quotes that this holds exactly for the finitely generated monoids.
[Deitmar 2006, §2] defines an exponent with the group of fractions of each stalk in place of its group of units.
The two numbers are equal if all stalks are cancellative; *Monoid schemes* has an example in which they differ.

**Theorem 9.3 (counting).** Let \(X\) be a monoid scheme of finite type, with exponent \(e\), and put
\[
N_X(y)=\sum_{x\in X}(y-1)^{n(x)} .
\]

(a) For every finite abelian group \(H\),
\(\#X(H_0)=\sum_{x\in X}|H|^{n(x)}\cdot\#\operatorname{Hom}(F_x,H)\).

(b) If \(n\) is prime to \(e\), then \(\#X(\mathbb F_{1^n})=N_X(n+1)\). The polynomial \(N_X\) is the only
polynomial with this property.

(c) The function \(n\mapsto\#X(\mathbb F_{1^n})\) is given by a polynomial in \(n\), for all \(n\ge1\), if and only
if \(X\) is torsion free. In this case the polynomial is \(N_X(n+1)=\sum_xn^{n(x)}\), whose coefficients are
non-negative integers.

(d) \(\zeta_{N_X}(s)=\prod_{x\in X}\zeta_{(y-1)^{n(x)}}(s)\), with the factors given by Proposition 6.4(f).

(e) Let \(X_{\mathbb Z}\) be a scheme such that \(X((K,\cdot))\) and \(X_{\mathbb Z}(K)\) are in bijection for
every finite field \(K\). Then \(\#X_{\mathbb Z}(\mathbb F_q)=N_X(q)\) for every prime power \(q\) with \(q-1\)
prime to \(e\), and for every prime power \(q\) if \(X\) is torsion free.

*Proof.* (a) follows from Proposition 9.1 and
\(\operatorname{Hom}(\mathbb Z^n\times F,H)=H^n\times\operatorname{Hom}(F,H)\). (b) If \(|H|\) is prime to \(e\),
every homomorphism \(F_x\to H\) is trivial, because the order of the image of an element divides \(e\) and
\(|H|\). So (a) for \(H=\mu_n\) gives \(\sum_xn^{n(x)}=N_X(n+1)\). There are infinitely many \(n\) prime to \(e\),
so \(N_X\) is determined. (c) If \(X\) is torsion free, then \(e=1\) and (b) applies to all \(n\). Conversely, let
\(P\) be a polynomial with \(\#X(\mathbb F_{1^n})=P(n)\) for all \(n\). By (b), \(P(n)=\sum_xn^{n(x)}\) for all
\(n\equiv1\) modulo \(e\), so \(P(y)=\sum_xy^{n(x)}\). If \(e\) divides \(n\), every homomorphism from \(F_x\) to
the roots of unity has values in \(\mu_n\), so \(\#\operatorname{Hom}(F_x,\mu_n)=|F_x|\), and (a) gives
\(P(n)=\sum_x|F_x|\,n^{n(x)}\) for these \(n\). Hence \(\sum_x(|F_x|-1)y^{n(x)}=0\). All coefficients are
non-negative, so every \(F_x\) is trivial. (d) is Proposition 6.4(a). (e) We have \((K,\cdot)=(K^\times)_0\), and
\(\mathbb F_q^\times\cong\mu_{q-1}\). Now apply (b) and (c). \(\square\)

*Reference:* [Connes–Consani 2010, Theorem 4.10] states (c), (d) and (e) for torsion free \(X\), without the
converse in (c). [Deitmar 2006, Theorem 1] states (e) in general, for the base change of \(X\), and calls \(N_X\)
the zeta-polynomial.

**Example 9.4.**

- The affine line \(\operatorname{Spec}\mathbb F_1[T]\), where \(\mathbb F_1[T]=\{0,1,T,T^2,\dots\}\), has two
  points, \(\{0\}\) and \(\{0,T,T^2,\dots\}\), with local dimensions \(1\) and \(0\). So \(N_X(y)=(y-1)+1=y\).
- The projective line, glued from \(\operatorname{Spec}\mathbb F_1[T]\) and
  \(\operatorname{Spec}\mathbb F_1[T^{-1}]\) along \(\operatorname{Spec}\mathbb F_1[T,T^{-1}]\), has three points,
  with local dimensions \(0,1,0\). So \(N_X(y)=y+1\) and
  \(\zeta_{N_X}(s)=\frac1s\cdot\frac s{s-1}\cdot\frac1s=\frac1{s(s-1)}\), as in [Connes–Consani 2010, §4.4].
- \(\operatorname{Spec}\mathbb F_{1^m}\) is a point with group of units \(\mu_m\). So \(N_X=1\), \(e=m\) and
  \(\#X(\mathbb F_{1^n})=\gcd(m,n)\). The zeta function \(1/s\) does not see the torsion. For \(m\ge2\) the
  function \(\gcd(m,n)\) is not a polynomial in \(n\), in agreement with (c). The scheme
  \(\operatorname{Spec}\mathbb Z[T]/(T^m-1)\) has \(\gcd(m,q-1)\) points over \(\mathbb F_q\). So the value
  \(N_X(q)=1\) is the number of points over \(\mathbb F_q\) only when \(q-1\) is prime to \(m\), as in (e).
- For \(M=\{0,1,a\}\) with \(a^2=0\), the only prime ideal is \(\{0,a\}\), and \(N_X=1\). Indeed
  \(\mathbb Z[a]/(a^2)\) has one homomorphism to every field. So the counting theorem applies to this monoid,
  although \(X_M\) is not an affine variety over \(\mathbb F_1\) (Example 4.10).

### 9.2 \(\mathbb F_1\)-schemes

[Connes–Consani 2010, §3] treats monoid schemes as functors. An *\(\mathfrak{Mo}\)-functor* is a functor from the
category of monoids to sets, and an *\(\mathfrak{Mo}\)-scheme* is an \(\mathfrak{Mo}\)-functor that has an open
cover by representable subfunctors [Connes–Consani 2010, Definitions 3.1 and 3.9]. By
[Connes–Consani 2010, Proposition 3.16], every \(\mathfrak{Mo}\)-scheme is the functor \(M\mapsto X(M)\) of a
monoid scheme \(X\), its *geometric realization*, which is unique up to isomorphism. The proof there is indicated
by reference to the case of rings, and this lesson does not reproduce it. [Connes–Consani 2010, §4] then joins the
category of monoids and the category of rings along the adjoint functors \(M\mapsto\mathbb Z[M]\) and
\(A\mapsto(A,\cdot)\).

**Definition 9.5.** An *\(\mathbb F_1\)-scheme* consists of an \(\mathfrak{Mo}\)-scheme \(\underline X\), a scheme
\(X_{\mathbb Z}\), and maps \(e_A:\underline X((A,\cdot))\to X_{\mathbb Z}(A)\) for all rings \(A\), natural in
\(A\), such that \(e_K\) is bijective for every field \(K\). It is *Noetherian* if the geometric realization of
\(\underline X\) is of finite type and the scheme \(X_{\mathbb Z}\) is Noetherian.

*Reference:* [Connes–Consani 2010, Definitions 4.7 and 4.9]. There an \(\mathbb F_1\)-scheme is a functor on a
category that contains the monoids and the rings; [Connes–Consani 2010, Proposition 4.2] shows that this is the
same datum.

**Examples.** For a monoid \(M\), the triple of \(\operatorname{Spec}M\), \(\operatorname{Spec}\mathbb Z[M]\) and
the bijections \(\operatorname{Hom}(M,(A,\cdot))=\operatorname{Hom}(\mathbb Z[M],A)\) is an \(\mathbb F_1\)-scheme;
here \(e_A\) is bijective for all rings. For the projective line of Example 9.4, with
\(X_{\mathbb Z}=\mathbb P^1_{\mathbb Z}\), a morphism from the spectrum of a monoid lands in one of the two charts,
because the only open subset of such a spectrum that contains the maximal ideal is the whole spectrum. So
\(\underline X((A,\cdot))\) consists of the points \([a:1]\) and
\([1:b]\) with \(a,b\in A\) [Connes–Consani 2010, Lemma 3.12]. This is all of \(\mathbb P^1(A)\) if \(A\) is a
field, and it is not for \(A=\mathbb Z\), which has the point \([2:3]\). [Connes–Consani 2010, §4.3] makes this
remark. For a Chevalley group, [Connes–Consani 2010, Theorem 4.8] states that \(\mathfrak G\) extends to a scheme over
\(\mathbb F_{1^2}\), in the variant of the definition for pairs \((M,\epsilon)\); the bijection on fields is
Proposition 8.7.

**Theorem 9.6.** Let \(\mathcal X\) be a Noetherian \(\mathbb F_1\)-scheme and \(X\) the geometric realization of
its \(\mathfrak{Mo}\)-scheme. Suppose that \(X\) is torsion free. Then:

1. there is a polynomial \(N\) such that \(N(x+1)\) has non-negative integer coefficients and
   \(\#X(\mathbb F_{1^n})=N(n+1)\) for all \(n\ge1\);
2. \(\#X_{\mathbb Z}(\mathbb F_q)=N(q)\) for every prime power \(q\);
3. the zeta function of \(\mathcal X\) is \(\zeta_N(s)=\prod_{x\in X}\zeta_{(y-1)^{n(x)}}(s)\).

*Proof.* This is Theorem 9.3(c), (e) and (d), with \(N=N_X\). \(\square\)

*Reference:* [Connes–Consani 2010, Theorem 4.10].

In [Connes–Consani 2010] the third statement is written with the tensor product of Kurokawa. For two rational
functions with divisors \(\sum_im_i[a_i]\) and \(\sum_jn_j[b_j]\), it is a function with the divisor
\(\sum_{i,j}m_in_j[a_i+b_j]\) [Manin 1995, (1.19)]. The function \(1-1/s\) has the divisor \([1]-[0]\), so its
\(n\)-th tensor power has the divisor \(\sum_j(-1)^{n-j}\binom nj[j]\), which is the divisor of
\(1/\zeta_{(y-1)^n}\) by Proposition 6.4(f). With the convention that the zeroth tensor power is \(s\), the formula
of [Connes–Consani 2010, Theorem 4.10] reads
\[
\zeta_{\mathcal X}(s)=\prod_{x\in X}\frac1{(1-\frac1s)^{\otimes n(x)}} .
\]
[Connes–Consani 2010, §4.4] adds that the formula continues to hold in the presence of torsion, with the treatment
of torsion of [Deitmar 2006]. By Theorem 9.3(b) and (c) this means that \(N\) is then the polynomial \(N_X\), which
gives the number of points over \(\mathbb F_{1^n}\) only for \(n\) prime to the exponent.

**Gadgets and \(\mathbb F_1\)-schemes.** Restricted to the monoids \(D_0\), the functor of a monoid scheme of
finite type is a functor on finite abelian groups, graded by the local dimension (Proposition 9.1). For
\(X=\operatorname{Spec}M\) it is the graded functor of the gadget \(X_M\) (Proposition 7.4), and
[Connes–Consani 2010, Proposition 3.20] makes this comparison for the examples of [Connes–Consani 2011a, §3]. So
the functor of a torsion free Noetherian \(\mathbb F_1\)-scheme has a counting grading, and its counting polynomial
counts the points of \(X_{\mathbb Z}\) over finite fields. The condition of Definition 2.4 is of a different
kind: it determines \(X_{\mathbb Z}\) from the points and the algebra, and it does not control the number of
points. Example 4.8 satisfies Definition 2.4 and has too few points for an \(\mathbb F_1\)-scheme with the same
extension of scalars. The last monoid of Example 9.4 gives an \(\mathbb F_1\)-scheme and does not satisfy
Definition 2.4.

## 10. Exercises

**Exercise 1 (squares in the torus).** Let \(X(D)=\{g^2:g\in D\}\), with the algebra \(\mathbb C[T,T^{-1}]\) and
the evaluation \(f\mapsto f(h)\) for \(h\in X(D)\).

(a) Show that \(X\) is an affine variety over \(\mathbb F_1\) with \(X\otimes_{\mathbb F_1}\mathbb Z=\mathbb G_{m,\mathbb Z}\).

(b) Show that \(X\) has \(n/\gcd(2,n)\) points over \(\mathbb F_{1^n}\), and that it has no counting polynomial.

*Solution.* (a) A homomorphism \(u\) maps \(g^2\) to \(u(g)^2\), so \(X\) is a subfunctor of \(D\mapsto D\), and
\(X\) is a finite algebraic sub-gadget of \(\mathcal G(\mathbb G_{m,\mathbb Z})\). Let
\(f=\sum_{j\in S}b_jT^j\) be integral, with \(S\) finite. Choose an odd number \(n\) larger than all differences
of elements of \(S\), let \(D=\mu_n\) and let \(\xi\) be a generator. Since \(n\) is odd, \(h=\xi^2\) is a
generator, and \(h\in X(D)\). The elements \(h^j\), \(j\in S\), are pairwise distinct, so \(b_j\) is the
coefficient of \(h^j\) in \(f(h)\in\mathbb Z[D]\). Hence \(f\in\mathbb Z[T,T^{-1}]\), and Corollary 3.5 applies.
(b) The squares form the subgroup of index \(\gcd(2,n)\) of \(\mu_n\). A counting polynomial \(N\) would satisfy
\(N(n+1)=n\) for all odd \(n\), so \(N=x-1\); but \(\#X(\mathbb F_{1^2})=1\neq2\).

**Exercise 2 (morphisms and extension of scalars).** Let \(\mathbb G_m\) and \(\mathbb A^1\) be the gadgets of
Corollary 4.6.

(a) Show that the morphisms of gadgets \(\mathbb G_m\to\mathbb G_m\) are given by \(g\mapsto g^j\) and
\(\varphi^*(T)=T^j\), for \(j\in\mathbb Z\).

(b) Show that there is exactly one morphism of gadgets \(\mathbb A^1\to\mathbb G_m\).

(c) Conclude that the functor of extension of scalars is not full.

*Solution.* (a) Let \(\varphi\) be a morphism. By Proposition 3.7(a), \(\varphi^*\) restricts to a ring
homomorphism of \(\mathbb Z[T,T^{-1}]\) into itself, so \(\varphi^*(T)\) is a unit of \(\mathbb Z[T,T^{-1}]\). The
units of this ring are the elements \(\pm T^j\): if \(uv=1\), the product of the terms of highest degree of \(u\)
and \(v\) and the product of their terms of lowest degree are both equal to \(1\), so \(u\) and \(v\) are
monomials with coefficients \(\pm1\). For \(g\in D\) the condition of Definition 2.3 for
\(f=T\) says \(\varphi_D(g)=(\varphi^*T)(g)=\pm g^j\) in \(\mathbb Z[D]\). Since \(\varphi_D(g)\in D\), the sign is
\(+\). So \(\varphi_D(g)=g^j\) and \(\varphi^*(T)=T^j\). Conversely these data are a morphism. (b) Here
\(\varphi^*(T)\) is a unit of the ring \(\mathbb Z[S]\) of integral functions of \(\mathbb A^1\), so
\(\varphi^*(T)=\pm1\), and \(\varphi_D(x)=\pm1\in D\) forces the sign \(+\). So \(\varphi_D\) is the constant map
with value \(1\), and this is a morphism. (c) By (a) the automorphism \(T\mapsto-T\) of
\(\mathbb G_{m,\mathbb Z}\) is not of the form \(\varphi_{\mathbb Z}\).

**Exercise 3 (zeta functions).**

(a) Compute \(\zeta_N\) for \(N(x)=(x^2-1)(x^2-x)\), which is the order of \(\mathrm{GL}_2(\mathbb F_q)\) at
\(x=q\), and for \(N(x)=(1+x)(1+x+x^2)\), which is the number of complete flags in \(\mathbb F_q^3\) at \(x=q\).

(b) Let \(N\) have degree \(d\) and satisfy \(x^dN(1/x)=N(x)\). Show that
\(\zeta_N(d-s)=(-1)^{N(1)}\zeta_N(s)\).

*Solution.* (a) \(N=x^4-x^3-x^2+x\) gives \(\zeta_N(s)=\frac{(s-2)(s-3)}{(s-1)(s-4)}\). This also follows from
\(N=(x-1)(x^3-x)\), Proposition 6.4(c) and \(\zeta_{x^3-x}(s)=(s-1)/(s-3)\):
\(\zeta_N(s)=\frac{s-2}{s-4}\cdot\frac{s-3}{s-1}\). For the flags, \(N=1+2x+2x^2+x^3\) and
\(\zeta_N(s)=1/(s(s-1)^2(s-2)^2(s-3))\), with \(N(1)=6\), the order of the symmetric group on three letters.
(b) The hypothesis says \(a_{d-i}=a_i\). So
\[
\zeta_N(d-s)=\prod_i(d-s-i)^{-a_i}=(-1)^{-\sum_ia_i}\prod_i(s-(d-i))^{-a_{d-i}}=(-1)^{N(1)}\zeta_N(s).
\]
For the flags this gives \(\zeta_N(3-s)=\zeta_N(s)\), and for \(\mathbb P^d\) it gives
\(\zeta(d-s)=(-1)^{d+1}\zeta(s)\).

**Exercise 4 (the affine line with holomorphic functions).** Let \(\mathcal A\) be the algebra of the continuous
functions on the closed unit disc that are holomorphic in the open disc. Let \(X\) be the gadget over
\(\mathbb F_1\) with \(X(D)=D_0\), the algebra \(\mathcal A\), and the evaluation given by
\(\chi(f(x))=f(\chi(x))\) for all characters, where \(\chi(0)=0\). Show that the ring of integral functions is
\(\mathbb Z[T]\) and that \(X\) is an affine variety over \(\mathbb F_1\) with extension of scalars
\(\mathbb A^1_{\mathbb Z}\).

*Solution.* As in Proposition 5.2, \(X\) is a gadget. Let \(f\) be integral. Its values at the points
\(g\in D\) show, as in the proof of Proposition 5.2, that the restriction of \(f\) to \(S^1\) satisfies the
hypothesis of Lemma 5.1. So \(f=P\) on \(S^1\) for a Laurent polynomial \(P=\sum_ja_jT^j\) with integer
coefficients. For \(j<0\) the Fourier coefficient is
\(a_j=\frac1{2\pi i}\oint_{|z|=1}f(z)z^{-j-1}dz\). The function \(f(z)z^{-j-1}\) is holomorphic in the open disc,
so its integral over the circle \(|z|=r\) is \(0\) for \(r<1\) by Cauchy's theorem, and these integrals tend to
the integral over \(|z|=1\) because \(f\) is uniformly continuous on the closed disc. So \(a_j=0\) for \(j<0\), and
\(P\in\mathbb Z[T]\). The function \(f-P\) is continuous on the closed disc, holomorphic inside and \(0\) on the
circle, so it is \(0\) by the maximum principle. Conversely a polynomial with integer coefficients has the value
\(P(x)\in\mathbb Z[D]\) at \(x\in D_0\). The map \(\mathbb C[T]\to\mathcal A\) is injective, and a point \(x\) is
determined by the homomorphism \(T\mapsto x\). Now apply Theorem 3.3(c).

*Reference:* Soulé's 2009 Vanderbilt lectures. With rings as test objects and the points \(\mu(R)\cup\{0\}\), the same
algebra gives the affine line of [Soulé 2004, §5.2.1], a case of [Soulé 2004, Théorème 1].

**Exercise 5 (\(\mathrm{SL}_2\) and the field with three elements).** Let \((D,\epsilon)=(\mu_2,\epsilon)\), where
\(\mu_2=\{1,\epsilon\}\), and let \(G\) be the gadget of \(\mathrm{SL}_2\) of Section 8.4.

(a) Show that \(\mathbb Z[D,\epsilon]=\mathbb Z\) and that \(i\) maps \(G(D,\epsilon)\) bijectively onto a set of
\(24\) matrices in \(\mathrm{SL}_2(\mathbb Z)\).

(b) Show that reduction modulo \(3\) maps this set bijectively onto \(\mathrm{SL}_2(\mathbb F_3)\).

(c) Determine the points of degree \(1\) and the group that they form.

*Solution.* (a) By Lemma 1.2(a) with the set of representatives \(\{1\}\), the ring \(\mathbb Z[D,\epsilon]\) is
free of rank one, and \(\bar\epsilon=-1\). So \(D_0=\{0,1,\epsilon\}\) is mapped to \(\{0,1,-1\}\). By
Section 8.4 the points are the pairs \((a,t)\) and the triples \((a,t\bar\sigma,b)\) with \(t=\pm1\) and
\(a,b\in\{0,\pm1\}\). There are \(6+18=24\) of them, and \(i\) is injective by Step 1 of the proof of
Theorem 8.3. (b) The homomorphism \(\mathbb Z\to\mathbb F_3\) maps \(\{0,1,-1\}\) bijectively onto
\(\mathbb F_3\). The formulas for \(i\) commute with ring homomorphisms, so the composite map from
\(G(D,\epsilon)\) to \(\mathrm{SL}_2(\mathbb F_3)\) is the map of Proposition 8.7 for \(K=\mathbb F_3\), which is
bijective. Indeed \(\#\mathrm{SL}_2(\mathbb F_3)=3^3-3=24\). (c) The points of degree \(1\) are those with
\(a=0\) and \(b=0\). Their images are \(\pm1\) and \(\pm\sigma\), the group \(\mathcal N(\mathbb Z)\), which is
cyclic of order \(4\) and generated by \(\sigma\). There are \(12\) points of degree \(2\) and \(8\) of degree
\(3\).

**Exercise 6 (an idempotent).** Let \(M=\{0,1,e\}\) with \(e^2=e\).

(a) Show that \(M\) is not cancellative and that \(\mathbb Z[M]\cong\mathbb Z\times\mathbb Z\).

(b) Show that \(X_M\) is an affine variety over \(\mathbb F_1\) with extension of scalars
\(\operatorname{Spec}(\mathbb Z\times\mathbb Z)\).

(c) Compute the counting polynomial, the grading of Proposition 7.4 and the zeta function.

*Solution.* (a) \(e\cdot e=e\cdot1\) and \(e\neq0\), \(e\neq1\). The ring \(\mathbb Z[M]\) has the basis
\(1,e\), and \(b+ce\mapsto(b,b+c)\) is an isomorphism onto \(\mathbb Z\times\mathbb Z\). (b) A morphism
\(M\to D_0\) sends \(e\) to an idempotent of \(D_0\), that is, to \(0\) or \(1\). So \(X_M(D)\) has two points
\(x_0,x_1\) for every \(D\), and the values of \(f=b+ce\) are \(f(x_0)=b\) and \(f(x_1)=b+c\). So \(f\) is
integral if and only if \(b\) and \(b+c\) are integers, that is, \(f\in\mathbb Z[M]\). Corollary 3.5 applies. So
the hypothesis of Theorem 4.4 is not necessary. (c) \(X_M\) has two points over every \(\mathbb F_{1^n}\), so
\(N=2\) and \(\zeta(s)=1/s^2\). The prime ideals are \(\{0\}\) and \(\{0,e\}\). In both localizations the group of
units is trivial: in the localization at \(\{0\}\) the element \(e\) becomes a unit with \(e^2=e\), so \(e=1\).
Both points have degree \(0\), and \(N(x)=(x-1)^0+(x-1)^0=2\), in agreement with Proposition 7.4.

## 11. What this lesson does not prove

- **The group of Tits.** That the group \(\mathcal N_{D,\epsilon}\) of Section 8.2 is the group constructed in
  [Tits 1966, §4.3] is stated in [Connes–Consani 2011a, §4.3].
- **Varieties that are not affine.** The converse in [Soulé 2004, Proposition 3], that a variety whose extension
  of scalars is affine comes from an affine variety, and the counts in [Soulé 2004, Théorème 2]. The lesson proves
  the gluing under condition (E) (Proposition 5.6) and the theorem on regular toric varieties for both systems of
  test objects (Theorem 5.8); in particular \(\mathbb P^d\) is a variety in this sense, with the algebras of
  continuous functions. Proposition 4.13 treats \(\mathbb P^d\) with algebraic functions.
- **The affinely torified varieties.** [López Peña–Lorscheid 2011b, Theorem 2.10]. The lesson *Torified varieties
  and the limits of monoid schemes* proves the affine case under the condition that the fibres over all primes are
  reduced, and shows by an example that the condition is needed.
- **The functorial theory of \(\mathfrak{Mo}\)-schemes.** [Connes–Consani 2010, Proposition 3.16] (geometric
  realization) and [Connes–Consani 2010, Theorem 4.8]; the equivalence of "Noetherian" and "finitely generated" for
  monoids, quoted in [Connes–Consani 2010, §4.4]; the base change of a monoid scheme that is not affine and its
  points over fields, for which see *Monoid schemes*.
- **Standard facts.** The structure of finitely generated abelian groups, which is the case of the ring
  \(\mathbb Z\) of the statement on finite modules over a principal ideal domain [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]; Bessel's
  inequality and Fejér's theorem for Fourier series, and the Stone–Weierstrass theorem; Cauchy's theorem and
  integral formula, the identity theorem, locally uniform limits of holomorphic functions, and the maximum principle
  (Exercise 4, Theorem 5.8, Example 5.7); the
  finiteness of the group of roots of unity of a number field; the construction of projective space by gluing
  [Stacks, Tag [01ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-projective-space)].

## References

- [Soulé 2004] C. Soulé, *Les variétés sur le corps à un élément*, [arXiv:math/0304444](https://arxiv.org/pdf/math/0304444).
- [Connes–Consani 2011a] A. Connes, C. Consani, *On the notion of geometry over \(\mathbb F_1\)*, arXiv:0809.2926.
  Result numbers refer to version 2. Free at https://alainconnes.org/wp-content/uploads/GeomoverF1.pdf
- [Connes–Consani 2010] A. Connes, C. Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024.
  Result numbers refer to version 3. Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Connes–Consani–Marcolli 2009b] A. Connes, C. Consani, M. Marcolli, *Fun with \(\mathbb F_1\)*, [arXiv:0806.2401](https://arxiv.org/pdf/0806.2401).
- [Deitmar 2006] A. Deitmar, *Remarks on zeta functions and K-theory over \(\mathbb F_1\)*, [arXiv:math/0605429](https://arxiv.org/pdf/math/0605429).
- [López Peña–Lorscheid 2011a] J. López Peña, O. Lorscheid, *Mapping \(\mathbb F_1\)-land: an overview of geometries over
  the field with one element*, [arXiv:0909.0069](https://arxiv.org/pdf/0909.0069).
- [López Peña–Lorscheid 2011b] J. López Peña, O. Lorscheid, *Torified varieties and their geometries over
  \(\mathbb F_1\)*, [arXiv:0903.2173](https://arxiv.org/pdf/0903.2173v3). Result numbers refer to version 3.
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 01I1 and 0ASV carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Soulé 1999] C. Soulé, *On the field with one element*, talk at the Arbeitstagung, Bonn, June 1999, preprint
  IHES/M/99/55. Free at https://www.mpim-bonn.mpg.de/preblob/175 (the Arbeitstagung notes, DVI file)
- [Manin 1995] Yu. Manin, *Lectures on zeta functions and motives (according to Deninger and Kurokawa)*, Astérisque
  228 (1995), 121–163. Free at https://www.numdam.org/item/AST_1995__228__121_0/
- [Kurokawa 2005] N. Kurokawa, *Zeta functions over \(\mathbb F_1\)*, Proc. Japan Acad. Ser. A Math. Sci. 81 (2005),
  180–184. Free at https://doi.org/10.3792/pjaa.81.180
- [Deitmar–Koyama–Kurokawa 2008] A. Deitmar, S. Koyama, N. Kurokawa, *Absolute zeta functions*, Proc. Japan Acad.
  Ser. A Math. Sci. 84 (2008), 138–142. Free at https://doi.org/10.3792/pjaa.84.138
- [Kim–Koyama–Kurokawa 2009] S. Kim, S. Koyama, N. Kurokawa, *The Riemann hypothesis and functional equations for
  zeta functions over \(\mathbb F_1\)*, Proc. Japan Acad. Ser. A Math. Sci. 85 (2009), 75–80. Free at https://doi.org/10.3792/pjaa.85.75
- [Tits 1966] J. Tits, *Normalisateurs de tores. I. Groupes de Coxeter étendus*, J. Algebra 4 (1966), 96–116.
  Cited through [Connes–Consani 2011a]. Free at https://doi.org/10.1016/0021-8693(66)90053-6
- [Chevalley 1955] C. Chevalley, *Sur certains groupes simples*, Tôhoku Math. J. (2) 7 (1955), 14–66. Cited
  through [Connes–Consani 2011a]. Free at https://doi.org/10.2748/tmj/1178245104
- [Chevalley 1961] C. Chevalley, *Certains schémas de groupes semi-simples*, Séminaire Bourbaki, exposé 219;
  reprinted in Séminaire Bourbaki, Vol. 6, Soc. Math. France, 1995. Cited through [Connes–Consani 2011a]. Free at https://www.numdam.org/item/SB_1960-1961__6__219_0/
- [SGA3] M. Demazure, A. Grothendieck, *Schémas en groupes*, Séminaire de géométrie algébrique. Cited through
  [Connes–Consani 2011a] and [López Peña–Lorscheid 2011b]. Free at https://webusers.imj-prg.fr/~patrick.polo/SGA3/ (re-edition by P. Gille and P. Polo)
