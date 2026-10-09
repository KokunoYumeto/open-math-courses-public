# Characteristic one and hyperrings

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision is self-checked by the writing AI and corrects a point found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. The proofs in Sections 6.5 and 6.6 were drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

## Introduction

The monoid \(\mathbb{F}_1=\{0,1\}\) of this course has a multiplication and no addition. There are two ways to give it an addition without turning it into the field \(\mathbb{F}_2\).

- Put \(1+1=1\). The result is the *Boolean semifield* \(\mathbb{B}\). A semiring in which \(1+1=1\) is said to have *characteristic one*. The tropical semifields \(\mathbb{Z}_{\max}\) and \(\mathbb{R}_{\max}\) are of this kind. They are used in *The arithmetic site* and *The scaling site*.
- Let \(1+1\) be the set \(\{0,1\}\). The result is the *Krasner hyperfield* \(\mathbf{K}\). In a hyperring the sum of two elements is a nonempty set of elements. The quotient of a ring by a group of units is a hyperring. The adèle class space of a global field is such a quotient.

The lesson does five things.

1. Section 1 studies semirings of characteristic one: the order they carry, the semifields among them, and the maps \(x\mapsto x^n\), which are injective endomorphisms when multiplication can be cancelled.
2. Section 2 studies ideals and congruences in characteristic one. The two notions separate: a congruence is not determined by an ideal. The morphisms to \(\mathbb{B}\) play the part that morphisms to fields play for rings.
3. Section 3 defines hyperrings and hyperfields. It proves that the quotients \(R/G\) are hyperrings, and it introduces the Krasner hyperfield \(\mathbf{K}\), the sign hyperfield \(\mathbf{S}\) and the tropical hyperfield \(\mathbf{T}\). A morphism from a ring to \(\mathbf{K}\), \(\mathbf{S}\) or \(\mathbf{T}\) is a prime ideal, a prime ideal with an ordering of its residue field, or a nonarchimedean seminorm.
4. Sections 4 and 5 present results of [Connes–Consani 2011c]. A hyperfield that contains \(\mathbf{K}\) is the same thing as a projective geometry with at least four points on every line, whose points form an abelian group acting by collineations. The adèle class space \(\mathbb{A}_k/k^\times\) is a hyperring that contains \(\mathbf{K}\), and its closed prime ideals are the places of \(k\).
5. Section 6 returns to characteristic one. The ordinary addition of positive real numbers is recovered from the operation \(\max\) by a formula whose coefficients are given by the entropy function. This is the analogue, in characteristic one, of the formula for the sum of two Teichmüller representatives in a ring of Witt vectors. Section 6.5 carries this out for every perfect semiring \(R\) of characteristic one and an element \(\rho\ge 1\): after a completion defined by \(\rho\), the same formula defines a ring \(W(R,\rho)\), which is an algebra over \(\mathbb{R}\). Section 6.6 treats an earlier form of the construction, in which the least upper bounds are assumed to exist.

**What is assumed.** Commutative rings, ideals, prime ideals and fields. Semirings are defined below. Section 5 uses the adèle ring of a global field; the facts used are recalled there. Section 6 uses the concavity of the logarithm. Section 6.5 uses Cauchy sequences, the Heine–Borel theorem and the uniform continuity of continuous functions on compact metric spaces, from the core course [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10), whose text is [Lebl]; the completion of a space with a pseudometric is constructed in Lemma 6.12.

**Conventions.** Rings are commutative with \(1\). A *semiring* is a set \(R\) with two commutative and associative operations \(+\) and \(\cdot\), with neutral elements \(0\) and \(1\), such that \(x(y+z)=xy+xz\) and \(0\cdot x=0\) for all \(x,y,z\). A *morphism* of semirings preserves \(+\), \(\cdot\), \(0\) and \(1\). The semiring \(\{0\}\), in which \(1=0\), is allowed. A *semifield* is a semiring with \(1\neq 0\) in which every nonzero element has an inverse for the multiplication. The group of invertible elements of \(R\) is written \(R^\times\).

**References.** Basic references are [Connes–Consani 2011b] and [Connes 2011] for characteristic one, [Lescot 2013] for ideals, [Connes–Consani 2011c] and [Connes–Consani 2010b] for hyperrings, and [Lorscheid 2022] for the tropical hyperfield.

## 1. Semirings of characteristic one

### 1.1 The definition and the order

**Definition 1.1.** A semiring \(R\) has *characteristic one* if \(1+1=1\) in \(R\).

The name comes from a comparison with rings. In a ring of characteristic \(p\) one has \((p+1)\cdot 1=1\). For \(p=1\) this reads \(1+1=1\). [Connes–Consani 2011b, §2.3] and [Lorscheid 2022, §4.2] also call such a semiring *idempotent*; the reason is part (a) of the next lemma.

*Reference:* [Connes–Consani 2011b, Definition 2.7].

**Lemma 1.2.** Let \(R\) be a semiring of characteristic one.

(a) \(x+x=x\) for all \(x\).

(b) The relation \(x\le y\), defined by \(x+y=y\), is a partial order on \(R\). The sum \(x+y\) is the least upper bound of \(x\) and \(y\), and \(0\) is the least element.

(c) If \(x\le y\), then \(x+z\le y+z\) and \(xz\le yz\) for all \(z\).

(d) If \(x+y=0\), then \(x=y=0\).

(e) \((x+y)^m=\sum_{k=0}^{m}x^ky^{m-k}\) for all \(m\ge 1\).

*Proof.* (a) \(x+x=x(1+1)=x\).

(b) Reflexivity is (a). If \(x+y=y\) and \(y+x=x\), then \(x=y\). If \(x+y=y\) and \(y+z=z\), then \(x+z=x+(y+z)=(x+y)+z=y+z=z\). So \(\le\) is a partial order. From \(x+(x+y)=x+y\) we get \(x\le x+y\), and in the same way \(y\le x+y\). If \(x\le z\) and \(y\le z\), then \((x+y)+z=x+(y+z)=x+z=z\), so \(x+y\le z\). Finally \(0+x=x\) gives \(0\le x\).

(c) \((x+z)+(y+z)=(x+y)+(z+z)=y+z\) and \(xz+yz=(x+y)z=yz\).

(d) \(x\le x+y=0\) and \(0\le x\), so \(x=0\). In the same way \(y=0\).

(e) By induction on \(m\). Multiply the formula for \(m\) by \(x+y\). Each monomial \(x^jy^{m+1-j}\) with \(0\le j\le m+1\) appears once or twice in the result, and by (a) a repeated term counts once. □

From now on a semiring of characteristic one always carries the order of Lemma 1.2.

**Examples 1.3.**

(1) *The Boolean semifield.* \(\mathbb{B}=\{0,1\}\) with \(1+1=1\). It is a semifield. For a semiring \(R\), the map \(\mathbb{B}\to R\) sending \(0\) to \(0\) and \(1\) to \(1\) is a morphism exactly when \(R\) has characteristic one. So the semirings of characteristic one are the semirings that receive a morphism from \(\mathbb{B}\), and this morphism is unique.

(2) *The tropical semifields.* \(\mathbb{Z}_{\max}\) is the set \(\mathbb{Z}\cup\{-\infty\}\). Its semiring addition is \((x,y)\mapsto\max(x,y)\). Its semiring multiplication is the usual addition \((x,y)\mapsto x+y\). Its zero is \(-\infty\) and its unit is the integer \(0\). The semifield \(\mathbb{R}_{\max}\) is defined in the same way on \(\mathbb{R}\cup\{-\infty\}\). In both, the order of Lemma 1.2 is the usual order, and the \(n\)-th power of \(x\) is the usual product \(nx\). The exponential map identifies \(\mathbb{R}_{\max}\) with the semifield \(\mathbb{R}_+^{\max}=([0,\infty),\max,\times)\). This *multiplicative model* is the one used in [Connes–Consani 2011b] and in Section 6.

(3) *Polynomials over \(\mathbb{B}\).* The semiring \(\mathbb{B}[x]\) of polynomials with coefficients in \(\mathbb{B}\) has characteristic one. A polynomial is the same as a finite set \(A\subset\mathbb{N}\) of exponents: \(f_A=\sum_{a\in A}x^a\). Then \(f_A+f_B=f_{A\cup B}\) and \(f_Af_B=f_{A+B}\), where \(A+B=\{a+b:a\in A,\ b\in B\}\).

(4) *Lattices.* A distributive lattice with least element \(0\) and greatest element \(1\) is a semiring of characteristic one, with \(x+y=x\vee y\) and \(xy=x\wedge y\). Examples are the set \(\mathcal{P}(\mathbb{N})\) of subsets of \(\mathbb{N}\) with union and intersection, and the chain \(\{0 < a < 1\}\) with \(\max\) and \(\min\).

(5) *Ideals of a ring.* Let \(A\) be a nonzero ring. The set \(\mathrm{Id}(A)\) of ideals of \(A\), with the sum \(I+J\) and the product \(IJ\) of ideals, is a semiring. Its zero is the ideal \((0)\) and its unit is \(A\). It has characteristic one because \(I+I=I\). Its order is inclusion. The finitely generated ideals form a sub-semiring \(\mathrm{Id}_{\mathrm{fg}}(A)\). For \(A=\mathbb{Z}\) the map \(n\mapsto n\mathbb{Z}\) identifies \((\mathbb{N},\gcd,\times)\) with \(\mathrm{Id}(\mathbb{Z})\), where \(\gcd(n,0)=n\). In this semiring \(n\le m\) means that \(m\) divides \(n\).

There is no morphism between a nonzero ring and a nonzero semiring of characteristic one, in either direction. Let \(f:A\to R\) be a morphism from a ring to a semiring of characteristic one. Then \(f(1)+f(-1)=f(0)=0\), so \(f(1)=0\) by Lemma 1.2 (d), and \(R=\{0\}\). Let \(f:R\to A\) be a morphism in the other direction. Then \(f(1)+f(1)=f(1)\) in the ring \(A\), so \(f(1)=0\) and \(A=\{0\}\). In particular there is no morphism \(\mathbb{B}\to\mathbb{Z}\) and none \(\mathbb{Z}\to\mathbb{B}\). Hyperrings (Section 3) are a setting in which rings and the rule \(1+1=1\) meet.

### 1.2 Semifields of characteristic one

**Proposition 1.4.** Let \(G\) be an abelian group, written multiplicatively, with a partial order such that \(x\le y\) implies \(xz\le yz\), and such that any two elements \(x,y\) have a least upper bound \(x\vee y\). On \(F=G\cup\{0\}\) put \(0\cdot x=0\), \(x+0=x\), and \(x+y=x\vee y\) for \(x,y\in G\). Then \(F\) is a semifield of characteristic one. Every semifield of characteristic one is obtained in this way, from its group of units with the order of Lemma 1.2.

*Proof.* The operation \(\vee\) is commutative, associative and idempotent, and \(0\) is neutral for \(+\) by definition. For \(z\in G\) the map \(x\mapsto zx\) is a bijection of \(G\) that preserves the order, and so is its inverse. Hence \(z(x\vee y)=zx\vee zy\). This is the distributive law for nonzero elements. The cases with a zero are clear. So \(F\) is a semiring, \(1+1=1\vee 1=1\), and every nonzero element is invertible.

Conversely let \(F\) be a semifield of characteristic one and \(G=F^\times\). By Lemma 1.2 (d) the sum of two elements of \(G\) is not \(0\), so it lies in \(G\). By Lemma 1.2 (b) and (c) the order restricted to \(G\) is compatible with multiplication, and \(x+y\) is the least upper bound of \(x\) and \(y\) in \(G\). So \(F\) is the semifield built from \((G,\le)\). □

The semifields \(\mathbb{Z}_{\max}\), \(\mathbb{R}_{\max}\) and \(\mathbb{R}_+^{\max}\) come from the groups \((\mathbb{Z},+)\), \((\mathbb{R},+)\) and \((\mathbb{R}_{>0},\times)\) with their usual orders. The group \(\mathbb{Q}_{>0}\), ordered by \(x\le y\) when \(x/y\) is an integer, gives the semifield of fractional ideals \(x\mathbb{Z}\) of \(\mathbb{Z}\): the least upper bound of \(x\) and \(y\) is the positive generator of \(x\mathbb{Z}+y\mathbb{Z}\). It contains \((\mathbb{N},\gcd,\times)\).

**Theorem 1.5.** Let \(F\) be a semifield.

(a) Either \(F\) is a field, or \(x+y=0\) implies \(x=y=0\).

(b) In the second case, \(1\) is the only element of finite order in the group \(F^\times\).

(c) If every element of \(F^\times\) has finite order, then \(F\) is a field or \(F\) is isomorphic to \(\mathbb{B}\). This applies when \(F\) is finite.

In particular, \(\mathbb{B}\) is the only finite semifield of characteristic one, and the group of units of a semifield of characteristic one has no element of finite order other than \(1\).

*Proof.* (a) Suppose \(x+y=0\) with \(x\ne 0\). Put \(e=x^{-1}y\). Then \(1+e=0\), and \(z+ez=(1+e)z=0\) for every \(z\). So every element has an opposite, \((F,+)\) is a group, and \(F\) is a ring in which every nonzero element is invertible, that is, a field.

(b) Let \(x\in F^\times\) with \(x^n=1\), \(n\ge 1\). Put \(s=1+x+\dots+x^{n-1}\). Then \(xs=x+x^2+\dots+x^{n-1}+1=s\). If \(s=0\), then \(1=0\) by the assumption of the second case, which is false. So \(s\) is invertible and \(x=1\).

(c) Suppose \(F\) is not a field. By (a) and (b) the group \(F^\times\) is trivial, so \(F=\{0,1\}\). The element \(1+1\) is not \(0\) by (a). So \(1+1=1\) and \(F=\mathbb{B}\).

For the last statement: a semifield of characteristic one is not a field, since \(1+1=1\) would give \(1=0\) in a field. So (b) applies to it, and (c) applies to it if it is finite. □

*Reference:* [Connes–Consani 2011b, Proposition 2.13] states that \(\mathbb{B}\) is the only finite semifield of characteristic one.

### 1.3 The Frobenius endomorphisms

**Definition 1.6.** A semiring \(R\) is *multiplicatively cancellative* if \(xy=xz\) and \(x\neq 0\) imply \(y=z\).

Taking \(z=0\) shows that such a semiring has no zero divisors: \(xy=0\) implies \(x=0\) or \(y=0\). Every semifield is multiplicatively cancellative, and so is every sub-semiring of a semifield.

**Theorem 1.7 (Frobenius endomorphisms).** Let \(R\) be a multiplicatively cancellative semiring of characteristic one and let \(n\ge 1\) be an integer.

(a) \((x+y)^n=x^n+y^n\) for all \(x,y\). So \(\varphi_n:x\mapsto x^n\) is an endomorphism of the semiring \(R\).

(b) \(x\le y\) if and only if \(x^n\le y^n\).

(c) \(\varphi_n\) is injective.

*Proof.* (a) By Lemma 1.2 (e),
\[ (x^n+y^n)(x+y)^{n-1}=\sum_{k=0}^{n-1}x^{n+k}y^{n-1-k}+\sum_{k=0}^{n-1}x^{k}y^{2n-1-k}. \]
The first sum contains the monomials \(x^ay^{2n-1-a}\) with \(n\le a\le 2n-1\). The second contains those with \(0\le a\le n-1\). So each monomial of degree \(2n-1\) appears exactly once, and by Lemma 1.2 (e) the right side is \((x+y)^{2n-1}=(x+y)^n(x+y)^{n-1}\). If \(x+y=0\), then \(x=y=0\) and (a) is clear. Otherwise \((x+y)^{n-1}\neq 0\), because \(R\) has no zero divisors. Cancelling it gives \(x^n+y^n=(x+y)^n\). Since \(\varphi_n\) also preserves products, \(0\) and \(1\), it is an endomorphism.

(b) If \(x\le y\), then \(x^n\le y^n\) by Lemma 1.2 (c). Conversely let \(x^n\le y^n\) and put \(s=x+y\). By (a), \(s^n=x^n+y^n=y^n\). If \(y=0\), then \(x^n=0\), so \(x=0\) and \(x\le y\). Let \(y\ne 0\). Since \(y\le s\), Lemma 1.2 (c) gives
\[ y^n=y^{n-1}y\le y^{n-1}s\le s^{n-1}s=s^n=y^n. \]
So \(y^{n-1}s=y^{n-1}y\). Cancelling \(y^{n-1}\neq 0\) gives \(s=y\), that is, \(x\le y\).

(c) If \(x^n=y^n\), then \(x\le y\) and \(y\le x\) by (b). □

*Reference:* [Connes–Consani 2011b, Proposition 2.16]; [Connes 2011, Lemma 4.3], whose proof has the same first step.

The exponent \(n=0\) is excluded: \(x\mapsto x^0=1\) is not an endomorphism.

**Examples 1.8.**

(1) In \(\mathbb{Z}_{\max}\) the map \(\varphi_n\) is \(x\mapsto nx\). Theorem 1.7 says that \(n\max(x,y)=\max(nx,ny)\). The map is injective. It is not surjective for \(n\ge 2\). In \(\mathbb{R}_{\max}\) it is bijective.

(2) Let \(A\) be a principal ideal domain. The semiring \(\mathrm{Id}(A)\) is multiplicatively cancellative: if \((a)(b)=(a)(c)\) with \(a\ne 0\), then \(ab\) and \(ac\) differ by a unit, so \((b)=(c)\). Theorem 1.7 gives \((I+J)^n=I^n+J^n\) for all ideals \(I,J\) of \(A\). For \(A=\mathbb{Z}\) this is \(\gcd(a,b)^n=\gcd(a^n,b^n)\).

(3) Cancellation is needed. Let \(A=k[x,y]\) for a field \(k\), \(\mathfrak{m}=(x,y)\) and \(\mathfrak{q}=(x^2,y^2)\). In \(\mathrm{Id}(A)\) we have \((x)+(y)=\mathfrak{m}\) and \((x)^2+(y)^2=\mathfrak{q}\). But \(\mathfrak{q}\neq\mathfrak{m}^2\), because \(xy\in\mathfrak{m}^2\) and \(xy\notin\mathfrak{q}\). So \(\varphi_2\) is not additive. Accordingly \(\mathrm{Id}(A)\) is not multiplicatively cancellative: \(\mathfrak{m}\mathfrak{q}=(x^3,x^2y,xy^2,y^3)=\mathfrak{m}\mathfrak{m}^2\).

(4) In \(\mathbb{B}[x]\), \((1+x)^2=1+x+x^2\neq 1+x^2\), so \(\varphi_2\) is not additive. It is not injective either. Let \(f=1+x+x^2+x^3+x^4\) and \(g=1+x+x^3+x^4\). Then \(f^2=g^2=\sum_{k=0}^{8}x^k\), because \(\{0,1,3,4\}+\{0,1,3,4\}=\{0,1,\dots,8\}\). The semiring \(\mathbb{B}[x]\) has no zero divisors, but it is not multiplicatively cancellative: \((1+x)(1+x+x^2)=(1+x)(1+x^2)\).

**Definition 1.9.** A multiplicatively cancellative semiring \(R\) of characteristic one is *perfect* if \(\varphi_n\) is surjective for every \(n\ge 1\).

*Reference:* [Connes 2011, Definition 4.4]. [Connes–Consani 2011b, Definition 2.17] uses the same word for a semiring of characteristic one with a family of automorphisms \(\vartheta_\lambda\), \(\lambda\) a positive real number, such that \(\vartheta_n=\varphi_n\), \(\vartheta_\lambda\vartheta_\mu=\vartheta_{\lambda\mu}\) and \(\vartheta_\lambda(x)\vartheta_\mu(x)=\vartheta_{\lambda+\mu}(x)\).

**Proposition 1.10.** Let \(R\) be perfect. For a rational number \(\alpha=a/b>0\) put \(\theta_\alpha=\varphi_a\varphi_b^{-1}\). Then \(\theta_\alpha\) is a well defined automorphism of \(R\), and for all rational \(\alpha,\beta>0\) and all \(x\in R\):
\[ \theta_\alpha\theta_\beta=\theta_{\alpha\beta},\qquad \theta_\alpha(x)\,\theta_\beta(x)=\theta_{\alpha+\beta}(x). \]
We write \(x^\alpha=\theta_\alpha(x)\).

*Proof.* By Theorem 1.7 each \(\varphi_n\) is an automorphism. Clearly \(\varphi_m\varphi_n=\varphi_{mn}\), so the \(\varphi_n\) commute. If \(a/b=a'/b'\), then \(\varphi_a\varphi_{b'}=\varphi_{ab'}=\varphi_{a'b}=\varphi_{a'}\varphi_b\), hence \(\varphi_a\varphi_b^{-1}=\varphi_{a'}\varphi_{b'}^{-1}\). So \(\theta_\alpha\) is well defined, and the first formula follows. For the second, write \(\alpha=a/n\) and \(\beta=b/n\), and let \(z=\varphi_n^{-1}(x)\). Then \(\theta_\alpha(x)=z^a\), \(\theta_\beta(x)=z^b\), and \(z^az^b=z^{a+b}=\theta_{\alpha+\beta}(x)\). □

*Reference:* [Connes 2011, Proposition 4.5].

In \(\mathbb{R}_+^{\max}\), \(\theta_\alpha(x)=x^\alpha\) in the usual sense, and \(x\mapsto x^\alpha\) is an automorphism for every real \(\alpha>0\). So \(\mathbb{R}_+^{\max}\) is perfect in the sense of both works. The semifield \(\mathbb{Z}_{\max}\) is not perfect. The semifield \(\mathbb{B}\) is perfect, with \(\theta_\alpha\) the identity.

## 2. Ideals and congruences in characteristic one

A reference for this section is [Lescot 2013]. Throughout, \(R\) is a semiring of characteristic one.

**Definition 2.1.**

- An *ideal* of \(R\) is a subset \(I\) with \(0\in I\), \(I+I\subseteq I\) and \(RI\subseteq I\). It is *prime* if \(I\ne R\) and \(xy\in I\) implies \(x\in I\) or \(y\in I\).
- An ideal \(I\) is *saturated* if \(x\le y\) and \(y\in I\) imply \(x\in I\). The *saturation* of an ideal \(I\) is \(\overline{I}=\{x:x\le y\text{ for some }y\in I\}\).
- A *congruence* on \(R\) is an equivalence relation \(\sim\) such that \(x\sim x'\) and \(y\sim y'\) imply \(x+y\sim x'+y'\) and \(xy\sim x'y'\). The set \(R/{\sim}\) of classes is then a semiring of characteristic one, and \(R\to R/{\sim}\) is a morphism.
- The *kernel* of a morphism of semirings \(f:R\to S\) is \(\ker f=f^{-1}(0)\). The *congruence of \(f\)* is the relation \(f(x)=f(y)\).

By Lemma 1.2 (c) the saturation \(\overline{I}\) is an ideal. It is saturated, and it is the smallest saturated ideal that contains \(I\). The word "saturated" is that of [Lescot 2013].

For a ring, congruences and ideals correspond to each other. In characteristic one this fails in two ways. Not every ideal is a kernel. And a congruence is not determined by its kernel.

**Proposition 2.2.** Let \(I\) be an ideal of \(R\).

(a) The kernel of a morphism of semirings \(f:R\to S\) is a saturated ideal.

(b) Write \(x\equiv_Iy\) if there is \(i\in I\) with \(x+i=y+i\). This is a congruence on \(R\). The kernel of \(R\to R/{\equiv_I}\) is \(\overline{I}\).

(c) \(I\) is the kernel of a morphism if and only if \(I\) is saturated.

*Proof.* (a) The kernel is an ideal. If \(x\le y\) and \(f(y)=0\), then \(f(x)=f(x)+f(y)=f(x+y)=f(y)=0\).

(b) The relation is reflexive (take \(i=0\)) and symmetric. If \(x+i=y+i\) and \(y+j=z+j\), then \(x+(i+j)=z+(i+j)\). So it is an equivalence relation. If \(x+i=y+i\), then \((x+z)+i=(y+z)+i\) and \(xz+iz=yz+iz\) with \(iz\in I\). So it is a congruence. An element \(x\) is in the kernel when \(x+i=i\) for some \(i\in I\), that is, when \(x\le i\) for some \(i\in I\).

(c) This follows from (a) and (b), because \(\overline{I}=I\) when \(I\) is saturated. □

**Examples 2.3.**

(1) Let \(C=\{0 < a < 1\}\) be the chain of Examples 1.3 (4). Its ideals are \(\{0\}\), \(\{0,a\}\) and \(C\), and all three are saturated. Every partition of \(C\) into intervals is a congruence. Indeed, let \(x\le x'\) lie in one class and let \(y\) be any element. Then the pair \(\max(x,y),\max(x',y)\) is \(x,x'\), or it is \(y,x'\) with \(x\le y\le x'\), or it is \(y,y\). In each case the two elements lie in one class. The same holds for \(\min\). The only other partition, \(\{0,1\},\{a\}\), is not a congruence: \(0\sim 1\) would give \(a=\max(0,a)\sim\max(1,a)=1\). So \(C\) has exactly four congruences. Two of them, equality and the partition \(\{0\},\{a,1\}\), have the same kernel \(\{0\}\).

(2) Suppose that \(R\ne\{0\}\) has no zero divisors. Define \(\beta:R\to\mathbb{B}\) by \(\beta(0)=0\) and \(\beta(x)=1\) for \(x\ne 0\). This is a morphism: it preserves sums by Lemma 1.2 (d), and products because there are no zero divisors. Its kernel is \(\{0\}\). It is injective only when \(R=\mathbb{B}\). For example \(\beta:\mathbb{Z}_{\max}\to\mathbb{B}\) is a morphism of semifields with kernel \(\{0\}\) which is not injective. A morphism of fields is always injective.

(3) In \(\mathbb{B}[x]\) let \(I\) be the ideal of all multiples of \(1+x\). It does not contain \(1\): in terms of sets of exponents, \(\{0,1\}+A\) is never \(\{0\}\). But \(1\le 1+x\). So \(I\) is not saturated, and \(\overline{I}=\mathbb{B}[x]\). By Proposition 2.2, \(I\) is not the kernel of a morphism.

**Proposition 2.4 (congruences on a semifield).** Let \(F\) be a semifield of characteristic one and \(G=F^\times\).

(a) The only ideals of \(F\) are \(\{0\}\) and \(F\).

(b) Let \(\sim\) be a congruence on \(F\) with \(1\not\sim 0\). Then the class \(N\) of \(1\) is a subgroup of \(G\). It is closed under addition. It is *convex*: if \(x\le z\le y\) and \(x,y\in N\), then \(z\in N\). Moreover \(x\sim y\) if and only if \(x=y=0\), or \(x,y\in G\) and \(xy^{-1}\in N\).

(c) Conversely, let \(N\) be a convex subgroup of \(G\) that is closed under addition. Then the relation described in (b) is a congruence \(\sim_N\) on \(F\) with \(1\not\sim_N0\).

So the congruences on \(F\) are the relation with a single class and the relations \(\sim_N\). Indeed, if \(1\sim 0\), then \(x=x\cdot 1\sim x\cdot 0=0\) for all \(x\).

*Proof.* (a) An ideal that contains a unit contains \(1\), and then it contains everything.

(b) If \(x\sim 0\) for some \(x\in G\), then \(1=x^{-1}x\sim 0\). So the class of \(0\) is \(\{0\}\), and \(N\subseteq G\). If \(x,y\in N\), then \(xy\sim 1\), \(x^{-1}=x^{-1}\cdot 1\sim x^{-1}x=1\) and \(x+y\sim 1+1=1\). So \(N\) is a subgroup closed under addition. Let \(x\le z\le y\) with \(x,y\in N\). Then \(z=z+x\sim z+1\) and \(y=y+z\sim 1+z\). Hence \(z\sim y\sim 1\). For \(x,y\in G\), multiplying by \(y^{-1}\) or by \(y\) shows that \(x\sim y\) if and only if \(xy^{-1}\sim 1\).

(c) The relation \(\sim_N\) is an equivalence relation because \(N\) is a subgroup, and it is compatible with multiplication. For addition it is enough to show that \(x\sim_Nx'\) implies \(x+y\sim_Nx'+y\). This is clear if \(x=x'=0\) or if \(y=0\). Otherwise \(x'=nx\) with \(n\in N\). The elements \(a=(n^{-1}+1)^{-1}\) and \(b=n+1\) belong to \(N\). From \(a^{-1}\ge 1\) and \(a^{-1}\ge n^{-1}\) we get \(a\le 1\) and \(a\le n\). Also \(1\le b\) and \(n\le b\). By Lemma 1.2 (c),
\[ a(x+y)=ax+ay\le nx+y\le bx+by=b(x+y). \]
So \((nx+y)(x+y)^{-1}\) lies between \(a\) and \(b\). It belongs to \(N\) by convexity. □

**Example 2.5.** In \(\mathbb{Z}_{\max}\) and \(\mathbb{R}_{\max}\) the group \(G\) is \(\mathbb{Z}\) or \(\mathbb{R}\) with its usual order, and every subgroup is closed under \(\max\). A convex subgroup that contains some \(t>0\) contains the interval \([-mt,mt]\) for every \(m\ge 1\), so it is the whole group. The convex subgroups are therefore \(\{0\}\) and \(G\). So \(\mathbb{Z}_{\max}\) and \(\mathbb{R}_{\max}\) have exactly three congruences. The quotients are the semifield itself, \(\mathbb{B}\), and \(\{0\}\). Consequently a morphism from \(\mathbb{Z}_{\max}\) or \(\mathbb{R}_{\max}\) to a nonzero semiring \(S\) is either injective, or the composite of \(\beta\) with the morphism \(\mathbb{B}\to S\).

**Theorem 2.6 (points with values in \(\mathbb{B}\)).** The map \(f\mapsto\ker f\) is a bijection from the set of morphisms \(R\to\mathbb{B}\) to the set of saturated prime ideals of \(R\).

*Proof.* Let \(f:R\to\mathbb{B}\) be a morphism. Its kernel is a saturated ideal by Proposition 2.2. It is not \(R\), because \(f(1)=1\). If \(f(xy)=0\), then \(f(x)f(y)=0\), so \(f(x)=0\) or \(f(y)=0\). So \(\ker f\) is a saturated prime ideal. It determines \(f\), since \(f\) takes the value \(1\) outside its kernel.

Conversely let \(P\) be a saturated prime ideal. Define \(f(x)=0\) for \(x\in P\) and \(f(x)=1\) otherwise. Then \(f(0)=0\) and \(f(1)=1\). We have \(xy\in P\) if and only if \(x\in P\) or \(y\in P\), so \(f(xy)=f(x)f(y)\). If \(x,y\in P\), then \(x+y\in P\). If \(x+y\in P\), then \(x,y\in P\), because \(x\le x+y\), \(y\le x+y\) and \(P\) is saturated. So \(f(x+y)=0\) exactly when \(f(x)=f(y)=0\). This means \(f(x+y)=f(x)+f(y)\). □

**Example 2.7 (the spectrum of a ring).** Let \(A\) be a nonzero ring and \(R=\mathrm{Id}_{\mathrm{fg}}(A)\). For a prime ideal \(\mathfrak{p}\) of \(A\) let \(P_{\mathfrak p}\) be the set of finitely generated ideals contained in \(\mathfrak{p}\). Then \(\mathfrak{p}\mapsto P_{\mathfrak p}\) is a bijection from the set of prime ideals of \(A\) to the set of saturated prime ideals of \(R\). With Theorem 2.6, the set of morphisms \(\mathrm{Id}_{\mathrm{fg}}(A)\to\mathbb{B}\) is in bijection with the prime spectrum of \(A\).

To see this, note first that \(P_{\mathfrak p}\) is closed under sums and under products with elements of \(R\). It is saturated because the order is inclusion. It does not contain \(A\). It is prime because \(IJ\subseteq\mathfrak{p}\) implies \(I\subseteq\mathfrak{p}\) or \(J\subseteq\mathfrak{p}\). Conversely let \(P\) be a saturated prime ideal of \(R\) and let \(\mathfrak{p}=\{a\in A:(a)\in P\}\). We have \((a+b)\subseteq(a)+(b)\) and \((ra)\subseteq(a)\), and \(P\) is saturated, so \(\mathfrak{p}\) is an ideal. It is proper because \((1)\notin P\), and prime because \((ab)=(a)(b)\). A finitely generated ideal \(I=(a_1,\dots,a_r)\) is the sum of the \((a_i)\) and contains each of them. So \(I\in P\) if and only if every \((a_i)\) is in \(P\), that is, if and only if \(I\subseteq\mathfrak{p}\). Hence \(P=P_{\mathfrak p}\). Finally \(\mathfrak{p}\) is recovered from \(P_{\mathfrak p}\) as the set of \(a\) with \((a)\in P_{\mathfrak p}\).

For \(A=\mathbb{Z}\): the morphisms \((\mathbb{N},\gcd,\times)\to\mathbb{B}\) are \(f_0\), with \(f_0(n)=1\) for \(n\neq 0\), and \(f_p\) for each prime number \(p\), with \(f_p(n)=0\) exactly when \(p\) divides \(n\).

**Theorem 2.8 (enough saturated primes).** Let \(I\) be a saturated ideal of \(R\) and let \(x\in R\) be such that \(x^n\notin I\) for all \(n\ge 0\). Then there is a saturated prime ideal \(P\supseteq I\) with \(x\notin P\).

*Proof.* Let \(\Sigma\) be the set of saturated ideals \(J\supseteq I\) that contain no power \(x^n\), \(n\ge 0\). It contains \(I\). The union of a chain in \(\Sigma\) is in \(\Sigma\). By Zorn's lemma \(\Sigma\) has a maximal element \(P\). Since \(x^0=1\notin P\), \(P\neq R\). Suppose \(uv\in P\) with \(u\notin P\) and \(v\notin P\). The ideals \(\overline{P+Ru}\) and \(\overline{P+Rv}\) are saturated and strictly larger than \(P\). So they are not in \(\Sigma\). Hence there are \(m,n\ge 0\), \(p,p'\in P\) and \(a,b\in R\) with \(x^m\le p+au\) and \(x^n\le p'+bv\). By Lemma 1.2 (c),
\[ x^{m+n}\le(p+au)(p'+bv)=pp'+pbv+aup'+ab\,uv. \]
The right side is in \(P\), and \(P\) is saturated. So \(x^{m+n}\in P\). This contradicts \(P\in\Sigma\). So \(P\) is prime. □

**Corollary 2.9.** (a) If \(R\ne\{0\}\), there is a morphism \(R\to\mathbb{B}\).

(b) Let \(I\) be a saturated ideal and \(r(I)=\{x:x^n\in I\text{ for some }n\ge 1\}\). Then \(r(I)\) is a saturated ideal, and it is the intersection of the saturated prime ideals that contain \(I\).

(c) A saturated ideal which is maximal among the saturated ideals different from \(R\) is prime.

*Proof.* (a) The ideal \(\{0\}\) is saturated and does not contain \(1\). Apply Theorem 2.8 to \(I=\{0\}\) and \(x=1\), and then Theorem 2.6.

(b) If \(x^m\in I\) and \(y^n\in I\), every term of \((x+y)^{m+n}=\sum_kx^ky^{m+n-k}\) is a multiple of \(x^m\) or of \(y^n\). So \(x+y\in r(I)\). Clearly \(r(I)\) is stable under multiplication by elements of \(R\). If \(x\le y\) and \(y^n\in I\), then \(x^n\le y^n\), so \(x^n\in I\). So \(r(I)\) is a saturated ideal. A prime ideal that contains \(I\) contains \(r(I)\). Conversely let \(x\notin r(I)\). Then \(I\neq R\), so \(1\notin I\). So \(x^n\notin I\) for all \(n\ge 0\), and Theorem 2.8 gives a saturated prime ideal that contains \(I\) and not \(x\).

(c) Let \(M\) be such an ideal. Theorem 2.8, applied to \(I=M\) and \(x=1\), gives a saturated prime ideal \(P\supseteq M\). Since \(P\neq R\), \(P=M\). □

*Reference:* (c) is [Lescot 2013, Proposition 2.1], proved there by a computation of the same kind as in Theorem 2.8.

An ideal \(I\) is *radical* if \(r(I)=I\). By Corollary 2.9 (b) a saturated ideal is radical if and only if it is an intersection of saturated prime ideals. The next result says when finitely many suffice. By convention \(R\) is the intersection of the empty family.

**Theorem 2.10.** Suppose that every increasing sequence \(J_1\subseteq J_2\subseteq\cdots\) of saturated ideals of \(R\) is stationary. Then every saturated radical ideal of \(R\) is the intersection of finitely many saturated prime ideals.

*Proof.* Suppose not. By the chain condition, the set of saturated radical ideals that are not finite intersections of saturated prime ideals has a maximal element \(J\). Then \(J\ne R\), and \(J\) is not prime. So there are \(u,v\notin J\) with \(uv\in J\). Put \(K=r(\overline{J+Ru})\) and \(L=r(\overline{J+Rv})\). By Corollary 2.9 (b) these are saturated radical ideals. They contain \(J\) strictly. By the choice of \(J\), each of them is a finite intersection of saturated prime ideals. We show that \(J=K\cap L\); this is a contradiction. Let \(x\in K\cap L\). There are \(m,n\ge 1\), \(j,j'\in J\) and \(a,b\in R\) with \(x^m\le j+au\) and \(x^n\le j'+bv\). As in the proof of Theorem 2.8, \(x^{m+n}\le(j+au)(j'+bv)\in J\). So \(x^{m+n}\in J\), and \(x\in J\) because \(J\) is radical. □

The chain condition is the *weakly noetherian* condition of [Lescot 2013, Definition 2.5].

*Reference:* [Lescot 2013, Theorem 6.3] is stated without the chain condition. The proof given there takes a maximal element of a set of saturated ideals, which needs the condition, and [Lescot 2013, Corollary 6.4] assumes it. Without the condition the conclusion fails, as Example 2.11 shows. So we state the theorem with it.

**Example 2.11.** Let \(R=\mathcal{P}(\mathbb{N})\), with union as sum and intersection as product. Every ideal of \(R\) is saturated: if \(X\subseteq Y\) and \(Y\in I\), then \(X=X\cap Y\in I\). Every ideal is radical, since \(X^n=X\). The ideal \(\{\emptyset\}\) is not the intersection of finitely many prime ideals. Indeed, let \(P_1,\dots,P_r\) be prime ideals with \(P_1\cap\dots\cap P_r=\{\emptyset\}\). For each \(n\in\mathbb{N}\) the singleton \(\{n\}\) is outside some \(P_i\). So some \(P_i\) misses two singletons \(\{m\}\ne\{n\}\). But \(\{m\}\cap\{n\}=\emptyset\in P_i\), and \(P_i\) is prime. This is a contradiction.

## 3. Hyperrings and hyperfields

### 3.1 Definitions

**Definition 3.1.** A *canonical hypergroup* is a set \(H\) with an element \(0\) and a map \(+\) from \(H\times H\) to the set of nonempty subsets of \(H\), such that for all \(x,y,z\in H\):

- (H1) \(x+y=y+x\);
- (H2) \((x+y)+z=x+(y+z)\);
- (H3) \(x+0=\{x\}\);
- (H4) there is exactly one element \(-x\) with \(0\in x+(-x)\);
- (H5) if \(x\in y+z\), then \(z\in x+(-y)\).

Here the sum of two subsets is \(A+B=\bigcup_{a\in A,\,b\in B}(a+b)\), and an element stands for the set that contains only it. We write \(x-y\) for \(x+(-y)\) and \(-A\) for \(\{-a:a\in A\}\). The names *canonical hypergroup*, and *reversibility* for property (H5), are those of [Connes–Consani 2011c, §2].

An abelian group is a canonical hypergroup in which all sums have one element.

**Lemma 3.2.** In a canonical hypergroup:

(a) \(-0=0\) and \(-(-x)=x\);

(b) \(0\in x+y\) if and only if \(y=-x\);

(c) if \(z\in x+y\), then \(-z\in(-x)+(-y)\);

(d) two subsets \(X\) and \(Y\) have a common element if and only if \(0\in X-Y\).

*Proof.* (a) \(0\in 0+0\) by (H3). And \(0\in x+(-x)=(-x)+x\), so \(x=-(-x)\) by the uniqueness in (H4). (b) is (H4). (c) By (H1), reversibility also says: if \(x\in y+z\), then \(y\in x-z\). Let \(z\in x+y\). Then \(x\in z-y\). Apply the rule to \(x\in(-y)+z\): this gives \(-y\in x-z\). Apply it to \(-y\in(-z)+x\): this gives \(-z\in(-y)-x\). (d) If \(x\in X\cap Y\), then \(0\in x-x\subseteq X-Y\). If \(0\in x-y\) with \(x\in X\) and \(y\in Y\), then \(-y=-x\) by (b), so \(y=x\) by (a). □

**Definition 3.3.** A *hyperring* is a set \(R\) with a map \(+\) as above and a multiplication such that: \((R,+)\) is a canonical hypergroup; the multiplication is commutative and associative with a unit \(1\); \(0\cdot x=0\) for all \(x\); \(x(y+z)=xy+xz\) for all \(x,y,z\), as an equality of sets; and \(1\neq 0\). A *hyperfield* is a hyperring in which every nonzero element is invertible.

A *morphism* of hyperrings is a map \(f:R\to R'\) with \(f(0)=0\), \(f(1)=1\), \(f(xy)=f(x)f(y)\) and \(f(x+y)\subseteq f(x)+f(y)\) for all \(x,y\). An *ideal* of \(R\) is a subset \(I\) with \(0\in I\), \(x+y\subseteq I\) for all \(x,y\in I\), and \(RI\subseteq I\). It is *prime* if \(I\neq R\) and \(xy\in I\) implies \(x\in I\) or \(y\in I\). The *kernel* of a morphism \(f\) is \(f^{-1}(0)\); it is an ideal.

*Reference:* [Connes–Consani 2011c, Definition 2.1], where the multiplication need not be commutative.

Some remarks.

- A nonzero ring is a hyperring whose sums have one element. A morphism of nonzero rings is the same as a morphism of hyperrings between them.
- In a hyperring \(-x=(-1)x\). Indeed \(0=0\cdot x\in(1+(-1))x=x+(-1)x\). So an ideal contains \(-x\) when it contains \(x\). A morphism satisfies \(f(-x)=-f(x)\), because \(0=f(0)\in f(x)+f(-x)\).
- The conditions \(f(0)=0\) and \(f(1)=1\) do not follow from the other two. The constant maps with value \(0\) or \(1\), from any hyperring to the hyperfield \(\mathbf{K}\) defined below, satisfy the other two.
- Hyperrings can also be treated as ordered blueprints, a variant of the objects of *Blueprints and blue schemes*: a relation \(z\in x+y\) is read as \(z\le x+y\) ([Lorscheid 2022, Remark 1.4]).

### 3.2 Quotients by groups of units

**Lemma 3.4 (orbit hypergroups).** Let \(A\) be an abelian group and \(\Gamma\) a group of automorphisms of \(A\). Let \(A/\Gamma\) be the set of orbits \([x]=\Gamma x\). Put
\[ [x]+[y]=\{[a+b]:a\in[x],\ b\in[y]\}. \]
Then \(A/\Gamma\) is a canonical hypergroup with zero \([0]\) and \(-[x]=[-x]\). For all \(x_1,\dots,x_n\in A\),
\[ [x_1]+\dots+[x_n]=\{[a_1+\dots+a_n]:a_i\in[x_i]\}. \]

*Proof.* (H1) is clear. We prove that \(([x_1]+[x_2])+[x_3]\) is the set of all \([a_1+a_2+a_3]\) with \(a_i\in[x_i]\). An element of the left side is \([c+a_3]\) with \(c\in[a_1+a_2]\) and \(a_i\in[x_i]\). Then \(c=\gamma(a_1+a_2)=\gamma a_1+\gamma a_2\) for some \(\gamma\in\Gamma\), and \(\gamma a_i\in[x_i]\). So the left side is contained in the right side. Conversely \([a_1+a_2+a_3]\in[a_1+a_2]+[x_3]\). The right side is symmetric in the three indices. With (H1) this gives (H2). The formula for \(n\) terms follows by induction in the same way.

(H3): \([x]+[0]=\{[a]:a\in[x]\}=\{[x]\}\). (H4): \([0]\in[x]+[y]\) means that \(a+b=0\) for some \(a\in[x]\), \(b\in[y]\), that is, \([y]=[-x]\). (H5): if \([x]\in[y]+[z]\), then \(\gamma x=b+c\) with \(b\in[y]\), \(c\in[z]\) and \(\gamma\in\Gamma\). Then \(c=\gamma x+(-b)\), so \([z]\in[x]+[-y]\). □

*Reference:* [Connes–Consani 2010b, Lemma 4.1].

**Theorem 3.5 (quotient hyperrings).** Let \(R\) be a nonzero ring and \(G\) a subgroup of \(R^\times\). Let \(R/G\) be the set of orbits \([x]=xG\), with the sum of Lemma 3.4 for the action of \(G\) on \((R,+)\) by multiplication, and with the product \([x][y]=[xy]\).

(a) \(R/G\) is a hyperring, and \(\pi:R\to R/G\), \(x\mapsto[x]\), is a morphism.

(b) \((R/G)^\times=R^\times/G\). The hyperring \(R/G\) is a hyperfield if and only if \(R\) is a field.

(c) The maps \(J\mapsto\pi(J)\) and \(I\mapsto\pi^{-1}(I)\) are inverse bijections between the ideals of \(R\) and the ideals of \(R/G\). Prime ideals correspond to prime ideals.

*Proof.* (a) Each element of \(G\) acts on \((R,+)\) by an automorphism. So \((R/G,+)\) is a canonical hypergroup by Lemma 3.4. The product is well defined because \(xg\cdot yh=xy\cdot gh\). It is commutative and associative with unit \([1]\), and \([0][x]=[0]\). For the distributive law: \([z]([x]+[y])\) is the set of classes \([z(xg+yh)]=[zxg+zyh]\) with \(g,h\in G\), and this is \([zx]+[zy]\). Finally \([1]\ne[0]\) because \(R\neq 0\). The map \(\pi\) preserves \(0\), \(1\) and products, and \(\pi(x+y)=[x+y]\in[x]+[y]\).

(b) \([x][y]=[1]\) means \(xy\in G\). There is such a \(y\) if and only if \(x\in R^\times\).

(c) Let \(J\) be an ideal of \(R\). Then \(JG=J\), so \(\pi^{-1}(\pi(J))=J\). The set \(\pi(J)\) is an ideal: for \(a,b\in J\) the elements of \([a]+[b]\) are the \([ag+bh]\), and \(ag+bh\in J\); and \([r][a]=[ra]\). Conversely let \(I\) be an ideal of \(R/G\). Then \(\pi^{-1}(I)\) is an ideal of \(R\): if \([a],[b]\in I\), then \([a+b]\in[a]+[b]\subseteq I\) and \([ra]=[r][a]\in I\). And \(\pi(\pi^{-1}(I))=I\) because \(\pi\) is surjective. Finally \(J\neq R\) if and only if \(\pi(J)\neq R/G\), and \(ab\in J\) if and only if \([a][b]\in\pi(J)\). So \(J\) is prime if and only if \(\pi(J)\) is prime. □

*Reference:* the construction is due to Krasner; see [Krasner 1983] and [Connes–Consani 2011c, Proposition 2.5].

### 3.3 The Krasner hyperfield and the sign hyperfield

**Definition 3.6.**

- The *Krasner hyperfield* \(\mathbf{K}\) is the set \(\{0,1\}\) with its usual multiplication and the sums \(0+0=\{0\}\), \(0+1=\{1\}\), \(1+1=\{0,1\}\).
- The *sign hyperfield* \(\mathbf{S}\) is the set \(\{-1,0,1\}\) with its usual multiplication and the sums \(x+0=\{x\}\), \(1+1=\{1\}\), \((-1)+(-1)=\{-1\}\), \(1+(-1)=\{-1,0,1\}\).
- A hyperring \(R\) is an *extension of \(\mathbf{K}\)* if \(1+1=\{0,1\}\) in \(R\). It is an *extension of \(\mathbf{S}\)* if \(1+1=\{1\}\) and \(1-1=\{-1,0,1\}\) in \(R\).

Both are hyperfields, by Theorem 3.5. Let \(F\) be a field with at least three elements. Then \(F^\times+F^\times=F\) (see the proof of Proposition 3.7), so \(F/F^\times=\{[0],[1]\}\) is \(\mathbf{K}\). Let \(F\) be an ordered field with set of positive elements \(F_{>0}\). Then \(F/F_{>0}=\{[-1],[0],[1]\}\) is \(\mathbf{S}\): the sum of two positive elements is positive, and every element is a difference of two positive elements. So \(\mathbf{K}\) records whether an element of a field is zero, and \(\mathbf{S}\) records the sign of an element of an ordered field.

The multiplicative monoid of \(\mathbf{K}\) is \(\mathbb{F}_1=\{0,1\}\). That of \(\mathbf{S}\) is \(\mathbb{F}_{1^2}=\{0\}\cup\mu_2\). In \(\mathbf{S}\) we have \(1+1=1\), as in characteristic one, and still \(1\) has an opposite. The absolute value \(\mathbf{S}\to\mathbf{K}\) is a morphism. If \(R\) is an extension of \(\mathbf{K}\), the subset \(\{0,1\}\) with the operations of \(R\) is a copy of \(\mathbf{K}\). If \(R\) is an extension of \(\mathbf{S}\), then \(-1\neq 1\) in \(R\), because \(0\notin 1+1\), and the subset \(\{-1,0,1\}\) is a copy of \(\mathbf{S}\), by Lemma 3.2 (c).

*Reference:* [Connes–Consani 2011c, Definition 2.2].

An *ordering* of a field \(F\) is a subset \(P\) (the positive elements) with \(P+P\subseteq P\) and \(PP\subseteq P\), such that \(F\) is the disjoint union of \(P\), \(\{0\}\) and \(-P\).

**Proposition 3.7.** Let \(R\) be a nonzero ring and \(G\) a subgroup of \(R^\times\).

(a) \(R/G\) is an extension of \(\mathbf{K}\) if and only if \(G\cup\{0\}\) is a subfield of \(R\) with at least three elements.

(b) \(R/G\) is an extension of \(\mathbf{S}\) if and only if \(F=G\cup\{0\}\cup(-G)\) is a subfield of \(R\) and \(G\) is an ordering of \(F\).

*Proof.* In \(R/G\), the sum \([1]+[1]\) is the set of classes of the elements of \(G+G\), and \([1]-[1]\) is the set of classes of the elements of \(G-G\).

(a) So \([1]+[1]=\{[0],[1]\}\) if and only if \(G+G=G\cup\{0\}\). Suppose this holds. Then \(G\neq\{1\}\), because \(\{1+1\}\) has one element. The set \(k=G\cup\{0\}\) is closed under addition and multiplication. Since \(0\in G+G\), there are \(g,h\in G\) with \(g=-h\), so \(-1=gh^{-1}\in G\). So \(k\) is a subring in which every nonzero element is invertible, that is, a subfield, and it has at least three elements. Conversely let \(k=G\cup\{0\}\) be a subfield with at least three elements. Then \(G+G\subseteq k\) and \(0=1+(-1)\in G+G\). For \(c\in G\) choose \(g\in G\) with \(g\neq c\). Then \(c=g+(c-g)\in G+G\). Hence \(G+G=k\).

(b) \(R/G\) is an extension of \(\mathbf{S}\) if and only if \(G+G=G\) and \(G-G=G\cup\{0\}\cup(-G)\). Suppose this holds. Then \(G\) and \(-G\) are disjoint: if \(g=-h\) with \(g,h\in G\), then \(0=g+h\in G\), which is false. The set \(F\) is closed under addition, since \(G+G=G\), \((-G)+(-G)=-G\) and \(G+(-G)=F\). It is closed under multiplication, and it contains \(-1\) and the inverses of its nonzero elements. So \(F\) is a subfield, and \(G\) is an ordering of \(F\). Conversely let \(G\) be an ordering of a subfield \(F\). Then \(G+G=G\), because \(g=g/2+g/2\). And \(G-G=F\), because \(x=2x-x\), \(0=1-1\) and \(-x=x-2x\) for \(x\in G\). □

*Reference:* (a) is [Connes–Consani 2011c, Proposition 2.6], stated there for \(G\ne\{1\}\). [Connes–Consani 2010b, Theorem 4.2] states the criterion for every proper subgroup \(G\) of \(R^\times\); this fails for \(R=\mathbb{F}_4\) and \(G=\{1\}\), where \(G\cup\{0\}=\mathbb{F}_2\) is a subfield and \(R/G=\mathbb{F}_4\) is a field. So we keep the condition on the number of elements. (b) is [Connes–Consani 2011c, Proposition 5.1].

**Examples 3.8.**

(1) Let \(F\supseteq k\) be fields, with \(k\) of at least three elements. Then \(F/k^\times\) is a hyperfield extension of \(\mathbf{K}\). For example \(\mathbb{F}_9/\mathbb{F}_3^\times\) has five elements ([Connes–Consani 2011c, Example 2.7]).

(2) Let \(A\) be a nonzero ring that contains a field \(k\) with at least three elements. Then \(A/k^\times\) is a hyperring extension of \(\mathbf{K}\). The adèle class space of Section 5 is of this kind.

(3) \(\mathbb{C}/\mathbb{R}_{>0}\) is a hyperfield extension of \(\mathbf{S}\). Its nonzero elements are the points of the unit circle ([Connes–Consani 2011c, Example 5.7]).

(4) \(\mathbb{F}_7/\{\pm 1\}\) is a hyperfield with four elements which is an extension neither of \(\mathbf{K}\) nor of \(\mathbf{S}\) (Exercise 3).

**Proposition 3.9 (calculus in extensions of \(\mathbf{K}\)).** Let \(E\) be a canonical hypergroup in which \(x+x=\{0,x\}\) for all \(x\). By the distributive law, this holds for the additive hypergroup of a hyperring extension of \(\mathbf{K}\).

(a) \(-x=x\) for all \(x\).

(b) \(x\in x+y\) if and only if \(y\in\{0,x\}\).

(c) If \(x\neq y\) are nonzero, then \(x+y\) contains none of \(0,x,y\), and it has at least two elements.

(d) \(E\) does not have exactly three or exactly four elements.

*Proof.* (a) \(0\in x+x\). (b) If \(x\in x+y\), then \(y\in x-x=x+x=\{0,x\}\) by (H5). The converse is clear from \(x+0=\{x\}\) and \(x+x=\{0,x\}\). (c) \(0\notin x+y\) by (a) and Lemma 3.2 (b). \(x\notin x+y\) and \(y\notin x+y\) by (b). Suppose \(x+y=\{z\}\). Then \((x+y)+z=z+z=\{0,z\}\). By (H5), \(z\in y+x\) gives \(x\in z-y=y+z\). So \(x+(y+z)\supseteq x+x\ni x\). By (H2), \(x\in\{0,z\}\), so \(x=z\in x+y\). This contradicts (b). (d) By (c), two distinct nonzero elements force two more nonzero elements. □

*Reference:* [Connes–Consani 2011c, Proposition 2.3].

**Proposition 3.10 (extensions of \(\mathbf{S}\)).** Let \(R\) be a hyperring extension of \(\mathbf{S}\).

(a) \(x+x=\{x\}\) and \(x-x=\{-x,0,x\}\) for all \(x\).

(b) \(x\in x+y\) if and only if \(y\in\{0,x,-x\}\).

(c) Write \(x\preceq y\) if \(y=x\) or \(y\in x+1\). This is a partial order on \(R\).

(d) If \(R\neq\{-1,0,1\}\), then \(R\) is infinite.

*Proof.* (a) follows from the distributive law. (b) If \(x\in x+y\), then \(y\in x-x\) by (H5). Conversely \(x\) lies in \(x+0\), in \(x+x\) and in \(x-x\).

(c) Let \(x\preceq y\preceq z\) with \(x\neq y\) and \(y\neq z\). Then \(z\in y+1\subseteq(x+1)+1=x+(1+1)=x+1\). So \(\preceq\) is transitive. Suppose \(x\preceq y\), \(y\preceq x\) and \(x\neq y\). Then \(x\in y+1\subseteq(x+1)+1=x+1\), so \(1\in\{0,x,-x\}\) by (b), and \(x=\pm 1\). In the same way \(y=\pm 1\). So one of \(x,y\) is \(1\) and the other is \(-1\). But \(1\preceq -1\) would mean \(-1\in 1+1=\{1\}\), which is false.

(d) Let \(x\notin\{-1,0,1\}\) and \(x_1\in x+1\). Then \(x_1\neq x\) by (b). Also \(x_1\notin\{-1,0,1\}\): otherwise (H5) gives \(x\in x_1-1\), and the sets \(0-1\), \(1-1\) and \(-1-1\) are contained in \(\{-1,0,1\}\). So \(x\prec x_1\) and \(x_1\notin\{-1,0,1\}\). Repeating this gives \(x\prec x_1\prec x_2\prec\cdots\). By (c) these elements are distinct. □

*Reference:* [Connes–Consani 2011c, Proposition 5.2 and Corollary 5.4]. The corollary there says that every hyperfield extension of \(\mathbf{S}\) is infinite; this needs \(R\neq\mathbf{S}\), and the proof works for hyperrings, as above.

So \(\mathbf{K}\) has finite extensions, such as \(\mathbb{F}_9/\mathbb{F}_3^\times\), and \(\mathbf{S}\) has none except itself.

### 3.4 The tropical hyperfield

**Definition 3.11.** The *tropical hyperfield* \(\mathbf{T}\) is the set \([0,\infty)\) with the usual multiplication and the sums
\[ a\boxplus b=\{\max(a,b)\}\ \text{ if }a\neq b,\qquad a\boxplus a=[0,a]. \]

Equivalently: \(c\in a\boxplus b\) if and only if the largest of the three numbers \(a,b,c\) occurs at least twice among them.

*Reference:* [Lorscheid 2022, §1.8], where the definition is attributed to Viro.

**Theorem 3.12.** \(\mathbf{T}\) is a hyperfield. For \(a,b,c\ge 0\) with maximum \(m\), the set \((a\boxplus b)\boxplus c\) is \([0,m]\) if \(m\) occurs at least twice among \(a,b,c\), and it is \(\{m\}\) otherwise.

*Proof.* We prove the formula first.

*Case \(a\neq b\).* Let \(m'=\max(a,b)\). Then \((a\boxplus b)\boxplus c=m'\boxplus c\). If \(c\neq m'\), this is \(\{\max(m',c)\}=\{m\}\), and \(m\) occurs once among \(a,b,c\). If \(c=m'\), this is \([0,m]\), and \(m\) occurs twice.

*Case \(a=b\).* Then \((a\boxplus b)\boxplus c\) is the union of the sets \(e\boxplus c\) for \(e\in[0,a]\). If \(c>a\), each of these sets is \(\{c\}=\{m\}\), and \(m\) occurs once. If \(c\le a\), the union contains \([0,c]\) (for \(e=c\)), the element \(c\) (for \(e < c\)) and the elements \(e\in(c,a]\). So it is \([0,a]=[0,m]\), and \(m\) occurs at least twice.

The formula is symmetric in \(a,b,c\). With (H1) this gives (H2). (H3): \(a\boxplus 0=\{a\}\) for \(a\neq 0\), and \(0\boxplus 0=\{0\}\). (H4): \(0\in a\boxplus b\) if and only if \(a=b\); so \(-a=a\). (H5): the condition "the largest of \(a,b,c\) occurs at least twice" is symmetric. The distributive law \(c(a\boxplus b)=ca\boxplus cb\) holds for \(c>0\) because multiplication by \(c\) preserves the order, and it is clear for \(c=0\). Every nonzero element is invertible. □

The largest element of \(a\boxplus b\) is \(\max(a,b)\). So the semifield \(\mathbb{R}_+^{\max}\) is obtained from \(\mathbf{T}\) by keeping the largest element of each sum. The hyperfield \(\mathbf{T}\) is not an extension of \(\mathbf{K}\), since \(1\boxplus 1=[0,1]\).

### 3.5 Morphisms from a ring

**Theorem 3.13.** Let \(A\) be a ring.

(a) The map \(f\mapsto\ker f\) is a bijection from the set of morphisms \(A\to\mathbf{K}\) to the set of prime ideals of \(A\). This holds for every hyperring \(A\).

(b) The morphisms \(A\to\mathbf{S}\) correspond bijectively to the pairs \((\mathfrak{p},P)\), where \(\mathfrak{p}\) is a prime ideal of \(A\) and \(P\) is an ordering of the field of fractions of \(A/\mathfrak{p}\). The morphism attached to \((\mathfrak{p},P)\) sends \(a\) to the sign of its image in that field.

(c) The morphisms \(A\to\mathbf{T}\) are the maps \(v:A\to[0,\infty)\) with \(v(0)=0\), \(v(1)=1\), \(v(ab)=v(a)v(b)\) and \(v(a+b)\le\max(v(a),v(b))\) for all \(a,b\).

*Proof.* (a) Let \(A\) be a hyperring and \(f:A\to\mathbf{K}\) a morphism. Then \(\ker f\) is an ideal. It is proper because \(f(1)=1\), and prime because \(f(xy)=f(x)f(y)\). It determines \(f\). Conversely let \(\mathfrak{p}\) be a prime ideal, and let \(f\) be \(0\) on \(\mathfrak{p}\) and \(1\) elsewhere. Then \(f\) is multiplicative, \(f(0)=0\) and \(f(1)=1\). We check that \(f(x+y)\subseteq f(x)+f(y)\). If \(x,y\in\mathfrak{p}\), then \(x+y\subseteq\mathfrak{p}\). If \(x,y\notin\mathfrak{p}\), the right side is \(\{0,1\}\). If \(x\in\mathfrak{p}\) and \(y\notin\mathfrak{p}\), the right side is \(\{1\}\), and we must show that \(x+y\) does not meet \(\mathfrak{p}\). If \(z\in(x+y)\cap\mathfrak{p}\), then \(y\in z-x\subseteq\mathfrak{p}\) by (H5), which is false.

(b) Let \(f:A\to\mathbf{S}\) be a morphism. Its composite with the absolute value \(\mathbf{S}\to\mathbf{K}\) is a morphism with the same kernel. So \(\mathfrak{p}=\ker f\) is a prime ideal, by (a). For \(q\in\mathfrak{p}\) we have \(f(a+q)\in f(a)+0=\{f(a)\}\). So \(f\) induces a map \(\bar f:A/\mathfrak{p}\to\mathbf{S}\). It is a morphism with kernel \(\{0\}\). Let \(F\) be the field of fractions of \(A/\mathfrak{p}\). Put \(\tilde f(a/b)=\bar f(a)\bar f(b)\). This is well defined. Indeed, if \(ad=bc\), then \(\bar f(a)\bar f(d)=\bar f(b)\bar f(c)\); multiplying by \(\bar f(b)\bar f(d)\), whose square is \(1\), gives \(\bar f(a)\bar f(b)=\bar f(c)\bar f(d)\). The map \(\tilde f\) is multiplicative. For \(x=a/b\) and \(y=c/d\),
\[ \tilde f(x+y)=\bar f(ad+bc)\,\bar f(bd)\in\big(\bar f(ad)+\bar f(bc)\big)\bar f(bd)=\bar f(a)\bar f(b)+\bar f(c)\bar f(d)=\tilde f(x)+\tilde f(y). \]
So \(\tilde f:F\to\mathbf{S}\) is a morphism. Put \(P=\tilde f^{-1}(1)\). Then \(PP\subseteq P\), and \(P+P\subseteq P\) because \(1+1=\{1\}\). Since \(\tilde f(-x)=-\tilde f(x)\) and \(\tilde f(x)\neq 0\) for \(x\neq 0\), the field \(F\) is the disjoint union of \(P\), \(\{0\}\) and \(-P\). So \(P\) is an ordering of \(F\), and \(f(a)\) is the sign of the image of \(a\) in \(F\).

Conversely let \((\mathfrak{p},P)\) be given. The sign map of the ordered field \((F,P)\) is the quotient map \(F\to F/P=\mathbf{S}\) of Theorem 3.5. Its composite with \(A\to A/\mathfrak{p}\to F\) is a morphism \(A\to\mathbf{S}\) with kernel \(\mathfrak{p}\). The two constructions are inverse to each other.

(c) Let \(v:A\to\mathbf{T}\) be a morphism. Then \(v(a+b)\in v(a)\boxplus v(b)\subseteq[0,\max(v(a),v(b))]\). Conversely let \(v\) satisfy the four conditions. Since \(v(-1)^2=v(1)=1\), we have \(v(-1)=1\) and \(v(-a)=v(a)\). If \(v(a)=v(b)\), then \(v(a+b)\le v(a)\) says that \(v(a+b)\in v(a)\boxplus v(b)\). If \(v(a)>v(b)\), then
\[ v(a)=v\big((a+b)+(-b)\big)\le\max\big(v(a+b),v(b)\big) \]
forces \(v(a)\le v(a+b)\). Hence \(v(a+b)=v(a)\), which is the only element of \(v(a)\boxplus v(b)\). □

*Reference:* (a) [Connes–Consani 2011c, Proposition 2.9]. (b) [Connes–Consani 2011c, Proposition 2.11]. (c) [Lorscheid 2022, Theorem 2.2], stated there for ordered blueprints and attributed to Viro.

For a field \(F\) this reads as follows. There is one morphism \(F\to\mathbf{K}\). The morphisms \(F\to\mathbf{S}\) are the orderings of \(F\). The morphisms \(F\to\mathbf{T}\) are the nonarchimedean absolute values of \(F\), the trivial one included. There is exactly one morphism \(\mathbb{Z}\to\mathbf{S}\), the sign: a finite field has no ordering, and \(\mathbb{Q}\) has only one. Its composite with the absolute value is the morphism \(\mathbb{Z}\to\mathbf{K}\) with kernel \(\{0\}\). Compare this with the absence of morphisms between \(\mathbb{Z}\) and \(\mathbb{B}\) in Section 1.

Part (c) needs the opposites of a ring: it fails for semirings (Exercise 4).

## 4. Extensions of the Krasner hyperfield and projective geometry

A reference for this section is [Connes–Consani 2011c, §3].

### 4.1 Hypergroups and geometries

**Definition 4.1.** A *\(\mathbf{K}\)-vector space* is a canonical hypergroup \(E\) with \(x+x=\{0,x\}\) for all \(x\). A *projective geometry* is a set \(\mathcal{P}\) of points with a set \(\mathcal{L}\) of subsets of \(\mathcal{P}\), called lines, such that:

- (P1) two distinct points \(x,y\) lie on exactly one line, written \(L(x,y)\);
- (P2) if \(x\neq y\), \(z\notin L(x,y)\), \(t\in L(x,y)\setminus\{x\}\) and \(u\in L(x,z)\setminus\{x\}\), then the lines \(L(t,u)\) and \(L(y,z)\) have a common point;
- (P3′) every line has at least four points.

In (P2) the points \(t\) and \(u\) are distinct: a point \(t=u\neq x\) would lie on \(L(x,y)\) and on \(L(x,z)\), and these lines would be equal by (P1). Axiom (P2) says that a line which meets two sides of a triangle, away from their common vertex, meets the third side. In [Connes–Consani 2011c, §3] the axiom (P3) asks for three points on each line, and (P3′) is its variant with four points. The correspondence below needs four. So in this lesson the words *projective geometry* always include (P3′). A projective space of dimension at least 1 over \(\mathbb{F}_2\) satisfies (P1) and (P2), but its lines have three points, so it is not a projective geometry in this sense.

The name \(\mathbf{K}\)-vector space is that of [Connes–Consani 2011c]: \(\mathbf{K}\) acts on \(E\) by \(0\cdot x=0\) and \(1\cdot x=x\). Proposition 3.9 applies to every \(\mathbf{K}\)-vector space.

**Theorem 4.2.** (a) Let \(E\) be a \(\mathbf{K}\)-vector space and \(\mathcal{P}=E\setminus\{0\}\). The sets \(L(x,y)=(x+y)\cup\{x,y\}\), for \(x\ne y\) in \(\mathcal{P}\), are the lines of a projective geometry on \(\mathcal{P}\): they satisfy (P1), (P2) and (P3′).

(b) Let \((\mathcal{P},\mathcal{L})\) be a projective geometry, that is, a set of points with lines that satisfy (P1), (P2) and (P3′), and let \(E=\mathcal{P}\cup\{0\}\). Put \(x+0=0+x=\{x\}\), \(x+x=\{0,x\}\), and \(x+y=L(x,y)\setminus\{x,y\}\) for \(x\neq y\) in \(\mathcal{P}\). Then \(E\) is a \(\mathbf{K}\)-vector space.

(c) These two constructions are inverse to each other.

*Proof.* (a) Let \(x\neq y\) in \(\mathcal{P}\). By Proposition 3.9 (c), \(x+y\) is contained in \(\mathcal{P}\setminus\{x,y\}\) and has at least two elements. So \(L(x,y)\subseteq\mathcal{P}\) has at least four points. This is (P3′).

*Claim.* If \(z\in L(x,y)\) and \(z\neq x\), then \(L(x,z)=L(x,y)\). This is clear for \(z=y\). Let \(z\in x+y\). By (H5), \(y\in z-x=x+z\). Then
\[ x+y\subseteq x+(x+z)=(x+x)+z=\{0,x\}+z=\{z\}\cup(x+z). \]
So \(L(x,y)\subseteq L(x,z)\). Since \(y\in x+z\), the same argument with \(y\) and \(z\) exchanged gives \(L(x,z)\subseteq L(x,y)\).

Now let \(a\neq b\) be two points of a line \(L(x,y)\). If \(a\neq x\), the claim gives \(L(x,y)=L(x,a)=L(a,x)\). Then \(b\in L(a,x)\) and \(b\neq a\), so \(L(a,x)=L(a,b)\) by the claim. If \(a=x\), the claim gives \(L(x,y)=L(x,b)=L(a,b)\). So every line through \(a\) and \(b\) is equal to \(L(a,b)\). This is (P1).

For (P2), let \(x,y,z,t,u\) be as in the axiom. If \(t=y\), then \(y\) is a common point; if \(u=z\), then \(z\) is one. Otherwise \(t\in x+y\) and \(u\in x+z\), so \(x\in t+y\) and \(x\in u+z\) by (H5). Hence
\[ 0\in x+x\subseteq(t+y)+(u+z)=(t+u)+(y+z). \]
By Lemma 3.2 (d), and because \(-w=w\) for all \(w\), the sets \(t+u\) and \(y+z\) have a common element. As \(t\neq u\) and \(y\neq z\), these sets are contained in \(L(t,u)\) and \(L(y,z)\).

(b) The operation is commutative, \(0\) is neutral, and \(0\in x+y\) only for \(y=x\). So (H1), (H3) and (H4) hold, with \(-x=x\), and \(x+x=\{0,x\}\).

(H5). Let \(x\in y+z\); we show \(z\in x+y\). If \(y=0\), then \(x=z\). If \(z=0\), then \(x=y\) and \(0\in x+x\). If \(y=z\neq 0\), then \(x\in\{0,y\}\), and \(z=y\) lies in \(0+y\) and in \(y+y\). If \(y\neq z\) are nonzero, then \(x\in L(y,z)\setminus\{y,z\}\). So \(L(x,y)=L(y,z)\) by (P1), and \(z\in L(x,y)\setminus\{x,y\}=x+y\).

(H2). Put \(\Phi(x,y,z)=(x+y)+z\). It is enough to show that \(\Phi\) does not change when \(x,y,z\) are permuted: then \(x+(y+z)=\Phi(y,z,x)=\Phi(x,y,z)\) by (H1). This is clear if one of the three elements is \(0\). Let \(x,y,z\in\mathcal{P}\).

*Case 1: \(x=y=z\).* There is nothing to prove.

*Case 2: exactly two of them are equal.* Say the elements are \(x,x,z\) with \(x\neq z\), and let \(L=L(x,z)\). Then \(\Phi(x,x,z)=\{0,x\}+z=\{z\}\cup(L\setminus\{x,z\})=L\setminus\{x\}\). And \(\Phi(x,z,x)=\Phi(z,x,x)=(x+z)+x\) is the union of the sets \(w+x=L\setminus\{w,x\}\) for \(w\in L\setminus\{x,z\}\). By (P3′) there are at least two such \(w\). So this union is \(L\setminus\{x\}\).

*Case 3: \(x,y,z\) are distinct and on one line \(L\).* Then \(\Phi(x,y,z)\) is the union of \(z+z=\{0,z\}\) and of the sets \(w+z=L\setminus\{w,z\}\) for \(w\in L\setminus\{x,y,z\}\). If \(L\) has at least five points, this union is \(L\cup\{0\}\). If \(L\) has exactly four points \(x,y,z,w\), it is \(\{0,x,y,z\}\). Both are symmetric in \(x,y,z\).

*Case 4: \(x,y,z\) are not on one line.* We show that \(\Phi(x,y,z)\subseteq\Phi(y,z,x)\). Applying this three times gives \(\Phi(x,y,z)\subseteq\Phi(y,z,x)\subseteq\Phi(z,x,y)\subseteq\Phi(x,y,z)\). Also \(\Phi(x,y,z)=\Phi(y,x,z)\) by (H1). So \(\Phi\) is symmetric.

Let \(p\in\Phi(x,y,z)\). There is \(w\in L(x,y)\setminus\{x,y\}\) with \(p\in L(w,z)\setminus\{w,z\}\). First, \(p\) is on none of the lines \(L(x,y)\), \(L(y,z)\), \(L(x,z)\). If \(p\in L(x,y)\), then \(L(x,y)\) contains the two points \(w,p\) of \(L(w,z)\), so \(L(x,y)=L(w,z)\ni z\), which is excluded. If \(p\in L(y,z)\), then \(L(y,z)=L(p,z)=L(w,z)\ni w\); so \(L(y,z)\) contains \(w\) and \(y\), hence equals \(L(x,y)\), which is excluded. The same argument works for \(L(x,z)\).

Now apply (P2) to the three points \(w,y,z\), with \(t=x\) and \(u=p\). This is allowed: \(z\notin L(w,y)=L(x,y)\), \(x\in L(w,y)\setminus\{w\}\) and \(p\in L(w,z)\setminus\{w\}\). So the lines \(L(x,p)\) and \(L(y,z)\) have a common point \(v\). Then \(v\neq y\), because otherwise \(L(x,p)=L(x,y)\ni p\). Also \(v\neq z\), because otherwise \(L(x,p)=L(x,z)\ni p\). And \(v\neq x\), \(v\neq p\), because \(x\) and \(p\) are not on \(L(y,z)\). So \(v\in y+z\) and \(p\in L(v,x)\setminus\{v,x\}=v+x\). Hence \(p\in(y+z)+x=\Phi(y,z,x)\).

(c) If the geometry is built from \(E\) as in (a), then \(L(x,y)\setminus\{x,y\}=x+y\), because \(x,y\notin x+y\). If \(E\) is built from the geometry as in (b), then \((x+y)\cup\{x,y\}=L(x,y)\), and every line of the geometry is of this form, because it has at least two points. □

The proof of (b) uses (P1) throughout, (P2) only in Case 4, and (P3′) in Cases 2 and 3. With only three points on a line, (b) fails (Exercise 5).

*Reference:* [Connes–Consani 2011c, Proposition 3.1], which attributes the correspondence to Prenowitz and to Lyndon [Lyndon 1961].

**Example 4.3 (projective spaces).** Let \(k\) be a field with at least three elements and \(V\) a vector space over \(k\). The group \(k^\times\) acts on \((V,+)\) by automorphisms, so \(V/k^\times\) is a canonical hypergroup by Lemma 3.4. As \(k^\times+k^\times=k\), we get \([x]+[x]=\{[(g+h)x]:g,h\in k^\times\}=\{[0],[x]\}\). So \(V/k^\times\) is a \(\mathbf{K}\)-vector space. Its nonzero elements are the points of the projective space \(\mathbb{P}(V)\). For two distinct points \([x],[y]\) the vectors \(x,y\) are linearly independent, and
\[ L([x],[y])=\{[gx+hy]:g,h\in k^\times\}\cup\{[x],[y]\} \]
is the set of points of the projective line spanned by \(x\) and \(y\). So the geometry of \(V/k^\times\) is that of \(\mathbb{P}(V)\). Its lines have \(|k|+1\ge 4\) points.

For \(k=\mathbb{F}_2\) the lines of \(\mathbb{P}(V)\) have three points, and the construction of Theorem 4.2 (b) does not give a hypergroup (Exercise 5). This matches the condition "at least three elements" in Proposition 3.7: \(V/\mathbb{F}_2^\times=V\) is a group, in which \(x+x=\{0\}\).

### 4.2 Hyperfields and geometries on groups

**Theorem 4.4.** Let \(G\) be an abelian group.

(a) Let \(H\) be a hyperfield extension of \(\mathbf{K}\) with \(H^\times=G\). Then for every \(g\in G\) the translation \(x\mapsto gx\) maps each line of the geometry of \(H\) onto a line.

(b) Conversely, suppose given a projective geometry with set of points \(G\), such that every translation maps each line onto a line. Then \(H=G\cup\{0\}\), with the multiplication of \(G\) extended by \(0\cdot x=0\) and with the sums of Theorem 4.2 (b), is a hyperfield extension of \(\mathbf{K}\).

(c) This gives a bijection between the hyperfield structures on the monoid \(G\cup\{0\}\) that are extensions of \(\mathbf{K}\), and the projective geometries on the set \(G\) that are invariant under translations.

*Proof.* (a) By the distributive law, \(gL(x,y)=g(x+y)\cup\{gx,gy\}=(gx+gy)\cup\{gx,gy\}=L(gx,gy)\).

(b) By Theorem 4.2, \((H,+)\) is a \(\mathbf{K}\)-vector space, and \(1+1=\{0,1\}\). It remains to check that \(g(x+y)=gx+gy\). This is clear if \(g=0\), \(x=0\), \(y=0\) or \(x=y\). Otherwise \(gL(x,y)\) is a line through \(gx\) and \(gy\). So it is \(L(gx,gy)\), and removing \(gx\) and \(gy\) gives \(g(x+y)=gx+gy\).

(c) This follows from (a), (b) and Theorem 4.2 (c). □

*Reference:* [Connes–Consani 2011c, Lemma 3.5], which also covers groups that are not commutative.

In other words: a hyperfield extension of \(\mathbf{K}\) is a projective geometry together with an abelian group that acts on the points simply transitively and maps lines onto lines, and a base point.

**Examples 4.5.**

(1) *One line.* Let \(G\) be an abelian group with at least four elements. Take \(G\) itself as the only line. Then (P1) and (P3′) hold, (P2) is empty, and translations preserve the line. The hyperfield of Theorem 4.4 has the sums \(x+y=G\setminus\{x,y\}\) for \(x\neq y\) in \(G\). It is written \(\mathbf{K}[G]\) in [Connes–Consani 2011c, Proposition 3.6]. Together with \(\mathbf{K}\) itself, this gives a hyperfield extension of \(\mathbf{K}\) with \(n\) elements for \(n=2\) and for every \(n\ge 5\). By Proposition 3.9 (d) there is none with three or four elements.

(2) For a prime power \(q\ge 3\), the hyperfield \(\mathbb{F}_{q^2}/\mathbb{F}_q^\times\) is \(\mathbf{K}[G]\) for a cyclic group \(G\) of order \(q+1\). Indeed its geometry is the projective line over \(\mathbb{F}_q\), a single line with \(q+1\) points, and its group of units \(\mathbb{F}_{q^2}^\times/\mathbb{F}_q^\times\) is cyclic of order \(q+1\).

(3) *A hyperfield that is not a quotient.* Let \(G=(\mathbb{Z}/2\mathbb{Z})^2\). The hyperfield \(\mathbf{K}[G]\) has five elements. It is not isomorphic to a quotient \(R/\Gamma\) of a ring by a group of units. Suppose it is. By Theorem 3.5 (b), \(R\) is a field. By Proposition 3.7 (a), \(k=\Gamma\cup\{0\}\) is a subfield, and \(R^\times/k^\times\) is isomorphic to \(G\). Choose \(x\in R\setminus k\). The classes \([1+cx]\), \(c\in k\), are distinct, because \(1\) and \(x\) are linearly independent over \(k\). So \(k\) is finite. Then \(R^\times\), a union of four classes of \(k^\times\), is finite, and \(R\) is a finite field. But the group of units of a finite field is cyclic, and so are its quotients; \(G\) is not cyclic.

**Example 4.6 (a plane).** Let \(F=\mathbb{F}_{27}=\mathbb{F}_3[g]\) with \(g^3=g-1\). (The polynomial \(t^3-t+1\) has no root in \(\mathbb{F}_3\), so it is irreducible.) Then \(g^9=(g-1)^3=g^3-1=g+1\) and \(g^{13}=g^9g^3g=(g+1)(g-1)g=g^3-g=-1\). So \(g\) has order \(26\) and generates \(F^\times\). Let \(H=F/\mathbb{F}_3^\times\) and \(e=[g]\). Then \(H^\times=\{e^i:i\in\mathbb{Z}/13\mathbb{Z}\}\), and \(H\) has \(14\) elements. Its geometry is the projective plane over \(\mathbb{F}_3\), with \(13\) points and four points on each line. Since \(1+g=g^9\) and \(1-g=-g^3\),
\[ e^0+e^1=\{e^3,e^9\},\qquad L(e^0,e^1)=\{e^i:i\in D\},\quad D=\{0,1,3,9\}. \]
By Theorem 4.4 (a) the translates \(D+i\) are lines. Every nonzero class modulo \(13\) is a difference of two elements of \(D\) in exactly one way: the twelve differences are \(\pm1,\pm3,\pm9,\pm2,\pm8,\pm6\), that is \(1,12,3,10,9,4,2,11,8,5,6,7\). So two distinct points \(e^a,e^b\) lie on exactly one translate \(D+i\). This translate is the line through them, and \(e^a+e^b\) consists of its two other points. For example \(2=3-1\), so \(0\) and \(2\) lie in \(D-1=\{12,0,2,8\}\), and \(e^0+e^2=\{e^8,e^{12}\}\). One can check this in \(F\): \(1+g^2=-g^8\) and \(1-g^2=-g^{12}\).

### 4.3 What is known about all extensions

A projective geometry is *Desarguesian* if Desargues's theorem on triangles in perspective holds in it. It has *dimension at least 2* if it contains three points that are not on one line. The lesson quotes the following results without proof.

**Theorem 4.7** ([Connes–Consani 2011c, Theorem 3.8]). Let \(H\) be a hyperfield extension of \(\mathbf{K}\). Assume that the geometry of \(H\) is Desarguesian and of dimension at least 2. Then there are a field \(F\) and a subfield \(k\) of \(F\) with \(H\cong F/k^\times\), and the pair \((F,k)\) is unique.

The proof in [Connes–Consani 2011c] rests on Karzel's classification of commutative incidence groups. The same work notes that the Desargues condition holds automatically when the geometry has dimension at least three. Example 4.5 (3) shows that the hypothesis on the dimension cannot be dropped.

*Finite extensions.* By [Connes–Consani 2011c, Theorem 3.11], a finite hyperfield extension \(H\) of \(\mathbf{K}\) is of one of three kinds: \(H=\mathbf{K}[G]\) for a finite abelian group \(G\); or \(H=\mathbb{F}_{q^m}/\mathbb{F}_q^\times\) (for \(m=1\) and \(q\ge 3\) this is \(\mathbf{K}\) itself); or the geometry of \(H\) is a finite non-Desarguesian projective plane, on which \(H^\times\) acts simply transitively by collineations. According to [Connes–Consani 2011c, Remark 3.12] no example of the third kind is known.

*Infinite extensions.* [Connes–Consani 2011c, Example 4.7] obtains, from a theorem of Hall on difference sets in \(\mathbb{Z}\), hyperfield extensions \(H\) of \(\mathbf{K}\) with \(H^\times\cong\mathbb{Z}\) whose geometry is a non-Desarguesian plane. Example 4.6 is the finite model of this construction.

*Morphisms.* [Connes–Consani 2011c, Theorem 3.13] states the following. Let \(A_1\) and \(A_2\) be algebras over fields \(k_1\) and \(k_2\) different from \(\mathbb{F}_2\), and let \(\rho:A_1/k_1^\times\to A_2/k_2^\times\) be a morphism of hyperrings whose image contains three points that are not on one line (in the words of that work: the range of \(\rho\) has \(\mathbf{K}\)-dimension greater than 2). Then \(\rho\) is induced by a unique ring homomorphism \(\tilde\rho:A_1\to A_2\), and \(\tilde\rho\) maps \(k_1\) into \(k_2\). The proof uses the description of morphisms of projective geometries by semilinear maps due to Faure and Frölicher. The hypothesis on the image cannot be dropped: [Connes–Consani 2011c, Remark 3.16] gives the maps induced by \(x\mapsto x^n\), \(n\ge 3\) odd, on \((\mathbb{Q}\times\mathbb{Q})/\mathbb{Q}^\times\); they are morphisms of hyperrings, their image lies on one line, and they are not induced by a ring homomorphism.

## 5. The adèle class space

A reference for this section is [Connes–Consani 2011c, §7].

Let \(k\) be a global field: a finite extension of \(\mathbb{Q}\), or of \(\mathbb{F}_p(t)\). Let \(\Sigma_k\) be its set of places, \(k_v\) the completion of \(k\) at the place \(v\), and \(\mathcal{O}_v=\{x\in k_v:|x|_v\le 1\}\) for a nonarchimedean place \(v\). The *adèle ring* \(\mathbb{A}_k\) is the set of families \(a=(a_v)_{v\in\Sigma_k}\) with \(a_v\in k_v\) for all \(v\) and \(a_v\in\mathcal{O}_v\) for all but finitely many \(v\). Addition and multiplication are defined componentwise. We use the following facts, which follow from the definitions; for idèles and the topology of restricted products see [Milne CFT, Chapter V, Section 4].

- The diagonal map embeds \(k\) in \(\mathbb{A}_k\) as a subfield.
- The units of \(\mathbb{A}_k\) are the *idèles*: the families with \(a_v\neq 0\) for all \(v\) and \(|a_v|_v=1\) for all but finitely many \(v\).
- \(\mathbb{A}_k\) is a topological ring. A subset is a neighbourhood of \(0\) if and only if it contains a set \(\prod_{v\in S}U_v\times\prod_{v\notin S}\mathcal{O}_v\), where \(S\) is a finite set of places that contains the archimedean ones, and \(U_v\) is a neighbourhood of \(0\) in \(k_v\).

For \(E\subseteq\Sigma_k\) let \(1_E\) be the adèle with components \(1\) at the places of \(E\) and \(0\) elsewhere. Write \(1_v=1_{\{v\}}\). The *idèle class group* is \(C_k=\mathbb{A}_k^\times/k^\times\). The *adèle class space* is the set \(\mathbb{H}_k=\mathbb{A}_k/k^\times\) of orbits of \(k^\times\) acting on \(\mathbb{A}_k\) by multiplication. Let \(\pi:\mathbb{A}_k\to\mathbb{H}_k\) be the quotient map. We give \(\mathbb{H}_k\) the quotient topology. For \(x=\pi(a)\) the condition \(a_w=0\) depends only on \(x\); we write it \(x_w=0\).

**Theorem 5.1.** (a) \(\mathbb{H}_k\), with the operations of Theorem 3.5, is a hyperring extension of \(\mathbf{K}\). In particular \(x+x=\{0,x\}\) for every \(x\in\mathbb{H}_k\).

(b) Its group of units is \(C_k\).

(c) The nonzero elements of \(\mathbb{H}_k\) are the points of the projective space of the \(k\)-vector space \(\mathbb{A}_k\). For nonzero \(x\neq y\), the set \(x+y\) consists of the points of the line through \(x\) and \(y\), other than \(x\) and \(y\).

*Proof.* (a) and (b) follow from Theorem 3.5 and Proposition 3.7 (a), since \(k\) is an infinite subfield of \(\mathbb{A}_k\). (c) is Example 4.3. □

*Reference:* [Connes–Consani 2011c, Theorem 7.1].

So the sums of \(\mathbb{H}_k\) record the projective geometry of \(\mathbb{A}_k\) over \(k\). By the result on morphisms quoted in Section 4.3, this geometry keeps a large part of the ring structure of the adèles. [Connes–Consani 2011c, Theorem 7.5] makes this precise for \(k=\mathbb{Q}\): a morphism \(\rho:\mathbb{Z}[T]\to\mathbb{H}_\mathbb{Q}\) is either of the form \(P\mapsto\pi(P(a))\) for a unique adèle \(a\), or it factors through \((\mathbb{Q}+\mathbb{Q}\,1_E)/\mathbb{Q}^\times\) for a set \(E\) of places. The lesson does not prove this.

**Theorem 5.2.** For \(Z\subseteq\Sigma_k\) let \(J_Z=\{a\in\mathbb{A}_k:a_v=0\text{ for all }v\in Z\}\).

(a) The map \(Z\mapsto J_Z\) is a bijection from the set of subsets of \(\Sigma_k\) to the set of closed ideals of \(\mathbb{A}_k\). Moreover \(J_Z=1_E\,\mathbb{A}_k\) with \(E=\Sigma_k\setminus Z\).

(b) The ideal \(J_Z\) is prime if and only if \(Z\) has exactly one element. So the closed prime ideals of \(\mathbb{A}_k\) are the ideals \(\mathfrak{p}_w=J_{\{w\}}\), \(w\in\Sigma_k\).

(c) The closed prime ideals of the hyperring \(\mathbb{H}_k\) are the sets \(\pi(\mathfrak{p}_w)=\{x\in\mathbb{H}_k:x_w=0\}\). They are in bijection with the places of \(k\).

*Proof.* (a) \(J_Z\) is an ideal. It is closed: if \(a_w\neq 0\) for some \(w\in Z\), choose a neighbourhood \(U_w\) of \(0\) in \(k_w\) that does not contain \(-a_w\), and a neighbourhood \(N\) of \(0\) as above with \(w\in S\) and this \(U_w\); then \(a+N\) does not meet \(J_Z\). Different \(Z\) give different \(J_Z\), because \(1_v\in J_Z\) exactly when \(v\notin Z\).

Let \(J\) be a closed ideal. Let \(E\) be the set of places \(v\) such that \(a_v\neq 0\) for some \(a\in J\). For \(v\in E\) choose such an \(a\). Then \(1_v=ab\in J\), where \(b\) has component \(a_v^{-1}\) at \(v\) and \(0\) elsewhere. So \(1_F=\sum_{v\in F}1_v\in J\) for every finite \(F\subseteq E\). We show that \(1_E\) is in the closure of \(J\). Let \(N=\prod_{v\in S}U_v\times\prod_{v\notin S}\mathcal{O}_v\) be a neighbourhood of \(0\) as above, and let \(F=S\cap E\). Then \(1_F-1_E=-1_{E\setminus F}\) has component \(0\) at every place of \(S\), and component \(0\) or \(-1\) elsewhere. So it lies in \(N\), and \(1_F\in 1_E+N\). Since \(J\) is closed, \(1_E\in J\). Every element of \(J\) vanishes outside \(E\), so \(J\subseteq J_Z\) with \(Z=\Sigma_k\setminus E\). Conversely every \(a\in J_Z\) satisfies \(a=a\,1_E\in J\). So \(J=J_Z=1_E\,\mathbb{A}_k\).

(b) \(J_\emptyset=\mathbb{A}_k\) is not prime. If \(Z\) contains two places \(w\neq w'\), then \(1_w1_{w'}=0\in J_Z\), and \(1_w,1_{w'}\notin J_Z\). The ideal \(\mathfrak{p}_w\) is the kernel of the projection \(\mathbb{A}_k\to k_w\) to a field, so it is prime.

(c) By Theorem 3.5 (c), \(J\mapsto\pi(J)\) is a bijection from the prime ideals of \(\mathbb{A}_k\) to the prime ideals of \(\mathbb{H}_k\), and \(\pi^{-1}(\pi(J))=J\). By the definition of the quotient topology, \(\pi(J)\) is closed exactly when \(J\) is closed. □

*Reference:* [Connes–Consani 2011c, Propositions 7.2 and 7.3].

The ring \(\mathbb{A}_k\) has other prime ideals, which are not closed. For example, the adèles with finitely many nonzero components form a proper ideal. A maximal ideal that contains it is prime and contains every \(1_v\). So it is none of the \(\mathfrak{p}_w\).

**Remark 5.3 (the role of the addition).** Forget the sums and keep only the multiplicative monoid of \(\mathbb{H}_k\). In *Commutative monoids and their spectra*, a prime ideal of a monoid \(M\) is a subset \(I\ne M\) with \(0\in I\) and \(MI\subseteq I\), such that \(ab\in I\) implies \(a\in I\) or \(b\in I\). For every nonempty set \(Z\) of places, the union of the \(\pi(\mathfrak{p}_w)\), \(w\in Z\), is a prime ideal of the monoid \(\mathbb{H}_k\). If \(Z\) contains two places \(w\ne w'\), it is not an ideal of the hyperring. Indeed choose \(c\in k\) with \(c\neq 0,-1\). The sum \(\pi(1_{\Sigma_k\setminus\{w\}})+\pi(1_{\Sigma_k\setminus\{w'\}})\) contains the class of \(1_{\Sigma_k\setminus\{w\}}+c\,1_{\Sigma_k\setminus\{w'\}}\). The components of this adèle are \(c\) at \(w\), \(1\) at \(w'\) and \(1+c\) elsewhere. None of them is \(0\). So the sums are what reduces the closed prime ideals to the places.

*Reference:* [Connes–Consani 2011c, Remark 7.4].

**Theorem 5.4 (prime elements).** An element \(x\) of \(\mathbb{H}_k\) is *prime* if the ideal \(x\mathbb{H}_k\) is prime. For a place \(w\) let \(\varpi_w=\pi(1_{\Sigma_k\setminus\{w\}})\).

(a) Every principal prime ideal of \(\mathbb{H}_k\) is one of the \(\pi(\mathfrak{p}_w)\), and \(\pi(\mathfrak{p}_w)=\varpi_w\mathbb{H}_k\).

(b) The prime elements of \(\mathbb{H}_k\) are the elements \(u\varpi_w\) with \(u\in C_k\) and \(w\in\Sigma_k\). The place \(w\) is determined by the element: it is the only place where the element vanishes.

(c) \(u\varpi_w=u'\varpi_w\) if and only if \(u^{-1}u'\) lies in the image of \(k_w^\times\) in \(C_k\). Here \(k_w^\times\) is embedded in the idèles at the place \(w\), with components \(1\) elsewhere.

(d) \((u\varpi_w)(u'\varpi_w)=uu'\varpi_w\). So the prime elements over a place \(w\) form a group, isomorphic to \(C_k/k_w^\times\), with unit \(\varpi_w\). The product of two prime elements over different places is not prime.

*Proof.* For an adèle \(a\) we have \(\pi(a)\mathbb{H}_k=\pi(a\mathbb{A}_k)\). By Theorem 3.5 (c), \(\pi(a)\) is prime if and only if \(a\mathbb{A}_k\) is a prime ideal of \(\mathbb{A}_k\). Let \(a\) be such an adèle and let \(S=\{v:a_v\neq 0\}\).

*Step 1: \(|a_v|_v=1\) for all but finitely many \(v\in S\).* Since \(a\) is an adèle, \(|a_v|_v\le 1\) for all but finitely many \(v\). Suppose that the set \(Y\) of nonarchimedean \(v\in S\) with \(|a_v|_v < 1\) is infinite. Split \(Y\) into two infinite subsets \(Y'\) and \(Y''\). Let \(y\) have components \(a_v\) for \(v\in Y'\) and \(1\) elsewhere. Let \(z\) have components \(1\) for \(v\in Y'\) and \(a_v\) elsewhere. These are adèles and \(yz=a\). As \(a\mathbb{A}_k\) is prime, \(y=ab\) or \(z=ab\) for some adèle \(b\). If \(y=ab\), then \(b_v=a_v^{-1}\) for \(v\in Y''\), so \(|b_v|_v>1\) at infinitely many places. This is impossible. If \(z=ab\), the same happens on \(Y'\).

*Step 2.* Let \(u\) have components \(a_v\) for \(v\in S\) and \(1\) for \(v\notin S\). By Step 1, \(u\) is an idèle, and \(a=u\,1_S\). So \(a\mathbb{A}_k=1_S\mathbb{A}_k=J_{\Sigma_k\setminus S}\). By Theorem 5.2 (b) this ideal is prime exactly when \(\Sigma_k\setminus S\) is a single place \(w\). So the adèles \(a\) with \(a\mathbb{A}_k\) prime are the \(u\,1_{\Sigma_k\setminus\{w\}}\) with \(u\) an idèle, and \(w\) is the only place where \(a\) vanishes. This proves (a) and (b).

(c) Let \(j,j'\) be idèles. Then \(\pi(j)\varpi_w=\pi(j')\varpi_w\) means that there is \(q\in k^\times\) with \(j_v=qj'_v\) for all \(v\neq w\). This says that the idèle \(j(qj')^{-1}\) has all its components equal to \(1\), except at \(w\).

(d) \(\varpi_w^2=\varpi_w\). With (b) and (c), \(u\mapsto u\varpi_w\) induces a bijection from \(C_k/k_w^\times\) to the set of prime elements over \(w\), and it turns products into products. If \(w\neq w'\), the product \(u\varpi_w\,u'\varpi_{w'}\) vanishes at two places, so it is not prime by (b). □

*Reference:* [Connes–Consani 2011c, Theorem 7.9 and Proposition 7.10]. There the set \(P(\mathbb{H}_k)\) of prime elements, with this partial multiplication, is called a groupoid; its units are the \(\varpi_w\).

*Function fields.* Let \(k\) have characteristic \(p>0\), with field of constants \(\mathbb{F}_q\), and let \(X\) be the smooth projective curve over \(\mathbb{F}_q\) with function field \(k\). Let \(k^{\mathrm{ab}}\) be a maximal abelian extension of \(k\), and let \(W\) be the group of elements of \(\mathrm{Gal}(k^{\mathrm{ab}}/k)\) that act on the algebraic closure of \(\mathbb{F}_q\) by an integral power of the Frobenius. The valuations of \(k^{\mathrm{ab}}\) are the points of a cover \(X^{\mathrm{ab}}\to X\). Consider the pairs of valuations of \(k^{\mathrm{ab}}\) with the same restriction to \(k\), modulo the diagonal action of \(W\); they form a groupoid, the loop groupoid of the cover. [Connes–Consani 2011c, Theorem 7.12] states that this groupoid is canonically isomorphic to \(P(\mathbb{H}_k)\), and that the isomorphism is compatible with the actions of \(W\) and of \(C_k\), which class field theory identifies. The lesson does not prove this.

The adèle class space returns in *The arithmetic site* and *The scaling site*.

## 6. The entropy formula and the Witt construction in characteristic one

Basic references for this section are [Connes 2011] and [Connes–Consani 2011b, §2].

### 6.1 The model: Teichmüller representatives

Let \(p\) be a prime number, \(A\) a perfect ring of characteristic \(p\), and \(W(A)\) its ring of Witt vectors, with the multiplicative Teichmüller map \(\tau:A\to W(A)\). Every element of \(W(A)\) is a series \(\sum_n\tau(x_n)p^n\). The map \(\tau\) is not additive. [Connes 2011, Theorem 3.4] writes its defect as
\[ \tau(x)+\tau(y)=\tilde\tau\Big(\sum_{\alpha\in I_p}w_p(\alpha)\,x^\alpha y^{1-\alpha}\Big). \]
Here \(I_p\) is the set of rational numbers in \([0,1]\) whose denominator is a power of \(p\), the coefficients \(w_p(\alpha)\in\mathbb{F}_p[[T]]\) depend only on \(p\), and \(\tilde\tau(\sum a_nT^n)=\sum\tau(a_n)p^n\). The lesson does not prove or use this formula. It is the model for what follows: the addition of a richer structure is written with the "fractional powers" \(x^\alpha y^{1-\alpha}\) of a perfect structure.

In characteristic one the perfect structure is \(\mathbb{R}_+^{\max}\), the sum is a supremum, and the coefficients turn out to be \(w(\alpha)=e^{TS(\alpha)}\), where \(S\) is the entropy function.

### 6.2 Entropy and the variational formula

For \(p=(p_1,\dots,p_n)\) with \(p_i\ge 0\) and \(\sum_ip_i=1\), put \(S(p)=-\sum_ip_i\log p_i\), with \(0\log 0=0\). For \(\alpha\in[0,1]\) put \(S(\alpha)=S(\alpha,1-\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)\).

**Lemma 6.1.** Let \(a_1,\dots,a_n\) be real numbers. For every \(p\) as above,
\[ S(p)+\sum_ip_ia_i\le\log\sum_ie^{a_i}, \]
with equality if and only if \(p_i=e^{a_i}/\sum_je^{a_j}\) for all \(i\). The supremum of the left side over the \(p\) with rational coordinates is \(\log\sum_ie^{a_i}\).

*Proof.* Let \(I_0=\{i:p_i>0\}\). The logarithm is strictly concave. By Jensen's inequality,
\[ S(p)+\sum_ip_ia_i=\sum_{i\in I_0}p_i\log\frac{e^{a_i}}{p_i}\le\log\sum_{i\in I_0}e^{a_i}\le\log\sum_ie^{a_i}. \]
The first inequality is an equality if and only if \(e^{a_i}/p_i\) is the same for all \(i\in I_0\). The second is an equality if and only if \(I_0\) contains every index. Together these say that \(p_i=e^{a_i}/\sum_je^{a_j}\). The left side is a continuous function of \(p\), and the points with rational coordinates are dense. □

*Reference:* for \(n=2\), [Connes–Consani 2011b, Lemma 2.19] and [Connes 2011, Lemma 6.7].

Taking exponentials, the lemma says the following. For \(T>0\) and \(x_1,\dots,x_n\ge 0\),
\[ \sup_p\ e^{TS(p)}\prod_ix_i^{p_i}=\Big(\sum_ix_i^{1/T}\Big)^T, \tag{6.1} \]
where \(p\) runs over the rational points of the simplex and \(0^0=1\). Indeed, if all \(x_i\) are positive, apply the lemma to \(a_i=(\log x_i)/T\) and multiply by \(T\). If some \(x_i\) are \(0\), the terms with \(p_i>0\) for such an \(i\) vanish, and the other terms are those of the same formula for the positive \(x_i\).

### 6.3 Deformed additions on \(\mathbb{R}_+^{\max}\)

**Definition 6.2.** Let \(\bar I=\mathbb{Q}\cap[0,1]\) and \(I=\mathbb{Q}\cap(0,1)\). A *weight* is a function \(s:\bar I\to\mathbb{R}\) which is bounded above, with \(s(0)=s(1)=0\). For \(x,y\in[0,\infty)\) put
\[ x+_sy=\sup_{\alpha\in\bar I}\ e^{s(\alpha)}x^\alpha y^{1-\alpha}, \]
where \(x^\alpha y^{1-\alpha}\) means \(y\) for \(\alpha=0\) and \(x\) for \(\alpha=1\).

In \(\mathbb{R}_+^{\max}\) sums are suprema. So \(x+_sy\) is the sum \(\sum_{\alpha\in\bar I}w(\alpha)x^\alpha y^{1-\alpha}\) with \(w=e^s\), computed in \(\mathbb{R}_+^{\max}\). This is the expression studied in [Connes 2011, §5]. The supremum is finite, because \(s\) is bounded above and \(x^\alpha y^{1-\alpha}\le\max(x,y)\).

**Lemma 6.3.** Let \(s\) be a weight, \(x,y,z\ge 0\) and \(\lambda>0\).

(a) \(x+_s0=x=0+_sx\).

(b) \((x+_sy)z=xz+_syz\).

(c) \(x+_sy\ge\max(x,y)\). Equality holds for all \(x,y\) if and only if \(s\le 0\).

(d) \((x+_sy)^\lambda=x^\lambda+_{\lambda s}y^\lambda\).

*Proof.* (a) If \(y=0\), only the term \(\alpha=1\) is nonzero. (b) \(z=z^\alpha z^{1-\alpha}\). (c) The terms \(\alpha=0\) and \(\alpha=1\) are \(y\) and \(x\). If \(s\le 0\), every term is at most \(x^\alpha y^{1-\alpha}\le\max(x,y)\). If \(s(\alpha)>0\) for some \(\alpha\), then \(1+_s1\ge e^{s(\alpha)}>1\). (d) The map \(t\mapsto t^\lambda\) is increasing and continuous, so it commutes with suprema. □

**Theorem 6.4 (the entropy weight).** Let \(T>0\) and \(s=TS\), that is, \(w(\alpha)=e^{TS(\alpha)}=\alpha^{-T\alpha}(1-\alpha)^{-T(1-\alpha)}\). Write \(+_T\) for \(+_{TS}\). Then for all \(x,y\ge 0\)
\[ x+_Ty=\big(x^{1/T}+y^{1/T}\big)^T. \]
Consequently:

(a) \(+_T\) is commutative and associative, and \(x_1+_T\dots+_Tx_n=\big(\sum_ix_i^{1/T}\big)^T=\sup_pe^{TS(p)}\prod_ix_i^{p_i}\);

(b) \(x\mapsto x^{1/T}\) is an isomorphism from \(([0,\infty),+_T,\times)\) to the semiring \(([0,\infty),+,\times)\) of nonnegative real numbers; so \(([0,\infty),+_T,\times)\) is a semiring, and its ring of differences (Lemma 6.16) is \(\mathbb{R}\);

(c) \(\lim_{T\to 0}(x+_Ty)=\max(x,y)\).

*Proof.* The formula is (6.1) for \(n=2\). Then \((x+_Ty)^{1/T}=x^{1/T}+y^{1/T}\) and \((xy)^{1/T}=x^{1/T}y^{1/T}\), which gives (b) and the first equality in (a). The second equality in (a) is (6.1). For (c), let \(x\ge y\) and \(x>0\). Then \(x\le x+_Ty=x\big(1+(y/x)^{1/T}\big)^T\le 2^Tx\). □

*Reference:* [Connes 2011, Lemma 7.1 and Corollary 7.2]; [Connes–Consani 2011b, Example 2.21].

So the ordinary addition is recovered from \(\max\) and the multiplication alone, by weighting the monomials \(x^\alpha y^{1-\alpha}\) with the exponential of the entropy. The parameter \(T\) plays the part of a temperature. For a system with energy levels \(E_1,\dots,E_n\), put \(a_i=-E_i/T\) in Lemma 6.1. The lemma then says that the free energy \(F=-T\log\sum_ie^{-E_i/T}\) is the minimum of \(\sum_ip_iE_i-T\,S(p)\) over the probability vectors \(p\). This is the variational principle of thermodynamics. With \(x_i=e^{-E_i}\), Theorem 6.4 (a) reads \(x_1+_T\dots+_Tx_n=e^{-F}\). [Connes–Consani 2011b, §1] starts from this remark. The sum of \(n\) terms equal to \(1\) is \(n^T\). The limit (c) is the passage from the nonnegative real numbers to \(\mathbb{R}_+^{\max}\), called dequantization in [Connes–Consani 2011b, §1].

### 6.4 Why the entropy: the functional equations

**Proposition 6.5.** Let \(s\) be a weight such that, for all \(\alpha,\beta\in I\),
\[ \text{(C)}\quad s(1-\alpha)=s(\alpha),\qquad\qquad\text{(A)}\quad s(\alpha)+\alpha\,s(\beta)=s(\alpha\beta)+(1-\alpha\beta)\,s\Big(\frac{\alpha(1-\beta)}{1-\alpha\beta}\Big). \]
Then \(+_s\) is commutative and associative. So \(([0,\infty),+_s,\times)\) is a semiring.

*Proof.* Commutativity follows from (C) by the substitution \(\alpha\mapsto 1-\alpha\). For \(p=(p_1,p_2,p_3)\) with rational \(p_i\ge 0\) and \(\sum p_i=1\), define
\[ h(p)=s(p_1+p_2)+(p_1+p_2)\,s\Big(\frac{p_1}{p_1+p_2}\Big)\ \text{ if }p_1+p_2>0,\qquad h(0,0,1)=0. \]
By Lemma 6.3 (d), \((x+_sy)^\alpha=\sup_\beta e^{\alpha s(\beta)}x^{\alpha\beta}y^{\alpha(1-\beta)}\) for \(\alpha>0\). Substitute this in the definition of \((x+_sy)+_sz\) and put \(p=(\alpha\beta,\alpha(1-\beta),1-\alpha)\). Every \(p\neq(0,0,1)\) comes from exactly one pair \((\alpha,\beta)\) with \(\alpha>0\), namely \(\alpha=p_1+p_2\) and \(\beta=p_1/(p_1+p_2)\). The point \((0,0,1)\) corresponds to the term \(\alpha=0\), which is \(z\). So
\[ (x+_sy)+_sz=\sup_p\ e^{h(p)}x^{p_1}y^{p_2}z^{p_3}, \]
with \(0^0=1\). It remains to see that \(h\) is symmetric in \((p_1,p_2,p_3)\). Then \((x+_sy)+_sz\) is symmetric in \((x,y,z)\), and with commutativity this gives associativity.

Suppose all \(p_i>0\). By (C), \(h\) does not change when \(p_1\) and \(p_2\) are exchanged. Apply (A) to \(\alpha=p_1+p_2\) and \(\beta=p_1/(p_1+p_2)\). Then \(\alpha\beta=p_1\), \(\alpha(1-\beta)=p_2\) and \(1-\alpha\beta=p_2+p_3\), so
\[ h(p_1,p_2,p_3)=s(p_1)+(p_2+p_3)\,s\Big(\frac{p_2}{p_2+p_3}\Big)=h(p_2,p_3,p_1). \]
The last step uses \(s(p_1)=s(p_2+p_3)\), which is (C). So \(h\) is invariant under a transposition and under a cyclic permutation, hence under all permutations. Suppose some \(p_i=0\). Using \(s(0)=s(1)=0\) one finds that \(h(p)=0\) at the three vertices, and that \(h(p)=s(q)\) when exactly two coordinates are nonzero, \(q\) being either of them. This is symmetric by (C). □

The equations (C) and (A) are those of [Connes 2011, §5], written for \(s=\log w\). They are sufficient for associativity. They are not necessary: by Lemma 6.3 (c) every weight \(s\le 0\) gives \(+_s=\max\).

**Theorem 6.6.** Let \(s:I\to\mathbb{R}\) be a function.

(a) \(s\) satisfies (C) and (A) if and only if there is a function \(\ell\) on the positive integers, with real values and with \(\ell(mn)=\ell(m)+\ell(n)\) for all \(m,n\), such that
\[ s\Big(\frac kn\Big)=\ell(n)-\frac kn\,\ell(k)-\frac{n-k}n\,\ell(n-k)\qquad(0 < k < n). \]
The function \(\ell\) is determined by \(s\).

(b) If \(s\) satisfies (C) and (A), and \(s(1/n)\ge 0\) for every \(n\ge 2\), then there is \(T\ge 0\) with \(s=TS\) on \(I\).

*Reference:* [Connes 2011, Theorems 5.2 and 5.3]. There the values lie in a uniquely divisible abelian group for (a), and in a partially ordered group with real powers for (b); and (b) is proved under the hypothesis \(w(\alpha)\ge 1\) for all \(\alpha\in I\).

*Proof.* Let \(\Delta_n\) be the set of \(p=(p_1,\dots,p_n)\) with rational \(p_i>0\) and \(\sum_ip_i=1\).

*Step 1: entropies of \(n\) terms.* Assume (C) and (A). Define \(H_1(1)=0\), \(H_2(p_1,p_2)=s(p_1)\), and for \(n\ge 3\)
\[ H_n(p_1,\dots,p_n)=H_{n-1}(p_1+p_2,p_3,\dots,p_n)+(p_1+p_2)\,s\Big(\frac{p_1}{p_1+p_2}\Big). \]
The same relation holds for \(n=2\). We claim that \(H_n\) is a symmetric function on \(\Delta_n\). For \(n=2\) this is (C). For \(n=3\), \(H_3\) is the function \(h\) of Proposition 6.5, and the proof given there shows that it is symmetric. Let \(n\ge 4\). By induction, \(H_n\) does not change when \(p_3,\dots,p_n\) are permuted. Applying the definition twice,
\[ H_n(p)=H_{n-2}(\sigma,p_4,\dots,p_n)+\sigma\,H_3\Big(\frac{p_1}\sigma,\frac{p_2}\sigma,\frac{p_3}\sigma\Big),\qquad\sigma=p_1+p_2+p_3. \]
This does not change when \(p_1,p_2,p_3\) are permuted. These two groups of permutations generate all permutations.

*Step 2: grouping.* Let \(p\in\Delta_n\) and let \(\{1,\dots,n\}\) be partitioned into blocks \(B_1,\dots,B_m\). Put \(q_j=\sum_{i\in B_j}p_i\), and let \(p^{(j)}\) be the vector \((p_i/q_j)_{i\in B_j}\). Then
\[ H_n(p)=H_m(q)+\sum_{j=1}^mq_j\,H_{|B_j|}\big(p^{(j)}\big). \]
We argue by induction on \(n-m\). If \(n=m\), the blocks are singletons and the formula is the symmetry of \(H_n\). Otherwise some block has two elements. By symmetry we may assume that \(1,2\in B_1\). Let \(p'=(p_1+p_2,p_3,\dots,p_n)\), with the partition obtained by merging \(1\) and \(2\). By induction the formula holds for \(p'\). Passing from \(p'\) to \(p\) adds \((p_1+p_2)\,s(p_1/(p_1+p_2))\) to the left side, by the definition of \(H_n\). It adds the same quantity to the term \(q_1H_{|B_1|}(p^{(1)})\) on the right, by the definition of \(H_{|B_1|}\), and it changes no other term.

*Step 3: the function \(\ell\).* Put \(\ell(n)=H_n(1/n,\dots,1/n)\). Grouping \(mn\) equal terms into \(m\) blocks of \(n\) terms gives \(\ell(mn)=\ell(m)+\ell(n)\). Grouping \(n\) equal terms into two blocks of \(k\) and \(n-k\) terms gives
\[ \ell(n)=s\Big(\frac kn\Big)+\frac kn\,\ell(k)+\frac{n-k}n\,\ell(n-k). \]
This is the formula of (a). For \(k=1\) it reads \(n\ell(n)=(n-1)\ell(n-1)+n\,s(1/n)\), since \(\ell(1)=0\). So
\[ n\,\ell(n)=\sum_{j=2}^nj\,s(1/j), \]
and \(\ell\) is determined by \(s\).

*Step 4: the converse in (a).* Let \(\ell\) be as in (a). Replacing \((k,n)\) by \((ck,cn)\) changes the right side of the formula by \(\ell(c)\big(1-\frac kn-\frac{n-k}n\big)=0\). So the formula defines a function \(s\) on \(I\). Let \(L\) be the homomorphism from \((\mathbb{Q}_{>0},\times)\) to \((\mathbb{R},+)\) with \(L(a/b)=\ell(b)-\ell(a)\). Then \(s(\alpha)=\alpha L(\alpha)+(1-\alpha)L(1-\alpha)\), which gives (C). For \(p\in\Delta_3\), using \(L(p_1/(p_1+p_2))=L(p_1)-L(p_1+p_2)\), one finds
\[ s(p_1+p_2)+(p_1+p_2)\,s\Big(\frac{p_1}{p_1+p_2}\Big)=\sum_{i=1}^3p_iL(p_i). \]
The right side is symmetric in \(p\). The two sides of (A), for \(\alpha=p_1+p_2\) and \(\beta=p_1/(p_1+p_2)\), are the values of the left side at \((p_1,p_2,p_3)\) and at \((p_2,p_3,p_1)\), as in the proof of Proposition 6.5. So (A) holds.

*Step 5: positivity.* Assume moreover that \(s(1/n)\ge 0\) for \(n\ge 2\). By Step 3, \(n\ell(n)\) is a nondecreasing function of \(n\), and \(\ell\ge 0\). Let \(a,b\ge 2\) be integers and \(\theta=\log b/\log a\). We show that \(\theta\,\ell(a)\le\ell(b)\). Let \(0 < \varepsilon < 1\).

We first find integers \(k\ge 1\) and \(m\ge 0\) with \(0\le k\theta-m < \varepsilon\). Choose \(N>1/\varepsilon\). Two of the \(N+1\) numbers \(i\theta-\lfloor i\theta\rfloor\), \(0\le i\le N\), differ by less than \(1/N\). Their difference gives integers \(k_0\ge 1\) and \(m_0\) with \(|k_0\theta-m_0| < \varepsilon\). If \(k_0\theta\ge m_0\), take \(k=k_0\) and \(m=m_0\). Otherwise put \(\delta=m_0-k_0\theta\), so \(0 < \delta < \varepsilon\), and \(j=\lfloor 1/\delta\rfloor\). Then \(1-\delta < j\delta\le 1\), and \(k=jk_0\), \(m=jm_0-1\) satisfy \(k\theta-m=1-j\delta\in[0,\delta)\). In both cases \(m>k\theta-1>-1\), so \(m\ge 0\).

Then \(a^m\le a^{k\theta}=b^k < a^{m+\varepsilon}\). Since \(n\ell(n)\) is nondecreasing, \(a^m\ell(a^m)\le b^k\ell(b^k)\), that is, \(a^m\,m\,\ell(a)\le b^k\,k\,\ell(b)\). Hence
\[ (k\theta-\varepsilon)\,\ell(a)\le m\,\ell(a)\le\frac{b^k}{a^m}\,k\,\ell(b)\le a^\varepsilon\,k\,\ell(b). \]
Dividing by \(k\) gives \((\theta-\varepsilon)\,\ell(a)\le a^\varepsilon\,\ell(b)\). Letting \(\varepsilon\to 0\) gives \(\theta\,\ell(a)\le\ell(b)\), that is, \(\ell(a)/\log a\le\ell(b)/\log b\). Exchanging \(a\) and \(b\) gives equality. So \(T=\ell(n)/\log n\) does not depend on \(n\ge 2\), \(T\ge 0\), and \(\ell(n)=T\log n\) for all \(n\ge 1\). The formula of (a) becomes
\[ s\Big(\frac kn\Big)=T\Big(\log n-\frac kn\log k-\frac{n-k}n\log(n-k)\Big)=T\,S\Big(\frac kn\Big). \]
□

Theorem 6.6 (a) gives many solutions of (C) and (A): the function \(\ell\) can be prescribed freely on the prime numbers. Here are two. For \(\ell=-T\log\) with \(T>0\), the solution is \(-TS\le 0\), and \(+_s=\max\). For \(\ell=v_2\), the exponent of \(2\) in \(n\), one finds \(s(2^{-j})=j\); this is not bounded above, so \(s\) is not a weight (Exercise 7). Part (b) says that positivity singles out the entropy. With Theorem 6.4 and Lemma 6.3 (c) we obtain:

**Corollary 6.7.** Let \(s\) be a weight that satisfies (C) and (A), with \(s(1/n)\ge 0\) for all \(n\ge 2\). Then either \(s=0\) and \(+_s=\max\), or there is \(T>0\) with \(x+_sy=(x^{1/T}+y^{1/T})^T\) for all \(x,y\).

### 6.5 The general construction

[Connes 2011, §6] carries out the construction of Section 6.3 for a perfect semiring \(R\) of characteristic one (Definition 1.9) and an invertible element \(\rho\) of \(R\) with \(\rho\ge 1\) and \(\rho\neq 1\). The element \(\rho\) plays the part of \(e^T\): in \(\mathbb{R}_+^{\max}\) with \(\rho=e^T\), the weight \(\rho^{S(\alpha)}\) is the weight \(e^{TS(\alpha)}\) of Theorem 6.4. In general the terms \(\rho^{S(\alpha)}x^\alpha y^{1-\alpha}\) need not have a least upper bound in \(R\). One first keeps the elements that are bounded by powers of \(\rho\), and completes them for a distance defined by \(\rho\).

Throughout this section, \(R\) is a perfect semiring of characteristic one, and \(\rho\in R^\times\) satisfies \(\rho\ge 1\) and \(\rho\neq 1\). For rational \(q>0\) we write \(x^q=\theta_q(x)\) as in Proposition 1.10. For rational \(a<0\) put \(\rho^a=(\rho^{-1})^{-a}\), and put \(\rho^0=1\). We write \(u<v\) when \(u\le v\) and \(u\neq v\). Let
\[ R_\rho=\{0\}\cup\bigcup_{n\ge 0}\,[\rho^{-n},\rho^n],\qquad [\rho^{-n},\rho^n]=\{x\in R\mid \rho^{-n}\le x\le\rho^n\},\qquad M=R_\rho\setminus\{0\}. \]

**Theorem 6.8.** (a) The set \(M\) carries a pseudometric \(d\), defined in (6.3) below. Let \(\widehat{M}\) be the separated completion of \((M,d)\) (Lemma 6.12) and \(\bar R_\rho=\widehat{M}\sqcup\{0\}\). The addition and the multiplication of \(M\) extend continuously to \(\widehat{M}\). With \(0\) neutral for the addition and absorbing for the multiplication, \(\bar R_\rho\) is a perfect semiring of characteristic one. Every \(x\in\widehat{M}\) satisfies \(\rho^{-N}\le x\le\rho^N\) for some integer \(N\).

(b) The automorphisms \(x\mapsto x^q\) of \(\bar R_\rho\), \(q\) rational and positive, extend to automorphisms \(x\mapsto x^t\), \(t\) real and positive, and \(x^t\) depends continuously on \((t,x)\). The powers \(\rho^a\) are defined for all real \(a\), and \(d(\rho^a,\rho^b)=|a-b|\).

(c) Let \(x,y\in\bar R_\rho\) be nonzero. Put \(I(n)=\frac1n\mathbb{Z}\cap[0,1]\) and
\[ s_n(x,y)=\sum_{\alpha\in I(n)}\rho^{S(\alpha)}x^\alpha y^{1-\alpha}, \tag{6.2} \]
where the sum is computed in \(\bar R_\rho\) and \(x^\alpha y^{1-\alpha}\) means \(y\) for \(\alpha=0\) and \(x\) for \(\alpha=1\). The sequence \(s_n(x,y)\) converges, and its limit \(x+_wy\) is the least upper bound of the elements \(\rho^{S(\alpha)}x^\alpha y^{1-\alpha}\), \(0\le\alpha\le 1\).

(d) Put \(0+_wy=y+_w0=y\) for all \(y\). Then \(A=(\bar R_\rho,+_w,\cdot)\) is a semiring, and \(\rho^a+_w\rho^b=\rho^{\log(e^a+e^b)}\) for all real \(a,b\).

(e) The ring of differences \(W(R,\rho)\) of \(A\) (Lemma 6.16) is a nonzero algebra over \(\mathbb{R}\). Let \([a,b]\) be the class of \((a,b)\in A\times A\). For real \(t>0\), the real numbers \(t\) and \(-t\) act by \(t\,[a,b]=[\rho^{\log t}a,\rho^{\log t}b]\) and \((-t)\,[a,b]=[\rho^{\log t}b,\rho^{\log t}a]\).

(f) Let \(R'\) and \(\rho'\) satisfy the same hypotheses as \(R\) and \(\rho\), and let \(f:R\to R'\) be a morphism of semirings with \(f(\rho)=\rho'\). Then \(f\) induces a morphism of \(\mathbb{R}\)-algebras \(W(R,\rho)\to W(R',\rho')\). Identities induce identities, and composites induce composites.

*Reference:* [Connes 2011, Proposition 6.5, Lemma 6.6, Proposition 6.8, Corollary 6.9 and Theorem 6.11]. Part (f) is not stated there. [Connes 2011] writes the limit in (c) as \(\sum_{\alpha\in\bar I}w(\alpha)x^\alpha y^{1-\alpha}\) with \(w(\alpha)=\rho^{S(\alpha)}\), as in Section 6.3.

The proof occupies the rest of this section.

**Lemma 6.9.** (a) For rational numbers \(a<b\), \(\rho^a<\rho^b\) and \(\rho^a+\rho^b=\rho^b\). The rules \(\rho^a\rho^b=\rho^{a+b}\) and \((\rho^a)^q=\rho^{aq}\) hold for rational \(a,b\) and rational \(q>0\).

(b) \(R_\rho\) is a sub-semiring of \(R\), and \(x^q\in R_\rho\) for \(x\in R_\rho\) and rational \(q>0\). So \(R_\rho\) is a perfect semiring of characteristic one.

(c) Let \(x,y,z\) be elements of a multiplicatively cancellative semiring of characteristic one, with \(z\neq 0\). Then \(xz\le yz\) if and only if \(x\le y\).

*Proof.* (a) Each \(\theta_q\) is an automorphism of \(R\) that preserves sums, so it preserves the order, and so does its inverse \(\theta_{1/q}\). Applying \(\theta_q\) to \(\rho\rho^{-1}=1\) shows that \(\rho^q\) is invertible with inverse \((\rho^{-1})^q\); with Proposition 1.10 this gives the two rules. Applying \(\theta_q\) to \(1+\rho=\rho\) gives \(1\le\rho^q\), and \(\rho^q\neq 1\) because \(\theta_q\) is injective and \(\rho\neq 1\). Multiplication by an invertible element preserves the order (Lemma 1.2 (c)) and is injective. Multiplying \(1\le\rho^{b-a}\) and \(1\neq\rho^{b-a}\) by \(\rho^a\) gives \(\rho^a\le\rho^b\) and \(\rho^a\neq\rho^b\). The equality \(\rho^a+\rho^b=\rho^b\) is the definition of \(\rho^a\le\rho^b\).

(b) Let \(x\in[\rho^{-m},\rho^m]\), \(y\in[\rho^{-n},\rho^n]\) and \(k=\max(m,n)\). By Lemma 1.2 (b), (c) and by (a), \(\rho^{-k}\le x\le x+y\le\rho^k+\rho^k=\rho^k\) and \(\rho^{-m-n}\le xy\le\rho^{m+n}\). Applying \(\theta_q\) gives \(\rho^{-mq}\le x^q\le\rho^{mq}\), and \(\rho^{-N}\le\rho^{-mq}\), \(\rho^{mq}\le\rho^N\) for an integer \(N\ge mq\). Moreover \(0,1\in R_\rho\). So \(R_\rho\) is a sub-semiring which contains \(x^{1/n}\) together with \(x\). Like \(R\), it is multiplicatively cancellative and of characteristic one.

(c) \(xz\le yz\) means \(xz+yz=yz\), that is \((x+y)z=yz\). Since \(z\neq 0\), this holds if and only if \(x+y=y\). □

*Reference:* [Connes 2011, Lemma 6.2].

**Lemma 6.10.** For rational \(q>0\) let \(U_q\) be the set of pairs \((x,y)\in M\times M\) with \(x\le y\rho^q\) and \(y\le x\rho^q\). For \(x,y\in M\) put
\[ d(x,y)=\inf\{q\in\mathbb{Q}_{>0}\mid (x,y)\in U_q\}. \tag{6.3} \]
(a) \(d\) is a pseudometric on \(M\): it is finite, \(d(x,x)=0\), \(d(x,y)=d(y,x)\), and \(d(x,z)\le d(x,y)+d(y,z)\). If \(q>d(x,y)\) is rational, then \((x,y)\in U_q\).

(b) For finitely many \(x_i,y_i\in M\) (at least one), for \(x,y,u,v,z\in M\) and for rational \(q>0\),
\[ d\Big(\sum_ix_i,\sum_iy_i\Big)\le\max_i\,d(x_i,y_i),\quad d(xy,uv)\le d(x,u)+d(y,v),\quad d(xz,yz)=d(x,y),\quad d(x^q,y^q)=q\,d(x,y). \tag{6.4} \]
(c) Put \(x^0=1\). For \(x\in M\) and rational \(a,b\ge 0\), \(d(x^a,x^b)=|a-b|\,d(x,1)\).

(d) \(d(\rho^a,\rho^b)=|a-b|\) for rational \(a,b\).

*Proof.* (a) By Lemma 6.9 (a), \(U_q\subseteq U_r\) for \(q<r\), and \((x,x)\in U_q\) for all \(q\). If \(x,y\in[\rho^{-n},\rho^n]\), then \(x\le\rho^n=\rho^{-n}\rho^{2n}\le y\rho^{2n}\) and likewise \(y\le x\rho^{2n}\), so \(d(x,y)\le 2n\). If \(q>d(x,y)\), there is a rational \(r<q\) with \((x,y)\in U_r\subseteq U_q\). Symmetry is clear. If \((x,y)\in U_q\) and \((y,z)\in U_r\), then \(x\le y\rho^q\le z\rho^{q+r}\) and \(z\le y\rho^r\le x\rho^{q+r}\), so \((x,z)\in U_{q+r}\). Taking the infimum over \(q\) and \(r\) gives the triangle inequality.

(b) Let \(r>\max_id(x_i,y_i)\) be rational. By (a), \(x_i\le y_i\rho^r\) and \(y_i\le x_i\rho^r\) for all \(i\); adding these inequalities (Lemma 1.2 (c)) gives \((\sum_ix_i,\sum_iy_i)\in U_r\). If \((x,u)\in U_q\) and \((y,v)\in U_r\), multiplying the inequalities gives \((xy,uv)\in U_{q+r}\). By Lemma 6.9 (c), \((xz,yz)\in U_r\) if and only if \((x,y)\in U_r\). Applying \(\theta_q\) and \(\theta_{1/q}\) shows that \((x,y)\in U_r\) if and only if \((x^q,y^q)\in U_{qr}\).

(c) Let \(a>b\). By (b), \(d(x^a,x^b)=d(x^{a-b}x^b,1\cdot x^b)=d(x^{a-b},1^{a-b})=(a-b)\,d(x,1)\).

(d) By Lemma 6.9 (a), \(\rho^a\le\rho^b\rho^q\) holds if and only if \(a\le b+q\). So \((\rho^a,\rho^b)\in U_q\) if and only if \(|a-b|\le q\). □

*Reference:* [Connes 2011, (110), Lemmas 6.3 and 6.4].

By (6.4), the relation \(d(x,y)=0\) is compatible with sums, products and the powers \(x^q\). It is not the equality relation in general.

**Example 6.11.** Let \(R\) be \(\mathbb{R}^2\) with an absorbing zero adjoined, with the addition of vectors as multiplication and the maximum for the lexicographic order as addition (Proposition 1.4). It is a perfect semifield of characteristic one, with \((a,b)^t=(ta,tb)\). Take \(\rho=(1,0)\). Every element of \(\mathbb{R}^2\) lies in \(M\). For rational \(q>0\), the two inequalities \((a_1,b_1)\le(a_2+q,b_2)\) and \((a_2,b_2)\le(a_1+q,b_1)\) hold if \(q>|a_1-a_2|\), and one of them fails if \(q<|a_1-a_2|\). So \(d((a_1,b_1),(a_2,b_2))=|a_1-a_2|\). In particular \(d((0,1),1)=0\) although \((0,1)\neq 1\).

**Lemma 6.12 (separated completion).** Let \(d\) be a pseudometric on a set \(M\). Call two Cauchy sequences \((x_j)\) and \((y_j)\) in \(M\) equivalent if \(d(x_j,y_j)\to 0\), and let \(\widehat{M}\) be the set of equivalence classes. Let \(\iota(x)\) be the class of the constant sequence \(x\).

(a) For classes \(\xi=[x_j]\) and \(\eta=[y_j]\), the limit \(d(\xi,\eta)=\lim_jd(x_j,y_j)\) exists and defines a metric on \(\widehat{M}\). One has \(d(\iota x,\iota y)=d(x,y)\), and \(\iota(M)\) is dense in \(\widehat{M}\).

(b) \(\widehat{M}\) is complete.

(c) Let \(N\) be a complete metric space, \(k\ge 1\), \(C\ge 0\), and let \(f\colon M^k\to N\) satisfy \(d(f(x),f(y))\le C\sum_id(x_i,y_i)\). Then there is a unique continuous map \(\hat f\colon\widehat{M}^k\to N\) with \(\hat f(\iota x_1,\dots,\iota x_k)=f(x_1,\dots,x_k)\), and \(\hat f\) satisfies the same inequality.

*Proof.* (a) Since \(|d(x_j,y_j)-d(x_l,y_l)|\le d(x_j,x_l)+d(y_j,y_l)\), the real numbers \(d(x_j,y_j)\) form a Cauchy sequence, and the same inequality shows that the limit does not depend on the representatives. The limit is symmetric and satisfies the triangle inequality, and it vanishes only for equivalent sequences. If \((x_j)\) is a Cauchy sequence, then \(d(\iota x_l,[x_j])=\lim_jd(x_l,x_j)\) is small for large \(l\). So \(\iota(M)\) is dense.

(b) Let \((\xi_l)\) be a Cauchy sequence in \(\widehat{M}\), and choose \(x_l\in M\) with \(d(\iota x_l,\xi_l)<1/l\). Then \(d(x_l,x_m)<1/l+d(\xi_l,\xi_m)+1/m\), so \((x_l)\) is a Cauchy sequence in \(M\). Its class \(\xi\) satisfies \(d(\xi_l,\xi)\le 1/l+d(\iota x_l,\xi)\), which tends to \(0\).

(c) If \((x_{i,j})_j\) represents \(\xi_i\), then \(f(x_{1,j},\dots,x_{k,j})\) is a Cauchy sequence in \(N\); let \(\hat f(\xi_1,\dots,\xi_k)\) be its limit. By the inequality, it does not depend on the representatives, and the inequality passes to the limit. So \(\hat f\) is continuous. It is unique because \(\iota(M)^k\) is dense. □

**Proposition 6.13.** Let \(\widehat{M}\) be the separated completion of \((M,d)\). We write \(x\) for \(\iota(x)\) when \(x\in M\). By (6.4) and Lemma 6.12 (c), the addition, the multiplication and the maps \(x\mapsto x^q\) extend to continuous maps on \(\widehat{M}\); the first estimate of (6.4) gives \(d(x+y,u+v)\le d(x,u)+d(y,v)\). Put \(\bar R_\rho=\widehat{M}\sqcup\{0\}\), where \(0\) is neutral for the addition and absorbing for the multiplication. We write \(d\) for the metric of \(\widehat{M}\).

(a) \(\bar R_\rho\) is a perfect semiring of characteristic one, and \(d(xz,yz)=d(x,y)\) for \(x,y,z\in\widehat{M}\).

(b) If \(a_j\le b_j\) in \(\widehat{M}\), \(a_j\to a\) and \(b_j\to b\), then \(a\le b\).

(c) Every \(x\in\widehat{M}\) satisfies \(\rho^{-N}\le x\le\rho^N\) for some integer \(N\ge 0\).

(d) For \(x\in\widehat{M}\) and real \(t\ge 0\), let \(x^t\) be the limit of \(x^{q_j}\), for rational \(q_j\ge 0\) with \(q_j\to t\), where \(x^0=1\). The limit exists and does not depend on the \(q_j\). For \(x,y\in\widehat{M}\) and real \(a,b,t\ge 0\),
\[ d(x^a,x^b)=|a-b|\,d(x,1),\qquad d(x^t,y^t)=t\,d(x,y),\qquad d(x^a,y^b)\le a\,d(x,y)+|a-b|\,d(y,1). \tag{6.5} \]
So \(x^t\) depends continuously on \((t,x)\). For real \(s,t>0\), \((x^s)^t=x^{st}\), \(x^sx^t=x^{s+t}\), \((xy)^t=x^ty^t\) and \((x+y)^t=x^t+y^t\). With \(0^t=0\), the map \(x\mapsto x^t\) is an automorphism of \(\bar R_\rho\) with inverse \(x\mapsto x^{1/t}\).

(e) The map \(a\mapsto\rho^a\) extends from \(\mathbb{Q}\) to a map from \(\mathbb{R}\) to \(\widehat{M}\) with \(d(\rho^a,\rho^b)=|a-b|\). It satisfies \(\rho^{a+b}=\rho^a\rho^b\), \((\rho^a)^t=\rho^{at}\) for \(t>0\), and \(\rho^a+\rho^b=\rho^{\max(a,b)}\). So \(\rho^a<\rho^b\) for real \(a<b\).

*Proof.* (a) The identities that define a semiring and do not involve \(0\), and the identity \(1+1=1\), hold on the dense set \(\iota(M)\). Both sides of each identity are continuous, so the identities hold on \(\widehat{M}\). Sums and products of elements of \(\widehat{M}\) lie in \(\widehat{M}\), so the identities that involve \(0\) hold as well. The equality \(d(xz,yz)=d(x,y)\) holds on \(M\) by (6.4), and it passes to \(\widehat{M}\) by continuity. So \(xz=yz\) with \(z\neq 0\) implies \(x=y\) if \(x,y\neq 0\); and if \(x=0\neq y\), then \(xz=0\neq yz\). Hence \(\bar R_\rho\) is multiplicatively cancellative. The extended maps \(x\mapsto x^q\) preserve sums and products, and the extension of \(\theta_{1/q}\) is inverse to that of \(\theta_q\), because this holds on \(\iota(M)\). The extension of \(\theta_n\) is \(x\mapsto x^n\), by continuity. With \(0^q=0\), the map \(\varphi_n\) is therefore surjective for every \(n\ge 1\), and \(\bar R_\rho\) is perfect.

(b) \(a+b=\lim_j(a_j+b_j)=\lim_jb_j=b\).

(c) Let the Cauchy sequence \((x_j)\) in \(M\) represent \(x\). Choose \(j_0\) with \(d(x_j,x_{j_0})<1\) for \(j\ge j_0\), and \(N\) with \(x_{j_0}\in[\rho^{-N},\rho^N]\). By Lemma 6.10 (a), \((x_j,x_{j_0})\in U_1\), so \(\rho^{-N-1}\le x_j\le\rho^{N+1}\) for \(j\ge j_0\). Now (b) gives \(\rho^{-N-1}\le x\le\rho^{N+1}\).

(d) The relations of Lemma 6.10 (c) and (6.4) pass to \(\widehat{M}\) by continuity. So \(d(x^{q_j},x^{q_l})=|q_j-q_l|\,d(x,1)\): the sequence \((x^{q_j})\) is a Cauchy sequence, and two such sequences with the same limit \(t\) have the same limit, since the interleaved sequence is a Cauchy sequence too. The relations (6.5) hold for rational exponents and pass to the limit; the third follows from the first two. The four identities hold for rational exponents by Proposition 1.10 and (a), and they pass to the limit by continuity. For the first, take rational \(s_j\to s\) and \(t_j\to t\): then \((x^{s_j})^{t_j}\to(x^s)^t\) by the continuity in \((t,x)\), and \(x^{s_jt_j}\to x^{st}\). The identities \((x^t)^{1/t}=x\), \((xy)^t=x^ty^t\) and \((x+y)^t=x^t+y^t\) say that \(x\mapsto x^t\) is an automorphism.

(e) By Lemma 6.10 (d), \(a\mapsto\rho^a\) preserves distances on \(\mathbb{Q}\). Since \(\widehat{M}\) is complete, it extends to a distance-preserving map on \(\mathbb{R}\). The three identities hold for rational \(a,b,t\) by Lemma 6.9 (a), and they pass to the limit by continuity. If \(a<b\), then \(\rho^a+\rho^b=\rho^b\) says that \(\rho^a\le\rho^b\), and \(\rho^a\neq\rho^b\) since \(d(\rho^a,\rho^b)=b-a>0\). □

*Reference:* [Connes 2011, Proposition 6.5]. Its proof does not check multiplicative cancellation, which Definition 1.9 requires; the equality \(d(xz,yz)=d(x,y)\) gives it.

**Lemma 6.14 (suprema of continuous families).** Let \(Y\subset\mathbb{R}^m\) be closed, bounded and nonempty, and let \(f\colon Y\to\widehat{M}\) be continuous. For \(\delta>0\), a *\(\delta\)-net* is a finite set \(E\subseteq Y\) such that every point of \(Y\) has distance at most \(\delta\) from \(E\). Put \(\omega_f(\delta)=\sup\{d(f(s),f(t))\mid s,t\in Y,\ |s-t|\le\delta\}\), and write \(\sum_Ef\) for \(\sum_{s\in E}f(s)\).

(a) \(\omega_f(\delta)\to 0\) as \(\delta\to 0\). If \(E\) is a \(\delta\)-net and \(E'\) an \(\eta\)-net, then \(d(\sum_Ef,\sum_{E'}f)\le\omega_f(\max(\delta,\eta))\).

(b) The set \(f(Y)\) has a least upper bound \(\sup_Yf\) in \(\bar R_\rho\), and \(d(\sum_Ef,\sup_Yf)\le\omega_f(\delta)\) for every \(\delta\)-net \(E\). If \(D\subseteq Y\) is dense in \(Y\), then \(\sup_Yf\) is also the least upper bound of \(f(D)\).

(c) If \(\Phi\colon\widehat{M}\to\widehat{M}\) is continuous and \(\Phi(u+v)=\Phi(u)+\Phi(v)\) for all \(u,v\), then \(\Phi(\sup_Yf)=\sup_Y(\Phi\circ f)\). This applies to \(u\mapsto zu\) for \(z\in\widehat{M}\), to \(u\mapsto u^t\) for real \(t>0\), and to constant maps.

(d) If \(g\colon Y\to\widehat{M}\) is continuous, then \(d(\sup_Yf,\sup_Yg)\le\sup_{s\in Y}d(f(s),g(s))\).

(e) Let \(Y'\subset\mathbb{R}^{m'}\) be closed, bounded and nonempty, and let \(\Psi\colon Y\times Y'\to\widehat{M}\) be continuous. Then \(s\mapsto\sup_{t\in Y'}\Psi(s,t)\) is continuous on \(Y\), and \(\sup_{s\in Y}\sup_{t\in Y'}\Psi(s,t)=\sup_{Y\times Y'}\Psi\).

*Proof.* The set \(Y\) is compact by the Heine–Borel theorem ([Real Analysis I, Theorem 7.4.14](https://www.jirka.org/ra/html/sec_metcompact.html#thm_msbw)), so \(f\) is uniformly continuous ([Real Analysis I, Theorem 7.5.11](https://www.jirka.org/ra/html/sec_metcont.html#thm_Xcompactfunifcont)); this is the first statement of (a). Finitely many balls of radius \(\delta\) cover \(Y\), so \(\delta\)-nets exist.

(a) Consider the pairs \((s,t)\in E\times E'\) with \(|s-t|\le\max(\delta,\eta)\). Every \(s\in E\) is the first coordinate of such a pair, because \(E'\) is an \(\eta\)-net, and every \(t\in E'\) is the second coordinate of such a pair. As \(u+u=u\), \(\sum_Ef\) is the sum of the \(f(s)\) over these pairs, and \(\sum_{E'}f\) is the sum of the \(f(t)\). Now apply the first estimate of (6.4), which holds on \(\widehat{M}\) by continuity.

(b) Let \(E_n\) be \(\delta_n\)-nets with \(\delta_n\to 0\). By (a), the sums \(\sum_{E_n}f\) form a Cauchy sequence; let \(u\) be its limit. By (a), \(d(\sum_Ef,u)\le\omega_f(\delta)\) for every \(\delta\)-net \(E\). For \(s\in Y\) choose \(s_n\in E_n\) with \(|s-s_n|\le\delta_n\). Then \(f(s_n)\le\sum_{E_n}f\), and Proposition 6.13 (b) gives \(f(s)\le u\). Let \(v\) be an upper bound of \(f(D)\), where \(D\) is dense in \(Y\) (for instance \(D=Y\)). Then \(v\neq 0\), since only \(0\) lies below \(0\). For \(s\in Y\) and \(s_j\in D\) with \(s_j\to s\), Proposition 6.13 (b) applied to \(f(s_j)\le v\) gives \(f(s)\le v\). So \(\sum_{E_n}f\le v\) (Lemma 1.2 (b)), and Proposition 6.13 (b) gives \(u\le v\). Hence \(u\) is the least upper bound of \(f(Y)\) and of \(f(D)\).

(c) \(\Phi(\sum_{E_n}f)=\sum_{E_n}\Phi\circ f\), and \(\Phi\circ f\) is continuous; let \(n\to\infty\) and use (b). Multiplication by \(z\) is continuous by (6.4) and additive by distributivity. The map \(u\mapsto u^t\) is continuous and additive by Proposition 6.13 (d). A constant map \(c\) is additive because \(c+c=c\).

(d) Apply the first estimate of (6.4) to \(\sum_{E_n}f\) and \(\sum_{E_n}g\), and let \(n\to\infty\).

(e) By (d), \(d(\sup_t\Psi(s,t),\sup_t\Psi(s',t))\le\sup_td(\Psi(s,t),\Psi(s',t))\), which tends to \(0\) as \(s'\to s\), because \(\Psi\) is uniformly continuous on the compact set \(Y\times Y'\). So the left side of the equality exists by (b). The right side exists by (b) as well, since \(Y\times Y'\subset\mathbb{R}^{m+m'}\) is closed and bounded. An element is an upper bound of all \(\sup_t\Psi(s,t)\) if and only if it is an upper bound of all \(\Psi(s,t)\). So both sides are the least element of the same set. □

For \(x,y\in\widehat{M}\) and \(0\le\alpha\le 1\) put \(F_{x,y}(\alpha)=\rho^{S(\alpha)}x^\alpha y^{1-\alpha}\). With \(x^0=1\), this is \(y\) for \(\alpha=0\) and \(x\) for \(\alpha=1\), as in (6.2). Put \(B(x,y)=\sup_{0\le\alpha\le 1}F_{x,y}(\alpha)\).

**Proposition 6.15.** Let \(x,y,u,v\in\widehat{M}\), and put \(\omega_S(\delta)=\sup\{|S(\alpha)-S(\beta)|\mid|\alpha-\beta|\le\delta\}\).

(a) \(F_{x,y}\) is continuous, and \(d(s_n(x,y),B(x,y))\le\omega_S(1/n)+\frac1n\big(d(x,1)+d(y,1)\big)\). So \(s_n(x,y)\to B(x,y)\). The elements \(F_{x,y}(\alpha)\) with rational \(\alpha\) have the same least upper bound \(B(x,y)\), and the sums of these elements over the finite sets of rational numbers in \([0,1]\), ordered by inclusion, converge to \(B(x,y)\).

(b) \(s_n(x,y)\le s_m(x,y)\) if \(n\) divides \(m\). The sequence need not be increasing: \(s_2(1,1)=\rho^{\log 2}>\rho^{S(1/3)}=s_3(1,1)\).

(c) \(x+y\le s_n(x,y)\le B(x,y)\le\rho^{\log 2}(x+y)\le\rho\,(x+y)\).

(d) \(d(B(x,y),B(u,v))\le\max\big(d(x,u),d(y,v)\big)\).

If one of the two elements in (6.2) is \(0\), all terms with \(0<\alpha<1\) vanish, and the sums are equal to the other element.

*Proof.* (a) By (6.4), (6.5) and Proposition 6.13 (e), \(d(F_{x,y}(\alpha),F_{x,y}(\beta))\le|S(\alpha)-S(\beta)|+|\alpha-\beta|\big(d(x,1)+d(y,1)\big)\). The function \(S\) is continuous on \([0,1]\), because \(t\log t\to 0\) as \(t\to 0\). So \(F_{x,y}\) is continuous, \(\omega_{F_{x,y}}(\delta)\le\omega_S(\delta)+\delta\big(d(x,1)+d(y,1)\big)\), and \(I(n)\) is a \(1/n\)-net. Lemma 6.14 (b) gives the estimate and the statement on rational \(\alpha\). For the last statement, note that a finite set which contains a \(\delta\)-net is a \(\delta\)-net.

(b) \(I(n)\subseteq I(m)\) if \(n\) divides \(m\). By Proposition 6.13 (e), \(s_n(1,1)=\rho^c\) with \(c=\max_{\alpha\in I(n)}S(\alpha)\). This maximum is \(S(1/2)=\log 2\) for \(n=2\), and it is \(S(1/3)<\log 2\) for \(n=3\), because \(\alpha=1/2\) is the only point with \(S(\alpha)=\log 2\) (Lemma 6.1 with \(a_1=a_2=0\)).

(c) For \(0<\alpha<1\), the powers preserve the order, so \(x^\alpha y^{1-\alpha}\le(x+y)^\alpha(x+y)^{1-\alpha}=x+y\). By Lemma 6.1 with \(a_1=a_2=0\), \(0\le S(\alpha)\le\log 2<1\), so \(1\le\rho^{S(\alpha)}\le\rho^{\log 2}\le\rho\). The terms of index \(\alpha=0\) and \(\alpha=1\) are \(y\) and \(x\). Hence every term is at most \(\rho^{\log 2}(x+y)\), so \(B(x,y)\le\rho^{\log 2}(x+y)\), and \(x+y\le s_n(x,y)\le B(x,y)\).

(d) By (6.4) and (6.5), \(d(F_{x,y}(\alpha),F_{u,v}(\alpha))\le\alpha\,d(x,u)+(1-\alpha)\,d(y,v)\). Apply Lemma 6.14 (d). □

*Reference:* [Connes 2011, Lemma 6.6]. There the sums are compared with the sums over \(I(nm)\), and the limit is identified through the increase along divisibility.

**Lemma 6.16 (the ring of differences).** Let \(A\) be a semiring, with addition \(\oplus\). For \((a,b),(c,e)\in A\times A\) write \((a,b)\sim(c,e)\) if \(a\oplus e\oplus k=c\oplus b\oplus k\) for some \(k\in A\).

(a) The relation \(\sim\) is an equivalence relation. The classes \([a,b]\) form a commutative ring \(G(A)\), with \([a,b]+[c,e]=[a\oplus c,b\oplus e]\), \([a,b]\,[c,e]=[ac\oplus be,ae\oplus bc]\), zero \([0,0]\), unit \([1,0]\) and \(-[a,b]=[b,a]\).

(b) \(j(a)=[a,0]\) is a morphism of semirings from \(A\) to \(G(A)\). For every morphism of semirings \(g\) from \(A\) to a ring \(B\), the map \([a,b]\mapsto g(a)-g(b)\) is the unique morphism of rings \(\bar g\colon G(A)\to B\) with \(\bar g\circ j=g\).

(c) \(1=0\) in \(G(A)\) if and only if \(1\oplus x=x\) for some \(x\in A\).

The ring \(G(A)\) is the *ring of differences* of \(A\).

*Proof.* (a) Take \(k=0\) for reflexivity; symmetry is clear. Let \(a\oplus e\oplus k=c\oplus b\oplus k\) and \(c\oplus h\oplus l=f\oplus e\oplus l\). Then
\[ a\oplus h\oplus(e\oplus k\oplus l)=b\oplus k\oplus(c\oplus h\oplus l)=b\oplus k\oplus f\oplus e\oplus l=f\oplus b\oplus(e\oplus k\oplus l), \]
so \((a,b)\sim(f,h)\). The sum is compatible with \(\sim\): add the two relations. For the product, let \(a\oplus b'\oplus k=a'\oplus b\oplus k\). Multiply this relation by \(c\), multiply it by \(e\) and exchange the two sides, and add the results:
\[ (ac\oplus be)\oplus(a'e\oplus b'c)\oplus(kc\oplus ke)=(a'c\oplus b'e)\oplus(ae\oplus bc)\oplus(kc\oplus ke). \]
This says \([a,b][c,e]=[a',b'][c,e]\). The product formula is symmetric in the two factors, so the product is well defined. In the product of three pairs, for either bracketing, the first coordinate is the sum of the products of three coordinates that contain an even number of second coordinates, and the second coordinate is the sum of the others; so the product is associative, and the distributive law follows in the same way. The class \([0,0]\) is neutral for the sum, \([1,0]\) for the product, and \([a,b]+[b,a]=[a\oplus b,a\oplus b]=[0,0]\).

(b) \(j\) preserves sums, products, \(0\) and \(1\). If \(a\oplus e\oplus k=c\oplus b\oplus k\), then \(g(a)+g(e)+g(k)=g(c)+g(b)+g(k)\) in \(B\), so \(g(a)-g(b)=g(c)-g(e)\). Thus \(\bar g\) is well defined, and it is a morphism of rings. It is unique because \([a,b]=j(a)-j(b)\).

(c) \([1,0]=[0,0]\) means that \(1\oplus 0\oplus x=0\oplus 0\oplus x\) for some \(x\). □

*Reference:* [Connes 2011, §4.2], where \(G(A)\) is called the symmetrization of \(A\).

**Proposition 6.17.** For \(x,y\in\widehat{M}\) put \(x+_wy=B(x,y)\), and put \(0+_wy=y+_w0=y\) for \(y\in\bar R_\rho\).

(a) \(A=(\bar R_\rho,+_w,\cdot)\) is a semiring.

(b) \(\rho^a+_w\rho^b=\rho^{\log(e^a+e^b)}\) for real \(a,b\).

(c) The map \(\kappa\) with \(\kappa(t)=\rho^{\log t}\) for \(t>0\) and \(\kappa(0)=0\) is an injective morphism of semirings from \(([0,\infty),+,\times)\) to \(A\).

*Proof.* (a) Since \(S(1-\alpha)=S(\alpha)\), \(F_{x,y}(\alpha)=F_{y,x}(1-\alpha)\); so \(+_w\) is commutative. The element \(0\) is neutral by definition.

*Associativity.* Let \(x,y,z\in\widehat{M}\). For \(0<a\le 1\), Lemma 6.14 (c), applied to \(u\mapsto u^a\) and then to the multiplication by \(\rho^{S(a)}z^{1-a}\), gives
\[ \rho^{S(a)}\,B(x,y)^a\,z^{1-a}=\sup_{0\le b\le 1}G(a,b),\qquad G(a,b)=\rho^{S(a)+aS(b)}\,x^{ab}\,y^{a(1-b)}\,z^{1-a}. \]
For \(a=0\) both sides are \(z\). The map \(G\) is continuous on \([0,1]^2\) by Proposition 6.13, so Lemma 6.14 (e) gives \((x+_wy)+_wz=\sup_{[0,1]^2}G\). Expanding the logarithms shows that
\[ S(a)+aS(b)=S\big(ab,\,a(1-b),\,1-a\big), \]
where \(S(p)=-\sum_ip_i\log p_i\) as in Section 6.2. So \(G(a,b)=J(ab,a(1-b),1-a)\), where \(J(p)=\rho^{S(p)}x^{p_1}y^{p_2}z^{p_3}\) on the simplex \(\Delta=\{p\in[0,1]^3\mid p_1+p_2+p_3=1\}\). The map \((a,b)\mapsto(ab,a(1-b),1-a)\) sends \([0,1]^2\) onto \(\Delta\): for \(p\in\Delta\) take \(a=p_1+p_2\), and \(b=p_1/a\) if \(a>0\). Hence \((x+_wy)+_wz\) is the least upper bound of the set \(J(\Delta)\). In the same way, \(x+_w(y+_wz)\) is the least upper bound of the elements \(\rho^{S(a)+(1-a)S(b)}x^ay^{(1-a)b}z^{(1-a)(1-b)}\); here \(S(a)+(1-a)S(b)=S\big(a,(1-a)b,(1-a)(1-b)\big)\), and \((a,b)\mapsto(a,(1-a)b,(1-a)(1-b))\) also sends \([0,1]^2\) onto \(\Delta\). So both sides are the least upper bound of \(J(\Delta)\). If one of \(x,y,z\) is \(0\), both sides are the \(+_w\)-sum of the other two.

*Distributivity.* For \(z\in\widehat{M}\), \(zF_{x,y}(\alpha)=F_{zx,zy}(\alpha)\), because \(z=z^\alpha z^{1-\alpha}\) and \((uv)^\alpha=u^\alpha v^\alpha\). Lemma 6.14 (c) gives \(z(x+_wy)=zx+_wzy\). The cases with a factor \(0\) are clear, and the multiplication is that of \(\bar R_\rho\).

(b) By Proposition 6.13 (e), \(s_n(\rho^a,\rho^b)=\rho^{c_n}\) with \(c_n=\max_{\alpha\in I(n)}\big(S(\alpha)+\alpha a+(1-\alpha)b\big)\). By Lemma 6.1, \(c_n\le c=\log(e^a+e^b)\), with equality at \(\alpha_*=e^a/(e^a+e^b)\). Some point of \(I(n)\) lies within \(1/n\) of \(\alpha_*\), and the function in brackets is continuous; so \(c_n\to c\). Since \(d(\rho^{c_n},\rho^c)=|c_n-c|\), \(s_n(\rho^a,\rho^b)\to\rho^c\).

(c) \(\kappa(st)=\kappa(s)\kappa(t)\) and \(\kappa(1)=1\) by Proposition 6.13 (e), and \(\kappa(s+t)=\kappa(s)+_w\kappa(t)\) by (b); the cases with \(0\) hold by definition. The map \(\kappa\) is injective because \(d(\rho^a,\rho^b)=|a-b|\) and \(\rho^a\neq 0\). □

*Reference:* [Connes 2011, Lemma 6.7, Proposition 6.8 and Corollary 6.9]. For \(s=S\), the function \(S(a)+aS(b)\) of \(p=(ab,a(1-b),1-a)\) is the function \(h\) in the proof of Proposition 6.5.

*Proof of Theorem 6.8.* Parts (a) and (b) are Lemma 6.10 and Proposition 6.13, part (c) is Proposition 6.15 (a), and part (d) is Proposition 6.17. Let \(W(R,\rho)=G(A)\).

*\(W(R,\rho)\neq 0\).* By Lemma 6.16 (c) we must show that \(1+_wx\neq x\) for every \(x\in\bar R_\rho\). For \(x=0\), \(1+_w0=1\neq 0\). Let \(x\in\widehat{M}\), and choose an integer \(N\ge 0\) with \(x\le\rho^N\) (Proposition 6.13 (c)). For \(0\le\alpha\le 1\), \(x^\alpha\le\rho^{N\alpha}\), so \(x=x^\alpha x^{1-\alpha}\le\rho^{N\alpha}x^{1-\alpha}\), that is, \(\rho^{-N\alpha}x\le x^{1-\alpha}\). The term of index \(\alpha\) of \(1+_wx\) is \(\rho^{S(\alpha)}x^{1-\alpha}\). Hence
\[ 1+_wx\ \ge\ \rho^{S(\alpha)-N\alpha}\,x\qquad(0\le\alpha\le 1). \]
For \(\alpha=e^{-N}/(1+e^{-N})\), Lemma 6.1 with \(a_1=-N\) and \(a_2=0\) gives \(S(\alpha)-N\alpha=\beta\), where \(\beta=\log(1+e^{-N})>0\). If \(1+_wx=x\), then \(\rho^\beta x\le 1\cdot x\), so \(\rho^\beta\le 1\) by Lemma 6.9 (c), applied in \(\bar R_\rho\). This contradicts \(1<\rho^\beta\) (Proposition 6.13 (e)).

*The algebra over \(\mathbb{R}\).* Define \(r\colon\mathbb{R}\to W(R,\rho)\) by \(r(t)=j(\kappa(t))\) for \(t\ge 0\) and \(r(t)=-j(\kappa(-t))\) for \(t<0\). On \([0,\infty)\), \(r\) preserves sums and products by Proposition 6.17 (c) and Lemma 6.16 (b), and \(r(-t)=-r(t)\) for all \(t\). For \(s\ge u\ge 0\), \(r(s)=r(s-u)+r(u)\), so \(r(s)+r(-u)=r(s-u)\). For \(0\le s<u\), the same argument gives \(r(s)+r(-u)=-r(u-s)=r(s-u)\). For two negative numbers, take negatives. Products follow from those of positive numbers and the rule of signs. So \(r\) is a morphism of rings, and \(r(1)=1\neq 0\). As \(\mathbb{R}\) is a field, \(r\) is injective, and \(W(R,\rho)\) is an algebra over \(\mathbb{R}\) with \(t\cdot w=r(t)\,w\). For \(t>0\), \(r(t)=[\rho^{\log t},0]\) and \(r(-t)=[0,\rho^{\log t}]\), and the product formula of Lemma 6.16 (a) gives the formulas of (e).

*Functoriality.* Let \(f:R\to R'\) be a morphism of semirings with \(f(\rho)=\rho'\). It preserves sums, hence the order. The equality \(f(x^{1/n})^n=f(x)\) gives \(f(x^q)=f(x)^q\) for rational \(q>0\), because \(x\mapsto x^n\) is injective on \(R'\) (Theorem 1.7). So \(f\) maps \([\rho^{-n},\rho^n]\) into \([\rho'^{-n},\rho'^n]\), \(M\) into \(M'\), and \(U_q\) into \(U'_q\); thus \(d(f(x),f(y))\le d(x,y)\). By Lemma 6.12 (c), \(f\) extends to a continuous map \(\bar f\colon\widehat{M}\to\widehat{M'}\); put \(\bar f(0)=0\). By continuity, \(\bar f\) preserves sums, products and real powers, and \(\bar f(\rho^a)=\rho'^a\). So \(\bar f(s_n(x,y))=s_n(\bar fx,\bar fy)\) and \(\bar f(x+_wy)=\bar f(x)+_w\bar f(y)\): \(\bar f\) is a morphism of semirings \(A\to A'\). By Lemma 6.16 (b) it induces a morphism of rings \(W(R,\rho)\to W(R',\rho')\), which maps \(r(t)\) to \(r'(t)\) and is therefore \(\mathbb{R}\)-linear. Identities and composites are preserved, by the uniqueness statements in Lemma 6.12 (c) and Lemma 6.16 (b). □

*Reference:* [Connes 2011, Theorem 6.11], whose proof contains the inequality \(1+_wx\ge\rho^\beta x\).

**Example 6.18.** (1) Let \(R=\mathbb{R}_+^{\max}\) and \(\rho=e^T\) with \(T>0\). Then \(R_\rho=R\), and \(d(x,y)=|\log x-\log y|/T\) for \(x,y>0\). This is a complete metric on \((0,\infty)\), so \(\bar R_\rho=R\). By Lemma 6.1, as in (6.1), the least upper bound of the terms \(e^{TS(\alpha)}x^\alpha y^{1-\alpha}\) is \(x+_Ty\). So \(x+_wy=x+_Ty\), and \(W(\mathbb{R}_+^{\max},e^T)\cong\mathbb{R}\) by Theorem 6.4 (b).

(2) In Example 6.11, \(d((a,b),(a,0))=0\) and \(d((a,0),(c,0))=|a-c|\). So \(\widehat{M}=\{\rho^a\mid a\in\mathbb{R}\}\), the map \(\kappa\) of Proposition 6.17 (c) is surjective, and it is an isomorphism of semirings from \(([0,\infty),+,\times)\) to \(A\). Hence \(W(R,(1,0))\cong\mathbb{R}\). The second coordinate disappears in the completion.

### 6.6 The construction with given suprema

[Connes–Consani 2011b, Theorem 2.20] is an earlier form of the construction. It uses least upper bounds that are assumed to exist, instead of the completion of Section 6.5. This section states it with a precise hypothesis, proves it, and compares the two constructions.

Let \(K\) be a semiring of characteristic one with automorphisms \(\vartheta_t\), \(t\in\mathbb{R}_{>0}\), such that \(\vartheta_n(x)=x^n\) for integers \(n\ge 1\), \(\vartheta_s\vartheta_t=\vartheta_{st}\) and \(\vartheta_s(x)\vartheta_t(x)=\vartheta_{s+t}(x)\). This is the notion of perfection of [Connes–Consani 2011b, Definition 2.17] (see the reference after Definition 1.9). We write \(x^t=\vartheta_t(x)\). The semiring \(K\) need not be multiplicatively cancellative. Let \(\sigma\in K\) satisfy \(\sigma\le 1\), and assume that \(\sigma\) can be cancelled: \(\sigma x=\sigma y\) implies \(x=y\). Let \(L\) be the set of fractions \(x/\sigma^n\), \(x\in K\), \(n\ge 0\), where \(x/\sigma^n=y/\sigma^m\) means \(x\sigma^m=y\sigma^n\), with the usual sum and product of fractions.

**Lemma 6.19.** \(L\) is a semiring of characteristic one, \(x\mapsto x/1\) is an injective morphism from \(K\) to \(L\), and \(\sigma\) is invertible in \(L\). The automorphisms \(\vartheta_t\) extend uniquely to automorphisms of \(L\), and the extensions have the same three properties.

*Proof.* The relation is transitive: from \(x\sigma^m=y\sigma^n\) and \(y\sigma^k=z\sigma^m\) we get \(x\sigma^{m+k}=y\sigma^{n+k}=z\sigma^{m+n}\), and cancelling \(\sigma^m\) gives \(x\sigma^k=z\sigma^n\). The sum \(x/\sigma^n+y/\sigma^m=(x\sigma^m+y\sigma^n)/\sigma^{n+m}\) and the product \(xy/\sigma^{n+m}\) are compatible with the relation, and the axioms reduce to those of \(K\) on a common denominator. The map \(x\mapsto x/1\) is injective by the definition of the relation, and \(1/\sigma\) is inverse to \(\sigma/1\). For \(t>0\) and an integer \(m>t\), \(\vartheta_t(\sigma)\vartheta_{m-t}(\sigma)=\vartheta_m(\sigma)=\sigma^m\), so \(\vartheta_t(\sigma)\) is invertible in \(L\). Hence \(\vartheta_t(x/\sigma^n)=\vartheta_t(x)\,\vartheta_t(\sigma)^{-n}\) is the only possible extension. It is well defined: \(x\sigma^m=y\sigma^n\) gives \(\vartheta_t(x)\vartheta_t(\sigma)^m=\vartheta_t(y)\vartheta_t(\sigma)^n\). It is a morphism of semirings, its inverse is the extension of \(\vartheta_{1/t}\), and the three properties hold on fractions because they hold on numerators and on \(\sigma\). □

*Reference:* [Connes–Consani 2011b, Proposition 2.18], where \(\sigma\) is written \(\rho\) and \(L\) is written \(K_\rho\).

Put \(\rho=\sigma^{-1}\in L\). Multiplying \(\sigma\le 1\) by \(\rho\) gives \(\rho\ge 1\). For real \(s\) put \(\rho^s=\vartheta_s(\rho)\) if \(s>0\), \(\rho^0=1\), and \(\rho^s=\vartheta_{-s}(\sigma)\) if \(s<0\). By the three properties, \(\rho^s\rho^t=\rho^{s+t}\) for real \(s,t\), and \((\rho^s)^t=\rho^{st}\) for real \(s\) and \(t>0\). Moreover \(\rho^s\le\rho^t\) for \(s<t\), since \(\rho^{t-s}=\vartheta_{t-s}(\rho)\ge\vartheta_{t-s}(1)=1\). For \(x,y\in L\) and \(0\le\alpha\le 1\) put \(F_{x,y}(\alpha)=\rho^{S(\alpha)}x^\alpha y^{1-\alpha}\), meaning \(y\) for \(\alpha=0\) and \(x\) for \(\alpha=1\). In [Connes–Consani 2011b] the weight is written \(\sigma^{-S(\alpha)}\). Consider the two conditions:

- (S1) for all \(x,y\in L\), the elements \(F_{x,y}(\alpha)\), \(0\le\alpha\le 1\), have a least upper bound \(B(x,y)\) in \(L\);
- (S2) for all \(x,y,z\in L\), the elements \(zF_{x,y}(\alpha)\), \(0\le\alpha\le 1\), have the least upper bound \(zB(x,y)\).

[Connes–Consani 2011b, §2.4] assumes that the idempotent integrals it uses exist, regards them as least upper bounds, and leaves the technical aspects aside. Its proof of associativity and distributivity moves the multiplication by an element, and the automorphisms \(\vartheta_t\), through these least upper bounds. For the automorphisms this needs no hypothesis: an automorphism preserves the order, and so does its inverse, so it maps a least upper bound to a least upper bound. For the multiplication it is condition (S2). Example 6.21 shows that (S2) does not follow from (S1), even when \(K\) is multiplicatively cancellative.

**Theorem 6.20.** Assume (S1) and (S2), and put \(x\oplus y=B(x,y)\).

(a) \((L,\oplus,\cdot)\) is a semiring.

(b) \(\rho^a\oplus\rho^b=\rho^{\log(e^a+e^b)}\) for real \(a,b\). The map \(\kappa\) with \(\kappa(t)=\rho^{\log t}\) for \(t>0\) and \(\kappa(0)=0\) is a morphism of semirings from \(([0,\infty),+,\times)\) to \((L,\oplus,\cdot)\), and the ring of differences \(W(K,\sigma)\) of \((L,\oplus,\cdot)\) is an algebra over \(\mathbb{R}\). It can be the zero ring; if it is not, the map \(\mathbb{R}\to W(K,\sigma)\) is injective.

(c) Let \((K',\sigma')\) be another pair as above that satisfies (S1) and (S2), and let \(f:L\to L'\) be a morphism of semirings with \(f(\sigma)=\sigma'\), \(f\circ\vartheta_t=\vartheta'_t\circ f\) for all \(t>0\), and \(f(B(x,y))=B'(f(x),f(y))\) for all \(x,y\in L\). Then \(f\) induces a morphism of \(\mathbb{R}\)-algebras \(W(K,\sigma)\to W(K',\sigma')\).

*Proof.* First, (S2) implies that \(zB(x,y)^t\) is the least upper bound of the elements \(zF_{x,y}(\alpha)^t\), for real \(t>0\): apply (S2) with the multiplier \(z^{1/t}\), and then the automorphism \(\vartheta_t\).

(a) Commutativity follows from \(F_{x,y}(\alpha)=F_{y,x}(1-\alpha)\). For \(0<\alpha<1\), \(0^\alpha=\vartheta_\alpha(0)=0\), so \(B(x,0)=x\) and \(0\) is neutral. Distributivity: \(zF_{x,y}(\alpha)=F_{zx,zy}(\alpha)\), because \(z=z^\alpha z^{1-\alpha}\); now apply (S2). Associativity: if one of \(x,y,z\) is \(0\), both sides are the \(\oplus\)-sum of the other two. Otherwise \((x\oplus y)\oplus z\) is the least upper bound of the elements \(F_{B(x,y),z}(a)\), \(0\le a\le 1\). For \(0<a\le 1\), the first remark, with the multiplier \(\rho^{S(a)}z^{1-a}\) and \(t=a\), shows that \(F_{B(x,y),z}(a)\) is the least upper bound of the elements \(G(a,b)=\rho^{S(a)+aS(b)}x^{ab}y^{a(1-b)}z^{1-a}\), \(0\le b\le 1\), where a factor with exponent \(0\) is omitted. Put \(G(0,b)=z\). An element is an upper bound of all \(F_{B(x,y),z}(a)\) if and only if it is an upper bound of all \(G(a,b)\). So \((x\oplus y)\oplus z\) is the least upper bound of the set of all \(G(a,b)\). As in the proof of Proposition 6.17 (a), this set is the set of the elements \(\rho^{S(p)}x^{p_1}y^{p_2}z^{p_3}\), \(p\in\Delta\), and so is the corresponding set for \(x\oplus(y\oplus z)\).

(b) Since \(s\mapsto\rho^s\) is nondecreasing, the element \(F_{\rho^a,\rho^b}(\alpha)=\rho^{S(\alpha)+\alpha a+(1-\alpha)b}\) is largest at \(\alpha=e^a/(e^a+e^b)\), by Lemma 6.1. So \(\rho^a\oplus\rho^b=\rho^{\log(e^a+e^b)}\), and \(\kappa\) is a morphism of semirings as in Proposition 6.17 (c). The construction of \(r\) in the proof of Theorem 6.8 gives a morphism of rings \(r\colon\mathbb{R}\to W(K,\sigma)\). It is injective unless \(W(K,\sigma)=0\), because \(\mathbb{R}\) is a field.

(c) By the hypothesis on \(f\), it is a morphism of semirings from \((L,\oplus,\cdot)\) to \((L',\oplus',\cdot)\). It maps \(\rho^s\) to \(\rho'^s\), hence \(\kappa(t)\) to \(\kappa'(t)\). Lemma 6.16 (b) gives a morphism of rings \(W(K,\sigma)\to W(K',\sigma')\), and it maps \(r(t)\) to \(r'(t)\). □

*Reference:* [Connes–Consani 2011b, Theorem 2.20]. The theorem there does not state (S2), and it does not specify the morphisms for which the construction is functorial. Its proof notes that \(W(K,\sigma)\) can be the zero ring.

**Example 6.21 (condition (S2) is needed).** Let \(C\) be the real vector space of convergent real sequences, \(C_0\subset C\) the subspace of the sequences that are eventually \(0\), and \(G=C/C_0\). Order \(C\) by \(a\le b\) if \(a_n\le b_n\) for all \(n\), and \(G\) by \([a]\le[b]\) if \(a_n\le b_n\) for all large \(n\). For the addition of sequences, both are ordered groups in which the least upper bound of two elements is the termwise maximum. Let \(P=C\sqcup\{0_P\}\) and \(Q=G\sqcup\{0_Q\}\) be the corresponding semifields of characteristic one (Proposition 1.4). In this example the group laws of \(C\) and \(G\), which are the multiplications of \(P\) and \(Q\), are written additively; so the unit of \(P\) is the zero sequence \(0\), and \(\vartheta_t\) is the multiplication of sequences by \(t\). The quotient map \(h\colon P\to Q\) is a morphism of semirings that commutes with all \(\vartheta_t\). Let \(\mathbf{1}\) be the constant sequence \(1\), and \(\mathbf{v}=(1/n)_{n\ge 1}\).

(i) Take \(\sigma=-\mathbf{1}\) in \(P\) and \(\sigma=-[\mathbf{1}]\) in \(Q\). In \(P\), for \(x,y\in C\), the element \(F_{x,y}(\alpha)\) is the sequence \(S(\alpha)\mathbf{1}+\alpha x+(1-\alpha)y\), and by Lemma 6.1 the least upper bound \(B_P(x,y)\) is the convergent sequence \(\big(\log(e^{x_n}+e^{y_n})\big)_n\). In \(Q\), let \(x_n\to\bar x\) and \(y_n\to\bar y\), and put \(p=e^{\bar x}/(e^{\bar x}+e^{\bar y})\). For \(\alpha\neq p\), the difference between the terms of index \(p\) and \(\alpha\) converges to \(\big(S(p)+p\bar x+(1-p)\bar y\big)-\big(S(\alpha)+\alpha\bar x+(1-\alpha)\bar y\big)>0\) (Lemma 6.1). It is eventually positive, so the term of index \(p\) is the largest term, and \(B_Q([x],[y])=[S(p)\mathbf{1}+px+(1-p)y]\). In \(P\) and \(Q\), multiplication by a nonzero element is an order automorphism, so (S1) and (S2) hold.

(ii) Let \(K=\{(0_P,0_Q)\}\cup\{(x,\xi)\in C\times G\mid h(x)\le\xi\}\), with the operations and the \(\vartheta_t\) of \(P\times Q\). The inequality \(h(x)\le\xi\) is preserved by sums, products and the \(\vartheta_t\), so \(K\) is a semiring with automorphisms \(\vartheta_t\) as above, and it is multiplicatively cancellative. The element \(\sigma=(-\mathbf{1},-[\mathbf{1}])\) and its inverse \((\mathbf{1},[\mathbf{1}])\) lie in \(K\), so \(\sigma<1\) is invertible and \(L=K\). The order of \(K\) is the componentwise order. If a family of nonzero elements of \(K\) has least upper bounds \(X\) in \(P\) and \(\Xi\) in \(Q\) of its two families of coordinates, then \((X,\Xi\vee h(X))\) is its least upper bound in \(K\), where \(\vee\) is the least upper bound in \(G\). Indeed this element lies in \(K\) and is an upper bound, and an upper bound \((y,\eta)\in K\) satisfies \(y\ge X\), \(\eta\ge\Xi\) and \(\eta\ge h(y)\ge h(X)\). By (i), (S1) holds for \(K\).

(iii) Let \(X=(\mathbf{v},h(\mathbf{v}))\), \(Y=(0,[0])\), which is the unit of \(K\), and \(Z=(0,[\mathbf{1}])\). Put \(U=B_P(\mathbf{v},0)=\big(\log(1+e^{1/n})\big)_n\), \(H=h(U)\), and \(V=B_Q(h(\mathbf{v}),[0])=\big[\big(\log 2+\tfrac1{2n}\big)_n\big]\). For \(t>0\), \(2e^{t/2}<1+e^t<2e^t\), since \((e^{t/2}-1)^2>0\) and \(1<e^t\). With \(t=1/n\), this gives \(V<H<V+[\mathbf{1}]\) in \(G\). By (ii), the least upper bound in \(K\) of the elements \(F_{X,Y}(\alpha)\) is \(B_K(X,Y)=(U,V\vee H)=(U,H)\). Multiplication by \(Z\) adds \([\mathbf{1}]\) to the second coordinate, and this is an order automorphism of \(Q\). So \(B_K(ZX,ZY)=(U,(V+[\mathbf{1}])\vee H)=(U,V+[\mathbf{1}])\). But \(Z\,B_K(X,Y)=(U,H+[\mathbf{1}])\), which is different. So the multiplication of \(K\) is not distributive over \(B_K\), although \(K\) satisfies (S1), is multiplicatively cancellative, and \(\sigma<1\) is invertible. Condition (S2) fails for the multiplier \(Z\), which is not invertible in \(K\).

(iv) The morphism \(h\) commutes with the \(\vartheta_t\) and maps the element \(\sigma\) of \(P\) to that of \(Q\), but \(h(B_P(\mathbf{v},0))=H\neq V=B_Q(h(\mathbf{v}),h(0))\). So the condition \(f(B(x,y))=B'(f(x),f(y))\) in Theorem 6.20 (c) does not follow from the other conditions on \(f\).

**Example 6.22 (the two constructions can differ).** Let \(R\) be the semifield of Example 6.11, with \(\vartheta_t(a,b)=(ta,tb)\). In \(R\), multiplication by a nonzero element is an order automorphism, so (S2) follows from (S1).

(1) Take \(\sigma=(-1,0)\), so \(\rho=(1,0)\). For \(x=(a_1,b_1)\) and \(y=(a_2,b_2)\), the first coordinate \(S(\alpha)+\alpha a_1+(1-\alpha)a_2\) of \(F_{x,y}(\alpha)\) is largest exactly at \(\alpha=p=e^{a_1}/(e^{a_1}+e^{a_2})\) (Lemma 6.1). In the lexicographic order the term of index \(p\) is therefore the largest term, and
\[ B(x,y)=\Big(\log(e^{a_1}+e^{a_2}),\ \frac{e^{a_1}b_1+e^{a_2}b_2}{e^{a_1}+e^{a_2}}\Big). \]
Let \(D=\mathbb{R}[\varepsilon]/(\varepsilon^2)\). The map \((a,b)\mapsto e^a(1+b\varepsilon)\), \(0\mapsto 0\), is an isomorphism from \((R,B,\cdot)\) onto the sub-semiring \(D_+=\{0\}\cup\{u+v\varepsilon\mid u>0\}\) of \(D\). It is bijective, it is multiplicative because \(e^{a_1}(1+b_1\varepsilon)\,e^{a_2}(1+b_2\varepsilon)=e^{a_1+a_2}(1+(b_1+b_2)\varepsilon)\), and it is additive because \(e^{a_1}(1+b_1\varepsilon)+e^{a_2}(1+b_2\varepsilon)=(e^{a_1}+e^{a_2})+(e^{a_1}b_1+e^{a_2}b_2)\varepsilon\). The ring of differences of \(D_+\) is \(D\): the map \([u,v]\mapsto u-v\) is injective, because \(u-v=u'-v'\) in \(D\) means \(u+v'=u'+v\) in \(D_+\); and it is surjective, because \(u+v\varepsilon=(u+m+v\varepsilon)-m\) for a real number \(m>\max(0,-u)\). So \(W(R,\sigma)\cong D\), which contains the nonzero nilpotent element \(\varepsilon\). For the same \(\rho\), Section 6.5 gives \(W(R,\rho)\cong\mathbb{R}\) (Example 6.18 (2)).

(2) Take \(\sigma=(0,-1)\), so \(\rho=(0,1)\). For \(x=(a_1,b_1)\) and \(y=(a_2,b_2)\), the first coordinate of \(F_{x,y}(\alpha)\) is \(\alpha a_1+(1-\alpha)a_2\). If \(a_1>a_2\), the term of index \(1\), which is \(x\), is the largest term, so \(B(x,y)=x\); if \(a_1=a_2\), \(B(x,y)=(a_1,\log(e^{b_1}+e^{b_2}))\). In particular \(B(1,(1,0))=(1,0)\), and \(W(R,\sigma)=0\) by Lemma 6.16 (c), although \(\sigma<1\). For the same \(\rho\), the set \(M\) of Section 6.5 is \(\{(0,b)\mid b\in\mathbb{R}\}=\{\rho^b\mid b\in\mathbb{R}\}\), with \(d(\rho^{b_1},\rho^{b_2})=|b_1-b_2|\); so \(W(R,\rho)\cong\mathbb{R}\), as in Example 6.18 (2).

**Remark 6.23 (the hypotheses compared).** (a) If \(K\) is multiplicatively cancellative and \(\sigma\neq 1\), then \(L\) is multiplicatively cancellative and perfect in the sense of Definition 1.9, and \(\rho=\sigma^{-1}\) satisfies \(\rho\ge 1\) and \(\rho\neq 1\). So Section 6.5 applies to \(L\) and \(\rho\). It keeps only the elements bounded by powers of \(\rho\), and it identifies elements at distance \(0\); by Example 6.22 the two rings can differ. Conversely, the semiring \(\bar R_\rho\) of Section 6.5 satisfies the hypotheses of Theorem 6.20 with \(\sigma=\rho^{-1}\), by Propositions 6.13 and 6.15 (a) and Lemma 6.14 (c). There both constructions give \(W(R,\rho)\).

(b) Neither set of hypotheses implies the other. The semiring \([0,\infty)^2\), with the coordinatewise maximum and product, \(\vartheta_t(u,v)=(u^t,v^t)\) and \(\sigma=(e^{-1},e^{-1})\), satisfies (S1) and (S2), and \(B\) is the coordinatewise ordinary sum (Lemma 6.1). It is not multiplicatively cancellative: \((1,0)(1,1)=(1,0)(1,2)\). In the other direction, let \(R'\) consist of \(0\) and the functions \(e^f\) on \([0,1]\), where \(f\) is continuous, convex, and affine on each interval of some finite partition of \([0,1]\), with the pointwise maximum and product. It is a perfect, multiplicatively cancellative semiring of characteristic one, and Section 6.5 applies to it with \(\rho\) the constant function \(e\). Let \(x(\tau)=e^\tau\) and \(y=1\). The terms \(e^{S(\alpha)+\alpha\tau}\) have the pointwise supremum \(e^{h(\tau)}\), \(h(\tau)=\log(1+e^\tau)\). If \(e^g\in R'\) were their least upper bound in \(R'\), then \(g\ge h\). The functions \(h_n\) that agree with \(h\) at the points \(k/n\) and are affine in between are convex, satisfy \(h_n\ge h\) because \(h\) is convex, and \(e^{h_n}\in R'\). So \(g\le h_n\) for all \(n\), and \(g=h\). But \(h''>0\), so \(h\) is affine on no interval. Hence (S1) fails for \(R'\).

## 7. Exercises

**Exercise 1 (endomorphisms of the tropical semifields).** (a) Show that the endomorphisms of the semiring \(\mathbb{Z}_{\max}\) are the maps \(\mathrm{Fr}_c:x\mapsto cx\), \(-\infty\mapsto-\infty\), for the integers \(c\ge 0\). Which of them are injective? (b) Show that the automorphisms of \(\mathbb{R}_{\max}\) are the maps \(x\mapsto\lambda x\) with \(\lambda>0\) real.

*Solution.* (a) Let \(f\) be an endomorphism. It fixes \(-\infty\) and the integer \(0\), and it satisfies \(f(x+y)=f(x)+f(y)\) and \(f(\max(x,y))=\max(f(x),f(y))\). For \(x\in\mathbb{Z}\), \(f(x)+f(-x)=f(0)=0\), so \(f(x)\neq-\infty\). So \(f\) restricts to a homomorphism of groups \(\mathbb{Z}\to\mathbb{Z}\), and \(f(x)=cx\) with \(c=f(1)\). From \(\max(1,0)=1\) we get \(\max(c,0)=c\), so \(c\ge 0\). Conversely \(\mathrm{Fr}_c\) preserves \(\max\) and \(+\) for every \(c\ge 0\). It is injective if and only if \(c\ge 1\). The map \(\mathrm{Fr}_0\) sends every integer to \(0\); it is the composite \(\mathbb{Z}_{\max}\to\mathbb{B}\to\mathbb{Z}_{\max}\) of Example 2.5. Since \(\mathrm{Fr}_c\mathrm{Fr}_d=\mathrm{Fr}_{cd}\), the injective endomorphisms form a monoid isomorphic to the multiplicative monoid of positive integers. Only \(\mathrm{Fr}_1\) is an automorphism.

(b) An automorphism \(f\) restricts to a bijection \(\mathbb{R}\to\mathbb{R}\) which is additive, and nondecreasing because it preserves \(\max\). Put \(\lambda=f(1)\). Then \(f(q)=q\lambda\) for rational \(q\). We have \(\lambda\ge 0\), and \(\lambda\neq 0\) because \(f\) is injective. For real \(x\) and rational \(q < x < q'\) we get \(q\lambda\le f(x)\le q'\lambda\). So \(f(x)=\lambda x\). Conversely \(x\mapsto\lambda x\) is an automorphism for \(\lambda>0\).

**Exercise 2 (congruences).** Let \(G=\mathbb{Z}^2\), with its addition. Let \(F_1\) be the semifield of Proposition 1.4 for the product order: \((a,b)\le(a',b')\) when \(a\le a'\) and \(b\le b'\). Let \(F_2\) be the one for the lexicographic order: \((a,b)\le(a',b')\) when \(a < a'\), or \(a=a'\) and \(b\le b'\). Find all congruences on \(F_1\) and on \(F_2\), and their quotients.

*Solution.* By Proposition 2.4 we need the convex subgroups \(N\) of \(G\) that are closed under least upper bounds.

*Product order.* The least upper bound is the componentwise maximum. Let \((a,b)\in N\). Then \((|a|,|b|)\), the least upper bound of \((a,b)\) and \((-a,-b)\), is in \(N\). By convexity \(N\) contains every \((c,d)\) with \(0\le c\le|a|\) and \(0\le d\le|b|\). So \(N\) contains \((1,0)\) if \(a\neq 0\), and \((0,1)\) if \(b\neq 0\). Hence \(N\) is one of \(0\), \(\mathbb{Z}\times 0\), \(0\times\mathbb{Z}\), \(\mathbb{Z}^2\). Each of these is a convex subgroup closed under least upper bounds. So \(F_1\) has five congruences. The quotients are \(F_1\); \(\mathbb{Z}_{\max}\) in two ways, by the morphisms \((a,b)\mapsto b\) and \((a,b)\mapsto a\); \(\mathbb{B}\); and \(\{0\}\).

*Lexicographic order.* The order is total, so every subgroup is closed under least upper bounds. Let \(N\) be a convex subgroup that contains some \((a,b)\) with \(a>0\). For any \((c,d)\) choose \(m\) with \(ma>|c|\). Then \(-m(a,b)\le(c,d)\le m(a,b)\), so \((c,d)\in N\). Hence \(N=\mathbb{Z}^2\). Otherwise \(N\subseteq 0\times\mathbb{Z}\), and \(N\) is \(0\) or \(0\times\mathbb{Z}\) as in Example 2.5. The subgroup \(0\times\mathbb{Z}\) is convex. So \(F_2\) has four congruences. The quotients are \(F_2\); \(\mathbb{Z}_{\max}\), by the morphism \((a,b)\mapsto a\); \(\mathbb{B}\); and \(\{0\}\).

**Exercise 3 (a hyperfield with four elements).** Let \(H=\mathbb{F}_7/\{\pm 1\}\), with elements \(0\), \(a=[1]\), \(b=[2]\), \(c=[3]\). (a) Compute the products and the sums in \(H\). (b) Show that \(H\) is a hyperfield which is an extension neither of \(\mathbf{K}\) nor of \(\mathbf{S}\). (c) Determine the morphisms \(H\to\mathbf{K}\), \(\mathbf{K}\to H\), \(H\to\mathbf{S}\) and \(H\to\mathbf{T}\).

*Solution.* (a) \(b^2=[4]=[-3]=c\), \(bc=[6]=[-1]=a\) and \(c^2=[9]=[2]=b\). So \(H^\times=\{a,b,c\}\) is cyclic of order \(3\), with unit \(a\). The elements of \([x]+[y]\) are \([x+y]\) and \([x-y]\). So \(a+a=\{[2],[0]\}=\{0,b\}\), \(a+b=\{[3],[-1]\}=\{a,c\}\) and \(a+c=\{[4],[-2]\}=\{b,c\}\). Multiplying by \(b\) and by \(c\) gives \(b+b=\{0,c\}\), \(b+c=\{a,b\}\) and \(c+c=\{0,a\}\).

(b) \(H\) is a hyperfield by Theorem 3.5, since \(\mathbb{F}_7\) is a field. Its unit is \(a\), and \(a+a=\{0,b\}\) is neither \(\{0,a\}\) nor \(\{a\}\).

(c) By Theorem 3.5 (c) the only prime ideal of \(H\) is \(\{0\}\). By Theorem 3.13 (a) there is exactly one morphism \(H\to\mathbf{K}\); it sends every nonzero element to \(1\). A morphism \(f:\mathbf{K}\to H\) would satisfy \(f(1+1)=\{0,a\}\subseteq a+a=\{0,b\}\), which is false. So there is none. A morphism \(f:H\to\mathbf{S}\) would give a morphism \(f\pi:\mathbb{F}_7\to\mathbf{S}\), hence an ordering of \(\mathbb{F}_7\) by Theorem 3.13 (b). A finite field has no ordering. So there is none. A morphism \(f:H\to\mathbf{T}\) gives a map \(v=f\pi\) on \(\mathbb{F}_7\) as in Theorem 3.13 (c). Since every nonzero element of \(\mathbb{F}_7\) is a root of unity, \(v(x)=1\) for \(x\neq 0\). So \(f(x)=1\) for \(x\neq 0\). This map is a morphism, because \(f(x+y)\subseteq\{0,1\}\subseteq[0,1]=1\boxplus 1\) for nonzero \(x,y\). So there is exactly one morphism \(H\to\mathbf{T}\).

**Exercise 4 (the tropical hyperfield).** (a) Let \(a_1,\dots,a_n\ge 0\) have maximum \(m\), with \(n\ge 2\). Show that \(a_1\boxplus\dots\boxplus a_n\) is \([0,m]\) if \(m\) occurs at least twice among the \(a_i\), and \(\{m\}\) otherwise. Deduce that \(0\in a_1\boxplus\dots\boxplus a_n\) if and only if the maximum occurs at least twice. (b) Let \(F\) be a field with a nonarchimedean absolute value \(|\cdot|\), let \(U=\{x:|x|=1\}\), and assume that the residue field has more than two elements. Show that \([x]\mapsto|x|\) identifies the hyperfield \(F/U\) with the set \(|F|\) of values, with the sums \((a\boxplus b)\cap|F|\). What changes for \(F=\mathbb{Q}_2\)? (c) Let \(R=\{0\}\cup[1,\infty)\), a sub-semiring of the real numbers, and let \(v(0)=0\), \(v(x)=1/x\) for \(x\neq 0\). Show that \(v\) satisfies the four conditions of Theorem 3.13 (c), but that \(v(1+2)\notin v(1)\boxplus v(2)\).

*Solution.* (a) By induction on \(n\). The case \(n=2\) is the definition. Let \(n\ge 3\), let \(B=a_1\boxplus\dots\boxplus a_{n-1}\) and let \(m'\) be the maximum of \(a_1,\dots,a_{n-1}\). Suppose \(B=\{m'\}\), so \(m'\) occurs once among the first \(n-1\) terms. Then \(B\boxplus a_n=m'\boxplus a_n\). If \(a_n\neq m'\) this is \(\{\max(m',a_n)\}=\{m\}\), and \(m\) occurs once. If \(a_n=m'\) it is \([0,m]\), and \(m\) occurs twice. Suppose \(B=[0,m']\), so \(m'\) occurs at least twice. If \(a_n>m'\), every \(e\boxplus a_n\) with \(e\in B\) is \(\{a_n\}=\{m\}\), and \(m\) occurs once. If \(a_n\le m'\), the union of the \(e\boxplus a_n\) is \([0,a_n]\cup\{a_n\}\cup(a_n,m']=[0,m']\), and \(m=m'\) occurs at least twice. For the last statement: if \(m\) occurs once, then \(m>0\), so \(0\notin\{m\}\).

(b) Two nonzero elements have the same class if and only if they have the same absolute value. So \([x]\mapsto|x|\) is a bijection from \(F/U\) to \(|F|\), and it is multiplicative. The sum \([x]+[y]\) is the set of values \(|xu+yu'|\) with \(u,u'\in U\). If \(|x|>|y|\), all these values are \(|x|\). Let \(|x|=|y|=r>0\) and \(c=y/x\in U\). Then \(|xu+yu'|=r\,|u+cu'|\le r\). If \(|t| < 1\), then \(u=t-c\) is in \(U\), and \(u+c\cdot 1=t\). So every value less than \(1\) occurs as \(|u+cu'|\). Since the residue field has more than two elements, there is \(u\in U\) whose residue class is not that of \(-c\). Then \(|u+c|=1\). So the set of values \(|u+cu'|\) is \([0,1]\cap|F|\), and \([x]+[y]\) corresponds to \([0,r]\cap|F|=(r\boxplus r)\cap|F|\). For \(F=\mathbb{Q}_2\) the residue field is \(\mathbb{F}_2\), and the sum of two units is never a unit. So \([1]+[1]\) corresponds to the values less than \(1\): the value \(1\) of \(1\boxplus 1\) is missing.

(c) \(v(0)=0\), \(v(1)=1\) and \(v(xy)=v(x)v(y)\). For \(x,y\ge 1\) we have \(v(x+y)=1/(x+y) < \max(1/x,1/y)\). But \(v(1+2)=1/3\) and \(v(1)\boxplus v(2)=1\boxplus\tfrac12=\{1\}\).

**Exercise 5 (three points on a line are not enough).** Let \(\mathcal{P}\) be the projective plane over \(\mathbb{F}_2\), with seven points and three points on each line. Define sums on \(E=\mathcal{P}\cup\{0\}\) as in Theorem 4.2 (b). Show that (H2) fails. Which step of the proof of Theorem 4.2 uses four points?

*Solution.* Let \(x\neq z\) be points and let \(w\) be the third point of \(L(x,z)\). Then \(x+z=\{w\}\) and \(x+w=\{z\}\). So \((x+x)+z=\{0,x\}+z=\{z,w\}\), and \(x+(x+z)=x+w=\{z\}\). These differ. In the proof of Theorem 4.2 (b), Case 2 needs two points of \(L(x,z)\) other than \(x\) and \(z\). Case 3 needs a fourth point on the line as well: for the three points \(x,z,w\) of a line here, \((x+z)+w=w+w=\{0,w\}\) and \(x+(z+w)=x+x=\{0,x\}\).

**Exercise 6 (a line in the adèle class space).** Let \(k=\mathbb{Q}\) and let \(e\in\mathbb{A}_\mathbb{Q}\) be the adèle with component \(1\) at the real place and \(0\) at every prime. Describe \(\pi(1)+\pi(e)\) in \(\mathbb{H}_\mathbb{Q}\). Which of its elements are units, and which are prime elements?

*Solution.* The sum is the set of \(\pi(g+he)\) with \(g,h\in\mathbb{Q}^\times\), that is, the set of \(\pi(1+te)\) with \(t\in\mathbb{Q}^\times\). The adèle \(1+te\) has component \(1+t\) at the real place and \(1\) at every prime. For \(t\neq-1\) it is an idèle, so \(\pi(1+te)\) is a unit. For \(t=-1\) it is \(1_{\Sigma\setminus\{\infty\}}\), and \(\pi(1-e)=\varpi_\infty\) is a prime element over the real place. Different \(t\) give different classes: if \(1+te=q(1+t'e)\) with \(q\in\mathbb{Q}^\times\), the components at a prime give \(q=1\), and then \(t=t'\). So \(t\mapsto\pi(1+te)\) is a bijection from \(\mathbb{Q}^\times\) to \(\pi(1)+\pi(e)\). This is the projective line through \(\pi(1)\) and \(\pi(e)\) without these two points, as in Theorem 5.1 (c). It contains one prime element.

**Exercise 7 (entropy).** (a) Compute the sum \(1+_T\dots+_T1\) of \(n\) terms, and say which \(p\) attains the supremum in Theorem 6.4 (a). (b) Let \(\ell(n)=v_2(n)\) be the exponent of \(2\) in \(n\). Compute the function \(s\) of Theorem 6.6 (a) at \(1/2\), at \(1/3\) and at \(2^{-j}\). Is \(s\) a weight? (c) For \(T>0\), show that \(s=-TS\) satisfies (C) and (A), and determine \(+_s\).

*Solution.* (a) The sum is \(n^T\), by Theorem 6.4 (a). The supremum of \(e^{TS(p)}\) is attained at \(p=(1/n,\dots,1/n)\) only, by Lemma 6.1 with \(a_i=0\); there \(S(p)=\log n\).

(b) \(s(1/2)=\ell(2)-\tfrac12\ell(1)-\tfrac12\ell(1)=1\). \(s(1/3)=\ell(3)-\tfrac13\ell(1)-\tfrac23\ell(2)=-\tfrac23\). \(s(2^{-j})=\ell(2^j)-2^{-j}\ell(1)-(1-2^{-j})\,\ell(2^j-1)=j\), because \(2^j-1\) is odd. So \(s\) is not bounded above, and it is not a weight: the supremum that would define \(1+_s1\) is infinite. By Theorem 6.6 (a), \(s\) satisfies (C) and (A). Since \(s(1/3) < 0\), this does not contradict Theorem 6.6 (b).

(c) \(\ell=-T\log\) satisfies \(\ell(mn)=\ell(m)+\ell(n)\), and the formula of Theorem 6.6 (a) gives \(s=-TS\). So (C) and (A) hold. As \(s\le 0\), Lemma 6.3 (c) gives \(x+_sy=\max(x,y)\).

## 8. What this lesson does not prove

The following results are stated in the lesson and not proved.

1. [Connes–Consani 2011c, Theorem 3.8]: a hyperfield extension of \(\mathbf{K}\) whose geometry is Desarguesian of dimension at least 2 is \(F/k^\times\) for a unique pair of fields \(k\subseteq F\) (Theorem 4.7). The proof there uses Karzel's classification of commutative incidence groups.
2. [Connes–Consani 2011c, Theorem 3.11 and Remark 3.12]: the three kinds of finite hyperfield extensions of \(\mathbf{K}\), and the absence of known examples of the third kind.
3. [Connes–Consani 2011c, Example 4.7], with a theorem of Hall: hyperfield extensions of \(\mathbf{K}\) with group of units \(\mathbb{Z}\) and a non-Desarguesian plane as geometry.
4. [Connes–Consani 2011c, Theorem 3.13 and Remark 3.16]: a morphism \(A_1/k_1^\times\to A_2/k_2^\times\) whose image contains three points not on one line comes from a unique ring homomorphism. The proof there uses a theorem of Faure and Frölicher.
5. [Connes–Consani 2011c, Theorem 7.5]: the morphisms \(\mathbb{Z}[T]\to\mathbb{H}_\mathbb{Q}\).
6. [Connes–Consani 2011c, Theorem 7.12]: for a function field, the groupoid of prime elements of \(\mathbb{H}_k\) is the loop groupoid of the maximal abelian cover of the curve.
7. The facts on adèles recalled at the beginning of Section 5; see [Milne CFT, Chapter V, Section 4].
8. [Connes 2011, Theorem 3.4]: the formula for the sum of two Teichmüller representatives.
9. [Lescot 2013, Example 6.2]: a semiring of characteristic one with six elements in which \(\{0\}\) is not an intersection of saturated primary ideals. (An ideal \(Q\neq R\) is primary if \(xy\in Q\) implies \(x\in Q\) or \(y^n\in Q\) for some \(n\ge 1\).) So Theorem 2.10 does not extend to a primary decomposition of all saturated ideals.
10. [Lorscheid 2022, Proposition 4.3]: in the language of ordered blueprints, imposing \(1+1=1\) on the ordered blueprint of \(\mathbf{T}\) gives the tropical semifield with its order.

## References

Results of the first six works are numbered as in the arXiv versions.

- [Connes–Consani 2011b] A. Connes, C. Consani, *Characteristic one, entropy and the absolute point*, arXiv:0911.3537. Free at https://alainconnes.org/wp-content/uploads/char1absolutepoint.pdf
- [Connes 2011] A. Connes, *The Witt construction in characteristic one and quantization*, arXiv:1009.1769. Free at https://alainconnes.org/wp-content/uploads/Wittcar1.pdf
- [Connes–Consani 2011c] A. Connes, C. Consani, *The hyperring of adèle classes*, arXiv:1001.4260. Free at https://alainconnes.org/wp-content/uploads/The-hyperring-of-adeles-classes-2011.pdf
- [Connes–Consani 2010b] A. Connes, C. Consani, *From monoids to hyperstructures: in search of an absolute arithmetic*, arXiv:1006.4810. Free at https://alainconnes.org/wp-content/uploads/From-monoids-to-hyperstructures-2010.pdf
- [Lescot 2013] P. Lescot, *Prime and primary ideals in characteristic one*, [arXiv:1310.8400](https://arxiv.org/pdf/1310.8400).
- [Lorscheid 2022] O. Lorscheid, *Tropical geometry over the tropical hyperfield*, [arXiv:1907.01037](https://arxiv.org/pdf/1907.01037).
- [Lebl] J. Lebl, *Basic Analysis I* and *Basic Analysis II: Introduction to Real Analysis*, version 6.3 (15 May 2026), freely available at [www.jirka.org/ra](https://www.jirka.org/ra/). It is the text of the core courses *Real Analysis I* and *Real Analysis II*.

The following works are cited through [Connes–Consani 2011c] and [Lorscheid 2022], whose bibliographies give these details.

- [Krasner 1983] M. Krasner, *A class of hyperrings and hyperfields*, Internat. J. Math. Math. Sci. 6 (1983). Free at https://doi.org/10.1155/S0161171283000265
- [Lyndon 1961] R. C. Lyndon, *Relation algebras and projective geometries*, Michigan Math. J. 8 (1961). Free at https://doi.org/10.1307/mmj/1028998510
- [Milne CFT] J. S. Milne, *Class Field Theory*, course notes, version 4.03, 2020. Free at https://www.jmilne.org/math/CourseNotes/CFT.pdf
