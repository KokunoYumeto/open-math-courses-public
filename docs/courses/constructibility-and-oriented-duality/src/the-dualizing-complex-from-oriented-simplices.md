# The dualizing complex from oriented simplices

The dualizing complex of a polyhedron can be written as a sheaf complex of oriented simplices. A $d$-simplex contributes in degree $-d$, with its coefficient extended to the **closed** simplex. The differential is its oriented boundary. This construction includes boundary points, branches, non-pure complexes and infinitely many locally finite simplices. Its stalks record local homology rather than merely the dimension of a simplex containing the point.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use [Constructible sheaves on a triangulation](../../sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md) for locally finite simplices, open stars, closed-simplex sheaves and the diagram/derived comparison. The exact current sheaf-operation prerequisites used here are locally closed support as internal Hom, exceptional composition, internal duality, oriented manifold dualizing objects, and constant-complex acyclicity on locally closed convex sets. The proof uses those results with their stated hypotheses. The simplicial construction is proved directly by a finite filtration of an injective complex. The two quasi-isomorphisms are constructed, rather than deduced from purity of the associated layers alone.

## The skeleton index and the support operation

Let $S$ be a locally finite simplicial complex with a uniform dimension bound $N<\infty$, and put $X=|S|$. The source's local finiteness means each vertex belongs to only finitely many simplices. No globally finite complex, pure dimension, orientability, field or Noetherian ring is assumed. Let $k$ be a commutative ring of finite global dimension. Write $\sigma^\circ$ for an open simplex, $\overline\sigma$ for its closed realization, and $d_\sigma=\#\sigma-1$.

Use the decreasing closed filtration

\[
 X_k=\bigcup_{d_\sigma\leq-k}\sigma^\circ,
 \qquad
 L_k=X_k\setminus X_{k+1}
     =\coprod_{d_\sigma=-k}\sigma^\circ.
 \tag{1}
\]

Thus $X_k=X$ for $k\leq-N$, $X_k=\varnothing$ for $k>0$, and $L_k$ is the union of the open $(-k)$-simplices. Each skeleton is closed: in a finite local subcomplex the union of the corresponding closed faces is closed, and local finiteness gives such neighborhoods everywhere. This also explains why a dimension bound, rather than a globally finite number of cells, makes the filtration finite.

For a locally closed subset $L$, use

\[
 R\Gamma_L F=R\mathcal Hom(k_L,F),
 \qquad k_L\text{ extended by zero from }L.
 \tag{2}
\]

This is a **sheaf** on $X$, not the single complex of global supported sections. A locally closed inclusion $j:L\to X$ gives
$R\Gamma_LF\simeq Rj_*j^!F$. In particular the ordinary direct image $Rj_*$ appears after exceptional restriction; replacing it by open extension by zero changes the boundary stalks.

The locally compact polyhedron has finite compact-support cohomological dimension. Indeed the finite skeleton filtration reduces compactly supported cohomology of an arbitrary sheaf to that on the disjoint open simplices; those are manifolds of dimension at most $N$. Compact support on a disjoint union gives direct sums, and local finiteness ensures each compact subset meets finitely many closed simplices. The manifold compact-support bound and the compact-support localization triangles give vanishing above $N$. Consequently $a_X^!k$ is defined under the existing exceptional-operation contract. Set

\[
 \omega_X=a_X^!k,\qquad D_XA=R\mathcal Hom(A,\omega_X).
 \tag{3}
\]

Initially the construction supplies a bounded-below object. The cellular model below will prove that $\omega_X$ is in fact bounded, in degrees $[-N,0]$.

## A supported layer is pure in its indexed degree

For an open $d$-simplex let $o_\sigma$ be its integral orientation line tensored with $k$. It is a constant free rank-one coefficient on that simplex, without choosing a generator. On its closed realization use the same constant line. [Exceptional composition](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-composition--composition-restriction-and-change-of-base) and [internal duality](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure) give

\[
 D_X(k_{\sigma^\circ})
   \simeq Rj_{\sigma*}\omega_{\sigma^\circ}
   \simeq Rj_{\sigma*}(o_\sigma[d])
   \simeq k_{\overline\sigma}\otimes_k o_\sigma[d].
 \tag{4}
\]

The first identity applies internal duality with the bounded input $k_{\sigma^\circ}$ and the bounded-below target $\omega_X$; it requires no biduality assertion. The middle identity is the exact oriented manifold dualizing formula, with cohomological degree $-d$.

To verify the last identity, factor $j_\sigma$ through the closed embedding of $\overline\sigma$. A sufficiently small convex neighborhood in that closed simplex meets $\sigma^\circ$ in a nonempty locally closed convex set, at every point of $\overline\sigma$. Its constant-section map is an isomorphism on derived cohomology. The resulting ordinary image has the constant orientation line in degree zero at every such point and zero elsewhere; these identifications commute with restriction. This checks an actual natural ordinary-image map on a basis. No arbitrary nonproper fibre base change is used.

For $d=-k$, the family of closed $d$-simplices is locally finite. The extension-by-zero constant sheaf on $L_k$ is the locally finite direct sum of the $k_{\sigma^\circ}$. Internal Hom changes a direct sum to a product, but here every point has a neighborhood meeting only finitely many closed supports. On that neighborhood the product and direct sum coincide, so (2)–(4) give

\[
 R\Gamma_{L_k}\omega_X
 \simeq
 \left(\bigoplus_{d_\sigma=-k}
       k_{\overline\sigma}\otimes_k o_\sigma\right)[-k].
 \tag{5}
\]

It follows that

\[
 H^j_{L_k}(\omega_X)=0\quad(j\ne k),\qquad
 K^k:=H^k_{L_k}(\omega_X)
     =\bigoplus_{d_\sigma=-k}
        k_{\overline\sigma}\otimes_k o_\sigma.
 \tag{6}
\]

The shift $[-k]=[d]$ puts the unshifted sheaf in degree $k=-d$. This is the source purity assertion, with its supported operation and negative skeleton index retained.

## Reconstruct from a finite pure support filtration

We give the finite form of the filtered construction needed here. Let $(X_k)$ be a decreasing closed filtration equal to $X$ and to $\varnothing$ at its two ends. If a bounded-below object $F$ satisfies
$H^j_{X_k\setminus X_{k+1}}F=0$ for $j\ne k$, define $K^k$ by these degree-$k$ layer sheaves. The boundary morphisms of the localization triangles give

\[
 d_K^k:K^k\longrightarrow K^{k+1}.
 \tag{7}
\]

Then $K$ is a complex and $F\simeq K$ in the derived category. This assertion includes a reconstruction map, rather than only a collapsed spectral sequence.

**Construction and proof.** Choose a bounded-below injective resolution $I$ of $F$ and set

\[
 P^kI=\Gamma_{X_k}I,
 \qquad Q^k=P^kI/P^{k+1}I.
 \tag{8}
\]

The exact coefficient sequence
$0\to k_{L_k}\to k_{X_k}\to k_{X_{k+1}}\to0$ and injectivity show that $Q^k$ computes $R\Gamma_{L_k}F$. Thus its cohomology is concentrated in degree $k$. Every filtration is finite, including at each stalk.

Define an actual subcomplex of $I$ by

\[
 G^k=P^kI^k\cap d_I^{-1}(P^{k+1}I^{k+1}).
 \tag{9}
\]

If $x\in G^k$, then $d_Ix\in P^{k+1}I^{k+1}$ and its next differential is zero, so $d_Ix\in G^{k+1}$. The map $G\to I$ is inclusion. Send $x\in G^k$ to its cycle class in $H^k(Q^k)=K^k$ to obtain $G\to K$. In this description $d_K[x]$ is the class of $d_Ix$ in $H^{k+1}(Q^{k+1})$. Changing a lift by a boundary or an element of $P^{k+1}$ changes this class by a boundary. The same representative has $d_I^2x=0$, so $d_K^2=0$ and $G\to K$ is a chain map. This is the localization-triangle boundary (7), with the same differential convention.

Here is a direct check of both quasi-isomorphisms. All lifts may be taken at a stalk, where the cohomology of the finite filtered sheaf complexes is the cohomology of their stalk complexes. This suffices to check a sheaf quasi-isomorphism.

For $G\to I$, take a cocycle $z\in I^q$. Starting at the lowest filtration index $a<q$, if $z\in P^a$, its class in $Q^a$ is a degree-$q$ cycle. Since $H^q(Q^a)=0$, subtract a differential of an element of $P^aI^{q-1}$ to move $z$ into $P^{a+1}$. Repeat finitely to obtain a cohomologous cocycle in $P^qI^q$, hence in $G^q$. If a cocycle $z\in G^q$ is $d_Iy$ in $I$, the same argument in degree $q-1$, using $d_Iy\in P^q$, replaces $y$ by an element of $P^{q-1}I^{q-1}$ without changing its differential. That primitive is in $G^{q-1}$. These prove surjectivity and injectivity on cohomology.

For $G\to K$, lift a $K$-cycle $\alpha\in K^q$ to $x\in G^q$. The condition $d_K\alpha=0$ lets one subtract $u\in P^{q+1}I^q$ so that $d_I(x-u)\in P^{q+2}$. In all subsequent indices $a\geq q+2$, $H^{q+1}(Q^a)=0$ lets one subtract another element of $P^aI^q$ and move this differential into $P^{a+1}$. At the finite terminal index it is zero. None of these corrections changes $\alpha$, so a cocycle of $G$ lifts it.

If a cocycle $x\in G^q$ maps to a boundary $d_K\beta$, lift $\beta\in K^{q-1}$ to $y\in G^{q-1}$. The image of $x-d_Iy$ is zero in $H^q(Q^q)$, so write
$x-d_Iy=d_Iz+w$ with $z\in P^qI^{q-1}$ and $w\in P^{q+1}I^q$. Then $z\in G^{q-1}$ and $w$ is a cocycle. The vanishing $H^q(Q^a)=0$ for every $a\geq q+1$ successively makes $w$ a differential, with a primitive in $G^{q-1}$. Hence $x$ is a boundary in $G$. This proves injectivity. We obtain the explicit isomorphism roof

\[
 F\simeq I\ \longleftarrow^{\sim}\ G
                  \ \longrightarrow^{\sim}\ K.
 \tag{10}
\]

Every correction terminates because the filtration is finite. There is no infinite convergence, unbounded totalization or termwise splitting assumption. Applying this to (5) proves $\omega_X\simeq K$ and its bounded range $[-N,0]$. This completes the finite supported-filtration reconstruction. $\square$

## The differential is the oriented boundary

Choose an ordering of the vertices to name orientation generators. For
$\sigma=[v_0,\ldots,v_d]$ with $v_0<\cdots<v_d$, let
$\tau_i=[v_0,\ldots,\widehat v_i,\ldots,v_d]$. Under (6), the differential is

\[
 \partial_\sigma=
 \sum_{i=0}^d(-1)^i\,\rho_{\sigma\tau_i},
 \qquad
 \rho_{\sigma\tau_i}:
 k_{\overline\sigma}\otimes o_\sigma
       \longrightarrow
 k_{\overline{\tau_i}}\otimes o_{\tau_i}.
 \tag{11}
\]

Each $\rho_{\sigma\tau_i}$ is the closed-face restriction tensored with the unsigned identification of the ordered orientation generators. The incidence sign is the single external factor $(-1)^i$ in (11). Components to a simplex that is not a codimension-one face are zero. For $d=0$ the target degree $1$ is zero; there is no artificial empty-simplex augmentation.

To identify this with (7), localize near the interior of one codimension-one face. The open simplex is a half-collar of that face, and the connecting map is the dual of the compact-support localization boundary of this collar. In the oriented interval the two-endpoint calculation fixes the generator by the difference of endpoint values $b-a$, so its dual sends the edge to terminal vertex minus initial vertex. Tensor this one-dimensional calculation with the face orientation, retaining the coordinate order. Boundary orientation is outward-normal-first; the orientation on the face opposite $v_i$ is $(-1)^i$ times its listed order. This gives exactly (11), with no additional fibre shift.

For completeness that sign is the ordinary determinant comparison: writing the simplex orientation with edge vectors based at $v_0$, the outward normal at the face opposite $v_i$ followed by that face's ordered tangent vectors has orientation $(-1)^i$ relative to the listed simplex orientation. Equivalently it is the sign in deleting the $i$th entry of the alternating ordered vertex generator. A neighborhood away from all faces has zero target; nonfaces have disjoint support there. These local identifications determine the sheaf component maps and prove (11) globally.

One can also check the complex identity directly. For a codimension-two face obtained by deleting entries $i<j$, the two routes have signs

\[
 (-1)^{i+j-1}\quad\text{and}\quad(-1)^{i+j},
 \tag{12}
\]

whose sum is zero in any coefficient ring. Their closed-face restrictions are the same map, so $\partial^2=0$. This agrees with the actual filtered proof; it is not its substitute.

Changing an orientation multiplies that simplex's generator by $-1$ and changes the adjacent incidence matrices by the corresponding basis changes. The resulting sheaf complexes are isomorphic. Keeping the lines $o_\sigma$ is an orientation-independent way to state the same object.

## Stalks are relative local chains

If $x\in\rho^\circ$, the summand $k_{\overline\sigma}\otimes_k o_\sigma$ has stalk $o_\sigma$ when $\rho\leq\sigma$ and zero otherwise. Thus the stalk complex is

\[
 K_x^{-d}=
 \bigoplus_{\substack{d_\sigma=d\\\rho\leq\sigma}}o_\sigma,
 \qquad
 \partial\text{ keeps only faces still containing }\rho.
 \tag{13}
\]

There are finitely many such cofaces. This is the relative simplicial chain complex of the closed star of $\rho$ modulo its faces not containing $\rho$, placed in negative chain degrees. It explains the local homology interpretation and works without purity. At a vertex $v$ of a cone on a finite complex $L$, it becomes the relative chain complex $(\operatorname{Cone}L,L)$, so

\[
 H^{-d}(\omega_X)_v\simeq
 \widetilde H_{d-1}(L;k),
 \tag{14}
\]

with augmented reduced-homology conventions, including an empty link at an isolated vertex. The formula follows directly by separating cone simplices from base simplices in (13): deleting the cone vertex is zero in the relative quotient; the other face maps are the link's augmented boundary maps, with a consistent shift of signs. No manifold assumption on the link is made.

## Exercises with complete solutions

### A closed interval has zero dualizing stalk at an endpoint

*Difficulty: Introductory.*

Order the vertices $v_0<v_1$ of one closed edge. Write the sheaf complex and compute all stalk cohomology groups. Compare ordinary restriction to the edge with the supported open-edge layer.

**Solution.** The complex is

\[
 k_{[v_0,v_1]}\quad\xrightarrow{\ (-\rho_0,\rho_1)\ }\quad
 k_{\{v_0\}}\oplus k_{\{v_1\}},
 \qquad\text{degrees }-1,0.
\]

At an interior point the target is zero and the source is $k$, so only $H^{-1}=k$ remains. At either endpoint the map is $-1$ or $+1$ from $k$ to $k$, hence the stalk complex is acyclic. Consequently $\omega_X$ is the open interval's orientation coefficient extended by zero and shifted by $[1]$.

Its ordinary restriction to the open edge has zero stalk at the endpoints after open extension. In contrast $R\Gamma_{(v_0,v_1)}\omega_X=k_{[v_0,v_1]}[1]$ by (5), with endpoint stalks $k$. These are the supported layer's ordinary-image boundary contributions; the next layer differential cancels them in the reconstructed object.

### A branching vertex detects the number of arms

*Difficulty: Intermediate.*

Take a finite star graph with central vertex $v$ and $m\geq1$ distinct edges to outer vertices. Orient every edge away from $v$. Compute $\omega_X$ at $v$, at the outer vertices and in edge interiors.

**Solution.** At $v$, all $m$ edge summands survive and the central vertex summand survives. The differential is
$k^m\to k$, $(a_1,\ldots,a_m)\mapsto-\sum_i a_i$. It is onto, so $H^0=0$ and
$H^{-1}=\ker(\sum)=k^{m-1}$, with an explicit basis $e_i-e_m$ for $i<m$. At an outer vertex only its one edge and that vertex remain; the map is $+1$, hence the stalk is acyclic. In an edge interior only the edge remains, giving $k$ in degree $-1$.

For $m=1$ even the central endpoint stalk vanishes. When $k\ne0$, the $m=2$ central coefficient is free of rank one, consistent with a line neighborhood, while $m=3$ gives a free rank-two coefficient that detects branching. The displayed stalk calculations hold also for the zero ring, where every coefficient vanishes.

### Non-pure complexes keep their separate degree-zero pieces

*Difficulty: Intermediate.*

Adjoin an isolated vertex $w$ disjoint from a star graph. Describe its dualizing stalk and compare it with a terminal vertex belonging to an edge. For the degree distinction assume $k\ne0$, and explain why a global shift by the maximum dimension does not describe the whole complex.

**Solution.** At $w$ there are no edge cofaces. Formula (13) leaves a single $k$ in degree zero with zero differential, so $H^0(\omega_X)_w=k$. At a terminal edge vertex there is also an edge summand in degree $-1$, and its incidence map to the vertex is an isomorphism, making that stalk zero. The same zero-dimensional simplex type therefore has different surrounding local chains.

The graph interiors have a degree-$-1$ coefficient, while the isolated point has degree zero. A single orientation local system shifted by $[1]$ would place the isolated point in the wrong degree. Formula (6) handles all dimensions together and does not assume the complex is pure.

### Triangle incidence signs cancel without dividing by two

*Difficulty: Intermediate.*

For vertices $0<1<2$, compute both differentials on the oriented triangle and show that their composite is zero. Repeat over a ring of characteristic two.

**Solution.** The first boundary is
$[12]-[02]+[01]$. Taking the next boundary gives

\[
 ([2]-[1])-([2]-[0])+([1]-[0])=0.
\]

Each vertex receives two opposite incidence routes, as in (12). The sheaf restrictions along the two routes agree. Over characteristic two the signs are both $+1$, but each repeated coefficient is $1+1=0$; the composite still vanishes. No step divides by two or uses characteristic zero. At vertex $0$, order the surviving edges as $[01],[02]$. The stalk complex is $k\to k^2\to k$ with maps $a\mapsto(a,-a)$ and $(b,c)\mapsto-b-c$. The first is injective, the second is onto, and its kernel is exactly the first image. Thus the dualizing stalk vanishes there. The other vertices give the same exact complex after changing basis, in agreement with the interval boundary mechanism.

### Local finiteness makes the infinite line a bounded sheaf complex

*Difficulty: Intermediate.*

Triangulate $\mathbb R$ with vertices $\mathbb Z$ and edges $[j,j+1]$, all oriented to the right. Explain why the infinite sums in (6) are legitimate, and compute the stalks at integer and noninteger points. Can an unrestricted product-to-stalk interchange replace local finiteness?

**Solution.** Each compact interval meets only finitely many closed edges and vertices. The sheaf complex has an infinite locally finite sum of edge coefficients in degree $-1$ and vertex coefficients in degree zero, with the usual terminal-minus-initial restrictions. At a noninteger point only one edge remains, giving $k$ in degree $-1$. At an integer $j$ the two incident edges remain; the map is $(a,b)\mapsto a-b$, which is onto with kernel the diagonal $k$. Again only degree $-1$ survives, and the diagonal identifications glue as the line orientation.

The global number of cells is infinite, but the number of terms near any point and the length of the degree interval are finite. This is exactly what makes the local product and direct sum agree in (5). General products of sheaves need not commute with stalks, so an unrestricted interchange supplies no replacement for this finite local-support argument.

### A torsion link gives torsion local dualizing cohomology

*Difficulty: Advanced.*

Let $L$ be a finite simplicial triangulation of $\mathbb RP^2$ and $X=\operatorname{Cone}L$. Compute the dualizing cohomology at its cone vertex over $\mathbb Z$ and over $\mathbb F_2$. Explain why a three-dimensional maximum does not force concentration in degree $-3$.

**Solution.** The projective plane has one cell in each dimension $0,1,2$. Its attaching loop for the two-cell traverses the one-cell twice, giving cellular differential $\mathbb Z\xrightarrow{2}\mathbb Z$ from degree two to one, and zero from degree one to zero. Thus its reduced homology over $\mathbb Z$ is $\mathbb Z/2$ in degree one and zero otherwise. Formula (14) gives
$H^{-2}(\omega_X)_v=\mathbb Z/2$, with all other groups zero.

Over $\mathbb F_2$, the multiplication-by-two boundary is zero, so the link has reduced homology $\mathbb F_2$ in degrees one and two. The cone vertex therefore has $\mathbb F_2$ in degrees $-2$ and $-3$. It is not a manifold point: its link does not have the homology of a two-sphere in either coefficient calculation. The finite cellular stalk complex has free terms over either ring, and its torsion cohomology over $\mathbb Z$ presents no failure of perfection. The geometry alone does not force local dualizing cohomology into a single maximum-dimensional degree.

### The filtered reconstruction needs a complex, not a direct sum of layers

*Difficulty: Advanced.*

Assume $k\ne0$. Use the closed interval to compare $\omega_X$ with the direct sum of its two pure layers, shifted into degrees $-1$ and zero but with zero differential. Identify the step in (9)–(10) that preserves the extension data.

**Solution.** With zero differential, the proposed direct sum has at an endpoint a $k$ in degree $-1$ and another $k$ in degree zero. The actual dualizing stalk is zero by the first solution, since the connecting incidence map is an isomorphism. Purity of the individual layers therefore does not permit splitting the filtered object.

The subcomplex $G^k$ in (9) retains representatives whose differential lands in the next support level. Their images under $d_I$ define the nonzero connecting differential on $K$. Both maps in the roof (10) preserve this differential and are proved quasi-isomorphisms by finite correction of cocycles and primitives. Dropping the differential discards the endpoint cancellation and the extension class; a collapsed collection of graded layer groups alone cannot reconstruct $F$.

## References and proof boundaries

Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §§4.6–4.7, pp. 94–98, supplies the exceptional and dualizing framework; §5.1, pp. 105–108, gives the dimension bound and orientation shift. In particular, Proposition 4.6.6 treats a bounded first input and bounded-below duality target, while Lemma 5.1.3 and Definition 5.1.4 identify the orientation shift. The programme proofs linked below construct the exceptional adjoint by a finite resolution and fix its interval generator. The independent finite reconstruction above uses enough injectives and the stated supported-cohomology identities. Its incidence differential is checked by the outward-normal convention and the interval boundary; the two contributions at a codimension-two face cancel. The local star-and-link calculation includes singular polyhedra and integral torsion, so it cannot be replaced by an orientation-sheaf assertion valid only on manifolds.

For a freely readable antecedent, see Masaki Kashiwara, *Index theorem for constructible sheaves*, Astérisque 130 (1985), §1.3–1.5, pp. 195–196; [free article](https://www.numdam.org/item/AST_1985__130__193_0/). It constructs oriented subanalytic chain sheaves and a chain resolution of the orientation sheaf on a real analytic manifold. The arbitrary polyhedron's closed-simplex model and finite reconstruction are proved above; they are not inferred merely from that manifold statement.

The operation inputs are [SH02-EX-EMBEDDING](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions), [SH02-EX-INTERNAL](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure), [SH02-EX-DUALIZING](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-dualizing--dualizing-objects-and-supported-dual-sections)/[SH02-EX-DUAL-SECTIONS](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-dual-sections--duality-of-ordinary-and-supported-sections), SH02-MD-EUCLIDEAN/SH02-MD-ORIENTATION-LINE/SH02-MD-SUBMERSION, and SH02-CA-CONSTANT, with their stated coefficient and degree ranges. The sheaf model and seven solved exercises use these prerequisites. The argument requires neither unrestricted biduality nor nonproper fibre base change, arbitrary product-to-stalk interchange or reconstruction from an infinite filtration.

