# Derived tensor products of simplicial modules

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The tensor product of modules over a simplicial ring \(A\) does not preserve quasi-isomorphisms: over \(A=\mathbb Z\), a free simplicial resolution of \(\mathbb Z/2\) tensored with \(\mathbb Z/2\) has the homology \(\operatorname{Tor}_*(\mathbb Z/2,\mathbb Z/2)\), which \(\mathbb Z/2\otimes\mathbb Z/2\) does not see. Its left derived functor \(E\otimes^\ell_AF\) on \(D_\bullet(A)\) is computed by replacing one factor by a module that is flat in every degree. Such replacements come from the standard free resolution, a bisimplicial module whose diagonal is the replacement. This lesson constructs the derived tensor product, proves that it is exact in each variable, and compares it with the derived tensor product of complexes when \(A\) is a ring placed in every degree. It then treats the derived extension of scalars along a map of simplicial rings, with its adjunction on Ext groups, and shows that a quasi-isomorphism of simplicial rings induces an equivalence of derived categories. The derived tensor product of simplicial algebras ends the lesson.

**Prerequisites.** [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md); Lemma 2.6 of [*Multisimplicial objects and spectral diagrams*](multisimplicial-objects-and-spectral-diagrams.md); Lemma 1.1 of [*Stable derived functors*](stable-derived-functors.md); Theorems 1.1–1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution). From the AI-integrated Stacks project: the standard simplicial object of an adjunction and its homotopy equivalence [[Stacks, Tag 08NC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial), [Tag 08ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial-homotopy)] and polynomial algebras [[Tag 08NA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-example-polynomial-algebra)]; homotopy equivalences of simplicial abelian groups [[Tag 08P2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-equivalence)]; flat modules on a ringed site [[Tag 03EX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-tor-zero), [Tag 03EY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-ses), [Tag 03EZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-resolution-of-flat), [Tag 05V4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-flat-change-of-rings)]; K-flat complexes and the derived tensor product [[Tag 06YP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-quasi-isomorphism), [Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat), [Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution), [Tag 06YU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-derived-tor)]; the spectral sequences of a double complex [[Tag 0132](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-first-quadrant-ss)]; essentially constant pro-objects [[Tag 05PU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-essentially-constant-diagram)].

## Conventions

\(T\) is the topos of sheaves on a small site and \(A\) a simplicial ring of \(T\). Modules, homotopies, \(\operatorname{Hot}_\bullet(A)\), \(D_\bullet(A)\), \(Q\colon A\text{-}\operatorname{Mod}\to D_\bullet(A)\), the cone \(\gamma\) and the suspension \(\sigma\) are as in [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md). Tensor products \(L\otimes_AE\) of \(A\)-modules are formed degreewise: \((L\otimes_AE)_n=L_n\otimes_{A_n}E_n\). An \(A\)-module \(L\) is *flat* if every \(L_n\) is a flat \(A_n\)-module. For a simplicial sheaf of sets \(X\), \(A^{(X)}\) is the free \(A\)-module on \(X\), with \((A^{(X)})_n=A_n^{(X_n)}\); it is flat, and \(A^{(X)}\otimes_AE=\mathbb Z^{(X)}\otimes_{\mathbb Z}E\) naturally.

A *bisimplicial \(A\)-module* is a simplicial object \(M=(M_{\bullet,q})_{q\geq0}\) of the category of \(A\)-modules. Its term \(M_{p,q}\) is an \(A_p\)-module; the index \(p\) is the *internal* direction, in which \(M_{\bullet,q}\) is an \(A\)-module, and \(q\) the *external* one, in which each column \(M_{p,\bullet}\) is a simplicial \(A_p\)-module. The diagonal \(\Delta M\), with \((\Delta M)_n=M_{n,n}\), is an \(A\)-module. An \(A\)-module \(E\), regarded as constant in the external direction, is a bisimplicial module \(cE\) with \(\Delta cE=E\).

## 1. Bisimplicial modules and the standard resolution

**Lemma 1.1 (diagonals).** Let \(f\colon M\to M'\) be a map of bisimplicial abelian sheaves. If every column map \(f_{p,\bullet}\) is a quasi-isomorphism, then \(\Delta f\) is a quasi-isomorphism. The same holds if every row map \(f_{\bullet,q}\) is a quasi-isomorphism.

**Proof.** By Lemma 2.6 of the lesson on multisimplicial objects, there are natural homotopy equivalences between \(N\Delta M\) and the total complex of the double complex \(NM\) obtained by normalizing in both directions. So it suffices that \(\operatorname{Tot}(Nf)\) is a quasi-isomorphism. Normalize the external direction first. The column \(p\) of \(NM\) is then the subcomplex of \(N(M_{p,\bullet})\) cut out by the internal faces \(d_1,\ldots,d_p\). It is a direct summand of \(N(M_{p,\bullet})\), naturally in \(M\): it is the Moore part of the simplicial object \(p\mapsto N(M_{p,\bullet})\) of the abelian category of complexes (Theorem 1.1 of *The cotangent complex*). A natural direct summand of a quasi-isomorphism is a quasi-isomorphism, so \(Nf\) is a quasi-isomorphism on every column. Let \(K\) be the double complex whose column \(p\) is the cone of the column map \((Nf)_p\). Its columns are acyclic, it vanishes outside the region \(p\geq0\), \(q\geq-1\), and \(\operatorname{Tot}K\) is the cone of \(\operatorname{Tot}(Nf)\). The spectral sequence of \(K\) whose first page is the homology of the columns is zero from the first page on and converges to \(H_*(\operatorname{Tot}K)\) [Stacks, Tag 0132]. So \(\operatorname{Tot}K\) is acyclic. The case of rows is symmetric. \(\square\)

**Construction 1.2 (standard free resolution).** The free module functor \(X\mapsto A^{(X)}\), from simplicial sheaves of sets to \(A\)-modules, is left adjoint to the forgetful functor \(V\). For an \(A\)-module \(L\), let \(F_A(L)\) be the standard simplicial object of this adjunction evaluated at \(L\) [Stacks, Tag 08NC]: the bisimplicial \(A\)-module with external terms
\[
F_A(L)_{\bullet,q}=\bigl(A^{(V(-))}\bigr)^{q+1}(L),
\]
with external faces induced by the counit \(A^{(VL)}\to L\) and degeneracies induced by the unit \(X\to VA^{(X)}\). It comes with an augmentation \(F_A(L)\to cL\). Put
\[
P(L)=\Delta F_A(L),
\]
with the map \(P(L)\to L\) induced by the augmentation.

**Lemma 1.3.** Let \(L\) be an \(A\)-module.

1. For every \(p\), the augmentation makes the column \(F_A(L)_{p,\bullet}\) a resolution of \(L_p\): its homology is \(L_p\) in degree \(0\) and zero in positive degrees. Every term \(F_A(L)_{p,q}\) is a free \(A_p\)-module.
2. \(P(L)\) is flat, \(P(L)\to L\) is a quasi-isomorphism, and both are natural in \(L\).
3. \(P\) carries quasi-isomorphisms to quasi-isomorphisms.

**Proof.** (1) By [Stacks, Tag 08ND], after applying \(V\) the augmentation \(VF_A(L)\to VcL\) is a homotopy equivalence of simplicial objects, in the external direction, of the category of simplicial sheaves of sets. Evaluating at an internal degree \(p\) and at an object of the site gives, for the sections, a map of simplicial abelian groups that is a homotopy equivalence of simplicial sets. It is a quasi-isomorphism [Stacks, Tag 08P2]. Homology commutes with sheafification, so \(F_A(L)_{p,\bullet}\to L_p\) is a quasi-isomorphism. The terms are free modules on sheaves of sets.

(2) \(P(L)_n=F_A(L)_{n,n}\) is a free \(A_n\)-module. By (1) the map \(F_A(L)\to cL\) is a quasi-isomorphism on every column, so \(P(L)=\Delta F_A(L)\to\Delta cL=L\) is a quasi-isomorphism by Lemma 1.1. The construction is functorial.

(3) If \(f\colon L\to L'\) is a quasi-isomorphism, then \(P(L)\to L\to L'\) and \(P(L)\xrightarrow{P(f)}P(L')\to L'\) agree, so \(P(f)\) is a quasi-isomorphism by two out of three. \(\square\)

In particular every \(A\)-module has a flat replacement, natural in the module.

## 2. Flatness and quasi-isomorphisms

**Lemma 2.1 (constant rings).** Let \(\Lambda\) be a ring of \(T\), \(L\) a simplicial \(\Lambda\)-module and \(f\colon E\to F\) a quasi-isomorphism of simplicial \(\Lambda\)-modules. If \(L\) is flat, or if \(E\) and \(F\) are flat, then \(L\otimes_\Lambda f\) is a quasi-isomorphism.

**Proof.** By the Eilenberg–Zilber theorem (Theorem 1.3 of *The cotangent complex*, valid for sheaves of modules), \(N(L\otimes_\Lambda E)\) is naturally homotopy equivalent to \(\operatorname{Tot}(NL\otimes_\Lambda NE)\). Since \(N_nL\) is a direct summand of \(L_n\), \(NL\) is a complex of flat modules if \(L\) is flat. Placed in nonpositive cohomological degrees it is bounded above, hence K-flat [Stacks, Tag 06YQ], and \(\operatorname{Tot}(NL\otimes_\Lambda-)\) preserves quasi-isomorphisms [Stacks, Tag 06YP]. This is the first case. In the second, \(NE\) and \(NF\) are K-flat. Choose a quasi-isomorphism \(K\to NL\) from a K-flat complex [Stacks, Tag 06YS]. In the commutative square formed by \(\operatorname{Tot}(K\otimes NE)\to\operatorname{Tot}(K\otimes NF)\) and \(\operatorname{Tot}(NL\otimes NE)\to\operatorname{Tot}(NL\otimes NF)\), the two vertical maps are quasi-isomorphisms because \(NE\) and \(NF\) are K-flat, and the upper map is one because \(K\) is K-flat. So the lower map is a quasi-isomorphism. \(\square\)

**Proposition 2.2.** Let \(L\) be an \(A\)-module and \(f\colon E\to F\) a quasi-isomorphism of \(A\)-modules. If \(L\) is flat, or if \(E\) and \(F\) are flat, then \(L\otimes_Af\colon L\otimes_AE\to L\otimes_AF\) is a quasi-isomorphism.

**Proof.** Tensor the augmentation \(F_A(L)\to cL\) with \(f\). This gives a commutative square of bisimplicial modules
\[
\begin{array}{ccc}
F_A(L)\otimes_AcE&\longrightarrow&F_A(L)\otimes_AcF\\
\downarrow&&\downarrow\\
c(L\otimes_AE)&\longrightarrow&c(L\otimes_AF),
\end{array}
\]
whose diagonal is the square formed by \(P(L)\otimes_Af\) and \(L\otimes_Af\). The row \(q\) of the upper map is \(A^{(X_q)}\otimes_Af=\mathbb Z^{(X_q)}\otimes_{\mathbb Z}f\), where \(X_q\) is the simplicial sheaf underlying \(F_A(L)_{\bullet,q-1}\) (with \(F_A(L)_{\bullet,-1}=L\)). This is a quasi-isomorphism by Lemma 2.1 for \(\Lambda=\mathbb Z\), since \(\mathbb Z^{(X_q)}\) is flat. So the upper diagonal map is a quasi-isomorphism by Lemma 1.1. The column \(p\) of the left vertical map is the augmented complex \(F_A(L)_{p,\bullet}\otimes_{A_p}E_p\to L_p\otimes_{A_p}E_p\). By Lemma 1.3 (1), \(F_A(L)_{p,\bullet}\) is a resolution of \(L_p\) by free \(A_p\)-modules. If \(E_p\) is flat, tensoring with \(E_p\) keeps it exact. If \(L_p\) is flat, it stays exact after tensoring with any module [Stacks, Tag 03EZ]. In both cases the left vertical map is a quasi-isomorphism on every column, and so is the right one; by Lemma 1.1 their diagonals are quasi-isomorphisms. By two out of three, \(L\otimes_Af\) is a quasi-isomorphism. \(\square\)

## 3. The derived tensor product

**Definition 3.1.** For \(A\)-modules \(E\) and \(F\) put
\[
E\otimes^\ell_AF=P(E)\otimes_AP(F).
\]
By Lemma 1.3 and Proposition 2.2, this functor of two variables carries quasi-isomorphisms in either variable to quasi-isomorphisms. It therefore induces a functor in each variable on \(D_\bullet(A)\), and the two commute, which gives a functor
\[
-\otimes^\ell_A-\colon D_\bullet(A)\times D_\bullet(A)\to D_\bullet(A).
\]
The symmetry of the tensor product makes it symmetric, and the natural map \(E\otimes^\ell_AF\to E\otimes_AF\) is induced by the augmentations.

**Proposition 3.2.** Let \(E\) and \(F\) be \(A\)-modules.

1. If \(s\colon L\to E\) and \(t\colon M\to F\) are quasi-isomorphisms and \(L\) or \(M\) is flat, the natural maps identify \(E\otimes^\ell_AF\) with \(L\otimes_AM\) in \(D_\bullet(A)\). In particular \(E\otimes^\ell_AF\cong L\otimes_AF\) when \(L\) is flat.
2. The pro-object of \(D_\bullet(A)\) given by \(L\otimes_AM\), indexed by the pairs of quasi-isomorphisms \(L\to E\), \(M\to F\) of \(\operatorname{Hot}_\bullet(A)\), is essentially constant with value \(E\otimes^\ell_AF\) [Stacks, Tag 05PU]. So \(\otimes^\ell_A\) is the left derived functor of \(\otimes_A\colon\) \(\operatorname{Hot}_\bullet(A)\times\operatorname{Hot}_\bullet(A)\to\) \(\operatorname{Hot}_\bullet(A)\).

**Proof.** (1) Suppose that \(L\) is flat. In the sequence
\[
\begin{aligned}&P(E)\otimes P(F)\\&\quad \xleftarrow{P(s)\otimes1}P(L)\otimes P(F)\\&\quad \to L\otimes P(F)\\&\quad \xleftarrow{1\otimes P(t)}L\otimes P(M) \to L\otimes M\end{aligned}
\]
all maps are quasi-isomorphisms by Proposition 2.2: the first two because \(P(F)\) is flat and \(P(s)\) and \(P(L)\to L\) are quasi-isomorphisms, the last two because \(L\) is flat and \(P(t)\) and \(P(M)\to M\) are quasi-isomorphisms. If \(M\) is flat, exchange the roles of the two factors.

(2) The index category is cofiltered by the right calculus of fractions (Theorem 4.2 (1) of the lesson on simplicial rings and modules). For an index \(j=(s\colon L\to E,\ t\colon M\to F)\), let \(c_j\colon E\otimes^\ell_AF\to L\otimes_AM\) be the inverse of the isomorphism \(s\otimes^\ell t\) followed by the map \(L\otimes^\ell_AM\to L\otimes_AM\). By functoriality the \(c_j\) form a cone over the pro-object, and \(c_j\) is an isomorphism when \(L\) or \(M\) is flat, by (1). Let \(i=(P(E)\to E,\ P(F)\to F)\). For any index \(j\), the index \(k=(P(L)\to E,\ P(M)\to F)\) maps to \(i\) by \(P(s),P(t)\) and to \(j\) by the augmentations, so \(c_i\) and \(c_j\) are the composites of \(c_k\) with the maps from the value at \(k\). Since \(c_k\) is invertible, the map from the value at \(k\) to the value at \(j\) is \(c_jc_k^{-1}\), the composite of the map from the value at \(k\) to the value at \(i\), which is \(c_ic_k^{-1}\), with \(c_i^{-1}\) and \(c_j\). With the morphism \(c_i^{-1}\) from the value at \(i\), these are the conditions of [Stacks, Tag 05PU]. \(\square\)

**Proposition 3.3 (exactness).** Let \(E\) be an \(A\)-module. The functor \(E\otimes^\ell_A-\) on \(D_\bullet(A)\) commutes with the suspension, and it carries distinguished triangles to distinguished triangles. The same holds in the other variable.

**Proof.** Put \(L=P(E)\). By Proposition 3.2 (1), \(E\otimes^\ell_AF\cong L\otimes_AF\), naturally in \(F\). The functor \(L\otimes_A-\) preserves quasi-isomorphisms by Proposition 2.2. It commutes with the degreewise tensor product by \(\gamma_{\mathbb Z}\) and \(\sigma_{\mathbb Z}\), so \(L\otimes\sigma F=\sigma(L\otimes F)\), and with pushouts, so it carries the cone \(C(u)\) of a map \(u\colon F\to F'\), with its maps \(j\) and \(p\), to the cone of \(L\otimes u\). Hence it carries the triangle of \(u\) to the triangle of \(L\otimes u\), and distinguished triangles to distinguished triangles. The other variable follows by symmetry. \(\square\)

**Proposition 3.4 (constant rings).** Let \(A\) be the constant simplicial ring of a ring \(\Lambda\), and identify \(D_\bullet(\Lambda)\) with \(D^{\leq0}(\Lambda)\) through normalization (Lemma 1.1 of the lesson on stable derived functors). Then \(N(E\otimes^\ell_\Lambda F)\cong NE\otimes^{\mathbf L}_\Lambda NF\) in \(D(\Lambda)\) [Stacks, Tag 06YU], naturally in \(E\) and \(F\).

**Proof.** By Eilenberg–Zilber, \(N(P(E)\otimes_\Lambda P(F))\) is naturally homotopy equivalent to \(\operatorname{Tot}(NP(E)\otimes_\Lambda NP(F))\). The complex \(NP(E)\) is bounded above with flat terms, hence K-flat [Stacks, Tag 06YQ], and quasi-isomorphic to \(NE\). So this total complex computes \(NE\otimes^{\mathbf L}_\Lambda NF\). \(\square\)

For instance, for constant \(\Lambda\)-modules \(E\) and \(F\) the homology of \(E\otimes^\ell_\Lambda F\) is \(\operatorname{Tor}^\Lambda_*(E,F)\).

## 4. Extension of scalars

Let \(f\colon A\to B\) be a map of simplicial rings. Restriction of scalars from \(B\)-modules to \(A\)-modules is exact, preserves quasi-isomorphisms and induces a functor \(D_\bullet(B)\to D_\bullet(A)\), which we do not write. For an \(A\)-module \(E\) put
\[
B\otimes^\ell_AE=B\otimes_AP(E).
\]
If \(L\) is a flat \(A\)-module, \(B\otimes_AL\) is a flat \(B\)-module in every degree [Stacks, Tag 05V4].

**Proposition 4.1.** The functor \(B\otimes^\ell_A-\) carries quasi-isomorphisms to quasi-isomorphisms and induces a functor \(D_\bullet(A)\to D_\bullet(B)\). For every quasi-isomorphism \(L\to E\) with \(L\) flat, \(B\otimes^\ell_AE\cong B\otimes_AL\) naturally, and the pro-object \(B\otimes_AM\) over the quasi-isomorphisms \(M\to E\) of \(\operatorname{Hot}_\bullet(A)\) is essentially constant with value \(B\otimes^\ell_AE\). The functor commutes with the suspension and carries distinguished triangles to distinguished triangles.

**Proof.** A map of \(B\)-modules is a quasi-isomorphism if and only if it is one of \(A\)-modules. For a quasi-isomorphism \(L'\to L\) of flat \(A\)-modules, \(B\otimes_AL'\to B\otimes_AL\) is a quasi-isomorphism by Proposition 2.2 (second case). Hence \(B\otimes_AP(-)\) preserves quasi-isomorphisms, and for a flat replacement \(L\to E\) the maps \(B\otimes_AP(E)\leftarrow B\otimes_AP(L)\to B\otimes_AL\) are quasi-isomorphisms. The statement on pro-objects follows as in Proposition 3.2 (2). The functor \(B\otimes_A-\) commutes with \(\sigma\) and with cones, so the last statement follows as in Proposition 3.3. \(\square\)

**Proposition 4.2 (adjunction).** The functor \(B\otimes^\ell_A-\colon D_\bullet(A)\to D_\bullet(B)\) is left adjoint to restriction of scalars. For \(E\in D_\bullet(A)\), \(F\in D_\bullet(B)\) and \(n\in\mathbb Z\) there are isomorphisms
\[
\operatorname{Ext}^n_B(B\otimes^\ell_AE,F)\cong\operatorname{Ext}^n_A(E,F),
\]
natural in \(E\) and \(F\). They carry the long exact sequences of Theorem 3.9 of the lesson on triangles, for a distinguished triangle in either variable, to each other.

**Proof.** Write \(a\colon P\to1\) for the augmentation, and \(u_L\colon L\to B\otimes_AL\), \(c_F\colon B\otimes_AF\to F\) for the unit and counit of extension and restriction of scalars on modules. For an \(A\)-module \(E\) and a \(B\)-module \(F\) put
\[
\begin{gathered}\eta_E=Q(u_{P(E)})\,Q(a_E)^{-1},\\ \varepsilon_F=c_F\circ(1\otimes a_F),\end{gathered}
\]
a morphism \(E\to B\otimes^\ell_AE\) of \(D_\bullet(A)\) and a map \(B\otimes_AP(F)\to F\) of \(B\)-modules, both natural. All functors involved preserve quasi-isomorphisms, so \(\eta\) and \(\varepsilon\) are natural transformations on the derived categories.

*The first triangle identity.* By naturality of \(u\), \((1\otimes a_F)\,u_{P(F)}=u_F\,a_F\), and \(c_Fu_F=1\). So the composite of \(\eta_F\) with \(\varepsilon_F\), regarded as a map of \(A\)-modules, is \(Q(a_F)Q(a_F)^{-1}=1\).

*The second triangle identity.* The composite \(\varepsilon_{B\otimes^\ell E}\circ(B\otimes^\ell\eta_E)\) is \(c\circ\) \((1\otimes a_{B\otimes P(E)})\circ\) \((1\otimes P(u_{P(E)}))\circ\) \(Q(1\otimes P(a_E))^{-1}\). Naturality of \(a\) gives \(a_{B\otimes P(E)}P(u_{P(E)})=u_{P(E)}a_{P(E)}\), and \(c\circ(1\otimes u_{P(E)})=1\). So the composite is \(Q(1\otimes a_{P(E)})\,Q(1\otimes P(a_E))^{-1}\). The two maps \(a_{P(E)}\) and \(P(a_E)\) from \(P(P(E))\) to \(P(E)\) are equal in \(D_\bullet(A)\), because their composites with the isomorphism \(a_E\) agree. They remain equal after \(B\otimes_A-\): if \(f,g\colon X\to Y\) are maps of flat modules with \(Q(f)=Q(g)\), then \(ft\simeq gt\) for a quasi-isomorphism \(t\), which may be taken from a flat module by composing with an augmentation; then \(B\otimes t\) is a quasi-isomorphism and \((B\otimes f)(B\otimes t)\simeq(B\otimes g)(B\otimes t)\). So the composite is the identity.

This proves the adjunction, hence the case \(n=0\). For general \(n\), take \(m=\max(0,-n)\). The flat replacement \(\sigma^mP(E)\) of \(\sigma^mE\) gives \(B\otimes^\ell_A\sigma^mE\cong\sigma^m(B\otimes^\ell_AE)\) (Proposition 4.1), and
\[
\begin{aligned}&\operatorname{Hom}_B(\sigma^m(B\otimes^\ell_AE),\sigma^{m+n}F)\\&\quad \cong\operatorname{Hom}_B(B\otimes^\ell_A\sigma^mE,\sigma^{m+n}F)\\&\quad \cong\operatorname{Hom}_A(\sigma^mE,\sigma^{m+n}F).\end{aligned}
\]
Restriction of scalars commutes with \(\sigma\), and so do the unit and counit, because \(B\otimes_A\sigma L=\sigma(B\otimes_AL)\). So the isomorphisms are compatible with the transition maps of the colimits defining Ext and with the isomorphisms of Proposition 2.2 (1) of the lesson on triangles. Since \(B\otimes^\ell_A-\) carries distinguished triangles to distinguished triangles, and the isomorphisms are natural, they commute with the maps of the long exact sequences, including the connecting maps. \(\square\)

**Corollary 4.3.** If \(f\colon A\to B\) is a quasi-isomorphism of simplicial rings, then \(B\otimes^\ell_A-\colon D_\bullet(A)\to D_\bullet(B)\) and restriction of scalars are inverse equivalences.

**Proof.** For an \(A\)-module \(E\), the unit \(\eta_E\) is represented by \(P(E)=P(E)\otimes_AA\to P(E)\otimes_AB\), which is \(P(E)\otimes_Af\), a quasi-isomorphism by Proposition 2.2 since \(P(E)\) is flat. For a \(B\)-module \(F\), the composite of the unit at \(F\), regarded as an \(A\)-module, with the counit \(\varepsilon_F\), regarded as a map of \(A\)-modules, is the identity of \(F\) by a triangle identity. The unit is an isomorphism, so \(\varepsilon_F\) is a quasi-isomorphism of \(A\)-modules, hence of \(B\)-modules. \(\square\)

**Proposition 4.4 (transitivity).** For maps \(A\to B\to C\) of simplicial rings and \(E\in D_\bullet(A)\) there is an isomorphism \(C\otimes^\ell_B(B\otimes^\ell_AE)\cong C\otimes^\ell_AE\), natural in \(E\).

**Proof.** \(B\otimes_AP(E)\) is a flat \(B\)-module, so by Proposition 4.1 the left side is \(C\otimes_B(B\otimes_AP(E))=C\otimes_AP(E)\), the right side. \(\square\)

## 5. Simplicial algebras

Let \(A\text{-}\mathrm{Alg}\) be the category of simplicial \(A\)-algebras, with its homotopy category \(\operatorname{Hot}(A\text{-}\mathrm{Alg})\) and its derived category \(D(A\text{-}\mathrm{Alg})\) (Theorem 4.2 (2) of the lesson on simplicial rings and modules). An algebra is *flat* if its underlying module is flat.

**Lemma 5.1.** For every \(A\)-algebra \(B\) there is a quasi-isomorphism of \(A\)-algebras \(P^{\mathrm{alg}}(B)\to B\), natural in \(B\), such that \(P^{\mathrm{alg}}(B)_n\) is a polynomial \(A_n\)-algebra for every \(n\). In particular \(P^{\mathrm{alg}}(B)\) is flat.

**Proof.** The polynomial algebra functor \(X\mapsto A[X]\), from simplicial sheaves of sets to \(A\)-algebras, with \(A[X]_n=A_n[X_n]\), is left adjoint to the forgetful functor [Stacks, Tag 08NA]. Its standard simplicial object, evaluated at \(B\), is a simplicial object of \(A\)-algebras, augmented to \(B\). After forgetting to simplicial sheaves of sets the augmentation is a homotopy equivalence [Stacks, Tag 08ND]. As in Lemma 1.3, every column is a resolution of the corresponding \(B_p\), so the diagonal \(P^{\mathrm{alg}}(B)\to B\) is a quasi-isomorphism by Lemma 1.1. It is a map of algebras because all the structure maps are. In degree \(n\) the diagonal is a polynomial \(A_n\)-algebra on a sheaf of sets, free as an \(A_n\)-module on its monomials. \(\square\)

**Proposition 5.2.** Let \(B\) and \(C\) be \(A\)-algebras. The pro-object \(P'\otimes_AC'\) of \(D(A\text{-}\mathrm{Alg})\), indexed by the pairs of quasi-isomorphisms \(P'\to B\), \(C'\to C\) of \(\operatorname{Hot}(A\text{-}\mathrm{Alg})\), is essentially constant. Its value, written \(B\otimes^\ell_AC\), is \(P'\otimes_AC\) for every flat \(P'\), and \(B\otimes_AC'\) for every flat \(C'\). So \(\otimes^\ell_A\) is the left derived functor of the tensor product of algebras on the homotopy category. Its underlying module is \(B\otimes^\ell_AC\) in the sense of Definition 3.1.

**Proof.** The index category is cofiltered by the right calculus of fractions for algebras. By Lemma 5.1 the flat algebras are cofinal. If \(P'\) is flat, then \(P'\otimes_AC''\to P'\otimes_AC'\) is a quasi-isomorphism for every quasi-isomorphism \(C''\to C'\), by Proposition 2.2, and it is a map of algebras. The proof of Proposition 3.2 (2) applies, with \(P^{\mathrm{alg}}\) in place of \(P\). The last statement is Proposition 3.2 (1), applied to the flat module underlying \(P^{\mathrm{alg}}(B)\). \(\square\)

## 6. Exercises

**6.1.** Show that \(A\otimes^\ell_AE\cong E\) for every \(A\)-module \(E\), and that \(B\otimes^\ell_AA\cong B\) for every map of simplicial rings \(A\to B\).

**6.2.** Let \(A=\mathbb Z\) in the topos of sets. Let \(s\colon P(\mathbb Z/2)\to\mathbb Z/2\) be the flat replacement of the constant module \(\mathbb Z/2\). Show that \(s\otimes\mathbb Z/2\) is not a quasi-isomorphism, and compute \(H_*(\mathbb Z/2\otimes^\ell_{\mathbb Z}\mathbb Z/2)\).

**6.3.** Let \(f\colon A\to B\) be a map of simplicial rings in the topos of sets. Using Proposition 4.2 and Example 2.5 of the lesson on triangles, show that \(\operatorname{Ext}^{-q}_A(A,F)\cong\pi_q(F)\) for every \(B\)-module \(F\) and \(q\geq0\).

## 7. Complete solutions

**6.1.** \(A\) is a flat \(A\)-module, so by Proposition 3.2 (1), \(A\otimes^\ell_AE\cong A\otimes_AE=E\). Likewise, by Proposition 4.1, \(B\otimes^\ell_AA\cong B\otimes_AA=B\).

**6.2.** \(H_*(P(\mathbb Z/2))\) is \(\mathbb Z/2\) in degree \(0\). By Proposition 3.4, \(H_n(P(\mathbb Z/2)\otimes\mathbb Z/2)=\) \(H_n(\mathbb Z/2\otimes^\ell\mathbb Z/2)=\) \(\operatorname{Tor}^{\mathbb Z}_n(\mathbb Z/2,\mathbb Z/2)\), which is \(\mathbb Z/2\) for \(n=0,1\) and \(0\) for \(n\geq2\). The constant module \(\mathbb Z/2\otimes\mathbb Z/2=\mathbb Z/2\) has no homology in degree \(1\), so \(s\otimes\mathbb Z/2\) is not a quasi-isomorphism.

**6.3.** By Proposition 4.2 with \(E=A\), \(\operatorname{Ext}^n_B(B\otimes^\ell_AA,F)\cong\operatorname{Ext}^n_A(A,F)\), and \(B\otimes^\ell_AA\cong B\) by Exercise 6.1. By Example 2.5 of the lesson on triangles, applied over \(B\), \(\operatorname{Ext}^{-q}_B(B,F)=\pi_q(F)\).

## Sources

Derived tensor products of simplicial modules, extension of scalars along maps of simplicial rings and the invariance of the derived category under quasi-isomorphisms of simplicial rings are due to Illusie, in his work on the cotangent complex. The standard free resolution goes back to Godement's standard constructions and their use for simplicial resolutions by André and Quillen. The K-flat complexes used for constant rings are those of the Stacks project.
