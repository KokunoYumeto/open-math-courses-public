# SH02-FAG-UNIT — Analytic geometry for finite maps

A finite holomorphic map can ramify and can have image of positive codimension. The stratifications needed for sheaf theory must accommodate both phenomena. This lesson constructs compatible strata near a finite fibre, beginning with a prescribed coefficient stratification. It also proves the dimension and conormal consequences used in finite holomorphic microsupport.

The proofs below are deductions from explicit analytic prerequisites. Those prerequisites are not proved in this lesson.

## SH02-FAG-CONTRACT — Analytic inputs and conventions

All analytic spaces are reduced complex analytic spaces. Their dimensions are complex dimensions. A finite holomorphic map means a proper holomorphic map with finite fibres. A complex analytic stratification is locally finite, has connected smooth locally closed strata, and has analytic stratum closures and boundaries. No global finite number of strata is assumed.

The following are the external analytic contracts used in this lesson.

| Contract | Required fact | Exact mathematical source |
| --- | --- | --- |
| Analytic components | Locally finite irreducible components, a dense regular locus, analytic singular loci, and strict dimension drop for a proper analytic subset of an irreducible space | Demailly, II.4.24, II.4.26, II.4.31 and II.5.3, pp.98, 100, 102–103 |
| Finite equations | The ideal sheaf of an analytic subset is coherent; locally it has finitely many generators | Demailly, II.4.29, pp.99–100 |
| Analytic difference | For closed analytic subsets $A,B$, the closure of $A\setminus B$ is analytic | Demailly, II.5.4, p.103 |
| One equation | On an irreducible analytic space, a holomorphic function which is not identically zero has an empty zero set or a zero set of pure codimension one | Demailly, II.6.2, p.106 |
| Finite image | A proper holomorphic image is analytic; a finite surjective holomorphic map preserves dimension | Demailly, II.8.8, pp.118–119, and II.8.1(b), p.116 |
| Whitney failure | If $H$ is reduced and equidimensional and $C\subset H$ is closed analytic, the points of $C$ where $(H_{\mathrm{reg}},C)$ fails the Whitney conditions form a closed analytic subset which is nowhere dense in $C$ | Teissier, VI.2.1, p.477 |

Demailly references mean the 21 June 2012 version of [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Teissier references mean [*Variétés polaires II*, Lecture Notes in Mathematics 961 (1982), pp.314–491](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf). The complex inverse and constant-rank theorems are also used. These references are precise prerequisite contracts, rather than claims that their underlying analytic foundations have been proved here.

The dimension bound below is derived from the one-equation theorem. The inequality printed in Demailly II.6.3 in that version points in the opposite direction; it is not the assertion used here.

## SH02-FAG-EQUATIONS — A lower dimension bound for simultaneous equations

**Proposition.** Let $Z$ be pure of dimension $m$, and let $g_1,\ldots,g_r$ be holomorphic functions. Every local irreducible component $D$ of their common zero set satisfies

$$
\dim D\geq m-r.
\tag{FAG1}
$$

**Proof.** For one equation, work on each local irreducible component of $Z$. If the function vanishes identically, that component is retained. Otherwise the one-equation contract gives either the empty set or components of dimension $m-1$.

Suppose the assertion has been proved for $r-1$ equations. Near a given point their zero set has finitely many irreducible components, each of dimension at least $m-r+1$. Intersect each with the zero set of $g_r$. An identically zero restriction leaves its component; a nonzero restriction lowers the dimension by exactly one whenever its zero set is nonempty. The common zero set is the finite union of these intersections. Each of its irreducible components is an irreducible component of at least one member of that union, so its dimension is at least $m-r$. This proves the induction. $\square$

Repeated equations and zero functions are included. For example, the two equations $z_1=0$ and $z_1=0$ in $\mathbb C^m$ define a set of codimension one. This also explains why a general inequality asserting codimension at least the number of equations would be false. The bound in FAG1 permits empty intersections and zero-dimensional spaces.

## SH02-FAG-IMAGE — Images and the rank away from a proper analytic subset

**Proposition.** Let $f:Y\to X$ be finite holomorphic. If $C\subset Y$ is a closed irreducible analytic subset, then $f(C)$ is closed irreducible analytic and

$$
\dim f(C)=\dim C.
\tag{FAG2}
$$

**Proof.** The restriction to $C$ is proper. The proper-image contract makes its image analytic, and a proper map between locally compact Hausdorff spaces is closed. If this image were a union of two proper closed analytic subsets, their inverse images would express $C$ as such a union. Thus the image is irreducible. The map $C\to f(C)$ is finite and surjective; the finite-dimension contract proves FAG2. $\square$

**Rank lemma.** A holomorphic map with finite fibres has differential rank $k$ on a dense open subset of the regular part of every pure $k$-dimensional irreducible source component.

**Proof.** On an open subset where the differential has its maximum rank $s$, the constant-rank theorem gives local fibres of dimension $k-s$. A positive value would contradict finite fibres. Hence $s=k$. The locus where that rank drops is a proper analytic subset of the regular part, and its complement is dense. $\square$

For the stratification construction we need a closed analytic exceptional set on the whole component. Embed a neighbourhood of $C$ into $\mathbb C^N$ and take local generators $h_j$ of its analytic ideal. At a regular point of a pure $k$-dimensional component, the matrix $dh$ has rank $N-k$. Choose coordinates for a local embedding of the target. The restriction of $df$ to $TC$ has rank less than $k$ exactly when

$$
\operatorname{rank}
\begin{pmatrix}dh\\df\end{pmatrix}<N.
\tag{FAG3}
$$

The maximal minors give holomorphic equations across the singular locus. Together with $C_{\mathrm{sing}}$, their zero set is a closed analytic exceptional subset of $C$. It is proper by the rank lemma. This construction uses generators of the reduced analytic ideal, so the Jacobian has the asserted rank on the regular locus.

## SH02-FAG-FIBRE — Restricting around an entire finite fibre

**Lemma.** Suppose $f:Y\to X$ is proper and $x\in X$. If an open set $V\subset Y$ contains $f^{-1}(x)$, then there is a neighbourhood $U$ of $x$ such that

$$
f^{-1}(U)\subset V.
\tag{FAG4}
$$

**Proof.** The closed set $Y\setminus V$ has closed image under the proper map. That image does not contain $x$. Its complement is a possible $U$. $\square$

For a finite fibre, choose one source neighbourhood at each of its finitely many points. Each neighbourhood can meet only finitely many strata of a locally finite prescribed stratification. FAG4 then places the full inverse image of a smaller target neighbourhood in their union. All the refinements below can therefore use a finite list of local analytic sets. Empty fibres are allowed: with $V=\varnothing$, the same argument gives an empty inverse image near $x$.

## SH02-FAG-ADAPTED — Constructing compatible Whitney strata

**Theorem.** Let $f:Y\to X$ be finite holomorphic, and fix a locally finite complex analytic source stratification. Near each finite fibre there are compatible Whitney stratifications of source and target refining that source partition, such that every source stratum maps locally biholomorphically onto a target stratum.

**Proof.** Use FAG4 to restrict around the whole fibre. Analytic component decompositions and the prescribed partition are locally finite, so after this restriction the construction involves finitely many local components, closures and boundaries. Shrinking further during the construction is harmless. We will use at most $\dim X+1$ stages, including dimension zero.

Proceed in descending dimension. At the stage indexed by $k$, let $Z\subset X$ be the remaining closed analytic set, with dimension at most $k$, and let $W=f^{-1}(Z)$. FAG2 applied to components shows that $\dim W\leq k$. All strata already chosen have dimension greater than $k$; each is open in the regular part of its analytic closure.

For each $k$-dimensional irreducible component $C$ of $W$, mark the following closed analytic exceptional subsets: its singular locus, intersections with other components, and the rank-drop set FAG3. Also mark every proper intersection of $C$ with a closure or boundary of the prescribed source partition. On the remaining part of $C$, membership in every such closure and boundary is constant. Since each original stratum is its closure minus its boundary, the remaining part of $C$ lies in one original stratum.

Next consider a previously chosen source stratum $S$. Its closure $H$ is pure analytic, and $S$ is open in $H_{\mathrm{reg}}$. If $C$ is not contained in $H$, mark the proper intersection $C\cap H$. If $C\subset H$, mark the Whitney-failure subset from the external contract. It is proper on each irreducible component of $C$. On the complement the pair $(H_{\mathrm{reg}},C_{\mathrm{reg}})$ satisfies the Whitney conditions. Restricting the upper regular part to its open subset $S$ keeps the same tangent spaces, so $(S,C_{\mathrm{reg}})$ satisfies them there too.

On each $k$-dimensional target component of $Z$, mark its singular locus, component intersections and its Whitney-failure subsets relative to the previously chosen target strata. Add every component of $Z$ of dimension below $k$. Finally add the images of all marked source subsets and of all source components of dimension below $k$.

Every set just added to the target is closed analytic. For the source images this follows from properness and FAG2. Their dimensions are below $k$, since each marked subset in a $k$-dimensional irreducible component was proper. Their finite union is therefore a closed analytic set

$$
Z'\subset Z,\qquad \dim Z'<k.
\tag{FAG5}
$$

Take the connected components of $Z\setminus Z'$ as the new target strata. Over each, take the connected components of its inverse image in the retained source components. Every source point is regular, lies in its prescribed original stratum, and has differential rank $k$. A $k$-dimensional component has a $k$-dimensional analytic image by FAG2; after removal of target component intersections, that image lies in one target component. The source and target strata thus have the same dimension, and the inverse function theorem makes the restriction a local biholomorphism.

Each connected source stratum maps onto its connected target stratum. Its image is open because the map is a local biholomorphism. It is also closed: the source component is closed in the full inverse image of the target stratum, and the map on that inverse image is the proper base change of $f$. A nonempty subset both open and closed in a connected target stratum is the whole stratum.

The new strata satisfy the Whitney conditions with every previously fixed higher stratum by the choice of the exceptional sets. Distinct new strata of the same dimension have disjoint closures away from $Z'$ and $f^{-1}(Z')$. Replace $Z$ by $Z'$ and continue. Later stages leave the higher strata fixed. At each later stage, a component is either contained in or disjoint from each earlier analytic closure, because every proper intersection has been removed. This gives the frontier condition as well as the Whitney conditions.

The process ends after dimension zero. Its connected-component subdivisions remain locally finite: analytic irreducible components are locally finite, and the regular connected pieces remain locally connected with finitely many branches after removal of a proper analytic subset. The regular-complement argument is the one in Demailly II.5.3 and its use of Remark II.4.2. There are only finitely many dimension stages. This proves the local theorem. $\square$

In particular, branch points are assigned to lower strata before the restriction is declared locally biholomorphic. The theorem permits several sheets, several source components, and target strata with empty inverse image. It asserts no global injectivity.

## SH02-FAG-COEFFICIENTS — Why one refinement serves all coefficients

Suppose the prescribed source partition makes the cohomology sheaves of a bounded complex $G$ locally constant. All choices in the preceding proof concern the map and that analytic partition. A restriction of a locally constant sheaf to a smaller stratum is locally constant. Therefore the refined partition is still adapted to $G$.

If scalar extension is derived and the stalk complexes are perfect, a locally constant model by perfect complexes remains locally constant after scalar extension. The geometric partition stays fixed. In particular, one refinement works for all residue-field extensions used in the finite-map coefficient argument. This statement requires no perverse t-structure over the original ring.

## SH02-FAG-CONORMAL — Closed affine conormals and their dimensions

**Proposition.** Let $S$ be a connected complex stratum in an $n$-dimensional complex manifold $M$, with analytic closure and boundary. Then $\overline{T^*_S M}$ is a closed complex analytic conic subset of $T^*M$, pure of dimension $n$.

**Proof.** Work locally on a pure $d$-dimensional component $Z$ of the closure. The stratum is dense and open in the relevant regular part. Choose generators $h_j$ for the reduced analytic ideal of $Z$. In $T^*M$ over $Z$, impose the vanishing of the $(n-d+1)$-minors of the matrix obtained by adjoining the covector row $\xi$ to the rows $dh_j$. This gives a closed analytic set $Q$.

On $Z_{\mathrm{reg}}$, the rows $dh_j$ span the annihilator of $TZ$ and have rank $n-d$. The minor condition says exactly that $\xi$ belongs to their span. Hence

$$
Q|_{Z_{\mathrm{reg}}}=T^*_{Z_{\mathrm{reg}}}M.
\tag{FAG6}
$$

The analytic-difference contract makes the closure of $Q$ minus its part over $Z_{\mathrm{sing}}$ analytic. This is the desired conormal closure, because restriction of the conormal bundle to a dense open subset of the regular component does not change its closure. That bundle has base dimension $d$ and fibre dimension $n-d$, so its components and their analytic closures have dimension $n$. Scaling covectors preserves the defining condition, which proves conicity. $\square$

This is an affine version of the conormal construction in Teissier II.4.1, pp.379–380. If $d=n$, the conormal is the zero section and the assertion concerns its closure. If $d=0$, it is the full cotangent fibre. These cases do not require a nonempty projectivized conormal.

A locally finite union of such closed conormals is analytic: locally only finitely many source strata can occur, so the union is a finite union of analytic sets near every cotangent point.

## SH02-FAG-BOUNDARY — Annihilation at a boundary stratum

For a Whitney stratification, every covector in a closed conormal based at a boundary stratum $T$ annihilates $TT$.

**Proof.** Choose covectors $\xi_i\in T^*_{S}M$ converging to a covector $\xi$ based at $y\in T$. Pass to a subsequence for which the tangent spaces $T_{y_i}S$ converge in the Grassmannian to a plane $L$. The covectors $\xi_i$ annihilate those tangent spaces, so their limit annihilates $L$. Whitney condition (a) gives $T_yT\subset L$. Thus $\xi$ annihilates $T_yT$. The case where the limiting point remains in $S$ follows directly from the same argument. $\square$

## SH02-FAG-EXAMPLES — Two small maps to test the statement

For $f:\mathbb C\to\mathbb C$, $f(z)=z^r$ with $r\geq1$, use the strata $\{0\}$ and $\mathbb C^*$ on both sides. The nonzero restriction has $r$ sheets and is locally biholomorphic; the point stratum maps isomorphically to a point. The lower stratum accommodates ramification when $r>1$.

For the closed embedding $\mathbb C\hookrightarrow\mathbb C^2$, $z\mapsto(z,0)$, take the image line and its complement as target strata. The line is the image of the sole source stratum, and the complement has empty inverse image. A finite map may therefore have positive-codimension image without violating the equal-dimension assertion for corresponding nonempty strata.

These examples check the role of strata, rather than replacing any hypothesis in the theorem.

## SH02-FAG-STATUS — The precise contribution to finite-map microsupport

FAG1 supplies the dimension bound for the equations defining a cotangent inverse image. FAG2–FAG5 supply the adapted finite-map geometry and its coefficient independence. FAG6 and the boundary argument supply analytic conormal closures and their annihilation property. These are the analytic deductions requested by SH02-FH-ANALYTIC-INPUT.

The remaining external prerequisites are the exact analytic contracts listed at the start, including the analytic Whitney-failure theorem and its own analytic dependencies. This lesson proves no Morse-pair existence, microsupport detection by normal Morse data, controlled holomorphic perturbation, intersection conservation, or perverse theorem. Their statements are given separately in the finite-map lesson.
