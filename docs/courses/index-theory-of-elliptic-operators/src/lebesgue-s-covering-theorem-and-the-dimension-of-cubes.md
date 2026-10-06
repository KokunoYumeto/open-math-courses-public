# Lebesgue's covering theorem and the dimension of cubes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lesson Covering dimension and finite trivializing covers proves that every compact subset of \(\mathbb R^n\) has covering dimension at most \(n\). This lesson proves the reverse inequality for simplices and cubes, so that \(\dim[0,1]^n=n\) (Theorem 4.3). The key is a covering property of the simplex, the lemma of Knaster, Kuratowski and Mazurkiewicz (Theorem 2.1), which we derive from Brouwer's fixed-point theorem. Consequences: cubes of different dimensions are not homeomorphic, nor are open subsets of Euclidean spaces of different dimensions (Corollary 5.1), and a compact subset of an \(n\)-manifold with nonempty interior has covering dimension exactly \(n\) (Corollary 5.2).

Covering dimension and the covering property of cubes go back to Lebesgue [Lebesgue 1911; Lebesgue 1921]; the invariance of dimension was first proved by Brouwer [Brouwer 1911]. Theorem 2.1 is due to Knaster, Kuratowski and Mazurkiewicz [KKM 1929, §2], who derived it from Sperner's combinatorial lemma and deduced Brouwer's fixed-point theorem from it; here the implication runs the other way. Theorem 3.1 is obtained from Theorem 2.1 as in [KKM 1929, §4].

We use Brouwer's fixed-point theorem from the core course [Algebraic Topology (D60)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), Lecture 30, Theorem 30.1: every continuous map of the closed unit ball \(D^n\) of \(\mathbb R^n\) to itself has a fixed point. From the lesson on covering dimension we use Definition 2.1, Lemma 1.2, Hemmingsen's characterization (Theorem 2.3), closed subspaces (Corollary 2.4), compact subsets of \(\mathbb R^n\) (Theorem 4.2) and compact subsets of manifolds (Theorem 5.2(1)).

## 1. Fixed points on compact convex sets

Norms and distances in \(\mathbb R^n\) are Euclidean, and \(\langle\cdot,\cdot\rangle\) is the standard inner product.

**Lemma 1.1** (Nearest points). Let \(K\subseteq\mathbb R^n\) be closed, convex and nonempty. Every \(x\in\mathbb R^n\) has exactly one nearest point \(r(x)\) in \(K\), and \(\|r(x)-r(y)\|\le\|x-y\|\) for all \(x,y\in\mathbb R^n\).

**Proof.** *Existence.* Fix \(k_0\in K\). The set \(K\cap\{k:\|x-k\|\le\|x-k_0\|\}\) is closed, bounded and nonempty, hence compact, and the continuous function \(k\mapsto\|x-k\|\) attains its minimum on it. That minimum is the distance from \(x\) to \(K\).

*A variational inequality.* Let \(p\in K\) be a nearest point to \(x\), and \(k\in K\). For \(0<t\le1\) the point \(p+t(k-p)\) lies in \(K\), so
\[
\|x-p\|^2\le\|x-p-t(k-p)\|^2=\|x-p\|^2-2t\langle x-p,k-p\rangle+t^2\|k-p\|^2 .
\]
Dividing by \(t\) and letting \(t\to0\) gives \(\langle x-p,k-p\rangle\le0\).

*Uniqueness and the bound.* Let \(p\) be a nearest point to \(x\) and \(q\) a nearest point to \(y\). The variational inequality gives \(\langle x-p,q-p\rangle\le0\) and \(\langle y-q,p-q\rangle\le0\). Adding,
\[
0\ge\langle (x-p)-(y-q),\,q-p\rangle=\langle x-y,\,q-p\rangle+\|p-q\|^2 ,
\]
so \(\|p-q\|^2\le\langle x-y,p-q\rangle\le\|x-y\|\,\|p-q\|\) and \(\|p-q\|\le\|x-y\|\). For \(y=x\) this shows that the nearest point is unique. \(\square\)

**Corollary 1.2** (Brouwer's theorem for convex sets). Let \(K\subseteq\mathbb R^n\) be compact, convex and nonempty. Every continuous map \(f:K\to K\) has a fixed point.

**Proof.** Choose \(R>0\) with \(\|k\|\le R\) for all \(k\in K\), and let \(r\) be the nearest-point map of Lemma 1.1. The map \(h(u)=R^{-1}f(r(Ru))\) is continuous and sends \(D^n\) into \(R^{-1}K\subseteq D^n\). By Brouwer's fixed-point theorem, \(h(u)=u\) for some \(u\in D^n\). The point \(x=Ru\) satisfies \(x=f(r(x))\in K\); hence \(r(x)=x\) and \(f(x)=x\). \(\square\)

## 2. The lemma of Knaster, Kuratowski and Mazurkiewicz

Let \(v_0,\dots,v_n\in\mathbb R^n\) be affinely independent, that is, \(v_1-v_0,\dots,v_n-v_0\) are linearly independent, and let \(\Delta=\operatorname{conv}\{v_0,\dots,v_n\}\) be their *simplex*. Every \(x\in\Delta\) has unique *barycentric coordinates* \(t_0(x),\dots,t_n(x)\ge0\) with \(\sum_it_i(x)=1\) and \(x=\sum_it_i(x)v_i\). They are restrictions of affine functions on \(\mathbb R^n\): \((t_1,\dots,t_n)\) is the coordinate vector of \(x-v_0\) in the basis \(v_1-v_0,\dots,v_n-v_0\), and \(t_0=1-\sum_{i\ge1}t_i\). So \(\Delta=\{x\in\mathbb R^n:t_i(x)\ge0\text{ for all }i\}\) is closed; it is also bounded and convex, hence compact and convex. For a nonempty \(S\subseteq\{0,\dots,n\}\), the *face* \(\Delta_S=\operatorname{conv}\{v_i:i\in S\}\) consists of the \(x\in\Delta\) with \(t_i(x)=0\) for \(i\notin S\). The *facet opposite \(v_i\)* is \(\Delta^{(i)}=\{x\in\Delta:t_i(x)=0\}\).

**Theorem 2.1** (Knaster–Kuratowski–Mazurkiewicz). Let \(C_0,\dots,C_n\) be closed subsets of \(\Delta\) such that \(\Delta_S\subseteq\bigcup_{i\in S}C_i\) for every nonempty \(S\subseteq\{0,\dots,n\}\). Then \(\bigcap_{i=0}^nC_i\ne\varnothing\).

**Proof.** For \(S=\{i\}\) the hypothesis gives \(v_i\in C_i\), so each \(C_i\) is nonempty, and \(d_i(x)=d(x,C_i)\) is a continuous function on \(\Delta\) that vanishes exactly on \(C_i\). Suppose that the intersection is empty. Then \(s(x)=\sum_id_i(x)>0\) for every \(x\in\Delta\), and
\[
f(x)=\sum_{i=0}^n\frac{d_i(x)}{s(x)}\,v_i
\]
is a continuous map \(\Delta\to\Delta\). By Corollary 1.2 it has a fixed point \(x\). By the uniqueness of barycentric coordinates, \(t_i(x)=d_i(x)/s(x)\) for every \(i\). The set \(S=\{i:t_i(x)>0\}\) is nonempty and \(x\in\Delta_S\). By hypothesis \(x\in C_i\) for some \(i\in S\). Then \(d_i(x)=0\), so \(t_i(x)=0\), against \(i\in S\). \(\square\)

## 3. The covering theorem for simplices

**Theorem 3.1** (Lebesgue's covering theorem). Let \(F_1,\dots,F_k\) be closed subsets of \(\Delta\) that cover \(\Delta\), each disjoint from at least one facet of \(\Delta\). Then some point of \(\Delta\) lies in at least \(n+1\) of the sets \(F_m\).

**Proof.** For each \(m\) choose \(\lambda(m)\in\{0,\dots,n\}\) with \(F_m\cap\Delta^{(\lambda(m))}=\varnothing\), and let \(C_i\) be the union of the \(F_m\) with \(\lambda(m)=i\), a closed set. We check the hypothesis of Theorem 2.1. Let \(S\) be nonempty and \(x\in\Delta_S\), and choose \(m\) with \(x\in F_m\). For \(j\notin S\) the face \(\Delta_S\) lies in the facet \(\Delta^{(j)}\), so \(F_m\) meets \(\Delta^{(j)}\) and \(\lambda(m)\ne j\). Hence \(\lambda(m)\in S\), and \(x\in C_{\lambda(m)}\subseteq\bigcup_{i\in S}C_i\). Theorem 2.1 gives a point \(x\) in every \(C_i\): for each \(i\) there is \(m_i\) with \(\lambda(m_i)=i\) and \(x\in F_{m_i}\). The indices \(m_0,\dots,m_n\) are distinct because their labels are. \(\square\)

**Lemma 3.2** (Small sets miss a facet). Let \(L>0\) be such that \(|t_i(x)-t_i(y)|\le L\|x-y\|\) for all \(i\) and all \(x,y\in\Delta\); such an \(L\) exists because the \(t_i\) are restrictions of affine functions. Every subset of \(\Delta\) with diameter less than \(\varepsilon=1/\bigl((n+1)L\bigr)\) is disjoint from some facet of \(\Delta\). For the simplex with vertices \(0,e_1,\dots,e_n\), \(n\ge1\), one can take \(L=\sqrt n\).

**Proof.** Let \(F\subseteq\Delta\) have diameter less than \(\varepsilon\), and suppose that \(F\) meets every facet: for each \(i\) there is \(y^{(i)}\in F\) with \(t_i(y^{(i)})=0\). Take \(x\in F\). Then \(t_i(x)=t_i(x)-t_i(y^{(i)})\le L\|x-y^{(i)}\|<L\varepsilon\) for every \(i\), and \(1=\sum_it_i(x)<(n+1)L\varepsilon=1\), which is impossible.

For the vertices \(0,e_1,\dots,e_n\), the coordinates are \(t_i(x)=x_i\) for \(i\ge1\) and \(t_0(x)=1-\sum_ix_i\). Then \(|x_i-y_i|\le\|x-y\|\), and \(\bigl|\sum_i(x_i-y_i)\bigr|\le\sqrt n\,\|x-y\|\) by the Cauchy–Schwarz inequality. \(\square\)

## 4. The dimension of simplices and cubes

**Definition 4.1.** Definition 2.1 of the covering-dimension lesson makes sense for \(n=-1\): \(\dim X\le-1\) means that every finite open cover of \(X\) has an open refinement of order at most \(0\), that is, \(X=\varnothing\). A normal space \(X\) has *covering dimension \(n\ge0\)*, written \(\dim X=n\), if \(\dim X\le n\) and not \(\dim X\le n-1\). If \(\dim X\le n\) holds for no \(n\), then \(\dim X=\infty\). Since a cover of order at most \(n+1\) has order at most \(n+2\), \(\dim X\le n\) implies \(\dim X\le n+1\); so \(\dim X\) is well defined, and it is invariant under homeomorphisms.

**Theorem 4.2.** Every \(n\)-simplex \(\Delta\subseteq\mathbb R^n\) has \(\dim\Delta=n\).

**Proof.** \(\Delta\) is compact, so \(\dim\Delta\le n\) by Theorem 4.2 of the covering-dimension lesson. For \(n=0\), \(\Delta\) is a point and not empty. Let \(n\ge1\), and suppose that \(\dim\Delta\le n-1\). Let \(\varepsilon\) be as in Lemma 3.2. The sets \(\{y\in\Delta:\|y-x\|<\varepsilon/3\}\), \(x\in\Delta\), are open in \(\Delta\) and have diameter less than \(\varepsilon\); by compactness finitely many of them, \(U_1,\dots,U_p\), cover \(\Delta\). The compact metric space \(\Delta\) is normal. Hemmingsen's Theorem 2.3 of the covering-dimension lesson, applied with \(n-1\), gives an open shrinking \(\{V_m\}\) of \(\{U_m\}\) of order at most \(n\), and Lemma 1.2(1) there gives closed sets \(F_m\subseteq V_m\) that cover \(\Delta\). The \(F_m\) have order at most \(n\) and diameter less than \(\varepsilon\), so each is disjoint from some facet (Lemma 3.2). Theorem 3.1 gives a point in \(n+1\) of them, a contradiction. \(\square\)

**Theorem 4.3** (Dimension of cubes). For every \(n\ge0\), \(\dim[0,1]^n=n\).

**Proof.** For \(n=0\) the cube is a point. Let \(n\ge1\). The cube is compact, so \(\dim[0,1]^n\le n\). The simplex \(\Delta=\{x:x_i\ge0,\ \sum_ix_i\le1\}\) with vertices \(0,e_1,\dots,e_n\) is closed in \([0,1]^n\), since \(0\le x_i\le\sum_jx_j\le1\) on it. If \(\dim[0,1]^n\le n-1\), then \(\dim\Delta\le n-1\) by Corollary 2.4 of the covering-dimension lesson, against Theorem 4.2. \(\square\)

**Corollary 4.4** (Small closed covers of cubes). Let \(n\ge1\) and \(\varepsilon_n=1/\bigl((n+1)\sqrt n\bigr)\). Every cover of \([0,1]^n\) by finitely many closed sets of diameter less than \(\varepsilon_n\) has a point that lies in at least \(n+1\) of them.

**Proof.** Let \(\Delta\subseteq[0,1]^n\) be the simplex of Theorem 4.3. The sets \(F_m\cap\Delta\) are closed, cover \(\Delta\) and have diameter less than \(\varepsilon_n\), so by Lemma 3.2, with \(L=\sqrt n\), each is disjoint from some facet. Theorem 3.1 gives a point of \(\Delta\) in at least \(n+1\) of them. \(\square\)

## 5. Consequences

**Corollary 5.1** (Invariance of dimension). Let \(m\ne n\). Then \([0,1]^m\) and \([0,1]^n\) are not homeomorphic, and no nonempty open subset of \(\mathbb R^m\) is homeomorphic to an open subset of \(\mathbb R^n\). In particular \(\mathbb R^m\) and \(\mathbb R^n\) are not homeomorphic.

**Proof.** The first statement follows from Theorem 4.3, because the covering dimension is invariant under homeomorphisms. For the second, by symmetry let \(m>n\), and suppose that \(h\) is a homeomorphism from a nonempty open \(U\subseteq\mathbb R^m\) onto an open \(V\subseteq\mathbb R^n\). Then \(U\) contains a cube \(Q=a+[0,s]^m\) with \(s>0\), which is homeomorphic to \([0,1]^m\), so \(\dim Q=m\). Its image \(h(Q)\) is compact in \(\mathbb R^n\), so \(\dim h(Q)\le n<m\) by Theorem 4.2 of the covering-dimension lesson; but \(h(Q)\) is homeomorphic to \(Q\). \(\square\)

**Corollary 5.2** (Compact subsets of manifolds). Let \(M\) be a manifold of dimension \(n\) and \(C\subseteq M\) compact. Then \(\dim C\le n\), and \(\dim C=n\) if \(C\) has nonempty interior. In particular a nonempty compact manifold of dimension \(n\) has covering dimension \(n\).

**Proof.** The bound \(\dim C\le n\) is Theorem 5.2(1) of the covering-dimension lesson. Let \(x\) be an interior point of \(C\) and \(\varphi:W\to\varphi(W)\) a chart with \(x\in W\); replacing \(W\) by \(W\cap\operatorname{int}C\), we may assume \(W\subseteq C\). The open set \(\varphi(W)\subseteq\mathbb R^n\) contains a cube \(Q=a+[0,s]^n\) with \(s>0\). The set \(\varphi^{-1}(Q)\) is compact, hence closed in \(C\), and homeomorphic to \(Q\), so \(\dim\varphi^{-1}(Q)=n\) by Theorem 4.3. If \(\dim C\le n-1\), Corollary 2.4 of the covering-dimension lesson would give \(\dim\varphi^{-1}(Q)\le n-1\). So \(\dim C=n\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Prove Theorem 2.1 for \(n=1\) directly: if \([v_0,v_1]=C_0\cup C_1\) with \(C_0,C_1\) closed, \(v_0\in C_0\) and \(v_1\in C_1\), then \(C_0\cap C_1\ne\varnothing\).

*Solution.* A segment is connected, and two disjoint nonempty closed sets cannot cover a connected space.

**Exercise 6.2.** For \(i=0,\dots,n\) let \(F_i=\{x\in\Delta:t_i(x)=\max_jt_j(x)\}\). Show that the \(F_i\) are closed and cover \(\Delta\), that \(F_i\) is disjoint from the facet \(\Delta^{(i)}\), and that exactly one point lies in all of them. So the number \(n+1\) in Theorem 3.1 cannot be raised, and the point it provides can be unique.

*Solution.* The \(F_i\) are closed because the \(t_j\) are continuous, and every point has a largest coordinate. On \(\Delta^{(i)}\), \(t_i=0\); if \(t_i\) were the largest coordinate there, all coordinates would vanish, against \(\sum_jt_j=1\). A point lies in every \(F_i\) exactly when all its coordinates are equal, that is, when they all equal \(1/(n+1)\): the barycentre.

**Exercise 6.3.** Show that the circle \(S^1=\{x\in\mathbb R^2:\|x\|=1\}\) has \(\dim S^1=1\).

*Solution.* The closed half circles \(\{x\in S^1:x_2\ge0\}\) and \(\{x\in S^1:x_2\le0\}\) are homeomorphic to \([-1,1]\) by \(x\mapsto x_1\), hence to \([0,1]\), so they have dimension \(1\) by Theorem 4.3. The finite sum theorem (Theorem 3.2 of the covering-dimension lesson) gives \(\dim S^1\le1\), and Corollary 2.4 there, applied to a half circle, excludes \(\dim S^1\le0\).

**Exercise 6.4.** Show that there is no continuous injective map \([0,1]^2\to\mathbb R\).

*Solution.* A continuous injective map from a compact space to a Hausdorff space is a homeomorphism onto its image, which here is a compact subset of \(\mathbb R\) and so has dimension at most \(1\) (Theorem 4.2 of the covering-dimension lesson). By Theorem 4.3, \(\dim[0,1]^2=2\).

## Where this leads

Together with the covering-dimension lesson, this lesson shows that the covering dimension of cubes, simplices and compact manifolds is the expected number. Dimension theory develops much further, for instance to separable metric spaces and to the comparison of covering dimension with inductive dimensions.

## References

- [Brouwer 1911] L. E. J. Brouwer, Beweis der Invarianz der Dimensionenzahl, *Mathematische Annalen* 70 (1911), 161–165, [doi:10.1007/BF01461154](https://doi.org/10.1007/BF01461154); free scan at the [Göttingen digitization centre](https://resolver.sub.uni-goettingen.de/purl?GDZPPN00226370X).
- [KKM 1929] B. Knaster, C. Kuratowski and S. Mazurkiewicz, Ein Beweis des Fixpunktsatzes für \(n\)-dimensionale Simplexe, *Fundamenta Mathematicae* 14 (1929), 132–137, [doi:10.4064/fm-14-1-132-137](https://doi.org/10.4064/fm-14-1-132-137) (free at the publisher).
- [Lebesgue 1911] H. Lebesgue, Sur la non-applicabilité de deux domaines appartenant respectivement à des espaces à \(n\) et \(n+p\) dimensions, *Mathematische Annalen* 70 (1911), 166–168; free scan at the [Göttingen digitization centre](https://resolver.sub.uni-goettingen.de/purl?GDZPPN002263718).
- [Lebesgue 1921] H. Lebesgue, Sur les correspondances entre les points de deux espaces, *Fundamenta Mathematicae* 2 (1921), 256–285, [doi:10.4064/fm-2-1-256-285](https://doi.org/10.4064/fm-2-1-256-285) (free at the publisher).
