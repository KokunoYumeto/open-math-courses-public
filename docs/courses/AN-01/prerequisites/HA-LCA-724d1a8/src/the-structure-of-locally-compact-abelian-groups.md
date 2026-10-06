# The structure of locally compact abelian groups

**Lesson HA-LCA-12.** Self-checked by the writing AI.

Every locally compact Hausdorff abelian group has an open subgroup of the form \(\mathbb R^a\times K\), where \(K\) is compact. We will also split off the real factor from the whole group, and prove the full classification
\[
 G\cong\mathbb R^a\times\mathbb Z^b\times K
 \quad\text{when }G\text{ is compactly generated}.             \tag{1}
\]
The compact group need not be metrizable, and the ambient group need not be countable or \(\sigma\)-compact.

All groups below are Hausdorff. Write \(\mathbb T=\mathbb R/\mathbb Z\) and \(E(t)=e^{2\pi it}\); characters take values in the complex unit circle. A compactly generated group is generated **algebraically** by a compact set. A monothetic group is the **closure** of a cyclic subgroup. These are different conditions.

We use the proved [Pontryagin theorem](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-2-1), [closed-subgroup duality](subgroups-quotients-and-annihilators.md#ha-lca-10-theorem-2-1), [character separation](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-corollary-4-2), and [closed Euclidean subgroup classification](subgroups-quotients-and-annihilators.md#ha-lca-10-proposition-6-1). In particular, a discrete subgroup of \(\mathbb R^n\) is generated freely by a finite linearly independent family of real vectors. The classical duals and their product topologies are proved in [HA-LCA-02, §§3–4](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1).

The free source for the structure arguments is Dikran Dikranjan, [*Introduction to Topological Groups*](https://users.dimi.uniud.it/~dikran.dikranjan/ITG.pdf), version 26 February 2018: Theorem 2.1.10, Corollary 2.1.13, §7.4, Lemmas 8.0.6–7 and 9.2.7, Propositions 11.2.4 and 11.3.1–2, and Theorem 12.5.5 with Exercise 12.5.7. We give every needed argument, including the algebra, lifting and splitting steps. The examples use complete earlier programme proofs, with exact locators below.

Written and checked by GPT-6 Astra (OpenAI), Ultra, October 2026. The new exposition in this lesson is released under CC0. The separately linked earlier readings and their retained source packages keep their own licences.

## 1. Algebra, compact open subgroups and small quotients

<a id="ha-lca-12-lemma-1-0"></a>
**Lemma 1.0 — Finitely generated abelian groups.** Every finitely generated abelian group is isomorphic to \(\mathbb Z^r\times F\), with \(r\) finite and \(F\) a finite abelian group.

**Proof.** A chosen list of \(m\) generators gives a surjection \(\mathbb Z^m\to A\); let \(L\) be its kernel. The set \(\mathbb Z^m\) is closed and discrete in \(\mathbb R^m\): small coordinate boxes isolate its points, and a point outside it has a coordinate separated from the integers. Every subset of \(\mathbb Z^m\) is therefore closed in \(\mathbb R^m\). The earlier Euclidean subgroup theorem gives a finite free basis of \(L\). Its basis vectors are integer columns, so \(L\) is the image of a finite integer matrix.

We describe its diagonal reduction. Swapping rows or columns, changing a row's sign, and adding an integer multiple of one row or column to another are invertible integer operations. Row operations change the basis of the ambient \(\mathbb Z^m\); column operations change the generating list for \(L\). They preserve the isomorphism type of \(\mathbb Z^m/L\).

If the matrix is nonzero, place a positive entry \(d\) in its upper left corner. Divide each entry in its first column by \(d\), subtract the corresponding multiple of the first row, and, if a nonzero remainder occurs, swap that row to the top. The positive pivot has strictly decreased. The same procedure with columns handles its first row. Each nonzero remainder strictly decreases a positive integer, so after finitely many such decreases the pivot divides every entry in its row and column. Clear those entries by subtraction.

If some entry of the remaining block is not divisible by \(d\), add its row to the first row. The first-column pivot stays \(d\), while the chosen off-diagonal entry is now in the first row. Division followed by a column swap again gives a strictly smaller positive pivot. Repeat. There can be only finitely many such decreases, so eventually the first row and column are cleared and \(d\) divides the remaining block. Continue on that smaller block. Induction on its dimensions terminates the process with positive diagonal entries \(d_1,\ldots,d_s\), all other entries zero. Consequently
\[
 \mathbb Z^m/L\cong
 \mathbb Z^{m-s}\times\prod_{j=1}^s\mathbb Z/d_j\mathbb Z.       \tag{2}
\]
Zero columns and entries \(d_j=1\) cause no difficulty. This proves the assertion; uniqueness of invariant factors is not needed. Integer division and the permitted integer arithmetic were established in [HA-LCA-01, Lemma 4.2](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-lemma-4-2). \(\square\)

<a id="ha-lca-12-lemma-1-1"></a>
**Lemma 1.1 — Compact open neighbourhoods.** In a compact Hausdorff space, the connected component of a point is the intersection of its clopen neighbourhoods. A totally disconnected locally compact Hausdorff space has a base of compact open neighbourhoods.

**Proof.** The first assertion, including the compactness argument that makes the intersection connected, is proved in [HA-LCA-09, Exercise 6.5](the-pontryagin-duality-theorem.md#ha-lca-09-exercise-6-5). We apply that precise compact-space assertion, without a countability restriction.

Let \(x\in O\), with \(O\) open in a totally disconnected locally compact space \(X\). By [finite-Radon Lemma 1.3](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3), choose a compact neighbourhood \(C\) of \(x\) contained in \(O\). Its connected subsets are also connected in \(X\), so its components are singletons. For each \(y\in C\setminus\operatorname{int}_X C\), the first assertion supplies a clopen subset of \(C\) containing \(x\) and excluding \(y\). Their complements cover the compact set \(C\setminus\operatorname{int}_X C\). Choose finitely many, and intersect the corresponding clopen neighbourhoods to obtain \(D\). If that compact set is empty, take \(D=C\).

Then \(D\) is compact, contains \(x\), and lies in \(\operatorname{int}_X C\). It is relatively open in \(C\). Intersecting a representing open subset of \(X\) with \(\operatorname{int}_X C\) shows that \(D\) is open in \(X\). Thus \(x\in D\subseteq O\), as required. \(\square\)

<a id="ha-lca-12-proposition-1-2"></a>
**Proposition 1.2 — Compact open stabilizers.** If \(E\) is a compact open subset of an LCA group and \(0\in E\), it contains a compact open subgroup. In a totally disconnected LCA group, compact open subgroups form a neighbourhood base at zero.

**Proof.** The function \(1_E\) lies in \(C_c(G)\). Uniform continuity of its translates, proved in [Haar Lemma 1.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-lemma-1-1), supplies a neighbourhood \(W\) of zero such that
\[
 \sup_x|1_E(x-w)-1_E(x)|<1\qquad(w\in W).
\]
The differences take only the values \(0,1,-1\), so they vanish. Hence \(W\) lies in the stabilizer
\[
 S=\{s\in G:E+s=E\}.
\]
This is a subgroup. A subgroup containing a neighbourhood is open, since it is a union of translates of that neighbourhood. Every open subgroup is closed, since its complement is a union of its other open cosets. Also \(S\subseteq E\), because \(0\in E\). Thus \(S\) is compact and open. In fact \(E\) is a finite union of its cosets, by compactness.

In the totally disconnected case, first choose \(E\) inside the prescribed neighbourhood by Lemma 1.1, and then choose \(S\subseteq E\). \(\square\)

<a id="ha-lca-12-lemma-1-3"></a>
**Lemma 1.3 — Quotients by compact subgroups.** Let \(K\) be a compact subgroup of an LCA group \(G\), and let \(q:G\to G/K\). The inverse image of a compact set is compact, and \(q\) is closed. In particular, if \(G/K\) is compact, then \(G\) is compact.

**Proof.** For compact \(C\subseteq G/K\), the [compact lifting lemma](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-1-1) provides a compact \(L\subseteq G\) with \(q(L)=C\). Then
\[
 q^{-1}(C)=L+K,
\]
which is compact as a continuous image of the compact product \(L\times K\).

If \(F\subseteq G\) is closed and \(y\notin q(F)\), choose a compact neighbourhood \(C\) of \(y\) in \(G/K\). The set \(F\cap q^{-1}(C)\) is compact, so its image is compact and closed in the Hausdorff quotient. The open neighbourhood
\[
 \operatorname{int}C\setminus q(F\cap q^{-1}(C))
\]
of \(y\) misses \(q(F)\). Therefore \(q(F)\) is closed. Apply the first assertion to the whole compact quotient for the last claim. The compact-product and compact-closed facts used here are [finite-Radon Lemmas 1.1 and 1.6](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-1). \(\square\)

<a id="ha-lca-12-lemma-1-4"></a>
**Lemma 1.4 — Small compact kernels.** If \(Q\) is compact abelian and \(U\) is a neighbourhood of zero, there is a closed subgroup \(C\subseteq U\) such that
\[
 Q/C\cong\mathbb T^r\times F
 \quad\text{for finite }r\text{ and finite abelian }F.          \tag{3}
\]

**Proof.** Replace \(U\) by an open neighbourhood inside it. Characters separate points, so for each \(x\in Q\setminus U\) there is a character \(\chi\) with \(\chi(x)\ne1\). These open non-kernel sets cover \(Q\setminus U\). A finite subcover gives characters \(\chi_1,\ldots,\chi_m\) with common kernel \(C\subseteq U\). When \(Q\setminus U\) is empty, the empty family, with \(C=Q\), is allowed.

The diagonal character map identifies \(Q/C\) with a closed subgroup \(S\) of \(\mathbb T^m\): its image is compact, and a continuous bijection from compact to Hausdorff is a homeomorphism, since it maps closed sets to compact closed sets. Closed-subgroup duality makes the restriction \(\mathbb Z^m=\widehat{\mathbb T^m}\to\widehat S\) surjective. Thus \(\widehat S\) is finitely generated. Lemma 1.0 gives \(\widehat S\cong\mathbb Z^r\times F_0\). All these dual groups are discrete, so that algebraic isomorphism is topological. Taking duals and using Pontryagin duality gives \(S\cong\mathbb T^r\times\widehat F_0\). The finite character theorem of [HA-LCA-01, Theorem 1.1](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-1-1) shows that \(\widehat F_0\) is finite. \(\square\)

## 2. Dense cyclic subgroups

<a id="ha-lca-12-theorem-2-1"></a>
**Theorem 2.1 — Monothetic dichotomy.** A monothetic LCA group is either compact or topologically isomorphic to the discrete group \(\mathbb Z\).

**Proof.** Suppose \(\{na:n\in\mathbb Z\}\) is dense. If \(a\) has finite order, this finite subgroup is closed and equals \(G\). Otherwise identify it algebraically with \(\mathbb Z\), with the topology induced by \(G\).

If this subgroup is discrete, it is locally compact and hence closed in \(G\), by [HA-LCA-09, Lemma 1.2](the-pontryagin-duality-theorem.md#ha-lca-09-lemma-1-2). Density then gives \(G=\mathbb Z\). Assume it is not discrete. Every nonempty relatively open subset \(O\) of \(\mathbb Z\) is unbounded above. Indeed, if \(O\) were bounded above, it would have a largest element \(m\). Then \(O-m\) is an open neighbourhood of zero contained in the nonpositive integers; its negative is contained in the nonnegative integers. Their intersection is the open singleton \(\{0\}\), a contradiction.

Choose a compact neighbourhood \(U\) of zero and a symmetric open neighbourhood \(W\) with \(W+W\subseteq U\). Finitely many translates \(g_i+W\) cover \(U\). Each intersects the dense cyclic subgroup in a nonempty relatively open set, so choose a positive integer \(n_i\) with \(n_i a\in g_i+W\). It follows that
\[
 U\subseteq\bigcup_i(n_i a+U).                                \tag{4}
\]
Put \(A=\{n:na\in U\}\) and \(N=\max_i n_i\). The set \(A\) is unbounded above because it contains the nonempty relatively open set corresponding to \(\operatorname{int}U\). For any integer \(t\), let \(s\) be the least member of \(A\) with \(s\ge t\). By (4), \(s=n_i+u\) for some \(u\in A\). Since \(u<s\), minimality gives \(u<t\le s\). Consequently \(1\le t-u\le n_i\le N\). Thus
\[
 \mathbb Z=A+\{1,\ldots,N\}.
\]
The whole dense cyclic subgroup lies in the compact set \(\bigcup_{j=1}^N(ja+U)\). This set is closed in \(G\), so it contains \(G\). Therefore \(G\) is compact. \(\square\)

## 3. A discrete lattice with compact quotient

<a id="ha-lca-12-lemma-3-1"></a>
**Lemma 3.1 — Lattice lemma.** If an LCA group \(G\) is generated by a compact neighbourhood \(V\) of zero, there is a closed discrete subgroup \(\Lambda\cong\mathbb Z^s\) such that
\[
 G/\Lambda\ \text{is compact},\qquad V\cap\Lambda=\{0\}.       \tag{5}
\]
The case \(s=0\), with \(\Lambda=\{0\}\), is allowed.

**Proof.** First suppose \(G\) is topologically generated by finitely many elements \(a_1,\ldots,a_m\); we temporarily omit the condition on \(V\). Induct on \(m\), starting with the trivial group. If each cyclic closure is compact, their finite sum is a compact subgroup containing the dense group generated by the \(a_j\). It equals \(G\), and \(\Lambda=0\) works. Otherwise, after reordering, the closure of \(\mathbb Za_m\) is noncompact. Theorem 2.1 says it is the closed discrete cyclic subgroup \(Z=\mathbb Za_m\).

The quotient \(G/Z\) is topologically generated by the images of \(a_1,\ldots,a_{m-1}\). Induction gives a closed discrete free subgroup \(\Lambda_1\) with compact quotient. Its inverse image \(\Lambda\) in \(G\) is closed. The restricted quotient \(\Lambda\to\Lambda_1\) is open: for an open set \(O\subseteq G\),
\[
 q(O\cap\Lambda)=q(O)\cap\Lambda_1.
\]
Since \(\Lambda_1\) is discrete, its kernel \(Z\) is open in \(\Lambda\); since \(Z\) itself is discrete, \(\Lambda\) is discrete. Lift a free basis of \(\Lambda_1\) to elements of \(\Lambda\). These lifts, together with \(a_m\), freely generate \(\Lambda\): projecting a relation first kills all lift coefficients, and the infinite order of \(a_m\) kills the last coefficient. Conversely, subtracting the lifted image of any element leaves an element of \(Z\). Thus \(\Lambda\) is free of finite rank. The natural identification \(G/\Lambda\cong(G/Z)/\Lambda_1\) is topological, because both quotient maps are open.

Now let \(G\) be generated by \(V\). Enlarge \(V\) to a compact symmetric neighbourhood \(K\) containing zero and generating \(G\). Choose a symmetric open \(W\) with \(W+W\subseteq K\). Compactness gives a finite \(F\subseteq K\) with \(K\subseteq F+W\). Hence
\[
 K+K\subseteq F+F+W+W\subseteq K+\langle F\rangle.
\]
Induction gives \(nK\subseteq K+\langle F\rangle\) for every \(n\ge1\), so \(G=K+\langle F\rangle\). Put \(D=\overline{\langle F\rangle}\). This is a closed LCA subgroup, topologically finitely generated, and \(G/D=q(K)\) is compact. The first part gives a closed discrete free \(\Lambda\subseteq D\) with \(D/\Lambda\) compact. In \(G/\Lambda\), the compact subgroup \(D/\Lambda\) has compact quotient \(G/D\). Lemma 1.3 therefore makes \(G/\Lambda\) compact.

The compact set \(V\) meets the closed discrete group \(\Lambda\) in finitely many points: the intersection is compact and discrete, and its singleton cover has a finite subcover. Write their coordinates in a free basis of \(\Lambda\). Choose a positive integer \(k\) larger than the absolute value of every nonzero coordinate that occurs. Then \(k\Lambda\cap V=\{0\}\). The subgroup \(k\Lambda\) is closed and discrete, still free of the same rank, and \(\Lambda/k\Lambda\) is finite. Its compact quotient extension
\[
 (G/k\Lambda)/(\Lambda/k\Lambda)\cong G/\Lambda
\]
is compact by Lemma 1.3. Replace \(\Lambda\) by \(k\Lambda\). \(\square\)

## 4. Splitting the real direction

<a id="ha-lca-12-lemma-4-1"></a>
**Lemma 4.1 — Divisible extension and open splitting.** An abelian group \(D\) is called divisible if, for every positive integer \(n\), every element is \(n\) times another element.

1. Any homomorphism from a subgroup \(A\subseteq B\) into a divisible group \(D\) extends to \(B\).
2. If a divisible subgroup \(D\) of a Hausdorff abelian topological group \(B\) is open, then \(B\cong D\times C\) topologically for a discrete subgroup \(C\).

**Proof.** For the first assertion, order all extensions by inclusion of their domains. A chain has its union as an extension, so the maximality principle gives a maximal extension \(u:H\to D\). If \(x\notin H\), the set \(\{n\in\mathbb Z:nx\in H\}\) is \(m\mathbb Z\) for some \(m\ge0\). To see the latter elementary assertion, take its least positive element when there is one and use division with remainder; otherwise the subgroup is zero.

When \(m=0\), choose \(y=0\). When \(m>0\), use divisibility to choose \(y\) with \(my=u(mx)\). Define
\[
 u'(h+kx)=u(h)+ky.                                           \tag{6}
\]
If two such expressions represent the same element, their coefficient difference is a multiple of \(m\), or is zero in the \(m=0\) case. The equality \(my=u(mx)\) then makes the right sides equal. Formula (6) is a homomorphism extending \(u\) to the larger subgroup \(H+\mathbb Zx\), a contradiction. Thus \(H=B\).

For the second assertion, extend the identity of \(D\) to a retraction \(r:B\to D\). It is continuous at zero, because its restriction to the open subgroup \(D\) is the identity, and hence continuous everywhere by translation. Put \(C=\ker r\). It is closed; \(C\cap D=\{0\}\) and \(D\) is open, so \(C\) is discrete. The maps
\[
 D\times C\longrightarrow B,\quad(d,c)\longmapsto d+c,
 \qquad
 B\longrightarrow D\times C,\quad b\longmapsto(r(b),b-r(b))
                                                                  \tag{7}
\]
are continuous inverse homomorphisms, with the subspace topology on \(C\). \(\square\)

<a id="ha-lca-12-lemma-4-2"></a>
**Lemma 4.2 — Extending a local Euclidean homomorphism.** Suppose \(\phi:B_R(0)\subseteq\mathbb R^n\to E\) is continuous, \(\phi(0)=0\), and
\[
 \phi(x+y)=\phi(x)+\phi(y)
 \quad\text{whenever }x,y,x+y\in B_R(0).                      \tag{8}
\]
It extends uniquely to a continuous homomorphism \(F:\mathbb R^n\to E\). If \(\phi\) is a homeomorphism onto an open identity neighbourhood, then \(F(\mathbb R^n)\) is an open connected subgroup isomorphic to
\(\mathbb R^{n-b}\times\mathbb T^b\) for some \(0\le b\le n\).
In particular a connected abelian group with such a local chart is of this form.

**Proof.** For \(x\in\mathbb R^n\), choose a positive integer \(m\) with \(x/m\in B_R(0)\), and set
\[
 F(x)=m\phi(x/m).                                             \tag{9}
\]
If another integer \(l\) is admissible, all partial sums \(j x/(ml)\), \(1\le j\le l\), lie on the segment from zero to \(x/m\) and hence in the ball. Repeated use of (8) gives \(\phi(x/m)=l\phi(x/(ml))\). Interchanging \(m,l\) proves independence in (9). Choosing one sufficiently large \(m\) for \(x,y,x+y\) proves additivity. For \(x\) in the original ball the same partial-sum argument gives \(F(x)=\phi(x)\). Therefore \(F\) is continuous at zero and hence everywhere. Any extension must satisfy (9), which proves uniqueness.

If \(\phi\) is a local homeomorphism as stated, \(N=F(\mathbb R^n)\) contains an open neighbourhood of zero and is an open subgroup. Moreover \(F\) is open: in an open subset of \(\mathbb R^n\), each point has a small translate of a ball on which \(F\) is a translate of the local homeomorphism. Its kernel \(L\) is closed, and the injectivity of \(\phi\) makes \(L\) discrete. The earlier Euclidean subgroup theorem gives a basis \(v_1,\ldots,v_b\) for \(L\), linearly independent over \(\mathbb R\). Extend these vectors to a real basis. The associated invertible linear map takes \(\mathbb Z^b\times0\) onto \(L\), so the open quotient maps give
\[
 N\cong\mathbb R^n/L\cong\mathbb T^b\times\mathbb R^{n-b}.     \tag{10}
\]
The vector-space basis extension and continuity of these linear maps were proved in [HA-LCA-10, Lemma 6.0](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-6-0). The space \(\mathbb R^n\) is connected: a segment joins any two points, and intervals are connected by the intermediate-value property proved in [Banach Lemma 1.1](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-1-1). Continuous images of connected sets are connected, since a separation would pull back to a separation. Thus \(N\) is connected. If \(E\) is connected, its open subgroup \(N\) is also closed, and must be all of \(E\). The argument includes \(n=0\), with a singleton ball. \(\square\)

<a id="ha-lca-12-theorem-4-3"></a>
**Theorem 4.3 — Principal structure theorem.** Every LCA group has an open subgroup topologically isomorphic to \(\mathbb R^a\times K\), with \(a\) finite and \(K\) compact abelian. More precisely, every compactly generated LCA group is isomorphic to
\[
 \mathbb R^a\times\mathbb Z^b\times K.                         \tag{11}
\]

**Proof.** We first treat a compactly generated \(G\). Adding a compact identity neighbourhood to a compact generating set makes Lemma 3.1 applicable. Choose its lattice \(\Lambda\), so \(Q=G/\Lambda\) is compact. Since \(\Lambda\) is discrete, choose a compact symmetric identity neighbourhood \(U\) with
\[
 (U+U+U)\cap\Lambda=\{0\}.                                   \tag{12}
\]
To make this choice, first take an open set missing the other lattice points, shrink under triple addition, and take a symmetric compact neighbourhood inside the smaller set.

Let \(q:G\to Q\). By Lemma 1.4, there is a closed subgroup \(C\subseteq q(\operatorname{int}U)\) such that \(Q/C\cong\mathbb T^t\times F_0\), with \(F_0\) finite. Put \(J=q^{-1}(C)\) and \(K_0=J\cap U\). This last set is compact. If \(x,y\in K_0\), then \(q(x-y)\in C\subseteq q(U)\), so \(q(x-y)=q(u)\) for some \(u\in U\). Now \(x-y-u\in3U\cap\Lambda\), which is zero by (12). Thus \(x-y=u\in K_0\), proving that \(K_0\) is a subgroup. Every element of \(C\) has a lift in \(K_0\); subtracting such a lift from any element of \(J\) gives
\[
 J=K_0+\Lambda,\qquad K_0\cap\Lambda=\{0\}.                  \tag{13}
\]

Pass to \(E=G/K_0\), with quotient map \(l\), and write \(\Lambda'=l(\Lambda)\). Lemma 1.3 says that \(l\) is closed. Both \(\Lambda\) and \(\Lambda\setminus\{0\}\) are closed in \(G\), so \(\Lambda'\) and \(\Lambda'\setminus\{0\}\) are closed in \(E\). Therefore \(\Lambda'\) is closed and discrete. Equation (13) and the open quotient maps identify
\[
 E/\Lambda'\cong G/J\cong Q/C\cong\mathbb T^t\times F_0.     \tag{14}
\]
Denote the resulting open quotient by \(p:E\to\mathbb T^t\times F_0\).

We check the local lift explicitly. Choose a symmetric open \(W\subseteq E\) with \(3W\cap\Lambda'=\{0\}\). The restriction \(p|_W\) is injective and open onto \(p(W)\), hence a homeomorphism. The map
\[
 e:\mathbb R^t\to\mathbb T^t\times F_0,\qquad
 x\longmapsto(x+\mathbb Z^t,0)
\]
is a homeomorphism on a sufficiently small ball \(B_R(0)\), whose image we choose inside \(p(W)\). Indeed, coordinate intervals of length less than one give local charts for the open quotient \(\mathbb R/\mathbb Z\). Define \(\phi=(p|_W)^{-1}\circ e\) on that ball. Its image is open in \(E\). For \(x,y,x+y\) in the ball,
\(\phi(x)+\phi(y)-\phi(x+y)\) belongs to both \(3W\) and \(\ker p=\Lambda'\), so is zero. Lemma 4.2 produces an open connected subgroup \(N\subseteq E\) with \(N\cong\mathbb R^a\times\mathbb T^c\).

This group is divisible: real coordinates can be divided and circle coordinates have roots. Lemma 4.1 splits \(E=N\times B\) with \(B\) discrete. The image of a compact generating set of \(G\) generates \(B\) and is compact, hence finite by its singleton open cover. Thus \(B\) is finitely generated, and Lemma 1.0 gives \(B\cong\mathbb Z^b\times F_1\), with \(F_1\) finite.

In \(E\cong\mathbb R^a\times\mathbb Z^b\times\mathbb T^c\times F_1\), the subgroup \(\mathbb T^c\times F_1\) is compact. Its inverse image \(K_1\subseteq G\) is compact by Lemma 1.3. The induced open quotient gives
\[
 G/K_1\cong\mathbb R^a\times\mathbb Z^b.                      \tag{15}
\]
We have yet to split this quotient. Closed-subgroup duality identifies
\[
 A=K_1^\perp\subseteq\widehat G,\qquad
 A\cong\widehat{G/K_1}\cong\mathbb R^a\times\mathbb T^b.
\]
The subgroup \(A\) is open because \(K_1\) is compact, by [HA-LCA-10, Corollary 2.2](subgroups-quotients-and-annihilators.md#ha-lca-10-corollary-2-2). It is divisible, so Lemma 4.1 splits \(\widehat G=A\times D\) with \(D\) discrete. Taking duals and applying the product theorem and Pontryagin duality gives
\[
 G\cong\mathbb R^a\times\mathbb Z^b\times\widehat D.
\]
The last factor is compact by [HA-LCA-02, Theorem 2.1](characters-and-the-dual-group.md#ha-lca-02-theorem-2-1). This proves (11).

For arbitrary \(G\), a compact symmetric identity neighbourhood generates an open compactly generated subgroup \(G_1\). Apply (11) to \(G_1\). In the resulting product, \(\mathbb R^a\times\{0\}\times K\) is open because \(\mathbb Z^b\) is discrete. Its image is the required open subgroup of \(G\). \(\square\)

<a id="ha-lca-12-corollary-4-4"></a>
**Corollary 4.4 — A global real factor.** Every LCA group is topologically isomorphic to
\[
 G\cong\mathbb R^a\times H,\qquad
 H\ \text{has a compact open subgroup}.                      \tag{16}
\]
If \(G\) is compactly generated, one may take \(H\cong\mathbb Z^b\times K\) with \(K\) compact. Conversely every group in (11) is compactly generated.

**Proof.** Identify the principal open subgroup \(U\) with \(\mathbb R^a\times K\). Its projection \(U\to\mathbb R^a\) extends algebraically to \(r:G\to\mathbb R^a\) by Lemma 4.1. The extension is continuous at zero because it agrees with a continuous map on the open neighbourhood \(U\), and hence continuous everywhere. Let \(s:\mathbb R^a\to G\) be inclusion of the real factor of \(U\); then \(r\circ s\) is the identity.

Put \(H=\ker r\), a closed subgroup. The continuous inverse maps
\[
 g\longmapsto(r(g),g-s(r(g))),\qquad
 (x,h)\longmapsto s(x)+h
\]
give (16). Also \(H\cap U=K\), so \(K\) is compact and open in \(H\).

Recover the compactly generated assertion directly from this split. Projection makes \(H\) compactly generated, and \(H/K\) is a finitely generated discrete group. Write \(H/K\cong\mathbb Z^b\times F\) by Lemma 1.0. The inverse image \(K'\) of its finite factor is compact by Lemma 1.3 and open because that factor is open in the discrete quotient. Then \(H/K'\cong\mathbb Z^b\). Lift the standard basis to \(h_1,\ldots,h_b\in H\). The homomorphism
\[
 s_0:\mathbb Z^b\to H,\qquad(n_j)\longmapsto\sum_jn_jh_j
\]
is continuous, since its domain is discrete, and is a section of the quotient \(\pi\). The maps \(h\mapsto(h-s_0(\pi h),\pi h)\) and \((k,n)\mapsto k+s_0(n)\) are continuous inverses between \(H\) and \(K'\times\mathbb Z^b\).

Conversely a compact real cube, finitely many integer basis vectors and the whole compact factor form a compact generating set for (11). Every real vector is an integer multiple of a vector in the cube, and every integer vector is generated by the basis. \(\square\)

## 5. Compact groups read through their discrete duals

<a id="ha-lca-12-theorem-5-1"></a>
**Theorem 5.1 — Four compact-group correspondences.** Let \(K\) be compact abelian and let \(\Gamma=\widehat K\), a discrete group.

1. \(K\) is connected if and only if \(\Gamma\) is torsion-free.
2. \(K\) is totally disconnected if and only if \(\Gamma\) is torsion.
3. If \(\Gamma\) has an element of infinite order, there is a nontrivial continuous homomorphism \(\mathbb R\to K\).
4. \(K\) is metrizable if and only if \(\Gamma\) is countable.

In assertion 3, a one-parameter subgroup means such a homomorphism and its image; it need not be a closed subgroup isomorphic to \(\mathbb R\).

**Proof.** Assertion 1, in both directions and for arbitrary compact \(K\), is the complete connectedness proof in [HA-LCA-09, Exercise 6.5](the-pontryagin-duality-theorem.md#ha-lca-09-exercise-6-5). Its inputs are the compact component lemma, a finite clopen quotient construction and finite character separation.

For assertion 2, first suppose every \(\gamma\in\Gamma\) has finite order. Its image lies in a finite group of roots of unity. The image of a connected subset is therefore a singleton. Two points in a connected subset consequently have all their character values equal; character separation makes them equal. Hence \(K\) is totally disconnected.

Conversely, if \(K\) is totally disconnected, fix \(\gamma\in\Gamma\). Proposition 1.2 gives a compact open subgroup \(N\) inside \(\{x:|\gamma(x)-1|<1\}\). The [small-arc subgroup lemma](characters-and-the-dual-group.md#ha-lca-02-lemma-1-2) forces \(\gamma(N)=1\). The quotient \(K/N\) is compact and discrete, hence finite. Thus \(\gamma\), which factors through it, has finite order.

For assertion 3, define \(u:\mathbb Z\gamma_0\to\mathbb R\) by \(u(n\gamma_0)=n\), where \(\gamma_0\) has infinite order. Lemma 4.1 extends it to \(u:\Gamma\to\mathbb R\), continuous because \(\Gamma\) is discrete. Dualizing and using \(\widehat{\mathbb R}\cong\mathbb R\) and \(\widehat\Gamma\cong K\) yields a continuous homomorphism \(v:\mathbb R\to K\). Continuity of dual maps is proved in [HA-LCA-09, Proposition 5.1](the-pontryagin-duality-theorem.md#ha-lca-09-proposition-5-1). Evaluation gives
\[
 \gamma_0(v(t))=E(tu(\gamma_0))=E(t),
\]
so \(v\) is nontrivial.

For assertion 4, if \(\Gamma=\{\gamma_j:j\ge1\}\) is countably infinite, evaluation embeds \(K\) continuously and injectively into \(\mathbb T^{\mathbb N}\). Compactness makes it a homeomorphism onto its image. The product has the metric
\[
 d(z,w)=\sum_{j\ge1}2^{-j}|z_j-w_j|.                          \tag{17}
\]
This is a metric because a zero sum forces equality of every coordinate. It gives the product topology: its small values control any prescribed finite list of coordinate distances, and conversely its tail is bounded by \(2\sum_{j>N}2^{-j}\), while the finitely many initial terms are controlled by a product neighbourhood. Restrict the metric to \(K\). For a finite dual use a finite product, and for the trivial group use its unique metric.

Now suppose \(K\) is compact metrizable, with metric \(\rho\). For each positive integer \(n\), finitely many balls of radius \(1/n\) cover \(K\). Their centres, over all \(n\), form a countable dense set \(\{x_j\}\). The continuous real functions \(f_j(x)=\rho(x,x_j)\) separate points: if \(x\ne y\), take \(x_j\) sufficiently close to \(x\); the triangle inequality gives different distances to \(x\) and \(y\).

The complex algebra generated by \(1,f_1,f_2,\ldots\) is closed under conjugation and separates points. The [proved complex approximation theorem](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-corollary-2-2) makes it uniformly dense in \(C(K)\). Polynomials in finitely many \(f_j\), with coefficients in \(\mathbb Q+i\mathbb Q\), form a countable set. They are dense in that algebra: for a fixed finite sum of monomials, approximate each coefficient and bound the error by the sum of its coefficient error times the finite sup norm of the corresponding monomial. Thus \(C(K)\) is separable.

Distinct characters are at least distance \(1\) apart in its sup norm. Otherwise \(|\gamma(x)\overline{\eta(x)}-1|<1\) for every \(x\), and the small-arc lemma would imply \(\gamma=\eta\). Choose, for each character, the first element of a fixed countable dense subset of \(C(K)\) within distance \(1/3\). Distinct characters receive distinct elements, by the triangle inequality. This injects \(\Gamma\) into a countable set and proves assertion 4. \(\square\)

<a id="ha-lca-12-corollary-5-2"></a>
**Corollary 5.2 — Profinite compact abelian groups.** A compact abelian group is totally disconnected if and only if it is an inverse limit of finite discrete abelian groups. Equivalently its discrete dual is torsion.

**Proof.** If \(K\) is totally disconnected, its open subgroups \(N\) form a base by Proposition 1.2, and each \(K/N\) is finite. Order these subgroups by reverse inclusion, with the natural quotient maps. Their finite intersections are again open subgroups. Evaluation gives a continuous map
\[
 K\longrightarrow\varprojlim_N K/N.                         \tag{18}
\]
It is injective because the intersection of all identity neighbourhoods in a Hausdorff group is \(\{0\}\). A compatible tuple in the inverse limit determines closed cosets in \(K\). Any finite list of these cosets has nonempty intersection: the coset specified at the intersection of their subgroups lies inside each. Compactness gives a common point, proving surjectivity. The map is a homeomorphism because its source is compact and its target Hausdorff.

Conversely an inverse limit of finite discrete groups is a closed subgroup of their compact product. It is closed because each compatibility equation is the inverse image of a finite discrete diagonal, which is closed; the product is compact by [Banach Lemma 4.1](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-4-1). Any connected subset projects to a singleton in each coordinate, so has at most one point. This proves total disconnectedness. The dual equivalence is Theorem 5.1(2). \(\square\)

## 6. Kronecker's theorem

<a id="ha-lca-12-theorem-6-1"></a>
**Theorem 6.1 — Dense cyclic subgroups of a torus.** The element
\(\theta+\mathbb Z^n\in\mathbb T^n\), where \(\theta=(\theta_1,\ldots,\theta_n)\), generates a dense subgroup if and only if
\[
 1,\theta_1,\ldots,\theta_n
 \quad\text{are linearly independent over }\mathbb Q.         \tag{19}
\]
Every finite-dimensional torus has a topological generator.

**Proof.** Characters of \(\mathbb T^n\) are precisely
\(x+\mathbb Z^n\mapsto E(m\cdot x)\), \(m\in\mathbb Z^n\), by the earlier classical duality and product calculation. For
\(L=\overline{\{k\theta+\mathbb Z^n:k\in\mathbb Z\}}\), its annihilator is
\[
 L^\perp=\{m\in\mathbb Z^n:m\cdot\theta\in\mathbb Z\}.        \tag{20}
\]
Indeed, triviality on the generator is equivalent to triviality on all its integer multiples, and continuity gives triviality on their closure. By [double annihilation](subgroups-quotients-and-annihilators.md#ha-lca-10-proposition-1-2), \(L=\mathbb T^n\) if and only if \(L^\perp=\{0\}\).

A nonzero \(m\) in (20), with \(m\cdot\theta=k\), gives the rational relation \(-k+\sum_jm_j\theta_j=0\). Conversely any nontrivial rational relation can be multiplied by a common denominator to give such integers. Its \(m\) cannot be zero, since a nonzero constant cannot equal zero. This proves (19).

Choose each \(\theta_j\) outside the rational span of \(1,\theta_1,\ldots,\theta_{j-1}\). This span is countable: it is the image of the countable set \(\mathbb Q^j\). Countability follows by listing rational numerator-denominator pairs and finite tuples in increasing bounds on their entries. The real line is uncountable, as proved by nested compact intervals avoiding the entries of a proposed list in [HA-LCA-10, Example 6.3](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-3), so each choice is possible. The tuple satisfies (19). The zero-dimensional torus is the trivial group and is generated by its identity. \(\square\)

## 7. Solenoids and groups of finite residues

<a id="ha-lca-12-example-7-1"></a>
**Example 7.1 — The rational solenoid.** The dual
\(\Sigma=\widehat{\mathbb Q_{\mathrm{disc}}}\) is compact, connected and metrizable, but is not locally connected.

**Proof.** Compactness follows from discreteness of \(\mathbb Q\). Torsion-freeness and countability of \(\mathbb Q\) give connectedness and metrizability by Theorem 5.1. The explicit factorial-coordinate description
\[
 \Sigma\cong
 \{(z_n)_{n\ge1}\in\mathbb T^{\mathbb N}:
       z_{n+1}^{\,n+1}=z_n\}
\]
uses multiplicative circle coordinates and is proved in [HA-LCA-09, Example 5.4](the-pontryagin-duality-theorem.md#ha-lca-09-example-5-4).

To examine local connectedness use the fully proved adelic description. Let
\[
 \mathbb A=\mathbb R\times\mathbb A_f,\qquad
 K_f=\prod_p\mathbb Z_p\subseteq\mathbb A_f.
\]
[HA-LCA-11, Lemmas 4.2–4.3](the-poisson-summation-formula.md#ha-lca-11-lemma-4-2) construct these groups, prove that the diagonal rational subgroup is closed and discrete, and prove
\(\widehat{\mathbb A}\cong\mathbb A\) and
\(\mathbb Q^\perp=\mathbb Q\). Closed-subgroup duality consequently gives
\[
 \Sigma\cong\mathbb A/\mathbb Q.                              \tag{21}
\]
For \(0<\varepsilon<1/2\), the open set
\[
 U=(-\varepsilon,\varepsilon)\times K_f
\]
maps homeomorphically onto its image under the open quotient
\(q:\mathbb A\to\mathbb A/\mathbb Q\). Indeed, a rational difference of two points of \(U\) is integral at every prime and thus an integer, by the rational-denominator calculation of HA-LCA-11, Lemma 4.2. Its real absolute value is less than \(2\varepsilon<1\), so it is zero. The restriction is open because \(U\) and the quotient map are open.

The group \(K_f\) is totally disconnected. Each \(\mathbb Z_p\) is an inverse limit of finite residue groups, constructed in [HA-LCA-10, Example 6.4](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-4). A connected subset has a single value in every finite residue coordinate, hence is a singleton. The same coordinate argument applies to their product. This product has no isolated points: the elements with \(2\)-adic coordinate \(2^j\) and all other coordinates zero are nonzero and converge to zero; translate them to get the assertion at every point.

A connected subset of \(U\) has a singleton projection to \(K_f\), so lies in one set \((-\varepsilon,\varepsilon)\times\{k\}\). That set has empty interior because \(k\) is not isolated. Thus \(U\) contains no nonempty connected open subset. If \(\Sigma\) were locally connected at zero, its open neighbourhood \(q(U)\) would contain a connected open neighbourhood of zero, whose inverse image in \(U\) would contradict this conclusion. Here local connectedness means having a base of connected open neighbourhoods. \(\square\)

<a id="ha-lca-12-example-7-2"></a>
**Example 7.2 — \(p\)-adic and profinite integers.** For every prime \(p\),
\[
 \widehat{\mathbb Z_p}\cong
 \mathbb Q_p/\mathbb Z_p
 \cong\mathbb Z[1/p]/\mathbb Z                               \tag{22}
\]
as discrete groups. The profinite integers
\[
 \mathbb Z_{\mathrm{prof}}=
 \varprojlim_{n\mid m}\mathbb Z/n\mathbb Z
\]
satisfy
\[
 \mathbb Z_{\mathrm{prof}}\cong\prod_p\mathbb Z_p,\qquad
 \widehat{\mathbb Z_{\mathrm{prof}}}\cong\mathbb Q/\mathbb Z. \tag{23}
\]
Both integer groups are compact and totally disconnected. The group \(\mathbb Q_p\) has the compact open neighbourhood base \(p^j\mathbb Z_p\), \(j\in\mathbb Z\), and
\[
 \mathbb Q_p=\bigcup_{j\ge0}p^{-j}\mathbb Z_p.                \tag{24}
\]
We write \(\mathbb Z_{\mathrm{prof}}\) to distinguish it from the Pontryagin dual \(\widehat{\mathbb Z}=\mathbb T\).

**Proof.** The construction and self-duality of \(\mathbb Q_p\), with \(\mathbb Z_p^\perp=\mathbb Z_p\), are proved in HA-LCA-10, Example 6.4. Restriction to \(\mathbb Z_p\) and closed-subgroup duality give the first isomorphism in (22). Every coset in \(\mathbb Q_p/\mathbb Z_p\) has a representative in \(\mathbb Z[1/p]\) by the \(p\)-adic fractional-part construction. Its kernel is
\(\mathbb Z[1/p]\cap\mathbb Z_p=\mathbb Z\), also proved there. This gives the second isomorphism. The quotient is discrete because \(\mathbb Z_p\) is open, and each of its elements has \(p\)-power order.

For (23), extract from a compatible family modulo all integers its residues modulo \(p^j\), for each prime \(p\). Conversely, residues at all prime powers determine a unique residue modulo every positive integer. Here is the finite step. For coprime \(a,b\), choose \(u,v\in\mathbb Z\) with \(ua+vb=1\) by Bézout. Given residues \(r\bmod a\), \(s\bmod b\), the integer
\[
 r\,vb+s\,ua
\]
has the prescribed residues. The difference of two choices is divisible by \(a\) and \(b\), hence by \(ab\): writing the difference as \(ak\), Bézout implies \(b\mid k\). This proves existence and uniqueness modulo \(ab\); induction handles finitely many prime powers. Every integer greater than one has a prime divisor: its least divisor greater than one must be prime, or a smaller divisor would exist. Repeated division terminates by strict decrease, giving a prime factorization; uniqueness follows by using the prime-divides-product consequence of Bézout to cancel matching prime factors. Apply the finite residue construction to this prime-power decomposition of each integer. The resulting residues are compatible modulo all \(n\), because uniqueness identifies the reduction of the residue at any multiple of \(n\) with the residue at \(n\). The two constructions are inverse, and each coordinate depends on finitely many residue coordinates, so the maps are continuous.

The arbitrary-product dual theorem [HA-LCA-02, Theorem 4.3](characters-and-the-dual-group.md#ha-lca-02-theorem-4-3), applied to (22), gives
\[
 \widehat{\mathbb Z_{\mathrm{prof}}}
 \cong\bigoplus_p\mathbb Z[1/p]/\mathbb Z.
\]
Map this direct sum to \(\mathbb Q/\mathbb Z\) by adding representatives. It is onto: a rational \(r\) has finitely many nonzero local fractional parts and
\(r-\sum_p\{r\}_p\in\mathbb Z\), by the rational identity in [HA-LCA-11, Lemma 4.3](the-poisson-summation-formula.md#ha-lca-11-lemma-4-3). It is injective: if a finite sum of \(p\)-power-denominator representatives \(r_p\) is an integer, then at a fixed prime \(p\) all the other summands are integral, so \(r_p\) is \(p\)-integral as well. An element of \(\mathbb Z[1/p]\) integral at \(p\) is an integer. Thus every summand is zero modulo \(\mathbb Z\).

Compactness and total disconnectedness follow from the finite inverse-limit construction and Corollary 5.2, or from the torsion duals just computed. Formula (24) and the compact open neighbourhood base were proved in HA-LCA-10, Example 6.4. They also show directly that \(\mathbb Q_p\) is totally disconnected: distinct points are separated by a coset of some \(p^j\mathbb Z_p\), which is clopen, so a connected subset cannot contain both. Yet its dual \(\mathbb Q_p\) is torsion-free, since this field has characteristic zero. Compactness is therefore essential in Theorem 5.1(2). \(\square\)

## 8. Exercises with complete solutions

<a id="ha-lca-12-exercise-8-1"></a>
**Exercise 8.1.** Show that a discrete LCA group is compactly generated if and only if it is finitely generated.

**Solution.** A compact subset of a discrete space is finite: its open cover by singletons has a finite subcover. Thus a compact generating set is finite. Conversely a finite generating set is compact, since any open cover has a finite subcover obtained by choosing one set for each element. Thus it is a compact generating set. Both directions concern algebraic generation. \(\square\)

<a id="ha-lca-12-exercise-8-2"></a>
**Exercise 8.2.** Give the one- and two-dimensional forms of Kronecker's theorem, including a dense generator and a nondense irrational example in \(\mathbb T^2\).

**Solution.** For \(n=1\), the annihilator is
\(\{m\in\mathbb Z:m\theta\in\mathbb Z\}\). If \(\theta\) is irrational it is zero, so the cyclic subgroup is dense by double annihilation. If \(\theta=a/b\) with \(b>0\), its \(b\)-th multiple is zero and the cyclic group is finite, so is closed and cannot be dense in the infinite circle. Thus irrationality is exactly the condition.

For \(n=2\), a character indexed by \((m,n)\) kills the generator exactly when
\[
 r+m\theta_1+n\theta_2=0
 \quad\text{for some }r,m,n\in\mathbb Z.                     \tag{25}
\]
If the only such triple is zero, the annihilator is zero and the subgroup is dense. Any nonzero triple has \((m,n)\ne(0,0)\) and puts the cyclic closure in that character's proper kernel. The kernel is proper because varying a coordinate with nonzero coefficient gives a nonconstant character. This proves both directions explicitly.

The element \((\sqrt2,\sqrt3)+\mathbb Z^2\) is a dense generator. If \(m\sqrt2+n\sqrt3=k\) with integers \(m,n,k\) and \(mn\ne0\), squaring gives
\[
 \sqrt6=\frac{k^2-2m^2-3n^2}{2mn},
\]
a contradiction. For the irrationalities used here, a reduced fraction \(a/b\) with square \(2\) or \(6\) has \(a\) even; substituting \(a=2c\) forces \(b\) even as well. A reduced fraction with square \(3\) has both numerator and denominator divisible by \(3\), using the prime-divides-product consequence of Bézout. These contradictions prove that \(\sqrt2,\sqrt3,\sqrt6\) are irrational. If one of \(m,n\) is zero, the remaining relation forces both coefficients and \(k\) to vanish by the corresponding irrationality.

In contrast, for irrational \(\alpha\), the element \((\alpha,2\alpha)\) has annihilating character \((2,-1)\). Its cyclic closure lies in the proper subtorus \(2x-y=0\) modulo \(\mathbb Z\), so is not dense in \(\mathbb T^2\). Irrational coordinates separately do not suffice. \(\square\)

<a id="ha-lca-12-exercise-8-3"></a>
**Exercise 8.3.** Prove that \(\widehat{\mathbb Z_p}\) is torsion, identify its elements, and check total disconnectedness of \(\mathbb Z_p\) directly.

**Solution.** For a continuous character \(\chi\), continuity and the neighbourhood base give some \(j\ge0\) with
\(\chi(p^j\mathbb Z_p)\subseteq\{|z-1|<1\}\). The small-arc lemma makes this subgroup trivial, so \(\chi\) factors through
\(\mathbb Z_p/p^j\mathbb Z_p\cong\mathbb Z/p^j\mathbb Z\).
The finite cyclic character calculation in [HA-LCA-02, Corollary 3.2](characters-and-the-dual-group.md#ha-lca-02-corollary-3-2) gives
\[
 \chi(x)=E(k\,r_j(x)/p^j),\qquad k\in\mathbb Z/p^j\mathbb Z, \tag{26}
\]
where \(r_j(x)\) is an integer representative of the residue of \(x\). Changing the representative changes the exponent by an integer. Each character has \(p\)-power order, and increasing \(j\) identifies the parameter \(k/p^j\) modulo \(\mathbb Z\). These are exactly the elements of \(\mathbb Z[1/p]/\mathbb Z\), agreeing with (22).

Theorem 5.1 gives total disconnectedness. Directly, the continuous finite residue projections separate points. A connected subset has a singleton image under each projection, so all its points have the same residues and are equal. \(\square\)

<a id="ha-lca-12-exercise-8-4"></a>
**Exercise 8.4.** Prove that a compact abelian group is metrizable if and only if its dual is countable, with an explicit metric in one direction and a countability argument in the other.

**Solution.** If the dual is enumerated as \((\gamma_j)\), character separation makes
\[
 d_K(x,y)=\sum_{j\ge1}2^{-j}|\gamma_j(x)-\gamma_j(y)|          \tag{27}
\]
a metric. For a finite dual use a finite sum; for the trivial dual, \(K\) has one point by character separation. The finite-coordinate and tail estimates in Theorem 5.1 give the topology of the evaluation image in the circle product. Evaluation is a continuous injection from compact to Hausdorff, so this is the original topology of \(K\).

Conversely, finite \(1/n\)-nets in a compact metric \(K\) give a countable dense list \((x_j)\). The real functions \(f_j(x)=\rho(x,x_j)\) separate points by the triangle inequality. The complex algebra they generate with constants is dense in \(C(K)\) by the earlier complex approximation theorem. Its polynomials with rational real and imaginary coefficients are countable and dense. Explicitly, for a fixed finite polynomial \(P=\sum_{\alpha\in F}c_\alpha f^\alpha\), set \(M_\alpha=\|f^\alpha\|_\infty\). Choose rational complex \(q_\alpha\) with
\[
 |c_\alpha-q_\alpha|
 <\frac{\varepsilon}{|F|\max(1,M_\alpha)}.
\]
Then \(\|P-\sum_{\alpha\in F}q_\alpha f^\alpha\|_\infty<\varepsilon\); the zero polynomial is handled separately. Each \(M_\alpha\) is finite by compactness and continuity.

Distinct characters are at least distance \(1\) apart in the sup norm, by the small-arc lemma applied to their quotient. Assign each character the first member of a fixed countable dense sequence in \(C(K)\) within distance \(1/3\). Two characters assigned the same member would be less than \(2/3\) apart. Thus the assignment is injective, proving countability. No countable dual was assumed in this direction. \(\square\)
