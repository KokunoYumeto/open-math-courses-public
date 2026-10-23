# Derived de Rham complexes in characteristic p

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Over a ring of characteristic \(p\), the de Rham complex of a free algebra has a large cohomology, described by the Cartier isomorphism: the cohomology in degree \(i\) is the module of \(i\)-forms on the Frobenius twist. Applied to the columns of the derived de Rham complex, this gives the conjugate filtration, an increasing filtration whose graded pieces are the shifted derived exterior powers of the cotangent complex of the Frobenius twist. This lesson proves the Cartier isomorphism for free algebras and for smooth morphisms of schemes, constructs the conjugate filtration, computes its graded pieces, and deduces that the derived de Rham complex of a smooth morphism is its de Rham complex, and that of a relatively perfect map is the algebra itself.

**Prerequisites.** [*The derived de Rham complex*](the-derived-de-rham-complex.md) (Definition 1.1, Lemmas 1.2–1.4, Definition 2.1, Theorem 2.3); [*Cotangent complexes of simplicial rings*](cotangent-complexes-of-simplicial-rings.md) (Corollary 3.5); [*Localization morphisms and the cotangent complex*](localization-morphisms-and-the-cotangent-complex.md) (Proposition 3.2, Proposition 4.1); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Theorem 3.2: Deligne–Lazard); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#5-localization-étale-maps-smooth-maps-and-tensor-products) (Proposition 5.1).

## Conventions

\(T\) is a topos, \(p\) a prime number, and \(A\) a ring of \(T\) with \(p\cdot1=0\). The Frobenius \(F_A\colon A\to A\), \(a\mapsto a^p\), is a map of rings. For an \(A\)-algebra \(B\), the *Frobenius twist* is \(B^{(p)}=B\otimes_{A,F_A}A\), an \(A\)-algebra through the second factor, with the map of rings \(W\colon B\to B^{(p)}\), \(b\mapsto b\otimes1\), which satisfies \(W(ab)=a^pW(b)\) for \(a\in A\). The *relative Frobenius* is the map of \(A\)-algebras
\[
F_{B/A}\colon B^{(p)}\to B,\qquad b\otimes a\mapsto ab^p.
\]
Since \(d(b^p)=pb^{p-1}db=0\), the de Rham complex \(\Omega^\bullet_{B/A}\) is a complex of \(B^{(p)}\)-modules through \(F_{B/A}\), and its cohomology sheaves \(H^i(\Omega^\bullet_{B/A})\) are \(B^{(p)}\)-modules; they form a graded-commutative \(B^{(p)}\)-algebra. If \(B=A[X]\) is free on a sheaf of sets \(X\), then \(B^{(p)}=A[X]\), free on the elements \(W(x)\). A degreewise free resolution \(P\to B\) gives the simplicial \(A\)-algebra \(P^{(p)}\), degreewise free, and \(L\Omega^\bullet_{B/A}\) is computed by \(|\Omega^\bullet_{P/A}|\) as in the lesson on the derived de Rham complex.

## 1. The Cartier map

**Proposition 1.1.** For every \(A\)-algebra \(B\) there is a unique homomorphism of graded \(A\)-algebras
\[
C^{-1}\colon\Omega^\bullet_{B^{(p)}/A}\to H^\bullet(\Omega^\bullet_{B/A})
\]
with \(C^{-1}(W(b))=b^p\) and \(C^{-1}(dW(b))=[b^{p-1}db]\) for \(b\in B\). It is \(B^{(p)}\)-linear, and natural in \(B\).

**Proof.** In degree \(0\), \(C^{-1}=F_{B/A}\), which lands in the cycles because \(d(ab^p)=0\). In degree \(1\), consider \(\delta\colon B\to H^1(\Omega^\bullet_{B/A})\), \(b\mapsto[b^{p-1}db]\). The form \(b^{p-1}db\) is closed: \(d(b^{p-1}db)=(p-1)b^{p-2}db\wedge db=0\). The map \(\delta\) is additive: in the polynomial ring \(\mathbb Z[X,Y]\), \(c_p=\frac1p\big((X+Y)^p-X^p-Y^p\big)\) has integer coefficients and
\[
\begin{aligned}dc_p&=(X+Y)^{p-1}d(X+Y)\\&\quad-X^{p-1}dX-Y^{p-1}dY,\end{aligned}
\]
so, substituting \(b\), \(b'\) and reducing modulo \(p\),
\[
\begin{aligned}&(b+b')^{p-1}d(b+b')-b^{p-1}db-b'^{p-1}db'\\&\quad=d\big(c_p(b,b')\big)\end{aligned}
\]
is exact. It satisfies \(\delta(bb')=b^p\delta(b')+b'^p\delta(b)\) and \(\delta(ab)=a^p\delta(b)\) for \(a\in A\), since \(da=0\). So \(b\otimes a\mapsto a\,\delta(b)\) is a well defined \(A\)-linear derivation of \(B^{(p)}\) into the \(B^{(p)}\)-module \(H^1\), and it induces a \(B^{(p)}\)-linear map \(\Omega^1_{B^{(p)}/A}\to H^1(\Omega^\bullet_{B/A})\) with \(dW(b)\mapsto\delta(b)\). Classes of degree \(1\) square to zero in \(H^\bullet\), as forms of degree \(1\) do, so this map extends uniquely to the exterior algebra \(\Omega^\bullet_{B^{(p)}/A}=\Lambda^\bullet\Omega^1_{B^{(p)}/A}\). Uniqueness holds because the \(W(b)\) and \(dW(b)\) generate. All constructions are sectionwise and compatible with sheafification. \(\square\)

**Remark 1.2.** The map \(C^{-1}\) does not lift to a map of complexes into \(\Omega^\bullet_{B/A}\) with the same values, in general. For \(p=2\), \(A=\mathbb F_2\) and \(B=\mathbb F_2[x,y]\), such a lift would be additive in degree \(1\) and send \(dW(b)\) to \(b\,db\); but \((x+y)\,d(x+y)-x\,dx-y\,dy=d(xy)\), which is nonzero in \(\Omega^1_{B/A}\). For a free algebra with chosen generators a lift exists (Section 2), but it depends on the generators, so it is not functorial.

## 2. The Cartier isomorphism

**Theorem 2.1.** If \(B=A[X]\) for a sheaf of sets \(X\), or more generally \(B=\operatorname{Sym}_A(M)\) for a flat \(A\)-module \(M\), then \(C^{-1}\) is an isomorphism.

**Proof.** *One variable.* Let \(B=A[t]\), so \(B^{(p)}=A[t']\) with \(t'=W(t)\). The complex \(A[t]\xrightarrow{d}A[t]\,dt\) is the direct sum, over \(n\geq1\), of the complexes \(At^n\to At^{n-1}dt\), multiplication by \(n\), and of \(A\) in degree \(0\). For \(p\nmid n\) the image of \(n\) in \(\mathbb F_p\subseteq A\) is a unit, so the summand is contractible; for \(p\mid n\) the differential is zero. So \(H^0=\bigoplus_kAt^{pk}\) and \(H^1=\bigoplus_kAt^{pk}t^{p-1}dt\), free \(A\)-modules, and \(C^{-1}\) sends the basis \(t'^k\), \(t'^kdt'\) of \(\Omega^\bullet_{A[t']/A}\) to the basis \(t^{pk}\), \(t^{pk+p-1}dt\). This decomposition also shows that \(\Omega^\bullet_{A[t]/A}\) is the direct sum of a complex with zero differential, equal to its cohomology, and of a contractible complex.

*Finitely many variables.* For \(B=A[t_1,\dots,t_r]\), \(\Omega^\bullet_{B/A}=\bigotimes_i\Omega^\bullet_{A[t_i]/A}\) as complexes. By the decomposition of each factor, the tensor product is the direct sum of the tensor product of the parts with zero differential and of complexes having a contractible tensor factor, which are contractible. So \(H^\bullet(\Omega^\bullet_{B/A})=\bigotimes_iH^\bullet(\Omega^\bullet_{A[t_i]/A})\), and \(C^{-1}\), being multiplicative, is the tensor product of the isomorphisms of the first case.

*Sheaves of sets.* \(A[X]\) is the sheaf associated with the presheaf \(U\mapsto A(U)[X(U)]\), the filtered colimit of the polynomial rings on the finite subsets of \(X(U)\). Every \(A(U)\) has \(p\cdot1=0\). Differentials, cohomology of complexes, Frobenius twists and \(C^{-1}\) commute with filtered colimits and with sheafification, which is exact. So the finite case gives the claim.

*Flat modules.* By Theorem 3.2 of the lesson on non-additive functors, \(M\) is the local inductive limit of a local system of finite free modules, and the constructions involved commute with local inductive limits, which are exact. The finite free case is the second case, locally. \(\square\)

**Theorem 2.2.** Let \(f\colon X\to S\) be a smooth morphism of schemes with \(p\cdot1=0\) on \(S\). Put \(A=f^{-1}\mathcal O_S\) and \(B=\mathcal O_X\). Then \(C^{-1}\colon\Omega^i_{B^{(p)}/A}\to H^i(\Omega^\bullet_{X/S})\) is an isomorphism for every \(i\).

**Proof.** The question is local on \(X\), and for affine opens \(U=\operatorname{Spec}R'\subseteq X\) over \(V=\operatorname{Spec}R\subseteq S\) the sheaves involved are the quasi-coherent modules associated with the corresponding modules over \(R'\) and \(R'^{(p)}=R'\otimes_{R,F_R}R\), and \(C^{-1}\) is compatible. So it suffices to treat a smooth map of rings \(R\to R'\) with \(p=0\) in \(R\). The source and target of \(C^{-1}\) are \(R'^{(p)}\)-modules, and localizing \(R'\) at \(g\) corresponds to localizing \(R'^{(p)}\) at \(W(g)\), since \(F_{R'/R}(W(g))=g^p\); the de Rham complex of \(R'_g\) is \(\Omega^\bullet_{R'/R}\otimes_{R'^{(p)}}R'^{(p)}_{W(g)}\), and localization is exact. By [[Stacks, Tag 054L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-etale-over-affine-space)] we may therefore assume that \(R'\) is étale over \(C=R[x_1,\dots,x_d]\).

For the étale map \(C\to R'\), the relative Frobenius \(R'\otimes_{C,F_C}C\to R'\), \(r\otimes c\mapsto r^pc\), is an isomorphism [[Stacks, Tag 0EBS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-relative-frobenius-etale)]. Since \(R'^{(p)}=R'\otimes_CC^{(p)}\) and \(F_{C/R}\circ W=F_C\) on \(C\), this says that \(C\otimes_{C^{(p)}}R'^{(p)}\to R'\), \(c\otimes r\mapsto cF_{R'/R}(r)\), is an isomorphism. Moreover \(\Omega^1_{R'/R}=\Omega^1_{C/R}\otimes_CR'\) because \(C\to R'\) is étale [[Stacks, Tag 0FLV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derham.html#derham-lemma-etale)]. Hence \(\Omega^\bullet_{R'/R}=\Omega^\bullet_{C/R}\otimes_{C^{(p)}}R'^{(p)}\), with differential \(d\otimes1\): elements of \(R'^{(p)}\) act through \(p\)-th powers, which have zero differential. The map \(C^{(p)}\to R'^{(p)}\) is flat, as the base change of the flat map \(C\to R'\). So \(H^i(\Omega^\bullet_{R'/R})=H^i(\Omega^\bullet_{C/R})\otimes_{C^{(p)}}R'^{(p)}\), and also \(\Omega^i_{R'^{(p)}/R}=\Omega^i_{C^{(p)}/R}\otimes_{C^{(p)}}R'^{(p)}\). Under these identifications \(C^{-1}\) for \(R'\) is \(C^{-1}\) for \(C\) tensored with \(R'^{(p)}\), by naturality, and the latter is an isomorphism by Theorem 2.1. \(\square\)

## 3. The conjugate filtration

For a complex \(K\), \(\tau^{\leq i}K\) is the canonical truncation: \(K^j\) for \(j<i\), the cycles \(Z^i\) in degree \(i\), and \(0\) above. It is functorial, and \(\tau^{\leq i}K/\tau^{\leq i-1}K\) is quasi-isomorphic to \(H^i(K)[-i]\).

**Definition 3.1.** Let \(P\to B\) be a degreewise free resolution. The *conjugate filtration* of \(|\Omega^\bullet_{P/A}|\) is \(\operatorname{Fil}_i=|\tau^{\leq i}\Omega^\bullet_{P/A}|\), \(i\geq-1\), the realization of the canonical truncations of the columns. For the standard resolution it is the conjugate filtration of \(L\Omega^\bullet_{B/A}\).

It is increasing, \(\operatorname{Fil}_{-1}=0\), and exhaustive, since every element of the realization lies in finitely many columns of bounded degrees.

**Theorem 3.2.** Let \(P\to B\) be a degreewise free resolution.

1. For every \(i\geq0\) there is a quasi-isomorphism, natural in \(P\),
\[
\operatorname{Fil}_i/\operatorname{Fil}_{i-1}\simeq|\Omega^i_{P^{(p)}/A}|[-i],
\]
where \(|\Omega^i_{P^{(p)}/A}|\) is the unnormalized complex of the simplicial module \(\Omega^i_{P^{(p)}/A}\), in degrees \(\leq0\).
2. Suppose \(\operatorname{Tor}_j^A(B,A_F)=0\) for \(j>0\), where \(A_F\) is \(A\) regarded as an \(A\)-algebra through \(F_A\). Then \(P^{(p)}\to B^{(p)}\) is a degreewise free resolution, \(L_{B/A}\otimes_BB^{(p)}\to L_{B^{(p)}/A}\) is a quasi-isomorphism, and
\[
\operatorname{Fil}_i/\operatorname{Fil}_{i-1}\simeq\Lambda^iL_{B^{(p)}/A}[-i].
\]

**Proof.** (1) The quotient \(\operatorname{Fil}_i/\operatorname{Fil}_{i-1}\) is the realization of the simplicial object \(\tau^{\leq i}/\tau^{\leq i-1}\) of the columns, which maps quasi-isomorphically, column by column, to the simplicial object \(H^i(\Omega^\bullet_{P/A})[-i]\): divide by the boundaries in degree \(i-1\) and \(i\). By Lemma 1.2 of the lesson on the derived de Rham complex, the realizations are quasi-isomorphic. By Theorem 2.1 and the naturality of \(C^{-1}\), \(C^{-1}\colon\Omega^i_{P^{(p)}_n/A}\to H^i(\Omega^\bullet_{P_n/A})\) is an isomorphism of simplicial modules.

(2) \(P\) is a degreewise free, hence flat, simplicial \(A\)-module quasi-isomorphic to \(B\), so the homotopy of \(P^{(p)}=P\otimes_AA_F\) is \(\operatorname{Tor}^A_\bullet(B,A_F)\), which is \(B^{(p)}\) in degree \(0\). So \(P^{(p)}\to B^{(p)}\) is a degreewise free resolution, and by Corollary 3.5 of the lesson on cotangent complexes of simplicial rings, \(\Omega^1_{P^{(p)}/A}\otimes_{P^{(p)}}B^{(p)}\cong L_{B^{(p)}/A}\), the map \(\Omega^1_{P^{(p)}/A}\to\Omega^1_{P^{(p)}/A}\otimes B^{(p)}\) being a quasi-isomorphism. Taking exterior powers of these flat modules, \(\Omega^i_{P^{(p)}/A}\simeq\Lambda^iL_{B^{(p)}/A}\). The base change statement is Proposition 4.1 of the lesson on localization morphisms, for \(A\to B\) and \(F_A\colon A\to A\). \(\square\)

So the conjugate filtration is an increasing filtration of the derived de Rham complex, starting at \(0\) and exhausting it, whose graded pieces are the shifted derived exterior powers \(\Lambda^iL_{B^{(p)}/A}[-i]\) of the cotangent complex of the Frobenius twist: this is the *derived Cartier isomorphism*. In particular \(L\Omega^\bullet_{B/A}\) is computed, up to extensions, by the cotangent complex.

**Proposition 3.3.** The chain of filtered quasi-isomorphisms of Theorem 2.3 of the lesson on the derived de Rham complex, between the realizations for the standard resolution and for another degreewise free resolution \(P'\), consists of quasi-isomorphisms on every step of the conjugate filtration. So the conjugate filtration does not depend on the free resolution.

**Proof.** The filtrations are increasing, start at \(0\) and are exhaustive, so it suffices to consider the graded pieces, and by Theorem 3.2 (1) the maps \(|\Omega^i_{-^{(p)}/A}|\) of the twisted resolutions. In the proof of Theorem 2.3 there, the map \(\alpha\) comes from contractions by maps of complexes, which preserve canonical truncations, so Lemma 1.3 there applies to every \(\operatorname{Fil}_i\); the map \(\beta\) compares, for each \(m\), the free algebras \(A[S_\bullet]\) and \(A[S]\), whose Frobenius twists are the free algebras on the same sheaves of sets, so the weight argument given there applies to \(\Omega^i\) of the twists. \(\square\)

## 4. Smooth and relatively perfect maps

**Corollary 4.1.** Let \(f\colon X\to S\) be a smooth morphism of schemes with \(p\cdot1=0\) on \(S\). Then \(\Lambda^nL_{X/S}\to\Omega^n_{X/S}\) is a quasi-isomorphism for every \(n\), and the map \(L\Omega^\bullet_{X/S}\to\Omega^\bullet_{X/S}\) induced by the augmentation of the standard resolution is a quasi-isomorphism, carrying the conjugate filtration to the canonical filtration \(\tau^{\leq i}\) and inducing on graded pieces the Cartier isomorphisms of Theorem 2.2.

**Proof.** For an affine open as in the proof of Theorem 2.2, \(L_{R'/R}\to\Omega^1_{R'/R}\) is a quasi-isomorphism because \(R\to R'\) is smooth (Proposition 5.1 of the lesson *The cotangent complex*), and by Proposition 3.2 of the lesson on localization morphisms, \(L_{X/S}\) is the associated quasi-coherent module locally. So \(L_{X/S}\to\Omega^1_{X/S}\) is a quasi-isomorphism of flat modules, and so are its exterior powers. The same holds for \(X^{(p)}=X\times_{S,F_S}S\), smooth over \(S\), and for \(B^{(p)}\) on \(X\), the inverse image of \(\mathcal O_{X^{(p)}}\) along the relative Frobenius, a homeomorphism.

The augmentation \(\varepsilon\colon P\to B\) induces maps of complexes \(\Omega^\bullet_{P_n/A}\to\Omega^\bullet_{B/A}\), hence a map from \(|\Omega^\bullet_{P/A}|\) to the realization of the constant object \(\Omega^\bullet_{B/A}\) and, by Lemma 1.4 of the lesson on the derived de Rham complex, to \(\Omega^\bullet_{B/A}\). It carries \(\operatorname{Fil}_i\) into \(\tau^{\leq i}\). On graded pieces it is, through \(C^{-1}\) on both sides (Theorems 2.1 and 2.2, naturality), the map \(|\Omega^i_{P^{(p)}/A}|\to\Omega^i_{B^{(p)}/A}\). Since \(B\) is flat over \(A\), Theorem 3.2 (2) applies, and this map is the composite of the quasi-isomorphism \(|\Omega^i_{P^{(p)}/A}|\simeq\Lambda^iL_{B^{(p)}/A}\) with the quasi-isomorphism \(\Lambda^iL_{B^{(p)}/A}\to\Omega^i_{B^{(p)}/A}\). The filtrations are increasing, start at \(0\) and are exhaustive, so the map is a quasi-isomorphism. \(\square\)

An \(A\)-algebra \(B\) with \(\operatorname{Tor}^A_j(B,A_F)=0\) for \(j>0\) is *relatively perfect* if \(F_{B/A}\colon B^{(p)}\to B\) is an isomorphism. For instance, an étale \(A\)-algebra of rings is relatively perfect [[Stacks, Tag 0EBS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-relative-frobenius-etale)].

**Lemma 4.2.** Let \(B\) be an \(A\)-algebra with \(\operatorname{Tor}^A_j(B,A_F)=0\) for \(j>0\). The map \(L_{B^{(p)}/A}\otimes_{B^{(p)}}B\to L_{B/A}\) induced by \(F_{B/A}\) is zero in \(D(B)\).

**Proof.** Let \(P\to B\) be the standard resolution. The relative Frobenius maps \(F_{P_n/A}\colon P_n^{(p)}\to P_n\) form a map of simplicial \(A\)-algebras \(P^{(p)}\to P\) over \(F_{B/A}\), and \(P^{(p)}\to B^{(p)}\) is a degreewise free resolution by Theorem 3.2 (2). By the naturality in Corollary 3.5 of the lesson on cotangent complexes of simplicial rings, the map of the lemma is represented by \(\Omega^1(F_{P/A})\otimes B\). On \(\Omega^1_{P_n^{(p)}/A}\), generated by the \(dW(x)\), it sends \(dW(x)\) to \(d(x^p)=0\). \(\square\)

**Corollary 4.3.** Let \(B\) be relatively perfect over \(A\). Then \(L_{B/A}\cong0\), and the map \(L\Omega^\bullet_{B/A}\to B\) given by the augmentation in simplicial degree \(0\) is a quasi-isomorphism.

**Proof.** By Lemma 4.2, the map \(L_{B^{(p)}/A}\otimes_{B^{(p)}}B\to L_{B/A}\) is zero, and it is an isomorphism because \(F_{B/A}\) is one. So \(L_{B/A}\cong0\), and \(L_{B^{(p)}/A}\cong L_{B/A}\otimes_BB^{(p)}\cong0\) (Theorem 3.2 (2)). Then \(\operatorname{Fil}_i/\operatorname{Fil}_{i-1}\simeq0\) for \(i\geq1\), and \(L\Omega^\bullet_{B/A}\simeq\operatorname{Fil}_0\simeq|P^{(p)}|\), the realization of \(\Omega^0_{P^{(p)}/A}=P^{(p)}\) through \(C^{-1}=F_{P/A}\) in degree \(0\). This is quasi-isomorphic to \(B^{(p)}\), and to \(B\) through \(F_{B/A}\). The composite is the augmentation, because \(F_{P/A}\) followed by \(\varepsilon\) is \(F_{B/A}\) followed by the augmentation of \(P^{(p)}\). \(\square\)

**Remark 4.4.** The conjugate filtration need not split. For a free algebra, a choice of generators gives a lift of \(C^{-1}\) to a map of complexes, as in the proof of Theorem 2.1, and the filtration of \(\Omega^\bullet_{A[X]/A}\) splits. These splittings are not compatible with all maps of free algebras (Remark 1.2), so they do not assemble on the columns of the derived de Rham complex.

## 5. Exercises

**Exercise 5.1.** Let \(p=3\), \(A=\mathbb F_3\) and \(B=\mathbb F_3[t]\), with \(t^m\,dt\) of polynomial degree \(m+1\). List a basis of \(H^1(\Omega^\bullet_{B/A})\) in the polynomial degrees \(\leq9\), and check that \(C^{-1}\) maps \(dW(t)\), \(W(t)\,dW(t)\) and \(W(t)^2dW(t)\) onto it.

**Exercise 5.2.** Let \(B\) be an étale algebra over a ring \(A\) with \(p=0\) in \(A\). Show that \(L\Omega^\bullet_{B/A}\) is quasi-isomorphic to \(B\), and deduce that \(H^i(\Omega^\bullet_{B/A})=0\) for \(i>0\) and \(H^0=B\).

## 6. Complete solutions

**Solution 5.1.** \(d(t^n)=nt^{n-1}dt\), which is zero exactly when \(3\mid n\). So the boundaries in degree \(1\) are spanned by the \(t^{n-1}dt\) with \(3\nmid n\), and \(H^1\) has the basis of the classes of \(t^{m}dt\) with \(m\equiv2\pmod3\). In polynomial degrees \(m+1\leq9\) these are \([t^2dt]\), \([t^5dt]\), \([t^8dt]\). By Proposition 1.1 and multiplicativity, \(C^{-1}(dW(t))=[t^2dt]\), \(C^{-1}(W(t)\,dW(t))=[t^3\cdot t^2dt]=[t^5dt]\) and \(C^{-1}(W(t)^2dW(t))=[t^6\cdot t^2dt]=[t^8dt]\).

**Solution 5.2.** An étale algebra is flat, so \(\operatorname{Tor}^A_j(B,A_F)=0\) for \(j>0\), and it is relatively perfect [[Stacks, Tag 0EBS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-relative-frobenius-etale)]. Corollary 4.3 gives \(L\Omega^\bullet_{B/A}\simeq B\). An étale algebra is smooth, so by Corollary 4.1 (for the affine schemes involved) \(L\Omega^\bullet_{B/A}\simeq\Omega^\bullet_{B/A}\). Hence \(\Omega^\bullet_{B/A}\) has cohomology \(B\) in degree \(0\) only. Directly: \(\Omega^1_{B/A}=0\) for étale \(B\).

## Sources

The derived de Rham complex in characteristic \(p\), the inverse Cartier map and its relation with the cotangent complex of the Frobenius twist are due to Illusie, in his work on the cotangent complex; Illusie's formulation as a direct sum decomposition was later corrected to the statement on the graded pieces of the conjugate filtration. The conjugate filtration, the derived Cartier isomorphism in this form and the triviality for relatively perfect maps are due to Bhatt, *p-adic derived de Rham cohomology* ([arXiv:1204.6560](https://arxiv.org/abs/1204.6560)), Section 3. The Cartier isomorphism for smooth morphisms is classical and goes back to Cartier; the reduction to étale coordinates uses the AI-integrated Stacks project.
