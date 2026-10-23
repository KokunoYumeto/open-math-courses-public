# Giraud's characterization of topoi

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A topos is a category equivalent to the category of sheaves on a small site. Giraud showed that topoi can be recognized without a site: a locally small category is a topos exactly when it has finite limits, small coproducts that are disjoint and stable under pullback, quotients of equivalence relations that are effective and stable under pullback, and a small set of generators. The site is then a small full subcategory that contains the generators and is closed under fibre products, with the families that are epimorphic in the category as coverings. Every object is recovered as the sheaf of its points with values in that subcategory.

Categories built from topoi by limits and colimits, such as the second total category of a fibred topos and the category of equivariant sheaves on a pseudo-category, have these properties for formal reasons, while a site for them is hard to write down in general. The theorem shows that they are topoi.

**Prerequisites.** Sites, sheaves and sheafification in the sense of the AI-integrated Stacks project [[Stacks, Tag 00VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-definition-site), [Tag 00VL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-section-sheaves), [Tag 00WH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-sheafification-adjoint), [Tag 00WJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-sheafification-exact)], with limits and colimits of sheaves [[Tag 00W2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-limit-sheaf), [Tag 00WI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-colimit-sheaves)]; [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Definition 2.1, Propositions 2.2 and 3.1, Lemma 4.1, Theorems 4.2 and 4.3); [*Equivariant sheaves on simplicial topoi*](equivariant-sheaves-on-simplicial-topoi.md) (Definition 3.2, Propositions 2.2 and 6.3, Remark 6.4); [*Cohomology of the second total topos and local systems*](cohomology-of-the-second-total-topos-and-local-systems.md) (its standing hypotheses).

## Conventions

Categories are locally small. A family of morphisms \(f_a\colon Y_a\to X\) is *epimorphic* if two morphisms \(g,h\colon X\to Z\) with \(gf_a=hf_a\) for every \(a\) are equal. For an object \(T\), a *\(T\)-point* of \(X\) is a morphism \(T\to X\); a \(T\)-point of a fibre product is a pair of \(T\)-points with the same image. A *subobject* of \(X\) is a monomorphism \(j\colon Z\to X\); a morphism \(g\) into \(X\) *factors through* it if \(g=jh\) for some \(h\), which is then unique.

A *relation* on \(Y\) is a subobject \((r_1,r_2)\colon R\to Y\times Y\). It is an *equivalence relation* if, for every object \(T\), the pairs \((r_1x,r_2x)\), \(x\) a \(T\)-point of \(R\), form an equivalence relation on the set of \(T\)-points of \(Y\). By the Yoneda lemma this means that the diagonal of \(Y\) factors through \(R\), that the exchange of the factors of \(Y\times Y\) carries \(R\) into \(R\), and that the morphism \(R\times_YR\to Y\times Y\) given by the outer projections factors through \(R\); here \(R\times_YR\) is formed with \(r_2\) and \(r_1\). The *kernel pair* of a morphism \(f\colon Y\to X\) is \(Y\times_XY\) with its two projections; it is an equivalence relation on \(Y\). The coproduct of the empty family is an initial object \(0\).

**Definition 1.1.** A category \(\mathcal E\) satisfies *Giraud's conditions* if:

- (G1) \(\mathcal E\) has finite limits.
- (G2) \(\mathcal E\) has small coproducts, and they are disjoint and stable under pullback. That is, for a small family \((Y_a)\) with coproduct \(Y=\coprod_aY_a\) and inclusions \(\iota_a\), every \(\iota_a\) is a monomorphism, \(Y_a\times_YY_b=0\) for \(a\neq b\), and for every morphism \(g\colon X\to Y\) the projections \(Y_a\times_YX\to X\) exhibit \(X\) as the coproduct of the \(Y_a\times_YX\). This includes the empty family.
- (G3) Every equivalence relation \(R\) on an object \(Y\) has a coequalizer \(q\colon Y\to Q\) of \(r_1\) and \(r_2\), and \(R\) is the kernel pair of \(q\). These coequalizers are stable under pullback: for every morphism \(Q'\to Q\), the morphism \(Y\times_QQ'\to Q'\) is the coequalizer of the two morphisms \(R\times_QQ'\rightrightarrows Y\times_QQ'\) induced by \(r_1\) and \(r_2\).
- (G4) There is a small set \(G\) of objects such that, for every object \(Y\), the family of all morphisms from objects of \(G\) to \(Y\) is epimorphic.

## 1. Consequences of the conditions

In this section \(\mathcal E\) satisfies (G1)–(G3).

**Lemma 1.2.**

1. Every morphism \(X\to0\) is an isomorphism.
2. Let \(j_a\colon A_a\to Z\) be a small family of subobjects with \(A_a\times_ZA_b=0\) for \(a\neq b\). Then the morphism \(\coprod_aA_a\to Z\) induced by the \(j_a\) is a monomorphism.
3. A family \(f_a\colon Y_a\to X\) is epimorphic if and only if \(\coprod_aY_a\to X\) is an epimorphism. A coproduct of epimorphisms is an epimorphism.

**Proof.** (1) Let \(f\colon X\to0\). By (G2) for the empty family, the empty family of pullbacks exhibits \(X\) as a coproduct, so \(X\) is initial, and \(f\) is a morphism between initial objects.

(2) Put \(A=\coprod_aA_a\) and let \(j\colon A\to Z\) be the induced morphism. Applying (G2) to the two projections of \(A\times_ZA\), this object is the coproduct of the \(A_a\times_ZA_b\). These are initial for \(a\neq b\), and \(A_a\times_ZA_a=A_a\), with both projections the identity, since \(j_a\) is a monomorphism. So the two projections \(A\times_ZA\to A\) agree on every summand, hence are equal, and \(j\) is a monomorphism.

(3) A morphism out of \(\coprod_aY_a\) is the family of its restrictions to the summands, which gives the first statement. If every \(f_a\colon Y_a\to X_a\) is an epimorphism and \(g,h\colon\coprod_aX_a\to Z\) agree after \(\coprod_af_a\), then \(g\iota_af_a=h\iota_af_a\), so \(g\iota_a=h\iota_a\) for every \(a\), and \(g=h\). \(\square\)

**Lemma 1.3 (images).** Let \(f\colon Y\to X\) be a morphism with kernel pair \(R\), let \(q\colon Y\to Q\) be the coequalizer of \(R\), which exists by (G3), and let \(m\colon Q\to X\) be the morphism with \(f=mq\). Then \(q\) is an epimorphism and \(m\) is a monomorphism.

**Proof.** A coequalizer is an epimorphism. The morphism \(q\times q\colon Y\times_XY\to Q\times_XQ\) is the composite of \(Y\times_XY\to Q\times_XY\) and \(Q\times_XY\to Q\times_XQ\). The first is the pullback of \(q\) along the projection \(Q\times_XY\to Q\), and the second the pullback of \(q\) along the second projection \(Q\times_XQ\to Q\). By (G3) the pullbacks of \(q\) are coequalizers, hence epimorphisms, so \(q\times q\) is an epimorphism. Let \(p_1,p_2\colon Q\times_XQ\to Q\) be the projections. Then \(p_k\circ(q\times q)=q\circ\mathrm{pr}_k\), and \(q\circ\mathrm{pr}_1=q\circ\mathrm{pr}_2\) on \(Y\times_XY=R\). Hence \(p_1=p_2\): the projections of the kernel pair of \(m\) are equal, and \(m\) is a monomorphism. \(\square\)

**Lemma 1.4.** A morphism that is both a monomorphism and an epimorphism is an isomorphism.

**Proof.** Let \(m\colon A\to X\) be a monomorphism and an epimorphism. Put \(Z=X\sqcup X\), with inclusions \(\iota_1,\iota_2\), which are monomorphisms with \(X\times_ZX=0\) over \(\iota_1\) and \(\iota_2\), by (G2). The four morphisms
\[
\begin{aligned}d_1&=(\iota_1,\iota_1)\colon X\to Z\times Z,\\ d_2&=(\iota_2,\iota_2)\colon X\to Z\times Z,\\ e_{12}&=(\iota_1m,\iota_2m)\colon A\to Z\times Z,\\ e_{21}&=(\iota_2m,\iota_1m)\colon A\to Z\times Z\end{aligned}
\]
are monomorphisms, because \(\iota_1\), \(\iota_2\) and \(m\) are. Any two of them have an initial fibre product. Indeed, for two different ones, the first coordinates or the second coordinates lie in different copies of \(X\), so a \(T\)-point of their fibre product gives a \(T\)-point of the initial object \(X\times_ZX\) over \(\iota_1\) and \(\iota_2\), and \(T\) is initial by Lemma 1.2 (1). By Lemma 1.2 (2), they define a relation \(R=X\sqcup X\sqcup A\sqcup A\to Z\times Z\).

It is an equivalence relation. The diagonal of \(Z\) is \(d_1\) on the first copy of \(X\) and \(d_2\) on the second, so it factors through \(R\). The exchange of the factors fixes \(d_1\) and \(d_2\) and exchanges \(e_{12}\) and \(e_{21}\). By (G2), \(R\times_ZR\) is the coproduct of the sixteen fibre products of the pieces, and on each of them the outer projections factor through \(R\). For instance, on the piece of \(d_1\) and \(e_{12}\), the points are the pairs \((x,a)\) with \(\iota_1x=\iota_1ma\), that is \(x=ma\), and the outer projections give \((\iota_1ma,\iota_2ma)\), a point of \(e_{12}\). On the piece of \(e_{12}\) and \(e_{21}\), the condition \(\iota_2ma=\iota_2ma'\) gives \(a=a'\), and the outer projections give \((\iota_1ma,\iota_1ma)\), a point of \(d_1\). The pieces of \(d_2\) and \(e_{21}\), of \(e_{12}\) and \(d_2\), of \(e_{21}\) and \(d_1\), of \(e_{21}\) and \(e_{12}\), and of \(d_k\) with itself are treated in the same way. The remaining pieces join different copies of \(X\), so they are initial.

By (G3), \(R\) is the kernel pair of its coequalizer \(c\colon Z\to P\). Since \(e_{12}\) factors through \(R\), \(c\iota_1m=c\iota_2m\), and since \(m\) is an epimorphism, \(c\iota_1=c\iota_2\). So \((\iota_1,\iota_2)\colon X\to Z\times Z\) factors through the kernel pair \(R\), by a morphism \(k\colon X\to R\). By (G2), \(X\) is the coproduct of the fibre products of \(k\) with the four pieces of \(R\). Three of them are initial: a \(T\)-point of the fibre product with \(d_1\) has \(\iota_2x=\iota_1x'\) in the second coordinate, one with \(d_2\) has \(\iota_1x=\iota_2x'\) in the first, and one with \(e_{21}\) has \(\iota_1x=\iota_2ma\) in the first. So \(X\) is isomorphic to its fibre product with the piece \(e_{12}\), and the projection to \(A\) gives \(s\colon X\to A\) with \((\iota_1,\iota_2)=(\iota_1ms,\iota_2ms)\). Since \(\iota_1\) is a monomorphism, \(ms=1_X\). Then \(msm=m\), and since \(m\) is a monomorphism, \(sm=1_A\). \(\square\)

**Proposition 1.5.**

1. Every epimorphism is the coequalizer of its kernel pair, and every pullback of an epimorphism is an epimorphism.
2. Let \(e\colon B'\to B\) be an epimorphism and \(g\colon B\to Z\) a morphism such that \(ge\) factors through a subobject \(j\colon Z'\to Z\). Then \(g\) factors through \(j\).

**Proof.** (1) Let \(f\colon Y\to X\) be an epimorphism, and write \(f=mq\) as in Lemma 1.3. Then \(m\) is an epimorphism because \(f\) is, and a monomorphism by Lemma 1.3, so it is an isomorphism by Lemma 1.4. Hence \(f\) is, up to this isomorphism, the coequalizer \(q\) of its kernel pair, and by (G3) its pullbacks are coequalizers, hence epimorphisms.

(2) Let \(j'\colon B\times_ZZ'\to B\) be the pullback of \(j\) along \(g\), a monomorphism. Since \(ge\) factors through \(j\), \(e\) factors through \(j'\), and then \(j'\) is an epimorphism because \(e\) is. By Lemma 1.4, \(j'\) is an isomorphism, and \(g\) factors through \(j\) by the projection \(B\times_ZZ'\to Z'\) composed with \(j'^{-1}\). \(\square\)

## 2. The site of generators

In this section and the next, \(\mathcal E\) satisfies (G1)–(G4).

**Lemma 2.1.** There is a small full subcategory \(\mathcal C\) of \(\mathcal E\) that contains \(G\) and, for every diagram \(U\to W\leftarrow V\) in \(\mathcal C\), a fibre product \(U\times_WV\) formed in \(\mathcal E\). For every object \(Y\) of \(\mathcal E\), the family of all morphisms from objects of \(\mathcal C\) to \(Y\) is epimorphic. Call a set of morphisms of \(\mathcal C\) with a common target a *covering* if it is epimorphic in \(\mathcal E\). Then \(\mathcal C\) is a site [Stacks, Tag 00VH].

**Proof.** Put \(\mathcal C^{(0)}=G\), and let \(\mathcal C^{(n+1)}\) consist of \(\mathcal C^{(n)}\) and a chosen fibre product of every diagram \(U\to W\leftarrow V\) of objects of \(\mathcal C^{(n)}\). Since \(\mathcal E\) is locally small, these are small sets, and the full subcategory on \(\bigcup_n\mathcal C^{(n)}\) has the stated property, each diagram lying in some \(\mathcal C^{(n)}\). The family of morphisms into \(Y\) from objects of \(\mathcal C\) contains the family from objects of \(G\), so it is epimorphic. The coverings of an object form a set, \(\mathcal C\) being small.

An isomorphism is a covering. If \(\{U_i\to U\}\) is a covering and so is \(\{U_{ij}\to U_i\}\) for every \(i\), then \(\coprod_{i,j}U_{ij}\to\coprod_iU_i\to U\) is a composite of epimorphisms (Lemma 1.2 (3)), so \(\{U_{ij}\to U\}\) is a covering. If \(\{U_i\to U\}\) is a covering and \(V\to U\) is a morphism of \(\mathcal C\), the fibre products \(U_i\times_UV\) lie in \(\mathcal C\). By (G2), \(\coprod_i(U_i\times_UV)=(\coprod_iU_i)\times_UV\), and its morphism to \(V\) is a pullback of the epimorphism \(\coprod_iU_i\to U\). It is an epimorphism by Proposition 1.5 (1), so \(\{U_i\times_UV\to V\}\) is a covering. \(\square\)

**Lemma 2.2.** For every object \(X\) of \(\mathcal E\), the presheaf \(h_X=\operatorname{Hom}_{\mathcal E}(-,X)\) on \(\mathcal C\) is a sheaf.

**Proof.** Let \(\{U_i\to U\}\) be a covering. By Lemma 1.2 (3) and Proposition 1.5 (1), the epimorphism \(\coprod_iU_i\to U\) is the coequalizer of its kernel pair, which is \(\coprod_{i,j}U_i\times_UU_j\) by (G2). So a morphism \(U\to X\) is the same as a family of morphisms \(U_i\to X\) whose restrictions to \(U_i\times_UU_j\) through the two projections agree for all \(i,j\). This is the sheaf condition [Stacks, Tag 00VL]. \(\square\)

## 3. Giraud's theorem

**Theorem 3.1 (Giraud).** Let \(\mathcal E\) satisfy Giraud's conditions, and let \(\mathcal C\) be as in Lemma 2.1. The functor
\[
\Phi\colon\mathcal E\to\operatorname{Sh}(\mathcal C),\qquad X\mapsto h_X,
\]
is an equivalence of categories. In particular \(\mathcal E\) is a topos.

**Proof.** By Lemma 2.2, \(\Phi\) takes values in sheaves.

*\(\Phi\) is faithful.* If \(h_u=h_v\) for \(u,v\colon X\to Y\), then \(ua=va\) for every morphism \(a\colon U\to X\) with \(U\in\mathcal C\). These morphisms form an epimorphic family (Lemma 2.1), so \(u=v\).

*\(\Phi\) is full.* Let \(\alpha\colon h_X\to h_Y\) be a morphism of sheaves. Let \(S=\coprod_{(U,a)}U\), the coproduct over the pairs of an object \(U\) of \(\mathcal C\) and a morphism \(a\colon U\to X\). Let \(p\colon S\to X\) be \(a\) on the summand of \((U,a)\), and \(v\colon S\to Y\) be \(\alpha(a)\) there. By Lemma 2.1 and Lemma 1.2 (3), \(p\) is an epimorphism, so by Proposition 1.5 (1) it is the coequalizer of its kernel pair \(S\times_XS\). By (G2), \(S\times_XS\) is the coproduct of the objects \(U\times_XU'\), over pairs of summands \((U,a)\) and \((U',a')\). Let \(w\colon W\to U\times_XU'\) with \(W\in\mathcal C\), with components \(b\colon W\to U\) and \(b'\colon W\to U'\), so that \(ab=a'b'\). Since \(\alpha\) is a morphism of presheaves, \(\alpha(a)b=\alpha(ab)=\alpha(a'b')=\alpha(a')b'\). So the two composites of \(v\) with the projections of \(S\times_XS\) agree on \(U\times_XU'\) after composition with every such \(w\). These \(w\) form an epimorphic family, so \(v\) is constant on the kernel pair of \(p\), and there is a unique \(u\colon X\to Y\) with \(up=v\). For \(a\colon U\to X\) with \(U\in\mathcal C\), \(ua=up\iota_{(U,a)}=v\iota_{(U,a)}=\alpha(a)\). Hence \(h_u=\alpha\).

*\(\Phi\) is essentially surjective.* Let \(F\) be a sheaf on \(\mathcal C\). Let \(S=\coprod_{(U,s)}U\), the coproduct over the pairs of an object \(U\) of \(\mathcal C\) and an element \(s\in F(U)\), with inclusions \(\iota_{U,s}\). For \(W\in\mathcal C\), let \(\Lambda(W)\) be the set of the sextuples \(\lambda=(U,s,b,U',s',b')\), with \(b\colon W\to U\) and \(b'\colon W\to U'\) morphisms of \(\mathcal C\) and \(F(b)(s)=F(b')(s')\). Each \(\lambda\) gives the \(W\)-point \(\lambda^\sharp=(\iota_{U,s}b,\iota_{U',s'}b')\) of \(S\times S\). Let \(R_0=\coprod_{W,\lambda}W\), over all \(W\in\mathcal C\) and \(\lambda\in\Lambda(W)\), with the morphism \(R_0\to S\times S\) given by the \(\lambda^\sharp\). Factor it as an epimorphism \(e\colon R_0\to R\) followed by a monomorphism \(j\colon R\to S\times S\), by Lemma 1.3.

*Step 1.* Let \(W\in\mathcal C\), and let \(x=\iota_{U,s}b\) and \(y=\iota_{U',s'}b'\) be \(W\)-points of \(S\), with \(b\colon W\to U\) and \(b'\colon W\to U'\) in \(\mathcal C\). Then \((x,y)\) factors through \(j\) if and only if \(F(b)(s)=F(b')(s')\).

If \(F(b)(s)=F(b')(s')\), then \((x,y)=\lambda^\sharp\) for \(\lambda=(U,s,b,U',s',b')\), which factors through \(R_0\), hence through \(j\). Conversely, let \((x,y)=jk\) with \(k\colon W\to R\). The pullback \(W\times_RR_0\to W\) of \(e\) is an epimorphism (Proposition 1.5 (1)). By (G2), \(W\times_RR_0\) is the coproduct of the fibre products of \(k\) with the summands \(W'_\lambda\) of \(R_0\). Composing the morphisms into these fibre products from objects of \(\mathcal C\) (Lemma 2.1) with the projections to \(W\) gives a covering \(\{z\colon Z\to W\}\). For each \(z\) there are \(W'\in\mathcal C\), \(\lambda=(U_1,s_1,b_1,U'_1,s'_1,b'_1)\in\Lambda(W')\) and \(z'\colon Z\to W'\) with
\[
\begin{aligned}\iota_{U,s}bz&=\iota_{U_1,s_1}b_1z',\\ \iota_{U',s'}b'z&=\iota_{U'_1,s'_1}b'_1z'.\end{aligned}
\]
If \(Z\) is not initial, the first equation gives a \(Z\)-point of the fibre product of two summand inclusions of \(S\), so \((U,s)=(U_1,s_1)\) by (G2) and Lemma 1.2 (1), and \(bz=b_1z'\) because \(\iota_{U,s}\) is a monomorphism. In the same way \((U',s')=(U'_1,s'_1)\) and \(b'z=b'_1z'\). Then
\[
\begin{aligned}F(z)F(b)(s)&=F(z')F(b_1)(s_1)\\&=F(z')F(b'_1)(s'_1)\\&=F(z)F(b')(s').\end{aligned}
\]
If \(Z\) is initial, the empty family is a covering of \(Z\), so \(F(Z)\) has exactly one element, and the same equality holds. By the sheaf property of \(F\), \(F(b)(s)=F(b')(s')\).

*Step 2.* Every \(W\)-point \(x\) of \(S\), \(W\in\mathcal C\), has the form of Step 1 locally: by (G2), \(W\) is the coproduct of the \(W\times_SU\) over the summands \(U\) of \(S\), and composing morphisms into these pieces from objects of \(\mathcal C\) gives a covering \(\{z\colon Z\to W\}\) with \(xz=\iota_{U,s}c\) for some \((U,s)\) and \(c\colon Z\to U\). For finitely many \(W\)-points, the fibre products in \(\mathcal C\) of such coverings give a common one.

*Step 3.* \(R\) is an equivalence relation on \(S\). On the summand of \((U,s)\), the diagonal is \((\iota_{U,s},\iota_{U,s})\), which factors through \(j\) by Step 1; so the diagonal factors through \(j\). For symmetry and transitivity we use Proposition 1.5 (2) with the epimorphisms \(\coprod Z\to W\) of coverings and \(\coprod_{W\to R}W\to R\), over the morphisms from objects of \(\mathcal C\) (Lemma 2.1). They show that a morphism into \(S\times S\) factors through \(j\) if its restrictions to the members of a covering of every \(W\)-point of its source do. For a \(W\)-point of \(R\), \(W\in\mathcal C\), with components \((x,y)\), take a covering on which \(x\) and \(y\) have the form of Step 1. By Step 1 the condition \(F(b)(s)=F(b')(s')\) holds there, and it is symmetric, so \((y,x)\) factors through \(j\) on the covering, hence on \(W\). For a \(W\)-point of \(R\times_SR\), with components \((x,y)\) and \((y,w)\), take a covering on which \(x\), \(y\) and \(w\) have the form of Step 1. There Step 1 gives \(F(b)(s)=F(b')(s')=F(b'')(s'')\), so \((x,w)\) factors through \(j\).

*Step 4.* By (G3), \(R\) has a coequalizer \(q\colon S\to X\), and \(R=S\times_XS\). For \(V\in\mathcal C\) and \(t\in F(V)\) put \(\theta_V(t)=q\iota_{V,t}\in h_X(V)\). For a morphism \(g\colon V'\to V\) of \(\mathcal C\), Step 1 with \(b=g\) and \(b'=\mathrm{id}\) shows that \((\iota_{V,t}g,\iota_{V',F(g)(t)})\) factors through \(R\). So \(\theta_V(t)g=\theta_{V'}(F(g)(t))\), and \(\theta\colon F\to h_X\) is a morphism of presheaves.

*Step 5.* Each \(\theta_V\) is injective: if \(q\iota_{V,t}=q\iota_{V,t'}\), then \((\iota_{V,t},\iota_{V,t'})\) factors through the kernel pair \(R\) of \(q\), and Step 1 with \(b=b'=\mathrm{id}\) gives \(t=t'\).

*Step 6.* Each \(\theta_V\) is surjective. Let \(x\colon V\to X\). Since \(q\) is an epimorphism, so is \(V\times_XS\to V\) (Proposition 1.5 (1)). As in Step 2, there is a covering \(\{z_k\colon Z_k\to V\}\) with \(xz_k=q\iota_{U_k,s_k}c_k\) for some \((U_k,s_k)\) and \(c_k\colon Z_k\to U_k\). Put \(t_k=F(c_k)(s_k)\in F(Z_k)\). On \(Z_{kl}=Z_k\times_VZ_l\), with projections \(\pi_k\) and \(\pi_l\),
\[
\begin{aligned}q\iota_{U_k,s_k}c_k\pi_k&=xz_k\pi_k\\&=xz_l\pi_l=q\iota_{U_l,s_l}c_l\pi_l.\end{aligned}
\]
So \((\iota_{U_k,s_k}c_k\pi_k,\iota_{U_l,s_l}c_l\pi_l)\) factors through \(R\), and Step 1 gives \(F(\pi_k)(t_k)=F(\pi_l)(t_l)\). As \(F\) is a sheaf, there is \(t\in F(V)\) with \(F(z_k)(t)=t_k\) for every \(k\). By Step 4,
\[
\begin{aligned}\theta_V(t)z_k&=\theta_{Z_k}(t_k)=\theta_{U_k}(s_k)c_k\\&=q\iota_{U_k,s_k}c_k=xz_k.\end{aligned}
\]
The \(z_k\) form an epimorphic family, so \(\theta_V(t)=x\).

Hence \(\theta\) is an isomorphism of sheaves \(F\cong h_X=\Phi(X)\). \(\square\)

**Proposition 3.2.** Let \(\mathcal D\) be a small site. Then \(\operatorname{Sh}(\mathcal D)\) satisfies Giraud's conditions. Consequently, a locally small category satisfies Giraud's conditions if and only if it is equivalent to the category of sheaves on a small site.

**Proof.** Limits of sheaves are computed in presheaves [Stacks, Tag 00W2], which gives (G1). Colimits of sheaves are the sheafifications of the colimits of presheaves [Tag 00WI], and sheafification, the left adjoint of the inclusion [Tag 00WH], is exact [Tag 00WJ]. In presheaves, limits and colimits are computed objectwise, so (G2) and (G3) hold there because they hold for sets. Coproducts of sets are disjoint unions, and an equivalence relation on a set is the kernel pair of the quotient map; the pullback of a surjection is a surjection, which is the coequalizer of its kernel pair.

(G2). Let \((Y_a)\) be sheaves, \(P\) their coproduct as presheaves and \(Y=P^\#\) their coproduct as sheaves. By exactness, the monomorphisms \(Y_a\to P\) give monomorphisms \(Y_a\to Y\), and \(Y_a\times_YY_b\) is the sheafification of the empty presheaf \(Y_a\times_PY_b\), the initial sheaf, for \(a\neq b\). Let \(g\colon X\to Y\) be a morphism of sheaves, and \(X'=X\times_YP\), a presheaf. By (G2) for presheaves, \(X'\) is the presheaf coproduct of the \(Y_a\times_PX'=Y_a\times_YX\), which are sheaves. Sheafifying, and using exactness, \(X=X\times_YY=X'^\#\) is the sheaf coproduct of the \(Y_a\times_YX\).

(G3). Let \(R\) be an equivalence relation on a sheaf \(Y\); it is one in presheaves. Let \(Q^p\) be its coequalizer in presheaves, so that \(R=Y\times_{Q^p}Y\), and \(Q=(Q^p)^\#\) its coequalizer in sheaves. By exactness, \(R=Y\times_QY\). Let \(Q'\to Q\) be a morphism of sheaves, and \(P'=Q'\times_QQ^p\). In presheaves, \(Y\times_{Q^p}P'\to P'\) is the coequalizer of \(R\times_{Q^p}P'\rightrightarrows Y\times_{Q^p}P'\). Sheafification preserves coequalizers and fibre products, and carries \(P'\), \(Y\times_{Q^p}P'\) and \(R\times_{Q^p}P'\) to \(Q'\), \(Y\times_QQ'\) and \(R\times_QQ'\). So \(Y\times_QQ'\to Q'\) is the coequalizer of \(R\times_QQ'\rightrightarrows Y\times_QQ'\).

(G4). The sheaves \(h_U^\#\), \(U\in\mathcal D\), form a small set, and the morphisms \(h_U^\#\to F\) correspond to the elements of \(F(U)\) [Tag 00WH] and the Yoneda lemma. Two morphisms \(F\rightrightarrows F'\) that agree after composition with all of them agree on all sections, so they are equal.

Giraud's conditions are invariant under equivalence of categories, and Theorem 3.1 gives the converse. \(\square\)

## 4. Second total topoi and classifying topoi

**Corollary 4.1.** Let \(X\) be a good topos fibred over a small category \(I\) (Definition 2.1 of the lesson on fibred topoi). Then \(\operatorname{Top}^{\mathrm o}(X)\) satisfies Giraud's conditions, so it is a topos, and for every object \(i\) the functor \(i^{\mathrm o*}\) is the inverse image of a morphism of topoi \(X_i\to\operatorname{Top}^{\mathrm o}(X)\). In particular, the standing hypotheses of the lesson on the cohomology of the second total topos hold for every good fibred topos.

**Proof.** Each \(X_i\) is equivalent to the category of sheaves on a small site (Lemma 4.1 of the lesson on fibred topoi), so it satisfies Giraud's conditions (Proposition 3.2). By Proposition 2.2 (b) of that lesson, \(\operatorname{Top}^{\mathrm o}(X)\) has finite limits and small colimits, computed levelwise. A morphism of \(\operatorname{Top}^{\mathrm o}(X)\) is therefore a monomorphism if and only if all its levels are, its kernel pair being computed levelwise. Coproducts, their pullbacks and the fibre products of their summands are computed levelwise. An equivalence relation of \(\operatorname{Top}^{\mathrm o}(X)\) is an equivalence relation in every level, and its coequalizer, the kernel pair of the coequalizer and the pullbacks in (G3) are computed levelwise. So (G1)–(G3) hold in \(\operatorname{Top}^{\mathrm o}(X)\) because they hold in every \(X_i\). The category is locally small, a morphism being a family of morphisms indexed by the small set of objects of \(I\).

For (G4), let \(G_i\) be a small generating set of \(X_i\), and let \(i^{\mathrm o}_!\) be the left adjoint of \(i^{\mathrm o*}\) (Proposition 3.1 (2) there). The objects \(i^{\mathrm o}_!(U)\), \(i\in I\), \(U\in G_i\), form a small set. If \(u,v\colon E\to E'\) are distinct, then \(u_i\neq v_i\) for some \(i\), so \(u_ia\neq v_ia\) for some \(a\colon U\to E_i\) with \(U\in G_i\). By the naturality of the adjunction, the morphisms \(i^{\mathrm o}_!(U)\to E\) adjoint to \(a\), composed with \(u\) and \(v\), are adjoint to \(u_ia\) and \(v_ia\), so they differ. By Theorem 3.1, \(\operatorname{Top}^{\mathrm o}(X)\) is a topos. By Proposition 3.1 (2) there, \(i^{\mathrm o*}\) has a left adjoint and a right adjoint \(i^{\mathrm o}_*\); so it preserves limits and colimits, and with \(i^{\mathrm o}_*\) it is the inverse image of a morphism of topoi. \(\square\)

**Corollary 4.2.** Let \(X\) be a good pseudo-category (Definition 3.2 of the lesson on equivariant sheaves). Then \(BX\) satisfies Giraud's conditions, so it is a topos, the *classifying topos* of \(X\). The functors \(\operatorname{ner}\colon BX\to\operatorname{Top}(X)\) and \(\operatorname{ner}^{\mathrm o}\colon BX\to\operatorname{Top}^{\mathrm o}(X)\) are the inverse images of morphisms of topoi \(\operatorname{Top}(X)\to BX\) and \(\operatorname{Top}^{\mathrm o}(X)\to BX\).

**Proof.** By Proposition 2.2 (1) of the lesson on equivariant sheaves, \(BX\) has finite limits and small colimits, and the forgetful functor \(U\colon BX\to X_0\) creates them. The topos \(X_0\) satisfies Giraud's conditions by Proposition 3.2. Since \(U\) creates finite limits, a morphism of \(BX\) is a monomorphism if and only if its image is, and an equivalence relation of \(BX\) is carried to one of \(X_0\). Since \(U\) creates colimits as well, coproducts and their pullbacks, coequalizers of equivalence relations, their kernel pairs and the pullbacks in (G3) are computed in \(X_0\). So (G1)–(G3) hold in \(BX\), which is locally small. By Proposition 6.3 (1) there, \(BX\) has a small generating family. By Theorem 3.1, \(BX\) is a topos. By Proposition 2.2 (2) and Proposition 6.3 (2) there, \(\operatorname{ner}\) and \(\operatorname{ner}^{\mathrm o}\) preserve finite limits and have right adjoints. Their targets are topoi, by Theorem 4.2 of the lesson on fibred topoi and Corollary 4.1. So they are the inverse images of morphisms of topoi. \(\square\)

**Remark 4.3.** When every \(f_!\) preserves fibre products, Theorem 4.3 of the lesson on fibred topoi gives an explicit site for \(\operatorname{Top}^{\mathrm o}(X)\), built levelwise from sites of the \(X_i\). Corollary 4.1 needs no such hypothesis; its site is the small full subcategory of Lemma 2.1, with the epimorphic families as coverings.

## 5. Exercises

**Exercise 5.1** (easy). Show that the category of commutative rings has finite limits and small coproducts, that the inclusion \(\mathbb Z\to\mathbb Q\) is a monomorphism and an epimorphism but not an isomorphism, and that its coproducts are not disjoint.

**Exercise 5.2** (medium). Show that in the category of abelian groups, coproducts are disjoint but not stable under pullback, and that its initial object is not strict. Conclude that this category is not equivalent to a topos.

**Exercise 5.3** (medium). Let \(f\colon X_0\to X_1\) be a morphism of topoi whose inverse image \(f^*\) has a left adjoint \(f_!\), regarded as a topos fibred over \(\{0\to1\}\). Describe \(\operatorname{Top}^{\mathrm o}(X)\) and a generating set of it, and deduce from Corollary 4.1 that it is a topos. Show that every \(f_!\) of a localization morphism \(T/U\to T\) preserves fibre products, so that Theorem 4.3 of the lesson on fibred topoi also applies in that case.

**Exercise 5.4** (hard). Let \(\mathcal P\) be the category of partially ordered sets and increasing maps. Show that \(\mathcal P\) satisfies (G1), (G2) and (G4), that every equivalence relation has a coequalizer, but that some equivalence relation is not the kernel pair of its coequalizer. Conclude that \(\mathcal P\) is not equivalent to a topos.

## 6. Complete solutions

**Solution 5.1.** Finite limits of rings are computed on the underlying sets. The coproduct of two rings is their tensor product over \(\mathbb Z\), and the coproduct of an arbitrary family is the filtered colimit of the coproducts of its finite subfamilies. The inclusion \(\mathbb Z\to\mathbb Q\) is injective, hence a monomorphism, and it is not surjective. Two ring maps \(\mathbb Q\to A\) that agree on \(\mathbb Z\) agree on every \(1/n\), the inverse of the image of \(n\); so it is an epimorphism. By Lemma 1.4, the conditions (G1)–(G3) cannot all hold. Directly: the coproduct of \(\mathbb Q\) with itself is \(\mathbb Q\otimes\mathbb Q=\mathbb Q\), with both inclusions the identity, so the fibre product of the two inclusions is \(\mathbb Q\), while the initial ring is \(\mathbb Z\). So coproducts are not disjoint. The initial ring is not strict either: \(\mathbb Z[t]\to\mathbb Z\), \(t\mapsto0\), is not an isomorphism.

**Solution 5.2.** The coproduct of \(A\) and \(B\) is \(A\oplus B\), and the fibre product of the inclusions is \(\{(a,b):(a,0)=(0,b)\}=0\), the initial group; so coproducts are disjoint. Pull back the coproduct \(A\oplus A\) along the diagonal \(\delta\colon A\to A\oplus A\), \(a\mapsto(a,a)\). The pullback of the first summand is \(\{a:(a,a)\in A\oplus0\}=0\), and so is that of the second. So the coproduct of the pullbacks is \(0\), while the pullback of \(A\oplus A\) is \(A\). For \(A\neq0\) stability fails. The initial object \(0\) is also final, so every group has a morphism to \(0\), which is an isomorphism only for the zero group. By Lemma 1.2 (1) and Proposition 3.2, the category is not equivalent to a topos.

**Solution 5.3.** An object of \(\operatorname{Top}^{\mathrm o}(X)\) is a triple \((E_0,E_1,\varphi)\) with \(\varphi\colon E_0\to f^*E_1\), and a morphism is a pair of morphisms compatible with the \(\varphi\) (Definition 2.1 of the lesson on fibred topoi). By Proposition 3.1 (2) there, \(0^{\mathrm o}_!(L)=(L,f_!L,\eta)\), with \(\eta\colon L\to f^*f_!L\) the unit, and \(1^{\mathrm o}_!(M)=(0,M,0)\). For generating sets \(G_0\) of \(X_0\) and \(G_1\) of \(X_1\), these objects form a generating set, as in the proof of Corollary 4.1, which shows that \(\operatorname{Top}^{\mathrm o}(X)\) is a topos. For a localization \(j\colon T/U\to T\), \(j_!\) sends \(V\to U\) to \(V\); fibre products in \(T/U\) are computed in \(T\), so \(j_!\) preserves them.

**Solution 5.4.** Finite limits of partially ordered sets are computed on the underlying sets with the componentwise order, and coproducts are disjoint unions, ordered summand by summand; a pullback of a disjoint union is the disjoint union of the pullbacks, so (G2) holds. The chain \(\{0<1\}\) generates: two distinct increasing maps differ at a point, that is, after composition with a map from the chain constant at that point. Every pair of maps \(r_1,r_2\colon R\to Y\) has a coequalizer: identify \(r_1(\rho)\) with \(r_2(\rho)\) for every \(\rho\), order the quotient set by the smallest preorder for which the quotient map is increasing, and identify the elements of each cycle of that preorder.

Now let \(Y=\{0<1\}\), and let \(R\) be the set \(Y\times Y\) ordered by \((0,0)\leq(1,1)\) and equality otherwise, with \(r_1,r_2\) the two coordinates. The map \((r_1,r_2)\colon R\to Y\times Y\) is injective and increasing, hence a monomorphism. It is an equivalence relation. The diagonal \(Y\to R\), \(y\mapsto(y,y)\), is increasing. The exchange of the coordinates preserves the order of \(R\). For transitivity, let \(((a,b),(b,c))\leq((a',b'),(b',c'))\) in \(R\times_YR\), that is, \((a,b)\leq(a',b')\) and \((b,c)\leq(b',c')\) in \(R\). Either both are equalities, or \((a,b)=(0,0)\) and \((a',b')=(1,1)\); then \(b=0\neq1=b'\), so \((b,c)=(0,0)\) and \((b',c')=(1,1)\). In both cases \((a,c)\leq(a',c')\), so \(((a,b),(b,c))\mapsto(a,c)\) is increasing into \(R\). The coequalizer of \(r_1,r_2\) identifies \(0\) and \(1\), so it is \(Y\to\{\ast\}\), whose kernel pair is \(Y\times Y\) with the componentwise order, in which \((0,0)\leq(0,1)\). In \(R\) these two elements are not comparable, so the identity map from the kernel pair to \(R\) is not increasing, and \(R\) is not the kernel pair of its coequalizer. By (G3) and Proposition 3.2, \(\mathcal P\) is not equivalent to a topos.

## Sources

Giraud's characterization of topoi is due to Giraud; it is Théorème 1.2 of Exposé IV of SGA 4 (*Théorie des topos et cohomologie étale des schémas*, tome 1, retyped edition, [normalesup.org](https://www.normalesup.org/~forgogozo/SGA4/tomes/tome1.pdf)). The proof given here goes through effective epimorphisms and the site of generators; the invertibility of monomorphic epimorphisms is derived from the exactness conditions by an equivalence relation on \(X\sqcup X\). Its use for the second total topos of a fibred topos and for the classifying topos of a pseudo-category follows Illusie, in his work on the cotangent complex.
