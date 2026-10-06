# Nonproper holomorphic pushforwards through cutoffs

A nonproper direct image can be constructible when all changes along its fibres occur below a fixed level. The hypothesis is a relative condition on the differential of an exhaustion. It yields four actual comparison maps, with different directions for ordinary and proper supports. A closed cutoff can include the threshold itself; an open cutoff cannot. Complex cotangent symmetry makes the two signed hypotheses coincide, while a separate real coefficient argument proves perfection.

Let \(k\) be a commutative ring of finite global dimension. Manifolds are Hausdorff, countable at infinity and of uniformly bounded finite dimension, and all sheaf complexes are globally bounded. Let \(f:Y\to X\) be holomorphic between complex manifolds, and let \(\varphi:Y\to\mathbb R\) be real analytic. Fix \(t_0\in\mathbb R\). For a weakly complex constructible \(G\), write \(\Lambda=\operatorname{SS}(G)\), using the real-part identification of complex and real cotangent bundles. We use the actual closed complex analytic, complex-conic Lagrangian \(\Lambda\), as proved in Complex microlocal stratifications and constructibility.

The application treated here belongs to the theory of direct images of \(\mathbb C\)-constructible sheaves under non-proper maps; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §4.4 and §8.6. The real cutoff proof and boundary estimates come from the microlocal foundations. We explain their maps, support arguments, endpoints and sharp threshold estimate, then prove the complex and perfect-coefficient conclusions. The general ordinary geometric bound holds with inclusions; equality fails in general, as the comparison below shows.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## The closed level and the horizontal covectors

Define

\[
Y_t=\{y:\varphi(y)<t\},\qquad Z_t=\{y:\varphi(y)\leq t\},\qquad
j_t:Y_t\hookrightarrow Y,\quad i_t:Z_t\hookrightarrow Y.
\qquad\text{(1)}
\]

Set \(f_t=fj_t\) and \(\bar f_t=fi_t\). Here \(Z_t\) is the closed sublevel, and it need not equal \(\overline{Y_t}\). Nor need \(Z_t\) be a manifold. We interpret its sheaves as sheaves on the closed topological subspace, or use their closed direct images on \(Y\).

The horizontal space at \(y\) is

\[
V_{f,y}=\{(df_y)^t\xi:\xi\in T^*_{f(y)}X\}\subset T_y^*Y.
\qquad\text{(2)}
\]

It is complex-linear even when the rank of \(df\) changes; the collection need not be a vector subbundle. The transpose is complex-linear, with no conjugation. Real covectors are identified by \(\rho(\eta)(v)=\operatorname{Re}\eta(v)\). In particular, if \(\ell_y=\rho^{-1}(d\varphi_y)\), then \(\ell_y(v)=d\varphi_y(v)-i\,d\varphi_y(iv)\).

The two hypotheses are

\[
\operatorname{supp}(G)\cap Z_t\longrightarrow X
\text{ is proper for every }t\in\mathbb R,
\qquad\text{(3)}
\]

and

\[
d\varphi_y\notin\Lambda_y+V_{f,y}
\quad\text{whenever }\varphi(y)>t_0.
\qquad\text{(4)}
\]

The sum in (4) is the ordinary fibrewise sum. No closure, limiting sum, or replacement of \(\Lambda\) by an arbitrary large bound occurs in this condition. Formula (3) is relative properness of every support sublevel, not absolute properness of \(\varphi\), and not properness only for one chosen level. The support is the closed support, including its limit points with zero stalk.

Both \(\Lambda_y\) and \(V_{f,y}\) are invariant under multiplication by \(-1\). Therefore their sum is invariant under \(-1\), and (4) also gives

\[
-d\varphi_y\notin\Lambda_y+V_{f,y}
\quad(\varphi(y)>t_0).
\qquad\text{(5)}
\]

This is the reason the ordinary and supported cutoff theorems apply together. It is independent of Verdier duality and of coefficient perfection. For a submersion the condition can be written in the relative cotangent bundle: the class of \(d\varphi_y\) avoids the image of \(\Lambda_y\) in \(T_y^*Y/V_{f,y}\). For a general map this remains a fibrewise quotient statement, without asserting a quotient vector bundle.

## Four maps, with their endpoint rules

Under (3)–(4), the natural maps in the following table are isomorphisms. The letters match the four map assertions in the referenced real theorem.

| Source assertion | Natural map | Allowed level |
| --- | --- | --- |
| (a), ordinary open restriction | \(Rf_*G\longrightarrow R(f_t)_*j_t^{-1}G\) | \(t>t_0\) |
| (a′), ordinary closed restriction | \(Rf_*G\longrightarrow R(\bar f_t)_*i_t^{-1}G\) | \(t\geq t_0\) |
| (c), open proper-support extension | \(R(f_t)_!j_t^{-1}G\longrightarrow Rf_!G\) | \(t>t_0\) |
| (c′), closed supported counit | \(R(\bar f_t)_*i_t^!G\longrightarrow Rf_!G\) | \(t\geq t_0\) |

The first two maps come from the restriction units \(G\to Rj_{t*}j_t^{-1}G\) and \(G\to i_{t*}i_t^{-1}G\). The third comes from the open counit \(j_{t!}j_t^{-1}G\to G\), followed by \(Rf_!\). The fourth uses \(i_{t*}i_t^!G\to G\). On its support, \(\bar f_t\) is proper by (3), so its proper direct image equals its ordinary direct image. This explains the star in the fourth row. It does not turn \(i_t^!\) into \(i_t^{-1}\), or reverse the counit.

The two microsupport assertions, (b) and (d), give

\[
\operatorname{SS}(Rf_*G)\subset D_0,
\qquad \operatorname{SS}(Rf_!G)\subset D_0,
\qquad\text{(6)}
\]

where

\[
\begin{split}
D_0&=f_\pi f_d^{-1}\bigl(\Lambda\cap\pi_Y^{-1}(Z_{t_0})\bigr)\\
&=\{(x,\xi):\text{some }y\in Z_{t_0},\ f(y)=x,
\ (y,(df_y)^t\xi)\in\Lambda\}.
\end{split}
\qquad\text{(7)}
\]

Here \(f_d(y,\xi)=(y,(df_y)^t\xi)\) and \(f_\pi(y,\xi)=(f(y),\xi)\). The zero covectors are retained in both maps. The bound uses the original \(\Lambda\) over the threshold closed sublevel, rather than the microsupport of a cutoff sheaf with new boundary normals.

Both \(Rf_*G\) and \(Rf_!G\) are weakly complex constructible. If \(G\) has perfect stalks, both outputs have perfect stalks and are complex constructible. We prove the four maps and (6) first, then the two additional claims.

## A proper map to a cylinder

The useful intermediate map is

\[
h=(f,\varphi):Y\longrightarrow X\times\mathbb R,
\qquad q:X\times\mathbb R\longrightarrow X,
\qquad H=Rh_*G=Rh_!G.
\qquad\text{(8)}
\]

The equality defining \(H\) holds because \(h\) is proper on \(\operatorname{supp}(G)\). Indeed, a compact set in \(X\times\mathbb R\) has compact base projection and an upper bound \(b\) for its second coordinate. Its supported inverse image is a closed subset of the compact inverse image of that base projection in \(\operatorname{supp}(G)\cap Z_b\). This proves properness without assuming \(f\) proper.

Composition and proper base change identify \(Rf_*G\) with \(Rq_*H\), and \(Rf_!G\) with \(Rq_!H\). They identify the open and closed cutoff objects in the table with the corresponding ordinary, open proper-support and closed supported images of \(H\) below the level \(t\). For the last identification use exceptional proper base change: the restriction with supports to \(X\times(-\infty,t]\) corresponds to \(i_t^!G\), rather than ordinary restriction. These statements concern derived complexes and their natural maps.

The proper microsupport estimate for \(h\) says that a possible covector \((x,s;\xi,\sigma)\) of \(H\) lifts to a point \(y\) satisfying \(f(y)=x\), \(\varphi(y)=s\), and

\[
(df_y)^t\xi+\sigma\,d\varphi_y\in\Lambda_y.
\qquad\text{(9)}
\]

If \(s>t_0\) and \(\sigma>0\), division by the positive real number \(\sigma\) in (9) contradicts (4): \(\Lambda\) is positively conic and \(V_f\) is a vector space. Thus the positive exclusion forces \(\sigma\leq0\) on the upper cylinder. The negative exclusion similarly forces \(\sigma\geq0\). In our complex situation both hold, so every covector of \(H\) above \(t_0\) has vertical component zero. The two one-sided statements are still useful separately because they identify the directions of the maps.

## One-sided continuation and the closed threshold

We spell out the real continuation argument used in (8). Its precise one-sided convex continuation theorem and boundary estimates are the current foundation contracts. This proof does not use duality of infinite coefficient modules.

Suppose first that \(\operatorname{SS}(H)\) has \(\sigma\leq0\) for \(s>t_0\). Let \(W\) be a small convex coordinate neighborhood in \(X\), and let \(t>t_0\). One-sided convex continuation gives

\[
R\Gamma(W\times(t_0,\infty);H)
\xrightarrow{\sim}
R\Gamma(W\times(t_0,t);H).
\qquad\text{(10)}
\]

The two intervals have the same saturation in the allowed increasing vertical direction; an increasing change of the vertical coordinate retains the sign condition. Cover \(W\times\mathbb R\) by \(W\times(-\infty,t)\) and \(W\times(t_0,\infty)\). Their intersection is \(W\times(t_0,t)\). Derived Mayer–Vietoris and (10) show that restriction to the lower open part is an isomorphism. Such neighborhoods \(W\) form a basis, proving the ordinary open row of the table as a sheaf isomorphism.

For the ordinary closed row fix \(x\in X\), \(t\geq t_0\), and \(b>t\). The supported part of the closed fibre \(\{x\}\times(-\infty,t]\) is compact. For a compact base neighborhood, properness of the support below \(b\) implies that sets \(W\times(-\infty,u)\), with \(W\ni x\) shrinking and \(t<u<b\) decreasing to \(t\), are cofinal neighborhoods of this compact supported fibre. Otherwise an escaping sequence could be chosen in that one compact sublevel; a subsequence would converge into the fibre and contradict the prescribed neighborhood.

Compact-neighborhood continuity identifies the filtered colimit of their cohomology with cohomology of the closed fibre. Proper base change on the closed sublevel identifies this with the closed-cutoff stalk. Each full-to-open comparison in the system is already an isomorphism, since \(u>t_0\). Its colimit proves the closed comparison, including \(t=t_0\). Both shrinking base neighborhoods and compact supported sublevels are essential; no unbounded half-strip is being treated as compact.

For the supported rows use the opposite sign \(\sigma\geq0\). When \(t_0<t<t'\), one-sided continuation in the decreasing direction and the localization triangle give

\[
R\Gamma_{W\times(-\infty,t]}(W\times\mathbb R;H)
\xrightarrow{\sim}
R\Gamma_{W\times(-\infty,t']}(W\times\mathbb R;H).
\qquad\text{(11)}
\]

The difference is the band \((t,t']\). On \(W\times(t,\infty)\), ordinary restriction to \(W\times(t',\infty)\) is an isomorphism because these upper tails have the same decreasing saturation in that domain. The fibre of this restriction is the supported band term, so it vanishes. This proves (11).

The filtered colimit over these closed support cutoffs computes \(Rq_!H\). Locally over a compact base set, a support proper over the base is compact and hence bounded above in its vertical coordinate. Conversely the intersection with any closed sublevel is proper over the base by (3). This is cofinality of the actual proper-support families. Finite cohomological dimension permits their filtered-colimit calculation on bounded resolutions. Thus the closed supported comparison is an isomorphism for \(t>t_0\).

At \(t=t_0\) use localization and the increasing union of upper tails \(\{s>t_0\}=\bigcup_{t>t_0}\{s>t\}\). On a flabby resolution these sections are calculated by the inverse-limit complex with termwise surjective restrictions. The cohomology systems of the supported cutoffs are already constant; the localization triangle identifies the upper-tail systems accordingly. Their derived-limit obstruction vanishes. Taking fibres proves the closed supported comparison at \(t_0\). Finally an open cutoff is the union of smaller closed support cutoffs. If \(t>t_0\), these contain cofinally many levels above \(t_0\), proving the open extension row. If \(t=t_0\), this last argument has no such levels, which explains the strict endpoint in the open rows.

## Removing the new boundary covectors

For the ordinary case choose \(t>t_0\) and extend the ordinary open cutoff of \(H\) by \(Rj_*\). Its support lies below the closed level \(t\) and is proper over \(X\). Near the new boundary the horizontal conormal transversality holds because \(H\) has no nonzero vertical covector there. More generally the one-sided cutoff proof uses the open boundary estimate under its signed exclusion. Every new vertical boundary normal of this ordinary extension is nonpositive; preexisting upper-tail vertical covectors are also nonpositive. A sum with vertical component zero therefore has both vertical components zero. The proper estimate for \(q\) gives

\[
\operatorname{SS}(Rq_*H)\subset
\{(x,\xi): (x,s;\xi,0)\in\operatorname{SS}(H)
\text{ for some }s\leq t\}.
\qquad\text{(12)}
\]

For the exceptional case use the closed supported cutoff. Its new boundary normal and every preexisting relevant vertical component are nonnegative. Their sum can again be zero only if both are zero. The same bound (12) follows for \(Rq_!H\). Below the boundary there is no added normal; at the boundary this no-cancellation argument removes the possible added directions. This step is why the final estimate is sharper than simply applying a proper image theorem to an arbitrary real cutoff coefficient.

Apply (9) with \(\sigma=0\) to lift (12) into \(\Lambda\) at a point of \(Z_t\). Fix \((x,\xi)\) in the microsupport of either output and let \(t\downarrow t_0\). All its lifting points lie in one compact supported fibre sublevel, using any fixed \(t_1>t_0\). A subsequence converges to \(y\) with \(f(y)=x\) and \(\varphi(y)\leq t_0\). Its lifted covectors are exactly \((df_y)^t\xi\), so continuity of \(df\) and closedness of \(\Lambda\) give membership in \(\Lambda\) at the limit. This proves (6)–(7), including all zero-transpose and critical-differential cases.

## Complex geometry of the threshold image

The set

\[
B_0=\{(y,\xi):\varphi(y)\leq t_0,
\ (y,(df_y)^t\xi)\in\Lambda\}
\subset Y\times_X T^*X
\qquad\text{(13)}
\]

is closed subanalytic. The level inequality is real analytic and the cotangent correspondence is holomorphic. On this actual set, \(f_\pi\) is proper. To check this, let \(K\subset T^*X\) be compact. Its base projection is compact. The \(y\)-coordinates in \(f_\pi^{-1}(K)\cap B_0\) belong to \(\operatorname{supp}(G)\cap Z_{t_0}\), whose inverse image of that compact base projection is compact by (3). Pairing this with \(\xi\in K\) and using closedness proves compactness. We used \(\pi_Y\Lambda=\operatorname{supp}(G)\), including the zero covectors. Thus \(D_0=f_\pi(B_0)\) is closed subanalytic.

The real cotangent transport theorem proves that this image is isotropic: restrict the original closed isotropic \(\Lambda\) to the closed subanalytic base region, pull through the differential correspondence, and take the proper supported cotangent image. Real analyticity of the level inequality supplies the needed subanalyticity; it does not assert that the cutoff is complex analytic.

For \(\lambda\in\mathbb C^*\),

\[
(df_y)^t(\lambda\xi)=\lambda(df_y)^t\xi.
\qquad\text{(14)}
\]

The original \(\Lambda\) is complex-conic, and the inequality in (13) depends only on \(y\). Hence \(B_0\), and therefore \(D_0\), is complex-conic. This direct argument works even though \(D_0\) was only proved subanalytic. The complex constructibility criterion from the preceding lessons applies to the closed complex-conic subanalytic isotropic bound (6). It proves weak complex constructibility of both outputs once boundedness is established. The source coefficient cutoffs themselves need only be real constructible.

## Boundedness and perfect coefficients through real cutoffs

The closed ordinary and supported coefficients on the ambient manifold are

\[
P_t=i_{t*}i_t^{-1}G\simeq G\overset L\otimes k_{Z_t},
\qquad Q_t=i_{t*}i_t^!G\simeq R\Gamma_{Z_t}G
\simeq R\mathcal Hom(k_{Z_t},G).
\qquad\text{(15)}
\]

The extension \(k_{Z_t}\) is perfect real constructible. Locally finite real subanalytic stratifications adapted to the level set exist; its stalks are either \(k\) or zero. It is generally not complex constructible. The weak real tensor/Hom results give bounded weak real constructibility of \(P_t\) and \(Q_t\). They give global amplitude bounds using the fixed real dimension and finite global dimension of \(k\), rather than a bound chosen separately at every point.

Both objects are supported in \(\operatorname{supp}(G)\cap Z_t\). Thus \(f\) is proper on their supports. The real proper direct-image theorem gives bounded weak real constructible \(Rf_*P_t\) and \(Rf_*Q_t\). The closed rows of the table identify them with \(Rf_*G\) and \(Rf_!G\), respectively, for every \(t\geq t_0\). This proves the boundedness required by the complex microsupport criterion.

If \(G\) has perfect stalks, the real perfect tensor theorem proves the stalks of \(P_t\) perfect. The real perfect internal Hom theorem proves the same for \(Q_t\). The latter assertion uses the actual constructible Hom theorem; it does not replace a local supported complex by the algebraic Hom of the two ordinary stalks. Finally Perfect coefficients on compact fibres gives perfect stalks of their proper images, including singular compact level fibres. Combining this with the already proved complex geometry gives the perfect conclusion.

These arguments preserve arbitrary commutative finite-global-dimension coefficients and do not assume Noetherianity. They also prove the weak version for infinite coefficient modules. No weak biduality or infinite dual-tensor evaluation formula is needed.

## The printed extra geometric equality

The general real Proposition 5.4.17(b) contains an equality between the threshold geometric image and the unrestricted geometric image. Its first microsupport inclusion is the bound used above. The additional geometric equality does not hold for arbitrary real sheaves under its positive signed hypothesis. Exercise 6 gives the exact half-open interval calculation, with both support properness and the positive exclusion checked. The current foundation proof retains

\[
\operatorname{SS}(Rf_*G)\subset D_0
\subset f_\pi f_d^{-1}(\operatorname{SS}(G)).
\qquad\text{(16)}
\]

The second relation here is always the set inclusion from restricting the base level. The exceptional printed bound already uses that inclusion. We do not infer a stronger equality for complex inputs from the failed general real assertion, or claim that the real counterexample is complex constructible. The complex and perfect conclusions proved here require only (6), so their proof is unaffected.

## Exercises

### 1. The threshold point in a complex disc
*Difficulty: Introductory.*

Let \(Y=\mathbb C\), \(X=\mathrm{pt}\), \(G=k_Y\), \(\varphi(z)=|z|^2\) and \(t_0=0\). Check the hypotheses and calculate all four cutoff complexes, including their closed endpoint. Explain why the open formulas cannot include \(t=0\).

**Solution.** Every closed support sublevel is a compact disc, a point, or the empty set, so (3) holds. The microsupport of \(k_Y\) is the zero section, and the horizontal space for a map to a point is zero. The differential of \(|z|^2\) is nonzero for \(z\neq0\), exactly outside the threshold. Thus (4) holds. Ordinary cohomology of \(\mathbb C\), an open disc and a nonempty closed disc is \(k\) in degree zero. At the closed endpoint the ordinary restriction is to the point \(0\), with cohomology \(k\). All ordinary comparisons are therefore isomorphisms in their stated ranges.

The complex orientation of \(\mathbb C\) has real dimension two, so \(R\Gamma_c(\mathbb C;k)=k[-2]\); the same is true for any nonempty open disc. For a closed disc, the supported complex \(R\Gamma_{Z_t}(\mathbb C;k)\) also equals \(k[-2]\). One can calculate it from the localization triangle: the complement retracts onto a circle, and the restriction from \(\mathbb C\) is an isomorphism on degree-zero cohomology, leaving the circle's degree-one class in degree two of the fibre. At \(t=0\), \(i_0^!k_Y=k[-2]\), the real two-dimensional point costalk. Its closed direct image has that same global complex. Thus the supported closed endpoint also works. The natural orientation class supplies the supported comparison isomorphisms. By contrast \(Y_0=\varnothing\). Both its ordinary and proper-support complexes vanish, whereas the full complexes \(k\) and \(k[-2]\) do not for \(k\neq0\). This verifies the strict open endpoint and the difference between ordinary restriction and closed supports.

### 2. Proper levels over a noncompact base
*Difficulty: Intermediate.*

Let \(f:\mathbb C_w\times\mathbb C_z\to\mathbb C_w\) be projection, \(G=k\), and \(\varphi(w,z)=|z|^2\). Verify relative properness and horizontal exclusion with \(t_0=0\). Compute both direct images and their threshold bound. Does \(\varphi\) have to be proper on the whole source?

**Solution.** The inverse image of a compact base set in a closed level is its product with a compact disc, or with a point or the empty set. This is compact, proving relative properness for every real level. The zero-section microsupport plus the horizontal space consists of multiples of \(dw\). Under the real-part cotangent identification, \(d|z|^2\) corresponds to \(2\bar z\,dz\). It is horizontal precisely when \(z=0\), so the exclusion holds outside the threshold. For \((w,\xi)\), its pullback is \((\xi,0)\); membership in the zero section forces \(\xi=0\). The threshold image (7) is therefore exactly the zero section of \(T^*\mathbb C_w\).

Product cohomology or the cutoff comparisons give \(Rf_*k=k_{\mathbb C_w}\) and \(Rf_!k=k_{\mathbb C_w}[-2]\). The compact-support shift is the real dimension of the fibre, with its canonical complex orientation. Their microsupports are the predicted zero section and their stalks are perfect. The source function is not proper absolutely: the inverse image of any nonnegative compact interval contains arbitrarily large \(w\). Relative compactness over compact base sets is exactly the needed condition.

### 3. A closed sublevel is not the closure of its open companion
*Difficulty: Introductory.*

Take \(f:\mathbb C\to\mathrm{pt}\), \(G=k_{\{0\}}\), and \(\varphi\equiv0\), with \(t_0=0\). Determine the open and closed sublevels at the threshold, check all hypotheses, and calculate the four rows.

**Solution.** Here \(Y_0=\varnothing\), so \(\overline{Y_0}=\varnothing\), while \(Z_0=\mathbb C\). This is already a strict difference. For negative levels the supported sublevel is empty, and for nonnegative levels it is the compact support \(\{0\}\). Thus every supported sublevel is proper to a point. No point has \(\varphi>t_0\), so the differential exclusion is vacuous; it does not require \(d\varphi\neq0\) at the threshold.

The full ordinary and proper-support images of the skyscraper are both \(k\). For \(t>0\) both cutoff spaces equal \(\mathbb C\), and all four maps are identities on the full object. At \(t=0\) the closed embedding is the identity of \(\mathbb C\), so its ordinary and exceptional restrictions both leave \(G\) unchanged. The two closed comparisons are still identities. The open cutoff at \(0\) is empty and gives zero, so the open comparisons fail at the endpoint for \(k\neq0\). Replacing the closed sublevel by the closure of the open sublevel would therefore falsify the theorem.

### 4. Real cutoff coefficients, complex outputs
*Difficulty: Intermediate.*

In the projection of Exercise 2, fix \(t>0\). Explain why the ambient coefficient \(P_t=k_{\mathbb C_w\times\{|z|^2\leq t\}}\) is generally only real constructible. Why can its proper direct image nevertheless be complex constructible? Compare its coefficient argument with that for \(Q_t=R\Gamma_{\{|z|^2\leq t\}}k\).

**Solution.** Near a boundary point with \(|z|^2=t\), the closed disc has a smooth real hypersurface boundary. The closed-halfspace local calculation gives a nonzero one-sided real conormal ray in \(\operatorname{SS}(P_t)\). This ray is not stable under multiplication by \(i\), or even by \(-1\), so the complex constructibility criterion fails for the source coefficient. Its cohomology is still real constructible, and every stalk is \(k\) or zero. The real tensor theorem therefore supplies perfection of \(P_t\).

The proper image of \(P_t\) is the ordinary cohomology of the closed-disc fibres and equals \(k_{\mathbb C_w}\). Its complex cotangent bound is obtained from the original zero-section \(\Lambda\) at \(z=0\), not by declaring the real boundary ray complex-conic. The cylinder proof shows why no extra boundary direction survives horizontal projection. For \(Q_t\), the real supported/Hom theorem gives a bounded perfect real constructible coefficient, and the proper image is \(k_{\mathbb C_w}[-2]\). Ordinary stalkwise Hom alone cannot calculate its boundary or central supported complexes. Once their real perfection is established, (6) gives weak complex constructibility of both images, and hence their full perfect complex constructibility.

### 5. Infinite weak coefficients survive the cutoff proof
*Difficulty: Intermediate.*

Let \(k\) be a field and \(M=\bigoplus_{j\geq1}k\). Replace the constant sheaf in Exercise 1 by the constant sheaf \(M_Y\). Verify the weak conclusions and explain precisely where the perfect conclusion fails. Is biduality required by the proof?

**Solution.** The constant sheaf \(M_Y\) is globally bounded and weakly complex constructible: its microsupport is the zero section. The same compact-disc sublevels and differential exclusion apply. Ordinary cohomology of \(\mathbb C\) or a disc is \(M\); compactly supported cohomology of the oriented real two-dimensional fibre is \(M[-2]\). The finite topological cell calculations and the cutoff continuation work for these coefficient modules, so both direct images to a point are bounded and weakly complex constructible. At a point this merely says their cohomology is an allowed coefficient module.

The vector space \(M\) is infinite-dimensional, so it is not a perfect complex over the field. Consequently neither \(M\) nor \(M[-2]\) has perfect stalks, and no perfect conclusion follows. The proof uses signed continuation, real bounded Hom with the finite cutoff sheaf, and proper supports; it never identifies \(M\) with its algebraic double dual or uses an infinite dual-tensor evaluation formula. Complex cotangent geometry and perfect coefficients are distinct requirements here.

### 6. A strict geometric inclusion in the real theorem
*Difficulty: Advanced.*

Assume \(k\neq0\). Let \(f:\mathbb R\to\mathrm{pt}\), \(\varphi(s)=s\), \(G=k_{(0,1]}\), and \(t_0=-1\). Check the positive relative exclusion and support properness. Calculate ordinary cohomology, the threshold geometric image and the unrestricted geometric image. Give the corresponding exceptional example. What does this comparison establish about the complex theorem?

**Solution.** The closed support of \(G\) is \([0,1]\), so every support sublevel is compact. At the open endpoint \(0\) the microsupport ray is the nonpositive multiples of \(ds\); at the closed endpoint \(1\) its outward convention again gives the nonpositive multiples of \(ds\). At interior points it is the zero covector. Since the horizontal space for the point map is zero, \(d\varphi=ds\) is excluded from this microsupport everywhere, in particular above \(-1\). The triangle

\[
k_{(0,1]}\longrightarrow k_{[0,1]}\longrightarrow k_{\{0\}}
\xrightarrow{+1}
\]

gives ordinary cohomology zero: the two right global complexes are \(k\), and their restriction is the identity. The threshold region \(s\leq-1\) misses the closed support, so its geometric image is empty. The full geometric image contains the zero cotangent fibre of the point, since every interior point of the interval supplies a zero covector. That fibre is a singleton, so the image is precisely that singleton. The inclusion between the two geometric images is strict, while the actual output microsupport is empty and satisfies the threshold bound.

For the exceptional case use \(G'=k_{[0,1)}\). Its endpoint rays are nonnegative multiples of \(ds\), so the negative exclusion holds. The triangle removing the endpoint \(1\) from the closed compact interval gives \(R\Gamma_c(\mathbb R;G')=0\); compact global sections of the closed interval restrict identically to that endpoint. Its threshold image is again empty and its full geometric image the singleton. These are real sheaves with one-sided cotangent rays. They disprove the stronger general real geometric equality, not a separate complex-input equality: the rays are not complex-conic and the source is not a complex manifold. For the complex theorem we have proved the sufficient inclusions, with no stronger image equality inferred from the printed general claim.

### 7. An exhaustion bounded above on the chosen source
*Difficulty: Advanced.*

For \(f:\mathbb C\to\mathrm{pt}\) and \(G=k\), restrict the source to \(V=\{|z|^2<R^2\}\), where \(R>0\). Can the restricted function \(\varphi=|z|^2\) satisfy (3)? Replace it by \(\psi=(R^2-|z|^2)^{-1}\), calculate its closed levels and differential, and find a valid threshold.

**Solution.** For any \(u\geq R^2\), the closed \(\varphi\)-sublevel in \(V\) is all of the open disc \(V\), which is not compact. Thus the restricted bounded-above function fails the hypothesis requiring every support sublevel proper. Compactness of the smaller levels does not repair this failure.

The new function is positive and real analytic on \(V\). If \(u<1/R^2\), its closed sublevel is empty. If \(u\geq1/R^2\), the inequality is equivalent to

\[
|z|^2\leq R^2-1/u,
\]

which is a compact disc strictly inside \(V\); at equality \(u=1/R^2\) it is the point \(0\). Every finite level is therefore compact. Moreover

\[
d\psi=(R^2-|z|^2)^{-2}\,d|z|^2.
\]

The factor is positive and nowhere zero. Thus the signed differential exclusions remain the same, and \(t_0=1/R^2\) is valid. The theorem recovers ordinary cohomology \(k\) and compactly supported cohomology \(k[-2]\) of \(V\), with the closed endpoint at its centre. This repair enforces all levels, rather than just the one compact band used to choose the source neighborhood. In a relative application the same algebra gives a finite closed level contained in an earlier proper relative sublevel, provided that level remains a closed supported subset there; this is the role of the reparameterization in the later complex-curve application.

## Proof obligations and the next application

The lesson proves the four typed cutoff comparisons, their strict and nonstrict endpoints, the original-microsupport threshold bound, weak complex constructibility and the separate perfect-stalk conclusion. It relies on current exact real one-sided continuation, support-family base change, boundary estimates and cotangent transport, together with the previously proved real compact-fibre and complex constructibility applications. The next application must construct neighborhoods over a complex curve with these exact hypotheses; that requires the unbounded horizontal-covector argument, one-variable Laurent orders and all-level exhaustion repair, rather than invoking nonproper constructibility without a cutoff.
