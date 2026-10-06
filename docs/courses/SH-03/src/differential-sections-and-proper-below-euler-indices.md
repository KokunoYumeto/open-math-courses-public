# Differential sections and proper-below Euler indices

A characteristic cycle gives a global Euler number when a differential section meets the microsupport in a compact set. On a noncompact manifold, the sublevels must also control escape of the support. Ordinary cohomology uses an ordinary direct image from an open sublevel. Compactly supported cohomology follows by duality and uses the opposite differential section. A strict local minimum then reads a stalk or a costalk.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

This lesson treats index formulas for differential sections and proper-below Euler indices, the local form of the index theorem of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §4. Use Continuous sections and supported cycle intersections for the supported section class, proper trace and full section-intersection diagram; Characteristic cycles from supported microlocal identities for the actual kernel unit and evaluated trace; Proper characteristic classes and the compact index for compact finiteness and the characteristic-class integral; and Antipodal duality and half-line characteristic cycles for the normalized antipodal map and Verdier cycle duality.

The exact written SH-02 prerequisites are Four ways to impose a boundary, Replacing a nonproper map by a bounded part and its one-parameter mechanism, including the full cutoff proof and finite-band Morse comparisons. SH-02 owns these proofs. The course's constructible duality supplies the actual stalk/costalk pairing. The minimum argument uses the isotropic discrete-critical-value theorem, relative to its recorded subanalytic foundations. Lower and transitive proof closure and independent review remain open.

## Recovering the base class from the microlocal trace

Let \(X\) be real analytic, Hausdorff and countable at infinity, with the standing finite uniform dimension bound. Let \(k\) be a field of characteristic zero and \(F\in D^b_{\mathbb R\text{-c}}(k_X)\), with finite perfect stalks. Set

\[
 M=T^*X,\quad \pi:M\to X,\quad
 \Lambda=\operatorname{SS}(F),\quad D=\operatorname{supp}(F)=\pi\Lambda,\quad
 E=\pi^{-1}\omega_X.
 \qquad\text{(1)}
\]

Supports in (1) are closed; a boundary point with zero stalk can remain in the support. The section coefficient is \(P=\pi^!k_X\), and its ordered cup with \(E\) has coefficient \(\omega_M\).

For a continuous section \(\sigma:X\to M\), put \(J=\sigma^{-1}\Lambda\) and \(K=\sigma(X)\cap\Lambda\). The graph is closed, and projection identifies \(K\) homeomorphically with the closed set \(J\). The proper supported trace \(\alpha_K\) therefore exists even when \(J\) is noncompact. We claim

\[
 C(F)=\beta_\pi\bigl(\operatorname{CC}(F)\bigr)
     =\iota_{J,D}\,\alpha_K\bigl([\sigma]\cap\operatorname{CC}(F)\bigr)
       \quad\text{in }H^0_D(X;\omega_X).
 \qquad\text{(2)}
\]

Here \(\beta_\pi\) uses the inverse ordinary unit \(\omega_X\to R\pi_*E\); \(\iota_{J,D}\) enlarges the closed support. The final equality is the previously proved supported section-intersection theorem. We establish the first equality through the actual trace maps.

Let \(\delta:X\hookrightarrow X^2\) be the diagonal and \(A_F=F\boxtimes D_XF\). Exceptional external-Hom comparison gives \(\delta^!A_F=R\mathcal Hom(F,F)\). Its identity unit is the adjoint of the particular kernel map \(u_F:k_{\Delta_X}\to A_F\). Diagonal microlocalization sends this to \(e_F:k_M\to\mu\!hom(F,F)\); ordinary recovery sends this specific unit back to \(\operatorname{id}_F\).

The evaluated kernel map is

\[
 A_F\xrightarrow{\eta_\delta}\delta_*\delta^{-1}A_F
 =\delta_*(F\otimes D_XF)
 \xrightarrow{\delta_*t_F}\delta_*\omega_X,\qquad
 t_F=\operatorname{ev}\circ\text{graded symmetry}.
 \qquad\text{(3)}
\]

Naturality of ordinary recovery in (3) takes the microlocal trace \(\mu\!hom(F,F)\to E\) to

\[
 \delta^!A_F\xrightarrow{\delta^!\eta_\delta}
 \delta^!\delta_*\delta^{-1}A_F
 \simeq\delta^{-1}A_F\xrightarrow{t_F}\omega_X.
 \qquad\text{(4)}
\]

The middle identification is the exceptional counit for the closed embedding. Thus the first part of (4) is precisely the exceptional-to-ordinary diagonal comparison defining the base characteristic class. On the center-supported target, recovery is the inverse ordinary unit \(R\pi_*E\to\omega_X\): composition with its unit is the identity because the zero-normal Fourier projection is the identity. This fixes the actual bottom arrow.

The endomorphism and diagonal objects are supported on \(D\), and the microlocal Hom is supported on \(\Lambda\). Restrict the recovery square to these closed supports and apply support adjunction. The supported identity and microlocal unit correspond because the unrestricted recovery already takes the particular identity to itself. Unique lifting from a supported source retains this square before forgetting support. In the microlocal route, the map \(k_D\to R\pi_*k_\Lambda\) is adjoint to closed-constant restriction \(\pi^{-1}k_D\to k_\Lambda\), the first arrow defining \(\beta_\pi\). In the base route, (4) on that supported identity defines \(C(F)\). These two morphisms \(k_D\to\omega_X\) agree. This proves (2) with its unit, ordinary restriction, exceptional comparison, graded evaluation and output support.

If \(D\) is compact, then \(J\subset D\) is compact and \(K=\sigma(J)\) is compact. Constructible compact finiteness makes \(R\Gamma(X;F)\) a bounded finite complex. The compact characteristic-class index and composition of the \(\pi\) and point traces yield

\[
 \chi(X;F)=\int_XC(F)
          =\#\bigl([\sigma]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(5)}
\]

Neither smoothness of \(\sigma\) nor a transverse or discrete intersection is required. The number is the dualizing trace of the supported cup, including when its support has positive dimension.

## Compact sublevels and a compact critical intersection

Let \(I\subset\mathbb R\) be an open interval and \(\varphi:X\to I\) real analytic. Write

\[
 \sigma_\varphi(x)=(x;d\varphi_x),\quad
 L_\varphi=\sigma_\varphi(X),\quad
 K_\varphi=L_\varphi\cap\operatorname{SS}(F).
 \qquad\text{(6)}
\]

Assume

\[
 D\cap\{\varphi\leq t\}\text{ is compact for every }t\in I,
 \qquad K_\varphi\text{ is compact}.
 \qquad\text{(7)}
\]

Then ordinary global cohomology is bounded and finite dimensional and

\[
 \chi(X;F)=\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(8)}
\]

Both hypotheses are needed: the first concerns every closed support sublevel, and the second the full microsupport, including zero covectors. We prove finiteness and the equality together.

**Choose a level inside the target interval.** The values \(\varphi(\pi K_\varphi)\) form a compact subset of \(I\). Choose \(a<t\) in \(I\) with \(a\) greater than all these values; if the intersection is empty, take any \(a<t\) in \(I\). Then

\[
 d\varphi_x\notin\operatorname{SS}(F)\quad
                 \text{whenever }\varphi(x)>a.
 \qquad\text{(9)}
\]

At a supported point in this region, \(d\varphi_x\ne0\), since the zero covector belongs to the microsupport. Every closed compact band in \(I\) has compact inverse image on \(D\) by (7), so \(\varphi|_D:D\to I\) is proper.

The written proper-below comparison has target \(\mathbb R\). Choose an increasing analytic diffeomorphism \(h:I\to\mathbb R\) and put \(\psi=h\varphi\). An affine map suffices for \(I=\mathbb R\), a logarithm for a half-line, and \(\log((s-\alpha)/(\beta-s))\) for \((\alpha,\beta)\). Since \(h'>0\), conicity gives

\[
 d\psi_x=h'(\varphi(x))d\varphi_x,\qquad
 d\psi_x\in\operatorname{SS}(F)
       \Longleftrightarrow d\varphi_x\in\operatorname{SS}(F).
 \qquad\text{(10)}
\]

This includes zero covectors. Its real closed sublevels on \(D\) are exactly the compact original sublevels. Apply the actual SH-02 proper-below ordinary restriction theorem with \(f:X\to\mathrm{pt}\), whose horizontal covector space is zero, and threshold \(h(a)\). It gives

\[
 R\Gamma(X;F)\xrightarrow{\sim}R\Gamma(\Omega_t;F),\quad
 \Omega_t=\{\varphi<t\},\quad j_t:\Omega_t\hookrightarrow X,\quad
 F_t=Rj_{t*}j_t^{-1}F.
 \qquad\text{(11)}
\]

Direct-image composition identifies the target with \(R\Gamma(X;F_t)\). This is the specific open restriction map proved by one-sided propagation and proper-support control. It is not a claim that arbitrary ordinary sections commute with a closed exhaustion.

**Constructibility and compact support of the cutoff.** The open set \(\Omega_t\) is subanalytic, so \(k_{\Omega_t}=j_{t!}k\) is constructible. Actual open internal-Hom adjunction gives
\(R\mathcal Hom(k_{\Omega_t},F)=Rj_{t*}R\mathcal Hom(k,j_t^{-1}F)=F_t\).
The perfect internal-Hom theorem therefore proves bounded constructibility and perfect stalks. The inclusion \(j_t\) need not be proper. Moreover

\[
 \operatorname{supp}(F_t)\subset\overline{D\cap\Omega_t}
              \subset D\cap\{\varphi\leq t\}.
 \qquad\text{(12)}
\]

The rightmost set is compact. Applying compact finiteness to \(F_t\) and then (11) proves the asserted ordinary finiteness.

**The positive graph avoids every new boundary covector.** On \(\Omega_t\), the canonical open restriction gives \(F_t=F\); outside the last set of (12), \(F_t\) vanishes locally. At a potential new intersection, \(x\in D\cap\{\varphi=t\}\), (9) gives \(d\varphi_x\ne0\). The local boundary is smooth, with strict-normal polar \(\mathbb R_{\leq0}d\varphi_x\). The ordinary open-boundary theorem requires avoidance of its opposite positive ray by \(\operatorname{SS}(F)_x\). Condition (9) and conicity provide exactly that requirement. Thus at this boundary

\[
 \operatorname{SS}(F_t)_x\subset\operatorname{SS}(F)_x+
                                      \mathbb R_{\leq0}d\varphi_x.
 \qquad\text{(13)}
\]

If \(d\varphi_x=p+c\,d\varphi_x\), with \(p\in\operatorname{SS}(F)_x\) and \(c\leq0\), then \(p=(1-c)d\varphi_x\). Since \(1-c>0\), conicity contradicts (9). Therefore

\[
 L_\varphi\cap\operatorname{SS}(F_t)=K_\varphi
                           \subset\pi^{-1}\Omega_t.
 \qquad\text{(14)}
\]

Inside the open set this is canonical restriction; outside it, (12)–(13) exclude intersections. Replacing \(Rj_*\) with \(j_!\) would give the other added normal sign and would not supply this proof.

Apply (5) to compactly supported \(F_t\) and the original section \(\sigma_\varphi\). Characteristic cycles agree on \(\Omega_t\), and the actual compact intersection in (14) lies there. Supported cup, open extension and trace composition consequently identify their numbers. With (11) this proves

\[
 \chi(X;F)=\chi(X;F_t)
 =\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F_t)\bigr)
 =\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(15)}
\]

A bounded interval causes no difficulty: one chooses a level inside it above the compact critical-value set and takes a cofinal approach to its upper endpoint.

## Compact cohomology uses the opposite section

Keep the first hypothesis of (7), but replace the second by

\[
 L_\varphi\cap\operatorname{SS}(F)^a\text{ is compact},
 \qquad a(x;\xi)=(x;-\xi).
 \qquad\text{(16)}
\]

Then compact cohomology is bounded and finite dimensional, and

\[
 \chi_c(X;F)
 =\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)^a\bigr)
 =\#\bigl([\sigma_{-\varphi}]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(17)}
\]

The proper-below hypothesis remains on \(\varphi\). We do not impose that hypothesis on \(-\varphi\); instead we apply the ordinary theorem to the dual.

Constructible duality gives the same closed support for \(D_XF\) and \(F\), and

\[
 \operatorname{SS}(D_XF)=\operatorname{SS}(F)^a,\qquad
 \operatorname{CC}(D_XF)=\operatorname{CC}(F)^a.
 \qquad\text{(18)}
\]

Thus (8) applies to \(D_XF\) and proves finiteness of its ordinary global complex. Actual global duality gives

\[
 R\operatorname{Hom}_k(R\Gamma_c(X;F),k)
                         \simeq R\Gamma(X;D_XF).
 \qquad\text{(19)}
\]

No finiteness of the left input was assumed. Over a field, algebraic dualization is exact and detects nonzero vectors. A vector space whose dual is finite dimensional embeds in its finite-dimensional double dual and is finite dimensional itself. Equation (19) thus proves finite compact cohomology in finitely many degrees. Dualization reverses degree and preserves the alternating sum, so \(\chi_c(X;F)=\chi(X;D_XF)\). This proves the first equality of (17).

For the second, apply the diffeomorphism \(a\) to the supported cup. It takes the graph of \(\sigma_{-\varphi}\) to that of \(\sigma_\varphi\). Exceptional composition for \(\pi a=\pi\) takes the section's normalized unit \(1\) to \(1\), while \(E=\pi^{-1}\omega_X\) has its canonical ordinary antipodal identification. Exceptional tensor comparison takes the ordered cup to the corresponding antipodal cup, and composition of diffeomorphism and point traces preserves its number. In coordinates the relative fibre-orientation factor and dualizing transformation both contain \((-1)^{\dim X}\); those factors already belong to these actual maps. No additional dimension sign is appended to (17).

## A strict minimum reads a stalk and a costalk

Let \(x_0\in X\) and let \(\rho\) be real analytic near it, with

\[
 \rho(x_0)=0,\qquad d\rho_{x_0}=0,\qquad
                         \operatorname{Hess}_{x_0}\rho>0.
 \qquad\text{(20)}
\]

After restriction to a sufficiently small neighborhood, both the \(d\rho\) and \(-d\rho\) graph intersections with the microsupport are contained in \(\{p_0\}\), where \(p_0=(x_0;0)\). An empty local intersection has number zero. Then

\[
 \chi(F_{x_0})=\#\bigl([\sigma_\rho]\cap\operatorname{CC}(F)\bigr)_{p_0},
 \qquad
 \chi(i_{x_0}^!F)=\#\bigl([\sigma_{-\rho}]\cap\operatorname{CC}(F)\bigr)_{p_0}.
 \qquad\text{(21)}
\]

The second input is the ambient point costalk, which can differ from the ordinary stalk.

**Isolation and compact sublevels.** Choose analytic coordinates \(x_0=0\) and a small closed coordinate ball \(\overline B_R\). Positive Hessian and Taylor's formula give \(c|x|^2\leq\rho(x)\leq C|x|^2\) there, for positive \(c,C\), with no other zero. Apply the isotropic discrete-critical-value theorem to

\[
 \Lambda\cap\pi^{-1}\overline B_R,\qquad
                  \Lambda^a\cap\pi^{-1}\overline B_R.
 \qquad\text{(22)}
\]

These are closed conic subanalytic isotropic carriers: the singular-form subset criterion preserves isotropy. Their base projections are compact, so the required properness holds for \(\rho\). The two sets of selected values are locally finite near zero. Choose \(\epsilon_0>0\) with neither having a value in \((0,\epsilon_0)\) and with \(\epsilon_0<cR^2\). Set \(U=B_R\cap\{\rho<\epsilon_0\}\), with \(\rho:U\to(-1,\epsilon_0)\). Its closed support sublevels are compact: for \(s<\epsilon_0\), the lower quadratic bound keeps them strictly inside \(B_R\). Both graph intersections in \(T^*U\) are contained in \(\{p_0\}\).

**Actual shrinking restrictions.** For \(0<s'<s<\epsilon_0\), the finite-band Morse theorem gives an isomorphism

\[
 R\Gamma(\{\rho<s\};F)\longrightarrow R\Gamma(\{\rho<s'\};F).
 \qquad\text{(23)}
\]

There is no positive differential in the microsupport on the intervening band, and the closed bands on the support are compact. An increasing interval-to-line change realizes the exact stated properness requirement of the provider. The quadratic bounds make these sublevels a neighborhood basis of zero. Stalks are exact filtered colimits; on a bounded resolution their section complexes therefore have colimit \(F_0\). Since (23) is already an isomorphism, every such section complex maps isomorphically to \(F_0\). Apply (8) on one sublevel with the interval having that upper endpoint. Its only possible intersection is \(p_0\), proving the first equality of (21).

The same argument applies to \(D_XF\) using the second carrier of (22). The actual constructible point pairing gives

\[
 (D_XF)_0\simeq R\operatorname{Hom}_k(i_0^!F,k).
 \qquad\text{(24)}
\]

The costalk is perfect, so its Euler number equals that of its dual. Equations (18) and the normalized antipodal number comparison prove the second equality of (21). This uses actual restrictions and the costalk pairing; no transversality at the zero covector is assumed.

## Exercises with complete solutions

### Closed and open rays have different compact indices

*Difficulty: Intermediate.*

On \(X=\mathbb R_t\), take \(\varphi(t)=t\). Verify the hypotheses for \(A=k_{[0,\infty)}\) and \(B=k_{(0,\infty)}\) as ambient sheaves. Compute their ordinary and compact section complexes and the two section numbers.

**Solution.** Both closed supports are \([0,\infty)\), so the closed sublevels are empty or compact intervals. The microsupport of \(A\) is the positive-base zero section with nonnegative covectors at zero; that of \(B\) has nonpositive covectors there. The graph \(dt\) meets the first only at \((0;dt)\) and misses the second. The graph \(-dt\) misses the first and meets the second only at \((0;-dt)\). All four intersections are compact.

Constant closed-ray cohomology gives \(R\Gamma(X;A)=k\). In the actual triangle \(B\to A\to k_0\xrightarrow{+1}\), the ordinary global restriction \(k\to k\) is the identity, so \(R\Gamma(X;B)=0\). Duality \(D_XA=B[1]\) and the actual global pairing give \(R\Gamma_c(X;A)=0\). Compact sections of that same triangle give \(R\Gamma_c(X;B)=k[-1]\). Thus

\[
 \chi(A)=1,\quad\chi_c(A)=0,\qquad
                         \chi(B)=0,\quad\chi_c(B)=-1.
 \qquad\text{(25)}
\]

The cycles are the positive-base zero-section chamber plus the positive point-fibre ray for \(A\), and that chamber minus the negative point-fibre ray for \(B\). A constant nonzero section misses the zero section. At its smooth fibre-ray intersection, the normalized full-point-conormal number is \(+1\); the cycle's weight gives positive-section numbers \(1,0\) and negative-section numbers \(0,-1\). These agree with (25). The zero-stalk endpoint of \(B\) remains in its closed support.

### Compact intersection alone does not control escape

*Difficulty: Intermediate.*

Keep \(A=k_{[0,\infty)}\), but use \(\varphi(t)=-t\). Compute the graph intersection and ordinary Euler number, and locate the failed hypothesis.

**Solution.** The section \(-dt\) misses both the zero section and nonnegative point-fibre ray, so its intersection number is zero. Yet \(R\Gamma(X;A)=k\), of ordinary index one. For every \(s\), the support sublevel is \([\max(0,-s),\infty)\), which is noncompact. The proper-below condition is false. The empty graph intersection cannot eliminate contributions escaping along noncompact sublevels; (12) supplies no compact cutoff here. This is not an application of the ordinary theorem with a different sign.

### A zero cycle can coexist with infinite global cohomology

*Difficulty: Advanced.*

Let \(Z=\{0,1,2,\ldots\}\), \(i:Z\hookrightarrow\mathbb R\), \(P=k\oplus k[1]\) constant on its isolated points, and \(F=i_*P\). Use \(\varphi(t)=t\). Verify constructibility and below-properness, then compute the cycle, full microsupport intersection and ordinary cohomology.

**Solution.** The point family is closed and locally finite. Each neighborhood has a finite subanalytic stratification with perfect point coefficients and uniformly bounded degrees \(-1,0\). Hence \(F\) is bounded R-constructible. Every closed sublevel contains finitely many support points and is compact.

Each point-conormal coefficient is \(\chi(P)=1-1=0\), so locally finite cycle gluing gives \(\operatorname{CC}(F)=0\). The localized point object \(P\) is nonzero, however, so the full cotangent fibre over every integer belongs to the microsupport. The graph intersection is \(\{(m;dt):m\in Z\}\), which is noncompact. Thus the second hypothesis of (7) fails.

Ordinary sections on a discrete space are products, an exact functor on vector spaces. Consequently

\[
 H^0(X;F)=\prod_{m\geq0}k,\qquad H^{-1}(X;F)=\prod_{m\geq0}k.
 \qquad\text{(26)}
\]

Both groups are infinite dimensional. Their alternating dimensions do not define an Euler number by cancellation. The zero cup of a zero cycle does not prove the theorem's missing finiteness conclusion; its hypothesis deliberately concerns the full microsupport.

### A bounded phase interval still has cofinal upper levels

*Difficulty: Intermediate.*

Let \(X=(-1,\infty)_t\), \(A=k_{[0,\infty)}\) on \(X\), and \(\varphi(t)=t/(1+t)\) with target \(I=(-\infty,1)\). Check (7), exhibit \(h:I\to\mathbb R\) increasing and analytic, and calculate both indices.

**Solution.** The derivative is \((1+t)^{-2}>0\). For \(s<0\) the support sublevel is empty; for \(0\leq s<1\) it is \([0,s/(1-s)]\), compact in \(X\). The positive differential graph meets the microsupport only at zero with covector \(dt\); the antipodal comparison is empty. The ray computations give ordinary index \(1\) and compact index \(0\).

Take \(h(s)=-\log(1-s)\); then \(h\varphi(t)=\log(1+t)\). It is an increasing analytic diffeomorphism onto the line, with positive derivative. Conicity preserves differential membership. A sufficiently high level is any \(s\in(0,1)\); cofinal levels approach \(1\) from below. The actual restriction in (11) is to \(t<s/(1-s)\), and the ordinary boundary adds negative multiples of \(dt\). The positive graph avoids those new directions. Thus both index theorems apply despite the bounded-above target interval.

### A minimum separates stalks from costalks

*Difficulty: Advanced.*

Near zero in the ambient line, take \(\rho(t)=t^2\), \(A=k_{[0,\infty)}\) and \(B=k_{(0,\infty)}\). Compute both point measurements and deduce the local positive- and negative-minimum numbers. Explain the singular intersection at \((0;0)\).

**Solution.** The stalks are \(A_0=k\) and \(B_0=0\). For \(A\), sections on a punctured small interval come from its positive component and give \(k\). The full-to-punctured restriction is the identity \(k\to k\), so the support triangle gives \(i_0^!A=0\). Apply \(i_0^!\) to \(B\to A\to k_0\xrightarrow{+1}\); since \(i_0^!k_0=k\), it yields \(i_0^!B=k[-1]\).

The positive-minimum numbers in (21) are \(1,0\); the negative-minimum numbers are \(0,-1\). The graph \(d\rho=2t\,dt\) meets the positive-base zero section only at zero; it can meet a point-fibre piece only there, also with zero covector. The opposite graph has the same isolated base point. These are frontier intersections of the crossing's pieces, not transverse intersections of smooth nonzero rays. The supported cup and isolated-point trace remain defined and distinguish the two costalks.

### Finite graded coefficients preserve two different global indices

*Difficulty: Advanced.*

Put \(P=k^2\oplus k[1]\) and \(F=k_{[0,\infty)}\otimes_kP\oplus k_0[1]\) on the ambient line, with zero coefficient differentials. Use \(\varphi(t)=t\). Compute both global complexes and section numbers. Does zero ordinary Euler number make the ordinary complex zero?

**Solution.** Finite constant tensor coefficients and finite sums commute with the section maps. The closed-ray ordinary complex is \(k\) and its compact complex is zero, so

\[
 R\Gamma(X;F)=P\oplus k[1]=k^2\oplus k^2[1],\qquad
                              R\Gamma_c(X;F)=k[1].
 \qquad\text{(27)}
\]

The indices are \(0,-1\). The ordinary complex is nonzero, with two-dimensional cohomology in degrees zero and \(-1\).

The cycle weight of \(P\) is \(2-1=1\); the shifted point contributes minus the normalized full point conormal. Hence
\(\operatorname{CC}(F)=\operatorname{CC}(k_{[0,\infty)})-[T_0^*X]\).
The positive section meets the closed-ray fibre with number \(1\) and the subtracted point fibre with number \(-1\), totaling zero. The negative section meets only the latter, giving \(-1\). The support sublevels are compact and both full microsupport graph intersections are singletons. Finite graded cancellation does not identify ordinary and compact indices or kill the ordinary global complex.

## The next local index problem

The supported base-class comparison, continuous compact index, both proper-below differential indices and minimum stalk/costalk formulas are now proved relative to their named prerequisites. A general analytic phase need not have a minimum. Its isolated microlocal intersection measures the supported test \(R\Gamma_{\{\varphi\geq\varphi(x_0)\}}F\). That assertion requires a radial cutoff with explicit positive-phase and boundary-exclusion estimates, and remains a subsequent teaching target.
