# Mapping a pretree to the completion of a subset

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M\) be a pretree and \(T\) a subset, for example a connected Hausdorff space \(M\) with a set \(T\) of cut points ([Cut points of a connected space](cut-points-of-a-connected-space.md)). The subset \(T\) is a pretree, and it has a completion \(\Phi(T)\), the pretree of its flows ([The completion of a pretree](the-completion-of-a-pretree.md)). Every point \(x\) of \(M\) defines a flow of \(T\): the flow towards \(x\), seen from the points of \(T\). This gives a map
\[
\varphi\colon M\to\Phi(T),
\]
which is the identity on \(T\). The lesson studies this map.

- The map \(\varphi\) respects betweenness through points of \(T\) (Lemma 1.2).
- For a flow \(p\) that is not a flow towards a point of \(T\), there is a set \(R_M(p)\subseteq M\), the part of \(M\) that lies on the same side as \(p\) of every point of \(T\). The map \(\varphi\) sends each point of \(R_M(p)\) to \(p\) or to a neighbour of \(p\) (Proposition 2.3).
- If \(M\) is a compact connected Hausdorff space and \(T\) a set of cut points, then \(R_M(p)\) is not empty, closed and connected. So every point of \(\Phi(T)\) is the image of a point of \(M\) or is adjacent to the image of a point of \(T\) (Theorem 3.2).

The lesson follows Lemmas 5.10 to 5.13 and Proposition 5.14 of [Bowditch]. It uses the lessons on flows and on the completion, [Adjacent points of the completion](adjacent-points-of-the-completion.md), Lemma 6.1 of [The dense quotient of a pretree](the-dense-quotient-of-a-pretree.md), and in Section 3 the lesson on cut points.

## 1. The map

Let \(M\) be a pretree and \(T\subseteq M\) a subset, with the betweenness of \(M\). Let \(P\) be the set of flows of the pretree \(T\) and \(\Phi=\Phi(T)\) its completion, with betweenness \(\langle prq\rangle\) and intervals \([p,q]_\Phi\). For \(a\in T\), \(\bar a\) is the flow of \(T\) towards \(a\), and \(\bar T\) is the set of these flows. Intervals without a subscript are intervals of \(M\).

For \(x\in M\) let \(\varphi(x)\) be the following relation on \(T\): for \(u,v\in T\),
\[
uv.\varphi(x)\quad\Longleftrightarrow\quad v\in(u,x] .
\]
This is the restriction to \(T\) of the flow towards \(x\) in the pretree \(M\), so it is a flow of \(T\) (Section 1 of [Flows on a pretree](flows-on-a-pretree.md)). For \(x\in T\) it is the flow \(\bar x\) of \(T\), because intervals between points of \(T\), intersected with \(T\), are the intervals of the pretree \(T\). So
\[
\varphi\colon M\to\Phi(T),\qquad\varphi(x)=\bar x\ \text{ for }x\in T .
\]

We use the following facts from the lesson on the completion. For flows \(p\ne q\) of \(T\), the interval \((p,q)\) of the pretree of \(T\) with its flows is a subset of \(T\).

- (R1) For a flow \(p\ne\bar a\): \((p,\bar a)\) consists of \(a\) and of the points \(v\in T\) with \(av.p\).
- (R2) For distinct flows \(p,q\) different from \(\bar a\): \(\langle p\,\bar a\,q\rangle\) holds if and only if \(a\in(p,q)\), that is, if and only if every \(u\in T\setminus\{a\}\) has \(ua.p\) or \(ua.q\).

(R1) is Lemma 1.1(2) there; (R2) is Definition 2.1 there with the definition of the pretree of \(T\) with its flows.

**Lemma 1.1.** Let \(a\in T\), \(x\in M\) and \(v\in T\). Then \(v\in[a,x]\) if and only if \(\bar v\in[\bar a,\varphi(x)]_\Phi\).

**Proof.** Write \(p=\varphi(x)\). For \(v=a\) both statements hold. Let \(v\ne a\). Then \(v\in[a,x]\) means \(v\in(a,x]\), that is, \(av.p\).

*If \(\bar v=p\)*: then \(av.p\) holds, because \(av.\bar v\), and \(\bar v\) lies in \([\bar a,p]_\Phi\).

*If \(p=\bar a\)*: then \(av.p\) fails, and \([\bar a,p]_\Phi=\{\bar a\}\) does not contain \(\bar v\).

*Otherwise* \(\bar a\), \(\bar v\) and \(p\) are distinct, and \(\bar v\in[\bar a,p]_\Phi\) means \(\langle\bar a\,\bar v\,p\rangle\). By (R2) this means \(v\in(\bar a,p)\), and by (R1), since \(v\ne a\), it means \(av.p\). \(\blacksquare\)

**Lemma 1.2.** Let \(x,y\in M\) and \(a\in T\).

1. If \(a\in[x,y]\), then \(\bar a\in[\varphi(x),\varphi(y)]_\Phi\).
2. If \(\langle\varphi(x)\,\bar a\,\varphi(y)\rangle\), then \(xay\).
3. If \([x,y]\) contains a point of \(T\), then for every \(v\in T\): \(v\in[x,y]\) if and only if \(\bar v\in[\varphi(x),\varphi(y)]_\Phi\).

**Proof.** Write \(p=\varphi(x)\) and \(q=\varphi(y)\).

(1) Let \(a\in[x,y]\) and \(u\in T\setminus\{a\}\). We show \(ua.p\) or \(ua.q\), that is, \(a\in(u,x]\) or \(a\in(u,y]\). If \(a=x\), the first holds; if \(a=y\), the second. If \(xay\), then (T3) with the point \(u\ne a\) gives \(xau\) or \(yau\).

If \(\bar a\) is \(p\) or \(q\), it lies in \([p,q]_\Phi\). Suppose \(\bar a\) is neither \(p\) nor \(q\). If \(p=q\), then \(ua.p\) for every \(u\in T\setminus\{a\}\), and \(p=\bar a\) by Lemma 2.2 of the lesson on flows; so \(p\ne q\). Then (R2) gives \(\langle p\,\bar a\,q\rangle\).

(2) By (R2), every \(u\in T\setminus\{a\}\) has \(a\in(u,x]\) or \(a\in(u,y]\). Since \(p\ne\bar a\), there is \(u\in T\setminus\{a\}\) for which \(ua.p\) fails (Lemma 2.2 of the lesson on flows): \(a\notin(u,x]\). In particular \(a\ne x\). In the same way \(a\ne y\). For this \(u\) we have \(a\in(u,y]\), so \(uay\). By (T3) with the point \(x\ne a\): \(uax\) or \(yax\). The first is excluded. So \(xay\).

(3) Choose \(a\in[x,y]\cap T\). Then \([x,y]=[x,a]\cup[a,y]\), by Lemma 3.2 of the first lesson if \(a\) is not \(x\) or \(y\). By (1), \(\bar a\in[p,q]_\Phi\), so in the same way \([p,q]_\Phi=[p,\bar a]_\Phi\cup[\bar a,q]_\Phi\). By Lemma 1.1, \(v\in[a,x]\) if and only if \(\bar v\in[\bar a,p]_\Phi\), and likewise for \(y\) and \(q\). \(\blacksquare\)

Statement (3) can fail if \([x,y]\) contains no point of \(T\) (Exercise 5.1).

## 2. The side of a point on which a flow lies

For \(a\ne b\) in \(M\) let
\[
R_M(a,b)=\{x\in M\mid xab\ \text{fails}\}.
\]
It contains \(a\) and \(b\). It consists of \(a\) and of the points that \(a\) does not separate from \(b\): the points other than \(a\) in it form the class of \(b\) under the relation "\(a\) is not between the two points", which is an equivalence relation on \(M\setminus\{a\}\) (Lemma 3.1 of the lesson on adjacent points). So
\[
\begin{gathered}
R_M(a,b)=R_M(a,b')\\
\text{if } bab' \text{ fails}.
\end{gathered}\tag{1}
\]

Let \(a\in T\) and let \(p\) be a flow of \(T\) other than \(\bar a\). Put
\[
H(a,p)=\{b\in T\setminus\{a\}\mid ba.p\ \text{fails}\}.
\]

**Lemma 2.1.** The set \(H(a,p)\) is not empty, and \(bab'\) fails for all \(b,b'\in H(a,p)\).

**Proof.** It is not empty by Lemma 2.2 of the lesson on flows, because \(p\ne\bar a\). If \(bab'\), then (F2) gives \(ba.p\) or \(b'a.p\). \(\blacksquare\)

By Lemma 2.1 and (1) the set \(R_M(a,b)\) is the same for all \(b\in H(a,p)\). We write
\[
R_M(a,p)=R_M(a,b),\qquad b\in H(a,p).
\]
It is the side of \(a\) in \(M\) on which the points of \(T\) lie from which \(p\) does not run to \(a\).

**Lemma 2.2.** Let \(a\in T\), let \(p\ne\bar a\) be a flow of \(T\), and \(x\in R_M(a,p)\). Then \(\langle p\,\bar a\,\varphi(x)\rangle\) fails.

**Proof.** Write \(q=\varphi(x)\); we may assume \(q\ne\bar a\) and \(q\ne p\). Choose \(b\in H(a,p)\). Then \(xab\) fails. Also \(a\ne x\), because \(\varphi(a)=\bar a\). So \(a\notin(b,x]\), that is, \(ba.q\) fails. Since \(ba.p\) fails too, (R2) shows that \(\langle p\,\bar a\,q\rangle\) fails. \(\blacksquare\)

For a flow \(p\) of \(T\) that is not in \(\bar T\) let
\[
R_M(p)=\bigcap_{a\in T}R_M(a,p),
\]
with \(R_M(p)=M\) if \(T\) is empty.

**Proposition 2.3.** Let \(p\in\Phi\setminus\bar T\) and \(x\in R_M(p)\). Then either \(\varphi(x)=p\), or \(\varphi(x)=\bar a\) for a point \(a\in T\) such that \(\bar a\) and \(p\) are adjacent in \(\Phi\).

**Proof.** Let \(q=\varphi(x)\ne p\). By Lemma 2.2, \(\langle p\,\bar a\,q\rangle\) fails for every \(a\in T\). Suppose there is \(r\) with \(\langle prq\rangle\). Then \(r\notin\bar T\). Since \(p\) and \(r\) are different points outside \(\bar T\), there is a point \(\bar a\) with \(\langle p\,\bar a\,r\rangle\) (Lemma 6.1 of the lesson on the dense quotient). Then \(\langle p\,\bar a\,q\rangle\), by Lemma 3.2 of the first lesson in the pretree \(\Phi\). This is a contradiction.

So \(p\) and \(q\) are adjacent. By Theorem 2.3 of the lesson on adjacent points, exactly one of them lies in \(\bar T\); so \(q=\bar a\) for some \(a\in T\). \(\blacksquare\)

**Lemma 2.4.** Let \(p\in\Phi\setminus\bar T\) and let \(T_0\subseteq T\) be finite and not empty. Then there is a point \(b\in T_0\) that lies in \(R_M(a,p)\) for every \(a\in T_0\).

**Proof.** In the pretree of \(T\) with its flows consider the sets \((b,p)\cap T_0\), \(b\in T_0\), and choose \(b\in T_0\) for which this set has the least number of points. It is empty: if \(a\in(b,p)\cap T_0\), then \((a,p)\subseteq(b,p)\) and \(a\notin(a,p)\) by Lemma 3.2 of the first lesson, so \((a,p)\cap T_0\) would be smaller.

Let \(a\in T_0\). If \(a=b\), then \(b\in R_M(a,p)\), because this set contains \(a\). Otherwise \(a\notin(b,p)\), that is, \(ba.p\) fails. So \(b\in H(a,p)\), and \(R_M(a,p)=R_M(a,b)\) contains \(b\). \(\blacksquare\)

## 3. Cut points of a compact connected space

Let \(M\) be a connected Hausdorff space, with the pretree structure of the lesson on cut points: \(xay\) means that there is a separation \(U\,a\,V\) with \(x\in U\) and \(y\in V\). Recall that a branch of the space \(M\) with boundary point \(a\) is a set \(U\cup\{a\}\) with \(U\,a\,V\).

**Lemma 3.1.** Let \(a\) be a cut point of \(M\) and \(b\ne a\). Then \(R_M(a,b)\) is the intersection of all branches of \(M\) with boundary point \(a\) that contain \(b\), and there is such a branch. So \(R_M(a,b)\) is coherent; if \(M\) is compact, it is closed and connected.

**Proof.** Since \(a\) is a cut point there is a separation at \(a\), and \(b\) lies on one of its sides; that side with \(a\) is a branch containing \(b\).

Let \(x\in R_M(a,b)\) and let \(U\cup\{a\}\) be a branch with \(U\,a\,V\) and \(b\in U\). If \(x\) were in \(V\), then \(xab\). So \(x\in U\cup\{a\}\). Conversely let \(x\notin R_M(a,b)\). Then \(xab\): there is a separation \(V\,a\,U\) with \(x\in V\) and \(b\in U\), and the branch \(U\cup\{a\}\) contains \(b\) and not \(x\).

The last statements are Proposition 5.2(3) of the lesson on cut points. \(\blacksquare\)

**Theorem 3.2.** Let \(M\) be a compact connected Hausdorff space, \(T\) a set of cut points of \(M\), and \(\varphi\colon M\to\Phi(T)\) the map of Section 1.

1. For every \(p\in\Phi(T)\setminus\bar T\), the set \(R_M(p)\) is not empty, closed and connected.
2. Every point of \(\Phi(T)\) lies in \(\varphi(M)\) or is adjacent to a point of \(\bar T\).

**Proof.** (1) If \(T\) is empty, \(R_M(p)=M\). Otherwise the sets \(R_M(a,p)\), \(a\in T\), are closed by Lemma 3.1, and every finite number of them have a common point by Lemma 2.4. Since \(M\) is compact, their intersection is not empty. It is coherent by Lemma 3.1 and Proposition 5.2(2) of the lesson on cut points, hence closed and connected.

(2) A point of \(\bar T\) is \(\varphi(a)\) for some \(a\in T\). Let \(p\notin\bar T\) and choose \(x\in R_M(p)\). By Proposition 2.3, \(p=\varphi(x)\) or \(p\) is adjacent to a point of \(\bar T\). \(\blacksquare\)

## 4. An example

Let \(M=[0,1]\) and let \(T\) be the open interval \((0,1)\), the set of all cut points of \(M\). The pretree \(T\) is that of the ordered set \((0,1)\), which is isomorphic to the real line as an ordered set. So, as in Example 6.1 of [Stars and the three kinds of flows](stars-and-the-three-kinds-of-flows.md), the flows of \(T\) are: the flows \(\bar t\); for each \(t\in T\) the flow \(t^-\) of the numbers below \(t\), directed upwards, and the flow \(t^+\) of the numbers above \(t\), directed downwards; and the flows of \(T\) itself, directed upwards or downwards.

The map \(\varphi\) sends \(t\in T\) to \(\bar t\). For \(u,v\in T\), \(v\in(u,0]\) means \(v<u\); so \(\varphi(0)\) is the flow of \(T\) directed downwards, and \(\varphi(1)\) the flow of \(T\) directed upwards. The flows \(t^-\) and \(t^+\) are not in the image of \(\varphi\). They are adjacent to \(\bar t\) (Example 4.1 of the lesson on adjacent points), as Theorem 3.2 says. Exercise 5.2 shows that \(R_M(t^-)=\{t\}\).

## 5. Exercises

**5.1.** Let \(M\) be the vertex set of the path with vertices \(u,v,x\) in this order, and \(T=\{u,v\}\). Determine \(\varphi\), and show that Lemma 1.2(3) fails for the pair \(x,x\) and the point \(v\).

**5.2.** In the example of Section 4, let \(p=t^-\). Determine \(H(a,p)\) and \(R_M(a,p)\) for every \(a\in T\), and show that \(R_M(p)=\{t\}\).

**5.3.** Let \(x,y\in M\setminus T\) be points such that no point of \(T\) lies between them. Show that \(\varphi(x)=\varphi(y)\).

**5.4.** Let \(M\) be the union of a circle \(C\) and a segment \(S\) in the plane that meet in one point \(c\), an endpoint of \(S\); let \(e\) be the other endpoint of \(S\), and \(T\) the set of all cut points of \(M\). Determine \(T\), and show that \(\varphi\) maps every point of \(C\) to \(\bar c\).

## 6. Solutions

**5.1.** The flows of \(T\), a set of two points with the empty relation, are \(\bar u\), which consists of the pair \((v,u)\), the flow \(\bar v\), which consists of \((u,v)\), and the empty relation. We have \(\varphi(u)=\bar u\) and \(\varphi(v)=\bar v\). For \(x\): \(v\in(u,x]\) holds and \(u\in(v,x]\) fails, so \(\varphi(x)=\bar v\). Now \(\bar v\) lies in \([\varphi(x),\varphi(x)]_\Phi=\{\bar v\}\), but \(v\notin[x,x]=\{x\}\). The interval \([x,x]\) contains no point of \(T\).

**5.2.** By the formula of Example 6.1 of the lesson on stars, \(uv.p\) holds if and only if \(u<v<t\) or \(t\le v<u\). So \(ba.p\) holds if and only if \(b<a<t\) or \(t\le a<b\). For \(a<t\): \(H(a,p)\) is the set of \(b>a\), and \(R_M(a,p)\), the set of points that \(a\) does not separate from such a \(b\), is \([a,1]\). For \(a\ge t\): \(H(a,p)\) is the set of \(b<a\), and \(R_M(a,p)=[0,a]\). The intersection of the sets \([a,1]\) with \(a<t\) and \([0,a]\) with \(a\ge t\) is \(\{t\}\).

**5.3.** Let \(u,v\in T\) with \(v\in(u,x]\). Since \(x\notin T\), this means \(uvx\). By (T3) with the point \(y\ne v\): \(uvy\) or \(xvy\). The second fails by assumption. So \(v\in(u,y]\). By symmetry the two flows agree.

**5.4.** A point \(z\) of \(S\) other than \(e\) is a cut point: removing it leaves the part of \(S\) beyond \(z\), which is open in \(M\) and connected, and the rest, which is open and not empty. The point \(e\) is not a cut point, and a point \(z\ne c\) of \(C\) is not a cut point: \(C\setminus\{z\}\) is connected and contains \(c\), and \(S\) is connected and contains \(c\). So \(T=S\setminus\{e\}\). Let \(x\in C\), \(x\ne c\). The only separation at \(c\) has the sides \(C\setminus\{c\}\) and \(S\setminus\{c\}\), so \(ucx\) for every \(u\in T\setminus\{c\}\); that is, \(uc.\varphi(x)\) for all these \(u\). By Lemma 2.2 of the lesson on flows, \(\varphi(x)=\bar c\). And \(\varphi(c)=\bar c\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 5. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
