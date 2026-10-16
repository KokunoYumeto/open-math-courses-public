# Van Kampen's lemma

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagram over a presentation is a plane map whose darts carry letters and whose bounded faces read relators. Diagrams are named after E. R. van Kampen, who introduced them to study relations in groups; Bridson's survey [Bridson] recounts their history in its introduction and proves van Kampen's lemma for diagrams in the plane in its Section 4. This lesson proves van Kampen's lemma in three parts: a word that is a product of \(k\) conjugates of relators has a diagram with at most \(k\) bounded faces (Theorem 3.1); the exterior walk of a diagram is homotopic to a product of conjugates of its face walks, one for each bounded face (Theorem 4.1); and every closed walk in a diagram has a label that represents the identity, so that the diagram maps to the Cayley graph (Theorem 5.1). Together they show that a word represents the identity exactly when it has a diagram, and that its area is the least number of bounded faces of such a diagram. Plane maps and their operations are those of [Plane maps](plane-maps.md); words, presentations, walks and Cayley graphs those of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md).

## 1. Diagrams

Throughout, \(\langle S\mid R\rangle\) is a presentation with \(R\) symmetrized, \(G\) its group and \(X\) its Cayley graph.

**Definition 1.1.** A *labelled plane map* is a plane map \(D\) with a letter \(\mathrm{lab}(d)\) for each dart \(d\), such that \(\mathrm{lab}(\theta d)=\mathrm{lab}(d)^{-1}\). It is a *diagram over* \(\langle S\mid R\rangle\) if the boundary walk of every bounded face has its label in \(R\). A *base* of \(D\) is a dart \(o_1\) of the outer face, or nothing if \(D\) is trivial. The boundary walk of the outer face read from \(o_1\) is the *exterior walk*, the empty walk at the vertex of a trivial map; its label is the *exterior word*, and the tail of \(o_1\) is the *base vertex*. A diagram with a base is a diagram *for* its exterior word, and its *area* is its number of bounded faces.

Reading a boundary walk from another dart permutes its label cyclically, and the reverse of a boundary walk has the inverse label; since \(R\) is symmetrized, the condition on a bounded face does not depend on where and in which direction it is read.

**Example 1.2.** The trivial map is a diagram for the empty word. A single edge \(\{p,q\}\) with \(\mathrm{lab}(p)=x\) has the one face \((p,q)\) (Proposition 3.1 of [Plane maps](plane-maps.md)); with the base \(p\) it is a diagram of area \(0\) for \(x\,x^{-1}\). A single loop with the faces \((g_1)\) and \((g_2)\) and \(\mathrm{lab}(g_1)=x\), with \((g_1)\) as outer face, is a diagram of area \(1\) for the word \(x\) if \(x^{-1}\in R\).

## 2. Three operations

In the exterior walk \((o_1,\ldots,o_m)\) of a diagram with \(m\ge1\), the *corner after* \(o_i\) is the corner \((o_i,o_{i+1})\) of the outer face, indices modulo \(m\); the corner after \(o_m\) is the *base corner*.

**Lemma 2.1** (bouquets). Let \(u_1,\ldots,u_k\) be words and \(r_1,\ldots,r_k\) nonempty words in \(R\). There is a diagram of area \(k\) for
\[
u_1r_1u_1^{-1}\cdots u_kr_ku_k^{-1} .
\]

*Proof.* We build diagrams \(D_i\) of area \(i\) for \(W_i=u_1r_1u_1^{-1}\cdots u_ir_iu_i^{-1}\), starting with the trivial map \(D_0\). Each new edge below gets the stated letter on its first dart, the one leaving the part already built, and the inverse letter on the other dart. The base is kept, except that the first dart added to the trivial map becomes the base.

Let \(u=u_{i+1}=y_1\cdots y_n\) and \(r=r_{i+1}=x_1\cdots x_\ell\). First add \(n\) pendant edges (Proposition 3.1 of [Plane maps](plane-maps.md)), the first in the base corner of \(D_i\) (in the trivial map, the first edge itself), each further one in the corner after the previous new dart labelled \(y_j\), which enters a vertex of degree one. Each addition inserts \(y_j\,y_j^{-1}\) into the exterior walk, so the exterior word becomes \(W_i\,y_1\cdots y_n\,y_n^{-1}\cdots y_1^{-1}\). Call \(c_0\) the end of the last dart labelled \(y_n\), or the base vertex if \(n=0\), and \(\gamma\) the corner of the outer face at \(c_0\) between the arrival along \(u\) and the return: the corner after the dart labelled \(y_n\), or the base corner if \(n=0\). If \(n=0\) and \(D_i\) is trivial, there is no corner yet, and the first edge added below is added to the trivial map.

If \(\ell=1\), add a loop with \(\mathrm{lab}(g_1)=x_1\) in the corner \(\gamma\) (Proposition 3.3 there). The exterior word becomes \(W_iux_1u^{-1}\), and the new face \((g_2)\) has the label \(x_1^{-1}\in R\).

If \(\ell\ge2\), add \(\ell-1\) pendant edges labelled \(x_1,\ldots,x_{\ell-1}\) along a path from \(c_0\), the first in \(\gamma\), each further one at the new leaf. The exterior word becomes \(W_i\,u\,x_1\cdots x_{\ell-1}\,x_{\ell-1}^{-1}\cdots x_1^{-1}\,u^{-1}\). Let \(\alpha_1\) be the dart labelled \(x_{\ell-1}\), which enters the last leaf, and \(\alpha_2\) the dart labelled \(x_1^{-1}\), which returns to \(c_0\). Add a chord \(\{g_1,g_2\}\) with \(\mathrm{lab}(g_1)=x_\ell\) between the corners after \(\alpha_1\) and after \(\alpha_2\) (Proposition 3.2 there); \(g_1\) runs from the leaf to \(c_0\). Since \(\varphi(\alpha_1)=\theta\alpha_1\) (Proposition 1.2(2) there), the outer face splits into
\[
\begin{gathered}
(g_1,\ \varphi(\alpha_2),\ \ldots,\ \alpha_1),\\
(g_2,\ \theta\alpha_1,\ \ldots,\ \alpha_2).
\end{gathered}
\]
The first consists of \(g_1\) followed by the old exterior walk from \(\varphi(\alpha_2)\) to \(\alpha_1\), which leaves out the return path \(x_{\ell-1}^{-1},\ldots,x_1^{-1}\). Declared outer and read from the base, its word is \(W_i\,u\,x_1\cdots x_{\ell-1}x_\ell\,u^{-1}=W_{i+1}\). The second is \(g_2\) followed by the return path, with the label \(x_\ell^{-1}x_{\ell-1}^{-1}\cdots x_1^{-1}=r^{-1}\in R\). In both cases one bounded face is added, so \(D_{i+1}\) has area \(i+1\). \(\square\)

**Lemma 2.2** (inserting a cancelling pair). If \(D\) is a diagram for \(w=w_1w_2\) and \(x\) is a letter, there is a diagram with the same bounded faces for \(w_1\,x\,x^{-1}\,w_2\).

*Proof.* If \(D\) is trivial, take the single edge of Example 1.2. Otherwise add a pendant edge \(\{p,q\}\) with \(\mathrm{lab}(p)=x\) (Proposition 3.1 of [Plane maps](plane-maps.md)) in the corner after the last dart of \(w_1\), keeping the base, or, if \(w_1\) is empty, in the base corner, taking \(p\) as the new base. The exterior walk gains \(p,q\) at that place. \(\square\)

**Lemma 2.3** (cancelling a pair). If \(D\) is a diagram for \(w=w_1\,x\,x^{-1}\,w_2\), there is a diagram for \(w_1w_2\) whose bounded faces are bounded faces of \(D\), with their labels; in particular its area is at most the area of \(D\).

*Proof.* Let \((o_1,\ldots,o_m)\) be the exterior walk and \(d_1=o_j\), \(d_2=o_{j+1}\) the two darts of the pair, where \(j-1\) is the length of \(w_1\). Let \(v_0\) be the tail of \(d_1\), \(v_1\) its head, which is the tail of \(d_2\), and \(v_2\) the head of \(d_2\). If \(m=2\), the trivial map is a diagram for the empty word \(w_1w_2\). Let \(m\ge3\), and let \(a\) be the dart before \(d_1\) and \(b\) the dart after \(d_2\) in the exterior walk; \(a\ne d_2\) and \(b\ne d_1\) because \(m\ge3\). Each case below produces a diagram whose outer face is the outer face of \(D\) with \(d_1\) and \(d_2\) removed, possibly with one dart replaced by another dart with the same label, and whose bounded faces are bounded faces of \(D\) with the same labels. Its base is \(o_1\) if \(j\ge2\) and \(b=o_3\) if \(j=1\), or the dart that replaces it; in each case the new exterior word is \(w_1w_2\).

*Case 1: \(d_2=\theta d_1\).* Then \(v_1\) has degree one (Proposition 1.2(2) of [Plane maps](plane-maps.md)). Delete the edge of \(d_1\): by Proposition 2.2 there, with the outer face written \((d_1,\theta d_1,b,\ldots,a)\), the component of \(v_1\) is the single vertex \(v_1\), and the other component is a plane map with the outer face \((b,\ldots,a)\) and all the bounded faces of \(D\).

*Case 2: \(d_2\ne\theta d_1\).* Add a chord \(\{g_1,g_2\}\) in the outer face \(O\) between the corner after \(a\) and the corner after \(d_2\) (Proposition 3.2 there, with \(\alpha_1=a\) and \(\alpha_2=d_2\)); its label plays no role. As \(\varphi(a)=d_1\) and \(\varphi(d_2)=b\), the outer face splits into
\[
O'=(g_1,b,\ldots,a),\qquad T=(g_2,d_1,d_2),
\]
and we declare \(O'\) outer. The dart \(g_1\) runs from \(v_0\) to \(v_2\).

*Case 2a: \(v_0\ne v_2\).* The chord is not a loop; contract it (Proposition 2.3 there). The outer face becomes \((b,\ldots,a)\), which is \(O\) without \(d_1\) and \(d_2\); the face \(T\) becomes \((d_1,d_2)\), of length two; the other faces keep their boundary walks. Now delete the edge \(e_2=\{d_2,\theta d_2\}\). Its dart \(d_2\) lies in \((d_1,d_2)\), and \(\theta d_2\) lies in another face \(f_2=(\theta d_2,c_1,\ldots,c_s)\), because \(\theta d_2\ne d_1,d_2\). By Proposition 2.1 there, the two faces merge into \((d_1,c_1,\ldots,c_s)\): the face \(f_2\) with \(\theta d_2\) replaced by \(d_1\), which has the same label \(x\). If \(f_2\) is the outer face, the outer face is \(O\) without \(d_1,d_2\) and with \(\theta d_2\) replaced by \(d_1\); otherwise the outer face is \(O\) without \(d_1,d_2\), and the bounded face \(f_2\) keeps its label.

*Case 2b: \(v_0=v_2\).* The chord is a loop at \(v_0\), with \(g_1\) in the outer face \(O'\) and \(g_2\) in \(T\ne O'\). Cut along it (Proposition 4.1 of [Plane maps](plane-maps.md)): the result is a plane map whose outer face is \(O'\) without \(g_1\), that is \((b,\ldots,a)\), and whose bounded faces are bounded faces of \(D\), lying on the side of the loop that contains \(O'\), with their boundary walks. The faces on the other side, \(T\) among them, are discarded. \(\square\)

The two cases of Case 2 are the combinatorial form of the argument for diagrams in the plane in [Bridson, Lemma 4.2.3], where an arc joining the ends of the cancelling pair encloses a disc that is collapsed onto it, or, when the pair is already closed, the enclosed region is removed.

## 3. Constructing diagrams

**Theorem 3.1** (van Kampen's lemma, construction). Let \(w\) be a word that is freely equal to \(u_1r_1u_1^{-1}\cdots u_kr_ku_k^{-1}\) with \(r_i\in R\). Then \(w\) has a diagram with at most \(k\) bounded faces.

*Proof.* A factor with \(r_i\) empty is freely trivial and can be omitted, so we may assume all \(r_i\) nonempty. Lemma 2.1 gives a diagram of area \(k\) for the product \(P\). Cancel pairs in its exterior word one at a time by Lemma 2.3, as long as there are any; by Lemma 1.1 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md) this ends with a diagram for \(\rho(P)=\rho(w)\), of area at most \(k\). Now let \(w=w^{(0)},w^{(1)},\ldots,w^{(t)}=\rho(w)\) be the words of a sequence of cancellations from \(w\) to its normal form. Going backwards, \(w^{(i-1)}\) is obtained from \(w^{(i)}\) by inserting a cancelling pair, and Lemma 2.2 turns a diagram for \(w^{(i)}\) into one for \(w^{(i-1)}\) with the same bounded faces. At the end we have a diagram for \(w\) of area at most \(k\). \(\square\)

## 4. Reading diagrams

**Theorem 4.1** (van Kampen's lemma, reading the boundary). Let \(D\) be a labelled plane map with a base, base vertex \(v\) and bounded faces \(f_1,\ldots,f_F\). The exterior walk is homotopic in \(D\) to a product \(c_1\cdots c_F\) of closed walks at \(v\) with
\[
c_i=A_i\,B_i\,A_i^{\mathrm{rev}},
\]
where \(A_i\) is a walk from \(v\), \(A_i^{\mathrm{rev}}\) its reverse, and \(B_i\) the boundary walk of \(f_i\) read from one of its darts, or the reverse of such a walk. In particular the exterior word is freely equal to a product of \(F\) conjugates of the labels of the bounded faces or of their inverses; for a diagram over \(\langle S\mid R\rangle\), to a product of \(F\) conjugates of relators.

*Proof.* Induction on the number of edges. If \(F=0\), the underlying graph is a tree or a single vertex (Proposition 1.3 of [Plane maps](plane-maps.md)), and the closed exterior walk is homotopic to the empty walk by Lemma 3.3 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md).

Let \(F\ge1\). The dual map has the faces of \(D\) as vertices and is connected (Lemma 2.1 of [Sphere maps](course:barnettes-conjecture/sphere-maps)); it has \(F+1\ge2\) vertices, so some dual edge joins the outer face \(O\) to another face. That is, some edge \(e=\{d,\theta d\}\) has \(d\in O\) and \(\theta d\) in a bounded face \(f=(\theta d,b_1,\ldots,b_q)\). Write the exterior walk as \(A\,d\,B\) with \(A=(o_1,\ldots,o_{j-1})\), \(d=o_j\) and \(B=(o_{j+1},\ldots,o_m)\). The walk \(b=(b_1,\ldots,b_q)\) runs from the tail of \(d\) to its head, since \(\theta d\) runs back.

By Proposition 2.1 of [Plane maps](plane-maps.md), \(D-e\) is a plane map whose outer face is the cyclic sequence \((o_{j+1},\ldots,o_m,o_1,\ldots,o_{j-1},b_1,\ldots,b_q)\) and whose bounded faces are the \(f_i\) other than \(f\), with the same boundary walks. Read from \(o_1\) if \(j\ge2\), and otherwise from the first dart of \(b\,B\) (if any), its exterior walk is the closed walk \(A\,b\,B\) at \(v\). By induction, \(A\,b\,B\) is homotopic in \(D-e\), and hence in \(D\), to a product of \(F-1\) closed walks of the required form for the faces other than \(f\). In \(D\), inserting backtracks gives
\[
\begin{aligned}
A\,d\,B&\simeq A\,d\,b^{\mathrm{rev}}\,b\,B\\
&\simeq\bigl(A\,(d\,b^{\mathrm{rev}})\,A^{\mathrm{rev}}\bigr)\,\bigl(A\,b\,B\bigr),
\end{aligned}
\]
and \(d\,b^{\mathrm{rev}}\) is the reverse of the boundary walk of \(f\), read from \(d\). The statement on labels follows from Lemma 3.2 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md), because the label of \(A\,B\,A^{\mathrm{rev}}\) is \(\mathrm{lab}(A)\,\mathrm{lab}(B)\,\mathrm{lab}(A)^{-1}\) and \(R\) is symmetrized. \(\square\)

**Corollary 4.2.** A word \(w\) represents the identity of \(G\) exactly when it has a diagram over \(\langle S\mid R\rangle\), and then its area is the least area of a diagram for \(w\).

*Proof.* By Theorem 4.1, a diagram of area \(F\) for \(w\) writes \(w\) as a product of \(F\) conjugates of relators, so \(\overline w=1\) and the area of \(w\) is at most \(F\) (Lemma 2.1 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md)). Conversely, Theorem 3.1 turns an expression with \(k\) conjugates into a diagram of area at most \(k\). \(\square\)

## 5. Diagrams in the Cayley graph

**Theorem 5.1** (van Kampen's lemma, the map to the Cayley graph). In a diagram over \(\langle S\mid R\rangle\), the label \(w\) of every closed walk satisfies \(\overline w=1\). Consequently, if \(v\) is the base vertex, then for every vertex \(h\) of the Cayley graph \(X\) there is exactly one label-preserving map \(\kappa:D\to X\) with \(\kappa(v)=h\).

*Proof.* We prove the first statement for every labelled plane map whose bounded faces have labels in \(R\), by induction on the number of edges. If there are no bounded faces, the underlying graph is a tree or a single vertex (Proposition 1.3 of [Plane maps](plane-maps.md)), every closed walk is homotopic to the empty walk (Lemma 3.3 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md)), and its label is freely trivial (Lemma 3.2 there).

Otherwise choose \(e=\{d,\theta d\}\) and \(f=(\theta d,b_1,\ldots,b_q)\) as in the proof of Theorem 4.1. The label of \(f\) lies in \(R\), so \(\overline{\mathrm{lab}(\theta d)}\;\overline{\mathrm{lab}(b)}=1\), that is, \(\overline{\mathrm{lab}(b)}=\overline{\mathrm{lab}(d)}\), and \(b\) runs from the tail of \(d\) to its head. In a closed walk \(c\), replace every occurrence of \(d\) by \(b\) and every occurrence of \(\theta d\) by \(b^{\mathrm{rev}}\). The result is a closed walk \(c'\) in \(D-e\) with \(\overline{\mathrm{lab}(c')}=\overline{\mathrm{lab}(c)}\). By Proposition 2.1 of [Plane maps](plane-maps.md), \(D-e\) is a labelled plane map whose bounded faces are bounded faces of \(D\), with labels in \(R\), and it has fewer edges; so \(\overline{\mathrm{lab}(c')}=1\) by induction.

The diagram is connected, and its closed walks at \(v\) have labels representing \(1\); Lemma 4.3 of [Words, free groups and Cayley graphs](words-free-groups-and-cayley-graphs.md) gives the map \(\kappa\) and its uniqueness. \(\square\)

## 6. Uses in the programme

The course [A projection of irrational trace and the Baum–Connes conjecture](course:irrational-trace-and-baum-connes/graphical-presentations-and-coned-diagrams) states two lists of facts about diagrams and plane maps in Section 3 of its lesson Graphical presentations and coned diagrams, and the courses [A torsion-free counterexample to the Kadison–Kaplansky conjecture](course:kadison-kaplansky-projections/the-conjecture-and-scalar-compression) and [A torsion-free counterexample to reduced Baum–Connes injectivity](course:reduced-baum-connes-injectivity/the-reduced-assembly-map-and-the-torus-class) use them through it. Their proofs are here: the three parts of (VK) are Theorem 3.1, Theorem 4.1 and Theorem 5.1, and the four parts of (MAP) are Proposition 1.2, Proposition 2.1, Proposition 2.2 and Proposition 2.3 of [Plane maps](plane-maps.md), where a plane graph is a plane map in the sense of Definition 1.1 there.

## 7. Exercises

**7.1.** For \(\langle s\mid s^n\rangle\), \(n\ge1\), with \(R\) the words \(s^n\) and \(s^{-n}\), describe a diagram of area two for \(s^{2n}\), and show that the area of \(s^{2n}\) is two.

**7.2.** Show that if every relator has even length, then every word representing the identity of \(G\) has even length.

**7.3.** Let \(D\) be a diagram for \(w\) with base \(o_1\), and let \(o_i\) be another dart of the outer face. Show that \(D\) with the base \(o_i\) is a diagram for a cyclic permutation of \(w\), and conclude that cyclic permutations of a word representing the identity have the same area.

**7.4.** Follow the proof of Theorem 3.1 for \(\langle s,t\mid R\rangle\) with \(R\) the symmetrization of \(sts^{-1}t^{-1}\), the word \(w=ts\,t^{-1}s^{-1}\) and the expression \(w=u\,r\,u^{-1}\) with \(u=t\) and \(r=s\,t^{-1}s^{-1}t\): build the bouquet, cancel, and count the faces.

## 8. Solutions

**7.1.** The bouquet of Lemma 2.1 for two copies of the factor \(s^n\) with empty \(u\) consists of two cycles of length \(n\) at the base vertex (loops if \(n=1\)), each with a bounded face labelled \(s^{-n}\); its exterior word is \(s^{2n}\), so the area is at most two. In the free group on \(s\), a product of \(k\) conjugates of \(s^{\pm n}\) equals \(s^{n\epsilon}\) with \(\epsilon\) a sum of \(k\) signs, because the free group on one letter is abelian. For \(s^{2n}\) this sum is \(2\), so \(k\ge2\), and the area is two.

**7.2.** In a diagram for \(w\), the lengths of all boundary walks add up to \(2E\) (Proposition 1.2(1) of [Plane maps](plane-maps.md)). The bounded faces have relator labels of even length, so the exterior walk, of length \(|w|\), has even length. By Corollary 4.2 every word representing the identity has a diagram.

**7.3.** The outer face and the bounded faces are unchanged, and reading the boundary walk of the outer face from \(o_i\) permutes the exterior word cyclically. So a diagram for \(w\) gives a diagram of the same area for each cyclic permutation, and conversely; by Corollary 4.2 the areas agree.

**7.4.** The bouquet: a pendant edge labelled \(t\) from the base vertex to \(c_0\), a path labelled \(s\), \(t^{-1}\), \(s^{-1}\) from \(c_0\), and a chord labelled \(t\) closing it at \(c_0\). Its exterior word is \(t\,s\,t^{-1}s^{-1}t\,t^{-1}\), and the bounded face reads \(r^{-1}=t^{-1}sts^{-1}\). The last two letters \(t\,t^{-1}\) cancel: their darts are the chord, from the end of the path to \(c_0\), and the reverse of the stem, from \(c_0\) to the base vertex. This is Case 2a of Lemma 2.3. Contracting the new chord identifies the base vertex with the end of the path; deleting the stem merges the face of length two into the outer face, where the chord takes the place of the base dart, with the same label \(t\). The result is a square with exterior word \(ts\,t^{-1}s^{-1}=w\), read from the chord, and one bounded face. As \(w\) is reduced and not empty, it is not freely trivial, so its area is one.

## References

- [Bridson] M. R. Bridson, *The geometry of the word problem*, in: Invitations to Geometry and Topology, Oxford University Press, 2002, Introduction and Section 4 (singular disc diagrams, Proposition 4.1.2, van Kampen's lemma, Theorem 4.2.2, and Lemmas 4.2.3 and 4.2.6), on the author's page. https://people.maths.ox.ac.uk/bridson/papers/bfs/bfs.pdf
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Section 1.2 (presentations of fundamental groups) and Section 1.3 (Cayley complexes), on the author's page. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
