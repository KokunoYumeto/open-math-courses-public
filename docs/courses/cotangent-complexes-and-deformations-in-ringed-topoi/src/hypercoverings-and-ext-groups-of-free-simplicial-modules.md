# Hypercoverings and Ext groups of free simplicial modules

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Lambda\) be a ring of a topos \(T\) with enough points, and \(X\) a simplicial sheaf. On derived categories, the free simplicial \(\Lambda\)-module \(\Lambda^{(X)}\) is left adjoint to the functor forgetting the module structure. So the Ext groups \(\operatorname{Ext}^p(\Lambda^{(X)},F)\) of a simplicial \(\Lambda\)-module \(F\) are morphisms of the simplicial derived category of \(T\), from \(X\) to the \(p\)-fold suspension of \(F\). When \(X\) is a Kan simplicial sheaf, the right fractions write these morphisms as a colimit over the fibrant quasi-isomorphisms \(X'\to X\). The terms of the colimit are the cohomology groups of an explicit complex built from the maps \(X'_j\to F_i\). For \(X\) the final object, the \(X'\) are the hypercoverings of \(T\), and for a \(\Lambda\)-module \(F\) the complex is the Čech complex of \(X'\): sheaf cohomology is the colimit over the hypercoverings of their Čech cohomology. This is Verdier's hypercovering theorem.

The same computation shows that, unlike for simplicial sets, the homotopy classes of maps between Kan simplicial sheaves need not give all the morphisms between them in the simplicial derived category. For the classifying topos of the group \(\mathbb Z\), a generator of the first cohomology group with coefficients in \(\mathbb Z\) is such a morphism.

**Prerequisites.** [*The simplicial derived category of a topos*](the-simplicial-derived-category-of-a-topos.md) (Conventions, Section 1, Corollary 3.3, Definition 4.2); [*Local fibrations and Kan's subdivision functor*](local-fibrations-and-kan-s-subdivision-functor.md) (Lemmas 2.2–2.3, Theorem 3.7 and its proof, Propositions 4.1 and 4.3); [*Simplicial groups and right fractions*](simplicial-groups-and-right-fractions.md) (Proposition 1.2, Proposition 3.1, Section 4); [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md) (Definition 2.1 and the paragraph after it, Theorem 3.1); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md) (Conventions, Lemma 1.1, Section 4, Remark 4.3); [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md) (Conventions, Section 1.1, Definition 2.1, Proposition 2.4); [*Cohomology of simplicial topoi and cohomological descent*](cohomology-of-simplicial-topoi-and-cohomological-descent.md) (the definition of hypercoverings before Corollary 5.3, Exercise 6.1); [*The cotangent complex*](course:AG-HP/the-cotangent-complex), Theorems 1.1 and 1.2 (normalization and Dold–Kan); [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), expression (1.8). From the AI-integrated Stacks project: homotopic maps of simplicial objects give homotopic chain maps [[Stacks, Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N)]; Hom complexes [[Tag 0A8H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-section-hom-complexes)]; Ext groups through injective resolutions [[Tag 06XR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-compute-ext-resolutions)].

## Conventions

As in the lessons on the simplicial derived category, on local fibrations and on simplicial groups: \(T=\operatorname{Sh}(\mathcal C)\) for a small site \(\mathcal C\), \(e\) is the final simplicial sheaf, \(\underline{\operatorname{Homs}}\) are mapping objects, \(\operatorname{Hom}(K,X)\) is the sheaf of maps from a finite simplicial set \(K\) to \(X\), \(\operatorname{Hot}(X,Y)=\pi_0\operatorname{Hom}(X,Y)\) is the set of homotopy classes of maps, fibrations are the local fibrations, and a *fibrant quasi-isomorphism* is a map that is both. \(\Lambda\) is a commutative ring of \(T\), regarded as a constant simplicial ring. Simplicial \(\Lambda\)-modules, \(K\odot E\), \(\underline{\operatorname{Homs}}_\Lambda\), \(\operatorname{Hot}_\Lambda\) and \(D_\bullet(\Lambda)\) are as in the lesson on simplicial rings and modules. The cone \(\gamma E\), the suspension \(\sigma E\), the sequence \(\mathsf c_E\) and the groups \(\operatorname{Ext}^p_\Lambda\) are as in the lesson on triangles and Ext groups; for \(p\geq0\), \(\operatorname{Ext}^p_\Lambda(E,F)=\operatorname{Hom}_{D_\bullet(\Lambda)}(E,\sigma^pF)\).

For a simplicial \(\Lambda\)-module \(V\), \(NV\) is its Moore complex, \(CV\) its unnormalized complex, with differential \(\sum_i(-1)^id_i\), and \(DV\subset CV\) the subcomplex of degenerate elements. Complexes are graded homologically. \(L[p]\) is the complex with \(L[p]_n=L_{n-p}\) and differential \((-1)^pd\); placing \(L_n\) in cohomological degree \(-n\), this is the usual shift. A complex is *contractible* if its identity is chain homotopic to \(0\). \(H^p(T,F)\) is the \(p\)-th derived functor of \(\Gamma(T,-)\) on \(\Lambda\)-modules.

## 1. Free simplicial modules

For a simplicial sheaf \(X\), \(\Lambda^{(X)}\) is the simplicial \(\Lambda\)-module whose terms are the free \(\Lambda\)-modules \(\Lambda^{(X_n)}=\Lambda\otimes_{\mathbb Z}\mathbb Z^{(X_n)}\).

**Lemma 1.1.**

1. For a simplicial \(\Lambda\)-module \(F\), the \(\Lambda\)-linear maps \(\Lambda^{(X)}\to F\) are the maps \(X\to F\) of simplicial sheaves.
2. For a simplicial set \(K\), \(\Lambda^{(K\times X)}=K\odot\Lambda^{(X)}\). The simplicial abelian group of global sections of \(\underline{\operatorname{Homs}}_\Lambda(\Lambda^{(X)},F)\) is the simplicial set \(\operatorname{Hom}(X,F)\), with the pointwise addition, and \(\operatorname{Hot}_\Lambda(\Lambda^{(X)},F)=\operatorname{Hot}(X,F)\).
3. A map of simplicial \(\Lambda\)-modules is a quasi-isomorphism if and only if the underlying map of simplicial sheaves is one.

**Proof.** (1) In each degree, the free module on a sheaf is left adjoint to the forgetful functor, and the adjoint maps are compatible with the faces and degeneracies by naturality.

(2) In degree \(n\) both sides are \(\bigoplus_{K_n}\Lambda^{(X_n)}\), with the same simplicial operators. An \(n\)-simplex of the global sections of \(\underline{\operatorname{Homs}}_\Lambda(\Lambda^{(X)},F)\) is a linear map \(\Delta[n]\odot\Lambda^{(X)}\to F\), that is, a linear map \(\Lambda^{(\Delta[n]\times X)}\to F\), that is, by (1), a map \(\Delta[n]\times X\to F\). Both groups \(\operatorname{Hot}\) are the \(\pi_0\) of this simplicial set (Lemma 1.1 of the lesson on simplicial rings and modules, Section 1.2 of the lesson on the simplicial derived category).

(3) The quasi-isomorphisms of simplicial modules are the maps inducing isomorphisms on the homology sheaves of the Moore complexes. By the paragraph after Definition 2.1 of the lesson on homotopy sheaves, these are the quasi-isomorphisms of the underlying simplicial sheaves. \(\square\)

**Proposition 1.2.** If \(T\) has enough points, \(\Lambda^{(-)}\) carries quasi-isomorphisms of simplicial sheaves to quasi-isomorphisms.

**Proof.** Let \(f\colon X\to Y\) be a quasi-isomorphism and \(x\) a point of a conservative family. The stalk of \(\Lambda^{(f)}\) at \(x\) is \(\Lambda_x\otimes_{\mathbb Z}\mathbb Z[f_x]\). By Corollary 3.3 (3) of the lesson on the simplicial derived category, \(f_x\) is a quasi-isomorphism of simplicial sets. So \(\mathbb Z[f_x]\) is one (Theorem 3.1 of the lesson on homotopy sheaves), and so is the map \(C\mathbb Z[f_x]\) of unnormalized complexes, which have the same homology as the Moore complexes (Theorem 1.1 of the lesson on the cotangent complex).

The cone \(P\) of \(C\mathbb Z[f_x]\) is an acyclic complex of free abelian groups in degrees \(\geq0\). Its groups of boundaries \(B_{n-1}=d(P_n)\) are free, as subgroups of free abelian groups. So the exact sequences \(0\to B_n\to P_n\to B_{n-1}\to0\) split, and the splittings give a contraction of \(P\). Hence \(\Lambda_x\otimes P\), the cone of \(\Lambda_x\otimes C\mathbb Z[f_x]=C(\Lambda^{(f)})_x\), is contractible. So \(C(\Lambda^{(f)})\), and with it \(N(\Lambda^{(f)})\), induces isomorphisms on the stalks at \(x\) of the homology sheaves. These stalks detect isomorphisms of sheaves, so \(\Lambda^{(f)}\) is a quasi-isomorphism. \(\square\)

**Proposition 1.3.** Suppose that \(T\) has enough points. Then \(\Lambda^{(-)}\) and the forgetful functor induce functors \(D_\bullet(T)\to D_\bullet(\Lambda)\) and \(D_\bullet(\Lambda)\to D_\bullet(T)\), and the first is left adjoint to the second:
\[
\begin{aligned}&\operatorname{Hom}_{D_\bullet(\Lambda)}(\Lambda^{(X)},F)\\&\quad\cong\operatorname{Hom}_{D_\bullet(T)}(X,F),\end{aligned}
\]
naturally in \(X\) and \(F\). Let \(s\colon X'\to X\) be a quasi-isomorphism and \(u\colon X'\to F\) a map, and let \(\tilde u\colon\Lambda^{(X')}\to F\) be the linear map extending \(u\). From right to left, the bijection carries \(us^{-1}\) to \(\tilde u\,\Lambda^{(s)}{}^{-1}\).

**Proof.** Both functors carry quasi-isomorphisms to quasi-isomorphisms (Proposition 1.2 and Lemma 1.1 (3)). \(D_\bullet(T)\) and \(D_\bullet(\Lambda)\) are the localizations of the categories of simplicial sheaves and of simplicial \(\Lambda\)-modules with respect to the quasi-isomorphisms (Definition 4.2 of the lesson on the simplicial derived category, Section 4 of the lesson on simplicial rings and modules). So both functors are defined on them. So are the unit \(X\to\Lambda^{(X)}\) and the counit \(\varepsilon_F\colon\Lambda^{(F)}\to F\) of the adjunction of Lemma 1.1 (1): a natural transformation between functors that invert the quasi-isomorphisms is natural on the localization (Conventions of the lesson on the simplicial derived category). The triangle identities hold before localization, hence after. From right to left, the bijection is \(\varphi\mapsto\varepsilon_F\circ\Lambda^{(\varphi)}\). For \(\varphi=us^{-1}\) this is \(\varepsilon_F\Lambda^{(u)}\Lambda^{(s)}{}^{-1}=\tilde u\,\Lambda^{(s)}{}^{-1}\). \(\square\)

**Corollary 1.4.** If \(T\) has enough points, then for a simplicial sheaf \(X\), a simplicial \(\Lambda\)-module \(F\) and \(p\geq0\),
\[
\operatorname{Ext}^p_\Lambda(\Lambda^{(X)},F)\cong\operatorname{Hom}_{D_\bullet(T)}(X,\sigma^pF).
\]
The right side depends only on the simplicial abelian sheaf underlying \(F\).

**Proof.** Apply Proposition 1.3 to \(\sigma^pF\). Since \(\sigma E=\sigma_{\mathbb Z}\otimes_{\mathbb Z}E\) (Conventions of the lesson on triangles and Ext groups), the simplicial sheaf underlying \(\sigma^pF\) is determined by the simplicial abelian sheaf \(F\). \(\square\)

## 2. The Hom complex of a simplicial sheaf

**Lemma 2.1.** Let \(0\to A\to B\to C\to0\) be an exact sequence of complexes of sheaves of \(\Lambda\)-modules that is split in each degree: \(B_n=A_n\oplus C_n\), with differential \(d_B(a,c)=(d_Aa+\tau c,d_Cc)\) for maps \(\tau\colon C_n\to A_{n-1}\).

1. The maps \(\tau\) form a chain map \(C\to A[1]\). If \(B\) is contractible, it is a chain homotopy equivalence.
2. If \(A\) and \(C\) are contractible, so is \(B\), and every contraction of \(A\) extends to a contraction of \(B\).

**Proof.** From \(d_B^2=0\), \(d_A\tau+\tau d_C=0\): \(\tau\) is a chain map to \(A[1]\). Write a map \(h\) of degree \(1\) of \(B\) as a matrix with entries \(\alpha\colon A_n\to A_{n+1}\), \(\beta\colon C_n\to A_{n+1}\), \(\gamma\colon A_n\to C_{n+1}\) and \(\epsilon\colon C_n\to C_{n+1}\). The equation \(d_Bh+hd_B=1\) reads
\[
\begin{aligned}d_A\alpha+\alpha d_A+\tau\gamma&=1,\\ d_C\gamma+\gamma d_A&=0,\\ d_C\epsilon+\epsilon d_C+\gamma\tau&=1,\\ d_A\beta+\beta d_C+\alpha\tau+\tau\epsilon&=0.\end{aligned}
\]
(1) Let \(h\) be a contraction of \(B\). The second equation says that \(\gamma\) is a chain map \(A[1]\to C\). The first says that \(\tau\gamma\) is homotopic to the identity of \(A[1]\), through the homotopy \(-\alpha\), and the third that \(\gamma\tau\) is homotopic to the identity of \(C\), through \(\epsilon\).

(2) Given contractions \(\alpha\) of \(A\) and \(\epsilon\) of \(C\), put \(\gamma=0\) and \(\beta=-\alpha\tau\epsilon\). The first three equations hold. In the fourth, \(d_A\beta=-(1-\alpha d_A)\tau\epsilon\) and \(\alpha d_A\tau\epsilon=-\alpha\tau d_C\epsilon\), so its left side is \(\alpha\tau(1-d_C\epsilon-\epsilon d_C)=0\). The contraction \(h\) restricts to \(\alpha\) on \(A\). \(\square\)

**Lemma 2.2.** Let \(V\) be a simplicial \(\Lambda\)-module. The subcomplex \(DV\) is contractible, and the inclusion \(\iota\colon NV\to CV\) is a chain homotopy equivalence, with homotopy inverse the projection \(\rho\colon CV\to NV\) along \(DV\). The maps \(\iota\) and \(\rho\) are natural in \(V\).

**Proof.** We use Theorem 1.1 of the lesson on the cotangent complex and its proof: \(CV=NV\oplus DV\) as complexes, with \(\rho\) given in each degree by a natural projection \(\pi_n\); \(DV\) is the union of the subcomplexes \(D^{(r)}\), \(r\geq-1\), with \(D^{(r)}_n=\sum_{j\leq r}s_jV_{n-1}\); and \((-1)^rs_r\) induces a contraction of \(D^{(r)}/D^{(r-1)}\). These facts, and the Dold–Kan decomposition below, are given by universal formulas in the faces and degeneracies. So they hold for simplicial sheaves of modules: apply them to the simplicial modules of sections over the objects of \(T\).

By the Dold–Kan theorem (Theorem 1.2 there), \(V_n=\bigoplus_\varphi\varphi^*N_mV\), the sum over the surjections \(\varphi\colon[n]\to[m]\). Moreover \(s_j\psi^*=(\psi\sigma_j)^*\), where \(\sigma_j\colon[n]\to[n-1]\) is the surjection that repeats \(j\). So \(D^{(r)}_n\) is the sum of the summands of the \(\varphi\) with \(\varphi(j)=\varphi(j+1)\) for some \(j\leq r\), and \(D^{(r-1)}\subset D^{(r)}\) is split in each degree. Starting from \(D^{(-1)}=0\), Lemma 2.1 (2) extends a contraction of \(D^{(r-1)}\) to one of \(D^{(r)}\). Since \(D^{(r)}_n=D_nV\) for \(r\geq n-1\), these contractions agree in degree \(n\) for \(r\geq n\), and they define a contraction \(h\) of \(DV\). Then \(\rho\iota=1\), and \(1-\iota\rho=dk+kd\), where \(k\) is \(h\) on \(DV\) and \(0\) on \(NV\). \(\square\)

For a simplicial \(\Lambda\)-module \(E\), the sequence \(N(\mathsf c_E)\colon0\to NE\to N\gamma E\to N\sigma E\to0\) is exact, because normalization is exact (Theorem 1.1 of the lesson on the cotangent complex). It is split in each degree. Indeed, \(\mathsf c_E\) is split in each degree (Section 1.1 of the lesson on triangles and Ext groups). If \(t\) is a section of \(v_E\colon\gamma E_n\to\sigma E_n\), then \(\pi_nt\) restricts to a section of \(N_nv_E\), since \(\pi_n\) is natural and fixes \(N_n\). The module \(\gamma E\) is homotopy equivalent to \(0\), so \(N\gamma E\) is contractible [Stacks, Tag 019S]. By Lemma 2.1 (1), the chain map \(\tau_E\colon N\sigma E\to NE[1]\) of this split sequence is a chain homotopy equivalence. By induction on \(p\), the composite of \(\tau_{\sigma^{p-1}E}\), \(\tau_{\sigma^{p-2}E}[1]\), …, \(\tau_E[p-1]\) is a chain homotopy equivalence
\[
\tau^{(p)}_E\colon N\sigma^pE\to NE[p]\qquad(p\geq0).
\]

**Definition 2.3.** For a simplicial sheaf \(Y\) and a simplicial \(\Lambda\)-module \(M\), \(\operatorname{Hom}^\bullet(Y,M)\) is the Hom complex of abelian groups
\[
\operatorname{Hom}^\bullet_\Lambda\bigl(C\Lambda^{(Y)},CM\bigr)
\]
[Stacks, Tag 0A8H], with the cohomological grading. By Lemma 1.1 (1), its term of degree \(p\) is
\[
\prod\nolimits_q\operatorname{Hom}_T(Y_q,M_{q-p}).
\]
So it is the complex associated with the groups \(\operatorname{Hom}_T(Y_j,M_i)\), cosimplicial in \(j\) and simplicial in \(i\). Its \(p\)-th cohomology group is the group of homotopy classes of chain maps \(C\Lambda^{(Y)}\to CM[p]\) (loc. cit.); the argument there is formal and applies to complexes of sheaves.

**Proposition 2.4.** For a simplicial sheaf \(Y\), a simplicial \(\Lambda\)-module \(M\) and \(p\geq0\), there are isomorphisms of groups, natural in \(Y\),
\[
H^p\operatorname{Hom}^\bullet(Y,M)\cong\operatorname{Hot}(Y,\sigma^pM).
\]

**Proof.** We pass through four groups of homotopy classes. Those of chain maps \(C\Lambda^{(Y)}\to CM[p]\) are those of chain maps \(N\Lambda^{(Y)}\to NM[p]\): compose with the homotopy equivalences \(\iota\) and \(\rho\) of Lemma 2.2, which are natural. Composition with \(\tau^{(p)}_M\) identifies the latter with the homotopy classes of chain maps \(N\Lambda^{(Y)}\to N\sigma^pM\). By Remark 4.3 of the lesson on simplicial rings and modules, normalization identifies these with \(\operatorname{Hot}_\Lambda(\Lambda^{(Y)},\sigma^pM)\), and this is \(\operatorname{Hot}(Y,\sigma^pM)\) by Lemma 1.1 (2). Every step is additive and natural in \(Y\). \(\square\)

**Remark 2.5.** By Lemma 2.2, \(NE\) and \(CE\) are isomorphic in the derived category \(D(\Lambda)\) of \(\Lambda\)-modules, naturally in \(E\). So in Proposition 2.4 of the lesson on triangles and Ext groups the Moore complexes may be replaced by the unnormalized ones:
\[
\begin{aligned}\operatorname{Ext}^p_\Lambda(E,F)&\cong\operatorname{Hom}_{D(\Lambda)}(NE,NF[p])\\&\cong\operatorname{Hom}_{D(\Lambda)}(CE,CF[p]).\end{aligned}
\]

## 3. Hypercoverings

For a Kan simplicial sheaf \(X\), let \(I_X\) be the category whose objects are the fibrant quasi-isomorphisms \(s\colon X'\to X\). A morphism from \(s''\colon X''\to X\) to \(s\) is a homotopy class of maps \(a\colon X''\to X'\) with \(sa\simeq s''\). Each such \(X'\) is Kan, since \(X'\to X\to e\) is a composite of fibrations.

**Lemma 3.1.** Suppose that \(T\) has enough points, and let \(X\) and \(K\) be Kan simplicial sheaves.

1. The category \(I_X^{\mathrm{op}}\) is filtered.
2. The pairs \((s,u)\), with \(s\colon X'\to X\) in \(I_X\) and \(u\in\operatorname{Hot}(X',K)\), define a bijection
\[
\begin{aligned}&\varinjlim_{s\in I_X^{\mathrm{op}}}\operatorname{Hot}(X',K)\\&\quad\to\operatorname{Hom}_{D_\bullet(T)}(X,K),\end{aligned}
\]
\((s,u)\mapsto us^{-1}\). The colimit is taken along the maps \(u\mapsto ua\) induced by the morphisms \(a\) of \(I_X\).

**Proof.** We use Section 4 of the lesson on simplicial groups: the quasi-isomorphisms form a right multiplicative system in \(\operatorname{Hot}_\bullet(T)_{\mathrm{kan}}\) (Theorem 4.1), and \(D_\bullet(T)_{\mathrm{kan}}\to D_\bullet(T)\) is an equivalence (Theorem 4.3).

*Making a quasi-isomorphism fibrant.* Let \(t\colon W\to X\) be a quasi-isomorphism with \(W\) Kan. By Proposition 3.1 of the lesson on simplicial groups, \(t=s''i\) with \(s''\colon X''\to X\) a fibrant quasi-isomorphism and \(i\colon W\to X''\) a homotopy equivalence with homotopy inverse \(q\). Then \(s''\simeq tq\).

(1) The identity of \(X\) is an object. Let \(s\colon X'\to X\) and \(s_1\colon X'_1\to X\) be objects. By the axiom RMS2, there are a quasi-isomorphism \(t\colon W\to X'\) and a map \(g\colon W\to X'_1\) with \(s_1g\simeq st\). Make \(st\) fibrant: \(st=s''i\). Then \(tq\colon s''\to s\) and \(gq\colon s''\to s_1\) are morphisms of \(I_X\). Let \(a,b\colon s''\to s\) be two morphisms. Then \(sa\simeq sb\), and by the axiom RMS3 there is a quasi-isomorphism \(t\colon W\to X''\) with \(at\simeq bt\). Make \(s''t\) fibrant: \(s''t=s'''i\). Then \(tq\colon s'''\to s''\) is a morphism with \(atq\simeq btq\).

(2) A morphism \(a\colon s''\to s\) of \(I_X\) gives \((ua)s''^{-1}=us^{-1}\), since \(s''=sa\) in \(D_\bullet(T)\). So the map is well defined. It is surjective by Corollary 4.2 of the lesson on simplicial groups. Suppose that \(us^{-1}=u_1s_1^{-1}\). By (1) there are morphisms \(a\colon s''\to s\) and \(a_1\colon s''\to s_1\). The elements \(ua\) and \(u_1a_1\) of \(\operatorname{Hot}(X'',K)\) have the same image \(us^{-1}\). By Corollary 4.2 there, \(uar\simeq u_1a_1r\) for some fibrant quasi-isomorphism \(r\colon X'''\to X''\), and \(r\) is a morphism from \(s''r\) to \(s''\). So \((s,u)\) and \((s_1,u_1)\) have the same class in the colimit. \(\square\)

**Theorem 3.2.** Suppose that \(T\) has enough points. Let \(X\) be a Kan simplicial sheaf and \(F\) a simplicial \(\Lambda\)-module. For \(p\geq0\) there is an isomorphism of groups
\[
\begin{aligned}&\operatorname{Ext}^p_\Lambda(\Lambda^{(X)},F)\\&\quad\cong\varinjlim_{s\in I_X^{\mathrm{op}}}H^p\operatorname{Hom}^\bullet(X',F).\end{aligned}
\]

**Proof.** By Corollary 1.4, the left side is \(\operatorname{Hom}_{D_\bullet(T)}(X,\sigma^pF)\) as a set. The simplicial sheaf \(\sigma^pF\) is a simplicial group, hence Kan (Proposition 1.2 of the lesson on simplicial groups). By Lemma 3.1 with \(K=\sigma^pF\) and by Proposition 2.4, the right side is in bijection with it. The bijection is additive. Two elements of the colimit have representatives \((s,u)\) and \((s,u_1)\) with a common \(s\), since \(I_X^{\mathrm{op}}\) is filtered. By Proposition 1.3, they correspond to \(\tilde u\,\Lambda^{(s)}{}^{-1}\) and \(\tilde u_1\Lambda^{(s)}{}^{-1}\). In the additive category \(D_\bullet(\Lambda)\) (Conventions of the lesson on triangles and Ext groups), their sum is \((\tilde u+\tilde u_1)\Lambda^{(s)}{}^{-1}\), and \(\tilde u+\tilde u_1\) extends \(u+u_1\). \(\square\)

For an arbitrary simplicial sheaf \(X\), the map \(e^\infty_X\colon X\to\operatorname{Ex}^\infty X\) is a quasi-isomorphism to a Kan simplicial sheaf (Proposition 4.1 of the lesson on local fibrations). So \(\Lambda^{(e^\infty_X)}\) is a quasi-isomorphism (Proposition 1.2), and Theorem 3.2 applied to \(\operatorname{Ex}^\infty X\) computes \(\operatorname{Ext}^p_\Lambda(\Lambda^{(X)},F)\).

**Definition 3.3.** As in the lesson on cohomology of simplicial topoi, a *hypercovering* of \(T\) (of its final object) is a simplicial sheaf \(X'\) such that \(X'_0\to e\) and the maps \(X'_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nX')_{n+1}\), \(n\geq0\), are epimorphisms. The *Čech cohomology* \(\check H^p(X',F)\) of a \(\Lambda\)-module \(F\) is the cohomology of the cochain complex \(q\mapsto\operatorname{Hom}_T(X'_q,F)\), with the alternating sum of the maps induced by the faces as differential.

**Lemma 3.4.** If \(T\) has enough points, a simplicial sheaf \(X'\) is a hypercovering if and only if \(X'\to e\) is a fibrant quasi-isomorphism.

**Proof.** A section of \((\operatorname{cosk}_n\operatorname{sk}_nX')_{n+1}\) over \(U\in\mathcal C\) is a map between the \(n\)-truncations of \(\Delta[n+1]\times h_U\) and of \(X'\). Since \(\partial\Delta[n+1]\) is the \(n\)-skeleton of \(\Delta[n+1]\), and maps out of an \(n\)-skeleton are determined by their \(n\)-truncations, it is a map \(\partial\Delta[n+1]\times h_U\to X'\). So the target is \(\operatorname{Hom}(\partial\Delta[n+1],X')\) (Lemma 1.1 (3) of the lesson on the simplicial derived category). Let \(p\colon X'\to e\) and \(i_m\colon\partial\Delta[m]\subset\Delta[m]\). The map \(q_{i_m}(p)\) of Lemma 2.2 of the lesson on local fibrations is \(X'_m\to\operatorname{Hom}(\partial\Delta[m],X')\), and for \(m=0\) it is \(X'_0\to e\). By that lemma, \(X'\) is a hypercovering exactly when \(p\) has the local lifting property relative to all boundary inclusions.

If \(p\) is a fibrant quasi-isomorphism, it has this property by Proposition 4.3 of the lesson on local fibrations. Conversely, suppose it has the property. A horn \(\Lambda^k[n]\subset\Delta[n]\) is the composite of two pushouts of boundary inclusions: first attach the missing face along its boundary, which gives \(\partial\Delta[n]\), then the simplex along its boundary. By Lemma 2.3 of the lesson on local fibrations, \(p\) is a fibration. Let \(x\) be a point of a conservative family. Stalks commute with \(\operatorname{Hom}(K,-)\) for finite \(K\) (Lemma 1.1 (2) of the lesson on the simplicial derived category), so \(q_{i_m}(p)_x=q_{i_m}(p_x)\) is surjective for every \(m\). So the stalk \(p_x\colon X'_x\to\Delta[0]\) is a trivial fibration, hence a quasi-isomorphism (Theorem 3.7 of the lesson on local fibrations). By Corollary 3.3 (3) of the lesson on the simplicial derived category, \(p\) is a quasi-isomorphism. \(\square\)

By Lemma 3.4 and Proposition 1.2, \(\Lambda^{(X')}\to\Lambda^{(e)}=\Lambda\) is a quasi-isomorphism for every hypercovering \(X'\) of a topos with enough points. The lesson on cohomology of simplicial topoi uses this acyclicity, for \(\Lambda=\mathbb Z\) and every topos, in its proof of cohomological descent, where it is taken from the AI-integrated Stacks project.

**Corollary 3.5 (Verdier).** Suppose that \(T\) has enough points, and let \(F\) be a \(\Lambda\)-module. For \(p\geq0\),
\[
H^p(T,F)\cong\varinjlim_{X'}\check H^p(X',F),
\]
the colimit over the category of hypercoverings \(X'\) of \(T\) and homotopy classes of maps, taken along the maps induced by these.

**Proof.** Apply Theorem 3.2 to \(X=e\), which is Kan, and to the constant simplicial module \(F\). Here \(\Lambda^{(e)}=\Lambda\). The objects of \(I_e\) are the hypercoverings (Lemma 3.4), and every map commutes with the maps to \(e\). By Lemma 2.2, the complex \(CF\) is homotopy equivalent to \(NF\), which is \(F\) in degree \(0\). So \(\operatorname{Hom}^\bullet(X',F)\) is homotopy equivalent to \(\operatorname{Hom}^\bullet_\Lambda(C\Lambda^{(X')},F)\), naturally in \(X'\). This is the Čech complex of \(X'\), except that its differential from degree \(q\) has the sign \((-1)^{q+1}\); the cohomology is the same. On the other side, \(\operatorname{Ext}^p_\Lambda(\Lambda,F)\cong\operatorname{Hom}_{D(\Lambda)}(\Lambda,F[p])\) by Proposition 2.4 of the lesson on triangles and Ext groups. For an injective resolution \(F\to I\), this is the group of homotopy classes of maps \(\Lambda\to I[p]\) [Stacks, Tag 06XR], that is, \(H^p\operatorname{Hom}_\Lambda(\Lambda,I)\), which is \(H^p\Gamma(T,I)=H^p(T,F)\). \(\square\)

In the AI-integrated Stacks project, hypercoverings of an object of a site with fibre products are built, in each degree, from families of objects of the site [[Stacks, Tag 01G5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-definition-hypercovering)], and the theorem is proved for them [[Tag 01H0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-theorem-cohomology-hypercoverings)]. Definition 3.3 allows arbitrary simplicial sheaves.

**Remark 3.6.** For the topos of sets, the homotopy category of Kan complexes is equivalent to the simplicial derived category (Corollary 4.4 of the lesson on simplicial groups). For a topos with enough points, the functor \(\operatorname{Hot}_\bullet(T)_{\mathrm{kan}}\to D_\bullet(T)\) need not be full. Let \(T\) be the classifying topos of the group \(\mathbb Z\). Its objects are the sets with an action of \(\mathbb Z\), its abelian sheaves are the modules over \(\Lambda_0=\mathbb Z[t,t^{-1}]\), and the underlying set is a conservative point. Take \(\Lambda=\mathbb Z\) with the trivial action, and the Kan objects \(e\) and \(\sigma\mathbb Z\).

On one side, \(\operatorname{Hot}(e,\sigma\mathbb Z)=H^1\operatorname{Hom}^\bullet(e,\mathbb Z)\) by Proposition 2.4. As in the proof of Corollary 3.5, \(\operatorname{Hom}^\bullet(e,\mathbb Z)\) is homotopy equivalent to \(\operatorname{Hom}^\bullet_\Lambda(C\Lambda,\mathbb Z)\). This complex has \(\operatorname{Hom}_T(e,\mathbb Z)=\mathbb Z\) in every degree \(q\geq0\). Its differential from degree \(q\) is multiplication by \((-1)^{q+1}\sum_{i=0}^{q+1}(-1)^i\), which is \(0\) for \(q\) even and \(1\) for \(q\) odd. So \(H^1\operatorname{Hom}^\bullet(e,\mathbb Z)=0\).

On the other side, the group \(\operatorname{Hom}_{D_\bullet(T)}(e,\sigma\mathbb Z)\) is \(\operatorname{Ext}^1_\Lambda(\Lambda,\mathbb Z)=H^1(T,\mathbb Z)\), by Corollary 1.4 and the proof of Corollary 3.5. Here \(\Gamma(T,-)=\operatorname{Hom}_{\Lambda_0}(\mathbb Z,-)\). The free resolution \(0\to\Lambda_0\xrightarrow{t-1}\Lambda_0\to\mathbb Z\to0\) gives \(H^1(T,\mathbb Z)=\operatorname{coker}(\mathbb Z\xrightarrow{0}\mathbb Z)=\mathbb Z\). So the map from homotopy classes to morphisms of \(D_\bullet(T)\) is not surjective between these two Kan objects.

## 4. Exercises

**Exercise 4.1** (easy). Let \(Y\) be a simplicial sheaf and \(F\) a \(\Lambda\)-module. Show that \(H^0\operatorname{Hom}^\bullet(Y,F)=\operatorname{Hom}_T(\pi_0(Y),F)\), where \(\pi_0(Y)\) is the coequalizer of \(d_0,d_1\colon Y_1\rightrightarrows Y_0\).

**Exercise 4.2** (medium). Let \(T\) be the topos of sets. Show that \(\operatorname{Ext}^p_\Lambda(\Lambda^{(X)},F)\cong H^p\operatorname{Hom}^\bullet(X,F)\) for a Kan complex \(X\) and a simplicial \(\Lambda\)-module \(F\). Deduce that \(\operatorname{Ext}^p_\Lambda(\Lambda,F)=0\) for a constant module \(F\) and \(p>0\).

**Exercise 4.3** (hard). Let \(G\) be a group and \(T\) its classifying topos, of sets with an action of \(G\). Let \(EG\) be the Čech nerve of the \(G\)-set \(G\), with left translations: \((EG)_n=G^{n+1}\) with the diagonal action, faces omitting and degeneracies repeating an entry. Show that \(EG\) is a hypercovering, and that every hypercovering receives a map from \(EG\), unique up to homotopy. Deduce that \(H^p(T,F)\) is the cohomology of the complex of maps \(G^{q+1}\to F\) commuting with the action of \(G\), for every \(G\)-module \(F\).

**Exercise 4.4** (medium). In the situation of Remark 3.6, let \(X'\) be the Čech nerve of the \(\mathbb Z\)-set \(\mathbb Z\), with the translation action. Show that there is no map \(e\to X'\). Show that \(\check H^1(X',\mathbb Z)\cong\mathbb Z\), generated by the class of \(\phi(a_0,a_1)=a_1-a_0\), and that this class maps to a generator of \(H^1(T,\mathbb Z)\).

## 5. Complete solutions

**Solution 4.1.** As in the proof of Corollary 3.5, \(\operatorname{Hom}^\bullet(Y,F)\) is homotopy equivalent to the complex \(q\mapsto\operatorname{Hom}_T(Y_q,F)\), whose differential from degree \(q\) is \((-1)^{q+1}\) times the alternating sum of the maps induced by the faces. In degree \(0\), the differential is \(f\mapsto-(fd_0-fd_1)\). Its kernel consists of the maps \(f\colon Y_0\to F\) with \(fd_0=fd_1\), that is, of the maps from the coequalizer \(\pi_0(Y)\) to \(F\).

**Solution 4.2.** By Theorem 3.2, the left side is the colimit of the groups \(H^p\operatorname{Hom}^\bullet(X',F)\) over \(I_X^{\mathrm{op}}\). Let \(s\colon X'\to X\) be an object of \(I_X\). By Theorem 3.7 of the lesson on local fibrations, \(s\) is a trivial fibration. As in the proof of that theorem, it has a section \(u\), with \(su=1\), and an elementary homotopy from \(us\) to \(1\). So \(u\colon1_X\to s\) and \(s\colon s\to1_X\) are inverse isomorphisms of \(I_X\). The endomorphisms of \(1_X\) are the homotopy classes of maps \(a\colon X\to X\) with \(a\simeq1\); there is only one. So every object of \(I_X\) is isomorphic to \(1_X\), every set of morphisms has one element, and the colimit is \(H^p\operatorname{Hom}^\bullet(X,F)\). For \(X=\Delta[0]\), \(\Lambda^{(X)}=\Lambda\), and \(C\Lambda\) and \(CF\) are homotopy equivalent to \(\Lambda\) and \(F\) in degree \(0\) (Lemma 2.2). So \(\operatorname{Hom}^\bullet(\Delta[0],F)\) is homotopy equivalent to \(\operatorname{Hom}_\Lambda(\Lambda,F)=F\) in degree \(0\), and its cohomology vanishes in positive degrees. This agrees with Example 2.5 of the lesson on triangles and Ext groups.

**Solution 4.3.** The map \(G\to e\) is an epimorphism of \(G\)-sets, since \(G\) is nonempty. So \(EG\) is a hypercovering, by Exercise 6.1 of the lesson on cohomology of simplicial topoi.

The action of \(G\) on \(G^{n+1}\) is free, so the \(G\)-set of nondegenerate \(n\)-simplices of \(EG\) is free. Choose a set of representatives of its orbits. Let \(X'\) be a hypercovering. By the first paragraph of the proof of Lemma 3.4, the maps \(X'_n\to\operatorname{Hom}(\partial\Delta[n],X')\) are epimorphisms of \(G\)-sets, that is, surjective, and so is \(X'_0\to e\). Construct \(g\colon EG\to X'\) skeleton by skeleton, attaching the nondegenerate simplices as in the expression (1.8) of the lesson on Kan complexes. Suppose that \(g\) is defined and equivariant on the \((n-1)\)-skeleton. For each representative \(\xi\), the restriction of \(g\) to the boundary of \(\xi\) is an element of \(\operatorname{Hom}(\partial\Delta[n],X')\). Choose a preimage \(g(\xi)\in X'_n\), and put \(g(h\xi)=hg(\xi)\) for \(h\in G\); this is well defined because the action is free. The values on degenerate simplices are forced by the degeneracies. This extends \(g\), equivariantly, to the \(n\)-skeleton.

Let \(g,g'\colon EG\to X'\) be two maps. The \(G\)-set of nondegenerate simplices of \(\Delta[1]\times EG\) that do not lie in \(\partial\Delta[1]\times EG\) is again free, since \(G\) acts freely on the second factor. The same construction, relative to \(\partial\Delta[1]\times EG\), on which the map is given by \(g\) and \(g'\), gives an elementary homotopy from \(g\) to \(g'\).

So \(EG\) is an initial object of the category of hypercoverings and homotopy classes of maps, and a terminal object of the opposite category, over which the colimit of Corollary 3.5 is taken. The colimit of a functor on a category with a terminal object is its value there. So \(H^p(T,F)=\check H^p(EG,F)\), the cohomology of the complex \(q\mapsto\operatorname{Hom}_T(G^{q+1},F)\) of equivariant maps.

**Solution 4.4.** A map \(e\to X'\) is determined by a point of \(X'_0=\mathbb Z\) fixed by the translations, and there is none.

A \(1\)-cochain is a function \(\psi\colon\mathbb Z^2\to\mathbb Z\) invariant under simultaneous translation, that is, \(\psi(a_0,a_1)=f(a_1-a_0)\) for a function \(f\colon\mathbb Z\to\mathbb Z\). The coboundary of \(\psi\) is
\[
\begin{aligned}&\delta\psi(a_0,a_1,a_2)\\&\quad=\psi(a_1,a_2)-\psi(a_0,a_2)+\psi(a_0,a_1).\end{aligned}
\]
With \(x=a_1-a_0\) and \(y=a_2-a_1\), the cocycle condition says \(f(x+y)=f(x)+f(y)\) for all \(x,y\), that is, \(f(x)=cx\) with \(c=f(1)\). The \(0\)-cochains are the invariant functions on \(\mathbb Z\), the constants, and their coboundaries are \(0\). So \(\check H^1(X',\mathbb Z)\cong\mathbb Z\), generated by the class of \(\phi\), with \(c=1\). The nerve \(X'\) is \(E\mathbb Z\). By Solution 4.3, \(\check H^1(E\mathbb Z,\mathbb Z)\to H^1(T,\mathbb Z)\) is an isomorphism, so the class of \(\phi\) maps to a generator.

## Sources

The derived adjunction between free simplicial modules and the forgetful functor, the complex \(\operatorname{Hom}^\bullet(Y,M)\), Proposition 2.4, Theorem 3.2 and its relation with Verdier's theorem are due to Illusie, in his work on the cotangent complex. So is the observation that the homotopy category of Kan simplicial sheaves is not in general equivalent to the simplicial derived category. Hypercoverings and the theorem computing cohomology as a colimit of Čech cohomology over them are due to Verdier; the AI-integrated Stacks project proves the theorem for sites [[Stacks, Tag 01H0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-theorem-cohomology-hypercoverings)]. The contractibility of the degenerate subcomplex is classical; Lemma 2.2 extends contractions along the filtration of the lesson on the cotangent complex.
