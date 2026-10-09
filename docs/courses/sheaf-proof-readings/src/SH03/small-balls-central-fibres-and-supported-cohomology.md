# Small balls, central fibres and supported cohomology

The three small-ball comparisons can be read from one arrow between two coefficient complexes. The ordinary sections give its source, the punctured sections give its target, and supported sections give its fibre. We first calculate that arrow on an interval, including its closed endpoint and compact-support maps, then transfer the calculation along the proper scalar map \(h=|\varphi|^2\).

*Scope.* The scalar and support comparisons, uniform compact-cap implication, extension-continuity calculations, proper-image and closed-embedding microsupport formulas, deformation and zero-section criteria, and closed-cutoff argument are proved below. The [directional reading](directional-neighborhoods-and-the-compact-cap-test.md#from-the-cap-comparison-back-to-all-local-tests-compact-cap-converse) proves the cap-test converse, and the [limiting-boundary reading](limiting-covectors-at-open-boundaries.md) proves the arbitrary-open and missing-submanifold estimates. The [limiting tensor proof](limiting-covectors-at-open-boundaries.md#products-restriction-and-the-limiting-sum-limiting-tensor-estimate) treats arbitrary bounded coefficients over a ring of finite global dimension. The constructibility/microsupport criterion uses its linked subanalytic and microlocal prerequisites. The cotangent lesson supplies critical-value and cotangent-transport arguments relative to those subanalytic foundations.

*AI-written exposition: GPT-6 Astra (OpenAI), Ultra; worked solutions: GPT-6.1 Sol (OpenAI), Ultra. Original programme expression is dedicated to the public domain under CC0; human mathematical sources are credited below.*

The duality lesson proves the [constant-interval comparison](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#homotopy-invariance-from-a-proper-interval-proper-interval-homotopy), [closed-support localization](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#closed-support-and-its-bound-closed-support-bound), [proper-image fibre formula](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-derived-fibre-formula-and-c-soft-acyclicity-derived-proper-image-fibre) and [support-colimit comparison](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-actual-point-to-compact-comparison-point-to-compact-comparison) used here. Its proofs through the orientation section do not use this small-ball theorem. The application here concerns arbitrary weak coefficients; no perfectness is inferred from compactness of a fibre.

## The three comparisons

Let \(X\) be a finite-dimensional real analytic manifold, Hausdorff and countable at infinity. Let \(k\) be commutative of finite global dimension, let \(F\in D^b_{w\text{-}\mathbb R\text{-}c}(k_X)\), and let
\(\varphi:X\to\mathbb R^r\) be analytic. Assume \(\varphi\) is proper on the closed support of \(F\). No finite-generation or perfect-stalk hypothesis is imposed.

Write

\[
B_\epsilon=\{z:|z|<\epsilon\},\quad
\overline B_\epsilon=\{z:|z|\leq\epsilon\},\quad
B_{a,b}=\{z:a<|z|<b\},\quad S_c=\{z:|z|=c\}.
\tag{1}
\]

Every sheaf coefficient on an inverse image below means the ordinary restriction of \(F\) there. For a closed \(Z\subset X\), \(R\Gamma_Z(X;F)\) is derived cohomology with support in \(Z\).

**Small-ball theorem.** There is \(\epsilon_0>0\) such that the following natural maps are isomorphisms.

For \(0<\epsilon<\epsilon_0\), ordinary restriction gives

\[
R\Gamma(\varphi^{-1}\overline B_\epsilon;F)
\longrightarrow R\Gamma(\varphi^{-1}B_\epsilon;F)
\longrightarrow R\Gamma(\varphi^{-1}(0);F).
\tag{2}
\]

For \(0<\epsilon'<\epsilon<\epsilon_0\), inclusion of supports gives

\[
R\Gamma_{\varphi^{-1}(0)}(X;F)
\longrightarrow R\Gamma_{\varphi^{-1}\overline B_{\epsilon'}}(X;F)
\longrightarrow R\Gamma_c(\varphi^{-1}B_\epsilon;F).
\tag{3}
\]

The support of each coefficient contribution in the closed inner ball is compact and lies in the larger open ball; this specifies the second map in (3).

Finally, if
\(0\leq\epsilon^{\prime\prime}<\epsilon^{\prime\prime\prime}<\epsilon'\leq\epsilon<\epsilon_0\), ordinary restriction gives

\[
R\Gamma(\varphi^{-1}B_{0,\epsilon};F)
\longrightarrow R\Gamma(\varphi^{-1}B_{\epsilon^{\prime\prime},\epsilon'};F)
\longrightarrow R\Gamma(\varphi^{-1}S_{\epsilon^{\prime\prime\prime}};F).
\tag{4}
\]

The intermediate sphere lies strictly inside the annulus. In particular the last coefficient space is an inverse image in \(X\), where \(F\) is defined.

<a id="local-support-under-images"></a>
<a id="local-support-before-and-after-an-ordinary-image-local-support-under-images"></a>

## Local support before and after an ordinary image

We first supply the sheaf-theoretic image estimate used by the geometric argument. Let \(f:Y\to X\) be \(C^1\), and let \(G\in D^+(k_Y)\). The manifolds have the standing finite dimension bounds; neither constructibility nor finite coefficients are needed in this section. For a closed subset \(Z\) of a local open domain, write \(\mathcal L_ZG\) for the derived **sheaf** of sections supported in \(Z\). Its derived global sections are \(R\Gamma_Z(Y;G)\). This distinguishes a supported sheaf from a single complex of global sections.

For a real \(C^1\) function \(\psi\) near \(y\), its local support test is

\[
\mathcal T_{y,\psi}(G)
=\bigl(\mathcal L_{\{\psi\geq\psi(y)\}}G\bigr)_y.
\tag{T1}
\]

A covector \(p\) is outside \(\operatorname{SS}(G)\) when some open cotangent neighbourhood \(W\) of \(p\) has every test (T1) zero whenever \((y,d\psi_y)\in W\). The neighbourhood precedes the choices of point and function. This definition includes zero covectors and implies closedness and positive conicity: multiplying a test function by a positive constant preserves its support set and scales its differential.

Put \(S=\operatorname{supp}(G)\), the closure of the union of the nonzero cohomology stalks. Outside \(S\) the complex vanishes on a neighbourhood, so all its tests vanish there. Conversely, at a nonzero stalk the constant-function test is that stalk itself. Taking closure shows \((y,0)\in\operatorname{SS}(G)\) at every \(y\in S\). Hence the base projection of the actual microsupport is exactly \(S\).

For a closed \(Z\subset X\), there is a natural equality of derived sheaf operations

\[
\mathcal L_Z Rf_*G
\simeq Rf_*\mathcal L_{f^{-1}Z}G.
\tag{T2}
\]

Here is a resolution proof with its acyclicity checked. For a closed inclusion \(i:Z\hookrightarrow X\), the underived support functor is \(\underline\Gamma_Z=i_*i^!\). The functor \(i^!\) sends injectives to injectives because its left adjoint \(i_*\) is exact. The functor \(i_*\) also preserves injectives because its left adjoint \(i^{-1}\) is exact. Thus \(\underline\Gamma_Z\) preserves injectives. Likewise \(f_*\) preserves injectives by exactness of \(f^{-1}\).

For any sheaf \(I\), a section of \(f_*I\) on \(U\) vanishes on \(U\setminus Z\) exactly when its corresponding section of \(I\) vanishes on \(f^{-1}(U\setminus Z)\). Consequently \(\underline\Gamma_Z f_*I=f_*\underline\Gamma_{f^{-1}Z}I\), naturally on all opens. Apply this equality to a bounded-below injective resolution of \(G\). The preservation just proved shows that both sides compute the derived composites, proving (T2). This identity itself does not require properness.

Now assume \(f|_S\) is proper. The complex \(\mathcal L_{f^{-1}Z}G\) is still supported on \(S\): localization is local, and it vanishes where \(G\) vanishes. Write it as a closed direct image from \(S\) and resolve there by injectives. Their closed images on \(Y\) are injective and supported on \(S\), so their ordinary and proper images by \(f\) agree. The [derived fibre formula (F6)](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-derived-fibre-formula-and-c-soft-acyclicity-derived-proper-image-fibre) applies. Its compact and ordinary fibre sections agree on the compact coefficient support. It therefore turns (T2) into

\[
\bigl(\mathcal L_ZRf_*G\bigr)_x
\simeq R\Gamma\bigl(f^{-1}(x);
 (\mathcal L_{f^{-1}Z}G)|_{f^{-1}(x)}\bigr).
\tag{T3}
\]

The same statement holds after restricting to any open domain of a test function. Properness survives that base restriction. This is the precise point where a closed fibre may be used; the formula is not asserted for an arbitrary nonproper ordinary image.

<a id="proper-image-microsupport-proof"></a>
<a id="the-proper-image-microsupport-estimate-proper-image-microsupport-proof"></a>

## The proper-image microsupport estimate

In the cotangent correspondence set

\[
\begin{aligned}
A&=\{(y;\xi): (y,df_y^t\xi)\in\operatorname{SS}(G)\}
   \subset Y\times_XT^*X,\\
f_\pi(y;\xi)&=(f(y);\xi),\qquad
\Gamma=f_\pi(A).
\end{aligned}
\tag{T4}
\]

The set \(A\) is closed, and its base points lie in \(S\), including those with \(df_y^t\xi=0\). To prove that \(f_\pi|_A\) is proper, let \(K\subset T^*X\) be compact and let \(Q\subset X\) be its compact base projection. Its inverse image is a closed subset of

\[
\bigl(S\cap f^{-1}Q\bigr)\times_X K.
\tag{T5}
\]

The first factor is compact by support properness, and the fibre product is closed in the product of two compact spaces. Thus (T5) is compact. Proper maps between these locally compact Hausdorff spaces are closed, as proved in [(F1), the proper-fibre neighborhood argument](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#a-proper-map-shrinks-neighbourhoods-of-its-fibre-proper-fibre-neighbourhoods), so \(\Gamma\) is closed. It is conic because transpose differentials commute with positive scaling.

Take \(p\notin\Gamma\) and an open cotangent neighbourhood \(W\) of \(p\) disjoint from \(\Gamma\). If a \(C^1\) function \(\phi\) near \(x\) has \((x,d\phi_x)\in W\), then
\((y,d(\phi\circ f)_y)\notin\operatorname{SS}(G)\) for every \(y\in f^{-1}(x)\): otherwise (T4) would put \((x,d\phi_x)\) in \(\Gamma\).

Apply (T3) to \(Z=\{\phi\geq\phi(x)\}\). At each fibre point the restricted complex in its right side has stalk (T1) for \(\psi=\phi\circ f\), and that stalk is zero. A sheaf complex whose cohomology stalks all vanish is zero, so the whole fibre complex is zero. Hence the target local support test vanishes. The same argument works for every point and function with differential in the already chosen \(W\). By the neighbourhood-uniform definition,

\[
\operatorname{SS}(Rf_*G)\subset
f_\pi f_d^{-1}\operatorname{SS}(G),
\qquad f_d(y;\xi)=(y;df_y^t\xi).
\tag{T6}
\]

Properness on \(S\) also gives \(Rf_!G\simeq Rf_*G\), so the same estimate applies to that image. This proof includes critical points, zero covectors and arbitrary bounded-below coefficients. It proves an inclusion; no equality for every proper map is inferred. The classical support-test argument is Proposition 4.1.1(i), printed p. 61, of Kashiwara and Schapira's freely available [*Microlocal Study of Sheaves*](https://www.numdam.org/item/AST_1985__128__1_0/). The resolution argument (T2), the support check for (T3) and the compactness in (T5) supply the required operation details here.

<a id="closed-embedding-microsupport-proof"></a>
<a id="closed-embeddings-preserve-every-local-support-test-closed-embedding-microsupport-proof"></a>

## Closed embeddings preserve every local support test

Let \(i:S\hookrightarrow U\) be a closed smooth embedding and \(H\in D^+(k_S)\), with arbitrary stalk modules. For a local \(C^1\) function \(\psi\) on \(U\), the support identity underlying (T2) specializes to

\[
\bigl(\mathcal L_{\{\psi\ge\psi(x)\}}i_*H\bigr)_x
\simeq
\bigl(\mathcal L_{\{\psi|_S\ge\psi(x)\}}H\bigr)_x
\quad(x\in S).
\tag{E1}
\]

Here \(i_*\) is exact. On an injective resolution of \(H\), sections of its direct image supported in a target closed set are exactly sections supported in the inverse image. Closed direct image preserves injectives, since its left adjoint \(i^{-1}\) is exact. Thus the termwise equality derives to the displayed identity; no equivalence between different definitions of microsupport is imported.

**Closed-embedding formula.** With \(i_d:T^*U|_S\to T^*S\) restricting covectors and \(i_\pi\) including them in \(T^*U\),

\[
\operatorname{SS}(i_*H)=i_\pi i_d^{-1}\operatorname{SS}(H).
\tag{E2}
\]

The upper inclusion is (T6), since a closed embedding is proper. For the reverse, suppose a target covector \((x;\eta_0,\nu_0)\) is outside \(\operatorname{SS}(i_*H)\). Choose smooth product coordinates \((u,z)\) with \(S=\{z=0\}\), and a single open cotangent neighborhood \(W\) on which every target test vanishes. The preimage of \(W\) under the continuous map \((u,\eta)\mapsto(u,0;\eta,\nu_0)\) is an open neighborhood \(V\) of \((x,\eta_0)\) in \(T^*S\). Every intrinsic \(C^1\) test \(g\) at a point with \((u,dg_u)\in V\) has an ambient extension

\[
\widetilde g(u,z)=g(u)+\langle\nu_0,z\rangle.
\tag{E3}
\]

Its derivative at \((u,0)\) lies in \(W\), and (E1) identifies its zero local support test with the intrinsic test for \(g\). All tests in the same \(V\) therefore vanish, so \((x,\eta_0)\notin\operatorname{SS}(H)\). Outside \(S\) the image sheaf is zero locally. This proves equality, including zero intrinsic covectors and every conormal direction. The formula uses neither a rank assumption on a different map nor a finite-generation hypothesis.

The bounded-below scope in these two sections is justified at the resolution level: (T2) uses a bounded-below injective resolution, and the proper-fibre formula (F6) is already proved for bounded-below inputs. In (T4)–(T6), properness on the closed coefficient support supplies the required compactness, and the local tests annihilate the entire fibre complex. The identical supported-section equality and test-function extensions prove (E1)–(E3) in this scope. None of these arguments uses an upper cohomological truncation. The weakly constructible comparisons and the zero-section criterion below retain their separately stated bounded hypotheses.

<a id="deformation-proof"></a>
<a id="continuing-cohomology-through-a-compact-moving-boundary-deformation-proof"></a>

## Continuing cohomology through a compact moving boundary

The local-constancy criterion needs control of cohomology on nested balls. We prove the deformation result that supplies it. It applies to \(D^+\) complexes on locally compact Hausdorff spaces and uses no constructibility assumption. The human source is the freely available [Astérisque 128](https://www.numdam.org/item/AST_1985__128__1_0/), Theorem 1.4.3, printed pp. 30–31. The proof below includes the inverse-limit and endpoint arguments behind its continuation step.

We use two continuity calculations. First, [compact-neighborhood continuity (D5)](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#cohomology-near-a-compact-set-and-the-interval-bound-interval-cohomology-bound) extends to \(A\in D^+(k_X)\):

\[
\mathop{\mathrm{colim}}_{K\subset V\text{ open}}H^q(V;A)
\simeq H^q(K;A|_K)
\quad(K\text{ compact}).
\tag{N1}
\]

The same injective-complex proof applies. Restriction to an open preserves injectives, and restriction of each injective term to \(K\) is c-soft, hence acyclic for sections on the compact space. The bounded-below acyclic-resolution comparison used for the fibre formula therefore computes the right side. The compact-germ section identity holds termwise, and exact filtered colimits commute with cohomology. This verifies (N1) for bounded-below complexes, including ones not bounded above.

Second, for increasing opens \(V_n\) with union \(V\),

\[
0\longrightarrow\lim{}^1_n H^{q-1}(V_n;A)
\longrightarrow H^q(V;A)
\longrightarrow\lim_n H^q(V_n;A)\longrightarrow0.
\tag{N2}
\]

To verify the sequence and the degree \(q-1\), choose a bounded-below injective complex \(I\) and put \(C_n=\Gamma(V_n;I)\). Every restriction is degreewise surjective by flabbiness. For any tower \(M_n\) with restrictions \(r_n\), write

\[
\Delta:\prod_nM_n\to\prod_nM_n,
\qquad (a_n)\mapsto(a_n-r_n a_{n+1}).
\tag{N3}
\]

Its kernel is \(\lim M_n\); by definition its cokernel is \(\lim{}^1 M_n\). For the complexes \(C_n\), the map \(\Delta\) is degreewise onto: choose \(a_0\), then recursively lift \(a_n-b_n\) to \(a_{n+1}\). Its kernel is \(\Gamma(V;I)\), by sheaf gluing. Products of modules are exact, so the long exact cohomology sequence gives (N2). The same recursion shows \(\lim{}^1 M_n=0\) whenever the transitions are surjective. In particular, it vanishes for a constant system of isomorphisms. Constancy only in degree \(q\) would not remove the left term of (N2).

**Deformation theorem.** Let \(F\in D^+(k_X)\), let \(S\) be its closed cohomological support, and let \((U_t)_{t\in\mathbb R}\) be open subsets satisfying:

1. \(U_t=\bigcup_{s<t}U_s\).
2. \(S\cap\overline{U_t\setminus U_s}\) is compact whenever \(s<t\).
3. For the closed limiting front
   \[
   B_s=\bigcap_{t>s}\overline{U_t\setminus U_s},
   \tag{N4}
   \]
   every \(s\le t\) and \(x\in B_s\setminus U_t\) satisfy
   \[
   (\mathcal L_{X\setminus U_t}F)_x=0.
   \tag{N5}
   \]

Then restriction from \(R\Gamma(\bigcup_tU_t;F)\) to each \(R\Gamma(U_s;F)\) is an isomorphism, as is every restriction between members of the family. The endpoint \(s=t\) is included in (N5). The same statement holds for any nonempty open real parameter interval, by reparametrizing it increasingly by \(\mathbb R\).

**Compact reduction.** Closed restriction and direct image identify \(F\) with its complex on \(S\): the restriction unit is an isomorphism on all stalks. For \(W_t=U_t\cap S\),
\(\overline{W_t\setminus W_s}^{\,S}\subset S\cap\overline{U_t\setminus U_s}^{\,X}\).
The left side is closed in the compact right side, and its limiting front is contained in \(S\cap B_s\). Identity (E1), in its underlying closed-subspace form, identifies the support tests; smoothness was not needed for that identity. Cohomology on each open is also identified. Thus it suffices to prove the theorem with all \(\overline{U_t\setminus U_s}\) compact.

Fix \(s\). The compact sets \(K_t=\overline{U_t\setminus U_s}\), \(t>s\), shrink towards \(B_s\) as \(t\) decreases to \(s\). Every open neighborhood \(V\) of \(B_s\) contains some \(K_u\) with \(s<u\le t\), for any previously fixed \(t>s\). Otherwise the closed sets \(K_v\setminus V\), \(s<v\le t\), would have the finite-intersection property in the compact \(K_t\), yielding a point of \(B_s\setminus V\). This also proves the assertion when the front is empty. The front is disjoint from \(U_s\), since that set is open.

**Right continuity.** Put \(Q_s=\mathcal L_{X\setminus U_s}F\). We show

\[
\mathop{\mathrm{colim}}_{t>s}H^q(U_t;Q_s)=0.
\tag{N6}
\]

For \(t>s\), localization applied to \(Q_s\) has outside term \(\mathcal L_{X\setminus U_t}F\). Indeed, the two closed-support functors compose by intersection and preserve injectives as in (T2), while \(X\setminus U_t\subset X\setminus U_s\). If \(j_t:U_t\hookrightarrow X\), its triangle is

\[
\mathcal L_{X\setminus U_t}F\longrightarrow Q_s
\longrightarrow Rj_{t*}(Q_s|_{U_t})\xrightarrow{+1}.
\tag{N7}
\]

Both first terms vanish on \(B_s\), by (N5), including its endpoint case; at a point inside \(U_t\) the first term vanishes automatically. Hence the last term vanishes there too. Given \(a\in H^q(U_t;Q_s)\), apply (N1) to this last term on the compact \(B_s\). It makes the restriction of \(a\) zero on \(V\cap U_t\) for some open neighborhood \(V\) of \(B_s\). Here sections of \(Rj_{t*}\) on \(V\) are the derived sections on \(V\cap U_t\); the equality is obtained with the same injective resolution, since direct image preserves injectives.

Choose \(s<u\le t\) with \(K_u\subset V\). The opens \(U_s\) and \(U_u\cap V\) cover \(U_u\). The complex \(Q_s\) is zero on the first and on their intersection. The two-open Mayer–Vietoris triangle identifies \(R\Gamma(U_u;Q_s)\) with \(R\Gamma(U_u\cap V;Q_s)\), on which \(a\) is zero. For completeness, that triangle follows termwise from the sheaf gluing sequence on a flabby injective resolution: its difference map onto intersection sections is surjective. Thus the restriction of \(a\) is zero on \(U_u\), proving (N6).

Taking the localization triangle for \(U_s\) on \(U_t\), then an exact filtered colimit, gives

\[
\mathop{\mathrm{colim}}_{t>s}H^q(U_t;F)\xrightarrow{\sim}H^q(U_s;F).
\tag{N8}
\]

Its last term is constantly \(H^q(U_s;F)\), with identity restrictions, and (N6) kills the supported term in adjacent degrees. These are actual restriction maps.

**The real-parameter continuation argument.** An inverse system \(M_t\) with both natural maps

\[
\mathop{\mathrm{colim}}_{t>s}M_t\xrightarrow{\sim}M_s,
\qquad M_s\xrightarrow{\sim}\lim_{u<s}M_u
\tag{N9}
\]

has all its restrictions invertible. To prove injectivity, take an element at time \(b\) which vanishes at time \(a<b\). Its zero times in \([a,b]\) form a nonempty initial segment. At their supremum \(c\), the inverse-limit injectivity in (N9) gives zero at \(c\) if \(c>a\); if \(c=a\), zero is already known. If \(c<b\), the colimit injectivity gives zero at some time strictly larger than \(c\), a contradiction. Thus it vanishes at \(b\). To prove surjectivity, extend an element at \(a\) using the colimit map and consider the supremum of its extension times up to \(b\). Extensions are now unique, so before that supremum they form a compatible family. The inverse-limit surjectivity extends to the supremum, and the colimit surjectivity extends beyond it unless it equals \(b\). This proves extension to \(b\), including the case where the supremum is initially \(a\).

Choose \(N\) with \(F\in D^{\ge N}\). Derived sections have no cohomology below \(N\). Induct on \(q\ge N\). For any \(s\), choose \(s_n\uparrow s\); hypothesis 1 gives \(U_s=\bigcup_nU_{s_n}\). In degree \(q=N\), the left term of (N2) is zero. At every later degree it is zero by the already-proved constancy in degree \(q-1\). Thus (N2) provides the second isomorphism of (N9) for \(M_t=H^q(U_t;F)\), while (N8) provides the first. The continuation argument proves constancy in degree \(q\). Finally apply (N2) to \(\bigcup_{n\ge0}U_n=\bigcup_tU_t\); every \(\lim{}^1\) is now zero and the inverse limit identifies by restriction with every fixed stage. The resulting map is a cohomology isomorphism in every degree, proving the theorem in \(D^+\). \(\square\)

<a id="zero-section-criterion-proof"></a>
<a id="zero-microsupport-gives-a-constant-bounded-complex-zero-section-criterion-proof"></a>

## Zero microsupport gives a constant bounded complex

For \(F\in D^b(k_X)\) on a smooth finite-dimensional manifold, the following are equivalent:

1. \(\operatorname{SS}(F)\subset T_X^*X\), the zero section.
2. Locally, \(F\) is a constant bounded coefficient complex.
3. Every cohomology sheaf of \(F\) is locally constant.

The coefficient modules may be infinite. Condition 2 refers to the whole derived object and retains its extension data.

**From zero microsupport to actual descent.** Work in a coordinate neighborhood on which condition 1 holds and choose a ball \(B(x,R)\) whose closure lies in that neighborhood. For \(y\in B(x,R)\) and \(0<r<R-|x-y|\), interpolate centers and radii:

\[
c(t)=(1-t)y+tx,\quad \rho(t)=(1-t)r+tR,
\quad U_t=B(c(t),\rho(t)).
\tag{Z1}
\]

Use a slightly larger open parameter interval containing \([0,1]\). It can be chosen so that every radius is positive and the closures of all balls stay in a fixed compact subset of the coordinate neighborhood. Since \(R-r>|x-y|\), the triangle inequality gives \(\overline{U_s}\subset U_t\) for \(s<t\), and continuity gives the increasing-union property. The front (N4) is the sphere \(\partial U_s\): interior and exterior points are excluded by continuity, while each sphere point lies in every later ball and outside \(U_s\). It is contained in \(U_t\) for \(s<t\). At the only remaining endpoint \(s=t\), the complement of the ball is tested by \(\psi(z)=|z-c(s)|^2\), whose differential is nonzero on that sphere. Condition 1 makes each such local support test zero. All deformation hypotheses hold; hence the actual restriction

\[
R\Gamma(B(x,R);F)\xrightarrow{\sim}R\Gamma(B(y,r);F)
\tag{Z2}
\]

is an isomorphism. Let \(r\downarrow0\). With a fixed injective resolution, exact filtered colimits of these section complexes identify with the stalk complex, so (Z2) gives \(R\Gamma(B(x,R);F)\simeq F_y\) for every \(y\) in the original ball. Put \(C=R\Gamma(B(x,R);F)\). The adjunction counit is

\[
C_{B(x,R)}\longrightarrow F|_{B(x,R)}.
\tag{Z3}
\]

Its stalk maps are exactly the restriction maps just proved invertible. It is therefore an isomorphism of sheaf complexes. Since any stalk of this nonempty ball is bounded in the original global degree interval for \(F\), so is \(C\). This proves condition 2 without splitting cohomology degrees.

**Constant coefficients and the converse.** For a constant bounded coefficient complex \(C_U\), every \(C^1\) test at a nonzero covector has a submersion coordinate chart in which its support set is \(\{u_1\ge0\}\). The chart and its open negative half are products of contractible intervals. The [ordinary homotopy calculation](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#homotopy-invariance-from-a-proper-interval-proper-interval-homotopy), including its actual unit, identifies the derived sections of \(C_U\) on each with \(C\). Restriction is the identity under those units. The localization triangle consequently gives zero for the supported stalk. This applies to every nonzero test in a neighborhood of a nonzero cotangent point, so \(\operatorname{SS}(C_U)\) is contained in the zero section.

Condition 2 plainly gives condition 3 by exactness of the constant-sheaf functor. Conversely, under condition 3, only finitely many cohomology sheaves occur, so near a fixed point all of them can be made constant on a common open neighborhood. Each has microsupport in its zero section by the preceding argument. Finite truncation triangles then give the same bound for \(F\). To justify this last step directly, a local support functor sends a distinguished triangle to a triangle. Outside the union of the microsupports of two terms, intersect their two open testing neighborhoods. Every test for those two terms is zero, hence so is the test for the third. This proves the triangle microsupport inequality, and induction through the finite truncations proves condition 1. No assertion that arbitrary cohomology sheaves have microsupport contained in that of their complex was used. \(\square\)

Combining (E2) with this criterion gives the exact form used on strata:

\[
\operatorname{SS}(i_*H)\subset T_S^*U
\quad\Longleftrightarrow\quad
\operatorname{SS}(H)\subset T_S^*S
\quad\Longleftrightarrow\quad
H\text{ is locally a constant bounded complex}.
\tag{Z4}
\]

The middle covector restriction is surjective with kernel the conormal bundle. These proofs supply the closed-embedding and zero-section inputs of the constructibility criterion. The [missing-submanifold proof](limiting-covectors-at-open-boundaries.md#the-trace-across-a-missing-submanifold-missing-submanifold-trace) supplies its boundary estimate. The [limiting tensor proof](limiting-covectors-at-open-boundaries.md#products-restriction-and-the-limiting-sum-limiting-tensor-estimate) supplies the tensor input for bounded coefficients over a ring of finite global dimension. Involutivity and compatible microlocal stratification remain separate inputs.

<span id="proper-norm-square-and-both-signed-critical-sets"></span>

<a id="uniform-compact-cap-proof"></a>
<a id="one-compact-cap-works-for-an-entire-family-uniform-compact-cap-proof"></a>

## One compact cap works for an entire family

The deformation theorem gives more than a separate vanishing statement at each stalk. If many coefficient complexes avoid the same open set of covectors, the **same geometric cap and base** work for all of them. This is the form needed before taking limits of extensions. We prove this implication explicitly. Its [converse and directional sheaf projector](directional-neighborhoods-and-the-compact-cap-test.md#from-the-cap-comparison-back-to-all-local-tests-compact-cap-converse) are proved in the companion prerequisite reading.

Work in a coordinate open set \(X\subset\mathbb R^n\), and fix a nonzero covector \((x_0,\xi_0)\). Let \((F_\lambda)\) be any family in \(D^+(k_X)\). Suppose a single open cotangent neighborhood \(W\) of \((x_0,\xi_0)\) misses every \(\operatorname{SS}(F_\lambda)\). No common lower cohomological bound, constructibility, or finite-rank hypothesis on this family is needed. In this section the definition (T1) is used for bounded-below complexes, with the same localization and support operations.

Translate and linearly change coordinates so that \(x_0=0\) and \(\xi_0=dx_1\), and write \(x=(x_1,x')\). There are \(h,\delta>0\) and an open neighborhood \(V\) of zero such that, putting

\[
C=\{v:v_1\leq-\delta|v'|\},\quad
H=\{x:x_1\geq-h\},\quad L=\{x:x_1=-h\},\quad
K_x=(x+C)\cap H,\quad B_x=(x+C)\cap L,
\tag{U1}
\]

all \(K_x\), for \(x\in V\), lie in \(X\), are compact, and the actual restriction maps satisfy

\[
R\Gamma(K_x;F_\lambda)\xrightarrow{\sim}
R\Gamma(B_x;F_\lambda)
\qquad(x\in V,\ \lambda\text{ arbitrary}).
\tag{U2}
\]

Here and below coefficients on a compact set mean ordinary inverse image to that set. The constants, sets and maps in (U1) do not depend on \(\lambda\).

First take a small angular neighborhood of \(dx_1\) and a base neighborhood whose product lies in the positive conic enlargement of \(W\). Choose \(\delta\) so small that every \(dx_1+\eta\,dx'\) with \(|\eta|\leq\delta\) has direction in that angular neighborhood. Positive rescaling does not change a support test. Then choose \(h\) and the vertex neighborhood small enough that a slightly enlarged compact cap lies in the chosen base neighborhood. Compactness follows directly from \(-h\leq y_1\leq x_1-\delta|y'-x'|\). These choices use only \(W\), and ensure that all subsequent boundary tests vanish for every member of the family. Fix one \(F=F_\lambda\) during the proof. Extend it by zero to the ambient vector space; every boundary test we use is inside the original coordinate domain.

### An explicit analytic motion and its rim

For a permitted vertex \(a=(a_1,a')\) above \(L\), let \(R=h+a_1>0\), \(q=\delta^2|y'-a'|^2\), and \(D=a+\operatorname{Int}C\). For \(t>0\), define

\[
g_t(q)=R^2-(R^2-q)\exp\!\left(-\frac{R^2-q}{t}\right),
\qquad
D_t=\{y:y_1<a_1-\sqrt{g_t(q)}\}.
\tag{U3}
\]

The function \(g_t\) is positive: for \(q\geq R^2\) this is immediate, while for \(0\leq q<R^2\) it is at least \(q\), strictly so at \(q=0\). More generally \(g_t(q)\geq q\) for all \(q\geq0\). Thus \(D_t\subset D\), with strict separation from the side of \(D\) except along the rim on \(L\). The graph in (U3) is real analytic. Writing \(s=R^2-q\), differentiation gives

\[
\partial_t g_t=-\frac{s^2}{t^2}e^{-s/t}\leq0,
\qquad
\partial_q g_t=e^{-s/t}(1-s/t),\qquad
|\partial_q g_t|\leq1\quad(0\leq q\leq R^2).
\tag{U4}
\]

For the last inequality, \(|1-u|e^{-u}\leq1\) for \(u\geq0\): on \([0,1]\) both factors are at most one, and on \([1,\infty)\) the maximum of \((u-1)e^{-u}\) is \(e^{-2}\). Consequently the transverse derivative of \(\sqrt{g_t(q)}\) has norm at most \(\delta\sqrt{q/g_t(q)}\leq\delta\). All outward boundary differentials in \(H\) therefore have the permitted direction \(dx_1+\eta\,dx'\).

The domains increase continuously with \(t\), and their union is \(D\), since \(g_t(q)\to q\) as \(t\to\infty\). A point of \(L\) belongs to \(D_t\) exactly when \(q<R^2\); hence \(D_t\cap L=D\cap L\) for every \(t\). As \(t\downarrow0\), the closures of their portions in \(H\) shrink to \(\overline D\cap L\). Indeed every such point has \(q\leq R^2\), and \(g_t(q)\to R^2\) uniformly there, because \(0\leq s e^{-s/t}\leq t/e\). This uniform estimate will also control the compact limits below.

Let \(j:D\hookrightarrow\mathbb R^n\). To leave the whole region below the base fixed, apply deformation to

\[
A=Rj_*(F|_D),\qquad
U_t=D_t\cup(D\setminus H).
\tag{U5}
\]

The closure of every difference \(U_t\setminus U_s\), \(s<t\), is contained in the fixed compact cap \(\overline D\cap H\). The family is left continuous. Inside \(D\), a limiting front above \(L\) is a graph from (U3). At a later parameter it has entered \(U_t\), and at the parameter itself its support test vanishes by (U4). Outside \(D\), the only possible limiting-front points are the rim \(\partial D\cap L\). A point of the side strictly above \(L\) has a neighborhood disjoint from \(D_t\) for all parameters in a small interval about any fixed finite parameter, while the region below \(L\) is unchanged. At a rim point both \(D_t\) and \(D\) have analytic smooth boundaries with the permitted outward differentials. In dimension one there are no rim points; the same argument uses intervals.

We must check the support test on \(A\), rather than silently replace it by a test on \(F\) at a point outside \(D\). Put \(Z_t=D\setminus D_t\). Since \(Z_t\cap L=\varnothing\), its portions \(Z_t^+=Z_t\cap H\) and \(Z_t^-=Z_t\cap\{y_1\leq-h\}\) are disjoint closed subsets of \(D\), both open and closed in \(Z_t\). Therefore

\[
\mathcal L_{Z_t}(F|_D)
\simeq\mathcal L_{Z_t^+}(F|_D)\oplus
       \mathcal L_{Z_t^-}(F|_D).
\tag{U6}
\]

At a rim point \(y\), the two smooth support tests \((\mathcal L_{\mathbb R^n\setminus D_t}F)_y\) and \((\mathcal L_{\mathbb R^n\setminus D}F)_y\) vanish. Apply \(\mathcal L_{\mathbb R^n\setminus D_t}\) to the localization triangle for \(D\). Its composite with \(\mathcal L_{\mathbb R^n\setminus D}\) is the latter functor, because the second support is contained in the first. The resulting triangle gives \((\mathcal L_{\mathbb R^n\setminus D_t}A)_y=0\). By (T2) and (U6),

\[
\mathcal L_{\mathbb R^n\setminus U_t}A
\simeq Rj_*\mathcal L_{Z_t^+}(F|_D)
\quad\text{is a direct summand of}\quad
\mathcal L_{\mathbb R^n\setminus D_t}A.
\tag{U7}
\]

Its stalk at the rim is consequently zero. This checks the endpoint and later-parameter front conditions of (N5), including the rim. Reparametrizing \((0,\infty)\) by \(\mathbb R\), the proved deformation theorem applies and gives

\[
R\Gamma(D;F)\xrightarrow{\sim}R\Gamma(U_t;F).
\tag{U8}
\]

### Passing to the closed cap and its closed base

The fixed open region \(V_-=D\setminus H\) has closure in \(D\) contained in \(U_t\), since \(D\cap L\subset D_t\). Extension by zero of \(F|_{V_-}\) to \(D\) has closed support inside \(U_t\); restricting its derived sections from \(D\) to \(U_t\) is therefore an isomorphism. This follows by representing it as the direct image from its closed support and then taking sections there. In the two localization triangles for the closed upper part of \(D\) and of \(U_t\), the open-part comparison and (U8) are isomorphisms. Thus their third comparison is the actual restriction isomorphism

\[
R\Gamma(D\cap H;F|_H)\xrightarrow{\sim}
R\Gamma(D_t\cap H;F|_H).
\tag{U9}
\]

Fix \(x\in V\) and put \(a=x+\rho e_1\), \(\rho>0\) small. The left domains in (U9) are a cofinal family of relative open neighborhoods in \(H\) of \(K_x\). The right domains, as \(\rho,t\downarrow0\), are cofinal neighborhoods in \(H\) of \(B_x\). To verify the second assertion quantitatively, all domains lie in a fixed compact larger cap. Along any sequence with \(\rho,t\to0\), a limit of points in their closures satisfies \(q\leq(h+x_1)^2\) and \(y_1=-h\), by the uniform bound \(s e^{-s/t}\leq t/e\). Hence the limit lies in \(B_x\). If arbitrarily small parameters failed to put the whole closure in a prescribed open neighborhood of \(B_x\), compactness would give a contradictory sequence of points outside that neighborhood. The same argument with the cone inequality proves the first cofinality assertion.

The right domains need not be ordered merely by decreasing \(\rho\). Choose a nested cofinal sequence of pairs \((\rho_m,t_m)\) recursively: put both new domains inside their predecessors and inside the \(1/m\)-neighborhoods of their respective compact sets. The compactness argument just given permits each choice. Restriction in both columns commutes with (U9). Compact-neighborhood continuity (N1), on the locally compact closed space \(H\), now identifies the colimit of these isomorphisms with

\[
\operatorname*{colim}_m R\Gamma(D(a_m)\cap H;F|_H)
\longrightarrow
\operatorname*{colim}_m R\Gamma(D_{t_m}(a_m)\cap H;F|_H)
\simeq R\Gamma(B_x;F),
\tag{U10}
\]

whose source is \(R\Gamma(K_x;F)\). Here the filtered colimits can equivalently be taken on every cohomology group, where they are exact; all identifications are induced by restriction. This proves (U2), with its natural map. Every geometric choice was independent of \(F_\lambda\), so the proof establishes the claimed family uniformity. At a zero covector, a common excluded neighborhood instead forces every \(F_\lambda\) to vanish on one common base neighborhood by the constant-function test; any small cap there gives the zero comparison.

<a id="extension-continuity-proof"></a>
<a id="the-two-limits-of-extension-use-different-supports-extension-continuity-proof"></a>

## The two limits of extension use different supports

For subsequent boundary arguments it is useful to keep the limit operations separate. Let \(O_m\) be increasing open subsets of a locally compact Hausdorff space \(Z\), with union \(O\). Write \(j_m:O_m\hookrightarrow Z\), \(j:O\hookrightarrow Z\), and let \(F\in D^+(k_O)\). Ordinary extension is recovered by the derived inverse limit with its actual restriction maps:

\[
Rj_*F\simeq\operatorname*{holim}_m Rj_{m*}(F|_{O_m}).
\tag{J1}
\]

Choose one bounded-below injective resolution \(I\) on \(O\). Each complex \(j_{m*}(I|_{O_m})\) is a bounded-below complex of injectives: restriction to an open set preserves injectives because its left adjoint, extension by zero, is exact, and direct image preserves injectives because inverse image is exact. Products of these injective models compute the derived products. To check this, their Hom complexes from an acyclic complex are acyclic by the [bounded-below injective-resolution argument](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#constructing-enough-injectives-explicit-injective-models). Hom into their termwise product is the product of those Hom complexes. Products of module complexes preserve acyclicity, so the product model has the required injective property as well. All these models have the common lower bound of \(I\). In each degree and over each open \(V\subset Z\), the restrictions from \(V\cap O_{m+1}\) to \(V\cap O_m\) are surjective by flabbiness. Hence the map \(1-\mathrm{shift}\) on the product of these section groups is surjective, by recursively lifting one component at a time. Its kernel is \(\Gamma(V\cap O;I)\), by the sheaf gluing axiom. The homotopy-fibre complex of this map is consequently quasi-isomorphic to \(j_*I\), proving (J1). This argument does not assume that arbitrary products of sheaves are exact, or that the cohomology restriction maps stabilize.

Extension by zero has a direct-limit comparison on **compact** tests. For a compact \(K\subset Z\), the natural maps give, in every degree,

\[
\operatorname*{colim}_m H^q(K;j_{m!}(F|_{O_m}))
\xrightarrow{\sim} H^q(K;j_!F).
\tag{J2}
\]

Indeed put \(V=K\cap O\) and \(V_m=K\cap O_m\). Open-extension base change on stalks identifies restriction to \(K\) with extension by zero from these open subsets of \(K\). Since \(K\) is compact, the resulting cohomology groups are \(H_c^q(V_m;F|_{V_m})\) and \(H_c^q(V;F|_V)\). A bounded-below c-soft resolution on \(V\), restricted to the opens \(V_m\), computes them. Its compact-section complexes have direct limit the compact-section complex on \(V\): every compact support lies in some \(V_m\), and extension by zero is the given transition map. Exactness of filtered colimits proves (J2). The identification is natural for restriction from a compact cap to its closed base, because it was built from the original restriction and extension maps. Thus if all cap/base comparisons for the objects \(j_{m!}(F|_{O_m})\) are isomorphisms, the same comparison for \(j_!F\) is an isomorphism.

The last statement is a comparison on a specified compact cap. The [converse cap-test theorem](directional-neighborhoods-and-the-compact-cap-test.md#from-the-cap-comparison-back-to-all-local-tests-compact-cap-converse) converts it into an exclusion from microsupport. Likewise (J1) supplies the inverse limit for ordinary extensions, but a pointwise vanishing stalk cannot simply be commuted with an infinite product. The directional reading proves [uniform propagation](directional-neighborhoods-and-the-compact-cap-test.md#propagation-for-a-prescribed-cone-directional-propagation), [one localization for a whole family](directional-neighborhoods-and-the-compact-cap-test.md#one-localization-for-an-entire-family-uniform-directional-localization), and the [noncharacteristic open-boundary estimates](directional-neighborhoods-and-the-compact-cap-test.md#the-two-noncharacteristic-open-boundary-estimates-noncharacteristic-open-boundaries). The [limiting-boundary proof](limiting-covectors-at-open-boundaries.md#the-full-open-extension-estimates-arbitrary-open-extensions) supplies the arbitrary-open estimates and the [missing-submanifold trace](limiting-covectors-at-open-boundaries.md#the-trace-across-a-missing-submanifold-missing-submanifold-trace), with arbitrary bounded-below coefficients. The [limiting tensor proof](limiting-covectors-at-open-boundaries.md#products-restriction-and-the-limiting-sum-limiting-tensor-estimate) treats arbitrary bounded coefficients over a ring of finite global dimension; the geometric foundations remain separate.

<a id="scalar-profile"></a>
<a id="the-scalar-profile-and-its-geometric-input-scalar-profile"></a>

## The scalar profile and its geometric input

Set

\[
h=|\varphi|^2:X\to\mathbb R,\qquad
\Lambda=\operatorname{SS}(F).
\tag{5}
\]

If a compact set of real numbers has upper bound \(R^2\), its support inverse image under \(h\) is closed in \(\operatorname{supp}(F)\cap\varphi^{-1}\overline B_R\), which is compact. If it lies below zero, its inverse image is empty. Thus \(h\) is proper on the same closed coefficient support. Write

\[
H=Rh_*F\in D^b_{w\text{-}\mathbb R\text{-}c}(k_{\mathbb R}).
\tag{7}
\]

The boundedness here follows from the [ordinary-image bound](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#why-the-operations-remain-globally-bounded-globally-bounded-operations), since \(X\) has a uniform finite dimension bound. The sheaf image estimate is now (T6). To obtain weak constructibility of \(H\), the remaining geometric contracts are precise: the [constructibility/microsupport criterion](constructibility-from-microsupport-and-perfect-stalks.md#geometric-equivalence) makes the actual \(\operatorname{SS}(F)\) closed, conic, subanalytic and isotropic; [proper cotangent transport](isotropic-cotangent-transport-and-discrete-critical-values.md#proper-direct-transport) makes \(h_\pi h_d^{-1}\operatorname{SS}(F)\) a set with those same properties. Its required properness was proved in (T5), using the actual support. Estimate (T6) and the reverse constructibility criterion then make the cohomology of \(H\) locally constant on the pieces of a locally finite subanalytic stratification of \(\mathbb R\). The cotangent transport argument is supplied in the linked lesson, including singular-form detection. The linked proofs specify their subanalytic set, singular-form, involutivity and compatible-stratification inputs. The local-support proof of the image estimate is (T1)–(T6). No finiteness condition on the coefficient modules enters this deduction.

On the line, the connected strata are points and intervals. Local finiteness, applied near zero, gives \(\delta>0\) with no point stratum in \((0,\delta)\), for a common stratification of the finitely many cohomology sheaves. We may insert zero as a point stratum if necessary. Since \(h\geq0\), \(H\) vanishes on the negative half-line. The entire remaining calculation uses precisely these two properties: zero on the negative side and locally constant cohomology on \(I=(0,\delta)\).

Here is why a locally constant sheaf \(L\) on an interval is constant, even for an infinite module. To transport a stalk element between two points, cover their compact connecting segment by trivializing subintervals and subdivide it into finitely many pieces subordinate to them. Consecutive overlaps are connected, so continuation of a constant section is unique. Refining a subdivision does not change the result. Two choices have a common refinement, giving the same transport. Concatenation and reversal show that these transports compose and are inverse. Fixing one stalk now supplies sections locally at every point, with the constant gluing rule; hence it identifies the sheaf with the constant sheaf of that stalk.

Put \(B=R\Gamma(I;H)\). The exact constant-sheaf functor is left adjoint to sections. Its derived counit gives

\[
H|_I\simeq B_I.
\tag{9}
\]

To check the counit, first take one cohomology sheaf, which is constant by the preceding argument. Its ordinary cohomology on every nonempty subinterval is its coefficient in degree zero, by the proper-interval homotopy proof in (O1)–(O3) of the duality lesson. The counit is therefore the identity on every stalk. Induct on the finite number of cohomology degrees using the natural truncation triangles. This proves (9) for the whole complex and proves that \(B\) has the same cohomological bounds as \(H|_I\). No splitting into cohomology sheaves has been assumed. In particular, all restrictions between positive subintervals identify their section complexes with the same \(B\).

<span id="ordinary-ball-cohomology-is-the-central-coefficient"></span>

<a id="scalar-endpoint-proof"></a>
<a id="an-interval-star-and-its-closed-endpoint-scalar-endpoint-proof"></a>

## An interval star and its closed endpoint

We prove the scalar assertion in the category of all sheaves. Start with a sheaf \(Q\) on \(J=(-\eta,t)\), zero on \((-\eta,0)\) and constant with value \(N\) on \((0,t)\). Let \(i\) be the inclusion of zero and \(j\) the inclusion of \((0,t)\). The natural maps from open extension and to the closed-point restriction give the stalkwise exact sequence

\[
0\longrightarrow j_!N\longrightarrow Q\longrightarrow i_*Q_0
\longrightarrow0.
\tag{S1}
\]

The sheaf \(N_{[0,t)}\), extended from that closed subset of \(J\), fits into a second exact sequence:

\[
0\longrightarrow j_!N\longrightarrow N_{[0,t)}
\longrightarrow i_*N\longrightarrow0.
\tag{S2}
\]

The half-closed interval \([0,t)\) contracts to zero. It is locally compact, so the proper-interval homotopy argument applies to its constant coefficients, just as it did to a closed ball. Consequently its ordinary derived sections are \(N\) and restriction to zero is the identity. Taking sections in (S2) proves \(R\Gamma(J;j_!N)=0\). Taking sections in (S1) now proves that the actual restriction \(R\Gamma(J;Q)\to Q_0\) is an isomorphism.

For the closed scalar interval \([0,t]\), the identical argument uses the open inclusion \((0,t]\to[0,t]\) and the constant sheaf on \([0,t]\). Its ordinary cohomology is again \(N\), with identity restriction to zero. It follows that \(R\Gamma([0,t];Q)\to Q_0\) is an isomorphism whenever \(Q\) is constant on \((0,t]\). No condition on the attachment homomorphism at zero is imposed in either calculation.

Apply these calculations to every cohomology sheaf of a bounded complex. The restriction maps commute with truncation triangles; induction on the cohomology range proves the derived assertions. In particular, with \(A=H_0\),

\[
R\Gamma(J;H)\longrightarrow H_0=A
\tag{10}
\]

is the natural isomorphism. Because \(H\) vanishes to the left of zero, restriction identifies \(R\Gamma(J;H)\) with \(R\Gamma([0,t);H)\). The closed-interval calculation applies since \(t\) is interior to the constant positive region. Both maps to \(A\) are restrictions, so their composite relation proves that

\[
R\Gamma([0,t];H)\longrightarrow R\Gamma([0,t);H)
\longrightarrow A
\tag{S3}
\]

consists of isomorphisms. It also proves their compatibility as \(t\) decreases. This supplies the closed endpoint directly; no microlocal endpoint or general triangulation-star theorem is used.

<span id="supported-cohomology-is-the-fibre-of-one-map"></span>

<a id="scalar-support-proof"></a>
<a id="one-fibre-computes-every-small-closed-support-scalar-support-proof"></a>

## One fibre computes every small closed support

Under (9) and (10), restriction to the positive part defines

\[
u:A\longrightarrow B.
\tag{13}
\]

The inverse of the restriction isomorphism to \(A\) in (10) is unique in the derived category. Thus this is a specified arrow, independent of the interval chosen, and not a choice of a map between abstractly isomorphic coefficient objects. Put \(D=\operatorname{Cone}(u)[-1]\), with the cone differential of (P2) in the duality lesson. Localization on \(J\) gives

\[
D\longrightarrow A\xrightarrow{u}B\xrightarrow{+1},
\qquad
D\simeq R\Gamma_{\{0\}}(\mathbb R;H)
\simeq\operatorname{Cone}(u)[-1].
\tag{14}
\]

For \(0<t'<t\), the complement in \(J\) of \([0,t']\) has a zero negative part and the constant positive part \((t',t)\). Its sections are \(B\), with the same map from \(A\). Hence localization also gives

\[
R\Gamma_{[0,t']}(\mathbb R;H)
\longrightarrow A\xrightarrow{u}B\xrightarrow{+1}.
\tag{15}
\]

The inclusion of supports \(\{0\}\subset[0,t']\) induces the identity on \(A\) and the restriction isomorphism on \(B\). Taking the corresponding fibres shows that the actual support inclusion is an isomorphism. These maps commute for all smaller and larger positive inner endpoints.

To pass to compact supports without an unproved inverse-limit assertion, restrict to the closed subspace \([0,t)\subset J\). A complex with zero cohomology off this subspace is the closed direct image of its restriction, as a stalk check proves. Resolve that restriction by injectives and push them forward by the closed inclusion. Closed direct image is exact and preserves injectives because its left adjoint is exact. We have therefore chosen a representative whose terms are actually supported in \([0,t)\).

Every compact subset of \([0,t)\) lies in \([0,r]\) for some \(0<r<t\). Termwise compact sections of this representative are consequently the filtered union of its sections with those closed supports. Exactness of filtered colimits gives the comparison on cohomology, and the compatible support maps already proved yield

\[
R\Gamma_c([0,t);H)\simeq D.
\tag{16}
\]

The map from each inner closed support to this compact-section complex is the map induced by inclusion, and is an isomorphism. This calculation works for arbitrary bounded coefficient complexes, independently of their perfection.

<span id="annuli-and-spheres-read-the-nearby-coefficient"></span>

<a id="proper-support-transport"></a>
<a id="transport-along-the-map-proper-on-coefficient-support-proper-support-transport"></a>

## Transport along the map proper on coefficient support

We justify all the comparison maps used to return to \(X\). Put \(S=\operatorname{supp}(F)\) and let \(i:S\to X\). A stalk check gives \(F\simeq i_*i^{-1}F\), since \(F\) has zero cohomology off \(S\). The restricted map \(h|_S\) is proper. Thus proper base change applies even if \(h\) is not proper on all of \(X\).

For an open scalar set \(V\), derived sections of \(Rh_*F\) on \(V\) are sections of \(F\) on \(h^{-1}V\), by composition of ordinary direct images. For a closed scalar subset, first use proper base change for \(h|_S\) and then sections. These identifications include their restriction maps. Moreover, for a closed scalar \(K\) and an open scalar \(V\),

\[
\begin{aligned}
R\Gamma_K(\mathbb R;Rh_*F)&\simeq R\Gamma_{h^{-1}K}(X;F),\\
R\Gamma_c(V;Rh_*F)&\simeq R\Gamma_c(h^{-1}V;F).
\end{aligned}
\tag{S4}
\]

For the first equality, use an injective resolution of \(i^{-1}F\) on \(S\) and its closed direct image on \(X\). These terms are injective and supported on \(S\). Their ordinary and proper direct images by \(h\) agree, because every section support is closed inside a set proper over the base. The support of an image section is the proper image of the original support, as in (F3) and (D2) of the duality lesson. Thus sections supported in \(K\) are exactly the sections supported in \(h^{-1}K\), term by term. The second equality is the already-proved proper-image composition, since \(Rh_*F=Rh_!F\). Both proofs retain inclusion of closed supports and passage to compact supports; they do not identify only the resulting objects.

The closed and open restrictions in (S3) therefore give

\[
R\Gamma(\{h\leq t\};F)
\longrightarrow R\Gamma(\{h<t\};F).
\tag{11}
\]

and proper base change at zero gives

\[
A=H_0\simeq R\Gamma(h^{-1}(0);F).
\tag{12}
\]

Take \(t=\epsilon^2\) and choose \(\epsilon_0^2<\delta\). These are precisely the maps in (2). Likewise (14)–(16), transported by (S4) with \(t'=(\epsilon')^2\), give all the maps in (3). Compactness is only required on the coefficient support, exactly as in the statement.

For \(0\le s<q<r\le t<\delta\), the constant-complex comparison (9) gives

\[
R\Gamma((0,t);H)
\longrightarrow R\Gamma((s,r);H)
\longrightarrow H_q.
\tag{17}
\]

The last arrow is restriction to an interior point of a nonempty interval. Proper base change identifies its target with sections on \(h^{-1}(q)\). Substituting

\[
t=\epsilon^2,\quad r=(\epsilon')^2,\quad
q=(\epsilon^{\prime\prime\prime})^2,\quad s=(\epsilon^{\prime\prime})^2.
\tag{18}
\]

gives the punctured ball, annulus and pulled-back sphere in (4), including \(\epsilon^{\prime\prime}=0\) and \(\epsilon'=\epsilon\). Every map here is induced by the same restriction or support operation as in the theorem. Subject to the stated geometric proper-image input, this completes the proof of all three comparisons.

<a id="signed-critical-check"></a>
<a id="the-two-signed-critical-sets-give-a-second-check-signed-critical-check"></a>

## The two signed critical sets give a second check

The earlier microlocal route to the same positive interval remains useful for recording both covector directions. Let \(\Lambda=\operatorname{SS}(F)\). The geometric constructibility criterion makes the actual \(\Lambda\) closed, conic, subanalytic and isotropic, with base equal to the closed support. The antipodal set has the same properties. The [direct analytic-curve proof of microlocal Bertini–Sard](isotropic-cotangent-transport-and-discrete-critical-values.md#direct-critical-set-proof), applied to \(h\) and these two sets, gives the closed locally finite critical-value sets

\[
\begin{aligned}
C_+&=\{h(x):dh_x\in\Lambda\},\\
C_-&=\{h(x):-dh_x\in\Lambda\}.
\end{aligned}
\tag{6}
\]

Properness is available on their base because it is the actual coefficient support. Shrink \(\delta\) to avoid both sets on \((0,\delta)\), allowing zero itself to remain critical. The proper-image microsupport estimate lifts a scalar covector \((t;\tau)\) to \(\tau\,dh_x\in\Lambda\), with \(h(x)=t\). If \(\tau>0\), conicity contradicts the first exclusion; if \(\tau<0\), it contradicts the second. Thus

\[
\operatorname{SS}(H)|_{(0,\delta)}
\subset T^*_{(0,\delta)}(0,\delta).
\tag{8}
\]

This recovers local constancy on the positive interval through the zero-section criterion. The image estimate is (T6). The critical-value proof now uses curve selection and the singular-form test (C1)–(C6), without the uniformization/Sard inputs of general cotangent transport. It uses the stated analytic curve-selection and singular-form prerequisites; the zero-section criterion, including actual derived local descent, is proved above. The scalar proof above needs no additional microlocal Morse endpoint result once positive local constancy is known.

<a id="local-chart-cutoff"></a>
<a id="applying-the-theorem-in-an-open-coordinate-chart-local-chart-cutoff"></a>

## Applying the theorem in an open coordinate chart

For an open chart \(X\subset\mathbb R^n\) and \(\varphi(x)=x-x_0\), choose a closed ball of radius \(R\) about \(x_0\) contained in \(X\), and set

\[
F'=F\otimes k_{\overline B_R(x_0)}.
\tag{19}
\]

Here is a direct proof that the cutoff preserves weak constructibility. More generally let \(Z\subset X\) be closed and subanalytic, with inclusion \(i\). Choose a locally finite subanalytic cover \((E_a)\) on which all the finitely many cohomology sheaves of \(F\) are locally constant. The sets \(E_a\cap Z\) and \(E_a\setminus Z\) are subanalytic by intersection and difference in the subanalytic set calculus. They still form a locally finite cover: each is a subset of its original member, and only two new members arise from it.

The stalks of \(k_Z\) are \(k\) on \(Z\) and zero elsewhere, so this sheaf is flat. Exact restriction and closed direct image give, by the canonical stalkwise identification,

\[
F\otimes^L k_Z\simeq i_*i^{-1}F,
\qquad
H^j(F\otimes^L k_Z)|_E\simeq
\begin{cases}
H^j(F)|_E,&E\subset Z,\\
0,&E\subset X\setminus Z.
\end{cases}
\tag{K1}
\]

Each new cover member therefore has locally constant cohomology. This is exactly the defining cover condition for weak constructibility. It preserves the original global cohomological interval and imposes no finite-generation, perfection or noncharacteristic condition. The argument uses only the stated subanalytic set calculus; it does not require the limiting tensor microsupport estimate.

Apply this with \(Z=\overline B_R(x_0)\). The result in (19) has compact closed support and agrees with \(F\) on the interior. Apply the small-ball theorem to it and use restriction and support excision to transfer the comparisons to sufficiently small balls for \(F\). This keeps the chart open and imposes no global properness assumption on it.

None of \(A,B,D\) has been assumed perfect. Finiteness of compact or sphere cohomology for perfect constructible coefficients is a subsequent theorem, not a consequence of the present weak-coefficient calculation.

## Examples and exercises with solutions

### The two sides of a point give its local degree

*Difficulty: Introductory.*

On the oriented line take \(F=k_{\mathbb R}\) and \(\varphi(x)=x\), with \(k\neq0\). Compute \(A,B,u,D\), and identify the ordinary and compactly supported cohomology of a small open ball.

**Solution.** Here \(h=x^2\). The central fibre is one point, so \(A=k\). A positive level has its negative and positive points, giving \(B=k\oplus k\), ordered in that order. Restriction of a constant section gives \(u(v)=(v,v)\). The exact sequence
\(0\to k\xrightarrow{u}k^2\xrightarrow{(a,b)\mapsto b-a}k\to0\)
shows \(D=k[-1]\). Thus ordinary cohomology of the small interval is \(k\) in degree zero, while compactly supported cohomology and cohomology supported at its central point are \(k[-1]\). The difference convention fixes the oriented local generator.

### A central point sheaf has no nearby coefficient

*Difficulty: Introductory.*

Take \(F=k_{\{0\}}[m]\) on \(\mathbb R\), for an integer \(m\), with \(\varphi(x)=x\). Compute all three types of comparison.

**Solution.** The support is a compact point. Its central coefficient is \(A=k[m]\), its positive-level coefficient is \(B=0\), and \(u=0\). Hence \(D=A=k[m]\). Every small closed or open ball contains the point, so both ordinary groups and their restriction to the central fibre are \(k[m]\). Central, closed-inner and compact-outer support groups are also \(k[m]\), with identity maps. Punctured balls, annuli and positive sphere fibres have zero coefficient. This distinguishes a support contribution at the point from the local degree of an ambient constant sheaf.

### A vanishing stalk can still have a nonzero costalk

*Difficulty: Intermediate.*

Take \(F=k_{(0,\infty)}\) on \(\mathbb R\), with \(\varphi(x)=x\). Compute \(A,B,u,D\). Explain how the ordinary ball restriction can be an isomorphism even though the positive part has nonzero sections.

**Solution.** The central stalk is zero, so \(A=0\). Each positive scalar \(h=x^2\) level meets the supported positive side once; the negative point contributes zero. Thus \(B=k\), \(u=0\) and \(D=k[-1]\). Ordinary cohomology on the whole small ball is zero by the vertex-star calculation, with its zero restriction to the central stalk. On the punctured ball the positive component contributes \(k\), and removing the central point has removed the extension-by-zero boundary condition. Its local support triangle is \(k[-1]\to0\to k\). Compact support on the small positive interval also gives \(k[-1]\), as (3) requires. Stalk and costalk are different here.

### The sphere must be pulled back before taking coefficients

*Difficulty: Intermediate.*

Let \(X=\mathbb R\), \(\varphi(x)=x^2\) with target \(\mathbb R\), and \(F=k_X\). For \(0\leq a<c<b\leq\epsilon\), describe the three spaces in (4), compute their ordinary cohomology and their maps.

**Solution.** The punctured inverse-image ball is
\(( -\sqrt\epsilon,0)\sqcup(0,\sqrt\epsilon)\).
The annulus inverse image is
\(( -\sqrt b,-\sqrt a)\sqcup(\sqrt a,\sqrt b)\),
where \(\sqrt a=0\) is allowed. The sphere in the target is \(\{-c,c\}\), and its inverse image under \(x^2\) is \(\{-\sqrt c,\sqrt c\}\). All three have ordinary coefficient \(k^2\) in degree zero, with branches ordered negative then positive. The maps are identity maps on the two branch coefficients. Taking coefficients directly on \(S_c\) in the target would use a space where \(F\) is not defined. Also the scalar norm square here is \(h=x^4\), so its sphere level is \(c^2\), not \(c\).

### The isomorphisms impose no finite rank

*Difficulty: Intermediate.*

Over a field let \(V=\bigoplus_{j\geq1}k\), take the constant sheaf \(F=V_{\mathbb R}\), and use \(\varphi(x)=x\). Are the small-ball and supported comparisons valid? Are their coefficient complexes perfect?

**Solution.** The sheaf is weakly constructible, and the identity is proper on its closed support. The same restriction maps as in the first exercise give \(A=V\), \(B=V^2\), \(u(v)=(v,v)\), and \(D=V[-1]\). The difference map \((a,b)\mapsto b-a\) again identifies the cokernel and has a splitting \(v\mapsto(0,v)\), so all natural comparisons are isomorphisms. None of the nonzero coefficient complexes is perfect over the field, because its cohomology is infinite dimensional. A compact central fibre does not make infinite weak coefficients finite.

### A compact cutoff repairs an open chart application

*Difficulty: Advanced.*

Let \(X\) be the open unit disk in \(\mathbb R^2\), \(x_0=0\), \(F=k_X\) and \(\varphi(x)=x\). Explain why global properness is absent, perform the local cutoff, and compute the central and nearby coefficients and the supported degree for sufficiently small balls.

**Solution.** The inverse image of the compact closed unit disk in the target is all of \(X\), which is not compact. Thus the original support properness assumption fails. Choose \(0<R<1\) and replace \(F\) by \(k_{\overline B_R}\) as a sheaf on \(X\). Its support is compact, and it agrees with \(k_X\) on the smaller open disk. The theorem therefore applies there and transfers by excision.
The central coefficient is \(A=k\). A positive radial level is a circle. Its constant-sheaf cohomology is \(k\) in degrees zero and one: cover it by two arcs whose intersection is two arcs, and the Mayer–Vietoris differential \(k^2\to k^2\) is \((u,v)\mapsto(v-u,v-u)\). Its kernel and cokernel are both \(k\). Choosing the standard circle generator gives \(B\simeq k\oplus k[-1]\). Restriction of the disk unit maps to the degree-zero unit; there is no degree-one component from \(k\), since \(k\) is projective as a coefficient module. Thus the fibre of \(u\) is \(D=k[-2]\). Compact support on a small open disk and support at its centre both have this oriented degree-two coefficient, while ordinary disk cohomology is \(k\).

## Natural maps distinguish infinite self-similarity from stabilization

Over a field let \(V=\bigoplus_{n\geq0}k e_n\). An abstract vector-space isomorphism
\(V\simeq V\oplus V\) exists: send the even basis vectors to the first copy and the odd basis vectors to the second. This observation does not make the actual punctured-interval restriction invertible. For the constant sheaf \(V_{\mathbb R}\), that restriction is

\[
V\xrightarrow{\Delta}V\oplus V,\qquad
\Delta(v)=(v,v).
\tag{20}
\]

The map is injective; its cokernel is \(V\), identified by
\((a,b)\mapsto b-a\). Its derived fibre is therefore \(V[-1]\), not zero. This is the central costalk in the increasing orientation, and the same nonzero complex is obtained by cohomology with support in any sufficiently small closed interval, and by compact cohomology on a larger open interval, using (3). Stabilization concerns these natural maps, not a list of abstractly isomorphic coefficient objects.

### Infinite doubling does not make the central costalk vanish

*Difficulty: Intermediate.*

Give the explicit isomorphism \(V\to V\oplus V\) using parity of the displayed basis. Compare it with (20). Compute the central support complex and explain why costalk conservativity for weakly constructible sheaves remains valid.

**Solution.** Send \(e_{2m}\) to \((e_m,0)\) and \(e_{2m+1}\) to \((0,e_m)\). This has inverse sending the two copies' basis vectors back to their even and odd indices. It is an abstract isomorphism. The natural restriction from a connected interval to its negative and positive punctured components sends the same constant section to both sides; it is \(\Delta\), which differs from the parity map. The difference map \(V\oplus V\to V\) is surjective and has kernel the diagonal, so the support triangle gives the central complex \(V[-1]\), with \(V\) in degree one. It is nonzero.

On a \(d\)-dimensional manifold, the analogous ball/sphere restriction has relative coefficient \(V\otimes\mathrm{or}_x^\vee[-d]\), also nonzero. In a weakly constructible object, a maximal nonzero stratum is locally closed with all other nonzero strata absent near one of its interior points. Closed-support localization reduces its costalk there to this intrinsic shifted coefficient. Thus some costalk is nonzero. Infinite self-similarity of \(V\) does not interfere with the natural-map argument used in [weak operation comparisons](weak-constructibility-under-sheaf-operations.md#costalks-detect-a-weakly-constructible-object).

<span id="references"></span>

<span id="accessible-sources-and-the-scope-of-their-small-ball-statements"></span>

<a id="sources-and-proof-boundary"></a>
<a id="human-sources-and-proof-inputs-sources-and-proof-boundary"></a>
<a id="sources-and-the-remaining-proof-boundary"></a>
<a id="sources-and-the-remaining-proof-boundary-sources-and-proof-boundary"></a>

## Human sources and proof inputs

Andreas Hohl and Pierre Schapira, [*Unusual functorialities for weakly constructible sheaves*, version 2, §4 and Lemma 4.1](https://arxiv.org/html/2303.11189v2#S4), state the weak proper-image stability and the passage to weak cohomological constructibility. Those passages refer to earlier foundations; they do not supply a complete small-ball proof. The paper's Proposition 4.2 motivates the costalk check above, where the natural diagonal map is retained to handle infinite self-similar coefficients.

The independent scalar argument in this edition starts with the actual interval attachment and proves the open, closed and compact-support maps by two short exact sequences and localization. Its elementary sheaf-operation ingredients are proved in the [current duality reconstruction](../../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#compact-support-extension-lifting-and-acyclicity-compact-support-proof), with injective models, bounded operations and constant local-support calculations. The complete scalar argument needed here is supplied above, including its actual restriction and support-inclusion maps.

The proper-image microsupport estimate is proved in (T1)–(T6), following the cited freely available Astérisque argument with its support operations supplied explicitly. The closed-cutoff sheaf argument is (K1), using the defining subanalytic cover. The companion cotangent lesson supplies the geometric transport arguments and a direct proof for both signed critical sets. The geometric prerequisites are the linked subanalytic foundations, the analytic critical-value proof used for surjective form detection, and the involutivity and stratification inputs of the constructibility/microsupport criterion. The boundary and bounded tensor estimates have exact companion proofs linked above. The closed-embedding and zero-section inputs are now proved in (E1)–(E3) and (N1)–(Z4). No external source text, figure or archive is included in this reader.

The uniform compact-cap implication (U1)–(U10) follows the compact-cap argument of Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Theorem 3.1.1, implication (1) to (3), printed pp. 49–53. The explicit exponential graph (U3) has uniform derivative and cap-collapse estimates, with rim support-summand and nested-neighborhood arguments. Equations (J1)–(J2) give ordinary and compact-support extension limits. The directional reading supplies the propagation and noncharacteristic open-boundary prerequisites linked above. The [limiting-boundary reading](limiting-covectors-at-open-boundaries.md) proves the arbitrary-open and missing-submanifold applications. The [limiting tensor proof](limiting-covectors-at-open-boundaries.md#products-restriction-and-the-limiting-sum-limiting-tensor-estimate) supplies the bounded tensor argument; geometric foundations remain separate.
