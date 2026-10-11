# Dendrites and cut points

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *dendrite* is a Peano continuum that contains no simple closed curve. Arcs are dendrites (Exercise 5.1). This lesson proves two things. First, a cohomological criterion: a Peano continuum of covering dimension at most one whose first Čech cohomology vanishes for some nonzero coefficient group is a dendrite (Corollary 2.2). Second, the structure of dendrites that makes them useful: two points of a dendrite are joined by exactly one arc, and every point strictly inside that arc is a cut point that separates them (Theorem 3.1). Together:

> a Peano continuum with more than one point, of covering dimension at most one and with vanishing first Čech cohomology, has a cut point (Corollary 3.2).

The contrapositive is how the statement is used. If a construction produces a Peano continuum with more than one point, of dimension at most one and *without* cut points, then its first Čech cohomology cannot vanish. OpenAI's proof (2026) that the first \(L^2\)-Betti number of the universal cover of a finite aspherical Poincaré complex of dimension four is zero ends in this way: from a nonzero Betti number it constructs a continuum with more than one point, without cut points, of dimension at most one and with vanishing first Čech cohomology with coefficients in \(\mathbb F_2\), shows that it is locally connected, and so contradicts Corollary 3.2 [OpenAI-S, Section 10].

The lesson uses [Every path contains an arc](every-path-contains-an-arc.md) and [First Čech cohomology of a compact metric space](first-cech-cohomology-of-a-compact-metric-space.md).

## 1. Cut points

Let \(L\) be a connected space. A point \(p\in L\) is a *cut point* of \(L\) if \(L\setminus\{p\}\) is not connected. It *separates* two points \(a,b\in L\setminus\{p\}\) if \(a\) and \(b\) lie in different components of \(L\setminus\{p\}\).

Every point of an arc other than its two endpoints is a cut point of the arc and separates the endpoints; the endpoints are not cut points (Lemma 1.1 of [Every path contains an arc](every-path-contains-an-arc.md)). A simple closed curve has no cut point (Exercise 6.2 there).

**Lemma 1.1.** Let \(L\) be a Peano continuum and \(p\in L\). Every component \(C\) of \(L\setminus\{p\}\) is open in \(L\), and if \(L\) has more than one point then \(p\in\overline C\).

**Proof.** \(L\setminus\{p\}\) is open, so its components are open by Lemma 1.2 of [Paths in locally connected spaces](paths-in-locally-connected-spaces.md). The complement of \(C\) in \(L\setminus\{p\}\) is a union of components, hence open, so \(\overline C\subseteq C\cup\{p\}\). If \(p\notin\overline C\), then \(C\) is open and closed in \(L\), nonempty, and different from \(L\), which contradicts the connectedness of \(L\). \(\blacksquare\)

## 2. A criterion for containing no simple closed curve

**Theorem 2.1.** Let \(Z\) be a compact metric space with \(\dim Z\le1\) and \(\check H^1(Z;k)=0\) for some abelian group \(k\ne0\). Then \(Z\) contains no simple closed curve.

**Proof.** A simple closed curve \(C\subseteq Z\) is compact, hence closed in \(Z\). By Corollary 5.2 of [First Čech cohomology of a compact metric space](first-cech-cohomology-of-a-compact-metric-space.md), \(\check H^1(C;k)=0\). By Corollary 4.3 of that lesson, \(\check H^1(C;k)\ne0\). \(\blacksquare\)

**Definition.** A *dendrite* is a Peano continuum that contains no simple closed curve.

**Corollary 2.2.** A Peano continuum \(L\) with \(\dim L\le1\) and \(\check H^1(L;k)=0\) for some \(k\ne0\) is a dendrite.

## 3. Arcs and cut points in a dendrite

**Theorem 3.1.** Let \(L\) be a dendrite and \(a\ne b\) two points of \(L\).

1. There is exactly one arc in \(L\) from \(a\) to \(b\). We denote it by \([a,b]\).
2. Every point \(p\in[a,b]\) other than \(a\) and \(b\) is a cut point of \(L\) and separates \(a\) and \(b\).
3. A point of \(L\) that separates \(a\) and \(b\) lies on \([a,b]\).

**Proof.** (1) An arc from \(a\) to \(b\) exists by Corollary 4.2 of [Every path contains an arc](every-path-contains-an-arc.md). If \(A\ne B\) were two such arcs, \(A\cup B\) would contain a simple closed curve by Lemma 5.2 of that lesson.

(2) Suppose \(a\) and \(b\) lie in the same component of \(L\setminus\{p\}\). By Corollary 4.3 of that lesson there is an arc \(B\) from \(a\) to \(b\) that does not contain \(p\). Then \(B\ne[a,b]\), which contradicts (1). So \(a\) and \(b\) lie in different components of \(L\setminus\{p\}\); in particular \(L\setminus\{p\}\) is not connected.

(3) If \(p\notin[a,b]\), then \([a,b]\) is a connected subset of \(L\setminus\{p\}\) containing \(a\) and \(b\), so they lie in one component. \(\blacksquare\)

So the points that separate \(a\) from \(b\) are exactly the points of \([a,b]\) other than \(a\) and \(b\).

**Corollary 3.2.** Let \(L\) be a Peano continuum with more than one point.

1. If \(L\) is a dendrite, then \(L\) has uncountably many cut points.
2. If \(\dim L\le1\) and \(\check H^1(L;k)=0\) for some abelian group \(k\ne0\), then \(L\) has a cut point.
3. If \(\dim L\le1\) and \(L\) has no cut point, then \(L\) contains a simple closed curve, and \(\check H^1(L;k)\ne0\) for every abelian group \(k\ne0\).

**Proof.** (1) Take \(a\ne b\) in \(L\). The arc \([a,b]\) minus its endpoints is in bijection with the open interval \((0,1)\), and all its points are cut points by Theorem 3.1. (2) follows from Corollary 2.2 and (1). (3) If \(L\) contained no simple closed curve, it would be a dendrite and have cut points by (1). So it contains a simple closed curve, and Theorem 2.1 excludes \(\check H^1(L;k)=0\). \(\blacksquare\)

## 4. What the hypotheses do

*Dimension.* Theorem 2.1 uses \(\dim Z\le1\) through Corollary 5.2 of the Čech lesson: a cocycle on a closed subset extends to the whole space because the nerve of a cover in which every point lies in at most two members has no triangles with three different indices, so every cochain on it is a cocycle.

*Local connectedness.* Theorem 3.1 uses it twice, to find arcs (Corollary 4.2 of the arc lesson) and to find them inside a component of \(L\setminus\{p\}\) (Corollary 4.3). The continuum \(S\) of Exercise 6.1 of [Paths in locally connected spaces](paths-in-locally-connected-spaces.md) contains no simple closed curve (Exercise 5.5), yet two of its points are joined by no arc.

*A nonzero coefficient group.* For \(k=0\) the group \(\check H^1(Z;k)\) is zero for every \(Z\), and the circle shows that Theorem 2.1 fails.

## 5. Exercises

**5.1.** Show that an arc is a dendrite.

**5.2** (two pieces with one common point). Let \(Z\) be a compact metric space and \(Z=A\cup B\) with \(A,B\) closed and \(A\cap B=\{x_0\}\). Show that if \(\check H^1(A;k)=0\) and \(\check H^1(B;k)=0\), then \(\check H^1(Z;k)=0\).

**5.3.** Let \(a,b,c\) be three distinct points of a dendrite. Show that \([a,b]\subseteq[a,c]\cup[c,b]\).

**5.4.** Let \(L\) be a dendrite and \(p\in L\). Show that every component \(C\) of \(L\setminus\{p\}\) has the property that \(C\cup\{p\}\) is connected, and that for \(a\in C\) the arc \([a,p]\) lies in \(C\cup\{p\}\).

**5.5.** Show that the closed topologist's sine curve \(S\) of Exercise 6.1 of [Paths in locally connected spaces](paths-in-locally-connected-spaces.md) contains no simple closed curve.

## 6. Solutions

**5.1.** An arc \(A\) is a Peano continuum, being homeomorphic to \([0,1]\). Let \(C\subseteq A\) be a simple closed curve. It is connected and has more than one point, so by Lemma 1.1(2) of the arc lesson it contains the subarc between any two of its points, and \(h^{-1}(C)\) is a compact interval \([s,t]\) with \(s<t\). So \(C=h([s,t])\) is an arc. But no space is both an arc and a simple closed curve (Exercise 6.2 of the arc lesson).

**5.2.** By Theorem 3.1 of the Čech lesson it suffices to split every cocycle \(c\) on the nerve of a finite open cover \((U_i)\) of \(Z\). Its restrictions to the covers \((U_i\cap A)\) of \(A\) and \((U_i\cap B)\) of \(B\) are split by locally constant maps \(h_i^A\) on \(U_i\cap A\) and \(h_i^B\) on \(U_i\cap B\). For indices \(i,j\) with \(x_0\in U_i\cap U_j\),
\[
\begin{aligned}
h_j^A(x_0)-h_i^A(x_0)&=c_{ij}\\
&=h_j^B(x_0)-h_i^B(x_0),
\end{aligned}
\]
so \(\gamma=h_i^A(x_0)-h_i^B(x_0)\) is the same for all \(i\) with \(x_0\in U_i\). Define \(h_i\) on \(U_i\) as \(h_i^A\) on \(U_i\cap A\) and \(h_i^B+\gamma\) on \(U_i\cap B\); the two rules agree at \(x_0\). On \(U_i\cap U_j\), \(h_j-h_i=c_{ij}\). It remains to see that \(h_i\) is locally constant. The sets \(A\setminus\{x_0\}=Z\setminus B\) and \(B\setminus\{x_0\}=Z\setminus A\) are open in \(Z\), and there \(h_i\) is locally constant. If \(x_0\in U_i\), there are open sets \(O_A,O_B\subseteq U_i\) containing \(x_0\) such that \(h_i^A\) is constant on \(O_A\cap A\) and \(h_i^B\) on \(O_B\cap B\). Then \(h_i\) is constant on \(O_A\cap O_B\), with the value \(h_i(x_0)\), because every point of \(O_A\cap O_B\) lies in \(O_A\cap A\) or in \(O_B\cap B\).

**5.3.** Let \(f\) run along \([a,c]\) from \(a\) to \(c\) on \([0,\frac12]\) and along \([c,b]\) from \(c\) to \(b\) on \([\frac12,1]\). This is a path from \(a\) to \(b\) with image \([a,c]\cup[c,b]\). By Theorem 4.1 of the arc lesson the image contains an arc from \(a\) to \(b\), and by Theorem 3.1(1) this arc is \([a,b]\).

**5.4.** By Lemma 1.1, \(p\in\overline C\), and a set between a connected set and its closure is connected; so \(C\cup\{p\}\) is connected. Let \(a\in C\) and \(h:[0,1]\to[a,p]\) a homeomorphism with \(h(0)=a\), \(h(1)=p\). The set \(h([0,1))=[a,p]\setminus\{p\}\) is connected, contains \(a\) and lies in \(L\setminus\{p\}\), so it lies in the component \(C\).

**5.5.** Let \(C\subseteq S\) be a simple closed curve. It is path connected. By Exercise 6.1 of the paths lesson no path in \(S\) joins \((0,0)\) to \((1,\sin1)\); the same argument shows that no path in \(S\) joins a point of \(\{0\}\times[-1,1]\) to a point of \(G\). So \(C\) lies in \(\{0\}\times[-1,1]\) or in \(G\). The first is an arc. The second is homeomorphic to \((0,1]\), and \(C\), being compact and connected, lies in a subset of it homeomorphic to a compact interval, which is an arc or a point. By Exercise 5.1 an arc contains no simple closed curve.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 10. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
