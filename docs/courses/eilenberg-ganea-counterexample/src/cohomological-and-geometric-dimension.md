# Cohomological and geometric dimension

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A group has two natural dimensions. Its cohomological dimension is the length of the shortest projective resolution of the integers over its group ring; its geometric dimension is the least dimension of a classifying space, a CW complex with the group as fundamental group and contractible universal cover. The cellular chains of a classifying space give a resolution, so the first dimension never exceeds the second. Eilenberg and Ganea proved in 1957 that the two agree when the cohomological dimension is at least three, and Stallings and Swan proved that groups of cohomological dimension one are free. Whether every group of cohomological dimension two has a two-dimensional classifying space remained open. OpenAI answered this question negatively in 2026 [OpenAI-EG]: there is a finitely generated residually finite group of cohomological dimension two and geometric dimension three. This course proves the theorem. This lesson defines the two dimensions, proves the comparison theorem for projective resolutions and the inequality between the dimensions, computes the dimension of the plane group \(\mathbb Z^2\), and lays out the proof.

- Projective resolutions and cohomological dimension (Section 1).
- Classifying spaces and geometric dimension (Section 2).
- Subgroups and the plane group (Section 3).
- The Eilenberg–Ganea problem and the theorem (Section 4).

Groups act on modules from the left. For a group \(G\), the group ring \(\mathbb ZG\) consists of the finite integer combinations of elements of \(G\), as in Section 1 of [Group algebras and zero divisors](course:torsion-free-group-algebra-with-zero-divisors/group-algebras-and-zero-divisors) with coefficients in \(\mathbb Z\), and the *trivial module* \(\mathbb Z\) is the integers with every group element acting as the identity. The *augmentation* \(\varepsilon\colon\mathbb ZG\to\mathbb Z\) sends \(\sum_gn_gg\) to \(\sum_gn_g\).

## 1. Projective resolutions and cohomological dimension

Let \(R\) be a ring. A module is *free* if it has a basis, and *projective* if it is a direct summand of a free module.

**Lemma 1.1** (lifting). Let \(P\) be a projective module, \(\pi\colon M\to N\) a surjective homomorphism and \(\varphi\colon P\to N\) a homomorphism. There is a homomorphism \(\tilde\varphi\colon P\to M\) with \(\pi\tilde\varphi=\varphi\).

*Proof.* Let \(P\oplus Q=F\) with \(F\) free on a basis \((b_i)\), and extend \(\varphi\) by \(0\) on \(Q\) to \(\Phi\colon F\to N\). Choose \(m_i\in M\) with \(\pi(m_i)=\Phi(b_i)\), let \(\tilde\Phi\colon F\to M\) send \(b_i\) to \(m_i\), and restrict \(\tilde\Phi\) to \(P\). \(\square\)

An *augmented complex* over a module \(M\), a *chain map over* \(\mathrm{id}_M\) and *chain homotopic* chain maps are defined as in Section 2 of [Torsion-freeness and the zero divisors](course:torsion-free-group-algebra-with-zero-divisors/torsion-freeness-and-the-zero-divisors). A *projective resolution* of \(M\) is an exact augmented complex \(\cdots\to P_1\to P_0\to M\to0\) with all \(P_k\) projective; it has *length* \(n\) if \(P_k=0\) for \(k>n\).

**Lemma 1.2** (comparison). Let \(P\) be an augmented complex over \(M\) with all \(P_k\) projective, and \(C\) an exact augmented complex over \(M\). There is a chain map \(P\to C\) over \(\mathrm{id}_M\), and any two such chain maps are chain homotopic.

*Proof.* This is the proof of Lemma 2.1 of [Torsion-freeness and the zero divisors](course:torsion-free-group-algebra-with-zero-divisors/torsion-freeness-and-the-zero-divisors), with Lemma 1.1 in place of the choice of values on a basis. *Existence:* \(\varepsilon\colon C_0\to M\) is onto, so Lemma 1.1 lifts \(\varepsilon\colon P_0\to M\) to \(\alpha_0\colon P_0\to C_0\). If \(\alpha_0,\ldots,\alpha_k\) are constructed, \(\alpha_kd\) maps \(P_{k+1}\) into the kernel of \(C_k\to C_{k-1}\) (into \(\ker\varepsilon\) if \(k=0\)), which is the image of \(d\colon C_{k+1}\to C_k\); Lemma 1.1, applied to the surjection of \(C_{k+1}\) onto this image, gives \(\alpha_{k+1}\) with \(d\alpha_{k+1}=\alpha_kd\). *Homotopy:* for \(\beta=\alpha-\alpha'\), the map \(\beta_0\) has image in \(\ker\varepsilon=dC_1\), and lifting gives \(s_0\) with \(ds_0=\beta_0\). If \(s_0,\ldots,s_k\) are constructed with \(\beta_j=ds_j+s_{j-1}d\), then \(d(\beta_{k+1}-s_kd)=\beta_kd-ds_kd=s_{k-1}dd=0\), so \(\beta_{k+1}-s_kd\) maps into \(dC_{k+2}\), and lifting gives \(s_{k+1}\). \(\square\)

For a module \(A\) and a projective resolution \(P\) of \(M\), let \(H^k(\mathrm{Hom}_R(P,A))\) be the cohomology of the cochain complex \(\mathrm{Hom}_R(P_0,A)\to\mathrm{Hom}_R(P_1,A)\to\cdots\).

**Corollary 1.3** (independence of the resolution). For two projective resolutions \(P,C\) of \(M\) and every module \(A\), the groups \(H^k(\mathrm{Hom}_R(P,A))\) and \(H^k(\mathrm{Hom}_R(C,A))\) are isomorphic for every \(k\).

*Proof.* As in Corollary 2.2 of [Torsion-freeness and the zero divisors](course:torsion-free-group-algebra-with-zero-divisors/torsion-freeness-and-the-zero-divisors): chain maps \(P\to C\to P\) and \(C\to P\to C\) over \(\mathrm{id}_M\) exist by Lemma 1.2 and are chain homotopic to the identities, and chain homotopies induce equal maps on cohomology. \(\square\)

**Definition 1.4.** For a group \(G\) and a \(\mathbb ZG\)-module \(A\), the *cohomology* \(H^k(G;A)\) is \(H^k(\mathrm{Hom}_{\mathbb ZG}(P,A))\) for any projective resolution \(P\) of the trivial module \(\mathbb Z\). The *cohomological dimension* \(\operatorname{cd}G\) is the least \(n\) such that \(\mathbb Z\) has a projective resolution of length \(n\) over \(\mathbb ZG\), or \(\infty\) if there is none.

Every module is a quotient of a free module, so projective resolutions exist; by Corollary 1.3, \(H^k(G;A)\) is well defined up to isomorphism.

**Lemma 1.5** (a lower bound). If \(H^n(G;A)\ne0\) for some \(\mathbb ZG\)-module \(A\), then \(\operatorname{cd}G\ge n\).

*Proof.* A projective resolution \(P\) of length less than \(n\) has \(P_n=0\), so \(H^n(\mathrm{Hom}_{\mathbb ZG}(P,A))=0\), and \(H^n(G;A)=0\) by Corollary 1.3. \(\square\)

## 2. Classifying spaces and geometric dimension

**Definition 2.1.** A *classifying space* for a group \(G\) is a connected CW complex \(Y\) with \(\pi_1(Y)\cong G\) and contractible universal cover. The *geometric dimension* \(\operatorname{gd}G\) is the least dimension of a classifying space for \(G\), or \(\infty\) if there is none.

We use the following standard facts of covering space theory and cellular homology without proof; they extend the statements (COV) and (CELL) of [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity) to CW complexes of any dimension, and a course proving them is recorded as an open obligation of this course.

**(CW)** (covering spaces and cellular chains; [Hatcher, Section 1.3, Propositions 1.33, 1.34, 1.39 and 4.1, Lemma 2.34 and Theorem 2.35]). Let \(Y\) be a connected CW complex with fundamental group \(G\) and universal cover \(\widetilde Y\).

1. \(\widetilde Y\) is a CW complex whose cells are the lifts of the cells of \(Y\). The group \(G\) acts on \(\widetilde Y\) by deck transformations, homeomorphisms commuting with the covering map, which permute the lifts of every cell freely and transitively and act on cellular chains by chain maps.
2. The singular homology of a CW complex is the homology of its cellular chain complex, and with the augmentation sending every vertex to \(1\) the augmented cellular chain complex computes reduced homology.

**Lemma 2.2** (\(\operatorname{cd}\le\operatorname{gd}\)). If \(Y\) is a classifying space for \(G\) of dimension \(n\), the augmented cellular chain complex of \(\widetilde Y\) is a free resolution of \(\mathbb Z\) over \(\mathbb ZG\) of length \(n\). In particular \(\operatorname{cd}G\le\operatorname{gd}G\).

*Proof.* Orient every cell of \(Y\) and each of its lifts compatibly. By (CW 1), \(G\) permutes the oriented \(k\)-cells of \(\widetilde Y\) freely, with one orbit for each \(k\)-cell of \(Y\), so the cellular chain group \(C_k(\widetilde Y)\) is a free \(\mathbb ZG\)-module with basis one chosen lift of each \(k\)-cell, and the boundary maps and the augmentation are \(\mathbb ZG\)-linear. The space \(\widetilde Y\) is contractible, so its reduced singular homology vanishes, by the homotopy invariance of singular homology [Fomberg, Theorem 1.13 and Corollary 1.14] in the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60). By (CW 2) the augmented cellular chain complex is exact. It has no terms above degree \(n\). \(\square\)

The same argument shows more generally: if \(G\) acts freely on an acyclic CW complex \(X\) of dimension \(n\), permuting its cells, then the augmented cellular chains of \(X\) form a free resolution of \(\mathbb Z\) of length \(n\), so \(\operatorname{cd}G\le n\). *Acyclic* means that the reduced integral homology vanishes; the complex need not be contractible, and the action need not give a classifying space.

A connected graph with fundamental group \(G\) and a tree as universal cover is a classifying space of dimension one; the circle is one for \(\mathbb Z\), with universal cover the real line.

## 3. Subgroups and the plane group

**Lemma 3.1** (subgroups). If \(H\) is a subgroup of \(G\), then \(\operatorname{cd}H\le\operatorname{cd}G\).

*Proof.* \(G\) is the disjoint union of right cosets \(H\gamma_j\), so \(\mathbb ZG=\bigoplus_j\mathbb ZH\gamma_j\) is a free \(\mathbb ZH\)-module. Hence every free \(\mathbb ZG\)-module is free over \(\mathbb ZH\), and every projective \(\mathbb ZG\)-module, a direct summand of a free one, is projective over \(\mathbb ZH\). A projective resolution of \(\mathbb Z\) over \(\mathbb ZG\) of length \(n\) is therefore one over \(\mathbb ZH\). \(\square\)

Write the group \(\mathbb Z^2\) multiplicatively, generated by commuting elements \(x,y\). Its group ring is the ring \(R=\mathbb Z[x^{\pm1},y^{\pm1}]\) of Laurent polynomials, a commutative domain, and the augmentation is \(f\mapsto f(1,1)\).

**Lemma 3.2** (the plane group). The sequence
\[
\begin{aligned}
0\to R&\xrightarrow{\ d_2\ }R^2\xrightarrow{\ d_1\ }R\\
&\xrightarrow{\ \varepsilon\ }\mathbb Z\to0,
\end{aligned}\tag{3.1}
\]
with \(d_1(a,b)=(x-1)a+(y-1)b\) and \(d_2(r)=\bigl((y-1)r,\,-(x-1)r\bigr)\), is a free resolution of \(\mathbb Z\), and \(H^2(\mathbb Z^2;\mathbb Z)\cong\mathbb Z\). Hence \(\operatorname{cd}\mathbb Z^2=2\).

*Proof.* Clearly \(d_1d_2=0\) and \(\varepsilon d_1=0\), and \(\varepsilon\) is onto. *Exactness at \(R\).* For a monomial, \(x^ay^b-1=(x^a-1)y^b+(y^b-1)\), and \(x^a-1\) is a multiple of \(x-1\) for every integer \(a\), since \(x^{-1}-1=-x^{-1}(x-1)\); the same holds for \(y\). So \(f-f(1,1)\) lies in the ideal generated by \(x-1\) and \(y-1\), and \(\ker\varepsilon=\operatorname{im}d_1\). *Exactness at \(R^2\).* Let \((x-1)a=-(y-1)b\). Substituting \(y=1\), a ring homomorphism to the domain \(\mathbb Z[x^{\pm1}]\), gives \((x-1)a(x,1)=0\), so \(a(x,1)=0\). By the computation for monomials in the exactness at \(R\), \(a(x,y)-a(x,1)\) is a multiple of \(y-1\), so \(a=(y-1)r\) for some \(r\in R\). Then \((y-1)\bigl((x-1)r+b\bigr)=0\), and \(b=-(x-1)r\), since \(R\) is a domain: \((a,b)=d_2(r)\). *Exactness at the left.* \(d_2\) is injective, since \(R\) is a domain.

Apply \(\mathrm{Hom}_R(-,\mathbb Z)\). Since \(\mathrm{Hom}_R(R,\mathbb Z)\cong\mathbb Z\) by \(\varphi\mapsto\varphi(1)\), and \(\varphi(z)=\varepsilon(z)\varphi(1)\) for the trivial module, the map induced by \(d_2\) sends \((\varphi_1,\varphi_2)\) to \(\varepsilon(y-1)\varphi_1-\varepsilon(x-1)\varphi_2=0\). So \(H^2(\mathbb Z^2;\mathbb Z)\cong\mathrm{Hom}_R(R,\mathbb Z)\cong\mathbb Z\ne0\), and \(\operatorname{cd}\mathbb Z^2\ge2\) by Lemma 1.5; the resolution (3.1) gives \(\operatorname{cd}\mathbb Z^2\le2\). \(\square\)

**Corollary 3.3.** A group containing a subgroup isomorphic to \(\mathbb Z^2\) has cohomological dimension at least \(2\).

## 4. The Eilenberg–Ganea problem and the theorem

By Lemma 2.2, \(\operatorname{cd}G\le\operatorname{gd}G\). Eilenberg and Ganea proved in 1957 that equality holds when \(\operatorname{cd}G\ge3\), and that \(\operatorname{gd}G\le3\) when \(\operatorname{cd}G=2\); Stallings, for finitely generated groups, and Swan, in general, proved that a group of cohomological dimension one is free, so that its geometric dimension is one as well [Davis, Theorems F.3.2 and F.3.3]. These theorems are background and are not used in this course. The *Eilenberg–Ganea problem* asks whether some group has cohomological dimension two and geometric dimension three [Davis, Section 8.5 and Appendix F.3]; the *Eilenberg–Ganea conjecture* asserts that no such group exists.

A group is *residually finite* if every element other than the identity survives in some finite quotient. A simplicial complex is *flag* if every finite set of pairwise adjacent vertices spans a simplex. For a finite flag complex \(L\) with vertex set \(V\), the *right-angled Artin group* \(A_L\) has a generator \(a_q\) for each \(q\in V\), with \(a_q\) and \(a_r\) commuting whenever \(\{q,r\}\) is an edge of \(L\) and no other relations; the *height homomorphism* \(\lambda\colon A_L\to\mathbb Z\) sends every \(a_q\) to \(1\). A complex is *acyclic* if its reduced integral homology vanishes.

**Theorem 4.1** (OpenAI [OpenAI-EG, Theorem 1.1]). There is a finitely generated residually finite group \(G\) with
\[
\operatorname{cd}G=2,\qquad\operatorname{gd}G=3.
\]
One may take \(G\) to be the kernel of the height homomorphism of \(A_L\) for a finite acyclic flag triangulation \(L\) of the presentation complex of
\[
\begin{aligned}
\langle x,y\mid{}&x^2=y^5,\\
&x^2=(xy^{-1})^3\rangle .
\end{aligned}\tag{4.1}
\]
No two-dimensional classifying space for this group exists, with any number of cells. OpenAI's release contains a formalization of this statement in Lean [OpenAI-EG-Lean].

The group acts freely on a two-dimensional acyclic simplicial complex \(X\) with finitely many cell orbits, which gives \(\operatorname{cd}G\le2\) by the remark after Lemma 2.2, and a subgroup \(\mathbb Z^2\) gives \(\operatorname{cd}G\ge2\) by Corollary 3.3. It also acts freely on a contractible three-dimensional cube complex, which gives \(\operatorname{gd}G\le3\). The difficulty is the lower bound \(\operatorname{gd}G\ge3\): an acyclic complex need not be contractible, and showing that \(X\) is not contractible would not exclude a different two-dimensional classifying space. The proof compares the cycles of \(X\) with the relations of *any* hypothetical two-dimensional classifying space, through labels of the edges of \(X\) by unit quaternions:

1. If a two-dimensional classifying space existed, every labelling of the edges by unit quaternions close enough to \(1\) whose product around every triangle of \(X\) is \(1\) would have product \(1\) around every closed path.
2. For every \(\epsilon>0\) there is such a labelling within \(\epsilon\) of \(1\), with product \(1\) around every triangle but not around some closed path.

The first statement uses a degree argument for word maps on the group of unit quaternions, solved on finite quotients and passed to the group by compactness; the second pulls back a nontrivial representation of the fundamental group of \(L\) into the unit quaternions along slowly varying maps.

The lessons are:

1. This lesson.
2. [Word maps on unit quaternions and degree](word-maps-on-unit-quaternions-and-degree.md): unit quaternions, word maps, mapping degree on isolating open sets, and the nonvanishing of the degree on a conjugation-invariant part of a fibre.
3. [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md): from a two-dimensional classifying space to a presentation whose relators contain chosen boundary chains.
4. [Exact counts and a quadratic estimate](exact-counts-and-a-quadratic-estimate.md): signed counts of relators and the quadratic estimate for products of labels.
5. [Finite quotients and the comparison theorem](finite-quotients-and-the-comparison-theorem.md): solving finite systems of word equations by degree, compactness, and statement 1 above.
6. [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md).
7. [The cube complex and its universal cover](the-cube-complex-and-its-universal-cover.md): a contractible three-dimensional cube complex with a free action.
8. [The level complex and its acyclicity](the-level-complex-and-its-acyclicity.md): the height level \(X\), its acyclicity, and the cycle basis.
9. [An acyclic seed with quaternion monodromy](an-acyclic-seed-with-quaternion-monodromy.md): the complex \(L\) and a nontrivial representation of its fundamental group.
10. [Traces and direction vectors](traces-and-direction-vectors.md): normal forms in right-angled Artin groups and a slowly varying direction map.
11. [Small transport and the counterexample](small-transport-and-the-counterexample.md): statement 2 above and the proof of Theorem 4.1.

## 5. Exercises

**5.1.** Show that \(\operatorname{cd}\mathbb Z=1\), using the resolution \(0\to\mathbb Z[t^{\pm1}]\xrightarrow{t-1}\mathbb Z[t^{\pm1}]\to\mathbb Z\to0\) and \(H^1(\mathbb Z;\mathbb Z)\).

**5.2.** Show that a group with an element of finite order larger than one has infinite cohomological dimension.

**5.3.** Check the exactness of (3.1) at \(R^2\) for the element \(\bigl(y-1,-(x-1)\bigr)\), and find an element of \(\ker\varepsilon\) and its preimage under \(d_1\).

**5.4.** Show that \(\mathbb Z^3\) has cohomological dimension at least \(2\), and that a group containing \(\mathbb Z^3\) has cohomological dimension at least \(2\). (It is \(3\); the exercise asks only for what Corollary 3.3 gives.)

**5.5.** Let \(G\) act freely on an acyclic two-dimensional CW complex \(X\), permuting its cells. Explain why this proves \(\operatorname{cd}G\le2\) but not \(\operatorname{gd}G\le2\).

## 6. Solutions

**5.1.** \(t-1\) is injective on the domain \(\mathbb Z[t^{\pm1}]\), and \(\ker\varepsilon\) is generated by \(t-1\), as in the proof of Lemma 3.2; so the sequence is a free resolution of length one. Applying \(\mathrm{Hom}(-,\mathbb Z)\) gives \(\mathbb Z\xrightarrow{0}\mathbb Z\), since \(\varepsilon(t-1)=0\), so \(H^1(\mathbb Z;\mathbb Z)\cong\mathbb Z\ne0\) and \(\operatorname{cd}\mathbb Z\ge1\) by Lemma 1.5. Also \(\operatorname{cd}\mathbb Z\ge1\) because a resolution of length \(0\) would make \(\mathbb Z\) projective, and then \(H^1=0\).

**5.2.** A power of the element has prime order \(\ell\) and generates a cyclic subgroup \(H\). By Lemma 3.1, \(\operatorname{cd}H\le\operatorname{cd}G\). By Corollary 3.2 of [Torsion-freeness and the zero divisors](course:torsion-free-group-algebra-with-zero-divisors/torsion-freeness-and-the-zero-divisors), \(H^k(H;\mathbb F_\ell)\cong\mathbb F_\ell\) for every \(k\), so \(\operatorname{cd}H=\infty\) by Lemma 1.5.

**5.3.** \(d_1\bigl(y-1,-(x-1)\bigr)=(x-1)(y-1)-(y-1)(x-1)=0\), and the element is \(d_2(1)\). For example \(x^2y-1\in\ker\varepsilon\), and \(x^2y-1=(x^2-1)y+(y-1)=d_1\bigl((x+1)y,\,1\bigr)\).

**5.4.** \(\mathbb Z^3\) contains \(\mathbb Z^2\), so Corollary 3.3 applies to it and to every group containing it.

**5.5.** The augmented cellular chains of \(X\) form a free resolution of length two, by the remark after Lemma 2.2. A classifying space needs a contractible universal cover; \(X\) is acyclic, but need not be simply connected or contractible, and \(X/G\) need not have fundamental group \(G\).

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [OpenAI-EG-Lean] OpenAI, Lean formalization of the Eilenberg–Ganea counterexample, OpenAI Math Release, scope note `lean/docs/249.md`. https://github.com/openai/math/blob/main/lean/docs/249.md
- [Davis] M. W. Davis, *The Geometry and Topology of Coxeter Groups*, Princeton University Press, 2008; first edition on the author's page. https://people.math.osu.edu/davis.12/davisbook.pdf
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
