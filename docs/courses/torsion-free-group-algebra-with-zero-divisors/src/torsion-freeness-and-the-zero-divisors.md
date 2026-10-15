# Torsion-freeness and the zero divisors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that the group of the construction is torsion-free and proves the theorem of the course, Theorem 4.1 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md) [OpenAI-KZ, Sections 5 and 6]. The cone complex \(X\) of [Cone pictures and asphericity](cone-pictures-and-asphericity.md) has \(\pi_2(X)=0\); from this, all higher homotopy groups vanish, and the cellular chains of the universal cover form a free resolution of length two of the trivial module over the group ring. A group with an element of prime order \(\ell\) cannot have such a resolution: restricted to the cyclic subgroup, it would compute group cohomology with coefficients in \(\mathbb F_\ell\) that vanishes above degree two, while the periodic resolution of the cyclic group shows that this cohomology is \(\mathbb F_\ell\) in every degree. The comparison theorem for resolutions, proved here, connects the two computations. The zero divisors then come from the cancellation mechanism of the first lesson.

- The universal cover and asphericity (Section 1).
- Resolutions and the comparison theorem (Section 2).
- Cyclic groups (Section 3).
- Torsion-freeness (Section 4).
- The zero divisors (Section 5).

Throughout, \(\Gamma\) is one of the graphs of Proposition 3.1 of [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md): it has the prescribed types, girth at least \(L\), and admits no reduced spherical arrangement. Its cone complex \(X\), the group \(G=\pi_1(X,o)\), labels, and the inputs (PI1), (COV), (CELL) and the Hurewicz theorem are as in [Cone pictures and asphericity](cone-pictures-and-asphericity.md); \(p\colon\widetilde X\to X\) is the universal cover. Modules are left modules.

## 1. The universal cover and asphericity

A *classifying space* for a group \(G\) is a connected CW complex with fundamental group isomorphic to \(G\) and contractible universal cover.

**Proposition 1.1** (asphericity; [OpenAI-KZ, Corollary 5.3]). \(\pi_n(X)=0\) for all \(n\ge2\), \(\widetilde H_k(\widetilde X;\mathbb Z)=0\) for all \(k\), and \(\widetilde X\) is contractible. So \(X\) is a finite two-dimensional classifying space for \(G\).

*Proof.* By Proposition 6.1 of [Cone pictures and asphericity](cone-pictures-and-asphericity.md), \(\pi_2(X)=0\), so \(\pi_2(\widetilde X)=0\) by (COV 4). The cover \(\widetilde X\) is simply connected, and by (COV 1) it is a CW complex of dimension two whose \(2\)-cells are attached along closed edge paths. The Hurewicz theorem with \(q=2\) gives \(\widetilde H_0(\widetilde X)=H_1(\widetilde X)=0\) and \(H_2(\widetilde X)\cong\pi_2(\widetilde X)=0\), and \(H_k(\widetilde X)=0\) for \(k\ge3\) by (CELL 1). Now let \(q\ge3\) and suppose \(\pi_i(\widetilde X)=0\) for \(1\le i<q\); the Hurewicz theorem gives \(\pi_q(\widetilde X)\cong H_q(\widetilde X)=0\). By induction all homotopy groups of \(\widetilde X\) vanish, and \(\pi_n(X)\cong\pi_n(\widetilde X)=0\) for \(n\ge2\) by (COV 4).

The map from \(\widetilde X\) to a point therefore induces isomorphisms on all homotopy groups, and both spaces are CW complexes. By Whitehead's theorem, a map between CW complexes that induces isomorphisms on all homotopy groups is a homotopy equivalence; this is proved in [Homotopy fibres and the Serre spectral sequence, Section B.4](course:DG-CHAR/DG-CHAR-13B), after Theorem B.5. So \(\widetilde X\) is contractible. \(\square\)

**Lemma 1.2** (the cellular resolution). Let \(C_k\) be the cellular chain groups of \(\widetilde X\), as in (CELL 1), with \(G\) acting by deck transformations. Each \(C_k\) is a free \(\mathbb ZG\)-module, with basis one chosen lift of each \(k\)-cell of \(X\); the boundary maps are \(\mathbb ZG\)-linear; and with the augmentation \(\varepsilon\colon C_0\to\mathbb Z\) sending every vertex to \(1\), where \(G\) acts trivially on \(\mathbb Z\), the sequence
\[
0\longrightarrow C_2\longrightarrow C_1\longrightarrow C_0\xrightarrow{\ \varepsilon\ }\mathbb Z\longrightarrow0
\]
is exact.

*Proof.* Orient every cell of \(X\) and give each of its lifts the orientation lifted through \(p\). Deck transformations commute with \(p\), so they preserve these orientations, and by (COV 1) the group \(G\) permutes the oriented \(k\)-cells of \(\widetilde X\) freely, with one orbit for each \(k\)-cell of \(X\). Hence \(C_k\) is free with basis the chosen lifts. A deck transformation carries the attaching path of a cell to the attaching path of its image, so by the boundary formula of (CELL 1) the boundary maps commute with the action; \(\varepsilon\) commutes with it because vertices go to vertices. By (CELL 1) the augmented complex computes \(\widetilde H_*(\widetilde X;\mathbb Z)\), which vanishes by Proposition 1.1. \(\square\)

A sequence \(\cdots\to P_1\to P_0\to M\to0\) of modules that is exact, with all \(P_k\) free, is a *free resolution* of \(M\). Lemma 1.2 gives a free resolution of the trivial module \(\mathbb Z\) over \(\mathbb ZG\) with \(P_k=0\) for \(k\ge3\).

## 2. Resolutions and the comparison theorem

Let \(R\) be a ring. An *augmented complex* over an \(R\)-module \(M\) is a sequence of \(R\)-linear maps \(\cdots\to P_1\xrightarrow{d}P_0\xrightarrow{\varepsilon}M\) with \(dd=0\) and \(\varepsilon d=0\). A *chain map over* \(\mathrm{id}_M\) between augmented complexes \(P\) and \(C\) consists of \(R\)-linear maps \(\alpha_k\colon P_k\to C_k\) with \(d\alpha_k=\alpha_{k-1}d\) and \(\varepsilon\alpha_0=\varepsilon\). Two chain maps \(\alpha,\alpha'\) are *chain homotopic* if there are \(R\)-linear maps \(s_k\colon P_k\to C_{k+1}\) with
\[
\alpha_k-\alpha_k'=ds_k+s_{k-1}d
\]
for all \(k\ge0\), with \(s_{-1}=0\).

**Lemma 2.1** (comparison; [Hatcher, Lemma 3.1, with the remark on p. 197 that its proof holds over every ring]). Let \(P\) be an augmented complex over \(M\) with all \(P_k\) free, and \(C\) a free resolution of \(M\), or more generally an augmented complex over \(M\) that is exact. Then there is a chain map \(P\to C\) over \(\mathrm{id}_M\), and any two such chain maps are chain homotopic.

*Proof.* *Existence.* For a basis element \(b\) of \(P_0\), choose \(\alpha_0(b)\in C_0\) with \(\varepsilon\alpha_0(b)=\varepsilon(b)\), using that \(\varepsilon\colon C_0\to M\) is onto. Suppose \(\alpha_0,\ldots,\alpha_k\) are constructed. For a basis element \(b\) of \(P_{k+1}\), the element \(\alpha_k(db)\) satisfies \(d\alpha_k(db)=\alpha_{k-1}(ddb)=0\) if \(k\ge1\), and \(\varepsilon\alpha_0(db)=\varepsilon(db)=0\) if \(k=0\). By exactness of \(C\) it is \(d\) of some element of \(C_{k+1}\), which we take as \(\alpha_{k+1}(b)\). Extend linearly.

*Homotopy.* Let \(\alpha,\alpha'\) be two chain maps over \(\mathrm{id}_M\) and \(\beta=\alpha-\alpha'\), so \(\varepsilon\beta_0=0\). For a basis element \(b\) of \(P_0\), \(\beta_0(b)\) lies in \(\ker\varepsilon=dC_1\); choose \(s_0(b)\) with \(ds_0(b)=\beta_0(b)\). Suppose \(s_0,\ldots,s_k\) are constructed with \(\beta_j=ds_j+s_{j-1}d\) for \(j\le k\). For a basis element \(b\) of \(P_{k+1}\),
\[
\begin{aligned}
d\bigl(\beta_{k+1}(b)-s_k(db)\bigr)&=\beta_k(db)-ds_k(db)\\
&=s_{k-1}(ddb)=0,
\end{aligned}
\]
so \(\beta_{k+1}(b)-s_k(db)=ds_{k+1}(b)\) for some \(s_{k+1}(b)\in C_{k+2}\). \(\square\)

For an \(R\)-module \(A\), applying \(\mathrm{Hom}_R(-,A)\) to an augmented complex \(P\), without the term \(M\), gives the cochain complex \(\mathrm{Hom}_R(P_0,A)\to\mathrm{Hom}_R(P_1,A)\to\cdots\), with \(\delta\varphi=\varphi\circ d\).

**Corollary 2.2** (independence of the resolution). For two free resolutions \(P,C\) of \(M\) and every \(R\)-module \(A\), the cochain complexes \(\mathrm{Hom}_R(P,A)\) and \(\mathrm{Hom}_R(C,A)\) have isomorphic cohomology in every degree.

*Proof.* By Lemma 2.1 there are chain maps \(\alpha\colon P\to C\) and \(\beta\colon C\to P\) over \(\mathrm{id}_M\). The composite \(\beta\alpha\) and the identity of \(P\) are both chain maps \(P\to P\) over \(\mathrm{id}_M\), hence chain homotopic, and likewise \(\alpha\beta\) and the identity of \(C\). Applying \(\mathrm{Hom}_R(-,A)\), a chain homotopy \(\gamma-\gamma'=ds+sd\) becomes \(\gamma^*-\gamma'^*=s^*\delta+\delta s^*\), so \(\gamma^*\) and \(\gamma'^*\) agree on cohomology. Hence \(\alpha^*\) and \(\beta^*\) induce mutually inverse isomorphisms. \(\square\)

For a group \(H\), the cohomology of \(\mathrm{Hom}_{\mathbb ZH}(P,A)\) for a free resolution \(P\) of the trivial module \(\mathbb Z\) is the *cohomology* \(H^k(H;A)\) of \(H\) with coefficients in \(A\); by Corollary 2.2 it does not depend on \(P\).

## 3. Cyclic groups

Let \(H=\langle g\rangle\) be cyclic of prime order \(\ell\), and put \(N=1+g+\cdots+g^{\ell-1}\in\mathbb ZH\). The ring \(\mathbb ZH\) is commutative, and multiplication by an element of it is \(\mathbb ZH\)-linear.

**Lemma 3.1** (the periodic resolution). The sequence
\[
\begin{aligned}&\cdots\xrightarrow{\,N\,}\mathbb ZH\xrightarrow{\,g-1\,}\mathbb ZH\xrightarrow{\,N\,}\mathbb ZH\\&\qquad\xrightarrow{\,g-1\,}\mathbb ZH\xrightarrow{\ \varepsilon\ }\mathbb Z\to0,\end{aligned}
\]
with multiplication maps alternating between \(g-1\) and \(N\), and the augmentation \(\varepsilon(\sum_iy_ig^i)=\sum_iy_i\), is a free resolution of \(\mathbb Z\).

*Proof.* Write \(y=\sum_{i=0}^{\ell-1}y_ig^i\), indices modulo \(\ell\). Then \((g-1)y=\sum_i(y_{i-1}-y_i)g^i\), which vanishes exactly when all \(y_i\) are equal, that is, when \(y\in\mathbb ZN\); and \(Ny=\varepsilon(y)N\), which vanishes exactly when \(\varepsilon(y)=0\). The image of \(N\) is \(\mathbb ZN\). The image of \(g-1\) is the set of \(z=\sum_iz_ig^i\) with \(\sum_iz_i=0\): such elements have \(\varepsilon(z)=0\), and conversely, for \(\sum_iz_i=0\) the equations \(y_{i-1}-y_i=z_i\) are solved by \(y_0=0\), \(y_i=y_{i-1}-z_i\), consistently around the cycle. So the kernel of each map is the image of the next, \(\ker\varepsilon\) is the image of \(g-1\), and \(\varepsilon\) is onto. \(\square\)

**Corollary 3.2.** Let \(\mathbb F_\ell\) carry the trivial action of \(H\). Then \(H^k(H;\mathbb F_\ell)\cong\mathbb F_\ell\) for every \(k\ge0\).

*Proof.* \(\mathrm{Hom}_{\mathbb ZH}(\mathbb ZH,\mathbb F_\ell)\cong\mathbb F_\ell\) by \(\varphi\mapsto\varphi(1)\). Under this identification, the map induced by multiplication by \(x\in\mathbb ZH\) is multiplication by \(\varepsilon(x)\), since \(\varphi(x)=x\varphi(1)=\varepsilon(x)\varphi(1)\) for the trivial action. Now \(\varepsilon(g-1)=0\) and \(\varepsilon(N)=\ell=0\) in \(\mathbb F_\ell\). So the cochain complex of the periodic resolution has \(\mathbb F_\ell\) in every degree and zero coboundaries. \(\square\)

## 4. Torsion-freeness

**Theorem 4.1** (torsion-freeness; [OpenAI-KZ, Corollary 5.3]). The group \(G\) is torsion-free.

*Proof.* Suppose \(g\in G\) has finite order \(m>1\). For a prime \(\ell\) dividing \(m\), the element \(g^{m/\ell}\) has order \(\ell\); call it \(g\) again, and let \(H=\langle g\rangle\). The group \(G\) is the disjoint union of right cosets \(H\gamma_j\), so \(\mathbb ZG=\bigoplus_j\mathbb ZH\gamma_j\), and each summand is isomorphic to \(\mathbb ZH\) by \(x\mapsto x\gamma_j\); thus \(\mathbb ZG\) is a free \(\mathbb ZH\)-module. The resolution of Lemma 1.2, viewed over \(\mathbb ZH\), is therefore a free resolution \(C\) of \(\mathbb Z\) with \(C_3=0\), and \(\mathrm{Hom}_{\mathbb ZH}(C_3,\mathbb F_\ell)=0\) gives \(H^3(\mathrm{Hom}_{\mathbb ZH}(C,\mathbb F_\ell))=0\). By Corollary 2.2 and Corollary 3.2 the same group is isomorphic to \(H^3(H;\mathbb F_\ell)\cong\mathbb F_\ell\ne0\). This contradiction proves the theorem. \(\square\)

The argument shows more generally that a group with a finite-dimensional classifying space is torsion-free: the cellular chains of the universal cover give a free resolution of finite length.

## 5. The zero divisors

**Lemma 5.1** (finite presentation). Choose one letter from each pair \(\{t,\bar t\}\). The group \(G\) is generated by the \(8258\) elements \(\varphi(t)\) of the chosen letters, with defining relators the labels of the closed paths \(c_e\) of the proof of Lemma 3.3 of [Cone pictures and asphericity](cone-pictures-and-asphericity.md), one for every component of \(\Gamma\) and every edge outside its spanning tree. In particular \(G\) is finitely presented.

*Proof.* The proof of that lemma constructs a homotopy equivalence \(\Phi\colon X\to X'\) that is the identity on the rose \(F\), together with a homotopy inverse and homotopies relative to \(F\); so \(\Phi\) induces an isomorphism \(\pi_1(X,o)\to\pi_1(X',o)\) that is the identity on the classes of the loops of \(F\). By (PI1 1), applied to \(F\) with the tree \(\{o\}\), \(\pi_1(F,o)\) is free on the loops of the chosen letters. The complex \(X'\) is \(F\) with disks attached along the loops \(\lambda\circ c_e\), so by (PI1 2) \(\pi_1(X',o)\) is the quotient of this free group by the normal subgroup generated by the labels of the \(c_e\). There are finitely many letters, components and edges. \(\square\)

**Proof of Theorem 4.1 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md).** For all large multiples \(n\) of \(2v^2\), Proposition 3.1 of [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md) gives a graph \(\Gamma\) as above. Let \(X\) be its cone complex and \(G=\pi_1(X,o)\). By Lemma 5.1, \(G\) is finitely presented; by Proposition 1.1, \(X\) is a finite two-dimensional classifying space for \(G\); by Theorem 4.1, \(G\) is torsion-free.

Let \(\Lambda_A\) and \(\Lambda_B\) be the components of \(\Gamma\) containing \(x_A\) and \(x_B\), with vertex sets \(A'\) and \(B'\). They are connected immersed labelled graphs over \(T\), and the outgoing letters of a vertex in its component are its type \(S_x\), since all edges at a vertex lie in its component. We check the hypotheses of Proposition 3.2 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md), with \(\varphi\colon T\to G\) as in Section 1 of [Cone pictures and asphericity](cone-pictures-and-asphericity.md):

- every closed path in \(\Lambda_A\) or \(\Lambda_B\) has label \(1\), by Lemma 1.1 of [Cone pictures and asphericity](cone-pictures-and-asphericity.md);
- \(\#(S_x\cap S_y)\) is odd for all \(x\in A'\) and \(y\in B'\), by Lemma 2.1(2) of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md);
- \(g_x\ne1\) for \(x\ne x_A\) and \(h_y\ne1\) for \(y\ne x_B\), by Proposition 6.1 of [Cone pictures and asphericity](cone-pictures-and-asphericity.md).

So \(\alpha=\sum_{x\in A'}g_x\) and \(\beta=\sum_{y\in B'}h_y^{-1}\) are nonzero elements of \(\mathbb F_2[G]\) with \(\alpha\beta=0\). \(\square\)

By Proposition 2.2 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md), the group \(G\) does not have the unique-product property. The proof is probabilistic: it shows that suitable matchings exist for all large \(n\), without exhibiting matchings from which a presentation and the zero divisors could be written down. The supports of \(\alpha\) and \(\beta\) are the labels of the vertices of two components of \(\Gamma\).

*What the course assumes.* Besides earlier lessons of the programme, the proof uses the standard facts (SURF) of [Spherical arrangements and planar intervals](spherical-arrangements-and-planar-intervals.md), the planar separator theorem (SEP) of [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md), and (PI1), (COV), (CELL) and (PL) of [Cone pictures and asphericity](cone-pictures-and-asphericity.md), with exact statements and locators in those lessons. Everything else is proved in the ten lessons of the course.

## 6. Exercises

**6.1.** Compute \(H^k(H;\mathbb Z)\) for \(H\) cyclic of prime order \(\ell\) from the periodic resolution.

**6.2.** Let \(G=\mathbb Z\), with the circle as classifying space and the real line as universal cover. Write down the cellular resolution of Lemma 1.2 over \(\mathbb ZG=\mathbb Z[z,z^{-1}]\).

**6.3.** Show that the relators of Lemma 5.1 number \(E-V+c\), where \(E,V,c\) are the numbers of edges, vertices and components of \(\Gamma\).

**6.4.** In the proof of Lemma 2.1, where is it used that the modules \(P_k\) are free, and where that \(C\) is exact?

**6.5.** Let \(H\ne1\) be a finite group. Show that \(\mathbb Z\) has no free resolution of finite length over \(\mathbb ZH\).

## 7. Solutions

**6.1.** \(\mathrm{Hom}_{\mathbb ZH}(\mathbb ZH,\mathbb Z)\cong\mathbb Z\), with the maps induced by \(g-1\) and \(N\) being multiplication by \(0\) and by \(\ell\). The cochain complex is \(\mathbb Z\xrightarrow0\mathbb Z\xrightarrow\ell\mathbb Z\xrightarrow0\mathbb Z\xrightarrow\ell\cdots\). So \(H^0=\mathbb Z\), \(H^k=0\) for odd \(k\), and \(H^k=\mathbb Z/\ell\) for even \(k\ge2\).

**6.2.** The line has vertices \(z^i\) and edges from \(z^i\) to \(z^{i+1}\); the deck group acts by translation. Both \(C_0\) and \(C_1\) are free of rank one, and the boundary of the chosen edge is \(z-1\) times the chosen vertex: \(0\to\mathbb ZG\xrightarrow{z-1}\mathbb ZG\xrightarrow\varepsilon\mathbb Z\to0\).

**6.3.** For a component with \(V_\Lambda\) vertices and \(E_\Lambda\) edges, a spanning tree has \(V_\Lambda-1\) edges, so \(E_\Lambda-V_\Lambda+1\) edges lie outside it. Summing over the \(c\) components gives \(E-V+c\).

**6.4.** Freeness of \(P_k\) allows defining \(\alpha_k\) and \(s_k\) by choosing values on a basis. Exactness of \(C\) provides the preimages under \(d\) (and the surjectivity of \(\varepsilon\colon C_0\to M\)) in each inductive step.

**6.5.** Take \(h\in H\) with \(h\ne1\); it has finite order \(m>1\). For a prime \(\ell\) dividing \(m\), the element \(h^{m/\ell}\) generates a subgroup \(K\) of order \(\ell\). As in the proof of Theorem 4.1, \(\mathbb ZH\) is a free \(\mathbb ZK\)-module, so a free resolution of \(\mathbb Z\) over \(\mathbb ZH\) of length \(d\) is also one over \(\mathbb ZK\), and it gives \(H^{d+1}(K;\mathbb F_\ell)=0\). This contradicts Corollary 3.2.

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
