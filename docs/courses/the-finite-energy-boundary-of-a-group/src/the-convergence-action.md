# The convergence action

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The compact space \(X=\Gamma\cup B\) of [The compact space and its boundary](the-compact-space-and-its-boundary.md) carries an action of \(\Gamma\) by homeomorphisms. This lesson shows what that action looks like far out in the group. If group elements \(g_n\) converge, as points of \(X\), to a boundary point \(a\), and their inverses converge to a boundary point \(b\), then the maps \(g_n\) push all of \(X\) except a neighbourhood of \(b\) into any given neighbourhood of \(a\) (Theorem 3.1). So \(\Gamma\) acts on its boundary as a convergence group in the sense of [Convergence actions and their elements](course:convergence-groups/convergence-actions-and-their-elements) (Corollary 3.2), and every element of infinite order is parabolic or loxodromic on \(B\).

Two further results use this. For a parabolic element with fixed point \(p\), the points \(g\) and \(gp\) of \(X\) come close together as \(g\) leaves finite sets (Theorem 4.2). And if \(\Gamma\) has no elements of finite order other than the identity, every orbit in \(B\) is dense (Theorem 5.2).

The only input beyond the previous lesson is the square summability of the edge lengths: a level cut of a finite-energy function, translated far away, becomes short. The argument is that of [OpenAI-S, Section 4].

The standing assumptions and the notation of the previous lesson are in force: the triangular presentation, \(\mathcal D_0\ne\mathcal D\), the one-ended Cayley graph \(G\), the families \(\mathcal F_0\subseteq\mathcal F\), the space \(X\) with its metric \(\rho\), the boundary \(B\), and the edge lengths \(\lambda\) with \(\sum_e\lambda(e)^2<\infty\).

## 1. Group elements far away

A sequence \((g_n)\) in \(\Gamma\) *tends to infinity* if every finite subset of \(\Gamma\) contains \(g_n\) for only finitely many \(n\); similarly for a family indexed by \(g\in\Gamma\). Group elements are also points of \(X\). Since the points of \(\Gamma\) are isolated in \(X\), a sequence in \(\Gamma\) that converges in \(X\) to a point of \(B\) tends to infinity, and a sequence of pairwise distinct elements of \(\Gamma\) has a subsequence that converges in \(X\) to a point of \(B\).

For \(g\in\Gamma\) and an edge \(e=(h,s)\), \(ge=(gh,s)\). For a fixed edge \(e\) and a finite set \(A\) of edges, \(ge\in A\) for only finitely many \(g\).

**Lemma 1.1** (right moves). For every \(s\in\Gamma\), \(\rho(u,us)\to0\) as \(u\to\infty\) in \(\Gamma\).

**Proof.** Fix a path in \(G\) from \(1\) to \(s\), with edges \(e_1,\dots,e_k\). The edges \(ue_1,\dots,ue_k\) form a path from \(u\) to \(us\), so \(\rho(u,us)\le\sum_i\lambda(ue_i)\). Let \(\varepsilon>0\). Only finitely many edges have length at least \(\varepsilon/k\), and each \(ue_i\) is one of them for only finitely many \(u\). So \(\rho(u,us)<\varepsilon\) for all but finitely many \(u\). \(\blacksquare\)

**Lemma 1.2.** If \(\Gamma\) has an infinite cyclic subgroup of finite index, then \(G\) is not one-ended.

**Proof.** Let \(Z=\langle z\rangle\) be the subgroup and \(t_1,\dots,t_k\) representatives of the cosets \(Zt_i\). Every element is \(z^nt_i\) for a unique pair \((n,i)\); put \(\varphi(z^nt_i)=n\). For a generator \(s\) write \(t_is=z^{c}t_j\); then \(\varphi(z^nt_is)=n+c\). So there is \(L\) with \(|\varphi(e^+)-\varphi(e^-)|\le L\) for every edge. The set \(A=\{g:|\varphi(g)|\le L\}\) is finite. In \(G\setminus A\) no edge joins a vertex with \(\varphi>L\) to one with \(\varphi<-L\), so every component lies in one of these two sets. Both sets are infinite, and \(G\setminus A\) has finitely many components (Lemma 1.1 of the previous lesson); so there are at least two infinite components. \(\blacksquare\)

By the standing assumptions, \(\Gamma\) therefore has no infinite cyclic subgroup of finite index.

## 2. Translated cuts are short

For \(g\in\Gamma\) and an edge \(e\) put
\[
\Lambda_g(e)=\sum_{e'\sim e}\lambda(ge'),
\]
the total length of the translates by \(g\) of the edges that equal \(e\) or share a cell with it. For a set \(C\) of edges, \(V(C)\) is the set of ends of the edges of \(C\).

**Lemma 2.1** (diameter of a translated dual component). Let \(C\) be a dually connected set of edges and \(g\in\Gamma\). Then the diameter of \(gV(C)\) in \(X\) is at most \(2\sum_{e\in C}\Lambda_g(e)\).

**Proof.** Let \(v,v'\in V(C)\) be ends of \(e,e'\in C\), and let \(e=e_0,e_1,\dots,e_k=e'\) be a sequence of distinct edges of \(C\) in which \(e_{i-1}\) and \(e_i\) are edges of a common cell \(\sigma_i\). Go from \(v\) along \(e_0\), if necessary, then inside \(\sigma_1\) to an end of \(e_1\), along \(e_1\) if necessary, inside \(\sigma_2\) to an end of \(e_2\), and so on to \(v'\). Inside a cell, two of its vertices are joined by a path that uses each edge of the cell at most once, and every edge of \(\sigma_i\) satisfies \(e''\sim e_i\); so the translate by \(g\) of the part inside \(\sigma_i\) has length at most \(\Lambda_g(e_i)\). Also \(\lambda(ge_i)\le\Lambda_g(e_i)\). Hence
\[
\begin{aligned}
\rho(gv,gv')&\le2\sum_{i=0}^k\Lambda_g(e_i)\\
&\le2\sum_{e\in C}\Lambda_g(e).
\end{aligned}
\]
\(\blacksquare\)

**Lemma 2.2** (translated cut lengths). Let \(F\) have finite energy, and for \(g\in\Gamma\) let
\[
I(F,g)=\int_{\mathbb R}\ \sum_{e\in S(F,t)}\Lambda_g(e)\,dt .
\]
Then \(I(F,g)=\sum_e|dF(e)|\,\Lambda_g(e)\le D\,\|dF\|\,\|\lambda\|\), and \(I(F,g)\to0\) as \(g\to\infty\).

**Proof.** The first equality is Tonelli's theorem, as in Lemma 3.1 of [Finite-energy functions on a Cayley complex](finite-energy-functions-on-a-cayley-complex.md): the levels \(t\) with \(e\in S(F,t)\) form an interval of length \(|dF(e)|\). Exchanging the order of summation,
\[
\begin{gathered}
I(F,g)=\sum_{e'}\alpha(e')\,\lambda(ge'),\\
\alpha(e')=\sum_{e\sim e'}|dF(e)| .
\end{gathered}
\]
Since at most \(D\) edges \(e\) satisfy \(e\sim e'\), the Cauchy–Schwarz inequality gives \(\alpha(e')^2\le D\sum_{e\sim e'}|dF(e)|^2\), and summing over \(e'\) gives \(\|\alpha\|\le D\|dF\|\). The function \(e'\mapsto\lambda(ge')\) has the same norm as \(\lambda\). So \(I(F,g)\le\|\alpha\|\,\|\lambda\|\).

Let \(\varepsilon>0\) and choose finite sets \(A_1,A_2\) of edges such that \(\alpha\) has norm at most \(\varepsilon\) outside \(A_1\) and \(\lambda\) has norm at most \(\varepsilon\) outside \(A_2\). Split the sum over \(e'\) into three parts: \(e'\notin A_1\); \(e'\in A_1\) and \(ge'\notin A_2\); \(e'\in A_1\) and \(ge'\in A_2\). The first is at most \(\varepsilon\|\lambda\|\) and the second at most \(\|\alpha\|\varepsilon\), by the Cauchy–Schwarz inequality. The third is empty for all but finitely many \(g\). \(\blacksquare\)

**Proposition 2.3** (collapse of translated cuts). Let \((g_n)\) be a sequence in \(\Gamma\) converging in \(X\) to \(a\in B\), and let \(T_1,\dots,T_q\in\mathcal F\). There is a subsequence, still written \((g_n)\), such that for every \(i\) and almost every \(t\in\mathbb R\)
\[
\sup\{\rho(g_nv,a):\ v\in V(S(T_i,t))\}\longrightarrow0 .
\]
If in addition \(g_n^{-1}\to b\in B\), the subsequence can be chosen so that also, for every \(i\) and almost every \(t\),
\[
\sup\{\rho(g_n^{-1}v,b):\ v\in V(S(T_i,t))\}\longrightarrow0 .
\]
The supremum over the empty set is \(0\).

**Proof.** *Base functions.* Let \(F_1,\dots,F_m\in\mathcal F_0\). Since \(g_n\to\infty\), Lemma 2.2 gives \(I(F_j,g_n)\to0\) for each \(j\). Pass to a subsequence with \(\sum_n\sum_jI(F_j,g_n)<\infty\), and write
\[
\sigma_{j,n}(t)=\sum_{e\in S(F_j,t)}\Lambda_{g_n}(e),
\]
so that \(I(F_j,g_n)=\int_{\mathbb R}\sigma_{j,n}(t)\,dt\). By monotone convergence, for each \(j\),
\[
\int_{\mathbb R}\ \sum_n\sigma_{j,n}(t)\,dt<\infty,
\]
so for almost every \(t\) the series \(\sum_n\sigma_{j,n}(t)\) converges, and its terms tend to \(0\): \(\sigma_{j,n}(t)\to0\) as \(n\to\infty\).
Call a level \(t\) *admissible for \(F_j\)* if this holds and \(t\) is regular for \(F_j\); almost every level is admissible. Let \(t\) be admissible. By Lemma 1.2 of the previous lesson the cut \(S(F_j,t)\) has finitely many dual components \(C_1,\dots,C_r\). Choose \(v_l\in V(C_l)\). By Lemma 1.1, \(\rho(g_n,g_nv_l)\to0\), so \(g_nv_l\to a\). By Lemma 2.1 every \(v\in V(C_l)\) has \(\rho(g_nv,g_nv_l)\le2\sigma_{j,n}(t)\). So the supremum of \(\rho(g_nv,a)\) over \(v\in V(S(F_j,t))\) tends to \(0\).

*The functions \(h_{O,U}\).* Let \(T=h_{O,U}\), where \(O\) has the conditions \((F_j;a_j,b_j)\). By Lemma 3.1(2) of the previous lesson, for \(0<t<1\) the cut \(S(T,t)\) is contained in the union of the cuts \(S(F_j,a_j+t)\) and \(S(F_j,b_j-t)\). For almost every \(t\) all these levels are admissible, because translations and reflections of the line preserve sets of measure zero. For such \(t\) the claim for \(T\) follows from the claim for the \(F_j\). For \(t<0\) and \(t>1\) the cut is empty.

*The subsequence.* Apply the first part to the finite list consisting of the \(T_i\) that lie in \(\mathcal F_0\) and of the functions \(F_j\) in the conditions of the boxes of the other \(T_i\). For the second statement choose the subsequence so that \(\sum_n\sum_j\bigl(I(F_j,g_n)+I(F_j,g_n^{-1})\bigr)<\infty\), and argue for \((g_n^{-1})\) and \(b\) in the same way. \(\blacksquare\)

## 3. Convergence

**Theorem 3.1.** Let \((g_n)\) be a sequence in \(\Gamma\) with \(g_n\to a\in B\) and \(g_n^{-1}\to b\in B\) in \(X\). Then for every closed set \(K\subseteq X\setminus\{b\}\) and every open set \(U\subseteq X\) containing \(a\),
\[
\begin{gathered}
g_n(K)\subseteq U\\
\text{for all but finitely many }n .
\end{gathered}
\]
Equivalently: if \(x_n\to x\) in \(X\) and \(x\ne b\), then \(g_nx_n\to a\).

**Proof.** The first formulation implies the second as in Lemma 1.2(3) of the lesson on convergence actions. The second implies the first: if \(g_n(K)\not\subseteq U\) for infinitely many \(n\), choose \(x_n\in K\) with \(g_nx_n\notin U\) and a subsequence with \(x_n\to x\in K\); then \(g_nx_n\to a\in U\), which is impossible. We prove the second by contradiction. If it fails, there are a subsequence and points \(x_n\to r\ne b\) with \(g_nx_n\to s\ne a\).

*Step 1: vertices.* Since \(\Gamma\) is dense in \(X\) and \(g_n\) is continuous at \(x_n\), there is a vertex \(v_n\) with \(\rho(v_n,x_n)<\frac1n\) and \(\rho(g_nv_n,g_nx_n)<\frac1n\). So \(v_n\to r\) and \(g_nv_n\to s\).

*Step 2: two cuts.* The functions in \(\mathcal F\) are the coordinates of \(X\), so there are \(F\in\mathcal F\) with \(F(r)\ne F(b)\) and \(F'\in\mathcal F\) with \(F'(s)\ne F'(a)\). Apply Proposition 2.3 to \(F,F'\), in both directions, and pass to the subsequence. Choose a level \(t\) strictly between \(F(b)\) and \(F(r)\), regular for \(F\), for which the first statement of the proposition holds; and a level \(t'\) strictly between \(F'(a)\) and \(F'(s)\), regular for \(F'\), for which the second holds. Thus, with \(S_1=S(F,t)\) and \(S_2=S(F',t')\),
\[
\begin{gathered}
\sup_{v\in V(S_1)}\rho(g_nv,a)\to0,\\
\sup_{v\in V(S_2)}\rho(g_n^{-1}v,b)\to0 .
\end{gathered}
\]

*Step 3: the side of \(r\).* Suppose \(F(b)<t<F(r)\); the other case is the same with the inequalities reversed. Let \(\Sigma=\{v\in\Gamma:F(v)>t\}\). For large \(n\), \(v_n\in\Sigma\), because \(F(v_n)\to F(r)\). The set \(N=\{y\in X:F(y)<t\}\) is an open neighbourhood of \(b\) that contains no vertex of \(\Sigma\), and it contains vertices, because \(b\) is a limit of vertices. Let \(C_n\) be the set of vertices joined to \(v_n\) by a path inside \(\Sigma\). A path in \(G\) from \(v_n\) to a vertex in \(N\) has a first edge in \(S_1\); its end \(w_n\) in \(\Sigma\) lies in \(C_n\) and in \(V(S_1)\). Hence
\[
g_nw_n\to a .
\]

*Step 4: \(g_nC_n\) does not cross the second cut.* For large \(n\), \(g_n^{-1}v\in N\) for every \(v\in V(S_2)\), so no edge of \(g_n^{-1}S_2\) has an end in \(\Sigma\). So no edge with both ends in \(C_n\) lies in \(g_n^{-1}S_2\), that is, no edge of the form \(g_ne\) with both ends of \(e\) in \(C_n\) lies in \(S_2\). The vertices \(g_nv_n\) and \(g_nw_n\) are joined by a path of such edges. Along it \(F'\) does not cross the level \(t'\), and \(t'\) is regular; so \(F'(g_nv_n)\) and \(F'(g_nw_n)\) lie on the same side of \(t'\).

*Step 5: contradiction.* \(F'(g_nv_n)\to F'(s)\) and \(F'(g_nw_n)\to F'(a)\), and \(t'\) lies strictly between \(F'(s)\) and \(F'(a)\). For large \(n\) the two values lie on opposite sides of \(t'\). \(\blacksquare\)

**Corollary 3.2.** \(\Gamma\) acts on \(B\) as a convergence group: every sequence of pairwise distinct elements of \(\Gamma\) has a subsequence \((g_n)\) and points \(a,b\in B\) such that \((g_n)\) collapses on \(B\) with repelling point \(b\) and attracting point \(a\). Here \(a\) and \(b\) are the limits in \(X\) of \(g_n\) and \(g_n^{-1}\). The space \(B\) is infinite. Consequently every element of infinite order of \(\Gamma\) is parabolic or loxodromic for the action on \(B\), and the results of the lesson on convergence actions apply.

**Proof.** A sequence of pairwise distinct elements has a subsequence with \(g_n\to a\) and \(g_n^{-1}\to b\) in \(X\), and \(a,b\in B\) by Section 1. A closed subset of \(B\setminus\{b\}\) is closed in \(X\), and an open subset of \(B\) containing \(a\) is \(U\cap B\) with \(U\) open in \(X\); since \(B\) is invariant, Theorem 3.1 gives \(g_n(K)\subseteq U\cap B\) for large \(n\). Finally \(B\) is a connected metric space with more than one point (Theorem 5.1 of the previous lesson), so it is infinite: the distances from a fixed point form a connected subset of the line containing \(0\) and a positive number. \(\blacksquare\)

## 4. Parabolic elements

**Lemma 4.1.** Let \(h\in\Gamma\) be parabolic for the action on \(B\), with fixed point \(p\). Then \(h^n\to p\) in \(X\) as \(n\to\infty\) and as \(n\to-\infty\).

**Proof.** The powers of \(h\) are pairwise distinct. Let \(z\) be the limit in \(X\) of a subsequence \((h^{n_i})\) with \(|n_i|\to\infty\); then \(z\in B\). By Lemma 1.1, \(\rho(h^{n_i},h^{n_i}h)\to0\), so \(h^{n_i+1}\to z\). Left multiplication by \(h\) is continuous on \(X\), so \(h^{n_i+1}=h\cdot h^{n_i}\to hz\). Hence \(hz=z\), and \(z=p\). Since \(X\) is compact, the whole sequences converge to \(p\). \(\blacksquare\)

**Theorem 4.2** (parabolic comparison). Let \(h\in\Gamma\) be parabolic for the action on \(B\), with fixed point \(p\). Then
\[
\rho(g,gp)\longrightarrow0\qquad(g\to\infty\text{ in }\Gamma).
\]

**Proof.** Suppose not. Then there are pairwise distinct \(g_n\) with \(g_n\to a\) and \(g_np\to c\) in \(X\), where \(a,c\in B\) and \(a\ne c\).

*Step 1: the cosets \(g_n\langle h\rangle\) tend to infinity.* That is, every finite set of vertices meets \(g_n\langle h\rangle\) for only finitely many \(n\). Otherwise some vertex \(w\) lies in \(g_n\langle h\rangle\) for infinitely many \(n\), so \(g_n=wh^{j_n}\) along a subsequence, with \(|j_n|\to\infty\) because the \(g_n\) are distinct. By Lemma 4.1 and the continuity of \(w\), \(g_n\to wp\); and \(g_np=wh^{j_n}p=wp\). So \(a=wp=c\), a contradiction.

*Step 2: small steps.* Let \(u_{n,j}=g_nh^j\) for \(j\ge0\). Then \(u_{n,0}=g_n\), and \(u_{n,j}\to g_np\) as \(j\to\infty\), by Lemma 4.1 and the continuity of \(g_n\). Let
\[
\delta_n=\sup_{j\ge0}\rho(u_{n,j},u_{n,j+1}).
\]
Since \(u_{n,j+1}=u_{n,j}h\) and all \(u_{n,j}\) lie in \(g_n\langle h\rangle\), Lemma 1.1 and Step 1 give \(\delta_n\to0\).

*Step 3: three points.* Let \(d=\rho(a,c)\) and choose \(0<d_1<d_2<d_3<d\). For large \(n\), \(\rho(a,u_{n,0})<d_1\), while \(\rho(a,u_{n,j})\to\rho(a,g_np)>d_3\) as \(j\to\infty\). So for \(i=1,2,3\) there is a first index \(j\) with \(\rho(a,u_{n,j})\ge d_i\); let \(y^i_n\) be the vertex \(u_{n,j}\) for this index. Then \(d_i\le\rho(a,y^i_n)<d_i+\delta_n\). Pass to a subsequence with \(y^i_n\to z_i\) for \(i=1,2,3\). Then \(\rho(a,z_i)=d_i\), so \(z_1,z_2,z_3\) are distinct, and they lie in \(B\) by Step 1.

*Step 4: a conjugate of \(h\).* Let \(k_n=g_nhg_n^{-1}\). Then \(k_nu_{n,j}=u_{n,j+1}\), so \(\rho(k_ny^i_n,y^i_n)\le\delta_n\) and
\[
k_ny^i_n\to z_i\qquad(i=1,2,3).
\]
If the \(k_n\) take infinitely many values, pass to a subsequence of pairwise distinct ones with \(k_n\to a'\) and \(k_n^{-1}\to b'\) in \(X\). At least two of the points \(z_i\) differ from \(b'\), and for these Theorem 3.1 gives \(k_ny^i_n\to a'\). So two of the \(z_i\) equal \(a'\), a contradiction. Otherwise some \(k\) equals \(k_n\) for infinitely many \(n\); along these, \(ky^i_n\to kz_i\) by continuity, so \(k\) fixes the three points \(z_i\) of \(B\). But \(k\) has infinite order, and an element of infinite order of a convergence group has at most two fixed points (Theorem 2.1 of the lesson on convergence actions). \(\blacksquare\)

## 5. Orbits are dense

**Lemma 5.1.** A \(\Gamma\)-invariant subset of \(B\) with at least two points is dense in \(B\).

**Proof.** Let \(Y\) be such a set and \(a\in B\). Choose vertices \(g_n\to a\) and pass to a subsequence with \(g_n^{-1}\to b\in B\). Take \(z\in Y\) with \(z\ne b\). By Theorem 3.1, \(g_nz\to a\), and \(g_nz\in Y\). \(\blacksquare\)

**Theorem 5.2.** Suppose in addition that \(\Gamma\) is torsion-free. Then every orbit of \(\Gamma\) in \(B\) is dense: \(B\) has no closed invariant subset other than \(\varnothing\) and \(B\).

**Proof.** By Lemma 5.1 it suffices to show that no point \(c\in B\) is fixed by all of \(\Gamma\): then every orbit has at least two points, and so has every nonempty closed invariant set.

Suppose \(c\) is such a point. Choose \(a\in B\) with \(a\ne c\), vertices \(g_n\to a\), and a subsequence with \(g_n^{-1}\to b\in B\). If \(b\ne c\), Theorem 3.1 gives \(c=g_nc\to a\), which is false. So \(g_n^{-1}\to c\). Choose disjoint closed subsets \(A,C\) of \(B\) that are neighbourhoods in \(B\) of \(a\) and \(c\). By Corollary 3.2, applied to \((g_n)\) and to \((g_n^{-1})\), for large \(n\)
\[
g_n(A)\subseteq A,\qquad g_n^{-1}(C)\subseteq C .
\]
Fix such an \(n\) with \(g_n\ne1\) and write \(g=g_n\). It has infinite order.

*\(g\) is not parabolic.* Suppose it is, with fixed point \(p\). For \(x\in A\) the points \(g^jx\), \(j\ge0\), lie in \(A\) and tend to \(p\) (Proposition 2.3 of the lesson on convergence actions, or \(x=p\)); so \(p\in A\). For \(y\in C\) the points \(g^{-j}y\) lie in \(C\) and tend to \(p\); so \(p\in C\). But \(A\cap C=\varnothing\).

*\(g\) is not loxodromic.* Suppose it is. It fixes \(c\), so by Corollary 3.5 of the lesson on convergence actions the stabilizer of \(c\), which is all of \(\Gamma\), contains \(\langle g\rangle\) with finite index. This contradicts Lemma 1.2.

By Corollary 3.2 no third possibility exists. \(\blacksquare\)

## 6. Exercises

**6.1.** Show that in Theorem 3.1 the points \(a\) and \(b\) may coincide, using a parabolic element.

**6.2.** Let \(g\in\Gamma\) be loxodromic for the action on \(B\), with repelling point \(b\) and attracting point \(a\). Show that \(g^n\to a\) and \(g^{-n}\to b\) in \(X\) as \(n\to\infty\).

**6.3.** Let \(F\) have finite energy and \(g_n\to\infty\). Show that there is a subsequence such that for almost every \(t\) the number of edges \(e\in S(F,t)\) with \(\lambda(g_ne)\ge\varepsilon\) tends to \(0\) for every \(\varepsilon>0\), hence is \(0\) for large \(n\).

**6.4.** Where does the proof of Theorem 3.1 use that the two cuts are taken at regular levels, and where that the levels avoid a set of measure zero?

**6.5.** Show that Lemma 5.1 holds for every convergence group on a compact metric space \(M\) in the following form: if \((g_n)\) collapses with the pair \((b,a)\), then \(a\) lies in the closure of every invariant set with at least two points.

## 7. Solutions

**6.1.** Let \(h\) be parabolic with fixed point \(p\) (if \(\Gamma\) has such an element). By Lemma 4.1, \(h^n\to p\) and \(h^{-n}\to p\), so for \(g_n=h^n\) both limits are \(p\).

**6.2.** Let \(z\) be the limit in \(X\) of a subsequence \((g^{n_i})\), \(n_i\to\infty\); then \(z\in B\), and after passing to a further subsequence \(g^{-n_i}\to z'\in B\). By Corollary 3.2 the subsequence collapses on \(B\) with repelling point \(z'\) and attracting point \(z\). By Proposition 3.1 of the lesson on convergence actions, \((g^n)_{n\ge1}\) and all its subsequences collapse with repelling point \(b\) and attracting point \(a\), and the pair is unique because \(B\) has at least three points (Lemma 1.2(5) there). So \(z=a\) and \(z'=b\). By compactness the whole sequences converge.

**6.3.** As in the proof of Proposition 2.3 choose the subsequence with \(\sum_nI(F,g_n)<\infty\); for almost every \(t\), \(\sum_{e\in S(F,t)}\Lambda_{g_n}(e)\to0\). Since \(\lambda(g_ne)\le\Lambda_{g_n}(e)\), the number of \(e\in S(F,t)\) with \(\lambda(g_ne)\ge\varepsilon\) is at most \(\varepsilon^{-1}\sum_{e\in S(F,t)}\Lambda_{g_n}(e)\), which tends to \(0\); being an integer, it is \(0\) for large \(n\).

**6.4.** Regularity of \(t\) makes every vertex lie in \(\Sigma\) or in \(N\), so that a path leaving \(\Sigma\) has an edge in \(S_1\); regularity of \(t'\) is used in Step 4, where a path that does not cross the level \(t'\) stays on one side of it. Avoiding the sets of measure zero gives the two uniform convergences of Step 2.

**6.5.** Let \(Y\subseteq M\) be invariant with at least two points, and choose \(z\in Y\) with \(z\ne b\). Then \(g_nz\to a\) by Lemma 1.2(3) of the lesson on convergence actions, and \(g_nz\in Y\).

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
