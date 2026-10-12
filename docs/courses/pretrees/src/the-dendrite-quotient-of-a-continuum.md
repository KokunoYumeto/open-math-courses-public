# The dendrite quotient of a continuum

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *continuum* is here a compact connected Hausdorff space. Its cut points arrange it like a tree: the space is a pretree ([Cut points of a connected space](cut-points-of-a-connected-space.md)). This lesson turns that arrangement into a space. Every continuum \(M\) has a quotient \(D\) in which two points are identified unless a set of cut points ordered like the rational numbers separates them, and:

- \(D\) is a continuum, and the quotient map \(M\to D\) has connected fibres; the preimage of every closed connected subset of \(D\) is closed and connected (Theorem 3.4);
- if \(M\) has a countable dense subset, \(D\) is a *dendrite*: a compact metrizable space that is connected and locally connected and contains no simple closed curve (Theorem 4.1);
- in particular, a continuum with a countable dense subset in which any two points are separated by a third point is a dendrite (Corollary 4.2).

The quotient can be a single point; a circle has no cut points at all. Whether it is more than a point is a separate question for each continuum.

The construction passes through the pretrees of the earlier lessons: the set \(T\) of cut points, its completion \(\Phi(T)\), and the dense quotient of the completion. The lesson follows Lemmas 5.15 to 5.21, Proposition 5.22 and Theorem 5.23 of [Bowditch]. It uses [Mapping a pretree to the completion of a subset](mapping-a-pretree-to-the-completion-of-a-subset.md), [The dense quotient of a pretree](the-dense-quotient-of-a-pretree.md), [Quotients of pretrees](quotients-of-pretrees.md), the lesson on cut points, and [Dendrites from pretrees](dendrites-from-pretrees.md).

## 1. The quotient map

Throughout, \(M\) is a compact connected Hausdorff space with the pretree structure of the lesson on cut points, and \(T\) is a set of cut points of \(M\); the main case is the set of all cut points. We use the following objects.

- \(\Phi=\Phi(T)\) is the completion of the pretree \(T\), with betweenness \(\langle prq\rangle\), and \(\bar T\) the set of the flows \(\bar a\) towards points \(a\in T\).
- \(\varphi\colon M\to\Phi\) is the map of the lesson on the map to the completion: \(\varphi(x)\) is the flow of \(T\) towards \(x\), and \(\varphi(a)=\bar a\) for \(a\in T\).
- \(\approx\) is the least codense relation of \(\Phi\), \(\Psi=\Phi/{\approx}\) the dense quotient, and \(\pi\colon\Phi\to\Psi\) the quotient map. The pretree \(\Psi\) is complete, dense and median (Corollary 6.3 of the lesson on the dense quotient).
- \(f=\pi\circ\varphi\colon M\to\Psi\).

**Lemma 1.1.** The map \(f\colon M\to\Psi\) is surjective.

**Proof.** Let \(p\in\Phi\). By Theorem 3.2 of the lesson on the map to the completion, \(p=\varphi(x)\) for some \(x\in M\), or \(p\) is adjacent to \(\bar a=\varphi(a)\) for some \(a\in T\). In the second case the interval between \(p\) and \(\bar a\) in \(\Phi\) is empty and contains no rational subset, so \(p\approx\bar a\) by Theorem 3.3 of the lesson on the dense quotient, and \(\pi(p)=f(a)\). \(\blacksquare\)

**Proposition 1.2.** For \(x,y\in M\): \(f(x)=f(y)\) if and only if the interval \((x,y)\) of the pretree \(M\) contains no rational subset that consists of points of \(T\).

So if \(T\) is the set of all cut points, \(f(x)\ne f(y)\) means that \(x\) and \(y\) are separated by a set of cut points which, in its order from \(x\) to \(y\), is countable, dense and without ends.

**Proof.** \(f(x)=f(y)\) means \(\varphi(x)\approx\varphi(y)\). Write \(p=\varphi(x)\), \(q=\varphi(y)\).

Let \(Q\subseteq T\cap(x,y)\) be a rational subset of \(M\), and \(\bar Q\) the set of the flows \(\bar a\), \(a\in Q\). By Lemma 1.2(1) of the lesson on the map to the completion, \(\bar Q\subseteq[p,q]_\Phi\). Since \(a\mapsto\bar a\) preserves and reflects betweenness, \(\bar Q\) is a rational subset of \(\Phi\). It is infinite, so \(p\ne q\); and it has no least and no greatest element in the direction of \([p,q]_\Phi\), so it contains neither \(p\) nor \(q\). Hence \(\bar Q\subseteq(p,q)_\Phi\), and \(p\approx q\) fails by Theorem 3.3 of the lesson on the dense quotient.

Conversely let \(p\approx q\) fail. By Proposition 6.2 of that lesson there is a rational subset of \(\Phi\) in \((p,q)_\Phi\) that consists of points \(\bar a\) with \(a\) in some set \(Q\subseteq T\). For \(a\in Q\), \(\langle p\,\bar a\,q\rangle\) gives \(xay\), by Lemma 1.2(2) of the lesson on the map to the completion. So \(Q\subseteq T\cap(x,y)\), and \(Q\) is a rational subset of \(M\). \(\blacksquare\)

*The topology.* We give \(\Psi\) the quotient topology of \(f\): a subset \(O\subseteq\Psi\) is open if and only if \(f^{-1}(O)\) is open in \(M\). The set \(\Psi\) with this topology is written \(D\), or \(D_T(M)\). The map \(f\colon M\to D\) is continuous and surjective, so \(D\) is compact and connected. A subset of \(D\) is closed if and only if its preimage in \(M\) is closed.

## 2. Preclosed sets

Let \(S\) be a pretree, \(Q\subseteq S\) a nonempty full subset and \(x\in S\setminus Q\). We say that a point \(y\) *separates \(x\) from \(Q\)* if \(y\notin Q\) and \(xyq\) for all \(q\in Q\). By Lemma 1.1 of the lesson on quotients, applied to the full sets \(\{x\}\) and \(Q\), it suffices that \(y\notin Q\) and \(xyq\) for one \(q\in Q\).

**Definition.** A subset \(Q\) of a pretree \(S\) is *preclosed* if it is nonempty and full, and every point of \(S\setminus Q\) is separated from \(Q\) by some point of \(S\).

**Lemma 2.1.** Let \(R\) be a full relation on a pretree \(S\), with quotient map \(\rho\colon S\to S/R\). If \(\mathcal Q\subseteq S/R\) is preclosed, then \(\rho^{-1}(\mathcal Q)\) is preclosed.

**Proof.** The set \(\rho^{-1}(\mathcal Q)\) is nonempty, and full by Corollary 3.2(2) of the lesson on quotients. Let \(x\) be a point outside it. Then \(\rho(x)\notin\mathcal Q\), so there is a class \(Y\notin\mathcal Q\) between \(\rho(x)\) and a class \(Z\in\mathcal Q\). By the definition of the betweenness of classes there is \(y\in Y\) with \(xyz\) for \(z\in Z\). The point \(y\) is not in \(\rho^{-1}(\mathcal Q)\), and \(xyz\) holds for one point \(z\) of \(\rho^{-1}(\mathcal Q)\). So \(y\) separates \(x\) from \(\rho^{-1}(\mathcal Q)\). \(\blacksquare\)

For distinct points \(x,y\) of a median pretree let
\[
\begin{gathered}
J(x,y)=\{z\mid\operatorname{med}(x,y,z)=y\}\\
=\{z\mid y\in[x,z]\}.
\end{gathered}
\]
The two descriptions agree because \(y\) lies in \([x,y]\) and in \([y,z]\). So \(J(x,y)\) consists of \(y\) and the points beyond \(y\) as seen from \(x\). It is the complement of the set \(H(x,y)\) of the lesson on dendrites from pretrees.

**Lemma 2.2.** Let \(S\) be a dense median pretree.

1. For \(x\ne y\) the set \(J(x,y)\) is preclosed.
2. Every set with one point is preclosed.

**Proof.** (1) *\(J(x,y)\) is full.* Let \(z,z'\in J(x,y)\) and \(w\in[z,z']\), and suppose \(y\notin[x,w]\). In particular \(w\ne y\). For \(u\in\{z,z'\}\) with \(u\ne y\) we have \(xyu\), and (T3) with the point \(w\) gives \(xyw\) or \(uyw\); the first is excluded, so \(y\in(u,w)\), and \(u\ne w\). If \(z\) and \(z'\) both differ from \(y\), then \(w\in(z,z')\) and \(y\in(z,w)\cap(w,z')\), against Lemma 3.2 of the first lesson. If \(z=y\), then \(z'\ne y\), because \(w\ne y\); so \(y\in(z',w)\), while \(w\in[y,z']\) with \(w\ne y\) and \(w\ne z'\) gives \(w\in(z',y)\). This contradicts (T2). The case \(z'=y\) is the same.

*Separation.* Let \(z\notin J(x,y)\), and \(m=\operatorname{med}(x,y,z)\). Then \(m\ne y\), and \(m\) lies in \([x,y]\) and in \([y,z]\). Since \(S\) is dense there is \(w\in(y,m)\). By Lemma 3.2 of the first lesson, \((y,m)\subseteq(y,x)\) and \((y,m)\subseteq(y,z)\). So \(xwy\), which shows \(y\notin[x,w]\), that is, \(w\notin J(x,y)\); and \(zwy\) with \(y\in J(x,y)\). So \(w\) separates \(z\) from \(J(x,y)\).

(2) For \(x\ne q\) choose \(y\in(x,q)\). \(\blacksquare\)

We return to the pretree \(\Phi=\Phi(T)\).

**Lemma 2.3.** Let \(Q\subseteq\Phi\) be preclosed and \(p\in\Phi\setminus Q\). Then there is a point \(a\in T\) such that \(\bar a\) separates \(p\) from \(Q\).

**Proof.** Let \(r\) separate \(p\) from \(Q\). If \(r\in\bar T\), we are done. Otherwise, since \(r\notin Q\), let \(r'\) separate \(r\) from \(Q\). For \(q\in Q\), the relations \(\langle prq\rangle\) and \(\langle rr'q\rangle\) put \(p,r,r',q\) in a row (Lemma 2.3(2) of the first lesson). So \(r'\) separates \(p\) from \(Q\), and if \(r'\in\bar T\), we are done.

Otherwise \(r\) and \(r'\) are different points outside \(\bar T\), and there is \(a\in T\) with \(\langle r\,\bar a\,r'\rangle\) (Lemma 6.1 of the lesson on the dense quotient). For \(q\in Q\): \(\bar a\) lies in \((r,r')_\Phi\subseteq(r,q)_\Phi\subseteq(p,q)_\Phi\), by Lemma 3.2 of the first lesson. And \(\bar a\notin Q\): otherwise \(\langle r\,r'\,\bar a\rangle\), against \(\langle r\,\bar a\,r'\rangle\). So \(\bar a\) separates \(p\) from \(Q\). \(\blacksquare\)

Recall from the lesson on the map to the completion that \(R_M(a,b)\), for \(a\ne b\) in \(M\), is the set of points \(x\) for which \(xab\) fails.

**Proposition 2.4.** Let \(Q\subseteq\Phi\) be preclosed. Then \(\varphi^{-1}(Q)\) is the intersection of the sets \(R_M(a,b)\), taken over all pairs of points \(a\ne b\) of \(T\) such that \(\bar b\) separates \(\bar a\) from \(Q\); it is \(M\) if there is no such pair. Consequently \(\varphi^{-1}(Q)\) is closed and connected.

**Proof.** Let \(x\in\varphi^{-1}(Q)\) and let \((a,b)\) be such a pair. Then \(\langle\bar a\,\bar b\,\varphi(x)\rangle\), so \(abx\) by Lemma 1.2(2) of the lesson on the map to the completion. Hence \(xab\) fails, by (T2), and \(x\in R_M(a,b)\).

Let \(x\notin\varphi^{-1}(Q)\), and \(p=\varphi(x)\). By Lemma 2.3 there is \(a\in T\) such that \(\bar a\) separates \(p\) from \(Q\); and since \(\bar a\notin Q\), there is \(b\in T\) such that \(\bar b\) separates \(\bar a\) from \(Q\). So \((a,b)\) is one of the pairs. For \(q\in Q\), \(\langle p\,\bar a\,q\rangle\) and \(\langle\bar a\,\bar b\,q\rangle\) put \(p,\bar a,\bar b,q\) in a row, so \(\langle\varphi(x)\,\bar a\,\bar b\rangle\). By the same Lemma 1.2(2), \(xab\). So \(x\notin R_M(a,b)\).

Each set \(R_M(a,b)\) with \(a\in T\) is coherent (Lemma 3.1 of the lesson on the map to the completion), and an intersection of coherent sets is coherent (Proposition 5.2(2) of the lesson on cut points). Since \(M\) is compact, a coherent set is closed and connected. \(\blacksquare\)

## 3. The quotient is a continuum

**Lemma 3.1.** Let \(x\ne y\) be points of \(D\). Then \(J(x,y)\) is closed in \(D\), and \(f^{-1}(J(x,y))\) is closed and connected. For every point \(x\in D\), the set \(\{x\}\) is closed and the fibre \(f^{-1}(x)\) is closed and connected.

**Proof.** Let \(Q\) be \(J(x,y)\) or \(\{x\}\). It is preclosed in \(\Psi\) by Lemma 2.2. So \(\pi^{-1}(Q)\) is preclosed in \(\Phi\) by Lemma 2.1, and \(f^{-1}(Q)=\varphi^{-1}(\pi^{-1}(Q))\) is closed and connected by Proposition 2.4. A subset of \(D\) with closed preimage is closed. \(\blacksquare\)

**Lemma 3.2.** \(D\) is a Hausdorff space, and for \(x\ne y\) in \(D\) the set \(H(x,y)\) of points \(w\) with \(\operatorname{med}(x,y,w)\ne y\) is open.

**Proof.** \(H(x,y)\) is the complement of \(J(x,y)\). For \(x\ne y\) choose \(z\in(x,y)\). The open sets \(H(x,z)\ni x\) and \(H(y,z)\ni y\) are disjoint, by Lemma 1.1(1) of the lesson on dendrites from pretrees. \(\blacksquare\)

**Lemma 3.3.** Let \(g\colon X\to Y\) be a continuous surjective map from a compact space onto a Hausdorff space such that \(g^{-1}(y)\) is connected for every \(y\in Y\). Then \(g^{-1}(C)\) is connected for every closed connected set \(C\subseteq Y\).

**Proof.** Suppose \(g^{-1}(C)=A\cup B\) with \(A,B\) disjoint and closed in \(g^{-1}(C)\), hence closed in \(X\) and compact. Each fibre \(g^{-1}(y)\), \(y\in C\), is connected, so it lies in \(A\) or in \(B\). So \(g(A)\) and \(g(B)\) are disjoint, and their union is \(C\). They are compact, hence closed in \(Y\). Since \(C\) is connected, one of them is empty; so \(A\) or \(B\) is empty. \(\blacksquare\)

**Theorem 3.4.** Let \(M\) be a compact connected Hausdorff space and \(T\) a set of cut points of \(M\). Then \(D=D_T(M)\) is a compact connected Hausdorff space, and \(f\colon M\to D\) is a continuous surjective map such that the preimage of every closed connected subset of \(D\) is closed and connected in \(M\).

**Proof.** \(D\) is compact and connected as the image of \(M\), and Hausdorff by Lemma 3.2. The fibres are connected by Lemma 3.1. Apply Lemma 3.3. \(\blacksquare\)

## 4. The quotient is a dendrite

**Theorem 4.1.** Let \(M\) be a compact connected Hausdorff space with a countable dense subset, and \(T\) a set of cut points of \(M\). Then \(D=D_T(M)\) is a dendrite:

1. \(D\) is metrizable, connected and locally connected;
2. for \(x\ne y\) in \(D\) the interval \([x,y]\) of the pretree \(\Psi\) is an arc from \(x\) to \(y\), and it is the only arc in \(D\) from \(x\) to \(y\);
3. \(D\) contains no simple closed curve;
4. a point \(z\) separates \(x\) from \(y\) in the space \(D\) if and only if \(xzy\) in the pretree \(\Psi\). So the pretree \(\Psi\) is the pretree of the connected space \(D\).

**Proof.** The space \(D\) is compact. The image under \(f\) of a countable dense subset of \(M\) is a countable dense subset of \(D\). The pretree \(\Psi\) is complete, dense and median, and the sets \(H(x,y)\) are open by Lemma 3.2. These are the assumptions of Theorem 5.1 of the lesson on dendrites from pretrees, which gives (1), (2) and (3).

(4) Let \(xzy\) in \(\Psi\). Put \(U=H(x,z)\), the set of \(w\) with \(z\notin[x,w]\), and let \(V\) be the set of \(w\) with \(xzw\). Then \(D\setminus\{z\}\) is the disjoint union of \(U\) and \(V\), with \(x\in U\) and \(y\in V\). The set \(U\) is open. The set \(V\) is open too: for \(w\in V\), the open set \(H(w,z)\) contains \(w\), and it lies in \(V\), because for \(w'\in H(w,z)\) axiom (T3), applied to \(xzw\) and the point \(w'\ne z\), gives \(xzw'\) or \(wzw'\), and the second fails. So \(U\,z\,V\) is a separation with \(x\in U\) and \(y\in V\).

Conversely let \(U\,z\,V\) be a separation of the space \(D\) with \(x\in U\) and \(y\in V\). The interval \([x,y]\) is an arc by (2), so it is connected; it contains \(x\) and \(y\), so it is not contained in \(U\) or in \(V\), and it contains \(z\). Since \(z\) is neither \(x\) nor \(y\), this is \(xzy\). \(\blacksquare\)

**Corollary 4.2.** Let \(M\) be a compact connected Hausdorff space with a countable dense subset such that for any two points \(x\ne y\) there is a point \(z\) that separates \(x\) from \(y\). Then \(M\) is a dendrite, and for \(x\ne y\) the points that separate \(x\) from \(y\), together with \(x\) and \(y\), form the only arc from \(x\) to \(y\).

**Proof.** Let \(T\) be the set of all cut points. By assumption the pretree \(M\) is dense, so its least codense relation is equality, and by Theorem 3.3 of the lesson on the dense quotient any two points \(x\ne y\) are separated by a rational subset of \(M\). Its points lie between \(x\) and \(y\), so they are cut points. By Proposition 1.2, \(f\) is injective. So \(f\colon M\to D\) is a continuous bijection from a compact space onto a Hausdorff space, hence a homeomorphism, and \(M\) is a dendrite by Theorem 4.1.

A homeomorphism carries separations to separations. So \(z\) separates \(x\) from \(y\) in \(M\) if and only if \(f(z)\) separates \(f(x)\) from \(f(y)\) in \(D\), which by Theorem 4.1(4) and (2) means that \(f(z)\) is a point of the arc from \(f(x)\) to \(f(y)\) other than its ends. \(\blacksquare\)

**Example 4.3.** (a) A circle has no cut points. Then \(T\) is empty, \(\Phi(T)\) has one point, and \(D\) is a point.

(b) Let \(M=[0,1]\) and \(T\) the set \((0,1)\) of all cut points. Any two points \(x<y\) are separated by the rational numbers between them. By Proposition 1.2, \(f\) is injective, so \(D\) is homeomorphic to \([0,1]\).

(c) Let \(M\) be the union of a circle and a segment that meet in one endpoint \(c\) of the segment. The cut points are the points of the segment other than its free end. Two points of the circle are separated by no cut point, so the circle is mapped to one point; two points of the segment are separated by a rational set of cut points. So \(D\) is homeomorphic to the segment, and \(f\) contracts the circle to the point \(c\).

## 5. Exercises

**5.1.** Let \(M\) be the union of two circles in the plane with one common point \(c\). Determine the cut points of \(M\) and the space \(D\).

**5.2.** In Example 4.3(c), verify with Theorem 3.4 that the preimage of every closed connected subset of \(D\) is connected.

**5.3.** Show that Lemma 3.3 fails without the assumption that the fibres are connected.

**5.4.** Let \(S\) be a dense median pretree and \(x\ne y\). Show that \(J(x,y)\cap J(y,x)=\varnothing\) and that \(J(x,y)\cup J(y,x)\) is the set of points \(z\) for which \(\operatorname{med}(x,y,z)\) is \(x\) or \(y\).

**5.5.** Let \(M\) be as in Theorem 4.1 and \(T\subseteq T'\) two sets of cut points. Show that \(f(x)=f(y)\) for the set \(T'\) implies \(f(x)=f(y)\) for the set \(T\), so that \(D_T(M)\) is the image of \(D_{T'}(M)\) under a surjective map \(g\) with \(g\circ f_{T'}=f_T\), and that \(g\) is continuous.

## 6. Solutions

**5.1.** Removing \(c\) leaves two disjoint open arcs, so \(c\) is a cut point. Removing another point \(z\) leaves a connected set: the circle through \(z\) without \(z\) is connected and contains \(c\), and so is the other circle. So \(T=\{c\}\). The pretree \(T\) has one point, its only flow is the empty relation, and \(\Phi(T)\) and \(D\) are single points.

**5.2.** Identify \(D\) with the segment \(S\) and \(f\) with the map that is the identity on \(S\) and sends the circle \(C\) to \(c\). A closed connected subset of \(S\) is a closed subsegment \(I\). If \(c\notin I\), the preimage is \(I\); if \(c\in I\), it is \(I\cup C\), a union of two connected sets with the common point \(c\).

**5.3.** Let \(X=[0,1]\), \(Y\) a circle, and \(g\) the map that winds \([0,1]\) once around the circle, with \(g(0)=g(1)\); the fibre of this point has two points. A closed arc \(C\) of the circle with \(g(0)\) in its interior has the preimage \([0,s]\cup[t,1]\) with \(s<t\), which is not connected.

**5.4.** If \(z\) lay in both sets, \(y\in[x,z]\) and \(x\in[y,z]\). Then \(z\) is neither \(x\) nor \(y\), since \(y\notin[x,x]\) and \(x\notin[y,y]\); so \(xyz\) and \(yxz\), against (T2). The second statement is the definition: \(z\in J(x,y)\) means \(\operatorname{med}(x,y,z)=y\), and \(z\in J(y,x)\) means \(\operatorname{med}(y,x,z)=x\).

**5.5.** By Proposition 1.2, \(f_{T'}(x)=f_{T'}(y)\) means that \((x,y)\) contains no rational subset of points of \(T'\); then it contains none of points of \(T\). So \(g\) is well defined by \(g(f_{T'}(x))=f_T(x)\), and it is surjective because \(f_T\) is. For an open set \(O\subseteq D_T(M)\), the preimage of \(g^{-1}(O)\) under \(f_{T'}\) is \(f_T^{-1}(O)\), which is open; so \(g^{-1}(O)\) is open in the quotient topology.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 5. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
