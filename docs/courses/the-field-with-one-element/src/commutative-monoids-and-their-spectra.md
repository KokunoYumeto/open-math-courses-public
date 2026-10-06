# Commutative monoids and their spectra

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

Take a commutative ring and forget its addition. What is left is a set with a commutative multiplication, a unit \(1\)
and an absorbing element \(0\): a commutative monoid with zero. The simplest geometry over the field with one element
replaces rings by such monoids. A monoid \(M\) plays the role of a ring over \(\mathbb F_1\), and the ring
\(\mathbb Z[M]\) spanned by \(M\) is its base change to the integers. This lesson develops the commutative algebra of
monoids that the course uses: ideals and prime ideals, the spectrum, localization, the structure sheaf, quotients,
finiteness conditions, and the passage from \(M\) to \(\mathbb Z[M]\). The next lesson, *Monoid schemes*, glues
spectra together.

Most definitions are copied from ring theory. The interest lies in what changes. The lesson proves the following
statements. The first six have no counterpart for rings, and the seventh relates a monoid to its ring.

1. A non-zero monoid has exactly one maximal ideal, the set of its non-units. A union of ideals is an ideal, and a
   union of prime ideals is a prime ideal (Section 2).
2. For every multiplicative set \(S\) that does not contain \(0\) there is a largest ideal disjoint from \(S\). It
   is prime and it is given by a formula, so prime ideals are found without Zorn's lemma (Theorem 2.8).
3. A non-empty open subset of the spectrum is a basic open set \(D(f)\) exactly when it has a largest point, and
   every non-zero localization of a monoid is the localization at a prime ideal (Theorems 3.4 and 4.3).
4. A section of the structure sheaf over any open set is a compatible family of germs. The formulas
   \(\mathcal O(D(f))=M_f\) and \(\mathcal O(\operatorname{Spec}M)=M\) follow in two lines (Section 5).
5. Quotients of a monoid are described by congruences, and only some congruences come from ideals (Section 6).
6. A finitely generated monoid has finitely many prime ideals, and its spectrum is a finite partially ordered set
   (Section 7).
7. The map \(\operatorname{Spec}\mathbb Z[M]\to\operatorname{Spec}M\) is surjective, and its fibres are spectra of
   group rings. The ring \(\mathbb Z[M]\) is a domain exactly when \(M\) is cancellative and torsion-free
   (Section 8).

Section 9 works out free monoids and the monoids of lattice points of cones. Section 10 compares the monoids with
zero used here with the monoids without zero of [Deitmar 2005]. Section 11 contains exercises with solutions.

**What is assumed.** Commutative rings, ideals, prime ideals and localization [Stacks, Tags [00AR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-rings-basic) and [00CM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-localization)]; the
spectrum of a ring with its Zariski topology [Stacks, Tag [00DY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-spectrum-ring)]; sheaves on a topological space and their stalks
[Stacks, Tags [006S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-sheaves) and [0078](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-stalks)]. Section 9 uses linear algebra over \(\mathbb Q\) and \(\mathbb R\). The lessons
*Counting over finite fields and the limit q → 1* and *Weil's proof for curves and what is missing over the
integers* explain why one looks for a geometry below the integers; they are not used in the proofs.

Basic references are [Deitmar 2005], [Chu–Lorscheid–Santhanam 2012], [Cortiñas–Haesemeyer–Walker–Weibel 2015] and
[Connes–Consani 2010b].

**Conventions.** Rings are commutative with \(1\). \(\mathbb N=\{0,1,2,\dots\}\). The word *monoid* always has the
meaning of Definition 1.1: commutative, written multiplicatively, with \(1\) and with \(0\). A *commutative monoid
without zero* is a monoid in the ordinary sense, in which no zero is required. For elements \(a,b\) of a monoid,
"\(a\) divides \(b\)" means \(b=ac\) for some \(c\).

## 1. Monoids with zero

**Definition 1.1.** A *monoid* is a set \(M\) with an associative and commutative multiplication, an element \(1\)
such that \(1a=a\) for all \(a\in M\), and an element \(0\) such that \(0a=0\) for all \(a\in M\). A *morphism* of
monoids is a map \(\varphi:M\to N\) with \(\varphi(ab)=\varphi(a)\varphi(b)\), \(\varphi(1)=1\) and \(\varphi(0)=0\).
The set of morphisms is written \(\operatorname{Hom}(M,N)\). A *submonoid* of \(M\) is a subset that contains \(0\)
and \(1\) and is closed under multiplication.

The elements \(0\) and \(1\) are unique. If \(0=1\) then \(a=1a=0a=0\) for all \(a\), so \(M=\{0\}\). This is the
*zero monoid*, written \(0\).

**Definition 1.2.** An element \(a\in M\) is a *unit* if \(ab=1\) for some \(b\in M\). The units form an abelian
group \(M^\times\). If \(M\neq0\), then \(0\) is not a unit, because \(0b=0\neq1\).

**Examples 1.3.**

(a) \(\mathbb F_1=\{0,1\}\). For every monoid \(M\) there is exactly one morphism \(\mathbb F_1\to M\) and exactly
one morphism \(M\to0\).

(b) If \(R\) is a ring, forgetting the addition gives the monoid \((R,\cdot)\). A ring homomorphism is a morphism of
the multiplicative monoids.

(c) Let \(A\) be a commutative monoid without zero. Then \(A_0=A\sqcup\{0\}\), with \(0a=0\) for all \(a\), is a
monoid. If \(A=G\) is an abelian group, every non-zero element of \(G_0\) is a unit; we call \(G_0\) a *group with
zero*. For a field \(k\) we have \((k,\cdot)=(k^\times)_0\). For \(n\ge1\) the monoid
\(\mathbb F_{1^n}=(\mu_n)_0\) consists of \(0\) and the \(n\)-th roots of unity.

(d) Let \(P\) be a commutative monoid without zero, written additively. We write \(\mathbb F_1[P]\) for the monoid
\(P_0\) in multiplicative notation: its elements are \(0\) and the symbols \(\chi^m\), \(m\in P\), with
\(\chi^m\chi^{m'}=\chi^{m+m'}\) and \(1=\chi^0\). For \(P=\mathbb N^n\) put \(x_i=\chi^{e_i}\). Then
\(\mathbb F_1[x_1,\dots,x_n]:=\mathbb F_1[\mathbb N^n]\) consists of \(0\) and the monomials
\(x^a=x_1^{a_1}\cdots x_n^{a_n}\). It is the *free monoid* on \(x_1,\dots,x_n\). For \(P=\mathbb Z^n\) we get the
group with zero \(\mathbb F_1[x_1^{\pm1},\dots,x_n^{\pm1}]\) of Laurent monomials.

(e) The product \(M\times N\) of two monoids, with componentwise multiplication, is a monoid with zero \((0,0)\) and
one \((1,1)\).

(f) The set \(\{0,1,\varepsilon\}\) with \(\varepsilon^2=0\) is a monoid. So is \(\{0,e,1\}\) with \(e^2=e\).

(g) For readers who know adèles: let \(K\) be a global field with adèle ring \(\mathbb A_K\). The group \(K^\times\)
acts on \(\mathbb A_K\) by multiplication, and the product of \(\mathbb A_K\) descends to the set of orbits
\(\mathbb A_K/K^\times\). This is the monoid of adèle classes of [Connes–Consani 2010b, Section 3.2]. Its group of
units is the idèle class group \(\mathbb A_K^\times/K^\times\).

**Proposition 1.4 (free monoids).** Let \(N\) be a monoid and \(b_1,\dots,b_n\in N\). There is exactly one morphism
\(\varphi:\mathbb F_1[x_1,\dots,x_n]\to N\) with \(\varphi(x_i)=b_i\) for all \(i\).

*Proof.* A morphism with \(\varphi(x_i)=b_i\) must send \(x^a\) to \(b_1^{a_1}\cdots b_n^{a_n}\) and \(0\) to \(0\).
This map is a morphism, because exponents add. \(\square\)

**Definition 1.5.** A monoid \(M\) is *without zero divisors* if \(M\neq0\) and \(ab=0\) implies \(a=0\) or \(b=0\).

**Proposition 1.6 (adjoining a zero).**

(a) Let \(A\) be a commutative monoid without zero and \(N\) a monoid. Restriction to \(A\) is a bijection from
\(\operatorname{Hom}(A_0,N)\) to the set of maps \(\psi:A\to N\) with \(\psi(ab)=\psi(a)\psi(b)\) and \(\psi(1)=1\).

(b) A monoid \(M\) is isomorphic to \(A_0\) for some commutative monoid \(A\) without zero if and only if \(M\) is
without zero divisors. In that case \(A\cong M\setminus\{0\}\).

*Proof.* (a) Extend \(\psi\) by \(0\mapsto0\). The extension is multiplicative, and it is the only extension that is
a morphism. (b) In \(A_0\) a product of two elements of \(A\) lies in \(A\), and \(1\neq0\). Conversely, if \(M\) is
without zero divisors, then \(M\setminus\{0\}\) contains \(1\) and is closed under multiplication, and
\(M=(M\setminus\{0\})_0\). \(\square\)

Several monoids of Examples 1.3 have zero divisors, so they are not of the form \(A_0\):
\(\varepsilon\cdot\varepsilon=0\) in \(\{0,1,\varepsilon\}\); \((1,0)(0,1)=(0,0)\) in \(M\times N\) when
\(M,N\neq0\); and in the monoid of adèle classes the classes of two non-zero adèles with disjoint supports have
product \(0\). The monoid \((R,\cdot)\) of a ring is without zero divisors exactly when \(R\) is a domain. Zero
divisors are the reason for working with a zero from the start; Section 10 returns to this.

## 2. Ideals, prime ideals and faces

**Definition 2.1.** An *ideal* of a monoid \(M\) is a subset \(I\subseteq M\) with \(0\in I\) and \(ab\in I\) for all
\(a\in I\), \(b\in M\). The ideal *generated* by a subset \(T\subseteq M\) is
\(\langle T\rangle=\{tb:t\in T,\ b\in M\}\cup\{0\}\); for one element \(f\) it is \(fM\). An ideal \(I\) is *proper*
if \(I\neq M\). This holds if and only if \(1\notin I\), and if and only if \(I\) contains no unit.

**Lemma 2.2.**

(a) The union and the intersection of a non-empty family of ideals of \(M\) are ideals.

(b) If \(M\neq0\), then \(\mathfrak m_M:=M\setminus M^\times\) is an ideal, and it contains every proper ideal.

*Proof.* (a) Both contain \(0\) and are stable under multiplication by elements of \(M\). (b) We have
\(0\in\mathfrak m_M\) by Definition 1.2. Let \(a\in\mathfrak m_M\) and \(b\in M\). If \(ab\) were a unit, say
\((ab)c=1\), then \(a(bc)=1\) and \(a\) would be a unit. So \(ab\in\mathfrak m_M\). A proper ideal contains no unit,
so it lies in \(\mathfrak m_M\). \(\square\)

So a non-zero monoid has exactly one maximal ideal, \(\mathfrak m_M\). A ring with exactly one maximal ideal is
called local [Stacks, Tag [07BI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-local-ring)]; in this sense every non-zero monoid is local. The difference from rings is that an
ideal of a monoid has no addition to respect. In a ring the non-units are stable under multiplication by ring
elements, but not under addition: in \(\mathbb Z\) the elements \(2\) and \(3\) are non-units and \(3-2=1\). For
the same reason the union of two ideals of a monoid is an ideal, which is rarely true in a ring.

**Definition 2.3.** An ideal \(\mathfrak p\) of \(M\) is *prime* if \(\mathfrak p\neq M\) and \(ab\in\mathfrak p\)
implies \(a\in\mathfrak p\) or \(b\in\mathfrak p\). The set of prime ideals of \(M\) is written
\(\operatorname{Spec}M\). A *face* of \(M\) is a subset \(F\subseteq M\) with \(1\in F\), \(0\notin F\), and such
that for all \(a,b\in M\):
\[
ab\in F\iff a\in F\ \text{and}\ b\in F .
\]

**Lemma 2.4.** A subset \(\mathfrak p\subseteq M\) is a prime ideal if and only if \(M\setminus\mathfrak p\) is a
face. So \(\mathfrak p\mapsto M\setminus\mathfrak p\) is a bijection from \(\operatorname{Spec}M\) to the set of
faces of \(M\), and it reverses inclusions.

*Proof.* Let \(\mathfrak p\) be prime and \(F=M\setminus\mathfrak p\). Then \(0\notin F\), and \(1\in F\) because
\(\mathfrak p\) is proper. If \(a,b\in F\) then \(ab\in F\), because \(\mathfrak p\) is prime. If \(ab\in F\) then
\(a,b\in F\), because \(\mathfrak p\) is an ideal. Conversely let \(F\) be a face and \(\mathfrak p=M\setminus F\).
Then \(0\in\mathfrak p\) and \(1\notin\mathfrak p\). If \(a\in\mathfrak p\) and \(b\in M\), then \(ab\notin F\),
since \(ab\in F\) would force \(a\in F\). So \(\mathfrak p\) is a proper ideal. If \(ab\in\mathfrak p\) and
\(a,b\notin\mathfrak p\), then \(a,b\in F\) and \(ab\in F\), a contradiction. \(\square\)

**Examples 2.5.** Let \(M\neq0\). The maximal ideal \(\mathfrak m_M\) is prime; its face \(M^\times\) is the
smallest face. The ideal \(\{0\}\) is prime if and only if \(M\) is without zero divisors; its face
\(M\setminus\{0\}\) is then the largest face. The zero monoid has no prime ideal.

**Lemma 2.6.** Let \(\varphi:M\to N\) be a morphism and \(\mathfrak q\) a prime ideal of \(N\). Then
\(\varphi^{-1}(\mathfrak q)\) is a prime ideal of \(M\).

*Proof.* It contains \(0\), it is stable under multiplication by \(M\), and it does not contain \(1\), because
\(\varphi(1)=1\notin\mathfrak q\). If \(ab\in\varphi^{-1}(\mathfrak q)\), then
\(\varphi(a)\varphi(b)\in\mathfrak q\), so \(\varphi(a)\in\mathfrak q\) or \(\varphi(b)\in\mathfrak q\).
\(\square\)

So a morphism \(\varphi:M\to N\) induces a map \(\varphi^*:\operatorname{Spec}N\to\operatorname{Spec}M\),
\(\mathfrak q\mapsto\varphi^{-1}(\mathfrak q)\). A morphism between non-zero monoids is called *local* if
\(\varphi^{-1}(\mathfrak m_N)=\mathfrak m_M\), that is, if \(\varphi(a)\) is a unit only when \(a\) is a unit.

**Proposition 2.7 (points are morphisms to \(\mathbb F_1\)).** For a prime ideal \(\mathfrak p\) of \(M\) define
\(\chi_{\mathfrak p}:M\to\mathbb F_1\) by \(\chi_{\mathfrak p}(a)=0\) if \(a\in\mathfrak p\) and
\(\chi_{\mathfrak p}(a)=1\) if \(a\notin\mathfrak p\). Then \(\mathfrak p\mapsto\chi_{\mathfrak p}\) is a bijection
\[
\operatorname{Spec}M\longrightarrow\operatorname{Hom}(M,\mathbb F_1),
\]
with inverse \(\chi\mapsto\chi^{-1}(0)\).

*Proof.* The map \(\chi_{\mathfrak p}\) sends \(0\) to \(0\) and \(1\) to \(1\). It is multiplicative by Lemma 2.4:
\(ab\notin\mathfrak p\) holds if and only if \(a\notin\mathfrak p\) and \(b\notin\mathfrak p\). Conversely \(\{0\}\)
is a prime ideal of \(\mathbb F_1\), so \(\chi^{-1}(0)\) is a prime ideal by Lemma 2.6. The two constructions are
inverse to each other. \(\square\)

For a ring one needs homomorphisms to all fields to see all points of the spectrum. For a monoid the single target
\(\mathbb F_1\) is enough. *Reference:* [Connes–Consani 2010b, Theorem 3.1] recalls the corresponding statement for
the schemes built from monoids.

A subset \(S\subseteq M\) is *multiplicative* if \(1\in S\) and \(st\in S\) for all \(s,t\in S\). A face is a
multiplicative subset.

**Theorem 2.8 (the prime ideal of a multiplicative set).** Let \(S\) be a multiplicative subset of \(M\) with
\(0\notin S\). Put
\[
S^{\mathrm{sat}}=\{a\in M: ab\in S\ \text{for some}\ b\in M\},\qquad
\mathfrak p_S=M\setminus S^{\mathrm{sat}} .
\]

(a) \(S^{\mathrm{sat}}\) is a face. It is the smallest face that contains \(S\).

(b) \(\mathfrak p_S\) is a prime ideal with \(\mathfrak p_S\cap S=\emptyset\), and it contains every ideal \(I\) of
\(M\) with \(I\cap S=\emptyset\).

*Proof.* (a) We have \(1\in S\subseteq S^{\mathrm{sat}}\), and \(0\notin S^{\mathrm{sat}}\) because
\(0b=0\notin S\). If \(ab\in S\) and \(a'b'\in S\), then \((aa')(bb')\in S\), so \(S^{\mathrm{sat}}\) is closed
under multiplication. If \(aa'\in S^{\mathrm{sat}}\), say \((aa')b\in S\), then \(a(a'b)\in S\) and \(a'(ab)\in S\),
so \(a,a'\in S^{\mathrm{sat}}\). Hence \(S^{\mathrm{sat}}\) is a face. A face \(F\supseteq S\) contains every
divisor of every element of \(S\), so \(F\supseteq S^{\mathrm{sat}}\).

(b) By (a) and Lemma 2.4, \(\mathfrak p_S\) is a prime ideal, and it is disjoint from \(S\). Let \(I\) be an ideal
with \(I\cap S=\emptyset\) and let \(a\in I\). Then \(ab\in I\) for all \(b\), so \(ab\notin S\) for all \(b\). Hence
\(a\notin S^{\mathrm{sat}}\), that is, \(a\in\mathfrak p_S\). \(\square\)

In a ring, a prime ideal that is disjoint from \(S\) and contains a given ideal is found with Zorn's lemma, and there
is no largest one in general. Here the prime ideal is given by a formula: \(\mathfrak p_S\) is the set of elements
that divide no element of \(S\).

**Corollary 2.9.** Let \(M\) be a monoid.

(a) If \(M\neq0\), then \(\operatorname{Spec}M\neq\emptyset\).

(b) Let \(f\in M\) be not nilpotent. Then
\(\mathfrak p_f:=\{a\in M: a\ \text{divides no power}\ f^n,\ n\ge0\}\) is a prime ideal, and it is the largest prime
ideal that does not contain \(f\).

(c) For an ideal \(I\) put \(\sqrt I=\{a\in M:a^n\in I\ \text{for some}\ n\ge1\}\). Then \(\sqrt I\) is the
intersection of all prime ideals containing \(I\). In particular the set of nilpotent elements of \(M\) is the
intersection of all prime ideals.

*Proof.* (a) \(\mathfrak m_M\) is prime. (b) The set \(S=\{f^n:n\ge0\}\) is multiplicative and \(0\notin S\). By
Theorem 2.8, \(\mathfrak p_f=\mathfrak p_S\) is prime and \(f\notin\mathfrak p_f\). A prime ideal \(\mathfrak q\)
with \(f\notin\mathfrak q\) contains no power of \(f\), so it is disjoint from \(S\) and
\(\mathfrak q\subseteq\mathfrak p_S\). (c) If \(a^n\in I\subseteq\mathfrak p\) with \(\mathfrak p\) prime, then
\(a\in\mathfrak p\). Conversely let \(a\notin\sqrt I\) and \(S=\{a^n:n\ge0\}\). No power \(a^n\) with \(n\ge1\) lies
in \(I\), and \(1\notin I\), because otherwise \(I=M\) would contain \(a\). So \(S\cap I=\emptyset\), and
\(0\notin S\) because \(0\in I\). By Theorem 2.8 the prime ideal \(\mathfrak p_S\) contains \(I\) and not \(a\).
(If \(I=M\), both sides are \(M\), the intersection of the empty family.) \(\square\)

**Lemma 2.10.** The union of a non-empty family of prime ideals of \(M\) is a prime ideal.

*Proof.* The complement of the union is the intersection of the faces \(F_i=M\setminus\mathfrak p_i\). It contains
\(1\) and not \(0\), and \(ab\) lies in all \(F_i\) if and only if \(a\) and \(b\) lie in all \(F_i\). So it is a
face, and Lemma 2.4 applies. \(\square\)

So any two prime ideals \(\mathfrak p,\mathfrak q\) are contained in a smallest prime ideal, namely
\(\mathfrak p\cup\mathfrak q\). In \(\mathbb Z\) the union \(2\mathbb Z\cup3\mathbb Z\) is not an ideal of the ring.

## 3. The spectrum as a topological space

**Definition 3.1.** For a subset \(T\subseteq M\) and an element \(f\in M\) put
\[
V(T)=\{\mathfrak p\in\operatorname{Spec}M:T\subseteq\mathfrak p\},\qquad
D(f)=\{\mathfrak p\in\operatorname{Spec}M:f\notin\mathfrak p\}.
\]

**Proposition 3.2.** Let \(M\) be a monoid.

(a) \(V(T)=V(\langle T\rangle)\) for every subset \(T\).

(b) \(V(\{0\})=\operatorname{Spec}M\) and \(V(M)=\emptyset\). For ideals \(I,J\) we have
\(V(I)\cup V(J)=V(I\cap J)\). For a non-empty family of ideals \(I_\alpha\) we have
\(\bigcap_\alpha V(I_\alpha)=V(\bigcup_\alpha I_\alpha)\).

(c) The sets \(V(I)\), \(I\) an ideal, are the closed sets of a topology on \(\operatorname{Spec}M\). The sets
\(D(f)\) are open and form a basis of this topology, and \(D(f)\cap D(g)=D(fg)\).

(d) \(D(f)=\emptyset\) if and only if \(f\) is nilpotent. If \(M\neq0\), then \(D(f)=\operatorname{Spec}M\) if and
only if \(f\) is a unit.

(e) \(D(f)\subseteq D(g)\) if and only if \(g\) divides \(f^n\) for some \(n\ge1\).

*Proof.* (a) A prime ideal that contains \(T\) contains \(\langle T\rangle\). (b) Every prime ideal contains \(0\)
and none contains \(1\). A prime ideal that contains \(I\) or \(J\) contains \(I\cap J\). If \(\mathfrak p\) contains
neither, take \(a\in I\setminus\mathfrak p\) and \(b\in J\setminus\mathfrak p\); then \(ab\in I\cap J\) and
\(ab\notin\mathfrak p\). The last formula is clear, and \(\bigcup_\alpha I_\alpha\) is an ideal by Lemma 2.2.
(c) Part (b) gives the axioms for closed sets. \(D(f)\) is the complement of \(V(fM)\), and the complement of
\(V(I)\) is \(\bigcup_{f\in I}D(f)\). The formula \(D(f)\cap D(g)=D(fg)\) restates Lemma 2.4. (d) \(D(f)\) is empty
if and only if \(f\) lies in all prime ideals, that is, \(f\) is nilpotent (Corollary 2.9(c)). Every prime ideal lies
in \(\mathfrak m_M\). So \(D(f)=\operatorname{Spec}M\) if and only if \(f\notin\mathfrak m_M\). (e) If \(f^n=gh\) and
\(g\in\mathfrak p\), then \(f^n\in\mathfrak p\) and \(f\in\mathfrak p\). Conversely suppose that no power \(f^n\),
\(n\ge1\), lies in \(gM\). Then \(1\notin gM\) as well, since otherwise \(gM=M\) would contain \(f\). So
\(S=\{f^n:n\ge0\}\) is disjoint from the ideal \(gM\), and \(0\notin S\). By Theorem 2.8 the prime ideal
\(\mathfrak p_S\) contains \(g\) and not \(f\). It lies in \(D(f)\) and not in \(D(g)\). \(\square\)

The topology of (c) is the *Zariski topology*. It is the topology generated by the sets \(D(f)\). From now on
\(\operatorname{Spec}M\) carries this topology. For a morphism \(\varphi:M\to N\) the map \(\varphi^*\) of Lemma 2.6
is continuous, because \((\varphi^*)^{-1}(D(f))=D(\varphi(f))\).

**Proposition 3.3 (order and the closed point).** Let \(M\neq0\) and \(X=\operatorname{Spec}M\).

(a) The closure of a point \(\mathfrak p\) is \(V(\mathfrak p)\). So \(\mathfrak q\) lies in the closure of
\(\mathfrak p\) if and only if \(\mathfrak p\subseteq\mathfrak q\), and different points have different closures.

(b) Every open set \(U\) is *stable under generization*: if \(\mathfrak p\in U\) and
\(\mathfrak q\subseteq\mathfrak p\) is prime, then \(\mathfrak q\in U\).

(c) The point \(\mathfrak m_M\) lies in every non-empty closed subset of \(X\), and \(X\) is the only open set that
contains \(\mathfrak m_M\).

(d) \(X\) is quasi-compact and connected.

*Proof.* (a) \(V(\mathfrak p)\) is closed and contains \(\mathfrak p\). A closed set \(V(I)\) that contains
\(\mathfrak p\) has \(I\subseteq\mathfrak p\), hence \(V(\mathfrak p)\subseteq V(I)\). (b) \(U\) is a union of sets
\(D(f)\), and \(f\notin\mathfrak p\) implies \(f\notin\mathfrak q\). (c) If \(V(I)\neq\emptyset\) then \(I\) is
proper, so \(I\subseteq\mathfrak m_M\) by Lemma 2.2. The complement of an open set that contains \(\mathfrak m_M\) is
a closed set that does not contain \(\mathfrak m_M\), so it is empty. (d) In an open cover of \(X\) one member
contains \(\mathfrak m_M\), so it is \(X\). If \(X=U\sqcup U'\) with \(U,U'\) open, the one that contains
\(\mathfrak m_M\) is \(X\). \(\square\)

The spectrum of a ring is quasi-compact too [Stacks, Tag [00E8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-compact)], but it need not be connected: the spectrum of a
product of two rings is the disjoint union of the two spectra [Stacks, Tag [00ED](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-product)]. The spectrum of a product of two
non-zero monoids is connected. Exercise 2 describes it.

For a prime ideal \(\mathfrak p\) write
\[
\Lambda(\mathfrak p)=\{\mathfrak q\in\operatorname{Spec}M:\mathfrak q\subseteq\mathfrak p\}
\]
for the set of its generizations. By Proposition 3.3(b) every open set that contains \(\mathfrak p\) contains
\(\Lambda(\mathfrak p)\). In fact \(\Lambda(\mathfrak p)\) is the intersection of all open sets containing
\(\mathfrak p\): if \(\mathfrak q\not\subseteq\mathfrak p\), take \(f\in\mathfrak q\setminus\mathfrak p\); then
\(D(f)\) contains \(\mathfrak p\) and not \(\mathfrak q\).

**Theorem 3.4 (basic open sets).** For a non-empty open subset \(U\) of \(\operatorname{Spec}M\) the following are
equivalent.

(i) \(U=D(f)\) for some \(f\in M\).

(ii) \(U\) has a largest element for inclusion.

(iii) \(U=\Lambda(\mathfrak p)\) for some prime ideal \(\mathfrak p\).

If \(U=D(f)\), then the largest element of \(U\) is \(\mathfrak p_f\).

*Proof.* (i)⇒(iii): \(D(f)\neq\emptyset\), so \(f\) is not nilpotent. By Corollary 2.9(b) every
\(\mathfrak q\in D(f)\) lies in \(\mathfrak p_f\). Conversely \(\mathfrak q\subseteq\mathfrak p_f\) implies
\(f\notin\mathfrak q\). So \(D(f)=\Lambda(\mathfrak p_f)\). (iii)⇒(ii) is clear. (ii)⇒(i): let \(\mathfrak p\) be
the largest element of \(U\). Since \(U\) is open there is \(f\) with \(\mathfrak p\in D(f)\subseteq U\). Every
\(\mathfrak q\in U\) satisfies \(\mathfrak q\subseteq\mathfrak p\), hence \(f\notin\mathfrak q\). So
\(U\subseteq D(f)\). \(\square\)

**Corollary 3.5.** Let \(f\in M\) be not nilpotent. If a family of open subsets of \(\operatorname{Spec}M\) covers
\(D(f)\), then one member of the family contains \(D(f)\).

*Proof.* One member \(W\) contains the point \(\mathfrak p_f\). By Proposition 3.3(b) it contains
\(\Lambda(\mathfrak p_f)=D(f)\). \(\square\)

The set \(\Lambda(\mathfrak p)\) need not be open (Example 9.2), and in condition (ii) a largest element cannot be
weakened to a unique maximal element:

**Example 3.6 (one maximal point, no largest point).** Let \(Q\) be the set of all sequences
\(\gamma=(\gamma_1,\gamma_2,\dots)\) of integers with only finitely many non-zero terms, such that \(\gamma=0\) or
the first non-zero term of \(\gamma\) is positive. \(Q\) is closed under addition, and \(Q\cap(-Q)=\{0\}\). Let
\(e_n\in Q\) be the sequence with \(n\)-th term \(1\) and all other terms \(0\). Let
\(M=\mathbb F_1[Q\times\mathbb N]\), and put \(f_n=\chi^{(e_n,0)}\) and \(t=\chi^{(0,1)}\). Then:

- \(f_{n+1}\) divides \(f_n\), because \(e_n-e_{n+1}\in Q\);
- \(f_n\) divides no power of \(f_{n+1}\), because the first non-zero term of \(ke_{n+1}-e_n\) is \(-1\);
- the divisors of \(t^k\) are the \(t^j\) with \(j\le k\), because \(\gamma\in Q\) and \(-\gamma\in Q\) force
  \(\gamma=0\);
- \(t\) divides no power of \(f_n\), because the second coordinate of \((ke_n,0)-(0,1)\) is negative.

By Proposition 3.2(e) the first two facts give \(D(f_1)\subsetneq D(f_2)\subsetneq\cdots\). Let
\(\mathfrak w_n=\mathfrak p_{f_n}\) and \(\mathfrak z=\mathfrak p_t\) be the largest points of \(D(f_n)\) and
\(D(t)\). By Theorem 3.4 the \(\mathfrak w_n\) form a strictly increasing chain. By the third fact
\(\mathfrak z=\{\chi^{(\gamma,j)}:\gamma\neq0\}\cup\{0\}\), so \(f_n\in\mathfrak z\) for all \(n\). By the fourth
fact \(t\in\mathfrak w_n\) for all \(n\). Now consider the open set
\[
U=D(t)\cup\bigcup_{n\ge1}D(f_n).
\]
The point \(\mathfrak z\) is maximal in \(U\): a point \(\mathfrak q\in U\) with
\(\mathfrak q\supsetneq\mathfrak z\) is not in \(D(t)\), so \(f_n\notin\mathfrak q\) for some \(n\); but
\(f_n\in\mathfrak z\subseteq\mathfrak q\). It is the only maximal point: a maximal point \(\mathfrak q\) of \(U\)
that lies in \(D(t)\) satisfies \(\mathfrak q\subseteq\mathfrak z\), so \(\mathfrak q=\mathfrak z\); and a point of
\(D(f_n)\) lies in \(\mathfrak w_n\subsetneq\mathfrak w_{n+1}\in U\), so it is not maximal. But \(\mathfrak z\) is
not the largest point of \(U\), because \(t\in\mathfrak w_1\) and \(t\notin\mathfrak z\). So \(U\) has exactly one
maximal point and no largest point. By Theorem 3.4, \(U\) is not of the form \(D(f)\). It is not even homeomorphic to
the spectrum of a monoid: by Proposition 3.3 the spectrum of a non-zero monoid has a point that lies in the closure
of every point, and the closure of a point \(\mathfrak q\) in \(U\) is \(V(\mathfrak q)\cap U\).

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 2.4] states that an open subset of a monoid scheme with
a unique maximal point is affine; this fails for the set \(U\) above, so Theorem 3.4 asks for a largest point. For
finitely generated monoids the two conditions agree (Corollary 7.3).

## 4. Localization

Let \(S\) be a multiplicative subset of \(M\). If \(0\notin S\), Theorem 2.8 gives the face \(S^{\mathrm{sat}}\) and
the prime ideal \(\mathfrak p_S\). If \(0\in S\) we put \(S^{\mathrm{sat}}=M\). In both cases
\(S^{\mathrm{sat}}\) is the set of elements that divide an element of \(S\).

**Proposition 4.1 (localization).** Let \(S\) be a multiplicative subset of \(M\). On \(M\times S\) define
\((a,s)\sim(a',s')\) if \(tas'=ta's\) for some \(t\in S\).

(a) This is an equivalence relation. Write \(a/s\) for the class of \((a,s)\) and \(S^{-1}M\) for the set of
classes. The product \((a/s)(b/u)=ab/su\) is well defined and makes \(S^{-1}M\) a monoid with zero \(0/1\) and one
\(1/1\). The map \(\iota:M\to S^{-1}M\), \(a\mapsto a/1\), is a morphism, and \(\iota(s)\) is a unit for every
\(s\in S\).

(b) If \(\varphi:M\to N\) is a morphism with \(\varphi(S)\subseteq N^\times\), there is exactly one morphism
\(\varphi':S^{-1}M\to N\) with \(\varphi'\circ\iota=\varphi\). It is given by
\(\varphi'(a/s)=\varphi(a)\varphi(s)^{-1}\).

(c) \(\iota(a)=\iota(b)\) if and only if \(ta=tb\) for some \(t\in S\). The monoid \(S^{-1}M\) is zero if and only if
\(0\in S\).

(d) \(a/s\) is a unit of \(S^{-1}M\) if and only if \(a\in S^{\mathrm{sat}}\).

*Proof.* (a) The relation is reflexive and symmetric. If \(tas'=ta's\) and \(ua's''=ua''s'\) with \(t,u\in S\), then
\[
(tus')\,a\,s''=us''(tas')=us''(ta's)=ts(ua's'')=ts(ua''s')=(tus')\,a''\,s ,
\]
and \(tus'\in S\). So the relation is transitive. If \(tas'=ta's\), then \(t(ab)(s'u)=t(a'b)(su)\), so the product
does not depend on the representative of the first factor; by commutativity the same holds for the second. The
monoid axioms are inherited from \(M\). The map \(\iota\) is a morphism by the definition of the product, and
\((s/1)(1/s)=s/s=1/1\).

(b) Since \(a/s=\iota(a)\iota(s)^{-1}\), the morphism \(\varphi'\) is unique. It is well defined: from
\(tas'=ta's\) we get \(\varphi(t)\varphi(a)\varphi(s')=\varphi(t)\varphi(a')\varphi(s)\), and \(\varphi(t)\),
\(\varphi(s)\), \(\varphi(s')\) are units. It is multiplicative and preserves \(0\) and \(1\).

(c) The first statement is the definition of the relation for \(s=s'=1\). The monoid \(S^{-1}M\) is zero if and only
if \(1/1=0/1\), that is, \(t=t\cdot0=0\) for some \(t\in S\).

(d) If \(ab=s'\in S\), then \((a/s)(bs/s')=abs/ss'=1/1\). Conversely, if \((a/s)(b/u)=1/1\), then \(t\,ab=t\,su\) for
some \(t\in S\), so \(a\cdot tb\in S\) and \(a\in S^{\mathrm{sat}}\). \(\square\)

For \(f\in M\) we write \(M_f=S^{-1}M\) with \(S=\{f^n:n\ge0\}\). For a prime ideal \(\mathfrak p\) we write
\(M_{\mathfrak p}=S^{-1}M\) with \(S=M\setminus\mathfrak p\), which is a face and so a multiplicative set. If
\(S\subseteq T\) are multiplicative subsets, (b) gives a morphism \(S^{-1}M\to T^{-1}M\), \(a/s\mapsto a/s\). In
particular, for prime ideals \(\mathfrak q\subseteq\mathfrak p\) there is a morphism
\[
\rho_{\mathfrak p,\mathfrak q}:M_{\mathfrak p}\longrightarrow M_{\mathfrak q},\qquad a/s\mapsto a/s .
\]
These morphisms satisfy \(\rho_{\mathfrak p,\mathfrak p}=\mathrm{id}\) and
\(\rho_{\mathfrak q,\mathfrak r}\circ\rho_{\mathfrak p,\mathfrak q}=\rho_{\mathfrak p,\mathfrak r}\) for
\(\mathfrak r\subseteq\mathfrak q\subseteq\mathfrak p\).

**Proposition 4.2 (prime ideals of a localization).** Let \(S\) be a multiplicative subset of \(M\). The map
\(\iota^*:\operatorname{Spec}S^{-1}M\to\operatorname{Spec}M\) is a homeomorphism onto the subspace
\(\{\mathfrak p\in\operatorname{Spec}M:\mathfrak p\cap S=\emptyset\}\). Its inverse sends \(\mathfrak p\) to
\(S^{-1}\mathfrak p:=\{a/s:a\in\mathfrak p,\ s\in S\}\).

*Proof.* Let \(\mathfrak Q\) be a prime ideal of \(S^{-1}M\). Then \(\iota^{-1}(\mathfrak Q)\) is prime by Lemma 2.6,
and it is disjoint from \(S\), because \(\iota(S)\) consists of units. Now let \(\mathfrak p\) be a prime ideal of
\(M\) with \(\mathfrak p\cap S=\emptyset\). We claim that \(a/s\in S^{-1}\mathfrak p\) if and only if
\(a\in\mathfrak p\). Indeed, if \(a/s=a'/s'\) with \(a'\in\mathfrak p\), then \(tas'=ta's\in\mathfrak p\) for some
\(t\in S\); since \(ts'\in S\) is not in \(\mathfrak p\), we get \(a\in\mathfrak p\). The claim shows that
\(S^{-1}\mathfrak p\) is an ideal, that \(1/1\notin S^{-1}\mathfrak p\), that \((a/s)(b/u)\in S^{-1}\mathfrak p\)
implies \(a\in\mathfrak p\) or \(b\in\mathfrak p\), and that \(\iota^{-1}(S^{-1}\mathfrak p)=\mathfrak p\). So
\(S^{-1}\mathfrak p\) is a prime ideal that maps to \(\mathfrak p\). Conversely, for a prime ideal \(\mathfrak Q\) of
\(S^{-1}M\) we have \(a/s\in\mathfrak Q\) if and only if \(a/1\in\mathfrak Q\), because \(s/1\) is a unit. So
\(\mathfrak Q=S^{-1}(\iota^{-1}(\mathfrak Q))\). Hence the two maps are inverse bijections. The map \(\iota^*\) is
continuous. It sends \(D(a/s)=D(a/1)\) onto the intersection of \(D(a)\) with the image, so it is a homeomorphism
onto its image. \(\square\)

**Theorem 4.3 (every localization is local at a prime).** Let \(S\) be a multiplicative subset of \(M\) with
\(0\notin S\).

(a) The canonical morphism \(S^{-1}M\to(S^{\mathrm{sat}})^{-1}M=M_{\mathfrak p_S}\) is an isomorphism.

(b) The maximal ideal of \(S^{-1}M\) is \(S^{-1}\mathfrak p_S\), and its preimage in \(M\) is \(\mathfrak p_S\).

(c) If \(f\in M\) is not nilpotent, then \(M_f\cong M_{\mathfrak p_f}\). If \(\mathfrak p\) is a prime ideal, then
the maximal ideal of \(M_{\mathfrak p}\) is
\(\mathfrak pM_{\mathfrak p}:=\{a/s:a\in\mathfrak p,\ s\notin\mathfrak p\}\), its preimage in \(M\) is
\(\mathfrak p\), and the units of \(M_{\mathfrak p}\) are the fractions \(a/s\) with \(a,s\notin\mathfrak p\).

*Proof.* (a) By Proposition 4.1(d) the elements of \(S^{\mathrm{sat}}\) become units in \(S^{-1}M\). So
Proposition 4.1(b) gives morphisms \(S^{-1}M\to(S^{\mathrm{sat}})^{-1}M\) and
\((S^{\mathrm{sat}})^{-1}M\to S^{-1}M\) that are compatible with the maps from \(M\). Both composites are compatible
with the maps from \(M\), so they are identities by the uniqueness in Proposition 4.1(b). (b) The monoid \(S^{-1}M\)
is not zero. By Proposition 4.1(d) its non-units are the fractions \(a/s\) with \(a\notin S^{\mathrm{sat}}\), that
is, with \(a\in\mathfrak p_S\). By the claim in the proof of Proposition 4.2 these form the set
\(S^{-1}\mathfrak p_S\), whose preimage in \(M\) is \(\mathfrak p_S\). (c) For \(S=\{f^n\}\) we have
\(\mathfrak p_S=\mathfrak p_f\) (Corollary 2.9). For \(S=M\setminus\mathfrak p\) we have \(S^{\mathrm{sat}}=S\),
because \(S\) is a face, and \(\mathfrak p_S=\mathfrak p\). \(\square\)

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 1.1]; [Chu–Lorscheid–Santhanam 2012, Corollary 2.5].

For a ring \(R\) the localization \(R_f\) is rarely a local ring. For a monoid, \(M_f\) and \(M_{\mathfrak p_f}\)
are the same thing.

**Examples 4.4.**

(a) If \(M\neq0\), the map \(\iota:M\to M_{\mathfrak m_M}\) is an isomorphism: the set \(M\setminus\mathfrak m_M\)
consists of units already, so the identity of \(M\) has the universal property of Proposition 4.1(b).

(b) \(\mathbb F_1[x]_x=\mathbb F_1[x^{\pm1}]\), and
\(\mathbb F_1[x_1,\dots,x_n]_{x_1\cdots x_n}=\mathbb F_1[x_1^{\pm1},\dots,x_n^{\pm1}]\).

(c) Let \(M=\{0,1\}\cup\{x^a:a\ge1\}\cup\{y^b:b\ge1\}\), with \(x^ax^{a'}=x^{a+a'}\), \(y^by^{b'}=y^{b+b'}\) and
\(x^ay^b=0\). In \(M_x\) we have \(y/1=0/1\), because \(x\cdot y=x\cdot0\). So
\(M_x=\{0\}\cup\{x^n:n\in\mathbb Z\}\cong\mathbb F_1[x^{\pm1}]\), and \(\iota:M\to M_x\) is not injective.

## 5. The structure sheaf

Throughout this section \(X=\operatorname{Spec}M\). An element of \(M_{\mathfrak p}\) is called a *germ* at
\(\mathfrak p\).

**Definition 5.1.** For an open subset \(U\subseteq X\) let \(\mathcal O(U)=\mathcal O_M(U)\) be the set of all
families \(s=(s_{\mathfrak p})_{\mathfrak p\in U}\) with \(s_{\mathfrak p}\in M_{\mathfrak p}\) and
\[
\rho_{\mathfrak p,\mathfrak q}(s_{\mathfrak p})=s_{\mathfrak q}\qquad\text{for all}\ \mathfrak p,\mathfrak q\in U\
\text{with}\ \mathfrak q\subseteq\mathfrak p .
\]
For open sets \(V\subseteq U\) the restriction \(\mathcal O(U)\to\mathcal O(V)\) forgets the components outside
\(V\).

The set \(\mathcal O(U)\) is a submonoid of the product monoid \(\prod_{\mathfrak p\in U}M_{\mathfrak p}\), because
the maps \(\rho_{\mathfrak p,\mathfrak q}\) are morphisms. The restriction maps are morphisms. The monoid
\(\mathcal O(\emptyset)\) has one element.

**Theorem 5.2.**

(a) \(\mathcal O\) is a sheaf of monoids on \(X\).

(b) If an open set \(U\) has a largest point \(\mathfrak p\), then \(\mathcal O(U)\to M_{\mathfrak p}\),
\(s\mapsto s_{\mathfrak p}\), is an isomorphism. In particular \(\mathcal O(D(f))\cong M_f\) for every \(f\in M\),
and \(\mathcal O(X)\cong M\).

(c) For every \(\mathfrak p\in X\) the map from the stalk \(\mathcal O_{\mathfrak p}\) to \(M_{\mathfrak p}\) induced
by \(s\mapsto s_{\mathfrak p}\) is an isomorphism.

*Proof.* (a) Let \(U=\bigcup_iU_i\) be an open cover. Two elements of \(\mathcal O(U)\) with the same restrictions to
all \(U_i\) have the same components, so they are equal. Let \(s^i\in\mathcal O(U_i)\) be sections that agree on all
intersections \(U_i\cap U_j\). Define \(s_{\mathfrak p}=s^i_{\mathfrak p}\) for any \(i\) with
\(\mathfrak p\in U_i\); this does not depend on \(i\). If \(\mathfrak q\subseteq\mathfrak p\) are in \(U\) and
\(\mathfrak p\in U_i\), then \(\mathfrak q\in U_i\) by Proposition 3.3(b), so
\(\rho_{\mathfrak p,\mathfrak q}(s_{\mathfrak p})=\rho_{\mathfrak p,\mathfrak q}(s^i_{\mathfrak p})
=s^i_{\mathfrak q}=s_{\mathfrak q}\). So \(s\in\mathcal O(U)\), and \(s\) restricts to \(s^i\) on \(U_i\).

(b) For \(x\in M_{\mathfrak p}\) the family \((\rho_{\mathfrak p,\mathfrak q}(x))_{\mathfrak q\in U}\) lies in
\(\mathcal O(U)\), because
\(\rho_{\mathfrak q,\mathfrak r}\circ\rho_{\mathfrak p,\mathfrak q}=\rho_{\mathfrak p,\mathfrak r}\), and its
component at \(\mathfrak p\) is \(x\). Every \(s\in\mathcal O(U)\) satisfies
\(s_{\mathfrak q}=\rho_{\mathfrak p,\mathfrak q}(s_{\mathfrak p})\) for all \(\mathfrak q\in U\), so \(s\) is the
family attached to \(x=s_{\mathfrak p}\). Hence \(s\mapsto s_{\mathfrak p}\) is bijective. If \(f\) is not
nilpotent, \(D(f)\) has the largest point \(\mathfrak p_f\) (Theorem 3.4) and
\(M_{\mathfrak p_f}\cong M_f\) (Theorem 4.3). If \(f\) is nilpotent, then \(D(f)=\emptyset\) and \(M_f=0\). If
\(M\neq0\), then \(X\) has the largest point \(\mathfrak m_M\), and \(M_{\mathfrak m_M}=M\) (Example 4.4(a)).

(c) The maps \(s\mapsto s_{\mathfrak p}\) are compatible with restriction, so they induce a morphism
\(\mathcal O_{\mathfrak p}\to M_{\mathfrak p}\). It is surjective: an element of \(M_{\mathfrak p}\) is \(a/u\) with
\(u\notin\mathfrak p\), and the family of the fractions \(a/u\in M_{\mathfrak q}\), \(\mathfrak q\in D(u)\), is a
section over \(D(u)\) with value \(a/u\) at \(\mathfrak p\). It is injective: let \(s\in\mathcal O(U)\) and
\(s'\in\mathcal O(U')\) with \(\mathfrak p\in U\cap U'\) and \(s_{\mathfrak p}=s'_{\mathfrak p}\). Choose
\(f\notin\mathfrak p\) with \(D(f)\subseteq U\cap U'\), and let \(\mathfrak z=\mathfrak p_f\) be the largest point of
\(D(f)\). Since \(M_f\cong M_{\mathfrak z}\), we can write \(s_{\mathfrak z}=a/f^n\) and
\(s'_{\mathfrak z}=a'/f^n\) with \(a,a'\in M\) and the same \(n\). Then \(s_{\mathfrak q}=a/f^n\) and
\(s'_{\mathfrak q}=a'/f^n\) in \(M_{\mathfrak q}\) for all \(\mathfrak q\in D(f)\). For \(\mathfrak q=\mathfrak p\)
this gives \(t\,a\,f^n=t\,a'\,f^n\) for some \(t\notin\mathfrak p\). If \(\mathfrak q\in D(tf)\), then
\(t\notin\mathfrak q\), so \(a/f^n=a'/f^n\) in \(M_{\mathfrak q}\). So \(s\) and \(s'\) agree on the neighbourhood
\(D(tf)\) of \(\mathfrak p\). \(\square\)

For the spectrum of a ring, the structure sheaf is built in [Stacks, Tag [01HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-affine-schemes)], and the proof that \(D(f)\) has the
sections \(R_f\) needs an argument with partitions of unity. For a monoid, part (b) is a formality, because \(D(f)\)
has a largest point. The next proposition shows that Definition 5.1 agrees with the definition by local fractions
used in [Deitmar 2005, Section 2.1] and [Cortiñas–Haesemeyer–Walker–Weibel 2015, Section 1].

**Proposition 5.3 (sections are locally fractions).** Let \(U\subseteq X\) be open and let
\(s=(s_{\mathfrak p})_{\mathfrak p\in U}\) be a family with \(s_{\mathfrak p}\in M_{\mathfrak p}\). Then
\(s\in\mathcal O(U)\) if and only if every point of \(U\) has an open neighbourhood \(V\subseteq U\) and elements
\(a,u\in M\) such that \(u\notin\mathfrak q\) and \(s_{\mathfrak q}=a/u\) in \(M_{\mathfrak q}\) for all
\(\mathfrak q\in V\).

*Proof.* Suppose the local condition holds and let \(\mathfrak q\subseteq\mathfrak p\) be in \(U\). Choose \(V\),
\(a\), \(u\) for the point \(\mathfrak p\). Then \(\mathfrak q\in V\) by Proposition 3.3(b), so
\(s_{\mathfrak q}=a/u=\rho_{\mathfrak p,\mathfrak q}(a/u)=\rho_{\mathfrak p,\mathfrak q}(s_{\mathfrak p})\).
Conversely let \(s\in\mathcal O(U)\) and \(\mathfrak p\in U\). Choose \(g\) with
\(\mathfrak p\in D(g)\subseteq U\), and let \(\mathfrak z=\mathfrak p_g\). Write \(s_{\mathfrak z}=a/g^n\), using
\(M_g\cong M_{\mathfrak z}\). For \(\mathfrak q\in D(g)\) we have \(\mathfrak q\subseteq\mathfrak z\), hence
\(s_{\mathfrak q}=\rho_{\mathfrak z,\mathfrak q}(s_{\mathfrak z})=a/g^n\), and \(g^n\notin\mathfrak q\). So
\(V=D(g)\) and \(u=g^n\) work. \(\square\)

*Reference:* [Deitmar 2005, Proposition 2.1] proves the statements on stalks and global sections of Theorem 5.2 for
the sheaf of local fractions. [Cortiñas–Haesemeyer–Walker–Weibel 2015, Remark 2.12] states the description of
sections as compatible families.

**Remark 5.4 (morphisms).** Let \(\varphi:M\to N\) be a morphism, \(\mathfrak Q\in\operatorname{Spec}N\) and
\(\mathfrak p=\varphi^{-1}(\mathfrak Q)\). By Proposition 4.1(b), \(\varphi\) induces a morphism
\(\varphi_{\mathfrak Q}:M_{\mathfrak p}\to N_{\mathfrak Q}\), \(a/s\mapsto\varphi(a)/\varphi(s)\). It is local: by
Theorem 4.3(c), \(\varphi(a)/\varphi(s)\) is a unit if and only if \(\varphi(a)\notin\mathfrak Q\), that is,
\(a\notin\mathfrak p\). For an open set \(U\subseteq\operatorname{Spec}M\) the rule
\((s_{\mathfrak p})\mapsto(\varphi_{\mathfrak Q}(s_{\varphi^*\mathfrak Q}))_{\mathfrak Q}\) is a morphism
\(\mathcal O_M(U)\to\mathcal O_N((\varphi^*)^{-1}(U))\), compatible with restrictions. For
\(U=\operatorname{Spec}M\) it is \(\varphi\) itself. The lesson *Monoid schemes* takes this up: it shows that
\(M\mapsto(\operatorname{Spec}M,\mathcal O_M)\) is a contravariant equivalence from monoids to affine monoid schemes.

**Example 5.5 (the punctured plane).** Let \(M=\mathbb F_1[x,y]\). A monomial lies in a face if and only if each
variable that occurs in it does. So \(M\) has four faces and four prime ideals: \(\{0\}\), \(xM\), \(yM\) and
\(\mathfrak m=xM\cup yM\). Since \(M\) is a submonoid of the group with zero
\(G_0=\mathbb F_1[x^{\pm1},y^{\pm1}]\), every localization \(S^{-1}M\) with \(0\notin S\) embeds in \(G_0\) by
\(a/s\mapsto as^{-1}\), and the maps \(\rho\) become inclusions. We get
\[
M_{xM}=\{x^ay^b:a\ge0,\ b\in\mathbb Z\}\cup\{0\},\qquad
M_{yM}=\{x^ay^b:a\in\mathbb Z,\ b\ge0\}\cup\{0\},\qquad M_{\{0\}}=G_0 .
\]
Let \(U=X\setminus\{\mathfrak m\}=D(x)\cup D(y)=\{\{0\},xM,yM\}\). A section over \(U\) is a triple of germs at the
three points with the same image in \(G_0\). So
\[
\mathcal O(U)=M_{xM}\cap M_{yM}=M .
\]
The restriction \(\mathcal O(X)\to\mathcal O(U)\) is an isomorphism, although \(U\neq X\). The set \(U\) has two
maximal points and no largest point, so it is not of the form \(D(f)\). Exercise 4 shows that the restriction to
the punctured spectrum is not always an isomorphism.

**Example 5.6 (a disconnected open set).** Let \(M\) be the monoid of Example 4.4(c). Its faces are \(\{1\}\),
\(\{1\}\cup\{x^a\}\) and \(\{1\}\cup\{y^b\}\); the set of all non-zero elements is not a face, because \(xy=0\). So
\(X\) has three points: \(\mathfrak p_x=\{0\}\cup\{x^a\}\), \(\mathfrak p_y=\{0\}\cup\{y^b\}\) and
\(\mathfrak m=\mathfrak p_x\cup\mathfrak p_y\). We have \(D(x)=\{\mathfrak p_y\}\), \(D(y)=\{\mathfrak p_x\}\) and
\(D(x)\cap D(y)=D(xy)=\emptyset\). The open set \(U=D(x)\cup D(y)\) is a discrete space with two points, and
\[
\mathcal O(U)=M_x\times M_y\cong\mathbb F_1[x^{\pm1}]\times\mathbb F_1[y^{\pm1}] .
\]
The space \(X\) itself is connected, and it has two minimal points.

## 6. Quotients: congruences and ideals

**Definition 6.1.** A *congruence* on \(M\) is an equivalence relation \(\sim\) on \(M\) such that \(a\sim b\)
implies \(ac\sim bc\) for all \(c\in M\).

**Proposition 6.2.**

(a) Let \(\sim\) be a congruence on \(M\). The set \(M/{\sim}\) of classes \([a]\) is a monoid with
\([a][b]=[ab]\), and \(\pi:M\to M/{\sim}\), \(a\mapsto[a]\), is a surjective morphism.

(b) Let \(\varphi:M\to N\) be a morphism. The relation \(a\sim_\varphi b\iff\varphi(a)=\varphi(b)\) is a
congruence, called the *kernel congruence* of \(\varphi\), and \(\varphi\) induces an isomorphism of
\(M/{\sim_\varphi}\) onto the submonoid \(\varphi(M)\) of \(N\).

(c) Let \(\sim\) be a congruence and \(\varphi:M\to N\) a morphism such that \(a\sim b\) implies
\(\varphi(a)=\varphi(b)\). Then there is exactly one morphism \(\bar\varphi:M/{\sim}\to N\) with
\(\bar\varphi\circ\pi=\varphi\).

(d) The intersection of a non-empty family of congruences, as subsets of \(M\times M\), is a congruence. So every
subset \(R\subseteq M\times M\) lies in a smallest congruence, the congruence *generated* by \(R\).

*Proof.* (a) If \(a\sim a'\) and \(b\sim b'\), then \(ab\sim a'b\sim a'b'\). So the product is well defined, and the
monoid axioms pass to the classes. (b) If \(\varphi(a)=\varphi(b)\) then \(\varphi(ac)=\varphi(bc)\). The map
\([a]\mapsto\varphi(a)\) is a well defined injective morphism with image \(\varphi(M)\). (c) Put
\(\bar\varphi([a])=\varphi(a)\). (d) The conditions of Definition 6.1 pass to intersections, and \(M\times M\) is a
congruence containing \(R\). \(\square\)

So congruences on \(M\) describe the surjective morphisms out of \(M\), as ideals do for a ring.

**Definition 6.3.** Let \(I\) be an ideal of \(M\). Define \(a\sim_Ib\) if \(a=b\) or \(a,b\in I\). This is a
congruence. The monoid \(M/I:=M/{\sim_I}\) is the *quotient of \(M\) by the ideal \(I\)*. As a set it is
\((M\setminus I)\sqcup\{0\}\); the product of \(a,b\in M\setminus I\) is \(ab\) if \(ab\notin I\) and \(0\)
otherwise.

For example \(\mathbb F_1[x]/\langle x^n\rangle=\{0,1,x,\dots,x^{n-1}\}\) with \(x^n=0\); for \(n=2\) this is the
monoid \(\{0,1,\varepsilon\}\) of Example 1.3(f). The monoid of Example 4.4(c) is
\(\mathbb F_1[x,y]/\langle xy\rangle\). For every non-zero monoid, \(M/\mathfrak m_M=(M^\times)_0\).

**Proposition 6.4.** Let \(\sim\) be a congruence on \(M\) and let \(I_\sim=[0]\) be the class of \(0\).

(a) \(I_\sim\) is an ideal, and \(a\sim_{I_\sim}b\) implies \(a\sim b\).

(b) \(\sim\) is of the form \(\sim_I\) for an ideal \(I\) if and only if every class other than \(I_\sim\) has
exactly one element. In that case \(I=I_\sim\).

(c) A morphism \(\varphi:M\to N\) factors through \(\pi:M\to M/I\) if and only if \(\varphi(I)=\{0\}\), and the
factorization is unique.

*Proof.* (a) If \(a\sim0\) then \(ab\sim0b=0\). Two elements of \(I_\sim\) are both equivalent to \(0\). (b) The
classes of \(\sim_I\) are \(I\) and the one-element sets \(\{a\}\), \(a\notin I\). (c) If \(\varphi(I)=\{0\}\), then
\(a\sim_Ib\) implies \(\varphi(a)=\varphi(b)\), and Proposition 6.2(c) applies. Conversely \(\pi(I)=\{0\}\).
\(\square\)

**Proposition 6.5 (the spectrum of a quotient).** Let \(\sim\) be a congruence on \(M\) and \(\pi:M\to M/{\sim}\).

(a) The map \(\pi^*:\operatorname{Spec}(M/{\sim})\to\operatorname{Spec}M\) is a homeomorphism onto its image. The
image is the set of prime ideals of \(M\) that are unions of classes of \(\sim\).

(b) If \(\sim\) is \(\sim_I\) for an ideal \(I\), the image is the closed set \(V(I)\). So
\(\operatorname{Spec}(M/I)\cong V(I)\).

(c) In general the image is not closed.

*Proof.* (a) For a prime ideal \(\mathfrak Q\) of \(M/{\sim}\) the set \(\pi^{-1}(\mathfrak Q)\) is a union of
classes, and \(\mathfrak Q=\pi(\pi^{-1}(\mathfrak Q))\), because \(\pi\) is surjective. So \(\pi^*\) is injective.
Let \(\mathfrak p\) be a prime ideal of \(M\) that is a union of classes. Then \(\pi(\mathfrak p)\) is an ideal of
\(M/{\sim}\), and \(\pi^{-1}(\pi(\mathfrak p))=\mathfrak p\). So \([1]\notin\pi(\mathfrak p)\), and
\([a][b]\in\pi(\mathfrak p)\) implies \(ab\in\mathfrak p\), hence \(a\in\mathfrak p\) or \(b\in\mathfrak p\). So
\(\pi(\mathfrak p)\) is a prime ideal with \(\pi^*(\pi(\mathfrak p))=\mathfrak p\). Finally \(\pi^*\) is continuous
and maps \(D([a])\) onto the intersection of \(D(a)\) with the image. (b) A prime ideal \(\mathfrak p\) is a union
of classes of \(\sim_I\) if and only if \(I\subseteq\mathfrak p\) or \(I\cap\mathfrak p=\emptyset\). The second case
does not occur, because \(0\in I\cap\mathfrak p\). (c) See Example 6.6. \(\square\)

**Example 6.6 (the diagonal).** Let \(\Delta:\mathbb F_1[x,y]\to\mathbb F_1[t]\) be the morphism with
\(x\mapsto t\) and \(y\mapsto t\). It is surjective. Its kernel congruence identifies \(x^ay^b\) and
\(x^{a'}y^{b'}\) when \(a+b=a'+b'\), and the class of \(0\) is \(\{0\}\). The monoid \(\mathbb F_1[t]\) has two
faces, \(\{1\}\) and the set of all powers of \(t\), so it has the two prime ideals \(\langle t\rangle\) and
\(\{0\}\). Their preimages under \(\Delta\) are \(\mathfrak m=xM\cup yM\) and \(\{0\}\), with
\(M=\mathbb F_1[x,y]\). So the image of \(\Delta^*\) in the four-point space of Example 5.5 is
\(\{\{0\},\mathfrak m\}\). It is not closed, because the closure of the point
\(\{0\}\) is the whole space. After base change to \(\mathbb Z\) (Section 8) the map \(\Delta\) becomes the
surjection \(\mathbb Z[x,y]\to\mathbb Z[t]\) with kernel \((x-y)\), whose spectrum is the closed diagonal of the
affine plane. *Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Remark 2.7.1].

**Remark 6.7 (how quotients differ from the ring case).**

1. In a ring, congruences and ideals are the same thing: \(a\equiv b\) if and only if \(a-b\in I\). A monoid has no
   subtraction, and a congruence is not determined by the class of \(0\). The kernel congruence of \(\Delta\) and
   the kernel congruence of \(\mathbb F_1[x]\to\mathbb F_1\), \(x\mapsto1\), both have \(I_\sim=\{0\}\), and neither
   morphism is injective. A morphism is injective if and only if its kernel congruence is equality;
   \(\varphi^{-1}(0)=\{0\}\) is not enough. [Deitmar 2013, Introduction] puts it this way: for a ring all
   congruences come from ideals, and a monoid has far more congruences than ideals.
2. The quotients by ideals are the special congruences of Proposition 6.4(b). The spectrum of such a quotient is a
   closed subset of \(\operatorname{Spec}M\) (Proposition 6.5). This property does not single them out: the morphism
   \(\mathbb F_{1^2}\to\mathbb F_1\) that sends \(-1\) to \(1\) is a quotient by a congruence that does not come
   from an ideal, and both spectra are one point.
3. The sum of two ideals of a ring corresponds to the union of two ideals of a monoid (Lemma 2.2). The quotient
   \(M/(I\cup J)\) is also the quotient of \(M/I\) by the image of \(J\): both are obtained from \(M\) by collapsing
   \(I\cup J\) to \(0\).
4. If \(\mathfrak p\) is a prime ideal, then \(M/\mathfrak p\) is without zero divisors, because
   \(M\setminus\mathfrak p\) is closed under multiplication. But a monoid without zero divisors need not embed in a
   group with zero (Section 7), so \(M/\mathfrak p\) is a weaker analogue of an integral domain.
5. After base change to \(\mathbb Z\), a quotient by an ideal becomes the quotient of \(\mathbb Z[M]\) by an ideal
   spanned by elements of \(M\), and a quotient by a congruence becomes the quotient by an ideal spanned by
   differences \(a-b\) of elements of \(M\) (Proposition 8.4).

Exercise 3 lists all quotients of \(\mathbb F_1[x]\).

**Remark 6.8 (prime congruences and dimension).** The space \(\operatorname{Spec}M\) has few points, and two things
are lost. It does not see closed conditions: the image of the diagonal in Example 6.6 is not closed. And it does not
see dimension: a group with zero \(G_0\) has the single prime ideal \(\{0\}\), so its spectrum is a point. This
holds also for \(G=\mathbb Z^n\), although the corresponding ring over \(\mathbb C\) (Section 8) is the ring of
Laurent polynomials in \(n\) variables, of dimension \(n\). [Jarra 2023a, Introduction] makes this point for the
\(n\)-torus over any group with zero.

A second space, built from congruences, repairs both defects. A congruence \(\sim\) on \(M\) is *prime* if
\(M/{\sim}\) is cancellative (Definition 7.4), that is, if \(1\not\sim0\) and \(ab\sim ac\) implies \(a\sim0\) or
\(b\sim c\). The *congruence space* \(\operatorname{Cong}M\) is the set of prime congruences on \(M\), with the
topology generated by the sets \(U_{a,b}=\{\sim\ :\ a\not\sim b\}\) for \(a,b\in M\)
[Lorscheid–Ray 2024, Definitions 2.3 and 2.9]. The same space, for a class of objects that contains monoids and
rings, is the starting point of [Deitmar 2013, Section 2.1]. Three facts are elementary.

1. If \(\sim\) is prime, then \(I_\sim\) is a prime ideal: \(1\notin I_\sim\), and \(ab\sim0=a0\) with
   \(a\not\sim0\) gives \(b\sim0\). The map \(\operatorname{Cong}M\to\operatorname{Spec}M\),
   \(\sim\ \mapsto I_\sim\), is continuous, because the preimage of \(D(a)\) is \(U_{a,0}\). It is surjective,
   because the kernel congruence of \(\chi_{\mathfrak p}:M\to\mathbb F_1\) (Proposition 2.7) is prime and has
   \(I_\sim=\mathfrak p\).
2. Let \(\varphi:M\to N\) be a morphism and \(\approx\) a prime congruence on \(N\). The kernel congruence of
   \(M\to N/{\approx}\) is prime, because its quotient is isomorphic to a submonoid of \(N/{\approx}\)
   (Proposition 6.2), and a submonoid of a cancellative monoid is cancellative. This defines a map
   \(\operatorname{Cong}N\to\operatorname{Cong}M\). It is continuous, because the preimage of \(U_{a,b}\) is
   \(U_{\varphi(a),\varphi(b)}\). For the diagonal \(\Delta\) of Example 6.6 its image is closed. Indeed, the kernel
   congruence of \(\Delta\) is generated by the pair \((x,y)\): replace \(y\) by \(x\) in a monomial, one factor at a
   time. So by Proposition 6.2 the image consists of the prime congruences on
   \(\mathbb F_1[x,y]\) with \(x\sim y\), and this set is the complement of \(U_{x,y}\). *Reference:*
   [Lorscheid–Ray 2024, Example 2.15].
3. On a group with zero \(G_0\) the prime congruences correspond to the subgroups \(H\) of \(G\), by: \(a\sim_Hb\)
   if \(a=b=0\), or \(a,b\neq0\) and \(ab^{-1}\in H\). Indeed, if \(\sim\) is prime and \(g\sim0\) for some
   \(g\in G\), then \(1=g^{-1}g\sim0\). So no element of \(G\) is equivalent to \(0\), and on \(G\) the relation is
   the coset relation of the subgroup \(H=\{g:g\sim1\}\). Conversely \(G_0/{\sim_H}=(G/H)_0\) is cancellative. So
   \(\operatorname{Cong}((\mathbb Z^n)_0)\) is the set of subgroups of \(\mathbb Z^n\). It contains chains
   \(0\subset H_1\subset\dots\subset H_n\) with \(H_i\) of rank \(i\), while the spectrum is a point.

For an arbitrary monoid, the fibre of \(\operatorname{Cong}M\to\operatorname{Spec}M\) over \(\mathfrak p\) is the
congruence space of the group with zero \(M_{\mathfrak p}/\mathfrak pM_{\mathfrak p}\)
[Lorscheid–Ray 2024, Proposition 2.18]. A space with the expected dimension is obtained by restricting the
congruences and enlarging the base. [Jarra 2023a, Definitions 3.1 and 5.2] calls a monoid a *domain* if it is
isomorphic to a submonoid of \((K,\cdot)\) for a field \(K\), calls a congruence *strong* if its quotient is a
domain, and calls a group with zero \(F\) *algebraically closed* if for every \(\alpha\in F^\times\) and
\(n\ge1\) the equation \(x^n=\alpha\) has exactly \(n\) solutions in \(F\). An example is the group of all complex
roots of unity, with zero. For such an \(F\) and a fan \(\Sigma\), [Jarra 2023a, Theorem A] states: the space of
those strong congruences on the toric monoid scheme of \(\Sigma\) over \(F\) for which \(F\) maps injectively to the
quotient is catenary, and its Krull dimension is that of the complex toric variety of \(\Sigma\). For the
\(n\)-torus over \(F\) these congruences are the ones generated by relations \(X^{z_i}\sim\lambda_i\),
\(i=1,\dots,c\), where \(z_1,\dots,z_c\) is part of a basis of \(\mathbb Z^n\) and \(\lambda_i\in F^\times\)
[Jarra 2023a, Proposition 6.1]. The proof of Theorem A in that work (Theorems 5.13 and 5.15 of the third arXiv
version) uses [Jarra 2023a, Lemma 5.12]: if \(G\) is a torsion-free abelian group of finite rank and \(H_1,H_2\) are
subgroups with \(H_1\cap H_2=\{0\}\) such that \(G/H_1\) and \(G/H_2\) are torsion-free, then \(G/(H_1\oplus H_2)\) is
torsion-free. This lemma is false: for \(G=\mathbb Z^2\), \(H_1=\mathbb Z(1,0)\) and \(H_2=\mathbb Z(1,2)\) both
quotients \(G/H_i\) are infinite cyclic, but \(G/(H_1\oplus H_2)\cong\mathbb Z/2\mathbb Z\). So the proof of Theorem A
in that version is incomplete; the example does not refute Theorem A. Theorem A and Proposition 6.1 are proved in *Monoid schemes*,
Section 6.6 (Theorem 6.19 and Corollary 6.20), with a different argument; this lesson does not use them.

## 7. Finiteness and regularity conditions

### Finitely generated monoids

**Definition 7.1.** A subset \(\Gamma\subseteq M\) *generates* \(M\) if every non-zero element of \(M\) is a product
of finitely many elements of \(\Gamma\); the empty product is \(1\). The monoid \(M\) is *finitely generated* if a
finite set generates it. By Proposition 1.4 this holds if and only if there is a surjective morphism
\(\mathbb F_1[x_1,\dots,x_n]\to M\) for some \(n\).

**Proposition 7.2.** Let \(\Gamma\) generate \(M\).

(a) For every prime ideal \(\mathfrak p\) we have \(\mathfrak p=\langle\Gamma\cap\mathfrak p\rangle\), and
\(M\setminus\mathfrak p\) is the set of all products of elements of \(\Gamma\setminus\mathfrak p\). The map
\(\mathfrak p\mapsto\Gamma\cap\mathfrak p\) is injective. If \(\Gamma\) is finite, \(M\) has at most
\(2^{|\Gamma|}\) prime ideals.

(b) Let \(\Gamma\) be finite, let \(\mathfrak p\) be a prime ideal, and let \(f\) be the product of the elements of
\(\Gamma\setminus\mathfrak p\). Then \(D(f)=\Lambda(\mathfrak p)\), \(\mathfrak p=\mathfrak p_f\) and
\(M_{\mathfrak p}\cong M_f\).

(c) If \(\Gamma\) is finite, every localization \(S^{-1}M\) is isomorphic, compatibly with the maps from \(M\), to
\(M_f\) for some \(f\in M\), and it is finitely generated.

*Proof.* (a) Let \(a\in\mathfrak p\), \(a\neq0\), and write \(a=\gamma_1\cdots\gamma_k\) with
\(\gamma_i\in\Gamma\). Here \(k\ge1\), because \(1\notin\mathfrak p\). Since \(\mathfrak p\) is prime, some
\(\gamma_i\) lies in \(\mathfrak p\), and \(a\in\gamma_iM\). So
\(\mathfrak p\subseteq\langle\Gamma\cap\mathfrak p\rangle\), and the other inclusion is clear. If
\(a\notin\mathfrak p\), then \(a\neq0\) and \(a=\gamma_1\cdots\gamma_k\) with no \(\gamma_i\) in \(\mathfrak p\),
because \(\mathfrak p\) is an ideal. Conversely a product of elements outside \(\mathfrak p\) is outside
\(\mathfrak p\). The remaining statements follow.

(b) We have \(f\notin\mathfrak p\). If \(\mathfrak q\in D(f)\), then no element of \(\Gamma\setminus\mathfrak p\)
lies in \(\mathfrak q\), since each of them divides \(f\). So
\(\Gamma\cap\mathfrak q\subseteq\Gamma\cap\mathfrak p\), and
\(\mathfrak q=\langle\Gamma\cap\mathfrak q\rangle\subseteq\mathfrak p\) by (a). Conversely
\(\mathfrak q\subseteq\mathfrak p\) implies \(f\notin\mathfrak q\). So \(D(f)=\Lambda(\mathfrak p)\). Theorem 3.4
gives \(\mathfrak p=\mathfrak p_f\), and Theorem 4.3(c) gives \(M_f\cong M_{\mathfrak p}\).

(c) If \(0\in S\), then \(S^{-1}M=0=M_f\) for \(f=0\). Otherwise \(S^{-1}M\cong M_{\mathfrak p_S}\) by
Theorem 4.3(a), and \(M_{\mathfrak p_S}\cong M_f\) by (b). The monoid \(M_f\) is generated by the images of the
elements of \(\Gamma\) and by \(1/f\). \(\square\)

*Reference:* [Chu–Lorscheid–Santhanam 2012, Lemma 2.9 and Proposition 2.10];
[Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 1.5].

**Corollary 7.3 (finite spectra).** Let \(M\) be finitely generated and \(X=\operatorname{Spec}M\). Then \(X\) is
finite. A subset of \(X\) is open if and only if it is stable under generization. Every set \(\Lambda(\mathfrak p)\)
is open. A non-empty open set is of the form \(D(f)\) if and only if it has exactly one maximal element.

*Proof.* \(X\) is finite by Proposition 7.2(a), and \(\Lambda(\mathfrak p)\) is open by Proposition 7.2(b). Open sets
are stable under generization (Proposition 3.3). A subset \(U\) that is stable under generization is the union of
the open sets \(\Lambda(\mathfrak p)\), \(\mathfrak p\in U\). In a finite partially ordered set every element lies
below a maximal one; so a subset with exactly one maximal element has a largest element, and Theorem 3.4 applies.
\(\square\)

So the spectrum of a finitely generated monoid is a finite partially ordered set, with the topology whose open sets
are the subsets closed under passing to smaller elements. Example 3.6 shows that the last statement of the corollary
needs finite generation.

### Cancellative monoids and the group completion

**Definition 7.4.** A monoid \(M\) is *cancellative*, or *integral*, if \(M\neq0\) and
\[
ab=ac\ \text{and}\ a\neq0\quad\Longrightarrow\quad b=c .
\]

Both words are in use: [Chu–Lorscheid–Santhanam 2012, Section 2.1] says integral, and
[Cortiñas–Haesemeyer–Walker–Weibel 2015, Section 1] says cancellative. For a commutative monoid \(A\) without
zero, [Deitmar 2008, Introduction] calls \(A\) integral if \(ab=ac\) implies \(b=c\); this holds if and only if
\(A_0\) is cancellative in the sense of Definition 7.4. A cancellative monoid is without zero divisors:
\(ab=0=a0\) with \(a\neq0\) gives \(b=0\). The converse fails: in \(\{0,e,1\}\) we have \(e\cdot e=e\cdot1\).

**Proposition 7.5 (group completion).** Let \(M\) be a monoid without zero divisors, and let
\(M^{\mathrm{gp}}=M_{\{0\}}\) be the localization at the prime ideal \(\{0\}\), that is, at \(S=M\setminus\{0\}\).

(a) \(M^{\mathrm{gp}}=G_0\), where \(G=(M^{\mathrm{gp}})^\times\) is the abelian group of the fractions \(a/s\) with
\(a,s\neq0\).

(b) Let \(H\) be an abelian group and \(\varphi:M\to H_0\) a morphism with \(\varphi^{-1}(0)=\{0\}\). Then there is
exactly one morphism \(\varphi':M^{\mathrm{gp}}\to H_0\) with \(\varphi'\circ\iota=\varphi\), and it restricts to a
group homomorphism \(G\to H\).

(c) \(\iota:M\to M^{\mathrm{gp}}\) is injective if and only if \(M\) is cancellative. Hence a monoid is cancellative
if and only if it is isomorphic to a submonoid of \(G_0\) for some abelian group \(G\).

*Proof.* (a) By the definition of the relation in Proposition 4.1, \(a/s=0/1\) if and only if \(ta=0\) for some
\(t\neq0\), that is, \(a=0\). For \(a\neq0\) the fraction \(a/s\) has the inverse \(s/a\). (b) We have
\(\varphi(S)\subseteq H=(H_0)^\times\), so Proposition 4.1(b) applies, and a morphism maps units to units. (c) By
Proposition 4.1(c), \(\iota(a)=\iota(b)\) if and only if \(ta=tb\) for some \(t\neq0\). If \(M\) is a submonoid of
\(G_0\), then \(M\neq0\), and \(ab=ac\) with \(a\neq0\) gives \(b=c\) after multiplication by \(a^{-1}\) in \(G_0\).
\(\square\)

The monoid \(M^{\mathrm{gp}}\) is the *group completion* of \(M\). For a cancellative monoid we regard \(M\) as a
submonoid of \(M^{\mathrm{gp}}\). All localizations \(S^{-1}M\) with \(0\notin S\) are then submonoids of
\(M^{\mathrm{gp}}\) as well, by \(a/s\mapsto as^{-1}\). More generally, let \(M\) be a submonoid of a group with zero
\(H_0\), and let \(0\notin S\). Then \(a/s\mapsto as^{-1}\) is an injective morphism \(S^{-1}M\to H_0\): it exists by
Proposition 4.1(b), and \(as^{-1}=a's'^{-1}\) gives \(as'=a's\), hence \(a/s=a'/s'\). In particular
\(M^{\mathrm{gp}}\) is the submonoid of \(H_0\) that consists of \(0\) and the fractions \(ab^{-1}\) with
\(a,b\in M\setminus\{0\}\). Example 5.5 used this for \(M=\mathbb F_1[x,y]\).

**Definition 7.6.** A monoid \(M\) is *torsion-free* if \(a^n=b^n\) for some \(n\ge1\) implies \(a=b\).

**Proposition 7.7.** Let \(M\) be cancellative, with \(M^{\mathrm{gp}}=G_0\). Then \(M\) is torsion-free if and only
if the group \(G\) is torsion-free.

*Proof.* Let \(G\) be torsion-free and \(a^n=b^n\) in \(M\). If \(a=0\), then \(b^n=0\), so \(b=0\). Otherwise
\(b\neq0\), and \((a/b)^n=1\) in \(G\), so \(a/b=1\) and \(a=b\). Conversely let \(M\) be torsion-free and
\(g=a/b\in G\) with \(g^n=1\). Then \(a^n=b^n\) in \(M\), so \(a=b\) and \(g=1\). \(\square\)

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Section 1] defines torsion-free monoids and notes the first
implication.

The monoid \(\mathbb F_{1^n}\) is cancellative, and it is torsion-free only for \(n=1\). The monoid
\(\{0,e,1\}\) is torsion-free and not cancellative. A torsion-free monoid has no nilpotent element other than
\(0\), since \(a^n=0=0^n\) gives \(a=0\).

### Normal monoids

**Definition 7.8.** Let \(M\) be cancellative. The *normalization* of \(M\) is
\[
M_{\mathrm{nor}}=\{\alpha\in M^{\mathrm{gp}}:\alpha^n\in M\ \text{for some}\ n\ge1\}.
\]
\(M\) is *normal* if \(M_{\mathrm{nor}}=M\): every \(\alpha\in M^{\mathrm{gp}}\) with a power in \(M\) lies in
\(M\).

**Proposition 7.9.** Let \(M\) be cancellative.

(a) \(M_{\mathrm{nor}}\) is a submonoid of \(M^{\mathrm{gp}}\) that contains \(M\).

(b) If \(N\) is a submonoid with \(M\subseteq N\subseteq M^{\mathrm{gp}}\), then \(N\) is cancellative and the
inclusion induces an isomorphism \(N^{\mathrm{gp}}\cong M^{\mathrm{gp}}\).

(c) \(M_{\mathrm{nor}}\) is normal, and it is contained in every normal monoid \(N\) with
\(M\subseteq N\subseteq M^{\mathrm{gp}}\).

*Proof.* (a) If \(\alpha^n\in M\) and \(\beta^m\in M\), then \((\alpha\beta)^{nm}=(\alpha^n)^m(\beta^m)^n\in M\).
(b) \(N\) is cancellative by Proposition 7.5(c). By Proposition 7.5(b) the inclusion induces a morphism
\(N^{\mathrm{gp}}\to M^{\mathrm{gp}}\), \(a/b\mapsto ab^{-1}\). It is injective, because \(ab^{-1}=a'b'^{-1}\) gives
\(ab'=a'b\). It is surjective, because every non-zero element of \(M^{\mathrm{gp}}\) is a fraction of elements of
\(M\subseteq N\). (c) By (b), \(N\) is normal if and only if every \(\alpha\in M^{\mathrm{gp}}\) with a power in
\(N\) lies in \(N\). If \(\alpha^n\in M_{\mathrm{nor}}\), then \((\alpha^n)^m\in M\) for some \(m\), so
\(\alpha\in M_{\mathrm{nor}}\). If \(N\) is normal and \(\alpha\in M_{\mathrm{nor}}\), then
\(\alpha^n\in M\subseteq N\), so \(\alpha\in N\). \(\square\)

Passing to the normalization does not change the spectrum. This holds in a more general form, without any
cancellation.

**Theorem 7.10 (extensions by roots).** Let \(M\) be a submonoid of a monoid \(N\) such that every \(b\in N\) has a
power \(b^n\in M\) with \(n\ge1\). Then
\[
\operatorname{Spec}N\longrightarrow\operatorname{Spec}M,\qquad\mathfrak Q\mapsto\mathfrak Q\cap M,
\]
is a homeomorphism. Its inverse sends \(\mathfrak p\) to
\(\mathfrak p'=\{b\in N:b^n\in\mathfrak p\ \text{for some}\ n\ge1\}\). In particular
\(\operatorname{Spec}M_{\mathrm{nor}}\to\operatorname{Spec}M\) is a homeomorphism for every cancellative monoid
\(M\).

*Proof.* The map is \(j^*\) for the inclusion \(j:M\to N\), so it is continuous. Let \(\mathfrak p\) be a prime
ideal of \(M\). We show that \(\mathfrak p'\) is a prime ideal of \(N\). It contains \(0\). Let
\(b\in\mathfrak p'\) with \(b^n\in\mathfrak p\), and let \(c\in N\) with \(c^m\in M\). Then
\((bc)^{nm}=(b^n)^m(c^m)^n\in\mathfrak p\), so \(bc\in\mathfrak p'\). Since \(1\notin\mathfrak p\), we have
\(1\notin\mathfrak p'\). Let \(b,c\in N\) with \(bc\in\mathfrak p'\), say \((bc)^n\in\mathfrak p\). Choose
\(k\ge1\) with \(b^k\in M\) and \(c^k\in M\). Then \((b^k)^n(c^k)^n=((bc)^n)^k\in\mathfrak p\), and both factors lie
in \(M\). So \((b^k)^n\in\mathfrak p\) or \((c^k)^n\in\mathfrak p\), that is, \(b\in\mathfrak p'\) or
\(c\in\mathfrak p'\). Next, \(\mathfrak p'\cap M=\mathfrak p\): for \(b\in M\), \(b^n\in\mathfrak p\) if and only if
\(b\in\mathfrak p\). Finally let \(\mathfrak Q\) be a prime ideal of \(N\) and \(\mathfrak p=\mathfrak Q\cap M\). If
\(b\in\mathfrak Q\), choose \(n\) with \(b^n\in M\); then \(b^n\in\mathfrak Q\cap M=\mathfrak p\), so
\(b\in\mathfrak p'\). If \(b\in\mathfrak p'\), then \(b^n\in\mathfrak p\subseteq\mathfrak Q\), so
\(b\in\mathfrak Q\). Hence \(\mathfrak Q=\mathfrak p'\), and the two maps are inverse bijections. The map is open:
for \(b\in N\) with \(b^n\in M\) we have \(D(b)=D(b^n)\) in \(\operatorname{Spec}N\), and its image is the set
\(D(b^n)\) of \(\operatorname{Spec}M\). \(\square\)

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Remark 1.6.1] treats the case \(N=M_{\mathrm{nor}}\).

**Example 7.11 (the cusp monoid).** Let \(M=\{0\}\cup\{t^n:n=0\ \text{or}\ n\ge2\}\), a submonoid of
\(\mathbb F_1[t]\). It is generated by \(t^2\) and \(t^3\). It is cancellative, with
\(M^{\mathrm{gp}}=\mathbb F_1[t^{\pm1}]\), since \(t=t^3/t^2\); so it is torsion-free. It is not normal: \(t\) lies in
\(M^{\mathrm{gp}}\) and \(t^2\in M\), but \(t\notin M\). A power \(t^{kn}\) with \(n\ge1\) lies in \(M\) only if
\(k\ge0\), so \(M_{\mathrm{nor}}=\mathbb F_1[t]\). By Theorem 7.10, \(\operatorname{Spec}M\) has two points, like
\(\operatorname{Spec}\mathbb F_1[t]\).

## 8. The monoid ring and the map from Spec Z[M] to Spec M

### The monoid ring

**Definition 8.1.** Let \(k\) be a ring and \(M\) a monoid. The *monoid algebra* \(k[M]\) is the free \(k\)-module
with basis \(M\setminus\{0\}\), with the \(k\)-bilinear multiplication that extends the product of \(M\); a product
of basis elements that is \(0\) in \(M\) is \(0\) in \(k[M]\). It is a commutative \(k\)-algebra. The map
\(M\to k[M]\) that sends \(a\neq0\) to the basis element \(a\) and \(0\) to \(0\) is a morphism of monoids
\(M\to(k[M],\cdot)\). If \(k\neq0\) it is injective, and we regard \(M\) as a subset of \(k[M]\). For an ideal
\(I\) of \(M\) we write \(k[I]\) for the \(k\)-span of \(I\setminus\{0\}\); it is an ideal of \(k[M]\). The ring
\(\mathbb Z[M]\) is the *base change of \(M\) to the integers*.

In other words, \(k[M]\) is the usual monoid algebra of \(M\) modulo the ideal spanned by the zero of \(M\).

**Examples 8.2.** \(k[\mathbb F_1[P]]\) is the usual monoid algebra \(k[P]\) of the additive monoid \(P\). In
particular \(k[\mathbb F_1[x_1,\dots,x_n]]=k[x_1,\dots,x_n]\), \(k[G_0]\) is the group algebra \(k[G]\), and
\(\mathbb Z[\mathbb F_1]=\mathbb Z\). Further \(\mathbb Z[\mathbb F_{1^n}]=\mathbb Z[x]/(x^n-1)\) and
\(\mathbb Z[\{0,1,\varepsilon\}]=\mathbb Z[\varepsilon]/(\varepsilon^2)\). The ring \(\mathbb Z[\{0,e,1\}]\) has
the basis \(1,e\) with \(e^2=e\), so it is isomorphic to \(\mathbb Z\times\mathbb Z\) by \(1\mapsto(1,1)\),
\(e\mapsto(0,1)\).

**Proposition 8.3 (adjunction).** Let \(R\) be a \(k\)-algebra. Restriction to \(M\) is a bijection
\[
\operatorname{Hom}_{k\text{-alg}}(k[M],R)\longrightarrow\operatorname{Hom}(M,(R,\cdot)).
\]
For \(k=\mathbb Z\): ring homomorphisms \(\mathbb Z[M]\to R\) are the same as monoid morphisms \(M\to(R,\cdot)\).

*Proof.* A homomorphism of \(k\)-algebras restricts to a morphism of monoids, and it is determined by its values on
the basis. A morphism \(\psi:M\to(R,\cdot)\) extends \(k\)-linearly from the basis. The extension is multiplicative,
because \(\psi(ab)=\psi(a)\psi(b)\) also when \(ab=0\). \(\square\)

*Reference:* [Deitmar 2005, Theorem 1.1], for monoids without zero.

**Proposition 8.4 (localization and quotients).**

(a) For a multiplicative subset \(S\subseteq M\) there is a canonical isomorphism of \(k\)-algebras
\(S^{-1}k[M]\cong k[S^{-1}M]\).

(b) For a congruence \(\sim\) on \(M\) let \(J_\sim\subseteq k[M]\) be the \(k\)-span of the elements \(a-b\) with
\(a\sim b\). Then \(J_\sim\) is an ideal and \(k[M/{\sim}]\cong k[M]/J_\sim\). For an ideal \(I\) of \(M\) this
gives \(k[M/I]\cong k[M]/k[I]\).

*Proof.* (a) The homomorphism \(k[M]\to k[S^{-1}M]\) induced by \(\iota\) sends \(S\) to units, so it factors
through a homomorphism \(u:S^{-1}k[M]\to k[S^{-1}M]\) [Stacks, Tag [00CP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-universal-property-localization)]. The morphism of monoids
\(M\to(S^{-1}k[M],\cdot)\) sends \(S\) to units. By Proposition 4.1(b) it extends to \(S^{-1}M\), and by
Proposition 8.3 to a homomorphism \(v:k[S^{-1}M]\to S^{-1}k[M]\). Both \(u\circ v\) and \(v\circ u\) fix the images
of \(M\) and the inverses of the elements of \(S\). These generate the two algebras, so \(u\) and \(v\) are inverse
isomorphisms.

(b) If \(a\sim b\) and \(c\in M\), then \(c(a-b)=ca-cb\) with \(ca\sim cb\); so \(J_\sim\) is an ideal. The
surjective homomorphism \(k[M]\to k[M/{\sim}]\) induced by \(\pi\) vanishes on \(J_\sim\). Define a \(k\)-linear map
\(\sigma:k[M/{\sim}]\to k[M]/J_\sim\) on the basis by \([a]\mapsto a+J_\sim\) for \([a]\neq[0]\). It is well
defined, because \(a\sim a'\) gives \(a-a'\in J_\sim\). The composite
\(k[M]/J_\sim\to k[M/{\sim}]\to k[M]/J_\sim\) is the identity: it fixes \(a+J_\sim\) if \(a\not\sim0\), and if
\(a\sim0\) then \(a=a-0\in J_\sim\). So \(k[M]/J_\sim\to k[M/{\sim}]\) is injective, hence an isomorphism. For
\(\sim\,=\,\sim_I\) the span of the differences \(a-b\) with \(a,b\in I\) is \(k[I]\). \(\square\)

*Reference:* [Chu–Lorscheid–Santhanam 2012, Lemma 2.7] and [Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 5.5] for
(a).

So ideals of \(M\) correspond to ideals of \(k[M]\) spanned by monomials, and congruences to ideals spanned by
binomials and monomials. For the diagonal of Example 6.6, \(J_\sim\) is the ideal generated by \(x-y\).

**Theorem 8.5 (properties of \(M\) and of \(k[M]\)).** Let \(k\neq0\) be a ring and \(M\) a monoid.

(a) \(M\) is finitely generated if and only if \(k[M]\) is a finitely generated \(k\)-algebra.

(b) \(k[M]\) is an integral domain if and only if \(k\) is an integral domain and \(M\) is cancellative and
torsion-free.

(c) If \(k[M]\) is a normal domain, then \(M\) is normal and torsion-free.

*Proof.* (a) If \(\Gamma\) generates \(M\), it generates \(k[M]\) as a \(k\)-algebra. Conversely let
\(g_1,\dots,g_r\) generate \(k[M]\). Each \(g_j\) is a \(k\)-linear combination of finitely many elements of \(M\).
Let \(\Gamma\) be the finite set of all elements of \(M\) that occur, and let \(M'\subseteq M\) be the submonoid
generated by \(\Gamma\). The \(k\)-span of \(M'\setminus\{0\}\) is a subalgebra that contains all \(g_j\), so it is
\(k[M]\). Since \(M\setminus\{0\}\) is a basis and \(k\neq0\), this forces \(M'=M\).

(b) Let \(k[M]\) be a domain. Then \(M\neq0\), and \(k\) is a domain, being a subring of \(k[M]\). If \(ab=ac\) in
\(M\) with \(a\neq0\), then \(a(b-c)=0\) in \(k[M]\), so \(b=c\). Hence \(M\) is cancellative. Suppose that \(M\) is
not torsion-free. Choose \(a\neq b\) in \(M\) such that \(a^n=b^n\) for some \(n\ge1\), and let \(n\) be the
smallest such exponent for this pair. Then \(n\ge2\). Neither \(a\) nor \(b\) is \(0\): if \(b=0\) then \(a^n=0\)
and \(a=0\), because \(M\) is without zero divisors. In \(k[M]\) we have
\[
0=a^n-b^n=(a-b)(c_0+c_1+\dots+c_{n-1}),\qquad c_i=a^{n-1-i}b^i .
\]
The \(c_i\) are non-zero elements of \(M\). They are pairwise different: if \(c_i=c_j\) with \(i<j\), cancelling
\(a^{n-1-j}b^i\) gives \(a^{j-i}=b^{j-i}\) with \(1\le j-i<n\), against the choice of \(n\). So
\(c_0+\dots+c_{n-1}\) is a sum of \(n\) different basis elements, and it is not zero. Also \(a-b\neq0\). This
contradicts the assumption that \(k[M]\) is a domain.

Conversely let \(k\) be a domain and \(M\) cancellative and torsion-free. Then \(M\subseteq G_0=M^{\mathrm{gp}}\)
with \(G\) torsion-free (Proposition 7.7), and \(k[M]\) is a subring of the group algebra \(k[G]\). Let
\(x,y\in k[G]\) be non-zero. The finitely many elements of \(G\) that occur in \(x\) and \(y\) generate a subgroup
\(G'\). It is finitely generated and torsion-free, hence \(G'\cong\mathbb Z^r\) [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. So \(x\) and
\(y\) lie in \(k[G']\cong k[t_1^{\pm1},\dots,t_r^{\pm1}]\), which is a localization of a polynomial ring over a
domain. Hence \(xy\neq0\).

(c) Recall that a domain is normal if it is integrally closed in its fraction field [Stacks, Tag [0309](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-domain-normal)]. By (b),
\(M\) is cancellative and torsion-free. Let \(G_0=M^{\mathrm{gp}}\). By Proposition 8.4(a),
\(k[G]=k[M^{\mathrm{gp}}]\) is a localization of \(k[M]\), so it lies in the fraction field \(K\) of \(k[M]\). Let
\(\alpha\in G\) with \(\alpha^n\in M\). Then \(\alpha\in K\) is a root of the monic polynomial \(X^n-\alpha^n\) over
\(k[M]\), so \(\alpha\in k[M]\). Now \(\alpha\) is an element of the basis \(G\) of \(k[G]\), and \(k[M]\) is the
\(k\)-span of the basis elements in \(M\setminus\{0\}\). Since \(k\neq0\), this gives \(\alpha\in M\). \(\square\)

*Reference:* [Chu–Lorscheid–Santhanam 2012, Lemma 2.11] for (a).
[Cortiñas–Haesemeyer–Walker–Weibel 2015, Lemma 5.10] proves that \(k[M]\) is a domain when \(k\) is a domain and
\(M\) is cancellative with torsion-free group completion. A converse of (c) for finitely generated \(M\) is quoted
in Section 12, for coefficient rings that contain a field and for \(k=\mathbb Z\).

Together with Proposition 8.4(b), part (b) decides when a prime ideal of \(M\) spans a prime ideal of \(k[M]\): for
\(\mathfrak p\in\operatorname{Spec}M\), the ideal \(k[\mathfrak p]\) is prime if and only if \(k\) is a domain and
\(M/\mathfrak p\) is cancellative and torsion-free. For \(M=\{0,e,1\}\) and \(\mathfrak p=\{0\}\) it is not: the zero
ideal of \(\mathbb Z\times\mathbb Z\) is not prime.

**Corollary 8.6.** Let \(M\) be finitely generated. Then every ideal of \(M\) is generated by finitely many
elements, and every ascending chain of ideals of \(M\) becomes stationary.

*Proof.* The ring \(\mathbb Z[M]\) is finitely generated, hence Noetherian [Stacks, Tag [00FN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-permanence)]. Let \(I\) be an ideal
of \(M\). The ideal \(\mathbb Z[I]\) is generated by finitely many elements \(g_1,\dots,g_r\). Each \(g_j\) is a
\(\mathbb Z\)-linear combination of finitely many elements of \(I\). Let \(T\subseteq I\) be the finite set of all
elements that occur, and \(J=\langle T\rangle\subseteq I\). Then \(\mathbb Z[J]\) is an ideal of \(\mathbb Z[M]\)
that contains all \(g_j\), so \(\mathbb Z[J]=\mathbb Z[I]\) and \(J=I\). The union of an ascending chain of ideals
is an ideal (Lemma 2.2). It is finitely generated, and its generators lie in one member of the chain. \(\square\)

The converse fails: if \(G\) is an abelian group that is not finitely generated, the only ideals of \(G_0\) are
\(\{0\}\) and \(G_0\), but \(G_0\) is not finitely generated.

**Examples 8.7 (three warnings).**

(a) *Torsion.* \(\operatorname{Spec}\mathbb F_{1^n}\) is one point, but
\(\mathbb Z[\mathbb F_{1^n}]=\mathbb Z[x]/(x^n-1)\) is not a domain for \(n\ge2\).

(b) *The cusp.* For the monoid \(M\) of Example 7.11, \(\mathbb Z[M]=\mathbb Z[t^2,t^3]\subseteq\mathbb Z[t]\). It
is a domain and it is not normal, in agreement with Theorem 8.5: \(t\) lies in the fraction field, \(t^2\) lies in
\(\mathbb Z[M]\), and \(t\) does not.

(c) *Nilpotents from non-cancellation.* Let \(M=\{0,1,a,b,c_2,c_3,\dots\}\), with zero \(0\) and unit \(1\), where
\(a\) and \(b\) have degree \(1\), \(c_n\) has degree \(n\), and the product of two elements of degrees
\(i,j\ge1\) is \(c_{i+j}\). This is a monoid without zero divisors and without nilpotent elements other than \(0\). But \(a^2=ab=b^2=c_2\), so in
\(\mathbb Z[M]\) we get \((a-b)^2=c_2-2c_2+c_2=0\). The ring \(\mathbb Z[M]\) is not reduced, and \(M\) is neither
cancellative nor torsion-free.

### Prime ideals of rings and of monoids

**Proposition 8.8.** Let \(R\) be a ring. Every prime ideal of the ring \(R\) is a prime ideal of the monoid
\((R,\cdot)\), and the inclusion \(\operatorname{Spec}R\to\operatorname{Spec}(R,\cdot)\) is a homeomorphism onto its
image.

*Proof.* A prime ideal \(P\) of the ring contains \(0\), is stable under multiplication by \(R\), is different from
\(R\), and \(ab\in P\) implies \(a\in P\) or \(b\in P\). For \(f\in R\) the set \(D(f)\) of
\(\operatorname{Spec}(R,\cdot)\) meets \(\operatorname{Spec}R\) in the basic open set \(D(f)\) of the Zariski
topology of the ring [Stacks, Tag [00DY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-spectrum-ring)]. So the subspace topology and the Zariski topology have the same basis.
\(\square\)

*Reference:* [Cortiñas–Haesemeyer–Walker–Weibel 2015, Observation 5.2.1].

**Example 8.9 (the integers).** The monoid \((\mathbb Z,\cdot)\) is generated by \(-1\) and the prime numbers. By
Proposition 7.2(a) a prime ideal \(\mathfrak p\) of \((\mathbb Z,\cdot)\) is determined by the set \(\Sigma\) of
prime numbers it contains, and
\[
\mathfrak p=\mathfrak p_\Sigma:=\{0\}\cup\bigcup_{\ell\in\Sigma}\ell\mathbb Z .
\]
Conversely, for every set \(\Sigma\) of prime numbers, \(\mathfrak p_\Sigma\) is a prime ideal of
\((\mathbb Z,\cdot)\): it is an ideal, it does not contain \(1\), and a prime number that divides \(ab\) divides
\(a\) or \(b\). So \(\operatorname{Spec}(\mathbb Z,\cdot)\) is in bijection with the set of all sets of prime
numbers, ordered by inclusion. The prime ideals of the ring \(\mathbb Z\) are the \(\mathfrak p_\Sigma\) with
\(\Sigma\) empty or a single prime. The others, such as \(2\mathbb Z\cup3\mathbb Z\), are prime ideals of the monoid
only; compare Lemma 2.10.

### The map from Spec Z[M] to Spec M

**Definition 8.10.** For a monoid \(M\) let
\[
\beta_M:\operatorname{Spec}\mathbb Z[M]\longrightarrow\operatorname{Spec}M,\qquad P\mapsto P\cap M .
\]
It is the composite of the inclusion of Proposition 8.8 for \(R=\mathbb Z[M]\) and the map induced by the morphism
\(M\to(\mathbb Z[M],\cdot)\). So it is continuous. We have \(\beta_M^{-1}(D(f))=D(f)\) and
\(\beta_M^{-1}(V(I))=V(\mathbb Z[I])\) for \(f\in M\) and ideals \(I\) of \(M\). For a morphism
\(\varphi:M\to N\), with induced ring homomorphism \(\mathbb Z[\varphi]\), the maps satisfy
\(\beta_M\circ\operatorname{Spec}(\mathbb Z[\varphi])=\varphi^*\circ\beta_N\).

*Reference:* [Chu–Lorscheid–Santhanam 2012, Theorem 3.2].

**Definition 8.11.** For a prime ideal \(\mathfrak p\) of \(M\) put
\[
G_{\mathfrak p}=(M_{\mathfrak p})^\times,\qquad
\kappa(\mathfrak p)=M_{\mathfrak p}/\mathfrak pM_{\mathfrak p} .
\]
By Theorem 4.3(c), \(\mathfrak pM_{\mathfrak p}\) is the set of non-units of \(M_{\mathfrak p}\), so
\(\kappa(\mathfrak p)=(G_{\mathfrak p})_0\) is a group with zero. We call it the *residue monoid* of \(M\) at
\(\mathfrak p\). It plays the role of the residue field of a ring at a prime ideal, and
[Lorscheid–Ray 2024, Section 2.6] calls it the residue field. If \(M\) is without zero divisors, then
\(\kappa(\{0\})=M^{\mathrm{gp}}\).

**Lemma 8.12 (morphisms to a group with zero).** Let \(H\) be an abelian group.

(a) Let \(\varphi:M\to H_0\) be a morphism. Then \(\mathfrak p=\varphi^{-1}(0)\) is a prime ideal, and there is
exactly one group homomorphism \(\chi:G_{\mathfrak p}\to H\) with \(\varphi(a)=\chi(a/1)\) for all
\(a\notin\mathfrak p\).

(b) Conversely, for a prime ideal \(\mathfrak p\) and a group homomorphism \(\chi:G_{\mathfrak p}\to H\), the map
\(\varphi\) with \(\varphi(a)=\chi(a/1)\) for \(a\notin\mathfrak p\) and \(\varphi(a)=0\) for \(a\in\mathfrak p\) is
a morphism \(M\to H_0\) with \(\varphi^{-1}(0)=\mathfrak p\).

So \(\operatorname{Hom}(M,H_0)\) is the disjoint union of the sets
\(\operatorname{Hom}_{\mathrm{groups}}(G_{\mathfrak p},H)\), \(\mathfrak p\in\operatorname{Spec}M\).

*Proof.* (a) \(\{0\}\) is a prime ideal of \(H_0\), so \(\mathfrak p\) is prime by Lemma 2.6. We have
\(\varphi(M\setminus\mathfrak p)\subseteq H=(H_0)^\times\). By Proposition 4.1(b), \(\varphi\) extends to a morphism
\(\varphi':M_{\mathfrak p}\to H_0\), which maps units to units. Let \(\chi\) be its restriction to
\(G_{\mathfrak p}\). For \(a\notin\mathfrak p\) we get \(\varphi(a)=\varphi'(a/1)=\chi(a/1)\). The homomorphism
\(\chi\) is unique, because \(G_{\mathfrak p}\) consists of the elements \((a/1)(s/1)^{-1}\) with
\(a,s\notin\mathfrak p\). (b) \(\varphi(1)=1\) and \(\varphi(0)=0\). If \(a\) or \(b\) lies in \(\mathfrak p\), then
\(ab\in\mathfrak p\) and \(\varphi(ab)=0=\varphi(a)\varphi(b)\). Otherwise \(ab\notin\mathfrak p\), and
\(\varphi(ab)=\chi(ab/1)=\varphi(a)\varphi(b)\). The two constructions are inverse to each other. \(\square\)

For \(H=\{1\}\) this is Proposition 2.7. For \(H=\mu_n\) it describes the morphisms \(M\to\mathbb F_{1^n}\). For
\(H=k^\times\), \(k\) a field, it describes the morphisms \(M\to(k,\cdot)\), that is, by Proposition 8.3, the ring
homomorphisms \(\mathbb Z[M]\to k\).

**Theorem 8.13 (the fibres of \(\beta\)).** Let \(M\) be a monoid.

(a) For \(\mathfrak p\in\operatorname{Spec}M\), the ring homomorphism
\(\mathbb Z[M]\to\mathbb Z[\kappa(\mathfrak p)]=\mathbb Z[G_{\mathfrak p}]\) induces a homeomorphism of
\(\operatorname{Spec}\mathbb Z[G_{\mathfrak p}]\) onto the fibre \(\beta_M^{-1}(\mathfrak p)\), with its subspace
topology.

(b) \(\beta_M\) is surjective.

(c) For every field \(k\), the set of ring homomorphisms \(\mathbb Z[M]\to k\) is the disjoint union of the sets
\(\operatorname{Hom}_{\mathrm{groups}}(G_{\mathfrak p},k^\times)\), \(\mathfrak p\in\operatorname{Spec}M\). The
homomorphisms that belong to \(\mathfrak p\) are those whose kernel \(P\) satisfies \(\beta_M(P)=\mathfrak p\).

*Proof.* (a) Let \(S=M\setminus\mathfrak p\) and \(R=\mathbb Z[M]\). By Proposition 8.4,
\(\mathbb Z[M_{\mathfrak p}]=S^{-1}R\) and
\(\mathbb Z[\kappa(\mathfrak p)]=S^{-1}R/\mathbb Z[\mathfrak pM_{\mathfrak p}]\). The ideal
\(\mathbb Z[\mathfrak pM_{\mathfrak p}]\) is spanned by the fractions \(a/s=(a/1)(1/s)\) with \(a\in\mathfrak p\),
so it is the ideal of \(S^{-1}R\) generated by the image of \(\mathfrak p\). By the description of the spectrum of a
localization and of a quotient of a ring [Stacks, Tags [00E3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-localization) and [00E5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-closed)], the map
\(\operatorname{Spec}\mathbb Z[\kappa(\mathfrak p)]\to\operatorname{Spec}R\) is a homeomorphism onto the set of
prime ideals \(P\) of \(R\) with \(P\cap S=\emptyset\) and \(P\supseteq\mathfrak p\). These two conditions say
\(P\cap M=\mathfrak p\). (b) The ring \(\mathbb Z[G_{\mathfrak p}]\) has the homomorphism to \(\mathbb Z\) that
sends every element of \(G_{\mathfrak p}\) to \(1\). Its kernel is a prime ideal, so the fibre is not empty.
(c) Combine Proposition 8.3 and Lemma 8.12 for \(H=k^\times\). If \(\Phi:\mathbb Z[M]\to k\) extends
\(\varphi:M\to(k,\cdot)\), then \(\ker\Phi\cap M=\varphi^{-1}(0)\). \(\square\)

So \(\operatorname{Spec}\mathbb Z[M]\) is, as a set, the disjoint union of the spectra of the group rings
\(\mathbb Z[G_{\mathfrak p}]\), indexed by the points of \(\operatorname{Spec}M\). When \(G_{\mathfrak p}\) is free
of rank \(r\), the ring \(\mathbb Z[G_{\mathfrak p}]\) is a ring of Laurent polynomials in \(r\) variables, and the
fibre is a torus of dimension \(r\) over \(\mathbb Z\). The space \(\operatorname{Spec}M\) records how these tori
fit together. Note that \(\operatorname{Spec}M\) is connected while \(\operatorname{Spec}\mathbb Z[M]\) need not be:
for \(M=\{0,e,1\}\) the spectrum has two points, \(\{0\}\subset\{0,e\}\), and
\(\operatorname{Spec}\mathbb Z[M]=\operatorname{Spec}(\mathbb Z\times\mathbb Z)\) is the disjoint union of the two
fibres.

**Corollary 8.14 (counting points).** Let \(M\) be finitely generated.

(a) For every prime ideal \(\mathfrak p\), the group \(G_{\mathfrak p}\) is finitely generated. So
\(G_{\mathfrak p}\cong\mathbb Z^{r(\mathfrak p)}\times T_{\mathfrak p}\) with \(T_{\mathfrak p}\) finite.

(b) For every finite abelian group \(H\),
\[
|\operatorname{Hom}(M,H_0)|=\sum_{\mathfrak p\in\operatorname{Spec}M}|H|^{r(\mathfrak p)}\cdot
|\operatorname{Hom}(T_{\mathfrak p},H)| .
\]

(c) Suppose that all groups \(G_{\mathfrak p}\) are torsion-free, and put
\(N(q)=\sum_{\mathfrak p}(q-1)^{r(\mathfrak p)}\). Then \(\mathbb Z[M]\) has \(N(q)\) homomorphisms to the finite
field \(\mathbb F_q\), for every prime power \(q\), and \(M\) has \(N(n+1)\) morphisms to \(\mathbb F_{1^n}\), for
every \(n\ge1\).

*Proof.* (a) \(M_{\mathfrak p}\) is generated by a finite set \(\Gamma'\) (Proposition 7.2(c)). If a product of
elements of \(\Gamma'\) is a unit, every factor is a unit. So \(G_{\mathfrak p}\) is generated by the units in
\(\Gamma'\), and the structure theorem for finitely generated abelian groups applies [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)].
(b) \(\operatorname{Hom}(\mathbb Z^r\times T,H)=H^r\times\operatorname{Hom}(T,H)\); now use Lemma 8.12 and the
finiteness of \(\operatorname{Spec}M\). (c) Take \(H=\mathbb F_q^\times\), of order \(q-1\), and use
Proposition 8.3; then take \(H=\mu_n\), of order \(n\). \(\square\)

*Reference:* [Deitmar 2005, Section 6] observes the relation between the two counts of (c) in examples.
[Connes–Consani 2010, Proposition 3.18 and Theorem 4.10] prove the decomposition of Lemma 8.12 and part (c) for
schemes built from monoids. [Deitmar 2006, Theorem 1] treats unit groups with torsion: the count over
\(\mathbb F_q\) is a fixed polynomial in \(q\) for all \(q\) such that \(q-1\) is prime to a number \(e\). By (b) one
can take the polynomial \(\sum_{\mathfrak p}(q-1)^{r(\mathfrak p)}\) and for \(e\) the product of the orders of the
groups \(T_{\mathfrak p}\).

Part (c) gives a count over \(\mathbb F_q\) that is a polynomial in \(q\) and has a meaning "over
\(\mathbb F_{1^n}\)" at \(q=n+1\); compare *Counting over finite fields and the limit q → 1*. The lesson *Monoid
schemes* extends the count to spaces glued from spectra.

## 9. Examples: free monoids and the monoids of cones

### Free monoids

**Example 9.1 (the free monoid on \(n\) generators).** Let \(M=\mathbb F_1[x_1,\dots,x_n]\). For a subset
\(J\subseteq\{1,\dots,n\}\) let \(\mathfrak p_J=\langle x_j:j\in J\rangle\). It consists of \(0\) and the monomials
divisible by some \(x_j\) with \(j\in J\). Its complement is the set of monomials in the \(x_i\) with \(i\notin J\),
which is a face. By Proposition 7.2(a) these \(2^n\) ideals are all the prime ideals of \(M\), and
\(\mathfrak p_J\subseteq\mathfrak p_K\) if and only if \(J\subseteq K\). So \(\operatorname{Spec}M\) is the set of
subsets of \(\{1,\dots,n\}\), and by Corollary 7.3 a family of subsets is open when it contains, with a subset, all
smaller subsets. For every \(J\),
\[
M_{\mathfrak p_J}=\mathbb F_1\big[x_j\ (j\in J),\ x_i^{\pm1}\ (i\notin J)\big],\qquad
G_{\mathfrak p_J}\cong\mathbb Z^{\,n-|J|},\qquad
\kappa(\mathfrak p_J)=\mathbb F_1\big[x_i^{\pm1}\ (i\notin J)\big].
\]
The ring \(\mathbb Z[M]\) is \(\mathbb Z[x_1,\dots,x_n]\), and \(\beta_M\) sends a prime ideal \(P\) of this ring to
\(\mathfrak p_J\) with \(J=\{j:x_j\in P\}\). The fibre over \(\mathfrak p_J\) is the set of prime ideals that contain
\(x_j\) for \(j\in J\) and no \(x_i\) with \(i\notin J\). By Theorem 8.13 it is the spectrum of the Laurent
polynomial ring in the variables \(x_i\), \(i\notin J\). So affine \(n\)-space over \(\mathbb Z\) is cut into \(2^n\)
tori, one for each point of \(\operatorname{Spec}M\). The count of Corollary 8.14 is
\[
N(q)=\sum_J(q-1)^{n-|J|}=q^n ,
\]
and \(M\) has \(N(m+1)=(m+1)^n\) morphisms to \(\mathbb F_{1^m}\), as Proposition 1.4 shows directly.

**Example 9.2 (infinitely many generators).** Let \(I\) be an infinite set and \(M\) the free monoid on generators
\(x_i\), \(i\in I\): its non-zero elements are the monomials, each involving finitely many \(x_i\). As in
Example 9.1 the prime ideals are the \(\mathfrak p_J=\langle x_j:j\in J\rangle\) for arbitrary subsets
\(J\subseteq I\). We claim:
\[
\Lambda(\mathfrak p_J)\ \text{is open}\iff I\setminus J\ \text{is finite}.
\]
If \(I\setminus J\) is finite, let \(f\) be the product of the \(x_i\) with \(i\notin J\). Then \(D(f)\) consists of
the \(\mathfrak p_K\) with \(K\subseteq J\), so \(D(f)=\Lambda(\mathfrak p_J)\). Conversely let
\(\Lambda(\mathfrak p_J)\) be open. By Theorem 3.4 it equals \(D(f)\) for some \(f\), which is a monomial in
finitely many variables. If \(I\setminus J\) were infinite, there would be \(i\in I\setminus J\) such that \(x_i\)
does not occur in \(f\). Then \(\mathfrak p_{\{i\}}\in D(f)\), but
\(\mathfrak p_{\{i\}}\not\subseteq\mathfrak p_J\). This proves the claim. *Reference:*
[Cortiñas–Haesemeyer–Walker–Weibel 2015, Example 1.4] treats finite \(J\).

When \(I\setminus J\) is infinite, the stalk at \(\mathfrak p_J\) is not reached on any open set: for every open
neighbourhood \(U\) of \(\mathfrak p_J\) the map \(\mathcal O(U)\to M_{\mathfrak p_J}\) is not surjective. Indeed,
choose \(f\) with \(\mathfrak p_J\in D(f)\subseteq U\) and \(i\in I\setminus J\) such that \(x_i\) does not occur in
\(f\). A section over \(U\) with germ \(1/x_i\) at \(\mathfrak p_J\) would restrict to an element of
\(\mathcal O(D(f))=M_f\) with image \(1/x_i\) in \(M_{\mathfrak p_J}\). But \(M_f\to M_{\mathfrak p_J}\) is
injective, since \(M\) is cancellative, and \(1/x_i\notin M_f\). For finitely generated monoids this cannot happen,
by Proposition 7.2(b).

### The monoids of cones

**Definition 9.3.** A *lattice* is a free abelian group \(L\) of finite rank \(n\). We write
\(L_{\mathbb R}=L\otimes\mathbb R\cong\mathbb R^n\) and regard \(L\) as a subgroup of \(L_{\mathbb R}\). A *rational
polyhedral cone* in \(L_{\mathbb R}\) is a set of the form
\[
C=\operatorname{cone}(v_1,\dots,v_r)=\{t_1v_1+\dots+t_rv_r:\ t_i\in\mathbb R,\ t_i\ge0\}
\]
with \(v_1,\dots,v_r\in L\). Then \(C\cap L\) is a submonoid of the additive group \(L\), and
\(\mathbb F_1[C\cap L]\) is the *monoid of the cone* \(C\). Its elements are \(0\) and the \(\chi^m\) with
\(m\in C\cap L\).

**Lemma 9.4 (Gordan's lemma).** Let \(C=\operatorname{cone}(v_1,\dots,v_r)\) with \(v_i\in L\), and let
\(K=\{\sum t_iv_i:0\le t_i\le1\}\). Then \(K\cap L\) is finite and generates the additive monoid \(C\cap L\). So
\(\mathbb F_1[C\cap L]\) is finitely generated.

*Proof.* \(K\) is bounded and \(L\cong\mathbb Z^n\), so \(K\cap L\) is finite. Let \(m=\sum t_iv_i\in C\cap L\) with
\(t_i\ge0\). Then \(m=\sum\lfloor t_i\rfloor v_i+m'\) with \(m'=\sum(t_i-\lfloor t_i\rfloor)v_i\in K\), and
\(m'=m-\sum\lfloor t_i\rfloor v_i\in L\). The \(v_i\) lie in \(K\cap L\) too. \(\square\)

**Lemma 9.5 (rational coefficients).** Let \(w_1,\dots,w_s\in L\) and \(m\in L\). If \(m=\sum_jt_jw_j\) with real
numbers \(t_j>0\), then there are integers \(N\ge1\) and \(n_j\ge1\) with \(Nm=\sum_jn_jw_j\).

*Proof.* Choose a basis of \(L\). The set \(W=\{t\in\mathbb R^s:\sum t_jw_j=m\}\) is the solution set of a system of
linear equations with integer coefficients. Gaussian elimination over \(\mathbb Q\) shows that
\(W=t^0+\mathbb Rz_1+\dots+\mathbb Rz_d\) with \(t^0,z_1,\dots,z_d\in\mathbb Q^s\). So the points of \(W\) with
rational coordinates are dense in \(W\). The points of \(W\) with all coordinates positive form a non-empty open
subset of \(W\), so one of them is rational. Multiply by a common denominator. \(\square\)

**Proposition 9.6.** The monoid of a rational polyhedral cone is finitely generated, cancellative, torsion-free and
normal.

*Proof.* Let \(M=\mathbb F_1[C\cap L]\). It is finitely generated by Lemma 9.4. It is a submonoid of the group with
zero \(\mathbb F_1[L]\), so it is cancellative, and \(M^{\mathrm{gp}}=\mathbb F_1[G]\) for the subgroup \(G\) of \(L\)
generated by \(C\cap L\) (Proposition 7.5). \(G\) is torsion-free, so \(M\) is torsion-free (Proposition 7.7). Let
\(\alpha\in G\) with \(n\alpha\in C\cap L\) for some \(n\ge1\). Then \(\alpha=\frac1n(n\alpha)\in C\) and
\(\alpha\in L\). So \(M\) is normal. \(\square\)

**Theorem 9.7 (the monoids of cones).** For a monoid \(M\) the following are equivalent.

(i) \(M\cong\mathbb F_1[C\cap L]\) for a lattice \(L\) and a rational polyhedral cone \(C\subseteq L_{\mathbb R}\).

(ii) \(M\) is finitely generated, cancellative, torsion-free and normal.

*Proof.* (i)⇒(ii) is Proposition 9.6. Let \(M\) satisfy (ii), let \(a_1,\dots,a_r\) be non-zero generators and
\(M^{\mathrm{gp}}=G_0\). The group \(G\) is generated by the \(a_i\) and torsion-free (Proposition 7.7), hence free
of finite rank [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. Put \(L=G\), written additively, and \(C=\operatorname{cone}(a_1,\dots,a_r)\).
Then \(M\setminus\{0\}\subseteq C\cap L\). Let \(b\in C\cap L\), \(b\neq0\). Write \(b=\sum t_ia_i\) with
\(t_i\ge0\), and drop the terms with \(t_i=0\). By Lemma 9.5 some multiple \(Nb\), \(N\ge1\), is a sum of the
\(a_i\) with positive integer coefficients, so \(Nb\in M\). Since \(M\) is normal, \(b\in M\). Hence
\(M=\mathbb F_1[C\cap L]\). \(\square\)

*Reference:* the argument for (ii)⇒(i) is part of the proof of
[Cortiñas–Haesemeyer–Walker–Weibel 2015, Theorem 4.4].

The cusp monoid of Example 7.11 satisfies all conditions of (ii) except normality. It is not the monoid of a cone.

**Definition 9.8.** A *face* of a rational polyhedral cone \(C\) is a subset \(F\subseteq C\) that contains \(0\), is
closed under addition and under multiplication by non-negative real numbers, and satisfies
\[
x,y\in C,\ x+y\in F\quad\Longrightarrow\quad x,y\in F .
\]
For example \(C\) is a face. If \(u:L_{\mathbb R}\to\mathbb R\) is a linear form with \(u\ge0\) on \(C\), then
\(C\cap\ker u\) is a face: \(u(x)+u(y)=0\) and \(u(x),u(y)\ge0\) force \(u(x)=u(y)=0\). The *dimension* of a face
\(F\) is the dimension of the linear subspace \(F-F=\{x-y:x,y\in F\}\) that it spans.

**Lemma 9.9.** Let \(C=\operatorname{cone}(v_1,\dots,v_r)\) and let \(F\) be a face of \(C\). Then
\(F=\operatorname{cone}(v_i:v_i\in F)\). In particular \(C\) has at most \(2^r\) faces, and every face is a rational
polyhedral cone.

*Proof.* Let \(x\in F\) and write \(x=\sum t_iv_i\) with \(t_i\ge0\). If \(t_i>0\), then \(x\) is the sum of
\(t_iv_i\in C\) and \(\sum_{k\neq i}t_kv_k\in C\), so \(t_iv_i\in F\) and \(v_i\in F\). Hence
\(x\in\operatorname{cone}(v_i:v_i\in F)\). The other inclusion is clear. \(\square\)

**Theorem 9.10 (prime ideals and faces).** Let \(C=\operatorname{cone}(v_1,\dots,v_r)\) be a rational polyhedral
cone in \(L_{\mathbb R}\), \(P=C\cap L\) and \(M=\mathbb F_1[P]\).

(a) The map \(F\mapsto\mathfrak p_F:=\{\chi^m:m\in P\setminus F\}\cup\{0\}\) is an inclusion-reversing bijection from
the set of faces of \(C\) to \(\operatorname{Spec}M\).

(b) \(M/\mathfrak p_F\cong\mathbb F_1[F\cap L]\).

(c) \(M_{\mathfrak p_F}\cong\mathbb F_1[(C-F)\cap L]\), where \(C-F=\{x-y:x\in C,\ y\in F\}\) is a rational
polyhedral cone.

(d) \(G_{\mathfrak p_F}\cong(F-F)\cap L\), and this group is free abelian of rank \(\dim F\).

*Proof.* Call a subset \(Q\subseteq P\) a face of \(P\) if \(0\in Q\) and, for \(m,m'\in P\), \(m+m'\in Q\) holds
exactly when \(m,m'\in Q\). The faces of the monoid \(M\) (Definition 2.3) are the sets \(\{\chi^m:m\in Q\}\) for
faces \(Q\) of \(P\). So by Lemma 2.4, (a) says that \(F\mapsto F\cap L\) is a bijection from the faces of \(C\) to
the faces of \(P\).

If \(F\) is a face of \(C\), then \(F\cap L\) is a face of \(P\). By Lemma 9.9, \(F\) is the cone generated by the
\(v_i\in F\), which lie in \(F\cap L\). So \(F=\operatorname{cone}(F\cap L)\), and the map is injective.

Let \(Q\) be a face of \(P\), and let \(F=\operatorname{cone}(Q)\) be the set of all finite sums \(\sum t_jq_j\)
with \(q_j\in Q\) and \(t_j\ge0\). We show that \(F\cap L=Q\) and that \(F\) is a face of \(C\).

*\(F\cap L=Q\).* Let \(m\in F\cap L\), \(m\neq0\), and write \(m=\sum t_jq_j\) with \(q_j\in Q\) and \(t_j>0\). By
Lemma 9.5, \(Nm=\sum n_jq_j\in Q\) for some integers \(N,n_j\ge1\). Now \(m\in P\) and \((N-1)m\in P\), and their
sum \(Nm\) lies in \(Q\). Since \(Q\) is a face of \(P\), \(m\in Q\).

*\(F\) is a face.* \(F\) contains \(0\) and is closed under addition and under multiplication by non-negative
numbers. Let \(x,y\in C\) with \(x+y\in F\). Write \(x=\sum a_iv_i\), \(y=\sum b_iv_i\) with \(a_i,b_i\ge0\), and
\(x+y=\sum_jt_jq_j\) with \(q_j\in Q\), \(t_j>0\). Let \(I=\{i:a_i+b_i>0\}\). Then
\[
0=\sum_{i\in I}(a_i+b_i)v_i+\sum_jt_j(-q_j)
\]
with positive coefficients. By Lemma 9.5, applied to \(m=0\) and the vectors \(v_i\) (\(i\in I\)) and \(-q_j\),
there are positive integers \(n_i,k_j\) with \(\sum_{i\in I}n_iv_i=\sum_jk_jq_j\in Q\). For each \(i_0\in I\) this
element of \(Q\) is the sum of \(v_{i_0}\in P\) and another element of \(P\). Since \(Q\) is a face of \(P\),
\(v_{i_0}\in Q\). Hence \(x=\sum_{i\in I}a_iv_i\in F\), and in the same way \(y\in F\).

This proves (a); the bijection reverses inclusions by construction.

(b) \(M/\mathfrak p_F\) consists of \(0\) and the \(\chi^m\) with \(m\in F\cap L\), and the product of two such
elements is never in \(\mathfrak p_F\).

(c) Let \(w_1,\dots,w_s\in F\cap L\) generate the cone \(F\) (Lemma 9.9). Then
\(C-F=\operatorname{cone}(v_1,\dots,v_r,-w_1,\dots,-w_s)\). Since \(M\) is cancellative, \(M_{\mathfrak p_F}\) is the
submonoid of \(\mathbb F_1[L]\) of all \(\chi^{m-g}\) with \(m\in P\), \(g\in F\cap L\), together with \(0\). These
exponents lie in \((C-F)\cap L\). Conversely let \(z\in(C-F)\cap L\), \(z=x-y\) with \(x\in C\) and
\(y=\sum t_jw_j\in F\), \(t_j\ge0\). Put \(g=\sum\lceil t_j\rceil w_j\in F\cap L\). Then \(g-y\in F\subseteq C\), so
\(z+g=x+(g-y)\in C\cap L=P\), and \(z=(z+g)-g\).

(d) By (c), \(G_{\mathfrak p_F}\) is the group of lattice points of \((C-F)\cap-(C-F)\). We show that this set is
\(F-F\). Clearly \(F-F\subseteq C-F\), and \(F-F\) is stable under \(z\mapsto-z\). Conversely let \(z=x-y\) and
\(-z=x'-y'\) with \(x,x'\in C\) and \(y,y'\in F\). Then \(x+x'=y+y'\in F\), so \(x,x'\in F\) and \(z\in F-F\). The
group \(\Lambda=(F-F)\cap L\) is finitely generated (Corollary 8.14(a)) and torsion-free, hence free
[Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. It contains the \(w_j\), which span \(F-F\), so its rank is at least \(\dim F\). Elements of
\(L\cong\mathbb Z^n\) that are linearly independent over \(\mathbb Z\) are linearly independent over \(\mathbb R\),
because the rank of an integer matrix is the same over \(\mathbb Q\) and over \(\mathbb R\). So the rank of
\(\Lambda\) is at most \(\dim F\). \(\square\)

*Reference:* [Jarra 2023a, Lemma 5.9] states the bijection of (a) for faces cut out by linear forms.

The smallest face of \(C\) is \(C\cap(-C)\). It is a face: it is a linear subspace contained in \(C\), and if
\(x,y\in C\) and \(x+y\in C\cap(-C)\), then
\(-x=y-(x+y)\in C\), so \(x\in C\cap(-C)\), and likewise \(y\). Every face \(F\) contains it: for
\(z\in C\cap(-C)\) both \(z\) and \(-z\) lie in \(C\), and their sum \(0\) lies in \(F\), so \(z\in F\). This face
corresponds to the maximal ideal of \(M\), and the face \(C\) corresponds to the ideal \(\{0\}\).

**Corollary 9.11.** Let \(M=\mathbb F_1[C\cap L]\) be the monoid of a rational polyhedral cone. Then for every
prime power \(q\) and every \(m\ge1\),
\[
|\operatorname{Hom}_{\mathrm{rings}}(\mathbb Z[M],\mathbb F_q)|=\sum_F(q-1)^{\dim F},\qquad
|\operatorname{Hom}(M,\mathbb F_{1^m})|=\sum_Fm^{\dim F},
\]
where \(F\) runs over the faces of \(C\).

*Proof.* Theorem 9.10(a),(d) and Corollary 8.14(c). \(\square\)

**Example 9.12 (the quadric cone).** Let \(L=\mathbb Z^2\) and
\(C=\operatorname{cone}((1,0),(1,2))=\{(a,b):0\le b\le2a\}\). The lattice points of the set \(K\) of Lemma 9.4 are
\((0,0)\), \((1,0)\), \((1,1)\), \((1,2)\) and \((2,2)=(1,0)+(1,2)\). So \(M=\mathbb F_1[C\cap L]\) is generated by
\[
x=\chi^{(1,0)},\qquad y=\chi^{(1,1)},\qquad z=\chi^{(1,2)},\qquad\text{with}\quad xz=y^2 .
\]
By Lemma 9.9 every face of \(C\) is generated by a subset of \(\{(1,0),(1,2)\}\). All four subsets give faces:
\(\{0\}\), the rays \(\rho_1=\mathbb R_{\ge0}(1,0)\) and \(\rho_2=\mathbb R_{\ge0}(1,2)\), which are cut out by the
linear forms \(b\) and \(2a-b\), and \(C\). So \(M\) has four prime ideals,
\[
\mathfrak p_C=\{0\},\qquad\mathfrak p_{\rho_1}=\langle y,z\rangle,\qquad\mathfrak p_{\rho_2}=\langle x,y\rangle,
\qquad\mathfrak p_{\{0\}}=\mathfrak m_M=\langle x,y,z\rangle .
\]
As an ordered set, \(\operatorname{Spec}M\) is the same as \(\operatorname{Spec}\mathbb F_1[x_1,x_2]\). The
monoids differ: \(M\) needs three generators, because none of \(x,y,z\) is a product of two non-units. The
localization at \(\mathfrak p_{\rho_1}\) is \(M_x\), the monoid
of the half-plane \(C-\rho_1=\{(a,b):b\ge0\}\), and \(G_{\mathfrak p_{\rho_1}}=\mathbb Z(1,0)\) has rank
\(1=\dim\rho_1\).

The ring \(\mathbb Z[M]\) is isomorphic to \(\mathbb Z[X,Y,Z]/(XZ-Y^2)\). Indeed, this quotient is spanned by the
monomials \(X^iZ^k\) and \(X^iYZ^k\). The homomorphism \(X\mapsto x\), \(Y\mapsto y\), \(Z\mapsto z\) sends them to
\(\chi^{(i+k,2k)}\) and \(\chi^{(i+k+1,2k+1)}\). These are pairwise different, and they are all the basis elements
of \(\mathbb Z[M]\). So the homomorphism is bijective. Corollary 9.11 gives
\[
N(q)=(q-1)^2+2(q-1)+1=q^2 .
\]
This agrees with a direct count of the solutions of \(XZ=Y^2\) in \(\mathbb F_q^3\): there are \(2q-1\) solutions
with \(Y=0\) and \((q-1)^2\) solutions with \(Y\neq0\).

## 10. Monoids without zero and the convention of [Deitmar 2005]

In [Deitmar 2005] a monoid is a commutative monoid without zero: a set \(A\) with an associative and commutative
multiplication and a unit. The symbol \(\mathbb F_1\) denotes the trivial monoid \(\{1\}\) there. An ideal is a
subset \(\mathfrak a\subseteq A\) with \(\mathfrak aA\subseteq\mathfrak a\); the empty set is an ideal. A prime
ideal is an ideal \(\mathfrak p\neq A\) whose complement is closed under multiplication; the empty set is a prime
ideal. The closed sets of the spectrum are the sets \(V(\mathfrak a)\). Localization is defined as in
Proposition 4.1, the structure sheaf is defined by local fractions as in Proposition 5.3, and the base change to
\(\mathbb Z\) is the monoid ring \(\mathbb Z[A]\). The next proposition translates all of this into the language of
this lesson.

**Proposition 10.1.** Let \(A\) be a commutative monoid without zero and \(M=A_0\).

(a) \(\mathfrak a\mapsto\mathfrak a\cup\{0\}\) is an inclusion-preserving bijection from the ideals of \(A\) in the
sense of [Deitmar 2005] to the ideals of \(M\). Prime ideals correspond to prime ideals, and the empty set
corresponds to \(\{0\}\).

(b) This bijection is a homeomorphism from the spectrum of \(A\) in the sense of [Deitmar 2005] to
\(\operatorname{Spec}M\).

(c) For a multiplicative subset \(S\subseteq A\) we have \(S^{-1}M=(S^{-1}A)_0\).

(d) Let \(U\subseteq\operatorname{Spec}M\) be open and non-empty. A section of \(\mathcal O_M\) over \(U\) is either
the family with all components \(0\), or a family of non-zero germs
\(s_{\mathfrak p}\in A_{\mathfrak p}\). The families of the second kind are exactly the sections over \(U\) of the
structure sheaf of [Deitmar 2005].

(e) \(\mathbb Z[M]\) is the monoid ring \(\mathbb Z[A]\).

(f) Let \(B\) be another commutative monoid without zero. The morphisms \(A_0\to B_0\) that are induced by
morphisms \(A\to B\) are exactly the morphisms \(\varphi\) with \(\varphi^{-1}(0)=\{0\}\).

*Proof.* (a) If \(\mathfrak aA\subseteq\mathfrak a\), then \(\mathfrak a\cup\{0\}\) is an ideal of \(M\).
Conversely, if \(I\) is an ideal of \(M\), then \((I\setminus\{0\})A\subseteq I\setminus\{0\}\), because a product
of non-zero elements of \(M\) is not zero. The conditions for a prime ideal agree on non-zero elements, and a
product \(ab\) in \(M\) is \(0\) only if \(a=0\) or \(b=0\). (b) The closed sets correspond. (c) The relation of
Proposition 4.1 on \(M\times S\) restricts to the same relation on \(A\times S\), and \((0,s)\sim(a,s')\) holds
only for \(a=0\). (d) The point \(\{0\}\) is prime and lies in \(U\) (Proposition 3.3(b)). The map
\(\rho_{\mathfrak p,\{0\}}:M_{\mathfrak p}\to M_{\{0\}}=M^{\mathrm{gp}}\) sends only \(0\) to \(0\). So for
\(s\in\mathcal O_M(U)\): if one component of \(s\) is \(0\), then \(s_{\{0\}}=0\), and then all components are
\(0\). If all components are non-zero, Proposition 5.3 describes \(s\) by local fractions \(a/u\), in which
necessarily \(a,u\in A\). This is the condition of [Deitmar 2005, Section 2.1]. (e) Both rings have the basis \(A\).
(f) A morphism \(A\to B\) extends by \(0\mapsto0\) (Proposition 1.6), and the extension maps \(A\) into \(B\).
Conversely \(\varphi^{-1}(0)=\{0\}\) means \(\varphi(A)\subseteq B\). \(\square\)

So nothing is lost by adjoining a zero. Three things change.

1. *More monoids.* By Proposition 1.6 the monoids \(A_0\) are exactly the monoids without zero divisors. Monoids
   with zero divisors are needed for closed subsets: for an ideal \(I\) the closed set \(V(I)\) is the spectrum of
   \(M/I\) (Proposition 6.5), and \(M/I\) is without zero divisors only if \(I\) is prime. Without zero, \(V(I)\)
   is in general not a spectrum at all. Every spectrum \(\operatorname{Spec}A_0\) has the smallest point \(\{0\}\), but
   the closed set \(V(xy)\) in \(\operatorname{Spec}\mathbb F_1[x,y]\) has two minimal points (Example 5.6).
2. *More morphisms and more points.* By part (f), \(\operatorname{Hom}(A_0,B_0)\) is larger than the set of
   morphisms \(A\to B\). For example \(\operatorname{Hom}(M,\mathbb F_1)=\operatorname{Spec}M\)
   (Proposition 2.7), whereas a monoid without zero has exactly one morphism to the trivial monoid. Accordingly
   [Deitmar 2005, Proposition 2.4] finds that the \(\mathbb F_1\)-points of a scheme are its connected components,
   while with zero the \(\mathbb F_1\)-points are all the points [Connes–Consani 2010b, Theorem 3.1].
3. *Spectra with several minimal points.* In \(\operatorname{Spec}A_0\) the point \(\{0\}\) lies in every
   non-empty open set, as noted in [Deitmar 2005, Section 1.2] for the empty prime ideal. The spectrum of a monoid
   with zero divisors has no such point in general.

The works [Connes–Consani 2010b], [Chu–Lorscheid–Santhanam 2012] and
[Cortiñas–Haesemeyer–Walker–Weibel 2015] use monoids with zero, under the names pointed monoids or
\(\mathcal M_0\). So does [Deitmar 2013, Section 1.1]. This course follows them: a monoid has a zero, and
\(\mathbb F_1=\{0,1\}\).

## 11. Exercises

**Exercise 1 (groups with zero).** Let \(M\neq0\) be a monoid. Show that the following are equivalent: (i) every
non-zero element of \(M\) is a unit; (ii) \(\{0\}\) and \(M\) are the only ideals of \(M\); (iii)
\(\operatorname{Spec}M\) has one point and \(M\) has no nilpotent element other than \(0\). Give a monoid with a
one-point spectrum that is not a group with zero.

*Solution.* (i)⇒(ii): a proper ideal contains no unit, so it is \(\{0\}\). (ii)⇒(i): for \(a\neq0\) the ideal \(aM\)
is not \(\{0\}\), so \(aM=M\) and \(a\) is a unit. (i)⇒(iii): every prime ideal lies in
\(\mathfrak m_M=\{0\}\), so \(\{0\}\) is the only prime ideal; a unit is not nilpotent. (iii)⇒(i): the only prime
ideal is \(\mathfrak m_M\). By Corollary 2.9(c) the set of nilpotent elements is the intersection of all prime
ideals, that is, \(\mathfrak m_M\). So \(\mathfrak m_M=\{0\}\). The monoid \(\{0,1,\varepsilon\}\) with
\(\varepsilon^2=0\) has the single prime ideal \(\{0,\varepsilon\}\), and \(\varepsilon\) is not a unit.

**Exercise 2 (products).** Let \(M\) and \(N\) be non-zero monoids.

(a) Show that the faces of \(M\times N\) are the sets \(F_1\times F_2\), where \(F_1\) is a face of \(M\) or
\(F_1=M\), \(F_2\) is a face of \(N\) or \(F_2=N\), and not both \(F_1=M\) and \(F_2=N\).

(b) Describe \(\operatorname{Spec}(\mathbb F_1\times\mathbb F_1)\).

(c) Show that \(\mathbb Z[\mathbb F_1\times\mathbb F_1]\cong\mathbb Z\times\mathbb Z\times\mathbb Z\), and describe
\(\beta\).

*Solution.* (a) Let \(F\) be a face of \(M\times N\). Put \(F_1=\{a:(a,1)\in F\}\) and \(F_2=\{b:(1,b)\in F\}\).
Since \((a,b)=(a,1)(1,b)\), we have \((a,b)\in F\) if and only if \(a\in F_1\) and \(b\in F_2\). So
\(F=F_1\times F_2\). The set \(F_1\) contains \(1\), and \(aa'\in F_1\) if and only if \(a,a'\in F_1\). If
\(0\notin F_1\), then \(F_1\) is a face of \(M\). If \(0\in F_1\), then \(0=0\cdot a\in F_1\) gives \(a\in F_1\) for
all \(a\), so \(F_1=M\). The same holds for \(F_2\). Not both are improper, because \((0,0)\notin F\). Conversely
every such product contains \((1,1)\), does not contain \((0,0)\), and satisfies the condition of Definition 2.3.

So \(\operatorname{Spec}(M\times N)\) has \(mn+m+n\) points if \(\operatorname{Spec}M\) has \(m\) points and
\(\operatorname{Spec}N\) has \(n\) points. It contains the disjoint open subsets \(D((1,0))\) and \(D((0,1))\),
which are copies of \(\operatorname{Spec}M\) and \(\operatorname{Spec}N\) by Proposition 4.2, because
\((M\times N)_{(1,0)}\cong M\). But it has \(mn\) further points, it has a single closed point, and it is connected
(Proposition 3.3). For rings, the spectrum of a product is the disjoint union [Stacks, Tag [00ED](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-product)].

(b) Write \(e_1=(1,0)\), \(e_2=(0,1)\). The only face of \(\mathbb F_1\) is \(\{1\}\). By (a) the faces are
\(\{1\}\), \(\{1,e_1\}\) and \(\{1,e_2\}\), and the prime ideals are \(\mathfrak m=\{0,e_1,e_2\}\),
\(\mathfrak p_1=\{0,e_2\}\) and \(\mathfrak p_2=\{0,e_1\}\). The ideal \(\{0\}\) is not prime, because
\(e_1e_2=0\). The open sets are \(\emptyset\), \(\{\mathfrak p_1\}=D(e_1)\), \(\{\mathfrak p_2\}=D(e_2)\),
\(\{\mathfrak p_1,\mathfrak p_2\}\) and the whole space.

(c) The ring has the basis \(1,e_1,e_2\) with \(e_i^2=e_i\) and \(e_1e_2=0\). Put \(e_3=1-e_1-e_2\). Then
\(e_3^2=1-2e_1-2e_2+e_1+e_2=e_3\) and \(e_3e_1=e_3e_2=0\). So \(e_1,e_2,e_3\) are orthogonal idempotents with sum
\(1\), and \(x\mapsto(xe_1,xe_2,xe_3)\) is an isomorphism onto
\(\mathbb Ze_1\times\mathbb Ze_2\times\mathbb Ze_3\cong\mathbb Z^3\). The spectrum is the disjoint union of three
copies of \(\operatorname{Spec}\mathbb Z\). On the first copy \(e_1=1\) and \(e_2=0\), so \(\beta\) maps it to
\(\mathfrak p_1\). The second copy maps to \(\mathfrak p_2\). On the third copy \(e_1=e_2=0\), so it maps to
\(\mathfrak m\). Each fibre is \(\operatorname{Spec}\mathbb Z\), in agreement with Theorem 8.13: all groups
\(G_{\mathfrak p}\) are trivial. In particular \(\mathbb Z[M\times N]\) is not \(\mathbb Z[M]\times\mathbb Z[N]\).

**Exercise 3 (the quotients of \(\mathbb F_1[x]\)).**

(a) Show that every congruence on \(\mathbb F_1[x]\) is exactly one of the following: equality; the congruence
\(\sim_I\) of the ideal \(I=\langle x^n\rangle\), \(n\ge0\); or, for integers \(r\ge0\) and \(m\ge1\), the
congruence \(\sim_{r,m}\) with
\[
x^a\sim_{r,m}x^b\iff a=b\ \text{or}\ \big(a,b\ge r\ \text{and}\ m\ \text{divides}\ a-b\big),
\]
in which \(0\) is equivalent only to itself.

(b) For each quotient determine the spectrum and the base change to \(\mathbb Z\).

(c) Which of the quotients are cancellative?

*Solution.* (a) Let \(\sim\) be a congruence. *Case 1:* \(x^n\sim0\) for some \(n\ge0\). Take \(n\) minimal. Then
\(x^a\sim0\) for all \(a\ge n\). Suppose \(x^a\sim x^b\) with \(a<b\) and \(a<n\), and put \(d=b-a\). Multiplying by
\(x^d\) repeatedly gives \(x^a\sim x^{a+d}\sim x^{a+2d}\sim\cdots\), and \(x^{a+kd}\sim0\) for large \(k\). So
\(x^a\sim0\), against the choice of \(n\). Hence the classes of \(1,x,\dots,x^{n-1}\) have one element each, and
\(\sim\) is \(\sim_I\) for \(I=\langle x^n\rangle\). *Case 2:* no power of \(x\) is equivalent to \(0\), and
\(\sim\) is not equality. Let \(r\) be the smallest exponent such that \(x^r\sim x^b\) for some \(b>r\), and let
\(m\ge1\) be minimal with \(x^r\sim x^{r+m}\). Multiplying by powers of \(x\) gives \(x^a\sim x^{a+km}\) for all
\(a\ge r\), \(k\ge0\). Conversely let \(x^a\sim x^b\) with \(a<b\). Then \(a\ge r\) by the choice of \(r\). Write
\(b-a=km+j\) with \(0\le j<m\), and put \(a'=a+km\). Then \(x^{a'}\sim x^a\sim x^b=x^{a'+j}\). Choose \(k'\) with
\(r+k'm\ge a'\) and multiply by \(x^{r+k'm-a'}\): this gives \(x^{r+k'm}\sim x^{r+k'm+j}\), hence
\(x^r\sim x^{r+j}\). By the choice of \(m\), \(j=0\). So \(\sim\) is \(\sim_{r,m}\). The listed congruences are
pairwise different.

(b) \(\mathbb F_1[x]\) has the prime ideals \(\{0\}\) and \(\langle x\rangle\), and base change
\(\mathbb Z[x]\). The quotient \(\mathbb F_1[x]/\langle x^n\rangle\) is the zero monoid for \(n=0\). For \(n\ge1\)
the element \(x\) is nilpotent, the only prime ideal is \(\langle x\rangle\), and the base change is
\(\mathbb Z[x]/(x^n)\). The quotient \(C_{r,m}=\mathbb F_1[x]/{\sim_{r,m}}\) has the \(r+m\) non-zero elements
\(1,x,\dots,x^{r+m-1}\), with \(x^{r+m}=x^r\). For \(r=0\) it is \(\mathbb F_{1^m}\), with one prime ideal. For
\(r\ge1\) it is without zero divisors, \(x\) is neither a unit nor nilpotent, and a face that contains a power
\(x^k\), \(k\ge1\), contains \(x\) and so all non-zero elements. So there are two prime ideals, \(\{0\}\) and the
maximal ideal. By Proposition 8.4(b) the base change is \(\mathbb Z[x]/(x^{r+m}-x^r)\), because every difference
\(x^{a+km}-x^a\) with \(a\ge r\) is a multiple of \(x^{r+m}-x^r\). The fibres of \(\beta\) over the two points are
\(V(x^m-1)\setminus V(x)\) and \(V(x)\): the spectra of \(\mathbb Z[x]/(x^m-1)\) and of \(\mathbb Z\). This agrees
with Theorem 8.13, since the localization of \(C_{r,m}\) at \(\{0\}\) is \(\mathbb F_{1^m}\).

(c) \(\mathbb F_1[x]\) is cancellative. \(\mathbb F_1[x]/\langle x^n\rangle\) is cancellative only for \(n=1\),
where it is \(\mathbb F_1\): for \(n\ge2\) we have \(x\cdot x^{n-1}=x\cdot0\). \(C_{r,m}\) is cancellative only for
\(r=0\): for \(r\ge1\) we have \(x^r\cdot x^m=x^r\cdot1\) and \(x^m\neq1\). So the congruences on
\(\mathbb F_1[x]\) with a cancellative quotient, that is, the prime congruences of Remark 6.8, are: equality,
\(x\sim0\), and \(x^m\sim1\) for \(m\ge1\). This agrees with fact 3 of Remark 6.8 and the fibre description quoted
there: the group \(G_{\mathfrak p}\) is \(\mathbb Z\) at \(\mathfrak p=\{0\}\), with subgroups
\(m\mathbb Z\), and it is trivial at \(\mathfrak p=\langle x\rangle\).

*Reference:* [Lorscheid–Ray 2024, Example 2.10] lists the prime congruences on \(\mathbb F_1[t]\) as equality,
\(\langle(t,0)\rangle\) and \(\langle(t,t^k)\rangle\), \(k\ge0\); this fails for \(k\ge2\), because the quotient by
\(t\sim t^k\) is \(C_{1,k-1}\), which is not cancellative, so the list above has \(\langle(t^m,1)\rangle\) instead.
[Lorscheid–Ray 2024, Example 2.15] describes the prime congruences on free monoids by subgroups, in agreement with
the list above.

**Exercise 4 (sections over the punctured spectrum).** Let \(M\) be cancellative.

(a) Show that for every non-empty open set \(U\subseteq\operatorname{Spec}M\),
\(\mathcal O(U)\cong\bigcap_{\mathfrak p\in U}M_{\mathfrak p}\), the intersection being taken in
\(M^{\mathrm{gp}}\).

(b) Let \(P=\mathbb N^2\setminus\{(1,0)\}\) and \(M=\mathbb F_1[P]\), with \(x^ay^b=\chi^{(a,b)}\). Show that \(M\)
is finitely generated with four prime ideals, and that for
\(U=\operatorname{Spec}M\setminus\{\mathfrak m_M\}\) the restriction \(\mathcal O(\operatorname{Spec}M)\to\mathcal
O(U)\) is injective and not surjective. Compare with Example 5.5.

*Solution.* (a) \(\{0\}\) is a prime ideal, and it lies in \(U\) by Proposition 3.3(b). The maps
\(\rho_{\mathfrak p,\{0\}}:M_{\mathfrak p}\to M^{\mathrm{gp}}\) are injective, because \(M\) is cancellative. A
section \(s\in\mathcal O(U)\) is determined by \(g=s_{\{0\}}\in M^{\mathrm{gp}}\), since
\(\rho_{\mathfrak p,\{0\}}(s_{\mathfrak p})=g\) for all \(\mathfrak p\in U\); and \(g\) lies in every
\(M_{\mathfrak p}\), \(\mathfrak p\in U\). Conversely, for \(g\) in the intersection let \(s_{\mathfrak p}\) be the
element of \(M_{\mathfrak p}\) with image \(g\). For \(\mathfrak q\subseteq\mathfrak p\) in \(U\) the elements
\(\rho_{\mathfrak p,\mathfrak q}(s_{\mathfrak p})\) and \(s_{\mathfrak q}\) have the same image \(g\), so they are
equal.

(b) \(P\) is closed under addition: if \(u+v=(1,0)\) with \(u,v\in\mathbb N^2\), then \(u\) or \(v\) is \((1,0)\).
\(M\) is generated by \(y\), \(x^2\), \(x^3\) and \(xy\): every integer \(a\ge2\) is of the form \(2i+3j\), and
\((1,b)=(1,1)+(0,b-1)\) for \(b\ge1\). \(M\) is a submonoid of \(\mathbb F_1[\mathbb Z^2]\), so it is cancellative,
and \(M^{\mathrm{gp}}=\mathbb F_1[\mathbb Z^2]\), because \(x=x^3/x^2\). A face that contains \(x^2\) or \(x^3\)
contains both, because \((x^2)^3=(x^3)^2\). A face that contains \(xy\) contains \(x^2y^2=x^2\cdot y\cdot y\),
hence \(x^2\) and \(y\). A face that contains \(x^2\) and \(y\) contains \(x^2y^2=(xy)^2\), hence \(xy\). So there
are four faces: \(\{1\}\), the powers of \(y\), the elements \(x^a\) with \(a\neq1\), and the set of all non-zero
elements. Let \(\mathfrak p_1\) be the complement of the powers of \(y\), and \(\mathfrak p_2\) the complement of the
set of the \(x^a\). Then \(U=\{\{0\},\mathfrak p_1,\mathfrak p_2\}\), and
\[
M_{\mathfrak p_1}=\{x^ay^b:a\ge0,\ b\in\mathbb Z\}\cup\{0\},\qquad
M_{\mathfrak p_2}=\{x^ay^b:a\in\mathbb Z,\ b\ge0\}\cup\{0\},
\]
because \(x=xy/y\) and \(x=x^3/x^2\). By (a), \(\mathcal O(U)=M_{\mathfrak p_1}\cap M_{\mathfrak p_2}
=\mathbb F_1[x,y]\). It contains \(x\), which is not in \(M=\mathcal O(\operatorname{Spec}M)\). In Example 5.5 the
restriction was bijective. Here \(\mathcal O(U)\) is the normalization of \(M\).

**Exercise 5 (the cone over a square).** Let \(M\) be the quotient of \(\mathbb F_1[x,y,z,w]\) by the congruence
generated by the pair \((xw,yz)\). Let \(L=\mathbb Z^3\) and \(C=\operatorname{cone}(v_1,v_2,v_3,v_4)\) with
\[
v_1=(1,0,0),\quad v_2=(0,1,0),\quad v_3=(1,0,1),\quad v_4=(0,1,1).
\]

(a) Show that \(x\mapsto\chi^{v_1}\), \(y\mapsto\chi^{v_2}\), \(z\mapsto\chi^{v_3}\), \(w\mapsto\chi^{v_4}\)
induces an isomorphism \(M\cong\mathbb F_1[C\cap L]\).

(b) Show that \(M\) has ten prime ideals.

(c) Count the solutions of \(xw=yz\) in \(\mathbb F_q^4\) in two ways.

*Solution.* (a) Let \(\varphi:\mathbb F_1[x,y,z,w]\to\mathbb F_1[C\cap L]\) be the morphism of Proposition 1.4.
Since \(v_1+v_4=v_2+v_3\), we have \(\varphi(xw)=\varphi(yz)\). So the kernel congruence of \(\varphi\) contains the
generated congruence \(\sim\), and \(\varphi\) induces \(\bar\varphi:M\to\mathbb F_1[C\cap L]\)
(Proposition 6.2). A point \(\sum t_iv_i\) of \(C\) is \((t_1+t_3,\ t_2+t_4,\ t_3+t_4)\). So
\[
C=\{(p,q,r)\in\mathbb R^3:\ p,q,r\ge0,\ r\le p+q\}:
\]
for a point of the right-hand side take \(t_3=\min(p,r)\), \(t_4=r-t_3\), \(t_1=p-t_3\), \(t_2=q-t_4\); these
numbers are non-negative, and they are integers if \(p,q,r\) are. Hence the \(v_i\) generate the monoid
\(C\cap L\), and \(\bar\varphi\) is surjective. For injectivity, use \(xw\sim yz\) to replace a factor \(xw\) by
\(yz\) as long as possible. So every monomial is equivalent to one of the form \(x^ay^bz^c\) or \(y^bz^cw^d\).
Their images are \(\chi^{(a+c,\,b,\,c)}\) and \(\chi^{(c,\,b+d,\,c+d)}\). In the first family the third coordinate
is at most the first, with equality only for \(a=0\). In the second family the third coordinate is at least the
first, with equality only for \(d=0\). So \(\varphi\) is injective on these monomials. No monomial is equivalent to
\(0\), because \(\varphi\) sends monomials to non-zero elements. Hence \(\bar\varphi\) is injective.

(b) By Theorem 9.10 we count the faces of \(C\). By Lemma 9.9 a face \(F\) is the cone generated by the set \(E\) of
the \(v_i\) it contains. If \(v_1,v_4\in F\), then \(v_2+v_3=v_1+v_4\in F\), so \(v_2,v_3\in F\); and conversely.
This excludes six of the sixteen subsets \(E\): those that contain \(\{v_1,v_4\}\) but not \(\{v_2,v_3\}\), or the
reverse. The other ten are faces, of the form \(C\cap\ker u\) with \(u\ge0\) on \(C\) (Definition 9.8). In the
coordinates \((p,q,r)\):
\(u=0\) gives \(C\); the forms \(p\), \(q\), \(r\) and \(p+q-r\) give the cones generated by
\(\{v_2,v_4\}\), \(\{v_1,v_3\}\), \(\{v_1,v_2\}\) and \(\{v_3,v_4\}\); the forms \(q+r\), \(p+r\), \(p+2q-r\) and
\(2p+q-r\) give the rays through \(v_1\), \(v_2\), \(v_3\) and \(v_4\); and \(p+q\) gives \(\{0\}\). So \(C\) has
one face of dimension \(0\), four of dimension \(1\), four of dimension \(2\) and one of dimension \(3\).

(c) By (a), Proposition 1.4, Proposition 6.2(c) and Proposition 8.3, the ring homomorphisms
\(\mathbb Z[M]\to\mathbb F_q\) are the quadruples \((x,y,z,w)\in\mathbb F_q^4\) with \(xw=yz\). By Corollary 9.11
and (b) their number is
\[
(q-1)^3+4(q-1)^2+4(q-1)+1=q^3+q^2-q .
\]
Directly: the solutions are the \(2\times2\) matrices over \(\mathbb F_q\) with determinant \(0\). There are
\((q^2-1)(q^2-q)\) invertible matrices, since the first column is any non-zero vector and the second any vector
outside the line spanned by the first. So the number of solutions is
\(q^4-(q^2-1)(q^2-q)=q^3+q^2-q\).

## 12. What this lesson does not prove

- The structure theorem for finitely generated abelian groups, in the form: a finitely generated abelian group is
  the product of a free group of finite rank and a finite group. This is the case of the ring \(\mathbb Z\) of the
  structure theorem for finite modules over a principal ideal domain [Stacks, Tag [0ASV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-modules-PID)]. It is used in
  Theorem 8.5(b), Corollary 8.14, Theorem 9.7 and Theorem 9.10(d).
- The Hilbert basis theorem: a finitely generated ring is Noetherian [Stacks, Tag [00FN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-permanence)]. It is used in
  Corollary 8.6.
- The universal property of the localization of a ring [Stacks, Tag [00CP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-universal-property-localization)], and the description of the spectrum of
  a localization and of a quotient of a ring [Stacks, Tags [00E3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-localization) and [00E5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-spec-closed)]. They are used in Proposition 8.4 and
  Theorem 8.13.
- A converse of Theorem 8.5(c). Let \(M\) be finitely generated, normal and torsion-free, and let \(k\) be an
  integrally closed domain that contains a field. Then \(k[M]\) is an integrally closed domain. This is the affine
  case of [Cortiñas–Haesemeyer–Walker–Weibel 2015, Proposition 6.1(1)], where it is deduced from the normality of
  toric varieties. The ring \(\mathbb Z\) contains no field, but the statement for \(k=\mathbb Z\) follows from the
  statement for \(k=\mathbb Q\). Let \(M^{\mathrm{gp}}=G_0\). Then \(\mathbb Z[M]=\mathbb Q[M]\cap\mathbb Z[G]\)
  inside \(\mathbb Q[G]\), and all these rings have the same fraction field. The group \(G\) is free of finite rank,
  as in the proof of Theorem 9.7, so \(\mathbb Z[G]\) is a ring of Laurent polynomials over \(\mathbb Z\). It is a
  normal domain, because a principal ideal domain is normal, a polynomial ring over a normal domain is normal, and
  a localization of a normal domain is normal [Stacks, Tags [00GZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-PID-normal), [00H1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-polynomial-ring-normal) and [00GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-localize-normal-domain)]. So an element of the fraction
  field that is integral over \(\mathbb Z[M]\) lies in \(\mathbb Q[M]\) and in \(\mathbb Z[G]\), hence in
  \(\mathbb Z[M]\).
- The statement that \(M\mapsto(\operatorname{Spec}M,\mathcal O_M)\) is a contravariant equivalence between monoids
  and affine monoid schemes ([Deitmar 2005, Proposition 2.2] for monoids without zero). It belongs to the lesson
  *Monoid schemes* and is not used here.
- The description of the fibres of the congruence space quoted in Remark 6.8 [Lorscheid–Ray 2024, Proposition 2.18].
  The results of [Jarra 2023a] quoted there are proved in *Monoid schemes*, Section 6.6.

## References

- [Deitmar 2005] A. Deitmar, *Schemes over F_1*, [arXiv:math/0404185](https://arxiv.org/pdf/math/0404185).
- [Deitmar 2006] A. Deitmar, *Remarks on zeta functions and K-theory over F_1*, [arXiv:math/0605429](https://arxiv.org/pdf/math/0605429).
- [Deitmar 2008] A. Deitmar, *F_1-schemes and toric varieties*, [arXiv:math/0608179](https://arxiv.org/pdf/math/0608179).
- [Deitmar 2013] A. Deitmar, *Congruence schemes*, International Journal of Mathematics 24 (2013), no. 2,
  [arXiv:1102.4046](https://arxiv.org/pdf/1102.4046).
- [Connes–Consani 2010] A. Connes, C. Consani, *Schemes over F_1 and zeta functions*, arXiv:0903.2024. Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Connes–Consani 2010b] A. Connes, C. Consani, *From monoids to hyperstructures: in search of an absolute
  arithmetic*, arXiv:1006.4810. Free at https://alainconnes.org/wp-content/uploads/From-monoids-to-hyperstructures-2010.pdf
- [Chu–Lorscheid–Santhanam 2012] C. Chu, O. Lorscheid, R. Santhanam, *Sheaves and K-theory for F_1-schemes*,
  [arXiv:1010.2896](https://arxiv.org/pdf/1010.2896).
- [Cortiñas–Haesemeyer–Walker–Weibel 2015] G. Cortiñas, C. Haesemeyer, M. E. Walker, C. Weibel, *Toric varieties,
  monoid schemes and cdh descent*, [arXiv:1106.1389](https://arxiv.org/pdf/1106.1389).
- [Lorscheid–Ray 2024] O. Lorscheid, S. Ray, *The topological shadow of F_1-geometry: congruence spaces*,
  [arXiv:2305.12801](https://arxiv.org/pdf/2305.12801).
- [Jarra 2023a] M. Jarra, *Strong congruence spaces and dimension in F_1-geometry*, [arXiv:2305.15953](https://arxiv.org/pdf/2305.15953).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 006S, 0078, 00AR, 00CM, 00DY, 00E3 and 0ASV carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.

Result numbers in the cited preprints are those of the arXiv versions.
