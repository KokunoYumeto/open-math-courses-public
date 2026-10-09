# The extremal argument and its consequences

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Corollary 3.2 of [Blowing up by transitive tournaments](blowing-up-by-transitive-tournaments.md), a counterexample to the second neighborhood conjecture would produce a nonempty finite oriented graph \(G\) in which every vertex has an in-neighbor and
\[
|U|+|F^2(U)|<2|F(U)|\qquad(\varnothing\ne U\subsetneq V(G)). \tag{0.1}
\]
This lesson shows that no such graph exists (Theorem 2.1), which proves the conjecture (Theorem 3.1). The argument works with sets of ordered pairs of vertices. Applying \(F\) to the first coordinates of a set of pairs, column by column, turns (0.1) into an inequality for the whole set; applying \(F\) to the second coordinates, row by row, gives a second one. An extremal choice of two sets of pairs, together with the pruning theorem of [Ranks, matchings and pruning](ranks-matchings-and-pruning.md), then yields a contradiction. Sections 4 and 5 derive weighted forms of the theorem and consequences for directed triangles.

## 1. Sets of pairs

Let \(G\) be a nonempty finite oriented graph with vertex set \(X\) and image operator \(F\). For \(S\subseteq X\times X\) define
\[
F_1S=\{(i,j):(p,j)\in S\text{ and }p\to i\text{ for some }p\},\qquad F_2S=\{(i,j):(i,s)\in S\text{ and }s\to j\text{ for some }s\},
\]
and \(F_1^2=F_1\circ F_1\), \(F_2^2=F_2\circ F_2\). The *column* of \(S\) at \(j\) is \(S^{(j)}=\{p:(p,j)\in S\}\), and the *row* of \(S\) at \(i\) is \(S_{(i)}=\{s:(i,s)\in S\}\). Let \(\Delta=\{(v,v):v\in X\}\).

**Lemma 1.1.** For every \(S\subseteq X\times X\) and \(i,j\in X\),
\[
(F_1S)^{(j)}=F(S^{(j)}),\quad(F_1^2S)^{(j)}=F^2(S^{(j)}),\quad(F_2S)_{(i)}=F(S_{(i)}),\quad(F_2^2S)_{(i)}=F^2(S_{(i)}).
\]

*Proof.* By definition, \(i\in(F_1S)^{(j)}\) if and only if \(p\to i\) for some \(p\in S^{(j)}\), that is, \(i\in F(S^{(j)})\). Applying this twice gives the second identity, and the last two are proved in the same way with rows. \(\square\)

In the language of [Ranks, matchings and pruning](ranks-matchings-and-pruning.md), regard the members of a set \(P\subseteq X\times X\) as left members and those of \(Q\subseteq X\times X\) as right members, for the relation \(\to\) of \(G\). Then \(F_1P\) is the set of points covered by members of \(P\), and \(F_2Q\) the set covered by members of \(Q\). Since a left and a right member conflict exactly when they cover a common point, \(P\) and \(Q\) have no conflicting pair if and only if \(F_1P\cap F_2Q=\varnothing\). We then call the pair \((P,Q)\) *compatible*.

**Lemma 1.2.** The pair \((\Delta,\Delta)\) is compatible.

*Proof.* A point \((i,j)\in F_1\Delta\cap F_2\Delta\) would satisfy \(j\to i\) (from \((j,j)\in\Delta\)) and \(i\to j\) (from \((i,i)\in\Delta\)), which is impossible in an oriented graph. \(\square\)

**Lemma 1.3.** Suppose every vertex of \(G\) has an in-neighbor, and let \((P,Q)\) be compatible with \(\Delta\subseteq P\cap Q\). Then every column of \(P\) and every row of \(Q\) is a nonempty proper subset of \(X\).

*Proof.* The column \(P^{(j)}\) contains \(j\). If \(P^{(j)}=X\), then \((F_1P)^{(j)}=F(X)=X\) by Lemma 1.1, because every vertex has an in-neighbor. Choose \(w\to j\). Then \((w,j)\in F_1P\), and also \((w,j)\in F_2\Delta\subseteq F_2Q\), since \((w,w)\in Q\) and \(w\to j\). This contradicts compatibility. Similarly, the row \(Q_{(i)}\) contains \(i\); if \(Q_{(i)}=X\), then \(\{i\}\times X\subseteq F_2Q\), and for \(w\to i\) the point \((i,w)\) lies in \(F_1\Delta\subseteq F_1P\), a contradiction. \(\square\)

## 2. Strictly concave growth is impossible

**Theorem 2.1.** There is no nonempty finite oriented graph \(G\) in which every vertex has an in-neighbor and (0.1) holds for every nonempty proper set \(U\) of vertices.

*Proof.* Suppose \(G\) is such a graph, with vertex set \(X\). For a compatible pair \((P,Q)\) put
\[
M(P,Q)=|P|+|Q|,\qquad d(P,Q)=|X|^2-|F_1P|-|F_2Q| .
\]
By compatibility, \(d(P,Q)\) is the number of points of \(X\times X\) lying in neither \(F_1P\) nor \(F_2Q\). Among the compatible pairs with \(\Delta\subseteq P\cap Q\), which exist by Lemma 1.2 and are finite in number, choose one for which \(M+d\) is as large as possible, and write \(M=M(P,Q)\), \(d=d(P,Q)\).

*Step 1: the strict inequalities for \(P\) and \(Q\).* By Lemma 1.3, (0.1) applies to every column of \(P\) and every row of \(Q\). Summing over the columns and using Lemma 1.1, and doing the same with rows,
\[
|P|+|F_1^2P|<2|F_1P|,\qquad|Q|+|F_2^2Q|<2|F_2Q| . \tag{2.1}
\]
The inequalities are strict because \(X\ne\varnothing\).

*Step 2: two large families.* Let
\[
\mathcal R=(X\times X)\setminus F_2^2Q,\qquad\mathcal C=(X\times X)\setminus F_1^2P .
\]
By (2.1),
\[
|\mathcal R|+|\mathcal C|=2|X|^2-|F_2^2Q|-|F_1^2P|>2|X|^2+M-2|F_1P|-2|F_2Q|=M+2d . \tag{2.2}
\]

*Step 3: the diagonal survives and conflicts with nothing.* If \((v,v)\in F_2^2Q\), there are \(s\) with \(s\to v\) and \((v,s)\in F_2Q\); but \((s,s)\in P\) and \(s\to v\) give \((v,s)\in F_1P\), contrary to compatibility. Hence \(\Delta\subseteq\mathcal R\), and symmetrically \(\Delta\subseteq\mathcal C\): if \((v,v)\in F_1^2P\), there is \(p\to v\) with \((p,v)\in F_1P\), while \((p,p)\in Q\) gives \((p,v)\in F_2Q\).

Regard \(\mathcal R\) as left members and \(\mathcal C\) as right members. Suppose the left member \((v,v)\) conflicts with a right member \((i,s)\), so \(v\to i\) and \(s\to v\). Starting from \((s,s)\in P\), the arc \(s\to v\) gives \((v,s)\in F_1P\), and then \(v\to i\) gives \((i,s)\in F_1^2P\), contrary to \((i,s)\in\mathcal C\). Suppose a left member \((p,j)\) conflicts with the right member \((v,v)\), so \(p\to v\) and \(v\to j\). Starting from \((p,p)\in Q\), we get \((p,v)\in F_2Q\) and then \((p,j)\in F_2^2Q\), contrary to \((p,j)\in\mathcal R\). Hence every diagonal member, on either side, conflicts with nothing.

*Step 4: the opposite points are uncovered.* Let \((p,j)\in\mathcal R\) and \((i,s)\in\mathcal C\) conflict, so \(p\to i\) and \(s\to j\), with opposite point \((p,s)\). If \((p,s)\in F_1P\), choose \((u,s)\in P\) with \(u\to p\); then \(u\to p\to i\) puts \((i,s)\) into \(F_1^2P\), which is impossible. If \((p,s)\in F_2Q\), choose \((p,t)\in Q\) with \(t\to s\); then \(t\to s\to j\) puts \((p,j)\) into \(F_2^2Q\), which is impossible. Therefore the set \(H\) of opposite points satisfies
\[
H\subseteq(X\times X)\setminus(F_1P\cup F_2Q),\qquad|H|\le d . \tag{2.3}
\]

*Step 5: pruning gives a better pair.* Theorem 3.1 of [Ranks, matchings and pruning](ranks-matchings-and-pruning.md) gives \(P'\subseteq\mathcal R\) and \(Q'\subseteq\mathcal C\) without conflicts between them, keeping every member that conflicts with nothing, such that the number of deleted members is at most \(|H|\) plus the number of shared points covered by no member of \(P'\cup Q'\). By Step 3, \(\Delta\subseteq P'\cap Q'\), and \((P',Q')\) is compatible. A point is covered by a member of \(P'\) exactly when it lies in \(F_1P'\), and by a member of \(Q'\) exactly when it lies in \(F_2Q'\); so at most \(d'=d(P',Q')\) points are covered by no member of \(P'\cup Q'\). With (2.3),
\[
|\mathcal R\setminus P'|+|\mathcal C\setminus Q'|\le d+d' .
\]
Using (2.2),
\[
M(P',Q')+d'\ge|\mathcal R|+|\mathcal C|-(d+d')+d'>M+2d-d=M+d,
\]
contradicting the choice of \((P,Q)\). \(\square\)

The quantity \(d\) is what makes the argument close: the uncovered shared points that the pruning theorem charges are paid for by the increase of \(d'\), and the opposite points are paid for by the old \(d\) through (2.3).

## 3. The second neighborhood theorem

**Theorem 3.1** (OpenAI 2026; Seymour's second neighborhood conjecture). Every nonempty finite oriented graph has a vertex \(v\) with \(|N_1^+(v)|\le|N_2^+(v)|\).

*Proof.* If some nonempty finite oriented graph had no such vertex, Corollary 3.2 of [Blowing up by transitive tournaments](blowing-up-by-transitive-tournaments.md) would provide a graph excluded by Theorem 2.1. \(\square\)

## 4. Weighted forms

Seacrest showed that the conjecture is equivalent to versions with weights on arcs and on vertices [Sea12], as recounted in [OpenAI-SN]. With Theorem 3.1 established, these versions hold; we derive them directly from Theorem 3.1. For a function \(\eta\) on vertices and a set \(S\), write \(\eta(S)=\sum_{x\in S}\eta(x)\).

**Theorem 4.1** (Arc weights). Let \(D\) be a nonempty finite oriented graph and \(w:A(D)\to[0,\infty)\); put \(w(xy)=0\) when \((x,y)\) is not an arc. For vertices \(v,s\) let
\[
\beta_v(s)=\max\Bigl(\{0\}\cup\{w(us)-w(vs):u\in V(D),\ v\to u\to s\}\Bigr).
\]
Then some vertex \(v\) satisfies
\[
\sum_{s\in V(D)}\beta_v(s)\ge\sum_{u\in N_1^+(v)}w(vu).
\]

Arcs of weight \(0\) are arcs of \(D\) and are used in the definition of \(\beta_v\).

*Proof.* *Integer weights.* Suppose all weights are integers. For \(s\in V(D)\) let \(K_s=\max(\{1\}\cup\{w(us):u\to s\})\). Let \(D^w\) be the oriented graph with vertices \((s,k)\), \(s\in V(D)\), \(1\le k\le K_s\), and arcs \((u,l)\to(s,k)\) whenever \(u\to s\) in \(D\) and \(k\le w(us)\). It has no loops, and opposite arcs would require opposite arcs in \(D\).

Fix a vertex \((v,l)\). Its out-neighbors are the \((u,k)\) with \(v\to u\) and \(k\le w(vu)\), so \(|N_1^+((v,l))|=\sum_{u\in N_1^+(v)}w(vu)\). A walk \((v,l)\to(u,k)\to(s,k')\) exists exactly when \(v\to u\to s\), \(w(vu)\ge1\) and \(k'\le w(us)\). Let \(m_v(s)\) be the largest \(w(us)\) over the \(u\) with \(v\to u\to s\) and \(w(vu)\ge1\), and \(m_v(s)=0\) if there is no such \(u\). The walks of length two from \((v,l)\) end at the \((s,k')\) with \(k'\le m_v(s)\); none of them is in the block of \(v\), because \(D\) has no walk \(v\to u\to v\). Among these, \((s,k')\) is an out-neighbor exactly when \(v\to s\) and \(k'\le w(vs)\). Hence
\[
|N_2^+((v,l))|=\sum_s\max\bigl(0,\,m_v(s)-w(vs)\bigr)\le\sum_s\beta_v(s),
\]
because a positive term \(m_v(s)-w(vs)\) equals \(w(us)-w(vs)\) for some \(u\) with \(v\to u\to s\). Theorem 3.1 applied to \(D^w\) gives a vertex \((v,l)\) with \(\sum_uw(vu)=|N_1^+((v,l))|\le|N_2^+((v,l))|\le\sum_s\beta_v(s)\).

*Rational weights.* Multiplying all weights by a positive integer \(c\) multiplies both sides by \(c\), so the integer case applies.

*Real weights.* Let \(w_k(e)=\lfloor kw(e)\rfloor/k\). For each \(k\) some vertex \(v_k\) satisfies the inequality for \(w_k\), and some vertex \(v\) equals \(v_k\) for infinitely many \(k\). Both sides of the inequality for \(v\) are continuous functions of the weights, since \(\beta_v(s)\) is a maximum of finitely many affine functions, and \(w_k\to w\). Letting \(k\to\infty\) along those \(k\) gives the inequality for \(w\). \(\square\)

**Corollary 4.2** (Vertex weights). Let \(D\) be a nonempty finite oriented graph and \(\eta:V(D)\to[0,\infty)\). Some vertex \(v\) satisfies \(\eta(N_1^+(v))\le\eta(N_2^+(v))\).

*Proof.* Apply Theorem 4.1 with \(w(us)=\eta(s)\) on every arc \(u\to s\). Then \(\sum_{u\in N_1^+(v)}w(vu)=\eta(N_1^+(v))\). If \(v\to s\), every difference \(w(us)-w(vs)\) equals \(0\), so \(\beta_v(s)=0\). If \(s\in N_2^+(v)\), then \(w(vs)=0\) and every \(u\) with \(v\to u\to s\) gives \(w(us)=\eta(s)\), so \(\beta_v(s)=\eta(s)\). For every other \(s\), including \(s=v\), there is no walk \(v\to u\to s\), and \(\beta_v(s)=0\). Hence \(\sum_s\beta_v(s)=\eta(N_2^+(v))\). \(\square\)

The next statement asks for one weighting that works at every vertex simultaneously. Its proof uses a separation argument.

**Lemma 4.3.** Let \(V\) be a finite set and \(\mathsf M\) a real \(V\times V\) matrix. If no vector \(\xi\ge0\) satisfies \((\mathsf M^{\mathsf T}\xi)_v<0\) for every \(v\in V\), then some \(\eta\ge0\) with \(\sum_v\eta_v=1\) satisfies \(\mathsf M\eta\ge0\) in every coordinate.

*Proof.* Let \(\Sigma=\{\eta\ge0:\sum_v\eta_v=1\}\), \(K=\{\mathsf M\eta:\eta\in\Sigma\}\) and \(O=[0,\infty)^V\), and suppose \(K\cap O=\varnothing\). The set \(K-O=\{y-z:y\in K,\,z\in O\}\) is convex. It is closed: if \(y_k-z_k\to x\) with \(y_k\in K\), a subsequence of \(y_k\) converges to some \(y\in K\) because \(K\) is compact, so \(z_k\to y-x\in O\), and \(x=y-(y-x)\). It does not contain \(0\). A closed nonempty set has a point \(\omega\) of least Euclidean norm (minimize over its intersection with a large closed ball), and \(\omega\ne0\). For \(x\in K-O\) and \(0<\lambda\le1\), the point \(\omega+\lambda(x-\omega)\) lies in \(K-O\), so
\[
0\le|\omega+\lambda(x-\omega)|^2-|\omega|^2=2\lambda\,\omega\cdot(x-\omega)+\lambda^2|x-\omega|^2 ;
\]
dividing by \(\lambda\) and letting \(\lambda\to0\) gives \(\omega\cdot x\ge|\omega|^2>0\). Taking \(x=y-te_v\) with \(y\in K\) and \(t\ge0\) gives \(\omega\cdot y\ge t\,\omega_v+|\omega|^2\) for all \(t\ge0\), so \(\omega_v\le0\) for every \(v\); and \(t=0\) gives \(\omega\cdot y>0\). Put \(\xi=-\omega\ge0\). For \(y=\mathsf Me_v\in K\), \((\mathsf M^{\mathsf T}\xi)_v=\xi\cdot\mathsf Me_v<0\), for every \(v\). This contradicts the hypothesis. \(\square\)

**Corollary 4.4** (A balanced weighting). Every nonempty finite oriented graph \(D\) has a weighting \(\eta:V(D)\to[0,\infty)\) with \(\eta(V(D))=1\) such that
\[
\eta(N_1^+(v))\le\eta(N_2^+(v))\qquad\text{for every }v\in V(D).
\]

*Proof.* Let \(\mathsf M_D\) have entry \(1\) at \((v,s)\) if \(s\in N_2^+(v)\), entry \(-1\) if \(s\in N_1^+(v)\), and \(0\) otherwise; then \((\mathsf M_D\eta)_v=\eta(N_2^+(v))-\eta(N_1^+(v))\). Let \(\overleftarrow D\) be \(D\) with every arc reversed. The directed distance from \(v\) to \(s\) in \(\overleftarrow D\) equals the distance from \(s\) to \(v\) in \(D\), so \(\mathsf M_{\overleftarrow D}=\mathsf M_D^{\mathsf T}\). If some \(\xi\ge0\) satisfied \((\mathsf M_D^{\mathsf T}\xi)_v<0\) for every \(v\), then \(\xi(N_2^+(v))<\xi(N_1^+(v))\) would hold in \(\overleftarrow D\) at every vertex, contradicting Corollary 4.2 for \(\overleftarrow D\). Lemma 4.3 therefore gives the weighting. \(\square\)

The weighting may need zero entries; see Exercise 6.1.

## 5. Directed triangles

A *directed triangle* is a directed cycle \(x\to y\to z\to x\) of length three. For a vertex \(v\) of an oriented graph \(D\) of order \(n\), let \(N_1^-(v)=\{u:u\to v\}\) and let
\[
Z(v)=V(D)\setminus\bigl(\{v\}\cup N_1^+(v)\cup N_1^-(v)\bigr)
\]
be the set of vertices not adjacent to \(v\). Since \(D\) is oriented, \(n-1=d^+(v)+d^-(v)+|Z(v)|\). Write \(\delta^\pm(D)=\min_vd^\pm(v)\).

**Corollary 5.1.** If \(D\) is a nonempty finite oriented graph of order \(n\) without directed triangles, some vertex \(v\) satisfies
\[
d^+(v)\le|Z(v)|\qquad\text{and}\qquad n-1\ge2d^+(v)+d^-(v).
\]

*Proof.* Let \(w\in N_2^+(v)\), reached by \(v\to u\to w\). By definition \(w\ne v\) and \(w\notin N_1^+(v)\), and \(w\notin N_1^-(v)\), since \(w\to v\) would close a directed triangle. Hence \(N_2^+(v)\subseteq Z(v)\) for every \(v\). Theorem 3.1 gives a vertex with \(d^+(v)\le|N_2^+(v)|\le|Z(v)|\), and then \(n-1=d^+(v)+d^-(v)+|Z(v)|\ge2d^+(v)+d^-(v)\). \(\square\)

**Corollary 5.2.** If an oriented graph \(D\) of order \(n\ge1\) satisfies \(\delta^+(D)\ge n/3\) and \(\delta^-(D)\ge n/3\), then \(D\) contains a directed triangle.

*Proof.* Otherwise Corollary 5.1 gives \(n-1\ge2\delta^+(D)+\delta^-(D)\ge n\). \(\square\)

Caccetta and Häggkvist conjectured that minimum out-degree at least \(n/3\) alone forces a directed cycle of length at most three in every digraph on \(n\) vertices; Corollary 5.2 assumes the bound for in-degrees as well. This consequence of the second neighborhood conjecture is recorded in Sullivan's survey [Sul], as noted in [OpenAI-SN].

**Corollary 5.3.** Let \(r\ge1\). If every vertex of an oriented graph \(D\) of order \(n\) has \(d^+(v)=d^-(v)=r\) and \(D\) has no directed triangle, then \(n\ge3r+1\). In particular, this holds when \(D\) has directed girth four, that is, when its shortest directed cycle has length four.

*Proof.* Corollary 5.1 gives \(n-1\ge3r\). \(\square\)

The case of girth four of the conjecture of Behzad, Chartrand and Wall, that an \(r\)-regular digraph of directed girth \(g\) has at least \(r(g-1)+1\) vertices, is the second statement of Corollary 5.3. The bound is attained:

**Example 5.4.** For \(r\ge1\) and \(n=3r+1\), let \(D\) have vertex set \(\mathbb Z/n\) and arcs \(x\to x+a\) for \(a\in\{1,\dots,r\}\). Every vertex has in- and out-degree \(r\). A closed walk of length \(L\) has steps \(a_1,\dots,a_L\in\{1,\dots,r\}\) with \(a_1+\dots+a_L\equiv0\pmod n\); for \(L\le3\), the sum lies between \(1\) and \(3r<n\), so there are no opposite arcs and no directed triangles. The cycle \(0\to r\to2r\to3r\to0\) has length four, because \(3r+1\equiv0\). Hence \(D\) is an oriented graph of directed girth four with exactly \(3r+1\) vertices.

## 6. Exercises

**6.1.** Let \(D\) be the transitive tournament on \(\{1,\dots,n\}\), \(n\ge2\), with \(x\to y\) for \(x<y\). Show that the only weighting with the properties of Corollary 4.4 is the point mass at \(1\).

**6.2.** In Example 5.4, compute \(N_1^+(0)\), \(N_2^+(0)\) and \(Z(0)\), and show that every vertex attains equality in both inequalities of Corollary 5.1. Deduce that Corollary 5.2 fails if \(n/3\) is replaced by \((n-1)/3\).

**6.3.** Let \(D'\) be obtained from \(D\) by deleting the arcs of weight \(0\), with the weights of the remaining arcs unchanged. Show that Theorem 4.1 for \(D\) follows from Theorem 4.1 for \(D'\).

**6.4.** In the proof of Theorem 2.1, the families \(\mathcal R\) and \(\mathcal C\) are generally not compatible. Explain which part of the proof uses each of the following: the in-neighbor hypothesis; the orientation of \(G\); the strictness of (0.1).

## 7. Solutions

**6.1.** For every \(v\), every walk of length two from \(v\) ends at a vertex larger than \(v+1\), which is already an out-neighbor, so \(N_2^+(v)=\varnothing\). The condition becomes \(\eta(N_1^+(v))\le0\), so \(\eta\) vanishes on \(N_1^+(1)=\{2,\dots,n\}\), and \(\eta(1)=1\). Conversely, this \(\eta\) satisfies the condition at every vertex, since no vertex has \(1\) as an out-neighbor.

**6.2.** \(N_1^+(0)=\{1,\dots,r\}\); the walks of length two end in \(\{2,\dots,2r\}\), so \(N_2^+(0)=\{r+1,\dots,2r\}\); \(N_1^-(0)=\{2r+1,\dots,3r\}\), so \(Z(0)=\{r+1,\dots,2r\}\). Hence \(d^+(0)=|Z(0)|=r\) and \(n-1=3r=2d^+(0)+d^-(0)\); by symmetry this holds at every vertex. Here \(\delta^+=\delta^-=r=(n-1)/3\), and there is no directed triangle.

**6.3.** The sums \(\sum_{u\in N_1^+(v)}w(vu)\) agree in \(D\) and \(D'\), since the deleted arcs have weight \(0\), and so do the values \(w(us)\) and \(w(vs)\). Every walk \(v\to u\to s\) of \(D'\) is a walk of \(D\), so the maximum defining \(\beta_v(s)\) in \(D\) is taken over a larger set, and \(\beta^{D}_v(s)\ge\beta^{D'}_v(s)\). A vertex satisfying the inequality in \(D'\) therefore satisfies it in \(D\).

**6.4.** The in-neighbor hypothesis is used in Lemma 1.3, to show that the columns of \(P\) and the rows of \(Q\) are proper, so that (0.1) applies to them. The orientation is used in Lemma 1.2, to start the maximization with \((\Delta,\Delta)\). Strictness of (0.1) gives the strict inequalities (2.1), hence the strict inequality (2.2), which is the source of the contradiction. Steps 3 and 4 use only the definitions of \(\mathcal R\) and \(\mathcal C\), the inclusion \(\Delta\subseteq P\cap Q\) and the compatibility of \((P,Q)\).

## References

- [OpenAI-SN] OpenAI, *A proof of Seymour's second-neighborhood conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf
- [Sea12] T. Seacrest, *The arc-weighted version of the second neighborhood conjecture*, Journal of Graph Theory (2015); preprint 2012. https://arxiv.org/abs/1212.1883
- [Sul] B. D. Sullivan, *A summary of problems and results related to the Caccetta–Häggkvist conjecture*, 2006. https://arxiv.org/abs/math/0605646
