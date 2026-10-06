# Isotropic cotangent transport and discrete critical values

Suppose a function has derivative constrained to an isotropic cotangent set. Why should its selected values be locally finite? There are two issues: selected points may escape to infinity, and selected values may accumulate near a point that stays in a compact set. Properness controls the first issue. An analytic curve and the canonical one-form settle the second.

We first prove this directly on the source manifold. We then establish the two cotangent transports, including their singular-set form calculus and the variable-rank linear-image argument. This also recovers the critical-value conclusion through the cotangent bundle of the line. Manifolds are finite dimensional, real analytic, Hausdorff and countable at infinity. Conic means invariant under every strictly positive fibre scale. No coefficient ring or sheaf finiteness condition enters these geometric results.

Kashiwara–Schapira's [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/) uses canonical forms to establish proper cotangent transport. We give its compactness and singular-form steps below, alongside a direct critical-set proof using analytic curve selection.

*Programme exposition: CC0. AI contributors: GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, October 2026.*

## Exact geometric inputs {#geometric-inputs}

We use the following foundational results as prerequisites:

1. Subanalytic sets are closed under finite Boolean operations, closure and analytic inverse image. Their regular loci are subanalytic and dense. A regular point has an ambient neighborhood in which the set is a closed analytic submanifold.
2. If a point lies in the closure of a subanalytic set, an analytic curve through that point enters the set at every sufficiently small positive parameter. Squaring the parameter gives a two-sided version if needed. This applies to the auxiliary subanalytic sets used below.
3. An analytic map proper on the closure of a subanalytic subset has subanalytic image of that subset. The subset itself need not be closed.
4. Every closed subanalytic set admits a proper surjective analytic parametrization by a manifold. For the analytic map in (C9), we use the analytic critical-value theorem, (A1)–(A8). Its analytic Taylor, implicit-function and constant-rank inputs remain explicitly stated calculus prerequisites.

Subanalytic sets and limiting tangent directions states the geometric prerequisites in their wider normal-cone setting. Its local curve-selection reduction identifies the required analytic preparation and cell/Puiseux inputs. Here items 1–2 suffice for the direct critical-value proof, together with elementary compactness and one-variable calculus. Items 3–4 enter the general image theorems later.

## Testing a one-form along approaches to a singular set {#singular-form-calculus}

For an analytic one-form \(\theta\) and subanalytic \(E\subset M\), write \(\theta|_E=0\) when the form kills every tangent vector at every regular point of \(E\). It does not mean that the ambient covector is zero. In a coordinate chart define the point cone by

\[
C_x(E)=\{v:\ z_j\in E,\ z_j\to x,\ c_j>0,\ c_j\to\infty,
\ c_j(z_j-x)\to v\}.
\tag{C1}
\]

The definition also makes sense at \(x\notin E\). Coordinate changes carry the limiting vector by their derivative, by first-order Taylor expansion.

**Form test.** The condition \(\theta|_E=0\) is equivalent to \(\theta_x(v)=0\) for every ambient \(x\) and \(v\in C_x(E)\).

**Proof.** First, replacing \(E\) by its regular locus does not change (C1). Given a representing sequence, density provides regular \(w_j\) with \(\|w_j-z_j\|<1/(j c_j)\). The scaled error tends to zero. The same argument shows \(C_x(E)=C_x(\overline E)\).

Suppose \(v\ne0\) is in (C1). In a chart around \(x\), the subanalytic set

\[
\{(z,r,w):z\in E_{\mathrm{reg}},\ r>0,\ z-x=rw\}
\tag{C2}
\]

has \((x,0,v)\) in its closure: take \(r_j=1/c_j\) and \(w_j=c_j(z_j-x)\) after the regular approximation. Curve selection gives analytic \(z(t),r(t),w(t)\), with that endpoint, lying in (C2) for positive \(t\). There is a finite \(k\ge1\) and \(b>0\) with \(r(t)=bt^k+O(t^{k+1})\), since \(r\) is analytic, positive for positive \(t\), and zero at zero. Consequently

\[
z(t)=x+bt^k v+O(t^{k+1}),\qquad
0=\theta_{z(t)}(z'(t))=bk t^{k-1}\theta_x(v)+O(t^k).
\tag{C3}
\]

At each positive parameter the curve lies locally in the regular manifold, so the first equality to zero follows from the hypothesis. Divide by \(t^{k-1}\) and take the limit. The zero vector needs no argument. Conversely any tangent vector at a regular point is obtained in (C1) from a smooth curve with that derivative. This proves the equivalence. \(\square\)

**Analytic pullback, closure and union.** If \(h:M'\to M\) is analytic, \(E',E\) are subanalytic, and \(h(E')\subset E\), then

\[
\theta|_E=0\quad\Longrightarrow\quad(h^*\theta)|_{E'}=0.
\tag{C4}
\]

Indeed, a sequence for \(v\in C_{x'}(E')\) gives
\(c_j(h(z_j)-h(x'))\to dh_{x'}v\): the first-order remainder multiplied by \(c_j\) tends to zero because \(c_j\|z_j-x'\|\) is bounded. Apply the form test. Equality of the cones of \(E\) and \(\overline E\) proves that vanishing passes to the closure and back. For a locally finite union, every convergent sequence lies locally in finitely many members; a subsequence lies in one member. Thus its point cone is the union of their cones, and vanishing on the members implies vanishing on their union. In particular, (C4) applies to a subset wholly contained in the singular locus; regularity of its image points is not assumed.

For \(T^*X\), let \(\alpha_X\) be the canonical one-form, \(\alpha_{(x,\xi)}(v)=\xi(d\pi(v))\). A conic subanalytic \(\Lambda\) is isotropic here when \(\alpha_X|_\Lambda=0\). This agrees with symplectic isotropy on its regular locus: in coordinates \(\alpha=\sum\xi_i dx_i\), \(d\alpha=\sum d\xi_i\wedge dx_i\); the radial vector \(R=\sum\xi_i\partial_{\xi_i}\) is tangent to the regular locus and satisfies \(\iota_Rd\alpha=\alpha\). Hence vanishing of the two-form implies vanishing of the one-form, while differentiating the pulled-back one-form proves the converse.

<span id="the-microlocal-bertinisard-theorem"></span>

## Critical values directly from analytic curves {#direct-critical-set-proof}

Let \(\varphi:X\to\mathbb R\) be analytic and \(\Lambda\subset T^*X\) closed, conic, subanalytic and isotropic. Assume that \(\varphi|_{\pi(\Lambda)}\) is proper. The selected values are

\[
S_\varphi
=\{\varphi(x):d\varphi_x\in\Lambda\}.
\tag{9}
\]

**Microlocal Bertini–Sard theorem.** The set \(S_\varphi\) is closed and locally finite in the ambient line. Equivalently, every compact interval meets it in a finite set.

**Proof.** Introduce the analytic derivative section \(s(x)=(x,d\varphi_x)\). Its selected source set is

\[
E=s^{-1}(\Lambda),\qquad s^*\alpha_X=d\varphi,
\qquad d\varphi|_E=0.
\tag{C5}
\]

The set \(E\) is closed and subanalytic, and the final assertion follows from (C4). If \(x_0\in E\), then \(\varphi\) is constant on \(E\) in some neighborhood of \(x_0\). Otherwise the subanalytic set \(E\setminus\varphi^{-1}(\varphi(x_0))\) would have \(x_0\) in its closure. Select an analytic curve \(\gamma\) through \(x_0\) entering this set. Apply (C4) to \(\gamma:(0,\epsilon)\to E\). Then

\[
(\varphi\circ\gamma)'(t)=0\quad(0<t<\epsilon),
\qquad \varphi(\gamma(t))=\varphi(x_0).
\tag{C6}
\]

The second equality follows from the first by the mean value theorem and continuity at zero. It contradicts the chosen set. This argument needs no connected-component enumeration, uniformization or Sard theorem.

For compact \(J\subset\mathbb R\), the set \(\pi(\Lambda)\cap\varphi^{-1}(J)\) is compact by the stated properness. The closed subset \(E\cap\varphi^{-1}(J)\) is compact too. The neighborhoods on which \(\varphi|_E\) is constant cover it, so finitely many suffice. Its image \(S_\varphi\cap J\) is therefore finite. A subset of the line finite on every compact interval is locally finite and closed: a convergent sequence of distinct points would lie in a single compact interval. \(\square\)

The support includes zero covectors. Positive conicity and closedness imply

\[
\pi(\Lambda)=\{x:(x,0)\in\Lambda\}.
\tag{C7}
\]

Indeed, scaling any member of a nonempty fibre to zero stays in the closed set; the reverse inclusion is immediate. Thus the support is itself closed and subanalytic. Properness is required only there, not on all of \(X\).

The same proof applies to the negative test \(-d\varphi_x\in\Lambda\), using \(s_-(x)=(x,-d\varphi_x)\) and \(s_-^*\alpha=-d\varphi\). Each signed value set is closed and locally finite; so is their union. The hypotheses impose positive conicity, not invariance under the antipodal map.

## Detecting vanishing after a surjective analytic map {#surjective-form-detection}

The transport theorems need the converse of (C4). Suppose \(h(E')=E\), with both subsets subanalytic. Then

\[
(h^*\theta)|_{E'}=0\quad\Longrightarrow\quad\theta|_E=0.
\tag{C8}
\]

To prove it, pass to \(T=\overline{E'}\) using the closure argument above and choose a proper analytic uniformization \(q:W\to T\). Pullback gives \((hq)^*\theta=0\) on the manifold \(W\). Around a regular point of \(E\), choose \(V\) such that \(E\cap V=N\) is a closed analytic submanifold of \(V\). Then \(\overline E\cap V=N\). Continuity and surjectivity give \(E\subset h(T)\subset\overline E\), so

\[
hq:(hq)^{-1}(V)\longrightarrow N
\quad\text{is surjective.}
\tag{C9}
\]

The domain \((hq)^{-1}(V)\) is an open analytic manifold and the map (C9) is analytic into the embedded analytic manifold \(N\). Both have countable atlases. For positive-dimensional \(N\), the analytic critical-value theorem makes regular values dense in each target chart: critical values have measure zero, and surjectivity ensures a lift at every value. This invokes only that theorem's standalone calculus proof, not the later conormal or isotropic results in its host lesson. At a regular value, an onto differential lifts every tangent vector of \(N\); the zero pullback therefore kills every such vector. Continuity of \(\theta|_N\) extends this to all points of \(N\). When \(\dim N=0\), tangent spaces vanish. This proves (C8) at every regular point. Properness was used for the available uniformization; it was not imposed on \(h\), and we did not infer that an arbitrary analytic image is subanalytic.

## The two cotangent maps {#the-two-maps-have-different-targets}

For an analytic \(f:Y\to X\), set

\[
C_f=Y\times_XT^*X,
\qquad
f_\pi:C_f\to T^*X,
\qquad
f_d:C_f\to T^*Y.
\tag{1}
\]

Their action is

\[
f_\pi(y;\xi)=(f(y);\xi),\qquad
f_d(y;\xi)=(y;df_y^t\xi).
\tag{2}
\]

They commute with positive fibre scaling, and the second is linear over \(Y\), with no constant-rank hypothesis. In local coordinates both pulled-back canonical forms are \(\sum_i\xi_i\,d f_i(y)\). Thus

\[
f_d^*\alpha_Y=f_\pi^*\alpha_X
\quad\text{on }C_f.
\tag{3}
\]

These conventions use the transpose differential with its displayed positive sign. No antipodal map enters this identity.

## Proper direct transport {#proper-direct-transport}

Given conic subanalytic isotropic \(\Lambda_Y\subset T^*Y\), define

\[
A=f_d^{-1}(\Lambda_Y)\subset C_f,
\qquad
D_f(\Lambda_Y)=f_\pi(A).
\tag{5}
\]

**Direct-transport theorem.** If the actual restriction \(f_\pi|_A:A\to T^*X\) has compact inverse images of compact sets, then \(D_f(\Lambda_Y)\) is closed, conic, subanalytic and isotropic. Closedness of \(\Lambda_Y\) is not an additional hypothesis.

**Proof.** The set \(A\) is subanalytic and conic. Its stated properness forces it to be closed in the correspondence manifold: if \(a_j\in A\) converges to \(a\), the images and their limit form a compact target set \(K\). The compact inverse image of \(K\) in \(A\) is also compact, hence closed, in the Hausdorff ambient manifold. It contains \(a\). First countability turns this sequential argument into closedness. Now the map is proper on \(\overline A=A\); foundational input 3 makes its image subanalytic.

A converging sequence in the image has preimages in the compact inverse image of the sequence together with its limit. Compactness gives a convergent subsequence with the required limiting image, so the image is closed. Conicity follows from fibre scaling. Finally (C4) and (3) give \((f_\pi^*\alpha_X)|_A=(f_d^*\alpha_Y)|_A=0\). Apply (C8) to the surjection from \(A\) onto its now-known subanalytic image. \(\square\)

There is also a distinct weaker image assertion. If only \(f_\pi|_{\overline A}\) is proper, input 3 and the same form argument still give a conic subanalytic isotropic image of \(A\). They do not make that image closed. Neither version assumes global properness of the base map.

## Variable-rank linear images and inverse transport {#isotropic-inverse-transport}

We supply the conic-image calculation used for the other direction. Work locally over a relatively compact base chart, using analytic bundle coordinates. Let \(L:E\to F\) be an analytic linear bundle map over the identity and \(H\subset E\) a positive-conic subanalytic set. Let \(D\) be the closed unit disk bundle and set

\[
H_0=H\cap D,\qquad B=L(H_0),\qquad L(H)=\mathbb R_{>0}B.
\tag{C10}
\]

Over every compact base set, \(D\) is compact. Thus \(L\) is proper on \(\overline{H_0}\), giving subanalytic \(B\). Also \(L(D)\) is closed and proper over the base: for a convergent image sequence, its base points lie in a compact set and its disk preimages have a convergent subsequence. Compactness over a compact base follows directly from continuity. Therefore \(\overline B\subset L(D)\) is proper over the base.

For any subanalytic \(B\subset F\) whose closure is proper over the base, its strictly positive saturation is subanalytic. To see this put \(\mu(t,e)=te\), \(p(t,e)=e\), and

\[
Q=\{(t,e):0<t\le1,\ te\in B\},\qquad
\mathbb R_{>0}B=\mu((0,1]\times B)\cup p(Q).
\tag{C11}
\]

The first image covers scales at most one, the second scales at least one. On the closure of the first domain, \(\mu\) is proper: a compact target set bounds the base, while \(\overline B\) over that base and \([0,1]\) are compact. For the second image, \(\overline Q\subset[0,1]\times F\), and its intersection with \([0,1]\times K\) is compact for every compact \(K\subset F\); hence \(p\) is proper on \(\overline Q\). Input 3 proves both images subanalytic. We image the original domains, so this calculation does not add zero vectors absent from \(B\). In (C10), every nonzero member of \(H\) can be positively scaled into the unit disk; any zero member is already there. This proves (C10), including kernel outputs, at variable rank.

**Inverse-transport theorem.** For conic subanalytic isotropic \(\Lambda_X\subset T^*X\), the set

\[
I_f(\Lambda_X)=f_d\bigl(f_\pi^{-1}(\Lambda_X)\bigr)
\tag{4}
\]

is conic, subanalytic and isotropic, without a noncharacteristic or rank assumption. Indeed, \(B=f_\pi^{-1}(\Lambda_X)\) is a conic subanalytic subset of the bundle \(C_f\to Y\). The linear-image calculation applies to \(f_d\). Equations (C4) and (3) make \(f_d^*\alpha_Y\) vanish on \(B\), and (C8) detects vanishing on its image. This is the ordinary transpose-differential image; it makes no claim to equal a limiting characteristic inverse.

## A second proof using the cotangent line {#why-a-one-dimensional-isotropic-image-has-isolated-covector-tests}

For conic subanalytic isotropic \(\Gamma\subset T^*\mathbb R\), consider

\[
i:\mathbb R\to T^*\mathbb R,
\qquad i(t)=(t;1),\qquad S=i^{-1}(\Gamma).
\tag{6}
\]

The section pulls \(a\,dt\) back to \(dt\), so (C4) gives

\[
dt|_S=0.
\tag{7}
\]

If distinct \(t_j\in S\) converged to any ambient \(t_0\), pass to points on one side and set \(c_j=1/|t_j-t_0|\). Then

\[
c_j(t_j-t_0)=1\quad\text{or}\quad-1.
\tag{8}
\]

The resulting nonzero cone vector contradicts the form test for \(dt\). This works even at a point outside \(S\) and does not assume \(\Gamma\) closed. Thus \(S\) is closed and locally finite.

Apply this observation to the function theorem. Its cotangent correspondence is \(C_\varphi=X\times\mathbb R_a\), with

\[
\varphi_d(x,a)=(x;a\,d\varphi_x),\qquad
\varphi_\pi(x,a)=(\varphi(x);a).
\tag{10}
\]

The incidence \(A=\varphi_d^{-1}(\Lambda)\) is closed. For compact \(K\subset T^*\mathbb R\), denote its projections to the base and covector coordinates by \(J\) and \(B\). The inverse image of \(K\) in \(A\) is a closed subset of

\[
\bigl(\pi(\Lambda)\cap\varphi^{-1}(J)\bigr)\times B,
\tag{11}
\]

which is compact by the support-properness assumption. This includes \(a=0\): membership in the incidence still requires a base point in \(\pi(\Lambda)\). Proper direct transport therefore gives a closed conic subanalytic isotropic \(\Gamma=\varphi_\pi(A)\), and

\[
S_\varphi=\{t:(t;1)\in\Gamma\}=i^{-1}(\Gamma).
\tag{12}
\]

The cotangent-line calculation proves the same critical-value conclusion. Unlike the earlier direct proof, this route also uses proper subanalytic images and surjective form detection. Keeping the routes separate makes their actual prerequisite requirements visible.

## Exercises with solutions

### Escape of source points allows accumulation of selected values

*Difficulty: Advanced.* Let \(\Lambda\subset T^*\mathbb R\) be the zero section together with every full fibre above a positive integer, and set \(\varphi(x)=1/(1+x^2)\). Determine the selected values and test the theorem's properness hypothesis.

**Solution.** The integer fibres are locally finite in the cotangent ambient. Each is closed and analytic, and its canonical form vanishes since its base coordinate is fixed. The zero section also has zero canonical form. The local finite-union rule proves isotropy, while locality proves closedness and subanalyticity. All fibres scale positively. The support is the whole line. On the zero section the test requires \(\varphi'(x)=-2x/(1+x^2)^2=0\), hence \(x=0\); each positive integer is selected because its whole fibre is present. Therefore

\[
S_\varphi=\{1\}\cup\{1/(1+m^2):m\ge1\}.
\tag{14}
\]

Zero is an accumulation value but is not a value of \(\varphi\). The selected points escape to infinity; \(\varphi^{-1}([0,1])=\mathbb R\) is not compact. Thus properness on the support fails. Individual isolation of every existing selected value does not imply closed local finiteness in the ambient line.

### Ordinary critical values on a closed analytic submanifold

*Difficulty: Intermediate.* Let \(N\subset X\) be a closed analytic submanifold with \(\varphi|_N\) proper. Identify its critical values through the theorem, and compute the case \(N=\{(u,v):v=u^2\}\), \(\varphi(u,v)=v\).

**Solution.** Take \(\Lambda=T_N^*X\). This is closed and conic. In submanifold coordinates it is an analytic bundle; a tangent vector to its total space projects to \(T_xN\), which its covector kills, proving canonical-form isotropy. Its support is exactly \(N\). The condition \(d\varphi_x\in T_N^*X\) is \(d(\varphi|_N)_x=0\), so the selected values are precisely the ordinary critical values. Their closed local finiteness follows under the given properness. On the parabola the restriction is \(u\mapsto u^2\), a proper function with derivative \(2u\). Its unique critical point is \((0,0)\) and its unique critical value is zero; equivalently \(dv(1,2u)=2u\).

### A quadratic function and two source strata

*Difficulty: Intermediate.* Take \(\varphi(x)=x^2\) and \(\Lambda\) equal to the zero section of \(T^*\mathbb R\) together with its full fibre over zero. Compute the transported set and both signed selections.

**Solution.** The two conormals form a closed conic subanalytic isotropic union. The support is all of \(\mathbb R\), on which \(x^2\) is proper. In (10), membership of \((x,2ax)\) requires \(a=0\) when \(x\ne0\), while every \(a\) is admitted when \(x=0\). Consequently

\[
\Gamma=\{(t;0):t\ge0\}\cup T^*_{\{0\}}\mathbb R_t.
\tag{13}
\]

Both slices \(a=1\) and \(a=-1\) select only \(t=0\). Directly, \(\pm2x\,dx\) lies in the zero section only when \(x=0\), and the full fibre adds that same point. Hence both signed value sets are \(\{0\}\).

### Proper incidence for a nonproper base map

*Difficulty: Intermediate.* For \(f(u,v)=u\), compute direct transport of the point conormal \(T^*_{\{(0,0)\}}\mathbb R^2\). Compare the properness condition with that for the source zero section.

**Solution.** In correspondence coordinates, \(f_d(u,v;\xi)=(u,v;\xi,0)\). Point-conormal membership forces \(u=v=0\); the incidence maps isomorphically to the closed target fibre \(T^*_{\{0\}}\mathbb R\). This map is proper, although the base projection has noncompact fibres. For the source zero section, incidence only forces \(\xi=0\), and the inverse image of the single output \((0;0)\) contains the entire line \((0,v;0)\). The hypothesis fails. The resulting image nevertheless happens to be the target zero section, showing that the sufficient properness condition is not necessary for isotropy in each particular example.

### A critical differential can collapse an ordinary inverse image

*Difficulty: Introductory.* For \(f(y)=y^3\) and \(\Lambda_X=T^*_{\{0\}}\mathbb R\), compare (4) with the conormal of the inverse-image point.

**Solution.** The base equation is \(y^3=0\), so \(y=0\). Every input covector is allowed, but \(df_y^t\xi=3y^2\xi=0\). The ordinary inverse transport is the single zero covector \((0;0)\), a zero-dimensional conic analytic isotropic set. The conormal of \(f^{-1}(0)=\{0\}\) is the full fibre. The difference reflects the actual zero derivative; no noncharacteristic condition was available to identify these sets, and a limiting inverse construction is a different operation.

## Sources and scope {#references-and-further-geometric-work}

Kashiwara and Schapira, [*Microlocal Study of Sheaves*](https://www.numdam.org/item/AST_1985__128__1_0/), Astérisque 128 (1985), develops the isotropic-set setting and canonical-form transport for locally closed subanalytic sets. The transport statements here allow arbitrary subanalytic subsets: the form test (C1)–(C4), uniformization and the proper-closure image theorem supply the required arguments for that broader convention.

The form test, pullback/closure/union rules, local constancy on the selected source set, compactness proof of finite values, surjective detection, conic linear-image calculation and cotangent-line comparison are proved above from the listed prerequisites. The subanalytic foundations and elementary analytic-calculus inputs remain prerequisites. The analytic critical-value theorem used in (C9) has its full argument in the linked section, independent of that lesson's later conormal results. The constructibility criterion for sheaves additionally requires microsupport and stratification results; it is not a conclusion of this geometric lesson.
