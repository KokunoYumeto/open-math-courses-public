# A word detector in unitriangular matrices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The girth condition of the cover asks that every short closed walk of the tower that cannot be shortened has nontrivial holonomy. The voltages will be random elements of a nilpotent group that maps onto the group \(U_{\mathbb Z}\) of upper unitriangular integer \(m\times m\) matrices. This lesson shows why such a group can detect short walks: a short cyclically nonbacktracking closed walk in a graph of large girth has a support of bounded cycle rank, so after collapsing a spanning tree its holonomy is a nontrivial free word of bounded length, and a nontrivial free word of length less than \(m\) is never an identity on \(U_{\mathbb Z}\), by a finite form of the Magnus expansion [OpenAI-KK, Section 8.1].

- The rank bound (Section 1).
- Pivot words (Section 2).
- The matrix detector (Section 3).
- The choice of \(m\) (Section 4).

## 1. The rank bound

A *metric graph* is a graph whose edges are intervals of positive lengths; it carries the path metric. Its *girth* is the infimum of the lengths of its embedded circles, \(+\infty\) for a forest, and \(b_1(S)\) denotes its first Betti number, the rank of its first homology.

**Lemma 1.1** (rank bound; [OpenAI-KK, Lemma 8.1]). Let \(S\) be a finite connected metric graph of total length at most \(Cg\) and girth greater than \(g>0\). Then
\[
b_1(S)\le B(C)=\max\{1,\lceil20C\rceil\}^2 .
\]
Vertices of degree one and parallel edges are allowed.

*Proof.* Put \(a=g/10\) and choose a maximal set \(\mathcal P\) of points of \(S\) with pairwise distances at least \(a\); every point of \(S\) is within \(a\) of \(\mathcal P\). If \(|\mathcal P|\ge2\), each \(p\in\mathcal P\) is joined to another point of \(\mathcal P\) by a shortest path of length at least \(a\), whose initial piece of length \(a/2\) lies in the open ball of radius \(a/2\) about \(p\); these balls are disjoint. So \(|\mathcal P|a/2\le Cg\), and \(|\mathcal P|\le\max\{1,\lceil20C\rceil\}\).

Let \(K\) be the graph with vertex set \(\mathcal P\) and one edge for each pair at distance at most \(3a\), mapped to a chosen shortest path in \(S\). Every path of \(S\) between points of \(\mathcal P\) is homotopic, relative to its ends, to the image of a path in \(K\): cut it into segments of length at most \(a\), choose points of \(\mathcal P\) within \(a\) of the cut points, and replace each segment by the chosen path between the chosen points, which are at distance at most \(3a\). The segment, the two connecting paths and the replacement form a closed path of length at most \(6a<g\), which is null-homotopic: after cancelling backtracks, a nonempty reduced closed path in a graph contains an embedded circle of at most its length. So \(K\) is connected and its map is surjective on fundamental groups, hence on first homology with rational coefficients, and \(b_1(S)\le b_1(K)\le|\mathcal P|^2\le B(C)\). \(\square\)

## 2. Pivot words

Let \(W\) be a closed walk in a graph whose edges carry formal variables \(x_e\), with \(x_e^{-1}\) for the reverse orientation. Its *holonomy word* is the product of the variables along the walk.

**Lemma 2.1** (pivot words; [OpenAI-KK, Lemma 8.2]). Let \(W\) be a nonempty cyclically nonbacktracking closed walk of length at most \(Cg\) in a graph with unit edges and girth greater than \(g\). There is a spanning tree \(T\) of the support of \(W\) such that, after setting the variables of the edges of \(T\) equal to \(1\), the holonomy word of \(W\) has a nontrivial free reduction of length at most
\[
L(C)=\lceil3C\,B(C)\rceil .
\]

*Proof.* Let \(S\) be the support of \(W\) and \(b=b_1(S)\). A vertex of degree one in \(S\) would force a backtrack of \(W\), also across its base point, so all degrees are at least two and \(b\ge1\). If all degrees are two, \(S\) is a circle, which we regard as one *arc* with a chosen end. Otherwise suppress the vertices of degree two; with all degrees at least three, Euler's formula gives at most \(2b-2\) vertices and \(3b-3\) arcs. In both cases there are at most \(3b\) arcs, and \(b\le B(C)\) by Lemma 1.1, since \(S\) has total length at most \(Cg\).

The arcs shorter than \(g/(3b)\) form a forest: a circuit of such arcs would have length less than \(g\). Extend it to a spanning tree of the suppressed graph, and from every arc outside this tree delete one edge, its *pivot*. The remaining edges form a spanning tree \(T\) of \(S\). Start \(W\) at a vertex that is an end of an arc. Since \(W\) does not backtrack, it traverses every arc it enters completely, and each crossing of a pivot belongs to a separate traversal of an arc of length at least \(g/(3b)\). So there are at most \(Cg\cdot3b/g\le3CB(C)\) pivot crossings, and the word with the tree variables set to \(1\) has at most \(L(C)\) letters. Collapsing \(T\) is a homotopy equivalence from \(S\) to a bouquet of circles, one for each pivot, and it carries \(W\) to a closed path whose class in the free group on the pivots is that word. A nonempty cyclically nonbacktracking closed walk in a graph is not null-homotopic, so the class is nontrivial, and free reduction does not increase the length. \(\square\)

## 3. The matrix detector

Let \(U_{\mathbb Z}\) be the group of upper unitriangular \(m\times m\) integer matrices, and \(U\) the real ones.

**Lemma 3.1** (the matrix detector; [OpenAI-KK, Lemma 8.2]). Let \(w\) be a nontrivial reduced word of length less than \(m\) in letters \(x_1,\ldots,x_r\) and their inverses.

1. There are \(X_1,\ldots,X_r\in U_{\mathbb Z}\) with \(w(X_1,\ldots,X_r)\ne1\).
2. For variable matrices \(X_j\in U\), every entry of \(w(X_1,\ldots,X_r)\) is a polynomial of total degree at most \(m-1\) in the entries above the diagonal of the \(X_j\), and some entry of \(w(X)-1\) is a nonzero polynomial.
3. This remains true if every \(X_j\) is replaced by \(c_jX_jc'_j\) with fixed \(c_j,c'_j\in U\).

*Proof.* (1) Write \(w=x_{j_1}^{a_1}\cdots x_{j_k}^{a_k}\) with \(a_s\ne0\) and \(j_s\ne j_{s+1}\); then \(k\le|w|<m\). In noncommuting power series put \(x_j=1+Z_j\) and \((1+Z)^a=\sum_{h\ge0}\binom ahZ^h\), also for \(a<0\). In the expansion of \(w\), the monomial \(Z_{j_1}Z_{j_2}\cdots Z_{j_k}\) has coefficient \(a_1a_2\cdots a_k\ne0\): each factor \((1+Z_{j_s})^{a_s}\) contributes a power of \(Z_{j_s}\), a power at least two would create equal adjacent letters, and \(k\) letters from \(k\) factors require one letter from each. Now put
\[
Z_j=\sum_{s:\,j_s=j}E_{s,s+1}\in M_m(\mathbb Z) ,
\]
with the matrix units \(E_{s,s+1}\); these are nilpotent, so the series are finite sums and \(X_j=1+Z_j\in U_{\mathbb Z}\). A product \(Z_{i_1}\cdots Z_{i_t}\) has a nonzero \((1,k+1)\) entry only if \(t=k\) and \(i_s=j_s\) for all \(s\), because its entries follow chains of indices \(1\to2\to\cdots\). So the \((1,k+1)\) entry of \(w(X)\) is \(a_1\cdots a_k\ne0\), and \(w(X)\ne1\).

(2) Give the entry \((u,v)\), \(u<v\), the weight \(v-u\). The inverse of \(1+Y\), with \(Y\) strictly upper triangular, is \(\sum_{h=0}^{m-1}(-Y)^h\). In a product of such matrices and inverses, every monomial of the \((u,v)\) entry is a product of entries along a chain \(u=i_0<i_1<\cdots<i_q=v\), of total weight \(v-u\le m-1\); since every variable has weight at least one, its degree is at most \(m-1\). By (1) the polynomial entry of \(w(X)-1\) at \((1,k+1)\) is not identically zero.

(3) The maps \(X\mapsto cXc'\) are bijections of \(U\) given by polynomials with polynomial inverses, so they carry a nonzero polynomial to a nonzero polynomial. \(\square\)

## 4. The choice of \(m\)

Fix, once and for all, an integer \(m\ge2\) with
\[
m>L(201C_*) ,\tag{4.1}
\]
where \(C_*\) is the constant of the girth condition (Section 4 of [Thin triangles, overlap balls and the residual forest](thin-triangles-overlap-balls-and-the-residual-forest.md)).

**Lemma 4.1.** For large \(\ell\), let \(W\) be a nonempty cyclically nonbacktracking closed walk in the tower \(Y\), based in layer \(i\), of length at most \(C_*H_i/\log_2d\). Assign independent variable matrices \(X_e\in U\) to the edges of its support. Then some entry of the holonomy \(w(X)-1\) is a nonzero polynomial of degree at most \(m-1\), also after every \(X_e\) is multiplied on either side by fixed matrices of \(U\).

*Proof.* The layers \(j\) met by \(W\) satisfy \(H_j\ge H_i-C_*H_i/\log_2d\ge\frac{200}{201}H_i\) for large \(\ell\). By Proposition 4.1(5) of [Pruning and recovery of long paths](pruning-and-recovery-of-long-paths.md), every circuit of the support, a cyclically nonbacktracking closed path based in some such layer \(j\), has length greater than \(g_j=H_j/(100\log_2d)\ge g\), where \(g=H_i/(201\log_2d)\). The length of \(W\) is at most \(201C_*g\). By Lemma 2.1 with \(C=201C_*\), setting the tree variables to \(1\) leaves a nontrivial reduced word of length at most \(L(201C_*)<m\), so by Lemma 3.1 the holonomy with the tree variables equal to \(1\) has a nonzero entry polynomial, and so does the holonomy with all variables free, which specializes to it. Lemma 3.1(2) and (3) give the degree bound and the invariance. \(\square\)

## 5. Exercises

**5.1** (easy). For \(m=3\), compute the commutator \([X,Y]=XYX^{-1}Y^{-1}\) of \(X=1+E_{12}\) and \(Y=1+E_{23}\) and show that it is \(1+E_{13}\).

**5.2** (easy). Show that every word of length one or two that is nontrivial and reduced is detected by \(U_{\mathbb Z}\) with \(m=3\), and give a nontrivial reduced word of length four that is an identity on \(U_{\mathbb Z}\) for \(m=2\).

**5.3** (medium). For the word \(w=x_1x_2x_1^{-1}x_2^{-1}\), carry out the construction of Lemma 3.1(1) with \(m=5\) and compute the \((1,5)\) entry of \(w(X)\).

**5.4** (medium). In Lemma 1.1, give an example showing that some girth hypothesis is needed: a connected metric graph of total length \(1\) with arbitrarily large \(b_1\).

## 6. Solutions

**5.1.** \(XY=1+E_{12}+E_{23}+E_{13}\), \(X^{-1}=1-E_{12}\), \(Y^{-1}=1-E_{23}\), and multiplying out, \(XYX^{-1}Y^{-1}=1+E_{13}\).

**5.2.** A reduced word of length one or two is \(x^{\pm1}\), \(x^{\pm2}\) or \(x^{\pm1}y^{\pm1}\) with \(y\ne x\); with \(x\mapsto1+E_{12}\) and \(y\mapsto1+E_{23}\) its value has a nonzero entry above the diagonal. For \(m=2\), \(U_{\mathbb Z}\cong\mathbb Z\) is abelian, so the commutator \(xyx^{-1}y^{-1}\) is an identity.

**5.3.** Here \(k=4\), \(a=(1,1,-1,-1)\), \(Z_1=E_{12}+E_{34}\), \(Z_2=E_{23}+E_{45}\). The \((1,5)\) entry is \(a_1a_2a_3a_4=1\).

**5.4.** A bouquet of \(n\) circles of length \(1/n\) each has total length \(1\) and \(b_1=n\); its girth is \(1/n\), which makes \(C=n\) in the lemma.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 8.1, Lemmas 8.1 and 8.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
