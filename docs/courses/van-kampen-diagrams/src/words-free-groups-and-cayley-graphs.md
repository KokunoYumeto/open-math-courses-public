# Words, free groups and Cayley graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson collects the algebra behind van Kampen diagrams: words and their free reduction, the free group, groups given by generators and relators, walks in graphs up to backtracking, and Cayley graphs. The normal form of Lemma 1.1 lets [Van Kampen's lemma](van-kampens-lemma.md) pass from a product of conjugates of relators to any word representing the same element, and the Cayley graph receives the label-preserving maps of diagrams. Graphs are described by darts as in [Plane maps](plane-maps.md).

## 1. Words and free reduction

Let \(S\) be a set. A *letter* is a pair \(x=(s,\varepsilon)\) with \(s\in S\) and \(\varepsilon\in\{1,-1\}\), written \(s\) or \(s^{-1}\); its inverse is \(x^{-1}=(s,-\varepsilon)\). A *word* is a finite sequence of letters, possibly empty; words are multiplied by concatenation, and the inverse of \(w=x_1\cdots x_n\) is \(w^{-1}=x_n^{-1}\cdots x_1^{-1}\). A *cancelling pair* in a word is a pair of consecutive letters \(x\,x^{-1}\); *cancelling* it deletes the two letters. A word without cancelling pairs is *reduced*. Two words are *freely equal* if one is obtained from the other by finitely many cancellations and insertions of cancelling pairs.

**Lemma 1.1** (normal form). Every word \(w\) is freely equal to exactly one reduced word \(\rho(w)\). Every sequence of cancellations applied to \(w\) that continues until no cancelling pair is left ends at \(\rho(w)\).

*Proof.* Let \(\mathrm{Red}\) be the set of reduced words. For a letter \(x\) define \(L_x:\mathrm{Red}\to\mathrm{Red}\) by \(L_x(v)=xv\) if \(v\) does not begin with \(x^{-1}\), and by deleting the first letter of \(v\) if it does. Both results are reduced. If \(v\) does not begin with \(x^{-1}\), then \(xv\) begins with \(x\) and \(L_{x^{-1}}(xv)=v\). If \(v=x^{-1}v'\), then \(v'\) does not begin with \(x\), because \(v\) is reduced, and \(L_{x^{-1}}(v')=x^{-1}v'=v\). So \(L_{x^{-1}}L_x\) is the identity, and by symmetry so is \(L_xL_{x^{-1}}\).

For a word \(w=x_1\cdots x_n\) put \(L_w=L_{x_1}\circ\cdots\circ L_{x_n}\), the identity for the empty word. Inserting or cancelling a pair \(x\,x^{-1}\) inserts or removes \(L_xL_{x^{-1}}\), so freely equal words have the same \(L_w\). For a reduced word \(v\), \(L_v\) sends the empty word to \(v\): if \(v=xv'\), then \(v'\) is reduced and does not begin with \(x^{-1}\), and by induction \(L_v(\varnothing)=L_x(v')=xv'\).

If \(w\) is freely equal to reduced words \(v\) and \(v'\), then \(v=L_v(\varnothing)=L_w(\varnothing)=L_{v'}(\varnothing)=v'\). Cancellations shorten a word, so a sequence of cancellations continued as long as possible stops at a reduced word freely equal to \(w\), which is therefore \(\rho(w)\). \(\square\)

**Lemma 1.2** (the free group). The reduced words with the product \(v\cdot v'=\rho(vv')\) form a group \(F(S)\), the *free group* on \(S\), with the empty word as identity and \(v^{-1}\) as the inverse of \(v\). For words \(w,w'\), \(\rho(ww')=\rho(w)\cdot\rho(w')\). For every group \(G\) and every map \(f:S\to G\) there is exactly one homomorphism \(F(S)\to G\) extending \(f\).

*Proof.* Free equality is compatible with concatenation, so \(ww'\) is freely equal to \(\rho(w)\rho(w')\), and Lemma 1.1 gives \(\rho(ww')=\rho(\rho(w)\rho(w'))\). Hence \(\rho(\rho(uv)w)=\rho(uvw)=\rho(u\rho(vw))\), which is associativity; the empty word is an identity, and \(vv^{-1}\) cancels completely. For \(f\), put \(f(s^{-1})=f(s)^{-1}\) and \(f(x_1\cdots x_n)=f(x_1)\cdots f(x_n)\); inserting or cancelling a pair \(x\,x^{-1}\) does not change the value, so \(f(\rho(w))=f(w)\), and \(f(v\cdot v')=f(vv')=f(v)f(v')\). A homomorphism extending \(f\) is determined on the letters, which generate \(F(S)\). \(\square\)

A word \(w\) also denotes the element \(\rho(w)\) of \(F(S)\), and its image in any quotient.

## 2. Groups given by generators and relators

A *presentation* \(\langle S\mid R\rangle\) consists of a set \(S\) and a set \(R\) of words, the *relators*. The set \(R\) is *symmetrized* if it contains the inverse of each of its words and all their cyclic permutations \(x_i\cdots x_nx_1\cdots x_{i-1}\). The smallest symmetrized set containing \(R\) is written \(\widehat R\). The group of the presentation is
\[
G=\langle S\mid R\rangle=F(S)/N,
\]
where \(N\) is the smallest normal subgroup of \(F(S)\) containing the elements \(\rho(r)\), \(r\in R\). The image of a word \(w\) in \(G\) is written \(\overline w\).

**Lemma 2.1.** \(N\) consists of the elements \(\rho(u_1r_1u_1^{-1}\cdots u_kr_ku_k^{-1})\) with \(k\ge0\), words \(u_i\) and \(r_i\in\widehat R\), and \(\langle S\mid\widehat R\rangle=\langle S\mid R\rangle\). So \(\overline w=1\) exactly when \(w\) is freely equal to such a product.

*Proof.* Let \(P\) be the set of these elements. It is closed under products, under inverses, because \((uru^{-1})^{-1}=ur^{-1}u^{-1}\) with \(r^{-1}\in\widehat R\), and under conjugation, because \(v(uru^{-1})v^{-1}=(vu)r(vu)^{-1}\). So \(P\) is a normal subgroup containing \(\rho(R)\). Conversely, a normal subgroup containing \(\rho(r)\) contains \(\rho(r^{-1})\) and the cyclic permutations of \(r\), since
\[
\begin{gathered}
x_i\cdots x_nx_1\cdots x_{i-1}=v^{-1}rv,\\
v=x_1\cdots x_{i-1},
\end{gathered}
\]
in \(F(S)\); so it contains \(\rho(\widehat R)\) and hence \(P\). Thus \(N=P\), and \(\widehat R\) has the same normal closure as \(R\). \(\square\)

For a word \(w\) with \(\overline w=1\), its *area* is the least \(k\) in such an expression with \(r_i\in\widehat R\).

## 3. Walks and backtracking

A *graph* is given by a set of darts with a fixed-point-free involution \(\theta\) and a tail for each dart; the head of \(d\) is the tail of \(\theta d\), and the edges are the pairs \(\{d,\theta d\}\). The underlying graph of a map is an example. Walks, closed walks and reverses are as in [Plane maps](plane-maps.md). A *backtrack* in a walk is a pair of consecutive darts \(d,\theta d\). Two walks are *homotopic* if one is obtained from the other by finitely many insertions and deletions of backtracks; homotopic walks have the same ends. A walk without backtracks is *reduced*.

**Lemma 3.1.** Every walk is homotopic to exactly one reduced walk. If \(c\simeq c'\) and \(c''\) continues them, then \(cc''\simeq c'c''\), and similarly on the left. For a vertex \(v\) of a graph \(Y\), the homotopy classes of closed walks at \(v\) form a group \(\pi_1(Y,v)\) under concatenation, the inverse of the class of \(c\) being the class of its reverse.

*Proof.* Choose for each edge one of its darts as a symbol \(s\) and write the other as \(s^{-1}\). A walk becomes a word in these symbols, a backtrack becomes a cancelling pair, and deleting a backtrack from a walk leaves a walk, because \(d\) and \(\theta d\) together return to the tail of \(d\). By Lemma 1.1 the cancellations of a walk \(c\), continued as long as possible, end at the unique reduced word freely equal to \(c\), which is a reduced walk; any reduced walk homotopic to \(c\) is a reduced word freely equal to \(c\), so it is this one. Concatenation is compatible with insertions and deletions, and a walk followed by its reverse cancels completely. \(\square\)

**Lemma 3.2** (labels). Let the darts of a graph be labelled by letters with \(\mathrm{lab}(\theta d)=\mathrm{lab}(d)^{-1}\), and let the label of a walk be the word of the labels of its darts. Homotopic walks have freely equal labels.

*Proof.* A backtrack \(d,\theta d\) has the label \(x\,x^{-1}\) with \(x=\mathrm{lab}(d)\). \(\square\)

A *cycle* in a graph is a connected subgraph in which every vertex has degree two, a loop counting twice: a loop, two edges joining the same two vertices, or a closed walk through at least three distinct vertices without repeated vertices. A *tree* is a connected graph without cycles.

**Lemma 3.3** (trees). In a tree, every closed walk is homotopic to the empty walk.

*Proof.* Let \(c=(d_1,\ldots,d_n)\) be a reduced closed walk with \(n\ge1\) in some graph. Choose \(i\le j\) with \(\mathrm{tail}(d_i)=\mathrm{head}(d_j)\) and \(j-i\) as small as possible; \(i=1\), \(j=n\) is a candidate. Then the tails of \(d_i,\ldots,d_j\) are distinct. If \(j=i\), the dart \(d_i\) is a loop. If \(j=i+1\), the darts \(d_i\) and \(d_{i+1}\) run between the same two distinct vertices in opposite directions, and \(d_{i+1}\ne\theta d_i\) because \(c\) is reduced, so they lie on two different edges joining these vertices. If \(j\ge i+2\), the walk \(d_i,\ldots,d_j\) passes through at least three distinct vertices and returns, and its edges join distinct pairs of consecutive vertices. In each case the edges form a cycle. So a tree has no reduced closed walk of positive length, and by Lemma 3.1 every closed walk in it is homotopic to its reduced form, the empty walk. \(\square\)

## 4. Cayley graphs

**Definition 4.1.** The *Cayley graph* \(X\) of \(G=\langle S\mid R\rangle\) has the vertex set \(G\) and, for each \(g\in G\) and each letter \(x\), a dart \((g,x)\) from \(g\) to \(g\overline x\), labelled \(x\), with
\[
\theta(g,x)=(g\overline x,\,x^{-1}) .
\]
This \(\theta\) is an involution without fixed points, and \(\mathrm{lab}(\theta d)=\mathrm{lab}(d)^{-1}\).

**Lemma 4.2** (determinism). For each vertex \(g\) and each letter \(x\), exactly one dart leaves \(g\) with the label \(x\). Hence for each word \(w\) there is exactly one walk from \(g\) with label \(w\); it ends at \(g\overline w\), and it is closed exactly when \(\overline w=1\).

*Proof.* The dart is \((g,x)\). The walk is built letter by letter, and its end is \(g\) multiplied by the images of the letters. \(\square\)

A *label-preserving map* from a labelled graph \(Y\) to \(X\) sends vertices to vertices and darts to darts, compatibly with tails, with \(\theta\) and with labels.

**Lemma 4.3** (label-preserving maps). Let \(Y\) be a connected labelled graph, \(v\) a vertex of \(Y\) and \(h\in G\). A label-preserving map \(\kappa:Y\to X\) with \(\kappa(v)=h\) exists exactly when every closed walk at \(v\) has a label \(w\) with \(\overline w=1\). It is then unique, and \(\kappa(u)=h\overline w\) for the label \(w\) of any walk from \(v\) to \(u\).

*Proof.* A label-preserving map sends a walk from \(v\) with label \(w\) to a walk from \(h\) with label \(w\), which ends at \(h\overline w\) by Lemma 4.2. So \(\kappa(u)=h\overline w\) for every walk from \(v\) to \(u\), which proves uniqueness, and a closed walk at \(v\) goes to a closed walk at \(h\), so its label satisfies \(\overline w=1\).

Conversely, suppose the condition holds. For two walks \(c,c'\) from \(v\) to \(u\) with labels \(w,w'\), the closed walk \(c\) followed by the reverse of \(c'\) has the label \(ww'^{-1}\), so \(\overline w=\overline{w'}\), and \(\kappa(u)=h\overline w\) is well defined because \(Y\) is connected. A dart \(d\) from \(u\) to \(u'\) goes to the dart \((\kappa(u),\mathrm{lab}(d))\), which ends at \(\kappa(u)\overline{\mathrm{lab}(d)}=\kappa(u')\); and \(\theta d\) goes to \((\kappa(u'),\mathrm{lab}(d)^{-1})=\theta(\kappa(u),\mathrm{lab}(d))\). \(\square\)

## 5. Exercises

**5.1.** Find \(\rho(w)\) for \(w=s\,t\,t^{-1}\,s^{-1}\,s\,t\,s^{-1}\,s\) by two different orders of cancellation, and compute \(L_w(\varnothing)\) letter by letter.

**5.2.** Let \(G=\langle s,t\mid sts^{-1}t^{-1}\rangle\). Show that \(s^at^b\mapsto(a,b)\) is an isomorphism \(G\to\mathbb Z^2\), and that the Cayley graph is the square grid: the vertices \((a,b)\), with \(s\)-darts to \((a+1,b)\) and \(t\)-darts to \((a,b+1)\).

**5.3.** In Lemma 4.3, show that the condition need only be checked on a set of closed walks at \(v\) whose classes generate \(\pi_1(Y,v)\).

**5.4.** Show that a reduced closed walk at \(v\) in a graph \(Y\) maps under a label-preserving map to a closed walk in \(X\) which need not be reduced, but whose label is freely equal to the label of the original walk.

## 6. Solutions

**5.1.** Cancelling \(t\,t^{-1}\) gives \(s\,s^{-1}\,s\,t\,s^{-1}\,s\); then \(s\,s^{-1}\) at the front gives \(s\,t\,s^{-1}\,s\), and \(s^{-1}\,s\) at the end gives \(s\,t\). Cancelling first \(s^{-1}\,s\) at the end and then the other pairs also ends at \(s\,t\). Letter by letter from the right: \(L_s(\varnothing)=s\), \(L_{s^{-1}}(s)=\varnothing\), \(L_t(\varnothing)=t\), \(L_s(t)=st\), \(L_{s^{-1}}(st)=t\), \(L_{t^{-1}}(t)=\varnothing\), \(L_t(\varnothing)=t\), \(L_s(t)=st\). So \(L_w(\varnothing)=st=\rho(w)\).

**5.2.** The map \(s\mapsto(1,0)\), \(t\mapsto(0,1)\) extends to \(F(S)\to\mathbb Z^2\) by Lemma 1.2, and the relator goes to \(0\), so it factors through \(G\). In \(G\), \(ts=st\), so every element is \(\overline{s^at^b}\); and \(s^at^b\mapsto(a,b)\) is injective on these, so the map is an isomorphism. The dart \((g,s)\) runs from \((a,b)\) to \((a+1,b)\), and \((g,t)\) to \((a,b+1)\).

**5.3.** If \(c\simeq c'\), their labels are freely equal (Lemma 3.2) and have the same image in \(G\); and the label of a concatenation is the product of the labels. So the set of classes whose labels map to \(1\) is a subgroup of \(\pi_1(Y,v)\), and it is everything once it contains a generating set.

**5.4.** The image walk has the same label, letter by letter. It is reduced exactly when no two consecutive letters cancel, since in \(X\) the dart after \((g,x)\) is \(\theta(g,x)\) exactly when the next letter is \(x^{-1}\); a reduced walk in \(Y\) may well have a cancelling pair of labels, for instance a closed walk around two edges with labels \(x\) and \(x^{-1}\) between the same two vertices.

## References

- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Section 1.A (graphs and free groups) and Section 1.3 (Cayley complexes), on the author's page. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
- [Bridson] M. R. Bridson, *The geometry of the word problem*, in: Invitations to Geometry and Topology, Oxford University Press, 2002, Section 1 (presentations, products of conjugates of relators and the area of a word, Definition 1.2.2), on the author's page. https://people.maths.ox.ac.uk/bridson/papers/bfs/bfs.pdf
