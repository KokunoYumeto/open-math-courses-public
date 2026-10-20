# Left derived functors of left adjoints on total topoi

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(u\colon X\to Y\) be a morphism of fibred topoi, with rings on the two total topoi and a ring map from the ring of \(X\) to the inverse image of the ring of \(Y\). The inverse image of sheaves, followed by restriction of scalars, sends modules on \(\operatorname{Top}(Y)\) to modules on \(\operatorname{Top}(X)\). When the inverse images of the levels have left adjoints, this functor has a left adjoint \(u_!\). It is explicit on the modules induced from the levels, and it is computed by presentations in general. Under an exactness condition on flat modules, \(u_!\) has a left derived functor on bounded above complexes. That functor is computed by the standard simplicial resolution of a complex of flat modules, and it is adjoint to the inverse image at the level of derived Hom complexes. For a constant fibred topos this gives the derived colimit over a small category, together with the adjunction between derived colimits and constant diagrams in its \(R\operatorname{Hom}\) form.

**Prerequisites.** [*Cohomology of total topoi*](cohomology-of-total-topoi.md) (Lemma 1.1, Section 2); Propositions 4.2 and 4.4 of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); [*Derived colimits over a small category*](derived-colimits-over-a-small-category.md) for Section 4; left derived functors computed by a class of complexes [[Stacks, Tag 06XN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-find-existence-computes)]; adjoint functors on derived categories [[Stacks, Tag 0DVC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors)]; flat modules on ringed topoi [[Stacks, Tag 03EY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-ses)].

## 1. The functor \(u_!\)

**1.1. Setting.** Let \(X\) be a topos fibred over \(I\), \(Y\) one fibred over \(J\), and \(u=(u,v)\colon X\to Y\) a morphism (Definition 1.1 of the lesson on morphisms of fibred topoi). Let \(\mathcal O_X\) be a ring of \(\operatorname{Top}(X)\) and \(\mathcal O_Y\) a ring of \(\operatorname{Top}(Y)\), as in Section 4.1 of that lesson: rings \(\mathcal O_{X,i}\) with ring maps \(f^{-1}\mathcal O_{X,i'}\to\mathcal O_{X,i}\), and module inverse images \(f^*L=\mathcal O_{X,i}\otimes_{f^{-1}\mathcal O_{X,i'}}f^{-1}L\) for \(f\colon i\to i'\); the same for \(Y\). The inverse image \(u^{-1}\mathcal O_Y\), with levels \(u_i^{-1}\mathcal O_{Y,v(i)}\), is a ring of \(\operatorname{Top}(X)\). We are given a ring map \(\varphi\colon\mathcal O_X\to u^{-1}\mathcal O_Y\). For an \(\mathcal O_Y\)-module \(M\), let \(u^*M\) be the \(u^{-1}\mathcal O_Y\)-module \(u^{-1}M\), regarded as an \(\mathcal O_X\)-module through \(\varphi\). Its levels are \(u_i^*M_{v(i)}\), where \(u_i^*\) is \(u_i^{-1}\) followed by restriction of scalars along \(\varphi_i\). We assume:

**(L)** for every object \(i\) of \(I\), the inverse image of sheaves \(u_i^{-1}\colon Y_{v(i)}\to X_i\) has a left adjoint.

The ring map goes from \(\mathcal O_X\) to \(u^{-1}\mathcal O_Y\), so \(u^*\) is not the module inverse image of a morphism of ringed topoi.

For modules on \(X^{\mathrm{dis}}\), the product of the levels with the rings \(\mathcal O_{X,i}\), the restriction \(e^*\) has the left adjoint \(e_!\) with
\[
(e_!L)_j=\bigoplus_i\ \bigoplus_{g\colon j\to i}g^*L_i ,
\]
by Proposition 4.2 (b) of the lesson on morphisms of fibred topoi. For an object \(k\) of \(J\), we write \(k_!\) for the left adjoint of the level functor \(k^*\) on \(\mathcal O_Y\)-modules, given by the same proposition.

**Lemma 1.2.**

1. Each \(u_i^*\colon\operatorname{Mod}(\mathcal O_{Y,v(i)})\to\operatorname{Mod}(\mathcal O_{X,i})\) has a left adjoint \(u_{i!}\).
2. The functor \(u^*\) is exact, and it has a left adjoint \(u_!\). For a module \(L\) on \(X^{\mathrm{dis}}\),
\[
(u_!e_!L)_j=\bigoplus_i\ \bigoplus_{f\colon j\to v(i)}f^*u_{i!}L_i ,
\]
the module inverse images being those of \(Y\).

**Proof.** (1) This is the proof of Proposition 4.4 (a) of the lesson on morphisms of fibred topoi, with \(u_i\) in place of \(f\): the left adjoint sends the free module on an object \(E\) of \(X_i\) to the free module on its image under the left adjoint of \(u_i^{-1}\), and it is extended to all modules by presentations.

(2) Exactness is checked levelwise, and \(u_i^{-1}\) and restriction of scalars are exact. For a module \(M\) on \(\operatorname{Top}(Y)\), the adjunctions give
\[
\begin{aligned}&\operatorname{Hom}(e_!L,u^*M)\\&\quad=\prod_i\operatorname{Hom}\bigl(L_i,u_i^*M_{v(i)}\bigr)\\&\quad=\prod_i\operatorname{Hom}\bigl(u_{i!}L_i,M_{v(i)}\bigr)\\&\quad=\operatorname{Hom}\Bigl(\bigoplus_iv(i)_!u_{i!}L_i,M\Bigr).\end{aligned}
\]
So \(G(L)=\bigoplus_iv(i)_!u_{i!}L_i\), whose levels are the stated ones, represents \(M\mapsto\operatorname{Hom}(e_!L,u^*M)\); a map \(e_!L'\to e_!L\) induces a map \(G(L')\to G(L)\) by the Yoneda lemma. Every module \(E\) on \(\operatorname{Top}(X)\) has a presentation \(e_!L_1\to e_!L_0\to E\to0\): the counit \(e_!e^*E\to E\) is an epimorphism, since at the level \(j\) its component on the summand of \(\mathrm{id}_j\) is the identity of \(E_j\), and the same applies to its kernel. Put \(u_!E=\operatorname{coker}(G(L_1)\to G(L_0))\). Then
\[
\begin{aligned}\operatorname{Hom}(u_!E,M)&=\ker\bigl(\operatorname{Hom}(e_!L_0,u^*M)\\&\qquad\to\operatorname{Hom}(e_!L_1,u^*M)\bigr)\\&=\operatorname{Hom}(E,u^*M).\end{aligned}
\]
So \(u_!E\) represents \(M\mapsto\operatorname{Hom}(E,u^*M)\), independently of the presentation up to unique isomorphism, and \(u_!e_!=G\). \(\square\)

## 2. Flat modules

Call a module on \(\operatorname{Top}(X)\) *levelwise flat* if all its levels are flat. Tensor products are computed levelwise (Proposition 4.2 (c) of the lesson on morphisms of fibred topoi), so a levelwise flat module is flat.

**Lemma 2.1.**

1. If the components of a module \(L\) on \(X^{\mathrm{dis}}\) are flat, then \(e_!L\) is levelwise flat, and \(e_!\) carries short exact sequences of such modules to short exact sequences.
2. Every module on \(\operatorname{Top}(X)\) is a quotient of a module \(e_!L\) with \(L\) flat.
3. A bounded above exact complex of flat modules on a ringed topos has flat kernels; so it is spliced from short exact sequences of flat modules.

**Proof.** (1) The levels of \(e_!L\) are direct sums of modules \(g^*L_i=\mathcal O_{X,j}\otimes_{g^{-1}\mathcal O_{X,i}}g^{-1}L_i\), which are flat [Stacks, Tag 05VD]. If \(0\to L'\to L\to L''\to0\) is exact with flat terms, then so is \(0\to g^{-1}L'\to g^{-1}L\to g^{-1}L''\to0\), with \(g^{-1}L''\) flat over \(g^{-1}\mathcal O_{X,i}\). Tensoring with \(\mathcal O_{X,j}\) keeps it exact [Stacks, Tag 03EX].

(2) Every module \(E\) is a quotient of \(e_!e^*E\), and \(e^*E\) is a quotient of a free, hence flat, module \(L\); the functor \(e_!\) is right exact.

(3) Let \(F^\bullet\) be exact with flat terms and \(F^n=0\) for \(n>a\). Then \(F^{a-1}\to F^a\) is surjective, and its kernel is flat [Stacks, Tag 03EY]. Descending induction on the degree gives the claim. \(\square\)

## 3. The left derived functor

We assume, in addition to (L):

**(H)** for every object \(j\) of \(J\) and every pair \((i,f)\) of an object \(i\) of \(I\) and an arrow \(f\colon j\to v(i)\), the functor \(f^*u_{i!}\colon\operatorname{Mod}(\mathcal O_{X,i})\to\operatorname{Mod}(\mathcal O_{Y,j})\) carries short exact sequences of flat modules to exact sequences.

**Proposition 3.1.** Let \(F^\bullet\) be a bounded above exact complex of \(\mathcal O_X\)-modules of the form \(e_!P\) with \(P\) flat. Then \(u_!F^\bullet\) is exact.

**Proof.** For each \(m\), form the standard simplicial resolution \((e_!e^*)^{\bullet+1}F^m\to F^m\) of the module \(F^m\), defined by the construction of [Stacks, Tag 08N8] for the adjunction between \(e_!\) and \(e^*\). These form a double complex \(B_{n,m}=(e_!e^*)^{n+1}F^m\), \(n\geq0\).

*The augmentation.* Since \(F^m=e_!P^m\) is in the image of \(e_!\), the augmentation \((e_!e^*)^{\bullet+1}e_!P^m\to e_!P^m\) is a homotopy equivalence of simplicial objects [Stacks, Tag 08ND]. The functor \(u_!\) is additive, so it carries homotopies to homotopies, and \(u_!\) of the augmentation is a homotopy equivalence of simplicial modules. By [Stacks, Tag 019T], the associated chain complex of \(u_!B_{\bullet,m}\) is homotopy equivalent to \(u_!F^m\) in degree \(0\). In each total degree only finitely many \(B_{n,m}\) are nonzero, so the total complex of \(u_!B\) is quasi-isomorphic to \(u_!F^\bullet\) [Stacks, Tag 0132].

*The rows.* We have \(B_{n,\bullet}=e_!(L_n^\bullet)\) with \(L_n^\bullet=e^*(e_!e^*)^nF^\bullet\). By induction on \(n\), using that \(e^*\) is exact and Lemma 2.1 (1), (3), each \(L_n^\bullet\) is a bounded above exact complex of flat modules on \(X^{\mathrm{dis}}\). By Lemma 1.2 (2),
\[
\begin{aligned}&u_!B_{n,\bullet}\\&\quad=\Bigl(\bigoplus_i\ \bigoplus_{f\colon j\to v(i)}f^*u_{i!}(L_n^\bullet)_i\Bigr)_j .\end{aligned}
\]
Split \(L_n^\bullet\) into short exact sequences of flat modules (Lemma 2.1 (3)). By (H), each \(f^*u_{i!}\) keeps them exact, so every row \(u_!B_{n,\bullet}\) is exact. Again only finitely many terms occur in each total degree, so the total complex of \(u_!B\) is exact. Hence \(u_!F^\bullet\) is exact. \(\square\)

**Theorem 3.2.** Assume (L) and (H).

1. The functor \(u_!\) has a left derived functor \(Lu_!\colon D^-(\mathcal O_X)\to D^-(\mathcal O_Y)\), computed by the bounded above complexes of modules of the form \(e_!P\) with \(P\) flat.
2. If \(M^\bullet\) is a bounded above complex of levelwise flat modules, \(Lu_!M^\bullet\) is represented by the total complex of the double complex \(u_!\bigl((e_!e^*)^{n+1}M^m\bigr)\).
3. For \(E\in D^-(\mathcal O_X)\) and \(F\in D^+(\mathcal O_Y)\), there is a canonical isomorphism in \(D(\operatorname{Ab})\)
\[
\begin{gathered}R\operatorname{Hom}(Lu_!E,F)\\ \cong R\operatorname{Hom}(E,u^*F).\end{gathered}
\]

**Proof.** (1) Let \(\mathcal P\) be the set of bounded above complexes of modules \(e_!P\), \(P\) flat. Every bounded above complex receives a quasi-isomorphism from a complex in \(\mathcal P\) [Stacks, Tag 05T7], by Lemma 2.1 (2). If \(s\colon P^\bullet\to P'^\bullet\) is a quasi-isomorphism in \(\mathcal P\), its cone is an exact complex in \(\mathcal P\), since \(e_!P\oplus e_!P'=e_!(P\oplus P')\). By Proposition 3.1, \(u_!\) of the cone, the cone of \(u_!s\), is exact, so \(u_!s\) is a quasi-isomorphism. By [Stacks, Tag 06XN], \(Lu_!\) is everywhere defined on \(D^-(\mathcal O_X)\) and every complex in \(\mathcal P\) computes it.

(2) For each \(m\), the augmented complex \((e_!e^*)^{\bullet+1}M^m\to M^m\) is exact: as in Proposition 2.1 of the lesson on cohomology of total topoi, it becomes contractible after \(e^*\) [Stacks, Tags 08ND, 019T], and \(e^*\) detects exactness. So the total complex of \((e_!e^*)^{n+1}M^m\) is quasi-isomorphic to \(M^\bullet\) [Stacks, Tag 0133]. It is bounded above, and its terms are of the form \(e_!P\) with \(P=e^*(e_!e^*)^nM^m\) levelwise flat, by Lemma 2.1 (1) and induction on \(n\). So it lies in \(\mathcal P\), and (1) applies.

(3) Represent \(E\) by a complex \(P^\bullet\in\mathcal P\) and \(F\) by a bounded below complex of injectives \(I^\bullet\), which is K-injective [Stacks, Tag 070J]. Then \(R\operatorname{Hom}(Lu_!E,F)\) is the Hom complex \(\operatorname{Hom}^\bullet(u_!P^\bullet,I^\bullet)\), and adjunction in each degree identifies it with \(\operatorname{Hom}^\bullet(P^\bullet,u^*I^\bullet)\). It remains to see that this complex represents \(R\operatorname{Hom}(E,u^*F)\). Let \(u^*I^\bullet\to J^\bullet\) be a quasi-isomorphism to a bounded below complex of injectives, and \(C^\bullet\) its cone, an exact bounded below complex. For a term \(e_!L\) of \(P^\bullet\) and \(k\geq1\),
\[
\begin{aligned}&\operatorname{Ext}^k(e_!L,u^*I^q)\\&\quad=\operatorname{Hom}_D\bigl(Lu_!(e_!L),I^q[k]\bigr)\\&\quad=\operatorname{Ext}^k(u_!e_!L,I^q)=0,\end{aligned}
\]
by [Stacks, Tag 0DVC] for the adjoint pair \((u_!,u^*)\), with \(u^*\) exact, by (1), and because \(I^q\) is injective. So \(\operatorname{Ext}^k(e_!L,C^q)=0\) for \(k\geq1\), and by dimension shifting along the short exact sequences of the exact complex \(C^\bullet\), the complexes \(\operatorname{Hom}(e_!L,C^\bullet)\) are exact. Since \(P^\bullet\) is bounded above and \(C^\bullet\) bounded below, each term of \(\operatorname{Hom}^\bullet(P^\bullet,C^\bullet)\) is a finite product, and this complex is exact. So \(\operatorname{Hom}^\bullet(P^\bullet,u^*I^\bullet)\to\operatorname{Hom}^\bullet(P^\bullet,J^\bullet)\) is a quasi-isomorphism, and the target represents \(R\operatorname{Hom}(E,u^*F)\). \(\square\)

**Remark 3.3.** Suppose that every \(f^*u_{i!}\) as in (H) is exact, and that every module inverse image \(g^*\) of \(X\) is exact, for instance when the ring maps of \(X\) are flat. Then the formula of Theorem 3.2 (2) holds for every bounded above complex \(M^\bullet\). Indeed, choose a quasi-isomorphism \(P^\bullet\to M^\bullet\) from a bounded above complex of flat modules. Each functor \(N\mapsto u_!\bigl((e_!e^*)^{n+1}N\bigr)\) is then exact, being built from \(e^*\), the functors \(g^*\), direct sums and the functors \(f^*u_{i!}\) by Lemma 1.2 (2). So it carries \(P^\bullet\to M^\bullet\) to a quasi-isomorphism, and so does the total complex. Without the exactness of the \(g^*\), the terms \((e_!e^*)^{n+1}M\) involve module inverse images of non-flat modules, and this argument does not apply.

## 4. Derived colimits

**Proposition 4.1.** Let \((T,\mathcal O)\) be a ringed topos and \(K\) a small category. Let \(X\) be the constant fibred topos over \(I=K^{\mathrm{op}}\) with value \((T,\mathcal O)\), \(Y=(T,\mathcal O)\) over the one-point category, and \(u\) the identity on every level, with \(\varphi\) the identity. Then \(\operatorname{Mod}(\mathcal O_X)\) is the category of functors \(K\to\operatorname{Mod}(\mathcal O)\), \(u^*\) is the constant functor, \(u_!\) is the colimit over \(K\), and (L), (H) hold. So the derived colimit \(L\varinjlim_K\) on \(D^-(\operatorname{Fun}(K,\operatorname{Mod}(\mathcal O)))\) satisfies
\[
R\operatorname{Hom}\bigl(L\varinjlim_KE,F\bigr)\cong R\operatorname{Hom}(E,cF)
\]
for \(F\in D^+(\mathcal O)\), where \(cF\) is the constant diagram.

**Proof.** An object of \(\operatorname{Top}(X)\) is a functor \(I^{\mathrm{op}}=K\to T\) (Examples 5.2 (c) of the lesson on fibred topoi), and a module over the constant ring is a functor to \(\mathcal O\)-modules. The levels of \(u^*M\) are \(M\) with identity maps, so \(u^*\) is the constant functor, and its left adjoint is the colimit. Every \(u_i\) is the identity, so (L) holds with \(u_{i!}=\mathrm{id}\), and the functors in (H) are identities. Theorem 3.2 applies. The left derived functor of the colimit is unique up to unique isomorphism, so it is the derived colimit of the lesson on derived colimits. \(\square\)

This is the adjunction of Corollary 2.4 of the lesson on derived colimits, in the form of an isomorphism of \(R\operatorname{Hom}\) complexes, for diagrams of modules over a ring of a topos.

## 5. Exercises

**Exercise 5.1.** Suppose all levels of \(X\) and \(Y\) are punctual topoi, \(J\) is the one-point category, and \(Y\) has the ring \(R\). Show that (L) and (H) hold, and that for an \(\mathcal O_X\)-module \(E\), \(u_!E\) is the colimit over \(I^{\mathrm{op}}\) of the functor \(i\mapsto R\otimes_{\mathcal O_{X,i}}E_i\), whose map for \(g\colon i_0\to i_1\) is
\[
\begin{aligned}R\otimes_{\mathcal O_{X,i_1}}E_{i_1}&=R\otimes_{\mathcal O_{X,i_0}}g^*E_{i_1}\\&\longrightarrow R\otimes_{\mathcal O_{X,i_0}}E_{i_0}\end{aligned}
\]
induced by \(E_g\).

**Exercise 5.2.** Show that the flatness in Lemma 2.1 (1) is needed. Take \(I=\{0\to1\}\) with punctual levels, the rings \(\mathcal O_{X,1}=\mathbb Z\), \(\mathcal O_{X,0}=\mathbb Z/2\mathbb Z\), and the short exact sequence \(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2\mathbb Z\to0\) of \(\mathcal O_{X,1}\)-modules at the level \(1\), and zero at the level \(0\).

**Exercise 5.3.** In the situation of Proposition 4.1 with \(T\) punctual, \(\mathcal O=\mathbb Z\) and \(K\) the category with two objects \(0,1\) and two arrows \(a,b\colon1\to0\) besides the identities, compute \(L_n\varinjlim_KE\) for a diagram \(E\) of free abelian groups, and check Theorem 3.2 (3) in degree \(0\) against the universal property of coequalizers.

## 6. Complete solutions

**5.1.** On punctual topoi, the inverse images of sets are identities, so (L) holds, and \(u_i^*\) is restriction of scalars along \(\mathcal O_{X,i}\to R\), whose left adjoint is \(u_{i!}=R\otimes_{\mathcal O_{X,i}}-\). With \(J\) a point, the functors in (H) are the \(u_{i!}\), and tensor products carry short exact sequences of flat modules to exact sequences [Stacks, Tag 03EX]. A map \(u_!E\to N\) is a map \(E\to u^*N\), that is, a family of \(\mathcal O_{X,i}\)-linear maps \(E_i\to N\) compatible with the \(E_g\), that is, a family of \(R\)-linear maps \(R\otimes_{\mathcal O_{X,i}}E_i\to N\) compatible with the maps of the statement. This is the universal property of the colimit. The identification \(R\otimes_{\mathcal O_{X,i_0}}g^*E_{i_1}=R\otimes_{\mathcal O_{X,i_1}}E_{i_1}\) is associativity of tensor products, as \(g^*E_{i_1}=\mathcal O_{X,i_0}\otimes_{\mathcal O_{X,i_1}}E_{i_1}\).

**5.2.** Let \(L\) be the module on \(X^{\mathrm{dis}}\) with \(L_1\) the given sequence and \(L_0=0\). By the formula for \(e_!\) in Section 1.1, the level \(0\) of \(e_!L\) is \(L_0\oplus g^*L_1=\mathbb Z/2\mathbb Z\otimes_{\mathbb Z}L_1\), the arrows with source \(0\) being \(\mathrm{id}_0\) and \(g\colon0\to1\). Tensoring the sequence with \(\mathbb Z/2\mathbb Z\) gives \(\mathbb Z/2\mathbb Z\xrightarrow{0}\mathbb Z/2\mathbb Z\to\mathbb Z/2\mathbb Z\to0\), which is not injective on the left. So \(e_!\) does not carry this short exact sequence, whose last term \(\mathbb Z/2\mathbb Z\) is not flat, to a short exact sequence.

**5.3.** A diagram \(E\) is a pair of maps \(E(a),E(b)\colon E_1\to E_0\), and its colimit is the coequalizer \(E_0/(E(a)-E(b))E_1\). The two-term complex \(E_1\xrightarrow{E(a)-E(b)}E_0\), in homological degrees \(1\) and \(0\), computes \(L\varinjlim_K\). Its homology is a homological \(\delta\)-functor, equal to the colimit in degree \(0\). For an object \(k\), let \(\mathbb Z[K(k,-)]\) be the diagram of free abelian groups on the sets of arrows from \(k\); by the Yoneda lemma, every diagram is a quotient of a direct sum of these. For \(k=1\), the map \(E(a)-E(b)\colon\mathbb Z\to\mathbb Z^{\{a,b\}}\) sends \(1\) to \(a-b\); for \(k=0\), it is the map \(0\to\mathbb Z\). Both are injective, so the homology in degree \(1\) vanishes on direct sums of these diagrams. So the \(\delta\)-functor is coeffaceable, hence universal, by the dual of [Stacks, Tag 010T], and it coincides with \(L_\bullet\varinjlim_K\). So \(L_0\varinjlim E=\operatorname{coker}(E(a)-E(b))\), \(L_1\varinjlim E=\ker(E(a)-E(b))\), and \(L_n=0\) for \(n\geq2\). In degree \(0\), Theorem 3.2 (3) says that maps from the coequalizer to an abelian group \(F\) are the maps \(E_0\to F\) whose composites with \(E(a)\) and \(E(b)\) agree, which are the maps of diagrams \(E\to cF\). This is the universal property of the coequalizer.

## Sources

The functors \(u_!\), their left derived functors and the adjunction formula are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams, where they are proposed for computing cotangent complexes from local factorizations of a morphism. The existence of derived functors through a class of complexes is treated in the Stacks project [Stacks, Tag 06XN]. Standard resolutions go back to Godement's book on sheaf theory.
