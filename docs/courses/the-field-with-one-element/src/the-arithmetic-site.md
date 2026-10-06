# The arithmetic site

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions (AI Integrated Stacks Project citations; the general topos statements located in a later lesson) are self-checked by the writing AI. Public domain (CC0).*

The arithmetic site of Connes and Consani is a pair. The first member is a topos: the category of sets with an action of the monoid \(\mathbb N^\times\) of positive integers under multiplication. The second member is a structure sheaf: the semiring \(\mathbb Z_{\max}\) of tropical integers, on which a positive integer \(k\) acts by the Frobenius map \(n\mapsto kn\). This lesson defines the pair and proves its three main properties.

1. The points of the topos correspond to the non-zero subgroups of \(\mathbb Q\). Two subgroups give isomorphic points exactly when one is a positive rational multiple of the other (Theorem 2.2). In terms of finite adèles, the set of isomorphism classes of points is \(\mathbb Q_{>0}\backslash\mathbb A^f/\widehat{\mathbb Z}^\times\) (Proposition 2.4).
2. The points of the site with values in the tropical semifield \(\mathbb R_{\max}\) form the quotient \(\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\) of the adèle class space of \(\mathbb Q\). The Frobenius automorphisms of \(\mathbb R_{\max}\) act on these points as the scaling action of \(\mathbb R_+^\times\) (Theorem 4.6).
3. The square of the site carries a Frobenius correspondence \(\Psi(\lambda)\) for every real \(\lambda>0\). The composition law is \(\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')\), except when \(\lambda\) and \(\lambda'\) are irrational and \(\lambda\lambda'\) is rational. In that case the composite is a tangential deformation of \(\Psi(\lambda\lambda')\) (Theorem 6.8).

The reason for studying this pair is Weil's proof. The lesson *Weil's proof for curves and what is missing over the integers* lists what that proof uses for a curve \(C\) over a finite field \(\mathbb F_q\): the points of \(C\) over an algebraic closure, the Frobenius map acting on them, the surface \(C\times C\), and the Frobenius correspondences on that surface. The arithmetic site supplies an object of each kind for the integers.

- The field of constants \(\mathbb F_q\) becomes the Boolean semifield \(\mathbb B\), which is the semiring of global sections of the structure sheaf (Proposition 3.3).
- The algebraic closure \(\overline{\mathbb F}_q\) becomes \(\mathbb R_{\max}\), and the Frobenius \(x\mapsto x^q\) becomes the one-parameter group \(\operatorname{Fr}_\mu\), \(\mu\in\mathbb R_+^\times\).
- The set \(C(\overline{\mathbb F}_q)\) becomes \(\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\) (Theorem 4.6).
- The surface \(C\times C\) becomes the square of the site, and the graphs of the powers of the Frobenius become the correspondences \(\Psi(\lambda)\) (Sections 5 and 6).

The site proves nothing about the zeros of the zeta function. What it gives toward that goal, and what is missing, is the subject of *The scaling site*.

The lesson assumes categories, functors, limits and colimits, adjoint functors and presheaves. The facts about toposes that it needs are stated in Section 1 with references, and everything about points is proved there for the toposes that occur. From *Characteristic one and hyperrings* the lesson uses idempotent semirings and the semifields \(\mathbb B\), \(\mathbb Z_{\max}\) and \(\mathbb R_{\max}\); the definitions are repeated below. The \(p\)-adic numbers and the adèles of \(\mathbb Q\) are recalled in Sections 2 and 4.

Basic references are [Connes–Consani 2016b], which contains all the results on the arithmetic site that this lesson treats, and [Leinster 2010] for a short introduction to toposes. The arithmetic site was announced in [Connes–Consani 2014]. There the structure sheaf is the semiring \((\mathbb N\cup\{\infty\},\min,+)\) in place of \(\mathbb Z_{\max}\), and [Connes–Consani 2016b, Remark 3.4] relates the two versions.

### Conventions

- Semirings are commutative, with \(0\) and \(1\), and \(0\cdot a=0\). Morphisms of semirings preserve \(0\) and \(1\). A semiring is *idempotent* if \(1+1=1\); then \(a+a=a\) for all \(a\). In an abstract idempotent semiring the addition is written \(\oplus\). A semiring is *multiplicatively cancellative* if \(1\neq0\) and \(ab=ac\) with \(a\neq0\) implies \(b=c\). A *semifield* is a semiring with \(1\neq0\) in which every non-zero element is invertible.
- \(\mathbb B=\{0,1\}\) with \(1+1=1\) is the Boolean semifield.
- Let \(G\) be a totally ordered abelian group, written additively. Then \(G_{\max}=(G\cup\{-\infty\},\max,+)\) is the idempotent semifield in which the semiring addition is \(\max\), the semiring multiplication is \(+\), the zero is \(-\infty\) and the unit is \(0\in G\). Its \(k\)-th power map is \(x\mapsto kx\). In the same way \(G_{\min}=(G\cup\{\infty\},\min,+)\), and \(x\mapsto-x\) is an isomorphism \(G_{\max}\to G_{\min}\). We use this for \(G=\mathbb Z\), \(\mathbb Q\), \(\mathbb R\) and their subgroups. The sub-semiring \(\{-\infty,0\}\) of \(G_{\max}\) is a copy of \(\mathbb B\).
- In this lesson a *monoid* is a commutative monoid written multiplicatively, with unit \(1\). A zero element is not assumed. This differs from the other lessons of the course, because the monoid \(\mathbb N^\times=\{1,2,3,\dots\}\) under multiplication has no zero. Exercise 3 treats the monoid \(\mathbb N_0^\times=\mathbb N^\times\cup\{0\}\) obtained by adjoining one.
- \(\mathbb N=\{0,1,2,\dots\}\). \(\mathbb Q_{>0}\) is the group of positive rationals under multiplication, and \(\mathbb R_+^\times=(0,\infty)\) under multiplication. For a subgroup \(H\) of \(\mathbb Q\) or \(\mathbb R\), \(H_{>0}=\{h\in H:h>0\}\).

## 1. Sets with an action of a commutative monoid

For the general theory, for presheaves on any small category, see [Connes–Consani 2016b, Section 2.2] and [Connes–Consani 2017, Section 3.1]. We need only a category with one object, and we prove what we use.

### The topos of \(M\)-sets

Let \(M\) be a monoid. An *\(M\)-set* is a set \(A\) with a map \(M\times A\to A\), \((m,a)\mapsto ma\), such that \(1a=a\) and \((mn)a=m(na)\). A map \(f:A\to B\) of \(M\)-sets is *equivariant* if \(f(ma)=mf(a)\). The \(M\)-sets and the equivariant maps form a category \(M\text{-}\mathbf{Set}\).

Regard \(M\) as a category with one object, whose morphisms are the elements of \(M\). A functor from this category to sets is an \(M\)-set, and a natural transformation is an equivariant map. Since \(M\) is commutative, covariant and contravariant functors are the same. So \(M\text{-}\mathbf{Set}\) is the category of presheaves of sets on a small category. Such a category is a topos [Leinster 2010, Examples 1.6(iv)]. We write \(\widehat M\) for \(M\text{-}\mathbf{Set}\) regarded as a topos. In particular \(\widehat{\mathbb N^\times}\) is the topos of \(\mathbb N^\times\)-sets.

Limits and colimits in \(M\text{-}\mathbf{Set}\) are formed on the underlying sets.

- The terminal object \(1\) is a one-point set.
- The product \(A\times B\) is the product of sets with \(m(a,b)=(ma,mb)\).
- The equalizer of \(f,g:A\to B\) is the subset \(\{a:f(a)=g(a)\}\).
- Coproducts are disjoint unions.
- The coequalizer of \(f,g:A\to B\) is the quotient of \(B\) by the smallest equivalence relation that contains all pairs \((f(a),g(a))\). The set of these pairs is stable under \(M\), so the relation is stable under \(M\), and the quotient is an \(M\)-set.

**Example 1.1.** (a) \(M\) acts on itself by multiplication. For an \(M\)-set \(A\) and \(a\in A\) there is exactly one equivariant map \(e_a:M\to A\) with \(e_a(1)=a\), namely \(e_a(m)=ma\). For \(m\in M\) the multiplication \(\mu_m:M\to M\), \(\mu_m(n)=nm\), is equivariant, and \(e_a\circ\mu_m=e_{ma}\).

(b) By unique factorization, \(\mathbb N^\times\) is the free commutative monoid on the set of primes. So an \(\mathbb N^\times\)-set is a set with one self-map for each prime, such that these maps commute with each other. Examples are \(\mathbb Q_{>0}\) and the interval \((0,\infty)\subset\mathbb R\), with \(k\) acting by multiplication by \(k\).

(c) The *global sections* of an \(M\)-set \(A\) are the equivariant maps \(1\to A\). They correspond to the fixed points of \(A\): the elements \(a\) with \(ma=a\) for all \(m\in M\).

### Points and tensor products

A *geometric morphism* \(f:\mathcal E\to\mathcal F\) between toposes is a pair of functors \(f^{\ast}:\mathcal F\to\mathcal E\) and \(f_{\ast}:\mathcal E\to\mathcal F\) such that \(f^{\ast}\) is left adjoint to \(f_{\ast}\) and \(f^{\ast}\) preserves finite limits [Leinster 2010, Definition 3.3], [Stacks, Tag [00XA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-topos)]. A *point* of a topos \(\mathcal E\) is a geometric morphism \(p\) from the topos of sets to \(\mathcal E\) [Leinster 2010, Definition 3.5], [Stacks, Tag [00Y4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-point-topos)]. So a point has an inverse image functor \(p^{\ast}:\mathcal E\to\mathbf{Set}\). The set \(p^{\ast}(A)\) is the *stalk* of \(A\) at \(p\). A morphism of points \(p\to q\) is a natural transformation \(p^{\ast}\to q^{\ast}\).

For \(\mathcal E=\widehat M\) the functors \(p^{\ast}\) can be described completely.

**Definition 1.2.** Let \(X\) and \(A\) be \(M\)-sets. The *tensor product* \(X\otimes_MA\) is the quotient of the set \(X\times A\) by the smallest equivalence relation \(\sim\) such that \((mx,a)\sim(x,ma)\) for all \(m\in M\), \(x\in X\), \(a\in A\). We write \([x,a]\) for the class of \((x,a)\). An equivariant map \(f:A\to B\) induces the map \([x,a]\mapsto[x,f(a)]\) from \(X\otimes_MA\) to \(X\otimes_MB\). An equivariant map \(g:X\to X'\) induces the map \([x,a]\mapsto[g(x),a]\).

For example, \(X\otimes_MM\cong X\) by \([x,m]\mapsto mx\), with inverse \(x\mapsto[x,1]\).

**Lemma 1.3.** For every \(M\)-set \(X\), the functor \(X\otimes_M-\) from \(M\)-sets to sets is left adjoint to the functor \(S\mapsto\operatorname{Map}(X,S)\). Here \(\operatorname{Map}(X,S)\) is the set of all maps \(X\to S\), with the action \((m\cdot g)(x)=g(mx)\). In particular \(X\otimes_M-\) preserves all colimits.

**Proof.** A map \(X\otimes_MA\to S\) is the same as a map \(\varphi:X\times A\to S\) with \(\varphi(mx,a)=\varphi(x,ma)\). Such a \(\varphi\) is the same as a map \(A\to\operatorname{Map}(X,S)\), \(a\mapsto\varphi(-,a)\), and the condition on \(\varphi\) says exactly that this map is equivariant. The bijection is natural in \(A\) and \(S\). A left adjoint preserves colimits [Stacks, Tag [0038](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-adjoint-exact)]. \(\square\)

**Lemma 1.4.** Let \(F:M\text{-}\mathbf{Set}\to\mathbf{Set}\) be a functor that preserves colimits. Let \(X=F(M)\), with \(m\in M\) acting by \(F(\mu_m)\). Then \(X\) is an \(M\)-set, and there is an isomorphism \(X\otimes_MA\cong F(A)\), natural in \(A\). Moreover, for \(M\)-sets \(X\) and \(X'\), every natural transformation \(X\otimes_M-\to X'\otimes_M-\) is induced by exactly one equivariant map \(X\to X'\).

**Proof.** \(X\) is an \(M\)-set because \(\mu_m\circ\mu_n=\mu_{mn}\). Define \(\tau_A:X\otimes_MA\to F(A)\) by \(\tau_A[x,a]=F(e_a)(x)\). This is well defined, since \(F(e_a)(mx)=F(e_a\circ\mu_m)(x)=F(e_{ma})(x)\). It is natural in \(A\), since \(f\circ e_a=e_{f(a)}\) for an equivariant map \(f\). For \(A=M\) it is the bijection \([x,m]\mapsto mx\).

Every \(M\)-set \(A\) is a colimit of copies of \(M\). Let \(P_0=\coprod_{a\in A}M\) and \(P_1=\coprod_{(m,a)\in M\times A}M\). Let \(d:P_1\to P_0\) send the copy with index \((m,a)\) to the copy with index \(a\) by \(\mu_m\), and let \(d':P_1\to P_0\) send it to the copy with index \(ma\) by the identity. Let \(e:P_0\to A\) be \(e_a\) on the copy with index \(a\). Then \(e\) is a coequalizer of \(d\) and \(d'\). Indeed, as a set \(P_0\) is \(M\times A\), the relation generated by \(d\) and \(d'\) is \((nm,a)\sim(n,ma)\), and the quotient is \(M\otimes_MA\cong A\).

Both \(F\) and \(X\otimes_M-\) preserve coproducts and coequalizers, and \(\tau\) is natural. Since \(\tau_M\) is bijective, so are \(\tau_{P_0}\) and \(\tau_{P_1}\), and hence so is \(\tau_A\).

For the last statement, let \(\theta\) be a natural transformation \(X\otimes_M-\to X'\otimes_M-\). Identify \(X\otimes_MM\) with \(X\). Then \(\theta_M\) is a map \(X\to X'\), and it is equivariant by naturality with respect to the maps \(\mu_m\). Naturality with respect to \(e_a\) gives \(\theta_A[x,a]=[\theta_M(x),a]\). So \(\theta\) is induced by \(\theta_M\). Conversely, an equivariant map \(g\) induces a natural transformation \(\theta\) with \(\theta_M=g\). \(\square\)

**Definition 1.5.** An \(M\)-set \(X\) is *flat* if the functor \(X\otimes_M-\) preserves finite limits.

**Proposition 1.6.** Let \(X\) be a flat \(M\)-set. Then \(p_X^{\ast}=X\otimes_M-\) and \(p_{X\ast}=\operatorname{Map}(X,-)\) form a point \(p_X\) of \(\widehat M\). Every point \(p\) of \(\widehat M\) is isomorphic to \(p_X\) for a flat \(M\)-set \(X\), namely \(X=p^{\ast}(M)\). The morphisms of points \(p_X\to p_{X'}\) correspond bijectively to the equivariant maps \(X\to X'\). So \(X\mapsto p_X\) is an equivalence from the category of flat \(M\)-sets to the category of points of \(\widehat M\).

**Proof.** The first statement is Lemma 1.3 and the definition of flatness. Let \(p\) be a point. Then \(p^{\ast}\) preserves colimits, because it is a left adjoint. By Lemma 1.4, \(p^{\ast}\cong X\otimes_M-\) with \(X=p^{\ast}(M)\), and \(X\) is flat because \(p^{\ast}\) preserves finite limits. A right adjoint is determined by its left adjoint up to a unique isomorphism, so \(p\cong p_X\). The statement on morphisms is the last part of Lemma 1.4. \(\square\)

### The three conditions

Flatness can be tested on \(X\) itself. Consider the following conditions on an \(M\)-set \(X\).

- **(F1)** \(X\) is not empty.
- **(F2)** For all \(x,x'\in X\) there are \(z\in X\) and \(k,k'\in M\) with \(kz=x\) and \(k'z=x'\).
- **(F3)** For all \(x\in X\) and \(k,k'\in M\) with \(kx=k'x\) there are \(z\in X\) and \(w\in M\) with \(wz=x\) and \(kw=k'w\).

**Lemma 1.7.** Let \(X\) be an \(M\)-set that satisfies (F2) and (F3), and let \(A\) be any \(M\)-set. Two pairs \((x,a)\) and \((x',a')\) in \(X\times A\) have the same class in \(X\otimes_MA\) if and only if there are \(z\in X\) and \(k,k'\in M\) with
\[
kz=x,\qquad k'z=x',\qquad ka=k'a'.
\]

**Proof.** Write \((x,a)\,\mathrm R\,(x',a')\) if such \(z,k,k'\) exist. If they exist, then \((x,a)=(kz,a)\sim(z,ka)=(z,k'a')\sim(k'z,a')=(x',a')\). So \(\mathrm R\) implies \(\sim\). The relation \(\mathrm R\) is reflexive (take \(z=x\), \(k=k'=1\)) and symmetric. It contains the generating pairs of \(\sim\): for \((mx,a)\) and \((x,ma)\) take \(z=x\), \(k=m\), \(k'=1\). So it remains to show that \(\mathrm R\) is transitive.

Let \((x,a)\,\mathrm R\,(x',a')\) through \(z,k,k'\), and let \((x',a')\,\mathrm R\,(x'',a'')\) through \(y,l,l'\). So \(ly=x'\), \(l'y=x''\) and \(la'=l'a''\). By (F2) there are \(u\in X\) and \(s,t\in M\) with \(su=z\) and \(tu=y\). Then \((k's)u=x'=(lt)u\). By (F3) there are \(v\in X\) and \(w\in M\) with \(wv=u\) and \(k'sw=ltw\). Now
\[
(ksw)v=ksu=kz=x,\qquad(l'tw)v=l'tu=l'y=x'',
\]
and
\[
(ksw)a=sw(ka)=sw(k'a')=(k'sw)a'=(ltw)a'=tw(la')=tw(l'a'')=(l'tw)a''.
\]
So \((x,a)\,\mathrm R\,(x'',a'')\) through \(v\), \(ksw\), \(l'tw\). \(\square\)

**Theorem 1.8.** An \(M\)-set \(X\) is flat if and only if it satisfies (F1), (F2) and (F3).

*Remark.* The corresponding statement holds for functors on an arbitrary small category; see [Connes–Consani 2017, Section 3.1], which also describes the points of a presheaf topos by flat functors (Proposition 1.6 is the case of one object). The lesson does not use these results: it proves the case of a commutative monoid.

**Proof.** A functor defined on a category with finite limits preserves finite limits if and only if it preserves the terminal object, binary products and equalizers [Stacks, Tag [0035](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-left-exact)].

Let \(X\) be flat. The set \(X\otimes_M1\) is a quotient of \(X\), and it is a one-point set because \(X\otimes_M-\) preserves the terminal object. So \(X\neq\emptyset\), which is (F1). The functor preserves the product \(M\times M\), so the map \(X\otimes_M(M\times M)\to(X\otimes_MM)\times(X\otimes_MM)=X\times X\), \([z,(k,k')]\mapsto(kz,k'z)\), is bijective. Its surjectivity is (F2). Let \(k,k'\in M\). The equalizer of \(\mu_k,\mu_{k'}:M\to M\) is \(E=\{w\in M:kw=k'w\}\). Under \(X\otimes_MM=X\) the maps \(X\otimes\mu_k\) and \(X\otimes\mu_{k'}\) are \(x\mapsto kx\) and \(x\mapsto k'x\). Since the functor preserves equalizers, the image of \(X\otimes_ME\to X\), \([z,w]\mapsto wz\), is \(\{x:kx=k'x\}\). This is (F3).

Conversely, let \(X\) satisfy (F1), (F2) and (F3). We use Lemma 1.7 throughout.

*Terminal object.* Two elements \([x,\ast]\) and \([x',\ast]\) of \(X\otimes_M1\) are equal if and only if there are \(z,k,k'\) with \(kz=x\) and \(k'z=x'\). By (F2) this always holds. By (F1) the set \(X\otimes_M1\) is not empty. So it is a one-point set.

*Products.* Let \(A\) and \(B\) be \(M\)-sets, and let \(c:X\otimes_M(A\times B)\to(X\otimes_MA)\times(X\otimes_MB)\) be the map \([x,(a,b)]\mapsto([x,a],[x,b])\). It is surjective: given \([x,a]\) and \([x',b]\), choose \(z,k,k'\) with \(kz=x\) and \(k'z=x'\); then \([x,a]=[z,ka]\) and \([x',b]=[z,k'b]\), so the pair is \(c[z,(ka,k'b)]\). It is injective: suppose \([x,a]=[x',a']\) and \([x,b]=[x',b']\). By Lemma 1.7 there are \(z,k,k'\) with \(kz=x\), \(k'z=x'\), \(ka=k'a'\), and there are \(y,l,l'\) with \(ly=x\), \(l'y=x'\), \(lb=l'b'\). By (F2) there are \(u,s,t\) with \(su=z\) and \(tu=y\). Then \((ks)u=x=(lt)u\), so by (F3) there are \(v,w\) with \(wv=u\) and \(ksw=ltw\). Then \((k'sw)v=x'=(l'tw)v\), so by (F3) there are \(v',w'\) with \(w'v'=v\) and \(k'sww'=l'tww'\). Put \(K=ksww'=ltww'\) and \(K'=k'sww'=l'tww'\). Then
\[
Kv'=x,\qquad K'v'=x',\qquad Ka=sww'(ka)=sww'(k'a')=K'a',\qquad Kb=tww'(lb)=tww'(l'b')=K'b'.
\]
So \([x,(a,b)]=[x',(a',b')]\) by Lemma 1.7.

*Equalizers.* Let \(f,g:A\to B\) be equivariant and \(E=\{a:f(a)=g(a)\}\). The map \(X\otimes_ME\to X\otimes_MA\) is injective: if \((x,a)\) and \((x',a')\) with \(a,a'\in E\) are equivalent in \(X\times A\), the elements \(z,k,k'\) of Lemma 1.7 show that they are equivalent in \(X\times E\). Its image is contained in the equalizer of \(X\otimes f\) and \(X\otimes g\). Let \([x,a]\) be in that equalizer, so \([x,f(a)]=[x,g(a)]\). By Lemma 1.7 there are \(z,k,k'\) with \(kz=x=k'z\) and \(kf(a)=k'g(a)\). By (F3) there are \(v,w\) with \(wv=z\) and \(kw=k'w\). Then \([x,a]=[kwv,a]=[v,kwa]\), and
\[
f(kwa)=w\,kf(a)=w\,k'g(a)=k'w\,g(a)=kw\,g(a)=g(kwa).
\]
So \(kwa\in E\), and \([x,a]\) is in the image. \(\square\)

If \(M\) is cancellative, that is, if \(ab=ac\) implies \(b=c\), then (F3) is equivalent to the simpler condition

- **(F3')** if \(kx=k'x\) for some \(x\in X\), then \(k=k'\).

Indeed (F3) gives \(kw=k'w\), hence \(k=k'\); and (F3') gives (F3) with \(z=x\) and \(w=1\).

**Example 1.9.** (a) \(M\) itself is flat. (F1) is clear. For (F2) take \(z=1\), \(k=x\), \(k'=x'\). For (F3) take \(z=1\) and \(w=x\). The point \(p_M\) has \(p_M^{\ast}(A)=M\otimes_MA=A\): its inverse image is the forgetful functor, and the stalk of \(A\) is the underlying set of \(A\).

(b) Let \(M=\mathbb N^\times\). The terminal object \(1\) is not flat, since \(2\cdot\ast=3\cdot\ast\) contradicts (F3'). The disjoint union of two copies of \(\mathbb N^\times\) is not flat, since (F2) fails for two elements of different copies. The sub-\(\mathbb N^\times\)-set \(\mathbb N^\times\setminus\{1\}\) of \(\mathbb N^\times\) is not flat: for \(x=2\) and \(x'=3\), an element \(z\) as in (F2) would divide \(2\) and \(3\), so \(z=1\).

## 2. The points of the topos of \(\mathbb N^\times\)-sets

### Flat sets over a cancellative monoid

Let \(M\) be a cancellative monoid. It embeds in its group of fractions \(\Gamma\), the abelian group of quotients \(ab^{-1}\) with \(a,b\in M\). For \(M=\mathbb N^\times\) the group \(\Gamma\) is \(\mathbb Q_{>0}\).

A *directed \(M\)-subset* of \(\Gamma\) is a subset \(P\subseteq\Gamma\) such that \(P\neq\emptyset\), \(MP\subseteq P\), and for all \(p,p'\in P\) there is \(c\in P\) with \(p\in Mc\) and \(p'\in Mc\). Such a \(P\) is an \(M\)-set under multiplication.

**Proposition 2.1.** Let \(M\) be a cancellative monoid with group of fractions \(\Gamma\).

1. Every directed \(M\)-subset of \(\Gamma\) is a flat \(M\)-set.
2. Every flat \(M\)-set is isomorphic to a directed \(M\)-subset of \(\Gamma\) that contains \(1\).
3. Let \(P\) and \(P'\) be directed \(M\)-subsets of \(\Gamma\). The equivariant maps \(P\to P'\) are exactly the maps \(p\mapsto\gamma p\) with \(\gamma\in\Gamma\) and \(\gamma P\subseteq P'\).

**Proof.** (1) (F1) and (F2) are part of the definition. (F3') holds because \(kx=k'x\) in the group \(\Gamma\) gives \(k=k'\).

(2) Let \(X\) be flat, and fix \(x_0\in X\). For \(x\in X\) choose, by (F2), \(z\in X\) and \(k,k'\in M\) with \(kz=x_0\) and \(k'z=x\), and put \(\rho(x)=k'k^{-1}\in\Gamma\). This does not depend on the choice. Let \(y,l,l'\) be another choice, so \(ly=x_0\) and \(l'y=x\). By (F2) there are \(u,s,t\) with \(su=z\) and \(tu=y\). Then \(ksu=x_0=ltu\) and \(k'su=x=l'tu\), so \(ks=lt\) and \(k's=l't\) by (F3'). Hence \(k'k^{-1}=(k's)(ks)^{-1}=(l't)(lt)^{-1}=l'l^{-1}\).

The map \(\rho:X\to\Gamma\) is equivariant: for \(m\in M\) the same \(z\) and \(k\) serve for \(mx\), with \(mk'\) in place of \(k'\). It is injective. Let \(x,x'\in X\). Choose \(y,a,a'\) with \(ay=x\), \(a'y=x'\), and then \(z,k,b\) with \(kz=x_0\), \(bz=y\). Then \(x=abz\) and \(x'=a'bz\), so \(\rho(x)=abk^{-1}\) and \(\rho(x')=a'bk^{-1}\). If these are equal, then \(a=a'\) and \(x=x'\). So \(X\) is isomorphic to \(P=\rho(X)\). This set contains \(\rho(x_0)=1\), it is stable under \(M\), and it is directed, because \(\rho(x)\) and \(\rho(x')\) lie in \(M\rho(y)\) for \(y\) as above.

(3) A map \(p\mapsto\gamma p\) with \(\gamma P\subseteq P'\) is equivariant. Let \(f:P\to P'\) be equivariant. Fix \(p_0\in P\) and put \(\gamma=f(p_0)p_0^{-1}\). For \(p\in P\) choose \(c\in P\) and \(k,k'\in M\) with \(p_0=kc\) and \(p=k'c\). Then \(f(p_0)=kf(c)\) and \(f(p)=k'f(c)=k'k^{-1}f(p_0)=pp_0^{-1}f(p_0)=\gamma p\). \(\square\)

By Proposition 1.6, the category of points of \(\widehat M\) is therefore equivalent to the category whose objects are the directed \(M\)-subsets \(P\) of \(\Gamma\), and whose morphisms \(P\to P'\) are the elements \(\gamma\in\Gamma\) with \(\gamma P\subseteq P'\).

### The case of \(\mathbb N^\times\)

**Theorem 2.2.**

1. For every non-zero subgroup \(H\subseteq\mathbb Q\), the set \(H_{>0}\), with \(k\in\mathbb N^\times\) acting by multiplication, is a flat \(\mathbb N^\times\)-set.
2. Every flat \(\mathbb N^\times\)-set is isomorphic to \(H_{>0}\) for a non-zero subgroup \(H\subseteq\mathbb Q\).
3. For non-zero subgroups \(H\) and \(H'\), the equivariant maps \(H_{>0}\to H'_{>0}\) are exactly the maps \(x\mapsto rx\) with \(r\in\mathbb Q_{>0}\) and \(rH\subseteq H'\).

Consequently, the category of points of \(\widehat{\mathbb N^\times}\) is equivalent to the category whose objects are the non-zero subgroups of \(\mathbb Q\) and whose morphisms \(H\to H'\) are the numbers \(r\in\mathbb Q_{>0}\) with \(rH\subseteq H'\), composed by multiplication. We write \(p_H\) for the point with \(p_H^{\ast}=H_{>0}\otimes_{\mathbb N^\times}-\). Two points \(p_H\) and \(p_{H'}\) are isomorphic if and only if \(H'=rH\) for some \(r\in\mathbb Q_{>0}\).

*Reference:* [Connes–Consani 2016b, Theorem 2.1] states the result as an equivalence with the category of totally ordered groups that are isomorphic to non-zero subgroups of \(\mathbb Q\), with the injective morphisms of ordered groups. The two statements agree: an order-preserving homomorphism between subgroups of \(\mathbb Q\) is multiplication by some \(r\geq0\) (Lemma 4.2), and it is injective exactly when \(r>0\).

**Proof.** We apply Proposition 2.1 to \(M=\mathbb N^\times\) and \(\Gamma=\mathbb Q_{>0}\). It is enough to show that the directed \(\mathbb N^\times\)-subsets of \(\mathbb Q_{>0}\) are exactly the sets \(H_{>0}\).

Let \(H\) be a non-zero subgroup of \(\mathbb Q\). Then \(H_{>0}\) is not empty and is stable under \(\mathbb N^\times\). Let \(a,b\in H_{>0}\). Both are integer multiples of \(1/n\) for a common denominator \(n\), and every subgroup of the infinite cyclic group \(\frac1n\mathbb Z\) is cyclic. So \(\mathbb Za+\mathbb Zb=\mathbb Zc\) with \(c>0\). Then \(c\in H_{>0}\), and \(a=kc\), \(b=k'c\) with positive integers \(k,k'\). So \(H_{>0}\) is directed.

Let \(P\subseteq\mathbb Q_{>0}\) be a directed \(\mathbb N^\times\)-subset, and put \(H=P\cup\{0\}\cup(-P)\). For \(p,p'\in P\) choose \(c\in P\) with \(p=kc\) and \(p'=k'c\). Then \(p+p'=(k+k')c\in P\), and \(p-p'=(k-k')c\) lies in \(P\), in \(\{0\}\) or in \(-P\), according to the sign of \(k-k'\). Hence \(H\) is closed under addition and under negation. It is a non-zero subgroup of \(\mathbb Q\) with \(H_{>0}=P\).

Statement 3 is Proposition 2.1(3). If \(r\) is an isomorphism, its inverse is \(r^{-1}\) with \(r^{-1}H'\subseteq H\), so \(rH=H'\). \(\square\)

In particular every morphism between points of \(\widehat{\mathbb N^\times}\) is given by an injective map of flat sets.

### Subgroups of \(\mathbb Q\) and finite adèles

For a prime \(p\) let \(v_p\) be the \(p\)-adic valuation on \(\mathbb Q\), with \(v_p(0)=+\infty\). For a non-zero subgroup \(H\subseteq\mathbb Q\) put
\[
h_p(H)=\sup\{-v_p(x):x\in H,\ x\neq0\}\in\mathbb Z\cup\{+\infty\}.
\]
If \(H\) contains \(\mathbb Z\), this is the largest exponent with which \(p\) occurs in the denominator of an element of \(H\), or \(+\infty\) if these exponents are not bounded.

**Lemma 2.3.**

1. Let \(H\) be a non-zero subgroup of \(\mathbb Q\). Then \(h_p(H)\geq0\) for all but finitely many \(p\), and
\[
H=\{x\in\mathbb Q:v_p(x)\geq-h_p(H)\text{ for all primes }p\}.
\]
2. Let \(h=(h_p)_p\) be a family with \(h_p\in\mathbb Z\cup\{+\infty\}\) and \(h_p\geq0\) for all but finitely many \(p\). Then \(H(h)=\{x\in\mathbb Q:v_p(x)\geq-h_p\text{ for all }p\}\) is a non-zero subgroup of \(\mathbb Q\), and \(h_p(H(h))=h_p\) for all \(p\).
3. For \(r\in\mathbb Q_{>0}\) one has \(h_p(rH)=h_p(H)-v_p(r)\).

So \(H\mapsto(h_p(H))_p\) is a bijection from the set of non-zero subgroups of \(\mathbb Q\) to the set of families as in (2).

**Proof.** (1) Pick \(y\neq0\) in \(H\). Then \(v_p(y)=0\) for all but finitely many \(p\), and \(h_p(H)\geq-v_p(y)\). The inclusion \(\subseteq\) holds by the definition of \(h_p\). For the other inclusion let \(x\neq0\) with \(v_p(x)\geq-h_p(H)\) for all \(p\). Let \(S\) be the finite set of primes with \(v_p(x)< v_p(y)\). For \(p\in S\) there is \(y_p\in H\), \(y_p\neq0\), with \(-v_p(y_p)\geq-v_p(x)\), by the definition of the supremum. The subgroup generated by \(y\) and the \(y_p\) is cyclic; let \(z\) be a generator. Then \(z\in H\). Since \(y\) and the \(y_p\) are integer multiples of \(z\), we get \(v_p(z)\leq v_p(y)\) for all \(p\) and \(v_p(z)\leq v_p(y_p)\) for \(p\in S\). Hence \(v_p(z)\leq v_p(x)\) for every prime \(p\). So \(x/z\) is an integer, and \(x\in\mathbb Zz\subseteq H\).

(2) \(H(h)\) is a subgroup because \(v_p(x+y)\geq\min(v_p(x),v_p(y))\) and \(v_p(-x)=v_p(x)\). Let \(x_0=\prod_{h_l<0}l^{-h_l}\), a finite product. Then \(v_p(x_0)\geq-h_p\) for all \(p\), so \(x_0\in H(h)\) and \(H(h)\neq0\). By definition \(h_p(H(h))\leq h_p\). Fix \(p\). If \(h_p\) is finite, the element \(p^{-h_p}\prod_{l\neq p,\,h_l<0}l^{-h_l}\) lies in \(H(h)\) and has \(-v_p\) equal to \(h_p\). If \(h_p=+\infty\), the elements \(p^{-n}\prod_{l\neq p,\,h_l<0}l^{-h_l}\) lie in \(H(h)\) for all \(n\). So \(h_p(H(h))=h_p\).

(3) \(-v_p(rx)=-v_p(r)-v_p(x)\). \(\square\)

Let \(\mathbb Q_p\) be the field of \(p\)-adic numbers, with valuation \(v_p:\mathbb Q_p\to\mathbb Z\cup\{+\infty\}\), ring of integers \(\mathbb Z_p=\{v_p\geq0\}\) and group of units \(\mathbb Z_p^\times=\{v_p=0\}\). Two elements of \(\mathbb Q_p\) have the same valuation if and only if they differ by a factor in \(\mathbb Z_p^\times\). The ring of *finite adèles* is
\[
\mathbb A^f=\Big\{(a_p)_p\in\prod_p\mathbb Q_p:\ a_p\in\mathbb Z_p\text{ for all but finitely many }p\Big\}.
\]
It contains the subring \(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\), and it contains \(\mathbb Q\), embedded diagonally. The group \(\widehat{\mathbb Z}^\times=\prod_p\mathbb Z_p^\times\) acts on \(\mathbb A^f\) by multiplication.

**Proposition 2.4.** For \(a\in\mathbb A^f\) put \(H_a=\{x\in\mathbb Q:xa\in\widehat{\mathbb Z}\}\).

1. The map \(a\mapsto H_a\) induces a bijection from \(\mathbb A^f/\widehat{\mathbb Z}^\times\) to the set of non-zero subgroups of \(\mathbb Q\), and \(h_p(H_a)=v_p(a_p)\).
2. For \(r\in\mathbb Q_{>0}\) one has \(H_{ra}=r^{-1}H_a\). Hence \(a\mapsto p_{H_a}\) induces a bijection from \(\mathbb Q_{>0}\backslash\mathbb A^f/\widehat{\mathbb Z}^\times\) to the set of isomorphism classes of points of \(\widehat{\mathbb N^\times}\).

*Reference:* [Connes–Consani 2016b, Proposition 2.5].

**Proof.** (1) \(xa\in\widehat{\mathbb Z}\) means \(v_p(x)+v_p(a_p)\geq0\) for all \(p\). So \(H_a=H(h)\) with \(h_p=v_p(a_p)\), and \(h_p\geq0\) for all but finitely many \(p\) because \(a\in\mathbb A^f\). By Lemma 2.3(2), \(H_a\) is a non-zero subgroup with \(h_p(H_a)=v_p(a_p)\). Two finite adèles have the same valuation at every prime if and only if they differ by a factor in \(\widehat{\mathbb Z}^\times\). Every family \(h\) as in Lemma 2.3(2) occurs: take \(a_p=p^{h_p}\), and \(a_p=0\) if \(h_p=+\infty\). So the claim follows from the bijection of Lemma 2.3.

(2) \(x\in H_{ra}\) means \(xra\in\widehat{\mathbb Z}\), that is, \(xr\in H_a\). The rest follows from (1) and Theorem 2.2. \(\square\)

**Example 2.5.** (a) \(a=1\) gives \(H=\mathbb Z\). The flat set is \(\mathbb Z_{>0}=\mathbb N^\times\), and \(p_{\mathbb Z}\) is the point of Example 1.9(a).

(b) \(a=0\) gives \(H=\mathbb Q\). On the flat set \(\mathbb Q_{>0}\) every \(k\in\mathbb N^\times\) acts bijectively.

(c) Let \(S\) be a set of primes, and let \(a_p=0\) for \(p\in S\) and \(a_p=1\) otherwise. Then \(H_a=\mathbb Z[S^{-1}]\), the ring of rationals whose denominator is a product of primes in \(S\). By Lemma 2.3(3), the set of primes with \(h_p=+\infty\) does not change when \(H\) is replaced by \(rH\). So different sets \(S\) give non-isomorphic points, and the set of isomorphism classes of points is uncountable.

(d) Let \(a_p=p\) for all \(p\). Then \(H_a\) is the group of rationals with square-free denominator, and all its heights \(h_p\) are \(1\). This point is not isomorphic to any point in (a), (b) or (c): by Lemma 2.3(3), replacing \(H\) by \(rH\) changes only finitely many of the \(h_p\).

(e) The \(\mathbb N^\times\)-set \((0,\infty)\subset\mathbb R\) is not flat. For \(x=1\) and \(x'=\sqrt2\), condition (F2) would give \(\sqrt2=k'/k\). It is the disjoint union of the flat sets \(\lambda\,\mathbb Q_{>0}\), one for each class \(\lambda\) in \(\mathbb R_+^\times/\mathbb Q_{>0}\).

## 3. The structure sheaf

### Semirings in the topos

A *semiring in \(\widehat M\)* is an \(M\)-set \(\mathcal O\) with a semiring structure such that every \(m\in M\) acts by a semiring endomorphism. Equivalently, the addition and the multiplication \(\mathcal O\times\mathcal O\to\mathcal O\) are equivariant, and \(0\) and \(1\) are fixed points.

Let \(p\) be a point of \(\widehat M\). The functor \(p^{\ast}\) preserves finite products, so \(p^{\ast}(\mathcal O\times\mathcal O)=p^{\ast}\mathcal O\times p^{\ast}\mathcal O\), and \(p^{\ast}\) turns the addition and the multiplication of \(\mathcal O\) into two operations on the stalk \(p^{\ast}\mathcal O\). The semiring axioms are equalities between maps that are built from these operations and from finite products. So they hold in the stalk: *the stalk of a semiring is a semiring*. A morphism of points \(\varphi:p\to q\) gives a morphism of semirings \(\varphi_{\mathcal O}:p^{\ast}\mathcal O\to q^{\ast}\mathcal O\), by naturality.

For \(p=p_X\) the operations are computed as follows. Given two elements of \(X\otimes_M\mathcal O\), use (F2) to write them as \([z,a]\) and \([z,b]\) with the same \(z\). Then
\[
[z,a]+[z,b]=[z,a+b],\qquad[z,a]\cdot[z,b]=[z,ab].
\]
Indeed, the bijection \(X\otimes_M(\mathcal O\times\mathcal O)\to(X\otimes_M\mathcal O)\times(X\otimes_M\mathcal O)\) sends \([z,(a,b)]\) to \(([z,a],[z,b])\), and the functor sends the addition to \([z,(a,b)]\mapsto[z,a+b]\).

### The arithmetic site

Recall that \(\mathbb Z_{\max}=(\mathbb Z\cup\{-\infty\},\max,+)\). For \(k\in\mathbb N^\times\) let
\[
\operatorname{Fr}_k:\mathbb Z_{\max}\to\mathbb Z_{\max},\qquad\operatorname{Fr}_k(n)=kn,\quad\operatorname{Fr}_k(-\infty)=-\infty.
\]
This is a semiring endomorphism: \(k\max(a,b)=\max(ka,kb)\) because \(k>0\), \(k(a+b)=ka+kb\), and \(k\cdot0=0\). Also \(\operatorname{Fr}_k\circ\operatorname{Fr}_l=\operatorname{Fr}_{kl}\). Since the semiring multiplication of \(\mathbb Z_{\max}\) is \(+\), the map \(\operatorname{Fr}_k\) is the \(k\)-th power map \(x\mapsto x^k\) of the semiring. It is the analogue of the Frobenius endomorphism \(x\mapsto x^p\) of a ring of characteristic \(p\).

**Definition 3.1.** The *arithmetic site* is the pair \((\widehat{\mathbb N^\times},\mathbb Z_{\max})\): the topos of \(\mathbb N^\times\)-sets, together with the semiring \(\mathbb Z_{\max}\) in it, on which \(k\in\mathbb N^\times\) acts by \(\operatorname{Fr}_k\). The semiring \(\mathbb Z_{\max}\) with this action is the *structure sheaf* of the site.

*Reference:* [Connes–Consani 2016b, Definition 3.1].

**Theorem 3.2.** Let \(H\subseteq\mathbb Q\) be a non-zero subgroup and \(H_{\max}=(H\cup\{-\infty\},\max,+)\). The map
\[
\beta:p_H^{\ast}(\mathbb Z_{\max})=H_{>0}\otimes_{\mathbb N^\times}\mathbb Z_{\max}\to H_{\max},\qquad\beta[y,n]=ny,\quad\beta[y,-\infty]=-\infty,
\]
is an isomorphism of semirings. If \(r\in\mathbb Q_{>0}\) and \(rH\subseteq H'\), the morphism of points \(p_H\to p_{H'}\) given by \(r\) induces on the stalks the map \(H_{\max}\to H'_{\max}\), \(h\mapsto rh\).

*Reference:* [Connes–Consani 2016b, Theorem 3.2].

**Proof.** The map is well defined, since \(\beta[ky,n]=nky=\beta[y,kn]\), and both sides are \(-\infty\) for \(n=-\infty\). It is surjective: \(h=\beta[h,1]\) for \(h>0\), \(h=\beta[-h,-1]\) for \(h<0\), \(0=\beta[y,0]\), and \(-\infty=\beta[y,-\infty]\).

It is injective. Let \(\beta[y,n]=\beta[y',n']\). By (F2) there are \(z\in H_{>0}\) and \(k,k'\) with \(kz=y\) and \(k'z=y'\). If \(n,n'\in\mathbb Z\), then \(nkz=n'k'z\), so \(kn=k'n'\), since \(z\neq0\). If one of \(n,n'\) is \(-\infty\), both are. In both cases \(\operatorname{Fr}_k(n)=\operatorname{Fr}_{k'}(n')\), so \([y,n]=[z,\operatorname{Fr}_k(n)]=[z,\operatorname{Fr}_{k'}(n')]=[y',n']\).

It is a morphism of semirings. Take two elements \([z,n]\) and \([z,n']\) with the same \(z\). Their sum in the stalk is \([z,\max(n,n')]\), and \(\beta\) sends it to \(\max(n,n')z=\max(nz,n'z)\), because \(z>0\). Their product is \([z,n+n']\), and \(\beta\) sends it to \(nz+n'z\). The zero \([z,-\infty]\) goes to \(-\infty\) and the unit \([z,0]\) goes to \(0\).

The morphism of points given by \(r\) sends \([y,n]\) to \([ry,n]\), and \(\beta[ry,n]=r\cdot ny\). \(\square\)

So the stalk at \(p_{\mathbb Z}\) is \(\mathbb Z_{\max}\) itself, the stalk at \(p_{\mathbb Q}\) is \(\mathbb Q_{\max}\), and every stalk is a semifield between the two, up to isomorphism.

**Proposition 3.3.** The global sections of the structure sheaf form the sub-semiring \(\{-\infty,0\}\) of \(\mathbb Z_{\max}\), which is isomorphic to \(\mathbb B\).

*Reference:* [Connes–Consani 2016b, Proposition 3.5].

**Proof.** By Example 1.1(c) the global sections are the elements fixed by all \(\operatorname{Fr}_k\). An integer \(n\) with \(kn=n\) for all \(k\) is \(0\), and \(-\infty\) is fixed. In \(\{-\infty,0\}\) the unit \(0\) satisfies \(\max(0,0)=0\), so this semiring is \(\mathbb B\). \(\square\)

**Remark 3.4 (what the structure sheaf adds).** The topos alone has many symmetries. Every permutation of the primes extends to an automorphism \(\sigma\) of the monoid \(\mathbb N^\times\), and twisting the action by \(\sigma\) is an automorphism of the category of \(\mathbb N^\times\)-sets. The structure sheaf is compatible with none of them except the identity. Suppose that \(\theta\) is a semiring automorphism of \(\mathbb Z_{\max}\) with \(\theta\circ\operatorname{Fr}_k=\operatorname{Fr}_{\sigma(k)}\circ\theta\) for all \(k\). On \(\mathbb Z\) the map \(\theta\) is an automorphism of the group \((\mathbb Z,+)\) that preserves the order, so \(\theta\) is the identity. Then \(\operatorname{Fr}_k=\operatorname{Fr}_{\sigma(k)}\), and evaluating at \(1\) gives \(k=\sigma(k)\). These symmetries of the topos are discussed in [Connes–Consani 2016b, Remark 2.8].

## 4. Points over \(\mathbb R_{\max}\) and the adèle class space

### Points with values in a semifield

Let \(G\) be a totally ordered abelian group. The main case is \(G=\mathbb R\). For \(\mu\in\mathbb R_+^\times\) the map
\[
\operatorname{Fr}_\mu:\mathbb R_{\max}\to\mathbb R_{\max},\qquad\operatorname{Fr}_\mu(x)=\mu x,\quad\operatorname{Fr}_\mu(-\infty)=-\infty,
\]
is an automorphism of the semifield \(\mathbb R_{\max}\), and \(\operatorname{Fr}_\mu\circ\operatorname{Fr}_{\mu'}=\operatorname{Fr}_{\mu\mu'}\). These are the *Frobenius automorphisms*. [Connes–Consani 2016b] uses the multiplicative form \(\mathbb R_+^{\max}=([0,\infty),\max,\times)\) of this semifield. The map \(x\mapsto e^x\), \(-\infty\mapsto0\), is an isomorphism from \(\mathbb R_{\max}\) to \(\mathbb R_+^{\max}\), and it turns \(\operatorname{Fr}_\mu\) into \(x\mapsto x^\mu\).

**Definition 4.1.** A *point of the arithmetic site over \(G_{\max}\)* is a pair \((p,f)\), where \(p\) is a point of \(\widehat{\mathbb N^\times}\) and \(f:p^{\ast}(\mathbb Z_{\max})\to G_{\max}\) is a morphism of semirings. Two such pairs \((p,f)\) and \((q,g)\) are *equivalent* if there is an isomorphism of points \(\varphi:p\to q\) with \(g\circ\varphi_{\mathcal O}=f\), where \(\varphi_{\mathcal O}\) is the induced isomorphism of the stalks of the structure sheaf. The point \((p,f)\) is *degenerate* if the image of \(f\) is \(\{-\infty,0\}\). We write \(\mathcal P(G)\) for the set of equivalence classes.

*Reference:* [Connes–Consani 2016b, Definition 3.6], for \(G=\mathbb R\).

An automorphism \(\theta\) of \(G_{\max}\) acts on \(\mathcal P(G)\) by \((p,f)\mapsto(p,\theta\circ f)\). This is compatible with the equivalence. In particular \(\mathbb R_+^\times\) acts on \(\mathcal P(\mathbb R)\) through the Frobenius automorphisms.

**Lemma 4.2.** Let \(H\) be a non-zero subgroup of \(\mathbb Q\) and \(G\) a totally ordered abelian group.

1. The morphisms of semirings \(f:H_{\max}\to G_{\max}\) are exactly the maps with \(f(-\infty)=-\infty\) whose restriction \(f_0\) to \(H\) is an order-preserving group homomorphism \(H\to G\).
2. Such an \(f_0\) is either zero or strictly increasing.
3. If \(G=\mathbb R\), then \(f_0(h)=\lambda h\) for a unique real number \(\lambda\geq0\).

**Proof.** (1) A morphism \(f\) satisfies \(f(-\infty)=-\infty\), \(f(0)=0\), \(f(h+h')=f(h)+f(h')\) and \(f(\max(h,h'))=\max(f(h),f(h'))\). For \(h\in H\) we get \(f(h)+f(-h)=0\), so \(f(h)\neq-\infty\). So \(f_0\) is a group homomorphism \(H\to G\), and the last identity says that it preserves the order. Conversely, an order-preserving homomorphism satisfies \(f_0(\max(h,h'))=\max(f_0(h),f_0(h'))\), because \(H\) is totally ordered. Extended by \(-\infty\mapsto-\infty\), it is a morphism of semirings.

(2) Suppose \(f_0(h_0)=0\) for some \(h_0>0\). Let \(h\in H\). Since \(h/h_0\) is rational, there are integers \(n>0\) and \(m\) with \(nh=mh_0\). Then \(nf_0(h)=mf_0(h_0)=0\), and \(f_0(h)=0\), because a totally ordered group has no torsion. So if \(f_0\neq0\), then \(f_0(h)\neq0\) for all \(h>0\). As \(f_0(h)\geq f_0(0)=0\), we get \(f_0(h)>0\) for \(h>0\).

(3) Fix \(h_0>0\) in \(H\) and put \(\lambda=f_0(h_0)/h_0\geq0\). With \(n,m\) as in (2), \(nf_0(h)=m\lambda h_0=n\lambda h\). \(\square\)

A subgroup \(L\) of \(G\) has *rank one* if \(L\neq0\) and \(L\), with the order induced from \(G\), is isomorphic as an ordered group to a subgroup of \(\mathbb Q\).

**Theorem 4.3.** Let \(G\) be a totally ordered abelian group. Identify the stalk of the structure sheaf at \(p_H\) with \(H_{\max}\) by Theorem 3.2.

1. Every point over \(G_{\max}\) is equivalent to a point \((p_H,f)\), with \(H\) a non-zero subgroup of \(\mathbb Q\) and \(f:H_{\max}\to G_{\max}\) a morphism of semirings.
2. Two points \((p_H,f)\) and \((p_{H'},f')\) are equivalent if and only if there is \(r\in\mathbb Q_{>0}\) with \(H'=rH\) and \(f'(rh)=f(h)\) for all \(h\in H\).
3. The point \((p_H,f)\) is degenerate if and only if \(f_0=0\). The map \((p_H,f)\mapsto p_H\) induces a bijection from the set of classes of degenerate points to the set of isomorphism classes of points of \(\widehat{\mathbb N^\times}\).
4. If \((p_H,f)\) is not degenerate, then \(f_0(H)\) is a rank-one subgroup of \(G\). The map \((p_H,f)\mapsto f_0(H)\) induces a bijection from the set of classes of non-degenerate points to the set of rank-one subgroups of \(G\).

**Proof.** (1) Let \((p,f)\) be a point. By Theorem 2.2 there is an isomorphism \(\varphi:p\to p_H\) for some \(H\). Then \((p,f)\) is equivalent to \((p_H,f\circ\varphi_{\mathcal O}^{-1})\).

(2) By Theorem 2.2 the isomorphisms \(p_H\to p_{H'}\) are the numbers \(r\in\mathbb Q_{>0}\) with \(rH=H'\). By Theorem 3.2 they act on the stalks by \(h\mapsto rh\).

(3) The image of \(f\) is \(\{-\infty\}\cup f_0(H)\). It equals \(\{-\infty,0\}\) if and only if \(f_0=0\). For each \(H\) there is exactly one \(f\) with \(f_0=0\). By (2), two degenerate points \((p_H,f)\) and \((p_{H'},f')\) are equivalent if and only if \(H'=rH\) for some \(r\), that is, if and only if \(p_H\cong p_{H'}\).

(4) Let \(f_0\neq0\). By Lemma 4.2, \(f_0\) is strictly increasing. So it is an isomorphism of ordered groups from \(H\) to \(L=f_0(H)\), and \(L\) has rank one. Equivalent points have the same \(L\): with \(r\) as in (2), \(f'_0(H')=f'_0(rH)=f_0(H)\).

The map is injective. Let \(f_0(H)=f'_0(H')=L\). Then \(\vartheta=(f'_0)^{-1}\circ f_0\) is an isomorphism of ordered groups \(H\to H'\). It restricts to an equivariant bijection \(H_{>0}\to H'_{>0}\). By Theorem 2.2(3) there is \(r\in\mathbb Q_{>0}\) with \(\vartheta(h)=rh\) for \(h>0\), hence for all \(h\in H\), and \(rH=H'\). Since \(f'(rh)=f'(\vartheta(h))=f(h)\), the two points are equivalent by (2).

The map is surjective. Let \(L\subseteq G\) have rank one. There are a non-zero subgroup \(H\subseteq\mathbb Q\) and an isomorphism of ordered groups \(g:H\to L\). By Lemma 4.2(1), \(g\) extends to a morphism of semirings \(f:H_{\max}\to G_{\max}\), and \((p_H,f)\) is sent to \(L\). \(\square\)

**Corollary 4.4 (the case \(G=\mathbb R\)).** For a non-zero subgroup \(H\subseteq\mathbb Q\) and a real number \(\lambda\geq0\), let \((H,\lambda)\) denote the point \((p_H,f)\) over \(\mathbb R_{\max}\) with \(f(h)=\lambda h\).

1. Every point over \(\mathbb R_{\max}\) is equivalent to some \((H,\lambda)\). Two points \((H,\lambda)\) and \((H',\lambda')\) are equivalent if and only if there is \(r\in\mathbb Q_{>0}\) with \(H'=rH\) and \(\lambda'=\lambda/r\).
2. \((H,\lambda)\) is degenerate if and only if \(\lambda=0\).
3. A subgroup \(L\) of \(\mathbb R\) has rank one if and only if \(L\neq0\) and \(x/y\in\mathbb Q\) for all non-zero \(x,y\in L\). The rank-one subgroups of \(\mathbb R\) are the groups \(\lambda H\) with \(\lambda>0\) and \(H\) a non-zero subgroup of \(\mathbb Q\). Under Theorem 4.3(4), the class of \((H,\lambda)\) with \(\lambda>0\) corresponds to \(L=\lambda H\).
4. \(\operatorname{Fr}_\mu\) sends the class of \((H,\lambda)\) to the class of \((H,\mu\lambda)\). On rank-one subgroups it acts by \(L\mapsto\mu L\). It fixes every degenerate point.

**Proof.** (1) and (2) follow from Lemma 4.2(3) and Theorem 4.3: the condition \(f'(rh)=f(h)\) reads \(\lambda'rh=\lambda h\). (3) If \(L=\lambda H\), the ratios are rational and \(h\mapsto\lambda h\) is an isomorphism of ordered groups \(H\to L\). If \(L\neq0\) has rational ratios, fix \(x_0>0\) in \(L\); then \(H=x_0^{-1}L\) is a subgroup of \(\mathbb Q\) and \(L=x_0H\). If \(L\) has rank one, it is the image of an isomorphism of ordered groups \(g:H\to L\) with \(H\subseteq\mathbb Q\), and \(g(h)=\lambda h\) with \(\lambda>0\) by Lemma 4.2(3). (4) \(\operatorname{Fr}_\mu\circ f\) is \(h\mapsto\mu\lambda h\). \(\square\)

### The adèle class space

The ring of *adèles* of \(\mathbb Q\) is \(\mathbb A_{\mathbb Q}=\mathbb A^f\times\mathbb R\). The field \(\mathbb Q\) is embedded diagonally, and \(\mathbb Q^\times\) acts on \(\mathbb A_{\mathbb Q}\) by multiplication. The set of orbits \(\mathbb A_{\mathbb Q}/\mathbb Q^\times\) is the *adèle class space* of \(\mathbb Q\). The group \(\widehat{\mathbb Z}^\times\) acts on \(\mathbb A_{\mathbb Q}\) by multiplication on the factor \(\mathbb A^f\). The two actions commute, and we write \(\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\) for the set of orbits of \(\mathbb Q^\times\times\widehat{\mathbb Z}^\times\). We write \([a,x]\) for the class of \((a,x)\in\mathbb A^f\times\mathbb R\). The group \(\mathbb R_+^\times\) acts on this set by scaling the real component: \(\mu\cdot[a,x]=[a,\mu x]\).

This scaling action comes from the idèle class group. The group of *idèles* \(\mathbb A_{\mathbb Q}^\times\) is the group of invertible adèles, and the *idèle class group* is \(C_{\mathbb Q}=\mathbb A_{\mathbb Q}^\times/\mathbb Q^\times\). It acts on the adèle class space by multiplication.

**Lemma 4.5.** Every idèle can be written in exactly one way as \(q\cdot(u,\mu)\) with \(q\in\mathbb Q^\times\), \(u\in\widehat{\mathbb Z}^\times\) and \(\mu\in\mathbb R_+^\times\). So \(C_{\mathbb Q}\cong\widehat{\mathbb Z}^\times\times\mathbb R_+^\times\).

**Proof.** An adèle \((a,x)\) is invertible if and only if \(x\neq0\), \(a_p\neq0\) for all \(p\), and \(v_p(a_p)=0\) for all but finitely many \(p\). For such an adèle put \(q=\operatorname{sign}(x)\prod_pp^{v_p(a_p)}\), a finite product. Then \(q^{-1}(a,x)\) has valuation \(0\) at every prime and a positive real component, so it lies in \(\widehat{\mathbb Z}^\times\times\mathbb R_+^\times\). If \(q\in\mathbb Q^\times\) lies in \(\widehat{\mathbb Z}^\times\times\mathbb R_+^\times\), then \(v_p(q)=0\) for all \(p\) and \(q>0\), so \(q=1\). This gives uniqueness. \(\square\)

On the quotient by \(\widehat{\mathbb Z}^\times\), the class of \((u,\mu)\) in \(C_{\mathbb Q}\) acts as the scaling by \(\mu\). So the action of \(C_{\mathbb Q}\) on \(\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\) is the scaling action of \(\mathbb R_+^\times=C_{\mathbb Q}/\widehat{\mathbb Z}^\times\).

**Theorem 4.6.** Recall the subgroup \(H_a\) of Proposition 2.4 and the points \((H,\lambda)\) of Corollary 4.4.

1. The map \((a,x)\mapsto(H_a,|x|)\) induces a bijection
\[
\Theta:\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\to\mathcal P(\mathbb R)
\]
from the quotient of the adèle class space of \(\mathbb Q\) by \(\widehat{\mathbb Z}^\times\) to the set of equivalence classes of points of the arithmetic site over \(\mathbb R_{\max}\).
2. \(\Theta(\mu\cdot c)=\operatorname{Fr}_\mu(\Theta(c))\) for all \(\mu\in\mathbb R_+^\times\). So the action of the Frobenius automorphisms on the points corresponds to the action of the idèle class group on the quotient of the adèle class space.
3. The classes \([a,0]\) correspond to the degenerate points. They form a copy of \(\mathbb Q_{>0}\backslash\mathbb A^f/\widehat{\mathbb Z}^\times\), the set of isomorphism classes of points of the topos. The classes \([a,x]\) with \(x\neq0\) correspond to the rank-one subgroups \(|x|H_a\) of \(\mathbb R\).

*Reference:* [Connes–Consani 2016b, Theorem 3.8 and Lemma 3.7].

**Proof.** (1) Two pairs \((a,x)\) and \((a',x')\) have the same class if and only if there are \(q\in\mathbb Q^\times\) and \(u\in\widehat{\mathbb Z}^\times\) with \(a'=qua\) and \(x'=qx\). We claim that this holds if and only if there are \(s\in\mathbb Q_{>0}\) and \(u\in\widehat{\mathbb Z}^\times\) with \(a'=sua\) and \(|x'|=s|x|\). If \(q,u\) are given, take \(s=|q|\) and replace \(u\) by \(-u\) if \(q<0\); this is allowed because \(-1\in\widehat{\mathbb Z}^\times\). If \(s,u\) are given, then \(x'=sx\) or \(x'=-sx\); in the first case take \(q=s\), in the second take \(q=-s\) and replace \(u\) by \(-u\).

By Proposition 2.4, \(a'\in s\widehat{\mathbb Z}^\times a\) if and only if \(H_{a'}=s^{-1}H_a\). So \((a,x)\) and \((a',x')\) have the same class if and only if there is \(r=s^{-1}\in\mathbb Q_{>0}\) with \(H_{a'}=rH_a\) and \(|x'|=|x|/r\). By Corollary 4.4(1) this says that \((H_a,|x|)\) and \((H_{a'},|x'|)\) are equivalent. So \(\Theta\) is well defined and injective. It is surjective, because every point is equivalent to some \((H,\lambda)\), and \(H=H_a\) for some \(a\) by Proposition 2.4.

(2) \(\Theta(\mu\cdot[a,x])\) is the class of \((H_a,\mu|x|)\), which is \(\operatorname{Fr}_\mu\) of the class of \((H_a,|x|)\) by Corollary 4.4(4). The statement on the idèle class group is the remark after Lemma 4.5.

(3) This follows from Corollary 4.4(2) and (3) and Proposition 2.4(2). \(\square\)

### Orbits of the Frobenius flow

**Proposition 4.7.** Let \(H\) be a non-zero subgroup of \(\mathbb Q\) and \(\lambda>0\). The set of \(\mu\in\mathbb R_+^\times\) such that \(\operatorname{Fr}_\mu\) fixes the class of \((H,\lambda)\) is the subgroup of \(\mathbb Q_{>0}\) generated by the primes \(p\) with \(h_p(H)=+\infty\). These are the primes with \(pH=H\). For \(H=H_a\) they are the primes with \(a_p=0\).

**Proof.** By Corollary 4.4, \((H,\mu\lambda)\) is equivalent to \((H,\lambda)\) if and only if there is \(r\in\mathbb Q_{>0}\) with \(rH=H\) and \(\mu\lambda=\lambda/r\), that is, if and only if \(\mu^{-1}\), or equivalently \(\mu\), lies in the group \(\{r\in\mathbb Q_{>0}:rH=H\}\). By Lemma 2.3, \(rH=H\) if and only if \(h_p(H)-v_p(r)=h_p(H)\) for all \(p\), that is, \(v_p(r)=0\) for every \(p\) with \(h_p(H)\) finite. The positive rationals with this property form the subgroup generated by the primes \(p\) with \(h_p(H)=+\infty\). For \(r=p\) the criterion shows that \(pH=H\) if and only if \(h_p(H)=+\infty\). The last statement is Proposition 2.4(1). \(\square\)

**Example 4.8.** (a) \(H=\mathbb Z\). The points \((\mathbb Z,\lambda)\), \(\lambda>0\), correspond to the subgroups \(\lambda\mathbb Z\) of \(\mathbb R\). No \(\operatorname{Fr}_\mu\) with \(\mu\neq1\) fixes one of them. The orbit is a copy of \(\mathbb R_+^\times\).

(b) \(H=\mathbb Z[1/p]\). The point \((H,\lambda)\) is fixed exactly by \(\operatorname{Fr}_\mu\) with \(\mu\in p^{\mathbb Z}\). Its orbit is \(\mathbb R_+^\times/p^{\mathbb Z}\), a circle of length \(\log p\) in the coordinate \(\log\mu\). By Proposition 4.7 the same holds for every \(H\) with \(h_p(H)=+\infty\) and all other \(h_l(H)\) finite. In adelic terms these are the classes \([a,x]\) with \(x\neq0\), \(a_p=0\) and \(a_l\neq0\) for all primes \(l\neq p\). They form the periodic orbits of length \(\log p\) of the Frobenius flow.

(c) \(H=\mathbb Z[1/6]\). The isotropy group is \(2^{\mathbb Z}3^{\mathbb Z}\). It is dense in \(\mathbb R_+^\times\), because \(\log2/\log3\) is irrational. So the quotient topology on the orbit \(\mathbb R_+^\times/2^{\mathbb Z}3^{\mathbb Z}\) is the trivial one: its only open sets are the empty set and the whole orbit. This orbit is not a line or a circle, in contrast with the orbits in (a) and (b).

(d) \(G=\mathbb Z\). The rank-one subgroups of \(\mathbb Z\) are the subgroups \(n\mathbb Z\) with \(n\geq1\). By Theorem 4.3 the non-degenerate points over \(\mathbb Z_{\max}\) correspond to the positive integers, and they all lie over the point \(p_{\mathbb Z}\) of the topos. Exercise 4 continues this example.

## 5. The square of the site and the Frobenius correspondences

In this section and the next we use the min-plus form of the semirings. The map \(x\mapsto-x\) is an isomorphism \(G_{\max}\to G_{\min}\), and it commutes with the maps \(\operatorname{Fr}_k\). So the arithmetic site is also the pair \((\widehat{\mathbb N^\times},\mathbb Z_{\min})\), and the results of Sections 3 and 4 hold with \(\min\) in place of \(\max\). In \(G_{\min}\) the zero is \(\infty\), the unit is \(0\), the semiring sum of two elements is the smaller one, and the semiring product is their sum as numbers. We write \(\mathbb N_{\min}=(\mathbb N\cup\{\infty\},\min,+)\) for the sub-semiring of \(\mathbb Z_{\min}\) of the elements \(x\) with \(\min(x,0)=0\). It is written \(\mathbb Z_{\min}^+\) in [Connes–Consani 2016b].

### The tensor square

A *\(\mathbb B\)-module* is a commutative monoid \((E,\oplus,0)\) with \(x\oplus x=x\) for all \(x\). It carries the partial order \(x\leq y\iff x\oplus y=y\), and \(x\oplus y\) is the least upper bound of \(x\) and \(y\). A map between \(\mathbb B\)-modules is *linear* if it preserves \(\oplus\) and \(0\). A map \(\varphi:E_1\times E_2\to F\) is *bilinear* if it is linear in each variable.

For a totally ordered set \(P\), the set \(P_{\min}=P\cup\{\infty\}\) with the operation \(\min\) is a \(\mathbb B\)-module with zero \(\infty\). Let \(P_1\) and \(P_2\) be totally ordered sets. The *quadrant* with corner \((u,v)\in P_1\times P_2\) is
\[
\langle u,v\rangle=\{(a,b)\in P_1\times P_2:a\geq u,\ b\geq v\}.
\]
Let \(\operatorname{Sub}(P_1\times P_2)\) be the set of finite unions of quadrants, the empty set included. It is a \(\mathbb B\)-module under union, with zero \(\emptyset\).

**Proposition 5.1.** Let \(P_1\) and \(P_2\) be totally ordered sets. Define \(\psi:(P_1)_{\min}\times(P_2)_{\min}\to\operatorname{Sub}(P_1\times P_2)\) by \(\psi(u,v)=\langle u,v\rangle\) for \(u\in P_1\) and \(v\in P_2\), and \(\psi(u,v)=\emptyset\) if \(u=\infty\) or \(v=\infty\). Then \(\psi\) is bilinear. For every bilinear map \(\varphi:(P_1)_{\min}\times(P_2)_{\min}\to F\) into a \(\mathbb B\)-module there is exactly one linear map \(\rho:\operatorname{Sub}(P_1\times P_2)\to F\) with \(\rho\circ\psi=\varphi\).

In other words, \(\operatorname{Sub}(P_1\times P_2)\) is the tensor product \((P_1)_{\min}\otimes_{\mathbb B}(P_2)_{\min}\).

*Reference:* [Connes–Consani 2016b, Proposition 6.6], for \(P_1=P_2=\mathbb Z\).

**Proof.** Let \(P\) be a totally ordered set and \(g:P_{\min}\to F\) a map with \(g(\infty)=0\). Then \(g\) is linear if and only if it reverses the order, that is, \(u\leq u'\) implies \(g(u')\leq g(u)\). Indeed, if \(g\) is linear and \(u\leq u'\), then \(g(u)=g(\min(u,u'))=g(u)\oplus g(u')\). Conversely, \(\min(u,u')\) is one of the two elements, say \(u\), and then \(g(u)\oplus g(u')=g(u)\) because \(g(u')\leq g(u)\). So a map \(\varphi\) on \((P_1)_{\min}\times(P_2)_{\min}\) is bilinear if and only if it vanishes when one argument is \(\infty\) and reverses the order in each variable. The map \(\psi\) has these properties, since \(u\leq u'\) implies \(\langle u',v\rangle\subseteq\langle u,v\rangle\).

Let \(\varphi\) be bilinear. For \(E=\bigcup_{i\in I}\langle\alpha_i\rangle\), with \(I\) finite and \(\alpha_i\in P_1\times P_2\), put \(\rho(E)=\bigoplus_{i\in I}\varphi(\alpha_i)\). This does not depend on the representation of \(E\). Let also \(E=\bigcup_j\langle\beta_j\rangle\). Each \(\beta_j\) lies in \(E\), so \(\beta_j\geq\alpha_i\) in both coordinates for some \(i\). Then \(\varphi(\beta_j)\leq\varphi(\alpha_i)\leq\bigoplus_i\varphi(\alpha_i)\). Hence \(\bigoplus_j\varphi(\beta_j)\leq\bigoplus_i\varphi(\alpha_i)\), and by symmetry the two are equal. The map \(\rho\) is linear, because a representation of \(E\cup E'\) is obtained by putting together representations of \(E\) and \(E'\). It satisfies \(\rho\circ\psi=\varphi\). It is the only linear map with this property, because every element of \(\operatorname{Sub}(P_1\times P_2)\) is a finite union of quadrants. \(\square\)

**Proposition 5.2.** Let \(G_1\) and \(G_2\) be totally ordered abelian groups, or let \(G_1=G_2=\mathbb N\).

1. \(\operatorname{Sub}(G_1\times G_2)\) is an idempotent semiring. Its addition is the union, its multiplication is the sum \(E+E'=\{\alpha+\alpha':\alpha\in E,\ \alpha'\in E'\}\), its zero is \(\emptyset\) and its unit is \(\langle0,0\rangle\). Moreover \(\langle\alpha\rangle+\langle\alpha'\rangle=\langle\alpha+\alpha'\rangle\).
2. The maps \(\iota_1(a)=\langle a,0\rangle\) and \(\iota_2(b)=\langle0,b\rangle\), with \(\iota_j(\infty)=\emptyset\), are morphisms of semirings \((G_j)_{\min}\to\operatorname{Sub}(G_1\times G_2)\).
3. Let \(R\) be an idempotent semiring, and let \(f_j:(G_j)_{\min}\to R\) be morphisms of semirings for \(j=1,2\). There is exactly one morphism of semirings \(\rho:\operatorname{Sub}(G_1\times G_2)\to R\) with \(\rho\circ\iota_j=f_j\). It is given by \(\rho\big(\bigcup_i\langle a_i,b_i\rangle\big)=\bigoplus_if_1(a_i)f_2(b_i)\).

So \(\operatorname{Sub}(G_1\times G_2)\) is the coproduct of \((G_1)_{\min}\) and \((G_2)_{\min}\) in the category of idempotent semirings.

**Proof.** (1) The inclusion \(\langle\alpha\rangle+\langle\alpha'\rangle\subseteq\langle\alpha+\alpha'\rangle\) is clear. If \(\beta\geq\alpha+\alpha'\) in both coordinates, then \(\beta=\alpha+(\beta-\alpha)\) with \(\beta-\alpha\geq\alpha'\); in the case of \(\mathbb N\) the difference lies again in \(\mathbb N\times\mathbb N\). So \(\langle\alpha\rangle+\langle\alpha'\rangle=\langle\alpha+\alpha'\rangle\). The sum distributes over unions. Hence the sum of two finite unions of quadrants is a finite union of quadrants. The sum is commutative and associative, \(\emptyset+E=\emptyset\), and \(\langle0,0\rangle+E=E\).

(2) \(\iota_1(\min(a,a'))=\langle a,0\rangle\cup\langle a',0\rangle\), because one of the two quadrants contains the other. \(\iota_1(a+a')=\iota_1(a)+\iota_1(a')\) by (1), and \(\iota_1(0)=\langle0,0\rangle\). The same holds for \(\iota_2\).

(3) The map \((a,b)\mapsto f_1(a)f_2(b)\) is bilinear. By Proposition 5.1 there is exactly one linear map \(\rho\) with \(\rho\langle a,b\rangle=f_1(a)f_2(b)\). It is multiplicative on quadrants by (1), hence on all elements by distributivity, and \(\rho\langle0,0\rangle=1\). So \(\rho\) is a morphism of semirings with \(\rho\circ\iota_j=f_j\). Conversely, a morphism \(\rho\) with \(\rho\circ\iota_j=f_j\) satisfies \(\rho\langle a,b\rangle=\rho(\iota_1(a)+\iota_2(b))=f_1(a)f_2(b)\). So it is unique. \(\square\)

**Definition 5.3.** For \(n,m\in\mathbb N^\times\) let \(\operatorname{Fr}_{n,m}\) be the endomorphism of the semiring \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\) with \(\operatorname{Fr}_{n,m}\circ\iota_1=\iota_1\circ\operatorname{Fr}_n\) and \(\operatorname{Fr}_{n,m}\circ\iota_2=\iota_2\circ\operatorname{Fr}_m\), which exists by Proposition 5.2(3). So
\[
\operatorname{Fr}_{n,m}\Big(\bigcup_i\langle a_i,b_i\rangle\Big)=\bigcup_i\langle na_i,mb_i\rangle,
\]
and \(\operatorname{Fr}_{n,m}\circ\operatorname{Fr}_{n',m'}=\operatorname{Fr}_{nn',mm'}\). The *square of the arithmetic site* is the pair \((\widehat{\mathbb N^\times\times\mathbb N^\times},\operatorname{Sub}(\mathbb Z\times\mathbb Z))\): the topos of sets with an action of the monoid \(\mathbb N^\times\times\mathbb N^\times\), together with the semiring \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)=\mathbb Z_{\min}\otimes_{\mathbb B}\mathbb Z_{\min}\), on which \((n,m)\) acts by \(\operatorname{Fr}_{n,m}\).

*Reference:* [Connes–Consani 2016b, Proposition 6.7 and Definition 6.10], where this pair is called the unreduced square.

The *multiplication* \(\mu:\operatorname{Sub}(\mathbb Z\times\mathbb Z)\to\mathbb Z_{\min}\) is the morphism with \(\mu\circ\iota_1=\mu\circ\iota_2=\mathrm{id}\). So \(\mu(E)=\min\{a+b:(a,b)\in E\}\). It plays the role of the diagonal: for a ring \(A\), the diagonal of \(\operatorname{Spec}A\times\operatorname{Spec}A\) is defined by the multiplication \(A\otimes A\to A\).

The map \(\operatorname{Fr}_{n,n}\) is not the \(n\)-th power map of the semiring \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\); see Example 5.10.

Points of the square over \(\mathbb R_{\min}\), their equivalence and their classes are defined as in Definition 4.1, with the topos \(\widehat{\mathbb N^\times\times\mathbb N^\times}\) and the semiring \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\). The next result justifies the name "square".

**Proposition 5.4.**

1. Every point of \(\widehat{\mathbb N^\times\times\mathbb N^\times}\) is isomorphic to the point \(p_{H_1,H_2}\) given by the flat set \(H_{1,>0}\times H_{2,>0}\), for non-zero subgroups \(H_1,H_2\subseteq\mathbb Q\). The isomorphisms \(p_{H_1,H_2}\to p_{H_1',H_2'}\) are the pairs \((r_1,r_2)\) of positive rationals with \(r_jH_j=H_j'\).
2. The stalk of \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\) at \(p_{H_1,H_2}\) is isomorphic to the semiring \(\operatorname{Sub}(H_1\times H_2)\), by the map \(\big[(y_1,y_2),\bigcup_i\langle a_i,b_i\rangle\big]\mapsto\bigcup_i\langle a_iy_1,b_iy_2\rangle\).
3. For points \((p_{H_j},f_j)\) of the arithmetic site over \(\mathbb R_{\min}\), \(j=1,2\), let \(f\) be the morphism \(\operatorname{Sub}(H_1\times H_2)\to\mathbb R_{\min}\) with \(f\circ\iota_j=f_j\). Then \(\big((p_{H_1},f_1),(p_{H_2},f_2)\big)\mapsto(p_{H_1,H_2},f)\) induces a bijection from \(\mathcal P(\mathbb R)\times\mathcal P(\mathbb R)\) to the set of equivalence classes of points of the square over \(\mathbb R_{\min}\).

*Reference:* [Connes–Consani 2016b, Proposition 6.11].

**Proof.** (1) The monoid \(M=\mathbb N^\times\times\mathbb N^\times\) is cancellative, with group of fractions \(\mathbb Q_{>0}\times\mathbb Q_{>0}\). By Proposition 2.1 it is enough to find its directed \(M\)-subsets \(P\). Let \(P_1\) and \(P_2\) be the two projections of \(P\). Each \(P_j\) is a directed \(\mathbb N^\times\)-subset of \(\mathbb Q_{>0}\): it is stable under \(\mathbb N^\times\), and for two elements of \(P_j\) one takes the \(j\)-th coordinate of a common \(c\in P\) for two preimages. So \(P_j=H_{j,>0}\) by the proof of Theorem 2.2. We claim that \(P=P_1\times P_2\). Let \((p_1,p_2)\in P_1\times P_2\). There are \(q_1,q_2\) with \((p_1,q_2)\in P\) and \((q_1,p_2)\in P\). Choose \(c=(c_1,c_2)\in P\) with \((p_1,q_2)=(k_1c_1,k_2c_2)\) and \((q_1,p_2)=(l_1c_1,l_2c_2)\). Then \((p_1,p_2)=(k_1,l_2)\cdot c\in P\). Conversely, every product \(H_{1,>0}\times H_{2,>0}\) is a directed \(M\)-subset. The statement on isomorphisms follows from Proposition 2.1(3).

(2) Write \(y=(y_1,y_2)\), and for \(E=\bigcup_i\langle a_i,b_i\rangle\) put \(yE=\bigcup_i\langle a_iy_1,b_iy_2\rangle\). This does not depend on the representation of \(E\), because \(yE\) is the set of all \((h_1,h_2)\in H_1\times H_2\) with \((h_1,h_2)\geq(ay_1,by_2)\) for some \((a,b)\in E\). Also
\[
E=\{(a,b)\in\mathbb Z\times\mathbb Z:(ay_1,by_2)\in yE\},
\]
since \((ay_1,by_2)\geq(a_iy_1,b_iy_2)\) if and only if \((a,b)\geq(a_i,b_i)\). We refer to this as (S). The map \([y,E]\mapsto yE\) is well defined on the tensor product, because \((ny_1,my_2)E=y\operatorname{Fr}_{n,m}(E)\).

It is surjective. Let \(\bigcup_i\langle h_i,h_i'\rangle\) be given. The finitely many \(h_i\) lie in a cyclic subgroup of \(H_1\), so \(h_i=a_iy_1\) with \(y_1\in H_{1,>0}\) and \(a_i\in\mathbb Z\). In the same way \(h_i'=b_iy_2\).

It is injective. Let \(yE=y'E'\). Choose \(z=(z_1,z_2)\) and \(k_j,k_j'\) with \(y_j=k_jz_j\) and \(y_j'=k_j'z_j\). Then \([y,E]=[z,\operatorname{Fr}_{k_1,k_2}E]\) and \([y',E']=[z,\operatorname{Fr}_{k_1',k_2'}E']\), and \(z\operatorname{Fr}_{k_1,k_2}E=yE=y'E'=z\operatorname{Fr}_{k_1',k_2'}E'\). By (S), \(\operatorname{Fr}_{k_1,k_2}E=\operatorname{Fr}_{k_1',k_2'}E'\). So the two classes are equal.

It is a morphism of semirings. For two classes \([z,E]\) and \([z,F]\) with the same \(z\) we have \(z(E\cup F)=zE\cup zF\) and \(z(E+F)=zE+zF\), by Proposition 5.2(1), and \(z\emptyset=\emptyset\), \(z\langle0,0\rangle=\langle0,0\rangle\).

(3) By (1) and (2), every point of the square over \(\mathbb R_{\min}\) is equivalent to a point \((p_{H_1,H_2},f)\) with \(f:\operatorname{Sub}(H_1\times H_2)\to\mathbb R_{\min}\) a morphism of semirings. By Proposition 5.2(3), such morphisms \(f\) correspond to pairs \((f_1,f_2)=(f\circ\iota_1,f\circ\iota_2)\). An isomorphism \((r_1,r_2)\) of points acts on the stalks by \(\langle h_1,h_2\rangle\mapsto\langle r_1h_1,r_2h_2\rangle\). By the uniqueness in Proposition 5.2(3), it is compatible with \(f\) and \(f'\) if and only if each \(r_j\) is compatible with \(f_j\) and \(f_j'\). So the classes of points of the square correspond to the pairs of classes of points of the site. \(\square\)

### The Frobenius morphisms

**Definition 5.5.** For a real number \(\lambda>0\) let \(\mathcal F_\lambda:\operatorname{Sub}(\mathbb Z\times\mathbb Z)\to\mathbb R_{\min}\) be the morphism of semirings with \(\mathcal F_\lambda(\iota_1(a))=\lambda a\) and \(\mathcal F_\lambda(\iota_2(b))=b\). Explicitly,
\[
\mathcal F_\lambda\Big(\bigcup_i\langle a_i,b_i\rangle\Big)=\min_i(\lambda a_i+b_i),\qquad\mathcal F_\lambda(\emptyset)=\infty.
\]
The *Frobenius congruence* \(\mathcal C_\lambda\) is the equivalence relation \(E\sim_\lambda E'\iff\mathcal F_\lambda(E)=\mathcal F_\lambda(E')\) on \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\). It is compatible with both operations, because \(\mathcal F_\lambda\) is a morphism.

*Reference:* [Connes–Consani 2016b, Proposition 6.13], where the morphism is written \(\mathcal F(\lambda,q)(E)=q^{\mathcal F_\lambda(E)}\) for a fixed \(q\in(0,1)\).

For \(\lambda=1\) we get \(\mathcal F_1=\mu\), and \(\mathcal C_1\) is the congruence of the diagonal.

**Proposition 5.6.**

1. For \(n,m\in\mathbb N^\times\) one has \(\mu\circ\operatorname{Fr}_{n,m}=m\cdot\mathcal F_{n/m}\). So \(E\sim_{n/m}E'\) if and only if \(\operatorname{Fr}_{n,m}(E)\sim_1\operatorname{Fr}_{n,m}(E')\): the congruence \(\mathcal C_{n/m}\) is the inverse image of the diagonal congruence under \(\operatorname{Fr}_{n,m}\).
2. If \(\lambda\neq\lambda'\), then \(\mathcal C_\lambda\neq\mathcal C_{\lambda'}\).
3. Let \(\lambda\) be irrational and \(E,E'\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\). The following are equivalent.
   - (a) \(\mathcal F_\lambda(E)=\mathcal F_\lambda(E')\).
   - (b) There is \(\delta>0\) such that \(\mathcal F_{\lambda'}(E)=\mathcal F_{\lambda'}(E')\) for all real \(\lambda'\) with \(|\lambda'-\lambda|<\delta\).
   - (c) There is a sequence of pairs \((n_j,m_j)\) of positive integers with \(n_j/m_j\to\lambda\) and \(\mu(\operatorname{Fr}_{n_j,m_j}E)=\mu(\operatorname{Fr}_{n_j,m_j}E')\) for all \(j\).

So for a rational parameter the Frobenius congruence comes from the diagonal and the maps \(\operatorname{Fr}_{n,m}\), and for an irrational parameter it is the limit of the congruences with rational parameters, in the sense of (3).

*Reference:* [Connes–Consani 2016b, Propositions 6.12, 6.13 and 6.16].

**Proof.** (1) Both sides are linear maps, and on a quadrant \(\mu(\operatorname{Fr}_{n,m}\langle a,b\rangle)=na+mb=m\big(\tfrac nma+b\big)\). Multiplication by \(m\) is injective on \(\mathbb R_{\min}\).

(2) Let \(\lambda<\lambda'\). Choose positive integers \(a,b\) with \(\lambda< b/a<\lambda'\), and let \(E=\langle a,0\rangle\cup\langle0,b\rangle\) and \(E'=\langle a,0\rangle\). Then \(\mathcal F_\lambda(E)=\min(\lambda a,b)=\lambda a=\mathcal F_\lambda(E')\), but \(\mathcal F_{\lambda'}(E)=b<\lambda'a=\mathcal F_{\lambda'}(E')\).

(3) If \(E\) or \(E'\) is empty, each of the three conditions says that both are empty. Let both be non-empty, with finitely many corners \(\alpha_i\) of \(E\) and \(\alpha_j'\) of \(E'\). Write \(L_\kappa(a,b)=\kappa a+b\), so that \(\mathcal F_\kappa(E)=\min_iL_\kappa(\alpha_i)\). Since \(\lambda\) is irrational, \(L_\lambda\) is injective on \(\mathbb Z\times\mathbb Z\).

(a) implies (b). Let \(\alpha\) be the corner of \(E\) where \(L_\lambda\) is smallest, and \(\alpha'\) the corner of \(E'\) where it is smallest. By (a), \(L_\lambda(\alpha)=L_\lambda(\alpha')\), so \(\alpha=\alpha'\). For every other corner \(\alpha_i\) of \(E\) we have \(L_\lambda(\alpha_i)>L_\lambda(\alpha)\), and the same holds for \(E'\). These finitely many strict inequalities remain true when \(\lambda\) is replaced by a number \(\lambda'\) close to \(\lambda\). For such \(\lambda'\) we get \(\mathcal F_{\lambda'}(E)=L_{\lambda'}(\alpha)=\mathcal F_{\lambda'}(E')\).

(b) implies (c). Take positive rationals \(n_j/m_j\) converging to \(\lambda\), and use (1).

(c) implies (a). By (1), \(\mathcal F_{n_j/m_j}(E)=\mathcal F_{n_j/m_j}(E')\). The function \(\kappa\mapsto\mathcal F_\kappa(E)\) is continuous, because it is the minimum of finitely many continuous functions. \(\square\)

### Newton polygons and the reduced square

For a non-empty \(E\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\), the *Newton polygon* \(\operatorname{New}(E)\) is the convex hull of \(E\) in \(\mathbb R^2\). If \(E=\bigcup_{i=1}^r\langle\alpha_i\rangle\), then
\[
\operatorname{New}(E)=\operatorname{conv}\{\alpha_1,\dots,\alpha_r\}+\mathbb R_{\geq0}^2 .
\]
We refer to this formula as (N1). The right side is convex and contains \(E\). Conversely, let \(c=\sum_it_i\alpha_i+u\) with \(t_i\geq0\), \(\sum_it_i=1\) and \(u\in\mathbb R_{\geq0}^2\). The point \(u\) is a convex combination \(\sum_js_jn_j\) of points \(n_j\in\mathbb N^2\), for instance of the corners of a unit square that contains it. Then \(c=\sum_{i,j}t_is_j(\alpha_i+n_j)\) is a convex combination of points of \(E\). By (N1), \(\operatorname{New}(E)\) is closed and \(\operatorname{New}(E)+\mathbb R_{\geq0}^2=\operatorname{New}(E)\). Let \(L_\kappa(a,b)=\kappa a+b\). Since \(L_\kappa\geq0\) on \(\mathbb R_{\geq0}^2\), (N1) gives
\[
\mathcal F_\kappa(E)=\min_iL_\kappa(\alpha_i)=\min_{\operatorname{New}(E)}L_\kappa .
\]
We refer to this formula as (N2). It says that \(\kappa\mapsto\mathcal F_\kappa(E)\) records the supporting lines of the Newton polygon.

**Lemma 5.7.** Let \(F\subseteq\mathbb Z^2\) be a subset with \(F+\mathbb N^2\subseteq F\) that is contained in some quadrant. Then \(F\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\).

This is the case of two variables of Dickson's lemma.

**Proof.** After a translation we may assume \(F\subseteq\mathbb N^2\), and we may assume \(F\neq\emptyset\). For \(x\in\mathbb N\) let \(g(x)=\min\{y:(x,y)\in F\}\), with \(g(x)=\infty\) if there is no such \(y\). If \((x,y)\in F\) then \((x+1,y)\in F\), so \(g\) is non-increasing. Let \(x_0\) be the least \(x\) with \(g(x)<\infty\). Let \(J\) be the set that consists of \(x_0\) and of all \(x>x_0\) with \(g(x)< g(x-1)\). It is finite, because \(g\) takes values in \(\mathbb N\) on \([x_0,\infty)\) and drops at each element of \(J\) other than \(x_0\). We claim that \(F=\bigcup_{x\in J}\langle x,g(x)\rangle\). The right side is contained in \(F\). Let \((a,b)\in F\). Then \(a\geq x_0\) and \(b\geq g(a)\). Let \(x\) be the largest element of \(J\) with \(x\leq a\). Then \(g\) is constant on \([x,a]\), so \(g(x)=g(a)\leq b\) and \((a,b)\in\langle x,g(x)\rangle\). \(\square\)

**Theorem 5.8.** Let \(E,E'\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\) be non-empty. The following are equivalent.

- (a) \(\mathcal F_\lambda(E)=\mathcal F_\lambda(E')\) for all real \(\lambda>0\).
- (b) \(\mu(\operatorname{Fr}_{n,m}E)=\mu(\operatorname{Fr}_{n,m}E')\) for all \(n,m\in\mathbb N^\times\).
- (c) \(\operatorname{New}(E)=\operatorname{New}(E')\).
- (d) There is a non-empty \(F\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\) with \(E+F=E'+F\).

If \(E\) and \(E'\) are contained in \(\mathbb N\times\mathbb N\), then \(F\) in (d) can be chosen in \(\mathbb N\times\mathbb N\).

*Reference:* [Connes–Consani 2016b, Propositions 6.19 and 6.21].

**Proof.** (a) and (b) are equivalent. By Proposition 5.6(1), (b) is (a) for rational \(\lambda\). The function \(\lambda\mapsto\mathcal F_\lambda(E)\) is continuous and the rationals are dense.

(c) implies (a) by (N2).

(d) implies (a). \(\mathcal F_\lambda\) is a morphism, so \(\mathcal F_\lambda(E)+\mathcal F_\lambda(F)=\mathcal F_\lambda(E')+\mathcal F_\lambda(F)\), and \(\mathcal F_\lambda(F)\) is a real number.

(a) implies (c). Suppose \(\operatorname{New}(E)\neq\operatorname{New}(E')\). After exchanging \(E\) and \(E'\), there is a point \(c\in\operatorname{New}(E')\) that is not in \(\operatorname{New}(E)\). The set \(\operatorname{New}(E)\) is closed and convex. We claim that there is \((s,t)\in\mathbb R^2\) with
\[
sc_1+tc_2<\inf\{sx+ty:(x,y)\in\operatorname{New}(E)\}.
\]
This is the separation of a point from a closed convex set, and the proof is short. Let \(p=(p_1,p_2)\) be a point of \(\operatorname{New}(E)\) at the least distance from \(c\). It exists: fix \(q\in\operatorname{New}(E)\); the points of \(\operatorname{New}(E)\) that are at most as far from \(c\) as \(q\) form a compact set, and the distance to \(c\) has a minimum on it. Put \((s,t)=p-c\), which is not \((0,0)\). Let \((x,y)\in\operatorname{New}(E)\), put \((d_1,d_2)=(x,y)-p\), and let \(0<\theta\leq1\). The point \(p+\theta(d_1,d_2)\) lies in \(\operatorname{New}(E)\), because this set is convex. So its distance from \(c\) is at least that of \(p\):
\[
(s+\theta d_1)^2+(t+\theta d_2)^2\geq s^2+t^2,\qquad\text{that is,}\qquad2\theta(sd_1+td_2)+\theta^2(d_1^2+d_2^2)\geq0 .
\]
Dividing by \(\theta\) and letting \(\theta\) tend to \(0\) gives \(sd_1+td_2\geq0\). Hence \(sx+ty\geq sp_1+tp_2=sc_1+tc_2+s^2+t^2\) for all \((x,y)\in\operatorname{New}(E)\). This proves the claim.

Since \(\operatorname{New}(E)+\mathbb R_{\geq0}^2=\operatorname{New}(E)\) and the infimum is finite, \(s\geq0\) and \(t\geq0\). By (N1) the infimum equals \(\min_i(sa_i+tb_i)\), taken over the corners \(\alpha_i=(a_i,b_i)\) of \(E\). This is a continuous function of \((s,t)\). So the strict inequality remains true after a small change of \((s,t)\), and we may assume \(s>0\) and \(t>0\). Dividing by \(t\) and putting \(\lambda=s/t\) we get \(L_\lambda(c)<\mathcal F_\lambda(E)\). By (N2), \(\mathcal F_\lambda(E')\leq L_\lambda(c)\). So \(\mathcal F_\lambda(E')<\mathcal F_\lambda(E)\), which contradicts (a).

(c) implies (d). Let \(C=\operatorname{New}(E)=\operatorname{New}(E')\). Write \(E=\bigcup_{i=1}^r\langle\alpha_i\rangle\) and \(E'=\bigcup_{j=1}^{r'}\langle\alpha_j'\rangle\), let \(k=\max(r,r')\), and put
\[
F=kC\cap\mathbb Z^2 .
\]
Then \(F\) is not empty, \(F+\mathbb N^2\subseteq F\), and \(F\) is contained in a quadrant, because \(C\) is. By Lemma 5.7, \(F\in\operatorname{Sub}(\mathbb Z\times\mathbb Z)\). We show that \(E+F=(k+1)C\cap\mathbb Z^2\). Since the same holds for \(E'\), this gives (d).

Since \(C\) is convex, \(C+kC=(k+1)C\). So \(E+F\subseteq(k+1)C\cap\mathbb Z^2\). Let \(z\in(k+1)C\cap\mathbb Z^2\). By (N1), \(z=(k+1)\big(\sum_it_i\alpha_i+u\big)\) with \(t_i\geq0\), \(\sum_it_i=1\) and \(u\in\mathbb R_{\geq0}^2\). Some \(t_i\) is at least \(1/r\geq1/(k+1)\). For this \(i\),
\[
z-\alpha_i=\big((k+1)t_i-1\big)\alpha_i+\sum_{j\neq i}(k+1)t_j\alpha_j+(k+1)u .
\]
The coefficients of the \(\alpha_j\) are non-negative and their sum is \(k\). So \(z-\alpha_i\in kC\) by (N1). As \(z-\alpha_i\in\mathbb Z^2\), it lies in \(F\), and \(z=\alpha_i+(z-\alpha_i)\in E+F\).

If \(E,E'\subseteq\mathbb N\times\mathbb N\), then \(C\subseteq\mathbb R_{\geq0}^2\) and \(F\subseteq\mathbb N\times\mathbb N\). \(\square\)

**Corollary 5.9.** Write \(E\approx E'\) if \(E=E'=\emptyset\), or if both are non-empty and \(\operatorname{New}(E)=\operatorname{New}(E')\).

1. The relation \(\approx\) is a congruence on the semiring \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\). The quotient semiring \(\operatorname{Conv}(\mathbb Z\times\mathbb Z)\) is identified, by \(E\mapsto\operatorname{New}(E)\), with the set of Newton polygons together with \(\emptyset\). Its addition sends \(C,C'\) to the convex hull of \(C\cup C'\), and its multiplication is the sum \(C+C'\). Every \(\operatorname{Fr}_{n,m}\) respects \(\approx\), so \(\mathbb N^\times\times\mathbb N^\times\) acts on \(\operatorname{Conv}(\mathbb Z\times\mathbb Z)\) by semiring endomorphisms.
2. \(\operatorname{Conv}(\mathbb Z\times\mathbb Z)\) is multiplicatively cancellative.
3. Let \(R\) be a multiplicatively cancellative semiring. Every morphism of semirings \(\rho:\operatorname{Sub}(\mathbb Z\times\mathbb Z)\to R\) factors in exactly one way through the quotient map \(\gamma:\operatorname{Sub}(\mathbb Z\times\mathbb Z)\to\operatorname{Conv}(\mathbb Z\times\mathbb Z)\).
4. Let \(\operatorname{Conv}(\mathbb N\times\mathbb N)\) be the image of \(\operatorname{Sub}(\mathbb N\times\mathbb N)\) under \(\gamma\). Every morphism of semirings \(\rho:\operatorname{Sub}(\mathbb N\times\mathbb N)\to R\) into a multiplicatively cancellative semiring with \(\rho\langle1,0\rangle\neq0\) and \(\rho\langle0,1\rangle\neq0\) factors in exactly one way through \(\gamma\).

The pair \((\widehat{\mathbb N^\times\times\mathbb N^\times},\operatorname{Conv}(\mathbb Z\times\mathbb Z))\), with the action of (1), is the *reduced square* of the arithmetic site.

*Reference:* [Connes–Consani 2016b, Proposition 6.21 and Definition 6.22].

**Proof.** (1) By Theorem 5.8, \(\approx\) is the intersection of the congruences \(\mathcal C_\lambda\), \(\lambda>0\); note that \(\mathcal F_\lambda(E)=\infty\) only for \(E=\emptyset\). An intersection of congruences is a congruence. The convex hull of \(E\cup E'\) is the convex hull of \(\operatorname{New}(E)\cup\operatorname{New}(E')\), and the convex hull of \(E+E'\) is \(\operatorname{New}(E)+\operatorname{New}(E')\). By (N1), \(\operatorname{New}(\operatorname{Fr}_{n,m}E)\) is the image of \(\operatorname{New}(E)\) under the linear map \((x,y)\mapsto(nx,my)\), because this map sends \(\mathbb R_{\geq0}^2\) onto itself. So \(E\approx E'\) implies \(\operatorname{Fr}_{n,m}E\approx\operatorname{Fr}_{n,m}E'\).

(2) The quotient is not the zero semiring. Let \(E+F\approx E'+F\) with \(F\neq\emptyset\). If \(E=\emptyset\), then \(E'+F=\emptyset\) and \(E'=\emptyset\). Otherwise \(\mathcal F_\lambda(E)+\mathcal F_\lambda(F)=\mathcal F_\lambda(E')+\mathcal F_\lambda(F)\) for all \(\lambda\), so \(\mathcal F_\lambda(E)=\mathcal F_\lambda(E')\) for all \(\lambda\), and \(E\approx E'\) by Theorem 5.8.

(3) \(R\) is idempotent, because \(1\oplus1=\rho(\langle0,0\rangle\cup\langle0,0\rangle)=1\). So \(x\oplus y=0\) implies \(x=x\oplus x\oplus y=x\oplus y=0\). Let \(E\approx E'\) be non-empty. By Theorem 5.8 there is a non-empty \(F\) with \(E+F=E'+F\), so \(\rho(E)\rho(F)=\rho(E')\rho(F)\). Every quadrant \(\langle a,b\rangle\) is invertible in \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\), with inverse \(\langle-a,-b\rangle\). So \(\rho\langle a,b\rangle\) is invertible in \(R\), hence non-zero. Then \(\rho(F)\), a finite non-empty sum of non-zero elements, is non-zero. Cancelling it gives \(\rho(E)=\rho(E')\). The factorization is unique because \(\gamma\) is surjective.

(4) The proof is the same, with \(F\subseteq\mathbb N\times\mathbb N\). Now \(\rho\langle a,b\rangle=(\rho\langle1,0\rangle)^a(\rho\langle0,1\rangle)^b\) is non-zero because \(R\) has no zero divisors. \(\square\)

**Example 5.10.** Let \(E=\langle2,0\rangle\cup\langle0,2\rangle\) and \(E'=E\cup\langle1,1\rangle\). The point \((1,1)\) is not in \(E\), so \(E\neq E'\). It is the midpoint of \((2,0)\) and \((0,2)\), so \(\operatorname{New}(E)=\operatorname{New}(E')\). For \(F=\langle1,0\rangle\cup\langle0,1\rangle\) one finds
\[
E+F=\langle3,0\rangle\cup\langle2,1\rangle\cup\langle1,2\rangle\cup\langle0,3\rangle=E'+F .
\]
So \(\operatorname{Sub}(\mathbb Z\times\mathbb Z)\) is not multiplicatively cancellative. Moreover \(E'=F+F\) is the square of \(F\) in this semiring, while \(E=\operatorname{Fr}_{2,2}(F)\). So \(\operatorname{Fr}_{2,2}\) is not the squaring map, and the squaring map is not additive: the square of \(\langle1,0\rangle\cup\langle0,1\rangle\) is \(E'\), and the union of the squares is \(E\). In \(\operatorname{Conv}(\mathbb Z\times\mathbb Z)\) the classes of \(E\) and \(E'\) agree, as they must by Lemma 6.1 below.

### Correspondences

**Definition 5.11.** A *correspondence on the arithmetic site* is a triple \((R,\ell,r)\), where \(R\) is a multiplicatively cancellative semiring and \(\ell,r:\mathbb N_{\min}\to R\) are morphisms of semirings, such that \(\ell(1)\neq0\), \(r(1)\neq0\), and \(R\) is generated as a semiring by \(\ell(1)\) and \(r(1)\). Here \(1\) is the integer \(1\in\mathbb N\). It generates \(\mathbb N_{\min}\); it is not the unit of \(\mathbb N_{\min}\), which is the integer \(0\). An *isomorphism* of correspondences \((R,\ell,r)\to(R',\ell',r')\) is an isomorphism of semirings \(\theta:R\to R'\) with \(\theta\circ\ell=\ell'\) and \(\theta\circ r=r'\).

*Reference:* [Connes–Consani 2016b, Definition 7.1], where these triples are called reduced correspondences.

The semiring \(R\) of a correspondence is idempotent, because it receives a morphism from the idempotent semiring \(\mathbb N_{\min}\). It has no zero divisors, so \(\ell(n)=\ell(1)^n\) and \(r(n)=r(1)^n\) are non-zero for all \(n\in\mathbb N\).

**Example 5.12 (the Frobenius correspondences).** For a real number \(\lambda>0\) let
\[
R(\lambda)=\big((\mathbb N+\lambda\mathbb N)\cup\{\infty\},\min,+\big)\subseteq\mathbb R_{\min},\qquad\ell_\lambda(n)=\lambda n,\quad r_\lambda(n)=n .
\]
The triple \(\Psi(\lambda)=(R(\lambda),\ell_\lambda,r_\lambda)\) is a correspondence, the *Frobenius correspondence* with parameter \(\lambda\). The semiring \(R(\lambda)\) is multiplicatively cancellative because it is a sub-semiring of a semifield. For \(\lambda=1\) we get \(\Psi(1)=(\mathbb N_{\min},\mathrm{id},\mathrm{id})\), the identity correspondence. For an integer \(n\geq1\), \(\Psi(n)=(\mathbb N_{\min},\operatorname{Fr}_n,\mathrm{id})\) plays the role of the graph of \(\operatorname{Fr}_n\). Multiplication by \(n\) is an isomorphism from \(\Psi(1/n)\) to \((\mathbb N_{\min},\mathrm{id},\operatorname{Fr}_n)\), which plays the role of the transpose of that graph.

**Proposition 5.13.** Let \((R,\ell,r)\) be a correspondence. There is exactly one morphism of semirings \(\rho:\operatorname{Conv}(\mathbb N\times\mathbb N)\to R\) with \(\rho(\gamma\langle n,0\rangle)=\ell(n)\) and \(\rho(\gamma\langle0,n\rangle)=r(n)\) for all \(n\in\mathbb N\), and \(\rho\) is surjective.

*Reference:* [Connes–Consani 2016b, Lemma 7.2].

**Proof.** By Proposition 5.2(3) for \(G_1=G_2=\mathbb N\), there is exactly one morphism \(\rho_0:\operatorname{Sub}(\mathbb N\times\mathbb N)\to R\) with \(\rho_0\circ\iota_1=\ell\) and \(\rho_0\circ\iota_2=r\). It satisfies \(\rho_0\langle1,0\rangle=\ell(1)\neq0\) and \(\rho_0\langle0,1\rangle=r(1)\neq0\). By Corollary 5.9(4), \(\rho_0=\rho\circ\gamma\) for exactly one \(\rho\). The image of \(\rho\) contains \(\ell(1)\) and \(r(1)\), which generate \(R\). \(\square\)

So every correspondence is a quotient of the semiring \(\operatorname{Conv}(\mathbb N\times\mathbb N)\) of Newton polygons in the quadrant. Correspondences are given by congruences on the reduced square, in the same way as closed subschemes of \(C\times C\) are given by ideals.

**Proposition 5.14.** For the Frobenius correspondence \(\Psi(\lambda)\), the morphism of Proposition 5.13 sends \(\operatorname{New}(E)\) to \(\mathcal F_\lambda(E)\). So \(\Psi(\lambda)\) identifies two Newton polygons exactly when the linear form \(L_\lambda\) has the same minimum on them, that is, when they have the same supporting line of slope \(-\lambda\). If \(\Psi(\lambda)\) and \(\Psi(\lambda')\) are isomorphic correspondences, then \(\lambda=\lambda'\).

*Reference:* [Connes–Consani 2016b, Remark 6.14].

**Proof.** The morphism \(\rho_0\) of the last proof sends \(\langle a,b\rangle\) to the product of \(\ell_\lambda(a)\) and \(r_\lambda(b)\) in \(R(\lambda)\), which is the number \(\lambda a+b=\mathcal F_\lambda\langle a,b\rangle\). Let \(\theta:R(\lambda)\to R(\lambda')\) be an isomorphism of correspondences. Then \(\theta(\lambda a)=\lambda'a\) and \(\theta(b)=b\) for \(a,b\in\mathbb N\). Since \(\theta\) and \(\theta^{-1}\) preserve \(\min\), they preserve the order of real numbers. So \(\lambda a\leq b\) if and only if \(\lambda'a\leq b\), for all \(a,b\in\mathbb N\). If \(\lambda<\lambda'\), choose positive integers with \(\lambda< b/a<\lambda'\); then \(\lambda a\leq b\) but \(\lambda'a>b\). So \(\lambda=\lambda'\). \(\square\)

## 6. The composition law

### Composition of correspondences

For rings, two correspondences given by ring maps \(A\to R\leftarrow A\) and \(A\to R'\leftarrow A\) are composed by forming \(R\otimes_AR'\), where \(R\) is an \(A\)-algebra by its second map and \(R'\) by its first. For the arithmetic site, [Connes–Consani 2016b, Section 7] replaces the tensor product \(R\otimes_{\mathbb N_{\min}}R'\) by its multiplicatively cancellative reduction. We define this reduction by its universal property. The proofs rest on a property of power maps.

**Lemma 6.1.** Let \(T\) be a multiplicatively cancellative idempotent semiring and \(n\geq1\). Then \((x\oplus y)^n=x^n\oplus y^n\) for all \(x,y\in T\), and \(x^n=y^n\) implies \(x=y\).

*Reference:* [Connes 2011, Lemma 4.3]. The lesson *Characteristic one and hyperrings* treats this result as well.

**Proof.** If \(x\oplus y=0\), then \(x=x\oplus x\oplus y=x\oplus y=0\), and also \(y=0\). The semiring \(T\) has no zero divisors: \(ab=0=a\cdot0\) with \(a\neq0\) gives \(b=0\). In an idempotent semiring, \((x\oplus y)^m=\bigoplus_{i=0}^mx^iy^{m-i}\) for all \(m\geq0\), by induction on \(m\).

Let \(s=x\oplus y\). If \(s=0\), then \(x=y=0\) and both claims hold. Let \(s\neq0\). Every monomial \(x^iy^j\) with \(i+j=2n-1\) has \(i\geq n\) or \(j\geq n\). So
\[
(x^n\oplus y^n)\,s^{n-1}=\bigoplus_{i+j=2n-1}x^iy^j=s^{2n-1}=s^n\,s^{n-1}.
\]
Since \(s^{n-1}\neq0\), we can cancel it, and \(x^n\oplus y^n=s^n\).

Now let \(x^n=y^n\). If \(x=0\), then \(y^n=0\) and \(y=0\). Let \(x\) and \(y\) be non-zero; then \(s\neq0\). We have
\[
x\,s^{n-1}=\bigoplus_{i=1}^{n}x^iy^{n-i},\qquad y\,s^{n-1}=\bigoplus_{i=0}^{n-1}x^iy^{n-i}.
\]
The two sums have the same terms for \(1\leq i\leq n-1\). The first has the extra term \(x^n\) and the second has the extra term \(y^n\), and these are equal. So \(x\,s^{n-1}=y\,s^{n-1}\), and \(x=y\). \(\square\)

In an idempotent semiring we say that \(x\) *absorbs* \(y\) if \(x\oplus y=x\). Absorption is transitive, and if \(x\) absorbs \(y\) then \(xz\) absorbs \(yz\). A morphism of semirings preserves absorption. In a sub-semiring of \(\mathbb R_{\min}\), \(x\) absorbs \(y\) exactly when \(x\leq y\) as real numbers.

**Definition 6.2.** Let \(\Psi=(R,\ell,r)\) and \(\Psi'=(R',\ell',r')\) be correspondences.

1. An *amalgam* of \((\Psi,\Psi')\) is a triple \((T,f,g)\), where \(T\) is a multiplicatively cancellative semiring and \(f:R\to T\), \(g:R'\to T\) are morphisms of semirings with \(f\circ r=g\circ\ell'\).
2. An amalgam \((T_0,f_0,g_0)\) is *universal* if for every amalgam \((T,f,g)\) there is exactly one morphism of semirings \(\rho:T_0\to T\) with \(\rho\circ f_0=f\) and \(\rho\circ g_0=g\).
3. Suppose that a universal amalgam \((T_0,f_0,g_0)\) exists and that \(f_0(\ell(1))\neq0\) and \(g_0(r'(1))\neq0\). The *composite* \(\Psi\circ\Psi'\) is the correspondence \((R'',f_0\circ\ell,g_0\circ r')\), where \(R''\) is the sub-semiring of \(T_0\) generated by \(f_0(\ell(1))\) and \(g_0(r'(1))\).

The semiring \(T\) of an amalgam is idempotent, because it receives a morphism from an idempotent semiring. So Lemma 6.1 applies to it. A universal amalgam is unique up to a unique isomorphism, so the composite is well defined up to isomorphism.

A universal amalgam \((T_0,f_0,g_0)\) is generated as a semiring by the images of \(f_0\) and \(g_0\). Indeed, let \(T_1\subseteq T_0\) be the sub-semiring generated by these images. It is multiplicatively cancellative, so \((T_1,f_0,g_0)\) is an amalgam, and universality gives a morphism \(\rho:T_0\to T_1\) with \(\rho\circ f_0=f_0\) and \(\rho\circ g_0=g_0\). Followed by the inclusion \(T_1\subseteq T_0\), it is an endomorphism of \(T_0\) that has the same two properties as the identity. By the uniqueness in Definition 6.2(2) it is the identity, and so \(T_1=T_0\).

[Connes–Consani 2016b, Section 7.2] describes the composite through the tensor product \(R\otimes_{\mathbb N_{\min}}R'\) and the multiplicatively cancellative semiring associated with it. For the Frobenius correspondences it works with maps \(\varphi:R\times R'\to T\) into a multiplicatively cancellative semiring that are additive in each variable, vanish when one argument is zero, and satisfy \(\varphi(aa',bb')=\varphi(a,b)\varphi(a',b')\) and \(\varphi(r(x)a,b)=\varphi(a,\ell'(x)b)\). An amalgam \((T,f,g)\) gives such a map, \(\varphi(a,b)=f(a)g(b)\), and this map sends the pair of units to the unit of \(T\). Conversely, let \(\varphi\) be such a map that sends the pair of units to the unit, and put \(f(a)=\varphi(a,1)\) and \(g(b)=\varphi(1,b)\), where \(1\) denotes the unit of \(R\) or of \(R'\). Then \(f\) and \(g\) are morphisms of semirings, \(\varphi(a,b)=\varphi(a\cdot1,1\cdot b)=f(a)g(b)\), and the last condition with \(a=1\) and \(b=1\) gives \(f\circ r=g\circ\ell'\). So the amalgams correspond to the maps \(\varphi\) of this kind that send the pair of units to the unit. Definition 6.2 states the reduction as a universal property and does not use the tensor product. We do not claim that every pair of correspondences has a universal amalgam. The theorems below show that every pair of Frobenius correspondences has one.

### The generic case

For \(\lambda,\lambda'>0\) let
\[
R(\lambda\lambda',\lambda')=\big((\mathbb N+\lambda\lambda'\mathbb N+\lambda'\mathbb N)\cup\{\infty\},\min,+\big)\subseteq\mathbb R_{\min},
\]
and let \(f_0:R(\lambda)\to R(\lambda\lambda',\lambda')\), \(f_0(a)=\lambda'a\), and \(g_0:R(\lambda')\to R(\lambda\lambda',\lambda')\), \(g_0(b)=b\). These are morphisms of semirings, and \(f_0(r_\lambda(n))=\lambda'n=g_0(\ell_{\lambda'}(n))\). So \((R(\lambda\lambda',\lambda'),f_0,g_0)\) is an amalgam of \((\Psi(\lambda),\Psi(\lambda'))\), for all \(\lambda\) and \(\lambda'\).

Recall that in \(R(\lambda)\) the semiring product of \(a\) and \(a'\) is the number \(a+a'\), and the \(N\)-th power of \(a\) is the number \(Na\).

**Lemma 6.3.** Let \((T,f,g)\) be an amalgam of \((\Psi(\lambda),\Psi(\lambda'))\). For finite \(a\in R(\lambda)\) and \(b\in R(\lambda')\) put \(m(a,b)=f(a)g(b)\). If \(\lambda'a_1+b_1<\lambda'a_2+b_2\), then \(m(a_1,b_1)\) absorbs \(m(a_2,b_2)\).

**Proof.** Let \(\delta=(\lambda'a_2+b_2)-(\lambda'a_1+b_1)>0\), and choose an integer \(N\geq1\) with \(N\delta>2\lambda'\). Let \(k\) be the least integer with \(k\geq Na_1\), and let \(k'\) be the greatest integer with \(k'\leq Na_2\). Both are in \(\mathbb N\), and
\[
\lambda'k+Nb_1< N(\lambda'a_1+b_1)+\lambda'< N(\lambda'a_2+b_2)-\lambda'<\lambda'k'+Nb_2 .
\]
We use three facts.

- In \(R(\lambda)\), \(Na_1\leq k\), so \(Na_1\) absorbs \(k\). Hence \(f(a_1)^N\) absorbs \(f(k)\), and \(m(a_1,b_1)^N=f(a_1)^Ng(b_1)^N\) absorbs \(f(k)g(Nb_1)\).
- Since \(f\circ r_\lambda=g\circ\ell_{\lambda'}\), we have \(f(k)=g(\lambda'k)\), so \(f(k)g(Nb_1)=g(\lambda'k+Nb_1)\). In the same way \(f(k')g(Nb_2)=g(\lambda'k'+Nb_2)\). By the displayed inequality, \(g(\lambda'k+Nb_1)\) absorbs \(g(\lambda'k'+Nb_2)\).
- In \(R(\lambda)\), \(k'\leq Na_2\), so \(f(k')\) absorbs \(f(a_2)^N\), and \(f(k')g(Nb_2)\) absorbs \(m(a_2,b_2)^N\).

By transitivity, \(m(a_1,b_1)^N\) absorbs \(m(a_2,b_2)^N\). By Lemma 6.1,
\[
\big(m(a_1,b_1)\oplus m(a_2,b_2)\big)^N=m(a_1,b_1)^N\oplus m(a_2,b_2)^N=m(a_1,b_1)^N,
\]
and therefore \(m(a_1,b_1)\oplus m(a_2,b_2)=m(a_1,b_1)\). \(\square\)

**Theorem 6.4.** Let \(\lambda,\lambda'>0\). Suppose that \(\lambda\) is rational, or that \(\lambda\lambda'\notin\mathbb Q\lambda'+\mathbb Q\). Then \((R(\lambda\lambda',\lambda'),f_0,g_0)\) is a universal amalgam of \((\Psi(\lambda),\Psi(\lambda'))\), and
\[
\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda').
\]

*Reference:* [Connes–Consani 2016b, Proposition 7.3], for \(\lambda\lambda'\notin\mathbb Q\lambda'+\mathbb Q\).

**Proof.** Let \((T,f,g)\) be an amalgam and \(m(a,b)=f(a)g(b)\) as in Lemma 6.3.

*Step 1. If \(\lambda'a+b=\lambda'a'+b'\), then \(m(a,b)=m(a',b')\).* Suppose first that \(\lambda=c/d\) with positive integers \(c,d\). Then \(da\in\mathbb N\) for every finite \(a\in R(\lambda)\). So \(f(a)^d=f(da)=f(r_\lambda(da))=g(\ell_{\lambda'}(da))=g(\lambda'da)\), and
\[
m(a,b)^d=g(\lambda'da)\,g(db)=g\big(d(\lambda'a+b)\big).
\]
The right side is the same for \((a',b')\). So \(m(a,b)^d=m(a',b')^d\), and \(m(a,b)=m(a',b')\) by Lemma 6.1.

Suppose now that \(\lambda\) is irrational and \(\lambda\lambda'\notin\mathbb Q\lambda'+\mathbb Q\). Write \(a=x\lambda+y\) and \(a'=x'\lambda+y'\) with \(x,y,x',y'\in\mathbb N\). The equality gives \((x-x')\lambda\lambda'=(y'-y)\lambda'+(b'-b)\), which lies in \(\mathbb Q\lambda'+\mathbb Q\). So \(x=x'\), and then \(y\lambda'+b=y'\lambda'+b'\). Since \(f(y)=g(\lambda'y)\), we get \(m(a,b)=f(x\lambda)f(y)g(b)=f(x\lambda)\,g(y\lambda'+b)\), and the same formula for \((a',b')\) gives the same value.

*Step 2. The morphism \(\rho\).* Every finite element \(z\) of \(R(\lambda\lambda',\lambda')\) is \(\lambda'a+b\) with finite \(a\in R(\lambda)\) and \(b\in R(\lambda')\). Put \(\rho(z)=m(a,b)\), which is well defined by Step 1, and \(\rho(\infty)=0\). Then \(\rho(z+z')=\rho(z)\rho(z')\) and \(\rho(0)=1\). For \(z< z'\), \(\rho(z)\) absorbs \(\rho(z')\) by Lemma 6.3, so \(\rho(\min(z,z'))=\rho(z)\oplus\rho(z')\). Hence \(\rho\) is a morphism of semirings. It satisfies \(\rho(f_0(a))=m(a,0)=f(a)\) and \(\rho(g_0(b))=m(0,b)=g(b)\). It is the only such morphism, because every finite element of \(R(\lambda\lambda',\lambda')\) is a product \(f_0(a)g_0(b)\).

*Step 3. The composite.* The elements \(f_0(\ell_\lambda(1))=\lambda\lambda'\) and \(g_0(r_{\lambda'}(1))=1\) generate the sub-semiring \(R(\lambda\lambda')\), and \(f_0\circ\ell_\lambda=\ell_{\lambda\lambda'}\), \(g_0\circ r_{\lambda'}=r_{\lambda\lambda'}\). \(\square\)

### The tangent semiring

Let
\[
\mathbb T=\{(c,s,t)\in\mathbb R^3:s\leq t\}\cup\{\infty\},
\]
with the following operations. The element \(\infty\) is neutral for \(\oplus\) and \(x\cdot\infty=\infty\) for all \(x\). For triples,
\[
(c,s,t)\oplus(c',s',t')=\begin{cases}(c,s,t)&\text{if }c< c',\\ (c',s',t')&\text{if }c'< c,\\ (c,\min(s,s'),\max(t,t'))&\text{if }c=c',\end{cases}
\qquad(c,s,t)\cdot(c',s',t')=(c+c',s+s',t+t').
\]
The triple \((c,s,t)\) stands for the function \(\varepsilon\mapsto c+\min(s\varepsilon,t\varepsilon)\) near \(\varepsilon=0\). It has the value \(c\) at \(0\), the slope \(s\) to the right of \(0\) and the slope \(t\) to the left.

**Lemma 6.5.** With these operations \(\mathbb T\) is a multiplicatively cancellative idempotent semiring with zero \(\infty\) and unit \((0,0,0)\). The map \(\operatorname{ev}:\mathbb T\to\mathbb R_{\min}\), \(\operatorname{ev}(c,s,t)=c\), \(\operatorname{ev}(\infty)=\infty\), is a morphism of semirings.

**Proof.** For \(x=(c,s,t)\) let \(\phi_x(\varepsilon)=c+\min(s\varepsilon,t\varepsilon)\), and let \(\phi_\infty\) be the constant \(\infty\). Since \(s\leq t\), \(\phi_x(\varepsilon)=c+s\varepsilon\) for \(\varepsilon\geq0\) and \(\phi_x(\varepsilon)=c+t\varepsilon\) for \(\varepsilon\leq0\). So \(x\) is determined by the germ of \(\phi_x\) at \(0\). We claim that near \(0\)
\[
\phi_{x\oplus y}=\min(\phi_x,\phi_y),\qquad\phi_{xy}=\phi_x+\phi_y .
\]
The second equality holds for all \(\varepsilon\); check it for \(\varepsilon\geq0\) and for \(\varepsilon\leq0\). For the first, let \(x=(c,s,t)\) and \(y=(c',s',t')\). If \(c< c'\), then \(\phi_x<\phi_y\) near \(0\) by continuity. If \(c=c'\), then \(\min(\phi_x,\phi_y)\) is \(c+\min(s,s')\varepsilon\) for \(\varepsilon\geq0\) and \(c+\max(t,t')\varepsilon\) for \(\varepsilon\leq0\).

The germs at \(0\) of functions with values in \(\mathbb R\cup\{\infty\}\) form an idempotent semiring under pointwise \(\min\) and pointwise \(+\). The map that sends \(x\) to the germ of \(\phi_x\) is injective, it carries the operations of \(\mathbb T\) to these operations, and it carries \((0,0,0)\) and \(\infty\) to the unit and the zero. So the semiring axioms hold in \(\mathbb T\), and \(\mathbb T\) is idempotent. It is multiplicatively cancellative, because its multiplication is the addition of triples. The map \(\operatorname{ev}\) is the evaluation of germs at \(\varepsilon=0\). \(\square\)

**Definition 6.6.** For a real number \(\kappa>0\) let \(u_\kappa=(\kappa,1,1)\) and \(w=(1,0,0)\) in \(\mathbb T\), and let \(R^\varepsilon(\kappa)\) be the sub-semiring of \(\mathbb T\) generated by \(u_\kappa\) and \(w\). Let \(\ell^\varepsilon_\kappa(n)=u_\kappa^n=(n\kappa,n,n)\) and \(r^\varepsilon(n)=w^n=(n,0,0)\) for \(n\in\mathbb N\), and let both maps send \(\infty\) to \(\infty\). The triple \(\Psi^\varepsilon(\kappa)=(R^\varepsilon(\kappa),\ell^\varepsilon_\kappa,r^\varepsilon)\) is the *tangential Frobenius correspondence* with parameter \(\kappa\).

This is a correspondence. The semiring \(R^\varepsilon(\kappa)\) is multiplicatively cancellative as a sub-semiring of \(\mathbb T\). The maps \(\ell^\varepsilon_\kappa\) and \(r^\varepsilon\) are morphisms of semirings, since for \(n< n'\) the element \(u_\kappa^n\) absorbs \(u_\kappa^{n'}\) and \(w^n\) absorbs \(w^{n'}\).

The elements of \(R^\varepsilon(\kappa)\) are found as follows. A monomial is \(u_\kappa^xw^y=(\kappa x+y,x,x)\). A finite sum of monomials is the triple \((c,s,t)\), where \(c\) is the least value of \(\kappa x+y\) among them, and \(s\) and \(t\) are the least and the greatest \(x\) among the monomials with this value. Hence
\[
R^\varepsilon(\kappa)=\{(c,s,t):c\in\mathbb N+\kappa\mathbb N,\ s\leq t,\ s,t\in X_\kappa(c)\}\cup\{\infty\},\qquad X_\kappa(c)=\{x\in\mathbb N:c-\kappa x\in\mathbb N\}.
\]

- If \(\kappa\) is irrational, each set \(X_\kappa(c)\) has one element. Then \(\operatorname{ev}\) restricts to an isomorphism of semirings \(R^\varepsilon(\kappa)\to R(\kappa)\), and this is an isomorphism of correspondences \(\Psi^\varepsilon(\kappa)\to\Psi(\kappa)\).
- If \(\kappa=a/b\) with positive integers \(a,b\), then \(X_\kappa(a)\) contains \(0\) and \(b\). The three elements \(u_\kappa^b=(a,b,b)\), \(w^a=(a,0,0)\) and \(u_\kappa^b\oplus w^a=(a,0,b)\) are different, and \(\operatorname{ev}\) sends each of them to \(a\). An isomorphism of correspondences \(\Psi^\varepsilon(\kappa)\to\Psi(\kappa)\) would send \(u_\kappa\) to \(\kappa\) and \(w\) to \(1\). So it would agree with \(\operatorname{ev}\) on the generators, hence everywhere. As \(\operatorname{ev}\) is not injective, \(\Psi^\varepsilon(\kappa)\) is not isomorphic to \(\Psi(\kappa)\).

[Connes–Consani 2016b, Definition 7.6] calls \(\Psi^\varepsilon(1)\) the tangential deformation of the identity correspondence and writes it \(\operatorname{id}_\varepsilon\). That paper works with germs of functions of \(\varepsilon\), as in the proof of Lemma 6.5, and its generator is the germ of \(\varepsilon\mapsto(1+\varepsilon)\kappa\), which is the triple \((\kappa,\kappa,\kappa)\). The map \((c,s,t)\mapsto(c,\kappa s,\kappa t)\) is an automorphism of \(\mathbb T\) that sends \(u_\kappa\) to this triple and fixes \(w\). So the two choices give isomorphic correspondences.

**Theorem 6.7.** Let \(\lambda\) be irrational and \(\lambda\lambda'\in\mathbb Q\lambda'+\mathbb Q\). Then the pair \((\Psi(\lambda),\Psi(\lambda'))\) has a universal amalgam, and
\[
\Psi(\lambda)\circ\Psi(\lambda')=\Psi^\varepsilon(\lambda\lambda').
\]

*Reference:* [Connes–Consani 2016b, Proposition 7.4].

**Proof.** The number \(\lambda'\) is irrational. Otherwise \(\mathbb Q\lambda'+\mathbb Q=\mathbb Q\), and \(\lambda=\lambda\lambda'/\lambda'\) would be rational.

*The amalgam.* Let \(U_\varepsilon=(\lambda\lambda',1,1)\), \(V_\varepsilon=(\lambda',0,0)\) and \(W_\varepsilon=(1,0,0)\), and let \(T_\varepsilon\) be the sub-semiring of \(\mathbb T\) that they generate. Every finite element of \(R(\lambda)\) is \(x\lambda+y\) for exactly one pair \((x,y)\in\mathbb N^2\), because \(\lambda\) is irrational. Define
\[
f_\varepsilon(x\lambda+y)=U_\varepsilon^xV_\varepsilon^y=(\lambda'(x\lambda+y),x,x),\qquad g_\varepsilon(b)=(b,0,0),
\]
and \(f_\varepsilon(\infty)=g_\varepsilon(\infty)=\infty\). Both maps are multiplicative and send the unit to the unit. They are additive: \(R(\lambda)\) is totally ordered, and if \(a< a'\) then \(f_\varepsilon(a)\) absorbs \(f_\varepsilon(a')\), because \(\lambda'a<\lambda'a'\); the same holds for \(g_\varepsilon\). Note that \(g_\varepsilon(x\lambda'+y)=V_\varepsilon^xW_\varepsilon^y\). Finally \(f_\varepsilon(r_\lambda(n))=(\lambda'n,0,0)=g_\varepsilon(\ell_{\lambda'}(n))\). So \((T_\varepsilon,f_\varepsilon,g_\varepsilon)\) is an amalgam.

*Monomials and fibres.* For \(e=(e_1,e_2,e_3)\in\mathbb Z^3\) let \(\sigma(e)=e_1\lambda\lambda'+e_2\lambda'+e_3\). For \(e\in\mathbb N^3\) the monomial \(M_\varepsilon(e)=U_\varepsilon^{e_1}V_\varepsilon^{e_2}W_\varepsilon^{e_3}\) equals \((\sigma(e),e_1,e_1)\). If \(d\in\mathbb Z^3\) has \(\sigma(d)=0\) and \(d_1=0\), then \(d_2\lambda'+d_3=0\), so \(d=0\), since \(\lambda'\) is irrational. Hence a point of \(\mathbb Z^3\) is determined by its value under \(\sigma\) and its first coordinate. For \(c\in\sigma(\mathbb N^3)\) let \(X(c)\) be the set of first coordinates of the points \(e\in\mathbb N^3\) with \(\sigma(e)=c\), and for \(x\in X(c)\) let \(e(c,x)\) be the point with first coordinate \(x\). For \(i\leq k\leq j\) in \(X(c)\),
\[
(j-i)\,e(c,k)=(j-k)\,e(c,i)+(k-i)\,e(c,j),
\]
because both sides have the value \((j-i)c\) under \(\sigma\) and the first coordinate \((j-i)k\). We refer to this identity as (L).

Every element of \(T_\varepsilon\) other than \(\infty\) is a finite sum of monomials. By the definition of \(\oplus\), such a sum is the triple \((c,s,t)\), where \(c\) is the least value of \(\sigma\) among the monomials, and \(s\leq t\) are the least and the greatest first coordinates among those of value \(c\). So
\[
T_\varepsilon=\{(c,s,t):c\in\sigma(\mathbb N^3),\ s,t\in X(c),\ s\leq t\}\cup\{\infty\},\qquad(c,s,t)=M_\varepsilon(e(c,s))\oplus M_\varepsilon(e(c,t)).
\]

*Universality.* Let \((T,f,g)\) be an amalgam. Put \(U=f(\lambda)\), \(V=f(1)=g(\lambda')\), \(W=g(1)\), and \(M(e)=U^{e_1}V^{e_2}W^{e_3}\) for \(e\in\mathbb N^3\). Then \(M(e+e')=M(e)M(e')\). In the notation of Lemma 6.3, \(M(e)=f(e_1\lambda+e_2)\,g(e_3)=m(e_1\lambda+e_2,e_3)\), and \(\lambda'(e_1\lambda+e_2)+e_3=\sigma(e)\).

Step 1. If \(\sigma(e)<\sigma(e')\), then \(M(e)\) absorbs \(M(e')\). This is Lemma 6.3.

Step 2. Let \(i\leq k\leq j\) in \(X(c)\), and put \(A=M(e(c,i))\), \(B=M(e(c,j))\) and \(D=M(e(c,k))\). Then \(A\oplus B\) absorbs \(D\). If \(i=j\) this is clear, because then \(A=B=D\). Let \(N=j-i\geq1\). By (L), \(D^N=A^{j-k}B^{k-i}\). This is one of the terms of \((A\oplus B)^N=\bigoplus_{l=0}^NA^lB^{N-l}\), so \((A\oplus B)^N\) absorbs \(D^N\). By Lemma 6.1, \((A\oplus B\oplus D)^N=(A\oplus B)^N\oplus D^N=(A\oplus B)^N\), and then \(A\oplus B\oplus D=A\oplus B\).

Step 3. Define \(\rho:T_\varepsilon\to T\) by \(\rho(\infty)=0\) and
\[
\rho(c,s,t)=M(e(c,s))\oplus M(e(c,t)).
\]
It is additive. If \(c< c'\), then \(\rho(c,s,t)\) absorbs \(\rho(c',s',t')\) by Step 1. If \(c=c'\), then by Step 2 the sum of the four monomials of \(\rho(c,s,t)\oplus\rho(c,s',t')\) equals the sum of the two with the first coordinates \(\min(s,s')\) and \(\max(t,t')\). It is multiplicative. The product \(\rho(c,s,t)\rho(c',s',t')\) is the sum of the four monomials \(M(e(c,x)+e(c',x'))\) with \(x\in\{s,t\}\) and \(x'\in\{s',t'\}\). The points \(e(c,x)+e(c',x')\) have the value \(c+c'\), and their first coordinates \(x+x'\) lie between \(s+s'\) and \(t+t'\). By Step 2 the sum equals \(M(e(c+c',s+s'))\oplus M(e(c+c',t+t'))=\rho(c+c',s+s',t+t')\). Also \(\rho(0,0,0)=M(0)=1\). So \(\rho\) is a morphism of semirings.

It sends \(U_\varepsilon,V_\varepsilon,W_\varepsilon\) to \(U,V,W\). Hence \(\rho\circ f_\varepsilon\) and \(f\) agree on the generators \(\lambda\) and \(1\) of \(R(\lambda)\), and \(\rho\circ g_\varepsilon\) and \(g\) agree on the generators \(\lambda'\) and \(1\) of \(R(\lambda')\). So \(\rho\circ f_\varepsilon=f\) and \(\rho\circ g_\varepsilon=g\). Such a \(\rho\) is unique, because \(T_\varepsilon\) is generated by \(U_\varepsilon=f_\varepsilon(\lambda)\), \(V_\varepsilon=f_\varepsilon(1)\) and \(W_\varepsilon=g_\varepsilon(1)\).

*The composite.* The elements \(f_\varepsilon(\ell_\lambda(1))=U_\varepsilon=u_{\lambda\lambda'}\) and \(g_\varepsilon(r_{\lambda'}(1))=W_\varepsilon=w\) generate \(R^\varepsilon(\lambda\lambda')\), and \(f_\varepsilon\circ\ell_\lambda=\ell^\varepsilon_{\lambda\lambda'}\), \(g_\varepsilon\circ r_{\lambda'}=r^\varepsilon\). \(\square\)

In the situation of Theorem 6.7 the triple \((R(\lambda\lambda',\lambda'),f_0,g_0)\) is still an amalgam, but it is not universal. The morphism \(T_\varepsilon\to R(\lambda\lambda',\lambda')\) given by universality is \(\operatorname{ev}\). It is not injective: there is \(d\neq0\) in \(\mathbb Z^3\) with \(\sigma(d)=0\), and then \(e=(|d_1|,|d_2|,|d_3|)\) and \(e+d\) are two points of \(\mathbb N^3\) with the same value under \(\sigma\) and different first coordinates.

### The law in all cases

**Theorem 6.8.** Let \(\lambda,\lambda'>0\) be real numbers. The composite \(\Psi(\lambda)\circ\Psi(\lambda')\) exists.

1. If \(\lambda\lambda'\notin\mathbb Q\), or if \(\lambda\) and \(\lambda'\) are both rational, then \(\Psi(\lambda)\circ\Psi(\lambda')\cong\Psi(\lambda\lambda')\).
2. If \(\lambda\) and \(\lambda'\) are irrational and \(\lambda\lambda'\in\mathbb Q\), then \(\Psi(\lambda)\circ\Psi(\lambda')\cong\Psi^\varepsilon(\lambda\lambda')\), and this correspondence is not isomorphic to \(\Psi(\lambda\lambda')\).

*Reference:* [Connes–Consani 2016b, Theorem 7.7]. There the correspondence \(\Psi^\varepsilon(\kappa)\) is written \(\operatorname{id}_\varepsilon\circ\Psi(\kappa)\), with \(\operatorname{id}_\varepsilon=\Psi^\varepsilon(1)\). Exercise 6 shows that \(\Psi^\varepsilon(1)\circ\Psi(\kappa)\cong\Psi^\varepsilon(\kappa)\), so the two notations agree.

**Proof.** If \(\lambda\) is rational, Theorem 6.4 gives \(\Psi(\lambda\lambda')\). This covers the case where both parameters are rational, and the case where \(\lambda\) is rational and \(\lambda'\) is irrational, in which \(\lambda\lambda'\) is irrational. Let \(\lambda\) be irrational. If \(\lambda\lambda'\notin\mathbb Q\lambda'+\mathbb Q\), Theorem 6.4 gives \(\Psi(\lambda\lambda')\), and here \(\lambda\lambda'\) is irrational. If \(\lambda\lambda'\in\mathbb Q\lambda'+\mathbb Q\), then \(\lambda'\) is irrational and Theorem 6.7 gives \(\Psi^\varepsilon(\lambda\lambda')\). By the remarks after Definition 6.6, \(\Psi^\varepsilon(\lambda\lambda')\) is isomorphic to \(\Psi(\lambda\lambda')\) if \(\lambda\lambda'\) is irrational, and it is not if \(\lambda\lambda'\) is rational.

These cases are all the cases. If \(\lambda\lambda'\) is irrational, each of them gives \(\Psi(\lambda\lambda')\). If \(\lambda\lambda'\) is rational, then \(\lambda\) and \(\lambda'\) are both rational or both irrational. In the first case the composite is \(\Psi(\lambda\lambda')\). In the second case \(\lambda\lambda'\in\mathbb Q\lambda'+\mathbb Q\), and the composite is \(\Psi^\varepsilon(\lambda\lambda')\). \(\square\)

**Remark 6.9 (supporting lines and faces).** By Proposition 5.13, \(\Psi(\kappa)\) and \(\Psi^\varepsilon(\kappa)\) are quotients of \(\operatorname{Conv}(\mathbb N\times\mathbb N)\). Let \(E=\bigcup_i\langle a_i,b_i\rangle\subseteq\mathbb N\times\mathbb N\) be non-empty, and let \(c=\mathcal F_\kappa(E)\). The quotient map to \(R(\kappa)\) sends \(\operatorname{New}(E)\) to \(c\) (Proposition 5.14). The quotient map to \(R^\varepsilon(\kappa)\) sends \(\langle a,b\rangle\) to \(u_\kappa^aw^b=(\kappa a+b,a,a)\). So it sends \(\operatorname{New}(E)\) to \((c,s,t)\), where \(s\) and \(t\) are the least and the greatest \(a_i\) among the corners with \(\kappa a_i+b_i=c\). By (N1), the set of points of \(\operatorname{New}(E)\) where \(L_\kappa\) takes its minimum \(c\) is the segment from \((s,c-\kappa s)\) to \((t,c-\kappa t)\). This segment is the *face* of the Newton polygon in the direction \((\kappa,1)\). Hence:

- \(\Psi(\kappa)\) identifies two Newton polygons when they have the same supporting line of slope \(-\kappa\);
- \(\Psi^\varepsilon(\kappa)\) identifies them when they have the same face on that line.

For irrational \(\kappa\), a line of slope \(-\kappa\) contains at most one point of \(\mathbb Z^2\). So the face is a single corner, and it is determined by the line. This is why \(\Psi^\varepsilon(\kappa)\cong\Psi(\kappa)\) in that case. For rational \(\kappa\) the face can be an edge, and \(\Psi^\varepsilon(\kappa)\) remembers it. In these terms Theorem 6.8 says that the composite of two Frobenius correspondences with irrational parameters remembers the face in the direction \((\lambda\lambda',1)\), and that the composite of two with rational parameters remembers only the supporting line.

**Example 6.10.** (a) By Theorem 6.4, \(\Psi(2)\circ\Psi(1/2)\cong\Psi(1)\) and \(\Psi(1/2)\circ\Psi(2)\cong\Psi(1)\). Consider the second composite. An amalgam \((T,f,g)\) of \((\Psi(1/2),\Psi(2))\) satisfies \(f(1)=g(2)\). With \(U=f(1/2)\) and \(W=g(1)\) this says \(U^2=W^2\). Lemma 6.1 gives \(U=W\), and this is why the composite is the identity correspondence. The step from \(U^2=W^2\) to \(U=W\) uses that \(T\) is multiplicatively cancellative. This is the role of the reduction.

(b) For \(\lambda=\sqrt2\) and \(\lambda'=1/\sqrt2\), Theorem 6.8 gives \(\Psi(\sqrt2)\circ\Psi(1/\sqrt2)\cong\Psi^\varepsilon(1)\), which is not the identity correspondence \(\Psi(1)\). So \(\Psi(1/\lambda)\) is not an inverse of \(\Psi(\lambda)\) when \(\lambda\) is irrational.

(c) Let \(\lambda=1+1/\pi\) and \(\lambda'=\pi\). Then \(\lambda\lambda'=\pi+1\) lies in \(\mathbb Q\lambda'+\mathbb Q\), so Theorem 6.7 applies: the universal amalgam is the semiring \(T_\varepsilon\) with three generators, and the composite is \(\Psi^\varepsilon(\pi+1)\cong\Psi(\pi+1)\). In the other order, \(\lambda=\pi\) and \(\lambda'=1+1/\pi\), the product \(\pi+1\) does not lie in \(\mathbb Q\lambda'+\mathbb Q=\mathbb Q+\mathbb Q\pi^{-1}\), because \(\pi\) is not a root of a quadratic polynomial with rational coefficients. So Theorem 6.4 applies, and the universal amalgam is a sub-semiring of \(\mathbb R_{\min}\). Both composites are isomorphic to \(\Psi(\pi+1)\).

## 7. Exercises

**Exercise 1 (sets with one endomorphism).** Let \(T=\{t^n:n\in\mathbb N\}\) be the free monoid on one generator \(t\). A \(T\)-set is a set \(A\) with a map \(\tau:A\to A\), the action of \(t\).

(a) Show that, up to isomorphism, the flat \(T\)-sets are \(\mathbb N\) and \(\mathbb Z\), with \(\tau(n)=n+1\). So the topos of \(T\)-sets has exactly two isomorphism classes of points.

(b) Find all equivariant maps between these two \(T\)-sets.

(c) Show that the stalk of a \(T\)-set \(A\) at the point \(\mathbb Z\) is the colimit of the sequence \(A\to A\to A\to\cdots\) in which every map is \(\tau\). Compute it for \(A=\mathbb N\), and for a non-empty set \(A\) on which \(\tau\) is constant.

*Solution.* (a) \(T\) is cancellative, and its group of fractions is \(\{t^n:n\in\mathbb Z\}\), which we identify with \((\mathbb Z,+)\). In additive notation, a directed \(T\)-subset is a non-empty \(P\subseteq\mathbb Z\) with \(P+1\subseteq P\), such that any two \(p,p'\in P\) lie in \(c+\mathbb N\) for some \(c\in P\). The last condition always holds with \(c=\min(p,p')\). So \(P=\mathbb Z\), or \(P=\{n:n\geq n_0\}\) for some \(n_0\). By Proposition 2.1 these are the flat \(T\)-sets, up to isomorphism. The translation by \(-n_0\) is an isomorphism from \(\{n\geq n_0\}\) to \(\mathbb N\). The \(T\)-sets \(\mathbb N\) and \(\mathbb Z\) are not isomorphic, since \(\tau\) is surjective on \(\mathbb Z\) and not on \(\mathbb N\).

(b) By Proposition 2.1(3), the equivariant maps \(P\to P'\) are the translations \(n\mapsto n+\gamma\) with \(\gamma\in\mathbb Z\) and \(\gamma+P\subseteq P'\). So the maps \(\mathbb N\to\mathbb N\) are the translations by \(\gamma\geq0\); the maps \(\mathbb N\to\mathbb Z\) and \(\mathbb Z\to\mathbb Z\) are all translations; and there is no map \(\mathbb Z\to\mathbb N\).

(c) The colimit \(L\) of the sequence is the set of pairs \((i,a)\in\mathbb N\times A\) modulo the equivalence relation generated by \((i,a)\sim(i+1,\tau a)\). The stalk is \(\mathbb Z\otimes_TA\), the set of pairs \((n,a)\in\mathbb Z\times A\) modulo the relation generated by \((n+1,a)\sim(n,\tau a)\). The map \((i,a)\mapsto[-i,a]\) respects the relations, since \([-i,a]=[-i-1,\tau a]\). It is surjective, since \([n,a]=[0,\tau^na]\) for \(n\geq0\). It is injective. By Lemma 1.7, \([-i,a]=[-j,b]\) means that there are \(z\in\mathbb Z\) and \(k,k'\in\mathbb N\) with \(z+k=-i\), \(z+k'=-j\) and \(\tau^ka=\tau^{k'}b\). Then, in \(L\), \((i,a)\sim(i+k,\tau^ka)=(-z,\tau^{k'}b)=(j+k',\tau^{k'}b)\sim(j,b)\).

For \(A=\mathbb N\), the map \((i,a)\mapsto a-i\) is a bijection \(L\to\mathbb Z\), in agreement with \(\mathbb Z\otimes_TT\cong\mathbb Z\). If \(\tau\) is constant with value \(a_0\), then \((i,a)\sim(i+1,a_0)\) for all \(a\), and \((i,a_0)\sim(i+1,a_0)\). So all elements of \(L\) are equivalent, and the stalk is one point. The stalk at the point \(\mathbb Z\) sees only the eventual behaviour of \(\tau\), while the stalk at the point \(\mathbb N\) is \(A\) itself.

**Exercise 2 (a stalk computation).** Let \(n\geq1\), and let \(A_n=\mathbb Z/n\mathbb Z\) with \(k\in\mathbb N^\times\) acting by multiplication by \(k\).

(a) Show that \([y,a]\mapsto ay+nH\) is a bijection from the stalk \(p_H^{\ast}(A_n)\) to \(H/nH\).

(b) Compute the stalk for \(H=\mathbb Z\), for \(H=\mathbb Q\) and for \(H=\mathbb Z[1/p]\).

*Solution.* (a) The map is well defined: \(ay+nH\) depends only on \(a\) modulo \(n\), and \([ky,a]\) and \([y,ka]\) both go to \(kay+nH\). It is surjective. Let \(h\in H\). The group generated by \(h\) and by some element of \(H_{>0}\) is cyclic, with a generator \(y>0\). Then \(h=ay\) with \(a\in\mathbb Z\), and \(h+nH\) is the image of \([y,a]\). It is injective. Let \(ay-a'y'=nh\) with \(h\in H\). Let \(z>0\) be a generator of the cyclic group \(\mathbb Zy+\mathbb Zy'+\mathbb Zh\). Then \(y=kz\), \(y'=k'z\) and \(h=dz\) with \(k,k'\in\mathbb N^\times\) and \(d\in\mathbb Z\), and \((ak-a'k')z=ndz\). So \(ka\equiv k'a'\) modulo \(n\), and \([y,a]=[z,ka]=[z,k'a']=[y',a']\).

(b) For \(H=\mathbb Z\) the stalk is \(\mathbb Z/n\mathbb Z\). For \(H=\mathbb Q\) we have \(n\mathbb Q=\mathbb Q\), and the stalk is one point. Let \(H=\mathbb Z[1/p]\), and write \(n=p^en'\) with \(p\nmid n'\). Since \(p\) is invertible in \(H\), \(nH=n'H\). The map \(\mathbb Z\to H/n'H\) is surjective: for \(x=c/p^j\in H\) choose integers \(s,t\) with \(sp^j+tn'=1\); then \(x=cs+n'(ct/p^j)\) is congruent to \(cs\). Its kernel is \(\mathbb Z\cap n'H=n'\mathbb Z\): if \(m=n'c/p^j\), then \(p^jm=n'c\), so \(n'\) divides \(m\). Hence the stalk is \(\mathbb Z/n'\mathbb Z\). The stalk at \(p_{\mathbb Z[1/p]}\) forgets the \(p\)-part of \(n\).

**Exercise 3 (adjoining zero).** Let \(\mathbb N_0^\times=\mathbb N^\times\cup\{0\}\) be the multiplicative monoid of all non-negative integers. In the convention of the other lessons it is the monoid with zero that belongs to \(\mathbb N^\times\).

(a) Show that the flat \(\mathbb N_0^\times\)-sets are, up to isomorphism, the sets \(H_{\geq0}=\{h\in H:h\geq0\}\) for the subgroups \(H\subseteq\mathbb Q\), the subgroup \(H=0\) included.

(b) Show that the equivariant maps \(H_{\geq0}\to H'_{\geq0}\) are the maps \(x\mapsto rx\) with \(r\in\mathbb Q\), \(r\geq0\) and \(rH\subseteq H'\). Conclude that the category of points of \(\widehat{\mathbb N_0^\times}\) is obtained from that of \(\widehat{\mathbb N^\times}\) by adding the zero maps and one object that is both initial and terminal.

(c) Let \(0\in\mathbb N_0^\times\) act on \(\mathbb Z_{\max}\) by \(n\mapsto0\) for \(n\in\mathbb Z\) and \(-\infty\mapsto-\infty\). Show that this is a semiring endomorphism and that the stalk of \(\mathbb Z_{\max}\) at the new point is \(\mathbb B\).

*Solution.* (a) \(\mathbb N_0^\times\) is not cancellative, so we use Theorem 1.8 directly. Let \(X\) be flat and let \(\omega:X\to X\) be the action of \(0\). For \(x,x'\in X\) choose \(z,k,k'\) with \(kz=x\) and \(k'z=x'\). Then \(\omega(x)=(0\cdot k)z=\omega(z)=\omega(x')\). So \(\omega\) is constant. Let \(0_X\) be its value. Then \(n0_X=n\omega(x)=\omega(x)=0_X\) for all \(n\).

If \(nx=0_X\) with \(n\geq1\), then \(x=0_X\). Indeed \(nx=0_X=0x\), so by (F3) there are \(z,w\) with \(wz=x\) and \(nw=0w=0\). Then \(w=0\) and \(x=\omega(z)=0_X\). Hence \(X^{\ast}=X\setminus\{0_X\}\) is stable under \(\mathbb N^\times\). If \(X^{\ast}=\emptyset\), then \(X=\{0_X\}=H_{\geq0}\) for \(H=0\). Otherwise \(X^{\ast}\) is a flat \(\mathbb N^\times\)-set. For (F2), let \(x,x'\in X^{\ast}\) and take \(z,k,k'\) as in (F2) for \(X\); then \(k,k'\neq0\) and \(z\neq0_X\), because \(x,x'\neq0_X\). For (F3'), let \(kx=k'x\) with \(k,k'\in\mathbb N^\times\) and \(x\in X^{\ast}\). By (F3) for \(X\) there are \(z,w\) with \(wz=x\) and \(kw=k'w\). Here \(w\neq0\), since \(x\neq0_X\), so \(k=k'\). By Theorem 2.2, \(X^{\ast}\cong H_{>0}\) for a non-zero subgroup \(H\), and then \(X\cong H_{\geq0}\), with \(0_X\mapsto0\).

Conversely \(H_{\geq0}\) is flat. (F1) is clear. For (F2): if \(x,x'>0\) use Theorem 2.2; if \(x=0\) take \(z=x'\), \(k=0\), \(k'=1\). For (F3), let \(kx=k'x\). If \(x>0\), then \(k=k'\); take \(z=x\) and \(w=1\). If \(x=0\), take \(z=0\) and \(w=0\).

(b) Let \(f:H_{\geq0}\to H'_{\geq0}\) be equivariant. Then \(f(0)=f(0\cdot0)=0\cdot f(0)=0\). Suppose \(f(x)=0\) for some \(x>0\). For \(y>0\) choose \(z>0\) and \(k,k'\geq1\) with \(kz=x\) and \(k'z=y\). Then \(kf(z)=0\), so \(f(z)=0\) and \(f(y)=k'f(z)=0\). So \(f=0\), the map with \(r=0\). Otherwise \(f\) maps \(H_{>0}\) to \(H'_{>0}\) equivariantly, and \(f(x)=rx\) with \(r>0\) by Theorem 2.2(3). Conversely all these maps are equivariant. For \(H=0\), there is exactly one equivariant map from \(\{0\}\) to any \(H'_{\geq0}\), and exactly one from any \(H_{\geq0}\) to \(\{0\}\). So the point \(\{0\}\) is initial and terminal.

(c) The map \(\operatorname{Fr}_0\) preserves \(\max\) and \(+\): for integers both sides are \(0\), and if one argument is \(-\infty\) one checks \(\max(a,-\infty)=a\mapsto0=\max(0,-\infty)\) and \(a+(-\infty)=-\infty\mapsto-\infty\). The stalk at the point \(\{0\}\) is the quotient of \(\mathbb Z_{\max}\) by the equivalence relation generated by \(x\sim kx\) for \(k\in\mathbb N_0^\times\). For \(n\in\mathbb Z\) this gives \(n\sim0\cdot n=0\), and \(-\infty\) is equivalent only to itself. So the stalk has two elements, the classes of \(0\) and of \(-\infty\), and it is \(\mathbb B\).

These are the statements of [Connes–Consani 2016b, Theorem 2.4 and Remark 3.3].

**Exercise 4 (other value semifields).**

(a) Show that the classes of non-degenerate points of the arithmetic site over \(\mathbb Z_{\max}\) correspond to the positive integers, and that the endomorphism \(\operatorname{Fr}_k\) of \(\mathbb Z_{\max}\) acts on them by \(n\mapsto kn\).

(b) Show that the classes of non-degenerate points over \(\mathbb Q_{\max}\) correspond to the non-zero subgroups of \(\mathbb Q\), hence to \(\mathbb A^f/\widehat{\mathbb Z}^\times\).

(c) The inclusion \(\mathbb Q_{\max}\subseteq\mathbb R_{\max}\) induces a map \(\mathcal P(\mathbb Q)\to\mathcal P(\mathbb R)\). Show that it is injective and that, under the bijection \(\Theta\) of Theorem 4.6, its image is the set of classes \([a,x]\) with \(x\in\mathbb Q\).

*Solution.* (a) By Theorem 4.3(4) with \(G=\mathbb Z\), the classes correspond to the rank-one subgroups of \(\mathbb Z\). These are the subgroups \(n\mathbb Z\) with \(n\geq1\). If \((p_H,f)\) has \(f_0(H)=n\mathbb Z\), then \(\operatorname{Fr}_k\circ f\) has the subgroup \(kn\mathbb Z\). Here \(H\cong\mathbb Z\), so all these points lie over the point \(p_{\mathbb Z}\) of the topos.

(b) Every non-zero subgroup of \(\mathbb Q\) has rank one. Apply Theorem 4.3(4) and Proposition 2.4(1).

(c) On degenerate points the map is the identity of the set of isomorphism classes of points of the topos, by Theorem 4.3(3). On non-degenerate points it sends a rank-one subgroup \(L\subseteq\mathbb Q\) to the same subgroup of \(\mathbb R\). So it is injective. A rank-one subgroup \(\lambda H\) of \(\mathbb R\), with \(H\subseteq\mathbb Q\) and \(\lambda>0\), is contained in \(\mathbb Q\) if and only if \(\lambda\in\mathbb Q\). The class \([a,x]\) with \(x\neq0\) corresponds to \(|x|H_a\). So the image consists of the classes \([a,x]\) with \(x\in\mathbb Q\).

**Exercise 5 (the semirings \(R(\lambda)\)).** Show that for real numbers \(\lambda,\lambda'>0\) the semirings \(R(\lambda)\) and \(R(\lambda')\) are isomorphic if and only if \(\lambda'\in\{\lambda,1/\lambda\}\), or both \(\lambda\) and \(\lambda'\) lie in \(\{k,1/k:k\in\mathbb N^\times\}\). Compare with Proposition 5.14.

*Solution.* An isomorphism of semirings \(\theta:R(\lambda)\to R(\lambda')\) maps \(\infty\) to \(\infty\). On the finite elements it is a bijection that is additive for the addition of real numbers and preserves their order, because \(\theta\) preserves the semiring product and \(\min\).

The conditions are sufficient. Multiplication by \(1/\lambda\) is an isomorphism \(R(\lambda)\to R(1/\lambda)\), and \(R(k)=\mathbb N_{\min}\) for \(k\in\mathbb N^\times\).

They are necessary. *Case 1: \(\lambda\) and \(\lambda'\) are irrational.* The monoid \(\mathbb N+\lambda\mathbb N\) is free on \(1\) and \(\lambda\), and these are its only non-zero elements that are not sums of two non-zero elements. So \(\theta\) maps \(\{1,\lambda\}\) onto \(\{1,\lambda'\}\). If \(\theta(1)=1\) and \(\theta(\lambda)=\lambda'\), then \(a\lambda\leq b\) if and only if \(a\lambda'\leq b\), for all \(a,b\in\mathbb N\), and \(\lambda=\lambda'\) as in Proposition 5.14. If \(\theta(1)=\lambda'\) and \(\theta(\lambda)=1\), then \(a\lambda\leq b\) if and only if \(a\leq b\lambda'\), and \(\lambda=1/\lambda'\).

*Case 2: one parameter is irrational and the other is rational.* If \(\lambda'\) is rational, any two non-zero finite elements \(x,y\) of \(R(\lambda')\) satisfy \(ax=by\) for some positive integers \(a,b\). In \(R(\lambda)\) with \(\lambda\) irrational, the elements \(1\) and \(\lambda\) do not. So there is no isomorphism.

*Case 3: \(\lambda=n/m\) and \(\lambda'=n'/m'\) in lowest terms.* Multiplication by \(m\) is an isomorphism from \(R(\lambda)\) onto \(S_{\min}\), where \(S=m\mathbb N+n\mathbb N\subseteq\mathbb N\). The set \(S\) contains all large integers, because \(m\) and \(n\) are coprime. Define \(S'\) in the same way. An isomorphism \(S_{\min}\to S'_{\min}\) restricts to an additive bijection \(\theta:S\to S'\). For non-zero \(s,t\in S\), the integer \(st\) is the sum of \(s\) copies of \(t\) and also of \(t\) copies of \(s\). So \(s\theta(t)=\theta(st)=t\theta(s)\). Hence \(\theta(t)=ct\) for a constant \(c\in\mathbb Q_{>0}\), and \(cS=S'\). For large \(x\), both \(x\) and \(x+1\) are in \(S\), so \(c=c(x+1)-cx\) is an integer. By symmetry \(1/c\) is an integer. So \(c=1\) and \(S=S'\). If \(1\in S\), that is, if \(m=1\) or \(n=1\), then \(S=\mathbb N=S'\), so \(m'=1\) or \(n'=1\), and both parameters lie in \(\{k,1/k\}\). Otherwise \(m,n\geq2\) and \(m\neq n\). The least non-zero element of \(S\) is \(\min(m,n)\), and the least element of \(S\) that is not divisible by it is \(\max(m,n)\). So \(S=S'\) gives \(\{m,n\}=\{m',n'\}\), that is, \(\lambda'\in\{\lambda,1/\lambda\}\).

Comparison: the semiring \(R(\lambda)\) alone does not determine \(\lambda\). The semiring together with the two morphisms \(\ell_\lambda\) and \(r_\lambda\) does, by Proposition 5.14.

*Reference:* [Connes–Consani 2016b, Propositions 6.12(ii) and 6.13(iii)] treat the parameters \(n/m\) with coprime \(n,m\geq2\) and the irrational parameters. [Connes–Consani 2014, Proposition 3.4(iii)] states the criterion \(\lambda'\in\{\lambda,1/\lambda\}\) for all positive real parameters; this condition is not necessary when both parameters are integers or inverses of integers, for example \(R(2)=R(3)=\mathbb N_{\min}\), so we prove the statement above.

**Exercise 6 (the tangential deformation of the identity).** Let \(\kappa>0\) be a real number. Show that the pair \((\Psi^\varepsilon(1),\Psi(\kappa))\) has a universal amalgam and that \(\Psi^\varepsilon(1)\circ\Psi(\kappa)=\Psi^\varepsilon(\kappa)\).

*Solution.* Write \(u=u_1=(1,1,1)\) and \(w=(1,0,0)\) for the generators of \(R^\varepsilon(1)\). So \(\ell^\varepsilon_1(1)=u\) and \(r^\varepsilon(1)=w\). By the description after Definition 6.6, the elements of \(R^\varepsilon(1)\) are \(\infty\) and the triples \((c,s,t)\) of integers with \(0\leq s\leq t\leq c\).

*The amalgam.* Let \(f_0:R^\varepsilon(1)\to\mathbb T\), \(f_0(c,s,t)=(\kappa c,s,t)\), and \(g_0:R(\kappa)\to\mathbb T\), \(g_0(b)=(b,0,0)\), with \(\infty\mapsto\infty\). Both are morphisms of semirings, and \(f_0(r^\varepsilon(n))=(\kappa n,0,0)=g_0(\ell_\kappa(n))\). Let \(T_0\) be the sub-semiring of \(\mathbb T\) generated by the two images. It is generated by \(f_0(u)=(\kappa,1,1)=u_\kappa\) and by the elements \(g_0(b)\), since \(f_0(w)=g_0(\kappa)\). Its monomials are \(u_\kappa^xg_0(b)=(\kappa x+b,x,x)\) with \(x\in\mathbb N\) and \(b\in\mathbb N+\kappa\mathbb N\). So \(T_0\) consists of \(\infty\) and of the triples \((c,s,t)\) with \(c\in\mathbb N+\kappa\mathbb N\) and \(s\leq t\) in \(Y(c)=\{x\in\mathbb N:c-\kappa x\in\mathbb N+\kappa\mathbb N\}\).

*Universality.* Let \((T,f,g)\) be an amalgam, so \(f(w)=g(\kappa)\). Put \(U=f(u)\), and \(M(x,b)=U^xg(b)\) for \(x\in\mathbb N\) and finite \(b\in R(\kappa)\). Then \(M(x+x',b+b')=M(x,b)M(x',b')\).

Step 1. If \(\kappa x+b<\kappa x'+b'\), then \(M(x,b)\) absorbs \(M(x',b')\). Let \(\delta\) be the difference of the two numbers, and let \(N\geq1\) be an integer with \(N\delta>2\kappa\). Put \(k=Nx+1\), and \(k'=Nx'-1\) if \(x'\geq1\), \(k'=0\) if \(x'=0\). In \(R^\varepsilon(1)\), \(u^{Nx}=(Nx,Nx,Nx)\) absorbs \(w^k=(k,0,0)\), because \(Nx< k\). Applying \(f\), \(U^{Nx}\) absorbs \(g(\kappa)^k=g(\kappa k)\), and \(M(x,b)^N\) absorbs \(g(\kappa k+Nb)\). In \(R^\varepsilon(1)\), \(w^{k'}\) absorbs \(u^{Nx'}\); for \(x'=0\) both are the unit. So \(g(\kappa k'+Nb')\) absorbs \(M(x',b')^N\). Finally
\[
\kappa k+Nb=N(\kappa x+b)+\kappa< N(\kappa x'+b')-\kappa\leq\kappa k'+Nb',
\]
so \(g(\kappa k+Nb)\) absorbs \(g(\kappa k'+Nb')\). By transitivity \(M(x,b)^N\) absorbs \(M(x',b')^N\), and by Lemma 6.1 \(M(x,b)\) absorbs \(M(x',b')\).

Step 2. Let \(c\in\mathbb N+\kappa\mathbb N\) and \(i\leq k\leq j\) in \(Y(c)\). In \(\mathbb N\times(\mathbb N+\kappa\mathbb N)\),
\[
(j-i)\,(k,c-\kappa k)=(j-k)\,(i,c-\kappa i)+(k-i)\,(j,c-\kappa j).
\]
As in Step 2 of the proof of Theorem 6.7, it follows that \(M(i,c-\kappa i)\oplus M(j,c-\kappa j)\) absorbs \(M(k,c-\kappa k)\).

Step 3. Define \(\rho(c,s,t)=M(s,c-\kappa s)\oplus M(t,c-\kappa t)\) and \(\rho(\infty)=0\). As in Step 3 of the proof of Theorem 6.7, \(\rho\) is a morphism of semirings \(T_0\to T\). It sends \(u_\kappa=(\kappa,1,1)\) to \(M(1,0)=U=f(u)\), and \(g_0(b)=(b,0,0)\) to \(M(0,b)=g(b)\). So \(\rho\circ g_0=g\). Also \(\rho(f_0(w))=\rho(g_0(\kappa))=g(\kappa)=f(w)\). So \(\rho\circ f_0\) and \(f\) agree on the generators \(u\) and \(w\) of \(R^\varepsilon(1)\), and \(\rho\circ f_0=f\). The morphism \(\rho\) is unique, because \(T_0\) is generated by the images of \(f_0\) and \(g_0\).

*The composite.* The elements \(f_0(\ell^\varepsilon_1(1))=u_\kappa\) and \(g_0(r_\kappa(1))=w\) generate \(R^\varepsilon(\kappa)\) inside \(T_0\), and \(f_0\circ\ell^\varepsilon_1=\ell^\varepsilon_\kappa\), \(g_0\circ r_\kappa=r^\varepsilon\). So \(\Psi^\varepsilon(1)\circ\Psi(\kappa)=\Psi^\varepsilon(\kappa)\). For irrational \(\kappa\) this is isomorphic to \(\Psi(\kappa)\). For rational \(\kappa\) it is the statement of [Connes–Consani 2016b, Lemma 7.8] together with the paragraph that follows it.

## What this lesson does not prove

- The statements of topos theory for an arbitrary small category \(\mathcal D\): that the points of the topos of presheaves on \(\mathcal D\) correspond to the flat functors, and that a functor to sets is flat if and only if it satisfies the three filtering conditions; both statements are in [Connes–Consani 2017, Section 3.1]. This lesson proves the case of a commutative monoid (Proposition 1.6 and Theorem 1.8), which is all it uses. The general case is Theorem 4.1 of the later lesson *The scaling site*, applied to the covering families that consist of a single isomorphism: for them every presheaf is a sheaf ([Sites and sheaves](course:ag-etale-cohomology/sites-and-sheaves#1-local-data-and-their-agreement), course on étale cohomology), so the presheaves form a topos [Leinster 2010, Examples 1.6(iv)], and the stalk functor of that theorem is the tensor product with the functor. So a functor is flat exactly when it satisfies the filtering conditions: if it is flat, the tensor product and its right adjoint form a point, whose functor is the given one; if it satisfies the conditions, the stalk functor preserves finite limits.
- Two facts of category theory: a left adjoint preserves colimits [Stacks, Tag [0038](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-adjoint-exact)], and a functor on a category with finite limits preserves finite limits if it preserves the terminal object, binary products and equalizers [Stacks, Tag [0035](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-characterize-left-exact)].
- The relation with the zeta function. [Connes–Consani 2016b, Theorem 4.2] states that the counting distribution of the action of the Frobenius automorphisms on \(\mathcal P(\mathbb R)=\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^\times\), which is defined in Section 4.2 of that paper through a trace formula, has the completed Riemann zeta function as its Hasse–Weil zeta function. It recalls this from [Connes–Consani 2010] and [Connes–Consani 2010b]. The lesson *Weil's proof for curves and what is missing over the integers* treats that counting function.
- The relation with \(\operatorname{Spec}\mathbb Z\). [Connes–Consani 2016b, Theorem 5.3] constructs a geometric morphism from the topos of sheaves on \(\operatorname{Spec}\mathbb Z\) to \(\widehat{\mathbb N_0^\times}\) that sends the prime \(p\) to the point given by the group \(\mathbb Z[1/p]\). Exercise 3 describes the points of \(\widehat{\mathbb N_0^\times}\).
- The existence of a composite for two arbitrary correspondences. Definition 6.2 defines the composite when a universal amalgam exists. The lesson proves the existence for the pairs \((\Psi(\lambda),\Psi(\lambda'))\) and, in Exercise 6, for the pairs \((\Psi^\varepsilon(1),\Psi(\kappa))\).

## References

- [Connes–Consani 2016b] A. Connes, C. Consani, *Geometry of the arithmetic site*, arXiv:1502.05580. Free at https://alainconnes.org/wp-content/uploads/arithmeticsite.pdf
- [Connes–Consani 2014] A. Connes, C. Consani, *The arithmetic site*, arXiv:1405.4527. Free at https://alainconnes.org/wp-content/uploads/The-arithmetic-site-2014.pdf
- [Connes–Consani 2017] A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191. Free at https://alainconnes.org/wp-content/uploads/scalingsite.pdf
- [Connes–Consani 2010] A. Connes, C. Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024. Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Connes–Consani 2010b] A. Connes, C. Consani, *From monoids to hyperstructures: in search of an absolute arithmetic*, arXiv:1006.4810. Free at https://alainconnes.org/wp-content/uploads/From-monoids-to-hyperstructures-2010.pdf
- [Connes 2011] A. Connes, *The Witt construction in characteristic one and quantization*, arXiv:1009.1769. Free at https://alainconnes.org/wp-content/uploads/Wittcar1.pdf
- [Leinster 2010] T. Leinster, *An informal introduction to topos theory*, [arXiv:1012.5647](https://arxiv.org/pdf/1012.5647).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tag 0038 carries such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
