# The Heisenberg group and its laws

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The voltages of the covering graph in this course are elements of the integral Heisenberg group \(\mathsf H\). Two of its properties are used. It is torsion-free and contains the commuting pair \((z,x)\), which spans the torus whose Bott class the course shows to vanish. And its laws are long: if the word of a closed path in a graph is a law in \(\mathsf H\), then some *bicycle*, a connected subgraph of cycle rank two without vertices of valence one, is traversed at least four times. The pruning of the graph in later lessons removes all short bicycles; this lesson turns that into the statement that short closed paths are not laws, which is what the choice of voltages needs [OpenAI-BCI, Lemma 4.13].

- Normal form and commutators in \(\mathsf H\) (Section 1).
- Words, laws and their coordinates (Section 2).
- Bicycles and cores of graphs (Section 3).
- The theorem: laws use a bicycle four times (Section 4).
- Sharpness (Section 5).

Only elementary group theory and graph theory are used.

## 1. The group and its coordinates

Commutators are \([a,b]=aba^{-1}b^{-1}\). The integral Heisenberg group is
\[
\begin{gathered}
\mathsf H=\langle x,y,z\mid [x,y]=z,\\
[x,z]=[y,z]=1\rangle .
\end{gathered}
\]
Let \(\mathrm{UT}_3(\mathbb Z)\) be the group of integral upper triangular \(3\times3\) matrices with diagonal entries \(1\), and write \(M(\alpha,\beta,\gamma)\) for the matrix with entries \(\alpha\) at \((1,2)\), \(\beta\) at \((2,3)\) and \(\gamma\) at \((1,3)\). Matrix multiplication gives
\[
\begin{aligned}
&M(\alpha,\beta,\gamma)M(\alpha',\beta',\gamma')\\
&\quad=M(\alpha+\alpha',\,\beta+\beta',\\
&\qquad\quad\gamma+\gamma'+\alpha\beta').
\end{aligned}\tag{1.1}
\]

**Lemma 1.1** (normal form). Every element of \(\mathsf H\) has exactly one expression \(x^ny^lz^c\) with \(n,l,c\in\mathbb Z\). Writing \((n,l,c)\) for this element,
\[
\begin{aligned}
&(n,l,c)(n',l',c')\\
&\quad=(n+n',\,l+l',\\
&\qquad\quad c+c'-ln'),\\
&(n,l,c)^{-1}\\
&\quad=(-n,-l,-c-ln).
\end{aligned}\tag{1.2}
\]
The assignment \(x\mapsto M(1,0,0)\), \(y\mapsto M(0,1,0)\), \(z\mapsto M(0,0,1)\) extends to an isomorphism \(\mathsf H\to\mathrm{UT}_3(\mathbb Z)\), which sends \((n,l,c)\) to \(M(n,l,c+nl)\).

*Proof.* By (1.1), \(M(1,0,0)M(0,1,0)=M(1,1,1)\) and \(M(0,1,0)M(1,0,0)=M(1,1,0)\); the inverse of \(M(1,1,0)\) is \(M(-1,-1,1)\), and \(M(1,1,1)M(-1,-1,1)=M(0,0,1)\). So the three matrices satisfy \([x,y]=z\). The matrix \(M(0,0,1)\) commutes with every \(M(\alpha,\beta,\gamma)\) by (1.1). Hence the assignment extends to a homomorphism \(\phi:\mathsf H\to\mathrm{UT}_3(\mathbb Z)\).

In \(\mathsf H\) the element \(z\) is central, and \(xy=zyx\), so \(yx=z^{-1}xy\). Conjugating by \(y\) gives \(yx^{\pm1}y^{-1}=(xz^{-1})^{\pm1}\), hence \(yx^{n'}y^{-1}=x^{n'}z^{-n'}\) for every integer \(n'\), and by induction on \(|l|\)
\[
\begin{gathered}
y^lx^{n'}=x^{n'}y^lz^{-ln'}\\
(l,n'\in\mathbb Z).
\end{gathered}\tag{1.3}
\]
Using (1.3) and the centrality of \(z\), the product \(x^ny^lz^c\cdot x^{n'}y^{l'}z^{c'}\) equals \(x^{n+n'}y^{l+l'}z^{c+c'-ln'}\). In particular the set of elements of the form \(x^ny^lz^c\) contains the generators and their inverses and is closed under products, so it is all of \(\mathsf H\). The product rule in (1.2) has just been proved, and the inverse rule follows from it: \((n,l,c)(-n,-l,-c-ln)\) equals \((0,0,c-c-ln+ln)=(0,0,0)\).

By (1.1), \(\phi(x^n)=M(n,0,0)\), \(\phi(y^l)=M(0,l,0)\) and \(\phi(z^c)=M(0,0,c)\), so \(\phi(x^ny^lz^c)=M(n,l,c+nl)\). Distinct triples have distinct images, which proves uniqueness of the normal form and injectivity of \(\phi\). Every \(M(\alpha,\beta,\gamma)\) is the image of \((\alpha,\beta,\gamma-\alpha\beta)\), so \(\phi\) is onto. \(\square\)

**Corollary 1.2.** \(\mathsf H\) is torsion-free. Its center is \(\{z^c\}\cong\mathbb Z\). The elements \(z\) and \(x\) generate a free abelian subgroup of rank two, and \(z^ux^v=(v,0,u)\).

*Proof.* If \((n,l,c)^k=1\) with \(k\ge1\), the first two coordinates of (1.2) give \(kn=kl=0\), so \(n=l=0\); then \((0,0,c)^k=(0,0,kc)\) forces \(c=0\). An element \((n,l,c)\) commuting with \(x=(1,0,0)\) satisfies \(c-l=c\) by (1.2), so \(l=0\); commuting with \(y=(0,1,0)\) gives \(n=0\). Finally \(z^ux^v=x^vz^u=(v,0,u)\), and these elements are distinct for distinct \((u,v)\). \(\square\)

**Lemma 1.3** (commutators). For \(g=(n,l,c)\) and \(h=(n',l',c')\),
\[
[g,h]=z^{\,nl'-ln'} .
\]
In particular \([g,h]\) is central and depends only on the first two coordinates, and \([x^\varepsilon,y^m]=z^{\varepsilon m}\).

*Proof.* By (1.2), \(gh=(N,L,c+c'-ln')\) and \(hg=(N,L,c+c'-l'n)\) with \(N=n+n'\), \(L=l+l'\). Then \((hg)^{-1}\) is \((-N,-L,-c-c'+l'n-LN)\), and (1.2) gives
\[
\begin{gathered}
gh(hg)^{-1}\\
=(0,0,\,l'n-ln'-LN+LN),
\end{gathered}
\]
which is \(z^{nl'-ln'}\). \(\square\)

## 2. Words and laws

Let \(X\) be a graph; loops and multiple edges are allowed. Choose an orientation of every edge, and attach a distinct variable \(t_e\) to every edge \(e\). An *edge path* is a sequence of traversals of edges, each in the positive or negative direction, such that each traversal starts where the previous one ends. Its *word* reads \(t_e\) on a positive traversal of \(e\) and \(t_e^{-1}\) on a negative one. A word is an *\(\mathsf H\)-law* if it evaluates to the identity for every assignment of elements of \(\mathsf H\) to the variables.

For an edge path or word \(V\) and an edge \(e\), let \(n_e(V)\) be the number of positive traversals of \(e\) minus the number of negative ones, and call the total number of traversals of \(e\) its *multiplicity*. An edge path is *reduced as a based path* if no two consecutive traversals in its linear order are the same edge in opposite directions. A closed edge path is *cyclically reduced* if moreover its last and first traversals are not the same edge in opposite directions.

**Lemma 2.1** (coordinates of a word). Let \(w=t_{e_1}^{\varepsilon_1}\cdots t_{e_L}^{\varepsilon_L}\) be a word, and assign \(t_e=(n_e,l_e,c_e)\). Then the value of \(w\) is
\[
\begin{gathered}
\Bigl(\sum_ea_en_e,\ \sum_ea_el_e,\\
\sum_ea_ec_e+Q\Bigr),\qquad a_e=n_e(w),
\end{gathered}
\]
where \(Q\) is a polynomial with integer coefficients and degree at most two in the variables \(n_e,l_e\), not depending on the \(c_e\). The word is an \(\mathsf H\)-law if and only if \(a_e=0\) for every \(e\) and \(Q\) is the zero polynomial.

*Proof.* By (1.2), \(t_e^{-1}=(-n_e,-l_e,-c_e-l_en_e)\), so each letter has first two coordinates linear in \((n_e,l_e)\) and third coordinate \(\pm c_e\) plus a polynomial of degree at most two in \((n_e,l_e)\). Induct on \(L\): if the value of the first \(k\) letters has the stated form, multiplying by the next letter adds the coordinates and subtracts the product of the second coordinate of the first factor with the first coordinate of the second factor; both are linear in the variables \(n_e,l_e\), so the correction term has degree at most two and does not involve the \(c_e\).

If all \(a_e\) vanish and \(Q=0\), the value is the identity for every assignment. Conversely, let \(w\) be a law. Assigning \(t_e=x\) for one edge \(e\) and the identity to all other variables gives the value \((a_e,\ast,\ast)\), so \(a_e=0\). Then the value is \((0,0,Q)\), so \(Q\) vanishes at every integer point. A polynomial in \(m\) variables vanishing at all integer points is zero: for \(m=1\) a nonzero polynomial has finitely many roots, and in general, expanding in powers of the last variable, every coefficient vanishes at all integer points by the case \(m=1\), hence is zero by induction. \(\square\)

A cyclic rotation of a closed edge path, that is, the same closed path started at another of its traversals, has a word conjugate to the original word under every assignment; so rotations of laws are laws.

## 3. Bicycles and cores

For a finite graph \(S\), the *cycle rank* is \(b_1(S)=|E(S)|-|V(S)|+c(S)\), where \(c(S)\) is the number of components; it is the rank of the cycle space of \(S\). The *valence* of a vertex counts edge ends, so a loop contributes two. A *bicycle* is a finite connected graph \(B\) with \(b_1(B)=2\) and no vertex of valence one. Its *length* is its number of edges, or the sum of positive edge lengths \(\ell(e)\) if such lengths are given.

**Lemma 3.1** (shapes of bicycles). After suppressing its vertices of valence two, a bicycle is one of the following: a *theta*, two vertices joined by three edges; a *figure-eight*, one vertex with two loops; a *barbell*, two vertices joined by an edge, with one loop at each. A figure-eight or a barbell contains two edge-disjoint cycles; a theta consists of three paths between two vertices, any two of which form a cycle.

*Proof.* A connected graph has \(\sum_v(\operatorname{val}(v)-2)=2|E|-2|V|\), which is \(2b_1-2=2\) when \(b_1=2\). All valences are at least two, so either exactly one vertex has valence four, or exactly two vertices have valence three, and all others have valence two. Suppressing valence-two vertices (replacing each maximal path through them by one edge) keeps \(b_1\) and the valences of the remaining vertices; a bicycle is not a cycle, so at least one vertex remains. With one vertex of valence four and \(|E|=|V|+1=2\), both edges are loops. With two vertices \(u,v\) of valence three and three edges: a loop at \(u\) uses two of its three ends, so either there are no loops and the three edges join \(u\) to \(v\), or there is a loop at \(u\), the third end of \(u\) is an edge to \(v\), and the remaining two ends at \(v\) form a loop. \(\square\)

**Lemma 3.2** (bicycles inside cycle rank two). Every finite connected graph \(S\) with \(b_1(S)\ge2\) contains a bicycle as a subgraph.

*Proof.* Choose a spanning tree \(T\) of \(S\) and two distinct edges \(f_1,f_2\) of \(S\) outside \(T\); they exist because \(|E(S)|-|E(T)|=b_1(S)\). Let \(T'\) be the smallest subtree of \(T\) containing the endpoints of \(f_1\) and \(f_2\), and let \(B=T'\cup\{f_1,f_2\}\). Then \(B\) is connected, \(|V(B)|=|V(T')|\) and \(|E(B)|=|E(T')|+2=|V(B)|+1\), so \(b_1(B)=2\). A leaf of \(T'\) is an endpoint of \(f_1\) or \(f_2\), since otherwise removing it would give a smaller subtree; so its valence in \(B\) is at least two. Other vertices of \(T'\) have valence at least two in \(T'\). If \(T'\) is a single vertex, both \(f_i\) are loops at it and its valence is four. \(\square\)

**Lemma 3.3** (cores). Let \(S\) be a finite connected graph and \(C\) a nonempty cyclically reduced closed edge path whose edges lie in \(S\). Repeatedly delete a vertex of valence one together with its edge. Then \(C\) never uses a deleted edge, the cycle rank does not change, and the process ends with a subgraph \(K\), the *core*, which contains all edges of \(C\) and has no vertex of valence one. If \(b_1(S)=1\), then \(K\) is a cycle.

*Proof.* Suppose \(C\) uses only edges of the current graph, and let \(v\) have valence one there, with edge \(e\). A visit of \(C\) to \(v\) would enter and leave through \(e\), which is an immediate reversal in the cyclic order of \(C\); so \(C\) does not visit \(v\) and does not use \(e\). Deleting a vertex and an edge keeps \(b_1\) and connectedness. The process ends, and \(K\) contains the nonempty edge set of \(C\). If \(b_1(K)=1\), then \(|E(K)|=|V(K)|\) and every valence is at least two, so \(\sum_v\operatorname{val}(v)=2|E(K)|=2|V(K)|\) forces every valence to be two; a finite connected graph with all valences two is a cycle. \(\square\)

## 4. Laws use a bicycle four times

Edges have positive lengths \(\ell(e)\), and an edge path \(W\) has length \(\ell(W)\), the sum of the lengths of its traversals. The *support* of \(W\) is the subgraph of its edges and their endpoints.

**Theorem 4.1** (laws contain a bicycle used four times; [OpenAI-BCI, Lemma 4.13]). Let \(W\) be a nonempty closed edge path in \(X\), reduced as a based path, whose word is an \(\mathsf H\)-law. Then the support of \(W\) contains a bicycle \(B\) every edge of which is traversed at least four times by \(W\). Consequently
\[
\ell(W)\ge4\,\ell(B).
\]
In particular, if every bicycle in the support of \(W\) has length at least \(T\), then \(\ell(W)\ge4T\).

*Proof.* *Balance.* Assigning \(t_e=x\) and the identity to all other variables evaluates the word to \(x^{n_e(W)}\), and \(x\) has infinite order, so
\[
\begin{gathered}
n_e(W)=0\\
\text{for every edge }e.
\end{gathered}\tag{4.1}
\]
Thus every edge of the support has positive even multiplicity. Call an edge *paired* if its multiplicity is exactly two and *heavy* if it is at least four.

*Intervals of paired edges.* Let \(e\) be paired. By (4.1) its two traversals have opposite signs. Rotate \(W\) to start at the first of them and write its word as
\[
W=t_e^{\varepsilon}\,U\,t_e^{-\varepsilon}\,V,\qquad\varepsilon=\pm1 .
\]
Here \(U\) is the part of \(W\) strictly between the two traversals of \(e\) in the original linear order. Fix an edge \(f\neq e\), put \(n=n_f(U)\), assign \(t_e=x\), \(t_f=y\) and the identity to all other variables. Since \(e\) does not occur in \(U\) or \(V\), (4.1) gives \(n_f(V)=-n\), and the rotated word evaluates to
\[
x^{\varepsilon}y^{n}x^{-\varepsilon}y^{-n}=[x^\varepsilon,y^n]=z^{\varepsilon n}
\]
by Lemma 1.3. The rotation is a law and \(z\) has infinite order, so \(n=0\):
\[
\begin{gathered}
n_f(U)=0\\
\text{for every edge }f .
\end{gathered}\tag{4.2}
\]
(For \(f=e\) this holds because \(e\) does not occur in \(U\).)

*An innermost interval.* Join the two positions of each paired edge in the linear order of \(W\) by an interval. Two such intervals cannot cross: if the intervals of \(e\) and \(f\) crossed, the interior of the interval of \(e\) would contain exactly one traversal of \(f\), and \(n_f\) of that interior would be \(\pm1\), contradicting (4.2). If paired edges exist, choose an interval minimal for inclusion and let \(U\) be the edge path strictly inside it. Every edge occurring in \(U\) is heavy: a paired edge occurring in \(U\) would, by (4.2), occur twice in \(U\), and its interval would be smaller. The traversal \(t_e^{\varepsilon}\) ends at the vertex where \(t_e^{-\varepsilon}\) starts, so \(U\) is a closed edge path. It is nonempty, since otherwise the two traversals of \(e\) would be consecutive, an immediate reversal in \(W\). It is reduced as a based path, being a contiguous part of \(W\), and \(n_f(U)=0\) for all \(f\) by (4.2). If there are no paired edges, put \(U=W\); it has the same four properties, and all its edges are heavy.

*Cycle rank of the support.* Let \(S\) be the support of \(U\), a finite connected graph. Repeatedly remove the first and last traversals of \(U\) while they are the same edge in opposite directions. This writes \(U=PCP^{-1}\) with \(C\) cyclically reduced. If the process emptied \(U\), its last step would remove two consecutive traversals forming an immediate reversal inside \(U\), which is impossible; so \(C\) is nonempty. Each removal deletes one positive and one negative traversal of the same edge, so \(n_f(C)=n_f(U)=0\) for all \(f\).

Suppose \(b_1(S)\le1\). If \(b_1(S)=0\), then \(S\) is a tree and the deletions of Lemma 3.3 remove every edge, while \(C\) keeps its edges; this is impossible. If \(b_1(S)=1\), the core \(K\) is a cycle containing the edges of \(C\). At each vertex of the cycle \(K\), the path \(C\) cannot reverse the traversal by which it arrived, since \(C\) is cyclically reduced; so \(C\) runs around \(K\) in one direction, \(k\ge1\) times, and \(n_f(C)=\pm k\neq0\) for every edge \(f\) of \(K\). This contradicts \(n_f(C)=0\). Hence \(b_1(S)\ge2\).

*The bicycle.* By Lemma 3.2, \(S\) contains a bicycle \(B\). Every edge of \(S\) occurs in \(U\), hence is heavy in \(W\). Since the lengths are positive,
\[
\begin{gathered}
\ell(W)=\sum_e(\text{multiplicity of }e)\,\ell(e)\\
\ge4\sum_{e\in E(S)}\ell(e)\ge4\,\ell(B). \qquad\square
\end{gathered}
\]

With \(\mathbb Z\) in place of \(\mathsf H\) only (4.1) survives: a word is a law in \(\mathbb Z\) exactly when it is balanced, and the step "cycle rank of the support" above shows that the support of a balanced cyclically reduced closed path contains a bicycle. Friedman, Izsak and Silberman characterize the *abelian girth* of a graph, the least length of such a balanced path, through its bicycles [FIS, Lemma 2.6], and their proof contains this step. The two-variable substitution is what forces the factor four for \(\mathsf H\).

**Corollary 4.2.** Let \(T>0\). If a graph contains no bicycle of length less than \(T\), then every nonempty cyclically reduced closed edge path of length less than \(4T\) has a word that is not an \(\mathsf H\)-law.

*Proof.* A cyclically reduced closed path is reduced as a based path, and Theorem 4.1 gives \(\ell(W)\ge4T\) for a law. \(\square\)

In the course, Corollary 4.2 is applied with \(T=1.52\,m_i\), the scale below which the pruning removes all bicycles near layer \(i\); closed paths of length at most \(6.04\,m_i\) are then nonlaws, with room for the variation of the scale along the path (lesson [Thetas and the pruned old graph](thetas-and-the-pruned-old-graph.md)).

## 5. Sharpness

On a bouquet of two loops \(a,b\) (one vertex, two edges), the word
\[
aba^{-1}b^{-1}a^{-1}bab^{-1}=[a,b]\,[a^{-1},b]
\]
is cyclically reduced: no two cyclically consecutive letters are inverse to each other. It is an \(\mathsf H\)-law, because by Lemma 1.3 the commutator \([g,h]=z^{nl'-ln'}\) changes sign when \(g\) is replaced by \(g^{-1}\), whose first two coordinates are \((-n,-l)\). Each edge is traversed four times, the support is a figure-eight, and \(\ell(W)=4\ell(a)+4\ell(b)=4\ell(B)\). So the factor four in Theorem 4.1 cannot be improved, and the inequality is not strict. Subdividing the two loops into paths, with one variable for each new edge, gives the same equality for figure-eights of any lengths.

## 6. Exercises

**Exercise 6.1.** Show that \(\mathsf H\) is nilpotent of class two: \([[g,h],k]=1\) for all \(g,h,k\), and \([gg',h]=[g,h][g',h]\).

**Exercise 6.2.** Show that the commutator word \([[a,b],c]\), read on a bouquet of three loops, is cyclically reduced and an \(\mathsf H\)-law. Find the bicycle of Theorem 4.1 and compare \(\ell(W)\) with \(4\ell(B)\).

**Exercise 6.3.** Show that the commutator \(aba^{-1}b^{-1}\) on a bouquet of two loops is balanced but not an \(\mathsf H\)-law. Which step of the proof of Theorem 4.1 detects this?

**Exercise 6.4.** Let \(W\) be a cyclically reduced closed path in a theta graph with branches \(P_1,P_2,P_3\) between vertices \(u\) and \(v\). Show that if \(W\) is an \(\mathsf H\)-law then every branch is traversed at least four times, and give an example of such a law.

**Exercise 6.5.** Compute the polynomial \(Q\) of Lemma 2.1 for the word \([t_1,t_2]\), and deduce Lemma 1.3 from it.

## 7. Solutions

**6.1.** By Lemma 1.3, \([g,h]\) is a power of \(z\), which is central, so \([[g,h],k]=1\). The exponent \(nl'-ln'\) is additive in the first two coordinates of \(g\), and the first two coordinates of \(gg'\) are the sums of those of \(g\) and \(g'\) by (1.2); hence \([gg',h]=[g,h][g',h]\).

**6.2.** The word is \(aba^{-1}b^{-1}\,c\,bab^{-1}a^{-1}\,c^{-1}\); its consecutive pairs \(b^{-1}c\), \(cb\) and the cyclic pair \(c^{-1}a\) are not inverse pairs, and the commutator parts are reduced, so it is cyclically reduced. Since \([a,b]\) is central by Exercise 6.1, \([[a,b],c]=1\) for every assignment. The loops \(a,b\) are traversed four times and \(c\) twice; the bicycle is the figure-eight on \(a,b\), and \(\ell(W)=4\ell(a)+4\ell(b)+2\ell(c)>4\ell(B)\).

**6.3.** Every loop is traversed once in each direction, so the word is balanced. Assigning \(a=x\), \(b=y\) gives \([x,y]=z\neq1\). In the proof, both loops are paired; the interval of \(a\) contains exactly one traversal of \(b\), which is the crossing excluded by (4.2), and indeed the two-variable substitution evaluates to \(z^{\pm1}\).

**6.4.** The edges of one branch are traversed equally often, since a cyclically reduced path entering the interior of a branch runs through it. If some branch were traversed only twice, its edges would be paired, and Theorem 4.1 would give a bicycle of heavy edges in the support; but the only bicycle inside a theta is the whole theta, which contains that branch. If the path used only two branches, its support would be a cycle, which the proof of Theorem 4.1 excludes. So every branch is traversed at least four times. An example: with the closed paths \(a=P_1P_2^{-1}\) and \(b=P_1P_3^{-1}\) at \(u\), the word \([a,b][a^{-1},b]\) is a law. Its free reduction cancels one pair \(P_1^{-1}P_1\), and its cyclic reduction one more, leaving the closed path
\[
\begin{gathered}
P_2^{-1}P_1P_3^{-1}P_2P_1^{-1}P_3\\
P_1^{-1}P_2P_3^{-1}P_1P_2^{-1}P_3
\end{gathered}
\]
at \(v\), a cyclic conjugate of a law, hence a law, which traverses each branch exactly four times.

**6.5.** With \(t_i=(n_i,l_i,c_i)\), (1.2) gives \(t_1t_2=(n_1+n_2,l_1+l_2,c_1+c_2-l_1n_2)\) and the computation of Lemma 1.3 gives \([t_1,t_2]=(0,0,n_1l_2-l_1n_2)\). So the exponent sums vanish and \(Q=n_1l_2-l_1n_2\), which is Lemma 1.3.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Section 4.7, Lemma 4.13. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [FIS] J. Friedman, A. Izsak and L. Silberman, *Abelian girth and girth*, arXiv:1511.03678 (2015), Lemma 2.6. https://arxiv.org/abs/1511.03678
