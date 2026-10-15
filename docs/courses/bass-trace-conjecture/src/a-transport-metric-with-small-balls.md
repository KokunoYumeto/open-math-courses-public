# A transport metric with small balls

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the proof of the sparse-chain vanishing theorem (Theorem 5.1 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md)). The proof cuts the simplicial complex \(K\) into small pieces and compares areas of the cuts. It needs two kinds of geometric structure. A metric on the realization of \(K\) gives balls in which to cut: it is the transport distance between probability vectors, scaled by \(1/\sqrt n\). Euclidean structures on the top simplices, one for each spanning tree of the vertex set, give areas: each top simplex has volume \(1/n!\), and every distance function has gradient of norm at most one. Because the graph has bounded degree, a ball of fixed radius meets only exponentially many top simplices, and in high dimension the total volume of a ball is much smaller than the volume that the cutting argument of the later lessons produces. This margin fixes the dimension bound \(n_0(D)\). The lesson follows [OpenAI-BT, Section 3].

- The setting (Section 1).
- Potentials and the transport metric (Section 2).
- Local finiteness (Section 3).
- Tree Euclidean structures (Section 4).
- The volume margin in high dimension (Section 5).

## 1. The setting

Throughout this lesson and the next three, \(D\ge2\), \(Y\) is the vertex set of a countable connected simple graph in which every vertex has at most \(D\) neighbours, \(d\) is the graph distance on \(Y\), and a countable group \(H\) acts on the graph by automorphisms, freely on vertices. Let \(n\ge1\) and let \(K\) be a nonempty \(H\)-invariant simplicial complex on \(Y\) as in Theorem 5.1: every simplex is a face of an \(n\)-simplex, there are finitely many \(H\)-orbits of simplices, and the vertices of every \(n\)-simplex span a connected subgraph. The \(n\)-simplices are the *top simplices*; the simplices of \(K\) are called *original* to distinguish them from subdivisions in later lessons.

The *realization* \(|K|\) is the set of functions \(p:Y\to[0,1]\) with finite support, \(\sum_yp(y)=1\), and \(\operatorname{supp}p\in K\). For a simplex \(\sigma\in K\), with vertex set \(V(\sigma)\), the *closed simplex* is the set of \(p\in|K|\) with \(\operatorname{supp}p\subseteq V(\sigma)\), and its *relative interior* \(\sigma^\circ\) is the set with \(\operatorname{supp}p=V(\sigma)\). We use the same letter for a simplex and its closed simplex. A closed simplex is a convex set in the vector space \(\mathbb R^{(Y)}\) of finitely supported functions, and its *affine span* is the set of \(x\in\mathbb R^{(Y)}\) supported in \(V(\sigma)\) with \(\sum_yx(y)=1\).

## 2. Potentials and the transport metric

A function \(\ell:Y\to\mathbb R\) is *\(1\)-Lipschitz* if \(|\ell(v)-\ell(w)|\le d(v,w)\) for all \(v,w\). For \(p,q\in|K|\) put
\[
\begin{aligned}
&\sqrt n\,\rho(p,q)\\
&\ =\sup_\ell\ \sum_{v\in Y}\ell(v)\\
&\qquad\cdot\bigl(p(v)-q(v)\bigr),
\end{aligned}
\tag{2.1}
\]
the supremum over \(1\)-Lipschitz functions \(\ell\). This is the Kantorovich–Rubinstein form of the transport distance between \(p\) and \(q\), scaled by \(1/\sqrt n\); the properties needed are proved below. For a finite nonempty set \(V\subseteq Y\) let
\[
\begin{aligned}
\mathcal P_V=\Bigl\{&\ell\in\mathbb R^V:\ \sum_{v\in V}\ell(v)=0,\\
&|\ell(v)-\ell(w)|\le d(v,w)\\
&\qquad\text{for all }v,w\in V\Bigr\}.
\end{aligned}
\]

**Lemma 2.1.** (a) \(\mathcal P_V\) is compact and contains \(0\).
(b) Every \(\ell\in\mathcal P_V\) is the restriction to \(V\) of a \(1\)-Lipschitz function on \(Y\).
(c) If \(p\), \(q\) are supported in \(V\), the supremum in (2.1) is finite and equals \(\max_{\ell\in\mathcal P_V}\sum_v\ell(v)(p(v)-q(v))\).

*Proof.* (a) \(\mathcal P_V\) is closed. For \(\ell\in\mathcal P_V\), the zero sum gives a coordinate \(\le0\) and one \(\ge0\), so every coordinate has absolute value at most \(\max_{v,w\in V}d(v,w)\); so \(\mathcal P_V\) is bounded.
(b) Put \(\tilde\ell(y)=\min_{v\in V}(\ell(v)+d(v,y))\). Each function \(y\mapsto\ell(v)+d(v,y)\) is \(1\)-Lipschitz by the triangle inequality, and so is their minimum. For \(w\in V\), the term \(v=w\) gives \(\tilde\ell(w)\le\ell(w)\), and \(\ell(v)+d(v,w)\ge\ell(w)\) for all \(v\) gives equality.
(c) Only the values of \(\ell\) on \(V\) enter the sum, and adding a constant to \(\ell\) does not change it, because \(\sum_v(p(v)-q(v))=0\). The restriction of a \(1\)-Lipschitz function to \(V\), minus its mean over \(V\), lies in \(\mathcal P_V\); conversely (b) extends elements of \(\mathcal P_V\). So the supremum is the maximum of a continuous function on the compact set \(\mathcal P_V\). \(\square\)

**Lemma 2.2.** (a) For all \(p,q\in|K|\) and \(v\in Y\),
\[
|p(v)-q(v)|\le\sqrt n\,\rho(p,q).
\tag{2.2}
\]
(b) \(\rho\) is a metric on \(|K|\), and \(\rho(hp,hq)=\rho(p,q)\) for \(h\in H\), where \((hp)(y)=p(h^{-1}y)\).
(c) On the set of points supported in a fixed finite set \(V\), \(\rho\) is the restriction of a norm on the space of \(x\in\mathbb R^V\) with \(\sum x=0\). In particular every closed simplex, with the metric \(\rho\), is homeomorphic to a Euclidean simplex, hence compact, and affine functions on it are continuous.

*Proof.* (a) The indicator function of \(\{v\}\) and its negative are \(1\)-Lipschitz, since \(d(v,w)\ge1\) for \(w\ne v\).
(b) Symmetry follows by replacing \(\ell\) with \(-\ell\), and the triangle inequality by applying each \(\ell\) to \(p-q=(p-u)+(u-q)\). By (a), \(\rho(p,q)=0\) implies \(p=q\). Graph automorphisms preserve \(d\), so \(\ell\mapsto\ell\circ h^{-1}\) permutes the \(1\)-Lipschitz functions.
(c) Put \(\|x\|=\frac1{\sqrt n}\max_{\ell\in\mathcal P_V}\sum_v\ell(v)x(v)\) for \(x\) with zero sum. It is subadditive and absolutely homogeneous (\(\mathcal P_V=-\mathcal P_V\)), and positive for \(x\ne0\) by the argument of (a). A norm on a finite-dimensional space is bounded above by a multiple of the Euclidean norm (the identity map is a bounded linear map, [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20): Lebl, *Basic Analysis II*, Proposition 8.2.4), so it is continuous; its minimum on the compact Euclidean unit sphere is positive, which gives the bound below. So the topology is the Euclidean one. \(\square\)

For \(c\in|K|\) and \(s\ge0\) write
\[
\begin{gathered}
f_c(p)=\rho(c,p),\\
\begin{aligned}
U_s(c)&=\{p:\ f_c(p)<s\},\\
L_s(c)&=\{p:\ f_c(p)\le s\},\\
S_s(c)&=\{p:\ f_c(p)=s\}.
\end{aligned}
\end{gathered}
\]
The function \(f_c\) is \(1\)-Lipschitz for \(\rho\), hence continuous.

A *polyhedron* in \(\mathbb R^N\) is a set \(P=\{x:\ a_k\cdot x\le b_k\ (k\in I),\ Ax=c\}\) with \(I\) finite. A point \(x\in P\) is a *vertex* of \(P\) if the vectors \(a_k\) with \(a_k\cdot x=b_k\), together with the rows of \(A\), span \(\mathbb R^N\).

**Lemma 2.3.** A bounded nonempty polyhedron has finitely many vertices, and every linear functional attains its maximum over it at a vertex.

*Proof.* A vertex is the unique solution of the linear system formed by its tight inequalities, as equations, and \(Ax=c\); there are finitely many such systems. The polyhedron \(P\) is compact, so a linear functional \(L\) attains its maximum. Among the maximizers choose \(x\) with the largest number of tight inequalities. If \(x\) is not a vertex, choose \(\delta\ne0\) with \(a_k\cdot\delta=0\) for the tight \(k\) and \(A\delta=0\). Then \(x+t\delta\in P\) for small \(|t|\), so \(L\cdot\delta=0\) by maximality. Since \(P\) is bounded, \(t^*=\sup\{t\ge0:x+t\delta\in P\}\) is finite; at \(x+t^*\delta\in P\) the previously tight inequalities stay tight, \(L\) is still maximal, and at least one more inequality is tight. This contradicts the choice of \(x\). \(\square\)

**Lemma 2.4** (branches). Let \(\sigma\) be a closed simplex and \(c\in|K|\), and put \(V=V(\sigma)\cup\operatorname{supp}c\). For each vertex \(\ell\) of \(\mathcal P_V\) define the affine function
\[
b_\ell(p)=\frac1{\sqrt n}\sum_{v\in V}\ell(v)\bigl(c(v)-p(v)\bigr)
\]
on the affine span of \(\sigma\). Then \(f_c=\max_\ell b_\ell\) on \(\sigma\). For \(h\in H\), the functions attached to \((h\sigma,hc)\) are the functions \(p\mapsto b_\ell(h^{-1}p)\) attached to \((\sigma,c)\).

*Proof.* By Lemma 2.1(c) and Lemma 2.3, for \(p\in\sigma\) the maximum defining \(\sqrt n\,\rho(c,p)\) is attained at a vertex of \(\mathcal P_V\). The map \(\ell\mapsto\ell\circ h^{-1}\) is a bijection \(\mathcal P_V\to\mathcal P_{hV}\) preserving the defining constraints, hence vertices. \(\square\)

We call the \(b_\ell\) the *branches* of \(f_c\) on \(\sigma\). They depend on \((\sigma,c)\) and are permuted by \(H\).

## 3. Local finiteness

**Lemma 3.1** (support distance). For \(c,p\in|K|\),
\[
\begin{aligned}
&\min_{a\in\operatorname{supp}c,\ v\in\operatorname{supp}p}d(a,v)\\
&\quad\le\sum_vp(v)\,d(v,\operatorname{supp}c)\\
&\quad\le\sqrt n\,\rho(c,p).
\end{aligned}
\tag{3.1}
\]

*Proof.* The function \(\ell=-d(\,\cdot\,,\operatorname{supp}c)\) is \(1\)-Lipschitz and vanishes on \(\operatorname{supp}c\), so \(\sum_v\ell(v)(c(v)-p(v))\) equals \(\sum_vp(v)d(v,\operatorname{supp}c)\). The first inequality holds because \(p\) is a probability vector. \(\square\)

For \(A\subseteq Y\) and an integer \(k\ge0\) write \(B_k(A)=\{v:\ d(v,A)\le k\}\).

**Lemma 3.2** ([OpenAI-BT, Lemma 3.1]). (a) If a top simplex meets \(L_s(c)\), all its vertices lie in \(B_{\lfloor s\sqrt n\rfloor+n}(\operatorname{supp}c)\), a finite set. So every closed ball meets only finitely many simplices, and it is compact.
(b) Every vertex lies in finitely many simplices.
(c) For \(c\in|K|\), \(s\ge0\) and a simplex \(\kappa\), only finitely many \(h\in H\) satisfy \(L_s(hc)\cap\kappa\ne\varnothing\).
(d) The stabilizer \(H_\kappa=\{h:h\kappa=\kappa\}\) of a simplex has at most \(|V(\kappa)|\) elements.
(e) For \(c\in|K|\) and \(s\ge0\), only finitely many \(h\in H\) satisfy \(L_s(hc)\cap L_s(c)\ne\varnothing\).

*Proof.* (a) If \(p\in\sigma\cap L_s(c)\), then (3.1) gives a vertex of \(\sigma\) at distance at most \(\lfloor s\sqrt n\rfloor\) from \(\operatorname{supp}c\), distances being integers. The \(n+1\) vertices of \(\sigma\) span a connected subgraph, so every vertex of \(\sigma\) is joined to that one by a path of at most \(n\) edges. A ball of finite radius in a graph of bounded degree is finite. Every simplex is a face of a top simplex, so finitely many simplices meet the ball. A closed ball is closed, and contained in the finite union of the closed simplices it meets, each compact by Lemma 2.2(c); so it is compact.
(b) A top simplex containing \(v\) has all its vertices in \(B_n(\{v\})\).
(c) If \(L_s(hc)\) meets \(\kappa\), (3.1) gives \(a\in\operatorname{supp}c\) and \(w\in V(\kappa)\) with \(d(ha,w)\le s\sqrt n\). For each of the finitely many pairs \((a,w)\), the point \(ha\) lies in a finite ball, and \(h\mapsto ha\) is injective because the action is free.
(d) Fix \(v\in V(\kappa)\); \(h\mapsto hv\) is injective and maps \(H_\kappa\) into \(V(\kappa)\).
(e) A common point gives \(\rho(hc,c)\le2s\), and (3.1) gives \(a,a'\in\operatorname{supp}c\) with \(d(ha,a')\le2s\sqrt n\); conclude as in (c). \(\square\)

## 4. Tree Euclidean structures

Fix a top simplex \(\sigma\) and a spanning tree \(T\) of the subgraph spanned by \(V(\sigma)\); it has \(n\) edges. The vectors \(\varepsilon_v-\varepsilon_w\) for the edges \(\{v,w\}\) of \(T\), with either orientation, form a basis of the space of vectors supported in \(V(\sigma)\) with zero sum. The *tree Euclidean structure* is the inner product on this space for which these vectors are orthonormal; it gives the affine span of \(\sigma\) a Euclidean geometry. For a convex polytope \(F\subseteq\sigma\), the set \(F\cap\sigma^\circ\) is the union of the relatively open faces of \(F\) that lie in \(\sigma^\circ\): a coordinate \(p(v)\) is an affine function, nonnegative on \(\sigma\), and if it vanishes at one point of a relatively open face it vanishes on the whole face. A *polyhedral set of dimension at most \(j\)* in \(\sigma^\circ\) is a finite union \(Z\) of such sets with \(\dim F\le j\). For \(0\le j\le n\), its *\(j\)-area* is the sum of the \(j\)-dimensional volumes of the \(j\)-dimensional pieces of a decomposition of \(Z\) into finitely many disjoint relatively open convex polytopes, measured in orthonormal coordinates of their affine spans; pieces of lower dimension contribute \(0\), and for \(j=0\) the area is the number of points. Volumes do not depend on the orthonormal coordinates or on the decomposition, by the change of variables theorem for orthogonal maps and additivity of Jordan content ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20): Lebl, *Basic Analysis II*, Theorem 10.7.2 and Propositions 10.5.1, 10.5.7). Let \(a_j^\sigma(Z)\) be the average of the \(j\)-areas over all spanning trees \(T\). An element \(h\in H\) maps spanning trees of \(V(\sigma)\) to spanning trees of \(V(h\sigma)\), so
\[
a_j^{h\sigma}(hZ)=a_j^\sigma(Z).
\tag{4.1}
\]

**Lemma 4.1** ([OpenAI-BT, Lemma 3.2]). In every tree Euclidean structure on a top simplex \(\sigma\), the \(n\)-volume of \(\sigma\) is \(1/n!\). Every branch of every \(f_c\) on \(\sigma\) has gradient of norm at most \(1\), and so does its restriction to any affine subspace of the span of \(\sigma\).

*Proof.* Root \(T\) at a vertex \(v_0\), number the other vertices \(v_1,\ldots,v_n\) so that each parent precedes its children, and put \(t_i=\varepsilon_{v_i}-\varepsilon_{\mathrm{parent}(v_i)}\) and \(e_i=\varepsilon_{v_i}-\varepsilon_{v_0}\). Each \(e_i\) is the sum of the \(t_j\) along the path from \(v_0\) to \(v_i\), so the matrix expressing the \(e_i\) in the orthonormal basis \(t_j\) is triangular with ones on the diagonal and has determinant \(1\). The simplex \(\sigma\) is \(\varepsilon_{v_0}\) plus the image of the standard simplex \(\{x_i\ge0,\ \sum x_i\le1\}\) under \(x\mapsto\sum x_ie_i\). The standard simplex has volume \(1/n!\) (by Fubini's theorem and induction on \(n\)), and a linear map multiplies volumes by the absolute value of its determinant ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20): Lebl, Theorem 10.2.3 and Theorem 10.7.2). So the volume is \(1/n!\).

A branch is \(b_\ell(p)=\frac1{\sqrt n}\sum_v\ell(v)(c(v)-p(v))\) with \(\ell\) the restriction of a \(1\)-Lipschitz function. Its derivative in the direction \(t_i\) is \(\frac1{\sqrt n}\bigl(\ell(\mathrm{parent}(v_i))-\ell(v_i)\bigr)\), of absolute value at most \(1/\sqrt n\), since tree edges are graph edges. In the orthonormal basis \(t_1,\ldots,t_n\), the squared norm of the gradient is the sum of the \(n\) squared derivatives, at most \(1\). On an affine subspace the gradient is the orthogonal projection of the full gradient, whose norm is no larger. \(\square\)

The Euclidean structures of different top simplices need not agree on common faces. They are used only inside the relative interiors of top simplices.

## 5. The volume margin in high dimension

Fix
\[
R=4D^2,\qquad r=R/2 .
\]

**Lemma 5.1.** A vertex \(v\) of the graph lies in at most \(D^{2n}\) connected sets of \(n+1\) vertices.

*Proof.* For each such set choose a spanning tree rooted at \(v\). Traversing it so that every tree edge is used once in each direction gives a walk of length \(2n\) starting at \(v\) whose set of visited vertices is the given set. Different sets give different walks, and there are at most \(D^{2n}\) walks of length \(2n\) from \(v\). \(\square\)

**Proposition 5.2** (volume bound). For every \(c\in|K|\),
\[
\begin{aligned}
&\sum_{\sigma\ \mathrm{top}}a_n^\sigma\bigl(L_R(c)\cap\sigma^\circ\bigr)\\
&\quad\le V_R=\frac{(n+1)\,D^{\lfloor R\sqrt n\rfloor+1}\,D^{2n}}{n!}.
\end{aligned}
\]

*Proof.* Put \(k=\lfloor R\sqrt n\rfloor\). The ball \(B_k(\{a\})\) has at most \(\sum_{j=0}^kD^j\le D^{k+1}\) vertices, since \(D\ge2\), so \(B_k(\operatorname{supp}c)\) has at most \((n+1)D^{k+1}\) vertices. By (3.1), every top simplex meeting \(L_R(c)\) has a vertex in this set, and by Lemma 5.1 each vertex lies in at most \(D^{2n}\) top simplices, since their vertex sets are connected. Each top simplex contributes at most its full area \(1/n!\) (Lemma 4.1). \(\square\)

The later lessons compare \(V_R\) with \((R-r)^n/n!\). The ratio is
\[
\frac{V_R}{(R-r)^n/n!}=\frac{(n+1)\,D^{\lfloor4D^2\sqrt n\rfloor+1}}{2^n},
\]
since \((R-r)^n=(2D^2)^n=2^nD^{2n}\). Its base-two logarithm is \(-n+4D^2\log_2(D)\sqrt n+O_D(\log n)\), so the ratio tends to \(0\) as \(n\to\infty\) with \(D\) fixed. Choose \(n_0(D)\ge1\) such that for all \(n\ge n_0(D)\)
\[
V_R<\frac{(R-r)^n}{n!}.
\tag{5.2}
\]
Since \(\lfloor x\rfloor\le x\), the inequality holds when the function
\[
\begin{aligned}
f(n)=n&-\log_2(n+1)\\
&-(4D^2\sqrt n+1)\log_2D
\end{aligned}
\]
is positive, and \(f\) is increasing for \(n\ge(4D^2\log_2D)^2\). An exact computation gives the admissible values

| \(D\) | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| \(n_0(D)\) | 274 | 3283 | 16416 | 53950 | 138598 |

These values serve the proof; they are not claimed to be optimal. From here on fix \(n\ge n_0(D)\). The degree bound \(D\), and with it \(R\) and \(r\), stays fixed as the dimension grows; the strict margin (5.2) is the only place where the dimension enters the cutting argument.

## 6. Exercises

**6.1** (easy). For vertices \(v\), \(w\) of \(K\), show that \(\rho(\varepsilon_v,\varepsilon_w)=d(v,w)/\sqrt n\), where \(\varepsilon_v\) is the point of \(|K|\) supported at \(v\).

**6.2** (easy). Let \(V=\{v,w\}\) with \(d(v,w)=1\). Find \(\mathcal P_V\) and its vertices.

**6.3** (easy). Show that the grid \(\mathbb Z^2\), with \(D=4\), has exactly \(4\) connected sets of two vertices and \(18\) connected sets of three vertices containing a given vertex. Compare with \(D^{2n}\).

**6.4** (medium). Let \(n=1\), let \(\sigma=\{v,w\}\) be an edge of \(K\) and \(c=\varepsilon_v\). Compute \(f_c\) on \(\sigma\) and its branches.

**6.5** (medium). Show that the function \(f\) of Section 5 is increasing for \(n\ge(4D^2\log_2D)^2\).

## 7. Solutions

**6.1.** Take \(V=\{v,w\}\). For a \(1\)-Lipschitz \(\ell\), \(\ell(v)-\ell(w)\le d(v,w)\), with equality for \(\ell=d(\,\cdot\,,w)\). So the supremum in (2.1) is \(d(v,w)\).

**6.2.** \(\mathcal P_V=\{(t,-t):\ |2t|\le1\}\), a segment with vertices \(\pm(\tfrac12,-\tfrac12)\).

**6.3.** The two-element sets are \(\{x,x\pm\epsilon_i\}\), four of them. A connected three-element set containing \(x\) is a path of three vertices or an L-shape: \(6\) straight or bent paths with \(x\) in the middle, and \(12\) with \(x\) at an end (\(4\) choices of the first step times \(3\) choices of the second step away from \(x\)); \(6+12=18\). The bounds are \(16\) and \(256\).

**6.4.** The vertices \(v\), \(w\) are adjacent, since \(\sigma\) is a top simplex with connected vertex set, and \(V=\{v,w\}\). For \(p=(1-s)\varepsilon_v+s\varepsilon_w\) with \(0\le s\le1\), \(c-p\) takes the value \(s\) at \(v\) and \(-s\) at \(w\). For the vertex \(\ell=(t,-t)\) of \(\mathcal P_V\), with \(t=\pm\tfrac12\) by Exercise 6.2, the branch is \(b_\ell(p)=ts+(-t)(-s)=2ts\), so the branches are \(s\) and \(-s\), and \(f_c(p)=\max(s,-s)=s\).

**6.5.** \(f'(n)=1-\frac1{(n+1)\ln2}-\frac{2D^2\log_2D}{\sqrt n}\). For \(n\ge(4D^2\log_2D)^2\) the last term is at most \(\tfrac12\), and \(\frac1{(n+1)\ln2}<\tfrac12\) since \(n\ge16\). So \(f'>0\).

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Section 3, Lemmas 3.1 and 3.2. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
