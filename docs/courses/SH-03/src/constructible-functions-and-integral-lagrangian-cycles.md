# Constructible functions and integral Lagrangian cycles

*Original programme exposition, examples and solutions are dedicated to the public domain under CC0.*

A characteristic cycle remembers exactly the Grothendieck class of a constructible complex. Equivalently, it remembers the complex's local Euler function. The correspondence does not identify sheaf objects: monodromy, individual cohomology groups and cancellation between shifts can disappear. This lesson proves the complete correspondence and constructs its inverse through local intersections with positive-Hessian graphs.

The characteristic-cycle and local-index theory is due to Kashiwara; see his [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque **130** (1985), 193–209. P. Schapira's [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf) (1991), Theorem 3.4 and Remark 3.6, pp. 88–90, states Kashiwara's correspondence between Grothendieck classes, constructible functions and Lagrangian cycles. The argument below supplies its dimension induction and local-intersection inverse in the programme's fixed orientation convention. The Grothendieck correspondence supplies the constructible-function realization and its injectivity, including noncompact manifolds and locally infinite strata. The integer-coefficient lesson proves the integral chain lift, the actual local constant model, and the coefficient functor for a whole triangle. The conormal orientation comparison fixes the tangential sign of the normalized generator. The geometric input is generic conormality along any subanalytic base. The local index input is the strict-minimum stalk formula, with its specified shrinking restrictions. The cycle-support and dilation theorem and closed-support chain construction fix the support and orientation conventions used below.

We use compatible locally finite subanalytic stratifications, the local finite-component theorem and the subanalytic dimension theorem. These geometric prerequisites allow arbitrary locally finite decompositions; a global finite stratification is not assumed.

## The three groups and their coefficients

Let \(X\) be real analytic, Hausdorff and countable at infinity, with a uniform finite dimension bound. Work on a component of dimension \(n\); differing component dimensions are handled separately. Fix a field \(k\) of characteristic zero, and let
\[
\mathcal D(X)=D^b_{\mathrm{rc}}(X;k),\qquad
K_0(X)=K_0(\mathcal D(X)).
\qquad\text{(1)}
\]
Objects have one global bounded cohomological range and finite constructible stalk cohomology. Stalk ranks may be unbounded over all of \(X\). All supports below are closed supports.

Write \(\pi:T^*X\to X\). The integral coefficient of a cotangent cycle is
\[
B_{\mathbb Z}=\operatorname{or}_{T^*X/X,\mathbb Z}.
\qquad\text{(2)}
\]
It is the orientation sign line of the \(n\)-dimensional cotangent fibre. Let \(\mathcal Z_n(B_{\mathbb Z})\) be the sheaf of subanalytic \(n\)-cycles with this coefficient. The sheaf \(\mathcal L_{X,\mathbb Z}\) consists of cycles carried, locally, by closed positive-conic subanalytic isotropic subsets of \(T^*X\). Isotropy means vanishing of the canonical one-form on the regular pieces, with its singular point-cone interpretation.

The chain model identifies this as the allowed-support subsheaf of \(\mathcal Z_n(B_{\mathbb Z})\). Its sections have finite chain descriptions near each point; no global finite number of pieces is required. Put
\[
LC(X)=\Gamma(T^*X;\mathcal L_{X,\mathbb Z}).
\qquad\text{(3)}
\]
The actual support of a section is itself a closed conic subanalytic isotropic set. To justify this from the sheaf definition, first work near one cotangent point on one allowed carrier. A finite compatible subdivision and the rank-one coefficient line describe the cycle by its coefficients on regular \(n\)-pieces. The closures of its nonzero pieces give its closed subanalytic support; if nonempty, this support is pure of dimension \(n\). It inherits canonical-form vanishing from the carrier. On a smaller neighborhood, every sufficiently short positive scaling path stays in the original representative neighborhood. Scaling preserves the carrier and its regular pieces, transports their orientation continuously from the identity, and acts positively on the fibre sign line. The locally constant cycle coefficient therefore agrees with its transported coefficient on those regular pieces. Their difference is a cycle carried on a set of dimension less than \(n\), and hence is zero by the top-chain support theorem. This proves the equality at frontier and singular points as well. Chaining these short paths along the connected positive scaling orbit propagates vanishing and nonvanishing. The full ambient cotangent bundle contains the entire orbit, so the actual support is positive-conic. Subanalyticity and isotropy are local, so they hold globally. This argument uses local carrier representatives and does not commute global sections with a sheaf colimit.

The integral characteristic-cycle construction and additivity give
\[
CC_{\mathbb Z}:K_0(X)\longrightarrow LC(X).
\qquad\text{(4)}
\]
Here the integer lift is a chain statement, not an assumption that a homology group has no torsion. On a dense regular conormal model, a perfect coefficient complex \(V\) on a smooth base \(Z\) contributes the integer \((-1)^{\dim Z}\chi(V)\) to the graph-normalized integral conormal generator. After a locally finite compatible refinement, these integers specify an integral top chain. Coefficient extension from \(\mathbb Z\) to \(k\) is injective on the chain group in every degree: it is the coefficientwise injection on each oriented cell, with the same integral boundary incidence numbers. The boundary of this integral top chain maps to the zero boundary of the field characteristic cycle, so injectivity in the boundary degree makes the integral boundary zero. This proves existence and uniqueness through every frontier, independently of the refinement. For a localized distinguished triangle, use the same microlocal coefficient functor on all three terms and its actual connecting map. The resulting triangle of perfect coefficient complexes has additive Euler characteristic. Its shared factor \((-1)^{\dim Z}\) is the same on the three conormal models. Equality on the dense regular pieces determines the full cycles, giving
\[
CC_{\mathbb Z}(F)=CC_{\mathbb Z}(F')+CC_{\mathbb Z}(F''),
\qquad CC_{\mathbb Z}(F[r])=(-1)^rCC_{\mathbb Z}(F).
\qquad\text{(5)}
\]
The full construction of the finite coefficient model, chain injection, frontier extension and triangle comparison is supplied in the linked integer-coefficient lesson. Equation (5) verifies every defining Grothendieck relation, hence proves (4).

The third group is \(CF(X)\), integer valued functions with locally finite subanalytic level partition. The preceding function lesson proved the ring bijection
\[
\chi:K_0(X)\xrightarrow{\ \sim\ }CF(X),\qquad
\chi F(x)=\sum_q(-1)^q\dim_k H^q(F)_x.
\qquad\text{(6)}
\]
The result retains arbitrary locally infinite stratifications through actual bounded sheaf realizations and finitely many skeleton triangles.

## A cycle over a smooth base has one integer coefficient

Let \(Y\subset U\) be a closed analytic embedded submanifold of an analytic open subset \(U\subset X\). Its full conormal \(N=T_Y^*U\) is a smooth \(n\)-manifold. A top cycle with closed support contained in \(N\) is a section of
\[
\operatorname{or}_{N,\mathbb Z}\otimes B_{\mathbb Z}|_N.
\qquad\text{(7)}
\]
Indeed the lowest-dualizing/top-cycle comparison on the closed smooth support identifies cycles with that sheaf. One can also see it from a local oriented subdivision: the zero boundary condition across each codimension-one face equates the coefficients of the adjacent top cells. They consequently give a locally constant orientation coefficient, including where the cycle itself vanishes.

The graph-normalized conormal cycle \([T_Y^*U]\) canonically trivializes the sign line in (7). In this normalization the sheaf \(k_Y\) has characteristic cycle \((-1)^{\dim Y}[T_Y^*U]\). The two generators agree only in even base dimension. To see why the sign line is trivial without orienting \(Y\), split locally
\[
TU|_Y\simeq TY\oplus N_{Y/U}.
\]
The tangent orientation of the conormal total space has tangential factor \(\operatorname{or}_{TY}\) and normal-dual factor \(\operatorname{or}_{N_{Y/U}^*}\). The cotangent fibre coefficient restricts to the product of their dual tangential and normal orientation lines. A tangential or normal frame reversal occurs twice in their tensor product, so the sign monodromy cancels. This establishes triviality; the graph trace fixes which of the two primitive integral generators is \([T_Y^*U]\). In a tangential model its zero-section factor is \((-1)^{\dim Y}\) times the positive tangent-fibre point unit, while the closed normal factor is the primitive point-conormal unit. Consequently the finite coefficient sheaf has the extra \((-1)^{\dim Y}\) in (9). The frame cancellation makes this convention global on a nonorientable base.

Every conormal fibre is a connected vector space, including its zero vector. Since a coefficient section in (7) is locally constant, it is constant on the entire fibre. Along a base component it is also constant. Thus every such cycle has the form
\[
\lambda=m_Y[T_Y^*U],
\qquad\text{(8)}
\]
where \(m_Y:Y\to\mathbb Z\) is locally constant. If a component's integer is nonzero, its whole conormal fibre occurs in the cycle support. A half-fibre with a nonzero uncancelled boundary cannot itself be a cycle on this smooth conormal manifold.

The local conormal coefficient theorem gives, for any bounded locally constant finite coefficient complex \(A\) on \(Y\),
\[
CC_{\mathbb Z}(i_*A)
=(-1)^{\dim Y}\left(\sum_q(-1)^q\operatorname{rank}H^q(A)\right)[T_Y^*U].
\qquad\text{(9)}
\]
For completeness, take a sufficiently small contractible analytic ball \(B\subset Y\) on which all \(H^q(A)\) are constant. These finitely many local systems have no higher cohomology on \(B\). The hypercohomology spectral sequence therefore gives \(H^q(R\Gamma(B;A))\simeq\Gamma(B;H^q(A))\). Put \(V=R\Gamma(B;A)\), a bounded finite-dimensional complex. The constant-section counit \(a_B^{-1}V\to A|_B\) induces the usual constant-section identification on each cohomology stalk and is consequently a quasi-isomorphism. The normalized closed-conormal trace for this actual model is \((-1)^{\dim Y}\chi(V)[T_B^*U]\), with the orientation just fixed. Restriction of that trace agrees on overlapping balls; gluing proves (9) with the locally constant Euler rank of \(A\). Nothing here trivializes monodromy around the whole of \(Y\).

## Closed conicity makes the base projection controlled

Let \(\lambda\in LC(X)\), and let \(\Lambda=\operatorname{supp}\lambda\). The zero cycle is realized by the zero object, so assume \(\Lambda\ne\varnothing\). Its base projection satisfies
\[
S=\pi(\Lambda)=\{x:(x;0)\in\Lambda\}.
\qquad\text{(10)}
\]
If \((x;\xi)\in\Lambda\), every \((x;t\xi)\), \(t>0\), lies there. Letting \(t\) tend to zero and using closedness puts \((x;0)\) in \(\Lambda\). The converse is immediate. Therefore \(S\) is closed and subanalytic, by inverse image under the analytic zero section. This proves the needed projection statement without assuming the bundle projection proper. Write \(d=\dim S\leq n\).

Apply the generic conormal theorem to the closed conic isotropic \(\Lambda\) and the subanalytic base \(S\). Retain only its dimension-\(d\) generic regular part \(Y\). The dimension theorem and removal of the subanalytic critical values give
\[
Y\subset S\text{ open},\qquad
R=S\setminus Y\text{ closed subanalytic},\qquad
\dim R<d,\qquad
\Lambda\cap\pi^{-1}Y\subset T_Y^*X.
\qquad\text{(11)}
\]
The union \(Y\) is an embedded analytic submanifold, possibly with infinitely many connected components, all of dimension \(d\).

Here is the dimension argument that makes (11) a strict descent. In the dimension-\(d\) regular part \(S^{(d)}_{\mathrm{reg}}\), apply the projection to the regular pieces of \(A=\Lambda\cap\pi^{-1}S\). Its rank-\(<d\) locus is conic subanalytic, and its image is subanalytic by conic projection. The analytic critical-value theorem makes that image measure zero in the smooth base. A subanalytic measure-zero set has dimension less than \(d\); its closure inside \(S^{(d)}_{\mathrm{reg}}\) still has dimension less than \(d\). Remove that relative closure and call the remaining dimension-\(d\) smooth part \(Y\). It is open in \(S\). The complement of \(S^{(d)}_{\mathrm{reg}}\) in \(S\) already has dimension less than \(d\), including any lower-dimensional components. The closure in \(S\) of the removed set can add points only in this complement, so \(R=S\setminus Y\) is closed and subanalytic of dimension less than \(d\). Over \(Y\), every regular cotangent point has projection onto \(TY\); the vanishing canonical one-form says that its covector annihilates \(TY\). To treat an arbitrary point of \(A\) over \(Y\), approximate it by regular points of \(A\). Their bases eventually remain in the same smooth local part of \(Y\), since \(Y\) is open in \(S\). The conormal bundle is closed over that part, so their limit also annihilates \(TY\). This proves the last inclusion in (11) for singular covectors and zero covectors as well. For \(d=0\), the critical locus is empty and the same argument leaves no lower-dimensional remainder.

Set \(U=X\setminus R\). Then \(Y=S\cap U\) is closed in \(U\), and the restricted cycle has support in \(T_Y^*U\). Equation (8) gives one integer \(m_Y\) on each connected component of \(Y\). Choose a sufficiently small relatively compact subanalytic ball around any base point, including a point of \(R\). Its intersection with \(Y\) has finitely many connected components. Every global component of \(Y\) meeting that ball contains one of these local components, and different global components contain different ones. Thus only finitely many global components meet the ball. Componentwise integer ranks are consequently locally finite even at the frontier, although their values need not be bounded over all of \(X\).

## Realize the generic coefficient by an actual bounded complex

Define \(a_Y=(-1)^d m_Y\), \(m_+=\max(a_Y,0)\) and \(m_-=\max(-a_Y,0)\). On \(Y\), construct the locally constant sheaves whose ranks on each component are these finite integers, and put
\[
A_Y=k_Y^{m_+}\oplus k_Y^{m_-}[1].
\qquad\text{(12)}
\]
The notation means the actual sheaf on the disjoint components, with its indicated finite rank at every point. It is not an infinite sum of Grothendieck classes. The two degrees are \(-1,0\), uniformly over all components. Its Euler function on \(Y\) is \(a_Y=(-1)^d m_Y\), so the signed coefficient in (9) is \((-1)^d a_Y=m_Y\).

Let \(i_Y:Y\hookrightarrow U\) be closed and \(j_U:U\hookrightarrow X\) open, and take
\[
F_Y=j_{U!}i_{Y*}A_Y.
\qquad\text{(13)}
\]
These two extension functors are exact. At points of \(Y\) the stalks are the finite coefficients in (12); outside \(Y\) they are zero. Choose a compatible locally finite subanalytic stratification of \(X\) for the closed sets \(S,R\), refined by the component pieces of \(Y\). A stratum in \(Y\) sees a constant rank and a stratum outside sees zero. The local finite-component observation after (11) makes this a legitimate locally finite refinement at frontier points. Thus (13) is constructible, has finite stalks and remains in its two global degrees.

This is the needed real-subanalytic extension argument. It uses the exact stalk formula and compatible stratification, rather than a proper-image theorem or a complex-analytic-boundary assertion with narrower hypotheses. Its closed support lies in \(S\).

The actual open restriction of (13) is \(j_U^{-1}F_Y=i_{Y*}A_Y\). Restriction of characteristic cycles commutes with their identity and trace maps. By (9), its coefficient on \(T_Y^*U\) is \((-1)^d\chi(A_Y)=(-1)^d a_Y=m_Y\), and there is no support over \(U\setminus Y\). Thus the equality holds on the whole cotangent bundle of this open set:
\[
CC_{\mathbb Z}(F_Y)|_{T^*U}=\lambda|_{T^*U}.
\qquad\text{(14)}
\]
Now set
\[
\lambda_1=\lambda-CC_{\mathbb Z}(F_Y).
\qquad\text{(15)}
\]
It is again an integral cycle with an allowed carrier: take the finite union \(\Lambda\cup SS(F_Y)\), which is closed conic subanalytic isotropic. The closed support of \(F_Y\) lies in \(S\). At every point of \(X\setminus S\) the sheaf vanishes on a neighborhood, so its microsupport has no covector there; consequently both terms of (15) have support over \(S\). Equation (14) says that their difference vanishes as a cycle section on the entire open set \(T^*U\), not merely on the generic regular covectors. Its actual support must therefore project into \(S\setminus U=R\). Hence
\[
\pi(\operatorname{supp}\lambda_1)\subset R,\qquad
\dim\pi(\operatorname{supp}\lambda_1)<d.
\qquad\text{(16)}
\]
The difference may have new conormal terms over the frontier \(R\); (16) permits and controls them. Discarding those terms instead would invalidate surjectivity.

Repeat on the actual residual cycle. Its closed conic support again has a closed subanalytic base projection by (10). The projection dimension drops strictly at each nonzero step, so there are at most \(d+1\leq n+1\) steps. We obtain bounded constructible complexes \(F_0,\ldots,F_r\), each in the same two degrees, and
\[
\lambda=\sum_{\ell=0}^r CC_{\mathbb Z}(F_\ell)
       =CC_{\mathbb Z}\!\left(\bigoplus_{\ell=0}^rF_\ell\right).
\qquad\text{(17)}
\]
The sum and direct sum in (17) are finite, and all summands have the same degree range \([-1,0]\). This proves surjectivity of (4), including noncompact \(X\), infinitely many strata, unbounded global coefficient ranks and nonorientable bases. If connected components of \(X\) have differing dimensions bounded by \(N\), perform the construction on each component, pad completed constructions with zero objects up to \(N+1\) stages, and glue the object at each stage over the disjoint open components. Each point has a neighborhood in its own component, so the glued objects remain constructible with finite stalks. Their common two-degree range and the same finite stage bound give one object of \(\mathcal D(X)\) realizing the global cycle. No infinite Grothendieck relation is used.

## A positive minimum measures the ordinary stalk

We need the exact local index result. Given \(F\in\mathcal D(X)\), \(x\in X\), and an analytic function \(\rho\) near \(x\) with
\[
\rho(x)=0,\qquad d\rho_x=0,\qquad
\operatorname{Hess}_x\rho>0,
\qquad\text{(18)}
\]
after shrinking its domain, the differential graph meets \(SS(F)\) in a subset of the singleton \(\{(x;0)\}\). In particular the intersection is empty if \(F\) vanishes on a neighborhood of \(x\). A zero stalk Euler value by itself does not imply an empty microsupport intersection. The normalized supported intersection number satisfies
\[
\#\bigl([\Gamma_{d\rho}]\cap CC_{\mathbb Z}(F)\bigr)_{(x;0)}
=\chi F(x).
\qquad\text{(19)}
\]
The integer in (19) is defined with the same ordered graph orientation, supported cup product and point trace as the field-valued intersection. Extending the orientation coefficient from \(\mathbb Z\) to \(k\) commutes with these maps and takes the primitive point generator to \(1\). It therefore sends the integral intersection to the field trace without a further sign. Since \(k\) has characteristic zero, \(\mathbb Z\to k\) is injective, and the field identity implies the integer equality in (19).

We spell out the local support and limit argument. Write \(x=0\) in an analytic chart, and choose a closed coordinate ball \(\overline B_R\) lying in the domain of \(\rho\). After decreasing \(R\), positive Hessian gives \(c|u|^2\leq\rho(u)\leq C|u|^2\) on this ball, with \(c,C>0\), and zero is its unique zero. Cut the closed conic isotropic carrier \(SS(F)\) by \(\pi^{-1}\overline B_R\). Canonical-form vanishing is inherited by this subanalytic subset. Its base projection is closed by (10) and is contained in the compact ball, so the restriction of \(\rho\) to that projection is proper. The isotropic critical-value theorem therefore makes the values selected by \(d\rho\) locally finite in the ambient real line. Choose \(0<\epsilon<cR^2\) so that none of those selected values lies in \((0,\epsilon)\), and set \(U=B_R\cap\{\rho<\epsilon\}\). Any point of \(\Gamma_{d\rho}\cap SS(F|_U)\) must have value zero and hence base point zero. This proves the asserted isolation, including a singular intersection at the zero covector.

Let \(D\) be the closed support of \(F\) in the chart. For \(0\leq t<\epsilon\), the closed support sublevel on \(U\) is \(D\cap\overline B_R\cap\{\rho\leq t\}\). The lower quadratic bound keeps it strictly inside the ball, and it is compact. Negative sublevels are empty. These are precisely the proper-below support conditions; no compactness of the original support on \(X\) is imposed.

Write \(U_t=\{u\in U:\rho(u)<t\}\). For \(0<t'<t<\epsilon\), choose \(0<r<t'\) and an increasing analytic diffeomorphism \(h:(-1,t)\to\mathbb R\). On \(U_t\), the function \(h\circ\rho\) has compact closed support sublevels and its positive differential avoids the microsupport above \(h(r)\). The positive open-cutoff theorem therefore identifies the actual restriction \(R\Gamma(U_t;F)\to R\Gamma(U_{t'};F)\) as a quasi-isomorphism. Its hypothesis concerns a positive multiple of \(d\rho\), so conicity gives exactly the avoidance already checked. These maps compose as ordinary restrictions.

The quadratic bounds make the \(U_t\) a neighborhood basis of zero. Take a bounded-below injective resolution on \(U\); its restrictions to the open \(U_t\) compute their derived sections. The filtered colimit of their section complexes is the stalk complex, degree by degree. Filtered colimits of vector spaces are exact, so every canonical map from this stable family of derived section complexes to \(F_0\) is a quasi-isomorphism. In particular their cohomology is finite-dimensional. Apply the ordinary proper-below differential index theorem on \(U_t\), with target interval \((-1,t)\). The checked closed sublevels are compact and its graph intersection is contained in \(\{(0;0)\}\). Open excision identifies its supported intersection with the local intersection in (19); the section complex just identified has Euler value \(\chi F(0)\). Together with the coefficient comparison above this proves (19), with its positive-minimum sign and without a transversality assumption.

## Vanishing cycle means vanishing Grothendieck class

Every element \(c\in K_0(X)\) is represented by one object. Indeed it starts as a finite integer combination of object classes; replace a negative coefficient by a shift \([1]\) and take the finite direct sum. Suppose \(CC_{\mathbb Z}(c)=0\), and choose such an \(F\). At each point choose a positive quadratic function as in (18). Equation (19) gives \(\chi F(x)=0\). Therefore its entire Euler function vanishes. Injectivity of (6) gives \(c=[F]=0\).

Together with (17) this proves
\[
CC_{\mathbb Z}:K_0(X)\xrightarrow{\ \sim\ }LC(X).
\qquad\text{(20)}
\]
This is injectivity on classes, not a criterion that an object itself is zero. A nonzero \(F\oplus F[1]\) has both Euler function and characteristic cycle zero.

## The Euler morphism is independent of the test

For \(\lambda\in LC(X)\) define
\[
Eu(\lambda)(x)
=\#\bigl([\Gamma_{d\rho}]\cap\lambda\bigr)_{(x;0)},
\qquad\text{(21)}
\]
where \(\rho\) satisfies (18). Surjectivity supplies \(F\) with \(CC_{\mathbb Z}(F)=\lambda\). Equation (19) proves that the intersection in (21) is isolated after shrinking and gives
\[
Eu(\lambda)=\chi F.
\qquad\text{(22)}
\]
Indeed \(\operatorname{supp}\lambda\subset SS(F)\), so the same shrinking gives an isolated supported intersection for \(\lambda\). Its ordered local intersection is intrinsic to the integral cycle and the chosen graph. Equation (19) identifies it with \(\chi F(x)\) for every admissible phase and every realizing object. Thus (21) is independent of the phase, its chart and the sufficiently small neighborhood, and any other realization gives exactly the same value. The right side of (22) is constructible. Additivity of the supported intersection in the cycle makes \(Eu\) a homomorphism. In particular the normalization is \(Eu([T_Y^*U])=(-1)^{\dim Y}1_Y\), since (9) sends \(k_Y\) to \((-1)^{\dim Y}[T_Y^*U]\).

If \(F,G\) realize the same cycle, (20) gives \([F]=[G]\), and (6) gives \(\chi F=\chi G\). Conversely (19) already shows equality of their values directly. We have the commuting isomorphisms
\[
\begin{array}{ccc}
K_0(X)&\xrightarrow{\ CC_{\mathbb Z}\ }&LC(X)\\
{\scriptstyle\chi}\downarrow&&\downarrow{\scriptstyle Eu}\\
CF(X)&=&CF(X).
\end{array}
\qquad\text{(23)}
\]
In particular every integral Lagrangian cycle has exactly one associated constructible function and every such function has exactly one associated cycle. A chosen complex realizing either is generally far from unique.

All constructions restrict to analytic open subsets: stalk Euler, cycle coefficients, identity/trace construction and the isolated supported intersection do so. Surjectivity and injectivity apply on each such subset with the same local hypotheses. Consequently (23) also identifies the sheaves
\[
\pi_*\mathcal L_{X,\mathbb Z}\simeq\mathcal{CF}_X,
\qquad\text{(24)}
\]
and the sheafification of \(U\mapsto K_0(U)\) with both sides. The Grothendieck group itself is still formed using its finite triangle relations; sheafification does not authorize infinite relations. The generic realization is one way to construct its inverse, while (21) makes that inverse intrinsic.

## Examples and exercises with complete solutions

### Infinitely many fibres require only one coefficient stage
*Difficulty: Intermediate.*

On \(X=\mathbb R\), let \(P_j=CC_{\mathbb Z}(k_{\{j\}})\) for \(j\in\mathbb Z\), the normalized full cotangent fibre. Construct an object realizing the locally finite cycle \(\lambda=\sum_{j\in\mathbb Z}jP_j\). Determine its Euler function and discuss global compact cohomology.

**Solution.** The cycle sum denotes a locally finite section of the chain sheaf. Its base support is \(\mathbb Z\setminus\{0\}\), closed subanalytic of dimension zero. Define \(A\) on positive integer points with stalk \(k^j\), and \(B\) on negative integer points with stalk \(k^{-j}\), extending both by zero. They are actual sheaves on a locally finite discrete set, constructible with finite stalks. Take \(F=A\oplus B[1]\), in degrees \(-1,0\). Additivity and point normalization give its cycle \(\lambda\).

Its Euler function is \(j\) at integer \(j\), and zero elsewhere, including zero. Compact global cohomology has an infinite direct sum of the positive coefficients in degree zero and of the negative coefficients in degree \(-1\). It is not finite dimensional, so it has no finite Euler integral of the compact-support type. The local correspondence (23) remains valid. There is one dimension-zero coefficient stage, not an infinite sum of classes.

### Frontier terms remain in the residual cycle
*Difficulty: Advanced.*

In the cotangent line use normalized cycles
\[
C=CC_{\mathbb Z}(k_{[0,\infty)}),\quad
O=CC_{\mathbb Z}(k_{(0,\infty)}),\quad
P=CC_{\mathbb Z}(k_{\{0\}}).
\]
Let \(\lambda=3C-2O\). Use the highest-dimensional realization followed by a zero-dimensional correction, and compute \(Eu(\lambda)\).

**Solution.** The endpoint localization triangle gives \(C=O+P\). Thus
\[
\lambda=O+3P.
\]
Here the open ambient set is \(U=\mathbb R\setminus\{0\}\), and the dimension-one smooth base of the cycle is \(Y=(0,\infty)\). Over \(Y\), \(O\) has coefficient \(m_Y=-1\) in the graph-normalized zero-section generator; there is no cycle over the negative component of \(U\). The coefficient required in (12) is consequently \(a_Y=(-1)^1m_Y=1\). Its degree-zero constant sheaf extends by zero to \(k_{(0,\infty)}\), with full cycle \(O\), including its boundary conormal term. The residual cycle is \(3P\), realized by \(k_{\{0\}}^3\). Hence \(F=k_{(0,\infty)}\oplus k_{\{0\}}^3\) realizes \(\lambda\). Its Euler function is one on \(x>0\), three at zero, and zero on \(x<0\).

Equivalently, since \(\chi k_{[0,\infty)}=1_{[0,\infty)}\), the function is \(3\,1_{[0,\infty)}-2\,1_{(0,\infty)}\). Replacing the first-stage cycle by only its restriction over \(Y\) and forgetting its frontier term would give an incorrect residual.

### Monodromy prevents uniqueness of the realizing object
*Difficulty: Intermediate.*

Embed a circle \(Y\) as a closed analytic curve in \(\mathbb R^2\). Compare the cycles of its constant rank-one local system and its rank-one local system with monodromy \(-1\), both extended by the closed embedding. Compare their cohomology.

**Solution.** Each system is locally rank one on a base of dimension one, so (9) gives the same cycle \(-[T_Y^*\mathbb R^2]\). Their Euler functions both equal \(1_Y\), and (20) identifies their Grothendieck classes. They differ as sheaves because their monodromy automorphisms differ.

Cutting the circle gives the complex \([k\xrightarrow{T-1}k]\) in degrees zero and one. For \(T=1\) both cohomology groups are \(k\); for \(T=-1\), multiplication by \(-2\) is invertible in characteristic zero and both vanish. Their global Euler values are both zero. Neither equality of cycles nor equality of classes identifies the objects or their individual cohomology groups.

### The orientation coefficient permits a nonorientable base
*Difficulty: Intermediate.*

Let \(X=\mathbb{RP}^2\). Explain why \(CC_{\mathbb Z}(k_X)\) is a globally defined normalized zero-section cycle, and compute the Euler function of \(-2CC_{\mathbb Z}(k_X)\). Is an orientation of \(X\) needed?

**Solution.** The geometric zero section has orientation line \(\operatorname{or}_X\). On it the cotangent fibre coefficient \(B_{\mathbb Z}\) is the dual orientation sign line, with the same \(\pm1\) monodromy. Their tensor square is trivial. Thus the normalized cycle is global with coefficient (2), despite the absence of an untwisted fundamental orientation.

The function is the constant \(-2\), realized by \(k_X^2[1]\). Equations (5) and (23) give the asserted cycle and Euler function. No choice of orientation or replacement of the relative coefficient by a constant untwisted coefficient is allowed or needed.

### A positive test cannot be replaced by a negative one
*Difficulty: Intermediate.*

For \(F=k_{[0,\infty)}\) on \(\mathbb R\), compare the local graph-cycle numbers at zero for \(\rho(t)=t^2\), \(\rho'(t)=3t^2+t^3\), and \(-t^2\).

**Solution.** The first two phases have zero value and differential and positive Hessian at zero; after shrinking, each has a strict minimum. Equation (19) gives number \(\chi F_0=1\) for both.

The negative phase is a maximum. The negative-Hessian counterpart of the local index theorem measures the ambient point costalk. For the closed positive halfline, the full-to-punctured section map on a small interval is \(k\to k\), the identity. Its support triangle gives \(i_0^!F=0\). Thus the negative graph number is zero. This is a singular zero-covector intersection, and the supported trace still applies. Condition (18) is essential to the Euler morphism's definition.

### A zero cycle can have nonzero microsupport
*Difficulty: Introductory.*

Take \(F=k_{\{0\}}\oplus k_{\{0\}}[1]\) on \(\mathbb R\). Find its characteristic cycle, local Euler function and Grothendieck class. Is it the zero object?

**Solution.** Shift additivity gives \(CC_{\mathbb Z}(F)=P-P=0\). The only possible nonzero Euler value is at zero, where it is \(1-1=0\). Hence \([F]=0\) by (6) or (20). However \(H^0(F)=k_{\{0\}}\) and \(H^{-1}(F)=k_{\{0\}}\), so it is nonzero. Its microsupport is the full point fibre. Cancellation of the cycle does not remove this microsupport.

### Zero dimension is already the full correspondence
*Difficulty: Introductory.*

Let \(X\) be a countable discrete zero-dimensional analytic manifold. Describe all three groups in (23), including functions with unbounded integer values.

**Solution.** The cotangent space is \(X\) itself, each fibre a point. A degree-zero cycle is an arbitrary locally specified integer at each point; there is no boundary and every support is locally subanalytic and closed in the discrete topology. Every integer valued function has locally finite values because a singleton is a neighborhood. Thus both \(LC(X)\) and \(CF(X)\) are the full product \(\prod_{x\in X}\mathbb Z\).

For a function \(m(x)\), choose at each point a vector space of dimension \(\max(m(x),0)\) in degree zero and one of dimension \(\max(-m(x),0)\) in degree \(-1\). These form an actual globally two-degree sheaf complex. Equation (6) identifies \(K_0(X)\) with that product too. At a point the minimum test has a zero-dimensional Hessian, positive definite in the vacuous zero-vector sense, and the local intersection simply reads the integer. There is no residual induction after this stage.

### A compact global trace can vanish while the cycle does not
*Difficulty: Intermediate.*

Let \(F=k_Y\) for the analytic circle \(Y\subset\mathbb R^2\) used above. Compare \(Eu(CC_{\mathbb Z}(F))\), its Euler integral and its local cycle.

**Solution.** The local function is \(1_Y\), with compact closed support. Its Euler integral is \(\chi(Y;k)=1-1=0\). Its characteristic cycle remains the nonzero cycle \(-[T_Y^*\mathbb R^2]\), whose coefficient in the graph-normalized generator is minus one in every local conormal chart. Thus the proper image to a point forgets the spatial information by a global trace, whereas \(Eu\) recovers the entire function before integration. The zero global number cannot replace the pointwise criterion used in the injectivity proof.

## References and continuation

- M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), 193–209, and P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), J. Pure Appl. Algebra 72 (1991), 83–93: characteristic cycles, the Euler morphism and the correspondence between constructible functions and Lagrangian cycles. The proof here expands the finite projection-dimension induction and uses the programme's proofs for its geometric and index inputs.
- The linked SH-03 lessons supply normalized integral chains, conormal coefficients, triangle additivity, generic singular conormal containment, positive-Hessian isolation and the constructible-function Grothendieck bijection.

Original prose, organization, examples and solutions are dedicated to CC0. The correspondence above retains the geometric, chain and local-index prerequisites identified in the linked programme proofs.
