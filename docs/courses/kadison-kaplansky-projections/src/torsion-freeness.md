# Torsion-freeness

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group \(\Gamma\) defined by the voltage cover must be torsion-free, since the conjecture concerns torsion-free groups. The proof attaches to the Cayley graph a cone over every indexed copy. The resulting two-dimensional complex is acyclic, by the direct decomposition of the cycle space into the cycle spaces of the copies, and every finite cyclic subgroup of \(\Gamma\) would act freely on its cells, because the stabilizer of a copy embeds into the torsion-free group \(F\). A finite cyclic group of prime order cannot act freely on an acyclic complex of dimension two: the cellular chains would be a free resolution of length two, while the periodic resolution shows that the trivial module has nonzero homology in every degree [OpenAI-KK, Section 7.5].

- Stabilizers of copies (Section 1).
- The cone complex (Section 2).
- Free resolutions over a cyclic group (Section 3).
- The theorem (Section 4).

The setting of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md) and [Thin triangles, overlap balls and the residual forest](thin-triangles-overlap-balls-and-the-residual-forest.md) is in force.

## 1. Stabilizers of copies

**Lemma 1.1** (stabilizers; [OpenAI-KK, Lemma 7.12]). The stabilizer in \(\Gamma\) of an indexed copy embeds as a subgroup into \(F\). In particular it contains no element of finite order other than the identity.

*Proof.* Fix a representative \((C,\phi)\). An element \(h\) stabilizes the indexed copy when \((C,h\phi)\sim(C,\phi)\), that is, when there is \(a\in F\) with \(\delta_aC=C\) and \(h\phi=\phi\delta_a\) on \(C\). Such \(a\) is unique: \(\phi\) is injective, and the deck action is free on vertices. If \(h_1,h_2\) correspond to \(a_1,a_2\), then \(h_1h_2\phi=h_1\phi\delta_{a_2}=\phi\delta_{a_1}\delta_{a_2}=\phi\delta_{a_1a_2}\), so \(h\mapsto a\) is a homomorphism. If \(a=1_F\), then \(h\phi=\phi\), so \(h\) fixes a group vertex and \(h=1\). Hence the homomorphism is injective, and \(F\) is torsion-free. \(\square\)

The stabilizer need not be trivial: a deck transformation that preserves a component gives a nontrivial symmetry of its copy.

## 2. The cone complex

Let \(Z\) be the two-dimensional cell complex obtained from \(\widehat X\) by attaching, for every indexed copy \(Q\) and every positive edge \(e:s(e)\to t(e)\) of \(Q\), a triangle \(\tau_{Q,e}\) with boundary
\[
\begin{gathered}
\partial\tau_{Q,e}=e+\sigma_{Q,s(e)}\\
-\sigma_{Q,t(e)} ,
\end{gathered}\tag{2.1}
\]
where \(\sigma_{Q,x}\) is the spoke from \(c_Q\) to \(x\), oriented away from the center. Edges of different copies give different triangles, even when they are the same edge of \(X\). The one-skeleton of \(Z\) is \(\widehat X\).

**Lemma 2.1** (acyclicity; [OpenAI-KK, Lemma 7.13]). For every field \(k\), the augmented cellular chain complex of finitely supported chains
\[
\begin{gathered}
0\longrightarrow C_2(Z;k)\xrightarrow{\ \partial_2\ }C_1(Z;k)\\
\xrightarrow{\ \partial_1\ }C_0(Z;k)\xrightarrow{\ \varepsilon\ }k\longrightarrow0
\end{gathered}
\]
is exact.

*Proof.* \(\widehat X\) is connected, which gives exactness at \(C_0\) and at \(k\).

*At \(C_1\).* Let \(c\) be a finite one-cycle. For each center, the coefficients of the spokes of \(c\) at that center sum to zero, since \(\partial c\) vanishes at the center. A finite chain of vertices of the connected copy \(Q\) with coefficient sum zero is the boundary of a finite chain of edges of \(Q\): join each vertex of its support to a fixed one by a path. By (2.1), adding the boundaries of the corresponding triangles removes all spoke terms at \(c_Q\). The resulting cycle lies in \(X\). By Proposition 5.1 of the lesson on thin triangles it is a finite sum of cycles \(c_Q\) of copies, and each \(c_Q\) is the boundary of the same combination of triangles of \(Q\), since its spoke terms cancel. So \(c\) is a boundary.

*At \(C_2\).* A finite combination of triangles gives, for each copy, the edge chain \(c_Q\) of its coefficients. If its boundary vanishes, the spoke part at \(c_Q\) vanishes, which by (2.1) says \(\partial c_Q=0\); and the part in \(X\) is \(\sum_Qc_Q=0\). By the direct decomposition, every \(c_Q=0\), and so all coefficients vanish, since the triangles of \(Q\) correspond to its oriented edges. \(\square\)

## 3. Free resolutions over a cyclic group

Let \(p\) be a prime, \(k=\mathbb F_p\), \(C_p=\langle\gamma\rangle\) cyclic of order \(p\), and \(A=k[C_p]\). With \(z=\gamma-1\), \(A=k[z]/(z^p)\), since \(\gamma^p=1\) gives \(z^p=(\gamma-1)^p=\gamma^p-1=0\) in characteristic \(p\). The trivial module is \(k=A/(z)\). A *free resolution* of \(k\) is an exact sequence \(\cdots\to F_1\to F_0\to k\to0\) of free \(A\)-modules, possibly of infinite rank.

**Lemma 3.1** (the periodic resolution). The sequence
\[
\cdots\xrightarrow{\ z\ }A\xrightarrow{\ z^{p-1}\ }A\xrightarrow{\ z\ }A\longrightarrow k\longrightarrow0
\]
is a free resolution of \(k\). After applying \(k\otimes_A-\), all its differentials vanish, so the resulting complex has homology \(k\) in every degree \(n\ge0\).

*Proof.* In the basis \(1,z,\ldots,z^{p-1}\) of \(A\), the kernel of multiplication by \(z\) is spanned by \(z^{p-1}\), which is the image of multiplication by \(z^{p-1}\), and the kernel of multiplication by \(z^{p-1}\) is spanned by \(z,\ldots,z^{p-1}\), the image of multiplication by \(z\); the augmentation \(A\to k\) has kernel \((z)\). Since \(z\) acts by zero on \(k\), the maps \(k\otimes_Az\) and \(k\otimes_Az^{p-1}\) vanish. \(\square\)

**Lemma 3.2** (comparison). If \(F_\bullet\) and \(F'_\bullet\) are free resolutions of \(k\), the complexes \(k\otimes_AF_\bullet\) and \(k\otimes_AF'_\bullet\) have isomorphic homology in every degree.

*Proof.* Lift the identity of \(k\) to a chain map \(f:F_\bullet\to F'_\bullet\): send each basis element of \(F_0\) to a preimage of its augmentation, and inductively send each basis element \(e\) of \(F_n\) to a preimage under \(\partial'\) of \(f(\partial e)\), which is a cycle because \(\partial'f(\partial e)=f(\partial\partial e)=0\), and so a boundary by exactness. Construct \(g:F'_\bullet\to F_\bullet\) in the same way. The composite \(gf\) lifts the identity, and so does the identity map; their difference \(u\) is null-homotopic: on a basis element of \(F_0\), \(u\) has augmentation zero, so it is a boundary \(\partial h_0(e)\); inductively, \(u-h_{n-1}\partial\) is a cycle on each basis element of \(F_n\), hence equal to \(\partial h_n(e)\) for some \(h_n(e)\). Extending linearly gives \(u=\partial h+h\partial\). Tensoring with \(k\) preserves chain maps and homotopies, so \(gf\) and \(fg\) induce the identity on homology. \(\square\)

## 4. The theorem

**Proposition 4.1** (torsion-freeness; [OpenAI-KK, Proposition 7.14]). The group \(\Gamma\) is finitely generated and torsion-free.

*Proof.* It is generated by the finite set \(S\). Suppose it has an element of finite order other than \(1\); a power of it generates a subgroup \(C_p\) of prime order \(p\). Left translation acts on \(Z\) by cellular maps, and \(C_p\) acts freely on the cells. A nontrivial element cannot fix a group vertex. If it fixed a formal edge \((h,\sigma)\), it would fix its initial vertex \(h\), since left translation preserves positive orientations. If it fixed a center, a spoke or a triangle, it would stabilize the corresponding indexed copy, which Lemma 1.1 excludes for an element of finite order.

Over \(k=\mathbb F_p\), choose orientations and one representative in every \(C_p\)-orbit of cells. Since the action on cells is free, each \(C_j(Z;k)\) is a free \(A=k[C_p]\)-module with these representatives as a basis. By Lemma 2.1, \(C_\bullet(Z;k)\) is then a free resolution of \(k\) of length two, so \(k\otimes_AC_\bullet(Z;k)\) has zero homology in degrees greater than two. By Lemmas 3.1 and 3.2, this homology is \(k\) in every degree, a contradiction. \(\square\)

With Proposition 7.1 of the lesson on voltage covers, Propositions 4.1 and 5.2 of the lesson on thin triangles, and Proposition 4.1 here, the geometric conclusion, Theorem 3.1 of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md), is proved, under the girth condition (2.1) there.

## 5. Exercises

**5.1** (easy). Compute the kernel and the image of multiplication by \(z\) on \(A=\mathbb F_2[z]/(z^2)\), and check exactness of the periodic resolution for \(p=2\).

**5.2** (medium). Let \(\mathbb Z/2\) act on the circle by the antipodal map, with the cell structure of two vertices and two edges exchanged by the action. Write the cellular chain complex over \(\mathbb F_2\) as a complex of free \(\mathbb F_2[\mathbb Z/2]\)-modules, and show that it is not a resolution of \(\mathbb F_2\).

**5.3** (medium). Why must the triangles of different copies over the same edge of \(X\) be distinct cells for Lemma 2.1? Give the consequence at \(C_2\) if they were identified.

**5.4** (medium). The infinite dihedral group \(\langle a,b\mid a^2,b^2\rangle\) acts on the real line, \(a\) by \(t\mapsto-t\) and \(b\) by \(t\mapsto1-t\), with vertices at the integers and edges \([n,n+1]\). Show that this cell complex is acyclic, and find a cell mapped to itself by \(a\) and one mapped to itself by \(b\).

## 6. Solutions

**5.1.** On \(\mathbb F_2[z]/(z^2)\) with basis \(1,z\), multiplication by \(z\) sends \(1\mapsto z\), \(z\mapsto0\): its kernel and image are both spanned by \(z\). For \(p=2\), \(z^{p-1}=z\), so the resolution is \(\cdots\xrightarrow zA\xrightarrow zA\to k\to0\), exact at every \(A\) since kernel equals image, and at \(A\to k\) since the kernel of the augmentation is \((z)\).

**5.2.** Both chain groups are free of rank one, \(C_1=A\,e\) and \(C_0=A\,v\), with \(\partial e=\gamma v-v=zv\). The homology in degree one is the kernel of multiplication by \(z\), spanned by \(z e\), which is nonzero; the circle is not acyclic, so this is a free complex of length one that is not a resolution.

**5.3.** If triangles over the same edge of \(X\) were identified, the boundary formula (2.1) could not hold for each copy separately, and an edge chain shared by two copies would be the boundary of one cell with spokes to two centers; the injectivity argument at \(C_2\), which reads off \(\partial c_Q=0\) copy by copy, would fail.

**5.4.** The line is a tree, so its finitely supported chains are acyclic, as in Lemma 2.1 with no triangles. The reflection \(a\) fixes the vertex \(0\), and \(b\) maps the edge \([0,1]\) to itself, reversing it. By Lemmas 3.1 and 3.2, a group of order two cannot act freely on the cells of an acyclic complex of finite dimension; in the cone complex of this lesson, fixed cells are excluded by Lemma 1.1, and this is why \(\Gamma\) has no torsion.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 7.5, Lemmas 7.12 and 7.13, Proposition 7.14. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
