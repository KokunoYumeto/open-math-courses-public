# Aligned presentations of the cycle module

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The comparison theorem of [Finite quotients and the comparison theorem](finite-quotients-and-the-comparison-theorem.md) starts from a group \(\Gamma\) with a finite generating alphabet \(S\) and a finite list \(\mathcal D\) of words whose chains form a basis of the cycle module of the generator graph. Such a list need not be a presentation of \(\Gamma\): the chain of a word forgets the order of its letters. If \(\Gamma\) has a classifying space of dimension two, this lesson produces an actual presentation of \(\Gamma\), with any number of generators and relators, whose relators include, for each word of \(\mathcal D\), a relator with exactly the same chain, and whose remaining relators are controlled by additional letters of value \(1\) [OpenAI-EG, Section 3.1]. The construction is linear algebra over the group ring, realized by words: adjoining letters, changing free generators, and three shears.

- Generator graphs and chains of words (Section 1).
- Presentations and moves that keep a basis (Section 2).
- From a classifying space to a presentation (Section 3).
- Aligned presentations (Section 4).

Throughout, \(\Gamma\) is a group and \(\Lambda=\mathbb Z\Gamma\), acting on the left. A *direct sum* \(\Lambda^{(I)}\) over an index set \(I\) consists of the finitely supported families; its standard basis is \((e_i)_{i\in I}\). Cohomological dimension, classifying spaces and the statement (CW) are as in [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md).

## 1. Generator graphs and chains of words

Let \(A\) be a set with a map \(A\to\Gamma\), the *values* of its letters; distinct letters are kept distinct even if their values coincide, and a letter may have value \(1\). The *generator graph* has vertex set \(\Gamma\) and, for every \(g\in\Gamma\) and \(a\in A\), an oriented edge from \(g\) to \(g\bar a\), where \(\bar a\) is the value of \(a\). Its chains of edges form \(\Lambda^{(A)}\), with \(ge_a\) the edge from \(g\) to \(g\bar a\), and the boundary map is
\[
\partial_1\colon\Lambda^{(A)}\to\Lambda,\qquad\partial_1(e_a)=\bar a-1 .
\]
Its kernel is the *cycle module*. A word \(w\) in the letters of \(A\) and their inverses has a *value* \(\bar w\in\Gamma\) and a *chain* \([w]\in\Lambda^{(A)}\), the signed sum of the edges traversed by the path that starts at \(1\) and reads \(w\): the letter \(a\) at vertex \(g\) traverses \(ge_a\) forwards, and \(a^{-1}\) at vertex \(g\) traverses \(g\bar a^{-1}e_a\) backwards.

**Lemma 1.1** (chains of words). For words \(u,v,b\):

1. \([uv]=[u]+\bar u[v]\), \([u^{-1}]=-\bar u^{-1}[u]\), and \(\partial_1[u]=\bar u-1\);
2. if \(\bar b=1\), then \([vbv^{-1}]=\bar v[b]\) and \([vb^{-1}v^{-1}]=-\bar v[b]\);
3. the chain depends only on the element of the free group on \(A\) represented by the word.

*Proof.* (1) The path reading \(uv\) reads \(u\) from \(1\) and then \(v\) from \(\bar u\), and the path reading \(u^{-1}\) is the path reading \(u\), translated to start at \(\bar u^{-1}\) and traversed backwards. The boundary of the chain of a path is its endpoint minus its starting point. (2) By (1), \([vbv^{-1}]=[v]+\bar v[b]+\bar v\bar b[v^{-1}]\), which is \([v]+\bar v[b]-[v]\), and \([b^{-1}]=-[b]\) when \(\bar b=1\). (3) Inserting or deleting \(aa^{-1}\) or \(a^{-1}a\) adds a forward and a backward traversal of one edge. \(\square\)

## 2. Presentations and moves that keep a basis

A *presentation* \(\langle A\mid R\rangle\) of \(\Gamma\) consists of a set \(A\) with values generating \(\Gamma\) and an indexed family \(R\) of words, the *relators*, of value \(1\), whose normal closure in the free group on \(A\) is the kernel of the map to \(\Gamma\). Its *relator boundary map* is
\[
\Lambda^{(R)}\to\Lambda^{(A)},\qquad e_r\mapsto[r],
\]
with image in the cycle module. The presentation has the *basis property* if this map is an isomorphism onto the cycle module, that is, if the chains of the relators form a \(\Lambda\)-basis of the cycle module. All index sets may be infinite, of any cardinality.

**Lemma 2.1** (moves). Each of the following changes of a presentation with the basis property gives a presentation of \(\Gamma\) with the basis property.

1. *Adjoining a letter with a definition relator:* add a letter \(s\) and the relator \(sw^{-1}\), where \(w\) is a word in the old letters with \(\bar w=\bar s\).
2. *A change of free generators:* replace a letter \(a\) by a new letter \(t\) with value \(\bar a\bar w^{-1}\), where \(w\) is a word not involving \(a\), and substitute \(a=tw\) in every relator.
3. *A shear:* split the relators into two families, keep the words of the first, and multiply each word \(r\) of the second by finitely many words \(v_kb_k^{\pm1}v_k^{-1}\), with \(b_k\) relators of the first family.

*Proof.* (1) The new relator has chain \(e_s+\bar s[w^{-1}]=e_s-[w]\), with coefficient \(1\) on the new edge. Every new cycle minus the corresponding multiple of this chain is a cycle on the old letters, so the new relator chains form a basis. The normal closure is the kernel, since the new letter is eliminated by its relator.

(2) The substitution \(a\mapsto tw\) is an isomorphism of free groups, with inverse \(t\mapsto aw^{-1}\), and it preserves values. By Lemma 1.1, \([tw]=e_t+\bar t[w]\). The map \(e_a\mapsto e_t+\bar t[w]\), fixing the other edges, is an isomorphism \(\Lambda^{(A)}\to\Lambda^{(A')}\) of chain modules commuting with \(\partial_1\), since \(\partial_1(e_t+\bar t[w])=\bar t\bar w-1=\bar a-1\); by Lemma 1.1 and induction on the length of words, it carries the chain of each old relator to the chain of the substituted relator.

(3) By Lemma 1.1, multiplying \(r\) by \(v_kb_k^{\pm1}v_k^{-1}\) adds \(\pm\bar v_k[b_k]\) to its chain, since \(\bar r=1\). The change of the relator boundary map is therefore an invertible change of basis of \(\Lambda^{(R)}\), triangular with respect to the two families, and the new chains form a basis. The old relator is recovered from the new one by multiplying with the inverse factors, so the normal closures agree. \(\square\)

## 3. From a classifying space to a presentation

We use the following facts of homotopy theory, proved in the course on cell complexes, fundamental groups and covering spaces: parts 1 and 2 are Propositions 2.1 and 3.1 of [Cell complexes and homotopy equivalences](course:cell-complexes-and-covering-spaces/cell-complexes-and-homotopy-equivalences), with Lemma 4.3 and Proposition 4.2 there for spanning trees and their contractibility; parts 3 and 5 are Corollaries 2.5 and 4.2 of [Fundamental groups of graphs and two-complexes](course:cell-complexes-and-covering-spaces/fundamental-groups-of-graphs-and-two-complexes); and part 4 is Proposition 4.1 of [Universal covers and cellular chains](course:cell-complexes-and-covering-spaces/universal-covers-and-cellular-chains).

**(HE)** (homotopy equivalences of CW complexes; also [Hatcher, Propositions 0.17, 0.18, 1.26 and 1A.2]).

1. If \(T\) is a contractible subcomplex of a CW complex \(Y\), the quotient map \(Y\to Y/T\) is a homotopy equivalence.
2. Attaching cells along homotopic maps gives homotopy equivalent CW complexes.
3. Every map from a circle to a graph is homotopic to a closed edge path.
4. A homotopy equivalence of connected CW complexes induces an isomorphism of fundamental groups and lifts to a homotopy equivalence of universal covers.
5. The fundamental group of a CW complex with one vertex, edges \(A\) and \(2\)-cells attached along words \(R\) in the edges is \(\langle A\mid R\rangle\).

**Lemma 3.1** (aspherical presentations). If \(\Gamma\) has a classifying space of dimension at most two, then \(\Gamma\) has a presentation with the basis property.

*Proof.* Let \(Y\) be such a classifying space. Its \(1\)-skeleton is connected and contains a maximal tree \(T\), which is contractible. By (HE 1) and (HE 2), \(Y\) is homotopy equivalent to the complex obtained from the wedge of circles \(Y^1/T\) by attaching the \(2\)-cells along closed edge paths homotopic to their attaching maps, which exist by (HE 3). This complex \(Y'\) has one vertex, and by (HE 5) it is the complex of a presentation \(\langle A\mid R\rangle\) of \(\pi_1(Y')\cong\pi_1(Y)\cong\Gamma\). By (HE 4) its universal cover is homotopy equivalent to that of \(Y\), hence contractible. By (CW) its cellular chains are those of the generator graph of \(A\), with a \(2\)-cell over every relator attached along the path reading it from each vertex, and by Lemma 2.2 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md) the augmented cellular chain complex
\[
0\to\Lambda^{(R)}\to\Lambda^{(A)}\xrightarrow{\ \partial_1\ }\Lambda\to\mathbb Z\to0
\]
is exact. Exactness at \(\Lambda^{(R)}\) and at \(\Lambda^{(A)}\) is the basis property. \(\square\)

## 4. Aligned presentations

Let \(S\) be a finite generating alphabet of \(\Gamma\) and \(\mathcal D\) a finite indexed list of words on \(S\), each of value \(1\), such that
\[
\begin{gathered}
\Lambda^{(\mathcal D)}\to\ker\partial_1,\\
e_z\mapsto[z],
\end{gathered}\tag{4.1}
\]
is an isomorphism onto the cycle module of the generator graph of \(S\).

**Lemma 4.1** (aligned presentation; [OpenAI-EG, Lemma 3.2]). If moreover \(\Gamma\) has a classifying space of dimension at most two, then there is a presentation
\[
\Gamma=\bigl\langle S,\mathcal T\bigm|(\rho_z)_{z\in\mathcal D},\ (r)_{r\in\mathcal R}\bigr\rangle
\]
with the basis property such that:

1. every letter of \(\mathcal T\) has value \(1\);
2. \([\rho_z]=[z]\) for every \(z\in\mathcal D\);
3. projecting the chains \([r]\), \(r\in\mathcal R\), to the coordinates of the \(\mathcal T\)-edges gives an isomorphism
\[
\Lambda^{(\mathcal R)}\to\Lambda^{(\mathcal T)}.\tag{4.2}
\]

The sets \(\mathcal T\) and \(\mathcal R\) may be infinite; \(\rho_z\) are the *distinguished* relators and the \(r\in\mathcal R\) the *ordinary* ones.

*Proof.* *Step 1.* Start with a presentation \(\langle A\mid R\rangle\) with the basis property, from Lemma 3.1. Adjoin the letters of \(S\), each with a definition relator, by Lemma 2.1(1). Then, for each \(a\in A\), choose a word \(w_a\) on \(S\) with value \(\bar a\), and replace \(a\) by a letter \(t_a\) of value \(1\), substituting \(a=t_aw_a\), by Lemma 2.1(2). Let \(T=\{t_a\}\) and let \(R\) denote the current relator family. The letters are now \(S\amalg T\), and the \(T\)-edges are loops, so the cycle module is \(\ker\partial_1|_{\Lambda^{(S)}}\oplus\Lambda^{(T)}\). By (4.1) it is identified with \(\Lambda^{(I)}\), \(I=\mathcal D\amalg T\): the index \(z\in\mathcal D\) corresponds to \([z]\) and \(t\in T\) to \(e_t\). In these coordinates the relator boundary map is an isomorphism
\[
\mathsf A\colon\Lambda^{(R)}\to\Lambda^{(I)}.
\]

*Step 2.* Adjoin letters \(u_i\), \(i\in I\), of value \(1\), each with the one-letter relator \(u_i\), by Lemma 2.1(1). The \(U\)-edges are loops, the cycle module becomes \(\Lambda^{(I)}\oplus\Lambda^{(I)}\), the second summand spanned by the \(U\)-edges, and the relator boundary map becomes
\[
\begin{aligned}
D_0=\begin{pmatrix}\mathsf A&0\\0&1\end{pmatrix}\colon{}&\Lambda^{(R)}\oplus\Lambda^{(I)}\\
&\to\Lambda^{(I)}\oplus\Lambda^{(I)} .
\end{aligned}
\]

*Step 3.* On the relator index module put
\[
P=\begin{pmatrix}1&\mathsf A^{-1}\\0&1\end{pmatrix},\qquad Q=\begin{pmatrix}1&0\\-\mathsf A&1\end{pmatrix}.
\]
Composing,
\[
\begin{aligned}
PQP&=\begin{pmatrix}0&\mathsf A^{-1}\\-\mathsf A&0\end{pmatrix},\\
D_0PQP&=\begin{pmatrix}0&1\\-\mathsf A&0\end{pmatrix}.
\end{aligned}\tag{4.3}
\]
Replacing the boundary map \(D\) by \(DP\) adds to the boundary of each relator of the second family, indexed by \(i\in I\), the combination \(D(\mathsf A^{-1}e_i,0)\) of translates of boundaries of the first family, and keeps the first family; replacing \(D\) by \(DQ\) does the same with the roles of the families exchanged. Each column of \(\mathsf A\) and \(\mathsf A^{-1}\) is finitely supported, so each change adds finitely many translates, and it is realized by a shear of Lemma 2.1(3): multiply the changing relator by the words \(v_kb_k^{\pm1}v_k^{-1}\) for the required translates \(\bar v_k[b_k]\). After the three shears \(P,Q,P\), the boundary map is \(D_0PQP\), the presentation still presents \(\Gamma\), and it has the basis property.

*Reading off.* By (4.3), the relator of the second family indexed by \(i\in I\) has chain \((e_i,0)\): for \(i=z\in\mathcal D\) this is \([z]\), and we call this relator \(\rho_z\); for \(i=t\in T\) it is \(e_t\). The relator of the first family indexed by \(r\in R\) has chain \((0,-\mathsf Ae_r)\), supported on the \(U\)-edges. Put \(\mathcal T=T\amalg U\) and let the ordinary relators be the second-family relators indexed by \(T\) together with the first family, \(\mathcal R=T\amalg R\). Projected to the \(\mathcal T\)-coordinates, their chains are given by
\[
\begin{aligned}
\begin{pmatrix}1_T&0\\0&-\mathsf A\end{pmatrix}\colon{}&\Lambda^{(T)}\oplus\Lambda^{(R)}\\
&\to\Lambda^{(T)}\oplus\Lambda^{(I)}=\Lambda^{(\mathcal T)},
\end{aligned}
\]
an isomorphism. All letters of \(\mathcal T\) have value \(1\). \(\square\)

The words in \(\mathcal D\) have value \(1\), but their normal closure need not be the whole kernel, so they need not present \(\Gamma\), and the construction does not use them as relators: the distinguished relators \(\rho_z\) have the same chains as the words \(z\), not necessarily the same letters in the same order. The comparison theorem bridges this difference with labels in the unit quaternions.

## 5. Exercises

**5.1.** Let \(\Gamma=\mathbb Z\), \(S=\{t\}\) with \(\bar t=t\). Describe the generator graph and its cycle module, and show that the empty list \(\mathcal D\) satisfies (4.1).

**5.2.** For \(\Gamma=\mathbb Z^2=\langle x,y\rangle\), \(S=\{x,y\}\), show that the commutator \(xyx^{-1}y^{-1}\) has chain \((1-y)e_x+(x-1)e_y\), and that \(\mathcal D=\{xyx^{-1}y^{-1}\}\) satisfies (4.1), using Lemma 3.2 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md).

**5.3.** Show that the words \(xyx^{-1}y^{-1}\) and \(yxy^{-1}x^{-1}\) in the free group have chains that differ only by sign and translation, but represent different elements of the free group.

**5.4.** Verify the products (4.3).

**5.5.** In the proof of Lemma 4.1, explain why the letters \(u_i\) are needed: what goes wrong if the shears are applied to \(\mathsf A\) alone?

## 6. Solutions

**5.1.** The graph is the line with vertices \(t^n\) and edges from \(t^n\) to \(t^{n+1}\). The boundary map \(\Lambda\to\Lambda\), \(e_t\mapsto t-1\), is injective, so the cycle module is \(0\), and the empty list gives the isomorphism \(0\to0\).

**5.2.** By Lemma 1.1 and commutativity,
\[
\begin{aligned}
[xyx^{-1}y^{-1}]&=e_x+xe_y-xyx^{-1}e_x-xyx^{-1}y^{-1}e_y\\
&=(1-y)e_x+(x-1)e_y.
\end{aligned}
\] In Lemma 3.2 of that lesson, the kernel of \(d_1\) is the image of the injective map \(d_2(r)=\bigl((y-1)r,-(x-1)r\bigr)\), which is \(-r\) times this chain.

**5.3.** \([yxy^{-1}x^{-1}]=(1-x)e_y+(y-1)e_x\), which is \(-[xyx^{-1}y^{-1}]\); the two words are inverse to each other in the free group, \((xyx^{-1}y^{-1})^{-1}=yxy^{-1}x^{-1}\), and a commutator of free generators is not its own inverse.

**5.4.** First
\[
\begin{aligned}
PQ&=\begin{pmatrix}1-\mathsf A^{-1}\mathsf A&\mathsf A^{-1}\\-\mathsf A&1\end{pmatrix}\\
&=\begin{pmatrix}0&\mathsf A^{-1}\\-\mathsf A&1\end{pmatrix},
\end{aligned}
\]
then \(PQP=\begin{pmatrix}0&\mathsf A^{-1}\\-\mathsf A&-\mathsf A\mathsf A^{-1}+1\end{pmatrix}\), and multiply by \(D_0\) on the left.

**5.5.** Shears change the relator boundary map by triangular matrices with identity diagonal blocks. To obtain relators whose chains are exactly the basis elements \(e_i\) from the family \(R\) alone, one would have to write \(\mathsf A^{-1}\) as a product of such matrices, which need not be possible. The identity block carried by the loops \(u_i\) makes room for three shears whose composite \(PQP\) exchanges the two blocks, as in (4.3); this is the usual way of writing \(\begin{pmatrix}0&\mathsf A^{-1}\\-\mathsf A&0\end{pmatrix}\) as a product of elementary block matrices.

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
