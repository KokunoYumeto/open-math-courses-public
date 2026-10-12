# Quotients of pretrees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a tree one can contract a subtree to a single vertex, and the result is a tree. The same can be done in a pretree. A subset is *full* if it contains the interval between any two of its points, and an equivalence relation is *full* if all its classes are full. This lesson shows that the set of classes of a full relation is a pretree in a natural way, and how the quotient inherits properties.

- Betweenness of classes is defined through points, and the quotient \(T/{\sim}\) is a pretree (Theorem 2.2).
- The quotient map sends the interval between two points onto the interval between their classes (Proposition 3.1). So images and preimages of full sets are full, and a quotient of a quotient is a quotient (Proposition 3.3).
- If \(T\) is a median pretree, so is \(T/{\sim}\) (Theorem 4.1). If \(T\) is complete, so is \(T/{\sim}\) (Theorem 4.2).

A quotient of a dense pretree need not be dense (Example 5.1); the quotients that are dense are the subject of the next lesson.

The lesson follows Lemmas 4.1 and 4.2 of [Bowditch]. It uses [Betweenness and pretrees](betweenness-and-pretrees.md), [Dense, complete and median pretrees](dense-complete-and-median-pretrees.md) and, for completeness, the criterion of [Directed arcs and suprema](directed-arcs-and-suprema.md).

## 1. Full sets that do not meet

Let \(T\) be a pretree. Recall that \(X\subseteq T\) is full if \([x,x']\subseteq X\) for all \(x,x'\in X\). A set with one point is full.

**Lemma 1.1.** Let \(X,Y\subseteq T\) be full and disjoint, \(x,x'\in X\), \(y,y'\in Y\), and \(z\in T\setminus(X\cup Y)\). Then \(xzy\) holds if and only if \(x'zy'\) holds.

**Proof.** Let \(xzy\). The relation \(yzy'\) fails, because \(Y\) is full and \(z\notin Y\). By (T3), applied to \(xzy\) and the point \(y'\ne z\): \(xzy'\) or \(yzy'\). So \(xzy'\). In the same way, \(xzx'\) fails, and (T3) applied to \(y'zx\) and the point \(x'\ne z\) gives \(y'zx'\). The converse is the same statement with the roles exchanged. \(\blacksquare\)

For disjoint nonempty full sets \(X,Y\) and a point \(z\) we write
\[
X\,z\,Y
\]
if \(z\notin X\cup Y\) and \(xzy\) for some \(x\in X\), \(y\in Y\). By Lemma 1.1 this then holds for all \(x\in X\) and \(y\in Y\).

## 2. Full relations and the quotient

**Definition 2.1.** A *full relation* on a pretree \(T\) is an equivalence relation \(\sim\) on \(T\) all of whose classes are full subsets. The set of classes is written \(T/{\sim}\), and \(\pi\colon T\to T/{\sim}\) is the map that sends a point to its class. For classes \(X,Y,Z\) we write \(XYZ\) if \(X\ne Z\) and there is a point \(y\in Y\) with \(X\,y\,Z\).

If \(XYZ\), then \(Y\) differs from \(X\) and from \(Z\), because the point \(y\) lies in \(Y\) and not in \(X\cup Z\). It is not required that every point of \(Y\) lies between \(X\) and \(Z\) (Example 5.3).

Equality is a full relation, with \(T/{\sim}=T\). The relation with one class is full. On the real line, the full relations are the partitions of the line into convex sets.

**Theorem 2.2.** Let \(\sim\) be a full relation on a pretree \(T\). With the relation of Definition 2.1, \(T/{\sim}\) is a pretree.

**Proof.** (T0) holds because \(XYZ\) requires \(X\ne Z\), and (T1) because the definition is symmetric.

(T2): suppose \(XYZ\) and \(XZY\). There are \(y\in Y\) with \(X\,y\,Z\) and \(z\in Z\) with \(X\,z\,Y\). Choose \(x\in X\). By Lemma 1.1, \(xyz\) and \(xzy\), against (T2) in \(T\).

(T3): let \(XZY\) and \(W\ne Z\); we show \(XZW\) or \(YZW\). Choose \(z\in Z\) with \(X\,z\,Y\), and points \(x\in X\), \(y\in Y\), \(w\in W\). Then \(xzy\) and \(w\ne z\), so \(xzw\) or \(yzw\). Suppose \(xzw\). Then \(W\ne X\): otherwise \(z\in[x,w]\subseteq X\). The point \(z\) lies in neither \(X\) nor \(W\). So \(X\,z\,W\), and \(XZW\). In the same way \(yzw\) gives \(YZW\). \(\blacksquare\)

## 3. Intervals in the quotient

Throughout this section \(\sim\) is a full relation on \(T\). Intervals of \(T/{\sim}\) are written like those of \(T\).

**Proposition 3.1.** For all \(x,y\in T\),
\[
\pi([x,y])=[\pi(x),\pi(y)] .
\]

**Proof.** Let \(X=\pi(x)\) and \(Y=\pi(y)\). If \(X=Y\), then \([x,y]\subseteq X\) because \(X\) is full, and both sides are \(\{X\}\). Let \(X\ne Y\).

Let \(w\in[x,y]\) and \(W=\pi(w)\). If \(W\) is \(X\) or \(Y\), it lies in \([X,Y]\). Otherwise \(w\notin X\cup Y\); then \(w\ne x,y\), so \(xwy\), and \(X\,w\,Y\). Hence \(XWY\).

Conversely, \(X\) and \(Y\) are the images of \(x\) and \(y\). If \(XWY\), there is \(w\in W\) with \(X\,w\,Y\); by Lemma 1.1, \(xwy\). So \(W=\pi(w)\) with \(w\in[x,y]\). \(\blacksquare\)

**Corollary 3.2.**

1. If \(F\subseteq T\) is full, then \(\pi(F)\) is full.
2. If \(\mathcal G\subseteq T/{\sim}\) is full, then \(\pi^{-1}(\mathcal G)\) is full.
3. If \(F\subseteq T\) is linear, then \(\pi(F)\) is linear. So the image of an arc is an arc.
4. Two different classes \(X,Y\) are adjacent in \(T/{\sim}\) if and only if \(X\cup Y\) is full in \(T\).

**Proof.** (1) For \(x,y\in F\): \([\pi(x),\pi(y)]=\pi([x,y])\subseteq\pi(F)\).

(2) Let \(\pi(x),\pi(y)\in\mathcal G\) and \(w\in[x,y]\). Then \(\pi(w)\in[\pi(x),\pi(y)]\subseteq\mathcal G\).

(3) Let \(X,Y,Z\) be three different classes in \(\pi(F)\), with points \(x,y,z\in F\) in them. One of the three points lies between the other two, say \(xyz\). Then \(Y\in[X,Z]\) by Proposition 3.1, and \(Y\ne X,Z\); so \(XYZ\).

(4) Let \(x\in X\), \(y\in Y\). By Proposition 3.1, \([X,Y]=\{X,Y\}\) holds if and only if \([x,y]\subseteq X\cup Y\). If \(X\cup Y\) is full, this holds. If it holds for all \(x\in X\) and \(y\in Y\), then \(X\cup Y\) is full, because \(X\) and \(Y\) are full. \(\blacksquare\)

**Proposition 3.3** (a quotient of a quotient). Let \(\approx\) be a full relation on the pretree \(T/{\sim}\), and define a relation \(\sim'\) on \(T\) by
\[
x\sim'y\quad\Longleftrightarrow\quad\pi(x)\approx\pi(y).
\]
Then \(\sim'\) is a full relation on \(T\). Its classes are the preimages under \(\pi\) of the classes of \(\approx\), and the resulting bijection
\[
T/{\sim'}\ \longrightarrow\ (T/{\sim})/{\approx}
\]
preserves and reflects betweenness.

**Proof.** The classes of \(\sim'\) are the sets \(\pi^{-1}(\mathcal X)\) for the classes \(\mathcal X\) of \(\approx\); they are full by Corollary 3.2(2). The bijection sends \(\pi^{-1}(\mathcal X)\) to \(\mathcal X\).

Let \(\mathcal X,\mathcal Y,\mathcal Z\) be classes of \(\approx\) with \(\mathcal X\ne\mathcal Z\), and \(X',Y',Z'\) their preimages in \(T\).

Suppose \(X'Y'Z'\) in \(T/{\sim'}\): there are \(x\in X'\), \(z\in Z'\) and \(y\in Y'\) outside \(X'\cup Z'\) with \(xyz\). Then \(\pi(y)\in[\pi(x),\pi(z)]\) by Proposition 3.1. The three classes \(\pi(x)\in\mathcal X\), \(\pi(y)\in\mathcal Y\), \(\pi(z)\in\mathcal Z\) are distinct, so \(\pi(x)\,\pi(y)\,\pi(z)\) holds in \(T/{\sim}\), and \(\pi(y)\notin\mathcal X\cup\mathcal Z\). This is \(\mathcal X\mathcal Y\mathcal Z\).

Suppose \(\mathcal X\mathcal Y\mathcal Z\): there are \(X\in\mathcal X\), \(Z\in\mathcal Z\) and \(Y\in\mathcal Y\) outside \(\mathcal X\cup\mathcal Z\) with \(XYZ\) in \(T/{\sim}\). So there are \(y\in Y\), \(x\in X\), \(z\in Z\) with \(xyz\). Then \(x\in X'\), \(z\in Z'\), \(y\in Y'\), and \(y\notin X'\cup Z'\) because \(\pi(y)=Y\). This is \(X'Y'Z'\). \(\blacksquare\)

## 4. Medians and completeness

**Theorem 4.1.** Let \(\sim\) be a full relation on a median pretree \(T\). Then \(T/{\sim}\) is a median pretree, and for \(x,y,z\in T\)
\[
\begin{gathered}
\operatorname{med}(\pi(x),\pi(y),\pi(z))\\
=\pi(\operatorname{med}(x,y,z)).
\end{gathered}
\]

**Proof.** Let \(w=\operatorname{med}(x,y,z)\). It lies in \([x,y]\), \([y,z]\) and \([z,x]\). By Proposition 3.1, \(\pi(w)\) lies in \([\pi(x),\pi(y)]\), \([\pi(y),\pi(z)]\) and \([\pi(z),\pi(x)]\). So \(\pi(w)\) is a median, and it is the median by Proposition 6.2 of the first lesson. \(\blacksquare\)

**Theorem 4.2.** Let \(\sim\) be a full relation on a complete pretree \(T\). Then \(T/{\sim}\) is complete.

**Proof.** By Theorem 4.3 of the lesson on directed arcs it suffices to show that every directed arc \((\mathcal A,\prec)\) of \(T/{\sim}\) has a supremum. If \(\mathcal A\) has a maximum, that is one. Let \(\mathcal A\) be endless.

*Step 1: a least element.* Choose \(M\in\mathcal A\). The elements \(X\succeq M\) form an endless final segment, and a supremum of a final segment of \(\mathcal A\) is a supremum of \(\mathcal A\), by the definition of a supremum. So we may assume that \(M\) is the least element of \(\mathcal A\). Then for every \(Z\in\mathcal A\), because \(\mathcal A\) is full and directed,
\[
[M,Z]=\{X\in\mathcal A\mid X\preceq Z\}.\tag{1}
\]
Fix a point \(m\in M\).

*Step 2: the sets \(B_Z\).* For \(Z\in\mathcal A\), \(Z\ne M\), and \(z\in Z\) put \(B_Z=[m,z]\setminus Z\).

(a) By Proposition 3.1 and (1), \(\pi([m,z])\) is the set of \(X\in\mathcal A\) with \(X\preceq Z\). So \(\pi(B_Z)\) is the set of \(X\in\mathcal A\) with \(X\prec Z\).

(b) \(B_Z\) does not depend on the choice of \(z\): a point \(x\ne m\) of \(B_Z\) has \(mxz\) and \(x\notin Z\), and by Lemma 1.1, applied to the full sets \(\{m\}\) and \(Z\), then \(mxz'\) for every \(z'\in Z\).

(c) \(B_Z\) is an arc that contains \(m\). It is linear as a subset of \([m,z]\), and \(m\notin Z\). Let \(x,x'\in B_Z\) and \(w\in[x,x']\). Then \(w\in[m,z]\), and \(\pi(w)\in[\pi(x),\pi(x')]\). The classes \(\pi(x)\) and \(\pi(x')\) come before \(Z\) in the directed arc \(\mathcal A\), so every element of the interval between them comes before \(Z\). Hence \(w\notin Z\).

(d) If \(Z\prec Z'\), then \(B_Z\subseteq B_{Z'}\). Choose \(z'\in Z'\). By (a) for \(Z'\) there is a point \(z\in Z\cap[m,z']\). Then \([m,z]\subseteq[m,z']\), and for \(x\in[m,z]\) we have \(\pi(x)\preceq Z\prec Z'\), so \(x\notin Z'\).

*Step 3: an arc of \(T\).* Let \(A\) be the union of the sets \(B_Z\). By (c) and (d) it is the union of a chain of arcs, so it is an arc: any two or three of its points lie in one \(B_Z\). By (a), and because \(\mathcal A\) is endless, \(\pi(A)=\mathcal A\).

The point \(m\) lies between no two points of \(A\): two points of \(A\) lie in some \([m,z]\), and an end of an interval is not between two of its points. So \(A\) has a direction in which \(m\) is the least point, and for \(b\in A\) the points of \(A\) up to \(b\) form the interval \([m,b]\).

*\(A\) is endless.* Suppose \(b\) is the greatest point of \(A\). Then \(A=[m,b]\). Let \(b\in B_Z\), so that \(\pi(b)\prec Z\), and choose \(w\in A\) with \(\pi(w)=Z\). Then \(w\in[m,b]\), so \(Z\in[M,\pi(b)]\) by Proposition 3.1, and \(Z\preceq\pi(b)\) by (1). This is a contradiction.

*Step 4: the candidate.* Since \(T\) is complete, the directed arc \(A\) has a supremum \(q\). Because \(A\) is endless, \([m,q)\) is a final segment of \(A\); it contains the least point, so
\[
A=[m,q).
\]
Let \(Q=\pi(q)\).

*\(Q\notin\mathcal A\).* Suppose \(Q\in\mathcal A\). Choose \(Z\in\mathcal A\) with \(Q\prec Z\), and \(w\in A\) with \(\pi(w)=Z\). Since \(w\in[m,q]\), Proposition 3.1 gives \(Z\in[M,Q]\), and (1) gives \(Z\preceq Q\). This is a contradiction.

*Step 5: \(\mathcal A=[M,Q)\).* By Proposition 3.1, \(\pi([m,q])=[M,Q]\). So \(\mathcal A=\pi(A)\subseteq[M,Q]\), and since \(Q\notin\mathcal A\), \(\mathcal A\subseteq[M,Q)\). Conversely let \(X\in[M,Q)\). Then \(X=\pi(x)\) for some \(x\in[m,q]\), and \(x\ne q\) because \(X\ne Q\). So \(x\in A\) and \(X\in\mathcal A\).

The direction of \([M,Q)\) in which \(M\) is least and the order \(\prec\) are directions on the same linear set with the same least element, so they are equal (Proposition 5.2 of the first lesson). Hence \([M,Q)\) is a final segment of \(\mathcal A\) with the order of \(\mathcal A\), and \(Q\) is a supremum of \(\mathcal A\). \(\blacksquare\)

## 5. Examples

**Example 5.1** (a dense pretree with a quotient that is not dense). On the real line let \(X\) be the set of numbers \(\le0\) and \(Y\) the set of numbers \(>0\). The relation with the two classes \(X,Y\) is full, and \(T/{\sim}\) has two points, which are adjacent. The real line is dense; the quotient is not.

**Example 5.2** (the integers as a quotient of the line). On the real line let \(x\sim y\) if \(x\) and \(y\) have the same integer part. The classes are the sets \(C_k\) of numbers \(x\) with \(k\le x<k+1\). For \(i<j<k\) every point of \(C_j\) lies between a point of \(C_i\) and a point of \(C_k\), and no other relations hold. So \(T/{\sim}\) is the pretree of the integers. Neither the real line nor the pretree of the integers is complete. On the closed interval \([0,n]\), which is complete, the same relation has the quotient \(\{0,1,\dots,n\}\), which is complete, in accordance with Theorem 4.2.

**Example 5.3** (contracting a part of a tree). Let \(T\) be the vertex set of the tree with centre \(u\) joined to three vertices \(a,b,c\). The relation with the classes \(\{a,u\}\), \(\{b\}\), \(\{c\}\) is full. The class \(\{a,u\}\) lies between \(\{b\}\) and \(\{c\}\), through its point \(u\); the point \(a\) of this class does not lie between \(b\) and \(c\). The quotient is a path of three points.

## 6. Exercises

**6.1.** In Example 5.3, check directly that no other relation holds in the quotient, and that the quotient is median with the medians given by Theorem 4.1.

**6.2.** On the real line let \(x\sim y\) if \(x=y\) or both lie in \([0,1]\). Show that \(\sim\) is full and that \(T/{\sim}\) is isomorphic to the real line as a pretree.

**6.3.** Show by examples that \(T/{\sim}\) can be median when \(T\) is not, and complete when \(T\) is not.

**6.4.** Let \(\sim\) be a full relation on \(T\) and \(F\subseteq T\) a full subset. Show that the restriction of \(\sim\) to \(F\) is a full relation on the pretree \(F\), and that the natural bijection from its set of classes onto \(\pi(F)\) preserves and reflects betweenness.

**6.5.** Let \(\sim\) be a full relation on the vertex set \(T\) of a tree \(\sigma\). Show that every class is the vertex set of a connected part of \(\sigma\), that \(T/{\sim}\) is the vertex set of a tree, and that two classes are joined by an edge of this tree exactly when some edge of \(\sigma\) joins a vertex of one to a vertex of the other.

## 7. Solutions

**6.1.** Write \(A=\{a,u\}\), \(B=\{b\}\), \(C=\{c\}\). A relation with \(B\) in the middle needs \(b\) between two other vertices, and \(b\) is an end of the tree; likewise for \(C\). So the only relations are \(BAC\) and \(CAB\). The median of \(A,B,C\) is \(A\), the class of \(u=\operatorname{med}(a,b,c)\); medians of triples with a repeated point are trivial.

**6.2.** The class \([0,1]\) and the one-point classes are convex, so the relation is full. Let \(f(x)=x\) for \(x\le0\), \(f(x)=0\) for \(0\le x\le1\), and \(f(x)=x-1\) for \(x\ge1\). This is a nondecreasing map of the line onto itself whose fibres are the classes, so it induces a bijection \(g\) from \(T/{\sim}\) onto the line. If \(XYZ\), there are points \(x<y<z\) or \(z<y<x\) in the three classes, and \(f(x),f(y),f(z)\) are distinct; so \(g(Y)\) lies strictly between \(g(X)\) and \(g(Z)\). Conversely, if \(g(X)<g(Y)<g(Z)\), then points \(x,y,z\) of the classes satisfy \(x<y<z\) because \(f\) is nondecreasing, and \(y\notin X\cup Z\); so \(XYZ\).

**6.3.** Three points with the empty relation have no median. The relation whose classes are two of the points together and the third alone is full, since two points with nothing between them form a full set; its quotient has two points and is median. The open interval \((0,1)\) of the real line is not complete; the relation with one class is full and its quotient is a single point, which is complete.

**6.4.** The classes of the restriction are the sets \(X\cap F\) with \(X\in\pi(F)\); they are full as intersections of full sets, and \(X\cap F\mapsto X\) is a bijection onto \(\pi(F)\). If \(X\cap F\), \(Y\cap F\), \(Z\cap F\) are related in the quotient of \(F\), the points that show it also show \(XYZ\). Conversely let \(XYZ\) with \(X,Y,Z\in\pi(F)\), and choose \(x\in X\cap F\), \(z\in Z\cap F\). There is \(y\in Y\) with \(X\,y\,Z\), so \(xyz\) by Lemma 1.1, and \(y\in[x,z]\subseteq F\). So \(y\in Y\cap F\) shows the relation in the quotient of \(F\).

**6.5.** A class is full, so with two vertices it contains the path between them; it is the vertex set of a connected part. By Proposition 3.1 the intervals of \(T/{\sim}\) are images of intervals of \(T\), which are finite; so \(T/{\sim}\) is discrete, and it is median by Theorem 4.1. By Theorem 2.1 of [Discrete pretrees and trees](discrete-pretrees-and-trees.md) it is the vertex set of the tree whose edges join the adjacent pairs. By Corollary 3.2(4), classes \(X\ne Y\) are adjacent exactly when \(X\cup Y\) is full. If \(X\cup Y\) is full, the path from a vertex of \(X\) to a vertex of \(Y\) stays in \(X\cup Y\), so one of its edges joins \(X\) to \(Y\). If an edge joins \(x\in X\) to \(y\in Y\), then for \(x'\in X\) and \(y'\in Y\) the interval \([x',y']\) lies in \([x',x]\cup[x,y]\cup[y,y']\subseteq X\cup Y\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 4. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
