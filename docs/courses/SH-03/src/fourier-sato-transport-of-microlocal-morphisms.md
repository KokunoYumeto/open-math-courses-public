# Fourier-Sato transport of microlocal morphisms

Fourier-Sato transformation exchanges a vector and a covector. For conic sheaves it transports not just microsupport, but the full sheaf of directional morphisms. Its cotangent exchange is not homogeneous for ordinary cotangent dilation, so the contact-kernel theorem cannot be applied to that exchange directly. We will apply the theorem on positive-ray spaces, then add two coordinates to recover every cotangent point, including both zero axes.

Use When a kernel quantizes a contact transformation. The exact foundational inputs are bounded Fourier transformation, radial descent and its orientation trace, the smooth and closed-embedding microlocal Hom comparisons, and the regular open/closed boundary microsupport formulas. We display the particular versions used. Their foundational proofs remain prerequisites.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## A typed Fourier comparison

Let \(Z\) be a smooth finite-dimensional Hausdorff manifold, countable at infinity, and let \(E\to Z\) be a smooth real vector bundle of fixed finite rank \(n\). The coefficient ring \(k\) is commutative with identity and finite global dimension. Let \(F_1,F_2\in D^b(k_E)\) have cohomology locally constant along positive scalar orbits in each fibre. This is positive conicity; it imposes no invariance under negative scalars and no constructibility or finite-generation condition on the coefficients.

On \(E\times_ZE^*\), with projections \(p,q\), use the negative Fourier convention

\[
\mathcal F_E(F)=Rq_!\left(p^{-1}F\otimes k_{\{\langle x,\xi\rangle\le0\}}\right).
\qquad\text{(1)}
\]

The Fourier prerequisite preserves bounded conic complexes under these hypotheses. Its finite fibre bounds, rather than properness of the bundle projection, supply boundedness. Write \(M_X(A,B)=\mu\operatorname{hom}_X(A,B)\), with the first argument contravariant.

There is a canonical cotangent diffeomorphism

\[
\mathscr L_E:T^*E\longrightarrow T^*E^*,\qquad
(z,x;\zeta,\xi)\longmapsto(z,\xi;\zeta,-x)
\qquad\text{(2)}
\]

in local bundle coordinates. Intrinsically, its base point is the restriction of the input covector to the vertical tangent. The identity
\(\mathscr L_E^*\theta_{E^*}=\theta_E-d\langle x,\xi\rangle\)
specifies its remaining coordinates uniquely and proves that the expressions glue under bundle changes. This is the exact cotangent-exchange prerequisite.

**Theorem.** There is an isomorphism, natural in both bounded conic inputs,

\[
(\mathscr L_E)_*M_E(F_2,F_1)
\simeq M_{E^*}(\mathcal F_EF_2,\mathcal F_EF_1).
\qquad\text{(3)}
\]

Both sides are sheaves of complexes on all of \(T^*E^*\). The direct image by a diffeomorphism in (3) is exact. In particular (3) includes \(x=0\), \(\xi=0\), their intersection, and arbitrary base covectors \(\zeta\). We construct the isomorphism using a fixed auxiliary bundle metric and the specified orientation comparisons. No perfection of either input is needed.

## Exact radial and microlocal inputs

Let \(B\to Z\) temporarily be any rank-\(m\) bundle. Put \(B_0=B\setminus0\), \(S=S(B)=B_0/\mathbb R_{>0}\), and \(S^*=S(B^*)\). Opposite real rays are distinct. Let \(j:B_0\hookrightarrow B\) and \(\gamma:B_0\to S\), with \(j^*,\gamma^*\) on the dual bundle. The star here labels the dual bundle; it is not a sheaf operation.

The radial descent input gives, for any bounded conic \(H\),

\[
H|_{B_0}\simeq\gamma^{-1}G,\qquad
G=R\gamma_*(H|_{B_0}).
\qquad\text{(4)}
\]

The comparison is the radial counit. Its proof is the cylinder descent theorem after logarithmic radial coordinates. Restriction to a metric unit sphere identifies \(G\) with a bounded complex, so no unbounded angular object is introduced.

Here are the two exact microlocal Hom transport inputs. For a smooth submersion \(f:U\to V\), let
\(C_f=U\times_VT^*V\), let \(h_f:C_f\to T^*U\) send a covector to its transpose differential, and let \(\rho_f:C_f\to T^*V\) forget its lifted base point. Then

\[
M_U(f^{-1}A_2,f^{-1}A_1)
\simeq(h_f)_*\rho_f^{-1}M_V(A_2,A_1).
\qquad\text{(5)}
\]

The map \(h_f\) is the closed horizontal cotangent embedding. The smooth exceptional comparison first carries the common relative dualizing complex in both arguments; the simultaneous invertible-line cancellation produces (5). Thus it adds no degree. For a closed embedding \(i:U\hookrightarrow V\), the corresponding comparison is

\[
M_V(i_*A_2,i_*A_1)
\simeq(h_i)_*\rho_i^{-1}M_U(A_2,A_1),
\qquad\text{(6)}
\]

where \(C_i=U\times_VT^*V\), \(h_i\) is its closed inclusion in \(T^*V\), and \(\rho_i\) restricts a covector to \(TU\). In (6), \(i_*\) is exact and proper. These are the actual smooth and closed-embedding comparisons for arbitrary bounded complexes. In particular they do not invoke an external-Hom exchange requiring both input coefficients to be perfect.

For (4), the horizontal set in (5) is

\[
H_B=\{(z,x;\zeta,\xi):x\ne0,\ \langle x,\xi\rangle=0\}.
\qquad\text{(7)}
\]

Indeed its omitted tangent direction is the fibre Euler field. The exact conic microsupport criterion places \(\operatorname{SS}(H)\) in Euler annihilation, also on the zero section where the Euler field is zero. The microlocal Hom support bound places \(M_B(H_2,H_1)\) there too.

## The proper radial shift

On \(S^*\times_ZS\), put
\(D=\{(b,a):b(a)\le0\}\).
Let \(\mathcal T_D=\Phi_{k_D}\), integrating the \(S\) variable with proper supports. For any bounded \(G\in D^b(k_S)\), the particular proper radial comparison needed here is

\[
\mathcal F_B(j_!\gamma^{-1}G)|_{B^*_0}
\simeq(\gamma^*)^{-1}\mathcal T_D(G)[-1].
\qquad\text{(8)}
\]

We verify its normalization from the exact radial prerequisites. Let \(O_B\) be the bundle orientation local system on \(Z\); positive dual orientation identifies \(O_B\otimes O_{B^*}\) with \(k\). Write \(\mathcal S_{B^*}\) for the inverse Fourier operator from \(B\) to \(B^*\). Its proper-support comparison uses the positive pairing and the factor \(O_{B^*}[m]\). Pulling its output back by the fibre antipode \(a_{B^*}\) changes that positive pairing into (1), so

\[
\mathcal F_B(H)\simeq
a_{B^*}^{-1}\mathcal S_{B^*}(H)
\otimes\pi^{-1}O_{B^*}[-m].
\qquad\text{(9)}
\]

Here \(\pi:B^*\to Z\). The comparison is the specified proper-support formula for the inverse followed by antipodal inverse image and cancellation of its base orientation factor. No integration variable is reversed in this pullback.

The proper radial inverse formula, applied to the bundle \(B^*\) and input \(j_!\gamma^{-1}G\), turns \(\mathcal S_{B^*}\) into the positive sphere kernel with coefficient \(\omega_{S/Z}\) on its integrated \(S\) factor. It identifies the punctured output with the inverse image of that sphere operator; this is the radial comparison before its radial counit is applied. The increasing radial direction placed first gives
\(\operatorname{or}_{S/Z}\simeq\tau_S^{-1}O_B\),
and hence \(\omega_{S/Z}\simeq\tau_S^{-1}O_B[m-1]\).
After the antipode on the output sphere, the inequality is \(b(a)\le0\). The projection formula and positive dual-orientation pairing now cancel \(O_B\otimes O_{B^*}\), and the degree becomes

\[
(m-1)-m=-1.
\qquad\text{(10)}
\]

This proves (8) with its particular comparison map. Equivalently, the remaining degree is the compactly supported trace of the positive radial line, oriented by increasing logarithmic radius. The actual radial formula keeps \(j_!\); the ordinary radial formula with \(Rj_*\) is a different comparison. No orientability hypothesis on \(B\) has been inserted.

## A contact kernel on the two ray spaces

Assume \(m\ge2\). On \(T^*S\) select \(\Omega_S\), the covectors with nonzero restriction to the tangent of the ray-sphere fibre. Select \(\Omega_{S^*}\) similarly. Base covectors remain unrestricted. Regard \(D\) as a closed subset of the absolute product \(S^*\times S\), including equality of base points.

In a local orthonormal bundle frame, let \(a,b\) be unit representatives of the two rays. The boundary \(C\) of \(D\) inside the relative product is \(b(a)=0\). Its derivative is nonzero in each angular factor there. The conormal to the closed negative side has parameter \(t<0\). Its physical angular components, in output/input order, are
\((t a,t b)\).
The input antipode therefore gives angular covectors
\(\beta=t a\), \(\alpha=-t b\).
The base diagonal conormal gives equal input and output base covectors \(\zeta\). Thus the selected relation is the graph of

\[
\chi_S(z,a;\zeta,\alpha)
=\left(z,\frac{\alpha}{|\alpha|};\zeta,-|\alpha|a\right),
\qquad \alpha(a)=0,\quad\alpha\ne0.
\qquad\text{(11)}
\]

This expression is in the local orthonormal frame. The intrinsic conormal relation to the pairing boundary defines the same map on overlaps, including the transformation of the base covectors. Recovering \(a=-\beta/|\beta|\) and \(\alpha=|\beta|b\) gives its smooth inverse. Both conormal projections are therefore proper homeomorphisms onto the selected regions. The graph is relatively closed there.

Differentiating \(b(a)=0\) gives \(b\,da+a\,db=0\). Hence
\(\beta\,db=\alpha\,da\), and the base tautological terms agree. Formula (11) preserves the tautological form and commutes with positive ordinary cotangent dilation. It is the contact transformation to which the theorem applies.

We check the kernel conditions. The regular closed-halfspace model inside the smooth closed base diagonal gives cohomological constructibility of \(k_D\), with its locally perfect \(k\) coefficients. The exact regular-boundary microsupport and closed-embedding formulas put its microsupport, in the union of the two selected regions, in the branch just calculated. One angular component is nonzero precisely when \(t\ne0\), precisely when the other is nonzero. Conormals to the base diagonal over the interior have zero angular components and are excluded.

For the identity condition, use the restriction map \(k_D\to k_C\). Its cone is the open interior sheaf, shifted by one. The regular open-boundary formula puts that cone's nonzero angular normals on the opposite branch \(t>0\). Thus this map is an invertible microlocal germ at each point of the selected negative graph. It carries the identity of \(k_D\) to the identity of \(k_C\). The smooth-submanifold formula gives
\(M(k_C,k_C)\simeq k_{T_C^*}\), with identity section one and no codimension shift. Therefore the actual identity-induced map for \(k_D\) is invertible along the negative graph. This is a local germ comparison along that graph: the open-interior cone has microsupport elsewhere in the selected angular region, so the restriction map is not asserted invertible throughout that whole region.

All three conditions of the contact-kernel theorem hold. Its actual natural comparison gives

\[
(\chi_S)_*M_S(G_2,G_1)
\simeq M_{S^*}(\mathcal T_DG_2,\mathcal T_DG_1)
\quad\text{on }\Omega_{S^*}.
\qquad\text{(12)}
\]

No constructibility condition is imposed on the \(G_i\). The support projections of \(D\) are proper too, since the integrated sphere fibres are compact; the contact theorem used the separately checked proper graph projections.

## Returning to nonzero vectors and vertical covectors

Define
\(U_B=\{(z,x;\zeta,\xi):x\ne0,\ \xi\ne0\}\subset T^*B\),
where \(\xi\) is the vertical covector. We first prove (3) on \(U_B\). Choose \(G_i\) as in (4), and replace \(H_i\) by \(H_i'=j_!\gamma^{-1}G_i\). The actual open–closed triangle is

\[
H_i'\longrightarrow H_i\longrightarrow i_*i^{-1}H_i\xrightarrow{+1},
\qquad\text{(13)}
\]

with \(i\) the zero section. The first arrow is an ordinary isomorphism on \(B_0\). Under (1), the third term transforms to \(\pi^{-1}i^{-1}H_i\): its integrated fibre is a single point and has no Fourier degree. The smooth inverse microsupport estimate puts that transform at zero vertical covectors. Thus the transformed first arrow is a microlocal denominator wherever the output vertical covector is nonzero. The support and cone bounds for microlocal Hom invert these actual arrows in both arguments. This is the precise reason the replacement does not lose the comparison on \(U_B\) and its image \(U_{B^*}\).

Use (5) for \(\gamma\) on the input and for \(\gamma^*\) on the output of (8). The common output shift \([-1]\) cancels in the two Hom arguments by simultaneous invertible-complex cancellation. On the horizontal set (7), the two ray-space cotangent projections commute with the transformations. Indeed write
\(x=r a\), \(r=|x|>0\), and let \(R=|\xi|>0\). The input angular covector is \(\alpha=r\xi\). Fourier exchange gives output base ray \(b=\xi/R\) and angular covector \(\beta=-R x=-Rr a\). These are exactly (11), since \(|\alpha|=rR\). In local orthonormal coordinates the base covector \(\zeta\) agrees too. Intrinsic differential pullback makes these commuting correspondences global.

Consequently the pullback of (12), followed by (8) and the actual maps in (13), gives

\[
M_B(H_2,H_1)|_{U_B}
\simeq\mathscr L_B^{-1}
M_{B^*}(\mathcal F_BH_2,\mathcal F_BH_1)|_{U_B}.
\qquad\text{(14)}
\]

This is an isomorphism of sheaves, not just of directional cohomology groups. To see the extension from the horizontal set explicitly, (5) presents the input as the closed extension from (7). Both Fourier inputs are conic, so the output is also supported on its horizontal set; (2) exchanges the two horizontal sets. The open–closed triangle identifies any complex supported there with its closed extension from ordinary restriction. Thus the commuting horizontal comparisons give (14) on the entire good region. All inverse images by the displayed smooth cotangent maps and diffeomorphisms are exact.

## Two extra coordinates recover both axes

Return to the original rank-\(n\) bundle, with no lower bound on \(n\). Put
\(\widehat E=E\oplus\mathbb R_s\oplus\mathbb R_t\),
and
\(\widehat F_i=F_i\boxtimes k_{\mathbb R_s\times\{0\}_t}\).
These are bounded and conic for simultaneous positive fibre dilation. The exact Fourier stabilization comparison, with increasing \(s\) orientation, gives

\[
\mathcal F_{\widehat E}(\widehat F_i)
\simeq(\mathcal F_EF_i)\boxtimes
k_{\{0\}_u\times\mathbb R_v}[-1].
\qquad\text{(15)}
\]

Here \(u,v\) are dual base coordinates to \(s,t\). This particular comparison is the proper-support kernel map obtained by integrating \(s\) first: for \(u\ne0\), its cut is a closed half-line with zero compact cohomology; for \(u=0\), the full line contributes the stated degree \(-1\). It is a sheaf comparison across \(u=0\), fixed by the closed-support restriction and orientation trace.

Embed all of \(T^*E\) into \(T^*\widehat E\) by

\[
a(z,x;\zeta,\xi)
=(z,x,s=1,t=0;\zeta,\xi,u=0,v=1).
\qquad\text{(16)}
\]

Its fibre base \((x,1,0)\) and vertical covector \((\xi,0,1)\) are both nonzero for every \(x,\xi\). Fourier exchange sends this point to

\[
(z,\xi,u=0,v=1;\zeta,-x,du=-1,dv=0)
=b\,\mathscr L_E(z,x;\zeta,\xi),
\qquad\text{(17)}
\]

where \(b:T^*E^*\hookrightarrow T^*\widehat E^*\) inserts those fixed extra coordinates. Both output fibre components are again nonzero. Since \(\operatorname{rank}\widehat E=n+2\ge2\), (14) applies to every point of (16), even when both original components vanish.

Now apply (5) and (6) successively. For \(\widehat F_i\), the constant \(s\) factor has microlocal Hom concentrated at \(u=0\), and restriction at \(s=1\) returns the original object by (5). The closed \(t=0\) factor has its comparison constant along the entire normal covector fibre by (6); restriction at \(v=1\) returns it without a shift. Thus

\[
a^{-1}M_{\widehat E}(\widehat F_2,\widehat F_1)
\simeq M_E(F_2,F_1).
\qquad\text{(18)}
\]

On the output in (15), the closed \(u=0\) factor is tested at \(du=-1\), and the constant \(v\) factor at \(v=1,dv=0\). The same two exact comparisons, together with cancellation of the common \([-1]\), give

\[
b^{-1}M_{\widehat E^*}(\mathcal F_{\widehat E}\widehat F_2,
\mathcal F_{\widehat E}\widehat F_1)
\simeq M_{E^*}(\mathcal F_EF_2,\mathcal F_EF_1).
\qquad\text{(19)}
\]

The closed-embedding comparison permits every fixed normal covector, including \(-1\). Pull back (14) for \(\widehat E\) by \(a\), use the actual commuting equality \(\mathscr L_{\widehat E}a=b\mathscr L_E\) from (17), and apply (18)–(19). This proves (3) on all cotangent points. Naturality follows because the radial units, Fourier comparisons, support triangles, contact comparison and smooth/closed transport maps used throughout are natural in both inputs. In rank zero, Fourier transformation is also directly the identity over \(Z\), consistent with this stabilized proof. \(\square\)

## Exercises with complete solutions

### Why the original rotation is not a contact transformation

*Difficulty: Introductory.*

For a rank-one bundle over a point, compare \(\mathscr L(x;\lambda\xi)\) with ordinary cotangent dilation of \(\mathscr L(x;\xi)\). Explain where ordinary homogeneity reappears in the proof.

**Solution.** The first point is \((\lambda\xi;-x)\), while the second is \((\xi;-\lambda x)\). They generally have different base points. Thus (2) does not commute with ordinary cotangent dilation. On the ray spaces (11), scaling \((\zeta,\alpha)\) by positive \(\lambda\) leaves the ray \(\alpha/|\alpha|\) fixed and scales \((\zeta,\beta)\) by \(\lambda\). That map is ordinarily homogeneous and is the one to which the contact theorem applies. The two added coordinates give rank at least two, so this ray-space construction is available even for the original rank-one bundle.

### The two axes and their intersection

*Difficulty: Intermediate.*

At a point \((z,x;\zeta,\xi)\), allow \(x=0\), \(\xi=0\), or both. Write the stabilized input and output fibre components and explain why neither leaves the good regions.

**Solution.** The input base fibre is \((x,1,0)\) and its vertical covector is \((\xi,0,1)\). The output base fibre is \((\xi,0,1)\) and its vertical covector is \((-x,-1,0)\). Each has a displayed coordinate equal to \(1\) or \(-1\), so none is zero in any of the three cases. The base covector \(\zeta\) is unrestricted. Equations (18)–(19) recover the original microlocal Hom objects as entire inverse-image sheaves. Thus the proof covers both axes and their intersection; a punctured-region comparison alone would not do so.

### The radial degree over a nonorientable bundle

*Difficulty: Intermediate.*

Let \(B\) have rank \(m\ge2\) and possibly nontrivial orientation system \(O_B\). Calculate the coefficient and degree remaining in (8). Identify the fixed comparison that trivializes the coefficient.

**Solution.** The proper radial inverse kernel carries \(\omega_{S/Z}=\tau_S^{-1}O_B[m-1]\), with the positive radial direction placed first. Formula (9) adds the output-pulled \(O_{B^*}[-m]\). Projection along the relative sphere correspondence makes both lines pullbacks of base lines; their product is trivialized by the positive dual-basis pairing \(O_B\otimes O_{B^*}\to k\). Their degrees add to \(-1\). This is \(k[-1]\) with that particular comparison, even if each sign local system has nontrivial monodromy. Discarding either line before the pairing would lose the intrinsic normalization. The common degree cancels when both output arguments enter microlocal Hom.

### A conic sheaf that does not descend to real projective space

*Difficulty: Introductory.*

Take \(k\ne0\) and \(F=k_{[0,\infty)}\) on a real line. Is it conic? Is it invariant under multiplication by \(-1\)? Which direction quotient is allowed in (4)?

**Solution.** Its cohomology is constant on each positive scalar orbit: the positive ray carries \(k\), the negative ray carries zero, and the origin is a fixed orbit. Thus it is conic. The antipodal pullback is \(k_{(-\infty,0]}\), which has different stalks on both open rays and is not isomorphic to \(F\). The punctured positive-ray quotient has two points and distinguishes those coefficients. The quotient by all nonzero real scalars identifies the two rays and cannot represent them. The proof uses the former quotient throughout.

### A rank-one boundary checks both sides of Fourier exchange

*Difficulty: Advanced.*

Over a nonzero ring as in the theorem, let \(F=k_{[0,\infty)}\) on \(E=\mathbb R\). Use the negative kernel to identify \(\mathcal F_EF\). Check self microlocal Hom at \((0;\xi)\) for \(\xi>0\), and at \((x;0)\) for \(x>0\), against their images under (2).

**Solution.** If \(\xi>0\), the integrated slice of the closed positive ray is the point zero, with cohomology \(k\). If \(\xi\le0\), it is the full closed positive half-line, whose compact cohomology is zero. The open-support comparison therefore gives \(\mathcal F_EF=k_{(0,\infty)}\), with no shift. At the input boundary in a positive covector direction, the map from the closed ray to its endpoint sheaf is a microlocal isomorphism: its open-interior cone has only the opposite boundary direction. Thus self microlocal Hom is \(k\), with identity one. Its image \((\xi;0)\) lies in the interior of the output ray, where self microlocal Hom is also \(k\). At \((x;0)\), the input is locally the constant sheaf, so the same value is \(k\). Its image is \((0;-x)\), a negative boundary direction of the open positive ray. In that direction the triangle from open ray to closed ray to endpoint identifies the open ray with the endpoint sheaf shifted by \([-1]\), since the closed ray is null there. Self Hom cancels that shift and is again \(k\), with identity one. Both boundary signs and both distinct axis phenomena agree with (3).

### Why one stabilization coordinate is insufficient

*Difficulty: Intermediate.*

Compare adjoining only a point-supported real coordinate, tested at \((t=0,\tau=1)\), with adjoining only a constant real coordinate, tested at \((s=1,\sigma=0)\). Which original axis can still violate the good-region condition in each case? Explain the role of their common use.

**Solution.** The point coordinate makes the vertical covector \((\xi,1)\) nonzero, but its fibre base is \((x,0)\), which still vanishes when \(x=0\). The constant coordinate makes the fibre base \((x,1)\) nonzero, but its vertical covector \((\xi,0)\) still vanishes when \(\xi=0\). Their joint use makes both components nonzero simultaneously. Under Fourier exchange the point factor becomes a constant factor and the constant factor becomes point-supported with degree \(-1\), exactly as (15) specifies. The common shift cancels in the two Hom inputs. Each single-coordinate microlocal comparison is valid, but neither alone puts every original point into the angular contact region.
