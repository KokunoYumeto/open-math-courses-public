# Thin triangles, overlap balls and the residual forest

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Different embedded copies of components of the cover overlap in the Cayley graph. For the operator comparison at the end of the course, each copy must receive a domain disjoint from the others, at the cost of removing one finite ball per copy, and the Cayley edges outside these domains must form a forest. The tool is the coned graph \(\widehat X\): its triangles are uniformly thin, a fact proved here from short *chain* fillings with an explicit constant, by integrating a discrete one-form around a loop [OpenAI-KK, Lemma 7.6]. Thin triangles give short paths avoiding a center, short paths give intrinsic distance bounds in a copy, and ordering the copies by the distance of their centers from a root confines all earlier overlaps of a copy to one ball [OpenAI-KK, Sections 7.3 and 7.4].

- Short chain fillings (Section 1).
- Thin triangles from chain fillings (Section 2).
- Avoidance (Section 3).
- One ball for all earlier overlaps (Section 4).
- Cycle coordinates and the residual forest (Section 5).
- The incidence count (Section 6).

The setting of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md) is in force: the cover \(P\) with the girth condition (2.1) there, the group \(\Gamma\), its formal Cayley graph \(X\), the embedded indexed copies \(Q\), the coned graph \(\widehat X\) with centers \(c_Q\), and the minimal diagrams of problem (b) with Lemmas 5.1, 6.1 and 7.2 there. Distances without subscript are distances in \(\widehat X\); \(d_Q\) is the graph distance of the copy \(Q\).

## 1. Short chain fillings

For a walk \(\gamma\) in a graph, its *chain* is the sum of its oriented edges, with the convention that an oriented edge plus its reverse is zero.

**Lemma 1.1** (short chain fillings; [OpenAI-KK, Lemma 7.5]). The chain of every closed walk of length \(n\) in \(\widehat X\) is a sum of at most \(12n\) chains of closed walks of length at most four.

*Proof.* Rotate the walk to start at a group vertex, which does not change its chain, and divide it into sides: \(m\le n\) sides. Take a minimal diagram of problem (b), so that \(b\le6m\) by Lemma 6.1 of the previous lesson. For each arc choose a *standard path* between the images of its ends: the generator edge if the arc has an incidence on a fixed side, and otherwise the two-spoke passage through the center of the copy of one of its incidences, reversed for the reverse arc.

On a bounded face, replace the standard path of each incident arc by the passage through the center of the copy of that face. Each replacement changes the chain by the chain of a closed walk of length at most four, and the passages through one center telescope around the face to zero. On an adjustable side, the same replacements with the center of that side telescope to the side itself; fixed sides are their own standard paths. The chain of the exterior standard path is the sum of the chains of the standard paths around the bounded faces, since the two incidences of each internal arc cancel. Altogether the chain of the walk is a sum of chains of closed walks of length at most four, one for each incidence of an arc on a bounded face or an adjustable side: at most \(2b\le12m\le12n\). \(\square\)

## 2. Thin triangles from chain fillings

A *geodesic triangle* consists of three vertices and geodesics between them, its *sides*. It is \(D_0\)-*thin* if every vertex on a side has distance at most \(D_0\) from a vertex on one of the other two sides.

**Lemma 2.1** (thin triangles; [OpenAI-KK, Lemma 7.6]). Let \(G\) be a connected graph with unit edges in which the chain of every closed walk of length \(n\) is a sum of at most \(12n\) chains of closed walks of length at most four. Then every geodesic triangle of \(G\) is \(D_0\)-thin with \(D_0=10^6\).

*Proof.* Fix a geodesic triangle with sides \([x,y]\), \([x,w]\), \([y,w]\), of lengths \(n=d(x,y)\), \(u=d(x,w)\), \(v=d(y,w)\), and put \(a=\frac12(n+u-v)\) and \(b=u-a=v-(n-a)\). Let \(R\) be the largest distance from a vertex of a side to the union of the other two sides; we may assume \(R\ge100\). Relabel so that it is attained at \(z\in[x,y]\), at position \(j=d(x,z)\). Then every vertex of the other two sides has distance at least \(R\) from \(z\); in particular \(j\ge R\) and \(n-j\ge R\). Positions on a side are distances from its first named end.

*Three positional rules.* (i) A position \(h<a-R\) on \([x,y]\) is within \(R\) of \([x,w]\). By the definition of \(R\) it is within \(R\) of one of the other sides; if it were within \(R\) of the position \(t\) of \([y,w]\), then \(t\ge n-h-R\) and \(u\le h+R+(v-t)\le2h+2R+v-n\), that is, \(h\ge a-R\). (ii) Symmetrically, a position \(h>a+R\) on \([x,y]\) is within \(R\) of \([y,w]\). (iii) A position \(k>a+R\) on \([x,w]\) is within \(R\) of \([y,w]\): if it were within \(R\) of the position \(h\) of \([x,y]\), then \(h\ge k-R\) and \(v\le(u-k)+R+(n-h)\), at most \(u+n-2k+2R\), that is, \(k\le a+R\).

*A loop around \(z\).* We construct a segment \([h_-,h_+]\) of \([x,y]\) with \(j-h_-\ge R\) and \(h_+-j\ge R\), and an *alternate path* from \(h_+\) to \(h_-\) whose vertices have distance at least \(R\) from \(z\), so that together they form a closed walk of length at most \(200R\). A *bridge* is a path of length at most \(R\) from a position of one side to a vertex of another, given by the positional rules; a bridge from a vertex at distance at least \(4R\) from \(z\) stays at distance at least \(3R\) from \(z\).

If \(j<a-6R\), take \(h_-=\max(0,j-4R)\) and \(h_+=j+4R<a-2R\). By rule (i), both ends have bridges to \([x,w]\), where we take the trivial bridge at \(x\) if \(h_-=0\); join the bridge ends along \([x,w]\). The bridge ends have positions within \(R\) of \(h_\pm\), so this piece of \([x,w]\) has length at most \(h_+-h_-+2R\le10R\), and the closed walk has length at most \(20R\). The case \(j>a+6R\) is symmetric.

If \(|j-a|\le6R\), take \(h_-=\max(0,\lfloor a-10R\rfloor)\) and \(h_+=\min(n,\lceil a+10R\rceil)\), so that \(j-h_-\ge4R\) and \(h_+-j\ge4R\) unless they are clipped at \(x\) or \(y\). Bridge \(h_-\) to \([x,w]\) by rule (i) and \(h_+\) to \([y,w]\) by rule (ii), trivially at a clipped end, and let \(s_-\) and \(t_+\) be the positions of the bridge ends on \([x,w]\) and \([y,w]\). Then \(|s_--h_-|\le R\), \(|t_+-(n-h_+)|\le R\), \(a-h_-\le10R+1\) and \(h_+-a\le10R+1\). If \(b\le20R+2\), join the bridge ends through \(w\): the two pieces have lengths \(u-s_-\le31R+3\) and \(v-t_+\le31R+3\), and the closed walk has length at most \(84R+8\). If \(b>20R+2\), take the vertex \(A\in[x,w]\) at position \(k=\lceil a+20R\rceil<u\). By rule (iii) it has a bridge to a vertex \(B\in[y,w]\) at a position \(t\), and comparing distances to \(w\), \(|(u-k)-(v-t)|\le R\), so \(|t-(n-a+20R)|\le R+1\). The alternate path goes from \(h_+\) across its bridge to \(t_+\), along \([y,w]\) to \(t\), across the bridge to \(A\), and along \([x,w]\) back to \(s_-\) and across the last bridge to \(h_-\); the two pieces along the sides have lengths at most \(32R+2\) and \(31R+2\), and the closed walk has length at most \(86R+6\). The bridge from \(A\) stays far from \(z\), because \(d(z,A)\ge k-j\ge14R\).

In every case the vertices of the alternate path lie on the other two sides, at distance at least \(R\) from \(z\), or on bridges, at distance at least \(3R\).

*A one-form.* Put \(r_0=\lfloor R/4\rfloor\) and divide the closed walk into four consecutive paths, consecutive ones sharing an end: \(I_1\) is the segment of \([x,y]\) from position \(j-r_0\) to \(j+r_0\), \(I_2\) the segment from \(j+r_0\) to \(h_+\), \(I_3\) the alternate path from \(h_+\) to \(h_-\), and \(I_4\) the segment from \(h_-\) to \(j-r_0\). Then
\[
\begin{gathered}
d(I_1,I_3)\ge R-r_0\ge\tfrac R3,\\
d(I_2,I_4)=2r_0\ge\tfrac R2-2\ge\tfrac R3 ,
\end{gathered}
\]
the second because \(I_2\) and \(I_4\) lie on one geodesic. Put \(q_0=R/3\) and
\[
\begin{gathered}
f(p)=\min\{q_0,d(p,I_1)\},\\
g(p)=\min\{q_0,d(p,I_2)\},
\end{gathered}
\]
\(1\)-Lipschitz functions of vertices, and on an oriented edge from \(p\) to \(p'\)
\[
\omega(p,p')=\frac{f(p)+f(p')}2\,\bigl(g(p')-g(p)\bigr),
\]
which changes sign with the orientation. So \(\omega\) pairs with chains, and its sum along a closed walk depends only on the chain. Along the four paths, \(f=0\) on \(I_1\), \(g=0\) on \(I_2\), \(f=q_0\) on \(I_3\) and \(g=q_0\) on \(I_4\), so only \(I_3\) contributes, and the sum of \(\omega\) around the closed walk is \(q_0(g(h_-)-g(h_+))=q_0^2\). On a closed walk of length at most four, subtracting the value of \(f\) at its first vertex does not change the sum, because the increments of \(g\) sum to zero; afterwards \(|f|\le2\) on the walk and each increment of \(g\) is at most \(1\), so the sum has absolute value at most \(16\). By hypothesis, the chain of the closed walk of length at most \(200R\) is a sum of at most \(12\cdot200R\) such chains, so
\[
\Bigl(\frac R3\Bigr)^2\le16\cdot12\cdot200R ,
\]
and \(R\le345600<10^6\). Geodesics exist between any two vertices, since path lengths are integers; no local finiteness is used. \(\square\)

**Corollary 2.2.** Every geodesic triangle of \(\widehat X\) is \(D_0\)-thin, \(D_0=10^6\).

*Proof.* Lemmas 1.1 and 2.1. \(\square\)

## 3. Avoidance

**Lemma 3.1** (a short path avoiding one center; [OpenAI-KK, Lemma 7.7]). Fix an integer \(L\ge1\). For large \(\ell\), uniformly in the copy \(Q\) and the layer \(i\): if a walk in \(\widehat X\) of length at most \(L\) joins vertices \(u,x\) of \(Q\), with \(u\) over layer \(i\), and does not visit \(c_Q\), then
\[
d_Q(u,x)\le24(L+1)L_i .\tag{3.1}
\]

*Proof.* Close the walk by the passage \(x\to c_Q\to u\), the *designated side*; there are at most \(L+1\) sides, and only the designated one passes through \(c_Q\). Take a minimal diagram of problem (b). Every arc occurrence on the designated side is shorter than \(L_j\), for the layer \(j\) of its first vertex. If its other incidence is a bounded face, this is Lemma 6.1 of the previous lesson; if it is a fixed side, the arc has length one; if it is another adjustable side, that side passes through a different center, and a long arc would make the two copies equal by Lemma 7.2 of the previous lesson. An arc with both incidences on the designated side is impossible: its edges are exterior bridges, and the part of the designated side between the two traversals of such a bridge is an excursion, without side breaks, whose ends have equal images; since \(Q\) is embedded, its source ends coincide, and the excursion, the bridge and the part they enclose can be removed, which keeps the faces and lowers the number of edges.

So the designated side consists of at most \(2b\le12(L+1)\) arc occurrences, each shorter than its local \(L_j\). After a prefix of length \(t\), the next layer \(j\) has \(H_j\le H_i+t\), so the next arc has length at most \(L_i+100t/\log_2d\). By induction over at most \(12(L+1)\) arcs, all the ratios \(H_j/H_i\) are bounded by a quantity that tends to \(1\) as \(\ell\to\infty\), so each arc has length at most \(2L_i\) for large \(\ell\). The image of the designated side is a walk in \(Q\) from \(x\) to \(u\) of length at most \(24(L+1)L_i\). \(\square\)

## 4. One ball for all earlier overlaps

Put
\[
\begin{gathered}
L^*=4D_0+8,\quad C_*=10^7(L^*+1),\\
C_\bullet=2\cdot10^4(L^*+1) .
\end{gathered}
\]
The thin-triangle constant \(D_0\) does not depend on \(C_*\), so there is no circularity; in particular \(C_*\ge10^4\), as Lemma 6.1 of the previous lesson requires.

**Proposition 4.1** (one ball for all earlier overlaps; [OpenAI-KK, Proposition 7.8]). For large \(\ell\) there is a well-order of the indexed copies and, in each copy \(Q\), a ball \(B(Q)\) of \(Q\) with the following properties.

1. Every vertex that \(Q\) shares with an earlier copy lies in \(B(Q)\).
2. The edges of \(Q\) with at least one end in \(B(Q)\) form a forest.
3. If \(B(Q)\) contains a vertex over layer \(i\), then \(|V(B(Q))|\le\mathfrak w_i=2^{C_\bullet H_i}\).

*Proof.* Fix a group vertex \(o\). There are countably many indexed copies: \(P\) has countably many components, and a label map from a component is fixed by one value. Enumerate them, and order the copies by \(d(c_Q,o)\), then by the enumeration; this is a well-order. For each copy choose once a geodesic from \(c_Q\) to \(o\), and let \(u\in Q\) be its vertex after \(c_Q\).

Let \(x\in Q\) lie in a different copy with center \(B'\) and \(d(B',o)\le d(c_Q,o)=k\). Centers are not adjacent, so \(c_Q,x,B'\) is a geodesic, and a geodesic from \(B'\) to \(o\) avoids \(c_Q\), since through \(c_Q\) it would have length \(2+k\). If \(k<D_0+3\), the walk from \(x\) to \(B'\), to \(o\), and back along the chosen geodesic to \(u\) avoids \(c_Q\) and has length at most \(1+k+(k-1)=2k\). If \(k\ge D_0+3\), let \(p\) be the vertex at distance \(t=D_0+3\) from \(c_Q\) on the chosen geodesic. The vertices of the side \(c_Q,x,B'\) of the geodesic triangle \(c_Q,B',o\) are at distance more than \(D_0\) from \(p\), so by Corollary 2.2, \(p\) is within \(D_0\) of a vertex \(q\) of the geodesic from \(B'\) to \(o\); a shortest walk from \(p\) to \(q\) avoids \(c_Q\), because \(d(p,c_Q)=t>D_0\). Also \(d(B',q)=d(B',o)-d(q,o)\), which is at most \(k-(k-t-D_0)=t+D_0\). The walk from \(x\) to \(B'\), along the geodesic to \(q\), across to \(p\), and along the chosen geodesic to \(u\) avoids \(c_Q\) and has length at most \(2t+2D_0\). In both cases the length is at most \(L^*\).

Let \(i\) be the layer of \(u\), and let \(B(Q)\) be the ball of radius \(R_Q=\lceil25(L^*+1)L_i\rceil\) about \(u\) in \(Q\). By Lemma 3.1 with \(L=L^*\), every vertex shared with an earlier copy lies in \(B(Q)\); the center \(u\) does not depend on the earlier copy.

If the ball, with all edges of \(Q\) between its vertices, contained a cycle, a shortest-path tree from \(u\) and one more edge would give a circuit of length at most \(2R_Q+1\); a vertex outside with two edges into the ball would give one of length at most \(2R_Q+2\). All layers met differ from \(i\) by at most \(R_Q+1\), so \(H_j\ge H_i/2\) for large \(\ell\), and since \(R_Q\le2500(L^*+1)H_i/\log_2d+1\), such a circuit, a cyclically nonbacktracking closed walk of the component, would have length less than \(C_*H_j/\log_2d\), against the girth condition. So the ball is a tree and every outside vertex has at most one edge into it, which proves 2.

The copy has maximum degree at most \(6D\), so \(|V(B(Q))|\le(1+6D)^{R_Q+1}\), and \(\log_2(1+6D)\le3\log_2d\) for large \(\ell\). Hence, for every layer \(j\) met in the ball,
\[
\begin{aligned}
&\log_2|V(B(Q))|\\
&\quad\le7500(L^*+1)H_i+6\log_2d\\
&\quad\le8000(L^*+1)H_i\\
&\quad\le16000(L^*+1)H_j\\
&\quad\le C_\bullet H_j .\qquad\square
\end{aligned}
\]

## 5. Cycle coordinates and the residual forest

For a field \(k\), let \(Z_1(G;k)\) be the space of finitely supported \(k\)-valued cycles of a graph \(G\), with a fixed orientation of each edge.

**Proposition 5.1** (direct cycle coordinates; [OpenAI-KK, Proposition 7.9]). Inclusion of the copies induces an isomorphism
\[
\begin{gathered}
\bigoplus_QZ_1(Q;k)\longrightarrow Z_1(X;k),\\
(c_Q)_Q\longmapsto\sum_Qc_Q .
\end{gathered}
\]

*Proof.* A finitely supported cycle is a combination of the chains of finitely many circuits: choose a spanning forest of its support, subtract the circuit of each other edge with the right coefficient, and note that a cycle supported on a finite forest is zero, by removing leaves. A closed walk in \(X\) reads a word trivial in \(\Gamma\), so it bounds a diagram whose faces carry source walks in \(P\); the label maps of the diagram give each face its copy, and the chain of the exterior is the sum of the chains of the faces. This proves surjectivity. For injectivity, let \(\sum_Qc_Q=0\) with finitely many nonzero terms, and let \(Q\) be the latest copy with \(c_Q\ne0\). Every edge in the support of \(c_Q\) occurs in another term, of an earlier copy, so both its ends lie in \(B(Q)\), and \(c_Q\) is a cycle supported on the tree \(B(Q)\); so \(c_Q=0\), a contradiction. \(\square\)

**Proposition 5.2** (assigned domains and the residual forest; [OpenAI-KK, Proposition 7.10]). Put \(D_Q=V(Q)\setminus\bigcup_{Q'<Q}V(Q')\), and let \(E_{\mathrm{int}}\) be the set of edges of copies \(Q\) with both ends in \(D_Q\). The sets \(D_Q\) are pairwise disjoint, \(V(Q)\setminus D_Q\subseteq V(B(Q))\), each edge of \(E_{\mathrm{int}}\) belongs to this set for exactly one \(Q\), and the graph \((V(X),E(X)\setminus E_{\mathrm{int}})\) is a forest.

*Proof.* If \(Q'<Q\), a vertex of \(Q'\) is not in \(D_Q\); this gives disjointness, and with it the uniqueness for internal edges. The inclusion is Proposition 4.1(1). If the remaining graph contained a circuit, its chain over \(\mathbb F_2\) would be a nonzero cycle \(c=\sum_Qc_Q\), by Proposition 5.1. Let \(Q\) be the latest copy with \(c_Q\ne0\). An edge of \(c_Q\) with both ends outside \(B(Q)\) occurs in no earlier term, so it has a nonzero coefficient in \(c\); but both its ends lie in \(D_Q\), so it was deleted. Hence \(c_Q\) is supported on the edges meeting \(B(Q)\), which form a forest by Proposition 4.1(2), and \(c_Q=0\), a contradiction. \(\square\)

## 6. The incidence count

The *type* of a vertex \(x\) of an indexed copy \(Q\) is the base vertex in \(Y\) under its source vertex; it does not depend on the representative of \(Q\).

**Proposition 6.1** (the incidence count; [OpenAI-KK, Proposition 7.11]). The map \((Q,x)\mapsto(x,\operatorname{type}_Q(x))\) is a bijection from the set of pairs of an indexed copy and one of its vertices onto \(\Gamma\times V(Y)\). It intertwines left translation by \(\Gamma\) on copies and on the first coordinate.

*Proof.* Given \(x\in\Gamma\) and \(v\in V(Y)\), let \(C\) be the component of \((v,1_F)\) and \(\phi\) the label map of \(C\) with \(\phi(v,1_F)=x\); this is an incidence of type \(v\) at \(x\). Conversely, a representative of an incidence of type \(v\) at \(x\) has its source vertex \((v,f)\); applying \(\delta_{f^{-1}}\) and changing the map accordingly, which is the equivalence of indexed copies, moves the source vertex to \((v,1_F)\), and then the map is the one just constructed. Left translation changes \(x\) and leaves the component and its vertex \((v,1_F)\) unchanged. \(\square\)

For nonnegative numbers \(a_v\) on the base vertices put \(a_Q(x)=a_{\operatorname{type}_Q(x)}\) and
\[
\mathcal S_a=\sum_{i\in\mathbb Z}\mathfrak w_i\sum_{v\text{ in layer }i}a_v .
\]

**Corollary 6.2** (weighted sums). For every copy \(Q\) and every \(x\in\Gamma\),
\[
\begin{gathered}
\sum_{y\in B(Q)}a_Q(y)\le\mathcal S_a,\\
\sum_{Q:\,x\in V(Q)\setminus D_Q}|V(B(Q))|\,a_Q(x)\le\mathcal S_a .
\end{gathered}
\]

*Proof.* A base vertex in layer \(i\) occurs at most \(|V(B(Q))|\le\mathfrak w_i\) times among the types in \(B(Q)\). In the second sum every incidence has \(x\in B(Q)\), so \(|V(B(Q))|\le\mathfrak w_i\) for the layer \(i\) of its type, and by Proposition 6.1 each type occurs at most once at \(x\). \(\square\)

## 7. Exercises

**7.1** (easy). Check the identity \(b=u-a=v-(n-a)\) and show that \(0\le a\le n\).

**7.2** (medium). Show that in the infinite \(3\)-regular tree every geodesic triangle is \(0\)-thin, and that a cycle of length \(4k\) contains geodesic triangles that are not \((k-1)\)-thin.

**7.3** (medium). In the proof of Lemma 2.1, compute the sum of \(\omega\) around a closed walk of length four whose vertices \(p_0,p_1,p_2,p_3\) have \(f=(0,1,2,1)\) and \(g=(0,1,1,0)\).

**7.4** (medium). Give an example of two indexed copies whose images in \(X\) share an edge, and explain why their cycle spaces still form a direct sum.

## 8. Solutions

**7.1.** \(u-a=\frac12(u-n+v)\) and \(v-(n-a)=\frac12(v-n+u)\). By the triangle inequality \(v\le n+u\) and \(u\le n+v\), so \(0\le a\le n\).

**7.2.** In a tree the three geodesics between three vertices are unions of the paths to a common branch point, so every vertex of a side lies on one of the other sides. In a cycle of length \(4k\), let \(x\) and \(y\) be antipodal, \(w\) the vertex at distance \(k\) from both, the short sides the arcs through \(w\), and the side \([x,y]\) the arc of length \(2k\) through the other half of the cycle. Its middle vertex has distance \(k\) from \(x\) and from \(y\), and distance more than \(k\) from every other vertex of the short sides, so the triangle is not \((k-1)\)-thin.

**7.3.** \(\omega(p_0,p_1)=\frac12\cdot1=\frac12\), \(\omega(p_1,p_2)=\frac32\cdot0=0\), \(\omega(p_2,p_3)=\frac32\cdot(-1)=-\frac32\), \(\omega(p_3,p_0)=\frac12\cdot0=0\); the sum is \(-1\), within the bound \(16\).

**7.4.** Two distinct copies may share the edges of a path of length less than \(L_i\) (Lemma 7.2 of the previous lesson). Their shared edges lie in the ball of the later copy, which is a tree, so a nonzero cycle of the later copy cannot be cancelled by cycles of the earlier one.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 7.3 and 7.4, Lemmas 7.5, 7.6 and 7.7, Propositions 7.8 to 7.11. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
