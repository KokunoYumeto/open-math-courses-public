# Relative difference bundles, radial pairs and the planar normalization

This receiving proof supplies the relative-bundle inputs used by *Graded C\*-algebras, Clifford algebras and graded Hilbert modules*, Section 7, and *The Thom isomorphism for a vector bundle*. Every space in Sections 0–4 is compact Hausdorff; a closed subspace need not be a cofibration, a CW subcomplex, metrizable, or nonempty. Bundles have finite, locally constant complex rank, which may differ on different components. No relative-excision theorem, Bott-periodicity theorem, or Chern-character theorem is used to prove the relative correspondence.

For a unital C\*-algebra, \(K_0\) is the Grothendieck group of projections under direct sum and stable projection homotopy. For an ideal \(J\), use the forced unitization and
\[
K_0(J)=\ker\bigl(K_0(J^+)\longrightarrow K_0(\mathbb C)\bigr).
\]
We use the corresponding stable-unitary definition of \(K_1\). Matrix positive square roots and their continuous dependence are supplied by the actually earlier [continuous functional-calculus lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Theorem 5.1. All additional topological, bundle and relative constructions needed below are proved here. In particular an external strong-excision statement is not a proof input.

<a id="rk-topology"></a>
## 0. The compact-space extension tools

### Lemma RK.0. Shrinking, cutoffs and matrix extension

On a compact Hausdorff space \(X\), finite open covers have continuous subordinate partitions of unity with closed supports inside their members. A continuous real, complex or finite-matrix-valued function on a closed \(Y\subset X\) extends to \(X\). The same assertions apply to \(X\times[0,1]\) and its closed subspaces, including unions with an endpoint slice.

**Proof.** First \(X\) is normal. For a point \(x\) and a closed set \(F\) not containing it, choose disjoint neighborhoods of \(x\) and each point of \(F\), then intersect the finitely many neighborhoods of \(x\) and unite those of \(F\). Compactness gives these finite choices. Applying this point–closed-set separation to every point of one of two disjoint closed sets, then taking a finite union, separates the two sets by disjoint open neighborhoods. In particular, if \(K\subset U\) with \(K\) closed and \(U\) open, there is an open \(V\) with \(K\subset V\subset\overline V\subset U\).

For completeness the cutoff construction follows from this last inclusion. Given disjoint closed sets \(K,F\), successively choose open \(V_t\), indexed by dyadic rationals \(0<t<1\), so that \(K\subset V_t\), \(\overline V_s\subset V_t\) for \(s<t\), and \(\overline V_t\subset X\setminus F\). At each finite stage insert intermediate sets by the preceding shrinking property. Put \(f(x)=\inf\{t:x\in V_t\}\), with infimum \(1\) for the empty set. Then \(f=0\) on \(K\), \(f=1\) on \(F\). The identities
\(\{f<a\}=\bigcup_{t<a}V_t\) and
\(\{f>a\}=\bigcup_{t>a}(X\setminus\overline V_t)\)
show continuity. Thus \(1-f\) is a cutoff equal to one on \(K\) and zero on \(F\).

For a finite cover \(U_i\), choose, around each point, an open set whose closure lies in some \(U_i\), and take a finite subcover \(V_j\). Shrink once more to closed sets \(K_j\subset V_j\) still covering \(X\): choose finitely many smaller neighborhoods inside the \(V_j\) and group their closures. Cutoffs \(b_j\) equal to one on \(K_j\), with supports inside \(V_j\), have positive sum. The functions \(b_j/\sum b_j\), grouped by their containing \(U_i\), give the asserted partition.

Here is the extension argument rather than an appeal to an extension theorem. If \(g:Y\to[-M,M]\) is continuous, the two closed sets
\(\{g\le -M/3\}\) and \(\{g\ge M/3\}\) are disjoint closed subsets of \(X\). A cutoff between them gives \(h:X\to[-M/3,M/3]\), equal to the indicated endpoint on each set. Then \(\|g-h|_Y\|\le 2M/3\). Repeat on the residual function, with \(M\) replaced successively by \((2/3)^jM\). The uniformly convergent series of the \(h_j\) is continuous and extends \(g\). Its norm is at most \(M\). Complex functions are handled by their real and imaginary parts; matrices by their finitely many entries. For self-adjoint matrix data, extend the entries and replace the extension by its average with its adjoint. The cylinder is again compact Hausdorff. To check compactness directly, a finite selection from an open cover covers each compact vertical interval; shrinking its finitely many product neighborhoods gives a neighborhood of the base point whose entire vertical interval is covered by that selection. Finitely many such base neighborhoods cover compact X, giving a finite selection for the cylinder. Hausdorffness follows by separating coordinates. Thus the proof applies also to the stated cylinders and closed unions. \(\square\)

<a id="rk-bundle-projection"></a>
## 1. Bundles, projections and cylinder transport

### Lemma RK.1. The bundle–projection correspondence in the required generality

Every finite-rank complex bundle over compact Hausdorff \(X\) has a Hermitian metric, an isometric embedding in a finite trivial bundle, and an orthogonal complementary bundle. The Grothendieck group of bundles is naturally \(K_0(C(X))\). Bundle isomorphism and stable projection homotopy give the same classes; a bundle over \(X\times[0,1]\) has isomorphic endpoint restrictions.

**Proof.** The local ranks have finitely many values, because their clopen level sets cover a compact space. All constructions below may therefore be made on those finitely many clopen sets and padded to a common finite ambient dimension. Choose a finite trivializing cover and the partition \(\rho_j\) of Lemma RK.0. The sum of the local Hermitian metrics weighted by \(\rho_j\) is a positive Hermitian metric; terms with support inside a chart extend by zero. Continuous Gram–Schmidt gives orthonormal local frames. In those frames the map
\[
i(v)=\bigl(\sqrt{\rho_j(x)}\,v_j\bigr)_j,\qquad v\in E_x,
\]
is continuous, isometric, and injective. Thus \(p(x)=i_xi_x^*\) is a continuous projection in some \(M_N(C(X))\). Its range is \(E_x\), and the range of \(1-p(x)\) is its orthogonal complement.

Conversely, if \(p(x)\) is a continuous projection, its ranges form a bundle. Indeed, near \(x_0\) one has \(\|p(x)-p(x_0)\|<1\), and projection from one range to the other is injective in both directions: if \(p(x_0)v=v\) and \(p(x)v=0\), then \(\|v\|\le\|p(x)-p(x_0)\|\|v\|\), so \(v=0\). The finite-dimensional ranges have equal dimension and the projected basis at \(x_0\) is a continuous local frame.

We record the precise transport used for homotopies. For projections \(p,q\) with \(\|p-q\|<1\), set
\[
t=qp+(1-q)(1-p),\qquad
u=t(t^*t)^{-1/2}.
\]
The two summands send the \(p\)-range and its complement into the \(q\)-range and its complement. On each the map is bounded below by \(1-\|p-q\|\); the same holds for \(t^*\). Thus \(t\) is invertible, \(u\) is unitary, \(up=qu\), and these formulas vary continuously. A projection on \(X\times[0,1]\) is uniformly continuous in the interval variable in supremum norm: a finite subcover of \(X\) proves the uniform assertion from joint continuity. Divide the interval into finitely many segments on which projections are close. Successive transports give a continuous unitary \(u_t\) with \(u_0=1\) and \(u_tp_0u_t^*=p_t\). This proves cylinder transport after embedding the cylinder bundle in a trivial bundle.

Two isometric embeddings of the same bundle give the path of isometric embeddings
\[
i_s=\cos s\,i_0\oplus\sin s\,i_1,\qquad 0\le s\le\pi/2.
\]
The endpoint projections are the two original ones with zero padding; a path of constant scalar unitaries rearranges their blocks. Changing the metric is harmless: join metrics by their positive convex combination and normalize the embeddings continuously. An isomorphism lets us use the same bundle for this comparison. Conversely projection homotopy gives isomorphic endpoint bundles by the transport just proved. Direct sums of projections are direct sums of bundles. Taking Grothendieck groups proves the assertion about \(K_0\), including nonconstant rank and naturality under pullback. \(\square\)

We also use the following consequence of the definition of \(K_0\). For any unitary \(v\) in a unital matrix algebra, \(p\) and \(vpv^*\) have equal stable projection classes. With
\(R_s=\begin{psmallmatrix}\cos s&-\sin s\\ \sin s&\cos s\end{psmallmatrix}\),
the unitary path
\[
R_s\begin{pmatrix}v&0\\0&1\end{pmatrix}R_s^*
\begin{pmatrix}1&0\\0&v^*\end{pmatrix}
\]
starts at \(\operatorname{diag}(v,v^*)\) and ends at \(1\). Conjugating \(p\oplus0\) by this path proves the claim. In a finite scalar matrix algebra every unitary is itself path connected to one: diagonalize it and replace each eigenvalue \(e^{i\theta}\) by \(e^{it\theta}\).

<a id="rk-unitary-extension"></a>
### Lemma RK.2. Extending a unitary which is homotopic to one

If \(Y\subset X\) is closed and \(w:Y\to U(N)\) is joined to \(1\) by a continuous unitary path, it has a continuous unitary extension \(U:X\to U(N)\).

**Proof.** View the path \(w_t\) in \(C(Y,M_N)\); compactness makes it continuous in supremum norm. Choose a finite partition \(t_j\) with
\(\|w_{t_{j+1}}w_{t_j}^*-1\|<1\). On this ball the convergent power series for \(\log(1+z)\) gives a continuous logarithm of the unitary; equivalently the finite-matrix spectral calculus gives its eigenvalue arguments in \((-\pi/2,\pi/2)\). Thus
\[
w_{t_{j+1}}w_{t_j}^*=\exp(ih_j)
\]
with \(h_j\) self-adjoint. Extend \(h_j\) to a self-adjoint matrix \(H_j\) on \(X\) by Lemma RK.0. The ordered product
\(U=\exp(iH_{m-1})\cdots\exp(iH_0)\)
restricts to \(w\). The same proof works on any compact cylinder with its closed subspace; it does not assume that an arbitrary unitary on \(Y\) extends. \(\square\)

<a id="rk-difference"></a>
## 2. The complete relative difference-bundle theorem

Let \(\mathcal D(X,Y)\) be the group generated by triples
\[
(E,F,\sigma),\qquad \sigma:E|_Y\longrightarrow F|_Y
\]
with \(\sigma\) a specified bundle isomorphism. Impose isomorphism, direct-sum addition, and endpoint equality for triples over the compact cylinder pair. A triple is zero if its comparison extends to an isomorphism over \(X\). These are exactly the difference-bundle relations; comparison data, rather than just equal restriction classes, are required.

### Theorem RK.3. Relative bundles equal the operator ideal group

For every compact Hausdorff \(X\) and closed \(Y\),
\[
\mathcal D(X,Y)\ \cong\ K_0\bigl(C_0(X\setminus Y)\bigr).
\]
This isomorphism is natural under maps of compact pairs. Its forgetful map to \(K_0(C(X))\) sends the triple to \([E]-[F]\).

**Proof.** Put \(J=C_0(X\setminus Y)\). Extension by zero identifies \(J\) with
\(\{f\in C(X):f|_Y=0\}\): for a function vanishing at infinity, each set \(\{|f|\ge\varepsilon\}\) is compact inside \(X\setminus Y\), so its zero extension is continuous at \(Y\); the converse follows by compactness of these level sets. If \(Y=\varnothing\), comparison data are empty and the defining group is the bundle Grothendieck group. Here the forced unitization of the already unital algebra \(J=C(X)\) is \(C(X)\oplus\mathbb C\), through \((a,\lambda)\mapsto(a+\lambda1,\lambda)\); its scalar-kernel group is exactly \(K_0(C(X))\). Projections and stable homotopies in a direct sum are coordinatewise, proving that kernel assertion. Lemma RK.1 therefore proves the empty-subspace case without representing the forced unitization faithfully inside \(C(X)\). If \(X=\varnothing\), all groups vanish. Hence assume \(Y\ne\varnothing\). The forced unitization \(J^+\) is now represented faithfully by the functions on \(X\) which are constant on \(Y\); its scalar map is that constant.

We first construct a map
\(\Phi:K_0(J)\to\mathcal D(X,Y)\).
An element is represented by \([p]-[q]\) with projections over \(J^+\) whose scalar projections \(p_0,q_0\) have equal rank. Pad them to one matrix size. Choose a constant partial isometry \(v_0\) from \(p_0\) to \(q_0\), and take
\[
\Phi([p]-[q])=(\operatorname{ran}p,\operatorname{ran}q,v_0).
\]
Different choices of \(v_0\) differ by a unitary of the common finite-dimensional range, whose unitary group is path connected by the scalar diagonalization above. They are therefore homotopic comparisons. In a projection homotopy the scalar projections are transported continuously by Lemma RK.1, so the scalar comparison can also be chosen continuously. Direct sums give addition; adding the same projection to \(p\) and \(q\) adds the zero triple with its global identity comparison. These checks are precisely the stable-homotopy and Grothendieck relations defining \(K_0(J)\), so \(\Phi\) is well defined.

We construct its inverse explicitly and check all its choices. Give \(E,F\) metrics and isometric finite embeddings with projections \(p,q\in M_N(C(X))\). The polar comparison
\[
u=\sigma(\sigma^*\sigma)^{-1/2}
\]
is a unitary from \(E|_Y\) to \(F|_Y\); its embedded matrix satisfies \(u^*u=p|_Y\), \(uu^*=q|_Y\). The positive factor can be interpolated to one, through invertibles, so replacing \(\sigma\) by \(u\) is an allowed homotopy. On \(Y\) the matrix
\[
W=\begin{pmatrix}1-p&u^*\\u&1-q\end{pmatrix}
\]
is self-adjoint and squares to one: the off-diagonal products vanish since \(u=qup\). It sends the range of \(p\oplus0\) onto the range of \(0\oplus q\). Moreover
\[
\exp\!\left(i\pi t\,\frac{1-W}{2}\right),\qquad 0\le t\le1,
\]
is a path from \(1\) to \(W\). Lemma RK.2 therefore supplies a global unitary lift \(U\) of \(W\). Define projections over \(C(X)\) by
\[
R=U(p\oplus0)U^*,\qquad S=0\oplus q.
\]
They agree on \(Y\). The following rebasing unitary uses the global projection \(S\):
\[
T(S)=\begin{pmatrix}S&1-S\\1-S&-S\end{pmatrix},\qquad
P=T(S)\bigl(R\oplus(1-S)\bigr)T(S)^*,\qquad
P_*=\operatorname{diag}(1_{2N},0_{2N}).
\]
One has \(T(S)^*=T(S)\), \(T(S)^2=1\), and
\(T(S)(S\oplus(1-S))T(S)^*=P_*\).
Consequently \(P|_Y=P_*\), so \(P-P_*\in M_{4N}(J)\). Put
\[
\Psi(E,F,\sigma)=[P]-[P_*]\in K_0(J).
\]

If \(U_0,U_1\) lift the same \(W\), the unitary \(V=U_1U_0^*\) restricts to one on \(Y\). It belongs to the matrix unitization of \(J\), and conjugates \(R_0\) to \(R_1\). After rebasing, the corresponding unitary is
\(T(S)(V\oplus1)T(S)^*\), which also restricts to one. Hence the two \(P\)'s have equal \(K_0(J)\) classes by the unitary-conjugation path above.

Embedding choices are joined, after padding, by the isometric-embedding rotation of Lemma RK.1, and metric choices by its metric interpolation. The resulting \(p,q,u,W\) are continuous over the compact cylinder. Apply Lemma RK.2 to the pair \((X\times[0,1],Y\times[0,1])\): the displayed exponential makes the cylinder \(W\) homotopic to one. A lift on this cylinder gives a projection path with boundary constantly \(P_*\). The preceding lift-independence check identifies its endpoints with any originally chosen lifts. Isomorphic triples are covered by transporting their embeddings through the isomorphisms. A homotopy of triples is covered by embedding the actual cylinder bundles. Direct sums make block sums of all these matrices, after a constant permutation. Zero padding of \(p,q\) adds zero blocks to \(R,S\) and identity blocks to \(1-S\); after the same constant permutation it therefore adds equal constant projections to \(P\) and \(P_*\), contributing zero to their difference. This checks the padding used in the embedding rotations. If \(\sigma\) extends globally, its global polar isometry makes the same \(W\) a global unitary; choose \(U=W\). Then \(R=S\), \(P=P_*\), and \(\Psi=0\). Thus \(\Psi\) respects every defining relation of \(\mathcal D(X,Y)\).

Here are both inverse checks. For an original triple the map \(U\) identifies \(E\) with \(\operatorname{ran}R\), while the lower-block embedding identifies \(F\) with \(\operatorname{ran}S\). On \(Y\),
\[
U(e,0)=W(e,0)=(0,ue).
\]
Thus the comparison of these two range bundles is the identity on their common boundary range. Add their common complement \(\operatorname{ran}(1-S)\), a zero triple, and conjugate both bundles by \(T(S)\). This is exactly
\((\operatorname{ran}P,\operatorname{ran}P_*,\mathrm{id})\).
It proves \(\Phi\Psi(E,F,\sigma)=(E,F,\sigma)\), including the specified comparison, not merely its forgetful class.

Conversely, for \([p]-[q]\) over \(J^+\), the boundary \(W\) is a constant matrix. Choose that constant matrix as \(U\). All rebasing matrices then belong to matrix algebras over \(J^+\). Within \(K_0(J^+)\),
\[
[P]-[P_*]=[R]+[1-S]-[S]-[1-S]=[p]-[q].
\]
The equality uses only unitary conjugation, direct sums and cancellation. Both sides lie in the scalar kernel, proving \(\Psi\Phi=1\). The same computation over \(C(X)\) gives the forgetful class \([p]-[q]=[E]-[F]\).

For a map of compact pairs, pulling back any chosen matrices gives permissible choices for the pulled-back construction. Choice independence proves naturality. This also covers \(Y=X\), where \(J=0\) and every comparison is already global. \(\square\)

<a id="rk-collapse"></a>
### Corollary RK.3a. Quotients and compact support

For nonempty closed \(Y\), the quotient \(X/Y\) is compact Hausdorff and is the one-point compactification of \(X\setminus Y\). Thus
\[
K_0(C_0(X\setminus Y))
=\ker\bigl(K_0(C(X/Y))\longrightarrow K_0(\mathbb C)\bigr).
\]
The construction in Theorem RK.3 gives actual bundle differences on this quotient: the matrix \(P\), constant on \(Y\), descends to a projection on \(X/Y\).

**Proof.** Compactness follows from the quotient map. Two points outside \(Y\) are separated by disjoint neighborhoods which can also avoid \(Y\). A point outside \(Y\) and the collapsed point are separated by normality between that point and the closed set \(Y\); taking the complementary closed neighborhood gives saturated separating neighborhoods. This proves Hausdorffness. A neighborhood of the collapsed point has compact complement inside \(X\setminus Y\); conversely the complement of any compact subset of \(X\setminus Y\) is such a neighborhood. This is precisely the one-point compactification topology. Functions on the quotient are exactly functions constant on \(Y\), already identified with \(J^+\). The scalar evaluation and projection description now prove the assertion. No good-pair or cofibration hypothesis was used. \(\square\)

<a id="rk-radial"></a>
## 3. Radial disc/sphere pairs and bundle symbols

### Theorem RK.4. The arbitrary compact-base radial identification

Let \(V\to X\) be a finite-rank real or complex Euclidean bundle over a compact Hausdorff base, with closed unit ball and unit sphere bundles \(B(V),S(V)\). Then
\[
v\longmapsto\frac{v}{\sqrt{1+\|v\|^2}}
\]
is a proper homeomorphism
\(V\to B(V)\setminus S(V)\), with inverse
\(w\mapsto w/\sqrt{1-\|w\|^2}\).
For \(i=0,1\) it therefore gives
\[
K_i(C_0(V))\cong K_i(C_0(B(V)\setminus S(V))).
\]
In degree zero Theorem RK.3 identifies the right group with the specified difference-bundle triples for the disc/sphere pair.

**Proof.** A finite isometric bundle embedding, proved over real scalars by exactly the same partition and Gram–Schmidt argument as Lemma RK.1, realizes every bounded ball bundle as the closed subset
\(\{(x,z):p(x)z=z,\ \|z\|\le R\}\)
of a compact \(X\) times a finite-dimensional closed ball. Thus it is compact. The sphere is closed in it, and the total vector bundle is locally compact. The two displayed formulas are continuous in each trivialization, preserve the base point, and are inverse by direct substitution. They glue because the norm is intrinsic. A homeomorphism is proper: the inverse sends compact sets to compact sets. Pullback is consequently an isometric *-isomorphism of the vanishing-at-infinity function algebras, giving both group identifications from their definitions. Rank-zero components have empty sphere and identity radial map on their zero bundle; no exception is needed. \(\square\)

<a id="rk-symbol-rules"></a>
### Corollary RK.4a. The exact symbol rules used by the consumers

For bundles \(E^+,E^-\) over \(B(V)\), an isomorphism
\(\sigma:E^+|_{S(V)}\to E^-|_{S(V)}\) defines an element of \(K_0(C_0(V))\). Its image under restriction to the zero section is
\([s^*E^+]-[s^*E^-]\). A homotopy through boundary-invertible symbols preserves the class. An everywhere invertible comparison has zero class. Tensoring both bundles and the comparison with a bundle pulled back from \(X\) defines the \(K^0(X)\)-action on these relative symbols.

**Proof.** The first assertion is the preceding theorem followed by RK.3. Forgetting the comparison, then pulling back along the zero section, gives the stated difference by RK.3's forgetful formula and naturality. A boundary-invertible homotopy is an actual triple on the cylinder pair, one of the defining relations. An everywhere invertible comparison is the global extension relation. Tensor product respects isomorphism, sums, cylinder homotopy and global extension, so it descends to the bundle Grothendieck group in each variable. Lemma RK.1 identifies the absolute action with \(K_0(C(X))\); projection tensor products have precisely the tensor-product range bundles.

In particular the Clifford symbol \(c(v)^+:S^+\to S^-\), with inverse \(\|v\|^{-2}c(v)^-\) on the sphere, is such a triple. The ball homotopy in the graded Clifford lesson, equation (7.4), is boundary fixed and ends in an everywhere invertible map; the relative-zero conclusion follows from these relations alone. For a complex line \(L\), the symbol
\[
(\mathbf1,\pi^*L,\ \lambda\longmapsto\lambda v)
\]
on \((B(L),S(L))\) is a specified comparison: at a unit vector \(v\) it is a unitary map onto \(L_x\). Its zero-section difference is \(1-[L]\). For \(S=\Lambda^*E\) the corresponding zero-section difference is \(\sum_j(-1)^j[\Lambda^jE]\). These assertions use the actual comparisons and do not follow just from the two bundles having equal rank. \(\square\)

<a id="rk-low-dimensional-unitaries"></a>
## 4. The elementary homotopy calculations needed on the plane and sphere

### Lemma RK.5. Loops and two-spheres in finite unitary groups

Every loop \(g:S^1\to U(n)\) is homotopic to
\(\operatorname{diag}(z^k,1,\ldots,1)\), where \(k\) is the winding of \(\det g\); two loops are homotopic exactly when these integers agree. Every map \(S^2\to U(n)\) is nullhomotopic.

**Proof.** We give the small amount of sphere topology and lifting required by these statements. If \(d=1,2\) and \(m>d\), every map \(f:S^d\to S^m\) is nullhomotopic. Take a fine finite triangulation of the domain: regular polygon subdivision gives it for \(S^1\); subdividing the faces of an octahedron and projecting radially gives arbitrarily small triangles on \(S^2\). The radial maps on the finitely many original closed faces have bounded derivatives, so refinement indeed makes their diameters tend to zero. Uniform continuity of \(f\) makes the values at all vertices of a simplex as close as desired to every value of \(f\) on that simplex. Interpolate the vertex values linearly and normalize to length one. Their closeness ensures that no interpolated vector is zero, that the resulting map \(f'\) is uniformly close to \(f\), and that normalized straight interpolation from \(f\) to \(f'\) is a homotopy. On each simplex the image of \(f'\) lies in the sphere of the real linear span of at most \(d+1\) vertex vectors. Finitely many such proper subspaces do not cover \(\mathbb R^{m+1}\): choose a nonzero linear functional vanishing on each subspace; the product of these functionals is a nonzero polynomial and cannot vanish everywhere. Thus there is a point of \(S^m\) missed by \(f'\). Stereographic projection from that point identifies its complement with \(\mathbb R^m\), where \(f'\) contracts. This proves the assertion. In particular every loop on \(S^2\) contracts. A free contraction can be made a based contraction by adjoining the path traced by its base point before each loop and the reverse path after it; the final retraced path contracts. Thus \(S^2\) is simply connected.

A path into \(U(1)\) has a continuous real argument: partition its parameter interval into pieces whose images, after division by the initial value, lie in the open semicircle about one, take the continuous argument there, and continue from the preceding endpoint. For a loop, the change in argument is \(2\pi k\). It is homotopy invariant: for sufficiently nearby loops the same finite partition and argument branches give continuously varying endpoint changes, and the integer-valued change must be constant; a finite subdivision in the homotopy parameter proves the claim. A loop with argument \(\theta(t)\) is homotopic, through loops, to
\(\exp(i(\theta(0)+2\pi kt))\)
by linear interpolation of its argument. A constant scalar factor is joined to one. This proves the loop statement for \(U(1)\). For a map \(S^2\to U(1)\), continue the argument along paths from a fixed base point. Path independence follows because loops in \(S^2\) contract and the argument change is invariant during such a contraction. The resulting argument is continuous: on a sufficiently small neighborhood its values are the local argument branch plus a fixed multiple of \(2\pi\). Scaling this global argument contracts the map.

We now reduce higher unitary groups to this scalar case, proving the needed lifting instead of invoking a fibration theorem. For unit vectors \(a,b\in\mathbb C^n\) whose range projections \(p=aa^*,q=bb^*\) satisfy \(\|p-q\|<1\), set
\[
t(b,a)=ba^*+(1-q)(1-p),\qquad
C(b,a)=t(b,a)\bigl(t(b,a)^*t(b,a)\bigr)^{-1/2}.
\]
On the line of \(a\) the first map sends \(a\) to \(b\); on its complement it is the close-projection map into the complement of \(b\). The lower bound and adjoint bound in RK.1 make it invertible. Since \(t^*t\,a=a\), the unitary \(C(b,a)\) sends \(a\) exactly to \(b\), and the formula depends continuously on the two vectors.

Let \(g:Z\to U(n)\), with \(Z=S^1\) or \(S^2\) and \(n\ge2\). Its first column \(a_0:Z\to S^{2n-1}\) contracts to the constant first coordinate vector by the sphere argument, since \(2n-1>\dim Z\). Write this contraction as \(a_s\). Uniform continuity in \(s\) and a finite partition allow us to construct a homotopy of unitary matrices starting at \(g\): on a segment beginning at \(s_j\), left multiply its current value at \(s_j\) by \(C(a_s,a_{s_j})\). The formulas agree at the segment endpoints and have first column \(a_s\). At the end the unitary fixes the first coordinate and is \(\operatorname{diag}(1,h)\), with \(h:Z\to U(n-1)\). Induction reduces it to a scalar map.

For loops the determinant winding is unchanged during these homotopies and equals the winding of that final scalar loop. Hence the scalar classification proves both existence and uniqueness of the asserted loop normal form; a constant unitary path moves the nontrivial coordinate to the first position. For \(Z=S^2\), the scalar endpoint is nullhomotopic by the preceding global-argument proof, giving the second assertion. If a based nullhomotopy of a unitary map is required, replace a homotopy \(H_s(x)\) by \(H_s(x_0)^*H_s(x)\). When the original map is one at \(x_0\), this leaves its initial map unchanged and keeps that point fixed throughout. \(\square\)

<a id="rk-planar-bott"></a>
## 5. The actual planar projection and its comparison sign

### Theorem RK.6. Planar relative normalization

Use the complex orientation \(z=x+iy\). The relative triple
\[
\mathfrak b=(\mathbf1,\mathbf1,z)
\quad\text{on }(D^2,S^1)
\]
corresponds, under the radial identification of RK.4, to
\[
[q]-[P],\qquad
q(\zeta)=\frac1{1+|\zeta|^2}
\begin{pmatrix}1&\overline\zeta\\\zeta&|\zeta|^2\end{pmatrix},
\qquad P=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
This is the positive planar Bott class in the stated comparison convention. It generates \(K_0(C_0(\mathbb R^2))\cong\mathbb Z\), while \(K_1(C_0(\mathbb R^2))=0\). The comparison \(\overline z\) gives its negative.

**Proof.** In the construction of RK.3 take \(p=q=1\). The boundary involution is
\(\begin{psmallmatrix}0&\overline z\\z&0\end{psmallmatrix}\).
On the closed disc the following is an explicit unitary lift:
\[
U(w)=
\begin{pmatrix}
\sqrt{1-|w|^2}&\overline w\\
w&-\sqrt{1-|w|^2}
\end{pmatrix}.
\]
It is self-adjoint and its square is one, including on the boundary. Thus \(R=U\operatorname{diag}(1,0)U^*\) is the range projection of
\((\sqrt{1-|w|^2},w)\), and \(S=P\) is constant. The rebasing unitary in RK.3 is also constant, so the resulting relative class is \([R]-[P]\). Under
\(\zeta=w/\sqrt{1-|w|^2}\)
its range is \(\mathbb C(1,\zeta)\), which is exactly the displayed \(q(\zeta)\). This radial identification preserves complex orientation: it preserves angle, and its radial coordinate \(r/\sqrt{1-r^2}\) has positive derivative; the radial and angular Jacobian factors are both positive. At infinity \(q\) tends to \(P\), so \(q-P\) is a matrix over \(C_0(\mathbb R^2)\). This proves the projection formula and its sign by an actual lift.

We also prove its generating assertion locally. Every bundle on a disc is trivial: a projection for it is homotoped by \(p(x)\mapsto p(tx)\) to its constant central value, and RK.1 transports the bundle along this homotopy. In a disc/sphere triple the two trivial bundles consequently have the same rank, and the comparison is a loop in \(GL_n(\mathbb C)\). Its polar homotopy reduces it to \(U(n)\). By RK.5 that loop is homotopic to \(\operatorname{diag}(z^k,1,\ldots,1)\). Its determinant winding is additive on sums and zero for a globally extendible comparison, since a disc extension contracts the loop. Thus winding is a well-defined map of the difference-bundle group to \(\mathbb Z\), and its normal form proves that it is an isomorphism, taking \(\mathfrak b\) to one. RK.3 and RK.4 prove the stated \(K_0\) result, with no Bott theorem as a premise. Inverting or conjugating the scalar comparison changes \(k\) to \(-k\).

Finally a unitary in the forced unitization of \(C_0(\mathbb R^2)\) with scalar part one is a based map from the one-point compactification \(S^2\) to \(U(n)\). RK.5 contracts it through based unitary maps. General scalar parts may be normalized to one by a path of constant scalar matrices. The stable-unitary definition of \(K_1\) therefore gives zero. \(\square\)

<a id="rk-line-sign"></a>
### Lemma RK.6a. The tautological line and first Chern sign

The range of the preceding projection on the compactified plane is the tautological line \(L\) on \(\mathbb{CP}^1\), using the chart
\(\zeta\mapsto[1:\zeta]\). Its first Chern number in the complex orientation is \(-1\). Consequently
\[
\mathfrak b=[L]-[1],\qquad
u=1-[L]=-\mathfrak b
\]
as reduced classes on that sphere. The relative line Thom comparison
\(\lambda\mapsto\lambda v\) restricts in a unitary fibre frame to \(z\), and therefore has precisely the positive relative class of RK.6, not the class specified by \(\overline z\).

**Proof.** The chart formula already identifies the range with the line spanned by \((1,\zeta)\); at infinity it is the line spanned by \((0,1)\). On the other chart put \(w=1/\zeta\), with frame \((w,1)\). Along the equator \(|\zeta|=1\),
\[
(1,\zeta)=\zeta(w,1).
\]
Thus a vector with northern coefficient \(\lambda\) has southern coefficient \(\zeta\lambda\). The positively oriented boundary coordinate of the southern complex disc is \(w\), and \(\zeta=w^{-1}\). The obstruction to extending the northern nonzero section across that disc is therefore the degree \(-1\) of its southern boundary coefficient. This is the first Chern integer of a complex line: equivalently it is the Euler obstruction of its underlying oriented real plane. This convention can be defined directly by that obstruction on the two-cell sphere. It is independent of the frames, because a frame change extending over a disc has boundary degree zero. Tensoring lines adds their boundary degrees, and dualizing reverses them. In particular a line with first Chern class \(k h\) on the complex-oriented sphere, with \(\langle h,[S^2]\rangle=1\), has clutching degree \(-k\).

There is also a direct differential check of this same normalization. The unit frame \(s=(1,\zeta)/\sqrt{1+|\zeta|^2}\) has unitary connection form
\[
s^*ds=\frac{i(x\,dy-y\,dx)}{1+x^2+y^2},
\qquad
d(s^*ds)=\frac{2i\,dx\wedge dy}{(1+x^2+y^2)^2}.
\]
With the convention \(iF/(2\pi)\), its integral is
\(-\pi^{-1}\int_{\mathbb R^2}(1+|\zeta|^2)^{-2}\,dx\,dy=-1\);
polar coordinates give the integral \(\pi\). This is a check of the transition obstruction just computed, not an appeal to a Chern–Weil theorem to identify a bundle.

The constant projection \(P\) has the trivial range line, so the formula for \(\mathfrak b\) follows. A unitary local fibre frame writes \(v=z e\) and \(\lambda v=z\lambda e\), giving the stated comparison. Its zero-section difference remains \(1-[L]\), by RK.4a: the sign of the fibre comparison and the sign of the zero-section difference are different pieces of specified data. \(\square\)

<a id="rk-sphere-ring"></a>
## 6. The integral sphere ring used by the line-bundle example

### Theorem RK.7. The groups and relation on \(\mathbb{CP}^1\)

With \(L\) tautological and \(u=1-[L]\),
\[
K^0(\mathbb{CP}^1)=\mathbb Z[1]\oplus\mathbb Z u,\qquad
K^1(\mathbb{CP}^1)=0,\qquad u^2=0.
\]
Line bundles on this sphere are classified by their first Chern integer. A line \(E_k\) with \(c_1(E_k)=k h\) satisfies \(E_k\cong L^{\otimes(-k)}\) and
\([E_k]=[1]+k u\).

**Proof.** Write the sphere as two closed discs with a collar of the common circle. A bundle is trivial on each disc by RK.6's disc argument, so their trivializations identify it with a bundle glued by a loop \(g:S^1\to GL_n(\mathbb C)\). Such gluing really is locally trivial near the equator: enlarge each hemisphere into the collar and extend \(g\) constantly in the collar's transverse coordinate, giving overlapping product trivializations.

A homotopy of gluing maps constructs the same bundle over the sphere times an interval, so RK.1 makes its endpoints isomorphic. Changing either disc trivialization multiplies \(g\) by a map which extends over that disc; its boundary loop contracts by radial contraction, followed if necessary by a constant matrix path. Thus the gluing homotopy class is unchanged. Conversely an isomorphism of the bundles gives exactly such two trivialization changes. This proves the gluing classification without importing a classification theorem. Polar homotopy and RK.5 show that rank \(n\ge1\) bundles on the sphere are classified by their determinant winding \(k\), and each is isomorphic to the line glued by \(z^k\) plus \(n-1\) trivial lines. Rank and winding add under direct sum. Every integer occurs already for a line. Their bundle Grothendieck group is therefore \(\mathbb Z^2\), with basis the trivial line and \(L-[1]\), or equivalently the trivial line and \(u\). For line bundles, RK.6a identifies the first Chern integer as the negative of the gluing winding, proving the stated line classification.

We prove the ring relation integrally and explicitly. For scalar loops \(f,g\), the unitary path
\[
\begin{pmatrix}f&0\\0&1\end{pmatrix}
R_t
\begin{pmatrix}1&0\\0&g\end{pmatrix}
R_t^*,\qquad 0\le t\le\pi/2,
\]
starts at \(\operatorname{diag}(f,g)\) and ends at
\(\operatorname{diag}(fg,1)\). Set \(f=g=z\) and use the gluing classification. It gives an actual bundle isomorphism
\[
L\oplus L\ \cong\ L^{\otimes2}\oplus\mathbf1.
\]
Hence \(u^2=(1-[L])^2=1-2[L]+[L]^2=0\) in the integral bundle ring. There is no rational-injectivity or torsion argument in this proof. Since \([L]=1-u\) and \(u^2=0\), its integer positive and negative powers give
\([L]^{-k}=1+ku\), proving the formula for \(E_k\).

The stable-unitary definition of \(K^1(\mathbb{CP}^1)\) is the group of stable homotopy classes of maps from this sphere to finite unitary groups. RK.5 makes every such map nullhomotopic, so that group is zero. \(\square\)

<a id="rk-line-classification"></a>
### Lemma RK.7a. The line-bundle identifications valid on arbitrary compact bases

Every complex line bundle over a compact Hausdorff \(X\) is a pullback of the tautological line on some finite \(\mathbb{CP}^{N-1}\). The classifying map supplied by a finite embedding is independent, up to homotopy after enlarging \(N\), of the embedding. Its tensor and dual bundles have respectively the product and inverse transition functions. In particular none of these assertions says that singular \(H^2(X;\mathbb Z)\) classifies line bundles on an arbitrary compact Hausdorff base.

**Proof.** The finite embedding of RK.1 sends each fibre to a line in \(\mathbb C^N\). Its projection matrix is continuous, so the associated line is a continuous map into projective space: locally choose a projected coordinate vector which is nonzero and use its coordinate ratios as a projective chart. Pulling back the tautological line gives exactly the original embedded bundle. The orthogonal-sum rotation of RK.1 joins any two such maps after enlarging the ambient dimension. A unitary local frame has transitions in \(U(1)\). Tensor frames multiply these scalars; dual frames invert them, and evaluation identifies \(L\otimes L^*\) with the trivial line. This proves precisely the identifications used by the relative line symbols and finite projective-space pullbacks. \(\square\)

<a id="rk-source-scope"></a>
## Source comparison, licence and remaining scope

The actually read free primary comparison is A. Hatcher, *Vector Bundles & K-Theory*, Version 2.2, November 2017: Propositions 1.2–1.4 for metrics, complements and finite embeddings; Theorem 1.6 and the compact-base portion of Proposition 1.7 for cylinder bundles; Example 1.10 and Proposition 1.11 for clutching; Example 1.13 for the integral line relation; Section 2.1's definitions for locally constant rank and bundle group completion. The [author's download page](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html) identifies the edition and links the [actual free PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). Its copyright page states author copyright, 2003. No open licence is inferred for that PDF, and its copyright is retained.

The actual free corrected second edition of B. Blackadar, [*K-Theory for Operator Algebras*](https://www.bruceblackadar.com/Mathematics/book6.pdf), Section 5.4, supplies a comparison of relative-group definitions. That text explicitly omits a proof of strong excision, Theorem 5.4.2. The complete inverse maps, unitary extension, lift-choice checks and injectivity needed in this compact-space setting are proved in RK.0–RK.3 here; the omitted external theorem is not used. The source retains its author copyright and the usage terms on the [author's publication page](https://www.bruceblackadar.com/mathpubs.html).

This fresh capsule's original text is CC0. Its proofs cover every compact Hausdorff closed pair, all finite-rank Euclidean radial pairs over such bases, the relative symbol relations, the precise planar projection and line sign, the integral \(\mathbb{CP}^1\) groups and ring relation, and the stated finite-projective-space line identification. It does not claim a general coefficient Bott isomorphism, the full Atiyah–Bott–Shapiro theorem, the rational relative Chern-character theorem, the cohomological projective-bundle/splitting theorem, or the cohomological Thom isomorphism. In particular the broader Section 8 character and Todd-factor proof in the Thom consumer still requires eligible, delivered proofs of those cohomological providers. The analytic Thom theorem in that consumer supplies its own later Thom-group computation; it is not a premise of any result here.
