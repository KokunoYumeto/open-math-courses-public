# The compact space and its boundary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Gamma\) be a finitely presented group whose Cayley graph is one-ended and which has finite-energy functions that are not limits of finitely supported ones. This lesson builds a compact metric space \(X\) that contains \(\Gamma\) as a dense set of isolated points, on which \(\Gamma\) acts by homeomorphisms, and studies the *boundary* \(B=X\setminus\Gamma\). The results:

- the edges of the Cayley graph have square summable lengths in the metric of \(X\) (Proposition 4.2);
- \(B\) is a continuum with more than one point (Theorem 5.1);
- two vertices close to the same boundary point are joined by a path in the Cayley graph that stays close to that point (Theorem 6.2).

The space is the closure of \(\Gamma\) in a cube, embedded by countably many functions with values in \([0,1]\). The first functions are the translates of the function \(f\) of [Finite-energy functions on a Cayley complex](finite-energy-functions-on-a-cayley-complex.md), whose level sides are connected. They are not enough for the third result: a set cut out by several level conditions may have several components. So further functions are added that record in which component a vertex lies, and the work of Sections 2 and 3 is to see that there are only finitely many components to record and that the new functions still have finite energy. The construction is that of [OpenAI-S, Section 3].

Notation and results of the previous lesson are used throughout: the triangular presentation \(\Gamma=\langle S\mid R\rangle\), the Cayley graph \(G\) with edge set \(E\), cells, the relation \(e\sim e'\) with its bound \(D\), gradients, energy, cuts \(S(F,t)\), regular levels, dual adjacency.

## 1. Standing assumptions and the base functions

Throughout this lesson:

1. \(\Gamma=\langle S\mid R\rangle\) is a triangular presentation with \(\mathcal D_0\ne\mathcal D\). In particular \(\Gamma\) is infinite.
2. \(G\) is *one-ended*: for every finite set \(A\) of vertices, the graph \(G\setminus A\), obtained by deleting the vertices of \(A\) and the edges at them, has exactly one infinite component.

We fix a function \(f\) as in Theorem 4.1 of the previous lesson.

**Lemma 1.1.** For a finite set \(A\) of vertices, \(G\setminus A\) has finitely many components.

**Proof.** If \(A\) is empty there is one. Otherwise every component of \(G\setminus A\) contains a neighbour of a vertex of \(A\), because \(G\) is connected, and \(A\) has finitely many neighbours. \(\blacksquare\)

*Translates.* For \(F:\Gamma\to\mathbb R\) and \(g\in\Gamma\) let \((gF)(v)=F(g^{-1}v)\). Left multiplication by \(g\) maps the edge \((h,s)\) to \((gh,s)\) and the cell \((h,r)\) to \((gh,r)\); it preserves \(\sim\) and dual adjacency. Since \(d(gF)(gh,s)=dF(h,s)\),
\[
\begin{gathered}
\mathcal E(gF)=\mathcal E(F),\\
S(gF,t)=g\,S(F,t),
\end{gathered}
\]
and the level sides of \(gF\) are the translates of those of \(F\).

*The base family.* Let \(\mathcal F_0\) consist of all translates \(gf\), \(g\in\Gamma\), and all indicator functions \(1_{\{v\}}\), \(v\in\Gamma\). It is a countable family of functions \(\Gamma\to[0,1]\) of finite energy, and it is invariant: \(g1_{\{v\}}=1_{\{gv\}}\).

**Lemma 1.2.** Let \(F\in\mathcal F_0\) and let \(t\) be regular for \(F\). Then \(S(F,t)\) has finitely many dual components.

**Proof.** If \(t\notin(0,1)\) the cut is empty. Let \(0<t<1\). For \(F=gf\) the cut is the translate of \(S(f,t)\), which is dually connected by Theorem 4.1 of the previous lesson. For \(F=1_{\{v\}}\) the cut consists of edges at \(v\), a finite set. \(\blacksquare\)

## 2. Boxes

Let \(Q_0=[0,1]^{\mathcal F_0}\) with the product topology, and write \(z=(z_F)_{F\in\mathcal F_0}\) for its points. The *base profile* of a vertex \(v\) is the point \((F(v))_F\) of \(Q_0\).

A *box* is given by finitely many *conditions* \((F_i;a_i,b_i)\), \(1\le i\le m\), with \(F_i\in\mathcal F_0\) and real numbers \(a_i<b_i\). It stands for the open set
\[
\begin{gathered}
O=\{z\in Q_0:\ a_i<z_{F_i}<b_i\\
\text{for all }i\}
\end{gathered}
\]
and for its *vertex set* \(O(\Gamma)=\{v:\ a_i<F_i(v)<b_i\text{ for all }i\}\), the set of vertices whose base profile lies in \(O\). The \(2m\) cuts \(S(F_i,a_i)\), \(S(F_i,b_i)\) are its *endpoint cuts*. The *components* of the box are the maximal connected sets of vertices in \(O(\Gamma)\). The translate \(gO\) has the conditions \((gF_i;a_i,b_i)\); its vertex set is \(g\,O(\Gamma)\).

A box is *good* if

- every \(a_i\) and \(b_i\) is regular for \(F_i\), and
- for any two different ones among its \(2m\) endpoint cuts, say \(S\) and \(S'\), there are only finitely many pairs \((e,e')\) with \(e\in S\), \(e'\in S'\) and \(e\sim e'\).

Translates of good boxes are good.

**Lemma 2.1** (good boxes exist). Let \(z\in Q_0\) and let \(N\) be a neighbourhood of \(z\) in \(Q_0\). There is a good box \(O\) with \(z\in O\subseteq N\).

**Proof.** By the definition of the product topology there are distinct \(F_1,\dots,F_m\in\mathcal F_0\) and reals \(\alpha_i<z_{F_i}<\beta_i\) such that \(N\) contains all points with \(\alpha_i<z'_{F_i}<\beta_i\) for all \(i\). Consider the tuples
\[
\begin{gathered}
(a_1,b_1,\dots,a_m,b_m),\\
\alpha_i<a_i<z_{F_i}<b_i<\beta_i .
\end{gathered}
\]
They form a nonempty open subset \(P\) of \(\mathbb R^{2m}\), and each gives a box containing \(z\) and contained in \(N\). We show that the tuples for which the box is not good form a set of measure zero.

For each of the \(2m\) positions, the tuples whose entry there is a value of the corresponding function form a countable union of hyperplanes. For two different positions, with functions \(F\) and \(F'\) (possibly \(F=F'\)), Lemma 3.1 of the previous lesson says that the set of \((s,t)\in\mathbb R^2\) for which infinitely many pairs \(e\sim e'\) have \(e\in S(F,s)\), \(e'\in S(F',t)\) has measure zero; so the tuples whose entries at the two positions form such a pair have measure zero in \(\mathbb R^{2m}\), by Fubini's theorem. A finite union of sets of measure zero does not contain \(P\). \(\blacksquare\)

**Proposition 2.2** (finitely many components). A good box has finitely many components.

**Proof.** Let \(S_1,\dots,S_N\) be the endpoint cuts, \(S_k=S(F_{(k)},c_k)\), and let \(G'\) be the graph obtained from \(G\) by deleting all edges of \(S_1\cup\dots\cup S_N\) and keeping all vertices.

*Reduction to \(G'\).* An edge of \(G'\) crosses none of the levels, and the levels are regular; so along a path in \(G'\) each \(F_{(k)}\) stays on one side of \(c_k\). Hence \(O(\Gamma)\) is a union of components of \(G'\). Conversely an edge of \(G\) between two vertices of \(O(\Gamma)\) crosses none of the levels \(a_i,b_i\), so it is an edge of \(G'\). Therefore the components of the box are the components of \(G'\) that lie in \(O(\Gamma)\), and it suffices to show that \(G'\) has finitely many components.

*The exceptional edges.* Let \(E_0\) be the set of edges \(e\) that lie in some \(S_k\) and satisfy \(e\sim e'\) for some edge \(e'\) of another cut \(S_l\), \(l\ne k\). Since the box is good, \(E_0\) is finite.

*Dual components.* Fix \(k\). By Lemma 1.2, \(S_k\) has finitely many dual components. View \(S_k\) as a graph with dual adjacency; every edge is dually adjacent to at most \(D\) others. Deleting the finitely many elements of \(E_0\) leaves finitely many dual components of \(S_k\setminus E_0\): each of them is a dual component of \(S_k\) or contains an element dually adjacent to a deleted one.

*One component of \(G'\) on each side.* Let \(C\) be a dual component of \(S_k\setminus E_0\). Every edge of \(C\) has one end with \(F_{(k)}>c_k\), its *upper end*, and one with \(F_{(k)}<c_k\), its *lower end*. We claim that all upper ends of edges of \(C\) lie in one component of \(G'\), and likewise all lower ends. It suffices to treat two dually adjacent edges \(e,e'\in C\), which are edges of a common cell. The boundary of the cell is a closed path with at most three edges. If its vertices are not three distinct ones, or it has fewer than three edges, then any two of its edges that are not loops join the same two vertices, and the upper ends of \(e\) and \(e'\) coincide. Otherwise the cell is a triangle with three distinct vertices; if the upper ends of \(e\) and \(e'\) are different vertices \(p,p'\), the third vertex is the common lower end, and the third edge \(e''\) of the cell joins \(p\) and \(p'\). Then \(e''\notin S_k\), because both its ends are upper. And \(e''\) lies in no other cut \(S_l\): otherwise \(e\sim e''\) would put \(e\) into \(E_0\). So \(e''\) is an edge of \(G'\), and \(p,p'\) lie in the same component of \(G'\). The same argument applies to lower ends.

*Counting.* If all cuts are empty, \(G'=G\) is connected. Otherwise, if \(G'\) is not connected, every component \(Y\) of \(G'\) has an edge of \(G\) leaving it, because \(G\) is connected; this edge was deleted, so it lies in some cut and has an end in \(Y\). A cut edge lies in \(E_0\) or in a dual component of some \(S_k\setminus E_0\). The ends of the edges of \(E_0\) meet at most \(2|E_0|\) components of \(G'\), and the ends of the edges of one dual component meet at most two. So the number of components of \(G'\) is finite. \(\blacksquare\)

**Lemma 2.3.** There is a countable family \(\mathcal O\) of good boxes that is invariant under translation and is a basis of the topology of \(Q_0\): for every \(z\in Q_0\) and every neighbourhood \(N\) of \(z\) there is \(O\in\mathcal O\) with \(z\in O\subseteq N\).

**Proof.** There are countably many finite lists \(F_1,\dots,F_m\) of distinct elements of \(\mathcal F_0\). For each list the good tuples \((a_1,b_1,\dots,a_m,b_m)\) form the complement of a set of measure zero in the open set \(\{a_i<b_i\}\subseteq\mathbb R^{2m}\), by the proof of Lemma 2.1; such a set is dense, and we choose a countable dense subset of it. In the proof of Lemma 2.1 the open set \(P\) then contains one of the chosen tuples. So the chosen boxes form a countable basis. Add all translates of the chosen boxes; the family stays countable, consists of good boxes, and is invariant. \(\blacksquare\)

We fix such a family \(\mathcal O\).

## 3. Functions that record components

For a box \(O\) with conditions \((F_i;a_i,b_i)\) the *margin* is the function on \(Q_0\)
\[
\begin{gathered}
\psi_O(z)=\max\bigl(0,\ \mu_O(z)\bigr),\\
\mu_O(z)=\min_i\bigl(1,\ z_{F_i}-a_i,\ b_i-z_{F_i}\bigr).
\end{gathered}
\]
It is continuous, has values in \([0,1]\), and is positive exactly on \(O\). For a vertex \(v\) we write \(\psi_O(v)\) for its value at the base profile of \(v\). For \(O\in\mathcal O\) and a component \(U\) of \(O\), define on vertices
\[
h_{O,U}=\psi_O\cdot1_U .
\]
Let \(\mathcal F\) consist of \(\mathcal F_0\) and all functions \(h_{O,U}\) with \(O\in\mathcal O\) and \(U\) a component of \(O\). By Proposition 2.2 it is countable. It is invariant: \(g\,h_{O,U}=h_{gO,gU}\).

**Lemma 3.1.** Let \(O\in\mathcal O\) have the conditions \((F_i;a_i,b_i)\), \(1\le i\le m\), and let \(U\) be a component of \(O\).

1. For every edge, \(|dh_{O,U}(e)|\le|d\psi_O(e)|\) and \(|d\psi_O(e)|\le\max_i|dF_i(e)|\). Hence \(\mathcal E(h_{O,U})\le\sum_i\mathcal E(F_i)<\infty\).
2. For \(0<t<1\),
\[
\begin{gathered}
S(h_{O,U},t)\subseteq\bigcup_{i=1}^m\bigl(S_i^-\cup S_i^+\bigr),\\
S_i^-=S(F_i,a_i+t),\\
S_i^+=S(F_i,b_i-t).
\end{gathered}
\]
For all but countably many \(t\), the level \(t\) is regular for \(h_{O,U}\) and the levels \(a_i+t\), \(b_i-t\) are regular for \(F_i\).

**Proof.** (1) Each of the functions \(1\), \(F_i-a_i\), \(b_i-F_i\) changes along \(e\) by at most \(\max_i|dF_i(e)|\), so does their minimum, and so does its maximum with \(0\). This is the second inequality. For the first let \(e\) have ends \(p,q\). If both lie in \(U\), \(dh_{O,U}(e)=d\psi_O(e)\) up to sign; if neither does, \(dh_{O,U}(e)=0\). Let \(p\in U\) and \(q\notin U\). If \(\psi_O(q)\) were positive, \(q\) would lie in \(O(\Gamma)\) and be adjacent to \(p\), hence lie in the component \(U\). So \(\psi_O(q)=0\) and \(|dh_{O,U}(e)|=\psi_O(p)=|d\psi_O(e)|\). The energy bound follows from \(\max_i|dF_i(e)|^2\le\sum_i|dF_i(e)|^2\).

(2) Let \(e\in S(h_{O,U},t)\), with ends \(p,q\) and \(h_{O,U}(q)<t<h_{O,U}(p)\). Then \(p\in U\) and \(\psi_O(p)>t\), so \(F_i(p)-a_i>t\) and \(b_i-F_i(p)>t\) for all \(i\). At \(q\) we have \(\psi_O(q)<t\): either \(q\in U\) and \(\psi_O(q)=h_{O,U}(q)\), or \(q\notin U\) and \(\psi_O(q)=0\) as in (1). Since \(t<1\), some \(i\) has \(F_i(q)-a_i<t\) or \(b_i-F_i(q)<t\). In the first case \(F_i(q)<a_i+t<F_i(p)\), in the second \(F_i(p)<b_i-t<F_i(q)\). The exceptional \(t\) are those for which \(t\), \(a_i+t\) or \(b_i-t\) is a value of the function in question, a countable set. \(\blacksquare\)

## 4. The space \(X\)

The *profile* of a vertex \(v\) is the point \(\pi(v)=(F(v))_{F\in\mathcal F}\) of the cube \([0,1]^{\mathcal F}\). Let
\[
\begin{gathered}
X=\overline{\pi(\Gamma)}\subseteq[0,1]^{\mathcal F},\\
B=X\setminus\pi(\Gamma).
\end{gathered}
\]
For \(F\in\mathcal F\) the coordinate function \(x\mapsto x_F\) on \(X\) is continuous and equals \(F\) on vertices; we write \(F(x)\) for it. Likewise \(\psi_O\), a continuous function of the coordinates in \(\mathcal F_0\), is defined and continuous on \(X\).

**Proposition 4.1.**

1. \(X\) is a compact metrizable space, and \(\pi(\Gamma)\) is dense in \(X\).
2. \(\pi\) is injective, and every \(\pi(v)\) is an isolated point of \(X\). So \(\pi(\Gamma)\) is open and discrete, and \(B\) is closed.
3. A closed subset of \(X\) that is disjoint from \(B\) is a finite set of vertices. Every neighbourhood of a point of \(B\) contains infinitely many vertices.
4. For \(g\in\Gamma\) the map \((gx)_F=x_{g^{-1}F}\) is a homeomorphism of \(X\), this defines an action of \(\Gamma\) on \(X\), and \(g\pi(v)=\pi(gv)\). The set \(B\) is invariant.

**Proof.** (1) A countable product of intervals is compact and metrizable, and \(X\) is a closed subset. (2) Let \(v\) be a vertex and \(F=1_{\{v\}}\). The set \(\{x\in X:F(x)>\frac12\}\) is open in \(X\) and contains, among the profiles, only \(\pi(v)\). An open subset of \(X\) lies in the closure of the profiles it contains, since the profiles are dense; so this open set is \(\{\pi(v)\}\). In particular \(\pi(w)\ne\pi(v)\) for \(w\ne v\). (3) Such a set is compact and consists of isolated points, so it is finite. A point of \(B\) is a limit of profiles and is not a profile, so each of its neighbourhoods contains infinitely many. (4) The map permutes the coordinates of the cube, so it is a homeomorphism of the cube, with inverse given by \(g^{-1}\). From \((gh)^{-1}F=h^{-1}(g^{-1}F)\) it follows that \((gh)x=g(hx)\). For a vertex, \(\pi(gv)_F=F(gv)=(g^{-1}F)(v)=\pi(v)_{g^{-1}F}\). So \(g\) maps the set of profiles onto itself, hence its closure \(X\) onto itself and \(B\) onto itself. \(\blacksquare\)

From now on we identify \(v\) with \(\pi(v)\), so that \(\Gamma\subseteq X\) and \(X=\Gamma\cup B\).

*The metric.* Enumerate \(\mathcal F=\{F_1,F_2,\dots\}\), put \(c_j=2^{-j}/(1+\|dF_j\|)\), and
\[
\rho(x,y)=\sum_jc_j\,|F_j(x)-F_j(y)| .
\]
This is a metric on \(X\) that induces the product topology: the series converges uniformly, so \(\rho\) is continuous on \(X\times X\); it separates points because all \(c_j\) are positive; and a continuous metric on a compact space induces its topology. For an edge \(e\) let \(\lambda(e)=\rho(e^-,e^+)\) be its *length*.

**Proposition 4.2.** \(\sum_{e\in E}\lambda(e)^2<\infty\). In particular, for every \(\varepsilon>0\) only finitely many edges have length at least \(\varepsilon\).

**Proof.** \(\lambda=\sum_jc_j|dF_j|\) pointwise on \(E\), and \(\sum_jc_j\|dF_j\|\le\sum_j2^{-j}\). So the series converges in \(\ell^2(E)\), and its sum, which is \(\lambda\), has norm at most \(1\). \(\blacksquare\)

## 5. The boundary is a continuum

**Theorem 5.1.** Under the standing assumptions, \(B\) is a compact connected metric space with more than one point.

**Proof.** *\(B\) is not empty.* Otherwise \(X=\Gamma\) would be compact, discrete and infinite.

*\(B\) is not a single point.* Suppose \(B=\{x\}\). For \(\varepsilon>0\) the set \(\{y\in X:|f(y)-f(x)|\ge\varepsilon\}\) is closed and does not contain \(x\), so it is a finite set of vertices by Proposition 4.1(3). So \(f\) tends to the constant \(f(x)\) at infinity, contrary to Theorem 4.1 of the previous lesson.

*\(B\) is connected.* Suppose \(B=B_1\cup B_2\) with \(B_1,B_2\) disjoint, nonempty and closed. Let \(3\eta>0\) be the distance between them and \(N_i\) the set of points of \(X\) at distance less than \(\eta\) from \(B_i\). Then \(N_1,N_2\) are open and any point of \(N_1\) has distance at least \(\eta\) from any point of \(N_2\). The set \(X\setminus(N_1\cup N_2)\) is closed and disjoint from \(B\), hence a finite set \(A_0\) of vertices. Each \(N_i\) contains infinitely many vertices. An edge with one end in \(N_1\) and the other in \(N_2\) has length at least \(\eta\), so by Proposition 4.2 there are finitely many such edges. Let \(A\) be \(A_0\) together with the ends of these edges.

In \(G\setminus A\) every vertex lies in \(N_1\) or in \(N_2\), and no edge joins a vertex in \(N_1\) to one in \(N_2\). So each component of \(G\setminus A\) lies in \(N_1\) or in \(N_2\). By Lemma 1.1 there are finitely many components; since \(N_1\setminus A\) is infinite, one of the components inside \(N_1\) is infinite, and so is one inside \(N_2\). This contradicts one-endedness. \(\blacksquare\)

## 6. Paths near a boundary point

**Lemma 6.1** (the component at a point). Let \(O\in\mathcal O\) with components \(U_1,\dots,U_r\).

1. On \(X\): \(\sum_jh_{O,U_j}=\psi_O\), and \(h_{O,U_i}h_{O,U_j}=0\) for \(i\ne j\), and \(0\le h_{O,U_j}\le\psi_O\).
2. If \(x\in X\) and \(\psi_O(x)>0\), there is exactly one component \(U_O(x)\) of \(O\) with \(h_{O,U_O(x)}(x)>0\).
3. A vertex \(v\) with \(h_{O,U}(v)>0\) lies in \(U\).

**Proof.** (1) holds at vertices by the definition of the functions, and both sides of each relation are continuous on \(X\); the sum is finite by Proposition 2.2. Since vertices are dense, the relations hold on \(X\). (2) follows: the values \(h_{O,U_j}(x)\) are nonnegative, at most one is positive, and their sum is positive. (3) is the definition. \(\blacksquare\)

**Theorem 6.2** (paths near a boundary point). Let \(x\in B\) and let \(W\) be an open neighbourhood of \(x\) in \(X\). There is an open neighbourhood \(V\subseteq W\) of \(x\) such that any two vertices in \(V\) are joined by a path in \(G\) all of whose vertices lie in \(W\).

**Proof.** *Step 1: finitely many tests.* By the definition of the product topology there are a finite set \(\mathcal T\subseteq\mathcal F\) and \(\tau>0\) such that \(W\) contains
\[
\begin{gathered}
W'=\{y\in X:\ |T(y)-T(x)|<\tau\\
\text{for all }T\in\mathcal T\}.
\end{gathered}
\]
Let \(\mathcal O_{\mathcal T}\) be the finite set of boxes \(O\) for which some \(h_{O,U}\) belongs to \(\mathcal T\).

*Step 2: a small box.* Let \(x_0\in Q_0\) be the point with coordinates \(F(x)\), \(F\in\mathcal F_0\). The points \(z\in Q_0\) with the following three properties form an open neighbourhood of \(x_0\):

- \(|z_F-F(x)|<\tau\) for every \(F\in\mathcal T\cap\mathcal F_0\);
- for every \(O\in\mathcal O_{\mathcal T}\) with \(\psi_O(x)>0\): \(z\in O\) and \(|\psi_O(z)-\psi_O(x)|<\tau\);
- for every \(O\in\mathcal O_{\mathcal T}\) with \(\psi_O(x)=0\): \(\psi_O(z)<\tau\).

Since \(\mathcal O\) is a basis, there is \(O'\in\mathcal O\) containing \(x_0\) all of whose points have these properties. Then \(\psi_{O'}(x)>0\), and we let \(U'=U_{O'}(x)\), a connected set of vertices.

*Step 3: \(U'\) lies in the right components.* Let \(O\in\mathcal O_{\mathcal T}\) with \(\psi_O(x)>0\). We claim \(U'\subseteq U_O(x)\). By the second property \(O'(\Gamma)\subseteq O(\Gamma)\), so the connected set \(U'\) lies in one component \(U\) of \(O\). The set of \(y\in X\) with \(h_{O',U'}(y)>0\) and \(h_{O,U_O(x)}(y)>0\) is open and contains \(x\), so it contains a vertex \(v\). By Lemma 6.1(3), \(v\in U'\subseteq U\) and \(v\in U_O(x)\). Two components with a common vertex are equal.

*Step 4: \(U'\subseteq W'\).* Let \(v\in U'\) and \(T\in\mathcal T\).

- If \(T\in\mathcal F_0\), then \(|T(v)-T(x)|<\tau\) by the first property, since the base profile of \(v\) lies in \(O'\).
- Let \(T=h_{O,U}\) with \(\psi_O(x)>0\). If \(U=U_O(x)\), then \(v\in U\) by Step 3, so \(T(v)=\psi_O(v)\), while \(T(x)=\psi_O(x)\) by Lemma 6.1; these differ by less than \(\tau\) by the second property. If \(U\ne U_O(x)\), then \(T(x)=0\), and \(T(v)=0\) because \(v\) lies in the other component \(U_O(x)\).
- Let \(T=h_{O,U}\) with \(\psi_O(x)=0\). Then \(T(x)=0\) and \(0\le T(v)\le\psi_O(v)<\tau\) by Lemma 6.1(1) and the third property.

*Step 5: the neighbourhood.* Let
\[
V=W\cap\{y\in X:\ h_{O',U'}(y)>0\}.
\]
It is open and contains \(x\). Every vertex in \(V\) lies in \(U'\) by Lemma 6.1(3). Two vertices of \(U'\) are joined by a path inside \(U'\), and \(U'\subseteq W'\subseteq W\). \(\blacksquare\)

**Corollary 6.3.** Let \(u_n,v_n\in\Gamma\) be two sequences converging in \(X\) to the same point \(x\in B\). There are paths \(P_n\) in \(G\) from \(u_n\) to \(v_n\) such that the largest distance from \(x\) to a vertex of \(P_n\) tends to \(0\).

**Proof.** For \(k\ge1\) let \(W_k\) be the open ball of radius \(\frac1k\) about \(x\) and \(V_k\) a neighbourhood as in Theorem 6.2. Choose \(n_1<n_2<\dots\) such that \(u_n,v_n\in V_k\) for all \(n\ge n_k\). For \(n_k\le n<n_{k+1}\) let \(P_n\) be a path from \(u_n\) to \(v_n\) with all vertices in \(W_k\); for \(n<n_1\) take any path. \(\blacksquare\)

The theorem is about paths of vertices of the graph. It does not say that \(B\) is locally connected.

## 7. Exercises

**7.1.** Show that the Cayley graph of \(\mathbb Z^2=\langle s,t\mid sts^{-1}t^{-1}\rangle\), after the presentation is made triangular, is one-ended, and that the Cayley graph of \(\mathbb Z\) is not.

**7.2.** Let \(O\) be the box with the two conditions \((f;a,b)\) and \((gf;a',b')\). Its vertex set is the intersection of four level sides, each of which is connected. Explain in one sentence why this does not make the vertex set connected, and say which statement of this lesson controls the number of its components.

**7.3.** Show that the function \(\lambda\) of Proposition 4.2 is invariant in the following weak sense: for every \(g\in\Gamma\) and every \(\varepsilon>0\) only finitely many edges \(e\) have \(\rho(ge^-,ge^+)\ge\varepsilon\). Is \(\rho\) itself invariant under \(\Gamma\)?

**7.4.** Let \(x\in B\) and \(O\in\mathcal O\) with \(\psi_O(x)>0\). Show that there is a neighbourhood of \(x\) in \(X\) all of whose vertices lie in \(U_O(x)\).

**7.5.** Where is one-endedness used in this lesson, and where is the finiteness of Proposition 2.2 used?

## 8. Solutions

**7.1.** The presentation \(\langle s,t,y\mid y^{-1}st,\ y^{-1}ts\rangle\) is triangular and presents \(\mathbb Z^2\): the relators say \(y=st\) and \(y=ts\). Its Cayley graph is the square grid with one diagonal in every square. Let \(A\) be finite, inside the square \([-n,n]^2\). The vertices outside this square form a connected set (walk around the square along rows and columns), and it is infinite; every other component of \(G\setminus A\) lies inside the square and is finite. For \(\mathbb Z\), removing the vertex \(0\) leaves the two infinite components of positive and of negative integers.

**7.2.** An intersection of connected sets need not be connected, as two overlapping rings in the plane show. Proposition 2.2 bounds the number of components when the box is good.

**7.3.** The edge \(ge\) has ends \(ge^-\) and \(ge^+\), and \(e\mapsto ge\) is a bijection of \(E\). So the edges with \(\rho(ge^-,ge^+)\ge\varepsilon\) are the images under \(g^{-1}\) of the edges of length at least \(\varepsilon\), finitely many by Proposition 4.2. The metric itself is not invariant in general:
\[
\begin{aligned}
&\rho(gx,gy)\\
&\ =\sum_jc_j\,|(g^{-1}F_j)(x)-(g^{-1}F_j)(y)|,
\end{aligned}
\]
and \(g^{-1}F_j\) is another member \(F_{j'}\) of the family, which enters \(\rho\) with the weight \(c_{j'}\), not \(c_j\).

**7.4.** The set \(\{y\in X:h_{O,U_O(x)}(y)>0\}\) is open and contains \(x\), and its vertices lie in \(U_O(x)\) by Lemma 6.1(3).

**7.5.** One-endedness is used once, in the proof that \(B\) is connected. Proposition 2.2 makes the sum in Lemma 6.1(1) finite, so that the relations pass from vertices to \(X\) by continuity; it also makes \(\mathcal F\) countable.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
