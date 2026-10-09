# Thompson's group F and dyadic partitions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Thompson's group \(F\) is the group of piecewise linear homeomorphisms of \([0,1]\) whose breakpoints are dyadic rationals and whose slopes are powers of \(2\). Richard Thompson found it in the 1960s, and in 1979 Ross Geoghegan asked whether it is amenable. Two classical facts made the question hard: Brin and Squier showed that \(F\) has no free subgroup of rank two, so the free-subgroup obstruction to amenability is unavailable, and Chou showed that \(F\) is not elementary amenable, so \(F\) cannot be built from finite and abelian groups by the usual closure operations. The survey [Gu, Section 1] describes this history and the many partial results that followed. In September 2026 OpenAI proved that \(F\) is not amenable [OpenAI-F]. This course gives a complete proof.

The proof has three ingredients. This lesson develops the dyadic combinatorics of \(F\): partitions of \([0,1]\) into dyadic intervals, the operation of restricting a partition to one of its intervals and rescaling, and the fact that \(F\) moves any ordered pair of separated dyadic intervals affinely onto any other such pair. The lesson [A Lipschitz map of the Hilbert ball that moves every point](a-lipschitz-map-of-the-hilbert-ball-that-moves-every-point.md) constructs a Lipschitz map of the closed unit ball of a Hilbert space into itself that moves every point by at least \(\tfrac12\). The lesson [Thompson's group F is not amenable](thompsons-group-f-is-not-amenable.md) combines the two with the Følner criterion.

The lesson uses only elementary real analysis.

## 1. The group

A *dyadic rational* is a number \(k2^{-r}\) with \(k\in\mathbb Z\) and \(r\ge0\) an integer. The dyadic rationals form a subring \(\mathbb Z[\tfrac12]\) of \(\mathbb Q\), and it contains \(2^q\) for every \(q\in\mathbb Z\).

**Definition 1.1.** *Thompson's group* \(F\) is the set of homeomorphisms \(g:[0,1]\to[0,1]\) for which there are dyadic rationals \(0=x_0<x_1<\dots<x_m=1\) and integers \(q_1,\dots,q_m\) such that \(g\) is affine with slope \(2^{q_k}\) on \([x_{k-1},x_k]\) for \(k=1,\dots,m\). We call such \(x_k\) *breakpoints* of \(g\); they are not required to be points where the slope changes. The product of \(h,g\in F\) is the composition \(hg=h\circ g\).

An element of \(F\) has positive slopes, so it is increasing, and \(g(0)=0\), \(g(1)=1\).

**Lemma 1.2.** Let \(g\in F\) with breakpoints and slopes as in Definition 1.1. On \([x_{k-1},x_k]\) we have \(g(x)=2^{q_k}x+b_k\) with \(b_k\in\mathbb Z[\tfrac12]\). In particular \(g\) maps dyadic rationals of \([0,1]\) to dyadic rationals.

**Proof.** We show by induction that \(g(x_k)\) is dyadic. We have \(g(x_0)=0\), and \(g(x_k)=g(x_{k-1})+2^{q_k}(x_k-x_{k-1})\) is a sum and product of dyadic rationals. Then \(b_k=g(x_{k-1})-2^{q_k}x_{k-1}\) is dyadic, and for dyadic \(x\in[x_{k-1},x_k]\) so is \(g(x)=2^{q_k}x+b_k\). \(\square\)

**Proposition 1.3.** \(F\) is a group under composition, and it is countable.

**Proof.** The identity lies in \(F\). Let \(g\in F\) be as in Definition 1.1. By Lemma 1.2 the points \(y_k=g(x_k)\) are dyadic, and \(0=y_0<y_1<\dots<y_m=1\). On \([y_{k-1},y_k]\) the inverse is \(g^{-1}(y)=2^{-q_k}(y-b_k)\), affine with slope \(2^{-q_k}\). So \(g^{-1}\in F\), and \(g^{-1}\) maps dyadic rationals to dyadic rationals by Lemma 1.2 applied to \(g^{-1}\).

Let \(h\in F\) have breakpoints \(z_0<\dots<z_l\). The finite set \(P=\{x_0,\dots,x_m\}\cup\{g^{-1}(z_0),\dots,g^{-1}(z_l)\}\) consists of dyadic rationals and contains \(0\) and \(1\). Let \(p<p'\) be consecutive points of \(P\). Then \(g\) is affine on \([p,p']\) with slope a power of \(2\), because no \(x_k\) lies strictly between \(p\) and \(p'\). The interval \(g([p,p'])=[g(p),g(p')]\) contains no \(z_j\) in its interior, because \(z_j=g(g^{-1}(z_j))\) and \(g^{-1}(z_j)\in P\); so \(h\) is affine on it with slope a power of \(2\). Hence \(h\circ g\) is affine on \([p,p']\) with slope a power of \(2\), and \(h\circ g\in F\).

An element of \(F\) is determined by a finite list of breakpoints and slopes, since \(g(0)=0\) and \(g\) is affine between consecutive breakpoints. There are countably many finite lists of dyadic rationals and integers, so \(F\) is countable. \(\square\)

**Example 1.4.** The functions
\[
A(x)=\begin{cases}x/2,&0\le x\le\frac12,\\ x-\frac14,&\frac12\le x\le\frac34,\\ 2x-1,&\frac34\le x\le1,\end{cases}\qquad
B(x)=\begin{cases}x,&0\le x\le\frac12,\\ \frac x2+\frac14,&\frac12\le x\le\frac34,\\ x-\frac18,&\frac34\le x\le\frac78,\\ 2x-1,&\frac78\le x\le1\end{cases}
\]
agree at the common endpoints of their pieces, so they are continuous, increasing and onto \([0,1]\); they belong to \(F\). Exercise 6.1 shows \(AB\neq BA\).

## 2. Dyadic intervals and partitions

**Definition 2.1.** A *dyadic interval* is an interval \([k2^{-r},(k+1)2^{-r}]\) with integers \(r\ge0\) and \(0\le k<2^r\); its *level* is \(r\) and its length \(|I|=2^{-r}\). A *dyadic partition* is a finite set \(T\) of dyadic intervals, called its *cells*, whose union is \([0,1]\) and whose interiors are pairwise disjoint. We write \(|T|\) for the number of cells. For \(n\ge0\), the *uniform partition* \(T^{(n)}\) consists of the \(2^n\) dyadic intervals of level \(n\). A dyadic partition \(T\) *respects* an interval \(I\subseteq[0,1]\) if \(I\) is the union of the cells of \(T\) contained in \(I\).

**Lemma 2.2.** (a) If two dyadic intervals have intersecting interiors, then one of them contains the other.

(b) Let \(I\) be a dyadic interval and \(T\) a dyadic partition whose cells all have length at most \(|I|\). Then \(T\) respects \(I\).

**Proof.** (a) Let \(I\) have level \(r\) and \(J\) level \(s\ge r\). Then \(I\) is the union of the \(2^{s-r}\) dyadic intervals of level \(s\) contained in it, and distinct dyadic intervals of level \(s\) have disjoint interiors. If the interior of \(J\) meets that of \(I\), it meets the interior of one of these level-\(s\) intervals, which is then \(J\). So \(J\subseteq I\).

(b) Let \(C\) be the union of the cells of \(T\) contained in \(I\); it is a closed subset of \(I\). Let \(x\) be an interior point of \(I\) that is not an endpoint of any cell; all but finitely many interior points of \(I\) are of this kind. The point \(x\) lies in the interior of some cell \(K\). By (a), \(K\) and \(I\) are nested. If \(I\subseteq K\), then \(|K|\le|I|\) forces \(K=I\). In either case \(K\subseteq I\), so \(x\in C\). The points of this kind are dense in \(I\), and \(C\) is closed, so \(C=I\). \(\square\)

For a dyadic interval \(I\) with left endpoint \(a\) let \(s_I:[0,1]\to I\), \(s_I(x)=a+|I|x\), be its increasing affine chart. For dyadic intervals \(I,J\) put \(I\cdot J=s_I(J)\).

**Definition 2.3.** If a dyadic partition \(T\) respects a dyadic interval \(I\), the *normalized restriction* of \(T\) to \(I\) is
\[
T_I=\{s_I^{-1}(K):K\in T,\ K\subseteq I\}.
\]

**Lemma 2.4.** Let \(I,J\) be dyadic intervals and \(T\) a dyadic partition.

(a) \(I\cdot J\) is a dyadic interval of level \(\operatorname{level}(I)+\operatorname{level}(J)\), it is contained in \(I\), and \(s_{I\cdot J}=s_I\circ s_J\).

(b) If \(T\) respects \(I\), then \(T_I\) is a dyadic partition whose cells correspond to the cells of \(T\) contained in \(I\). If moreover \(I\neq[0,1]\), then \(|T_I|<|T|\).

(c) If \(T\) respects \(I\) and \(I\cdot J\), then \(T_I\) respects \(J\), and
\[
(T_I)_J=T_{I\cdot J}.\tag{2.1}
\]

**Proof.** Write \(I=[k2^{-r},(k+1)2^{-r}]\) and \(J=[l2^{-s},(l+1)2^{-s}]\), so \(s_I(x)=(k+x)2^{-r}\).

(a) We have \(s_I(J)=[(k2^s+l)2^{-r-s},(k2^s+l+1)2^{-r-s}]\) with \(0\le k2^s+l<2^{r+s}\), a dyadic interval of level \(r+s\), contained in \(s_I([0,1])=I\). The map \(s_I\circ s_J\) is increasing and affine and carries \([0,1]\) onto \(I\cdot J\); an increasing affine map is determined by the image of \([0,1]\), so \(s_I\circ s_J=s_{I\cdot J}\).

(b) Let \(K\subseteq I\) be a cell of \(T\), of level \(t\) and left endpoint \(m2^{-t}\). Since \(K\subseteq I\), we have \(t\ge r\) and \(k2^{t-r}\le m<(k+1)2^{t-r}\). Then
\[
s_I^{-1}(K)=\bigl[(m-k2^{t-r})2^{-(t-r)},\ (m-k2^{t-r}+1)2^{-(t-r)}\bigr]
\]
is a dyadic interval of level \(t-r\). The cells of \(T\) contained in \(I\) have union \(I\) and disjoint interiors, and \(s_I^{-1}\) is a homeomorphism of \(I\) onto \([0,1]\); so their images have union \([0,1]\) and disjoint interiors. If \(I\neq[0,1]\), some cell of \(T\) is not contained in \(I\), since the cells cover \([0,1]\); so \(|T_I|<|T|\).

(c) By (a), \(I\cdot J\subseteq I\). A cell \(s_I^{-1}(K)\) of \(T_I\) lies in \(J\) exactly when \(K\subseteq s_I(J)=I\cdot J\). The union of these cells is \(s_I^{-1}\) of the union of the cells of \(T\) contained in \(I\cdot J\), which is \(s_I^{-1}(I\cdot J)=J\); so \(T_I\) respects \(J\). Finally
\[
(T_I)_J=\{s_J^{-1}s_I^{-1}(K):K\in T,\ K\subseteq I\cdot J\}=\{s_{I\cdot J}^{-1}(K):K\in T,\ K\subseteq I\cdot J\}=T_{I\cdot J}
\]
by (a). \(\square\)

## 3. Images of uniform partitions

For \(g\in F\) and a dyadic partition \(T\) write \(gT=\{g(K):K\in T\}\). Its members are closed intervals with union \([0,1]\) and disjoint interiors, but they need not be dyadic intervals.

**Lemma 3.1.** Let \(g\in F\), with breakpoints and slopes as in Definition 1.1, and put \(c=\max_kq_k\). There is \(n_g\) such that for every \(n\ge n_g\) the set \(gT^{(n)}\) is a dyadic partition all of whose cells have length at most \(2^{c-n}\).

Consequently, for every finite set \(K\subseteq F\) and every finite set \(\mathcal J\) of dyadic intervals there is \(n_0\) such that for all \(n\ge n_0\) and all \(g\in K\), the set \(gT^{(n)}\) is a dyadic partition that respects every member of \(\mathcal J\).

**Proof.** Write \(g(x)=2^{q_k}x+b_k\) on \([x_{k-1},x_k]\) as in Lemma 1.2. Choose \(n_g\) such that for \(n\ge n_g\): (i) every \(x_k\) is an integer multiple of \(2^{-n}\); (ii) \(n\ge q_k\) for every \(k\); (iii) every \(b_k\) is an integer multiple of \(2^{q_k-n}\). This is possible because the \(x_k\) and \(b_k\) are dyadic, and each condition, once true for \(n\), stays true for larger \(n\). Fix \(n\ge n_g\) and a cell \(K=[m2^{-n},(m+1)2^{-n}]\) of \(T^{(n)}\). By (i), \(K\subseteq[x_{k-1},x_k]\) for some \(k\), and
\[
g(K)=\bigl[(m+b_k2^{n-q_k})2^{-(n-q_k)},\ (m+b_k2^{n-q_k}+1)2^{-(n-q_k)}\bigr].
\]
By (ii) and (iii), \(n-q_k\ge0\) and \(m+b_k2^{n-q_k}\) is an integer. Since \(g(K)\subseteq[0,1]\), it is a dyadic interval of length \(2^{q_k-n}\le2^{c-n}\). The images of the cells of \(T^{(n)}\) cover \([0,1]\) and have disjoint interiors because \(g\) is a homeomorphism.

For the second statement, for each \(g\in K\) choose \(n\ge n_g\) so large that \(2^{c-n}\le\min_{J\in\mathcal J}|J|\), where \(c\) is the constant of \(g\). Every larger \(n\) has the same two properties, and Lemma 2.2(b) shows that \(gT^{(n)}\) respects every \(J\in\mathcal J\). Let \(n_0\) be the largest of these finitely many thresholds. \(\square\)

## 4. Moving pairs of intervals

For intervals \(I,J\subseteq[0,1]\) write \(I<J\) if \(\max I<\min J\); thus \(I<J\) requires a gap of positive length between them. A dyadic interval \(I\) is *internal* if \(0<\min I\) and \(\max I<1\). For an increasing homeomorphism \(h\) of \([0,1]\) and dyadic intervals \(I,I'\), the condition \(h\circ s_I=s_{I'}\) says that \(h\) maps \(I\) onto \(I'\) and is affine on \(I\): indeed, if \(h\) is affine on \(I\) with \(h(I)=I'\), then \(h\circ s_I\) is an increasing affine map of \([0,1]\) onto \(I'\), hence equal to \(s_{I'}\).

**Lemma 4.1.** Let \(I<J\) and \(I'<J'\) be internal dyadic intervals. There is \(h\in F\) with \(h\circ s_I=s_{I'}\) and \(h\circ s_J=s_{J'}\).

**Proof.** The intervals \(I<J\) leave three gaps \([0,\min I]\), \([\max I,\min J]\), \([\max J,1]\), each of positive length with dyadic endpoints; likewise \(I'<J'\) leave three gaps. Choose \(N\) such that all twelve gap endpoints are integer multiples of \(2^{-N}\). Each gap \([\alpha,\beta]\) is then the union of the dyadic intervals of level \(N\) that it contains. In each of the three positions, compare the number of these intervals in the gap of \(I<J\) with the number in the corresponding gap of \(I'<J'\). While the numbers differ, replace one interval on the side with fewer intervals by its two halves, which are dyadic intervals of the next level; each replacement increases that number by one. At the end the two sides have equally many intervals in each gap.

We obtain dyadic partitions \(P\) and \(P'\) with the same number of cells, in which \(I\) and \(I'\) occupy the same position in the left-to-right order, and so do \(J\) and \(J'\). Define \(h\) on the \(i\)-th cell \(C\) of \(P\) as the increasing affine map onto the \(i\)-th cell \(C'\) of \(P'\). Consecutive cells share endpoints in both partitions, so these maps agree at common endpoints, and \(h\) is an increasing homeomorphism of \([0,1]\). Its breakpoints are cell endpoints, which are dyadic, and its slope on \(C\) is \(|C'|/|C|\), a power of \(2\). So \(h\in F\), and \(h\) maps \(I\) affinely onto \(I'\) and \(J\) affinely onto \(J'\). \(\square\)

**Lemma 4.2** (covariance). Let \(g,h\in F\), let \(n\ge0\), and let \(I,I'\) be dyadic intervals with \(h\circ s_I=s_{I'}\). If \(gT^{(n)}\) is a dyadic partition that respects \(I\) and \((hg)T^{(n)}\) is a dyadic partition that respects \(I'\), then
\[
\bigl((hg)T^{(n)}\bigr)_{I'}=\bigl(gT^{(n)}\bigr)_I.\tag{4.1}
\]

**Proof.** The cells of \((hg)T^{(n)}\) are the sets \(h(C)\) with \(C\in gT^{(n)}\). Since \(h(I)=I'\) and \(h\) is a bijection, \(h(C)\subseteq I'\) exactly when \(C\subseteq I\). For such \(C\), the identity \(s_{I'}^{-1}\circ h=s_I^{-1}\) on \(I\) gives \(s_{I'}^{-1}(h(C))=s_I^{-1}(C)\). \(\square\)

The condition that \(I,J,I',J'\) be internal in Lemma 4.1 cannot be dropped: every element of \(F\) fixes \(0\) and \(1\) (Exercise 6.4).

## 5. Restricting uniform partitions

The uniform partitions behave simply under normalized restriction. If \(I\) is a dyadic interval of level \(r\le n\), then \(T^{(n)}\) respects \(I\), and
\[
(T^{(n)})_I=T^{(n-r)},\tag{5.1}
\]
because the cells of \(T^{(n)}\) inside \(I\) are the \(2^{n-r}\) dyadic intervals of level \(n\) in \(I\), and \(s_I^{-1}\) maps them to the \(2^{n-r}\) dyadic intervals of level \(n-r\), by the proof of Lemma 2.4(b). If \(r>n\), then \(T^{(n)}\) does not respect \(I\), because \(I\) is shorter than every cell.

## 6. Exercises

**Exercise 6.1** (easy). Compute \(AB(\tfrac78)\) and \(BA(\tfrac78)\) for the elements of Example 1.4, and conclude that \(F\) is not abelian.

**Exercise 6.2** (medium). Find all \(n\ge0\) for which \(AT^{(n)}\) is a dyadic partition.

**Exercise 6.3** (easy). Show that the element \(h\) of Lemma 4.1 is not unique: find two distinct elements of \(F\) that map \([\tfrac14,\tfrac12]\) affinely onto itself.

**Exercise 6.4** (easy). Show that no element of \(F\) maps \([0,\tfrac12]\) onto \([\tfrac14,\tfrac12]\).

**Exercise 6.5** (medium). Let \(I\) be a dyadic interval and \(T\) a dyadic partition that respects \(I\). Show that \(T\) respects \(I\cdot J\) for every cell \(J\) of \(T_I\), and that \(\{I\cdot J:J\in T_I\}\) is the set of cells of \(T\) contained in \(I\).

## 7. Solutions

**6.1.** \(A(\tfrac78)=2\cdot\tfrac78-1=\tfrac34\) and \(B(\tfrac34)=\tfrac34-\tfrac18=\tfrac58\), so \(BA(\tfrac78)=\tfrac58\). Also \(B(\tfrac78)=\tfrac34\) and \(A(\tfrac34)=\tfrac12\), so \(AB(\tfrac78)=\tfrac12\). Since \(\tfrac58\neq\tfrac12\), \(AB\neq BA\).

**6.2.** For \(n=0\), \(AT^{(0)}=\{[0,1]\}\) is a dyadic partition. For \(n=1\), \(A([\tfrac12,1])=[\tfrac14,1]\) is not a dyadic interval. For \(n\ge2\), conditions (i)–(iii) in the proof of Lemma 3.1 hold: the breakpoints \(\tfrac12,\tfrac34\) are multiples of \(2^{-n}\); the slopes are \(2^{-1},2^0,2^1\) and \(n\ge1\); and \(b_1=0\), \(b_2=-\tfrac14\in2^{-n}\mathbb Z\), \(b_3=-1\in2^{1-n}\mathbb Z\). So \(AT^{(n)}\) is a dyadic partition exactly for \(n=0\) and \(n\ge2\). For example \(AT^{(2)}=\{[0,\tfrac18],[\tfrac18,\tfrac14],[\tfrac14,\tfrac12],[\tfrac12,1]\}\).

**6.3.** The identity and \(B\) both do: \(B\) is the identity on \([0,\tfrac12]\).

**6.4.** Every \(g\in F\) satisfies \(g(0)=0\), so \(g([0,\tfrac12])\) contains \(0\), while \([\tfrac14,\tfrac12]\) does not.

**6.5.** Let \(J=s_I^{-1}(K)\) with \(K\in T\), \(K\subseteq I\). Then \(I\cdot J=s_I(J)=K\) is a cell of \(T\), and a partition respects each of its own cells: the cells contained in \(K\) are \(K\) itself, since any other cell meets \(K\) at most in an endpoint. As \(J\) runs over \(T_I\), the cell \(K=I\cdot J\) runs over the cells of \(T\) contained in \(I\), by Definition 2.3.

## References

- [Gu] V. Guba, *Amenability problem for Thompson's group F: state of the art*, arXiv:2305.07113. https://arxiv.org/abs/2305.07113. Section 1 (history, the results of Brin–Squier and Chou, Geoghegan's question).
- [OpenAI-F] OpenAI, *Thompson's group F is nonamenable*, OpenAI Math Release preprint, 23 September 2026, Section 2.1. https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026
