# Separable pretrees and the order of intervals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a complete dense median pretree every interval \([a,b]\) is an ordered set in which between any two points there is a third and every nonempty subset has a least upper bound ([Dense, complete and median pretrees](dense-complete-and-median-pretrees.md), Corollary 4.4). The real interval \([0,1]\) has these two properties and one more: a countable subset, the rational numbers, that meets every open interval. This lesson shows that the third property is what is missing: if the pretree is *separable*, every interval \([a,b]\) with \(a\ne b\) is ordered like \([0,1]\) (Theorem 4.1).

Separability of a pretree is defined by a countable subset that is dense in a weak sense, which only asks that it reach every "side branch" between two points. The first result (Proposition 2.2) turns such a set into a countable set that meets every open interval, by adding medians. The second ingredient is Cantor's theorem on countable dense orders (Theorem 3.1), proved here.

The lesson follows Lemmas 2.12 and 2.13 of [Bowditch]. We use the first two lessons of the course: [Betweenness and pretrees](betweenness-and-pretrees.md) for finite trees, directions and medians, and the lesson named above.

## 1. Gates in a tree

Let \(\tau\) be a tree, \(P=[x,y]_\tau\) the vertex set of a path, and \(b\) a vertex. The *gate* of \(b\) on \(P\) is the branch vertex \(g\) of \(x,y,b\): the unique vertex of \([x,y]_\tau\cap[y,b]_\tau\cap[b,x]_\tau\) (Lemma 6.1 of the first lesson).

**Lemma 1.1.** Let \(g\) be the gate of \(b\) on \(P=[x,y]_\tau\).

1. \([b,g]_\tau\cap P=\{g\}\), and for every \(p\in P\), \([b,p]_\tau=[b,g]_\tau\cup[g,p]_\tau\).
2. If \(z\in P\) and \(g\in[x,z]_\tau\), then \(g\) is also the gate of \(b\) on \([x,z]_\tau\). If \(g\notin[x,z]_\tau\), the gate of \(b\) on \([x,z]_\tau\) is \(z\).
3. Let \(a\) be another vertex, with gate \(g'\ne g\) on \(P\). Then
\[
[a,b]_\tau=[a,g']_\tau\cup[g',g]_\tau\cup[g,b]_\tau .
\]

**Proof.** (1) Since \(g\) lies on \([b,x]_\tau\) and on \([b,y]_\tau\), the path \([b,g]_\tau\) meets \([g,x]_\tau\) and \([g,y]_\tau\) only in \(g\) (Lemma 1.1(2) of the first lesson), and \(P=[x,g]_\tau\cup[g,y]_\tau\). For \(p\in P\), going from \(b\) to \(g\) and then along \(P\) to \(p\) visits no vertex twice, so it is the path from \(b\) to \(p\).

(2) By (1), \(g\in[b,x]_\tau\) and \(g\in[b,z]_\tau\). If also \(g\in[x,z]_\tau\), then \(g\) lies in all three paths of \(x,z,b\). If \(g\notin[x,z]_\tau\), then \(z\in[x,g]_\tau\), so \(z\) lies on \([b,x]_\tau=[b,g]_\tau\cup[g,x]_\tau\); it lies on \([b,z]_\tau\) and \([x,z]_\tau\) as an end. So \(z\) lies in all three paths.

(3) Go from \(a\) to \(g'\), along \(P\) to \(g\), and on to \(b\). We show that no vertex is visited twice. By (1), \([a,g']_\tau\) and \([g,b]_\tau\) meet \(P\) only in \(g'\) and in \(g\). Suppose \(w\) lies in \([a,g']_\tau\) and in \([g,b]_\tau\). The paths from \(w\) to \(g'\) and from \(w\) to \(g\) have a common initial part, from \(w\) to some vertex \(w'\), and after \(w'\) they have no common vertex; so going from \(g'\) to \(w'\) and on to \(g\) is the path from \(g'\) to \(g\), which lies in \(P\). Hence \(w'\in P\). But \(w'\in[a,g']_\tau\) gives \(w'=g'\), and \(w'\in[g,b]_\tau\) gives \(w'=g\); this contradicts \(g'\ne g\). \(\blacksquare\)

## 2. Weakly and strongly dense subsets

Let \(T\) be a median pretree and \(x\ne y\) points of \(T\). Since \(\operatorname{med}(x,y,z)\in[x,y]\), every point \(z\) falls into exactly one of three classes: \(\operatorname{med}(x,y,z)=x\), or \(=y\), or \(\in(x,y)\). Put
\[
\begin{gathered}
P(x,y)=\{z\in T:\\
\operatorname{med}(x,y,z)\in(x,y)\}.
\end{gathered}
\]
It contains \((x,y)\), because a point \(z\in(x,y)\) is its own median with \(x\) and \(y\). In a tree, \(P(x,y)\) consists of the vertices whose gate on the path from \(x\) to \(y\) is not an end of the path.

A subset \(R\subseteq T\) is *strongly dense* if \(R\cap(x,y)\ne\varnothing\) for all \(x\ne y\), and *weakly dense* if \(R\cap P(x,y)\ne\varnothing\) for all \(x\ne y\). A strongly dense set is weakly dense. If \(T\) has a weakly dense subset, then \(T\) is dense: for \(z\in P(x,y)\) the median \(\operatorname{med}(x,y,z)\) lies in \((x,y)\).

**Lemma 2.1.** Let \(T\) be a median pretree, \(x\ne y\), \(a\in P(x,y)\) and \(z=\operatorname{med}(x,y,a)\). Let \(b\in P(x,z)\) and \(c\in P(z,y)\). Then \(z=\operatorname{med}(a,b,c)\).

**Proof.** Let \(m_b=\operatorname{med}(x,z,b)\in(x,z)\) and \(m_c=\operatorname{med}(z,y,c)\in(z,y)\). Take a finite tree \(\tau\) that contains \(x,y,z,a,b,c,m_b,m_c\) with the same betweenness (Corollary 4.5 of the first lesson), and let \(P=[x,y]_\tau\). The points \(m_b,z,m_c\) lie on \(P\) in this order, between \(x\) and \(y\), and they are distinct.

*Gates.* The gate of \(a\) on \(P\) is \(z\), because \(z\) lies on the three paths of \(x,y,a\). Let \(g\) be the gate of \(b\) on \(P\). If \(g\notin[x,z]_\tau\), then by Lemma 1.1(2) the gate of \(b\) on \([x,z]_\tau\) is \(z\); but that gate is \(m_b\), which lies on the three paths of \(x,z,b\), and \(m_b\ne z\). So \(g\in[x,z]_\tau\), and by Lemma 1.1(2), \(g=m_b\). In the same way the gate of \(c\) on \(P\) is \(m_c\).

*The three paths.* The gates \(z,m_b,m_c\) are distinct, so Lemma 1.1(3) gives
\[
[a,b]_\tau=[a,z]_\tau\cup[z,m_b]_\tau\cup[m_b,b]_\tau,
\]
and similarly for \([a,c]_\tau\) and \([b,c]_\tau\). The first two contain \(z\) as a gate, and \([b,c]_\tau\) contains \([m_b,m_c]_\tau\), which contains \(z\). So \(z\) lies in \([a,b]\cap[b,c]\cap[c,a]\). \(\blacksquare\)

**Proposition 2.2.** Let \(T\) be a median pretree and \(R\subseteq T\) weakly dense. Then the set
\[
R'=\{\operatorname{med}(a,b,c):\ a,b,c\in R\}
\]
is strongly dense. If \(R\) is countable, so is \(R'\).

**Proof.** Let \(x\ne y\). Choose \(a\in R\cap P(x,y)\) and put \(z=\operatorname{med}(x,y,a)\in(x,y)\). Choose \(b\in R\cap P(x,z)\) and \(c\in R\cap P(z,y)\). By Lemma 2.1, \(z=\operatorname{med}(a,b,c)\in R'\). \(\blacksquare\)

A median pretree is *separable* if it has a countable weakly dense subset; by Proposition 2.2 this is the same as having a countable strongly dense subset. A separable pretree is dense.

## 3. Countable dense orders

A totally ordered set is *dense* if between any two of its elements there is a third, and *without ends* if it has no least and no greatest element.

**Theorem 3.1** (Cantor). Any two nonempty countable dense totally ordered sets without ends are isomorphic as ordered sets.

**Proof.** Let \(A=\{a_1,a_2,\dots\}\) and \(B=\{b_1,b_2,\dots\}\) be such sets; both are infinite. We construct finite sets \(f_0\subseteq f_1\subseteq\dots\) of pairs \((a,b)\in A\times B\) such that each \(f_n\) is an order isomorphism from a finite subset of \(A\) onto a finite subset of \(B\). Start with \(f_0=\varnothing\).

*Odd steps.* At step \(2k-1\), if \(a_k\) is not yet in the domain, the elements \(u_1<\dots<u_r\) of the domain divide \(A\) into \(r+1\) parts: below \(u_1\), between \(u_i\) and \(u_{i+1}\), above \(u_r\). The element \(a_k\) lies in one of them. The corresponding part of \(B\), cut out by the images of the \(u_i\), is not empty, because \(B\) is dense and without ends. Choose an element \(b\) of it and add the pair \((a_k,b)\). The enlarged set of pairs is again an order isomorphism.

*Even steps.* At step \(2k\), do the same for \(b_k\) and the inverse.

The union \(f\) of all \(f_n\) is defined on every \(a_k\), takes every value \(b_k\), and preserves the order, since any two pairs lie in some \(f_n\). \(\blacksquare\)

## 4. The order of an interval

**Theorem 4.1.** Let \(T\) be a complete separable median pretree and \(a\ne b\) points of \(T\). Let \(<\) be the direction of \([a,b]\) with \(a<b\). Then there is a bijection \(\Phi:[a,b]\to[0,1]\) with \(\Phi(a)=0\), \(\Phi(b)=1\), such that \(s<t\) if and only if \(\Phi(s)<\Phi(t)\).

**Proof.** Let \(R\) be a countable strongly dense subset and \(Q=R\cap(a,b)\).

*\(Q\) is a countable dense order without ends, and it meets every interval.* For \(s<t\) in \([a,b]\), the interval \((s,t)\) of \(T\) is the set of points of \([a,b]\) strictly between \(s\) and \(t\) (Corollary 5.3 of the first lesson), and it contains a point of \(R\), which lies in \(Q\). Applying this to \(s,t\in Q\), to \(s=a\) and to \(t=b\) gives the claim.

*An isomorphism on \(Q\).* By Theorem 3.1 there is an order isomorphism \(\varphi\) from \(Q\) onto the set of rational numbers in \((0,1)\).

*The extension.* Put \(\Phi(a)=0\), \(\Phi(b)=1\), and for \(t\in(a,b)\)
\[
\Phi(t)=\sup\{\varphi(q):\ q\in Q,\ q\le t\}.
\]
The set is not empty, and \(\Phi(t)\in(0,1)\): there are \(q,q'\in Q\) with \(q<t<q'\), so \(\varphi(q)\le\Phi(t)\le\varphi(q')\). For \(t\in Q\), \(\Phi(t)=\varphi(t)\).

*\(\Phi\) is strictly increasing.* Let \(s<t\) in \([a,b]\). Choose \(q,q'\in Q\) with \(s<q<q'<t\). Then \(\Phi(s)\le\varphi(q)<\varphi(q')\le\Phi(t)\); for \(s=a\) or \(t=b\) the outer inequalities hold because \(0<\varphi<1\).

*\(\Phi\) is onto.* Let \(0<r<1\) and \(Y=\{q\in Q:\varphi(q)<r\}\). It is not empty. By Corollary 4.4 of the previous lesson \(Y\) has a least upper bound \(t\) in \([a,b]\). Then \(a<t\), and \(t<b\), because an element \(q'\in Q\) with \(\varphi(q')>r\) is an upper bound of \(Y\). We show \(\Phi(t)=r\).

For every rational \(\rho\) with \(0<\rho<r\), the element \(\varphi^{-1}(\rho)\) lies in \(Y\), so it is at most \(t\), and \(\rho\le\Phi(t)\). Hence \(\Phi(t)\ge r\).

Let \(q\in Q\) with \(q\le t\), and suppose \(\varphi(q)>r\). Choose a rational \(\rho\) with \(r<\rho<\varphi(q)\) and let \(q''=\varphi^{-1}(\rho)\). Then \(q''<q\le t\), and \(q''\) is an upper bound of \(Y\), because \(\varphi<r<\rho\) on \(Y\). This contradicts the choice of \(t\). So \(\varphi(q)\le r\) for all such \(q\), and \(\Phi(t)\le r\). \(\blacksquare\)

**Corollary 4.2.** In a complete separable median pretree, every interval \([a,b]\) with \(a\ne b\) has as many points as the real line, and for \(s<t\) in \([a,b]\) the bijection \(\Phi\) maps \((s,t)\) onto the open interval \((\Phi(s),\Phi(t))\).

**Proof.** \((s,t)\) is the set of points of \([a,b]\) strictly between \(s\) and \(t\), and \(\Phi\) is an order isomorphism onto \([0,1]\). \(\blacksquare\)

## 5. Exercises

**5.1.** Let \(T\) be the vertex set of the tree with a centre \(m\) joined to three vertices \(x,y,z\). Determine \(P(x,y)\), and show that \(\{x,y,z\}\) is not weakly dense while \(T\) has no strongly dense subset.

**5.2.** Let \(T=[0,1]\) with the betweenness of the line. Show that a subset is weakly dense if and only if it is strongly dense, if and only if it is dense in the usual sense.

**5.3.** Let \(R\) be the tripod of Section 3 of the previous lesson, and let \(R_0\) be the set of its points of rational height on legs 1 and 2 only, without the centre. Show that \(R_0\) is not weakly dense in \(R\), that the set \(R_1\) of all points of rational height other than the centre is weakly dense and strongly dense, and that the centre is a median of three points of \(R_1\).

**5.4.** In the proof of Theorem 4.1, where is completeness used, and what goes wrong for \(T=\mathbb Q\cap[0,1]\)?

**5.5.** Show that the hypothesis "without ends" cannot be dropped from Theorem 3.1: give two countable dense totally ordered sets that are not isomorphic.

## 6. Solutions

**5.1.** The median of \(x,y\) and \(z\) or \(m\) is \(m\in(x,y)\), so \(P(x,y)=\{m,z\}\). For the pair \(x,m\): the medians \(\operatorname{med}(x,m,y)\) and \(\operatorname{med}(x,m,z)\) are \(m\), and \(\operatorname{med}(x,m,x)=x\); so \(P(x,m)\) is empty, and no subset is weakly dense. The points \(x\) and \(m\) are adjacent, so no subset is strongly dense either.

**5.2.** For \(x<y\), the median of \(x,y,z\) is the middle one of the three numbers, so \(P(x,y)=(x,y)\).

**5.3.** Let \(x\ne y\) be two points of leg 3 of \(R\). The gate of a point of legs 1 and 2 on the segment between them is the lower of the two points, so \(R_0\cap P(x,y)\) is empty. The set \(R_1\) meets every open interval of \(R\): an interval between two points contains points of rational height other than the centre. So it is strongly dense, hence weakly dense. The centre is the median of the points of height 1 on the three legs.

**5.4.** Completeness enters through Corollary 4.4 of the previous lesson, which gives the least upper bound \(t\) of \(Y\) and so a point with \(\Phi(t)=r\). In \(\mathbb Q\cap[0,1]\), which is dense, median and separable but not complete, \(\Phi\) can be taken to be the identity on the rationals, and it is not onto \([0,1]\): the irrational numbers are missed.

**5.5.** The rational numbers in \((0,1)\) and in \([0,1)\) are countable dense totally ordered sets; the second has a least element and the first has none, and an order isomorphism preserves least elements.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 2. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
- G. Cantor, *Beiträge zur Begründung der transfiniten Mengenlehre* (Erster Artikel), Mathematische Annalen 46 (1895), 481–512: the characterization of the order type of the rational numbers.
