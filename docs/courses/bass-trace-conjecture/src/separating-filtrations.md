# Separating filtrations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Keep the setting of [A transport metric with small balls](a-transport-metric-with-small-balls.md): the graph \(Y\) of degree at most \(D\), the group \(H\) acting freely, the complex \(K\) with top dimension \(n\ge n_0(D)\), the metric \(\rho\) on \(|K|\) and the radii \(r=2D^2<R=4D^2\). This lesson cuts \(|K|\) repeatedly into pieces of diameter at most \(2R\), lowering the dimension of the cut at each step, until a set of isolated points remains. The cuts must be invariant under \(H\), but translates of a local cut may overlap, and \(H\) need not be amenable. Following Braun and Sauer, the cuts are allowed to depend on a point of a compact space on which \(H\) acts freely; the overlapping translates can then be separated in the product of the parameter space with \(|K|\). The lesson follows [OpenAI-BT, Section 4].

- A free parameter space (Section 1).
- Triangulations and polytopal cells (Section 2).
- Admissible filtrations (Section 3).
- Compatible cuts (Section 4).
- Existence and the zero-dimensional stratum (Section 5).

## 1. A free parameter space

A subset of a topological space is *clopen* if it is both open and closed. A function on a space \(X\) is *locally constant* if it is constant on the pieces of a finite partition of \(X\) into clopen sets.

**Lemma 1.1** ([OpenAI-BT, Lemma 4.1]; compare [Braun–Sauer, Section 2]). Every countable group \(H\) acts by homeomorphisms on a compact Hausdorff space \(X\) with the following properties: the clopen sets form a basis of the topology; no element \(h\ne1\) fixes a point of \(X\); and there is a function \(\mu\) from the clopen sets to \([0,1]\) with \(\mu(X)=1\), \(\mu(A\cup B)=\mu(A)+\mu(B)\) for disjoint clopen \(A\), \(B\), and \(\mu(hA)=\mu(A)\).

*Proof.* If \(H\) is trivial, take a point. Otherwise, for \(a\in H\setminus\{1\}\) let \(k_a\) be the order of \(a\) if it is finite and \(k_a=2\) otherwise, and let
\[
\begin{aligned}
X_a=\bigl\{&\xi:H\to\mathbb Z/k_a:\\
&\xi(ta)=\xi(t)+1\ \text{for all }t\in H\bigr\}.
\end{aligned}
\]
Choose a representative \(t_C\) of each left coset \(C=t_C\langle a\rangle\). Every element of \(C\) is \(t_Ca^j\), with \(j\) determined modulo \(k_a\) when \(a\) has finite order and determined in \(\mathbb Z\) otherwise. So \(\xi\mapsto(\xi(t_C))_C\) is a bijection from \(X_a\) onto \((\mathbb Z/k_a)^{H/\langle a\rangle}\), with inverse \(\xi(t_Ca^j)=\omega_C+j\); we call \(\omega_C\) the *offsets*. Let \(H\) act by \((h\xi)(t)=\xi(h^{-1}t)\); this preserves the defining rule of \(X_a\). In offsets, \(h\) carries the coset \(C\) to \(hC\), and \(h^{-1}t_{hC}=t_Ca^{i}\) for some \(i=i(h,C)\), so the offset of \(h\xi\) at \(hC\) is \(\omega_C+i(h,C)\): the action permutes the coordinates and adds constants.

Let \(X=\prod_{a\ne1}X_a\), a product of countably many copies of finite discrete sets indexed by pairs \((a,C)\), with the product topology and the coordinatewise action of \(H\). Enumerate the coordinates as \(1,2,\ldots\) and put \(\operatorname{dist}(\xi,\xi')=2^{-k}\), where \(k\) is the first coordinate at which \(\xi\) and \(\xi'\) differ; this metric gives the product topology. Every sequence has a subsequence that is eventually constant in the first coordinate, a further subsequence eventually constant in the second, and so on; the diagonal subsequence converges. So \(X\) is compact ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20): Lebl, *Basic Analysis II*, Theorem 7.4.11), and it is Hausdorff. The *cylinders*, sets defined by prescribing finitely many offsets, are clopen and form a basis. A clopen set is compact and open, hence a finite union of cylinders. Put \(\mu(\text{cylinder})=\prod k_a^{-1}\) over the prescribed coordinates, extend to finite unions of cylinders by refining them to cylinders over a common finite set of coordinates and counting, and note that the result does not depend on the refinement. An element \(h\) maps a cylinder to a cylinder prescribing the same number of coordinates of each kind \(a\), so \(\mu(hA)=\mu(A)\); each \(h\) acts by a homeomorphism.

If \(a\ne1\) and \(\xi\in X\), the \(a\)-coordinate satisfies \((a\xi_a)(1)=\xi_a(a^{-1})=\xi_a(1)-1\ne\xi_a(1)\), since \(k_a\ge2\). So \(a\xi\ne\xi\). \(\square\)

Fix such \((X,\mu)\). For a locally constant function \(f\), constant equal to \(f_i\) on the pieces \(A_i\) of a finite clopen partition, put \(\int_Xf\,d\mu=\sum_if_i\,\mu(A_i)\). Passing to a common refinement shows that this does not depend on the partition. The integral is linear, monotone, and invariant: \(\int_Xf(hx)\,d\mu(x)=\int_Xf\,d\mu\). For a clopen \(B\) write \(\int_Bf\,d\mu=\int_Xf\,1_B\,d\mu\). No other measure theory is used in the course.

**Lemma 1.2.** Let \(F\subseteq H\setminus\{1\}\) be finite. There is a finite partition of \(X\) into clopen sets \(A\) with \(A\cap hA=\varnothing\) for all \(h\in F\).

*Proof.* For \(x\in X\) and \(h\in F\), \(hx\ne x\); choose disjoint clopen sets \(U\ni x\) and \(V\ni hx\) (the clopen sets form a basis of a Hausdorff space), and put \(N_{x,h}=U\cap h^{-1}V\). Then \(hN_{x,h}\subseteq V\) is disjoint from \(N_{x,h}\subseteq U\). The clopen set \(N_x=\bigcap_{h\in F}N_{x,h}\) contains \(x\) and is disjoint from its translates by \(F\). Finitely many \(N_x\) cover the compact space \(X\); the atoms of the finite Boolean algebra they generate form the partition, and each atom lies in some \(N_x\). \(\square\)

## 2. Triangulations and polytopal cells

An *affine simplex* in a closed original simplex \(\sigma\) is the convex hull of affinely independent points of \(\sigma\). A *triangulation* of \(\sigma\) is a finite set of affine simplices in \(\sigma\), closed under taking faces, with union \(\sigma\), such that any two of them meet in a common face (possibly empty). A *triangulation refining \(K\)* is a choice of a triangulation \(T|_\sigma\) of every original simplex \(\sigma\) such that, for every face \(\tau\) of \(\sigma\), \(T|_\tau\) consists of the members of \(T|_\sigma\) contained in \(\tau\). A triangulation \(S\) *refines* \(T\) if every simplex of \(S\) lies in a simplex of \(T\) and every simplex of \(T\) is a union of simplices of \(S\). A *subcomplex* is a subset closed under faces, identified with the union of its simplices.

**Lemma 2.1** (carriers). Let \(S\) refine \(T\) and let \(E\) be a simplex of \(S\). The smallest simplex \(F\) of \(T\) containing \(E\) satisfies \(E^\circ\subseteq F^\circ\), where \({}^\circ\) denotes the relative interior. So every point lies in the relative interior of exactly one simplex of \(T\), its *carrier*, and a subcomplex of \(T\) containing a point contains its carrier.

*Proof.* The intersection of the simplices of \(T\) containing \(E\) is a common face of each, so \(F\) is a simplex of \(T\). The faces of \(F\) are cut out by barycentric coordinates of \(F\), which are affine functions, nonnegative on \(F\). If one of them vanishes at a point of \(E^\circ\), it vanishes on \(E\), being affine and nonnegative on \(E\); then \(E\) lies in a proper face of \(F\), contrary to minimality. The relative interiors of the simplices of a triangulation are disjoint and cover it, which gives the second assertion with \(S=T\), and a subcomplex containing a point of \(F^\circ\) contains \(F\). \(\square\)

A *convex polytope* is a bounded intersection of finitely many closed half-spaces and hyperplanes in an affine space; its *faces* are its intersections with supporting hyperplanes, together with itself. Given a triangulation \(S\) of a closed simplex \(\tau\) and a finite set \(\mathcal B\) of affine functions on the affine span of \(\tau\) and a number \(t\), the *cells* cut out by \((S,\mathcal B,t)\) are the closures of the nonempty sets
\[
\begin{aligned}
&E^\circ\cap\{p:\ \operatorname{sign}(b(p)-t)=s_b\\
&\qquad\qquad\text{for all }b\in\mathcal B\},
\end{aligned}
\]
for \(E\in S\) and sign vectors \(s\in\{-1,0,1\}^{\mathcal B}\). These relatively open sets partition \(\tau\). Each cell is a convex polytope, obtained from \(E\) by the corresponding closed inequalities and equations, and each face of a cell is again a cell: it is obtained by turning some inequalities into equations, and it is the closure of the relatively open set of the face of \(E\) with the corresponding signs. If \(\mathcal B\subseteq\mathcal B'\), every cell for \(\mathcal B\) is a union of cells for \(\mathcal B'\). A closed subset of \(\tau\) defined by conditions on the signs of the numbers \(b(p)-t\) is a union of cells.

**Lemma 2.2** (coning). Let \(C\) be a convex polytope of dimension \(k\ge1\), let \(\partial C\) be the union of its proper faces, and let \(\Sigma\) be a triangulation of \(\partial C\) in which every proper face of \(C\) is a union of simplices. Let \(m\) be the mean of the vertices of \(C\). Then \(\Sigma\), together with \(m\) and the cones \(\operatorname{conv}(\{m\}\cup E)\) over \(E\in\Sigma\), is a triangulation of \(C\).

*Proof.* The point \(m\) lies in the relative interior of \(C\), because it is a convex combination with positive weights of all vertices. Each \(E\in\Sigma\) lies in a proper face of \(C\), contained in a supporting hyperplane that does not contain \(m\), so \(m\) is affinely independent of \(E\) and the cone is a simplex. Every ray from \(m\) inside the affine span of \(C\) leaves \(C\) through exactly one point of \(\partial C\), by convexity; so the cones cover \(C\), and two cones meet in the cone over the common face of their bases, which is a common face. \(\square\)

## 3. Admissible filtrations

A family \(x\mapsto T(x)\), \(x\in X\), of triangulations refining \(K\) is *locally constant* if for every original simplex \(\sigma\) the triangulation \(T(x)|_\sigma\) is constant on the pieces of a finite clopen partition of \(X\) (the partition may depend on \(\sigma\)); it is *equivariant* if \(T(hx)=hT(x)\) for \(h\in H\), where \(h\) acts on \(|K|\) by \((hp)(y)=p(h^{-1}y)\). The same terms apply to families of subcomplexes. Refinements always keep the earlier subcomplexes as subcomplexes.

Begin with \(T_n(x)=K\) and \(Z_n(x)=|K|\). Suppose that for some \(d\) with \(n\ge d\ge1\) the families \(T_n,\ldots,T_d\) and \(Z_n,\ldots,Z_d\) have been chosen, with \(Z_d(x)\) a subcomplex of \(T_d(x)\), and write \(P(x)=Z_d(x)\). An *admissible choice* at stage \(d\) is a locally constant equivariant family \(T_{d-1}\) of triangulations refining \(T_d\), with a locally constant equivariant family \(Z_{d-1}\) of subcomplexes, such that for every \(x\):

1. \(Z_{d-1}(x)\subseteq P(x)\);
2. for every simplex \(F\) of \(T_d(x)\) contained in \(P(x)\), \(\dim\bigl(F\cap Z_{d-1}(x)\bigr)\le\dim F-1\), a negative bound meaning that the intersection is empty;
3. every connected component of \(P(x)\setminus Z_{d-1}(x)\), in the topology of \(\rho\), has \(\rho\)-diameter at most \(2R\).

A *filtration* \((T_j,Z_j)_{j=0}^n\) is *admissible* if every stage is an admissible choice. By induction, \(\dim Z_j(x)\le j\). By condition 2 with \(\dim F=0\), the new separator avoids the vertices of \(T_d(x)\).

The basic move cuts along a level set. For a separator \(Z\subseteq P\), a center \(c\in|K|\) and \(t\in(r,R)\), remove the part of \(Z\) inside the open ball and insert the slice of \(P\):
\[
Z'=\bigl(Z\setminus U_t(c)\bigr)\cup\bigl(P\cap S_t(c)\bigr).
\]
A component of \(P\setminus Z'\) cannot pass between the ball and its exterior without crossing the inserted slice; inside the ball its diameter is at most \(2t\), and outside the ball the old separator remains. The next lemma carries out this move for many centers at once, compatibly with triangulations, translates and the parameter.

## 4. Compatible cuts

**Lemma 4.1** (compatible cuts [OpenAI-BT, Lemma 4.2]). Let \(T\), \(S\) be locally constant equivariant families of triangulations refining \(K\), with \(S\) refining \(T\), and let \(P\subseteq T\) and \(Z\subseteq S\) be locally constant equivariant families of subcomplexes with \(Z\subseteq P\). Let \(\{(c_\alpha,B_\alpha)\}_{\alpha\in A}\) be a countable family of centers \(c_\alpha\in|K|\) and clopen sets \(B_\alpha\subseteq X\), invariant under \(H\) in the sense that \(h\) permutes the pairs \((hc_\alpha,hB_\alpha)\), such that only finitely many of the balls \(L_R(c_\alpha)\) meet any given original simplex. Put
\[
\begin{gathered}
\mathcal U_t(x)=\bigcup_{\alpha:\,x\in B_\alpha}U_t(c_\alpha),\\
\mathcal S_t(x)=\bigcup_{\alpha:\,x\in B_\alpha}S_t(c_\alpha).
\end{gathered}
\]
For all \(t\in(r,R)\) outside a countable set there is a locally constant equivariant family of triangulations refining \(S\) in which
\[
\begin{gathered}
P(x)\cap\mathcal S_t(x)\quad\text{and}\\
\bigl(Z(x)\setminus\mathcal U_t(x)\bigr)\cup{}\\
\bigl(P(x)\cap\mathcal S_t(x)\bigr)
\end{gathered}
\tag{4.1}
\]
are subcomplexes, and \(\dim(F\cap S_t(c_\alpha))\le\dim F-1\) for every simplex \(F\) of \(T(x)\) or \(S(x)\) and every \(\alpha\). Consequently, if \(Z\) satisfies condition 2 of Section 3 relative to \(T\), so do both sets (4.1). If every component of \(P(x)\setminus Z(x)\) has diameter at most \(2R\), so does every component of the complement in \(P(x)\) of the second set.

*Proof.* *Generic levels.* On a closed original simplex \(\sigma\), \(f_c\) is the maximum of its finitely many branches (Lemma 2.4 of [A transport metric with small balls](a-transport-metric-with-small-balls.md)). For a simplex \(F\subseteq\sigma\), the set \(F\cap\{f_c=t\}\) lies in the union of the sets \(F\cap\{b=t\}\) over the branches \(b\). If no branch is constant with value \(t\) on the affine span of \(F\), each \(\{b=t\}\) meets that span in a proper affine subspace or not at all, and \(\dim(F\cap\{f_c=t\})\le\dim F-1\). Each branch constant on the span of \(F\) excludes one value of \(t\). Only finitely many triangulations \(T(x)|_\sigma\), \(S(x)|_\sigma\) occur, by local constancy and compactness of \(X\); there are countably many original simplices and centers. So the excluded values form a countable set. Fix \(t\in(r,R)\) outside it.

*Cells.* For an original simplex \(\tau\) and \(x\in X\), let \(\mathcal B_\tau(x)\) be the set of restrictions to the span of \(\tau\) of all branches of \(f_{c_\alpha}\) on all original simplices \(\sigma\supseteq\tau\), over the finitely many \(\alpha\) with \(x\in B_\alpha\) and \(L_R(c_\alpha)\cap\sigma\ne\varnothing\) (Lemma 3.2(b) of that lesson gives finitely many \(\sigma\)). Let \(\mathcal Q_\tau(x)\) be the cells cut out by \((S(x)|_\tau,\mathcal B_\tau(x),t)\). If \(\tau\subseteq\sigma\), then \(\mathcal B_\sigma(x)\) restricts into \(\mathcal B_\tau(x)\), because cofaces of \(\sigma\) are cofaces of \(\tau\); so every cell of \(\mathcal Q_\sigma(x)\) lying in \(\tau\) is a union of cells of \(\mathcal Q_\tau(x)\). For a center whose ball \(L_R(c_\alpha)\) misses \(\sigma\), \(f_{c_\alpha}>R>t\) on \(\sigma\), so \(U_t(c_\alpha)\) and \(S_t(c_\alpha)\) miss \(\sigma\). Hence \(\sigma\cap\mathcal U_t(x)\) is the union of the relatively open cells on which all branches of some active center are \(<t\), and \(\sigma\cap\mathcal S_t(x)\) is defined by sign conditions as well; the two sets (4.1), intersected with \(\sigma\), are closed and defined by sign conditions and by membership in subcomplexes of \(S(x)\), so they are unions of cells of \(\mathcal Q_\sigma(x)\).

*Triangulation.* Triangulate the original simplices in order of increasing dimension, a vertex being its own triangulation. When \(\sigma\) is reached, \(\partial\sigma\) is triangulated so that each face \(\tau\) is triangulated by a refinement of \(\mathcal Q_\tau(x)\), hence of the cells of \(\mathcal Q_\sigma(x)\) lying in \(\partial\sigma\). Treat the cells of \(\mathcal Q_\sigma(x)\) not contained in \(\partial\sigma\) in order of increasing dimension, and triangulate each by Lemma 2.2, coning the already triangulated boundary from the mean of its vertices; a zero-dimensional cell is its own triangulation. Cells meet in common faces, and the triangulations of common faces agree, so the result is a triangulation of \(\sigma\) restricting to the given one on \(\partial\sigma\). It refines \(S(x)\), and the sets (4.1) are subcomplexes, being unions of cells.

*Equivariance and local constancy.* Each step is canonical: branches, cells, the order of treatment and the mean of the vertices of a cell commute with the affine maps induced by \(H\), by Lemma 2.4 of that lesson and the invariance of the family of centers. This includes elements stabilizing \(\sigma\). The construction on \(\sigma\) uses finitely many data: \(S(x)\) and the activation conditions \(x\in B_\alpha\) on \(\sigma\), its faces and their cofaces, over finitely many centers; on a common refinement of the corresponding finite clopen partitions all of them are constant.

*Dimension and separation.* The first set (4.1) lies in \(\bigcup_\alpha S_t(c_\alpha)\), so it meets every simplex \(F\) of \(T\) or \(S\) in dimension at most \(\dim F-1\). The second set lies in the union of \(Z\) and these level sets, so it satisfies condition 2 whenever \(Z\) does. Let \(C\) be a component of \(P(x)\) minus the second set. If \(C\) meets an active ball \(U_t(c_\alpha)\), the connected set \(f_{c_\alpha}(C)\) contains a value \(<t\) and does not contain \(t\), because \(C\subseteq P(x)\) avoids \(P(x)\cap S_t(c_\alpha)\). So \(f_{c_\alpha}<t\) on \(C\), and \(C\) has diameter at most \(2t<2R\). Otherwise \(C\) avoids all active open balls, so it avoids \(Z(x)\): a point of \(C\cap Z(x)\) outside \(\mathcal U_t(x)\) would lie in the second set. Then \(C\) is a connected subset of \(P(x)\setminus Z(x)\), inside one of its components, of diameter at most \(2R\). \(\square\)

The lemma does not require the active balls to be disjoint. Genericity with respect to \(S\) matters when \(S\) already carries the old separator: the old separator then meets each inserted level set in lower dimension.

## 5. Existence and the zero-dimensional stratum

**Lemma 5.1** ([OpenAI-BT, Lemma 4.3]). For any admissible choices up to stage \(d\), an admissible choice at stage \(d\) exists. Hence admissible filtrations \((T_j,Z_j)_{j=0}^n\) exist.

*Proof.* Each closed original simplex is compact. Choose representatives of the finitely many orbits of original simplices, cover each by finitely many open balls \(U_r(c)\), and take all \(H\)-translates of these centers, each with activation set \(X\). The balls \(U_r(c)\) cover \(|K|\), and by Lemma 3.2(c) of [A transport metric with small balls](a-transport-metric-with-small-balls.md) only finitely many balls \(L_R(c)\) meet a given original simplex. Apply Lemma 4.1 with \(T=S=T_d\) and \(Z=\varnothing\), and a generic \(t\in(r,R)\), and put
\[
Z_{d-1}(x)=Z_d(x)\cap\bigcup_cS_t(c),
\]
the first set (4.1). It is a subcomplex of the new triangulation \(T_{d-1}(x)\) and satisfies conditions 1 and 2. Let \(C\) be a component of \(Z_d(x)\setminus Z_{d-1}(x)\), choose \(p\in C\) and a covering ball \(U_r(c)\ni p\). The connected set \(f_c(C)\) contains a value \(<r<t\) and avoids \(t\), so \(C\subseteq U_t(c)\), of diameter at most \(2t<2R\). \(\square\)

**Lemma 5.2** (iterated dimension drop). Let \((T_j,Z_j)\) be admissible. For every simplex \(F\) of \(T_i(x)\) contained in \(Z_i(x)\) and every \(0\le j\le i\),
\[
\begin{aligned}
&\dim\bigl(F\cap Z_j(x)\bigr)\\
&\quad\le\dim F-(i-j).
\end{aligned}
\tag{5.1}
\]
In particular a proper face of an original simplex meets \(Z_j(x)\) in dimension less than \(j\).

*Proof.* For \(j=i\) there is nothing to prove, and \(j=i-1\) is condition 2. The set \(F\cap Z_{i-1}(x)\) is a subcomplex of the refinement \(T_{i-1}(x)\), each of its simplices \(F'\) lies in \(Z_{i-1}(x)\) and has \(\dim F'\le\dim F-1\), and by induction \(\dim(F'\cap Z_j(x))\le\dim F'-(i-1-j)\). For the last assertion take \(i=n\): an original simplex \(F\) of dimension at most \(n-1\) meets \(Z_j(x)\) in dimension at most \(n-1-(n-j)=j-1\). \(\square\)

**Lemma 5.3** (carriers of the zero-dimensional stratum [OpenAI-BT, Lemma 4.4]). Let \((T_j,Z_j)\) be admissible and \(z\in Z_0(x)\). For every \(i\) there is exactly one \(i\)-simplex \(S_i\) of \(T_i(x)\) contained in \(Z_i(x)\) and containing \(z\), and \(z\) lies in its relative interior. In particular every point of \(Z_0(x)\) lies in the relative interior of a top simplex of \(K\).

*Proof.* Let \(F\) be the carrier of \(z\) in \(T_i(x)\) (Lemma 2.1). The subcomplex \(Z_i(x)\) contains \(z\), hence \(F\), so \(\dim F\le i\). If \(\dim F<i\), (5.1) with \(j=0\) would make \(F\cap Z_0(x)\) empty, although it contains \(z\). So \(F\) is an \(i\)-simplex. Any simplex of \(T_i(x)\) containing \(z\) contains its carrier \(F\) as a face; an \(i\)-simplex in \(Z_i(x)\) with this property equals \(F\), as \(\dim Z_i(x)\le i\). For \(i=n\), \(T_n(x)=K\). \(\square\)

Admissible filtrations exist, and the local move of Lemma 4.1 stays among them. [Near-minimal separators](near-minimal-separators.md) chooses the separators with nearly least area and compares them with these moves.

## 6. Exercises

**6.1** (easy). For \(H=\mathbb Z/2=\{1,a\}\), describe \(X\), the action and \(\mu\) of Lemma 1.1, and check that the action is free.

**6.2** (easy). Show that the integral of a locally constant function does not depend on the clopen partition used to compute it.

**6.3** (medium). Let \(\sigma\) be a closed triangle, \(S\) the triangulation consisting of \(\sigma\) and its faces, and \(\mathcal B=\{b\}\) a single affine function taking the values \(0\), \(1\), \(2\) at the three vertices. List the cells cut out by \((S,\mathcal B,\tfrac12)\) by dimension.

**6.4** (medium). Show that the conditions of Section 3 imply \(\dim Z_j(x)\le j\) for every \(j\).

**6.5** (medium). Let \(Z_0(x)\) be the last stratum of an admissible filtration. Show that \(Z_0(x)\) is discrete: every point of \(Z_0(x)\) has a neighbourhood in \(|K|\) containing no other point of \(Z_0(x)\).

## 7. Solutions

**6.1.** There is one element \(a\ne1\), of order \(k_a=2\), and one coset \(C=H\). So \(X=X_a\) has two points, the functions \(\xi\) with \(\xi(a)=\xi(1)+1\) in \(\mathbb Z/2\), determined by \(\xi(1)\in\{0,1\}\). The element \(a\) maps \(\xi\) to \(\xi(a^{-1}\,\cdot\,)\), which has \(\xi(a^{-1})=\xi(1)+1\) at \(1\): it exchanges the two points. \(\mu\) gives each point mass \(\tfrac12\).

**6.2.** Two partitions have a common refinement into clopen sets \(A_i\cap A'_j\). On each piece of a partition the function value is constant, and \(\mu\) is additive, so both sums equal the sum over the common refinement.

**6.3.** The level \(\{b=\tfrac12\}\) crosses \(\sigma\) along a segment joining a point of the edge \([v_0,v_1]\) and a point of the edge \([v_0,v_2]\). Dimension \(0\): the three vertices and the two endpoints of the segment. Dimension \(1\): the segment, the two pieces of each of the edges \([v_0,v_1]\) and \([v_0,v_2]\), and the edge \([v_1,v_2]\). Dimension \(2\): the small triangle near \(v_0\) where \(b<\tfrac12\), and the quadrilateral where \(b>\tfrac12\).

**6.4.** \(Z_n(x)=|K|\) has dimension \(n\). If \(\dim Z_d(x)\le d\), every simplex \(F\) of \(T_d(x)\) contained in \(Z_d(x)\) has \(\dim F\le d\), so by condition 2 \(\dim(F\cap Z_{d-1}(x))\le d-1\). Since \(Z_{d-1}(x)\subseteq Z_d(x)\) is the union of these intersections, \(\dim Z_{d-1}(x)\le d-1\).

**6.5.** \(Z_0(x)\) is a subcomplex of \(T_0(x)\) of dimension \(0\), a set of vertices of \(T_0(x)\). By Lemma 3.2(a) of [A transport metric with small balls](a-transport-metric-with-small-balls.md), a closed ball meets only finitely many original simplices, and each original simplex has finitely many vertices of \(T_0(x)\). So a small ball around a point of \(Z_0(x)\) contains no other point of \(Z_0(x)\).

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Section 4, Lemmas 4.1–4.4. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
- [Braun–Sauer] S. Braun and R. Sauer, *Volume and macroscopic scalar curvature*, Geometric and Functional Analysis 31 (2021), 1321–1376; arXiv:2012.08999, Section 2. https://arxiv.org/abs/2012.08999
