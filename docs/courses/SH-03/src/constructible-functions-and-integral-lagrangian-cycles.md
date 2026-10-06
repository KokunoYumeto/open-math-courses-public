# Constructible functions and integral Lagrangian cycles

*Original draft written by AI in Codex. Source-scope and reader repairs by GPT-6 Astra (OpenAI), Ultra, 6 October 2026. Self-checked by the revising AI. Original programme text is public domain (CC0).*

A characteristic cycle remembers exactly the Grothendieck class of a constructible complex. Equivalently, it remembers the complex's local Euler function. The correspondence does not identify sheaf objects: monodromy, individual cohomology groups and cancellation between shifts can disappear. This lesson proves the complete correspondence and constructs its inverse through local intersections with positive-Hessian graphs.

The correspondence between constructible functions, integral Lagrangian cycles and Grothendieck groups is due to Kashiwara and Schapira; see M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), and P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf) (1991). Read Constructible functions and Euler integration for the full Grothendieck bijection, including noncompact manifolds and locally infinite strata. Integer coefficients and additive characteristic cycles proves the integral lift, local conormal coefficient and triangle additivity. Finite conormal closures and generic base directions proves generic conormal containment, including singular covectors. Differential sections and proper-below Euler indices proves the positive-Hessian local stalk formula with actual shrinking maps. The chain, orientation and supported trace constructions are in Lagrangian cycles and proper cotangent images and Subanalytic chains and closed cycle supports.

These are exact written programme providers. Compatible subanalytic stratifications, local finite-component and dimension theorems retain their existing owned foundational obligations in this course. The arguments below prove the correspondence relative to those precise prerequisites.

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
The support of a section of this sheaf is closed, conic and subanalytic and remains isotropic. Here are the local-to-global details needed below. On a relatively compact chart, a finite compatible subdivision describes a cycle by constant coefficients on regular top pieces; its actual support is the union of closures of the pieces with nonzero coefficient. It is subanalytic and lies in the given isotropic carrier. Positive radial transport preserves the coefficient on a smooth regular piece and its normalized orientation; the dense top-chain comparison extends that equality to the frontier. Thus the support and cycle are positive-conic. Subanalyticity and isotropy are local properties, so these statements hold for the global support. They do not require taking an arbitrary infinite union in one chart.

The integral characteristic-cycle construction and additivity give
\[
CC_{\mathbb Z}:K_0(X)\longrightarrow LC(X).
\qquad\text{(4)}
\]
More explicitly, generic finite coefficient complexes give integer multiplicities. The injection \(\mathbb Z\hookrightarrow k\), together with the integral boundary incidence numbers, extends their integral top chain to a cycle at every frontier. One actual coefficient functor represents a whole localized distinguished triangle, so its Euler coefficients add. Dense top-chain determination then proves
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

The sign line in (7) is canonically trivialized by the normalized conormal cycle
\([T_Y^*U]=CC_{\mathbb Z}(k_Y)\). To check why this works without orienting \(Y\), split locally
\[
TU|_Y\simeq TY\oplus N_{Y/U}.
\]
The tangent orientation of the conormal total space is the product of the orientation of \(TY\) and that of \(N_{Y/U}^*\). The fibre orientation coefficient in (2) restricts to the orientation of \(T^*U|_Y\), which is the product of the dual tangential and dual normal orientation lines. Their tensor product has trivial sign monodromy: each tangential and normal sign appears twice. The trace-normalized conormal construction fixes the integral generator and its order, including the codimension convention. We use that generator, rather than choosing a new untwisted orientation.

Every conormal fibre is a connected vector space, including its zero vector. Since a coefficient section in (7) is locally constant, it is constant on the entire fibre. Along a base component it is also constant. Thus every such cycle has the form
\[
\lambda=m_Y[T_Y^*U],
\qquad\text{(8)}
\]
where \(m_Y:Y\to\mathbb Z\) is locally constant. If a component's integer is nonzero, its whole conormal fibre occurs in the cycle support. A half-fibre with a nonzero uncancelled boundary cannot itself be a cycle on this smooth conormal manifold.

The local conormal coefficient theorem gives, for any bounded locally constant finite coefficient complex \(A\) on \(Y\),
\[
CC_{\mathbb Z}(i_*A)
=\left(\sum_q(-1)^q\operatorname{rank}H^q(A)\right)[T_Y^*U].
\qquad\text{(9)}
\]
Its proof uses the actual constant-section counit on contractible base balls, then the normalized finite conormal formula, and glues by restriction. It permits monodromy and requires no global constant trivialization.

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

For clarity, the geometric provider does more than inspect generic covectors one at a time. On the regular cotangent pieces over the regular base it removes the values where the projection has rank below \(d\). Those values and their relative closures have dimension below \(d\), by conic subanalytic projection, Sard's theorem and the subanalytic dimension bound. At the remaining regular cotangent points, every tangent vector of \(Y\) lifts. Vanishing of the canonical one-form implies that the covector annihilates \(TY\). Regular cotangent points are dense, and the ordinary conormal is closed over this smooth base; taking limits proves the same containment for singular covectors and zero covectors. This is precisely the complete generic containment theorem proved in the linked conormal lesson.

Set \(U=X\setminus R\). Then \(Y=S\cap U\) is closed in \(U\), and the restricted cycle has support in \(T_Y^*U\). Equation (8) gives one integer \(m_Y\) on each connected base component. The local finite-component theorem ensures that a sufficiently small relatively compact subanalytic chart, including one at a frontier point, meets only finitely many components of \(Y\). Distinct global components meeting such a chart must contain distinct local components there. Thus componentwise integer ranks are locally finite even near \(R\).

## Realize the generic coefficient by an actual bounded complex

Define \(m_+=\max(m_Y,0)\), \(m_-=\max(-m_Y,0)\). On \(Y\), construct the locally constant sheaves whose ranks on each component are these finite integers, and put
\[
A_Y=k_Y^{m_+}\oplus k_Y^{m_-}[1].
\qquad\text{(12)}
\]
The notation means that actual sheaf on the disjoint components, with its indicated rank at every point. It is not an infinite sum of Grothendieck classes. The two degrees are \(-1,0\), uniformly over all components. Its Euler function on \(Y\) is \(m_Y\).

Let \(i_Y:Y\hookrightarrow U\) be closed and \(j_U:U\hookrightarrow X\) open, and take
\[
F_Y=j_{U!}i_{Y*}A_Y.
\qquad\text{(13)}
\]
These two extension functors are exact. At points of \(Y\) the stalks are the finite coefficients in (12); outside \(Y\) they are zero. Choose a compatible locally finite subanalytic stratification of \(X\) for the closed sets \(S,R\), refined by the component pieces of \(Y\). A stratum in \(Y\) sees a constant rank and a stratum outside sees zero. The local finite-component observation after (11) makes this a legitimate locally finite refinement at frontier points. Thus (13) is constructible, has finite stalks and remains in its two global degrees.

This is the needed real-subanalytic extension argument. It uses the exact stalk formula and compatible stratification, rather than a proper-image theorem or a complex-analytic-boundary assertion with narrower hypotheses. Its closed support lies in \(S\).

Restriction of characteristic cycles to \(U\) commutes with their identity and trace construction. Equations (9) and (12) therefore give
\[
CC_{\mathbb Z}(F_Y)|_{T^*U}=\lambda|_{T^*U}.
\qquad\text{(14)}
\]
Now set
\[
\lambda_1=\lambda-CC_{\mathbb Z}(F_Y).
\qquad\text{(15)}
\]
It is again an integral cycle with an allowed carrier: use the finite union
\(\Lambda\cup SS(F_Y)\), which is closed conic subanalytic isotropic. The closed support of \(F_Y\) lies in \(S\), hence its microsupport projects into \(S\). Equation (14) removes every remaining base point in \(Y\). Consequently
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
The sum and direct sum in (17) are finite. This proves surjectivity of (4), including noncompact \(X\), infinitely many strata, unbounded global coefficient ranks and a nonorientable base. The uniform dimension bound also makes the number of stages uniform across components of differing dimension.

## A positive minimum measures the ordinary stalk

We need the exact local index result. Given \(F\in\mathcal D(X)\), \(x\in X\), and an analytic function \(\rho\) near \(x\) with
\[
\rho(x)=0,\qquad d\rho_x=0,\qquad
\operatorname{Hess}_x\rho>0,
\qquad\text{(18)}
\]
its differential graph has an isolated local intersection with \(SS(F)\) at the zero covector, or an empty intersection if \(F\) is invisible there. The normalized supported intersection number satisfies
\[
\#\bigl([\Gamma_{d\rho}]\cap CC_{\mathbb Z}(F)\bigr)_{(x;0)}
=\chi F(x).
\qquad\text{(19)}
\]
The integral number maps to the corresponding \(k\)-valued trace by the injective coefficient map. Thus the existing field trace identity is also the integral identity in (19).

Here is the proof mechanism, including isolation. Work in coordinates \(x=0\). Positive Hessian gives \(c|u|^2\leq\rho(u)\leq C|u|^2\) on a small closed ball, for positive constants. Apply the discrete critical-value theorem to the closed conic isotropic microsupport cut over that ball. Its base is compact. The values selected by \(d\rho\) are locally finite, so shrink to exclude all positive selected values near zero. A sufficiently small \(\rho\)-sublevel lies strictly inside the ball and has compact closed support sublevels. Since \(\rho\) vanishes there only at zero, the graph meets the microsupport only over zero.

For two sufficiently small positive levels, the finite-band Morse theorem makes the **actual restriction** of section complexes an isomorphism. Compact closed bands and microsupport avoidance supply its hypotheses. The quadratic bounds make these sublevels a neighborhood basis; exact stalk colimits identify their stable section complex with \(F_x\). The proper-below differential index theorem identifies its Euler value with the supported local graph-cycle number. This proves (19). All comparisons, critical-value conditions, compactness checks and shrinking maps are proved in the linked differential-index lesson. This argument covers a singular intersection at \((x;0)\); no transverse nonzero-covector assumption is inserted.

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
Thus the value is independent of the analytic phase, its chart, the sufficiently small neighborhood and the realizing object. The right side is constructible. Local intersection is additive in the cycle, so \(Eu\) is a homomorphism.

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
On the generic base \(Y=\mathbb R\setminus\{0\}\), the coefficient is one on the positive component and zero on the negative component. Extending that coefficient by zero gives \(k_{(0,\infty)}\), with cycle \(O\); this includes its boundary conormal term. The residual cycle is \(3P\), realized by \(k_{\{0\}}^3\). Hence \(F=k_{(0,\infty)}\oplus k_{\{0\}}^3\) realizes \(\lambda\). Its Euler function is one on \(x>0\), three at zero, and zero on \(x<0\).

Equivalently, since \(\chi k_{[0,\infty)}=1_{[0,\infty)}\), the function is \(3\,1_{[0,\infty)}-2\,1_{(0,\infty)}\). Replacing the first-stage cycle by only its restriction over \(Y\) and forgetting its frontier term would give an incorrect residual.

### Monodromy prevents uniqueness of the realizing object
*Difficulty: Intermediate.*

Embed a circle \(Y\) as a closed analytic curve in \(\mathbb R^2\). Compare the cycles of its constant rank-one local system and its rank-one local system with monodromy \(-1\), both extended by the closed embedding. Compare their cohomology.

**Solution.** Each system is locally rank one, so (9) gives the same normalized full conormal cycle \([T_Y^*\mathbb R^2]\). Their Euler functions both equal \(1_Y\), and (20) identifies their Grothendieck classes. They differ as sheaves because their monodromy automorphisms differ.

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

**Solution.** The local function is \(1_Y\), with compact closed support. Its Euler integral is \(\chi(Y;k)=1-1=0\). Its characteristic cycle remains the nonzero normalized full conormal \([T_Y^*\mathbb R^2]\), whose coefficient is one in every local conormal chart. Thus the proper image to a point forgets the spatial information by a global trace, whereas \(Eu\) recovers the entire function before integration. The zero global number cannot replace the pointwise criterion used in the injectivity proof.

## References and continuation

- M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), 193–209, and P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), J. Pure Appl. Algebra 72 (1991), 83–93: characteristic cycles, the Euler morphism and the correspondence between constructible functions and Lagrangian cycles. The proof here expands the finite projection-dimension induction and uses the programme's proofs for its geometric and index inputs.
- The linked SH-03 lessons supply normalized integral chains, conormal coefficients, triangle additivity, generic singular conormal containment, positive-Hessian isolation and the constructible-function Grothendieck bijection.

Original prose, organization, examples and solutions are dedicated to CC0. The correspondence above retains the geometric, chain and local-index prerequisites identified in the linked programme proofs.
