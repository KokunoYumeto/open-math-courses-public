# Every path contains an arc

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A path may pass through the same point many times. An *arc*, a homeomorphic image of the interval \([0,1]\), does not. This lesson proves that nothing is lost by asking for arcs: if two distinct points of a metric space are joined by a path, the image of the path contains an arc joining them (Theorem 4.1). With the theorem of [Paths in locally connected spaces](paths-in-locally-connected-spaces.md) it follows that any two points of a connected open subset of a Peano continuum are the endpoints of an arc inside that subset (Corollary 4.2).

The proof has two steps. First the loops of the path are erased, longest first, which gives a path whose fibres are intervals (Proposition 2.1). Then such a path is reparametrized to an injective one by an explicit monotone function (Proposition 3.1). The last section shows that two different arcs with the same endpoints always contain a simple closed curve (Lemma 5.2).

We assume the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): compactness, connectedness, and the fact that a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism.

## 1. Arcs and simple closed curves

An *arc* is a topological space homeomorphic to \([0,1]\). A *simple closed curve* is a space homeomorphic to the circle \(S^1=\{z\in\mathbb C:|z|=1\}\).

**Lemma 1.1.** Let \(A\) be an arc and \(h:[0,1]\to A\) a homeomorphism.

1. The points \(p\in A\) for which \(A\setminus\{p\}\) is connected are exactly \(h(0)\) and \(h(1)\).
2. Let \(u=h(s)\) and \(v=h(t)\) with \(s<t\). The set \(h([s,t])\) is an arc, and every connected subset of \(A\) that contains \(u\) and \(v\) contains \(h([s,t])\).

**Proof.** (1) For \(0<r<1\) the set \(A\setminus\{h(r)\}\) is the union of the disjoint nonempty open subsets \(h([0,r))\) and \(h((r,1])\). The sets \(A\setminus\{h(0)\}=h((0,1])\) and \(A\setminus\{h(1)\}=h([0,1))\) are connected.

(2) The map \(x\mapsto h(s+x(t-s))\) is a homeomorphism from \([0,1]\) onto \(h([s,t])\). If \(C\subseteq A\) is connected and contains \(u,v\), then \(h^{-1}(C)\) is a connected subset of \([0,1]\) containing \(s\) and \(t\), hence the interval \([s,t]\). \(\blacksquare\)

By (1) the two points \(h(0),h(1)\) do not depend on the choice of \(h\). They are the *endpoints* of \(A\), and \(A\) is an arc *from* one of them *to* the other. If \(h\) is a homeomorphism, so is \(x\mapsto h(1-x)\); so for either order of the endpoints there is a homeomorphism \(h\) with \(h(0)\) the first and \(h(1)\) the second.

By (2) the set \(h([s,t])\) is the smallest connected subset of \(A\) containing \(u\) and \(v\), so it depends only on \(A\), \(u\) and \(v\). We write \(A[u,v]\) for it; it is an arc from \(u\) to \(v\), the *subarc* of \(A\) between \(u\) and \(v\). Taking \(u,v\) to be the endpoints: a connected subset of an arc that contains both endpoints is the whole arc.

## 2. Erasing loops

**Proposition 2.1.** Let \(X\) be a metric space and \(f:[0,1]\to X\) a path from \(a\) to \(b\), with \(a\ne b\). There is a path \(g:[0,1]\to X\) from \(a\) to \(b\) with \(g([0,1])\subseteq f([0,1])\) and with the property

> (\(\ast\)) if \(x<y\) and \(g(x)=g(y)\), then \(g\) is constant on \([x,y]\).

**Proof.** *Step 1: the loops.* Let
\[
\begin{gathered}
E=\{(s,t)\in[0,1]^2:\\
s\le t,\ f(s)=f(t)\}.
\end{gathered}
\]
It is a closed subset of the square, hence compact. We choose open intervals \(I_1=(s_1,t_1)\), \(I_2=(s_2,t_2),\dots\) one after another. Suppose \(I_1,\dots,I_{n-1}\) are chosen, and let \(E_n\) be the set of \((s,t)\in E\) such that for every \(j<n\)
\[
t\le s_j\quad\text{or}\quad s\ge t_j\quad\text{or}\quad s=t .
\]
For \(s<t\) this says that the open interval \((s,t)\) is disjoint from \(I_1,\dots,I_{n-1}\). The set \(E_n\) is compact and contains the diagonal, so
\[
\ell_n=\max\{t-s:(s,t)\in E_n\}
\]
exists. If \(\ell_n=0\), stop. Otherwise choose \((s_n,t_n)\in E_n\) with \(t_n-s_n=\ell_n\) and put \(I_n=(s_n,t_n)\). So \(f(s_n)=f(t_n)\), the intervals \(I_n\) are pairwise disjoint, and since their lengths add up to at most \(1\), either there are finitely many of them or \(\ell_n\to0\).

*Step 2: the closed intervals \([s_n,t_n]\) are pairwise disjoint.* Their interiors are disjoint, so two of them could only share an endpoint: \(t_n=s_m\) for some \(n\ne m\). Then \(f(s_n)=f(t_n)=f(s_m)=f(t_m)\), so \((s_n,t_m)\in E\). Let \(k=\min(n,m)\). For \(j<k\) the interval \(I_j\) is disjoint from \(I_n\) and from \(I_m\), and it does not contain the point \(t_n\), because an open interval containing \(t_n\) meets \(I_n\). So \(I_j\) is disjoint from \((s_n,t_m)\), and \((s_n,t_m)\in E_k\). Its length \(\ell_n+\ell_m\) exceeds \(\ell_k\), which contradicts the choice of \(\ell_k\) as a maximum.

*Step 3: the path \(g\).* Let \(K=[0,1]\setminus\bigcup_nI_n\), a closed set. Define
\[
g(x)=\begin{cases}f(s_n)&\text{if }x\in[s_n,t_n],\\ f(x)&\text{otherwise.}\end{cases}
\]
By Step 2 this is well defined. Since \(f(s_n)=f(t_n)\), we have \(g=f\) on \(K\). The image of \(g\) lies in the image of \(f\), and \(g(0)=f(0)=a\), \(g(1)=f(1)=b\), because \(0\) and \(1\) lie in \(K\).

\(g\) is continuous. At a point of some \(I_n\) it is locally constant. Let \(x\in K\) and \(\varepsilon>0\), and choose \(\delta>0\) with \(d(f(y),f(x))<\varepsilon\) for \(|y-x|<\delta\). Let \(|y-x|<\delta\). If \(y\in K\), then \(g(y)=f(y)\). If \(y\in I_n\), then, as \(x\notin I_n\), an endpoint \(e\) of \(I_n\) lies between \(y\) and \(x\) or equals \(x\); so \(|e-x|<\delta\) and \(g(y)=f(e)\). In both cases \(d(g(y),g(x))<\varepsilon\).

*Step 4: property (\(\ast\)).* Let \(x<y\) with \(g(x)=g(y)\). Put \(x'=s_n\) if \(x\in[s_n,t_n]\) for some \(n\), and \(x'=x\) otherwise; put \(y'=t_m\) if \(y\in[s_m,t_m]\) for some \(m\), and \(y'=y\) otherwise. Then
\[
\begin{gathered}
x'\le x<y\le y',\qquad x',y'\in K,\\
f(x')=g(x)=g(y)=f(y').
\end{gathered}
\]
Here \(x',y'\in K\) by Step 2: an endpoint of one interval lies in no other. So \((x',y')\in E\). An interval \(I_j\) that meets the open interval \((x',y')\) lies inside it, because \(I_j\) contains neither \(x'\) nor \(y'\).

Suppose first that no \(I_j\) meets \((x',y')\). Then \((x',y')\in E_n\) for every \(n\), so \(\ell_n\ge y'-x'>0\) for every \(n\): the construction never stops and \(\ell_n\) does not tend to \(0\). This contradicts Step 1.

So some \(I_j\) lies in \((x',y')\); take the least such \(j\). Then no earlier interval meets \((x',y')\), so \((x',y')\in E_j\) and \(\ell_j\ge y'-x'\). An interval of length at least \(y'-x'\) inside \((x',y')\) is \((x',y')\) itself: \(I_j=(x',y')\). Hence \(g\) is constant on \([x',y']\), which contains \([x,y]\). \(\blacksquare\)

## 3. Paths whose fibres are intervals

**Proposition 3.1.** Let \(X\) be a metric space and \(g:[0,1]\to X\) a continuous map with \(g(0)\ne g(1)\) and with property (\(\ast\)) of Proposition 2.1. Then \(g([0,1])\) is an arc from \(g(0)\) to \(g(1)\).

**Proof.** Let \(A=g([0,1])\), a compact set, and \(\Delta\) its diameter. Let \(q_1,q_2,\dots\) be the rational numbers in \([0,1]\) and \(p_n=g(q_n)\); the points \(p_n\) are dense in \(A\). For \(x\in[0,1]\) let
\[
D_n(x)=\min_{0\le z\le x}d(p_n,g(z)),
\]
the distance from \(p_n\) to the compact set \(g([0,x])\).

*\(D_n\) is nonincreasing and continuous.* The first is clear. Let \(x<x'\) and let the minimum for \(x'\) be attained at \(z^\ast\). If \(z^\ast\le x\), then \(D_n(x)=D_n(x')\). Otherwise \(x<z^\ast\le x'\) and
\[
\begin{aligned}
D_n(x)&\le d(p_n,g(x))\\
&\le D_n(x')+d(g(z^\ast),g(x)).
\end{aligned}
\]
So
\[
\begin{aligned}
0&\le D_n(x)-D_n(x')\\
&\le\sup_{x\le z\le x'}d(g(z),g(x)),
\end{aligned}
\]
which tends to \(0\) with \(x'-x\), uniformly in \(x\), because \(g\) is uniformly continuous.

*The function \(\varphi\).* Put
\[
\varphi(x)=\sum_{n\ge1}2^{-n}\bigl(D_n(0)-D_n(x)\bigr).
\]
Each term is continuous, nondecreasing in \(x\) and between \(0\) and \(2^{-n}\Delta\). So the series converges uniformly, \(\varphi\) is continuous and nondecreasing, and \(\varphi(0)=0\).

*Claim: for \(x<y\), \(\varphi(x)=\varphi(y)\) if and only if \(g(x)=g(y)\).* If \(g(x)=g(y)\), then by (\(\ast\)) \(g\) is constant on \([x,y]\), so \(g([0,y])=g([0,x])\) and \(D_n(y)=D_n(x)\) for all \(n\). Conversely let \(g(x)\ne g(y)\). Then \(g(y)\notin g([0,x])\): if \(g(y)=g(z)\) with \(z\le x\), then \(g\) would be constant on \([z,y]\), which contains \(x\). Let \(\eta>0\) be the distance from \(g(y)\) to the compact set \(g([0,x])\), and choose \(n\) with \(d(p_n,g(y))<\eta/2\). Then
\[
\begin{gathered}
D_n(y)\le d(p_n,g(y))<\frac\eta2,\\
D_n(x)\ge\eta-d(p_n,g(y))>\frac\eta2 .
\end{gathered}
\]
So the \(n\)th term of \(\varphi\) is strictly larger at \(y\) than at \(x\), and no term is smaller. Hence \(\varphi(x)<\varphi(y)\).

*The homeomorphism.* Let \(c=\varphi(1)\). By the claim \(c>0\), since \(g(0)\ne g(1)\). By the intermediate value theorem \(\varphi\) maps \([0,1]\) onto \([0,c]\). Define
\[
h:[0,c]\to A,\qquad h(\varphi(x))=g(x).
\]
By the claim \(h\) is well defined and injective, and it is onto. It is continuous: for a closed \(F\subseteq A\), the set \(h^{-1}(F)=\varphi(g^{-1}(F))\) is the continuous image of a compact set, hence closed. A continuous bijection from the compact space \([0,c]\) onto the Hausdorff space \(A\) is a homeomorphism. Finally \(h(0)=g(0)\) and \(h(c)=g(1)\). \(\blacksquare\)

## 4. The arc theorem

**Theorem 4.1.** Let \(X\) be a metric space and \(f\) a path in \(X\) from \(a\) to \(b\), with \(a\ne b\). Then \(f([0,1])\) contains an arc from \(a\) to \(b\).

**Proof.** Proposition 2.1 gives a path \(g\) from \(a\) to \(b\) inside \(f([0,1])\) with property (\(\ast\)), and by Proposition 3.1 its image is an arc from \(a\) to \(b\). \(\blacksquare\)

**Corollary 4.2.** Let \(L\) be a locally connected complete metric space and \(U\subseteq L\) a connected open set. Any two distinct points of \(U\) are the endpoints of an arc contained in \(U\). In particular this holds for every connected open subset of a Peano continuum, and for the Peano continuum itself.

**Proof.** Theorem 4.1 of [Paths in locally connected spaces](paths-in-locally-connected-spaces.md) gives a path in \(U\) between the two points; apply Theorem 4.1. \(\blacksquare\)

**Corollary 4.3.** Let \(L\) be a Peano continuum, \(p\in L\), and let \(a\ne b\) lie in the same component of \(L\setminus\{p\}\). Then there is an arc from \(a\) to \(b\) that does not contain \(p\).

**Proof.** The set \(L\setminus\{p\}\) is open, so its component \(C\) containing \(a\) and \(b\) is open (Lemma 1.2 of the previous lesson) and connected. Corollary 4.2 gives an arc from \(a\) to \(b\) in \(C\). \(\blacksquare\)

## 5. Two arcs with the same endpoints

**Lemma 5.1** (gluing two arcs). Let \(X\) be a Hausdorff space and \(A,B\subseteq X\) arcs, both from \(u\) to \(v\), with \(A\cap B=\{u,v\}\). Then \(A\cup B\) is a simple closed curve.

**Proof.** Choose homeomorphisms \(h_A:[0,1]\to A\) and \(h_B:[0,1]\to B\) that send \(0\) to \(u\) and \(1\) to \(v\). Define \(\Phi:S^1\to A\cup B\) by
\[
\begin{gathered}
\Phi(e^{i\pi t})=h_A(t),\qquad \Phi(e^{-i\pi t})=h_B(t)\\
(0\le t\le1).
\end{gathered}
\]
The two rules agree at \(t=0\), where both give \(u\), and at \(t=1\), where \(e^{i\pi}=e^{-i\pi}\) and both give \(v\). So \(\Phi\) is well defined, and it is continuous because it is continuous on each of the two closed half circles. It is onto. It is injective: it is injective on each half circle, and a point in the image of both lies in \(A\cap B=\{u,v\}\), which corresponds to \(t\in\{0,1\}\) on both halves, that is, to the same point of \(S^1\). A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism. \(\blacksquare\)

**Lemma 5.2.** Let \(X\) be a Hausdorff space and \(A,B\subseteq X\) arcs, both from \(a\) to \(b\). If \(A\ne B\), then \(A\cup B\) contains a simple closed curve.

**Proof.** If \(A\subseteq B\), then \(A\) is a connected subset of \(B\) containing both endpoints of \(B\), so \(A=B\) by Lemma 1.1. Hence there is a point \(p\in A\setminus B\). Let \(h:[0,1]\to A\) be a homeomorphism with \(h(0)=a\), \(h(1)=b\), and \(p=h(r)\); then \(0<r<1\), because \(a,b\in B\). The set \(T=h^{-1}(B)\) is closed, since the compact set \(B\) is closed in \(X\); it contains \(0\) and \(1\) and not \(r\). Let
\[
\begin{gathered}
s=\max(T\cap[0,r]),\\
t=\min(T\cap[r,1]).
\end{gathered}
\]
Then \(s<r<t\), the points \(u=h(s)\) and \(v=h(t)\) are distinct points of \(B\), and \(h((s,t))\) is disjoint from \(B\). The subarcs \(A[u,v]=h([s,t])\) and \(B[u,v]\) are arcs from \(u\) to \(v\) whose intersection is \(\{u,v\}\). By Lemma 5.1 their union is a simple closed curve. \(\blacksquare\)

## 6. Exercises

**6.1.** Let \(f:[0,1]\to\mathbb R\) be the path from \(0\) to \(1\) that is linear on each third of \([0,1]\), with \(f(\frac13)=\frac23\) and \(f(\frac23)=\frac13\). Find all pairs \(s<t\) with \(f(s)=f(t)\), show that \(\ell_1=\frac12\), and describe the path \(g\) of Proposition 2.1 for one choice of \(I_1\). Is the choice of \(I_1\) unique?

**6.2.** Show that a simple closed curve \(C\) stays connected when one point is removed and becomes disconnected when two points are removed. Deduce that no space is both an arc and a simple closed curve.

**6.3.** Let \(L\) be a Peano continuum. Show that for every \(\varepsilon>0\) there is \(\delta>0\) such that any two distinct points at distance less than \(\delta\) are the endpoints of an arc of diameter at most \(\varepsilon\).

**6.4.** Give a path \(f\) in the plane from \(a\) to \(b\ne a\) whose image contains two different arcs from \(a\) to \(b\).

## 7. Solutions

**6.1.** On the three thirds, \(f(x)=2x\), \(f(x)=1-x\) and \(f(x)=2x-1\). A value \(w\in[\frac13,\frac23]\) is taken at \(\frac w2\), at \(1-w\) and at \(\frac{1+w}2\); values outside this range are taken once. So the pairs are those among these three points for one \(w\). The differences are \(1-\frac{3w}2\), \(\frac{3w-1}2\) and \(\frac12\), and the first two are at most \(\frac12\) for \(w\) in the range. So \(\ell_1=\frac12\), attained by \((\frac w2,\frac{1+w}2)\) for every \(w\in[\frac13,\frac23]\): the choice is not unique. With \(w=\frac13\), \(I_1=(\frac16,\frac23)\), and \(g\) equals \(2x\) on \([0,\frac16]\), the constant \(\frac13\) on \([\frac16,\frac23]\), and \(2x-1\) on \([\frac23,1]\). This \(g\) is nondecreasing, so \(\ell_2=0\) and the construction stops.

**6.2.** It is enough to treat \(C=S^1\). The map \(t\mapsto e^{2\pi it}\) sends \((0,1)\) homeomorphically onto \(S^1\setminus\{1\}\), and rotations move any point to \(1\); so \(S^1\) minus a point is connected. \(S^1\setminus\{1,e^{2\pi ir}\}\) with \(0<r<1\) is the union of the images of \((0,r)\) and \((r,1)\), which are disjoint, nonempty and open in it. An arc has points whose removal disconnects it (Lemma 1.1), a simple closed curve has none.

**6.3.** By Exercise 6.2 of the previous lesson there is \(\delta>0\) such that points at distance less than \(\delta\) are joined by a path whose image has diameter at most \(\varepsilon\). By Theorem 4.1 this image contains an arc between them.

**6.4.** Let \(f(t)=e^{3\pi it}\), a path in the circle from \(a=1\) to \(b=-1\) that runs one and a half times around. Its image is the whole circle, which contains the upper and the lower half circle, two arcs from \(1\) to \(-1\).

## References

- OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 10, where the arc theorem is used. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
