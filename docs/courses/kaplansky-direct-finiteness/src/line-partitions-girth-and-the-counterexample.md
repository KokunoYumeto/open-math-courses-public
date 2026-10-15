# Line partitions, girth and the counterexample

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

With the holes and the random slabs fixed, each slab is partitioned into lines, the line through its hole being the axis in the direction \(d_j\). The local trades of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md) then remove every line through a hole and keep every other degree equal to \(D\). Every short cycle of the resulting incidence graph would be one of the polygons excluded in [Random slabs and the local lemma](random-slabs-and-the-local-lemma.md), so the girth is at least \(12\). This proves the theorem on line systems. A finite search then fixes the field, the incidence data, the vectors, the group and the two elements, and the criterion of the earlier lessons gives Kaplansky's counterexample, a nonsurjunctive automaton and a nonsofic group.

- Partitions of a slab (Section 1).
- Trades and the girth (Section 2).
- A terminating prescription (Section 3).
- The counterexample and its consequences (Section 4).
- Remarks on the construction (Section 5).

## 1. Partitions of a slab

**Lemma 1.1** (slab partitions; [OpenAI-DF2, Lemma 5.8]). Let \(\Sigma\) be a three-dimensional affine space with direction space \(P\oplus d\), where \(\dim_QP=2\) and \(\dim_Qd=1\). Then \(\Sigma\) has a partition into lines whose directions project to nonzero vectors of \(P\). For every point \(o\in\Sigma\), \(\Sigma\) also has a partition into lines that contains \(o+d\) and whose other lines have directions projecting to nonzero vectors of \(P\).

*Proof.* For the first statement use the lines parallel to a fixed direction of \(P\). For the second, choose \(0\ne\delta\in d\) and identify \(P\) with a field \(Q_2\) of \(q^2\) elements containing \(Q\) (it exists by [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40): Judson, Theorems 22.6 and 22.7). Let \(J:P\to P\) be multiplication by an element \(\eta\in Q_2\setminus Q\). Then \(J\) has no eigenvector over \(Q\): \(\eta x=\lambda x\) with \(x\ne0\) and \(\lambda\in Q\) forces \(\eta=\lambda\). So for every \(x\ne0\) the vectors \(x\) and \(Jx\) form a basis of \(P\). Besides \(o+d\), take the sets
\[
\begin{aligned}
\Lambda_\gamma=\{&o+x+\gamma(Jx)\,\delta:\\
&x\in P,\ \gamma(x)=1\},
\end{aligned}
\]
one for each nonzero \(Q\)-linear form \(\gamma:P\to Q\). The set \(\{x:\gamma(x)=1\}\) is an affine line in \(P\), and \(x\mapsto o+x+\gamma(Jx)\delta\) is injective and affine, so \(\Lambda_\gamma\) is an affine line whose direction projects onto the line \(\ker\gamma\) of \(P\). A point of \(\Sigma\) off \(o+d\) has the form \(o+x+c\delta\) with \(x\ne0\) and \(c\in Q\); since \(x,Jx\) is a basis, there is exactly one linear form \(\gamma\) with \(\gamma(x)=1\) and \(\gamma(Jx)=c\), and it is nonzero. So the \(q^2-1\) lines \(\Lambda_\gamma\) partition the \(q^3-q\) points off \(o+d\), and \(o+d\) contains the other \(q\). \(\square\)

Choose the slab subspaces \(P_{j,C}\) as in Corollary 5.2 of the previous lesson, so that every slab contains at most one hole and no candidate polygon event occurs. For each index \(j\), apply Lemma 1.1 in every slab of every coset of \(U_j\), with the hole of the slab as the designated point when there is one. This gives the *preliminary partition* of \(\mathcal A\) with label \(G_j\). Its line through a hole \(o\) is the *axis* \(o+d_j\), and the axes are its only lines whose directions have zero \(E_j\)-component; every other line of a slab in the coset \(C\) has a direction with nonzero \(E_j\)-component in \(P_{j,C}\).

## 2. Trades and the girth

**Lemma 2.1** (the trades; [OpenAI-DF2, Lemma 5.9]). For every hole \(o\) and every bundle \(r\), remove the \(q\) axes \(o+d_j\), \(\rho(j)=r\), and insert the \(q-1\) replacement lines of label \(R_r\) in \(o+W_r\). Let \(\mathcal F\) be the resulting family of lines. Then every line of \(\mathcal F\) lies in \(V=\mathcal A\setminus O\), every point of \(V\) lies on exactly \(D\) lines of \(\mathcal F\), the lines of \(\mathcal F\) with one label are pairwise disjoint, and lines with different labels are different lines.

*Proof.* No line is removed twice: an axis \(o+d_j\) is removed only for the hole \(o\) and the bundle \(\rho(j)\), and two holes on one axis of partition \(j\) would lie in one slab, which was excluded. Lines of different preliminary partitions have directions in different spaces \(U_j\), which meet only in \(0\) (Lemma 2.2 of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md)), so they are different lines; replacement lines have directions \(e_r\), which meet the \(U_j\) and each other only in \(0\); replacement lines of one label are distinct and disjoint by Lemma 4.2 there. So the removals and insertions are of distinct lines, and their effects on the degrees add.

Initially every point lies on exactly one line of each of the \(D\) preliminary partitions. By Lemma 3.1 there, each trade leaves the degree of every point other than its hole unchanged, and the hole \(o\) loses the \(q\) axes of the bundle. A hole lies on no axis of another hole and on no replacement line, so after the \(D/q\) trades of \(o\) it lies on no line, while every point of \(V\) still lies on \(D\) lines. Every preliminary line through a hole is an axis and was removed, and the replacement lines miss \(O\), so every line of \(\mathcal F\) lies in \(V\). Disjointness within a label is inherited from the partition or from Lemma 4.2. \(\square\)

*Proof of Theorem 1.1 of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md).* The holes come from Lemma 4.1 there, the slabs from Corollary 5.2 of [Random slabs and the local lemma](random-slabs-and-the-local-lemma.md), and \(\mathcal F\) from Lemma 2.1; the size and degree statements are proved. Suppose the incidence graph had a cycle of length \(2k<12\). Two distinct lines share at most one point, so \(k\ge3\), and the cycle is a polygon \(x_0,x_1,\ldots,x_k=x_0\) of distinct points with consecutive points on distinct lines of \(\mathcal F\) and \(k\in\{3,4,5\}\). Label each step by the label of its line. Consecutive lines have different labels, since lines of one label are disjoint while consecutive lines of the polygon meet.

If some step is generic, the polygon is a candidate polygon: a step on a line of partition \(j\) has its vector in \(U_j\) with nonzero \(E_j\)-component (the line is not an axis), and a step on a replacement line of label \(R_r\) has its vector in \(e_r\) and both endpoints in \(T_r\). Each generic step lies in a slab of its coset \(C\), so its \(E_j\)-component lies in \(P_{j,C}\), and the event of the polygon occurs, which was excluded. If all steps are replacement steps, the directions \(e_r\) that occur are independent, so closure forces each label to occur at least twice; as no label occurs at two adjacent positions, each occurs exactly twice, and the polygon is a rectangle with sides of directions \(e_r\), \(e_{r'}\), \(r\ne r'\), all on replacement lines. That is an exceptional rectangle, excluded by Lemma 4.2 of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md). So the girth is at least \(12\). \(\square\)

## 3. A terminating prescription

The existence proofs used random choices. To define one specific field, group and pair of elements, the choices are made by a finite search in a fixed order. For each \(h=2,3,\ldots\) in turn:

1. Put \(q=2^h\), and let \(\ell\) be the least prime with \(\ell\equiv-1\pmod{q^{100}}\), found by testing \(q^{100}-1,\,2q^{100}-1,\ldots\) for primality; the search terminates by (LIN). Put \(D=\ell+1\), \(s=\lfloor\log_qD\rfloor\), \(b=s+20\), \(n=10b\).
2. Let \(g\) be the first monic irreducible polynomial over \(\mathbb F_2\) of degree \(h(\ell-1)\), in lexicographic order of coefficient vectors, and \(K=\mathbb F_2[Z]/(g)\). Irreducible polynomials of every degree \(N\) exist: a field with \(2^N\) elements exists and is a simple extension of \(\mathbb F_2\) (Judson, Theorem 22.6 and Corollary 22.12), and the minimal polynomial of a generator is irreducible of degree \(N\).
3. Let \(Q=\{x\in K:x^q=x\}\), a subfield with \(q\) elements because \(h\) divides \(h(\ell-1)\) (Judson, Theorem 22.7), and let \(\zeta\) be the first element of \(K\) of multiplicative order \(\ell\). It exists: \(\ell\) divides \(2^{\ell-1}-1\) by Fermat's little theorem ([Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30): Judson, Theorem 6.19), hence divides \(|K^\times|=2^{h(\ell-1)}-1\), and \(K^\times\) is cyclic (Judson, Corollary 22.11).
4. In a fixed order, test every pair \((O,\mathcal F)\) of a set \(O\subseteq S\) and a family \(\mathcal F\) of affine lines in \(\mathcal A=Q^n\) for: \(2q^n/D^2\le|O|\le7q^n/D^2\); every line of \(\mathcal F\) avoids \(O\); every point of \(\mathcal A\setminus O\) lies on exactly \(D\) lines of \(\mathcal F\); the incidence graph has no cycle of length less than \(12\).

Stop at the first success; if no pair succeeds, go to the next \(h\). For each \(h\) this is a finite computation, and by Theorem 1.1 of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md) some pair succeeds for every large \(h\), for every enumeration of \(Q\). So the search stops. It searches the incidence data directly, not the random choices of the existence proof; it is not claimed to be practical.

From the output, put \(m=|O|\), \(t=|\mathcal A\setminus O|\), and let \(x_v\) be the vectors of Proposition 3.1 of [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md), computed from the interpolation polynomials. The local injections \(\iota_{vf}\), the point \(v_*\), the slots and the forms are fixed by the first-in-order rules: at each point, the \(\ell+1\) lines through it are matched in order to the lines through \(0\) of \(\mathbb F_\ell^2\), with \(1\) sent to the first nonzero vector of the matched line, and the points are assigned in order to the first \(t\) pairs \((s,\alpha)\) in lexicographic order. This fixes the groups \(N\), \(H\), \(L\), \(F\), \(G=L\times F\) and the elements \(a,b\in K[G]\) of [Packing and the reverse defect](packing-and-the-reverse-defect.md). They are finite expressions in group words and field elements; they are well defined whether or not two displayed words represent the same element of \(G\), so no solution of the word problem is needed.

## 4. The counterexample and its consequences

*Proof of Theorem 5.1 of [Directly finite group algebras](directly-finite-group-algebras.md).* The search of Section 3 terminates. Its output satisfies the hypotheses of Proposition 3.1 of [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md): \(q=2^h\ge4\), \(O\subseteq S\), the size bounds, and lines of \(\mathcal F\) in \(V\); so the vectors \(x_v\) satisfy \(0<m<t\le m\ell^2\) and the pairing identities. The incidence system is \(D\)-regular with \(D=\ell+1\) and has girth at least \(12\). The field \(K\) has characteristic two and contains \(Q\) and a primitive \(\ell\)-th root of unity \(\zeta\). So the incidence criterion, Theorem 1.1 of [The glued group and planar balance](the-glued-group-and-planar-balance.md), proved in [Packing and the reverse defect](packing-and-the-reverse-defect.md), gives a finitely presented group \(G\) with an element of order \(\ell\) and \(a,b\in K[G]\) with \(ab=1\) and \(ba\ne1\). \(\square\)

*Proof of Corollary 5.2 of [Directly finite group algebras](directly-finite-group-algebras.md).* By Proposition 2.2 of [Sofic groups and surjunctivity](sofic-groups-and-surjunctivity.md), the cellular automaton \(T_b:K^G\to K^G\), \((T_bx)(g)=\sum_ub_u\,x(gu)\), is injective, its image is the set of configurations fixed by \(T_{ba}\), and it misses the configuration \(\delta_h\) for every \(h\) with \((ba-1)_h\ne0\). So \(G\) is not surjunctive, and by Theorem 5.1 there, \(G\) is not sofic. \(\square\)

The nonvanishing of \(ba-1\) is certified by the sandwich of [Packing and the reverse defect](packing-and-the-reverse-defect.md), Lemma 3.1, and the character \(\varepsilon\) of \(K[H]\), which maps the defect to the matrix \(-\kappa X^{\mathsf T}X-I_t\) over \(K\). The local rule of the automaton can be read off any finite expression \(b=\sum_i\lambda_iu_i\) with repetitions allowed: the memory \(\{u_i\}\) and the rule \(p\mapsto\sum_i\lambda_ip(u_i)\) give the same map \(T_b\).

## 5. Remarks on the construction

*Torsion and denominators.* The averages over subgroups of orders \(\ell\), \(\ell^2\), \(\ell^3\) and \(\ell^m\) need these odd orders to be invertible in \(K\); no inverse of \(|S_m|\) is used. Characteristic two enters through Remark 3.2 of [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md): the regular degree \(\ell+1\) must vanish in \(K\). The group of Theorem 5.1 has odd torsion; the torsion-free example over \(\mathbb F_2\) of the same family uses a different construction ([Directly finite group algebras](directly-finite-group-algebras.md), Section 6).

*Finiteness of the group.* By Lemma 2.1 of [Directly finite group algebras](directly-finite-group-algebras.md), the group must be infinite, and by Lemma 2.2 there, any counterexample lives on a finitely generated group; finite presentability of \(G\) is the extra information given by [Packing and the reverse defect](packing-and-the-reverse-defect.md), Lemma 5.1.

*A group of type \(F_\infty\).* A group has type \(F_\infty\) if it has a classifying space with finitely many cells in each dimension. A companion manuscript of the OpenAI release constructs a group of type \(F_\infty\) into which every finitely presented group embeds [OpenAI-Finfty, Theorem 1.1]. An embedding \(G\hookrightarrow U\) induces an injective homomorphism \(K[G]\to K[U]\), so the images of \(a\) and \(b\) give a counterexample over a group of type \(F_\infty\), which by Section 4 is again neither sofic nor surjunctive [OpenAI-DF2, Corollary 7.4]. This embedding theorem is not proved in the programme and is not used elsewhere in the course.

## 6. Exercises

**6.1** (easy). For \(q=2\), take \(P=\mathbb F_4\) as a two-dimensional \(\mathbb F_2\)-space and \(\eta=\omega\) with \(\omega^2=\omega+1\). List the three nonzero forms \(\gamma\) and the three lines \(\Lambda_\gamma\) of Lemma 1.1 in the slab \(P\oplus\mathbb F_2\delta\) with \(o=0\), and check that they partition the six points off the axis.

**6.2** (easy). Explain why a cycle of length \(4\) in the incidence graph of a family of affine lines is impossible.

**6.3** (medium). In the search of Section 3, why is it legitimate to search the pairs \((O,\mathcal F)\) directly, rather than the random choices of the existence proof? What does the existence proof guarantee about the search?

**6.4** (medium). Show that if \(a,b\in K[G]\) satisfy \(ab=1\ne ba\) and \(G\le U\), then the same elements show that \(K[U]\) is not directly finite, and that \(U\) is neither surjunctive nor sofic.

## 7. Solutions

**6.1.** The nonzero forms on \(\mathbb F_4=\{0,1,\omega,\omega^2\}\) over \(\mathbb F_2\) with basis \(1,\omega\) are \(\gamma_1(x_0+x_1\omega)=x_0\), \(\gamma_2=x_1\), \(\gamma_3=x_0+x_1\). Multiplication by \(\omega\) sends \(1\mapsto\omega\), \(\omega\mapsto\omega^2=1+\omega\), \(\omega^2\mapsto1\). The point of \(\Lambda_\gamma\) over \(x\) is \(x+\gamma(\omega x)\delta\).

- \(\gamma_1(x)=1\) for \(x=1\) and \(x=\omega^2\); \(\gamma_1(\omega)=0\) and \(\gamma_1(1)=1\), so \(\Lambda_{\gamma_1}=\{1,\ \omega^2+\delta\}\).
- \(\gamma_2(x)=1\) for \(x=\omega\) and \(x=\omega^2\); \(\gamma_2(\omega^2)=1\) and \(\gamma_2(1)=0\), so \(\Lambda_{\gamma_2}=\{\omega+\delta,\ \omega^2\}\).
- \(\gamma_3(x)=1\) for \(x=1\) and \(x=\omega\); \(\gamma_3(\omega)=1\) and \(\gamma_3(\omega^2)=0\), so \(\Lambda_{\gamma_3}=\{1+\delta,\ \omega\}\). The six points off the axis \(\{0,\delta\}\) are \(1,\omega,\omega^2,1+\delta,\omega+\delta,\omega^2+\delta\), each covered once.

**6.2.** A cycle of length \(4\) consists of two points on two distinct lines; two affine lines sharing two points coincide.

**6.3.** The theorem on line systems only asserts that suitable pairs exist for every large \(h\); the random choices were a tool in its proof. Searching all pairs in a fixed order finds one such pair, the first in that order, for the least \(h\) that admits one; the existence proof guarantees that this \(h\) exists, so the search terminates.

**6.4.** The inclusion induces an injective homomorphism \(K[G]\to K[U]\) of algebras, so \(ab=1\) and \(ba-1\ne0\) hold in \(K[U]\). If \(K\) is finite, Corollary 6.1 of [Sofic groups and surjunctivity](sofic-groups-and-surjunctivity.md) applies to \(U\).

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Sections 5.5, 6 and 7 (Lemmas 5.8, 5.9, Corollaries 7.3 and 7.4). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [OpenAI-Finfty] OpenAI, *A universal group of type \(F_\infty\)*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/A-universal-group-of-type-F-infinity-September-23-2026
