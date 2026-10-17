# Folding pairs and lifting cycles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The induction of [The linear bound](the-linear-bound.md) saves vertices by identifying pairs. If a set of vertices of low degree is paired up and every pair is identified, the graph loses a third of these vertices or more; the smaller *quotient* graph is decomposed by induction, and its cycles are lifted back. A quotient cycle may enter a pair at one of its two vertices and leave at the other; a connecting path through an expanding *router* then joins the two, and the [routing theorem](routing-in-graphs-with-cut-expansion.md) supplies all these paths at once. This lesson proves the two statements that make this work: the pair folding lemma, which bounds the edges lost when pairs are identified, and the batch resolution lemma, which carries out the folding and the lifting for many overlapping vertex sets together.

## 1. Pair folding

Identifying a pair \(\{u,v\}\) of vertices of a graph replaces them by one vertex adjacent to all neighbours of \(u\) and of \(v\). An edge \(uv\) becomes a loop, and two edges \(uw\), \(vw\) become parallel. To keep a simple quotient, such edges are set aside beforehand. A degree bound at the paired vertices alone does not keep their number small: pairing the \(m\) vertices of one side of a complete bipartite graph with sides of sizes \(m\) and \(a\) makes \(am/2\) pairs of edges parallel, although every paired vertex has degree \(a\). The lemma therefore also bounds, at every vertex, the number of neighbours in each folding set.

**Lemma 1.1** (pair folding). Let \(J\) be a finite simple graph and \(X_1,\dots,X_t\) pairwise disjoint subsets of \(V(J)\). Let \(a\ge1\), and suppose that \(m_i=|X_i|\ge\max\{8,a^2\}\) for every \(i\), that \(d_J(x)\le a\) for every \(x\in X_1\cup\dots\cup X_t\), and that
\[
d_i(v)=|N_J(v)\cap X_i|\le a
\]
for every \(v\in V(J)\) and every \(i\). Then there are pairings of the vertices inside each \(X_i\), leaving exactly \(m_i\bmod2\) vertices of \(X_i\) unpaired, and a set \(E_{\rm err}\subseteq E(J)\) with
\[
|E_{\rm err}|\le2\sum_im_i,
\]
such that identifying every pair in \(J-E_{\rm err}\) gives a simple graph \(Q\) in which every edge comes from exactly one remaining edge of \(J\), its *representative*. Keeping all quotient vertices, including isolated ones,
\[
|V(Q)|=|V(J)|-\sum_i\Bigl\lfloor\frac{m_i}2\Bigr\rfloor .
\]
If \(t=0\), the identity and \(E_{\rm err}=\varnothing\) satisfy the conclusion.

*Proof.* Let \(t\ge1\).

*Random pairings.* If \(m_i\) is even, choose a uniformly random perfect pairing of \(X_i\). If \(m_i\) is odd, add a dummy vertex, choose a uniformly random perfect pairing of the \(m_i+1\) vertices, and delete the dummy vertex and its pair, leaving its partner unpaired. Choose independently for different \(i\). In a uniform perfect pairing of a set of even size \(M\), the partner of a fixed vertex is uniform among the other \(M-1\) vertices, and given one pair, the remaining pairs form a uniform perfect pairing of the other \(M-2\) vertices. Hence, for distinct \(u,v\in X_i\) and for two disjoint pairs inside \(X_i\),
\[
\begin{gathered}
\Pr(\{u,v\}\text{ paired})\le\frac1{m_i-1},\\
\Pr(\text{both paired})\le\frac1{(m_i-1)(m_i-3)} .
\end{gathered}
\]
For even \(m_i\) these are equalities. For odd \(m_i\) the exact values are \(1/m_i\) and \(1/(m_i(m_i-2))\), which are smaller.

*Counting the errors.* Let \(\pi\) map every vertex to its class after the identifications; classes have one or two vertices. Let \(Z\) be the number of edges of \(J\) that become loops plus the number of unordered pairs of distinct edges of \(J\) that become the same edge, not a loop. We bound \(\mathbb EZ\). Two distinct edges of the simple graph \(J\) either share exactly one end or have four distinct ends, so the following cases are complete.

*Loops.* An edge becomes a loop exactly when its ends form a pair in some \(X_i\). The vertices of \(X_i\) have degree at most \(a\), so at most \(am_i/2\) edges lie inside \(X_i\), and the expected number of loops from \(X_i\) is at most \(am_i/(2(m_i-1))\).

*A common end.* If \(vu\) and \(vw\), with \(u\ne w\), become the same edge that is not a loop, then \(\pi(u)=\pi(w)\ne\pi(v)\); classes have at most two vertices, so \(u\) and \(w\) form a pair in some \(X_i\). For a fixed \(v\) there are \(\binom{d_i(v)}2\) such pairs \(\{u,w\}\subseteq X_i\). Since \(\binom d2\le\frac{(a-1)d}2\) for every integer \(0\le d\le a\), and
\[
\sum_{v\in V(J)}d_i(v)=\sum_{x\in X_i}d_J(x)\le am_i
\]
(both sides count the pairs of a vertex of \(X_i\) and an incident edge), the expected contribution charged to \(X_i\) is at most
\[
\frac1{m_i-1}\sum_v\binom{d_i(v)}2\le\frac{a(a-1)m_i}{2(m_i-1)} .
\]
Loops and common ends together contribute at most
\[
\sum_i\frac{a^2m_i}{2(m_i-1)}\le\frac47\sum_ia^2,
\]
since \(m_i\ge8\).

*Four distinct ends, one folding set.* If \(uv\) and \(xy\) with four distinct ends become the same edge, the two classes are \(\{u,x\},\{v,y\}\) or \(\{u,y\},\{v,x\}\); all four vertices lie in folding sets, since a class of one vertex cannot contain two of them. If both pairs lie in one \(X_i\), both edges lie inside \(X_i\). With \(e_i\le am_i/2\) edges inside \(X_i\), there are at most \(e_i^2/2\) such pairs of edges, each with two possible patterns, and the contribution is at most
\[
\begin{aligned}
&\sum_i\frac{e_i^2}{(m_i-1)(m_i-3)}\\
&\quad\le\sum_i\frac{a^2m_i^2}{4(m_i-1)(m_i-3)}\\
&\quad\le\frac{16}{35}\sum_ia^2,
\end{aligned}
\]
using \(m_i/(m_i-1)\le8/7\) and \(m_i/(m_i-3)\le8/5\).

*Four distinct ends, two folding sets.* If the two pairs lie in different sets \(X_i\) and \(X_j\), both edges join \(X_i\) to \(X_j\), and only one pattern is possible, since pairs stay inside their sets. Let \(e_{ij}\) be the number of edges between \(X_i\) and \(X_j\). There are at most \(e_{ij}^2/2\) such pairs of edges, and by independence of the two pairings the contribution is at most
\[
\begin{aligned}
&\sum_{i<j}\frac{e_{ij}^2}{2(m_i-1)(m_j-1)}\\
&\quad\le\frac{32}{49}\sum_{i<j}\frac{e_{ij}^2}{m_im_j}\le\frac{16}{49}\sum_ia^2 .
\end{aligned}
\]
For the last step, fix \(i\): since \(e_{ij}\le am_j\) and \(\sum_{j\ne i}e_{ij}\le am_i\),
\[
\sum_{j\ne i}\frac{e_{ij}^2}{m_im_j}\le\frac a{m_i}\sum_{j\ne i}e_{ij}\le a^2 ,
\]
and summing over \(i\) counts each unordered pair of sets twice.

Altogether, using \(a^2\le m_i\),
\[
\begin{aligned}
\mathbb EZ&\le\Bigl(\frac47+\frac{16}{35}+\frac{16}{49}\Bigr)\sum_ia^2\\
&=\frac{332}{245}\sum_ia^2<2\sum_im_i .
\end{aligned}
\]

*Deleting the errors.* Fix pairings with \(Z\le\mathbb EZ\). Delete every edge that becomes a loop, and in every class of \(s\ge2\) edges that become the same edge, delete all but one. Since \(s-1\le\binom s2\), at most \(Z\) edges are deleted; they form \(E_{\rm err}\). Identifying the pairs in \(J-E_{\rm err}\) gives a simple graph in which every edge has exactly one representative. No vertex is deleted, and every pair removes one vertex, which gives the order formula. \(\square\)

## 2. Batch resolution

The induction applies Lemma 1.1 not to one graph but to many graphs \(J_W\), called *batches*, whose vertex sets overlap inside a common set \(Y\). Their quotients are decomposed separately by induction, and all their cycles are lifted through the same routers. The degree bound is imposed on the union of the batches, which keeps the load on the routers independent of the number of batches.

Throughout this section \(D\) is a large real number and
\[
\begin{gathered}
a=D^{0.01},\quad L_0=D^{0.03},\\
B_0=D^{0.30},\quad\sigma=D^{0.90}.
\end{gathered}
\]

**Lemma 2.1** (batch resolution). For all sufficiently large \(D\) the following holds. Let \(Y\) be a finite set and \(\mathcal W\) a finite indexed family of subsets \(W\subseteq Y\) with \(|W|\le B_0\). For every index let \(J_W\) be a simple graph on \(W\); the \(J_W\) have pairwise disjoint edge sets, and \(F\) denotes their union, taken on \(Y\).

Let \(\mathcal R\) be a family of graphs on pairwise disjoint subsets of \(Y\), each \(R\in\mathcal R\) of order \(r_R\) with \(\sigma\le r_R\le D^{1.02}\), with \(E(R)\cap E(F)=\varnothing\), and with its edges partitioned into two spanning graphs \(P_R\) and \(T_R\), each of cut expansion at least \(\sigma/4\). Call \(P_R\) the *router* of \(R\).

For some pairs \((W,R)\) let an *active set* \(X_{W,R}\subseteq W\cap V(R)\) be given, with
\[
\begin{gathered}
|X_{W,R}|\ge L_0,\\
d_F(x)\le a\quad(x\in X_{W,R}).
\end{gathered}
\]
Sums over pairs \((W,R)\) include only active sets; put \(\Sigma_Y=\sum_{W,R}|X_{W,R}|\).

Then there are simple graphs \(Q_W\), the *quotients*, with all their vertices retained, of orders
\[
\begin{aligned}
q_W&=|W|-\sum_R\Bigl\lfloor\frac{|X_{W,R}|}2\Bigr\rfloor\\
&\le|W|-\frac13\sum_R|X_{W,R}|\le B_0,
\end{aligned}
\]
so that \(\sum_Wq_W\le\sum_W|W|-\frac13\Sigma_Y\), with the following property. For every choice of cycle-and-edge partitions of the quotients, with \(t_W\) members for \(Q_W\), there are sets \(U_R\subseteq E(P_R)\) and a cycle-and-edge partition of
\[
E(F)\cup\bigcup_{R\in\mathcal R}U_R
\]
with at most \(\sum_Wt_W+8\Sigma_Y\) members. The graphs \(R'=R-U_R\), on \(V(R)\), contain \(T_R\); the members of the partition together with the graphs \(R'\) partition \(E(F)\cup\bigcup_RE(R)\). The threshold for \(D\) is absolute.

*Proof.* The quotients are fixed first, before any router edge is used.

**2.1. Edges to heavy neighbours.** Fix a batch \(W\). Its active sets are pairwise disjoint, because the graphs \(R\) have disjoint vertex sets. For an active set \(X=X_{W,R}\) put
\[
H_X=\{v\in W:|N_{J_W}(v)\cap X|>a\},
\]
and let \(E_X\) be the set of edges of \(J_W\) between \(X\) and \(H_X\). Every vertex of an active set has degree at most \(a\) in \(J_W\subseteq F\), so \(H_X\) meets no active set of the batch. If \(H_X\ne\varnothing\), then
\[
a|H_X|<|E_X|\le\sum_{x\in X}d_{J_W}(x)\le a|X| ,
\]
so in all cases \(|H_X|\le|X|\). An edge of \(E_X\) has one end in \(X\) and the other outside every active set, so the sets \(E_X\) for different active sets are disjoint.

By Corollary 3.1 of [Paths, cycles and Lovász's decomposition theorem](paths-cycles-and-lovasz-decompositions.md), the bipartite graph on \(X\cup H_X\) with edge set \(E_X\) has a decomposition into paths with at most two ends at each vertex, hence into at most \(|X|+|H_X|\le2|X|\) paths. From each path delete the edge at each end lying in \(H_X\), as in the cycle packing argument of Conlon, Fox and Sudakov [CFS, Section 6], and make every deleted edge a single-edge member; at most two edges are deleted, and they are distinct, since a path with both ends in \(H_X\) has at least two edges. What remains of a path is either edgeless, and is ignored, or a path of even positive length with both ends in \(X\), since the paths alternate between \(X\) and \(H_X\); call it a *remnant*. Its ends are distinct. For every remnant \(L\) in \(X=X_{W,R}\), record a demand in the router \(P_R\) between the ends of \(L\), with forbidden set \(V(L)\cap V(R)\), forming a team on its own. Once this demand is routed, \(L\) is closed into a cycle. Every path of the decomposition thus gives at most two single edges and one cycle, at most \(6|X|\) members in total.

**2.2. The quotients.** Delete all sets \(E_X\) from \(J_W\), keeping the vertex set \(W\), and call the result \(J_W^0\). Active vertices still have degree at most \(a\). For an active \(X\) and \(v\in W\), either \(v\in H_X\), and all its edges to \(X\) were deleted, or \(v\) had at most \(a\) neighbours in \(X\); so \(|N_{J_W^0}(v)\cap X|\le a\). For large \(D\), \(L_0\ge\max\{8,a^2\}\). Lemma 1.1, applied to \(J_W^0\) with the active sets of \(W\) as folding sets, gives at most \(2\sum_R|X_{W,R}|\) error edges, which become single-edge members, and a simple quotient \(Q_W\) with quotient map \(\pi_W\). Every edge \(e\) of \(Q_W\) has a unique representative \(\hat e\) in \(J_W^0\).

Every pair removes one vertex. Since \(\lfloor m/2\rfloor\ge m/3\) for every integer \(m\ge2\), the order formula of Lemma 1.1 gives the bounds on \(q_W\) and \(\sum_Wq_W\). The quotients do not depend on the partitions chosen for them later.

**2.3. Switches of a quotient cycle.** Fix cycle-and-edge partitions of all quotients. A single-edge member \(e\) of a quotient partition is replaced by its representative \(\hat e\). Let \(C\) be a cycle of \(Q_W\) with vertices \(z_1,\dots,z_s\) in cyclic order, \(s\ge3\), and edges \(e_j=z_jz_{j+1}\), indices modulo \(s\). At the visit \(z_j\), let \(u_j\) be the end of \(\hat e_{j-1}\) in the class \(\pi_W^{-1}(z_j)\), and \(v_j\) the end of \(\hat e_j\) in that class. If \(u_j=v_j\), the two representatives meet at that vertex. Otherwise the class is a pair \(\{u_j,v_j\}\) inside an active set \(X_{W,R}\), and we record a *switch* demand between \(u_j\) and \(v_j\) in the router \(P_R\).

Let \(Z_C\) be the set of all ends of the representatives \(\hat e_1,\dots,\hat e_s\). Every switch demand of \(C\) in the router \(P_R\) receives the forbidden set \(Z_C\cap V(R)\), and the switch demands of \(C\) in \(P_R\) form one team. Teams of different cycles, also of different batches, are different, and differ from the one-demand teams of Section 2.1.

**2.4. The load on a router.** Fix \(R\) and collect all demands in \(P_R\), from all batches and both constructions. Every demand end lies in an active set, so it has degree at most \(a\) in \(F\). Associate with every occurrence of a vertex \(x\) as a demand end an edge of \(F\) at \(x\):

- for the demand closing a remnant \(L\), the edge of \(L\) at its end \(x\);
- for a switch with \(u_j\ne v_j\), the edge \(\hat e_{j-1}\) at the occurrence of \(u_j\), and \(\hat e_j\) at the occurrence of \(v_j\).

At a fixed vertex these edges are distinct. Remnants come from edge-disjoint paths, and the sets \(E_X\) are disjoint. A quotient edge lies in exactly one member and has one representative; a cycle visits each class once, and a switch uses its two edges at two different vertices. The two constructions use disjoint edges, because the sets \(E_X\) were deleted before folding, and different batches have disjoint edge sets, whatever their vertex sets and pairings. So the number of demand ends at \(x\) is at most \(d_F(x)\le a\).

**2.5. Supplying the connections.** A team of switch demands of a cycle \(C\) has at most \(s\le q_W\le B_0\) demands, and \(|Z_C|\le2s\le2B_0\). A remnant team has one demand, with a forbidden set of at most \(|W|\le B_0\) vertices. Apply Theorem 2.1 of [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md) once in every router \(P_R\), to all its demands, with
\[
\begin{gathered}
r=r_R,\quad h=\frac\sigma4,\quad k=a,\\
b=B_0,\quad z=2B_0 .
\end{gathered}
\]
By Corollary 2.2 there, \(\ell=O(D^{0.12}\log^2D)\) uniformly in \(R\), so
\[
\begin{aligned}
\ell^2(a+B_0)+2B_0&=O(D^{0.54}\log^4D)\\
&=o(D^{0.90}),
\end{aligned}
\]
and for large \(D\) this is at most \(\sigma/512=h/128\), the hypothesis of the theorem. If a router has no demand, nothing is used. The paths supplied in one router are pairwise edge-disjoint over all teams and batches, and paths of one team have disjoint sets of inner vertices.

**2.6. The completed cycles are cycles.** For a remnant \(L\), the supplied path has the ends of \(L\) as its ends, and its inner vertices lie in \(V(R)\) and avoid \(V(L)\cap V(R)\), hence avoid \(V(L)\). So \(L\) and the path form a cycle, with at least two edges of \(L\) and at least one of the path.

For a quotient cycle \(C\), the classes of \(z_1,\dots,z_s\) are pairwise disjoint. At a visit with \(u_j=v_j\), the representatives use one vertex of the class; at a switch, they use its two vertices, and the supplied path joins them. So, before inner vertices of supplied paths are added, the vertices used at different visits are distinct. Every supplied path for \(C\) avoids \(Z_C\) in its inner vertices, and \(Z_C\) contains all these vertices. Two supplied paths for \(C\) in one router have disjoint inner vertices, as one team; paths in different routers lie in the disjoint sets \(V(R)\). Hence the closed walk formed by the representatives and the supplied paths, in cyclic order, repeats no vertex.

One case deserves a separate word. If a visited class is a pair \(\{u,u'\}\) with \(u_j=v_j=u\), the other vertex \(u'\) need not lie in \(Z_C\) and may be an inner vertex of a supplied path. No representative of \(C\) contains \(u'\), since the representatives meet that class only at \(u\); and no second supplied path of \(C\) can contain \(u'\), by the team condition in its router and by disjointness of routers. So \(u'\) is visited at most once. The same holds for vertices of classes not visited by \(C\).

The cycle contains the \(s\ge3\) representatives, so its length is at least three. A quotient cycle without switches lifts to its representatives alone. Every member of a quotient partition gives exactly one member for \(F\).

**2.7. Accounting.** For each batch, every edge of \(J_W\) has exactly one destination: an edge deleted from a path end in Section 2.1 is a single-edge member; an edge of a remnant lies in its closed cycle; an error edge of the folding is a single-edge member; every other edge is the representative of exactly one quotient edge and lies in the lifted member of that edge. The batches have disjoint edge sets, so every edge of \(F\) is accounted for once. Let \(U_R\) be the set of edges of all paths supplied in \(P_R\); each is used once, these edges are not in \(F\), and different routers are edge-disjoint. So the members form a partition of \(E(F)\cup\bigcup_RU_R\). The heavy-neighbour work gives at most \(6\Sigma_Y\) members, the folding errors at most \(2\Sigma_Y\), and the quotient partitions exactly \(\sum_Wt_W\); supplied paths add no members. Finally \(U_R\subseteq E(P_R)\) is disjoint from \(E(T_R)\), so \(R'=R-U_R\) contains \(T_R\), and its edges are exactly the edges of \(R\) not used by a member. \(\square\)

## 3. Exercises

**3.1** (easy). Verify the example of Section 1: pairing the \(m\) vertices of one side of a complete bipartite graph with sides of sizes \(m\) (even) and \(a\) creates exactly \(am/2\) pairs of parallel edges. Which hypothesis of Lemma 1.1 fails?

**3.2** (medium). Prove the two probability formulas for a uniform perfect pairing of a set of even size \(M\): a given pair occurs with probability \(1/(M-1)\), and two given disjoint pairs both occur with probability \(1/((M-1)(M-3))\).

**3.3** (medium). Show that \(\binom d2\le\frac{(a-1)d}2\) for all integers \(0\le d\le a\).

**3.4** (medium). In Section 2.3, why must the forbidden set of a switch demand contain the ends of all representatives of \(C\), and not only those of \(\hat e_{j-1}\) and \(\hat e_j\)?

## 4. Solutions

**3.1.** Every pair \(\{u,v\}\) of the \(m\)-side becomes one vertex, and each of the \(a\) vertices \(w\) on the other side is adjacent to both \(u\) and \(v\), so the edges \(uw\) and \(vw\) become parallel: \(a\) pairs of parallel edges for each of the \(m/2\) pairs of vertices. The paired vertices have degree \(a\), but every vertex \(w\) of the other side has \(m\) neighbours in the folding set, and \(m>a\) when \(m\ge\max\{8,a^2\}\). The hypothesis \(d_i(w)\le a\) fails.

**3.2.** The number of perfect pairings of an even set of size \(M\) is \((M-1)(M-3)\cdots1\). Fixing one pair leaves a set of size \(M-2\), so a given pair occurs in a fraction \(1/(M-1)\) of all pairings; fixing two disjoint pairs leaves a set of size \(M-4\), a fraction \(1/((M-1)(M-3))\).

**3.3.** \(\binom d2=\frac{d(d-1)}2\le\frac{d(a-1)}2\) because \(d-1\le a-1\); for \(d=0\) both sides vanish.

**3.4.** A supplied path for the switch at \(z_j\) may pass near any part of the lifted cycle. If one of its inner vertices were an end of another representative \(\hat e_m\), the lifted closed walk would visit that vertex twice. Forbidding all of \(Z_C\) excludes this, and the team condition excludes collisions between two supplied paths of the same cycle.

## References

- [OpenAI-EG] OpenAI, *A linear cycle-and-edge decomposition of every graph*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
- [CFS] D. Conlon, J. Fox and B. Sudakov, *Cycle packing*, Random Structures & Algorithms 45 (2014), 608–626; arXiv:1310.0632. Removing the end edges of paths in a bipartite graph so that all ends lie on one side is used in its Section 6. https://arxiv.org/abs/1310.0632
