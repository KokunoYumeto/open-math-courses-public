# A continuum without cut points and its graph

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The boundary \(B\) of the earlier lessons either has no cut point, or it contains a block \(L\) without cut points ([A block of the boundary](a-block-of-the-boundary.md)). In both cases there is a compact connected space without cut points, of dimension at most one, together with a graph whose vertices accumulate on it and a group that acts on both. This lesson states the properties of these data that the later arguments use, in one list (Theorem 2.1), and verifies them in the two cases. Nothing else about the group and the boundary is used afterwards.

The lesson follows the last part of Section 7 of [OpenAI-S]. It uses the earlier lessons of this course and [Convergence actions and their elements](course:convergence-groups/convergence-actions-and-their-elements).

## 1. The two cases

We keep the notation of the earlier lessons: \(\Gamma\) with its finite generating set \(S\), the Cayley graph \(G\), the compact metric space \(X=\Gamma\cup B\) with metric \(\rho\), and the action of \(\Gamma\) on \(X\). We assume that \(\Gamma\) has no element of finite order other than the identity. A sequence in a group *tends to infinity* if it leaves every finite subset.

Let \(P\) be the set of cut points of \(B\).

*Case A: \(P\) is empty.* Put \(H=\Gamma\), \(L=B\), \(Y=X\), and let \(K\) be the Cayley graph \(G\), with vertex set \(I=\Gamma\).

*Case B: \(P\) is not empty.* We assume the two hypotheses on \(\Gamma\) of the lesson on a block of the boundary. With the notation of that lesson, \(r\) is a vertex of the tree of cut points outside \(P\), \(R\) the set of cut points adjacent to \(r\), \(H\) the stabilizer of \(r\), and \(L\) the closure of \(R\). Put \(Y=H\cup L\subseteq X\), and let \(K\) be the graph on \(I=R\) of Proposition 2.1(4) there.

In both cases \(H\) maps \(L\), \(Y\) and \(I\) to themselves, and it maps edges of \(K\) to edges.

## 2. The properties

**Theorem 2.1.** In Case A and in Case B the following hold.

1. \(Y\) is the closure of \(H\) in \(X\); it is compact, and the points of \(H\) are isolated in \(Y\). The space \(L\) is compact and connected, has more than one point and no cut point, and \(\dim L\le1\). If \(\check H^1(B;k)=0\) for an abelian group \(k\), then \(\check H^1(L;k)=0\).
2. Let \((h_n)\) be a sequence in \(H\) with \(h_n\to a\in L\) and \(h_n^{-1}\to b\in L\). Then for every closed set \(C\subseteq Y\setminus\{b\}\) and every open subset \(U\) of \(Y\) containing \(a\), \(h_n(C)\subseteq U\) for all but finitely many \(n\).
3. \(K\) is connected and has finitely many orbits under \(H\) of vertices and of edges. Either \(I=H\) or \(I\subseteq L\). Every point of \(L\) is the limit of a sequence of pairwise distinct points of \(I\).
4. For every \(w\in I\): \(\rho(hw,h)\to0\) as \(h\to\infty\) in \(H\).
5. For every \(x\in L\) and every neighbourhood \(W\) of \(x\) in \(Y\) there is a neighbourhood \(V\) of \(x\) in \(Y\) such that any two points of \(I\cap V\) are joined by a path in \(K\) all of whose points lie in \(W\).
6. If \(I\subseteq L\), then for every \(p\in I\) there is an element \(h\in H\) of infinite order with \(hp=p\) and \(h^jz\to p\) as \(j\to\infty\), for every \(z\in L\).

In Case A, statement (4) says that right multiplication by a fixed element moves far vertices very little; in Case B it compares a group element with the image of a cut point. In both cases it is the link between the graph and the group.

## 3. Case A

Here \(H=\Gamma\), \(Y=X\), \(L=B\), and \(K=G\) with \(I=\Gamma\).

(1) \(\Gamma\) is dense in \(X\) and its points are isolated (Proposition 4.1 of [The compact space and its boundary](the-compact-space-and-its-boundary.md)). \(B\) is compact and connected with more than one point (Theorem 5.1 there), it has no cut point by the assumption of this case, and \(\dim B\le1\) (Theorem 2.3 of [Dimension and cohomology of the boundary](dimension-and-cohomology-of-the-boundary.md)). The statement on Čech cohomology says nothing here, because \(L=B\).

(2) is Theorem 3.1 of [The convergence action](the-convergence-action.md).

(3) The Cayley graph is connected. \(\Gamma\) acts transitively on its vertices, and every edge is a translate of an edge \(\{1,s\}\) with \(s\in S\). Every neighbourhood of a point of \(B\) contains infinitely many vertices (Proposition 4.1(3) of the lesson on the compact space), so the point is the limit of a sequence of distinct vertices.

(4) is Lemma 1.1 of the lesson on the convergence action: \(\rho(u,uw)\to0\) as \(u\to\infty\), for every \(w\in\Gamma\).

(5) is Theorem 6.2 of the lesson on the compact space.

(6) There is nothing to show, since \(I\) does not lie in \(L\).

## 4. Case B

We use the lesson on a block of the boundary: the statements (T1) to (T4) and (1) of its Section 1, Lemma 1.1, Proposition 2.1, Lemma 2.2, Proposition 3.1 and Theorem 4.1.

(1) *The closure of \(H\).* Let \((h_n)\) be a sequence in \(H\) that tends to infinity and converges in \(X\), to a point \(x\); then \(x\in B\). Fix \(p\in R\). The points \(h_np\) lie in \(R\), and \(\rho(h_n,h_np)\to0\) by (1) of that lesson. So \(h_np\to x\), and \(x\in L\). Hence the closure of \(H\) lies in \(H\cup L\). Conversely let \(p\in R\). The group \(H_p\) is infinite; take pairwise distinct \(h_n\in H_p\). Then \(\rho(h_n,p)=\rho(h_n,h_np)\to0\), so \(p\) lies in the closure of \(H\). So does \(L\), the closure of \(R\). The closure of \(H\) is therefore \(Y\); it is compact, and its points in \(H\) are isolated, because they are isolated in \(X\). The properties of \(L\) are Theorem 4.1 of that lesson.

(2) is Theorem 3.1 of the lesson on the convergence action, for the sequence \((h_n)\) and the sets \(C\) and \(U'\), where \(U'\) is an open subset of \(X\) with \(U'\cap Y=U\); the set \(C\) is closed in \(X\) because \(Y\) is.

(3) The statements on \(K\) are Proposition 2.1(4) of that lesson, and \(I=R\subseteq L\). The space \(L\) is connected with more than one point, so it has no isolated point; and \(R\) is dense in \(L\). So every neighbourhood of a point of \(L\) contains infinitely many points of \(R\).

(4) is (1) of that lesson, for \(w\in R\) and \(h\in H\).

(5) We first show: if \(a_n,b_n\in R\) both tend to \(x\in L\), there are paths in \(K\) from \(a_n\) to \(b_n\) such that the largest distance from \(x\) to a point of the \(n\)-th path tends to \(0\). If \(a_n=b_n\), take the path with the one point \(a_n\). Otherwise take the path in \(K^*\) of Proposition 3.1 of that lesson and its projected path. Since \(\pi(a_n)=a_n\ne b_n=\pi(b_n)\), the projected path is a path in \(K\) from \(a_n\) to \(b_n\) all of whose points are points of the original path (Lemma 2.2 there).

Now suppose (5) fails for some \(x\) and \(W\). Then for every \(n\) there are points \(a_n,b_n\in R\) at distance less than \(1/n\) from \(x\) that are not joined by a path in \(K\) inside \(W\). This contradicts what was just shown, because \(W\) contains a ball around \(x\) in \(Y\).

(6) Let \(p\in R\). The group \(H_p\) is infinite (Lemma 1.1 there), and its elements other than the identity have infinite order. Let \(h\) be one of them. It fixes the cut point \(p\), and the stabilizer of a cut point contains no loxodromic element (Theorem 1.1 of [The tree of cut points](course:convergence-groups/the-tree-of-cut-points)). So \(h\) is parabolic with fixed point \(p\), and \(h^jz\to p\) for every \(z\in B\) (Proposition 2.3 and Lemma 1.2(3) of the lesson on convergence actions and their elements). \(\blacksquare\)

## 5. Exercises

**5.1.** In Case B, show that \(H\) is infinite and that no point of \(H\) lies in \(L\).

**5.2.** In Case B, let \(h_n\in H\) tend to infinity. Show that every limit point of the sequence in \(X\) lies in \(L\), and that the sequence has a subsequence as in Theorem 2.1(2).

**5.3.** Show that in both cases every point of \(I\) lies on an edge of \(K\).

## 6. Solutions

**5.1.** \(H\) contains the infinite groups \(H_p\), \(p\in R\). The points of \(H\) are points of \(\Gamma\), and \(L\subseteq B\) is disjoint from \(\Gamma\).

**5.2.** The limit points lie in the closure \(Y=H\cup L\) of \(H\), and not in \(H\), because the points of \(H\) are isolated and the sequence leaves every finite set. Since \(X\) is compact, a subsequence of \((h_n)\) converges, to a point \(a\in L\); the inverses of this subsequence also tend to infinity, so a further subsequence of them converges to a point \(b\in L\).

**5.3.** \(K\) is connected and \(I\) has more than one point: in Case A, \(\Gamma\) is infinite; in Case B, \(R\) has at least two points. So every point is joined to another point by a path, whose first step is an edge at the point.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
