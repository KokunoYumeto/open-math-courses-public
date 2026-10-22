# Filtered internal Hom and the formulas of Cartan

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(A\) be a commutative ring of a topos \(T\). For filtered complexes \(L,M\) of \(A\)-modules, the sheaf of homomorphisms of degree \(n\) from \(L\) to \(M\) is filtered by the homomorphisms that raise the filtration index by at least \(p\). This lesson derives this filtered Hom on the filtered derived category \(DF(A)\), with no boundedness condition, and proves:

- the filtered derived Hom \(R\mathcal Hom(L,M)\), the filtered derived global sections and the filtered derived Hom \(R\operatorname{Hom}(L,M)=R\Gamma R\mathcal Hom(L,M)\) exist on all of \(DF(A)\), commute with \(\operatorname{gr}\) and with passage to the underlying complexes, and \(\operatorname{Ext}^n_{\mathrm{fil}}(L,M)=\) \(H^nF^0R\operatorname{Hom}(L,M)\);
- the isomorphism of Cartan \(R\mathcal Hom(L\otimes^{\mathbf L}M,N)\cong\) \(R\mathcal Hom(L,R\mathcal Hom(M,N))\), which makes \(DF(A)\) a closed symmetric monoidal category, compatibly with \(\operatorname{gr}\);
- the evaluation, composition and product morphisms built from it, their compatibilities with each other and with \(\operatorname{gr}\);
- for a morphism of ringed topoi \(f\), the adjunction between \(Lf^*\) and \(Rf_*\) on filtered derived categories and its internal form \(R\mathcal Hom(L,Rf_*M)\cong\) \(Rf_*R\mathcal Hom(Lf^*L,M)\), compatibly with \(\operatorname{gr}\); the global product \(R\operatorname{Hom}(L_1,M_1)\otimes\) \(^{\mathbf L}R\operatorname{Hom}(L_2,M_2)\to\) \(R\operatorname{Hom}(L_1\otimes^{\mathbf L}L_2,M_1\otimes^{\mathbf L}M_2)\), which on \(H^0F^0\) is \((f_1,f_2)\mapsto f_1\otimes^{\mathbf L}f_2\).

**Prerequisites.** [*Filtered derived categories*](filtered-derived-categories.md) (Propositions 2.2, 2.3, 4.6 (1), Definition 4.2, Lemma 4.3); [*Filtered tensor products on a ringed topos*](filtered-tensor-products-on-a-ringed-topos.md) (Lemmas 1.2, 1.4, 2.2, 3.1, Proposition 2.3, Corollary 2.4, Proposition 3.2, Theorem 3.3, Proposition 4.1). From the AI-integrated Stacks project: Hom complexes of sheaves and their cohomology [[Stacks, Tag 0A8X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-hom-complexes)]; Hom from a K-flat into a K-injective complex [[Tag 0A96](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-RHom-from-K-flat-into-K-injective)]; restriction of K-injective complexes to a slice [[Tag 08FI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-restrict-K-injective-to-open)]; K-injective complexes [[Tag 070I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-K-injective)]; right derived functors [[Tag 05S9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-right-derived-functor-defined)] and adjoint derived functors [[Tag 0FND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors-general)]; the adjunction of \(Lf^*\) and \(Rf_*\) for modules [[Tag 07A6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-adjoint)]; internal homs in monoidal categories [[Tag 0GWJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-remark-internal-hom-monoidal)]; essentially constant systems [[Tag 05PU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-essentially-constant-diagram)].

## Conventions

As in the lesson on filtered tensor products: \(T\) is a topos, \(A\) a commutative ring of \(T\), \(\otimes=\otimes_A\), and \(CF(A)\), \(KF(A)\), \(DF(A)\), \(DG(A)\) are formed from \(A\)-modules. For complexes \(K,L\), \(\mathcal Hom^n(K,L)=\prod_k\mathcal Hom_A(K^k,L^{k+n})\) with \(\mathrm df=d_L\circ f-(-1)^nf\circ d_K\) [Tag 0A8X], and \(\operatorname{Hom}^\bullet(K,L)=\Gamma(T,\mathcal Hom^\bullet(K,L))\). We use the following morphisms of complexes, verified on homogeneous local sections from the sign rules (the verification for \(c\) is written out in the proof of Lemma 1.3):
\[
\begin{gathered}
c\colon\mathcal Hom^\bullet(K\otimes L,M)\\
\to\mathcal Hom^\bullet(K,\mathcal Hom^\bullet(L,M)),\\
c(f)(x)(y)=f(x\otimes y);\\
\mathrm{ev}\colon\mathcal Hom^\bullet(L,M)\otimes L\to M,\\
f\otimes y\mapsto f(y);\\
\mathrm{comp}\colon\mathcal Hom^\bullet(L,M)\otimes\mathcal Hom^\bullet(K,L)\\
\to\mathcal Hom^\bullet(K,M),\\
g\otimes f\mapsto g\circ f.
\end{gathered}
\]
The map \(c\) is an isomorphism, inverse \(g\mapsto(x\otimes y\mapsto g(x)(y))\), and \(c(\mathrm{ev})=\mathrm{id}\).

## 1. Hom complexes of filtered complexes

**Definition 1.1.** For \(L,M\in CF(A)\), \(\mathcal Hom^\bullet(L,M)\) is filtered by the subsheaves \(F^n\mathcal Hom^m(L,M)\) of families \((f^k)\) with \(f^k(F^pL^k)\subset F^{p+n}M^{k+m}\) for all \(p\): on \(U\in T\), the sections are the families over \(T/U\) with this property. If \(L\) has filtration in \([a,b]\) and \(M\) in \([c,d]\), this filtration is in \([c-b,d-a]\), and \(\Gamma(U,\mathcal Hom^\bullet(L,M))=\operatorname{Hom}^\bullet(L|_U,M|_U)\) as filtered complexes. For graded complexes, \(k^n\mathcal Hom^\bullet(E,F)=\) \(\prod_{j-i=n}\mathcal Hom^\bullet(k^iE,k^jF)\). As in the lesson on filtered derived categories, there is a natural morphism of graded complexes
\[
\begin{aligned}&\gamma\colon\operatorname{gr}\mathcal Hom^\bullet(L,M)\\&\quad\longrightarrow\mathcal Hom^\bullet(\operatorname{gr}L,\operatorname{gr}M),\\&f\in F^n\mapsto(\operatorname{gr}^pf\colon\\&\qquad\operatorname{gr}^pL\to\operatorname{gr}^{p+n}M)_p.\end{aligned}
\tag{1.1}
\]

**Lemma 1.2.** If \(M\) is of injective type (every \(\operatorname{gr}^pM^k\) an injective \(A\)-module), then \(\gamma\) is an isomorphism, and so is its global version \(\operatorname{gr}\operatorname{Hom}^\bullet(L,M)\to\operatorname{Hom}^\bullet(\operatorname{gr}L,\operatorname{gr}M)\).

**Proof.** The restriction of an injective \(A\)-module to \(T/U\) is injective (its left adjoint, extension by zero, is exact), so it suffices to prove the global statement for every \(U\); this is Lemma 4.3 of the lesson on filtered derived categories, applied in \(\operatorname{Mod}(A|_U)\). \(\square\)

**Lemma 1.3.** For \(L,M,N\in CF(A)\), the maps \(c\), \(\mathrm{ev}\) and \(\mathrm{comp}\) are morphisms of filtered complexes, \(c\) is an isomorphism of filtered complexes, and they are compatible with \(\operatorname{gr}\): under \(\gamma\) and \(\mu\colon\operatorname{gr}L\otimes\operatorname{gr}M\to\operatorname{gr}(L\otimes M)\),
\[
\begin{gathered}\gamma\circ\operatorname{gr}(c(f))=c(\operatorname{gr}(f)\circ\mu),\\ \operatorname{gr}(\mathrm{ev})\circ\mu=\mathrm{ev}\circ(\gamma\otimes\mathrm{id}),\\ \gamma\circ\operatorname{gr}(\mathrm{comp})\circ\mu\\ =\mathrm{comp}\circ(\gamma\otimes\gamma),\end{gathered}
\]
the first for every \(f\in F^n\mathcal Hom^\bullet(L\otimes M,N)\), as maps \(\operatorname{gr}L\to\mathcal Hom^\bullet(\operatorname{gr}M,\operatorname{gr}N)(n)\).

**Proof.** For \(f\) of degree \(n\) and \(x\) of degree \(|x|\), \(c(\mathrm df)(x)(y)=\) \(d f(x\otimes y)-\) \((-1)^nf(dx\otimes y)-\) \((-1)^{n+|x|}f(x\otimes dy)\), while \(\mathrm d(c(f))(x)=\) \(\mathrm d(c(f)(x))-(-1)^nc(f)(dx)\) evaluated at \(y\) gives \(df(x\otimes y)-\) \((-1)^{n+|x|}f(x\otimes dy)-\) \((-1)^nf(dx\otimes y)\); so \(c\) is a morphism of complexes. For \(\mathrm{ev}\): \(\mathrm{ev}(\mathrm d(f\otimes y))=\) \((\mathrm df)(y)+(-1)^{|f|}f(dy)=\) \(df(y)\). For \(\mathrm{comp}\): \(\mathrm d(g\circ f)=(\mathrm dg)\circ f+(-1)^{|g|}g\circ\mathrm df\). Filtrations: \(f\in F^n\mathcal Hom(L\otimes M,N)\) means \(f(F^pL\otimes F^qM)\subset F^{p+q+n}N\) for all \(p,q\), that is, \(c(f)(F^pL)\subset F^{p+n}\mathcal Hom(M,N)\); so \(c\) and its inverse preserve the filtrations. If \(f\in F^p\mathcal Hom(L,M)\) and \(y\in F^qL\), then \(f(y)\in F^{p+q}M\), so \(\mathrm{ev}\) maps \(F^r(\mathcal Hom(L,M)\otimes L)\) into \(F^rM\); the same argument applies to \(\mathrm{comp}\). The three identities hold on local sections: both sides send \(\bar x\) (resp. \(\bar f\otimes\bar y\), \(\bar g\otimes\bar f\)) to the class of \(y\mapsto f(x\otimes y)\) (resp. of \(f(y)\), of \(g\circ f\)) in the appropriate graded piece. \(\square\)

## 2. The filtered derived Hom

**Lemma 2.1.** Let \(I\) be filtered K-injective, \(P\) filtered K-flat and \(L\in CF(A)\).

1. \(\gamma\colon\) \(\operatorname{gr}\mathcal Hom^\bullet(L,I)\to\) \(\mathcal Hom^\bullet(\operatorname{gr}L,\operatorname{gr}I)\) is an isomorphism. If \(L\) is filtered acyclic, \(\mathcal Hom^\bullet(L,I)\) and \(\operatorname{Hom}^\bullet(L,I)\) are filtered acyclic; hence a filtered quasi-isomorphism \(L\to L'\) induces filtered quasi-isomorphisms \(\mathcal Hom^\bullet(L',I)\to\mathcal Hom^\bullet(L,I)\) and \(\operatorname{Hom}^\bullet(L',I)\to\operatorname{Hom}^\bullet(L,I)\).
2. \(\mathcal Hom^\bullet(P,I)\) is filtered K-injective, and so is its restriction to every \(T/U\).
3. \(\Gamma(T,-)\) of a filtered K-injective complex is a filtered complex of abelian groups whose graded pieces are \(\Gamma(T,\operatorname{gr}^p-)\).

**Proof.** (1) \(I\) is of injective type, so Lemma 1.2 applies; \(\mathcal Hom^\bullet(\operatorname{gr}^iL,\operatorname{gr}^jI)\) is acyclic when \(\operatorname{gr}^iL\) is, since \(\operatorname{gr}^jI\) is K-injective [Tag 070I] and its restrictions to the slices are K-injective [Tag 08FI]; its global sections are acyclic for the same reason. (2) \(\operatorname{gr}\mathcal Hom^\bullet(P,I)\cong\prod\mathcal Hom^\bullet(\operatorname{gr}^iP,\operatorname{gr}^jI)\), finite products of complexes that are K-injective [Tag 0A96] with injective terms (\(\operatorname{Hom}(G,\mathcal Hom(F,J))=\operatorname{Hom}(G\otimes F,J)\) is exact in \(G\) for \(F\) flat and \(J\) injective). Restriction to \(T/U\) preserves all these properties. (3) The filtration of each term of a filtered K-injective complex splits (Lemma 2.2 (4) of the lesson on filtered tensor products), and \(\Gamma\) preserves split exact sequences. \(\square\)

**Proposition 2.2.** Put, for \(L,M\in DF(A)\) and a filtered K-injective resolution \(M\to I\),
\[
\begin{gathered}R\mathcal Hom(L,M)=\mathcal Hom^\bullet(L,I),\\ R\Gamma(T,M)=\Gamma(T,I),\\ R\operatorname{Hom}(L,M)=\operatorname{Hom}^\bullet(L,I).\end{gathered}
\]

1. These define functors \(DF(A)^{\mathrm o}\times DF(A)\to DF(A)\), \(DF(A)\to DF(\mathrm{Ab})\) and \(DF(A)^{\mathrm o}\times DF(A)\to DF(\mathrm{Ab})\), exact in each variable; \(R\Gamma\) is the right derived functor of \(\Gamma\) [Tag 05S9].
2. \(\gamma\) induces natural isomorphisms \(\operatorname{gr}R\mathcal Hom(L,M)\cong\) \(R\mathcal Hom(\operatorname{gr}L,\operatorname{gr}M)\), \(\operatorname{gr}R\Gamma(T,M)\cong R\Gamma(T,\operatorname{gr}M)\), \(\operatorname{gr}R\operatorname{Hom}(L,M)\cong\) \(R\operatorname{Hom}(\operatorname{gr}L,\operatorname{gr}M)\), where on \(DG(A)\) these functors are computed componentwise in \(D(A)\): \(k^nR\mathcal Hom(E,F)=\) \(\prod_iR\mathcal Hom(k^iE,k^{i+n}F)\). The underlying objects are \(R\mathcal Hom\), \(R\Gamma\), \(R\operatorname{Hom}\) of the underlying complexes.
3. \(R\Gamma(T,R\mathcal Hom(L,M))\cong\) \(R\operatorname{Hom}(L,M)\) naturally, compatibly with \(\operatorname{gr}\).
4. \(\operatorname{Ext}^n_{\mathrm{fil}}(L,M)=\) \(H^nF^0R\operatorname{Hom}(L,M)\), and \(H^nR\operatorname{Hom}(L,M)=\operatorname{Ext}^n(L,M)\) for the underlying objects.

**Proof.** (1) Filtered K-injective resolutions exist (Proposition 2.3 (2) of the lesson on filtered tensor products), and \(KF_{\mathrm{inj}}(A)\to DF(A)\) is an equivalence (Corollary 2.4 there); compose a quasi-inverse with \(\mathcal Hom^\bullet(L,-)\), \(\Gamma\), \(\operatorname{Hom}^\bullet(L,-)\). In \(L\), these carry filtered quasi-isomorphisms to filtered quasi-isomorphisms by Lemma 2.1 (1). For a filtered K-injective \(I\), every filtered quasi-isomorphism \(I\to K'\) has a left inverse in \(KF(A)\) (Corollary 2.4 (2) there), so the ind-object \((I\to K')\mapsto\Gamma(T,K')\) is essentially constant with value \(\Gamma(T,I)\), as in the proof of Proposition 4.6 (3) of the lesson on filtered derived categories. (2) For \(I\) as above, \(\operatorname{gr}I\) is a graded K-injective resolution of \(\operatorname{gr}M\); apply Lemma 2.1 (1) and (3). The underlying complex of \(I\) is K-injective with injective terms (Lemma 2.2 (4) of the lesson on filtered tensor products). (3) Let \(P\to L\) be a filtered K-flat resolution. Then \(\mathcal Hom^\bullet(L,I)\to\mathcal Hom^\bullet(P,I)\) is a filtered quasi-isomorphism into a filtered K-injective complex (Lemma 2.1), so \(R\Gamma(T,R\mathcal Hom(L,M))=\) \(\Gamma(T,\mathcal Hom^\bullet(P,I))=\) \(\operatorname{Hom}^\bullet(P,I)\), which receives the filtered quasi-isomorphism \(\operatorname{Hom}^\bullet(L,I)\to\operatorname{Hom}^\bullet(P,I)\). (4) \(\operatorname{Hom}_{DF}(L,M[n])=\) \(\operatorname{Hom}_{KF}(L,I[n])=\) \(H^nF^0\operatorname{Hom}^\bullet(L,I)\) by Corollary 2.4 (2) of the lesson on filtered tensor products and (4.1) of the lesson on filtered derived categories; the second statement is the case of the underlying complexes. \(\square\)

## 3. Cartan's isomorphism and the closed monoidal structure

**Theorem 3.1.** For \(L,M,N\in DF(A)\), with filtered K-flat resolutions \(P\to L\), \(Q\to M\) and a filtered K-injective resolution \(N\to I\), the isomorphism \(c\colon\) \(\mathcal Hom^\bullet(P\otimes Q,I)\to\) \(\mathcal Hom^\bullet(P,\mathcal Hom^\bullet(Q,I))\) induces natural isomorphisms
\[
\begin{gathered}R\mathcal Hom(L\otimes^{\mathbf L}M,N)\cong\\
R\mathcal Hom(L,R\mathcal Hom(M,N)),\\
R\operatorname{Hom}(L\otimes^{\mathbf L}M,N)\cong\\
R\operatorname{Hom}(L,R\mathcal Hom(M,N)),\end{gathered}
\tag{3.1}
\]
and a bijection, natural in \(L,M,N\),
\[
\begin{aligned}\Phi\colon&\operatorname{Hom}_{DF}(L\otimes^{\mathbf L}M,N)\\&\xrightarrow{\ \sim\ }\operatorname{Hom}_{DF}(L,R\mathcal Hom(M,N)),\end{aligned}
\]
obtained from (3.1) by \(H^0F^0\). Thus \(DF(A)\) is a closed symmetric monoidal category with internal Hom \(R\mathcal Hom\). The isomorphisms (3.1) and \(\Phi\) commute with \(\operatorname{gr}\): under (3.1) of the lesson on filtered tensor products and Proposition 2.2 (2), \(\operatorname{gr}\) of (3.1) is (3.1) for \(\operatorname{gr}L,\operatorname{gr}M,\operatorname{gr}N\) in \(DG(A)\), computed componentwise in \(D(A)\), and \(\operatorname{gr}\Phi(g)\) corresponds to \(\Phi(\operatorname{gr}g)\).

**Proof.** \(P\otimes Q\) is filtered K-flat and represents \(L\otimes^{\mathbf L}M\); \(\mathcal Hom^\bullet(Q,I)\) is filtered K-injective and represents \(R\mathcal Hom(M,N)\) (Lemma 2.1 (2)); so both sides of (3.1) are represented by the two sides of \(c\), with \(L\) represented by \(P\) on the right (Lemma 2.1 (1)). By Lemma 1.3, \(c\) is an isomorphism of filtered complexes, natural in \(P,Q,I\). Independence of the resolutions follows from the naturality of \(c\) and Lemma 2.1 (1). The global version is \(\Gamma(T,-)\) of the first. For \(\Phi\): \(\operatorname{Hom}_{DF}(L\otimes^{\mathbf L}M,N)=\) \(\operatorname{Hom}_{KF}(P\otimes Q,I)=\) \(H^0F^0\operatorname{Hom}^\bullet(P\otimes Q,I)\), and likewise on the right with the filtered K-injective \(\mathcal Hom^\bullet(Q,I)\) (Corollary 2.4 (2) of the lesson on filtered tensor products). The statement about \(\operatorname{gr}\) is the first identity of Lemma 1.3 applied on these models. \(\square\)

By [Tag 0GWJ], the internal Hom gives canonical morphisms. We fix them as follows, writing \([M,N]=R\mathcal Hom(M,N)\) and \(\otimes\) for \(\otimes^{\mathbf L}\), and suppressing associativity and unit isomorphisms (Theorem 3.3 of the lesson on filtered tensor products).

**Definition 3.2.**

1. The *evaluation* \(\mathrm{ev}_{M,N}=\) \(\Phi^{-1}(\mathrm{id})\colon[M,N]\) \(\otimes M\to\) \(N\).
2. The *composition* \(\mathrm{comp}\colon[M,N]\otimes[L,M]\to[L,N]\) is \(\Phi\) of \([M,N]\otimes[L,M]\otimes L\xrightarrow{1\otimes\mathrm{ev}}[M,N]\) \(\otimes M\xrightarrow{\mathrm{ev}}\) \(N\).
3. The *product* \(\pi\colon[L_1,M_1]\) \(\otimes[L_2,M_2]\to[L_1\otimes L_2,M_1\otimes M_2]\) is \(\Phi\) of
\[
\begin{aligned}&[L_1,M_1] \otimes[L_2,M_2] \otimes L_1\\&\quad \otimes L_2 \xrightarrow{1\otimes\sigma\otimes1}[L_1,M_1]\\&\quad \otimes L_1 \otimes[L_2,M_2] \otimes L_2\\&\quad \xrightarrow{\mathrm{ev}\otimes\mathrm{ev}}M_1 \otimes M_2.\end{aligned}
\]
4. For \(L\in DF(A)\) put \(L^\vee=[L,A]\), \(A\) with filtration in \([0,0]\); the morphism \(\nu_{L,M}\colon L^\vee\otimes M\to[L,M]\) is \(\Phi\) of \(L^\vee\otimes M\otimes L\xrightarrow{1\otimes\sigma}\) \(L^\vee\otimes L\otimes M\xrightarrow{\mathrm{ev}\otimes1}\) \(A\otimes M=\) \(M\).

The same definitions in \(D(A)\) and \(DG(A)\) give the corresponding morphisms there.

**Proposition 3.3.**

1. \(\mathrm{ev}\), \(\mathrm{comp}\), \(\pi\) and \(\nu\) are natural, and \(\Phi^{-1}(g)=\mathrm{ev}\circ(g\otimes1)\) for every \(g\colon X\to[M,N]\).
2. On models: if \(Q\to M\) is a filtered K-flat resolution and \(N\to I\) a filtered K-injective one, \(\mathrm{ev}_{M,N}\) is represented by \(\mathrm{ev}\colon\mathcal Hom^\bullet(Q,I)\otimes Q\to I\), the source representing \([M,N]\otimes M\) because \(Q\) is filtered K-flat.
3. The evaluation is compatible with the product: \(\mathrm{ev}_{L_1\otimes L_2,M_1\otimes M_2}\circ(\pi\otimes1)=\) \((\mathrm{ev}\otimes\mathrm{ev})\circ(1\otimes\sigma\otimes1)\).
4. Composition is associative and unital: \(\mathrm{comp}\circ(\mathrm{comp}\otimes1)=\) \(\mathrm{comp}\circ(1\otimes\mathrm{comp})\), and \(\mathrm{comp}(\iota_N\otimes1)=\) \(\mathrm{id}=\) \(\mathrm{comp}(1\otimes\iota_L)\) for \(\iota_L=\Phi(\lambda)\colon A\to[L,L]\).
5. \(\operatorname{gr}\) carries \(\mathrm{ev}\), \(\mathrm{comp}\), \(\pi\), \(\nu\) of \(DF(A)\) to those of \(DG(A)\), under the identifications (3.1) of the lesson on filtered tensor products and Proposition 2.2 (2); the underlying-complex functor carries them to those of \(D(A)\). In \(DG(A)\) they are computed componentwise: on the summand \(R\mathcal Hom(k^iE,k^jF)\otimes k^{i'}E\), \(\mathrm{ev}\) is the evaluation \(R\mathcal Hom(k^iE,k^jF)\otimes k^iE\to k^jF\) of \(D(A)\) if \(i'=i\) and zero otherwise; \(\mathrm{comp}\) maps \(R\mathcal Hom(k^jE',k^lE'')\otimes\) \(R\mathcal Hom(k^iE,k^{j'}E')\) to \(R\mathcal Hom(k^iE,k^lE'')\) by the composition of \(D(A)\) if \(j=j'\) and by zero otherwise.
6. The unit isomorphisms \(A\otimes L\cong L\) and \([A,L]\cong L\) (the latter \(\Phi^{-1}\)-adjoint to \(\lambda\)) identify \(\pi\) for \((L_1,M_1,L_2,M_2)=(L,A,A,M)\) with \(\nu_{L,M}\).

**Proof.** (1) Naturality follows from that of \(\Phi\). \(\Phi\) is natural in the first variable, so \(\Phi^{-1}(g)=\) \(\Phi^{-1}(\mathrm{id}\circ g)=\) \(\Phi^{-1}(\mathrm{id})\circ(g\otimes1)\). (2) On these models \(\Phi\) is the map induced by \(c\) on \(H^0F^0\) (proof of Theorem 3.1), and \(c(\mathrm{ev})=\mathrm{id}\). (3) is (1) applied to \(g=\pi\). (4) By (1) and the definition, both sides of each identity are \(\Phi\) of the same composite of evaluations, by naturality of \(\sigma\) and coherence. (5) The functors \(\operatorname{gr}\) and "underlying complex" are symmetric monoidal (Theorem 3.3 of the lesson on filtered tensor products) and commute with \(\Phi\) (Theorem 3.1), so they carry \(\Phi^{-1}(\mathrm{id})\) to \(\Phi^{-1}(\mathrm{id})\) and the composites defining \(\mathrm{comp}\), \(\pi\), \(\nu\) to the corresponding composites. In \(DG(A)\), \(\operatorname{Hom}_{DG}(X\otimes E,F)=\) \(\prod_{a,b}\operatorname{Hom}_{D(A)}(X_a\otimes E_b,F_{a+b})\cong\) \(\prod_{a,b}\operatorname{Hom}_{D(A)}(X_a,R\mathcal Hom(E_b,F_{a+b}))=\) \(\operatorname{Hom}_{DG}(X,[E,F])\) (Proposition 2.3 of the lesson on filtered derived categories and Theorem 3.1), so \(\Phi^{-1}(\mathrm{id})\) is, on the summand \(R\mathcal Hom(E_i,F_j)\otimes E_{i'}\), the evaluation of \(D(A)\) if \(i'=i\) and zero otherwise; the description of \(\mathrm{comp}\) follows. (6) Both are \(\Phi\) of the same composite after the unit identifications, by (1) and naturality. \(\square\)

**Remark 3.4.** The evaluation \(L\otimes[L,M]\to M\) in the order used by Illusie is \(\mathrm{ev}\circ\sigma\); on models it is \(y\otimes f\mapsto(-1)^{|y||f|}f(y)\). With the conventions of this course, the evaluation in the order \([L,M]\otimes L\) carries no sign, and so does \(\Phi\).

## 4. Morphisms of ringed topoi and global products

**Proposition 4.1.** Let \(f\colon(T',A')\to(T,A)\) be a morphism of ringed topoi.

1. \(Rf_*M=f_*I\), for a filtered K-injective resolution \(M\to I\), defines an exact functor \(Rf_*\colon DF(A')\to DF(A)\), the right derived functor of \(f_*\), with \(\operatorname{gr}Rf_*M\cong Rf_*\operatorname{gr}M\) componentwise and with underlying object \(Rf_*\) of the underlying complex.
2. \(Lf^*\) (Proposition 4.1 of the lesson on filtered tensor products) is left adjoint to \(Rf_*\): \(\operatorname{Hom}_{DF(A')}(Lf^*L,M)=\) \(\operatorname{Hom}_{DF(A)}(L,Rf_*M)\), bifunctorially.
3. There is a natural isomorphism \(R\mathcal Hom(L,Rf_*M)\cong\) \(Rf_*R\mathcal Hom(Lf^*L,M)\) in \(DF(A)\), compatible with \(\operatorname{gr}\); applying \(R\Gamma(T,-)\) and \(H^0F^0\) recovers \(R\operatorname{Hom}(L,Rf_*M)\cong\) \(R\operatorname{Hom}(Lf^*L,M)\) and (2).
4. For \(L,N\in DF(A)\) there is a natural morphism \(R\mathcal Hom(L,N)\to\) \(Rf_*R\mathcal Hom(Lf^*L,Lf^*N)\), (3) composed with \(R\mathcal Hom(L,\eta_N)\) for the unit \(\eta_N\colon N\to Rf_*Lf^*N\) of (2).

**Proof.** (1) The filtration of each term of \(I\) splits, so \(f_*\) preserves it and \(\operatorname{gr}f_*I=f_*\operatorname{gr}I\), with \(\operatorname{gr}^pI\) K-injective. Every filtered quasi-isomorphism out of \(I\) has a left inverse in \(KF(A')\), so as in Proposition 2.2 (1) the right derived functor is defined everywhere with value \(f_*I\). (2) The adjunction \(f^*\dashv f_*\) on modules gives \(\operatorname{Hom}_{CF}(f^*L,M)=\operatorname{Hom}_{CF}(L,f_*M)\), where \(f^*L\) is filtered by the images of the \(f^*F^pL\) (a filtered map \(f^*L\to M\) is one whose adjoint carries \(F^pL\) into \(f_*F^pM\)); it is compatible with filtered homotopies, so \(f^*\) and \(f_*\) are adjoint exact functors between \(KF(A)\) and \(KF(A')\). The left derived functor of \(f^*\) is defined everywhere with value \(f^*P\) for a filtered K-flat resolution \(P\to L\): the filtered K-flat resolutions are initial among filtered quasi-isomorphisms into \(L\) and \(f^*\) carries filtered quasi-isomorphisms between them to filtered quasi-isomorphisms, as in Proposition 3.2 of the lesson on filtered tensor products. Then [Tag 0FND] gives the adjunction. (3) Let \(P\to L\) be a filtered K-flat resolution, \(M\to I\) a filtered K-injective resolution and \(f_*I\to J\) a filtered K-injective resolution. Since \(f^*P\) is filtered K-flat, \(\mathcal Hom^\bullet(f^*P,I)\) is filtered K-injective (Lemma 2.1 (2)) and represents \(R\mathcal Hom(Lf^*L,M)\); so \(Rf_*R\mathcal Hom(Lf^*L,M)\) is represented by \(f_*\mathcal Hom^\bullet(f^*P,I)\). The adjunction on sections over each \(U\) gives an isomorphism of filtered complexes \(f_*\mathcal Hom^\bullet(f^*P,I)\cong\mathcal Hom^\bullet(P,f_*I)\), and we compose it with \(\varphi\colon\mathcal Hom^\bullet(P,f_*I)\to\mathcal Hom^\bullet(P,J)\), whose target represents \(R\mathcal Hom(L,Rf_*M)\). It remains to see that \(\varphi\) is a filtered quasi-isomorphism, that is, that \(\varphi_{ij}\colon\mathcal Hom^\bullet(P_i,f_*I_j)\to\mathcal Hom^\bullet(P_i,J_j)\) is a quasi-isomorphism for \(P_i=\operatorname{gr}^iP\), \(I_j=\operatorname{gr}^jI\), \(J_j=\operatorname{gr}^jJ\) (Lemma 2.1 (1)). It suffices that \(\Gamma(U,\varphi_{ij})\) is a quasi-isomorphism for every \(U\in T\): the cohomology sheaves of the cone of \(\varphi_{ij}\) are the sheaves associated with the cohomology of its sections. Write \(f_U\colon T'/f^{-1}U\to T/U\) for the restriction of \(f\). Then \(H^n\Gamma(U,\mathcal Hom^\bullet(P_i,f_*I_j))=\) \(\operatorname{Hom}_K(f_U^*(P_i|_U),I_j|_{f^{-1}U}[n])\), which is \(\operatorname{Hom}_D(Lf_U^*(P_i|_U),I_j|_{f^{-1}U}[n])\) (the restriction of \(I_j\) is K-injective [Tag 08FI] and \(f_U^*(P_i|_U)\) is K-flat), and \(H^n\Gamma(U,\mathcal Hom^\bullet(P_i,J_j))=\) \(\operatorname{Hom}_D(P_i|_U,J_j|_U[n])\); the map between them induced by \(\varphi_{ij}\) is the adjunction bijection of [Tag 07A6] for \(f_U\), since \(J_j|_U\) is a K-injective resolution of \(f_{U*}(I_j|_{f^{-1}U})=(f_*I_j)|_U\), which computes \(Rf_{U*}\). The compatibility with \(\operatorname{gr}\) holds on these models. Applying \(R\Gamma(T,-)\) and \(H^0F^0\) (Proposition 2.2 (3) and (4)) recovers the global form and the bijection of (2). (4) is a definition. \(\square\)

**Proposition 4.2.** Let \(\rho\colon(T,A)\to(\mathrm{pt},\mathbf Z)\) be the morphism to the punctual topos ringed by \(\mathbf Z\), so \(R\rho_*=R\Gamma(T,-)\). For \(L_i,M_i\in DF(A)\) there is a natural *global product*
\[
\begin{aligned}&R\operatorname{Hom}(L_1,M_1)\\&\quad\otimes^{\mathbf L}_{\mathbf Z}R\operatorname{Hom}(L_2,M_2)\\&\quad\longrightarrow R\operatorname{Hom}(L_1\otimes^{\mathbf L}L_2,\\&\qquad M_1\otimes^{\mathbf L}M_2)\end{aligned}
\tag{4.1}
\]
in \(DF(\mathrm{Ab})\), compatible with \(\operatorname{gr}\), whose effect on \(H^0F^0\), composed with \(H^0F^0(X)\otimes H^0F^0(Y)\to\) \(H^0F^0(X\otimes^{\mathbf L}Y)\), is \((f_1,f_2)\mapsto f_1\otimes^{\mathbf L}f_2\) for \(f_i\in\operatorname{Hom}_{DF}(L_i,M_i)\). Likewise there is a global composition \(R\operatorname{Hom}(M,N)\otimes^{\mathbf L}R\operatorname{Hom}(L,M)\to\) \(R\operatorname{Hom}(L,N)\) inducing composition of morphisms on \(H^0F^0\).

**Proof.** By Proposition 2.2 (3), \(R\operatorname{Hom}(L_i,M_i)=R\rho_*[L_i,M_i]\). By Proposition 4.1 (2), a morphism \(R\rho_*X\otimes R\rho_*Y\to R\rho_*Z\) in \(DF(\mathrm{Ab})\) is the same as a morphism \(L\rho^*(R\rho_*X\otimes R\rho_*Y)=\) \(L\rho^*R\rho_*X\otimes L\rho^*R\rho_*Y\to\) \(Z\); take the composite of the counits \(L\rho^*R\rho_*\to\mathrm{id}\) with the product \(\pi\) of Definition 3.2, for \(X=[L_1,M_1]\), \(Y=[L_2,M_2]\), \(Z=[L_1\otimes L_2,M_1\otimes M_2]\). Compatibility with \(\operatorname{gr}\) follows from Propositions 3.3 (5) and 4.1. An element \(f_i\in\) \(H^0F^0R\operatorname{Hom}(L_i,M_i)=\) \(\operatorname{Hom}_{DF}(\mathbf Z,R\rho_*[L_i,M_i])\) is adjoint to \(\phi_i\colon A=L\rho^*\mathbf Z\to[L_i,M_i]\), and \(\Phi^{-1}(\phi_i)=\mathrm{ev}\circ(\phi_i\otimes1)\colon L_i\to M_i\) is \(f_i\): on models \(P_i\to L_i\), \(M_i\to I_i\), both identifications of \(H^0F^0\operatorname{Hom}^\bullet(P_i,I_i)\) with \(\operatorname{Hom}_{DF}(L_i,M_i)\) send the class of a filtered morphism \(P_i\to I_i\) to itself. The image of \(f_1\otimes f_2\) is adjoint to \(\pi\circ(\phi_1\otimes\phi_2)\), and \(\Phi^{-1}(\pi\circ(\phi_1\otimes\phi_2))=\) \(\mathrm{ev}\circ(\pi\otimes1)\circ(\phi_1\otimes\phi_2\otimes1)=\) \((\mathrm{ev}\otimes\mathrm{ev})\circ(1\otimes\sigma\otimes1)\circ(\phi_1\otimes\phi_2\otimes1)\) by Proposition 3.3 (3); by naturality of \(\sigma\) (with \(\sigma_{A,L_1}\) the unit identification) this is \((\mathrm{ev}\circ(\phi_1\otimes1))\otimes(\mathrm{ev}\circ(\phi_2\otimes1))=\) \(f_1\otimes f_2\). The global composition is constructed in the same way from \(\mathrm{comp}\), and the same computation with Proposition 3.3 (1) shows that it induces composition. \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that the map \(L\otimes\mathcal Hom^\bullet(L,M)\to M\), \(y\otimes f\mapsto f(y)\), without sign, is not a morphism of complexes in general (when \(2\ne0\) in \(A\)), while \(y\otimes f\mapsto(-1)^{|y||f|}f(y)\) is.

**Exercise 5.2.** Let \(E,F\in DG(A)\) be concentrated in weights \(0\) and \(1\) respectively. Compute the weights of \(R\mathcal Hom(E,F)\) and \(R\mathcal Hom(F,E)\), and describe the composition \(R\mathcal Hom(F,E)\otimes R\mathcal Hom(E,F)\to\) \(R\mathcal Hom(E,E)\) componentwise.

**Exercise 5.3.** Let \(L\in DF(A)\) have filtration in \([0,1]\), and \(M\in D(A)\), with filtration in \([0,0]\). Show that \(R\mathcal Hom(L,M)\) has filtration in \([-1,0]\), with \(\operatorname{gr}^0R\mathcal Hom(L,M)\cong R\mathcal Hom(\operatorname{gr}^0L,M)\) and \(\operatorname{gr}^{-1}R\mathcal Hom(L,M)\cong R\mathcal Hom(\operatorname{gr}^1L,M)\), and that the triangle of this filtration is \(R\mathcal Hom(-,M)\) applied to the triangle of the filtration of \(L\).

## 6. Complete solutions

**Solution 5.1.** For \(e(y\otimes f)=f(y)\) and homogeneous \(y,f\),
\[
\begin{aligned}&e(\mathrm d(y\otimes f)) =f(dy)\\&\quad +(-1)^{|y|}(\mathrm df)(y) =f(dy)\\&\quad +(-1)^{|y|}\bigl(d(f(y))-(-1)^{|f|}f(dy)\bigr),\end{aligned}
\]
so \(e\circ\mathrm d-d\circ e\) sends \(y\otimes f\) to \(\bigl((-1)^{|y|}-1\bigr)d(f(y))+\) \(\bigl(1-(-1)^{|y|+|f|}\bigr)f(dy)\). Let \(L=A\) placed in degree \(1\), \(M=(A\xrightarrow{\mathrm{id}}A)\) in degrees \(2,3\), \(f\in\mathcal Hom^1(L,M)\) the identity \(L^1\to M^2\), and \(y=1\in L^1\). Then \(dy=0\) and \(d(f(y))\) is the generator \(e_3\) of \(M^3\), so the defect is \(-2e_3\), nonzero when \(2\ne0\) in \(A\). With the sign \((-1)^{|y||f|}\) the map is \(\mathrm{ev}\circ\sigma\), a composite of morphisms of complexes.

**Solution 5.2.** \(k^nR\mathcal Hom(E,F)=\) \(\prod_iR\mathcal Hom(k^iE,k^{i+n}F)\) is nonzero only for \(n=1\) (\(i=0\)), and \(R\mathcal Hom(F,E)\) only for \(n=-1\). The source \(R\mathcal Hom(F,E)\otimes R\mathcal Hom(E,F)\) is concentrated in weight \(-1+1=0\), and \(R\mathcal Hom(E,E)\) in weight \(0\). By Proposition 3.3 (5) the composition is the composition \(R\mathcal Hom(k^1F,k^0E)\otimes\) \(R\mathcal Hom(k^0E,k^1F)\to\) \(R\mathcal Hom(k^0E,k^0E)\) of \(D(A)\). For instance, for \(k^0E=k^1F=A\) it is the multiplication \(A\otimes A\to A\).

**Solution 5.3.** On models, \(L\) filtered K-flat \(P\) and \(M\to I\) K-injective with filtration in \([0,0]\): \(f\in F^n\mathcal Hom(P,I)\) means \(f(F^pP)\subset F^{p+n}I\), which is \(I\) for \(p+n\le0\) and \(0\) otherwise; so \(F^1=0\), \(F^0=\) \(\{f:f(F^1P)=0\}=\) \(\mathcal Hom(P/F^1P,I)\), \(F^{-1}=\mathcal Hom(P,I)\). Hence \(\operatorname{gr}^0=\mathcal Hom(\operatorname{gr}^0P,I)\) and \(\operatorname{gr}^{-1}=\) \(\mathcal Hom(P,I)/\mathcal Hom(P/F^1P,I)=\) \(\mathcal Hom(F^1P,I)=\) \(\mathcal Hom(\operatorname{gr}^1P,I)\), the sequence \(0\to\) \(\mathcal Hom(P/F^1P,I)\to\) \(\mathcal Hom(P,I)\to\) \(\mathcal Hom(F^1P,I)\to\) \(0\) being exact since \(I\) has injective terms. This short exact sequence is \(\mathcal Hom^\bullet(-,I)\) applied to \(0\to F^1P\to P\to P/F^1P\to0\), so the triangles correspond, by naturality of the triangle of a short exact sequence.

## Sources

The filtered derived Hom, the isomorphisms of Cartan in the filtered setting, the contraction, composition and product morphisms and their compatibility with passage to the associated graded are due to Illusie, in his work on the cotangent complex, where they are constructed on bounded filtered complexes. The isomorphism expressing the adjunction between tensor product and Hom is due to Cartan. The unbounded internal Hom of complexes of modules on a ringed site, through K-injective and K-flat complexes, is treated in the AI-integrated Stacks project, Chapter *Cohomology on Sites*.
