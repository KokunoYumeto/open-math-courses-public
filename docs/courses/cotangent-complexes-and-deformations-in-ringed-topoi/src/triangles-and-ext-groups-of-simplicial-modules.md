# Triangles and Ext groups of simplicial modules

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Over a ring, Ext groups and their long exact sequences come from the shift functor and the distinguished triangles of the derived category of complexes. Over a simplicial ring \(A\) there are no complexes to shift. Their role is played by the suspension \(\sigma E\) of a simplicial module, its tensor product with the reduced chains of the simplicial circle. The suspension is fully faithful on \(D_\bullet(A)\), but it is not an equivalence: every suspension has \(\pi_0=0\). This lesson uses it to define the Ext groups of \(A\)-modules, the distinguished triangles of \(D_\bullet(A)\) and their long exact sequences, and it describes \(\operatorname{Ext}^1\) through extensions of simplicial modules. When \(A\) is a ring placed in every degree, normalization identifies all of this with the derived category of modules and its usual sign conventions. The cotangent complex is an object of \(D_\bullet\), and its transitivity triangles and the obstruction classes of deformation theory are triangles and Ext classes of this kind.

**Prerequisites.** [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md); Lemma 1.1 of [*Stable derived functors*](stable-derived-functors.md); Proposition 2.1 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md); Theorems 1.1 and 1.2 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution) and the paragraph after its Theorem 1.3, which turns chain homotopies into simplicial homotopies. From the AI-integrated Stacks project: triangulated categories [[Stacks, Tag 0145](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-triangulated-category), [Tag 014A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-third-isomorphism-triangle), [Tag 0149](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-representable-homological)]; the cone of a map of complexes [[Tag 014L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-the-same-up-to-isomorphisms)] and the triangle of a short exact sequence of complexes [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)]; Ext groups in a derived category [[Tag 06XQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-ext)]; left and right fractions [[Tag 04VD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-left-localization), [Tag 04VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-right-localization)] and additive localizations [[Tag 05QE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-localization-additive)]; adjoint functors [[Tag 07RB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-adjoint-fully-faithful)]; extensions and the Baer sum [[Tag 010K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-definition-ext-group), [Tag 010L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-baer-sum)].

## Conventions

\(T\) is a topos and \(A\) a simplicial ring of \(T\). The notation is that of [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md): \(K\odot E\), \(\underline{\operatorname{Homs}}\), the path module \(\operatorname{Path}(F)\) with its evaluations \(\operatorname{ev}_0,\operatorname{ev}_1\) at the vertices \(e_0,e_1\), the homotopy category \(\operatorname{Hot}_\bullet(A)\), the derived category \(D_\bullet(A)\) and the localization functor \(Q\colon A\text{-}\operatorname{Mod}\to D_\bullet(A)\). For an \(A\)-module \(E\):

- \(\gamma E=(\Delta[1]\odot E)/(e_1\odot E)\) is the cone, with the injection \(i_E\colon E\to\gamma E\) through \(e_0\), and \(\sigma E=\gamma E/E\) is the suspension, with the projection \(v_E\colon\gamma E\to\sigma E\);
- \(PE=\ker(\operatorname{ev}_1\colon\operatorname{Path}(E)\to E)\) is the module of paths ending at \(0\), with the fibration \(\operatorname{ev}_0\colon PE\to E\), and \(\Omega E=\ker(\operatorname{ev}_0\colon PE\to E)\) is the module of loops.

The modules \(\gamma E\) and \(PE\) are homotopy equivalent to \(0\). Write \(\gamma_{\mathbb Z}\) and \(\sigma_{\mathbb Z}\) for the cone and suspension of the constant simplicial abelian group \(\mathbb Z\). Since \(\Delta[1]\odot E\) is the degreewise tensor product \(\mathbb Z^{(\Delta[1])}\otimes E\), we have \(\gamma E=\gamma_{\mathbb Z}\otimes E\) and \(\sigma E=\sigma_{\mathbb Z}\otimes E\), degreewise tensor products over \(\mathbb Z\).

By Theorem 4.2 (1) of the lesson on simplicial rings and modules, the quasi-isomorphisms admit a calculus of left fractions and a calculus of right fractions in \(\operatorname{Hot}_\bullet(A)\). Hence [Stacks, Tags 04VD, 04VH, 05QE] \(D_\bullet(A)\) is additive, and every morphism \(E\to F\) of \(D_\bullet(A)\) can be written \(Q(s)^{-1}Q(f)\), with a map \(f\colon E\to F'\) and a quasi-isomorphism \(s\colon F\to F'\), and also \(Q(g)Q(t)^{-1}\), with a quasi-isomorphism \(t\colon E'\to E\). For maps \(f,g\colon E\to F\), \(Q(f)=Q(g)\) holds if and only if \(sf\simeq sg\) for some quasi-isomorphism \(s\) out of \(F\), and if and only if \(ft\simeq gt\) for some quasi-isomorphism \(t\) into \(E\). We often write \(f\) for \(Q(f)\). The homotopy sheaves \(\pi_n\) are functors on \(D_\bullet(A)\), so a morphism of \(D_\bullet(A)\) is an isomorphism exactly when it induces isomorphisms on all \(\pi_n\).

## 1. Suspension and loops

**1.1. Two exact sequences.** For \(A\)-modules \(E\) and \(F\) there are exact sequences, natural in \(E\) and in \(F\),
\[
\mathsf c_E\colon\ 0\to E\xrightarrow{i_E}\gamma E\xrightarrow{v_E}\sigma E\to0,
\]
\[
0\to\Omega F\to PF\xrightarrow{\operatorname{ev}_0}F\to\pi_0(F)\to0.
\]
The first is split in each degree: in degree \(n\), \(\gamma E\) is a sum of copies of \(E_n\) indexed by the \(n\)-simplices of \(\Delta[1]\) other than the constant simplex at \(1\), and \(E\) is the copy indexed by the constant simplex at \(0\). In the second, \(\operatorname{ev}_0\) is a fibration and \(\pi_0(PF)=0\), so its cokernel is the constant module \(\pi_0(F)\) (Lemma 3.2 (1) of the lesson on simplicial rings and modules). When \(\pi_0(F)=0\) the second sequence is short exact; we call it \(\mathsf f_F\). Since \(\gamma E\) and \(PF\) are acyclic, the long exact sequences give natural isomorphisms
\[
\partial\colon\pi_n(\sigma E)\to\pi_{n-1}(E)\quad(n\geq1),
\]
\[
\partial\colon\pi_{n+1}(F)\to\pi_n(\Omega F)\quad(n\geq0),
\]
and \(\pi_0(\sigma E)=0\) because \((\sigma E)_0=0\) (Lemma 3.5 of the lesson on simplicial rings and modules).

**1.2. Adjunctions.** The bijection \(\operatorname{Hom}_A(\Delta[1]\odot E,F)=\) \(\operatorname{Hom}_A(E,\operatorname{Path}(F))\) restricts to natural bijections
\[
\begin{gathered}\operatorname{Hom}_A(\gamma E,F)\\ =\operatorname{Hom}_A(E,PF),\\ \operatorname{Hom}_A(\sigma E,F)\\ =\operatorname{Hom}_A(E,\Omega F).\end{gathered} \tag{1.2}
\]
Indeed, a map out of \(\Delta[1]\odot E\) factors through \(\gamma E\) exactly when it vanishes on \(e_1\odot E\), that is, when its adjoint has \(\operatorname{ev}_1=0\); it factors through \(\sigma E\) when it vanishes on \(e_0\odot E\) as well. Under the first bijection, composition with \(i_E\) corresponds to composition with \(\operatorname{ev}_0\). So \(\sigma\) is left adjoint to \(\Omega\). Let \(\eta_E\colon E\to\Omega\sigma E\) be the unit and \(\varepsilon_F\colon\sigma\Omega F\to F\) the counit. The unit is adjoint to the projection \(\Delta[1]\odot E\to\sigma E\), and the counit is induced by the evaluation \(\Delta[1]\odot\Omega F\to\Delta[1]\odot\operatorname{Path}(F)\to F\).

**Lemma 1.3.** Let \(\mu\colon\Delta[1]\times\Delta[1]\to\Delta[1]\) be the map induced by \(\max\colon[1]\times[1]\to[1]\) (Proposition 2.1 of the lesson on décalage).

1. There is a map \(b_E\colon\gamma E\to P\sigma E\), natural in \(E\), with \(b_Ei_E=\eta_E\) and \(\operatorname{ev}_0b_E=v_E\). So \((\eta_E,b_E,1)\) is a morphism from \(\mathsf c_E\) to the exact sequence \(0\to\Omega\sigma E\to P\sigma E\to\sigma E\to0\).
2. There is a map \(b'_F\colon\gamma\Omega F\to PF\), natural in \(F\), such that \(b'_Fi_{\Omega F}\) is the inclusion \(\Omega F\subseteq PF\) and \(\operatorname{ev}_0b'_F=\varepsilon_Fv_{\Omega F}\). So \((1,b'_F,\varepsilon_F)\) maps \(\mathsf c_{\Omega F}\) to the second sequence of 1.1.

**Proof.** Write \(\Delta[1]\odot(\Delta[1]\odot E)=(\Delta[1]\times\Delta[1])\odot E\), with the path coordinate \(s\) on the first factor and the cone coordinate \(t\) on the second.

(1) The composite of \(\mu\odot E\colon(\Delta[1]\times\Delta[1])\odot E\to\Delta[1]\odot E\) with the projection to \(\sigma E\) vanishes where \(t=1\), because \(\max(s,1)=1\) and \(e_1\odot E\) maps to \(0\). So it factors through \(\Delta[1]\odot\gamma E\), and its adjoint is a map \(b_E\colon\gamma E\to\operatorname{Path}(\sigma E)\). Where \(s=1\) the composite vanishes too, so \(\operatorname{ev}_1b_E=0\) and \(b_E\) lands in \(P\sigma E\). Where \(s=0\), \(\max(0,t)=t\), so \(\operatorname{ev}_0b_E=v_E\). Where \(t=0\), \(\max(s,0)=s\), so \(b_Ei_E\) is adjoint to the projection \(\Delta[1]\odot E\to\sigma E\): it is \(\eta_E\).

(2) Let \(\operatorname{ev}\colon\Delta[1]\odot\operatorname{Path}(F)\to F\) be the evaluation. The composite
\[
\begin{aligned}&(\Delta[1]\times\Delta[1])\odot\Omega F\\&\quad \xrightarrow{\mu\odot\Omega F}\Delta[1]\odot\Omega F\\&\quad \to\Delta[1]\odot\operatorname{Path}(F) \xrightarrow{\operatorname{ev}}F\end{aligned}
\]
vanishes where \(t=1\), because loops vanish at both ends. It factors through \(\Delta[1]\odot\gamma\Omega F\), with adjoint \(b'_F\colon\gamma\Omega F\to\operatorname{Path}(F)\). Where \(s=1\) it vanishes as well, so \(b'_F\) lands in \(PF\). Where \(s=0\) it is the evaluation of loops at \(t\), which induces \(\varepsilon_F\) on \(\sigma\Omega F\); so \(\operatorname{ev}_0b'_F=\varepsilon_Fv_{\Omega F}\). Where \(t=0\) it is the evaluation at \(s\), whose adjoint is the inclusion \(\Omega F\subseteq\operatorname{Path}(F)\). Every map in the construction is natural. \(\square\)

**Corollary 1.4.** The unit \(\eta_E\) is a quasi-isomorphism for every \(E\). The counit \(\varepsilon_F\) induces isomorphisms on \(\pi_n\) for \(n\geq1\), and it is a quasi-isomorphism if and only if \(\pi_0(F)=0\).

**Proof.** The sequence \(0\to\Omega\sigma E\to P\sigma E\to\sigma E\to0\) is exact, because \(\pi_0(\sigma E)=0\). In the morphism of Lemma 1.3 (1) both middle terms are acyclic, so the connecting maps of the two long exact sequences are isomorphisms, and their naturality gives \(\pi_n(\eta_E)\circ\partial=\partial\) on \(\pi_{n+1}(\sigma E)\). So \(\eta_E\) is a quasi-isomorphism.

For the counit, let \(I\subseteq F\) be the image of \(\operatorname{ev}_0\). Since \(\operatorname{ev}_0b'_F=\varepsilon_Fv_{\Omega F}\) and \(v_{\Omega F}\) is surjective, \(\varepsilon_F\) factors as \(\sigma\Omega F\xrightarrow{\varepsilon'}I\subseteq F\), and \((1,b'_F,\varepsilon')\) maps \(\mathsf c_{\Omega F}\) to the short exact sequence \(0\to\Omega F\to PF\to I\to0\). The same argument shows that \(\varepsilon'\) is a quasi-isomorphism. The cokernel of \(I\subseteq F\) is the constant module \(\pi_0(F)\). So \(I\to F\) induces isomorphisms on \(\pi_n\) for \(n\geq1\), and \(\pi_0(I)=0\). Hence \(\varepsilon_F\) induces isomorphisms on \(\pi_n\) for \(n\geq1\), and it is a quasi-isomorphism exactly when \(\pi_0(F)=\pi_0(\sigma\Omega F)=0\). \(\square\)

**Proposition 1.5.** The functors \(\sigma\) and \(\Omega\) carry quasi-isomorphisms to quasi-isomorphisms. They induce functors \(\sigma,\Omega\colon D_\bullet(A)\to D_\bullet(A)\), and \(\sigma\) is left adjoint to \(\Omega\). The functor \(\sigma\colon D_\bullet(A)\to D_\bullet(A)\) is fully faithful, and its essential image consists of the modules \(F\) with \(\pi_0(F)=0\).

**Proof.** The natural isomorphisms \(\partial\) of 1.1 show that both functors preserve quasi-isomorphisms, so they induce functors on the localization. The unit and the counit are natural transformations between functors preserving quasi-isomorphisms. Their images under \(Q\) are natural with respect to all morphisms of \(D_\bullet(A)\), since naturality with respect to \(Q(s)\) implies naturality with respect to \(Q(s)^{-1}\), and they satisfy the triangle identities because these hold for modules. So \(\sigma\) is left adjoint to \(\Omega\) on \(D_\bullet(A)\). By Corollary 1.4 the unit is an isomorphism, so \(\sigma\) is fully faithful [Stacks, Tag 07RB]. Every \(\sigma E\) has \(\pi_0=0\), and if \(\pi_0(F)=0\) then \(F\cong\sigma\Omega F\) by Corollary 1.4. \(\square\)

## 2. Ext groups

**Definition 2.1.** For \(E,F\in D_\bullet(A)\) and \(p\in\mathbb Z\) put
\[
\begin{aligned}&\operatorname{Ext}^p_A(E,F)\\&\quad =\varinjlim_{n\geq\max(0,-p)}\operatorname{Hom}_{D_\bullet(A)}(\sigma^nE,\sigma^{n+p}F),\end{aligned}
\]
with transition maps \(a\mapsto\sigma(a)\). By Proposition 1.5 these maps are bijective, so \(\operatorname{Ext}^p_A(E,F)\) is the group \(\operatorname{Hom}(\sigma^nE,\sigma^{n+p}F)\) for any admissible \(n\). In particular, for \(p,q\geq0\),
\[
\operatorname{Ext}^p_A(E,F)=\operatorname{Hom}(E,\sigma^pF),
\]
\[
\begin{aligned}&\operatorname{Ext}^{-q}_A(E,F) =\operatorname{Hom}(\sigma^qE,F)\\&\quad =\operatorname{Hom}(E,\Omega^qF).\end{aligned}
\]
These groups are functorial in both variables, contravariantly in \(E\). We write \(\operatorname{Ext}^p\) when \(A\) is clear.

**Proposition 2.2.** Let \(i\geq0\). There are natural isomorphisms

1. \(\operatorname{Ext}^p(\sigma^iE,F)\cong\operatorname{Ext}^{p-i}(E,F)\) and \(\operatorname{Ext}^p(E,\sigma^iF)\cong\operatorname{Ext}^{p+i}(E,F)\);
2. \(\operatorname{Ext}^p(E,\Omega^iF)\cong\operatorname{Ext}^{p-i}(E,\sigma^i\Omega^iF)\).

The counit \(\varepsilon^{(i)}\colon\sigma^i\Omega^iF\to F\) of the adjunction between \(\sigma^i\) and \(\Omega^i\) induces isomorphisms on \(\pi_n\) for \(n\geq i\), and \(\pi_n(\sigma^i\Omega^iF)=0\) for \(n<i\). The map \(\operatorname{Ext}^{p-i}(E,\sigma^i\Omega^iF)\to\operatorname{Ext}^{p-i}(E,F)\) induced by \(\varepsilon^{(i)}\) is bijective if \(p\leq0\), and for every \(p\) if \(\pi_n(F)=0\) for all \(n<i\).

**Proof.** (1) Since \(\sigma^n\sigma^i=\sigma^{n+i}\), both isomorphisms are reindexings of the colimits.

(2) For \(n\geq\max(0,-p,i-p)\), \(\sigma^{n+p}\Omega^iF=\sigma^{n+p-i}(\sigma^i\Omega^iF)\), and \(\operatorname{Hom}(\sigma^nE,\sigma^{n+p-i}(\sigma^i\Omega^iF))\) computes \(\operatorname{Ext}^{p-i}(E,\sigma^i\Omega^iF)\).

The counit \(\varepsilon^{(i)}\) is the composite \(\varepsilon_F\circ\sigma(\varepsilon^{(i-1)}_{\Omega F})\). The statement on \(\pi_n\) follows by induction on \(i\) from Corollary 1.4 and the isomorphisms \(\partial\) of 1.1. If \(\pi_n(F)=0\) for \(n<i\), then \(\varepsilon^{(i)}\) is a quasi-isomorphism. If \(p\leq0\), take \(n=i-p\). An element of \(\operatorname{Ext}^p(E,\Omega^iF)=\operatorname{Hom}(\sigma^{-p}E,\Omega^iF)\) is a morphism \(a\); at level \(n\) it is \(\sigma^i(a)\), and its image under \(\varepsilon^{(i)}\) is \(\varepsilon^{(i)}\sigma^i(a)\in\) \(\operatorname{Hom}(\sigma^{i-p}E,F)=\) \(\operatorname{Ext}^{p-i}(E,F)\). This is the adjunction bijection, so the map induced by \(\varepsilon^{(i)}\) is bijective. \(\square\)

**Remark 2.3.** For \(p>0\) the map induced by \(\varepsilon^{(i)}\) need not be bijective, so \(\operatorname{Ext}^p(E,\Omega^iF)\) and \(\operatorname{Ext}^{p-i}(E,F)\) can differ. Let \(T\) be the topos of sets, \(A=\mathbb Z\) and \(E=F=\mathbb Z\), constant. A path in a constant simplicial set is constant, so \(\Omega\mathbb Z=0\) and \(\operatorname{Ext}^1(\mathbb Z,\Omega\mathbb Z)=0\). But \(\operatorname{Ext}^0(\mathbb Z,\mathbb Z)=\pi_0(\mathbb Z)=\mathbb Z\) by Example 2.5. Part (2) of the proposition gives the correct value, since \(\sigma\Omega\mathbb Z=0\).

**Proposition 2.4 (constant rings).** Let \(A\) be the constant simplicial ring of a ring \(\Lambda\) of \(T\). Identify \(D_\bullet(\Lambda)\) with \(D^{\leq0}(\Lambda)\subseteq D(\Lambda)\) through normalization (Lemma 1.1 of the lesson on stable derived functors), \(N_nE\) being placed in cohomological degree \(-n\). For a simplicial \(\Lambda\)-module \(E\), let \(\theta_E\colon N\sigma E\to(NE)[1]\) be the connecting morphism in \(D(\Lambda)\) of the short exact sequence of complexes \(N(\mathsf c_E)\) [Stacks, Tag 0152].

1. \(\theta_E\) is an isomorphism, natural in \(E\): normalization carries the suspension to the shift.
2. There are isomorphisms \(\operatorname{Ext}^p_\Lambda(E,F)\cong\) \(\operatorname{Hom}_{D(\Lambda)}(NE,(NF)[p])=\) \(\operatorname{Ext}^p_{D(\Lambda)}(NE,NF)\) [Stacks, Tag 06XQ], natural in \(E\) and \(F\).

**Proof.** (1) The connecting morphisms of a δ-functor are natural in the short exact sequence, so \(\theta\) is natural in \(E\). The triangle \((NE,N\gamma E,N\sigma E,\theta_E)\) is distinguished and \(N\gamma E\) is acyclic, so \(\theta_E\) is an isomorphism [Stacks, Tag 0149].

(2) Let \(\Theta_k\colon N\sigma^kX\to(NX)[k]\) be the composite of \(\theta_{\sigma^{k-1}X}\), \(\theta_{\sigma^{k-2}X}[1]\), …, \(\theta_X[k-1]\). For \(a\colon\sigma^nE\to\sigma^{n+p}F\), naturality of \(\theta\) gives
\[
\begin{aligned}&\Theta_{n+p+1}\,N(\sigma a)\,\Theta_{n+1}^{-1}\\&\quad =\bigl(\Theta_{n+p}\,N(a)\,\Theta_n^{-1}\bigr)[1].\end{aligned}
\]
So the bijections \(\operatorname{Hom}(\sigma^nE,\sigma^{n+p}F)\to\) \(\operatorname{Hom}(NE[n],NF[n+p])\to\) \(\operatorname{Hom}(NE,NF[p])\), given by normalization, which is fully faithful, followed by conjugation with \(\Theta\) and the shift by \(-n\), are compatible with the transition maps. \(\square\)

**Example 2.5 (the topos of sets).** Let \(T\) be the topos of sets and \(A\) any simplicial ring. For every \(A\)-module \(F\), \(\operatorname{Hom}_{D_\bullet(A)}(A,F)=\pi_0(F)\). Hence \(\operatorname{Ext}^{-q}_A(A,F)=\pi_q(F)\) for \(q\geq0\), and \(\operatorname{Ext}^p_A(A,F)=0\) for \(p>0\).

**Proof.** An \(A\)-linear map \(\Delta[n]\odot A=A^{(\Delta[n])}\to F\) is an \(n\)-simplex of \(F\). So \(\underline{\operatorname{Homs}}_A(A,F)=F\), and \(\operatorname{Hot}_A(A,F)=\pi_0(F)\) by Lemma 1.1 of the lesson on simplicial rings and modules, naturally in \(F\). A quasi-isomorphism \(s\colon F\to F'\) induces a bijection on \(\pi_0\). So a morphism \(Q(s)^{-1}Q(f)\) with \(f\in\pi_0(F')\) equals \(Q(f_0)\) for \(f_0=\pi_0(s)^{-1}(f)\), because \(f=sf_0\) in \(\operatorname{Hot}_\bullet(A)\). If \(Q(f_0)=0\), then \(sf_0\simeq0\) for some quasi-isomorphism \(s\), so \(\pi_0(s)(f_0)=0\) and \(f_0=0\). Thus \(\pi_0(F)\to\operatorname{Hom}_{D_\bullet(A)}(A,F)\) is bijective. Then \(\operatorname{Ext}^{-q}(A,F)=\) \(\operatorname{Hom}(A,\Omega^qF)=\) \(\pi_0(\Omega^qF)=\) \(\pi_q(F)\), and \(\operatorname{Ext}^p(A,F)=\) \(\operatorname{Hom}(A,\sigma^pF)=\) \(\pi_0(\sigma^pF)=\) \(0\) for \(p>0\). \(\square\)

## 3. Cones and distinguished triangles

For a map \(u\colon E\to F\) of \(A\)-modules, the cone \(C(u)=F\amalg_E\gamma E\) is the cokernel in the exact sequence
\[
\begin{aligned}&0 \to E \xrightarrow{(-i_E,\,u)}\gamma E\oplus F\\&\quad \xrightarrow{\pi}C(u) \to0.\end{aligned} \tag{3.1}
\]
Let \(j\colon F\to C(u)\) be the restriction of \(\pi\) to \(F\), and \(p\colon C(u)\to\sigma E\) the map induced by \(F\to0\), so that \(p\pi=(v_E,0)\). The *fibre* of \(u\) is \(\operatorname{Fib}(u)=E\times_FPF\), the fibre product of \(u\) and \(\operatorname{ev}_0\), with the projection \(q\colon\operatorname{Fib}(u)\to E\). It sits in an exact sequence
\[
\begin{aligned}&0 \to\operatorname{Fib}(u) \to E\oplus PF\\&\quad \xrightarrow{(u,\,-\operatorname{ev}_0)}F\\&\quad \to\operatorname{coker}\pi_0(u) \to0,\end{aligned} \tag{3.2}
\]
because \((u,-\operatorname{ev}_0)\) is a fibration, as \(\operatorname{ev}_0\) is, and \(\pi_0(PF)=0\) (Lemma 3.2 (1) of the lesson on simplicial rings and modules). For \(F=0\), \(C(u)=\sigma E\) and \(p=1\); for \(u=1_E\), \(C(1_E)=\gamma E\). Similarly \(\operatorname{Fib}(0\to F)=\Omega F\) and \(\operatorname{Fib}(1_F)\cong PF\). Both constructions are functorial for commutative squares.

**Definition 3.1.** A *triangle* of \(D_\bullet(A)\) is a sequence \(E\xrightarrow{f}F\xrightarrow{g}G\xrightarrow{h}\sigma E\) of morphisms of \(D_\bullet(A)\). A morphism of triangles is a triple \((a,b,c)\) of morphisms with \(bf=f'a\), \(cg=g'b\) and \(h'c=\sigma(a)h\). The *triangle of* a map \(u\colon E\to F\) of \(A\)-modules is
\[
E\xrightarrow{u}F\xrightarrow{j}C(u)\xrightarrow{-p}\sigma E,
\]
and a triangle is *distinguished* if it is isomorphic to the triangle of some map of \(A\)-modules.

The sign agrees with the convention for complexes in the Stacks project, where the triangle \((K,L,C(f),f,i,-p)\) of a map of complexes is distinguished [Stacks, Tag 014L]. Proposition 3.10 shows that the two notions agree for constant rings, and Corollary 3.6 that the triangle of the sequence \(\mathsf c_E\) has the identity of \(\sigma E\) as third map.

**Lemma 3.2 (exact sequences).** Let \(X=(0\to E\xrightarrow{u}F\xrightarrow{v}G\to0)\) be an exact sequence of \(A\)-modules.

1. The map \(s_X\colon C(u)\to G\) induced by \((0,v)\colon\gamma E\oplus F\to G\) is a quasi-isomorphism, and \(s_Xj=v\).
2. Put \(\chi(X)=-p\,s_X^{-1}\colon G\to\sigma E\) in \(D_\bullet(A)\). The triangle \(\underline\chi(X)=(E,F,G,u,v,\chi(X))\) is distinguished, and every morphism of exact sequences \((a,b,c)\colon X\to X'\) is a morphism of triangles \(\underline\chi(X)\to\underline\chi(X')\).
3. Every distinguished triangle is isomorphic to \(\underline\chi(X)\) for some exact sequence \(X\).

**Proof.** (1) The map \((0,v)\) kills the image \(\{(-i_Ex,ux)\}\) of \(E\). The triple \((1_E,\operatorname{pr}_2,s_X)\) is a morphism from (3.1) to \(X\), and \(\operatorname{pr}_2\colon\gamma E\oplus F\to F\) is a homotopy equivalence, so \(s_X\) is a quasi-isomorphism by the five lemma on the long exact sequences. And \(s_Xj=v\) by construction.

(2) By (1), \((1,1,s_X)\) is an isomorphism from the triangle of \(u\) to \(\underline\chi(X)\); its last square reads \(\chi(X)s_X=-p\). The morphism \((a,b,c)\) induces a map of cones \(C(a,b)\colon C(u)\to C(u')\) with \(s_{X'}C(a,b)=c\,s_X\) and \(p'C(a,b)=\sigma(a)p\). Hence \(\chi(X')c\,s_X=-p'C(a,b)=\sigma(a)\chi(X)s_X\), and \(\chi(X')c=\sigma(a)\chi(X)\).

(3) It suffices to treat the triangle of a map \(u\colon E\to F\). By Proposition 3.3 of the lesson on simplicial rings and modules, \(u=rm\) with \(m\colon E\to M(u)\) a monomorphism and \(r\) a homotopy equivalence. The square \((1_E,r)\) from \(m\) to \(u\) induces a map of cones \(C(m)\to C(u)\), compatible with the maps \(j\) and \(p\), and a quasi-isomorphism by the five lemma applied to the sequences (3.1). So the triangle of \(u\) is isomorphic to the triangle of \(m\), which is isomorphic to \(\underline\chi(X)\) for \(X=(0\to E\to M(u)\to M(u)/E\to0)\), by (2). \(\square\)

**Proposition 3.3 (homotopy sheaves).** Let \((E,F,G,f,g,h)\) be a distinguished triangle. The sequence
\[
\begin{aligned}&\quad \cdots \to\pi_nE \to\pi_nF \to\pi_nG\\&\quad \xrightarrow{\partial\pi_n(h)}\pi_{n-1}E \to\cdots\\&\quad \quad \to\pi_0F \to\pi_0G \to0\end{aligned}
\]
is exact, where \(\partial\) is the isomorphism \(\pi_n(\sigma E)\to\pi_{n-1}(E)\) of 1.1. If \(B\to A\) is a map of simplicial rings, restriction of scalars carries distinguished triangles of \(D_\bullet(A)\) to distinguished triangles of \(D_\bullet(B)\).

**Proof.** By naturality of \(\partial\), isomorphic triangles give isomorphic sequences, so by Lemma 3.2 (3) we may take \(\underline\chi(X)\). Write \(\delta_Y\) for the connecting maps of the long exact sequence of homotopy sheaves of an exact sequence \(Y\). The morphisms \((1,\operatorname{pr}_2,s_X)\colon(3.1)\to X\) and \((-1,\operatorname{pr}_1,p)\colon(3.1)\to\mathsf c_E\) give \(\delta_X\pi_n(s_X)=\delta_{(3.1)}\) and \(\partial\pi_n(p)=-\delta_{(3.1)}\). Hence \(\delta_X=-\partial\pi_n(p)\pi_n(s_X)^{-1}=\partial\pi_n(\chi(X))\), and the sequence is the long exact sequence of \(X\). Restriction of scalars commutes with \(\gamma\), \(\sigma\), sums and pushouts. So it carries the triangle of \(u\) over \(A\) to the triangle of \(u\) over \(B\), and it preserves quasi-isomorphisms. \(\square\)

**Proposition 3.4.** Let \(u\colon E\to F\) be a map of \(A\)-modules, with \(j\colon F\to C(u)\) and \(p\colon C(u)\to\sigma E\) as above, and let \(k\colon C(u)\to C(j)\) and \(q\colon C(j)\to\sigma F\) be the corresponding maps for \(j\). The map \(\lambda\colon C(j)=C(u)\amalg_F\gamma F\to\sigma E\), equal to \(p\) on \(C(u)\) and to \(0\) on \(\gamma F\), is a quasi-isomorphism, \(\lambda k=p\), and \(\sigma(u)\lambda\simeq-q\).

**Proof.** \(\lambda\) is well defined because \(pj=0\). The sequence \(0\to F\xrightarrow{j}C(u)\xrightarrow{p}\sigma E\to0\) is exact, as (3.1) shows, and its pushout along \(i_F\) is an exact sequence \(0\to\gamma F\to C(j)\xrightarrow{\lambda}\sigma E\to0\). Since \(\gamma F\) is acyclic, \(\lambda\) is a quasi-isomorphism. Clearly \(\lambda k=p\).

*The case \(u=1_F\).* Then \(C(u)=\gamma F\), \(j=i_F\), and \(C(i_F)=(\gamma F\oplus\gamma F)/\{(-i_Fx,i_Fx)\}\), the first summand being the cone of \(j\). The maps \(\lambda\) and \(q\) are induced by \(v_F\) on the second and on the first summand. These modules and maps are obtained from the case \(F=\mathbb Z\) in the topos of sets by the degreewise tensor product \(\otimes_{\mathbb Z}F\): the sequence \(0\to\mathbb Z\to\gamma_{\mathbb Z}\oplus\gamma_{\mathbb Z}\to C(i_{\mathbb Z})\to0\) is split in each degree, so it stays exact. A homotopy \(\Delta[1]\odot C(i_{\mathbb Z})\to\sigma_{\mathbb Z}\) from \(\lambda+q\) to \(0\) gives, after tensoring with \(F\), an \(A\)-linear homotopy, because \((\Delta[1]\odot C)\otimes F=\Delta[1]\odot(C\otimes F)\). By the Dold–Kan correspondence and the passage from chain homotopies to simplicial homotopies (Theorem 1.2 of *The cotangent complex* and the paragraph after its Theorem 1.3), it suffices to show that \(N(\lambda+q)\) is null-homotopic.

By Theorem 1.1 of *The cotangent complex*, \(N_m\gamma_{\mathbb Z}\) is isomorphic to the quotient of \((\gamma_{\mathbb Z})_m\) by the degenerate simplices, which is free on the nondegenerate \(m\)-simplices of \(\Delta[1]\) other than the vertex \(1\): the vertex \(0\) for \(m=0\), the edge \((01)\) for \(m=1\), and none for \(m\geq2\). The \(1\)-simplices of \(\Delta[1]\) are \((00)\), \((01)\) and \((11)\), and \((11)\) is zero in \(\gamma_{\mathbb Z}\). So \(N\gamma_{\mathbb Z}\) is \(\mathbb Z\epsilon\) in degree \(1\), with \(\epsilon=(01)-(00)\), and \(\mathbb Ze_0\) in degree \(0\), with \(d\epsilon=d_0\epsilon=-e_0\), since \(d_0(01)\) is the vertex \(1\). Hence \(NC(i_{\mathbb Z})\) is \(\mathbb Z\epsilon_1\oplus\mathbb Z\epsilon_2\) in degree \(1\) and \(\mathbb Z\bar e\) in degree \(0\), the two copies of \(e_0\) being identified, with \(d(x\epsilon_1+y\epsilon_2)=-(x+y)\bar e\). And \(N\sigma_{\mathbb Z}=\mathbb Z\bar\epsilon\) in degree \(1\), with \(N(q)(x\epsilon_1+y\epsilon_2)=x\bar\epsilon\) and \(N(\lambda)(x\epsilon_1+y\epsilon_2)=y\bar\epsilon\). The map \(h(\bar e)=-\bar\epsilon\) from degree \(0\) to degree \(1\) satisfies \(hd=N(\lambda+q)\) in degree \(1\), and \(dh=0=N(\lambda+q)\) in degree \(0\). So \(\lambda+q\simeq0\).

*The general case.* The commutative square \((u,1_F)\) from \(u\) to \(1_F\) induces \(c_0\colon C(u)\to C(1_F)=\gamma F\), equal to \(\gamma(u)\) on \(\gamma E\) and to \(i_F\) on \(F\), with \(c_0j=i_F\). Together with the identity of \(\gamma F\) it induces \(c\colon C(j)\to C(i_F)\). On \(C(u)\), \(v_Fc_0=\sigma(u)p\). So \(\lambda_1c=\sigma(u)\lambda\) and \(q_1c=q\), where \(\lambda_1\) and \(q_1\) are the maps for \(1_F\). Hence \(\sigma(u)\lambda=\lambda_1c\simeq-q_1c=-q\). \(\square\)

**Corollary 3.5 (rotation).** If \((E,F,G,f,g,h)\) is distinguished, so is \((F,G,\sigma E,g,h,-\sigma(f))\).

**Proof.** We may assume that the triangle is the triangle of \(u\colon E\to F\). By Proposition 3.4, \((1,1,-\lambda)\) is an isomorphism from the triangle \((F,C(u),C(j),j,k,-q)\) of \(j\) to \((F,C(u),\sigma E,j,-p,-\sigma(u))\): indeed \(-\lambda k=-p\) and \((-\sigma(u))(-\lambda)=\sigma(u)\lambda=-q\) in \(D_\bullet(A)\). \(\square\)

**Corollary 3.6.** For every \(A\)-module \(E\), \(\chi(\mathsf c_E)=1_{\sigma E}\): the triangle \((E,\gamma E,\sigma E,i_E,v_E,1)\) is distinguished. If \(\pi_0(F)=0\), then \(\chi(\mathsf f_F)=\varepsilon_F^{-1}\).

**Proof.** For \(X=\mathsf c_E\), the cone \(C(i_E)\) and its maps are those of the case \(u=1_E\) in the proof of Proposition 3.4: \(s_X\) is \(\lambda_1\) and \(p\) is \(q_1\). So \(\chi(\mathsf c_E)=-q_1\lambda_1^{-1}=1\). By Lemma 1.3 (2), \((1,b'_F,\varepsilon_F)\) is a morphism from \(\mathsf c_{\Omega F}\) to \(\mathsf f_F\). By Lemma 3.2 (2), \(\chi(\mathsf f_F)\varepsilon_F=\chi(\mathsf c_{\Omega F})=1\), and \(\varepsilon_F\) is invertible in \(D_\bullet(A)\) by Corollary 1.4. \(\square\)

**Lemma 3.7.** Let \(E\xrightarrow{f}F\xrightarrow{g}G\) be maps of \(A\)-modules. The following are equivalent:

1. \(gf\simeq0\);
2. \(g=g'j\) for some \(g'\colon C(f)\to G\);
3. \(f=qf'\) for some \(f'\colon E\to\operatorname{Fib}(g)\).

**Proof.** A homotopy from \(gf\) to \(0\) is a map \(\Delta[1]\odot E\to G\) equal to \(gf\) on \(e_0\odot E\) and to \(0\) on \(e_1\odot E\), that is, a map \(H\colon\gamma E\to G\) with \(Hi_E=gf\). By (1.2) it is also a map \(H'\colon E\to PG\) with \(\operatorname{ev}_0H'=gf\). Homotopy is a symmetric relation (Lemma 1.1 of the lesson on simplicial rings and modules). Given \(H\), the map \((H,g)\colon\gamma E\oplus F\to G\) kills \(\{(-i_Ex,fx)\}\) and induces \(g'\) with \(g'j=g\). Given \(H'\), the pair \((f,H')\) is a map \(f'\colon E\to F\times_GPG=\operatorname{Fib}(g)\) with \(qf'=f\). Conversely, \(jf\simeq0\), since \(jf=\kappa i_E\) for the map \(\kappa\colon\gamma E\to C(f)\) induced by the first summand, and \(\gamma E\) is homotopy equivalent to \(0\). And \(gq\simeq0\), since \(gq=\operatorname{ev}_0\operatorname{pr}_2\) with \(\operatorname{pr}_2\colon\operatorname{Fib}(g)\to PG\), and \(PG\) is homotopy equivalent to \(0\). So (2) and (3) each imply (1). \(\square\)

**Proposition 3.8.** Let \((E,F,G,f,g,h)\) be a distinguished triangle and \(M\in D_\bullet(A)\). The sequences of groups of morphisms of \(D_\bullet(A)\)
\[
\begin{aligned}&\operatorname{Hom}(G,M) \xrightarrow{g^*}\operatorname{Hom}(F,M)\\&\quad \xrightarrow{f^*}\operatorname{Hom}(E,M),\end{aligned}
\]
\[
\begin{aligned}&\operatorname{Hom}(M,E) \xrightarrow{f_*}\operatorname{Hom}(M,F)\\&\quad \xrightarrow{g_*}\operatorname{Hom}(M,G)\end{aligned}
\]
are exact. The same holds for the diagram \(\sigma^nE\to\sigma^nF\to\sigma^nG\), for every \(n\geq0\).

**Proof.** Both statements depend only on the isomorphism class of the diagram \(E\to F\to G\).

*The first sequence.* Take the triangle of \(u\colon E\to F\). The composite \(ju\) is null-homotopic by Lemma 3.7. Let \(a\colon F\to M\) satisfy \(au=0\). Write \(a=Q(s)^{-1}Q(a')\), with \(a'\colon F\to M'\) and a quasi-isomorphism \(s\colon M\to M'\). Then \(Q(a'u)=0\), so \(ta'u\simeq0\) for a quasi-isomorphism \(t\colon M'\to M''\). By Lemma 3.7, \(ta'=bj\) for some \(b\colon C(u)\to M''\), and \(a=Q(ts)^{-1}Q(b)\circ j\).

*The second sequence.* By Lemma 3.2 (3) take \(\underline\chi(X)\) with \(X=(0\to E\xrightarrow{u}F\xrightarrow{v}G\to0)\). Let \(\iota\colon E\to\operatorname{Fib}(v)\) be \(x\mapsto(ux,0)\). Since \(v\) is surjective, (3.2) for \(v\) is a short exact sequence \(0\to\operatorname{Fib}(v)\to F\oplus PG\to G\to0\), and \((\iota,\operatorname{in}_1,1_G)\) is a morphism from \(X\) to it. Its middle term is a homotopy equivalence, so \(\iota\) is a quasi-isomorphism. Since \(q\iota=u\), the diagram \(E\to F\to G\) is isomorphic to \(\operatorname{Fib}(v)\xrightarrow{q}F\xrightarrow{v}G\), whose composite is null-homotopic by Lemma 3.7. Let \(b\colon M\to F\) satisfy \(vb=0\). Write \(b=Q(b')Q(t)^{-1}\), with \(b'\colon M'\to F\) and a quasi-isomorphism \(t\colon M'\to M\). Then \(Q(vb')=0\), so \(vb't'\simeq0\) for a quasi-isomorphism \(t'\colon M''\to M'\), and \(b't'=qc\) for some \(c\colon M''\to\operatorname{Fib}(v)\) by Lemma 3.7. So \(b=q\circ Q(c)Q(tt')^{-1}\).

*Suspensions.* The functor \(\sigma=\sigma_{\mathbb Z}\otimes-\) preserves pushouts, and the exchange of factors \(\sigma_{\mathbb Z}\otimes\gamma_{\mathbb Z}\cong\gamma_{\mathbb Z}\otimes\sigma_{\mathbb Z}\) of the degreewise tensor product gives an isomorphism \(\sigma C(u)\cong C(\sigma u)\) carrying \(\sigma(j)\) to the map \(j\) of \(\sigma u\). So \(\sigma E\to\sigma F\to\sigma C(u)\) is isomorphic to the beginning of the triangle of \(\sigma u\), and induction on \(n\) gives the last statement. \(\square\)

**Theorem 3.9 (long exact sequences).** Let \((E,F,G,f,g,h)\) be a distinguished triangle and \(M\in D_\bullet(A)\). The sequences
\[
\begin{aligned}&\quad \cdots \to\operatorname{Ext}^p(G,M)\\&\quad \xrightarrow{g^*}\operatorname{Ext}^p(F,M)\\&\quad \xrightarrow{f^*}\operatorname{Ext}^p(E,M)\\&\quad \quad \xrightarrow{\partial}\operatorname{Ext}^{p+1}(G,M) \to\cdots,\end{aligned}
\]
\[
\begin{aligned}&\quad \cdots \to\operatorname{Ext}^p(M,E)\\&\quad \xrightarrow{f_*}\operatorname{Ext}^p(M,F)\\&\quad \xrightarrow{g_*}\operatorname{Ext}^p(M,G)\\&\quad \quad \xrightarrow{\partial}\operatorname{Ext}^{p+1}(M,E) \to\cdots\end{aligned}
\]
are exact. Here \(\partial\) is \(\operatorname{Ext}^p(E,M)\cong\operatorname{Ext}^{p+1}(\sigma E,M)\) followed by \(h^*\), respectively \(h_*\) followed by \(\operatorname{Ext}^p(M,\sigma E)\cong\operatorname{Ext}^{p+1}(M,E)\), with the isomorphisms of Proposition 2.2 (1).

**Proof.** At level \(n\), exactness at \(\operatorname{Ext}^p(F,M)\) and at \(\operatorname{Ext}^p(M,F)\) is Proposition 3.8 for \(\sigma^n\) of the triangle with target \(\sigma^{n+p}M\), respectively for \(\sigma^{n+p}\) of the triangle with source \(\sigma^nM\). By Corollary 3.5, the triangles \((F,G,\sigma E,g,h,-\sigma f)\) and \((G,\sigma E,\sigma F,h,-\sigma f,-\sigma g)\) are distinguished. The first gives exactness at \(\operatorname{Ext}^{p+1}(G,M)\) and at \(\operatorname{Ext}^p(M,G)\). The second gives exactness at \(\operatorname{Ext}^{p+1}(\sigma E,M)\cong\operatorname{Ext}^p(E,M)\) and at \(\operatorname{Ext}^p(M,\sigma E)\cong\operatorname{Ext}^{p+1}(M,E)\), because under the isomorphisms of Proposition 2.2 (1) the maps \((\sigma f)^*\) and \((\sigma f)_*\) become \(f^*\) and \(f_*\). \(\square\)

**Proposition 3.10 (constant rings).** Let \(A\) be the constant simplicial ring of a ring \(\Lambda\), with the notation of Proposition 2.4. For a triangle \(X=(E,F,G,f,g,h)\) of \(D_\bullet(\Lambda)\) put \(NX=\) \((NE,NF,NG,Nf,Ng,\theta_E\,N(h))\).

1. For an exact sequence \(X\) of simplicial \(\Lambda\)-modules, \(\theta_E\,N(\chi(X))\) is the connecting morphism of the short exact sequence of complexes \(N(X)\) [Stacks, Tag 0152].
2. A triangle \(X\) is distinguished if and only if \(NX\) is distinguished in \(D(\Lambda)\).

**Proof.** (1) Write \(\delta_Y\) for the connecting morphism of \(N(Y)\). The morphisms \((1,\operatorname{pr}_2,s_X)\colon(3.1)\to X\) and \((-1,\operatorname{pr}_1,p)\colon(3.1)\to\mathsf c_E\) give \(\delta_XN(s_X)=\delta_{(3.1)}\) and \(\theta_EN(p)=-\delta_{(3.1)}\). Hence \(\theta_EN(\chi(X))=-\theta_EN(p)N(s_X)^{-1}=\delta_X\).

(2) By (1) and [Stacks, Tag 0152], \(N\underline\chi(X)\) is distinguished for every exact sequence \(X\). By Lemma 3.2 (3) and the naturality of \(\theta\), \(NX\) is distinguished whenever \(X\) is. Conversely, let \(NX\) be distinguished. Write \(f=Q(u)Q(t)^{-1}\), with \(u\colon E'\to F\) and a quasi-isomorphism \(t\colon E'\to E\). Then \((t,1,1)\) is an isomorphism to \(X\) from \(X'=(E',F,G,u,g,\sigma(t)^{-1}h)\), so \(NX'\) is distinguished. Let \(Y\) be the triangle of \(u\). The distinguished triangles \(NY\) and \(NX'\) have the same first morphism, so there is an isomorphism of triangles \((1,1,\varphi)\colon NY\to NX'\) [Stacks, Tags 0145, 014A]. Normalization is fully faithful on \(D_\bullet(\Lambda)\), so \(\varphi=N(\varphi')\) for an isomorphism \(\varphi'\colon C(u)\to G\). The equalities \(\varphi'j=g\) and \(\sigma(t)^{-1}h\varphi'=-p\) hold because their images under \(N\) hold, for the second after composition with the isomorphism \(\theta_{E'}\). So \(X\cong X'\cong Y\) is distinguished. \(\square\)

## 4. Extensions and the first Ext group

For \(A\)-modules \(G\) and \(E\), let \(\operatorname{Ext}_{A\text{-}\mathrm{Mod}}(G,E)\) be the group of isomorphism classes of extensions of \(G\) by \(E\) in the abelian category of \(A\)-modules, with the Baer sum [Stacks, Tags 010K, 010L]. For \(g\colon G'\to G\) and \(f\colon E\to E'\) write \(Xg\) for the pullback and \(fX\) for the pushout of an extension \(X\).

**Lemma 4.1.** The rule \(X\mapsto\chi(X)\) defines a homomorphism
\[
\begin{aligned}&\chi \colon\operatorname{Ext}_{A\text{-}\mathrm{Mod}}(G,E) \to\operatorname{Ext}^1_A(G,E)\\&\quad =\operatorname{Hom}_{D_\bullet(A)}(G,\sigma E),\end{aligned}
\]
with \(\chi(Xg)=\chi(X)g\) and \(\chi(fX)=\sigma(f)\chi(X)\). It vanishes on split extensions.

**Proof.** An isomorphism of extensions is a morphism \((1,b,1)\), so \(\chi(X)\) depends only on the class of \(X\), by Lemma 3.2 (2). The morphisms \((1,b,g)\colon Xg\to X\) and \((f,b,1)\colon X\to fX\) give the two formulas. Cones, \(s_X\) and \(p\) commute with direct sums, so \(\chi(X\oplus X')=\chi(X)\oplus\chi(X')\). The Baer sum is \(\nabla(X\oplus X')\Delta\), with \(\Delta\) the diagonal of \(G\) and \(\nabla\) the sum map of \(E\). Hence \(\chi(X+X')=\) \(\sigma(\nabla)(\chi(X)\oplus\chi(X'))\Delta=\) \(\chi(X)+\chi(X')\). A split extension is the zero of the group. \(\square\)

**Lemma 4.2.** Let \(X=(0\to F\xrightarrow{i}M\xrightarrow{w}E\to0)\) be an exact sequence of \(A\)-modules. The following are equivalent:

1. \(\chi(X)=0\);
2. there is a quasi-isomorphism \(s\colon E'\to E\) such that \(Xs\) splits;
3. there is a quasi-isomorphism \(t\colon F\to F'\) such that \(tX\) splits.

**Proof.** If \(tX\) splits, then \(\sigma(t)\chi(X)=\chi(tX)=0\), and \(\sigma(t)\) is invertible, so \(\chi(X)=0\); in the same way (2) implies (1). Let \(\chi(X)=0\).

(1)⇒(3). By Corollary 3.5 applied twice, \((E,\sigma F,\sigma M,\chi(X),-\sigma i,-\sigma w)\) is distinguished. By Proposition 3.8, \(\operatorname{Hom}(\sigma M,\sigma F)\to\) \(\operatorname{Hom}(\sigma F,\sigma F)\to\) \(\operatorname{Hom}(E,\sigma F)\) is exact, and \(1_{\sigma F}\) maps to \(\chi(X)=0\). So \(1_{\sigma F}=b\circ(-\sigma i)\) for some \(b\). Since \(\sigma\) is fully faithful, \(b=-\sigma(r)\) for a morphism \(r\colon M\to F\) with \(ri=1_F\). Write \(r=Q(t)^{-1}Q(r')\), with \(r'\colon M\to F'\) and a quasi-isomorphism \(t\colon F\to F'\). Then \(Q(r'i)=Q(t)\), so \(t''r'i\simeq t''t\) for a quasi-isomorphism \(t''\colon F'\to F''\). The map \(t_1=t''r'i\) is homotopic to a quasi-isomorphism, hence a quasi-isomorphism, and \(t_1X=(t''r')(iX)\). The extension \(iX=(0\to M\to M\amalg_FM\to E\to0)\) splits: the sum of the two copies of \(M\) is a retraction. So \(t_1X\) splits.

(1)⇒(2). By Corollary 3.5, \((M,E,\sigma F,w,\chi(X),-\sigma i)\) is distinguished, and by Proposition 3.8 the sequence \(\operatorname{Hom}(E,M)\to\) \(\operatorname{Hom}(E,E)\to\) \(\operatorname{Hom}(E,\sigma F)\) is exact. So \(1_E=wr\) for some \(r\colon E\to M\) in \(D_\bullet(A)\). Write \(r=Q(r')Q(s)^{-1}\), with \(r'\colon E'\to M\) and a quasi-isomorphism \(s\colon E'\to E\). Then \(Q(wr')=Q(s)\), so \(wr's''\simeq ss''\) for a quasi-isomorphism \(s''\). The map \(s_1=wr's''\) is a quasi-isomorphism, and \(Xs_1=(Xw)(r's'')\) splits, because \(Xw=(0\to F\to M\times_EM\to M\to0)\) has the diagonal as a section. \(\square\)

**Proposition 4.3.** Let \(E,F\) be \(A\)-modules and \(u\in\operatorname{Ext}^1_A(E,F)\).

1. There are a quasi-isomorphism \(t\colon F\to F'\) and an extension \(X\) of \(E\) by \(F'\) with \(\sigma(t)^{-1}\chi(X)=u\). There are also a quasi-isomorphism \(s\colon E'\to E\) and an extension \(Y\) of \(E'\) by \(F\) with \(\chi(Y)s^{-1}=u\).
2. Let \(t'\colon F\to F'\) and \(t''\colon F\to F''\) be quasi-isomorphisms, and \(X'\), \(X''\) extensions of \(E\) by \(F'\), \(F''\). Then \(\sigma(t')^{-1}\chi(X')=\sigma(t'')^{-1}\chi(X'')\) if and only if there are quasi-isomorphisms \(r'\colon F'\to H\) and \(r''\colon F''\to H\) with \(r't'\simeq r''t''\) and \(r'X'=r''X''\) in \(\operatorname{Ext}_{A\text{-}\mathrm{Mod}}(E,H)\).
3. Let \(s'\colon E'\to E\) and \(s''\colon E''\to E\) be quasi-isomorphisms, and \(Y'\), \(Y''\) extensions of \(E'\), \(E''\) by \(F\). Then \(\chi(Y')s'^{-1}=\chi(Y'')s''^{-1}\) if and only if there are quasi-isomorphisms \(r'\colon D\to E'\) and \(r''\colon D\to E''\) with \(s'r'\simeq s''r''\) and \(Y'r'=Y''r''\) in \(\operatorname{Ext}_{A\text{-}\mathrm{Mod}}(D,F)\).

**Proof.** (1) Write \(u=Q(s)^{-1}Q(f)\), with \(f\colon E\to G\) and a quasi-isomorphism \(s\colon\sigma F\to G\). Then \(\pi_0(G)=\pi_0(\sigma F)=0\), so \(\mathsf f_G\) is an extension of \(G\) by \(\Omega G\). Put \(X=\mathsf f_Gf\) and \(t=\Omega(s)\eta_F\colon F\to\Omega G\), a quasi-isomorphism by Corollary 1.4 and Proposition 1.5. By Lemma 4.1 and Corollary 3.6, \(\chi(X)=\varepsilon_G^{-1}f\). Naturality of \(\varepsilon\) and a triangle identity give
\[
\begin{aligned}&\varepsilon_G\,\sigma(t) =\varepsilon_G\,\sigma\Omega(s)\,\sigma(\eta_F)\\&\quad =s\,\varepsilon_{\sigma F}\,\sigma(\eta_F) =s.\end{aligned}
\]
Hence \(\sigma(t)^{-1}\chi(X)=(\varepsilon_G\sigma(t))^{-1}f=s^{-1}f=u\). For the second statement, write \(u=Q(f)Q(s)^{-1}\), with \(f\colon E'\to\sigma F\) and a quasi-isomorphism \(s\colon E'\to E\), and put \(Y=\mathsf c_Ff\). By Corollary 3.6, \(\chi(Y)=\chi(\mathsf c_F)f=f\), so \(\chi(Y)s^{-1}=u\).

(2) If \(r'\) and \(r''\) exist, then \(\sigma(r')\chi(X')=\) \(\chi(r'X')=\) \(\chi(r''X'')=\) \(\sigma(r'')\chi(X'')\) and \(r't'=r''t''\) in \(D_\bullet(A)\). So
\[
\begin{aligned}&\sigma(t')^{-1}\chi(X')\\&\quad =\sigma(r't')^{-1}\sigma(r')\chi(X')\\&\quad =\sigma(r''t'')^{-1}\sigma(r'')\chi(X'')\\&\quad =\sigma(t'')^{-1}\chi(X'').\end{aligned}
\]
Conversely, the left Ore condition gives quasi-isomorphisms \(r'_1\colon F'\to H_1\) and \(r''_1\colon F''\to H_1\) with \(r'_1t'\simeq r''_1t''\). Then \(\chi(r'_1X')=\sigma(r'_1t')\,\sigma(t')^{-1}\chi(X')\), and the same expression for \(X''\) has the same value. So \(\chi(r'_1X'-r''_1X'')=0\), and Lemma 4.2 gives a quasi-isomorphism \(q\colon H_1\to H\) such that \(q(r'_1X'-r''_1X'')\) splits. Put \(r'=qr'_1\) and \(r''=qr''_1\).

(3) In the same way, with the right Ore condition and Lemma 4.2 (2). \(\square\)

**Proposition 4.4 (true triangles).** Call a morphism of short exact sequences of \(A\)-modules a quasi-isomorphism if its three components are, and call two morphisms \(X\rightrightarrows Y\) homotopic if they are joined by a morphism of exact sequences \(\Delta[1]\odot X\to Y\). Let \(VT_\bullet(A)\), the category of *true triangles*, be the localization of the category of short exact sequences of \(A\)-modules at the quasi-isomorphisms.

1. Every morphism of \(VT_\bullet(A)\) has the form \(Q(s)^{-1}Q(f)\), with \(f\) a morphism and \(s\) a quasi-isomorphism of exact sequences, and \(Q(f)=Q(g)\) if and only if \(sf\simeq sg\) for some quasi-isomorphism \(s\).
2. \(\underline\chi\) induces a functor from \(VT_\bullet(A)\) to the category of distinguished triangles of \(D_\bullet(A)\). It is essentially surjective and conservative.

**Proof.** (1) The proofs of Lemmas 1.1 and 1.2 and of the left half of Theorem 4.2 (1) of the lesson on simplicial rings and modules apply to short exact sequences, componentwise. They use the functors \(K\odot-\), quotients by \(K'\odot-\) for simplicial subsets \(K'\subseteq K\), and contractions and homotopies induced by maps of simplicial sets, which carry short exact sequences to short exact sequences and morphisms to morphisms. They also use cokernels of monomorphisms and pushouts along monomorphisms. For these, regard an exact sequence as a three-term complex. If \(0\to X\to Z\to W\to0\) is exact in each place and two of the three-term complexes \(X,Z,W\) are short exact sequences, then so is the third, by the long exact homology sequence. The cokernel of a componentwise monomorphism \(X\to Z\) is such a \(W\). A pushout \(Y\amalg_XZ\) of a componentwise monomorphism \(X\to Z\) sits in a sequence \(0\to Y\to Y\amalg_XZ\to W\to0\) of this kind.

(2) By Lemma 3.2 (2), \(\underline\chi\) is a functor. It carries quasi-isomorphisms to isomorphisms of triangles and homotopic morphisms to equal ones, so it factors through \(VT_\bullet(A)\). It is essentially surjective by Lemma 3.2 (3). If \(\underline\chi(Q(s)^{-1}Q(f))\) is an isomorphism, so is \(\underline\chi(Q(f))\). Its components are the images of the components of \(f\) in \(D_\bullet(A)\), which are therefore quasi-isomorphisms, and \(Q(s)^{-1}Q(f)\) is an isomorphism. \(\square\)

## 5. Exercises

**5.1.** Show that the triangles \((0,F,F,0,1,0)\), \((E,E,0,1,0,0)\) and \((E,0,\sigma E,0,0,\pm1)\) are distinguished.

**5.2.** Let \((E,F,G,f,g,h)\) be a distinguished triangle. Show that \(f\) is an isomorphism if and only if \(G\cong0\). Show that if \(h=0\), then \(g\) has a right inverse \(r\colon G\to F\) in \(D_\bullet(A)\), and \((f,r)\colon E\oplus G\to F\) is an isomorphism.

**5.3.** Let \(T\) be the topos of sets, \(A=\mathbb Z\), and \(X=(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2\to0)\), an exact sequence of constant simplicial abelian groups. Show that \(\chi(X)\neq0\).

## 6. Complete solutions

**5.1.** The exact sequences \(0\to0\to F\xrightarrow{1}F\to0\) and \(0\to E\xrightarrow{1}E\to0\to0\) give the first two triangles by Lemma 3.2 (2); their third maps go to or from \(\sigma0=0\) and \(0\). By Corollary 3.6, \((E,\gamma E,\sigma E,i_E,v_E,1)\) is distinguished. Since \(\gamma E\cong0\) in \(D_\bullet(A)\), \(v_E=0\) there, and \((1,\gamma E\to0,1)\) is an isomorphism to \((E,0,\sigma E,0,0,1)\). Finally \((-1,1,1)\) is an isomorphism from \((E,0,\sigma E,0,0,1)\) to \((E,0,\sigma E,0,0,-1)\): its last square reads \((-1)\cdot1=\sigma(-1)\cdot1\).

**5.2.** By Proposition 3.3, \(\pi_*(f)\) is bijective if and only if \(\pi_*(G)=0\); a morphism of \(D_\bullet(A)\) is an isomorphism exactly when it induces isomorphisms on all \(\pi_n\), and \(G\cong0\) exactly when \(\pi_*(G)=0\). If \(h=0\), apply Proposition 3.8 to the distinguished triangle \((F,G,\sigma E,g,h,-\sigma f)\) of Corollary 3.5 and \(M=G\): the sequence \(\operatorname{Hom}(G,F)\to\) \(\operatorname{Hom}(G,G)\to\) \(\operatorname{Hom}(G,\sigma E)\) is exact, and \(1_G\) maps to \(h=0\), so \(1_G=gr\) for some \(r\). Since \(h=0\), the maps \(\partial\pi_n(h)\) of Proposition 3.3 vanish, so \(0\to\pi_nE\to\pi_nF\to\pi_nG\to0\) is exact for every \(n\), and \(\pi_n(r)\) splits it. Hence \(\pi_n(f,r)\colon\pi_nE\oplus\pi_nG\to\pi_nF\) is bijective for every \(n\), and \((f,r)\) is an isomorphism.

**5.3.** Suppose \(\chi(X)=0\). By Lemma 4.2 there is a quasi-isomorphism \(t\colon\mathbb Z\to F'\) such that \(tX=(0\to F'\to M'\to\mathbb Z/2\to0)\) splits. The long exact sequence of homotopy groups of \(tX\) begins with \(\pi_1(\mathbb Z/2)=0\), so \(0\to\pi_0F'\to\pi_0M'\to\mathbb Z/2\to0\) is exact, and it splits because \(tX\) does. The morphism \(X\to tX\) induces on \(\pi_0\) a morphism of exact sequences from \(X\) (whose terms equal their \(\pi_0\)) to this sequence, with outer components \(\pi_0(t)\), an isomorphism, and the identity of \(\mathbb Z/2\). By the five lemma it is an isomorphism, so \(X\) splits. But \(\mathbb Z\) has no element of order \(2\). So \(\chi(X)\neq0\).

## Sources

The suspension and loop functors of simplicial modules and their adjunction belong to the classical homotopy theory of simplicial objects. Over a simplicial ring of a topos, the Ext groups defined through the suspension, the distinguished triangles and their long exact sequences, the description of \(\operatorname{Ext}^1\) by extensions up to quasi-isomorphism and the category of true triangles are due to Illusie, in his work on the cotangent complex. The sign conventions for triangles follow those of the Stacks project for complexes.
