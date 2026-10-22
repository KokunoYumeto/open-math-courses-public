# The co-Lie complex of a group scheme

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The co-Lie complex of a group scheme \(G\) over \(S\), flat and locally of finite presentation, is the derived pullback of its cotangent complex along the unit section. It is a perfect complex on \(S\) with tor amplitude in \([-1,0]\). Its cohomology in degree \(0\) is the module of invariant differential forms, its cohomology in degree \(-1\) vanishes exactly when \(G\) is smooth, and its dual, the Lie complex, governs the deformations of \(G\). This lesson proves its basic properties: it is the co-Lie complex of \(G\) viewed as a torsor over \(S\), it depends contravariantly on \(G\) and commutes with base change, and an exact sequence of group schemes \(1\to G\to H\to K\to1\) gives a distinguished triangle \(\ell_K\to\ell_H\to\ell_G\to\ell_K[1]\). The triangle computes the co-Lie complexes of the groups of roots of unity and of Frobenius kernels.

**Prerequisites.** [*Torsors, co-Lie complexes and the Atiyah class*](torsors-co-lie-complexes-and-the-atiyah-class.md) (Definition 1.1, Lemma 1.2, Proposition 1.3, Theorem 3.3, Propositions 3.4 and 3.5); [*Flat group schemes are local complete intersections*](flat-group-schemes-are-local-complete-intersections.md) (Theorem 3.1, Corollary 3.2); [*Deformations of diagrams of schemes*](deformations-of-diagrams-of-schemes.md) (Conventions, Propositions 1.3 and 1.4). From the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex#2-independence-of-the-resolution): Theorem 2.2, Theorem 6.1 and formula (7.3) of [Theorem 7.2](course:AG-HP/the-cotangent-complex#7-complete-intersections-and-computations). From the AI-integrated Stacks project: duals of perfect complexes [[Stacks, Tag 08DQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-dual-perfect-complex)]; tor amplitude and pullback [[Tag 08H5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-tor-amplitude-pullback), [Tag 0D6D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-pullback-composition)]; smooth morphisms [[Tag 01V8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-flat-smooth-fibres), [Tag 02G1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-omega-finite-locally-free)]; differentials at a rational point [[Tag 0B2D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-tangent-space-cotangent-space)]; relative Frobenius and differentials [[Tag 0CCC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-relative-frobenius-omega)]; triangles [[Tag 05QR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-third-object-zero), [Tag 05QT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-split), [Tag 0149](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-representable-homological)].

## Conventions

\(S\) is a scheme and \(G\) a group scheme over \(S\), flat and locally of finite presentation, with structure morphism \(\pi\colon G\to S\), unit \(e\colon S\to G\) and multiplication \(m\). Cotangent complexes of morphisms of schemes are those of Section 10 of *The cotangent complex*, on Zariski sites. A homomorphism \(u\colon G\to H\) of group schemes over \(S\) satisfies \(ue_G=e_H\). The notions of torsor and co-Lie complex of a torsor are those of [*Torsors, co-Lie complexes and the Atiyah class*](torsors-co-lie-complexes-and-the-atiyah-class.md); \(G\) acts on itself by left multiplication, and \(\pi\colon G\to S\) is then the trivial \(G_S\)-torsor, with the section \(e\).

## 1. Definition and first properties

**Definition 1.1.** The *co-Lie complex* of \(G\) is
\[
\ell_G=Le^*L_{G/S}\in D(\mathcal O_S),
\]
and its *Lie complex* is \(\ell_G^\vee=R\mathcal Hom(\ell_G,\mathcal O_S)\). The *co-Lie module* is \(\omega_G=e^*\Omega_{G/S}\), and \(\operatorname{Lie}(G)=\mathcal Hom(\omega_G,\mathcal O_S)\).

**Proposition 1.2.**

1. \(\ell_G\) is perfect with tor amplitude in \([-1,0]\), and \(\ell_G^\vee\) is perfect with tor amplitude in \([0,1]\). Locally on \(S\), \(\ell_G\) is a complex of finite free modules in degrees \(-1\) and \(0\).
2. \(H^0(\ell_G)=\omega_G\).
3. \(\ell_G\) is the co-Lie complex \(\ell_{G/S}\) of the trivial torsor \(\pi\colon G\to S\): the isomorphism \(\ell_{G/S}\cong Le^*L_{G/S}\) of Theorem 3.3 (1) of the lesson on torsors, for the section \(e\), identifies them. In particular \(a^*\ell_G\cong L_{N(G,G)/N(G,S)}\) for the augmentation \(a\colon N(G,G)\to S\), and \(\ell_G\cong R\varepsilon_*f^G_*t_{[n}L^G_{G/S}\) for \(n\leq-1\). The same holds for \(G\) acting on itself by right multiplication, a torsor under the opposite group \(G^{\mathrm o}\), with the same section \(e\).

**Proof.** (1) By Theorem 3.1 of [*Flat group schemes are local complete intersections*](flat-group-schemes-are-local-complete-intersections.md), \(L_{G/S}\) is locally a complex of finite free modules in degrees \(-1\) and \(0\); its derived pullback along \(e\) is locally such a complex [Tag 08H5], since every point of \(S\) has an open neighbourhood \(V\) with \(e(V)\) inside an open of \(G\) where \(L_{G/S}\) has this form. The dual of a perfect complex is perfect [Tag 08DQ], and locally it is the dual complex of finite free modules, in degrees \(0\) and \(1\).

(2) \(L_{G/S}\in D^{\leq0}\) with \(H^0=\Omega_{G/S}\) (Theorem 6.1 of *The cotangent complex*), and for objects of \(D^{\leq0}\), \(H^0(Le^*K)=e^*H^0(K)\) ((0.1) of the lesson on deformations of diagrams).

(3) This is Theorem 3.3 (1) of the lesson on torsors, for the torsor \(\pi\) and its section \(e\), together with its Proposition 3.5 (1); the argument does not depend on which of the two actions is used. \(\square\)

**Proposition 1.3 (functoriality).** A homomorphism \(u\colon G\to H\) of group schemes over \(S\), both flat and locally of finite presentation, gives a map
\[
\begin{aligned}&\ell(u) \colon\ell_H =Le_G^*Lu^*L_{H/S}\\&\quad \longrightarrow Le_G^*L_{G/S} =\ell_G,\end{aligned}
\]
\(Le_G^*\) of the functoriality map \(Lu^*L_{H/S}\to L_{G/S}\) of the square formed by \(u\) and the identity of \(S\), through \(Le_G^*Lu^*=Le_H^*\) [Tag 0D6D]. Then \(\ell(\mathrm{id})=\mathrm{id}\) and \(\ell(vu)=\ell(u)\circ\ell(v)\) for \(v\colon H\to K\). On \(H^0\), \(\ell(u)\) is the map \(\omega_H\to\omega_G\) induced on differentials.

**Proof.** Functoriality maps compose (Theorem 2.2 of *The cotangent complex*), and so do the identifications of derived pullbacks. On \(H^0\) the functoriality map is the map of differentials (Theorem 6.1 there). \(\square\)

**Proposition 1.4 (base change).** Let \(g\colon S'\to S\) be a morphism, \(G'=G\times_SS'\) and \(g'\colon G'\to G\) the projection.

1. The functoriality map \(Lg'^*L_{G/S}\to L_{G'/S'}\) is an isomorphism.
2. It induces an isomorphism \(Lg^*\ell_G\cong\ell_{G'}\), through \(Le_{G'}^*Lg'^*=Lg^*Le_G^*\).
3. In particular, for \(s\in S\) and \(i_s\colon\operatorname{Spec}\kappa(s)\to S\), \(Li_s^*\ell_G\cong\ell_{G_s}\).

**Proof.** (1) The square formed by \(g'\), \(g\) and the structure morphisms is cartesian, and \(G\) is flat over \(S\), so this is Proposition 1.4 of the lesson on deformations of diagrams. (2) Apply \(Le_{G'}^*\), with \(g'e_{G'}=e_Gg\). (3) is (2) for \(g=i_s\). \(\square\)

So \(\ell_{G'}^\vee\cong Lg^*\ell_G^\vee\) as well, duals of perfect complexes commuting with derived pullback.

**Proposition 1.5 (smoothness).** \(G\) is smooth over \(S\) if and only if \(\ell_G\) has tor amplitude in \([0,0]\), that is, \(\ell_G\cong\omega_G[0]\) with \(\omega_G\) finite locally free.

**Proof.** If \(G\) is smooth, \(L_{G/S}\cong\Omega_{G/S}[0]\) with \(\Omega_{G/S}\) finite locally free (Propositions 5.1 and 10.1 of *The cotangent complex*, [Tag 02G1]), so \(\ell_G=e^*\Omega_{G/S}[0]\). Conversely, let \(\ell_G\) have tor amplitude in \([0,0]\). For \(s\in S\), the fibre \(G_s\) is a group scheme over \(\kappa(s)\), and \(\ell_{G_s}\cong Li_s^*\ell_G\) (Proposition 1.4 (3)) has no cohomology in degree \(-1\). By Corollary 3.2 of the lesson on flat group schemes, \(G_s\) is smooth over \(\kappa(s)\). As \(G\to S\) is flat and locally of finite presentation with smooth fibres, it is smooth [Tag 01V8]. \(\square\)

## 2. Exact sequences

A sequence \(1\to G\xrightarrow{\iota}H\xrightarrow{\rho}K\to1\) of group schemes over \(S\), flat and locally of finite presentation, is *exact* if \(\iota\) identifies \(G\) with the kernel \(H\times_{K,e_K}S\) of \(\rho\), and \(\rho\) is an epimorphism of sheaves for the fpqc topology: for every scheme \(V\) over \(S\) and \(k\in K(V)\) there is an fpqc covering \(\{V_i\to V\}\) with points \(h_i\in H(V_i)\), \(\rho(h_i)=k|_{V_i}\).

**Lemma 2.1.** In an exact sequence, \(\rho\colon H\to K\) is a \(G_K\)-torsor for the action of \(G\) on \(H\) by left multiplication, \(g\cdot h=\iota(g)h\). In particular \(\rho\) is syntomic and faithfully flat.

**Proof.** The action is over \(K\), as \(\rho(\iota(g)h)=\rho(h)\). The morphism \(G\times_SH\to H\times_KH\), \((g,h)\mapsto(\iota(g)h,h)\), has the inverse \((h',h)\mapsto(h'h^{-1},h)\): a point \(h'h^{-1}\) with \(\rho(h'h^{-1})=e\) is a point of the kernel \(G\). Applying the exactness to \(V=K\) and \(k=\mathrm{id}_K\) gives an fpqc covering \(\{K_i\to K\}\) over which \(\rho\) has sections. So \(\rho\) is a torsor (Definition 1.1 of the lesson on torsors), and it is syntomic and faithfully flat by Proposition 1.3 (1) there. \(\square\)

**Proposition 2.2 (the triangle of an exact sequence).** For an exact sequence \(1\to G\xrightarrow{\iota}H\xrightarrow{\rho}K\to1\) of group schemes over \(S\), flat and locally of finite presentation, there is a distinguished triangle
\[
\begin{aligned}&\ell_K \xrightarrow{\ \ell(\rho)\ }\ell_H \xrightarrow{\ \ell(\iota)\ }\ell_G\\&\quad \longrightarrow\ell_K[1]\end{aligned} \tag{2.1}
\]
in \(D(\mathcal O_S)\), natural in the exact sequence.

**Proof.** Apply \(Le_H^*\) to the transitivity triangle of \(H\xrightarrow{\rho}K\to S\) (Proposition 1.3 of the lesson on deformations of diagrams):
\[
\begin{aligned}&Le_H^*L\rho^*L_{K/S}\to Le_H^*L_{H/S}\\&\quad\to Le_H^*L_{H/K}\to Le_H^*L\rho^*L_{K/S}[1].\end{aligned}
\]
Since \(\rho e_H=e_K\), the first term is \(Le_K^*L_{K/S}=\ell_K\) [Tag 0D6D], and the first map is \(\ell(\rho)\) (Proposition 1.3). The second term is \(\ell_H\). The square formed by \(\iota\colon G\to H\), \(e_K\colon S\to K\), \(\rho\) and \(\pi_G\) is cartesian, \(G\) being the kernel, and \(\rho\) is flat (Lemma 2.1); so the functoriality map \(L\iota^*L_{H/K}\to L_{G/S}\) is an isomorphism (Proposition 1.4 of the lesson on deformations of diagrams). With \(\iota e_G=e_H\), the third term is \(Le_G^*L\iota^*L_{H/K}\cong Le_G^*L_{G/S}=\ell_G\). The composite of the functoriality maps \(L\iota^*L_{H/S}\to L\iota^*L_{H/K}\to L_{G/S}\) is the functoriality map of \(\iota\) over \(S\) (Theorem 2.2 of *The cotangent complex*), so the second map becomes \(\ell(\iota)\). Naturality follows from the naturality of transitivity triangles and of functoriality maps. \(\square\)

**Corollary 2.3.** In an exact sequence as above, there is a long exact sequence
\[
\begin{aligned}&0 \to H^{-1}(\ell_K) \to H^{-1}(\ell_H)\\&\quad \to H^{-1}(\ell_G) \to\omega_K \to\omega_H\\&\quad \to\omega_G \to0,\end{aligned}
\]
and \(\ell(\rho)\) is an isomorphism if and only if \(\ell_G=0\), that is, if and only if \(G\) is étale over \(S\).

**Proof.** The long exact sequence of (2.1) [Tag 0149], with \(H^i=0\) outside \([-1,0]\). The third vertex of a distinguished triangle vanishes if and only if the first map is an isomorphism [Tag 05QR]. Finally \(\ell_G=0\) if and only if \(G\) is smooth with \(\omega_G=0\) (Proposition 1.5), that is, smooth with \(\Omega_{G/S}=\pi^*\omega_G=0\), which is étale. \(\square\)

## 3. Examples

**Example 3.1 (smooth groups).** For \(\mathbf G_{a,S}=\operatorname{Spec}\mathcal O_S[x]\), \(\ell=\mathcal O_S\,dx\) in degree \(0\); for \(\mathbf G_{m,S}=\operatorname{Spec}\mathcal O_S[t,t^{-1}]\), \(\ell=\mathcal O_S\,dt\) in degree \(0\), the value at \(t=1\) of the invariant form \(dt/t\).

**Example 3.2 (roots of unity).** Let \(n\geq1\) and \(\mu_n=\operatorname{Spec}\mathcal O_S[t]/(t^n-1)\). By formula (7.3) of *The cotangent complex*, \(L_{\mu_n/S}\) is locally \([B\bar e\to B\,dt]\), \(\bar e\mapsto nt^{n-1}dt\), with \(\bar e\) the class of \(t^n-1\), and pulling back along \(t=1\),
\[
\ell_{\mu_n}\cong\bigl[\mathcal O_S\xrightarrow{\ n\ }\mathcal O_S\bigr]
\]
in degrees \(-1,0\). The exact Kummer sequence \(1\to\mu_n\to\mathbf G_m\xrightarrow{n}\mathbf G_m\to1\) gives the same answer through Proposition 2.2: the \(n\)-th power map multiplies \(dt/t\) by \(n\), so \(\ell(n)\) is multiplication by \(n\) on \(\mathcal O_S\) (Exercise 4.1).

**Example 3.3 (Frobenius kernel of the additive group).** Let \(S\) have characteristic \(p\), and \(\alpha_p=\operatorname{Spec}\mathcal O_S[x]/(x^p)\), the kernel of \(F\colon\mathbf G_a\to\mathbf G_a\), \(x\mapsto x^p\). The sequence \(1\to\alpha_p\to\mathbf G_a\xrightarrow{F}\mathbf G_a\to1\) is exact: \(F\) corresponds to \(\mathcal O_S[y]\to\mathcal O_S[x]\), \(y\mapsto x^p\), which makes \(\mathcal O_S[x]\) free with basis \(1,x,\ldots,x^{p-1}\), so \(F\) is a finite locally free surjection, and every point of \(\mathbf G_a\) has \(p\)-th roots fppf locally. Since \(d(x^p)=0\), \(\ell(F)=0\), and the triangle (2.1) splits [Tag 05QT]:
\[
\ell_{\alpha_p}\cong\mathcal O_S\oplus\mathcal O_S[1].
\]
The same follows from formula (7.3) of *The cotangent complex* applied to \(x^p\), whose derivative vanishes.

## 4. Exercises

**4.1.** Prove the claims of Example 3.2: that the Kummer sequence is exact for the fppf topology, hence for fpqc; that \(\ell(n)\) is multiplication by \(n\); and that (2.1) gives \(\ell_{\mu_n}\cong[\mathcal O_S\xrightarrow{n}\mathcal O_S]\).

**4.2.** Let \(G\) be a finite group, viewed as the constant group scheme \(G_S\) over \(S\). Show that \(\ell_{G_S}=0\). Deduce from Corollary 2.3 that for an exact sequence \(1\to G_S\to H\to K\to1\) with \(G\) finite constant, \(\ell(\rho)\colon\ell_K\to\ell_H\) is an isomorphism.

**4.3.** Let \(k\) be a field. Show that \(\dim_kH^{-1}(\ell_G)-\dim_kH^0(\ell_G)=\) \(-\dim G\) for every group scheme \(G\) locally of finite type over \(k\), and compute both dimensions for \(\mu_n\) when \(\operatorname{char}k=p\) divides \(n\).

## 5. Complete solutions

**4.1.** The \(n\)-th power map of \(\mathbf G_m\) corresponds to \(\mathcal O_S[s,s^{-1}]\to\mathcal O_S[t,t^{-1}]\), \(s\mapsto t^n\), which makes \(\mathcal O_S[t,t^{-1}]\) a free module with basis \(1,t,\ldots,t^{n-1}\). So it is finite locally free and surjective, an fppf covering, and every point \(c\in\mathbf G_m(V)\) has an \(n\)-th root after the base change \(V\times_{\mathbf G_m}\mathbf G_m\to V\), an fppf covering. Its kernel is \(\operatorname{Spec}\mathcal O_S[t,t^{-1}]/(t^n-1)=\mu_n\), as \(t\) is invertible modulo \(t^n-1\). By Example 3.1, \(\ell_{\mathbf G_m}\) is free on the class of \(dt\) at \(t=1\), and the pullback of \(ds\) is \(d(t^n)=nt^{n-1}dt\), which is \(n\,dt\) at \(t=1\). So \(\ell(n)\) is multiplication by \(n\) on \(\mathcal O_S\). The triangle (2.1) is \(\mathcal O_S\xrightarrow{n}\mathcal O_S\to\ell_{\mu_n}\to\mathcal O_S[1]\), so \(\ell_{\mu_n}\) is the cone of multiplication by \(n\), the complex \([\mathcal O_S\xrightarrow{n}\mathcal O_S]\) in degrees \(-1,0\).

**4.2.** \(G_S\) is a disjoint union of copies of \(S\), so \(G_S\to S\) is étale and \(L_{G_S/S}=0\) (Propositions 5.1 and 10.1 of *The cotangent complex*), hence \(\ell_{G_S}=0\). Corollary 2.3 gives the rest.

**4.3.** By Proposition 1.2 (1), \(\ell_G\) is a perfect complex of \(k\)-vector spaces with cohomology in degrees \(-1,0\), and by Corollary 3.2 of the lesson on flat group schemes, \(\dim H^0=\dim\operatorname{Lie}(G)\) and \(\dim H^{-1}=\dim\operatorname{Lie}(G)-\dim G\); the difference is \(-\dim G\). For \(\mu_n\) with \(p\mid n\), Example 3.2 gives \([k\xrightarrow{0}k]\): both dimensions are \(1\), and \(\dim\mu_n=0\).

## Sources

The co-Lie complex of a finite flat group scheme over an affine base and the triangle of an exact sequence are due to Mazur and Roberts; the co-Lie complex of a flat group scheme locally of finite presentation over an arbitrary base and its interpretation through torsors are due to Illusie, in his work on the cotangent complex.
