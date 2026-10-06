# Lorentz cones and their vertex characteristic cycles

A smooth cone boundary has an inward and an outward conormal. At its vertex, those conormals acquire additional fibre pieces. The distinction between a closed cone, its open interior and its punctured boundary changes both the pieces and their coefficients. We calculate these cycles from actual local support tests, duality and support triangles, including the dimension-dependent vertex signs.

Use Directional tests at a constructible boundary for the neighborhood definition of microsupport, Constructible costalks and Verdier duality for the natural costalk-to-dual-stalk pairing, and Antipodal duality and half-line characteristic cycles for the supported antipodal operation and its actual unit/evaluation compatibility. Integer coefficients and additive characteristic cycles supplies normalized conormals, integral dense-piece determination and additivity. The exact constant-interval and closed-cover prerequisites are SH02-CA-CONSTANT and SH02-CA-CLOSED-MV; the proper-support comparison is SH02-EX-BASECHANGE-BRIDGE. Their lower and transitive foundations remain open. We prove the special contraction and convex-vertex arguments needed here rather than importing a general cone computation.

Let \(k\) be a field of characteristic zero. Set \(d=n+1\), with \(n\geq0\), and work on the real analytic manifold \(X=\mathbb R_t\times\mathbb R_x^n\), with its standard orientation. Every sheaf below is the indicated constant coefficient extended by zero; it lies in \(D^b_{\mathbb R\text{-}c}(k_X)\) with finite perfect stalks. Cycle normalizations and orientation coefficients are those of the linked lessons.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## Open pieces and closed carriers

Put

\[
Z_\pm=\{\pm t\geq|x|\},\qquad Z_0=\{|t|\leq|x|\},
\qquad U_\epsilon=\operatorname{Int}(Z_\epsilon),
\qquad S_\pm=\{\pm t=|x|>0\}.
\qquad\text{(1)}
\]

Thus \(U_0=\{|t|<|x|\}\). For \(n=0\), this middle interior and both punctured boundaries are empty. For \(n\geq1\), each \(S_\pm\) is an analytic hypersurface of dimension \(n\): its points have \(x\ne0\), where the norm is analytic. All these sets are semialgebraic and hence subanalytic. The cone vertex is the single point \(o=(0,0)\).

Write \((t,x;\tau,\xi)\) for cotangent coordinates. Define the trimmed normalized chains

\[
\begin{aligned}
\sigma_\epsilon&=[T_X^*X]|_{U_\epsilon},\quad \epsilon\in\{+,0,-\},\\
\tau_{\epsilon_1,\epsilon_2}
&=[T_{S_{\epsilon_1}}^*X]|_{\{\epsilon_2\tau>0\}},
\quad \epsilon_1,\epsilon_2\in\{+,-\},\\
\gamma_\pm&=[T_o^*X]|_{\{\pm\tau>|\xi|\}},
\qquad \gamma_0=[T_o^*X]|_{\{|\tau|<|\xi|\}}.
\end{aligned}
\qquad\text{(2)}
\]

The first sign of \(\tau\) labels the base hypersurface; its second sign labels the time component of the covector. The \(\gamma_\pm\) restrictions are **strict** timelike regions. Their closed carriers include the light boundary \(\pm\tau=|\xi|\). A restriction in (2) is a chain with its frontier germs retained, not an independently closed cycle. The sums proved below have the required frontier cancellation.

These pieces partition the dense top-dimensional parts of the relevant conormals. Missing zero-section cone boundaries and missing light directions in the point fibre have dimension at most \(d-1\). The integral top-chain injection therefore gives

\[
[T_X^*X]=\sigma_++\sigma_0+\sigma_-,\qquad
[T_o^*X]=\gamma_++\gamma_0+\gamma_-.
\qquad\text{(3)}
\]

This reasoning includes \(n=0\): the omitted origin in a line has dimension zero, while the chains have dimension one. It does not discard frontier boundary terms.

## Contractions identify the actual constant-section map

We need constant cohomology on some nonconvex test cuts. The following argument derives it from proper interval projection.

Let \(Y\) be a nonempty contractible locally compact Hausdorff subspace of a finite-dimensional Euclidean space. The projection \(p:Y\times[0,1]\to Y\) is proper: the preimage of a compact set is its product with a compact interval. Proper base change and constant-interval acyclicity identify the stalks of the actual unit

\[
k_Y\longrightarrow Rp_*k_{Y\times[0,1]}
\qquad\text{(4)}
\]

with \(k\to R\Gamma([0,1];k)\), the constant-section isomorphism. Thus (4) is an isomorphism. On derived global sections, both endpoint restrictions are inverses of the same projection pullback. For any homotopy \(H:Y\times[0,1]\to Y\), the two end maps therefore induce the same map on \(R\Gamma(Y;k)\), by composing their endpoint restrictions with \(H^*\).

Apply this to a contraction from the identity to the constant map through a chosen point. The latter map factors through \(R\Gamma(\{\mathrm{pt}\};k)=k\). Point restriction and the constant-section map have both composites equal to the identity, the second by the homotopy argument. Consequently

\[
k\xrightarrow{\sim}R\Gamma(Y;k_Y).
\qquad\text{(5)}
\]

For every inclusion between two such spaces, the restriction in these identifications is the identity on \(k\), because it restricts the same constant section. No nonproper fibrewise base-change claim was used. The argument also explains exactly which map occurs in the localization calculation below.

## Uniform tests at a closed convex vertex

Take \(C=Z_+\), and write \(q(t,x)=\tau t+\xi\cdot x\). Its positive polar is

\[
C^\circ=\{(\tau,\xi):\tau\geq|\xi|\}.
\qquad\text{(6)}
\]

Indeed, if \(\tau\geq|\xi|\), then \(q(t,x)\geq(\tau-|\xi|)t\geq0\) on \(C\). If \(\tau<|\xi|\) and \(\xi\ne0\), evaluation on \((1,-\xi/|\xi|)\) is negative. Moving its spatial component slightly towards zero keeps that evaluation negative and gives a vector in \(\operatorname{Int}C\). If \(\xi=0\), necessarily \(\tau<0\), and \((1,0)\) serves. Thus outside the polar there is an interior vector \(v\) with \(q(v)<0\).

Fix that \(v\). Choose a complement \(H\) to its span. In coordinates \(z=y+sv\), the cone is a Lipschitz epigraph

\[
C=\{y+sv:s\geq g(y)\}.
\qquad\text{(7)}
\]

Here is the elementary geometry behind this assertion. Choose \(\eta>0\) with \(v+B_\eta\subset C\). For each \(y\), sufficiently large positive \(s\) puts \(y+sv\) in \(C\); sufficiently negative \(s\) makes its time coordinate negative. Closedness, convexity and stability under addition by \(v\) make the allowed parameters a closed ray. Its first value is \(g(y)\). For \(\delta\in H\), the vector \(\delta+(|\delta|/\eta)v\) lies in \(C\). Adding it to a point of \(C\) and then interchanging \(y,y+\delta\) proves

\[
|g(y+\delta)-g(y)|\leq |\delta|/\eta.
\qquad\text{(8)}
\]

Now choose a cotangent neighborhood of \((o,q)\) on which the evaluation of every covector on \(v\) is negative, bounded away from zero. For any allowed \(C^1\) test \(\varphi\), at any testing point \(a\in C\) in that neighborhood, continuity lets us use a small box centered at \(a\) on which \(\partial_s\varphi<-c<0\). Subtract \(\varphi(a)\). Strict monotonicity and the intermediate value theorem give a unique continuous graph \(s=h(y)\) on a smaller base ball, with \(h(0)=0\), such that

\[
\varphi(y,s)<\varphi(a)\quad\Longleftrightarrow\quad s>h(y).
\qquad\text{(9)}
\]

Continuity is not an unproved implicit-function step: the derivative bound makes a change of root at most the change of the function at the old root divided by \(c\). Uniform continuity on a smaller closed box therefore gives continuity of \(h\).

Write the translated epigraph threshold as \(g_a\); because \(a\in C\), \(g_a(0)\leq0\). Choose the base ball so small that \(g_a(y),h(y)<\varepsilon/4\), with vertical coordinate in \((-\varepsilon,\varepsilon)\). Both

\[
A=C\cap\text{box},\qquad
A_<=C\cap\text{box}\cap\{\varphi<\varphi(a)\}
\qquad\text{(10)}
\]

are nonempty and contractible. Move every vertical coordinate linearly to \(\varepsilon/2\); the entire path retains \(s\geq g_a(y)\), and for \(A_<\) retains \(s>h(y)\). Then contract the base ball at that common height. The sets are locally compact: they are the intersection of a closed cone with an open set. Formula (5) makes the actual restriction from the constant stalk to sections on \(A_<\) the identity \(k\to k\), with no higher cohomology. These boxes can be taken arbitrarily small. Localization thus gives

\[
\bigl(R\Gamma_{\{\varphi\geq\varphi(a)\}}k_C\bigr)_a=0.
\qquad\text{(11)}
\]

At points outside \(C\), shrink to its open complement. The fixed cotangent neighborhood, chosen before \(a\) and \(\varphi\), works for all the tests just described. Hence every vertex covector outside (6) is absent from microsupport. This proves a neighborhood statement, not merely vanishing for one linear test.

Conversely, if \(q\in C^\circ\), the linear function \(q\) is nonnegative on all of \(C\). Its supported sheaf equals \(k_C\) near the vertex, so its support-test stalk is \(k\ne0\). Every such covector belongs to microsupport. Together,

\[
SS(k_{Z_+})\cap T_o^*X=C^\circ.
\qquad\text{(12)}
\]

Away from the vertex, the constant interior has only zero covectors. On \(S_+\), the analytic coordinate \(u=t-|x|\) straightens the support to \(u\geq0\). The closed-half-line test with the constant tangential coordinates gives precisely the positive conormal multiples of \(du\). For completeness, negative normal covectors are excluded by the same monotone epigraph boxes as above. A covector with a nonzero tangential component is excluded by using a tangent coordinate on which the test decreases; the half-space is invariant in that direction, and the cut and uncut boxes contract to the same slice over a contractible half-ball. Positive pure normal multiples have the nonzero linear support test. Thus the only nonzero smooth-boundary part is \(\tau_{+,+}\). Repeating with the coordinate \(-t\) proves the corresponding result for \(Z_-\), whose inward conormal is \(\tau_{-,-}\).

## The positive vertex germ is the actual point sheaf

Let \(A=C\setminus\{o\}\). The support triangle is

\[
k_A\longrightarrow k_C\xrightarrow{r}k_o\xrightarrow{+1}.
\qquad\text{(13)}
\]

For \(q\) strictly inside (6), there is \(b>0\) with \(q(z)\geq b|z|\) on \(C\). One may take any \(b<(\tau-|\xi|)/\sqrt2\). This strict inequality persists for nearby covectors. For every \(C^1\) test with such differential at \(o\), the mean-value estimate along the segment from \(o\) to \(z\in C\) gives \(\varphi(z)-\varphi(o)>0\) for all sufficiently small nonzero \(z\in C\). The local support of \(k_A\) is entirely in the closed test cut, so its support-test stalk equals its zero stalk at \(o\).

At nearby nonvertex points, \(k_A=k_C\), whose nonzero boundary normals have \(|\tau|=|\xi|\), and whose interiors are constant. They avoid the same strict timelike cotangent neighborhood. Thus \(SS(k_A)\) misses that neighborhood and (13) makes the actual restriction \(r\) a microlocal isomorphism there:

\[
(k_{Z_+})_{(o,q)}\simeq(k_o)_{(o,q)},
\qquad \tau>|\xi|.
\qquad\text{(14)}
\]

This is an isomorphism in the point-localized derived category, not equality of ordinary stalk ranks. At a positive conormal over \(S_+\), the support triangle for the local closed half-space identifies its sheaf with \(k_{S_+}\), since the open half-space is invisible in the inward direction. Normalized conormal cycles and microlocal invariance now give coefficient \(+1\) on \(\tau_{+,+}\) and \(\gamma_+\); the interior constant coefficient gives \(+1\) on \(\sigma_+\). The microsupport calculation excludes other top-dimensional pieces. Integral dense-piece determination, including frontier germs, proves

\[
CC(k_{Z_\pm})=\sigma_\pm+\tau_{\pm,\pm}+\gamma_\pm.
\qquad\text{(15)}
\]

For the minus cone the same restriction argument uses \(-\tau>|\xi|\). These are equalities of cycles through the vertex: the sum agrees with the existing characteristic cycle as a top chain, so its frontier cancels. No individual term is asserted to be a cycle on its own.

## Costalks fix the duality shift

We compute the dual rather than inferring it from a picture. At an interior point of \(C\), the point costalk of \(k_C\) is the ambient orientation coefficient in degree \(d\), namely \(k[-d]\) with the chosen orientation. At a smooth boundary point it is zero: a small closed half-ball and that half-ball with its boundary center removed are contractible, and their constant-section restriction is the identity by (5).

The same statement holds at the vertex. The link

\[
L=C\cap\{t^2+|x|^2=1\}
\qquad\text{(16)}
\]

is homeomorphic to the closed unit \(n\)-ball by \(u=x/t\); its inverse is
\((t,x)=(1,u)/\sqrt{1+|u|^2}\). The punctured cone in a small ball is \((0,\varepsilon)\times L\), hence contractible. The unpunctured intersection is convex. Their restriction is again \(k\to k\), so its fibre, the point costalk at \(o\), is zero. The link description includes \(n=0\), where \(L\) is one point.

Natural constructible duality identifies the dual stalk with the coefficient dual of that costalk. The dual therefore has zero stalks outside \(U_+\), and its restriction to \(U_+\) is the orientation sheaf in shift \([d]\). The actual open-extension counit is a stalkwise isomorphism and yields

\[
D_Xk_{Z_\pm}=k_{U_\pm}[d],\qquad
D_Xk_{U_\pm}=k_{Z_\pm}[d].
\qquad\text{(17)}
\]

The second equality follows from constructible biduality and reversal of the shift under the contravariant dual. No differentiation of a nonsmooth homeomorphism, or cotangent transport by one, is needed.

The supported antipode acts on the trimmed normalized pieces by

\[
\sigma_\epsilon^a=(-1)^d\sigma_\epsilon,\quad
\tau_{\epsilon_1,\epsilon_2}^a=(-1)^n\tau_{\epsilon_1,-\epsilon_2},\quad
\gamma_\pm^a=\gamma_\mp,\quad \gamma_0^a=\gamma_0.
\qquad\text{(18)}
\]

These signs use the base dimensions \(d,n,0\) of the corresponding conormals and their orientation coefficients. Combining (15), (17), actual antipodal duality and the shift rule gives

\[
CC(k_{U_\pm})
=\sigma_\pm-\tau_{\pm,\mp}+(-1)^{n+1}\gamma_\mp.
\qquad\text{(19)}
\]

The smooth open-boundary coefficient is always \(-1\): its sign is \((-1)^{d+n}=-1\). The vertex coefficient instead has sign \((-1)^d\). These two signs have different origins.

## Support triangles calculate both middle regions and the boundaries

The open complement of \(Z_0\) is the disjoint union \(U_+\sqcup U_-\). Its localization triangle is

\[
k_{U_+}\oplus k_{U_-}\longrightarrow k_X
\longrightarrow k_{Z_0}\xrightarrow{+1}.
\qquad\text{(20)}
\]

Let \(D=Z_+\cup Z_-\), a closed set with intersection \(Z_+\cap Z_-=\{o\}\). Actual restrictions, diagonal and difference give a stalkwise exact sequence

\[
0\longrightarrow k_D\longrightarrow k_{Z_+}\oplus k_{Z_-}
\longrightarrow k_o\longrightarrow0.
\qquad\text{(21)}
\]

At the vertex its maps are \(k\to k^2\to k\), diagonal then difference; elsewhere they are identities on the single present cone. Hence no open-cover interpretation is being substituted for this closed-cover sequence. The open complement of \(D\) is \(U_0\), with triangle \(k_{U_0}\to k_X\to k_D\xrightarrow{+1}\).

Finally let \(B_\pm=Z_\pm\setminus U_\pm=S_\pm\cup\{o\}\). Two support triangles give
\([k_{S_\pm}]=[k_{Z_\pm}]-[k_{U_\pm}]-[k_o]\). Apply the proved additive characteristic-cycle map to these actual triangles, and substitute (3), (15), (19). This proves every row of the following table.

| Sheaf &emsp; | Integral characteristic cycle |
| --- | --- |
| \(k_X\) | \(\sigma_++\sigma_0+\sigma_-\) |
| \(k_o\) | \(\gamma_++\gamma_0+\gamma_-\) |
| \(k_{Z_\pm}\) | \(\sigma_\pm+\tau_{\pm,\pm}+\gamma_\pm\) |
| \(k_{U_\pm}\) | \(\sigma_\pm-\tau_{\pm,\mp}+(-1)^{n+1}\gamma_\mp\) |
| \(k_{Z_0}\) | \(\sigma_0+\tau_{+,-}+\tau_{-,+}+(-1)^n(\gamma_++\gamma_-)\) |
| \(k_{U_0}\) | \(\sigma_0-\tau_{+,+}-\tau_{-,-}+\gamma_0\) |
| \(k_{S_\pm}\) | \(\tau_{\pm,+}+\tau_{\pm,-}-\gamma_0+\bigl((-1)^n-1\bigr)\gamma_\mp\) |

For example, (21) and the complement triangle give
\(CC(k_{U_0})=CC(k_X)-CC(k_{Z_+})-CC(k_{Z_-})+CC(k_o)\).
For \(S_+\), the \(\gamma_+\) coefficients cancel, whereas the remaining opposite timelike coefficient is
\(-(-1)^{n+1}-1=(-1)^n-1\). These computations explain the displayed covector signs and the coefficient \(-2\) that occurs in odd spatial dimension. All lower-dimensional frontier terms cancel because the equations were obtained by the characteristic-cycle map on genuine sheaf triangles.

## Exercises with complete solutions

### The light boundary is not the timelike interior

*Difficulty: Introductory.*

For \(\xi\ne0\), find a nonzero \(z\in Z_+\) on which \(q=(|\xi|,\xi)\) vanishes. Explain why the strict vertex-chain region in (2) differs from the closed microsupport fibre in (12).

**Solution.** Take \(z=(1,-\xi/|\xi|)\). It lies on \(S_+\) and \(q(z)=0\). Every strictly timelike positive covector is uniformly positive on nonzero future-cone directions, which is the margin used in (14). A light covector has no such margin. Microsupport is closed and includes all \(\tau\geq|\xi|\); the top-dimensional point-conormal chain is trimmed to \(\tau>|\xi|\), and its carrier closure includes that boundary. The light directions have dimension \(d-1\) in the point fibre and meet closures of the smooth-boundary conormals. They are retained by the chain frontier, not assigned a separate top-dimensional \(\gamma_+\) coefficient.

### A nonlinear test outside the polar

*Difficulty: Intermediate.*

Assume \(n\geq1\) and test \(k_{Z_+}\) at \(o\) with \(\varphi(t,x)=x_1+t^2\). Determine its local support complex, and compare the test \(\psi=t\). Give an interior cone direction controlling the first test.

**Solution.** The first differential is \((\tau,\xi)=(0,e_1)\), outside (6). Take \(v=(1,-e_1/2)\): it is strictly inside \(Z_+\), and \(d\varphi_o(v)=-1/2\). Nearby differentials retain negative evaluation on \(v\); along this direction the nonlinear derivative remains negative on a sufficiently small box. The epigraph construction (7)–(11) makes the smaller-value cut contractible and identifies the actual restriction with \(k\to k\). Its fibre is zero. For \(\psi=t\), the smaller-value cut misses \(Z_+\) entirely, so the support complex is \(k\) in degree zero. The nonlinear first calculation uses a neighborhood of the differential and monotonicity, rather than replacing all \(C^1\) tests by a single linear half-space.

### Two dimensions change the vertex parity

*Difficulty: Intermediate.*

Compare \(n=1\) and \(n=2\) in the open future cone, closed middle and punctured future boundary formulas. Which smooth-boundary coefficient is independent of this parity?

**Solution.** For \(n=1\), the open future vertex coefficient is \(+\gamma_-\); the closed middle has \(-\gamma_+-\gamma_-\); and the punctured future boundary has opposite timelike coefficient \(-2\gamma_-\), besides \(-\gamma_0\) and its two boundary conormals. For \(n=2\), those three coefficients become \(-\gamma_-\), \(+\gamma_++\gamma_-\), and zero on \(\gamma_-\), respectively. The open smooth-boundary coefficient is \(-\tau_{+,-}\) in both cases, since its antipodal conormal sign \((-1)^n\) combines with the ambient duality shift \((-1)^{n+1}\). Using the ambient dimension for both signs would give the wrong boundary answer.

### The zero-spatial-dimension specialization

*Difficulty: Intermediate.*

Set \(n=0\). Reduce all seven rows to the line formulas, including the middle regions and the punctured boundaries.

**Solution.** There are no \(\tau\) chains, \(\sigma_0=\gamma_0=0\), \(Z_0=\{o\}\), and \(U_0=S_+=S_-=\varnothing\). The two \(\sigma\) chains are the positive and negative zero-section rays, while \(\gamma_\pm\) are the corresponding point-fibre rays. The first two rows give their full sums. Closed half-lines give \(\sigma_\pm+\gamma_\pm\), and open half-lines give \(\sigma_\pm-\gamma_\mp\), since \((-1)^{n+1}=-1\). The closed-middle row is \(\gamma_++\gamma_-\), the point cycle. The open-middle row is zero. In the boundary row, \((-1)^n-1=0\) and all other terms vanish, as required for the empty sheaves. No connectedness assumption on a spacelike region was needed.

### A zero vertex stalk can carry a nonzero vertex cycle

*Difficulty: Advanced.*

Assume \(n\geq1\) and take a nonzero spacelike covector \(p=(o;\tau,\xi)\) with \(|\tau|<|\xi|\). Determine the actual localized objects \((k_{U_0})_p\) and \((k_{S_\pm})_p\) in terms of \((k_o)_p\). Compare their shifts with the \(\gamma_0\) coefficients.

**Solution.** The closed cone objects are invisible at \(p\) by (12) and its minus version. Their open interiors are invisible too, by (17) and dual microsupport. Localizing the triangle of (21) therefore gives \((k_D)_p\simeq(k_o)_p[-1]\). The complement triangle, with \((k_X)_p=0\), gives \((k_{U_0})_p\simeq(k_o)_p[-2]\). For \(B_\pm\), the triangle of open interior and closed cone makes \((k_{B_\pm})_p=0\). Its point-removal triangle gives \((k_{S_\pm})_p\simeq(k_o)_p[-1]\). Thus the two coefficients are \(+1\) and \(-1\), respectively, by the even and odd shift rules. All these sheaves have ordinary stalk zero at \(o\); that stalk cannot recover their microlocal vertex complexes or cycles. The two-step shift in the open middle is actual derived information behind its positive coefficient.

### Graded coefficients retain the same geometric signs

*Difficulty: Advanced.*

Take \(n=2\), and let \(P=k\oplus k^2[1]\). Calculate the cycles of \(P_{Z_+}\) and its Verdier dual, and verify antipodal compatibility. What changes for \(Q=k\oplus k[1]\)?

**Solution.** The Euler weight is \(\chi(P)=1-2=-1\), so the first cycle is \(-\sigma_+-\tau_{+,+}-\gamma_+\). Its dual is \(P^\vee_{U_+}[3]\), with Euler weight \((-1)^3\chi(P^\vee)=1\). The open-cone formula gives \(\sigma_+-\tau_{+,-}-\gamma_-\). Applying (18) to the first cycle gives exactly that result: the zero-section sign is \(-1\), the smooth hypersurface sign is \(+1\), and the point pieces are exchanged with sign \(+1\). For \(Q\), the Euler weight is zero, so both cycles vanish. The coefficient complexes and their sheaves remain nonzero, and their microsupport still records the cone directions: direct summands with nonzero tests cannot disappear by an Euler cancellation. Characteristic cycles forget that cancellation's graded constituents.

### A distant cap changes the compact index

*Difficulty: Advanced.*

Compute compactly supported cohomology for the constant sheaves on
\(C_1=Z_+\cap\{t\leq1\}\), \(C_1\setminus\{o\}\),
\(U_+\cap\{t\leq1\}\), and \(U_+\cap\{t<1\}\).
Explain why the last two have identical vertex-cycle germs despite different compact Euler characteristics.

**Solution.** The first set is compact and convex, so its ordinary and compact cohomology are \(k\) in degree zero. Point removal has the actual restriction \(k\to k\); its localization triangle makes the second compact cohomology zero. The third is the complement in \(C_1\) of its compact lateral boundary \(L_1=\{t=|x|,\ 0\leq t\leq1\}\). This boundary contracts to the vertex by scalar multiplication, so (5) gives its cohomology \(k\). Restriction from \(C_1\) to \(L_1\) is the constant-section identity. Its localization triangle therefore makes the third compact cohomology zero, including \(n=0\), when \(L_1\) is one point. The fourth is homeomorphic to \((0,1)\times B^n\), with \(B^n\) the open unit ball, by \((t,u)\mapsto(t,tu)\). This is an open \(d\)-ball up to homeomorphism, with compact cohomology \(k[-d]\). Their Euler characteristics are \(1,0,0,(-1)^d\). The last two sheaves agree on a neighborhood of the vertex, so their characteristic cycles agree there by locality. Their different compact indices involve the upper cap at \(t=1\); a vertex coefficient alone is not a whole-support compact index.

### The closed middle has a different dual vertex

*Difficulty: Advanced.*

Assume \(n\geq1\). Compute the point costalk of \(k_{Z_0}\) and the vertex stalk of its Verdier dual. Can \(D_Xk_{Z_0}\) equal \(k_{U_0}[d]\), as it does for the two convex closed cones? Compare their cycles.

**Solution.** The unpunctured middle cone in a small ball contracts to its vertex, so its ordinary cohomology is \(k\) by (5). Its link on the unit sphere is described by
\(t\in[-1/\sqrt2,1/\sqrt2]\) and \(x=\sqrt{1-t^2}\,u\), with \(u\in S^{n-1}\). Thus it is an interval times \(S^{n-1}\), and the punctured middle cone retracts to that sphere. For \(n=1\), it has two components and the actual restriction is diagonal \(k\to k^2\); its fibre is \(k[-1]\). For \(n\geq2\), the sphere has cohomology \(k\) in degree zero and \(k\) in degree \(n-1\). This follows inductively from the closed upper/lower hemisphere sequence: each hemisphere is a contractible compact ball and their intersection is the sphere of one lower dimension. The restriction from the cone is the constant-section isomorphism in degree zero. Its fibre therefore has a single cohomology group \(k\) in degree \(n\), namely \(i_o^!k_{Z_0}\simeq k[-n]\), with the spatial orientation fixing a generator. Natural costalk duality gives \((D_Xk_{Z_0})_o\simeq k[n]\). The open-middle extension has zero stalk at \(o\), even after shift, so the proposed isomorphism fails.

Applying (18) to the closed-middle row and comparing the open-middle row gives precisely

\[
CC(D_Xk_{Z_0})
=(-1)^dCC(k_{U_0})+(-1)^n[T_o^*X].
\]

The additional point-cycle coefficient agrees with the Euler weight of the nonzero dual vertex stalk. This cycle equation is not by itself a direct-sum decomposition of the dual sheaf. The noncontractible punctured middle link is the reason the convex-cone duality argument cannot simply be reused for this closed set.

## References

The characteristic cycle at the vertex of a Lorentz cone is a basic example in the theory of characteristic cycles of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). The polar, the uniform epigraph test, the proper-interval contraction, the vertex restriction, the costalk duality calculation and the support-triangle derivations are proved above, with the prerequisite lessons linked.
