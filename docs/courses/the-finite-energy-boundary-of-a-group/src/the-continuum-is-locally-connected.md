# The continuum is locally connected

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that the continuum \(L\) without cut points of the lesson [A continuum without cut points and its graph](a-continuum-without-cut-points-and-its-graph.md) is locally connected (Theorem 7.1). With the results of the course on continua this contradicts the other properties of \(L\) (Corollary 7.3).

The idea of the proof is to produce connected subsets of \(L\) as limits of paths of the graph \(K\). Near a point \(x\) of \(L\), two vertices of \(K\) are joined by a path of \(K\) that stays near \(x\). Such a path is a finite sequence of vertices and not a connected subset of \(L\). It is replaced by paths through vertices of larger and larger depth; their edges become short, and their vertex sets have a connected set of limit points inside \(L\). For this one needs paths at every depth \(m\) between vertices near two given points \(x,y\) of \(L\), that is, the component labels \(Q_m(x)\) and \(Q_m(y)\) must agree for every \(m\). The main step is Theorem 4.1: beyond one threshold \(M\), equal labels at depth \(m\) imply equal labels at depth \(m+1\).

The lesson follows the second half of Section 9 of [OpenAI-S]. It uses [Vertices of large depth](vertices-of-large-depth.md) and [Component labels and annular depth](component-labels-and-annular-depth.md).

## 1. The setting

We use the data \(Y=H\cup L\), \(K\), \(I\) and the properties (S1) to (S7) of the lesson on component labels and annular depth, and the depth \(D\) of that lesson. As in the lesson on vertices of large depth, \(A\) is a closed subset of \(Y\) with \(1\in A\) and \(L\not\subseteq A\); \(p_1,\dots,p_k\) are the chosen points of the orbits of \(H\) in \(I\), with \(p_1=1\) if \(I=H\); \(R(u)\) is the set of \(g\in H\) with \(gp_i=u\), for \(u\) in the orbit of \(p_i\); and \(I_m\) is the set of vertices \(u\in I\setminus A\) with \(D(A,g)\ge m\) for all \(g\in R(u)\). From that lesson we use the following.

- (V1) \(I_0\supseteq I_1\supseteq\cdots\), and for every finite set \(E\subseteq I\) there is \(m\) with \(E\cap I_m=\varnothing\) (Lemma 4.1(2)).
- (V2) For \(x\in L\setminus A\) and \(N\ge1\), all \(g\in H\) in some neighbourhood of \(x\) in \(Y\) have \(D(A,g)\ge N\).
- (Q1) For every \(m\ge0\) there is a map \(Q_m\) from \(L\setminus A\) to the set of components of \(K[I_m]\) such that every \(x\in L\setminus A\) is the limit of a sequence of pairwise distinct vertices in \(I_m\), and all vertices of \(I_m\) in some neighbourhood of \(x\) in \(Y\) belong to \(Q_m(x)\).
- (Q2) \(Q_m\) is locally constant on \(L\setminus A\).
- (T) Let \(m_n\) be integers with \(m_n\to\infty\) and \(g_n\in H\) with \(D(A,g_n)\ge m_n\). After passing to a subsequence there is a point \(q\in L\) such that for any two points \(z,z'\in L\setminus\{q\}\) and all large \(n\): \(g_nz\notin A\), \(g_nz'\notin A\) and
\[
Q_{m_n+1}(g_nz)=Q_{m_n+1}(g_nz').
\]
(Lemma 2.1 and Theorem 6.1(2) of that lesson.)

The values of \(Q_m\) are called *labels*.

## 2. Majority labels

A label is attached to a point of \(L\). To compare labels along the group, we attach to a group element \(g\) the label that most points of a translate \(gZ\) of a fixed three-point set have.

Choose a set \(Z\subseteq L\) of three points; \(L\) is infinite, because it is connected with more than one point. For \(g\in H\) the set \(gZ\) consists of three points of \(L\).

**Lemma 2.1.** For every finite set \(S\subseteq H\) there is \(M\ge1\) such that for all \(m\ge M\) the following hold.

1. If \(D(A,g)\ge m\), then at least two points of \(gZ\) lie outside \(A\) and have the same label under \(Q_{m+1}\).
2. For \(g\) as in (1) let \(J_m(g)\) be the label under \(Q_{m+1}\) of at least two points of \(gZ\). If \(s\in S\) and \(D(A,g)\ge m\), \(D(A,gs)\ge m\), then
\[
J_m(g)=J_m(gs).
\]

The label \(J_m(g)\) is well defined: two different labels cannot each be the label of two points of a set of three points. It is the *majority label* of \(g\).

**Proof.** *There is \(M_1\) such that (1) holds for all \(m\ge M_1\).* Suppose not. Then for every \(n\) there are \(m_n\ge n\) and \(g_n\in H\) with \(D(A,g_n)\ge m_n\) for which (1) fails. Pass to a subsequence and choose \(q\) as in (T). Two points \(z,z'\) of \(Z\) are different from \(q\). By (T), for large \(n\) the points \(g_nz\) and \(g_nz'\) lie outside \(A\) and have the same label under \(Q_{m_n+1}\). So (1) holds for \(m_n\) and \(g_n\), a contradiction.

*There is \(M\ge M_1\) such that (2) holds for all \(m\ge M\).* Suppose not. Then for every \(n\) there are \(m_n\ge n\), \(m_n\ge M_1\), and \(g_n\in H\), \(s_n\in S\) with
\[
\begin{gathered}
D(A,g_n)\ge m_n,\quad D(A,g_ns_n)\ge m_n,\\
J_{m_n}(g_n)\ne J_{m_n}(g_ns_n).
\end{gathered}
\]
Since \(S\) is finite, we may pass to a subsequence with \(s_n=s\) for all \(n\). Pass to a further subsequence and choose \(q\) as in (T), for the sequences \((m_n)\) and \((g_n)\). Choose two points \(z_1,z_2\) of \(Z\) different from \(q\), and two points \(z_3,z_4\) of \(Z\) with \(sz_3\ne q\) and \(sz_4\ne q\); this is possible, because \(s\) is injective on \(L\), so at most one point of \(Z\) is mapped to \(q\). The points \(sz_3,sz_4\) lie in \(L\). By (T), applied to \(z_1\) and each of \(z_2\), \(sz_3\), \(sz_4\), for large \(n\) the four points
\[
g_nz_1,\quad g_nz_2,\quad g_nsz_3,\quad g_nsz_4
\]
lie outside \(A\) and have one label under \(Q_{m_n+1}\). It is the label of two points of \(g_nZ\), hence equal to \(J_{m_n}(g_n)\), and the label of two points of \(g_nsZ\), hence equal to \(J_{m_n}(g_ns)\). This is a contradiction. \(\blacksquare\)

The lemma is applied to the sequence \((g_n)\) only; the elements \(g_ns\) enter through the points \(sz_3,sz_4\). With two points in place of three the argument fails: one point of \(Z\), and one of \(sZ\), may be the exceptional point \(q\).

## 3. Moves between representatives

We choose a finite set \(S\subseteq H\) with the following two properties.

- (M1) For every edge of \(K\), with ends \(u\) and \(v\) in either order, there are \(g\in R(u)\) and \(s\in S\) with \(gs\in R(v)\).
- (M2) If \(I\subseteq L\), then for every \(i\) there is \(h_i\in S\) with \(h_ip_i=p_i\) and \(h_i^jz\to p_i\) as \(j\to\infty\), for every \(z\in L\).

For (M2) take the elements given by (S6). For (M1), recall from (S3) that the edges of \(K\) form finitely many orbits of \(H\); choose one edge in each orbit, with ends \(u_e,v_e\) for \(e=1,\dots,r\), and elements \(a_e\in R(u_e)\), \(b_e\in R(v_e)\). Let \(S\) contain the elements \(s_e=a_e^{-1}b_e\) and \(s_e^{-1}\) for \(e=1,\dots,r\). An edge of \(K\) with ends \(u,v\) is the image under some \(h\in H\) of one of the chosen edges. If \(u=hu_e\) and \(v=hv_e\), then \(g=ha_e\) lies in \(R(u)\) and \(gs_e=hb_e\) lies in \(R(v)\). If \(u=hv_e\) and \(v=hu_e\), then \(g=hb_e\) lies in \(R(u)\) and \(gs_e^{-1}=ha_e\) lies in \(R(v)\). So (M1) holds.

From here on \(S\) is this set and \(M\) is the number given by Lemma 2.1 for \(S\).

## 4. One threshold for all larger depths

**Theorem 4.1.** For every \(m\ge M\) and all \(x,y\in L\setminus A\):
\[
\begin{gathered}
Q_m(x)=Q_m(y)\\
\Longrightarrow\quad Q_{m+1}(x)=Q_{m+1}(y).
\end{gathered}
\]

**Proof.** Fix \(m\ge M\). If \(v\in I_m\) and \(g\in R(v)\), then \(D(A,g)\ge m\), so the majority label \(J_m(g)\) is defined. The proof has three steps.

*Step 1: adjacent vertices.* Let \(v,w\in I_m\) be the ends of an edge of \(K\). By (M1) there are \(g\in R(v)\) and \(s\in S\) with \(gs\in R(w)\). Both have depth at least \(m\), so by Lemma 2.1(2)
\[
J_m(g)=J_m(gs).
\]

*Step 2: near a point of \(L\).* We show: for every \(x\in L\setminus A\) there is a neighbourhood \(W_x\) of \(x\) in \(Y\) such that
\[
J_m(g)=Q_{m+1}(x)
\]
for every vertex \(v\in I_m\cap W_x\) and every \(g\in R(v)\). By (Q2) there is an open set \(U\subseteq Y\) containing \(x\) such that \(U\cap L\) lies in \(L\setminus A\) and \(Q_{m+1}\) is constant on \(U\cap L\).

*The case \(I\subseteq L\).* We show first that for every \(v\in I_m\) and every \(g\in R(v)\)
\[
J_m(g)=Q_{m+1}(v). \tag{1}
\]
Here \(v\in L\setminus A\), so the right side is defined. Let \(v=gp_i\) and let \(h_i\) be as in (M2). For every \(j\ge0\) the element \(gh_i^j\) maps \(p_i\) to \(v\), so it lies in \(R(v)\) and has depth at least \(m\). By Lemma 2.1(2) with \(s=h_i\),
\[
J_m(g)=J_m(gh_i)=J_m(gh_i^2)=\cdots .
\]
By (Q2) there is a neighbourhood \(N\) of \(v\) in \(L\), contained in \(L\setminus A\), on which \(Q_{m+1}\) is constant. For each of the three points \(z\in Z\) we have \(h_i^jz\to p_i\), hence \(gh_i^jz\to v\). So for large \(j\) the three points of \(gh_i^jZ\) lie in \(N\) and have the label \(Q_{m+1}(v)\); then \(J_m(gh_i^j)=Q_{m+1}(v)\). This proves (1). Now let \(W_x=U\). A vertex \(v\in I_m\cap U\) lies in \(U\cap L\), so \(Q_{m+1}(v)=Q_{m+1}(x)\), and (1) gives the claim.

*The case \(I=H\).* Here \(R(v)=\{v\}\) for every vertex \(v\). Suppose there is no neighbourhood \(W_x\) as claimed. Then there is a sequence \((g_n)\) in \(I_m\) with \(g_n\to x\) and
\[
J_m(g_n)\ne Q_{m+1}(x)\quad\text{for all }n .
\]
Since \(x\notin H\), every element occurs only finitely often in this sequence. Pass to a subsequence in which the \(g_n^{-1}\) are pairwise distinct and converge to a point \(b\), which lies in \(L\). At least two points of \(Z\) are different from \(b\). By (S2), for the closed set \(Z\setminus\{b\}\) and the open set \(U\): for large \(n\) the points \(g_nz\), \(z\in Z\setminus\{b\}\), lie in \(U\cap L\) and have the label \(Q_{m+1}(x)\). Hence \(J_m(g_n)=Q_{m+1}(x)\), a contradiction.

*Step 3: conclusion.* In both cases \(J_m(g)\) does not depend on the choice of \(g\in R(v)\): for \(I\subseteq L\) by (1), and for \(I=H\) because \(R(v)\) has one element. Write \(j(v)\) for this label. By Step 1, \(j(v)=j(w)\) for adjacent vertices \(v,w\in I_m\). So \(j\) is constant on every component of \(K[I_m]\).

Let \(x,y\in L\setminus A\) with \(Q_m(x)=Q_m(y)\), and let \(G\) be this component. By (Q1) there are a vertex \(v\in G\) in \(W_x\) and a vertex \(w\in G\) in \(W_y\). By Step 2,
\[
Q_{m+1}(x)=j(v)=j(w)=Q_{m+1}(y).
\]
\(\blacksquare\)

In (1) the vertex \(v\) need not belong to \(I_{m+1}\). The label \(Q_{m+1}(v)\) is the component of \(K[I_{m+1}]\) that contains the vertices of \(I_{m+1}\) near \(v\).

## 5. Short edges

**Lemma 5.1.** For every \(\varepsilon>0\) there is \(m_\varepsilon\) such that for all \(m\ge m_\varepsilon\) the two ends of every edge of \(K[I_m]\) have distance less than \(\varepsilon\).

**Proof.** Let \(u_e,v_e\), \(e=1,\dots,r\), be the ends of the chosen edges of Section 3. By (S4), for all but finitely many \(h\in H\) and all \(e\),
\[
\begin{aligned}
\rho(hu_e,hv_e)&\le\rho(hu_e,h)+\rho(h,hv_e)\\
&<\varepsilon .
\end{aligned}
\]
Let \(F\subseteq H\) be the finite set of exceptions, and \(E\) the finite set of the vertices \(hu_e\), \(hv_e\) with \(h\in F\). By (V1) there is \(m_\varepsilon\) with \(E\cap I_m=\varnothing\) for \(m\ge m_\varepsilon\). An edge of \(K[I_m]\) has ends \(hu_e\), \(hv_e\) for some \(h\) and \(e\). For \(m\ge m_\varepsilon\) these ends are not in \(E\), so \(h\notin F\), and their distance is less than \(\varepsilon\). \(\blacksquare\)

The proof uses that \(K\) has finitely many orbits of edges. It does not use that a vertex has finitely many neighbours, and in the case \(I\subseteq L\) a vertex may have infinitely many.

## 6. Limit points of chains

**Lemma 6.1.** Let \(Y\) be a compact metric space with metric \(\rho\). For \(n\ge1\) let \(v_{n,0},\dots,v_{n,r_n}\) be points of \(Y\), and let \(P_n\) be the set of these points. Assume:

- for every \(\varepsilon>0\) and all but finitely many \(n\): \(\rho(v_{n,i-1},v_{n,i})<\varepsilon\) for \(i=1,\dots,r_n\);
- \(v_{n,0}\to x\) and \(v_{n,r_n}\to y\).

Let \(C\) be the set of points \(z\in Y\) such that every neighbourhood of \(z\) meets \(P_n\) for infinitely many \(n\). Then \(C\) is closed and connected, and it contains \(x\) and \(y\).

**Proof.** If \(z\notin C\), then \(z\) has an open neighbourhood that meets \(P_n\) for finitely many \(n\) only, and no point of this neighbourhood lies in \(C\). So \(C\) is closed. It contains \(x\) and \(y\), because \(v_{n,0}\to x\) and \(v_{n,r_n}\to y\).

*If \(W\) is an open set containing \(C\), then \(P_n\subseteq W\) for all but finitely many \(n\).* Otherwise there are infinitely many \(n\) with a point \(w_n\in P_n\setminus W\). A subsequence of \((w_n)\) converges to a point \(z\) of the closed set \(Y\setminus W\). Every neighbourhood of \(z\) contains \(w_n\) for infinitely many \(n\), so \(z\in C\subseteq W\), a contradiction.

*\(C\) is connected.* Suppose \(C\) is the union of two disjoint nonempty closed sets \(C_0\) and \(C_1\), with \(x\in C_0\). They are compact, so their distance \(\delta\) is positive. Let \(W_0\) and \(W_1\) be the sets of points of \(Y\) at distance less than \(\delta/3\) from \(C_0\) and from \(C_1\). They are open, and a point of \(W_0\) and a point of \(W_1\) have distance more than \(\delta/3\). For all large \(n\) we have \(P_n\subseteq W_0\cup W_1\), by the statement just proved; \(v_{n,0}\in W_0\); and \(\rho(v_{n,i-1},v_{n,i})<\delta/3\) for all \(i\). For such \(n\), no \(v_{n,i}\) lies in \(W_1\): the first such point would have distance less than \(\delta/3\) from its predecessor in \(W_0\). So \(P_n\subseteq W_0\) for all large \(n\). Then the neighbourhood \(W_1\) of a point of \(C_1\) meets \(P_n\) for finitely many \(n\) only, and this point is not in \(C\). This is a contradiction. \(\blacksquare\)

## 7. Local connectedness

A space is *locally connected* if for every point \(x\) and every open set \(U\) containing \(x\) there is a connected open set \(V\) with \(x\in V\subseteq U\) ([Paths in locally connected spaces](course:continua-arcs-and-cut-points/paths-in-locally-connected-spaces)).

**Theorem 7.1.** Let \(Y=H\cup L\), \(K\) and \(I\) satisfy (S1) to (S7). Then \(L\) is locally connected.

**Proof.** Let \(U\) be an open subset of \(L\) and \(x\in U\). We show:

> (P) there is a neighbourhood \(V\) of \(x\) in \(L\) such that every \(y\in V\) lies with \(x\) in a connected subset of \(U\).

*The set \(A\).* Choose an open set \(U_1\subseteq Y\) with \(U_1\cap L=U\), and \(r>0\) smaller than \(\rho(x,1)\) such that the closed ball of radius \(r\) around \(x\) lies in \(U_1\). Let \(O=B(x,r)\) and
\[
A=Y\setminus O .
\]
Then \(A\) is closed, \(1\in A\), and \(x\in L\setminus A\). So the lesson on vertices of large depth and Sections 1 to 5 apply to \(A\). We have \(L\setminus A=L\cap O\) and \(\overline O\cap L\subseteq U\).

*Equal labels at all depths.* Let \(M\) be the number of Section 3. By (Q2) there is a neighbourhood \(V\) of \(x\) in \(L\), contained in \(L\cap O\), with \(Q_M(y)=Q_M(x)\) for all \(y\in V\). By Theorem 4.1 and induction on \(m\),
\[
Q_m(y)=Q_m(x)\qquad(y\in V,\ m\ge M).
\]

*Paths.* Fix \(y\in V\). For every \(m\ge M\) there are, by (Q1), vertices \(a_m\) and \(b_m\) in the component \(Q_m(x)=Q_m(y)\) of \(K[I_m]\) with
\[
\rho(a_m,x)<\frac1m,\qquad\rho(b_m,y)<\frac1m ,
\]
and a path of \(K[I_m]\) from \(a_m\) to \(b_m\). Let \(P_m\) be the set of its vertices. Then
\[
P_m\subseteq I_m\subseteq I\setminus A\subseteq O .
\]
By Lemma 5.1, for every \(\varepsilon>0\) and all large \(m\), consecutive vertices of the path have distance less than \(\varepsilon\).

*The limit set.* Let \(C\) be the set of points \(z\in Y\) every neighbourhood of which meets \(P_m\) for infinitely many \(m\). By Lemma 6.1, \(C\) is connected and contains \(x\) and \(y\). A point outside \(\overline O\) has a neighbourhood that does not meet \(O\), hence no \(P_m\); so \(C\subseteq\overline O\). We show \(C\subseteq L\). If \(I\subseteq L\), every \(P_m\) lies in the closed set \(L\), and a point outside \(L\) has a neighbourhood that meets no \(P_m\). If \(I=H\), let \(h\in H\). By (V1) there is \(m_0\) with \(h\notin I_m\) for all \(m\ge m_0\). The set \(\{h\}\) is a neighbourhood of \(h\) in \(Y\), and it meets \(P_m\) for finitely many \(m\) only; so \(h\notin C\). Hence
\[
C\subseteq\overline O\cap L\subseteq U .
\]
This proves (P).

*Components of \(U\) are open.* Let \(G\) be a component of \(U\) and \(x\in G\). By (P) a neighbourhood \(V\) of \(x\) in \(L\) consists of points that lie with \(x\) in a connected subset of \(U\); such a subset lies in \(G\). So \(V\subseteq G\). Hence \(G\) is open in \(L\).

For \(x\in U\), the component of \(U\) that contains \(x\) is a connected open set that contains \(x\) and lies in \(U\). So \(L\) is locally connected. \(\blacksquare\)

**Corollary 7.2.** If \(Y=H\cup L\), \(K\) and \(I\) satisfy (S1) to (S7), then \(\dim L\le1\) does not hold.

**Proof.** By (S1) and Theorem 7.1, \(L\) is a locally connected compact connected metric space with more than one point, that is, a Peano continuum with more than one point; and \(\check H^1(L;k)=0\) for the group \(k\) with two elements, by (S7). If \(\dim L\le1\), then \(L\) has a cut point, by Corollary 3.2(2) of [Dendrites and cut points](course:continua-arcs-and-cut-points/dendrites-and-cut-points). This contradicts (S1). \(\blacksquare\)

**Corollary 7.3.** Let \(\Gamma\), \(B\) and \(X\) be as in the lesson on a continuum without cut points and its graph, in Case A or in Case B, with the assumptions made there. Then \(\check H^1(B;k)\ne0\) for the group \(k\) with two elements.

**Proof.** Suppose \(\check H^1(B;k)=0\). By Theorem 2.1 of that lesson the data \(Y=H\cup L\), \(K\), \(I\) of the two cases satisfy (S1) to (S6), \(\check H^1(L;k)=0\), which is (S7), and \(\dim L\le1\). This contradicts Corollary 7.2. \(\blacksquare\)

Corollary 7.3 is the form in which the result is used. In [Dimension and cohomology of the boundary](dimension-and-cohomology-of-the-boundary.md) the group \(\check H^1(B;k)\) is shown to vanish under a condition on the Cayley complex. So that condition, together with the assumptions under which the boundary \(B\) exists and one of the two cases applies, cannot hold.

## 8. Exercises

**8.1.** Let \(Y=[0,1]\). Determine the set \(C\) of Lemma 6.1 for the chains \(v_{n,i}=i/n\), \(0\le i\le n\). Show by an example that the first assumption of the lemma cannot be dropped.

**8.2.** In Lemma 6.1, show that \(C\) is the set of limits of convergent sequences \((w_{n_j})_j\) with \(n_1<n_2<\cdots\) and \(w_{n_j}\in P_{n_j}\).

**8.3.** Let \(Y=H\cup L\), \(K\), \(I\) satisfy (S1) to (S7). Show that any two points of \(L\) are the ends of an arc in \(L\), and that for every \(p\in L\) any two points of \(L\setminus\{p\}\) are the ends of an arc in \(L\setminus\{p\}\).

**8.4.** In the proof of Theorem 7.1 the number \(M\) depends on the set \(A\), hence on \(x\) and \(U\). Explain why the proof does not need a number \(M\) that works for all \(x\) and \(U\).

## 9. Solutions

**8.1.** Every point of \([0,1]\) has distance at most \(1/n\) from \(P_n\), so every neighbourhood of every point meets \(P_n\) for all large \(n\): \(C=[0,1]\). For the chains with the two points \(v_{n,0}=0\), \(v_{n,1}=1\) the set \(C\) is \(\{0,1\}\), which is not connected; the consecutive points have distance \(1\).

**8.2.** If \(w_{n_j}\to z\), every neighbourhood of \(z\) contains \(w_{n_j}\) for large \(j\), so it meets \(P_n\) for infinitely many \(n\). Conversely let \(z\in C\). Choose \(n_1\) and \(w_{n_1}\in P_{n_1}\) with \(\rho(w_{n_1},z)<1\); when \(n_{j-1}\) is chosen, the ball of radius \(1/j\) around \(z\) meets \(P_n\) for infinitely many \(n\), so there are \(n_j>n_{j-1}\) and \(w_{n_j}\in P_{n_j}\) in this ball. Then \(w_{n_j}\to z\).

**8.3.** By Theorem 7.1 and (S1), \(L\) is a Peano continuum. By Corollary 4.2 of [Every path contains an arc](course:continua-arcs-and-cut-points/every-path-contains-an-arc), any two distinct points of a connected open subset of a Peano continuum are the ends of an arc in that subset. Apply it to \(L\), and to \(L\setminus\{p\}\), which is open, and connected because \(p\) is not a cut point.

**8.4.** Local connectedness is a statement about one point \(x\) and one open set \(U\) at a time. For given \(x\) and \(U\) the proof fixes \(A\), and with it the sets \(I_m\), the labels \(Q_m\), the set \(S\) and the number \(M\); what it needs is that \(M\) does not depend on the points \(y\) near \(x\) and on the depth \(m\ge M\). That is the content of Theorem 4.1.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Sections 9 and 10. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
