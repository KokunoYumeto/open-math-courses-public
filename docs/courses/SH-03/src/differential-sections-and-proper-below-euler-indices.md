# Differential sections and proper-below Euler indices

A characteristic cycle gives a global Euler number when a differential section meets the microsupport in a compact set. On a noncompact manifold, the sublevels must also control escape of the support. Ordinary cohomology uses an ordinary direct image from an open sublevel. Compactly supported cohomology follows by duality and uses the opposite differential section. A strict local minimum then reads a stalk or a costalk.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The [supported section-intersection theorem](continuous-sections-and-supported-cycle-intersections.md#the-complete-supported-section-intersection-comparison) compares proper trace from the actual intersection with ordinary descent from the entire conic carrier. The [identity and evaluated microlocal trace](characteristic-cycles-from-supported-microlocal-identities.md#ordinary-restriction-and-the-unique-supported-trace), the [ordinary microlocal recovery](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-zero--two-recoveries-and-their-boundary-triangle), and the [closed-embedding adjunction comparison](closed-supports-and-evaluated-proper-transport.md#name-both-adjunctions-before-composing-their-maps) identify that descent with the base characteristic class. The [compact characteristic-class index](proper-characteristic-classes-and-the-compact-index.md#compact-support-gives-an-integer-index) then gives the compact case.

For noncompact support, the precise input is the ordinary open-cutoff map MO26+ in [Replacing a nonproper map by a bounded part](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-relative-cutoff--replacing-a-nonproper-map-by-a-bounded-part). Its [proof of the actual four cutoff maps](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-cutoff-proof--proof-of-the-four-cutoff-maps) retains properness on each closed support sublevel. The [ordinary open-boundary estimate](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-boundary--four-ways-to-impose-a-boundary) excludes the new negative boundary covectors from the positive differential graph. The [perfect internal-Hom calculation](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom) makes this ordinary cutoff a bounded constructible complex, although the open embedding need not be proper.

The compact-cohomology formula uses the [actual antipodal cycle comparison](antipodal-duality-and-half-line-characteristic-cycles.md#microlocalization-retains-the-coefficient-map-and-support), together with [dual section and point-measurement pairings](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#duality-exchanges-the-measurements-before-biduality). The local minimum argument uses the [isotropic discrete-critical-value theorem](../../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#direct-critical-set-proof) and its explicit subanalytic prerequisites. It then proves stabilization through the same open-cutoff map, before passing to the stalk.

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), Theorems 4.2–4.3, printed pp. 199–200, gives the proper-below ordinary and compact index formulas. Proposition 5.1 and Lemma 5.2, pp. 200–201, calculate a generic local test and its negative-Hessian degree; Theorem 8.3, p. 205, gives the strict-minimum stalk and costalk formulas. The paper writes an explicit ambient factor in its cycle convention. Here the section-first supported cup, evaluated microlocal identity and graph-normalized conormal coefficient determine the signs. The proof below derives the noncompact formulas through an ordinary open cutoff and keeps the minimum's stalk and costalk maps distinct.

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

The middle identification is the inverse of the exceptional unit \(u_B:B\to\delta^!\delta_*B\), where \(B=\delta^{-1}A_F\); it is invertible because the closed direct image is fully faithful. To identify the resulting map, let \(\varepsilon_{A_F}:\delta_*\delta^!A_F\to A_F\) be the exceptional counit and put \(b=\delta^{-1}\varepsilon_{A_F}:\delta^!A_F\to\delta^{-1}A_F\), using the ordinary closed counit on its source. Naturality of the ordinary unit gives \(\delta_*b=\eta_\delta\varepsilon_{A_F}\). Taking the exceptional adjoint of this equality gives \(u_B b=\delta^!\eta_\delta\). Consequently the first part of (4) is exactly \(b\), the exceptional-to-ordinary comparison defining the base characteristic class. This proves equality of the specified maps.

On the center-supported target, ordinary recovery is the inverse of the bundle unit \(\omega_X\to R\pi_*E\). Indeed specialization is supported on the zero normal vector, where the Fourier projection is the identity, and the closed-embedding adjunction cancels its unit with its counit. Thus the recovered map composed with the ordinary bundle unit is the identity. The [ordinary bundle-unit proof](continuous-sections-and-supported-cycle-intersections.md#proper-trace-and-ordinary-descent-have-different-domains) makes that unit invertible, fixing the bottom arrow as \(R\pi_*E\to\omega_X\). No compact Fourier recovery or added dimension sign is used here.

Put \(H=\mu\!hom(F,F)\). It is supported on the closed \(\Lambda\), so closed ordinary adjunction identifies it with the direct image of its restriction there and factors its unit uniquely as \(k_M\to k_\Lambda\to H\). Likewise the ordinary identity factors through \(k_D\), since \(R\mathcal Hom(F,F)\) vanishes off \(D\). Ordinary image of \(H\) vanishes off \(D\) as well: over any open set disjoint from \(D\), its inverse-image open set has zero input. Recovery therefore compares these supported identities, not only their images after forgetting support.

Explicitly, the microlocal route starts with \(k_D\to R\pi_*k_\Lambda\), adjoint to the closed-constant restriction \(\pi^{-1}k_D\to k_\Lambda\), then uses the factored unit, evaluated trace and inverse bundle unit. Naturality of recovery takes that composite to the factored ordinary identity followed by (4), which defines \(C(F)\). Equivalently, the trace square has sources supported on \(D\), and closed support adjunction lifts it uniquely to \(R\Gamma_D\omega_X\). Thus the two actual morphisms \(k_D\to\omega_X\) agree. This proves the first equality in (2); the section-intersection theorem supplies the second with its support enlargement \(J\subset D\).

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

At a supported point in this region, \(d\varphi_x\ne0\), since the zero covector belongs to the microsupport. If \(Q\subset I\) is compact, choose \(b\in I\) above its maximum. Then \(D\cap\varphi^{-1}(Q)\) is a closed subset of the compact \(D\cap\{\varphi\le b\}\). Thus \(\varphi|_D:D\to I\) is proper. The proof below still uses the stronger compactness of whole closed sublevels in (7); compactness of bands alone would allow escape toward the lower endpoint.

The written proper-below comparison has target \(\mathbb R\). Choose an increasing analytic diffeomorphism \(h:I\to\mathbb R\) and put \(\psi=h\varphi\). Use \(h(s)=s\) for \(I=\mathbb R\), \(h(s)=\log(s-\alpha)\) for \((\alpha,\infty)\), \(h(s)=-\log(\beta-s)\) for \((-\infty,\beta)\), and \(h(s)=\log((s-\alpha)/(\beta-s))\) for \((\alpha,\beta)\). Each has positive derivative and ranges over all of \(\mathbb R\). Since \(h'>0\), conicity gives

\[
 d\psi_x=h'(\varphi(x))d\varphi_x,\qquad
 d\psi_x\in\operatorname{SS}(F)
       \Longleftrightarrow d\varphi_x\in\operatorname{SS}(F).
 \qquad\text{(10)}
\]

This includes zero covectors. For every real \(b\), the closed \(\psi\)-sublevel on \(D\) equals \(D\cap\{\varphi\le h^{-1}(b)\}\) and is compact. For the map \(f:X\to\mathrm{pt}\), the horizontal covector space in MO25+ is zero. Equation (9), multiplied by the positive derivative in (10), is exactly that exclusion above the threshold \(h(a)\). All hypotheses of the actual ordinary open restriction MO26+ therefore hold; its output at \(h(t)>h(a)\) is

\[
 R\Gamma(X;F)\xrightarrow{\sim}R\Gamma(\Omega_t;F),\quad
 \Omega_t=\{\varphi<t\},\quad j_t:\Omega_t\hookrightarrow X,\quad
 F_t=Rj_{t*}j_t^{-1}F.
 \qquad\text{(11)}
\]

Direct-image composition identifies the target with \(R\Gamma(X;F_t)\). This is the specific open restriction map proved by one-sided propagation and proper-support control. It is not a claim that arbitrary ordinary sections commute with a closed exhaustion.

**Constructibility and compact support of the cutoff.** The open set \(\Omega_t\) is subanalytic, so \(k_{\Omega_t}=j_{t!}k\) is constructible. Actual open internal-Hom adjunction gives
\(R\mathcal Hom(k_{\Omega_t},F)=Rj_{t*}R\mathcal Hom(k,j_t^{-1}F)=F_t\).
The [perfect internal-Hom theorem](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom) therefore proves bounded constructibility and perfect stalks. The inclusion \(j_t\) need not be proper. Moreover

\[
 \operatorname{supp}(F_t)\subset\overline{D\cap\Omega_t}
              \subset D\cap\{\varphi\leq t\}.
 \qquad\text{(12)}
\]

To check the first inclusion, an open neighborhood disjoint from \(\overline{D\cap\Omega_t}\) has zero restricted input on its intersection with \(\Omega_t\), so every derived ordinary-image stalk there vanishes. The second inclusion uses closedness of \(D\) and continuity of \(\varphi\). The rightmost set is compact by (7). Applying compact finiteness to the entire bounded constructible complex \(F_t\), then using (11), proves the asserted ordinary finiteness.

**The positive graph avoids every new boundary covector.** On \(\Omega_t\), the canonical open restriction gives \(F_t=F\); outside the last set of (12), \(F_t\) vanishes locally. At a potential new intersection, \(x\in D\cap\{\varphi=t\}\), (9) gives \(d\varphi_x\ne0\). The local boundary is smooth, with strict-normal polar \(\mathbb R_{\leq0}d\varphi_x\). The ordinary open-boundary theorem requires that its opposite positive ray meet \(\operatorname{SS}(F)\) only at zero, on the whole local boundary under consideration. Shrink around \(x\) so the boundary remains smooth and \(\varphi>a\) there. Equation (9) and positive conicity exclude every nonzero positive multiple of \(d\varphi\) at all of those boundary points. At points outside \(D\), the input vanishes locally. The theorem therefore applies on this neighborhood and gives at its boundary

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

Apply (5) to compactly supported \(F_t\) and the original section \(\sigma_\varphi\). Their characteristic cycles agree on \(\pi^{-1}\Omega_t\), by the actual open restriction of the identity and trace. Both cups have the same compact support \(K_\varphi\) by (14), contained in that open set. Excision identifies the two classes in cohomology with this closed support, while open extension and trace composition identify their integrals. This is comparison at the actual compact intersection; no integral on all of the possibly noncompact \(D\) is introduced. With (11) this proves

\[
 \chi(X;F)=\chi(X;F_t)
 =\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F_t)\bigr)
 =\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(15)}
\]

All restriction maps to levels above \(a\) are isomorphisms by the same argument, and they commute with further open restriction. A single level inside \(I\) already proves (15), even when the upper endpoint is finite. Cofinal levels may approach that endpoint, but no passage of ordinary sections through an exhaustion is needed for the equality.

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

Constructible biduality gives the same closed support for \(D_XF\) and \(F\): local vanishing of one implies local vanishing of the other after applying duality twice. The actual swapped-kernel comparison, with its identity and evaluated coefficient, gives

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

No finiteness of the left input was assumed. Over a field, algebraic dualization is exact, so the degree-\(q\) cohomology of the left side is \(\operatorname{Hom}_k(H^{-q}R\Gamma_c(X;F),k)\). It detects nonzero vectors. If this dual is finite dimensional, its source embeds by evaluation into its finite-dimensional double dual and is itself finite dimensional. The finite range and finite dimensions supplied by the ordinary theorem on the right of (19) therefore imply both boundedness and finiteness of compact cohomology on the left. Dualization changes \(q\) to \(-q\), and \((-1)^{-q}=(-1)^q\); hence \(\chi_c(X;F)=\chi(X;D_XF)\). This proves the first equality of (17).

For the second, apply the diffeomorphism \(a\) to the supported cup, keeping the coefficient order \(P,E\). It takes the graph of \(\sigma_{-\varphi}\) to that of \(\sigma_\varphi\). The ordinary identification \(a^{-1}E=E\) is precisely the cycle action in (18). For the other factor, use \(a^{-1}P\simeq a^!P\simeq P\) with exceptional composition for \(\pi a=\pi\). The adjoint of the transformed section class is again \(1\), because the defining composition \(\pi a\sigma_{-\varphi}=\operatorname{id}_X\) has the same identity counit. It is therefore the actual class \([\sigma_\varphi]\).

Naturality of the exceptional tensor map sends this ordered product to the transformed dualizing class. Diffeomorphism trace followed by the point trace is the same point trace, by exceptional composition. The two compact supports correspond homeomorphically, so their numbers agree. In a fibre chart, the relative orientation map on \(P\) and the dualizing map include the fibre antipode sign \((-1)^{\dim X}\). These are already part of the compared maps and supply no additional scalar in (17).

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

Take the ball with closure contained in the neighborhood where \(\rho\) is defined, and regard both sets in (22) as carriers on that neighborhood. They are closed conic subanalytic isotropic sets: intersection with the closed base ball preserves subanalyticity and canonical-form vanishing. Their base projections are closed subsets of \(\overline B_R\), hence compact. The restriction of \(\rho\) to each such projection is therefore proper, which is exactly the support condition in the discrete-critical-value theorem. The two selected-value sets are locally finite in the ambient line. Choose \(\epsilon_0>0\) so neither has a value in \((0,\epsilon_0)\) and \(\epsilon_0<cR^2\).

Put \(U=B_R\cap\{\rho<\epsilon_0\}\), with \(\rho:U\to(-1,\epsilon_0)\). The closed support of \(F|_U\) is \(D\cap U\). For \(0\le s<\epsilon_0\), its closed sublevel equals the closed subset \(D\cap\overline B_R\cap\{\rho\le s\}\), since the lower quadratic bound keeps this set strictly inside \(B_R\). It is compact; negative sublevels are empty. If either signed differential belongs to the local microsupport at a point of \(U\), its selected value cannot lie in \((0,\epsilon_0)\). The unique zero of \(\rho\) is \(x_0\), so both intersections are contained in \(\{p_0\}\).

**Actual shrinking restrictions.** All sublevels in this paragraph are taken inside \(U\). For \(0<s'<s<\epsilon_0\), the actual open-cutoff map gives an isomorphism

\[
 R\Gamma(\{\rho<s\};F)\longrightarrow R\Gamma(\{\rho<s'\};F).
 \qquad\text{(23)}
\]

Here is a verification using precisely MO26+. Work on \(U_s=\{\rho<s\}\), and choose \(0<r<s'<s\). An increasing analytic diffeomorphism \(h_s:(-1,s)\to\mathbb R\) turns \(\rho|_{U_s}\) into a real-valued function with compact closed support sublevels. Above the threshold \(h_s(r)\), its positive differential avoids the microsupport because \(\rho>r>0\) and there are no selected positive values. MO26+ at \(h_s(s')\) is exactly the restriction (23). Thus every transition in this shrinking family is the specified quasi-isomorphism, and their compositions agree by ordinary restriction.

The quadratic bounds make \(U_s\) a neighborhood basis of zero: it contains a sufficiently small coordinate ball, and \(U_s\subset B_{\sqrt{s/c}}\). Choose a bounded-below injective resolution \(F\to I^\bullet\) on \(U\). Restriction to each open \(U_s\) is acyclic for sections, so \(\Gamma(U_s;I^\bullet)\) computes its derived sections. Their filtered colimit is the stalk complex \(I^\bullet_0\), degree by degree; exactness of filtered colimits of vector spaces makes its cohomology the corresponding colimit. This stalk complex represents \(F_0\). Because all transition maps (23) are quasi-isomorphisms, the canonical map from every \(R\Gamma(U_s;F)\) to \(F_0\) is a quasi-isomorphism. Apply (8) on any \(U_s\), with target interval \((-1,s)\); the checked closed sublevels remain compact and its only possible graph intersection is \(p_0\). This proves the first equality of (21).

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

Use the normalized rays of the [half-line calculation](antipodal-duality-and-half-line-characteristic-cycles.md#closed-and-open-half-lines-select-different-conormal-rays): \(\alpha_+\) is the positive-base part of \([T_X^*X]\), and \(\beta_\pm\) are the positive- and negative-covector parts of \([T_{\{0\}}^*X]\). The fixed normalization gives \(CC(A)=-\alpha_++\beta_+\) and \(CC(B)=-\alpha_+-\beta_-\). Both normalized horizontal and vertical chain generators are positive in their respective coordinates; the minus horizontal weight is the characteristic-cycle coefficient of the constant line. Each row has zero boundary at the crossing.

A constant nonzero section misses the zero section. At its smooth point-fibre intersection, the section unit followed by the normalized closed point trace has number \(+1\), for either section sign. The fibre-ray weights therefore give positive-section numbers \(1,0\) and negative-section numbers \(0,-1\). These agree with (25). The zero-stalk endpoint of \(B\) remains in its closed support.

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

The supported base-class comparison gives the continuous compact index, the two proper-below differential indices, and the minimum stalk and costalk formulas. For a general analytic phase, an isolated microlocal intersection instead measures the supported test \(R\Gamma_{\{\varphi\geq\varphi(x_0)\}}F\). The next lesson establishes this local formula using a radial cutoff with explicit positive-phase and boundary-exclusion estimates.
