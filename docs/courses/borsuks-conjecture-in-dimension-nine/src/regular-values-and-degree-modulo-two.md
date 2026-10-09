# Regular values and degree modulo two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of Borsuk's counterexample counts preimages of well-chosen points modulo two. This lesson provides the three tools: Sard's theorem, which supplies points whose preimages are not degenerate (Section 2); the fact that preimages of such points are smooth manifolds (Section 3); and the degree modulo two of a map between closed manifolds, which can be read off from any such preimage, even when the map is smooth only near that preimage (Section 4).

We use from the core courses: Taylor's theorem in one variable ([Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10), Lebl, *Basic Analysis I*, Theorem 4.3.2); Lebesgue outer measure on \(\mathbb R^p\) and Fubini's theorem ([Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), Fremlin, *Measure Theory*, Volume 1, 115C–115G, and Volume 2, 251N and 252D); and singular homology with coefficients, excision and homotopy invariance ([Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), Fomberg's notes, Theorems 1.13 and 1.23 and Corollary 1.14; with coefficients as explained in Section 1 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes)). From [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport) we use the smooth inverse function theorem (Theorem 1.2) and submersion coordinates (Corollary 1.3). From [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes) we use Lemma 1.2 (local homology), Proposition 2.3(2) (every manifold is \(\mathbb Z/2\)-orientable), Proposition 3.2 (local degree), Theorem 4.1 (classes on compact subsets) and Corollary 5.1 (fundamental classes). Homology is singular homology with coefficients in \(\mathbb F_2=\mathbb Z/2\) unless stated otherwise.

## 1. Smooth maps and regular values

A *smooth \(n\)-manifold* is a Hausdorff space with a countable basis and an atlas of homeomorphisms (charts) from open sets onto open subsets of \(\mathbb R^n\) whose transition maps are smooth. Open subsets, finite products and finite disjoint unions of smooth manifolds are smooth manifolds. A map \(g:M\to N\) between smooth manifolds is *smooth near* a point \(x\) if, in charts around \(x\) and \(g(x)\), it is smooth on a neighbourhood of \(x\). Its derivative at \(x\) in these charts is a linear map \(\mathbb R^n\to\mathbb R^p\), where \(n=\dim M\) and \(p=\dim N\); changing charts composes it on both sides with invertible matrices (the derivatives of transition maps), so its rank, and whether it is surjective, injective or invertible, do not depend on the charts.

**Definition 1.1.** Let \(g:M\to N\) be smooth near every point of an open set \(O\subseteq M\). A point \(x\in O\) is *regular* if the derivative of \(g\) at \(x\) is surjective, and *critical* otherwise. A point \(y\in N\) is a **regular value** of \(g|_O\) if every \(x\in O\) with \(g(x)=y\) is regular; points not in \(g(O)\) are regular values.

## 2. Sard's theorem

A set \(Z\subseteq\mathbb R^p\) is *null* if its Lebesgue outer measure is zero: for every \(\varepsilon>0\) it is covered by countably many boxes of total volume less than \(\varepsilon\) (Fremlin 115C). Subsets and countable unions of null sets are null, and a nonempty open set is not null (Fremlin 115D). A set that is a countable union of compact sets is Borel, hence Lebesgue measurable (Fremlin 115G).

**Theorem 2.1** (Sard, 1942). Let \(U\subseteq\mathbb R^n\) be open and \(g:U\to\mathbb R^p\) smooth, and let \(C\) be the set of critical points of \(g\). Then \(g(C)\) is null.

*Proof.* We argue by induction on \(n\), for all \(p\) simultaneously. If \(p=0\) there are no critical points. If \(n=0\), the set \(g(C)\) has at most one point, which is null when \(p\ge1\). Let \(n\ge1\), \(p\ge1\), and assume the theorem for maps defined on open subsets of \(\mathbb R^{n-1}\). For \(i\ge1\) let \(C_i\) be the set of points of \(U\) at which all partial derivatives of \(g\) of orders \(1,\dots,i\) vanish. These sets are closed in \(U\), and \(C\supseteq C_1\supseteq C_2\supseteq\cdots\). Fix \(q\ge1\) with \((q+1)p>n\). Then
\[
C=(C\setminus C_1)\cup\bigcup_{i=1}^{q-1}(C_i\setminus C_{i+1})\cup C_q ,
\]
and we show that each of these pieces has null image. Open and closed subsets of \(U\) are countable unions of compact sets, and so are their intersections; every point of such a piece \(E\) will have an open neighbourhood \(O\) with \(g(E\cap O)\) null, and countably many of these neighbourhoods cover \(E\) because \(U\) has a countable basis.

*Step 1: \(g(C\setminus C_1)\) is null.* If \(p=1\), a critical point has zero derivative, so \(C=C_1\). Let \(p\ge2\) and \(\bar x\in C\setminus C_1\). Some first partial derivative of some coordinate of \(g\) is nonzero at \(\bar x\); after permuting the coordinates of \(\mathbb R^n\) and of \(\mathbb R^p\) (isometries, which preserve null sets), \(\partial g_1/\partial x_1(\bar x)\neq0\). The map \(\eta(x)=(g_1(x),x_2,\dots,x_n)\) has invertible derivative at \(\bar x\), so by the smooth inverse function theorem it restricts to a diffeomorphism from an open \(O\ni\bar x\) onto an open \(O'\subseteq\mathbb R^n\). The map \(\gamma=g\circ\eta^{-1}:O'\to\mathbb R^p\) has the form \(\gamma(t,z)=(t,\gamma_2(t,z),\dots,\gamma_p(t,z))\), \(t\in\mathbb R\), \(z\in\mathbb R^{n-1}\). Its derivative is block lower triangular with a \(1\) in the corner, so \((t,z)\) is critical for \(\gamma\) exactly when \(z\) is critical for \(\gamma^t(z)=(\gamma_2,\dots,\gamma_p)(t,z)\), defined on the open set \(O'_t=\{z:(t,z)\in O'\}\subseteq\mathbb R^{n-1}\). By the chain rule the critical points of \(\gamma\) are \(\eta(C\cap O)\), so \(g(C\cap O)\) is the set of critical values of \(\gamma\). It is a countable union of compact sets, and its intersection with each hyperplane \(\{t\}\times\mathbb R^{p-1}\) is \(\{t\}\) times the critical values of \(\gamma^t\), which are null in \(\mathbb R^{p-1}\) by the induction hypothesis. By Fubini's theorem (Fremlin 251N and 252D, applied to \(\mathbb R^p=\mathbb R\times\mathbb R^{p-1}\)), \(g(C\cap O)\) is null.

*Step 2: \(g(C_i\setminus C_{i+1})\) is null for \(1\le i\le q-1\).* Let \(\bar x\in C_i\setminus C_{i+1}\). Some partial derivative of order \(i+1\) of some \(g_r\) is nonzero at \(\bar x\); write it as \(\partial w/\partial x_s\), where \(w\) is a partial derivative of \(g_r\) of order \(i\), and permute coordinates so that \(s=1\). Then \(w\) vanishes on \(C_i\), and \(\eta(x)=(w(x),x_2,\dots,x_n)\) restricts to a diffeomorphism from an open \(O\ni\bar x\) onto an open \(O'\). The set \(O'_0=\{z\in\mathbb R^{n-1}:(0,z)\in O'\}\) is open, and \(\bar\gamma(z)=g(\eta^{-1}(0,z))\) is smooth on it. Every point of \(C_i\cap O\) is mapped by \(\eta\) into \(\{0\}\times O'_0\), and at such a point \(Dg=0\) because \(i\ge1\); so the corresponding \(z\) is a critical point of \(\bar\gamma\). Hence \(g(C_i\cap O)\) is contained in the set of critical values of \(\bar\gamma\), which is null by the induction hypothesis.

*Step 3: \(g(C_q)\) is null.* Let \(Q\subseteq U\) be a closed cube of side \(\delta\); countably many such cubes cover \(U\). Let \(M_0\) bound the absolute values of all partial derivatives of order \(q+1\) of all coordinates of \(g\) on \(Q\). For \(x\in C_q\cap Q\) and \(x+h\in Q\), the function \(\phi(s)=g_j(x+sh)\) on \([0,1]\) has \(\phi^{(l)}(0)=0\) for \(1\le l\le q\), so Taylor's theorem gives \(s\in(0,1)\) with \(\phi(1)-\phi(0)=\phi^{(q+1)}(s)/(q+1)!\), and \(|\phi^{(q+1)}(s)|\le n^{q+1}M_0|h|^{q+1}\). Hence \(|g(x+h)-g(x)|\le c|h|^{q+1}\) with \(c=\sqrt p\,n^{q+1}M_0\). Divide \(Q\) into \(r^n\) cubes of side \(\delta/r\). If one of them, \(Q'\), contains a point \(x\in C_q\), then every point of \(Q'\) is \(x+h\) with \(|h|\le\sqrt n\delta/r\), so \(g(Q')\) lies in a cube of side \(2c(\sqrt n\delta/r)^{q+1}\), of volume \(b\,r^{-(q+1)p}\) with \(b\) independent of \(r\). So \(g(C_q\cap Q)\) is covered by boxes of total volume at most \(b\,r^{n-(q+1)p}\), which tends to \(0\) as \(r\to\infty\). \(\square\)

**Corollary 2.2.** Let \(g:M\to N\) be smooth near every point of an open set \(O\subseteq M\), with \(M,N\) smooth manifolds. Then in every chart of \(N\) the critical values of \(g|_O\) form a null set. In particular every nonempty open subset of \(N\) contains a regular value of \(g|_O\).

*Proof.* Cover \(O\) by countably many chart domains on which \(g\) maps into a chart domain of \(N\) and is smooth; in each, Theorem 2.1 applies. A null set has empty interior, and a transition map of \(N\) is smooth, so it maps null sets to null sets (Exercise 5.1); hence the statement does not depend on the chart. \(\square\)

## 3. Regular level sets

**Proposition 3.1** (Regular level sets). Let \(g:M\to N\) be smooth near every point of an open set \(O\subseteq M\), with \(\dim M=n\ge p=\dim N\), and let \(y\) be a regular value of \(g|_O\). Then \(L=g^{-1}(y)\cap O\) is a smooth manifold of dimension \(n-p\), and its topology is the subspace topology. Near each \(x\in L\) there are coordinates \((u,z)\in\mathbb R^p\times\mathbb R^{n-p}\) on \(M\) and coordinates on \(N\) around \(y\) in which \(g(u,z)=u\), \(y=0\), and \(L=\{u=0\}\); then \(z\) is a chart of \(L\). If a map \(G\) is smooth near \(x\) on \(M\), its restriction \(z\mapsto G(0,z)\) is smooth on \(L\), and its derivative is the derivative of \(G\) restricted to the \(z\)-directions, that is, to the kernel of the derivative of \(g\). If \(g^{-1}(y)\subseteq O\) and \(M\) is compact, then \(L\) is compact.

*Proof.* The coordinates are those of Corollary 1.3 of [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport) (submersion coordinates). Two such charts of \(L\) differ by the restriction of a smooth change of coordinates of \(M\) to \(\{u=0\}\), which is smooth. \(L\) is Hausdorff with a countable basis as a subspace of \(M\). If \(g^{-1}(y)\subseteq O\), then \(L=g^{-1}(y)\) is closed in \(M\) because \(g\) is continuous on \(M\); a closed subset of a compact space is compact. \(\square\)

**Corollary 3.2.** If in Proposition 3.1 \(n=p\), then \(L\) is discrete; if moreover \(L\) is compact, it is finite.

*Proof.* A zero-dimensional manifold is discrete, and a compact discrete space is finite. \(\square\)

## 4. Degree modulo two

Let \(M\) be a closed (compact) smooth \(n\)-manifold, possibly disconnected. Each group \(H_n(M,M\setminus x)\cong\mathbb F_2\) has exactly one generator, and these generators form a \(\mathbb Z/2\)-orientation (Proposition 2.3(2) of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes)). By Theorem 4.1(2) there, with \(K=M\), there is a unique class
\[
[M]\in H_n(M)
\]
whose image in \(H_n(M,M\setminus x)\) is the generator for every \(x\in M\); we call it the (total) fundamental class. If \(Y\) is a connected closed \(n\)-manifold, then \(H_n(Y)=\{0,[Y]\}\), and \(H_n(Y)\to H_n(Y,Y\setminus y)\) is an isomorphism for every \(y\) (Corollary 5.1 there).

**Definition 4.1.** For a continuous map \(q:M\to Y\) from a closed \(n\)-manifold to a connected closed \(n\)-manifold, the **degree modulo two** \(\deg_2q\in\mathbb F_2\) is defined by \(q_*[M]=\deg_2(q)\,[Y]\).

Homotopic maps have the same degree modulo two, because they induce the same map on homology. The identity has degree one.

**Lemma 4.2** (Local counting). Let \(M\) be a closed smooth \(n\)-manifold, \(Y\) a Hausdorff space, \(q:M\to Y\) continuous, and \(y\in Y\). Suppose \(y\) has an open neighbourhood \(W\) with a homeomorphism \(\psi:W\to W'\) onto an open subset of \(\mathbb R^n\), and that for each \(x\in q^{-1}(y)\), in a chart of \(M\) around \(x\), the map \(\psi\circ q\) is differentiable at \(x\) with invertible derivative. Then \(q^{-1}(y)\) is finite, and the image of \([M]\) in \(H_n(Y,Y\setminus y)\cong\mathbb F_2\) is \(|q^{-1}(y)|\) modulo two times the generator. If \(Y\) is a connected closed \(n\)-manifold, then
\[
\deg_2q=|q^{-1}(y)|\bmod 2 .
\]

*Proof.* By Proposition 3.2 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes), each \(x\in q^{-1}(y)\) has a neighbourhood containing no other point of \(q^{-1}(y)\). So \(q^{-1}(y)\), a closed subset of the compact space \(M\), is finite: \(q^{-1}(y)=\{x_1,\dots,x_N\}\). Choose disjoint open chart balls \(B_j\ni x_j\) with \(q(B_j)\subseteq W\) and \(q(B_j\setminus x_j)\subseteq Y\setminus y\), small enough for Proposition 3.2. Put \(F=q^{-1}(y)\). The class \([M]\) maps to a class in \(H_n(M,M\setminus F)\), and \(q_*\) sends this group to \(H_n(Y,Y\setminus y)\) because \(q(M\setminus F)\subseteq Y\setminus y\). Excision of the closed set \(M\setminus\bigcup_jB_j\), contained in the open set \(M\setminus F\), gives
\[
H_n(M,M\setminus F)\cong H_n\Bigl(\bigcup_jB_j,\bigcup_jB_j\setminus F\Bigr)=\bigoplus_{j=1}^NH_n(B_j,B_j\setminus x_j),
\]
and the component of \([M]\) in the \(j\)-th summand corresponds to the generator of \(H_n(M,M\setminus x_j)\). Similarly \(H_n(W,W\setminus y)\cong H_n(Y,Y\setminus y)\) by excision of the closed set \(Y\setminus W\), and \(\psi\) identifies it with \(H_n(\mathbb R^n,\mathbb R^n\setminus\psi(y))\). In charts, Proposition 3.2 says that \(q_*\) maps the integral local generator at \(x_j\) to the integral local generator at \(\psi(y)\) when the derivative has positive determinant; reducing coefficients modulo two (Lemma 1.2(2) there), it maps the generator of \(H_n(B_j,B_j\setminus x_j)\) to the generator of \(H_n(\mathbb R^n,\mathbb R^n\setminus\psi(y))\). If the determinant is negative, apply this to \(\rho\circ\psi\circ q\) for a reflection \(\rho\) of \(\mathbb R^n\) fixing \(\psi(y)\); the homeomorphism \(\rho\) induces an automorphism of \(H_n(\mathbb R^n,\mathbb R^n\setminus\psi(y))\cong\mathbb F_2\), which is the identity. So the image of \([M]\) is \(N\) times the generator. If \(Y\) is a connected closed \(n\)-manifold, \([Y]\) maps to the generator of \(H_n(Y,Y\setminus y)\) by an isomorphism, and comparing gives \(\deg_2q=N\bmod2\). \(\square\)

In particular, if \(q:M\to Y\) is smooth between closed \(n\)-manifolds and \(y\) is a regular value, then \(\deg_2q\equiv|q^{-1}(y)|\pmod2\); but the lemma needs smoothness only near the one fibre \(q^{-1}(y)\).

**Corollary 4.3.** If \(q:M\to Y\) is not surjective, then \(\deg_2q=0\). So a map of degree one modulo two is surjective.

*Proof.* If \(y\notin q(M)\), then \(q\) maps \(M\) into \(Y\setminus y\), so the image of \(q_*[M]\) in \(H_n(Y,Y\setminus y)\) is zero, while \([Y]\) maps to the generator. \(\square\)

## 5. Exercises

**5.1.** Show that a smooth map \(\theta:U\to\mathbb R^p\) on an open \(U\subseteq\mathbb R^p\) maps null sets to null sets. (Cover \(U\) by countably many closed cubes on which the derivative is bounded.)

**5.2.** Let \(g:\mathbb R\to\mathbb R\) be smooth with \(g(t)=0\) for \(t\le0\) and \(g(t)=e^{-1/t}\) for \(t>0\). Find its critical points and critical values, and check Theorem 2.1 directly.

**5.3.** Let \(q:S^1\to S^1\), \(q(z)=z^d\) for an integer \(d\ne0\), on the unit circle of \(\mathbb C\). Use Lemma 4.2 to compute \(\deg_2q\).

**5.4.** In Lemma 4.2, why is the hypothesis on \(q\) only needed at the points of \(q^{-1}(y)\), and not near them? Where does the proof use that \(M\) is compact?

## 6. Solutions

**5.1.** On a closed cube \(Q\subseteq U\) with \(\|D\theta\|\le\Lambda\), the mean value inequality gives \(|\theta(a)-\theta(b)|\le\Lambda|a-b|\). A null subset of \(Q\) is covered by cubes of total volume less than \(\varepsilon\), which may be taken inside a slightly larger cube in \(U\); the image of a cube of side \(s\) lies in a cube of side \(2\Lambda\sqrt p\,s\), so the image is covered by cubes of total volume at most \((2\Lambda\sqrt p)^p\varepsilon\). Countably many cubes cover \(U\).

**5.2.** \(g'(t)=e^{-1/t}/t^2>0\) for \(t>0\) and \(g'(t)=0\) for \(t\le0\) (all derivatives of \(e^{-1/t}\) tend to \(0\) as \(t\downarrow0\)). The critical points are \(t\le0\), and the only critical value is \(0\), a null set. Here the critical set is not null, but its image is.

**5.3.** Every point is a regular value: \(q\) is a local diffeomorphism. The preimage of \(1\) has \(|d|\) points, so \(\deg_2q=d\bmod2\).

**5.4.** Proposition 3.2 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes) only needs differentiability at the point with invertible derivative; it produces the isolating ball and the homotopy to the linear map itself. Compactness is used to conclude that the closed discrete set \(q^{-1}(y)\) is finite, and to have the fundamental class \([M]\).

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
- [Hat] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002 (author's page). https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
