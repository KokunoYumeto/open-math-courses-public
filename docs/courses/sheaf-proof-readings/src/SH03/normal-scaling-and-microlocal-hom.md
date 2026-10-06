# Normal scaling, microlocal Hom and involutivity

The microsupport of a sheaf records where local sections fail to continue. Its involutivity is a constraint on the entire closed set, including its singular points. We prove that constraint by constructing a sheaf of directional morphisms: its identity cannot vanish at a point of microsupport, while an empty cone and the resulting covector estimate would force exactly that vanishing.

The construction requires several actual comparison maps. We begin with Hom on ordinary rectangles, prove continuity along a noncompact locally closed subset, then construct normal specialization and the forward Fourier transform. Their support maps give a concrete representative for the microlocal identity. This order keeps the neighborhood limits outside Hom and makes the final contradiction apply to arbitrary stalk modules.

Throughout, \(k\) is an arbitrary commutative ring, and manifolds are smooth, finite dimensional, Hausdorff and second countable. Specialization, Fourier transport and the cone-vanishing lemma work in \(D^+\). The external-Hom inputs and the final sheaf \(F\) are bounded; their microlocal-Hom output need only be bounded below. Finite global dimension is used solely for the optional upper amplitude bound in (H4). No constructibility, perfectness or finite-generation assumption is made.

## Proof inputs and reading route {#microlocal-proof-inputs}

The following previous readings supply the sheaf operations and local tests used below. The microlocalization argument below uses these specific sheaf-operation and local-test proofs.

| Input | Exact available argument |
|---|---|
| Injectives, compact germs and c-soft lifting; proper-support base change, composition, adjunction and orientation trace | Duality maps, together with its injective models and ordinary cohomology bound |
| Proper-image and closed-embedding microsupport; uniform compact caps | Small-ball comparisons and its closed-embedding proof |
| Directional unit, correspondence kernel, cap converse, propagation and opposite open extension | Directional neighborhoods, especially the kernel and propagation |
| Arbitrary-open boundary limits and the trace from a missing submanifold | Limiting covectors and the trace proof |
| Closed-set Hamiltonian invariance once involutivity is known | Involutive subsets |

Smooth product charts give the constant-factor submersion formula used here; the radial section spells out its bounded-below argument. Local normal calculations take place in adapted product charts. A global supported-specialization statement is also given with its explicit tubular-neighborhood input; the diagonal application and the proof of involutivity use the product chart itself. Further subanalytic stratification, finiteness and constructible-duality theorems remain separate work.

## External Hom at independent covectors {#external-hom-estimate}

Let \(X\) and \(Y\) be finite-dimensional real manifolds, Hausdorff and countable at infinity, of dimensions \(n\) and \(m\). Let \(k\) be any fixed commutative ring. No finite generation, perfectness, constructibility or finite global dimension is assumed in the following estimate. For \(F\in D^b(k_X)\), \(G\in D^b(k_Y)\), and the two projections \(q_X,q_Y\), put
\[
\begin{aligned}
K(F,G)&=R\mathcal Hom(q_Y^{-1}G,q_X^!F),\\
\operatorname{SS}(K(F,G))
&\subset \operatorname{SS}(F)\times\operatorname{SS}(G)^a,
\qquad a(y,\eta)=(y,-\eta).
\end{aligned}
\tag{H1}
\]
The output is in \(D^+\), which is the range of the support-test and directional results used here. When \(k\) has finite global dimension, the additional upper bound proved below makes the output bounded.

The proof uses the already constructed bounded-below exceptional adjunction, proper-support base change and composition, the ordinary and compact cohomological dimension bounds, and the cone-test equivalence including cones with empty interior. It also uses extension by zero in an opposite-cone open. Its argument and exact scope are recalled below. These are statements about arbitrary coefficient sheaves. No tensor description of the first Hom argument by its dual is used.

### Rectangle adjunction before either variable shrinks {#external-hom-rectangle}

For ordinary opens \(U\subset X\) and \(V\subset Y\), let \(p:U\times V\to U\) be projection. There is a natural isomorphism of derived module complexes
\[
\begin{aligned}
R\Gamma(U\times V;K(F,G))
&\simeq R\operatorname{Hom}_{k_U}
 \bigl(Rp_!q_V^{-1}(G|_V),F|_U\bigr)\\
&\simeq R\operatorname{Hom}_{k_U}
 \bigl((R\Gamma_c(V;G))_U,F|_U\bigr)\\
&\simeq R\operatorname{Hom}_k
 \bigl(R\Gamma_c(V;G),R\Gamma(U;F)\bigr).
\end{aligned}
\tag{H2}
\]
Here \((A)_U\) denotes the constant complex associated to the module complex \(A\), not a constant object obtained by replacing \(F\) by one of its stalks.

Open restriction of the exceptional image is the one fixed by exceptional composition: for an open inclusion \(u\), the exact adjunction \(u_!\dashv u^{-1}\) gives \(u^!=u^{-1}\). Consequently \(q_X^!F|_{U\times V}\simeq p^!(F|_U)\), compatibly with the trace. Global sections of internal Hom compute the derived morphism complex. The first line is therefore \(Rp_!\dashv p^!\). The second is proper-support base change in the Cartesian square obtained from \(V\to\{\mathrm{pt}\}\) by pullback to \(U\). The last is the exact constant-sheaf functor's derived adjunction with sections.

All these constructions are available over an arbitrary ring. To make the coefficient range explicit, use a bounded-above open-generator flat resolution of the first Hom input and a bounded-below injective resolution of the target. The finite-length flat replacement that requires finite global dimension is unnecessary. In every degree of their Hom complex only finitely many terms occur: if the flat model vanishes above \(d\) and the injective model below \(a\), a degree-\(r\) term has \(a-r\le p\le d\). Internal Hom of a flat sheaf into an injective is injective by tensor–Hom adjunction. Restriction of an injective to an open remains injective because open extension by zero is exact. Thus these models compute both the internal and global derived Hom and give the bounded-below, natural adjunction (H2).

The maps in (H2) matter. If \(V'\subset V\), restriction of the kernel's sections corresponds to precomposition with compact-support extension:
\[
\begin{gathered}
R\Gamma(U\times V;K)\longrightarrow R\Gamma(U\times V';K),\\
R\operatorname{Hom}_k(A,B)\longrightarrow
R\operatorname{Hom}_k(A',B),\qquad
A'=R\Gamma_c(V';G)\longrightarrow A=R\Gamma_c(V;G),\\
B=R\Gamma(U;F).
\end{gathered}
\tag{H3}
\]
Indeed, the map \(Rp'_!q_{V'}^{-1}G\to Rp_!q_V^{-1}G\) is induced by the counit \(u_!u^{-1}\to\mathrm{id}\) for \(u:U\times V'\hookrightarrow U\times V\). Its adjoint is precisely restriction of a morphism into \(p^!F\). Trace-compatible exceptional composition makes this the same map as in (H3). Restriction in \(U\) instead acts on the second Hom argument by \(R\Gamma(U;F)\to R\Gamma(U';F)\). The two operations commute by naturality of these adjunctions.

### The coefficient bounds, including the arbitrary-ring range {#external-hom-amplitude}

Suppose \(F\in D^{[a,b]}(k_X)\) and \(G\in D^{[c,d]}(k_Y)\). The manifold bounds hold over arbitrary \(k\), so
\[
\begin{aligned}
R\Gamma(U;F)&\in D^{[a,b+n]}(k),&
R\Gamma_c(V;G)&\in D^{[c,d+m]}(k),\\
K(F,G)&\in D^{\ge a-d-m}(k_{X\times Y});\\
\operatorname{gldim}k=g<\infty
&\quad\Longrightarrow\quad
K(F,G)\in D^{[a-d-m,\ b+n-c+g]}(k_{X\times Y}).
\end{aligned}
\tag{H4}
\]
The first line follows by the finite cohomology-sheaf truncation triangles and the ordinary and compact dimension bounds. For the lower Hom bound, resolve the first module complex by a bounded-above projective complex vanishing above \(d+m\), and represent the second by a complex vanishing below \(a\). The Hom complex has no term below \(a-d-m\). The projective resolution may extend indefinitely to the left; that does not affect this conclusion.

If the global dimension is \(g\), the first complex has a projective model in degrees \([c-g,d+m]\). One obtains it by resolving a bounded representative and truncating its left exact tail at the \(g\)-th syzygy; that syzygy is projective. A representative of the second complex in \([a,b+n]\) now gives the upper bound \(b+n-c+g\).

These are uniform bounds on every ordinary rectangle. To pass to the sheaf, take a bounded-below injective representative of \(K\). Its restriction to a rectangle computes derived sections there, and the filtered colimit over rectangles computes its stalk complex. Exactness of filtered colimits commutes with cohomology. Thus the rectangular bounds imply exactly (H4). This is a colimit of the already computed Hom complexes' cohomology; no colimit is moved through a Hom argument. In particular, the upper bound is optional for (H1).

### Directional representatives and zero covectors {#external-hom-directional-input}

The problem is local on \(X\times Y\). Work in coordinate vector spaces \(E_X,E_Y\), using open extension by zero to extend an input beyond its chart if necessary. Exact open restriction of inverse image, internal Hom and the exceptional image identifies the resulting kernel with the original one on the chart.

If \((x_0,\xi_0)\notin\operatorname{SS}(F)\) and \(\xi_0\ne0\), the compact-cap and cone-test equivalence provides a closed convex cone \(C\subset E_X\) and a representative \(H\), identified with \(F\) on a fixed neighborhood of \(x_0\), such that
\[
Rq_{C*}H=0,\qquad
\langle c,\xi_0\rangle<0\quad(c\in C\setminus\{0\}).
\tag{H5}
\]
The directional topology consists of ordinary opens invariant under addition by \(C\). The representative can be chosen bounded when \(F\) is bounded: its supported-lens construction is the fibre of two ordinary open images of bounded complexes, and the manifold dimension bound bounds both images. It is enough here that it be bounded above and below; no boundedness theorem for the directional projector is required.

Strict negativity makes \(C\) pointed. If \(C=\{0\}\), its directional direct image is the identity, so \(H=0\), and the claimed local exclusion is immediate. Hence the nontrivial arguments below may assume \(C\setminus\{0\}\ne\varnothing\). If the tested covector itself is zero, the zero-section criterion gives local vanishing of the original input; the kernel vanishes on the corresponding product neighborhood. This handles zero covectors without angular normalization. The same alternatives apply to \(G\).

### The first factor: a cone with no motion in the second variable {#external-hom-first-factor}

Use \(H\) from (H5) in the target input of the kernel. For a \(C\)-open \(U\subset E_X\), derived direct-image composition gives \(R\Gamma(U;H)=R\Gamma(U;Rq_{C*}H)=0\), where the latter sections are in the directional topology. Formula (H2) gives
\[
R\Gamma(U\times V;K(H,G))=0
\quad\text{for every \(C\)-open \(U\) and ordinary open \(V\)},\qquad
Rq_{C\times\{0\}*}K(H,G)=0.
\tag{H6}
\]
The second assertion follows from the first on a basis. If an ordinary open is invariant under \(C\times\{0\}\), an ordinary rectangle \(B\times V\) inside it enlarges to \((B+C)\times V\) inside it. These rectangles are a directional basis. A bounded-below injective representative, followed by exact filtered stalk colimits, shows that vanishing of their derived sections is vanishing of the directional image.

For every \(\eta\), a nonzero vector \((c,0)\) pairs with \((\xi_0,\eta)\) as \(\langle c,\xi_0\rangle<0\). The cone-to-test theorem therefore excludes \((x_0,y;\xi_0,\eta)\) from the kernel's microsupport, and then from the original kernel wherever the two agree. This uses the cone \(C\times\{0\}\) exactly as it stands; it need not have interior in the product space. Compactness of its unit directions makes negativity persist on a neighborhood of the first covector, while leaving the second covector unrestricted.

### Compact supports in the opposite direction {#external-hom-opposite-extension}

We recall the precise consequence of the opposite-open extension theorem. Let \(H\in D^+(k_E)\), let \(C\) be closed convex with \(Rq_{C*}H=0\), and let \(\Omega\) be an ordinary open invariant under \(-C\). Suppose \(\Omega\cap(L+C)\) is relatively compact for every compact \(L\). Then \(Rq_{C*}H_\Omega=0\), where \(H_\Omega=j_!j^{-1}H\).

Here is the support argument behind this assertion. On a directional basis member \(U=B_\epsilon(x)+C\), its intersection with \(\Omega\) is relatively compact. A bounded-below injective resolution, open extension and the proved c-soft acyclicity identify \(H^r(U;H_\Omega)\) with the filtered colimit of \(H^r_K(U;H)\) over \(K\) closed in \(U\) and contained in \(\Omega\). The closure of each \(K\) in \(E\) is compact. Set \(D_K=\overline K-C\). It is closed, is \(C\)-closed, and satisfies \(K\subset D_K\cap U\subset\Omega\): if \(z=w-c\in U\), then \(w=z+c\in U\), so \(w\in\overline K\cap U=K\), and \(-C\)-invariance gives \(z\in\Omega\). These are cofinal supported terms. Directional support compatibility identifies their cohomology with supported cohomology of \(Rq_{C*}H=0\). This proves the opposite-open assertion using bounded-below injectives and exact filtered colimits, over arbitrary \(k\).

If \(\Omega'\subset\Omega\) is also \((-C)\)-open and \(\Omega\setminus\Omega'\) is relatively compact, the resulting comparison is the actual extension map
\[
R\Gamma_c(\Omega';H)\xrightarrow{\ \sim\ }R\Gamma_c(\Omega;H).
\tag{H7}
\]
Both open extensions have zero directional image. The coefficient-set localization triangle is
\[
H_{\Omega'}\longrightarrow H_\Omega
 \longrightarrow H_{\Omega\setminus\Omega'}\longrightarrow,
\qquad
\operatorname{supp}(H_{\Omega\setminus\Omega'})
 \subset\overline{\Omega\setminus\Omega'}.
\tag{H8}
\]
Its first arrow is open extension, and its last object has compact closed support. Its ordinary global cohomology vanishes by composition with \(Rq_{C*}\). On this compactly supported object ordinary and compactly supported cohomology agree. Applying compactly supported cohomology to (H8), with open-extension composition, proves (H7), including its specified map. This step is the reason for the compact difference hypothesis.

### An explicit lens for the second factor {#external-hom-second-factor-lens}

Suppose \((y_0,\eta_0)\notin\operatorname{SS}(G)\), with \(\eta_0\ne0\). Choose a bounded representative \(H\) agreeing with \(G\) near \(y_0\), killed by \(Rq_{C*}\), with \(\langle c,\eta_0\rangle<0\) for \(c\in C\setminus\{0\}\). The trivial-cone case has already been handled. Put \(D=-C\), and choose the linear functional \(\ell(c)=-\langle c,\eta_0\rangle\). Compactness of the unit section of \(C\) gives a constant \(\kappa>0\) with \(\ell(c)\ge\kappa|c|\) on \(C\).

Take a compact closed ball \(B\) with \(y_0\) in its interior and \(a>\sup_B\ell\). Define
\[
\Omega=\{\ell<a\},\qquad
\Omega'=\Omega\setminus(B+C),\qquad
S=\Omega\cap(B+C)=\Omega\setminus\Omega'.
\tag{H9}
\]
Both opens are \(D\)-invariant. The sum \(B+C\) is closed because \(B\) is compact and \(C\) is closed. Its complement is invariant under \(-C\): if \(y-c\in B+C\), then \(y\in B+C\). Also \(\Omega-C\subset\Omega\). The ball \(B\) lies in \(S\), so \(y_0\in\operatorname{Int}S\).

For every compact \(L\) and every \(y=l+c\in\Omega\cap(L+C)\), one has
\[
\kappa|c|\le\ell(c)=\ell(y)-\ell(l)<a-\inf_L\ell .
\tag{H10}
\]
Thus this intersection is bounded and relatively compact. Its closure lies in the closed bounded set \((L+C)\cap\{\ell\le a\}\). In particular \(S\) has compact closure. This proves all the forward-slice bounds needed below, including those for arbitrary intersections of \(\Omega,\Omega'\) with a \(D\)-open.

Use \(H\) in the first Hom argument and localize by this lens. For a locally closed set \(S\), write \(H_S=k_S\otimes H\); \(k_S\) is flat since its stalks are \(k\) or zero. The relevant object and its actual currying identification are
\[
\begin{aligned}
K_S&=R\mathcal Hom(q_Y^{-1}(H_S),q_X^!F)\\
&\simeq R\mathcal Hom(k_{E_X\times S},K(F,H)).
\end{aligned}
\tag{H11}
\]
The second expression means internal Hom with the locally closed coefficient sheaf, not an unexplained support functor on an arbitrary nonclosed set. It equals ordinary derived sections with support when the set is closed. In the present case it is the fibre of the two ordinary open images associated to \(\Omega'\subset\Omega\). Since \(H_S\) is still bounded, (H4) makes \(K_S\) bounded below, even over arbitrary \(k\). On \(E_X\times\operatorname{Int}S\) it is naturally identified with \(K(F,H)\), and hence with \(K(F,G)\) near the point under consideration.

There need not be a global morphism \(K_S\to K(F,H)\) for a locally closed \(S\). The proof uses the canonical local identification on the interior and the following actual fibre maps. Tensor the exact coefficient-set triangle \(k_{\Omega'}\to k_\Omega\to k_S\) with \(H\), apply the contravariant first Hom argument, and take sections. For every ordinary open \(U\subset E_X\) and \(D\)-open \(W\subset E_Y\), this gives
\[
\begin{aligned}
R\Gamma(U\times W;K_S)
\simeq\operatorname{fib}\bigl[
 &R\Gamma(U\times(W\cap\Omega);K(F,H))\\
 &\longrightarrow R\Gamma(U\times(W\cap\Omega');K(F,H))
\bigr].
\end{aligned}
\tag{H12}
\]
For an open inclusion \(j\), the identity
\(R\mathcal Hom(k_O,A)=Rj_*(A|_O)\)
follows from \(j_!\dashv j^{-1}\), or directly on injective representatives. This identifies the two terms and the arrow in (H12) as the stated ordinary sections and their restriction map.

The pair \(W\cap\Omega'\subset W\cap\Omega\) satisfies all the hypotheses of (H7): both opens are \(D=-C\)-invariant, their difference lies in the relatively compact \(S\), and (H10) bounds all forward slices. Hence
\[
R\Gamma_c(W\cap\Omega';H)
 \xrightarrow{\ \sim\ }
R\Gamma_c(W\cap\Omega;H).
\tag{H13}
\]
By (H2)–(H3), the arrow inside the fibre in (H12) is precomposition with exactly (H13), with second Hom argument \(R\Gamma(U;F)\). It is therefore an isomorphism. All these rectangular section complexes of \(K_S\) vanish, so the same basis argument as in (H6) gives
\[
Rq_{\{0\}\times D*}K_S=0,\qquad
\langle(\xi,-\eta_0),(0,-c)\rangle
 =\langle\eta_0,c\rangle<0
 \quad(c\in C\setminus\{0\}).
\tag{H14}
\]
The cone test excludes \((x_0,y_0;\xi,-\eta_0)\) for every \(\xi\). Local agreement transfers this exclusion to the original kernel. Together with the first-factor exclusion and the zero-covector cases, this proves (H1).

The geometry was fixed before taking any cohomological degree. Its angular inequalities hold with a strict margin on compact unit cone sections, and the local representative agrees on a fixed ordinary neighborhood. Thus the exclusions hold on cotangent neighborhoods, as the definition of microsupport requires. For a family with a common avoided cotangent neighborhood, the uniform cap construction allows the same cone and lens. One must separately impose the common cohomological bounds needed for any subsequent bounded-below product argument; individual boundedness does not imply such common bounds.

### A stalk cannot be moved through an infinite Hom {#external-hom-infinite-check}

Let \(k\ne0\), let \(M=\bigoplus_{j\ge1}k\), and on \(X=\mathbb R\) let \(A=\bigoplus_{j\ge1}k_{\{1/j\}}\). Compare the stalk at zero of \(\mathcal Hom(M_X,A)\) with \(\operatorname{Hom}_k(M,A_0)\). Explain why the rectangle argument retained ordinary neighborhoods inside its Hom.

**Solution.** Exact stalks commute with direct sums, so \(A_0=0\). For each basis vector \(e_j\) of \(M\), send the associated constant generator to the global section \(1\) of the summand \(k_{\{1/j\}}\). The universal property of the direct sum defines a morphism \(M_X\to A\). Its restriction to every neighborhood of zero is nonzero, since that neighborhood contains \(1/j\) for all sufficiently large \(j\). Thus
\[
\bigl(\mathcal Hom(M_X,A)\bigr)_0\ne0,
\qquad
\operatorname{Hom}_k(M,A_0)=0.
\tag{H15}
\]
The same example applies in degree zero to derived Hom. With \(Y\) a point and \(G=M\), it is an instance of the kernel in (H1). Moving the neighborhood colimit through the first, infinite Hom argument would give the wrong result. This does not contradict the zero-section criterion: \(A_0=0\), but \(A\) does not vanish on any neighborhood of zero.

### Why an arbitrary ring gives a bounded-below output {#external-hom-ring-check}

Take both manifolds to be a point, \(k=\mathbb Z/4\mathbb Z\), and \(F=G=\mathbb Z/2\mathbb Z\). Determine whether the output of (H1) is bounded.

**Solution.** The free resolution of \(G\) has every term \(k\), with each differential multiplication by \(2\). Its image and kernel are both \(2k\), so it is exact in positive resolution degrees. Applying \(\operatorname{Hom}_k(-,\mathbb Z/2\mathbb Z)\) makes every differential zero. Therefore \(\operatorname{Ext}^r_k(G,F)=\mathbb Z/2\mathbb Z\) for every \(r\ge0\). The output is bounded below but not above. Formula (H1) still applies. Finite global dimension in the optional upper bound cannot simply be omitted, even for these finite modules.

### The second covector must change sign {#external-hom-sign-check}

Let \(X\) be a point, \(Y=\mathbb R\), \(F=k\), and \(G=k_{[0,\infty)}\), with \(k\ne0\). Check the direction at the boundary.

**Solution.** With an orientation of the line, \(q_X^!k=k_{\mathbb R}[1]\). Thus the kernel is \(R\Gamma_{[0,\infty)}k_{\mathbb R}[1]\). Closed-support localization identifies it with \(k_{(0,\infty)}[1]\): on the positive open ray it is \(k[1]\), on the negative ray it vanishes, and at zero the restriction \(k\to R\Gamma((-\epsilon,0);k)=k\) is the identity, so the supported stalk is zero. Open–closed localization supplies the stated sheaf identification.

The closed ray has the positive boundary covectors; the open ray has the negative boundary covectors, as the one-dimensional support tests show. A shift changes neither set. Consequently omitting the antipode from (H1) would give a false inclusion. The compact-support extension in (H13), entering Hom contravariantly, is the mechanism producing that sign.

## Normal scaling and the positive deformation {#normal-deformation-charts}

Let \(M\) be a closed smooth submanifold of a smooth manifold \(X\). Everything is local along \(M\), so an embedded submanifold closed in an ambient open set is also allowed. In adapted coordinates write \(X=(u,z)\) and \(M=\{u=0\}\). The deformation has coordinates \((v,z,t)\) and maps

\[
p(v,z,t)=(tv,z),\qquad
\Omega=\{t>0\},\quad j:\Omega\hookrightarrow\widetilde X_M,
\quad s:E=T_MX\hookrightarrow\widetilde X_M,\quad s(v,z)=(v,z,0).
\tag{N1}
\]

Here is why these local models glue, including the central fibre. A change of adapted coordinates is \(u'=f(u,z),\ z'=g(u,z)\), where \(f(0,z)=0\). Its deformation change is

\[
v'=\int_0^1 D_u f(rt v,z)\,v\,dr,
\qquad z'=g(tv,z),\qquad t'=t.
\tag{N2}
\]

For \(t\ne0\), the first expression equals \(f(tv,z)/t\), by the fundamental theorem of calculus. It is smooth also at zero. The inverse adapted change supplies its smooth inverse: their composites are the identity for \(t\ne0\), hence everywhere by continuity. The same argument verifies the cocycle. At zero the transition is \(v'=D_u f(0,z)v,\ z'=g(0,z)\), precisely the normal-bundle transition. Thus the central fibre is \(E\), while \(p\) identifies each nonzero fibre with \(X\). These compatible charts define the deformation manifold.

For \(F\in D^+(k_X)\), set

\[
\nu_MF=s^{-1}Rj_*p_+^{-1}F,
\qquad p_+=p|_\Omega.
\tag{N3}
\]

All functors here preserve a lower cohomological bound. The positive scaling
\((v,z,t)\mapsto(\lambda v,z,t/\lambda)\) leaves \(p\) unchanged and restricts on the central fibre to normal dilation. The section and support comparisons below construct the resulting coherent dilation isomorphism, including its restriction at zero; thus specialization is strongly conic in the sense of (C1).

## Neighborhoods of a noncompact locally closed set {#noncompact-neighborhood-gluing}

Fix an arbitrary commutative ring \(k\). In this section \(Y\) is locally compact Hausdorff and second countable, and \(Z\subset Y\) is locally closed. In particular these hypotheses hold for a locally closed subset of one of our metrizable manifolds. Write \(i:Z\hookrightarrow Y\). Sections on \(Z\) always mean sections of the inverse-image sheaf, not sections on \(Y\) supported in \(Z\).

We use the proved compact-germ comparison, compact lifting and c-soft quotient properties. Their proofs apply to locally compact Hausdorff spaces and arbitrary \(k\)-modules. We will extend the neighborhood comparison to noncompact \(Z\), rather than infer it from its compact version.

First choose an ambient open \(Y_0\) in which \(Z\) is closed. Neighborhoods contained in \(Y_0\) are cofinal among all ambient neighborhoods of \(Z\), so we may work in \(Y_0\). It is again locally compact Hausdorff and second countable. Such a space has a compact exhaustion

\[
K_1\subset\operatorname{int}K_2\subset K_2
\subset\operatorname{int}K_3\subset\cdots,
\qquad \bigcup_n K_n=Y_0.
\tag{T1}
\]

Indeed, a countable base and local compactness give a countable cover by relatively compact opens. At each stage cover the preceding compact set and the next compact closure by finitely many relatively compact opens and take the union of their closures. This gives (T1). The same argument applies to \(Z\), since it is closed in \(Y_0\); alternatively intersect this exhaustion with \(Z\).

We will need a locally finite refinement with controlled closures. Given an open cover of \(Y_0\), cover the compact shell \(K_n\setminus\operatorname{int}K_{n-1}\) by finitely many opens \(N_{nj}\) whose compact closures lie both in a cover member and in \(\operatorname{int}K_{n+1}\setminus K_{n-2}\). Put \(K_j=\varnothing\) for \(j\le0\). Such pointwise shrinkings exist by local compactness and Hausdorff separation. The shells are covered, and the family of all these closures is locally finite: a neighborhood inside \(\operatorname{int}K_m\) meets no member with \(n\ge m+2\), and only finitely many members were chosen at each earlier stage.

**Neighborhood gluing.** For every sheaf \(Q\) of \(k\)-modules, the natural restriction map is an isomorphism

\[
\underset{Z\subset U\text{ open in }Y}{\operatorname{colim}}
\Gamma(U;Q)
\xrightarrow{\sim}\Gamma(Z;i^{-1}Q).
\tag{T2}
\]

The transition maps are restrictions to smaller neighborhoods. To prove surjectivity, let \(s\) be a section on \(Z\). By the sheaf definition of inverse image, it is locally represented by sections \(s_a\in\Gamma(O_a;Q)\), where the \(O_a\) are ambient opens covering \(Z\), and each \(s_a\) represents \(s\) on all of \(O_a\cap Z\). Shrinking the original representative domain ensures this last condition.

Apply the preceding refinement to the cover consisting of the \(O_a\) and \(Y_0\setminus Z\). Discard members assigned to \(Y_0\setminus Z\). Relabel the remaining family \(N_j\), with \(\overline{N_j}\subset O_{a(j)}\). It still covers \(Z\), and its closures are locally finite in \(Y_0\). For each pair let \(E_{jk}\subset O_{a(j)}\cap O_{a(k)}\) be the open locus where the two representative germs agree. Set

\[
D_{jk}=(\overline{N_j}\cap\overline{N_k})\setminus E_{jk},
\qquad
D=\bigcup_{j,k}D_{jk},
\qquad
U=\left(\bigcup_jN_j\right)\setminus D.
\tag{T3}
\]

Each \(D_{jk}\) is closed in \(Y_0\). It misses \(Z\), because both representatives have the prescribed germ \(s_z\) at any \(z\in Z\cap\overline{N_j}\cap\overline{N_k}\). Local finiteness of the closures makes the family of pairwise intersections locally finite; hence \(D\) is closed and disjoint from \(Z\). Thus \(U\) is an actual open neighborhood of \(Z\). On \(N_j\cap U\) the representatives agree on all overlaps and glue to a section representing \(s\). This is the required noncompact gluing step.

For injectivity, two sections with equal restriction to \(Z\) have equal germs at every point of \(Z\). Their equality locus is open in their common domain and contains \(Z\); restricting to that neighborhood identifies their classes. No compactness is needed for this part.

## Derived neighborhood comparison with arbitrary coefficients {#derived-locally-closed-tautness}

For \(F\in D^+(k_Y)\) and every integer \(q\), restriction induces

\[
\underset{Z\subset U\text{ open}}{\operatorname{colim}}
H^q(U;F)
\xrightarrow{\sim}
H^q(Z;i^{-1}F).
\tag{T4}
\]

Here are the resolution facts needed to derive (T2). If \(I\) is injective on \(Y\), it is flabby: the monomorphism \(k_U\hookrightarrow k_V\) for opens \(U\subset V\) makes restriction \(\Gamma(V;I)\to\Gamma(U;I)\) surjective. Its restriction to \(Z\) is c-soft. A section on a compact \(C\subset Z\) is, by the owned compact-germ comparison on \(Y\), represented on an ambient neighborhood of \(C\). Flabbiness extends that representative to \(Y\); restricting the extension to \(Z\) proves c-softness. This reasoning uses the compact theorem already proved, not the new derived assertion.

C-soft sheaves on a second-countable locally compact Hausdorff space are acyclic for ordinary sections. For completeness, the precise exhaustion argument is as follows. In an exact sequence \(0\to S\to E\to Q\to0\) with \(S\) c-soft, a global section of \(Q\) lifts over each compact set in an exhaustion (T1), by compact lifting. Given a lift over \(K_n\), choose any lift over \(K_{n+1}\). Their difference on \(K_n\) is a section of \(S|_{K_n}\), so c-softness extends it globally. Correct the second lift by that extension. The corrected lifts agree on nested interiors and glue to a global lift. Thus ordinary sections are right exact on such sequences. Embed a c-soft sheaf into an injective; the quotient is c-soft by the owned compact quotient argument. Repeat. Ordinary sections of this injective resolution are exact in positive degrees, proving acyclicity. This proof uses a compact exhaustion, not a manifold structure on \(Z\).

The new underived theorem also gives a stronger property for these particular resolutions. If \(I\) is ambient flabby and \(W\subset Z\) is open, then \(W\) is locally closed in \(Y\). Apply (T2) to \(W\): any section of \(i^{-1}I\) on \(W\) is represented on an ambient open neighborhood, and flabbiness of \(I\) extends it to \(Y\). Restriction to \(Z\) extends the original section. Thus \(i^{-1}I\) is itself flabby here. This follows from the proved locally closed gluing theorem; it is not an assertion that arbitrary inverse-image functors preserve flabby sheaves.

Now choose a bounded-below injective representative \(I^\bullet\) of \(F\). Open restriction preserves injectives, because its left adjoint, extension by zero, is exact. Hence \(\Gamma(U;I^\bullet)\) computes \(R\Gamma(U;F)\). Exact inverse image and the preceding c-soft acyclicity show that \(\Gamma(Z;i^{-1}I^\bullet)\) computes \(R\Gamma(Z;i^{-1}F)\), by the bounded-below acyclic-resolution comparison. Applying (T2) in each degree gives the actual complex identity

\[
\underset{U\supset Z}{\operatorname{colim}}\Gamma(U;I^\bullet)
\xrightarrow{\sim}\Gamma(Z;i^{-1}I^\bullet).
\tag{T5}
\]

Filtered colimits of modules are exact, so they commute with cohomology. This proves (T4) for the specified restriction map. There is no infinite-product/stalk interchange, no uniform compact neighborhood of \(Z\), and no finite global dimension hypothesis on \(k\).

The empty-subset comparison is zero on both sides, since the empty neighborhood is permitted. The proof concerns one fixed locally closed subset. It does not assert a continuity theorem for arbitrary varying subsets, an arbitrary inverse system, or an arbitrary non-locally-closed subset; such claims require their own hypotheses and proof.

## Supported comparison uses two varying neighborhoods {#supported-neighborhood-pairs}

Let \(A\subset Z\) be closed in \(Z\). Index pairs of ambient opens \((U,V)\) satisfying \(Z\subset U\) and \(Z\setminus A\subset V\subset U\), ordered by simultaneous shrinking. This system is filtered by intersections. There is a natural isomorphism

\[
\underset{(U,V)}{\operatorname{colim}}
H^q_{U\setminus V}(U;F)
\xrightarrow{\sim}
H^q_A(Z;i^{-1}F).
\tag{T6}
\]

The support \(U\setminus V\) is closed in \(U\) and meets \(Z\) only in \(A\). The map is induced by the restriction square for \(U,V\) and \(Z,Z\setminus A\), using the actual localization triangles

\[
\begin{array}{ccccc}
R\Gamma_{U\setminus V}(U;F)&\longrightarrow&R\Gamma(U;F)&\longrightarrow&R\Gamma(V;F)\xrightarrow{+1}\\
\downarrow&&\downarrow&&\downarrow\\
R\Gamma_A(Z;i^{-1}F)&\longrightarrow&R\Gamma(Z;i^{-1}F)&\longrightarrow&R\Gamma(Z\setminus A;i^{-1}F)\xrightarrow{+1}.
\end{array}
\tag{T7}
\]

One may take the left map to be the map of mapping fibres of the ordinary restriction square; this fixes it on complexes, rather than choosing an abstract isomorphism after computing groups. For the ambient injective representative, flabbiness makes \(\Gamma(U;I^m)\to\Gamma(V;I^m)\) onto, so its kernel complex computes the upper supported term. The lower fibre computes the lower supported term because both ordinary section complexes of \(i^{-1}I^\bullet\) compute their derived sections. C-softness alone is not being used to assert acyclicity for a fixed-support functor.

The projection of the pair system to neighborhoods of \(Z\) is cofinal: one can use \((U,U)\) and then common intersections. Its projection to neighborhoods of \(Z\setminus A\) is likewise cofinal: one can use \((Y,V)\), and intersections give common refinements with any other pair. Both \(Z\) and \(Z\setminus A\) are locally closed. Apply (T4) to the two ordinary terms of (T7), and take the exact filtered colimit of the long exact sequences. The five lemma gives (T6), compatibly with the localization maps.

It would be wrong to replace this varying-pair statement by commutation with a fixed ambient support. For example, take \(Y=\mathbb R\), \(Z=\{0\}\), and the constant sheaf \(k_Y\), with \(k\ne0\). Then \(R\Gamma_{\{0\}}(U;k_Y)\simeq k[-1]\) on small intervals, whereas \(R\Gamma_Z(Z;k)\simeq k\). In (T6) one may take \(V=\varnothing\), so the varying support is the entire shrinking neighborhood \(U\); the correct comparison gives \(k\) without a shift.

## Ordinary interval fibres and actual product base change {#ordinary-interval-fibre-unit}

We use the proved proper-interval unit and relative contraction, valid for \(D^+\) and arbitrary coefficients. Namely, a map of locally compact Hausdorff spaces with a section and a homotopy over the base from the identity to that section induces an isomorphism on ordinary derived sections of every inverse-image coefficient complex. Its proof uses properness only of the auxiliary projection with fibre \([0,1]\), not of the given map.

Let \(B\) be locally compact Hausdorff and \(W\subset B\times\mathbb R\) be open, with nonempty interval fibres over \(B\). For \(L\in D^+(k_B)\), the actual adjunction unit is an isomorphism

\[
L\xrightarrow{\sim}R\pi_*\pi^{-1}L,
\qquad \pi:W\longrightarrow B.
\tag{T8}
\]

This is local on \(B\). At \(b_0\), choose \(t_0\in W_{b_0}\) and an open neighborhood \(O\) such that \(O\times\{t_0\}\subset W\). On \(W|_O\) the section \(b\mapsto(b,t_0)\) and the homotopy \((b,t,s)\mapsto(b,(1-s)t+st_0)\) stay in every interval fibre. They remain valid on every open subset of \(O\). Relative contraction therefore gives the ordinary-section unit on all these opens, and proves (T8). This argument needs neither an orientation nor exceptional inverse image nor a globally chosen section. Empty fibres are handled by first replacing \(B\) by the open image of \(W\). For positive-parameter intervals one can use the same affine formula directly, or the coordinate \(\log t\).

Consequently ordinary direct image has the following particular product base change. For a continuous map \(f:Y\to X\) of locally compact Hausdorff spaces, put \(\widetilde f=f\times\operatorname{id}_J\), where \(J\) is an open real interval, and let \(q_X,q_Y\) be the projections. For \(K\in D^+(k_Y)\),

\[
q_X^{-1}Rf_*K\xrightarrow{\sim}
R\widetilde f_*q_Y^{-1}K.
\tag{T9}
\]

The canonical map is adjoint to the pullback of the counit \(f^{-1}Rf_*K\to K\). On rectangle neighborhoods \(O\times I\) of \((x,t)\), its right-hand cohomology stalk is the colimit of \(H^q(f^{-1}O\times I;q_Y^{-1}K)\). The interval contraction identifies this with \(H^q(f^{-1}O;K)\) by the actual pullback map, naturally under both restrictions. Their colimit is the left-hand stalk. This proves the specified map in (T9), even when \(f\) is nonproper. It proves this product case, not an unrestricted nonproper base-change theorem.

## Normal scaling and strong conicity {#specialization-strong-conicity}

Let \(M\hookrightarrow X\) be a closed embedded submanifold of a finite-dimensional second-countable manifold. Its normal deformation \(D=D_MX\) has central fibre \(E=T_MX\), inclusion \(s:E\hookrightarrow D\), positive chamber \(j:\Omega\hookrightarrow D\), and projection \(r:\Omega\simeq X\times\mathbb R_{>0}\to X\). In adapted coordinates these maps are \(p(v,b,t)=(tv,b)\) and \(t(v,b,t)=t\). For \(F\in D^+(k_X)\), define

\[
K=Rj_*r^{-1}F,
\qquad \nu_MF=s^{-1}K\in D^+(k_E).
\tag{T10}
\]

Exact inverse image and bounded-below ordinary direct image suffice for this definition. If \(F\in D^{[a,b]}\) and \(\dim X\le d\), the owned ordinary-image dimension bound on the \((d+1)\)-dimensional positive chamber gives the sufficient bound \(\nu_MF\in D^{[a,b+d+1]}\). No finite global dimension of \(k\) is needed for this ordinary construction.

The positive action on \(D\) is \(a_D(\lambda;v,b,t)=(\lambda v,b,t/\lambda)\). It preserves \(p\), \(\Omega\) and \(E\), and restricts on \(E\) to ordinary positive dilation. Let \(q_D\) and \(q_E\) denote the projections from the corresponding products with \(G=\mathbb R_{>0}\). Formula (T9) for the open inclusion \(j\), together with the change of coordinates \((\lambda,d)\mapsto(\lambda,a_D(\lambda,d))\), supplies actual base-change isomorphisms for both the projection and the action square. Since \(r\circ a_\Omega=r\circ q_\Omega\), their middle coefficients are canonically the same. They give

\[
a_D^{-1}K
\xrightarrow{\sim}R(\operatorname{id}_G\times j)_*a_\Omega^{-1}r^{-1}F
=R(\operatorname{id}_G\times j)_*q_\Omega^{-1}r^{-1}F
\xleftarrow{\sim}q_D^{-1}K,
\qquad
a_E^{-1}\nu_MF\xrightarrow{\sim}q_E^{-1}\nu_MF.
\tag{T11}
\]

The last comparison is inverse image of the first along \(\operatorname{id}_G\times s\). The equality in the middle is equality of the two composite inverse-image functors from \(X\), not a stalkwise choice. The comparisons are the canonical base-change maps from the counit, so they restrict to the identity at \(\lambda=1\). Their cocycle follows by pasting the action squares: both composites are adjoint to the same iterated counit under the equality \(a(\lambda,a(\mu,d))=a(\lambda\mu,d)\). This constructs a normalized strong conic structure. Pulling (T11) back along \(\lambda\mapsto(\lambda,v)\) identifies each orbit pullback with the constant complex of stalk \((\nu_MF)_v\), including a zero vector.

If \(S=\operatorname{supp}F\) is the closed support, then \(K\) vanishes away from the closure of \(r^{-1}S\): on such an open neighborhood the positive restriction is zero. Hence

\[
\operatorname{supp}(\nu_MF)\subset
E\cap\overline{r^{-1}S}=C_M(S).
\tag{T12}
\]

Neither equality of these supports nor a microsupport theorem is asserted.

## The parameter-fibre refinement in the deformation {#normal-parameter-neighborhoods}

The remaining geometric input can be proved without sheaf theory. We use the already stated differential-topology prerequisites: deformation charts and their functorial gluing, a smooth tubular neighborhood of the closed embedded submanifold, and a bundle metric. They remain distinct from the sheaf comparison proved above.

For the present local microlocal-Hom applications, first restrict to an adapted product chart, or to the vector-space coordinates \((x-y,y)\) for the diagonal. The identity product chart is then the required tubular identification, with its Euclidean metric. Every stalk and local involutivity argument below is computed after such restrictions, so those applications require no separate global tubular-neighborhood theorem. The global statement retained here has the explicitly stated additional geometric input.

Let \(V\subset E\) be open and positive-conic, and \(W\subset D\) any open neighborhood of \(V\). A tubular neighborhood identifies a neighborhood of \(M\) with a disk neighborhood \(D_0\subset E\), with identity normal differential. Its deformation identifies \(p^{-1}(D_0)\) with

\[
Q=\{(m,v,t):tv\in(D_0)_m\},
\qquad p(m,v,t)=(m,tv).
\tag{T13}
\]

Intersect \(W\) with this neighborhood; it still contains all of \(V\). Put \(A=\{m:0_m\in V\}\). It is open, and positive conicity implies \(E|_A\subset V\). For a positive-fibre base point \(x=(m,w)\in D_0\), define

\[
I_x=\{a>0:(m,w/a,a)\in W\}.
\tag{T14}
\]

For \(w\ne0\), choose the connected component of \(I_x\) containing \(\|w\|\), if that time belongs to \(I_x\), and choose the empty set otherwise. Denote it by \(J_x\). For \(w=0,m\in A\), instead take the initial component

\[
J_{(m,0)}=\{a>0:(m,0,b)\in W\text{ for all }0\le b\le a\}.
\tag{T15}
\]

It is a nonempty open interval, by openness at the compact segment up to any one of its points. For \(w=0,m\notin A\), take \(J_x=\varnothing\). Let \(W_+\) consist of \((m,w/a,a)\) with \(a\in J_x\), and set

\[
W_0=(W\cap\{t<0\})\cup V\cup W_+.
\tag{T16}
\]

We verify openness, since merely selecting a fibrewise interval would not suffice.

- At a positive point with \(w\ne0\), the compact time segment connecting its time to the anchor \(\|w\|\) lies in \(I_x\). Continuous dependence of both endpoints, compactness and openness keep that entire segment in \(W\) for nearby points.
- At a positive point \((m_0,0,t_0)\), take \(t_1>t_0\) whose full zero-axis segment lies in \(W\). The central unit disk over \(m_0\) is in \(V\), since \(m_0\in A\). Compactness gives a base neighborhood \(B\subset A\), \(0<\delta<t_0\), and \(\epsilon>0\) such that the disk box \(\|v\|\le1,0\le a\le\delta\) and the thin box \(\|v\|<\epsilon,\delta\le a\le t_1\), both over \(B\), lie in \(W\). For small nonzero \(w\), the path from \(a=\|w\|\) to a time near \(t_0\) lies in the first box when \(a\le\delta\) and the second when \(a\ge\delta\), provided \(\|w\|<\delta\epsilon\). Nearby zero-axis points also lie in the chosen initial interval.
- At a central point with \(v_0\ne0\), use the compact family

\[
d_u(v)=(1-u)+u\|v\|,
\qquad
H_u(m,v,t)=\bigl(m,v/d_u(v),t\,d_u(v)\bigr),
\quad 0\le u\le1.
\tag{T17}
\]

  It preserves \(p\) and joins a positive point to its anchor. At \((m_0,v_0,0)\) it traces a compact radial segment contained in \(V\). A nearby entire family stays in \(W\), so every nearby positive point is selected. Shrink also to keep the central slice in \(V\) and the negative slice in \(W\).
- At a central zero vector, the central full unit disk again gives a base neighborhood and a small positive-time disk box in \(W\). For \(\|v\|<1\), the segment from anchor time \(t\|v\|\) to \(t\) remains in that disk box. For \(v=0\), the initial-axis definition applies. Together with the central and negative slices this is an open neighborhood in \(W_0\).

Thus \(V\subset W_0\subset W\) is open, and every positive parameter fibre over \(X\) is an interval or empty. Its image \(U_{W_0}=r(W_0\cap\Omega)\) is open because positive projection is a product projection. Intersections of these neighborhoods again have interval fibres, so they form a filtered cofinal neighborhood family. The rank-zero case uses only the initial-axis construction; the empty case is immediate. There is no uniform choice of radius over a noncompact base or over all directions.

## Ordinary specialization sections and their maps {#specialization-neighborhood-sections}

For open conic \(V\subset E\), let \(\mathcal U(V)\) consist of open \(U\subset X\) with

\[
C_M(X\setminus U)\cap V=\varnothing.
\tag{T18}
\]

The cone is the central intersection of the closure of the positive lift. Therefore (T18) is equivalent to \(V\cup r^{-1}U\) being open in \(D_{\ge0}\). Indeed its complement is the positive lift of the closed set \(X\setminus U\), together with \(E\setminus V\); (T18) says that the latter contains all newly added central limit points. This also proves that intersections of admissible opens remain admissible, using the finite-union property of closure.

For an admissible \(U\), choose an ambient open \(W\subset D\) whose intersection with \(D_{\ge0}\) is \(V\cup r^{-1}U\). The actual map is

\[
R\Gamma(U;F)
\xrightarrow{r^*}R\Gamma(r^{-1}U;r^{-1}F)
\simeq R\Gamma(W;K)
\longrightarrow R\Gamma(V;\nu_MF).
\tag{T19}
\]

The middle identification is derived ordinary direct-image composition for the open inclusion. Choices of the negative part of \(W\) disappear after taking common intersections, since all terms \(R\Gamma(W;K)\) are computed on \(W\cap\Omega\). Hence (T19) is independent of that choice and natural under restriction in \(U\).

Since \(V\) is open in the closed central fibre, it is locally closed in \(D\), even when it is noncompact. Formula (T4), followed by ordinary direct-image composition, gives

\[
H^q(V;\nu_MF)
\simeq\underset{W\supset V}{\operatorname{colim}}
H^q(W\cap\Omega;r^{-1}F)
\simeq\underset{U\in\mathcal U(V)}{\operatorname{colim}}H^q(U;F).
\tag{T20}
\]

For the second comparison refine \(W\) by (T16) and apply (T8) to its positive projection onto \(U_W\). The descent isomorphism is the actual pullback unit, so it is compatible with restrictions between refinements. Each \(U_W\) is admissible: the neighborhood \(W\) contains \(V\) and its positive part lies in \(r^{-1}U_W\), so no central point of \(V\) lies in the closure of the complementary positive lift. Conversely an admissible \(U\) gives the neighborhood in (T19), and an interval-fibre refinement inside it has image contained in \(U\). These refinements show cofinality and prove that the isomorphism in (T20) is precisely induced by (T19).

For completeness, strong conicity justifies the corresponding stalk formula without pretending that conic opens form an ordinary neighborhood basis:

\[
H^q(\nu_MF)_v
\simeq
\underset{v\notin C_M(X\setminus U)}{\operatorname{colim}}H^q(U;F).
\tag{T21}
\]

Away from zero, polar coordinates identify a conic neighborhood with an angular/base open times \(\mathbb R_{>0}\). Restricting (T11) to its unit-radius section identifies the sheaf with the inverse image from that section. The interval unit computes the same stalk from conic sections. At a zero vector, any conic neighborhood contains the whole bundle over some base neighborhood. Restriction from that bundle to a small fibrewise ball induces an isomorphism: apply (T8) to the action map from the ball times \(G\), whose fibre over a vector \(w\ne0\) is the interval \((\|w\|/\epsilon,\infty)\), and whose fibre over zero is all of \(G\); (T11) then identifies the composite with the actual restriction, by its identity normalization at \(1\). Balls and base opens compute the ordinary zero stalk. Finally the complement of any closed conic set is open conic, which identifies the admissible systems in (T20) and (T21).

## Specialization with closed conic supports {#specialization-supported-comparison}

Let \(A\subset E\) be closed and conic. Consider pairs \((U,Z)\) where \(U\subset X\) is an open neighborhood of \(M\), \(Z\) is closed in \(X\), and \(C_M(Z)\subset A\). Maps shrink \(U\) and enlarge \(Z\). Intersections of the neighborhoods and unions of supports make the system filtered. The natural comparison is

\[
\underset{(U,Z)}{\operatorname{colim}}
H^q_{Z\cap U}(U;F)
\xrightarrow{\sim}
H^q_A(E;\nu_MF).
\tag{T22}
\]

Use the square of ordinary-section maps supplied by (T19), for \(U\) and \(U\setminus Z\), and take the map of localization fibres

\[
\begin{array}{ccccc}
R\Gamma_{Z\cap U}(U;F)&\longrightarrow&R\Gamma(U;F)&\longrightarrow&R\Gamma(U\setminus Z;F)\xrightarrow{+1}\\
\downarrow&&\downarrow&&\downarrow\\
R\Gamma_A(E;\nu_MF)&\longrightarrow&R\Gamma(E;\nu_MF)&\longrightarrow&R\Gamma(E\setminus A;\nu_MF)\xrightarrow{+1}.
\end{array}
\tag{T23}
\]

The square commutes because all maps in (T19) are the same pullback and restriction maps on common deformation neighborhoods. Equivalently, the closure of the positive lift of \(Z\cap U\) meets \(E\) only in \(C_M(Z)\subset A\). The localization-fibre description specifies the actual supported map and all its transition compatibilities.

For the middle terms, \(C_M(X\setminus U)=\varnothing\) exactly when \(U\) contains \(M\): the converse follows because an excluded point of \(M\) contributes its zero normal vector. Forgetting \(Z\) is cofinal among neighborhoods of \(M\), since the empty support is allowed. Thus (T20) with \(V=E\) identifies the filtered middle terms.

For the right terms one has

\[
C_M\bigl(X\setminus(U\setminus Z)\bigr)
\subset C_M(X\setminus U)\cup C_M(Z)\subset A.
\tag{T24}
\]

Every admissible open \(W\) for \(E\setminus A\) occurs exactly as the complement term of \((X,X\setminus W)\). Cofinality includes the arrows, not just this assertion about objects: given \((U,Z)\) and an admissible \(W\), the pair \((U,Z\cup(X\setminus W))\) is an allowed common refinement whose complement is \((U\setminus Z)\cap W\). This proves directed cofinality of the complement system. Formula (T20) with \(V=E\setminus A\) therefore identifies the filtered right terms. Exactness of filtered colimits and the localization sequences proves (T22), with the map already fixed by (T23).

All of (T4)–(T24) have the stated bounded-below scope. The supported assertions are ordinary derived sections with a specified closed support, not compact-support pushforwards. The coefficient ring remains arbitrary. Tubular-neighborhood/deformation geometry, enough injectives, the owned compact-extension arguments, and the proper-interval unit are the explicit inputs; no nonproper closed-base-change theorem, Fourier theorem, or microsupport involutivity assertion has been used.

## Radial descent with actual dilation maps {#strong-conic-radial-descent}

Let \(E\to B\) be a real vector bundle of fixed finite rank over a manifold, and let \(k\) be a fixed commutative coefficient ring. All complexes in this section are bounded below. Write \(a(v,t)=tv\), \(p(v,t)=v\), and \(e(v)=(v,1)\). We call \(F\) strongly conic when it comes with a natural dilation isomorphism

\[
\theta:p^{-1}F\xrightarrow{\sim}a^{-1}F,
\qquad e^{-1}\theta=\mathrm{id},
\qquad \theta(v,st)=\theta(sv,t)\theta(v,s).
\tag{C1}
\]

The last equality is an equality of pullback morphisms, not merely a collection of stalk identifications. This sufficient hypothesis is used throughout; no converse from orbitwise cohomological local constancy is needed. It includes the zero section, where the action fixes each point.

Choose a local bundle metric and let \(i_S:S(E)\hookrightarrow\dot E\) be its unit sphere. The map \(h:S(E)\times(0,\infty)\to\dot E\), \(h(s,r)=rs\), is a diffeomorphism. Pulling (C1) back along \((s,r)\mapsto(i_S(s),r)\) gives the actual descent isomorphism

\[
h^{-1}(F|_{\dot E})\simeq q^{-1}G,
\qquad G=i_S^{-1}F,
\qquad q:S(E)\times(0,\infty)\longrightarrow S(E).
\tag{C2}
\]

Its restriction at \(r=1\) is the identity. The ordinary interval-contraction unit \(G\to Rq_*q^{-1}G\) is an isomorphism, so evaluation on the sphere identifies \(Rq_*h^{-1}F\) with \(G\). There is no appeal to ordinary base change for a general nonproper map.

We use the smooth-submersion microsupport formula and the closed-embedding formula in their bounded-below scope. For the submersion formula, the forward estimate is the smooth constant-factor case of the compact-cap external-product proof: the added coefficient is the free constant sheaf in degree zero, so no flat resolution of an arbitrary second coefficient, finite global dimension, or upper truncation is involved. The reverse inclusion follows by pulling a base test function back to a product chart; the localization triangle and interval contraction identify its supported stalk with the base supported stalk. Iterating interval coordinates proves the assertion for a box. The closed-embedding proof is the identical supported-section and test-extension argument for a bounded-below injective resolution.

Applying the submersion formula to (C2) shows that every covector of \(\operatorname{SS}(F)\) off the zero section annihilates the radial Euler field. At the zero section that field is zero. Thus, in bundle coordinates,

\[
\operatorname{SS}(F)\subset
\{(z,x;\zeta,\xi):\langle x,\xi\rangle=0\}.
\tag{C3}
\]

The individual dilation isomorphisms in (C1), together with diffeomorphism covariance, also make microsupport invariant under the second of the two commuting positive actions

\[
r_\lambda(z,x;\zeta,\xi)=(z,x;\lambda\zeta,\lambda\xi),
\qquad
s_\mu(z,x;\zeta,\xi)=(z,\mu x;\zeta,\mu^{-1}\xi).
\tag{C4}
\]

The first invariance is ordinary cotangent conicity. No involutivity theorem is used here.

## Ordinary and supported radial contraction {#radial-contraction-maps}

### Exceptional pullback for a smooth projection {#relative-projection-purity}

We need the relative-purity formula with an arbitrary bounded-below target, not only the dualizing object. For a rank-\(r\) coordinate projection \(p:Y\times\mathbb R^r\to Y\), put \(\omega_p=\operatorname{or}_p[r]\). The orientation trace constructs a natural map
\(p^{-1}L\otimes\omega_p\to p^!L\) for every \(L\in D^+(k_Y)\): it is adjoint to integration
\(Rp_!(p^{-1}L\otimes\omega_p)\to L\). The compact-support coefficient comparison followed by the orientation trace defines this integration. Its comparison is invertible on proper-support fibres by the constant-coefficient compact cohomology of \(\mathbb R^r\); for \(D^+\) coefficients the bounded calculation extends degree by degree by truncation, since compact sections have finite cohomological dimension and the orientation line is flat. Thus this construction is valid over arbitrary \(k\).

The ordinary contraction used next is independent of relative purity. For the proper projection with fibre \([0,1]\), proper base change and constant-interval cohomology make its pullback unit an isomorphism; both endpoint restrictions are its inverse. A straight-line contraction of a convex ball to a section, over the unchanged base, consequently identifies restriction to that section with the inverse of the ordinary unit. This is the already proved relative-contraction argument used in (T8), before any appeal to (C5). No orientation is needed for this ordinary calculation. For the compact-support comparison above, only the flat orientation kernel is tensored; its finite cohomological dimension permits degreewise truncation without any finite flat resolution of \(L\).

Check the adjoint map on ordinary rectangles \(V\times B\), with \(B\) an oriented open ball. Ordinary contraction of \(B\), with its actual unit, identifies sections of the proposed source with \(R\Gamma(V;L)\otimes\operatorname{or}_B[r]\). On the target, exceptional adjunction identifies the section complex with \(R\operatorname{Hom}_Y(Rp_!k_{V\times B},L)\). Proper-support base change and open-extension composition give \(Rp_!k_{V\times B}=k_V\otimes\operatorname{or}_B[-r]\). Since the orientation module is locally free of rank one, the latter Hom is also \(R\Gamma(V;L)\otimes\operatorname{or}_B[r]\). Under these identifications the map is the identity: its adjoint is precisely the compact orientation trace on \(B\), followed by the counit for \(V\hookrightarrow Y\), and that trace takes the chosen orientation generator to one. This checks the map, not only its two objects.

Rectangles form an ordinary stalk basis. The cone of the comparison therefore has zero derived sections on that basis and zero cohomology stalks, proving the isomorphism \(p^!L\simeq p^{-1}L\otimes\operatorname{or}_p[r]\). Restricting to an open part of the projection gives the same isomorphism by exceptional composition with open extension, whose exceptional inverse image is ordinary restriction. Oriented changes of product chart identify the trace maps, so the local comparisons glue with the relative orientation line. This proves exactly the arbitrary-target smooth-projection formula used in (C5) and (C16), with no perfectness hypothesis on \(L\).

We first record the variable-interval calculation needed below. If \(r:W\to Y\) is the projection from an open subset of \(Y\times\mathbb R\), and every fibre is a nonempty interval, the oriented submersion identity and proper-support fibre formula give

\[
Rr_!\omega_r\xrightarrow{\operatorname{tr}}k_Y\quad\text{an isomorphism},
\qquad
Rr_*r^{-1}L
\simeq R\mathcal Hom(Rr_!\omega_r,L)
\simeq L,
\quad \omega_r=k_W[1].
\tag{C5}
\]

Indeed the trace stalk is integration of the oriented nonempty interval, hence an isomorphism. In the internal-Hom adjunction, precomposition with this trace is exactly the unit \(L\to Rr_*r^{-1}L\). The first internal-Hom argument is a shifted constant sheaf; the second is bounded below. These operations require no finite-generation or finite-global-dimension hypothesis. The identities are the already constructed exceptional projection adjunction and orientation trace, applied to an open part of a one-dimensional projection.

Let \(U\) be an open subset of a space with positive dilation, and suppose that for every point \(v\), the set of parameters \(t>0\) with \(t^{-1}v\in U\) is a nonempty interval in \(\log t\). The restricted action \(b:U\times(0,\infty)\to E\) becomes the projection from that open interval-fibre set after the change \((u,t)\mapsto(tu,t)\). Applying (C5), then (C1), then evaluation at \(t=1\), gives

\[
R\Gamma(E;F)\xrightarrow{\sim}R\Gamma(U\times(0,\infty);b^{-1}F)
\xrightarrow{\sim}R\Gamma(U;F|_U).
\tag{C6}
\]

This composite is the actual restriction: the action at parameter one is the inclusion of \(U\), and the dilation isomorphism is the identity there. Consequently the comparisons commute with further restriction of the open sets.

Write \(\tau:E\to B\) and \(i:B\hookrightarrow E\) for the projection and zero section. In a trivialization, (C6) applies to every fibrewise ball \(V\times B_\epsilon\): for a nonzero vector the parameter interval is \((|x|/\epsilon,\infty)\), and at zero it is all of \((0,\infty)\). Taking the compatible neighbourhood colimits over \(V\) and \(\epsilon\) proves

\[
\rho_F:R\tau_*F\xrightarrow{\sim}i^{-1}F,
\qquad
\rho_F=i^{-1}(\tau^{-1}R\tau_*F\longrightarrow F).
\tag{C7}
\]

This is stalk continuity over an ordinary open neighbourhood basis. It is not a noncompact-subspace tautness assertion.

For the second comparison, apply (C6) on the punctured bundle to the complement of a closed disk. Its parameter interval is \((0,|x|/R)\). The localization triangles for the zero section and for the closed disk therefore identify inclusion of zero-section support into disk support. Closed disk supports are cofinal among proper supports after shrinking the base: a support proper over \(V\) has compact intersection over the compact closure of a smaller base neighbourhood contained in \(V\), and hence has bounded fibre norm over that smaller neighbourhood. The proper-support construction and this cofinality prove

\[
\sigma_F:i^!F\simeq R\tau_!i_*i^!F\xrightarrow{\sim}R\tau_!F.
\tag{C8}
\]

The arrow is the closed-embedding counit. Both contractions have no orientation twist or shift. For rank zero, projection and zero section are identities and both maps are identities; for empty base all objects vanish.

## A punctured ordinary image through a proper sphere map {#punctured-sphere-pushforward}

Let \(\beta:S(E)\to B\). Equations (C2) and interval contraction identify \(R\dot\tau_*F\) with \(R\beta_*G\), by the actual radial evaluation map. The sphere projection is proper, so the owned proper-image estimate applies. The submersion equality in (C2) identifies a horizontal covector of \(G\) with the same base covector and zero vertical covector of \(F\) on the sphere. Equivalently, sphere restriction cannot conceal a radial conormal: (C3) annihilates the Euler field, whereas every nonzero sphere conormal pairs nontrivially with it. We obtain

\[
\operatorname{SS}(R\dot\tau_*(F|_{\dot E}))
\subset
\{(z;\zeta):\text{some }x\ne0\text{ satisfies }(z,x;\zeta,0)\in\operatorname{SS}(F)\}.
\tag{C9}
\]

This image is closed locally: dilation carries its witnesses to the sphere, and the sphere projection on these horizontal covectors is proper. Thus (C9) supplies an actual witness, not only membership in an unspecified closure. When the rank is zero the punctured bundle is empty. This proof supplies exactly the ordinary punctured estimate needed below without a general nonproper-image theorem.

## The Fourier kernel and its supported expression {#fourier-supported-kernel}

On \(E\times_B E^*\), let \(p,q\) be the projections to \(E,E^*\), and set

\[
N=\{\langle x,y\rangle\le0\},\qquad
C=\{\langle x,y\rangle\ge0\},\qquad
TF=Rq_!((p^{-1}F)_N).
\tag{C10}
\]

Here the subscript \(N\) means tensor with the flat constant extension sheaf \(k_N\). It is not local cohomology. The rank is finite, so this proper-support image preserves bounded-below complexes. The transform is strongly conic in \(y\): positive scaling of \(y\) preserves the kernel, and proper-support base change constructs the coherent normalized action isomorphisms.

For a strongly conic input there is a natural comparison

\[
TF\simeq Rq_*R\Gamma_C(p^{-1}F).
\tag{C11}
\]

Here are its actual maps. Put \(L=p^{-1}F\), \(H=R\Gamma_CL\), and \(W=\{\langle x,y\rangle>0\}\). Since the closure of \(W\) lies in \(C\), local cohomology with support in \(C\) acts as the identity on \(L_W\). Comparing the localization triangles for \(W\) and its complement gives

\[
R\Gamma_C(L_N)\simeq H_N.
\tag{C12}
\]

Moreover \(H_N\) is supported on \(x=0\). Near \(x\ne0\), use \(t=\langle x,y\rangle\) as one of the \(y\) coordinates, keeping \(x\) among the other coordinates. The coefficient \(L\) is pulled back from those other coordinates. At \(t=0\), the localization test for \(R\Gamma_{t\ge0}L\) compares sections of an interval and its negative half-interval. Both identify with the same coefficient by (C5), with the identity restriction map. Its supported stalk vanishes. It also vanishes for \(t<0\), proving the assertion.

The objects in (C12) are strongly conic under scaling \(x\). Conicity of local cohomology follows from its localization triangle and product/open base change; no arbitrary inverse-image/local-cohomology interchange is required. Apply (C8) to the first arrow below, properness on the actual zero-section support to the middle arrow, and (C7) to the last arrow:

\[
Rq_!L_N
\ \longleftarrow\ Rq_!R\Gamma_C(L_N)
\ \simeq\ Rq_!H_N
\ \longrightarrow\ Rq_*H_N
\ \longleftarrow\ Rq_*H.
\tag{C13}
\]

For the first arrow, restriction by the exceptional zero-section functor sees no change because that section lies in \(C\). For the last, ordinary zero-section restriction sees no change on passing from \(H\) to \(H_N\). Hence every displayed arrow is invertible and (C11) is proved.

## Testing on an open cone without using inversion {#fourier-open-cone-tests}

We require only the following elementary compact-support calculation. A nonempty open convex subset \(U\) of an oriented \(n\)-space has orientation trace \(R\Gamma_c(U;k)\simeq k[-n]\), compatible with extension between open convex sets. This follows from the owned Euclidean orientation calculation: translate an interior point to zero and let \(g\) be the continuous Minkowski gauge, so \(U=\{g<1\}\). The maps \(x\mapsto x/(1-g(x))\) and \(y\mapsto y/(1+g(y))\) are inverse orientation-preserving radial homeomorphisms with \(\mathbb R^n\), including directions where \(g=0\). Naturality of orientation trace identifies the extension map. Therefore localization gives

\[
R\Gamma_c(U\cap\{\ell\le0\};k)=0
\quad\text{whenever }U\cap\{\ell>0\}\ne\varnothing.
\tag{C14}
\]

Indeed the two open sets in the corresponding localization triangle have the same orientation generator and their extension map is an isomorphism. In particular a closed half-line has zero compactly supported cohomology. No cochain comparison for a one-point compactification, pointed closed-cone theorem, or global Poincaré-duality theorem is being inserted here.

Let \(V\subset E^*\) be open and fibrewise convex conic, and put \(B_0=\pi(V)\). Define its nonnegative polar only over this open base, and define a coefficient kernel on \(E|_{B_0}\) by

\[
D=V^\circ=\{x\in E|_{B_0}:\langle x,y\rangle\ge0\text{ for all }y\in V_{\tau(x)}\},
\qquad
K_V=Rp_{V!}\bigl(k_{C\cap(E\times_B V)}\otimes O_{E^*}[n]\bigr).
\tag{C15}
\]

The set \(D\) is closed in \(E|_{B_0}\): its complement is the projection of the open set of pairs with negative pairing. Each fibre of \(p_V:E\times_B V\to E|_{B_0}\) is a nonempty open convex set. Its orientation trace identifies the proper-support image of the full fibre with the constant sheaf. Inverting that trace and then restricting to \(C\) constructs \(k_{E|_{B_0}}\to K_V\). At a point of \(D\) the restriction retains the entire fibre and the map is an isomorphism. Outside \(D\), (C14), with \(\ell(y)=-\langle x,y\rangle\), makes its target zero. Closed localization now identifies \(K_V\) with \(k_D\). These are constructed maps, so stalk detection is legitimate. Over the empty fibres outside \(B_0\), extend by zero from the open base; do not assign the whole vector space as a vacuous polar.

Use (C11), then the exceptional projection adjunction on \(p_V\). Its relative dualizing object is \(O_{E^*}[n]\); twisting the first Hom argument by this object compensates for \(p_V^!\) in the second. This gives the actual natural chain

\[
\begin{aligned}
R\Gamma(V;TF)
&\simeq R\operatorname{Hom}_{E\times_B V}(k_C,p_V^{-1}F)\\
&\simeq R\operatorname{Hom}_{E|_{B_0}}(K_V,F|_{E|_{B_0}})\\
&\simeq R\Gamma_D(E|_{B_0};F|_{E|_{B_0}}).
\end{aligned}
\tag{C16}
\]

This proof does not require Fourier inversion. For \(V_1\subset V_2\), compact-support extension in the \(y\) variable gives \(K_{V_1}\to K_{V_2}\). Under the orientation identifications, this is the restriction map \(k_{V_1^\circ}\to k_{V_2^\circ}\), including the open-base extensions. Both objects are actual degree-zero sheaves; their stalk maps are the identity where both stalks are nonzero and zero otherwise. Consequently (C16) intertwines restriction of cone sections and enlargement of supports. That compatibility is needed for the stalk colimit below.

## The forward microsupport inclusion {#forward-fourier-microsupport}

In local bundle coordinates define

\[
\Phi_E(z,x;\zeta,\xi)=(z,\xi;\zeta,-x),
\qquad
\Phi_E^*\alpha_{E^*}=\alpha_E-d\langle x,\xi\rangle.
\tag{C17}
\]

The one-form identity shows that these expressions agree under changes of bundle coordinates; in particular the base covector is retained. We prove only the forward inclusion. Neither Fourier inversion nor microsupport involutivity is an input.

First suppose the vector \(x_0\) and vertical covector \(\xi_0\) are nonzero, and temporarily suppose \(R\Gamma_BF=0\), with \(B\) the zero section. Put \(H=R\Gamma_Cp^{-1}F\). The zero-section support of \(H\) vanishes: intersecting its closed support condition with \(x=0\) leaves precisely the pullback of \(R\Gamma_BF\). The open localization triangle therefore gives \(H\simeq Rj_*H|_{x\ne0}\). Together with (C11) and composition of ordinary images,

\[
TF\simeq R\dot q_*(H|_{x\ne0}).
\tag{C18}
\]

The coefficient on the right is strongly conic in \(x\). If \((z,\xi_0;\zeta,-x_0)\) belongs to \(\operatorname{SS}(TF)\), (C9) supplies some \(x_1\ne0\) such that \((z,x_1,\xi_0;\zeta,0,-x_0)\in\operatorname{SS}(H)\). Away from the incidence boundary, \(H\) is either zero or \(p^{-1}F\); the latter has zero \(y\)-covector. Thus \(\langle x_1,\xi_0\rangle=0\).

Here the needed supported-halfspace bound follows directly from the proved ordinary boundary estimate. Write \(g(x,y)=\langle x,y\rangle\), \(\Omega=\{g<0\}\), \(L=p^{-1}F\), and use the triangle \(R\Gamma_CL\to L\to Rj_*L|_\Omega\to\). The output covector under consideration has nonzero \(y\)-component, so it is absent from \(\operatorname{SS}(L)\). In the boundary bound for the last term, the signed normal is \(-\lambda\,dg\), \(\lambda\ge0\). In every limiting-sum witness its \(y\)-component is \(-\lambda_jx'_j\), while the \(L\)-covector has \(y\)-component zero. Since \(x'_j\to x_1\ne0\) and the output is finite, \(\lambda_j\) is bounded. After taking a subsequence, both summands converge; closedness of \(\operatorname{SS}(L)\) turns the limiting bound into the ordinary decomposition

\[
(\zeta,0,-x_0)=(\zeta,\alpha,0)-\lambda(0,\xi_0,x_1),
\qquad
(z,x_1;\zeta,\alpha)\in\operatorname{SS}(F),
\quad\lambda\ge0.
\tag{C19}
\]

It follows that \(x_0=\lambda x_1\), \(\alpha=\lambda\xi_0\), and \(\lambda>0\). Applying \(s_\lambda\) from (C4) gives \((z,x_0;\zeta,\xi_0)\in\operatorname{SS}(F)\). This proves the forward inclusion at these points, with the temporary assumption.

Remove that assumption by the natural triangle

\[
R\Gamma_BF\longrightarrow F\longrightarrow Rj_*(F|_{\dot E})\xrightarrow{+1},
\qquad
T(i_*i^!F)\simeq\pi^{-1}i^!F.
\tag{C20}
\]

The last identification is direct integration of the kernel on \(x=0\), where the pairing condition is automatic. Its microsupport has zero vertical covector and cannot contribute at \(-x_0\ne0\). The third term has no zero-section local cohomology and agrees with \(F\) near \(x_0\ne0\). The triangle inequality gives the desired inclusion without the temporary assumption.

To include both zero loci, add coordinates \((s,t)\) and their duals \((u,v)\). Define \(F'=F\boxtimes k_{\mathbb R\times\{0\}}\). This external product is simply submersion pullback in \(s\), followed by the closed embedding \(t=0\), so the exact submersion and closed-embedding formulas apply in \(D^+\). Direct integration of the Fourier kernel gives

\[
T_{E\oplus\mathbb R^2}F'
\simeq TF\boxtimes k_{\{0\}\times\mathbb R}[-1].
\tag{C21}
\]

Indeed \(t=0\), and the inequality is \(\langle x,y\rangle+su\le0\). Integrating \(s\) gives zero when \(u\ne0\), since its fibre is a closed half-line. At \(u=0\) it gives the original negative-pairing kernel times the oriented full-line cohomology \(k[-1]\). Proper-support base change along \(u=0\) and the closed localization triangle identify the whole intermediate object with this closed extension, not merely its stalks. The \(v\) variable is unrestricted. Remaining proper-support integration proves (C21).

If \(p=(z,x_0;\zeta,\xi_0)\) is absent from \(\operatorname{SS}(F)\), the exact product description makes

\[
p'=(z,x_0,1,0;\zeta,\xi_0,0,1)
\notin\operatorname{SS}(F'),
\qquad
\Phi(p')=(z,\xi_0,0,1;\zeta,-x_0,-1,0).
\tag{C22}
\]

Both relevant vectors of \(p'\) are nonzero. The preceding incidence argument excludes \(\Phi(p')\) from \(\operatorname{SS}(TF')\). On the right side of (C21), exact submersion pullback in \(v\) and closed extension at \(u=0\) allow every \(u\)-conormal coefficient, including \(-1\). Hence its exclusion is precisely the exclusion of \(\Phi_E(p)\) from \(\operatorname{SS}(TF)\). We have proved

\[
\operatorname{SS}(TF)\subset\Phi_E(\operatorname{SS}(F)).
\tag{C23}
\]

For rank zero, \(T\) and \(\Phi\) are identities; the same conclusion holds directly. Shifts in (C21) do not change microsupport. The proof uses only flat constant kernels and orientation lines, bounded-below local support, and finite-dimensional proper-support operations. It introduces no finite global dimension, constructibility, perfectness or finite-rank condition on the coefficient complex.

The inclusion explicitly includes a zero output cotangent covector. Such an output has \(\zeta=0\) and \(x_0=0\), while its base point \(\xi_0\) may be arbitrary. In (C22) the enlarged output still has the nonzero \(u\)-conormal coefficient \(-1\). The exact closed-embedding formula therefore detects the original zero output covector just as it detects a nonzero one. Thus (C23) can be applied to the zero covector over every point of the support of \(TF\).

## Strict normal supports at one covector {#strict-normal-support-stalks}

We now combine the supported specialization comparison with the proved Fourier kernel. Let \(L\in D^+(k_E)\) be strongly conic. In the application \(L=\nu_MF\), this hypothesis is supplied by (T11). For

\[
\mathsf T_E L
=Rq_!\bigl(p^{-1}L\otimes k_{\{\langle v,\xi\rangle\le0\}}\bigr),
\qquad \mu_MF=\mathsf T_E\nu_MF,
\tag{T25}
\]

the projections are \(p:E\times_M E^*\to E\) and \(q:E\times_M E^*\to E^*\). The kernel construction (C10) supplies its normalized strong conic structure, and (C16) supplies the following natural open-cone comparison for open fibrewise convex conic \(V\subset E^*\), with \(B=\pi(V)\):

\[
V^\circ=\{v\in E|_B:\langle v,\xi\rangle\ge0
\text{ for every }\xi\in V_{\tau(v)}\},
\qquad
R\Gamma(V;\mathsf T_E L)
\xrightarrow{\sim}R\Gamma_{V^\circ}(E|_B;L|_{E|_B}),
\tag{T26}
\]

The proof of (C16) identifies restriction in \(V\), restriction of the base and enlargement of the polar support with their actual kernel maps. Only this forward-kernel comparison and strong conicity are used below. Both are proved in \(D^+\) over arbitrary \(k\), so the following deductions retain that scope.

The polar is closed in \(E|_B\): a failed inequality is witnessed by a covector in the open set \(V\), and persists locally. It need not be closed in \(E\). Choose an ambient open \(O\subset X\) with \(O\cap M=B\). Restriction of the deformation construction to \(O\) shows that \(\nu_B(F|_O)=\nu_MF|_{E|_B}\); this follows directly by restricting \(j,r,s\) to open subsets, where ordinary direct image commutes with open restriction by its section definition. Apply (T22) inside \(O\) with support \(V^\circ\). Using (T26) gives

\[
H^q(V;\mu_MF)
\simeq\underset{U,Z}{\operatorname{colim}}
H^q_{Z\cap U}(U;F),
\quad U\cap M=B,
\quad C_M(Z)|_B\subset V^\circ.
\tag{T27}
\]

Here \(U\) is ambient open and \(Z\) is closed locally in \(O\), or closed in \(X\) after extension by closure. Those descriptions give the same system: if \(Z'\) is closed in \(O\), then \(\overline{Z'}^{X}\cap O=Z'\), and normal cones agree over \(B\) because they depend on germs there. Any \(U\) with \(U\cap M=B\) has a common refinement \(U\cap O\). These observations also preserve every restriction and support-enlargement map in (T23). The condition in (T27) is explicitly over \(B\), not over all of \(M\).

Fix \(\xi\in E_x^*\). Let \(\mathcal S_\xi\) be the system of germs at \(x\) of supports \(Z\) closed in some ambient open neighborhood of \(x\), such that

\[
C_M(Z)_x\subset
\{v\in E_x:\langle v,\xi\rangle>0\}\cup\{0\}.
\tag{T28}
\]

Thus a support is closed in some open neighborhood of \(x\); restriction identifies the same germ, and the order on germs is inclusion. Finite unions preserve (T28), so this is a filtered support system. The induced stalk formula is

\[
H^q(\mu_MF)_\xi
\simeq\underset{Z\in\mathcal S_\xi}{\operatorname{colim}}
H^q(R\Gamma_ZF)_x.
\tag{T29}
\]

We prove all cofinality assertions in this step. Strong conicity computes an ordinary stalk as the colimit of sections on open convex conic neighborhoods. Away from zero use a trivialization and polar coordinates, and compare a conic angular neighborhood with angular neighborhoods times bounded radial intervals by (T8). At zero use whole bundles over smaller base opens and their fibrewise balls. In detail the action map from a ball times \(G\) becomes an open projection with interval fibres, as in the proof of (T21); both its unit and the product-projection unit are invertible by (T8). Pulling back to the radius-parameter section \(1\), the normalized conic isomorphism identifies their composite with the actual restriction from the bundle to the ball. These comparisons prove the assertion about stalks, not an assertion that conic opens form an ordinary topological basis.

If a support occurs in (T27) for a neighborhood \(V\) of \(\xi\), every vector in \(C_M(Z)_x\) pairs nonnegatively with \(\xi\). A nonzero vector with zero pairing would pair negatively with a sufficiently small perturbation of \(\xi\) lying in the open fibre \(V_x\). Thus the support satisfies (T28).

Conversely, trivialize \(E\) near \(x\), equip it with a Euclidean norm and put \(C=C_M(Z)\). Its unit fibre \(C_x\cap S\) is compact. If it is nonempty, (T28) implies

\[
\delta=\min_{v\in C_x,\ \|v\|=1}\langle v,\xi\rangle>0.
\tag{T30}
\]

After shrinking the base to \(B\), every \(v\in C_b\) of norm one pairs with the constant representative of \(\xi\) by more than \(\delta/2\). Otherwise a sequence \(b_n\to x\) and compactness of the unit sphere would produce a limit direction in \(C_x\) with pairing at most \(\delta/2\), contradicting (T30). Choose a convex ball around \(\xi\) of radius less than \(\delta/4\), and saturate it by positive scaling. Over \(B\) this is an open convex conic neighborhood \(V\) whose polar contains \(C|_B\). This construction can be made inside any previously prescribed conic neighborhood of \(\xi\), by shrinking both the base and the ball.

If \(C_x\cap S\) is empty, the same compact-sphere argument gives a base neighborhood \(B\) on which \(C_b\cap S\) is empty. Take the whole dual bundle over \(B\), or any smaller prescribed open convex conic neighborhood. This includes \(\xi=0\); there is no division by \(\|\xi\|\). Rank zero also belongs to this case. We have proved cofinality of strict support germs with the supports in (T27), including refinement within an already specified conic neighborhood.

There is one remaining neighborhood parameter to check. For a fixed strict support germ and any prescribed ordinary neighborhood \(N\) of \(x\), choose the preceding \(B\) inside \(M\cap N\). A smaller ambient open inside \(N\) can be chosen with intersection \(B\) with \(M\); it is an allowable \(U\) in (T27). The resulting section colimit is therefore exactly the stalk of \(R\Gamma_ZF\). For finitely many supports or representatives first shrink to a common domain and take their union; the finite-union property of normal cones preserves (T28). This provides common refinements for the arrows as well as the objects. Exact filtered colimits and the naturality specified in (T26) and (T23) now prove (T29) with its actual support maps.

## Closed convex wedges for the diagonal {#diagonal-strict-support-wedges}

The geometric replacement of a strict support by a cone correspondence is also elementary. In a local normal chart \((u,b)\), where \(M=\{u=0\}\), suppose the unit fibre in (T30) is nonempty. Define

\[
\Gamma=\{u:\langle u,\xi\rangle\ge(\delta/2)\|u\|\}.
\tag{T31}
\]

This is a closed convex cone, and its nonzero vectors pair strictly positively with \(\xi\); in particular it contains no line. The unit directions of \(C_M(Z)_x\) lie in its interior. The support is contained in \(\{(u,b):u\in\Gamma\}\) near \(x\). If not, choose offending points tending to \(x\), normalize their nonzero \(u\)-coordinates, and pass to a unit-sphere subsequence. The normal-cone sequence criterion puts the limit in \(C_M(Z)_x\), whereas the failed inequalities put its pairing at most \(\delta/2\), contradicting (T30). If the unit fibre is empty, the same normalization argument shows that the support germ is contained in \(M\), and \(\Gamma=\{0\}\) suffices.

For the diagonal of a coordinate vector space, take \(u=x-y\) and identify the conormal by its first covector. Put \(\gamma=-\Gamma\). The containing support is then \(Z_\gamma=\{(x,y):y-x\in\gamma\}\), and \(\gamma\setminus\{0\}\) pairs strictly negatively with that first covector. Conversely the normal cone of this linear correspondence at the diagonal is exactly \(-\gamma\), so these correspondences satisfy the strict test. Enlarging a given local support to such a correspondence gives a cofinal support system, with actual enlargement maps. To obtain a common refinement for two correspondences, apply the same construction to their union, whose unit directions still have a positive minimum after the sign change. At the zero covector only the zero cone occurs. This supplies the geometric support step in the gamma-stalk calculation; converting its supported Hom complex to the directional projector still requires the actual Hom adjunction and kernel calculation supplied separately.

## The covectors that survive specialization {#specialization-microsupport-estimate}

We give the normal-cone convention explicitly. For a closed conic \(A\subset T^*X\), a point of the normal cone along \(T_M^*X\) has coordinates \((z,\alpha;v,\beta)\) if there are \(t_i>0\) decreasing to zero and

\[
(u_i,z_i;\alpha_i,\zeta_i)\in A,\quad
(z_i,\alpha_i)\longrightarrow(z,\alpha),\quad
u_i/t_i\longrightarrow v,\quad \zeta_i/t_i\longrightarrow\beta.
\tag{N4}
\]

The tangential coordinates on \(T_M^*X\) are \((z,\alpha)\); its normal coordinates in \(T^*X\) are \((u,\zeta)\). The same divided-coordinate construction as (N2), applied to this embedded submanifold, proves that (N4) defines its intrinsic normal bundle and normal cone. We identify this normal bundle with \(T^*E\) by
\((z,\alpha;v,\beta)\leftrightarrow(v,z;\alpha,\beta)\). To check this identification under adapted changes, write the normal transition as \(v'=A(z)v,\ z'=h(z)\). Covectors transform by \(\alpha'=A(z)^{-T}\alpha\) and \(\beta'=Dh(z)^{-T}(\beta-(dA(z)\,v)^T\alpha')\). These are exactly the equations obtained by dividing the ambient tangential covector transformation by the deformation parameter and taking its limit. They are also the cotangent transformation equations for \(\alpha\,dv+\beta\,dz=\alpha'\,dv'+\beta'\,dz'\). Thus the identification agrees on overlaps. With this convention,

\[
\operatorname{SS}(\nu_MF)
\subset C_{T_M^*X}(\operatorname{SS}(F)).
\tag{N5}
\]

To prove it, the smooth-submersion formula on \(t>0\) gives exactly the possible covectors

\[
(v,z,t;\alpha,\beta,\tau)
=(v,z,t;t\xi,\zeta,\langle v,\xi\rangle),
\qquad (tv,z;\xi,\zeta)\in\operatorname{SS}(F).
\tag{N6}
\]

Apply the missing-submanifold trace estimate to the hypersurface \(t=0\), with zero coefficient on the negative chamber. Any \((v,z;\alpha,\beta)\in\operatorname{SS}(\nu_MF)\) has witnesses in (N6) with \(t_i\downarrow0\), \((v_i,z_i;\alpha_i,\beta_i)\to(v,z;\alpha,\beta)\), and \(t_i|\tau_i|\to0\). Conicity of \(\operatorname{SS}(F)\) allows multiplication of its original covector by \(t_i\), giving

\[
(t_iv_i,z_i;\alpha_i,t_i\beta_i)\in\operatorname{SS}(F),
\qquad t_i\tau_i=\langle v_i,\alpha_i\rangle\longrightarrow0.
\tag{N7}
\]

The first membership is exactly the witness (N4); this proves (N5). The second also recovers the Euler-annihilation condition \(\langle v,\alpha\rangle=0\). Arbitrarily large original \(\xi_i\) are allowed. No uniform bound on those covectors, noncharacteristic hypothesis, or involutivity theorem has entered the argument.

Define \(\mu_MF=T_E\nu_MF\). Combining (N5) with the forward Fourier inclusion (C23) shows in particular

\[
\operatorname{supp}(\mu_MF)
\subset T_M^*X\cap\operatorname{SS}(F).
\tag{N8}
\]

Here support means the closure of the union of supports of cohomology sheaves. The defining support tests give \(\operatorname{SS}(A)\cap T_Y^*Y=\operatorname{supp}(A)\) for a complex on \(Y\): a zero covector is absent exactly when the coefficient vanishes on a base neighbourhood. At a point \(p=(z,\alpha)\) in the left side of (N8), take the zero cotangent covector in \(\operatorname{SS}(\mu_MF)\) over \(p\). Its inverse under (C17) is \((v=0,z;\alpha,\beta=0)\). By (N5), (N4) then gives points of \(\operatorname{SS}(F)\) converging to \((0,z;\alpha,0)\). Closedness puts that conormal point in \(\operatorname{SS}(F)\). This argument covers \(\alpha=0\) as well; no angular division is required.

## A sheaf of directional morphisms {#microlocal-hom-estimate}

For bounded \(F,G\) on \(X\), let \(q_1,q_2:X\times X\to X\) be the projections and define

\[
K_{G,F}=R\mathcal Hom(q_2^{-1}G,q_1^!F),\qquad
\mu hom(G,F)=\mu_\Delta K_{G,F}.
\tag{M1}
\]

Identify \(T_\Delta^*(X\times X)\) with \(T^*X\) by \((x,x;\xi,-\xi)\leftrightarrow(x;\xi)\). The rectangle calculation (H2) and its amplitude argument put \(K_{G,F}\) in \(D^+\), even for an arbitrary commutative ring and arbitrary stalk modules. Its external-Hom estimate and (N8) yield

\[
\operatorname{supp}\mu hom(G,F)
\subset\operatorname{SS}(G)\cap\operatorname{SS}(F).
\tag{M2}
\]

We also need the stronger estimate on its own microsupport. For closed subsets \(A,B\) of a smooth manifold, let \(C_p(A,B)\) consist of limits \((a_i-b_i)/t_i\) in local coordinates, where \(a_i\in A\), \(b_i\in B\), both approach \(p\), and \(t_i\downarrow0\). The coordinate independence follows from integrating the derivative along the segment from \(b_i\) to \(a_i\): if their divided difference has a finite limit, the divided error tends to zero. On \(T^*X\), use

\[
\omega=\sum_jd\xi_j\wedge dx_j,\qquad
H(a\,dx+b\,d\xi)=b\,\partial_x-a\,\partial_\xi.
\tag{M3}
\]

Thus \(\iota_{H\theta}\omega=-\theta\). We claim

\[
-H\bigl(\operatorname{SS}(\mu hom(G,F))\bigr)
\subset C(\operatorname{SS}(F),\operatorname{SS}(G)).
\tag{M4}
\]

In diagonal coordinates \(u=x-y,\ z=y\), an external-Hom covector \((\xi,-\eta)\) becomes \((\alpha,\beta)=(\xi,\xi-\eta)\). A normal-cone witness therefore has

\[
v=(x_i-y_i)/t_i\longrightarrow v_0,\qquad
\beta=(\xi_i-\eta_i)/t_i\longrightarrow\beta_0,
\qquad (x_i,\xi_i)\in\operatorname{SS}(F),\quad
(y_i,\eta_i)\in\operatorname{SS}(G).
\tag{M5}
\]

Both cotangent points converge to the same \(p\). Fourier exchange sends the limiting normal point to \(\beta_0\,dz-v_0\,d\xi\) over \(p\). Applying \(-H\) gives \((v_0,\beta_0)\), precisely the secant of the two original cotangent points. The forward inclusion (C23), (N5), and the external-Hom bound prove (M4). The order of the two sets and the minus sign are fixed by this computation, even when \(F=G\) makes the two-set cone symmetric.

## The actual identity class and the cutoff counit {#microlocal-identity-detection}

Work in a coordinate vector space \(V\) near \(x_0\), and fix \(p=(x_0,\xi_0)\). Write \(G_U\) for extension by zero from an open \(U\subset V\). The strict normal-support formula (T29) gives

\[
H^r\bigl(\mu hom(G,F)\bigr)_p
\simeq\operatorname*{colim}_{U,\gamma}
H^rR\operatorname{Hom}_U((P_\gamma G_U)|_U,F|_U),
\quad
\gamma\setminus\{0\}\subset\{w:\langle w,\xi_0\rangle<0\}.
\tag{M6}
\]

Here \(U\) runs through relatively compact neighbourhoods of \(x_0\), \(\gamma\) runs through closed convex cones with no line, and \(P_\gamma=q_\gamma^{-1}Rq_{\gamma*}\) is the directional projector. The zero cone is allowed. It is the only cone when \(\xi_0=0\).

We verify the formula and its maps. In normal coordinate \(x-y\), the supports \(Z_\gamma=\{y-x\in\gamma\}\) are cofinal among the local closed supports in (T29). Indeed the unit directions of an admissible normal cone at the base point form a compact subset of the strict positive \(\xi_0\)-halfspace. A slightly larger circular closed convex cone still lies strictly in that halfspace. If no sufficiently small product neighbourhood made the original support lie in this wedge, normalize a sequence of offending differences \(x_i-y_i\). A unit subsequential limit would be an offending normal direction, a contradiction. Negating the normal difference gives the displayed negative condition on \(\gamma\). If the unit-normal set is empty, the same argument shows that the support is locally contained in the diagonal; at \(\xi_0=0\) this is precisely the permitted case. Taking unions of two compact angular sets and then a slightly larger circular cone supplies common support refinements.

Thus the initial complex for the stalk system is \(R\Gamma_{Z_\gamma}(U\times W;K_{G,F})\). Move the closed support to the first internal-Hom argument and use exceptional projection adjunction. The actual comparison is

\[
\begin{aligned}
R\Gamma_{Z_\gamma}(U\times W;K_{G,F})
&\simeq R\operatorname{Hom}_U\!\left(
\left.Rq_{1!}(q_2^{-1}G_W)_{Z_\gamma}\right|_U,F|_U\right)\\
&\simeq R\operatorname{Hom}_U((P_\gamma G_W)|_U,F|_U).
\end{aligned}
\tag{M7}
\]

The first equality also uses open-extension adjunction in the second coordinate. Choose \(W\) relatively compact. The closed support of the kernel is contained in \(V\times\overline W\), so its projection to the first factor is proper: over a compact set it is a closed subset of a compact product. Hence its shriek image equals its ordinary image. The ordinary-space kernel calculation, including its actual comparison map, identifies that image with \(P_\gamma G_W\). The compact-localized kernel is bounded, and the finite proper-image cohomological-dimension bound makes this projector output bounded as well. Its use as the first Hom input is therefore within the established bounded-input range. No equality of ordinary and shriek images is asserted for unlocalized \(G\). Replacing \(U,W\) by \(U\cap W\) is cofinal, proving (M6).

At the zero cone, the diagonal kernel gives \(P_0G_U=G_U\). For \(G=F\), the identity of \(F|_U\) therefore determines a class in degree zero of the stalk in (M6). Enlarging the support from the diagonal to \(Z_\gamma\) reverses the first-Hom argument: the map \(k_{Z_\gamma}\to k_\Delta\) becomes the projector counit. After open adjunction, this class is represented by the actual arrow

\[
Q_{U,\gamma}=(P_\gamma F_U)_U\longrightarrow F.
\tag{M8}
\]

Neighbourhood restriction gives the same arrows after passing to smaller \(U\), because all comparisons in (M7) use restriction, proper-support adjunction and the fixed kernel counit. This verifies the transition maps of the identity class, rather than assigning an abstract name to it.

If \((\mu hom(F,F))_p=0\), exactness of filtered colimits says that this identity class becomes zero at one refined pair \((U,\gamma)\). Thus (M8) is zero as a derived morphism. The cone of the counit \(P_\gamma F_U\to F_U\) is killed by \(Rq_{\gamma*}\), since its unit is an isomorphism and the adjunction triangle identity identifies the induced map with that isomorphism's inverse. The cone test consequently excludes \(p\) from this cone's microsupport: \(\xi_0\) lies in the interior of the negative polar when it is nonzero. For \(\gamma=0\), the cone is zero directly. Restricting to \(U\) and extending again does not change its germ near \(x_0\). But the cone of the zero map (M8) is \(F\oplus Q_{U,\gamma}[1]\), so its microsupport contains \(\operatorname{SS}(F)\) there. We have proved

\[
(\mu hom(F,F))_p=0\quad\Longrightarrow\quad p\notin\operatorname{SS}(F).
\tag{M9}
\]

This uses no finite-rank description of Hom, no interchange of Hom and a filtered colimit, and no theorem identifying morphisms in a localized category.

## An empty cone and a zero stalk {#empty-cone-zero-stalk}

Let \(A\in D^+(k_W)\) on a neighbourhood of zero in \(\mathbb R_t\times\mathbb R_y^{m-1}\). Suppose, for some \(b>0\), that

\[
A|_{W\cap\{t>b|y|\}}=0,\qquad
\operatorname{SS}(A)\cap T_0^*W\subset\{\tau=0\}.
\tag{I1}
\]

Then \(A_0=0\). Choose \(a>b\) and set

\[
C=\{t\ge a|y|\},\qquad
C^{\circ a}=\{\tau\le0,\ |\eta|\le-a\tau\}.
\tag{I2}
\]

Every nonzero covector in this negative polar has \(\tau<0\). Its unit section is compact. Closedness of microsupport and (I1) therefore give a common neighbourhood \(W_1\) of zero avoiding all those nonzero covectors: otherwise normalize a sequence over points tending to zero and take a convergent subsequence in that compact unit section.

Put

\[
O_0=\{t>b|y|\},\qquad
O_{1,\epsilon}=O_0\cup\bigl(-\epsilon e_t+\operatorname{Int}C\bigr).
\tag{I3}
\]

Both opens are invariant under addition by \(C\), and \(0\in O_{1,\epsilon}\). Points in the closure of the difference satisfy

\[
-\epsilon+a|y|\le t\le b|y|,
\qquad |y|\le\epsilon/(a-b),\qquad |t|\le\epsilon+b\epsilon/(a-b).
\tag{I4}
\]

For each \(x\in O_{1,\epsilon}\), the set \((x+C)\setminus O_0\) is closed and lies in this bounded cap, hence compact. For small \(\epsilon\), all caps lie in \(W_1\). Apply prescribed-cone propagation to obtain the actual restriction isomorphism

\[
R\Gamma(O_{1,\epsilon}\cap W;A)
\xrightarrow{\sim}R\Gamma(O_0\cap W;A)=0.
\tag{I5}
\]

To apply the vector-space statement literally, use \(Rj_*A\) for the open inclusion \(j:W\hookrightarrow\mathbb R^m\). Its ordinary sections are the displayed sections and its microsupport agrees with that of \(A\) on \(W_1\). All geometric changes occur in the caps inside \(W_1\).

Set \(Z=W\setminus O_0\). As \(A\) vanishes outside \(Z\), ordinary closed extension identifies \(A=i_*i^{-1}A\). The relative open neighbourhoods \(O_{1,\epsilon}\cap Z\) form a basis at zero in \(Z\), by (I4). Taking filtered colimits of cohomology in (I5) computes the stalk of \(i^{-1}A\), and all its groups vanish. This proves the claim, without a nonproper fibre substitution.

## Involutivity of the entire microsupport {#microsupport-involutivity}

For a closed set \(S\) in a symplectic manifold, its point cone \(C_p(S)\) consists of limits \((s_i-p)/t_i\) with \(s_i\in S\) and \(t_i\downarrow0\). In the convention (M3), involutivity means

\[
\theta|_{C_p(S,S)}=0\quad\Longrightarrow\quad
-H\theta\in C_p(S),\qquad p\in S.
\tag{I6}
\]

Both signs follow by replacing \(\theta\) with \(-\theta\). For every bounded complex \(F\) of sheaves of modules over an arbitrary commutative ring, \(S=\operatorname{SS}(F)\) satisfies (I6).

Suppose \(v=H\theta\notin C_p(S)\), for a covector annihilating \(C_p(S,S)\). Then \(v\ne0\). Choose local coordinates on \(T^*X\) in which \(p=0\) and \(v=\partial_t\). Since the point cone is closed, some open angular cone around \(v\) contains no directions of \(S-p\) near zero. Otherwise normalize such directions, pass to a subsequence approaching that angular axis, and divide their points by their norms to put \(v\), after positive scaling, in \(C_p(S)\). Shrinking the angular cone and the base neighbourhood, we obtain \(b>0\) with \(S\cap\{t>b|y|\}=\varnothing\) there.

Take \(A=\mu hom(F,F)\). It belongs to \(D^+\), and (M2) makes it zero on this open cone. For any \(\alpha\in\operatorname{SS}(A)\) over \(p\), (M4) and the annihilation hypothesis imply

\[
0=\langle-H\alpha,\theta\rangle
=\langle\alpha,H\theta\rangle
=\langle\alpha,\partial_t\rangle.
\tag{I7}
\]

Thus (I1) holds. The empty-cone lemma gives \(A_p=0\), and (M9) contradicts \(p\in S\). This proves involutivity at every point, including singular points and the zero section. In dimension zero the tangent and cotangent spaces are zero and the assertion is immediate.

Combining (I6) with the already proved Hamiltonian invariance argument, a \(C^2\) function vanishing on \(\operatorname{SS}(F)\) has Hamiltonian trajectories that remain in that closed set as long as they stay in its domain. No subanalyticity or constructibility assumption is used for the involutivity theorem. The later recovery of Lagrangian strata inside a subanalytic isotropic containing set continues to require the explicitly stated subanalytic foundations in that separate lesson.

## Four checks on specialization and involutivity {#microlocal-worked-checks}

### A constant coefficient and a coefficient on the submanifold

Take \(X=\mathbb R^r_u\times\mathbb R^s_z\), \(M=\{u=0\}\), and the standard orientation of the normal \(r\)-space. Compute \(\nu_M\) and \(\mu_M\) on \(k_X\) and on the closed-extension sheaf \(k_M\).

**Solution.** On \(t>0\), the inverse image of \(k_X\) is constant. Ordinary sections on a small positive interval give \(k\), by interval contraction, so \(\nu_Mk_X=k_E\). For \(k_M\), the positive inverse image is the constant coefficient on \(v=0\). Closed extension commutes with its ordinary image; the same interval unit gives \(\nu_Mk_M=k_{0_E}\), with no shift. The Fourier kernel of \(k_{0_E}\) integrates over the single point \(v=0\), where its inequality is automatic. Hence \(\mu_Mk_M=k_{E^*}\). For the constant coefficient on \(E\), a nonzero dual vector cuts out a closed halfspace, whose compact cohomology is zero by (C14). At a zero dual vector the whole oriented \(r\)-space contributes \(k[-r]\). Proper-support base change and closed localization identify \(\mu_Mk_X=k_{0_{E^*}}[-r]\). On an unoriented normal bundle the corresponding normal orientation line accompanies this shift. For \(r=0\), all four constructions are identities, as the formulas require.

### A support condition is relative to its base

Take the rank-zero case \(X=M=\mathbb R\), \(F=k_X\), \(k\ne0\), and the open conic set \(V=(0,1)\) in the rank-zero dual bundle. Explain why the base restriction in the polar formula matters.

**Solution.** The deformation and Fourier functors are identities, so \(H^0(V;\mu_MF)=k\). Over the base \(B=(0,1)\), the full zero normal bundle is an allowable polar support. In the ambient open \(O=(0,1)\), take \(U=Z=O\); its supported degree-zero sections are \(k\). If one incorrectly demanded a globally closed \(Z\subset\mathbb R\) with \(C_M(Z)\subset V\), rank zero would force \(Z\subset(0,1)\). Every such \(Z\) is a proper subset of the connected interval. A constant section supported there is zero, so that incorrect system would give zero in degree zero. Closing a support in a larger ambient space is harmless only when the normal condition is checked over the specified open base.

### Why the zero cone must remain available

At \(p=(x_0,0)\), identify the allowed cones in (M6) and explain what it means for the identity class to vanish.

**Solution.** No nonzero vector can pair strictly negatively with the zero covector. Therefore \(\gamma=\{0\}\) is the only cone, and its projector is the identity. The class is represented by \(\mathrm{id}_{F|_U}\). It vanishes in the filtered colimit precisely when its restriction becomes the zero derived morphism on some smaller neighbourhood. An object's identity is zero exactly when the object is zero, so \(F\) vanishes on that neighbourhood. This is the zero-section condition \(p\notin\operatorname{SS}(F)\). Merely knowing that the ordinary stalk \(F_{x_0}\) is zero would not suffice: the infinite-point example above has that property and still fails to vanish on every neighbourhood.

### A truncated zero section cannot be a whole microsupport

In \(T^*\mathbb R\), consider \(S=\{(x,0):x\ge0\}\). Check (I6) at the origin and compare the result with the constant sheaf on the closed half-line.

**Solution.** The point cone of \(S\) at zero is the nonnegative horizontal ray, but \(C_0(S,S)\) is the entire horizontal line: differences of two nonnegative points have either sign. The covector \(\theta=d\xi\) annihilates this line, while \(-H\theta=-\partial_x\) is absent from the point cone. Thus \(S\) fails involutivity and cannot be the full microsupport of a bounded sheaf. Indeed the support tests for \(k_{[0,\infty)}\) give the horizontal ray together with the positive cotangent ray over \(x=0\). The added conormal ray is essential. At their common origin, the two-set cone contains two independent directions, so its annihilator is zero and the preceding obstruction disappears. This check uses the two-set cone, not just the tangent cone of one smooth branch.

## Sources and scope {#sources-and-scope}

Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), treat external Hom, specialization, Fourier transport, microlocal Hom and involutivity. An [author-hosted edition](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) is also available.

The proof here passes from neighborhood gluing and explicit kernel comparisons to the directional identity and an empty-cone contradiction. The coefficient ring is arbitrary. The external-Hom inputs and final complex are bounded; the resulting Hom, specialization and Fourier complexes are treated in the bounded-below category. This proves involutivity for the bounded complexes stated above, including singular and zero-covector points.

The forward Fourier estimate used here does not assert its reverse, Fourier inversion, or equivalence of orbitwise and coherent-action definitions of conicity. General supported specialization uses the stated tubular-neighborhood geometry; the local diagonal argument uses product charts. Compatible subanalytic stratification, compact finiteness, biduality and broader unbounded extensions are separate results, not consequences of the involutivity proof.
