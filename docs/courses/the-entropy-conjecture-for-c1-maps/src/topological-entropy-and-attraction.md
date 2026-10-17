# Topological entropy and attraction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Lemma 2.2 and the coefficient comparison were added by GPT-6 Astra (OpenAI), October 2026. Self-checked by the respective writing AIs. Public domain (CC0).*

Topological entropy measures how fast the orbits of a map become distinguishable at a fixed resolution. Shub's entropy conjecture predicts that this growth is at least the growth visible in homology. This course proves OpenAI's 2026 theorem that the conjecture fails for continuously differentiable self-maps: there is a \(C^1\) map of a compact manifold with zero topological entropy whose action on second homology has the eigenvalue \(2\).

This first lesson supplies the facts about entropy that the proof needs. Section 1 defines topological entropy and proves that it does not depend on the metric. Section 2 treats invariant subsets, unions and periodic maps, proves finite-dimensionality of the relevant homology, and states the conjecture. Section 3 proves a localization theorem: if every orbit approaches a compact invariant set on which the entropy is zero, the whole map has entropy zero. Section 4 shows that maps of the sphere which only move radii monotonically have zero entropy, even in products.

We use from the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (Lebl, *Basic Analysis II*): compactness through open covers ([Definition 7.4.7](https://www.jirka.org/ra/html/sec_metcompact.html)), the extreme value theorem ([Theorem 7.5.6](https://www.jirka.org/ra/html/sec_metcont.html)) and uniform continuity on compact spaces ([Theorem 7.5.11](https://www.jirka.org/ra/html/sec_metcont.html)).

## 1. Separated sets and entropy

Throughout this section \((X,d)\) is a nonempty compact metric space and \(F:X\to X\) is continuous. For an integer \(n\geq1\) put
\[
d_n(x,y)=\max_{0\leq j<n}d(F^jx,F^jy).
\]
Each \(d_n\) is a metric on \(X\), and \(d_1=d\). It is continuous on \(X\times X\), because each \(F^j\) is continuous; and \(d\leq d_n\). Hence a set is open for \(d_n\) exactly when it is open for \(d\): a \(d\)-ball contains the \(d_n\)-ball of the same radius, and a \(d_n\)-ball \(\{y:d_n(x,y)<r\}\) is the preimage of an open set under the continuous map \(y\mapsto d_n(x,y)\).

**Definition 1.1.** Let \(\varepsilon>0\). A set \(E\subseteq X\) is **\((n,\varepsilon)\)-separated** if \(d_n(x,y)>\varepsilon\) for all distinct \(x,y\in E\). Let \(s_F(n,\varepsilon)\) be the largest cardinality of an \((n,\varepsilon)\)-separated set. Put
\[
\begin{gathered}
h(F,\varepsilon)=\limsup_{n\to\infty}\frac1n\log s_F(n,\varepsilon),\\
h_{\mathrm{top}}(F)=\lim_{\varepsilon\downarrow0}h(F,\varepsilon).
\end{gathered}
\]
The number \(h_{\mathrm{top}}(F)\in[0,\infty]\) is the **topological entropy** of \(F\).

**Lemma 1.2.** (a) \(s_F(n,\varepsilon)\) is finite: it is at most the number of sets in any cover of \(X\) by open \(d_n\)-balls of radius \(\varepsilon/2\), and such finite covers exist. (b) \(s_F(n,\varepsilon)\) is nondecreasing in \(n\) and nonincreasing in \(\varepsilon\). Consequently \(h(F,\varepsilon)\) is nonincreasing in \(\varepsilon\), the limit defining \(h_{\mathrm{top}}(F)\) exists and equals \(\sup_{\varepsilon>0}h(F,\varepsilon)\), and \(h(F,\varepsilon)\geq0\).

*Proof.* (a) The open \(d_n\)-balls of radius \(\varepsilon/2\) about all points of \(X\) cover \(X\); by compactness finitely many do. Two points of one such ball are at \(d_n\)-distance less than \(\varepsilon\), so an \((n,\varepsilon)\)-separated set has at most one point in each ball. (b) Since \(d_n\leq d_{n+1}\), an \((n,\varepsilon)\)-separated set is \((n+1,\varepsilon)\)-separated; if \(\varepsilon'\leq\varepsilon\), an \((n,\varepsilon)\)-separated set is \((n,\varepsilon')\)-separated. Every one-point set is separated, so \(s_F\geq1\) and \(h(F,\varepsilon)\geq0\). A nonincreasing function of \(\varepsilon\) has a limit as \(\varepsilon\downarrow0\), equal to its supremum. \(\square\)

**Proposition 1.3 (independence of the metric).** If \(d\) and \(d'\) are metrics on \(X\) defining the same topology, they give the same topological entropy for \(F\).

*Proof.* The identity map \((X,d')\to(X,d)\) is continuous, so by compactness it is uniformly continuous (Lebl, Theorem 7.5.11): for \(\varepsilon>0\) there is \(\delta>0\) such that \(d'(x,y)<\delta\) implies \(d(x,y)<\varepsilon\). Let \(E\) be \((n,\varepsilon)\)-separated for \(d\). For distinct \(x,y\in E\) some \(j<n\) has \(d(F^jx,F^jy)>\varepsilon\), hence \(d'(F^jx,F^jy)\geq\delta>\delta/2\). So \(E\) is \((n,\delta/2)\)-separated for \(d'\), and \(s^{d}_F(n,\varepsilon)\leq s^{d'}_F(n,\delta/2)\). Therefore \(h^{d}(F,\varepsilon)\leq h^{d'}(F,\delta/2)\leq h^{d'}_{\mathrm{top}}(F)\) for every \(\varepsilon\), so \(h^d_{\mathrm{top}}(F)\leq h^{d'}_{\mathrm{top}}(F)\). Exchanging the metrics gives equality. \(\square\)

Consequently the entropy of a continuous self-map of a compact metrizable space, such as a compact manifold, is well defined. Two compatible metrics on a compact space are also **uniformly equivalent**, in the sense used in the proof: each is uniformly continuous with respect to the other. In particular, \(d(x_n,K)\to0\) for one compatible metric and a compact set \(K\) if and only if the same holds for every compatible metric (Exercise 5.4).

## 2. Invariant pieces and the conjecture

A set \(Z\subseteq X\) is **forward invariant** if \(F(Z)\subseteq Z\). For compact forward invariant \(Z\) we write \(F|_Z\) for the restriction, with the restricted metric, and \(s_Z(n,\varepsilon)\) for its separated-set numbers.

**Lemma 2.1.** Let \(Z,Z_1,Z_2\subseteq X\) be nonempty, compact and forward invariant.

(a) \(h_{\mathrm{top}}(F|_Z)\leq h_{\mathrm{top}}(F)\).

(b) If \(Z=Z_1\cup Z_2\), then \(s_Z(n,\varepsilon)\leq s_{Z_1}(n,\varepsilon)+s_{Z_2}(n,\varepsilon)\), and \(h_{\mathrm{top}}(F|_Z)\) is the larger of \(h_{\mathrm{top}}(F|_{Z_1})\) and \(h_{\mathrm{top}}(F|_{Z_2})\).

(c) If \(F^p=\mathrm{id}_X\) for some \(p\geq1\), then \(h_{\mathrm{top}}(F)=0\).

*Proof.* (a) The orbit metric of \(F|_Z\) is the restriction of \(d_n\), so separated subsets of \(Z\) are separated subsets of \(X\).

(b) An \((n,\varepsilon)\)-separated \(E\subseteq Z\) splits into \(E\cap Z_1\subseteq Z_1\) and \(E\setminus Z_1\subseteq Z_2\), each separated. For positive numbers \(a,b\) we have \(\log(a+b)\leq\log2+\max\{\log a,\log b\}\), so
\[
\begin{aligned}
&\frac1n\log s_Z(n,\varepsilon)\leq\frac{\log2}n\\
&\quad +\max_{i=1,2}\frac1n\log s_{Z_i}(n,\varepsilon),
\end{aligned}
\]
and the upper limit of a maximum of two sequences is the maximum of their upper limits. Thus \(h(F|_Z,\varepsilon)\leq\max_i h(F|_{Z_i},\varepsilon)\), which is at most \(\max_ih_{\mathrm{top}}(F|_{Z_i})\); letting \(\varepsilon\downarrow0\) gives \(\leq\), and (a) applied inside \(Z\) gives \(\geq\).

(c) For \(n\geq p\) every \(F^j\) with \(j<n\) equals some \(F^{j'}\) with \(j'<p\), so \(d_n=d_p\) and \(s_F(n,\varepsilon)=s_F(p,\varepsilon)\), a number independent of \(n\). Hence \(h(F,\varepsilon)=0\) for every \(\varepsilon\). \(\square\)

### Finite-dimensional homology

**Lemma 2.2.** Let \(M\) be a compact smooth \(n\)-manifold without boundary. It need not be orientable or connected. Each real singular homology group \(H_k(M;\mathbb R)\) is finite dimensional, and it vanishes for \(k>n\). Consequently \(\bigoplus_{k\geq0}H_k(M;\mathbb R)\) is finite dimensional.

*Proof.* A manifold is locally path connected, so its components are open. Compactness implies that there are finitely many components. Each is also closed and compact. Every singular simplex lies in one component, so the singular chain complex, and hence its homology, is the direct sum over these components. We can therefore suppose that \(M\) is connected. The empty manifold has zero homology. A compact zero-dimensional manifold is a finite discrete set. For a point there is one singular simplex in each degree, and its boundary coefficient is \(\sum_{j=0}^k(-1)^j\), equal to one for positive even \(k\) and zero for odd \(k\). Thus its homology is \(\mathbb R\) in degree zero and zero in higher degrees. Taking the direct sum proves the assertion for a finite discrete set. Suppose henceforth that \(n\geq1\).

*The oriented case: a finite cycle controls every degree.* Suppose first that \(M\) is oriented. Its real fundamental class exists by [Orientations and fundamental classes, Corollary 5.1](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes#5-fundamental-classes). Choose a singular cycle representing it:
\[
c=\sum_{i=1}^{N}a_i\sigma_i\in C_n(M;\mathbb R).
\]
The sum is finite by the definition of ordinary singular chains. Fix \(0\leq k\leq n\). Name the rear \(k\)-face and front \((n-k)\)-face of each simplex:
\[
\begin{aligned}
\tau_{i,k}&=\sigma_i|[v_{n-k},\ldots,v_n],\\
\eta_{i,k}&=\sigma_i|[v_0,\ldots,v_{n-k}].
\end{aligned}
\]
Set
\[
\begin{gathered}
W_k=\operatorname{span}_{\mathbb R}\{\tau_{1,k},\ldots,\tau_{N,k}\}\\
\subseteq C_k(M;\mathbb R).
\end{gathered}
\]
Thus \(\dim W_k\leq N\). The linear cap-product map on cocycles of degree \(n-k\) is
\[
\begin{aligned}
Z^{n-k}(M;\mathbb R)&\longrightarrow W_k\cap Z_k(M;\mathbb R),\\
\varphi&\longmapsto c\frown\varphi\\
&=\sum_{i=1}^{N}a_i\varphi(\eta_{i,k})\tau_{i,k}.
\end{aligned}
\]
This is a cycle because \(\partial c=0\) and \(\delta\varphi=0\), by the cap boundary identity, [Cap products and cohomology with compact supports, (1.1)–(1.2)](course:poincare-duality-on-manifolds/cap-products-and-cohomology-with-compact-supports#1-the-cap-product). The same identity makes the resulting homology class depend only on \([\varphi]\). By [Poincaré duality, Corollary 2.1](course:poincare-duality-on-manifolds/poincare-duality#2-consequences), every class of \(H_k(M;\mathbb R)\) is \([c\frown\varphi]\) for some such cocycle. Hence the map
\[
\begin{gathered}
W_k\cap Z_k(M;\mathbb R)\longrightarrow H_k(M;\mathbb R),\\
z\longmapsto[z]
\end{gathered}
\]
is surjective, and \(\dim H_k(M;\mathbb R)\leq N\). We do not assert that the individual faces spanning \(W_k\) are cycles. Vanishing for \(k>n\) is Corollary 5.1 of the orientation lesson. Thus the total dimension is at most \((n+1)N\). The cited duality proof is local-to-global and does not assume finite-dimensional homology.

*An oriented two-sheeted cover.* Let \(\operatorname{Or}(T_xM)\) be the set of orientations of the tangent space at \(x\). For a smooth manifold with no chosen orientation, let
\[
\begin{gathered}
\widetilde M=\coprod_{x\in M}\operatorname{Or}(T_xM),\\
p:\widetilde M\longrightarrow M,\qquad p(x,o)=x.
\end{gathered}
\]
The disjoint union here first defines the set of pairs \((x,o)\); the following charts define its topology. An orientation is one of the two equivalence classes of ordered tangent bases, where two bases are equivalent when their change-of-basis determinant is positive. A chart \(x_i:U_i\to\mathbb R^n\) identifies \(p^{-1}(U_i)\) with \(U_i\times\{+1,-1\}\), recording whether \(o\) agrees with its coordinate basis. Write \(g_{ji}=x_j\circ x_i^{-1}\) for the coordinate change from \(x_i(U_i\cap U_j)\) to \(x_j(U_i\cap U_j)\). On overlaps the labels obey
\[
\begin{gathered}
\varepsilon_j=s_{ji}(x)\varepsilon_i,
\\
s_{ji}(x)=\operatorname{sign}\det Dg_{ji}(x_i(x)).
\end{gathered}
\]
The sign is locally constant, and the chain rule gives \(s_{ki}=s_{kj}s_{ji}\). These transitions define a smooth two-sheeted covering. Its space is Hausdorff: points over different base points have disjoint inverse-image neighbourhoods, and the two points over one base point have disjoint sheet neighbourhoods. A countable atlas of \(M\) lifts to a countable atlas with two sheets per chart, so \(\widetilde M\) is second countable.

On the sheet labelled \(\varepsilon\), use the coordinate \(R_\varepsilon\circ x_i\), where \(R_+=1\) and \(R_-\) is reflection in the first coordinate. Its transition determinant has sign
\[
\varepsilon_j s_{ji}(x)\varepsilon_i=1.
\]
The cover is therefore oriented, by [Orientations and fundamental classes, Corollary 3.3](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes#3-orientations-from-charts). It is compact: finitely many closed chart balls \(K_i\subset U_i\) have interiors covering \(M\), and \(p^{-1}(K_i)\cong K_i\times\{+1,-1\}\) is compact. Their inverse images cover \(\widetilde M\). The oriented case already proved applies to each of its finitely many components.

*Transfer and the return to \(M\).* Every continuous simplex \(\sigma:\Delta^k\to M\) has exactly two lifts to \(\widetilde M\), one for each choice over a fixed vertex. Here is the lifting argument. A path lifts uniquely after a starting sheet is chosen: subdivide its compact parameter interval into pieces mapping into covering charts and successively use their inverse sheets. For a homotopy of paths with fixed endpoints, subdivide its parameter square into a rectangular grid fine enough that the image of each cell lies in one covering chart. The lift around that cell closes in its inverse sheet. Cancelling common grid edges shows that homotopic paths have the same lifted endpoint. Paths in the convex simplex with the same endpoints are homotopic relative to their endpoints by linear interpolation. Lift their images starting over the fixed vertex; the resulting endpoint is therefore independent of the path. This defines a lift of \(\sigma\). It is continuous: near any point of \(\Delta^k\), choose a convex relative neighbourhood mapping into one covering chart, where this construction agrees with a single continuous inverse sheet. Uniqueness follows from path lifting. The two choices give precisely the two lifts.

Write these lifts as \(\widetilde\sigma_1,\widetilde\sigma_2\). Define the real-linear maps
\[
\begin{aligned}
T_k:C_k(M;\mathbb R)&\longrightarrow C_k(\widetilde M;\mathbb R),\\
T_k(\sigma)&=\widetilde\sigma_1+\widetilde\sigma_2.
\end{aligned}
\]
There is no ordering choice in their sum. Restricting the two lifts to any face gives exactly the two lifts of that face: evaluation at one vertex of the face gives the two different sheet points, and a lift is determined there. Thus the alternating face sums satisfy \(\partial T_k=T_{k-1}\partial\). Composition of simplices with \(p\) defines a chain map \(p_\#:C_*(\widetilde M;\mathbb R)\to C_*(M;\mathbb R)\), and
\[
p_\#T_k=2\operatorname{id}_{C_k(M;\mathbb R)}.
\]
Both maps therefore descend to homology, with \(p_*T_*=2\operatorname{id}\). Since \(2\) is invertible in \(\mathbb R\), \(T_*:H_k(M;\mathbb R)\to H_k(\widetilde M;\mathbb R)\) is injective: it has left inverse \(\tfrac12p_*\). The target is finite dimensional and zero above degree \(n\), which proves both assertions for \(M\). This argument does not require the cover to be connected or the deck transformation to preserve orientation. \(\square\)

**Complex coefficients and spectral radius.** A complex singular chain is uniquely a real chain plus \(i\) times a real chain, and the boundary acts on both parts. The same decomposition holds for cycles and boundaries. Consequently the canonical complex-linear map
\[
\begin{gathered}
H_k(M;\mathbb R)\otimes_{\mathbb R}\mathbb C
\longrightarrow H_k(M;\mathbb C),\\
[c]\otimes z\longmapsto[zc]
\end{gathered}
\]
is an isomorphism, compatible with maps induced by continuous self-maps of \(M\). Lemma 2.2 makes the total complex homology a finite-dimensional vector space. Its endomorphism is block diagonal by degree, so its eigenvalues are exactly the union of the eigenvalues of the degree blocks: its characteristic polynomial is the product of theirs. The maximum of their absolute values is therefore the usual spectral radius on total homology. In particular a nonzero real eigenvector with eigenvalue \(2\) remains nonzero after complexification and gives spectral radius at least \(2\).

**The entropy conjecture.** Let \(M\) be a nonempty compact smooth manifold without boundary and \(f:M\to M\) continuous. The induced linear maps \(f_*:H_k(M;\mathbb R)\to H_k(M;\mathbb R)\) on singular homology with real coefficients (functoriality: [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), Fomberg's notes, Proposition 1.9; coefficients as in Section 1 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes)) have eigenvalues; let \(\rho(f_*)\) be the supremum of \(|\lambda|\) over the eigenvalues \(\lambda\in\mathbb C\) of \(f_*\otimes\mathbb C\) on the spaces \(H_k(M;\mathbb C)\).
(By Lemma 2.2 these spaces are finite dimensional and \(\rho(f_*)\) is the spectral radius of \(f_*\) on \(\bigoplus_kH_k(M;\mathbb R)\); this course only uses that a real eigenvector \(v\neq0\) with \(f_*v=2v\) forces \(\rho(f_*)\geq2\).) Shub's **entropy conjecture** asks whether
\[
h_{\mathrm{top}}(f)\geq\log\rho(f_*)\tag{2.1}
\]
for every \(C^1\) map \(f\) of a compact smooth manifold without boundary. Known results mark its scope: Manning proved (2.1) for the action on \(H_1\) of every continuous map; Misiurewicz and Przytycki proved it for the top-dimensional homology (the topological degree) of \(C^1\) maps; Yomdin proved (2.1) in full for \(C^\infty\) maps, by bounding homological growth through volume growth, and Gromov's Bourbaki exposition explains the estimates; Saghin and Xia, and Liao, Viana and Yang, proved it for classes of \(C^1\) diffeomorphisms. The counterexample of this course is a noninvertible \(C^1\) map whose eigenvalue \(2\) lives in \(H_2\) of a manifold of dimension at least five, so it is consistent with all of these.

## 3. Localization of entropy

**Theorem 3.1 (entropy localization).** Let \(F:X\to X\) be a continuous map of a nonempty compact metric space and \(Z\subseteq X\) a nonempty compact forward invariant set. Suppose that \(h_{\mathrm{top}}(F|_Z)=0\) and that \(d(F^nx,Z)\to0\) for every \(x\in X\).
Then \(h_{\mathrm{top}}(F)=0\).

No uniform rate of approach is assumed: different points may need arbitrarily long to come close to \(Z\). The proof shows that, nevertheless, the proportion of time an orbit spends far from \(Z\) is uniformly small in the long run.

*Proof.* Fix \(\varepsilon>0\) and an integer \(m\geq1\). Choose an \((m,\varepsilon/4)\)-separated set \(E\subseteq Z\) of the largest cardinality \(P=P(m)=s_Z(m,\varepsilon/4)\). Let \(V\subseteq X\) be the union of the open \(d_m\)-balls of radius \(\varepsilon/2\) about the points of \(E\). Then \(V\) is open, and \(Z\subseteq V\): a point \(z\in Z\) with \(d_m(z,e)>\varepsilon/4\) for all \(e\in E\) could be added to \(E\), contradicting the maximal cardinality. Choose also finitely many, say \(Q=Q(m)\), open \(d_m\)-balls of radius \(\varepsilon/2\) covering \(X\).

*Step 1: few visits outside \(V\).* We show: for every \(0<\tau<1\) there is an integer \(J\geq1\) with
\[
\begin{aligned}
&\#\{0\leq i<r:\ F^{mi}x\notin V\}\\
&\quad \leq\tau r+J\\
&\text{for all }x\in X\text{ and }r\geq1.
\end{aligned}\tag{3.1}
\]
The function \(y\mapsto d(y,X\setminus V)\) is continuous and positive on the compact set \(Z\) (if \(V=X\) there is nothing to prove), so it has a positive minimum \(\eta\) there (Lebl, Theorem 7.5.6). Every \(y\) with \(d(y,Z)<\eta\) lies in \(V\): take \(z\in Z\) with \(d(y,z)<\eta\), so \(y\) is closer to \(z\) than \(X\setminus V\) is. By hypothesis \(d(F^{mi}x,Z)\to0\) as \(i\to\infty\), so only finitely many indices \(i\) have \(F^{mi}x\notin V\). Choose \(k_x\geq1\) so large that
\[
\#\{0\leq i<k_x:\ F^{mi}x\notin V\}<\tau k_x .
\]
Let \(I_x=\{0\leq i<k_x:F^{mi}x\in V\}\) and \(O_x=\bigcap_{i\in I_x}(F^{mi})^{-1}(V)\). This is an open set containing \(x\), and every \(y\in O_x\) visits \(V\) at least at the times in \(I_x\); so \(y\) also has fewer than \(\tau k_x\) exceptional indices among its first \(k_x\). Finitely many sets \(O_{x_1},\ldots,O_{x_a}\) cover \(X\); put \(J=\max_bk_{x_b}\).

Now fix \(x\) and \(r\). Starting with \(x\), choose some \(O_{x_b}\) containing the current point, advance by \(k_{x_b}\) iterates of \(F^m\), and repeat from the point reached, as long as the next segment fits into the first \(r\) indices. The segments used cover the indices \(0,\ldots,r-\ell-1\) for some remainder \(0\leq\ell<J\). Each segment of length \(k\) contains fewer than \(\tau k\) exceptional indices, so together they contain at most \(\tau(r-\ell)\leq\tau r\); the remainder contains at most \(\ell<J\). This proves (3.1).

*Step 2: counting orbit descriptions.* Fix \(\tau\) and the corresponding \(J\), and let \(r\geq1\). To a point \(x\in X\) assign the following description of its first \(r\) blocks of length \(m\): the set \(S(x)=\{i<r:F^{mi}x\notin V\}\); for \(i\notin S(x)\), the first ball (in a fixed ordering) among the \(P\) balls about \(E\) that contains \(F^{mi}x\); for \(i\in S(x)\), the first ball among the \(Q\) covering balls that contains \(F^{mi}x\). By (3.1), \(|S(x)|\leq\tau r+J\), so the number of possible descriptions is at most
\[
2^r\,P^r\,Q^{\tau r+J}\tag{3.2}
\]
(\(2^r\) bounds the number of subsets, and \(P,Q\geq1\)). If \(x\) and \(y\) have the same description, then for each \(i<r\) the points \(F^{mi}x\) and \(F^{mi}y\) lie in one \(d_m\)-ball of radius \(\varepsilon/2\), so \(d(F^{mi+j}x,F^{mi+j}y)<\varepsilon\) for \(0\leq j<m\). That is, \(d_{mr}(x,y)<\varepsilon\). Hence an \((mr,\varepsilon)\)-separated set contains at most one point of each description:
\[
s_F(mr,\varepsilon)\leq2^rP^rQ^{\tau r+J}.
\]

*Step 3: limits.* For \(n\geq1\) put \(r=\lceil n/m\rceil\); then \(s_F(n,\varepsilon)\leq s_F(mr,\varepsilon)\) by Lemma 1.2(b), and \(r/n\to1/m\). Therefore
\[
\begin{aligned}
&h(F,\varepsilon)=\limsup_{n\to\infty}\frac1n\log s_F(n,\varepsilon)\\
&\quad \leq\frac{\log2+\log P(m)+\tau\log Q(m)}{m}.
\end{aligned}
\]
This holds for every \(\tau\in(0,1)\), with \(m\) fixed; letting \(\tau\downarrow0\) gives \(h(F,\varepsilon)\leq(\log2+\log P(m))/m\) for every \(m\geq1\). Now \(\frac1m\log P(m)=\frac1m\log s_Z(m,\varepsilon/4)\), and its upper limit as \(m\to\infty\) is \(h(F|_Z,\varepsilon/4)\leq h_{\mathrm{top}}(F|_Z)=0\). Taking the lower limit over \(m\) of the bound gives \(h(F,\varepsilon)\leq0\). As \(\varepsilon\) was arbitrary, \(h_{\mathrm{top}}(F)=0\). \(\square\)

**Remark 3.2.** The same conclusion follows from the variational principle: the hypothesis forces every invariant probability measure to live on \(Z\), and then all measure-theoretic entropies vanish. The direct proof above avoids measure theory and makes the role of compactness visible: it bounds the *proportion* of exceptional times uniformly, although it cannot bound the *last* exceptional time.

## 4. Radial register maps

Let \(\Sigma=\mathbb C\cup\{\infty\}\) be the Riemann sphere (its smooth structure is recalled in the next lesson; here only its topology matters: it is the one-point compactification of \(\mathbb C\), a compact metrizable space). For \(A>0\) let \(D_A=\{v\in\mathbb C:|v|\leq A\}\subseteq\Sigma\).

**Lemma 4.1 (radial maps have zero entropy).** Let \(T:\Sigma\to\Sigma\) be continuous with \(T(\Sigma)\subseteq D_A\), and suppose that
\[
\begin{gathered}
T(re^{i\theta})=R(r)e^{i\theta}\\
(0\leq r\leq A,\ \theta\in\mathbb R),
\end{gathered}
\]
where \(R:[0,A]\to[0,A]\) is continuous and nondecreasing with \(R(0)=0\). Then for every \(q\geq1\) the product map \(T^{\times q}(v_1,\ldots,v_q)=(Tv_1,\ldots,Tv_q)\) of \(\Sigma^q\) has zero topological entropy.

*Proof.* Fix a compatible metric \(d_\Sigma\) on \(\Sigma\) and give \(\Sigma^q\) the maximum metric. Fix \(\varepsilon>0\). The polar map \([0,A]\times S^1\to D_A\), \((r,u)\mapsto ru\), is continuous on a compact space, hence uniformly continuous (Lebl, Theorem 7.5.11). So there are partitions of \([0,A]\) into \(H\) half-open intervals and of \(S^1\) into \(K\) half-open arcs such that \(d_\Sigma(ru,r'u')<\varepsilon\) whenever \(r,r'\) lie in one interval and \(u,u'\) in one arc. Number the intervals from left to right and let \(b(r)\in\{1,\ldots,H\}\) be the number of the interval containing \(r\); then \(b\) is nondecreasing.

*Radius itineraries.* For \(N\geq1\) and \(r\in[0,A]\) consider the vector \(\iota_N(r)\in\{1,\ldots,H\}^N\) given by
\[
\begin{aligned}
&\iota_N(r)=\bigl(b(r),b(R(r)),\ldots,\\
&\qquad b(R^{N-1}(r))\bigr).
\end{aligned}
\]
Each \(R^j\) is nondecreasing, so each coordinate of \(\iota_N\) is a nondecreasing function of \(r\). Hence any two values of \(\iota_N\) are comparable coordinatewise: if \(r\leq r'\) then \(\iota_N(r)\leq\iota_N(r')\) in every coordinate. Listing the distinct values in increasing order of \(r\), the coordinate sum strictly increases at each change and stays between \(N\) and \(NH\). So \(\iota_N\) takes at most \(1+N(H-1)\) values. (This orders itineraries by their initial radii; it asserts nothing about monotonicity in time.)

*Orbits in the disc.* Write a point \(v\in D_A\) as \(v=ru\) with \(r=|v|\) and \(u\in S^1\), choosing \(u=1\) when \(v=0\). By induction \(T^jv=R^j(r)u\) for all \(j\geq0\), with the same \(u\): the radii \(R^j(r)\) stay in \([0,A]\), where \(T\) is given by the formula. If two points \(v=ru\), \(v'=r'u'\) of \(D_A\) have \(u,u'\) in one arc and \(\iota_N(r)=\iota_N(r')\), then \(d_\Sigma(T^jv,T^jv')<\varepsilon\) for \(0\leq j<N\). So length-\(N\) orbits of points of \(D_A\) have at most \(K(1+N(H-1))\) such descriptions.

*All of \(\Sigma^q\).* Cover \(\Sigma^q\) by \(C\) sets of diameter less than \(\varepsilon\) (finitely many suffice, by compactness). Let \(n\geq2\). Describe a point \(\mathbf v=(v_1,\ldots,v_q)\) by a set of this cover containing it, together with, for each coordinate \(k\), the description above of the point \(Tv_k\in D_A\) for \(N=n-1\). Two points with the same description are within \(\varepsilon\) at time \(0\) and, coordinatewise, at times \(1,\ldots,n-1\). Hence
\[
\begin{aligned}
&s_{T^{\times q}}(n,\varepsilon)\\
&\quad \leq C\bigl[K\bigl(1+(n-1)(H-1)\bigr)\bigr]^q,
\end{aligned}
\]
a polynomial in \(n\). Its logarithm divided by \(n\) tends to \(0\), so \(h(T^{\times q},\varepsilon)=0\) for every \(\varepsilon\). \(\square\)

The initial cover takes care of the points outside the disc, including \(\infty\), which need not move radially. The hypothesis that \(R\) is nondecreasing is essential (Exercise 5.3).

## 5. Exercises

**5.1.** Let \(F\) be an isometry of \((X,d)\). Show \(h_{\mathrm{top}}(F)=0\).

**5.2.** Let \(F(u)=u^2\) on the unit circle \(S^1\subseteq\mathbb C\), with the arc-length metric. Show that the \(2^n\) points \(e^{2\pi ik/2^n}\), \(0\leq k<2^n\), form an \((n,\varepsilon)\)-separated set for every \(\varepsilon<\pi/2\), and conclude \(h_{\mathrm{top}}(F)\geq\log2\).

**5.3.** Let \(T\) and \(R\) be as in Lemma 4.1 (with \(q=1\)). Show that every orbit of \(T\) converges, and that its limit lies on a circle \(\{|v|=r_*\}\) with \(R(r_*)=r_*\). Where would this argument fail if \(R\) were not nondecreasing?

**5.4.** Let \(d,d'\) be compatible metrics on a compact space \(X\), \(K\subseteq X\) compact, and \((x_n)\) a sequence. Show that \(d(x_n,K)\to0\) if and only if \(d'(x_n,K)\to0\).

**5.5.** In Theorem 3.1, why can one not simply choose a time \(N\) after which every orbit stays in \(V\)? Consider \(X=[0,1]\), \(F(x)=x^2\), \(Z=\{0,1\}\) and \(V=[0,\tfrac14)\cup(\tfrac34,1]\). Show that every orbit has at most three times outside \(V\), but that the last such time is unbounded as \(x\) ranges over \(X\).

## 6. Solutions

**5.1.** \(d_n=d\) for all \(n\), so \(s_F(n,\varepsilon)=s_F(1,\varepsilon)\) is bounded in \(n\).

**5.2.** For \(k\neq k'\), write \(k-k'=2^a\cdot c\) with \(c\) odd and \(0\leq a<n\). Then \(F^j\) multiplies arguments by \(2^j\); at \(j=n-1-a\) the two points have arguments differing by \(2\pi c\cdot2^{a+j}/2^n=\pi c\), i.e. they are antipodal, at arc distance \(\pi>\varepsilon\). So the set is \((n,\varepsilon)\)-separated and \(s_F(n,\varepsilon)\geq2^n\); hence \(h(F,\varepsilon)\geq\log2\).

**5.3.** Since \(T(\Sigma)\subseteq D_A\), it suffices to consider \(v=ru\in D_A\), where \(T^jv=R^j(r)u\). If \(R(r)\geq r\), then applying the nondecreasing map \(R\) repeatedly gives \(R^{j+1}(r)\geq R^j(r)\) for all \(j\); if \(R(r)<r\), the sequence decreases. In both cases \(R^j(r)\) is monotone and bounded, so it converges to some \(r_*\in[0,A]\), and continuity gives \(R(r_*)=r_*\). Hence \(T^jv\to r_*u\), a fixed point of \(T\). Without monotonicity the radii \(R^j(r)\) need not be monotone; for the tent map \(R(r)=1-|2r-1|\) on \([0,1]\) they can wander over the whole interval, and radius itineraries are no longer ordered by the initial radius, which was the key to the polynomial count in Lemma 4.1.

**5.4.** By uniform equivalence (proof of Proposition 1.3) for \(\varepsilon>0\) there is \(\delta>0\) with \(d'(x,y)<\delta\Rightarrow d(x,y)<\varepsilon\). If \(d'(x_n,K)<\delta\), pick \(y\in K\) with \(d'(x_n,y)<\delta\); then \(d(x_n,K)<\varepsilon\). So \(d'(x_n,K)\to0\) implies \(d(x_n,K)\to0\), and symmetrically.

**5.5.** Every orbit of a point \(x<1\) tends to \(0\), and \(1\) is fixed, so \(Z=\{0,1\}\) is attracting. An orbit is outside \(V\) exactly at the times \(k\) with \(\tfrac14\leq x^{2^k}\leq\tfrac34\). Once \(y=x^{2^k}\leq\tfrac34\), the condition \(y^{2^i}\geq\tfrac14\) means \(2^i\leq\log4/\log(1/y)\leq\log4/\log\tfrac43<5\), so \(i\leq2\): at most three exceptional times. For \(x=1-\delta\) the orbit stays in \((\tfrac34,1]\) while \((1-\delta)^{2^k}>\tfrac34\), that is for roughly \(\log_2(1/\delta)\) steps, before its exceptional times; so the last exceptional time is unbounded as \(\delta\downarrow0\). The proof of Theorem 3.1 uses only the bounded proportion of exceptional times, which is what survives in general.

## References

- [OpenAI-C1] OpenAI, *A \(C^1\) counterexample to the entropy conjecture*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026
- [Lebl] J. Lebl, *Basic Analysis II: Introduction to Real Analysis*, version 6.3; the text of the core course Real Analysis II. https://www.jirka.org/ra/
- [Fomberg] Y. Fomberg, *Algebraic Topology*, notes on lectures by Nir Lazarovich, Spring 2025; the homology part of the core course Algebraic Topology. https://yp.srht.site/notes/math/algebraic_topology.pdf
- [Gromov] M. Gromov, *Entropy, homology and semialgebraic geometry*, Séminaire Bourbaki, exposé 663 (1986), Numdam. https://www.numdam.org/item/SB_1985-1986__28__225_0/
- M. Shub (1974), A. Manning (1975), M. Misiurewicz and F. Przytycki (1977), Y. Yomdin (1987), R. Saghin and Z. Xia (2010), G. Liao, M. Viana and J. Yang (2013) are named for credit for the results quoted in Section 2; the course does not use them.
