# SH02-RR — From directional tests to further microlocal theories

Original English lesson for SH-02, released under CC0 1.0. The calculations below use the cited course results with their individual prerequisite status; the research projects do not import the later theorems they ask the reader to study.

A useful research question identifies which part of a construction survives a change of setting. Here the changes are concrete: deleting a zero section, replacing a positive real parameter by a complex one, imposing constructibility, transporting a cotangent relation, or recognizing a sheaf as the solutions of an operator system. Each route begins with a calculation available in this course and specifies what further theorem would be needed.

## SH02-RR-START — Choose the object before choosing the application

The standing sheaf coefficients are a commutative unital ring $k$ of finite global dimension. Bounded sheaf complexes may have arbitrary modules as stalks. A field, perfect stalks, a complex analytic manifold, or a coherent operator module enters only where explicitly stated below.

For a first pass, take the routes in the order written. They connect the following prerequisites:

| Start with | Then use | Question it makes precise |
|---|---|---|
| [Orientation and trace](../../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-TRACE) | [Fourier halfspaces](../../sheaf-proof-readings/SH02-fourier-sato.html#SH02-FS-SETUP) | Which boundary and shift does a transform retain? |
| [The deformation manifold](../../sheaf-proof-readings/SH02-normal-geometry.html#SH02-NG-CONSTRUCTION) | [Specialization section tests](../../sheaf-proof-readings/SH02-specialization.html#SH02-SP-SECTIONS) | Which limiting neighborhoods define the new sheaf? |
| [Between-level cohomology](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-MORSE) | [Finite critical complexes](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-MORSE-INEQUALITIES) | When do local directional obstructions produce numerical invariants? |
| [Localized morphisms](../../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-POINT) | [Kernel composition](../../sheaf-proof-readings/SH02-microlocal-hom.html#SH02-MH-KERNEL-COMPOSITION) | Which correspondence carries an actual equivalence? |
| [Involutivity](../involutivity.html#sh02-inv-theorem-microsupport-is-involutive) | [Directed propagation](../involutivity.html#sh02-inv-microlocal-flow-sections-between-opposite-sides-of-a-level-set) | What extra identification turns a sheaf result into an analytic result? |

The categorical foundations are taught in *Categorical and derived tools for analytic sheaves*; contact transformations, constructible sheaves and characteristic cycles in *Constructible and perverse sheaves*. A project may isolate a needed supporting lemma from another theory; it must specify that lemma without claiming the surrounding theory has been completed.

## SH02-RR-BOUNDARIES — Keep the zero section visible

Begin with [SH02-FS-CONE](../../sheaf-proof-readings/SH02-fourier-sato.html#SH02-FS-CONE), [SH02-SP-ZERO](../../sheaf-proof-readings/SH02-specialization.html#SH02-SP-ZERO), and the [direction-space comparisons](../conic-and-trace-applications.html#sh02-cta-radial-passing-from-vector-bundles-to-their-direction-spaces). On the oriented line, let $T$ be the Fourier functor defined by the nonpositive pairing $x\xi\leq0$. For the constant coefficient sheaf $k$ these calibrations are

$$
\begin{aligned}
T k_{\{0\}}&\simeq k_{\mathbb R},&
T k_{\mathbb R}&\simeq k_{\{0\}}[-1],\\
T k_{[0,\infty)}&\simeq k_{(0,\infty)},&
T k_{(0,\infty)}&\simeq k_{(-\infty,0]}[-1].
\end{aligned}
$$

**Check.** The zero input fibre integrates a point, and the whole-line input has nonzero compactly supported fibre cohomology only at $\xi=0$. The other two identities are the closed and open cone formulas. The orientation of the line identifies its orientation local system with $k$; the compact-support degree contributes $[-1]$. Thus changing a closed endpoint to an open endpoint changes both the output support and its degree.

**Project.** For a real vector bundle $E\to B$, compare a conic sheaf with the sheaf it induces on $(E\setminus0)/\mathbb R_{>0}$. Recover separately the data measured by zero-section inverse image and exceptional inverse image. Use the displayed line examples to test the difference between extending punctured data by $Rj_*$ and by $j_!$. Then write the two sphere-transform comparisons with the radial-first orientation convention of [SH02-MD-SPHERE](../../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-SPHERE).

The output should be a diagram containing the extension maps and the zero-section localization triangle. An equivalence on the sphere of directions alone cannot recover which extension was chosen. Over a nonorientable bundle, retain its orientation local system in the diagram rather than selecting unrelated local generators. The algebraic Fourier transforms mentioned in the antecedents live in other coefficient categories; this project provides a geometric calibration for a future comparison, not an identification with them.

## SH02-RR-DEFORMATION — Compare parameters as well as central fibres

Use [SH02-NG-FUNCTORIALITY](../../sheaf-proof-readings/SH02-normal-geometry.html#SH02-NG-FUNCTORIALITY), [SH02-NG-CONE-SEQUENCES](../../sheaf-proof-readings/SH02-normal-geometry.html#SH02-NG-CONE-SEQUENCES), and [SH02-SP-HOMOGENEOUS](../../sheaf-proof-readings/SH02-specialization.html#SH02-SP-HOMOGENEOUS). In an adapted chart $(u,z)$ with center $u=0$, the real deformation has coordinates $(v,z,t)$ and map

$$
u=tv.
$$

At $t=0$ the coordinate $v$ runs through the entire normal vector space. Positive time selects the one-sided limit used to define specialization. The [parameter orientation](../../sheaf-proof-readings/SH02-normal-geometry.html#SH02-NG-PARAMETER-ORIENTATION) records the relative determinant factor even where the deformation map is not submersive.

There is a small algebraic chart calculation that makes the comparison concrete. Let $K$ be any field, used here for coordinate algebras independently of the sheaf coefficient ring $k$. With $u=(u_1,\ldots,u_r)$, form

$$
A=K[u,z,t,v]/(u_1-tv_1,\ldots,u_r-tv_r).
$$

Eliminating the $u_i$ identifies $A$ with $K[z,t,v]$. Its central quotient is $K[z,v]$, and after inverting $t$ one may instead eliminate $v_i=t^{-1}u_i$, obtaining $K[u,z,t,t^{-1}]$. This verifies the full normal fibre and the unchanged nonzero fibres in this coordinate model. It does not choose a sheaf theory on the corresponding algebraic spaces.

**Project.** First carry out the chart calculation for a map of pairs whose normal differential has a kernel. Compare the coordinate map with the clean-embedding criterion in [SH02-NG-CLEAN-EMBEDDING](../../sheaf-proof-readings/SH02-normal-geometry.html#SH02-NG-CLEAN-EMBEDDING). Next choose a holomorphic function $f:X\to\mathbb C$ on a complex manifold and study the nearby- and vanishing-cycle construction of [Nearby cycles, monodromy and specialization](https://kokunoyumeto.github.io/open-math-courses-public/courses/nearby-cycles-monodromy-and-specialization/). The definitions start with $F\in D^b(k_X)$. For the regular section comparison, take $df\ne0$ along $Y=f^{-1}(0)$ and a weakly $\mathbb C$-constructible $F$. Record the choice of a lift in the universal cover of $\mathbb C^*$, the monodromy, and the shifted triangles before comparing nearby and vanishing cycles with normal specialization and microlocalization. General cycle constructions and these particular section comparisons have different hypotheses.

The positive real parameter is contractible; a punctured complex parameter has loops. Consequently a comparison must explain what happens to monodromy, as well as to the central fibre. A completed project should calculate both sides in one nonsingular local model and identify the extra theorem required to extend that calculation to a singular function. The algebraic deformation and any etale or coherent-sheaf version require their own exact sources and operation theorems. The complex nearby-cycle route belongs to SH-03. For a holomorphic map $f$ to a one-dimensional complex manifold, a bounded $\mathbb C$-constructible complex $G$ on its source and a compact subset $K$ of a fibre $f^{-1}(x)$, Proposition 8.6.2 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) gives open neighbourhoods $U$ of $x$ and $V\subset f^{-1}(U)$ of $K$ such that the direct images of $G|_V$ by $f|_V:V\to U$, with and without proper supports, are $\mathbb C$-constructible, and bounds their microsupports by the image of $\operatorname{SS}(G)$ under the cotangent correspondence of $f$; the memoir notes that the statement fails when the target has dimension other than one. Determine which step of the nearby-cycle construction this statement can supply.

## SH02-RR-MORSE — Turn local tests into finite information

Start with [SH02-MO-RELATIVE-CUTOFF](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-RELATIVE-CUTOFF) and [SH02-MO-FIELD-BOUNDARY](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-FIELD-BOUNDARY). The local datum at a possible critical level is a complex,

$$
J_x=\bigl(R\Gamma_{\{\varphi\geq\varphi(x)\}}F\bigr)_x.
$$

Its degree, its module structure, and the side of the inequality all matter. Numerical Morse inequalities follow in the course when $k$ is a field, every support sublevel is compact, the graph of $d\varphi$ meets microsupport in finitely many points, and the resulting $J_x$ have finite-dimensional bounded cohomology. These hypotheses do not impose constructibility on every sheaf in the course.

**Project.** Separate the following two extensions of that calculation.

1. For a smooth function with a nondegenerate critical point, compute $J_x$ in Morse coordinates and track the orientation line of its negative Hessian space. Then apply the finite-jump theorem to a function with finitely many such points and compact sublevels. The local calculation and the passage to the global Euler formula are part of the assigned SH-02 mathematical obligations; a project proposal does not count as their solution.
2. On a real analytic manifold, choose a sheaf adapted to a finite local stratification with one singular stratum. Determine the additional control on limiting conormals that makes the stratumwise tests compatible. Compare ordinary addition with the [asymptotic sum](../../sheaf-proof-readings/SH02-asymptotic-estimates.html#SH02-AE-SUM), and examine the constructibility criteria in Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Chapter 8, and in Stéphane Guillermou's [*Sheaves and symplectic geometry of cotangent bundles*](https://arxiv.org/abs/1905.07341v3), §1.2.3.

For the second project, use the $\mu$-stratification condition (Guillermou, Definition 1.2.19) when invoking the conormal criterion (Guillermou, Proposition 1.2.20); an arbitrary decomposition into strata is insufficient. Distinguish local constancy on strata from perfectness of stalk complexes, and distinguish either condition from the [cohomological constructibility condition used for duality](../../sheaf-proof-readings/SH02-cohomological-biduality.html#SH02-CB-SYSTEMS). State which version is used by the particular later theorem. The stratification and constructibility theory belongs to SH-03; the local critical complexes and endpoint conventions remain visible prerequisites here.

<a id="SH02-RR-MORSE-SOLUTION"></a>

### The local index, the finite Euler sum and the endpoint check

Here is the solution of the first project at the precise coefficient scope where an index determines the local object. Let \(\varphi\) have a nondegenerate critical point \(x\), with negative Hessian space \(E^-_x\) of dimension \(\tau\). Suppose \(F\) is a constant bounded coefficient complex on a sufficiently small Morse chart. Write \(P=F_x\). The full coordinate and supported-map calculation TMC1–TMC4 gives

\[
J_x\simeq P\otimes_k\operatorname{or}(E^-_x)[-\tau].
\tag{RMS1}
\]

Indeed the actual localization restriction is from the chart ball to its negative sublevel. In signed Morse coordinates \(\varphi-\varphi(x)=|u|^2-|v|^2\), the collapse \((u,v)\mapsto((1-s)u,v)\) preserves both members of this pair and their restriction map. It gives the negative disk relative to its punctured disk. Proper compact-interval units identify the endpoint maps, and the oriented Euclidean costalk is the displayed line in degree \(\tau\). Reversing the chosen negative orientation changes its generator by \(-1\); the orientation line records that choice without selecting a global trivialization. Index zero and dimension zero give \(P\) in degree zero. An arbitrary coefficient sheaf with extra singularities has its actual supported complex \(J_x\); a Hessian alone does not determine it.

For the finite global calculation impose the exact [MO34–MO36 hypotheses and restriction triangles](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-MORSE-INEQUALITIES): a field, compact support sublevels, finitely many intersections of \(d\varphi\) with microsupport, and bounded finite-dimensional local jump cohomology. Put \(L_\nu=\bigoplus_{\varphi(x_i)=c_\nu}J_{x_i}\). The actual level triangles are \(L_\nu\to B_\nu\to B_{\nu-1}\xrightarrow{+1}\), with \(B_0=0\) and \(B_r\simeq R\Gamma(X;F)\). Additivity of the alternating dimensions follows from the bounded long exact cohomology sequence, so

\[
\begin{gathered}
\chi R\Gamma(X;F)=\sum_i\chi J_{x_i},\\
\chi J_{x_i}=(-1)^{\tau_i}\chi P_i\\
\text{under the local hypothesis}\\
\text{of RMS1}.
\end{gathered}
\tag{RMS2}
\]

This proves the global Euler sum using the actual jumps; coincident critical values are grouped in the same direct sum, and the zero-jump case is the zero object. No splitting of the finite filtration is used. Only this numerical conclusion requires finite-dimensional field cohomology; RMS1 permits the original arbitrary bounded modules over the course ring.

The proposed endpoint test also has an explicit solution. On the oriented real line let \(F_c=k_{[0,\infty)}\) and \(F_o=k_{(0,\infty)}\), where the second is open extension by zero. At zero, with the displayed support inequality, localization and the [halfline boundary maps SPH10–SPH11](../sphere-kernels.html#SH02-SPH-BOUNDARY-ADJOINT) give

\[
\begin{array}{c|cc}
 & R\Gamma_{\{t\ge0\}}|_0 & R\Gamma_{\{t\le0\}}|_0\\
F_c & k & 0\\
F_o & 0 & k[-1]
\end{array}
\tag{RMS3}
\]

For the positive support both sheaves are already supported on the closed halfline, so the test is their stalk, respectively \(k\) and zero. For the negative support the closed-halfline costalk vanishes by the compact-support halfline contraction. For the open halfline, its localization triangle at zero is the fibre of \(0\to k\), giving \(k[-1]\); the boundary ordinary-section unit is the identity on \(k\). These are actual support maps before Euler characteristics, and the closed and open endpoint conventions produce different local objects.

<a id="SH02-RR-MU-REFINEMENT"></a>
<a id="sh02-rr-mu-refinement--the-geometric-input-for-a-conormal-criterion"></a>

<a id="SH02-RR-CHARACTERISTIC-VALUES"></a>

The [characteristic-value theorem](../characteristic-values-from-analytic-cells.html#CV0) proves local finiteness for an analytic function proper on the base of a closed conic subanalytic isotropic set. Its [limiting-tangent proof](../characteristic-values-from-analytic-cells.html#CV2) handles singular incidence. This is the value-avoidance result available for the isotropic constructions below, with properness and subanalyticity retained.

### The geometric input for a conormal criterion

Let \(X\) be a real analytic manifold of finite dimension \(n\), Hausdorff and countable at infinity. Subanalyticity and local finiteness are measured in the ambient \(X\), including points outside a stratum. A stratification is a locally finite partition into subanalytic analytic submanifolds of fixed dimension, with the frontier rule \(S_b\cap\overline{S_a}\ne\varnothing\Rightarrow S_b\subset\overline{S_a}\). Strata may be disconnected. Splitting connected components uses the subanalytic component theorem; local finiteness does not mean a globally finite number of strata.

The exact ordered condition is

\[
\begin{gathered}
\bigl(T_M^*X\widehat{+}T_N^*X\bigr)
\cap\pi^{-1}N\subset T_N^*X,\\
\pi:T^*X\longrightarrow X.
\end{gathered}
\tag{RRM1}
\]

It is required when \(N\) is a lower stratum in \(\overline M\setminus M\). Although the full limiting sum is symmetric, its restriction and target in (RRM1) depend on \(N\). Using [the full sequence test](../../sheaf-proof-readings/SH02-asymptotic-estimates.html#SH02-AE-SUM), its covectors may grow without bound: \(x_j\in M\), \(y_j\in N\), both bases tend to \(x\in N\), \(\xi_j+\eta_j\to\sigma\), and \(|x_j-y_j|\,|\xi_j|\to0\). The conclusion is \(\sigma|_{T_xN}=0\). Ordinary addition at a common base would give the empty set for disjoint strata and could not test this condition.

**Geometric carrying theorem, relative to the stated subanalytic inputs.** For a closed positive-conic subanalytic set \(\Lambda\subset T^*X\), canonical-form isotropy is equivalent to the existence of a \(\mu\)-stratification \(\mathcal S\) with

\[
\begin{gathered}
\Lambda\subset\Lambda_{\mathcal S},\\
\Lambda_{\mathcal S}=\bigcup_{S\in\mathcal S}T_S^*X.
\end{gathered}
\tag{RRM2}
\]

The stratification can simultaneously respect every membership in a prescribed locally finite subanalytic cover of \(X\). Isotropy here means that \(\alpha=\sum_i\xi_i\,dx_i\) vanishes on the regular locus. No coefficient ring, stalk perfection or sheaf boundedness assumption enters this geometric theorem.

**Proof and prerequisite accounting.** The finite conormal-cover proof supplies smooth subanalytic bases \(G_1,\ldots,G_m\) such that

\[
\begin{gathered}
\Lambda\subset\bigcup_{i=1}^{m}\overline{T_{G_i}^*X},\\
m\le n+1.
\end{gathered}
\tag{RRM3}
\]

Its finite bound counts possibly disconnected bases. On a maximum-rank regular part of the current cotangent remainder, projection is generically a submersion onto a smooth base \(G_i\). A lift of a base tangent vector is annihilated by \(\alpha\), so the cotangent covector annihilates that vector. Density then covers that whole regular part by \(\overline{T_{G_i}^*X}\). Removing this **closed** piece leaves an open subanalytic remainder whose maximum regular projection rank is smaller. Keep the remainder itself rather than closing it; rank zero terminates the process. Subanalytic regularity and dimension theory, conic projection and Sard's theorem are the precise inputs of this rank argument.

The compatible refinement proof applies to the prescribed cover enlarged by these finitely many \(G_i\) and \(X\setminus\bigcup_iG_i\). Compatibility means each stratum is wholly contained in or disjoint from each member. Here is why the refinement preserves the already established conditions. For an ordered pair, form its actual failure set

\[
\begin{gathered}
B_{M,N}=N\cap\pi\bigl(\\
(T_M^*X\widehat{+}T_N^*X)\\
\setminus T_N^*X\bigr).
\end{gathered}
\tag{RRM4}
\]

The limiting-sum isotropy proof and conic projection make this set subanalytic; generic conormality along \(N\) makes its relative closure nowhere dense in \(N\). Conic projection here is justified by restricting vectors to a bounded fibre disk, not by asserting that the full cotangent projection is proper.

Start with an ordinary compatible stratification. Suppose its possible failures are confined to a closed subanalytic union of strata \(Y\). For the locally finite union \(B\) of its incident-pair failure sets, put

\[
\begin{gathered}
\Omega=X\setminus\overline B^{\,X},\\
Y'=X\setminus\Omega\subset Y.
\end{gathered}
\tag{RRM5}
\]

The old stratification is \(\mu\) on \(\Omega\). To see that \(\Omega\cap Y\) is dense in \(Y\), choose in any nonempty relative open subset a regular patch of \(Y\) occupied by one stratum. There are only finitely many possible upper strata near that patch. The finite intersection of their pairwise open dense good loci contains a point with an ambient neighborhood disjoint from \(B\). This point belongs to \(\Omega\). The argument applies also to smaller-dimensional regular components of \(Y\); it does not assume pure dimension.

Keep each old stratum intersected with \(\Omega\). Refine only \(Y'\), remembering both original memberships and every \(Y'\cap\overline{S\cap\Omega}\). The latter memberships force every new lower stratum to lie wholly inside each upper frontier it meets. Closedness of \(Y'\) excludes a lower frontier entering \(\Omega\); incidences inside each part are those of its own stratification. Thus the combined partition has the full frontier rule. Since \(Y'\) is nowhere dense in \(Y\), subanalytic dimension gives \(\dim Y'<\dim Y\) when it is nonempty. Starting with \(Y=X\), at most \(n+1\) such steps leave no bad set. This bounds the number of stages, not the global number of strata. An arbitrary ordinary refinement of the whole good part would not preserve the \(\mu\)-condition.

For this final stratification, \(\Lambda_{\mathcal S}\) is closed. Indeed, local finiteness reduces any convergent conormal sequence to one upper stratum \(M\). If its limiting base lies in another stratum \(N\), the frontier rule and (RRM1), applied with the second covector zero, put its finite limit in \(T_N^*X\). Limits within the same stratum stay in its smooth conormal bundle. Its subanalyticity, conicity and isotropy follow from the locally finite union and singular one-form restriction rules. Membership compatibility gives \(T_{G_i}^*X\subset\Lambda_{\mathcal S}\), since a stratum contained in \(G_i\) has a smaller tangent space. Closedness then includes **all the closures** in (RRM3), proving (RRM2). Conversely, the singular one-form subset rule passes isotropy of \(\Lambda_{\mathcal S}\) to its subanalytic subset \(\Lambda\). \(\square\)

The underlying subanalytic lesson expressly retains deep set-operation, regularity, dimension, curve-selection, uniformization, resolution and compatible-triangulation inputs. Triangulation enters its surjective one-form detection argument, which is used in the boundary-form proof behind limiting-sum isotropy. These are remaining prerequisites, not newly proved foundations here. The published programme expositions used above are CC0; referenced works retain their own licences.

<a id="SH02-RR-MU-SHEAF"></a>
<a id="sh02-rr-mu-sheaf--sheaves-on-the-prescribed-microlocal-strata"></a>

### Sheaves on the prescribed microlocal strata

Let \(X\) be a finite-dimensional real analytic manifold, Hausdorff and countable at infinity, let \(\mathcal S\) be a locally finite subanalytic \(\mu\)-stratification, and let \(k\) be a commutative ring of finite global dimension. For \(F\in D^b(k_X)\), the exact fixed-stratification statement is

\[
\begin{gathered}
\operatorname{SS}(F)\subset\Lambda_{\mathcal S}\\
\Longleftrightarrow\\
H^j(F)|_S\text{ is locally constant}\\
\text{for every }S\in\mathcal S\text{ and every }j.
\end{gathered}
\tag{FSI1}
\]

This uses the **same** strata on both sides. It requires neither finite generation nor perfect stalks. The following deduction uses the [full tensor estimate](../../sheaf-proof-readings/SH02-characteristic-estimates.html#SH02-CHE-006), the [closed-embedding equality](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-PROPER-PUSH), the [zero-section local-constancy criterion](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-SUBMERSION), and the [missing-submanifold boundary estimate](../../sheaf-proof-readings/SH02-asymptotic-estimates.html#SH02-AE-BOUNDARY). Their foundational contracts remain explicit. In a local chart \(U\) with closed smooth \(S\), write \(i:S\hookrightarrow U\) and \(j:U\setminus S\hookrightarrow U\). The exact estimates needed are

\[
\begin{gathered}
\operatorname{SS}(A\otimes^LB)\subset
\operatorname{SS}(A)\widehat+\operatorname{SS}(B),\\
\operatorname{SS}(i_*H)=i_\pi i_d^{-1}\operatorname{SS}(H),\\
\operatorname{SS}(j_!K)\cap T^*U|_S\subset\\
\operatorname{SS}(K)\widehat+T_S^*U.
\end{gathered}
\tag{FSI2}
\]

Here \(A,B\in D^b(k_U)\), \(H\in D^b(k_S)\), \(K\in D^b(k_{U\setminus S})\), and \(i_d:T^*U|_S\to T^*S\) restricts covectors to \(TS\). The first and third lines impose no noncharacteristic or properness hypothesis. In the third line the first cotangent set is taken over the open complement and need not be ambient closed. The limiting operation is the [full sequence operation](../../sheaf-proof-readings/SH02-asymptotic-estimates.html#SH02-AE-SUM), not ordinary addition.

First the ordered \(\mu\)-condition implies the absorption bound

\[
\begin{gathered}
(\Lambda_{\mathcal S}|_U\widehat+T_S^*U)\cap T^*U|_S\\
\subset T_S^*U.
\end{gathered}
\tag{FSI3}
\]

Indeed, a full limiting witness has first base points on the strata and second base points in \(S\). Local finiteness allows a subsequence with the first base points in one fixed stratum \(R\). If \(R\ne S\), the frontier rule makes \(S\) a lower incident stratum, so (RRM1) gives precisely the conclusion. If \(R=S\), straighten \(S\) in smooth analytic coordinates: both covectors have zero tangential components there, so their convergent sum has zero tangential component. The coordinate comparison in (AE.25), with error bounded by the base separation times the first covector norm, retains this conclusion even when both summands diverge. The same proof applies when the first set is any subset of the total conormal, including its restriction to \(U\setminus S\).

Suppose now that the left side of (FSI1) holds. At a point of a stratum choose \(U\) so that its piece \(S\) is closed in \(U\). Inverse image to \(S\) and direct image from this closed embedding are exact. There is a canonical isomorphism

\[
i_*i^{-1}(F|_U)\simeq F|_U\otimes^Lk_S.
\tag{FSI4}
\]

One may check it on stalks: the stalks of \(k_S\) are \(k\) on \(S\) and zero elsewhere, so it is flat and tensoring restricts the original stalks exactly as the left side does. The first line of (FSI2), the bound \(\operatorname{SS}(k_S)\subset T_S^*U\), and (FSI3) put the microsupport of (FSI4) over \(S\) in \(T_S^*U\). Outside \(S\) that object vanishes locally, so this is its entire microsupport bound. The second line of (FSI2), and surjectivity of \(i_d\), now put the intrinsic microsupport of \(i^{-1}F\) in the zero section of \(T^*S\). The zero-section criterion gives local constancy of every cohomology sheaf. Exact inverse image identifies these sheaves with \(H^j(F)|_S\), proving the forward implication.

Conversely assume those cohomology restrictions are locally constant. Work in an ambient open neighborhood meeting only finitely many strata. Keep a closed union \(Y\) of its strata such that the conormal bound is already proved on the complement; initially \(Y\) is the entire neighborhood. If \(Y\) is nonempty, take a maximal stratum \(S\) in its finite frontier order. It is open in \(Y\): no closure of another stratum in \(Y\) can meet it from above, and a finite union of the other closures is closed. Thus \(Y'=Y\setminus S\) is closed. In the open manifold \(U=X\setminus Y'\) (inside the chosen neighborhood), \(S\) is closed and its complement is the part already proved.

For these inclusions the actual localization triangle is

\[
\begin{gathered}
j_!j^{-1}(F|_U)\longrightarrow F|_U\\
\longrightarrow i_*i^{-1}(F|_U)\xrightarrow{+1}.
\end{gathered}
\tag{FSI5}
\]

The zero-section criterion and the closed-embedding equality put the third term's microsupport in \(T_S^*U\). The first term has the induction bound on the complement; over \(S\) the third line of (FSI2), monotonicity, and (FSI3) put its microsupport in \(T_S^*U\) as well. The microsupport triangle inequality therefore gives the desired total-conormal bound for the middle term on \(U\). Replace the residual by \(Y'\) and repeat. Only finitely many local strata are removed; no globally finite stratification is assumed. Locality proves the reverse implication of (FSI1). \(\square\)

Applying this result to each degree-zero cohomology sheaf, and using the finite canonical truncation triangles, also gives

\[
\begin{gathered}
\operatorname{SS}(F)\subset\Lambda_{\mathcal S}\\
\Longleftrightarrow\\
\operatorname{SS}(H^j(F))\subset\Lambda_{\mathcal S}\\
\text{for every }j.
\end{gathered}
\tag{FSI6}
\]

The forward implication uses (FSI1) twice and retains the chosen stratification. In the reverse implication choose a finite cohomology interval \([a,b]\) and use the triangles \(\tau^{\le j-1}F\to\tau^{\le j}F\to H^j(F)[-j]\xrightarrow{+1}\) from \(j=a\) to \(b\), starting with zero. Shift invariance and the triangle bound suffice. No splitting of the extension data or uniform finite dimension of stalk modules is used.

The \(\mu\) hypothesis cannot be replaced by an arbitrary smooth subanalytic frontier partition. For \(k\ne0\) take \(Z=\{x^3=y^3z\}\subset\mathbb R^3\), \(N=\{x=y=0\}\), \(M=Z\setminus N\), and \(O=\mathbb R^3\setminus Z\). These form an ordinary finite stratification: \(M\) is smooth since its points have \(y\ne0\) and the defining equation has nonzero \(z\) derivative; the parametrization \((s,t)\mapsto(st,s,t^3)\), \(s\ne0\), gives \(\overline M=Z\); the nonzero polynomial makes \(\overline O=\mathbb R^3\). The sheaf \(k_Z\) is constant on \(M,N\) and zero on \(O\). At \((0,s,0)\), \(s\ne0\), the two tangent directions of that parametrization are \((0,1,0)\) and \((s,0,0)\), so the closed-embedding equality gives the normal \(dz\). Closedness of microsupport then yields

\[
\begin{gathered}
(0,0,0;dz)\in\operatorname{SS}(k_Z),\\
(\Lambda_{\{O,M,N\}})_{(0,0,0)}\\
=\mathbb R\,dx+\mathbb R\,dy.
\end{gathered}
\tag{FSI7}
\]

This verifies the failed fixed-partition bound directly. Geometry alone does not impose finite coefficients: an infinite-dimensional constant sheaf over a field still satisfies (FSI1) for the one-stratum partition.

The complete programme antecedent is Constructibility from microsupport and perfect stalks, the exact estimates and fixed-stratification proof; its cohomology formulation has the same scope. These checked programme expositions are CC0. The new calculations and exposition here are likewise dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). This supplies the fixed-stratum sheaf deduction relative to the named estimates; the stated estimates retain their original coefficient and stratification hypotheses.


<a id="SH02-RR-MU-WITNESS"></a>
<a id="sh02-rr-mu-witness--a-frontier-that-needs-unbounded-cancellation"></a>

### A frontier that needs unbounded cancellation

The polynomial frontier calculation provides a concrete check on the distinction. In coordinates \((t,x,y)\) on \(\mathbb R^3\), set

\[
\begin{gathered}
g=y^2-t^2x^2-x^3,\\
Z=\{g=0\},\\
M=Z\cap\{x\ne0\},\\
N=\{x=y=0\},\\
O=X\setminus Z.
\end{gathered}
\tag{RRM6}
\]

The three pieces \(O,M,N\) are analytic submanifolds, and their closures satisfy \(\overline M=Z\) and \(\overline O=X\); the three-piece partition has the frontier rule. For the first equality use \((t,s)\mapsto(t,s^2-t^2,s(s^2-t^2))\) with \(s\ne\pm t\); every axis point is a limit. The gradient of \(g\) is nonzero on \(M\): if \(y=0\), its equation forces \(x=-t^2\ne0\), and its \(x\) derivative is then \(-t^4\).

For \(r>0\) tending to zero, choose

\[
\begin{gathered}
a_r=(r,-r^2,0)\in M,\\
b_r=(r,0,0)\in N,\\
\xi_r=dt+\frac{dx}{2r}\in T_{a_r,M}^*X,\\
\eta_r=-\frac{dx}{2r}\in T_{b_r,N}^*X.
\end{gathered}
\tag{RRM7}
\]

At \(a_r\) the gradient is \((-2r^5,-r^4,0)\), so the claimed upper covector is conormal. The lower conormal annihilates \(\partial_t\). Yet

\[
\begin{gathered}
\xi_r+\eta_r=dt,\\
|a_r-b_r|\,|\xi_r|=\frac r2\sqrt{1+4r^2}\longrightarrow0,\\
dt(\partial_t)=1.
\end{gathered}
\tag{RRM8}
\]

Thus (RRM1) fails at the origin. Normalizing the upper covector to bounded norm gives the limit \(dx\), a legitimate lower conormal, and loses this failure. Replacing the full sum by ordinary addition loses it as well.

Isolating the origin repairs the partition. Near a nonzero axis point, the two upper sheets are \(y=\pm x\sqrt{t^2+x}\); their \(t\) derivative is bounded by \(C|x|\). For a conormal \(\zeta\), its projection onto the lower tangent is therefore bounded by \(C|a-b|\,|\zeta|\), uniformly for nearby upper and lower points. In a full limiting-sum witness this tangential component tends to zero, proving (RRM1) over \(N\setminus\{0\}\). Pairs from the open stratum are automatic, and a point lower stratum has the full cotangent fibre. Hence \(O,M,N\setminus\{0\},\{0\}\) is a compatible \(\mu\)-refinement.

This establishes the geometric carrying and refinement input at its stated prerequisite scope. The [fixed-stratum sheaf criterion](#SH02-RR-MU-SHEAF) above now gives that converse and its reverse, relative to the exact named microsupport estimates. The [controlled-field flow proof](../../sheaf-proof-readings/SH02-open-prerequisite-proofs.html#SH02-PRP-CONTROLLED-FLOW) now proves the continuous local flow once compatible tube data and a controlled lift are given. The [controlled-lift proof](../../sheaf-proof-readings/SH02-open-prerequisite-proofs.html#SH02-PRP-CONTROLLED-LIFT) supplies the field from the compatible data. For smooth ambient maps submersive on every stratum, the [compatible-tube proof](../../sheaf-proof-readings/SH02-open-prerequisite-proofs.html#SH02-PRP-COMPATIBLE-TUBES) now constructs the data from explicit ordinary differential-topology inputs. Those inputs are separate from the microlocal dimension induction. Involutivity alone does not supply the subanalytic isotropy assumed in (RRM2).

A useful first test is to replace a halfspace sheaf by the extension from its open interior. Compute the two $J_x$ using the localization triangle before taking Euler characteristics. This catches an endpoint error that a calculation of the underlying support set would miss.

## SH02-RR-CONTACT — Ask which dilation a transformation respects

The starting results are the [Fourier cotangent map](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-LEGENDRE), its [two dilation actions](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-SYMPLECTIC), and [localized kernel composition](../../sheaf-proof-readings/SH02-microlocal-hom.html#SH02-MH-KERNEL-COMPOSITION). In bundle coordinates the map is

$$
\Phi_E(z,x;\zeta,\xi)=(z,\xi;\zeta,-x),
\qquad
\Phi_E^*\alpha_{E^*}=\alpha_E-d\langle x,\xi\rangle.
$$

It preserves the symplectic form. On components of positive bundle rank it does not commute with ordinary cotangent dilation: scaling a nonzero $\xi$ changes the target base coordinate. On a rank-zero component, $E=Z$ and $\Phi_E$ is the identity on $T^*Z$, so it does commute with that dilation. Its square is the cotangent lift of the vector-bundle antipode, which fixes $\zeta$. These are useful tests before attempting to pass to a space of directions.

**Project.** Choose open conic cotangent domains and a homogeneous symplectomorphism between them. Describe its signed graph in the product cotangent bundle. Find the conditions on a sheaf kernel that would make its two convolution composites the diagonal kernels in the appropriate localized categories. Check the unit and counit maps, the restriction on supports, and the compatibility with $\mu hom$; use [SH02-MH-COMPOSITION](../../sheaf-proof-readings/SH02-microlocal-hom.html#SH02-MH-COMPOSITION) to specify the last requirement.

Theorem 6.3.4 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), stated for a commutative coefficient ring of finite weak global dimension, takes open conic sets $\Omega_X\subset T^*X$ and $\Omega_Y\subset T^*Y$, a closed Lagrangian submanifold $\Lambda$ of $\Omega_X^a\times\Omega_Y$, where $a$ is the antipodal map, and $K\in D^b(k_{X\times Y})$. It assumes that the maps $(x,y;\xi,\eta)\mapsto(x;-\xi)$ from $\Lambda$ to $\Omega_X$ and $(x,y;\xi,\eta)\mapsto(y;\eta)$ from $\Lambda$ to $\Omega_Y$ are diffeomorphisms, that $\operatorname{SS}(K)\cap(\Omega_X^a\times T^*Y)$ and $\operatorname{SS}(K)\cap(T^*X\times\Omega_Y)$ are contained in $\Lambda$, that $K$ is cohomologically constructible, and that the natural morphism $k_\Lambda\to\mu hom(K,K)|_\Lambda$ is an isomorphism. It concludes that the functors $G\mapsto Rq_{1*}R\mathcal Hom(K,q_2^!G)$ and $F\mapsto Rq_{2!}(K\otimes q_1^{-1}F)$, where $q_1,q_2$ are the projections of $X\times Y$, are quasi-inverse equivalences between $D^+(Y;\Omega_Y)$ and $D^+(X;\Omega_X)$. Determine whether your candidate satisfies every condition, and whether the conclusion persists when the two maps from $\Lambda$ are only homeomorphisms. Then study the local realization and shift calculations in the same memoir, Theorem 6.3.5 and §7.4. The existence of a kernel for a contact transformation, the purity conditions along a Lagrangian, and the inertia-index shift are SH-03 results. The Fourier coordinate exchange above supplies a controlled model with two actions; it is not, by that fact alone, a map of ordinary cosphere quotients.

A concrete deliverable is a diagram with three panels: the geometric signed graph, the two kernel composites, and the induced map on microlocal Hom. Mark every shift in the second panel and every antipode in the first. If the projection rank of a Lagrangian changes, determine exactly which later shift theorem is needed instead of assigning a constant degree from a regular point.

## SH02-RR-OPERATORS — Identify the solution object before using its microsupport

Begin with [SH02-INV-THEOREM](../involutivity.html#sh02-inv-theorem-microsupport-is-involutive), [SH02-MH-HOM](../../sheaf-proof-readings/SH02-microlocal-hom.html#SH02-MH-HOM), and [SH02-MC-IDENTITY](../../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-IDENTITY). The analytic route changes both the coefficient field and the category of inputs. On a complex manifold $X$, the operator sheaf $\mathcal D_X$ and the holomorphic function sheaf $\mathcal O_X$ lead to

$$
\operatorname{Sol}(\mathcal M)
=R\mathcal Hom_{\mathcal D_X}(\mathcal M,\mathcal O_X).
$$

The external bridge to study is **Theorem 10.1.1** of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf): for a coherent $\mathcal D_X$-module, it identifies the microsupport of this solution complex with the characteristic variety, using the memoir's identification of complex and underlying real cotangent bundles. Holonomicity is not a hypothesis of this particular theorem. Its proof and the required analytic and operator-module foundations belong to SH-03. In the convention of §8.5.1 of the memoir, a real covector $a\,dx+b\,dy$ corresponds to $\zeta\,dz$ with $\zeta=(a-ib)/2$; thus the inverse map is $2\operatorname{Re}(\zeta\,dz)$. The normalization is part of the comparison, even though a positive scalar preserves a conic set.

**Project.** On a complex coordinate disk, take the operator $\partial_z$ and the module $\mathcal D/\mathcal D\partial_z$. Compute its solution complex from the two-term operator resolution. Local holomorphic primitives should account for the positive-degree term, and the surviving solutions should agree with the microsupport test for a constant sheaf. Compute the characteristic set from the order filtration as an independent check. Write down the real-cotangent identification explicitly; do not compare a complex cotangent set and a real one without that map.

Next compare a coherent module with a holonomic one. Determine which dimension condition on the characteristic variety is added by holonomicity, and which further result relates it to constructible solutions. Involutivity by itself does not impose the half-dimension condition: a whole symplectic manifold is involutive and has twice its Lagrangian dimension.

There is a second, distinct project at the microlocal level. On a complex manifold $X$, Proposition 10.6.2 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) gives canonical morphisms $\mathcal E_X^{\mathbb R}\to\mu hom(\mathcal O_X,\mathcal O_X)$ and $(\mathcal E_X^{\mathbb R})^a\to\mu hom(\Omega_X,\Omega_X)$, and Corollary 10.6.3 gives, for $p\in T^*X$, a natural morphism of rings $\mathcal E^{\mathbb R}_{X,p}\to\operatorname{Hom}_{D^+(X;p)}(\mathcal O_X,\mathcal O_X)$. Determine whether these morphisms yield actions on the cohomology sheaves of $\mu hom(F,\mathcal O_X)$ for every $F\in D^b(\mathbb C_X)$. The holomorphic top-form coefficient object $\Omega_X$ carries right actions, whereas $\mathcal O_X$ gives left actions. Identify the acting sheaf $\mathcal E_X^{\mathbb R}$, the composition law producing the action, and the module side before comparing it with [SH02-MH-COMPOSITION](../../sheaf-proof-readings/SH02-microlocal-hom.html#SH02-MH-COMPOSITION). Distinguish such a cohomology-level structure from placing the entire complex in a derived category of $\mathcal E_X^{\mathbb R}$-modules. A successful comparison must respect that distinction.

## SH02-RR-HYPERBOLIC — Separate propagation from the analytic interpretation

Use [SH02-LFI-ESCAPE](../../sheaf-proof-readings/SH02-local-forms-and-inverse-image.html#SH02-LFI-ESCAPE), [SH02-LFI-INVERSE](../../sheaf-proof-readings/SH02-local-forms-and-inverse-image.html#SH02-LFI-INVERSE), and [SH02-INV-MICROLOCAL-FLOW](../involutivity.html#sh02-inv-microlocal-flow-sections-between-opposite-sides-of-a-level-set). There are two different questions: whether restriction across a map preserves a microlocal object, and whether a section propagates along a Hamiltonian trajectory.

For the second question let $U\subset T^*X$ be open, $\phi\in C^2(U;\mathbb R)$, and suppose

$$
\operatorname{SS}(F)\cap U\subset\{\phi\geq0\},
\qquad
\operatorname{SS}(G)\cap U\subset\{\phi\leq0\}.
$$

The course result concerns each section of $\mathcal H^j\mu hom(G,F)$ and positive maximal Hamiltonian time inside $U$. Interchanging $F$ and $G$ changes the ordered cone and the propagation direction. At a critical point of $\phi$ the trajectory is stationary; no global completeness of the Hamiltonian flow is assumed.

**Project.** Choose a map of pairs $(Y,N)\to(X,M)$ and a conormal region on which to compare microlocalizations. Verify separately the escaping-covector exclusion, the noncharacteristic condition on the induced conormal map, and the ambient-lift condition in SH02-LFI-ESCAPE. Produce the two inverse-image comparisons with their relative orientation factors, and show where proper support becomes ordinary support. Then choose a Hamiltonian separating the two relevant microsupports and determine which ordered microlocal Hom can propagate forward.

To interpret the result for differential equations, supply the solution-complex identification from the preceding route and the precise microhyperbolic result required from §10.5 of *Microlocal study of sheaves*, in particular the setting of Theorems 10.5.1 and 10.5.4. For Theorem 10.5.4, start with a real analytic map of real analytic manifolds, a holomorphic extension between chosen complexifications, a coherent left $\mathcal D_X$-module, and an open region in the source conormal bundle. Check ordinary noncharacteristicity and the two additional normal-cone and ambient-lift conditions in that theorem; its full cotangent differential and its restricted conormal differential have distinct roles. Theorem 10.5.1 uses the normal cone $C_{T_M^*X}(\operatorname{char}(\mathcal M))$ to control microfunction solutions. Thus avoiding only the original characteristic set is not the microhyperbolic test. The function, hyperfunction, or microfunction coefficient object must also be specified.

A related product project starts from the [noncharacteristic tensor and Hom estimates](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-DIAGONAL) and the [asymptotic estimates](../../sheaf-proof-readings/SH02-characteristic-estimates.html#SH02-CHE-004). Compare $k_{\{x\geq0\}}$ and $k_{\{x\leq0\}}$ on the line: their tensor product exists and is $k_{\{0\}}$, although their boundary directions violate the no-cancellation hypothesis. Then investigate a proposed multiplication of distributions. State its wavefront convention and its exact analytic multiplication theorem separately. Sheaf tensor product, smooth wavefront, analytic wavefront, and the microsupport of an associated solution sheaf are different inputs until an explicit comparison connects them.

## SH02-RR-SHEAR — A transported conormal and an exact viscous wave

The [cotangent correspondence](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-COTANGENT) gives an explicit connection to fluid transport. Work on $[0,\infty)\times\mathbb R^3$ in Cartesian coordinates $x=(x_1,x_2,x_3)$, with viscosity $\nu>0$. Choose real constants $\gamma,a,b,c$ with $a\ne0$, and set

$$
\begin{aligned}
B(x)&=(\gamma x_2,0,0),&
\Phi_t(y)&=(y_1+\gamma ty_2,y_2,y_3),\\
\xi(t)&=(a,b-\gamma at,0),&
\phi(t,x)&=\xi(t)\cdot x,\\
J(t)&=(a^2+b^2)t-\gamma abt^2+\frac{\gamma^2a^2}{3}t^3,&
w(t,x)&=c e^{-\nu J(t)}\cos\phi(t,x)\,e_3.
\end{aligned}
\tag{RRS1}
$$

Here $\Phi_t$ is the flow of the shear $B$. The velocity $u=B+w$, with pressure $p=0$ and force $f=0$, is an exact smooth solution of

$$
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad\operatorname{div}u=0.
\tag{RRS2}
$$

**Proof.** Both summands are divergence-free. Since $w$ points along $e_3$ and has no $x_3$ dependence, $(w\cdot\nabla)B=(w\cdot\nabla)w=0$. Also $(B\cdot\nabla)B=\Delta B=0$. Finally,

$$
(\partial_t+B\cdot\nabla)\phi=0,
\qquad J'(t)=|\xi(t)|^2,
\qquad\Delta w=-|\xi(t)|^2w.
\tag{RRS3}
$$

Thus $(\partial_t+B\cdot\nabla)w=-\nu|\xi(t)|^2w$ cancels $-\nu\Delta w$. This proves the nonlinear equation, including its pressure and divergence constraints. $\square$

The changing spatial frequency is exactly the cotangent image of the initial normal:

$$
\xi(t)=(D\Phi_t)^{-T}(a,b,0),\qquad
\kappa_t(y,\eta)=\bigl(\Phi_t(y),(D\Phi_t)^{-T}\eta\bigr).
\tag{RRS4}
$$

The inverse transpose follows by differentiating $\phi(t,\Phi_t(y))=ay_1+by_2$. It preserves the tautological one-form because $((D\Phi_t)^{-T}\eta)\cdot D\Phi_t\,dy=\eta\cdot dy$.

For the sheaf calculation retain the standing coefficient ring and assume $k\ne0$. Let $H_t=\{x:\phi(t,x)=0\}$ and extend the constant sheaf $k$ from this closed plane by zero. The diffeomorphism identifies sections on the two planes, so $(\Phi_t)_*k_{H_0}\simeq k_{H_t}$. The [closed-embedding equality](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-PROPER-PUSH), applied to the constant sheaf on $H_t$, gives

$$
\operatorname{SS}(k_{H_t})=N^*H_t
=\{(x;s\xi(t)):x\in H_t,\ s\in\mathbb R\}
=\kappa_t(N^*H_0).
\tag{RRS5}
$$

This includes zero covectors over the plane and both normal directions. No antipodal map or cohomological shift occurs.

The same normal controls the viscous decay. Completing the square yields

$$
J(t)=a^2t+t\left(b-\frac{\gamma at}{2}\right)^2+
\frac{\gamma^2a^2}{12}t^3,
\qquad
\|w(t)\|_\infty\le |c|
e^{-\nu a^2t-\nu\gamma^2a^2t^3/12}.
\tag{RRS6}
$$

When $\gamma\ne0$, the normal's norm grows linearly as $t\to\infty$, giving cubic-in-time damping of this mode. The normal need not grow monotonically at earlier times. The nontrivial solution has infinite kinetic energy on $\mathbb R^3$ and persists smoothly for all $t\ge0$.

**Project.** On open spacetime $t>0$, compute the conormal to $\phi=0$. It is $s(-\gamma ax_2,\xi(t))$, and hence lies in the zero set of the transport symbol $\tau+B\cdot\xi$. At a nonzero spatial frequency the viscous symbol $i(\tau+B\cdot\xi)+\nu|\xi|^2$ has positive real part. Explain why the phase-plane sheaf in (RRS5) has not thereby been identified with a sheaf of viscous solutions. In particular, the actual function $w$ is smooth and has no nonzero distributional wavefront covectors.

**Research context.** The phase and polarization discussion in OpenAI's [*Finite Time Blowup for Navier-Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Sections 3.3 and 7.1, prompted this independently written calculation. Its claimed finite-energy blowup theorem is not used here. Related forced Euler work is attributed to Levent Alpöge and Tristan Buckmaster in [Buckmaster's primary statement](https://cims.nyu.edu/~tristanb/statement.pdf), which credits the preceding program to Diego Córdoba and Luis Martínez-Zoroa. These antecedents do not supply a theorem equating the phase sheaf with a PDE solution object.

## SH02-RR-DELIVERABLE — Make the next theorem assessable

For one chosen route, prepare a short mathematical note with four parts:

1. Specify the objects, coefficient category, bounds, ambient geometry, and support conditions.
2. Draw the comparison with its actual arrows. Name the units, counits, restriction maps, and orientation identifications that define them.
3. Work through a local model and an exceptional case, such as an open endpoint, a zero vector, a rank change, or a stationary trajectory.
4. State the exact additional theorem needed for the external step, its source and the conclusion it would add.

The local model tests a proposed theorem; it does not prove its full generality. Within SH-02, Fourier normalization and the exact remaining trace comparison retain their owning proof obligations. The general fibre-product Hom comparison is constructed in [SH02-MHPC-FIBRE-PRODUCT](../../sheaf-proof-readings/SH02-microlocal-hom-product-comparison.html#SH02-MHPC-FIBRE-PRODUCT), conditional on its named operation and Fourier prerequisites. A route that uses one of those comparisons must retain that dependency rather than selecting an arbitrary isomorphism with the same endpoints.

## SH02-RR-REFERENCES — Antecedents and further reading

The primary reference for these routes is M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), with the survey of P. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016). Its Chapters 1–6 cover the present course's mathematical targets; Chapters 7–9 lead to the topics of *Constructible and perverse sheaves*.

This lesson introduces no imported theorem from algebraic Fourier theory, etale sheaves, distribution products, or a derived category of microdifferential modules. An exact comparison in one of those settings would need an additional source and proof package. The license grant covers this original lesson, not the cited books.
