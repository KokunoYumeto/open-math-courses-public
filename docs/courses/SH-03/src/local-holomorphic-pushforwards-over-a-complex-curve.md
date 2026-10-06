# Local holomorphic pushforwards over a complex curve

Over a complex curve, the relative cutoff condition can be arranged near any compact part of a fibre. The decisive point is not boundedness of every covector: a horizontal covector may tend to infinity. Analyticity and the canonical one-form force its pole to be weaker than the vanishing of the base coordinate. This gives a full characteristic inverse at the central fibre, a uniform compact cutoff band, and both constructible direct images.

Let \(k\) be a commutative ring of finite global dimension. All manifolds are Hausdorff, countable at infinity and of uniformly bounded finite dimension; all sheaf complexes are globally bounded. Let \(f:Y\to X\) be holomorphic with \(\dim_{\mathbb C}X=1\). Fix \(x_0\in X\), a nonempty compact \(K\subset f^{-1}(x_0)\), and a weakly complex constructible \(G\). Perfect complex constructibility means, additionally, that every stalk is perfect. The empty \(K\) case is immediate by taking an empty source neighborhood.

The local statement treated here belongs to the theory of direct images of \(\mathbb C\)-constructible sheaves under non-proper maps; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §8.6. We prove the compact-fibre neighbourhood statement and the unbounded-covector lemma in detail. The exhaustion in the bounded neighbourhood is reparameterized to satisfy every closed-level properness hypothesis. A ball intersected with a small inverse-image base neighbourhood has the stated property; the same statement for a whole centred ball fails, as the example below shows.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

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

The graph is closed because the manifolds are Hausdorff. Put \(\widetilde G=R\gamma_*G\). The closed embedding is proper, so Holomorphic operations and complex Fourier symmetries gives bounded weak complex constructibility, and perfect stalks in the perfect case. Its actual microsupport is

\[
\widetilde\Lambda
=\{(y,f(y);\zeta,\xi):
(y,\zeta+(df_y)^t\xi)\in\operatorname{SS}(G)\}.
\qquad\text{(5)}
\]

This is the closed-embedding microsupport equality, including all conormal directions and zeros. Thus a horizontal covector \((0,\xi)\) of the product belongs to \(\widetilde\Lambda\) exactly when \((df_y)^t\xi\in\operatorname{SS}(G)\).

It suffices to construct a product neighborhood \(W\subset Z\times U\) of \(\gamma(K)\). Its graph inverse image \(V=\gamma^{-1}(W)\) is a neighborhood of \(K\) in \(f^{-1}(U)\), and the two images of \(\widetilde G|_W\) under \(p\) identify with the images of \(G|_V\) under \(f_V\). Formula (5) will translate the product bound back to (2). We now write \(G,\Lambda,f\) for this product coefficient, its actual microsupport, and the projection \(Z\times X\to X\).

Let

\[
j:Z\simeq Z\times\{x_0\}\hookrightarrow Z\times X,
\qquad A_0=j^\sharp\Lambda.
\qquad\text{(6)}
\]

The full sharp inverse is closed subanalytic isotropic and complex-conic; the holomorphic graph-normal model also makes it analytic. We use these existing geometric results, not ordinary cotangent restriction in place of the sharp inverse.

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

Real analytic curve selection gives a real analytic curve through \(q\) lying in (11) for small positive real parameters. Extend its finite coordinate functions holomorphically to a complex disc. The identity theorem preserves the equations of \(\mathcal A\); it does not need to preserve the real inequality at complex parameters. The positive real branch retains that inequality. The function \(u(t)\) is holomorphic, vanishes at zero and is not identically zero. Shrinking the disc leaves it nonzero for every nonzero parameter. Consequently

\[
\xi(t)=1/u(t),\qquad
(z(t),x(t);\zeta(t),\xi(t))\in\Lambda
\quad(0<|t|\ll1)
\qquad\text{(12)}
\]

is a meromorphic cotangent arc with finite holomorphic \(z,x,\zeta\). This supplies the required compactification argument. A holomorphic arc chosen without retaining the bad inequality would not prove the assertion for an arbitrary bad sequence.

For a closed complex-conic isotropic analytic set, the complex canonical one-form vanishes on it. The singular-set pullback criterion in Subanalytic sets and limiting tangent directions applies to every analytic arc in the set, even one contained in its singular locus. Apply it to both real and imaginary parts of the complex canonical form. Pulling back along (12) yields

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

For a general product source we use the real analytic exhaustion prerequisite appearing in the source proof: choose a positive proper real analytic \(\varphi:Z\to\mathbb R\). Existence of such an exhaustion on the chosen real analytic manifold is an explicit geometry contract; it is not deduced from holomorphic properness of \(f\). Regard \(\varphi\) as independent of \(x\) on the product.

The closed isotropic \(A_0\) in (6) has closed base projection because it includes its zero covectors. Properness of \(\varphi\) therefore implies properness on \(\pi A_0\). The microlocal discrete-critical-value theorem in Isotropic cotangent transport and discrete critical values says that

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

The coefficient in the differential is positive. On this part of \(W\), (18) and positive conicity give the relative exclusion for \(\psi\); complex minus stability gives its negative version. Nonproper holomorphic pushforwards through cutoffs now applies to the projection of \(W\), with the genuine all-level hypothesis. It proves both bounded weak complex outputs and their perfect stalks when the input is perfect.

Its sharp threshold bound only uses points with \(\psi\leq t_0\), equivalently \(\varphi\leq s_1\), which lie inside \(W\). Thus it uses the original \(\Lambda\), with no new boundary covectors. Return through (4)–(5). A threshold witness for the product bound has \(\zeta=0\) and \((df_y)^t\xi\in\operatorname{SS}(G)\). It lies in the graph neighborhood \(V\). This proves (1)–(2) for the original map.

## Centered balls in the source germ

Suppose \(Y\subset\mathbb C^n\) is open, \(0\in Y\), \(f(0)=x_0\), and \(K=\{0\}\). In the graph reduction take \(\varphi(z)=|z|^2\). Choose \(R>0\) with \(\overline B_R\subset Y\), and truncate the central \(A_0\) to the closed base ball \(\overline B_R\). This is a closed conic subanalytic isotropic set with compact base projection. Apply the discrete-critical-value theorem to squared norm on this truncated set. Its selected values in \([0,R^2]\) are finite. Choose \(0<s_1<s_2<R^2\) below its least positive selected value, if there is one. In particular (17) holds throughout this small positive band; the differential may belong to \(A_0\) at zero, which is allowed.

The compact-band proof of (18) applies unchanged. The reciprocal \(\psi=(s_2-|z|^2)^{-1}\) has every finite closed level strictly inside \(B_{\sqrt{s_2}}\), hence compact over compact base sets; no global properness of squared norm on the original open \(Y\) is needed. The graph inverse image of \(W\) is exactly (3), with \(r=\sqrt{s_2}\). This proves the centered-ball germ version and retains (2).

The literal assertion that \(V\) can always be the whole \(B_r\), with \(V\subset f^{-1}(U)\) and both images constructible on that entire \(U\), is stronger. Exercise 5 disproves it. In common uses one studies the pushforward of a ball on a smaller target germ; its coefficient over that germ is precisely \(G|_{B_r\cap f^{-1}(U)}\). The distinction matters for a global statement on \(U\).

## More than one complex base coordinate

For several base coordinates, (13) becomes \(\sum\zeta_i z_i'+\sum\xi_j x_j'=0\). Unbounded products in different coordinates can cancel, so the one-variable Laurent bound does not follow. In fact the exact equality (7) fails, as Exercise 6 shows with a smooth complex hypersurface and its conormal. The printed higher-base-dimension warning concerns the wider neighborhood phenomenon. Our explicit example proves failure of the crucial cotangent lemma, and the whole-ball calculation proves failure of that stronger neighborhood choice; neither is presented as a proof that no possible source neighborhood exists in a higher-dimensional base.

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

Assume \(k\neq0\). Let \(Y=\mathbb C^2\), \(f(z_1,z_2)=z_1\), \(L=\{z_2=z_1\}\), and \(G=k_L\). Take \(K=\{0\}\). Prove that no entire centered ball \(V=B_r(0)\), \(r>0\), can satisfy the printed whole-ball assertion on an open \(U\) with \(V\subset f^{-1}(U)\). Then explain how (3) repairs the local statement.

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

## Exact dependencies and source comparisons

The lesson proves the compact-fibre neighborhood application, full one-dimensional central sharp equality, meromorphic witness through a finite reciprocal chart, Laurent estimate, uniform compact band, all-level reciprocal repair and the ball-with-base-restriction version.

The printed bounded-source exhaustion is repaired to enforce every closed level. The literal whole-ball strengthening is replaced by (3), with a complete complex-constructible counterexample supplied. The wider printed higher-base-dimension warning is distinguished from the exact failure of the central cotangent equality proved here. General complex realization nonequivalence remains a separate teaching target. The following course material develops nearby and vanishing cycles with their actual covering maps and coefficient shifts.
