# Homotopy sheaves and the free abelian Whitehead theorem

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A simplicial object of a topos can be studied through its homotopy sheaves, or through the complex of abelian sheaves obtained by taking free abelian groups in each degree and normalizing. This course passes constantly between the two: for instance, a quasi-isomorphism of simplicial objects must induce an isomorphism in cohomology. The basic comparison is Illusie's form of the Whitehead theorem: if \(f\) is an \(n\)-quasi-isomorphism of simplicial sheaves, then so is the map \(\mathbb Z^{(f)}\) of free abelian simplicial sheaves, provided the topos has enough points or \(f\) is a homomorphism of simplicial abelian groups.

This lesson defines homotopy sheaves and proves that they commute with filtered colimits and with inverse images. It proves the theorem for simplicial sets by a simplicial argument, using horn fillers but no topology. It then proves both cases of the theorem for a topos: through points, and through Deligne's local inductive limits.

**Prerequisites.** [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), Sections 4.4, 5.2 and 5.3 (homotopy groups of Kan complexes, the Kan replacement \(A^{\mathrm{Kan}}\), anodyne extensions, Lemmas 5.3a–5.3e, the exact sequence (5.17), Theorem 5.3f and the factorization (5.19)); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution), Theorems 1.1–1.3 and Proposition 1.4 (normalization, Dold–Kan, Eilenberg–Zilber, homotopy groups of simplicial groups); [*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves), Theorems 3.1–3.3, 4.1 and 4.2; [*Topoi, morphisms and points*](course:ag-etale-cohomology/topoi-morphisms-and-points), Sections 1, 3, 4 and 5.

## Conventions

Throughout, \(\mathcal C\) is a small site and \(T=\operatorname{Sh}(\mathcal C)\) its topos. A *simplicial sheaf* is a simplicial object \(X\) of \(T\); its \(m\)-simplices over \(U\in\mathcal C\) form the set \(X_m(U)\), and \(X(U)\) is a simplicial set. For \(U\in\mathcal C\), \(h_U\) is the sheaf associated with the presheaf represented by \(U\), and \(T_{/U}=\operatorname{Sh}(\mathcal C_{/U})\) is the localized topos, equivalent to the category of sheaves over \(h_U\) ([*Topoi, morphisms and points*](course:ag-etale-cohomology/topoi-morphisms-and-points), Theorem 3.1). We write \(X|U\) for the restriction of \(X\) to it. A *base point of \(X\) over \(U\)* is a section \(x\in X_0(U)\); it is the same as a map from the terminal simplicial sheaf of \(T_{/U}\) to \(X|U\).

For a set \(S\), \(\mathbb Z[S]\) is the free abelian group on \(S\). For a sheaf \(E\), \(\mathbb Z^{(E)}\) is the free abelian sheaf on \(E\): the sheaf associated with \(U\mapsto\mathbb Z[E(U)]\). It is left adjoint to the functor forgetting the group structure. For a simplicial set \(K\) (or simplicial sheaf \(X\)) the free construction is applied in each degree and gives a simplicial abelian group \(\mathbb Z[K]\) (or simplicial abelian sheaf \(\mathbb Z^{(X)}\)).

For a simplicial set \(K\) we use the normalized chain complex \(N\mathbb Z[K]\): the quotient of the unnormalized complex by the subcomplex spanned by degenerate simplices. In degree \(q\) it is free on the nondegenerate \(q\)-simplices, with differential \(\sum_j(-1)^jd_j\), in which degenerate faces are omitted. A map of simplicial sets induces a chain map, since it sends degenerate simplices to degenerate simplices. By Theorem 1.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex), this complex has the same homology as the unnormalized and Moore complexes. We write \(H_q(K)\) for \(H_q(N\mathbb Z[K])\).

## 1. Homotopy sheaves

### 1.1. Homotopy groups by finite limits and colimits

For a Kan complex \(K\) and a vertex \(x\), Section 5.3 of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes) defines \(\pi_n(K,x)\) for \(n\geq1\) as the set of \(n\)-cycles at \(x\) (simplices \(a\in K_n\) with \(d_ia=e_{n-1}(x)\) for all \(i\)) modulo the relation (5.12), which is an equivalence relation there. For every simplicial set \(A\), let \(\pi_0(A)\) be the coequalizer of \(d_0,d_1\colon A_1\rightrightarrows A_0\), the set of components.

Section 5.2 of the same lesson constructs, functorially in \(A\), a Kan complex \(A^{\mathrm{Kan}}=\bigcup_rA^{(r)}\): \(A^{(r+1)}\) is obtained from \(A^{(r)}\) by attaching one copy of \(\Delta[m]\) along every horn map \(\Lambda^k[m]\to A^{(r)}\), for all \(m\geq1\) and \(0\le k\le m\). The inclusion \(A\subset A^{\mathrm{Kan}}\) is anodyne.

**Definition 1.1.** For a simplicial set \(A\), a vertex \(x\) and \(n\geq1\), put \(\pi_n(A,x)=\pi_n(A^{\mathrm{Kan}},x)\).

**Lemma 1.2.**

1. A map \(A\to B\) induces maps on all \(\pi_n\), functorially.
2. If \(A\) is Kan, the inclusion \(A\subset A^{\mathrm{Kan}}\) is a simplicial homotopy equivalence; it induces a bijection on \(\pi_0\) and isomorphisms on all \(\pi_n\), so Definition 1.1 agrees with the original groups.
3. For every \(A\), the inclusion \(A\subset A^{\mathrm{Kan}}\) induces a bijection \(\pi_0(A)\to\pi_0(A^{\mathrm{Kan}})\).
4. If \(A\) is a simplicial group, \(\pi_n(A,1)\cong H_n(NA)\) for \(n\ge0\), and right translation by \(x^{-1}\) gives an isomorphism \(\pi_n(A,x)\cong\pi_n(A,1)\) for every vertex \(x\).

**Proof.** (1) holds because \(A\mapsto A^{\mathrm{Kan}}\) is a functor and \(\pi_n\) of Kan complexes is functorial.

(2) Since \(A\) is Kan and \(i\colon A\subset A^{\mathrm{Kan}}\) is anodyne, the identity of \(A\) extends to \(r\colon A^{\mathrm{Kan}}\to A\) with \(ri=1\). The maps \(ir\) and \(1\) agree on \(A\), and (5.14) of the same lesson gives a homotopy \(ir\simeq1\) fixing \(A\). This is the argument in the proof of Theorem 5.3f there, and the converse half of Theorem 5.3f gives the bijection and the isomorphisms.

(3) Attaching \(\Delta[1]\) along a vertex adds one vertex joined by an edge to an old one. Attaching \(\Delta[m]\), \(m\geq2\), along a horn adds no vertex, since \(\Lambda^k[m]\) contains every vertex of \(\Delta[m]\), and it adds edges only between vertices that the horn already joins. Neither operation changes the set of components, and a countable union of such stages does not either.

(4) A simplicial group is Kan, and \(\pi_n(A,1)=H_n(NA)\) by Proposition 1.4 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex). Right translation by \(x^{-1}\) is an automorphism of the simplicial set \(A\) taking \(x\) to \(1\). By (2) the Kan replacement does not change these groups. \(\square\)

**Lemma 1.3.** For every \(n\geq0\), the pointed set \(\pi_n(A,x)\) (and for \(n\ge1\) its group law) is obtained from the sets \(A_m\), the face and degeneracy maps and the vertex \(x\) by a construction that uses only finite limits, finite and countable coproducts, pushouts, a sequential colimit, coequalizers and images.

**Proof.** The set of horn maps \(\Lambda^k[m]\to A^{(r)}\) is a finite limit of the sets \(A^{(r)}_j\), because \(\Lambda^k[m]\) has finitely many nondegenerate simplices. In degree \(j\), the attachment is the pushout of
\[
\begin{aligned}A^{(r)}_j&\longleftarrow\coprod_{m,k}\operatorname{Hom}(\Lambda^k[m],A^{(r)})\times\Lambda^k[m]_j\\&\longrightarrow\coprod_{m,k}\operatorname{Hom}(\Lambda^k[m],A^{(r)})\times\Delta[m]_j,\end{aligned}
\]
and a product with a finite set is a finite coproduct. Then \(A^{\mathrm{Kan}}\) is the sequential colimit of the \(A^{(r)}\). For a Kan complex \(K\), the set \(Z_n\) of \(n\)-cycles at \(x\) is a finite limit, and so is the set \(W_n\) of simplices \(H\in K_{n+1}\) satisfying (5.12) with \(a,b\in Z_n\). The relation (5.12) is an equivalence relation, so \(\pi_n(K,x)\) is the coequalizer of the two maps \(W_n\rightrightarrows Z_n\), \(H\mapsto d_{n+1}H\) and \(H\mapsto d_nH\). The product in \(\pi_n\) is specified by horn fillers whose final three faces are \(b,c,a\), all other faces being constant. Let \(P\) be the finite limit consisting of such fillers. The graph of the multiplication is the image of \(P\) in \(\pi_n^3\), and images are coequalizers of kernel pairs. The inverse is obtained in the same way. \(\square\)

### 1.2. The sheaf version

Let \(X\) be a simplicial sheaf with a global base point \(x\). Performing the construction of Lemma 1.3 with limits and colimits taken in \(T\) gives a sheaf \(\pi_n(X,x)\), the *\(n\)-th homotopy sheaf*. For a base point over \(U\in\mathcal C\) we apply this in \(T_{/U}\) and write \(\pi_n(X|U,x)\).

**Proposition 1.4.** \(\pi_n(X,x)\) is the sheaf associated with the presheaf \(U\mapsto\pi_n(X(U),x|_U)\). For \(n\ge1\) it is a sheaf of groups, abelian for \(n\ge2\).

**Proof.** In presheaves, limits and colimits are computed on sections. The construction of Lemma 1.3 performed on \(X\) regarded as a presheaf therefore gives the presheaf \(U\mapsto\pi_n(X(U),x|_U)\). Sheafification preserves colimits, being a left adjoint ([*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves), Theorems 3.2 and 4.2). It also preserves finite limits (Theorem 3.3 there). Hence it carries the presheaf construction on \(X\) to the same construction performed in \(T\) on the sheafification of \(X\), which is \(X\) itself. The group laws are carried along because they are given by the same diagrams. \(\square\)

**Proposition 1.5.** Let \(n\geq0\).

1. If \((X_\lambda,x_\lambda)\) is a filtered system of pointed simplicial sheaves, the canonical map \(\varinjlim_\lambda\pi_n(X_\lambda,x_\lambda)\to\pi_n(X,x)\) is an isomorphism, where \(X=\varinjlim_\lambda X_\lambda\) and \(x=\varinjlim_\lambda x_\lambda\).
2. If \(\Phi\colon T\to T'\) is a functor to a topos (or to the category of sets) that preserves colimits and finite limits, the canonical map \(\Phi\pi_n(X,x)\to\pi_n(\Phi X,\Phi x)\) is an isomorphism. This applies to the inverse image \(f^{-1}\) of a morphism of topoi \(f\colon T'\to T\).
3. In particular, for a point \(p\) of \(T\), \(\pi_n(X,x)_p\cong\pi_n(X_p,x_p)\).

**Proof.** (1) Filtered colimits in \(T\) are sheafifications of filtered colimits of presheaves. Filtered colimits of sets commute with finite limits, so filtered colimits of presheaves do too, and sheafification is exact. Filtered colimits therefore commute with every operation in Lemma 1.3. (2) \(\Phi\) preserves every operation in Lemma 1.3. The inverse image \(f^{-1}\) preserves colimits, being a left adjoint, and finite limits by definition of a morphism of topoi. (3) A point is a morphism from the topos of sets, with \(p^{-1}F=F_p\) ([*Topoi, morphisms and points*](course:ag-etale-cohomology/topoi-morphisms-and-points), Theorem 4.1). \(\square\)

For a simplicial abelian sheaf \(G\), Lemma 1.2(4) and Proposition 1.4 give natural isomorphisms
\[
\begin{aligned}\pi_n(G|U,x)&\cong\pi_n(G|U,0)\\&\cong H_n(NG)|U\end{aligned}
\tag{1.1}
\]
for every base point \(x\) over \(U\). Here \(NG\) is the normalized complex of abelian sheaves; its homology is the sheaf associated with the homology of sections, because sheafification is exact.

## 2. \(n\)-quasi-isomorphisms

**Definition 2.1.** Let \(f\colon X\to Y\) be a map of simplicial sheaves and \(n\in\mathbb N\). Then \(f\) is an *\(n\)-quasi-isomorphism* if \(\pi_0(f)\colon\pi_0(X)\to\pi_0(Y)\) is an epimorphism and, for every \(U\in\mathcal C\) and every base point \(x\) of \(X\) over \(U\), the map
\[
\begin{aligned}&\pi_i(f|U,x)\colon\\&\quad\pi_i(X|U,x)\to\pi_i(Y|U,f(x))\end{aligned}
\]
is an isomorphism for \(i<n\) and an epimorphism for \(i=n\). It is a *quasi-isomorphism* if it is an \(n\)-quasi-isomorphism for every \(n\). For simplicial sets (the topos of sets) the condition is imposed at every vertex.

For \(n\geq1\) the condition at \(i=0\) makes \(\pi_0(f)\) an isomorphism (Exercise 7.1). By (1.1), a map \(f\) of simplicial abelian sheaves is an \(n\)-quasi-isomorphism exactly when \(H_i(Nf)\) is an isomorphism for \(i<n\) and an epimorphism for \(i=n\). In cohomological indexing, \(N^{-q}=N_q\), this says that the cone of \(Nf\) is acyclic in degrees \(\geq-n\).

**Lemma 2.2.** Let \(\mathcal P\) be a conservative family of points of \(T\), and let \(f\colon X\to Y\) be a map of simplicial sheaves.

1. If \(f\) is an \(n\)-quasi-isomorphism, then \(f_p\colon X_p\to Y_p\) is an \(n\)-quasi-isomorphism of simplicial sets for every point \(p\).
2. If \(f_p\) is an \(n\)-quasi-isomorphism for every \(p\in\mathcal P\), then \(f\) is an \(n\)-quasi-isomorphism.

**Proof.** Let \(p\) be a point and \(U\in\mathcal C\). For \(u\) in the stalk \(h_{U,p}\), let \(\Phi_u(G)\) be the fibre over \(u\) of \(G_p\to h_{U,p}\), for \(G\) a sheaf over \(h_U\), that is, an object of \(T_{/U}\). The functor \(\Phi_u\) preserves colimits, which in \(T_{/U}\) are computed in \(T\), and finite limits, which in \(T_{/U}\) are fibre products over \(h_U\) (the terminal object \(h_U\) goes to a point). For a sheaf \(F\) on \(T\), \(\Phi_u(F|U)=\Phi_u(F\times h_U)=F_p\). By Proposition 1.5(2), \(\Phi_u\) commutes with homotopy sheaves.

(1) Stalks preserve epimorphisms, so \(\pi_0(f)_p=\pi_0(f_p)\) is surjective. A vertex \(\xi\) of \(X_p\) is the germ of a base point \(x\in X_0(U)\) for some \(U\) and some \(u\in h_{U,p}\) ([*Topoi, morphisms and points*](course:ag-etale-cohomology/topoi-morphisms-and-points), Theorem 4.1). The map \(\pi_i(f_p)\) at \(\xi\) is \(\Phi_u\pi_i(f|U,x)\), so it is bijective for \(i<n\) and surjective for \(i=n\).

(2) A map \(g\colon G\to G'\) in \(T_{/U}\) is an isomorphism (respectively an epimorphism) exactly when its underlying map in \(T\) is one, since colimits and finite limits in \(T_{/U}\) are computed from those of \(T\). By Proposition 5.1 of [*Topoi, morphisms and points*](course:ag-etale-cohomology/topoi-morphisms-and-points), this holds exactly when \(g_p\) is bijective (respectively surjective) for every \(p\in\mathcal P\). Since \(g_p\) is a map over \(h_{U,p}\), that holds exactly when every \(\Phi_u(g)\) is bijective (respectively surjective), for \(p\in\mathcal P\) and \(u\in h_{U,p}\). Apply this to \(g=\pi_i(f|U,x)\), for which \(\Phi_u(g)\) is \(\pi_i(f_p)\) at the vertex \(x_p\), and to \(\pi_0(f)\), whose stalk at \(p\) is \(\pi_0(f_p)\). \(\square\)

## 3. The theorem for simplicial sets

**Theorem 3.1.** Let \(f\colon K\to L\) be an \(n\)-quasi-isomorphism of simplicial sets, \(n\geq0\). Then \(H_i(K)\to H_i(L)\) is an isomorphism for \(i<n\) and surjective for \(i=n\). Equivalently, \(\mathbb Z[f]\) is an \(n\)-quasi-isomorphism of simplicial abelian groups.

The equivalence of the two formulations is (1.1) for the topos of sets. We prove the theorem in four steps.

**Lemma 3.2.** For every simplicial set \(A\), the inclusion \(A\subset A^{\mathrm{Kan}}\) induces isomorphisms \(H_*(A)\to H_*(A^{\mathrm{Kan}})\).

**Proof.** The nondegenerate simplices of \(\Delta[m]\) are the nonempty subsets of \([m]\), and those of \(\Lambda^k[m]\) are the subsets that omit some \(j\neq k\). The relative complex \(N\mathbb Z[\Delta[m]]/N\mathbb Z[\Lambda^k[m]]\) is therefore free on the two simplices \([m]\) and \(d_k[m]=[m]\smallsetminus\{k\}\). Modulo the horn, \(\partial[m]=(-1)^kd_k[m]\), so the relative complex is acyclic.

The free abelian functor and normalization take a pushout of simplicial sets along a monomorphism to a pushout of complexes, and normalization is exact (Theorem 1.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex)). Hence \(N\mathbb Z[A^{(r+1)}]/N\mathbb Z[A^{(r)}]\) is a direct sum of copies of these acyclic relative complexes, and each inclusion \(A^{(r)}\subset A^{(r+1)}\) induces isomorphisms on homology. Homology commutes with increasing unions of complexes. \(\square\)

**Lemma 3.3.** Let \(h\colon S\times\Delta[1]\to E\) be a simplicial homotopy from \(g_0=h|_{S\times\{0\}}\) to \(g_1=h|_{S\times\{1\}}\). Then \(N\mathbb Z[g_0]\) and \(N\mathbb Z[g_1]\) are chain homotopic.

**Proof.** Degreewise \(\mathbb Z[S\times\Delta[1]]=\mathbb Z[S]\otimes\mathbb Z[\Delta[1]]\). Theorem 1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex) gives the natural shuffle chain map \(\operatorname{sh}\colon N\mathbb Z[S]\otimes N\mathbb Z[\Delta[1]]\to N\mathbb Z[S\times\Delta[1]]\). On \(v\otimes[\epsilon]\), for a vertex \(\epsilon\) of \(\Delta[1]\), it is the simplex \(v\times\{\epsilon\}\). Let \(\iota\) be the edge of \(\Delta[1]\), so \(\partial\iota=[1]-[0]\). For \(v\) of degree \(q\), put \(P(v)=(-1)^q\,h_*\operatorname{sh}(v\otimes\iota)\). Since \(\operatorname{sh}\) is a chain map,
\[
\begin{aligned}&\partial\operatorname{sh}(v\otimes\iota)\\&\quad=\operatorname{sh}(\partial v\otimes\iota)\\&\qquad+(-1)^q\bigl(v\times\{1\}-v\times\{0\}\bigr),\end{aligned}
\]
and applying \(h_*\) gives \(\partial P(v)+P(\partial v)=g_{1*}v-g_{0*}v\). \(\square\)

**Lemma 3.4.** Let \(p\colon E\to L\) be a Kan fibration of Kan complexes which is an \(n\)-quasi-isomorphism. Then \(p\) has the right lifting property for \(\partial\Delta[m]\subset\Delta[m]\) whenever \(m\le n\). Consequently \(p\) lifts against every monomorphism \(A\subset B\) such that every nondegenerate simplex of \(B\) not in \(A\) has dimension \(\le n\).

**Proof.** We first show that every fibre \(F_b\) is nonempty, connected if \(n\geq1\), and has \(\pi_j(F_b,e)=0\) for \(1\le j\le n-1\). Nonemptiness uses only surjectivity on components: lift a path to \(b\) from a vertex of \(E\) in a component over that of \(b\), as in the proof of Lemma 5.3d of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes). For \(n\geq1\) connectedness uses injectivity on components and surjectivity on \(\pi_1\), by the argument of the same proof.

Let \(1\le j\le n-1\) and use the exact sequence (5.17) there. The map \(\pi_{j+1}(E)\to\pi_{j+1}(L)\) is surjective because \(j+1\le n\), so the boundary map \(\delta\colon\pi_{j+1}(L)\to\pi_j(F_b)\) is zero. Hence \(\pi_j(F_b)\to\pi_j(E)\) has zero kernel. Its image is the kernel of \(\pi_j(E)\to\pi_j(L)\), which is zero because \(j<n\). Thus \(\pi_j(F_b,e)=0\).

The proof of Lemma 5.3c there, carried out for a single dimension \(m\), fills \(\partial\Delta[m]\) in a nonempty Kan complex \(F\) using only the following: for \(m=1\), that \(F\) is connected; for \(m\ge2\), that \(F\) is connected and \(\pi_{m-1}(F,x)=0\). For \(m\le n\) these hold in every fibre. The proof of Lemma 5.3e, carried out in dimension \(m\), uses only this filling in the fibre over \(b(0)\) and the lifting (5.13). This gives the lifting property for \(m\le n\). A monomorphism of the stated kind is built by attaching its missing nondegenerate simplices along their boundaries in order of dimension, and \(p\) lifts against each attachment. \(\square\)

**Proof of Theorem 3.1.** *Reduction to Kan complexes.* Apply the functor \((-)^{\mathrm{Kan}}\). By Definition 1.1 and Lemma 1.2(3), \(f\) is an \(n\)-quasi-isomorphism exactly when \(f^{\mathrm{Kan}}\) is. By Lemma 3.2, the homology maps of \(f\) and \(f^{\mathrm{Kan}}\) agree up to isomorphism. So assume \(K\) and \(L\) are Kan.

*Factorization.* By (5.19) of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), \(f=pi\) with \(i\colon K\to E\) anodyne, \(p\colon E\to L\) a Kan fibration and \(E\) Kan. The proof of Theorem 5.3f there shows that \(i\) is a simplicial homotopy equivalence. It also shows that, since \(f\) bijects components and is bijective (respectively surjective) on \(\pi_i\) at every vertex, so is \(p\), in the same degrees. By Lemma 3.3, \(N\mathbb Z[i]\) is a chain homotopy equivalence. It remains to prove the theorem for \(p\), which satisfies Lemma 3.4.

*Surjectivity for \(i\le n\).* Let \(z\in N_i\mathbb Z[L]\) be a cycle, and let \(S\subset L\) be the finite simplicial subset generated by the simplices occurring in \(z\). It has dimension \(\le i\le n\). By Lemma 3.4 applied to \(\varnothing\subset S\), there is \(\sigma\colon S\to E\) with \(p\sigma\) equal to the inclusion of \(S\). Then \(\sigma_*z\) is a cycle with \(p_*\sigma_*z=z\).

*Injectivity for \(i<n\).* Let \(y\in N_i\mathbb Z[E]\) be a cycle with \(p_*y=\partial w\), \(w\in N_{i+1}\mathbb Z[L]\). Let \(R\subset E\) be generated by the simplices of \(y\), and let \(S\subset L\) be generated by \(p(R)\) and the simplices of \(w\). Then \(\dim R\le i\) and \(\dim S\le i+1\le n\). Lemma 3.4 gives a section \(\sigma\colon S\to E\) of \(p\) over \(S\).

Consider the square with top map \(R\times\partial\Delta[1]\to E\), equal to the inclusion on \(R\times\{0\}\) and to \(\sigma p|_R\) on \(R\times\{1\}\), and bottom map \(R\times\Delta[1]\to L\), \((r,t)\mapsto p(r)\). It commutes because \(p\sigma p=p\) on \(R\). Every nondegenerate simplex of \(R\times\Delta[1]\) has dimension \(\le i+1\le n\), so Lemma 3.4 gives a lift \(h\colon R\times\Delta[1]\to E\). By Lemma 3.3,
\[
\sigma_*p_*y-y=\partial P(y)+P(\partial y)=\partial P(y).
\]
Since \(w\) lies in \(N\mathbb Z[S]\), \(\sigma_*p_*y=\sigma_*\partial w=\partial\sigma_*w\). Therefore \(y=\partial(\sigma_*w-P(y))\) is a boundary. \(\square\)

Illusie states the topos theorem below for \(n\geq2\). The argument here gives every \(n\geq0\) for simplicial sets, and Sections 4 and 7 carry this range over to topoi.

## 4. Topoi with enough points

**Theorem 4.1.** Let \(T\) have enough points, and let \(f\colon X\to Y\) be an \(n\)-quasi-isomorphism of simplicial sheaves. Then \(\mathbb Z^{(f)}\colon\mathbb Z^{(X)}\to\mathbb Z^{(Y)}\) is an \(n\)-quasi-isomorphism.

**Proof.** For a morphism of topoi \(g\colon T'\to T\) and a sheaf \(E\), there is a natural isomorphism \(g^{-1}\mathbb Z^{(E)}\cong\mathbb Z^{(g^{-1}E)}\). Indeed, for an abelian sheaf \(B\) on \(T'\),
\[
\begin{aligned}\operatorname{Hom}(g^{-1}\mathbb Z^{(E)},B)&=\operatorname{Hom}(\mathbb Z^{(E)},g_*B)\\&=\operatorname{Hom}_T(E,g_*B)\\&=\operatorname{Hom}_{T'}(g^{-1}E,B),\end{aligned}
\]
using that \(g_*\) of an abelian sheaf is an abelian sheaf with underlying sheaf \(g_*\) of the underlying sheaf. For a point \(p\) this gives \(\mathbb Z^{(X)}_p=\mathbb Z[X_p]\).

Let \(\mathcal P\) be a conservative family of points. By Lemma 2.2(1), each \(f_p\) is an \(n\)-quasi-isomorphism. By Theorem 3.1, each \(\mathbb Z[f_p]=\mathbb Z^{(f)}_p\) is one, and Lemma 2.2(2) applied to \(\mathbb Z^{(f)}\) concludes. \(\square\)

## 5. Local inductive limits

The second case of the theorem needs no points. Its proof, which Illusie credits to a suggestion of Deligne, approximates a complex of sheaves locally by complexes of finitely generated abelian groups. The tool is Deligne's notion of a local inductive limit.

**Definition 5.1.** A *locally filtered system* \(L\) over \(\mathcal C\) assigns to every \(U\in\mathcal C\) a category \(L(U)\) and to every arrow \(V\to U\) of \(\mathcal C\) a restriction functor \(L(U)\to L(V)\), \(i\mapsto i|V\), functorially in \(V\to U\), such that:

- (LF0) every \(U\) has a covering \(\{U_\alpha\to U\}\) with every \(L(U_\alpha)\) nonempty;
- (LF1) for \(i,j\in L(U)\) there are a covering \(\{U_\alpha\to U\}\) and objects \(k_\alpha\in L(U_\alpha)\) with arrows \(i|U_\alpha\to k_\alpha\) and \(j|U_\alpha\to k_\alpha\);
- (LF2) for parallel arrows \(a,b\colon i\rightrightarrows j\) in \(L(U)\) there are a covering \(\{U_\alpha\to U\}\) and arrows \(c_\alpha\colon j|U_\alpha\to k_\alpha\) with \(c_\alpha(a|U_\alpha)=c_\alpha(b|U_\alpha)\).

A *local system* \(F\) on \(L\) assigns a set \(F(i)\) to every object, maps \(F(a)\colon F(i)\to F(j)\) to arrows of each \(L(U)\), and restriction maps \(F(i)\to F(i|V)\), functorially and compatibly. A sheaf \(E\) gives the *constant* local system \(E_L(i)=E(U)\) for \(i\in L(U)\).

**Construction 5.2.** Put \(P_F(U)=\varinjlim_{i\in L(U)}F(i)\), a colimit of sets over the category \(L(U)\), with restriction maps induced by \(i\mapsto i|V\). Define the *local inductive limit* \(\varinjlim_LF\) to be the sheaf associated with the presheaf \(P_F\).

**Proposition 5.3.** \(\operatorname{Hom}_T(\varinjlim_LF,E)\cong\operatorname{Hom}(F,E_L)\), naturally in \(F\) and in the sheaf \(E\).

**Proof.** By Theorem 3.2 of [*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves), maps from the sheafification are maps of presheaves \(P_F\to E\). Such a map is a family of maps \(F(i)\to E(U)\), natural in \(i\in L(U)\) and compatible with restriction, which is a map of local systems \(F\to E_L\). \(\square\)

**Proposition 5.4.**

1. Every section of \(\varinjlim_LF\) over \(U\) is, on some covering \(\{U_\alpha\to U\}\), the image of elements of \(F(i_\alpha)\), \(i_\alpha\in L(U_\alpha)\).
2. If \(s\in F(i)\) and \(t\in F(j)\), \(i,j\in L(U)\), have the same image in \((\varinjlim_LF)(U)\), there are a covering \(\{U_\alpha\to U\}\) and arrows \(a_\alpha\colon i|U_\alpha\to k_\alpha\), \(b_\alpha\colon j|U_\alpha\to k_\alpha\) with \(F(a_\alpha)(s|)=F(b_\alpha)(t|)\).

**Proof.** (1) By the construction of sheafification ([*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves), Theorem 3.1), every section of the associated sheaf is locally a section of \(P_F\), and an element of a colimit of sets is the class of an element of some \(F(i)\).

(2) Two sections of \(P_F(U)\) with the same image in the associated sheaf agree on some covering: they have the same image in \(P_F^+\), and \(P_F^+\to P_F^{++}\) is injective by Theorem 3.1 there. In \(P_F(U_\alpha)\), equality of classes means a finite zigzag of arrows in \(L(U_\alpha)\) carrying one element to the other. We show by induction on the length of a zigzag that its ends become equal at a common target, locally.

Suppose \((k,x)\) and \((k',x')\) already have, locally, arrows to some \(m\) with equal images, and \((k',x')\) is joined to \((k'',x'')\) by one arrow. If the arrow is \(c\colon k'\to k''\) with \(F(c)x'=x''\), use (LF1) to find locally \(m'\) with arrows from \(m\) and from \(k''\). The two resulting arrows \(k'\rightrightarrows m'\), one through \(m\) and one through \(c\), may differ, so use (LF2) to equalize them after a further arrow \(m'\to m''\). Then \(x\) and \(x''\) have the same image in \(F(m'')\). If the arrow is \(c\colon k''\to k'\) with \(F(c)x''=x'\), compose \(c\) with the arrow \(k'\to m\). Finitely many refinements of coverings occur. \(\square\)

**Proposition 5.5.** \(\varinjlim_L\) commutes with finite limits.

**Proof.** *Terminal object.* For the constant one-point system, \(P(U)\) is the set of components of \(L(U)\). By (LF0) the map to the terminal sheaf is locally surjective. By (LF1) any two elements become equal locally. Hence the associated sheaf is terminal.

*Binary products.* For local systems \(F,G\) consider \(\varinjlim_L(F\times G)\to\varinjlim_LF\times\varinjlim_LG\). A local section \(([s],[t])\) of the target, with \(s\in F(i)\) and \(t\in G(j)\), is locally the image of \((F(a)s,G(b)t)\in(F\times G)(k)\), where \(a,b\) are arrows to a common target given by (LF1). Suppose \((s,t)\in(F\times G)(k)\) and \((s',t')\in(F\times G)(k')\) have the same image. By Proposition 5.4(2), applied to the first and second components, there are locally targets \(m_1\) and \(m_2\) equalizing them. Use (LF1) to find a common target \(m\) of \(m_1,m_2\), and (LF2) twice to equalize the two arrows \(k\rightrightarrows m\) and the two arrows \(k'\rightrightarrows m\) after an arrow \(m\to m'\). At \(m'\) the two pairs agree. The map is therefore locally surjective, and injective on local representatives, so it is an isomorphism of sheaves ([*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves), Theorem 4.1).

*Equalizers.* Let \(u,v\colon F\rightrightarrows G\) and \(Q(i)=\{x\in F(i):u(x)=v(x)\}\). The map \(\varinjlim_LQ\to\varinjlim_LF\) is injective: Proposition 5.4(2) applied in \(F\) gives arrows to a common target, and \(Q\) is a subsystem. If a section \([s]\), \(s\in F(i)\), has \([u(s)]=[v(s)]\), then by Proposition 5.4(2) there are locally arrows \(a,b\colon i\rightrightarrows k\) with \(G(a)u(s)=G(b)v(s)\). By (LF2) there is locally an arrow \(c\colon k\to m\) with \(ca=cb=:d\). Then \(u(F(d)s)=v(F(d)s)\), so \(F(d)s\in Q(m)\) represents \([s]\) locally. \(\square\)

**Proposition 5.6.** Let \(L'\subset L\) be a subsystem with each \(L'(U)\) a full subcategory, stable under restriction and *locally cofinal*: every \(i\in L(U)\) has, on some covering, arrows \(i|U_\alpha\to i'_\alpha\) with \(i'_\alpha\in L'(U_\alpha)\). Then \(L'\) is locally filtered and \(\varinjlim_{L'}F|_{L'}\to\varinjlim_LF\) is an isomorphism.

**Proof.** (LF0) and (LF1) for \(L'\) follow from those for \(L\) followed by local cofinality. For (LF2), equalize in \(L\) and then map into \(L'\); the composites are arrows of \(L'\) because \(L'(U)\) is full. The map of local inductive limits is locally surjective by local cofinality, and injective by Proposition 5.4(2) in \(L\) followed by local cofinality. \(\square\)

**Proposition 5.7.**

1. Homotopy sheaves commute with local inductive limits: for a local system of pointed simplicial sets \((X(i),x(i))\) with local inductive limit \((X_\infty,x_\infty)\), \(\pi_n(X_\infty,x_\infty)\cong\varinjlim_L\pi_n(X(i),x(i))\).
2. For local systems of rings \(A(i)\) and sets \(S(i)\), with \(A=\varinjlim_LA(i)\) and \(S=\varinjlim_LS(i)\), the canonical map \(\varinjlim_LA(i)^{(S(i))}\to A^{(S)}\) is an isomorphism.
3. The functors \(N\) and \(K\) of the Dold–Kan correspondence commute with \(\varinjlim_L\).
4. \(\varinjlim_L\) carries a local system of exact sequences of abelian groups to an exact sequence of abelian sheaves, and commutes with homology.

**Proof.** (1) The construction of Lemma 1.3 uses finite limits and colimits, which \(\varinjlim_L\) preserves by Propositions 5.3 and 5.5. (3) and (4) hold for the same reason: \(N\) uses kernels and \(K\) uses finite direct sums (Theorem 1.2 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex)), and homology is built from kernels and cokernels. (2) For a sheaf of \(A\)-modules \(M\), an \(A\)-linear map from the left side is, by Proposition 5.3, a compatible family of \(A(i)\)-linear maps \(A(i)^{(S(i))}\to M(U)\). These are the same as compatible families of maps \(S(i)\to M(U)\), that is, maps of sheaves \(S\to M\), that is, \(A\)-linear maps \(A^{(S)}\to M\). \(\square\)

## 6. Approximation by finitely presented complexes

Let \(A\) be a ring, also written \(A\) for the constant sheaf of rings, and use cohomological indexing for complexes of \(A\)-modules. For a complex \(C\) of \(A\)-modules, \(C_U\) is the constant complex on \(\mathcal C_{/U}\), and maps \(C_U\to E|U\) correspond to maps of complexes \(C\to E(U)\), because the constant-module functor is left adjoint to sections.

**Construction 6.1.** Let \(u\colon E\to F\) be a map of complexes of \(A\)-modules on \(\mathcal C\). For \(U\in\mathcal C\) let \(L_u(U)\) be the category whose objects are pairs \((v,\varphi)\), where \(v\colon C\to D\) is a map of bounded complexes of finitely presented \(A\)-modules and \(\varphi=(\varphi_C,\varphi_D)\) is a map of arrows of complexes from \(C_U\to D_U\) to \(E|U\to F|U\). The arrows of \(L_u(U)\) are maps of arrows of complexes compatible with the \(\varphi\). Restriction keeps \(v\) and restricts \(\varphi\). The local systems \(i\mapsto C_i^q\), \(i\mapsto D_i^q\) and \(i\mapsto v_i\) are the *tautological* ones.

**Lemma 6.2.** Each \(L_u(U)\) is filtered, so \(L_u\) is locally filtered, and \(\varinjlim_{L_u}v_i=u\). If \(E\) and \(F\) vanish in degrees \(>a\), the objects whose complexes vanish in degrees \(>a\) are cofinal.

**Proof.** The zero complex gives an object, direct sums give common targets, and for parallel arrows \(\alpha,\beta\) the cokernel of \(\alpha-\beta\) (which is finitely presented) receives the maps \(\varphi\), because \(\varphi\circ(\alpha-\beta)=0\).

Fix a degree \(q\). Every \(x\in E^q(U)\) lies in the image of some object: take \(C=D=[A\xrightarrow{1}A]\) in degrees \(q,q+1\) and \(v=1\), with \(\varphi_C\) sending \(1\) to \(x\) and \(dx\), and \(\varphi_D\) sending \(1\) to \(u(x)\) and \(du(x)\). If \(z\in C_i^q\) maps to \(0\) in \(E^q(U)\), divide \(C_i\) by the subcomplex generated by \(z\) and \(dz\), and \(D_i\) by that generated by \(v(z)\) and \(dv(z)\). Both quotients are finitely presented, and \(\varphi\) factors through them because \(\varphi(z)=0\) and \(u\varphi(z)=0\). This gives an arrow of \(L_u(U)\) killing \(z\). The same holds for \(F\). Hence \(P(U)\to E^q(U)\) is bijective for every \(U\), and the associated sheaf is \(E^q\).

For the boundedness statement, the terms in degrees \(>a\) form a subcomplex. The quotient by it still receives \(\varphi\) when \(E\) and \(F\) vanish there. \(\square\)

**Lemma 6.3 (killing a kernel).** Suppose \(H^{q+1}(u)\) is injective, and let \(i=(v\colon C\to D,\varphi)\in L_u(U)\) be such that \(H^q(\operatorname{Cone}v)\) is a finitely generated \(A\)-module. Then there are a covering \(\{U_\alpha\to U\}\) and arrows \(i|U_\alpha\to i'_\alpha\) in \(L_u(U_\alpha)\) such that \(H^{q+1}(v'_\alpha)\) is injective with the same image as \(H^{q+1}(v)\), \(v'_\alpha\) agrees with \(v\) in degrees \(\ne q\), and the cokernel of \(v\to v'_\alpha\) is the identity of a finite free module placed in degree \(q\).

**Proof.** By the cone sequence, \(\ker H^{q+1}(v)\) is the image of \(H^q(\operatorname{Cone}v)\), hence finitely generated. Choose a finite free module \(M\) and \(c\colon M\to Z^{q+1}(C)\) whose classes generate \(\ker H^{q+1}(v)\). Then \(vc=dt\) for some \(t\colon M\to D^q\). The class of \(\varphi_Cc\) in \(H^{q+1}(E)(U)\) maps to the class of \(u\varphi_Cc=\varphi_Dvc=d\varphi_Dt\), which is zero. Since \(H^{q+1}(u)\) is injective, \(\varphi_Cc\) is locally a boundary: on a covering, \(\varphi_Cc=ds\) with \(s\colon M\to E^q|U_\alpha\). Put \(\delta=us-\varphi_Dt\colon M\to F^q\); then \(d\delta=u\varphi_Cc-\varphi_Dvc=0\).

Let \(C'=C\oplus M\) and \(D'=D\oplus M\), with \(M\) in degree \(q\), \(d'(m)=c(m)\) in \(C'\) and \(d'(m)=0\) in \(D'\). Let \(v'(x,m)=(vx+tm,m)\) in degree \(q\). Extend \(\varphi_C\) by \(s\) and \(\varphi_D\) by \(\delta\). One checks directly that \(v'\) is a chain map, that the extended maps are chain maps, and that \(u\varphi'_C=\varphi'_Dv'\) in degree \(q\), where both sides send \((x,m)\) to \(u\varphi_Cx+us(m)\). Finally \(H^{q+1}(C')=H^{q+1}(C)/\ker H^{q+1}(v)\) and \(H^{q+1}(D')=H^{q+1}(D)\). \(\square\)

**Lemma 6.4 (adding a cokernel).** Suppose \(H^q(u)\) is surjective, and let \(i=(v,\varphi)\in L_u(U)\) with \(H^{q+1}(v)\) injective and \(H^q(\operatorname{Cone}v)\) finitely generated. Then there are a covering \(\{U_\alpha\to U\}\) and arrows \(i|U_\alpha\to i'_\alpha\) such that \(H^{q+1}(v'_\alpha)=H^{q+1}(v)\), \(H^q(v'_\alpha)\) is surjective, and \(v'_\alpha\) agrees with \(v\) outside degrees \(q-1,q\).

**Proof.** Since \(H^{q+1}(v)\) is injective, \(H^q(D)\to H^q(\operatorname{Cone}v)\) is surjective. Choose a finite free \(M\) and \(t\colon M\to Z^q(D)\) whose classes, together with the image of \(H^q(v)\), generate \(H^q(D)\). Since \(H^q(u)\) is surjective, there is locally \(s\colon M\to Z^q(E|U_\alpha)\) with \([us]=[\varphi_Dt]\). Then \(\delta=us-\varphi_Dt\) is locally a boundary, \(\delta=d\varepsilon\) with \(\varepsilon\colon M\to F^{q-1}\).

Let \(C'=C\oplus M\) with \(M\) in degree \(q\) and zero differential. Let \(D'=D\oplus J\), where \(J=[M\xrightarrow{1}M]\) sits in degrees \(q-1,q\). Put \(v'(x,m)=(vx+tm,m)\) in degree \(q\), and \(v'=(v,0)\) in degree \(q-1\). Extend \(\varphi_C\) by \(s\), and \(\varphi_D\) by \(\varepsilon\) in degree \(q-1\) and \(\delta\) in degree \(q\). The chain-map identities reduce to \(d\varepsilon=\delta\), \(ds=0\), \(dt=0\) and \(\delta=us-\varphi_Dt\). Since \(J\) is acyclic and \(M\subset Z^q(C')\) adds no boundaries in degree \(q+1\), \(H^{q+1}\) is unchanged. In \(H^q(D')=H^q(D)\) the class of \((tm,m)\) is that of \(tm\), because \((0,m)\) is the boundary of \((0,m)\in D'^{q-1}\). So \(H^q(v')\) is surjective. \(\square\)

**Lemma 6.5.** Let \(A\) be Noetherian, and let \(u\colon E\to F\) be a map of complexes of \(A\)-modules vanishing in degrees \(>a\), with \(H^k(u)\) an isomorphism for \(k>b\) and an epimorphism for \(k=b\). Among the objects of \(L_u\) whose complexes vanish in degrees \(>a\), those with \(H^k(v)\) bijective for \(k>b\) and surjective for \(k=b\) form a locally cofinal subsystem.

**Proof.** The cone of such a \(v\) is a bounded complex of finitely generated modules, so its cohomology is finitely generated because \(A\) is Noetherian. Start from an object vanishing above \(a\). For \(q=a,a-1,\dots,b\) in turn, apply Lemma 6.4 in degree \(q\); \(H^{q+1}(v)\) is injective, for \(q=a\) because \(C^{a+1}=0\). This makes \(H^q(v)\) surjective without changing higher degrees. Then, if \(q>b\), apply Lemma 6.3 with index \(q-1\), which uses the injectivity of \(H^q(u)\). This makes \(H^q(v)\) injective with the same, full, image, and changes only degrees \(q-1\) and \(q\). After finitely many steps, each over a finer covering, the object has the required property, and no step adds terms above degree \(a\). \(\square\)

## 7. Homomorphisms of simplicial abelian sheaves

**Theorem 7.1.** Let \(f\colon X\to Y\) be a homomorphism of simplicial abelian sheaves which is an \(n\)-quasi-isomorphism. Then \(\mathbb Z^{(f)}\colon\mathbb Z^{(X)}\to\mathbb Z^{(Y)}\) is an \(n\)-quasi-isomorphism. No hypothesis on points is needed.

**Proof.** By Section 2, \(Nf\colon NX\to NY\), in cohomological indexing, is a map of complexes vanishing in degrees \(>0\) whose cohomology map is bijective in degrees \(>-n\) and surjective in degree \(-n\). Lemmas 6.2 and 6.5, with \(A=\mathbb Z\), \(a=0\) and \(b=-n\), give a locally filtered system \(L\) and a local system of maps \(g_i\colon C_i\to D_i\) of bounded complexes of finitely generated abelian groups, vanishing in degrees \(>0\), each with the same cohomological property, such that \(\varinjlim_Lg_i=Nf\) (Proposition 5.6).

Let \(h_i=K(g_i)\), a homomorphism of simplicial abelian groups. By Proposition 5.7(3) and the Dold–Kan isomorphism \(KN\cong1\), \(\varinjlim_Lh_i\cong f\). Each \(h_i\) is an \(n\)-quasi-isomorphism of simplicial abelian groups, so by Theorem 3.1 each \(\mathbb Z[h_i]\) is an \(n\)-quasi-isomorphism. By Proposition 5.7(2), \(\mathbb Z^{(f)}\cong\varinjlim_L\mathbb Z[h_i]\) in each degree. By Proposition 5.7(3)–(4), \(H_k(N\mathbb Z^{(f)})\) is the local inductive limit of the maps \(H_k(N\mathbb Z[h_i])\). These are bijective for \(k<n\) and surjective for \(k=n\), and \(\varinjlim_L\) preserves isomorphisms and epimorphisms. By (1.1), \(\mathbb Z^{(f)}\) is an \(n\)-quasi-isomorphism. \(\square\)

**Corollary 7.2.** If \(f\) is a quasi-isomorphism of simplicial sheaves, and either \(T\) has enough points or \(f\) is a homomorphism of simplicial abelian sheaves, then \(\mathbb Z^{(f)}\) is a quasi-isomorphism.

**Remark 7.3.** Illusie conjectured that neither hypothesis is needed. For quasi-isomorphisms (all \(n\) at once) this was proved by Van Osdol in 1977. Jardine's lecture notes on local homotopy theory give a short proof by Boolean localization and record that the statement was once called the Illusie conjecture. That proof rests on Barr's theorem, that every Grothendieck topos admits a Boolean localization, which this programme does not prove; the course uses only Theorems 4.1 and 7.1. Jardine's lemma does not cover \(n\)-quasi-isomorphisms for a fixed finite \(n\).

## 8. Exercises

**Exercise 8.1.** Show that for \(n\geq1\) the conditions of Definition 2.1 imply that \(\pi_0(f)\) is an isomorphism.

**Exercise 8.2.** Write out the relative normalized complex of \((\Delta[2],\Lambda^1[2])\) and check that it is acyclic.

**Exercise 8.3.** Let \(f\colon\partial\Delta[2]\to\Delta[0]\). Show that \(f\) is a \(1\)-quasi-isomorphism but not a \(2\)-quasi-isomorphism, and check the conclusion of Theorem 3.1 directly.

**Exercise 8.4.** Let \(L(U)\) be the category with one object and one arrow for every \(U\). Show that \(\varinjlim_LF\) is the sheaf associated with the presheaf \(U\mapsto F(U)\).

## 9. Complete solutions

**8.1.** Surjectivity is part of the definition. For injectivity, let \(\sigma,\tau\) be sections of \(\pi_0(X)\) over \(V\) with the same image under \(\pi_0(f)\). Since \(X_0\to\pi_0(X)\) is an epimorphism, there is a covering of \(V\) by objects \(U\) over which \(\sigma\) is the class of a base point \(x\) of \(X\) over \(U\). By Proposition 1.4, \(\pi_0(X|U,x)=\pi_0(X)|U\), and the condition at \(i=0<n\) says that \(\pi_0(f)|U\) is injective. So \(\sigma|U=\tau|U\) for every \(U\) of the covering, and \(\sigma=\tau\). A monomorphism and epimorphism of sheaves is an isomorphism (Theorem 4.1 of [*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves)).

**8.2.** The nondegenerate simplices of \(\Delta[2]\) not in \(\Lambda^1[2]\) are \(\{0,2\}\) and \(\{0,1,2\}\). Modulo the horn, \(\partial\{0,1,2\}=\{1,2\}-\{0,2\}+\{0,1\}\) is congruent to \(-\{0,2\}\). The relative complex is \(\mathbb Z\xrightarrow{-1}\mathbb Z\) in degrees \(2,1\), which is acyclic.

**8.3.** \(\pi_0\) is a point on both sides. The Kan replacement of \(\partial\Delta[2]\) has \(\pi_1\cong\mathbb Z\), by (5.8) of [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), and \(\pi_1(\Delta[0])=0\). So \(\pi_1(f)\) is surjective but not injective, and \(f\) is a \(1\)- but not a \(2\)-quasi-isomorphism. Directly, \(N\mathbb Z[\partial\Delta[2]]\) is \(\mathbb Z^3\to\mathbb Z^3\) with \(H_0=\mathbb Z\) and \(H_1=\mathbb Z\), generated by \(\{1,2\}-\{0,2\}+\{0,1\}\). The map to \(H_*(\Delta[0])\) is an isomorphism on \(H_0\) and surjective on \(H_1\), as Theorem 3.1 predicts, but not injective on \(H_1\).

**8.4.** The axioms (LF0)–(LF2) hold trivially, and \(P_F(U)=F(U)\), so Construction 5.2 is sheafification.

## Sources

The definitions of homotopy sheaves and \(n\)-quasi-isomorphisms of simplicial sheaves, and Theorems 4.1 and 7.1, are due to Illusie; the local-limit method of Section 6 is Deligne's, as Illusie records. The AI-integrated Stacks project contains a parallel treatment of homotopy sheaves and of the free abelian Whitehead theorem, in the files `illusie_volume_I/homotopy-sheaves.tex` and `illusie_volume_I/whitehead-free-abelian.tex` of [its repository](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts). The simplicial proof of Theorem 3.1 given here uses only the results on Kan complexes proved in [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes). For Remark 7.3: J. F. Jardine, *Local homotopy theory*, lecture notes, lecture 6a, Lemma 13.1 and Remark 13.2, [math.uwo.ca](https://www.math.uwo.ca/faculty/jardine/courses/localhom/localhom-lecture06a.pdf); J. F. Jardine, *Boolean localization, in practice*, Documenta Mathematica 1 (1996), 245–275, [EMIS](https://emis.dsd.sztaki.hu/journals/DMJDMV/vol-01/vol-01-eng.html).
