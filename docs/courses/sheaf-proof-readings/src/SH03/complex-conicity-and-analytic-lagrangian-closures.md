# Complex conicity and analytic Lagrangian closures

A real Lagrangian tangent plane need not be a complex tangent plane. Complex fibre dilations supply the extra information: they put both an Euler vector and its imaginary multiple in the tangent plane. The real symplectic form then detects both parts of the complex canonical form. We will use this calculation to prove that an involutive set with a subanalytic isotropic bound becomes complex analytic when it is locally invariant under complex dilations.

Let \(X\) be a complex analytic manifold of complex dimension \(n\), Hausdorff and countable at infinity. Put \(P=T^*X\), with its holomorphic cotangent structure. The corresponding real manifolds have dimensions \(2n\) and \(4n\). All statements are local on components of fixed dimension. There are no sheaf coefficients or derived shifts in this geometric lesson.

We give the tangent, boundary and rank arguments explicitly. The subanalytic uniformization and analytic removal theorems are stated as exact geometry prerequisites; their full underlying proofs remain open dependencies. The source account below credits the classical geometric mechanism and distinguishes its conventions from ours.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## Real covectors associated to holomorphic covectors

The real identification we use is

\[
\rho:(T^*X)^{\mathbb R}\longrightarrow T^*(X^{\mathbb R}),
\qquad \rho(\xi)(v)=\operatorname{Re}\bigl(\xi(v)\bigr).
\tag{1}
\]

Here \(v\) is a real tangent vector, regarded as a vector in the underlying real space of the complex tangent space. This identification is bijective: given a real covector \(\beta\), its corresponding complex-linear covector is

\[
\xi(v)=\beta(v)-i\beta(iv).
\tag{2}
\]

Indeed \(\xi(iv)=i\xi(v)\), and the real part of (2) is \(\beta(v)\). In coordinates \(z_j=x_j+iy_j\) and \(\xi_j=a_j+ib_j\),

\[
\rho\left(\sum_j\xi_j\,dz_j\right)
=\sum_j(a_j\,dx_j-b_j\,dy_j).
\tag{3}
\]

Consequently, for the complex canonical form and symplectic form,

\[
\alpha=\sum_j\xi_j\,dz_j,\qquad
\Omega=d\alpha=\sum_jd\xi_j\wedge dz_j,
\tag{4}
\]

the real canonical form and real symplectic form are \(\operatorname{Re}\alpha\) and \(\omega=\operatorname{Re}\Omega\). In particular \(\omega\) is nondegenerate. A vector annihilated by \(\operatorname{Re}\Omega\) against every real vector is also annihilated by \(\operatorname{Im}\Omega\): test against the imaginary multiple of each vector. Complex nondegeneracy of \(\Omega\) then makes that vector zero.

For a complex submanifold \(N\subset X\), (1) identifies its complex conormal with its real conormal. If \(\operatorname{Re}\xi\) annihilates the real tangent space of \(N\), test both \(v\) and \(iv\) in that tangent space. Both parts of \(\xi(v)\) vanish, so \(\xi\) annihilates the whole complex tangent space. This explains why complex conormals can be used in real microsupport estimates without changing the underlying subset.

## Analytic pieces and the different conicity conditions

A locally closed subset \(S\subset X\) is a **complex analytic piece** when its closure \(\overline S\) and its frontier \(\overline S\setminus S\) are closed complex analytic subsets of \(X\). Thus \(\mathbb C\setminus\{0\}\) is an analytic piece in \(\mathbb C\). An arbitrary open disc in \(\mathbb C\) is not: its closed-disc closure is not complex analytic. These pieces are subanalytic in the underlying real manifold.

Complex fibre multiplication is

\[
m_\lambda(x;\xi)=(x;\lambda\xi),\qquad \lambda\in\mathbb C^*.
\tag{5}
\]

A subset is positive-conic when invariant under all positive real \(\lambda\), and complex-conic when it is a union of entire \(\mathbb C^*\)-orbits. It is **locally complex-conic** when its intersection with each such orbit is open in that orbit. For a set closed in an open \(U\subset P\), this condition allows an orbit to leave \(U\); it asserts the local orbit directions at each point of the set. A zero covector has a singleton orbit.

If \(A\subset P\) is closed complex analytic, positive conicity implies complex conicity. Fix \((x;\xi)\in A\) with \(\xi\ne0\) and pull back \(A\) by the holomorphic orbit map \(\lambda\mapsto(x;\lambda\xi)\) on \(\mathbb C^*\). Its inverse image is an analytic subset of the connected complex curve \(\mathbb C^*\). It contains every positive real \(\lambda\), so the one-variable identity theorem makes it the entire curve. The zero orbit is already invariant. Conversely, complex conicity includes positive conicity.

This argument uses analyticity of \(A\). A closed positive real ray in a complex cotangent fibre does not become invariant under multiplication by \(i\).

## The real Lagrangian recovery used here

Suppose \(U\subset P\) is open and \(A\subset U\) is relatively closed and involutive. Assume it is locally complex-conic and is contained in a relatively closed positive-conic subanalytic real-isotropic set \(A_0\subset U\). Then the real recovery theorem gives

\[
A\text{ is subanalytic and real Lagrangian},\qquad
A=\overline{A_{\mathrm{reg}}}^{\,U},\qquad
\dim_{\mathbb R}A_{\mathrm{reg}}=2n.
\tag{6}
\]

Involutivity here is the singular two-set normal-cone condition, not an assumption that the set is already smooth. Real isotropy of the containing set is the singular canonical-form condition of the earlier lessons. At smooth conic points it gives the usual symplectic isotropy.

Here is why the earlier real recovery argument applies in this relative open setting. On the regular locus of \(A_0\), a relatively closed involutive subset of a smooth isotropic manifold is open; the smooth openness proof, using the local C1 flow and its differential, also forces dimension \(2n\). Its intersection there is therefore a union of regular components and is subanalytic. Let \(B\) be this union. A possible remainder \(A\setminus\overline B^{\,U}\) is an open restriction of the involutive set and lies in the singular residue of \(A_0\). That residue is isotropic and has dimension less than \(2n\). The no-small-involutive-subset argument makes the remainder empty. Thus \(A=\overline B^{\,U}\), which is subanalytic. Its regular points are simultaneously isotropic and coisotropic, hence real Lagrangian of dimension \(2n\); regular density gives the middle equality in (6).

All these steps take place in arbitrarily small ambient neighborhoods. The closed-set invariance proof requires closedness only in the chosen open flow domain and uses only times for which the trajectory exists there. The locally available dilation directions are sufficient; an entire orbit is not required to stay in \(U\). The dimension theory, local finiteness of regular components and singular normal-cone involutivity remain the exact prerequisites from that earlier argument. In particular, we have not assumed that an arbitrary initially non-subanalytic subset has regular points.

## Both Euler directions annihilate the complex canonical form

Fix \(p\in A_{\mathrm{reg}}\), and put \(L=T_pA_{\mathrm{reg}}\), a real Lagrangian plane for \(\omega\). Let

\[
E=\sum_j\xi_j\partial_{\xi_j}.
\tag{7}
\]

We view this complex vector as a real vector using the complex tangent structure. Local complex conicity puts both \(E_p\) and \(iE_p\) in \(L\): differentiate \(m_{e^t}p\) and \(m_{e^{it}}p\) at \(t=0\). These local orbit curves stay in the regular locus near a regular point. At a zero covector both vectors are zero, which causes no exception.

Our convention (4) gives

\[
\iota_E\Omega=\alpha.
\tag{8}
\]

This is a contraction identity, so it does not require a choice between the two Hamiltonian-isomorphism sign conventions. For every \(v\in L\), real isotropy and (8) yield

\[
\operatorname{Re}\alpha(v)=\omega(E,v)=0,
\qquad
-\operatorname{Im}\alpha(v)=\omega(iE,v)=0.
\tag{9}
\]

Thus \(\alpha\) pulls back to zero on \(A_{\mathrm{reg}}\) as a complex-valued one-form. Exterior differentiation gives

\[
\Omega|_{T A_{\mathrm{reg}}}=0.
\tag{10}
\]

Now take \(u,v\in L\). Complex bilinearity gives \(\Omega(iu,v)=i\Omega(u,v)=0\). Hence \(iu\in L^{\omega}\). Since \(L\) is real Lagrangian, \(L^{\omega}=L\); therefore

\[
iL=L.
\tag{11}
\]

The equality follows from inclusion and the invertibility of multiplication by \(i\). It follows that \(L\) has complex dimension \(n\), and (10) makes it complex Lagrangian.

The regular locus is an embedded real analytic manifold. The tangent invariance (11) makes it a complex submanifold. To check this last assertion locally, choose a complex-linear projection that is an isomorphism on \(L\). Its restriction to the regular locus is a real local diffeomorphism. Write the locus as a smooth graph over an open subset of \(\mathbb C^n\). Invariance of every tangent plane says that the graph differential is complex-linear. Its coordinate functions satisfy the Cauchy–Riemann equations, hence are holomorphic. This proves the complex submanifold assertion rather than treating tangent invariance as an analytic definition.

## The tangent space of a possible boundary hypersurface

Write \(R=A_{\mathrm{reg}}\) and \(D=A\setminus R\). By subanalytic dimension drop,

\[
\dim_{\mathbb R}D\le2n-1.
\tag{12}
\]

Suppose there is a \((2n-1)\)-dimensional regular part \(S\) of \(D\). Let \(S'\subset S\) be the open dense neighborhood-good locus where \((R,S)\) satisfies the ordered μ-condition. Its existence is the good-pair result. The complement in \(S\) has smaller dimension; if (12) is an equality, \(S'\) is nonempty.

For \(p\in S'\), choose \(p_k\in R\) tending to \(p\) and pass to a convergent subsequence of tangent planes,

\[
T_{p_k}R\longrightarrow\tau\subset T_pP.
\tag{13}
\]

Use a local coordinate trivialization and the compact Grassmannian. Each plane in (13) is a complex Lagrangian \(n\)-plane, so its limit has the same properties. The μ-condition implies

\[
T_pS'\subset\tau.
\tag{14}
\]

Indeed, for any covector \(\theta\) annihilating \(\tau\), convergence of the annihilator planes gives covectors \(\theta_k\in T^*_{p_k,R}P\) tending to \(\theta\). The bounded conormal-closure consequence of the μ-condition puts \(\theta\) in \(T^*_{p,S'}P\). Thus \(\tau^\perp\subset(T_pS')^\perp\), which is exactly (14). This uses conormals in \(T^*P\), because the two bases here are submanifolds of \(P\).

Since \(T_pS'\) has real dimension \(2n-1\), it cannot fit in a proper complex subspace of the complex \(n\)-plane \(\tau\). Such a proper subspace has real dimension at most \(2n-2\). Consequently

\[
T_pS'+iT_pS'=\tau,
\qquad
\dim_{\mathbb C}(T_pS'+iT_pS')=n.
\tag{15}
\]

The statement concerns the complex span of a real tangent space. It does not say that the odd-dimensional real manifold \(S'\) is a complex submanifold.

## Constructing the minimal complex Lagrangian hull

Fix a sufficiently small connected real analytic patch of \(S'\). A real analytic manifold has a local complexification: real analytic coordinate functions extend holomorphically, with the real patch a totally real submanifold of that complexification. Complexify the embedding into \(P\), obtaining a holomorphic map

\[
h:S'_{\mathbb C}\longrightarrow P.
\tag{16}
\]

At points of the real patch, its complex differential image is the complex span in (15), so its rank is \(n\). Every \((n+1)\)-minor of the differential is holomorphic and vanishes on that real patch. The identity theorem on a totally real coordinate patch makes it vanish nearby. Some \(n\)-minor is nonzero at the chosen point. After shrinking, \(h\) has constant complex rank \(n\). The holomorphic constant-rank theorem therefore gives a complex \(n\)-submanifold \(Z\) containing the patch of \(S'\).

This \(Z\) is **minimal as a germ**: any complex submanifold containing the real patch contains the germ of \(Z\). Compose its local holomorphic defining functions with \(h\). They vanish on the totally real patch, so they vanish on its complexification. That puts the image of \(h\) in the given submanifold.

At points of \(S'\), (14)–(15) identify \(TZ\) with a limiting complex Lagrangian tangent plane of \(R\). Thus \(\Omega|_{TZ}=0\) there. Pull back this two-form along (16). Each holomorphic coefficient vanishes on the real patch and hence throughout its complexification. Since \(h\) is a submersion onto \(Z\), \(\Omega|_{TZ}=0\) nearby. Its dimension is \(n\), so \(Z\) is a complex Lagrangian submanifold.

The complexification, real-patch identity theorem and holomorphic constant-rank theorem are the complex-analysis inputs in this construction. Minimality is a germ assertion; it does not assert a global smallest analytic subset containing an arbitrary real set.

## Regular points outside the hull cannot accumulate along an open boundary patch

We claim

\[
S'\cap\overline{R\setminus Z}
\text{ is nowhere dense in }S'.
\tag{17}
\]

All sets and closures in this step are restricted to a small ambient neighborhood where \(Z\) is defined and closed. The intersection in (17) is closed in \(S'\), so it suffices to rule out an open patch contained in it.

Suppose such a patch exists and shrink \(S'\) to that patch. Let \(C=\overline{R\setminus Z}\). It is closed and subanalytic, of pure real dimension \(2n\), with \(R\setminus Z\) open dense in \(C\). The uniformization prerequisite supplies a proper real analytic map from a real analytic manifold of the same dimension onto \(C\). Its exact statement is [Bierstone–Milman, Theorem 0.1](https://www.numdam.org/article/PMIHES_1988__67__5_0.pdf). The underlying uniformization proof is a geometry dependency.

We may arrange a proper surjection

\[
f:W\longrightarrow C
\quad\text{with}\quad
f^{-1}(R\setminus Z)\text{ open dense in }W.
\tag{18}
\]

Here is the needed refinement of the supplied uniformization. On each connected component of its \(2n\)-dimensional domain, retain the component if the map has maximal real rank \(2n\), and discard components of smaller maximal rank. The latter have measure-zero images in the smooth \(2n\)-dimensional part of \(C\), by Sard. Their countable union cannot cover an open part of that smooth locus. The retained union is closed and open in the original domain, so the restricted map remains proper and its image is closed. Its image contains a dense subset of the smooth locus; since that locus is dense in \(C\), it is onto \(C\).

On each retained component, rank \(2n\) holds on an open dense set by real analytic minors. The complement of \(R\setminus Z\) in \(C\) has dimension at most \(2n-1\). An open domain patch mapping into that complement would have a rank-\(2n\) point and a \(2n\)-dimensional local image there, a contradiction. Thus its inverse image has empty interior. This proves the density in (18); openness follows from the relative openness of \(R\setminus Z\) in \(C\).

Complexify \(W\) locally and extend \(f\) holomorphically to \(f_{\mathbb C}\). At every point of \(f^{-1}(R\setminus Z)\), the real differential takes values in the complex \(n\)-plane tangent to \(R\). Its complex span has dimension at most \(n\). Thus every \((n+1)\)-minor of \(df_{\mathbb C}\) vanishes on the dense open real part in (18). It vanishes on the whole real patch by continuity, and on its complexification by the identity theorem. Therefore

\[
\operatorname{rank}_{\mathbb C}df_{\mathbb C}\le n
\quad\text{also at points above }S'.
\tag{19}
\]

We also need a point above \(S'\) whose differential spans its tangent space. The set \(f^{-1}(S')\) is subanalytic and has a locally finite decomposition into smooth analytic pieces. For each such piece, its map to \(S'\) has critical values of measure zero unless it has a full-rank point. Surjectivity in (18) onto the open \((2n-1)\)-dimensional patch \(S'\) forces some piece to have rank \(2n-1\). Countable atlases suffice for this measure argument. At a full-rank point \(w\) of that piece,

\[
T_{f(w)}S'\subset\operatorname{Im}df_w.
\tag{20}
\]

Its complex span has dimension \(n\) by (15). Hence the holomorphic differential has rank at least \(n\) at \(w\), and (19) makes its rank exactly \(n\). A nonzero \(n\)-minor and (19) give constant rank near \(w\). The image there is a complex \(n\)-submanifold containing an open patch of \(S'\), since the selected real piece maps submersively to that patch. Minimality of \(Z\) makes the two complex submanifold germs equal.

But every real neighborhood of \(w\) meets \(f^{-1}(R\setminus Z)\) by (18). Its images lie outside \(Z\), whereas the local constant-rank image lies in \(Z\). This contradiction proves (17).

Properness matters when retaining a closed image in (18). Complex tangent planes, rather than a naive division of real differential rank by two, matter in (19).

## Involutivity removes the boundary hypersurface

If \(S\) were nonempty, choose

\[
p\in S'\setminus\overline{R\setminus Z},
\tag{21}
\]

using (17). Near \(p\), all points of \(R\) lie in \(Z\). By (6), \(A\) is the closure of \(R\), so near \(p\) we have \(A\subset Z\). It is a relatively closed involutive subset of the smooth real Lagrangian manifold \(Z\). The smooth involutive openness theorem therefore makes it open in \(Z\). Shrink once more at \(p\); then \(A=Z\) there.

This says \(p\) is a regular point of \(A\), contradicting \(p\in S'\subset D\). Hence no \((2n-1)\)-dimensional regular part of \(D\) exists. Subanalytic regular density and dimension decomposition give

\[
\dim_{\mathbb R}D\le2n-2.
\tag{22}
\]

The proof is local at every possible boundary patch, so (22) holds after every open restriction that meets \(A\). In particular, it is the local dimension condition needed by an extension theorem, rather than a single global dimension comparison masking a small-dimensional component.

## The exact analytic removal step

We use the following analytic removal prerequisite: a relatively closed subanalytic subset of a complex manifold is complex analytic if, on every open restriction, the points where its germ is not a complex submanifold have real dimension at least two less than that restriction. An exact formulation is [Peterzil–Starchenko, author manuscript, Corollary 4.2, PDF 11](https://math.haifa.ac.il/kobi/analytic.pdf). For a pure complex regular locus this is the small-boundary removal theorem associated with Shiffman. The full removal proof remains a complex-geometry prerequisite.

Apply it to \(A\). By (6) its nonempty local restrictions have pure real dimension \(2n\). Every real regular point is complex regular by (11), so the complex singular points lie in \(D\). Equation (22) gives the required local dimension bound. Therefore \(A\) is complex analytic in \(U\).

We have proved the complete application theorem: a relatively closed, locally complex-conic involutive set with a relatively closed positive-conic subanalytic real-isotropic bound is complex analytic. Its regular locus is complex Lagrangian of complex dimension \(n\). The extension step does not assume that \(D\) is itself complex analytic. The empty set is analytic; when \(n=0\), the ambient manifold is discrete and the conclusion holds directly, with no boundary argument needed.

## Exercises with complete solutions

### Recovering a holomorphic covector from its real part

*Difficulty: Introductory.*

On \(X=\mathbb C\), let \(\beta=3\,dx+2\,dy\). Find the corresponding holomorphic covector using (1), compute the real covector corresponding to its multiple by \(i\), and verify (2) on \(\partial_x\) and \(\partial_y\).

**Solution.** Formula (3) gives \(\xi=(3-2i)\,dz\). Multiplication by \(i\) gives \((2+3i)\,dz\), corresponding to \(2\,dx-3\,dy\). Since \(i\partial_x=\partial_y\) and \(i\partial_y=-\partial_x\), (2) gives \(\xi(\partial_x)=3-2i\) and \(\xi(\partial_y)=2+3i=i(3-2i)\). The minus sign before \(b\,dy\) in (3) is essential.

### A positive ray cannot be a closed complex analytic cone

*Difficulty: Introductory.*

In \(T^*\mathbb C\), fix \(x=0\) and set \(A=\{(0;\xi):\xi\in\mathbb R_{\ge0}\}\). Show it is closed and positive-conic but not complex analytic. Find the smallest closed complex analytic subset of that fibre containing it.

**Solution.** The real ray is closed and invariant under positive multiplication. If it were complex analytic in the fibre \(\mathbb C\), its holomorphic defining functions near any positive point would vanish on a real interval, hence on a complex neighborhood by the identity theorem. Analytic continuation along the fibre makes every holomorphic equation vanishing on the whole ray vanish identically. Its analytic closure is the full fibre \(T_0^*\mathbb C\). The ray is not the full fibre; for example \(i\) does not lie in it. The same conclusion follows from positive-to-complex conicity for a closed analytic subset: that result would force the entire orbit of \(\xi=1\).

### A real conormal has only one Euler direction

*Difficulty: Intermediate.*

Let \(N=\mathbb R\subset\mathbb C\). Express its real conormal under (1), check that it is real Lagrangian, and show why the calculation (9) fails to force a complex tangent plane.

**Solution.** Write \(z=x+iy\) and \(\xi=a+ib\). The real tangent to \(N\) is spanned by \(\partial_x\), so its conormal is

\[
\Lambda=\{y=0,\ a=0\},
\qquad z=x,\quad \xi=ib.
\tag{23}
\]

It has real dimension two and tangent spanned by \(\partial_x,\partial_b\). Since \(\omega=da\wedge dx-db\wedge dy\), its symplectic restriction is zero, so it is real Lagrangian in the real four-dimensional cotangent manifold. The real Euler vector \(E=b\partial_b\) is tangent. At \(b\ne0\), the imaginary Euler vector is \(iE=-b\partial_a\), which is not tangent. Moreover \(\alpha(\partial_x)=ib\), so its real part is zero but its imaginary part is not. Equation (9) has lost its second test. Thus (23) is positive-conic but not locally complex-conic at a nonzero covector, and it is not a complex submanifold.

### The minimal hull does not allow a half-Lagrangian boundary

*Difficulty: Advanced.*

In the zero section of \(T^*\mathbb C^n\), for \(n\ge1\), let \(S=\{\operatorname{Im}z_n=0\}\) and let \(B=\{\operatorname{Im}z_n\ge0\}\). Compute the complex span of \(TS\), exhibit its complexification map, and test involutivity of \(B\) at a boundary point.

**Solution.** The real tangent to \(S\) contains \(\partial_{x_j},\partial_{y_j}\) for \(j<n\), and \(\partial_{x_n}\). Its complex span also contains \(i\partial_{x_n}=\partial_{y_n}\), hence is the full tangent of the zero section, of complex dimension \(n\). Complexifying the real coordinates gives the map

\[
(u_1,v_1,\ldots,u_{n-1},v_{n-1},u_n)
\longmapsto
(u_1+iv_1,\ldots,u_{n-1}+iv_{n-1},u_n;0).
\tag{24}
\]

It has complex rank \(n\), and its image is the zero section near the point. This is the minimal hull.

At a boundary point of \(B\), its point cone inside the zero-section tangent satisfies \(\delta y_n\ge0\), while its two-set cone is the entire zero-section tangent plane: differences of two nonnegative \(y_n\)-coordinates can have either sign. In the real cotangent coordinates of (3), the fibre coefficient of \(dy_n\) is \(-b_n\). The covector \(\theta=-db_n\) on the ambient cotangent manifold annihilates the two-set cone. With the earlier convention \(\iota_{H\theta}\omega=-\theta\), we have \(H\theta=\partial_{y_n}\). Involutivity would require \(-H\theta=-\partial_{y_n}\) in the point cone, which it is not. Thus \(B\) is not involutive at its boundary, although its complex regular locus is Lagrangian. This is the missing hypothesis that the openness step uses.

### A crossing has a permissible boundary of real codimension two

*Difficulty: Intermediate.*

For \(X=\mathbb C\), put \(A=\{\xi=0\}\cup\{z=0\}\subset T^*X\). Identify its regular and singular parts, verify isotropy and involutivity, and compare its singular dimension with (22).

**Solution.** The equation \(z\xi=0\) makes \(A\) closed complex analytic and complex-conic. Its regular locus is the two punctured complex lines, each of complex dimension one and real dimension two. Their intersection \((0;0)\) is the only singular point, of real dimension zero. The canonical form \(\xi\,dz\) vanishes on both regular lines, so the subanalytic singular one-form criterion gives isotropy including their closure.

Each regular line is Lagrangian, hence involutive. At the crossing, the two-set cone is the full ambient underlying real \(\mathbb C^2\): a scaled point \((hz,0)\) on one line minus \((0,-h\xi)\) on the other realizes any vector \((z,\xi)\). Its annihilator is zero. The singular involutivity implication therefore has only the zero covector to test there, and it holds. Thus \(A\) is involutive everywhere. With \(n=1\), (22) says the singular dimension is at most zero, and this example attains it. The theorem removes hypersurface boundaries, not isolated intersections of complex branches.

### Complexification rank is not half of real rank

*Difficulty: Intermediate.*

Compare the real analytic maps \(f(t)=(t;0)\) and \(g(s,t)=(s+it;0)\) into \(T^*\mathbb C\). Compute their real ranks and the complex ranks of their complexifications. Explain the bound (19).

**Solution.** The map \(f\) has real rank one. Its complexification \(f_{\mathbb C}(u)=(u;0)\) has complex rank one, not zero and not a half-integer. The map \(g\) has real rank two. Its complexification \(g_{\mathbb C}(u,v)=(u+iv;0)\) has complex rank one; its differential has kernel \(\{\delta u+i\delta v=0\}\). Both differential images lie in the complex one-dimensional tangent plane to the zero section. That containment bounds the dimension of their complex spans by one. In (19) the target tangent plane has complex dimension \(n\); this is why all larger holomorphic minors vanish, even where the original map has less than maximal real rank.

### Analytic conicity alone does not give generic conormality

*Difficulty: Advanced.*

Let \(X=\mathbb C\), \(\Lambda=T^*X\), and \(Y=X\). Show that \(\Lambda\) is closed, complex analytic and complex-conic, but no open dense \(Y_0\subset Y\) satisfies \(\Lambda\cap\pi^{-1}Y_0\subset T_{Y_0}^*X\). Also show that finitely many closed analytic base conormals cannot cover \(\Lambda\).

**Solution.** All three properties of \(\Lambda\) hold because it is the whole cotangent manifold. An open subset \(Y_0\) of \(X\) has full base tangent space, so its conormal is the zero section over \(Y_0\). At every point of a nonempty such subset, \(\Lambda\) contains nonzero covectors; these are not in that conormal. Open density forces \(Y_0\) nonempty, proving failure of the generic assertion.

Every proper closed complex analytic subset of the connected complex line is discrete. A finite union of such subsets remains closed discrete locally and has a nonempty open complement. A closed analytic base equal to all of \(X\) contributes only the zero section. At a point outside the finitely many proper bases, none of their conormals has a fibre, and the all-base conormals have only the zero covector. They cannot cover the nonzero cotangent fibre there.

The omitted condition is isotropy: the whole \(T^*X\) has nonzero canonical form on its regular locus and has complex dimension two, greater than the Lagrangian dimension one. The conormal-cover theorem must retain isotropy, as in the real cover theorem and the Lagrangian microsupport applications. This counterexample shows the exact mathematical obstruction when that condition is omitted.

## The geometric input for complex constructibility

The result separates three mechanisms. Involutivity and a subanalytic isotropic bound recover real Lagrangian regularity. The two complex Euler directions make those regular tangent planes complex. Minimal complex hulls and involutive openness exclude a boundary of real codimension one; the exact analytic removal prerequisite then makes the whole set analytic. Applying this theorem to involutive microsupport will be one step in the complex constructibility criteria. The analytic conormal-cover and complex stratification arguments retain their own isotropy and geometry hypotheses.

## Sources, normalization and the boundary argument

**Classical complex microsupport geometry.** Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), §8.5, printed pp. 151–154, supplies the classical conic-isotropic/involutive analyticity mechanism. Proposition 8.5.3 first obtains complex regular tangent spaces, examines a possible boundary of real codimension one, and uses analytic extension after excluding that boundary. That proof uses a finite projection and holomorphic symmetric functions to control the regular set near a complex hull. The present lesson follows the same classical geometric question but proves its hull-containment step by proper real uniformization, maximal-rank component selection, Sard's theorem and holomorphic minors, as detailed in (18)–(20). Those are substantive proof steps, not substitutes for source credit.

**Conventions and local hypotheses.** The Astérisque convention at printed p. 151 identifies the real canonical form with twice the real part of the complex canonical form. Our explicitly defined covector map (1) identifies it with the real part itself, as checked in (2)–(4); the positive factor two is therefore not silently imported. The lesson also works in an ambient open subset with a relatively closed, locally complex-conic set. Its earlier real recovery theorem establishes subanalyticity and pure Lagrangian regularity before the complex argument. These hypotheses must be checked in the application; merely knowing positive real conicity does not supply the second Euler direction.

**The uniformization input.** Edward Bierstone and Pierre D. Milman, [*Semianalytic and subanalytic sets*, Publications Mathématiques de l’IHÉS 67 (1988), 5–42](https://www.numdam.org/article/PMIHES_1988__67__5_0.pdf), Theorem 0.1, p. 5, provides a proper real analytic surjection from a manifold of the same dimension onto a closed subanalytic set. Section 5, pp. 30–32, proves the analytic-set case and derives the subanalytic case using Proposition 3.12. Equation (18) uses this theorem, then proves the additional dense-open inverse-image property by selecting the maximal-rank components. This refinement and the later rank bound use properness and complex tangent containment separately. The foundational uniformization proof remains a prerequisite; its availability does not certify that all of its inputs have been developed in the programme.

**Complex regularity and removal.** Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter I, Lemma 7.15, p. 60, explains why a smooth submanifold with complex-invariant tangent spaces is complex analytic, using a graph and the Cauchy–Riemann equations. Ya’acov Peterzil and Sergei Starchenko, [*Complex analytic geometry and analytic-geometric categories*, author manuscript](https://math.haifa.ac.il/kobi/analytic.pdf), Theorem 4.1 and Corollary 4.2, manuscript pp. 10–11, provide the exact final removal condition on every open restriction. The proof reduces to the componentwise small-boundary theorem associated with Shiffman. Our dimension estimate (22) checks the local condition required by that result; it does not assume the residual boundary is already a complex analytic subset.

**Teaching scope.** The explicit real-covector calculation, two Euler tests, minimal hull, uniformization refinement and seven solved examples organize the lesson around the maps and hypotheses that the application needs. The analytic removal theorem and the earlier subanalytic and symplectic providers retain their own foundational proof obligations. This source account does not claim full transitive proof closure.
