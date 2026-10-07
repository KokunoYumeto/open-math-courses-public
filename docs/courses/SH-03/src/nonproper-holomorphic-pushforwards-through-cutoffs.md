# Nonproper holomorphic pushforwards through cutoffs

A nonproper direct image can be constructible when all changes along its fibres occur below a fixed level. The hypothesis is a relative condition on the differential of an exhaustion. It yields four actual comparison maps, with different directions for ordinary and proper supports. A closed cutoff can include the threshold itself; an open cutoff cannot. Complex cotangent symmetry makes the two signed hypotheses coincide, while a separate real coefficient argument proves perfection.

Let \(k\) be a commutative ring of finite global dimension. Manifolds are Hausdorff, countable at infinity and of uniformly bounded finite dimension, and input sheaf complexes are globally bounded. Let \(f:Y\to X\) be holomorphic between complex manifolds. The cutoff \(\varphi:Y\to\mathbb R\) may be real analytic; more generally, the same theorem holds for a \(C^2\) subanalytic function with subanalytic differential. The graph argument below proves the needed microsupport estimate at this regularity. Fix \(t_0\in\mathbb R\). For a weakly complex constructible \(G\), write \(\Lambda=\operatorname{SS}(G)\), using the real-part identification of complex and real cotangent bundles. We use the actual closed complex analytic, complex-conic Lagrangian \(\Lambda\), as proved by the four equivalent geometric tests.

The theorem includes the zero coefficient ring. In examples asserting a nonempty microsupport or a nonperfect infinite free module, take \(k\neq0\).

Kashiwara and Schapira develop nonproper cutoff direct images in [*Microlocal study of sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Theorem 4.4.1, printed pp. 73–75. Their Proposition 8.6.1, printed p. 154, gives the complex-constructible application. We organize the argument around the four natural maps and their endpoint rules, then recover the threshold microsupport bound and the separate perfect-coefficient assertion.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

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

Under (3)–(4), the natural maps in the following table are isomorphisms. The two restriction maps and the two support-forgetting maps have the following exact ranges.

| Cutoff operation | Natural map | Allowed level |
| --- | --- | --- |
| Ordinary open restriction | \(Rf_*G\longrightarrow R(f_t)_*j_t^{-1}G\) | \(t>t_0\) |
| Ordinary closed restriction | \(Rf_*G\longrightarrow R(\bar f_t)_*i_t^{-1}G\) | \(t\geq t_0\) |
| Open proper-support extension | \(R(f_t)_!j_t^{-1}G\longrightarrow Rf_!G\) | \(t>t_0\) |
| Closed supported counit | \(R(\bar f_t)_*i_t^!G\longrightarrow Rf_!G\) | \(t\geq t_0\) |

The first two maps come from the restriction units \(G\to Rj_{t*}j_t^{-1}G\) and \(G\to i_{t*}i_t^{-1}G\). The third comes from the open counit \(j_{t!}j_t^{-1}G\to G\), followed by \(Rf_!\). The fourth uses \(i_{t*}i_t^!G\to G\). On its support, \(\bar f_t\) is proper by (3), so its proper direct image equals its ordinary direct image. This explains the star in the fourth row. It does not turn \(i_t^!\) into \(i_t^{-1}\), or reverse the counit.

The same continuation also bounds both output microsupports by the original covectors at the threshold:

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

Composition and proper-support base change identify \(Rf_*G\) with \(Rq_*H\), and \(Rf_!G\) with \(Rq_!H\). They identify the open and closed cutoff objects in the table with the corresponding ordinary, open proper-support and closed supported images of \(H\) below \(t\). In the supported closed case use the first, invertible comparison in exceptional base change, (EX.17), with the exceptional map the closed inclusion of the cylinder sublevel. Together with closed support as \(i_*i^!\), (EX.15), this gives \(i_t^!G\), with its support-forgetting counit. This is distinct from the second comparison in (EX.17), which need not be invertible for closed base change.

These operations are already defined in the bounded-below category. In fact \(H\) is bounded: if \(G\in D^{[a,b]}\) and \(d=\dim_{\mathbb R}Y\), every fibre of \(h\) is closed in \(Y\); closed extension and the compact-support dimension bound (M3) give fibre cohomological dimension at most \(d\). The proper-support fibre formula therefore puts \(Rh_!G\) in \(D^{[a,b+d]}\). This uses no constructibility of \(H\) under the possibly nonanalytic map \(h\).

Here is the promised regularity check. For a \(C^1\) diffeomorphism \(u\), composing the \(C^1\) support tests (T1)–(T3) with \(u\) identifies their support complexes. The chain rule sends their differentials by \((du)^t\); this is a homeomorphism of cotangent bundles and carries whole testing neighborhoods to whole testing neighborhoods. Applying the same argument to \(u^{-1}\) proves exact covariance of microsupport, not just a test at one differential.

In coordinates factor \(h\) as its closed graph \(\gamma_h:Y\to Y\times(X\times\mathbb R)\), followed by the smooth projection \(p\). The \(C^2\) coordinate change \((y,z)\mapsto(y,z-h(y))\) makes that graph the flat zero section. Its closed-embedding microsupport formula, transported by the preceding \(C^1\) calculation, says that a graph covector \((\alpha,\beta)\) occurs exactly when \(\alpha+(dh_y)^t\beta\in\Lambda_y\). The projection \(p\) is proper on the graph coefficient's support because \(h\) is proper there. Apply the smooth proper-image estimate to \(p\): an output covector pulls back to \((0,\beta)\), and hence requires \((dh_y)^t\beta\in\Lambda_y\). Thus the usual proper microsupport estimate applies to our \(C^2\) cylinder map as well. No analytic direct-image constructibility assertion for \(h\) enters this argument.

The proper microsupport estimate for \(h\) says that a possible covector \((x,s;\xi,\sigma)\) of \(H\) lifts to a point \(y\) satisfying \(f(y)=x\), \(\varphi(y)=s\), and

\[
(df_y)^t\xi+\sigma\,d\varphi_y\in\Lambda_y.
\qquad\text{(9)}
\]

If \(s>t_0\) and \(\sigma>0\), division by the positive real number \(\sigma\) in (9) contradicts (4): \(\Lambda\) is positively conic and \(V_f\) is a vector space. Thus the positive exclusion forces \(\sigma\leq0\) on the upper cylinder. The negative exclusion similarly forces \(\sigma\geq0\). In our complex situation both hold, so every covector of \(H\) above \(t_0\) has vertical component zero. The two one-sided statements are still useful separately because they identify the directions of the maps.

## One-sided continuation and the closed threshold

The one-parameter continuation proof, (MO28)–(MO30), derives the two signs from derived open convex continuation, (G6). We apply its actual restriction maps, then prove the two closed endpoints by different limit arguments. No duality of infinite coefficient modules is used.

Suppose first that \(\operatorname{SS}(H)\) has \(\sigma\leq0\) for \(s>t_0\). Let \(W\) be a small convex coordinate neighborhood in \(X\), and let \(t>t_0\). One-sided convex continuation gives

\[
R\Gamma(W\times(t_0,\infty);H)
\xrightarrow{\sim}
R\Gamma(W\times(t_0,t);H).
\qquad\text{(10)}
\]

The two intervals have the same saturation in the allowed increasing vertical direction; an increasing change of the vertical coordinate retains the sign condition. Cover \(W\times\mathbb R\) by \(W\times(-\infty,t)\) and \(W\times(t_0,\infty)\). Their intersection is \(W\times(t_0,t)\). Derived Mayer–Vietoris and (10) show that restriction to the lower open part is an isomorphism. Such neighborhoods \(W\) form a basis, proving the ordinary open row of the table as a sheaf isomorphism.

For the ordinary closed row put \(L=\operatorname{supp}(H)\), fix \(x\in X\) and \(t\geq t_0\), and choose \(b>t\). The support \(L\) has proper closed sublevels: it is contained in the closed image under \(h\) of \(\operatorname{supp}(G)\), and (3) bounds every inverse image over a compact base set. Thus \(K_t=L\cap(\{x\}\times(-\infty,t])\) is compact. Choose a relatively compact base neighborhood \(V\) of \(x\). All points of \(L\cap(\overline V\times(-\infty,b])\) lie in one compact set.

The sets \(L\cap(W\times(-\infty,u))\), where \(W\subset V\) shrinks to \(x\) and \(t<u<b\) decreases to \(t\), are cofinal neighborhoods of \(K_t\) in \(L\). Indeed, if a neighborhood \(N\) of \(K_t\) contained none of them, choose points outside \(N\) whose bases tend to \(x\) and whose heights are at most \(t+1/n\). The preceding compact set supplies a convergent subsequence. Its limit is in \(K_t\) and outside \(N\), a contradiction. This also covers \(K_t=\varnothing\).

For precision, compact-neighborhood continuity here is a derived assertion on that actual compact set. Regard \(H\) as a complex on its closed support \(L\) and use an injective resolution there. Each term is flabby, hence c-soft; its restriction to the closed compact \(K_t\) is c-soft and acyclic for sections, by the compact-support resolution facts. Sections on \(K_t\) are the filtered colimit of sections on its neighborhoods: a finite cover represents all germs and a further finite shrinking makes the representatives agree, as in the compact-neighborhood argument preceding (G5). Exactness of filtered module colimits now gives the same assertion for cohomology. Thus

\[
\mathop{\mathrm{colim}}_{W\ni x,\ u\downarrow t}
R\Gamma(W\times(-\infty,u);H)
\simeq R\Gamma(K_t;H|_{K_t}).
\]

The right side is the closed-cutoff stalk by proper-support base change, since this cutoff is proper on its support. The colimit of \(R\Gamma(W\times\mathbb R;H)\) is the full ordinary image stalk. The comparison between them is the colimit of the actual restriction maps already proved invertible for every \(u>t_0\). It is therefore the ordinary closed restriction isomorphism, including \(t=t_0\). Both the compact supported sublevel and the shrinking base neighborhood are essential; an unbounded half-strip itself has not been declared compact.

For the supported rows use the opposite sign \(\sigma\geq0\). When \(t_0<t<t'\), one-sided continuation in the decreasing direction and the localization triangle give

\[
R\Gamma_{W\times(-\infty,t]}(W\times\mathbb R;H)
\xrightarrow{\sim}
R\Gamma_{W\times(-\infty,t']}(W\times\mathbb R;H).
\qquad\text{(11)}
\]

The difference is the band \((t,t']\). On \(W\times(t,\infty)\), ordinary restriction to \(W\times(t',\infty)\) is an isomorphism because these upper tails have the same decreasing saturation in that domain. The fibre of this restriction is the supported band term, so it vanishes. This proves (11).

To pass from (11) to proper supports, let \(Z_t'=X\times(-\infty,t]\) in the cylinder. There is a natural sheaf-level comparison

\[
\mathop{\mathrm{colim}}_{t\to+\infty}Rq_*R\Gamma_{Z_t'}H
\longrightarrow Rq_!H.
\]

It is an isomorphism by local cofinality of supports. A section over an open base \(W\) with support proper over \(W\) has compact support over every compact subset of \(W\). Shrinking around any base point to \(W'\Subset W\), its support over \(\overline{W'}\) is compact and hence bounded above in height. Conversely a closed support contained in \(L\cap Z_t'\) is proper over the base. On an injective resolution on \(L\), extended by the closed inclusion into the cylinder, the closed-support subcomplexes compute \(R\Gamma_{Z_t'}H\); their terms are injective, by the adjunctions for a closed inclusion. The resolution also computes proper image by the proper-support fibre and acyclicity proof. The local cofinality just proved identifies the filtered colimit term by term as sheaves, and filtered colimits are exact. This proves the comparison with its support-forgetting maps. It does not assert one uniform height bound for every section over a noncompact \(W\). Together with (11), it proves the closed supported row for \(t>t_0\).

The supported endpoint requires an inverse limit instead. Fix \(W\) and set \(A=R\Gamma(W\times\mathbb R;H)\), \(B_t=R\Gamma(W\times(t,\infty);H)\), and \(C_t=R\Gamma_{W\times(-\infty,t]}(W\times\mathbb R;H)\). Localization gives natural triangles \(C_t\to A\to B_t\xrightarrow{+1}\). The maps (11) and the identity of \(A\) show that the actual restrictions \(B_t\to B_{t'}\) are isomorphisms whenever \(t_0<t<t'\).

Choose \(t_n=t_0+2^{-n}\). The opens \(U_n=W\times(t_n,\infty)\) increase to \(U_0'=W\times(t_0,\infty)\). On a bounded-below flabby resolution \(I\) of \(H\), the restrictions \(\Gamma(U_{n+1};I^r)\to\Gamma(U_n;I^r)\) are surjective, and the sheaf gluing axiom identifies \(\Gamma(U_0';I^r)\) with their inverse limit. The product-difference map \(1-\mathrm{shift}\) on \(\prod_n\Gamma(U_n;I^r)\) is surjective: solve each successive restriction equation using that surjectivity. Its kernel is the inverse limit. Consequently the homotopy fibre of the product-difference map computes \(R\Gamma(U_0';H)\). This is the explicit tower calculation and Milnor sequence; the present use is for an increasing open union, whose termwise limit was just proved by gluing.

Every cohomology transition of the tower \(B_{t_n}\) is already an isomorphism. The product-difference map is therefore surjective on those cohomology products too, so its \(\lim^1\) term vanishes and \(B_{t_0}\to B_{t_n}\) is an isomorphism. These are the same restriction maps as in the localization triangles. Taking their fibres over the identity of \(A\) proves \(C_{t_0}\to C_{t_n}\) invertible. Composing with the strict-level comparison to \(Rq_!H\) gives exactly the closed supported counit at \(t_0\), naturally on the base.

Finally the proper supports of an open lower cutoff \(s<t\) are locally exhausted by closed cutoffs \(s\leq u<t\): a compact support lying in this open set has maximum height strictly less than \(t\). If \(t>t_0\), levels with \(t_0<u<t\) are cofinal among them. Their counits are isomorphisms by the closed supported result, so the open extension counit is an isomorphism as well. At \(t=t_0\) there are no such levels; the explicit nonzero examples below show why the open rows retain their strict endpoint.

## Removing the new boundary covectors

For the ordinary case choose \(t>t_0\), put \(\Omega=X\times(-\infty,t)\), and let \(j:\Omega\hookrightarrow X\times\mathbb R\). The ordinary extension \(Rj_*j^{-1}H\) has support in \(L\cap\{s\leq t\}\), hence proper over \(X\). At \(s=t\), the strict normal polar is \(N^*(\Omega)=\mathbb R_{\leq0}\,ds\). The condition \(\sigma\leq0\) excludes every nonzero element of \(-N^*(\Omega)\) from \(\operatorname{SS}(H)\). Thus the ordinary-open row of the four boundary estimates gives the ordinary closed sum \(\operatorname{SS}(H)+N^*(\Omega)\). At the boundary, a horizontal member of that sum has vertical component \(\sigma+\lambda=0\), where \(\sigma\leq0\) and \(\lambda\leq0\). Both must vanish. The proper-image estimate (MO8), together with the already proved ordinary comparison, therefore gives

\[
\operatorname{SS}(Rq_*H)\subset
\{(x,\xi): (x,s;\xi,0)\in\operatorname{SS}(H)
\text{ for some }s\leq t\}.
\qquad\text{(12)}
\]

For the exceptional case put \(Z=X\times(-\infty,t]\). At its boundary \(N^*(Z)=\mathbb R_{\leq0}\,ds\), whereas \(\sigma\geq0\) excludes its nonzero members from \(\operatorname{SS}(H)\). The closed-supported row of the same table bounds \(\operatorname{SS}(R\Gamma_ZH)\) by \(\operatorname{SS}(H)-N^*(Z)\). Now a horizontal sum has \(\sigma+\lambda=0\) with both numbers nonnegative; again both vanish. Proper image and the supported counit give (12) for \(Rq_!H\). Below the boundary no normal is added. This calculation, separately valid for either signed real hypothesis, removes the new cutoff directions before taking the threshold limit.

Apply (9) with \(\sigma=0\) to lift (12) into \(\Lambda\) at a point of \(Z_t\). Fix \((x,\xi)\) in the microsupport of either output and let \(t\downarrow t_0\). All its lifting points lie in one compact supported fibre sublevel, using any fixed \(t_1>t_0\). A subsequence converges to \(y\) with \(f(y)=x\) and \(\varphi(y)\leq t_0\). Its lifted covectors are exactly \((df_y)^t\xi\), so continuity of \(df\) and closedness of \(\Lambda\) give membership in \(\Lambda\) at the limit. This proves (6)–(7), including all zero-transpose and critical-differential cases.

## Complex geometry of the threshold image

The set

\[
B_0=\{(y,\xi):\varphi(y)\leq t_0,
\ (y,(df_y)^t\xi)\in\Lambda\}
\subset Y\times_X T^*X
\qquad\text{(13)}
\]

is closed subanalytic. The level inequality is subanalytic under either allowed regularity of \(\varphi\), and the cotangent correspondence is holomorphic. On this actual set, \(f_\pi\) is proper. To check this, let \(K\subset T^*X\) be compact. Its base projection is compact. The \(y\)-coordinates in \(f_\pi^{-1}(K)\cap B_0\) belong to \(\operatorname{supp}(G)\cap Z_{t_0}\), whose inverse image of that compact base projection is compact by (3). Pairing this with \(\xi\in K\) and using closedness proves compactness. We used \(\pi_Y\Lambda=\operatorname{supp}(G)\), including the zero covectors. Thus \(D_0=f_\pi(B_0)\) is closed subanalytic.

Apply proper direct cotangent transport to the actual conic subanalytic isotropic set \(\Lambda\cap\pi_Y^{-1}(Z_{t_0})\). It is isotropic as a subset of \(\Lambda\), and its inverse image under the differential correspondence is exactly \(B_0\), on which properness was just checked. That theorem proves \(D_0\) isotropic without a constant-rank or noncharacteristic assumption on \(f\). Its analytic map is the original \(f\); only subanalyticity of the level region is needed. No analyticity or constructibility of the cylinder image \(H\) is required here.

For \(\lambda\in\mathbb C^*\),

\[
(df_y)^t(\lambda\xi)=\lambda(df_y)^t\xi.
\qquad\text{(14)}
\]

The original \(\Lambda\) is complex-conic, and the inequality in (13) depends only on \(y\). Hence \(B_0\), and therefore \(D_0\), is complex-conic. This direct argument works even though \(D_0\) was only proved subanalytic. The complex-conic bound argument and four-test criterion apply to the closed complex-conic subanalytic isotropic bound (6). It proves weak complex constructibility of both outputs once boundedness is established. The source coefficient cutoffs themselves need only be real constructible.

## Boundedness and perfect coefficients through real cutoffs

The closed ordinary and supported coefficients on the ambient manifold are

\[
P_t=i_{t*}i_t^{-1}G\simeq G\overset L\otimes k_{Z_t},
\qquad Q_t=i_{t*}i_t^!G\simeq R\Gamma_{Z_t}G
\simeq R\mathcal Hom(k_{Z_t},G).
\qquad\text{(15)}
\]

The extension \(k_{Z_t}\) is perfect real constructible. The closed subanalytic level set admits a locally finite real subanalytic stratification; on each stratum its stalk is \(k\) or zero. This works for the \(C^2\) subanalytic cutoff as well as for an analytic one. The sheaf is flat over \(k\), so if \(G\in D^{[a,b]}\), then \(P_t\in D^{[a,b]}\). For \(Q_t\), the actual bounded internal-Hom estimate (M44), with first input \(k_{Z_t}\) in degree zero, gives the uniform sufficient range \(D^{[a,b+3d+g+1]}\), where \(d=\dim_{\mathbb R}Y\) and \(g=\operatorname{gld}(k)\). The weak real tensor and internal-Hom theorem proves both coefficients weakly real constructible. They need not be complex constructible.

Their supports lie in \(\operatorname{supp}(G)\cap Z_t\), where \(f\) is proper. Apply the real proper direct-image theorem on the actual support to this original analytic map \(f\). Its fibre compact-support dimension is at most \(d\), so the sufficient output ranges are \(D^{[a,b+d]}\) for \(Rf_*P_t\) and \(D^{[a,b+4d+g+1]}\) for \(Rf_*Q_t\). The closed rows identify these with \(Rf_*G\) and \(Rf_!G\) for every \(t\geq t_0\). Thus the global boundedness required by the complex criterion has been proved, not inferred from separate pointwise bounds. For nonanalytic \(\varphi\), this argument still uses analytic \(f\) with the real subanalytic coefficients (15), rather than a constructibility theorem for \(h\).

If \(G\) has perfect stalks, the perfect tensor and constructible internal-Hom proof makes \(P_t\) and \(Q_t\) perfect real constructible. For \(Q_t\) it uses actual constructible duality and evaluation; it does not identify a local supported complex with algebraic Hom of two ordinary stalks. The proper-image theorem for perfect stalks then applies to \(f\). Its proof restricts to the compact subanalytic coefficient support in each fibre and uses finite compact triangulation, so singular closed levels cause no exception. Combined with (6) and the complex criterion, this proves the perfect complex-constructible conclusion.

These arguments preserve arbitrary commutative finite-global-dimension coefficients and do not assume Noetherianity. They also prove the weak version for infinite coefficient modules. No weak biduality or infinite dual-tensor evaluation formula is needed.

## What the geometric image does not measure

The threshold set records possible original covectors; it does not record the maps in a fibre cohomology calculation. Those maps may cancel all the cohomology even though the unrestricted cotangent image is nonempty. Thus the conclusions proved here are the two inclusions

\[
\operatorname{SS}(Rf_*G)\subset D_0
\subset f_\pi f_d^{-1}(\operatorname{SS}(G)).
\qquad\text{(16)}
\]

The second inclusion follows by restricting the base level. The half-open interval calculations, worked out completely in Exercise 6, make it strict under the corresponding signed real hypotheses: the restriction between two copies of \(k\) is the identity, so its fibre vanishes while the unrestricted cotangent image retains a zero covector. This is a real example with one-sided rays, not a complex-constructible counterexample. The complex and perfect conclusions above use only (6); no equality between the two geometric images is needed.

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

For the exceptional case use \(G'=k_{[0,1)}\). Its endpoint rays are nonnegative multiples of \(ds\), so the negative exclusion holds. The triangle removing the endpoint \(1\) from the closed compact interval gives \(R\Gamma_c(\mathbb R;G')=0\); compact global sections of the closed interval restrict identically to that endpoint. Its threshold image is again empty and its full geometric image the singleton. These are real sheaves with one-sided cotangent rays. They disprove the stronger general real geometric equality, not a separate complex-input equality: the rays are not complex-conic and the source is not a complex manifold. For the complex theorem we have proved the sufficient inclusions, with no stronger image equality inferred from the real cutoff argument.

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

## Applying the cutoff criterion

To apply the criterion over a complex curve, choose a source neighborhood carrying a cutoff with every supported closed level proper, and exclude the relative differential above one threshold. A \(C^2\) subanalytic cutoff with subanalytic differential suffices by the graph argument. The ordinary and supported closed coefficients then compute the two images even at the threshold; the open coefficients require a strictly larger level. The next lesson constructs such neighborhoods by controlling possibly unbounded horizontal covectors, comparing one-variable Laurent orders, and arranging properness of all finite levels.

## References

M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985): Theorem 4.4.1, printed pp. 73–75, treats direct images using exhausting open cutoffs; Remark 8.3.2, printed p. 149, gives the real constructible consequence; Theorem 8.5.2, printed pp. 151–154, characterizes weak complex constructibility by cotangent geometry; Proposition 8.6.1, printed p. 154, applies these results to nonproper holomorphic maps. The four canonical comparisons, closed endpoints, threshold bound and subanalytic \(C^2\) extension are proved above using the linked sheaf-operation results.
