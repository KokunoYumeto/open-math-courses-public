# Homogeneous functions, Fourier transformation and specialization

Euler integration can retain a direction while discarding the distance along it. That is the setting of the Fourier transform studied here. Its inputs are homogeneous constructible functions on a vector bundle; its kernel is a closed pairing halfspace. Specialization first magnifies a function near a submanifold, then this Fourier transform turns normal directions into conormal directions. A pair of tangent branches will show why the magnified function contains more information than its set of limiting directions.

This lesson develops homogeneous constructible functions, their Fourier transform and specialization, following the calculus of P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf) (1991). Read Constructible functions and Euler integration for the function sheaf, its Grothendieck correspondence, local duality and support conditions. The prerequisite lessons are transport along a scaling action, Fourier kernels as radial averaging, and reading a sheaf at the normal scale. Their bounded constructions are explained where used below. Weak constructibility under sheaf operations and Perfect operations and finite microlocal coefficients prove the constructibility and finiteness required for those constructions.

## The coefficient and geometric setting

Work over a field \(k\) of characteristic zero. Manifolds and bundles are real analytic, Hausdorff, countable at infinity and of uniformly finite dimension. The input category \(D^b_{\mathrm{rc}}(X;k)\) consists of globally bounded complexes with finite dimensional, constructible stalk cohomology. No uniform bound on all stalk ranks is imposed. Write
\[
\chi F(x)=\sum_q(-1)^q\dim_k H^q(F)_x,
\qquad CF(X)=\{\text{integer valued constructible functions on }X\}.
\qquad\text{(1)}
\]
The level partition of a function in \(CF(X)\) is locally finite and subanalytic. Its closed support is the closure of its nonzero locus. Ordinary inverse image of functions is composition. The local duality operation \(D_X\) and exceptional inverse image are those of the preceding lesson:
\[
f^!\phi=D_Yf^*D_X\phi\quad(f:Y\longrightarrow X),
\qquad D_X\chi F=\chi(D_XF).
\qquad\text{(2)}
\]
In particular \(i^!\phi\) is a costalk operation when \(i\) is an embedding. It usually differs from \(i^*\phi\).

Let \(\tau:E\to Z\) have constant real rank \(n\), let \(i:Z\hookrightarrow E\) be its zero section, and write \(E^\times=E\setminus i(Z)\), with inclusion \(j\). A function is **homogeneous** if
\[
\phi(\lambda v)=\phi(v)\quad(\lambda>0).
\qquad\text{(3)}
\]
Denote this group by \(CF_{\mathbb R_{>0}}(E)\). Conic complexes have locally constant cohomology along positive scalar orbits. The SH-02 transport theorem supplies a natural action isomorphism, including the zero section, normalized at scalar one and satisfying the cocycle identity. Restriction only to the punctured bundle would leave the zero coefficient undetermined.

## Separate the zero section from the positive rays

The positive ray quotient \(S_E=E^\times/\mathbb R_{>0}\) is an analytic manifold. In a bundle chart it is the product of the base with the unit sphere. Normalizing a nonzero vector gives analytic local charts; transitions normalize the analytic linear bundle transitions and are analytic. This construction needs no choice of a global analytic metric. Let \(\gamma:E^\times\to S_E\) be the quotient.

There is an equivalence
\[
\gamma^{-1}:D^b_{\mathrm{rc}}(S_E;k)
 \ \simeq\ D^b_{\mathrm{rc},\mathbb R_{>0}}(E^\times;k),
\qquad\text{inverse }R\gamma_* .
\qquad\text{(4)}
\]
To prove it, work in a ray chart \(S\times\mathbb R_{>0}\). Normalized transport identifies a conic complex there with the pullback of its restriction at radius one. Ordinary cohomology of the positive parameter is \(k\) in degree zero and has no higher terms. The contractible parameter descent theorem therefore identifies both the unit and counit in (4) with isomorphisms. These are the actual adjunction maps, so they agree on chart overlaps. Constructibility is preserved: restrictions to radius one give analytic local sections, while pullback adds a product interval to a subanalytic stratification. Bounds are unchanged. Notice that \(R\gamma_!\gamma^{-1}G\simeq G[-1]\), since compactly supported cohomology of the positive ray is \(k[-1]\). The inverse in (4) is the ordinary image.

Let \(K_{\mathrm{con}}(E)\) be the Grothendieck group of the conic constructible bounded category. Define
\[
\begin{aligned}
\alpha[A]&=[i_*A],&
\beta[F]&=[R\gamma_*j^{-1}F],\\
\alpha''[F]&=[i^{-1}F],&
\beta''[G]&=[j_!\gamma^{-1}G].
\end{aligned}
\qquad\text{(5)}
\]
All four functors have the stated constructible bounded domains. The open–closed triangle
\[
j_!j^{-1}F\longrightarrow F\longrightarrow i_*i^{-1}F
\xrightarrow{+1}
\qquad\text{(6)}
\]
and (4) give
\[
1=\beta''\beta+\alpha\alpha'',\quad
\beta\beta''=1,\quad\alpha''\alpha=1,\quad
\beta\alpha=0,\quad\alpha''\beta''=0.
\qquad\text{(7)}
\]
Thus the sequence
\[
0\longrightarrow K_0(Z)\xrightarrow{\alpha}
K_{\mathrm{con}}(E)\xrightarrow{\beta}K_0(S_E)\longrightarrow0
\qquad\text{(8)}
\]
is split exact. Rank zero has empty ray quotient and reduces to \(K_0(E)=K_0(Z)\).

For functions, a homogeneous function is precisely the choice of its value on the zero section and a constructible function on \(S_E\), extended along the rays. The angular function is constructible by restriction to the analytic local sections of \(\gamma\); the converse follows from the local product charts. Extending the angular part by zero at the zero section remains constructible. Locally near a base point the sphere is compact, so only finitely many angular values occur. Subanalytic conic subsets extend across the origin by their radial cone in a relatively compact chart. This is the same local conic subanalytic geometry used by the conic extension theorem.

Consequently the function sequence corresponding to (8) is split exact. The ordinary Grothendieck theorem already proved in the preceding lesson identifies the groups at \(Z\) and \(S_E\). Its Euler map commutes with (5), because ray descent uses ordinary interval cohomology of Euler value one. The splitting (7) now proves
\[
\chi:K_{\mathrm{con}}(E)\xrightarrow{\ \sim\ }
CF_{\mathbb R_{>0}}(E).
\qquad\text{(9)}
\]
This supplies both surjectivity and injectivity. Explicitly, realize the zero and angular functions by bounded complexes \(A,B\) using the preceding lesson, and take \(i_*A\oplus j_!\gamma^{-1}B\). Conversely, a zero Euler class has zero zero-section and angular classes and hence vanishes by (7). Locally infinite stratifications are allowed: each realization is an actual sheaf complex and (6) is one triangle. No infinite sum of Grothendieck classes enters the proof.

## Ordinary and supported radial projection

Conic contraction supplies natural comparisons
\[
R\tau_*F\simeq i^{-1}F,\qquad R\tau_!F\simeq i^!F.
\qquad\text{(10)}
\]
The ordinary comparison restricts sections to a germ at zero. The supported comparison includes zero-section support into support proper over the base. Its proof compares the localization triangles for the zero section and a closed disk, then uses disk supports cofinal among proper supports after shrinking the base. Conicity makes the complementary radial restrictions isomorphisms. This gives an exact written proof even though \(\tau\) is generally nonproper.

We therefore define the two radial function images by
\[
\tau_*\phi=i^*\phi,\qquad \tau_!\phi=i^!\phi.
\qquad\text{(11)}
\]
These operations are defined for all homogeneous constructible functions. They extend the ordinary support-proper Euler image in this particular conic setting.

Choose an analytic norm in a local bundle trivialization and let \(B_\varepsilon\) be its open fibre ball. Then
\[
\begin{aligned}
\tau_!\phi&=\tau_!(\phi\,1_{B_\varepsilon}),\\
\tau_*\phi&=\tau_!(\phi\,1_{\overline B_\varepsilon}).
\end{aligned}
\qquad\text{(12)}
\]
The right sides are the usual Euler images: their closed coefficient supports are contained in the closed disk bundle, proper over the local base. To prove the first equality, realize \(\phi=\chi F\) conically by (9). At each fibre, the open-ball compact-section comparison identifies \(R\Gamma_c(B_\varepsilon;F)\) with the costalk at zero. The radius can be changed using scalar transport; all radii give the same costalk. Proper-support base change and (10) give the first equality. For the second, the closed-ball ordinary-section comparison identifies \(R\Gamma(\overline B_\varepsilon;F)\) with the ordinary zero stalk. The closed ball is compact, so this is also its compact-section complex; base change gives the second equality. These are the open and closed ball comparisons proved in Small balls, central fibres and supported cohomology, now applied to a conic complex.

Thus (12) is independent of radius and of the local analytic norm, since each side equals the intrinsic operation in (11). The local statements glue. For example,
\[
\tau_!1_E=(-1)^n1_Z,\qquad \tau_*1_E=1_Z.
\qquad\text{(13)}
\]
An open \(n\)-ball has compact Euler value \((-1)^n\), while a closed ball has value one. Replacing the ball in either line of (12) by the other changes the answer.

## The halfspace kernel and its inverse

Let \(\pi:E^*\to Z\) be the dual bundle. On \(E\times_ZE^*\) write \(p,q\) for the projections to \(E,E^*\), and put
\[
N=\{(v,\eta):\langle v,\eta\rangle\leq0\}.
\]
Let \(i_E:E^*\hookrightarrow E\times_ZE^*\) set \(v=0\). The function \((p^*\phi)1_N\) is conic in the \(v\) variable, so the supported radial operation of (11) is available. Define
\[
\widehat\phi=q_!\bigl((p^*\phi)1_N\bigr)
            =i_E^!\bigl((p^*\phi)1_N\bigr).
\qquad\text{(14)}
\]
Here \(q_!\) is this conic operation, not an unsupported extension of the general proper-support function definition to all nonproper maps.

For a conic representative \(F\) define its sheaf transform
\[
T_EF=Rq_!\bigl(p^{-1}F\otimes k_N\bigr).
\qquad\text{(15)}
\]
The conic Grothendieck theorem and perfect constructible operation theorem give
\[
\chi(T_EF)=\widehat{\chi F}.
\qquad\text{(16)}
\]
Indeed the kernel complex is conic in \(v\); (10) turns its image into the actual exceptional zero restriction. Equations (1)–(2), tensor multiplicativity and (14) give (16). This also proves that the output is a constructible function. Dilation of \(\eta\) preserves \(N\), so it is homogeneous in the dual variable. All complexes used in this argument are bounded and have finite stalks; the conic compact cut and constructibility proofs supply those assertions.

Let \(a\) be fibrewise negation. Define the inverse-direction operation by
\[
\check\psi=(-1)^n a^*\widehat\psi\quad
(\psi\in CF_{\mathbb R_{>0}}(E^*)).
\qquad\text{(17)}
\]
In this formula the hat transforms from \(E^*\) to \(E^{**}=E\). One can also apply the same formula to functions on \(E\), obtaining the inverse of the dual-to-primal transform.

The actual sheaf inversion theorem gives
\[
T_{E^*}T_EF\simeq
a^{-1}F\otimes\tau^{-1}O_E[-n],
\qquad\text{(18)}
\]
where \(O_E\) is the rank-one orientation local system. Its stalk Euler value is one, even on a nonorientable bundle. Applying (16) twice gives
\[
\widehat{\widehat\phi}=(-1)^na^*\phi,\qquad
\check{\widehat\phi}=\phi,\qquad
\widehat{\check\psi}=\psi.
\qquad\text{(19)}
\]
For the last equality use (18) on \(E^*\) and the fact that simultaneous negation of both pairing variables preserves \(N\), so the transform commutes with the antipode.

The proof underlying (18) is the written SH-02 radial kernel argument, not a citation to a missing external proof. The right adjoint has the positive-halfspace proper kernel and orientation complex \(O_E[n]\). Composing it with (15) gives the intersection of one nonpositive and one nonnegative halfspace in the intermediate dual variable. A localization triangle for the strict halfspace constructs its kernel as the positive scalar relation \(v=s w\), \(s>0\), with shift \([1]\). Compact integration along \(s>0\) gives \(k[-1]\) and cancels that shift. Normalized conic transport then identifies the resulting functor with the identity, including its gluing at zero. Expressing this inverse kernel using the same negative convention adds the antipode and \(O_E[n]\); solving for the same-sign square gives (18). The full halfspace triangle, maps and zero-section argument are supplied in the linked Fourier prerequisite.

As immediate tests,
\[
\widehat{1_{i(Z)}}=1_{E^*},\qquad
\widehat{1_E}=(-1)^n1_{0_{E^*}}.
\qquad\text{(20)}
\]
The first fibre is a point for every \(\eta\). For the second, \(\eta=0\) gives the open-ball Euler value \((-1)^n\); a nonzero \(\eta\) gives a closed halfspace cut through an open ball, whose Euler value is zero. This is compatible with (19).

## Base change and a finite fibre calculation

Let \(b:Z'\to Z\) be analytic and form \(E'=Z'\times_ZE\), with induced maps \(b_E,b_{E^*}\). Then
\[
\widehat{b_E^*\phi}=b_{E^*}^*\widehat\phi.
\qquad\text{(21)}
\]
To prove this, pull back the product \(E\times_ZE^*\). Its two projection squares are cartesian, and its negative pairing subset pulls back to the corresponding subset on \(E'\). Proper-support base change for the sheaf \(Rq_!\), followed by exact inverse image of the kernel, identifies \(b_{E^*}^{-1}T_EF\) with \(T_{E'}b_E^{-1}F\). Taking (16) proves (21). The map is the actual base-change map; it is compatible with successive pullbacks by cartesian pasting. Properness of \(b\) is unnecessary. This is the first base-change identity proved in Moving Fourier kernels across maps and products.

In particular the transform can be calculated on each fibre. For a vector space \(E\), (12)–(14) give the finite integral
\[
\widehat\phi(\eta)=
\int_E\phi(v)\,
1_{\{|v|<\varepsilon\}}\,
1_{\{\langle v,\eta\rangle\leq0\}}\,d\chi .
\qquad\text{(22)}
\]
Its closed support lies in a compact closed ball. Thus the preceding lesson's Euler integral applies. Conicity permits any positive radius, although the small-ball proof alone would already suffice for a sufficiently small radius. The norm is analytic in a linear chart and the result is independent of it by (14). The pairing boundary is included; the ball boundary is excluded.

## Open and closed convex cones

Let \(E\) now be an \(n\)-dimensional vector space. For a cone \(C\) put
\[
C^\circ=\{\eta:\langle v,\eta\rangle\geq0
                  \text{ for every }v\in C\}.
\]
Suppose \(U\) is a nonempty open convex subanalytic cone in \(E\). Suppose \(\gamma\) is a closed convex subanalytic cone containing zero and no line. It can have dimension less than \(n\). Then
\[
\widehat{1_U}=(-1)^n1_{-U^\circ},
\qquad
\widehat{1_\gamma}=1_{\operatorname{Int}(\gamma^\circ)}.
\qquad\text{(23)}
\]

Here is a direct Euler proof. For the open case let \(V=U\cap B_\varepsilon\). This is nonempty open convex in \(E\), so its compact Euler value is \((-1)^n\). If \(\eta\in-U^\circ\), the nonpositive halfspace contains all of \(U\), and (22) gives that value. Otherwise \(V\cap\{\langle v,\eta\rangle>0\}\) is nonempty open convex of the same dimension. The orientation trace identifies its compact-section extension into \(V\) with an isomorphism in top degree. The localization triangle consequently gives zero for the complementary closed halfspace cut. This proves the first formula, including its polar boundary. For \(U=\varnothing\) the transform is zero.

For the closed case the intersection
\[
C=\gamma\cap\{\langle v,\eta\rangle\leq0\}
\]
is a closed pointed cone. It is \(\{0\}\) precisely when \(\eta\) is strictly positive on all nonzero vectors of \(\gamma\), equivalently when \(\eta\in\operatorname{Int}(\gamma^\circ)\). The equivalence follows by compactness of \(\gamma\cap S^{n-1}\): strict positivity has a positive minimum on that set; failure of strict positivity permits an arbitrarily small perturbation of \(\eta\) violating the polar inequality.

If \(C\ne\{0\}\), choose a linear functional strictly positive on its nonzero vectors. Such a functional exists by finite dimensional convex separation for a closed pointed cone. The intersection \(C\cap S^{n-1}\) is homeomorphic, by radial normalization, to the compact convex level-one section for this functional. It has Euler value one. The closed truncated cone \(C\cap\overline B_\varepsilon\) contracts radially to its vertex and also has value one. Removing the spherical boundary gives
\[
\chi_c(C\cap B_\varepsilon)=1-1=0.
\qquad\text{(24)}
\]
If \(C=\{0\}\) its value is one. This proves the second formula. For \(\gamma=\{0\}\) the polar is all \(E^*\) and the same answer holds. In rank zero both spaces are points and the formulas reduce to ordinary identity. A cone containing a line is outside this second statement: a vector subspace has nonzero top compact cohomology, so the vanishing argument would fail.

## Specialization is a boundary measurement

Let \(M\hookrightarrow X\) be a closed analytic submanifold and let \(D_MX\) be its normal deformation. Write
\[
\Omega=\{t>0\}\xrightarrow{j}D_MX,\quad
s:T_MX\hookrightarrow D_MX,\quad p:D_MX\to X.
\]
In coordinates \(x=(x',x'')\) with \(M=\{x'=0\}\), deformation coordinates are \((v,x'',t)\) and \(p(v,x'',t)=(tv,x'')\). On the positive chamber \(r=p|_\Omega\) is the product projection \(X\times\mathbb R_{>0}\to X\). Define
\[
\nu_M\phi=-s^!\bigl((p^*\phi)1_\Omega\bigr),
\qquad
\mu_M\phi=\widehat{\nu_M\phi}.
\qquad\text{(25)}
\]
These are homogeneous constructible functions on \(T_MX\) and \(T_M^*X\), respectively.

We prove the sign and all representative comparisons. For \(F\in D^b_{\mathrm{rc}}(X;k)\) let \(H=r^{-1}F\) and put
\[
\nu_MF=s^{-1}Rj_*H.
\]
The localization triangle for \(j_!H\) is
\[
R\Gamma_{D_MX\setminus\Omega}(j_!H)
\longrightarrow j_!H\longrightarrow Rj_*H\xrightarrow{+1}.
\qquad\text{(26)}
\]
The first term vanishes on the positive and negative chambers; its support lies on the central fibre. It is therefore \(s_*s^!j_!H\). Ordinary restriction to that fibre kills the middle term, yielding the actual connecting isomorphism
\[
\nu_MF\simeq s^!j_!H[1].
\qquad\text{(27)}
\]
The shift \([1]\) changes Euler value by a minus sign. Tensor and inverse image give \(\chi(j_!H)=(p^*\chi F)1_\Omega\), and (2) now proves
\[
\chi(\nu_MF)=\nu_M(\chi F),\qquad
\chi(\mu_MF)=\mu_M(\chi F).
\qquad\text{(28)}
\]
This derivation agrees with the positive-parameter boundary comparison in SH-02. It uses ordinary \(r^{-1}\) in \(H\); using \(r^!=r^{-1}[1]\) instead would move the same shift into that input.

The deformation dilation \((v,x'',t)\mapsto(\lambda v,x'',t/\lambda)\) fixes \(p\), preserves \(\Omega\), and restricts to positive dilation on the central bundle. Naturality of the operations in (26) makes \(\nu_MF\) conic. The owned perfect-operation proof shows it is constructible, globally bounded and has finite stalks. Together with (9) and (16), this proves the asserted function domains in (25), their additivity and their dependence only on \(\phi\). These are local constructions along \(M\), so restriction to smaller analytic charts is compatible throughout.

Using \(s^!=D_{T_MX}s^*D_{D_MX}\), the coordinate expression is
\
(\nu_M\phi)(v,x'')=
-D_{T_MX}\!\left[
\left.D_{D_MX}
\bigl(\phi(tv,x'')\,1_{\{t>0\}}\bigr)\right|_{t=0}
\right.
\qquad\text{(29)}
\]
Both dualities are taken in their displayed ambient manifolds. Replacing them by duality only in the \(t\) variable would discard normal and tangential contributions. Equation (29) is simply (25) in deformation coordinates, so the construction is independent of the chart.

For any realization whose closed support is \(A\), neighborhoods outside \(\overline{r^{-1}A}\) give zero sections of \(Rj_*H\). Hence
\[
\operatorname{supp}\nu_M\phi\subset C_M(|\phi|),
\qquad\text{(30)}
\]
using the support-preserving realization in the preceding lesson. Equality and unit multiplicities do not follow.

## Two tangent branches retain two nearby components

In \(\mathbb R^2\) let
\[
A_1=\{(x,0):x\geq0\},\quad
A_2=\{(x,x^2):x\geq0\},\quad A=A_1\cup A_2,
\quad M=\{0\}.
\]
The two branches intersect just at the origin. Therefore
\[
1_A=1_{A_1}+1_{A_2}-1_{\{0\}}.
\qquad\text{(31)}
\]
Their normal cones at zero are both the closed positive horizontal ray \(C\). This follows directly by rescaling: on the second branch the normal coordinates satisfy \(v_y=t v_x^2\), \(v_x\geq0\), so every finite limit has \(v_y=0,v_x\geq0\), and every such vector is obtained.

We calculate specialization using actual chamber sections. Near a positive vector \((a,0)\), \(a>0\), the lifted first branch is \(v_y=0\), \(v_x\) in a small interval around \(a\), \(t>0\). The second is \(v_y=t v_x^2\) on the same parameter rectangle. For sufficiently small positive \(t\), both remain in any prescribed transverse neighborhood. Each branch is a contractible rectangle with constant coefficient, and their intersections are empty there. They give two copies of \(k\) in degree zero.

At the zero normal vector choose \(0\leq v_x<\delta\), \(0<t<\varepsilon\) with \(\varepsilon\delta^2\) smaller than the transverse neighborhood width. Each lifted branch again has a contractible parameter rectangle. The two rectangles meet exactly along \(v_x=0\), \(t>0\). For the constant sheaf on the union, the closed-union exact sequence is
\[
0\longrightarrow k_{\widetilde A}
\longrightarrow k_{\widetilde A_1}\oplus k_{\widetilde A_2}
\longrightarrow k_{\widetilde{\{0\}}}\longrightarrow0.
\qquad\text{(32)}
\]
The last map is the difference of the two restrictions. Chamber cohomology gives \(k\oplus k\to k\), surjective with diagonal kernel \(k\), and no higher cohomology. These boxes form cofinal normal-deformation neighborhoods; their restrictions preserve the constants and this difference map. Outside \(C\) a sufficiently small chamber box misses both branches.

Thus each branch separately specializes to \(1_C\), the intersection specializes to the zero-vector indicator, and additivity in (31) gives
\[
\nu_0(1_A)=2\,1_C-1_{\{0\}}.
\qquad\text{(33)}
\]
The value is two on the positive ray, one at its vertex, and zero elsewhere. The geometric normal cone alone is just \(C\); its indicator would miss the two approaching components.

## A homogeneous function survives its own normal rescaling

For the zero section of a vector bundle,
\[
\nu_Z\phi=\phi\qquad(\phi\in CF_{\mathbb R_{>0}}(E)).
\qquad\text{(34)}
\]
Use a conic representative from (9). The normal deformation is locally \(E\times\mathbb R\), with \(p(v,t)=tv\) on \(t>0\). Normalized conic transport identifies \(p^{-1}F\) on that chamber with the pullback of \(F\) from the \(v\) coordinate. Product interval descent makes the ordinary chamber image at \(t=0\) equal to \(F\); no compact integration along \(t\) is used. This is the specialization definition preceding (26). The transport and restriction maps glue over bundle charts, proving the sheaf comparison and then (34). In particular no extra rank sign occurs in specialization itself.

## Microlocal Hom at the level of functions

Let \(\Delta_X\subset X\times X\) be the diagonal and identify its conormal with \(T^*X\) by
\((x,x;\xi,-\xi)\mapsto(x;\xi)\). Define the bilinear function operation
\[
\mu\operatorname{hom}(\psi,\phi)
=\mu_{\Delta_X}(\phi\boxtimes D_X\psi).
\qquad\text{(35)}
\]
For constructible bounded \(G,F\), its actual sheaf counterpart is
\[
\mu\operatorname{hom}(G,F)
=\mu_{\Delta_X}
R\mathcal Hom(q_2^{-1}G,q_1^!F).
\qquad\text{(36)}
\]
The constructible external-Hom evaluation gives
\[
R\mathcal Hom(q_2^{-1}G,q_1^!F)
\simeq F\boxtimes D_XG.
\qquad\text{(37)}
\]
Its exact written provider is the constructible-factor external-Hom theorem in Finite local data and sheaf biduality. That theorem tests product neighborhoods, represents the compact-section system of \(G\) by a perfect complex, and applies finite-projective evaluation; the other input is allowed in \(D^+\). Here both are bounded constructible, so its hypotheses hold. Natural duality for specialization and microlocal Hom explains this evaluation and the diagonal convention.

Taking the Euler function of (37), applying (28) and then (16), proves
\[
\chi\bigl(\mu\operatorname{hom}(G,F)\bigr)
=\mu\operatorname{hom}(\chi G,\chi F).
\qquad\text{(38)}
\]
The exceptional projection \(q_1^!\) is essential to (37): its fibre dualizing complex supplies the ambient dimension shift. Ordinary Hom between two stalks would erase that factor and the boundary information used by specialization.

## Exercises with complete solutions

### Descent along a ray uses ordinary cohomology
*Difficulty: Introductory.*

For \(\gamma:(0,\infty)\to\{\mathrm{pt}\}\), calculate \(R\gamma_*k\) and \(R\gamma_!k\). Which induces the angular map in (5)?

**Solution.** The ray is contractible, so ordinary cohomology is \(k\) in degree zero. It is an oriented open one-manifold, so compact cohomology is \(k[-1]\). Their Euler values are \(1\) and \(-1\), respectively. The angular map uses \(R\gamma_*\), yielding value \(1\) and no shift. The proper image would negate the angular function.

### A constant function tests the cutoff boundary
*Difficulty: Introductory.*

On \(\mathbb R^2\), calculate \(\tau_*1\), \(\tau_!1\), and both integrals in (12). Repeat in dimension one.

**Solution.** In dimension two ordinary zero restriction is \(1\), and exceptional zero restriction of the constant coefficient has shift \([-2]\), hence also Euler value \(1\). The closed disk has Euler value \(1\); the open disk has value \((-1)^2=1\). This particular dimension conceals the distinction. In dimension one the closed interval still has value \(1\), but the open interval has value \(-1\). Thus \(\tau_*1=1\) and \(\tau_!1=-1\). Even when the numbers agree, the two corresponding complexes have different degrees.

### Fourier transformation on the four one-dimensional rays
*Difficulty: Intermediate.*

For the nonpositive pairing on \(\mathbb R\times\mathbb R^*\), transform the indicators of \((0,\infty)\), \([0,\infty)\), \((-\infty,0)\), and \((-\infty,0]\). Check the same-sign square.

**Solution.** Formula (23) gives, in that order,
\[
-1_{(-\infty,0]},\quad 1_{(0,\infty)},\quad
-1_{[0,\infty)},\quad 1_{(-\infty,0)}.
\]
For example the polar of the open positive ray is the closed positive dual ray, and its negative is the closed negative ray; the coefficient is \((-1)^1=-1\). Transforming \([0,\infty)\) twice gives \(-1_{(-\infty,0]}\), which is \(-a^*1_{[0,\infty)}\). Transforming the open positive ray twice similarly gives \(-1_{(-\infty,0)}\). The negative rays follow by antipodal symmetry. Thus the endpoints and sign agree with (19).

### A lower dimensional cone still has an open polar locus
*Difficulty: Intermediate.*

In \(\mathbb R^2\) let \(\gamma=\{(x,0):x\geq0\}\). Compute its transform and the value at a dual vector \((0,b)\).

**Solution.** Its polar is \(\{(\alpha,\beta):\alpha\geq0\}\), whose interior is \(\alpha>0\). Hence \(\widehat{1_\gamma}=1_{\{\alpha>0\}}\). At \((0,b)\) the pairing is zero on the whole ray. The truncated intersection is a half-open segment \([0,\varepsilon)\), with Euler value \(1-1=0\). The zero answer at the polar boundary is necessary even though the cone has ambient codimension one.

### Angular monodromy disappears only after taking the Euler function
*Difficulty: Advanced.*

On \(E=\mathbb R^2\), take a rank-one local system \(L\) on the ray circle \(S^1\), with monodromy \(-1\), and put \(F=j_!\gamma^{-1}L\). Find \(\chi F\) and \(\chi(T_EF)\). Does this determine \(T_EF\) as an object?

**Solution.** Every nonzero stalk has rank one and the zero stalk is zero. Thus \(\chi F=1_E-1_{\{0\}}\). By (20) and linearity,
\[
\chi(T_EF)=1_{\{0\}}-1_{E^*}.
\]
It is zero at the dual origin and \(-1\) elsewhere. This determines its Grothendieck class through (9), but not the object. The original \(F\) differs from the angular constant coefficient: their restrictions have different monodromy. The Fourier functor is an equivalence, so their transforms differ as objects too. Local Euler values discard that distinction.

### Pulling a bundle back adds no Fourier sign
*Difficulty: Intermediate.*

Let \(E\) be a possibly nonorientable real rank-three bundle and \(b:Z'\to Z\) an analytic map. Show that the pullback of its constant function transform is the transform of its pulled-back constant function. Identify the coefficient.

**Solution.** Both are \(-1_{0_{E'^*}}\) by (20), since the rank is three. Equation (21) proves equality for every homogeneous function, not just this test. Nonorientability changes the orientation local system in (18), but its stalk rank is one. Its Euler coefficient is consequently unchanged. The rank is also unchanged by base pullback; no dimension of \(Z'\) enters the sign.

### The specialization minus sign is a boundary shift
*Difficulty: Intermediate.*

Specialize the constant function on \(X=\mathbb R\) along \(M=\{0\}\), directly using (25). Then microlocalize it.

**Solution.** In the deformation plane the chamber function is \(1_{\{t>0\}}\). Its central ordinary restriction is zero, but the exceptional central restriction has Euler value \(-1\): (27) identifies it with the constant normal coefficient shifted by \([-1]\). The outer minus in (25) gives \(\nu_0(1_{\mathbb R})=1_{\mathbb R_v}\). Its one-dimensional Fourier transform is \(-1_{\{0\}}\) by (20), so \(\mu_0(1_{\mathbb R})=-1_{\{0\}}\). Omitting the boundary minus would reverse this result.

### Magnification distinguishes one branch from two
*Difficulty: Advanced.*

For \(A\) in (31), compute the values of \(\nu_0(1_A)\) at the origin, on the positive horizontal ray, and off that ray. Then compute \(\mu_0(1_A)\) on the dual plane.

**Solution.** The chamber rectangles and difference map in (32) give values \(1,2,0\), respectively. Equation (33) gives the whole function. Write \((\alpha,\beta)\) for the dual coordinates. By (23) and (20) in ambient dimension two,
\[
\mu_0(1_A)=2\,1_{\{\alpha>0\}}-1_{\mathbb R^{2*}}.
\]
Its value is \(1\) when \(\alpha>0\), and \(-1\) when \(\alpha\leq0\), including the origin. The subtraction of the vertex before Fourier transformation becomes subtraction of the constant function afterwards.

### A homogeneous half-ray needs no specialization correction
*Difficulty: Introductory.*

Let \(\phi=3\,1_{(0,\infty)}-2\,1_{\{0\}}\) on a normal line. Specialize along its zero section and then apply the Fourier transform.

**Solution.** The function is homogeneous, so (34) gives \(\nu_0\phi=\phi\). The ray calculation and (20) then give
\[
\mu_0\phi=-3\,1_{(-\infty,0]}-2\,1_{\mathbb R_\eta}.
\]
Here \(\mathbb R_\eta\) is the entire dual line, including zero. Thus the value is \(-5\) on the closed negative dual ray and \(-2\) on the positive ray. This computation introduces no normal-rank factor in specialization; its sign comes from Fourier integration.

### An exceptional projection fixes microlocal Hom's coefficient
*Difficulty: Advanced.*

For \(X=\mathbb R^m\), calculate \(\mu\operatorname{hom}(1_X,1_X)\). Explain why replacing \(q_1^!\) by \(q_1^{-1}\) in (36) gives the wrong coefficient when \(m\) is odd.

**Solution.** Duality gives \(D_X1_X=(-1)^m1_X\). Thus the function in (35) before diagonal specialization is \((-1)^m1_{X^2}\). It remains constant after specialization; Fourier transformation in the rank-\(m\) normal bundle contributes another factor \((-1)^m\) and concentrates it on the zero covectors. The product is \(1_{0_X}\). At the sheaf level \(q_1^!k_X\) contains the fibre orientation and shift \([m]\). Normal Fourier transformation has the matching orientation and shift \([-m]\), so the traces cancel. With the ordinary projection the first factor is absent and the result instead has Euler value \((-1)^m1_{0_X}\), incorrect for odd \(m\).

## References

- P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), J. Pure Appl. Algebra 72 (1991), 83–93: homogeneous functions and conic Grothendieck groups, Fourier transformation, specialization and microlocal Hom of constructible functions.
- Pierre Schapira, [Operations on constructible functions](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), *Journal of Pure and Applied Algebra* 72 (1991), 83–93, gives context for the sheaf-to-function calculus. No text or proof is imported from that copyrighted article.
- SH-02, conic descent, Fourier kernels, Fourier functoriality, specialization and cohomological biduality; the actual natural comparisons are used with their stated hypotheses.

Original prose, proofs as organized here, examples and solutions are dedicated to CC0. The integral characteristic-cycle correspondence and the remaining assigned chapters continue in the course.
