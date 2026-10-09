# Homogeneous functions, Fourier transformation and specialization

Euler integration can retain a direction while discarding the distance along it. That is the setting of the Fourier transform studied here. Its inputs are homogeneous constructible functions on a vector bundle; its kernel is a closed pairing halfspace. Specialization first magnifies a function near a submanifold, then this Fourier transform turns normal directions into conormal directions. A pair of tangent branches will show why the magnified function contains more information than its set of limiting directions.

*Original lesson text and complete solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

P. Schapira's [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), §§2–3, supplies the underlying Euler-function, proper-image and duality calculus, and states the Grothendieck-group correspondence. For Fourier transformation and normal specialization, see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://www.numdam.org/item/AST_1985__128__1_0/), Astérisque 128 (1985), §§2.1–2.2, pp. 39–46. Its §2.1 recalls the Fourier statements without proofs; we give the kernel and support arguments below. Definition 5.5.1, pp. 90–91, gives microlocal Hom with the exceptional first projection and the first-covector convention used here. The preceding lesson, Constructible functions and Euler integration, develops that calculus with locally finite strata and support-preserving bounded realizations.

For the directional constructions we use normalized conic transport, whole-complex parameter descent, the Fourier halfspace and radial-kernel proofs, and the positive-parameter specialization boundary map. The perfect-operation theorem supplies finite constructible coefficients through the actual zero-section comparison. We will keep the open or closed boundary, the support condition and the degree visible in each calculation.

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
Denote this group by \(CF_{\mathbb R_{>0}}(E)\). Conic complexes have locally constant cohomology along positive scalar orbits. The normalized transport theorem supplies a natural action isomorphism, including the zero section, normalized at scalar one and satisfying the cocycle identity. It is constructed from the ordinary parameter-projection counit and evaluation at one; whole-complex interval descent makes these maps invertible. Its uniqueness gives the cocycle identity. Restriction only to the punctured bundle would leave the zero coefficient and its attachment to the rays undetermined.

## Separate the zero section from the positive rays

The positive ray quotient \(S_E=E^\times/\mathbb R_{>0}\) is an analytic manifold. In a bundle chart it is the product of the base with the unit sphere. Normalizing a nonzero vector gives analytic local charts; transitions normalize the analytic linear bundle transitions and are analytic. This construction needs no choice of a global analytic metric. Let \(\gamma:E^\times\to S_E\) be the quotient.

There is an equivalence
\[
\gamma^{-1}:D^b_{\mathrm{rc}}(S_E;k)
 \ \simeq\ D^b_{\mathrm{rc},\mathbb R_{>0}}(E^\times;k),
\qquad\text{inverse }R\gamma_* .
\qquad\text{(4)}
\]
To prove it, work in a ray chart \(S\times\mathbb R_{>0}\), with projection \(r\) and radius-one section \(e\). Whole-complex parameter descent gives the ordinary counit \(r^{-1}Rr_*K\to K\) and evaluation \(Rr_*K\to e^{-1}K\) as isomorphisms whenever the cohomology of \(K\) is locally constant along the rays. The proof uses proper closed parameter intervals, their actual evaluation maps and compatible restriction as the intervals exhaust the ray. It therefore applies to the bounded complex itself, including extension data between its cohomology sheaves. For \(K=r^{-1}B\), the triangular identity identifies the unit with the inverse of evaluation. These are the global unit and counit of \(\gamma^{-1}\dashv R\gamma_*\), so their local inverses agree on chart overlaps and prove (4).

Constructibility is preserved: analytic radius-one sections identify the local ordinary image with an inverse image, while pullback adds a product interval to a subanalytic stratification. The cohomology bounds are unchanged, and every stalk remains finite. There is no uniform bound on ranks and no compactness assumption on the base. In contrast, proper-support base change and the positive radial orientation give \(R\gamma_!\gamma^{-1}G\simeq G[-1]\). Changing ray charts rescales the positive radius by a positive function, hence preserves this orientation line. The inverse in (4) is the ordinary image, with degree zero.

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
The first three functors have the stated bounded constructible domains by closed extension, inverse image and (4). For \(\beta''\), ordinary pullback on the punctured bundle is bounded constructible, and open extension is exact. Its extension across zero is constructible as well: over a relatively compact trivializing base chart the sphere is compact, so a locally finite angular stratification has only finitely many pieces there. Radially cone those subanalytic pieces in a bounded disk, and refine their frontiers together with the zero section. The radial map from the compact sphere times a closed radius interval is proper, so these images are subanalytic. This gives the required finite local stratification at zero. The degree bounds do not change. Pulling the normalized ray transport through the equivariant open extension makes the result conic, with zero stalk at the zero section. The open–closed triangle
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
This supplies both surjectivity and injectivity. Explicitly, use the preceding lesson's support-preserving realizations for the zero and angular functions, both in degrees \(-1,0\), and form \(i_*A\oplus j_!\gamma^{-1}B\). Its nonzero stalk locus is exactly the nonzero locus of the prescribed homogeneous function. Its closed sheaf support is consequently that function's closed support, including zero points approached by nonzero angular values. Thus the realization may be chosen both conic and support-preserving, with two global degrees even when the base is noncompact and the ranks are unbounded.

Conversely, an element of the Grothendieck group is a finite sum of object classes and their negatives; shifts and finite direct sums represent it by one object. If its Euler function is zero, ordinary restriction and angular descent give zero Euler functions for both summands of (7). The preceding Grothendieck theorem makes those two classes zero, so (7) makes the original class zero. Locally infinite stratifications are allowed throughout: the realizations are actual sheaf complexes and (6) is one triangle, not an infinite sum of Grothendieck relations. For rank zero the ray term is absent.

## Ordinary and supported radial projection

Conic contraction supplies natural comparisons
\[
R\tau_*F\simeq i^{-1}F,\qquad R\tau_!F\simeq i^!F.
\qquad\text{(10)}
\]
The first map is restriction of the ordinary projection counit to the zero section. In a trivialization, restriction from the full fibre to an open ball is invertible by radial interval descent; these restrictions are compatible as the base open set and radius shrink. Passing to the zero-section stalk system proves the ordinary comparison. The second map is
\[
i^!F=R\tau_!i_*i^!F\longrightarrow R\tau_!F,
\]
induced by the closed support counit. Compare the localization triangles for zero-section support and for support in a closed disk. On the complements, conic radial restriction is invertible; on unrestricted sections it is identity. The inclusion of zero-section support into disk support is therefore an isomorphism. Disk supports are cofinal among proper supports after passage to a base stalk: shrink to a base neighborhood with compact closure, then bound the fibre norm on the compact part of any proper closed support above that closure. The compatible support colimit proves that the displayed counit map is invertible. These are the ordinary and proper-support contraction maps.

Ordinary and exceptional inverse image preserve bounded constructibility and finite stalks here. Thus (10) also proves that both nonproper radial images have those properties. Global degree bounds come from the bounded input and the uniform finite dimension of the operations, not from a uniform rank bound or properness of the whole coefficient support.

We therefore define the two radial function images by
\[
\tau_*\phi=i^*\phi,\qquad \tau_!\phi=i^!\phi.
\qquad\text{(11)}
\]
These operations are defined for all homogeneous constructible functions. They extend the ordinary support-proper Euler image in this particular conic setting.

Choose a Euclidean norm, with analytic square, in a local bundle trivialization and let \(B_\varepsilon\) be its open fibre ball. Then
\[
\begin{aligned}
\tau_!\phi&=\tau_!(\phi\,1_{B_\varepsilon}),\\
\tau_*\phi&=\tau_!(\phi\,1_{\overline B_\varepsilon}).
\end{aligned}
\qquad\text{(12)}
\]
The right sides are the usual Euler images: their closed coefficient supports are contained in the closed disk bundle, proper over the local base. Realize \(\phi=\chi F\) conically by (9), and restrict to a single fibre over \(z\). The actual small-ball map includes point support into compact support in the open ball; the closed-ball map restricts ordinary sections to the zero stalk. The small-ball support and restriction proof makes these maps invertible for sufficiently small radii. It applies on the fibre with its identity coordinate map, which is proper on every closed coefficient support. Conic transport carries the maps for any one radius to those for any other positive radius, preserving point support and the ordinary restrictions. Hence they are invertible for every radius, without needing a single small-radius threshold uniform in \(z\).

For the first line of (12), compact extension from the open ball to the full fibre identifies its compact complex with the fibre costalk: the point-support counit factors through that extension and both point-to-compact maps are the just-proved isomorphisms. Proper-support base change identifies these complexes with the two radial image stalks. For the second line, the closed ball is compact, so its ordinary sections are its compact sections; restriction to zero gives the ordinary stalk. The cutoff's closed disk support is proper over the local base, so the preceding lesson's support-proper Euler image applies. Taking stalk Euler values proves (12). These are fibrewise equalities of constructible functions, with all terms already defined as bounded constructible images.

Thus (12) is independent of radius and of the chosen local Euclidean norm, since each side equals the intrinsic operation in (11). The local statements glue. For example,
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
Put \(L=p^{-1}F\otimes k_N\). It is bounded constructible by perfect inverse image and tensor, and its conic transport in \(v\) is the pulled-back transport of \(F\), since positive scaling preserves the closed inequality. Its image is identified by the specified counit
\[
i_E^!L=Rq_!(i_E)_*i_E^!L\longrightarrow Rq_!L=T_EF.
\]
The proper-support contraction just proved makes this map invertible. In particular its source proves finiteness and constructibility of the image even though \(q\) is not proper on the full support of \(L\). Exceptional inverse image on finite-dimensional manifolds gives a global degree bound. Equivalently, if \(F\in D^{[a,b]}\), the rank-\(n\) proper-support projection places \(T_EF\) in \(D^{[a,b+n]}\). No bound on all stalk ranks is used.

Taking Euler functions of this very comparison, tensor multiplicativity and (2) gives (16), hence independence of the conic representative through (9). Dual-coordinate scaling preserves \(N\) and commutes with \(q\). Proper-support base change pulls this invariance through the image as one normalized parameter isomorphism. Thus the output is homogeneous in the dual variable, including its zero section.

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

Here is the kernel argument behind (18), including its zero-section attachment. The right adjoint of \(T_E\) is
\[
S_EG=Rp_*R\mathcal Hom(k_N,q^!G).
\]
Its adjunction follows in order from \(Rq_!\dashv q^!\), tensor–Hom adjunction and \(p^{-1}\dashv Rp_*\). The fibre of \(q\) is \(E\), so \(q^!G=q^{-1}G\otimes O_E[n]\), with the orientation line pulled from the base. The negative-cut/positive-support comparison identifies this adjoint with the positive-halfspace proper kernel
\(Rp_!(q^!G\otimes k_{\{\langle v,\eta\rangle\geq0\}})\).

For clarity, that comparison is made by maps. Put \(L=p^{-1}F\), \(C=\{\langle v,\eta\rangle\geq0\}\), and \(H=R\Gamma_C L\). Localization by the strict positive pairing set gives
\(R\Gamma_C(L_N)\simeq H_N\).
The object \(H_N\) is supported on \(v=0\). Indeed, near \(v\ne0\), use \(\langle v,\eta\rangle\) as a dual coordinate. In these product coordinates the coefficient is pulled back from the remaining variables. Interval descent therefore makes the local-support boundary stalk the fibre of the identity restriction from an interval to its negative half-interval, so it vanishes. Forgetting support after \(Rq_!\), passing from \(!\) to \(*\) on the zero-section-supported object, and restricting after \(Rq_*\) give the chain
\[
Rq_!L_N\longleftarrow Rq_!R\Gamma_C(L_N)
\simeq Rq_!H_N\longrightarrow Rq_*H_N\longleftarrow Rq_*H.
\]
The first and last arrows are isomorphisms by the exceptional and ordinary contractions in (10), since the zero section lies in both closed halfspaces. The middle support-forgetting arrow is invertible because its support projects identically to the base. Interchanging the bundle and dual, reversing both inequalities and retaining the orientation coefficient proves the asserted formula for \(S_E\).

Now work over \(Y=E\times_ZE\), writing its coordinates as \((x,y)\). Let \(r\) integrate \(\eta\in E_z^*\), and set \(u=\langle x,\eta\rangle\), \(v=\langle y,\eta\rangle\). Composition, proper-support base change and projection formula identify \(S_ET_E\) with the kernel
\[
K=Rr_!k_{\{u\leq0,\ v\geq0\}}\otimes O_{E^*}[n].
\]
Here positive dual orientation identifies \(O_E\) with \(O_{E^*}\). Cut the second inequality by its strict complement. The resulting localization triangle is
\[
J\longrightarrow D\longrightarrow K\xrightarrow{+1},\qquad
J=Rr_!k_{\{u\leq0,v<0\}}\otimes O_{E^*}[n],\quad
D=Rr_!k_{\{u\leq0\}}\otimes O_{E^*}[n].
\]
Let \(Z_0=\{x=0\}\), \(V_0=\{y\ne0\}\), and
\(A=\{(x,y)\in V_0:x=sy\text{ for some }s\geq0\}\).
The set \(A\) is closed in \(V_0\): locally choose a linear functional nonzero on \(y\), so the possible scalar is a continuous quotient. Full-fibre orientation trace, followed by restriction to \(u\leq0\), constructs \(D\simeq k_{Z_0}\). Off \(x=0\), the fibre is a closed halfspace and its compact cohomology is zero.

On \(V_0\), the open halfspace \(v<0\) has its orientation coefficient in degree \(n\); after the displayed twist it gives \(k_{V_0}\). Restriction to \(u\leq0\) constructs the identification of \(J|_{V_0}\) with \(k_A\). For \(x=sy\), \(s\geq0\), the restriction leaves the fibre unchanged. For a negative multiple the fibre is empty. For independent \(x,y\), the fibre is a closed halfline times an open halfline times a Euclidean space and has zero compact cohomology. At \(y=0\) the strict inequality is impossible. Thus \(J\) is closed extension from \(A\) in \(V_0\), followed by open extension to \(Y\).

The arrow \(J\to D\) is restriction to \(A\cap Z_0\), then open extension inside \(Z_0\). At \((0,y)\) with \(y\ne0\), it is extension of compact support from an open halfspace to the full dual fibre, which sends the normalized top orientation class to itself. All other stalk maps have a zero source or target. Since these are already constructed degree-zero sheaves and their sheaf morphisms, this stalk check identifies the arrow itself.

Compare this with \(h(y,s)=(sy,y)\), \(s\geq0\), and \(h_+=h|_{s>0}\). The scalar open–closed triangle gives
\[
Rh_!k_{E\times[0,\infty)}\longrightarrow k_{Z_0}
\longrightarrow R(h_+)_!k_{E\times(0,\infty)}[1]\xrightarrow{+1}.
\]
Its first term is the same extension of \(k_A\): over \(y\ne0\), \(h\) is a homeomorphism to \(A\), and over the zero pair its fibre is the closed halfline, with zero compact cohomology. Its arrow to \(k_{Z_0}\) is the same restriction just identified. Taking the specified cofiber of this one map proves
\[
K\simeq R(h_+)_!k_{E\times(0,\infty)}[1].
\]
This comparison retains gluing at the zero pair, not only the nonzero radial fibres. All of its maps are restriction, extension and relative orientation trace, so they commute with bundle-coordinate changes and glue over the base. Rank zero also works: \(J=0\), \(D=k_Z\), and the positive halfline shifted by one has compact cohomology \(k\).

Applying the radial kernel to \(F\) gives
\(R\mathrm{pr}_!\mathrm{scaling}^{-1}F[1]\).
Normalized conic transport identifies its input with \(\mathrm{pr}^{-1}F\), including at zero. Compact integration over the positive scalar contributes \(k[-1]\), cancelling \([1]\), so \(S_ET_E\simeq\mathrm{id}\). The same calculation with the negative pairing proves \(T_ES_E\simeq\mathrm{id}\). It follows that the actual kernel adjunction has invertible unit and counit. This does not require identifying every radial isomorphism with an independently normalized adjunction map.

Finally, replacing the positive pairing by the negative one through \(x\mapsto-x\) gives
\[
S_EG\simeq a^{-1}T_{E^*}G\otimes\tau^{-1}O_E[n].
\]
Insert \(G=T_EF\), invert the preceding equivalence and use the canonical pairing \(O_E\otimes O_E\simeq k_Z\). This proves (18). The line remains present on a nonorientable bundle; only its stalk Euler value becomes one. The shift and antipode in (19) therefore follow without selecting an orientation or an extra sign for a Fourier adjunction.

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
To prove this, pull back the product \(E\times_ZE^*\). Its two projection squares are cartesian, and its negative pairing subset pulls back to the corresponding subset on \(E'\). Proper-support base change for the sheaf \(Rq_!\), followed by exact inverse image of the kernel, identifies \(b_{E^*}^{-1}T_EF\) with \(T_{E'}b_E^{-1}F\). Taking (16) proves (21). The map is the actual base-change map; it is compatible with successive pullbacks by cartesian pasting. Properness of \(b\) is unnecessary. More explicitly, let \(b_W:E'\times_{Z'}E'^*\to E\times_ZE^*\) be the induced map. The comparison is
\[
b_{E^*}^{-1}Rq_!(p^{-1}F\otimes k_N)
\xrightarrow{\sim}Rq'_!b_W^{-1}(p^{-1}F\otimes k_N)
=Rq'_!(p'^{-1}b_E^{-1}F\otimes k_{N'}).
\]
It pulls back properly supported sections, whose pulled-back supports remain proper over the new base, and then derives that map. The finite-dimensional base-change proof identifies it on the common fibres and proves its pasting compatibility. The first Fourier base-change identity is exactly this composite. It involves ordinary inverse image, and both Fourier fibres have rank \(n\); no dimension or orientation of \(Z'\to Z\) enters. The output is bounded constructible by the zero-section argument on \(E'\), even for a nonproper or critical base map.

In particular the transform can be calculated on each fibre. For a vector space \(E\), (12)–(14) give the finite integral
\[
\widehat\phi(\eta)=
\int_E\phi(v)\,
1_{\{|v|<\varepsilon\}}\,
1_{\{\langle v,\eta\rangle\leq0\}}\,d\chi .
\qquad\text{(22)}
\]
Its closed support lies in a compact closed ball. Thus the preceding lesson's Euler integral applies. Conicity permits any positive radius, although the small-ball proof alone would already suffice for a sufficiently small radius. The squared Euclidean norm is analytic in a linear chart, so its open-ball inequality is subanalytic. The result is independent of the norm by (14). The pairing boundary is included; the ball boundary is excluded.

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

If \(C\ne\{0\}\), a strictly positive linear functional can be obtained directly. The compact set \(C\cap S^{n-1}\) has compact convex hull. That hull does not contain zero: a positive convex combination equal to zero would express the negative of one nonzero cone vector as a positive sum of the others, putting a line in \(C\). Choose the point \(w\) of smallest Euclidean norm in the hull. It is nonzero, and differentiation along every segment from \(w\) to a point \(z\) of the hull gives \(\langle w,z\rangle\geq|w|^2>0\). Thus \(\ell(v)=\langle w,v\rangle\) is strictly positive on \(C\setminus0\).

The level-one section \(C\cap\{\ell=1\}\) is convex, closed and bounded, the last assertion following from the positive minimum on the unit link. Radial normalization identifies it homeomorphically with \(C\cap S^{n-1}\). It is a nonempty compact contractible subanalytic set, so its Euler value is one even if \(C\) has smaller dimension than \(E\). The closed truncated cone \(C\cap\overline B_\varepsilon\) contracts radially to its vertex and also has value one. Removing the included outer spherical boundary, while retaining the vertex, gives
\[
\chi_c(C\cap B_\varepsilon)=1-1=0.
\qquad\text{(24)}
\]
If \(C=\{0\}\) its value is one. This proves the second formula. For \(\gamma=\{0\}\) the polar is all \(E^*\) and the same answer holds. In rank zero both spaces are points and the formulas reduce to ordinary identity. A cone containing a line is outside this second statement. For example, if \(L\subset E\) is a vector subspace of dimension \(d\), (22) gives
\[
\widehat{1_L}=(-1)^d1_{L^\perp}.
\]
On the annihilator the truncated fibre is an open \(d\)-ball in \(L\); off it the fibre is a closed halfspace cut through that ball, whose compact cohomology vanishes by the open-convex localization argument. The sign uses \(d\), not the ambient \(n\). This explains exactly why the pointed-cone vanishing cannot be used for a cone containing a line.

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
This is the connecting arrow of (26), not an independently chosen identification. In a cochain model, the localization fibre is \(\operatorname{Cone}(j_!H\to Rj_*H)[-1]\). Restriction to the central fibre kills \(j_!H\), so the connecting map is the identity inclusion into that same cone. The remaining shift \([1]\) changes Euler value by a minus sign. Equivalently, the endpoint costalk of the open positive parameter coefficient is \(k[-1]\); shifting it by one restores the constant parameter coefficient in degree zero. Tensor and inverse image give \(\chi(j_!H)=(p^*\chi F)1_\Omega\), and (2) now proves
\[
\chi(\nu_MF)=\nu_M(\chi F),\qquad
\chi(\mu_MF)=\mu_M(\chi F).
\qquad\text{(28)}
\]
This derivation agrees with the positive-parameter boundary comparison in SH-02. It uses ordinary \(r^{-1}\) in \(H\); using \(r^!=r^{-1}[1]\) instead would move the same shift into that input.

The deformation dilation \((v,x'',t)\mapsto(\lambda v,x'',t/\lambda)\) fixes \(p\), preserves \(\Omega\), and restricts to positive dilation on the central bundle. Pullback under the corresponding parameterized diffeomorphism, followed by the ordinary chamber and central comparison maps, gives one transport isomorphism on the scalar parameter space. Its identity and composition laws come from inverse-image composition, so \(\nu_MF\) is conic, including at the zero section.

Finiteness does not follow merely from that conicity or from a nonproper open image. The map \(p\) is analytic on the whole deformation and \(k_\Omega\) is bounded constructible. Open internal-Hom adjunction gives
\[
Rj_*j^{-1}p^{-1}F\simeq R\mathcal Hom(k_\Omega,p^{-1}F).
\]
Perfect inverse image and internal Hom make this bounded constructible with finite stalks; ordinary central restriction preserves those properties. This is the specialization and microlocal-Hom finiteness proof, with the actual open-image comparison retained. Together with (9) and (16), it proves the function domains in (25), additivity and representative independence in (28). Uniform manifold dimension bounds control all degree ranges; pointwise finite ranks need not have a common bound. Normal bundles of different ranks on different components are treated componentwise, with the same uniform dimension bound. Restriction to smaller analytic charts commutes with every construction.

Using \(s^!=D_{T_MX}s^*D_{D_MX}\), the coordinate expression is
\[
(\nu_M\phi)(v,x'')=
-D_{T_MX}\!\left[
\left.D_{D_MX}
\bigl(\phi(tv,x'')\,1_{\{t>0\}}\bigr)\right|_{t=0}
\right](v,x'').
\qquad\text{(29)}
\]
Both dualities are taken in their displayed ambient manifolds. Replacing them by duality only in the \(t\) variable would discard normal and tangential contributions. Equation (29) is simply (25) in deformation coordinates, so the construction is independent of the chart.

Choose the support-preserving bounded realization of \(\phi\) from the preceding lesson, so its closed sheaf support is exactly \(A=|\phi|\). The closed support of its chamber inverse image is contained in \(r^{-1}A\). Outside \(\overline{r^{-1}A}\), an open neighborhood has zero chamber coefficient, hence zero derived chamber sections and zero \(Rj_*H\). Central restriction therefore has support inside \(T_MX\cap\overline{r^{-1}A}=C_M(A)\). Its Euler function can have still smaller support through cancellation, so we obtain only
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

We calculate specialization using actual chamber sections. Near a positive vector \((a,0)\), choose an ambient box
\[
|v_x-a|<\delta,\qquad |v_y|<h,\qquad |t|<\varepsilon,
\quad 0<\delta<a/2,\quad \varepsilon(a+\delta)^2<h.
\]
Its chamber part has \(0<t<\varepsilon\). The first lifted branch is \(v_y=0\), and the second is \(v_y=t v_x^2\). The inequality places the whole second graph inside the transverse width, for every \(v_x\) in this interval and every positive parameter in the box. Each graph is homeomorphic to the same open parameter rectangle, hence has constant-coefficient cohomology \(k\) in degree zero and no higher groups. They are disjoint because \(v_x>0\) and \(t>0\). Both are closed in the chamber box, so ordinary sections of their closed extensions give two copies of \(k\). Shrinking boxes restricts each constant section identically. Such boxes are cofinal among neighborhoods of the central point, proving the asserted stalk through its actual restriction maps.

At the zero normal vector choose the ambient open box
\(|v_x|<\delta\), \(|v_y|<h\), \(|t|<\varepsilon\), with \(\varepsilon\delta^2<h\).
On each branch its chamber support is parametrized by \([0,\delta)\times(0,\varepsilon)\), a contractible locally contractible space; these are ordinary sections, so its half-open edge adds no compact-support degree. The two supports meet exactly along \(v_x=0\), \(0<t<\varepsilon\), a contractible interval. For their closed extensions inside the chamber box, the stalkwise closed-union exact sequence is
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
Use the conic representative from (9), retaining both its angular part and its zero-section attachment. The normal deformation of a vector bundle along its zero section is canonically \(E\times\mathbb R\); the blow-down is \(p(v,t)=tv\). Normalized conic transport on \(t>0\) identifies \(p^{-1}F\) with the pullback under \(\mathrm{pr}_E\). For each open \(U\subset E\), ordinary parameter descent identifies sections on \(U\times(0,\varepsilon)\) with \(R\Gamma(U;F)\), by evaluation. These identifications commute with smaller \(U\) and smaller positive parameter intervals. Their stalk limits at \((v,0)\) therefore identify the actual central restriction of the chamber image with \(F_v\). The comparison is induced by transport and the ordinary counit, so it glues as a sheaf isomorphism and is natural in \(F\). No compact parameter integration occurs, and no normal-rank shift is introduced. Taking Euler values proves (34), also at the zero section and for nonorientable bundles.

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
The map from right to left in (37) is obtained by currying the actual evaluation
\[
(q_1^{-1}F\otimes q_2^{-1}D_XG)\otimes q_2^{-1}G
\longrightarrow q_1^{-1}F\otimes q_2^{-1}\omega_X
\xrightarrow{\sim}q_1^!F.
\]
The last comparison is smooth exceptional inverse image for the second-factor fibre. Tensor factors are kept in this order, with their derived symmetry when evaluation requires it.

Here is why this particular map is invertible. On a rectangle \(U\times V\), exceptional adjunction and proper-support composition identify sections of the Hom kernel with
\[
R\operatorname{Hom}_k\bigl(R\Gamma_c(V;G),R\Gamma(U;F)\bigr).
\]
Restriction in \(V\) is precomposition with extension of compact support; restriction in \(U\) acts on the second input. At \(y\), the actual compact-section neighborhood system of \(G\) is represented by its perfect costalk \(C_y=i_y^!G\). A bounded finite-projective model gives \(R\operatorname{Hom}_k(C_y,-)=C_y^\vee\otimes_k-\), which commutes with the filtered ordinary stalk limit at \(x\). Constructible duality identifies \(C_y^\vee=(D_XG)_y\). The stalk of the displayed map is consequently the finite-projective evaluation
\(F_x\otimes C_y^\vee\to R\operatorname{Hom}_k(C_y,F_x)\), an isomorphism. Rectangles form a neighborhood basis and stalks detect an isomorphism, proving (37) with its actual evaluation map.

This is the constructible-factor external-Hom theorem, in the factor order of (36). The diagonal duality lesson verifies the same transpose and the first-covector convention. Finite perfection is used on a represented compact-section system before passing Hom to a stalk. It is not an assertion that arbitrary sheaf Hom has the Hom of its two ordinary stalks.

Taking the Euler function of (37), applying (28) and then (16), proves
\[
\chi\bigl(\mu\operatorname{hom}(G,F)\bigr)
=\mu\operatorname{hom}(\chi G,\chi F).
\qquad\text{(38)}
\]
All operations are additive in each input at the Grothendieck-group level: duality reverses triangles but preserves their additive relation, external tensor multiplies Euler functions, and specialization and Fourier transformation are exact. Thus (35) is a bilinear, representative-independent homogeneous constructible function, without a compact-support assumption on either input.

Its support can also be checked using the same definitions. Locality and involutivity of function duality give \(|D_X\psi|=|\psi|\). The external function in (35) has closed support inside \(|\phi|\times|\psi|\). Its diagonal specialization therefore vanishes over every \(x\) outside \(|\phi|\cap|\psi|\), by (30). Fourier transformation is over that same base and preserves vanishing over a base open set, by (21). Hence
\[
\operatorname{supp}\mu\operatorname{hom}(\psi,\phi)
\subset \pi_X^{-1}(|\psi|\cap|\phi|),
\qquad\pi_X:T^*X\to X.
\]
This is only containment: Euler cancellation can remove directions or entire stalk values. It makes no inference about a sheaf's microsupport from its Euler function alone.

The exceptional projection \(q_1^!\) remains essential to (37): its second-factor fibre dualizing complex supplies the orientation and dimension shift. Specialization then uses the full ambient external coefficient, and Fourier transformation uses the first-covector identification \((\xi,-\xi)\mapsto\xi\). Ordinary Hom between two stalks would erase the duality factor and the boundary information used by specialization.

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

Directly, the open positive ray contributes the compact Euler value of \((0,\varepsilon)\), namely \(-1\), when \(\eta\leq0\), and contributes zero when \(\eta>0\). The closed positive ray contributes the point \(0\), of value one, when \(\eta>0\); when \(\eta\leq0\), its fibre is \([0,\varepsilon)\), whose value is zero. Negating both pairing variables gives the other two cases without altering compact degrees. This verifies all four values at the zero covector as well as the open-ray values.

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

There is a concrete difference already at the dual origin. Its transform stalk is \(R\Gamma_c(\mathbb R^2;F)=R\Gamma(S^1;L)[-1]\), by polar coordinates and compact radial integration. For monodromy \(-1\), the circle complex is \([k\xrightarrow{-2}k]\), acyclic in characteristic zero. For angular constant coefficients it is \(k\oplus k[-1]\), so the transform stalk is \(k[-1]\oplus k[-2]\). Both have Euler value zero there, while the objects differ. The Fourier transform retains this information until the Euler function is taken.

### Pulling a bundle back adds no Fourier sign
*Difficulty: Intermediate.*

Let \(E\) be a possibly nonorientable real rank-three bundle and \(b:Z'\to Z\) an analytic map. Show that the pullback of its constant function transform is the transform of its pulled-back constant function. Identify the coefficient.

**Solution.** Both are \(-1_{0_{E'^*}}\) by (20), since the rank is three. Equation (21) proves equality for every homogeneous function, not just this test. Nonorientability changes the orientation local system in (18), but its stalk rank is one. Its Euler coefficient is consequently unchanged. The rank is also unchanged by base pullback; no dimension of \(Z'\) enters the sign.

### The specialization minus sign is a boundary shift
*Difficulty: Intermediate.*

Specialize the constant function on \(X=\mathbb R\) along \(M=\{0\}\), directly using (25). Then microlocalize it.

**Solution.** In the deformation plane the chamber function is \(1_{\{t>0\}}\). Its central ordinary restriction is zero, but the exceptional central restriction has Euler value \(-1\): (27) identifies it with the constant normal coefficient shifted by \([-1]\). The outer minus in (25) gives \(\nu_0(1_{\mathbb R})=1_{\mathbb R_v}\). Its one-dimensional Fourier transform is \(-1_{\{0\}}\) by (20), so \(\mu_0(1_{\mathbb R})=-1_{\{0\}}\). Omitting the boundary minus would reverse this result.

The endpoint calculation is also a direct localization test. On a small parameter interval, the open extension of the positive constant coefficient has zero stalk at \(t=0\), whereas its ordinary chamber image has stalk \(k\). The central localization fibre is therefore \(k[-1]\), and its connecting map shifted by one is the identity of \(k\). The untouched \(v\)-coordinate gives the constant normal coefficient. This establishes the sign through the actual boundary triangle, rather than assigning a sign to an abstract rank-one vector space.

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

The normal quotient to the diagonal is identified with \(TX\) by \((v_1,v_2)\mapsto v_1-v_2\); its dual is precisely the chosen first covector. The fibre of \(q_1\) is the second copy of \(TX\). Their two orientation local systems are consequently the same sign line, and their tensor square is canonically trivial. Together with the shifts \([m]\) and \([-m]\), this gives the constant coefficient on the zero covectors with no remaining orientation factor. On \(\mathbb R^m\) these lines can be trivialized, but the argument does not obtain a sign from that choice.

## References

P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), *Journal of Pure and Applied Algebra* **72** (1991), 83–93, §§2–3: Euler integration, proper images, duality and the stated Grothendieck correspondence. M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://www.numdam.org/item/AST_1985__128__1_0/), Astérisque **128** (1985), §2.1, pp. 39–41, states the Fourier transform, inversion and bundle functoriality; §2.2, pp. 41–46, treats normal specialization; Definition 5.5.1, pp. 90–91, defines microlocal Hom. The function-level boundary signs, cone integrals and tangent-branch calculations are derived here using the complete programme proofs linked above.

The directional arguments use the linked conic-descent, Fourier-kernel, base-change, specialization and external-Hom proofs with the hypotheses stated above. The halfspace cofiber identifies the Fourier kernel across zero, the localization boundary fixes specialization's degree, and the external evaluation retains microlocal Hom's exceptional coefficient.

The next lesson relates constructible functions to integral Lagrangian cycles. The original exposition, examples and complete solutions here are dedicated to CC0; the named human sources retain their authorship and their own terms.
