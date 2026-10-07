# Supports, products and proper images of chains

To push a chain forward, control its closed support before integrating its oriented pieces. To multiply chains, keep their factor order before taking a boundary. These two rules make the same theory work with singular subanalytic supports, nonproper ambient maps and coefficients that are not fields.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

Subanalytic chains and closed cycle supports supplies the sheaves \(\mathcal C_p,\mathcal Z_p\), their support comparisons, boundary and softness. We use the programme's filtered colimits and stalkwise tensor products, and the SH-02 proper-support projection, exceptional trace and orientation lessons. M. Kashiwara's [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §1, supplies the oriented subanalytic chain model and its coefficient-sheaf formulation. Below we prove the flatness, support, trace and ordered-product statements needed to operate on that model.

## Finite subdivisions make chain stalks flat

Continue with a commutative ring \(A\) of finite global dimension and real analytic manifolds of uniformly finite dimension, Hausdorff and countable at infinity. Write

\[
 \mathcal C^{-p}=\mathcal C_p,\quad d^{-p}=\partial_p,\quad
 \mathcal Z_p=\ker(\partial_p).
 \qquad\text{(1)}
\]

Every stalk \((\mathcal C_p)_x\) is a filtered colimit of finite free \(A\)-modules. The finite modules describe finite subdivisions near the particular point; their ranks need not be uniformly bounded.

**Proof.** Represent finitely many germs on one relatively compact subanalytic neighborhood of \(x\). Choose a finite triangulation compatible with their pieces and with \(\{x\}\), shrink about \(x\), and orient the open \(p\)-cells. Delete lower-dimensional faces as in the directed comparison of chain representatives. Only cells whose closures contain \(x\) contribute germs. Their oriented chain germs generate a free module: if a finite linear combination vanishes near \(x\), test it in the interior of each contributing cell arbitrarily close to \(x\). The chain relations preserve this generic coefficient, so that coefficient is zero in \(A\). This uses no division and no assumption that \(A\) is a field.

A common compatible refinement on a smaller neighborhood contains the images of any two such finite free modules. Subdivision sends each oriented cell to the sum of its oriented subcells, discarding subcells whose closures miss \(x\). The generic-coefficient test makes this map injective. Equalities between two germ descriptions hold on a sufficiently small neighborhood and are detected on that common refinement; conversely the subdivision relations identify those descriptions. Thus these finite free submodules form a directed system with union the whole stalk. If \(p<0\) or exceeds the local ambient dimension, the stalk is zero, which is flat as well. \(\square\)

Tensoring a short exact sequence with these free modules is exact. Tensor commutes with filtered colimits, and filtered colimits of modules are exact. Consequently \(\mathcal C_p\) is flat. This argument does not prove that every stalk is finite free, and does not yet prove flatness of \(\mathcal Z_p\). For every sheaf \(F\),

\[
 \mathcal C_p\otimes_A^L F
 \simeq\mathcal C_p\otimes_A F=\mathcal C_p(F).
 \qquad\text{(2)}
\]

The cutoff extension proof makes \(\mathcal C_p(F)\) soft for every sheaf \(F\). A closed fibre inherits c-softness, so these sheaves are acyclic for proper direct image. Here \(f:Y\to X\) is analytic, \(\mathcal C_p=\mathcal C_p^Y\), and the coefficients in the following formula are a sheaf \(F\) on \(X\). The flat relative-soft tensor lemma and its fibrewise projection argument, (EX.12), give the underived isomorphism

\[
 f_!\mathcal C_p\otimes_A F
 \xrightarrow{\sim}
 f_!\bigl(\mathcal C_p\otimes_A f^{-1}F\bigr).
 \qquad\text{(3)}
\]

The arrow multiplies a properly supported section by a pulled-back local coefficient section. To prove it is an isomorphism, fix \(x\in X\), write \(E=\mathcal C_p|_{f^{-1}(x)}\), and consider \(M\mapsto\Gamma_c(f^{-1}(x);E\otimes_A M)\). Flatness of \(E\), the relative-soft tensor lemma and the finite cohomological dimension of the fibre make this functor exact. It preserves direct sums: a compact support meets only finitely many of the locally finite nonzero summands of a section. The comparison from \(\Gamma_c(E)\otimes_A M\) is an isomorphism on free modules, hence on every module by a free presentation. Its exactness also says that \(\Gamma_c(E)\) is flat. The proper-support stalk formula, and the identification of the coefficient sheaf on this fibre with the constant sheaf of value \(F_x\), now prove (3) and flatness of \(f_!\mathcal C_p\). Neither finite generation nor flatness of \(F_x\) enters this argument.

## Local systems give pure subanalytic supports

Let \(L\) be locally free of finite rank. A nonzero section
\(\alpha\in\Gamma(X;\mathcal C_p(L))\)
has a closed subanalytic support of pure dimension \(p\). The zero section has empty support.

**Proof.** Trivialize \(L\) near a point and use the finite cell refinement for all its finitely many coordinates. On an open \(p\)-cell the coefficient of the resulting chain is a locally constant vector, with its orientation sign. If that vector is nonzero, it stays nonzero throughout the connected cell; if zero, the cell contributes nothing. The support near the point is precisely the union of the closures of the nonzero \(p\)-cell pieces. A lower-dimensional germ cannot remain on its own: the chain presentation and ordinary orientation images determine it from arbitrarily nearby \(p\)-pieces. The finite local union is subanalytic, and every point of it is approached by \(p\)-dimensional pieces, proving purity. Closedness is part of the support definition. The local descriptions establish a closed subanalytic set globally, without requiring globally finitely many cells. \(\square\)

This assertion has a coefficient hypothesis. For arbitrary \(F\), a sheaf \(\mathcal C_p(F)\) can have sections supported on a set of smaller dimension or on a nonsubanalytic set. Exercise 1 checks the dimensional failure.

For a locally closed subanalytic \(S\) of dimension at most \(p\), set

\[
 T_S(L)=j_{S*}H^{-p}(\omega_S\otimes_A L|_S).
 \qquad\text{(4)}
\]

Here are the coefficient comparisons needed for supported chains. For any locally closed \(V\subset X\) and any relevant complex \(K\), the natural evaluation map \(R\mathcal Hom(A_V,K)\otimes_A L\to R\mathcal Hom(A_V,K\otimes_A L)\) is an isomorphism. Also \((Rj_{S*}\omega_S)\otimes_A L\to Rj_{S*}(\omega_S\otimes_A L|_S)\) is an isomorphism. On an open set where \(L=A^r\), both assertions are the commutation of the indicated additive derived functor with a finite direct sum. Evaluation defines the maps, so they agree under changes of basis and glue. This proves the supported internal-Hom assertion without replacing an internal Hom stalk by an unjustified Hom of stalks.

Since \(L\) is flat, taking the lowest cohomology commutes with tensoring by \(L\). Thus \(T_S(L)=T_S\otimes_A L\), and tensoring the kernel sequence for \(\partial\) gives \(\mathcal Z_p\otimes_A L=\ker(\mathcal C_p(L)\to\mathcal C_{p-1}(L))\). This is the notation \(\mathcal Z_p(L)\) used below. In particular the lowest-degree supported identity holds with these coefficients. Since \(\omega_S\otimes_A L|_S\) begins in degree \(-p\), the lowest-degree global calculation gives
\(\Gamma(X;T_S(L))=H^{-p}(S;\omega_S\otimes_A L|_S)\).

If \(S\) is **closed**, supported cycles satisfy

\[
 \Gamma_S(X;\mathcal Z_p(L))
 \simeq H^{-p}(S;\omega_S\otimes_A L|_S).
 \qquad\text{(5)}
\]

**Proof.** A germ of \(\mathcal Z_p(L)\) is represented on some closed \(S'\). The closed-support trace maps are injective, also after tensoring by flat \(L\). Thus, if its image in cycles is supported on \(S\), every off-\(S\) germ of the representative vanishes: enlargement cannot kill such a germ. The supported internal-Hom comparison just proved and the lowest-degree support identity identify the supported part with \(T_{S\cap S'}(L)\). Its closed trace to \(T_S(L)\) supplies the required representative. Conversely \(T_S(L)\) maps injectively into cycles and is supported on \(S\). Both maps are restrictions and closed traces, so they agree on overlaps, giving
\(H^0_S\mathcal Z_p(L)=T_S(L)\).
Taking global sections and using the lowest-degree identity proves (5). No interchange of arbitrary global sections or support functors with a filtered colimit is used. \(\square\)

For a **locally closed** \(S\), put \(B=\overline S\setminus S\). There is a more useful description:

\[
 \begin{split}
 H^{-p}(S;\omega_S\otimes_A L|_S)
 \simeq\{\,\alpha\in\Gamma_{\overline S}(X;\mathcal C_p(L)):
                    \operatorname{supp}(\partial\alpha)\subset B\,\}.
 \end{split}
 \qquad\text{(6)}
\]

The support condition is on \(\overline S\), so boundary germs are included.

**Proof.** The frontier triangle makes the boundary of a section of \(T_S(L)\) a cycle supported on \(B\). Its chain support is contained in \(\overline S\). This gives the forward map.

Conversely take a chain satisfying the right side. On \(O=X\setminus B\) it is a cycle supported on \(S\), which is closed in \(O\). Formula (5), in that open ambient manifold, identifies it with a section of \(H^{-p}(\omega_S\otimes L)\). Take the ordinary direct image of that section to \(X\). Its resulting chain agrees with the given chain on \(O\). Their difference is supported on \(B\), whose dimension is less than \(p\). The purity assertion for finite-rank \(L\) forces that difference to be zero. It also proves uniqueness. \(\square\)

This proof keeps both the closure in the chain support and the frontier in the boundary support.

## A global chain has an actual carrier

For finite-rank \(L\) the preceding descriptions prove

\[
 \begin{aligned}
 \Gamma(X;\mathcal C_p(L))
 &\simeq \underset{S\ \mathrm{locally\ closed},\ \dim S\leq p}
                     {\operatorname{colim}}
       H^{-p}(S;\omega_S\otimes L|_S),\\
 \Gamma(X;\mathcal Z_p(L))
 &\simeq \underset{S\ \mathrm{closed},\ \dim S\leq p}
                     {\operatorname{colim}}
       H^{-p}(S;\omega_S\otimes L|_S).
 \end{aligned}
 \qquad\text{(7)}
\]

Here the first comparison system uses the open-in-source, closed-in-target witnesses of the preceding lesson.

**Proof of representation and relations.** For a nonzero chain put
\(Z=\operatorname{supp}\alpha\) and \(D=\operatorname{supp}\partial\alpha\).
The boundary is local, so \(D\subset Z\). Purity makes \(Z\) a closed pure \(p\)-set and, unless the boundary is zero, \(D\) a closed pure \((p-1)\)-set. For \(p=0\), read \(D=\varnothing\). Set \(S=Z\setminus D\). Then
\(\overline S=Z\) and \(\partial S=D\):
a lower-dimensional closed subset cannot contain a relatively open piece of a pure \(p\)-set. Formula (6) represents \(\alpha\) on this single \(S\). A cycle instead has \(D=\varnothing\) and is represented on the closed \(Z\) by (5).

Suppose a section represented on a locally closed \(S'\) gives the zero chain. On a dense top regular refinement it has zero coefficients, so the comparison to that refinement is zero; this is already a relation in the first colimit. If two sections give the same chain, compare both to a common carrier refinement using their top regular pieces; their coefficient differences vanish there. On closed supports the transitions are injective, and a common closed union detects equality. This proves the colimit relations as well as surjectivity. The proof uses each chain's actual support, not a general rule that \(\Gamma\) commutes with sheaf colimits. \(\square\)

## Proper support makes the trace into a chain map

Let \(f:Y\to X\) be analytic. We construct

\[
 f_!\mathcal C^Y\longrightarrow\mathcal C^X.
 \qquad\text{(8)}
\]

Properness of \(f\) on all of \(Y\) is unnecessary. A section used in (8) must have support proper over the target open set.

For the untensored chain sheaves there is a correctly typed carrier description

\[
 f_!\mathcal C_p^Y
 \simeq \underset{S}{\operatorname{colim}}\,
        f_!j_{S*}H^{-p}\omega_S,
 \qquad f|_{\overline S}\ \mathrm{proper},\quad \dim S\leq p.
 \qquad\text{(9)}
\]

The terms on the right are sheaves on \(X\). To prove cofinality on stalks, let \(\alpha\) be a chain on \(f^{-1}U\) with closed support \(Z\) proper over a neighborhood \(U\) of \(x\). Choose a relatively compact subanalytic open \(O\) with \(x\in O\subset\overline O\subset U\). Apply the actual chain cutoff \(P_{f^{-1}O}\) from the preceding lesson. The result agrees with \(\alpha\) over \(O\), and its support is contained in \(Z\cap f^{-1}\overline O\). This last set is compact by the assumed properness. The cut chain therefore extends by zero from \(f^{-1}U\) to \(Y\), and (7) represents it on a global carrier whose closure is compact. Such a carrier is one of the indices in (9). This cutoff is used degree by degree; it need not commute with the boundary.

Conversely a section on a carrier with proper closure has support proper over its target domain. To compare two representatives of the same germ, shrink in the target until their chain sections agree and make a common carrier refinement there. The closure of the refinement is contained in the finite union of the original proper closures; a closed subset of that union is again proper. The relations in (7) therefore hold within the system in (9). This proves surjectivity and injectivity on stalks, hence (9), without exchanging an arbitrary direct image with a colimit. It permits noncompact carriers globally: compactness was used only to choose representatives near a target point.

Take such an \(S\), with \(T=\overline S\) and \(B=T\setminus S\). Put

\[
 K=f(T),\qquad C=f(B),\qquad V=K\setminus C=f(S)\setminus f(B).
 \qquad\text{(10)}
\]

Properness makes \(K,C\) closed subanalytic. We have \(\dim K\leq p\) and \(\dim C<p\); \(V\) is locally closed. Over \(V\),
\(S_0=T\cap f^{-1}V=S\cap f^{-1}V\)
is proper over \(V\). The exceptional-composition trace is
\[
 R(f_V)_!\omega_{S_0}\longrightarrow\omega_V.
 \qquad\text{(11)}
\]

For any left exact sheaf functor \(P\) and any complex \(E\in D^{\geq -p}\), the lowest-degree comparison is \(H^{-p}(RP(E))=P(H^{-p}E)\); this follows by applying \(RP\) to the lowest truncation triangle. Apply it to \(P=(f_V)_!\), using the lower bound \(\omega_{S_0}\in D^{\geq -p}\), and to the ordinary images of the carriers. Thus degree \(-p\) of (11) is the actual sheaf map \((f_V)_!H^{-p}\omega_{S_0}\to H^{-p}\omega_V\). Restrict the orientation section on \(S\) to the open subset \(S_0\), apply that map, and take ordinary direct image from \(V\) to \(X\). This is a section of \(T_V\), hence an \(X\)-chain. The trace in (11) is the exceptional-composition counit (EX.14). If the image has dimension less than \(p\), its degree-\(-p\) dualizing sheaf is zero, so this construction sends the chain to zero.

The map commutes with the boundary:

\[
 \partial f_*\alpha=f_*(\partial\alpha).
 \qquad\text{(12)}
\]

**Proof with the actual localization maps.** Regard \(f\) here as the proper map \(T\to K\). All constant sheaves on subsets in this paragraph are extended by zero in the indicated ambient space. Pull back the coefficient triangle \(A_V\to A_K\to A_C\to A_V[1]\) to \(T\). Its open and closed parts are \(f^{-1}V\) and \(f^{-1}C\). It maps to \(A_S\to A_T\to A_B\to A_S[1]\): the first map extends from \(f^{-1}V\subset S\), the middle is the identity, and the third restricts from \(f^{-1}C\) to \(B\). These maps commute already on the coefficient sheaves. Applying the unit of \(f^{-1}\dashv Rf_*\), followed by this triangle map, gives a morphism from the coefficient triangle on \(K\) to its counterpart \(Rf_*A_S\to Rf_*A_T\to Rf_*A_B\to\). Properness identifies \(Rf_*\) with \(Rf_!\) here.

Dualize that morphism of triangles with \(D_K=R\mathcal Hom(-,\omega_K)\). The internal exceptional adjunction (EX.20) and exceptional composition give \(D_KRf_!H\simeq Rf_*D_TH=Rf_!D_TH\) for each bounded coefficient object \(H\) used here. Its hypotheses are met: the coefficient sheaves are in degree zero, proper direct image has the finite dimension bound, and the dualizing target is bounded below. Dualizing an open extension gives ordinary image of its dualizing object, whereas dualizing a closed extension gives its closed dualizing image. With the usual coherent rotation of the dual localization triangles, the dual of the coefficient-unit map is the exceptional trace. The counit normalization commutes with shifts, so the last vertical arrow is the shifted trace without an independently chosen sign. We obtain
\[
 \begin{array}{ccccc}
 Rf_!\omega_B&\longrightarrow&Rf_!\omega_T&
       \longrightarrow&Rf_!Rj_{S*}\omega_S\longrightarrow Rf_!\omega_B[1]\\
 \downarrow&&\downarrow&&\downarrow\hspace{4.5em}\downarrow\\
 \omega_C&\longrightarrow&\omega_K&
       \longrightarrow&Rj_{V*}\omega_V\longrightarrow\omega_C[1].
 \end{array}
 \qquad\text{(13)}
\]
Push the closed-support objects to the indicated ambient spaces. The rightmost unshifted map is exactly restriction and (11), by the adjunction defining it; it is not a separately chosen cone map. The shifted arrow is the trace on \(B\to C\). The bottom closed set \(C\) can enlarge the actual frontier of \(V\); its extra lower-dimensional pieces do not change the degree-\(-p\) chain term.

Taking the connecting maps out of degree \(-p\) in (13) gives precisely (12). The bounds
\(\omega_B,\omega_C\in D^{\geq1-p}\)
identify degree \(1-p\) of their proper images with the images of the cycle sheaves used for the boundary. Closed-support enlargement preserves those cycles. Restriction and closed trace are natural, so the same diagram shows independence of carrier and compatibility with the comparisons in (9). This proves (8). \(\square\)

Identity maps give identity images. For \(Z\xrightarrow{g}Y\xrightarrow{f}X\), suppose \(g\) is proper on the source support and \(f\) is proper on its image. The composite is then proper there. Exceptional composition says that the trace for \(fg\) is the successive trace for \(g\) and \(f\), with the associativity proved in (EX.14). To compare the carrier formulas, remove the images of their frontiers and the lower-dimensional pieces on which the chosen restrictions differ. On the remaining common top-dimensional parts, open restriction and the trace composition give the same coefficient. The difference of the two output \(p\)-chains is therefore supported on a set of dimension less than \(p\), and the pure-support result makes it zero. This also covers a dimension drop, when both top-degree images vanish. Thus composition holds for the actual maps, including noncompact proper supports.

For any sheaf \(F\) on \(X\), (3) extends (8) to a chain map

\[
 f_!\mathcal C^Y(f^{-1}F)\longrightarrow\mathcal C^X(F).
 \qquad\text{(14)}
\]

Use the inverse of (3), followed by (8) tensored with \(F\), in each degree. Multiplication by pulled-back coefficients commutes with every morphism of the flat chain sheaves, in particular their boundary maps. Hence this is a chain map; the same naturality and the associativity of multiplication prove its compatibility with identity maps and composition. The argument does not assign a subanalytic carrier to a section with arbitrary coefficients, whose support can be nonsubanalytic. Proper support is the support condition in \(f_!\); (3) reduces the construction to the already defined untensored map. All terms are flat before tensoring and soft afterwards. No local freeness or perfection of \(F\) is required. We call the image of such a section \(f_*\alpha\).

## Products retain the geometric and cohomological order

For locally closed carriers \(S\subset X,T\subset Y\), the exceptional tensor and composition maps give a dualizing product

\[
 \omega_S\boxtimes^L\omega_T\longrightarrow\omega_{S\times T}.
 \qquad\text{(15)}
\]

Write \(a:S\to\mathrm{pt}\), \(b:T\to\mathrm{pt}\) and \(c:S\times T\to\mathrm{pt}\). Proper-support base change, composition and the projection formula (EX.11) identify \(Rc_!(\omega_S\boxtimes^L\omega_T)\) with \(Ra_!\omega_S\otimes_A^L Rb_!\omega_T\), in that order. Compose with the two counits to \(A\otimes_A^L A=A\). Its adjoint under \(Rc_!\dashv c^!\) is (15). This defines its normalization and its compatibility with open restriction, closed trace and iterated products; the relevant transposes are the same successive counits. We need this map, without asserting its invertibility for arbitrary singular carriers.

The passage to lowest classes also works over a ring. Put \(M=H^{-p}\omega_S\) and \(N=H^{-q}\omega_T\). The lower bounds on the two dualizing objects give canonical truncation maps \(M[p]\to\omega_S\) and \(N[q]\to\omega_T\). Tensor them in the derived category and compose with (15). Taking degree \(-p-q\) identifies the source with \(H^0(M\boxtimes^L N)=M\boxtimes N\), and gives the desired product into \(H^{-p-q}\omega_{S\times T}\). Lower Tor groups may occur in the derived tensor; this argument makes no claim that they vanish. Ordinary image of the two orientation sections produces a chain on \(S\times T\). Refinement and the trace compatibilities just proved make this independent of carriers. Finally tensor local sections with the degree-zero coefficients of \(F\) and \(G\), moving only those degree-zero factors through the chain terms. Bilinearity and the sheaf tensor relations give

\[
 \mathcal C^X(F)\boxtimes\mathcal C^Y(G)
 \longrightarrow\mathcal C^{X\times Y}(F\boxtimes G).
 \qquad\text{(16)}
\]

On oriented smooth pieces this is the ordered product orientation, first the \(X\)-coordinates and then the \(Y\)-coordinates. Indeed the ordered compact-support generators (M6), paired with their duals, make the increasing-interval trace equal to \(+1\); iterating those traces gives precisely the counit defining (15). The coefficient factors \(F,G\) have degree zero. Their ordinary tensor product in (16) does not assume that either coefficient sheaf is flat.

For \(\alpha\) of geometric degree \(p\) and \(\beta\) of degree \(q\),

\[
 \partial(\alpha\boxtimes\beta)
  =(\partial\alpha)\boxtimes\beta
       +(-1)^p\alpha\boxtimes(\partial\beta).
 \qquad\text{(17)}
\]

**Proof of the sign and map compatibility.** The oriented-simplex boundary calculation identifies the frontier connecting map with the outward-normal-first incidence map: the interval calculation is terminal endpoint minus initial endpoint, and a product collar tensors it with the ordered face orientation. On a product of oriented \(p\)- and \(q\)-cells, a face from the first factor already has its outward normal before both tangent-coordinate lists and has its first-factor incidence sign. For a face from the second factor, move that normal past the \(p\) coordinates of the first factor; the additional sign is \((-1)^p\).

Triangulate a product cell compatibly with its faces. The two incidences of each interior codimension-one face have opposite induced orientations and cancel over \(A\), including in characteristic two. The surviving faces therefore give (17). This computes the maps defined above: the collar connecting maps are the dual localization maps, and the transpose defining (15) is their ordered product of traces. A finite compatible refinement reduces any finite collection of chain germs to these calculations; the defining subdivision and orientation relations preserve them. Higher-codimension corners support no independent \((p+q-1)\)-chain. Thus the identity holds for all untensored chains. Every germ with coefficients is a finite sum of chain germs tensored with coefficient germs, so tensoring this equality with degree-zero coefficients proves it for arbitrary \(F,G\). \(\square\)

Equation (17) is also the tensor-complex sign, because \((-1)^{-p}=(-1)^p\). It proves that (16) is a map of complexes and that a product of cycles is a cycle. The factor-exchange diffeomorphism satisfies
\[
 \tau_*(\alpha\boxtimes\beta)=(-1)^{pq}\beta\boxtimes\alpha.
 \qquad\text{(18)}
\]
Moving the \(p\) coordinates through the \(q\) coordinates proves this sign; it is the Koszul sign in degrees \(-p,-q\). Associativity follows because both parenthesizations have the orientation order \(X,Y,Z\) and their transposes are the same three counits. If two maps are proper on their respective source supports, their product is proper on the product of those supports: the preimage of a compact target set is closed in the product of the two compact preimages of its projections. The proper image of the product and the product of the proper images have the same transpose, the ordered product of the two traces. This proves compatibility of the actual product and pushforward maps. The coefficient projection maps preserve these equalities by their sectionwise multiplication rule.

## A strip homotopy gives a supported boundary

For two \(p\)-cycles \(\gamma_0,\gamma_1\) on \(X\), a chain homotopy in this sense consists of
\[
 t\in\Gamma_{X\times[0,1]}(X\times\mathbb R;\mathcal C_{p+1}),
 \qquad
 \partial t=i_{0*}\gamma_0-i_{1*}\gamma_1,
 \qquad\text{(19)}
\]
where \(i_s(x)=(x,s)\). The endpoint order is the convention in (19).

Projection \(q:X\times\mathbb R\to X\) is proper on the closed support of \(t\): over a compact \(K\subset X\), that support is closed in the compact \(K\times[0,1]\). Its image \(D=q(\operatorname{supp}t)\) is closed. Apply (12) and the identity \(qi_s=\mathrm{id}\) to get
\[
 \partial(q_*t)=\gamma_0-\gamma_1.
 \qquad\text{(20)}
\]

The chain \(q_*t\) is supported on \(D\). Both endpoint cycles are supported there too: outside \(D\), the chain \(t\) vanishes over the corresponding target open set, so its boundary vanishes; the two terms in (19) lie on disjoint endpoint slices and must vanish separately. Thus (20) is a boundary equality inside \(\Gamma_D(X;\mathcal C)\), proving that the two cycles have the same class in
\(H^{-p}(\Gamma_D(X;\mathcal C))\),
or in degree \(p\) with homological indexing. Neither \(X\) nor \(D\) must be compact. The compact interval ensures properness in the parameter direction. The same argument works with coefficients pulled back from \(X\), using (14).

For comparison, if \(I\) is the interval chain oriented from \(0\) to \(1\), then
\(\partial(\gamma\boxtimes I)=(-1)^p(i_{1*}\gamma-i_{0*}\gamma)\).
The chain \((-1)^{p+1}\gamma\boxtimes I\) satisfies (19) for the constant homotopy. This keeps the endpoint convention separate from the orientation chosen on the parameter interval.

These operations yield the local half-ray contraction used to identify the chain complex with \(\omega_X\). In that contraction the addition map must be proper on the selected carrier, just as projection was proper on the strip support here. Chain-stalk flatness, trace, product and boundary compatibility supply the operations needed for that argument.

## Exercises with complete solutions

### Pure support needs the local-system hypothesis

*Difficulty: Intermediate.*

Let \(F=i_*(\mathbb Z/5)\) on \(\mathbb R\), supported at zero, and let \(p=1\). Exhibit a nonzero section of \(\mathcal C_1(F)\) with zero-dimensional support. Why does it not contradict the pure-support theorem? Explain what flatness does and does not imply here.

**Solution.** The left and right interval germs give
\((\mathcal C_1)_0=\mathbb Z^2\), so
\(\mathcal C_1(F)\) is the skyscraper with stalk \((\mathbb Z/5)^2\).
The global element \((1,0)\) is nonzero and has support \(\{0\}\), not a pure one-dimensional set. The coefficient sheaf is not locally free on the ambient line, so the pure-support theorem does not apply.

Chain-stalk flatness says that ordinary tensor with \(\mathcal C_1\) computes derived tensor and preserves short exact coefficient sequences. It does not say that tensoring preserves the geometric support dimension. The boundary of this section is \(1\in\mathbb Z/5\) at zero by the map \((a,b)\mapsto a-b\). The element \((1,1)\) is instead a cycle, still with the same zero-dimensional support. The later general coefficient-kernel theorem will include such cycles without imposing a pure-support statement on them.

### The closure in a locally closed carrier cannot be omitted

*Difficulty: Intermediate.*

Take the positive interval chain on \(S=(0,2)\subset\mathbb R\). Use (6) to locate its support and boundary. Can the right side of (6) be replaced by chains supported on \(S\) itself? Repeat with \(S=\mathbb R\setminus\{0\}\) and different weights on its two components.

**Solution.** Ordinary direct image of the orientation coefficient from \((0,2)\) has nonzero endpoint germs. The chain is supported on \([0,2]\), with boundary \([2]-[0]\). Thus it is on the right side of (6) with \(\overline S=[0,2]\) and frontier \(\{0,2\}\). It is not supported on the open \(S\), so removing the closure would discard the chain corresponding to the constant nonzero orientation section.

For the punctured line choose rightward weights \(a_-\) and \(a_+\). Its closure is all of \(\mathbb R\), its frontier is \(\{0\}\), and its boundary is
\((a_- -a_+)[0]\).
Every pair belongs to (6). Only the diagonal pairs are cycles. Ordinary image retains two independent germs at the deleted point; imposing closed cycle support on the unpunctured line imposes equality of the two coefficients.

### A nonproper projection can carry an unbounded proper chain

*Difficulty: Intermediate.*

Let \(f:\mathbb R^2\to\mathbb R\), \(f(x,y)=x\), and orient the parabola \(P=\{(s,s^2):s\in\mathbb R\}\) by increasing \(s\). Compute \(f_*[P]\). Compare the hyperbola \(H=\{(s,1/s):s>0\}\), with its parameter orientation. Is its closed carrier proper over \(\mathbb R\)?

**Solution.** The projection is not proper on the plane: a vertical fibre is unbounded. On the closed parabola it is a homeomorphism with inverse \(s\mapsto(s,s^2)\). The inverse image of a compact set is compact, so its restriction is proper despite the unbounded carrier. It preserves the chosen one-dimensional orientation. The normalized trace therefore gives \(f_*[P]=[\mathbb R]\), with zero boundary on both sides.

The positive hyperbola branch is closed in \(\mathbb R^2\): sequences with \(s\to0\) escape to infinity and have no finite limit there. It is nevertheless not proper over the target. Its part over the compact interval \([0,1]\) contains \((1/r,r)\) and is unbounded. Thus the hyperbola chain does not define a section in the domain of the global pushforward (8). The fact that its image is the familiar open ray does not repair missing properness of its carrier.

### A fold cancels oriented one-chains but preserves point weights

*Difficulty: Intermediate.*

For \(f:\mathbb R\to\mathbb R\), \(f(s)=s^2\), use the positive coordinate orientations to compute the images of the whole-line chain, the positive-ray chain and a point at \(s=-2\). Check (12) for the ray. Compare the reflection \(r(s)=-s\).

**Solution.** The square map is proper. Away from its critical value zero, the positive branch preserves orientation and the negative branch reverses it. Thus the whole-line chain has image coefficient \(1-1=0\) on the positive target ray, and zero elsewhere. A one-chain cannot have an isolated nonzero germ at zero; its whole pushforward is zero.

The rightward positive-ray chain \([(0,\infty)]\), with closed support \([0,\infty)\), has image the same rightward ray. Its boundary is \(-[0]\), and \(f_*[0]=[0]\). Both sides of (12) are therefore \(-[0]\). The point \([-2]\) maps to \([4]\) with coefficient \(+1\): zero-dimensional orientation has no derivative sign. Reflection sends the positively oriented whole line to its negative, but sends each point to its reflected point with its coefficient unchanged. The one-dimensional orientation degree and the zero-dimensional point weight are different calculations.

### Product faces and the strip sign

*Difficulty: Advanced.*

Let \(I=[0,1]\) and \(J=[0,2]\) denote their rightward interval chains, including ordinary-image boundary germs. Give the four oriented boundary edges of \(I\boxtimes J\), check the next boundary is zero, and compute the effect of exchanging the factors. For a \(p\)-cycle \(\gamma\), determine the sign of the constant strip chain that satisfies (19).

**Solution.** By (17),
\[
 \partial(I\boxtimes J)
  =[1]\boxtimes J-[0]\boxtimes J
      -I\boxtimes[2]+I\boxtimes[0].
 \qquad\text{(21)}
\]
The right edge points up, the left edge down, the upper edge left and the lower edge right. Taking another boundary yields
\[
 ([1,2]-[1,0])-([0,2]-[0,0])
   -([1,2]-[0,2])+([1,0]-[0,0])=0.
 \qquad\text{(22)}
\]
Every corner has two opposite contributions. Over characteristic two the minus signs become plus signs and each corner occurs twice, still zero. Factor exchange reverses the two-dimensional product orientation, so its image is \(-J\boxtimes I\), as \((-1)^{1\cdot1}=-1\).

For the strip with parameter oriented upwards,
\(\partial(\gamma\boxtimes[0,1])=(-1)^p(i_{1*}\gamma-i_{0*}\gamma)\).
Multiplying it by \((-1)^{p+1}\) gives exactly the endpoint order in (19). Projection of that signed strip is a valid pushforward because its support is closed in the compact-parameter strip, even if \(\gamma\) has noncompact support.

### A translation of an unbounded zero-cycle has a proper strip

*Difficulty: Advanced.*

On \(\mathbb R\), let
\(\gamma_0=\sum_{m\in\mathbb Z}[m]\) and
\(\gamma_1=\sum_{m\in\mathbb Z}[m+\tfrac12]\).
Construct a chain \(t\) in \(\mathbb R_x\times\mathbb R_u\) satisfying (19) for \(p=0\), and compute \(q_*t\). Verify properness and its boundary without assuming compact support.

**Solution.** For each integer \(m\), take the segment
\(u\mapsto(m+u/2,u)\), \(0\leq u\leq1\), oriented in the direction of increasing \(u\), and let \(t\) be the negative of their sum. The family is locally finite and consists of subanalytic pieces; hence it gives a sheafified one-chain with closed support in \(\mathbb R\times[0,1]\). Its boundary is the starting endpoint minus the finishing endpoint on every segment, so
\(\partial t=i_{0*}\gamma_0-i_{1*}\gamma_1\).

The support over a compact target interval meets only finitely many segments and is closed in that interval times \([0,1]\). Projection is therefore proper on it. Each segment projects with increasing coordinate orientation, so
\[
 q_*t=-\sum_{m\in\mathbb Z}[(m,m+\tfrac12)],
 \quad
 \partial(q_*t)=\sum_m([m]-[m+\tfrac12])=\gamma_0-\gamma_1.
 \qquad\text{(23)}
\]
The projected closed support is the locally finite union of the intervals \([m,m+\tfrac12]\), which is noncompact. Every equality holds locally with finitely many terms, so no convergence of an infinite scalar sum is required. This proves equality of the two cycle classes in the supported chain complex on that closed set, using properness in the parameter direction rather than compactness of the whole cycle.

## Sources and mathematical credit

Masaki Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §1.3–1.5, pp. 195–196, introduces the oriented subanalytic chain model and its coefficient-sheaf version. The finite-refinement flatness proof, proper-carrier trace construction, ordered-product boundary calculation and six examples above develop the operations on that model. In particular, the compact parameter of a strip controls properness even when its chain support is unbounded.

Pierre Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), edition dated 01/08/2026, supplies the projection formula in Theorem 4.4.7 (p. 91), proper-support base change in Theorem 4.5.3 (p. 93), and exceptional composition and internal adjunction in §4.6 (pp. 95–96). The programme proofs linked above fix the evaluated section maps, counits and factor order. The underived coefficient projection is proved here on fibres; arbitrary coefficient sheaves are handled by that map, without assigning them pure-dimensional subanalytic supports.
