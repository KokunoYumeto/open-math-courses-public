# Paths in locally connected spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A connected space need not be path connected: the closed topologist's sine curve of Exercise 6.1 is a compact connected subset of the plane in which some pairs of points are joined by no path. This lesson proves that local connectedness and completeness together exclude this. In a locally connected complete metric space, every connected open set is path connected (Theorem 4.1). In particular a locally connected compact connected metric space is path connected, and so is each of its connected open subsets (Corollary 4.2).

The proof constructs the path directly. A connected open set is covered by small connected open sets, any two of its points are joined by a finite chain of them (Lemma 2.1), and the chains are refined again and again while the interval \([0,1]\) is subdivided to match.

We assume the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): connected sets and components, compactness, complete metric spaces and uniformly continuous maps.

## 1. Continua and local connectedness

A *continuum* is a nonempty compact connected metric space. It is *nondegenerate* if it has more than one point.

A topological space is *locally connected* if for every point \(x\) and every open set \(U\) containing \(x\) there is a connected open set \(V\) with \(x\in V\subseteq U\). A *Peano continuum* is a locally connected continuum.

A *path* in a space \(X\) from \(a\) to \(b\) is a continuous map \(f:[0,1]\to X\) with \(f(0)=a\) and \(f(1)=b\). A space is *path connected* if any two of its points are joined by a path. A path connected space is connected, because it is a union of connected sets \(f([0,1])\) that all contain one chosen point.

For a subset \(A\) of a metric space \((L,d)\), \(\overline A\) is its closure and \(\operatorname{diam}A=\sup\{d(x,y):x,y\in A\}\) its diameter.

**Example 1.1.** A convex subset \(K\) of \(\mathbb R^n\) is locally connected: the intersection of \(K\) with an open ball is convex, convex sets are path connected by straight segments, and such intersections form a base of the topology of \(K\). So intervals, cubes and balls are locally connected. The circle is locally connected, because its small open arcs form a base and each is homeomorphic to an interval.

**Lemma 1.2** (components of open sets). In a locally connected space, every component of an open set is open.

**Proof.** Let \(U\) be open, \(C\) a component of \(U\) and \(x\in C\). Choose a connected open \(V\) with \(x\in V\subseteq U\). The union \(C\cup V\) is connected, because both sets are connected and contain \(x\), and it lies in \(U\). Since \(C\) is a maximal connected subset of \(U\), \(V\subseteq C\). \(\blacksquare\)

**Lemma 1.3** (small connected sets). Let \(L\) be a locally connected metric space, \(V\subseteq L\) open, \(x\in V\) and \(\varepsilon>0\). There is a connected open set \(W\) with \(x\in W\), \(\overline W\subseteq V\) and \(\operatorname{diam}W\le\varepsilon\).

**Proof.** Choose \(r\) with \(0<r\le\varepsilon/2\) so small that the closed ball \(\{y:d(x,y)\le r\}\) lies in \(V\). By local connectedness there is a connected open \(W\) with \(x\in W\) and \(W\) inside the open ball of radius \(r\) about \(x\). The closure of \(W\) lies in the closed ball, hence in \(V\), and \(\operatorname{diam}W\le2r\le\varepsilon\). \(\blacksquare\)

## 2. Chains

Let \(\mathcal W\) be a family of sets. A *chain in \(\mathcal W\) from \(a\) to \(b\)* is a finite sequence \(W_1,\dots,W_m\) of members of \(\mathcal W\) with
\[
\begin{gathered}
a\in W_1,\qquad b\in W_m,\\
W_i\cap W_{i+1}\ne\varnothing\quad(1\le i<m).
\end{gathered}
\]
Repeating the last member gives a longer chain from \(a\) to \(b\), so a chain can always be taken with \(m\ge2\).

**Lemma 2.1** (chain lemma). Let \(V\) be a connected space and \(\mathcal W\) a family of open subsets of \(V\) that covers \(V\). Any two points of \(V\) are joined by a chain in \(\mathcal W\).

**Proof.** Fix \(a\in V\) and let \(R\) be the set of points \(b\) that are joined to \(a\) by a chain in \(\mathcal W\). It contains \(a\): a single member of \(\mathcal W\) containing \(a\) is a chain from \(a\) to \(a\).

*\(R\) is open.* If \(W_1,\dots,W_m\) is a chain from \(a\) to \(b\), it is also a chain from \(a\) to every point of \(W_m\). So \(W_m\subseteq R\).

*\(V\setminus R\) is open.* Let \(b\notin R\) and choose \(W\in\mathcal W\) with \(b\in W\). If \(W\) contained a point \(c\in R\), a chain \(W_1,\dots,W_m\) from \(a\) to \(c\) would extend to the chain \(W_1,\dots,W_m,W\) from \(a\) to \(b\), because \(c\in W_m\cap W\). So \(W\subseteq V\setminus R\).

Since \(V\) is connected and \(R\) is nonempty, \(R=V\). \(\blacksquare\)

**Lemma 2.2** (a fine chain). Let \(L\) be a locally connected metric space, \(V\subseteq L\) a connected open set, \(a,b\in V\) and \(\varepsilon>0\). There is a chain \(W_1,\dots,W_m\) from \(a\) to \(b\), with \(m\ge2\), in which every \(W_i\) is a connected open set with
\[
\overline{W_i}\subseteq V,\qquad\operatorname{diam}W_i\le\varepsilon .
\]

**Proof.** By Lemma 1.3 the connected open sets \(W\) with \(\overline W\subseteq V\) and \(\operatorname{diam}W\le\varepsilon\) cover \(V\). Apply Lemma 2.1 to this family and lengthen the chain if \(m=1\). \(\blacksquare\)

## 3. The construction

Let \(L\) be a locally connected metric space, \(U\subseteq L\) a connected open set and \(a,b\in U\). We construct finite partitions \(\mathcal P_0,\mathcal P_1,\dots\) of \([0,1]\) into closed intervals, each refining the one before, together with

- a point \(f(r)\in U\) for every endpoint \(r\) of an interval of some \(\mathcal P_n\), and
- a connected open set \(V_I\) for every interval \(I\in\mathcal P_n\),

such that for every \(I=[s,t]\in\mathcal P_n\):

1. \(f(s)\in V_I\) and \(f(t)\in V_I\);
2. if \(n\ge1\), then \(\operatorname{diam}V_I\le2^{-n}\), and \(\overline{V_I}\subseteq V_J\) for the interval \(J\in\mathcal P_{n-1}\) that contains \(I\).

*Start.* \(\mathcal P_0=\{[0,1]\}\), \(V_{[0,1]}=U\), \(f(0)=a\), \(f(1)=b\).

*Step from \(n\) to \(n+1\).* Let \(I=[s,t]\in\mathcal P_n\). By Lemma 2.2, applied to the connected open set \(V_I\), the points \(f(s),f(t)\) and \(\varepsilon=2^{-(n+1)}\), there is a chain \(W_1,\dots,W_m\) from \(f(s)\) to \(f(t)\) with \(m\ge2\), each \(W_i\) connected and open, \(\overline{W_i}\subseteq V_I\) and \(\operatorname{diam}W_i\le2^{-(n+1)}\). Divide \(I\) into \(m\) intervals of equal length,
\[
\begin{gathered}
I_i=[r_{i-1},r_i],\\
s=r_0<r_1<\dots<r_m=t,
\end{gathered}
\]
put \(V_{I_i}=W_i\), and for \(0<i<m\) choose \(f(r_i)\in W_i\cap W_{i+1}\). The values \(f(s)\) and \(f(t)\) are kept. Both endpoints of \(I_i\) have their values in \(W_i\): for \(i=1\) because \(f(s)\in W_1\), for \(i=m\) because \(f(t)\in W_m\), and otherwise by the choice of \(f(r_{i-1})\) and \(f(r_i)\). Doing this for every \(I\in\mathcal P_n\) gives \(\mathcal P_{n+1}\); an endpoint shared by two intervals of \(\mathcal P_n\) keeps its one value, so the choices agree.

Let \(D\) be the set of all endpoints of all intervals of all \(\mathcal P_n\); the construction defines \(f:D\to U\).

**Lemma 3.1.** The construction has the following properties.

1. Every interval of \(\mathcal P_n\) has length at most \(2^{-n}\), and \(D\) is dense in \([0,1]\).
2. If \(I\in\mathcal P_n\), then \(f(D\cap I)\subseteq V_I\).
3. Let \(n\ge1\) and let \(\delta_n>0\) be the least length of an interval of \(\mathcal P_n\). If \(x,y\in D\) and \(|x-y|<\delta_n\), then \(d(f(x),f(y))\le2^{1-n}\).

**Proof.** (1) Every interval is divided into at least two equal parts at each step, so lengths at least halve. Every point of \([0,1]\) lies in an interval of \(\mathcal P_n\), hence within \(2^{-n}\) of a point of \(D\).

(2) Let \(x\in D\cap I\). Then \(x\) is an endpoint of an interval \(I'\in\mathcal P_k\) with \(I'\subseteq I\), for some \(k\ge n\). By property 1 of the construction \(f(x)\in V_{I'}\), and by property 2, applied \(k-n\) times, \(V_{I'}\subseteq V_I\).

(3) Let \(x<y\). Two distinct endpoints of \(\mathcal P_n\) are at least \(\delta_n\) apart, so at most one of them lies in the open interval between \(x\) and \(y\). Hence \(x\) and \(y\) lie in one interval \(I\in\mathcal P_n\), or in two intervals \(I,I'\in\mathcal P_n\) with a common endpoint \(r\). In the first case \(f(x),f(y)\in V_I\) by (2), and \(\operatorname{diam}V_I\le2^{-n}\). In the second case \(f(x),f(r)\in V_I\) and \(f(r),f(y)\in V_{I'}\), so \(d(f(x),f(y))\le2^{-n}+2^{-n}\). \(\blacksquare\)

## 4. Connected open sets are path connected

**Theorem 4.1.** Let \(L\) be a locally connected complete metric space and \(U\subseteq L\) a connected open set. Any two points of \(U\) are joined by a path in \(U\).

**Proof.** Let \(a,b\in U\) and carry out the construction of Section 3. By Lemma 3.1(3) the map \(f:D\to L\) is uniformly continuous: given \(\varepsilon>0\) choose \(n\ge1\) with \(2^{1-n}\le\varepsilon\); then \(|x-y|<\delta_n\) implies \(d(f(x),f(y))\le\varepsilon\). A uniformly continuous map from a dense subset of \([0,1]\) into a complete metric space extends to a continuous map \(F:[0,1]\to L\). It has \(F(0)=a\) and \(F(1)=b\).

It remains to see that \(F\) takes its values in \(U\). Let \(I\in\mathcal P_1\). The set \(D\cap I\) is dense in \(I\), because the endpoints of the intervals of \(\mathcal P_k\) inside \(I\) are within \(2^{-k}\) of every point of \(I\). So, by continuity and Lemma 3.1(2),
\[
\begin{aligned}
F(I)&\subseteq\overline{f(D\cap I)}\subseteq\overline{V_I}\\
&\subseteq V_{[0,1]}=U .
\end{aligned}
\]
The intervals of \(\mathcal P_1\) cover \([0,1]\), so \(F([0,1])\subseteq U\). \(\blacksquare\)

**Corollary 4.2.** Let \(L\) be a Peano continuum.

1. \(L\) is path connected, and every connected open subset of \(L\) is path connected.
2. Every component of an open subset of \(L\) is open and path connected.
3. For every point \(x\) and every open \(U\) containing \(x\) there is a path connected open set \(V\) with \(x\in V\subseteq U\).

**Proof.** A compact metric space is complete, so Theorem 4.1 applies to \(L\). (1) is the theorem, with \(U=L\) for the first statement. (2) follows from Lemma 1.2 and (1). For (3) take the connected open \(V\) given by local connectedness; it is path connected by (1). \(\blacksquare\)

The theorem gives paths, which may cross themselves. The lesson [Every path contains an arc](every-path-contains-an-arc.md) replaces them by injective paths.

## 5. Where each hypothesis is used

Local connectedness supplies the small connected open sets of Lemma 1.3; without it the chain lemma would still give chains of small open sets, but two points of a disconnected member cannot be joined inside it at the next stage. Completeness is used once, to extend \(f\) from \(D\) to \([0,1]\). The condition \(\overline{W_i}\subseteq V_I\) keeps the limit points inside \(U\), and \(m\ge2\) makes the intervals shrink, so that \(D\) is dense.

## 6. Exercises

**6.1** (the closed topologist's sine curve). Let
\[
\begin{gathered}
G=\{(x,\sin(1/x)):0<x\le1\},\\
S=G\cup(\{0\}\times[-1,1]).
\end{gathered}
\]
Show that \(S\) is a continuum, that \(S\) is not locally connected at \((0,0)\), and that no path in \(S\) joins \((0,0)\) to \((1,\sin1)\).

**6.2.** Let \(L\) be a Peano continuum. Show that for every \(\varepsilon>0\) there is \(\delta>0\) such that any two points \(a,b\) with \(d(a,b)<\delta\) are joined by a path whose image has diameter at most \(\varepsilon\).

**6.3** (converse of the chain lemma). Let \(V\) be a space such that for every cover of \(V\) by open sets any two points are joined by a chain in the cover. Show that \(V\) is connected.

**6.4.** Show that the product of two locally connected spaces is locally connected, and that an open subset of a locally connected space is locally connected.

**6.5.** Let \(L\) be a locally connected complete metric space and \(U\) an open subset. Show that the path components of \(U\) are its components.

## 7. Solutions

**6.1.** \(G\) is connected, as the image of \((0,1]\) under a continuous map, and \(S\) is its closure in the plane: every point \((0,y)\) with \(|y|\le1\) is a limit of points \((x_k,\sin(1/x_k))\) with \(x_k\to0\) and \(\sin(1/x_k)=y\), and a limit of points of \(G\) with first coordinates bounded away from \(0\) lies in \(G\). The closure of a connected set is connected, and \(S\) is closed and bounded. So \(S\) is a continuum.

Let \(B\) be the open disc of radius \(\frac12\) about \((0,0)\), and suppose \(V\) is a connected open subset of \(S\) with \((0,0)\in V\subseteq B\). Since \(G\) is dense in \(S\), \(V\) contains a point \((x_0,\sin(1/x_0))\) with \(x_0>0\). The first coordinate maps \(V\) onto a connected subset of \([0,1]\) containing \(0\) and \(x_0\), hence containing \([0,x_0]\). Choose \(x\in(0,x_0)\) with \(\sin(1/x)=1\). The only point of \(S\) with first coordinate \(x\) is \((x,1)\), which is not in \(B\). This contradicts \(V\subseteq B\).

Suppose \(f=(f_1,f_2):[0,1]\to S\) is a path from \((0,0)\) to \((1,\sin1)\). Let \(t_0\) be the largest \(t\) with \(f_1(t)=0\); then \(t_0<1\) and \(f_1(t)>0\) for \(t>t_0\), so \(f_2(t)=\sin(1/f_1(t))\) there. Let \(\eta>0\). By the intermediate value theorem \(f_1\) takes on \((t_0,t_0+\eta]\) every value in \((0,f_1(t_0+\eta)]\), among them values \(x\) with \(\sin(1/x)=1\) and values with \(\sin(1/x)=-1\). So \(f_2\) takes the values \(1\) and \(-1\) on every interval \((t_0,t_0+\eta]\) and is not continuous at \(t_0\).

**6.2.** By Lemma 1.3 the connected open sets of diameter at most \(\varepsilon\) cover \(L\); by compactness finitely many of them, \(W_1,\dots,W_k\), cover \(L\). Let \(\delta\) be a Lebesgue number of this cover: every set of diameter less than \(\delta\) lies in some \(W_i\). (If no such \(\delta\) existed, there would be sets \(A_j\) of diameter less than \(1/j\) in no \(W_i\); points \(x_j\in A_j\) have a subsequence converging to some \(x\in W_i\), and then \(A_j\subseteq W_i\) for large \(j\) in the subsequence.) If \(d(a,b)<\delta\), both points lie in one \(W_i\), which is connected and open, and Theorem 4.1 gives a path from \(a\) to \(b\) in \(W_i\).

**6.3.** Suppose \(V=A\cup B\) with \(A,B\) open, disjoint and nonempty, and take \(a\in A\), \(b\in B\). A chain from \(a\) to \(b\) in the cover \(\{A,B\}\) starts with \(A\) and ends with \(B\), so two consecutive members are \(A\) and \(B\); but \(A\cap B=\varnothing\).

**6.4.** Let \((x,y)\in U\subseteq X\times Y\) with \(U\) open. There are open \(U_1\ni x\), \(U_2\ni y\) with \(U_1\times U_2\subseteq U\), and connected open \(V_1,V_2\) with \(x\in V_1\subseteq U_1\), \(y\in V_2\subseteq U_2\). The set \(V_1\times V_2\) is open, and it is connected: it is the union of the connected sets \((V_1\times\{y'\})\cup(\{x\}\times V_2)\), \(y'\in V_2\), which all contain \((x,y)\). For an open subset \(O\) of a locally connected space and \(x\in U\subseteq O\) with \(U\) open in \(O\): \(U\) is open in the whole space, so there is a connected open \(V\) with \(x\in V\subseteq U\).

**6.5.** Every path component is connected, hence lies in a component. Conversely a component \(C\) of \(U\) is open in \(U\) by Lemma 1.2 (the open subset \(U\) is locally connected by Exercise 6.4), hence a connected open subset of \(L\), and it is path connected by Theorem 4.1. So \(C\) lies in one path component.

## References

- OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 10 (the statement of Theorem 4.1 for compact spaces, by the same subdivision). https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
