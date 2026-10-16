# Wall's D(2) problem and twisted homology

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite CW complex of dimension three can behave, for homology and cohomology with all systems of coefficients, like a complex of dimension two. Wall asked whether such a complex is then homotopy equivalent to a finite complex of dimension two. [OpenAI-W] gives a complex for which the answer is no. The proof has three parts: an obstruction that every finite complex of dimension two satisfies, a construction that produces complexes of dimension three with the required homology, and one explicit group.

This lesson states the problem and the theorem, lists the standard theorems of algebraic topology on which the course rests, and develops the tool of the whole course: the chain complex of a CW complex with coefficients twisted by a character of the fundamental group.

- The D(2) condition and the theorem (Section 1).
- Six standard theorems TOP1 to TOP6, all proved in the programme except the homotopy invariance in TOP5 (Section 2).
- Chains of the universal cover; coefficients in a module; characters (Section 3).
- Dimension two, \(H_0\), the Euler characteristic, maps to \(\mathbb Z\) (Lemmas 4.1 to 4.4).
- Presentation complexes and Fox derivatives (Lemma 5.1).

The lesson follows [OpenAI-W, Sections 1 and 2] for the notions. It needs groups, modules over a ring, and the basic notions of algebraic topology: CW complexes, the fundamental group, covering spaces, homology ([Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), core course).

## 1. The problem and the theorem

Let \(X\) be a finite connected CW complex, \(G=\pi_1(X)\) its fundamental group and \(\widetilde X\) its universal cover.

**Definition.** \(X\) satisfies the *condition D(2)* if
\[
H_i(\widetilde X;\mathbb Z)=0\ \text{ for all }i>2,
\]
and \(H^3(X;M)=0\) for every left module \(M\) over the group ring \(\mathbb Z[G]\).

The cohomology with coefficients in \(M\) is defined in Section 3. A complex of dimension at most two satisfies the condition, because it has no cells of dimension three. The condition is invariant under homotopy equivalence (TOP5 below, in its version for cohomology). So a complex that is homotopy equivalent to a complex of dimension at most two satisfies D(2). The *finite D(2) problem* asks for the converse: is every finite connected complex with D(2) homotopy equivalent to a finite complex of dimension at most two? According to [OpenAI-W], the question goes back to Wall (1965) and is Problem D3 of Wall's list of 1979.

**Theorem 1.1** ([OpenAI-W]). Assume the homotopy invariance in TOP5 of Section 2. There is a finite connected CW complex \(X\) of dimension three that satisfies the condition D(2) and is not homotopy equivalent to any finite CW complex of dimension at most two.

The complex has one vertex, five edges, six cells of dimension two and two cells of dimension three. Its fundamental group is infinite. The theorem is proved in [The counterexample](the-counterexample.md).

## 2. The standard theorems used

The course uses six theorems of algebraic topology that are in every textbook of the subject. Five of them, and the part of TOP5 on subcomplexes, are proved in the programme: in the course [Cell complexes, fundamental groups and covering spaces](course:cell-complexes-and-covering-spaces/cell-complexes-and-homotopy-equivalences), in the lesson [Frame fields and primary obstructions](course:DG-CHAR/DG-CHAR-08B) and in the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60); the places are given with each statement. The homotopy invariance in TOP5 is a **named hypothesis**, with a place in Hatcher's book [Hatcher], which is free on the author's page. All complexes are CW complexes, and maps are continuous.

**TOP1** (cells and the fundamental group; [Fundamental groups of graphs and two-complexes, Corollary 2.4 and Theorem 3.3](course:cell-complexes-and-covering-spaces/fundamental-groups-of-graphs-and-two-complexes)). Let \(Z\) be a connected complex.

- A complex with one vertex and loops \(x_1,\dots,x_g\) has the free group on \(x_1,\dots,x_g\) as its fundamental group.
- If \(Z'\) arises from \(Z\) by attaching cells of dimension two along loops that represent \(t_1,\dots,t_r\in\pi_1(Z)\), then \(\pi_1(Z)\to\pi_1(Z')\) is surjective, and its kernel is the normal closure of \(t_1,\dots,t_r\).
- If \(Z'\) arises from \(Z\) by attaching cells of dimension at least three, then \(\pi_1(Z)\to\pi_1(Z')\) is an isomorphism.

**TOP2** (covering spaces; [Universal covers and cellular chains, Theorem 1.1 and Propositions 3.1 and 3.2](course:cell-complexes-and-covering-spaces/universal-covers-and-cellular-chains)). Let \(Z\) be a connected complex, \(G=\pi_1(Z)\) and \(N\) a normal subgroup of \(G\).

- There is a connected covering \(p:Z_N\to Z\) with \(p_*\pi_1(Z_N)=N\). The space \(Z_N\) is a CW complex whose cells are the lifts of the cells of \(Z\). The group \(G/N\) acts on \(Z_N\) by homeomorphisms that commute with \(p\) and permute the cells; for every cell of \(Z\) it permutes the lifts of this cell freely and transitively.
- For \(N=1\) this is the universal cover \(\widetilde Z\), which is simply connected, and \(Z_N\) is the quotient of \(\widetilde Z\) by \(N\).
- A map \(f:F\to Z\) from a connected complex lifts to a map \(F\to Z_N\) if and only if \(f_*\pi_1(F)\subseteq N\).
- If \(Z\) is a simplicial complex, so is \(Z_N\), and \(p\) maps every simplex of \(Z_N\) isomorphically onto a simplex of \(Z\). If \(Z'\subseteq Z\) is a subcomplex, \(p^{-1}(Z')\) is a subcomplex of \(Z_N\).

**TOP3** (cellular homology; [Universal covers and cellular chains, Section 5 and Propositions 5.2 and 5.3](course:cell-complexes-and-covering-spaces/universal-covers-and-cellular-chains), and for \(H_1\) [Frame fields and primary obstructions, Lemma E.1](course:DG-CHAR/DG-CHAR-08B)). The homology of a complex \(Z\) with integer coefficients is the homology of its cellular chain complex \(C_*(Z)\), in which \(C_j(Z)\) is the free abelian group on the cells of dimension \(j\).

- If a cell of dimension \(j+1\) is attached to a complex \(Z\) of dimension at most \(j\) by a map \(\varphi:S^j\to Z\), its boundary in \(C_j(Z)\) is the cycle that represents the image of the fundamental class of \(S^j\) under \(\varphi\). In particular, if a cell of dimension two is attached along a closed path of edges \(e_{i_1}^{\epsilon_1}\cdots e_{i_q}^{\epsilon_q}\) with \(\epsilon_k=\pm1\), its boundary is \(\sum_k\epsilon_ke_{i_k}\).
- In a covering, the boundary of a lift of a cell is the lift of the boundary: the lifted cell is attached by the lifted map.
- For a connected complex, \(H_1(Z;\mathbb Z)\) is the abelianization of \(\pi_1(Z)\).

**TOP4** (Hurewicz; [Frame fields and primary obstructions, Lemma E.1](course:DG-CHAR/DG-CHAR-08B)). Let \(Z\) be a simply connected complex. Every class in \(H_2(Z;\mathbb Z)\) is the image of the fundamental class of \(S^2\) under a map \(S^2\to Z\).

**TOP5** (twisted coefficients). With the notation of Section 3:

- *Homotopy invariance.* Let \(h:Z\to Z'\) be a homotopy equivalence of connected complexes, and \(\theta:\pi_1(Z)\to\pi_1(Z')\) the isomorphism that it induces. For every right module \(N\) over \(\mathbb Z[\pi_1(Z')]\), with \(\theta^*N\) the same group with the action through \(\theta\), there are isomorphisms \(H_j(Z;\theta^*N)\cong H_j(Z';N)\) for all \(j\). The same holds for cohomology with coefficients in left modules, and for the homology of the universal covers.
- *Subcomplexes.* Let \(A\) be a connected subcomplex of a connected complex \(Z\), with \(\iota:\pi_1(A)\to\pi_1(Z)\). Then \(C_*(A;\iota^*N)\) is isomorphic to the subcomplex of \(C_*(Z;N)\) that is spanned by the cells of \(A\).

**TOP6** (simplicial models; [Fundamental groups of graphs and two-complexes, Corollary 4.4](course:cell-complexes-and-covering-spaces/fundamental-groups-of-graphs-and-two-complexes) and [Cell complexes and homotopy equivalences, Proposition 5.2](course:cell-complexes-and-covering-spaces/cell-complexes-and-homotopy-equivalences)).

- Every finite connected CW complex of dimension at most two is homotopy equivalent to a finite simplicial complex of dimension at most two.
- Every map from a finite simplicial complex \(F\) to a simplicial complex is homotopic to a map that is simplicial for an iterated barycentric subdivision of \(F\).

The part of TOP5 on subcomplexes is [Universal covers and cellular chains, Proposition 5.4](course:cell-complexes-and-covering-spaces/universal-covers-and-cellular-chains): if the lifts of the cells of \(A\) are chosen in \(\widetilde A\) and mapped to \(\widetilde Z\) by the map of that proposition, the boundary coefficients computed in \(\widetilde Z\) are the images under \(\iota\) of those computed in \(\widetilde A\). The homotopy invariance in TOP5 is a named hypothesis [Hatcher, Section 3.H]: it needs a comparison of the cellular chains of the universal cover with its singular chains as complexes of modules over the group ring, which [Hatcher] states without a detailed proof and which is not proved in the programme. It is recorded as an open obligation of the course.

Everything else in the course is proved in its four lessons and the lessons cited above.

## 3. Chains of the universal cover

Let \(Z\) be a connected complex and \(G=\pi_1(Z)\). By TOP2 the group \(G\) permutes the cells of \(\widetilde Z\). Choose one lift \(\tilde e\) of every cell \(e\) of \(Z\). Then every cell of dimension \(j\) of \(\widetilde Z\) is \(g\tilde e\) for exactly one \(g\in G\) and one cell \(e\) of \(Z\). So \(C_j(\widetilde Z)\) is a free left module over the group ring \(\mathbb Z[G]\), with the basis of the chosen lifts of the cells of dimension \(j\). The boundary maps commute with the action of \(G\); they are homomorphisms of \(\mathbb Z[G]\)-modules. For a cell \(e\) of dimension \(j\),
\[
\partial\tilde e=\sum_{e'}\lambda_{e,e'}\,\tilde e',\qquad\lambda_{e,e'}\in\mathbb Z[G],
\]
where \(e'\) runs through the cells of dimension \(j-1\). The elements \(\lambda_{e,e'}\) describe the complex.

**Definition.** For a right \(\mathbb Z[G]\)-module \(N\) and a left \(\mathbb Z[G]\)-module \(M\) put
\[
\begin{gathered}
C_*(Z;N)=N\otimes_{\mathbb Z[G]}C_*(\widetilde Z),\\
C^*(Z;M)=\operatorname{Hom}_{\mathbb Z[G]}\bigl(C_*(\widetilde Z),M\bigr),
\end{gathered}
\]
with the boundary maps induced by \(\partial\). Their homology groups are \(H_j(Z;N)\) and \(H^j(Z;M)\).

So \(C_j(Z;N)\) is a direct sum of copies of \(N\), one for each cell of dimension \(j\) of \(Z\), and \(\partial(n\otimes\tilde e)=\sum_{e'}n\lambda_{e,e'}\otimes\tilde e'\). An element of \(C^j(Z;M)\) is a choice of one element of \(M\) for each cell of dimension \(j\). For the module \(N=\mathbb Z\) with the trivial action, \(C_*(Z;\mathbb Z)\) is the cellular chain complex of \(Z\), by TOP3.

**Covers.** Let \(N\) be a normal subgroup of \(G\). The universal cover of \(Z_N\) is \(\widetilde Z\), with the group \(N\). So for a right \(\mathbb Z[N]\)-module \(N'\),
\[
C_*(Z_N;N')=N'\otimes_{\mathbb Z[N]}C_*(\widetilde Z).
\]
We call this the *formula for covers*. In particular, with the trivial module \(\mathbb Z\), the cellular chain complex of \(Z_N\) is \(\mathbb Z\otimes_{\mathbb Z[N]}C_*(\widetilde Z)\), which is \(\mathbb Z[G/N]\otimes_{\mathbb Z[G]}C_*(\widetilde Z)\). Here \(C_j(\widetilde Z)\) is free over \(\mathbb Z[N]\), with the basis \(s\tilde e\), where \(e\) runs through the cells of \(Z\) and \(s\) through representatives of the classes of \(G\) modulo \(N\).

**Characters.** A *character* is a homomorphism \(\rho:G\to\mathbb C^\times\) into the group of the nonzero complex numbers. It is *trivial* if \(\rho(g)=1\) for all \(g\). Let \(\mathbb C_\rho\) be the space \(\mathbb C\) with the right action \(v\cdot g=\rho(g)v\). We write
\[
C_*(Z;\rho)=\mathbb C_\rho\otimes_{\mathbb Z[G]}C_*(\widetilde Z)
\]
and \(H_j(Z;\rho)\) for its homology.
\(C_j(Z;\rho)\) is a complex vector space with the basis \(1\otimes\tilde e\), one element for each cell of dimension \(j\) of \(Z\). Extend \(\rho\) linearly to \(\mathbb Z[G]\to\mathbb C\). Then
\[
\partial(1\otimes\tilde e)=\sum_{e'}\rho(\lambda_{e,e'})\,(1\otimes\tilde e').
\]
So the boundary maps are the complex matrices \(\bigl(\rho(\lambda_{e,e'})\bigr)\). For the trivial character this is the cellular chain complex of \(Z\) with complex coefficients; its homology has the dimensions \(b_j(Z)\), the *Betti numbers*.

More generally, for a commutative ring \(R\) and a homomorphism \(\Theta\) from \(G\) to the units of \(R\), the complex \(C_*(Z;\Theta)\) consists of free \(R\)-modules with the boundary matrices \(\bigl(\Theta(\lambda_{e,e'})\bigr)\).

If \(\iota:H\to G\) is a homomorphism of groups, we write \(\rho\iota\) for the character \(\rho\circ\iota\) of \(H\). A character takes the same value on conjugate elements, so it does not depend on the choice of base points.

## 4. Four elementary properties

**Lemma 4.1** (dimension two). Let \(Z\) be a connected complex of dimension at most two and \(\rho\) a character. Then \(H_2(Z;\rho)\) is the kernel of \(\partial:C_2(Z;\rho)\to C_1(Z;\rho)\). If \(H_2(Z;\rho)=0\), then \(H_2(A;\rho\iota)=0\) for every connected subcomplex \(A\) with \(\iota:\pi_1(A)\to\pi_1(Z)\).

**Proof.** There are no cells of dimension three. By TOP5, \(C_*(A;\rho\iota)\) is a subcomplex of \(C_*(Z;\rho)\); the kernel of \(\partial\) on \(C_2(A;\rho\iota)\) is contained in the kernel on \(C_2(Z;\rho)\). \(\blacksquare\)

**Lemma 4.2** (degree zero). Let \(Z\) be a connected complex and \(\rho\) a character that is not trivial. Then \(H_0(Z;\rho)=0\).

**Proof.** \(\widetilde Z\) is connected, so \(H_0(\widetilde Z;\mathbb Z)=\mathbb Z\): for two vertices \(\tilde v,\tilde w\) of \(\widetilde Z\) the chain \(\tilde w-\tilde v\) is the boundary of a chain of \(C_1(\widetilde Z)\). Choose \(g\) with \(\rho(g)\ne1\) and a vertex \(\tilde v\). Then \(g\tilde v-\tilde v=\partial c\), so in \(C_0(Z;\rho)\)
\[
(\rho(g)-1)\,(1\otimes\tilde v)=\partial(1\otimes c),
\]
and \(1\otimes\tilde v\) is a boundary. For every other vertex \(\tilde w\), \(1\otimes\tilde w-1\otimes\tilde v\) is a boundary. So all of \(C_0(Z;\rho)\) consists of boundaries. \(\blacksquare\)

**Lemma 4.3** (Euler characteristic). Let \(Z\) be a finite connected complex of dimension at most two with \(c_j\) cells of dimension \(j\), and \(\chi(Z)=c_0-c_1+c_2\). For every character \(\rho\),
\[
\begin{aligned}
&\dim H_0(Z;\rho)-\dim H_1(Z;\rho)\\
&\qquad+\dim H_2(Z;\rho)=\chi(Z).
\end{aligned}
\]
In particular \(\chi(Z)=1-b_1(Z)+b_2(Z)\).

**Proof.** For a complex of finite-dimensional vector spaces, the alternating sum of the dimensions of the spaces is the alternating sum of the dimensions of the homology spaces: \(\dim C_j=\dim\ker\partial_j+\dim\operatorname{im}\partial_j\), and \(\dim H_j=\dim\ker\partial_j-\dim\operatorname{im}\partial_{j+1}\). The spaces \(C_j(Z;\rho)\) have the dimensions \(c_j\) for every \(\rho\). For the trivial character \(b_0=1\). \(\blacksquare\)

**Lemma 4.4** (maps to \(\mathbb Z\)). Let \(Z\) be a finite connected complex.

1. If \(b_1(Z)\ge1\), there is a surjective homomorphism \(\pi_1(Z)\to\mathbb Z\).
2. If \(b_1(Z)=0\), every homomorphism \(\pi_1(Z)\to\mathbb Z\) is trivial.

**Proof.** The group \(H_1(Z;\mathbb Z)\) is finitely generated, because \(C_1(Z)\) is. The complex \(C_*(Z;\mathbb C)\) is \(C_*(Z)\otimes\mathbb C\), and tensoring with \(\mathbb C\) keeps kernels and images; so \(b_1(Z)\) is the rank of \(H_1(Z;\mathbb Z)\). A finitely generated abelian group of rank \(\ge1\) maps onto \(\mathbb Z\); one of rank \(0\) is finite, and has only the trivial homomorphism to \(\mathbb Z\). A homomorphism \(\pi_1(Z)\to\mathbb Z\) factors through the abelianization, which is \(H_1(Z;\mathbb Z)\) by TOP3. \(\blacksquare\)

## 5. Presentation complexes

Let \(\langle x_1,\dots,x_g\mid r_1,\dots,r_h\rangle\) be a finite presentation of a group \(P\); the \(r_j\) are words in the letters \(x_i^{\pm1}\). Its *presentation complex* \(B\) has one vertex \(v\), one loop for each \(x_i\), and one cell \(D_j\) of dimension two for each \(r_j\), attached along the closed path of edges that the word \(r_j\) spells. By TOP1, \(\pi_1(B)=P\).

**Fox derivatives.** For a word \(w=y_1y_2\cdots y_q\) in the letters \(x_i^{\pm1}\) and a generator \(x_i\) define an element of \(\mathbb Z[P]\):
\[
\begin{aligned}
\frac{\partial w}{\partial x_i}={}&\sum_{k:\ y_k=x_i}u_k\\
&-\sum_{k:\ y_k=x_i^{-1}}u_kx_i^{-1}.
\end{aligned}
\]
Here \(u_k=y_1\cdots y_{k-1}\) is the part of the word before the letter number \(k\), read in \(P\). From the definition,
\[
\frac{\partial(ww')}{\partial x_i}=\frac{\partial w}{\partial x_i}+w\,\frac{\partial w'}{\partial x_i} .
\]

**Lemma 5.1.** Choose a vertex \(\tilde v\) of \(\widetilde B\), let \(\tilde x_i\) be the lift of the loop \(x_i\) that starts at \(\tilde v\), and \(\widetilde D_j\) the lift of \(D_j\) whose boundary path starts at \(\tilde v\). Then
\[
\begin{gathered}
\partial\tilde x_i=(x_i-1)\,\tilde v,\\
\partial\widetilde D_j=\sum_{i=1}^g\frac{\partial r_j}{\partial x_i}\,\tilde x_i .
\end{gathered}
\]
So for a character \(\rho\) of \(P\), the map \(\partial:C_2(B;\rho)\to C_1(B;\rho)\) has the matrix with the rows \(\bigl(\rho(\tfrac{\partial r_j}{\partial x_i})\bigr)_i\), \(j=1,\dots,h\), and \(H_2(B;\rho)=0\) if and only if these \(h\) rows are linearly independent.

**Proof.** The lift of the loop \(x_i\) that starts at \(u\tilde v\), for \(u\in P\), is \(u\tilde x_i\), and it ends at \(ux_i\tilde v\); this fixes the identification of \(P\) with the group of the cover. The lift of the path of \(r_j=y_1\cdots y_q\) from \(\tilde v\) passes the vertices \(u_k\tilde v\). A letter \(y_k=x_i\) is lifted to the edge \(u_k\tilde x_i\), run forward. A letter \(y_k=x_i^{-1}\) is lifted to a path from \(u_k\tilde v\) to \(u_kx_i^{-1}\tilde v\): this is the edge \(u_kx_i^{-1}\tilde x_i\), run backward. By TOP3 the boundary of \(\widetilde D_j\) is the sum of these edges with the signs \(+\) and \(-\). The last statement is Lemma 4.1. \(\blacksquare\)

The matrix of the lemma is computed from the words alone. For a character, every \(u_k\) is replaced by the number \(\rho(u_k)\), the product of the values of \(\rho\) on the letters before the position \(k\).

## 6. Exercises

**6.1.** The presentation \(\langle x\mid x^2\rangle\) has the real projective plane as its presentation complex. Compute \(H_2(B;\rho)\) for the two characters \(\rho(x)=\pm1\).

**6.2.** Compute the Fox derivatives of \(w=xax^{-1}a^{-n}\) by \(x\) and by \(a\), for \(n\ge1\).

**6.3.** The torus is the presentation complex of \(\langle a,b\mid aba^{-1}b^{-1}\rangle\). Show \(H_2(B;\rho)=0\) if and only if \(\rho\) is not trivial, and check Lemma 4.3.

**6.4.** Let \(X\) have dimension three. Show that \(H^3(X;M)=0\) if and only if every \(\mathbb Z[G]\)-linear map \(C_3(\widetilde X)\to M\) is of the form \(\psi\circ\partial_3\) with a \(\mathbb Z[G]\)-linear map \(\psi:C_2(\widetilde X)\to M\).

**6.5.** Let \(Z\) be finite, connected, of dimension at most two, and \(\rho\) a nontrivial character with \(H_2(Z;\rho)=0\). Show \(\chi(Z)\le0\) and \(b_1(Z)\ge1\).

## 7. Solutions

**6.1.** \(\partial r/\partial x=1+x\). So \(\partial:C_2\to C_1\) is the number \(1+\rho(x)\). For \(\rho(x)=1\) it is \(2\), and \(H_2=0\). For \(\rho(x)=-1\) it is \(0\), and \(H_2(B;\rho)=\mathbb C\).

**6.2.** The letters are \(x,a,x^{-1}\) and \(n\) times \(a^{-1}\). By \(x\): the first letter gives \(1\), the third gives \(-xa\cdot x^{-1}\). So \(\partial w/\partial x=1-xax^{-1}\). By \(a\): the second letter gives \(x\); the letter \(a^{-1}\) with the number \(l\) among the last \(n\) gives \(-xax^{-1}a^{-l}\). So
\[
\frac{\partial w}{\partial a}=x-xax^{-1}\sum_{l=1}^na^{-l}.
\]

**6.3.** \(\partial r/\partial a=1-aba^{-1}\) and \(\partial r/\partial b=a-aba^{-1}b^{-1}\). At a character: \(1-\rho(b)\) and \(\rho(a)-1\). The single row is \(0\) exactly if \(\rho\) is trivial. Lemma 4.3: \(\chi=1-2+1=0\). For a nontrivial \(\rho\): \(H_0=0\), \(H_2=0\), so \(H_1=0\). For the trivial one: \(1-2+1=0\) with \(b_1=2\), \(b_2=1\).

**6.4.** \(C^4=0\), so \(H^3(X;M)\) is the quotient of \(\operatorname{Hom}(C_3(\widetilde X),M)\) by the image of \(\psi\mapsto\psi\circ\partial_3\).

**6.5.** By Lemma 4.2, \(H_0(Z;\rho)=0\). By Lemma 4.3, \(\chi(Z)=-\dim H_1(Z;\rho)\le0\). From \(\chi(Z)=1-b_1+b_2\) we get \(b_1=1+b_2-\chi(Z)\ge1\).

## References

- [OpenAI-W] OpenAI, *A Counterexample to Wall's D(2) Problem*, OpenAI Math Release preprint, 6 October 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
