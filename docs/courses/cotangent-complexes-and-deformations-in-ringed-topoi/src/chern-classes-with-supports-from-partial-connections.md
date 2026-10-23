# Chern classes with supports from partial connections

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A module with a connection has vanishing Chern classes of positive degree in Hodge cohomology. A connection given only on an open subset \(U\), or only along a quotient of the differentials, still constrains the Chern classes: some Chern polynomials come from cohomology with supports in the complement \(Y\) of \(U\). This lesson constructs such classes for a module \(E\) of bounded perfect amplitude on a ringed space, equipped with a *partial connection* on \(U\), relative to a derivation \(\mathrm d\colon B\to\Omega\) into a locally free module of finite rank, for instance the universal derivation into the module of differentials, or the differential of a smooth morphism of complex spaces. The construction takes place on a topos \(\operatorname{Top}^{\mathrm o}(i)\) whose objects are a sheaf on \(U\), a sheaf on the whole space and a map between them; its cohomology with coefficients \((0\to F)\) is the cohomology of \(F\) with supports in \(Y\). The lesson proves:

- the cohomology of \(\operatorname{Top}^{\mathrm o}(i)\) with coefficients \((i^*F\to F)\), \((G\to0)\) and \((0\to F)\) is \(R\Gamma(X,F)\), \(R\Gamma(U,G)\) and \(R\Gamma_Y(X,F)\);
- a partial connection relative to an exact sequence \(0\to L\to\Omega|_U\to M\to0\) is the same as a map \(E|_U\to M\otimes E|_U\) satisfying the Leibniz rule along \(\Omega\to M\); it defines a class \(\operatorname{at}(E,D)\) on \(\operatorname{Top}^{\mathrm o}(i)\) with coefficients in \((L\to\Omega)\), which restricts on \(X\) to the class of the principal parts of \(E\) relative to \(\mathrm d\);
- the Chern classes \(c^n(E,D)\in\) \(H^n(\operatorname{Top}^{\mathrm o}(i),(\Lambda^nL\to\Omega^n))\) lift the Chern classes of \(E\) relative to \(\mathrm d\), which for the universal derivation are its Chern classes in Hodge cohomology; every polynomial in them that is isobaric of weight \(n>r\), where \(L\) is locally a direct summand of a free module of rank \(r\), is a class in \(H^n_Y(X,\Omega^n)\) lifting the same polynomial in the Chern classes of \(E\);
- for Bott's partial connection on the quotient \(N\) of the tangent module by a submodule that is closed under the bracket on \(U\), with \(N\) of bounded perfect amplitude, the Chern polynomials of \(N\) of weight larger than its rank on \(U\) come from cohomology with supports in \(Y\), and they vanish when \(U\) is the whole space;
- for a morphism of complex spaces, the principal parts of order one, formed on the diagonal of the fibre product, are the principal parts of the differential; the Chern classes of the sheaves of rings, carried to the differential forms of the complex space, satisfy the Whitney formula, are functorial, and for an invertible module come from \(\gamma\mapsto\gamma^{-1}\mathrm d\gamma\); for smooth morphisms the localized classes apply.

**Prerequisites.** [*Chern classes of perfect complexes*](chern-classes-of-perfect-complexes.md) (the conventions, Propositions 1.5 and 1.6, Definition 2.2, Propositions 2.3 and 2.4, Corollary 2.5); [*The Atiyah class of filtered complexes*](the-atiyah-class-of-filtered-complexes.md) (the conventions on \(\kappa\) and on triangles, Definition 4.1); [*L-series of endomorphisms of perfect complexes*](l-series-of-endomorphisms-of-perfect-complexes.md) (Definitions 1.1 and 3.1, Propositions 1.2, 1.3 and 3.2 (1), (3)); [*The Atiyah class of a module*](the-atiyah-class-of-a-module.md) (Definition 1.1, Lemma 1.2, Proposition 3.2); [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Theorem 3.2); [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md) (Theorem 2.6); [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Example 1.2 (c), Definition 2.1, Propositions 2.2, 3.1 (2) and 5.1, Theorem 4.3); [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md) (Section 4.3); [*Perfect filtered complexes and duality*](perfect-filtered-complexes-and-duality.md) (Definition 1.1). For Section 5: [*Cartan's coherence theorem and complex spaces*](course:complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces#3-complex-spaces) (Definition 3.1); [*Complex analytic spaces and analytification*](course:AG-QC/complex-analytic-spaces-and-analytification#1-analytic-equations-and-their-sheaves) (Section 1: morphisms through holomorphic coordinate representatives); [*Holomorphic functions of several variables*](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables#1-polydiscs-and-the-definition-of-holomorphy) (Definition 1.1); [*Coherent sheaves and Oka's theorem*](course:complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem#2-oka-s-coherence-theorem) (Theorem 2.1); the module of differentials of a map of sheaves of rings [[Tag 08RM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-universal-module)]. From the AI-integrated Stacks project: cohomology with support in a closed subset [[Stacks, Tag 0A39](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-cohomology-support)]; restrictions of injective sheaves to open subsets [[Tag 01E1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cohomology-of-open)] and the surjectivity of their restriction maps [[Tag 01EA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-injective-restriction-surjective)]; right adjoints of exact functors preserve injectives [[Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)]; acyclic resolutions compute derived functors [[Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity)]; morphisms into bounded below complexes of injectives [[Tag 05TG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-into-injective-complex)]; cohomology of modules and of abelian sheaves [[Tag 03FD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-cohomology-modules-abelian-agree)]; K-flat resolutions [[Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution)]; the triangle of a short exact sequence [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)]; the snake lemma [[Tag 010H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-snake)]; strictly perfect complexes [[Tag 08FL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-strictly-perfect)]; cohomology of quasi-coherent modules on affine schemes [[Tag 01XB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-coherent-affine-cohomology-zero)], for Exercise 5.4.

## Conventions

\(X\) is a topological space, \(i\colon U\to X\) the inclusion of an open subset and \(Y=X\smallsetminus U\); we write \(X\) and \(U\) also for the topoi of sheaves on them, and \(i^*F=F|_U\). For an abelian sheaf \(F\) on \(X\), \(\Gamma_Y(X,F)\) is the group of sections with support in \(Y\), that is, the kernel of the restriction \(\Gamma(X,F)\to\Gamma(U,F)\); \(R\Gamma_Y(X,-)\colon D^+(X)\to D^+(\mathrm{Ab})\) is its right derived functor, computed with bounded below complexes of injective abelian sheaves, and \(H^n_Y(X,-)=H^nR\Gamma_Y(X,-)\) [Tag 0A39]. For a ringed topos \((T,O)\) and \(K\in D(O)\), \(H^n(T,K)=\operatorname{Hom}_{D(O)}(O,K[n])\). Short exact sequences of complexes give triangles with the connecting morphism of [Tag 0152], and \(\kappa\colon(K\otimes E)[1]\to E\otimes K[1]\) is the isomorphism of the conventions of the lesson on the Atiyah class of filtered complexes; for a flat module \(K\) and a module \(E\), both in degree \(0\), it is \(k\otimes m\mapsto m\otimes k\).

## 1. The topos of an open subset and its complement

**Definition 1.1.** Let \(\operatorname{Top}^{\mathrm o}(i)\) be the category whose objects are triples \((G,F,\gamma)\), with \(G\) a sheaf on \(U\), \(F\) a sheaf on \(X\) and \(\gamma\colon G\to i^*F\) a morphism, written \((G\xrightarrow{\gamma}F)\) or \((G\to F)\); a morphism \((G,F,\gamma)\to(G',F',\gamma')\) is a pair of morphisms \(a\colon G\to G'\), \(b\colon F\to F'\) with \(\gamma'\circ a=i^*(b)\circ\gamma\).

Let \(e_X\) be the final object of \(X\) and \(V\subseteq e_X\) the subsheaf represented by \(U\). The localized topos \(X/V\) is the topos of sheaves on \(U\), and the localization morphism \(X/V\to X\) has inverse image \(i^*\). The diagram \(V\to e_X\), indexed by \(\{0\to1\}\), is a fibred topos with levels \(U\) and \(X\) (Example 1.2 (c) of the lesson on fibred topoi), and \(\operatorname{Top}^{\mathrm o}\) of this fibred topos is the category of Definition 1.1 (Definition 2.1 (2) there).

**Proposition 1.2.**

1. \(\operatorname{Top}^{\mathrm o}(i)\) is a topos, in which limits and colimits are computed levelwise. A morphism whose two components are isomorphisms is an isomorphism.
2. The functors \(\varepsilon_U^{-1}(G,F,\gamma)=G\) and \(\varepsilon_X^{-1}(G,F,\gamma)=F\) are the inverse images of morphisms of topoi \(\varepsilon_U\colon U\to\operatorname{Top}^{\mathrm o}(i)\) and \(\varepsilon_X\colon X\to\operatorname{Top}^{\mathrm o}(i)\), with direct images \(\varepsilon_{U*}G=(G\to e_X)\) and \(\varepsilon_{X*}F=(i^*F\xrightarrow{1}F)\).
3. The functor \(p^{-1}F=(i^*F\xrightarrow{1}F)\) is the inverse image of a morphism of topoi \(p\colon\operatorname{Top}^{\mathrm o}(i)\to X\), with direct image \(p_*(G,F,\gamma)=F\times_{i_*i^*F}i_*G\), the fibre product of the unit \(F\to i_*i^*F\) and \(i_*(\gamma)\). Moreover \(\varepsilon_X^{-1}p^{-1}=1\), \(\varepsilon_U^{-1}p^{-1}=i^*\) and \(p^{-1}=\varepsilon_{X*}\).

**Proof.** (1) By Proposition 5.1 of the lesson on fibred topoi, the fibred topos is good and its functors \(f_!\) preserve fibre products. So \(\operatorname{Top}^{\mathrm o}(i)\) is a topos (Theorem 4.3 there), with limits and colimits computed levelwise (Proposition 2.2 (b) there). If both components of a morphism are isomorphisms, their inverses form an inverse morphism.

(2) By Proposition 3.1 (2) there, each level functor has a left and a right adjoint, so it is exact and is the inverse image of a morphism of topoi. Its right adjoint is \(i^{\mathrm o}_*(Z)_j=\prod_{f\colon j\to i}f^*Z\), which gives the formulas: there is one arrow \(0\to1\) and there are none \(1\to0\).

(3) The functor \(p^{-1}=\varepsilon_{X*}\) commutes with limits, being a right adjoint, and with colimits, which are computed levelwise and commute with \(i^*\). For a sheaf \(F'\) on \(X\), a morphism \(p^{-1}F'\to(G,F,\gamma)\) is a pair \(a\colon i^*F'\to G\), \(b\colon F'\to F\) with \(\gamma\circ a=i^*(b)\). Through the adjunction between \(i^*\) and \(i_*\), it is a pair of morphisms \(F'\to i_*G\) and \(F'\to F\) with the same composite to \(i_*i^*F\), that is, a morphism \(F'\to F\times_{i_*i^*F}i_*G\). \(\square\)

**Proposition 1.3 (cohomology on \(\operatorname{Top}^{\mathrm o}(i)\)).** For complexes \(F\in D^+(X)\) and \(G\in D^+(U)\) of abelian sheaves,
\[
\begin{gathered}R\Gamma(\operatorname{Top}^{\mathrm o}(i),(i^*F\xrightarrow{1}F))=R\Gamma(X,F),\\
R\Gamma(\operatorname{Top}^{\mathrm o}(i),(G\to0))=R\Gamma(U,G),\\
R\Gamma(\operatorname{Top}^{\mathrm o}(i),(0\to F))=R\Gamma_Y(X,F),\end{gathered}
\]
and the exact sequence \(0\to(0\to F)\to\) \((i^*F\xrightarrow{1}F)\to\) \((i^*F\to0)\to0\) gives the triangle
\[
\begin{aligned}&R\Gamma_Y(X,F)\to R\Gamma(X,F)\\
&\quad\to R\Gamma(U,F)\to R\Gamma_Y(X,F)[1]\end{aligned}
\]
of [Tag 0A39], whose second map is the restriction.

**Proof.** Limits being computed levelwise, the final object of \(\operatorname{Top}^{\mathrm o}(i)\) is \((e_U\to e_X)\), and a global section of \((G,F,\gamma)\), a morphism from it, is a pair of sections \(s\in G(U)\), \(t\in F(X)\) with \(\gamma(s)=t|_U\). Hence \(\Gamma\) of \((i^*F\to F)\), \((G\to0)\) and \((0\to F)\) is \(F(X)\), \(G(U)\) and \(\Gamma_Y(X,F)\). On abelian sheaves, \(\varepsilon_{X*}F=(i^*F\to F)\) and \(\varepsilon_{U*}G=(G\to0)\) are exact, and they are right adjoint to the exact functors \(\varepsilon_X^{-1}\), \(\varepsilon_U^{-1}\), so they preserve injectives [Tag 015Z]. With a bounded below injective resolution this gives the first two formulas.

For the third, let \(F\to I\) be a quasi-isomorphism to a bounded below complex of injective abelian sheaves. The sequence of complexes
\[
0\to(0\to I)\to\varepsilon_{X*}I\to\varepsilon_{U*}i^*I\to0
\]
is exact, its terms being exact levelwise. Each \(i^*I^n\) is injective [Tag 01E1], so \(\varepsilon_{X*}I^n\) and \(\varepsilon_{U*}i^*I^n\) are injective, and on global sections the second map is the restriction \(I^n(X)\to I^n(U)\), which is surjective [Tag 01EA]. The long exact cohomology sequence gives \(H^q(\operatorname{Top}^{\mathrm o}(i),(0\to I^n))=0\) for \(q\geq1\). So \((0\to I)\) is a bounded below resolution of \((0\to F)\) by \(\Gamma\)-acyclic objects, and \(\Gamma(\operatorname{Top}^{\mathrm o}(i),(0\to I))=\Gamma_Y(X,I)\) computes \(R\Gamma(\operatorname{Top}^{\mathrm o}(i),(0\to F))\) [Tag 015E]; by definition it computes \(R\Gamma_Y(X,F)\). On global sections this exact sequence is \(0\to\Gamma_Y(X,I)\to I(X)\to I(U)\to0\), the sequence that defines the triangle of [Tag 0A39]. \(\square\)

**Rings and modules.** Let \(B\) be a sheaf of rings on \(X\), and \(B^{\mathrm o}=p^{-1}B=(i^*B\xrightarrow{1}B)\), a ring of \(\operatorname{Top}^{\mathrm o}(i)\). A \(B^{\mathrm o}\)-module is a triple \((G,F,\gamma)\) with \(G\) a \(B|_U\)-module, \(F\) a \(B\)-module and \(\gamma\colon G\to i^*F\) a \(B|_U\)-linear map (Section 4.3 of the lesson on morphisms of fibred topoi). With these rings, \(\varepsilon_U\), \(\varepsilon_X\) and \(p\) are morphisms of ringed topoi whose module inverse images are the exact functors of Proposition 1.2, so they are their own derived functors.

Products, colimits and multilinear maps of \(B^{\mathrm o}\)-modules are levelwise, and \(i^*\) commutes with tensor products and exterior powers. So tensor products and exterior powers of \(B^{\mathrm o}\)-modules are computed levelwise:
\[
\begin{aligned}&(G\xrightarrow{\gamma}F)\otimes(G'\xrightarrow{\gamma'}F')\\
&\quad=(G\otimes G'\xrightarrow{\gamma\otimes\gamma'}F\otimes F'),\\
&\Lambda^n(G\xrightarrow{\gamma}F)=(\Lambda^nG\xrightarrow{\Lambda^n\gamma}\Lambda^nF).\end{aligned}
\]
In particular a \(B^{\mathrm o}\)-module whose two levels are flat is flat. For a \(B^{\mathrm o}\)-module \(K\), \(H^n(\operatorname{Top}^{\mathrm o}(i),K)\) is computed by an injective resolution of \(K\) in the category of \(B^{\mathrm o}\)-modules [Tag 05TG], and it agrees with the cohomology of the underlying abelian sheaf [Tag 03FD]. So Proposition 1.3 computes it; the same holds on \(X\) and on \(U\).

## 2. Partial connections and the localized class

In the rest of the lesson, \(A\to B\) is a map of sheaves of rings on \(X\), and \(\mathrm d\colon B\to\Omega\) is an \(A\)-derivation into a \(B\)-module \(\Omega\) that is locally free of finite rank: \(\mathrm d\) is additive, \(\mathrm d(bb')=b\,\mathrm db'+b'\,\mathrm db\), and \(\mathrm d\) vanishes on the image of \(A\). The main example is the universal derivation into \(\Omega_{B/A}\), when this module is locally free of finite rank. Put \(\Omega^n=\Lambda^n\Omega\). On \(U\) an exact sequence of \(B|_U\)-modules
\[
0\to L\xrightarrow{u}\Omega|_U\xrightarrow{v}M\to0\tag{2.1}
\]
is given, with \(M\) locally free of finite rank. A local basis of \(M\) lifts locally to \(\Omega|_U\), so (2.1) splits locally; hence \(L\) is locally a direct summand of \(\Omega|_U\) and is flat. Put
\[
K=(L\xrightarrow{u}\Omega),
\]
a flat \(B^{\mathrm o}\)-module, so that \(\Lambda^nK=(\Lambda^nL\xrightarrow{\Lambda^nu}\Omega^n)\).

**Definition 2.1.** The *principal parts* of \(\mathrm d\) are the \(B\)-bimodule \(P_{\mathrm d}=B\oplus\Omega\), with the left structure \(b(c,\omega)=(bc,b\omega)\) and the right structure \((c,\omega)b=(cb,c\,\mathrm db+b\omega)\). For a \(B\)-module \(E\), \(P_{\mathrm d}(E)=P_{\mathrm d}\otimes_BE\) is formed with the right structure and is a \(B\)-module through the left one. Put
\[
\begin{gathered}\pi((c,\omega)\otimes m)=cm,\\
\iota(\omega\otimes m)=(0,\omega)\otimes m,\\
\mathrm d^1(m)=(1,0)\otimes m.\end{gathered}
\]

**Lemma 2.2.**

1. \(P_{\mathrm d}\) is a \(B\)-bimodule. For every \(B\)-module \(E\) the sequence of \(B\)-modules \(0\to\Omega\otimes E\xrightarrow{\iota}P_{\mathrm d}(E)\xrightarrow{\pi}E\to0\) is exact; it is natural in \(E\), and its formation commutes with restriction to \(U\). The map \(\mathrm d^1\) is additive, \(\pi\circ\mathrm d^1=1\), and \(\mathrm d^1(bm)=b\,\mathrm d^1(m)+\iota(\mathrm db\otimes m)\).
2. For the universal derivation into \(\Omega_{B/A}\), the rule \(x\otimes y\mapsto(xy,x\,\mathrm dy)\) induces an isomorphism of \(B\)-bimodules \(P^1_{B/A}\to P_{\mathrm d}\), which carries the maps \(\mathrm d^1\), \(\iota\), \(\pi\) of the lesson on the Atiyah class (Definition 1.1 and Lemma 1.2 there) to those of Definition 2.1.

**Proof.** (1) The right action is associative because \(\mathrm d\) is a derivation:
\[
\begin{aligned}&((c,\omega)b)b'\\
&\quad=(cbb',\,cb\,\mathrm db'+cb'\,\mathrm db+bb'\omega)\\
&\quad=(c,\omega)(bb');\end{aligned}
\]
it is unital because \(\mathrm d1=0\), and it commutes with the left action. The map \(c\mapsto(c,\mathrm dc)\) is right \(B\)-linear, since \((c,\mathrm dc)b=(cb,\mathrm d(cb))\), so it splits the sequence \(0\to\Omega\to P_{\mathrm d}\to B\to0\) of right \(B\)-modules, both actions agreeing on \(\Omega\). Hence the sequence stays exact after \(-\otimes_BE\), which is the exact sequence of (1); \(\iota\) and \(\pi\) are left \(B\)-linear, and \(\pi\) is well defined because \(\pi((c,\omega)b\otimes m)=cbm\). Restriction to \(U\) commutes with direct sums and tensor products. Finally \(\pi\mathrm d^1(m)=m\) and
\[
\begin{aligned}&\mathrm d^1(bm)=(1,0)b\otimes m=(b,\mathrm db)\otimes m\\
&\quad=b\,\mathrm d^1(m)+\iota(\mathrm db\otimes m).\end{aligned}
\]

(2) The rule is balanced over \(A\), because \(\mathrm d\) vanishes on \(A\), and it is a map of bimodules: \(zx\otimes yz'\mapsto\) \((zxyz',zx\,\mathrm d(yz'))=z(xy,x\,\mathrm dy)z'\). Let \(J=\ker(B\otimes_AB\to B)\). A local section of \(J\) is locally a sum \(\sum x_k\otimes y_k\) with \(\sum x_ky_k=0\), which equals \(\sum(x_k\otimes1)(1\otimes y_k-y_k\otimes1)\); so \(J\) is generated as a left \(B\)-module by the sections \(1\otimes b-b\otimes1\), and \(J^2\) by their products
\[
\begin{aligned}&(1\otimes b'-b'\otimes1)(1\otimes b-b\otimes1)\\
&\quad=1\otimes b'b-b'\otimes b-b\otimes b'+b'b\otimes1,\end{aligned}
\]
which the rule maps to \((0,\mathrm d(b'b)-b'\,\mathrm db-b\,\mathrm db')=0\). So it induces a map of bimodules \(P^1_{B/A}=(B\otimes_AB)/J^2\to P_{\mathrm d}\). This map sends the class \(\mathrm ds\) of \(1\otimes s-s\otimes1\) in \(J/J^2=\Omega_{B/A}\) to \((0,\mathrm ds)\) and is compatible with the projections to \(B\); by the five lemma it is an isomorphism. It carries \(\mathrm d^1(m)=(1\otimes1)\otimes m\) to \((1,0)\otimes m\), \(\iota(\mathrm ds\otimes m)=(1\otimes s-s\otimes1)\otimes m\) to \((0,\mathrm ds)\otimes m\), and \(\pi\) to \(\pi\). \(\square\)

**Definition 2.3.** Let \(E\) be a \(B\)-module. A *partial connection* on \(E|_U\) relative to (2.1) is a \(B|_U\)-linear map
\[
D\colon P_{\mathrm d}(E)|_U\to M\otimes E|_U
\]
with \(D\circ\iota=v\otimes1\) on \(\Omega|_U\otimes E|_U\).

**Lemma 2.4.** Let \(E\) be a \(B\)-module. The rule \(D\mapsto\nabla=D\circ\mathrm d^1\) is a bijection from the partial connections on \(E|_U\) relative to (2.1) to the additive maps \(\nabla\colon E|_U\to M\otimes E|_U\) such that
\[
\begin{aligned}&\nabla(bm)\\
&\quad=b\nabla(m)+v(\mathrm db)\otimes m\end{aligned}\tag{2.2}
\]
for local sections \(b\) of \(B\) and \(m\) of \(E\) over open subsets of \(U\). If \(L=0\) and \(v\) is the identity of \(M=\Omega|_U\), these maps \(\nabla\) are the *connections* on \(E|_U\) relative to \(\mathrm d\), and \(D\) is the retraction of \(\iota\) with \(1-\iota\circ D=s_\nabla\circ\pi\), where \(s_\nabla=\mathrm d^1-\iota\circ\nabla\) is a \(B\)-linear section of \(\pi\); for the universal derivation these are the connections and the sections of Proposition 3.2 of the lesson on the Atiyah class.

**Proof.** If \(D\) is a partial connection, \(\nabla=D\circ\mathrm d^1\) is additive, and by Lemma 2.2 (1)
\[
\begin{aligned}&\nabla(bm)=D\bigl(b\,\mathrm d^1m+\iota(\mathrm db\otimes m)\bigr)\\
&\quad=b\nabla(m)+v(\mathrm db)\otimes m.\end{aligned}
\]
Since \((c,\omega)\otimes m=c\,\mathrm d^1(m)+\iota(\omega\otimes m)\), the module \(P_{\mathrm d}(E)\) is generated by the sections \(\mathrm d^1(m)\) and \(\iota(\omega\otimes m)\), so \(D\) is determined by \(\nabla\).

Conversely, let \(\nabla\) satisfy (2.2). The rule \((c,\omega)\otimes m\mapsto c\nabla(m)+v(\omega)\otimes m\) is additive in each variable, left \(B\)-linear, and balanced for the right structure:
\[
\begin{aligned}&(c,\omega)b\otimes m=(cb,\,c\,\mathrm db+b\omega)\otimes m\\
&\quad\mapsto cb\nabla(m)+v(c\,\mathrm db+b\omega)\otimes m\\
&\quad=c\nabla(bm)+v(\omega)\otimes bm\end{aligned}
\]
by (2.2), which is the image of \((c,\omega)\otimes bm\). So it defines a \(B\)-linear map \(D\colon P_{\mathrm d}(E)|_U\to M\otimes E|_U\), with \(D\circ\mathrm d^1=\nabla\) and \(D\circ\iota=v\otimes1\).

For \(L=0\), (2.2) reads \(\nabla(bm)=b\nabla(m)+\mathrm db\otimes m\), and \(D\circ\iota=1\). The map \(s_\nabla\) is \(B\)-linear by Lemma 2.2 (1) and (2.2), and \(\pi s_\nabla=1\). The \(B\)-linear maps \(1-\iota D\) and \(s_\nabla\pi\) agree on the generators \(\mathrm d^1m\), where both give \(\mathrm d^1m-\iota\nabla(m)\), and on \(\iota(\Omega\otimes E)\), where both vanish. For the universal derivation, Lemma 2.2 (2) identifies these maps with those of the lesson on the Atiyah class. \(\square\)

**Lemma 2.5.** Let \(D\) be a partial connection on \(E|_U\). Then \(D\) is surjective, \(\iota\circ(u\otimes1)\) maps \(L\otimes E|_U\) into \(\operatorname{Ker}D\), and the sequence
\[
\begin{aligned}&0\to L\otimes E|_U\\
&\quad\xrightarrow{\iota(u\otimes1)}\operatorname{Ker}D\\
&\quad\xrightarrow{\pi}E|_U\to0\end{aligned}\tag{2.3}
\]
is exact.

**Proof.** \(D\iota(u\otimes1)=(vu)\otimes1=0\), and \(D\) is surjective because \(D\iota=v\otimes1\) is. Since \(M\) is flat, (2.1) stays exact after \(-\otimes E|_U\). The maps \(v\otimes1\), \(D\) and \(0\) form a map from the sequence \(0\to\Omega\otimes E|_U\to P_{\mathrm d}(E)|_U\to E|_U\to0\), exact by Lemma 2.2 (1), to the exact sequence \(0\to M\otimes E|_U\xrightarrow{1}M\otimes E|_U\to0\to0\). Their kernels are \(L\otimes E|_U\), \(\operatorname{Ker}D\) and \(E|_U\), and the cokernel of \(v\otimes1\) is \(0\). The snake lemma [Tag 010H] shows that (2.3), the sequence of kernels, is exact. \(\square\)

**Definition 2.6.** Let \(E\) be a \(B\)-module with a partial connection \(D\) on \(E|_U\). The sequence (2.3) on \(U\), the sequence of Lemma 2.2 (1) on \(X\) and the inclusion \(\operatorname{Ker}D\subseteq P_{\mathrm d}(E)|_U\) form an exact sequence of \(B^{\mathrm o}\)-modules
\[
\begin{aligned}&0\to(L\otimes E|_U\to\Omega\otimes E)\\
&\quad\to(\operatorname{Ker}D\to P_{\mathrm d}(E))\\
&\quad\to(E|_U\xrightarrow{1}E)\to0,\end{aligned}\tag{2.4}
\]
whose first term is \(K\otimes p^{-1}E\), and \(K\otimes p^{-1}E=K\otimes^{\mathbf L}p^{-1}E\) because \(K\) is flat. The *localized class* of \((E,D)\) is
\[
\operatorname{at}(E,D)=\kappa\circ\delta\colon p^{-1}E\to p^{-1}E\otimes K[1],
\]
where \(\delta\colon p^{-1}E\to(K\otimes p^{-1}E)[1]\) is the connecting morphism of (2.4) in \(D(B^{\mathrm o})\). Likewise the *principal parts class* of \(E\) relative to \(\mathrm d\) is \(\operatorname{at}^{\mathrm d}(E)=\kappa\circ\delta_E\colon E\to E\otimes\Omega[1]\), where \(\delta_E\) is the connecting morphism of the sequence of Lemma 2.2 (1) in \(D(B)\), \(\Omega\otimes E=\Omega\otimes^{\mathbf L}E\) because \(\Omega\) is flat.

**Proposition 2.7.** Let \(E\) be a \(B\)-module with a partial connection \(D\) on \(E|_U\).

1. \(\varepsilon_X^{-1}\operatorname{at}(E,D)=\operatorname{at}^{\mathrm d}(E)\). For the universal derivation into \(\Omega_{B/A}\), \(\operatorname{at}^{\mathrm d}(E)\) is the principal parts class \(\operatorname{at}^\Omega(E)\) of Definition 4.1 of the lesson on the Atiyah class of filtered complexes.
2. Let \(f\colon E'\to E\) be \(B\)-linear and \(D'\) a partial connection on \(E'|_U\) with \(D\circ P_{\mathrm d}(f)=(1\otimes f)\circ D'\) on \(U\). Then
\[
\begin{aligned}&\operatorname{at}(E,D)\circ p^{-1}f\\
&\quad=(p^{-1}f\otimes1)\circ\operatorname{at}(E',D').\end{aligned}
\]

**Proof.** (1) The exact functor \(\varepsilon_X^{-1}\) carries the sequence (2.4) to the sequence of Lemma 2.2 (1), and so the triangle of (2.4) to its triangle; it carries \(K\) to \(\Omega\) and \(\kappa\) to \(\kappa\). For the universal derivation, Lemma 2.2 (2) identifies the sequence of Lemma 2.2 (1) with the extension of principal parts of the lesson on the Atiyah class, which is the sequence (4.1) of the lesson on the Atiyah class of filtered complexes for the complex \(E\). Let \(F\to E\) be a quasi-isomorphism from a K-flat complex [Tag 06YS]. It induces a map from the sequence (4.1) of \(F\) to that of \(E\), whose first component \(\Omega\otimes F\to\Omega\otimes E\) is a quasi-isomorphism because \(\Omega\) is flat; so the connecting morphisms correspond under \(F\cong E\), and Definition 4.1 there gives \(\operatorname{at}^\Omega(E)=\operatorname{at}^{\mathrm d}(E)\).

(2) The maps \(P_{\mathrm d}(f)\) carry \(\operatorname{Ker}D'\) into \(\operatorname{Ker}D\), so they form a map from the sequence (2.4) of \((E',D')\) to that of \((E,D)\), with first component \(1\otimes p^{-1}f\) and third component \(p^{-1}f\). So \(\delta\circ p^{-1}f=(1\otimes p^{-1}f)[1]\circ\delta'\), and \(\kappa\) is natural. \(\square\)

## 3. Chern classes with supports

**Lemma 3.1.** If \(E\in D(B)\) has perfect amplitude in \([m,n]\), then \(p^{-1}E\in D(B^{\mathrm o})\) has perfect amplitude in \([m,n]\).

**Proof.** Choose an open covering \((V_\alpha)\) of \(X\) such that each \(E|_{V_\alpha}\) is isomorphic to a strictly perfect complex \(P_\alpha\) with terms in degrees \([m,n]\) [Tag 08FL]. The inverse image \(p^{-1}\) preserves surjective families, so the objects \(p^{-1}V_\alpha\) cover the final object of \(\operatorname{Top}^{\mathrm o}(i)\), and for every object \(W\) the objects \(W\times p^{-1}V_\alpha\) cover \(W\). The restriction of \(p^{-1}E\) to \(p^{-1}V_\alpha\) is the inverse image of \(E|_{V_\alpha}\), isomorphic to \(p^{-1}P_\alpha\), whose terms are direct summands of finite free \(B^{\mathrm o}\)-modules, in degrees \([m,n]\); so is its restriction to \(W\times p^{-1}V_\alpha\). This is Definition 1.1 of the lesson on perfect filtered complexes. \(\square\)

**Definition 3.2.** Let \(E\) be a \(B\)-module of bounded perfect amplitude, placed in degree \(0\), with a partial connection \(D\) on \(E|_U\). By Lemma 3.1, \(p^{-1}E\in D^{\leq0}(B^{\mathrm o})\) has bounded perfect amplitude, and \(K[1]\in D^{\leq0}(B^{\mathrm o})\). Put
\[
\begin{aligned}&c_t(E,D)=\sigma^S\bigl(c_t(\operatorname{at}(E,D))\bigr)\\
&\quad=\sum_nc^n(E,D)t^n,\end{aligned}
\]
where \(c_t(\operatorname{at}(E,D))\) is the characteristic series of Definition 3.1 of the lesson on L-series, with coefficients in \(K[1]\), and \(\sigma^S\) is the ring isomorphism of Proposition 1.3 there. Since \(K\) is flat, \(L\Lambda^nK=\Lambda^nK\) (Theorem 2.6 of the lesson on filtered and graded powers), so
\[
c^n(E,D)\in H^n\bigl(\operatorname{Top}^{\mathrm o}(i),(\Lambda^nL\to\Omega^n)\bigr).
\]
The ring \(\operatorname{Hom}(B^{\mathrm o},L\Lambda^\bullet(K)[1])=\) \(\prod_nH^n(\operatorname{Top}^{\mathrm o}(i),\Lambda^nK)\) of Definition 1.1 of the lesson on L-series is commutative (Proposition 1.2 (2) there). For \(P\in\mathbf Z[x_1,x_2,\dots]\) put \(P(E,D)=P(c^1(E,D),c^2(E,D),\dots)\) in this ring, and \(P^{\mathrm d}(E)=P(c^{\mathrm d,1}(E),c^{\mathrm d,2}(E),\dots)\) in the ring \(\prod_nH^n(X,\Omega^n)\) of Definition 2.2 of the lesson on Chern classes of perfect complexes, where
\[
\begin{aligned}&c^{\mathrm d}_t(E)=\sigma^S\bigl(c_t(\operatorname{at}^{\mathrm d}(E))\bigr)\\
&\quad=\sum_nc^{\mathrm d,n}(E)t^n\end{aligned}
\]
are the *Chern classes of \(E\) relative to \(\mathrm d\)*. For the universal derivation into \(\Omega_{B/A}\), \(c^{\mathrm d}_t(E)=c'_t(E)\), the Chern classes of \(E\) in Hodge cohomology, and \(P^{\mathrm d}(E)=P(E)=P(c'^1(E),c'^2(E),\dots)\): this is Proposition 2.3 (1) of the lesson on Chern classes of perfect complexes with Proposition 2.7 (1), the truncations \(L\Lambda^n\Omega\to\Lambda^n\Omega\) of Definition 2.2 there being isomorphisms because \(\Omega\) is flat. The polynomial \(P\) is *isobaric of weight \(n\)* if it is a linear combination of monomials \(x_{i_1}\cdots x_{i_k}\) with \(i_1+\cdots+i_k=n\).

**Theorem 3.3.** Let \(E\) be a \(B\)-module of bounded perfect amplitude with a partial connection \(D\) on \(E|_U\), and let \(r\geq0\) be an integer such that \(L\) is locally a direct summand of \((B|_U)^r\).

1. \(\varepsilon_X^{-1}c_t(E,D)=c^{\mathrm d}_t(E)\), hence \(\varepsilon_X^{-1}P(E,D)=P^{\mathrm d}(E)\) for every \(P\). For the universal derivation these are \(c'_t(E)\) and \(P(E)\).
2. For \(n>r\), \(\Lambda^nK=(0\to\Omega^n)\), and Proposition 1.3 identifies \(H^n(\operatorname{Top}^{\mathrm o}(i),\Lambda^nK)\) with \(H^n_Y(X,\Omega^n)\). Under this identification \(\varepsilon_X^{-1}\) is the canonical map \(H^n_Y(X,\Omega^n)\to H^n(X,\Omega^n)\).
3. If \(P\) is isobaric of weight \(n>r\), then \(P(E,D)\) is a class in \(H^n_Y(X,\Omega^n)\) whose image in \(H^n(X,\Omega^n)\) is \(P^{\mathrm d}(E)\).

**Proof.** (1) The morphism of ringed topoi \(\varepsilon_X\) carries \(B^{\mathrm o}\) to \(B\) and \(K\) to \(\Omega\). By Proposition 3.2 (3) of the lesson on L-series and Proposition 2.7 (1),
\[
\varepsilon_X^{-1}L_t(\operatorname{at}(E,D))=L_t(\operatorname{at}^{\mathrm d}(E)),
\]
and the same holds for \(c_t=L_t^{-1}\), \(\varepsilon_X^{-1}\) being a ring homomorphism. The shift isomorphisms commute with \(\varepsilon_X^{-1}\): they are constructed from a bounded above complex of flat modules by termwise operations (Theorem 3.2 of the lesson on Koszul complexes), all of which commute with \(\varepsilon_X^{-1}\), and \(K\) and \(\varepsilon_X^{-1}K=\Omega\) are flat. So \(\varepsilon_X^{-1}c_t(E,D)=\sigma^S(c_t(\operatorname{at}^{\mathrm d}(E)))=c^{\mathrm d}_t(E)\). The ring homomorphism \(\varepsilon_X^{-1}\) commutes with polynomials, and Definition 3.2 gives the case of the universal derivation.

(2) For \(n>r\), \(\Lambda^nL\) vanishes, because it vanishes locally, being locally a direct summand of \(\Lambda^n(B^r)=0\). So \(\Lambda^nK=(0\to\Omega^n)\), and Proposition 1.3 and the paragraph on rings and modules give \(H^n(\operatorname{Top}^{\mathrm o}(i),\Lambda^nK)=H^n_Y(X,\Omega^n)\). The map \(\varepsilon_X^{-1}\colon H^n(\operatorname{Top}^{\mathrm o}(i),\Lambda^nK)\to H^n(X,\Omega^n)\) is the composite of the map induced by the unit \(\Lambda^nK\to\varepsilon_{X*}\varepsilon_X^{-1}\Lambda^nK\) with the adjunction isomorphism \(H^n(\operatorname{Top}^{\mathrm o}(i),\varepsilon_{X*}\Omega^n)=H^n(X,\Omega^n)\), both functors being exact. The unit is the inclusion \((0\to\Omega^n)\to(i^*\Omega^n\xrightarrow{1}\Omega^n)\), so by Proposition 1.3 the map is the first map of the triangle of [Tag 0A39], the canonical map.

(3) A monomial of weight \(n\) is a product of classes \(c^{i_k}(E,D)\in H^{i_k}(\operatorname{Top}^{\mathrm o}(i),\Lambda^{i_k}K)\) with \(\sum_ki_k=n\), which the product of the ring of Definition 3.2 carries into \(H^n(\operatorname{Top}^{\mathrm o}(i),\Lambda^nK)\). By (2) this group is \(H^n_Y(X,\Omega^n)\), and by (1) and (2) the image of \(P(E,D)\) in \(H^n(X,\Omega^n)\) is \(P^{\mathrm d}(E)\). \(\square\)

**Remark 3.4.** For \(L=0\), Lemma 2.4 identifies the partial connections with the connections on \(E|_U\) relative to \(\mathrm d\), and Theorem 3.3 applies with \(r=0\): if \(E|_U\) has a connection, every \(c^{\mathrm d,n}(E)\) with \(n\geq1\) is the image of a class in \(H^n_Y(X,\Omega^n)\).

## 4. Bott's partial connection

In this section \(\mathrm d\) is the universal derivation into \(\Omega=\Omega_{B/A}\), which is locally free of finite rank, and \(\Theta=\mathcal Hom_B(\Omega,B)\), whose local sections are identified with the \(A\)-derivations of \(B\) by \(\xi(b)=\xi(\mathrm db)\), through the universal property of \(\Omega\). For local sections \(\xi\), \(\eta\) of \(\Theta\), the bracket \([\xi,\eta]\) is the section corresponding to the \(A\)-derivation \(b\mapsto\xi(\eta(b))-\eta(\xi(b))\); it satisfies
\[
\begin{gathered}[b\xi,\eta]=b[\xi,\eta]-\eta(b)\xi,\\
[\xi,b\eta]=b[\xi,\eta]+\xi(b)\eta.\end{gathered}
\]
A \(B\)-submodule \(\mathcal F\subseteq\Theta\) is *involutive on \(U\)* if \([\xi,\eta]\) is a section of \(\mathcal F\) for all local sections \(\xi\), \(\eta\) of \(\mathcal F\) over open subsets of \(U\).

**Proposition 4.1.** Let \(\mathcal F\subseteq\Theta\) be a \(B\)-submodule such that \(\mathcal F|_U\) is locally free of finite rank, locally a direct summand of \(\Theta|_U\), and involutive on \(U\). Put \(N=\Theta/\mathcal F\) and \(M=\mathcal Hom(\mathcal F|_U,B|_U)\), let \(v\colon\Omega|_U\to M\) be \(v(\omega)(\xi)=\xi(\omega)\), and \(L=\operatorname{Ker}v\).

1. The sequence \(0\to L\to\Omega|_U\xrightarrow{v}M\to0\) is exact, \(M\) is locally free of finite rank, and \(L\cong\mathcal Hom(N|_U,B|_U)\). If \(N|_U\) is locally a direct summand of \((B|_U)^q\), so is \(L\).
2. There is a unique partial connection on \(N|_U\) relative to this sequence whose map \(\nabla\) of Lemma 2.4, with values in \(M\otimes N|_U=\mathcal Hom(\mathcal F|_U,N|_U)\), is
\[
\nabla(\bar s)(\xi)=\overline{[\xi,s]}
\]
for local sections \(\xi\) of \(\mathcal F\) and \(s\) of \(\Theta\) over open subsets of \(U\), the bar denoting classes in \(N\). It is *Bott's partial connection*.

**Proof.** (1) The module \(\Theta\) is locally free of finite rank, and the canonical map \(\Omega\to\mathcal Hom(\Theta,B)\) is an isomorphism, \(\Omega\) being locally free of finite rank. Locally on \(U\), \(\Theta=\mathcal F\oplus\mathcal F'\); dualizing gives \(\mathcal Hom(\Theta,B)=M\oplus\mathcal Hom(\mathcal F',B)\), and under the isomorphism with \(\Omega|_U\), \(v\) is the projection to \(M\). So \(v\) is surjective and locally split, \(M\) is locally free of finite rank, and \(L\) is the module of forms that vanish on \(\mathcal F\), which \(\omega\mapsto(\bar s\mapsto s(\omega))\) identifies with \(\mathcal Hom(N|_U,B|_U)\). If \(N|_U\oplus Q\cong B^q\) on an open subset, then \(\mathcal Hom(N,B)\oplus\mathcal Hom(Q,B)\cong B^q\) there.

(2) Let \(\xi\), \(s\) be local sections of \(\mathcal F\) and \(\Theta\) over an open subset of \(U\). Since \([b\xi,s]=b[\xi,s]-s(b)\xi\) and \(s(b)\xi\) is a section of \(\mathcal F\), the map \(\xi\mapsto\overline{[\xi,s]}\) is \(B\)-linear. If \(s\) is a section of \(\mathcal F\), so is \([\xi,s]\), \(\mathcal F\) being involutive on \(U\). So \(\nabla(\bar s)\) is a well defined section of \(\mathcal Hom(\mathcal F|_U,N|_U)\), which \(\varphi\otimes n\mapsto(\xi\mapsto\varphi(\xi)n)\) identifies with \(M\otimes N|_U\), \(\mathcal F|_U\) being locally free of finite rank. The map \(\nabla\) is additive, and \([\xi,bs]=b[\xi,s]+\xi(b)s\) gives \(\nabla(b\bar s)(\xi)=b\nabla(\bar s)(\xi)+\xi(b)\bar s\), where \(\xi(b)=v(\mathrm db)(\xi)\). That is, \(\nabla(b\bar s)=b\nabla(\bar s)+v(\mathrm db)\otimes\bar s\), and Lemma 2.4 gives the partial connection. \(\square\)

**Corollary 4.2.** In the situation of Proposition 4.1, let \(D\) be Bott's partial connection. Suppose that \(N\) has bounded perfect amplitude and that \(N|_U\) is locally a direct summand of \((B|_U)^q\). Then for every polynomial \(P\) isobaric of weight \(n>q\), \(P(N)\in H^n(X,\Omega^n)\) is the image of the class \(P(N,D)\in H^n_Y(X,\Omega^n)\). If \(U=X\), the hypothesis on the amplitude of \(N\) holds automatically, and \(P(N)=0\) for every such \(P\).

**Proof.** By Proposition 4.1 (1), Theorem 3.3 (3) applies with \(r=q\). If \(U=X\), then \(N\) is locally a direct summand of \(\Theta\), hence of a finite free module, so it has perfect amplitude in \([0,0]\) (Proposition 1.6 of the lesson on Chern classes of perfect complexes). In that case \(Y\) is empty, \(\Gamma_Y(X,-)=0\), and so \(H^n_Y(X,\Omega^n)=0\). \(\square\)

## 5. Complex analytic spaces

In this section complex spaces are those of Definition 3.1 of [*Cartan's coherence theorem and complex spaces*](course:complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces#3-complex-spaces): Hausdorff and second countable, locally isomorphic to a quotient model \(V(\mathcal J)\subset W\), with \(W\subset\mathbf C^n\) open and \(\mathcal J\) a coherent ideal of \(\mathcal O_W\); morphisms are morphisms of locally ringed spaces over \(\mathbf C\). The base of a morphism is written \(S\), as \(Y\) is the complement of \(U\). We use from Section 1 of [*Complex analytic spaces and analytification*](course:AG-QC/complex-analytic-spaces-and-analytification#1-analytic-equations-and-their-sheaves) that a morphism into a quotient model \(V(\mathcal J)\subset W\) is determined by the pullbacks of the coordinates of \(W\), and that locally on the source it is given by holomorphic coordinate representatives whose substitution carries \(\mathcal J\) into the ideal of the source; conversely such representatives define a morphism. For a function \(H(w,u,v)\) holomorphic on a product \(Q\times D\times D\) of polydiscs,
\[
\begin{aligned}&H(w,u,v)-H(w,u,u)\\&\quad=\sum_j(v_j-u_j)\\&\qquad\cdot G_j(w,u,v),\\&G_j(w,u,v)\\&\quad=\int_0^1\frac{\partial H}{\partial v_j}\bigl(w,u,\\&\qquad u+\tau(v-u)\bigr)\,\mathrm d\tau,\end{aligned}\tag{5.1}
\]
by the fundamental theorem of calculus along \(\tau\mapsto H(w,u,u+\tau(v-u))\), the polydisc \(D\) being convex. Each \(G_j\) is continuous and, differentiating under the integral sign over \([0,1]\), holomorphic in each variable, so it is holomorphic (Definition 1.1 of [*Holomorphic functions of several variables*](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables#1-polydiscs-and-the-definition-of-holomorphy)); and \(G_j(w,u,u)=(\partial H/\partial v_j)(w,u,u)\). In particular a holomorphic function of \((w,u,v)\) that vanishes for \(v=u\) lies in the ideal generated by the \(v_j-u_j\).

**Lemma 5.1 (fibre products).** Let \(f\colon X\to S\) and \(g\colon X'\to S\) be morphisms of complex spaces.

1. Suppose that \(X=V(\mathcal J)\subset W\), \(X'=V(\mathcal J')\subset W'\) and \(S=V(\mathcal K)\subset W_S\subset\mathbf C^m\) are quotient models and that \(f\), \(g\) have holomorphic representatives \(F\colon W\to W_S\), \(G\colon W'\to W_S\). Let \(Q\) be the quotient model of \(W\times W'\) by the ideal generated by \(\mathcal J(u)\), \(\mathcal J'(v)\) and the \(F_k(u)-G_k(v)\), \(k=1,\ldots,m\), and \(p\colon Q\to X\), \(p'\colon Q\to X'\) the morphisms given by the projections. Then \(fp=gp'\), and for every complex space \(Z\) the rule \(h\mapsto(ph,p'h)\) is a bijection from the morphisms \(Z\to Q\) onto the pairs of morphisms \(a\colon Z\to X\), \(b\colon Z\to X'\) with \(fa=gb\).
2. In general there is a complex space \(X\times_SX'\) with morphisms \(p\), \(p'\) having the property of (1). Its points are the pairs \((x,x')\) with \(f(x)=g(x')\), with the topology induced from \(X\times X'\), and over open subsets as in (1) it is the space \(Q\) of (1).

**Proof.** (1) The ideal is locally finitely generated, \(\mathcal J\) and \(\mathcal J'\) being coherent, so it is coherent by Oka's theorem, and \(Q\) is a quotient model. The projections carry \(\mathcal J\) and \(\mathcal J'\) into this ideal, so \(p\) and \(p'\) are morphisms; \(fp\) and \(gp'\) have the representatives \(F(u)\) and \(G(v)\), which agree modulo the ideal, so \(fp=gp'\). Let \(a\), \(b\) be morphisms with \(fa=gb\), and \(s\), \(s'\) the pullbacks of the coordinates of \(W\) and \(W'\). Every local section of \(\mathcal J\) vanishes after substituting \(s\), and likewise for \(\mathcal J'\) and \(s'\); the pullbacks of the coordinates of \(W_S\) under \(fa\) and \(gb\) are \(F(s)\) and \(G(s')\), which are equal because \(fa=gb\). So \((s,s')\), with values in \(W\times W'\), annihilates the ideal of \(Q\) and defines a morphism \(h\colon Z\to Q\) with \(ph=a\) and \(p'h=b\); it is the only one, a morphism into \(Q\) being determined by the pullbacks of the coordinates.

(2) The points of \(Q\) in (1) are the \((u,v)\in X\times X'\) with \(F(u)=G(v)\), that is, \(f(u)=g(v)\). Cover \(S\) by open subsets isomorphic to quotient models, and \(X\), \(X'\) by open subsets isomorphic to quotient models that map into them and on which \(f\), \(g\) have representatives. The spaces \(Q\) of (1) for these open subsets have the universal property for the corresponding open subspaces; over the intersections, open subspaces of two of them have the same universal property and are identified by unique isomorphisms, compatible on triple intersections. Gluing gives a locally ringed space over \(\mathbf C\), locally isomorphic to quotient models, whose underlying space is the set of pairs with \(f(x)=g(x')\) with the topology induced from \(X\times X'\); it is Hausdorff and second countable. The universal property is local on \(Z\), and holds over each piece. \(\square\)

**Definition 5.2 (differentials and principal parts of complex spaces).** Let \(f\colon X\to S\) be a morphism of complex spaces, \(p_1\), \(p_2\) the projections of \(X\times_SX\) and \(\Delta\colon X\to X\times_SX\) the diagonal, with \(p_1\Delta=p_2\Delta=\mathrm{id}_X\). Over open subsets as in Lemma 5.1 (1), with \(X'=X\) and \(G=F\), \(\Delta\) has the representative \(u\mapsto(u,u)\) and identifies \(X\) with the closed subspace defined by the ideal generated by the \(v_j-u_j\): by (5.1), \(\mathcal J(v)\) lies in \(\mathcal J(u)+(v_j-u_j)_j\) and the \(F_k(u)-F_k(v)\) lie in \((v_j-u_j)_j\), and a function vanishing on the diagonal of \(W\times W\) lies in \((v_j-u_j)_j\). So \(\Delta\) is a closed immersion, its image being closed as \(X\) is Hausdorff. Let \(\mathcal I\) be its ideal, locally generated by the classes of the \(v_j-u_j\), and put
\[
\begin{gathered}P^1_{X/S}=\Delta^{-1}(\mathcal O_{X\times_SX}/\mathcal I^2),\\ \Omega^1_{X/S}=\Delta^{-1}(\mathcal I/\mathcal I^2).\end{gathered}
\]
Let \(\lambda,\rho\colon\mathcal O_X\to P^1_{X/S}\) be the ring maps induced by \(p_1\) and \(p_2\), \(\epsilon\colon P^1_{X/S}\to\Delta^{-1}(\mathcal O_{X\times_SX}/\mathcal I)=\mathcal O_X\) the projection, whose kernel is \(\Omega^1_{X/S}\), with \(\epsilon\lambda=\epsilon\rho=\mathrm{id}\), and \(\mathrm d=\rho-\lambda\colon\mathcal O_X\to\Omega^1_{X/S}\). These are the *principal parts of order one*, the *differentials* and the *differential* of \(X\) over \(S\). Locally \(\Omega^1_{X/S}\) is generated by the classes \(\mathrm dz_j\) of the \(v_j-u_j\), the \(z_j\) being the coordinates of \(W\).

**Lemma 5.3 (square-zero extensions with two sections).** Let \(R\) be a sheaf of rings on a topological space, \(\epsilon\colon R\to B\) a surjective map of sheaves of rings whose kernel \(N\) satisfies \(N^2=0\), and \(\lambda,\rho\colon B\to R\) maps of sheaves of rings with \(\epsilon\lambda=\epsilon\rho=\mathrm{id}\). Then \(N\) is a \(B\)-module, through \(\lambda\) or equivalently through \(\rho\); \(\mathrm d=\rho-\lambda\colon B\to N\) is a derivation; and \(r\mapsto(\epsilon(r),r-\lambda\epsilon(r))\) is an isomorphism of sheaves of rings from \(R\) onto \(B\oplus N\) with the product \((c,\omega)(c',\omega')=(cc',c\omega'+c'\omega)\), carrying \(\lambda(b)\) to \((b,0)\) and \(\rho(b)\) to \((b,\mathrm db)\). With the left \(B\)-structure through \(\lambda\) and the right one through \(\rho\), \(R\) is the \(B\)-bimodule \(P_{\mathrm d}\) of Definition 2.1.

**Proof.** For a local section \(\omega\) of \(N\), \(\rho(b)\omega-\lambda(b)\omega=(\mathrm db)\omega\in N^2=0\), so the two module structures agree. Then
\[
\begin{aligned}&\mathrm d(bb')=\rho(b)\rho(b')-\lambda(b)\lambda(b')\\&\quad=\rho(b)\,\mathrm db'+\lambda(b')\,\mathrm db=b\,\mathrm db'+b'\,\mathrm db.\end{aligned}
\]
The rule \((c,\omega)\mapsto\lambda(c)+\omega\) is inverse to the given map, and \((\lambda(c)+\omega)(\lambda(c')+\omega')=\) \(\lambda(cc')+\lambda(c)\omega'+\lambda(c')\omega\) since \(\omega\omega'=0\); so the map is an isomorphism of rings. It carries \(\lambda(b)\) to \((b,0)\) and \(\rho(b)=\lambda(b)+\mathrm db\) to \((b,\mathrm db)\). The left multiplication by \(\lambda(b)\) is \((c,\omega)\mapsto(bc,b\omega)\), and the right multiplication by \(\rho(b)\) is \((c,\omega)\mapsto(c,\omega)(b,\mathrm db)=(cb,c\,\mathrm db+b\omega)\): these are the structures of Definition 2.1. \(\square\)

**Proposition 5.4.** Let \(f\colon X\to S\) be a morphism of complex spaces, \(A=f^{-1}\mathcal O_S\), \(B=\mathcal O_X\), and \(\Omega_{B/A}\) the module of differentials of the map of sheaves of rings \(A\to B\), with its universal derivation \(\mathrm d_{B/A}\) [[Tag 08RM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-universal-module)].

1. \(\mathrm d\) is an \(A\)-derivation, and Lemma 5.3 identifies \(P^1_{X/S}\), with the left structure through \(\lambda\) and the right one through \(\rho\), with the bimodule \(P_{\mathrm d}\). For a \(B\)-module \(E\), the *extension of analytic principal parts* \(0\to\Omega^1_{X/S}\otimes E\to\) \(P^1_{X/S}\otimes_BE\to E\to0\), the tensor product being formed with \(\rho\), is the sequence of Lemma 2.2 (1) for \(\mathrm d\).
2. Let \(\varphi\colon\Omega_{B/A}\to\Omega^1_{X/S}\) be the \(B\)-linear map with \(\varphi\circ\mathrm d_{B/A}=\mathrm d\). The rule \(x\otimes y\mapsto\lambda(x)\rho(y)\) induces a map of \(B\)-bimodules \(P^1_{B/A}\to P^1_{X/S}\); through Lemma 2.2 (2) and (1) it is \((c,\omega)\mapsto(c,\varphi(\omega))\).
3. Let \(f\) be *smooth*: every point of \(X\) has an open neighbourhood isomorphic over \(S\) to the projection \(S'\times D\to S'\), for an open subspace \(S'\) of \(S\) and an open polydisc \(D\subset\mathbf C^n\). On such a neighbourhood \(\Omega^1_{X/S}\) is free with basis \(\mathrm dz_1,\ldots,\mathrm dz_n\), the \(z_k\) being the coordinates of \(D\), and \(\mathrm dh=\sum_k(\partial h/\partial z_k)\,\mathrm dz_k\).

**Proof.** (1) The maps \(\lambda\) and \(\rho\) agree on \(A\) because \(fp_1=fp_2\), so \(\mathrm d\) vanishes on \(A\). Lemma 5.3 applies to \(R=P^1_{X/S}\), with \(N=\Omega^1_{X/S}\), whose square vanishes because \(\mathcal I^2\) maps to \(0\). Its isomorphism respects both structures, so \(P^1_{X/S}\otimes_BE\cong P_{\mathrm d}(E)\), compatibly with the inclusion of \(\Omega^1_{X/S}\otimes E\) and the projection to \(E\).

(2) Through Lemma 5.3, \(\lambda(x)\rho(y)\) is \((x,0)(y,\mathrm dy)=(xy,x\,\mathrm dy)=\) \((xy,x\varphi(\mathrm d_{B/A}y))\). This is the image of \(x\otimes y\) under the map \(x\otimes y\mapsto(xy,x\,\mathrm d_{B/A}y)\) of Lemma 2.2 (2) followed by \((c,\omega)\mapsto(c,\varphi(\omega))\), a map of bimodules because \(\varphi\) is \(B\)-linear with \(\varphi\circ\mathrm d_{B/A}=\mathrm d\). So the rule factors through \(P^1_{B/A}\).

(3) After shrinking, let \(S'=V(\mathcal K)\subset W_S\) be a quotient model, so that \(X=S'\times D\) is the quotient model of \(W_S\times D\) by \(\mathcal K(w)\). By Lemma 5.1 (1), \(X\times_SX\) is the quotient model of \(W_S\times D\times W_S\times D\) by \(\mathcal K(w)\), \(\mathcal K(w')\) and the \(w_k-w'_k\); by (5.1) this is the quotient model of \(W_S\times D\times D\) by \(\mathcal K(w)\), with \(p_1\), \(p_2\) given by \((w,u)\), \((w,v)\) and \(\Delta\) by \(v=u\). By (5.1), applied to a representative, a local section \(h(w,u,v)\) of \(\mathcal O_{X\times_SX}\) whose restriction \(h(w,u,u)\) to the diagonal vanishes lies in the ideal generated by the \(v_k-u_k\); so these generate \(\mathcal I\), and the \(\mathrm dz_k\) generate \(\Omega^1_{X/S}\). The derivations \(\partial/\partial v_k\) of \(\mathcal O_{W_S\times D\times D}\) preserve the ideal generated by \(\mathcal K(w)\), whose generators do not involve \(v\), so they act on \(\mathcal O_{X\times_SX}\); they carry \(\mathcal I^2\) into \(\mathcal I\) and are linear over the functions of \((w,u)\). So \(h\mapsto(\partial h/\partial v_k)(w,u,u)\) induces an \(\mathcal O_X\)-linear map \(\Omega^1_{X/S}\to\mathcal O_X\) carrying \(\mathrm dz_l\) to \(\delta_{kl}\), and the \(\mathrm dz_k\) are linearly independent. Finally \(\mathrm dh\) is the class of \(h(w,v)-h(w,u)=\) \(\sum_k(v_k-u_k)G_k(w,u,v)\), and \(G_k(w,u,u)=(\partial h/\partial z_k)(w,u)\) by (5.1). \(\square\)

**Proposition 5.5 (Chern classes of complex spaces).** Let \(f\colon X\to S\), \(A\), \(B\) and \(\varphi\) be as in Proposition 5.4, and \(\Omega^n_{X/S}=\Lambda^n\Omega^1_{X/S}\). For \(E\in D(B)\) of bounded perfect amplitude put
\[
\begin{aligned}c_t(E,X/S)&=\Lambda^\bullet\varphi\bigl(c'_t(E)\bigr)\\&=\sum_nc^n(E,X/S)\,t^n,\end{aligned}
\]
with \(c^n(E,X/S)\in H^n(X,\Omega^n_{X/S})\), where \(c'_t(E)\) are the Chern classes in Hodge cohomology of Definition 2.2 of the lesson on Chern classes of perfect complexes, for the map of rings \(A\to B\) of the topos of sheaves on \(X\), and \(\Lambda^\bullet\varphi\) is the ring homomorphism induced by the maps \(\Lambda^n\varphi\).

1. Let \(\operatorname{at}^{\mathrm{an}}(E)\colon E\to E\otimes\Omega^1_{X/S}[1]\) be the class of the extension of analytic principal parts, formed with a K-flat resolution as in Definition 4.1 of the lesson on the Atiyah class of filtered complexes. Then \(\operatorname{at}^{\mathrm{an}}(E)=(1\otimes\varphi[1])\circ\operatorname{at}^\Omega(E)\), and \(c_t(E,X/S)\) is the image of \(\sigma^S(c_t(\operatorname{at}^{\mathrm{an}}(E)))\) under the truncations \(L\Lambda^n(\Omega^1_{X/S})\to\Omega^n_{X/S}\). If \(\Omega^1_{X/S}\) is locally free of finite rank, for instance if \(f\) is smooth, then \(c_t(E,X/S)=c^{\mathrm d}_t(E)\) of Definition 3.2 for every \(B\)-module \(E\) of bounded perfect amplitude.
2. (*Whitney formula*) For a distinguished triangle \(E'\to E\to E''\to E'[1]\) of objects of bounded perfect amplitude, \(c_t(E,X/S)=\) \(c_t(E',X/S)\,c_t(E'',X/S)\). If every point has a neighbourhood on which \(E\) is a direct summand of \(B^r\), then \(c^n(E,X/S)=0\) for \(n>r\).
3. (*Functoriality*) Let \(g\colon X'\to X\), \(h\colon S'\to S\) and \(f'\colon X'\to S'\) be morphisms of complex spaces with \(fg=hf'\), and \(G\colon X'\times_{S'}X'\to X\times_SX\) the morphism with \(p_iG=gp'_i\). Then \(G\Delta'=\Delta g\), and \(G\) induces a map \(g^*\Omega^1_{X/S}\to\Omega^1_{X'/S'}\) carrying \(1\otimes\mathrm db\) to \(\mathrm d(g^\sharp b)\). With \(g^*\) the inverse image followed by this map, \(g^*c_t(E,X/S)=c_t(Lg^*E,X'/S')\).
4. (*Invertible modules*) If \(E\) is an invertible \(\mathcal O_X\)-module, then \(c_t(E,X/S)=1+c^1(E,X/S)\,t\), and \(c^1(E,X/S)\in H^1(X,\Omega^1_{X/S})\) is the negative of the image of the class of \(E\) in \(H^1(X,\mathcal O_X^*)\) under \(\gamma\mapsto\gamma^{-1}\mathrm d\gamma\).

**Proof.** (1) Let \(F\to E\) be a quasi-isomorphism from a K-flat complex [Tag 06YS]. The map of Proposition 5.4 (2), tensored with \(F\), is a map from the extension of principal parts \(0\to\Omega_{B/A}\otimes F\to P^1_{B/A}(F)\to F\to0\) to the extension of analytic principal parts of \(F\), with first component \(\varphi\otimes1\) and last component the identity. So the connecting morphisms satisfy \(\delta^{\mathrm{an}}=(\varphi\otimes1)[1]\circ\delta\), and, \(\kappa\) being natural, \(\operatorname{at}^{\mathrm{an}}(E)=(1\otimes\varphi[1])\circ\operatorname{at}^\Omega(E)\). By Proposition 3.2 (1) of the lesson on L-series, \(c_t(\operatorname{at}^{\mathrm{an}}(E))=\varphi_*c_t(\operatorname{at}^\Omega(E))\); \(\sigma^S\) is natural in the coefficient object, and so are the truncations \(L\Lambda^n(K)\to\Lambda^nH^0(K)\). Proposition 2.3 (1) of the lesson on Chern classes of perfect complexes gives the first assertion. If \(\Omega^1_{X/S}\) is locally free of finite rank, it is flat, the truncations are isomorphisms (Theorem 2.6 of the lesson on filtered and graded powers), and for a \(B\)-module \(E\) the class \(\operatorname{at}^{\mathrm{an}}(E)\) is \(\operatorname{at}^{\mathrm d}(E)\) of Definition 2.6, by Proposition 5.4 (1) and the argument of the proof of Proposition 2.7 (1); so \(c_t(E,X/S)=c^{\mathrm d}_t(E)\).

(2) Proposition 2.3 (2), (4) of the lesson on Chern classes of perfect complexes, \(\Lambda^\bullet\varphi\) being a ring homomorphism.

(3) \(G\) exists by Lemma 5.1, and \(G\Delta'=\Delta g\) because both have the components \(g\). So \(G^\sharp\) carries \(\mathcal I\) into \(\mathcal I'\) and induces a ring map \(g^{-1}P^1_{X/S}\to P^1_{X'/S'}\) compatible with \(\lambda\), \(\rho\) and \(\epsilon\), hence a map \(g^{-1}\Omega^1_{X/S}\to\Omega^1_{X'/S'}\) carrying \(\mathrm db\) to \(\mathrm d(g^\sharp b)\); its \(B'\)-linear extension is the stated map. The two \(B'\)-linear maps \(g^*\Omega_{B/A}\to\Omega^1_{X'/S'}\) given by the functoriality map of differentials followed by \(\varphi'\), and by \(g^*\varphi\) followed by the map just constructed, agree on the generators \(1\otimes\mathrm d_{B/A}b\), where both give \(\mathrm d(g^\sharp b)\); so they are equal, and so are their exterior powers. Proposition 2.3 (3) of the lesson on Chern classes of perfect complexes, followed by \(\Lambda^\bullet\varphi'\), gives the formula.

(4) By Proposition 2.4 of the lesson on Chern classes of perfect complexes, \(c'_t(E)=1+c'^1(E)t\), with \(c'^1(E)\) the negative of the class of the extension \(0\to\Omega_{B/A}\to E^\vee\otimes P^1_{B/A}(E)\to B\to0\). By Proposition 5.4 (2), its image under \(\varphi\) is the class of \(0\to\Omega^1_{X/S}\to E^\vee\otimes P^1_{X/S}(E)\to B\to0\). The proof of Corollary 2.5 there computes this class through local bases \(e\) and the connections \(\nabla_e(be)=\mathrm db\otimes e\); it applies with \(\mathrm d\) in place of the universal derivation, since \(\nabla_e(b\gamma e)=\mathrm db\otimes\gamma e+b\gamma^{-1}\mathrm d\gamma\otimes\gamma e\) gives \(\nabla_{\gamma e}=\nabla_e-\gamma^{-1}\mathrm d\gamma\) for every derivation. \(\square\)

**Corollary 5.6 (smooth morphisms of complex spaces).** Let \(f\colon X\to S\) be a smooth morphism of complex spaces, and take in Sections 2 and 3 the derivation \(\mathrm d\colon\mathcal O_X\to\Omega^1_{X/S}\), into a module that is locally free of finite rank by Proposition 5.4 (3). A partial connection on \(E|_U\) relative to (2.1) is a splitting of the image under \(v\otimes1\) of the extension of analytic principal parts of \(E|_U\): a \(B|_U\)-linear retraction of its pushout along \(v\otimes1\) onto \(M\otimes E|_U\). For a \(B\)-module \(E\) of bounded perfect amplitude with a partial connection \(D\) on \(E|_U\), Theorem 3.3 holds with \(c^{\mathrm d}_t(E)=c_t(E,X/S)\): a polynomial isobaric of weight \(n>r\) in the classes \(c^i(E,D)\) is a class in \(H^n_Y(X,\Omega^n_{X/S})\) that lifts the same polynomial in the \(c^i(E,X/S)\).

**Proof.** By Proposition 5.4 (1) the extension of analytic principal parts of \(E\) is the sequence of Lemma 2.2 (1). A \(B|_U\)-linear map \(D\colon P_{\mathrm d}(E)|_U\to M\otimes E|_U\) with \(D\circ\iota=v\otimes1\) is the same as a retraction onto \(M\otimes E|_U\) of the pushout along \(v\otimes1\), that is, a partial connection in the sense of Definition 2.3. Theorem 3.3 and Proposition 5.5 (1) give the rest. \(\square\)

## 6. Exercises

**Exercise 6.1.** For abelian sheaves \(F\) on \(X\) and \(G\) on \(U\), compute with Proposition 1.2 (3) that \(p_*(i^*F\xrightarrow{1}F)=F\), \(p_*(G\to0)=i_*G\), and that \(p_*(0\to F)\) is the subsheaf of \(F\) of sections with support in \(Y\). Show that \(\Gamma(\operatorname{Top}^{\mathrm o}(i),K)=\Gamma(X,p_*K)\) for every abelian object \(K\), and recover the groups \(F(X)\), \(G(U)\) and \(\Gamma_Y(X,F)\) of the proof of Proposition 1.3.

**Exercise 6.2.** Suppose \(U=X\). Show that \(R\Gamma(\operatorname{Top}^{\mathrm o}(i),(0\to F))=0\) for every \(F\in D^+(X)\), and deduce from Theorem 3.3 that \(c^{\mathrm d,n}(E)=0\) for \(n\geq1\) when a \(B\)-module \(E\) of bounded perfect amplitude has a connection relative to \(\mathrm d\).

**Exercise 6.3.** Let \(E\) be a \(B\)-module that is locally a direct summand of a finite free module. Show that partial connections on \(E|_U\) relative to (2.1) exist locally on \(U\), that the maps \(\nabla\) of two of them differ by a \(B\)-linear map \(E|_U\to M\otimes E|_U\), and that the sum of the map \(\nabla\) of a partial connection and such a \(B\)-linear map is the map of a partial connection.

**Exercise 6.4.** Let \(X\) be the projective line over a field \(k\), \(A=k\), \(B=\mathcal O_X\), and \(E=\mathcal O(1)\), with the bases \(e_0\) on \(U_0=\operatorname{Spec}k[x]\) and \(e_1=xe_0\) on \(U_1=\operatorname{Spec}k[y]\), \(y=1/x\), as in Exercise 3.3 of the lesson on Chern classes of perfect complexes. Let \(U=U_0\), so that \(Y\) is the point \(\infty\). Show in two ways that \(c'^1(E)\) is the image of a class in \(H^1_Y(X,\Omega)\): by Theorem 3.3, and by the triangle of [Tag 0A39] together with \(H^1(U_0,\Omega)=0\) [Tag 01XB].

**Exercise 6.5.** Let \(k\) be a field, \(X=\operatorname{Spec}k[x,y]\), \(A=k\) and \(B=\mathcal O_X\), so that \(\Theta\) is free on \(\partial_x\), \(\partial_y\). Let \(\xi=x\partial_x+y\partial_y\), \(\mathcal F=B\xi\), and \(U=X\smallsetminus\{0\}\), where \(0\) is the point \(x=y=0\).

1. Show that \(\mathcal F\) satisfies the hypotheses of Proposition 4.1, that \(N|_U\) is locally free of rank one, and that \(N\) has perfect amplitude in \([-1,0]\).
2. Show that Bott's partial connection satisfies \(\nabla(\bar\partial_x)(\xi)=-\bar\partial_x\) and \(\nabla(\bar\partial_y)(\xi)=-\bar\partial_y\).
3. Deduce that for every \(P\) isobaric of weight \(n\geq2\), \(P(N)\) is the image of a class in \(H^n_{\{0\}}(X,\Omega^n)\).

**Exercise 6.6.** Let \(X=V(z^2)\subset\mathbf C\) be the double point and \(S\) a point. Show that \(X\times_SX\) is the quotient model of \(\mathbf C^2\) by \((u^2,v^2)\), that \(P^1_{X/S}\) is three-dimensional with basis \(1\), \(\lambda(z)\), \(\rho(z)\), and that \(\Omega^1_{X/S}\) is the one-dimensional space spanned by \(\mathrm dz\), with \(z\,\mathrm dz=0\).

**Exercise 6.7.** Let \(X=S=\mathbf C\) and \(f(z)=z^2\). Show that \(\Omega^1_{X/S}\) vanishes off the origin, that its stalk at the origin is \(\mathbf C\,\mathrm dz\) with \(z\,\mathrm dz=0\), and that it is not locally free.

## 7. Complete solutions

**Solution 6.1.** In \(p_*(G,F,\gamma)=F\times_{i_*i^*F}i_*G\): for \((i^*F\xrightarrow{1}F)\) the second map is the identity of \(i_*i^*F\), so the fibre product is \(F\); for \((G\to0)\) it is \(0\times_0i_*G=i_*G\); for \((0\to F)\) it is \(F\times_{i_*i^*F}0\), the kernel of \(F\to i_*i^*F\), whose sections over an open subset \(W\) are the sections of \(F\) over \(W\) that vanish on \(W\cap U\), that is, have support in \(Y\). The final object of \(\operatorname{Top}^{\mathrm o}(i)\) is \(p^{-1}e_X\), so by adjunction
\[
\begin{aligned}&\Gamma(\operatorname{Top}^{\mathrm o}(i),K)=\operatorname{Hom}(p^{-1}e_X,K)\\
&\quad=\operatorname{Hom}(e_X,p_*K)=\Gamma(X,p_*K).\end{aligned}
\]
For the three objects this is \(F(X)\), \(\Gamma(X,i_*G)=G(U)\), and the group of sections of \(F\) over \(X\) with support in \(Y\), which is \(\Gamma_Y(X,F)\).

**Solution 6.2.** With \(U=X\), \(Y\) is empty, and a section with empty support is \(0\), so \(\Gamma_Y(X,-)=0\) and \(R\Gamma_Y(X,-)=0\); Proposition 1.3 gives \(R\Gamma(\operatorname{Top}^{\mathrm o}(i),(0\to F))=0\). If \(\nabla\) is a connection on \(E\) relative to \(\mathrm d\), Lemma 2.4 with \(L=0\) makes it a partial connection on \(E|_U=E\), and Theorem 3.3 (3) applies with \(r=0\). For \(n\geq1\), \(P=x_n\) is isobaric of weight \(n>0\), so \(c^{\mathrm d,n}(E)=P^{\mathrm d}(E)\) is the image of a class in \(H^n_Y(X,\Omega^n)=0\).

**Solution 6.3.** On a free module with basis \((e_j)\), \(\nabla_0(\sum_jb_je_j)=\sum_j\mathrm db_j\otimes e_j\) satisfies \(\nabla_0(bm)=b\nabla_0(m)+\mathrm db\otimes m\). If \(E\oplus E'\cong B^n\) on an open subset, with projection \(q\colon B^n\to E\), then \((1\otimes q)\circ\nabla_0\), restricted to \(E\), satisfies the same rule there, because \(q(m)=m\) for sections \(m\) of \(E\). On \(U\) the map \((v\otimes1)\circ(1\otimes q)\circ\nabla_0\) is additive and satisfies (2.2), so by Lemma 2.4 it is the map of a partial connection. If \(\nabla\) and \(\nabla'\) satisfy (2.2), the terms \(v(\mathrm db)\otimes m\) cancel in \((\nabla-\nabla')(bm)\), so \(\nabla-\nabla'\) is \(B\)-linear. Conversely, for a \(B\)-linear \(\varphi\), \(\nabla+\varphi\) satisfies (2.2), and Lemma 2.4 applies.

**Solution 6.4.** Take for \(\mathrm d\) the universal derivation into \(\Omega=\Omega_{X/k}\), free of rank one on \(U_0\) and on \(U_1\). On \(U_0\), \(\nabla(be_0)=\mathrm db\otimes e_0\) is a connection on \(E|_U\), so by Lemma 2.4 it is a partial connection relative to (2.1) with \(L=0\). The module \(E\) is invertible, so it has perfect amplitude in \([0,0]\) (Proposition 1.6 of the lesson on Chern classes of perfect complexes). Theorem 3.3 (3) with \(r=0\) and \(P=x_1\) shows that \(c'^1(E)\) is the image of the class \(c^1(E,D)\in H^1_Y(X,\Omega)\). For the second way, the triangle of [Tag 0A39] gives the exact sequence
\[
H^1_Y(X,\Omega)\to H^1(X,\Omega)\to H^1(U_0,\Omega),
\]
and \(H^1(U_0,\Omega)=0\) because \(U_0\) is affine and \(\Omega\) is quasi-coherent [Tag 01XB]. So every class of \(H^1(X,\Omega)\) comes from \(H^1_Y(X,\Omega)\). By Exercise 3.3 of the lesson on Chern classes of perfect complexes \(c'^1(E)\ne0\), so the class \(c^1(E,D)\) is nonzero.

**Solution 6.5.** (1) The open subsets \(D(x)\) and \(D(y)\) cover \(U\). On \(D(x)\), \(a\partial_x+b\partial_y=(a/x)\xi+(b-ay/x)\partial_y\), and \(c\xi+d\partial_y=0\) gives \(cx=0\), hence \(c=0\) and \(d=0\); so \(\Theta=B\xi\oplus B\partial_y\) there, and symmetrically \(\Theta=B\xi\oplus B\partial_x\) on \(D(y)\). The map \(B\to\Theta\), \(b\mapsto b\xi\), is injective, because the coefficient \(x\) of \(\partial_x\) is a nonzerodivisor on \(B\). So \(\mathcal F\cong B\), \(\mathcal F|_U\) is locally a direct summand of \(\Theta|_U\), and \(N|_U\) is free of rank one on \(D(x)\) and on \(D(y)\). For local sections \(b\), \(c\) of \(B\),
\[
[b\xi,c\xi]=\bigl(b\,\xi(c)-c\,\xi(b)\bigr)\xi,
\]
by the two bracket identities and \([\xi,\xi]=0\); so \(\mathcal F\) is involutive. The complex \(B\xrightarrow{\xi}\Theta\) in degrees \(-1\) and \(0\) is strictly perfect, and it is quasi-isomorphic to \(N\) because the map is injective; so \(N\) has perfect amplitude in \([-1,0]\).

(2) Partial derivatives commute, so \([\partial_x,\partial_y]=0\), and the bracket identities give
\[
\begin{aligned}&[\xi,\partial_x]=-[\partial_x,x\partial_x+y\partial_y]\\
&\quad=-\partial_x(x)\partial_x-\partial_x(y)\partial_y=-\partial_x,\end{aligned}
\]
and likewise \([\xi,\partial_y]=-\partial_y\). So \(\nabla(\bar\partial_x)(\xi)=-\bar\partial_x\) and \(\nabla(\bar\partial_y)(\xi)=-\bar\partial_y\).

(3) By (1), Corollary 4.2 applies with \(q=1\) and \(Y=\{0\}\).

**Solution 6.6.** By Lemma 5.1 (1), with \(m=0\), \(X\times_SX\) is the quotient model of \(\mathbf C^2\) by \((u^2,v^2)\), a point with the ring \(\mathbf C[u,v]/(u^2,v^2)\); the diagonal ideal is generated by \(a=v-u\). With \(s=u\), \(v^2=a^2+2as+s^2\), so the ideal \((u^2,v^2)\) is \((s^2,a^2+2as)\), and \(P^1_{X/S}=\mathbf C[a,s]/(s^2,a^2+2as,a^2)=\) \(\mathbf C[a,s]/(s^2,a^2,as)\), with basis \(1\), \(s=\lambda(z)\) and \(a+s=\rho(z)\). Its ideal \(\Omega^1_{X/S}\) is spanned by \(a=\mathrm dz\), and \(z\,\mathrm dz=\lambda(z)a=sa=0\).

**Solution 6.7.** By Lemma 5.1 (1), \(X\times_SX\) is the quotient model of \(\mathbf C^2\) by \(u^2-v^2=-(v-u)(v+u)\), and the diagonal ideal \(\mathcal I\) is generated by \(a=v-u\). Near a point \((c,c)\) with \(c\neq0\), \(v+u\) is a unit, so \(a=0\) and \(\mathcal I=0\): \(\Omega^1_{X/S}\) vanishes off the origin. At the origin, with \(s=u\), \(u^2-v^2=-a(a+2s)\), and \(\mathcal O_{X\times_SX}/\mathcal I^2\) is the quotient of the convergent power series in \(a\), \(s\) by \((a^2+2as,a^2)=(a^2,as)\); so \(\mathcal I/\mathcal I^2\) is spanned by \(a=\mathrm dz\), and \(z\,\mathrm dz=sa=0\). A module that is locally free near the origin and vanishes at nearby points is zero near the origin, while its stalk \(\mathbf C\,\mathrm dz\) at the origin is not zero; so \(\Omega^1_{X/S}\) is not locally free.

## Sources

Chern classes with supports in a closed subset, obtained from a partial connection on the complement through the topos of an open subset and its complement, are due to Illusie, in his work on the cotangent complex, where the use of Chern classes of perfect complexes in the theory of Baum and Bott is credited to an observation of Grothendieck; Illusie states the construction for smooth morphisms of schemes and of analytic spaces; the lesson works with any derivation into a locally free module of finite rank. The principal parts and differentials of complex spaces, formed on the diagonal of the fibre product, are due to Grothendieck ([*Techniques de construction en géométrie analytique VII*](https://www.numdam.org/item/SHC_1960-1961__13_2_A1_0/), Séminaire Henri Cartan 13, 1960/61, exposé 14). Partial connections, and the localization at the singular set of the characteristic classes of the normal sheaf of a foliation, are due to Baum and Bott. The partial connection of Proposition 4.1 is due to Bott.
