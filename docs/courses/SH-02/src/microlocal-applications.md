# SH02-MA — Continuing coefficients and transporting local morphisms

Local unit: `SH02-MA`. License: GFDL-1.2-or-later, with no invariant sections or cover texts. Formalization and translation are absent.

This lesson connects three uses of a directional estimate: continuing an ordinary section, transporting an internal Hom, and choosing a representative in a localized category. The last use requires a fraction calculation. A sheaf of microlocal morphisms on an open set does not by itself compute the morphisms of the quotient category attached to that set.

Throughout, $k$ is a commutative unital ring of finite global dimension. Manifolds are finite-dimensional real smooth Hausdorff second-countable manifolds. Every complex belongs to the bounded derived category of **all** sheaves of $k$-modules. No field, constructibility, finite-rank, orientability or compact-support hypothesis is implicit. A constant complex $M_Z$ on a locally closed set means extension by zero to the stated ambient space. Supports are closed supports. For a closed convex cone $C$ in a real vector space, $C^\circ$ is its nonnegative polar and $C^{\circ a}=-C^\circ$. A proper cone contains no line. The operation $A\widehat+B$ is the asymptotic sum, including its escaping sequences, from asymptotic estimates.

The proof inputs are the cone topology and its projector, the cone continuation and microsupport tests, the characteristic estimates, [involutivity](involutivity.md), localized categories, and microlocal Hom. Each use below names the needed statement. The applications of microsupport localization go back to M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapter 6.

## SH02-MA-LOCAL-CONTINUATION — Cone continuation inside a chart

Let $E$ be a finite-dimensional real vector space, $B\subset E$ a bounded open convex set, and $C\subset E$ a closed convex cone. Suppose

$$
\operatorname{SS}(F)\subset B\times C^{\circ a}.
\tag{MA1}
$$

If $O\subset B$ is nonempty, open and convex, restriction induces

$$
R\Gamma((O+C)\cap B;F)\xrightarrow{\sim}R\Gamma(O;F).
\tag{MA2}
$$

The empty case has both sides zero. This is a local version of cone continuation: no extension of (MA1) across the boundary of $B$ is assumed.

**Proof.** Put $W=(O+C)\cap B$. We spell out why the proof of `SH02-MST-CUTOFF-CONVERSE` works with this domain. Among open convex sets $V$ with $O\subset V\subset W$, take those for which restriction to $O$ is a cohomological isomorphism. A chain has its union as an upper bound. Indeed a countable subchain covers that union, by second countability; degreewise sections of an injective resolution form a surjective inverse system. The product difference sequence and its Milnor exact sequence identify cohomology on the union with the constant system $H^*(O;F)$. This argument is bounded below and does not assume exactness of arbitrary inverse limits. Zorn's lemma gives a maximal $V$.

If $V\ne W$, take $z\in W\setminus\overline V$ and put $D=\overline{\operatorname{pos}(V-z)}$. Because $V$ is bounded and its closed convex closure is a positive distance from $z$, the closest-point inequality gives a linear functional strictly positive on $D\setminus0$. Thus $D$ is proper. Write $z=o+c$ with $o\in O$ and $c\in C$. The vector $o-z=-c$ is interior to $D$. Every nonzero covector in $D^{\circ a}$ is strictly negative on this vector, whereas a covector in $C^{\circ a}$ is nonnegative on it. Consequently

$$
D^{\circ a}\cap C^{\circ a}=\{0\}.
$$

The convex geometry lemma `SH02-MST-CONVEX-GEOMETRY` gives $D$-open sets $V_3\subset V_2$ such that

$$
V_2\setminus V_3=V_1\setminus V,
\qquad V_1=\operatorname{Int}\operatorname{conv}(V\cup\{z\}),
\qquad V_2=V_1\cup V_3,
\quad V=V_1\cap V_3.
$$

For each $w\in V_2$, the set $(w+D)\setminus V_3$ is closed, bounded, and contained in $V_1\subset W\subset B$. It is therefore compact inside the domain where $F$ is defined. Cone propagation, with ambient domain $B$, applies to $V_3\subset V_2$: the only support difference lies in $B$, and its required covectors are excluded by (MA1) and the displayed polar intersection. It gives $R\Gamma(V_2\cap B;F)\simeq R\Gamma(V_3\cap B;F)$. Mayer–Vietoris for $V_2\cap B=V_1\cup(V_3\cap B)$ now gives $R\Gamma(V_1;F)\simeq R\Gamma(V;F)$. This strictly enlarges $V$ within $W$, a contradiction. Therefore $V=W$, proving (MA2). The compact sets just checked, rather than an estimate on an artificially extended sheaf, justify the localization to $B$. $\square$

## SH02-MA-CONE-MODEL — A local directional model and its cohomology sheaves

Let $X\subset E$ be open and let $C\subset E$ be a proper closed convex cone. Suppose $F\in D^b(k_X)$ satisfies $\operatorname{SS}(F)\subset X\times C^{\circ a}$. For each $x\in X$ there is an ordinary neighborhood $B$ of $x$ and a bounded complex $A$ of sheaves on the directional space $E_C$ such that

$$
F|_B\simeq (\phi_C^{-1}A)|_B.
\tag{MA3}
$$

Moreover, for every integer $j$,

$$
\operatorname{SS}(\mathcal H^j(F))\subset X\times C^{\circ a}.
\tag{MA4}
$$

Here $E_C$ has the ordinary open sets stable under addition by $C$, and $\phi_C:E\to E_C$ is the identity of underlying sets. The cone may have empty interior or equal $\{0\}$.

**Proof.** Choose a bounded open convex $B$ containing $x$ with $\overline B\subset X$. Let $j:B\hookrightarrow E$ and set

$$
A=R\phi_{C*}Rj_*(F|_B)=R(\phi_Cj)_*(F|_B).
$$

This complex is bounded. To check that assertion on the possibly non-Hausdorff target, use its convex neighborhood basis $B_\epsilon(z)+C$. Each inverse image in $B$ is an ordinary open subset of a finite-dimensional manifold. The uniform finite cohomological-dimension bound for sections on such open subsets bounds all the higher direct-image stalks, independently of $z$ and $\epsilon$. The lower bound is preserved by right derived direct image. No locally compact six-operation theorem on $E_C$ is being used.

The two adjunction counits give $(\phi_C^{-1}A)|_B\to F|_B$. For $z\in B$ and sufficiently small $\epsilon$, its stalk is the filtered colimit of the restriction maps

$$
R\Gamma((B_\epsilon(z)+C)\cap B;F)
\longrightarrow R\Gamma(B_\epsilon(z);F).
$$

Each map is an isomorphism by (MA2), and the right-hand colimit computes $F_z$. Filtered colimits of modules are exact, so the counit is an isomorphism on every cohomology stalk. This proves (MA3).

Inverse image of sheaves is exact. Hence $\mathcal H^j(F)|_B\simeq (\phi_C^{-1}\mathcal H^j(A))|_B$. The forward cone-projector theorem says that the inverse image of any sheaf on $E_C$ has microsupport in $E\times C^{\circ a}$; it follows by applying the projector identity to that inverse image and using its polar bound. This theorem permits arbitrary modules and closed convex cones. Applying it locally at every $x$ proves (MA4). When $C=\{0\}$, $\phi_C$ is the ordinary identity and the assertion reduces to the unconstrained local model. $\square$

## SH02-MA-SECTION — A section cannot terminate across an allowed cone

Suppose $F\in D^b(k_X)$ has $\mathcal H^j(F)=0$ for $j<0$, and let

$$
u\in H^0R\Gamma(X;F)=\Gamma(X;\mathcal H^0(F)).
$$

Let $Z=\operatorname{supp}(u)$, let $x\in X$, and let $C\subset T_xX$ be a **nonzero** proper closed convex cone. Write $C_x(Z)$ for the ordinary tangent cone obtained by moving a point of $Z$ towards the fixed point $x$. If

$$
\operatorname{SS}(F)_x\cap C^{\circ a}\subset\{0\},
\qquad C_x(Z)\cap C\subset\{0\},
\tag{MA5}
$$

then $x\notin Z$.

**Proof.** Work in a chart centered at $x=0$. Suppose $x\in Z$. Compactness of unit directions, properness of $C$, and the second condition in (MA5) allow two slightly larger proper closed convex cones $C_1,C_2$ with

$$
C\setminus0\subset\operatorname{Int}C_1,
\quad C_1\setminus0\subset\operatorname{Int}C_2,
\quad C_x(Z)\cap C_2=\{0\}.
$$

One concrete construction chooses a linear functional strictly positive on $C\setminus0$, thickens its compact convex unit section twice by sufficiently small balls in that affine hyperplane, and then takes positive hulls. The forbidden tangent directions and the opposite halfspace stay a positive distance from these sections. These choices also give a nonzero $v\in\operatorname{Int}C_1$.

After shrinking the chart $W$, tangent-cone avoidance implies $Z\cap(W\cap C_2)=\{0\}$. Otherwise points of $Z\cap C_2\setminus0$ tending to zero, normalized to unit length, would give a forbidden tangent vector. Also $C_1^{\circ a}\subset C^{\circ a}$, so the first condition of (MA5), closedness and conicity of microsupport give

$$
\operatorname{SS}(F)\cap
\bigl(W\times(C_1^{\circ a}\setminus0)\bigr)=\varnothing.
$$

Set $O_0=\operatorname{Int}C_2$ and

$$
O_\epsilon=O_0\cup(-\epsilon v+\operatorname{Int}C_1).
$$

These are $C_1$-open, and $0\in O_\epsilon$. Their added cap has diameter $O(\epsilon)$. Indeed strict containment of the unit directions of $C_1$ in $\operatorname{Int}C_2$ gives $\operatorname{dist}(c,E\setminus\operatorname{Int}C_2)\ge a|c|$ for $c\in C_1$, with some $a>0$. If $c-\epsilon v\notin\operatorname{Int}C_2$, then $a|c|\le\epsilon|v|$. This bounds both $c$ and $c-\epsilon v$ by constants times $\epsilon$. For every $w\in O_\epsilon$, the set $(w+C_1)\setminus O_0$ is closed and lies in that bounded cap, hence is compact and lies in $W$ for small $\epsilon$.

Cone propagation therefore makes restriction $R\Gamma(O_\epsilon\cap W;F)\to R\Gamma(O_0\cap W;F)$ an isomorphism. The section $u$ is zero on $O_0\cap W$, since this set misses $Z$. The nonnegative cohomological bound identifies degree-zero hypercohomology on both opens with sections of $\mathcal H^0(F)$. Thus $u$ is zero on $O_\epsilon\cap W$, a neighborhood of $0$, contrary to $0\in Z$. $\square$

The nonzero-cone hypothesis is essential. If $C=\{0\}$, a nonzero constant section of $k_X$ satisfies both inclusions in (MA5), but its support is all of $X$. The argument concerns the support of the particular section; it never assumes that the entire complex vanishes on $O_0$.

## SH02-MA-TRACE-EXCHANGE — Pulling back Hom and tensor under one combined test

Let $f:Y\to X$ be smooth, put $A_i=\operatorname{SS}(F_i)$, and let $\omega_f=f^!k_X$ be the invertible relative orientation complex, with shift $[\dim Y-\dim X]$. Noncharacteristicness for a closed conic set $A$ means that $df_y^t\xi=0$ and $(f(y),\xi)\in A$ imply $\xi=0$.

If $f$ is noncharacteristic for $A_1\widehat+A_2^a$, then the natural morphism is an isomorphism:

$$
f^{-1}R\mathcal Hom(F_2,F_1)
\xrightarrow{\sim}
R\mathcal Hom(f^{-1}F_2,f^{-1}F_1).
\tag{MA6}
$$

If $f$ is noncharacteristic for $A_1\widehat+A_2$, the natural tensor/exceptional-image morphism is an isomorphism:

$$
f^{-1}F_1\otimes^L f^!F_2
\xrightarrow{\sim}f^!(F_1\otimes^L F_2).
\tag{MA7}
$$

The ordinary sum cannot replace the asymptotic sum in these hypotheses without a further assumption.

**Proof.** First consider a point $y$ whose image belongs to both closed supports. The zero covector belongs to each $A_i$ there. Hence each $A_i$ at that point is contained in the relevant combined set, with its indicated sign. The combined noncharacteristic condition therefore makes each $F_i$ noncharacteristic at that point. This pointwise assertion persists on a neighborhood: normalize any hypothetical sequence of characteristic covectors at nearby basepoints to unit length and use compactness of the unit sphere and closedness of microsupport. We may use the noncharacteristic relative-trace isomorphism there.

Set $H=R\mathcal Hom(F_2,F_1)$. The characteristic Hom estimate `SH02-CHE-006` gives $\operatorname{SS}(H)\subset A_1\widehat+A_2^a$, so the same trace theorem applies to $H$. Extraordinary internal-Hom adjunction, valid without a finite-rank or dualizability hypothesis on $F_2$, gives

$$
\begin{aligned}
\omega_f\otimes f^{-1}H
&\xrightarrow{\sim}f^!H\\
&\simeq R\mathcal Hom(f^{-1}F_2,f^!F_1)\\
&\simeq R\mathcal Hom(f^{-1}F_2,\omega_f\otimes f^{-1}F_1)\\
&\simeq\omega_f\otimes R\mathcal Hom(f^{-1}F_2,f^{-1}F_1).
\end{aligned}
\tag{MA8}
$$

The last step uses only that $\omega_f$ is an invertible locally constant complex. Cancel it. Naturality of the evaluation map and the defining counit of relative trace identify the resulting arrow with (MA6): tensor the ordinary Hom pullback/evaluation square by $\omega_f$, and its two vertical arrows are exactly the two trace maps in (MA8).

For tensor, put $K=F_1\otimes^L F_2$. Its characteristic estimate is $\operatorname{SS}(K)\subset A_1\widehat+A_2$. Replace $f^!F_2$ by $\omega_f\otimes f^{-1}F_2$, commute the invertible line past the first factor using the symmetric monoidal constraint, and then apply trace for $K$. This gives (MA7). The trace is defined as the adjoint of projection formula followed by $Rf_!f^!\to\mathrm{id}$, so this composite is precisely the canonical tensor/exceptional-image comparison. This fixes its shifts and symmetry signs.

Finally, if $f(y)$ is outside either closed support, the corresponding complex vanishes on a neighborhood. Every term in (MA6) or (MA7) then vanishes there; exceptional inverse image is local on the base as well. These cases cover the points where the intermediate individual noncharacteristic argument is unavailable. $\square$

## SH02-MA-COVERING-KERNEL — A covering of a complement as a Hom kernel

Let $M\subset X$ be a closed submanifold, let $j:X\setminus M\hookrightarrow X$, and let $p:\widetilde X\to X\setminus M$ be a covering, with an arbitrary number of sheets. The bases retain the manifold conventions above; the covering space is locally compact Hausdorff and need not be second countable. Write $\rho=jp$ and define

$$
K_\rho=R\rho_!k_{\widetilde X},
\qquad \mathcal R_M(F)=R\rho_*\rho^{-1}F.
$$

There is a canonical identification

$$
\mathcal R_M(F)\simeq R\mathcal Hom(K_\rho,F).
\tag{MA9}
$$

Both sides are bounded under the conventions of this lesson. Furthermore,

$$
\operatorname{SS}(\mathcal R_M(F))
\subset\operatorname{SS}(F)\cup
\bigl(\operatorname{SS}(F)\widehat+T_M^*X\bigr).
\tag{MA10}
$$

**Proof of the kernel and its bound.** A covering is a local diffeomorphism. Its proper-support direct image is exact: locally on an evenly covered open set it is the direct sum over the sheets, and direct sums of modules are exact. Thus $K_\rho=j_!L$, where $L=p_!k_{\widetilde X}$ is the local system with fibre the free module $k^{(S)}$ on the set of sheets. This is a direct sum, even for an infinite covering. No finite-rank replacement has occurred.

The map $\rho$ is also a local diffeomorphism onto the open complement. Its relative orientation is canonically $k$ in degree zero, so $\rho^!=\rho^{-1}$. Internal-Hom/direct-image adjunction now gives

$$
R\mathcal Hom(R\rho_!k,F)
\simeq R\rho_*R\mathcal Hom(k,\rho^!F)
\simeq R\rho_*\rho^{-1}F,
$$

including the canonical map in (MA9). This adjunction is used in the locally compact Hausdorff six-operation range of exceptional operations: $\rho_!$ is exact, so its required finite cohomological dimension is zero. To prove boundedness without imposing countability on the covering space, use the identification with $R\mathcal Hom(K_\rho,F)$ on the original second-countable base $X$. The uniform bounded-Hom theorem `SH02-MD-BOUNDED-HOM` applies there to the degree-zero sheaf $K_\rho$ and the bounded complex $F$. Thus no cohomological-dimension theorem requiring a second-countable covering manifold has been invoked.

Away from $M$, $K_\rho$ is locally constant, so its microsupport is contained in the zero section. Near $M$, choose a product chart $B\times D$ with $M=B\times\{0\}$ and $B$ contractible. A covering of $B\times(D\setminus0)$ is pulled back from a covering of $D\setminus0$: lift the contraction of $B$ by the unique path-lifting property, separately on every sheet. The lift and its inverse depend continuously on points by the evenly covered neighborhoods, and give an isomorphism of coverings. Consequently $j_!L$ is constant in the $B$ direction. The product/submersion microsupport estimate, with no restriction on the normal factor, gives

$$
\operatorname{SS}(K_\rho)
\subset T_X^*X\cup T_M^*X.
\tag{MA11}
$$

If the codimension is zero, the complement is locally empty at points of $M$, and this conclusion holds directly. The right side of (MA11) is antipodally invariant. The characteristic Hom estimate applied to (MA9) yields (MA10): asymptotic sum distributes over a finite union by taking a subsequence, and asymptotic sum with the zero section is the original closed conic set. For the latter assertion the second covectors are zero, so convergence of the sum bounds the first covectors; closedness then gives exactly the original set. $\square$

## SH02-MA-COVERING-BASECHANGE — Transporting the covering construction

Let $f:Y\to X$ be transverse to $M$, set $N=f^{-1}M$, and use the pulled-back covering $\widetilde Y=\widetilde X\times_XY\to Y\setminus N$ to define $\mathcal R_N$. Suppose $f$ is noncharacteristic for both

$$
A=\operatorname{SS}(F)
\quad\hbox{and}\quad A\widehat+T_M^*X.
$$

Then the ordinary base-change arrow is an isomorphism

$$
f^{-1}\mathcal R_M(F)
\xrightarrow{\sim}\mathcal R_N(f^{-1}F).
\tag{MA12}
$$

**Proof.** Transversality makes $N$ a closed submanifold and supplies the asserted complement covering. Proper-support base change for the Cartesian square gives $f^{-1}K_\rho\simeq K_{\rho_Y}$. Alternatively, on evenly covered opens this is the identity on the same direct sum of copies of $k$, and extension by zero commutes with inverse image; this direct calculation works for every cardinality of the sheet set.

By (MA11), $A\widehat+\operatorname{SS}(K_\rho)^a$ lies in the union of the two sets for which noncharacteristicness was assumed. Apply (MA6) with $F_1=F$ and $F_2=K_\rho$, then use (MA9) on both sides. This proves (MA12). The identification of arrows can be checked before deriving: restricting an evaluation pairing from an evenly covered open set pulls back the same sections on each sheet. Adjunction and the proper-support base-change identity extend that square to resolutions. Its mate is the usual $f^{-1}R\rho_*\to R\rho_{Y*}f'^{-1}$ arrow. Thus the proof establishes the specified base-change morphism, without invoking ordinary base change for an arbitrary nonproper map. $\square$

## SH02-MA-NULL-DIRECTIONS — Involutivity can make a removed set invisible

On $X=\mathbb R^2$, use coordinates $(x,y;\xi,\eta)$ and put

$$
\Omega=\{\eta>0\},
\qquad
\Omega'=\Omega\setminus\{x\le0,\ \xi=0\}.
\tag{MA13}
$$

For every bounded $F$,

$$
\operatorname{SS}(F)\cap\Omega'=\varnothing
\quad\Longleftrightarrow\quad
\operatorname{SS}(F)\cap\Omega=\varnothing.
\tag{MA14}
$$

It follows that the restriction localization $\mathcal D_X(\Omega)\to\mathcal D_X(\Omega')$ is the identity quotient by the same thick null subcategory. In particular it induces an isomorphism on every Hom group.

**Proof.** Only the forward implication needs proof. The closed subset $S=\operatorname{SS}(F)\cap\Omega$ of $\Omega$ is involutive and is contained in $\{x\le0,\xi=0\}$. The smooth function $\xi$ vanishes on $S$. Hamiltonian invariance `SH02-INV-DEFINITION`, deduced from involutivity and the two-sided tangent-flow theorem, makes $S$ invariant under the full local trajectories of its Hamiltonian vector field. These trajectories translate $x$, with both time directions allowed, while fixing $y,\xi,\eta$. They remain in $\Omega$ for every finite time. A point with $x\le0$ therefore flows to one with $x>0$, contradicting the containment of $S$. Thus $S$ is empty. The quotient assertion follows from the definition `SH02-MC-LOCAL`, with no assumption that either quotient is a sheaf of categories. $\square$

## SH02-MA-FRACTIONS — One endomorphism group and two independent sectors

Take $F=k_{\{(0,0)\}}$. For the regions in (MA13),

$$
H^0R\Gamma(\Omega';\mu hom(F,F))\simeq k\oplus k,
\qquad
\operatorname{Hom}_{\mathcal D_X(\Omega')}(F,F)\simeq k.
\tag{MA15}
$$

Under these identifications the canonical comparison from localized morphisms to microlocal Hom sections is the diagonal map $k\to k\oplus k$.

**Proof of the sheaf calculation.** The submanifold-Hom identity identifies $\mu hom(k_{\{0\}},k_{\{0\}})$ with $\mu_{\{0\}}k_{\{0\}}$. Specialization leaves the vertex sheaf on the normal vector space, and its Fourier–Sato transform is the constant sheaf on the dual fibre, in degree zero. Thus

$$
\mu hom(F,F)\simeq k_{T_0^*X}.
$$

The fibre $T_0^*X$ meets $\Omega'$ in two components, $\{\eta>0,\xi>0\}$ and $\{\eta>0,\xi<0\}$. Both are convex and contractible. Ordinary degree-zero sections are an independent copy of $k$ on each, proving the first part of (MA15), including when $k=0$.

**Proof in the quotient.** Put $L=\{x=0\}$ and $P=k_{\{x=0,y\ge0\}}$. The restriction map $P\to F$ has cone $k_{\{x=0,y>0\}}[1]$. Along the open ray its microsupport has $\eta=0$; at the endpoint its open-half-line sign is $\eta\le0$. Hence this cone is invisible on $\Omega$, and $P\to F$ is an $\Omega$-denominator.

We claim $P$ is left orthogonal, in every degree, to the null category $\mathcal N_\Omega$. Let $C\in\mathcal N_\Omega$, so $\operatorname{SS}(C)\subset\{\eta\le0\}$, and let $i:L\hookrightarrow X$. The characteristic exceptional-inverse-image estimate gives $\operatorname{SS}(i^!C)\subset\{\eta\le0\}$ on the line. To verify this even in the presence of unbounded normal covectors, use the sequence formula for $i^\#$: its output is the limit of the $dy$ components of the input covectors, every one of which is nonpositive. The escaping normal $dx$ components cannot change this inequality.

Cone continuation on $L=\mathbb R_y$, with the cone $[0,\infty)$ and the convex open set $(-\infty,0)$, gives

$$
R\Gamma(\mathbb R;i^!C)\xrightarrow{\sim}
R\Gamma(( -\infty,0);i^!C).
$$

Its localization triangle says $R\Gamma_{[0,\infty)}(\mathbb R;i^!C)=0$. Therefore exceptional adjunction yields

$$
R\operatorname{Hom}_X(P,C)
\simeq R\operatorname{Hom}_L(k_{[0,\infty)},i^!C)=0.
\tag{MA16}
$$

Now use the outgoing-fraction formula `SH02-MC-LOCAL`. Each denominator $F\to F'$ has cone in $\mathcal N_\Omega$, so (MA16) makes $\operatorname{Hom}(P,F)\to\operatorname{Hom}(P,F')$ an isomorphism. Taking its filtered colimit proves

$$
\operatorname{Hom}_{\mathcal D_X(\Omega)}(F,F)
\simeq\operatorname{Hom}_{\mathcal D_X(\Omega)}(P,F)
\simeq\operatorname{Hom}_{D^b(k_X)}(P,F)
\simeq k.
$$

The last step is ordinary inverse-image/closed-direct-image adjunction at the point: the stalk of $P$ there is the free rank-one module $k$ in degree zero. Equation (MA14) gives the same group for $\Omega'$. Scalar multiples of the identity induce that scalar on both microlocal sectors. This proves the final statement and explicitly establishes the fraction calculation which a point-stalk theorem alone would not supply. $\square$

## SH02-MA-BENT-LINE — A coefficient model across a corner

Let

$$
Z=\{(x,0):x\ge0\}\cup\{(0,y):y\ge0\}\subset\mathbb R^2.
$$

If $\operatorname{SS}(F)\subset\operatorname{SS}(k_Z)$, then there is an arbitrary bounded complex of $k$-modules $M$ with

$$
F\simeq M_Z\quad\hbox{in }D^b(k_{\mathbb R^2}).
\tag{MA17}
$$

The conclusion is an ordinary derived isomorphism on the whole plane, although the support has a corner.

**Proof.** Set $h(x,y)=x-y$. Its restriction $h_Z:Z\to\mathbb R$ is a proper homeomorphism, with inverse $t\mapsto(\max(t,0),\max(-t,0))$. The two covectors $\pm dh=\pm(dx-dy)$ are absent from $\operatorname{SS}(k_Z)$ at every point of $Z$. Away from the corner this follows from the usual conormal formula for a straight line. At the corner, a $C^1$ function whose differential has positive $dx$ and negative $dy$ is strictly increasing on one short arm and strictly decreasing on the other. Its strict sublevel set on $Z$ is one half-interval. The support-test triangle has the restriction $k\to k$ as its middle map and therefore has zero supported cohomology. The inequalities remain strict in a neighborhood of the chosen covector, which proves absence from microsupport. Reversing both signs interchanges the arms and proves the assertion for the opposite covector as well.

The zero-section support criterion puts $\operatorname{supp}(F)\subset Z$. Thus $h$ is proper on that support. The proper direct-image estimate gives

$$
\operatorname{SS}(Rh_*F)\subset T_{\mathbb R}^*\mathbb R,
$$

because a nonzero output covector $\tau\,dt$ would have to lift to $\tau(dx-dy)$ in $\operatorname{SS}(F)$, which was excluded. A complex on the line with zero-section microsupport is globally constant: cone continuation for the cone $\mathbb R$ identifies its cone projector with itself, while that projector is the constant complex of its global cohomology. Equivalently, continuation on increasing intervals gives the evaluation isomorphism at every stalk. Put $M=R\Gamma(\mathbb R;Rh_*F)\in D^b(k)$.

Finally let $i:Z\hookrightarrow\mathbb R^2$. Closed-support equivalence gives $F\simeq i_*i^{-1}F$, and

$$
Rh_*F\simeq R(h_Z)_*i^{-1}F.
$$

The homeomorphism $h_Z$ has exact inverse image and direct image. Pulling its constant complex back gives $i^{-1}F\simeq M_Z$ as a sheaf on $Z$, and extending by zero proves (MA17). No finite-generation, orientability or constructibility input entered this argument. $\square$

## SH02-MA-GRAPH-STALK — Formal adjunctions have a graph-relative stalk

Let $f:Y\to X$ be arbitrary and smooth. In its cotangent correspondence set

$$
E_f=Y\times_XT^*X,
\quad p=(y_0;\xi_0),\quad x_0=f(y_0),
\quad p_X=(x_0;\xi_0),\quad p_Y=(y_0;df_{y_0}^t\xi_0).
$$

Write $a:X\times Y\to X$ and $q:X\times Y\to Y$ for the projections. The graph is identified on conormals by

$$
(y;\xi)\longmapsto(f(y),y;\xi,-df_y^t\xi).
$$

The two graph-relative Hom complexes, both written on $E_f$, are

$$
\begin{aligned}
\mathcal H_f^+(G,F)&=\mu_{\Gamma_f}R\mathcal Hom(q^{-1}G,a^!F),\\
\mathcal H_f^-(F,G)&=\alpha^{-1}\mu_{\Gamma_f}R\mathcal Hom(a^{-1}F,q^!G),
\end{aligned}
\tag{MA18}
$$

where $\alpha(y;\xi)=(y;-\xi)$. For the formal microlocal operations of `SH02-MC-FOUR`, there are canonical isomorphisms

$$
\begin{aligned}
\operatorname{Hom}(f_{!,p}^{\mu}G,F)
&\simeq\operatorname{Hom}(G,f_{\mu,p}^!F)
\simeq H^0(\mathcal H_f^+(G,F))_p,\\
\operatorname{Hom}(F,f_{*,p}^{\mu}G)
&\simeq\operatorname{Hom}(f_{\mu,p}^{-1}F,G)
\simeq H^0(\mathcal H_f^-(F,G))_p.
\end{aligned}
\tag{MA19}
$$

The Hom groups use the localized categories at $p_X,p_Y$ and their formal pro/ind conventions. No representability, properness, finite-rank or noncharacteristic hypothesis is imposed. The degree-zero cohomology symbol is necessary: the objects in (MA18) are derived sheaves. Shifting an input gives the corresponding graded identities.

**The map to be proved invertible.** The external-Hom estimate and the support estimate for microlocalization give

$$
\operatorname{supp}\mathcal H_f^\pm
\subset f_\pi^{-1}\operatorname{SS}(F)
\cap f_d^{-1}\operatorname{SS}(G).
\tag{MA20}
$$

For the positive kernel the ambient covectors lie in $\operatorname{SS}(F)\times\operatorname{SS}(G)^a$; graph conormal restriction gives (MA20). For the negative kernel they lie in $\operatorname{SS}(F)^a\times\operatorname{SS}(G)$, and the antipode in (MA18) changes the signs back. Exactness and this bound show that the stalk at $p$ inverts a denominator in either input.

Graph recovery and ordinary adjunction define maps

$$
\begin{aligned}
\operatorname{Hom}(Rf_!G,F)&\longrightarrow H^0(\mathcal H_f^+(G,F))_p,\\
\operatorname{Hom}(f^{-1}F,G)&\longrightarrow H^0(\mathcal H_f^-(F,G))_p.
\end{aligned}
\tag{MA21}
$$

They take a local-cohomology class supported on the graph to its class on larger admissible supports in the microlocalization stalk formula. Since (MA20) inverts denominators, these maps extend to

$$
\begin{aligned}
L_+(G,F)&=\operatorname*{colim}_{G'\to G}
\operatorname*{colim}_{F\to F'}\operatorname{Hom}(Rf_!G',F'),\\
L_-(F,G)&=\operatorname*{colim}_{F'\to F}
\operatorname*{colim}_{G\to G'}\operatorname{Hom}(f^{-1}F',G').
\end{aligned}
\tag{MA22}
$$

Every indexing arrow is a denominator at its specified point. Expansion of the formal operations identifies (MA22) with the first two terms of (MA19); ordinary adjunction and interchange of the two filtered colimits give their mutual identification. It remains to prove bijectivity with the graph stalk. The following two sections supply both existence and the zero criterion.

## SH02-MA-GRAPH-CONES — The two opposite wedge calculations

Work in base charts, extending restricted inputs by zero when necessary; restriction to each chart is a denominator. Graph coordinates

$$
(x,y)\longmapsto(z,y)=(x-f(y),y)
$$

straighten the graph for every $f$, regardless of its rank. Choose relatively compact neighborhoods $U\ni x_0$, $V\ni y_0$, with $U$ convex and $f(\overline V)\subset U$. Such pairs are cofinal among product neighborhoods. Let $\gamma$ be a closed proper convex cone in the target chart with

$$
\gamma\subset\{z:\langle z,\xi_0\rangle<0\}\cup\{0\}.
\tag{MA23}
$$

Use the wedges

$$
Z_\gamma^+=\{(x,y):f(y)-x\in\gamma\},
\qquad Z_\gamma^-=\{(x,y):x-f(y)\in\gamma\}.
\tag{MA24}
$$

The first wedge has its nonzero normal directions strictly positive against $p$; the second has them strictly positive against $-p$. This is exactly the antipodal distinction in (MA18).

These wedges are cofinal for the microlocalization support-stalk formula `SH02-MH-TESTS`. Indeed the unit directions of an admissible normal cone at the basepoint are compact and lie in the required strict halfspace. Enlarge them slightly to a closed convex cone still in that halfspace. After shrinking the base neighborhoods, the admissible support lies in its wedge: otherwise normalized offending graph-normal secants would converge to a forbidden normal vector. Conversely each wedge is admissible. The center point used for each secant is $(0,y)$ in graph coordinates, so this argument uses the actual graph and does not replace $f$ by its derivative. Common cone enlargements and neighborhood shrinkings give a filtered system. If $\xi_0=0$, the normal cone must have no nonzero direction. The same normalized-secant argument then forces the support into the graph near the point. The zero cone $\gamma=\{0\}$ is cofinal in that case.

Let $D_\gamma=\phi_\gamma^{-1}R\phi_{\gamma*}$ be the ordinary cone projector. The elementary cutoff gives a denominator

$$
A_{U,\gamma}(H):=(D_\gamma H_U)_U\longrightarrow H
\quad\hbox{at }p_X.
\tag{MA25}
$$

For $\xi_0\ne0$, (MA23) places $\xi_0$ in the interior of $\gamma^{\circ a}$; for the zero cone (MA25) is ordinary neighborhood restriction.

For the positive graph complex, put $H_V=Rf_!(G_V)$. Its closed support is contained in the compact set $f(\overline V)\subset U$. The support-stalk formula and $Ra_!\dashv a^!$ give

$$
H^0(\mathcal H_f^+(G,F))_p
\simeq\operatorname*{colim}_{U,V,\gamma}
\operatorname{Hom}((D_\gamma H_V)_U,F).
\tag{MA26}
$$

Here is the precise kernel verification. Moving the support $Z_\gamma^+$ into the first Hom argument changes the local-cohomology group on $U\times V$ into the Hom out of

$$
Ra_!\bigl((q^{-1}G_V)_{Z_\gamma^+}\bigr)|_U.
$$

The closed support is contained in $X\times\overline V$, so $a$ is proper on it. Hence ordinary and proper-support direct image agree on this kernel. The cone-projector kernel is $\{(x',x):x'-x\in\gamma\}$. Composing it with $Rf_!G_V$ substitutes $x'=f(y)$, by proper-support base change and projection formula, and gives exactly $Z_\gamma^+$. This proves (MA26). Because $H_V$ is supported in $U$, its first argument is the actual cutoff $A_{U,\gamma}(H_V)$ in (MA25). Restriction of the wedge to the graph is that cutoff map, followed when needed by $Rf_!G_V\to Rf_!G$.

For the negative graph complex the other adjunction, $Rq_!\dashv q^!$, gives

$$
H^0(\mathcal H_f^-(F,G))_p
\simeq\operatorname*{colim}_{U,V,\gamma}
\operatorname{Hom}((f^{-1}D_\gamma F_U)_V,G).
\tag{MA27}
$$

This time the integrated variable is $x$. Its closed support lies in $\overline U\times Y$, so the projection $q$ is proper on that support. Pulling back the target cone kernel $\{x-x'\in\gamma\}$ along $x'=f(y)$ gives exactly $Z_\gamma^-$. Ordinary proper base change therefore identifies the integrated kernel with $f^{-1}D_\gamma F_U$. This argument works for characteristic maps as well, because the specific kernel projection just proved proper is the one to which base change is applied. The orientation present in $q^!G$ is used in that adjunction and leaves no additional shift in (MA27).

Since $f(V)\subset U$, the first argument of (MA27) is also $(f^{-1}A_{U,\gamma}(F))_V$. The map induced by restriction from the wedge to the graph is

$$
(f^{-1}A_{U,\gamma}(F))_V
\longrightarrow f^{-1}A_{U,\gamma}(F)
\longrightarrow f^{-1}F.
\tag{MA28}
$$

Only its first arrow is being asserted to be a $p_Y$-denominator automatically. Its second arrow is the inverse image of a $p_X$-denominator; no assertion that arbitrary inverse image preserves denominators is used. These kernel-restriction descriptions identify (MA26) and (MA27) with the canonical maps (MA21), including their signs.

## SH02-MA-GRAPH-FRACTIONS — Surjectivity and denominator clearing

**The positive graph stalk.** A class in (MA26) is an ordinary arrow $(D_\gamma H_V)_U\to F$. Invert the cutoff denominator to get a localized arrow $H_V\to F$ at $p_X$. The neighborhood restriction $G_V\to G$ is a denominator at $p_Y$, so this arrow defines an element of $L_+(G,F)$. If an ordinary double-fraction representative as in (MA22) is desired, use the outgoing fraction calculus for its target. Kernel restriction in (MA26) shows that its graph-stalk image is the original class. This proves surjectivity.

For injectivity take a class represented by $b:Rf_!G'\to F'$ in (MA22). If its graph-stalk image vanishes, (MA20) lets us test vanishing using the pair $(G',F')$ itself. The filtered-colimit zero criterion in (MA26) gives $U,V,\gamma$ such that

$$
(D_\gamma Rf_!G'_V)_U\longrightarrow Rf_!G'_V
\longrightarrow Rf_!G'\xrightarrow{b}F'
$$

is zero. The first arrow is a $p_X$-denominator, so the last two arrows already compose to zero in the localized target category. Refining the original incoming denominator by $G'_V\to G'$ kills the original element in the formal colimit. This proves injectivity without asserting that base neighborhoods alone are cofinal among all microlocal denominators.

**The negative graph stalk.** A representative of (MA27) is an ordinary arrow $(f^{-1}A_{U,\gamma}(F))_V\to G$. Invert its neighborhood restriction to get a localized arrow $f^{-1}A_{U,\gamma}(F)\to G$ at $p_Y$. The incoming denominator $A_{U,\gamma}(F)\to F$ at $p_X$ now makes this an element of $L_-(F,G)$. Formula (MA28) identifies its graph-stalk image with the original representative, proving surjectivity.

If a double-fraction representative $b:f^{-1}F'\to G'$ has zero graph-stalk image, first use (MA20) to pass to $(F',G')$. The zero criterion in (MA27) supplies $U,V,\gamma$ for which

$$
(f^{-1}A_{U,\gamma}(F'))_V
\longrightarrow f^{-1}A_{U,\gamma}(F')
\longrightarrow f^{-1}F'\xrightarrow b G'
$$

is zero. The first arrow is a $p_Y$-denominator; hence the remaining composite is zero in the localized category on $Y$. Refining the incoming denominator by $A_{U,\gamma}(F')\to F'$ kills the original element in $L_-(F,G)$. This proves injectivity. Both isomorphisms in (MA19) are established for their canonical maps. $\square$

For a check involving a nontrivial dimension shift, take $f:\mathbb R\to\{*\}$, $G=k_{\mathbb R}$ and $F=k$. The positive graph object is $k_{\mathbb R}[1]$, and its degree-zero stalk is zero. The negative one is $k_{\mathbb R}$, with stalk $k$. The formal neighborhood calculations give $R\Gamma_c(V;k)=k[-1]$ for the positive direct image and $R\Gamma(V;k)=k$ for the negative one. Their Hom groups are respectively zero and $k$, agreeing with (MA19). For $f=\mathrm{id}$, the formulas reduce to the ordinary single-covector microlocal Hom theorem.

## SH02-MA-ONE-SIDED-CURVATURE — A flat arm can create a full limiting fibre

For $1<r<2$, set $g(t)=0$ for $t\le0$ and $g(t)=t^r$ for $t\ge0$. Its graph $Z\subset\mathbb R^2$ is a $C^1$ submanifold, and its conormal bundle is the closed conic set

$$
A=\{(t,g(t);-g'(t)\lambda,\lambda):t,\lambda\in\mathbb R\}.
$$

In the given smooth coordinates its asymptotic self-sum is

$$
A\widehat+A=A\cup T_0^*\mathbb R^2.
\tag{MA29}
$$

This is the version with one flat arm. The symmetric two-curved-arm example and the resulting failure of $C^1$ coordinate invariance are proved in `SH02-CHE-REGULARITY`; that different graph is not substituted for this one.

**Proof.** For any prescribed fibre covector $(c,d)$ at the origin, choose $t_n>0$ tending to zero and put $a_n=rt_n^{r-1}$, $\lambda_n=-c/a_n$, $\mu_n=d-\lambda_n$. Take the conormal covectors with these respective normal coefficients at the graph points $(t_n,g(t_n))$ and $(0,0)$. Their sum is exactly $(c,d)$. The distance between the two basepoints is $O(t_n)$, while the first covector has norm $O(t_n^{1-r})$ when $c\ne0$. Thus their weighted separation is $O(t_n^{2-r})\to0$. For $c=0$ the first covector is zero and the condition holds directly. This proves $T_0^*\mathbb R^2\subset A\widehat+A$.

No limiting covector can have its base off the closed graph. At any nonzero graph parameter $t_0$, the derivative $g'$ is locally Lipschitz. Suppose two conormal covectors at $u_n,v_n\to t_0$, with coefficients $\lambda_n,\mu_n$, have a convergent sum with second component $d$. Their first component is

$$
-g'(v_n)(\lambda_n+\mu_n)
+(g'(v_n)-g'(u_n))\lambda_n.
$$

The second term tends to zero by the Lipschitz bound and the weighted-separation condition. The first tends to $-g'(t_0)d$, so the limit is conormal. Finally $A\subset A\widehat+A$ by using the same basepoint twice and taking zero as one input. These inclusions prove (MA29). At $r=2$, the derivative is locally Lipschitz even at zero, and the exclusion argument applies there too: the self-sum is then just $A$. $\square$

## SH02-MA-APPLICATION-PROBLEMS — Further calculations with solutions

**Problem 1: change the angle.** Let $v,w\in\mathbb R^2$ be linearly independent, and let $Z_{v,w}=\mathbb R_{\ge0}v\cup\mathbb R_{\ge0}w$. Prove the counterpart of (MA17) for a bounded complex whose microsupport lies in that of $k_{Z_{v,w}}$.

*Solution.* Choose a linear functional $\ell$ with $\ell(v)=1$ and $\ell(w)=-1$. It is proper and a homeomorphism from $Z_{v,w}$ to the line. At the vertex, a covector near $d\ell$ has opposite strict signs on the two arms; its support test again has one contractible strict sublevel arm and restriction $k\to k$. The same holds near $-d\ell$. The proper direct-image argument in `SH02-MA-BENT-LINE` therefore gives a constant complex on the line and then a constant coefficient complex on $Z_{v,w}$. This includes, for example, $v=(2,1)$ and $w=(-1,3)$, with no preferred Euclidean angle.

**Problem 2: infinitely many sheets.** Let $U\subset X\setminus M$ be an evenly covered contractible open set, with sheet set $S$. For a constant coefficient complex $Q$ on $U$, compute $K_\rho|_U$ and $\mathcal R_M(Q)|_U$. Explain why the two coefficient operations are different.

*Solution.* The proper-support kernel is $(k^{(S)})_U$. Its Hom into $Q_U$ is $(\prod_{s\in S}Q)_U$ on this trivializing domain: a map from a free direct sum is an independently specified value on every basis vector. The same result follows by taking the covering direct image of the pullback of $Q$. The proper-support construction sums over sheets, while its right-adjoint Hom construction takes products. Since products of modules are exact, a termwise product of a bounded representative computes this particular constant-coefficient example. The distinction persists when $S$ is countably infinite.

**Problem 3: the missing scalar comparison.** In (MA15), which microlocal section is not induced by any localized endomorphism when $k\ne0$?

*Solution.* The section which is $1$ on the sector $\xi>0$ and $0$ on $\xi<0$ is not diagonal. Every localized endomorphism is a scalar by the half-ray fraction calculation, and its restrictions to both sectors are that same scalar. The section is therefore absent from the image. This is a failure of surjectivity for the comparison on the open set, even though the comparison at each individual covector is an isomorphism.

**Problem 4: why combined noncharacteristicness is local to common support.** Suppose $F_1$ is zero near $f(y)$, while $F_2$ is characteristic there. Does (MA6) require a separate noncharacteristic assumption on $F_2$ at $y$?

*Solution.* No. Both internal Hom complexes vanish near $y$, since their second argument is zero. The proof of (MA6) invokes individual noncharacteristicness only at points of the common closed support, where the zero covectors of both factors put each relevant individual microsupport inside the combined set. Requiring individual conditions everywhere would add an unnecessary restriction.

## SH02-MA-BOUNDARY — Dependencies and further directions

The proofs above are complete relative to the named cone-continuation, six-operation, characteristic-estimate, microlocal-Hom and involutivity contracts. The calculations distinguish ordinary neighborhoods, directions in a cotangent fibre, and quotient-category denominators; each controls a different limit or localization.

The graph-relative calculation includes the actual cone-stalk formulas and denominator-clearing arguments, separately from the formal adjunction identities. The quadratic tangent-cone counterexample is the $m=1$ member of the full even-power family proved in `SH02-INV-POINT-TANGENT-FAILURE`, so its calculation is not duplicated here. The flat-arm asymptotic-sum calculation above supplies the exact geometry complementary to `SH02-CHE-REGULARITY`.

A next research calculation is to replace the two deleted sectors in (MA13) by several components and determine which compatibility conditions are imposed by involutivity before computing any quotient morphisms. Another is to replace the proper bent-line projection by a curve whose projection has a noncompact fibre: the proof then exposes exactly where a new properness or support hypothesis is needed.
