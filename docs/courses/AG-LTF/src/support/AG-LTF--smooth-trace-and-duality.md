# Smooth traces, duality and Gysin maps

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex Ultra, October 2026. Original explanatory text is CC0. The local-duality argument adapts the earlier CC0 exposition “Poincaré duality for smooth varieties” by the same stated writing model; the higher-dimensional trace is constructed here, and the divisor orientation is corrected through the supported Kummer class. Human mathematical sources are credited below. Independent human review is not claimed.*

A trace in top compact cohomology is more than a list of degrees on fibres: its local definitions must agree when coordinates change. We first construct the curve map as an actual morphism of sheaves, then connect smooth coordinate systems while retaining smooth one-dimensional projections. Compact-support adjunction turns the resulting trace into smooth duality. The same adjunction gives purity and Gysin maps with a positive Kummer normalization.

Let \(\Lambda=\mathbf Z/n\), with \(n\) invertible on every scheme considered, and put \(\Lambda(1)=\mu_n\). The case \(n=1\) is zero. Complexes have cohomological grading, so \(H^r(A[s])=H^{r+s}(A)\). In the relative theorem \(f:X\to S\) is separated, smooth of finite presentation, and purely of relative dimension \(d\), with \(S\) quasi-compact and quasi-separated. In the absolute theorem \(X/k\) is separated, smooth and finite type of pure dimension \(N\), with \(k\) algebraically closed. Neither finite local systems nor the coefficient ring are assumed to be vector spaces.

We use these exact preceding geometric results:

- [Pushforward, pullback and finite morphisms](course:ag-etale-cohomology/pushforward-pullback-and-finite-morphisms), §§3–4: finite strict-local decomposition, geometric stalks, exact finite pushforward and finite-data continuity. Its expressly stated cohomological continuity on affine inverse limits is retained as a foundation.
- [Constructible sheaves and extension by zero](course:ag-etale-cohomology/constructible-sheaves-and-extension-by-zero): the constructible Serre category and descent of finite presentations.
- [Cohomology with compact support](course:ag-etale-cohomology/cohomology-with-compact-support), §§5,7–12: composition, arbitrary base change, arbitrary-complex projection formula, sums, localization and the relative bound \([0,2d]\). Its expressly stated general constructibility and compact finiteness premises are retained; they are not silently proved anew here.
- [Smooth base change and local acyclicity](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity), Theorem 9.1: universal local acyclicity of smooth maps, including the strict-local fibre calculation used in §5.
- [Cohomological dimension and the Künneth formula](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula): derived Künneth.
- [Poincaré duality for curves](course:ag-etale-cohomology/poincare-duality-for-curves), §§2–11: degree trace, exact duality over \(\mathbf Z/n\), self-injectivity of these coefficients, and the compatibility of finite transfer and open extension with cup product.

Brown representability for derived categories of Grothendieck abelian categories is the categorical foundation used in §8 to construct a right adjoint. No smooth duality, purity, higher-dimensional trace or flat-family trace is assumed among the geometric inputs.

## 1. The trace of a smooth relative curve

Let \(S\) be quasi-compact and quasi-separated, let \(n\geq2\) be invertible on \(S\), and put \(\Lambda=\mathbf Z/n\) and \(\Lambda(1)=\mu_n\). Let

\[
h:X\longrightarrow S
\]

be separated, smooth, and of finite presentation, with every nonempty geometric fibre purely of dimension one. Empty fibres are permitted. The case \(n=1\) has zero coefficients and the unique zero trace. All sheaves are on the small étale site. The separated finite-type compact-support formalism over quasi-compact quasi-separated schemes is used with its canonical composition, arbitrary-base-change, projection, and open-extension maps. Its construction is the published provider the compact-support chapter identified in the source map below.

**Theorem RC.1.** There is a canonical morphism of sheaves

\[
\operatorname{Tr}_h:R^2h_!\mu_n\longrightarrow\Lambda_S.
\tag{RC.1}
\]

At a geometric point \(\bar s\), proper/compact base change identifies its stalk with the sum of the degree/Kummer traces on the connected components of the smooth curve \(X_{\bar s}\). The morphism commutes with every change of base within the compact-support formalism. If \(e:Y\to X\) is separated, étale, and of finite presentation, then

\[
\operatorname{Tr}_{he}
=\operatorname{Tr}_h\circ R^2h_!(\operatorname{tr}_e),
\qquad
\operatorname{tr}_e:e_!e^*\mu_n\longrightarrow\mu_n,
\tag{RC.2}
\]

under canonical composition. The same identity holds for a separated quasi-finite flat map of finite presentation between smooth relative curves, with the weighted trace constructed below. If all geometric fibres of \(h\) are nonempty and connected, (RC.1) is an isomorphism.

The proof constructs actual maps on coordinate neighborhoods and descends them. A specified collection of fibre homomorphisms is used to compare existing maps; it is not taken to be a sheaf morphism by itself.

### 1.1. Degree orientation over an algebraically closed field

Let \(k\) be algebraically closed with \(n\) invertible in \(k\). A connected smooth curve \(C\) of finite type has a smooth projective completion \(\overline C\). Its boundary is finite. Open localization and vanishing of positive cohomology on a finite scheme give a canonical isomorphism

\[
H^2_c(C,\mu_n)\xrightarrow{\sim}H^2(\overline C,\mu_n).
\tag{RC.3}
\]

Kummer, the vanishing of the Brauer group of a smooth projective curve over \(k\), and divisibility by \(n\) of \(\operatorname{Pic}^0(\overline C)\) give

\[
H^2(\overline C,\mu_n)
\simeq \operatorname{Pic}(\overline C)/n
\xrightarrow[\deg]{\sim}\Lambda.
\tag{RC.4}
\]

These inputs and this calculation are proved in the curve-duality chapter, §2, using its explicitly named preceding providers the multiplicative-group, Jacobian, proper-base-change and compact-support chapters. This is only the curve-duality chapter's degree trace, before its duality argument. Define \(\tau_C\) as (RC.3) followed by (RC.4), and define \(\tau_C\) for a disconnected smooth curve as the sum over its finitely many connected components. The trace on the empty curve is zero.

A nonempty open of a connected smooth curve has the same smooth projective completion. Consequently open extension

\[
H^2_c(V,\mu_n)\longrightarrow H^2_c(C,\mu_n)
\tag{RC.5}
\]

preserves trace. For an arbitrary open, the same assertion follows component by component, with zero from omitted components. A divisor of one point on a connected completion has trace \(+1\). This fixes the sign without a choice of a primitive root of unity.

### 1.2. Finite and quasi-finite weighted traces

The following zero-dimensional construction is included to specify precisely what is meant by the trace on sheets and by a branch weight. It does not assume (RC.1).

**Lemma RC.2.** If \(q:Z\to T\) is separated, quasi-finite, flat, and of finite presentation, and \(n\) is invertible on \(T\), there is a morphism

\[
\operatorname{tr}_q:q_!q^*\mu_n\longrightarrow\mu_n.
\tag{RC.6}
\]

Under the geometric-stalk formula for \(q_!\), its value at \(\bar t:\operatorname{Spec}\Omega\to T\) is

\[
(a_z)_{z\in |Z_{\bar t}|}\longmapsto
\sum_z m_z a_z,
\qquad
m_z=\dim_\Omega\mathcal O_{Z_{\bar t},z}.
\tag{RC.7}
\]

The stalk is a sum, with finite support. The trace commutes with arbitrary base change and composition. If \(q\) is étale, every \(m_z=1\); (RC.6) is the usual counit \(q_!q^*\to\mathrm{id}\), summing its sheets. An open immersion has the canonical extension map.

**Proof.** First suppose \(q\) finite locally free. For a finite locally free algebra \(B/A\), the determinant of multiplication defines

\[
N_{B/A}:B^*\longrightarrow A^*,\qquad
b\longmapsto\det_A(m_b).
\tag{RC.8}
\]

It is multiplicative and commutes with arbitrary ring base change, since multiplication, exterior powers, and the determinant commute with base change. Thus it defines a norm of unit sheaves. The norm commutes with \(n\)-th powers and therefore restricts to a map \(q_*q^*\mu_n\to\mu_n\).

Over the strict localization of \(T\) at \(\bar t\), the finite algebra is the product of its strictly local factors (the finite-morphism chapter, Lemma 3.2 and Theorem 3.3). Each factor \(B_z\) is finite free over the strictly local base and has rank \(m_z\), as seen by its geometric closed fibre. The invertible locally constant sheaf \(\mu_n\) has constant sections on such a connected factor. A scalar root of unity \(a_z\) has determinant norm \(a_z^{m_z}\). Products of these norms give (RC.7), in additive notation. In particular the branch weight is the whole local fibre length, including a nonreduced branch, and the unit followed by trace for a finite map of constant rank \(r\) is multiplication by \(r\).

Here is an actual local construction for a general \(q\); assigning (RC.7) to stalks alone would omit this step. Work on an affine target neighborhood and use the finite compactification supplied by relative Zariski's main theorem, as in the compact-support chapter, §7:

\[
Z\hookrightarrow\overline Z\longrightarrow T,
\qquad \overline Z/T\text{ finite}.
\tag{RC.9}
\]

After strict localization at \(\bar t\), split this finite scheme into its local factors. A factor whose closed point belongs to the open \(Z\) lies entirely in \(Z\): an open containing the closed point of a local scheme is the whole scheme. The other factors contribute an open part with empty closed fibre. The finitely many idempotents effecting this splitting descend to an étale neighborhood \(V\) of \(\bar t\); this is the ordinary filtered-colimit descent of elements and their finitely many idempotent equations. For the selected factors, the complement of \(Z_V\) has closed image in \(V\), since those factors are finite. Shrinking \(V\) removes that image. We obtain

\[
Z_V=Z_0\amalg Z_1\amalg\cdots\amalg Z_r,
\tag{RC.10}
\]

where each \(Z_i/V\), \(i>0\), is finite locally free and \((Z_0)_{\bar t}\) is empty. Flatness and finite presentation of \(q\) ensure finite local freeness on the selected factors.

For a section \(s\in(q_!q^*\mu_n)(V)\), its support is proper over \(V\) by the definition of \(q_!\). Its part in \(Z_0\) also has proper support: \(Z_0\) is clopen. The image of that support is closed and misses \(\bar t\). On the target open obtained by deleting this image, \(s\) has contributions only in the finite locally free factors. Apply their determinant norms and multiply the resulting roots of unity. This gives an actual target section near \(\bar t\), with every stalk equal to (RC.7). These sections agree on overlaps by stalk detection, hence glue; restriction and addition are respected. This constructs (RC.6).

This construction also proves arbitrary-base-change compatibility: proper supports pull back, the finite decompositions pull back, and determinant norm commutes with base change. Equivalently the two existing maps have the same formula (RC.7) on every geometric stalk, using the canonical base-change identification for \(q_!\) from the compact-support chapter, Lemma 2.2.

For composition \(Z\xrightarrow q T\xrightarrow r U\), one can check the two existing traces at a geometric point of \(U\). A local factor of the fibre of \(T\) is an Artinian \(\Omega\)-algebra \(A\), of length \(a\). A corresponding finite flat local factor of \(Z\) is free of rank \(b\) over \(A\), and has \(\Omega\)-length \(ab\). Thus the weights in the composite sum are products of the two weights. The finite decompositions just constructed justify reduction to these factors. Reindexing the finite sums proves composition. For étale maps all fibre lengths are one. Their canonical extension/sheet-sum counit has these same stalks, hence equals (RC.6). \(\square\)

Tensoring (RC.6) by \(\mu_n^{-1}\), and using the finite-support projection isomorphism

\[
q_!\Lambda\otimes_\Lambda F\simeq q_!q^*F
\tag{RC.11}
\]

for a \(\Lambda\)-sheaf \(F\) on \(T\), gives \(\operatorname{tr}_q:q_!q^*F\to F\). The projection isomorphism is the canonical one and is an isomorphism on stalks, where it is the distributivity of tensor over the finite-support sum. Its formula is again (RC.7); it is functorial in \(F\).

**Lemma RC.3 (finite curve norm).** If \(v:C\to D\) is finite between smooth curves over an algebraically closed field, then

\[
\tau_D\circ H^2_c(\operatorname{tr}_v)=\tau_C.
\tag{RC.12}
\]

**Proof.** First take connected smooth projective curves. A finite nonconstant map is flat: its finite algebra over any target discrete valuation ring is torsion free, hence free. Apply the exact finite direct-image functor to Kummer; its exactness is the finite-morphism chapter, Theorem 4.1. The norm (RC.8) gives the commutative diagram

\[
\begin{array}{ccccccccc}
1&\to&v_*\mu_n&\to&v_*\mathbf G_m&\xrightarrow{n}&v_*\mathbf G_m&\to&1\\
&&\downarrow\operatorname{tr}_v&&\downarrow N&&\downarrow N\\
1&\to&\mu_n&\to&\mathbf G_m&\xrightarrow{n}&\mathbf G_m&\to&1.
\end{array}
\tag{RC.13}
\]

Naturality of the connecting maps identifies \(H^2(\operatorname{tr}_v)\), under (RC.4), with norm on \(\operatorname{Pic}/n\). The norm of a line bundle can be written

\[
N(L)=\det(v_*L)\otimes\det(v_*\mathcal O_C)^{-1}.
\tag{RC.14}
\]

We check the degree assertion rather than infer it from the sheaf's branch weights. Over the target discrete valuation ring, the valuation of the determinant norm of a nonzero integral function \(b\) is the length of the quotient of the finite free lattice by multiplication by \(b\). Decomposing the quotient into its source branches shows

\[
\operatorname{ord}_y N(b)
=\sum_{x\mid y}[k(x):k(y)]\operatorname{ord}_x(b).
\tag{RC.15}
\]

For a rational function, subtract the formulas for a numerator and denominator. Applying the same lattice calculation to a divisor line bundle in (RC.14) gives

\[
N\bigl(\mathcal O_C(\textstyle\sum_x d_x[x])\bigr)
=\mathcal O_D\bigl(\textstyle\sum_x d_x[k(x):k(vx)][vx]\bigr).
\tag{RC.16}
\]

All residue degrees are one over the algebraically closed field. Thus norm preserves divisor degree, and (RC.13) proves (RC.12) for projective curves. This proof works even for an inseparable finite map; in the application below the map is generically étale. In (RC.7) the sheaf trace weights a root on a ramified branch by its local fibre length. In (RC.16) the norm pushes a source point divisor with its residue degree. These two compatible norm calculations concern different objects and do not replace one another.

A finite map of open smooth curves extends to a finite map of their smooth projective completions. Its inverse image of the target open is exactly the source open, by the valuative criterion for the given finite map. The completion square is therefore cartesian. Finite base change, open extension, and the norm map commute in this square: on every target stalk, retained source branches contribute their norms and omitted branches contribute zero in additive notation. Applying compact cohomology transports the projective identity to (RC.12). For disconnected curves apply the connected proof to each component and add. \(\square\)

**Corollary RC.4.** If \(u:C\to D\) is separated and quasi-finite flat between smooth curves over an algebraically closed field, then

\[
\tau_D\circ H^2_c(\operatorname{tr}_u)=\tau_C.
\tag{RC.17}
\]

Indeed each nonempty connected source component has a nonconstant function-field map to a target component. It extends to a finite map of smooth projective completions. If \(C'\) is the inverse image of \(D\) in the source completion, \(u\) factors as the open \(C\hookrightarrow C'\) followed by the finite map \(C'\to D\). Lemma RC.2 identifies \(\operatorname{tr}_u\) with the composite of open extension and the weighted finite trace. Equation (RC.5) and Lemma RC.3 give (RC.17). This proves the particular compatibility for an étale chart \(C\to\mathbf A^1_k\).

### 1.3. The actual relative map for the affine line

Write \(p:\mathbf P^1_S\to S\), \(a:\mathbf A^1_S\to S\), and \(j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S\). On each étale \(V\to S\), the Kummer class

\[
c_1^{(n)}\bigl(\mathcal O_{\mathbf P^1_V}(1)\bigr)
\in H^2(\mathbf P^1_V,\mu_n)
\]

is compatible with restriction. Multiples of this class define a sheaf morphism

\[
\kappa:\Lambda_S\longrightarrow R^2p_*\mu_n.
\tag{RC.18}
\]

Proper base change and (RC.4) show that each geometric stalk of \(\kappa\) is the degree-one generator, so \(\kappa\) is an isomorphism. Put \(\operatorname{Tr}_p=\kappa^{-1}\). This is already an actual sheaf map.

The complement \(i:S\hookrightarrow\mathbf P^1_S\) is the infinity section, with \(pi=\mathrm{id}_S\). Localization gives

\[
R^1(pi)_*\mu_n\longrightarrow R^2a_!\mu_n
\xrightarrow{j_!}R^2p_*\mu_n
\longrightarrow R^2(pi)_*\mu_n.
\]

Both outer terms vanish, since \(pi\) is the identity. Define

\[
\operatorname{Tr}_a:
R^2a_!\mu_n\xrightarrow[ j_!]{\sim}R^2p_*\mu_n
\xrightarrow{\kappa^{-1}}\Lambda_S.
\tag{RC.19}
\]

Kummer's connecting map and \(\mathcal O(1)\) commute with arbitrary base change, as do proper base change and open localization. Hence (RC.19) commutes with every base change. Its geometric fibres are precisely \(\tau_{\mathbf A^1}\).

### 1.4. Coordinate neighborhoods and descent

Every point of \(X\) has a quasi-compact open neighborhood \(U\) with an \(S\)-morphism

\[
u:U\longrightarrow\mathbf A^1_S
\tag{RC.20}
\]

which is étale. One can see this directly from a standard smooth presentation: choose one of its free variables as the coordinate and use the invertible Jacobian determinant in the other variables. Equivalently choose a local function whose relative differential generates the line bundle \(\Omega^1_{X/S}\); the smooth coordinate theorem gives the étale map after shrinking. The base need not be a field or reduced. This is the usual local algebraic structure theorem for smooth morphisms, not a cohomological trace input.

Since \(X/S\) is separated, the chart morphism is separated; its graph is closed in \(U\times_S\mathbf A^1_S\). The quasi-compact charts and their intersections are of finite presentation over \(S\), and the chart is quasi-finite. Its exact lower shriek and genuine sheet-sum trace are Lemma RC.2. By canonical composition define

\[
\theta_u:R^2(h|_U)_!\mu_n
\simeq R^2a_!(u_!u^*\mu_n)
\xrightarrow{R^2a_!\operatorname{tr}_u}R^2a_!\mu_n
\xrightarrow{\operatorname{Tr}_a}\Lambda_S.
\tag{RC.21}
\]

This composition is a morphism of sheaves. The arbitrary-base-change theorem for compact support and Lemma RC.2 identify its geometric stalk with the compact transfer along \(u_{\bar s}\), followed by \(\tau_{\mathbf A^1}\). Corollary RC.4 proves that this stalk equals \(\tau_{U_{\bar s}}\). In particular two coordinate maps on the same open give the same sheaf morphism: the two actual maps have equal geometric stalks. If \(W\subset U\) is a quasi-compact open, restriction of the chart is a chart on \(W\); (RC.5), or Lemma RC.2's composition law, proves

\[
\theta_u\circ R^2(h|_U)_!(\text{open extension from }W)
=\theta_{u|_W}.
\tag{RC.22}
\]

Choose finitely many such opens \(U_i\) covering \(X\). Put \(U_{ij}=U_i\cap U_j\) and let \(j_i,j_{ij}\) denote the open immersions into \(X\). Their intersections are quasi-compact because \(X\) is quasi-separated. On \(X\) the usual open-cover presentation is exact:

\[
\bigoplus_{i,j}(j_{ij})_!\mu_n
\xrightarrow{\text{difference}}
\bigoplus_i(j_i)_!\mu_n
\xrightarrow{\text{sum}}\mu_n\longrightarrow0.
\tag{RC.23}
\]

At a geometric point \(x\) this is the presentation of one copy of \(\mu_{n,x}\) by the copies indexed by the nonempty set of covering opens containing \(x\): differences generate precisely the kernel of summation. Thus (RC.23) is exact without an assumption on the geometry of overlaps.

For every \(\Lambda\)-sheaf \(G\) on \(X\), the compact-support fibre formula and the curve bound give

\[
R^qh_!G=0\quad(q>2).
\tag{RC.24}
\]

Consequently \(R^2h_!\) is right exact. More explicitly, factor (RC.23) through its image \(K\). The two resulting short exact sequences, together with \(R^3h_!\) vanishing on both kernels, give the exact presentation

\[
\bigoplus_{i,j}R^2(h|_{U_{ij}})_!\mu_n
\xrightarrow{\text{difference}}
\bigoplus_i R^2(h|_{U_i})_!\mu_n
\longrightarrow R^2h_!\mu_n\longrightarrow0.
\tag{RC.25}
\]

Here composition with exact open extension identifies the terms. By (RC.22) and coordinate independence on \(U_{ij}\), the sum of the maps \(\theta_{u_i}\) annihilates the first arrow. It therefore descends uniquely through (RC.25) to the actual morphism (RC.1).

At a geometric point of \(S\), (RC.25) remains exact. The absolute trace \(\tau_{X_{\bar s}}\), composed with each open-extension map, is \(\tau_{(U_i)_{\bar s}}\) by (RC.5). Equation (RC.21) has just this stalk. Surjectivity in (RC.25) proves that the descended trace has stalk \(\tau_{X_{\bar s}}\). Any two sheaf maps with those specified stalks are equal. This proves uniqueness and independence of the cover.

### 1.5. Base change, sheet compatibility, and coefficient extension

For \(g:S'\to S\), use the pulled-back cover and coordinates. The maps in (RC.21) commute with base change by the compact-support composition/base-change laws, the base change of the sheet sum, and (RC.19). The sheaf presentations (RC.23) also pull back. Since inverse image on étale sheaves is exact, the two descended maps agree after the surjection in (RC.25). Thus

\[
g^*\operatorname{Tr}_h=\operatorname{Tr}_{h'}
\tag{RC.26}
\]

under \(g^*R^2h_!\mu_n\simeq R^2h'_!\mu_n\). For a base outside the global quasi-compact category the statement is read on quasi-compact quasi-separated target neighborhoods where the same formalism is defined; the local maps agree on overlaps.

If \(e:Y\to X\) is separated, quasi-finite flat, and of finite presentation, and both \(Y/S\) and \(X/S\) are smooth curves, the two sides of (RC.2) are existing sheaf maps. Compact base change and Lemma RC.2 identify their stalks with the two sides of (RC.17) for \(e_{\bar s}\). Hence they are equal. This includes every étale map and every open-extension map needed to change relative coordinates. For an étale map there is no unmentioned ramification factor: each retained sheet has weight one. The finite completions used to prove the fibre identity retain their local-length weights through (RC.13).

If every geometric fibre is nonempty and connected, its degree trace is an isomorphism by (RC.3)-(RC.4). Stalk detection makes (RC.1) an isomorphism. Smoothness ensures that a connected geometric curve has one irreducible component: a regular curve's distinct irreducible components are disjoint.

For any \(\Lambda\)-sheaf \(F\) on \(S\), the canonical derived projection formula and (RC.24) give

\[
R^2h_!\mu_n\otimes_\Lambda F
\xrightarrow{\sim}R^2h_!\bigl(h^*F(1)\bigr).
\tag{RC.27}
\]

Indeed \(Rh_!\mu_n\) has cohomology only in degrees \(0,1,2\), and derived tensor with a sheaf cannot raise the upper cohomological degree. Its degree-two cohomology is its top cohomology tensored ordinarily with \(F\); the lower truncation contributes only degrees at most one. Define the \(F\)-trace by (RC.27) followed by \(\operatorname{Tr}_h\otimes\mathrm{id}_F\). It is functorial in \(F\), commutes with base change, and obeys the same sheet compatibility.

Finally (RC.24) gives \(Rh_!\mu_n[2]\in D^{\leq0}(S,\Lambda)\). Its canonical top-truncation map followed by (RC.1) defines

\[
Rh_!\mu_n[2]\longrightarrow R^2h_!\mu_n
\xrightarrow{\operatorname{Tr}_h}\Lambda_S.
\tag{RC.28}
\]

The étale compatibility of (RC.28) follows by naturality of top truncation and (RC.2). This is a curve trace in the derived category. Its construction has used neither an extraordinary inverse-image identification nor higher-dimensional duality.

## 2. Construction in higher dimension

### 2.1. Scope and the top-degree descent mechanism

Let \(S\) be quasi-compact and quasi-separated, let \(n\) be invertible on \(S\), and put \(\Lambda=\mathbf Z/n\). Let \(f:X\to S\) be separated and smooth of finite presentation, purely of relative dimension \(d\). The case \(n=1\) is the zero category. We construct

\[
\tau_f:R^{2d}f_!\Lambda_X(d)\longrightarrow\Lambda_S.
\tag{ST.1}
\]

The construction is compatible with arbitrary base change, étale maps in the source, composition of smooth maps, and coefficient reduction. It sums components; it does not select one component of a fibre. When \(d=0\), it is the étale summation map.

The compact-support chapter’s dimension bound says \(R^rf_!F=0\) for \(r>2d\), for every torsion sheaf \(F\). Its long exact sequence therefore makes \(R^{2d}f_!\) a right exact functor on sheaves. For a finite open cover \(X=\bigcup U_i\), with inclusions \(j_i\) and \(j_{ij}\), the stalkwise exact sequence

\[
\bigoplus_{i,j}j_{ij,!}\Lambda\longrightarrow
\bigoplus_i j_{i,!}\Lambda\longrightarrow\Lambda_X\longrightarrow0
\tag{ST.2}
\]

uses the difference of the two extension maps on intersections. To check exactness, choose any geometric point: the remaining terms are the usual augmented degree-zero Čech sequence of its nonempty finite set of covering indices. An element whose coefficient sum is zero is a sum of differences from those indices. Apply the right exact functor to obtain

\[
\bigoplus_{i,j}R^{2d}(fj_{ij})_!\Lambda(d)\longrightarrow
\bigoplus_iR^{2d}(fj_i)_!\Lambda(d)\longrightarrow
R^{2d}f_!\Lambda(d)\longrightarrow0.
\tag{ST.3}
\]

Thus local traces that agree on intersections descend to one trace. Equality of global trace maps can also be tested after these covering maps. The use of the highest possible degree is essential to this descent argument.

For a separated étale morphism \(u:V\to W\) of finite presentation, \(u_!\) is exact: its stalk is a finite direct sum over the geometric fibre. Its counit

\[
\operatorname{sum}_u:u_!u^*F\longrightarrow F
\tag{ST.4}
\]

adds those entries. Summation commutes with base change and with composition, by the same stalk formula. The identities also hold on complexes because this functor is exact.

### 2.2. Affine-space integration and local candidates

Write \(a_d:\mathbf A^d_S\to S\). The relative affine-line trace is obtained from \(\mathbf P^1_S\) using \(c_1(\mathcal O(1))\), proper base change and excision at infinity. It is the isomorphism

\[
\tau_{a_1}:R^2a_{1,!}\Lambda(1)\xrightarrow{\sim}\Lambda.
\tag{ST.5}
\]

There is no sign change: a degree-one Kummer Chern class has trace one. The relative-curve foundation proves that construction and its geometric normalization.

For composable maps with fibre dimensions at most \(e,d\), the compact-support composition spectral sequence has only one possible term of total degree \(2e+2d\). Its edge isomorphism is

\[
R^{2e}g_!R^{2d}h_!F\xrightarrow{\sim}
R^{2(e+d)}(gh)_!F.
\tag{ST.6}
\]

Indeed a term in that total degree requires both indices at their upper bounds; incoming and outgoing differentials would require an index above one of those bounds. Successive affine-line projections and (ST.6) define \(\tau_{a_d}\). These are isomorphisms, because (ST.5) is an isomorphism after every base change.

The definition is independent of the order of the coordinates. This can be checked on every geometric fibre by the proved derived Künneth formula. Compact cohomology of \(\mathbf A^1\) is the free rank-one module in degree two, with its Tate twist. Consequently compact cohomology of \(\mathbf A^d\) is the tensor product of these degree-two factors. Permuting them contributes \((-1)^{2\cdot2}=1\), and each factor's normalized generator integrates to one. All coordinate permutations preserve \(\tau_{a_d}\). The fibre formula for compact support and conservativity of geometric stalks prove the relative assertion.

If \(u:U\to\mathbf A^d_S\) is a separated étale coordinate map, the composition isomorphism and (ST.4) give a local candidate

\[
t_{f|_U,u}=\tau_{a_d}\circ
R^{2d}a_{d,!}(\operatorname{sum}_u):
R^{2d}(f|_U)_!\Lambda(d)\longrightarrow\Lambda_S.
\tag{ST.7}
\]

It already commutes with base change. Its independence of \(u\) requires a proof; geometric stalks alone do not prove independence until the fibre maps have been compared.

### 2.3. Connecting étale coordinates without introducing singular curve fibres

Fix a smooth finite-type \(d\)-fold \(U\) over an algebraically closed field \(k\), two étale coordinate maps \(u,v:U\to\mathbf A^d_k\), and a closed point \(x\). The differentials \(du_1,\ldots,du_d\) and \(dv_1,\ldots,dv_d\) are bases at \(x\).

There are functions \(w_i=\sum_jm_{ij}u_j\), with \(M=(m_{ij})\in\operatorname{GL}_d(k)\), such that every intermediate list formed by replacing the coordinates of \(u\) by those of \(w\), one at a time, has independent differentials at \(x\); the same holds while replacing \(w\) by \(v\). Here is the existence argument. The determinants of the finitely many mixed differential matrices are polynomials in the entries of \(M\). A mixed matrix using fixed rows from \(du\) can be completed to a basis by freely choosing its remaining rows, so its determinant polynomial is nonzero. A mixed matrix using fixed rows from \(dv\) has the same property, since those fixed rows are independent and every cotangent vector is a linear combination of the \(du_j\). Include \(\det M\) among these nonzero polynomials. Their product is nonzero. A nonzero polynomial over the infinite field \(k\) cannot vanish at every \(k\)-point: induct on the number of variables, using the finite number of roots of a nonzero polynomial in one variable. Choose \(M\) at which this product is nonzero.

Each intermediate coordinate map is therefore étale at \(x\). Restrict to the intersection of their finitely many étale loci, an open neighbourhood \(W\) of \(x\). We have connected \(u|_W\) to \(v|_W\) by changing one coordinate at a time while keeping every entire coordinate system étale. If the changed coordinate is moved to first position, the common remaining coordinates define

\[
h:W\longrightarrow\mathbf A^{d-1}_k
\tag{ST.8}
\]

as a smooth relative curve: either of the full coordinate maps factors it as an étale map to \(\mathbf A^1_{\mathbf A^{d-1}_k}\), followed by its smooth projection. This construction avoids a hidden use of a trace theorem for singular flat curves.

For those two full coordinate maps, (ST.7), (ST.6) and the order independence of affine-space integration express both candidates as

\[
\tau_{a_{d-1}}\circ R^{2d-2}a_{d-1,!}(\tau_h).
\tag{ST.9}
\]

The relative-curve construction identifies \(\tau_h\) with the composite obtained using **either** of its étale maps to the relative affine line. Hence changing the first coordinate leaves the candidate unchanged. Coordinate permutations allow the same conclusion for each step. The entire chain proves equality of the two candidates on \(W\).

The neighbourhoods just constructed cover every closed point of \(U\), and hence cover \(U\): a finite-type scheme over a field is Jacobson, so a nonempty closed complement would contain a closed point. A finite subcover and (ST.3) give equality on all of \(U\).

Now return to an arbitrary base \(S\). The candidates for two coordinate maps have compact-support base-change isomorphisms. At a geometric point of \(S\), they become exactly the maps just compared over its algebraically closed residue field. Equality at all geometric stalks proves equality of the original sheaf maps. This proves coordinate independence in (ST.7), including over nonreduced bases.

### 2.4. Global construction and functorial properties

Choose finitely many affine open charts of \(X\), after covering \(S\) by finitely many affine opens. Smooth coordinates give étale maps from these charts to \(\mathbf A^d_S\). Their intersections can be covered by charts with either inherited coordinate map, whose candidate traces agree by §2.3. Equation (ST.3) descends their sum to \(\tau_f\) in (ST.1). Comparing two covers with their common refinement proves independence of the cover. All constructions commute with base change. The base-changed open cover still covers, and its descended map is characterized by its chart restrictions, so \(\tau_f\) commutes with arbitrary base change.

If \(b:X'\to X\) is separated étale of finite presentation, the chart of \(X'\) obtained by composing with a chart of \(X\) gives

\[
\tau_{fb}=\tau_f\circ R^{2d}f_!(\operatorname{sum}_b).
\tag{ST.10}
\]

This is first the composition identity for the finite sums in (ST.4), and then descends by (ST.3). In particular it proves compatibility with open extension.

For separated smooth \(h:X\to Y\) of relative dimension \(d\) and \(g:Y\to S\) of relative dimension \(e\), choose a chart of \(Y/S\) and a relative chart of \(X/Y\). Their composite is an étale map to \(\mathbf A^d_S\times_S\mathbf A^e_S\): an étale map remains étale after the product base change, and compositions of étale maps are étale. Affine-space integration on that product can first integrate the \(d\) coordinates and then the \(e\) coordinates, by (ST.6) and §2.2. Summation over the intermediate étale sheets commutes with the first integration: its square is the compact-support base-change square for the affine-space projection, and the counit is a finite sum on each geometric stalk. Equivalently, on a geometric fibre both orders add the same entries and integrate the same normalized affine factors. The chart candidates consequently satisfy

\[
\tau_{gh}=\tau_g\circ R^{2e}g_!(\tau_h),
\tag{ST.11}
\]

under (ST.6), with the remaining twists retained. Apply (ST.3) first to the source charts and then to the intermediate charts to obtain (ST.11) globally. Associativity follows from the associativity of the compact-support composition isomorphisms and these same local integrations.

Every affine normalization is defined by the Kummer class of \(\mathcal O(1)\), and every other map is tensor, an étale counit, composition or descent. The Kummer coefficient diagrams and finite summation show that these maps commute with reduction \(\mathbf Z/n\to\mathbf Z/m\) when \(m\mid n\). This is a statement about the coefficient comparison maps themselves; it does not assert that arbitrary cohomology groups commute with ordinary underived tensor product.

### 2.5. Derived trace and arbitrary pulled-back coefficients

The amplitude bound places \(Rf_!\Lambda(d)[2d]\) in \(D^{\leq0}\). Its canonical truncation map to its degree-zero cohomology, followed by (ST.1), defines

\[
T_f:Rf_!\Lambda(d)[2d]\longrightarrow\Lambda.
\tag{ST.12}
\]

For an arbitrary complex \(A\) on \(S\), the already proved arbitrary-complex projection formula gives

\[
Rf_!\bigl(f^*A(d)[2d]\bigr)
\xrightarrow{\sim} A\otimes^L Rf_!\Lambda(d)[2d]
\xrightarrow{1\otimes T_f}A.
\tag{ST.13}
\]

Base change, étale extension and smooth composition of (ST.12) follow from those properties of the top-degree maps. For composition, both compact-support orientation complexes have highest degree zero, so the composition spectral sequence identifies the highest degree with (ST.6); the canonical truncation followed by the successive top traces is the truncation followed by (ST.11). Applying the projection formula and the associativity of derived tensor proves the corresponding properties of (ST.13), without imposing a boundedness or finite Tor-dimension condition on \(A\). The orientation shifts are even, so interchanging their factors introduces no sign.

## 3. Compact support near a geometric point

Let \(\bar x\to X\) be a geometric point. Use affine pointed étale neighbourhoods \((U,\bar u)\); morphisms preserve the chosen point. Fibre products and further affine neighbourhoods give common refinements, and two parallel maps agree after a further refinement. This is a cofiltered category, and its inverse limit is \(X_{(\bar x)}\).

A refinement \(v:U'\to U\) is separated and étale of finite presentation. The counit \(v_!v^*\Lambda\to\Lambda\), given by summation, induces

\[
R\Gamma_c(U',\Lambda(a))\longrightarrow
R\Gamma_c(U,\Lambda(a)).
\tag{3.1}
\]

On ordinary cohomology the direction is reversed: there is pullback from \(U\) to \(U'\). These two directions are dual under the curve theorem when \(U\) has dimension one. For a general refinement of smooth curves, factor its quasi-finite map as an open immersion followed by a finite map using normalization. The finite trace and the open adjunction proved in the curve-duality chapter identify (3.1) with the transpose of ordinary pullback. Thus this compatibility includes affine neighbourhoods and not just finite étale covers.

Write

\[
\mathcal C^r_{\bar x}(\Lambda(a))
=\{H^r_c(U,\Lambda(a))\}_U,
\qquad
H^r_{c,\mathrm{germ}}(X_{(\bar x)},\Lambda(a))
=\varprojlim_U H^r_c(U,\Lambda(a)).
\tag{3.2}
\]

The first object is a pro-module: it retains the system, including maps that eventually become zero. It is this object that our proof computes. The second is its inverse limit. Neither is a filtered colimit of compact groups using ordinary pullback. For a strict germ not finite type, (3.2) is a definition and does not assert that a finite-type compactification of the germ has been chosen.

**Lemma 3.1 (finite systems).** Inverse limit is exact on cofiltered systems of finite modules. Such a system is pro-zero if and only if its inverse limit is zero.

*Proof.* A pro-zero system means that for each target stage some later transition into it is zero. Its limit is then zero. Conversely, fix a stage \(i\). The images of later groups in the finite group \(A_i\) form a filtered decreasing family of subgroups, so their intersection is achieved by a common refinement of finitely many stages. That intersection is the image of the inverse limit in \(A_i\): any value in it has a compatible lift. To prove the last assertion, put all possible lifts in a product of finite discrete sets. The compatibility conditions are closed, and every finite family of them is solvable at one common refinement. Compactness of the product supplies a simultaneous solution. If the limit is zero, the intersection is zero, so a later map into \(A_i\) is zero.

For a levelwise short exact sequence of finite systems, a compatible element of the quotient likewise has compatible lifts: impose the lifting equations and the transition equations in the product of the finite sets of lifts. Every finite set of equations is solvable at one common refinement, by levelwise surjectivity. Compactness gives all the equations at once. Limits already preserve kernels, so they are exact. Finite diagrams in a pro-category can be represented at common indices by taking refinements; this proves the same assertion for an exact sequence of pro-finite modules. \(\square\)

No assumption of a countable list of neighbourhoods, and no unproved interchange with an infinite product of cochain degrees, occurs in this argument.

## 4. From pointwise vanishing to a uniform derived limit

Two elementary lemmas make the local induction rigorous.

**Lemma 4.1 (uniform refinement).** Let \(B\) be quasi-compact and quasi-separated, and let \(\{E_i\}\) be a cofiltered system of constructible finite module sheaves on \(B\). If its stalk system is pro-zero at every geometric point, then the sheaf system is pro-zero.

*Proof.* Fix \(i\). For a later stage \(j\), the image of \(E_j\to E_i\) is constructible by the Serre property. Its nonzero-stalk locus is a constructible subset of \(B\). Its complement, where that map is zero, is therefore open in the constructible topology. These complements cover \(B\), by the hypothesis on stalks. The constructible topology of a quasi-compact, quasi-separated scheme is compact: on an affine this is the compact topology generated by quasi-compact opens and their complements, and a finite affine cover gives the assertion for \(B\). A finite number of the complements consequently cover \(B\). Choose a common later stage for their maps. Its map to \(E_i\) is zero at every stalk and hence zero as a sheaf map. \(\square\)

Apply the lemma to kernels, cokernels and cohomology sheaves when their finite presentation has been fixed. In particular, an isomorphism of stalk pro-systems gives a pro-isomorphism of constructible sheaf systems. Pointwise vanishing alone would not justify this conclusion without the constructibility and compactness argument.

**Lemma 4.2 (bounded ghosts).** Suppose all \(K_i\) lie in \(D^{[a,b]}\), and each map in a chain induces zero on every cohomology object. A composite of \(b-a+1\) such maps is zero. Consequently a uniformly bounded system with pro-zero cohomology has pro-zero objects in the derived category.

*Proof.* If \(u:A\to B\) kills \(H^b\), its composite with \(B\to H^b(B)[-b]\) is zero. Indeed any map from \(A\in D^{\leq b}\) to the last object is determined by \(H^b(A)\), by the truncation triangle and the vanishing of Hom from \(D^{\leq b-1}\) to \(D^{\geq b}\). Thus \(u\) factors through \(\tau_{\leq b-1}B\). The next ghost, restricted to that truncation, factors through \(\tau_{\leq b-2}\) of its target by the same argument. Repeating lowers the upper degree by one at each step, and after \(b-a+1\) steps the composite factors through zero. For a system, first refine to kill all its finitely many cohomology degrees, and repeat this finitely many times. \(\square\)

We also use finite-presentation descent explicitly. A constructible sheaf and its morphisms on a strict local base descend to an étale neighbourhood of that base point. Equality or zero of a descended morphism holds at some later neighbourhood. This is the finite-presentation/continuity assertion from the finite-morphism and constructible-sheaf chapters: use finite presentations on the finite-presentation étale basis, and descend the finite generators and relations at a common stage. For a bounded derived diagram, make these descents in its finitely many cohomology degrees and use Lemma 4.2 to kill the remaining ghosts. Thus the computations below on a strict base give actual refined neighbourhood maps, rather than merely an equality of numerical fibre dimensions.

## 5. The relative-curve calculation

For a smooth \(f:X\to S\), fix \(\bar x\) over \(\bar s\). A neighbourhood diagram consists of an affine étale \(V\to S\), a pointed affine étale \(U\to X\times_S V\), and its smooth map \(g:U\to V\). Put \(j_V:V\to S\). Trace gives a morphism of inverse systems

\[
\{R(fj_U)_!\Lambda(d)\}_{{(U,V)}}
\longrightarrow
\{j_{V,!}\Lambda[-2d]\}_{{(U,V)}}.
\tag{5.1}
\]

On the left \(j_U:U\to X\); its map to the term on the right is \(j_{V,!}\operatorname{Tr}_g\). The transition maps on both sides are the étale counits. The trace constructed in §2 makes their squares commute by (ST.10).

**Proposition 5.1 (dimension one).** If \(d=1\), the cone system in (5.1) is pro-zero in the derived category. Equivalently, trace is an isomorphism of these bounded derived pro-systems.

*Proof.* Fix an original target diagram \((U_0,V_0)\). The chosen geometric point identifies \(B=(V_0)_{(\bar v_0)}\) with \(S_{(\bar s)}\), and selects the map \(B\to V_0\). First consider the relative trace cones on \(V_0\), before applying \(j_{V_0,!}\). Pullback along this selected map identifies their source terms with \(Rg_{U,!}\Lambda(1)\) on \(B\). Thus \(U_B\) means \(U\times_{V_0}B\), rather than the union of all sheets of \(U\times_SB\). They have degrees zero through two. The source neighbourhoods have smooth relative dimension one. Their images contain the closed point of \(B\), and a smooth map has open image; an open subset of a local scheme containing its closed point is the whole scheme. Thus every geometric fibre is nonempty.

For a geometric \(\bar t\to B\), compact base change gives the finite groups

\[
(R^qg_{U,!}\Lambda(1))_{\bar t}
=H^q_c(U_{\bar t},\Lambda(1)).
\tag{5.2}
\]

The inverse limit of the affine schemes \(U_{\bar t}\) is the local fibre
\(X_{(\bar x)}\times_B\bar t\). Continuity and smooth local acyclicity, already proved in the smooth-base-change chapter, give

\[
\mathop{\mathrm{colim}}_U H^r(U_{\bar t},\Lambda)
=\begin{cases}\Lambda&r=0,\\0&r>0.\end{cases}
\tag{5.3}
\]

The map from \(\Lambda\) in degree zero is the constant-section map. These are smooth affine curves over a separably closed field; passage to its algebraic closure is an étale-topos equivalence, so the proved curve theorem applies. It identifies each group in (5.2) with the dual of \(H^{2-q}(U_{\bar t},\Lambda)\), and identifies the transition trace with the transpose of pullback, by Section 3.

For positive ordinary degree, a finite group's generators all become zero at a common later stage by (5.3). The corresponding compact transition is zero. In ordinary degree zero the constant-section inclusion is injective, because the fibre is nonempty. Its finite quotient becomes zero at a later stage, since (5.3) says the colimit is exactly the constants. Exact finite-module duality turns this into the statement that the kernel system of the top trace is pro-zero. That trace is surjective: on each fibre it sums the component traces, each normalized to one. Thus at every \(\bar t\) the compact pro-system is \(\Lambda[-2]\), via trace.

Each \(R^qg_{U,!}\Lambda(1)\), its trace kernel and the relevant images are constructible, by the explicitly stated general constructibility input of the compact-support chapter. Their images are again constructible: on a common finite stratification where the two sheaves are locally constant, a morphism is locally a fixed map of finite modules, whose kernel and image are locally constant. This also proves the needed Serre assertion over the coherent strict base. Lemma 4.1 now kills the finitely many cohomology sheaves of the trace cone by one uniform refinement on \(B\). The cones have a fixed finite range, so repeated refinement and Lemma 4.2 kill their maps in the derived category itself.

Finally descend the finite data to \(V\)'s. The schemes and coefficients have finite presentation; compact base change identifies their cohomology sheaves over \(B\), and zero of the finitely many descended sheaf maps holds at a later base neighbourhood. Repeat the bounded-ghost construction there. For the resulting \(v:V'\to V_0\), the refined relative cone map \(C_{U'}\to v^*C_{U_0}\) is zero on \(V'\). Its adjoint \(v_!C_{U'}\to C_{U_0}\) is therefore zero. Applying \(j_{V_0,!}\) gives the zero cone map on \(S\) required in (5.1). Since the original diagram was arbitrary, this proves pro-zero of that system, including the extension-by-zero maps between different base neighbourhoods. \(\square\)

The proof used local acyclicity of the strict fibre, not the false assertion that a whole smooth affine curve has zero degree-one cohomology. The finite cohomology of whole curves supplies the uniform generator argument; their degree-one groups are allowed to be large.

## 6. Induction in the relative dimension

**Theorem 6.1 (local trace system).** Proposition 5.1 holds for every \(d\geq0\).

*Proof.* For \(d=0\), \(f\) is étale. After taking \(V\) to be a pointed étale neighbourhood in its source, the base-changed map has the distinguished section through \(\bar x\). Its image is open, since it is a section of an étale map. Restrict the source neighbourhood to that section. The trace comparison there is the identity of \(j_{V,!}\Lambda\). Such restrictions refine every diagram, proving the result.

The case \(d=1\) is Proposition 5.1. Suppose \(d>1\), and assume the result in lower dimension. Étale locally at \(\bar x\), smooth coordinates factor \(f\) as

\[
X\xrightarrow{h}Y\xrightarrow{g}S,
\qquad \dim(h)=1,\quad\dim(g)=d-1.
\tag{6.1}
\]

Indeed take an étale coordinate map to \(\mathbf A^d_S\), and project onto \(\mathbf A^{d-1}_S\). After restriction to an affine chart both maps are separated and smooth of finite presentation. This restriction is cofinal in the source neighbourhood system, so suffices for the local assertion.

Use neighbourhood triples \(U\to X\), \(V\to Y\), \(W\to S\), with \(U\to V\to W\). Any finite list of such conditions can be achieved by taking fibre products and a further affine pointed chart. Conversely every source neighbourhood admits such a refinement. Thus the iterated system is the same local system, indexed cofinally, and no special chosen sequence is being substituted for it.

The dimension-one result for \(h\), in the derived pro-category on \(Y\), is

\[
\{R(hj_U)_!\Lambda(1)\}_{(U,V)}
\xrightarrow{\sim}
\{j_{V,!}\Lambda[-2]\}_{(U,V)}.
\tag{6.2}
\]

Apply \(Rg_!\), tensor with the additional twist \((d-1)\), and use composition. Zero derived maps remain zero under this exact functor, so a pro-zero cone remains pro-zero. The resulting source terms are \(R(fj_U)_!\Lambda(d)\); the target terms are
\(R(gj_V)_!\Lambda(d-1)[-2]\). The induction hypothesis for \(g\) identifies their pro-system with
\(j_{W,!}\Lambda[-2(d-1)][-2]\). The composite is exactly (5.1), by compatibility of trace with composition and base change. It therefore has pro-zero cone.

Here is the compact Leray content of this argument. At every finite neighbourhood diagram, composition has the good-truncation spectral sequence

\[
R^pg_!R^qh_!\Lambda(d)
\Longrightarrow R^{p+q}(gh)_!\Lambda(d).
\tag{6.3}
\]

There are only \(0\leq q\leq2\) and \(0\leq p\leq2(d-1)\). Proposition 5.1 kills the unwanted rows uniformly as pro-sheaves; the remaining row is \(\Lambda(d-1)\) in degree two, via the actual trace map. The finite filtration then reduces (6.3) to the induction hypothesis. More strongly, Lemma 4.2 gives (6.2) at the derived level before applying \(Rg_!\), so possible extension maps between rows are killed as well. This is the justification of the limit Leray step. It uses finitely many truncations and refinements, rather than an unjustified interchange of infinite cochain totals with inverse limit. \(\square\)

## 7. The absolute local statement

**Corollary 7.1.** If \(X/k\) is smooth of pure dimension \(N\) and \(x\) is a closed point, then

\[
\mathcal C^r_x(\Lambda)=0\quad(r\ne2N),
\qquad
\operatorname{Tr}:\mathcal C^{2N}_x(\Lambda(N))
\xrightarrow{\sim}\Lambda.
\tag{7.1}
\]

The same formulas hold for the inverse-limit groups in (3.2).

*Proof.* Apply Theorem 6.1 to \(X\to\operatorname{Spec}k\). Pointed étale base neighbourhoods of the algebraically closed field refine to its distinguished copy of \(\operatorname{Spec}k\). Hence its target system is the constant \(\Lambda[-2N]\). Taking cohomology gives (7.1). Compact cohomology at every source stage is finite by the general finiteness input of the compact-support chapter. Lemma 3.1 passes the pro-isomorphism to inverse limits and identifies vanishing with pro-zero. Removing the twist gives \(\Lambda(-N)\) in degree \(2N\). \(\square\)

Explicitly, coordinates give a smooth relative curve from the strict germ of \(X\) to the strict germ of a smooth \((N-1)\)-fold. Equations (5.2)–(5.3) identify its local-fibre compact row with \(\Lambda(-1)\) in degree two. The finite Leray filtration of Section 6 then gives

\[
H^r_{c,\mathrm{germ}}(X_{(x)},\Lambda(N))
=H^{r-2}_{c,\mathrm{germ}}(Y_{(y)},\Lambda(N-1)),
\tag{7.2}
\]

via trace. Iteration ends at a point. Thus the claimed local concentration was proved from the curve case and local acyclicity; it has not been deduced from the global theorem we are about to prove.

## 8. Exceptional inverse image and its local description

Let \(f\) be separated finite type between quasi-compact, quasi-separated schemes. The category of \(\Lambda\)-module sheaves is Grothendieck. Brown representability in its derived category says that a contravariant cohomological functor taking sums to products is represented by an object. For fixed \(A\), apply it to

\[
E\longmapsto\operatorname{Hom}_S(Rf_!E,A).
\]

It is cohomological because \(Rf_!\) is exact, and takes sums to products because \(Rf_!\) preserves sums. Representing objects and Yoneda give a right adjoint \(Rf^!\), with

\[
\operatorname{Hom}_X(E,Rf^!A)
=\operatorname{Hom}_S(Rf_!E,A).
\tag{8.1}
\]

Naturality determines its functoriality and counit; adjoints of exact triangulated functors are exact, as follows by applying (8.1) to a triangle and its shifts. This constructs the operation without assuming its smooth formula.

For an affine étale \(j:U\to X\), exact extension by zero and composition give

\[
H^r(U,Rf^!A)
=\operatorname{Hom}_X(j_!\Lambda,Rf^!A[r])
=\operatorname{Hom}_S(R(fj)_!\Lambda,A[r]).
\tag{8.2}
\]

Sheafifying this presheaf computes \(H^r(Rf^!A)\). In particular its stalk is the filtered colimit over pointed \(U\) of the last groups. To see that sheafification is valid even for an unbounded \(A\), use a K-injective representative for \(Rf^!A\). Its sections on \(U\) compute hypercohomology; the filtered colimit of those section complexes is its stalk complex. Exact filtered colimits commute with taking cohomology, giving the assertion.

Composition of lower shrieks transposes to
\(R(gh)^!=Rh^!Rg^!\). The counit is the composite of the two counits: testing Hom makes both maps the identity map in the two adjunctions, so uniqueness proves their agreement and the associativity condition. For an étale base change \(v:V\to S\), with source map \(v_X\), the corresponding comparison
\(v_X^*Rf^!A=Rf_V^!v^*A\) follows by testing a complex \(B\) on the base-changed source:

\[
\begin{aligned}
\operatorname{Hom}(B,v_X^*Rf^!A)
&=\operatorname{Hom}(v_{X,!}B,Rf^!A)\\
&=\operatorname{Hom}(v_!Rf_{V,!}B,A)\\
&=\operatorname{Hom}(Rf_{V,!}B,v^*A).
\end{aligned}
\tag{8.3}
\]

These equalities also prove compatibility of the counit with étale localization: each comparison is the mate of the lower-shriek comparison under the same adjunction, so composing it with the counit returns that comparison. The two triangle identities for units and counits verify this directly. This is the compatibility isolated in Deligne's “Dualité,” §4.

There is also an internal comparison, for arbitrary \(A,E\),

\[
Rf_*R\mathcal Hom_X(E,Rf^!A)
\xrightarrow{\sim}R\mathcal Hom_S(Rf_!E,A).
\tag{8.4}
\]

To prove it, test by Hom from an arbitrary \(M\) on \(S\). The left group is, in order,

\[
\begin{aligned}
\operatorname{Hom}_X(f^*M\otimes^LE,Rf^!A)
&=\operatorname{Hom}_S(Rf_!(f^*M\otimes^LE),A)\\
&=\operatorname{Hom}_S(M\otimes^LRf_!E,A)\\
&=\operatorname{Hom}_S(M,R\mathcal Hom_S(Rf_!E,A)).
\end{aligned}
\tag{8.5}
\]

The middle equality is the already proved arbitrary-complex projection formula. Yoneda gives (8.4). Its map is evaluation followed by the counit, because every equality used that adjunction. Taking derived global sections gives the corresponding isomorphism of global derived Hom complexes. \(\square\)

## 9. The relative smooth duality formula

Transpose (ST.13) under (8.1). It gives a natural map

\[
t_{f,A}:f^*A(d)[2d]\longrightarrow Rf^!A.
\tag{9.1}
\]

**Theorem 9.1.** For every complex \(A\in D(S,\Lambda)\), (9.1) is an isomorphism. Under it the adjunction counit is precisely (ST.13).

*Proof.* Fix \(\bar x\) over \(\bar s\). In the neighbourhood diagrams of Section 5, untwist (5.1) to obtain the derived pro-comparison

\[
\{R(fj_U)_!\Lambda\}\xrightarrow{\sim}
\{j_{V,!}\Lambda(-d)[-2d]\}.
\tag{9.2}
\]

Its cone is pro-zero by Theorem 6.1. Apply Hom into \(A[r]\). The long exact sequences of the cone triangles, followed by exact filtered colimit, show that (9.2) gives an isomorphism

\[
\begin{aligned}
\mathop{\mathrm{colim}}_{(U,V)}
\operatorname{Hom}_S(R(fj_U)_!\Lambda,A[r])
&=\mathop{\mathrm{colim}}_{(U,V)}
\operatorname{Hom}_S(j_{V,!}\Lambda(-d)[-2d],A[r])\\
&=\mathop{\mathrm{colim}}_V H^{r+2d}(V,A(d))\\
&=(H^{r+2d}(A(d)))_{\bar s}.
\end{aligned}
\tag{9.3}
\]

There is no boundedness restriction on \(A\): any element of Hom from a cone is killed by the later zero cone map itself. Forgetting the auxiliary neighbourhood in these colimits is cofinal. For a fixed source neighbourhood and a fixed base neighbourhood, their fibre product has a further pointed source neighbourhood; similarly every base neighbourhood has such a source neighbourhood. This verifies both cofinality assertions in (9.3).

By (8.2), the left group is \(H^r(Rf^!A)_{\bar x}\); the right group is \(H^r(f^*A(d)[2d])_{\bar x}\). The comparison is the map induced by (9.1): both are obtained by precomposing Hom with the trace of the same neighbourhood diagram. All geometric stalks and all cohomological degrees agree, proving the theorem. Finally (9.1) was the adjoint of (ST.13), so the counit composed with \(Rf_!t_{f,A}\) is (ST.13), by the adjunction triangle identity. \(\square\)

This proof also verifies composition of the smooth identifications. Transpose the two successive traces; their composite is the transpose of the composite trace and hence \(t_{gh,A}\). Their twists add and their shifts add. The identification commutes with base change because the trace, the lower-shriek base-change comparison and inverse image do. It can alternatively be used to define that smooth upper-shriek base-change isomorphism, with the same counit.

For completeness, the formula gives the amplitude

\[
Rf^!(D^{[a,b]})\subset D^{[a-2d,b-2d]}.
\tag{9.4}
\]

Before knowing the formula, adjunction gives the lower bound \(Rf^!D^{\geq a}\subset D^{\geq a-2d}\). Indeed test (8.1) on \(E=\tau_{\leq a-2d-1}Rf^!A\). The lower-shriek amplitude places \(Rf_!E\) in \(D^{\leq a-1}\), so its Hom into \(A\in D^{\geq a}\) is zero. The truncation inclusion is therefore zero, forcing its cohomology to vanish. This adjunction argument alone supplies no analogous upper bound. Equation (9.3) proves the arbitrary-complex smooth formula directly, and that formula supplies both bounds in (9.4).

## 10. Global Poincaré duality

Set \(p:X\to\operatorname{Spec}k\) and

\[
K_X=\Lambda_X(N)[2N],\qquad
D_XE=R\mathcal Hom_X(E,K_X).
\tag{10.1}
\]

**Theorem 10.1.** For every \(E\in D(X,\Lambda)\), evaluation and trace give a canonical isomorphism

\[
R\Gamma(X,D_XE)
\xrightarrow{\sim}
R\operatorname{Hom}_\Lambda(R\Gamma_c(X,E),\Lambda).
\tag{10.2}
\]

For a finite locally constant \(F\), it gives mutually perfect finite-group pairings

\[
H^i_c(X,F)\times H^{2N-i}(X,F^\vee(N))
\xrightarrow{\ \operatorname{Tr}_X(a\cup b)\ }\Lambda,
\qquad F^\vee=\mathcal Hom_\Lambda(F,\Lambda).
\tag{10.3}
\]

*Proof.* Theorem 9.1 identifies \(Rp^!\Lambda\) with \(K_X\), with counit the specified trace. Apply (8.4) to \(p\), \(A=\Lambda\) and \(E\). The small étale site of the algebraically closed field is the category of modules, with exact global sections. Thus (8.4) is exactly (10.2), with its evaluation-and-trace map.

Locally \(F\) is a constant finite module \(M\). the curve-duality chapter, Lemma 3.1, proves that \(\Lambda\) is injective over itself, including composite \(n\); therefore \(R\operatorname{Hom}_\Lambda(M,\Lambda)=M^\vee\) in degree zero. Sheafifying a finite-free module resolution on a trivializing cover proves the same internal formula. The invertible twist is exact, so
\(D_XF=F^\vee(N)[2N]\).

The same self-injectivity identifies degree \(-i\) on the right of (10.2) with \(H^i_c(X,F)^\vee\): dualize cycles, boundaries and their quotient by the exact Hom functor. Degree \(-i\) on the left is \(H^{2N-i}(X,F^\vee(N))\). Compact groups are finite by the earlier stated finiteness input; the isomorphism proves finiteness of these ordinary groups as well. Finite-module evaluation is an isomorphism to the bidual, so each factor is the dual of the other. The pairing is (10.3) because (8.4) uses evaluation followed by the trace counit. \(\square\)

Invertibility of \(n\) is essential. In characteristic \(p\), the affine-vanishing chapter's Artin–Schreier example gives an infinite \(H^1(\mathbf A^1,\mathbf Z/p)\); the finite prime-to-characteristic pairing proved here has no such conclusion for those coefficients.

For a general constructible complex, (10.2) still uses internal derived Hom. Replacing it by just the ordinary degree-zero dual sheaf would drop ramification or extension terms. For local systems (10.3) is ordinary cohomology and needs neither free fibres nor a finite projective resolution of \(F\). We order the compactly supported factor first; exchanging degree \(r\) and degree \(s\) contributes \((-1)^{rs}\).

**Corollary 10.2 (top compact degree).** For connected \(X\), trace is an isomorphism

\[
H^{2N}_c(X,\Lambda(N))\xrightarrow{\sim}\Lambda.
\tag{10.4}
\]

*Proof.* Apply (10.3) to \(F=\Lambda(N)\) in degree \(2N\). Its other factor is \(H^0(X,\Lambda)=\Lambda\), since \(X\) is connected. Pairing with its constant section \(1\) is exactly trace, proving (10.4). For a finite union of connected components the group is a copy of \(\Lambda\) for each component and trace is their sum. \(\square\)

## 11. Purity and the distinction between sheaves and groups

Let \(i:Z\hookrightarrow X\) be a closed immersion of smooth \(k\)-schemes, with \(X\) purely \(N\)-dimensional and \(Z\) purely \((N-c)\)-dimensional. Write \(j:X-Z\hookrightarrow X\). The right adjoint \(i^!\) of exact \(i_*\) is sections supported on \(Z\), regarded as a sheaf on \(Z\). Since \(i_*\) is exact, \(i^!\) sends injectives to injectives. An injective resolution therefore gives both

\[
i_*Ri^!E\longrightarrow E\longrightarrow Rj_*j^*E\longrightarrow i_*Ri^!E[1]
\tag{11.1}
\]

and \(R\Gamma_Z(X,E)=R\Gamma(Z,Ri^!E)\). Indeed restriction of an injective sheaf to an open is surjective on sections, with kernel the supported sections, so (11.1) comes from that short exact sequence of resolution complexes. This proves the support formalism used here.

**Theorem 11.1 (smooth-pair purity).** There is a canonical orientation isomorphism

\[
Ri^!\Lambda_X=\Lambda_Z(-c)[-2c].
\tag{11.2}
\]

Consequently

\[
R^qi^!\Lambda_X=0\ (q\ne2c),\qquad
R^{2c}i^!\Lambda_X=\Lambda_Z(-c),
\tag{11.3}
\]

whereas the global groups satisfy

\[
H^r_Z(X,\Lambda)=H^{r-2c}(Z,\Lambda(-c)).
\tag{11.4}
\]

*Proof.* The structure maps satisfy \(p_Z=p_Xi\). Composition of right adjoints gives

\[
Ri^!Rp_X^!\Lambda=Rp_Z^!\Lambda.
\tag{11.5}
\]

Substitute the two proved smooth formulas:
\(Ri^!(\Lambda_X(N)[2N])=\Lambda_Z(N-c)[2N-2c]\).
An invertible local system \(T\) commutes with \(Ri^!\). To verify this, test Hom from \(B\) on \(Z\), move \(T\) to its inverse twist on the other argument, use \(i_*B\otimes T^{-1}=i_*(B\otimes i^*T^{-1})\), and apply the adjunction. Yoneda identifies the resulting functors. Thus twist by \((-N)\) and shift by \([-2N]\) give (11.2). Its single cohomology degree gives (11.3). Applying \(R\Gamma(Z,-)\) to (11.2) gives (11.4). \(\square\)

In particular \(H^{2c}_Z(X,\Lambda)=H^0(Z,\Lambda(-c))\), and the groups below \(2c\) vanish. Higher global groups need not vanish. For example take the zero section
\(Z=\mathbf P^1\times\{0\}\subset X=\mathbf P^1\times\mathbf A^1\), with \(c=1\). Then

\[
H^4_Z(X,\Lambda)=H^2(\mathbf P^1,\Lambda(-1))
=\Lambda(-2)\ne0.
\tag{11.6}
\]

So the global cohomology with supports is not concentrated in one degree. The concentrated object is \(Ri^!\Lambda\); global support cohomology also includes the cohomology of \(Z\).

## 12. Gysin maps, orientation and point classes

Transpose the purity isomorphism by the closed adjunction. The counit supplies
\(i_*\Lambda_Z\to\Lambda_X(c)[2c]\). With a twist and either ordinary or compact global sections, it gives

\[
\begin{aligned}
i_* &:H^r(Z,\Lambda(a))\longrightarrow H^{r+2c}(X,\Lambda(a+c)),\\
i_* &:H^r_c(Z,\Lambda(a))\longrightarrow H^{r+2c}_c(X,\Lambda(a+c)).
\end{aligned}
\tag{12.1}
\]

In the second line, \(Rp_{X,!}i_*=Rp_{Z,!}\), since a closed immersion is proper. These are the Gysin maps. Their degrees and twists record the codimension, not the dimensions of the whole varieties.

**Proposition 12.1.** Gysin maps compose for a chain of smooth closed immersions. They satisfy the projection formula, and in the top compact degree preserve trace:

\[
i_*(u\cup i^*v)=i_*u\cup v,
\qquad
\operatorname{Tr}_X(i_*u)=\operatorname{Tr}_Z(u)
\quad(u\in H^{2(N-c)}_c(Z,\Lambda(N-c))).
\tag{12.2}
\]

*Proof.* Purity was defined by (11.5), so for two closed immersions its orientation is the composite right-adjoint identification. The counit for their composite is the composite of their counits, as proved in Section 8. This proves composition, with the twists and shifts added. The closed projection formula follows on sheaf stalks, on \(Z\) by the identity tensor formula and off \(Z\) by zero, and hence on K-flat complexes. Applying its adjunction and the counit gives the first equality of (12.2); the class \(u\) remains first in the coefficient tensor. For trace, compose the counit of \(i\) with the counit of \(p_X\). Their composite is the counit of \(p_Z\), which Theorem 9.1 identifies with its trace. This is the second equality. \(\square\)

A closed point \(x\) has \(c=N\). Its class is \(i_*1\) in compact degree \(2N\), or the image of the supported class in ordinary degree \(2N\). Equation (12.2) gives

\[
\operatorname{Tr}_X(\operatorname{cl}_c(x))=1.
\tag{12.3}
\]

This fixes its orientation without choosing a root. Even if its ordinary image vanishes, its compact image is the generator of (10.4).

**Lemma 12.2 (divisor normalization).** For a smooth divisor \(D\) in a smooth \(X\), the Gysin class of \(1\) is \(c_1^{(n)}\mathcal O_X(D)\) in \(H^2(X,\mu_n)\).

*Proof.* First take a closed point \(x\) on \(\mathbf P^1_k\). Purity identifies \(H^2_x(\mathbf P^1,\mu_n)\) with \(\Lambda\), and its orientation generator maps to the Gysin class. Proposition 12.1 gives that class trace one. The supported Kummer class of the pair \((\mathcal O(x),1)\), with its trivialization away from \(x\), maps to \(c_1\mathcal O(x)\), whose trace is also one by the degree construction of §1. The forgetful map from this rank-one supported group to top cohomology is an isomorphism: the composite with trace sends its orientation generator to one. Thus the two supported classes are equal. Restrict to \(\mathbf A^1\) through an affine open containing \(x\); open localization and purity preserve this equality.

Near a point of \(D\), choose a normal parameter \(t\); after shrinking, \(t:X\to\mathbf A^1\) is smooth of relative dimension \(N-1\) and \(D=t^{-1}(0)\). Smooth base change for the complementary open direct image identifies the supported localization triangle with the pullback of the point triangle. This comparison also preserves the orientation defined by (11.5): writing \(i_0:\{0\}\hookrightarrow\mathbf A^1\) and \(h:D\to\{0\}\), the identity \(ti=i_0h\) gives \(Ri^!Rt^!=Rh^!Ri_0^!\). The two smooth formulas have the same twist \((N-1)\) and shift \([2N-2]\); canceling them gives the indicated supported comparison. Their composite counits agree by §8 and the trace composition proved in §2.

The Kummer class with support pulls back as well: the pair \((\mathcal O(D),1)\) is the pullback of the point's pair in the normal coordinate. The preceding point equality therefore proves equality of the two supported classes on these charts. Under purity the degree-two supported group is \(H^0(D,\Lambda)\), so equality on the charts proves equality globally. Forgetting support gives the asserted ordinary Chern class. This proof uses the positive class of \(\mathcal O(D)\) with its trivialization; it does not identify that class with an unsigned valuation-sequence boundary. \(\square\)

The construction commutes with étale localization. In the normal coordinate calculation it also commutes with transverse pullback: both local classes come from the pulled-back supported Kummer pair. These compatibilities are enough for the hyperplane and affine-space calculations below. No purity assertion for arbitrary singular closed subschemes has been used.

## 13. Perfect constant-coefficient complexes and products

One cannot in general replace the dual of a derived tensor by the tensor of its duals over \(\mathbf Z/n\). We prove the finite-projective property needed for constant coefficients.

**Lemma 13.1.** The complex \(A_X=R\Gamma_c(X,\Lambda)\) is perfect over \(\Lambda\): it has a bounded representative by finite projective modules, in degrees \([0,2N]\).

*Proof.* Its cohomology is finite and in that interval, by the earlier compact bound and finiteness input. For any module \(M\), the projection formula gives

\[
A_X\otimes^L_\Lambda M=R\Gamma_c(X,\underline M).
\tag{13.1}
\]

The right side has no negative cohomology and vanishes above \(2N\), since the compact bound applies to every \(\Lambda\)-sheaf. A bounded complex with finite cohomology over the Noetherian ring \(\Lambda\) admits a bounded-above resolution \(P\) by finite free modules: successively choose finite generators for the highest cohomology and the kernels of the maps already constructed. Noetherianity keeps each subsequent kernel finitely generated. We may take \(P^r=0\) for \(r>2N\).

Put \(Q=\operatorname{coker}(P^{-1}\to P^0)\). Since the negative cohomology of \(P\) vanishes, its nonpositive part is a free resolution of \(Q\). For every \(M\), (13.1) gives
\(\operatorname{Tor}_1^\Lambda(Q,M)=H^{-1}(P\otimes M)=0\).
Thus \(Q\) is flat, by the tensor criterion for flatness. It is finitely presented, so is projective. Replace the negative part of \(P\) by \(Q\) in degree zero. The resulting finite-projective complex, in degrees zero through \(2N\), is quasi-isomorphic to \(A_X\). \(\square\)

The same proof works for any separated finite-type variety when its constant coefficient is \(\Lambda\). It does not assert that \(R\Gamma_c(X,F)\) is perfect for a nonfree local system: already on a point, \(F=\mathbf Z/\ell\) over \(\mathbf Z/\ell^2\) is a counterexample.

**Lemma 13.2 (compact Künneth and trace).** For separated finite-type \(X,Y\),

\[
R\Gamma_c(X\times Y,\Lambda)
=A_X\otimes^L A_Y.
\tag{13.2}
\]

For smooth varieties of dimensions \(N,M\), the product trace is the tensor of their traces under the twisted version of (13.2).

*Proof.* Compact base change for \(\operatorname{pr}_1:X\times Y\to X\) identifies \(R\operatorname{pr}_{1,!}\Lambda\) with the constant complex \(\underline{R\Gamma_c(Y,\Lambda)}\). Apply composition and then the compact projection formula over the point to obtain (13.2). These maps are the external-product maps because both projection comparisons are defined by tensor and adjunction. For trace, factor the structure map of \(X\times Y\) as \(\operatorname{pr}_1\) followed by \(p_X\). The trace of \(\operatorname{pr}_1\) is the base change of the trace of \(p_Y\); composition compatibility gives the stated tensor trace. \(\square\)

Consequently duality for \(X\) and \(Y\), together with ordinary Künneth from the affine-vanishing chapter, proves constant-coefficient duality for their product. Here are the actual derived identifications:

\[
\begin{aligned}
&R\Gamma(X\times Y,\Lambda(N+M)[2N+2M])\\
&\quad=R\Gamma(X,\Lambda(N)[2N])\otimes^L
R\Gamma(Y,\Lambda(M)[2M])\\
&\quad=A_X^\vee\otimes^L A_Y^\vee\\
&\quad=(A_X\otimes^LA_Y)^\vee.
\end{aligned}
\tag{13.3}
\]

The last equality is valid by Lemma 13.1: on bounded finite-projective representatives it is the ordinary Hom–tensor identity with the graded signs. The first two comparisons are the factor Künneth and factor duality maps, so by Lemma 13.2 their composite is the product evaluation-and-trace map. This argument does not assume duality for the product in advance.

For classes \(a,b\) in compact degrees \(i,j\), and \(\alpha,\beta\) in the complementary ordinary degrees, the resulting value is

\[
(-1)^{j(2N-i)}
\operatorname{Tr}_X(a\cup\alpha)
\operatorname{Tr}_Y(b\cup\beta).
\tag{13.4}
\]

The sign moves \(b\) past \(\alpha\) before pairing the factors. For a composite \(n\), Tor contributions can still enter the cohomology of (13.2). The proof concerns derived complexes, so does not discard those terms.

## 14. Projective-space cohomology and the hyperplane generator

**Proposition 14.1.** Over an algebraically closed field with \(n\) invertible, the cohomology of \(\mathbf P^m\) is one free copy of \(\Lambda(-j)\) in each degree \(2j\), \(0\leq j\leq m\), and zero in every other degree. Its generator is \(h^j\), with \(h=c_1\mathcal O(1)\), retaining the indicated coefficient twist. The sum of these class maps is a derived decomposition

\[
\bigoplus_{j=0}^m\Lambda(-j)[-2j]
\xrightarrow{\sim}R\Gamma(\mathbf P^m,\Lambda).
\tag{14.1}
\]

*Proof.* The curve calculation gives \(R\Gamma_c(\mathbf A^1,\Lambda)=\Lambda(-1)[-2]\). To check the lower degrees, use compact localization in \(\mathbf P^1\): the map on degree-zero sections from \(\mathbf P^1\) to its single infinity point is an isomorphism, and the projective line has no degree-one cohomology. Thus the affine line has no compact cohomology in degrees zero and one. Its degree-two trace is (RC.19). Compact Künneth gives \(R\Gamma_c(\mathbf A^m,\Lambda)=\Lambda(-m)[-2m]\). The global smooth duality already proved in §10 therefore gives \(R\Gamma(\mathbf A^m,\Lambda)=\Lambda\) in degree zero.

Induct on \(m\), starting with a point. For the hyperplane \(i:\mathbf P^{m-1}\hookrightarrow\mathbf P^m\), purity and localization give

\[
R\Gamma(\mathbf P^{m-1},\Lambda(-1))[-2]
\longrightarrow R\Gamma(\mathbf P^m,\Lambda)
\longrightarrow R\Gamma(\mathbf A^m,\Lambda).
\tag{14.2}
\]

The restriction of the constant degree-zero section is an isomorphism. Since the last complex has no positive cohomology, the first map identifies every positive cohomology group with the hyperplane group shifted by two and twisted by \((-1)\); in degree one both groups are zero. Induction gives the asserted ranks and vanishings. Lemma 12.2 says \(i_*1=h\); the projection identity and \(i^*h=c_1\mathcal O_{\mathbf P^{m-1}}(1)\) show that the induction generator maps to \(h^j\). These actual class morphisms define (14.1), and the proved cohomology calculation makes it a quasi-isomorphism. No splitting of an arbitrary torsion cohomology complex has been assumed. \(\square\)

## 15. Sources and proof dependencies

P. Deligne, [*SGA 4*, Tome 3](https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf), Exposé XVIII, §§1.1,2–3, supplies the classical curve-to-trace construction and its smooth-duality application. The freely accessible French typesetting is dated 30 July 2024. The relative curve construction here uses actual chart morphisms and highest-degree descent; the smooth coordinate comparison retains smooth curve projections throughout. The degree-one normalization corrects the projective-line paragraph’s displayed degree-one typo to degree two.

Deligne, [*SGA 4½*](https://publications.ias.edu/sites/default/files/Number32.pdf), “Dualité,” §§2–4, supplies the comparison with the Artin curve argument, local concentration and adjunction. The exact preceding chapters named in the introduction supply the compact-support and curve foundations. The local proof in §§3–13 adapts their earlier CC0 companion exposition, with the previously stated trace input replaced by §§1–2 and the divisor-sign comparison replaced by the supported Kummer argument in Lemma 12.2. Free access to either primary PDF does not confer permission to copy its prose; no primary PDF prose is reproduced here.

The proved scope is smooth relative trace and duality, arbitrary pulled-back coefficient complexes, global smooth duality, smooth-pair purity and Gysin compatibility. Purity for arbitrary singular pairs and trace for general nonsmooth flat families are not used to establish these statements. The finiteness, constructibility, continuity and categorical foundations expressly identified in the introduction retain their stated status.
