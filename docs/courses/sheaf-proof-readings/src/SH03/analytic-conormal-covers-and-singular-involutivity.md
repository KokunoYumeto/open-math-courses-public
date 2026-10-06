# Analytic conormal covers and singular involutivity

The conormal of a singular analytic set consists of limits of conormals at its smooth points. Those limits can be much smaller than the whole cotangent fibre over a singular point. We will prove that this conormal is analytic, explain why its regular Lagrangian geometry also gives the real involutivity condition at singular points, and cover any closed analytic isotropic cone by finitely many such conormals. The finite family can contain bases with infinitely many components.

Let \(X\) be a complex manifold of complex dimension \(n\), Hausdorff and countable at infinity. Put \(P=T^*X\), \(\pi:P\to X\), and use

\[
\alpha=\sum_j\xi_j\,dz_j,\qquad
\Omega=d\alpha=\sum_jd\xi_j\wedge dz_j,\qquad
\omega=\operatorname{Re}\Omega.
\tag{1}
\]

We use the real covector identification and analytic-piece convention of Complex conicity and analytic Lagrangian closures. Fibre conicity in this lesson means invariance under all \(\mathbb C^*\) dilations. Isotropy of a subanalytic cone means vanishing of the canonical form in the singular one-form sense; on a closed complex analytic cone this is equivalent to vanishing of \(\alpha\) on its regular locus. There are no coefficient or derived-shift assumptions in this geometric lesson.

The cover and generic-base statements below explicitly require isotropy. The full cotangent bundle gives a counterexample when that hypothesis is omitted. The source account below identifies the analytic-ideal, specialization and image theorems used in the constructions.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## The exact analytic geometry inputs

We use local finite generation of reduced analytic ideals, locally finite irreducible components, analytic regular and singular loci, and constancy of dimension on an irreducible component. Closure of an analytic set after deleting an analytic subset retains precisely the components not contained in the deleted set. The complex deformation lesson proves the application of that component rule to real positive normal cones; in particular, those cones for analytic pieces are complex analytic and complex-conic.

Two further geometry inputs are needed here. A proper holomorphic map carries a closed analytic subset to a closed analytic subset. A holomorphic image that is subanalytic has real dimension twice the maximum generic complex rank on the regular irreducible components of its source. For the exact image and rank contracts see [Peterzil–Starchenko, Theorem 6.1 and Claim 1 in its proof, manuscript PDF 16–17](https://math.haifa.ac.il/kobi/analytic.pdf). We use these as explicit prerequisites; their underlying dimension and analytic removal machinery remains an open dependency.

We also use the following specialization contract. In a smooth complex Poisson manifold, if the reduced ideal of a closed analytic set is closed under the Poisson bracket and a holomorphic function has zero Hamiltonian field, intersecting that set with the function's zero fibre again gives an analytic set with bracket-closed reduced ideal. This is [Kashiwara–Monteiro-Fernandes, Corollary 1.1.14 PDF 6](https://www.numdam.org/item/10.24033/bsmf.2062.pdf). Its Thom stratification input is a further explicit open prerequisite. The arguments below show exactly how this contract gives the real singular condition; regular coisotropy alone is not used as a definition of that condition.

## From regular coisotropy to the real normal-cone condition

Recall the Hamiltonian convention

\[
\iota_{H\theta}\omega=-\theta.
\tag{2}
\]

For a locally closed real subset \(S\subset P\), involutivity at \(p\in S\) means

\[
C_p(S,S)\subset\ker\theta
\quad\Longrightarrow\quad
-H\theta\in C_p(S)
\qquad(\theta\in T_p^*P\text{ real}).
\tag{3}
\]

The first cone uses differences of two points of \(S\), and the second uses differences from the fixed point \(p\); both use positive real scales. Their precise definitions and signs are in Involutive subsets of subanalytic isotropic sets.

**Theorem.** A closed complex analytic subset \(S\subset P\) whose regular tangent spaces are complex coisotropic satisfies (3). No fibre-conicity assumption is needed for this theorem.

**Proof.** First consider holomorphic functions \(g,h\) vanishing on \(S\). At a regular point their differentials annihilate \(TS\). Coisotropy makes their Poisson bracket zero there. Regular density and continuity give

\[
\{\mathcal I_S,\mathcal I_S\}\subset\mathcal I_S,
\tag{4}
\]

where \(\mathcal I_S\) is the reduced ideal. Conversely, (4) implies coisotropy at a regular point because differentials of its local defining functions span its conormal. This converse will also be used for a specialized cone.

Fix \(p\). Use canonical holomorphic coordinates on \(P\) near \(p\), so that \(\Omega\) has constant coefficients. On the open chart where \(p+tv\) stays in that coordinate neighborhood, take the accessible analytic closure

\[
D=\overline{\{(v,t):t\ne0,\ p+tv\in S\}}.
\tag{5}
\]

The component rule makes \(D\) analytic and excludes components existing only at \(t=0\). Its central fibre is exactly the positive-real point cone,

\[
D\cap\{t=0\}=C_p(S)\times\{0\}.
\tag{6}
\]

For (6), apply the earlier analytic pair-normal-cone argument to \((S,\{p\})\). Its positive-power reparameterization is what identifies the complex central fibre with the cone using positive real scales.

Give the \(v\) coordinates the constant Poisson tensor associated with \(\Omega_p\), and make \(t\) a Casimir: its bracket with every function is zero. At \(t\ne0\), the map \(v\mapsto p+tv\) scales the symplectic form by \(t^2\). Each slice of (5) is consequently coisotropic. For two local holomorphic functions vanishing on \(D\), compute their bracket using only their \(v\) derivatives. It vanishes at every regular point of every nonzero slice. Those points are dense in \(D\), so the bracket vanishes on all of \(D\). Thus its reduced ideal is bracket-closed.

Apply the stated specialization contract to the Casimir \(t\). We conclude that

\[
C=C_p(S)\subset T_pP
\quad\text{is complex analytic and coisotropic at its regular points}
\tag{7}
\]

for the constant form \(\Omega_p\). This step concerns the point cone, including its singular points, rather than a guessed limiting tangent space of \(S\).

Suppose now that \(\theta\) satisfies the premise in (3). Since \(p\in S\), every sequence defining \(C_p(S)\) also defines a two-set sequence with second point \(p\). Thus \(\theta\) annihilates \(C\). The cone is complex-conic by the analytic normal-cone theorem. Therefore the complex-linear covector

\[
\ell(v)=\theta(v)-i\theta(iv)
\tag{8}
\]

vanishes on \(C\): both \(v\) and \(iv\) belong to that cone. Let \(u\) be the constant complex Hamiltonian vector satisfying \(\iota_u\Omega_p=-\ell\). Its underlying real vector is \(H\theta\), by taking real parts of that equality and using nondegeneracy of \(\omega_p\).

At a regular point of \(C\), \(d\ell\) annihilates its tangent space. By (7), \(u\) belongs to that tangent space. Hence the constant derivation \(u\) preserves the reduced analytic ideal of \(C\): for any ideal function its derivative is zero on the regular locus, then on all of \(C\). To verify flow preservation also at the vertex, choose local ideal generators \(g_1,\ldots,g_r\) near zero. There are holomorphic coefficients \(a_{ij}\) with

\[
u(g_i)=\sum_j a_{ij}g_j.
\tag{9}
\]

Along the real translation \(w(s)=su\), the vector \((g_i(w(s)))_i\) solves the corresponding linear ordinary differential equation with initial value zero. Uniqueness gives \(su\in C\) for sufficiently small positive and negative \(s\). The local C1 uniqueness proof applies to this equation by adjoining the time variable: the real system is \((s,g)'= (1,A(s)g)\), with real and imaginary parts of the holomorphic matrix coefficients. Its zero initial-value solution is therefore \(g=0\) in both time directions. Positive conicity then gives \(-u\in C\). As \(u=H\theta\) in real coordinates, this is (3). If \(u=0\), the conclusion holds because the cone contains zero. All reasoning was local near the arbitrary point \(p\). \(\square\)

For an analytic set with Lagrangian regular tangent spaces, coisotropy is available and the theorem gives real singular involutivity. In the conic case, regular symplectic isotropy makes \(\alpha\) vanish as well: the Euler vector \(E=\sum\xi_j\partial_{\xi_j}\) is tangent and \(\iota_E\Omega=\alpha\). Singular one-form calculus extends this vanishing from the dense regular locus. Thus a closed analytic conic set with Lagrangian regular locus is Lagrangian also in the earlier real singular sense.

## The tangent graph and the analytic conormal closure

For a closed complex analytic \(S\subset X\), define

\[
\Sigma_S=\overline{T^*_{S_{\mathrm{reg}}}X}^{\,T^*X}.
\tag{10}
\]

We prove that \(\Sigma_S\) is closed complex analytic, complex-conic, and pure of complex dimension \(n\), unless it is empty. Its regular tangent spaces are Lagrangian, and the preceding theorem gives its real singular involutivity.

First assume \(S\) is pure of complex dimension \(d\). In a coordinate chart \(U\subset X\), choose holomorphic generators \(f_1,\ldots,f_r\) for its **reduced ideal**. Let \(\operatorname{Gr}_d(\mathbb C^n)\) be the compact complex Grassmannian. The incidence conditions

\[
x\in S,\qquad df_j(x)|_L=0\quad(1\le j\le r)
\tag{11}
\]

define an analytic subset of \(U\times\operatorname{Gr}_d(\mathbb C^n)\). Over \(S_{\mathrm{reg}}\), the common kernel of the differentials is precisely \(T_xS\), of dimension \(d\); thus (11) has the unique plane \(L=T_xS\) there. Delete the analytic inverse image of \(S_{\mathrm{sing}}\), then take the component closure. The result is the analytic tangent graph

\[
\Gamma_S=\overline{\{(x,T_xS):x\in S_{\mathrm{reg}}\}}.
\tag{12}
\]

Its projection to \(S\) is proper because the Grassmannian is compact. Each retained component has dimension \(d\) and contains a dense regular tangent-graph part.

Over \(\Gamma_S\), impose \(\xi|_L=0\). This is the restriction of a holomorphic vector bundle of rank \(n-d\); its total incidence set

\[
E_S=\{(x,L,\xi):(x,L)\in\Gamma_S,\ \xi|_L=0\}
\tag{13}
\]

is analytic. The map \(q(x,L,\xi)=(x,\xi)\) is proper: over a compact cotangent set the omitted Grassmann coordinates remain compact. The proper holomorphic image theorem therefore makes \(q(E_S)\) closed analytic.

This image equals (10). It is closed and contains the ordinary regular conormal. Conversely, take \((x,L,\xi)\in E_S\). By (12), choose \(x_k\in S_{\mathrm{reg}}\) with \((x_k,T_{x_k}S)\to(x,L)\). Continuity of the annihilator subspaces allows \(\xi_k\in(T_{x_k}S)^\perp\) with \(\xi_k\to\xi\). For example, in a fixed Hermitian metric project \(\xi\) onto these annihilator spaces. Hence \((x,\xi)\) is a limit of ordinary conormals, as required.

Each component of (13) has dimension \(d+(n-d)=n\). On its dense regular conormal part, \(q\) is one-to-one and identifies that part with an \(n\)-dimensional ordinary conormal. Each proper analytic component image is therefore of dimension \(n\). Properness keeps the image family locally finite. This proves purity of \(\Sigma_S\). For nonpure \(S\), apply this argument to the locally finite irreducible components, grouped by their finitely many possible dimensions. The closure of the whole regular conormal is the union of their conormal closures: intersections and smaller component singularities can be deleted without changing those closures. The same proper and local-finiteness argument proves analyticity and purity in this case.

On an ordinary conormal \(\alpha\) vanishes, since its covector annihilates every projected tangent vector. It consequently vanishes on the closure by singular one-form calculus. At a regular point of the analytic closure, differentiation gives \(\Omega|_{T\Sigma_S}=0\). Purity gives complex dimension \(n\), so that regular tangent space is Lagrangian. Fibre scaling preserves the ordinary conormal and its closure. The result about real singular involutivity now applies to \(\Sigma_S\), proving every claimed property.

The Grassmann incidence retains limiting tangent planes. It does not replace them by the possibly larger tangent space obtained by linearizing equations at a singular point.

## What the ideal-generator formula actually requires

With the reduced ideal generators used in (11), the exact formula is

\[
\Sigma_S\cap T^*U
=\overline{\left\{\left(x,\sum_{j=1}^r\lambda_jdf_j(x)\right):
x\in S\cap U,\ \lambda_j\in\mathbb C\right\}}^{\,T^*U}.
\tag{14}
\]

At a regular point, the differential span is exactly the conormal, which proves one inclusion after closure. At a singular point, fix the finitely many coefficients \(\lambda_j\). Choose regular \(x_k\to x\). Then \(\sum_j\lambda_jdf_j(x_k)\to\sum_j\lambda_jdf_j(x)\). Thus every point of the set inside the bar already lies in the regular conormal closure, proving the other inclusion. Arbitrarily large coefficients are allowed before taking closure; they are sometimes necessary for a nonzero limiting covector.

Equations having the correct zero set do not suffice if their differentials fail to generate the regular conormal. For \(S=\{0\}\subset\mathbb C\), the equation \(z^2=0\) has differential zero on all of \(S\). Its differential-span closure is only \((0,0)\), whereas \(\Sigma_S=T_0^*\mathbb C\). Generators of the reduced ideal, here \(z\), give the correct formula. Thus the differential-span construction requires generators of the reduced ideal, not merely equations with the right zero set.

## Conicity makes the projected component family locally finite

Let \(\Lambda\subset P\) be closed complex analytic and complex-conic. Each irreducible component \(\Lambda_i\) is itself complex-conic. To check this, choose a regular point belonging to that component alone. For \(\lambda\) near 1, its image remains in the unique component near the point, so \(m_\lambda(\Lambda_i)=\Lambda_i\). More explicitly, the component image and \(\Lambda_i\) have a common nonempty relatively open germ, so irreducibility identifies them. The stabilizer of \(\Lambda_i\) is thus an open subgroup of the connected group \(\mathbb C^*\); it is the whole group.

Closedness and \(\lambda\to0\) put the zero covector over every projected point into the same component. Consequently,

\[
N_i=\pi(\Lambda_i)
=\{x:(x,0)\in\Lambda_i\}
\tag{15}
\]

is closed complex analytic, by inverse image under the holomorphic zero section. Projection need not be proper here. The equality in (15), rather than a general nonproper image theorem, proves closedness and analyticity of this particular image.

The family \((N_i)\) is locally finite on \(X\). A neighborhood of \((x_0,0)\) in \(P\) meets only finitely many \(\Lambda_i\). Choose it to contain a product of a base neighborhood with a small fibre ball. If \(N_i\) meets that base neighborhood, (15) puts a point of \(\Lambda_i\) at zero in the product. Thus only those finitely many projected components can occur. This zero-section argument prevents components escaping to infinity in the fibres from creating an accumulation of projected bases.

Let

\[
d_i=\max\operatorname{rank}_{\mathbb C}
(d\pi|_{T\Lambda_{i,\mathrm{reg}}}).
\tag{16}
\]

The holomorphic rank-dimension prerequisite, applied to the closed analytic image (15), gives \(\dim_{\mathbb C}N_i=d_i\). The image is irreducible: two proper analytic closed subsets covering it would pull back to two analytic subsets covering \(\Lambda_i\), and one would have to contain the whole component. Thus \(N_i\) is pure of that dimension. These uses of dimension are explicit; density alone would not prove (16) equals the image dimension.

## A finite cover by closed analytic base conormals

**Theorem.** If \(\Lambda\subset T^*X\) is closed complex analytic, complex-conic and isotropic, there are at most \(n+1\) closed complex analytic subsets \(X_d\subset\pi(\Lambda)\), indexed by \(0\le d\le n\), such that

\[
\Lambda\subset\bigcup_{d=0}^n\Sigma_{X_d}.
\tag{17}
\]

Empty bases can be omitted. The bases need not be smooth, connected, or strata of a partition.

**Proof.** Group the components above by \(d_i\), and set

\[
\Lambda^{(d)}=\bigcup_{d_i=d}\Lambda_i,
\qquad X_d=\bigcup_{d_i=d}N_i.
\tag{18}
\]

Local finiteness makes both unions closed analytic; nonempty \(X_d\) is pure of dimension \(d\). The cone \(\Lambda^{(d)}\) is isotropic as a subset of \(\Lambda\).

On each \(\Lambda_i\), maximum-rank regular points are open dense. After deleting component intersections, these are also regular points of \(\Lambda^{(d)}\). Points over \((X_d)_{\mathrm{reg}}\) are dense among them. Indeed, otherwise a rank-\(d\) neighborhood would have its local \(d\)-dimensional complex image inside the singular part of \(X_d\), whose dimension is smaller than \(d\). The constant-rank theorem and dimension monotonicity contradict that possibility.

At such a good point \(p=(x,\xi)\), the projection differential maps onto \(T_x(X_d)_{\mathrm{reg}}\). Given \(u\) in that base tangent space, choose \(v\in T_p\Lambda^{(d)}\) projecting to it. Then

\[
\xi(u)=\alpha_p(v)=0.
\tag{19}
\]

Thus the dense good subset lies in the ordinary conormal of \((X_d)_{\mathrm{reg}}\). Its closure contains all of \(\Lambda^{(d)}\), and (10) gives \(\Lambda^{(d)}\subset\Sigma_{X_d}\). Taking the finite union proves (17). \(\square\)

In particular, conic analyticity alone is insufficient: if \(\Lambda=T^*\mathbb C\), its projection rank is 1 and its covectors need not annihilate the tangent of the one-dimensional base. The failed equality in (19) identifies precisely where isotropy is needed.

## Analytic closures of the critical rank loci

The generic-base theorem requires analytic exceptional sets, so the real subanalytic Sard argument alone is not enough. Here is the additional rank-closure argument.

Let \(B\) be pure-dimensional closed complex analytic in a complex manifold \(M\), and let \(H\subset B\) be closed analytic and contain its singular locus. Assume \(R=B\setminus H\) is dense in \(B\). Let \(g:M\to N\) be holomorphic. For an integer \(e\), put

\[
Q=\{b\in R:\operatorname{rank}_{\mathbb C}(dg_b|_{T_bB})<e\}.
\tag{20}
\]

Then \(\overline Q^{\,M}\) is complex analytic. To prove it, build the analytic tangent graph \(\Gamma_B\) just as in (11)–(12), now with planes in \(TM\). Its projection \(r:\Gamma_B\to B\) is proper. The rank condition \(\operatorname{rank}(dg|_L)<e\) is a holomorphic minor condition on the tautological plane bundle, so defines a closed analytic subset \(Z\subset\Gamma_B\). Over \(R\), the graph is unique and \(Z\) is exactly the tangent graph of \(Q\). Delete \(r^{-1}H\) from \(Z\), and retain its component closure \(Z'\). It is analytic. Properness gives

\[
r(Z')=\overline Q^{\,M}.
\tag{21}
\]

For one inclusion, lift every point of \(Z'\) by its approximating graph points. For the other, a convergent sequence in \(Q\) has a subsequence of tangent planes in the compact Grassmannian fibre. Its lifted limit lies in \(Z'\). The proper holomorphic image theorem makes (21) analytic. Working on coordinate charts suffices; the resulting closures agree intrinsically on overlaps.

Deleting \(r^{-1}H\) before closure is essential: extra planes over a singular point can satisfy the rank condition even if they are not accessible from critical regular points.

## Generic conormality along an arbitrary analytic piece

**Theorem.** Under the hypotheses of the cover theorem, let \(Y\subset X\) be any complex analytic piece: its closure and frontier are analytic. There is a complex analytic piece \(Y_0\subset Y\), open dense in \(Y\), which is a complex submanifold, allowing different dimensions on different components, and satisfies

\[
\Lambda\cap\pi^{-1}Y_0\subset T^*_{Y_0}X.
\tag{22}
\]

**Proof.** Decompose the regular locus of \(Y\) into its finitely many dimension parts \(Y^{(e)}\). Each is a smooth analytic piece, open in \(Y\). To see the analytic-piece assertion explicitly, group the irreducible components of \(\overline Y\) by dimension and remove their singular loci, their intersections with other components, and the original frontier. These are analytic deletions, and the regular dimension parts are exactly the remaining smooth pieces. Their union is dense in \(Y\).

For each \(e\), set \(A_e=\Lambda\cap\pi^{-1}Y^{(e)}\). This is an analytic piece and a complex-conic isotropic set. Its closure is analytic by the component-deletion rule. Group the irreducible components of that closure by dimension \(a\), and delete singularities, component intersections and the frontier of \(A_e\). We get finitely many smooth analytic pieces \(R_{e,a}\), each dense in its own pure-dimensional closure \(B_{e,a}\); their union is dense in \(A_e\). All are complex-conic, because fibre dilation preserves the original sets and all these regularity and component conditions.

The critical locus

\[
Q_{e,a}=\{p\in R_{e,a}:\operatorname{rank}_{\mathbb C}
(d\pi_p|_{T_pR_{e,a}})<e\}
\tag{23}
\]

is conic. The rank-closure argument proves that its ambient closure \(\overline Q_{e,a}\) is closed analytic. Conicity persists on that closure, so the zero-section argument (15) shows that

\[
D_{e,a}=\pi(\overline Q_{e,a})
=\overline{\pi(Q_{e,a})}^{\,X}
\tag{24}
\]

is closed analytic. Here the closure equality merits a check. If bases of points of \(Q_{e,a}\) approach \(x\) while their covectors are unbounded, multiply each covector by a sufficiently small nonzero complex scalar so that it approaches zero. The points stay in \(Q_{e,a}\), and their limits show \((x,0)\in\overline Q_{e,a}\). The reverse inclusion follows by continuity of projection. Thus fibre escape cannot enlarge or spoil the exceptional image in (24).

Sard's theorem makes \(\pi(Q_{e,a})\) measure zero in the real \(2e\)-manifold \(Y^{(e)}\). This image is subanalytic by the conic projection theorem. Its relative closure has empty interior, by subanalytic dimension drop. Hence \(D_{e,a}\cap Y^{(e)}\) is nowhere dense there; intersecting an ambient closure with this open regular part gives the same relative closure. Define

\[
Y_0=\bigcup_e\left(Y^{(e)}\setminus\bigcup_aD_{e,a}\right).
\tag{25}
\]

Only finitely many dimensions occur. Formula (25) is an analytic piece, open dense in \(Y\), and a smooth complex manifold on each component. To check its analytic frontier, put \(B_e=\overline{Y^{(e)}}\). Its complement in \(\overline Y\) is the union of the original frontier, the singular locus of \(\overline Y\), and the closed analytic sets \(B_e\cap D_{e,a}\). An intersection with \(B_e\) outside \(Y^{(e)}\) already lies in the original frontier or singular locus, so this union removes precisely the intended points. Density gives \(\overline{Y_0}=\overline Y\), proving the frontier assertion. For \(e=0\), the rank inequality in (23) is impossible, so no critical set is removed and the conormal condition is automatic.

At a point of \(R_{e,a}\) over \(Y_0\), the projection has complex rank \(e\), so maps onto the base tangent space. Isotropy and the calculation (19) put its covector in the conormal \(T^*_{Y_0}X\). For an arbitrary point of \(A_e\) over \(Y_0\), approximate it by the dense union of the \(R_{e,a}\). Openness of \(Y_0\) inside the relevant base piece keeps the approximating bases there eventually. The ordinary conormal of that smooth local base is closed over its base, so the same annihilation holds in the limit. This proves (22), including singular points of \(\Lambda\) and zero covectors. \(\square\)

This argument allows \(\Lambda\) to have no covectors over a generic part of \(Y\). Surjectivity onto \(Y\) was never assumed. Analytic bad-set removal here will be needed for complex microlocal stratifications; a conormal cover by itself does not yet supply a compatible stratification or its frontier condition.

## Exercises with complete solutions

### Reduced equations and large coefficients

*Difficulty: Introductory.*

Compare formula (14) for \(S=\{0\}\subset\mathbb C\) using \(z\) and \(z^2\). For the cusp \(S=\{y^2=x^3\}\subset\mathbb C^2\), explain why restricting the coefficient of \(d(y^2-x^3)\) to a bounded set loses nonzero conormal limits at the origin.

**Solution.** The reduced generator \(z\) gives every covector \(\lambda dz\) at zero. The equation \(z^2\) gives only zero there and therefore fails despite having the same zero set. On the cusp, write \((x,y)=(t^2,t^3)\). Then

\[
d(y^2-x^3)=(-3t^4,2t^3),\qquad
\lambda=\frac{b}{2t^3}
\quad\Longrightarrow\quad
\lambda d(y^2-x^3)=\left(-\frac32tb,b\right).
\tag{26}
\]

For fixed nonzero \(b\), this tends to \((0,b)\), using unbounded coefficients. Bounded coefficients instead make both entries tend to zero. Formula (14) permits all finite coefficients at each nonzero \(t\), followed by closure; it imposes no uniform coefficient bound along a sequence.

### Crossing branches retain two lines

*Difficulty: Introductory.*

For \(S=\{xy=0\}\subset\mathbb C^2\), compute \((\Sigma_S)_0\) in covector coordinates \(a\,dx+b\,dy\). Compare it with the conormal to the point and with the tangent graph over zero.

**Solution.** The punctured horizontal branch has tangent \(\mathbb C\partial_x\) and conormal \(a=0\); the punctured vertical branch gives \(b=0\). Thus

\[
(\Sigma_S)_0=\{a=0\}\cup\{b=0\}.
\tag{27}
\]

Both lines are attained by constant covectors on their respective branches. The tangent graph at zero consists of exactly the two coordinate tangent lines, not all lines in \(\mathbb C^2\). Their annihilators give (27). The point conormal is the full fibre \(\mathbb C^2\), strictly larger: for example \((1,1)\) belongs to it but not to (27).

### The cusp's graph and singular fibre

*Difficulty: Intermediate.*

Give the limiting tangent plane and the entire origin conormal fibre for the complex cusp. Verify that each nonzero covector in that fibre is accessible from ordinary conormals.

**Solution.** At \(t\ne0\), its tangent line is spanned by \((2t,3t^2)\), or equivalently \((1,3t/2)\). Its unique limiting line is \(\mathbb C(1,0)\). The annihilator equation is \(2a+3tb=0\). A finite covector limit has bounded \(b\), hence \(a\to0\); every \((0,b_0)\) is obtained by taking \(b=b_0\), \(a=-3tb_0/2\). Therefore the origin fibre is exactly \(\{a=0\}\). It is a full complex line, and the tangent graph supplies that line even though the defining equation has zero differential at the origin.

### The real Hamiltonian sign at a smooth cone

*Difficulty: Intermediate.*

In \(T^*\mathbb C\), take the zero section. Write a real covector annihilating its point cone using \(z=x+iy\) and \(\xi=a+ib\). Compute \(-H\theta\) and check the singular involutivity convention directly.

**Solution.** The real symplectic form is \(da\wedge dx-db\wedge dy\). The point cone at any zero-section point is the real plane spanned by \(\partial_x,\partial_y\), and its two-set cone is the same plane. An annihilating real covector is \(\theta=A\,da+B\,db\). The convention \(\iota_{H\theta}\omega=-\theta\) gives \(H\theta=A\partial_x-B\partial_y\). Consequently \(-H\theta=-A\partial_x+B\partial_y\) belongs to that same point cone. The sign on the imaginary covector coordinate follows from the minus sign in \(\omega\); replacing it by a plus sign would give the wrong identification.

### A singular Lagrangian which is not fibre-conic

*Difficulty: Advanced.*

In \(T^*\mathbb C\), let \(L=\{\xi^2=z^3\}\), parametrized by \((z,\xi)=(t^2,t^3)\). Compute its point cone at the origin, show that its two-set cone there is all of \(\mathbb C^2\), and explain why the coisotropy theorem applies although \(\alpha\) is nonzero on its regular curve.

**Solution.** The point cone is \(\mathbb C\partial_z\). If \(t^2/h\) has a finite limit with \(h>0\), then \(t^3/h=t(t^2/h)\to0\); every complex first coordinate is obtainable by choosing a square root of a prescribed multiple of \(h\). For the pair cone, choose first parameter \(t\) and second parameter \(u=-t+ct^2\). Their differences are

\[
t^2-u^2=2ct^3+O(t^4),\qquad
t^3-u^3=2t^3+O(t^4).
\tag{28}
\]

Given a target \((A,B)\) with \(B\ne0\), choose \(c=A/B\), choose a fixed argument of \(t\) making \(t^3/|t|^3=B/|B|\), and take \(h=2|t|^3/|B|\). The quotients tend to \((A,B)\). Targets with \(B=0\) are already in the point cone and therefore in the two-set cone. Thus the pair cone is the whole space, and the premise of (3) at the origin forces \(\theta=0\), giving the conclusion directly.

Every regular tangent is a complex line in a complex symplectic surface, so is Lagrangian. The analytic coisotropy theorem gives real involutivity at all points. Meanwhile \(\alpha=\xi dz\) pulls back to \(2t^4dt\), which is nonzero away from zero. There is no contradiction: fibre conicity was needed to infer canonical-form vanishing from symplectic isotropy, and this curve is not fibre-conic.

### One finite base with infinitely many components

*Difficulty: Introductory.*

Let \(Z=\{m:m\in\mathbb Z\}\subset\mathbb C\) and \(\Lambda=\bigcup_{m\in\mathbb Z}T_m^*\mathbb C\). Exhibit the rank-group cover and check local finiteness.

**Solution.** The integers are the zero set of the entire function \(\sin(\pi z)\); they have no finite accumulation. Every compact base region meets finitely many of them, so the full vertical fibres form a closed locally finite analytic union. Each fibre is complex-conic and Lagrangian. Its projection rank is zero, so (18) gives \(X_0=Z\), with \(X_1\) empty. The single conormal \(\Sigma_Z\) equals \(\Lambda\). The cover is finite even though this one base has infinitely many connected components. Local finiteness is checked on compact coordinate neighborhoods, not by requiring the entire manifold to meet finitely many components.

### Generic bases for a zero section and a fibre

*Difficulty: Intermediate.*

Take \(\Lambda=\{\xi=0\}\cup\{z=0\}\subset T^*\mathbb C\). Give the cover (17). For \(Y=\mathbb C\) and for \(Y=\{0\}\), find a valid \(Y_0\) and verify (22). Explain what happens if \(\Lambda\) is replaced by all of \(T^*\mathbb C\).

**Solution.** The zero section has projection rank 1 and base \(X_1=\mathbb C\); the vertical fibre has rank zero and base \(X_0=\{0\}\). Their base conormals give exactly the stated union. For \(Y=\mathbb C\), take \(Y_0=\mathbb C\setminus\{0\}\). Over it, only the zero covector occurs, which annihilates its tangent. Including the origin would fail, since its nonzero vertical covectors do not annihilate the tangent of \(\mathbb C\). For the zero-dimensional base \(Y=\{0\}\), take all of it: its tangent is zero, and its conormal is the full fibre.

If \(\Lambda=T^*\mathbb C\), every nonempty open smooth base has arbitrary nonzero covectors above it. Its tangent is one-dimensional, so (22) fails on every possible open dense \(Y_0\subset\mathbb C\). Nor can finitely many closed analytic base conormals cover it. A closed analytic subset of the connected curve \(\mathbb C\) is either all of \(\mathbb C\), with zero-section conormal, or discrete, with full conormal fibres only over that discrete set. Finitely many discrete bases still leave some base point outside them, where only zero covectors have been covered. The full cotangent bundle is analytic and complex-conic but fails isotropy. It verifies the need for the hypothesis in both valid theorems.

### Why projected components need conicity

*Difficulty: Advanced.*

Consider the discrete analytic set \(A=\{(1/m,m):m\ge1\}\subset T^*\mathbb C\). Show that it is closed analytic and that its projected component family is not locally finite near zero. Identify the failure of the zero-section argument.

**Solution.** Its fibre coordinates tend to infinity, so every compact subset of \(T^*\mathbb C\) contains only finitely many of these points. The set is closed and locally a finite union of isolated analytic points, hence complex analytic. Each point is an irreducible component. Their projected bases are \(\{1/m\}\), which accumulate at zero, so are not locally finite there; their union is not closed in \(\mathbb C\). The set is not fibre-conic: scaling \((1/m,m)\) does not stay in its singleton component. In particular \((1/m,0)\) does not belong to it. Equation (15) therefore fails, and no neighborhood of \((0,0)\) detects those escaping components. Zero-dimensional regular tangent spaces have vanishing canonical form, so this example also shows that isotropy without conicity does not supply the projected local-finiteness argument.

## What remains a prerequisite

The normal-cone, ideal, flow, tangent-graph, finite-cover and generic-base arguments above are complete relative to the specified analytic image/dimension, Casimir specialization and subanalytic geometry contracts. We have not proved the underlying Thom stratification theorem or all analytic proper-image and dimension theory here. A complex microlocal stratification refining an analytic covering, the sheaf constructibility equivalences, and the nonproper curve-base direct-image theorem still require their own arguments. The defining-equation and missing-isotropy counterexamples retain the precise limits of the constructions; full transitive proof closure is not claimed.

## Sources and the conormal construction

**Reduced ideals and specialization.** Masaki Kashiwara and Teresa Monteiro Fernandes, [*Involutivité des variétés microcaractéristiques*, Bulletin de la Société Mathématique de France 114 (1986), 393–402](https://www.numdam.org/item/10.24033/bsmf.2062.pdf), Definition 1.1.9 and Lemma 1.1.11, printed p. 396, describe analytic involutivity by bracket closure of the defining ideal. Theorem 1.1.12, p. 397, assumes that the Hamiltonian field of the chosen holomorphic function is tangent to the original involutive analytic set; intersecting that set with the function's zero fibre then preserves involutivity. Corollary 1.1.14 applies when the Hamiltonian field vanishes identically. The proof uses Lemma 1.1.13 on limiting tangent spaces, a consequence of Thom stratification. This Casimir case is the exact input used for the central fibre of (5). The lesson then supplies the constant-Hamiltonian ideal equation and the flow argument at the cone vertex to obtain the real normal-cone condition (3). The analytic specialization theorem alone is not a definition of that real condition.

**Analytic images, dimensions and ideals.** Ya’acov Peterzil and Sergei Starchenko, [*Complex analytic geometry and analytic-geometric categories*, author manuscript](https://math.haifa.ac.il/kobi/analytic.pdf), Theorem 6.1 and Claim 1 of its proof, manuscript pp. 16–17, give analyticity of a closed holomorphic image in the analytic-geometric category and its dimension from maximal generic complex rank. Their proof uses countable local charts, regular irreducible components and the preceding removal results. Properness supplies closedness and subanalyticity in the applications here; neither arbitrary projection nor rank at a single exceptional point suffices. Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter II, Theorem 4.29 and Theorem 4.31, pp. 99–101, supplies coherence of the reduced ideal and analyticity of the singular locus; Corollary 5.4, p. 103, gives the component-deletion rule. Theorem 8.8, pp. 118–120, is the proper mapping theorem used for compact Grassmann incidence.

**What the lesson constructs.** The conormal is built from the closure of the tangent graph and its annihilator incidence, retaining compactness of the Grassmann factor. The reduced-generator test is essential: the solved zero-set example shows exactly why equations with vanishing differentials can give the wrong conormal. The finite covering argument groups the analytic bases by generic projection dimension and explicitly keeps isotropy. The final rank-drop construction deletes the analytic frontier before closing the critical locus and projects only after checking its analytic, conic and dimension properties.

**Teaching route and remaining foundations.** The sequence runs from singular involutivity to the tangent graph, the finite family and generic base directions, with eight complete solutions testing hypotheses and calculations. It does not purport to reprove the analytic local algebra, Thom stratification, proper-image theorem or subanalytic dimension theory. Those exact dependencies remain separate proof obligations. The source credit above identifies the mathematical mechanisms used, while the normal-cone flow, incidence and projection arguments are given explicitly here.
