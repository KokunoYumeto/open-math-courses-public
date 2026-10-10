# Two competing trees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the combinatorial heart of the bin-packing construction. There are two rooted trees and a quota for every depth such that each tree, using the full quotas, can mark its vertices so that every path from the root to a leaf meets at least \(d\) marks; but when the two trees must *share* the quotas, one of them has a root-to-leaf path with no mark at all. In the packing, the two trees will be the two possible "states" of a vertex of the graph, and the quotas will be scarce auxiliary items: a vertex cannot be served cheaply in both states at once.

The argument is a counting principle: more pairwise disjoint branches than marks available in their depth range leave a branch unmarked. Chalermsook and Chuzhoy used the same principle in their tree formulation of resource minimization for fire containment. The lemma below and its proof are self-contained; the course needs nothing beyond finite trees.

## 1. Trees, markings and the lemma

A *rooted tree* is a finite tree with a distinguished vertex, its root. The *depth* of a vertex is its distance to the root, and \(V_\ell(T)\) is the set of vertices of depth \(\ell\). A *complete path* is a path from the root to a leaf. A *marking* is a set of vertices of positive depth; it *hits* a path if the path contains a marked vertex.

**Lemma 1.1 (competing trees; OpenAI, 2026).** For every integer \(d\geq1\) there are rooted trees \(T^+,T^-\), an integer \(L\geq1\) and positive integers \(p_1,\ldots,p_L\) such that:

(a) every leaf of \(T^+\) and of \(T^-\) has depth \(L\);

(b) for each \(\sigma\in\{+,-\}\) the tree \(T^\sigma\) has a marking \(\mathcal M^\sigma\) with
\[
|\mathcal M^\sigma\cap V_\ell(T^\sigma)|\leq p_\ell\quad(1\leq\ell\leq L),\qquad|\mathcal M^\sigma\cap\pi|\geq d\quad\text{for every complete path }\pi\text{ of }T^\sigma;\tag{1.1}
\]

(c) if \(\mathcal A^+\) and \(\mathcal A^-\) are markings of \(T^+\) and \(T^-\) with
\[
|\mathcal A^+\cap V_\ell(T^+)|+|\mathcal A^-\cap V_\ell(T^-)|\leq p_\ell\qquad(1\leq\ell\leq L),\tag{1.2}
\]
then \(\mathcal A^+\) misses some complete path of \(T^+\) or \(\mathcal A^-\) misses some complete path of \(T^-\).

The trees, the quotas and the markings of (b) are produced by an explicit finite procedure from \(d\).

The smallest case shows the idea (Exercise 5.1). For \(d=1\), let \(T^+\) and \(T^-\) both be a root with one child, and \(p_1=1\). Each tree can mark its child; sharing the single mark at depth one, the two trees cannot both mark theirs. For larger \(d\), each tree must be hit \(d\) times by itself, while the shared quota should not allow both trees to be hit even once; the construction below achieves this with depths of rapidly growing number.

## 2. An auxiliary tree that no marking hits completely

We build one tree \(\mathcal T\), with some vertices coloured red or blue, by \(2d-1\) *phases*. Throughout, all leaves of the tree built so far have the same depth.

*Phase \(a\).* Start with a single root, at depth \(h_0=0\). At the start of phase \(a\) (\(1\leq a\leq2d-1\)), let \(u_1,\ldots,u_N\) be the current leaves, all of depth \(h_{a-1}\), numbered in any fixed way, and put \(h_a=h_{a-1}+N\). The phase owns the depths \(h_{a-1}+1,\ldots,h_a\), with quotas
\[
p_{h_{a-1}+i}=2^{i-1}\qquad(1\leq i\leq N).\tag{2.1}
\]
For each \(i\) attach to \(u_i\) exactly \(M_i=2^i\) paths with \(i\) edges, the *spines* of \(u_i\); they share \(u_i\) and are otherwise disjoint. Their endpoints have depth \(h_{a-1}+i\); colour \(2^{i-1}\) of them red and \(2^{i-1}\) blue. If \(i<N\), attach to each spine endpoint
\[
1+\sum_{j=i+1}^N2^{j-1}\tag{2.2}
\]
paths with \(N-i\) edges, the *continuation chains*, sharing only that endpoint; their vertices are not coloured. If \(i=N\), the spine endpoints already have depth \(h_a\). All vertices added in the phase are new, except the shared starting vertices.

After the phase every leaf has depth \(h_a\), and every vertex of smaller depth has a descendant of depth \(h_a\). After the last phase put \(L=h_{2d-1}\geq1\) and let \(\mathcal T\) be the final tree. The phases own disjoint blocks of depths, so each depth \(1\leq\ell\leq L\) receives exactly one quota \(p_\ell\geq1\).

**Lemma 2.1 (no complete hit).** Every marking \(\mathcal A\) of \(\mathcal T\) with \(|\mathcal A\cap V_\ell(\mathcal T)|\leq p_\ell\) for all \(\ell\) misses some complete path of \(\mathcal T\).

*Proof.* We construct, phase by phase, a path from the root that avoids \(\mathcal A\). The root has depth zero and is not marked. Suppose the path has reached, without meeting \(\mathcal A\), a vertex \(u_i\) at the start of phase \(a\).

The spines of \(u_i\) lie in the depths \(h_{a-1}+1,\ldots,h_{a-1}+i\), where \(\mathcal A\) has at most
\[
\sum_{j=1}^i2^{j-1}=2^i-1
\]
vertices by (2.1). The \(2^i\) spines are disjoint apart from \(u_i\), so each marked vertex lies on at most one of them, and some spine contains no marked vertex. Follow it to its endpoint. If \(i=N\), this endpoint has depth \(h_a\). If \(i<N\), the continuation chains of the endpoint lie in the depths \(h_{a-1}+i+1,\ldots,h_a\), where \(\mathcal A\) has at most \(\sum_{j=i+1}^N2^{j-1}\) vertices; there is one chain more than this, by (2.2), and the chains are disjoint apart from their common start, so some chain contains no marked vertex. Follow it to depth \(h_a\).

The vertex reached is a leaf of the tree at the end of phase \(a\), that is, one of the starting vertices of phase \(a+1\). After the last phase the path is a complete path of \(\mathcal T\) avoiding \(\mathcal A\). Each phase used only the marks in its own block of depths, so the argument applies to a marking of the whole final tree. \(\square\)

## 3. Colours and the two trees

**Lemma 3.1 (colour counts).** (a) For every depth \(\ell\) there are exactly \(p_\ell\) red and \(p_\ell\) blue vertices of depth \(\ell\) in \(\mathcal T\).

(b) Every complete path of \(\mathcal T\) contains exactly \(2d-1\) coloured vertices, one in each phase.

*Proof.* (a) Write \(\ell=h_{a-1}+i\) with \(1\leq i\leq N\) in phase \(a\). Coloured vertices are spine endpoints. The endpoints of the spines of \(u_{i'}\) have depth \(h_{a-1}+i'\), and spines of other phases lie in other blocks of depths. So the coloured vertices of depth \(\ell\) are the \(2^i\) endpoints of the spines of \(u_i\): \(2^{i-1}=p_\ell\) red and as many blue.

(b) In phase \(a\) a complete path leaves its starting vertex \(u_i\) along one spine, passes its endpoint, and continues along an uncoloured chain (if \(i<N\)). So it meets exactly one coloured vertex in each phase. \(\square\)

Since \(2d-1\) coloured vertices include at least \(d\) of one colour, every complete path of \(\mathcal T\) belongs to at least one of the families
\[
\mathcal P^+=\{\pi:\pi\text{ has at least }d\text{ red vertices}\},\qquad\mathcal P^-=\{\pi:\pi\text{ has at least }d\text{ blue vertices}\}.
\]
Both families are nonempty: at every phase start one may choose a spine with a red endpoint (or a blue one) and continue to the end of the phase.

*Definition of \(T^\pm\).* Let \(T^+\) be the union of the paths in \(\mathcal P^+\), in a copy of \(\mathcal T\), with the same root, and \(T^-\) the union of the paths in \(\mathcal P^-\), in another copy. Let \(\varphi^\pm:T^\pm\to\mathcal T\) send each copied vertex to its original. The map \(\varphi^\pm\) is injective, preserves the root, adjacency and depth, and keeps colours.

**Lemma 3.2.** (a) Every leaf of \(T^\pm\) has depth \(L\), and the complete paths of \(T^\pm\) are exactly the copies of the paths in \(\mathcal P^\pm\).

(b) The red vertices of \(T^+\) form a marking \(\mathcal M^+\), and the blue vertices of \(T^-\) a marking \(\mathcal M^-\), satisfying (1.1).

*Proof.* (a) Every vertex of \(T^+\) lies on a retained path, which continues to depth \(L\); so no vertex of depth less than \(L\) is a leaf, and the leaves are copies of leaves of \(\mathcal T\). A complete path of \(T^+\) ends at a leaf, and the path from the root to a leaf in a tree is unique; it is the copy of the retained path through that leaf, which belongs to \(\mathcal P^+\). The same holds for \(T^-\).

(b) Coloured vertices have positive depth. By Lemma 3.1(a) and injectivity of \(\varphi^+\), \(T^+\) has at most \(p_\ell\) red vertices of depth \(\ell\). By (a), every complete path of \(T^+\) is a copy of a path with at least \(d\) red vertices. The same argument applies to blue vertices in \(T^-\). \(\square\)

## 4. Proof of the lemma

Lemma 3.2 gives (a) and (b) of Lemma 1.1. For (c), suppose that \(\mathcal A^+\) and \(\mathcal A^-\) satisfy (1.2) and hit every complete path of \(T^+\) and of \(T^-\) respectively. Put
\[
\mathcal A=\varphi^+(\mathcal A^+)\cup\varphi^-(\mathcal A^-).
\]
Since \(\varphi^\pm\) preserve depth,
\[
|\mathcal A\cap V_\ell(\mathcal T)|\leq|\mathcal A^+\cap V_\ell(T^+)|+|\mathcal A^-\cap V_\ell(T^-)|\leq p_\ell,
\]
and \(\mathcal A\) consists of vertices of positive depth. By Lemma 2.1 some complete path \(\pi\) of \(\mathcal T\) avoids \(\mathcal A\). The path \(\pi\) lies in \(\mathcal P^+\) or in \(\mathcal P^-\), say in \(\mathcal P^+\). Its copy is a complete path of \(T^+\) (Lemma 3.2(a)), hence contains a vertex of \(\mathcal A^+\), whose image lies on \(\pi\) and in \(\mathcal A\). This contradicts the choice of \(\pi\). The case \(\pi\in\mathcal P^-\) is the same. \(\square\)

The construction is finite and explicit: each phase adds finitely many specified vertices, and the pruning is decided by counting colours along the finitely many complete paths. Only the sizes matter later through two numbers: the total quota \(P=\sum_\ell p_\ell\) and a bound \(D_*\) on the number of children of a vertex. Both depend only on \(d\).

## 5. Exercises

**5.1.** Carry out the construction for \(d=1\). Show that \(\mathcal T\) is a root with two children, one red and one blue, \(L=1\), \(p_1=1\), and that \(T^+\) and \(T^-\) are single edges.

**5.2.** For \(d=2\), show that phase 1 creates two vertices of depth 1, phase 2 creates the depths 2 and 3, and that at the start of phase 3 there are \(N=10\) leaves. Conclude \(L=13\).

**5.3.** In Lemma 2.1, where would the argument fail if each \(u_i\) had only \(2^i-1\) spines? And if the number (2.2) of continuation chains were one smaller?

**5.4.** Show directly, without Lemma 2.1, that in the case \(d=1\) of Exercise 5.1 the full tree \(\mathcal T\) cannot be hit completely by a marking with \(p_1=1\), and explain why this is the same statement as (c) there.

**5.5.** Show that \(\mathcal M^+\) hits every complete path of \(T^+\) at least \(d\) times, but that a complete path of \(\mathcal T\) not in \(\mathcal P^+\) may be hit by the red vertices only \(d-1\) times. Why does the proof of (c) never need to know which of \(\mathcal P^\pm\) a path of \(\mathcal T\) belongs to in advance?

## 6. Solutions

**5.1.** With \(d=1\) there is one phase, starting from the root alone, so \(N=1\), \(h_1=1\), \(p_1=2^0=1\). The root gets \(M_1=2\) spines of one edge, one endpoint red and one blue; since \(i=N\) there are no continuation chains. A complete path has one coloured vertex; \(\mathcal P^+\) is the path to the red child, \(\mathcal P^-\) the path to the blue child.

**5.2.** Phase 1 (\(N=1\)) gives the root two children, \(h_1=1\). Phase 2 starts with \(N=2\) leaves \(u_1,u_2\), owns depths 2 and 3 with \(p_2=1\), \(p_3=2\). The vertex \(u_1\) gets \(2\) spines of one edge, and each endpoint gets \(1+2^1=3\) chains of one edge: \(6\) leaves. The vertex \(u_2\) gets \(4\) spines of two edges: \(4\) leaves. So phase 3 starts with \(N=10\) leaves at depth \(3\) and owns depths \(4,\ldots,13\).

**5.3.** With \(2^i-1\) spines, the at most \(2^i-1\) marks in the spine depths could place one mark on every spine, and the path could not continue. With one chain fewer, the marks in the remaining depths of the phase could hit every chain. Either way the counting fails by exactly one, which is why the counts are chosen as they are.

**5.4.** \(\mathcal T\) has two complete paths, through the red and the blue child; with one mark at depth one, one child stays unmarked. A marking of \(\mathcal T\) with quota \(p_1\) is the same as a pair of markings of the two single edges \(T^+\), \(T^-\) with combined quota \(p_1\), which is (c).

**5.5.** A complete path of \(T^+\) is a copy of a path with at least \(d\) red vertices, all of which are in \(\mathcal M^+\). A path of \(\mathcal T\) with \(d\) blue and \(d-1\) red vertices lies in \(\mathcal P^-\setminus\mathcal P^+\). In the proof of (c), the unhit path \(\pi\) is produced by Lemma 2.1; only then does one look at which family contains it, and either answer gives a contradiction.

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
- P. Chalermsook and J. Chuzhoy (2010) are named for credit for the disjoint-branch counting principle in their work on resource minimization for fire containment; the course does not use their results.
