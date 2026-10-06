# Cylindrical wedges and support

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Convexity of every characteristic hyperplane section is a sufficient geometric condition for global smooth solvability. In higher dimensions, the exterior geometry is a planar angle extended along a subspace of codimension two. The resulting wedge contains whole lines. We therefore prove its continuation property directly between convex open sets rather than treating it as a pointed cone.

Basic references are Kalmes's papers on support geometry and Grubb's distribution lectures, listed below. We use the exterior-angle lemma proved in [Planar domains and directional solvability](planar-domains-and-directional-solvability.md), Lemma 2.1, and the general analytic theorem stated under [Convex continuation](lorentz-cones-and-domain-solvability.md#convex-continuation). Its polynomial \(R\) can be any nonzero complex constant-coefficient polynomial, of any degree. The Lorentz lesson subsequently specializes it to a wave operator; here we use the general statement with \(R(\xi)=P(-\xi)\).

Let \(P\ne0\) be a complex constant-coefficient polynomial on \(\mathbb R^n\), \(D=-i\partial\), with principal homogeneous part \(P_m\). A hyperplane is characteristic when its real nonzero normal \(N\) satisfies \(P_m(N)=0\). Lower order coefficients may be complex.

## The sufficient slice condition

**Theorem 1.1.** Suppose \(X\subset\mathbb R^n\) is open and \(X\cap\pi\) is convex or empty for every affine characteristic hyperplane \(\pi\). Then \(X\) is \(P\)-convex for supports. Consequently \(P(D)\) maps \(C^\infty(X)\) onto \(C^\infty(X)\).

The final implication is the global solvability theorem in [Approximation and global solvability from support geometry](approximation-and-global-support-solvability.md). We will prove the support statement itself.

If \(P\) is elliptic, every open set is support convex, by the ellipticity theorem in the boundary-distance lesson. This includes nonzero constant polynomials and the one-dimensional case. We may therefore assume \(n\geq2\) and that there is a nonzero real characteristic normal.

We may also prove the theorem one connected component at a time. Indeed a nonempty convex hyperplane section is connected and must lie in one component of \(X\); hence the same slice hypothesis holds on each component. Support convexity is componentwise, as proved in the planar lesson. For the following construction assume that \(X\) is nonempty and connected.

## Finding an exterior affine subspace

We first record the elementary separation fact in the exact form needed here.

**Lemma 2.1.** If \(C\) is a nonempty open convex subset of a finite dimensional real inner-product space and \(0\notin C\), there is a nonzero vector \(M\) with \(M\cdot x>0\) for every \(x\in C\).

**Specialization of the separation theorem.** The [supporting-covector lemma](../prerequisites/prerequisite-bridges.html#strict-separation-of-an-open-convex-set) proves that, for any \(q\notin C\), there is a nonzero real covector \(\eta\) with \(\eta(x)<\eta(q)\) on \(C\), including when \(q\) is a boundary point. Apply it at \(q=0\), and use the inner product to represent \(-\eta\) by \(M\). This gives exactly \(M\cdot x>0\). The published proof handles unbounded \(C\) by nearest points and compactness of unit covectors; no compactness of \(C\) is assumed.

Fix \(q\notin X\), and translate it to zero. We will find orthogonal complementary subspaces
\[
\begin{gathered}
\mathbb R^n=E\oplus L,\\
\dim E=2,\quad \dim L=n-2.
\end{gathered}
\tag{1}
\]
such that
\[
L\cap X=\varnothing,\qquad P_m|_E\not\equiv0,
\tag{2}
\]
and \(P_m|_E\) has a real nonzero zero.

Choose a characteristic normal \(N\), and put \(\pi=N^\perp\).

If \(X\cap\pi\) is empty, choose a real vector \(M\) with \(P_m(M)\ne0\). Such a vector exists, because a nonzero polynomial cannot vanish on all of real space. It cannot be parallel to \(N\). Take \(E=\operatorname{span}(N,M)\) and \(L=E^\perp\). Then \(L\subset\pi\) avoids \(X\), while \(P_m|_E\) is nonzero and vanishes at \(N\).

Suppose instead that \(C=X\cap\pi\) is nonempty. It is relatively open and convex in \(\pi\), and does not contain zero. Lemma 2.1 in the vector space \(\pi\) gives a nonzero \(M\in\pi\) with
\[
M\cdot x>0\quad\text{for all }x\in C.
\tag{3}
\]
The strict inequality also holds when zero is on the relative boundary of the slice; Lemma 2.1 included that case.

Set \(E=\operatorname{span}(N,M)\), \(L=E^\perp\). Then \(L\cap X=\varnothing\), by (3). If \(P_m|_E\not\equiv0\), we have obtained (2).

There remains a real possibility: the restriction could vanish identically on this entire two dimensional plane. To repair it, let \(\operatorname{pr}_E\) be orthogonal projection and set
\[
Y=\operatorname{pr}_E X.
\tag{4}
\]
It is open, nonempty and connected; projection of a Euclidean open set is open, and continuous images preserve connectedness. Also \(0\notin Y\), because the fiber at zero is \(L\), which avoids \(X\).

If \(P_m|_E\equiv0\), every affine line in \(E\) lifts to a characteristic hyperplane in \(\mathbb R^n\). Its intersection with \(Y\) is the projection of the corresponding convex section of \(X\), hence an interval or the empty set. It follows that \(Y\) is convex: any two of its points lie on a line, and the interval property includes their segment.

Separate zero from this open convex \(Y\). There is a nonzero \(M_0\in E\) with \(M_0\cdot y>0\) for every \(y\in Y\). Thus
\[
M_0\cdot x>0\text{ on }X,\qquad P_m(M_0)=0.
\tag{5}
\]
Choose again a real \(N_0\) with \(P_m(N_0)\ne0\), and replace our spaces by
\[
E_0=\operatorname{span}(M_0,N_0),\qquad L_0=E_0^\perp.
\tag{6}
\]
The first inequality in (5) makes \(L_0\) exterior to \(X\). The restriction to \(E_0\) is nonzero and has the characteristic vector \(M_0\). This completes the construction in every case.

## Projecting the characteristic geometry

Use the spaces now satisfying (2), and keep the notation \(Y=\operatorname{pr}_E X\). The restriction \(p=P_m|_E\) is a nonzero homogeneous polynomial on a two dimensional plane, with at least one real characteristic direction. It has only finitely many projective real zero directions, by one-variable polynomial root finiteness in the two projective coordinate charts.

For each such normal \(N\in E\), any line \(\ell\subset E\) normal to \(N\) has inverse image
\[
\operatorname{pr}_E^{-1}\ell=\ell+L,
\tag{7}
\]
a characteristic affine hyperplane. Therefore
\[
Y\cap\ell=\operatorname{pr}_E\bigl(X\cap(\ell+L)\bigr)
\tag{8}
\]
is an interval or empty, by the slice hypothesis. The planar exterior-angle lemma now gives a closed pointed angle \(B\subset E\setminus Y\), with vertex zero and aperture less than \(\pi\), containing a nonzero half-ray of every characteristic line of \(p\). A single half-ray is allowed when the angle degenerates.

The cylindrical wedge
\[
A=B+L
\tag{9}
\]
lies outside \(X\). Every characteristic hyperplane through zero has a ray in an arbitrarily small planar enlargement of this wedge. To see the two kinds of normal separately, take an open pointed planar angle \(\Gamma_E\) containing \(B\setminus\{0\}\), and put
\[
\Gamma=\Gamma_E+L.
\tag{10}
\]
If the characteristic normal \(N\) lies in \(E\), its orthogonal line in \(E\) has a nonzero ray in \(B\), hence in \(\Gamma_E\). If \(N\notin E\), its restriction to \(L\) is nonzero. For any \(e\in\Gamma_E\), solve \(N\cdot l=-N\cdot e\) with \(l\in L\). Then \(e+l\) is a nonzero vector of \(\Gamma\cap N^\perp\). This is the role of the directions along the edge \(L\).

## Continuation in a wedge with an edge

**Lemma 4.1.** Let \(E,L,B,\Gamma_E\) have the properties above, with the enlargement still of aperture less than \(\pi\). If \(P^tu=0\) in \(\Gamma=\Gamma_E+L\), and \(u\) vanishes there outside a bounded set, then \(u=0\) throughout \(\Gamma\).

**Proof.** Choose a linear form \(\lambda\) on \(E\) strictly positive on all nonzero points of \(\overline{\Gamma_E}\). Such a form exists because that closed angle has aperture less than \(\pi\); its middle ray can be used as the Euclidean normal. Extend \(\lambda\) to vanish on \(L\). For sufficiently large \(T>0\), the convex nonempty open set
\[
U_T=\{x\in\Gamma:\lambda(x)>T\}
\tag{11}
\]
lies outside the bounded support portion, so \(u=0\) there.

Let a characteristic affine hyperplane meet \(\Gamma\) at \(x\), and denote its normal by \(N\). The argument after (10) gives a vector \(v\in\Gamma\cap N^\perp\), with its \(E\)-component in \(\Gamma_E\). For all \(s\geq0\), \(x+sv\) remains in \(\Gamma\), because an open convex cone is closed under addition of its points, and \(L\) is a vector space. This ray remains in the same hyperplane, while
\[
\lambda(x+sv)=\lambda(x)+s\lambda(v)\longrightarrow+\infty.
\tag{12}
\]
Hence every characteristic hyperplane meeting \(\Gamma\) meets \(U_T\). Both sets are convex and open. The convex continuation theorem proves the assertion. \(\square\)

When \(L\ne\{0\}\), the wedge contains affine lines parallel to \(L\). The proof explicitly accommodates them and does not require a hyperplane supporting its closure only at the vertex.

## Completing the support estimate

**Proof of Theorem 1.1.** Let \(0\ne v\in\mathcal E'(X)\), put \(K=\operatorname{supp}P^tv\), and set
\[
r=d_X(K)>0.
\tag{13}
\]
The support hull theorem makes \(K\) nonempty. Fix \(q\notin X\) and the translated exterior wedge \(q+A\) constructed above. For every \(|h|<r\),
\[
(q+A+h)\cap K=\varnothing,
\tag{14}
\]
since all points of \(q+A\) lie in \(X^c\) and \(d_X(K)=r\).

Choose a sufficiently small planar enlargement \(\Gamma_E\) of \(B\) such that
\[
(q+\Gamma+h)\cap K=\varnothing.
\tag{15}
\]
Here is why the unbounded edge creates no compactness problem. Project the compact set \(K-q-h\) onto \(E\). Its projection is compact and disjoint from \(B\), by (14), because membership of the projection in \(B\) is exactly membership of the original point in \(B+L\). In particular the projection avoids zero. Its unit directions therefore form a compact subset of the circle disjoint from the directions of \(B\). Enlarge \(B\) slightly in angle, maintaining aperture less than \(\pi\) and avoiding those directions. This proves (15).

On \(q+\Gamma+h\), the compactly supported distribution \(v\) is homogeneous for \(P^t\) and vanishes outside a bounded set. Lemma 4.1 makes it zero on that entire open wedge.

We must also exclude points on its edge. Fix \(z=q+h\), \(|h|<r\), choose a unit ray vector \(e\in B\), and choose small \(\varepsilon>0\) such that \(|h-\varepsilon e|<r\). Apply the preceding construction to the shift \(h'=h-\varepsilon e\). The point
\[
z=(q+h')+\varepsilon e
\tag{16}
\]
lies in its open wedge, so \(v\) vanishes near \(z\). Thus \(B(q,r)\) misses \(\operatorname{supp}v\).

As this holds for every \(q\in X^c\), we obtain
\[
d_X(\operatorname{supp}v)\geq r.
\tag{17}
\]
The reverse inequality follows from \(\operatorname{supp}P^tv\subset\operatorname{supp}v\). The support-distance criterion proves support convexity. The componentwise reduction at the beginning covers disconnected \(X\), and completes the proof. \(\square\)

The theorem is a sufficient condition, not a proposed converse in all dimensions. Its hypothesis also controls all affine translates of the characteristic hyperplanes, not merely those passing through one fixed point.

## Exercises with solutions

**Exercise 1 — Intermediate level: a totally characteristic projection plane.** Let \(n=3\), \(P(\xi)=\xi_1\), \(X=\{x_2>0\}\), and \(q=0\). Begin with \(N=e_3\), \(M=e_2\) in the construction. Show why the resulting restriction vanishes identically, and carry out the repair.

**Solution.** Both chosen vectors are perpendicular to \(e_1\), so \(E=\operatorname{span}(e_3,e_2)\) has \(P|_E=0\). Its orthogonal complement \(L=\mathbb Re_1\) is exterior to \(X\). Projection gives the open halfplane \(Y=\{y_2>0\}\) in \(E\), whose separating normal is \(M_0=e_2\), a characteristic vector. Choose \(N_0=e_1\). Then \(E_0=\operatorname{span}(e_2,e_1)\), \(L_0=\mathbb Re_3\), and \(P|_{E_0}\) is nonzero. The new edge still avoids \(X\). This example shows why a chosen separating plane cannot automatically be assumed to have a nonzero restricted symbol.

**Exercise 2 — Elementary level: a normal using the edge.** Take \(E=\operatorname{span}(e_1,e_2)\), \(L=\mathbb Re_3\), and a normal \(N=(a,b,c)\) with \(c\ne0\). For \(e=(u,v,0)\in\Gamma_E\), find a vector in \((e+L)\cap N^\perp\), and verify the growth used in Lemma 4.1.

**Solution.** Take \(l=-(au+bv)e_3/c\). Then \(N\cdot(e+l)=0\), so the vector \(e+l\) lies in the wedge and in the normal's kernel. The form \(\lambda\) vanishes on \(L\), hence \(\lambda(e+l)=\lambda(e)>0\). A ray in this direction stays on any affine plane with normal \(N\) and makes \(\lambda\) grow without bound. The vector cannot be zero because its \(E\)-component is the nonzero \(e\).

**Exercise 3 — Intermediate level: why every affine slice is tested.** With \(P(\xi)=\xi_1\) in the plane, let \(X\) be the union of unit disks centered at \((-2,3)\) and \((2,3)\). Check all characteristic lines through zero, and find an affine characteristic line with a nonconvex intersection. Explain which assertion of the theorem is absent.

**Solution.** Characteristic normals satisfy \(N_1=0\), so characteristic lines are horizontal. The only such line through zero is \(x_2=0\), which misses both disks. But \(x_2=3\) meets \(X\) in the two disjoint intervals \((-3,-1)\) and \((1,3)\). Its intersection is not convex. The theorem's hypothesis requires every affine characteristic line, including this translate. In fact the disconnected union is support convex componentwise, so the example also illustrates that the slice hypothesis is sufficient rather than necessary on arbitrary open sets.

**Exercise 4 — Advanced level: moving an edge point into the open wedge.** Suppose \(A=B+L\) is exterior to \(X\) and \(K\Subset X\) has distance \(r\) from \(X^c\). Explain why avoiding \(A+h\) permits an angular enlargement even though \(L\) is unbounded. Then prove the exclusion of a point \(q+h\) on the translated edge.

**Solution.** The projection of \(K-q-h\) onto \(E\) is compact and disjoint from \(B\), since its membership in \(B\) would place the original point in \(B+L\). It avoids zero, so its unit directions are a compact set disjoint from the closed angle directions. A small angular enlargement avoids them and remains pointed. For the edge point, take a unit \(e\in B\) and \(\varepsilon>0\) small enough that \(|h-\varepsilon e|<r\). The construction at this new shift gives an open wedge containing \((q+h-\varepsilon e)+\varepsilon e=q+h\). Vanishing on that wedge excludes the point from the support. Vanishing on a wedge with the original edge alone would not exclude a distribution supported on that edge.

## References

- [Separating an open convex set by a supporting covector](../prerequisites/prerequisite-bridges.html#strict-separation-of-an-open-convex-set). Lemma 2.1 is its zero-vertex specialization with the covector sign reversed.
- Thomas Kalmes, [*Surjectivity of differential operators and linear topological invariants for spaces of zero solutions*](https://arxiv.org/abs/1408.4356), *Revista Matemática Complutense* 32 (2019), 37–55. This treats geometric criteria involving boundary distance and subspaces.
- Thomas Kalmes, [*Some results on surjectivity of augmented differential operators*](https://www.tu-chemnitz.de/mathematik/analysis/kalmes/Preprints/Some_results_on_surjectivity_of_augmented_differential_operators_manuscript.pdf), *Journal of Mathematical Analysis and Applications* 386 (2012), 125–134, Section 4. The planar exterior-angle criterion is a useful companion to the lifted wedge argument above.
- Gerd Grubb, *Distributions and Operators*, open lecture chapter [Distributions](https://web.math.ku.dk/~grubb/dist3.pdf), for the distributional operations used in the support estimates.
