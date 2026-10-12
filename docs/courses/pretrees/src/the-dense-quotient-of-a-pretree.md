# The dense quotient of a pretree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A quotient of a pretree by a full relation is a pretree ([Quotients of pretrees](quotients-of-pretrees.md)), and it may or may not be dense. This lesson studies the full relations whose quotient is dense; they are called *codense*. The results:

- Among the codense relations on a pretree \(T\) there is a least one, written \(\approx\) (Proposition 2.3). Its quotient \(T/{\approx}\) is the *dense quotient* of \(T\).
- Two points are identified in the dense quotient exactly when no set of points ordered like the rational numbers lies between them (Theorem 3.3).
- The relation \(\approx\) is reached from equality by repeating one step, in which two points are identified when the interval between their classes is finite. The step is repeated along the ordinal numbers until nothing changes (Theorem 5.2).
- For the completion \(\Phi(T)\) of [The completion of a pretree](the-completion-of-a-pretree.md), two points are identified in the dense quotient exactly when no set of points of \(T\) ordered like the rational numbers lies between them. The dense quotient of \(\Phi(T)\) is a complete dense median pretree (Proposition 6.2, Corollary 6.3).

The lesson follows Lemmas 4.3 to 4.5 of [Bowditch]. It uses the lesson on quotients throughout, [Discrete pretrees and trees](discrete-pretrees-and-trees.md) for finite intervals, and in Section 6 the lesson on the completion. Section 5 uses ordinal numbers; the facts needed are named there.

## 1. Comparing full relations

Let \(T\) be a pretree. An equivalence relation on \(T\) is a set \(R\) of pairs of points, and we write \(x\,R\,y\) for \((x,y)\in R\). For equivalence relations \(R\) and \(S\) we write
\[
R\le S
\]
if \(x\,R\,y\) implies \(x\,S\,y\), that is, if \(R\subseteq S\) as sets of pairs. Then every class of \(S\) is a union of classes of \(R\). Equality is the least equivalence relation, and the relation with one class the greatest; both are full. The quotient of \(T\) by a full relation \(R\) is written \(T/R\), as in the lesson on quotients.

**Lemma 1.1.**

1. The intersection of a nonempty set of full relations is a full relation.
2. The union of a nonempty set of full relations that is totally ordered by \(\le\) is a full relation.

**Proof.** (1) An intersection of equivalence relations is an equivalence relation, and the class of a point under the intersection is the intersection of its classes under the given relations. An intersection of full sets is full.

(2) Let \(R\) be the union. It is reflexive and symmetric. Let \(x\,R\,y\) and \(y\,R\,z\), say \(x\,S_1\,y\) and \(y\,S_2\,z\) with \(S_1,S_2\) in the given set. One of the two relations contains the other, say \(S_1\le S_2\). Then \(x\,S_2\,z\), so \(x\,R\,z\). To see that the classes are full, let \(x\,R\,y\) and \(w\in[x,y]\). Then \(x\,S\,y\) for some \(S\) in the set, the class of \(x\) under \(S\) is full, so \(x\,S\,w\), and \(x\,R\,w\). \(\blacksquare\)

## 2. Codense relations

**Definition 2.1.** A full relation \(R\) on \(T\) is *codense* if the pretree \(T/R\) is dense.

**Lemma 2.2.** A full relation \(R\) is codense if and only if for all \(x,y\in T\) that are not \(R\)-related there is a point \(z\) with \(xzy\) that is \(R\)-related neither to \(x\) nor to \(y\).

**Proof.** Let \(X\ne Y\) be classes, \(x\in X\) and \(y\in Y\). By the definition of the betweenness of classes and Lemma 1.1 of the lesson on quotients, a class lies between \(X\) and \(Y\) if and only if there is a point \(z\) outside \(X\cup Y\) with \(xzy\). \(\blacksquare\)

**Proposition 2.3.** The intersection of a nonempty set of codense relations is codense. The relation with one class is codense. So the intersection of all codense relations on \(T\) is the least codense relation.

**Proof.** Let \(R\) be the intersection; it is full by Lemma 1.1. If \(x,y\) are not \(R\)-related, they are not \(S\)-related for some \(S\) in the set. By Lemma 2.2 there is \(z\) with \(xzy\) that is \(S\)-related neither to \(x\) nor to \(y\); then it is \(R\)-related to neither, because \(R\le S\). So \(R\) is codense, by Lemma 2.2. The quotient by the relation with one class has at most one point, and is dense. \(\blacksquare\)

The least codense relation is written \(\approx\), or \(\approx_T\) when the pretree has to be named, and \(x\approx y\) for related points. The pretree \(T/{\approx}\) is the *dense quotient* of \(T\). By Theorems 4.1 and 4.2 of the lesson on quotients, the dense quotient of a median pretree is median, and the dense quotient of a complete pretree is complete. If \(T\) is dense, equality is codense, and \(\approx\) is equality.

## 3. Rational subsets

Recall that a totally ordered set is *dense* if between any two of its elements there is a third, and *without ends* if it has no least and no greatest element.

**Definition 3.1.** A subset \(Q\) of a pretree is *rational* if it is linear, nonempty and countable, and one of its directions is a dense order without ends. Two points \(x,y\) are *separated by a rational subset* if the interval \((x,y)\) contains a rational subset.

A rational subset is infinite, and its two directions are both dense and without ends, since each is the reverse of the other. By Cantor's theorem (Theorem 3.1 of [Separable pretrees and the order of intervals](separable-pretrees-and-the-order-of-intervals.md)) a rational subset with one of its directions is isomorphic to the ordered set of rational numbers; this explains the name, and is not used below.

**Lemma 3.2.** Let \(Q\subseteq(x,y)\) be rational, and let \(<\) be the direction of \([x,y]\) with \(x<y\). Then \(<\) is a dense order without ends on \(Q\), and:

1. for \(z\in Q\), the set of \(q\in Q\) with \(q<z\) is \(Q\cap(x,z)\), the set of \(q\in Q\) with \(q>z\) is \(Q\cap(z,y)\), and both are rational;
2. for \(z<w\) in \(Q\), the set of \(q\in Q\) with \(z<q<w\) is \(Q\cap(z,w)\), and it is rational.

**Proof.** The restriction of \(<\) to \(Q\) is a direction of \(Q\), so it is one of the two directions of \(Q\) (Proposition 5.2 of the first lesson), which are dense and without ends.

For distinct \(u,v\in[x,y]\), \(u<v\) holds if and only if \(u\in[x,v)\) (Corollary 5.3 of the first lesson). So for \(q,z\in Q\): \(q<z\) if and only if \(q\in(x,z)\). The reverse of \(<\) is the direction of \([x,y]\) in which \(y\) is least, so in the same way \(q>z\) if and only if \(q\in(z,y)\). For \(z<w\) the interval \([z,w]\) is the set of \(u\in[x,y]\) with \(z\le u\le w\), because \([x,y]\) is full. This gives the three descriptions.

Each of the three sets is a subset \(S\) of the ordered set \(Q\) of one of the forms "below \(z\)", "above \(z\)", "between \(z\) and \(w\)". It is not empty, because \(Q\) is without ends and dense. Between two elements of \(S\) there is an element of \(Q\), and it lies in \(S\). And \(S\) has no least and no greatest element: for example, an element \(q<z\) is not the greatest element below \(z\), because there is \(q'\in Q\) with \(q<q'<z\), and it is not the least, because \(Q\) has no least element. \(\blacksquare\)

**Theorem 3.3.** Let \(T\) be a pretree and \(x,y\in T\). Then \(x\approx y\) if and only if \(x\) and \(y\) are not separated by a rational subset.

**Proof.** Write \(x\,N\,y\) if \(x\) and \(y\) are not separated by a rational subset. We show that \(N\) is a codense relation and that \(N\le R\) for every codense relation \(R\). Then \(N\) is the least codense relation.

*(a)* Let \(Q\subseteq(x,y)\) be rational and \(z\in Q\). By Lemma 3.2(1), \(x\) and \(z\) are separated by a rational subset, and so are \(z\) and \(y\).

*(b) \(N\) is an equivalence relation.* It is reflexive, because \((x,x)\) is empty, and symmetric. For transitivity we show: if \(x\) and \(y\) are separated by a rational subset \(Q\), and \(z\) is any point, then \(x,z\) or \(z,y\) are separated by a rational subset. This is clear if \(z\) is \(x\) or \(y\). Otherwise choose \(w\in Q\). By Lemma 3.1 of the first lesson, \(w\in[x,z]\) or \(w\in[z,y]\). In the first case \((x,w)\subseteq(x,z)\), by Lemma 3.2 of the first lesson if \(w\ne z\); and \(Q\cap(x,w)\) is a rational subset of \((x,z)\), by Lemma 3.2(1). In the second case \(Q\cap(w,y)\) is a rational subset of \((z,y)\).

*(c) \(N\) is full.* Let \(x\,N\,y\) and \(w\in(x,y)\). Then \((x,w)\subseteq(x,y)\), so a rational subset of \((x,w)\) would separate \(x\) and \(y\). Hence \(x\,N\,w\).

*(d) \(N\) is codense.* If \(x,y\) are not \(N\)-related, choose a rational \(Q\subseteq(x,y)\) and \(z\in Q\). Then \(xzy\), and by (a) the point \(z\) is \(N\)-related neither to \(x\) nor to \(y\). Apply Lemma 2.2.

*(e) \(N\le R\) for every codense \(R\).* Let \(x,y\) be points that are not \(R\)-related; we construct a rational subset of \((x,y)\). Let \(D_n\) be the set of numbers \(k/2^n\) with \(0\le k\le2^n\), and \(D\) the union of the sets \(D_n\). We define a map \(h\colon D\to[x,y]\) on \(D_0,D_1,D_2,\dots\) in turn, so that for every \(n\):

- (i) \(h\) is strictly increasing on \(D_n\), for the direction of \([x,y]\) with \(x<y\);
- (ii) if \(a<b\) are consecutive elements of \(D_n\), then \(h(a)\) and \(h(b)\) are not \(R\)-related.

Put \(h(0)=x\) and \(h(1)=y\). Let \(h\) be defined on \(D_n\) with (i) and (ii). For consecutive \(a<b\) in \(D_n\), Lemma 2.2 gives a point \(c\in(h(a),h(b))\) that is \(R\)-related neither to \(h(a)\) nor to \(h(b)\); let \(h\) take this value at the midpoint of \(a\) and \(b\). Since \([x,y]\) is full, \(c\in[x,y]\), and \(h(a)<c<h(b)\). So (i) and (ii) hold on \(D_{n+1}\).

Let \(Q\) be the set of values of \(h\) at the elements of \(D\) other than \(0\) and \(1\). By (i), \(Q\) lies in \([x,y]\) strictly between \(x\) and \(y\), so \(Q\subseteq(x,y)\). It is linear and countable, and \(h\) is an isomorphism from the ordered set of the numbers \(k/2^n\) strictly between \(0\) and \(1\) onto \(Q\) with the direction of \([x,y]\). That ordered set is dense and without ends. So \(Q\) is rational, and \(x,y\) are not \(N\)-related. \(\blacksquare\)

## 4. The step by finite intervals

For points \(x,y\) of a pretree write \(x\simeq y\) if the interval \([x,y]\) is finite. This is the *finite interval relation*.

**Lemma 4.1.**

1. The finite interval relation is a full relation.
2. It is equality if and only if the pretree is dense.
3. Each of its classes is a discrete pretree, and the pretree is discrete if and only if there is at most one class.

**Proof.** (1) The relation is reflexive and symmetric, and transitive because \([x,z]\subseteq[x,y]\cup[y,z]\). If \(x\simeq y\) and \(w\in[x,y]\), then \([x,w]\subseteq[x,y]\) is finite, so \(x\simeq w\).

(2) If two points \(x\ne y\) are adjacent, then \([x,y]=\{x,y\}\) and \(x\simeq y\). Let the pretree be dense and \(x\ne y\). Choose \(z_1\in(x,y)\) and then \(z_{n+1}\in(x,z_n)\) for \(n\ge1\). By Lemma 3.2 of the first lesson the sets \(I_n=(x,z_n)\) decrease, and \(z_n\notin I_n\) while \(z_{n+1}\in I_n\). So for \(k<m\) we have \(z_m\in I_k\) and \(z_k\notin I_k\): the points \(z_n\) are distinct. They lie in \((x,y)\), so \([x,y]\) is infinite.

(3) A class is full, so the interval between two of its points, formed in the class, is their interval in the pretree, which is finite. The second statement is the definition of a discrete pretree. \(\blacksquare\)

Let \(R\) be a full relation on \(T\), with quotient map \(\pi\colon T\to T/R\). The *derived relation* \(R'\) is defined by
\[
\begin{gathered}
x\,R'\,y\quad\Longleftrightarrow\quad
[\pi(x),\pi(y)]\ \text{is finite},
\end{gathered}
\]
with the interval formed in the pretree \(T/R\). So \(R'\) identifies two points when their classes are related by the finite interval relation of \(T/R\).

**Lemma 4.2.** Let \(R\) be a full relation on \(T\).

1. \(R'\) is a full relation, \(R\le R'\), and \(T/R'\) is isomorphic, by the natural bijection, to the quotient of the pretree \(T/R\) by its finite interval relation.
2. \(x\,R'\,y\) holds if and only if \([x,y]\) meets only finitely many classes of \(R\).
3. If \(S\) is a full relation with \(R\le S\), then \(R'\le S'\).
4. \(R'=R\) if and only if \(R\) is codense.
5. If \(R\) is equality, \(R'\) is the finite interval relation of \(T\).

**Proof.** (1) Proposition 3.3 of the lesson on quotients, applied to the finite interval relation of \(T/R\), which is full by Lemma 4.1. If \(x\,R\,y\), then \(\pi(x)=\pi(y)\).

(2) By Proposition 3.1 of that lesson, \([\pi(x),\pi(y)]\) is the set of classes that meet \([x,y]\).

(3) Every class of \(R\) lies in a class of \(S\). So if \([x,y]\) meets finitely many classes of \(R\), it meets finitely many classes of \(S\).

(4) \(R'=R\) means that two classes of \(R\) with a finite interval between them are equal, that is, that the finite interval relation of \(T/R\) is equality. By Lemma 4.1(2) this holds if and only if \(T/R\) is dense.

(5) Then \(T/R=T\). \(\blacksquare\)

## 5. Repeating the step

This section uses ordinal numbers: transfinite induction, definition by transfinite recursion, and Hartogs' lemma, which says that for every set \(A\) there is an ordinal \(\gamma\) with no injective map from \(\gamma\) into \(A\). These are proved in the set theory part of the core course [Mathematical Logic, Set Theory, and Computability (C80)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C80), in the sections on the basic properties of the ordinals, on the transfinite recursion theorems, and on comparability and Hartogs' lemma.

For every ordinal \(\alpha\) define a relation \(R_\alpha\) on \(T\) by recursion:

- \(R_0\) is equality;
- \(R_{\alpha+1}=(R_\alpha)'\), the derived relation;
- \(R_\lambda\) is the union of the relations \(R_\beta\), \(\beta<\lambda\), if \(\lambda\) is a limit ordinal.

**Lemma 5.1.** Every \(R_\alpha\) is a full relation, and \(R_\beta\le R_\alpha\) for \(\beta\le\alpha\).

**Proof.** By transfinite induction on \(\alpha\). For \(\alpha=0\) the statement is clear. If it holds for \(\alpha\), then \(R_{\alpha+1}\) is full and \(R_\alpha\le R_{\alpha+1}\), by Lemma 4.2(1). If \(\lambda\) is a limit ordinal and the statement holds for all \(\beta<\lambda\), the relations \(R_\beta\), \(\beta<\lambda\), are full and totally ordered by \(\le\); their union is full by Lemma 1.1(2), and it contains each of them. \(\blacksquare\)

So the recursion is well defined: the derived relation is formed only of full relations. By Lemma 4.2(5), \(R_1\) is the finite interval relation of \(T\).

**Theorem 5.2.** Let \(T\) be a pretree and \(\approx\) its least codense relation.

1. \(R_\alpha\le{\approx}\) for every ordinal \(\alpha\).
2. There is an ordinal \(\alpha\) with \(R_{\alpha+1}=R_\alpha\).
3. If \(R_{\alpha+1}=R_\alpha\), then \(R_\alpha\) is the relation \(\approx\), and \(R_\beta=R_\alpha\) for all \(\beta\ge\alpha\).

**Proof.** (1) By transfinite induction. Equality lies in every equivalence relation. If \(R_\alpha\le{\approx}\), then \(R_{\alpha+1}=(R_\alpha)'\le({\approx})'\) by Lemma 4.2(3), and \(({\approx})'\) is \(\approx\) by Lemma 4.2(4). A union of relations contained in \(\approx\) is contained in \(\approx\).

(2) Suppose \(R_{\alpha+1}\ne R_\alpha\) for every \(\alpha\). Then for \(\beta<\alpha\) we have \(R_\beta\le R_{\beta+1}\le R_\alpha\) and \(R_\beta\ne R_{\beta+1}\), so \(R_\beta\ne R_\alpha\). So for every ordinal \(\gamma\), the map \(\alpha\mapsto R_\alpha\) is an injective map from \(\gamma\) into the set of all sets of pairs of points of \(T\). This contradicts Hartogs' lemma.

(3) By Lemma 4.2(4), \(R_\alpha\) is codense, so \({\approx}\le R_\alpha\); with (1), \(R_\alpha\) is \(\approx\). For \(\beta\ge\alpha\), Lemma 5.1 and (1) give \(R_\alpha\le R_\beta\le{\approx}\). \(\blacksquare\)

**Corollary 5.3.** Let \(\mathcal P\) be a set of full relations on \(T\) such that equality lies in \(\mathcal P\); if \(R\in\mathcal P\), then \(R'\in\mathcal P\); and the union of every nonempty subset of \(\mathcal P\) that is totally ordered by \(\le\) lies in \(\mathcal P\). Then \(\approx\) lies in \(\mathcal P\).

**Proof.** By transfinite induction, \(R_\alpha\in\mathcal P\) for every \(\alpha\); at a limit ordinal the relations \(R_\beta\), \(\beta<\lambda\), form a totally ordered subset of \(\mathcal P\). By Theorem 5.2, \(\approx\) is one of the \(R_\alpha\). \(\blacksquare\)

**Example 5.4.** If \(T\) is dense, \(R_1=R_0\) and \(\approx\) is equality. If \(T\) is discrete and not empty, \(R_1\) is the relation with one class, so \(R_2=R_1\), and the dense quotient is a single point. Exercises 7.1 and 7.2 give a pretree with \(R_1\) codense and neither equality nor the relation with one class, and a pretree in which \(R_2\ne R_1\).

## 6. The completion

Let \(\Phi=\Phi(T)\) be the completion of a pretree \(T\): the set of flows of \(T\) with the betweenness \(\langle prq\rangle\) of the lesson on the completion. The set \(\bar T\) of flows towards points is a copy of \(T\) in \(\Phi\): \(\langle\bar x\bar z\bar y\rangle\) holds if and only if \(xzy\) (Lemma 2.2(3) there). Intervals of \(\Phi\) are written \((p,q)_\Phi\). In this section \(\approx\) is the least codense relation of the pretree \(\Phi\).

**Lemma 6.1.** Let \(p\ne q\) be points of \(\Phi\) outside \(\bar T\). Then \((p,q)_\Phi\) contains a point of \(\bar T\).

**Proof.** By Lemma 1.1(1) of the lesson on the completion there is a point \(x\in T\) between \(p\) and \(q\) in the pretree of \(T\) with its flows. The flow \(\bar x\) is different from \(p\) and \(q\), so \(\langle p\,\bar x\,q\rangle\) by the definition of the betweenness of flows. \(\blacksquare\)

**Proposition 6.2.** Let \(p,q\in\Phi(T)\). Then \(p\approx q\) fails if and only if \((p,q)_\Phi\) contains a rational subset of \(\Phi\) that consists of points of \(\bar T\).

**Proof.** If there is such a subset, \(p\approx q\) fails by Theorem 3.3. For the converse we first show:

*Claim.* If \(p\approx q\) fails, there is a point \(z\in\bar T\cap(p,q)_\Phi\) such that \(p\approx z\) and \(z\approx q\) both fail.

By Theorem 3.3 there is a rational subset \(Q'\subseteq(p,q)_\Phi\). Let \(<\) be the direction of \([p,q]_\Phi\) with \(p<q\), and choose \(a<c<d<b\) in \(Q'\). If \(c\) or \(d\) lies in \(\bar T\), let \(z\) be that point; otherwise let \(z\) be a point of \(\bar T\) in \((c,d)_\Phi\), by Lemma 6.1. In each case \(a<z<b\). By Lemma 3.2(1) the set of \(r\in Q'\) with \(r<a\) is rational, and it lies in \((p,z)_\Phi\). So \(p\) and \(z\) are separated by a rational subset, and \(p\approx z\) fails by Theorem 3.3. In the same way the set of \(r\in Q'\) with \(r>b\) shows that \(z\approx q\) fails.

Now repeat the construction of part (e) of the proof of Theorem 3.3 in the pretree \(\Phi\), with \(x=p\), \(y=q\) and the relation \(\approx\), using the Claim in place of Lemma 2.2: for consecutive \(a<b\) in \(D_n\) the relation \(h(a)\approx h(b)\) fails, so there is a point of \(\bar T\) in \((h(a),h(b))_\Phi\) that is related neither to \(h(a)\) nor to \(h(b)\), and \(h\) takes this value at the midpoint. The set \(Q\) of values of \(h\) at the numbers other than \(0\) and \(1\) is a rational subset of \((p,q)_\Phi\), and it consists of points of \(\bar T\). \(\blacksquare\)

**Corollary 6.3.** Let \(T\) be a pretree.

1. The dense quotient \(\Phi(T)/{\approx}\) of the completion is a complete, dense, median pretree.
2. For \(x,y\in T\): \(\bar x\approx\bar y\) in \(\Phi(T)\) if and only if \(x\approx_Ty\), that is, if and only if \(x\) and \(y\) are not separated by a rational subset of \(T\).

**Proof.** (1) \(\Phi(T)\) is complete and median (Corollary 5.3 of the lesson on the completion). Its dense quotient is dense by definition, and complete and median by Theorems 4.1 and 4.2 of the lesson on quotients.

(2) Since \(x\mapsto\bar x\) preserves and reflects betweenness, a subset of \(T\) lies in \((x,y)\) and is rational if and only if the corresponding subset of \(\bar T\) lies in \((\bar x,\bar y)_\Phi\) and is rational in \(\Phi\). So by Proposition 6.2, \(\bar x\approx\bar y\) fails if and only if \(x\) and \(y\) are separated by a rational subset of \(T\). By Theorem 3.3 for \(T\), this means that \(x\approx_Ty\) fails. \(\blacksquare\)

The pretree \(\Phi(T)/{\approx}\) is written \(\Psi(T)\). By (2) the map \(x\mapsto\) class of \(\bar x\) induces an injective map from the dense quotient \(T/{\approx_T}\) into \(\Psi(T)\).

## 7. Exercises

**7.1.** Let \(T\) be the set of pairs \((t,i)\) with \(t\) a real number and \(i\in\{0,1\}\), ordered by \((t,i)<(t',i')\) if \(t<t'\), or \(t=t'\) and \(i<i'\), with the betweenness of this order. Determine \(R_1\), show that \(R_2=R_1\), and describe the dense quotient.

**7.2.** Let \(T\) be the set of pairs \((m,n)\) of integers, ordered by \((m,n)<(m',n')\) if \(m<m'\), or \(m=m'\) and \(n<n'\), with the betweenness of this order. Determine \(R_1\) and \(R_2\), and the dense quotient.

**7.3.** Show that \(x\simeq y\) implies \(x\approx y\), and give a proof that does not use ordinals.

**7.4.** Let \(T\) be the real line, and \(x^-\), \(x^+\) the two flows adjacent to \(\bar x\) in \(\Phi(T)\) ([Adjacent points of the completion](adjacent-points-of-the-completion.md), Example 4.1). Show that \(x^-\approx\bar x\approx x^+\) in \(\Phi(T)\), and that \(\bar x\approx\bar y\) fails for \(x\ne y\).

**7.5.** Let \(R\) be a full relation on \(T\) with \(R\le{\approx}\), and \(\pi\colon T\to T/R\) the quotient map. Show that for \(x,y\in T\): \(x\approx y\) if and only if \(\pi(x)\) and \(\pi(y)\) are related by the least codense relation of \(T/R\).

## 8. Solutions

**7.1.** The order is total, so \(T\) is a pretree, by the argument for the real line in Exercise 7.1 of the first lesson; the same holds in 7.2. For \(t<t'\) the interval between \((t,i)\) and \((t',i')\) contains all \((s,j)\) with \(t<s<t'\), so it is infinite; the interval between \((t,0)\) and \((t,1)\) consists of these two points. So the classes of \(R_1\) are the pairs \(\{(t,0),(t,1)\}\). By Lemma 4.2(2), two points are \(R_2\)-related if the interval between them meets finitely many of these pairs; for \(t<t'\) it meets the pairs of all \(s\) with \(t<s<t'\). So \(R_2=R_1\), and \(\approx\) is \(R_1\) by Theorem 5.2. A class lies between two others exactly when its \(t\) lies between theirs: the dense quotient is the real line.

**7.2.** The interval between \((m,n)\) and \((m',n')\) is finite if \(m=m'\), and for \(m<m'\) it contains all \((m,k)\) with \(k>n\). So the classes of \(R_1\) are the sets \(C_m\) of pairs with first entry \(m\). The interval between two points meets only the classes \(C_k\) with \(k\) between the first entries, finitely many. So \(R_2\) is the relation with one class, and \(R_2\ne R_1\). Then \(R_3=R_2\), and the dense quotient is a single point.

**7.3.** With ordinals: \(R_1\le{\approx}\) by Theorem 5.2(1). Without: let \(x\simeq y\) and suppose \(x\approx y\) fails. By Theorem 3.3 the interval \((x,y)\) contains a rational subset, which is infinite; but \([x,y]\) is finite.

**7.4.** The points \(x^-\) and \(\bar x\) are adjacent, so the interval between them in \(\Phi(T)\) has two points, and \(x^-\simeq\bar x\); likewise \(\bar x\simeq x^+\). By 7.3 the relations \(\approx\) follow. For \(x\ne y\) the rational numbers between \(x\) and \(y\) form a rational subset of the real line in \((x,y)\), so \(\bar x\approx\bar y\) fails by Corollary 6.3(2).

**7.5.** Let \(K\) be the least codense relation of \(T/R\), and \(S\) the relation on \(T\) with \(x\,S\,y\) if and only if \(\pi(x)\,K\,\pi(y)\). By Proposition 3.3 of the lesson on quotients, \(S\) is a full relation and \(T/S\) is isomorphic to the quotient of \(T/R\) by \(K\), which is dense. So \(S\) is codense, and \({\approx}\le S\). Conversely, since \(R\le{\approx}\), the classes of \(\approx\) are unions of classes of \(R\), so \(\approx\) defines an equivalence relation \(K_0\) on \(T/R\): two classes are \(K_0\)-related if their points are \(\approx\)-related. Its classes are the images of the classes of \(\approx\), which are full by Corollary 3.2(1) of that lesson. By Proposition 3.3 there, the quotient of \(T/R\) by \(K_0\) is isomorphic to \(T/{\approx}\), which is dense. So \(K_0\) is codense, \(K\le K_0\), and hence \(S\le{\approx}\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 4. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
- The Open Logic Project, *Set Theory: An Open Introduction* (the set theory part of the Open Logic Text), chapters on ordinals, on stages and ranks, and on choice: https://builds.openlogicproject.org/
