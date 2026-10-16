# Girth and centered moments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Every edge of a block draws its pair \((W,z)\) independently from the distribution of [Masks, lists and one draw per edge](masks-lists-and-one-draw-per-edge.md). This lesson shows that two families of requirements then hold together with positive probability. Every short cyclically nonbacktracking closed walk of \(Y\) has nontrivial holonomy, which is the girth condition of the cover; this uses the word detector of [A word detector in unitriangular matrices](a-word-detector-in-unitriangular-matrices.md) and a bound for the zeros of a polynomial at random points. Every block deviates from its mean by a small fraction of its normalization; this is a moment method in which walks that use some edge only once contribute nothing, and the remaining walks are counted through their cycle rank. A compactness argument chooses one assignment satisfying all requirements, which proves the realization theorem of [The model operator and finite tests](the-model-operator-and-finite-tests.md) [OpenAI-KK, Sections 9.7 to 9.9].

- Zeros of polynomials at random points (Section 1).
- Girth (Section 2).
- Walks without singleton edges (Section 3).
- Centered moments (Section 4).
- A simultaneous choice and the realization theorem (Section 5).

The notation of the preceding lessons is in force. Fix \(\eta>0\) and put \(\varepsilon=\eta/6\). The previous lesson, with this \(\varepsilon\), gives for every adjacent pair \((i,k)\) a finite distribution \(\mathcal D_{ik}\) of pairs \((W,z)\), with \(\|W\|\le C_W\) for a fixed \(C_W\). Every positive edge \(e:a\to b\) of \(Y\), with \(a\in A_i\) and \(b\in B_k\), receives an independent pair \((W_e,z_e)\) with distribution \(\mathcal D_{ik}\); its reverse orientation carries \(W_e^*\) and \(z_e^{-1}\).

## 1. Zeros of polynomials at random points

**Lemma 1.1** (the Schwartz–Zippel bound). Let \(P\) be a nonzero polynomial of total degree at most \(D'\) in \(x_1,\ldots,x_r\) over a field, and \(S_1,\ldots,S_r\) finite subsets of the field with \(|S_j|\ge s\). If \(X_1,\ldots,X_r\) are independent and \(X_j\) is uniform on \(S_j\), then
\[
\mathbb P\bigl(P(X_1,\ldots,X_r)=0\bigr)\le\frac{D'}s .
\]

*Proof.* Induction on \(r\); for \(r=0\), \(P\) is a nonzero constant. For \(r\ge1\) write \(P=\sum_{j=0}^ex_r^jP_j(x_1,\ldots,x_{r-1})\) with \(P_e\ne0\), so that \(P_e\) has degree at most \(D'-e\). By induction \(P_e(X_1,\ldots,X_{r-1})=0\) with probability at most \((D'-e)/s\). Otherwise, for fixed \(X_1,\ldots,X_{r-1}\), \(P\) is a nonzero polynomial of degree \(e\) in \(x_r\), with at most \(e\) roots, and \(X_r\) is one of them with conditional probability at most \(e/s\). \(\square\)

## 2. Girth

A closed walk in the voltage cover \(P\) projects to a closed walk in \(Y\) of the same length, based in the same layer, and with trivial holonomy (Section 2 of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md)). If the walk in \(P\) is cyclically nonbacktracking, so is its projection: the lift of an edge followed by its reverse is the lifted edge followed by its own reverse, because a lift is determined by its first vertex. So the girth condition (2.1) of that lesson holds as soon as every nonempty cyclically nonbacktracking closed walk of \(Y\), based in a layer \(i\) and of length at most \(C_*H_i/\log_2d\), has nontrivial holonomy.

**Proposition 2.1** (girth; [OpenAI-KK, Section 9.7]). For large \(\ell\) and every layer \(i\), the probability that some nonempty cyclically nonbacktracking closed walk of \(Y\) based in layer \(i\), of length at most \(C_*H_i/\log_2d\), has trivial holonomy is at most \(2^{-2H_i}\).

*Proof.* Fix such a walk \(w\), of length \(a\le C_*H_i/\log_2d\). Every edge of \(w\) belongs to a block whose *first index* \(j\) is the layer of its \(A\)-end, a vertex of \(w\); so \(|j-i|\le a\) and \(H_j\ge H_i-a\ge(1-C_*/\log_2d)H_i\).

*Case 1: some edge of \(w\) has first index \(j_0<I\).* Then all first indices \(j\) of edges of \(w\) are at most \(2I\). Indeed \(|j-j_0|\le a\le C_*(H_{j_0}+a)/\log_2d\), so \(a\le\epsilon_\ell H_{j_0}\) with \(\epsilon_\ell=2C_*/\log_2d\) for large \(\ell\), and \(j\le j_0+\epsilon_\ell(I+|j_0|)\); this is at most \((1+2\epsilon_\ell)I\le2I\) if \(0\le j_0<I\), and at most \(\epsilon_\ell I\) if \(j_0<0\). Let \(\pi_X:F\to U_{\mathbb Z}\) be the homomorphism to the unitriangular coordinate of the first factor (Section 3 of [An affine nilpotent group](an-affine-nilpotent-group.md)). By the construction of the draw, \(\pi_X(z_e)=b_{x_e}\), the unitriangular part of the first-factor element \(x_e\) of step 2, since \(z_0^n\) and the second-factor elements map to \(1\). So \(\pi_X\) of the holonomy of \(w\) is the holonomy word of \(w\) in the matrices \(b_{x_e}\), with \(b_{x_e}^{-1}\) on backward traversals. Condition on all choices other than the \(x_e\): the template pairs, frequencies, list entries and second-factor elements of all edges of \(w\). The \(x_e\) of the distinct undirected edges of \(w\) are then independent and uniform in their rectangles, and by Lemma 5.1(3) of the previous lesson their superdiagonal entries are independent and uniform on integer intervals with at least \(2^{E_0H_j}\) points. By Lemma 4.1 of the lesson on the word detector, some entry of the holonomy word minus \(1\) is a nonzero polynomial of degree at most \(m-1\) in these entries, and by Lemma 1.1 it vanishes with conditional probability at most \((m-1)2^{-E_0\min_jH_j}\).

*Case 2: all first indices are at least \(I\).* Use the homomorphism \(\pi_Y\) to the unitriangular coordinate of the second factor. Here \(\pi_Y(z_e)=b_{y_e}b_{v_e}\), where \(b_{y_e}=1+qY_e\) with \(Y_e\) strictly upper triangular with integer entries, and \(v_e\) is the chosen entry of the representative list. Condition on all choices other than the \(y_e\); then the \(b_{v_e}\) are fixed matrices of \(U\). By Lemma 4.1 of the lesson on the word detector, which allows fixed factors on either side, some entry of the holonomy word in the matrices \(b_{y_e}b_{v_e}\), minus \(1\), is a nonzero polynomial of degree at most \(m-1\) in the entries of the \(b_{y_e}\). The substitution \(b_{y_e}=1+qY_e\) is an invertible affine change of variables, so it stays a nonzero polynomial of degree at most \(m-1\) in the entries of the \(Y_e\). By Lemma 5.1(4) of the previous lesson these are independent and uniform on integer intervals with at least \(2^{E_0H_j}\) points, and Lemma 1.1 gives the same bound.

In both cases the probability of trivial holonomy is at most \((m-1)2^{-E_0(1-C_*/\log_2d)H_i}\). The layer \(i\) has \((d+1)2^{H_i}\) vertices, the maximum degree of \(Y\) is at most \(6D\), and \((6D)^a\le2^{a(2\log_2d+3)}\), so the number of walks to test is at most
\[
\begin{aligned}
&(d+1)2^{H_i}\sum_{1\le a\le C_*H_i/\log_2d}(6D)^a\\
&\quad\le2^{(3C_*+3)H_i}
\end{aligned}
\]
for large \(\ell\). Since \(E_0>10(C_*+C_\bullet+1)\), the union bound gives at most \((m-1)2^{(3C_*+3-E_0+o(1))H_i}\le2^{-2H_i}\). \(\square\)

## 3. Walks without singleton edges

In a walk, an undirected edge is a *singleton* if it is traversed exactly once. The *support* of a walk is the graph of its edges.

**Lemma 3.1** (walks without singleton edges; [OpenAI-KK, Lemma 9.5]). Let \(G\) be a graph of maximum degree \(\Delta\ge1\), in which parallel edges are distinct, \(v\) a vertex, and \(l\ge1\), \(b\ge0\) integers. The number of closed walks of length \(2l\) from \(v\) without singleton edges whose support has first Betti number at most \(b\) is at most
\[
\bigl(72(2b+2)^2\Delta\bigr)^l .
\]

*Proof.* The support \(S\) of such a walk is connected and has at most \(l\) edges, since every edge is traversed at least twice. Remove leaves other than \(v\) repeatedly, and let \(K\) be the remaining *core*. If \(S\) is a tree, \(K=\{v\}\). Otherwise \(K\) contains \(v\), \(b_1(K)=b_1(S)\le b\), and no vertex other than \(v\) has degree one in \(K\). For a connected graph, \(\sum_x(\deg_K(x)-2)=2b_1(K)-2\) (Exercise 6.3); all terms are nonnegative except possibly the root term, which is at least \(-1\), so every degree in \(K\) is at most \(2b+1\). The removed parts are trees, each attached to \(K\) at exactly one vertex: a removed part containing a cycle, or a path between two vertices of \(K\), could not have been removed leaf by leaf.

*The cores.* A connected subgraph \(K\ni v\) with \(a\) edges is determined by an exploration from \(v\): while some edge of \(K\) at the current vertex is unmarked, mark one, traverse it and push it on a stack, also if its far end was visited before; otherwise pop the top edge and return along it. Every edge of \(K\) is pushed and popped exactly once, and since \(K\) is connected the exploration reaches all of it. The word of pushes and pops has length \(2a\), and each push chooses one of at most \(\Delta\) edges at the current vertex, while a pop is determined by the stack. So there are at most \(4^a\Delta^a\) cores with \(a\) edges.

*The walks with a given core.* Declare every step a *core step*, along an edge of \(K\); a *descent*, from a vertex into a removed tree away from \(K\); or a *return*, toward \(K\). There are at most \(3^{2l}\) words of types. A core step has at most \(2b+2\) choices, a descent at most \(\Delta\), and a return is forced, as the edge toward \(K\) in a tree is unique. Every excursion into a removed tree begins and ends at its attachment vertex, so with \(c\) core steps and \(t\) descents there are \(t\) returns and \(2t+c=2l\). Every edge of \(K\) is traversed at least twice, so \(c\ge2a\) and \(t\le l-a\). This bounds the walks with core \(K\) by \(3^{2l}(2b+2)^{2l}\Delta^{l-a}\), also counting invalid type words. Multiplying by the number of cores and summing over \(0\le a\le l\), with \(\sum_{a\le l}4^a\le(l+1)4^l\le8^l\),
\[
\begin{aligned}
&\sum_{a=0}^l4^a\Delta^a\,9^l(2b+2)^{2l}\Delta^{l-a}\\
&\quad\le\bigl(72(2b+2)^2\bigr)^l\Delta^l .\qquad\square
\end{aligned}
\]

## 4. Centered moments

For an adjacent pair \((i,k)\), let \(X_{ik}\) be the operator from \(\ell^2(B_k\cap V(Y))\otimes\ell^2(F)\otimes\mathbb C^N\) to \(\ell^2(A_i\cap V(Y))\otimes\ell^2(F)\otimes\mathbb C^N\) with the entries
\[
\begin{aligned}
(X_{ik})_{ab}&=\sum_{e:\,a\to b}\Bigl(W_e\rho(z_e)\\
&\qquad-\mathbb E_{\mathcal D_{ik}}\bigl[W\rho(z)\bigr]\Bigr) .
\end{aligned}
\]

**Proposition 4.1** (block deviations; [OpenAI-KK, Section 9.8]). There is a fixed \(C_2\) such that for large \(\ell\) and every adjacent pair \((i,k)\),
\[
\mathbb P\Bigl(\|X_{ik}\|>\varepsilon\sqrt{dD_{ik}}\Bigr)\le2^{-4H_i} .
\]

*Proof.* *The finite test.* By Lemma 5.1(2) of the previous lesson, all possible voltages of the block and their inverses have coordinates at most \(x^C\), \(x=2^{H_i}\), for a fixed \(C\). Let \(\tilde X\) be the self-adjoint doubling of \(X_{ik}\) on \(\ell^2(J)\otimes\ell^2(F)\otimes\mathbb C^N\), \(J=(A_i\cup B_k)\cap V(Y)\). A vertex of \(A_i\) has at most \(d\) edges in the block and a vertex of \(B_k\) at most \(D_{ik}\le2D\), and each centered term has coefficient norms summing to at most \(2C_W\); so the rows of \(\tilde X\) have coefficient norm sums at most \(4C_WD\). Lemma 4.1 of [The model operator and finite tests](the-model-operator-and-finite-tests.md), with \(B=1\) and all possible voltages and their inverses as \(G\), gives a box \(\mathfrak B\) with \(|\mathfrak B|\le2^{cH_i}\), independent of the draws, such that
\[
\begin{aligned}
\|X_{ik}\|&\le\|P\tilde XP\|+C2^{-H_i}\cdot4C_WD\\
&\le\|P\tilde XP\|+\tfrac12\varepsilon\sqrt{dD_{ik}},
\end{aligned}
\]
the last inequality for large \(\ell\), because \(2^{H_i}\ge2^{H_0}\ge d^{5000}\) while \(\sqrt{dD_{ik}}\ge d^{3/2}/\sqrt2\). The operator \(P\tilde XP\) acts on a space of dimension at most \((d+1)2^{H_i+1}\cdot2^{cH_i}\cdot q^{n_{\mathrm f}}\le2^{C_1H_i}\), with \(C_1\) fixed, since \(q^{n_{\mathrm f}}=2^{A_*n_{\mathrm f}\log_2d}\le2^{A_*n_{\mathrm f}H_i}\).

Choose \(C_2>2(C_1+4)\), and put \(l=\lceil C_2H_i/\log_2d\rceil\).

*The expansion.* Write \(Z_e=W_e\rho(z_e)-\mathbb E_{\mathcal D_{ik}}[W\rho(z)]\), so that \(\mathbb EZ_e=0\) and \(\|Z_e\|\le2C_W\). The projection \(P\) keeps all vertex indices, so \(\operatorname{Tr}((P\tilde XP)^{2l})\) is the sum, over the closed walks \(x_0,x_1,\ldots,x_{2l}=x_0\) of length \(2l\) in the graph of the block, of the traces over deck and matrix indices of the products \(PZ^\pm_{e_1}P\cdots PZ^\pm_{e_{2l}}P\), where \(e_s\) is the edge of step \(s\) and \(Z^\pm_e\) is \(Z_e\) or \(Z_e^*\) according to its direction. If some undirected edge \(e\) is a singleton, condition on the pairs of all other edges: the product is \(\mathcal L\,PZ^\pm_eP\,\mathcal R\) with \(\mathcal L,\mathcal R\) independent of \(Z_e\), and its expected trace is \(\operatorname{Tr}(\mathcal L\,P\,\mathbb E[Z^\pm_e]\,P\,\mathcal R)=0\). Every other term has absolute value at most \(|\mathfrak B|N(2C_W)^{2l}\), the dimension at one vertex times the product of the norms.

*The count.* The support of a walk without singleton edges has at most \(l\) edges and lies in the layers \(i\) and \(k\). By Proposition 4.1(5) of [Pruning and recovery of long paths](pruning-and-recovery-of-long-paths.md), each of its embedded circles, a cyclically nonbacktracking closed path based in layer \(i\) or \(k\), has length greater than \(g=(H_i-1)/(100\log_2d)\). As a metric graph with unit edges, the support has girth greater than \(g\) and total length at most \(l\le101C_2g\) for large \(\ell\), so by Lemma 1.1 of [A word detector in unitriangular matrices](a-word-detector-in-unitriangular-matrices.md) its first Betti number is at most \(b=B(101C_2)\). By Lemma 3.1 with \(\Delta\le6D\), each base vertex has at most \((432(2b+2)^2D)^l\) such walks. With at most \((d+1)2^{H_i+1}\) base vertices,
\[
\begin{gathered}
\mathbb E\operatorname{Tr}\bigl((P\tilde XP)^{2l}\bigr)\le2^{C_1H_i}\,(C_4D)^l,\\
C_4=1728(2b+2)^2C_W^2 .
\end{gathered}
\]
The constant \(C_4\) is fixed after \(C_2\) and does not depend on \(i\) or \(\ell\); the dimension exponent \(C_1\) is unchanged.

*Markov's inequality.* Since \(\|P\tilde XP\|^{2l}\le\operatorname{Tr}((P\tilde XP)^{2l})\) and \(D_{ik}\ge D/2\),
\[
\begin{aligned}
&\mathbb P\Bigl(\|X_{ik}\|>\varepsilon\sqrt{dD_{ik}}\Bigr)\\
&\quad\le\mathbb P\Bigl(\|P\tilde XP\|>\tfrac12\varepsilon\sqrt{dD_{ik}}\Bigr)\\
&\quad\le2^{C_1H_i}\Bigl(\frac{8C_4}{\varepsilon^2d}\Bigr)^l .
\end{aligned}
\]
For large \(\ell\), \(8C_4/\varepsilon^2\le d^{1/2}\), and then the right side is at most \(2^{C_1H_i}d^{-l/2}\le2^{(C_1-C_2/2)H_i}\le2^{-4H_i}\). \(\square\)

The integer \(m\) of the word detector does not enter this argument: the cycle rank of the supports is bounded by the girth of the tower alone, so \(C_2\) can be chosen after \(m\).

## 5. A simultaneous choice and the realization theorem

**Proposition 5.1** (a simultaneous choice; [OpenAI-KK, Section 9.9]). For large \(\ell\) there is an assignment of pairs \((W_e,z_e)\), each in the support of the distribution of its block, such that

- (R1) every nonempty cyclically nonbacktracking closed walk of \(Y\), based in a layer \(i\) and of length at most \(C_*H_i/\log_2d\), has nontrivial holonomy, and
- (R2) \(\|X_{ik}\|\le\varepsilon\sqrt{dD_{ik}}\) for every adjacent pair \((i,k)\).

*Proof.* Each requirement, one walk in (R1) or one block in (R2), depends on the pairs of finitely many edges, since every block has finitely many edges, although its operator acts on an infinite deck space. For independent draws on any finite set of edges, Propositions 2.1 and 4.1 and the union bound bound the probability that some requirement depending only on these edges fails by
\[
\begin{aligned}
\sum_{i\in\mathbb Z}2^{-2H_i}+\sum_{i\in\mathbb Z}3\cdot2^{-4H_i}&\le6\cdot2^{-2H_0}\\
&<1 ,
\end{aligned}
\]
with at most three blocks for each first index. Enumerate the positive edges \(e_1,e_2,\ldots\) and the requirements \(R_1,R_2,\ldots\). For each \(n\), the finitely many edges on which \(R_1,\ldots,R_n\) depend admit an assignment satisfying \(R_1,\ldots,R_n\); extend it to all edges by fixed elements of the supports, and call the result \(\alpha_n\). Each edge has finitely many possible pairs, so successive subsequences and the diagonal give a subsequence along which \(\alpha_n(e_j)\) is eventually constant for every \(j\); let \(\alpha\) be the limit. A requirement \(R_r\) depends on finitely many edges, on which \(\alpha\) agrees with \(\alpha_n\) for all large \(n\) of the subsequence, and \(\alpha_n\) satisfies \(R_r\) for \(n\ge r\). So \(\alpha\) satisfies every requirement. \(\square\)

*Proof of Theorem 3.1 of [The model operator and finite tests](the-model-operator-and-finite-tests.md).* Take the assignment of Proposition 5.1, with \(\varepsilon=\eta/6\).

(1) \(\|W_e\|\le C_W=:C_\eta\). The pairs \((\text{label},W_e)\) number \(o(dD)\) by Lemma 5.1(1) of [Masks, lists and one draw per edge](masks-lists-and-one-draw-per-edge.md), and \(D_{ik}=D2^{|i|-|k|}\) is determined by the family in the label, which determines \(k-i\) and the signs of \(i\) and \(k\) (Section 3 of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md)).

(2) By (R1) and Section 2, the cover satisfies the girth condition.

(3) Fix an adjacent pair \((i,k)\). The entries of the block of \(T_P\) from \(B_k\) to \(A_i\) are \((dD_{ik})^{-1/2}\) times
\[
\begin{aligned}
&\sum_{e:\,a\to b}W_e\rho(z_e)\\
&\quad=\#\{e:a\to b\}\;\mathbb E_{\mathcal D_{ik}}[W\rho(z)]\\
&\qquad+(X_{ik})_{ab} .
\end{aligned}
\]
The first part, normalized, is \(\Pi U^0_{ik}\Pi\otimes\mathbb E_{\mathcal D_{ik}}[W\rho(z)]\), the compression of the normalized incidence to the surviving vertices tensored with the expectation of one draw, because the distribution is the same for all edges of the block. The block of \(\Pi O\Pi\) is \(\Pi U^0_{ik}\Pi\otimes h_ih_kp\) in every fiber. Since \(\|\Pi U^0_{ik}\Pi\|\le1\), Proposition 4.1 of the previous lesson and (R2) bound the block of \(T_P-\Pi O\Pi\) by \(\varepsilon+\varepsilon=2\varepsilon\), and the same holds for the adjoint blocks. The operator \(T_P-\Pi O\Pi\) is self-adjoint of layer width one, so each row of blocks has at most three nonzero blocks; the Schur test with block norms, \(|\langle K\xi,\zeta\rangle|\le\sum_{\alpha,\beta}\|K_{\alpha\beta}\|\|\xi_\beta\|\|\zeta_\alpha\|\), gives
\[
\|T_P-\Pi O\Pi\|\le3\cdot2\varepsilon=\eta .\qquad\square
\]

The constants are fixed in this order: the geometric constants \(C_*\), \(C_\bullet\), the integer \(m\) and the functions \(J_\pm\); then \(E_0\), \(A_*\), \(\kappa\); then the accuracy \(\eta\), hence \(\varepsilon\) and all the data of the previous lesson; then the test exponent \(C_1\) and the moment constant \(C_2\); and only then is \(\ell\) taken large. All estimates are uniform in the layers.

## 6. Exercises

**6.1** (easy). Show that Lemma 1.1 is sharp: find a nonzero polynomial of degree \(D'\) in one variable that vanishes with probability exactly \(D'/s\) at a uniform point of a set of \(s\ge D'\) elements.

**6.2** (easy). In the star with center \(v\) and \(\Delta\) leaves, count the closed walks of length \(4\) from \(v\) without singleton edges, and compare with Lemma 3.1.

**6.3** (medium). Show that \(\sum_x(\deg_K(x)-2)=2b_1(K)-2\) for a finite connected graph \(K\), and deduce that a connected graph with \(b_1(K)\le b\), in which every vertex other than one has degree at least two, has maximum degree at most \(2b+1\).

**6.4** (medium). Give countably many requirements on a sequence \((x_1,x_2,\ldots)\) of natural numbers, each depending on finitely many coordinates, such that every finite family of them can be satisfied but not all of them together. Which hypothesis of the argument in Proposition 5.1 fails?

## 7. Solutions

**6.1.** \(P(x)=\prod_{j=1}^{D'}(x-s_j)\) with distinct \(s_j\in S_1\) vanishes exactly at the \(D'\) points \(s_j\), with probability \(D'/s\).

**6.2.** Such a walk is \(v\to x\to v\to y\to v\) with leaves \(x,y\); if \(x\ne y\) both edges are used twice, and if \(x=y\) the edge is used four times. So there are \(\Delta^2\) walks. Lemma 3.1 with \(b=0\) and \(l=2\) gives \((288\Delta)^2\), of the same order \(\Delta^l\) with a much larger constant.

**6.3.** With \(V\) vertices and \(E\) edges, \(b_1(K)=E-V+1\) and \(\sum_x\deg_K(x)=2E\), so \(\sum_x(\deg_K(x)-2)=2E-2V\), which is \(2b_1(K)-2\). If every term is nonnegative except one, which is at least \(-1\), then each single term is at most \(2b-2+1\), so every degree is at most \(2b+1\).

**6.4.** Let \(R_n\) be the requirement \(x_1\ge n\). Every finite family is satisfied by a large \(x_1\), but no natural number satisfies all of them. The coordinates have infinitely many possible values, so no subsequence of solutions need be eventually constant at \(x_1\); in Proposition 5.1 every edge has finitely many possible pairs.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 9.7 to 9.9, Lemma 9.5. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
