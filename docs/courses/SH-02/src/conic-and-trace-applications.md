# Boundary conditions, incidence operators, and trace identities

Course SH-02. Unit SH02-CTA. Proofs use the explicitly named sheaf-theoretic imports.

The same boundary distinction has several consequences. It controls which sheaves descend to a directional topology, makes certain incidence operators invertible, and determines the local classes whose traces are residues. We keep the connecting morphisms in the calculations, since listing cohomology groups would lose extension and sign information.

## SH02-CTA-CONVENTIONS — Coefficients and exact dependencies

Except in the explicitly field-valued failure example and differential-form calculation, $k$ is a commutative unital ring of finite global dimension. Categories are $D^+(k_X)$ unless a bounded complex is specified. All locally compact spaces are Hausdorff. Manifolds have finite dimension, are countable at infinity, and have no boundary unless the text explicitly uses a compact manifold as a closed subset of its double. The orientation complex is $\omega_X=o_X[\dim X]$. Every tensor product and internal Hom is derived.

The operations, comparisons and support conventions are those of [exceptional operations](../../sheaf-proof-readings/SH02-exceptional-operations.html), especially SH02-EX-ADJOINT, SH02-EX-COMPOSITION, SH02-EX-BASECHANGE and SH02-EX-INTERNAL. Ordinary direct image remains $Rf_*$, whereas integration along a nonproper map is $Rf_!$. We use localization, proper-support base change, and the bounded-below projection formula at their stated finite-dimensional map bounds. The orientation and normalized trace are SH02-MD-SUBMERSION and SH02-MD-TRACE in [manifold duality](../../sheaf-proof-readings/SH02-manifold-duality.html). The finite-dimensional kernel formalism is SH02-KER-004 through SH02-KER-008 in [kernel calculus](../../sheaf-proof-readings/SH02-kernel-calculus.html).

### SH02-CTA-IMP-TRIANGULATION — Finite compatible triangulations

A compact real semialgebraic set, together with finitely many semialgebraic subsets, admits a finite compatible triangulation. The finite models below derive this triangulation from the compatible subanalytic construction. The sheaf consequence needed here follows from a finite filtration by open simplices: constant extension sheaves on these simplices have the local stabilization and perfectness property of SH02-CB-SYSTEMS, by the convex calculations in SH02-CB-CONVEX; finite localization triangles preserve that property. Thus $k_U$ for a semialgebraic open subset of a compact manifold is cohomologically constructible. This implication does not claim arbitrary open subsets have that property.

### SH02-CTA-IMP-DERHAM — Differential forms and compact supports

The smooth de Rham complex resolves the constant complex sheaf; its terms, also after tensoring by the orientation local system, are acyclic for compact supports; smooth partitions of unity subordinate to coordinate covers exist; integration obeys Stokes' theorem for compactly supported forms and the iterated-integral formula. These are the same SH-01 analytic prerequisites used by SH02-MD-DENSITIES.

### SH02-CTA-IMP-POLYHEDRA — A finite pair with a local system

We use finite triangulability of a mapping torus of a piecewise-linear map, compatible Euclidean triangulation of an embedded finite polyhedron, and cellular computation of cohomology with a rank-one local system. The finite models below construct the needed triangulations and identify cellular differentials with the actual connecting maps. The neighborhood and orientation construction then follows in SH02-CTA-ORIENTATION-OBSTRUCTION.

<a id="SH02-CTA-FINITE-TOPOLOGY"></a>

### Finite models for the topological inputs

The [compatible-triangulation construction](../compatible-whitney-triangulation.html#TC3), together with its [ambient globalization](../compatible-whitney-triangulation.html#TC4), applies to an arbitrary locally finite family of locally subanalytic subsets of a real analytic manifold. For finitely many semialgebraic subsets of a compact set, use their polynomial equalities and strict inequalities as the labels in Euclidean space. Compactness meets only finitely many simplices in the resulting locally finite complex. Compatibility therefore gives a finite triangulation of the compact set and all its labels. This proves the geometric input in SH02-CTA-IMP-TRIANGULATION; the finite simplex filtration in that paragraph supplies its sheaf consequence.

For the mapping-torus input, let \(P\subset\mathbb R^d\) be a finite linear polyhedron and let \(f:P\to P\) be piecewise linear. Its graph is a finite union of linear simplices and is semialgebraic. Put \(a(t)=t(1-t)\) and define

\[
 T(x,t)=\begin{pmatrix}
 a(t)x\\(1-t)x+t f(x)\\a(t)\\a(t)(2t-1)
 \end{pmatrix}.
\]

This is the map CTA-TOP1.

The image of the compact semialgebraic set \(P\times[0,1]\) is compact and semialgebraic, by the proved finite projection calculus used in TC3. If \(0<t<1\), the last two coordinates recover \(t\), and the first recovers \(x\). At the endpoints they give precisely \(T(x,1)=T(f(x),0)\). These are exactly the equivalence classes defining the mapping torus, including all points of a possibly noninjective fibre of \(f\) at the top. The induced continuous bijection from that compact quotient to the Hausdorff image is a homeomorphism: images of closed subsets are compact and hence closed. The finite compatible triangulation of this image therefore triangulates the mapping torus. Include the image of any specified finite subpolyhedral trajectory among the labels to triangulate the pair. In particular, represent the degree-two circle map by the piecewise-linear map of polygonal circles that wraps twice, and retain its fixed base vertex. Its base-point trajectory is the circle used in SH02-CTA-ORIENTATION-OBSTRUCTION. This argument requires no infinite subdivision or injectivity of the circle map.

An embedded finite linear polyhedron also admits the required compatible ambient triangulation. Enclose it in the interior of a cube. For every simplex choose affine equations for its affine hull and affine extensions of its facet inequalities. The finite collection of their hyperplanes, together with the cube's facets, cuts the cube into a finite complex of convex polytopes; each original simplex is a union of its faces. Subdivide this polytopal complex by chains of faces, using the barycenter of every face. The subdivisions agree on intersections and include the embedded polyhedron as a subcomplex. Extend to all Euclidean space through successive homothetic cubical shells: the subdivided boundary cells and their scaled copies bound convex prism-shaped cells, whose ordered staircase subdivisions agree on faces. Only finitely many shells meet a compact set. This gives a locally finite ambient triangulation. One barycentric subdivision makes the specified subcomplex full, since a chain whose face barycenters belong to the subcomplex is a chain entirely within it.

Finally, cellular cochains with a local system follow from the same finite simplex construction. Trivialize the system on each closed cell after pulling back along its characteristic map. The relative cohomology of a cell and its boundary is its coefficient module in the cell's degree and zero in other degrees, by the relative interval calculation and ordered products. Filter a finite pair by its relative skeleta. The connecting maps for successive triples are the oriented face-incidence maps, with parallel transport along the attaching paths. This identifies the cellular differential with the actual connecting morphism. The finite filtration's spectral sequence is concentrated in one row, so there are no further differentials or extension choices in each resulting cohomological degree. Equivalently, the usual subdivision and prism homotopies compare this complex with simplicial cochains; parallel transport along each simplex makes those homotopies valid for local coefficients as well. The resulting finite cellular complex therefore computes the pair's cohomology, not just its Euler characteristic. Applied to the sign local system below, lifting the attaching word gives exactly its displayed twisted differential. These arguments allow arbitrary coefficient modules; rank one is imposed only in that example.


<a id="SH02-CTA-DERHAM-INPUTS"></a>

### The differential-form inputs

The smooth partition construction in [OF2](../ordinary-involutivity-floor.html#OF2) applies to the standing Hausdorff, countable-at-infinity manifolds. Its locally finite bump functions, divided by their positive locally finite sum, give a smooth partition subordinate to any open cover after refinement. The referenced partition component retains its attribution and licence as stated there.

For completeness, the local de Rham calculation is explicit. On a ball centered at zero, a smooth form of positive degree has the following radial homotopy, denoted CTA-DR1. Write \(v=(v_1,\ldots,v_{p-1})\) for the tuple of tangent vectors.

\[
 \begin{aligned}
 &(h\alpha)_x(v)\\
 &\quad=\int_0^1 t^{p-1}
   \alpha_{tx}(x,v)\,dt.
 \end{aligned}
\]

Differentiate the coefficient functions under this integral. The product rule and the alternating formula for the exterior derivative give the integral of the derivative of the pullback by radial scaling. The fundamental theorem of calculus therefore gives

\[
 dh+hd=\operatorname{id}-c_0^*.
 \tag{CTA-DR2}
\]

Here \(c_0\) is the constant map to the center; its pullback is zero on positive-degree forms and sends a function to its value at the center; set \(h=0\) on functions. The factor in CTA-DR1 is integrable and smooth at zero, so no punctured-ball argument is involved. Thus closed positive-degree forms are locally exact, and a function with zero differential is locally constant. This proves that the smooth de Rham complex resolves the constant sheaf with complex coefficients.

Every sheaf of smooth forms is a module over smooth functions. A section of its restriction to a compact set has local representatives near each point. Choose finitely many relatively compact chart neighborhoods with these representatives, and a smooth partition whose sum is one on a neighborhood of the compact set and whose corresponding supports lie in the respective chart neighborhoods. Multiply each representative by its partition function and extend by zero. Their finite sum has the prescribed germ at every point of the compact set, since every representative occurring there has that germ. Its support is compact. This proves the c-soft extension property used to compute compactly supported derived sections. Tensoring with the orientation local system preserves the argument, since its transition functions are locally constant and cutoffs commute with them. The finite de Rham resolution and these c-soft terms therefore compute the required compact-support cohomology at the exact manifold dimension bound. This argument does not claim that arbitrary sheaves are c-soft.

On an oriented coordinate chart the integral of a compactly supported total derivative is zero, by the one-variable fundamental theorem of calculus in that coordinate. Integrate the other coordinates afterwards. Interchanging the orders is justified directly by rectangular Riemann sums on one compact containing the support: uniform continuity makes their errors tend to zero, independently of the order of summation. This proves the iterated-integral formula for the smooth compactly supported coefficient functions used here. To obtain Stokes on the manifold, choose a partition on a neighborhood of the compact support and sum the chart identities for each partitioned form. The extra derivative terms cancel because the sum of the partition functions is one near the support. Coordinate changes use the ordinary determinant change-of-variables formula and the orientation sign. This is precisely the compactly supported Stokes identity and iterated integration used in the line-trace and global-trace calculations below; no boundary term at infinity occurs.


## SH02-CTA-LINE-TRACE — Fixing an integration sign on one line

The trace of an orientation complex is normalized locally. A short resolution makes its comparison with integration of differential forms explicit, including the coefficient map from integers to complex numbers.

Choose real numbers $a<b$, and write $L=(-\infty,b]$, $R=[a,\infty)$ and $J=[a,b]$. On the increasing oriented line consider the complex

$$
K^0=\mathbb Z_L\oplus\mathbb Z_R,
\qquad K^1=\mathbb Z_J,
\qquad d_K(s,t)=t|_J-s|_J,
$$

with no other terms. The diagonal map $\mathbb Z_{\mathbb R}\to K$ is a quasi-isomorphism. At a point of $J$ its stalk complex is $\mathbb Z^2\xrightarrow{t-s}\mathbb Z$, whose kernel is the diagonal and whose cokernel is zero. Outside $J$ the sole nonzero stalk is one copy of $\mathbb Z$ in degree zero, and the diagonal map is the identity on it. This also checks the two endpoints.

Choose a smooth function $\rho$ that is zero near $(-\infty,a]$ and one near $[b,\infty)$. There is a sheaf morphism from $K$ to the complex $\mathcal A^0_{\mathbb R}\xrightarrow{d}\mathcal A^1_{\mathbb R}$ of smooth complex-valued forms:

$$
\phi^0(s,t)=(1-\rho)s+\rho t,
\qquad
\phi^1(u)=u\rho'(x)\,dx.
$$

Each product is extended by zero where the original closed-support sheaf is absent. The factor $1-\rho$ vanishes on a neighborhood of the right endpoint of $L$, the factor $\rho$ vanishes near the left endpoint of $R$, and $\rho'$ vanishes near both endpoints of $J$. Thus these are smooth extensions and define sheaf morphisms on arbitrary open subsets, including those crossing endpoints. Local constancy of $s,t$ gives

$$
d\phi^0(s,t)=(t-s)\rho'\,dx=\phi^1d_K(s,t).
$$

The diagonal integer section $m$ maps to the constant function $m$. Hence the map induced on degree-zero cohomology is precisely the specified embedding $\mathbb Z\to\mathbb C$.

The two closed rays have zero compactly supported cohomology over $\mathbb Z$: their one-point compactifications are compact intervals, and the relative cohomology of an interval and the added endpoint is zero by the constant interval calculation. The compact interval $J$ has compact cohomology $\mathbb Z$ in degree zero. The terms of $K$ are therefore acyclic for compactly supported sections, and its bounded complex of compactly supported sections computes $R\Gamma_c(\mathbb R;\mathbb Z)$ by the bounded hypercohomology argument. That complex has only one nonzero term, $\mathbb Z$ in degree one: a nonzero constant section on either ray cannot have compact support. Its generator maps to $\rho'\,dx$, and

$$
\int_{\mathbb R}\rho'(x)\,dx=1.
$$

The normalization can be recorded by the commuting diagram

$$
\begin{array}{ccc}
H_c^1(\mathbb R;\mathbb Z)&\xrightarrow{\sim}&H^1\Gamma_c(K)\\
\downarrow\scriptstyle{\operatorname{tr}}&&
\downarrow\scriptstyle{H^1\Gamma_c(\phi)}\\
\mathbb Z&&H_c^1(\mathbb R;\mathcal A^\bullet)\\
\downarrow\scriptstyle{\mathbb Z\hookrightarrow\mathbb C}&&
\downarrow\scriptstyle{\int}\\
\mathbb C&\xrightarrow{\mathrm{id}}&\mathbb C.
\end{array}
$$

The increasing-coordinate compact-support generator used in SH02-MD-EUCLIDEAN is the same endpoint-difference class. Its abstract trace is also $1$. This proves equality of the abstract and analytic maps after extension of scalars to $\mathbb C$. If the differential of $K$ is replaced by $s-t$, the chain map uses $-\rho'\,dx$ and the coordinate generator changes by the same sign. A convention must be changed consistently on both sides.

## SH02-CTA-FORM-TRACE — From a coordinate generator to a manifold

Let $X$ be a smooth $n$-manifold, with no orientability assumption. The de Rham resolution identifies compactly supported cohomology of $o_X^{\mathbb C}$ with cohomology of compactly supported smooth forms twisted by the complex orientation line. Under this identification the trace

$$
H_c^n(X;o_X^{\mathbb C})\longrightarrow\mathbb C
$$

is analytic integration of an orientation-twisted top form.

The exact analytic prerequisites are SH02-CTA-IMP-DERHAM; their role is isolated in the coordinate and partition-of-unity steps below.

On $\mathbb R^n$ take the ordered external product of the one-dimensional generators from SH02-CTA-LINE-TRACE. Its form representative is

$$
\rho_1'(x_1)\cdots\rho_n'(x_n)
\,dx_1\wedge\cdots\wedge dx_n.
$$

Its integral is $1$, and ordered composition of the normalized sheaf traces also gives $1$. The compact-support group in top degree is a free rank-one module with this generator by SH02-MD-EUCLIDEAN; thus the two functionals agree on the whole group of a coordinate ball. The ordering of the coordinates is part of this comparison. A coordinate change of negative orientation changes the local orientation generator and the form orientation by the same sign, so the statement glues for the orientation-twisted complex.

For a compactly supported top form $\alpha$ on $X$, choose a finite coordinate cover near its support and a subordinate smooth partition of unity there. It expresses $\alpha$ as a finite sum of top forms supported compactly inside coordinate balls. Each is closed, because it has top degree. Analytic integration and the abstract trace are additive and commute with open extension, so the local equality proves equality on the class of $\alpha$. Stokes' theorem makes analytic integration independent of the representative. The empty manifold gives the zero map; in dimension zero the statement is the sum of the values, with the prescribed orientation generators. This proves the comparison at every allowed dimension and fixes the possible overall sign rather than leaving it implicit.

## SH02-CTA-RESIDUES — A finite set of local trace classes

Let $X$ be a topological $n$-manifold, and let $o_X$ be its orientation sheaf over $k$. For a point $x$ and an open neighborhood $U$, define

$$
\operatorname{res}_x:
H^{n-1}(U\setminus\{x\};o_X)
\longrightarrow H^n_{\{x\}}(U;o_X)
\xrightarrow{\sim}k
$$

as the localization connecting map followed by the local trace identification. Excision identifies the middle group with $H^n_{\{x\}}(X;o_X)$. Its normalization is that the local orientation class has trace $1$. Naturality of localization makes this definition commute with restriction to a smaller neighborhood; no global orientation is chosen.

If $X$ is compact and $Z$ is finite, every $v\in H^{n-1}(X\setminus Z;o_X)$ satisfies

$$
\sum_{x\in Z}\operatorname{res}_x(v)=0.
$$

Indeed, disjoint small neighborhoods of the points and excision identify

$$
H_Z^n(X;o_X)=\bigoplus_{x\in Z}H^n_{\{x\}}(X;o_X)=k^Z.
$$

The coordinates of the connecting map into this group are the residues just defined. The following map, from supported to ordinary cohomology, has zero composite with the connecting map by the localization triangle. Since $X$ is compact, compose it with the trace on $H^n(X;o_X)$. On each direct summand this composite is the local trace, by composition of trace and extension of compact supports. It therefore sends $(a_x)$ to $\sum_x a_x$. This proves the formula. Applying the same argument to each connected component gives vanishing of the sum on that component separately. The assertion includes disconnected or nonorientable manifolds and arbitrary coefficient modules as allowed by the chapter ring. When $n=0$ the input group is zero, so the formula remains valid.

## SH02-CTA-INDEX — Residues weighted by a mapping index

Now suppose

$$
H^{n-1}(X;o_X)=H^n(X;o_X)=0.
$$

For any finite $Z\subset X$, localization gives an isomorphism

$$
\delta_Z:H^{n-1}(X\setminus Z;o_X)\xrightarrow{\sim}k^Z.
$$

Let $e_x\in H^{n-1}(X\setminus\{x\};o_X)$ be the class with residue $1$. Naturality for the inclusion of one point into $Z$ identifies its restriction to $X\setminus Z$ with the coordinate vector at $x$ under $\delta_Z$. Consequently every $v$ has the expansion

$$
v=\sum_{x\in Z}\operatorname{res}_x(v)
\,e_x|_{X\setminus Z}.
$$

Let $Y$ be a compact topological $(n-1)$-manifold, and let $g:Y\to X$ be continuous. Include in the data an isomorphism $g^{-1}o_X\simeq o_Y$.

For every closed $Z\subset X$ disjoint from $g(Y)$, the map factors as $g_Z:Y\to X\setminus Z$. The unit of inverse image and ordinary derived direct image, followed by the given coefficient isomorphism, defines

$$
R\Gamma(X\setminus Z;o_X)
\longrightarrow R\Gamma\bigl(Y;g_Z^{-1}(o_X|_{X\setminus Z})\bigr)
\xrightarrow{\sim}R\Gamma(Y;o_Y).
$$

Its degree-$(n-1)$ map is the pullback used below. Exact inverse image and the derived adjunction define it for arbitrary closed $Z$; no finiteness of $Z$ is required. If $Z\subset Z'$ and both avoid $g(Y)$, adjunction naturality identifies pullback after restriction with the same map to $Y$. The assumptions on the two cohomology groups of $X$ are used to obtain the singleton residue classes, not to define this pullback.

For $x\notin g(Y)$ define

$$
\operatorname{ind}_x(g)=\int_Y g^{-1}e_x.
$$

If $Z$ is finite and disjoint from $g(Y)$, pull the expansion of $v$ back to $Y$ and integrate. The result is

$$
\int_Y g^{-1}v
=\sum_{x\in Z}\operatorname{ind}_x(g)\operatorname{res}_x(v).
$$

This proof uses linearity and the actual localization basis, so it works over any of the stated rings and does not use division. Over $\mathbb Z$ the indices are integers. They depend on the specified orientation-sheaf comparison: reversing that comparison changes both the relevant pullback integral and the indices. If $Y$ or $Z$ is empty the equation is zero on both sides. For $n=0$ the hypotheses force the pointwise construction to be vacuous; a nonempty index construction concerns $n\ge1$.

## SH02-CTA-HOMOTOPY-TRACE — Proper homotopies preserve the adjunction trace

Let $p_X:X\to S$ and $p_Y:Y\to S$ be maps of locally compact Hausdorff spaces. Put $I=[0,1]$, let $p:Y\times I\to Y$ be projection, and let $j_t:Y\to Y\times I$ be its endpoint sections. Suppose a proper map $h:Y\times I\to X$ satisfies $p_Xh=p_Yp$, and put $f_t=hj_t$ for $t=0,1$. Assume that $h_!$, $p_{X!}$ and $p_{Y!}$ have finite cohomological dimension. The interval projection and its closed sections have finite cohomological dimension as well, so the exceptional adjunctions and their compositions are defined on $D^+$.

For $F\in D^+(k_S)$, the map associated with $f_t$ is

$$
\begin{aligned}
\operatorname{tr}_{f_t}:Rp_{Y!}p_Y^!F
&\simeq Rp_{X!}Rf_{t!}f_t^!p_X^!F\\
&\xrightarrow{Rp_{X!}\epsilon_{f_t}}
Rp_{X!}p_X^!F,
\end{aligned}
$$

where $\epsilon$ denotes the exceptional counit. Then $\operatorname{tr}_{f_0}=\operatorname{tr}_{f_1}$ as natural transformations.

The projection $p$ is proper. Proper base change and the constant interval calculation show that its ordinary unit $\mathrm{id}\to Rp_*p^{-1}$ is an isomorphism. Its right-adjoint mate is the exceptional counit

$$
\epsilon_p:Rp_!p^!\xrightarrow{\sim}\mathrm{id}.
$$

Here is a direct way to justify the mate within the bounded-below theory. For bounded test complexes $A$ and $B\in D^+$, successive ordinary and exceptional adjunctions identify the map induced by $\epsilon_p$ on $R\operatorname{Hom}(A,-)$ with precomposition by $A\to Rp_*p^{-1}A$. The latter is an isomorphism. Bounded sheaves and all their shifts detect a zero cone in $D^+$, so $\epsilon_p$ is an isomorphism. This argument does not require an unbounded exceptional theory.

The two endpoint traces give maps

$$
c_t=Rp_!\epsilon_{j_t}:
\mathrm{id}
=Rp_!Rj_{t!}j_t^!p^!
\longrightarrow Rp_!p^!.
$$

Trace composition for $pj_t=\mathrm{id}_Y$ says $\epsilon_pc_t=\mathrm{id}$. Therefore $c_0=c_1=\epsilon_p^{-1}$. Apply these equal natural transformations to $p_Y^!F$ and then apply $Rp_{Y!}$. Using $p^!p_Y^!=h^!p_X^!$, follow each by $Rp_{X!}\epsilon_h$. Trace composition for $hj_t=f_t$ identifies the resulting maps with $\operatorname{tr}_{f_t}$. They are equal, with their original unit and counit normalizations preserved. In particular the statement concerns equality of maps, not only isomorphism of their source and target objects.

## SH02-CTA-SUPPORT — Which coefficient system tests a support comparison?

Let $f:Y\to X$ be a topological submersion of fixed finite fiber dimension $d$ between locally compact Hausdorff spaces. Let $Z_1\subset Z_2$ be closed subsets of $Y$, and write $W=Z_2\setminus Z_1$. Denote the relative dualizing object by

$$
\omega_f=f^!k_X=o_f[d].
$$

For $F\in D^b(k_X)$ there are two useful vanishing tests.

If $H_c^j(W\cap Y_x;\mathbb Z)=0$ for every fiber $Y_x=f^{-1}(x)$ and every $j$, then the natural map

$$
Rf_*R\Gamma_{Z_1}(f^!F)
\longrightarrow Rf_*R\Gamma_{Z_2}(f^!F)
$$

is an isomorphism. If instead

$$
H_c^j(W\cap Y_x;o_{Y_x}^{\mathbb Z})=0
\quad\hbox{for every }x,j,
$$

then the natural map

$$
Rf_*R\Gamma_{Z_1}(f^{-1}F)
\longrightarrow Rf_*R\Gamma_{Z_2}(f^{-1}F)
$$

is an isomorphism. Thus the constant integral test also proves the second statement whenever the relative orientation restricts trivially on each $W\cap Y_x$, for example for a relatively orientable submersion. No coherent choice of those individual trivializations is needed to test stalkwise vanishing.

To prove the first assertion, proper-support base change identifies the stalk cohomology of $Rf_!\mathbb Z_W$ with the assumed fiber groups, so that object is zero. It is bounded by the finite-dimensional fiber bound. The projection formula over $\mathbb Z$ gives

$$
Rf_!k_W
\simeq (Rf_!\mathbb Z_W)\otimes^L_{\mathbb Z}k_X=0.
$$

No flatness of $k$ as an abelian group is needed: the derived tensor and the length-one flat-resolution bound over $\mathbb Z$ give the stated comparison. The constant-extension triangle $k_W\to k_{Z_2}\to k_{Z_1}\to$ yields, after applying internal Hom into $f^!F$ and $Rf_*$, a triangle whose third term is

$$
Rf_*R\mathcal Hom(k_W,f^!F)
\simeq R\mathcal Hom(Rf_!k_W,F)=0.
$$

Its first map is exactly the support inclusion in the statement, proving the first assertion.

For the second assertion the relevant comparison is

$$
\begin{aligned}
Rf_*R\mathcal Hom(k_W,f^{-1}F)
&\simeq Rf_*R\mathcal Hom(k_W\otimes\omega_f,f^!F)\\
&\simeq R\mathcal Hom(Rf_!(k_W\otimes\omega_f),F).
\end{aligned}
$$

The first isomorphism uses invertibility of the shifted orientation line, and the second is internal exceptional duality with bounded first argument. The integral orientation line restricts to $o_{Y_x}^{\mathbb Z}$ on a fiber. Proper-support base change, the assumed vanishing, and coefficient extension therefore make $Rf_!(k_W\otimes\omega_f)$ zero. The same support triangle proves the assertion. These arguments retain an arbitrary locally compact base and the full bounded input range. They use no base change for a nonproper ordinary direct image.

## SH02-CTA-ORIENTATION-OBSTRUCTION — A finite torsion test for the missing twist

The constant-coefficient hypothesis in SH02-CTA-SUPPORT cannot in general be used for the ordinary-inverse-image conclusion without its orientation qualification. We give an explicit counterexample over $\mathbb Z$.

Let $B$ be the two-dimensional mapping-torus polyhedron of the degree-two map of a circle, and let $A\subset B$ be the base-point trajectory, a circle. A cellular presentation has edges $a,b$ and one two-cell with attaching word $aba^{-1}b^{-2}$; $A$ is the $a$-edge and the vertex. The relative cellular chain complex with constant coefficients has one copy of $\mathbb Z$ in degrees two and one, with boundary $-1$. Its relative cochain complex is also $\mathbb Z\xrightarrow{-1}\mathbb Z$ in degrees one and two. Hence

$$
R\Gamma(B,A;\mathbb Z)=0.
$$

Let $\chi$ be the sign local system with $\chi(a)=-1$ and $\chi(b)=1$. The relation preserves the sign, so this is well defined. In the relative complex the coefficient of the $b$-edge in the boundary of the two-cell is $-3$: the positive $b$ is preceded by $a$ and contributes $-1$, while each inverse $b$ contributes $-1$. Explicitly the derivative of the attaching word with respect to $b$ is

$$
a-aba^{-1}b^{-1}-aba^{-1}b^{-2},
$$

which evaluates to $-3$ under $\chi$. The local system is its own dual, so the relative cochain differential is also $-3$. Consequently

$$
R\Gamma(B,A;\mathbb Z_\chi)\simeq(\mathbb Z/3)[-2].
$$

We now realize this sign system as the restriction of a manifold orientation system. Use the elementary topology inputs SH02-CTA-IMP-POLYHEDRA. The neighborhood and orientation construction after those inputs is explicit below.

Triangulate the finite two-dimensional polyhedron $B$ and embed it in $\mathbb R^5$ by placing its finitely many vertices in general position and extending affinely over simplices. Two disjoint simplices have dimensions with sum at most four, and general position makes their affine hulls disjoint; the corresponding assertion for simplices with a common face shows they meet exactly in that face. Choose a locally finite ambient triangulation containing $B$ as a subcomplex and subdivide barycentrically. Then $B$ is full: any simplex all of whose vertices lie in $B$ belongs to $B$.

For a point $z$ in this triangulated Euclidean space, let $s(z)$ be the sum of its barycentric coordinates at vertices belonging to $B$, and put $N=\{s>0\}$. This is an open neighborhood of $B$. On $N$, discard coordinates at vertices outside $B$ and divide the remaining ones by $s(z)$. Fullness makes the resulting point $r(z)$ belong to $B$. The formula agrees on simplex faces and is continuous. The straight segment from $z$ to $r(z)$ remains in the same simplex and in $N$, and it fixes $B$. Thus $r:N\to B$ is a deformation retraction.

Pull the real sign line associated with $\chi$ back through $r$, and let $Y$ be its total space. Local trivializations identify $Y$ with open subsets of $N\times\mathbb R$, so $Y$ is a six-dimensional manifold without boundary. The base $N\subset\mathbb R^5$ is oriented. The sign of the transition maps in the remaining one-dimensional direction is $\chi$, and consequently $o_Y^{\mathbb Z}|_B=\mathbb Z_\chi$ on the zero section. The compact sets $A\subset B$ are closed in $Y$.

Set $f:Y\to\mathrm{pt}$, $Z_1=A$, $Z_2=B$ and $F=\mathbb Z$. This is a topological submersion of fiber dimension six. Compactness of $B$ identifies compactly supported cohomology of its complement of $A$ with relative cohomology, giving

$$
R\Gamma_c(B\setminus A;\mathbb Z)=0,
\qquad
R\Gamma_c(B\setminus A;o_Y^{\mathbb Z})
\simeq(\mathbb Z/3)[-2].
$$

The cone of the ordinary-coefficient support map is therefore

$$
\begin{aligned}
\operatorname{Cone}\bigl(R\Gamma_A(Y;\mathbb Z)
\longrightarrow R\Gamma_B(Y;\mathbb Z)\bigr)
&\simeq R\operatorname{Hom}_{\mathbb Z}
   \bigl(R\Gamma_c(B\setminus A;o_Y^{\mathbb Z})[6],\mathbb Z\bigr)\\
&\simeq(\mathbb Z/3)[-5].
\end{aligned}
$$

The last degree uses $R\operatorname{Hom}_{\mathbb Z}(\mathbb Z/3,\mathbb Z)=(\mathbb Z/3)[-1]$. The cone is nonzero. This identifies exactly why extension from constant integral coefficients to constant $k$ coefficients is valid, whereas the additional passage to a nontrivial orientation system is not. The observation is an independently checked correction to the unqualified support exercise in the cited book, not a claim of an official author-issued erratum.

## SH02-CTA-DIRECTIONAL — Locally closed directional sets are fixed objects

Let $V$ be a finite-dimensional real vector space and let $\gamma\subset V$ be a closed convex cone containing zero. It may contain lines or have empty interior. Let $\phi:V\to V_\gamma$ be the identity to the topology whose open sets satisfy $U+\gamma=U$.

If $A$ is locally closed in $V_\gamma$, then the ordinary extension sheaf $k_A$ is canonically a fixed object of the directional projector:

$$
\phi^{-1}R\phi_*k_A\xrightarrow{\sim}k_A.
$$

To prove this, form $k_A$ first on $V_\gamma$, using an open inclusion followed by a closed inclusion. Pullback to the ordinary topology gives the ordinary $k_A$: inverse image commutes with open extension by zero and with the constant sheaf of a closed subset, as one checks from their restriction maps and their stalks, which are $k$ on $A$ and zero outside it. Write the resulting object as $\phi^{-1}L$. The unit $L\to R\phi_*\phi^{-1}L$ is an isomorphism by SH02-GAM-UNIT. The triangle identity says that the counit on $\phi^{-1}L$ is its inverse after pullback. This proves the assertion with its actual counit.

In particular $-\gamma$ is directionally closed. Indeed, if $x\notin-\gamma$ and $g\in\gamma$, then $x+g\in-\gamma$ would imply $-x=g+(-x-g)\in\gamma$, a contradiction. Its complement is ordinarily open, so it is directionally open. Every directionally open $\Omega$ is itself locally closed in the directional topology. Both $k_{-\gamma}$ and $k_\Omega$ therefore satisfy the displayed fixed-object identity. This proof includes $\gamma=0$, $\gamma=V$, empty $\Omega$, and the zero coefficient ring.

## SH02-CTA-QUADRATIC — A calculation that retains the gluing class

Let $W$ be a Euclidean space of dimension $r\ge0$, let $V=\mathbb R_t\oplus W$, and set $N=r+1$. Write $O=\operatorname{or}(V)$ and $O_W=\operatorname{or}(W)$, so the increasing $t$ coordinate identifies $O=O_W$. Let $T$ be the negative-halfspace Fourier functor of SH02-FS-SETUP. In the dual variables $(\tau,\xi)$ put

$$
C_\pm=\{(t,w):\ \pm t\ge\|w\|\},\quad
A_\pm=\{(\tau,\xi):\ \pm\tau>\|\xi\|\},\quad
P_\pm=\overline{A_\pm},
$$

and let $i:\mathbb R_\tau\hookrightarrow V^*$ be the zero-$\xi$ axis. We compute the closed double cone $C=C_+\cup C_-$, its exterior $D=\{|t|\le\|w\|\}$, their common boundary $B$, and the intersections $C_+,D_+,B_+$ of these three sets with $\{t\ge0\}$.

Two elementary objects will encode all boundary gluing. Choose a generator of the free rank-one $k$-module

$$
\operatorname{Hom}\bigl(k_{P_-}\otimes O[-N],k_{A_+}\bigr)=k
$$

and denote its cone by $Q_+$. Define $Q_-$ by exchanging the two signs. A different generator changes the cone by an isomorphism, so this defines the isomorphism class of $Q_\pm$, which is what a transform calculation requires. To verify the displayed Hom calculation without guessing an extension, use

$$
D_{V^*}k_{P_+}=k_{A_+}\otimes O[N]
$$

from SH02-CB-CONVEX. Tensor–Hom adjunction and compact duality reduce the Hom complex to the dual of the cohomology of $P_-\cap P_+=\{0\}$, with the displayed orientation and shift canceled. It is $k$ in degree zero. Thus a generator specifies the required extension class; for $k\ne0$ it is nonzero, including over rings with torsion. For the zero ring all objects and comparisons are zero.

There is a unique morphism $e_+:Q_+\to k_{V^*}$ extending the usual map $k_{A_+}\to k_{V^*}$, and similarly $e_-$. Indeed $R\operatorname{Hom}(k_{P_-},k_{V^*})=R\Gamma_{P_-}(V^*;k)=0$: localization compares the constant cohomology of $V^*$ and $V^*\setminus P_-$, both $k$, by an identity on constants. The latter complement contracts to an open spherical cap. This proves both existence and uniqueness through the cone triangle. Choosing a different generator of the first Hom group transports $e_+$ along the same cone isomorphism.

For a second object use the following explicit morphism:

$$
k_{P_-}\otimes O[-N]
\longrightarrow i_*k_{\{\tau\le0\}}\otimes O[-N]
\longrightarrow i_*k_{\{\tau>0\}}\otimes O_W[-r].
$$

The first arrow is restriction to the axis. The second is the connecting class of the open–closed decomposition of the oriented line, shifted and tensored by $O_W[-r]$. Let its cone be $R_+$. The Hom group from the first object to the last is $k$: adjunction along $i$ reduces it to the same one-dimensional connecting-class group. We have therefore specified the unit gluing class rather than merely two disjoint support strata.

The answers are

$$
\begin{aligned}
T k_{C_+}&=k_{A_+},\\
T k_C&\simeq k_{\{|\tau|\le\|\xi\|\}}[-1],\\
T k_D&\simeq k_{P_+\cup P_-}\otimes O[-r],\\
T k_{B_+}&\simeq Q_+,\\
T k_{D_+}&\simeq R_+,\\
T k_B&\simeq
\operatorname{fib}\bigl(Q_+\oplus Q_-\xrightarrow{e_+-e_-}k_{V^*}\bigr).
\end{aligned}
$$

We prove all the answers and the asserted unit classes. The first is SH02-FS-CONE. Applying $T$ to the closed-cover sequence for $C_+\cup C_-$ gives the fibre of

$$
k_{A_+}\oplus k_{A_-}\longrightarrow k_{V^*}.
$$

Each component is the inclusion of its open constant sheaf, with the difference sign from the closed-cover sequence. The map is injective and its cokernel is the constant sheaf on the closed complement of $A_+\cup A_-$. This proves the second answer, including its $[-1]$.

The complement of $D$ is the union of the two open interiors of $C_+$ and $C_-$. Their transforms are $k_{P_-}\otimes O[-N]$ and $k_{P_+}\otimes O[-N]$. The transform of $k_V$ is $k_0\otimes O[-N]$. The map to this point sheaf is the sum of the two restrictions; they are the trace-normalized compact-cohomology maps on the open cones. The sum is surjective and its kernel is $k_{P_+\cup P_-}\otimes O[-N]$. Taking its cone shifts the kernel by $[1]$, proving the third answer.

For $B_+$ use the localization triangle of the open interior in $C_+$. Its transformed first arrow has the source and target used to define $Q_+$. It is a generator: full faithfulness of $T$ identifies its Hom group with

$$
\operatorname{Hom}(k_{\operatorname{int}C_+},k_{C_+})
=H^0(\operatorname{int}C_+;k)=k,
$$

and the original inclusion is the unit generator. This proves the fourth answer without an unsupported splitting of its two cohomology sheaves.

For $D_+$ localize the open interior of $C_+$ in the closed halfspace $H=\{t\ge0\}$. The product formula of SH02-FF-PRODUCT gives

$$
Tk_H=i_*k_{\{\tau>0\}}\otimes O_W[-r].
$$

Again the transformed inclusion is a generator, since the original Hom group is $H^0(\operatorname{int}C_+;k)=k$. The explicit axis morphism defining $R_+$ is also a generator by the line adjunction calculation. Their cones are isomorphic. This proves the fifth answer and specifies its extension up to the harmless change of a unit generator.

Finally $B=B_+\cup B_-$ with intersection the origin. Transform its closed-cover triangle. The restrictions to the origin become the maps $e_\pm$: on $A_\pm$ the defining compact-support fibre is the origin and the restriction is its identity. The uniqueness just proved fixes the full maps. This is the last answer.

No positive-rank assumption was hidden. If $r=0$, then $D=B=\{0\}$ and $D_+=B_+=\{0\}$. The cones $Q_\pm$ and $R_+$ are $k_\mathbb R$ by the ordinary line localization triangle, and the last fibre is also $k_\mathbb R$. All answers reduce to $Tk_{\{0\}}=k_\mathbb R$ and $Tk_\mathbb R=k_0[-1]$ with the increasing orientation. Empty open strata are handled by the zero sheaf.

The calculation also treats a positive semidefinite quadratic form. If its null space is $K$, split the ambient space as $\mathbb R_t\oplus W\oplus K$ and replace the norm on $W$ by the positive-definite quotient norm. Each of the six sets is the corresponding set above times $K$. Its transform is the displayed answer externally tensored with

$$
k_{\{0\}\subset K^*}\otimes\operatorname{or}(K)[-\dim K].
$$

This follows from the biconic product theorem, with the order $t,W,K$ used for the orientation tensor. An isomorphism between two positive-definite quotient norms transports the formula by the transpose map. Thus degeneracy introduces a zero-dual-space support and an orientation shift; it does not justify applying the proper-cone formula to a cone containing lines.

## SH02-CTA-RADIAL — Passing from vector bundles to their direction spaces

Let $E\to Z$ be a rank-$n$ real vector bundle over an arbitrary locally compact Hausdorff base. Let $j:E\setminus0\hookrightarrow E$, $\gamma:E\setminus0\to S(E)$, and use $j^*,\gamma^*$ for the corresponding maps of the dual bundle. Here the star in the name of a map labels the dual bundle, not a direct-image operation. Write $p,q$ for the projections from $S(E)\times_ZS(E^*)$, and put $D=\{(u,\eta):\langle u,\eta\rangle\ge0\}$. Define

$$
\mathcal A(F)=Rq_*R\Gamma_D(p^{-1}F),\qquad
\mathcal B(G)=Rp_!\bigl((q^{-1}G)_D\otimes q^{-1}\omega_{S(E^*)/Z}\bigr).
$$

These are respectively the right and left operators of the orientation-twisted sphere kernel in SH02-SPH-SETUP. Let $T_E,S_E$ be the Fourier functor and its inverse in SH02-FS-SETUP. There are canonical isomorphisms

$$
\begin{aligned}
\mathcal A(F)&\simeq R\gamma^*_*\,(j^*)^{-1}T_E(Rj_*\gamma^{-1}F),\\
\mathcal B(G)&\simeq R\gamma_*\,j^{-1}S_E(Rj^*_!(\gamma^*)^{-1}G).
\end{aligned}
$$

All functors act on $D^+$, with arbitrary module coefficients. The statement identifies the displayed composites; it does not forget the choice of $Rj_*$ in the first line or $Rj_!$ in the second.

For the first comparison use the ordinary-image presentation $T_E=Rq_*R\Gamma_{\langle x,\xi\rangle\ge0}p^{-1}$ of SH02-FS-COMPARE. Restrict the output to $E^*\setminus0$. Ordinary open restriction commutes with direct image. Pulling $Rj_*\gamma^{-1}F$ through the product projection is the smooth base-change comparison for that product, and support Hom commutes with the ensuing open direct image by adjunction. The remaining correspondence is the product of the two positive radial bundles over $D$. Its coefficient and support condition are pulled back from the direction spaces. Integrating the input radial coordinate with ordinary direct image gives the identity by SH02-CON-CYLINDER; the same is true of the output radial coordinate when applying $R\gamma^*_*$. This proves the first formula. Every map used is a product base-change, support-adjunction, or radial unit comparison, so these local calculations agree under changes of radial trivialization.

For the second formula use the proper-support presentation

$$
S_EG=Rp_!\bigl((q^{-1}G)_{\langle x,\xi\rangle\ge0}\bigr)
\otimes\operatorname{or}(E)[n].
$$

Open extension by zero commutes with inverse image and with proper-support composition, so $Rj^*_!$ restricts the integrated variable to the positive radial bundle. Its fibre has compact cohomology $k[-1]$, normalized by the increasing logarithmic radial coordinate. This cancels one unit of the shift $[n]$. The radial-first orientation rule in SH02-MD-SPHERE identifies the remaining factor with $\omega_{S(E^*)/Z}$, using positive dual orientation. Proper-support base change and projection formula now give $\gamma^{-1}\mathcal B(G)$ on the punctured output. Applying $R\gamma_*$ gives the displayed result by the radial unit isomorphism. This proof records the radial shift and the side on which its orientation belongs.

In rank zero both direction spaces are empty, so both comparisons are the unique isomorphisms of zero functors. A nontrivial orientation local system of $E$ is retained by the sphere dualizing object. No compactness or finite dimension of the base is required. The exact smooth base-change comparison for arbitrary locally compact base, together with the corresponding proper-support operation contracts, remains an explicit prerequisite; a nonproper fibre calculation alone does not supply it.

## SH02-CTA-INTERSECTION — Smooth factors can have irregular intersections

Cohomological constructibility is not preserved by tensor product or internal Hom. The following construction separates smoothness of each support from the topology of their intersection.

Work over a nonzero field $k$. Put $Z=\{0\}\cup\{2^{-j}:j\ge1\}\subset\mathbb R$. There is a smooth nonnegative function $b$ with zero set exactly $Z$. Here is a construction that also verifies smoothness at the accumulation point. On the interval $(2^{-j-1},2^{-j})$ use

$$
b(t)=e^{-4^j}\rho(2^{j+1}t-1),\qquad
\rho(s)=
\begin{cases}
e^{-1/(s(1-s))},&0<s<1,\\
0,&s\notin(0,1).
\end{cases}
$$

On $t<0$ use $e^{-1/t^2}$, and on $t>1/2$ use $e^{-1/(t-1/2)^2}$. Set $b=0$ on $Z$. Each derivative of order $r$ on the $j$th interval is bounded by $C_r e^{-4^j}2^{(j+1)r}$, which tends to zero faster than every power of $2^{-j}$. Induction on derivatives proves that the pieces extend smoothly at zero with all derivatives zero; the other joins are flat by the definition of $\rho$.

In the plane take the two closed smooth curves $L=\mathbb R\times\{0\}$ and $M=\{(t,b(t))\}$, and put $F=k_L$, $G=k_M$. Both are cohomologically constructible by SH02-CB-SUBMANIFOLDS. Since their constant extension sheaves are stalkwise flat,

$$
F\otimes^L G=k_{Z\times\{0\}}.
$$

This tensor product fails the stabilization condition at the origin. A section on a small neighborhood of the origin restricts to a locally constant function on a tail of the convergent sequence $Z$. Such a function is eventually constant, but it may have independent values on any finite collection of the isolated points. For any pair of nested neighborhoods there is an isolated point in the smaller one, and its indicator function extends by zero to a section on the larger one. It is killed by the map to the stalk at zero but survives that restriction. Consequently the kernel of the canonical neighborhood ind-system map to the stalk $k$ is not an ind-zero system: no restriction to one smaller neighborhood kills all its sections. A representable system with the canonical stalk comparison would have ind-zero kernel. Thus the tensor product is not cohomologically constructible.

Internal Hom already fails stalk perfectness. If $i:M\hookrightarrow\mathbb R^2$, closed-support adjunction gives

$$
R\mathcal Hom(k_L,k_M)=R\Gamma_L k_M
=i_*R\Gamma_{Z}^{M}k_M.
$$

Use the coordinate $t$ on $M$. The localization sequence for $Z$ on a small interval $I$ contains

$$
k=H^0(I;k)\longrightarrow H^0(I\setminus Z;k)
\longrightarrow H^1_Z(I;k)\longrightarrow0.
$$

The middle term is the product of one copy of $k$ for each component of $I\setminus Z$. After shrinking toward zero, it still contains independent values on all the successive gaps $(2^{-j-1},2^{-j})$. Partition these gaps into infinitely many infinite subsequences. Their indicator functions give linearly independent elements of the direct-limit quotient by constant functions: a nonzero finite linear combination cannot become constant on a tail, because at least one chosen subsequence and an unchosen infinite subsequence both persist. Hence the degree-one stalk of $R\Gamma_Z^M k_M$ at zero is infinite-dimensional. It is not a perfect complex over $k$. This proves the second failure without assuming biduality for the irregular intersection.

### SH02-CTA-ACCUMULATING-GRAPHS — Two sequences of intersections

The same failure occurs for continuous graphs with isolated intersections approaching from both sides. Let $h:\mathbb R\to\mathbb R$ be continuous, with $h(0)=0$, and suppose that in an interval about zero its zero set is

$$
Z_h=\{0\}\cup\{a_j:j\ge1\}\cup\{-b_j:j\ge1\},
\qquad a_j\downarrow0,\quad b_j\downarrow0,
$$

where both sequences are strictly decreasing. Put $L=\mathbb R\times\{0\}$ and $M_h=\{(t,h(t))\}$. The homeomorphism $(t,y)\mapsto(t,y-h(t))$ carries the closed graph onto a coordinate line. Hence $k_{M_h}$ is cohomologically constructible, as is $k_L$: homeomorphisms identify the neighborhood and compact-support systems and the perfect stalks. Differentiability at the accumulation point is unnecessary.

Their derived tensor is $k_{L\cap M_h}$ because both extension sheaves have flat stalks. For any two sufficiently small nested neighborhoods of the origin, an isolated positive intersection remains in the smaller one. Its indicator section on the larger neighborhood vanishes in the stalk at zero and survives restriction to the smaller neighborhood. Thus the kernel of the ordinary neighborhood system's map to its stalk is not ind-zero. Formal stabilization fails, so the tensor is not cohomologically constructible.

For internal Hom, closed-support adjunction gives

$$
R\mathcal Hom(k_L,k_{M_h})
=i_*R\Gamma_{Z_h}^{M_h}k_{M_h},
$$

where $i:M_h\hookrightarrow\mathbb R^2$. On a small coordinate interval $I$ in the graph, the degree-one local-support group is the cokernel of the constant-function inclusion $k\to H^0(I\setminus Z_h;k)$. The latter group is the product of one $k$ for every complementary interval. Partition the positive gaps $(a_{j+1},a_j)$ into countably many infinite families, each having gaps in every neighborhood of zero. Set each family's indicator to zero on all the other gaps, including the negative ones. These functions give linearly independent classes in the stalk cokernel: if a finite linear combination becomes constant after shrinking, its values on the negative gaps force the constant to be zero, and a surviving positive gap in each chosen family then forces its coefficient to be zero. Over a nonzero field the stalk is infinite-dimensional, so it is not perfect. This proves the internal-Hom failure as well.

For a concrete two-sided oscillation, set $h(t)=t\sin(1/t)$ for $t\ne0$ and $h(0)=0$. Continuity follows from $|h(t)|\le|t|$. Its nonzero zeros are exactly $t=1/(m\pi)$ for nonzero integers $m$, so the preceding theorem applies with $a_j=b_j=1/(j\pi)$. The flattening homeomorphism supplies the individual support condition, and the two independent local calculations give both failures over $\mathbb Q$ in particular.

## SH02-CTA-INCIDENCE-CRITERION — A pair calculation detects an inverse kernel

Let $P,Q$ be compact oriented manifolds of the same dimension $d$. Let $\Omega\subset P\times Q$ be open, and put $U_p=\{q:(p,q)\in\Omega\}$ and $V_q=\{p:(p,q)\in\Omega\}$. Assume:

1. Each row and column is a nonempty open $d$-cell and is cohomologically constructible as an extension sheaf in its ambient compact manifold.
2. Locally in each parameter, a homeomorphism of the ambient product that fixes that parameter trivializes the pair consisting of the fibre and its open cell.
3. Every pair of rows, and every pair of columns, admits a finite compatible triangulation in its compact ambient manifold. In particular the tensor products of either row sheaf with the Verdier dual of the other have perfect global cohomology, by the finite cellular complex.
4. For distinct parameters $p,p'$, the closed subset $U_p\setminus U_{p'}$ of $U_p$ is nonempty and has constant-complex cohomology $k$ in degree zero; the analogous assertion holds for columns.

Then the operator

$$
\Phi(F)=Rq_!(k_\Omega\otimes p^{-1}F)
$$

and its right adjoint

$$
\Psi(G)=Rp_*R\mathcal Hom(k_\Omega,q^!G)
$$

are mutually inverse equivalences on $D^+$. Here $p,q$ are the two projections, and $q^!G=p^{-1}\omega_P\otimes q^{-1}G$.

We give the kernel proof, including the maps. Write $j:\Omega\hookrightarrow P\times Q$. The right-adjoint kernel, with factors interchanged, is

$$
L=Rj_*k_\Omega\otimes p^{-1}\omega_P.
$$

Indeed, locally over $Q$ the pair is constant, so SH02-CB-EXTERNAL-HOM applies to its cohomologically constructible column in the $P$ variable and to the arbitrary bounded-below coefficient $G$. It identifies internal Hom with tensoring by this kernel. These comparisons are the canonical evaluation comparisons and therefore agree on overlaps. Compactness of the projections identifies $*$ and $!$ at this step.

For fixed $p,p'$, the stalk of the composite kernel is

$$
R\Gamma\bigl(Q;k_{U_p}\otimes D_Q k_{U_{p'}}\bigr).
$$

The orientation shifts from $\omega_P$ and $\omega_Q$ cancel in the chosen oriented identifications; equivalently retain their orientation lines throughout and use the trace pairing on the diagonal. Proper-support base change justifies the stalk calculation, and local triviality of the pair over $P$ justifies restriction of $Rj_*k_\Omega$ to a row. Compact-support duality and tensor–Hom adjunction identify the dual of the displayed complex with $R\Gamma(U_p;k_{U_{p'}})$. The displayed complex is perfect by the finite compatible triangulation hypothesis, so algebraic biduality identifies it with

$$
R\operatorname{Hom}_k\bigl(R\Gamma(U_p;k_{U_{p'}}),k\bigr).
$$

For $p=p'$, the inner complex is $R\Gamma(U_p;k)=k$. For $p\ne p'$, localization on $U_p$ gives the triangle

$$
R\Gamma(U_p;k_{U_{p'}})\longrightarrow R\Gamma(U_p;k)
\longrightarrow R\Gamma(U_p\setminus U_{p'};k)\longrightarrow.
$$

The last arrow before the connecting map is pullback of the constant class. Both its source and target are canonically $k$ by the hypotheses, and it sends $1$ to $1$. Hence the first term is zero. The composite kernel is therefore supported on the diagonal. The adjunction unit is the kernel map $k_{\Delta_P}\to L\circ k_\Omega$; its restriction at $(p,p)$ corresponds under the preceding adjunctions to the identity of $k_{U_p}$. It sends $1$ to $1$, so it is an isomorphism at every diagonal stalk as well. This proves the first composite identity as a morphism, including its normalization. Repeating the argument with columns proves the other composite identity. Kernel composition now proves both functor identities on all of $D^+$; it is not an argument restricted to point sheaves or finite-rank inputs.

The argument also works in dimension zero. Orientations may be retained as local systems instead of trivialized, provided the row/column trace identifications in the displayed kernel calculation are supplied. The two applications below have the needed orientations.

## SH02-CTA-CAPS — Spherical windows of arbitrary radius

Let $P=Q=S^d$ be the unit sphere in an oriented Euclidean space, with its boundary orientation, and choose $-1\le c<1$. Define

$$
\Omega_c=\{(u,v):\langle u,v\rangle>c\}.
$$

First suppose $-1<c<1$. Its rows and columns are equal-radius open spherical caps. They are open $d$-balls, vary by rotations, and have a smooth boundary. Two caps and their boundaries are semialgebraic and admit a finite compatible triangulation by SH02-CTA-IMP-TRIANGULATION. Local charts reduce their extension sheaves to the open halfspace calculation in SH02-CB-CONVEX, so they satisfy the constructibility hypothesis of SH02-CTA-INCIDENCE-CRITERION.

We verify the difference hypothesis uniformly for $d\ge1$. Write $U,V$ for two distinct equal-radius caps. Neither can properly contain the other: they have the same spherical volume, and a strict containment of round caps would have a difference with nonempty interior. Thus $U\setminus V$ is nonempty. If some point $z\in\partial V$ lies outside $U$, stereographic projection from $z$ sends $V$ to an open affine halfspace. It sends $U$ to an open ball when $z\notin\overline U$, and to an open affine halfspace when $z\in\partial U$. The image of $U\setminus V$ is therefore the intersection of that convex open set with a closed halfspace. It is convex, and its constant-complex cohomology is canonically $k$ by SH02-CA-CONSTANT.

Otherwise $\partial V\subset U$. The connected closed ball $S^d\setminus U$ avoids $\partial V$. It lies either inside $V$ or in $S^d\setminus\overline V$, the two components of that complement. The latter possibility would imply a strict inclusion $V\subset U$, already excluded. Hence $S^d\setminus U\subset V$, and $U\setminus V=S^d\setminus V$ is a closed ball. It again has constant cohomology $k$. In dimension zero every cap is the singleton consisting of its centre, and distinct rows have singleton difference.

At $c=-1$, a row is $U_u=S^d\setminus\{-u\}$, again an open $d$-cell. For distinct centres, $U_u\setminus U_{u'}=\{-u'\}$, whose constant-complex cohomology is canonically $k$. Rotations still trivialize the pairs, and finite triangulations compatible with two points supply the constructibility and perfectness conditions. This includes $d=0$. The criterion therefore applies in both variables for the entire range $-1\le c<1$. At $c\ge1$ the kernel is zero, whereas at $c<-1$ it is the constant kernel and factors through global cohomology; for a nonzero coefficient ring these excluded values do not satisfy the same conclusion.

## SH02-CTA-GRASSMANN — Oriented complements and a determinant contraction

Let $W$ be an oriented real vector space of dimension $n$, and $1\le m\le n$. Let $P$ parametrize oriented $m$-planes and $Q$ oriented $(n-m)$-planes. Define $\Omega$ to consist of pairs $(A,B)$ with $W=A\oplus B$ and with the ordered direct-sum orientation agreeing with that of $W$. Both Grassmannians are compact manifolds of dimension $d=m(n-m)$. Their orientations are canonical from the oriented tautological plane and its oriented quotient: the tangent space is $\operatorname{Hom}(A,W/A)$, whose determinant orientation is unchanged by orientation-preserving changes of bases. Local lifts to the oriented linear group trivialize the pairs of each Grassmannian and its complement chart.

Fix one oriented plane $A_0$ and choose its positively oriented complement $B_0$. Each element of its row is the graph of a unique linear map $T:B_0\to A_0$, with the orientation transported from $B_0$. Thus the row is the affine space $\operatorname{Hom}(B_0,A_0)$. The analogous description holds for columns, with the order sign $(-1)^{m(n-m)}$ included when the two summands are exchanged. Reversing that sign merely selects the opposite orientation chart.

To compare another row, write its plane $A_1$ in the fixed decomposition by its projections $P_1:A_1\to A_0$ and $Q_1:A_1\to B_0$. It is transverse to the graph of $T$ with the required orientation exactly when

$$
\det(P_1-TQ_1)>0,
$$

where oriented bases of $A_1,A_0$ define the determinant. If $r=\operatorname{rank}Q_1>0$, choose a basis beginning with $\ker Q_1$ and then a basis in its image. The first $m-r$ columns of $P_1-TQ_1$ are fixed and independent. Row and column operations reduce its determinant to a nonzero constant times the determinant of an arbitrary affine $r\times r$ block. The remaining matrix coordinates are free. More explicitly, quotient $A_0$ by $P_1(\ker Q_1)$; the induced map from $Q_1(A_1)$ to that quotient is an unrestricted $r\times r$ part of $T$, translated by the corresponding part of $P_1$. A linear complement supplies all unused coordinates.

The row difference is therefore a product of Euclidean space with one of

$$
\{M\in\operatorname{Mat}_r(\mathbb R):\det M\le0\},
\qquad
\{M\in\operatorname{Mat}_r(\mathbb R):\det M\ge0\}.
$$

Both contract to the zero matrix by $M\mapsto sM$, $0\le s\le1$, because $\det(sM)=s^r\det M$. Simultaneously contract the unused coordinates. The resulting nonempty locally compact space has constant-complex cohomology $k$: homotopy invariance for constant coefficients follows from proper projection along the compact homotopy interval and SH02-CA-CONSTANT. If $r=0$, the underlying planes agree. Equal orientations give the same parameter; opposite orientations give disjoint rows, so their difference is the entire affine chart. These are all cases.

The row sheaves are cohomologically constructible by SH02-CTA-IMP-TRIANGULATION: oriented Grassmannians and the determinant conditions are compact semialgebraic data. The same argument applies to columns. SH02-CTA-INCIDENCE-CRITERION now proves that the oriented-complement kernel and its exceptional right adjoint are inverse equivalences on $D^+$ with arbitrary $k$-module coefficients.

Here an orientation means one of the two generators of the integral orientation line, including in dimension zero. Equivalently, oriented planes are unit decomposable elements of the corresponding exterior power; the zeroth exterior power has the two unit elements $+1,-1$. For $m=n$, the two Grassmannians are consequently two-point sets, and the compatibility relation is a bijection between them. Its kernel is a permutation kernel. This checks the endpoint without assigning a positive-dimensional chart to the zero plane.

## SH02-CTA-PROBLEMS — Four further calculations with solutions

**An index with two components.** Let $X=\mathbb R^2$ with its standard orientation, and let $Y$ be two copies of the circle with increasing angular parameter $\theta$. On the first component use $g_1(\theta)=(\cos\theta,\sin\theta)$ and on the second use $g_2(\theta)=(4+\cos\theta,-\sin\theta)$. Specify the orientation-sheaf comparisons by sending the standard plane generator to the increasing-angle generator on both components. A class on the complement of the two centres has residues $r,s\in k$. Find its pullback integral over $Y$.

**Solution.** An annulus containing either circle identifies the singleton residue generator with the positive angular generator by the local boundary map. The first circle has index $1$ about its centre and zero about the other; the second has index $-1$ about its own centre and zero about the first. The zero assertions also follow by extending each circle across its disk in the complement of the other centre. SH02-CTA-INDEX therefore gives $r-s$. This example uses neither complex analysis nor field coefficients.

**A spherical endpoint kernel.** On $S^0=\{-1,1\}$, compute the spherical-window transform for any $-1\le c<1$, and compare it with $c<-1$.

**Solution.** The inequality $uv>c$ holds exactly when $u=v$ in the first range, so the kernel is the diagonal constant sheaf. The functor is the identity on the pair of coefficient complexes. In the second range all four pairs occur, so the output at each point is the direct sum of both input complexes; it is not an equivalence for a nonzero ring. The shift and orientation dimension are both zero.

**A null direction in a quadratic transform.** In $\mathbb R_t\oplus\mathbb R_x\oplus\mathbb R_z$, let $C=\{t\ge|x|\}$, with $z$ unrestricted, and use ordered coordinates $(t,x,z)$. Compute $Tk_C$.

**Solution.** The two-dimensional proper-cone answer is $k_{\{\tau>|\xi|\}}$. The unrestricted $z$ direction transforms to $k_{\{\zeta=0\}}\otimes\operatorname{or}(\mathbb R_z)[-1]$. The biconic external-product formula gives their external product. In the indicated orientation it is the extension sheaf of $\{\tau>|\xi|,\ \zeta=0\}$ shifted by $[-1]$. This detects the shift lost by treating a cone with a line as a proper cone.

**Change the coefficient ring in the support obstruction.** In the six-manifold example, determine the cone of the support map over a commutative ring $k$ of finite global dimension, including $k=\mathbb Q$ and $k=\mathbb F_3$.

**Solution.** The compactly supported orientation cochains of the finite pair are the free complex $k\xrightarrow{-3}k$ in degrees one and two. Shift it by six and take its $k$-linear dual. The resulting support cone is represented by $k\xrightarrow{3}k$ in degrees four and five, where changing both generator signs does not change its isomorphism class. Its degree-four cohomology is $\ker(3:k\to k)$ and its degree-five cohomology is $k/3k$. It vanishes over $\mathbb Q$. Over $\mathbb F_3$ the differential is zero, so the cone is $k[-4]\oplus k[-5]$. Tensoring the integral answer with $k$ must be derived; using an ordinary tensor would miss the degree-four term.

## SH02-CTA-ANTECEDENTS — Antecedents and further work

The cone, incidence, residue, trace and support questions treated here come from the conic and Fourier–Sato theory of Kashiwara and Schapira; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapters 1–2. The residue discussion goes back to Birger Iversen. The course's [open prerequisite contracts](../../sheaf-proof-readings/SH02-open-prerequisites.html) state the Stacks project foundations actually used.

Three research directions follow from the calculations. One can seek geometric row-difference criteria for other compact incidence correspondences, retaining the evaluation map on the diagonal. One can study how the gluing class in a quadratic transform changes in a family whose null space jumps. One can classify support comparisons by the orientation-twisted fiber complex rather than a list of constant-coefficient Betti numbers. These are questions for further work, not additional theorems asserted here.
