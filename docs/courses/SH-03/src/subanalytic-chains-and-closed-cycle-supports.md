# Subanalytic chains and closed cycle supports

A subanalytic chain records an orientation and a coefficient on each smooth piece of a given dimension. Its support includes limiting points of those pieces. A cycle satisfies an additional compatibility condition at those limiting points. The dualizing object expresses that condition even at a branch or a singularity, where an orientation line on a manifold would be insufficient.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

We use the subanalytic filtrations and local finiteness established in the preceding constructibility lessons, and the locally closed support, exceptional-composition and manifold-orientation lessons of SH-02. The dualizing complex from oriented simplices fixes the incidence signs used in the examples. Subanalytic chains were introduced for this purpose by M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §1. Proper images, products, the local contraction proving the full chain resolution, coefficient flatness and intersections are treated in the following lessons.

## Orientations give a sheaf of chains

Let \(A\) be a commutative ring of finite global dimension. Let \(X\) be a real analytic manifold, Hausdorff and countable at infinity, of dimension \(n\); for several components use a uniform finite dimension bound and work component by component. Neither characteristic zero nor a field nor a global orientation is assumed. All tensor products in the initial chain definitions are ordinary sheaf tensor products over \(A_X\).

For \(p\geq0\), form an \(A\)-module from oriented subanalytic \(p\)-dimensional submanifolds \(S\subset X\), with three rules:

\[
 [S_1\amalg S_2]=[S_1]+[S_2],\qquad
 [S]=[V]\quad(V\subset S\text{ open and dense}),\qquad
 [S^{\mathrm{op}}]=-[S].
 \qquad\text{(1)}
\]

The orientations on the first two expressions are inherited from the indicated pieces. The dense subset is subanalytic. The disjoint union rule concerns unions that are again submanifolds of the indicated dimension; a compatible finite decomposition and dense deletion handle the general local subdivision. A lower-dimensional piece does not become a \(p\)-chain. Set the module to zero for \(p<0\).

Restriction to open sets gives a presheaf. Denote its sheafification by \(\mathcal C_p\). For an arbitrary sheaf \(F\) of \(A\)-modules put

\[
 \mathcal C_p(F)=\mathcal C_p\otimes_A F.
 \qquad\text{(2)}
\]

Sheafification is essential: a global section may require an unbounded number of different coefficients on a locally finite family, although each germ has a finite description. Exercise 5 constructs one.

For a \(p\)-manifold \(S\), let \(\operatorname{or}_S\) be its integral orientation sign line tensored with \(A\). An integral orientation chooses a generator of that line. Reversal multiplies it by \(-1\), including when these become the same scalar in characteristic two. The manifold-duality normalization is

\[
 \omega_S\simeq\operatorname{or}_S[p],
 \qquad H^{-p}(\omega_S)=\operatorname{or}_S.
 \qquad\text{(3)}
\]

Thus a degree-\(p\) geometric piece will occupy **cohomological degree \(-p\)** in the chain complex.

## The lowest dualizing degree on a singular support

For any locally closed subanalytic subset \(S\) let \(j_S:S\to X\) be its inclusion. Its dualizing object is defined by exceptional composition, \(\omega_S=j_S^!\omega_X\). If \(\dim S\leq p\), then

\[
 H^q(S;F)=H_c^q(S;F)=0\quad(q>p),\qquad
 H^q(\omega_S)=0\quad(q<-p).
 \qquad\text{(4)}
\]

Here the first assertion holds for every sheaf \(F\) on \(S\), with no coefficient finiteness condition.

**Proof of the dimension bound.** Choose a finite closed dimension filtration of \(S\) whose layer in dimension \(r\) is a disjoint union of \(r\)-manifolds. A locally finite stratification supplies such a filtration even if there are infinitely many strata globally. The manifold cohomological-dimension theorem supplies a c-soft resolution of length \(r\) for every sheaf on that layer.

Open extension by zero preserves c-softness in this situation. To see the relevant extension property, a section of \(j_!E\) on a compact subset has its nonzero germ support in a compact subset of the open stratum, away from its complement. Choose a compact neighborhood of that support inside the stratum. Prescribe the original values on its intersection with the given compact set, and zero on an outer compact boundary, where those prescriptions agree. C-soft extension then gives a section; it vanishes on a collar of that boundary, so its restriction extends by zero with compact support. Its extension by zero has all the desired values on the ambient compact set. This also applies to a disjoint union: a compactly supported section meets only finitely many members of a locally finite family.

Consequently the open-stratum term in
\(0\to j_!F|_U\to F\to i_*F|_{S\setminus U}\to0\)
has ordinary and compact-support cohomology zero above \(r\). For ordinary sections we use c-soft acyclicity on a countable-at-infinity locally compact space; for compact sections we use compact-support acyclicity. The closed term has the bound of the next filtration stage. Induction and the two long exact sequences give the first part of (4). This proof does not commute arbitrary ordinary global sections with a filtered colimit.

Exceptional adjunction gives, on every relatively open neighborhood \(V\subset S\),

\[
 R\Gamma(V;\omega_S|_V)
 \simeq R\operatorname{Hom}_A(R\Gamma_c(V;A),A).
 \qquad\text{(5)}
\]

The complex inside the dual has no cohomology above \(p\). Derived Hom into a module in degree zero therefore has no cohomology below \(-p\). Taking stalks proves the second part of (4). The same bound also gives

\[
 H^{-p}(S;\omega_S)
 \simeq\Gamma(S;H^{-p}\omega_S)
 \simeq\operatorname{Hom}_A(H_c^p(S;A),A).
 \qquad\text{(6)}
\]

Indeed separate \(H_c^p(S;A)[-p]\) from the lower truncation in (5). The dual of the lower truncation begins in degree \(1-p\); only the ordinary Hom of the top group contributes in degree \(-p\). Likewise the sheaf-to-global spectral sequence has only its \(H^0(S;H^{-p}\omega_S)\) term in that degree. No assertion that all higher Ext groups vanish is needed. \(\square\)

Write
\[
 T_S=j_{S*}H^{-p}(\omega_S).
 \qquad\text{(7)}
\]

The ordinary direct image in this formula retains boundary germs. It is not open extension by zero. For a locally closed subset \(V\subset S\), support adjunction and the lower bound give

\[
 j_{V*}H^{-p}(\omega_V)
 \simeq H^0_V(T_S).
 \qquad\text{(8)}
\]

For locally closed \(V\), \(H^0_V\) means degree zero of the **sheaf** operation \(R\mathcal Hom(A_V,-)\), with \(A_V\) extended by zero. In particular an open \(V\) gives ordinary direct image after restriction. For closed \(V\) it is the usual subsheaf of sections supported there.

To prove (8), use \(Rj_{V*}\omega_V=R\Gamma_V(Rj_{S*}\omega_S)\). Both derived support and derived ordinary image have nonnegative cohomological degree on sheaves. Since all dualizing cohomology begins at \(-p\), their degree-\(-p\) term is exactly the degree-zero support of the lowest sheaf. This identifies the actual maps as well as their objects.

Two consequences control the singular points. If \(V\) is closed in \(S\) and \(\dim(S\setminus V)<p\), the closed-support trace induces an isomorphism

\[
 j_{V*}H^{-p}\omega_V \xrightarrow{\sim} T_S.
 \qquad\text{(9)}
\]

Use the localization triangle and (4) on the lower-dimensional open complement; its ordinary derived image starts in degree \(1-p\). If \(U\) is open and dense in the \(p\)-dimensional regular part of a **closed** \(S\), let \(B=S\setminus U\). Then

\[
 0\longrightarrow T_S
 \longrightarrow j_{U*}\operatorname{or}_U
 \longrightarrow j_{B*}H^{1-p}\omega_B
 \qquad\text{(10)}
\]

is exact. This time use the closed-support triangle for \(B\); \(\dim B<p\) kills its degree-\(-p\) term. The displayed sequence makes no claim of surjectivity on the right. The last arrow measures failure of the orientations and coefficients on the regular pieces to fit at the singular set.

## Directed comparison of locally closed representatives

Let \(\mathscr L_p\) be the family of locally closed subanalytic subsets of dimension at most \(p\). Use a comparison \(S_1\preceq S_2\) when there is a subanalytic \(V\subset S_1\cap S_2\) such that

\[
 V\text{ is open in }S_1,\quad
 V\text{ is closed in }S_2,\quad
 \dim(S_1\setminus V)<p.
 \qquad\text{(11)}
\]

This is a directed preorder; one may quotient mutually comparable objects to obtain an ordered index. Distinct subsets differing by a detached lower-dimensional piece can be mutually comparable. Nothing below uses literal antisymmetry of subsets.

The comparison gives

\[
 T_{S_1}\longrightarrow T_{S_2}
 \qquad\text{(12)}
\]

by restricting to \(V\), then using the closed-support trace from \(V\) to \(S_2\). These maps are independent of the witness. If \(V'\) is another witness, \(V\cap V'\) is open and closed in \(V\), with lower-dimensional complement. Equation (9) makes passage to that intersection an isomorphism. Both maps then factor through the same trace and restriction. The same argument proves compatibility under composition: intersect witnesses for two consecutive comparisons.

Here is a common upper representative for \(S_1,S_2\):
\[
 R=(S_1\setminus\partial S_2)\cup(S_2\setminus\partial S_1),
 \qquad \partial S=\overline S\setminus S.
 \qquad\text{(13)}
\]

The frontier of a locally closed subanalytic set is closed and has smaller dimension. Indeed
\(R=(\overline S_1\cup\overline S_2)\setminus(\partial S_1\cup\partial S_2)\),
which is locally closed. The witness
\(V_i=S_i\setminus\partial S_j\)
is open in \(S_i\) and closed in \(R\): a point of \(R\) in \(\overline{V_i}\setminus V_i\) would lie in the frontier of \(S_i\), removed from the other piece, or in the frontier of \(S_j\), removed from the first. Its complement in \(S_i\) has dimension less than \(p\). Hence \(S_i\preceq R\).

These comparisons yield a concrete description of chains:

\[
 \mathcal C_p\simeq\underset{S\in\mathscr L_p}{\operatorname{colim}}T_S.
 \qquad\text{(14)}
\]

**Proof.** The top regular part of \(S\) is a comparison successor in (11); there (3) gives its orientation line. Thus it suffices to compare the chain presentation with orientation sections on smooth top-dimensional pieces. Work in a relatively compact subanalytic neighborhood. A finite compatible triangulation subdivides the relevant pieces into oriented open \(p\)-cells; after deletion of lower-dimensional faces these form a dense subset. A section of an orientation line has a locally constant coefficient on each such cell. This produces the map from (1) to (14).

Conversely those cell coefficients are represented by a finite sum of oriented symbols on a sufficiently small neighborhood. Two representations can be compared on a common finite subdivision. Their difference is zero precisely when every open \(p\)-cell coefficient is zero; lower-dimensional leftovers are deleted by (1). Orientation reversal gives exactly the opposite coefficient. This proves surjectivity and injectivity on germs. Compatible restriction then proves the sheaf isomorphism. Nonorientable pieces cause no obstruction to this argument: the cells trivialize their sign lines, and their transition signs are retained when the pieces are compared. \(\square\)

## Closed supports define cycles

Let \(\mathscr K_p\) consist of **closed** subanalytic subsets of dimension at most \(p\), ordered by inclusion. Their unions provide common upper bounds. For \(S\subset S'\), (8) identifies \(T_S\) with the subsheaf of \(T_{S'}\) supported on \(S\). In particular the transition is injective. Define

\[
 \mathcal Z_p=\underset{S\in\mathscr K_p}{\operatorname{colim}}T_S.
 \qquad\text{(15)}
\]

There is an injection \(\mathcal Z_p\hookrightarrow\mathcal C_p\). To check it, represent a germ on a closed \(S\). If a later chain comparison killed it, restriction to the common dense top-dimensional regular pieces would be zero. The injection in (10), followed by a compatible subdivision, then makes the original germ zero. Thus a coefficient compatible on a closed support is not lost in the larger locally closed colimit.

An open interval's chain illustrates the distinction. Its orientation contributes through ordinary direct image from the interval, with nonzero germs at both endpoints. The lowest dualizing sheaf of the **closed** interval has zero endpoint stalks, as the earlier cellular calculation proves. A global nonzero oriented interval therefore does not furnish a cycle on that closed interval.

For an arbitrary sheaf \(F\) define \(\mathcal Z_p(F)=\mathcal Z_p\otimes_A F\). At this stage we have proved the injection and the kernel statement below for the untensored sheaves. Exactness after arbitrary tensoring needs the flatness argument supplied by the full local chain resolution.

## The boundary comes from the frontier triangle

Take \(S\in\mathscr L_p\), and put \(B=\overline S\setminus S\). The localization triangle on \(\overline S\) is

\[
 \omega_B\longrightarrow\omega_{\overline S}
 \longrightarrow Rj_*\omega_S\longrightarrow\omega_B[1],
 \qquad\text{(16)}
\]

where the first and last objects are pushed forward from the closed frontier as necessary. Since \(\dim B<p\), its cohomology gives

\[
 0\longrightarrow T_{\overline S}
 \longrightarrow T_S
 \xrightarrow{\ b_S\ }T_B^{\,p-1}.
 \qquad\text{(17)}
\]

The superscript reminds us to take \(H^{-(p-1)}(\omega_B)\) in the last term. Map that term into \(\mathcal Z_{p-1}\). Localization and trace naturality make these arrows compatible with (12), so (14) yields

\[
 b_p:\mathcal C_p\longrightarrow\mathcal Z_{p-1},
 \qquad
 \partial_p:\mathcal C_p\xrightarrow{b_p}\mathcal Z_{p-1}
                     \hookrightarrow\mathcal C_{p-1}.
 \qquad\text{(18)}
\]

Equations (15) and (17) prove
\[
 \ker\partial_p=\mathcal Z_p,\qquad
 \partial_{p-1}\partial_p=0.
 \qquad\text{(19)}
\]

For the kernel assertion, a germ killed by \(b_p\) can be represented by \(T_S\). Its boundary in \(T_B^{p-1}\) cannot become zero merely by enlarging a closed support, because those transitions are injective. Exactness of (17) therefore lifts the germ to \(T_{\overline S}\), which is a cycle representative. Conversely a closed cycle has empty frontier and zero boundary. The image of the first boundary is already in \(\mathcal Z_{p-1}\), so the second boundary vanishes. This proof does not assert that \(b_p\) is onto.

Define a cohomological sheaf complex by
\[
 \mathcal C^{-p}=\mathcal C_p,\quad d^{-p}=\partial_p.
 \qquad\text{(20)}
\]

It is bounded in degrees \([-n,0]\). Since \(X\) itself is terminal among closed supports of dimension at most \(n\), \(\mathcal Z_n=H^{-n}\omega_X=\operatorname{or}_X\). Its inclusion as the degree-\(-n\) kernel defines a morphism
\[
 \omega_X=\operatorname{or}_X[n]\longrightarrow\mathcal C.
 \qquad\text{(21)}
\]

It is canonical with the orientation and trace conventions fixed above. Proving that (21) is an isomorphism requires killing the lower-degree local cycle classes. We have not inferred that conclusion just from (19).

All these constructions commute with restriction to an open subset. Indeed the support representatives and traces restrict, every local representative can be chosen in a relatively compact subanalytic neighborhood of the point under examination, and sheafification is determined by those germs. Hence both \(\mathcal C_p^X|_U=\mathcal C_p^U\) and \(\mathcal Z_p^X|_U=\mathcal Z_p^U\).

## Cutting chains proves softness

Let \(W\subset X\) be subanalytic and open. Restriction from a representative \(S\) to \(S\cap W\), followed by its ordinary image to \(X\), defines an endomorphism \(P_W\) of \(\mathcal C_p\). It is compatible with (12) and (14). It satisfies

\[
 P_W^2=P_W,\qquad P_W|_W=\mathrm{id},\qquad
 P_W|_{X\setminus\overline W}=0.
 \qquad\text{(22)}
\]

The closure in the last expression is necessary: a cut interval has new endpoint germs on \(\partial W\). Also \(P_W\) need not commute with the boundary; cutting can create a boundary.

For every sheaf \(F\), \(\mathcal C_p(F)\) is soft. Here softness means extension of a section from every closed subset, with no constructibility, local freeness or coefficient flatness assumption on \(F\).

**Proof.** A section on a closed \(Z\) extends to some open neighborhood \(U\) of \(Z\). The neighborhood representation uses the standard closed-neighborhood gluing property for sheaves on a paracompact Hausdorff space: local representatives can be shrunk in a locally finite cover so that their agreements give a single section near \(Z\). Choose a subanalytic open \(W\) with
\[
 Z\subset W\subset\overline W\subset U.
 \qquad\text{(23)}
\]
Such a \(W\) exists even for a nonsubanalytic \(Z\): a locally finite family of analytic coordinate balls, with compact closures in \(U\), can be chosen to cover \(Z\). Their union is subanalytic locally, and the union of their closures is closed and contained in \(U\).

Apply \(P_W\otimes\mathrm{id}_F\) to the neighborhood extension. By (22) its support is contained in \(\overline W\), so it extends by zero from \(U\) to \(X\), and it still equals the prescribed section near \(Z\). This is the required global extension. The argument uses an actual idempotent on chains, without assuming that tensor product preserves a prior exact sequence. \(\square\)

Softness supplies an acyclic chain model once (21) is proved to be an isomorphism. It does not make cycles soft, and it does not make chains flabby. The latter distinction is visible in Exercise 5.

## Exercises with complete solutions

### Deleting a point keeps a chain and cancels its interior boundary

*Difficulty: Introductory.*

Orient the real line to the right. Compare the chain on \((-2,3)\) with the sum of its pieces \((-2,0)\) and \((0,3)\). Determine the germ of \(\mathcal C_1\), its boundary and its cycle kernel at \(0\). Then cut the whole-line chain by \(W=(0,3)\).

**Solution.** Dense deletion gives
\([(-2,3)]=[(-2,0)]+[(0,3)]\).
Near \(0\), every one-dimensional subanalytic piece is, after dense deletion and subdivision, a left or right interval germ. Thus
\((\mathcal C_1)_0=A\oplus A\), with coordinates \(a_-\) and \(a_+\) using the positive line orientation. Also \((\mathcal C_0)_0=A\), generated by \([0]\). Terminal-minus-initial incidence gives
\[
 \partial(a_-,a_+)=a_- -a_+,\qquad
 (\mathcal Z_1)_0=\{(a,a):a\in A\}.
 \qquad\text{(24)}
\]
The original interval has germ \((1,1)\); the two pieces contribute \((1,0)\) and \((0,1)\). Their boundaries at zero are respectively \(+[0]\) and \(-[0]\), which cancel. The remaining global boundary is \([3]-[-2]\), so the interval is not a global cycle.

The whole-line cycle is sent by \(P_W\) to \([(0,3)]\), whose germ at zero is \((0,1)\) and whose boundary is \([3]-[0]\). In particular the cutoff has a nonzero germ at a point outside \(W\), but on \(\overline W\). It is idempotent and is not a chain map. These calculations remain valid over characteristic two: subtraction becomes addition and the kernel is still the diagonal.

### A singular vertex imposes a conservation law

*Difficulty: Intermediate.*

Let \(S\subset\mathbb R^2\) be three closed rays meeting only at their common endpoint \(v\), oriented away from \(v\). Over \(\mathbb Z\), find the compatibility condition for a chain with ray weights \((a,b,c)\) to be a cycle. Test \((2,-3,1)\) and \((2,3,1)\). Explain what changes in the lowest degree if an isolated point \(w\notin S\) is adjoined.

**Solution.** Each outward ray has initial endpoint \(v\), so its contribution there is the negative of its coefficient. There are no finite outer endpoints. Thus the boundary is
\[
 -(a+b+c)[v].
 \qquad\text{(25)}
\]
The lowest dualizing stalk at \(v\) is the kernel of
\(\mathbb Z^3\xrightarrow{-(1,1,1)}\mathbb Z\), hence is free of rank two. This is the cellular local-duality calculation, and also the kernel in (10): ordinary orientation sections on the three open rays have three independent germs, while the singular point records their sum. The first test has zero boundary and gives a global cycle on the closed rays. The second has boundary \(-6[v]\).

For \(S'=S\amalg\{w\}\), the closed inclusion \(S\subset S'\) has a zero-dimensional complement. Equation (9) with \(p=1\) identifies their \(H^{-1}\) sheaves after direct image; the isolated point contributes no one-cycle. It does contribute \(H^0(\omega_{S'})_w=\mathbb Z\). Removing lower-dimensional pieces preserves the lowest indexed degree, not the entire dualizing object.

### Ordinary boundary germs and closed cycle germs differ

*Difficulty: Intermediate.*

Let \(I=[0,1]\) and \(J=(0,1)\) in \(\mathbb R\), with \(p=1\). Compute \(T_I\) and \(T_J\), their global sections and the comparison \(T_I\to T_J\). Show separately that (11) is not an antisymmetric relation on literal subsets.

**Solution.** The closed interval's cellular complex has an edge in degree \(-1\), endpoint coefficients in degree zero, and the terminal-minus-initial differential. At an endpoint that differential is an isomorphism, while in the interior it is zero. Consequently
\[
 T_I=j_{J!}A_J,\qquad T_J=j_{J*}A_J=A_I
 \quad\text{as sheaves on }\mathbb R.
 \qquad\text{(26)}
\]
The first expression has zero endpoint stalks; the second has an \(A\) stalk at each endpoint. A section of \(j_{J!}A_J\) over \(\mathbb R\) would be constant on the connected \(J\) and vanish near both endpoints, hence is zero. Therefore \(\Gamma(\mathbb R;T_I)=0\), whereas \(\Gamma(\mathbb R;T_J)=A\). The comparison is the natural injection that is the identity on \(J\) and zero from each zero endpoint stalk. Its boundary sends \(a\) to \(a([1]-[0])\).

For the second assertion take \(S_1=J\) and \(S_2=J\amalg\{2\}\). The common witness \(J\) is open in each and closed in each as required in the two directions; the extra point has dimension zero, less than \(p\). Thus \(S_1\preceq S_2\) and \(S_2\preceq S_1\), although \(S_1\ne S_2\). Their \(T\) sheaves are isomorphic because the point has no degree-\(-1\) contribution. The directed system uses this comparison equivalence, rather than a false antisymmetry assertion.

### Arbitrary point coefficients survive the cutoff and the kernel

*Difficulty: Intermediate.*

On \(\mathbb R\), let \(F=i_*M\), where \(i:\{0\}\to\mathbb R\) and \(M\) is any \(A\)-module. Compute \(\mathcal C_1(F)\), \(\mathcal C_0(F)\), their boundary and its kernel. Calculate \(P_{(0,1)}\) on this coefficient sheaf. Does this calculation require \(M\) to be flat?

**Solution.** Tensor product is determined on stalks. The two sheaves are zero away from zero and have stalks \(M^2\) and \(M\) there. Equation (24) becomes
\[
 M^2\xrightarrow{(a,b)\mapsto a-b}M,\qquad
 \ker=\{(a,a):a\in M\}.
 \qquad\text{(27)}
\]
This sequence is split: \(m\mapsto(m,0)\) is a section of the boundary, and \((a,b)\mapsto(b,b)\) projects onto the kernel. It therefore survives tensoring with every module; no general flatness theorem has been used. Locally \(\mathcal Z_1=\operatorname{or}_{\mathbb R}=A\), so its tensor with \(F\) is exactly this diagonal copy of \(M\).

The cutoff acts by \((a,b)\mapsto(0,b)\). It is idempotent, has a potentially nonzero germ at zero, and takes the diagonal \((m,m)\) to a chain of boundary \(-m\). All these assertions hold, for example, with \(A=\mathbb Z\) and \(M=\mathbb Z/3\). The sheaves here are skyscrapers and are soft: a section on a closed set containing zero is determined by its \(M\)-coordinates, which extend globally; a closed set missing zero has only the zero section. This particular split calculation does not establish tensor exactness for all singular chain systems.

### Sheafification allows many weights, but not accumulating zero-dimensional support

*Difficulty: Advanced.*

Over \(\mathbb Z\), construct the zero-chain
\(\alpha=\sum_{r\geq1}r[r]\) on \(\mathbb R\). Show why it is a sheaf section but has no finite presentation by the presheaf generators in (1). On \(U=(0,1)\), consider instead the zero-chain with coefficient one at every \(1/r\), \(r\geq2\). Can it extend to \(\mathbb R\)? Reconcile the answer with softness.

**Solution.** The positive integers are a closed locally finite subanalytic zero-dimensional subset. On every relatively compact neighborhood only finitely many of them occur. Their finite weighted presentations agree on overlaps, hence glue to a section \(\alpha\) of \(\mathcal C_0\), or equivalently to a section of \(T_{\mathbb N}\).

A finite sum \(\sum_{\ell=1}^m a_\ell[S_\ell]\) has, at any point, a coefficient formed from the finite set of \(a_\ell\), with each term absent or present with one of its orientation signs. There are only finitely many such sums. The weights \(1,2,3,\ldots\) cannot be represented this way. Thus sheafification supplies more global sections than a single finite presheaf expression.

The reciprocal set is locally finite and closed **in \(U\)**, so its coefficient-one chain is a section there. If it extended across zero, some neighborhood of zero would have a finite local subanalytic zero-chain presentation. A zero-dimensional subanalytic subset has no infinite accumulation in a sufficiently small relatively compact neighborhood: a finite local stratification has only finitely many zero-dimensional strata. Such a presentation cannot contain every \(1/r\). The extension is impossible. Softness concerns sections on closed subsets of the ambient \(\mathbb R\), whereas the reciprocal support is not closed there; extension from every open subset would be flabbiness. This example distinguishes the two properties.

### Orientation cycles over the integers and in characteristic two

*Difficulty: Advanced.*

Take \(X=\mathbb RP^2\), \(p=n=2\). Compute \(\Gamma(X;\mathcal Z_2)\) over \(\mathbb Z\) and over \(\mathbb F_2\). Check the result using (6), and identify the lower dualizing cohomology over \(\mathbb Z\) that the top cycle calculation does not see.

**Solution.** Since \(X\) is a closed support, \(\mathcal Z_2=\operatorname{or}_X\). Transport around an orientation-reversing loop acts by \(-1\). An integral global coefficient must satisfy \(a=-a\), hence \(2a=0\). Over \(\mathbb Z\) this forces \(a=0\); over \(\mathbb F_2\) every coefficient satisfies it and the sign line is constant, giving a one-dimensional space of top cycles.

For an independent check, the usual one-cell-in-each-dimension decomposition has chain boundary \(2:A\to A\) in dimensions two to one and zero in dimensions one to zero. The attaching loop of the two-cell traverses the one-cell twice in the same induced direction, giving that integer \(2\). Its cochain complex is \(A\xrightarrow{0}A\xrightarrow{2}A\), and compactness makes ordinary and compact cohomology agree. Thus \(H_c^2(X;A)=A/2A\). Formula (6) gives
\[
 \Gamma(X;\mathcal Z_2)
 =\operatorname{Hom}_A(A/2A,A)=\{a\in A:2a=0\},
 \qquad\text{(28)}
\]
which has exactly the two values above.

The finite cellular cochain complex is free. Applying its derived \(A\)-dual computes \(R\Gamma(X;\omega_X)\) by (5), with \(A\xrightarrow{2}A\xrightarrow{0}A\) in degrees \(-2,-1,0\), up to the harmless consistent basis sign. Over \(\mathbb Z\) it has \(H^{-2}=0\), \(H^{-1}=\mathbb Z/2\) and \(H^0=\mathbb Z\). In particular the dualizing object is not zero just because there is no integral top cycle. No characteristic-zero assumption or division by two belongs in these constructions.
