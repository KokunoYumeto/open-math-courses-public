# Blueprints and blue schemes

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

The lesson *Monoid schemes* builds a geometry from commutative monoids. It keeps the multiplication of a ring and
forgets the addition. This is enough for toric varieties. But the equation \(ad-bc=1\) of the group
\(\mathrm{SL}_2\) and the rule for multiplying two matrices both use addition, so they cannot be written with
monoids alone.

A *blueprint* keeps a chosen part of the addition. It is a monoid \(A\) together with a set of relations
\(\sum a_i\equiv\sum b_j\) between formal sums of elements of \(A\), called a *pre-addition*. With no relations one
has a monoid. With all relations that hold in a ring one has the ring. In between there are objects such as
\[
\mathbb F_1[a,b,c,d]/\!\!/\langle ad\equiv bc+1\rangle ,
\]
whose elements are the monomials in \(a,b,c,d\) and whose only relation is the equation of \(\mathrm{SL}_2\), written
without a minus sign. Blueprints were introduced in [Lorscheid 2012a]. The geometric objects glued from their spectra
are *blue schemes*. Monoid schemes and ordinary schemes are both blue schemes.

The lesson does the following.

1. Section 1 defines blueprints in three equivalent ways: by a pre-addition, by generators and relations, and as a
   monoid inside a semiring. It treats \(\mathbb F_1\), \(\mathbb F_{1^2}\) and \(\mathbb F_{1^n}\), the semiring
   \(B^+\) and the ring \(B_{\mathbb Z}\) of a blueprint \(B\), and tensor products.
2. Sections 2 and 3 develop ideals, quotients, localization and the spectrum. The main result is that the points of
   the blueprint cut out by equations in affine space are the *zero patterns* of the solutions of the equations
   over fields (Theorem 3.3 and Corollary 3.4).
3. Section 4 defines blue schemes. A new feature is that a blueprint can differ from the global sections of its
   spectrum. The section also treats base extension to semirings and rings.
4. Section 5 constructs \(\operatorname{Proj}\) of a graded blueprint, with full proofs, and projective space.
5. Section 6 explains why blue schemes with their ordinary morphisms do not solve Tits's problem for
   \(\mathrm{SL}_2\). It then defines the rank space, Tits morphisms, the Tits category and Tits–Weyl models, and
   states the main theorem of [Lorscheid 2018a].
6. Section 7 proves the main theorem for \(\mathrm{SL}_2\) in full.
7. Section 8 says what blueprints achieve for Tits's problem and what remains open. Section 9 has exercises with
   solutions.

**What is assumed.** The lessons *Commutative monoids and their spectra* and *Monoid schemes*: monoids with zero,
their ideals, localization and spectra, and the base change \(M\mapsto\mathbb Z[M]\). Semirings and their
congruences. Schemes [Stacks, Tag [01II](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-schemes)] and \(\operatorname{Proj}\) of a graded ring [Stacks, Tag [01M3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-proj)]. Sections 6
to 8 use group schemes over \(\mathbb Z\) only through the example \(\mathrm{SL}_2\), where everything is computed by
hand. The lesson *Counting over finite fields and the limit q → 1* explains Weyl groups and Tits's proposal, and
*Torified varieties and the limits of monoid schemes* treats the same problem with other tools.

Basic references are [Lorscheid 2012a], [Lorscheid 2018a], [López Peña–Lorscheid 2012], the overview
[Lorscheid 2016] and the lecture notes [Lorscheid 2018c].

**Conventions.** Rings are commutative with \(1\). Semirings are commutative, with \(0\) and \(1\), and
\(0\cdot a=0\) for all \(a\); homomorphisms of semirings preserve \(0\), \(1\), sums and products. A *congruence*
on a semiring \(S\) is an equivalence relation \(\sim\) such that \(x\sim y\) and \(z\sim w\) imply
\(x+z\sim y+w\) and \(xz\sim yw\). Then \(S/{\sim}\) is a semiring. The *kernel congruence* of a homomorphism
\(g\) is the relation \(g(x)=g(y)\). A *monoid* is commutative, written multiplicatively, with a unit \(1\) and an
absorbing element \(0\); morphisms preserve \(1\) and \(0\); \(M^\times\) is the group of units.
\(\mathbb N=\{0,1,2,\dots\}\).

## 1. Blueprints

### 1.1 Pre-additions

Let \(A\) be a monoid. Let \(\mathbb N[A]\) be the set of finite formal sums \(\sum_{i=1}^na_i\) of non-zero elements
of \(A\). The order of the terms does not matter, repetitions are allowed, and the empty sum is written \(0\). Sums
are added by putting them together, and multiplied by
\[
\Bigl(\sum a_i\Bigr)\Bigl(\sum b_j\Bigr)=\sum a_ib_j ,
\]
where the terms with \(a_ib_j=0\) are left out. This makes \(\mathbb N[A]\) a semiring. We regard \(A\) as a subset
of \(\mathbb N[A]\): a non-zero element is a sum with one term, and the zero of \(A\) is the empty sum. When we write
a sum \(\sum a_i\) with \(a_i\in A\), terms equal to \(0\) are allowed and count for nothing. The inclusion
\(A\to\mathbb N[A]\) is multiplicative, and it is universal:

> (U) For every semiring \(S\) and every morphism of monoids \(f:A\to(S,\cdot)\) there is exactly one semiring
> homomorphism \(\mathbb N[A]\to S\) that extends \(f\). It sends \(\sum a_i\) to \(\sum f(a_i)\).

**Definition 1.1.** A *pre-addition* on a monoid \(A\) is a congruence \(\equiv\) on the semiring \(\mathbb N[A]\).
It is *proper* if \(a\equiv b\) with \(a,b\in A\) implies \(a=b\). A *blueprint* \(B=A/\!\!/\mathcal R\) is a monoid
\(A\) together with a proper pre-addition \(\mathcal R\). We write \(\sum a_i\equiv\sum b_j\) if the pair
\((\sum a_i,\sum b_j)\) lies in \(\mathcal R\), and we call such a pair a *relation of \(B\)*. The *semiring of
\(B\)* is \(B^+=\mathbb N[A]/\mathcal R\).

A *morphism of blueprints* \(f:B_1\to B_2\) is a morphism \(f:A_1\to A_2\) of the underlying monoids such that
\(\sum a_i\equiv\sum b_j\) in \(B_1\) implies \(\sum f(a_i)\equiv\sum f(b_j)\) in \(B_2\).

We write \(a\in B\) for \(a\in A\), and \(B^\times\) for \(A^\times\). Since \(\mathcal R\) is proper, the map
\(A\to B^+\) is injective. So \(A\) is a subset of \(B^+\). It contains \(0\) and \(1\), it is closed under
multiplication, and every element of \(B^+\) is a finite sum of elements of \(A\). A relation
\(\sum a_i\equiv\sum b_j\) of \(B\) is the same as an equality \(\sum a_i=\sum b_j\) in \(B^+\).

*Reference:* [Lorscheid 2012a, Definitions 1.1 and 1.2] allows monoids without zero and pre-additions that are not
proper. The blueprints of this lesson are the "proper blueprints with a zero" of that paper. This is the convention
of [Lorscheid 2018a, Section 1.1], [Lorscheid 2016, Definition 1.1] and [Lorscheid 2018c, Chapter 4].

**Proposition 1.2 (a blueprint is a monoid inside a semiring).**

(a) Let \(S\) be a semiring and \(A\subseteq S\) a subset that contains \(0\) and \(1\), is closed under
multiplication, and spans \(S\) additively: every element of \(S\) is a finite sum of elements of \(A\). Let
\(\mathcal R\) be the kernel congruence of the homomorphism \(\mathbb N[A]\to S\) given by (U). Then \(\mathcal R\) is
a proper pre-addition, and \((A/\!\!/\mathcal R)^+\cong S\). We write \((A\subset S)\) for this blueprint.

(b) Every blueprint \(B\) with underlying monoid \(A\) is equal to \((A\subset B^+)\).

(c) Let \((A\subset S)\) and \((A'\subset S')\) be as in (a). A map \(f:A\to A'\) is a morphism of blueprints if and
only if it is the restriction of a semiring homomorphism \(g:S\to S'\). The homomorphism \(g\) is determined by
\(f\); we write \(g=f^+\).

*Proof.* (a) The homomorphism \(\mathbb N[A]\to S\) is surjective because \(A\) spans \(S\). So its kernel congruence
\(\mathcal R\) satisfies \(\mathbb N[A]/\mathcal R\cong S\). If \(a\equiv b\) with \(a,b\in A\), then \(a=b\) in
\(S\). (b) The kernel congruence of \(\mathbb N[A]\to B^+\) is \(\mathcal R\) by the definition of \(B^+\).
(c) Let \(f\) be a morphism of blueprints. By (U) the map \(A\to A'\subseteq S'\) extends to a homomorphism
\(\mathbb N[A]\to S'\). It sends related sums to equal elements, because \(f\) preserves relations. So it factors
through \(S=\mathbb N[A]/\mathcal R\), and this gives \(g\). Conversely let \(g:S\to S'\) be a homomorphism with
\(g(A)\subseteq A'\). Then \(f=g|_A\) is a morphism of monoids. A relation \(\sum a_i\equiv\sum b_j\) is an
equality in \(S\); applying \(g\) gives \(\sum f(a_i)=\sum f(b_j)\) in \(S'\). Finally \(g\) is determined by its
values on \(A\), because \(A\) spans \(S\). \(\square\)

So there are three ways to give a blueprint: a monoid with a proper pre-addition; a monoid \(A\) sitting inside a
semiring that it spans; or generators and relations, which come next. *Reference:* [Lorscheid 2012a, Lemma 1.9];
[Lorscheid 2018c, Definition 4.1.1] takes the pair \((A\subset S)\) as the definition.

### 1.2 Generators and relations

An intersection of congruences on a semiring is a congruence. So every set \(E\) of pairs of elements of
\(\mathbb N[A]\) lies in a smallest congruence \(\langle E\rangle\), the congruence *generated* by \(E\). It need
not be proper.

**Definition 1.3.** Let \(A\) be a monoid and \(E\) a set of pairs of elements of \(\mathbb N[A]\). Let \(\bar A\) be
the image of \(A\) in the semiring \(\mathbb N[A]/\langle E\rangle\). We put
\[
A/\!\!/\langle E\rangle=\bigl(\bar A\subset\mathbb N[A]/\langle E\rangle\bigr).
\]
We write the pairs in \(E\) as relations, for example
\(\mathbb F_1[a,b,c,d]/\!\!/\langle ad\equiv bc+1\rangle\).

So the underlying monoid of \(A/\!\!/\langle E\rangle\) is a quotient of \(A\): two elements of \(A\) become equal
when the relations force them to be equal.

**Lemma 1.4 (universal property).** Let \(\pi:A\to\bar A\) be the quotient map of Definition 1.3, and let \(C\) be a
blueprint. Then \(f\mapsto f\circ\pi\) is a bijection from the set of morphisms of blueprints
\(A/\!\!/\langle E\rangle\to C\) to the set of morphisms of monoids \(g:A\to C\) such that
\(\sum g(a_i)\equiv\sum g(b_j)\) in \(C\) for every pair \((\sum a_i,\sum b_j)\) in \(E\).

*Proof.* Let \(g\) be such a morphism of monoids. By (U) it extends to a homomorphism \(g':\mathbb N[A]\to C^+\).
The kernel congruence of \(g'\) contains \(E\), hence \(\langle E\rangle\). So \(g'\) induces a homomorphism
\(\mathbb N[A]/\langle E\rangle\to C^+\), which maps \(\bar A\) into \(C\). By Proposition 1.2(c) this is a morphism
of blueprints \(f\) with \(f\circ\pi=g\). Conversely, if \(f\) is a morphism of blueprints, then \(g=f\circ\pi\)
satisfies the relations in \(E\), because they hold in \(A/\!\!/\langle E\rangle\) and \(f\) preserves relations.
The morphism \(f\) is determined by \(g\), because \(\pi\) is surjective. \(\square\)

*Steps.* The congruence \(\langle E\rangle\) has the following description. A *step* is the passage from a formal
sum \(w+u\lambda\) to the formal sum \(w+u\rho\), where \(w\in\mathbb N[A]\), \(u\) is a non-zero element of \(A\),
and \((\lambda,\rho)\) or \((\rho,\lambda)\) lies in \(E\). Two formal sums are congruent modulo
\(\langle E\rangle\) if and only if one is reached from the other by a finite chain of steps. Indeed, "joined by a
chain of steps" is an equivalence relation, and it is compatible with addition. Multiplying a step by a non-zero
element \(a\) of \(A\) gives a step, or an equality if \(au=0\). So multiplying a step by a formal sum
\(\sum a_k\) gives a chain of steps, one for each \(k\). Hence, if \(x,y\) and \(x',y'\) are joined by chains, so
are \(xx'\), \(yx'\) and \(yy'\), and the relation is a congruence. It contains \(E\), and every congruence that
contains \(E\) contains it. Example 8.2 and Exercise 6 use this description.

### 1.3 First examples

**Examples 1.5.**

(a) *Monoids.* The equality relation on \(\mathbb N[A]\) is a proper pre-addition. It gives the blueprint
\((A\subset\mathbb N[A])=A/\!\!/\langle\emptyset\rangle\), which we again call \(A\). By Lemma 1.4 a morphism of
blueprints between two monoids is the same as a morphism of monoids. So monoids form a full subcategory of
blueprints.

(b) *Semirings and rings.* A semiring \(S\) gives the blueprint \((S\subset S)\). By Proposition 1.2(c) a morphism
of blueprints between two semirings is a semiring homomorphism. For a blueprint \(B\) and a semiring \(S\),
Proposition 1.2(c) also shows
\[
\operatorname{Hom}(B,S)=\operatorname{Hom}_{\text{semirings}}(B^+,S). \tag{1.1}
\]

(c) *The field with one element* is the monoid \(\mathbb F_1=\{0,1\}\), with \(\mathbb F_1^+=\mathbb N\). For every
blueprint \(B\) there is exactly one morphism \(\mathbb F_1\to B\).

(d) \(\mathbb F_{1^2}=\{0,1,-1\}/\!\!/\langle1+(-1)\equiv0\rangle=(\{0,1,-1\}\subset\mathbb Z)\). Indeed, a formal
sum in \(\mathbb N[\{0,1,-1\}]\) is \(m\cdot1+n\cdot(-1)\) with \(m,n\in\mathbb N\), and the relation identifies
two such sums exactly when they have the same difference \(m-n\). The monoid \(\{0,1,-1\}\) without the relation is
a different blueprint.

(e) The *zero blueprint* \(0\) has the monoid \(\{0\}\), in which \(1=0\). For every blueprint \(B\) there is exactly
one morphism \(B\to0\).

**Lemma 1.6 (blueprints with \(-1\)).** Let \(B\) be a blueprint and \(\varepsilon\in B\) an element with
\(1+\varepsilon\equiv0\).

(a) \(B^+\) is a ring.

(b) \(\varepsilon\) is the only element of \(B\) with \(1+\varepsilon\equiv0\), and \(\varepsilon^2=1\).

(c) There is exactly one morphism \(\mathbb F_{1^2}\to B\). It sends \(-1\) to \(\varepsilon\).

*Proof.* (a) For \(x\in B^+\) we have \(x+\varepsilon x=(1+\varepsilon)x=0\). So every element of \(B^+\) has a
negative. (b) If also \(1+\varepsilon'\equiv0\), then \(\varepsilon\) and \(\varepsilon'\) are both the negative of
\(1\) in the ring \(B^+\), so they are equal in \(B^+\), hence in \(B\). In the ring \(B^+\) we have
\(\varepsilon^2=(-1)^2=1\). (c) By Lemma 1.4 a morphism \(\mathbb F_{1^2}\to B\) is a morphism of monoids
\(g:\{0,1,-1\}\to B\) with \(1+g(-1)\equiv0\). By (b) this forces \(g(-1)=\varepsilon\), and this \(g\) is a
morphism of monoids because \(\varepsilon^2=1\). \(\square\)

If such an \(\varepsilon\) exists we say that \(B\) is *with \(-1\)*, and we write \(-1\) for \(\varepsilon\) and
\(-a\) for \(\varepsilon a\). *Reference:* [Lorscheid 2012a, Lemma 1.4].

### 1.4 The ring of a blueprint

**Definition 1.7.** Let \(B\) be a blueprint. The *ring of \(B\)* is the group completion
\(B_{\mathbb Z}=B^+\otimes_{\mathbb N}\mathbb Z\) of the semiring \(B^+\). Its elements are the formal differences
\(x-y\) with \(x,y\in B^+\), and \(x-y=x'-y'\) if and only if \(x+y'+z=x'+y+z\) for some \(z\in B^+\). The blueprint
\(B\) is *cancellative* if the map \(B^+\to B_{\mathbb Z}\) is injective, that is, if \(x+z=y+z\) in \(B^+\) implies
\(x=y\).

Every semiring homomorphism from \(B^+\) to a ring factors through \(B_{\mathbb Z}\) in exactly one way. With (1.1)
this gives, for every ring \(R\),
\[
\operatorname{Hom}(B,R)=\operatorname{Hom}_{\text{rings}}(B_{\mathbb Z},R). \tag{1.2}
\]
If \(B\) is cancellative, then \(A\subseteq B^+\subseteq B_{\mathbb Z}\): the blueprint is a monoid inside a ring,
and its relations are the equalities between sums of elements of \(A\) that hold in the ring. Conversely, if \(R\) is
a ring and \(A\subseteq R\) contains \(0,1\) and is closed under multiplication, let \(S\) be the set of finite sums
of elements of \(A\). Then \((A\subset S)\) is a cancellative blueprint, and its ring is the subring of \(R\) spanned
by \(A\).

A monoid \(A\) is cancellative as a blueprint, and \(A_{\mathbb Z}=\mathbb Z[A]\) is the monoid ring of \(A\) with
the zero of \(A\) identified with \(0\), as in *Commutative monoids and their spectra*. A blueprint with \(-1\) is
cancellative, with \(B^+=B_{\mathbb Z}\), by Lemma 1.6(a). The notation of [Lorscheid 2018a] for \(B_{\mathbb Z}\)
is \(B^+_{\mathbb Z}\).

**Example 1.8 (a blueprint that is not cancellative).** Let
\[
B=\mathbb F_1[x]/\!\!/\langle 1+1\equiv x,\ 1+1+1\equiv x\rangle .
\]
Here \(\mathbb N[\mathbb F_1[x]]=\mathbb N[x]\) is the polynomial semiring. Modulo the relations, \(x\) equals
\(2\), and \(2\) equals \(3\). So every polynomial is congruent to a constant, and all constants \(\ge2\) are
congruent. The homomorphism \(\mathbb N[x]\to\mathbb N/(2\sim3)\), \(x\mapsto2\), respects the relations, and its
target has the three elements \(0,1,2\) with \(1+1=2\), \(2+1=2\), \(2\cdot2=2\). Hence
\(B^+=\mathbb N/(2\sim3)=\{0,1,2\}\). The images of \(x\) and \(x^2\) are both \(2\), so the underlying monoid of
\(B\) is \(\{0,1,2\}\): this blueprint is the semiring \(\{0,1,2\}\). It is not cancellative, because
\(1+2=0+2\). In the group completion this gives \(1=0\), so \(B_{\mathbb Z}=0\) although \(B\neq0\).

### 1.5 Cyclotomic extensions of \(\mathbb F_1\)

For a group \(G\) we write \(G_0=G\sqcup\{0\}\) for the monoid obtained by adding a zero.

**Definition 1.9.** Let \(n\ge1\) and let \(\mu_n\) be a cyclic group of order \(n\). Put
\[
\mathbb F_{1^n}=(\mu_n)_0\big/\!\!\big/\Bigl\langle\,\sum_{\zeta\in H}\zeta\equiv0\ :\ H\subseteq\mu_n
\text{ a subgroup},\ H\neq\{1\}\Bigr\rangle .
\]

For \(n=1\) this is the monoid \(\mathbb F_1\), and for \(n=2\) it is \(\mathbb F_{1^2}\) of Example 1.5(d). In this
lesson \(\mathbb F_{1^n}\) always denotes this blueprint. Its underlying monoid is the monoid \((\mu_n)_0\) that the
other lessons of the course call \(\mathbb F_{1^n}\); the two agree for \(n=1\).

*Reference:* [Lorscheid 2012a, Section 1.10] and [Lorscheid 2018c, Example 4.4.4]. In [Lorscheid 2014, Section 2.3]
and [Lorscheid 2016, Section 1.1] the relations are printed as \(\sum_{i=0}^{n/d}\zeta_n^{di}\equiv0\); the sum is
meant over the \(n/d\) elements \(\zeta_n^{di}\), \(1\le i\le n/d\), of the subgroup generated by \(\zeta_n^d\), for
the divisors \(d<n\) of \(n\).

**Proposition 1.10.** Let \(n\ge2\), let \(\zeta_n\in\mathbb C\) be a primitive \(n\)-th root of unity, and identify
\(\mu_n\) with the group generated by \(\zeta_n\). Then
\[
\mathbb F_{1^n}=\bigl(\{0\}\cup\mu_n\subset\mathbb Z[\zeta_n]\bigr).
\]
So the underlying monoid of \(\mathbb F_{1^n}\) is \((\mu_n)_0\), the blueprint is cancellative, and
\(\mathbb F_{1^n}^+=(\mathbb F_{1^n})_{\mathbb Z}=\mathbb Z[\zeta_n]\). It is with \(-1\) if and only if \(n\) is
even.

*Proof.* Let \(S=\mathbb N[(\mu_n)_0]/\langle E\rangle\) be the semiring of Definition 1.3, where \(E\) is the set
of relations in Definition 1.9. For a subgroup \(H\) write \(\sigma_H=\sum_{\zeta\in H}\zeta\). Choose a prime
\(p\) dividing \(n\) and let \(H_p\) be the subgroup of order \(p\). In \(S\) we have
\(1+\sum_{\zeta\in H_p,\zeta\neq1}\zeta=\sigma_{H_p}=0\). So \(1\) has a negative in \(S\), and as in Lemma 1.6(a)
the semiring \(S\) is a ring. By (U), a homomorphism from \(S\) to a ring \(R\) is a multiplicative map
\(\mu_n\to R\) that sends \(1\) to \(1\) and every \(\sigma_H\) with \(H\neq\{1\}\) to \(0\). So \(S\) is the
quotient of the group ring \(\mathbb Z[\mu_n]\) by the ideal \(J\) generated by these elements \(\sigma_H\). If
\(H\neq\{1\}\), choose a prime \(p\) dividing the order of \(H\). Then \(H_p\subseteq H\), and
\(\sigma_H=\sigma_{H_p}\tau\), where \(\tau\) is the sum of a set of representatives of the cosets of \(H_p\) in
\(H\). So \(J\) is generated by the elements \(\sigma_{H_p}\), \(p\) a prime divisor of \(n\).

Write \(n=\prod_pq_p\) with \(q_p\) the power of \(p\) in \(n\). Then \(\mu_n\) is the product of its subgroups
\(\mu_{q_p}\), so \(\mathbb Z[\mu_n]=\bigotimes_p\mathbb Z[\mu_{q_p}]\), and \(H_p\subseteq\mu_{q_p}\). Therefore
\[
S=\mathbb Z[\mu_n]/J\cong\bigotimes_p\ \mathbb Z[\mu_{q_p}]/(\sigma_{H_p}).
\]
Let \(q=q_p\) and let \(x\) be a generator of \(\mu_q\). Then \(\mathbb Z[\mu_q]=\mathbb Z[x]/(x^q-1)\) and
\(\sigma_{H_p}\) is the class of \(\Phi_q(x)=\sum_{i=0}^{p-1}x^{iq/p}\). This polynomial is monic of degree
\(q-q/p\), and \(x^q-1=(x^{q/p}-1)\Phi_q(x)\). So \(\mathbb Z[\mu_q]/(\sigma_{H_p})=\mathbb Z[x]/(\Phi_q)\) is a free
\(\mathbb Z\)-module of rank \(q-q/p\). Hence \(S\) is a free \(\mathbb Z\)-module of rank
\(\prod_p(q_p-q_p/p)=\varphi(n)\), where \(\varphi\) is Euler's function.

The injective homomorphism \(\mu_n\to\mathbb C^\times\) that sends a generator to \(\zeta_n\) sends every
\(\sigma_H\) with \(H\neq\{1\}\) to \(0\): the image \(H'\) of \(H\) is a non-trivial finite group of complex numbers,
and \(\xi\sum_{\eta\in H'}\eta=\sum_{\eta\in H'}\eta\) for an element \(\xi\neq1\) of \(H'\). So we get a surjective
ring homomorphism \(\psi:S\to\mathbb Z[\zeta_n]\).

Let \(f\in\mathbb Q[x]\) be the minimal polynomial of \(\zeta_n\). It has integer coefficients, because \(\zeta_n\)
is integral over the normal domain \(\mathbb Z\) [Stacks, Tag [00H7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-minimal-polynomial-normal-domain)]. Division with remainder by the monic
polynomial \(f\) shows that \(\mathbb Z[\zeta_n]\cong\mathbb Z[x]/(f)\) is a free \(\mathbb Z\)-module of rank
\(\deg f\).

*Claim.* If \(\xi\in\mathbb C\) is a root of \(f\) and \(p\) is a prime that does not divide \(n\), then \(\xi^p\)
is a root of \(f\).

By the claim and induction on the number of prime factors of \(k\), the number \(\zeta_n^k\) is a root of \(f\) for
every \(k\ge1\) prime to \(n\). These are \(\varphi(n)\) different numbers, so \(\deg f\ge\varphi(n)\). Now
\(\psi\otimes\mathbb Q\) is a surjective linear map from a space of dimension \(\varphi(n)\) onto a space of
dimension \(\deg f\ge\varphi(n)\). So it is bijective, and the kernel of \(\psi\) is a torsion group. It is \(0\),
because \(S\) is a free \(\mathbb Z\)-module. So \(\psi:S\to\mathbb Z[\zeta_n]\) is an isomorphism, and the map
\(\mu_n\to S\) becomes the inclusion of the \(n\)-th roots of unity. In particular it is injective, and
\(\mathbb F_{1^n}=((\mu_n)_0\subset\mathbb Z[\zeta_n])\). Finally \(-1\) is an \(n\)-th root of unity if and only if
\(n\) is even.

*Proof of the claim.* Since \(\zeta_n^n=1\), the polynomial \(f\) divides \(x^n-1\); write \(x^n-1=fh\) with
\(h\in\mathbb Z[x]\). Since \(f\) is irreducible, it is the minimal polynomial of its root \(\xi\), and
\(\xi^n=1\). Suppose that \(f(\xi^p)\neq0\). Then \(h(\xi^p)=0\), because \((\xi^p)^n=1\). So \(\xi\) is a root of
the polynomial \(h(x^p)\), and \(h(x^p)=fg\) with \(g\in\mathbb Z[x]\). Reduce modulo \(p\), and write a bar for the
reduction. In \(\mathbb F_p[x]\) we have \(\bar h(x^p)=\bar h(x)^p\). So \(\bar f\bar g=\bar h^p\). Let \(\pi\) be an
irreducible factor of \(\bar f\). Then \(\pi\) divides \(\bar h\), so \(\pi^2\) divides
\(\bar f\bar h=x^n-1\) in \(\mathbb F_p[x]\). Hence \(\pi\) divides the derivative \(nx^{n-1}\). Since \(n\neq0\) in
\(\mathbb F_p\), \(\pi\) divides \(x^{n-1}\), so \(\pi\) is a constant multiple of \(x\). But \(x\) does not divide
\(x^n-1\). This contradiction proves the claim. \(\square\)

So the blueprint \(\mathbb F_{1^n}\) has the ring \(\mathbb Z[\zeta_n]\), while the monoid \((\mu_n)_0\) has the ring
\(\mathbb Z[x]/(x^n-1)\). For odd \(n\ge3\) the semiring \(\mathbb F_{1^n}^+\) is a ring, although the monoid does
not contain \(-1\). Exercise 1 determines the morphisms between these blueprints.

### 1.6 Blueprints generated by elements of a ring

**Example 1.11.**

(a) Let \(R\) be a ring and \(t_1,\dots,t_n\in R\). Let \(A\) be the set consisting of \(0\) and of all products
\(t_1^{e_1}\cdots t_n^{e_n}\) with \(e_i\in\mathbb N\), and let \(S\) be the set of finite sums of elements of \(A\).
We write
\[
\mathbb F_1\langle t_1,\dots,t_n\rangle=(A\subset S)
\]
and call it the *blueprint generated by \(t_1,\dots,t_n\) in \(R\)*. It is cancellative. If the \(t_i\) generate
\(R\) as a ring, its ring is \(R\).

(b) Let \(\mathfrak a\) be an ideal of the polynomial ring \(\mathbb Z[T_1,\dots,T_n]\), let
\(R=\mathbb Z[T_1,\dots,T_n]/\mathfrak a\), and let \(t_i\) be the class of \(T_i\). The blueprint
\(\mathbb F_1\langle t_1,\dots,t_n\rangle\) is the *\(\mathbb F_1\)-model* of the closed subscheme
\(\operatorname{Spec}R\) of affine \(n\)-space over \(\mathbb Z\). By Definition 1.3 it is equal to
\(\mathbb F_1[T_1,\dots,T_n]/\!\!/\mathcal R_{\mathfrak a}\), where \(\mathcal R_{\mathfrak a}\) consists of all
pairs of sums of monomials whose difference lies in \(\mathfrak a\). *Reference:* [Lorscheid 2018a, Section 4.1].

(c) For \(\mathfrak a=0\) we get the free monoid \(\mathbb F_1[T_1,\dots,T_n]\). Inside the ring of Laurent
polynomials we get the monoid \(\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]=\mathbb F_1\langle T_i,T_i^{-1}\rangle\) of
Laurent monomials, and
\[
\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]=\mathbb F_1\langle -1,T_i,T_i^{-1}\rangle
=\bigl(\{0\}\cup\{\pm T^e:e\in\mathbb Z^r\}\subset\mathbb Z[T_1^{\pm1},\dots,T_r^{\pm1}]\bigr).
\]
In both every non-zero element is a unit. The first is a monoid, because the Laurent monomials are linearly
independent. So a morphism from \(\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]\) to a blueprint \(C\) is a choice of
\(r\) units of \(C\) (Example 1.5(a)). A morphism from \(\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\) to \(C\)
exists only if \(C\) is with \(-1\) (Lemma 1.6). Then \(C^+\) is a ring, and by Proposition 1.2(c) a morphism is a
ring homomorphism \(\mathbb Z[T_1^{\pm1},\dots,T_r^{\pm1}]\to C^+\) that maps the elements \(\pm T^e\) into \(C\).
This is again a choice of \(r\) units of \(C\).

(d) Let \(B=(A\subset B^+)\) be a blueprint. The *free blueprint* \(B[T_1,\dots,T_n]\) is
\((\{aT^e:a\in A,\ e\in\mathbb N^n\}\subset B^+[T_1,\dots,T_n])\), a monoid inside the polynomial semiring. A
morphism from it to a blueprint \(C\) is a morphism \(B\to C\) together with \(n\) elements of \(C\). If \(B\) is a
ring, then \(B[T]\) is not the polynomial ring: it contains only the monomials \(aT^e\). Its semiring is the
polynomial ring.

Different generators of the same ring give different blueprints. The blueprint \(\mathbb F_1\langle T\rangle\) inside
\(\mathbb Z[T]\) is the free monoid \(\mathbb F_1[T]\). The blueprint \(\mathbb F_1\langle T,T+1\rangle\) inside
\(\mathbb Z[T]\) has two generators \(x=T\), \(y=T+1\) and the relation \(y\equiv x+1\).

The next proposition describes the blueprint on which Sections 6 and 7 rest.

**Proposition 1.12 (the blueprint of \(\mathrm{SL}_2^n\)).** Let \(n\ge1\) and
\[
R_n=\mathbb Z[a_i,b_i,c_i,d_i:1\le i\le n]\big/(a_id_i-b_ic_i-1:1\le i\le n),
\]
the coordinate ring of the \(n\)-fold product \(\mathrm{SL}_2\times\dots\times\mathrm{SL}_2\) over \(\mathbb Z\).
Let \(B_n=\mathbb F_1\langle a_i,b_i,c_i,d_i:1\le i\le n\rangle\subseteq R_n\). Call a monomial in the \(4n\)
variables *reduced* if it is not divisible by any of the products \(a_id_i\).

(a) The reduced monomials form a basis of the \(\mathbb Z\)-module \(R_n\).

(b) Every monomial is, in \(R_n\), a sum of reduced monomials. Different monomials are different non-zero elements
of \(R_n\). So the underlying monoid of \(B_n\) is the free monoid \(\mathbb F_1[a_i,b_i,c_i,d_i]\), and \(B_n^+\) is
the set of all sums of reduced monomials: a free \(\mathbb N\)-module on the reduced monomials.

(c) The pre-addition of \(B_n\) is generated by the \(n\) relations \(a_id_i\equiv b_ic_i+1\). So
\[
B_n=\mathbb F_1[a_i,b_i,c_i,d_i]/\!\!/\langle a_id_i\equiv b_ic_i+1:1\le i\le n\rangle ,
\]
and a morphism from \(B_n\) to a blueprint \(C\) is the same as a family of elements
\(\alpha_i,\beta_i,\gamma_i,\delta_i\in C\) with \(\alpha_i\delta_i\equiv\beta_i\gamma_i+1\) for all \(i\).

(d) A morphism \(B_n\to C\) is the same as \(n\) morphisms \(B_1\to C\). So \(B_n\) is the coproduct of \(n\) copies
of \(B_1\) in the category of blueprints.

*Proof.* (a) Let \(n=1\) and write \(a,b,c,d\) for the variables and \(f=ad-bc-1\). Replacing \(ad\) by \(bc+1\)
repeatedly writes every monomial as a combination of reduced monomials, so these span \(R_1\). Order the monomials
lexicographically with \(a>d>b>c\). The leading monomial of \(f\) is \(ad\), with coefficient \(1\). If a non-zero
combination \(F\) of reduced monomials were zero in \(R_1\), then \(F=gf\) in \(\mathbb Z[a,b,c,d]\) with
\(g\neq0\). The leading monomial of \(gf\) is the leading monomial of \(g\) times \(ad\), which is not reduced, a
contradiction. For general \(n\), \(R_n=R_1\otimes\dots\otimes R_1\), and the tensor products of the basis elements
form a basis. These are the reduced monomials.

(b) Let \(M=\prod_ia_i^{\alpha_i}b_i^{\beta_i}c_i^{\gamma_i}d_i^{\delta_i}\) and \(m_i=\min(\alpha_i,\delta_i)\).
In \(R_n\) we have \(a_i^{m_i}d_i^{m_i}=(b_ic_i+1)^{m_i}\), hence
\[
M=\sum_{0\le r_i\le m_i}\ \prod_i\binom{m_i}{r_i}\,
a_i^{\alpha_i-m_i}d_i^{\delta_i-m_i}b_i^{\beta_i+r_i}c_i^{\gamma_i+r_i}. \tag{1.3}
\]
The monomials on the right are reduced and pairwise different. From the set of these monomials one recovers
\(\alpha_i-m_i\) and \(\delta_i-m_i\), then \(\beta_i\) and \(\gamma_i\) as the smallest exponents of \(b_i\) and
\(c_i\), and \(m_i\) as the largest exponent of \(b_i\) minus \(\beta_i\). So different monomials \(M\) have different
expansions, and by (a) they are different elements of \(R_n\), and not zero. The rest of (b) follows from (1.3) and
(a).

(c) Let \(\sim\) be the congruence on \(\mathbb N[\mathbb F_1[a_i,b_i,c_i,d_i]]\) generated by the pairs
\((a_id_i,\ b_ic_i+1)\). These pairs are relations of \(B_n\), so \(x\sim y\) implies \(x\equiv y\). For the
converse let \(\rho(M)\) be the formal sum on the right of (1.3), and extend \(\rho\) additively to formal sums. We
claim \(x\sim\rho(x)\). It is enough to take a monomial \(M\), and we use induction on \(\sum_im_i\). If all
\(m_i=0\), then \(\rho(M)=M\). Otherwise \(M=a_id_iM'\) for some \(i\), and \(M\sim b_ic_iM'+M'\). The rule
\(\binom{m}{r}=\binom{m-1}{r-1}+\binom{m-1}{r}\) gives \(\rho(M)=\rho(b_ic_iM')+\rho(M')\). By induction
\(b_ic_iM'\sim\rho(b_ic_iM')\) and \(M'\sim\rho(M')\). So \(M\sim\rho(M)\). Now let \(x\equiv y\). Then \(\rho(x)\)
and \(\rho(y)\) are formal sums of reduced monomials with the same image in \(R_n\), so \(\rho(x)=\rho(y)\) by (a).
Hence \(x\sim\rho(x)=\rho(y)\sim y\). The description of the morphisms is Lemma 1.4.

(d) This follows from (c). \(\square\)

For \(n=1\) we write \(B_1=\mathbb F_1[\mathrm{SL}_2]=\mathbb F_1[a,b,c,d]/\!\!/\langle ad\equiv bc+1\rangle\).

### 1.7 Tensor products

For monoids \(A\) and \(A'\) the *smash product* \(A\wedge A'\) is the quotient of \(A\times A'\) in which all pairs
\((a,0)\) and \((0,a')\) are identified with \((0,0)\). We write \(a\otimes a'\) for the class of \((a,a')\). It is
the coproduct of \(A\) and \(A'\) in the category of monoids: a morphism \(A\wedge A'\to C\) is the same as a pair of
morphisms \(g:A\to C\), \(g':A'\to C\), by \(a\otimes a'\mapsto g(a)g'(a')\).

**Definition 1.13.** Let \(B\) and \(B'\) be blueprints with underlying monoids \(A\) and \(A'\). Their *tensor
product over \(\mathbb F_1\)* is
\[
B\otimes_{\mathbb F_1}B'=(A\wedge A')/\!\!/\langle E\rangle ,
\]
where \(E\) consists of the pairs \((\sum a_i\otimes1,\ \sum b_j\otimes1)\) for all relations
\(\sum a_i\equiv\sum b_j\) of \(B\), and of the pairs \((\sum1\otimes a'_i,\ \sum1\otimes b'_j)\) for all relations
of \(B'\).

**Proposition 1.14.**

(a) \(B\otimes_{\mathbb F_1}B'\), with the morphisms \(a\mapsto a\otimes1\) and \(a'\mapsto1\otimes a'\), is the
coproduct of \(B\) and \(B'\) in the category of blueprints.

(b) \((B\otimes_{\mathbb F_1}B')^+\) is the coproduct of the semirings \(B^+\) and \(B'^+\), and
\((B\otimes_{\mathbb F_1}B')_{\mathbb Z}=B_{\mathbb Z}\otimes_{\mathbb Z}B'_{\mathbb Z}\).

*Proof.* (a) By Lemma 1.4 a morphism \(B\otimes_{\mathbb F_1}B'\to C\) is a morphism of monoids
\(A\wedge A'\to C\) that satisfies the relations in \(E\). This is a pair of morphisms of monoids \(g,g'\) that
preserve the relations of \(B\) and of \(B'\), that is, a pair of morphisms of blueprints. (b) By (1.1), (1.2) and
(a), semiring homomorphisms from \((B\otimes_{\mathbb F_1}B')^+\) to a semiring \(S\) are pairs of homomorphisms
\(B^+\to S\), \(B'^+\to S\), and ring homomorphisms from \((B\otimes_{\mathbb F_1}B')_{\mathbb Z}\) to a ring \(R\)
are pairs of ring homomorphisms \(B_{\mathbb Z}\to R\), \(B'_{\mathbb Z}\to R\). The coproduct of two rings is
their tensor product. \(\square\)

*Reference:* [Lorscheid 2012a, Proposition 1.12]; [Lorscheid 2018c, Definition 4.1.3].

For example \(\mathbb F_1[S]\otimes_{\mathbb F_1}\mathbb F_1[T]=\mathbb F_1[S,T]\), and by Proposition 1.12(d) the
blueprint \(B_n\) is the \(n\)-fold tensor power of \(\mathbb F_1[\mathrm{SL}_2]\).

**Lemma 1.15 (adjoining \(-1\)).** Let \(B\) be a blueprint with underlying monoid \(A\), and let \(\bar A\) be the
image of \(A\) in \(B_{\mathbb Z}\). Put
\[
B_{\mathrm{inv}}=\bigl(\bar A\cup(-\bar A)\subset B_{\mathbb Z}\bigr).
\]
Then \(B_{\mathrm{inv}}\cong B\otimes_{\mathbb F_1}\mathbb F_{1^2}\).

*Proof.* The set \(\bar A\cup(-\bar A)\) contains \(0\) and \(1\), is closed under multiplication, and spans
\(B_{\mathbb Z}\) additively. We show that \(B_{\mathrm{inv}}\) has the universal property of the coproduct. Let
\(C\) be a blueprint. A morphism from \(\mathbb F_{1^2}\) or from \(B_{\mathrm{inv}}\) to \(C\) sends \(-1\) to an
element \(\varepsilon\) with \(1+\varepsilon\equiv0\). So if \(C\) is not with \(-1\), there is no morphism
\(\mathbb F_{1^2}\to C\) and no morphism \(B_{\mathrm{inv}}\to C\). If \(C\) is with \(-1\), then \(C^+\) is a ring
and there is exactly one morphism \(\mathbb F_{1^2}\to C\) (Lemma 1.6). A morphism \(B\to C\) is a homomorphism
\(B^+\to C^+\) that maps \(A\) into \(C\). It extends in exactly one way to a ring homomorphism
\(B_{\mathbb Z}\to C^+\), and this extension maps \(\bar A\cup(-\bar A)\) into \(C\). By Proposition 1.2(c),
morphisms \(B_{\mathrm{inv}}\to C\) are the ring homomorphisms \(B_{\mathbb Z}\to C^+\) with this property. So
morphisms \(B_{\mathrm{inv}}\to C\) and morphisms \(B\to C\) correspond. \(\square\)

**Warning.** The tensor product of two cancellative blueprints need not be cancellative. Exercises 3 and 6 and
Example 8.2 give examples. Proposition 1.12 shows that the tensor powers of \(\mathbb F_1[\mathrm{SL}_2]\) are
cancellative; the reason is that \(B_1^+\) is a free \(\mathbb N\)-module.

## 2. Ideals, quotients and localization

In this section \(B\) is a blueprint with underlying monoid \(A\).

**Definition 2.1.** An *ideal* of \(B\) is a subset \(I\subseteq B\) with the following two properties.

(I1) \(0\in I\), and \(ab\in I\) for all \(a\in I\) and \(b\in B\).

(I2) If \(a+\sum b_j\equiv\sum c_k\) is a relation of \(B\) in which all \(b_j\) and all \(c_k\) lie in \(I\), then
\(a\in I\).

**Examples 2.2.**

(a) \(B\) is an ideal. The set \(\{0\}\) is an ideal: in (I2) the relation reads \(a\equiv0\), and then \(a=0\)
because the pre-addition is proper.

(b) Let \(B=A\) be a monoid. A relation \(a+\sum b_j\equiv\sum c_k\) is an equality of formal sums, so \(a=0\) or
\(a\) is one of the \(c_k\). Hence (I2) follows from (I1), and the ideals of the blueprint \(A\) are the ideals of
the monoid \(A\).

(c) Let \(B=R\) be a ring. An ideal of the ring satisfies (I1) and (I2). Conversely let \(I\) satisfy (I1) and (I2).
For \(b_1,b_2\in I\) and \(a=b_1+b_2\) the relation \(a\equiv b_1+b_2\) gives \(a\in I\), and the relation
\((-b_1)+b_1\equiv0\) gives \(-b_1\in I\). So the ideals of the blueprint \(R\) are the ideals of the ring \(R\).

(d) Let \(B\) be a semiring. The same argument shows that the ideals of \(B\) are the subsets that are closed under
addition and under multiplication by elements of \(B\), and that are *subtractive*: if \(a+b\in I\) and \(b\in I\),
then \(a\in I\). For \(B=\mathbb N\) these are the sets \(d\mathbb N\), \(d\ge0\): if \(d\) is the smallest positive
element of a subtractive ideal \(I\) and \(m=qd+r\in I\) with \(0\le r<d\), then \(r\in I\), so \(r=0\).

(e) In the semiring \(\{0,1,2\}\) of Example 1.8 the set \(\{0,2\}\) satisfies (I1) and is closed under addition.
It is not an ideal: \(1+2=2\) would force \(1\in I\). The only ideals are \(\{0\}\) and \(B\).

*Reference:* [Lorscheid 2012a, Definition 2.11 and Lemma 2.16]. In [Lorscheid 2018c, Definition 4.6.1] the subsets
with (I1) and (I2) are called \(k\)-ideals, and the subsets with (I1) alone are called \(m\)-ideals.

**Proposition 2.3 (quotients).** Let \(I\subseteq B\) be a subset with (I1). For \(x,y\in\mathbb N[A]\) write
\(x\equiv_Iy\) if there are sums \(u,v\) of elements of \(I\) with \(x+u\equiv y+v\) in \(B\).

(a) The relation \(\equiv_I\) is the congruence on \(\mathbb N[A]\) generated by the relations of \(B\) and the pairs
\((c,0)\) with \(c\in I\).

(b) Let \(B/I=A/\!\!/\langle\equiv_I\rangle\) be the blueprint of Definition 1.3 and \(\pi:B\to B/I\) the quotient
map. For every blueprint \(C\), composition with \(\pi\) is a bijection from the morphisms \(B/I\to C\) to the
morphisms \(f:B\to C\) with \(f(I)=\{0\}\).

(c) \(I\subseteq\pi^{-1}(0)\), with equality if and only if \(I\) is an ideal.

(d) A subset of \(B\) is an ideal if and only if it is of the form \(f^{-1}(0)\) for a morphism of blueprints
\(f:B\to C\).

*Proof.* (a) The relation is reflexive and symmetric. If \(x+u\equiv y+v\) and \(y+u'\equiv z+v'\), then
\(x+u+u'\equiv y+v+u'\equiv z+v'+v\); so it is transitive. It is compatible with addition. If \(x+u\equiv y+v\) and
\(x'+u'\equiv y'+v'\), then multiplying gives
\[
xx'+(xu'+ux'+uu')\equiv yy'+(yv'+vy'+vv'),
\]
and the two brackets are sums of elements of \(I\) by (I1). So \(\equiv_I\) is a congruence. It contains the
relations of \(B\) (take \(u=v=0\)) and the pairs \((c,0)\) (take \(u=0\), \(v=c\)). A congruence \(\sim\) that
contains the relations of \(B\) and all pairs \((c,0)\) satisfies \(u\sim0\sim v\) for sums of elements of \(I\), so
\(x+u\equiv y+v\) implies \(x\sim x+u\sim y+v\sim y\).

(b) This is Lemma 1.4: a morphism of monoids \(g:A\to C\) preserves the generating pairs of (a) if and only if it
is a morphism of blueprints \(B\to C\) with \(g(I)=\{0\}\).

(d), first half. Let \(f:B\to C\) be a morphism and \(J=f^{-1}(0)\). Then (I1) holds. If \(a+\sum b_j\equiv\sum c_k\)
with \(b_j,c_k\in J\), then \(f(a)\equiv0\) in \(C\), because zero terms count for nothing. So \(f(a)=0\), since the
pre-addition of \(C\) is proper.

(c) For \(c\in I\) we have \(c\equiv_I0\), so \(\pi(c)=0\). An element \(a\) lies in \(\pi^{-1}(0)\) if and only if
\(a\equiv_I0\), that is, \(a+u\equiv v\) for sums \(u,v\) of elements of \(I\). If \(I\) is an ideal, this implies
\(a\in I\) by (I2). Conversely, if \(I=\pi^{-1}(0)\), then \(I\) is an ideal by the first half of (d).

(d), second half. An ideal \(I\) is \(\pi^{-1}(0)\) by (c). \(\square\)

*Reference:* [Lorscheid 2012a, Propositions 2.12 and 2.13]; [Lorscheid 2018c, Proposition 4.6.9].

**Proposition 2.4 (the cancellative case).** Let \(B\) be cancellative and \(R=B_{\mathbb Z}\), so that
\(A\subseteq B^+\subseteq R\).

(a) If \(\mathfrak a\) is an ideal of the ring \(R\), then \(A\cap\mathfrak a\) is an ideal of \(B\). If \(I\) is an
ideal of \(B\), then the ideal \(IR\) of \(R\) generated by \(I\) is the set of all differences \(u-v\) of sums of
elements of \(I\), and \(I=A\cap IR\).

(b) Let \(I\) be an ideal of \(B\). Then \(B/I=(\bar A\subset\overline{B^+})\), where \(\bar A\) and
\(\overline{B^+}\) are the images of \(A\) and \(B^+\) in the ring \(R/IR\). So \(B/I\) is cancellative, its
underlying monoid is the image of \(A\) in \(R/IR\), and \((B/I)_{\mathbb Z}=R/IR\).

*Proof.* (a) The set \(A\cap\mathfrak a\) satisfies (I1). If \(a+\sum b_j=\sum c_k\) in \(R\) with
\(b_j,c_k\in\mathfrak a\), then \(a\in\mathfrak a\). Now let \(I\) be an ideal of \(B\). The set of differences
\(u-v\) is a subgroup of \(R\). It is stable under multiplication by elements of \(A\) by (I1), hence by all elements
of \(R\), because \(R\) consists of differences of sums of elements of \(A\). So it is the ideal \(IR\). Clearly
\(I\subseteq A\cap IR\). If \(a\in A\cap IR\), then \(a=u-v\), so \(a+v=u\) in \(R\). Since \(B^+\subseteq R\), this
is a relation \(a+v\equiv u\) of \(B\), and \(a\in I\) by (I2).

(b) For \(x,y\in\mathbb N[A]\) we have \(x\equiv_Iy\) if and only if \(x+u=y+v\) in \(R\) for some sums \(u,v\) of
elements of \(I\), that is, if and only if \(x-y\in IR\). So \(\mathbb N[A]/{\equiv_I}\) is the image of
\(\mathbb N[A]\) in \(R/IR\). This image is \(\overline{B^+}\), and it spans the ring \(R/IR\) as a group.
\(\square\)

*Reference:* [Lorscheid 2012a, Lemma 2.17]; [Lorscheid 2018a, Lemma 1.31].

**Definition 2.5.** An ideal \(\mathfrak p\) of \(B\) is *prime* if \(\mathfrak p\neq B\) and \(ab\in\mathfrak p\)
implies \(a\in\mathfrak p\) or \(b\in\mathfrak p\). The blueprint \(B\) is *local* if \(B\neq0\) and the set
\(B\setminus B^\times\) of non-units is an ideal. It is a *blue field* if \(B\neq0\) and every non-zero element is a
unit. For a submonoid \(A'\) of \(A\), the *subblueprint of \(B\) on \(A'\)* is \((A'\subset S')\), where \(S'\) is
the set of sums of elements of \(A'\) in \(B^+\); its relations are the relations of \(B\) between elements of
\(A'\). The *unit field* \(B^\star\) of \(B\) is the subblueprint on \(B^\times\cup\{0\}\).

An ideal other than \(B\) contains no unit. So in a local blueprint the ideal \(B\setminus B^\times\) contains every
ideal other than \(B\); it is the *maximal ideal*. A blue field is local, with maximal ideal \(\{0\}\). Every
non-zero monoid is local. A ring is local in this sense exactly when it is a local ring. If \(B\neq0\), then
\(B^\star\) is a blue field.

**Proposition 2.6 (localization).** Let \(S\subseteq A\) be a multiplicative subset. Let \(S^{-1}A\) be the
localization of the monoid \(A\), and let \(S^{-1}B^+\) be the localization of the semiring \(B^+\): its elements
are fractions \(x/s\), and \(x/s=x'/s'\) if and only if \(ts'x=tsx'\) for some \(t\in S\).

(a) The map \(S^{-1}A\to S^{-1}B^+\) is injective, and \(S^{-1}B=(S^{-1}A\subset S^{-1}B^+)\) is a blueprint. A
relation \(\sum a_i/s\equiv\sum b_j/s\) holds in \(S^{-1}B\) if and only if \(\sum ta_i\equiv\sum tb_j\) in \(B\) for
some \(t\in S\).

(b) The map \(\iota:B\to S^{-1}B\), \(a\mapsto a/1\), is a morphism, and \(\iota(S)\) consists of units. Every
morphism \(f:B\to C\) with \(f(S)\subseteq C^\times\) factors through \(\iota\) in exactly one way.

(c) \((S^{-1}B)_{\mathbb Z}=S^{-1}(B_{\mathbb Z})\). If \(B\) is cancellative, so is \(S^{-1}B\).

(d) If \(B'\) is the subblueprint of \(B\) on a submonoid \(A'\) and \(S\subseteq A'\), then \(S^{-1}B'\) is the
subblueprint of \(S^{-1}B\) on \(S^{-1}A'\).

*Proof.* (a) The condition for \(a/s=a'/s'\) is the same in \(S^{-1}A\) and in \(S^{-1}B^+\), because
\(A\subseteq B^+\). The image contains \(0/1\) and \(1/1\), is closed under multiplication, and spans
\(S^{-1}B^+\), because \(x/s=\sum a_i/s\) for \(x=\sum a_i\). The last statement is the definition of equality in
\(S^{-1}B^+\). (b) The homomorphism \(f^+:B^+\to C^+\) sends \(S\) to units, so it extends in exactly one way to
\(S^{-1}B^+\to C^+\), by \(x/s\mapsto f^+(x)f(s)^{-1}\). This extension maps \(a/s\) into \(C\). (c) Localization
and group completion commute, because both are defined by universal properties. If \(B^+\to B_{\mathbb Z}\) is
injective, then so is \(S^{-1}B^+\to S^{-1}B_{\mathbb Z}\), by the description of equality of fractions. (d) The
conditions for equality of fractions and for relations between fractions with numerators in \(A'\) are the same in
\(S^{-1}B'\) and in \(S^{-1}B\). \(\square\)

For \(h\in B\) we write \(B_h=S^{-1}B\) with \(S=\{h^n:n\ge0\}\). For a prime ideal \(\mathfrak p\) we write
\(B_{\mathfrak p}=S^{-1}B\) with \(S=B\setminus\mathfrak p\). *Reference:* [Lorscheid 2012a, Section 1.13].

**Proposition 2.7 (prime ideals of a localization).** Let \(S\subseteq B\) be a multiplicative subset. The map
\(\mathfrak Q\mapsto\iota^{-1}(\mathfrak Q)\) is a bijection from the prime ideals of \(S^{-1}B\) to the prime
ideals \(\mathfrak p\) of \(B\) with \(\mathfrak p\cap S=\emptyset\). Its inverse sends \(\mathfrak p\) to
\(S^{-1}\mathfrak p=\{a/s:a\in\mathfrak p,\ s\in S\}\).

*Proof.* Let \(\mathfrak Q\) be a prime ideal of \(S^{-1}B\). Then \(\iota^{-1}(\mathfrak Q)\) is an ideal by
Proposition 2.3(d), applied to \(B\to S^{-1}B\to S^{-1}B/\mathfrak Q\). It is prime, and it is disjoint from \(S\)
because \(\iota(S)\) consists of units. Since \(s/1\) is a unit, \(a/s\in\mathfrak Q\) if and only if
\(a/1\in\mathfrak Q\). So \(\mathfrak Q=S^{-1}(\iota^{-1}(\mathfrak Q))\).

Now let \(\mathfrak p\) be a prime ideal of \(B\) with \(\mathfrak p\cap S=\emptyset\). We claim: \(a/s\) lies in
\(S^{-1}\mathfrak p\) if and only if \(a\in\mathfrak p\). Indeed, if \(a/s=a'/s'\) with \(a'\in\mathfrak p\), then
\(ts'a=tsa'\in\mathfrak p\) for some \(t\in S\), and \(ts'\notin\mathfrak p\), so \(a\in\mathfrak p\). The claim
gives (I1) for \(S^{-1}\mathfrak p\), and \(1/1\notin S^{-1}\mathfrak p\), and
\(\iota^{-1}(S^{-1}\mathfrak p)=\mathfrak p\), and the prime property. For (I2), let \(x+\sum y_j\equiv\sum z_k\) in
\(S^{-1}B\) with \(y_j,z_k\in S^{-1}\mathfrak p\). Write all fractions with a common denominator \(s\):
\(x=a/s\), \(y_j=b_j/s\), \(z_k=c_k/s\), with \(b_j,c_k\in\mathfrak p\) by the claim. By Proposition 2.6(a) there is
\(t\in S\) with \(ta+\sum tb_j\equiv\sum tc_k\) in \(B\). Then \(ta\in\mathfrak p\) by (I2) for \(\mathfrak p\), so
\(a\in\mathfrak p\) and \(x\in S^{-1}\mathfrak p\). \(\square\)

*Reference:* [Lorscheid 2012a, Lemma 3.19].

**Corollary 2.8.** Let \(\mathfrak p\) be a prime ideal of \(B\). Then \(B_{\mathfrak p}\) is local with maximal
ideal \(\mathfrak pB_{\mathfrak p}=\{a/s:a\in\mathfrak p,\ s\notin\mathfrak p\}\), and
\(\kappa(\mathfrak p)=B_{\mathfrak p}/\mathfrak pB_{\mathfrak p}\) is a blue field, the *residue field* at
\(\mathfrak p\).

*Proof.* A fraction \(a/s\) with \(a\notin\mathfrak p\) is a unit, with inverse \(s/a\). By Proposition 2.7 the set
\(\mathfrak pB_{\mathfrak p}\) of the other fractions is a prime ideal, so it contains no unit. Hence it is the set of
non-units. By Proposition 2.3(c) the quotient map \(B_{\mathfrak p}\to\kappa(\mathfrak p)\) is surjective and sends
exactly \(\mathfrak pB_{\mathfrak p}\) to \(0\). So \(1\neq0\) in \(\kappa(\mathfrak p)\), and every non-zero element
is the image of a unit. \(\square\)

## 3. The spectrum

**Definition 3.1.** The *spectrum* \(\operatorname{Spec}B\) is the set of prime ideals of \(B\). For \(h\in B\) and
a subset \(E\subseteq B\) put
\[
D(h)=\{\mathfrak p\in\operatorname{Spec}B:h\notin\mathfrak p\},\qquad
V(E)=\{\mathfrak p\in\operatorname{Spec}B:E\subseteq\mathfrak p\}.
\]

**Proposition 3.2.**

(a) \(D(g)\cap D(h)=D(gh)\) and \(D(1)=\operatorname{Spec}B\). So the sets \(D(h)\) form a basis of a topology on
\(\operatorname{Spec}B\). In this topology the closure of a point \(\mathfrak p\) is \(V(\mathfrak p)\).

(b) Let \(f:B\to C\) be a morphism. If \(\mathfrak q\) is a prime ideal of \(C\), then \(f^{-1}(\mathfrak q)\) is a
prime ideal of \(B\). The map \(f^{\ast}:\operatorname{Spec}C\to\operatorname{Spec}B\),
\(\mathfrak q\mapsto f^{-1}(\mathfrak q)\), is continuous, and \((f^{\ast})^{-1}(D(h))=D(f(h))\).

(c) Let \(I\) be an ideal of \(B\) and \(\pi:B\to B/I\). Then \(\pi^{\ast}\) is a homeomorphism from
\(\operatorname{Spec}(B/I)\) onto the closed subset \(V(I)\).

(d) Let \(S\) be a multiplicative subset. Then \(\iota^{\ast}\) is a homeomorphism from
\(\operatorname{Spec}S^{-1}B\) onto \(\{\mathfrak p:\mathfrak p\cap S=\emptyset\}\). In particular
\(\operatorname{Spec}B_h\) is homeomorphic to \(D(h)\).

(e) If \(\operatorname{Spec}B\) is finite, a subset \(U\) is open if and only if it is *stable under generization*:
\(\mathfrak p\in U\) and \(\mathfrak q\subseteq\mathfrak p\) imply \(\mathfrak q\in U\).

*Proof.* (a) The first formula says that \(gh\notin\mathfrak p\) if and only if \(g\notin\mathfrak p\) and
\(h\notin\mathfrak p\). A point \(\mathfrak q\) lies in the closure of \(\mathfrak p\) if and only if every \(D(h)\)
that contains \(\mathfrak q\) contains \(\mathfrak p\), that is, \(\mathfrak p\subseteq\mathfrak q\).

(b) \(f^{-1}(\mathfrak q)\) is the preimage of \(0\) under \(B\to C\to C/\mathfrak q\), so it is an ideal by
Proposition 2.3. It does not contain \(1\), and it is prime because \(\mathfrak q\) is. The formula for the
preimage of \(D(h)\) is clear.

(c) If \(\mathfrak Q\) is a prime ideal of \(B/I\), then \(\pi^{-1}(\mathfrak Q)\) contains \(\pi^{-1}(0)=I\), and
\(\mathfrak Q=\pi(\pi^{-1}(\mathfrak Q))\) because \(\pi\) is surjective. So \(\pi^{\ast}\) is injective with image
in \(V(I)\). Let \(\mathfrak p\in V(I)\). The quotient map \(\pi_{\mathfrak p}:B\to B/\mathfrak p\) sends \(I\) to
\(0\), so \(\pi_{\mathfrak p}=g\circ\pi\) for a morphism \(g:B/I\to B/\mathfrak p\). The ideal
\(\mathfrak Q=g^{-1}(0)\) satisfies \(\pi^{-1}(\mathfrak Q)=\pi_{\mathfrak p}^{-1}(0)=\mathfrak p\). It is prime:
it does not contain \(1\), and \(\pi(a)\pi(b)\in\mathfrak Q\) means \(ab\in\mathfrak p\). So \(\pi^{\ast}\) is a
bijection onto \(V(I)\). It is continuous, and it maps \(D(\pi(h))\) onto \(D(h)\cap V(I)\); every basic open set of
\(\operatorname{Spec}(B/I)\) is of the form \(D(\pi(h))\).

(d) The bijection is Proposition 2.7. The map is continuous, \(D(a/s)=D(a/1)\), and \(\iota^{\ast}\) maps
\(D(a/1)\) onto the intersection of \(D(a)\) with the image. For \(S=\{h^n\}\) the image is \(D(h)\).

(e) Every \(D(h)\) is stable under generization, hence so is every open set. Conversely let \(U\) be stable under
generization. Its complement contains with each point \(\mathfrak p\) all \(\mathfrak q\supseteq\mathfrak p\), so
it is the union of the finitely many closed sets \(V(\mathfrak p)\), \(\mathfrak p\notin U\). \(\square\)

From now on \(\operatorname{Spec}B\) carries this topology. By Examples 2.2, the spectrum of a monoid is the
spectrum of *Commutative monoids and their spectra*, and the spectrum of a ring is its usual spectrum with the
Zariski topology.

**Theorem 3.3 (the spectrum of a cancellative blueprint).** Let \(B\) be a cancellative blueprint with underlying
monoid \(A\), and let \(R=B_{\mathbb Z}\). The map
\[
\beta:\operatorname{Spec}R\longrightarrow\operatorname{Spec}B,\qquad\mathfrak q\longmapsto\mathfrak q\cap A
\]
is continuous and surjective.

*Proof.* The map \(\beta\) is \(f^{\ast}\) for the morphism \(f:B\to R\), so it is well defined and continuous by
Proposition 3.2(b). Let \(\mathfrak p\) be a prime ideal of \(B\) and \(S=B\setminus\mathfrak p\). By Proposition
2.4(a), \(A\cap\mathfrak pR=\mathfrak p\). So the image of \(S\) in \(R/\mathfrak pR\) does not contain \(0\), and
the localization \(S^{-1}(R/\mathfrak pR)\) is not the zero ring. It has a prime ideal [Stacks, Tag [00E0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Zariski-topology)]. The
preimage \(\mathfrak q\) of this prime ideal in \(R\) is a prime ideal with \(\mathfrak pR\subseteq\mathfrak q\) and
\(\mathfrak q\cap S=\emptyset\). Hence \(\mathfrak q\cap A=\mathfrak p\). \(\square\)

*Reference:* [Lorscheid 2018a, Lemma 1.32]; [Lorscheid 2018c, Exercise 4.8.13].

The theorem fails without the hypothesis. The blueprint \(B\) of Example 1.8 has \(B_{\mathbb Z}=0\), whose
spectrum is empty. But \(\{0\}\) is a prime ideal of \(B\), because \(B=\{0,1,2\}\) has no zero divisors.

**Corollary 3.4 (zero patterns).** Let \(R\) be a ring generated by elements \(t_1,\dots,t_n\), and let
\(B=\mathbb F_1\langle t_1,\dots,t_n\rangle\) be the blueprint of Example 1.11(a). For a field \(k\) and a ring
homomorphism \(x:R\to k\) call
\[
Z(x)=\{i:x(t_i)=0\}\subseteq\{1,\dots,n\}
\]
the *zero pattern* of \(x\), and put \(\mathfrak p_x=\{a\in B:x(a)=0\}\).

(a) The set \(\mathfrak p_x\) consists of \(0\) and of the products \(t_1^{e_1}\cdots t_n^{e_n}\) with \(e_i>0\) for
some \(i\in Z(x)\). So it depends only on \(Z(x)\), and we write \(\mathfrak p_I\) for it if \(I=Z(x)\).

(b) The prime ideals of \(B\) are exactly the sets \(\mathfrak p_I\), where \(I\) runs through the zero patterns of
all homomorphisms from \(R\) to fields.

(c) For zero patterns \(I,I'\) we have \(\mathfrak p_I\subseteq\mathfrak p_{I'}\) if and only if \(I\subseteq I'\).
So \(\operatorname{Spec}B\) is finite, and its open sets are the sets of zero patterns that contain, with a zero
pattern, all smaller zero patterns.

*Proof.* (a) \(x(t_1^{e_1}\cdots t_n^{e_n})=\prod x(t_i)^{e_i}\) is zero if and only if \(e_i>0\) for some
\(i\in Z(x)\). (b) \(B\) is cancellative with ring \(R\). A prime ideal \(\mathfrak q\) of \(R\) is the kernel of
the homomorphism \(x\) from \(R\) to the fraction field of \(R/\mathfrak q\), and then
\(\mathfrak q\cap B=\mathfrak p_x\). Conversely the kernel of every \(x:R\to k\) is a prime ideal. So (b) follows
from Theorem 3.3. (c) If \(I\subseteq I'\), then \(\mathfrak p_I\subseteq\mathfrak p_{I'}\) by (a). If
\(\mathfrak p_I\subseteq\mathfrak p_{I'}\) and \(i\in I\), then \(t_i\in\mathfrak p_I\subseteq\mathfrak p_{I'}\), so
\(i\in I'\). The rest is Proposition 3.2(e). \(\square\)

So the points of the \(\mathbb F_1\)-model of a closed subscheme \(\mathcal X\) of affine \(n\)-space are the
patterns of vanishing coordinates that occur among the points of \(\mathcal X\) with values in fields.
*Reference:* [Lorscheid 2018a, Lemma 4.10] proves this for the models of adjoint Chevalley groups, with
algebraically closed fields.

**Examples 3.5.**

(a) *Affine space.* For \(B=\mathbb F_1[T_1,\dots,T_n]\subseteq\mathbb Z[T_1,\dots,T_n]\) every subset \(I\) is a
zero pattern: take the point with coordinates \(0\) for \(i\in I\) and \(1\) otherwise. So
\(\mathbb A^n_{\mathbb F_1}=\operatorname{Spec}\mathbb F_1[T_1,\dots,T_n]\) has \(2^n\) points \(\mathfrak p_I\),
ordered by inclusion of the sets \(I\), as in *Commutative monoids and their spectra*.

(b) *Blue fields.* The spectrum of a blue field is one point, because \(\{0\}\) is its only ideal other than \(B\).
This applies to \(\mathbb F_1\), \(\mathbb F_{1^n}\), \(\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]\) and
\(\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\).

(c) *\(\mathrm{SL}_2\).* Let \(B_1=\mathbb F_1[\mathrm{SL}_2]\). A homomorphism \(R_1\to k\) is a matrix
\(\begin{pmatrix}a&b\\ c&d\end{pmatrix}\) with entries in \(k\) and \(ad-bc=1\). If \(ad=0\), then \(bc=-1\), so
\(b\) and \(c\) are not zero. If \(bc=0\), then \(ad=1\). So a zero pattern is contained in \(\{a,d\}\) or in
\(\{b,c\}\). All seven such sets occur over \(\mathbb Q\):
\[
\begin{pmatrix}2&1\\1&1\end{pmatrix},\
\begin{pmatrix}0&1\\-1&1\end{pmatrix},\
\begin{pmatrix}1&1\\-1&0\end{pmatrix},\
\begin{pmatrix}0&1\\-1&0\end{pmatrix},\
\begin{pmatrix}1&0\\1&1\end{pmatrix},\
\begin{pmatrix}1&1\\0&1\end{pmatrix},\
\begin{pmatrix}1&0\\0&1\end{pmatrix}
\]
have the zero patterns \(\emptyset\), \(\{a\}\), \(\{d\}\), \(\{a,d\}\), \(\{b\}\), \(\{c\}\), \(\{b,c\}\). So
\(\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\) has seven points. We write them by their generators:

```
      (b,c)           (a,d)
      /   \           /   \
    (b)   (c)       (a)   (d)
       \     \     /     /
              (0)
```

A line joins a point to a point in its closure, which is drawn higher. There are two closed points: \((b,c)\), the
pattern of the diagonal matrices, and \((a,d)\), the pattern of the antidiagonal matrices. For \(B_n\) a zero
pattern is an \(n\)-tuple of such sets, so \(\operatorname{Spec}B_n\) has \(7^n\) points and \(2^n\) closed points.
*Reference:* [Lorscheid 2016, Example 1.6].

(d) *An arithmetic example.* Let \(B=\mathbb F_1\langle2,3,10,15\rangle\subseteq\mathbb Z\). A homomorphism from
\(\mathbb Z\) to a field has the zero pattern \(\{2,10\}\) in characteristic \(2\), \(\{3,15\}\) in characteristic
\(3\), \(\{10,15\}\) in characteristic \(5\), and \(\emptyset\) otherwise. So \(\operatorname{Spec}B\) has four
points: \(\{0\}\) and three closed points \(\mathfrak p_2,\mathfrak p_3,\mathfrak p_5\), where \(\mathfrak p_\ell\)
is the set of elements of \(B\) divisible by \(\ell\).

**Example 3.6 (all relations must be tested).** For a blueprint given by generators and relations, condition (I2)
concerns all relations, not only the generating ones. Take \(B=\mathbb F_1[x]/\!\!/\langle1+1\equiv x,\
1+1+1\equiv x\rangle\) from Example 1.8 and the set \(I\) of all multiples of \(x\). Each generating relation has at
least two terms outside \(I\), so neither one, used in (I2), forces \(1\in I\). But the two relations together give
\(1+x\equiv1+1+1\equiv x\), and the relation \(1+x\equiv x\) does force \(1\in I\). So \(I\) is not an ideal, as
Example 2.2(e) showed, and \(\operatorname{Spec}B\) is the single point \(\{0\}\).

## 4. Blue schemes

### 4.1 The structure sheaf

A *sheaf of blueprints* on a topological space \(X\) assigns to every open set \(U\) a blueprint \(\mathcal O(U)\)
and to every inclusion \(V\subseteq U\) a restriction morphism \(\mathcal O(U)\to\mathcal O(V)\), such that
\(\mathcal O\) is a sheaf of sets and such that a relation \(\sum s_i\equiv\sum t_j\) holds in \(\mathcal O(U)\) as
soon as it holds in \(\mathcal O(U_\alpha)\) for the members of an open cover of \(U\). The *stalk*
\(\mathcal O_x\) at a point \(x\) is the set of germs at \(x\); a relation between germs holds if it holds between
representatives on some neighbourhood of \(x\). A space with a sheaf of blueprints is a *blueprinted space*.

**Definition 4.1.** Let \(B\) be a blueprint and \(X=\operatorname{Spec}B\). For an open subset \(U\) of \(X\) let
\(\mathcal O_X(U)\) be the set of all families \(s=(s(\mathfrak p))_{\mathfrak p\in U}\) with
\(s(\mathfrak p)\in B_{\mathfrak p}\) that are *locally fractions*: every point of \(U\) has a neighbourhood
\(D(h)\subseteq U\) such that, for some \(a\in B\) and \(n\ge0\), \(s(\mathfrak q)=a/h^n\) in \(B_{\mathfrak q}\) for
all \(\mathfrak q\in D(h)\). Families are multiplied pointwise. A relation \(\sum s_i\equiv\sum t_j\) holds in
\(\mathcal O_X(U)\) if \(\sum s_i(\mathfrak p)\equiv\sum t_j(\mathfrak p)\) holds in \(B_{\mathfrak p}\) for every
\(\mathfrak p\in U\).

In the language of Proposition 1.2, \(\mathcal O_X(U)\) is the set of locally fractional families inside the product
semiring \(\prod_{\mathfrak p\in U}B_{\mathfrak p}^+\), together with the sums of such families. So it is a
blueprint. \(\mathcal O_X(\emptyset)\) is the zero blueprint.

**Proposition 4.2.** (a) \(\mathcal O_X\) is a sheaf of blueprints.

(b) For every \(\mathfrak p\in X\) the map \(s\mapsto s(\mathfrak p)\) induces an isomorphism from the stalk
\(\mathcal O_{X,\mathfrak p}\) to \(B_{\mathfrak p}\). In particular the stalks are local blueprints.

*Proof.* (a) Being locally a fraction is a local condition, and relations are tested pointwise.

(b) The map is surjective: an element \(a/s\in B_{\mathfrak p}\), with \(s\notin\mathfrak p\), is the value at
\(\mathfrak p\) of the section \(\mathfrak q\mapsto a/s\) over \(D(s)\). Now let \(s_i,t_j\) be sections near
\(\mathfrak p\) with \(\sum s_i(\mathfrak p)\equiv\sum t_j(\mathfrak p)\) in \(B_{\mathfrak p}\). After shrinking the
neighbourhood to some \(D(h)\) and bringing the fractions to a common denominator, \(s_i=a_i/h^n\) and
\(t_j=b_j/h^n\) on \(D(h)\). By Proposition 2.6(a) there is \(t\notin\mathfrak p\) with
\(\sum ta_i\equiv\sum tb_j\) in \(B\). For every \(\mathfrak q\in D(th)\) this relation shows
\(\sum s_i(\mathfrak q)\equiv\sum t_j(\mathfrak q)\) in \(B_{\mathfrak q}\). So the relation holds on the
neighbourhood \(D(th)\) of \(\mathfrak p\). For a single pair \(s,t\) this says that two sections with the same value
at \(\mathfrak p\) have the same germ, since relations between single elements are equalities. The stalks are local
by Corollary 2.8. \(\square\)

**Theorem 4.3 (basic open sets are affine).** Let \(h\in B\) and let \(\iota:B\to B_h\) be the localization. The
homeomorphism \(\iota^{\ast}:\operatorname{Spec}B_h\to D(h)\) of Proposition 3.2(d) extends to an isomorphism of
blueprinted spaces between \(\operatorname{Spec}B_h\) and \((D(h),\mathcal O_X|_{D(h)})\).

*Proof.* Let \(\mathfrak Q\) be a prime ideal of \(B_h\) and \(\mathfrak p=\iota^{-1}(\mathfrak Q)\). The elements
of \(B\setminus\mathfrak p\) become units in \((B_h)_{\mathfrak Q}\), and \(h\) and the elements \(a/1\) with
\(a\notin\mathfrak p\) become units in \(B_{\mathfrak p}\). By Proposition 2.6(b) there are morphisms
\(B_{\mathfrak p}\to(B_h)_{\mathfrak Q}\) and \((B_h)_{\mathfrak Q}\to B_{\mathfrak p}\) that are compatible with
the maps from \(B\), and they are inverse to each other by the uniqueness in Proposition 2.6(b). So the stalks at
corresponding points are identified. Under this identification a family of germs is locally a fraction of elements
of \(B_h\) if and only if it is locally a fraction of elements of \(B\): the fraction of \(a/h^m\) by a power
\((g/h^k)^n\) on \(D(g/h^k)\) is the fraction \(ah^{kn}/(h^mg^n)\) on \(D(gh)\), and a fraction \(a/g^n\) on
\(D(g)\subseteq D(h)\) is the fraction of \(a/1\) by \((g/1)^n\). Relations are tested in the stalks on both sides.
\(\square\)

*Reference:* [Lorscheid 2012a, Theorem 3.20].

**Definition 4.4.** A blueprinted space is *locally blueprinted* if all its stalks are local blueprints. A
*morphism* of locally blueprinted spaces \((X,\mathcal O_X)\to(Y,\mathcal O_Y)\) is a continuous map
\(\varphi:X\to Y\) together with morphisms of blueprints
\(\varphi^\#_V:\mathcal O_Y(V)\to\mathcal O_X(\varphi^{-1}(V))\) for all open \(V\subseteq Y\), compatible with
restrictions, such that the induced morphisms of stalks \(\mathcal O_{Y,\varphi(x)}\to\mathcal O_{X,x}\) send
non-units to non-units. A *blue scheme* is a locally blueprinted space in which every point has an open
neighbourhood that is isomorphic to \(\operatorname{Spec}B\) for some blueprint \(B\). It is *affine* if it is
isomorphic to some \(\operatorname{Spec}B\). Morphisms of blue schemes are morphisms of locally blueprinted spaces.

A morphism of blueprints \(f:B\to C\) induces a morphism of blue schemes
\(f^{\ast}:\operatorname{Spec}C\to\operatorname{Spec}B\): on points it is the map of Proposition 3.2(b), and a
section \(s\) is sent to the family \(\mathfrak Q\mapsto f_{\mathfrak Q}(s(f^{-1}(\mathfrak Q)))\), where
\(f_{\mathfrak Q}:B_{f^{-1}(\mathfrak Q)}\to C_{\mathfrak Q}\), \(a/s\mapsto f(a)/f(s)\), is given by Proposition
2.6(b). By Theorem 4.3 an open subset of a blue scheme is a blue scheme, and the affine open subsets form a basis
of the topology.

### 4.2 Global sections

For \(X=\operatorname{Spec}B\) write \(\Gamma B=\mathcal O_X(X)\). The map \(\sigma:B\to\Gamma B\) that sends \(a\)
to the family \(\mathfrak p\mapsto a/1\) is a morphism of blueprints. For rings it is an isomorphism, and for
monoids as well. For blueprints in general it is not. We call \(B\) *global* if \(\sigma\) is an isomorphism.

If \(B\) is cancellative, then \(\sigma\) is injective. Indeed, let \(\sigma(a)=\sigma(b)\), let \(R=B_{\mathbb Z}\),
and let \(\mathfrak a\) be the ideal of all \(r\in R\) with \(r(a-b)=0\). Suppose \(\mathfrak a\neq R\). Then there
is a prime ideal \(\mathfrak q\) of \(R\) with \(\mathfrak a\subseteq\mathfrak q\) [Stacks, Tag [00E0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Zariski-topology)], and
\(\mathfrak p=\mathfrak q\cap B\) is a prime ideal of \(B\) (Proposition 3.2(b)). Since \(a/1=b/1\) in
\(B_{\mathfrak p}\), there is \(t\in B\setminus\mathfrak p\) with \(ta=tb\). Then
\(t\in\mathfrak a\cap B\subseteq\mathfrak p\), a contradiction.
So \(1\in\mathfrak a\), and \(a=b\). Without the hypothesis \(\sigma\) need not be injective. The semiring
\(B=\{0,1,2\}\) of Example 1.8 has the single prime ideal \(\{0\}\), and in \(B_{\{0\}}\) we have \(1/1=2/1\),
because \(2\cdot1=2\cdot2\). So \(\sigma(1)=\sigma(2)\). *Reference:* [Lorscheid 2012a, Lemma 3.10] states the
injectivity for every blueprint in the sense of this lesson; the statement needs the hypothesis that \(B\) is
cancellative.

**Lemma 4.5 (blueprints inside a field).** Let \(K\) be a field and let \(B=(A\subset B^+)\) be a non-zero blueprint
such that \(B^+\) is a subsemiring of \(K\). For a prime ideal \(\mathfrak p\) put
\(A_{\mathfrak p}=\{as^{-1}:a\in A,\ s\in A\setminus\mathfrak p\}\subseteq K\), and let \(X=\operatorname{Spec}B\).

(a) \(B_{\mathfrak p}\) is the subblueprint of \(K\) on \(A_{\mathfrak p}\).

(b) \(\{0\}\) is a prime ideal of \(B\), and it lies in every non-empty open subset of \(X\). Every open subset of
\(X\) is connected.

(c) For a non-empty open set \(U\), the blueprint \(\mathcal O_X(U)\) is the subblueprint of \(K\) on
\(\bigcap_{\mathfrak p\in U}A_{\mathfrak p}\).

(d) \(B\) is global if and only if \(A=\bigcap_{\mathfrak p}A_{\mathfrak p}\). Here \(\mathfrak p\) may run through
all prime ideals, or through a set of prime ideals such that every prime ideal is contained in one of them.

*Proof.* (a) For \(S=A\setminus\mathfrak p\) the maps \(S^{-1}A\to K\) and \(S^{-1}B^+\to K\), \(x/s\mapsto xs^{-1}\),
are injective, because \(ts'x=tsx'\) implies \(s'x=sx'\) in a field. (b) The set \(\{0\}\) is an ideal, \(1\neq0\),
and \(A\) has no zero divisors. So \(\{0\}\) is prime. If \(D(h)\) is not empty, then \(h\neq0\) and
\(\{0\}\in D(h)\). So any two non-empty open sets meet, and no open set is the union of two disjoint non-empty open
subsets. (c) Let \(s\in\mathcal O_X(U)\). Near each point, \(s\) is a fraction \(a/h^n\), which is one element of
\(K\). So \(\mathfrak p\mapsto s(\mathfrak p)\in K\) is locally constant, hence constant by (b), and its value lies
in all \(A_{\mathfrak p}\), \(\mathfrak p\in U\). Conversely let \(c\in\bigcap_{\mathfrak p\in U}A_{\mathfrak p}\).
At \(\mathfrak p\in U\) write \(c=a/s\) with \(s\notin\mathfrak p\) and choose \(g\) with
\(\mathfrak p\in D(g)\subseteq U\). Then \(c=ag/(gs)\) on \(D(gs)\). So the constant family \(c\) is a section.
Relations are tested in the stalks, that is, in \(K\). (d) By (c), \(\sigma\) is the inclusion of \(A\) into
\(\bigcap_{\mathfrak p}A_{\mathfrak p}\). If \(\mathfrak q\subseteq\mathfrak p\), then
\(A_{\mathfrak p}\subseteq A_{\mathfrak q}\). \(\square\)

**Examples 4.6.**

(a) *A blueprint that is not global.* Let \(B=\mathbb F_1\langle2,3,10,15\rangle\subseteq\mathbb Z\) as in Example
3.5(d), inside \(K=\mathbb Q\). Its underlying monoid is
\(A=\{0\}\cup\{2^x3^y5^z:x,y,z\ge0,\ z\le x+y\}\), which does not contain \(5\). The three closed points give
\[
A_{\mathfrak p_2}=\{0\}\cup\{2^x3^y5^z:x\ge0\},\quad
A_{\mathfrak p_3}=\{0\}\cup\{2^x3^y5^z:y\ge0\},\quad
A_{\mathfrak p_5}=\{0\}\cup\{2^x3^y5^z:z\ge0\},
\]
with the other exponents arbitrary integers. For example \(5=15/3\in A_{\mathfrak p_2}\) and
\(5=10/2\in A_{\mathfrak p_3}\). By Lemma 4.5 the blueprint of global sections is
\(\Gamma B=\mathbb F_1\langle2,3,5\rangle\). It contains the section \(5\), which is \(10/2\) on \(D(2)\) and
\(15/3\) on \(D(3)\), and \(5\notin B\). So \(B\) is not global. The spectrum of \(\Gamma B\) has again four points.

(b) *The blueprints \(B_n\) of Proposition 1.12 are global.* The ring \(R_n\) is contained in the field
\(K=\mathbb Q(a_i,b_i,c_i:1\le i\le n)\): sending \(d_i\) to \((b_ic_i+1)/a_i\) maps the reduced monomials to
linearly independent elements of \(\mathbb Z[a_i^{\pm1},b_i,c_i]\). The elements \(a_i,b_i,c_i,b_ic_i+1\) are
pairwise non-associated irreducible elements of the polynomial ring \(\mathbb Z[a_i,b_i,c_i:1\le i\le n]\). So the
elements \(a_i,b_i,c_i,d_i\) are multiplicatively independent in \(K^\times\), and every element of the group they
generate is a Laurent monomial with unique exponents. By Example 3.5(c) every prime ideal lies in one of the
\(2^n\) closed points, and the complement of a closed point consists of the monomials in \(2n\) of the variables:
for each \(i\) either in \(a_i,d_i\) or in \(b_i,c_i\). So for a closed point \(\mathfrak p\), the set
\(A_{\mathfrak p}\) consists of \(0\) and of the Laurent monomials in which the \(2n\) variables that lie in
\(\mathfrak p\) have exponents \(\ge0\). Every variable lies in some closed point. So the intersection of the sets
\(A_{\mathfrak p}\) is the set of monomials with all exponents \(\ge0\), together with \(0\). This is \(A\), and
\(B_n\) is global by Lemma 4.5(d).

**Proposition 4.7.** Every local blueprint is global. In particular non-zero monoids and blue fields are global.

*Proof.* Let \(\mathfrak m=B\setminus B^\times\). It is a prime ideal, because a product of two units is a unit. If
\(\mathfrak m\in D(h)\), then \(h\) is a unit and \(D(h)=X\). So a global section \(s\) is of the form \(a/h^n\) on
all of \(X\) with \(h\) a unit, and \(s=\sigma(ah^{-n})\). The map \(B\to B_{\mathfrak m}\) is an isomorphism, since
the elements outside \(\mathfrak m\) are units already. Evaluating at \(\mathfrak m\) shows that \(\sigma\) is
injective and that a relation between sections \(\sigma(a_i)\), \(\sigma(b_j)\) implies the relation between the
\(a_i\) and \(b_j\) in \(B\). \(\square\)

**Example (a local blueprint with three points).** Let \(k_1\) and \(k_2\) be fields, let \(A=k_1\times k_2\) with
componentwise multiplication, and let \(U=k_1^\times\times k_2^\times\) be its group of units. Let
\(\mathbb N[U]\) be the semiring of formal sums of elements of \(U\). Define
\(\iota:A\to k_1\times k_2\times\mathbb N[U]\) by \(\iota(a,b)=(a,b,(a,b))\) if \((a,b)\in U\), and
\(\iota(a,b)=(a,b,0)\) otherwise. The target is a product of three semirings, and \(\iota\) is injective and
multiplicative. Let \(B=(\iota(A)\subset S)\), where \(S\) is the set of sums of elements of \(\iota(A)\). A relation
\(\sum x_i\equiv\sum y_j\) holds in \(B\) if and only if the units among the \(x_i\) and among the \(y_j\) are the
same, with multiplicities, and the first coordinates of the remaining terms have the same sum in \(k_1\) on both
sides, and their second coordinates have the same sum in \(k_2\). So
\(B\) is the monoid \(A\) with the relations that hold in \(k_1\) between the elements \((a,0)\), the relations that
hold in \(k_2\) between the elements \((0,b)\), and their consequences.

The set \(\mathfrak m=A\setminus U\) of non-units is an ideal: (I1) is clear, and in a relation
\(a+\sum b_j\equiv\sum c_k\) with \(b_j,c_k\in\mathfrak m\) the right side contains no unit, so \(a\) is not a unit.
So \(B\) is local, and by Proposition 4.7 it is global. Its prime ideals are \(\mathfrak p_1=k_1\times\{0\}\),
\(\mathfrak p_2=\{0\}\times k_2\) and \(\mathfrak m=\mathfrak p_1\cup\mathfrak p_2\). Indeed, the two projections
\(B\to k_2\) and \(B\to k_1\) are morphisms, and \(\mathfrak p_1\) and \(\mathfrak p_2\) are their preimages of
\(0\). A prime ideal \(\mathfrak p\) contains \((1,0)\) or \((0,1)\), because their product is \(0\). So it contains
\(\mathfrak p_1\) or \(\mathfrak p_2\). If it is larger than \(\mathfrak p_1\), it contains an element \((a,b)\) with
\(b\neq0\). This element is not a unit, so \(a=0\). Then \((0,1)=(1,b^{-1})(0,b)\in\mathfrak p\), so
\(\mathfrak p\) contains \(\mathfrak p_2\), and \(\mathfrak p=\mathfrak m\). So \(\operatorname{Spec}B\) has the
closed point \(\mathfrak m\) and two further points. *Reference:* [Lorscheid 2016, Example 1.8] treats this
blueprint with the two prime ideals \(\mathfrak p_1\) and \(\mathfrak p_2\) only, as an example of a blueprint that
is not global; with the third prime ideal \(\mathfrak m\) it is local, hence global. Example 4.6(a) is a blueprint
that is not global.

**Theorem 4.8.** Let \(B\) be a blueprint and \(\sigma:B\to\Gamma B\) as above.

(a) The morphism \(\sigma^{\ast}:\operatorname{Spec}\Gamma B\to\operatorname{Spec}B\) is an isomorphism of blue
schemes. So \(\Gamma B\) is global.

(b) Let \(X\) be a blue scheme and \(Y=\operatorname{Spec}B\). The map \(\varphi\mapsto\varphi^\#_Y\circ\sigma\) is
a bijection from the morphisms \(X\to Y\) to the morphisms of blueprints \(B\to\mathcal O_X(X)\), and it is natural
in \(X\) and \(B\). In particular, if \(C\) is a global blueprint, the morphisms
\(\operatorname{Spec}C\to\operatorname{Spec}B\) are the morphisms \(f^{\ast}\) with \(f:B\to C\).

(c) Every morphism of blue schemes is, locally on source and target, of the form \(f^{\ast}\).

(d) \(\operatorname{Spec}\mathbb F_1\) is a final object of the category of blue schemes. The blue scheme
\(\operatorname{Spec}(B\otimes_{\mathbb F_1}B')\), with the morphisms that belong to \(B\to B\otimes_{\mathbb F_1}B'\)
and \(B'\to B\otimes_{\mathbb F_1}B'\), is a product of \(\operatorname{Spec}B\) and \(\operatorname{Spec}B'\); we
write \(\operatorname{Spec}B\times\operatorname{Spec}B'\) for it. The category of blue schemes has all fibre
products.

*Proof of (b) and of the first two statements of (d).* The argument is the one for locally ringed spaces
[Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)]. For a morphism \(\varphi:X\to Y\) put \(f_\varphi=\varphi^\#_Y\circ\sigma\).

Let \(f:B\to\mathcal O_X(X)\) be a morphism of blueprints. For \(x\in X\) let \(f_x:B\to\mathcal O_{X,x}\) be \(f\)
followed by the passage to germs at \(x\), and let \(\mathfrak m_x\) be the set of non-units of the local blueprint
\(\mathcal O_{X,x}\). It is a prime ideal. Put \(\varphi(x)=f_x^{-1}(\mathfrak m_x)\), a prime ideal of \(B\) by
Proposition 3.2(b). For \(h\in B\) let \(X_h\) be the set of all \(x\) such that \(f_x(h)\) is a unit. Then
\(\varphi^{-1}(D(h))=X_h\). If \(x\in X_h\), the germ \(f_x(h)\) has an inverse germ, so \(f(h)\) has an inverse on
a neighbourhood of \(x\). Hence \(X_h\) is open and \(\varphi\) is continuous. Inverses in a monoid are unique, so
the local inverses glue to an inverse of \(f(h)\) over \(X_h\), which we write \(f(h)^{-1}\).

Let \(V\subseteq Y\) be open and \(s\in\mathcal O_Y(V)\). If \(s=a/h^n\) on \(D(h)\subseteq V\), consider the section
\(f(a)f(h)^{-n}\) over \(X_h\). Let also \(s=a'/h'^{\,n'}\) on \(D(h')\subseteq V\), and let \(x\in X_h\cap X_{h'}\)
and \(\mathfrak q=\varphi(x)\). Then \(a/h^n=a'/h'^{\,n'}\) in \(B_{\mathfrak q}\), so \(th'^{\,n'}a=th^na'\) for some
\(t\notin\mathfrak q\). Apply \(f\). Since \(f_x(t)\), \(f_x(h)\) and \(f_x(h')\) are units, the sections
\(f(a)f(h)^{-n}\) and \(f(a')f(h')^{-n'}\) have the same germ at \(x\). So they agree on \(X_h\cap X_{h'}\), and all
these sections glue to a section \(\varphi^\#_V(s)\) over \(\varphi^{-1}(V)\). The maps \(\varphi^\#_V\) are
morphisms of monoids, and they are compatible with restrictions. They preserve relations. Indeed, let
\(\sum s_i\equiv\sum s'_j\) in \(\mathcal O_Y(V)\), let \(x\in\varphi^{-1}(V)\) and \(\mathfrak q=\varphi(x)\), and
write \(s_i=a_i/h^n\) and \(s'_j=a'_j/h^n\) on some \(D(h)\) that contains \(\mathfrak q\). By Proposition 2.6(a)
there is \(t\notin\mathfrak q\) with \(\sum ta_i\equiv\sum ta'_j\) in \(B\). Applying \(f\) and multiplying by the
inverse of \(f(t)f(h)^n\) gives \(\sum\varphi^\#_V(s_i)\equiv\sum\varphi^\#_V(s'_j)\) on the neighbourhood
\(X_{th}\) of \(x\). The map of stalks \(B_{\mathfrak q}\to\mathcal O_{X,x}\) sends \(a/h\) to
\(f_x(a)f_x(h)^{-1}\), and \(f_x(a)\) is a non-unit for \(a\in\mathfrak q\). So
\(\varphi_f=(\varphi,\varphi^\#)\) is a morphism of blue schemes. It satisfies \(f_{\varphi_f}=f\), because
\(\varphi^\#_Y(\sigma(a))=f(a)\).

Conversely let \(\psi:X\to Y\) be a morphism and \(f=f_\psi\). For \(x\in X\) and \(\mathfrak q=\psi(x)\) the map
of stalks \(B_{\mathfrak q}\to\mathcal O_{X,x}\) sends \(b/1\) to \(f_x(b)\); it sends units to units and non-units
to non-units. So \(b\in\mathfrak q\) if and only if \(f_x(b)\in\mathfrak m_x\), and \(\psi\) and \(\varphi_f\)
agree on points. If \(s=a/h^n\) on \(D(h)\), then \(\psi^\#(s)\,f(h)^n=f(a)\) over \(X_h\), because
\(s\,\sigma(h)^n=\sigma(a)\) over \(D(h)\). So \(\psi=\varphi_f\). The bijection is natural:
\(f_{\varphi\circ\chi}=\chi^\#_X\circ f_\varphi\) for a morphism \(\chi:X'\to X\), and
\(f_{g^{\ast}\circ\varphi}=f_\varphi\circ g\) for a morphism of blueprints \(g:B\to B''\) and a morphism
\(\varphi:X\to\operatorname{Spec}B''\). If \(C\) is a global blueprint and \(f:B\to C\), then
\((f^{\ast})^\#_Y\circ\sigma=\sigma_C\circ f\), where \(\sigma_C:C\to\Gamma C\) is an isomorphism. So
\(f\mapsto f^{\ast}\) is a bijection from the morphisms \(B\to C\) to the morphisms
\(\operatorname{Spec}C\to\operatorname{Spec}B\).

By (b) and Example 1.5(c) there is exactly one morphism \(X\to\operatorname{Spec}\mathbb F_1\). By (b) and
Proposition 1.14(a), a morphism \(X\to\operatorname{Spec}(B\otimes_{\mathbb F_1}B')\) is the same as a pair of
morphisms \(B\to\mathcal O_X(X)\), \(B'\to\mathcal O_X(X)\), that is, a pair of morphisms
\(X\to\operatorname{Spec}B\), \(X\to\operatorname{Spec}B'\); by naturality the pair consists of the composites with
the two morphisms in (d). \(\square\)

Sections 6, 7 and 9 use only (b) and these two statements of (d). The lesson does not prove (a), (c) and the
existence of fibre products in general. *Reference:* [Lorscheid 2012a, Theorem 3.12, Corollary 3.14, Theorem 3.23,
Corollary 3.26 and Proposition 3.27]. The proof of (a) given there refers to the proof for rings, which uses that
\(B_h\to\mathcal O_X(D(h))\) is injective for every \(h\in B\). By the beginning of this subsection and Theorem 4.3
this holds for cancellative blueprints. For blueprints that are not cancellative, (a) and (c) need a separate
argument, which this lesson does not give.

### 4.3 Monoid schemes, schemes and semiring schemes

*Monoids.* Let \(A\) be a monoid. By Example 2.2(b), \(\operatorname{Spec}A\) is the same space for the blueprint
\(A\) as for the monoid \(A\). A localization of \(A\) as a blueprint is the localization of the monoid, again with
the equality relation as pre-addition. The sections of Definition 4.1 are the families of germs that are locally
fractions, as in *Commutative monoids and their spectra*. So the blueprinted space \(\operatorname{Spec}A\) is the
affine monoid scheme of the monoid \(A\), and each monoid of sections carries in addition a pre-addition:
\(\sum s_i\equiv\sum t_j\) holds if at every point the non-zero germs on the two sides agree, counted with
multiplicity. A morphism of sheaves of monoids preserves these relations. Hence the monoid schemes of the lesson
*Monoid schemes* are the blue schemes that have an open cover by spectra of monoids, and the morphisms are the
same. *Reference:* [Lorscheid 2012a, Section 3.7].

The pre-addition of \(\mathcal O_X(U)\) need not be the equality relation. The disjoint union \(X\) of two copies of
\(\operatorname{Spec}\mathbb F_1\) has \(\mathcal O_X(X)=\mathbb F_1\times\mathbb F_1\), with the relation
\((1,0)+(0,1)\equiv(1,1)\). *Reference:* [Lorscheid 2012a, Remark 3.33] gives this example.
[Lorscheid 2016, Section 1.3] characterizes monoid schemes by the condition that all blueprints of sections are
monoids; by the example this condition cannot be required for disconnected open sets, so we use open covers, as
in [Lorscheid 2012a, Section 3.7].

*Rings.* For a ring \(R\), Examples 2.2(c) and Definition 4.1 show that \(\operatorname{Spec}R\) is the affine
scheme of \(R\) [Stacks, Tag [01HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-affine-schemes)], each ring of sections being regarded as a blueprint. So schemes are the blue
schemes that have an open cover by spectra of rings, with the same morphisms. A *semiring scheme* is a blue scheme
that has an open cover by spectra of semirings. *Reference:* [Lorscheid 2012a, Section 3.8].

### 4.4 Base extension

For a blueprint \(B\) the morphisms \(B\to B^+\to B_{\mathbb Z}\) induce morphisms
\[
\operatorname{Spec}B_{\mathbb Z}\longrightarrow\operatorname{Spec}B^+
\overset{\alpha}{\longrightarrow}\operatorname{Spec}B .
\]
We write \(X^+=\operatorname{Spec}B^+\) and \(X_{\mathbb Z}=\operatorname{Spec}B_{\mathbb Z}\) for
\(X=\operatorname{Spec}B\), and \(\beta:X_{\mathbb Z}\to X\) for the composite. For a general blue scheme \(X\)
these constructions glue: there are a semiring scheme \(X^+\) and a scheme \(X_{\mathbb Z}\) with morphisms
\(\alpha:X^+\to X\) and \(\beta:X_{\mathbb Z}\to X\), such that every morphism from a semiring scheme to \(X\)
factors through \(\alpha\) in exactly one way, and every morphism from a scheme to \(X\) factors through \(\beta\) in
exactly one way. If \(X\) is covered by open subsets \(\operatorname{Spec}B_i\), then \(X^+\) and \(X_{\mathbb Z}\)
are covered by the open subsets \(\operatorname{Spec}B_i^+\) and \(\operatorname{Spec}(B_i)_{\mathbb Z}\). The gluing
is possible because localization commutes with \((-)^+\) and \((-)_{\mathbb Z}\) (Proposition 2.6). We do not prove
the general statement; *Reference:* [Lorscheid 2012a, Proposition 3.31 and Section 3.8]. The scheme \(X_{\mathbb Z}\)
is the *base extension of \(X\) to \(\mathbb Z\)*, and \(X^+\) is the base extension to semirings. For a ring \(k\)
one puts \(X_k=X_{\mathbb Z}\times_{\operatorname{Spec}\mathbb Z}\operatorname{Spec}k\). [Lorscheid 2018a] writes
\(X^+_{\mathbb Z}\) and \(X^+_k\).

For a monoid \(A\) we have \(A_{\mathbb Z}=\mathbb Z[A]\), so for a monoid scheme \(X\) the scheme \(X_{\mathbb Z}\)
is the base change of the lesson *Monoid schemes*. For a scheme \(X\) we have \(X_{\mathbb Z}=X\). By Theorem 3.3
the map \(\beta\) is surjective if \(X\) has an open cover by spectra of cancellative blueprints.

*Points.* For \(X=\operatorname{Spec}B\) and a blueprint \(C\) put \(X(C)=\operatorname{Hom}(B,C)\). If \(C\) is
global, these are the morphisms \(\operatorname{Spec}C\to X\), by Theorem 4.8(b). For a semiring \(C\) we have
\(X(C)=\operatorname{Hom}(B^+,C)\) by (1.1): points with values in semirings depend only on \(B^+\). For a ring
\(C\) we have \(X(C)=X_{\mathbb Z}(C)\) by (1.2).

*Products.* By Proposition 1.14, \((X\times Y)^+=X^+\times Y^+\), the product in the category of semiring schemes,
and \((X\times Y)_{\mathbb Z}=X_{\mathbb Z}\times Y_{\mathbb Z}\), for affine blue schemes \(X\) and \(Y\). For all
blue schemes the first formula is stated in [Lorscheid 2018a, Section 1.1]; this lesson uses the affine case only.

## 5. Proj and projective space

A reference for this section is [López Peña–Lorscheid 2012].

**Definition 5.1.** A *graded blueprint* is a blueprint \(B\) with underlying monoid \(A\), together with subsets
\(A_i\subseteq A\) for \(i\in\mathbb N\), such that:

- \(A=\bigcup_iA_i\), \(A_i\cap A_j=\{0\}\) for \(i\neq j\), \(1\in A_0\), and \(A_iA_j\subseteq A_{i+j}\);
- the pre-addition is *homogeneous*: if \(\sum a_k\equiv\sum b_l\) is a relation of \(B\), then for every \(i\) the
  terms of degree \(i\) on the two sides form a relation \(\sum_{a_k\in A_i}a_k\equiv\sum_{b_l\in A_i}b_l\).

A non-zero element of \(A_i\) is *homogeneous of degree \(i\)*. We put \(A_+=\bigcup_{i>0}A_i\).

So \(B^+\) is a graded semiring: it is the direct sum of the sets \(B_i^+\) of sums of elements of \(A_i\). If the
pre-addition of \(B\) is generated by relations between elements of the same degree, it is homogeneous: the pairs
\((x,y)\) whose parts \(x_i,y_i\) of every degree \(i\) satisfy \(x_i\equiv y_i\) form a congruence that contains the
generators, and it is contained in the pre-addition. The set \(A_+\) is an ideal of \(B\): in (I2), a relation
\(a+\sum b_j\equiv\sum c_k\) with \(b_j,c_k\in A_+\) and \(a\in A_0\) has the degree \(0\) part \(a\equiv0\).

In a graded blueprint in this sense every element is homogeneous. [López Peña–Lorscheid 2012, Section 2] allows in
addition elements that are sums of homogeneous elements of different degrees; we do not need them, by
Proposition 5.4(a).

**Examples.** (a) The free blueprint \(B[T_0,\dots,T_n]\) of Example 1.11(d) is graded by the degree of the monomial:
\(A_i\) consists of \(0\) and the elements \(aT^e\) with \(e_0+\dots+e_n=i\). (b) If \(R=\bigoplus_iR_i\) is a graded
ring, then \(R_{\mathrm{hom}}=(\bigcup_iR_i\subset R)\) is a graded blueprint. (c) If \(t_0,\dots,t_n\) are
homogeneous elements of degree \(1\) of a graded ring \(R\), then \(\mathbb F_1\langle t_0,\dots,t_n\rangle\) is a
graded blueprint: a product of \(i\) of the \(t_j\) lies in \(R_i\), and the relations are homogeneous because \(R\)
is a direct sum of the \(R_i\).

Let \(B\) be a graded blueprint and \(S\subseteq A\) a multiplicative subset. A non-zero fraction \(a/s\) in
\(S^{-1}B\) has the *degree* \(\deg a-\deg s\in\mathbb Z\); this is well defined, because \(ts'a=tsa'\neq0\) forces
\(\deg a-\deg s=\deg a'-\deg s'\). We write \((S^{-1}B)_0\) for the subblueprint of \(S^{-1}B\) on the set of \(0\)
and of the fractions of degree \(0\). For \(h\in A\) and a prime ideal \(\mathfrak p\) we put
\[
B_{(h)}=(B_h)_0,\qquad B_{(\mathfrak p)}=(B_{\mathfrak p})_0 .
\]

**Definition 5.2.** Let \(B\) be a graded blueprint. The set \(\operatorname{Proj}B\) consists of the prime ideals of
\(B\) that do not contain \(A_+\). It carries the topology induced from \(\operatorname{Spec}B\). For \(h\in A\) put
\(D_+(h)=D(h)\cap\operatorname{Proj}B\). For an open subset \(U\) of \(\operatorname{Proj}B\) let \(\mathcal O(U)\)
be the set of all families \(s=(s(\mathfrak p))_{\mathfrak p\in U}\) with \(s(\mathfrak p)\in B_{(\mathfrak p)}\)
that are locally of the form \(a/g\), with \(a\) and \(g\) of the same degree and \(g\notin\mathfrak q\) for all
\(\mathfrak q\) in a neighbourhood. Multiplication and relations are defined pointwise, as in Definition 4.1.

The sets \(D_+(h)\) with \(h\in A_+\) cover \(\operatorname{Proj}B\), because a point of \(\operatorname{Proj}B\)
does not contain all of \(A_+\). They form a basis of the topology: \(D_+(g)\cap D_+(h)=D_+(gh)\), and for
\(g\in A_0\) the set \(D_+(g)\) is the union of the sets \(D_+(gh)\), \(h\in A_+\).

**Theorem 5.3.** Let \(B\) be a graded blueprint and \(h\in A\) homogeneous of degree \(d>0\).

(a) The map \(\varphi:D_+(h)\to\operatorname{Spec}B_{(h)}\),
\(\mathfrak p\mapsto\{a/h^n\in B_{(h)}:a\in\mathfrak p\}\), is a homeomorphism.

(b) For \(\mathfrak p\in D_+(h)\) the inclusion \(B_{(h)}\to B_{(\mathfrak p)}\) induces an isomorphism
\((B_{(h)})_{\varphi(\mathfrak p)}\to B_{(\mathfrak p)}\).

(c) By (a) and (b), \((D_+(h),\mathcal O|_{D_+(h)})\) is isomorphic to \(\operatorname{Spec}B_{(h)}\). So
\(\operatorname{Proj}B\) is a blue scheme, and its stalk at \(\mathfrak p\) is \(B_{(\mathfrak p)}\).

*Proof.* (a) The set \(\varphi(\mathfrak p)\) is the preimage of the prime ideal \(\mathfrak pB_h\) of \(B_h\)
(Proposition 2.7) under the inclusion \(B_{(h)}\to B_h\). So it is a prime ideal of \(B_{(h)}\), and
\(a/h^n\in\varphi(\mathfrak p)\) if and only if \(a\in\mathfrak p\).

We construct the inverse map. Let \(\mathfrak Q\) be a prime ideal of \(B_{(h)}\). Let \(\psi(\mathfrak Q)\) be the
set consisting of \(0\) and of all \(a\in A\), homogeneous of some degree \(m\), with
\(a^d/h^m\in\mathfrak Q\). We show that \(\psi(\mathfrak Q)\) is a prime ideal of \(B\).

(I1): if \(a\in\psi(\mathfrak Q)\) has degree \(m\) and \(b\) has degree \(k\), then
\((ab)^d/h^{m+k}=(a^d/h^m)(b^d/h^k)\in\mathfrak Q\).

(I2): let \(a+\sum b_j\equiv\sum c_k\) be a relation of \(B\) with \(b_j,c_k\in\psi(\mathfrak Q)\), and let \(a\neq0\)
have degree \(m\). Since the pre-addition is homogeneous, we may drop all terms of degree different from \(m\). Raise
the relation to the \(d\)-th power; this is allowed because a pre-addition is compatible with products. On the left
we get \(a^d\) plus a sum of products of \(d\) factors, each containing at least one \(b_j\). On the right we get a
sum of products of \(d\) factors \(c_k\). All these products have degree \(md\) or are zero. Map the relation to
\(B_h\) and multiply it by \(1/h^m\). We get a relation
\[
\frac{a^d}{h^m}+\sum_u\frac{u}{h^m}\equiv\sum_v\frac{v}{h^m}
\]
between elements of \(B_{(h)}\), where every \(u\) and every \(v\) is of the form \(u=yb\) with
\(b\in\psi(\mathfrak Q)\) of degree \(m\) and \(y\) of degree \(m(d-1)\). For such a product,
\[
\Bigl(\frac{yb}{h^m}\Bigr)^d=\frac{b^d}{h^m}\cdot\frac{y^d}{h^{m(d-1)}}\in\mathfrak Q ,
\]
because the first factor lies in \(\mathfrak Q\) and the second lies in \(B_{(h)}\). Since \(\mathfrak Q\) is prime,
\(yb/h^m\in\mathfrak Q\). So all terms of the relation except \(a^d/h^m\) lie in \(\mathfrak Q\), and (I2) for
\(\mathfrak Q\) gives \(a^d/h^m\in\mathfrak Q\). Hence \(a\in\psi(\mathfrak Q)\).

Prime: \(1\notin\psi(\mathfrak Q)\), because \(1/1\notin\mathfrak Q\). If \(ab\in\psi(\mathfrak Q)\) with \(a,b\) of
degrees \(m,k\), then \((a^d/h^m)(b^d/h^k)\in\mathfrak Q\), so one factor lies in \(\mathfrak Q\). Finally
\(h\notin\psi(\mathfrak Q)\), because \(h^d/h^d=1\). So \(\psi(\mathfrak Q)\in D_+(h)\).

The two maps are inverse to each other. First,
\(\varphi(\psi(\mathfrak Q))=\{a/h^n:(a/h^n)^d\in\mathfrak Q\}=\mathfrak Q\). Second, a homogeneous element \(a\) of
degree \(m\) lies in \(\psi(\varphi(\mathfrak p))\) if and only if \(a^d/h^m\in\varphi(\mathfrak p)\), that is,
\(a^d\in\mathfrak p\), that is, \(a\in\mathfrak p\).

For \(g\) homogeneous of degree \(k\) we have \(g\notin\mathfrak p\) if and only if
\(g^d/h^k\notin\varphi(\mathfrak p)\). So \(\varphi\) maps \(D_+(gh)\) onto \(D(g^d/h^k)\). The sets \(D_+(gh)\) form
a basis of \(D_+(h)\), and every basic open set \(D(a/h^n)\) of \(\operatorname{Spec}B_{(h)}\) is the image of
\(D_+(ah)\). Hence \(\varphi\) is a homeomorphism.

(b) Let \(\mathfrak Q=\varphi(\mathfrak p)\) and \(S=B_{(h)}\setminus\mathfrak Q\). By Proposition 2.6(d),
\(S^{-1}B_{(h)}\) is a subblueprint of \(S^{-1}B_h\). The blueprint \(S^{-1}B_h\) is the localization of \(B\) at the
multiplicative set generated by \(h\) and by the elements \(g\notin\mathfrak p\) whose degree is a multiple of
\(d\). This is \(B_{\mathfrak p}\): if \(u\notin\mathfrak p\) is homogeneous, then \(u^d\) is inverted, hence \(u\)
is inverted. So \((B_{(h)})_{\mathfrak Q}\) is a subblueprint of \(B_{\mathfrak p}\), contained in
\(B_{(\mathfrak p)}\). It is all of \(B_{(\mathfrak p)}\): an element \(a/g\) with \(a,g\) of degree \(m\) and
\(g\notin\mathfrak p\) is the fraction of \(ag^{d-1}/h^m\) by \(g^d/h^m\).

(c) Under the identifications of (a) and (b), families that are locally of the form \(a/g\) with \(a,g\) of the same
degree correspond to families that are locally fractions of elements of \(B_{(h)}\), by the formula at the end of
the proof of (b). Relations are tested in the stalks on both sides. \(\square\)

*Reference:* [López Peña–Lorscheid 2012, Theorem 2.1] states this, for the more general graded blueprints of that
paper, by analogy with graded rings. The proof for rings uses the binomial formula to show that the inverse map
produces an ideal; for blueprints this step is replaced by the argument for (I2) above.

**Proposition 5.4.**

(a) Let \(R\) be a graded ring. Then \(\operatorname{Proj}R_{\mathrm{hom}}\) is the scheme \(\operatorname{Proj}R\)
of [Stacks, Tag [01M3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-proj)].

(b) Let \(B\) be a graded blueprint. Then \(B_{\mathbb Z}\) is a graded ring, \((B_{(h)})_{\mathbb Z}\) is the ring
\((B_{\mathbb Z})_{(h)}\) for every homogeneous \(h\) of positive degree, and
\((\operatorname{Proj}B)_{\mathbb Z}\cong\operatorname{Proj}B_{\mathbb Z}\). The same holds with \(B^+\) in place of
\(B_{\mathbb Z}\), where \(\operatorname{Proj}B^+\) means \(\operatorname{Proj}(B^+)_{\mathrm{hom}}\).

*Proof.* (a) As in Example 2.2(c), a subset \(I\) of \(\bigcup_iR_i\) is an ideal of the blueprint
\(R_{\mathrm{hom}}\) if and only if each \(I\cap R_i\) is a subgroup of \(R_i\) and \(R_jI\subseteq I\) for all
\(j\). So \(I\mapsto\bigoplus_i(I\cap R_i)\) is a bijection from the ideals of \(R_{\mathrm{hom}}\) to the
homogeneous ideals of \(R\). A homogeneous ideal \(\mathfrak a\) is prime if and only if \(fg\in\mathfrak a\)
implies \(f\in\mathfrak a\) or \(g\in\mathfrak a\) for homogeneous \(f,g\): if \(f,g\notin\mathfrak a\), remove from
\(f\) and \(g\) the components that lie in \(\mathfrak a\); then the product of the components of lowest degree is
the component of lowest degree of \(fg\) modulo \(\mathfrak a\). So the points of
\(\operatorname{Proj}R_{\mathrm{hom}}\) are the homogeneous prime ideals of \(R\) that do not contain
\(\bigoplus_{i>0}R_i\). The blueprint \((R_{\mathrm{hom}})_{(h)}\) is the ring \(R_{(h)}\) of elements of degree
\(0\) in \(R_h\), and the sheaves are defined in the same way.

(b) \(B^+\) is graded, so its group completion \(B_{\mathbb Z}\) is a graded ring. The natural map
\((B_{(h)})^+\to B^+_h\) is injective, because \(B_{(h)}\) is a subblueprint of \(B_h\) and \((B_h)^+=B_h^+\). Its
image consists of the sums of fractions \(a/h^n\) of degree \(0\). These are the fractions \(x/h^n\) with
\(x\in B^+_{nd}\), that is, the elements of degree \(0\) of \(B^+_h\). Passing to group completions gives
\((B_{(h)})_{\mathbb Z}=(B_{\mathbb Z})_{(h)}\). These identifications are compatible with the inclusions
\(D_+(gh)\subseteq D_+(h)\). By Section 4.4, \((\operatorname{Proj}B)_{\mathbb Z}\) is covered by the spectra of the
rings \((B_{(h)})_{\mathbb Z}\), glued in the same way as the charts \(\operatorname{Spec}(B_{\mathbb Z})_{(h)}\) of
\(\operatorname{Proj}B_{\mathbb Z}\). Here the elements \(h\in A_+\) suffice to cover
\(\operatorname{Proj}B_{\mathbb Z}\), because they span the ideal of elements of positive degree. \(\square\)

**Example 5.5 (projective space).** For a blueprint \(B\) put
\(\mathbb P^n_B=\operatorname{Proj}B[T_0,\dots,T_n]\). The blueprint \(B[T_0,\dots,T_n]_{(T_i)}\) is the free
blueprint over \(B\) in the \(n\) elements \(T_j/T_i\), \(j\neq i\). So \(\mathbb P^n_B\) is covered by \(n+1\)
copies of \(\mathbb A^n_B=\operatorname{Spec}B[T_1,\dots,T_n]\).

For \(B=\mathbb F_1\) the points of \(\mathbb P^n_{\mathbb F_1}\) are the prime ideals \(\mathfrak p_I\) of
\(\mathbb F_1[T_0,\dots,T_n]\) with \(I\neq\{0,\dots,n\}\). There are \(2^{n+1}-1\) points, and the \(n+1\) points
with \(I\) of size \(n\) are the closed points. This is the projective space of the lesson *Monoid schemes*. By
Proposition 5.4(b), \((\mathbb P^n_{\mathbb F_1})_{\mathbb Z}=\operatorname{Proj}\mathbb Z[T_0,\dots,T_n]\) is
projective space over \(\mathbb Z\). If \(B=k\) is a ring, then \(\mathbb P^n_k\) is not the projective space of
algebraic geometry, because \(k[T_0,\dots,T_n]\) contains only monomials; but \((\mathbb P^n_k)^+\) is.

**Example 5.6 (models of projective schemes; a line with three marked points).** Let \(\mathfrak a\) be a
homogeneous ideal of \(\mathbb Z[T_0,\dots,T_n]\), let \(R=\mathbb Z[T_0,\dots,T_n]/\mathfrak a\), and let
\(B=\mathbb F_1\langle t_0,\dots,t_n\rangle\subseteq R\) be the graded blueprint generated by the classes \(t_i\) of
the \(T_i\). Then \(\operatorname{Proj}B\) is an *\(\mathbb F_1\)-model* of the projective scheme
\(\operatorname{Proj}R\): by Proposition 5.4(b), \((\operatorname{Proj}B)_{\mathbb Z}=\operatorname{Proj}R\). By
Corollary 3.4 the points of \(\operatorname{Proj}B\) are the zero patterns \(I\neq\{0,\dots,n\}\) of the points of
\(\operatorname{Proj}R\) with homogeneous coordinates in a field. *Reference:*
[López Peña–Lorscheid 2012, Section 4].

Take the line \(x_0+x_1=x_2\) in the projective plane: \(R=\mathbb Z[x_0,x_1,x_2]/(x_0+x_1-x_2)\) and
\[
L=\operatorname{Proj}\mathbb F_1\langle x_0,x_1,x_2\rangle .
\]
A point of this line cannot have two zero coordinates. The points \([1:1:2]\) over \(\mathbb Q\) and
\([0:1:1]\), \([1:0:1]\), \([1:-1:0]\) show that the zero patterns are \(\emptyset\), \(\{0\}\), \(\{1\}\),
\(\{2\}\). So \(L\) has four points: a generic point and three closed points. Its base extension is
\(L_{\mathbb Z}=\operatorname{Proj}R\cong\mathbb P^1_{\mathbb Z}\). The monoid scheme \(\mathbb P^1_{\mathbb F_1}\)
has three points. So \(L\) and \(\mathbb P^1_{\mathbb F_1}\) are two \(\mathbb F_1\)-models of the projective line
that are not isomorphic. In the coordinate \(u=x_0/x_2\) the closed points of \(L\) are \(u=0\), \(u=1\) and
\(u=\infty\): the blue scheme \(L\) is the projective line together with the three points \(0,1,\infty\).
Exercise 4 continues this example.

**Remark 5.7 (the Grassmannian \(\operatorname{Gr}(2,4)\)).** [López Peña–Lorscheid 2012, Section 5] studies
\(\operatorname{Proj}\) of the blueprint generated by six elements \(x_{ij}\), \(1\le i<j\le4\), with the Plücker
relation \(x_{12}x_{34}+x_{14}x_{23}\equiv x_{13}x_{24}\), and finds \(36\) points. The proof of Proposition
1.12(a) and (c) applies with \(x_{13}x_{24}\) in the role of \(ad\): in the ring
\(\mathbb Z[x_{ij}]/(x_{12}x_{34}+x_{14}x_{23}-x_{13}x_{24})\) the monomials that are not divisible by
\(x_{13}x_{24}\) form a basis, and the relation rewrites every monomial as a sum of such monomials. So this
blueprint is the blueprint generated by the \(x_{ij}\) in that ring. Hence Corollary 3.4 applies, and it confirms
the count. A point of the cone \(x_{12}x_{34}+x_{14}x_{23}=x_{13}x_{24}\) over a field has a zero pattern \(I\) that
meets none of the three pairs \(\{12,34\}\), \(\{14,23\}\), \(\{13,24\}\), or exactly one of them, or all three; and
all such \(I\) occur. This gives \(1+9+27=37\) sets \(I\). Removing the set of all six indices leaves \(36\) points;
the six sets \(I\) with five elements are the closed points.

## 6. The Tits category

### 6.1 The problem for \(\mathrm{SL}_2\)

Tits, in no. 13 of his 1957 paper, whose beginning is reproduced in [Lorscheid–Thas 2023], considers geometries over a
"field of characteristic one". There the projective space of
dimension \(n\) over this field is a set of \(n+1\) points, all of whose subsets count as linear subspaces, and its
projectivities are the permutations of the points. In later work this became a requirement on a geometry over
\(\mathbb F_1\): a Chevalley group \(\mathcal G\) should have a model over \(\mathbb F_1\) whose group of
\(\mathbb F_1\)-points is the Weyl group \(W\) of \(\mathcal G\) [Lorscheid 2016, Prologue]; see *Counting over
finite fields and the limit q → 1*. We call this *Tits's problem*.

Take \(\mathcal G=\mathrm{SL}_{2,\mathbb Z}\), with coordinate ring \(R_1=\mathbb Z[a,b,c,d]/(ad-bc-1)\).
Let \(T\) be the diagonal torus, \(w_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and \(N=T\sqcup w_0T\) the scheme of
monomial matrices in \(\mathrm{SL}_2\); we shall see that \(N\) is the normalizer of \(T\). The Weyl group is
\(W=N/T\), of order \(2\).

A first obstruction is this. If \(W\) is the group of \(\mathbb F_1\)-points of a model of
\(\mathrm{SL}_2\), one expects base extension to \(\mathbb Z\) to give a homomorphism \(W\to N(\mathbb Z)\) that is
a section of \(N(\mathbb Z)\to W\); the lesson *Torified varieties and the limits of monoid schemes* states the
conditions under which this follows. But \(N(\mathbb Z)=\{\pm1,\pm w_0\}\) is cyclic of order \(4\), generated by
\(w_0\), and the class of \(w_0\) contains no element of order \(2\). So there is no such section
[Lorscheid 2016, Prologue].

Blueprints give a natural model: \(G=\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\), with
\(G_{\mathbb Z}=\mathrm{SL}_{2,\mathbb Z}\) by Proposition 1.12. Its two closed points are the patterns of \(T\) and
of \(w_0T\) (Example 3.5(c)). But the ordinary points and the ordinary morphisms of blue schemes do not see the
Weyl group or the group law.

**Proposition 6.1.** Let \(B_1=\mathbb F_1[\mathrm{SL}_2]\) and \(B_2=B_1\otimes_{\mathbb F_1}B_1\), and let
\(m:R_1\to R_2\) be the comultiplication of \(\mathrm{SL}_2\):
\[
m(a)=a_1a_2+b_1c_2,\quad m(b)=a_1b_2+b_1d_2,\quad m(c)=c_1a_2+d_1c_2,\quad m(d)=c_1b_2+d_1d_2 .
\]

(a) There are exactly three morphisms of blueprints \(B_1\to\mathbb F_1\). They are given by the matrices
\(\begin{pmatrix}1&0\\0&1\end{pmatrix}\), \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\) and
\(\begin{pmatrix}1&0\\1&1\end{pmatrix}\).

(b) No morphism of blueprints \(B_1\to B_2\) induces \(m\) on the rings. Hence the group law of
\(\mathrm{SL}_{2,\mathbb Z}\) is not the base extension of a morphism of blue schemes \(G\times G\to G\).

*Proof.* (a) By Proposition 1.12(c) a morphism is given by \(\alpha,\beta,\gamma,\delta\in\{0,1\}\) with
\(\alpha\delta\equiv\beta\gamma+1\) in \(\mathbb F_1\), that is, \(\alpha\delta=\beta\gamma+1\) in \(\mathbb N\). So
\(\alpha=\delta=1\) and \(\beta\gamma=0\).

(b) Such a morphism would send \(a\) to \(0\) or to a monomial \(M\) in the eight variables, with
\(M=a_1a_2+b_1c_2\) in \(R_2\). The right side is a sum of two different reduced monomials. By (1.3), \(M\) is a sum
of \((m_1+1)(m_2+1)\) different reduced monomials with positive coefficients. If there are exactly two, then
\((m_1,m_2)\) is \((1,0)\) or \((0,1)\), and the two monomials have the quotient \(b_1c_1\) or \(b_2c_2\). The
monomials \(a_1a_2\) and \(b_1c_2\) do not. For the last statement, \(G\times G=\operatorname{Spec}B_2\) by Theorem
4.8(d), and \(B_2\) is global by Example 4.6(b). So by Theorem 4.8(b) a morphism \(G\times G\to G\) is of the form
\(f^{\ast}\) for a morphism \(f:B_1\to B_2\), and its base extension to \(\mathbb Z\) is given by
\(f_{\mathbb Z}\). \(\square\)

So \(G\) has three \(\mathbb F_1\)-points in the ordinary sense, which do not form a group, and no group law in
the ordinary sense. [Lorscheid 2018a] solves both problems with a second kind of morphism. The group law becomes a
*Tits morphism*, and the Weyl group is recovered by a functor \(\mathcal W\) from a *rank space*, not as a set of
morphisms from \(\operatorname{Spec}\mathbb F_1\).

### 6.2 The rank space

A reference for Sections 6.2 to 6.4 is [Lorscheid 2018a, Sections 2 and 3]. That paper works with all blue
schemes. We give the definitions for affine blue schemes. This is the generality in which Section 7 uses them, and
the models in Theorem 6.15(b), (c) and (d) are affine.

In this subsection \(X=\operatorname{Spec}B\) is an affine blue scheme and \(x=\mathfrak p\) is a point of \(X\). We
put
\[
D_x=B/\mathfrak p .
\]
By Proposition 3.2(c), \(\operatorname{Spec}D_x\) is homeomorphic to the closure of \(x\) in \(X\). By (1.2) and
Proposition 2.3(b), \((D_x)_{\mathbb Z}=B_{\mathbb Z}/\mathfrak pB_{\mathbb Z}\), where
\(\mathfrak pB_{\mathbb Z}\) is the ideal generated by the image of \(\mathfrak p\). So
\(\operatorname{Spec}(D_x)_{\mathbb Z}\) is a closed subscheme of \(X_{\mathbb Z}\).

**Definition 6.2.** A prime number \(\ell\) is a *potential characteristic* of \(x\) if there are a field \(k\) of
characteristic \(\ell\) and a morphism of blueprints \(f:B\to k\) with \(f^{-1}(0)=\mathfrak p\). The point \(x\) is
*almost of indefinite characteristic* if all but finitely many prime numbers are potential characteristics of \(x\).

**Definition 6.3.** The point \(x\) is *pseudo-Hopf* if the following three conditions hold.

(PH1) \(x\) is almost of indefinite characteristic.

(PH2) The additive group of the ring \((D_x)_{\mathbb Z}\) is generated by the units of the blueprint
\((D_x)_{\mathrm{inv}}\) of Lemma 1.15.

(PH3) The additive group of \((D_x)_{\mathbb Z}\) is torsion-free.

The *rank* \(\operatorname{rk}x\) of \(x\) is the Krull dimension of the ring \((D_x)_{\mathbb Z}\otimes\mathbb Q\).

In (PH2), the negative of a unit of \((D_x)_{\mathrm{inv}}\) is a unit. So (PH2) says that every element of
\((D_x)_{\mathbb Z}\), and in particular of \((D_x)_{\mathrm{inv}}\), is a sum of units of
\((D_x)_{\mathrm{inv}}\). Over \(\mathbb Z\), a module is torsion-free if and only if it is flat
[Stacks, Tag [0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dedekind-torsion-free-flat)].

*Reference:* [Lorscheid 2018a, Definitions 1.20, 1.24, 2.1 and 2.3]. There \(X\) is any blue scheme. The closure of
\(x\) carries the structure of a reduced closed subscheme \(\bar x\) [Lorscheid 2018a, Section 1.4], and a
pseudo-Hopf point is a point that is almost of indefinite characteristic and such that \(\bar x\) is affine,
\(\bar x_{\mathrm{inv}}\) is generated by its units and \(\bar x_{\mathbb Z}\) is a flat scheme. For
\(X=\operatorname{Spec}B\) the subscheme \(\bar x\) is \(\operatorname{Spec}D_x\). The conditions of
[Lorscheid 2018a] are stated for the blueprint of global sections of \(\bar x\). This is \(D_x\) when \(D_x\) is
global, which holds in every case in which we verify the conditions, by Proposition 4.7. Potential
characteristics are defined there through morphisms from the residue field \(\kappa(x)\) to semifields, and \(0\)
and \(1\) are also allowed as characteristics; only prime characteristics matter for Definition 6.3.

**Definition 6.4.** Let \(X\) be connected. If \(X\) has a pseudo-Hopf point, the *rank* \(\operatorname{rk}X\) is
the smallest rank of a pseudo-Hopf point, and \(\mathcal Z(X)\) is the set of pseudo-Hopf points of rank
\(\operatorname{rk}X\). If \(X\) has no pseudo-Hopf point, \(\operatorname{rk}X=0\) and
\(\mathcal Z(X)=\emptyset\). If \(X\) is a disjoint union of connected open affine subschemes, \(\mathcal Z(X)\) is
the union of their sets \(\mathcal Z\).

**Definition 6.5.** Let \(D\) be a blueprint. Its *inverse closure* \(\widehat D\) is the subblueprint of
\(D_{\mathrm{inv}}\) on the set of those elements of \(D_{\mathrm{inv}}\) that are sums of elements of the image of
\(D\). For \(x\in\mathcal Z(X)\) let
\[
K_x=(\widehat{D_x})^\star
\]
be the unit field of the inverse closure of \(D_x\). The *rank space* of \(X\) is the blue scheme
\[
X^{\mathrm{rk}}=\coprod_{x\in\mathcal Z(X)}\operatorname{Spec}K_x ,
\]
a disjoint union of one-point spaces. The *Weyl extension* \(\mathcal W(X)\) of \(X\) is the underlying set of
\(X^{\mathrm{rk}}\). It is in bijection with \(\mathcal Z(X)\).

**Lemma 6.6.** Let \(x=\mathfrak p\) be a pseudo-Hopf point of \(X=\operatorname{Spec}B\). Then \(K_x\) is a
subblueprint of \((D_x)_{\mathrm{inv}}\), and its ring is
\((K_x)_{\mathbb Z}=(D_x)_{\mathbb Z}=B_{\mathbb Z}/\mathfrak pB_{\mathbb Z}\).

*Proof.* Write \(D=D_x\), let \(\bar A\) be the image of the monoid of \(D\) in \(D_{\mathbb Z}\), and let
\(\widehat A\) be the underlying monoid of \(\widehat D\). So
\(\bar A\subseteq\widehat A\subseteq\bar A\cup(-\bar A)\). Let \(u\) be a unit of \(D_{\mathrm{inv}}\). Then
\(u=\pm\bar a\) and \(u^{-1}=\pm\bar a'\) with \(\bar a,\bar a'\in\bar A\), so \(\bar a\bar a'=\pm1\). If
\(\bar a\bar a'=1\), then \(\bar a\) is a unit of \(\widehat A\). If \(\bar a\bar a'=-1\), then \(-1\in\bar A\) and
\(-\bar a'=(\bar a\bar a')\bar a'\in\bar A\), and \(\bar a\cdot(-\bar a')=1\); again \(\bar a\) is a unit of
\(\widehat A\). So every unit of \(D_{\mathrm{inv}}\) is, up to sign, a unit of \(\widehat D\). By (PH2) the units
of \(\widehat D\) generate the group \(D_{\mathbb Z}\). The ring of \(K_x\) is the subgroup of \(D_{\mathbb Z}\)
generated by these units. \(\square\)

So \((X^{\mathrm{rk}})_{\mathbb Z}\), which we write \(X^{\mathrm{rk}}_{\mathbb Z}\), is the disjoint union of the
closed subschemes \(\operatorname{Spec}B_{\mathbb Z}/\mathfrak pB_{\mathbb Z}\) of \(X_{\mathbb Z}\), for
\(\mathfrak p\in\mathcal Z(X)\). The inclusions of these subschemes define a morphism of schemes
\[
\rho_{X,\mathbb Z}:X^{\mathrm{rk}}_{\mathbb Z}\longrightarrow X_{\mathbb Z}.
\]
In [Lorscheid 2018a, Section 2.1] this morphism is obtained from morphisms of blue schemes
\(X^{\mathrm{rk}}\leftarrow X^{\sim}\to X\), where \(X^{\sim}=\coprod\operatorname{Spec}\widehat{D_x}\) is the
*pre-rank space*.

**Examples 6.7.**

(a) *Tori.* Let \(D\) be \(\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]\) or
\(\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\), and \(X=\operatorname{Spec}D\). It has one point \(x=\{0\}\), and
\(D_x=D\). For every field \(k\) the morphism \(D\to k\) with \(T_i\mapsto1\) has \(f^{-1}(0)=\{0\}\); so (PH1)
holds. The blueprint \(D_{\mathrm{inv}}\) is \(\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\) by Lemma 1.15; all
its non-zero elements are units, and they generate the group
\(D_{\mathbb Z}=\mathbb Z[T_1^{\pm1},\dots,T_r^{\pm1}]\), which is free. So \(x\) is pseudo-Hopf. Its rank is the
dimension of \(\mathbb Q[T_1^{\pm1},\dots,T_r^{\pm1}]\), which is \(r\): it is at most the dimension \(r\) of
\(\mathbb Q[T_1,\dots,T_r]\) [Stacks, Tag [00OP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dim-affine-space)], and the ideals \((T_1-1,\dots,T_j-1)\), \(0\le j\le r\), form a
chain of prime ideals of length \(r\). The inverse closure of \(D\) is \(D\). For
\(D=\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\) this holds because \(D_{\mathrm{inv}}=D\). For
\(D=\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]\) it holds because an element \(-T^e\) is not a sum of Laurent
monomials in \(\mathbb Z[T_1^{\pm1},\dots,T_r^{\pm1}]\). And \(D^\star=D\). So \(K_x=D\) and
\[
X^{\mathrm{rk}}=X,\qquad\operatorname{rk}X=r,\qquad\mathcal W(X)=\{x\}.
\]
In particular \(\operatorname{Spec}\mathbb F_1\) and \(\operatorname{Spec}\mathbb F_{1^2}\) are their own rank
spaces, of rank \(0\).

(b) *The affine line.* \(\mathbb A^1_{\mathbb F_1}=\operatorname{Spec}\mathbb F_1[T]\) has the points
\(\eta=\{0\}\) and \(x=(T)\). We have \(D_x=\mathbb F_1\), so \(x\) is pseudo-Hopf of rank \(0\) by (a). For
\(\eta\) we have \(D_\eta=\mathbb F_1[T]\), of rank \(1\). The units of \((D_\eta)_{\mathrm{inv}}\) are \(\pm1\),
and they do not generate \(\mathbb Z[T]\). So \(\eta\) is not pseudo-Hopf. Hence \(\mathcal Z=\{x\}\), the rank is
\(0\), the rank space is \(\operatorname{Spec}\mathbb F_1\), and \(\rho_{\mathbb Z}\) is the inclusion of the origin
into the affine line over \(\mathbb Z\).

(c) *Semiring schemes.* Let \(B\) be a semiring. If \(f:B\to k\) and \(f':B\to k'\) are homomorphisms to fields of
different characteristics \(\ell,\ell'>0\) with the same kernel \(\mathfrak p\), then
\(\ell\cdot1\in\mathfrak p\), so \(\ell=0\) in \(k'\), which is false. So a point of \(\operatorname{Spec}B\) has at
most one prime potential characteristic. It is not pseudo-Hopf, and the rank space of
\(\operatorname{Spec}B\) is empty. *Reference:* [Lorscheid 2018a, Example 2.8].

**Lemma 6.8.** Let \(X=\operatorname{Spec}B\) be connected and let \(r_0\) be the smallest rank of a point of
\(X\). If every point of rank \(r_0\) is pseudo-Hopf, then \(\operatorname{rk}X=r_0\) and \(\mathcal Z(X)\) is the
set of points of rank \(r_0\).

*Proof.* This follows from Definition 6.4. \(\square\)

This is the situation of [Lorscheid 2016, Section 2.1]. There the rank space is defined under a hypothesis (H):
\(X\) is connected and cancellative, and for every point \(x\) of smallest rank \(r\) the closure of \(x\), as a
closed subscheme, is isomorphic to the spectrum of \(\mathbb F_1[T_1^{\pm1},\dots,T_r^{\pm1}]\) or of
\(\mathbb F_{1^2}[T_1^{\pm1},\dots,T_r^{\pm1}]\).

### 6.3 Tits morphisms

**Definition 6.9.** Let \(X\) and \(Y\) be affine blue schemes. A *Tits morphism* \(\varphi:X\to Y\) is a pair
\(\varphi=(\varphi^{\mathrm{rk}},\varphi^+)\) of a morphism of blue schemes
\(\varphi^{\mathrm{rk}}:X^{\mathrm{rk}}\to Y^{\mathrm{rk}}\) and a morphism of semiring schemes
\(\varphi^+:X^+\to Y^+\) such that the square of schemes
\[
\begin{array}{ccc}
X^{\mathrm{rk}}_{\mathbb Z}&\xrightarrow{\ (\varphi^{\mathrm{rk}})_{\mathbb Z}\ }&Y^{\mathrm{rk}}_{\mathbb Z}\\
{\scriptstyle\rho_{X,\mathbb Z}}\downarrow\quad&&\quad\downarrow{\scriptstyle\rho_{Y,\mathbb Z}}\\
X_{\mathbb Z}&\xrightarrow{\ (\varphi^+)_{\mathbb Z}\ }&Y_{\mathbb Z}
\end{array}
\]
commutes. Tits morphisms are composed componentwise. The *Tits category* \(\operatorname{Sch}_{\mathcal T}\) has
the affine blue schemes as objects and the Tits morphisms as morphisms.

*Reference:* [Lorscheid 2018a, Definition 2.10], where the objects are all blue schemes.

The Tits category has three functors that matter here: the *Weyl extension*
\(\mathcal W:\operatorname{Sch}_{\mathcal T}\to\text{Sets}\), which sends \(\varphi\) to the map of underlying sets of
\(\varphi^{\mathrm{rk}}\); the base extension \(X\mapsto X^+\), \(\varphi\mapsto\varphi^+\) to semiring schemes;
and the base extension \(X\mapsto X_{\mathbb Z}\), \(\varphi\mapsto(\varphi^+)_{\mathbb Z}\) to schemes. If \(X\) is
the spectrum of a semiring, then \(X^{\mathrm{rk}}=\emptyset\) by Example 6.7(c) and \(X^+=X\), and a Tits morphism
\(X\to Y\) is just a morphism \(X\to Y^+\).

**Example 6.10 (the two kinds of morphisms are different).** Let
\(\mathbb G_m=\operatorname{Spec}\mathbb F_1[T^{\pm1}]\). The inclusion
\(\mathbb F_1[T]\subseteq\mathbb F_1[T^{\pm1}]\) gives a morphism of blue schemes
\(j:\mathbb G_m\to\mathbb A^1_{\mathbb F_1}\). There is no Tits morphism \(\varphi\) with \(\varphi^+=j^+\). Indeed,
by Examples 6.7 the rank space of \(\mathbb G_m\) is \(\mathbb G_m\), and the rank space of the affine line is the
origin. So \(\rho_{\mathbb Z}\circ(\varphi^{\mathrm{rk}})_{\mathbb Z}\) is the constant morphism from
\(\mathbb G_{m,\mathbb Z}\) to the origin of the affine line, and this is not \((j^+)_{\mathbb Z}\). In the other
direction, the multiplication of \(\mathrm{SL}_2\) is a Tits morphism (Theorem 7.2) and not a morphism of blue
schemes (Proposition 6.1). *Reference:* [Lorscheid 2018a, Section 2.2].

**Lemma 6.11 (products in the Tits category).** Let \(X_1,X_2\) be affine blue schemes and \(X=X_1\times X_2\)
their product as blue schemes, with projections \(q_1,q_2\). Assume:

(i) there are morphisms \(q_i^{\mathrm{rk}}:X^{\mathrm{rk}}\to X_i^{\mathrm{rk}}\) such that
\(p_i=(q_i^{\mathrm{rk}},q_i^+)\) is a Tits morphism \(X\to X_i\), for \(i=1,2\);

(ii) the morphism \((q_1^{\mathrm{rk}},q_2^{\mathrm{rk}}):X^{\mathrm{rk}}\to X_1^{\mathrm{rk}}\times
X_2^{\mathrm{rk}}\) is an isomorphism of blue schemes.

Then \(X\), with \(p_1\) and \(p_2\), is a product of \(X_1\) and \(X_2\) in \(\operatorname{Sch}_{\mathcal T}\).

*Proof.* Let \(\varphi_i=(\varphi_i^{\mathrm{rk}},\varphi_i^+):Y\to X_i\) be Tits morphisms. By Section 4.4,
\(X^+=X_1^+\times X_2^+\) and \(X_{\mathbb Z}=X_{1,\mathbb Z}\times X_{2,\mathbb Z}\). So there is exactly one
morphism \(\varphi^+:Y^+\to X^+\) with \(q_i^+\varphi^+=\varphi_i^+\), and by (ii) exactly one morphism
\(\varphi^{\mathrm{rk}}:Y^{\mathrm{rk}}\to X^{\mathrm{rk}}\) with
\(q_i^{\mathrm{rk}}\varphi^{\mathrm{rk}}=\varphi_i^{\mathrm{rk}}\). The pair
\((\varphi^{\mathrm{rk}},\varphi^+)\) is a Tits morphism: the two morphisms
\(\rho_{X,\mathbb Z}(\varphi^{\mathrm{rk}})_{\mathbb Z}\) and \((\varphi^+)_{\mathbb Z}\rho_{Y,\mathbb Z}\) from
\(Y^{\mathrm{rk}}_{\mathbb Z}\) to \(X_{\mathbb Z}\) have the same composites with the two projections, because
\[
(q_i^+)_{\mathbb Z}\,\rho_{X,\mathbb Z}\,(\varphi^{\mathrm{rk}})_{\mathbb Z}
=\rho_{X_i,\mathbb Z}\,(q_i^{\mathrm{rk}})_{\mathbb Z}\,(\varphi^{\mathrm{rk}})_{\mathbb Z}
=\rho_{X_i,\mathbb Z}\,(\varphi_i^{\mathrm{rk}})_{\mathbb Z}
=(\varphi_i^+)_{\mathbb Z}\,\rho_{Y,\mathbb Z}
=(q_i^+)_{\mathbb Z}\,(\varphi^+)_{\mathbb Z}\,\rho_{Y,\mathbb Z}.
\]
Here the first equality holds because \(p_i\) is a Tits morphism and the third because \(\varphi_i\) is one.
\(\square\)

**Lemma 6.12.** \(\operatorname{Spec}\mathbb F_1\) is a final object of \(\operatorname{Sch}_{\mathcal T}\).

*Proof.* By Example 6.7(a) its rank space is \(\operatorname{Spec}\mathbb F_1\), and its semiring scheme is
\(\operatorname{Spec}\mathbb N\). For an affine blue scheme \(X\) there is exactly one morphism
\(X^{\mathrm{rk}}\to\operatorname{Spec}\mathbb F_1\) and exactly one morphism \(X^+\to\operatorname{Spec}\mathbb N\),
by Theorem 4.8(b), since \(\mathbb F_1\) is initial among blueprints and \(\mathbb N\) among semirings. The square
of Definition 6.9 commutes because \(\operatorname{Spec}\mathbb Z\) is a final object in the category of schemes.
\(\square\)

### 6.4 Tits monoids and Tits–Weyl models

**Definition 6.13.** A *Tits monoid* is a monoid in the category \(\operatorname{Sch}_{\mathcal T}\): an affine
blue scheme \(G\) with Tits morphisms \(\mu:G\times G\to G\) and \(\epsilon:\operatorname{Spec}\mathbb F_1\to G\), where
\(G\times G\) is a product of \(G\) with itself in \(\operatorname{Sch}_{\mathcal T}\), such that \(\mu\) is
associative and \(\epsilon\) is a unit on both sides. Its *Weyl monoid* is the set \(\mathcal W(G)\) with the
product \(\mathcal W(\mu)\). For a blueprint \(C\) the set \(G^{\mathcal T}(C)\) of Tits morphisms
\(\operatorname{Spec}C\to G\) is a monoid, with the product \((\varphi,\psi)\mapsto\mu\circ(\varphi,\psi)\); its
elements are the *\(C\)-rational Tits points* of \(G\).

*Reference:* [Lorscheid 2018a, Definition 3.9]. [Lorscheid 2018a, Theorems 3.5 and 3.8] state that for all blue
schemes the product \(X_1\times X_2\) is a product in \(\operatorname{Sch}_{\mathcal T}\), and that the functors
\(\mathcal W\), \((-)^+\) and \((-)_{\mathbb Z}\) preserve finite products. The proofs there rest on
[Lorscheid 2018a, Proposition 3.3], the formula
\((X_1\times X_2)^{\mathrm{rk}}=X_1^{\mathrm{rk}}\times X_2^{\mathrm{rk}}\), and on [Lorscheid 2018a, Lemma 1.41],
the formula \(\widehat{B_1\otimes_{\mathbb F_1}B_2}=\widehat{B_1}\otimes_{\mathbb F_1}\widehat{B_2}\). The left
sides are always cancellative, so both formulas need the hypothesis that the right side is cancellative, and this
hypothesis can fail (Exercises 3 and 6). So this lesson verifies the hypotheses of Lemma 6.11 directly where it
needs them (Proposition 7.1 and Exercise 5).

*Group schemes.* Let \(\mathcal G\) be a group scheme over \(\mathbb Z\) and \(T\) a subgroup scheme. For a ring
\(k\), let \(\mathcal G(k)\) be the group of \(k\)-points. The *centralizer* \(C(T)\) and the *normalizer* \(N(T)\)
of \(T\) are the functors
\[
C(T)(k)=\{g\in\mathcal G(k):gtg^{-1}=t\ \text{for all}\ k\text{-algebras}\ k'\ \text{and all}\ t\in T(k')\},
\]
\[
N(T)(k)=\{g\in\mathcal G(k):gT(k')g^{-1}=T(k')\ \text{for all}\ k\text{-algebras}\ k'\}.
\]
[Lorscheid 2018a, Section 3.3] uses the following facts and notions, with references to [SGA3 II]. If
\(\mathcal G\) is of finite type and \(T\) is a torus, then \(C(T)\) and \(N(T)\) are subgroup schemes of
\(\mathcal G\), and the quotient \(\mathcal W(T)=N(T)/C(T)\) is a group scheme, the *Weyl group of \(\mathcal G\)
relative to \(T\)*. A torus \(T\subseteq\mathcal G\) is a *maximal torus* if for every algebraically closed field
\(k\) the torus \(T_k\) is contained in no larger torus of \(\mathcal G_k\). Its dimension is the *reductive rank*
of \(\mathcal G\), and \(W=\mathcal W(T)(\mathbb C)\) is the *ordinary Weyl group* of \(\mathcal G\). If
\(\mathcal G\) is split reductive, the *extended Weyl group* is \(\widetilde W=N(T)(\mathbb Z)\)
[Lorscheid 2016, Section 2.3]. This lesson uses these notions only for \(\mathrm{SL}_2\), where Section 7 computes
all of them by hand.

**Definition 6.14.** Let \(\mathcal G\) be an affine smooth group scheme of finite type over \(\mathbb Z\). A *Tits
model* of \(\mathcal G\) is a Tits monoid \((G,\mu,\epsilon)\) together with an isomorphism of group schemes
between \(G_{\mathbb Z}\), with the product \(\mu_{\mathbb Z}\), and \(\mathcal G\). Let \(e\) be the image of
\(\epsilon^{\mathrm{rk}}\) in \(G^{\mathrm{rk}}\). The component \(\mathfrak e=\operatorname{Spec}K_e\) of
\(G^{\mathrm{rk}}\) is the *Weyl kernel* of \(G\). By [Lorscheid 2018a, Lemmas 3.11 and 3.12], \(\mu^{\mathrm{rk}}\)
restricts to a commutative group law on \(\mathfrak e\), and if \(G\) is locally of finite type, the group scheme
\(\mathfrak e_{\mathbb Z}\) is diagonalizable, that is, a closed subgroup scheme of a split torus. It contains a
largest torus \(T\), the *canonical torus* of \(\mathcal G\) with respect to \(G\).
[Lorscheid 2018a, Section 3.3] regards \(G^{\mathrm{rk}}_{\mathbb Z}\), with the product
\((\mu^{\mathrm{rk}})_{\mathbb Z}\), as a group scheme and \(\rho_{G,\mathbb Z}\) as an inclusion of
\(G^{\mathrm{rk}}_{\mathbb Z}\) into \(\mathcal G\). Then \(\mathfrak e_{\mathbb Z}\subseteq C(T)\) and
\(G^{\mathrm{rk}}_{\mathbb Z}\subseteq N(T)\), and these inclusions induce a morphism of group schemes
\[
\Psi_{\mathfrak e}:G^{\mathrm{rk}}_{\mathbb Z}/\mathfrak e_{\mathbb Z}\longrightarrow\mathcal W(T)=N(T)/C(T).
\]
The Tits model \(G\) is a *Tits–Weyl model* of \(\mathcal G\) if \(T\) is a maximal torus of \(\mathcal G\) and
\(\Psi_{\mathfrak e}\) is an isomorphism.

*Reference:* [Lorscheid 2018a, Section 3.3 and Definition 3.13]. For \(G=\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\)
every object in this definition is computed in Section 7: there \(G^{\mathrm{rk}}_{\mathbb Z}\) is the group scheme
\(N\), and \(\rho_{G,\mathbb Z}\) is its inclusion into \(\mathrm{SL}_2\).

So a Tits–Weyl model carries two structures at once. Its base extension to \(\mathbb Z\) is the group scheme
\(\mathcal G\). For \(\mathrm{SL}_2\), as computed in Section 7, and for the split reductive groups of
[Lorscheid 2018a, Theorem 3.14], its rank space is a model of the normalizer of a maximal torus, whose set of
components is the Weyl group. The definition alone does not give this: it compares quotients only. For the model
\(\operatorname{Spec}\mathbb F_1[t]\) of the additive group \(\mathbb G_a\), with the comultiplication
\(t\mapsto t_1+t_2\), the rank space is a point, while the normalizer of the trivial maximal torus is all of
\(\mathbb G_a\).

**Theorem 6.15 (Lorscheid).**

(a) Let \(\mathcal G\) be an affine smooth group scheme of finite type over \(\mathbb Z\) that has a Tits–Weyl
model \(G\). Then:

1. the Weyl monoid \(\mathcal W(G)\) is a group, canonically isomorphic to the ordinary Weyl group \(W\) of
   \(\mathcal G\);
2. the rank of \(G\), defined as the rank of the connected component of \(G\) that contains the unit, is equal to
   the reductive rank of \(\mathcal G\);
3. the monoid \(G^{\mathcal T}(\mathbb F_1)\) is a subgroup of \(\mathcal W(G)\);
4. if \(\mathcal G\) is a split reductive group scheme, then \(G^{\mathcal T}(\mathbb F_{1^2})\) is canonically
   isomorphic to the extended Weyl group \(\widetilde W\) of \(\mathcal G\).

(b) Let \(n\ge1\) and let \(\mathrm{SL}_n\) be the \(\mathbb F_1\)-model of
\(\mathrm{SL}_{n,\mathbb Z}\subseteq\mathbb A^{n^2}_{\mathbb Z}\) in the sense of Example 1.11(b). The group law of
\(\mathrm{SL}_{n,\mathbb Z}\) descends in exactly one way to a monoid law \(\mu^+\) of \(\mathrm{SL}_n^+\). The
group law of the normalizer of the diagonal torus descends in exactly one way to a group law
\(\mu^{\mathrm{rk}}\) of \(\mathrm{SL}_n^{\mathrm{rk}}\). The pair \(\mu=(\mu^{\mathrm{rk}},\mu^+)\) is a Tits
morphism that makes \(\mathrm{SL}_n\) a Tits–Weyl model of \(\mathrm{SL}_{n,\mathbb Z}\). The group
\(\mathrm{SL}_n^{\mathcal T}(\mathbb F_1)\) is isomorphic to the alternating group \(A_n\). For a semiring \(S\)
that is contained in a ring, the set \(\mathrm{SL}_n(S)\) of points with values in \(S\) is the monoid of all
\(n\times n\) matrices \((a_{i,j})\) over \(S\) with
\[
\sum_{\sigma\ \text{even}}\ \prod_{i=1}^na_{i,\sigma(i)}=\sum_{\sigma\ \text{odd}}\ \prod_{i=1}^na_{i,\sigma(i)}+1 .
\]

(c) Each of the following group schemes has a Tits–Weyl model: the special linear groups
\(\mathrm{SL}_{n,\mathbb Z}\), the general linear groups \(\mathrm{GL}_{n,\mathbb Z}\), the adjoint Chevalley groups
of type \(A_n\), the symplectic groups \(\mathrm{Sp}_{2n,\mathbb Z}\), the special orthogonal groups
\(\mathrm{SO}_{n,\mathbb Z}\) for all \(n\), and the orthogonal groups \(\mathrm O_{n,\mathbb Z}\) for even \(n\),
in the integral forms of [Lorscheid 2018a, Section 4.3].

(d) Let \(\mathcal G\) be an adjoint Chevalley group scheme, that is, a split semisimple group scheme over
\(\mathbb Z\) with trivial centre, embedded in \(\mathrm{GL}_{n,\mathbb Z}\) by its adjoint representation in a
Chevalley basis of its Lie algebra. Let \(G\) be the \(\mathbb F_1\)-model of this embedding. Then the group law of
\(\mathcal G\) descends in exactly one way to a Tits morphism \(\mu\) that makes \(G\) a Tits–Weyl model of
\(\mathcal G\), and the group \(G^{\mathcal T}(\mathbb F_1)\) is trivial.

*Reference:* [Lorscheid 2018a, Theorem 3.14] for (a), [Lorscheid 2018a, Theorem 4.2] for (b),
[Lorscheid 2018a, Theorem 4.9] for (c) and [Lorscheid 2018a, Theorem 4.12] for (d).
[Lorscheid 2018a, Theorem 4.2] states the last sentence of (b) for all semirings \(S\). For \(n\ge3\) it holds for
the semirings that are contained in a ring and not for all semirings (Example 8.2); for \(n=2\) it holds for all
semirings (Corollary 7.3(d)).

This lesson proves (b) for \(n=2\) and verifies the four conclusions of (a) in this case (Theorem 7.2 and Corollary
7.3). It proves the last sentence of (b) for all \(n\) (Example 8.2). It does not prove the other statements.
Section 8.2 says what their proofs in [Lorscheid 2018a] use; for \(n\ge3\) the existence of \(\mu^+\) in (b) is
question (e) of Section 8.3. The tool for (c) is a criterion for closed subgroups [Lorscheid 2018a, Theorem 4.7].

## 7. The Tits–Weyl model of \(\mathrm{SL}_2\)

We use the notation of Proposition 1.12: \(R_n\) is the coordinate ring of \(\mathrm{SL}_2^n\) over \(\mathbb Z\),
and \(B_n\subseteq R_n\) is the blueprint generated by the coordinates. Put
\[
G=\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]=\operatorname{Spec}B_1,\qquad G^n=\operatorname{Spec}B_n .
\]
By Proposition 1.12(d) and Theorem 4.8(d), \(G^n\) is the \(n\)-fold product of \(G\) as a blue scheme. Its base
extensions are \((G^n)^+=\operatorname{Spec}B_n^+\) and \((G^n)_{\mathbb Z}=\mathrm{SL}_2^n\). In
\(\mathrm{SL}_{2,\mathbb Z}=\operatorname{Spec}R_1\) let
\[
T=V(b,c)=\operatorname{Spec}\mathbb Z[a^{\pm1}],\qquad w_0T=V(a,d)=\operatorname{Spec}\mathbb Z[b^{\pm1}]
\]
be the closed subschemes of diagonal and of antidiagonal matrices; on \(T\) we have \(d=a^{-1}\), and on \(w_0T\)
we have \(c=-b^{-1}\). The ideals \((b,c)\) and \((a,d)\) of \(R_1\) together contain \(ad-bc=1\). So by the Chinese
remainder theorem the closed subscheme \(N\) defined by \((b,c)\cap(a,d)=(ab,ac,bd,cd)\) is the disjoint union
\(T\sqcup w_0T\).

The two closed points of \(G\) are \(e=(b,c)\) and \(w=(a,d)\). We regard \(\{e,w\}\) as a group of order \(2\)
with unit \(e\). Put
\[
K_e=\mathbb F_1[t^{\pm1}],\qquad K_w=\mathbb F_{1^2}[t^{\pm1}],
\]
and for \(x=(x_1,\dots,x_n)\in\{e,w\}^n\) let \(K_x=\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\) if all \(x_i=e\), and
\(K_x=\mathbb F_{1^2}[t_1^{\pm1},\dots,t_n^{\pm1}]\) otherwise. Let \(\mathfrak p_x\) be the closed point of \(G^n\)
whose zero pattern consists of \(b_i,c_i\) for the \(i\) with \(x_i=e\) and of \(a_i,d_i\) for the \(i\) with
\(x_i=w\).

**Proposition 7.1 (the rank space of \(G^n\)).** Let \(n\ge1\).

(a) For \(x\in\{e,w\}^n\) we have \(B_n/\mathfrak p_x\cong K_x\). The quotient map sends \(a_i\mapsto t_i\),
\(d_i\mapsto t_i^{-1}\), \(b_i,c_i\mapsto0\) if \(x_i=e\), and \(b_i\mapsto t_i\), \(c_i\mapsto-t_i^{-1}\),
\(a_i,d_i\mapsto0\) if \(x_i=w\). Moreover \(K_x\cong K_{x_1}\otimes_{\mathbb F_1}\dots\otimes_{\mathbb F_1}K_{x_n}\).

(b) \(G^n\) is connected. Every point \(\mathfrak p_x\) is pseudo-Hopf of rank \(n\), and every other point of
\(G^n\) has rank \(>n\). Hence
\[
\operatorname{rk}G^n=n,\qquad\mathcal Z(G^n)=\{\mathfrak p_x:x\in\{e,w\}^n\},\qquad
(G^n)^{\mathrm{rk}}=\coprod_{x\in\{e,w\}^n}\operatorname{Spec}K_x .
\]

(c) \((G^n)^{\mathrm{rk}}_{\mathbb Z}=N^n\), and \(\rho_{G^n,\mathbb Z}\) is the inclusion of \(N^n\) into
\(\mathrm{SL}_2^n\).

(d) Let \(n=n'+n''\). Then \(G^n\), with its two projections, is a product of \(G^{n'}\) and \(G^{n''}\) in
\(\operatorname{Sch}_{\mathcal T}\), and
\((G^n)^{\mathrm{rk}}=(G^{n'})^{\mathrm{rk}}\times(G^{n''})^{\mathrm{rk}}\).

*Proof.* (a) By Proposition 2.4(b), \(B_n/\mathfrak p_x\) is the image of the monomials in the ring
\(R_n/\mathfrak p_xR_n\). This ring is the tensor product over \(i\) of the rings
\(R_1/(b,c)=\mathbb Z[a,d]/(ad-1)\) or \(R_1/(a,d)=\mathbb Z[b,c]/(bc+1)\). So it is
\(\mathbb Z[t_1^{\pm1},\dots,t_n^{\pm1}]\), with the images of the variables as stated. The image of the set of
monomials consists of \(0\) and of all Laurent monomials in the \(t_i\), with both signs if some \(x_i=w\), because
then \(-1\) is the image of \(b_ic_i\), and with sign \(+\) only if all \(x_i=e\). This is \(K_x\). By Example
1.11(c), a morphism \(K_x\to C\) is a choice of \(n\) units of \(C\), where \(C\) must be with \(-1\) if some
\(x_i=w\). This is the same as a family of morphisms \(K_{x_i}\to C\). So \(K_x\) is the coproduct of the
\(K_{x_i}\), which is the tensor product by Proposition 1.14(a).

(b) \(G^n\) is connected by Lemma 4.5(b) and Example 4.6(b). The point \(\mathfrak p_x\) has
\(D_{\mathfrak p_x}=K_x\). The conditions (PH2) and (PH3) and the rank depend only on this blueprint, so they
hold, with rank \(n\), by Example 6.7(a). For (PH1) compose \(B_n\to K_x\) with the morphism \(K_x\to k\),
\(t_i\mapsto1\), for any field \(k\); the preimage of \(0\) is \(\mathfrak p_x\). Also \(\widehat{K_x}=K_x\) and
\(K_x^\star=K_x\) by Example 6.7(a).

Now let \(y\) be any point of \(G^n\), with zero pattern \((I_1,\dots,I_n)\), where each \(I_i\) is one of the
seven sets of Example 3.5(c). Put \(k(y)=\sum_i(2-|I_i|)\). Then \(k(y)=0\) exactly for the points
\(\mathfrak p_x\). We show \(\operatorname{rk}y\ge n+k(y)\) by induction on \(k(y)\). The ring
\((D_y)_{\mathbb Z}=R_n/\mathfrak p_yR_n\) is the tensor product over \(i\) of the rings \(R_1/(I_i)\). For
\(|I_i|=1\) these are \(R_1/(a)=\mathbb Z[b^{\pm1},d]\), \(R_1/(d)=\mathbb Z[b^{\pm1},a]\),
\(R_1/(b)=\mathbb Z[a^{\pm1},c]\), \(R_1/(c)=\mathbb Z[a^{\pm1},b]\). Each factor is a free
\(\mathbb Z\)-module and embeds into a ring of Laurent polynomials over \(\mathbb Z\) (for \(R_1\) see Example
4.6(b)). A tensor product of injective maps between free \(\mathbb Z\)-modules is injective. So
\((D_y)_{\mathbb Z}\) embeds into a ring of Laurent polynomials over \(\mathbb Z\), and
\((D_y)_{\mathbb Z}\otimes\mathbb Q\) is a domain. Let \(k(y)>0\). Choose \(i\) with \(|I_i|<2\) and enlarge
\(I_i\) by one variable \(v\) to another of the seven sets. This gives a point \(y'\) with \(k(y')=k(y)-1\),
\(v\notin\mathfrak p_y\), and
\((D_{y'})_{\mathbb Z}\otimes\mathbb Q=((D_y)_{\mathbb Z}\otimes\mathbb Q)/(v)\). The image of \(v\) in
\((D_y)_{\mathbb Z}\otimes\mathbb Q\) is not zero, and the quotient by \(v\) is a domain. So \((v)\) is a non-zero
prime ideal. A chain of prime ideals of the quotient gives a chain of prime ideals containing \(v\), and \((0)\)
can be added to it. Hence \(\operatorname{rk}y\ge\operatorname{rk}y'+1\ge n+k(y)\).

So the points of smallest rank are the \(\mathfrak p_x\), and they are pseudo-Hopf. The formulas follow from Lemma
6.8 and Definition 6.5.

(c) By Lemma 6.6, \((G^n)^{\mathrm{rk}}_{\mathbb Z}\) is the disjoint union of the closed subschemes
\(V(\mathfrak p_xR_n)\) of \(\mathrm{SL}_2^n\). The subscheme \(V(\mathfrak p_xR_n)\) is the product over \(i\) of
the subschemes \(T\) (if \(x_i=e\)) or \(w_0T\) (if \(x_i=w\)). Their disjoint union over all \(x\) is \(N^n\).

(d) Write \(x=(x',x'')\) for \(x\in\{e,w\}^n\). The first projection \(q':G^n\to G^{n'}\) is given by the inclusion
\(B_{n'}\subseteq B_n\). Let \(q'^{\,\mathrm{rk}}\) map the component \(\operatorname{Spec}K_x\) to the component
\(\operatorname{Spec}K_{x'}\) by the inclusion \(K_{x'}\subseteq K_x\), \(t_i\mapsto t_i\). The square of Definition
6.9 commutes, because the two ring homomorphisms \(R_{n'}\to R_n\to R_n/\mathfrak p_xR_n\) and
\(R_{n'}\to R_{n'}/\mathfrak p_{x'}R_{n'}\to R_n/\mathfrak p_xR_n\) are equal. So \(q'\) and, in the same way,
\(q''\) satisfy hypothesis (i) of Lemma 6.11.

A morphism from a blue scheme \(Z\) to a disjoint union of blue schemes is a decomposition of \(Z\) into disjoint
open subsets together with a morphism from each of them to one of the pieces. So the product of two disjoint unions
is the disjoint union of the products of the pieces. Hence
\((G^{n'})^{\mathrm{rk}}\times(G^{n''})^{\mathrm{rk}}\) is the disjoint union of the blue schemes
\(\operatorname{Spec}(K_{x'}\otimes_{\mathbb F_1}K_{x''})\), by Theorem 4.8(d). By (a), the inclusions of
\(K_{x'}\) and \(K_{x''}\) into \(K_x\) induce an isomorphism \(K_{x'}\otimes_{\mathbb F_1}K_{x''}\to K_x\). So the
morphism \((q'^{\,\mathrm{rk}},q''^{\,\mathrm{rk}})\) is an isomorphism on every component. This is hypothesis
(ii). \(\square\)

*Reference:* [Lorscheid 2018a, Proposition 4.1] determines the rank space of the model of \(\mathrm{SL}_m\) for
every \(m\); this is the case \(n=1\) above when \(m=2\).

**Theorem 7.2 (the Tits–Weyl model of \(\mathrm{SL}_2\)).** Let \(m:R_1\to R_2\) be the comultiplication of
Proposition 6.1.

(a) \(m\) maps \(B_1^+\) into \(B_2^+\). Let \(m^+:B_1^+\to B_2^+\) be the restriction of \(m\); it is the only
homomorphism of semirings \(B_1^+\to B_2^+\) that induces \(m\) on the rings. Let
\(\mu^+:G^+\times G^+\to G^+\) be the morphism given by \(m^+\), and let
\(\epsilon^+:\operatorname{Spec}\mathbb N\to G^+\) be given by \(a,d\mapsto1\), \(b,c\mapsto0\). Then
\((G^+,\mu^+,\epsilon^+)\) is a monoid in the category of semiring schemes, and its base extension to \(\mathbb Z\)
is the group scheme \(\mathrm{SL}_{2,\mathbb Z}\). The antipode of \(R_1\) does not map \(B_1^+\) into itself.

(b) For \(x,y\in\{e,w\}\) there is exactly one morphism of blueprints \(m_{x,y}:K_{xy}\to K_{(x,y)}\) that induces
on the rings the product \(N\times N\to N\) on the component of \((x,y)\). It is given by
\[
m_{e,e}(t)=t_1t_2,\qquad m_{e,w}(t)=t_1t_2,\qquad m_{w,e}(t)=t_1t_2^{-1},\qquad m_{w,w}(t)=-t_1t_2^{-1}.
\]
These morphisms define a morphism \(\mu^{\mathrm{rk}}:G^{\mathrm{rk}}\times G^{\mathrm{rk}}\to G^{\mathrm{rk}}\).
Together with the unit \(\epsilon^{\mathrm{rk}}:\operatorname{Spec}\mathbb F_1\to G^{\mathrm{rk}}\) given by
\(K_e\to\mathbb F_1\), \(t\mapsto1\), it makes \(G^{\mathrm{rk}}\) a group in the category of blue schemes, and the
base extension of this group to \(\mathbb Z\) is the group scheme \(N\).

(c) The pairs \(\mu=(\mu^{\mathrm{rk}},\mu^+)\) and \(\epsilon=(\epsilon^{\mathrm{rk}},\epsilon^+)\) are Tits
morphisms \(G\times G\to G\) and \(\operatorname{Spec}\mathbb F_1\to G\), and \((G,\mu,\epsilon)\) is a Tits
monoid.

(d) \((G,\mu,\epsilon)\) is a Tits–Weyl model of \(\mathrm{SL}_{2,\mathbb Z}\). Its Weyl kernel is
\(\mathfrak e=\operatorname{Spec}\mathbb F_1[t^{\pm1}]\), its canonical torus is the diagonal torus \(T\), and
\[
\mathfrak e_{\mathbb Z}=T=C(T),\qquad G^{\mathrm{rk}}_{\mathbb Z}=N=N(T).
\]

*Proof.* (a) The elements \(m(a),m(b),m(c),m(d)\) are sums of monomials, so they lie in \(B_2^+\). Since \(B_1^+\)
consists of the sums of products of \(a,b,c,d\), we get \(m(B_1^+)\subseteq B_2^+\). The restriction is unique
because \(B_2^+\subseteq R_2\). By Section 4.4, \(\operatorname{Spec}B_2^+=G^+\times G^+\) and
\(\operatorname{Spec}B_3^+=G^+\times G^+\times G^+\). The two homomorphisms \(R_1\to R_3\) that express the
associativity of the group law of \(\mathrm{SL}_2\) are equal, and they restrict to the two homomorphisms
\(B_1^+\to B_3^+\) that express the associativity of \(\mu^+\). The same argument applies to the unit, where the
counit \(R_1\to\mathbb Z\) restricts to \(B_1^+\to\mathbb N\). The base extension of \(\mu^+\) to \(\mathbb Z\) is
given by \(m\). The antipode sends \(b\) to \(-b\). By Proposition 1.12, \(B_1^+\) is the set of combinations of
reduced monomials with coefficients in \(\mathbb N\), and the reduced monomials are a basis of \(R_1\). So
\(-b\notin B_1^+\).

(b) On \(T\) we use the coordinate \(t=a\), so a point of \(T\) is the matrix with diagonal entries \(t,t^{-1}\).
On \(w_0T\) we use the coordinate \(t=b\), so a point is \(\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix}\). Then
\[
\begin{pmatrix}t_1&0\\0&t_1^{-1}\end{pmatrix}\begin{pmatrix}0&t_2\\-t_2^{-1}&0\end{pmatrix}
=\begin{pmatrix}0&t_1t_2\\-(t_1t_2)^{-1}&0\end{pmatrix},\qquad
\begin{pmatrix}0&t_1\\-t_1^{-1}&0\end{pmatrix}\begin{pmatrix}t_2&0\\0&t_2^{-1}\end{pmatrix}
=\begin{pmatrix}0&t_1t_2^{-1}\\-t_1^{-1}t_2&0\end{pmatrix},
\]
\[
\begin{pmatrix}0&t_1\\-t_1^{-1}&0\end{pmatrix}\begin{pmatrix}0&t_2\\-t_2^{-1}&0\end{pmatrix}
=\begin{pmatrix}-t_1t_2^{-1}&0\\0&-t_1^{-1}t_2\end{pmatrix},
\]
and the product of two diagonal matrices has the entry \(t_1t_2\). So \(N\) is closed under the product, and on
the component of \((x,y)\) the product is given by the ring homomorphism
\(\mathbb Z[t^{\pm1}]\to\mathbb Z[t_1^{\pm1},t_2^{\pm1}]\) with the value of \(t\) stated in (b). This homomorphism
maps the monoid of \(K_{xy}\) into the monoid of \(K_{(x,y)}\): for \(x=y=w\) the value \(-t_1t_2^{-1}\) lies in
\(K_{(w,w)}=\mathbb F_{1^2}[t_1^{\pm1},t_2^{\pm1}]\), and \(K_{ww}=K_e\) has no element \(-1\) that would have to be
mapped. By Proposition 1.2(c) it is a morphism of blueprints \(m_{x,y}\). It is unique, because \(K_{(x,y)}\) is
contained in its ring. By Proposition 7.1, \(G^{\mathrm{rk}}\times G^{\mathrm{rk}}=(G^2)^{\mathrm{rk}}\) is the
disjoint union of the spaces \(\operatorname{Spec}K_{(x,y)}\). Let \(\mu^{\mathrm{rk}}\) map the component of
\((x,y)\) to the component of \(xy\) by \(m_{x,y}\). By construction \((\mu^{\mathrm{rk}})_{\mathbb Z}\) is the
product of \(N\).

The inverse of a diagonal matrix with entries \(t,t^{-1}\) has the entries \(t^{-1},t\). The inverse of
\(\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix}\) is \(\begin{pmatrix}0&-t\\t^{-1}&0\end{pmatrix}\). So the inverse of
\(N\) is given on \(T\) by \(t\mapsto t^{-1}\) and on \(w_0T\) by \(t\mapsto-t\). These are morphisms of blueprints
\(K_e\to K_e\) and \(K_w\to K_w\), and they define \(\iota^{\mathrm{rk}}:G^{\mathrm{rk}}\to G^{\mathrm{rk}}\). The
unit of \(N\) is the identity matrix, which lies on \(T\) at \(t=1\); it is the base extension of
\(\epsilon^{\mathrm{rk}}\).

It remains to check the group axioms for \(\mu^{\mathrm{rk}},\epsilon^{\mathrm{rk}},\iota^{\mathrm{rk}}\). Each
axiom is an equality of two morphisms between blue schemes that are finite disjoint unions of spectra of the blue
fields \(K_x\) (by Proposition 7.1, for \(n\le3\)) or of \(\mathbb F_1\). Such a spectrum is one point, and the blue
fields are global (Proposition 4.7). So by Theorem 4.8(b) a morphism between two such disjoint unions is a map
between the sets of components together with morphisms of blueprints between the blue fields, in the opposite
direction. It is determined by its base extension to \(\mathbb Z\): the map of components is determined because no
component becomes empty, and each morphism of blue fields is determined because each blue field is contained in
its ring. After base extension to \(\mathbb Z\) the axioms hold, because \(N\) is a group scheme. So they hold for
\(G^{\mathrm{rk}}\).

(c) The square of Definition 6.9 for \(\mu\) is
\[
\begin{array}{ccc}
N\times N&\longrightarrow&N\\
\downarrow&&\downarrow\\
\mathrm{SL}_2\times\mathrm{SL}_2&\longrightarrow&\mathrm{SL}_2
\end{array}
\]
with the products as horizontal maps and the inclusions as vertical maps, by Proposition 7.1(c) and the
constructions in (a) and (b). It commutes. The square for \(\epsilon\) commutes because both composites are the
identity matrix in \(\mathrm{SL}_2(\mathbb Z)\). By Proposition 7.1(d) the blue schemes \(G^2\) and \(G^3\) are the
products of two and three copies of \(G\) in \(\operatorname{Sch}_{\mathcal T}\), and
\(\operatorname{Spec}\mathbb F_1\) is final (Lemma 6.12). A Tits morphism is a pair, so the associativity of
\(\mu\) and the unit property of \(\epsilon\) follow from the same properties of \(\mu^+,\epsilon^+\) in (a) and of
\(\mu^{\mathrm{rk}},\epsilon^{\mathrm{rk}}\) in (b).

(d) By (a), \(G_{\mathbb Z}\) with \(\mu_{\mathbb Z}\) is the group scheme \(\mathrm{SL}_{2,\mathbb Z}\). So \(G\)
is a Tits model. The image of \(\epsilon^{\mathrm{rk}}\) is the point \(e\). So the Weyl kernel is
\(\mathfrak e=\operatorname{Spec}K_e\). On it \(\mu^{\mathrm{rk}}\) is given by \(t\mapsto t_1t_2\): this is the
multiplicative group over \(\mathbb F_1\), a commutative group. Its base extension
\(\mathfrak e_{\mathbb Z}=\operatorname{Spec}\mathbb Z[t^{\pm1}]\) is the torus \(T\). So the canonical torus is
\(T\).

We compute the centralizer and the normalizer of \(T\). Let \(k\) be a ring,
\(g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(k)\), let \(k'\) be a \(k\)-algebra and \(s\in k'^\times\),
and let \(\tau\) be the diagonal matrix with entries \(s,s^{-1}\). Then
\[
g\tau=\begin{pmatrix}as&bs^{-1}\\cs&ds^{-1}\end{pmatrix},\quad
\tau g=\begin{pmatrix}as&bs\\cs^{-1}&ds^{-1}\end{pmatrix},\quad
g\tau g^{-1}=\begin{pmatrix}ads-bcs^{-1}&ab(s^{-1}-s)\\cd(s-s^{-1})&ads^{-1}-bcs\end{pmatrix}.
\]
Let \(k_1=k[s,s^{-1}]\) be the ring of Laurent polynomials, in which \(s-s^{-1}\) is not a zero divisor, and let
\(\tau_1\in T(k_1)\) be the matrix \(\tau\) for this \(s\).

If \(g\in C(T)(k)\), then \(g\tau_1=\tau_1g\), so \(b(s-s^{-1})=0\) and \(c(s-s^{-1})=0\), hence \(b=c=0\).
Conversely a diagonal matrix commutes with all diagonal matrices. So \(C(T)=V(b,c)=T\).

If \(g\in N(T)(k)\), then \(g\tau_1g^{-1}\) is diagonal, so \(ab=cd=0\). Conversely let \(ab=cd=0\). Then also
\(ac=ac(ad-bc)=a^2cd-abc^2=0\) and \(bd=bd(ad-bc)=abd^2-b^2cd=0\). The formula shows that \(g\tau g^{-1}\) is
diagonal for every \(k'\) and every \(\tau\in T(k')\), so \(gT(k')g^{-1}\subseteq T(k')\). The matrix
\(g^{-1}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\) satisfies the same conditions, so
\(g^{-1}T(k')g\subseteq T(k')\) as well. Hence \(gT(k')g^{-1}=T(k')\), and
\(N(T)=V(ab,cd)=V(ab,ac,bd,cd)=N\).

The torus \(T\) is a maximal torus: if \(k\) is an algebraically closed field, a torus of \(\mathrm{SL}_{2,k}\)
that contains \(T_k\) is commutative, so it lies in \(C(T_k)=T_k\). By Proposition 7.1(c),
\(G^{\mathrm{rk}}_{\mathbb Z}=N=N(T)\), and \(\mathfrak e_{\mathbb Z}=T=C(T)\). So \(\Psi_{\mathfrak e}\), which
is induced by the inclusion \(G^{\mathrm{rk}}_{\mathbb Z}\subseteq N(T)\), is the identity of \(N/T\). This
quotient is the constant group scheme of order \(2\): the morphism from \(N=T\sqcup w_0T\) to
\(\operatorname{Spec}\mathbb Z\sqcup\operatorname{Spec}\mathbb Z\) is a homomorphism of group schemes with kernel
\(T\). \(\square\)

*Reference:* [Lorscheid 2018a, Theorem 4.2]; [Lorscheid 2018a, Appendix A.2] describes the points of this model.

**Corollary 7.3.**

(a) The Weyl monoid \(\mathcal W(G)=\{e,w\}\) is the group of order \(2\), which is the ordinary Weyl group of
\(\mathrm{SL}_2\). The rank of \(G\) is \(1\), the reductive rank of \(\mathrm{SL}_2\).

(b) \(G^{\mathcal T}(\mathbb F_1)\) is the trivial group.

(c) \(G^{\mathcal T}(\mathbb F_{1^2})\) is isomorphic to \(N(\mathbb Z)=\{\pm1,\pm w_0\}\), the cyclic group of
order \(4\). This is the extended Weyl group of \(\mathrm{SL}_2\).

(d) For every semiring \(S\), the set \(G(S)=\operatorname{Hom}(B_1,S)\) is
\[
\mathrm{SL}_2(S)=\Bigl\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:a,b,c,d\in S,\ ad=bc+1\Bigr\},
\]
and \(m^+\) induces on it the product of matrices. So \(\mathrm{SL}_2(S)\) is a monoid, and it is the group
\(\mathrm{SL}_2(S)\) if \(S\) is a ring.

*Proof.* (a) By Theorem 7.2(b), \(\mathcal W(\mu)\) is the product \((x,y)\mapsto xy\) of \(\{e,w\}\). The ordinary
Weyl group is \((N/T)(\mathbb C)\), of order \(2\). The rank is \(1\) by Proposition 7.1(b), and \(T\) has
dimension \(1\).

(b) and (c). Let \(C\) be \(\mathbb F_1\) or \(\mathbb F_{1^2}\). By Example 6.7(a),
\((\operatorname{Spec}C)^{\mathrm{rk}}=\operatorname{Spec}C\). Its semiring \(C^+\) is \(\mathbb N\) or
\(\mathbb Z\), and \(C_{\mathbb Z}=\mathbb Z\). Both \(\mathbb N\) and \(\mathbb Z\) are global: for \(\mathbb N\)
use Lemma 4.5(d) and Example 2.2(d), since the intersection of the sets
\(\{u/s:u,s\in\mathbb N,\ p\nmid s\}\) over all primes \(p\) is \(\mathbb N\). Let \(\varphi\) be a Tits morphism
\(\operatorname{Spec}C\to G\). By Theorem 4.8(b), \(\varphi^{\mathrm{rk}}\) is a point \(x\in\{e,w\}\) together
with a morphism of blueprints \(f:K_x\to C\), and \(\varphi^+\) is a homomorphism \(g:B_1^+\to C^+\), that is, a
matrix in \(\mathrm{SL}_2(\mathbb Z)\) with entries in \(C^+\). The square of Definition 6.9 says that this matrix
is the point \(n(x,f)\) of \(N(\mathbb Z)\) that \(f\) defines on the component of \(x\). So \(\varphi\) is
determined by \((x,f)\), and a pair \((x,f)\) comes from a Tits morphism if and only if the matrix \(n(x,f)\) has
entries in \(C^+\).

For \(C=\mathbb F_1\): there is no morphism \(K_w\to\mathbb F_1\), because \(K_w\) is with \(-1\) and \(\mathbb F_1\)
is not. The only morphism \(K_e\to\mathbb F_1\) sends \(t\) to \(1\), and \(n(e,f)\) is the identity matrix. So
there is exactly one Tits point. For \(C=\mathbb F_{1^2}\): the morphisms \(K_e\to\mathbb F_{1^2}\) are
\(t\mapsto\pm1\), with \(n(e,f)=\pm1\), and the morphisms \(K_w\to\mathbb F_{1^2}\) are \(t\mapsto\pm1\), with
\(n(w,f)=\pm w_0\). So \(\varphi\mapsto n(x,f)\) is a bijection from \(G^{\mathcal T}(\mathbb F_{1^2})\) to
\(N(\mathbb Z)\). It respects products, because the base extension of \(\mu\) to \(\mathbb Z\) is the product of
matrices. The group \(N(\mathbb Z)\) is cyclic of order \(4\), since \(w_0^2=-1\). The extended Weyl group is
\(N(T)(\mathbb Z)=N(\mathbb Z)\).

(d) The description of \(G(S)\) is Proposition 1.12(c) with (1.1). The product of two points \(g,h\) is the
homomorphism \(B_1^+\to S\) obtained from \(m^+\) and the pair \((g,h)\); the formulas for \(m\) show that it is the
product of the matrices. It is associative with the identity matrix as unit by Theorem 7.2(a). \(\square\)

Compare (b) with Proposition 6.1(a): there are three ordinary morphisms \(\operatorname{Spec}\mathbb F_1\to G\) and
one Tits morphism. The Weyl group is not \(G^{\mathcal T}(\mathbb F_1)\); it is \(\mathcal W(G)\). The non-trivial
element \(w\) of the Weyl group becomes a Tits point over \(\mathbb F_{1^2}\), in two ways, \(w_0\) and \(-w_0\).
This is how the theory avoids the obstruction of Section 6.1.

**Example 7.4 (\(\mathrm{SL}_2\) over the Boolean semiring).** Let \(\mathbb B=\{0,1\}\) with \(1+1=1\). In
\(\mathbb B\) the equation \(ad=bc+1\) says \(ad=1\). So \(\mathrm{SL}_2(\mathbb B)\) has the four elements
\[
1=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad u=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
l=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad j=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
with \(u^2=u\), \(l^2=l\), \(ul=lu=j\), and \(j\) absorbs \(u\), \(l\) and \(j\). This monoid is not a group. It
shows why the theory produces monoids and not groups: the inverse of a matrix needs \(-1\).

## 8. What blueprints achieve for Tits's problem, and what remains open

### 8.1 What is achieved

For \(\mathrm{SL}_2\), Section 7 gives the following picture. Theorem 6.15 asserts the same picture for the groups
listed there.

1. *A model.* The blue scheme \(G=\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\) is given by the equation of the
   group, written without a minus sign. Its base extension to \(\mathbb Z\) is \(\mathrm{SL}_{2,\mathbb Z}\). Its
   points are the zero patterns of the matrices of determinant \(1\), and its two closed points are the patterns of
   the two cosets of the diagonal torus in its normalizer.
2. *The group law.* The group law is not a morphism of blue schemes (Proposition 6.1). It is a Tits morphism: the
   pair of the matrix product on the semiring scheme \(G^+\) and of the group law of the rank space
   \(G^{\mathrm{rk}}\), which is a model over \(\mathbb F_1\) of the normalizer \(N\) (Theorem 7.2).
3. *The Weyl group.* The Weyl group is \(\mathcal W(G)\), the set of points of the rank space with the product
   induced by the group law. The functor \(\mathcal W\) takes the place of the set of \(\mathbb F_1\)-points.
4. *Points.* For every semiring \(S\) the set \(G(S)\) is a monoid of matrices with entries in \(S\) (Corollary
   7.3(d)). This applies to semirings without negatives, such as the Boolean semiring (Example 7.4). The Tits
   points with values in \(\mathbb F_{1^2}\) form the extended Weyl group.

Two things are given up. The first is the formula \(G(\mathbb F_1)=W\). The ordinary \(\mathbb F_1\)-points of \(G\)
do not form a group (Proposition 6.1), and the Tits points with values in \(\mathbb F_1\) form a subgroup of the
Weyl group that can be small: the alternating group \(A_n\) for the model of \(\mathrm{SL}_n\), and the trivial
group for the adjoint models (Theorem 6.15). [Lorscheid 2018a, Introduction] says explicitly that the theory breaks
with the convention that \(G(\mathbb F_1)\) is the Weyl group. The second is the inverse. The definition of a
Tits–Weyl model asks only for a monoid in the Tits category. Some models are groups: the torus
\(\operatorname{Spec}\mathbb F_1[t^{\pm1}]\), with \(t\mapsto t_1t_2\) and the inverse \(t\mapsto t^{-1}\)
[Lorscheid 2018a, Section 3.4]. The model of \(\mathrm{SL}_2\) is not a group, because its antipode needs \(-1\)
(Theorem 7.2(a)). According to
[Lorscheid 2018a, Introduction], Tits–Weyl models become groups after base extension to \(\mathbb F_{1^2}\); no
proof is given there.

[Lorscheid 2018a] and [Lorscheid 2016] contain further results. This lesson proves none of them.

- *Subgroups.* Let \(\mathcal G\) be a reductive group scheme with a Tits–Weyl model \(G\) and canonical torus
  \(T\). The parabolic subgroups of \(\mathcal G\) that contain \(T\) correspond to the submonoids of \(G\) that are
  Tits–Weyl models of them [Lorscheid 2018a, Theorem 5.2], and each of these submonoids contains a Tits–Weyl model
  of a Levi subgroup [Lorscheid 2018a, Theorem 5.7]. Exercise 5 treats the upper triangular matrices in
  \(\mathrm{SL}_2\) by hand.
- *Thin geometries.* [Lorscheid 2016, Section 3] considers a Tits–Weyl model that acts on a projective space over
  \(\mathbb F_1\) by a Tits morphism. It states, without proofs, that such an action yields a Coxeter complex with
  the action of the Weyl group and, on the level of \(\mathbb F_q\)-points, a spherical building with the action of
  \(\mathcal G(\mathbb F_q)\): for the types \(A_n\), \(B_n\) and \(C_n\) in Theorems 3.2 and 3.3 there, and for
  \(D_n\), with a modified construction, in Theorem 3.7 there. For the adjoint representation it states that the
  Coxeter complex of every type arises (Theorem 3.9 there), and it formulates the statement about buildings as a
  conjecture (Conjecture 3.10 there).

### 8.2 The general case

This lesson proves Theorem 6.15 for \(\mathrm{SL}_2\) only. The proofs of the other cases are in
[Lorscheid 2018a]. A reader who wants to verify them needs the following parts of that paper.

1. *Products in the Tits category:* [Lorscheid 2018a, Proposition 3.3, Theorem 3.5 and Theorem 3.8]. They are used
   to form \(G\times G\), and to see that \(\mathcal W\) and the base extensions send monoids to monoids. The
   proofs use the two formulas discussed after Definition 6.13, which need a hypothesis of cancellativity. For a
   given model \(G\) one can instead prove directly that the blue schemes \(G^n\) satisfy the hypotheses of Lemma
   6.11, as in Proposition 7.1. This lesson does this for \(\mathrm{SL}_2\), and for its subgroup of upper
   triangular matrices in Exercise 5, and for no other group.
2. *The special linear group:* [Lorscheid 2018a, Proposition 4.1 and Theorem 4.2]. Example 8.1 below determines
   the points of the model, and Example 8.2 its points with values in semirings. The proof of Theorem 4.2 there
   obtains \(\mu^+\) from the fact that the formulas for the product of two matrices contain no minus sign, and
   the uniqueness of \(\mu^+\) from cancellativity. The first step is complete if the pre-addition of
   \(\mathbb F_1[\mathrm{SL}_n]\) is generated by the determinant relation, as the proof of Proposition 4.1 there
   says, or if the semiring of \(\mathbb F_1[\mathrm{SL}_n]\otimes_{\mathbb F_1}\mathbb F_1[\mathrm{SL}_n]\) is
   contained in a ring; the second step uses the latter. For \(n=2\) both hold (Proposition 1.12), and the result
   is Theorem 7.2(a). For \(n\ge3\) neither holds (Example 8.2), and this lesson does not decide whether \(\mu^+\)
   exists (question (e) of Section 8.3).
3. *Closed subgroups:* the cube lemma [Lorscheid 2018a, Lemma 4.6] and the criterion
   [Lorscheid 2018a, Theorem 4.7] for closed subgroups of a group scheme with a Tits–Weyl model. It is applied in
   [Lorscheid 2018a, Section 4.3] to the general linear, symplectic and orthogonal groups. The criterion restricts
   the monoid law of the larger model to the subgroup; for \(\mathrm{GL}_n\) the larger model is that of
   \(\mathrm{SL}_{n+1}\). So these cases build on item 2.
4. *Adjoint groups:* [Lorscheid 2018a, Lemma 4.10, Proposition 4.11 and Theorem 4.12]. The monoid law \(\mu^+\) is
   obtained there from that of a general linear group, with the cube lemma.
5. *The properties of Tits–Weyl models:* [Lorscheid 2018a, Lemmas 3.11 and 3.12 and Theorem 3.14].

[Lorscheid 2016, Theorem 2.5] states more: every split reductive group scheme has a Tits–Weyl model, and so do its
Levi subgroups and its parabolic subgroups that contain the canonical torus. The text before that theorem says that
the statement is proved in [Lorscheid 2018a] for a large class of groups, and that an idea of M. Reineke extends it
to all split reductive group schemes. [Lorscheid 2016] gives no proof of this extension, and none of the works
cited in this lesson contains one.

**Example 8.1 (the points of the model of \(\mathrm{SL}_n\)).** Let \(n\ge1\), let
\(R=\mathbb Z[T_{ij}:1\le i,j\le n]/(\det(T_{ij})-1)\), and let
\(\mathrm{SL}_n=\operatorname{Spec}\mathbb F_1\langle t_{ij}\rangle\) be the \(\mathbb F_1\)-model of Example 1.11(b).
By Corollary 3.4 its points are the ideals \(\mathfrak p_I\), where \(I\) runs through the zero patterns of the
matrices of determinant \(1\) over fields. A set \(I\) of positions \((i,j)\) is such a zero pattern if and only if
its complement contains the graph \(\{(i,\sigma(i))\}\) of a permutation \(\sigma\). Indeed, if
\(\det(x_{ij})\neq0\), then some product \(\prod_ix_{i,\sigma(i)}\) is not zero. Conversely let the complement
\(J\) of \(I\) contain the graph of \(\sigma\). Let \(k=\mathbb Q(y_{ij}:(i,j)\in J)\) be a field of rational
functions, and let \(X\) be the matrix with the entry \(y_{ij}\) at the positions in \(J\) and \(0\) elsewhere. Its
determinant is a polynomial in the \(y_{ij}\). Different permutations contribute different monomials, and the
monomial of \(\sigma\) occurs. So \(\det X\neq0\). Dividing the first row of \(X\) by \(\det X\) gives a matrix of
determinant \(1\) with zero pattern \(I\).

Hence the closed points of \(\mathrm{SL}_n\) are the \(n!\) points \(\mathfrak p^\sigma\) whose zero pattern is the
complement of the graph of a permutation \(\sigma\), as stated in [Lorscheid 2018a, Proposition 4.1]. For \(n=2\)
these are the points \(e\) and \(w\).

**Example 8.2 (the points of \(\mathrm{SL}_n\) with values in a semiring).** Let \(n\ge1\). We keep the notation of
Example 8.1 and write \(\mathbb F_1[\mathrm{SL}_n]=\mathbb F_1\langle t_{ij}\rangle\). For a permutation \(\pi\) of
\(\{1,\dots,n\}\) let \(T_\pi=\prod_iT_{i,\pi(i)}\), and put
\[
E=\sum_{\pi\ \text{even}}T_\pi,\qquad O=\sum_{\pi\ \text{odd}}T_\pi,\qquad Q=O+1 .
\]
These are formal sums of monomials, and \(\det(T_{ij})-1=E-Q\). For formal sums \(x,y\) of monomials in the
\(T_{ij}\) we write \(x\sim y\) if \(x-y\) lies in the ideal \((E-Q)\) of \(\mathbb Z[T_{ij}]\), and
\(x\approx y\) if \(x\) and \(y\) are congruent modulo the congruence generated by the pair \((E,Q)\). Then
\(x\approx y\) implies \(x\sim y\). By Example 1.11(b), \(\mathbb F_1[\mathrm{SL}_n]\) is
\(\mathbb F_1[T_{ij}]/\!\!/\langle\sim\rangle\).

Let \(S\) be a semiring. For an \(n\times n\) matrix \(u=(u_{ij})\) over \(S\) and a formal sum \(x\), let
\(x(u)\in S\) be the value of \(x\) at \(T_{ij}=u_{ij}\). Let \(\mathcal M_n(S)\) be the set of all \(u\) with
\(E(u)=Q(u)\); this is the equation of Theorem 6.15(b). By Section 4.4 and Lemma 1.4,
\[
\mathrm{SL}_n(S)=\operatorname{Hom}(\mathbb F_1[\mathrm{SL}_n],S)
=\{u:\ x(u)=y(u)\ \text{whenever}\ x\sim y\},
\]
\[
\mathcal M_n(S)=\operatorname{Hom}\bigl(\mathbb F_1[T_{ij}]/\!\!/\langle E\equiv Q\rangle,S\bigr),\qquad
\mathrm{SL}_n(S)\subseteq\mathcal M_n(S).
\]

(a) *For every semiring \(S\), the set \(\mathcal M_n(S)\) is a monoid under the product of matrices.* Let
\(u,v\in\mathcal M_n(S)\). For a map \(k\) from \(\{1,\dots,n\}\) to itself put \(P_k=\prod_iu_{i,k(i)}\).
Multiplying out gives, for every permutation \(\sigma\),
\[
\prod_i(uv)_{i,\sigma(i)}=\sum_kP_k\prod_iv_{k(i),\sigma(i)} .
\]
If \(k(i_1)=k(i_2)\) for some \(i_1\neq i_2\), the product \(\prod_iv_{k(i),\sigma(i)}\) does not change when
\(\sigma\) is composed with the transposition of \(i_1\) and \(i_2\), and this composition exchanges the even and
the odd permutations. So the maps \(k\) that are not injective contribute the same element \(\nu\) of \(S\) to
\(E(uv)\) and to \(O(uv)\). If \(k=\pi\) is a permutation, then \(P_\pi=T_\pi(u)\) and
\(\prod_iv_{\pi(i),\sigma(i)}=T_{\sigma\pi^{-1}}(v)\). Hence
\[
E(uv)=\nu+E(u)E(v)+O(u)O(v),\qquad O(uv)=\nu+E(u)O(v)+O(u)E(v).
\]
Since \(E(u)=O(u)+1\) and \(E(v)=O(v)+1\), both \(E(uv)\) and \(O(uv)+1\) are equal to
\(\nu+2\,O(u)O(v)+O(u)+O(v)+1\). So \(uv\in\mathcal M_n(S)\). The identity matrix lies in \(\mathcal M_n(S)\), and
the product of matrices over \(S\) is associative.

(b) *If \(S\) is contained in a ring \(R'\), then \(\mathrm{SL}_n(S)=\mathcal M_n(S)\).* Let
\(u\in\mathcal M_n(S)\). In \(R'\) the equation \(E(u)=Q(u)\) says \(\det u=1\). So the ring homomorphism
\(\mathbb Z[T_{ij}]\to R'\) with \(T_{ij}\mapsto u_{ij}\) sends \(E-Q\) to \(0\). If \(x\sim y\), it sends \(x-y\)
to \(0\); so \(x(u)=y(u)\) in \(R'\), and both sides lie in \(S\). With (a), this proves the last sentence of
Theorem 6.15(b).

(c) *For \(n=3\) the relations \(\sim\) and \(\approx\) are different.* Write the variables as
\[
\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix},\qquad E=aei+bfg+cdh,\qquad Q=afh+bdi+ceg+1 .
\]
Put \(p=bcd+ace+abf\) and \(r=abcdei+abcefg+abcdfh\). Multiplying out gives \(pE=x+r\) and \(pQ=y+r\) with
\[
x=b^2cdfg+bc^2d^2h+a^2ce^2i+ac^2deh+a^2befi+ab^2f^2g,
\]
\[
y=b^2cd^2i+bc^2deg+a^2cefh+ac^2e^2g+a^2bf^2h+ab^2dfi+bcd+ace+abf .
\]
So \(x-y=p(E-Q)\), and \(x\sim y\). We show \(x\not\approx y\) with the steps of Section 1.2. A step that starts at
\(x\) writes \(x=w+m\lambda\) with a monomial \(m\) and \(\lambda=E\) or \(\lambda=Q\). If \(\lambda=Q\), then \(m\)
and \(m\cdot afh\) are terms of \(x\); but all terms of \(x\) have degree \(6\). If \(\lambda=E\), then
\(m\cdot aei\), \(m\cdot bfg\) and \(m\cdot cdh\) are terms of \(x\). The terms of \(x\) that are divisible by
\(aei\) are \(a^2ce^2i\) and \(a^2befi\). So \(m=ace\) or \(m=abf\). But \(ace\cdot bfg\) and \(abf\cdot cdh\) are
terms of \(r\) and not of \(x\). So no step starts at \(x\), and \(x\) is congruent modulo \(\approx\) only to
itself. Since \(x\neq y\), we get \(x\not\approx y\).

(d) *For \(n\ge4\) the relations \(\sim\) and \(\approx\) are different as well.* Let \(x,y,p,r\) be as in (c), in
the variables \(T_{ij}\) with \(i,j\le3\), and let \(E_3,O_3,Q_3\) be the sums \(E,O,Q\) for these nine variables.
Put \(s=T_{44}\cdots T_{nn}\). Then \(E=sE_3+E'\) and \(O=sO_3+O'\), where \(E'\) and \(O'\) are the sums of the
\(T_\pi\) over the even and the odd permutations \(\pi\) that move some \(i>3\). Put
\[
\tilde x=sx+pE',\qquad\tilde y=s(y-p)+p+pO' ,
\]
where \(y-p\) is \(y\) without its last three terms. Since \(pE_3=x+r\) and \(pO_3=(y-p)+r\), we get
\(\tilde x-\tilde y=pE-pO-p=p(E-Q)\). So \(\tilde x\sim\tilde y\). Let \(\phi\) be the morphism of monoids from
the monomials in the \(n^2\) variables to the monomials in the nine variables with \(\phi(T_{ij})=T_{ij}\) for
\(i,j\le3\), \(\phi(T_{ii})=1\) for \(i>3\), and \(\phi(T_{ij})=0\) for all other \(i,j\). Extended to formal sums,
\(\phi\) sends \(E\) to \(E_3\), \(Q\) to \(Q_3\), \(\tilde x\) to \(x\) and \(\tilde y\) to \(y\). So it sends a
step to a step or to an equality, and \(\tilde x\approx\tilde y\) would imply \(x\approx y\) for \(n=3\).

(e) *Consequences for \(n\ge3\).* The pre-addition of \(\mathbb F_1[\mathrm{SL}_n]\) is not generated by the
determinant relation. Let \(S_0\) be the semiring of \(\mathbb F_1[T_{ij}]/\!\!/\langle E\equiv Q\rangle\), and let
\(u_0\) be the matrix of the classes of the \(T_{ij}\) in \(S_0\). Then \(u_0\in\mathcal M_n(S_0)\). But
\(x(u_0)\neq y(u_0)\) for \(n=3\), and \(\tilde x(u_0)\neq\tilde y(u_0)\) for \(n\ge4\). So
\(u_0\notin\mathrm{SL}_n(S_0)\), and the hypothesis in (b) cannot be dropped. For \(n=2\) we have
\(\mathrm{SL}_2(S)=\mathcal M_2(S)\) for every semiring \(S\) (Corollary 7.3(d)), because \(\sim\) and \(\approx\)
agree by Proposition 1.12(c).

(f) *For \(n\ge3\) the blueprint
\(C=\mathbb F_1[\mathrm{SL}_n]\otimes_{\mathbb F_1}\mathbb F_1[\mathrm{SL}_n]\) is not cancellative.* Let \(J\) be
the \(n\times n\) matrix with all entries \(1\); its determinant is \(0\). First let \(\lambda\) be a formal sum
whose terms are different and are taken from the \(T_\pi\) and the monomial \(1\), and let \(\lambda\sim\rho\). Then
\(\rho-\lambda=f\cdot(E-Q)\) with \(f\in\mathbb Z[T_{ij}]\). Suppose that \(f\) is not constant, and let \(f_d\) be
its homogeneous part of highest degree \(d\ge1\). The part of degree \(d+n\) of \(f\cdot(E-Q)\) is
\(f_d\cdot\det(T_{ij})\). It is not zero, and its value at \(J\) is \(0\). Since \(\lambda\) has degree at most
\(n\), it is also the part of degree \(d+n\) of \(\rho\). But a non-zero polynomial with non-negative coefficients
has a positive value at \(J\). So \(f\) is an integer \(\ell\), and \(\rho=\lambda+\ell E-\ell Q\). Since \(\rho\)
has no negative coefficient, \(\ell>0\) is possible only if \(\lambda\) contains all terms of \(Q\), and
\(\ell<0\) only if \(\lambda\) contains all terms of \(E\). In all other cases \(\rho=\lambda\).

Let \(F\) be the monoid of the monomials in the \(T_{ij}\). We may take
\(C=(F\wedge F)/\!\!/\langle E_\otimes\rangle\), where \(E_\otimes\) consists of the pairs
\((\lambda\otimes1,\rho\otimes1)\) and \((1\otimes\lambda,1\otimes\rho)\) with \(\lambda\sim\rho\): by Lemma 1.4
and Proposition 1.14(a) this blueprint has the same morphisms to every blueprint as the tensor product of
Definition 1.13. Here \((\sum a_i)\otimes(\sum b_j)=\sum a_i\otimes b_j\). So a step in \(C\) replaces a part
\(\lambda\otimes m\) of a formal sum by \(\rho\otimes m\), or a part \(m\otimes\lambda\) by \(m\otimes\rho\), where
\(m\) is a monomial and \(\lambda\sim\rho\). Let \(t=T_{\mathrm{id}}\), and let \(E^\circ\) be \(E\) without the
term \(t\). Put
\[
z=t\otimes E^\circ+E^\circ\otimes1+O\otimes t+1\otimes O,\qquad
w=E^\circ\otimes t+1\otimes E^\circ+t\otimes O+O\otimes1 .
\]
In the ring \(\mathbb Z[T_{ij}]\otimes_{\mathbb Z}\mathbb Z[T_{ij}]\) we have
\[
z-w=(E-Q)\otimes(1-t)+(t-1)\otimes(E-Q).
\]
So \(z\) and \(w\) have the same image in \(C_{\mathbb Z}=R\otimes_{\mathbb Z}R\) (Proposition 1.14(b)). If
\(\lambda\otimes m\) or \(m\otimes\lambda\) is a part of \(z\), then \(\lambda\) is a part of one of the formal sums
\(E^\circ\), \(O\), \(t\) and \(1\). None of these four contains all terms of \(E\) or all terms of \(Q\), because
\(E\) has \(n!/2\ge3\) terms, among them \(t\), and \(Q\) consists of \(1\) and the terms of \(O\). By the first
part of the argument no step changes \(z\). So \(z\) is congruent only to itself, and \(z\neq w\) in \(C^+\).
Hence the map \(C^+\to C_{\mathbb Z}\) is not injective: the semiring of \(\mathrm{SL}_n\times\mathrm{SL}_n\) is
not contained in a ring.

### 8.3 Open problems

[Lorscheid 2018a] states the following problems.

(a) Does every Chevalley group, that is, every split reductive group scheme, have a Tits–Weyl model? Is there a
systematic construction? [Lorscheid 2018a, Introduction]. By Section 8.2, [Lorscheid 2016, Theorem 2.5] asserts a
positive answer to the first question, without a proof.

(b) A linear representation of a Chevalley group gives at most one Tits–Weyl model. When do two representations
give isomorphic models? Can the models be classified? [Lorscheid 2018a, Introduction]. For the adjoint group of
type \(A_1\) two models are described, and it is left open whether they are isomorphic in the Tits category
[Lorscheid 2018a, Remark A.1].

(c) Is there a canonical Tits–Weyl model of a Chevalley group? [Lorscheid 2018a, Introduction].

(d) Let \(U\) be the \(\mathbb F_1\)-model of the unipotent radical of a parabolic subgroup of a reductive group
scheme. Does \(\mathcal Z(U)\) consist of one point? This is what is needed to make \(U\) a Tits–Weyl model. It
holds for the parabolic subgroups of \(\mathrm{GL}_n\) that contain the upper triangular matrices
[Lorscheid 2018a, Remark 5.4 and Proposition 5.5].

This lesson adds two questions. They are questions of this lesson. The works cited here do not state them as open
problems.

(e) Let \(n\ge3\). Is the set \(\mathrm{SL}_n(S)\) closed under the product of matrices for every semiring \(S\)?
Taking for \(S\) the semiring of \(\mathbb F_1[\mathrm{SL}_n]\otimes_{\mathbb F_1}\mathbb F_1[\mathrm{SL}_n]\), one
sees that this is the same question as the following: is there a homomorphism from the semiring of
\(\mathbb F_1[\mathrm{SL}_n]\) to the semiring of
\(\mathbb F_1[\mathrm{SL}_n]\otimes_{\mathbb F_1}\mathbb F_1[\mathrm{SL}_n]\) that sends \(t_{ij}\) to
\(\sum_kt_{ik}\otimes t_{kj}\)? Such a homomorphism gives a morphism \(\mu^+\) as in Theorem 6.15(b). The answer is
yes for \(n=2\) (Theorem 7.2(a)), for the semirings \(S\) that are contained in a ring (Example 8.2(b)), and for
the sets \(\mathcal M_n(S)\) in place of \(\mathrm{SL}_n(S)\) (Example 8.2(a)).

(f) Is \(X_1\times X_2\) a product of \(X_1\) and \(X_2\) in the Tits category for all affine blue schemes
\(X_1\) and \(X_2\), as [Lorscheid 2018a, Theorem 3.5] states? Lemma 6.11 gives this when the rank space of
\(X_1\times X_2\) is the product of the rank spaces. This holds for the powers of
\(\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\) (Proposition 7.1). In Exercise 6 it does not hold, and
\(X_1\times X_2\) is a product in the Tits category all the same.

### 8.4 Bands and crowds

Later work returns to Tits's problem with other objects. We state what it claims. The lesson *A map of the
approaches* compares the approaches.

*Bands.* A *band* is a monoid \(B\) together with a *null set* \(N_B\). The null set is a subset of the semiring
\(\mathbb N[B]\) of formal sums that contains \(0\) and is closed under addition and under multiplication by
elements of \(B\), and for every \(a\in B\) there must be exactly one \(b\in B\) with \(a+b\in N_B\)
[Baker–Jin–Lorscheid 2024, Definition 1.1]. So a band records which sums count as zero, where a blueprint records
which sums are equal; and every band contains an element \(-1\), where a blueprint need not. A ring \(R\) is a band:
its null set consists of the sums that are zero in \(R\). The initial band is
\(\mathbb F_1^\pm=\{0,1,-1\}\), whose null set consists of the sums \(n\cdot1+n\cdot(-1)\); its monoid is the monoid
of \(\mathbb F_{1^2}\). The *Krasner hyperfield* is the band \(\mathbb K=\{0,1\}\) whose null set consists of the
sums \(n\cdot1\) with \(n\neq1\). Every band is an *ordered blueprint* [Baker–Jin–Lorscheid 2024, Section 1.2], that
is, a blueprint together with a partial order on its semiring that is compatible with sums and products
[Lorscheid 2018c, Definitions 5.1.1 and 5.2.1].

The points of the spectrum of a band in [Baker–Jin–Lorscheid 2024] are the prime ideals of the monoid \(B\), which
are called prime \(m\)-ideals there. The subsets that also satisfy the analogue of (I2) are called \(k\)-ideals.
For \(X=\operatorname{Spec}B\) the prime \(k\)-ideals form a second space, the *kernel space* of \(X\), which is
identified with the set \(X(\mathbb K)\) [Baker–Jin–Lorscheid 2024, Introduction]. The spectrum of this lesson
consists of prime ideals in the sense of Definition 2.1, which are the analogue of prime \(k\)-ideals.

*The Tits space.* The *Tits space* of a band scheme \(X\) is the set of closed points of \(X(\mathbb K)\)
[Baker–Jin–Lorscheid 2024, Section 3.4]. For the band scheme \(\mathrm{SL}_n\) defined by the relation
\(\det(T_{ij})-1\) over \(\mathbb F_1^\pm\), that section states that the closed points of
\(\mathrm{SL}_n(\mathbb K)\) are the ideals generated by the \(T_{ij}\) with \(j\neq\sigma(i)\), for
\(\sigma\in S_n\), and that this gives a bijection between the Tits space of \(\mathrm{SL}_n\) and the Weyl group
\(S_n\). These ideals have the same generators as the closed points of Example 8.1. The Introduction of
[Baker–Jin–Lorscheid 2024] says that a model with this property exists for a reductive group together with a
"sufficiently nice" representation, and refers to [Lorscheid–Thas 2023] and to its own Section 3.4. These two
texts establish the property for \(\mathrm{SL}_n\).

*Crowds.* [Lorscheid–Thas 2023, Introduction] counts [Lorscheid 2012b], [Lorscheid 2016] and [Lorscheid 2018a] as
solutions of Tits's problem and presents a further one. Its claims are the following.

- A *crowd* is a set \(G\) with an element \(1\) and a subset \(R\subseteq G^3\), the *crowd law*, subject to three
  axioms. A group is a crowd with \(R=\{(a,b,c):abc=1\}\) [Lorscheid–Thas 2023, Definition 5.1 and Section 5.2].
  An *algebraic crowd* is a functor from bands to crowds such that the underlying sets and the crowd laws are given
  by band schemes [Lorscheid–Thas 2023, Definition 5.9]. The main example is \(\mathrm{SL}_n\): the set
  \(\mathrm{SL}_n(B)\) consists of the \(n\times n\) matrices \((a_{ij})\) over \(B\) with
  \(\det(a_{ij})-1\in N_B\), and the crowd law consists of the triples \((a,b,c)\) with
  \(\sum_{k,l}a_{ik}b_{kl}c_{lj}-\delta_{ij}\in N_B\) for all \(i,j\), and the same for the cyclic permutations of
  \((a,b,c)\).
- The reason given for replacing the group law by a relation is the one met in Proposition 6.1: a group law uses the
  addition of the tensor powers of the coordinate algebra, and these tensor powers are not closed under addition
  [Lorscheid–Thas 2023, Section 5].
- [Lorscheid–Thas 2023, Theorem 1.1]: the simplices of the combinatorial flag variety \(\Omega_{S_n}\) of Borovik,
  Gelfand and White correspond bijectively to the \(\mathbb K\)-points of the flag varieties of all types, which
  are band schemes, and the face relation is given by the projections between flag varieties. The Coxeter complex
  of \(S_n\), which the paper regards as the projective geometry of dimension \(n-1\) over \(\mathbb F_1\) in the sense of Tits, is the subcomplex of the points all of whose vectors of Plücker coordinates
  have exactly one non-zero entry [Lorscheid–Thas 2023, Section 7.3].
- [Lorscheid–Thas 2023, Theorem 1.2]: the crowd \(\mathrm{SL}_n(\mathbb K)\) contains the symmetric group \(S_n\)
  as the subcrowd of permutation matrices, and \(\mathrm{SL}_n(\mathbb K)\) acts on \(\Omega_{S_n}\) by a *crowd
  activity* whose restriction to \(S_n\) is the usual action.
- [Lorscheid–Thas 2023, Theorem 5.14]: every closed subgroup scheme of \(\mathrm{SL}_{n,\mathbb Z}\) has a model
  over \(\mathbb F_1^\pm\) that is an affine algebraic crowd and that gives back, for every ring \(R\), the crowd of
  the group of \(R\)-points. The paper calls this immediate from the construction.

The crowd \(\mathrm{SL}_n(B)\) is not a group in general. The crowd \(\mathrm{SL}_2(\mathbb F_1^\pm)\) is the set
of the \(20\) matrices in \(\mathrm{SL}_2(\mathbb Z)\) with entries in \(\{0,1,-1\}\), and the product of
\(\begin{pmatrix}1&1\\0&1\end{pmatrix}\) with itself is empty [Lorscheid–Thas 2023, Example 5.11]. The same \(20\)
matrices are the morphisms of blueprints \(\mathbb F_1[\mathrm{SL}_2]\to\mathbb F_{1^2}\). Indeed, by Proposition
1.12(c) such a morphism is a matrix with entries \(\alpha,\beta,\gamma,\delta\in\{0,1,-1\}\) and
\(\alpha\delta=\beta\gamma+1\) in \(\mathbb Z\). Either \(\alpha\delta=1\) and \(\beta\gamma=0\), or
\(\alpha\delta=0\) and \(\beta\gamma=-1\). This gives \(2\cdot5+5\cdot2=20\) matrices.

[Lorscheid–Thas 2023] treats \(\mathrm{SL}_n\), that is, type \(A\). For the rest it states expectations and
problems. It expects that the formalism extends to other models of \(\mathrm{SL}_n\) and to other algebraic groups,
and that the Tits geometries of the types \(B\), \(C\) and \(D\) appear as subcomplexes of the
\(\mathbb K\)-points of suitable simplicial band schemes with crowd activities
[Lorscheid–Thas 2023, Section 7.6]. It names the study of the crowd activity of \(\mathrm{SL}_n(\mathbb K)\) on
\(\Omega_{S_n}\) as a problem [Lorscheid–Thas 2023, Introduction and Section 7.4].

### 8.5 Summary

Blueprints turn the two closed points of \(\operatorname{Spec}\mathbb F_1[\mathrm{SL}_2]\), and the \(n!\) closed
points of the model of \(\mathrm{SL}_n\), into the elements of the Weyl group. They let the group law descend to
\(\mathbb F_1\), at the price of a second notion of morphism. For \(\mathrm{SL}_2\) every step is proved in this
lesson. For \(\mathrm{SL}_n\) with \(n\ge3\) and for the groups built on it, the lesson reports the theorems of
[Lorscheid 2018a] and adds the questions (e) and (f) of Section 8.3 about their proofs. The cited works name as
open: a construction for all split reductive group schemes; the classification of Tits–Weyl models and a canonical
choice; unipotent radicals; and, in the language of bands and crowds, all Dynkin types other than \(A\).

## 9. Exercises

**Exercise 1 (morphisms between the blueprints \(\mathbb F_{1^n}\)).** Let \(k,n\ge1\).

(a) Show that the morphisms of blueprints \(\mathbb F_{1^k}\to\mathbb F_{1^n}\) are exactly the maps that send
\(0\) to \(0\) and restrict to an injective group homomorphism \(\mu_k\to\mu_n\).

(b) Deduce that a morphism exists if and only if \(k\) divides \(n\), and that there are then \(\varphi(k)\)
morphisms, where \(\varphi\) is Euler's function.

(c) Compare with the morphisms of monoids \((\mu_k)_0\to(\mu_n)_0\).

*Solution.* (a) Let \(g:(\mu_k)_0\to(\mu_n)_0\) be a morphism of monoids. For \(\zeta\in\mu_k\) we have
\(g(\zeta)g(\zeta^{-1})=g(1)=1\), so \(g(\zeta)\) is a unit, that is, \(g(\zeta)\in\mu_n\). So \(g\) restricts to a
group homomorphism \(\mu_k\to\mu_n\), and every group homomorphism arises in this way. By Proposition 1.10 the
underlying monoid of \(\mathbb F_{1^k}\) is \((\mu_k)_0\). So by Lemma 1.4, \(g\) is a morphism of blueprints
\(\mathbb F_{1^k}\to\mathbb F_{1^n}\) if and only if
\[
\sum_{\zeta\in H}g(\zeta)\equiv0\quad\text{in }\mathbb F_{1^n}\tag{9.1}
\]
for every subgroup \(H\neq\{1\}\) of \(\mu_k\). If \(g\) is injective, then \(g(H)\) is a subgroup of \(\mu_n\) of
the same order as \(H\), and (9.1) is one of the defining relations of \(\mathbb F_{1^n}\). If \(g\) is not
injective, take for \(H\) the kernel of \(g\). Then the left side of (9.1) is the sum of \(|H|\) terms \(1\), with
\(|H|\ge2\). Its image in \(\mathbb F_{1^n}^+\) is the number \(|H|\) in \(\mathbb Z[\zeta_n]\) if \(n\ge2\), and in
\(\mathbb N\) if \(n=1\). It is not \(0\). So (9.1) fails.

(b) An injective homomorphism from a cyclic group of order \(k\) to a cyclic group of order \(n\) exists if and
only if \(k\) divides \(n\). It sends a fixed generator to an element of order \(k\), and \(\mu_n\) has
\(\varphi(k)\) such elements.

(c) Every group homomorphism \(\mu_k\to\mu_n\) gives a morphism of monoids, and there are \(\gcd(k,n)\) of them: a
generator may go to any element whose order divides \(k\). For example there are two morphisms of monoids
\((\mu_2)_0\to(\mu_4)_0\), and one morphism of blueprints \(\mathbb F_{1^2}\to\mathbb F_{1^4}\), which sends \(-1\) to
\(-1\). There is a morphism of monoids \((\mu_n)_0\to\mathbb F_1\) for every \(n\), and no morphism of blueprints
\(\mathbb F_{1^n}\to\mathbb F_1\) for \(n\ge2\). So the blueprints \(\mathbb F_{1^n}\) behave like fields: all
morphisms between them are injective. In particular the automorphism group of \(\mathbb F_{1^n}\) is
\((\mathbb Z/n\mathbb Z)^\times\), the Galois group of \(\mathbb Q(\zeta_n)\) over \(\mathbb Q\).

*Reference:* [Lorscheid 2012a, Section 1.10] states that every morphism \(\mathbb F_{1^k}\to\mathbb F_{1^n}\) is
injective.

**Exercise 2 (an archimedean example).** Let \(A=[-1,1]\cap\mathbb Q\), a monoid under multiplication.

(a) Let \(B=(A\subset\mathbb Q)\). Show that \(\{0\}\) and \(B\) are the only ideals of \(B\). Deduce that
\(\operatorname{Spec}B\) is one point, that \(B\) is not local and not global, and that \(\Gamma B=\mathbb Q\).

(b) Let \(B'=A/\!\!/\langle1+(-1)\equiv0\rangle\). Let \(P\) be the set \((0,1]\cap\mathbb Q\) with its
multiplication, and \(\mathbb Z[P]\) the free abelian group on \(P\) with the product induced by \(P\). Show that
\(B'=(A\subset\mathbb Z[P])\), where a negative number \(-p\in A\) is sent to the negative of the basis element
\(p\). Show that the ideals of \(B'\) are \(\{0\}\), the sets \((-s,s)\cap\mathbb Q\) for real \(s\) with
\(0<s\le1\), and the sets \([-s,s]\cap\mathbb Q\) for rational \(s\) with \(0<s\le1\). Show that
\(\operatorname{Spec}B'\) has two points, that \(B'\) is local, and that the quotient of \(B'\) by its maximal ideal
is \(\mathbb F_{1^2}\).

(c) Show that the identity of \(A\) is a morphism \(B'\to B\), and describe the map
\(\operatorname{Spec}B\to\operatorname{Spec}B'\).

*Solution.* (a) Every rational number \(x\) is a sum of \(m\) copies of \(x/m\in A\) for large \(m\). So \(A\)
spans \(\mathbb Q\), and \(B\) is a cancellative blueprint with \(B^+=B_{\mathbb Z}=\mathbb Q\). By Proposition
2.4(a) every ideal \(I\) of \(B\) satisfies \(I=A\cap I\mathbb Q\), where \(I\mathbb Q\) is an ideal of the field
\(\mathbb Q\). So \(I=\{0\}\) or \(I=A\). The ideal \(\{0\}\) is prime, because \(A\) has no zero divisors. So
\(\operatorname{Spec}B=\{\{0\}\}\). The units of \(A\) are \(1\) and \(-1\). The set of non-units is
\((-1,1)\cap\mathbb Q\). It is not an ideal. Explicitly, \(1\equiv\tfrac12+\tfrac12\) would force \(1\) to lie in
it. So \(B\) is not local. By Lemma 4.5(c), with \(K=\mathbb Q\), the blueprint \(\Gamma B\) is the subblueprint of
\(\mathbb Q\) on \(A_{\{0\}}=\{as^{-1}:a,s\in A,\ s\neq0\}=\mathbb Q\). So \(\Gamma B=\mathbb Q\neq B\), and \(B\) is
not global. This agrees with Theorem 4.8(a): \(\operatorname{Spec}\mathbb Q\) is also one point.

(b) Define \(\Phi:\mathbb N[A]\to\mathbb Z[P]\) by (U) from the multiplicative map \(p\mapsto p\), \(-p\mapsto-p\),
\(0\mapsto0\), for \(p\in P\). It is surjective, and it sends \(1+(-1)\) to \(0\). Let \(\sim\) be the congruence
generated by the pair \((1+(-1),0)\). Then \(a+(-a)\sim0\) for all \(a\in A\), and \(x\sim y\) implies
\(\Phi(x)=\Phi(y)\). Conversely let \(\Phi(x)=\Phi(y)\). Let \(m_p,m'_p\) be the numbers of terms \(p\) and \(-p\)
in \(x\), and \(n_p,n'_p\) those in \(y\). Then \(m_p-m'_p=n_p-n'_p\) for all \(p\in P\). Adding to \(x\) the terms
\(p+(-p)\), each \(n'_p\) times, and to \(y\) the terms \(p+(-p)\), each \(m'_p\) times, gives the same formal sum.
So \(x\sim y\). Hence \(\mathbb N[A]/{\sim}=\mathbb Z[P]\). The map \(A\to\mathbb Z[P]\) is injective, so
\(B'=(A\subset\mathbb Z[P])\) by Definition 1.3. It is cancellative and with \(-1\), and
\(B'^+=B'_{\mathbb Z}=\mathbb Z[P]\).

A subset \(I\) with (I1) is a monoid ideal of \(A\), and \(I=-I\) because \(-1\in A\). Every such \(I\) satisfies
(I2). Indeed, let \(a+\sum b_j\equiv\sum c_k\) with \(b_j,c_k\in I\) and \(a\neq0\). In \(\mathbb Z[P]\) the element
\(a\) is \(\pm p\) for a basis element \(p\), and \(a=\sum c_k-\sum b_j\) is a combination of the basis elements
\(|b_j|\), \(|c_k|\). So \(p\) is one of them, and \(a\in I\). Hence the ideals of \(B'\) are the monoid ideals of
\(A\). Such an ideal is \(I=\{0\}\cup J\cup(-J)\) with \(J=I\cap P\) and \(PJ\subseteq J\). The condition
\(PJ\subseteq J\) says that \(J\) is closed downwards: if \(q\in J\) and \(q'\in P\) with \(q'\le q\), then
\(q'=(q'/q)q\in J\). Let \(J\neq\emptyset\) and \(s=\sup J\). Then \(J\) contains all rational \(q\) with
\(0 < q < s\), and no \(q > s\). So \(J=(0,s)\cap\mathbb Q\), or \(s\) is rational and
\(J=(0,s]\cap\mathbb Q\). This gives the list. The sets in the list are pairwise different.

The ideal \(\{0\}\) is prime. The ideal \(\mathfrak m=(-1,1)\cap\mathbb Q\) is prime, because its complement
\(\{1,-1\}\) is closed under multiplication. The ideal \([-1,1]\cap\mathbb Q\) is \(B'\). Let \(I\) be one of the
other ideals, with \(s<1\). Since \(s<\sqrt s\), there is a rational \(q\) with \(s<q<\sqrt s\). Then \(q\notin I\)
and \(q^2\in I\). So \(I\) is not prime. Hence \(\operatorname{Spec}B'=\{\{0\},\mathfrak m\}\). The non-units of
\(A\) form the ideal \(\mathfrak m\), so \(B'\) is local. By Proposition 2.4(b), \(B'/\mathfrak m\) is the image of
\(A\) in \(\mathbb Z[P]/\mathfrak m\mathbb Z[P]\). The ideal \(\mathfrak m\mathbb Z[P]\) is spanned by the basis
elements \(p<1\). So the quotient ring is \(\mathbb Z\), the image of \(A\) is \(\{0,1,-1\}\), and
\(B'/\mathfrak m=\mathbb F_{1^2}\).

(c) The relation \(1+(-1)\equiv0\) holds in \(B\). So the identity of \(A\) is a morphism \(B'\to B\) by Lemma
1.4. The induced map sends the point \(\{0\}\) of \(\operatorname{Spec}B\) to the point \(\{0\}\) of
\(\operatorname{Spec}B'\). The closed point \(\mathfrak m\) is not in the image. So the additional relations of
\(B\) remove the closed point: in \(B\) the relation \(1\equiv\tfrac12+\tfrac12\) joins the unit \(1\) to the
elements of \(\mathfrak m\).

*Reference:* [Lorscheid 2012a, Section 1.11]; the lists of ideals in (a) and (b) are stated in
[Lorscheid 2014, Section 4], where \(B'\) serves as the local blueprint at the archimedean place of a
compactification of \(\operatorname{Spec}\mathbb Z\).

**Exercise 3 (a tensor product of cancellative blueprints that is not cancellative).** Let
\(\mathbb Z[\varepsilon]=\mathbb Z[x]/(x^2)\), with \(\varepsilon\) the class of \(x\), and
\[
S=\{n+m\varepsilon:n,m\in\mathbb N,\ m\neq1\}\subseteq\mathbb Z[\varepsilon].
\]

(a) Show that \(S\) is a subsemiring of \(\mathbb Z[\varepsilon]\). So the blueprint \(S=(S\subset S)\) is
cancellative, with \(S_{\mathbb Z}=\mathbb Z[\varepsilon]\). Show that \(\widehat S=S\).

(b) Show that the elements \(2\varepsilon\otimes3\varepsilon\) and \(3\varepsilon\otimes2\varepsilon\) of
\(S\otimes_{\mathbb F_1}S\) are different, and that they have the same image in
\((S\otimes_{\mathbb F_1}S)_{\mathbb Z}\). So \(S\otimes_{\mathbb F_1}S\) is not cancellative.

(c) Deduce that the inverse closure of \(S\otimes_{\mathbb F_1}S\) is not isomorphic to
\(\widehat S\otimes_{\mathbb F_1}\widehat S\).

*Solution.* (a) Let \(M=\mathbb N\setminus\{1\}\). A sum of two elements of \(M\) is \(0\) or at least \(2\), so
\(M\) is closed under addition, and \(nm\in M\) for \(n\in\mathbb N\), \(m\in M\). We have
\((n+m\varepsilon)(n'+m'\varepsilon)=nn'+(nm'+n'm)\varepsilon\) with \(nm'+n'm\in M\). So \(S\) is closed under
sums and products, and it contains \(0\) and \(1\). A subsemiring of a ring is cancellative. The group generated by
\(S\) contains \(\varepsilon=3\varepsilon-2\varepsilon\), so \(S_{\mathbb Z}=\mathbb Z[\varepsilon]\). By Lemma 1.15,
\(S_{\mathrm{inv}}=(S\cup(-S)\subset\mathbb Z[\varepsilon])\). A sum of elements of \(S\) lies in \(S\). So the
elements of \(S_{\mathrm{inv}}\) that are sums of elements of \(S\) are the elements of \(S\), and \(\widehat S\) is
the subblueprint of \(S_{\mathrm{inv}}\) on \(S\), which is \(S\).

(b) We construct a semiring \(D\) and two homomorphisms \(f_1,f_2:S\to D\) with
\(f_1(2\varepsilon)f_2(3\varepsilon)\neq f_1(3\varepsilon)f_2(2\varepsilon)\).

*A monoid \(Q\).* Let \(Q=\mathbb N\sqcup\{6',6''\}\), and let \(\pi:Q\to\mathbb N\) be the identity on
\(\mathbb N\) with \(\pi(6')=\pi(6'')=6\). Define \(x+0=0+x=x\), and \(x+y=\pi(x)+\pi(y)\in\mathbb N\) if \(x\neq0\)
and \(y\neq0\). This addition is commutative with neutral element \(0\). It is associative: a sum of three
elements, in either bracketing, is \(\pi(x)+\pi(y)+\pi(z)\) if all three are non-zero, and it is the sum of the
other two if one of them is \(0\). So \(Q\) is a commutative monoid, written additively, in which \(6'\) and \(6''\)
are two further elements that behave like \(6\) in every sum with a non-zero element. For \(n\in\mathbb N\) and
\(x\in Q\) let \(n\cdot x\) be the sum of \(n\) copies of \(x\). Then \(n\cdot(x+y)=n\cdot x+n\cdot y\),
\((n+n')\cdot x=n\cdot x+n'\cdot x\) and \((nn')\cdot x=n\cdot(n'\cdot x)\), as in every commutative monoid.

*A biadditive map.* Define \(\beta:M\times M\to Q\) by \(\beta(a,b)=ab\), except that \(\beta(2,3)=6'\) and
\(\beta(3,2)=6''\). Then \(\beta(0,b)=0\) and \(\beta(a+a',b)=\beta(a,b)+\beta(a',b)\), and the same in the second
variable. Indeed, this is clear if \(a=0\), \(a'=0\) or \(b=0\). Otherwise \(a,a',b\ge2\), so \(a+a'\ge4\) and
\(\beta(a+a',b)=(a+a')b\), while \(\beta(a,b)\) and \(\beta(a',b)\) are non-zero, so their sum is
\(\pi(\beta(a,b))+\pi(\beta(a',b))=ab+a'b\). The point is that \(2\) and \(3\) are not sums of two non-zero
elements of \(M\). It follows that \(\beta(na,b)=n\cdot\beta(a,b)=\beta(a,nb)\) for \(n\in\mathbb N\).

*The semiring \(D\).* Let \(D=\mathbb N\times M\times M\times Q\), with componentwise addition and with the product
\[
(n,a,b,p)(n',a',b',p')=\bigl(nn',\ na'+n'a,\ nb'+n'b,\ n\cdot p'+n'\cdot p+\beta(a,b')+\beta(a',b)\bigr).
\]
The product is commutative, \((1,0,0,0)\) is a unit, and \((0,0,0,0)\) is absorbing. The product is additive in
each factor, because each component is: for the last one this uses the rules for \(n\cdot x\) and the biadditivity
of \(\beta\). The product is associative. For the first three components this is the associativity in
\(\mathbb N[\varepsilon_1,\varepsilon_2]/(\varepsilon_1^2,\varepsilon_2^2,\varepsilon_1\varepsilon_2)\). For three
elements \(x_i=(n_i,a_i,b_i,p_i)\), \(i=1,2,3\), the last component of \((x_1x_2)x_3\) is, by the same rules,
\[
\sum_{\{i,j,k\}=\{1,2,3\}}n_in_j\cdot p_k\;+\;\sum_{(i,j,k)}n_k\cdot\beta(a_i,b_j),
\]
where the first sum has three terms, one for each \(k\), and the second sum runs over the six orderings
\((i,j,k)\) of \(1,2,3\). This expression does not change when the three elements are permuted. Since the product is
commutative, \((x_1x_2)x_3=(x_2x_3)x_1=x_1(x_2x_3)\). So \(D\) is a semiring.

*The homomorphisms.* Put \(f_1(n+m\varepsilon)=(n,m,0,0)\) and \(f_2(n+m\varepsilon)=(n,0,m,0)\). Both maps are
additive and send \(1\) to the unit. They are multiplicative:
\((n,m,0,0)(n',m',0,0)=(nn',nm'+n'm,0,\beta(m,0)+\beta(m',0))=(nn',nm'+n'm,0,0)\), and in the same way for \(f_2\).
So \(f_1\) and \(f_2\) are semiring homomorphisms, that is, morphisms of blueprints \(S\to D\). By Proposition
1.14(a) there is a morphism \(g:S\otimes_{\mathbb F_1}S\to D\) with \(g(s\otimes t)=f_1(s)f_2(t)\). We get
\[
g(2\varepsilon\otimes3\varepsilon)=(0,2,0,0)(0,0,3,0)=(0,0,0,6'),\qquad
g(3\varepsilon\otimes2\varepsilon)=(0,3,0,0)(0,0,2,0)=(0,0,0,6'').
\]
These are different. So \(2\varepsilon\otimes3\varepsilon\neq3\varepsilon\otimes2\varepsilon\) in
\(S\otimes_{\mathbb F_1}S\).

By Proposition 1.14(b),
\((S\otimes_{\mathbb F_1}S)_{\mathbb Z}=\mathbb Z[\varepsilon]\otimes_{\mathbb Z}\mathbb Z[\varepsilon]\). There both
elements become \(6(\varepsilon\otimes\varepsilon)\). The monoid of a blueprint is a subset of its semiring. So the
map \((S\otimes_{\mathbb F_1}S)^+\to(S\otimes_{\mathbb F_1}S)_{\mathbb Z}\) is not injective, and
\(S\otimes_{\mathbb F_1}S\) is not cancellative.

(c) By (a), \(\widehat S\otimes_{\mathbb F_1}\widehat S=S\otimes_{\mathbb F_1}S\), which is not cancellative. The
inverse closure of any blueprint \(C\) is a subblueprint of \(C_{\mathrm{inv}}\), which is a monoid inside the ring
\(C_{\mathbb Z}\). So it is cancellative. A blueprint that is isomorphic to a cancellative blueprint is
cancellative. Hence the two blueprints are not isomorphic.

**Exercise 4 (the line with three marked points).** Let \(R=\mathbb Z[x_0,x_1,x_2]/(x_0+x_1-x_2)\),
\(B=\mathbb F_1\langle x_0,x_1,x_2\rangle\subseteq R\) and \(L=\operatorname{Proj}B\), as in Example 5.6. Write
\(0\), \(1\), \(\infty\) for the closed points \(x_0=0\), \(x_1=0\), \(x_2=0\) of \(L\).

(a) Show that \(B=\mathbb F_1[x_0,x_1,x_2]/\!\!/\langle x_0+x_1\equiv x_2\rangle\).

(b) Show that \(D_+(x_2)\) is the spectrum of \(\mathbb F_1\langle u,1-u\rangle\subseteq\mathbb Z[u]\), where
\(u=x_0/x_2\). Show that the residue fields of \(L\) at \(0\), \(1\) and \(\infty\) are \(\mathbb F_1\),
\(\mathbb F_1\) and \(\mathbb F_{1^2}\).

(c) For a blue field \(C\) let \(L(C)\) be the set of morphisms \(\operatorname{Spec}C\to L\). Show that
\(L(\mathbb F_1)\) has two elements and \(L(\mathbb F_{1^2})\) has three.

(d) Show that every automorphism of the blue scheme \(L\) fixes the point \(\infty\). Show that
\(\operatorname{Proj}B_{\mathrm{inv}}\) has an automorphism that exchanges \(0\) and \(\infty\).

*Solution.* (a) The substitution \(x_2\mapsto x_0+x_1\) identifies \(R\) with \(\mathbb Z[x_0,x_1]\). The monomial
\(x_0^ix_1^jx_2^k\) becomes \(x_0^ix_1^j(x_0+x_1)^k\). This polynomial is not zero. Its terms with the smallest
exponent of \(x_0\) have exponent \(i\), those with the smallest exponent of \(x_1\) have exponent \(j\), and its
degree is \(i+j+k\). So different monomials are different elements of \(R\), and the underlying monoid of \(B\) is
the free monoid \(\mathbb F_1[x_0,x_1,x_2]\). Let \(\sim\) be the congruence on the formal sums of monomials that is
generated by the pair \((x_2,\ x_0+x_1)\). The relation \(x_2\equiv x_0+x_1\) holds in \(B\), so \(y\sim y'\)
implies \(y\equiv y'\). For a formal sum \(y\) let \(\rho(y)\) be the formal sum of monomials in \(x_0,x_1\)
obtained by replacing \(x_2\) by \(x_0+x_1\) and multiplying out. Then \(y\sim\rho(y)\), because a congruence is
compatible with products. If \(y\equiv y'\), then \(\rho(y)\) and \(\rho(y')\) have the same image in
\(\mathbb Z[x_0,x_1]\), where the monomials in \(x_0,x_1\) are a basis. So \(\rho(y)=\rho(y')\), and
\(y\sim\rho(y)=\rho(y')\sim y'\).

(b) By Theorem 5.3, \(D_+(x_2)\cong\operatorname{Spec}B_{(x_2)}\). By Proposition 2.6, \(B_{x_2}\) is the monoid of
the fractions \(m/x_2^k\), \(m\) a monomial, inside the ring \(R_{x_2}\). The fractions of degree \(0\) are the
products of powers of \(u=x_0/x_2\) and \(v=x_1/x_2\), and they lie in the ring of elements of degree \(0\) of
\(R_{x_2}\), which is \(\mathbb Z[u,v]/(u+v-1)=\mathbb Z[u]\). So
\(B_{(x_2)}=\mathbb F_1\langle u,v\rangle\) with \(v=1-u\). By Corollary 3.4 its points are the zero patterns of
\((u,1-u)\): the generic point, the point \(u=0\), which is \(0\), and the point \(v=0\), which is \(1\). In the
same way \(D_+(x_0)\) is the spectrum of \(\mathbb F_1\langle u',z\rangle\subseteq\mathbb Z[u']\) with
\(u'=x_1/x_0\) and \(z=x_2/x_0=1+u'\), and its closed points are \(u'=0\), which is \(1\), and \(z=0\), which is
\(\infty\).

We compute residue fields with Propositions 2.6 and 2.4(b): for a cancellative blueprint with monoid \(A'\) and
ring \(R'\), and a prime ideal \(\mathfrak p\) with complement \(S'\), the residue field is the image of
\(S'^{-1}A'\) in the ring \(S'^{-1}R'/\mathfrak pS'^{-1}R'\), together with the semiring of sums of elements of this
image. At the point \(u=0\) of \(D_+(x_2)\) we have \(S'=\{v^j\}\), and the ring is
\(\mathbb Z[u,(1-u)^{-1}]/(u)=\mathbb Z\), with \(u\mapsto0\) and \(v\mapsto1\). The image of the monoid is
\(\{0,1\}\), and its sums form \(\mathbb N\). So the residue field at \(0\) is \(\mathbb F_1\). By the symmetry
that exchanges \(x_0\) and \(x_1\), the residue field at \(1\) is \(\mathbb F_1\). At the point \(z=0\) of
\(D_+(x_0)\) we have \(S'=\{u'^j\}\), and the ring is \(\mathbb Z[u'^{\pm1}]/(1+u')=\mathbb Z\), with
\(u'\mapsto-1\). The image of the monoid is \(\{0,1,-1\}\), and its sums form \(\mathbb Z\). So the residue field at
\(\infty\) is \(\mathbb F_{1^2}\).

(c) Let \(C\) be a blue field. We show that \(L(C)\) is the disjoint union, over the points \(x\) of \(L\), of the
sets \(\operatorname{Hom}(\kappa(x),C)\). A morphism \(\varphi:\operatorname{Spec}C\to L\) has one point \(x\) in
its image. Choose an affine open neighbourhood \(\operatorname{Spec}B'\) of \(x\), and let \(\mathfrak p\) be the
prime ideal of \(B'\) that corresponds to \(x\). Then \(\varphi\) is a morphism to \(\operatorname{Spec}B'\). Since
\(C\) is global (Proposition 4.7), \(\varphi=f^{\ast}\) for one morphism \(f:B'\to C\) with
\(f^{-1}(0)=\mathfrak p\) (Theorem 4.8(b)). The elements outside \(\mathfrak p\) go to non-zero elements of \(C\),
which are units. So \(f\) factors in exactly one way through \(B'_{\mathfrak p}\) (Proposition 2.6(b)) and then
through \(\kappa(\mathfrak p)=B'_{\mathfrak p}/\mathfrak pB'_{\mathfrak p}\) (Proposition 2.3(b)). Conversely every
morphism \(\kappa(\mathfrak p)\to C\) gives such an \(f\). The residue field does not depend on the choice of the
affine neighbourhood, because it is the quotient of the stalk of \(L\) at \(x\) by its maximal ideal.

The residue field at the generic point \(\eta\) of \(L\) is the localization of \(\mathbb F_1\langle u,v\rangle\) at
all non-zero elements. In it \(u\) and \(v\) are units with \(u+v\equiv1\). A morphism from it to
\(C=\mathbb F_1\) or \(C=\mathbb F_{1^2}\) would give units \(\alpha,\beta\in\{1,-1\}\) with \(\alpha+\beta=1\) in
\(\mathbb Z\). There are none. For every blueprint \(C\) there is one morphism \(\mathbb F_1\to C\). There is no
morphism \(\mathbb F_{1^2}\to\mathbb F_1\), and one morphism \(\mathbb F_{1^2}\to\mathbb F_{1^2}\) (Lemma 1.6). With
(b) we get
\[
\lvert L(\mathbb F_1)\rvert=0+1+1+0=2,\qquad\lvert L(\mathbb F_{1^2})\rvert=0+1+1+1=3,
\]
where the four terms belong to \(\eta\), \(0\), \(1\), \(\infty\). For comparison, the monoid scheme
\(\mathbb P^1_{\mathbb F_1}\) has the residue fields \(\mathbb F_1[T^{\pm1}]\), \(\mathbb F_1\), \(\mathbb F_1\). So
it has \(1+1+1=3\) points with values in \(\mathbb F_1\) and \(2+1+1=4\) with values in \(\mathbb F_{1^2}\).

(d) An automorphism \(\theta\) of \(L\) is a homeomorphism, so it permutes the closed points. It induces
isomorphisms between the stalks at \(\theta(x)\) and at \(x\), which send non-units to non-units in both
directions. So it induces isomorphisms between the residue fields at \(\theta(x)\) and at \(x\). By (b) the residue
field at \(\infty\) has three elements and the residue fields at \(0\) and \(1\) have two. So
\(\theta(\infty)=\infty\).

The blueprint \(B_{\mathrm{inv}}\) is the monoid of the elements \(\pm m\), \(m\) a monomial, inside \(R\) (Lemma
1.15). It is a graded blueprint: its elements are homogeneous elements of the graded ring \(R\), and its relations
are homogeneous because \(R\) is the direct sum of its homogeneous parts. By Corollary 3.4, applied to the
generators \(-1,x_0,x_1,x_2\) of \(R\), its prime ideals are given by the same zero patterns as those of \(B\). So
\(\operatorname{Proj}B_{\mathrm{inv}}\) has again the four points \(\eta,0,1,\infty\). The automorphism of
\(\mathbb Z[x_0,x_1,x_2]\) with \(x_0\mapsto x_2\), \(x_1\mapsto-x_1\), \(x_2\mapsto x_0\) sends
\(x_0+x_1-x_2\) to \(-(x_0+x_1-x_2)\). So it induces an automorphism \(\tau\) of the graded ring \(R\). It maps the
monoid of \(B_{\mathrm{inv}}\) to itself. So it is an automorphism of the graded blueprint \(B_{\mathrm{inv}}\)
(Proposition 1.2(c)), and \(\mathfrak p\mapsto\tau^{-1}(\mathfrak p)\) is an automorphism of
\(\operatorname{Proj}B_{\mathrm{inv}}\). A prime ideal that contains \(x_2=\tau(x_0)\) is mapped to one that
contains \(x_0\), and conversely. So this automorphism exchanges \(0\) and \(\infty\), and it fixes \(1\). In the
coordinate \(u\) it is \(u\mapsto1/u\). It does not come from an automorphism of \(L\): it needs \(-1\).

**Exercise 5 (the upper triangular matrices in \(\mathrm{SL}_2\)).** Let
\(\mathcal B\subseteq\mathrm{SL}_{2,\mathbb Z}\) be the closed subgroup scheme \(c=0\) of upper triangular
matrices. Its coordinate ring is
\(R_1/(c)=\mathbb Z[a^{\pm1},b]\), with \(d=a^{-1}\). Let \(P=\mathbb F_1\langle a,b,c,d\rangle\) be the blueprint
generated in this ring by the classes of the four coordinates, and \(H=\operatorname{Spec}P\).

(a) Show that \(P\) is the monoid \(\mathbb F_1[a^{\pm1},b]\) of the monomials \(a^ib^j\) with \(i\in\mathbb Z\),
\(j\ge0\). Show that \(H\) has two points, and determine their images under the morphism \(H\to G\) given by the
quotient map \(R_1\to R_1/(c)\).

(b) For \(n\ge1\) let \(H^n\) be the \(n\)-fold product of \(H\) as a blue scheme. Show that
\(\operatorname{rk}H^n=n\), that \(\mathcal Z(H^n)\) is the closed point, and that
\((H^n)^{\mathrm{rk}}=\operatorname{Spec}\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\). Deduce that \(H^n\) is the
\(n\)-fold product of \(H\) in the Tits category.

(c) Show that the group law of \(\mathcal B\) is not the base extension of a morphism of blue schemes
\(H\times H\to H\), that it defines a Tits morphism \(\mu\), and that \((H,\mu)\) is a Tits–Weyl model of
\(\mathcal B\). Determine \(\mathcal W(H)\), \(H^{\mathcal T}(\mathbb F_1)\) and
\(H^{\mathcal T}(\mathbb F_{1^2})\).

*Solution.* (a) The classes of \(a,b,c,d\) in \(\mathbb Z[a^{\pm1},b]\) are \(a\), \(b\), \(0\), \(a^{-1}\). Their
products are \(0\) and the monomials \(a^ib^j\) with \(i\in\mathbb Z\), \(j\ge0\). These monomials are linearly
independent. So two formal sums of them have the same image in the ring only if they are equal. Hence the
pre-addition of \(P\) is the equality relation, and \(P\) is the monoid \(\mathbb F_1[a^{\pm1},b]\) (Example
1.5(a)). A point of \(\mathcal B\) with values in a field has \(a\neq0\), \(d\neq0\), \(c=0\), and \(b\) is zero or
not. By Corollary 3.4 the prime ideals of \(P\) are \(\{0\}\), for the zero pattern \(\{c\}\), and the ideal
\((b)\) of the monomials with \(j\ge1\), for the zero pattern \(\{b,c\}\). The morphism \(B_1\to P\) is the
restriction of \(R_1\to R_1/(c)\) (Proposition 1.2(c)). The preimage of \(\{0\}\) is the set of monomials of \(B_1\)
that are divisible by \(c\), together with \(0\). This is the point \((c)\) of \(G\). The preimage of \((b)\) is the
point \((b,c)=e\).

(b) By (a), Definition 1.13 and Theorem 4.8(d), \(H^n\) is the spectrum of the monoid \(P_n\) of the monomials in
\(a_1^{\pm1},\dots,a_n^{\pm1},b_1,\dots,b_n\). It lies in the field \(\mathbb Q(a_i,b_i)\), so \(H^n\) is connected
(Lemma 4.5(b)). Its prime ideals are the ideals \(\mathfrak p_I\) generated by the \(b_i\) with \(i\in I\), for
the subsets \(I\) of \(\{1,\dots,n\}\). By Proposition 2.4(b), \(P_n/\mathfrak p_I\) is the monoid of the monomials
in the \(a_i^{\pm1}\) and the \(b_j\) with \(j\notin I\). The ring
\(\mathbb Q[a_i^{\pm1},b_j:j\notin I]\) has dimension \(2n-|I|\): it is a localization of a polynomial ring in
\(2n-|I|\) variables [Stacks, Tag [00OP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dim-affine-space)], and the ideals generated by the first \(r\) elements of the list
\(a_1-1,\dots,a_n-1\), \(b_j\) (\(j\notin I\)), for \(0\le r\le2n-|I|\), form a chain of prime ideals. So the
rank of \(\mathfrak p_I\) is \(2n-|I|\). The smallest rank is \(n\), and it is attained only at the closed point
\(x\), where \(I=\{1,\dots,n\}\) and the quotient is \(\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\), with \(t_i\) the
class of \(a_i\). This point is pseudo-Hopf by Example 6.7(a); for (PH1) use the morphisms \(a_i\mapsto1\),
\(b_i\mapsto0\) to fields. By Lemma 6.8 and Example 6.7(a), \(\operatorname{rk}H^n=n\),
\(\mathcal Z(H^n)=\{x\}\) and \((H^n)^{\mathrm{rk}}=\operatorname{Spec}\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\).
Its base extension to \(\mathbb Z\) is the torus \(T^n\) of diagonal matrices in \(\mathcal B^n\), and
\(\rho_{H^n,\mathbb Z}\) is its inclusion.

Let \(n=n'+n''\). The projection \(H^n\to H^{n'}\) is given by the inclusion \(P_{n'}\subseteq P_n\). On rank
spaces take the morphism given by the inclusion of \(\mathbb F_1[t_1^{\pm1},\dots,t_{n'}^{\pm1}]\) into
\(\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\). The square of Definition 6.9 commutes, as in the proof of Proposition
7.1(d). The monoid \(\mathbb F_1[t_1^{\pm1},\dots,t_n^{\pm1}]\) is the tensor product of the monoids for \(n'\) and
\(n''\). So the hypotheses of Lemma 6.11 hold, and \(H^n\) is the product of \(H^{n'}\) and \(H^{n''}\) in the Tits
category.

(c) The product of two matrices in \(\mathcal B\) is
\[
\begin{pmatrix}a_1&b_1\\0&a_1^{-1}\end{pmatrix}\begin{pmatrix}a_2&b_2\\0&a_2^{-1}\end{pmatrix}
=\begin{pmatrix}a_1a_2&a_1b_2+b_1a_2^{-1}\\0&(a_1a_2)^{-1}\end{pmatrix}.
\]
So the comultiplication \(\mathbb Z[a^{\pm1},b]\to\mathbb Z[a_1^{\pm1},b_1,a_2^{\pm1},b_2]\) sends \(a\) to
\(a_1a_2\) and \(b\) to \(a_1b_2+b_1a_2^{-1}\). The image of \(b\) is a sum of two different monomials. It is not an
element of the monoid \(P_2\), because the monomials are linearly independent. The monoid \(P_2\) is global
(Proposition 4.7). So by Theorem 4.8(b) the group law is not the base extension of a morphism of blue schemes
\(H\times H\to H\).

The comultiplication maps \(P^+=\mathbb N[a^{\pm1},b]\) into \(P_2^+=\mathbb N[a_1^{\pm1},b_1,a_2^{\pm1},b_2]\).
As in Theorem 7.2(a) its restriction defines a monoid law \(\mu^+\) on \(H^+\), with the unit \(a\mapsto1\),
\(b\mapsto0\). On \(H^{\mathrm{rk}}=\operatorname{Spec}\mathbb F_1[t^{\pm1}]\) let \(\mu^{\mathrm{rk}}\) be given by
\(t\mapsto t_1t_2\) and \(\epsilon^{\mathrm{rk}}\) by \(t\mapsto1\). This is a group law, with inverse
\(t\mapsto t^{-1}\), and its base extension is the group law of the diagonal torus \(T\). The square of Definition
6.9 for \(\mu=(\mu^{\mathrm{rk}},\mu^+)\) consists of the products of \(T\) and of \(\mathcal B\) and of the
inclusions \(T\times T\subseteq\mathcal B\times\mathcal B\) and \(T\subseteq\mathcal B\). It commutes. With (b) and
the argument of Theorem 7.2(c), \((H,\mu,\epsilon)\) is a Tits monoid, and a Tits model of \(\mathcal B\). Its Weyl
kernel is \(H^{\mathrm{rk}}\), and its canonical torus is \(T\).

For \(g\in\mathcal B(k)\) and \(\tau\in T(k')\) the formula in the proof of Theorem 7.2(d), with \(c=0\) and
\(d=a^{-1}\), gives
\[
g\tau g^{-1}=\begin{pmatrix}s&ab(s^{-1}-s)\\0&s^{-1}\end{pmatrix}.
\]
For \(\tau=\tau_1\) this is diagonal only if \(ab=0\), that is, \(b=0\), because \(a\) is a unit. So the normalizer
of \(T\) in \(\mathcal B\) is \(T\). The centralizer of \(T\) contains \(T\) and lies in the normalizer, so it is
\(T\) as well. As in Theorem 7.2(d), \(T\) is a maximal torus of \(\mathcal B\). The group scheme
\(\mathcal W(T)=N(T)/C(T)\) is trivial, and \(\Psi_{\mathfrak e}\) is the identity of the trivial group scheme
\(T/T\). So \(H\) is a Tits–Weyl model of \(\mathcal B\).

The Weyl monoid \(\mathcal W(H)\) has one element. As in the proof of Corollary 7.3, a Tits point of \(H\) with
values in \(C=\mathbb F_1\) or \(C=\mathbb F_{1^2}\) is a morphism \(f:\mathbb F_1[t^{\pm1}]\to C\); the condition
on the entries holds, because the diagonal matrix with entries \(f(t),f(t)^{-1}\) has entries in \(C\). So
\(H^{\mathcal T}(\mathbb F_1)\) is trivial, and \(H^{\mathcal T}(\mathbb F_{1^2})\) has the two elements
\(t\mapsto\pm1\). It is the group \(T(\mathbb Z)=\{\pm1\}\).

By (a) the inclusion \(H\to G\) maps \(\mathcal Z(H)\) to the point \(e\) of \(\mathcal Z(G)\), and the two rank
spaces have the same component \(\operatorname{Spec}\mathbb F_1[t^{\pm1}]\) at this point. So \(\mathcal W(H)\) is
the trivial subgroup \(\{e\}\) of \(\mathcal W(G)=\{e,w\}\): the Weyl group of the Borel subgroup is the trivial
subgroup of the Weyl group of \(\mathrm{SL}_2\). This is an instance of [Lorscheid 2018a, Theorem 5.2].

**Exercise 6 (the rank space of a product).** Let \(\mathbb Z[\varepsilon]=\mathbb Z[x]/(x^2)\) as in Exercise 3,
and let \(\theta=1+\varepsilon\), so that \(\theta^k=1+k\varepsilon\) for all \(k\in\mathbb Z\). Let
\(F=\mathbb F_1\langle\theta,\theta^{-1}\rangle\subseteq\mathbb Z[\varepsilon]\) be the blueprint generated by
\(\theta\) and \(\theta^{-1}\) (Example 1.11(a)), and \(X=\operatorname{Spec}F\).

(a) Show that \(\sum_{i=1}^m\theta^{k_i}\equiv\sum_{j=1}^{m'}\theta^{l_j}\) in \(F\) if and only if \(m=m'\) and
\(\sum_ik_i=\sum_jl_j\). Show that \(F\) is a blue field, that its point is pseudo-Hopf of rank \(0\), and that
\(X^{\mathrm{rk}}=X\).

(b) Put \(C=F\otimes_{\mathbb F_1}F\) and \([k,l]=\theta^k\otimes\theta^l\). Show that \([0,0]+[3,3]\) and
\([6,2]+[-3,1]\) are different elements of \(C^+\) with the same image in \(C_{\mathbb Z}\). So \(C\) is not
cancellative.

(c) Show that \(X\times X\) has one point \(z\), that \(z\) is pseudo-Hopf of rank \(0\), and that
\((X\times X)^{\mathrm{rk}}\) is not isomorphic to \(X^{\mathrm{rk}}\times X^{\mathrm{rk}}\).

(d) Show that \(X\times X\), with its two projections, is a product of \(X\) with itself in the Tits category.

*Solution.* (a) The monoid of \(F\) consists of \(0\) and the elements \(\theta^k\). In \(\mathbb Z[\varepsilon]\)
we have \(\sum_{i=1}^m\theta^{k_i}=m+(\sum_ik_i)\varepsilon\), and \(1,\varepsilon\) is a basis of
\(\mathbb Z[\varepsilon]\). This gives the relations. Every non-zero element of \(F\) is a unit, so \(F\) is a blue
field, and \(X\) is one point \(x=\{0\}\) with \(D_x=F\). Since \(\varepsilon=\theta-1\), the ring of \(F\) is
\(\mathbb Z[\varepsilon]\). For every field \(L\) the ring homomorphism \(\mathbb Z[\varepsilon]\to L\) with
\(\varepsilon\mapsto0\) gives a morphism \(F\to L\) that sends every \(\theta^k\) to \(1\), by (1.2); the preimage
of \(0\) is \(\{0\}\). This is (PH1). By Lemma 1.15, \(F_{\mathrm{inv}}\) is the monoid of the elements \(0\) and
\(\pm\theta^k\) inside \(\mathbb Z[\varepsilon]\). Its units \(\pm\theta^k\) generate the group
\(\mathbb Z[\varepsilon]\), which is free. This is (PH2) and (PH3). The ring \(\mathbb Q[\varepsilon]\) has the
single prime ideal \((\varepsilon)\), because \(\varepsilon\) is nilpotent. So the rank of \(x\) is \(0\). An
element \(-\theta^k=-1-k\varepsilon\) is not a sum of elements \(\theta^l\), because such a sum has a constant term
\(\ge0\). So \(\widehat F\) is the subblueprint of \(F_{\mathrm{inv}}\) on the monoid of \(F\), which is \(F\). Its
unit field is \(F\). Hence \(K_x=F\) and \(X^{\mathrm{rk}}=X\).

(b) By Definition 1.13 and the description of steps in Section 1.2, a step in \(C\) replaces a part
\(\sum_i[k_i,l]\) of a formal sum by \(\sum_j[k'_j,l]\), where \(\sum_i\theta^{k_i}\equiv\sum_j\theta^{k'_j}\) is a
relation of \(F\), or it does the same with the two entries exchanged. By (a) a relation of \(F\) with at most one
term on one side is an equality of formal sums. In \([0,0]+[3,3]\) the two terms have different first entries and
different second entries. So no step changes this formal sum, and it is congruent only to itself. In particular it
is different from \([6,2]+[-3,1]\) in \(C^+\). By Proposition 1.14(b),
\(C_{\mathbb Z}=\mathbb Z[\varepsilon_1,\varepsilon_2]/(\varepsilon_1^2,\varepsilon_2^2)\), and the image of
\([k,l]\) is \((1+k\varepsilon_1)(1+l\varepsilon_2)\). Both formal sums have the image
\(2+3\varepsilon_1+3\varepsilon_2+9\varepsilon_1\varepsilon_2\).

(c) By Theorem 4.8(d), \(X\times X=\operatorname{Spec}C\). The elements \([k,l]\) have different images in
\(C_{\mathbb Z}\), so the monoid of \(C\) consists of \(0\) and the elements \([k,l]\), which are units. So \(C\) is
a blue field, and \(X\times X\) is one point \(z=\{0\}\) with \(D_z=C\). The arguments of (a) apply to \(z\). For a
field \(L\), the morphism \(C\to L\) with \(\varepsilon_1,\varepsilon_2\mapsto0\) gives (PH1). The units
\(\pm(1+k\varepsilon_1)(1+l\varepsilon_2)\) of \(C_{\mathrm{inv}}\) generate the group \(C_{\mathbb Z}\), which is
free with the basis \(1,\varepsilon_1,\varepsilon_2,\varepsilon_1\varepsilon_2\). The ring
\(C_{\mathbb Z}\otimes\mathbb Q\) has the single prime ideal \((\varepsilon_1,\varepsilon_2)\). So \(z\) is
pseudo-Hopf of rank \(0\), and \((X\times X)^{\mathrm{rk}}=\operatorname{Spec}K_z\). As in (a), the inverse closure
of \(C\) is the subblueprint of \(C_{\mathrm{inv}}\) on the image of the monoid of \(C\), and it is its own unit
field. So \(K_z\) has the monoid of \(C\), and its relations are the equalities that hold in the ring
\(C_{\mathbb Z}\). Hence \(K_z\) is cancellative. By (a), \(X^{\mathrm{rk}}\times X^{\mathrm{rk}}=X\times X\) is the
spectrum of \(C\), which is not cancellative by (b). Blue fields are global (Proposition 4.7). So by Theorem
4.8(b) an isomorphism between \(\operatorname{Spec}K_z\) and \(\operatorname{Spec}C\) would be given by an
isomorphism of blueprints between \(K_z\) and \(C\). There is none.

(d) The identity on the monoid is a morphism \(c:C\to K_z\). The two projections \(q_i:X\times X\to X\) are given
by the morphisms \(\theta^k\mapsto[k,0]\) and \(\theta^k\mapsto[0,k]\) from \(F\) to \(C\). Their composites with
\(c\) give morphisms \(q_i^{\mathrm{rk}}:\operatorname{Spec}K_z\to\operatorname{Spec}F\). The square of Definition
6.9 for \((q_i^{\mathrm{rk}},q_i^+)\) commutes, because \(K_z\) and \(C\) have the same ring and
\(\rho_{X\times X,\mathbb Z}\) and \(\rho_{X,\mathbb Z}\) are identities. So the projections are Tits morphisms
\(p_i\). Let \(Y\) be an affine blue scheme and \(\varphi_1,\varphi_2:Y\to X\) Tits morphisms. As in the proof of
Lemma 6.11 there is exactly one \(\varphi^+:Y^+\to(X\times X)^+\) with \(q_i^+\varphi^+=\varphi_i^+\). The rank
space \(Y^{\mathrm{rk}}\) is a disjoint union of spectra of blue fields \(K_y\), and each \(K_y\) is contained in a
ring (Lemma 6.6). On \(\operatorname{Spec}K_y\) the morphisms \(\varphi_1^{\mathrm{rk}}\) and
\(\varphi_2^{\mathrm{rk}}\) are given by two morphisms \(F\to K_y\) (Theorem 4.8(b)), that is, by one morphism
\(f:C\to K_y\) (Proposition 1.14(a)). The homomorphism \(f^+\), followed by the inclusion of \(K_y^+\) into a ring,
factors through \(C_{\mathbb Z}\). So \(f\) preserves all equalities that hold in \(C_{\mathbb Z}\), and \(f=f'c\)
for exactly one morphism \(f':K_z\to K_y\). Hence there is exactly one morphism
\(\varphi^{\mathrm{rk}}:Y^{\mathrm{rk}}\to(X\times X)^{\mathrm{rk}}\) with
\(q_i^{\mathrm{rk}}\varphi^{\mathrm{rk}}=\varphi_i^{\mathrm{rk}}\). The rest of the proof of Lemma 6.11 applies
without change. So hypothesis (ii) of Lemma 6.11 is sufficient and not necessary.

Compare the remark after Definition 6.13 and question (f) of Section 8.3.

## What this lesson does not prove

The following statements are used or quoted without proof.

1. **Theorem 4.8(a) and (c), and fibre products.** The global sections of an affine blue scheme; the fact that
   morphisms of blue schemes are locally given by morphisms of blueprints; fibre products of blue schemes other
   than products of affine blue schemes. *Reference:* [Lorscheid 2012a, Theorem 3.12, Theorem 3.23, Corollary 3.26
   and Proposition 3.27]; see the remark after Theorem 4.8 for blueprints that are not cancellative. The lesson
   proves part (b) and the products of affine blue schemes in part (d), and it uses only these in Sections 6, 7
   and 9.
2. **Base extension of blue schemes that are not affine** (Section 4.4): the gluing of \(X^+\) and
   \(X_{\mathbb Z}\) and their universal properties. *Reference:* [Lorscheid 2012a, Proposition 3.31 and Section
   3.8]; [Lorscheid 2018a, Section 1.1]. The lesson proves the affine case and uses the general case only in
   Section 5, for the base extension of \(\operatorname{Proj}\).
3. **\(\operatorname{Proj}\) for graded blueprints with elements that are not homogeneous.** *Reference:*
   [López Peña–Lorscheid 2012, Section 2 and Theorem 2.1]. The lesson proves the case in which every element is
   homogeneous (Theorem 5.3).
4. **The Tits category of all blue schemes and its products.** *Reference:* [Lorscheid 2018a, Proposition 3.3,
   Theorem 3.5 and Theorem 3.8]; see the remark after Definition 6.13 and question (f) of Section 8.3. The lesson
   proves what it needs in Lemma 6.11, Lemma 6.12, Proposition 7.1 and Exercise 5.
5. **The general facts behind Definition 6.14.** That \(\mu^{\mathrm{rk}}\) restricts to a commutative group law
   on the Weyl kernel and that \(\mathfrak e_{\mathbb Z}\) is diagonalizable: [Lorscheid 2018a, Lemmas 3.11 and
   3.12]. That centralizers and normalizers of tori are group schemes and that their quotient exists:
   [SGA3 II], as cited in [Lorscheid 2018a, Section 3.3], where no exact locator is given. For \(\mathrm{SL}_2\) and
   its upper triangular subgroup the lesson computes these objects directly.
6. **Theorem 6.15(a):** [Lorscheid 2018a, Theorem 3.14]. The lesson verifies the four conclusions for
   \(\mathrm{SL}_2\) (Corollary 7.3).
7. **Theorem 6.15(b) for \(n\ge3\):** [Lorscheid 2018a, Proposition 4.1 and Theorem 4.2]. The lesson proves the
   case \(n=2\) (Theorem 7.2 and Corollary 7.3) and, for all \(n\), the description of the points (Example 8.1)
   and the last sentence of (b) (Example 8.2). For the existence of \(\mu^+\) see Section 8.2, item 2.
8. **Theorem 6.15(c) and (d):** [Lorscheid 2018a, Theorem 4.7, Section 4.3, Theorem 4.9, Lemma 4.10, Proposition
   4.11 and Theorem 4.12]. These proofs build on (b); see Section 8.2, items 3 and 4.
9. **The statements quoted in Section 8:** [Lorscheid 2018a, Theorems 5.2 and 5.7, Proposition 5.5];
   [Lorscheid 2016, Theorem 2.5 and Section 3], which are stated there without proofs;
   [Lorscheid–Thas 2023, Theorems 1.1, 1.2 and 5.14]; [Baker–Jin–Lorscheid 2024, Section 3.4].
10. **Four facts of commutative algebra:** the minimal polynomial over \(\mathbb Q\) of an algebraic integer has
    integer coefficients [Stacks, Tag [00H7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-minimal-polynomial-normal-domain)]; the polynomial ring in \(r\) variables over a field has dimension
    \(r\) [Stacks, Tag [00OP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dim-affine-space)]; every non-zero ring has a prime ideal [Stacks, Tag [00E0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Zariski-topology)]; a module over
    \(\mathbb Z\) is flat if and only if it is torsion-free [Stacks, Tag [0AUW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dedekind-torsion-free-flat)].

## References

Result numbers in the works of O. Lorscheid and coauthors refer to the arXiv versions.

- [Baker–Jin–Lorscheid 2024] M. Baker, T. Jin, O. Lorscheid, *New building blocks for \(\mathbb F_1\)-geometry:
  bands and band schemes*, [arXiv:2402.09612](https://arxiv.org/pdf/2402.09612).
- [López Peña–Lorscheid 2012] J. López Peña, O. Lorscheid, *Projective geometry for blueprints*, [arXiv:1203.1665](https://arxiv.org/pdf/1203.1665).
- [Lorscheid 2012a] O. Lorscheid, *The geometry of blueprints. Part I: Algebraic background and scheme theory*,
  [arXiv:1103.1745](https://arxiv.org/pdf/1103.1745).
- [Lorscheid 2012b] O. Lorscheid, *Algebraic groups over the field with one element*, [arXiv:0907.3824](https://arxiv.org/pdf/0907.3824).
- [Lorscheid 2014] O. Lorscheid, *Blueprints – towards absolute arithmetic?*, [arXiv:1204.3129](https://arxiv.org/pdf/1204.3129).
- [Lorscheid 2016] O. Lorscheid, *A blueprinted view on \(\mathbb F_1\)-geometry*, [arXiv:1301.0083](https://arxiv.org/pdf/1301.0083).
- [Lorscheid 2018a] O. Lorscheid, *The geometry of blueprints. Part II: Tits–Weyl models of algebraic groups*,
  [arXiv:1201.1324](https://arxiv.org/pdf/1201.1324).
- [Lorscheid 2018c] O. Lorscheid, *Blueprints and tropical scheme theory*, lecture notes of a course at IMPA,
  March–June 2018, version of 21 May 2018. Free at https://lorscheid.org/notes/2018-Blueprints/versions/lecturenotes180521.pdf
- [Lorscheid–Thas 2023] O. Lorscheid, K. Thas, *Towards the horizons of Tits's vision: on band schemes, crowds and
  \(\mathbb F_1\)-structures*, [arXiv:2305.13809](https://arxiv.org/pdf/2305.13809).
- [SGA3 II] M. Artin, J. E. Bertin, M. Demazure, P. Gabriel, A. Grothendieck, M. Raynaud, J.-P. Serre, *Schémas en
  groupes. II: Groupes de type multiplicatif, et structure des schémas en groupes généraux*, Lecture Notes in
  Mathematics 152, Springer. Cited here only through [Lorscheid 2018a], with the details given there. Free at https://webusers.imj-prg.fr/~patrick.polo/SGA3/ (re-edition by P. Gille and P. Polo)
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 00E0, 00OP and 01I1 carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
