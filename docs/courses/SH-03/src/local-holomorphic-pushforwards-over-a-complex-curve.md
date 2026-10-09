# Local holomorphic pushforwards over a complex curve

Over a complex curve, the relative cutoff condition can be arranged near any compact part of a fibre. The decisive point is not boundedness of every covector: a horizontal covector may tend to infinity. Analyticity and the canonical one-form force its pole to be weaker than the vanishing of the base coordinate. This gives a full characteristic inverse at the central fibre, a uniform compact cutoff band, and both constructible direct images.

Let \(k\) be a commutative ring of finite global dimension. All manifolds are Hausdorff, countable at infinity and of uniformly bounded finite dimension; all sheaf complexes are globally bounded. Let \(f:Y\to X\) be holomorphic with \(\dim_{\mathbb C}X=1\). Fix \(x_0\in X\), a nonempty compact \(K\subset f^{-1}(x_0)\), and a weakly complex constructible \(G\). Perfect complex constructibility means, additionally, that every stalk is perfect. The empty \(K\) case is immediate by taking an empty source neighborhood.

The theorem includes the zero coefficient ring, when every sheaf and microsupport is zero. In the coefficient examples identifying a nonempty microsupport or a nonconstant stalk, take \(k\neq0\).

Kashiwara and Schapira prove the local complex-curve direct-image theorem in [*Microlocal study of sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Proposition 8.6.2, printed pp. 154–156 (statement on pp. 154–155). Their Lemmas 8.6.3 and 8.6.4, printed pp. 155–156, provide the central cotangent equality and the discrete-critical-value argument. We develop these mechanisms using a finite reciprocal covector chart, then construct the needed exhaustion directly near the compact set. The final reciprocal reparameterization makes every finite closed cutoff level proper.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

## The neighborhood theorem and its cotangent bound

There exist an open neighborhood \(U\ni x_0\) and an open neighborhood \(V\supset K\), with \(V\subset f^{-1}(U)\), such that, for \(f_V:V\to U\),

\[
R(f_V)_*(G|_V),\qquad R(f_V)_!(G|_V)
\quad\text{are weakly complex constructible.}
\qquad\text{(1)}
\]

If \(G\) has perfect stalks, so do both outputs. Moreover, using the original microsupport restricted to \(V\),

\[
\operatorname{SS}(R(f_V)_*(G|_V))\cup
\operatorname{SS}(R(f_V)_!(G|_V))
\subset (f_V)_\pi (f_V)_d^{-1}(\operatorname{SS}(G)|_V).
\qquad\text{(2)}
\]

No added cutoff boundary directions appear on the right. For a Euclidean source and \(K=\{0\}\), we can choose

\[
V=B_r(0)\cap f^{-1}(U)
\qquad\text{(3)}
\]

for a sufficiently small radius and base neighborhood. Formula (3) is the centered-ball statement that the proof establishes. An entire ball would additionally require \(f(B_r)\subset U\), which can be incompatible with constructibility of the outputs on that \(U\).

## Reduction to a product without changing the original bound

Factor \(f\) through its closed holomorphic graph:

\[
Y\xrightarrow{\gamma} Z\times X\xrightarrow{p}X,
\qquad Z=Y,\quad \gamma(y)=(y,f(y)).
\qquad\text{(4)}
\]

The graph is closed because the manifolds are Hausdorff. Put \(\widetilde G=R\gamma_*G\). The closed embedding is proper, so the [holomorphic proper-image theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#proper-direct-image-uses-the-actual-support) gives bounded weak complex constructibility, and its [perfect-coefficient argument](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#perfect-coefficients-after-the-weak-geometric-proof) gives perfect stalks when \(G\) has them. Its actual microsupport is

\[
\widetilde\Lambda
=\{(y,f(y);\zeta,\xi):
(y,\zeta+(df_y)^t\xi)\in\operatorname{SS}(G)\}.
\qquad\text{(5)}
\]

The [closed-embedding equality in MO8](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-proper-push--collecting-tests-along-a-fibre) proves (5): a local support test for the graph coefficient is the same test on the graph, and restriction of the product covector \((\zeta,\xi)\) to its tangent is \(\zeta+(df_y)^t\xi\). This includes all conormal directions and zero covectors, without a noncharacteristic assumption. A horizontal covector \((0,\xi)\) belongs to \(\widetilde\Lambda\) exactly when \((df_y)^t\xi\in\operatorname{SS}(G)\).

It suffices to construct a product neighborhood \(W\subset Z\times U\) of \(\gamma(K)\). Its graph inverse image \(V=\gamma^{-1}(W)\) is a neighborhood of \(K\) in \(f^{-1}(U)\), and the two images of \(\widetilde G|_W\) under \(p\) identify with the images of \(G|_V\) under \(f_V\). Formula (5) will translate the product bound back to (2). We now write \(G,\Lambda,f\) for this product coefficient, its actual microsupport, and the projection \(Z\times X\to X\).

Let

\[
j:Z\simeq Z\times\{x_0\}\hookrightarrow Z\times X,
\qquad A_0=j^\sharp\Lambda.
\qquad\text{(6)}
\]

The [graph-conormal slice proof, (18)–(23)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#characteristic-inverse-isotropy), makes the full \(j^\sharp\Lambda\) closed, subanalytic and real-isotropic, including unbounded witnesses. Its [holomorphic version](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#full-characteristic-inverse-image-for-a-holomorphic-map) also makes it complex analytic and complex-conic: complex scaling preserves the sharp sequence criterion, and the normal-cone model is a holomorphic inverse image of a complex analytic normal cone. The actual microsupport \(\Lambda\) of the weakly complex constructible input is closed complex analytic by the [four equivalent geometric tests](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests). These conclusions need no perfect-stalk hypothesis.

## Closed horizontal saturation equals the full central sharp inverse

For the product projection let \(V_f\) be its horizontal cotangent space. The exact curve lemma is

\[
j_dj_\pi^{-1}\overline{\Lambda+V_f}=j^\sharp\Lambda=A_0.
\qquad\text{(7)}
\]

The bar is the ambient closure of the ordinary sum. It is not a limiting hat sum. Choose coordinates \((z,x;\zeta,\xi)\), with \(x\) one complex coordinate. A point \((z_0;\zeta_0)\) belongs to the left side precisely when there are points

\[
(z_n,x_n;\zeta_n,\xi_n)\in\Lambda,
\qquad (z_n,x_n,\zeta_n)\longrightarrow(z_0,x_0,\zeta_0).
\qquad\text{(8)}
\]

Indeed horizontal addition can replace \(\xi_n\) by any finite covector, while leaving \(\zeta_n\) unchanged. Conversely any convergent point of the ordinary horizontal sum has such a lift. There is no boundedness assumption on \(\xi_n\).

We will prove that every sequence (8) satisfies

\[
|\xi_n|\,|x_n-x_0|\longrightarrow0.
\qquad\text{(9)}
\]

For bounded \(\xi_n\) this is immediate. Once (9) holds in general, choose the domain point of the central embedding to be \(z_n\). Its image differs from \((z_n,x_n)\) only by \(x_n-x_0\), and its transpose covector is \(\zeta_n\). Since \(\zeta_n\) is bounded, (9) also holds with the norm of the full covector. This is exactly the full sharp sequence criterion. It proves the left-to-right inclusion in (7). In the opposite direction, any sharp sequence already has converging bases and converging restricted covectors, hence gives (8) after discarding its horizontal covector. This proves the other inclusion.

## A finite chart for an unbounded covector

Suppose (9) fails. A subsequence has \(\xi_n\neq0\), \(|\xi_n|\to\infty\), and \(|\xi_n|\,|x_n-x_0|\geq\epsilon>0\). Put \(u_n=1/\xi_n\). Complex cotangent conicity makes the original membership equivalent to

\[
(z_n,x_n;u_n\zeta_n,1)\in\Lambda.
\]

Thus, in finite coordinates \((z,x,\zeta,u)\), introduce the analytic set

\[
\mathcal A=\{(z,x,\zeta,u): (z,x;u\zeta,1)\in\Lambda\}.
\qquad\text{(10)}
\]

It is the holomorphic inverse image of the closed analytic \(\Lambda\). The bad sequence tends to \(q=(z_0,x_0,\zeta_0,0)\), within the real semianalytic subset

\[
\mathcal A\cap\{u\neq0,\ |x-x_0|^2\geq\epsilon^2|u|^2\}.
\qquad\text{(11)}
\]

The [analytic curve-selection construction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#from-a-local-analytic-presentation-to-analytic-curve-selection), applied to the real semianalytic set (11) in this finite chart, gives a real analytic curve through \(q\) lying in (11) for all small positive real parameters. Here \(u\neq0\) is the real analytic inequality \(|u|^2>0\); the squared-norm inequality is essential and stays part of the selected set. Extend the finite coordinate functions holomorphically to a complex disc. Local holomorphic equations of \(\mathcal A\) vanish on the positive real branch, so the identity theorem makes them vanish on that disc. The real inequality is used only on the positive real branch. The holomorphic function \(u(t)\) vanishes at zero and is not identically zero. Its zero has finite order, so after shrinking it is nonzero at every nonzero parameter. Undoing the complex cotangent scaling consequently gives

\[
\xi(t)=1/u(t),\qquad
(z(t),x(t);\zeta(t),\xi(t))\in\Lambda
\quad(0<|t|\ll1)
\qquad\text{(12)}
\]

is a meromorphic cotangent arc with finite holomorphic \(z,x,\zeta\). This supplies the required compactification argument. A holomorphic arc chosen without retaining the bad inequality would not prove the assertion for an arbitrary bad sequence.

Write \(\theta=\sum_i\zeta_i\,dz_i+\xi\,dx\). At a regular point of the complex-conic isotropic analytic set \(\Lambda\), the radial covector vector field \(R\) is tangent and \(\iota_R d\theta=\theta\). Isotropy thus gives \(\theta|_{\Lambda_{\mathrm{reg}}}=0\). This vanishing also tests singular arcs. The [point-cone form test and singular pullback proof, (C1)–(C4)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#singular-form-calculus), show that both \(\operatorname{Re}\theta\) and \(\operatorname{Im}\theta\) kill every limiting tangent direction to \(\Lambda\), including at singular points. At every nonzero parameter the derivative of (12) is such a tangent direction, even if the entire arc lies in the singular locus. Pulling back therefore yields

\[
\sum_i\zeta_i(t)z_i'(t)+\xi(t)x'(t)=0.
\qquad\text{(13)}
\]

The first term is holomorphic and bounded at zero. Therefore \(\xi(t)x'(t)\) is bounded. If \(x(t)\equiv x_0\), (11) is already impossible for positive real \(t\), since \(u(t)\neq0\). Otherwise let

\[
x(t)-x_0=a t^m+O(t^{m+1}),\qquad
u(t)=b t^r+O(t^{r+1}),\qquad a,b\neq0, m,r\geq1.
\qquad\text{(14)}
\]

Then \(\xi(t)x'(t)\) has leading order \(t^{m-r-1}\) with nonzero coefficient \(ma/b\). Boundedness forces \(r\leq m-1\). Hence

\[
\xi(t)(x(t)-x_0)=O(t^{m-r})\longrightarrow0.
\qquad\text{(15)}
\]

Along positive real parameters this contradicts (11). Thus (9) holds for every sequence, and (7) follows. The argument uses one scalar horizontal covector paired with one scalar base derivative. In several base coordinates boundedness of their sum does not bound each product.

## A compact band with a uniform relative exclusion

Only a neighborhood of the compact projection \(K_Z\subset Z\) of \(\gamma(K)\) is needed. Choose finitely many holomorphic coordinate charts \(\kappa_i\) and Euclidean balls \(\{|\kappa_i-c_i|<R_i\}\) covering \(K_Z\), with each closed ball compactly contained in its chart. On that chart put \(b_i=(R_i^2-|\kappa_i-c_i|^2)_+^3\), and extend \(b_i\) by zero to \(Z\). Here \(a_+=\max(a,0)\). The value and first two derivatives of \(a_+^3\) agree at \(a=0\), so each \(b_i\) is \(C^2\); its support is compactly inside the chart, which makes extension across the chart boundary harmless. Put \(b=\sum_i b_i\), \(N=\{b>0\}\), and \(\varphi=1/b\) on \(N\).

The open set \(N\) contains \(K_Z\) and has compact closure. The graphs of \(b\), \(db\), \(\varphi\), and \(d\varphi=-b^{-2}db\) are locally subanalytic: near any point, partition by the finitely many signs of \(R_i^2-|\kappa_i-c_i|^2\); on each piece all these functions have analytic formulas, and the formulas agree to the stated differentiability order. For \(c>0\), the sublevel \(\{\varphi\leq c\}=\{b\geq1/c\}\) is a closed subset of the finite union of compact ball supports and lies inside \(N\). For \(c\leq0\) it is empty. Thus \(\varphi\) is positive, \(C^2\), locally subanalytic, and proper, with every finite sublevel compact. This is the finite version of the [coordinate-ball cutoff construction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#1-the-compact-radial-bump-including-derivative-checks).

Restrict the product and its coefficient to \(N\times X\), and continue to write \(Z,G,\Lambda,A_0\) for these restrictions. The sharp inverse and ordinary closure identity are local, so (6)–(7) remain valid. Regard \(\varphi\) as independent of \(x\) on the product. The cutoff argument below uses its stated \(C^2\) subanalytic regularity; no global analytic exhaustion is needed.

The set \(\pi A_0\) is closed: positive conicity and closedness give \(\pi A_0=\{z:(z,0)\in A_0\}\). The chosen \(\varphi\) is therefore proper on \(\pi A_0\). The [critical-set proof using analytic curves](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#direct-critical-set-proof) extends to our function as follows. Set \(E=\{z:(z,d\varphi_z)\in A_0\}\). It is closed and subanalytic, since the derivative graph just constructed is subanalytic. If \(\varphi|_E\) were not locally constant at \(z_0\in E\), curve selection would give a real analytic \(\gamma\) through \(z_0\), entering \(E\setminus\{\varphi=\varphi(z_0)\}\) for positive parameter.

The lifted curve \(\ell(t)=(\gamma(t),d\varphi_{\gamma(t)})\) is \(C^1\) and lies in \(A_0\). For each positive parameter, its derivative is in the point cone of \(A_0\): use the difference quotients \((\ell(t+h)-\ell(t))/h\) with \(h>0\). The form test (C1)–(C3) therefore gives \(\alpha(\ell'(t))=d\varphi_{\gamma(t)}\gamma'(t)=0\). The ordinary chain rule, mean value theorem and continuity at zero imply \(\varphi(\gamma(t))=\varphi(z_0)\), a contradiction. Thus \(\varphi|_E\) is locally constant. For a compact interval \(J\), the closed set \(E\cap\varphi^{-1}(J)\) is compact. Finitely many of these constant-value neighborhoods cover it, so its image is finite. Consequently

\[
\{\varphi(z):d\varphi_z\in A_0\}
\quad\text{is closed and locally finite in }\mathbb R.
\qquad\text{(16)}
\]

Set \(s_0=\max_{\gamma(K)}\varphi\). Choose \(s_0<s_1<s_2\) so that the whole closed band \([s_1,s_2]\) misses (16). Such a gap exists above any fixed \(s_0\) because only finitely many selected values occur in a compact interval. Thus

\[
d\varphi_z\notin A_0
\quad(s_1\leq\varphi(z)\leq s_2).
\qquad\text{(17)}
\]

For some sufficiently small \(U\ni x_0\), this implies

\[
d\varphi_{(z,x)}\notin\Lambda+V_f
\quad(x\in U,\ s_1\leq\varphi(z)\leq s_2).
\qquad\text{(18)}
\]

Otherwise choose failing points with \(x_n\to x_0\). The \(z_n\) lie in the compact closed band, so a subsequence converges to \(z_0\) in that band. Membership in the ordinary sum at a failing point gives a lift \((z_n,x_n;d\varphi_{z_n},\xi_n)\in\Lambda\), after adjusting the horizontal covector. The lift can have unbounded \(\xi_n\). The finite covectors \((d\varphi_{z_n},0)\) nevertheless converge in the closed ordinary sum. Equation (7) places \(d\varphi_{z_0}\) in \(A_0\), contradicting (17). Compactness supplies the uniform neighborhood; the curve lemma supplies the unbounded-covector control.

## All closed levels after restricting the source

Set

\[
W=\{(z,x):\varphi(z)<s_2,\ x\in U\},\qquad
\psi(z,x)=\frac1{s_2-\varphi(z)},\qquad
t_0=\frac1{s_2-s_1}.
\qquad\text{(19)}
\]

The original \(\varphi|_W\) is bounded above, and its sufficiently large closed sublevels equal all of the open source \(W\). Therefore it does not automatically satisfy the all-level properness hypothesis. The reciprocal in (19) repairs this.

For \(u\leq0\) a closed \(\psi\)-sublevel is empty. For \(u>0\) it is defined by

\[
\varphi(z)\leq s_2-1/u<s_2.
\qquad\text{(20)}
\]

Over a compact subset of \(U\), this is a closed subset of the product of that base subset with a compact \(\varphi\)-sublevel in \(Z\). Intersecting with the actual closed support of \(G|_W\) remains compact: (20) stays strictly inside the cutoff and introduces no missing outer boundary points. Hence every closed supported \(\psi\)-level is proper over \(U\).

Moreover

\[
d\psi=(s_2-\varphi)^{-2}d\varphi,
\qquad \psi>t_0\Longleftrightarrow\varphi>s_1.
\qquad\text{(21)}
\]

The coefficient in the differential is positive. On this part of \(W\), (18) and positive conicity give the relative exclusion for \(\psi\); complex cotangent conicity gives its negative version as well. The function \(\psi\) is \(C^2\), with locally subanalytic function and derivative graphs. We can therefore use the subanalytic \(C^2\) form of [Nonproper holomorphic pushforwards through cutoffs](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/nonproper-holomorphic-pushforwards-through-cutoffs.md), with the all-level properness just proved.

Here is the coefficient argument at this regularity. The [real relative-cutoff theorem, MO24–MO27](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-relative-cutoff--replacing-a-nonproper-map-by-a-bounded-part), assumes a \(C^1\) function and supplies the actual restriction and supported counit maps. At a closed level \(t\geq t_0\), put \(H=G|_W\), \(Z_t=\{\psi\leq t\}\), \(P_t=H\otimes k_{Z_t}\), and \(Q_t=R\Gamma_{Z_t}H=R\mathcal Hom(k_{Z_t},H)\). Its isomorphisms are \(R(f|_W)_*H\longrightarrow R(f|_W)_*P_t\) and \(R(f|_W)_*Q_t=R(f|_W)_!Q_t\longrightarrow R(f|_W)_!H\). Their [one-sided continuation proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-cutoff-proof--proof-of-the-four-cutoff-maps) requires only the \(C^1\) differential tests.

The closed subanalytic cutoff coefficient \(k_{Z_t}\) has perfect stalks. The [weak tensor and internal-Hom theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#tensor-and-internal-hom-retain-the-full-limiting-sum) makes \(P_t,Q_t\) bounded weakly real constructible, including for infinite input stalks; the [perfect cutoff theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#compact-and-relatively-compact-cohomology) gives perfect stalks if \(H\) has them. Their closed supports lie in \(\operatorname{supp}(H)\cap Z_t\), on which the original holomorphic projection is proper. Apply its [proper weak real image theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#properness-on-support-supplies-the-cotangent-compactness) and the [compact-fibre perfection theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks). This proves global boundedness, weak real constructibility and the separate perfect-stalk assertion. It never requires the auxiliary map \((f,\psi)\) to be analytic.

For the complex geometry, MO27 bounds both output microsupports by \(D_0=(f|_W)_\pi(f|_W)_d^{-1}\bigl(\Lambda|_W\cap\pi^{-1}Z_{t_0}\bigr)\). The set inside this direct transport is closed, subanalytic, complex-conic and real-isotropic: the base cutoff preserves complex fibre scaling, and the point-cone form test passes isotropy to a subanalytic subset. Over a compact downstairs cotangent set \(C\), the correspondence inverse lies in the product of \(C\) with the compact set \(\operatorname{supp}(H)\cap Z_{t_0}\cap f^{-1}(\pi C)\); it is closed there. Thus the actual correspondence projection is proper. The [proper isotropic transport theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#proper-direct-transport) makes \(D_0\) closed, subanalytic and real-isotropic. Complex linearity of the transpose differential also makes \(D_0\) complex-conic. The [complex constructibility criterion, condition 2](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests), now gives both weak complex outputs. Together with the preceding perfect-stalk argument this proves the perfect assertion.

Its sharp threshold bound only uses points with \(\psi\leq t_0\), equivalently \(\varphi\leq s_1\), which lie inside \(W\). Thus it uses the original \(\Lambda\), with no new boundary covectors. Return through (4)–(5). A threshold witness for the product bound has \(\zeta=0\) and \((df_y)^t\xi\in\operatorname{SS}(G)\). It lies in the graph neighborhood \(V\). This proves (1)–(2) for the original map.

## Centered balls in the source germ

Suppose \(Y\subset\mathbb C^n\) is open, \(0\in Y\), \(f(0)=x_0\), and \(K=\{0\}\). In the graph reduction take \(\varphi(z)=|z|^2\). Choose \(R>0\) with \(\overline B_R\subset Y\), and truncate the central \(A_0\) to the closed base ball \(\overline B_R\). This is a closed conic subanalytic isotropic set with compact base projection. Apply the discrete-critical-value theorem to squared norm on this truncated set. Its selected values in \([0,R^2]\) are finite. Choose \(0<s_1<s_2<R^2\) below its least positive selected value, if there is one. In particular (17) holds throughout this small positive band; the differential may belong to \(A_0\) at zero, which is allowed.

The compact-band proof of (18) applies unchanged. The reciprocal \(\psi=(s_2-|z|^2)^{-1}\) has every finite closed level strictly inside \(B_{\sqrt{s_2}}\), hence compact over compact base sets; no global properness of squared norm on the original open \(Y\) is needed. The graph inverse image of \(W\) is exactly (3), with \(r=\sqrt{s_2}\). This proves the centered-ball germ version and retains (2).

The literal assertion that \(V\) can always be the whole \(B_r\), with \(V\subset f^{-1}(U)\) and both images constructible on that entire \(U\), is stronger. Exercise 5 disproves it. In common uses one studies the pushforward of a ball on a smaller target germ; its coefficient over that germ is precisely \(G|_{B_r\cap f^{-1}(U)}\). The distinction matters for a global statement on \(U\).

## More than one complex base coordinate

For several base coordinates, (13) becomes \(\sum\zeta_i z_i'+\sum\xi_j x_j'=0\). Unbounded products in different coordinates can cancel, so the one-variable Laurent bound does not follow. The exact equality (7) fails for the smooth complex hypersurface and conormal of Exercise 6. That example isolates the geometric obstruction to this proof. The whole-ball example separately excludes that stronger choice of neighborhood, even over a curve. Neither example proves that every possible source neighborhood fails the existential conclusion in a higher-dimensional base.

## Exercises

### 1. The largest allowed pole on a ramified curve
*Difficulty: Intermediate.*

Let \(S=\{x=z^m\}\subset\mathbb C_z\times\mathbb C_x\), with \(m\geq2\), and \(\Lambda=T_S^*(\mathbb C^2)\). Along \(z(t)=t\), \(x(t)=t^m\), choose the conormal multiplier \(\lambda(t)=t^{-(m-1)}\). Compute both covectors, the canonical one-form and the product in (9). What sharp direction does this produce at the central fibre?

**Solution.** A conormal is \(\lambda(dx-mz^{m-1}dz)\). Thus \(\zeta(t)=-m\) and \(\xi(t)=t^{-(m-1)}\). The horizontal covector is unbounded, whereas the restricted covector is finite and nonzero. The canonical form pulls back to

\[
-m\,dt+t^{-(m-1)}m t^{m-1}dt=0.
\]

Its base vanishing order is \(m\) and its horizontal pole order is \(r=m-1\), the largest allowed by (14). The product \(|\xi(t)|\,|x(t)|\) is \(|t|\), which tends to zero. Consequently the central sharp inverse contains \((z=0;\zeta=-m)\), despite the unbounded horizontal covector. Complex conicity then supplies every nonzero multiple of this covector, and closedness includes zero. This agrees with the point intersection of the smooth curve \(S\) with the central fibre. An ordinary bounded-covector restriction would miss the exhibited witness.

### 2. Why the bad inequality must accompany the selected arc
*Difficulty: Advanced.*

Suppose a bad sequence (8) satisfies \(|\xi_n|\,|x_n-x_0|\geq\epsilon\) and \(|\xi_n|\to\infty\). Describe the finite analytic and real inequality conditions needed for curve selection. If a proposed arc has \(x(t)-x_0=t^m\) and \(u(t)=t^m\), can bounded holomorphic \(z(t),\zeta(t)\) make it an isotropic cotangent arc?

**Solution.** Put \(u_n=1/\xi_n\). Complex cotangent scaling yields the finite analytic equation \((z,x;u\zeta,1)\in\Lambda\), or membership in \(\mathcal A\) from (10). The real condition that retains the bad sequence is \(u\neq0\) together with \(|x-x_0|^2\geq\epsilon^2|u|^2\). Real analytic curve selection on that semianalytic subset, followed by holomorphic extension, preserves the analytic equations and retains the inequality on the positive real branch. Selecting any arc of \(\mathcal A\setminus\{u=0\}\) would only prove a statement about that arbitrary arc, not contradict the original bad sequence.

For the proposed orders, \(\xi=1/u=t^{-m}\), so \(\xi x'=m/t\). This has a pole. The other canonical-form term \(\sum\zeta_i z_i'\) is holomorphic and bounded because every \(z_i,\zeta_i\) is holomorphic at zero. They cannot sum to zero. Hence no such isotropic arc with those finite holomorphic coordinates exists. The contradiction is exactly the strict inequality \(r\leq m-1\), rather than the weaker \(r\leq m\).

### 3. A compact part of a noncompact fibre
*Difficulty: Intermediate.*

Let \(f:\mathbb C_z\times\mathbb C_x\to\mathbb C_x\) be projection, \(G=k\), and \(K=\{|z|\leq A\}\times\{0\}\), with \(A>0\). Construct a product neighborhood as in the proof, compute both outputs, and explain why this is a compact-part statement rather than properness of the original map.

**Solution.** Take \(\varphi(z)=1+|z|^2\). Its differential is nonzero off \(z=0\). Since the original microsupport is the zero section, the central sharp inverse is the zero section and the only selected critical value is one. Choose \(1+A^2<s_1<s_2\), and any small disc \(U\ni0\). The uniform exclusion holds for all \(x\), since \(d\varphi\) has a nonzero vertical \(dz\)-component throughout the band, whereas the horizontal space consists of \(dx\)-covectors. Set \(W=\{|z|^2<s_2-1\}\times U\), with the reciprocal exhaustion from (19).

The ordinary fibre is an open complex disc, with cohomology \(k\), and the proper-support fibre has cohomology \(k[-2]\). Thus the outputs are \(k_U\) and \(k_U[-2]\), with zero-section microsupports and perfect stalks. The original projection has a noncompact whole fibre \(\mathbb C_z\), and neither the original map nor the chosen projection of \(W\) is proper. The theorem controls a neighborhood of the prescribed compact \(K\), using proper finite exhaustion levels. Its conclusion does not assert a uniform neighborhood of the entire original fibre.

### 4. The exact threshold after reciprocal reparameterization
*Difficulty: Intermediate.*

Assume \(\varphi\) is positive and proper on \(Z\), the band \([4,9]\) has the uniform exclusion (18), and \(K\subset\{\varphi<4\}\) on the central fibre. On \(W=\{\varphi<9\}\times U\), calculate a valid reciprocal exhaustion, its threshold and the part of the original microsupport used by the final bound. Check levels that are nonpositive.

**Solution.** Use \(\psi=1/(9-\varphi)\), which is positive on \(W\), and \(t_0=1/(9-4)=1/5\). A nonpositive closed level is empty. At a positive level \(u\), the inequality is \(\varphi\leq9-1/u<9\). Over any compact base set this is a closed supported subset of a compact \(\varphi\)-sublevel times that base set, so all finite levels are proper. Its differential is \((9-\varphi)^{-2}d\varphi\), a positive multiple, and \(\psi>1/5\) means precisely \(\varphi>4\). The exclusion therefore holds on the part of \(W\) above the threshold.

The final threshold region is \(\psi\leq1/5\), equivalent to \(\varphi\leq4\). The microsupport bound uses only the original \(\Lambda\) over this inner closed region. It introduces neither the boundary of \(\varphi<9\) nor any artificial normal covectors from the reciprocal function. The chosen outer level provides a source neighborhood; the inner threshold supplies the compact witnesses for the bound.

### 5. An entire ball creates a real target boundary
*Difficulty: Advanced.*

Assume \(k\neq0\). Let \(Y=\mathbb C^2\), \(f(z_1,z_2)=z_1\), \(L=\{z_2=z_1\}\), and \(G=k_L\). Take \(K=\{0\}\). Prove that no entire centered ball \(V=B_r(0)\), \(r>0\), can satisfy the whole-ball strengthening on an open \(U\) with \(V\subset f^{-1}(U)\). Then explain how (3) repairs the local statement.

**Solution.** The sheaf \(k_L\) is perfect complex constructible on the smooth closed complex line. The image of the entire source ball under \(f\) is the disc \(D_r=\{|w|<r\}\), since every \((w,0)\) with \(|w|<r\) belongs to the ball. Thus any allowed \(U\) must contain \(D_r\). On the line, a point is \((w,w)\), with squared norm \(2|w|^2\). The support inside the ball projects isomorphically onto \(D_a\), where \(a=r/\sqrt2\). Closed direct image of the line in \(V\), followed by this open embedding \(j:D_a\hookrightarrow U\), gives

\[
R(f_V)_*(G|_V)=Rj_*k_{D_a}=k_{\overline D_a},
\qquad R(f_V)_!(G|_V)=j_!k_{D_a}.
\]

The closure is taken inside \(U\); the whole closed disc lies there. Near a boundary point the intersection of a small neighborhood with \(D_a\) is contractible, giving the displayed ordinary image with no higher cohomology. At \(|w|=a\), the closed-disc coefficient has the inward one-sided real conormal ray, and the open extension has the outward ray. With \(\rho=|w|^2-a^2\), these are the nonpositive and nonnegative multiples of \(d\rho\), respectively. Both have a nonzero ray; neither is invariant under multiplication by \(i\) in the complex cotangent line. Hence neither output is weakly complex constructible on \(U\). The circle is inside \(D_r\subset U\), so no choice of such \(U\) removes it.

For the correct local version choose \(U=D_\delta\) with \(0<\delta<a\), and take \(V=B_r\cap f^{-1}(U)\). Its line support projects isomorphically onto all of \(U\). Both images are now \(k_U\), with perfect stalks and zero-section microsupport. This is the source coefficient of the original ball viewed over a smaller target germ. The counterexample refutes the literal entire-ball assertion together with its required containment; it preserves the compact-part neighborhood theorem.

### 6. The central cotangent equality fails for a surface base
*Difficulty: Advanced.*

Let \(Z=\mathbb C_z\), \(X=\mathbb C^2_{x_1,x_2}\), \(f:Z\times X\to X\) be projection, and \(S=\{x_2=z x_1\}\). Set \(\Lambda=T_S^*(Z\times X)\) and let \(j\) be the central fibre at \((0,0)\). Compute both sides of (7), showing that the closed horizontal side is strictly larger. Also give a multicoordinate arc where two unbounded terms in \(\sum\xi_i x_i'\) cancel.

**Solution.** The hypersurface is smooth because the \(x_2\)-derivative of its defining equation is one. Its conormal covectors are

\[
\lambda(-x_1\,dz-z\,dx_1+dx_2),
\quad\text{so }\zeta=-\lambda x_1,\quad
\xi_1=-\lambda z,\quad\xi_2=\lambda.
\]

For any fixed \(z_0\) and desired \(\zeta_0\neq0\), choose \(z=z_0\), \(x_1=t\), \(x_2=z_0t\), and \(\lambda=-\zeta_0/t\). The restricted covector is exactly \(\zeta_0\); horizontal addition cancels both unbounded horizontal entries. Taking \(t\to0\) puts every \((z_0;\zeta_0)\) in the closed horizontal side of (7), with zero included by closedness. That side is all of \(T^*Z\).

For any sharp witness, however, the full covector norm is at least \(|\lambda|\), and the displacement from the central fibre has norm at least \(|x_1|\). The sharp small-product condition therefore forces \(|\lambda x_1|\to0\), and hence \(\zeta\to0\). Conversely every zero covector on the central fibre is realized by a zero conormal. Thus \(j^\sharp\Lambda\) is exactly the zero section. The two sets differ. The example uses the actual conormal of a smooth complex hypersurface, so it is not an artifact of a nonanalytic cone.

For direct cancellation take the curve \(x(t)=(t,t^2)\) and \(\xi(t)=(-2/t,1/t^2)\). Then \(\xi_1x_1'+\xi_2x_2'=-2/t+2/t=0\), whereas \(|\xi(t)|\,|x(t)|\) grows like \(1/|t|\). These are conormal covectors of the smooth parabola \(x_2=x_1^2\). This explains the scalar step that fails in the larger base dimension. Neither calculation proves that every possible unbounded source neighborhood fails the wider existential neighborhood assertion.

### 7. A branched finite map retains its singular coefficient
*Difficulty: Intermediate.*

Take \(f(z)=z^m\) on \(\mathbb C\), with \(m\geq2\), \(G=k\), \(K=\{0\}\). Choose a source ball \(B_r\) and a target disc \(U=D_\delta\), with \(0<\delta<r^m\). Calculate the correct source neighborhood, both images, the monodromy and the original-microsupport bound.

**Solution.** Formula (3) gives \(V=\{|z|<\delta^{1/m}\}\), since this entire inverse-image disc is already inside \(B_r\). The map \(V\to U\) is finite and proper: the inverse image of a compact subset of \(U\) is closed and stays a positive distance from the source boundary. Consequently ordinary and proper-support images coincide. Finite fibres have no higher cohomology, so the output is concentrated in degree zero, with stalk \(k^m\) away from zero and stalk \(k\) at zero. Turning once around the origin cyclically permutes the \(m\) sheets. Proper base change justifies these stalks, and the specialization from the central stalk is the diagonal into the sheet coefficients. These modules are finite free and perfect.

The original microsupport is the zero section. For a downstairs covector \(\xi\), its transpose is \(m z^{m-1}\xi\). Away from zero this vanishes only for \(\xi=0\); at zero it vanishes for every \(\xi\). Thus (2) bounds the output by the zero section together with the full cotangent fibre at the branch point. The stalk jump makes the output nonconstant at that point, while complex cotangent conicity gives the expected full nonzero fibre there. Complex constructibility allows this analytic singular stratum; it does not require local constancy across a branch value.

## The geometry of the local construction

Three controls work together. The finite reciprocal cotangent chart retains a hypothetical bad inequality, so the canonical one-form forces the full sharp product to vanish. A finite coordinate-ball construction gives compact level sets around the prescribed compact part of the fibre, and the singular-form argument makes the selected critical values discrete. Finally the reciprocal of the distance to the outer level makes every finite closed level proper after the source is restricted.

The resulting neighborhood is a neighborhood of the chosen compact set, with no assertion of properness on the entire original source. Its microsupport bound uses only the original input over the inner closed threshold. In a Euclidean source the same construction with squared norm gives the ball intersected with the inverse image of a smaller target neighborhood. This retains complex constructibility without introducing the real target boundary created by an entire ball.

## References

M. Kashiwara and P. Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985): [Proposition 8.6.2, printed pp. 154–156](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=157), gives the local complex-constructible direct-image theorem over a complex curve; its statement is on pp. 154–155 and its proof concludes on p. 156. [Lemma 8.6.3, printed pp. 155–156](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=158), supplies the central cotangent equality and scalar pole-order argument; [Lemma 8.6.4, printed p. 156](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=159), gives the discrete-critical-value mechanism. The weak-coefficient and separate perfect-stalk conclusions follow here from the linked programme theorems. The finite coordinate-ball exhaustion, its \(C^2\) subanalytic critical-value argument, and the reciprocal cutoff are given explicitly above. The examples distinguish the full neighbourhood theorem from stronger ball and higher-dimensional cotangent claims.