# Complex conicity and analytic Lagrangian closures

A real Lagrangian tangent plane need not be a complex tangent plane. Complex fibre dilations supply the extra information: they put both an Euler vector and its imaginary multiple in the tangent plane. The real symplectic form then detects both parts of the complex canonical form. We will use this calculation to prove that an involutive set with a subanalytic isotropic bound becomes complex analytic when it is locally invariant under complex dilations.

Let \(X\) be a complex analytic manifold of complex dimension \(n\), Hausdorff and countable at infinity. Put \(P=T^*X\), with its holomorphic cotangent structure. The corresponding real manifolds have dimensions \(2n\) and \(4n\). All statements are local on components of fixed dimension. There are no sheaf coefficients or derived shifts in this geometric lesson.

We give the tangent, boundary and rank arguments explicitly. The subanalytic uniformization input is supplied by the dimension-controlled proper uniformization proof. The pure-dimensional analytic removal step is proved below from subanalytic dimension calculus and elementary holomorphic analysis. The source account below credits the classical geometric mechanism and distinguishes its conventions from ours.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Pure-dimensional analytic-removal proof added by GPT-6 Astra (OpenAI), Ultra, 9 October 2026. New original text is public domain (CC0).*

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

Here is why the earlier [real recovery argument](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#subanalyticity-forced-by-an-isotropic-containing-set) applies in this relative open setting. On the regular locus of \(A_0\), a relatively closed involutive subset of a smooth isotropic manifold is open; the [smooth openness proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#a-closed-involutive-subset-of-a-smooth-isotropic-manifold), using the [local C1 flow and its differential](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#local-c1-flow), also forces dimension \(2n\). Its intersection there is therefore a union of regular components and is subanalytic. Let \(B\) be this union. A possible remainder \(A\setminus\overline B^{\,U}\) is an open restriction of the involutive set and lies in the singular residue of \(A_0\). That residue is isotropic and has dimension less than \(2n\). The no-small-involutive-subset argument makes the remainder empty. Thus \(A=\overline B^{\,U}\), which is subanalytic. Its regular points are simultaneously isotropic and coisotropic, hence real Lagrangian of dimension \(2n\); regular density gives the middle equality in (6).

All these steps take place in arbitrarily small ambient neighborhoods. The [closed-set invariance proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#closed-set-tangent-invariance) requires closedness only in the chosen open flow domain and uses only times for which the trajectory exists there. The locally available dilation directions are sufficient; an entire orbit is not required to stay in \(U\). The dimension theory, local finiteness of regular components and singular normal-cone involutivity remain the exact prerequisites from that earlier argument. In particular, we have not assumed that an arbitrary initially non-subanalytic subset has regular points.

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

Suppose there is a \((2n-1)\)-dimensional regular part \(S\) of \(D\). Let \(S'\subset S\) be the open dense neighborhood-good locus where \((R,S)\) satisfies the ordered μ-condition. Its existence is the [good-pair result](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/microlocal-stratifications-by-removing-bad-loci.md#an-open-dense-good-locus-for-a-pair). The complement in \(S\) has smaller dimension; if (12) is an equality, \(S'\) is nonempty.

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

Suppose such a patch exists and shrink \(S'\) to that patch. Let \(C=\overline{R\setminus Z}\). It is closed and subanalytic, of pure real dimension \(2n\), with \(R\setminus Z\) open dense in \(C\). The dimension-controlled proper uniformization theorem supplies a proper real analytic map from a real analytic manifold of the same dimension onto \(C\). Its exact statement is [Bierstone–Milman, Theorem 0.1](https://www.numdam.org/article/PMIHES_1988__67__5_0.pdf#page=2). The internal proof applies to closed subanalytic subsets of finite-dimensional real analytic manifolds that are Hausdorff and countable at infinity, including the open cotangent chart used here. It retains the function-resolution and dimension-theory inputs stated in that proof.

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

The analytic removal criterion says that a relatively closed subanalytic subset of a complex manifold is complex analytic if, on every open restriction, the points where its germ is not a complex submanifold have real dimension at least two less than that restriction. An exact formulation is [Peterzil–Starchenko, author manuscript, Corollary 4.2, PDF 11](https://math.haifa.ac.il/kobi/analytic.pdf#page=11). For a pure complex regular locus this is the small-boundary theorem associated with Shiffman. The proof in the next section establishes this pure-dimensional case by constructing local holomorphic equations; the exceptional subset may be subanalytic without being complex analytic.

Apply the pure-dimensional theorem proved below to \(A\). By (6) its nonempty local restrictions have pure real dimension \(2n\). Every real regular point is complex regular by (11), so the complex singular points lie in \(D\). Equation (22) gives the required local dimension bound. Therefore \(A\) is complex analytic in \(U\).

We have proved the complete application theorem: a relatively closed, locally complex-conic involutive set with a relatively closed positive-conic subanalytic real-isotropic bound is complex analytic. Its regular locus is complex Lagrangian of complex dimension \(n\). The extension step does not assume that \(D\) is itself complex analytic. The empty set is analytic; when \(n=0\), the ambient manifold is discrete and the conclusion holds directly, with no boundary argument needed.

## Proof of removal across a subanalytic exceptional set

The small-boundary theorem is classically associated with Shiffman. [Peterzil–Starchenko, Theorem 4.1 and Corollary 4.2](https://math.haifa.ac.il/kobi/analytic.pdf#page=10) state the subanalytic criterion and explain that attribution. We now prove the pure-dimensional case used above, beginning with scalar holomorphic extension and constructing local equations for the entire closed set.

### The statement and its lower inputs

**Theorem.** Let \(A\) be a relatively closed subanalytic subset of a complex manifold \(V\). Suppose that \(E\subset A\) is relatively closed and subanalytic, that

\[
R=A\setminus E
\]

is a complex submanifold of pure complex dimension \(d\), and that \(A=\overline R\), with closure taken in \(V\). For \(d\geq1\), assume, locally at every point,

\[
\dim_{\mathbb R}E\leq 2d-2.
\tag{AR1}
\]

For \(d=0\), assume \(E=\varnothing\). Then \(A\) is a complex analytic subset of \(V\). No analyticity of \(E\) is assumed in positive dimension. Disconnected regular parts and branching over \(E\) are allowed.

For this statement a submanifold need not be closed in all of \(V\); it is embedded and locally closed. Since \(E\) and \(A\) are closed, \(R\) is open in \(A\), so its complex-manifold charts describe the entire set \(A\) near each of its points. The case \(d=0\) is immediate: \(A=R\) is locally a point. Stating this case separately avoids an ambiguity in conventions for the dimension of the empty set. The empty set is also immediate. Work henceforth with \(d\geq1\).

The subanalytic inputs are these precise forms of the existing programme calculus:

1. Local finite Boolean, closure and bounded-projection calculus; dimension is preserved by definable homeomorphisms, does not increase under definable maps, and satisfies \(\dim\overline S=\dim S\) and \(\dim(\overline S\setminus S)<\dim S\) for nonempty subanalytic \(S\).
2. A subanalytic set is a countable locally finite union of embedded real analytic manifold pieces; their dimensions are at most its dimension. In a compact bounded chart there is a finite such partition.

The local subanalytic calculus and compatible analytic partitions supply these set-theoretic facts. The [dimension and frontier proofs](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/analytic-finiteness-and-preparation/src/analytic-finiteness-for-preparation.md#dimension-fibrewise-closure-and-the-frontier) give the stated dimension inequalities.

For holomorphic functions we use the coordinate power-series expansion, identity theorem, Cauchy formula and the continuously differentiable Cauchy–Riemann characterization. Their proofs are in *Holomorphic functions of several variables*, Theorem 1.2, Theorem 2.1, Proposition 2.2 and Theorem 2.3. Locally uniform limits are holomorphic by the Cauchy formula, as also proved there in Theorem 3.1. The extension argument uses elementary Euclidean integration and smooth compactly supported bumps; it proves the special convolution convergence it needs directly.

Here is also a direct proof of the inverse/implicit theorem used below. After translating and multiplying by the inverse derivative, write a holomorphic map with invertible derivative as \(G(z)=z+h(z)\), with \(h(0)=0\) and \(Dh(0)=0\). On a sufficiently small closed complex ball of radius \(r\), \(\|Dh\|\leq1/2\). Integration along segments gives \(|h(z)-h(z')|\leq|z-z'|/2\). For \(|y|<r/4\), iterate \(z_{j+1}=y-h(z_j)\) from \(z_0=0\). This stays in the closed ball, and successive differences shrink by a factor at most \(1/2\); their geometric sum proves convergence and uniqueness of the fixed point in the complete closed ball. The iterates are holomorphic in \(y\), and the same geometric bound makes their convergence uniform on smaller target balls. The limit is holomorphic by the Cauchy formula and satisfies \(G(z(y))=y\). The inequality also gives injectivity of \(G\) on the ball. This is a holomorphic local inverse. Applying it to \((g,z_2,\ldots,z_d)\), after relabeling a nonzero partial derivative of \(g\), proves the complex implicit theorem for one equation. No analytic-set extension result enters these coordinate arguments.

### Two elementary consequences of dimension

Put \(q=2d\). Call a subset of \(\mathbb R^q\) *thin* in this proof if it is contained in a countable union of \(C^1\) images of open subsets of \(\mathbb R^s\), with \(s\leq q-2\). A zero-dimensional domain means a point. The image maps need not be embeddings or have constant rank.

**Ball covers.** If \(F\) is thin, then \(\mathcal H^{q-1}(F)=0\). Indeed, exhaust every parameter domain by compact cubes on which the map is Lipschitz. Subdividing an \(s\)-cube into cubes of side \(h\) gives \(O(h^{-s})\) image sets of diameter \(O(h)\). The sum of their \((q-1)\)-st powers is \(O(h^{q-1-s})\), which tends to zero. Countable subadditivity proves the assertion. In particular \(F\) has Lebesgue measure zero. For every compact subset of \(F\), every \(\delta>0\), and every ambient open neighborhood, there is a finite open ball cover inside that neighborhood, of radii \(r_i<\delta\), with \(\sum_i r_i^{q-1}<\delta\). Obtain a countable Hausdorff cover first, enlarge its radii by an arbitrarily small factor to make it open, and take a finite subcover of the compact set.

**Connected complements.** If \(D\subset\mathbb R^q\) is an open convex ball and \(F\subset D\) is thin, then \(D\setminus F\) is path connected. For \(a\notin F\), every endpoint \(c\) whose segment \([a,c]\) meets \(F\) belongs to

\[
\{a+t(y-a):y\in F,\ t\geq1\}.
\tag{AR2}
\]

Each parameterized piece of this set is a countable union of \(C^1\) images of dimension at most \(q-1\), after subdividing \([1,\infty)\) into bounded intervals. The same cube argument makes it Lebesgue null in \(\mathbb R^q\). Given \(a,b\in D\setminus F\), choose \(c\in D\) outside the two null sets (AR2). Convexity keeps \([a,c]\cup[c,b]\) in \(D\), and the choice keeps it disjoint from \(F\).

### Bounded holomorphic functions extend across a thin closed set

**Lemma.** Let \(D\subset\mathbb C^d\) be open, let \(F\subset D\) be relatively closed and thin, and let \(f\) be locally bounded on \(D\), holomorphic on \(D\setminus F\). Here local boundedness means boundedness on the complement of \(F\) near each point of \(D\). Then \(f\) extends uniquely to a holomorphic function on \(D\).

**Proof.** Work in a relatively compact open part where \(|f|\leq M\), and extend it by zero on \(F\). This gives a locally bounded measurable function \(u\). Fix a smooth compactly supported test function \(\varphi\), and choose a compact neighborhood \(K\) of its support in this open part. Cover \(F\cap K\) by balls as above, with doubled balls still in the open part. Choose smooth functions \(0\leq\chi_i\leq1\), equal to one on the covering balls, supported on their doubles, and satisfying

\[
\int |\nabla\chi_i|\leq C_q r_i^{q-1}.
\]

Set \(\chi=1-\prod_i(1-\chi_i)\). It is one near \(F\cap K\), and

\[
\int |\nabla\chi|\leq C_q\delta,
\qquad
\operatorname{vol}(\operatorname{supp}\chi)
\leq C_q\sum_i r_i^q\leq C_q\delta^2.
\tag{AR3}
\]

The test function \((1-\chi)\varphi\) has compact support in \(D\setminus F\). Integration by parts there, where \(f\) is holomorphic, gives for each coordinate \(j\)

\[
\int u\,\partial_{\bar z_j}\varphi
=\int u\chi\,\partial_{\bar z_j}\varphi
+\int u\varphi\,\partial_{\bar z_j}\chi.
\]

The absolute value is bounded by

\[
C_qM\bigl(\delta^2\|\nabla\varphi\|_\infty
+\delta\|\varphi\|_\infty\bigr),
\]

so it is zero on letting \(\delta\) tend to zero. Thus every distributional derivative \(\partial_{\bar z_j}u\) vanishes.

For completeness this distributional conclusion has a holomorphic representative without an additional removability theorem. Choose a nonnegative smooth function \(\rho\) supported in the unit ball with integral one and set \(\rho_\epsilon(x)=\epsilon^{-q}\rho(x/\epsilon)\). Such a function is obtained by normalizing \(\exp[-1/(1-|x|^2)]\) on the unit ball and extending it by zero. Convolve \(u\) with \(\rho_\epsilon\) on successively smaller interior domains. Differentiation of the smooth compactly supported kernel under the integral makes \(u_\epsilon\) smooth. Testing the already proved distributional Cauchy–Riemann identity against translates of that kernel shows that every \(\partial_{\bar z_j}u_\epsilon\) is zero. Thus \(u_\epsilon\) is holomorphic and bounded by \(M\).

Here local \(L^1\) convergence can be checked without a general convolution theorem. On a fixed compact set, cover the compact exceptional trace in a slightly larger neighborhood by finitely many balls of arbitrarily small total volume. Outside their union the compact set stays a positive distance from \(F\), and \(u=f\) is uniformly continuous on a compact neighborhood there. Consequently \(u_\epsilon\to u\) uniformly on that part. On the union of the balls the integral of \(|u_\epsilon-u|\) is at most \(2M\) times their volume. First choose the volume small and then \(\epsilon\) small. This proves \(u_\epsilon\to u\) in local \(L^1\).

On a compact set \(K_0\) inside a larger compact polydisc region \(K_1\), the iterated holomorphic mean inequality gives

\[
\sup_{K_0}|u_\epsilon-u_\eta|
\leq C_{K_0,K_1}\|u_\epsilon-u_\eta\|_{L^1(K_1)}.
\tag{AR4}
\]

To get this inequality, choose a common small polydisc around every point of \(K_0\), contained in \(K_1\), and apply the mean inequality in each complex variable; it follows from the Cauchy formula by averaging the radii. Hence the convolutions converge locally uniformly to a holomorphic function, by the same Cauchy formula. The limit represents \(u\), and agrees with \(f\) on \(D\setminus F\), since two continuous functions equal almost everywhere on that open set agree everywhere. Such local representatives agree on overlaps, because \(D\setminus F\) is dense, and therefore glue. Density also proves uniqueness. \(\square\)

### A projection that is proper near the point to be filled

Fix \(p\in A\), take a coordinate ball in \(\mathbb C^N\), and put \(p=0\). If \(N=d\), the set \(R\) is open in the ambient manifold. In a small convex ball \(D\) about \(p\), the set \(E\) is thin, so \(D\setminus E\) is connected. Its intersection with \(A\) is open because it is \(R\cap D\), closed because \(A\) is closed, and nonempty because \(R\) is dense in \(A\). It is therefore all of \(D\setminus E\), whose closure is \(D\); closedness then gives \(D\subset A\). We may assume \(N>d\), and write \(k=N-d\).

By closure invariance of subanalytic dimension, \(\dim_{\mathbb R}A=2d\) in a sufficiently small neighborhood of \(0\). Consider the lifted punctured set

\[
T=\{(r,u):0<r<\epsilon,\ |u|=1,\ ru\in A\}.
\]

It is subanalytic and is definably homeomorphic to \(A\cap\{0<|x|<\epsilon\}\). The link of limiting secant directions

\[
L=\{u:(0,u)\in\overline T\}
\tag{AR5}
\]

is compact and subanalytic. The strict-frontier inequality, applied to \(T\), gives

\[
\dim_{\mathbb R}L\leq 2d-1.
\tag{AR6}
\]

We claim that a surjective complex-linear map \(P:\mathbb C^N\to\mathbb C^d\) can be chosen with \(\ker P\cap L=\varnothing\), and with rank \(d\) at some point of every connected component of \(R\) in the coordinate ball.

First partition \(L\) into its finitely many smooth pieces. In the space of all complex \(d\)-by-\(N\) matrices, of real dimension \(2dN\), the incidence condition \(Pu=0\) imposes \(2d\) independent real linear equations for each nonzero \(u\). Over a piece of dimension \(s\), its solution incidence is a smooth vector bundle of dimension \(2dN-2d+s\leq2dN-1\). Its projection to matrix space is Lebesgue null: use countably many smooth coordinate patches and the elementary cube estimate above. Thus some matrices avoid \(L\). The avoiding set is open, because \(L\) is compact. Surjective matrices are dense, since an appropriate maximal minor is a nonzero polynomial.

The complex manifold \(R\) has countably many connected components. Select a point \(x_\nu\) in each. For every fixed complex tangent plane \(T_{x_\nu}R\), the condition that \(P\) restrict to an isomorphism there is the complement of the zero set of a nonzero polynomial in the entries of \(P\). It is open dense. Countably many such conditions can be imposed inside the nonempty open set just obtained: choose a closed ball inside it, then nested positive-radius closed balls, the \(\nu\)-th contained in the \(\nu\)-th open dense set and the preceding ball's interior, with diameters tending to zero. Their common point satisfies every condition. This elementary nested-ball argument supplies the required \(P\).

Avoidance of \(L\) yields constants \(c>0\) and \(\epsilon_0>0\) such that

\[
|Px|\geq c|x|\qquad
(x\in A,\ 0<|x|<\epsilon_0).
\tag{AR7}
\]

Otherwise, choosing successively smaller neighborhoods of zero, there would be a sequence \(x_\nu\in A\setminus\{0\}\) with \(x_\nu\to0\) and \(|Px_\nu|/|x_\nu|\to0\). A convergent subsequence of its unit directions would lie in \(L\cap\ker P\), a contradiction.

Complete \(z=Px\) to complex linear coordinates \((z,w)\in\mathbb C^d\times\mathbb C^k\). Choose a small fibre ball \(B=\{|w|<r\}\) and then a sufficiently small base ball \(D\) about zero. Require that the closed cylinder lies inside the original coordinate ball and the region where (AR7) holds. Norm equivalence and (AR7) imply \(|w|\leq C|z|\) on \(A\) there. By taking the base radius less than \(r/(2C)\), arrange

\[
A\cap(D\times\partial B)=\varnothing.
\tag{AR8}
\]

Replace \(A\) by its intersection with \(D\times B\). The projection

\[
\pi:A\longrightarrow D
\tag{AR9}
\]

is proper. For a compact \(K\subset D\), its preimage is a closed subset of the compact cylinder \(K\times\overline B\), and (AR8) keeps every limiting point in \(B\). No discreteness of the exceptional fibres has been assumed.

### The exceptional values and the finite holomorphic covering

Let

\[
C=\{x\in R:\operatorname{rank}_{\mathbb C}d(\pi|_R)_x<d\},
\qquad F=\pi(E\cup C),
\tag{AR10}
\]

with all sets restricted to the cylinder. The set \(C\) is closed in \(R\), so \(E\cup C\) is closed in \(A\). Properness of (AR9) makes \(F\) closed in \(D\). Here is the needed size estimate, without presuming that \(F\) or \(E\) is complex analytic.

By (AR1) and the analytic partition theorem, \(E\) is covered by countably many smooth parameterized pieces of real dimension at most \(2d-2\). On a connected complex coordinate patch in any connected component of \(R\), the holomorphic determinant of \(d\pi\) is not identically zero. Indeed, the exterior form \(d\pi_1\wedge\cdots\wedge d\pi_d\) is nonzero at the chosen point of that component; the identity theorem, along overlapping charts, forbids its vanishing on any open patch.

The zero set of a nonzero holomorphic function \(g\) on a connected coordinate domain is covered by countably many smooth complex hypersurface patches. To see the asserted covering, take a zero \(x\). Some Taylor coefficient is nonzero by the identity theorem; let its least order be \(m\geq1\). Choose a multi-index \(\alpha\) of order \(m-1\) for which a first derivative of \(\partial^\alpha g\) is nonzero at \(x\). Then

\[
\partial^\alpha g(x)=0,
\qquad d(\partial^\alpha g)_x\ne0.
\]

The complex implicit function theorem makes the zero set of \(\partial^\alpha g\) a smooth complex hypersurface near \(x\). For each of the countably many \(\alpha\), the noncritical part of this zero set has a countable chart cover. These patches cover all zeros of \(g\). The patches need not lie in the zero set of \(g\); containment of its zeros in their union is the only assertion needed.

Apply this observation to the determinant on countably many charts of \(R\). It shows that \(C\), and hence \(E\cup C\), is contained in countably many smooth parameterized pieces of real dimension at most \(2d-2\). Composing those parameterizations with the linear projection makes \(F\) thin in \(D\). It has empty interior, its complement is path connected, and the extension lemma applies to bounded holomorphic functions on that complement.

On \(\pi^{-1}(D\setminus F)\), the complex inverse function theorem makes \(\pi\) a local biholomorphism. Properness makes each fibre finite: it is both compact and discrete. A proper local homeomorphism with finite fibres is a covering of its image. To check this explicitly over a fibre \(\{x_1,\ldots,x_m\}\), choose disjoint inverse-coordinate neighborhoods of these points. If no smaller base neighborhood excluded additional preimages outside them, a sequence of such preimages over base points converging to the chosen value would, by properness, have a limiting preimage outside their union. This contradicts the displayed complete fibre. Shrinking now gives an evenly covered neighborhood.

The covering image is open and closed in \(D\setminus F\). It is nonempty: \(R\) is dense in \(A\), the noncritical points are dense in each component of \(R\), and their local images are open, so one such image meets \(D\setminus F\). Consequently the image is all of the connected set \(D\setminus F\). Its sheet number is a fixed finite integer \(m\geq1\).

We also record the density that will be needed at exceptional fibres:

\[
A=\overline{\pi^{-1}(D\setminus F)}
\quad\text{inside }D\times B.
\tag{AR11}
\]

Indeed, an arbitrary neighborhood of a point of \(A\) meets \(R\); the noncritical points are dense in \(R\); near a noncritical point \(\pi\) is open; and a nonempty open base image meets \(D\setminus F\). This reasoning remains valid in every prescribed neighborhood, proving (AR11).

### Equations that retain the complete fibre points

Over an evenly covered neighborhood write the sheets as

\[
w=a_1(z),\ldots,a_m(z),\qquad a_i(z)\in B\subset\mathbb C^k.
\]

For an auxiliary vector \(\lambda=(\lambda_1,\ldots,\lambda_k)\), use the complex bilinear pairing \(\lambda\cdot w=\sum_j\lambda_jw_j\), and form

\[
Q(z,w,\lambda)
=\prod_{i=1}^m\bigl(\lambda\cdot(w-a_i(z))\bigr).
\tag{AR12}
\]

Permuting the sheets does not change this polynomial, so its coefficients as a polynomial in \((w,\lambda)\) are single-valued holomorphic functions on \(D\setminus F\). They are bounded there: \(m\) is fixed and every \(a_i\) lies in the fixed bounded ball \(B\). Extend every one of its finitely many coefficients by the preceding lemma. Denote the resulting polynomial, with coefficients holomorphic on \(D\), by \(\widetilde Q\).

Expand only in \(\lambda\):

\[
\widetilde Q(z,w,\lambda)
=\sum_{|\beta|=m}q_\beta(z,w)\lambda^\beta.
\]

The finitely many functions \(q_\beta\) are holomorphic on \(D\times\mathbb C^k\). Let

\[
Y=\{(z,w)\in D\times B:q_\beta(z,w)=0
\text{ for every }\beta\}.
\tag{AR13}
\]

This is a complex analytic subset. For \(z\notin F\), it is exactly the original fibre: a product of linear polynomials in \(\lambda\) vanishes identically precisely when one of its factors is the zero polynomial, because \(\mathbb C[\lambda_1,\ldots,\lambda_k]\) is an integral domain. Thus (AR12) is identically zero in \(\lambda\) precisely when \(w=a_i(z)\) for some \(i\). This is why we use the full vector pairing; separate coordinate root equations could add points made from coordinates belonging to different sheets.

By (AR11), closedness of \(Y\), and equality over \(D\setminus F\), we have \(A\subset Y\). For the reverse inclusion fix \((z_0,w_0)\in Y\). Choose \(z_\nu\in D\setminus F\) tending to \(z_0\), enumerate each finite fibre arbitrarily as \(a_{1,\nu},\ldots,a_{m,\nu}\), and take a subsequence on which every coordinate of this finite tuple converges in \(\overline B\). Write its limit as \(b_1,\ldots,b_m\). Closedness of \(A\) and (AR8) give

\[
(z_0,b_i)\in A,\qquad b_i\in B.
\]

Continuity of the extended coefficients and the finite product gives the identity

\[
\widetilde Q(z_0,w,\lambda)
=\prod_{i=1}^m\bigl(\lambda\cdot(w-b_i)\bigr).
\tag{AR14}
\]

Since \((z_0,w_0)\in Y\), the left side is the zero polynomial in \(\lambda\). The integral-domain argument again yields \(w_0=b_i\) for some \(i\). Therefore \((z_0,w_0)\in A\), proving \(Y\subset A\).

We have proved \(A=Y\) near the arbitrary point \(p\). This proves the theorem, including discreteness of the exceptional fibres as a consequence, not a premise. \(\square\)

### Application to complex conicity

Take \(A\) to be the closed subanalytic involutive set considered above, \(R\) its dense real regular part and \(E=D=A\setminus R\). Its earlier proof gives pure real dimension \(2n\), makes every tangent plane of \(R\) complex, and proves that \(R\) is a complex submanifold of dimension \(n\). Equation (22) gives \(\dim_{\mathbb R}D\leq2n-2\) on every local restriction, and the subanalytic regular-locus provider makes \(D\) closed and subanalytic. Thus the theorem above with \(d=n\) supplies exactly the final analyticity step. The conicity, involutivity and isotropic-bound hypotheses are exactly those used in the preceding argument.

The theorem proved here is the pure-dimensional case used by this application. Peterzil–Starchenko's broader criterion also permits regular components of differing dimensions.

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

The result separates three mechanisms. Involutivity and a subanalytic isotropic bound recover real Lagrangian regularity. The two complex Euler directions make those regular tangent planes complex. Minimal complex hulls and involutive openness exclude a boundary of real codimension one; the proved small-boundary removal step then makes the whole set analytic. Applying this theorem to involutive microsupport will be one step in the complex constructibility criteria. The analytic conormal-cover and complex stratification arguments retain their own isotropy and geometry hypotheses.

## Sources, normalization and the boundary argument

**Classical complex microsupport geometry.** Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=154), §8.5, printed pp. 151–154, supplies the classical conic-isotropic/involutive analyticity mechanism. Proposition 8.5.3 first obtains complex regular tangent spaces, examines a possible boundary of real codimension one, and uses analytic extension after excluding that boundary. That proof uses a finite projection and holomorphic symmetric functions to control the regular set near a complex hull. The present lesson follows the same classical geometric question but proves its hull-containment step by proper real uniformization, maximal-rank component selection, Sard's theorem and holomorphic minors, as detailed in (18)–(20). Those are substantive proof steps, not substitutes for source credit.

**Conventions and local hypotheses.** The Astérisque convention at printed p. 151 identifies the real canonical form with twice the real part of the complex canonical form. Our explicitly defined covector map (1) identifies it with the real part itself, as checked in (2)–(4); the positive factor two is therefore not silently imported. The lesson also works in an ambient open subset with a relatively closed, locally complex-conic set. Its earlier real recovery theorem establishes subanalyticity and pure Lagrangian regularity before the complex argument. These hypotheses must be checked in the application; merely knowing positive real conicity does not supply the second Euler direction.

**The uniformization input.** Edward Bierstone and Pierre D. Milman, [*Semianalytic and subanalytic sets*, Publications Mathématiques de l’IHÉS 67 (1988), 5–42](https://www.numdam.org/article/PMIHES_1988__67__5_0.pdf#page=2), Theorem 0.1, p. 5, provides a proper real analytic surjection from a manifold of the same dimension onto a closed subanalytic set. Section 5, pp. 30–32, proves the analytic-set case and derives the subanalytic case using Proposition 3.12. Equation (18) uses this theorem, then proves the additional dense-open inverse-image property by selecting the maximal-rank components. This refinement and the later rank bound use properness and complex tangent containment separately. The programme proof is Dimension-controlled proper uniformization, steps N1–N10. It reduces compact torus presentations to the dimension of the image and glues a locally finite family of compact presentations properly; the lower function-resolution and dimension inputs are identified there.

**Complex regularity and removal.** Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=60), Chapter I, Lemma 7.15, p. 60, explains why a smooth submanifold with complex-invariant tangent spaces is complex analytic, using a graph and the Cauchy–Riemann equations. Ya’acov Peterzil and Sergei Starchenko, [*Complex analytic geometry and analytic-geometric categories*, author manuscript](https://math.haifa.ac.il/kobi/analytic.pdf#page=11), Theorem 4.1 and Corollary 4.2, manuscript pp. 10–11, provide the exact final removal condition on every open restriction. Their proof reduces to the componentwise small-boundary theorem associated with Shiffman. Our dimension estimate (22) checks the local condition, and the pure-dimensional proof above supplies the removal step used here. It extends bounded holomorphic coefficients across a thin closed set and uses vector-valued sheet equations to recover each entire fibre, including the exceptional fibres. The residual boundary is not assumed complex analytic.

**Teaching scope.** The explicit real-covector calculation, two Euler tests, minimal hull, uniformization refinement and seven solved examples organize the lesson around the maps and hypotheses that the application needs. The pure-dimensional removal argument is proved here from the stated subanalytic dimension and elementary holomorphic inputs. The earlier subanalytic and symplectic providers identify the remaining foundations of the conicity argument.
