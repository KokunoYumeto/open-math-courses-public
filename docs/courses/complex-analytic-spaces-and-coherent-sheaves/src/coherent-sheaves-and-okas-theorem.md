# Coherent sheaves and Oka's coherence theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The stalks of the sheaf of holomorphic functions are Noetherian rings, so relations among finitely many germs at one point are finitely generated. Oka's theorem says much more: finitely many relations can be chosen so that they generate the relations at every point of a neighbourhood. In the language of sheaves, the sheaf of holomorphic functions is coherent. This lesson proves Oka's theorem and draws the consequences that make coherent analytic sheaves a workable category: kernels, cokernels, images, extensions, tensor products and internal homomorphisms of coherent sheaves are coherent, coherent sheaves have analytic supports, and a coherent sheaf with a free stalk is free near that point.

We use [The local ring of holomorphic germs](the-local-ring-of-holomorphic-germs.md), in particular the Weierstrass division theorem in the form of its Theorem 2.1 and Lemmas 2.3 and 3.2. Sheaves of modules on a ringed space and their stalks are as in [Cohomology of sheaves on ringed spaces](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces); the general algebra of coherent modules on a ringed space is taken from the AI Integrated Stacks Project, with exact tags.

Basic references are [Demailly], [Oka 1950] and [Cartan 1950].

## 1. Coherent modules on a ringed space

Let \(\mathcal A\) be a sheaf of rings on a topological space \(X\) and \(\mathcal S\) a sheaf of \(\mathcal A\)-modules. Sections \(s_1,\ldots,s_q\in\mathcal S(U)\) define a morphism

\[
\sigma:\mathcal A^q|_U\to\mathcal S|_U,\qquad (g_1,\ldots,g_q)\mapsto\sum_j g_js_j ,
\tag{1.1}
\]

and its kernel \(\mathcal R(s_1,\ldots,s_q)\subset\mathcal A^q|_U\) is the **sheaf of relations** among the \(s_j\). The module \(\mathcal S\) is **of finite type** (locally finitely generated) if every point has a neighbourhood \(U\) and sections \(s_1,\ldots,s_q\in\mathcal S(U)\) for which \(\sigma\) is surjective, that is, whose germs generate every stalk \(\mathcal S_x\), \(x\in U\).

**Definition 1.1.** \(\mathcal S\) is **coherent** if it is of finite type and, for every open \(U\) and all finitely many \(s_1,\ldots,s_q\in\mathcal S(U)\), the sheaf of relations \(\mathcal R(s_1,\ldots,s_q)\) is of finite type. The sheaf of rings \(\mathcal A\) is **coherent** if it is coherent as a module over itself.

This is the definition of [Stacks, Tag 01BV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-definition-coherent). We use the following general facts, valid on any ringed space.

**Proposition 1.2.** Let \((X,\mathcal A)\) be a ringed space.

1. A finite type submodule of a coherent module is coherent. If \(\varphi:\mathcal F\to\mathcal G\) is a morphism of coherent modules, then \(\ker\varphi\), \(\operatorname{im}\varphi\) and \(\operatorname{coker}\varphi\) are coherent. If two of the three modules in a short exact sequence are coherent, so is the third. [Stacks, Tag 01BY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-abelian).
2. If \(\mathcal A\) is coherent, a module is coherent if and only if it is of finite presentation, that is, locally the cokernel of a morphism \(\mathcal A^p\to\mathcal A^q\). [Stacks, Tag 01BZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-structure-sheaf).
3. If \(\mathcal G\) is of finite type, \(\mathcal F\) is coherent, and \(\varphi:\mathcal G\to\mathcal F\) is injective on the stalk at \(x\), then \(\varphi\) is injective on a neighbourhood of \(x\). [Stacks, Tag 01C0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-finite-type-to-coherent-injective-on-stalk).

By part 1 applied to the split exact sequences \(0\to\mathcal A^{q-1}\to\mathcal A^q\to\mathcal A\to0\), if \(\mathcal A\) is coherent then so is every free module \(\mathcal A^q\). Consequently the relations among finitely many sections of \(\mathcal A^q\) form a coherent submodule of a free module.

**Lemma 1.3.** Let \(\mathcal S\) be of finite type and \(x\in X\).

1. If \(t_1,\ldots,t_N\in\mathcal S(U)\) have germs generating \(\mathcal S_x\), their germs generate \(\mathcal S_y\) for all \(y\) in a neighbourhood of \(x\).
2. If \(\mathcal S_x=0\), then \(\mathcal S\) vanishes on a neighbourhood of \(x\). Hence the support \(\operatorname{Supp}\mathcal S=\{y:\ \mathcal S_y\neq0\}\) is closed.

**Proof.** (1) Choose generators \(s_1,\ldots,s_q\) of \(\mathcal S\) near \(x\). Each \(s_i\) is, at \(x\), a combination of the \(t_k\) with coefficients in \(\mathcal A_x\); these coefficients and the identity they satisfy extend to a neighbourhood, on which every \(s_i\), and hence every stalk, lies in the span of the \(t_k\). (2) Apply (1) to the empty family. \(\square\)

## 2. Oka's coherence theorem

An **analytic sheaf** on a complex manifold \(M\) is a sheaf of \(\mathcal O_M\)-modules. A coherent analytic sheaf on an open subset of \(\mathbf C^n\) is called coherent for short.

**Theorem 2.1 (Oka).** For every complex manifold \(M\) the sheaf of rings \(\mathcal O_M\) is coherent.

The stalks \(\mathcal O_{M,x}\cong\mathcal O_n\) are Noetherian, so each stalk of a sheaf of relations is finitely generated. The content of the theorem is that one finite family of relations generates the stalks of the relation sheaf at all points of a neighbourhood. The proof is by induction on \(n=\dim M\), and the following lemma reduces relations among Weierstrass polynomials to relations among polynomials of bounded degree, which are governed by one fewer variable.

Let \(\Delta=\Delta'\times\Delta_n\) be a polydisc in \(\mathbf C^{n-1}\times\mathbf C\), and let \(P_1,\ldots,P_q\in\mathcal O(\Delta')[z_n]\) be monic polynomials in \(z_n\), of degrees at most \(\mu\). For \(x=(x',x_n)\in\Delta\) we call an element of \(\mathcal R(P_1,\ldots,P_q)_x\) **polynomial of degree at most \(\mu\)** if all its components lie in \(\mathcal O_{\mathbf C^{n-1},x'}[z_n]\) and have degree at most \(\mu\) in \(z_n\).

**Lemma 2.2.** For every \(x\in\Delta\), the \(\mathcal O_{\mathbf C^n,x}\)-module \(\mathcal R(P_1,\ldots,P_q)_x\) is generated by its elements that are polynomial of degree at most \(\mu\).

**Proof.** We may suppose that \(P_q\) has the maximal degree \(\mu\). The elements

\[
\rho_j=P_q\,e_j-P_j\,e_q\qquad(1\leq j<q),
\tag{2.1}
\]

where \(e_1,\ldots,e_q\) is the standard basis, are relations that are polynomial of degree at most \(\mu\). Split \(P_q=f'f''\) at \(x\) as in [The local ring of holomorphic germs, Lemma 3.2](the-local-ring-of-holomorphic-germs.md#3-unique-factorization): \(f'\) is a Weierstrass polynomial of some degree \(\mu'\) in \(z_n-x_n\), and \(f''\) is monic of degree \(\mu-\mu'\) with \(f''(x)\neq0\), so \(f''\) is a unit at \(x\).

Let \(g=(g_1,\ldots,g_q)\in\mathcal R(P_1,\ldots,P_q)_x\). For \(j<q\), divide \(g_j\) by \(f'\) at \(x\) (Theorem 2.1 of the same lesson): \(g_j=s_jf'+r_j\) with \(r_j\in\mathcal O_{\mathbf C^{n-1},x'}[z_n]\) of degree less than \(\mu'\). Put \(t_j=s_j/f''\), so that \(g_j=t_jP_q+r_j\), and put \(r_q=g_q+\sum_{j<q}t_jP_j\). Then

\[
g=\sum_{j<q}t_j\rho_j+(r_1,\ldots,r_q),
\tag{2.2}
\]

as one checks componentwise, so \(r=(r_1,\ldots,r_q)\) is a relation: \(\sum_{j<q}r_jP_j+r_qf'f''=0\). The polynomial \(S=-\sum_{j<q}r_jP_j\) has degree less than \(\mu'+\mu\) and is divisible by the Weierstrass polynomial \(f'\) in \(\mathcal O_{\mathbf C^n,x}\), with quotient \(f''r_q\). By Lemma 2.3 of the same lesson, \(S=f'T\) with a polynomial \(T\), and uniqueness of division gives \(f''r_q=T\), a polynomial of degree less than \(\mu\). Hence

\[
r=\frac1{f''}\bigl(f''r_1,\ldots,f''r_{q-1},\,T\bigr),
\]

where \(f''r_j\) has degree less than \((\mu-\mu')+\mu'=\mu\). So \(r\) is a unit multiple of a relation that is polynomial of degree less than \(\mu\), and by (2.2) \(g\) lies in the submodule generated by such relations and the \(\rho_j\). \(\square\)

**Proof of Theorem 2.1.** The statement is local, so let \(M\) be an open subset of \(\mathbf C^n\); we argue by induction on \(n\). For \(n=0\) the stalks are \(\mathbf C\) and there is nothing to prove. Let \(n\geq1\), let \(F_1,\ldots,F_q\in\mathcal O(U)\) and \(a\in U\); we show that \(\mathcal R(F_1,\ldots,F_q)\) is generated near \(a\) by finitely many sections. Take \(a=0\).

*Reductions.* If some \(F_j\) vanishes identically near \(0\), then near \(0\) the relation sheaf is the direct sum of \(\mathcal O\,e_j\) and the relation sheaf of the remaining functions; so we may assume that no germ \(F_{j,0}\) is zero. If some \(F_j(0)\neq0\), say \(F_q(0)\neq0\), then near \(0\) the relations are generated by \(F_qe_j-F_je_q\), \(j<q\): a relation \(g\) equals \(\sum_{j<q}(g_j/F_q)(F_qe_j-F_je_q)\). So we may assume that all \(F_j\) vanish at \(0\). After one linear change of coordinates all \(F_j\) are regular in \(z_n\) (apply Lemma 4.1 of [Holomorphic functions of several variables](holomorphic-functions-of-several-variables.md#4-the-riemann-extension-theorem) to the product \(F_1\cdots F_q\)), and \(F_j=u_jP_j\) with units \(u_j\) and Weierstrass polynomials \(P_j\). On a polydisc \(\Delta=\Delta'\times\Delta_n\) about \(0\) on which the \(u_j\) have no zeros and the coefficients of the \(P_j\) are holomorphic, the isomorphism \((g_j)\mapsto(g_ju_j)\) of \(\mathcal O^q\) carries \(\mathcal R(F_1,\ldots,F_q)\) onto \(\mathcal R(P_1,\ldots,P_q)\). So we may assume \(F_j=P_j\).

*Polynomial relations.* A polynomial element \(g\) of degree at most \(\mu\) at \(x\in\Delta\) has components \(g_j=\sum_{k=0}^\mu u_{jk}z_n^k\) with \(u_{jk}\in\mathcal O_{\mathbf C^{n-1},x'}\). Write \(P_j=\sum_{l=0}^{\mu}p_{jl}z_n^l\) with \(p_{jl}\in\mathcal O(\Delta')\). The expression \(\sum_jg_jP_j\) is a polynomial in \(z_n\) of degree at most \(2\mu\) with coefficients in \(\mathcal O_{\mathbf C^{n-1},x'}\), and it is zero as a germ at \(x\) if and only if all its coefficients are zero: for fixed \(z'\) near \(x'\), a polynomial in \(z_n\) that vanishes for all \(z_n\) near \(x_n\) has zero coefficients. So \(g\) is a relation exactly when

\[
\sum_{j=1}^q\ \sum_{k+l=m}p_{jl}\,u_{jk}=0\qquad(m=0,1,\ldots,2\mu).
\tag{2.3}
\]

This says that the vector \(u=(u_{jk})\in\mathcal O_{x'}^{q(\mu+1)}\) is a relation among the \(q(\mu+1)\) sections \(c_{jk}=(p_{j,m-k})_{0\leq m\leq2\mu}\) of the free module \(\mathcal O_{\Delta'}^{2\mu+1}\) (with \(p_{j,l}=0\) for \(l<0\) or \(l>\mu\)). By the induction hypothesis \(\mathcal O_{\Delta'}\) is coherent, hence so is \(\mathcal O_{\Delta'}^{2\mu+1}\) (Section 1), and the relation sheaf \(\mathcal R(c_{jk})\) is generated on a neighbourhood \(\Omega'\) of \(0\) by finitely many sections \(U_1,\ldots,U_N\in\mathcal O(\Omega')^{q(\mu+1)}\).

*Conclusion.* Put \(G_\nu=\bigl(\sum_kU_\nu^{jk}(z')z_n^k\bigr)_{1\leq j\leq q}\), a section of \(\mathcal R(P_1,\ldots,P_q)\) over \(\Omega=\Omega'\times\Delta_n\). At every \(x\in\Omega\), the germs \(U_{\nu,x'}\) generate the module of solutions of (2.3), so the germs \(G_{\nu,x}\) generate the polynomial relations of degree at most \(\mu\) at \(x\). By Lemma 2.2 these generate \(\mathcal R(P_1,\ldots,P_q)_x\). Thus \(G_1,\ldots,G_N\) generate the relation sheaf on \(\Omega\). \(\square\)

*Reference:* [Oka 1950] proves this theorem; the proof above follows the arrangement in [Demailly], which credits it.

## 3. The category of coherent analytic sheaves

From now on, \(M\) is a complex manifold and "coherent" means coherent over \(\mathcal O_M\). By Theorem 2.1 and Proposition 1.2(2), an analytic sheaf is coherent if and only if it has local **finite presentations**

\[
\mathcal O^p|_U\xrightarrow{\ A\ }\mathcal O^q|_U\longrightarrow\mathcal S|_U\longrightarrow0,
\tag{3.1}
\]

where \(A\) is a \(q\times p\) matrix of holomorphic functions on \(U\).

**Theorem 3.1.** Let \(M\) be a complex manifold.

1. Kernels, images and cokernels of morphisms of coherent sheaves are coherent; extensions of coherent sheaves are coherent; finitely generated subsheaves of coherent sheaves are coherent. The intersection and the sum of two coherent subsheaves of a coherent sheaf are coherent.
2. If \(\mathcal F\) and \(\mathcal G\) are coherent, so are \(\mathcal F\otimes_{\mathcal O}\mathcal G\) and \(\mathcal Hom_{\mathcal O}(\mathcal F,\mathcal G)\), and the stalk of the latter at \(x\) is \(\operatorname{Hom}_{\mathcal O_x}(\mathcal F_x,\mathcal G_x)\).
3. The annihilator ideal of a coherent sheaf is coherent, and the support of a coherent sheaf is an analytic subset of \(M\).
4. Every coherent sheaf has, near each point and for every \(m\), an exact sequence \(\mathcal O^{p_m}\to\cdots\to\mathcal O^{p_1}\to\mathcal O^{p_0}\to\mathcal S\to0\).

**Proof.** (1) The first three statements are Proposition 1.2(1). The intersection of \(\mathcal F,\mathcal G\subset\mathcal S\) is the kernel of \(\mathcal F\to\mathcal S/\mathcal G\), and the sum is the image of \(\mathcal F\oplus\mathcal G\to\mathcal S\).

(2) Tensor products: from presentations (3.1) of \(\mathcal F\) and \(\mathcal G\), right exactness of \(\otimes\) presents \(\mathcal F\otimes\mathcal G\) as a cokernel of a morphism of free modules of finite rank. Homomorphisms: from \(\mathcal O^p\to\mathcal O^q\to\mathcal F\to0\) on \(U\), left exactness of \(\mathcal Hom(-,\mathcal G)\) gives an exact sequence \(0\to\mathcal Hom(\mathcal F,\mathcal G)\to\mathcal G^q\to\mathcal G^p\), so \(\mathcal Hom(\mathcal F,\mathcal G)\) is a kernel of a morphism of coherent sheaves. Applying the same reasoning to stalks, where \(\operatorname{Hom}_{\mathcal O_x}(-,\mathcal G_x)\) is also left exact, identifies the stalks.

(3) The annihilator of \(\mathcal S\) is the kernel of \(\mathcal O\to\mathcal Hom(\mathcal S,\mathcal S)\), \(f\mapsto f\cdot\mathrm{id}\), hence coherent by (1) and (2); this is also [Stacks, Tag 0H2L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-annihilator). For the support, use a presentation (3.1) near \(x\). The stalk \(\mathcal S_y\) is zero exactly when \(A_y:\mathcal O_y^p\to\mathcal O_y^q\) is surjective, which by Nakayama's lemma happens exactly when the constant matrix \(A(y)\) has rank \(q\). So \(\operatorname{Supp}\mathcal S\cap U\) is the common zero set of the \(q\times q\) minors of \(A\), an analytic subset.

(4) Inductively, the kernel of a surjection \(\mathcal O^{p_k}\to\mathcal Z_{k-1}\) onto a coherent sheaf is coherent, hence finitely generated on a smaller neighbourhood. \(\square\)

A **locally free sheaf** of rank \(r\) is a sheaf locally isomorphic to \(\mathcal O^r\); locally free sheaves are coherent. The locally free sheaves are the sheaves of holomorphic sections of holomorphic vector bundles: transition matrices of local frames are holomorphic maps into \(\mathrm{GL}_r(\mathbf C)\) satisfying the cocycle condition, and conversely such a cocycle glues trivial bundles.

**Proposition 3.2.** If \(\mathcal S\) is coherent and \(\mathcal S_x\) is a free \(\mathcal O_x\)-module of rank \(r\), then \(\mathcal S\) is free of rank \(r\) on a neighbourhood of \(x\).

**Proof.** Choose sections \(s_1,\ldots,s_r\) near \(x\) whose germs form a basis of \(\mathcal S_x\). The morphism \(\sigma:\mathcal O^r\to\mathcal S\) of (1.1) is surjective near \(x\) by Lemma 1.3(1) and injective near \(x\) by Proposition 1.2(3), because \(\sigma_x\) is an isomorphism. \(\square\)

**Corollary 3.3.** Let \(\mathcal S\) be coherent and \(x\in M\). If a finite free resolution \(0\to\mathcal O_x^{p_m}\to\cdots\to\mathcal O_x^{p_0}\to\mathcal S_x\to0\) of the stalk exists, then \(\mathcal S\) has a finite free resolution of the same length on a neighbourhood of \(x\).

**Proof.** Build the sequence of Theorem 3.1(4) near \(x\) up to the stage \(m-1\), choosing at each stage generators whose germs at \(x\) give the given resolution of \(\mathcal S_x\); this is possible because a surjection onto a stalk lifts to a morphism near \(x\) that is surjective near \(x\) by Lemma 1.3. The kernel \(\mathcal Z_{m-1}\) of the last map is coherent, and its stalk at \(x\) is the kernel at the corresponding stage of the given resolution, which is the free module \(\mathcal O_x^{p_m}\). By Proposition 3.2, \(\mathcal Z_{m-1}\) is free near \(x\). \(\square\)

Every finitely generated \(\mathcal O_n\)-module has a free resolution of length at most \(n\), because \(\mathcal O_n\) is a regular local ring of dimension \(n\) ([The local ring of holomorphic germs, Proposition 1.1](the-local-ring-of-holomorphic-germs.md#1-the-ring-of-germs)) and regular local rings have finite global dimension equal to their dimension [Stacks, Tag 00O7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-regular-finite-gl-dim); over a local ring a finitely generated projective module is free. By Corollary 3.3 we obtain:

**Theorem 3.4 (local syzygies).** Every coherent analytic sheaf on an \(n\)-dimensional complex manifold has, near each point, a resolution \(0\to\mathcal O^{p_n}\to\cdots\to\mathcal O^{p_0}\to\mathcal S\to0\) by free sheaves of finite rank, of length at most \(n\).

## 4. Exercises

**Exercise 4.1.** Let \(F_1=z_1\), \(F_2=z_2\) on \(\mathbf C^2\). Show that \(\mathcal R(F_1,F_2)\) is the free sheaf generated by \((z_2,-z_1)\).

*Solution.* If \(g_1z_1+g_2z_2=0\) near a point, then at points with \(z_1\neq0\) we get \(g_1=-g_2z_2/z_1\). At \(0\), \(z_1\) divides \(g_2z_2\), and since \(z_1,z_2\) are coprime in the factorial ring \(\mathcal O_2\), \(z_1\) divides \(g_2\): \(g_2=-hz_1\), and then \(g_1=hz_2\). So every relation is \(h\,(z_2,-z_1)\), and \(h\) is unique because \(\mathcal O\) has no zero divisors. At other points the same holds since one of \(z_1,z_2\) is a unit there.

**Exercise 4.2.** On \(\mathbf C\), let \(\mathcal S=\mathcal O/(z)\), the skyscraper sheaf with stalk \(\mathbf C\) at \(0\). Show that \(\mathcal S\) is coherent but not locally free, and identify its support and its annihilator.

*Solution.* The presentation \(\mathcal O\xrightarrow{z}\mathcal O\to\mathcal S\to0\) shows coherence. The stalk at \(0\) is \(\mathbf C\), which is not free over \(\mathcal O_1\), while the stalks elsewhere are \(0\); so \(\mathcal S\) is not locally free. Its support is \(\{0\}\), the zero set of the \(1\times1\) minor \(z\), and its annihilator is the ideal sheaf \((z)\).

**Exercise 4.3.** Let \(H=\{z\in\mathbf C:\ \operatorname{Re}z\geq0\}\) and let \(\mathcal J\subset\mathcal O_{\mathbf C}\) be the subsheaf of germs vanishing on \(H\). Show that \(\mathcal J\) is not of finite type, although every stalk of \(\mathcal J\) is a finitely generated ideal.

*Solution.* If \(\operatorname{Re}x<0\), a small disc about \(x\) misses \(H\), so \(\mathcal J_x=\mathcal O_x\). If \(\operatorname{Re}x\geq0\), every neighbourhood of \(x\) meets \(H\) in a set with interior points, so a germ at \(x\) vanishing on \(H\) is zero by the identity theorem, and \(\mathcal J_x=0\). Both kinds of stalks are finitely generated. The support of \(\mathcal J\) is the open half-plane \(\{\operatorname{Re}z<0\}\), which is not closed; by Lemma 1.3 a sheaf of finite type has closed support. So \(\mathcal J\) is not of finite type. The set \(H\) is not an analytic subset, and Lesson 5 shows that for analytic subsets the corresponding ideal sheaf is coherent.

**Exercise 4.4.** Let \(\mathcal S\) be coherent on \(M\) and \(s\in\mathcal S(M)\). Show that \(\{x:\ s_x=0\}\) is open and that \(\{x:\ s_x\neq0\}\) is an analytic subset.

*Solution.* If \(s_x=0\), then \(s\) vanishes on a neighbourhood of \(x\) by the definition of germs; so the first set is open. The second set is the support of the image sheaf \(\mathcal O\cdot s\subset\mathcal S\), which is a finitely generated, hence coherent, subsheaf; by Theorem 3.1(3) its support is analytic.

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Oka 1950] K. Oka, Sur les fonctions analytiques de plusieurs variables. VII. Sur quelques notions arithmétiques, *Bulletin de la Société Mathématique de France* 78 (1950), 1–27. <https://www.numdam.org/item/BSMF_1950__78__1_0/>
- [Cartan 1950] H. Cartan, Idéaux et modules de fonctions analytiques de variables complexes, *Bulletin de la Société Mathématique de France* 78 (1950), 29–64. <https://www.numdam.org/item/BSMF_1950__78__29_0/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
