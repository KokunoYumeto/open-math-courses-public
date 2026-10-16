# Fundamental classes from finite chart gluing

*Written and self-checked by GPT-6 Astra (OpenAI), at Ultra, October 2026. New exposition dedicated to the public domain under CC0.*

A fundamental class is characterized by what it does near each point. This chapter constructs the class with coefficients in \(\mathbb F_2=\mathbb Z/2\mathbb Z\) by combining finitely many coordinate neighbourhoods around a compact set. The construction uses singular chains and does not require a triangulation, a cell decomposition or a smooth structure.

Let \(M\) be a Hausdorff topological manifold of dimension \(d\geq0\), without boundary. Thus each point has an open neighbourhood homeomorphic to an open subset of \(\mathbb R^d\). Second countability is permitted but is not needed for the compact-set arguments here. All homology in this chapter has coefficients in \(\mathbb F_2\). We write
\[
H_q(M\mid K)=H_q(M,M\setminus K;\mathbb F_2).
\tag{A.1}
\]
For \(L\subset K\), inclusion of the complementary subspaces gives a **restriction**
\[
r_{K,L}:H_q(M\mid K)\longrightarrow H_q(M\mid L).
\tag{A.2}
\]
These maps are induced by the identity on the numerator singular-chain complex; hence \(r_{L,J}r_{K,L}=r_{K,J}\) whenever \(J\subset L\subset K\). For \(K=\varnothing\) the relative complex is zero.

The required chain theory is proved in the earlier Thom chapter: [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1) gives the boundary and prism identities; [DG-CHAR-06 E.1](DG-CHAR-06.md#lemma-e-1) gives the exact sequence of complexes; [DG-CHAR-06 E.2](DG-CHAR-06.md#theorem-e-2) proves excision; [DG-CHAR-06 E.4](DG-CHAR-06.md#lemma-e-4) proves the exact sequence for two supports; and [DG-CHAR-06 E.5](DG-CHAR-06.md#lemma-e-5) computes sphere and punctured-space homology with arbitrary coefficients. We use their ordinary singular-chain versions, which apply to topological spaces. The elementary compactness and norm facts used below are proved in [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

## A. What a chain determines near a point

**Lemma A.1 (local groups and convex supports).** At every \(x\in M\),
\[
H_q(M\mid\{x\})\cong
\begin{cases}
\mathbb F_2,&q=d,\\
0,&q\ne d.
\end{cases}
\tag{A.3}
\]
Write \(\mu_x\) for the unique nonzero element in degree \(d\). If \(P\subset\mathbb R^d\) is nonempty, compact and convex, restriction to any \(x\in P\) gives an isomorphism
\[
H_q(\mathbb R^d\mid P)\longrightarrow H_q(\mathbb R^d\mid\{x\}).
\tag{A.4}
\]
Consequently \(P\) has a unique class \(\mu_P\) with nonzero restriction at every one of its points. The same assertion holds for the inverse image of \(P\) in a manifold chart containing it.

**Proof.** Compact subsets of a Hausdorff space are closed by [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). If a compact \(K\) lies in an open chart \(U\subset M\), excision gives
\[
H_q(U,U\setminus K)\ \cong\ H_q(M,M\setminus K).
\tag{A.5}
\]
Indeed, excise the closed set \(M\setminus U\), which is contained in the open set \(M\setminus K\). The chart homeomorphism identifies the left-hand pair with the corresponding pair in its open image \(V\subset\mathbb R^d\). Excising \(\mathbb R^d\setminus V\) from the Euclidean pair gives the further identification
\[
H_q(V,V\setminus K')\ \cong\
H_q(\mathbb R^d,\mathbb R^d\setminus K'),
\tag{A.6}
\]
where \(K'\) is the compact chart image. Both identifications commute with restrictions to compact subsets, because they arise from inclusions of pairs and a homeomorphism.

For \(K=\{x\}\), the Euclidean group in (A.6) is computed in [DG-CHAR-06 E.5](DG-CHAR-06.md#lemma-e-5). In positive dimension its reduced pair sequence identifies it with the reduced homology of a punctured Euclidean space, shifted by one degree. Radial deformation retracts that space onto \(S^{d-1}\), whose groups are computed there. In degree zero the relative group is zero because the complement is nonempty and maps onto the connected ambient space's degree-zero group. In dimension zero the pair is one point relative to the empty set. Its degree-zero homology is \(\mathbb F_2\), and its higher groups vanish. This proves (A.3). Since a one-dimensional \(\mathbb F_2\)-vector space has a single nonzero element, \(\mu_x\) does not require an orientation choice or a preferred chart.

For (A.4), translate \(x\) to the origin and choose \(R>\sup_{p\in P}|p|\). On either complement use
\[
H(v,t)=\left(1-t+\frac{tR}{|v|}\right)v,\qquad 0\leq t\leq1.
\tag{A.7}
\]
It fixes the sphere of radius \(R\) and retracts the complement of the origin onto that sphere. It also preserves the complement of \(P\). If \(v\notin P\) and \(|v|\leq R\), the homotopy moves outward on its ray. Were \(\lambda v\in P\) for \(\lambda\geq1\), convexity and \(0\in P\) would imply
\(v=\lambda^{-1}(\lambda v)+(1-\lambda^{-1})0\in P\), a contradiction. If \(|v|>R\), the homotopy has norm at least \(R\) throughout and misses \(P\).

Thus inclusion of these two complements is a homotopy equivalence through their common sphere. Homotopy invariance and the natural pair sequence, [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1) and [DG-CHAR-06 E.1](DG-CHAR-06.md#lemma-e-1), show that (A.4) is an isomorphism in every positive degree; the zero-degree relative groups both vanish for \(d>0\). For \(d=0\) there is just the one-point pair. This is also the explicit convex-support proof in [DG-CHAR-06 E.6](DG-CHAR-06.md#corollary-e-6).

The group in degree \(d\) in (A.4) is \(\mathbb F_2\). Its unique nonzero class maps to a nonzero class at every point because each map (A.4) is an isomorphism. This gives \(\mu_P\). Equations (A.5) and (A.6) transfer the assertion to chart supports. □

**Lemma A.2 (local comparison of values).** Let \(K\subset M\) be compact and let \(\alpha\in H_d(M\mid K)\). For \(x\in K\), write
\[
r_{K,\{x\}}\alpha=c_\alpha(x)\mu_x,\qquad c_\alpha(x)\in\mathbb F_2.
\tag{A.8}
\]
The function \(c_\alpha:K\to\mathbb F_2\), where the target is discrete, is locally constant.

**Proof.** Represent \(\alpha\) by a finite singular chain \(z\) whose boundary lies in \(C_{d-1}(M\setminus K;\mathbb F_2)\). After cancellation of equal simplices, let \(C\) be the union of the images of the simplices in \(\partial z\). This set is compact, since each simplex is compact, and it is disjoint from \(K\). It is therefore closed in \(M\). For a given \(x\in K\), take a chart and a closed coordinate ball \(B\) around \(x\), with \(x\) in its interior, such that \(B\) lies in the chart and avoids \(C\). Such a ball exists because the complement of \(C\) is an open neighbourhood of \(x\). In dimension zero use the one-point chart.

The same chain \(z\) is a relative cycle for \(M\mid B\). By A.1 its class there is either zero or \(\mu_B\), and its restrictions are respectively zero at every point of \(B\) or \(\mu_y\) at every \(y\in B\). For \(y\in K\cap B\), this restriction is also the point restriction of \(\alpha\), since both use the same chain \(z\). Thus \(c_\alpha\) is constant on \(K\cap\operatorname{int}B\), proving local constancy.

The class of \(z\) relative to points outside \(K\) need not be independent of the chosen representative of \(\alpha\). The assertion only compares the well-defined restrictions on \(K\); no extension outside \(K\) is part of its conclusion. □

## B. Detection and existence on a compact support

**Theorem B.1 (point restrictions detect the top group).** For every compact \(K\subset M\),
\[
H_q(M\mid K)=0\quad(q>d),
\qquad
H_d(M\mid K)\longrightarrow
\prod_{x\in K}H_d(M\mid\{x\})
\ \text{is injective}.
\tag{B.1}
\]

**Proof.** We prove both statements together. The two-support sequence [DG-CHAR-06 E.4](DG-CHAR-06.md#lemma-e-4), for compact and hence closed \(A,B\subset M\), has the form
\[
\begin{aligned}
\cdots&\longrightarrow H_{q+1}(M\mid A\cap B)
\longrightarrow H_q(M\mid A\cup B)
\\
&\longrightarrow H_q(M\mid A)\oplus H_q(M\mid B)
\\
&\longrightarrow H_q(M\mid A\cap B)\longrightarrow\cdots.
\end{aligned}
\tag{B.2}
\]
Its middle map consists of the two restrictions, and the next map is their difference, equal to their sum over \(\mathbb F_2\). The earlier proof obtains this exact sequence from quotient singular-chain complexes and the small-chain equivalence for the open complements; it is valid for these topological spaces.

Suppose the two conclusions hold on \(A,B,A\cap B\). If \(q>d\), the group of the union in (B.2) has zero group on either side, so it vanishes. In degree \(d\), the preceding intersection group is zero, so restriction to the two pieces is injective. A class whose restrictions at all points of the union vanish restricts to zero on each piece by their detection property, and hence is zero. Therefore both conclusions pass to \(A\cup B\).

Begin in \(\mathbb R^d\). Empty supports have zero relative groups. For nonempty compact convex supports, A.1 proves both conclusions. They follow for every finite union of compact convex sets by induction on the number of sets: the intersection of the last set with the preceding union is a union of at most one fewer compact convex sets, so the same induction covers that intersection.

Now let \(K\subset\mathbb R^d\) be arbitrary compact and nonempty. If \(d=0\), it is the one-point set and has already been treated. Otherwise, represent any relative class \(\alpha\) by a finite chain \(z\), and let \(C\) be the compact support of its boundary as in A.2. If \(C\ne\varnothing\), its distance from \(K\) is positive. For an elementary verification, if the infimum were zero, choose \(c_j\in C,k_j\in K\) with \(|c_j-k_j|<1/j\). Compactness supplies successive subsequences with \(c_j\to c\in C\) and \(k_j\to k\in K\); then \(c=k\), contrary to disjointness. The compactness and subsequence facts are [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

Choose closed balls centred at points of \(K\), small enough to avoid \(C\), whose interiors cover \(K\); retain finitely many by compactness. If \(C\) is empty there is no avoidance restriction. Their union \(P\) is a finite union of compact convex sets, contains \(K\), and avoids \(C\). The same chain \(z\) gives a class \(\beta\in H_q(\mathbb R^d\mid P)\) with \(r_{P,K}\beta=\alpha\).

For \(q>d\), the proved vanishing on \(P\) gives \(\beta=0\), hence \(\alpha=0\). In degree \(d\), assume every point restriction of \(\alpha\) is zero. For each chosen ball \(B\), its centre \(x\) belongs to \(K\). The restriction of \(\beta\) to \(B\) restricts to zero at \(x\), so A.1 makes it zero on \(B\). Consequently \(\beta\) restricts to zero at every point of the union \(P\), and finite-union detection gives \(\beta=0\). Again \(\alpha=0\). This proves both statements for all compact Euclidean supports.

For a compact support in one chart of \(M\), transfer this result using the excision identifications (A.5) and (A.6), which commute with point restrictions.

Finally take a general compact \(K\subset M\). Around each point of \(K\) choose an open coordinate ball \(V\) whose closed ball lies within the chart. That closed ball is compact in \(M\), being the continuous image of a compact Euclidean ball, and closed because \(M\) is Hausdorff. It is the closure of \(V\) in \(M\): it is closed, contains \(V\), and every point of its boundary is a limit of points of \(V\) in the chart. Choose finitely many of the opens \(V_1,\ldots,V_m\) covering \(K\) and put \(K_j=K\cap\overline V_j\).

These compact sets cover \(K\), each lies in one chart, and their finite intersections remain compact. Induct on the number of such chart-contained pieces. The intersection
\[
(K_1\cup\cdots\cup K_{m-1})\cap K_m
=\bigcup_{j<m}(K_j\cap K_m)
\]
has at most \(m-1\) chart-contained compact pieces. Thus the induction hypothesis applies to it as well as to the preceding union and the last piece. The union argument from (B.2) completes the proof. Only finitely many charts around each compact support were used. □

**Theorem B.2 (the canonical compact-support class).** Each compact \(K\subset M\) has a unique class
\[
\mu_K\in H_d(M\mid K)
\quad\text{such that}\quad
r_{K,\{x\}}\mu_K=\mu_x\quad(x\in K).
\tag{B.3}
\]
For compact \(L\subset K\), these classes satisfy \(r_{K,L}\mu_K=\mu_L\).

**Proof.** Uniqueness follows from B.1, by subtracting two classes with the prescribed point restrictions. Set \(\mu_\varnothing=0\).

For nonempty compact \(K\subset\mathbb R^d\), take a closed ball \(P\) containing it. A.1 supplies \(\mu_P\), whose image in \(H_d(\mathbb R^d\mid K)\) has all the required point restrictions, by composition of restrictions. In dimension zero take \(P=\mathbb R^0\). For \(K\) lying in a chart with image \(V\subset\mathbb R^d\), perform this construction in all of \(\mathbb R^d\) and then use the inverse of the excision isomorphism (A.6). The large ball is not required to lie in \(V\); only \(K\) must do so. Equation (A.5) then gives the class on \(M\). The maps to point groups are isomorphisms, hence preserve their unique nonzero elements.

For general \(K\), use the finite chart-contained pieces in B.1. Suppose classes have been constructed on \(A=K_1\cup\cdots\cup K_{j-1}\) and \(B=K_j\). Their restrictions to \(A\cap B\) have the same point values. B.1's detection on that compact intersection therefore makes these two restrictions equal. Exactness of (B.2) gives a class on \(A\cup B\) with the specified restrictions to \(A\) and \(B\). It has the required values at every point of the union. Induction gives \(\mu_K\), and uniqueness makes the construction independent of the chosen charts, balls and gluing lifts.

Finally \(r_{K,L}\mu_K\) has the prescribed values at every point of \(L\). Uniqueness on \(L\) identifies it with \(\mu_L\), proving compatibility. □

## C. Closed manifolds

**Corollary C.1 (the mod-two fundamental class).** If \(M\) is compact and without boundary, it has a unique class
\[
[M]_2\in H_d(M;\mathbb F_2)
\]
whose image at every point is \(\mu_x\), and \(H_q(M;\mathbb F_2)=0\) for \(q>d\). If \(M\) has \(c\) connected components, then
\[
H_d(M;\mathbb F_2)\cong\mathbb F_2^{\,c},
\tag{C.1}
\]
with the component fundamental classes as a basis and \([M]_2\) their sum. This includes \(c=0\) for the empty manifold.

**Proof.** Put \(K=M\) in B.1 and B.2. Its complement is empty, so the relative groups are the absolute groups. This gives the existence, uniqueness and vanishing assertions.

For a connected nonempty \(M\), A.2 says that the local coefficient of any \(\alpha\in H_d(M;\mathbb F_2)\) is locally constant on \(M\). A locally constant map to \(\{0,1\}\) on a connected space is constant: its two inverse images are disjoint open sets covering the space, and if both were nonempty they would disconnect it. If the coefficient is zero, B.1 gives \(\alpha=0\); if it is one, B.2 gives \(\alpha=[M]_2\). Thus this group is precisely \(\mathbb F_2\), and restriction to any point is an isomorphism.

Every point has a connected open coordinate-ball neighbourhood. Each connected component of \(M\) is therefore open: it contains such a neighbourhood of each of its points. The components are also closed, because their complements are unions of the other open components. Compactness of \(M\) now implies that there are finitely many components, and each is compact.

A singular simplex has connected image, since its domain is convex and hence path connected. It therefore lies in one component. The singular-chain complex of \(M\) consequently splits as the direct sum of the complexes of these finitely many components, with boundary respecting the summands. Kernels and images of this componentwise boundary split in the same way, so homology does too. Applying the connected case to each component gives (C.1). The sum of its component classes has the required value at each point, so it is \([M]_2\) by uniqueness. A compact zero-manifold is a finite discrete set; here the same construction is exactly the sum of its point classes. The empty singular-chain complex gives the stated empty case. □

## Further reading

Allen Hatcher, [*Algebraic Topology*, author-hosted Chapter 3](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf), Section 3.3, especially Lemma 3.27 and Theorem 3.26 on pages 236–238. The local-homology and compact-gluing arguments above use this freely accessible author version together with the exact programme chain proofs linked in the text. No external theorem is used as a substitute for those proofs.
